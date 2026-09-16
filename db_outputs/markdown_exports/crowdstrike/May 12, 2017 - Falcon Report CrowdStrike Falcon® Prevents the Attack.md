# Falcon Report: CrowdStrike Falcon® Prevents the Attack

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/falcon-intelligence-report-wanna-ransomware-spreads-rapidly-continually-encrypts-victim-files/
- **Date :** May 12, 2017

---

# Falcon Intelligence Report: Wanna Ransomware Spreads Rapidly; CrowdStrike Falcon® Prevents the Attack

May 12, 2017

• [ Falcon Intelligence Team](/en-us/blog/author.falcon-intelligence-team/ "Posts by Falcon Intelligence Team") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


_Wanna Decryption Ransom Screen_

Wanna (also known as WannaCry, WCry, WanaCrypt and WanaCrypt0r) ransomware exploded onto the ransomware scene on May 12, 2017, with a mass campaign impacting organizations in many countries. This second variant of the ransomware has been leveraging the EternalBlue (MS-17010) vulnerability, released by the Shadow Brokers actors, in order to spread over victim networks via the Windows file sharing protocol, Server Message Block (SMB), following an initial infection. CrowdStrike Falcon® Prevent offers protection for this variant through two types of coverage. Falcon Prevent has a Machine Learning layer (at the “Moderate Level”) and a Behavioral IOA layer (“Suspicious Process”). To ensure this ransomware is prevented, the Prevention Policies must be enabled.

For additional details on how to configure CrowdStrike Falcon® Prevent to stop Wanna ransomware and its variants, please visit the blog, ["CrowdStrike Falcon® Prevents WannaCry Ransomware."](/en-us/blog/falcon-endpoint-protection-blocks-the-ransomware-that-attacked-the-nhs/) Wanna ransomware targets 177 file types for encryption. Victim files are appended with .wncry.  Unlike other ransomware families, Wanna continues to encrypt victim files following any name changes, and any new files created following infection. A ransom note is displayed on the victim machine, which is completed using text from a library of Rich Text Format (RTF) files, in multiple languages and chosen based on machine location. A similar text based ransom note named @Please_Read_Me@.txt is added to each folder containing encrypted victim files. Observed ransom demands have been either $300 or $600 USD worth of Bitcoin (BTC) and the decryption software shows one of the following three possible Bitcoin wallet addresses:

  * 115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn
  * 12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw
  * 13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94

Wanna contains a resource name XIA, which is a password-protected ZIP archive file using the password WNcry@2ol7. This contains the following additional resource files: 

  * b.wnry
  * c.wnry
  * r.wnry
  * s.wnry
  * t.wnry
  * taskdl.exe
  * taskse.exe
  * u.wnry

Executing the main module directly drops files and folders into the directory in which it was run and causes further processes to be launched from those folders. However, executing the main module with the command line argument /i installs the malware as a service named uebdpwbdm529. When installed as a service, files and folders are installed to C:\ProgramData\uebdpwbdm529\. The service is started when the user logs on and executes the file C:\ProgramData\uebdpwbdm529\tasksche.exe. In order to utilize the SMB shadow broker exploitation capability, a process named winsecsvc.exe is installed in the Wanna directory. From current samples of Wanna, the file winsecsv.exe performs a check to the domain www.iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea<.>com, which has now been sinkholed by an unknown entity. Should the victim machine make a successful connection to this domain, the process will not perform SMB exploitation. However, if the domain is not reachable, the process tasksche.exe will be launched with the /i parameter to initialize the service installation. If the service is created successfully, Wanna will perform its usual file encryption operations as well as seek to exploit vulnerable SMB shares. The registration of the domain has disabled the SMB exploitation capability. The resource file named s.wnry is another ZIP file that contains a folder called TaskData. This contains a TOR bundle to communicate with the command-and-control (C2) servers, which is required for the victim to make the ransom payment. At present, observed C2s are:

  * gx7ekbenv2riucmf<.>onion 
  * 57g7spgrzlojinas<.>onion 
  * xxlvbrloxvriy2c5<.>onion 
  * 76jdd2ir2embyv47<.>onion 
  * cwwnhwhlz52maqm7<.>onion 

A file named 00000000.pky contains an RSA 2048-bit key, and file encryption is performed using the Microsoft Cryptographic Service Provider with a mix of AES with randomly generated 128-bit key and RSA, which occurs regardless of the network’s connectivity status. RSA Modulus:

