# Helldown Ransomware: An Overview of this Emerging Threat

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/helldown-ransomware-an-overview-of-this-emerging-threat
- **Date :** 2024-11-19

---

_This report on Helldown was originally published for our customers on 14 November 2024._

## Context

Through our social media monitoring, Sekoia’s Threat Detection & Research (TDR) team identified a [tweet](https://x.com/TuringAlex/status/1851969443426914503) posted on 31 October 2024 mentioning a Linux variant of the **Helldown** ransomware targeting **Linux** systems.

The Helldown ransomware group is a relatively new and still largely undocumented Intrusion Set (IS), previously known to deploy ransomware exclusively on Windows systems. He employs its own custom ransomware and engages in double extortion tactics. He is particularly active, claiming **31 victims** within **three months** , including Zyxel's European subsidiary.

This blog post provides a detailed examination of this emerging threat. Based on its pattern of targeting, we offer insights into its methods of operation. A technical analysis of both the Windows and Linux variants of this ransomware is also included.

## Helldown Intrusion Set

### Overview

Helldown is a relatively new Intrusion Set in the ransomware landscape, first documented by [Cyfirma](https://www.cyfirma.com/research/tracking-ransomware-august-2024/) in their August ransomware tracking report. Although still largely undocumented, the group is highly active, having listed 28 victims on its Data Leak Site (DLS) since 5 August 2024.

While the group’s exact methods remain unclear, both Cyfirma and [Cyberint](https://cyberint.com/blog/research/ransomware-trends-2024-report/) reports that it exploits vulnerabilities to infiltrate victims' networks and deploy its ransomware. The IS employs a double extortion strategy, exfiltrating large volumes of data and threatening to publish it on its .onion site if the ransom is not paid.

The group’s DLS underwent changes toward the end of August. Notably, while the victims listed on the original DLS were transferred to the new one, three victims were removed. The reason for this removal is unclear, but it may indicate that a ransom was paid.

### Victimology

As of 7 November 2024, the group has allegedly compromised 31 victims, primarily small and medium-sized businesses. However, some larger companies have also been affected, including **Zyxel Europe** which provides network and cybersecurity solutions, including firewalls, routers, and access points across Europe. Most of the victims are located in the United States, with others primarily in Europe, including 3 in France.

The timeline below illustrates that the group was highly active in August and October, with a quieter period in September. This period aligns with the switch to a new DLS, suggesting that the group may have prioritised developing its tools over active ransomware operations during this time.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58aa49553afbaf43f0c_6a92a2332e47a1e9fe0d63a0_6a2a7e82c1e5dce602a836e1.webp)

_Figure 1. Helldown victims over time as published on their DLS, as of 7 November 2024_

### Modus operandi

Like many ransomware groups, Helldown engages in double extortion. However, details about its Techniques, Tactics and Procedures remain undocumented. By analysing the profile of its victim, we can gain a clearer understanding of its intrusion and data theft techniques.

#### Initial access - the Zyxel lead

  * **TDR analysis hypothesis**



On 4 November 2024, through an analysis of the attack surfaces of various victims, TDR identified that at least eight victims, including one compromised in early August, were using Zyxel firewalls as IPSec VPN access points during the time of their breach. Historical searches on the Censys engine also revealed that two of these victims replaced their Zyxel firewalls with other brands shortly after being compromised. 

In an [advisory bulletin](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-multiple-vulnerabilities-in-firewalls-09-03-2024) issued on 3 September 2024, Zyxel announced security patches to address vulnerabilities in its firewalls. One of these, CVE-2024-42057, is especially critical as it allow an attacker to execute malicious code without authentication, although specific prerequisites must be met. This vulnerability was identified by nella17 (@nella17tw) of the Devcore research team. As of early/mid - November 2024, no public exploit code is available for this vulnerability or other recent vulnerabilities affecting Zyxel products.

In late September 2024, multiple users on the Zyxel forum reported instances of Zyxel firewalls with v5.38 firmware being compromised. Specifically, a file named zzz1.conf was uploaded, and a user account called OKSDW82A was created. This file was uploaded to VirusTotal twice from Russia, on 17 and 22 October. It contains a base64-encoded string which, when decoded, reveals an ELF binary for the MIPS architecture. The payload, however, appears to be incomplete. Sekoia assess with medium confidence this file is likely connected to the previously mentioned Zyxel compromise.

`We have observed similar exploitation patterns through our honeypots and reported these findings to the Zyxel Product Security Incident Response Team. If you are part of a SOC or CERT, we are available to share additional details under TLP:AMBER. Please reach out to us at tdr [ at ] sekoia [ dot ] io.  
  
09/27/2024 Update: Following our report, Zyxel published a security advisories officially referencing the vulnerability we identified on our honeypots and exploited by Helldown. This vulnerability has now been assigned the identifier CVE-2024-11667.  
`

On 9 October 2024, Zyxel EMEA published an article detailing the tracking of threat actors targeting Zyxel firewalls. Their investigation found that attackers exploited vulnerabilities to create access accounts (such as “SUPPOR87,” “SUPPOR817,” or “VPN”) through SSL VPN.

Based on this information, TDR assesses with high confidence that the attacker is exploiting a vulnerability in Zyxel firewalls as an entry point into victims' information systems.

  * **Truesec CSIRT confirmation**



On 7 November, [Truesec published](https://www.truesec.com/hub/blog/helldown-ransomware-group) a blog post indicating that its CSIRT had responded to incidents linked to Helldown, where a Zyxel vulnerability was exploited as an entry point. Truesec also described some of the group’s TTPs, which align with those observed by a Zyxel forum user who had privately communicated with TDR. It was shared that after compromising the Zyxel firewall, the attacker used the OKSDW82A account to connect via SSL VPN using an IP from Mullvad VPN. The attacker then leveraged the domain controller’s LDAP synchronisation credentials to pivot further into the network, conducting several actions before being halted by the EDR. Among other actions, the attacker used _certutil_ to download Advanced Port Scanner. They also attempted to execute HRSword, likely to disable the target machine’s defenses. Additionally, they used the _findstr_ command, probably to search for files of interest.

All of this evidence strongly suggests that Zyxel firewalls have been targeted by Helldown. Details about post-compromise activities indicate that, in at least one intrusion, the attacker's tactics align with typical ransomware methods. Compromising firewalls or VPN gateways is a common entry technique for ransomware groups, as it provides a foothold to an organisation's systems through equipment that is often poorly-monitored and offers access to critical resources

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58aa49553afbaf43f15_6a92a23432517fc4025f880e_6a2a7e82c1e5dce602a836e5.webp)

 _Figure 2 : Synthesis of TTPs used by Helldown_

#### Data stealing

According to the group’s disclosures on its leak site, it exfiltrates significant amounts of data,averaging 70GB when excluding outliers. The data exfiltration ranges from 22GB to as much as 431GB. This approach differs with the typical strategy of other ransomware operators, who generally prefer more selective and targeted data exfiltration to remain discreet and to maximise the potential damage in the event of a leak. 

According to DLS files overview, the stolen files are varied, with the majority being PDFs or scanned documents. Several victims on the DLS have NAS systems or electronic document management portals, suggesting the attacker likely obtained documents directly from these servers. We partially confirm this hypothesis by reviewing the list of stolen files (when accessible) on the group’s DLS. It appears that files are consistently located on D: or E: drives, with file paths suggesting network file sharing.

The large volume and variety of data suggest that the attacker does not selectively choose which documents to steal. Instead, they appear to target data sources that store administrative files, such as PDFs and document scans, which typically contain sensitive information (personal, financial, etc.), thereby intensifying the pressure on victims. Additionally, since data downloads over TOR are very slow, it is unlikely that a third party would attempt to download huge files this way, which diminishes the blackmail leverage.

## Helldown ransomware - Windows

Using VirusTotal and pivoting on elements within the ransom note, we identified several Windows payloads, all showing strong similarities. A technical analysis is performed on the following payload to understand how it works:

  * SHA256 hash: 0bfe25de8c46834e9a7c216f99057d855e272eafafdfef98a6012cecbbdcfabf
  * Size: 653.50 KB
  * File type: PE32 executable (GUI) Intel 80386, for MS Windows



### Dynamic analysis

The sandbox execution of the ransomware payload reveals the following behaviour:

  * **Shadow Copy Deletion** : The ransomware deletes system shadow copies using the commands wmic shadowcopy delete /nointeractive and vssadmin Delete Shadows /All /Quiet, executed via cmd.exe.
  * **Script Drop and Execution** : The binary creates a script at C:\ProgramData\1.bat and runs it. This script’s purpose is to terminate several processes, including databases and Microsoft Office applications (Word, Excel, _etc._) to properly encrypt these file types.
  * **Machine Encryption** : Files on the machine are encrypted, and their filenames are altered to include a random string of characters. Additionally, the file icon is also changed to a specific image, and a ransom note is generated on the desktop.
  * **Trace Removal** : Lastly, the script and ransomware binary are deleted, and the machine is switched off using shutdown command.



### Static analysis

Static analysis reveals that all ransomware instructions are executed directly from the main function. In addition to encryption, the ransomware performs the following actions:

  * **Configuration Loading** : A function loads the hardcoded configuration from the payload header, which is XOR-encrypted with the key “ _50_ ” . The configuration consists of an XML file with a root section titled _settings_ , containing various tags that specify which files to encrypt and which to ignore. The _settings_ section also includes commands for deleting shadow copies. Additionally, the _icon_encod_ and _content_ tags hold the icon that will be set as the default for encrypted files and the ransom note, respectively.
  * **Privilege Check** : The program checks if the current thread's impersonation token has Administrator privileges by calling the functions AllocateAndInitializeSid and CheckTokenMembership. If Administrator rights are confirmed, it dynamically disables the default redirection to 64-bit function calls on 64-bit operating systems.
  * **Pre-encryption Actions** : In the case studied, the enable_cmds setting in the configuration file is set to True, allowing the execution of commands specified under the cmds tag. These commands include deleting shadow copies using the shadow copy delete and vssadmin commands. Additionally, an icon file named C:\ProgramData\xx.ico is dropped, and a registry entry is created to set this icon as the default for encrypted files.



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58aa49553afbaf43f1b_6a92a22da2f46752fd00e8d8_6a2a7e81c1e5dce602a836d0.webp)

_Figure 3 : Helldown ransomware Icon for encrypted file_

  * **Process Termination** : A batch file named C:\ProgramData\1.bat is generated, containing instructions to terminate a list of processes specified in the configuration file using taskkill. This script is then executed to stop those processes.
  * **Ransom Note** : A ransom note file, named ReadMe.[encrypt_extension].txt, is created on the desktop. The contents of the note are base64-encoded within the content tag in the configuration file.



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58aa49553afbaf43f12_6a92a2316568d7e2b40855a9_6a2a7e81c1e5dce602a836d9.webp)

