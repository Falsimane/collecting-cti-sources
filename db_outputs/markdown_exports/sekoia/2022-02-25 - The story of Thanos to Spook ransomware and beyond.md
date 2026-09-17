# The story of Thanos to Spook ransomware and beyond

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/the-story-of-a-ransomware-builder-from-thanos-to-spook-and-beyond-part-2
- **Date :** 2022-02-25

---

In a blog post entitled [“The story of a ransomware builder: from Thanos to Spook and beyond (Part 1)”](/blog/the-story-of-a-ransomware-builder-from-thanos-to-spook-and-beyond-part-1), our colleagues from [CERT](/glossary/cert)-Sekoia described the results of incident response on a Spook ransomware attack. We took over and then investigated the Thanos builder used by the ephemeral group Spook and many other groups.

## 1.1 From Thanos to Spook

Online documentation shared by the cybersecurity community quickly stressed a link between the Spook ransomware and the Thanos ransomware. The Spook [ransomware group](/blog/an-insider-insights-into-conti-operations-part-one), like many other cybercriminal groups, uses auto-generated ransomware to impact its targets. The usage of malware builder is quite common in the cybercriminal ecosystem. It has two main benefits: it allows delegating the complexity to a more qualified developer and gains a lot of time during the weaponization step of an attack.

The Spook ransomware samples appear to be created by the Thanos builder. This builder has been sold on [underground forums](/blog/eternityteam-a-new-prominent-threat-group-on-underground-forums) since late 2019 according to the information we could find on these forums.

