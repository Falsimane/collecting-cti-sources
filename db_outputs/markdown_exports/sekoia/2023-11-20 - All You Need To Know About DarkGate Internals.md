# All You Need To Know About DarkGate Internals

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/darkgate-internals
- **Date :** 2023-11-20

---

## Introduction & objectives

DarkGate is sold as Malware-as-a-Service (MaaS) on various cybercrime forums by RastaFarEye persona, in the past months it has been used by multiple threat actors such as TA577 and Ducktail. **DarkGate** is a loader with RAT capabilities developed in _Delphi_ with modules developed in _C++_ , which gained notoriety in the second half of 2023, due to its capability to operate covertly and its agility to evade detection by antivirus systems. This technical report delves into an in-depth analysis of **DarkGate** , shedding light on its **inner workings** , **evasion techniques** , and potential **impacts**.

The analysis starts from the following AutoIt script: [SHA-256 b049b7e03749e7f0819f551ef809e63f8a69e38a0a70b697f8a5a82a792a1df9](https://bazaar.abuse.ch/sample/b049b7e03749e7f0819f551ef809e63f8a69e38a0a70b697f8a5a82a792a1df9/)

![Overview of DarkGate infection chains. Source : Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9abc_6a92a348e36224e46e90e2e9_6a2a6fb362f00361bfd90520.webp)

Overview of DarkGate infection chains. Source : Sekoia TDR Team

## Data obfuscation

### Unusual base64 encoding

The loader uses various techniques to obfuscate data, including strings and configuration encoding using the base64 algorithm with a first unordered alphabet.

![The two alphabets used for data encoding/decoding. Source : DarkGate Internals](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ae5_6a92a33ce17eff730b6578fc_6a2a6fb362f00361bfd904fb.webp)

The two alphabets used for data encoding/decoding. Source : DarkGate Internals

The second alphabet is used to decode the list of Command and Control (C2) URLs and the C2 HTTP messages, while the first one is used everywhere in the binary to decrypt the configuration and other strings employed for dynamic API resolution.

As introduced, the configuration of DarkGate is obfuscated in the PE, it uses a [TStringList](https://www.delphibasics.co.uk/RTL.php?Name=TStringList) to store it, TStringList which can be seen as a hashtable in the C world.

![DarkGate configuration decoded. Source: Sekoia TDR team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ac3_6a92a33d2e47a1e9fe0df67d_6a2a6fb362f00361bfd904fe.webp)

DarkGate configuration decoded. Source: Sekoia TDR team

There are many tools to extract this configuration of DarkGate, such as this one in [GitHub](https://github.com/telekom-security/malware_analysis/blob/main/darkgate/extractor.py).

### Message obfuscations

The communication between the bot and the server is made over HTTP. More details about the C2 communication are provided in the “Command and Control” section of this report. The content of the communication is obfuscated with base64 encoding (with the first alphabet) and a single byte XOR operation where the XOR key is derived from the Bot ID. For further information on the process of computing the BotID, an in depth analysis is provided in a recent [DCSO CyTec report](https://medium.com/@DCSO_CyTec/shortandmalicious-darkgate-d9102a457232).

`digest = MD5(product_id+processor+user+computer)`

The digest is encoded using a custom alphabet, which is leveraged as lookup table nibble-wise according to DCSO CyTec.

![IDA decompiled function used to XOR data. Source: DarkGate Internals by Sekoia TDR team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9af0_6a92a341e9a71d422840106a_6a2a6fb362f00361bfd9050a.webp)

IDA decompiled function used to XOR data. Source: DarkGate Internals by Sekoia TDR team

The following is a Python version of the XOR key derivation used by DarkGate. The seed of the key corresponds to the length of the bot identifier, and the key is XORed with each character to build the final XOR key:

`xorKey = len(botID)  
for char in xorKey:  
xorKey ^= ord(char)  
`

The following CyberChef recipe implements the deobfuscation function for the C2 messages.

![Message deobfuscation using CyberChef. Source: DarkGate Internals by Sekoia TDR team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ae2_6a92a3454538ee1e1c2e68d5_6a2a6fb362f00361bfd90517.webp)

Message deobfuscation using CyberChef. Source: DarkGate Internals by Sekoia TDR team

 _NB: the first string is a wide string in hexadecimal representation. (500072006F006700720061006D0020004D0061006E006100670065007200 = Program Manager)._

### File obfuscation

The malware encrypts some of the files it creates using the _Rijndael_ algorithm with a key length of 160 bits. It uses a stream cipher called _CFB8Bit_ instead of the commonly used block cipher. Again, the process used to create the key is explained in the DCSO CyTec report2

`digest = MD5(product_id+processor+user+computer)  
bot_id = custom_encode(digest)  
digest2 = MD5("mainhw"+bot_id+internal_mutex)  
encoded = custom_encode(digest2)  
aes_key = encoded[:7].lower()  
`

As shown above in the extract of code used to build the AES secret key, it uses string concatenation and custom encoding to generate both the AES key and the bot identifier. For instance, this function is used to encrypt the content of its logs, _e.g._ crash log.

## RAT TTPs

### Reverse shell

DarkGate implements a reverse shell that is started in a dedicated process, using pipes to redirect the standard input, output and error data streams (_e.g._ stdin, stdout, stderr).

![DarkGate function used to set up the reverse shell, leveraging standard input/output to create interactive shell. Source: Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ad6_6a92a33ea2f46752fd0186e6_6a2a6fb362f00361bfd90501.webp)

DarkGate function used to set up the reverse shell, leveraging standard input/output to create interactive shell. Source: Sekoia TDR Team

Once the connection is established, the commands are redirected to the local pipes of the victim's machine. These commands are executed on the victim's system via a command interpreter, and the results are sent back to the attacker through the pipe. Essentially, this allows the attacker to interact with the victim's system as if it has a command prompt or shell on that machine.

The connection is bidirectional, meaning the attackers can send commands and receive responses in real-time, enabling them to navigate the victim's system, exfiltrate data, or perform other malicious actions.

### PowerShell script execution

To facilitate the post compromise stage, DarkGate provides the capability to execute PowerShell files and commands. 

![DarkGate code used to 1\) execute \(if the file already exists\) or 2\) download and execute PowerShell script.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ac0_6a92a34a4c776939a1e0b9b8_6a2a6fb362f00361bfd90526.webp)

DarkGate code used to 1) execute (if the file already exists) or 2) download and execute PowerShell script.