_Figure 4 : Helldown ransom note from xml configuration_

  * **Post-encryption Actions** : In this case, the configuration file has enable_shutdown_system set to True. In addition to removing itself and the .bat script, the ransomware also shuts down the machine.



### Similarities

A comparison was made between the 4 payloads.

  * The behaviour is consistently the same.


  * The icons C:\ProgramData\xx.ico are all identical and have the hash: b83e8ff6d046dccad0f5a2777f067bdc8eb3b239c030165daf32f9dae902d012.
  * For 3 of the payloads, the C:\ProgramData\1.bat scripts are similar and have the hash 67aea3de7ab23b72e02347cbf6514f28fb726d313e62934b5de6d154215ee733. Only the payload with hash 3e3fad9888856ce195c9c239ad014074f687ba288c78ef26660be93ddd97289e has a different bat script with hash 2b15e09b98bc2835a4430c4560d3f5b25011141c9efa4331f66e9a707e2a23c0. The difference is minimal; in this script, the Chrome process is killed in addition to the others.



This ransomware shares many similarities with the Darkrace ransomware. This point is detailed later in point "Connection with the ransomware ecosystem".

## Helldown ransomware - Linux

On 31 October 2024, the Linux variant of the Helldown ransomware was first discovered by the cybersecurity researcher @TuringAlex. As detailed below, analysis of this code shows that this ransomware targets VMware ESX servers. The analysis focuses on the following sample:

  * SHA256 hash: 6ef9a0b6301d737763f6c59ae6d5b3be4cf38941a69517be0f069d0a35f394dd
  * Size: 237.30 KB
  * Fyle type: ELF Executable and Linkable format (Linux)



