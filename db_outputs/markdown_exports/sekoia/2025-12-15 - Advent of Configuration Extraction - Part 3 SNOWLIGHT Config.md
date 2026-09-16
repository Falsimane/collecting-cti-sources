# Advent of Configuration Extraction - Part 3: SNOWLIGHT Config

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/advent-of-configuration-extraction-part-3-mapping-got-plt-and-disassembling-the-snowlight-loader
- **Date :** 2025-12-15

---

In the third part of our series “Advent of Configuration Extraction”, we dissect **SNOWLIGHT** , a lightweight ELF downloader designed to retrieve and execute a remote payload on Linux systems. 

To extract the SNOWLIGHT configuration, and specifically the Command and Control (C2) port, we need to disassemble the main function and identify calls to dynamically imported functions based on their addresses. This requires resolving the mapping between the **Global Offset Table** and the **Procedure Linkage Table** , which allows us to associate each entry with the name of the imported function.

To perform this step reliably and automatically, the extractor relies on two powerful tools: **LIEF** for parsing the ELF format, and **Capstone** for disassembling the machine code.

## SNOWLIGHT

**SNOWLIGHT** is the identifier assigned by [Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/initial-access-brokers-exploit-f5-screenconnect?hl=en) to a lightweight ELF downloader designed to retrieve and execute a remote payload on Linux systems. Developed in C and measuring less than 10 KiloBytes, SNOWLIGHT communicates with its Command and Control server over a raw TCP socket, using a port that varies across samples. 

Its initial action is to transmit a 6 bytes message to the C2, containing a short architecture pattern followed by padding. This pattern consists of a single letter indicating the processor family, **i** for Intel and **a** for ARM, followed by the architecture size 32 or 64 bits, resulting in one of the following values: l32, l64, a32 or a64.The server responds with a XOR-encoded payload, currently using the hardcoded key **0x99**. SNOWLIGHT then decodes the payload and executes it entirely in memory through the memfd_create and fexecve system calls, leaving no artifacts on the disk.

