# MuddyWater replaces Atera by custom MuddyRot implant

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/muddywater-replaces-atera-by-custom-muddyrot-implant-in-a-recent-campaign
- **Date :** 2024-07-15

---

_This report was originally published for our customers on 20 June 2024._

_Today, the Check Point Research (CPR) team_[ _published_](https://research.checkpoint.com/2024/new-bugsleep-backdoor-deployed-in-recent-muddywater-campaigns/) _a report on the same implant, providing details of recent MuddyWater campaigns._

## Introduction

On June 9 2024, ClearSky [tweeted](https://x.com/ClearskySec/status/1799829814011994120) about a new campaign associated with the MuddyWater intrusion set, employed by the Iranian intelligence service MOIS (Ministry of Intelligence) against Western and Middle Eastern entities. According to the source, MuddyWater is suspected of targeting Turkey, Azerbaijan, Jordan, Saudi Arabia, and Israel, although the full list of targeted countries has not been confirmed during our investigation.

By examining the posted hashes and relevant infrastructure, we found that compared to previous campaigns, this time MuddyWater changed their infection chain and did not rely on the legitimate Atera remote monitoring and management tool (RMM) as a validator. Instead, we observed that they used a new and undocumented implant. Sekoia TDR analysts dubbed this tool ”MuddyRot”.

This report aims to compare past and current infection chains associated with MuddyWater and present a technical analysis of the “MuddyRot” malware, a new validator in the intrusion set’s arsenal.

## Technical analysis

### Recent infection chain

The MuddyWater intrusion set is known to rely primarily on two intrusion vectors when targeting Windows environments. They use public exploits to compromise internet-exposed servers, such as Exchange or SharePoint servers, and then move laterally within the network. Additionally, they send spear phishing emails from previously compromised email accounts to bypass security measures and increase the emails’ legitimacy in the recipient’s eyes.

On April 22 2024, our fellows at HarfangLab [published](https://harfanglab.io/en/insidethelab/muddywater-rmm-campaign/) a blogpost on recent MuddyWater infection chains leading to the installation of [SimpleHelp](https://simple-help.com/) (2023) and [Atera](https://www.atera.com/) (2023-2024). These infection chains involved an email (or possibly an instant messaging message) sent from a compromised account. The email included a link to an online storage service hosting a malicious ZIP archive, which contained the remote monitoring and management software.

In the recently observed campaigns, MuddyWater seems to have changed this infection chain by embedding the links in PDF files instead of emails. The one-page PDF used resembles MuddyWater’s recent emails—straightforward, without any images, and with decoys related to online courses or webinars to face cyber threats, as shown below. By clicking the embedded links, the user is redirected to a webpage hosted on the [Egnyte](https://www.egnyte.com/) service to download a ZIP archive containing the MuddyRot validator.

![Malicious PDF used by MuddyWater](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b09f9b7f8b2cd15e17_6a92a295a2f46752fd01283a_6a2a7dc80e66fd3d5e0a8756.webp)

Malicious PDF used by MuddyWater

**Figure 1. Malicious PDF used by MuddyWater**

### **MuddyRot analysis**

The MuddyRot malware is a x64 implant developed in C with several capabilities such as reverse shell, persistence and the possibility for the operators to download and upload files from/to the compromised workstation. Upon execution, the malware carries out a series of standard tasks, such as deobfuscating strings, dynamic API loading necessary functions, and creating a mutex.

All relevant strings, such as the malware configuration, file paths, and imported methods, are obfuscated through a simple method: each character of any relevant string has its decimal value subtracted by an integer. Several integers, such as 3, 4, 5, or 6, are used for obfuscation.

![Obfuscation used by Muddywater’s rotrot implant. Source: Sekoia Threat Detection & Research Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b09f9b7f8b2cd15e11_6a92a293e17eff730b654288_6a2a7dc80e66fd3d5e0a8750.webp)

Obfuscation used by Muddywater’s rotrot implant. Source: Sekoia Threat Detection & Research Team

**Figure 2. Obfuscation used by Muddywater’s MuddyRot implant**

The created mutex is named _DocumentUpdater,_ which is checked upon execution. If it already exists, the malware stops its execution.

Moreover, to reduce its detection, the malware uses the popular and well-spread technique of dynamic import loading using the pair LoadLibrary / GetProcAddress to load methods from various DLLs. To do so, the malware uses the PE header structures to access the InMemoryOrderModuleList, a doubly linked list containing loaded modules with the structure _LDR_DATA_TABLE_ENTRY. This structure provides information about the DLLs, including their names and address, that the malware uses to determine which DLLs to load afterwards. The malware then employs GetProcAddress to retrieve addresses of functions from Kernel32.dll, Advapi32.dll, Ole32.dll, and Ws2_32.dll.

### **Persistence**

At the very beginning of the malware execution, MuddyRot copies itself in the c:\programdata\softwarememory directory with the name documentsmanagerreporter.exe. The malware establishes persistence on the infected host by creating a scheduled task named DocumentsManagerReporter.

To avoid detection by security solutions that monitor the at command and the schtask.exe service, the malware uses the CoCreateInstance method with the object identifier (CLSID) 0F87369F-A4E5-4CFC-BD3E-73E6154572DDBD3E73E6154572DD, which corresponds to the Scheduled Task class object. The task is set to run daily at the time of the initial infection plus 1 minute.

![RotRot decompiled function in charge of coping itself. Source: Sekoia Threat Detection & Research Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b09f9b7f8b2cd15e1a_6a92a296dc30711238322d23_6a2a7dc80e66fd3d5e0a875a.webp)

RotRot decompiled function in charge of coping itself. Source: Sekoia Threat Detection & Research Team

**Figure 3. MuddyRot decompiled function in charge of coping itself**

### **C2 communication** of the "MuddyRot" malware

The malware communicates over a raw TCP socket on port 443, and the data are obfuscated using the same obfuscation as the one used for the strings where the subtraction value is fixed to... “3”.

![Method used for configuration desobfucation.Source: Sekoia TDR blogpost on MuddyWater C2 communication](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b09f9b7f8b2cd15e14_6a92a292dc30711238322a8b_6a2a7dc80e66fd3d5e0a874d.webp)

Method used for configuration desobfucation.Source: Sekoia TDR blogpost on MuddyWater C2 communication

**Figure 4. Method used for configuration desobfucation**

The first message to be sent to the C2 is the victim host fingerprint, which is the combination of the hostname and the username joined by a slash. The data is obfuscated using the same technique as the one leveraged for the string. Finally, the packet is structured as follows:

  * The first 4 bytes are the size of the fingerprint;
  * The next bytes are the fingerprint obfuscated.



If the victim received “-1”, the program stops, otherwise the malware enters in an infinite loop to await new order from the C2. Here are the commands supported by the implant:

**Command ID**| **Description**  
---|---  
0×1| Upload file (filename: exit)   
0×2| Download file (filename: exit)   
0×3| Reverse shell  
0×4| Update socket optval  
0×5| Kill process  
0×8| Delete Task  
0×9| Check if task exists  
0xA| Create scheduled task  
0×60| Update sleep interval  
0×61| Change socket optval  
0×62| PingBack C2 with the same message  
  
There is a file in the working directory named “exit” that is used as a buffer to upload to the C2 or download files from the C2. However, this file does not seem to be used elsewhere in the code. Therefore, it is likely that the operators handle this file through their reverse shell by renaming its content and copying push data in it for exfiltration, which is not very handy.

### **Reverse Shell**

The MuddyRot operator can connect to the victim host using the malware’s reverse shell capability. To trigger the functionality, the bot must receive the order ID “2”.

This technique involves creating anonymous pipes to handle the standard input, output, and/or error streams. These pipes are specified in the STARTUPINFO structure, ensuring that the input and output of the spawned command shell (cmd) are redirected through the pipes. By configuring the hStdInput, hStdOutput, and hStdError members of the STARTUPINFO structure to use the pipe handles, the reverse shell can seamlessly transmit commands to and receive outputs from the remote shell. This method enhances the stealth and functionality of the reverse shell, allowing an attacker to execute commands remotely while capturing the results in real-time.

![Decompiled method that configures the reverse shell on the infected host](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b09f9b7f8b2cd15e0e_6a92a294a2f46752fd0127e6_6a2a7dc80e66fd3d5e0a8753.webp)

Decompiled method that configures the reverse shell on the infected host

**Figure 5. Decompiled method that configures the reverse shell on the infected host**

The content of the reverse shell communication (received input: command to execute, and shell output) is obfuscated. To decode the incoming inputs the malware used the same deobfuscation as the rest of the C2 communication (n.b: subtract by 3 each byte) and for the output it added three bytes. The developer of this backdoor added the “terminate” command to stop the reverse shell.

## **Conclusion**

This is not the first time that we have seen MuddyWater using its own implant as victim validators. While previously these first-stage backdoors, such as Powerstats, were mostly written in PowerShell, in recent years MuddyWater has shifted to using Remote Monitoring and Management (RMM) tools such as Atera, Tactical RMM or SimpleHelp. This is possibly due to the extended functionalities these off-the-shelf tools offer compared to simple PowerShell-based reverse shells.

We don’t yet know why MuddyWater operators have reverted to using a homemade implant for their first infection stage in a least one campaign. It is likely that the increased monitoring of RMM tools by security vendors, following their rise in abuse by malicious threat actors, has influenced this change. Maybe one of its targets prevent Atera execution on its own network so Muddy operators had to change for something more custom.

The use of specific and homemade implants allows defenders to track MuddyWater activities more effectively. Consequently, we are providing Indicators of Compromise (IOCs) and Yara rules for MuddyRot.

## MuddyWater IOCs

**MuddyRot related codes**

`94278fa01900fdbfb58d2e373895c045c69c01915edc5349cd6f3e5b7130c472  
b8703744744555ad841f922995cef5dbca11da22565195d05529f5f9095fbfca  
73c677dd3b264e7eb80e26e78ac9df1dba30915b5ce3b1bc1c83db52b9c6b30e  
960d4c9e79e751be6cad470e4f8e1d3a2b11f76f47597df8619ae41c96ba5809  
`

**Infrastructure**

`91.235.234[.]202   
146.19.143[.]14 (down)  
`

**YARA rules**

The YARA rules are available on [Sekoia.io GitHub repository](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/MuddyWater/yara/).

Thank you for reading this blogpost. **We welcome any reaction, feedback or critics about this analysis. Please contact us on tdr[at]sekoia.io.**