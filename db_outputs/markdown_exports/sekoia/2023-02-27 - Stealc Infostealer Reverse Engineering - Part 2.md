# Stealc Infostealer: Reverse Engineering - Part 2

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-2
- **Date :** 2023-02-27

---

## Context

This report is a follow up of the [previous blog post](/blog/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-1) on Stealc. Stealc is an information stealer advertised on the underground forums XSS, Exploit and BHF by the _Plymouth_ threat actor. In this blog post, we focus on the technical analysis of a standalone sample. Similarities were observed with Vidar, Raccoon and Mars stealers during the reverse engineering phase.

Functionalities implemented in Stealc, including environment detection, anti-analysis, strings obfuscation, dynamic API resolution, a significant list of targeted browsers, extensions, wallets and installed software makes it a top-tier threat within the infostealer ecosystem. 

## Malware analysis

The next sections list the different techniques observed during the reverse engineering of Stealc to provide information and detailed explanations on Stealc operations and behaviors. 

 _All details of the infection chain, distribution and tracking of this threat were provided in_[ _part 1_](/blog/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-1) _._

Stealc sample SHA-256 used for the analysis is: [77d6f1914af6caf909fa2a246fcec05f500f79dd56e5d0d466d55924695c702d](https://bazaar.abuse.ch/sample/77d6f1914af6caf909fa2a246fcec05f500f79dd56e5d0d466d55924695c702d/)

Stealc sample SHA-256 with a next stage configured is: [1587857ad744c322a2b32731cdd48d98eac13f8aa8ff2f2afb01ebba88d15359](https://bazaar.abuse.ch/sample/1587857ad744c322a2b32731cdd48d98eac13f8aa8ff2f2afb01ebba88d15359/)

### Anti analysis

The malware implements anti-analysis techniques by adding unconditional jump to a nearby offset, confusing the decompiler that cannot grasp the pointed function. 

As shown in figure 1, the decompiler analyzed a function with multiple jump instructions (jz, jnz opcodes), with a destination address defined to the next address plus an offset of 1 or 2 (depending on the case). This results in the decompiler not making a correct assumption and avoiding decompiling the function. 

![Wrong disassembly of the main function due to Stealc implemented anti-analysis technique. 
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd597_6a92a421dc3071123832fe05_6a2a7a2bcf15f12139bf3e9f.webp)

Figure 1. Wrong disassembly of the main function due to Stealc implemented anti-analysis technique. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


Rebuilding the function by setting the location to undefined and patching the previous byte of the location with a NOP instruction, decompilers can work properly. When applying this technique, the decompiled opcodes are the following:

![Patched function that can be correctly decompiled by IDA.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd591_6a92a420dae089660dfd1ce3_6a2a7a2bcf15f12139bf3e9c.webp)

Figure 2. Patched function that can be correctly decompiled by IDA. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


Here, the instructions mov eax, 9DE9h (B8 E8 9D 00 00) are wrongly disassembled because of the location+1. Undefining the location, replacing the B8 of the mov instruction by a NOP(0x90) and re-defining the beginning of the next instruction to E8 results in the correct disassembly of this code section. 

![Jump in the middle trick patching example.
Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd58e_6a92a41ddae089660dfd1aba_6a2a7a2acf15f12139bf3e90.webp)

Figure 3. Jump in the middle trick patching example. Source: Sekoia  


### Main function overview

Following the patching of the sample, the main function of **Stealc** shows similarities to the one analyzed in [**Raccoon**](/blog/raccoon-stealer-v2-part-2-in-depth-analysis) and [**Mars**](/blog/mars-a-red-hot-information-stealer)**stealers** reverses, notably in terms of operation order and used techniques.

![Main function overview of Stealc infostealer.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd5a9_6a92a42616f788fda8e503d7_6a2a7a2bcf15f12139bf3eae.webp)

Figure 4. Main function overview of Stealc infostealer. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


The execution flow of Stealc is straightforward, it first deobfuscates strings used for further dynamic API resolution. Then, it performs various checks on the infected host to exit on particular conditions, it also checks the amount of RAM and whether it is executed by an antivirus solution. 

Finally, it verifies that the current date is preceding the hardcoded one.

After this initial setup and detection, the malware goes to the function responsible for the C2 interaction, in which the stealer configuration is downloaded, and data are exfiltrated.

### Defeating string encryption

The malware stores its strings and part of its configuration is obfuscated. Stealc data are **RC4** -encrypted and **base64** -encoded. The key for decryption is stored in the PE in cleartext, as seen in the first variable assignment in figure 5.

![Base64 decoding and RC4 decryption function.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd5a0_6a92a425e17eff730b65c193_6a2a7a2bcf15f12139bf3eab.webp)

Figure 5. Base64 decoding and RC4 decryption function. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


_For further analysis, an IDA script to decrypt the strings and assign their value to the correct DWORD is provided in annex 2._

### Dynamic API resolution

To reduce its detection rate by antivirus solutions, Stealc uses the Dynamic API Resolution (T1027.007) technique. To do so, the malware searches for the _kernel32_ base address using the PE header structure and goes through LDR_DATA_TABLE_ENTRY. Then, it iterates over the table until it matches the GetProcAddress function and returns the address of the dedicated entry.

![Debugging of the search GetProcAddess of Kernel32.dll.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd59d_6a92a41e2b0ef7af46bd55a4_6a2a7a2acf15f12139bf3e93.webp)

Figure 6. Debugging of the search GetProcAddess of Kernel32.dll. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


In figure 6, register EAX is used to store _kernel32_ base address:

  1. Register fs:000030h is the address of the [ProcessEnvironmentBlock](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb) (PEB) member of the [ThreadEnvironmentBlock](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-teb) (TEB) structure ;
  2. The offset 0xC of the PEB structure is the [LDR_DATA](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb_ldr_data) structure member that contains a pointer to the InMemoryOrderModuleList member;
  3. InMemoryOrderModuleList is a structure of type [LIST_ENTRY](https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb_ldr_data#remarks) whose member DllBase is pointer to _Kernel32_ (see figure6)



Once the malware obtains the address of GetProcAddress, it loads the function LoadLibrary and other functions from _kernel32_ including OpenEventA, CreateEventA, Sleep, VirtualAlloc, _etc_. 

LoadLibrary is used to load _advapi32, gdi32, user32, crypt32_ and _ntdll_ DLLs, only specific functions of these libraries are loaded afterwards.

![Extract of the function used to load extra libraries and their methods.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd588_6a92a423dae089660dfd1ded_6a2a7a2bcf15f12139bf3ea2.webp)

Figure 7. Extract of the function used to load extra libraries and their methods. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


### Environment detection & checks

Stealc attempts to detect its environment for two purposes:

  1. Exit in particular conditions (sandbox environment, unwanted location, _etc_.)
  2. Host fingerprinting



The malware implements the following exit conditions:

  * Username is JohnDoe (Windows Defender emulator default username);
  * Hostname is HAL9TH (Windows Defender emulator default hostname);
  * Configured language is Russian;
  * Expiration date is overdue, a date is hardcoded in the binary, if this date is passed, the malware exits. This is almost certainly a functionality added to the build by the developer(s) as part of their business model;
  * Section should be writable (by default Stealc configures its .text with write permission).
  * RAM capacity is below 1 GB;
  * No display is configured.



### Miscellaneous functionalities

Stealc also implements functionalities common to other malware of the stealer family. It has the capability to take a screenshot of the infected host and to fingerprint the infected machine. To retrieve this information, the sample queries the suitable registry keys and interacts with the Windows API.

The fingerprinted information are:

  * Public IP address;
  * Geolocation;
  * Hardware ID;
  * Operating System version;
  * Architecture;
  * Username;
  * Computer name;
  * Local time;
  * Language;
  * Keyboard layout;
  * Physical resources: CPU (core, name), RAM, number of threads, display resolution and GPU driver;
  * List of running processes;
  * List of installed applications.



### Command and Control communication

The malware communicates over HTTP, data are sent in POST requests that use multi-form structure whose forms are the stolen data encoded in base64.

In the first interaction, the infected host sends its HWID (hardware ID) and its build name (the value is "_default_ ").

The server responds with the following **base64** string:

MWZjZTYzMTFhZDg1NmUzYTVjNTQ5OTQ0NDU0NWJmOGJjNjc2MDc0YTY3ZWIwZDJiMmZiNTQwMWE4OTMxODM3Y2NiZDlhMTllfGlzZG9uZXxkb2NpYS5kb2N4fDF8MXwwfDF8MXwxfDF8MXw=

The decoded content from the base64 format is:

1fce6311ad856e3a5c5499444545bf8bc676074a67eb0d2b2fb5401a8931837ccbd9a19e|isdone|docia.docx|1|1|0|1|1|1|1|1|

The first hash is, in fact, an identifier used as a **token** for all communications, and sent in a dedicated form for each message. 

The early communications of the malware aim at downloading the configuration of the stealer, for instance the path and file patterns to look for on the infected host, the wallets or extensions to search, _etc._

The stealer **gets** its **configuration** from the **C2** , with a POST request whose two forms are sent. The form name "message" indicates which type of data will be sent, it could be "_browser_ ", "_plugin_ ", "_wallets_ " or "_files_ ". The structure of the C2 response (for the configuration) is always the same, data are concatenated with the pipe character | (see figure 9).

It repeats this same operation for each browser, their extensions, for the wallets and installed applications.

The list of targeted assets is provided in the [part 1 of Stealc analysis](/blog/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-1) in the annex 1 - Stealc capabilities.

![Downloaded configuration encoded in base64.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd59a_6a92a429cd1cab63350d0707_6a2a7a2bcf15f12139bf3eb4.webp)

Figure 8. Downloaded configuration encoded in base64. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


After downloading the bot configuration, the stealer sends the fingerprinted information (see section _Miscellaneous functionalities_ for the list of fingerprinted information that are exfiltrated).

The table below displays communications between the infected host and [Stealc C2](/blog/adversary-c2-infrastructures-tracked-in-2023).

  * main url: 752e382b4dcf5e3f.php
  * DLLs url: /dbe4ef521ee4cc21/



For each browser, wallets, plugins, the same actions are repeated and the forms are the same. The last communication is optional, this request is sent only if Stealc has a next stage configured on its panel.

#### File grabber

After stealing data from targeted browsers and their extensions, the stealer uses its file grabber functionality. The grabber configuration is received from the C2 and is formatted as follow:

standart|%DESKTOP%\\\|*.txt,*.doc,*.docx,*.xls|7000|1|0|

The structure of the configuration is the following one. First a _name,_ then a _directory_ or a _shortcut_ to a directory (here the desktop), thirdly a list of _file extensions_ that the malware wants to exfiltrate and finally the _maximum size_. We also identified 2 extra parameters that were not useful for the analysis.

In case the file name and path match the grabber filters, it is exfiltrated in a POST request to the C2 with three forms.

Table 2. List of forms and their content when conditions for exfiltration are metForm ID| Form name| Form value  
---|---|---  
1| token| The token value provided by the C2 in the earlier communication.  
2| file_name| The full file path to the stolen file encoded in base64.  
3| file| The file content encoded in base64.  
  
![Example of a file exfiltrated by the file grabber.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd58b_6a92a4238d1115926b20989d_6a2a7a2bcf15f12139bf3ea5.webp)

Figure 9. Example of a file exfiltrated by the file grabber. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


#### DLLs loading

To access particular files or data, Stealc requires external DLLs that are not embedded in the PE but rather downloaded from a specific URL hosted by the C2. The downloaded DLLs are:

  1. _sqlite3.dll_
  2.  _freebl3.dll_
  3.  _mozglue.dll_
  4.  _msvcp40.dll_
  5.  _nss3.dll_
  6.  _softokn3.dll_
  7.  _vcruntime140.dll_



The DLLS are all written in the C:\ProgramData\ directory and are then loaded (TTP: Shared Module: T1129). Of note, only specific functions are loaded by the malware.

![Sqlite3.dll function loading.
Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd5a3_6a92a41f69291914889a1685_6a2a7a2acf15f12139bf3e96.webp)

Figure 10. Sqlite3.dll function loading. Available on Sekoia Blogpost: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


After loading the required functionalities from the DLLs, Stealc exploits them to access data of interest, Similarly, when a targeted data is found on the infected host, it is sent to the C2 using a POST request and encoding data in base64.

As described in this section, **Stealc can be noisy** in case many files are exfiltrated to the C2.

### Next stage

As other analysed stealers observed upgrading their set of functionalities, Stealc is also able to download and execute a next stage payload. The next stage is configured by the request containing the form "_isdone_ " or “done”, depending on the sample. The C2 responds with a base64 data containing the URL of the next stage to download.

The sample (Stealc SHA-256: [1587857ad744c322a2b32731cdd48d98eac13f8aa8ff2f2afb01ebba88d15359](https://bazaar.abuse.ch/sample/1587857ad744c322a2b32731cdd48d98eac13f8aa8ff2f2afb01ebba88d15359/)) is configured to execute a next stage which is a Laplas Clipper, here is the response of Stealc C2 to configure the next stage, the next payload is configured by an URL that Stealc download and execute (see figure 15).

![Next stage configuration.
Available on Sekoia Blogpost about: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd5a6_6a92a4243e6167cebbf6d76a_6a2a7a2bcf15f12139bf3ea8.webp)

Figure 11. Next stage configuration. Available on Sekoia Blogpost about: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


![Decompiled function for the execution and download of the next.
Available on Sekoia Blogpost about: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6496522c3fa482dd594_6a92a4274c776939a1e0e679_6a2a7a2bcf15f12139bf3eb1.webp)

Figure 12. Decompiled function for the execution and download of the next. Available on Sekoia Blogpost about: Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity - Part 2.  


### Trace removal

Stealc attempts to reduce its infection traces by removing itself and its downloaded DLLs (T1070.004) with the following one-line command:

`cmd.exe /c timeout /t 5 & del /f /q "$STEALERPATH" & del "C:\ProgramData\*.dll" & exit`

The command is executed with a basic ShellExecuteA function from _Shell32.dll_.

## Conclusion

**Stealc** displays all functionalities and behaviors to be a **viable tool in the** information stealer catalog, and will almost certainly be incorporated in multiple intrusion sets’ toolsets, either as a shift or an expansion of their capabilities. Based on observed similarities between **Stealc** and other malware of the [infostealer](/blog/overview-of-the-russian-speaking-infostealer-ecosystem-the-logs) family, notably **Raccoon** and **Mars** stealer, Sekoia analysts assess it is likely a confirmation of a transmission and circulation of knowledge, including source code, and of human resources, in the Russian-speaking cybercriminal ecosystem.

Sekoia analysts expect Stealc developer will almost certainly continue to update its stealer with new and / or improved features in the near term to meet customers’ expectations and expand its customer base. To provide our customers with actionable intelligence, Sekoia analysts will continue to monitor emerging and prevalent infostealers, including Stealc.

## Annex 1 - Configuration extraction

As introduced in the _strings obfuscation_ section, Stealc embeds the address of the C2 and its different URLs in the rdata section of the PE.

Based on our observation, the script should meet the following requirements:

  1. Retrieve the RC4 key in rdata;
  2. Deobfuscate the strings until all patterns related to the C2 are spotted.



The RC4 key is hardcoded in the PE in cleartext and by definition RC4 keys are 20 bytes long. Stealc C2 information are stored with the following structure:

  * C2 base URL: http://<ip or domain> or https://<ip or domain>;
  * C2 URL resource which is a random string ending by extension;
  * C2 directory name where the DLLs are hosted (_nss3.dll, sqlite3.dll, etc_...).



The provided configuration extractor simply loops over that section to find the patterns described previously.

`from base64 import b64decode  
from pefile import PE, SectionStructure  
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms  
  
  
class Stealc:  
  
"""Stealc configuration"""  
  
rc4_key: bytes = b""  
base_url: str = ""  
endpoint_url: str = ""  
dlls_directory: str = ""  
  
def __str__(self):  
out = f"Stealc RC4 key: {self.rc4_key}\n"  
out += f"SteaC Command and Control:\n"  
out += f"\t- {''.join([self.base_url, self.endpoint_url])}\n"  
out += f"\t- {''.join([self.base_url, self.dlls_directory])}\n"  
return out  
  
def rc4_decrypt(self, data: bytes) -> bytes:  
"""decrypt RC4 data with the provided key."""  
  
algorithm = algorithms.ARC4(self.rc4_key)  
cipher = Cipher(algorithm, mode=None)  
decryptor = cipher.decryptor()  
return decryptor.update(data)  
  
  
def get_section(pe: PE, section_name: str) -> SectionStructure:  
"""return section by name, if not found raise KeyError exception."""  
  
for section in filter(  
lambda x: x.Name.startswith(section_name.encode()), pe.sections  
):  
return section  
  
available_sections = ", ".join(  
[_sec.Name.replace(b"\x00", b"").decode() for _sec in pe.sections]  
)  
raise KeyError(  
f"{section_name} not found in the PE, available sections: {available_sections}"  
)  
  
  
def get_rdata(pe_path: str) -> SectionStructure:  
"""Extract Stealc radata section"""  
  
pe = PE(pe_path)  
section_rdata = get_section(pe, ".rdata")  
return section_rdata  
  
  
def is_valid_string(data: bytes) -> bool:  
return True if all(map(lambda x: x >= 43 and x <= 122, data)) else False  
  
  
def search_Command_and_Control(stealc: Stealc, rdata_section: SectionStructure):  
"""  
Search two types of strings in rdata section of Stealc:  
1. The RC4 key which is 20 bytes long;  
2. Strings matching the way Stealc stores its C2 configuration (these strings are decoded (base64 decode + RC4 decryption),  
This works for the Stealc version at least until 15 Feb 2023 but could change in new versions...  
2.1 base url (`http://something...` or `https://something...`)  
2.2 endpoint which ends with `.php`  
2.3 DLLs directory starts and ends with `/` (eg: `/something_random/`)  
"""  
  
for string in filter(  
lambda x: x and is_valid_string(x), rdata_section.get_data().split(b"\x00" * 2)  
):  
if len(string) == 20 and not stealc.rc4_key:  
# Hopefully the RC4 key is stored as the beginning of the rdata section  
stealc.rc4_key = string  
print(f"[+] RC4 key found: {stealc.rc4_key}")  
if stealc.rc4_key and string != stealc.rc4_key:  
try:  
cleartext = stealc.rc4_decrypt(b64decode(string))  
# print(f"{string.decode():<40} {cleartext}")  
if cleartext.startswith(b"http://") or cleartext.startswith(  
b"https://"  
):  
print(f"[+] Found StealC Command and Control")  
stealc.base_url = cleartext.decode()  
elif cleartext.startswith(b"/") and cleartext.endswith(b"/"):  
print(f"[+] Found DLLs URL directory name")  
stealc.dlls_directory = cleartext.decode()  
elif cleartext.endswith(b".php"):  
print(f"[+] Found StealC endpoint")  
stealc.endpoint_url = cleartext.decode()  
  
except Exception:  
pass  
  
  
if __name__ == "__main__":  
import sys  
if len(sys.argv) < 2:  
print(f"not enough parameter, please provide as argument the path to stealc sample.")  
stealc = Stealc()  
rdata = get_rdata(sys.argv[1])  
search_Command_and_Control(stealc, rdata)  
print(stealc)  
`

## Annex 2 - IDA script for string deobfuscation

`from idaapi import *  
from ida_bytes import *  
from ida_name import *  
from base64 import b64decode  
from string import ascii_letters, digits  
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  
  
  
def read_rdata(name: str) -> str:  
print(f"read_rdata: {name}")  
addr = get_name_ea_simple(name)  
size = get_max_strlit_length(addr, ida_nalt.STRENC_DEFAULT)  
return get_bytes(addr, size - 1)  
  
def rc4_decrypt(key: bytes, data: bytes) -> bytes:  
  
algorithm = algorithms.ARC4(key)  
cipher = Cipher(algorithm, mode=None)  
decryptor = cipher.decryptor()  
return decryptor.update(data)  
  
def deobfuscate_string(base: int, end: int , KEY: bytes):  
ea = base  
size = 0  
clear = []  
addr = []  
  
while ea <= end:  
flags = ida_bytes.get_flags(ea)  
if ida_bytes.is_code(flags):  
instr_str = idc.generate_disasm_line(ea, 1)  
instr_str = " ".join(instr_str.split())  
if instr_str.startswith("push offset a") or instr_str.startswith("mov dword ptr [esp], offset a"):  
value = instr_str.split("offset")[-1].split(';')[0].strip()  
value = read_rdata(value)  
clear.append(rc4_decrypt(KEY, b64decode(value)))  
elif instr_str.startswith("mov dword_"):  
temp = instr_str.replace("mov dword_", "")  
temp = temp.split()[0].replace(",","")  
addr = int(temp, 16)  
string = get_bytes(addr, size)  
cleartext = clear.pop(-1)  
cleartext = cleartext.decode()  
idc.set_cmt(ea, cleartext, 0)  
text = ""  
for c in cleartext:  
if c in f"{ascii_letters}{digits}":  
text += c  
else:  
text += "_"  
cleartext = f"str_{text}"  
print(f"replace dword_{addr:x} by `{cleartext}`")  
set_name(addr, cleartext)  
ea += 1  
`