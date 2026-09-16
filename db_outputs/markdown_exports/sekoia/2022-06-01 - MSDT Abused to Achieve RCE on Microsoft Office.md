# MSDT Abused to Achieve RCE on Microsoft Office

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/msdt-abused-to-achieve-rce-on-microsoft-office
- **Date :** 2022-06-01

---

_This blog post on this Microsoft zero-day vulnerability was originally published as a FLINT report (_[_Sekoia_](/platform/intelligence) _Flash Intelligence) sent to our clients on May 31, 2022._

On May 27th a malicious Microsoft Office document was discovered by the NAO SEC security team and other threat hunters as MalwareByte researchers on VirusTotal. This DOCX document (MD5:_52945af1def85b171870b31fa4782e52_) has been crafted to load a specific remote HTML file by using the MSHTML engine. 

Once opened, the HTML file is using Javascript to replace its own URL by an URL containing the  _ms-msdt_ Protocol Scheme, pushing Microsoft Office to launch the Microsoft Support Diagnostic Tool utility (_msdt.exe_) with specific arguments, leading to the Remote Code Execution of an arbitrary Powershell payload. MSDT is a tool used to troubleshoot and collect diagnostic data for analysis by support professionals to resolve a problem.

It's not the first time that the Microsoft Support Diagnostic Tool is abused in order to obtain arbitrary code execution on Windows. In the past, it has been abused to execute specific remote executables via XSS [vulnerabilities on Electron apps](/blog/luckymouse-uses-a-backdoored-electron-app-to-target-macos) or as a Living of the Land (LOL) Windows binary.

However, the past exploitation required at least a "one-click" user interaction or a second XML file present on the computer to be achieved. In that specific case, no interaction is required by the user and MSDT directly executes the Powershell Script embedded in the  _IT_BrowseForFile_ parameter. As identified by John Hammond from the [cybersecurity](/blog/cybersecurity-skills-shortage-4-advices-to-better-deal-with-it) firm Huntress, the content of the _IT_BrowseForFile_ parameter needs to fill these conditions to be executed: 

  * At a minimum, two directory traversals (../) are required in the  _IT_BrowseForFile_ argument
  * Code wrapped within  _$()_ is executed via PowerShell, but spaces would break it
  * “” must be the last trailing string present at the end of the  _IT_BrowseForFile_ argument



At this time, we don’t know why Microsoft Support Diagnostic Tool allows arbitrary PowerShell execution inside the  _IT_BrowseForFile_ parameter. However, it is likely that researchers will find other "vulnerable" Microsoft utilities allowing such PowerShell execution in their parameters arguments in the coming weeks.

It is important to note that this vulnerability (CVE-2022-30190, also dubbed Follina by some security researchers) can be exploited even without opening the file by crafting a specific Rich Text Format (RTF) document and making the user preview it in the Windows Explorer Preview Pane. **Several researchers pointed out that even if the docx exploitation chain seems to not work anymore, the RTF one is still vulnerable.**

## A vulnerability with Chinese roots

The discovered document is not the first DOCX seen ITW exploiting this vulnerability. **Sekoia found that several intrusion sets were aware of it prior to its discovery by NAO SEC and the first wave of exploitation seems to have been done by Chinese**[**APT intrusion sets**](/blog/nobeliums-envyscout-infection-chain-goes-in-the-registry-targeting-embassies)**.** In the documents, the inclusion of the External resource in the initial exploit is finished by an exclamation mark likely to force the execution by the MSHTML engine without warning.

![Malicious reference to an external HTML file](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a669e9a71d42284114e8_6a92a47e3e6167cebbf703a0_6a2a7953e16dd066f4290363.webp)

Malicious reference to an external HTML file