![Thanos selling post \(Source Sekoia\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc40261188e_6a92a50a4b4041c693433ef6_6a2a6fa562f00361bfd8ff7a.webp)

Thanos selling post (Source Sekoia)

![Thanos selling post \(Source Sekoia\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc4026118a3_6a92a50e9f9b7f8b2cd0fd5b_6a2a6fa562f00361bfd8ff9a.webp)

Thanos selling post (Source Sekoia)

![Thanos selling post \(Source Sekoia\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc402611894_6a92a50b32517fc40260b507_6a2a6fa562f00361bfd8ff7d.webp)

Thanos selling post (Source Sekoia)

![Thanos selling post \(Source Sekoia\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc40261188b_6a92a508c5553634ac94cbfb_6a2a6fa462f00361bfd8ff72.webp)

Thanos selling post (Source Sekoia)

The builder offers the [ransomware group](/blog/an-insider-insights-into-conti-operations-part-two) a simple GUI where it can customize its ransomware.

![Thanos ransomware builder options, 2020. \(Source : Recorded Future\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc402611891_6a92a507a2f46752fd02b4f8_6a2a6fa462f00361bfd8ff6f.webp)

_Thanos ransomware builder options, 2020. (Source : Recorded Future)_

The builder allows threat actors to build a custom ransomware sample with multiple options (found in the resource once decrypted):

  * Custom ransom notes content and filename
  * Extensions of files to encrypt
  * Extension to add to encrypted files
  * Bitcoin address
  * Change wallpaper
  * Multiple OPSEC features (obfuscation, kill defenders, anti-VM,  _etc_)



This report focuses on the version used by the Spook ransomware group. Still, variants of other groups will have similar functionality.

### Spook ransomware execution

To achieve its goals, Spook samples (and by extension, other ransomware created using the Thanos builder), perform several actions:

  * Disable the Raccine anti-ransomware tool
  * Change configuration of multiple services
  * Set persistence
  * Kill the processes designated in the config file
  * Delete Shadow Copies
  * Encrypt files
  * Print the ransomware note
  * Delete artefacts



Those actions are performed using simple commands that can be found in the configuration file using the tool created by our colleagues [during the incident response step](/blog/the-story-of-a-ransomware-builder-from-thanos-to-spook-and-beyond-part-1).

### Disabling the Raccine anti-ransomware tool

Raccine (<https://github.com/Neo23x0/Raccine>) is a simple and open-source anti-ransomware tool. It kills the process that tries to delete the Shadow Copies. This is why it must be disabled before continuing. It is an opensource project which must be used with caution in production.

Here are some simple commands used by Thanos samples to perform Raccine deactivation:

`"taskkill" /F /IM RaccineSettings.exe   
"reg" delete  
"HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V   
"Raccine Tray" /F   
"reg" delete HKCU\Software\Raccine /F   
"schtasks" /DELETE /TN "Raccine Rules Updater" /F  
`

### Kill tasks and stop services

The ransomware stops multiple services using three tools: “sc.exe”, “net.exe”, and taskill.exe”. All these processes and services are stopped to ensure the encryption of files that might otherwise be write-locked. 

`"sc.exe" config FDResPub start= auto  
"sc.exe" config Dnscache start= auto  
"sc.exe" config SQLTELEMETRY start= disabled  
"sc.exe" config SstpSvc start= disabled  
"sc.exe" config SQLTELEMETRY$ECWDB2 start= disabled  
"sc.exe" config SSDPSRV start= auto  
"sc.exe" config upnphost start= auto  
"sc.exe" config SQLWriter start= disabled  
  
"net.exe" start Dnscache /y  
"net.exe" stop bedbg /y  
"net.exe" start FDResPub /y  
"net.exe" stop MSSQL$SQL_2008 /y  
"net.exe" start SSDPSRV /y  
"net.exe" stop avpsus /y  
"net.exe" stop NetBackup BMR MTFTP Service /y  
"net.exe" stop BMR Boot Service /y  
"net.exe" stop McAfeeDLPAgentService /y  
"net.exe" stop MSSQL$SQLEXPRESS /y  
…  
  
"taskkill.exe" /IM mspub.exe /F  
"taskkill.exe" /IM mspub.exe /F  
"taskkill.exe" /IM synctime.exe /F  
"taskkill.exe" /IM mydesktopqos.exe /F  
"taskkill.exe" /IM Ntrtscan.exe /F  
"taskkill.exe" /IM mysqld.exe /F  
…  
`

### Set persistence

The Spook samples simply create a .lnk file in a Startup folder to gain persistence on infected systems.

`C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\reload1.lnk`

### Delete shadow copies

To ensure that the target will not be able to restore its files, the ransomware will try to delete the Shadow Copy by running this PowerShell command:

`"powershell.exe" & Get-WmiObject Win32_Shadowcopy | ForEach-Object { $_Delete(); }`

However, the Spook sample that was found by our colleagues failed to delete the Shadow Copy.

### Encrypt files

The ransomware goes through the drives and encrypts all files containing one of the extensions that were specified by the user in the builder. The file encryption is done using [AES-256 algorithm](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in CBC mode, and the AES key is protected using a 2048 RSA public key. An interesting fact is that the AES key can be specified to the builder or automatically generated during the execution. If the key is specified, it can be retrieved in the sample and used to decrypt the files.

We saw a Spook sample opening a fake console window to ask the user to wait patiently during its computer encryption. This fake window is often used by samples created by the recent RobinHood group.

![“Please wait” console opened by Spook. Source : Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc40261189a_6a92a50fc9e0b85494c055bf_6a2a6fa562f00361bfd8ff9d.webp)

_“Please wait” console opened by Spook. Source : Sekoia_

### Print the ransom file to the user

At the end of its execution, the ransomware will warn the user that files on its computer have been encrypted via multiple ways. The ransomware drops multiple .txt and .hta ransom files. It will try to open the .hta file using “mshta.exe” or the .txt file using “notepad.exe”. It will also set a notification in the notification bar. Some samples also try to print the ransom note if a connected printer is detected.

`"C:\Windows\System32\mshta.exe"   
C:\Users\Admin\Desktop\RESTORE_FILES_INFO.hta  
`

![Spook ransom note \(Source Sekoia\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc402611897_6a92a50ec5553634ac94ce71_6a2a6fa562f00361bfd8ff85.webp)

 _Spook ransom note (Source Sekoia)_

### Delete the executable file

At the end, the ransomware will delete itself using the following cmd command.

`"cmd.exe" /C ping 127.0.0.7 -n 3 > Nul & fsutil file setZeroData offset=0  
length=524288 “%s” & Del /f /q “%s”  
`

This command is used to fill the file with zeros to make sure it is unrecoverable. The same command is used by the LockBit ransomware according to this [Fortinet article](https://community.fortinet.com/t5/FortiEDR/Technical-Tip-How-FortiEDR-protects-against-LockBit-Ransomware/ta-p/195776).

`"C:\Windows\System32\cmd.exe" "/C choice /C Y /N /D Y /T 3 & Del   
"C:\Users\Admin\AppData\Local\Temp\b256d10ea8b49cb596fa1dd7b9007b7d03debb3ad05b79c0de45401a82910e7e.exe  
`

Note that the “cmd.exe” commands used by the sample will have disguised 3-second sleep:

  * choice /C Y /N /D Y /T 3:Set a choice between one option “Y”, the choice is not printed to the user, the default response is “Y” and it waits 3 seconds before validating the default choice.
  * ping 127.0.0.7 -n 3 > Nul:A ping with 3 packets whose result is ignored.



Unlike other variants, the Spook samples do not seem to have the capability to exfiltrate files by themselves (the builder allows adding an exfiltration functionality through FTP). The data exfiltration must be done using another tool such as RClone. But half of the known Spook samples try to download PSexec during their execution like the incident response attests in blog part 1. The Spook ransomware seems to be simpler than other variants, exfiltration and lateral movement capabilities are delegated to other tools.

Another difference between Spook and older variants (such as the Prometheus’ ones) is that we did not see the Spook ransomware stopping services using “net.exe stop”. Most Spook samples do not have the capacity to spread themselves across the network, changing [firewall](/glossary/firewall) rules, enabling SMB and copying itself using “net use” as Prometheus could.

Prometheus is a ransomware group that was active in early 2021. For more details, you can read the [Cybereason report](https://www.cybereason.com/blog/research/cybereason-vs.-prometheus-ransomware) about Prometheus. What is described there about the Thanos builder corresponds to what we could observe.

## 1.2 Samples from different threat actors

From the Spook samples that were given to us, we started looking for similar files using YARA rules and other pivots on malware databases. This watch allowed us to find many Thanos samples from multiple groups.

`rule ransomware_win_thanos {  
meta:  
version = "2"  
malware = "Thanos"  
description = "Detect the ransomware from the Thanos builder"  
source = "SEKOIA.IO"  
creation_date = "2021-06-07"  
  
strings:  
$s1 = "$F935DC23-1CF0-11D0-ADB9-00C04FD58A0B" ascii  
$s2 = "b__" ascii  
  
condition:  
uint16(0)==0x5A4D and filesize < 600KB and $s1 and #s2 == 3  
}  
`

As Thanos is an off the shelf ransomware, it is not surprising that it is used by many groups. Here is a list of group that use Thanos builder:

**Name**| **Note file name**| **Encrypted file’s extension**| **Estimated period of activity**| **Double extorsion**  
---|---|---|---|---  
Thanos| RESTORE_FILES_INFO.txt| .cryptedrandom string|  | Yes  
Hakbit| HOW_TO_RECOVER_YOUR_FILES.txtHELP_ME_RECOVER_MY_FILES.txtHELP_ME_MY_FILES_NOT_MAKE_PUBLIC.txt| .[<victim_id>].[<email_addr>].CRYSTAL.VIPxxx| 04/2020 - 05/2020|   
Abarcy| Abarcy#2996.txt|  | |   
Hard| RESTORE_FILES_INFO.txt|  | |   
Milleni5000| RESTORE_FILES_INFO.txt|  | |   
Ravack| HELP_ME_RECOVER_MY_FILES.txt|  | |   
Energy| HOW_TO_DECYPHER_FILES.txt| .energy[potentialenergy@mail.ru]|  |   
josephnull| HOW_TO_DECYPHER_FILES.hta|  | 07/2020 |   
Alumni| HOW_TO_RECOVER_YOUR_FILES.txt|  | |   
Prometheus| RESTORE_FILES_INFO.txt| .[<victim_id>].PROM[<email_addr>].<victim_id>[<email_addr>]| 01/2021 - 05/2021| Yes  
RecoveryGroup| RESTORE_FILES_INFO.txt| .<victim_name>| 03/2021 - 08/2021|   
Haron| RESTORE_FILES_INFO.txt| .<victim_name>| 07/2021| Yes  
Undetermined russian speaking group| Инструкция.txt| none| |   
pingp0ng| decrypt_info.txt| .[<victim_id>].<email_addr>].noname|  |   
@Online7_365| decrypt_info.txt| .[<victim_id>].[<email_addr>].boooom.[<victim_id>].[<email_addr>].helpme| 08/2021 - 12/2021 |   
SpookRESTORE_FILES_INFO.txt.<victim_id>09/2021 - 10/2021YesRobinHoodRESTORE_FILES_INFO.txt.<victim_id>10/2021 - currentYesSteroikRESTORE_FILES_INFO.txt.<victim_id>10/2021|  MidasRESTORE_FILES_INFO.txt|  | |   
| | | |   
| | | |   
| | | 12/2021| Yes  
  
This list is the continuation of Cybereason’s work by Sekoia’s point of view on the usage of the Thanos builder. It is not exhaustive, and we found many Thanos samples that we were not able to attribute to a known ransomware group. As we can see, the Thanos builder is used by dangerous double extortion groups as well as script kiddies. Most of them seem to use the default configurations or common ones on ransom note name and encrypted file extension, which made them not very usable for attribution. However, the ransom note content usually leads us to the ransomware group.

## 2\. Ransomware current context

### 2.1 Who was the Spook ransomware group?

The Spook ransomware group had been operating between September 2021 and October 2021. It uses the previously described Thanos builder to generate Spook sample with the following ransom message:

`YOUR COMPANY WAS HACKED AND COMPROMISED!!!   
  
All your important files have been encrypted! Our encryption algorithms are very strong and your files are very well protected, the only way to get your files back is to cooperate with us and get the decrypter program.   
  
Do not try to recover your files without a decrypter program, you may damage them and then they will be impossible to recover.   
________________________________________________________________________________  
  
For us this is just business and to prove to you our seriousness, we will decrypt you three files for free. Just open our website, upload the encrypted files and get the decrypted files for free. _______________________________________________________________________________  
  
! WARNING !   
  
Whole your network was fully COMPROMISED!   
  
We has DOWNLOADED of your PRIVATE SENSITIVE Data, including your Billing info, Insuranse cases, Financial reports, Business audit, Banking Accounts! Also we have corporate correspondence, information about your clients. We got even more info about your partners and even about your staff.   
  
Additionally, you must know that your sensitive data has been stolen by our analyst experts and if you choose to no cooperate with us, you are exposing yourself to huge penalties with lawsuits and government if we both don't find an agreement. We have seen it before cases with multi million costs in fines and lawsuits, not to mention the company reputation and losing clients trust and the medias calling non-stop for answers. Come chat with us and you could be surprised on how fast we both can find an agreement without getting this incident public.   
________________________________________________________________________________  
  
IF YOU ARE AN EMPLOYER OF A COMPANY THEN YOU SHOULD KNOW THAT SPREADING SENSITIVE INFORMATION ABOUT YOUR COMPANY BEING COMPROMISED IS A VIOLATION OF CONFIDENTIALITY. YOUR COMPANY'S REPUTATION WILL SUFFER AND SANCTIONS WILL BE TAKEN AGAINST YOU.   
________________________________________________________________________________  
  
WE HIGHLY SUGGEST THAT YOU DON'T CONTACT THE AUTHORITIES REGARDING THIS INCIDENT BECAUSE IF YOU DO, THEN AUTHORITIES WILL MAKE THIS PUBLIC WHICH COMES WITH A COST FOR YOUR ENTERPRISE. THE RECOVERY PROCESS OF YOUR FILES WILL BE FASTER IF YOU COME AND CHAT WITH US EARLY. IF YOU CHOOSE TO COOPERATE, YOU WILL SEE THAT WE ARE PROFESSIONALS WHO GIVES GOOD SUPPORT.   
  
Instructions for contacting us:   
________________________________________________________________________________  
  
You have way:   
1) Using a TOR browser!   
a. Download and install TOR browser from this site: https://torproject.org/   
b. Open the Tor browser. Copy the link: http://spookuhvfyxzph54ikjfwf2mwmxt572krpom7reyayrmxbkizbvkpaid.onion/chat.php?track=754WRBXZ24 and paste it in the Tor browser.   
c. Start a chat and follow the further instructions.   
  
Key Identifier:   
…  
`

This message has multiple English errors, which can be explained since the builder is sold on Russian-speaking forums.

As you can see, the group practised double extortion. The data from targeted organizations were published on an onion leak website. It is interesting to note that the Spook’s website and the one of the former ransomware group Prometheus are very similar:

![Prometheus website screenshot. Source: Cyble](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc40261189d_6a92a50963e0c17b5dadf0df_6a2a6fa462f00361bfd8ff76.webp)

_Prometheus website screenshot. Source: Cyble_

Moreover, according to the [S2W’s blog](https://medium.com/s2wblog/prometheus-x-spook-prometheus-ransomware-rebranded-spook-ransomware-6f93bd8ab5dd), an old file tied to a Prometheus victim was found in the exact same location in the Spook WordPress server.

During its short period of activity, the Spook ransomware group announced it had hit 38 organizations, all published on its website between September 26, 2021, and October 19, 2021.

**During this time and according to the statements of the group, France was the most affected country, with 9 companies being targeted (which represents 23.7% of all known attacks).**

![Countries most impacted by the Spook ransomware known campaigns](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc4026118a0_6a92a5068d1115926b20ee87_6a2a6fa462f00361bfd8ff6c.webp)

_Countries most impacted by the Spook ransomware known campaigns_

The industries that were impacted the most included the financial, the manufacturing and the retail ones.

### 2.2 Multiplication of ransomware groups - where do the borders stand between them?

As per our observations, ransomware builders are regularly shared on many hacking forums. Very often, it is the developer himself who shares or sells a builder, or else the source code of ransomware is leaked from third parties.

![Example of a ransomware builder released on a hacking forum](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6a132517fc4026118a6_6a92a50ce9a71d422840bbaf_6a2a6fa562f00361bfd8ff82.webp)

Example of a ransomware builder released on a hacking forum

 _Example of a ransomware builder released on a hacking forum_

In any case, building kits allows threat actors to create customized [ransomware](https://www.sekoia.com/blog/xdr-vs-ransomware-en), with the possibility to create numerous variants with different configurations for each campaign.

The generated ransomware are thus more likely to escape detection, and the attribution is getting much more challenging.

It is not uncommon to see threat actors within the ransomware industry to be involved in several [ransomware groups](https://www.sekoia.com/blog/vice-society-a-discreet-but-steady-double-extortion-ransomware-group) or projects. For this reason, there is an increasing focus on ransomware affiliates or ransomware operators, instead of clearly separated groups.

## 3\. Conclusion

Posted on hacking forums in February 2020, the Thanos builder is still being used by many ransomware actors, with varying degrees of experience, to develop [new malware](https://www.sekoia.com/blog/raccoon-stealer-v2-part-2-in-depth-analysis) variants and conduct malicious campaigns.

In this blog post, we analyzed one of the latest ransomware developed with the Thanos builder.

Given Spook’s short period of activity, a large number of victims, and what has been observed by our colleagues during the incident response, we think that the former Prometheus group acquired multiple accesses by using the services of an access broker and recreated a quick arsenal using the Thanos builder to monetize these accesses.

## 4\. Annexes

### 4.1 Mapping MITRE ATT&CK

**Technique ID**| **Technique Name**  
---|---  
T1583.003| Acquire Infrastructure: Virtual Private Server  
T1588.001| Obtain Capabilities: Malware  
T1078| Valid Accounts  
T1027| Obfuscated Files or Information  
T1140| Deobfuscate/Decode Files or Information  
T1059.001| Command and Scripting Interpreter: PowerShell  
T1059.003| Command and Scripting Interpreter: Windows Command Shell  
T1112| Modify Registry  
T1547.001| Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder  
T1562.001| Impair Defenses: Disable or Modify Tools  
T1562.004| Impair Defenses: Disable or Modify System Firewall  
T1570| Lateral Tool Transfer  
T1071| Application Layer Protocol  
T1489| Service Stop  
T1490| Inhibit System Recovery  
T1016| System Network Configuration Discovery  
T1083| File and Directory Discovery  
T1486| Data Encrypted for Impact  
T1070.003| Indicator Removal on Host: Clear Command History  
T1070.004| Indicator Removal on Host: File Deletion  
  
### 4.2 YARA rules

`rule ransomware_win_thanos {  
meta:  
version = "2"  
malware = "Thanos"  
description = "Detect the ransomware from the Thanos builder"  
source = "SEKOIA"  
creation_date = "2021-06-07"  
  
strings:  
$s1 = "$F935DC23-1CF0-11D0-ADB9-00C04FD58A0B" ascii  
$s2 = "b__" ascii  
  
condition:  
uint16(0)==0x5A4D and filesize < 600KB and $s1 and #s2 == 3  
}  
`

### 4.3 Indicators

**SHA256**| **Attribution**  
---|---  
ce686daaf9d97fb2c42d9789d19f1dbdb81d1b45851cf3d9e67f46b578365764|   
d11fca3f8e2be9c5926e5e87f06dca48a19156c3296a589131d86f9a5d6fbc8f|   
4984825fb21206a2f2df5d2c84794f0ac4edea3c48d32e9284338d7082d55024| Hakbit  
edcac243808957cc898d4a08a8b0d5eaf875f5f439a3ca0acfaf84522d140e7e|   
34b93f1989b272866f023c34a2243978565fcfd23869cacc58ce592c1c545d8e| Hakbit  
6a5090762c6058bc223e37e89f53832faad80995e3c5ed7e59ed9f5a5e604e47|   
28a0fd7612bea3f286e5ff4e7b109dcaf46f9defed663af50d20a0b2086e13ac|   
5d40615701c48a122e44f831e7c8643d07765629a83b15d090587f469c77693d|   
1d4db8733c5f11ee8fca530aeb4a91069de04b1af64cbe1fa3ae2d3572a6e554| Prometheus  
1c3ecb9ea4d4690c7a96581aa25d26f02392fe6a104b61c2fcd0a68bde11f8d2|   
936a35ca214e9be1438c67a1153c854c28054994ce43f1eed39bb9dc52cb54dd|   
9bf0633f41d2962ba5e2895ece2ef9fa7b546ada311ca30f330f0d261a7fb184| Prometheus  
8d268be58a27d2c980b807ffe703ea28b0fd0cd1ba2e455902faebe9ec17c52e| RecoveryGroup  
899f48bad035165acf8869af63922619f8a901bbeb8a7fc13919ba90dd9e7768|   
8a4a038a965ba42a0442d44abf25e4d21f5049d4a4a8aa9cb6691ec4282814a1|   
52f7f9e8369a3e89899d40e89766c9642b137b25bfd58a2b564dac67a40445f3| Prometheus  
11aebdff8c064c160c2b21f3a844bacaecd581d9dc2e4224d31903d2a56e2dd3| Prometheus  
8c723af5c826adea162ef3f2e37a1cca7b43d549c9a5fab7c9ff17f65eb5d8e7| Prometheus  
ef97bf49a9bd00a994143852590cc3a2d20227e510dc2b5968704d8f100b4d3c| RecoveryGroup  
3605b9af44b153ef39a5bbe6d98ab8e6ef58b1f0f1c76eca4a3fb9b9a4042605|   
7891062da6c81bf31c740f9c33aac10224104bf2f6ab6bdf9c1e3895d07011ed|   
3c3a8067481153f82f3fb4d967c44cd735e635f75bb417e1f94492ee02df145a| filerestore000  
8dab7d5add0f7ca61c5f3bc6aae6dea30086ea3e0719d302748234b3ac4e31f8| Prometheus  
4852f22df095db43f2a92e99384ff7667020413e74f67fcbd42fca16f8f96f4c| RecoveryGroup  
caf815381680cfa6afedcd7c7af5a5c838788b1c7ec593ce817114a25ab63441| RecoveryGroup  
81411c9010f2adcb4758bac5ed6128d5a76b24689d477f6ed2c3003fd57e4f3b| RecoveryGroup  
81411c9010f2adcb4758bac5ed6128d5a76b24689d477f6ed2c3003fd57e4f3b| RecoveryGroup  
66ed5384220ff3091903e14a54849f824fdd13ac70dc4e0127eb59c1de801fc2| Haron  
6e6b78a1df17d6718daa857827a2a364b7627d9bfd6672406ad72b276014209c| Haron  
cbdb04d23e395b270e16d7ca81cc6b734039fa069932989d4e4f4d4d266df28b| Haron  
f261d0283d9f1e346a648537b859570741c52be11b95e527a108037d71363327|   
c6d7c39e83f12684cc9341305044fb03a61d23876d37746d96d31a9191bacb8f|   
34de4b269fe0721f4323dc549545fa5575a1bd5178174d382d0cee730eac5d89|   
fb17fb6e1e71c92d2ae5a06363886ea71d614e2603706d38ca8ebbc56d3dc120| RecoveryGroup  
eb2ed1680e9b2350d78f431849a9e8c5c1d91d97ae72767d228b2208e6f72f46| Streriok  
7f56c9ac52ad69fc02e73b653384a07397571ed12673c6eacd9ed574d371975f|   
bb744238e99e7654395a3c19fb4d491fffcdcd7a96c914f898a649ca39f11a33| @Online7_365  
e5d4335e72a6d1cad51de1f30dbb29c4942fa5574891cd0b0ed35a252b088028| Skull  
2c6802679ce8ac5ed90bd25d25805e284c7dd5269f7805c68cc5fd965a0adc21|   
84a47f4362ecaa832b466a392a827f77471fa4056e9e538c727aff4a6a6b48b4| Spook  
e347fd231a543a5dfd53b01ff0bc67b2bf37593e7ddc036f15bac8ad92f0d707| Spook  
8dad29bd09870ab9cacfdea9e7ab100d217ff128aea64fa4cac752362459991c| Spook  
d991aa2b1fad608b567be28e2d13d3d4f48eea3dea8f5d51a8e42aa9a2637426|   
32ec78179b1516765fd2ec4da82404352cb6837a906c7493283ef578930273e6| Spook  
869d05fe732ff419731def3140634df40e887d821430e46d17b1e3703c63b6cf| Spook  
b9018a268cf70981051bfdfa58cfa98c9dd222c17d9188b811b5660a3c2c59de| Spook  
44edca2989cfa4ba819191b70323fe5f83e300dd0c2e66abb42f1f9ca831f29b| Spook  
0ed55db21a1a5eeca96605f870cb6d4ddf1277e1e257371e75d6ee9e1507b216| Spook  
b256d10ea8b49cb596fa1dd7b9007b7d03debb3ad05b79c0de45401a82910e7e| Spook  
5ee42cc91ee256752213dbd7525816273a29257df0c52984865b7c34c51df1a2| MedusaLocker  
720f92a0233c07cfdafca70dc95b841682fdefd434835eca106c308f1dc8dc50| KukaJamba  
d4820f3c561fd274c69d01c9446951fca10291f728ab0ead0537a4eabd0f4b1d| RobinHood  
80379b9640f070381ef346cc2998a127abf3e75de6339801e415734140186fa0|   
c841ca56516b51ffa4b808209cad755960dd07ae0ce13c73a85cf635d076a7f5| @Online7_365  
20fa2538c879182151b86f35518d90952e24acd7078f84a4a01850e780574201| @Online7_365  
e64edc53f3457a0608354c18f398787fc2d281a9f4246724d2d73d9ddc34a861|   
74a717027b6212236662bf641c473b8f8cd65486898b02940357bb9b3035f38a|   
ca729ac6a7a2dbf47191c1a30d6aea9f3d8580c1e146a7a2b70858e7c61ea686|   
d6a68bf279f5e39d52b518a4b925361325376b276052379c7ac700fd7c8dae5b|   
21bcf864de80dc43669a1e6ad68ab5959f9e4c258b9ea2043a229cdb7343d095|   
6f08e40dd82613ecc87195778aaced37960609935b47cc45cc499f10cf57f685| RobinHood  
7b6a67b6de160992ade99643e4f82fbe55c9122bd3db3e586ecd215033d3c838| @Online7_365  
0a66157cca6b9aa3c3de9c76d55638f438c63b9d7189d41a8eb8da02ce1371b5| RobinHood  
43f627c288a92f89d6c089480faf9a5d2b935c5c1796e5776a01ed18cf4aa857| RobinHood  
c76c9ad75741a9d0f9fe66ba41f6fdfd67ad0ebe6cf354e75c420648ddb6ca9f|   
575d1ef0e51fbe96e7454b8f06b60118faf3e4ed7ef0f98908d0fcca6c0a9b82| Midas  
e9d0ee963a1463694686ea347989ef9c80cb06f91602ccbcde178e04a6062509|   
40eafc1053e4b93ac0767032e3df1d65bd839f4bf6d7f239c72e1bab862e6d48| KukaJamba  
aa207e58d8f8c2e48b10bd86b0cc1e6fc9edba51b57ab29fde7052840ac2b8b8| RobinHood  
fc0341bde264eead7433140738cc1088a9b02e6d6bfc6a51a80af9602e7ab3e7| RobinHood  
7eba89ee9f4ce6fad19f7e86cdf076456beb89f9f5a731380f352b54e120952b| RobinHood  
08d6b4739df157c6cf8a767267b86c77de44db881500ffdc4e709dd0de1c3d9a| RobinHood  
  
## 5\. Sources

  * [Medium - Decoding SmartAssembly strings, a Haron ransomware case study](https://medium.com/walmartglobaltech/decoding-smartassembly-strings-a-haron-ransomware-case-study-9d0c5af7080b)
  * [IBM - From thanos to prometheus: when ransomware encryption goes wrong](https://securityintelligence.com/posts/ransomware-encryption-goes-wrong/)
  * [CyberReason - Cybereason vs. Prometheus ransomware](https://www.cybereason.com/blog/research/cybereason-vs.-prometheus-ransomware)
  * [Medium - Prometheus x Spook: Prometheus ransomware rebranded Spook ransomware](https://medium.com/s2wblog/prometheus-x-spook-prometheus-ransomware-rebranded-spook-ransomware-6f93bd8ab5dd)