As shown in the figure 7, the function allows the download of a new PowerShell script if needed (by sending the action id 1489). Then, the function configures the PowerShell environment by searching the powershell.exe binary in its dedicated directory (it uses the directory alias [Synactive](https://learn.microsoft.com/en-us/windows/win32/winprog64/file-system-redirector) to avoid basic detection of the PowerShell path).

![function used to execute the PowerShell script. Source: DarkGate Internals by Sekoia TDR team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9adf_6a92a347adf0bb92a6511439_6a2a6fb362f00361bfd9051d.webp)

function used to execute the PowerShell script. Source: DarkGate Internals by Sekoia TDR team

The output of this execution is sent to “ _c:\temp\tskm_ ” before being sent to the Command and Control.

### Keylogger

To perform advanced keylogging activities on the infected host, the malware retrieves the foreground windows (the one the user is interacting with) to retrieve its process identifier. Then it combines the two Windows functions GetAsyncKeyState and GetKeyNameText aiming at capturing users’ keystrokes and writes them to the log file “ _masteroflog_ ”.

### Discord token hunting

Another functionality provided by DarkGate is to collect Discord tokens. To do it, it searches for the Discord process using a well documented technique that involves the windows API functions: CreateToolhelp32Snapshot, Process32First and Process32Next.

Then it attempts to open the process memory with access rights: PROCESS_QUERY_LIMITED_INFORMATION | PROCESS_DUP_HANDLE

Once the memory is acquired, the malware searches for this first string: 

`"events":[{"type":"channel_opened","properties":{"client_track_timestamp`

Then, it looks for the following string:

`{“token”: “`

And it extracts all the characters until it matches another double quote, that terminates the token.

In short, this method is used to search for the JSON discord token built in memory of the process.

### Remote access

In addition to the reverse shell functionality, DarkGate also provides **remote desktop access** using hidden Virtual Network Computing (**hVNC)**. To set up the access, the loader first checks if the software is installed on the infected machine and if not, it downloads it. If the software is already installed and configured with an access, DarkGate **substitutes** it with the following login / password default combination: _SafeMode_ / _darkgatepassword0_

For the software the user SafeMode is created with the following command line:

`cmd.exe “/c cmdkey /generic:\"127.0.0.2\" /user:\"SafeMode\" /pass:\"darkgatepassword0\"”`

### Privilege escalation

DarkGate uses different techniques to elevate its privileges on the infected host from standard user to local admin to _system_. For that purpose, the malware implements three techniques:

  * Restarts itself using [PsExec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec) from the Sysinternal suite;
  * Executes a raw stub that contains some privilege escalation code (we are not able to provide more information on this technique because no code related to this technique was found on the analysed samples);
  * Executes an embedded executable to elevate its privileges.



### Persistence

To keep access upon reboot on the infected host, DarkGate implements a set of persistence methods depending on the bot configuration. Attackers can configure the bot persistence using one of these techniques:

  1. Create a LNK file in the Startup folder that executes AutoIt3.exe with the AU3 script
  2. Set the registry key CurrentVersion\Run with the LNK file.
  3. Use one of the three DLLs loaded using Extexport.exe (more detail in the section: “LOLBAS DLL loading”)



![Lnk executing the Autoit.exe with DarkGate AU3 script to maintain the persistence.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ac6_6a92a346692919148899aec8_6a2a6fb362f00361bfd9051a.webp)

Lnk executing the Autoit.exe with DarkGate AU3 script to maintain the persistence.

In case a file is removed or the registry key is deleted by an antivirus software, the loader raises a critical error (BSOD: Blue Screen Of Death). The BSOD is triggered by a call to NtRaiseHardError with the ErrorCode value of 0xC0000350 corresponding to STATUS_HOST_DOWN.

Of note, this feature was announced earlier this year on a top-tier cybercrime forum, by “RastaFarEye” (the presumed DarkGate author).

![DarkGate advertisement on the XSS forum, announcing its BSOD feature.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9acc_6a92a34ee17eff730b658087_6a2a6fb362f00361bfd9053b.webp)

DarkGate advertisement on the XSS forum, announcing its BSOD feature.

## Defense evasion

### Union Api – Call Native Api using syscall

The developer of DarkGate highly likely borrows a technique detailed in a [Malaysian article](https://cybercoding.wordpress.com/2012/12/01/union-api/) dating back to 2012 which is a copy of GameDeception.]net that is down since 2013. Anti-virus (AV) solutions often hook calls to ntdll to identify potential malicious behaviour. This section covers the technique dubbed “**Union API** ” in the CyberCoding article and used by DarkGate.

This technique consists in retrieving the handle of ntdll by inspecting the PEB (Process Environment Block) structure, specifically in the InMemoryOrderModuleList. Then, it searches by hash where 0x240C0388 is the [**adler-32**](https://en.wikipedia.org/wiki/Adler-32) hash of ntdll. Once the handle is retrieved, the module copies its content, section by section, in a newly dedicated memory.

![Union-API lazy loading of the DLL. Source: Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9adc_6a92a3498d1115926b20519d_6a2a6fb362f00361bfd90523.webp)

Union-API lazy loading of the DLL. Source: Sekoia TDR Team

Whereafter, the loader sets the way syscall must be invoked regarding the CPU architecture. The loader is CPU architecture agnostic, it configures a redirect function concerning the type of architecture that is detected, using WOW32Reserved function where for x64 it uses: 

`lea edx, [esp + argX]   
call large dword ptr fs:0C0h  
`

and x86 architecture uses:

`__asm { sysenter }`

Each syscall has its own number of parameters, callee function pushes an array of parameters and calls the unioned API function with the array of parameters and the number of parameters (which is predefined by the callee). The number of parameters is used in a switch case to dispatch the call to the ntdll api with the correct amount of parameters. _E.g._ :

`ApiCall32(“NtfunctionName”, [1, 2, 3], 3)`

![Switch case used to invoke the conform version of ntdll Api call.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9aed_6a92a340692919148899ac7f_6a2a6fb362f00361bfd90507.webp)

Switch case used to invoke the conform version of ntdll Api call.

Each parameters are previously push on the stack before calling the system call stubs. And the syscall number is moved into EAX register.  
To get the syscall number corresponding to the provided ntdll function name, the module loops over the IMAGE_DIRECTORY_EXPORT->AdddressOfNames until the provided hash match the hash obtains from the function name in IMAGE_DIRECTORY_EXPORT->AddressOfNameOrdinals.

![Get syscall number](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9af9_6a92a33f2b0ef7af46bcf6ea_6a2a6fb362f00361bfd90504.webp)

Get syscall number

Here is an example of code used by DarkGate to write executable code into another process memory using the union API:

![Example of callee function using the union API technique ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9af6_6a92a34c4c776939a1e0bb0e_6a2a6fb362f00361bfd9052e.webp)

Example of callee function using the union API technique 

Malware author(s) use(s) this technique in conjunction with code obfuscation to make the analysis and detection of the malicious code even more challenging.

### Dynamic API resolution

As many other malware, DarkGate also uses dynamic API resolution:

  1. **Dynamic Loading** _:_ Dynamic API resolution involves loading external libraries or APIs into a program's memory during runtime. 
  2. **Function Pointers** : To access functions within dynamically loaded libraries or APIs, the malware uses function pointers. Function pointers are variables that store the memory address of a function within the loaded library. These pointers are assigned and invoked at runtime.



Each time DarkGate calls a function from DLLs usually tracked by AV, it dynamically loads the function using GetProcAddress from Kernel32 DLL. The function takes the name of the function to load as a parameter (the name is decoded from its base64 form using the first alphabet) and returns the _address_ of the desired function that is assigned to a _function pointer_. The function pointer is _invoked_ just after being assigned with its custom parameters.

![Example of code calling a DLL function using Dynamic API resolution](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9af3_6a92a344e36224e46e90df41_6a2a6fb362f00361bfd90514.webp)

Example of code calling a DLL function using Dynamic API resolution

  1. The caller function passes the parameters of the function to resolve, then the function decodes the function name (base64 with the custom alphabet). 
  2. Uses GetProcAddress from Kernel32.dll to get the address (type FARPROC) of the function
  3. Calls the function pointer with the parameters pushed by the caller function.



### Token thief via UpdateProcThreadAttribute

Many security solutions based on behaviour analytics leverage detection rules based on the parent-child process relationship. As part of its MaaS kit, DarkGate provides to its customers the possibility to spoof a specific process identifier to execute a _cmd.exe_. 

Windows introduced the PROC_THREAD_ATTRIBUTE_PARENT_PROCESS attribute in Windows 8.1 and Windows Server 2012 R2, which allows programmers to specify a parent process handle when creating a new process. This is used for purposes like creating child processes in job objects, but it does not directly allow spoofing the parent PID. It's mainly designed for creating child processes that inherit some characteristics from their parents.

![Code used by DarkGate to exploit the parent PID spoofing technique](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ad0_6a92a34be36224e46e90e4df_6a2a6fb362f00361bfd90529.webp)

Code used by DarkGate to exploit the parent PID spoofing technique

Furthermore, the technique implemented here, in addition to the technique of **spoofing a parent process PID** , allows an attacker to **elevate its privileges**. For instance, targeting a process owned by _NT\SYSTEM_ allows a local administrator to grant its privileges to the _SYSTEM_ one.

In addition to privilege escalation via the token thief, the code in the Figure 16 is used to execute a payload into process memory using [NtCreateThreadEx](https://cocomelonc.github.io/tutorial/2021/12/06/malware-injection-9.html) with the Union API.

Of note, this technique is detailed in the a ”[APT techniques: Token thief via UpdateProcThreadAttribute](https://cocomelonc.github.io/tutorial/2022/10/28/token-theft-2.html)” article written by Cocomelonc.

### LOLBAS DLL loading

**Extexport** is a binary executable that can be found in some Windows systems. It is a legitimate part of the Microsoft Windows operating system and is used for extracting and exporting data from Exchange Server databases. This binary is part of the [**LOLBAS**](https://lolbas-project.github.io/lolbas/Binaries/Extexport/) (Living Off the Land Binaries and Scripts). The binary can be used to load **additional DLLs** located in the _c:\test\_ directory without explicitly importing or executing them. For the loading process to occur, the DLL file must have one of the following names: _sqlite3.dll, mozcrt19.dll, mozsqlite3.dll_. Extexport is a valuable tool for attackers looking to fly under the radar.

![Function that searches extexport.exe to silently load attackers DLL](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ad3_6a92a3439d3b9ef4d8bbbfbb_6a2a6fb362f00361bfd90510.webp)

Function that searches extexport.exe to silently load attackers DLL

This DLLs loading is one of the exploit implements used by DarkGate to leverage its compromission, the loader used this technique in addition to the token thief via UpdateProcThreadAttribute details in the previous section to have an elevated DLL execution.

### APC injection via NtTestAlert

To reduce its footprint on the system and to evade detection, the loader uses APC injection (Asynchronous Process Call) via the NtTestAlert function from ntdll. The technique is used to execute arbitrary code within the address space of another process. 

**Asynchronous Procedure Call** is a function that gets executed asynchronously within the context of a specific thread. It’s a way to queue a function for execution in the context of another thread. 

**APC Queuing** , the NtQueueApcThread system calls are often used to insert an APC into a target thread. These calls allow malware authors to specify the target thread handle and the address of the function (the APC) to be executed within that thread's context.

To perform APC **Injection** , the attacker first allocates memory within the target process and writes the malicious code (here _cmd.exe_) into that memory space. Then, it uses NtQueueApcThread, to queue the address of this memory as an APC in the target thread.To trigger the execution of the injected code, the attacker typically relies on a mechanism that triggers the target thread to execute APCs. While there are several methods to achieve this, in the case of DarkGate, it uses NtTestAlert.

![Function used to create Process in SUSPENDED status](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ae8_6a92a3426017750314a4dbac_6a2a6fb362f00361bfd9050d.webp)

Function used to create Process in SUSPENDED status

As highlighted in the figure above, a new process is created in SUSPENDED state, the handler of the process is appended to a newly created APC queue. To resume the thread in order to execute the _cmd.exe_ , the loader executes the syscall NtTestAlert which causes it to execute any pending APCs.

![Code used to create the APC Queue and call NtTestAlert to start the SUSPENDED process ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9ad9_6a92a34da2f46752fd0191cb_6a2a6fb362f00361bfd90531.webp)

Code used to create the APC Queue and call NtTestAlert to start the SUSPENDED process 

As a copycat of the DarkGate code, here is the functionality re-coded in _C++_ reproducing the parent ID spoofing.

![Example of the PoC to spoof the parent PID part of the token thief technique](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f81584be1e5d9d9afc_6a92a34fdc307112383286db_6a2a6fb362f00361bfd9053e.webp)

Example of the PoC to spoof the parent PID part of the token thief technique

More details and a proof of concept of this technique is available in the article “[ _APC injection via NtTestAlert. Simple C++ malware_](https://cocomelonc.github.io/tutorial/2021/11/20/malware-injection-4.html#nttestalert)”. 

This technique is used by the malware to inject a payload into other process memory, where the payload could be a PE or command line.

### Environment detection

As other malware, DarkGate has an environment detection capability, as it attempts to detect numerous artefacts on the infected host.

The loader looks at physical resources, like the _RAM_ size, the number of _CPU_ , which type of graphical card is present (_e.g.:_ is the card virtualized: _vmware_ , _Microsoft Hyper-V_?).It also verifies that no security solutions are installed on the victim’s machine by looking at the running processes (_uiseagnt.exe, superantispyware.exe, etc._) and also checks the path to installed anti-virus solutions (_e.g.: C:\Program Files\Malwarebytes, C:\ProgramData\Kaspersky Lab, etc._).

![Checking for virtual solution setup for the graphical card](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f91584be1e5d9d9b0c_6a92a350e17eff730b65815a_6a2a6fb562f00361bfd905b2.webp)

Checking for virtual solution setup for the graphical card

The list of paths and binaries checked by DarkGate is provided on our [Github repository](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/DarkGate/scripts/AV_checked.txt).

## Command and Control

The communication with the attacker’s server is made over HTTP, where messages are obfuscated. The HTTP requests rely on POST requests using HTML form.

The first version of DarkGate observed in the wild was communicating with their C2 on the port **2351**(which is defined in the configuration) and **9999** (which is hardcoded in the binary). This changed recently, where DarkGate customer can add alternative C2 (the second one: 9999), as highlighted in this [Tria.ge execution: 231025-ys84bsfb32](https://tria.ge/231025-ys84bsfb32).

![Extract of DarkGate communication](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f91584be1e5d9d9b09_6a92a353dc307112383289ca_6a2a6fb562f00361bfd90607.webp)

Extract of DarkGate communication

The structure of the form data messages.

**Form item**| **Description**  
---|---  
 _id_|  Bot identifier generated at the infection  
 _data_|  Raw message (not always obfuscated)  
_act_|  Action identifier  
  
Table 1. Structure of the form data message 

As introduced in the section “Data Obfuscation”, the form “ _data_ ” is almost always obfuscated. The form “ _data_ ” is the **base64** encoded version of **XOR** data. In this case, the base64 uses the second alphabet and the XOR key is built from the bot identifier. For future investigation Sekoia.io [provides a script](https://SEKOIA-IO/Community - DarkGate/scripts/DarkGate-C2-communication-deobfuscator.py) to deobfuscate the communication.

Based on the reverse engineering technique, we centralised in a table (Annex X) the action identifier and the type of action executed by the malwareIt is worth mentioning that our investigation did not cover the entire action ID range.

Somehow, DarkGate’s communication with the C2 is different compared to its standard obfuscation method (base64 + XOR) on particular action IDs:

  1. Base64 encoding (2sc alphabet) (see CyberChef recipe in Figure 23)
  2. ZLib compressed data
  3. Uncompressed data is a pseudo map where key are integer and value are base64 encoded again with the second alphabet (see CyberChef recipe in Figure 24)



![CyberChef recipe to decode and decompress \(Zlib\) C2 message](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f91584be1e5d9d9b0f_6a92a3512b0ef7af46bd0099_6a2a6fb562f00361bfd905b7.webp)

CyberChef recipe to decode and decompress (Zlib) C2 message

‍

![CyberChef recipe to deobfuscate the decoded message in Figure 23. DarkGate Command&Control \(C2\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f91584be1e5d9d9b12_6a92a352dae089660dfc9580_6a2a6fb562f00361bfd905bb.webp)

CyberChef recipe to deobfuscate the decoded message in the previous image. DarkGate Command&Control (C2)

When it comes to the decoded data from the C2 communication, some data are represented in their hexadecimal wide string format (for exemple action id: 3500).

A correspondence table of the action ID and what it does on the infected host is available [here](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/DarkGate/scripts/action-id-documentations.md).

## Hunting for artefact on infected host

Due to its extensive range of functionalities, DarkGate leaves a multitude of artefacts on the infected host that can be helpful for post compromission hunting, such as registry keys, log and debug files.

The temporary directory is frequently used to drop files (PE, DLL) but also text, logs and debug files. Here is the list of files to look for when hunting for DarkGate infection traces:

  * _C:\temp\tskm_
  *  _C:\temp\id.txt_
  *  _C:\darkgateminertest_
  *  _C:\temp\testgpudec.txt_
  *  _C:\temp\etc.txt_
  *  _C:\temp\xmr.txt_
  *  _C:\temp\a_
  *  _c:\temp\PsExec.exe_
  *  _C:\temp\anydesk.exe_
  *  _C:\temp\rdpwrap.ini_
  *  _C:\temp\test.rdp_
  *  _C:\debug\data.bin_
  *  _C:\test\sqlite.dll_
  *  _C:\test\mozcrt19.dll_
  *  _C:\test\mozsqlite3.dll_



To leverage some of its functionalities, DarkGate overwrite files on the machine: 

  *  _C:\Users\SafeMode\AppData\Roaming\AnysDesk\system.conf_
  *  _C:\Users\ <created user>\AppData\Roaming\AnysDesk\system.conf_



While in the earliest version the loader created the user **SafeMode** , in the more recent one the attacker can define a custom username. 

Modified registry keys:

  * HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
  * HKLM\Software\Policies\Microsoft\Windows NT\Terminal Services
  * HKLM\Software\Policies\Microsoft\Windows NT\Terminal Services\DisableRemoteDesktopAntiAlias
  * HKLM\Software\Policies\Microsoft\Windows NT\Terminal Services\DisableSecuritySettings
  * HKCU:\Software\Microsoft\Terminal Server Client\AuthenticationLevelOverride



Read registry keys:

  * HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\CurrentBuildNumber
  * HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProductName
  * HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\CSDVersion



## Final words

**We assess with high confidence that the threat actors** behind **DarkGate** have advanced skills in malware developpement. However, some elements of their project rely on techniques with PoCs are available in open source (_e.g: Cocomelonc blog posts series on malware developpement_). 

Furthermore, instead of developing its own modules for remote access or for credential stealing, the malware uses legitimate tools (hVNC binary, Nirsoft toolset) that are well detected by security solutions. Nevertheless, the wide range of techniques used make DarkGate unique within the cybercrime landscape. It is also profitable from a threat actor's perspective, independently of their advancement (_e.g.:_ TA577) and their objectives. 

After examining the various **DarkGate** stages (the AutoIT script, its shellcode and also its core), it becomes evident that DarkGate represents a significant threat. Consequently, it is imperative to maintain continuous tracking and monitoring of DarkGate in both the short and long term.

Finally, the analysis of the loader detailed in this report is not exhaustive. The sections of this article related to the execution of piding.exe and to the inter process communication via SendMessage are incomplete, mainly due to the absence, within our surveilled perimeter, of of complete infection cases involving these functionalities.

## MITRE ATT&CK TTPs

**Tactic**| **Technique**  
---|---  
Resource Development| T1608.002 – Stage Capabilities: Upload Tool  
Execution| T1059.001 – Command and Scripting Interpreter: PowerShell  
Execution| T1059.003 – Command and Scripting Interpreter: Windows Command Shell  
Execution| T1106 – Native API  
Persistence| T1547.001 – Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder  
Privilege Escalation| T1548.002 – Bypass User Account Control  
Privilege Escalation| T1055.004 – Process Injection: Asynchronous Procedure Call  
Privilege Escalation| T1134 – Access Token Manipulation  
Defense Evasion| T1134.004 – Parent PID Spoofing  
Defense Evasion| T1027 – Obfuscated Files or Information  
Defense Evasion| T1027.007 – Obfuscated Files or Information: Dynamic API Resolution  
Defense Evasion| T1027.009 – Obfuscated Files or Information: Embedded Payloads  
Defense Evasion| T1070.004 – Indicator Removal: File Deletion  
Defense Evasion| T1112 – Modify Registry  
Defense Evasion| T1140 – Deobfuscate/Decode Files or Information  
Defense Evasion| T1620 – Reflective Code Loading  
Command and Control| T1071.001 – Web Protocols  
Command and Control| T1090.001 – Internal Proxy  
Command and Control| T1104 – Multi-Stage Channels  
Command and Control| T1105 – Ingress Tool Transfer  
Command and Control| T1132.002 – Non-Standard Encoding  
Command and Control| T1219 – Remote Access Software  
Command and Control| T1571 – Non-Standard Port  
Discovery| T1010 – Application Window Discovery  
Discovery| T1057 – Process Discovery  
Discovery| T1082 – System Information Discovery  
Discovery| T1083 – File and Directory Discovery  
Discovery| T1217 – Browser Information Discovery  
Collection| T1056.001 – Keylogging  
  
Table 2. MITRE ATT&CK TTPs