### Code overview

The code is straightforward, lacking both obfuscation and anti-debugging mechanisms. The execution workflow of main function is relatively concise, performing the following steps:

  * **Configuration Loading:** It loads a hard-coded XML configuration file containing various tags for specific actions.



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58aa49553afbaf43f18_6a92a230e17eff730b652b49_6a2a7e81c1e5dce602a836d6.webp)

_Figure 5 : Helldown Linux hardcoded configuration_

  * **File Search:** The ransomware iterates over the path provided as an argument to the program, targeting files with extensions specified in the XML file's excluded tags (_e.g._ , .vmdk).
  * **Encryption:** When it finds a file with a specified extension, it encrypts it either fully or partially depending on its size.
  * **Ransom Note Creation:** A ransom note is generated on the infected machine using details from the XML file.



### Encryption

The cry_thread function handles file encryption through the following steps:

  * **File Retrieval:** It pulls a file that was previously identified and placed in a queue.
  * **Open File in Write Mode:** It renames the file before opening it. If write permissions are not available, the operation stops.
  * **File Analysis:** The file size is checked to determine whether to fully or partially encrypt it.
  * **Key Generation:** A random 16-character ASCII encryption key is generated by the b_gen_salsa_key function, which is then RSA-encrypted via the b_rsa_enc function.
  * **Encryption:** A loop through the file with lseek64 is done to, reading data blocks, encrypting each with s20_crypt, and rewriting the data to the file at the same location.
  * **Signature:** The encryption key is encrypted using RSA PKCS1 and appended to the end of the file. The modulus is hardcoded and can be seen in the strings (ADD12705D38F6CB18...), while the exponent is set to 0x010001.
  * **Clear:** Deletes the keys from memory.