0x3daf5cc1317b0ef2a9859f054b11e8deb3b9a3911c31a72022ced1d82139ac0177eda0c3f7e5c2d29abc0cbe899fba5e2a66d7871e401e7e998d88f9c5ae1403e65aa461f5e7dd90349f628de02ea60a02bed4128afab5420b7060d20196bf2b76c34d661a75860c29bb87891315ae333b5ca5b3b4bf2dc15d96c7da3c5ad966fd74dc68ccc271b5edbd4b1219b9d9427fdf16f86748eea78f4fa8ae39db7b71399fb03abce42d915666b5674d3d5a03e8fe37635e39158fc2cd05dd4a718964f66c6c06a15eaa74f03b17b19fd1eec920b1585098b6e4ed59ce629b65a6c1244f82a0c53c26020461ca4a6aa3a395a8f834575a2de9d8e7fc313c76c84a03b3

Exponent: 0x10001 CrowdStrike Intelligence will continue to monitor the development of this ransomware and continue to provide more in-depth technical analysis. Watch a video to

learn more: [How To Stop WannaCry Ransomware with CrowdStrike Falcon® Endpoint Protection](/en-us/resources/videos/stop-wannacry-ransomware-crowdstrike-falcon-endpoint-protection/) Click for more information on [subscribing to Falcon Intelligence](/en-us/products/falcon-intelligence/intelligence-subscriptions-offerings/)

& to learn more about [how Falcon prevents ransomware attacks](/products/ransomware.html). 

#### Learn how to protect your organization from ransomware

[DOWNLOAD WHITEPAPER](/resources/white-papers/ransomware-white-paper.html)

JTNDc2NyaXB0JTIwdHlwZSUzRCUyMnRleHQlMkZqYXZhc2NyaXB0JTIyJTNFJTBBJTBBJTI0JTI4ZG9jdW1lbnQlMjkucmVhZHklMjhmdW5jdGlvbiUyMCUyOCUyOSUyMCU3QiUwQSUwQSUyMCUyMCUyMCUyMCUyNCUyOCUyMiUyM2Nvcm5lci1zbGlkZXIlMjIlMjkuY29ybmVyU2xpZGVyJTI4JTdCJTBBJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwZWxlbVRvUHJlc2VudCUwOSUwOSUyMCUzQSUyMCUyMiUyM3Nob3ctY3RhJTIyJTJDJTBBJTA5ZGlyZWN0aW9uRWZmZWN0JTIwJTIwJTIwJTIwJTIwJTIwJTIwJTNBJTIwJTIycmlnaHQlMjIlMkMlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBzcGVlZEVmZmVjdCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUzQSUyMDMwMCUyQyUwQSUwOXJpZ2h0JTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTIwJTNBJTIwMjAlMkMlMEElMDlib3R0b20lMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlM0ElMjA4MCUyQyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGNvb2tpZU1pbnV0ZXNUb0V4cGlyeSUyMCUzQSUyMDE1JTJDJTBBJTBBJTIwJTIwJTIwJTIwJTdEJTI5JTNCJTBBJTdEJTI5JTNCJTBBJTBBJTIwJTIwJTIwJTIwJTI0JTI4JTI3JTIzd2FubmEtcmVwb3J0JTI3JTI5LmNsaWNrJTI4ZnVuY3Rpb24lMjglMjklMjAlN0IlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBnYSUyOCUyN3NlbmQlMjclMkMlMjAlN0IlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBoaXRUeXBlJTNBJTIwJTI3ZXZlbnQlMjclMkMlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBldmVudENhdGVnb3J5JTNBJTIwJTI3QmxvZyUyNyUyQyUwQSUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMCUyMGV2ZW50QWN0aW9uJTNBJTIwJTI3Rm9sbG93ZWQlMjBDb3JuZXIlMjBQb3B1cCUyMExpbmslMjclMkMlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBldmVudExhYmVsJTNBJTIwJTI3V2FubmElMjBSZXBvcnQlMjclMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjAlN0QlMjklM0IlMjAlMEElMjAlMjAlMjAlMjAlMjAlMjAlMjAlMjBjb25zb2xlLmxvZyUyOCUyMnNlbnQtY2xpY2stdHJhY2slMjIlMjklM0IlMEElMjAlMjAlMjAlMjAlN0QlMjklM0IlMEElMEElM0MlMkZzY3JpcHQlM0U=

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)