By looking at the files containing this specific string on VirusTotal at the end of the Target Attribute URL, we have been able to find five other documents, exploiting this vulnerability since the beginning of March 2022. Here is the list of the documents, their description and the URL where the malicious HTML payload was hosted: 

  *  _05-2022-0438.doc_ (MD5:_52945af1def85b171870b31fa4782e52_), created on the 2022-05-25, is a blank document, possibly a repuposing of the intitial exploit. This document loads an HTML file hosted on the attackers-owned domain  _www.xmlformats[.]com_. It is worth to note that, Sekoia have been able to retreive another domain used by the same attacker and dubbed  _miniformats[.]com_.


  * _Exposing_Nitesh_Pariyar_Liar!!!.doc_ (MD5:_d313002804198b5af1e0b537799be348_), created on the 2022-03-25, is a document which seems to target an individual working for the Nepalese NCELL company which is the first private mobile service provider operating in Nepal and the second largest telecommunications company, after Nepal Telecom. This document loads a an HTML file hosted on the likely compromised Exchange server at the following URL:  _hxxps://exchange.oufca[.]com.au/aspnet_client/poc.html_


  *  _Exposing_Sonish_Liar!!!.doc_(MD5:_529c8f3d6d02ba996357aba535f688fc_), created on the 2022-04-06 - is a similar document but exposing another nepalese individual. This document request another HTML file hosted on the same server:  _hxxps://exchange.oufca[.]com.au/owa/auth/15.1.2375/themes/p3azx.html_


  *  _приглашение на интервью.doc_ (MD5:_f531a7c270d43656e34d578c8e71bc39_), created on the 2022-04-12 - is a document which seems to target specific individuals by asking for of an Interview on the Sputnik Russian radio broadcast related to Ukraine. This document loads an HTML file hosted on an VPS server at the following URL:  _hxxps://www.sputnikradio[.]net/radio/news/3134.html_


  *  _РЭТ-ЮМ-3044 от 12.04.2022.doc_ (MD5:_6bcee92ab337c9130f27143cc7be5a55_), created on the 2022-04-07, seems to target the CEO of the Concern Radio-Electronic Technologies. According to wikipedia CRET is producing fifth-generation Rostec R-168-5UN-2 encrypted Military-Transceiver which is used by the Russian forces in Ukraine. The document loads another HTML file hosted on _thesputnikradio[.]net_ server at the following URL:  
_hxxps://www.sputnikradio[.]net/radio/news/1134.html_


  *  _CSAFP'S_GUIDANCE_RE_NATIONAL_AND_LOCAL_ELECTION_2022_NLE.docx_ (MD5:  _8ee8fe6f0226e346e224cd72c728157c_), created on the 2022-03-09, is the first document seen ITW which exploits the [vulnerability](/blog/log4shell-the-defenders-worst-nightmare). This document impersonates the Philippines armed forces in a letter destined to several armed forces divisions. It loads the HTML file hosted on a VPS at the following URL:  _http://141.98.215[.]99/color.html_



It is interesting to note that there is no infrastructure connection between these documents. **Therefore, it seems that the same exploit has been used or repurposed by different threat actors before its discovery by the security researchers.**

Unfortunately for us, only one URL was active at the time of this writing. This small opportunity allowed us to grab a cabinet file executed on the victim’s workstation after the exploitation. This cabinet file (_test.cab_ \- MD5:_75b614b50ff24d567d1b136340507b82_) contains a binary is a compiled PyInstaller which contains a file named “ _loader.py_ ”. 

This loader - which seems to have Chinese origins according to the comments left by the developer - downloads an encoded shellcode from the server  _160.20.145[.]111_. Then, it performs useless RSA encryption and decryption operations on it and executes it in a new thread. The retrieved shellcode is a Cobalt Strike beacon which communicates with  _103.51.140[.]188_ by using jQuery malleable profile.

Both of the retrieved IP addresses are already known as malicious in Sekoia Intelligence Center.  _160.20.145[.]111_ to be a **PlugX C2** and  _103.51.140[.]188_ to be a [**CobaltStrike**](/blog/hunting-and-detecting-cobalt-strike)**C2**. As of today, no attribution to a specific Chinese intrusion set or activity cluster can be done with these technical indicators. 

## Vulnerability detection

