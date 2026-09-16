# Fake Update Utilizes New IDAT Loader To Execute StealC and Lumma Infostealers | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2023/08/31/fake-update-utilizes-new-idat-loader-to-execute-stealc-and-lumma-infostealers/
- **Date :** 2025-06-02

---

_Technical Analysis by: Thomas Elkins, Natalie Zargarov_ _  
__Contributions: Evan McCann, Tyler McGraw_

Recently, Rapid7 observed the Fake Browser Update lure tricking users into executing malicious binaries. While analyzing the dropped binaries, Rapid7 determined a new loader is utilized in order to execute infostealers on compromised systems including StealC and Lumma.

The IDAT loader is a new, sophisticated loader that Rapid7 first spotted in July 2023. In earlier versions of the loader, it was disguised as a 7-zip installer that delivered the SecTop RAT. Rapid7 has now observed the loader used to deliver infostealers like Stealc, Lumma, and Amadey. It implements several evasion techniques including Process Doppelgänging, DLL Search Order Hijacking, and Heaven's Gate. IDAT loader got its name as the threat actor stores the malicious payload in the IDAT chunk of PNG file format.

Prior to this technique, Rapid7 observed threat actors behind the lure utilizing malicious JavaScript files to either reach out to Command and Control (C2) servers or drop the Net Support Remote Access Trojan (RAT).

The following analysis covers the entire attack flow, which starts from a new ClearFake malware, spotted just several days ago, and ends with the stolen information in threat actors’ hands.

## Technical Analysis

Threat Actors (TAs) are often staging their attacks in the way security tools will not detect them and security researchers will have a hard time investigating them.