Early variants observed from August 2025 also include an access check on the file located at /tmp/log_de.log and terminate if this file is not accessible. Recent reporting indicates that SNOWLIGHT has been incorporated into intrusion campaigns attributed to the threat actor **UNC5174** , where it serves as an in-memory loader for the remote access trojan the [**VShell**](https://www.sysdig.com/blog/unc5174-chinese-threat-actor-vshell).

### Snowlight Configuration Access Logic

To build the configuration extractor, an initial manual analysis of several samples is required to understand how the malware accesses and parses its configuration. 

For this study, a static analysis was performed on the following sample: SHA-256: 344c391cfd4fd30407bf55872d05d44b679a117e407114c0e113b3c6c4cbbb29

SNOWLIGHT sample analysis was compiled with intact symbols and showed no signs of obfuscation. Because SNOWLIGHT is a downloader, the primary piece of information to extract from its configuration is the C2 server address, which the malware contacts to send an architecture identifier and retrieve the next stage. In our analysis, the extractor targets the x86_64 version. 

The SNOWLIGHT binary contains the main function, where the malware initialises a sockaddr_in structure holding the C2 address. The IP is stored directly in the section and copied into the structure before the call to gethostbyname. The assembly analysis also shows that the TCP port is explicitly set via the following instruction:

`mov word ptr [addr.sa_data], 811Fh // <- sin_port  
call _gethostbyname  
`

 _Code 1. Instruction preceding gethostbyname function_

This value, stored in little‑endian format, corresponds to port **8065**. The subsequent call to gethostbyname is used solely to resolve the IP address or domain name that has already been loaded into the structure.

Extraction of the configuration begins by parsing the section to locate the C2 address. In all samples analysed, the C2 value consistently appears immediately after the string "[kworker/0:2]". The section also contains the architecture identifier (the _magic_ value), which in this case is "l64", as the sample is an **x86_64** executable.

To obtain the port number, the extractor iterates over the instructions of the function main to identify the call to gethostbyname. The instruction immediately preceding this call contains the port value stored in the sockaddr_in structure. To locate the gethostbyname call, the extractor must resolve the mapping between the **Global Offset Table (GOT)** and the **Procedure Linkage Table (PLT)**. The GOT is a table of addresses used by the program to reference dynamically linked functions, while the PLT contains the actual code that jumps to these functions at runtime. Resolving the mapping between the GOT and PLT is essential to associate each PLT entry with its corresponding imported function name, including gethostbyname.

## Automating the Configuration Extraction

To perform the operations required for configuration extraction (parsing .rodata, resolving GOT/PLT, and disassembling), we rely on two tools: **LIEF** and **Capstone**.

[**LIEF**](https://lief.re/) is a cross‑platform library designed for parsing, modifying, and abstracting executable formats such as ELF, PE, and Mach‑O. It provides programmatic access to low‑level binary structures, including headers, sections, symbols, and relocation tables. LIEF is commonly used in malware analysis, reverse engineering, and binary instrumentation because it can accurately reconstruct internal metadata and allows controlled modifications without breaking binary integrity.

[**Capstone**](https://www.capstone-engine.org/) is a lightweight, multi‑architecture disassembly engine that converts raw machine code into human‑readable assembly instructions. It supports detailed operand information, multiple instruction sets, and configurable analysis modes, making it suitable for static analysis, emulation frameworks, and security tooling. Capstone is valued for its speed, reliability, and consistent API, enabling analysts to inspect execution flows across CPUs such as x86, ARM, MIPS, and more.

### Hunting the SNOWLIGHT C2 Inside .rodata

LIEF enables enumeration and inspection of the sections of an ELF binary. Using lief.parse(), the executable is loaded into an object model that exposes its internal structure. The sections are then iterated over via self.elf.sections to locate the section, identified through sec.fullname.startswith(b".rodata"). Once located, the raw contents is accessed through sec.content.

The data in.rodata is subsequently split using the \x00 delimiter to produce a list of pseudo string‑like patterns. Iterating through this list, allows identification of the marker string "[kworker/0:2]", which is consistently parent across all analysed samples. The C2 value is stored immediately following this marker.

The following code implements this extraction logic described above.

`c2 = None  
elf = lief.parse(binary_path)  
for sec in elf.sections:  
if sec.name.startswith(".rodata"):  
data = bytearray(sec.content)  
patterns = list(filter(None, data.split(b"\x00")))  
for i, p in enumerate(patterns):  
if p == b"[kworker/0:2]" and i + 1 < len(patterns):  
c2 = patterns[i + 1].decode()  
break  
if c2:  
print(f"C2 found: {c2}")  
else:  
print("C2 not found")  
`

_Code 2. Python snippet to extract the C2 string that consistently follow kworker marker_.

### Reconstructing Dynamic Calls via GOT and PLT Resolution

Once the C2 address has been extracted from the section, the next step is to recover the port used by the malware. This requires locating the call to gethostbyname within the disassembled main function. Because the binary relies on dynamic linking, the function’s effective address cannot be known statically; it must be resolved by reconstructing the relationship between the GOT and the PLT.

Using LIEF, this mapping can be rebuilt by inspecting the PLT-GOT relocations exposed through the elf.pltgot_relocations interface. Each relocation provides both the GOT-slot address (rel.address) and the associated imported symbol (rel.symbol.name). From these entries, we build a **GOT-slot map** , allowing us to determine which dynamic function is referenced at a given GOT address.

Subsequently, the section is analysed to compute the virtual address of each PLT stub,creating a **PLT-entry map** that associates each PLT thunk with the corresponding function name. This process relies on the regular layout of PLT entries (_e.g._ : 16-byte alignment on x86_64) and uses the symbol names also obtained from rel.symbol.name.

Together, these two maps allow us to identify the exact virtual address of the PLT call to gethostbyname.

`def resolve_gotplt(elf: lief.ELF.Binary) -> tuple[dict, dict]:  
"""  
Resolve GOT/PLT mappings using LIEF:  
- Build GOT map: GOT-slot VA → symbol.name  
- Build PLT map: PLT-entry VA → symbol.name  
Returns (got_map, plt_map)  
"""  
got_map = {}  
plt_map = {}  
  
# --- 1. Build GOT map using pltgot_relocations ---  
for rel in elf.pltgot_relocations:  
symname = rel.symbol.name if rel.symbol else "<no-name>"  
got_map[rel.address] = symname  
  
# --- 2. Build PLT map by computing PLT entry VAs ---  
plt_sec = elf.get_section(".plt")  
if plt_sec and len(elf.pltgot_relocations) > 0:  
plt_va = plt_sec.virtual_address  
plt_size = plt_sec.size  
  
# x86_64: PLT0 = 16 bytes, each following entry = 16 bytes  
PLT0_SZ = 16  
nentries = len(elf.pltgot_relocations)  
entry_sz = (plt_size - PLT0_SZ) // nentries  
  
for idx, rel in enumerate(elf.pltgot_relocations):  
entry_addr = plt_va + PLT0_SZ + idx * entry_sz  
plt_map[entry_addr] = rel.symbol.name  
  
return got_map, plt_map  
`

 _Code 3. Python snippet to rebuild the GOT and PLT using LIEF_.

### Tracing SNOWLIGHT’s Network Setup in Assembly

To recover the C2 port, the main function must be analysed. The first step consists of identifying its address. LIEF exposes all exported symbols through the exported_functions attribute, which makes it possible to locate the entry point of the main function directly. Once the virtual address of main is known, the raw bytes corresponding to this function can be extracted by combining the section_from_virtual_address() method and the section’s virtual_address, allowing to compute both the buffer to disassemble and its correct offset.

Capstone is then used to disassemble only the content of the main function. The disassembler must be initialised according to the architecture of the ELF file, which can be obtained from elf.header.machine_type. In the SNOWLIGHT samples analysed, this value corresponds to x86_64, so Capstone is configured with CS_ARCH_X86 and CS_MODE_64. Capstone’s disasm() method takes raw bytes and a virtual address as input and returns objects that expose the decoded instruction through the mnemonic object and the operand string via op_str. Operands are typed, and Capstone provides convenient enums to interpret them.

`from capstone import *  
from capstone.x86 import *  
import lief  
  
binary = lief.parse('/path/to/binary')  
text = binary.get_section(".text")  
text_base = text.virtual_address  
  
# INIT CAPSTONE  
md = Cs(CS_ARCH_X86, CS_MODE_32) # adjust according to the architecture  
md.detail = True # enable access to operands, registers, etc.  
  
# Disassemble the .text section and store instructions in a list for easy indexing  
instructions = list(md.disasm(bytes(text.content), text_base))  
  
# Iterate over instructions with index  
for idx, instr in enumerate(instructions):  
if instr.id == X86_INS_CALL:  
print(f"Call instruction found @0x{instr.address:x} - operand {instr.op_str}")  
  
# Print previous instruction if it exists  
if idx > 0:  
prev = instructions[idx - 1]  
print(f"Previous instruction: 0x{prev.address:x} {prev.mnemonic} {prev.op_str}")  
else:  
print("No previous instruction")  
`

_Code 4. Python snippet to disassemble the .text section and print each CALL instruction along with its previous instruction_.

As only the main function is interesting for the extraction, the decompilation starts from its prologue address (obtained previously) and stops when encountering X86_INS_RET instruction. This constant is provided by Capstone and corresponds to the assembly ret instruction, marking the epilogue of a function. Once this boundary is reached, we have reconstructed the full list of instructions belonging to the main function.

With the full list of instructions belonging to the main function, the final step consists of iterating through this sequence to identify how the malware sets the C2 port. The logic relies on detecting the call to gethostbyname, which is resolved dynamically at runtime. During iteration, we look for instructions whose ID is X86_INS_CALL. Capstone allows inspection of each operand, and we specifically check whether the operand type is X86_OP_IMM, meaning the call targets an immediate address rather than a register or memory operand.

The immediate value extracted from the call instruction corresponds to the PLT entry address. This address is then checked against the previously constructed PLT map. If the resolved symbol name matches gethostbyname, the address and instruction is saved for port retrieval.

Once the call to gethostbyname is identified, the extractor reads the instruction preceding the gethostbyname. The port is stored in the sin_port member of the sockaddr_in structure of that particular instruction because this is how the downloader is developed. This instruction contains an operand of type X86_OP_IMM, the immediate value represents the hard‑coded port in **network byte order**. To obtain the integer port number, we convert this value using htons and restores it to the host byte order. This yields the final TCP port used by SNOWLIGHT to communicate with its C2 server.

The full [SNOWLIGHT extractor](https://github.com/SEKOIA-IO/Community/blob/main/Configuration_extractors/SNOWLIGHT.py) code is available in the Sekoia.io community [Git repository](https://github.com/SEKOIA-IO/Community/tree/main/Configuration_extractors).

## Final words

The final phase of the extraction process consists of correlating the disassembled instructions with the dynamically resolved function addresses and recovering the hard‑coded C2 port used by SNOWLIGHT. By combining precise GOT/PLT resolution through LIEF with Capstone’s instruction level analysis, the call to gethostbyname can be reliably identified, allowing extraction of the immediate value that defines the malware’s network port. A clearly structured strategy during the design stage - separating .rodata parsing, ELF inspection, PLT/GOT mapping, and final disassembly - significantly accelerates extractor development and reduces ambiguity when dealing with dynamically linked ELF binaries.

Although this workflow is tailored to SNOWLIGHT’s current implementation, the methodology naturally generalises to other ELF‑based downloaders and lightweight loaders that embed static C2 endpoints and rely on standard libc APIs. Its modular architecture, leveraging LIEF for structural analysis and Capstone for instruction‑level reasoning, facilitates rapid adaptation to new variants, whether changes appear in symbol layout, compiler optimisations, calling conventions, or minor control‑flow adjustments. While heavily packed or obfuscated ELF samples may require complementary techniques, the approach presented here provides a robust and repeatable foundation for extracting configuration data from the majority of real‑world SNOWLIGHT samples observed in the wild.