Both static and dynamic analysis showed no evidence of network communication. If it is confirmed that the RSA-encrypted key is appended to the end of the file, this could explain why the attacker does not need prior knowledge of the key. With the private key, the attacker can decrypt this data and retrieve the key used to encrypt the file.

## ESX targeted

The code includes a function called kill_vms, which is invoked three times by kill_all_vms with arguments 1, 2, and 3, and performs the following tasks:

  * **List VMs:** The command esxcli vm process list is run to retrieve details of all active VMs, including their World ID, Process ID, VMX Cartel ID, UUID, display name, and the path to the VMX configuration file.
  * **Kill VMs:** A second instruction iterates through each World ID and issues the command esxcli vm process kill -type=x -world-id=worldid, killing each VM sequentially. The -type parameter takes the value passed by kill_all_vms (1 for soft, 2 for hard, and 3 for force shutdown).



Terminating VMs before encryption grants ransomware write access to image files. However, both static and dynamic analysis reveal that, while this functionality exists in the code, it is not actually invoked. 

All these observations suggest that the ransomware is not highly sophisticated and may still be under development.

## Connection with the ransomware ecosystem

### Helldown vs. Hellcat

On 4 November 2024, after the announcement of the Schneider Electric alleged compromise on the Hellcat DLS, a few cyber threat intelligence researchers began assessing a possible link between the Helldown and Hellcat ransomware groups. We believe that this connection remains unverified, as we have not discovered any similarities between the two ransomware groups.

Based on its DLS, Hellcat appears to have been active since early November 2024. Two accounts on the X social media, @grepcn and @ReyBreached, claiming to be Hellcat operators, posted to distinguish themselves from Helldown, each displaying Hellcat's DLS link in their profiles. 

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58aa49553afbaf43f0f_6a92a22f4b4041c693421ab3_6a2a7e81c1e5dce602a836d3.webp)

 _Figure 6 : ReyBreached's tweet denying the link between Hellcat and Helldown_

Additionally, @grepcn had hinted at the Schneider Electric compromise days before its official claim, lending credibility to the connection. Until further analysis of payloads and TTPs, there is no definitive link between Hellcat and Helldown. Currently, Sekoia regards them as two distinct, unrelated groups.

### Helldown vs. Darkrace or Donex

As mentioned during the static analysis, Helldown’s behaviour is very similar to that of Darkrace. Through VirusTotal, pivoting on the hash 2b15e09b98bc2835a4430c4560d3f5b25011141c9efa4331f66e9a707e2a23c0 associated with the bat script seen in one of the 4 Helldown payloads allows the identification of several other ransomware, including Darkrace and Donex. 