The detection of the CVE-2022-30190 exploitation can be done through analysis of process execution. msdt.exe executed with the  _IT_BrowseForFile_ argument containing $( is a sign of the [vulnerability](/blog/ongoing-roaming-mantis-smishing-campaign-targeting-france) exploitation attempt.

## Workarounds

As the current version of Office is still vulnerable with RTF documents, and Microsoft did not publish any patch yet, we advise to apply remediations. Different remediations, deployable by GPO, seems to be possible in the wait of the Official patch from Microsoft:

  * Remove the  _ms-msdt_ URI schema registry key in registry  _HKEY_CLASSES_ROOT_
  * Disable "_Troubleshooting wizards_ " in registry  _HKEY_LOCAL_MACHINE: SOFTWARE\Policies\Microsoft\Windows\ScriptedDiagnostics_



## IoCs

**Malicious documents hashs  
** _8ee8fe6f0226e346e224cd72c728157c  
6bcee92ab337c9130f27143cc7be5a55  
f531a7c270d43656e34d578c8e71bc39  
529c8f3d6d02ba996357aba535f688fc  
d313002804198b5af1e0b537799be348  
52945af1def85b171870b31fa4782e52_

**Loaders hashs  
** _414ac723fe6fdbd5cb1e703b0c225b50  
8e4d8cbbc7374574f40c31f02f225053  
75b614b50ff24d567d1b136340507b82_

**VPS servers  
** _103.51.140[.]188  
160.20.145[.]111  
141.98.215[.]99  
sputnikradio[.]net  
xmlformats[.]com  
miniformats[.]com  
onedrivo[.]com_

### **YARA rules  
**

`rule exploit_CVE202230190_html_file_hunting {  
meta:  
id ="70b5ddc4-443d-4bc7-b047-29ed2247f364"  
version = "1.0"  
description = "Detects the HTML file used for to exploit"  
cve = "CVE-2022-30190"  
source = "SEKOIA"  
ceation_date = "2022-05-30"  
modification_date = "2022-05-30"  
classification = "TLP:WHITE"  
strings:  
$script = "<script" ascii nocase  
$href = "location.href" ascii nocase  
$ms_msdt = "ms-msdt:" ascii nocase  
condition:  
filesize >= 4000 and $script and  
$ms_msdt in (@href..@href+20)  
}rule exploit_CVE202230190_Documentxmlrels_hunting {  
meta:  
id = "b3d06d37-fa80-4515-9aaf-1168c515bd8f"  
version = "1.0"  
description = "Detects document.xml.rels used by the DOCXs"  
warning = "Hunting rule, can produce FPs"  
cve = "CVE-2022-30190"  
source = "SEKOIA"  
creation_date = "2022-05-31"  
modification_date = "2022-05-31"  
classification = "TLP:WHITE"  
strings:  
$s = { 21 22 20 54 61 72 67 65  
74 4D 6F 64 65 3D 22 45  
78 74 65 72 6E 61 6C 22  
2F 3E }  
condition:  
uint32be(0) == 0x3C3F786D and #s == 1  
}rule exploit_CVE202230190_MalRTF_hunting {  
meta:  
id = "2302a0c8-4762-4751-8928-61e26c42ad0a"  
version = "1.0"  
description = "Detects potential RTFs exploiting CVE-2022-30190"  
warning = "Hunting rule, can produce FPs"  
source = "SEKOIA"  
creation_date = "2022-06-02"  
modification_date = "2022-06-02"  
classification = "TLP:WHITE"  
strings:  
$s = { 7B 5C 2A 5C 6F 62 6A 63 6C 61 73 73 20 68 74 74 70 }  
condition:  
uint32be(0) == 0x7B5C7274 and #s == 1  
}  
`

## **SIGMA rules**

### TTPs (ATT&CK)

  * Exploitation for Client Execution (T1203)
  * Command and Scripting Interpreter: PowerShell (T1059.001)
  * Phishing (T1566)



## References

  * [[Twitter] NaoSec Tweet related to the malicious document](https://twitter.com/nao_sec/status/1530196847679401984?s=20&t=AmJicjJLyI4l5RrHpnyZ9g)
  * [[Microsoft] Microsoft advisory](https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/)
  * [[Benjamin-altpeter] MSDT abuse via XSS on Electron Apps](https://benjamin-altpeter.de/shell-openexternal-dangers/)
  * [[LOLBAS] MSDT abuse to execute arbitrary code](https://lolbas-project.github.io/lolbas/Binaries/Msdt/)
  * [[Twitter] RTF execution chain still vulnerable](https://twitter.com/HaifeiLi/status/1531329940980805633)