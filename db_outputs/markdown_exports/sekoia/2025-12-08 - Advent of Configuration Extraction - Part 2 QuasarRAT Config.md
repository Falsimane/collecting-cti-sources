# Advent of Configuration Extraction - Part 2: QuasarRAT Config

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/advent-of-configuration-extraction-part-2-unwrapping-quasarrats-configuration
- **Date :** 2025-12-08

---

In the second part of our “Advent of Configuration Extraction” series, we unwrap QuasarRAT, a popular .NET remote access trojan (RAT), and show how to extract its encrypted configuration out of the binary. The article begins by detailing the environment: Jupyter Notebook, [pythonnet](https://github.com/pythonnet/pythonnet), [dnSpy](https://github.com/dnSpy/dnSpy) and friends—so every step is reproducible. Next, it presents the construction of a Python-based extractor for a clean QuasarRAT sample, then extends the approach to handle an obfuscated build. 

## RAT in the Chimney: Introducing QuasarRAT

[QuasarRAT](https://github.com/quasar/Quasar) is an open-source RAT that first appeared in 2014, under the name xRAT. Originally published on GitHub as a legitimate Windows remote administration tool. Over time, however, its accessibility, small size, and ease of modification have led to it being frequently abused by cybercriminals and threat actors for malicious purposes. For more information about the RAT itself, the JPCERT made a presentation at the [Botconf 2020](https://github.com/JPCERTCC/QuasarRAT-Analysis/blob/main/slides) which details the origins, variants and capabilities.

Implemented in **C#** on the **.NET Framework** , QuasarRAT lends itself readily to extension, recompilation and customisation. Its open-source codebase has been thoroughly analysed and adapted by threat actors seeking bespoke functionality.

Functionally, QuasarRAT supports a **broad set of remote administration functions** , including features such as system information collection, file management, remote desktop viewing, keylogging, and command execution. While these capabilities can be used for legitimate administrative tasks, they are also commonly leveraged in cyber espionage, unauthorized surveillance, and other forms of intrusion.

It has been observed in multiple attacks orchestrated by both [independent threat actors](https://securelist.com/gitvenom-campaign/115694/) and [state-aligned groups](https://www.botconf.eu/wp-content/uploads/formidable/2/Botconf2022-19-FaouCoteCyr.pdf). Its popularity stems from being lightweight, configurable, and freely available, making it a recurring tool in Windows-targeted malware campaigns.

## Elf’s Workshop Tour: Sleighing the Basics of IL

DnSpy and [ILSpy](https://github.com/icsharpcode/ILSpy) are widely adopted for .NET sample analysis. A [Jupyter Notebook](https://gist.github.com/lbpierre/15e6f3100ab88bf4fc80b5e51ff6dafb) environment has been configured to support configuration extraction development, incorporating libraries for PE/ELF manipulation, decompilation frameworks, and related tasks. To facilitate the environment portability, the configuration has been containerised with Docker. 

This installment of “Advent Of Configuration Extraction” focuses exclusively on the .NET decompiler component. The extractor for .NET malware configuration which must interact with the Intermediate Language (_a.k.a IL_) relies on a combination of pythonnet and [dnlib](https://github.com/0xd4d/dnlib). In this arrangement, dnlib serves as the core engine for reading, rewriting, and inspecting .NET assemblies, while pythonnet acts as a bridge that allows Python code to invoke dnlib’s APIs.

_Dnlib is an open-source .NET library designed for deep inspection and modification of .NET assemblies (EXE and DLL files). It exposes metadata, types, methods, attributes, and IL instructions in a programmatic fashion, making it a powerful tool for reverse engineering and malware analysis._

`import clr  
clr.AddReference("System.Memory")  
from System.Reflection import Assembly, MethodInfo, BindingFlags  
from System import Type  
  
DNLIB_PATH = '/workspace/utils/dnlib.dll' # path in docker to dnlib.dll  
clr.AddReference(DNLIB_PATH)  
  
import dnlib  
from dnlib.DotNet import *  
from dnlib.DotNet.Emit import OpCodes  
  
module = dnlib.DotNet.ModuleDefMD.Load(MALWARE_PE_PATH)  
`

_Code 1. Python prelude to load a .NET sample to interact with its namespaces, classes and methods_

The preceding Python snippet uses pythonnet’s clr module to load and interact with .NET assemblies. Invoking `AddReference(“System.Memory”)` grants access to low-level memory handling-types. These preliminary calls are required to import the dnlib framework for the next and most required step that will load to pythonnet the dnlib framework. Once dnlib is loaded, the script can open and analyse a .NET PE or DLL, enabling it to:

  * Decompile individual function.
  * Traverse the assembly structure: namespace, classes, methods, and variables.
  * Extract custom types, metadata entries, and embedded strings.



At this stage, the most “critical” portion of the lab setup is complete. The module variable provides programmatic access to the bulk of the decompiled .NET content. 

Before proceeding with QuasarRAT configuration extraction, a brief overview of the .NET Intermediate Language is necessary.

Within the .NET decompilation context, Intermediate Language (IL) is also referred to as MicroSoft IL (MSIL) or Common IL (CIL).

IL is a **stack‑based intermediate bytecode** used by .NET. High-level source (C#, VB.NET, _etc._) compiles into IL, which the Common Language Runtime(CLR) then **JIT-compiles** into native machine code.

IL is a **stack machine** , meaning:

  * Instructions **push** values onto a stack.
  * Other instructions **pop** values from the stack.
  * Operations work on the stack (not registers).



Each IL instruction has:

  1. **Opcode** : The operation, _e.g._`ldstr`, `stloc`, `call`, `add`, `ldc.i4`.
  2. **Operand** (optional): Additional data the instruction needs:


  * strings
  * class/method references
  * integers
  * branch targets
  * metadata tokens



The Intermediate Language instruction are as fallow: Instruction Operand

In the extract of IL code above, there are 3 distincts instructions: ldstr, stsfld and ldc.i4.

**Instruction** | **Description**| **Example**  
---|---|---  
`ldstr`| Load String: Pushes a **string literal** onto the evaluation stack.| `ldstr “Hello”` push the string Hello on the stack  
`stsfld`| Store into Static Field: Pops a value from the evaluation stack and **stores it into a static field** of a class.| `stsfld string Main.test.name` pop the last value on the stack into Main.Test.name  
`ldc.i4`| Load constant int32: pushes a 32-bit integer constant onto the evaluation stack.pushes a 32-bit integer constant onto the evaluation stack.| `ldc.i4 42`push the value 42 on the stack  
  
 _Table 1. Example of IL instructions_

## Mistletoe & Metadata: Pulling Out QuasarRAT’s Config

## RATnip for Rookies: Unwrapping the Bare-Bones Config

As noted earlier, QuasarRAT is an open-source project. In this example, a self-compiled sample with the [DEBUG disable](https://github.com/quasar/Quasar/blob/master/Quasar.Client/Config/Settings.cs#L16-L45) is employed, ensuring that all settings strings remain in plain text. The configuration resides in the Config namespace, within the Settings class. That class defines the following RAT configuration keys: _version, hosts, reconnectdelay, specialfolder, directory, subdirectory, installname, install, startup, mutex, startupkey, hidefile, enablelogger, encryptionkey, tag, logdirectoryname, serversignature, servercertificatestr, servercertificate, hidelogdirectory, hideinstallsubdirectory, installpath, logspath_ , and _unattendedmode_.

The extraction strategy relies on the pythonnet/dnlib stack to play with the assembly’s code structure. The extractor first iterates through all namespaces until it finds the one named `Config`, then scans the “Config” namespace’s classes until it reaches `Settings`.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a53de9a71d422840c61c_6a92a17a16f788fda8e421df_6a2a7fdbdff0174b6846ed28.webp)

Figure 1. Decompiled (#C) view of the Settings class from the Config namespace in dnSpy 

For simplicity, this example focuses solely on the Command-and-Control server entry stored in the Settings class member `HOSTS`.

This initial task is to locate the target namespace and class, as shown below:

`target_ns = "Config"  
target_class = "Settings"  
found_setting_class = None  
  
for t in module.Types:  
if t.Namespace.EndsWith(target_ns) and t.Name.EndsWith(target_class):  
found_setting_class = t  
break  
  
if found_setting_class:  
print("Class found:", found_setting_class)  
else:  
print("Class not found.")  
`

_Code 2. Python code to identify the Settings class from the Config namespace_

A glance at the class in dnSpy might suggest that iterating over `Settings.Fields` completes the task. In fact, this collection exposes only the field definitions (type and full name), not their actual values.

`for field in found_setting_class.Fields:  
print(field)  
`

_Code 3. Python code to iterate over filed of a the Settings class_

`System.String Quasar.Client.Config.Settings::VERSION  
System.String Quasar.Client.Config.Settings::HOSTS  
System.Int32 Quasar.Client.Config.Settings::RECONNECTDELAY  
System.Environment/SpecialFolder Quasar.Client.Config.Settings::SPECIALFOLDER  
System.String Quasar.Client.Config.Settings::DIRECTORY  
...  
`

_Log 1. Output of the Code 3 code._

In .NET IL, static fields are initialised by the class’s static constructor, known as (standing as **C** lass **C** ons**TOR**). Examining this initialiser in dnSpy requires switching the decompiled view from C# to IL, yielding the following output:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a53de9a71d422840c61c_6a92a17a16f788fda8e421df_6a2a7fdbdff0174b6846ed28.webp)

_Figure 2. Decompiled view (IL) of the Settings constructor method_

The extraction strategy begins by locating the Settings class’s static constructor. It then walks through each instruction alongside its predecessor in order to capture paired operation. In this case, the first instruction loads a literal string (`ldstr`), and the immediately following instruction references the corresponding class field.

Decompiling a method with dnlib requires a `dnlib.DotNet.MethodDefMD` instance. Instruction types can be detected in two ways:

  1. By comparing the opcode name as a string, _e.g._ : `instr.OpCode.Name == "ldstr"`.
  2. By comparing the opcode against the `dnlib.DotNet.Emit OpCodes`enum _e.g._ : `instr.Opcode == OpCodes.Ldstr`.



The direct opcode comparison is the option preferred at TDR for its clarity and consistency.

`for m in found_setting_class.Methods:  
prev_instr = None # Track previous instruction  
if m.IsStatic and m.Name == ".cctor":  
print("Analyze constructor method of the `Config.Settings` class")  
# Scan the IL instructions to find the constant assignment  
for instr in m.Body.Instructions:  
if instr.OpCode == OpCodes.Stsfld and instr.Operand is not None:  
field = instr.Operand  
if field.Name == "HOSTS":  
print(instr, prev_instr)  
# Get the previous instruction that loads the constant  
if prev_instr is not None:  
if prev_instr.OpCode == OpCodes.Ldstr: # String constant  
print("Get String constant", prev_instr.Operand)  
prev_instr = instr  
`

 _Code 4. Full Python code to read the HOSTS field of the Settings class from the Config namespace_

 _Quick tips: PowerShell’s Reflection capabilities can load a .NET assembly, then access its members or invoke its methods directly from the command line. This approach is especially useful for probing obfuscation and deobfuscation routines without a debugger._

[_Source: X message of_** _@struppigel_**](https://x.com/struppigel/status/1674442965538816000/photo/1)

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a53de9a71d422840c625_6a92a1792e47a1e9fe0cf413_6a2a7fdbdff0174b6846ed25.webp)

 _Figure 3. Example of PowerShell Reflection capabilities with the self-compiled QuasarRAT sample_

## Elf-Sized Encryption: Breaking the Obfuscated QuasarRAT

The sample under analysis has the following: [SHA-256: 4ef44bf6815e78603aec5b480f43fa26d883897c88ced763565e912c38ac9639](https://bazaar.abuse.ch/sample/4ef44bf6815e78603aec5b480f43fa26d883897c88ced763565e912c38ac9639/)

This build employs a generic .NET obfuscator, many tools are available on GitHub such as , [obfuscar](https://github.com/obfuscar/obfuscar). A quick inspection in dnSpy confirms significant obfuscation.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a53de9a71d422840c622_6a92a177bd6424423eee6acd_6a2a7fdbdff0174b6846ed22.webp)

_Figure 4. Decompiled code of obfuscated QuasarRAT_

Manual deobfuscation of each variant is impractical, so multiple extraction strategies must be explored. Since the DEBUG flag is unset, the RAT is expected to decrypt its settings at runtime.

Source code analysis indicates that QuasarRAT uses AES-256 in CBC mode, with the key derived via PBKDF2. Although, all the configuration keys remain declared in the Settings class, their actual values are assigned in the [Initialize method](https://github.com/quasar/Quasar/blob/master/Quasar.Client/Config/Settings.cs#L73-L88). A closer look at the [Aes256](https://github.com/quasar/Quasar/blob/master/Quasar.Common/Cryptography/Aes256.cs) module of the RAT reveals that it uses the default system implementation of AES implementation, and how the cryptographic material is configured. 

The aes module yields important insights:

  1. The AES key is stored as a class member and initialised in the static constructor (_c.f. .cctor method_);
  2. A **hardcodedsalt** value within in the aes class is required for PBKF2 key derivation;
  3. Encrypted strings follow a fixed layout:



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a53de9a71d422840c619_6a92a1762b0ef7af46bc19a0_6a2a7fdbdff0174b6846ed1f.webp)

Drawing on objectives and insights from the source code review, the extraction strategy to bypass obfuscation proceeds as follows:

  1. Locate the `Aes256` class in the `Crytography` namespace;
  2. Extract the hardcoded salt field from Aes256 class;
  3. Resolve cross-references to Aes256 in order to pinpoint the Settings class within the Config namespace;
  4. Retrieve the AES key stored in the Settings;
  5. Enumerate all encrypted string fields in Settings;
  6. Decrypt each string using the derived AES key and salt. 



Many of the utility routines, such as fetching a field from a type, iterating through class members, and resolving cross-references are generic and readily reusable across other .NET malware analysis.

### Step 1 - Searching the Cryptography.Aes256 class

Frequent interaction with .NET samples via Python typically starts with a routine that traverses the module’s types (represented in dnlib as a `ModuleDefMD`).

In QuasarRAT’s Aes256 implementation, the standard .NET AES provider `System.Security.Cryptography.AesCryptoServiceProvider` is instantiated. To locate these instantiations, a helper function loops over each `ModuleDefMD.Type`, then over each `MethodDef`, searching for an IL instruction of the form:

`Newobj System.Security.Cryptography.AesCryptoServiceProvider::.ctor()`

The following snippet demonstrates this scanning approach:

`def search_crypto_class():  
"""This function iterate over all class and methods  
of the module for the creation of the AesCryptoServiceProvider  
"""  
  
for mtype in module.GetTypes(): # iterates over each type  
if not mtype.HasMethods:  
continue  
for method in mtype.Methods: # iterates over each method  
if not method.HasBody:  
continue  
if not method.Body.HasInstructions:  
continue  
if len(method.Body.Instructions) < 20:  
continue  
for ptr in method.Body.Instructions: # iterate over each instruction  
# Verify that a crypto provider is contructed  
if (  
ptr.OpCode == OpCodes.Newobj  
and ptr.Operand.FullName  
== "System.Void System.Security.Cryptography.AesCryptoServiceProvider::.ctor()"  
):  
print(  
f"Crypto class found {method.FullName} in {mtype.Name}"  
)  
return mtype  
`

 _Code 5. Python function used to locate the AesCryptoServiceProvider constructor_

### Step 2 - Search the salt value

Within the common.Cryptography namespace, the salt for AES key derivation is stored as a private static byte array in the Aes256 class.

Since this array is the only compile-time constant in the class, it is initialised in the static constructor (). In that method, a `ldtoken` instruction loads a metadata token pointing to another static class where the raw byte data resides. By resolving this token, the salt value can be extracted directly from the referenced field:

  1. In the of the class there is a `ldtoken` (Load Token) the token is defined in another static class within a structure
  2. `call void <redacted path> RuntimeHelpers::InitialzeArray(<redacted>)`
  3. `stsfld unit8[] CryptoClass::seed_member`



`def search_salt(cryto_class) -> Optional[bytes]:  
for m in cryto_class.Methods:  
if m.IsStaticConstructor:  
# the seed is always a byte array -> System.Byte[]  
for instr in m.Body.Instructions:  
if instr.OpCode == OpCodes.Ldtoken:  
# we get the name of the static field here  
init_var_name = (instr.Operand.get_Name())   
# simply retrieve the structure member value   
seed = get_field_from_struct(init_var_name)   
if seed:  
return seed  
  
def get_field_from_struct(struct_name: str) -> Optional[bytes]:  
for typeDef in self.module.Types:  
for field in typeDef.Fields:  
if field.Name == struct_name and field.HasFieldRVA:  
return bytes(field.InitialValue)  
`

_Code 6. Python code used to extract the salt bytes array used to derive the AES key_

### Step 3 - Cryptographic function X-Ref

At this stage, the Aes256 class is accessible, and the next goal is to locate its sole caller, namely, the `Settings.Initialize` method. Identification of the constructor can proceed by spotting either the `Rfc2898DeriveBytes` invocation (`System.Security.Cryptography.Rfc2898DeriveBytes::.ctor`) or the `Aes256 .ctor` reference directly.

`def search_caller(class_name: str, method_name: str) -> Optional[Tuple[str, str]]:  
# Iterate over all types in the assembly  
for typeDef in self.module.Types:  
for method in typeDef.Methods:  
if not method.HasBody:  
continue # Skip methods without a body  
  
# Scan IL instructions for calls to A::func1  
for instr in method.Body.Instructions:  
if instr.OpCode == OpCodes.Call and instr.Operand is not None:  
if (  
instr.Operand.Name == method_name  
and instr.Operand.DeclaringType.Name == class_name  
):  
return typeDef.Name, method.Name  
`

 _Code 7. Python function used to search reference to a function in a program_

Once the constructor method is identified, the extractor performs a cross-reference search across all namespaces, types, and methods to pinpoint its unique caller. This exhaustive traversal can be time-consuming, as it requires inspecting all the assembly.

`def search_caller(class_name: str, method_name: str) -> str:  
# Iterate over all types in the assembly  
for typeDef in module.Types:  
for method in typeDef.Methods:  
if not method.HasBody:  
continue # Skip methods without a body  
  
# Scan IL instructions for calls to A::func1  
for instr in method.Body.Instructions:  
if instr.OpCode == OpCodes.Call and instr.Operand is not None:  
if instr.Operand.Name == method_name and instr.Operand.DeclaringType.Name == class_name:  
return typeDef.Name, method.Name  
`

 _Code 8. Python function used to return a handle to the specific function in a class_

### Step 4 - Searching for cryptographic material in Settings

At this point, the extractor re-uses the reference to the Settings class and is equipped to retrieve its configuration. The remaining steps rely primarily on Pythonic logic rather than dnlib-specific routines. In the Settings class’s initializer, the decryption routine is invoked repeatedly, a pattern leveraged by the extractor. By tallying the number of calls to each method within Settings, the routine with the highest call count can be inferred as the decryption function. Once identified, the extractor retrieves the first argument from each invocation, which corresponds to the encrypted string. On the other hand, there is a unique call to the Aes256 object construction whose unique parameter is the AES key.

_P.S.: The code only needs to retrieve one parameter as the decryption function only takes the encrypted string, the AES key is stored in a member of the Aes256 instance._

`def get_func_parameter(method) -> defaultdict:  
"""This only work in this context of func that take only ONE parameter"""  
  
is_call = None  
callers_with_args = defaultdict(list)  
  
# read the function instructions backward  
reversed_instructions = list(method.Body.Instructions)[::-1]  
  
for instr in reversed_instructions:  
if instr.OpCode == OpCodes.Call:  
is_call = instr.Operand  
if instr.OpCode == OpCodes.Ldsfld and is_call:  
callers_with_args[is_call].append(instr.Operand)  
is_call = None  
return callers_with_args  
`

 _Code 9. Extract the first argument of a function call_

`def search_aes_key(mclass):  
method_that_use_aes_key = None  
for m in mclass.Methods:  
ldsfld, calls = 0, defaultdict(int)   
for instr in m.Body.Instructions:  
if instr.OpCode == OpCodes.Ldsfld:  
ldsfld += 1  
elif instr.OpCode == OpCodes.Call:  
calls[str(instr.Operand.Name)] += 1  
  
if any(filter(lambda x: x > 2, calls.values())):  
method_that_use_aes_key = m  
# Here we search the function that initialize the AES key (PBKF2)  
# There is only one call to this function and the only arg is the   
# ref token to the AES key that is going to be derived  
call_to_search = None  
callers = get_func_parameter(m)  
counting = [n for v in callers.values() for n in v]  
values_counting = Counter(counting)  
unique = {num for values in callers.values() if all(values_counting[n] == 1 for n in values) for num in values}  
AES_key_variable = unique.pop()  
print(f"The AES key is located in {AES_key_variable.FullName}")  
aes_key = get_constant_from_class(mclass, AES_key_variable.Name)  
print(f"The AES key value is: {aes_key}")  
return aes_key  
  
if method_that_use_aes_key:  
break  
`

 _Code 10. Python function used extract the AES key_

### Step 5 - Pulling obfuscated string

This routine parallels the extraction method used for the unobfuscated sample. It locates the static constructor () of the target class and reads each field initialiser in declaration order. Since the CLR preserves the source order of static fields, the obfuscated string values emerge sequentially. Applying the previously recovered AES key, salt, and IV decrypts those strings and reveals the complete RAT configuration.

`def extract_all_encrypted_configuration(mclass) -> list:  
  
static_ctor = next((m for m in mclass.Methods if m.IsStatic and m.Name == ".cctor"), None)  
if not static_ctor or not static_ctor.HasBody:  
print(f"Static constructor (.cctor) not found in class '{class_name}'.")  
return []  
  
constants = []   
  
prev_instr = None # Track previous instruction  
  
for instr in static_ctor.Body.Instructions:  
if instr.OpCode == OpCodes.Stsfld and instr.Operand is not None:  
field = instr.Operand  
if prev_instr is not None:  
# Extract the constant value from the previous instruction  
if prev_instr.OpCode == OpCodes.Ldc_I4: # Integer constant  
# constants.append(prev_instr.GetLdcI4Value())  
# don't we only want string (encrypted configuration)  
pass  
elif prev_instr.OpCode == OpCodes.Ldc_R4: # Float constant  
# constants.append(prev_instr.Operand)  
# don't we only want string (encrypted configuration)  
pass  
elif prev_instr.OpCode == OpCodes.Ldstr: # String constant  
constants.append(prev_instr.Operand)  
  
prev_instr = instr # Update previous instruction  
  
return constants  
`

 _Code 11. Python function used to list encrypted string in the Settings class_

## Final Words

The final steps involve enumerating the decryption routine’s arguments and decoding the encrypted values using an appropriate Python cryptography library. A clearly defined strategy in the design phase, together with an optimized development environment, can significantly accelerate the extractor’s implementation. While this approach does not cover packed samples or certain QuasarRAT variants (for example, builds that substitute AES with another cipher), it delivers sufficiently accurate results for most real-world scenarios.

The full QuasarRAT extractor code is hosted in the [Sekoia Community Git](https://github.com/SEKOIA-IO/Community/blob/main/Configuration_extractors/QuasarRAT.py) repository.

The techniques presented throughout this article demonstrate a systematic approach to extracting QuasarRAT’s encrypted configuration from both clean and obfuscated .NET samples. By combining a reproducible lab environment (Docker-packaged Jupyter Notebook, pythonnet and dnlib) with a thorough understanding of the .NET Intermediate Language, it becomes possible to:

  * Locate and inspect critical classes (.cctor, Aes256, Settings).
  * Recover cryptographic parameters (AES key, salt, IV, HMAC layout).
  * Identify and invoke the decryption routine via IL instruction analysis.
  * Assemble a fully automated Python extractor capable of harvesting C2 settings.



Although tailored to QuasarRAT, this workflow scales naturally to other .NET-based malware that rely on similar initialisation patterns and public-domain cryptography APIs. Its modular design, emphasizing namespace/class traversal, cross-reference resolution and opcode comparison, facilitates rapid adaptation to variants employing different obfuscators or minor algorithmic tweaks.

Remaining gaps include handling packed executables, non-AES algorithms, and custom runtime loaders. Future enhancements may introduce dynamic tracing or integration with deobfuscation pipelines to broaden coverage.