Darkrace appeared in May 2023 and was documented by various cyber threat intelligence teams shortly after. According to [Quickheal](https://blogs.quickheal.com/darkrace-ransomware-a-deep-dive-into-its-techniques-and-impact/)'s analysis, it is a variant of LockBit 3 resulting from the leak of its code. [Avast](https://decoded.avast.io/threatresearch/decrypted-donex-ransomware-and-its-predecessors/) suggests that Donex ransomware, which emerged in February 2024, is a rebranded variant of Darkrace, part of a lineage of rebrands tracing back through previous ransomware campaigns. Of note, its DLS can no longer be reached since April 2024, suggesting that this ransomware family is no longer active. A public decryption tool for Darkrace, Donex, and related variants was released in April 2024, likely leading to the end of their operations.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58aa49553afbaf43f1e_6a92a2324b4041c693421b7b_6a2a7e81c1e5dce602a836dd.webp)

_Figure 7 : Comparison of Darkrace and Helldown XML configuration files_

Comparing the configuration files of Helldown, Donex and Darkrace reveals many similarities in content, although the balise names differ. It is noteworthy that Darkrace, Donex, and Helldown consistently use eponymous contact addresses through onionmail.org, along with communication through the TOX messaging platform.

At this point, it is difficult to establish a relationship between Darkrace or Donex and Helldown. Both codes are variants of LockBit 3. Given Darkrace and Donex's history of rebranding and their significant similarities to Helldown, the possibility of Helldown being another rebrand cannot be dismissed. However, this connection cannot be definitively confirmed at this stage.

## Conclusion

Helldown is a notably active new intrusion set, as shown by its large number of victims. Available data indicates that the group mainly targets Zyxel firewalls by exploiting an undocumented vulnerabilities. However, analysis suggests the ransomware they deploy is relatively basic. The group's success appears to rely more on its access to undocumented vulnerability code and its effective use of it, making it easier to gain access for its attacks.

Although there are operational similarities between Helldown ransomware and others like Darkrace and Donex, a formal relationship between them could not be established at this time.

The Zyxel vulnerability exploited by Helldown, as documented by Truesec, appears to match the one reported by a user on the Zyxel forum. It does not seem to align with any CVE currently listed by Zyxel, but Zyxel has stated that this issue is resolved in the latest firmware update. It would be beneficial for Zyxel to provide more information on this vulnerability to facilitate proper referencing.

Helldown deploys Windows ransomware derived from the LockBit 3 code. Given the recent development of ransomware targeting ESX, it appears that the group could be evolving its current operations to target virtualized infrastructures via VMware. Sekoia will continue to closely monitor this emerging threat.

## IoCs

  * **Helldown Windows payload - sha256**



 _0bfe25de8c46834e9a7c216f99057d855e272eafafdfef98a6012cecbbdcfab_  
 _7cd7c04c62d2a8b4697ceebbe7dd95c910d687e4a6989c1d839117e55c1cafd7_  
 _7731d73e048a351205615821b90ed4f2507abc65acf4d6fe30ecdb211f0b0872_  
 _3e3fad9888856ce195c9c239ad014074f687ba288c78ef26660be93ddd97289e_

  * **Helldown Windows - icon, ransom note and scripts - sha256**



 _2621c5c7e1c12560c6062fdf2eeeb815de4ce3856376022a1a9f8421b4bae8e1_  
 _47635e2cf9d41cab4b73f2a37e6a59a7de29428b75a7b4481205aee4330d4d19_  
 _cb48e4298b216ae532cfd3c89c8f2cbd1e32bb402866d2c81682c6671aa4f8ea_  
 _67aea3de7ab23b72e02347cbf6514f28fb726d313e62934b5de6d154215ee733_  
 _2b15e09b98bc2835a4430c4560d3f5b25011141c9efa4331f66e9a707e2a23c0_ (overlap with Darkrace and Donex)

  * **Helldown Linux payload - sha256**



 _6ef9a0b6301d737763f6c59ae6d5b3be4cf38941a69517be0f069d0a35f394dd_

  * **Helldown Linux - ransom note - sha256**



 _9ab19741ac36e198fb2fd912620bf320aa7fdeeeb8d4a9e956f3eb3d2092c92c_

  * **Zyxel compromission artefact (zzz1.conf) - sha256**



 _ccd78d3eba6c53959835c6407d81262d3094e8d06bf2712fefa4b04baadd4bfe_