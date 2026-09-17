# Taskloader at the root of a Pay-per-Install infection chain - HarfangLab

- **Source :** harfanglab
- **URL :** https://harfanglab.io/insidethelab/loader-galore-taskloader-at-the-start-of-a-pay-per-install-infection-chain/
- **Date :** 2023-09-28

---

In June 2023, we’ve observed multiple alerts that seemingly came from different sources. A quick search through our telemetry allowed us to identify multiple infected machines across our clients. Although they would sometimes present different behaviour, the initial infection vector stayed the same.

The servers were still actively delivering the initial payloads in early August in an intermittent fashion, and some of the malware sill went undetected by antivirus engines. Even though there has been evidence of TaskLoader infrastructure and payloads being active as early as 2016, we’ve seen it deliver more recent malware such as the recently observed [CustomerLoader](https://blog.sekoia.io/customerloader-a-new-malware-distributing-a-wide-variety-of-payloads/) and the [DotRunpex](https://research.checkpoint.com/2023/dotrunpex-demystifying-new-virtualized-net-injector-used-in-the-wild/) injector via BYOVD technique  _(Bring Your Own Vulnerable Driver)_ to try and terminate protected processes.

The overall attack process has similar TTPs as the [NullMixer](https://securelist.com/nullmixer-oodles-of-trojans-in-a-single-dropper/107498/) seen in mid-2022 and follows many of the same principles but with different infrastructure and newer malware.

We’ve taken this opportunity to dig deeper into the distribution of this malware and present some common malware analysis techniques that can be used to analyze this common threat and determine its capabilities, as well as providing a reliable source of information and analysis to allow the wider community to more effectively investigate these threats.

After analysis, we have reason to believe this is part of a PPI (Pay-per-Install) campaign, which is a kind of Infrastructure-as-a-Service which allows cyber criminals to pay a provider to launch their malicious software on infected machines.

## **Table of contents**

Infection vector

Sitool.exe – Step 1

Tempexec Delphi Installer – Step 2

Inetinfo.exe – Step 3

CustomerLoader

DotRunpeX

LgoogLoader

Fabookie

SmokeLoader

IoC table

## **Overview**

Here is a small schematic to demonstrate the execution flow of the malware.

  
![](https://harfanglab.io/medias/2023/12/image-48.png)

### **Infection vector**

The initial malware came from the `crack4windows[.]com`website, which offers all kinds of supposedly pirated software for free. This is a common vector for malware distribution. For instance, we identified some of the infections came from the download of the `TamoGraph Site Survey`software, used to measure wireless network signal intensity in a building.

The website also advertises other more common software, but they all distribute the same malware. It features fake “stars”, a downloads counter, and “thank you” messages written in different languages to legitimize the activity and lure users into a sense of confidence.

![](https://harfanglab.io/medias/2023/12/image.png)

The download contains a text file with instructions:
    
    
    TamoGraph Site Survey Crack 8.0 Build 271 
    Download link: http[:]//free3pc[.]site/download?id=GDtfLsBrxfU&s=C0B24C23 
    Zip Password: GDtfLsBrxfU_062123

Thee other “file hosting” domains have also been identified at this stage. We noticed that the password always contains the date of the download. The actual payload is hosted in these websites, which when accessed, try to pass as legitimate file sharing websites, although they cannot be used as such or contacted anywhere.

![](https://harfanglab.io/medias/2023/12/image-1-2.png) ![](https://harfanglab.io/medias/2023/12/image-3-1.png)

As it setups scheduled tasks for persistence, it has been previously dubbed as “TaskLoader” by other researchers. It also executes a binary called `sitool.exe`which has the Original Filename of `sihost.exe`to blend in with default Windows tools. The day following our initial investigation, the hash of this particular dropper was different, and it kept being updated regularly with mitigated differences on its detection rate.

### **Sitool.exe** – Step 1

Sitool is the first stage of TaskLoader and is quite simple. A quick analysis with DiE shows us it’s an obfuscated .NET binary.

![](https://harfanglab.io/medias/2023/12/image-2.png) Detect it Easy binary signatures and entropy graph.

Due to how .NET works, we can often decompile it from IL (Intermediate Language) to something that looks very close to its source code. If you’re interested in how .NET works, there is a great [DEFCON](https://media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20presentations/DEFCON-27-Alexandre-Borges-dotNET-Malware-Threats.pdf) talk about .NET malware. The entropy curve shows no significant areas of entropy, meaning this software is likely not packed or encrypted. Encrypted areas may show entropy from values ranging anywhere from 7.2 to 7.9.

Here, we simply used the common tool `de4dot`to deobfuscate the binary. Opening it with DNSpy, we can read some of its decompiled code. It seems to be a very simple task creator with primitive anti-analysis functionality. The following images show the main functions used by this binary.

![](https://harfanglab.io/medias/2023/12/image-4-2.png) Usage of the de4dot tool. ![](https://harfanglab.io/medias/2023/12/image-5.png)

The Main function used to create and start scheduled tasks.

![](https://harfanglab.io/medias/2023/12/image-6.png) Function to check if analysis processes are running.

The binary retrieves an encoded JSON in text form, which it uses to download a new payload and execute it from a temporary folder. The domain from which is gets its charge is different according to each case, although here it comes from the domain `avkit[.]org`.

![](https://harfanglab.io/medias/2023/12/image-7.png) Function used to retrieve a payload an creating a Task to run it.

After fuzzing the ID parameters in the domains that were used in the most recent attacks, we emulated the very simple decoding function which is called “DecryptSimpleString” to be able to read the JSON contents.

![](https://harfanglab.io/medias/2023/12/image-8.png) Reverses the string and removes predefined characters.

Even though we found multiple payloads encoded differently, they all decoded to the same string at the time of writing
    
    
    [{"m_guid":"<Date>","m_name":"weblo","m_fileurl":"http://hiapps[.]site/getmodule","m_cmdline":"/verysilent /n /pro /channel oki","m_log":""}]

With this, we found a new domain from which a _payload_ is distributed, `hiapps[.]site`. The command-line is also unique to this _payload_ and allowed us to better identify this program.

In the following figure, we can see with the given URL that this website has been delivering _payloads_ as early as 2017, and some samples that we found on VirusTotal from 2016 already included strings which contacted the `avkit[.]org`.

![](https://harfanglab.io/medias/2023/12/image-10-1024x152-1.png) WayBackMachine showing archived payload from 2017. ![](https://harfanglab.io/medias/2023/12/image-11.png) Sample first submitted in 2016.
    
    
    $ strings -a -el 1233132217d54e63701e4701c8e2cd28c475eed63707a87050ca2a17a5d1a08d.bin
    [...]
    SoftwareMail.RuTechPartnerLogComponentsDse
    SoftwareMail.RuTechPartnerLogComponentsVbm
    SoftwareMail.RuTech
    /transfer "down" "{0}" "{1}"
    bitsadmin.exe
    location.txt
    www.avkit.org
    UA-71688099-1
    54.171.215.105
    Start
    [...]

_Strings relative to the previous sample showing avkit[.]org and Google Container IDs (seen later) stayed the same._

### **Tempexec Delphi Installer – Step 2**

Once this charge has been retrieved, it’s renamed to a random 18-character name, put in the Windows Temp folder and executed. For practical purposes we renamed this “Tempexec”. Here is a command-line example:

`C:UsersuserAppDataLocalTemp\y7i2l2t6j1f0ttcts1v2r3r4a7k8k6r3.exe /verysilent / n /pro /channel oki`

Delphi is a language that evolved from Turbo Pascal for Windows and is often used to make install wizards.

Delphi is also often a language of choice for malware authors packing their wares. There [has been discussions on the subject](https://0x00sec.org/t/delphi-for-malware/22923) and reports from security vendors such as [Mandiant](https://www.mandiant.com/resources/blog/increased-use-of-delphi-packer-to-evade-malware-classification).

One of the install wizards written in Delphi is InnoSetup. It is a program which allows developers to create installers for Windows. These installers are now often used as a packer by malware authors since legitimate programs using it are often tagged as malicious by security software. This is a strategy to make it look like any alerts at this stage are false-positives. [ [1]](https://stackoverflow.com/questions/24864545/inno-setup-executable-seen-as-a-virus), [[2](https://stackoverflow.com/questions/68834409/program-installed-with-inno-setup-seen-as-trojan-wacatac-bml)]

It is nothing too complex. As we can see in `PEStudio`, the Overlay section (Which is simply data that has been appended to a PE), contains the InnoSetup signature. The _payload_ can be extracted by `innoextract`, an open source tool.

![](https://harfanglab.io/medias/2023/12/image-11-1.png) PEStudio identifies the InnoSetup overlay. ![](https://harfanglab.io/medias/2023/12/image-12.png) innoextract tool output.

Some newer versions of this stage, seen in August 2023, use very old versions (prior to 1.1.0) of InnoSetup, which innoextract cannot extract. Nevertheless, at the time of writing, we have not yet seen these new versions exhibit malicious behavior, or execute successfully. We therefore believe that this _payload_ is still under development.

InnoSetup can be scripted; so, according to the process tree, it spawns a second process that is only used to launch the `inetinfo` binary with command line arguments inherited from its parent.

### **Inetinfo.exe – Step 3**

This is where the main functionality of TaskLoader resides. It is again a .NET binary that has been obfuscated with Reactor. It starts by initializing a class with a dictionary associating keys to certain payloads. 

![](https://harfanglab.io/medias/2023/12/image-13.png) Objects associated with payloads being put in a dedicated dictionary

These classes `KControl` have a `Start` Method which will download and launch a payload according to their keys through the class `ProviderUrl`.

This class also requests `iplogger[.]org` which gives the attacker a way to log which IP addresses have executed a certain _payload_ .

It also checks registry keys corresponding to each payload to know if the malware has already been installed. 

![](https://harfanglab.io/medias/2023/12/image-14.png) IPLogger request and registry key install checks. ![](https://harfanglab.io/medias/2023/12/image-15.png) Payload URL to key association. ![](https://harfanglab.io/medias/2023/12/image-16.png) The “pac” payload naming convention.

Interestingly, the `RunItems` function calls upon `method_2` Which will send information such as the IP and the country where the _payload_ s being run and send it back to a **Google Analytics** dashboard. This corroborates that this _loader_ may be part of a _Loader-as-a-Service, campaign_ as this sort of data being sent to services like `iplogger` and `GAnalytics` are typical methods of _Pay-per-Install operations._.

![](https://harfanglab.io/medias/2023/12/image-17.png) RunItems function payload execution. ![](https://harfanglab.io/medias/2023/12/image-18.png) Methods for sending data to Google Analytics.

We we’re able to extract the data of the Google Analytics dashboard in debug mode:

`ContainerClass.Ec = "oki";`

`ContainerClass.Tid = "UA-71688099-1";`

`ContainerClass.HomeDom = "freesmartsoft[.]com";`

The command-line options also included some extra functionality:

![](https://harfanglab.io/medias/2023/12/image-20.png) The “/pro” command-line option modifies the DACL of the current process to deny rights to the Everyone group. ![](https://harfanglab.io/medias/2023/12/image-21.png) Following execution, the binary auto-deletes.

## **Payloads**

In this section we will go over the different payloads we’ve seen deployed in our telemetry. This section will serve mostly as a short reference to the malwares we’ve seen and point to the different references and techniques that aided us in our analysis, providing updates where we’ve seen changes. It is in no way an exhaustive list of all the payloads TaskLoader may deliver, as these may evolve over time, but rather show the general intention which is generally criminal activity used to gain initial access to a network or expand infrastructure.

### **CustomerLoader**

The samples we’ve seen use more recent versions of DotRunpeX, a .NET injector observed in the wild by [CheckpointResearch](https://research.checkpoint.com/2023/dotrunpex-demystifying-new-virtualized-net-injector-used-in-the-wild/) in March, 15 2023 and studied again after it regained popularity by the Sekoia.io analysts in July, 12 2023, who studied the a new loader who also used it and dubbed it [CustomerLoader](https://blog.sekoia.io/customerloader-a-new-malware-distributing-a-wide-variety-of-payloads/). We saw the same C2 servers (such as 5[.]42[.]94[.]169) that were mentioned in Sekoia’s article. 

![](https://harfanglab.io/medias/2023/12/image-22.png) ![](https://harfanglab.io/medias/2023/12/image-23.png) CustomerLoader sample calling old CustomerLoader C2 and executing the downloaded payload. ![](https://harfanglab.io/medias/2023/12/image-24.png) RastaMouse’s AMSI MemoryPatching, as also seen by the Sekoia.io analysts.

As these have been extensively documented in other articles and as the differences we encountered are very minor, we won’t be analyzing them further.

### **DotRunpeX**

A lot of the payloads we saw use the DotRunpeX file to inject the malware into processes. However, upon executing for dynamic analysis, we saw the typical alerts we’d expect from this injector, such as the UAC Bypasses documented by Checkpoint Research.

![](https://harfanglab.io/medias/2023/12/image-1-1.png) Various detections from the the payloads execution. ![](https://harfanglab.io/medias/2023/12/image-2-1.png) .inf file used with cmstp for UAC Bypass.

This .inf file was copied-pasted from Open-Source [GitHub](https://oddvar.moe/2017/08/15/research-on-cmstp-exe/) projects.

![](https://harfanglab.io/medias/2023/12/image-49.png)

[Blog](https://oddvar.moe/2017/08/15/research-on-cmstp-exe/) post by Oddvarmoe on bypassing UAC with CMSTP.

The usage of typical tools such as the [OldRod Deobfuscator](https://github.com/Washi1337/OldRod) didn’t wield any results, meaning this is a version that has been modified to bypass common analysis tools. This kind of obfuscation was previously observed by the Checkpoint Researchers in the aforementioned article.

While previous articles documented DotRunpeX using the `procexp`he driver that was loaded here was the `Zemana.sys`driver. Exploitation of this legitimate driver was a technique used to terminate EDRs that became popular in May 2023 when an user going by the handle `spyboy` advertised a [$3,000 tool to terminate all antivirus and EDR](https://twitter.com/S0ufi4n3/status/1663059373352943616/). It has since then been [replicated in open source projects](https://github.com/ZeroMemoryEx/Terminator). The BYOVD technique ([Bring Your Own Vulnerable Driver](https://www.sangfor.com/farsight-labs-threat-intelligence/cybersecurity/what-is-byovd-attacks-2023)) is used to kill protected processes and is now commonly seen in the wild. _in the wild_ It can now be considered general knowledge among adversaries and the usage of this driver by the DotRunpeX injector is also in accordance to what previous researchers [have seen.](https://twitter.com/_CPResearch_/status/1692468130776318230).

![Post Twitter &quot;EDR killer tools be like&quot;](https://harfanglab.io/medias/2023/09/twitter-edr-florian-roth.png)

The CERT-PL has recently done an [excellent article ](https://cert.pl/en/posts/2023/09/unpacking-whats-packed-dotrunpex/)on extracting the malware embedded in the resources of the injector, this warranted further research into the payloads so we used their key dumping tool to continue our analysis.

![](https://harfanglab.io/medias/2023/12/dotrunpex-key-ext.png) CERT-PL’s tools sucessfully extracting the resource encryption key.

### **LgoogLoader**

Once extracted and decrypted, we can see that one of the payloads tries to pass as a legitimate version of Windows Sysinternals ShellRunas tool. We’ve identified this as the LgoogLoader, and since we’ve seen little to no technical analysis of this malware so far, we’ve decided this is an opportunity give more information as to the internal working of this malware.

![](https://harfanglab.io/medias/2023/12/image-13-1.png) Resource information mimicking the ShellRunas tool.

The binary starting by loading some strings into the stack and then decrypting them, it does this with simple xor operations. These correspond to function names that will probably be used to resolve their addresses.

![](https://harfanglab.io/medias/2023/12/image-16-1.png) XOR Loops for decrypting strings. ![](https://harfanglab.io/medias/2023/12/image-17-1.png) Result after quickly XORing them in a script.

Given these strings, we can assume that they will be used to dynamically resolve the address of these functions, the same operation is repeated multiple times with different strings

![](https://harfanglab.io/medias/2023/12/image-18-1.png) More decrypted strings in memory.

The decryption of “kernel32.dll”, “GetModuleHandle”, “VirtualAlloc” and “GetProcAddress” usually indicate that this sample will resolve the address of certain functions and allocate memory to decrypt itself and execute the malicious payload without touching the disk. This is usually the behaviour of what we call “packed” malware.

With this information, we decided to find out which imports this binary used with the [Miasm framework](https://miasm.re/blog/). This framework allows us to create Python scripts that emulate code execution using its own JIT. This allows us to hook certain WinAPI calls to inspect and modify their behaviour, allowing us to bypass anti-debugging techniques without having to patch them manually. Another advantage is, if the script is written correctly, it may be used to unpack future similar samples. Although in this case, as we’ll see next, a debugger script will be more appropriate.

![](https://harfanglab.io/medias/2023/12/image-19.png) Here, we intercept the GetProcAddress function to write the API functions used by the malware to a file. ![](https://harfanglab.io/medias/2023/12/image-20-1.png) Interesting imported functions, indicating capabilities of HTTP communication.

We were also confronted with anti-debug techniques, such as checking that a Display is present or opening Raw Devices like the MBR, in order to verify their names.

![](https://harfanglab.io/medias/2023/12/image-22-1.png) If the Display Registry keys are not opened successfully, the program terminates itself. ![](https://harfanglab.io/medias/2023/12/image-29.png) Code checking for the EDID (Extend Display identification) of a monitor, and checking its validity. EDIDs usually aren’t emulated in certain VM software.

It would be quite tedious to patch each check manually, so we’ve prepared an x64dbg script to automate our debugging process.

This will usually fail in some step or another depending on the sample you have. Instead of trying to patch the control flow of the function to ignore the checks and verification of the EDID parameter. We decided that adding this registry key to our VM was simpler:

`HKEY_LOCAL_MACHINESYSTEMControlSet001EnumDISPLAYDefault_Monitor<monitor>Device ParametersEDID.`

![](https://harfanglab.io/medias/2023/12/image-32.png) Add a valid EDID value to the registry after retrieval [ from this repository](https://github.com/linuxhw/EDID). ![](https://harfanglab.io/medias/2023/12/image-33.png) After opening the MBR by using CreateFileW on \\.PhysicalDrive0 and use the DeviceIOControl call to check it against a list of predefined names for virtual machine prefixes.

One of the anti-debug techniques used by LgoogLoader is trying to open it’s own file in exclusive access mode. When a process is started for debugging, a _handle_ to the file is stored when the CREATE_PROCESS_DEBUG_EVENT event occurs, if that _handle_ is not closed, then the file can’t be opened for exclusive access. This is a known issue with `x64dbg`but it is not present in other debuggers __such as`OllyDbg`, making it somewhat unreliable.

![](https://harfanglab.io/medias/2023/12/image-36.png) CreateFileW anti-debug technique.

After these AntiDebug and AntiVM checks, it will then inject itself into another process using the [injection technique `RunPE`](https://unprotect.it/technique/process-hollowing-runpe/). We won’t go into details of how it works here, but it consists of creating a new process in suspended mode, and uses `VirtualAllocEx` and `WriteProcessMemory` to write its _payload_ into the child process, and uses `SetThreadContext`followed by `ResumeThread` calls to change the execution flow of the child process’s main thread.

![](https://harfanglab.io/medias/2023/12/image-37.png) Code snippet showing the writes the different sections of the PE header to avoid a single breakpoint PE dump and then resuming the thread

We can then attach ourselves to the new process using the debugger and resume the thread to see the payload’s execution flow. We then start seeing the process trying to download it’s encrypted config containing a payload. However, the domain seen in our infections was already inactive when we analyzed it.

![](https://harfanglab.io/medias/2023/12/image-38.png) The UserAgent used in the HTTP request. ![](https://harfanglab.io/medias/2023/12/image-39.png) URL used in our sample to retrieve the configuration.

Here is the `x32dbg` script used that allowed us to automate the analysis up to the injection point. It’s not meant to be used as is and work with all samples but rather give an idea of how to proceed to write scripts that analyze binaries like this.
    
    
    bc ; Clear breakpoints
    bphwc
    
    bp CreateFileW
    run
    rtr ; run to return
    step
    bpd CreateFileW
    
    ; Find first Hardware MBR name check
    
    zzz 100
    
    find eip,"8D85C8F7FFFF68????????50"
    log "found {0}", $result
    bp $result
    
    run
    
    ; Patch name
    memset ebp-838, A, 32
    
    ; Find second hardware Display device name check
    find eip,"8D8540FDFFFF68????????50"
    log "found {0}", $result
    bp $result  
    
    run
    
    ; Patch name
    memset ebp-2C0, A, 64
    
    ; AntiDebug - Opening itself and trying to set info
    bpe CreateFileW
    
    run
    run
    
    ; Patch CreateFile stack to succeed
    mov [esp+8], 00080000
    mov [esp+C], 00000007
    rtr
    step
    
    ; Patch set file information handle, this isn't important
    bp SetFileInformationByHandle
    run
    rtr
    mov eax, 1
    step
    
    ; Patch second CreateFile
    run
    mov [esp+8], 00080000
    mov [esp+C], 00000007
    rtr
    step
    run
    
    ; Patch second SetFileInfo
    rtr
    mov eax, 1
    step
    
    ; disable these breakpoints and move forward
    bpd CreateFileW
    bpd SetFileInformationByHandle
    
    ; Another round of GetProcAddress
    
    bp GetProcessHeap
    run
    rtr
    step
    
    bpd GetProcessHeap
    bp CreateProcessW
    run
    rtr
    step
    
    ; Here it should resume the thread which it hijacked in the new process
    bp SetThreadContext
    run
    
    ; Continue by attaching to the new process with a debugger and resuming the thread.
    ; Or 
    ; Look at [[esp+4]+0xb8] (It should contain the _CONTEXT structure from the SetThreadContext call), this gives us the EIP.
    ; You can dump the executable with tools such as pd64.exe and adjust its context in the debugger as you wish.

### **Fabookie**

Fabookie is a malicious software targeting Facebook Ads. In our specific case, the samples were trying to disguise as dxdiag.exe, a legitimate DirectX tool.

![](https://harfanglab.io/medias/2023/12/image-43.png) Attempt to disguise itself as DxDiag.

Fabookie steals Facebook session cookies from web browsers and employs Facebook Graph API Queries to gather more details about a user’s profile, connected payment methods, account balance, friends, and more. These hijacked credentials can subsequently be employed to launch ads using the victim’s account. This particular sample contacts it’s C2 servers and downloads an image, which contains the final Fabookie payload.

![](https://harfanglab.io/medias/2023/12/image-44.png) HTTP request of an imagc JPEG in Wireshark. ![](https://harfanglab.io/medias/2023/12/image-46.png) binwalk shows us there’s a PE within the image and allows us to extract it. ![](https://harfanglab.io/medias/2023/12/image-47.png) Strings of the Facebook billing API in the extracted PE.

We’ve added the domains and hashes to the IoC table but won’t be looking at this malware any further as it is well-known.

### **SmokeLoader**

SmokeLoader is a modular malware downloader first observed in 2011. It uses code obfuscation, API function resolution, and sandbox detection for evasion. After execution, it establishes persistence and contacts a C2 server to download additional payloads like banking trojans or ransomware, the C2s we’ve seen were already inactive by the time we investigated them. It also employs process injection techniques for stealth. Over the years, it has undergone various updates and revisions, making it a continually evolving sophisticated threat.

The inner workings of this loader deserve an article of its own. However, there is already literature from a few years back describing the [most of its features](https://n1ght-w0lf.github.io/malware%20analysis/smokeloader/).

![](https://harfanglab.io/medias/2023/12/image-4-1.png) Code for hashing Library and function names in first stage shellcode. ![](https://harfanglab.io/medias/2023/12/image-5-1.png) Hashing emulation with the Miasm framework. ![](https://harfanglab.io/medias/2023/12/image-6-1.png) Opaque predicate

### **Conclusion**

After an extensive analysis of the data and patterns across our telemetry, it’s clear that the infections we’ve observed are part of a coordinated PPI campaign. The use of common initial infection vectors and active C2 servers indicate that this is an ongoing operation with simple but time-tested and effective methods of compromise.

What’s alarming is the long history and adaptability of this infrastructure. The fact that some aspects date back as far as 2016 demonstrates both resilience and a continual development cycle, including the ability to deliver newer forms of malware like CustomerLoader.

We’ve laid out some analysis techniques that can be employed to study this threat further. Companies should update their IoC tables and implement strict security measures. We will continue to monitor this threat closely and provide updates as more information becomes available.

## **IoC table**

While an IoC table is provided, it should be used more of an anchor for other researchers to pivot and for the wider cybersecurity community to act on rather than a foolproof detection method. HarfangLab’s EDR has used Sigma and Yara rules to block the threats described in this article.

**Fabookie Stealer**  
---  
072cdef00c51d1c76eaa74cfc008890cd95288a745796963b441236ada7c1f73   
07d7f33376901a832dbdb441e57d72390d28225cd5fe5042f9048e5d55f40493  
155dd3b4d2665fc6486167b4f8ee758f5a848039216c76614ebf3167990e9ec6  
2c389fe6cbdf4948992278c96a3341f7d05659c5fd913d8eccea651961f496fd  
us[.]imgjeoigaa[.]com  
app[.]nnnaajjjgc[.]com  
**DotRunpeX** (LgoogStealer)  
b120d8658812d9d5dd2b0322b3e7aefa5d34ee2acaebdf15a8ef2d73f9743f22  
2f4daafe79aa0dc29829991c3983f35cae602c8e6ab1de28f7cfc95e2160a66  
109[.]206[.]241[.]33  
**CustomerLoader** (DotRunpeX)  
3d85c2571969b2a54f61f766f8b4ec4e167048d9b28b63ef742e7c0114d4f575  
4c9b551910643eb2c5a4adaf517f41cf1c5035c1526b11f108accd970e675e31  
**SmokeLoader**  
1df80330b824fe5e09ee3b12f1cdab76c223a627b54ccda3188945317c1f90a4  
**Initial Compromise Websites**  
crack4windows[.]com  
free1app[.]site  
free2app[.]site  
free3app[.]site  
freesmartsoft[.]com  
**Sitool.exe (TaskLoader Stage 1)**  
a6d9ebae8cadfd1f6e90cc8ebaf88eeee9dc98e73c10cd9d0c67fef35099e96f  
e2dcb80bcf46dbd1d44adb6ee0cd7a39e2c4829632fd94c83bba70c3907c52fb  
7bbca270f423c44dbcf5bcbe1db17fbbd9e701619dea1ef9c6086b7ecee8c6bb  
video-box[.]org  
avkit[.]org  
**Tempexec Delphi Installer**  
b278922ccdd484c70503d72ed4f747b77a869b40e7f632d1bef6a2f80011de36  
61581f8f1f64f392d7c887f1f6ae2ea0b6638b5deb2a9731094ae64f3d7d43d4  
9c81817acd4982632d8c7f1df3898fca1477577738184265d735f49fc5480f07  
hiapps[.]site  
**Inetinfo**  
37517181539521918488ce48e50196caf3afdfc1a87cec9bc524e8fc065ed81e  
hhk[.]ghwiwwhh[.]com  
ashoktodmal[.]com  
45[.]12[.]253[.]74  
85[.]217[.]144[.]228  
  
[ ![HarfangLab cyber threat research blog post about UAC-0057](https://harfanglab.io/medias/2025/08/sover1-424x283.png) Identifier: TRR250801. Summary In late July, we identified two clusters of malicious archives that were leveraged to target Ukraine and Poland since April 2025, and that we could link together from their similarities. Resulting infection chains are aimed at collecting… ](https://harfanglab.io/insidethelab/uac-0057-pressure-ukraine-poland/)[ ![2025 Threatscape report](https://harfanglab.io/medias/2024/12/banner-globe7-424x283.png) Looking ahead to 2025, we acknowledge that predicting the future is never an exact science. However, by analyzing emerging trends and patterns, we aim to anticipate the risks that could shape the cybersecurity landscape in the year to come, with… ](https://harfanglab.io/insidethelab/2025-cyber-threatscape-predictions/)[ ![APR31 indictment heading](https://harfanglab.io/medias/2024/04/apt31-indictment-heading-424x283.png) Identifier: TRR240401 On March 25, 2024, the U.S. Department of Justice (DoJ) released an indictment of seven hackers associated with APT31, a “hacking group in support of China’s Ministry of State Security” (MSS) which has been active for 14 years.… ](https://harfanglab.io/insidethelab/apt31-indictment-analysis/)[ ![Cyclops: a likely replacement for BellaCiao](https://harfanglab.io/medias/2024/08/cyclops-banner-424x283.jpg) Identifier: TRR240801. Summary This report introduces Cyclops, a newly discovered and previously undocumented malware platform written in Go which dates back to December 2023, and that we believe has been deployed against targets in the Middle-East in 2024. Cyclops allows… ](https://harfanglab.io/insidethelab/cyclops-replacement-bellaciao/)