![minerva_blog_image-cf.png](https://www.rapid7.com/cdn/images/blt8f5ea4ef3b98bb6c/683de07cc26e07cd8f28e778/minerva_blog_image-cf.png)

### Stage 1 - ClearFake

[ClearFake](https://rmceoin.github.io/malware-analysis/clearfake/) is a new malware first recognized just a few days ago. Its campaign started on July 19,2023 which aligns with the time Rapid7 spotted a new IDAT loader distribution. We first attributed that initial attack flow to the SocGolish malware, however the ClearFake seems to be less sophisticated. 

In this campaign, ClearFake malware uses base64 to obfuscate malicious Javascript, which can be easily deobfuscated by using [CyberChef](https://gchq.github.io/CyberChef/). As spotted by [Randy McEoin](https://infosec.exchange/@rmceoin), the “One noticeable difference from SocGholish is that there appears to be no tracking of visits by IP or cookies. As an analyst you can you go back to the compromised site over and over coming from the same IP and not clearing your browser cache. This also means the site owner is more likely to see the infection as well.”

![Screenshot-2023-11-07-at-10.22.04-AM.png](https://www.rapid7.com/cdn/images/bltefb1db594888e0fc/683de0a1da5c301f89a8349a/Screenshot-2023-11-07-at-10.22.04-AM.png)

This prompt falsely presents itself as a browser update, with the added layer of credibility coming from the fact that it appears to originate from the intended domain.

![Screenshot-2023-11-07-at-10.22.50-AM.png](https://www.rapid7.com/cdn/images/blt5c8dbfc031283f59/683de0c93e68ee1f6a889994/Screenshot-2023-11-07-at-10.22.50-AM.png)

Once the user interacts with the “Update Chrome” button, the browser is redirected to another URL where a binary automatically downloads to the user's default download folder. After the user double clicks the fake update binary, it will proceed to download the next stage payload. In this investigation, Rapid7 identified a binary called _**ChromeSetup.exe**_ , the file name widely used in previous SocGholish attacks and now adopted by ClearFake.

### Stage 2 - MSI Downloader

 _**ChromeSetup.exe**_ downloads and executes the Microsoft Software Installer (MSI) package from: _**hxxps://ocmtancmi2c5t[.]xyz/82z2fn2afo/b3/update[.]msi**_.

In similar investigations, Rapid7 observed that the initial dropper executable appearance and file name may vary depending on the user’s browser when visiting the compromised web page. In all instances, the executables contained invalid signatures and attempted to download and install an MSI package. 

Rapid7 determined that the MSI package executed with several switches intended to avoid detection:

  * /qn to avoid an installation UI
  * /quiet to prevent user interaction
  * /norestart to prevent the system from restarting during the infection process



When executed, the MSI dropper will write a legitimate _**VMwareHostOpen.exe**_ executable, multiple legitimate dependencies, and the malicious Dynamic-Link Library (DLL) file _**vmtools.dll**_. It will also drop an encrypted _**vmo.log**_ file which has a PNG file structure and is later decrypted by the malicious DLL.   
Rapid7 spotted an additional version of the attack where the MSI dropped a legitimate _**pythonw.exe**_ , legitimate dependencies, and the malicious DLL file _**python311.dll**_.**** In that case, the encrypted file was named _**pz.log**_ ,**** though the execution flow remains the same.

![Screenshot-2023-11-07-at-10.25.02-AM.png](https://www.rapid7.com/cdn/images/blt0a2a860e3cc84f51/683de0eeaaf620a4d679deac/Screenshot-2023-11-07-at-10.25.02-AM.png)

### Stage 3 - Decryptor

When executed, the legitimate _**VMWareHostOpen.exe**_ loads the malicious _**vmtools.dll**_**** from the same directory as from which the _**VMWareHostOpen.exe**_**** is executed. This technique is known as [DLL Search Order Hijacking.](https://attack.mitre.org/techniques/T1574/001/)

During the execution of _**vmtools.dll**_ , Rapid7 observed that the DLL loads API libraries from _**kernel32.dll**_ and _**ntdll.dll**_ using API hashing and maps them to memory. After the API functions are mapped to memory, the DLL reads the hex string _**83 59 EB ED 50 60 E8**_ and decrypts it using a bitwise XOR operation with the key _**F5 34 84 C3 3C 0F 8F**_ , revealing the string _**vmo.log**_. The file is similar to the _**Vmo\log**_ directory, where Vmware logs are stored. 

The DLL then reads the contents from _**vmo.log**_ into memory and searches for the string _**…IDAT**_. The DLL takes 4 bytes following _**…IDAT**_ and compares them to the hex values of _**C6 A5 79 EA**_. If the 4 bytes following _**…IDAT**_ are equal to the hex values **C6** _**A5 79 EA**_ , the DLL proceeds to copy all the contents following _**…IDAT**_ into memory.

![Screenshot-2023-11-07-at-10.25.54-AM.png](https://www.rapid7.com/cdn/images/blt99e697ad40c2b081/683de1118ac17c363c29ae29/Screenshot-2023-11-07-at-10.25.54-AM.png)

Once all the data is copied into memory, the DLL attempts to decrypt the copied data using the bitwise XOR operation with key _**F4 B4 07 9A**_. Upon additional analysis of other samples, Rapid7 determined that the XOR keys were always stored as 4 bytes following the hex string _**C6 A5 79 EA**_.

![Screenshot-2023-11-07-at-10.26.38-AM.png](https://www.rapid7.com/cdn/images/blt78595aa20f7c1b14/683de13a3e68eea6eb8899c6/Screenshot-2023-11-07-at-10.26.38-AM.png)

Once the DLL decrypts the data in memory, it is decompressed using the RTLDecompressBuffer function. The parameters passed to the function include:

  * Compression format
  * Size of compressed data
  * Size of compressed buffer
  * Size of uncompressed data
  * Size of uncompressed buffer

![Screenshot-2023-11-07-at-10.27.30-AM.png](https://www.rapid7.com/cdn/images/blt2682c403f0b67c0e/683de15cabf2ad5e973c4405/Screenshot-2023-11-07-at-10.27.30-AM.png)

The _**vmtools.dll**_ DLL utilizes the compression algorithm LZNT1 in order to decompress the decrypted data from the _**vmo.log**_ file.

After the data is decompressed, the DLL loads _**mshtml.dll**_ into memory and overwrites its .text section with the decompressed code. After the overwrite, _**vmtools.dll**_ calls the decompressed code.

### Stage 4 - IDAT Injector

Similarly to _**vmtools.dll**_ ,**** IDAT loader uses dynamic imports. The IDAT injector then expands the _**%APPDATA%**_ environment variable by using the _**ExpandEnvironmentStringsW**_ API call. It creates a new folder under _**%APPDATA%**_ , naming it based on the _**QueryPerformanceCounter**_ API call output and randomizing its value.  


All the dropped files by MSI are copied to the newly created folder. IDAT then creates a new instance of _**VMWareHostOpen.exe**_**** from the _**%APPDATA%**_ by using _**CreateProcessW**_ and exits.  


The second instance of _**VMWareHostOpen.exe**_**** behaves the same up until the stage where the IDAT injector code is called from _**mshtml.dll**_**** memory space. IDAT immediately started the implementation of the Heaven’s Gate evasion technique, which it uses for most API calls until the load of the infostealer is completed.   


Heaven's Gate is widely used by threat actors to evade security tools. It refers to a method for executing a 64-bit process within a 32-bit process or vice versa, allowing a 32-bit process to run in a 64-bit process. This is accomplished by initiating a call or jump instruction through the use of a reserved selector. The key points in analyzing this technique in our case is to change the process mode from 32-bit to 64-bit, the specification of the selector “0x0033” required and followed by the execution of a far call or far jump, as shown in Figure 8.

![Screenshot-2023-11-07-at-10.28.26-AM.png](https://www.rapid7.com/cdn/images/blt1ebefc36193b549e/683de17d2a76862d61bc84ab/Screenshot-2023-11-07-at-10.28.26-AM.png) ![](https://lh6.googleusercontent.com/CKIeq3iK_IHy2wNzhbU9v_3yVZ-ZI8MFxUWv0m8KDCoe-A_D5GUAeNhj9rFde177LKgK73k6yuwTWVf3A4JJQzbHWtAxWoC_UhulLm9k9TqIhH0uv8lcvgzdgH9Z8TwJI47uq0kIBj9Wb8kl92zeWzU)

  
The IDAT injector then expands the _**%TEMP%**_ environment variable by using the _**ExpandEnvironmentStringsW**_ API call. It creates a string based on the _**QueryPerformanceCounter**_ API call output and randomizes its value.  


Next, the IDAT loader gets the computer name by calling _**GetComputerNameW**_ API call, and the output is randomized by using _**rand**_ __ and _**srand**_ API calls. It uses that randomized value to set a new environment variable by using _**SetEnvironmentVariableW**_.**** This variable is set to a combination of _**%TEMP%**_ path with the randomized string created previously.

![Screenshot-2023-11-07-at-10.29.14-AM.png](https://www.rapid7.com/cdn/images/bltd32c111616458358/683de1a1543b8d2787bf11fc/Screenshot-2023-11-07-at-10.29.14-AM.png)

Now, the new _**cmd.exe**_ process is executed by the loader. The loader then creates and writes to the _**%TEMP%\89680228**_ file. 

Next, the IDAT injects code into cmd.exe process by using [**NtCreateSection + NtMapViewOfSection Code Injection**](https://www.ired.team/offensive-security/code-injection-process-injection/ntcreatesection-+-ntmapviewofsection-code-injection)**** technique**.** Using this technique the malware:

  * Creates a new memory section inside the remote process by using the NtCreateSection API call
  * Maps a view of the newly created section to the local malicious process with RW protection by using _**NtMapViewOfSection**_ API call
  * Maps a view of the previously created section to a remote target process with RX protection by using _**NtMapViewOfSection**_ API call
  * Fills the view mapped in the local process with shellcode by using _**NtWriteVirtualMemory**_ API call
  * In our case, IDAT loader suspends the main thread on the _**cmd.exe**_ __ process by using _**NtSuspendThread**_ API call and then resumes the thread by using _**NtResumeThread**_ __ API call  
After completing the injection, the second instance of _**VMWareHostOpen.exe**_**** exits.



### Stage 5 - IDAT Loader:

The injected loader code implements the Heaven’s Gate evasion technique in exactly the same way as the IDAT injector did. It retrieves the _**TCBEDOPKVDTUFUSOCPTRQFD**_ environment variable, and reads the _**%TEMP%\89680228**_ file data into the memory. The data is then recursively XORed with the **3D ED C0 D3** key. 

The decrypted data seems to contain configuration data, including which process the infostealer should be loaded, which API calls should be dynamically retrieved, additional code,and more. The loader then deletes the initial malicious DLL (_**vmtools.dll**_) by using _**DeleteFileW**_.**** The loader finally injects the infostealer code into the _**explorer.exe**_ process by using the Process Doppelgänging injection technique.

The**** Process Doppelgänging**** method utilizes the Transactional NTFS feature within the Windows operating system. This feature is designed to ensure data integrity in the event of unexpected errors. For instance, when an application needs to write or modify a file, there's a risk of data corruption if an error occurs during the write process. To prevent such issues, an application can open the file in a transactional mode to perform the modification and then commit the modification, thereby preventing any potential corruption. The modification either succeeds entirely or does not commence.

Process Doppelgänging exploits this feature to replace a legitimate file with a malicious one, leading to a process injection. The malicious file is created within a transaction, then committed to the legitimate file, and subsequently executed. The Process Doppelgänging**** in our sample was performed by:

  * Initiating a transaction by using _**NtCreateTransaction**_ API call
  * Creating a new file by using _**NtCreateFile**_ API call
  * Writing to the new file by using _**NtWriteFile**_**** API call
  * Writing malicious code into a section of the local process using _**NtCreateSection**_**** API call
  * Discarding the transaction by using _**NtRollbackTransaction**_**** API call
  * Running a new instance of explorer.exe process by using _**NtCreateProcessEx**_ API call
  * Running the malicious code inside explorer.exe process by using _**NtCreateThreadEx**_**** API call  




If the file created within a transaction is rolled back (instead of committed), but the file section was already mapped into the process memory, the process injection will still be performed.

The final payload injected into the _**explorer.exe**_ process was identified by Rapid7 as Lumma Stealer.

![Screenshot-2023-11-07-at-10.29.57-AM.png](https://www.rapid7.com/cdn/images/blt9290176e66ffeeee/683de1cb8ac17c278f29ae65/Screenshot-2023-11-07-at-10.29.57-AM.png)

Throughout the whole attack flow, the malware delays execution by using _**NtDelayExecution**_ , a technique that is usually used to escape sandboxes.

As previously mentioned, Rapid7 has investigated several IDAT loader samples. The main differences were:

  1. The legitimate software that loads the malicious DLL.
  2. The name of the staging directory created within _**%APPDATA%**_.
  3. The process the IDAT injector injects the Loader code to.
  4. The process into which the infostealer/RAT loaded into.
  5. Rapid7 observed the IDAT loader has been used to load the following infostealers and RAT: Stealc, Lumma and Amadey infostealers and SecTop RAT.

![Screenshot-2023-11-07-at-10.30.45-AM.png](https://www.rapid7.com/cdn/images/blt1e8c0fb901f9fc00/683de1f0da5c302bbda83524/Screenshot-2023-11-07-at-10.30.45-AM.png) ![Screenshot-2023-11-07-at-10.31.33-AM.png](https://www.rapid7.com/cdn/images/blt7434f8475c47b3b1/683de2134c5a0970285e0b97/Screenshot-2023-11-07-at-10.31.33-AM.png) ![](https://lh6.googleusercontent.com/xyU47bkeYKtttXdQ9SCSiGEdH4iQPzVF4GYUfqO1OPVA5Bnt3v3-xdstEcNnxIxSMzoKM6kG1Ds2dZMaJ8xvMQnsFyHSoDPnJ9Sf4iOiAYMFCpSwNmLF_2uhoqBt1TGYDBkw3Z9GqYvvs2KRNFOTXac)

## Conclusion

IDAT Loader is a new sophisticated loader that utilizes multiple evasion techniques in order to execute various commodity malware including InfoStealers and RAT’s. The Threat Actors behind the Fake Update campaign have been packaging the IDAT Loader into DLLs that are loaded by legitimate programs such as VMWarehost, Python and Windows Defender.

## Rapid7 Customers

For Rapid7 MDR and InsightIDR customers, the following Attacker Behavior Analytics (ABA) rules are currently deployed and alerting on the activity described in this blog:

  * Attacker Technique - MSIExec loading object via HTTP
  * Suspicious Process - FSUtil Zeroing Out a File
  * Suspicious Process - Users Script Spawns Cmd And Redirects Output To Temp File
  * Suspicious Process - Possible Dropper Script Executed From Users Downloads Directory
  * Suspicious Process - WScript Runs JavaScript File from Temp Or Download Directory



## MITRE ATT&CK Techniques:

Initial Access| Drive-by Compromise (T1189)| The ClearFake Uses Drive-by Compromise technique to target user’s web browser  
---|---|---  
Defense Evasion| System Binary Proxy Execution: Msiexec (T1218.007)| The ChromeSetup.exe downloader (C9094685AE4851FD5A5B886B73C7B07EFD9B47EA0BDAE3F823D035CF1B3B9E48) downloads and executes .msi file  
Execution| User Execution: Malicious File (T1204.002)| Update.msi (53C3982F452E570DB6599E004D196A8A3B8399C9D484F78CDB481C2703138D47) drops and executes VMWareHostOpen.exe  
Defense Evasion| Hijack Execution Flow: DLL Search Order Hijacking (T1574.001)| VMWareHostOpen.exe loads a malicious vmtools.dll (931D78C733C6287CEC991659ED16513862BFC6F5E42B74A8A82E4FA6C8A3FE06)  
Defense Evasion| Deobfuscate/Decode Files or Information (T1140)| vmtools.dll (931D78C733C6287CEC991659ED16513862BFC6F5E42B74A8A82E4FA6C8A3FE06) decrypts vmo.log(51CEE2DE0EBE01E75AFDEFFE29D48CB4D413D471766420C8B8F9AB08C59977D7) file  
Defense Evasion| Masquerading (T1036)| vmo.log(51CEE2DE0EBE01E75AFDEFFE29D48CB4D413D471766420C8B8F9AB08C59977D7) file masqueraded to .png file  
Execution| Native API (T1106)| The IDAT injector and IDAT loader are using Heaven’s Gate technique to evade detection  
Defense Evasion| Process Injection (T1055)| IDAT injector implements NtCreateSection + NtMapViewOfSection Code Injection technique to inject into cmd.exe process  
Defense Evasion| Process Injection: Process Doppelgänging (T1055.013)| IDAT loader implements Process Doppelgänging technique to load the InfoStealer  
Defense Evasion| Virtualization/Sandbox Evasion: Time Based Evasion (T1497.003)| Execution delays are performed by several stages throughout the attack flow  
  
## IOCs

IOC| SHA-256| Notes  
---|---|---  
InstaIIer.exe| A0319E612DE3B7E6FBB4B71AA7398266791E50DA0AE373C5870C3DCAA51ABCCF| MSI downloader  
ChromeSetup.exe| C9094685AE4851FD5A5B886B73C7B07EFD9B47EA0BDAE3F823D035CF1B3B9E48| MSI downloader  
MlcrоsоftЕdgеSеtuр.exe| 3BF4B365D61C1E9807D20E71375627450B8FEA1635CB6DDB85F2956E8F6B3EC3| MSI downloader  
update.msi| 53C3982F452E570DB6599E004D196A8A3B8399C9D484F78CDB481C2703138D47| MSI dropper, dropped pythonw.exe, python311.dll and pz.log files  
update.msi| D19C166D0846DDAF1A6D5DBD62C93ACB91956627E47E4E3CBD79F3DFB3E0F002| MSI dropper, dropped VMWareHostOpen.exe, vmtools.dll and vmo.log files  
DirectX12AdvancedSupport.msi| B287C0BC239B434B90EEF01BCBD00FF48192B7CBEB540E568B8CDCDC26F90959| MSI dropper, dropped MpCopyAccelerator.exe, MpClient.dll, and virginium.flac file  
python311.dll| BE8EB5359185BAA8E456A554A091EC54C8828BB2499FE332E9ECD65639C9A75B| Malicious dll loaded by pythonw.exe  
vmtools.dll| 931D78C733C6287CEC991659ED16513862BFC6F5E42B74A8A82E4FA6C8A3FE06| Malicious dll loaded by VMWareHostOpen.exe  
MpClient.dll| 5F57537D18ADCC1142294D7C469F565F359D5FF148E93A15CCBCEB5CA3390DBD| Malicious dll loaded by MpCopyAccelerator.exe  
vmo.log| 51CEE2DE0EBE01E75AFDEFFE29D48CB4D413D471766420C8B8F9AB08C59977D7| Encrypted payload decrypted by vmtools.dll  
pz.log| 8CE0901A5CF2D3014AAA89D5B5B68666DA0D42D2294A2F2B7E3A275025B35B79| Encrypted payload decrypted by python311.dll  
virginium.flac| B3D8BC93A96C992099D768BEB42202B48A7FE4C9A1E3B391EFBEEB1549EF5039| Encrypted payload decrypted by MpClient.dll  
ocmtancmi2c5t[.]xyz| | Host of the MSI package  
lazagrc3cnk[.]xyz| | Host of the MSI package  
omdowqind[.]site| | Domain that facilitated download of the MSI downloader  
weomfewnfnu[.]site| | Domain that facilitated download of the MSI downloader  
winextrabonus[.]life| | Domain that facilitated download of the MSI downloader  
bgobgogimrihehmxerreg[.]site| | Domain that facilitated download of the MSI downloader  
pshkjg[.]db[.]files[.]1drv[.]com| | Domain that facilitated download of the MSI downloader  
ooinonqnbdqnjdnqwqkdn[.]space| | Domain that facilitated download of the MSI downloader  
hello-world-broken-dust-1f1c[.]brewasigfi1978[.]workers[.]dev| | Domain that facilitated download of the MSI downloader  
doorblu[.]xyz| | C&C server  
costexcise[.]xyz| | C&C server  
buyerbrand[.]xyz| | C&C server  
94.228.169[.]55| | C&C server  
gapi-node[.]io| | C&C server  
gstatic-node[.]io| | C&C server  
  
**References:**  
  
<https://zeltser.com/media/docs/malware-analysis-lab.pdf>

## Article tags

  * [Detection and Response](/blog/tag/detection-and-response/)
  * [Research](/blog/tag/research/)