# Detecting Multi-Stage Infection Chains Madness

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/detecting-multi-stage-infection-chains-madness
- **Date :** 2025-04-22

---

During our daily tracking and analysis routine at **SekoiaTDR** team (Threat Detection & Research), we have been monitoring an attacker infrastructure internally called **“Cloudflare tunnel infrastructure to deliver multiple RATs”**. This infrastructure is used by several actors to host malicious files and deliver remote access trojans (RAT). Several security vendors ([Forcepoint](https://www.forcepoint.com/es/blog/x-labs/asyncrat-python-trycloudflare-malware), [Fortinet](https://www.fortinet.com/blog/threat-research/purehvnc-deployed-via-python-multi-stage-loader), [Orange](https://x.com/CERTCyberdef/status/1894733146114904465), [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/threat-actor-abuses-cloudflare-tunnels-deliver-rats)) have reported that the mentioned infrastructure has been operational since at least February 2024, illustrating its resilience. The related infection chains relying upon that infrastructure is particularly complex, with multiple steps involved (as explained in the schema below) and some variations observed from one campaign to another.

The objectives of these campaigns require analysis by examining the entire malware chain. This analysis will not be detailed here, but the data theft objective remains probable, and consistent with most active cybercriminals intrusion sets.

This report describes one of the latest observed infection chains (delivering AsyncRAT) relying on the Cloudflare tunnel infrastructure and the attacker’s tactics, techniques and procedures (TTPs), with a principal **focus on detection opportunities**. We will illustrate how the **SekoiaDefend** platform detects the different steps with several detection rules that will be shared in the technical details part.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6a12c7d7f8cbcb6977a4c8_blog-detecting-multi-stage-infection-chains-madness-infection-chains-distributing-RAT.webp)

_Figure 1. Infection chains distributing AsyncRAT_

## Initial Access (email -> windows-library)

The usual initial access vector used in that campaign (and still the most prevalent when targeting employees) is a **phishing email** , often disguised as an invoice or order, attempting to deceive the recipient into opening a malicious attachment under a false sense of urgency. Some of these emails may employ a deceptive tactic by including a fabricated conversation thread with a forged reply.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12635_6a92a1d66568d7e2b408160a_6a2a7f3d777d393c5381440c.webp)

_Figure 2. Phishing email sample_

The attachment contained in the phishing email is an old “**application/windows-library+xml** ” file type. and in the year 2025, it is not the primary method to access files over the network (we will explain why below). While this type of file is sometimes blocked at an email gateway, it is not always the case as it may be considered as a safe file format compared to binary ones.

It is possible to block this kind of malicious email using a simple Sigma rule “[Suspicious Email Attachment Received](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/network/email_suspicious_attachment_received.yml)”. It allows us to detect this suspicious attachment. This kind of rule is trivial as we only want to detect a list of given suspicious extensions in any events related to an email and a file. Most of our telemetry hits are either true positives or false positives easy to filter out in a given customer context (mostly IT actions). As we did not initially have the “.ms-library” extension, the rule was updated following that investigation.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12629_6a92a1e1a2f46752fd00b485_6a2a7f3d777d393c53814430.webp)

_Figure 3. Suspicious ms-library file sample_

If we look into that file content, the remote **WebDav** resource is clearly displayed and the file format is easy to detect and block eventually.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1262c_6a92a1dcdc3071123831e196_6a2a7f3d777d393c53814421.webp)

_Figure 4. Suspicious ms-library file sample_

Opening that file will open a warning pop-up for the user, and upon validation, it will create a network connection to the WebDav remote resource mentioned in the “url” entry, displaying the remote file.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1264d_6a92a1e0e17eff730b6501b0_6a2a7f3d777d393c5381442d.webp)

_Figure 5. Explorer Window displaying the malicious remote file_

## Execution (LNK -> HTA -> BAT -> Python)

In the first step of the execution, the deceptive tactic employed involves a**LNK file disguised as a shortcut to a PDF file** , which makes it relevant to the phishing email's theme. LNK files are commonly used in Windows systems to create shortcuts to other files or directories. The direct download of a LNK file from a browser triggers the mechanism where modern web browsers append a ".download" extension to such files to prevent automatic execution.

Therefore, the attacker's use of LNK access over the network likely aimed to bypass detection. Moreover, attempting to open the LNK file triggers a pop-up warning from Windows Security features, further hindering the attack.

![Pop-up Window warning following user interaction](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6a1536d89191eef4750eea_blog-detecting-multi-stage-pop-up-window-warning-following-user-interaction.webp)

_Figure 6. Pop-up Window warning following user interaction_

When the user interaction succeeded in passing these previous steps, the LNK execution will not open a PDF file but instead runs an HTA file (usually on the same website, but in some cases it can be a distinct one).

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12638_6a92a1d8dae089660dfbcf72_6a2a7f3d777d393c53814412.webp)

_Figure 7. LNK file properties pointing to the HTA file_

The HTA file uses Windows VBScript language to execute a BAT file from the same remote server.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1265c_6a92a1d96929191488991ca4_6a2a7f3d777d393c53814415.webp)

_Figure 8. Suspicious HTA content_

The HTA execution triggers the simple Sigma rule “[Mshta Suspicious Child Process](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/mshta_suspicious_child.yml)”, matching on the “cmd.exe” process run from “mshta.exe”. This is a really efficient way to detect that first step, which does not generate many false positives in our customer’s environments (only around 60 alerts in the last few days globally).

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12656_6a92a1dddae089660dfbd1b4_6a2a7f3d777d393c53814424.webp)

_Figure 9. Mshta Suspicious Child Process related events_

The Sigma correlation rule “[HTA Infection Chains](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/correlation_lnk-hta_infection_chain.yml)” aims at detecting any infection chain using an HTA file followed by some suspicious commands. In that case we are raising an alert, based on the temporal proximity between the HTA file creation and the “mshta.exe” that runs the previous file with the Explorer application as a parent process.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12650_6a92a1db693fca262e1a92ab_6a2a7f3d777d393c5381441e.webp)

_Figure 10. HTA Infection Chains related events_

The BAT file execution is quite complex (with many steps and relying on obfuscation to prevent any quick analysis/detection). In short, the script still leverages PowerShell to download and install its dependencies (two files archives containing the Python language and the Python scripts). For more detailed information, we advise you to read the [Fortinet report,](https://www.fortinet.com/blog/threat-research/purehvnc-deployed-via-python-multi-stage-loader) which is very complete and interesting.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12653_6a92a1d4bd6424423eee9184_6a2a7f3d777d393c53814406.webp)

_Figure 11. PowerShell execution for Python installation_

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12632_6a92a1d265cc84bc266e7153_6a2a7f3d777d393c53814400.webp)

 _Figure 12. Installation folders_

The BAT script's main objective is to proceed with the next step that requires Python language. This condition induces a particularly noisy activity as a side effect, which succeeded in triggering our rule “[ISO LNK Infection Chain](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/correlation_iso-lnk_chain.yml)”. In this rule, we are looking for an archive file created on disk (here not an ISO but an XZ archive) and followed by some Windows commands within five minutes. The Python installation directory embedding some archives files followed by PowerShell commands could trigger this kind of behaviour.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1263e_6a92a1d5dae089660dfbcc87_6a2a7f3d777d393c53814409.webp)

_Figure 13. ISO LNK Infection Chain related events_

The last two Sigma correlation rules are more difficult to enable in some environments where a lot of command-line administration tools are used. Indeed IT administrators usually need to perform commands that are similar to some attackers' TTPs. To overcome these difficulties, it is possible to build an alert filter using temporal conditions. It requires some effort but it makes it usable in this kind of environment.

## Execution (Python -> BAT -> DLL )

In the second step of the execution, the obfuscated Python continues by injecting the next stage to several “notepad.exe” processes.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12644_6a92a1e2a7a0bb1897156194_6a2a7f3d777d393c53814439.webp)

_Figure 14. Injection to notepad.exe_

Persistence is created using the Windows Startup folder with two VBS files and one BAT file, similar to the previous BAT file in terms of obfuscation. The VBS files are likely used to detect sandbox detonation with a loop over pressing a given key.

The obvious way to detect this behaviour/technique is to monitor these filesystems entries continuously. However, this can lead to false positives in the detection process. To avoid this downside, it is possible to use a hunting query which would quickly help the analyst to find the unusual entries.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12641_6a92a1d34538ee1e1c2e40bc_6a2a7f3d777d393c53814403.webp)

_Figure 15. Startup folder with the added VBS and BAT files_

Using the new [Sekoia Operating Language](https://docs.sekoia.com/xdr/features/investigate/sekoia_operating_language/), we could detect those entries with the following query.

`events  
  
| where timestamp >= ago(30d)  
  
| where file.path contains "Startup\"  
  
| where file.path contains "Users"  
  
| distinct file.path  
`

 _Code 1. SOL query sample for startup folder entries_

C:\Users\\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\PWS.vbs  
---  
C:\Users\\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\pws1.vbs  
C:\Users\\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startupppp.bat  
  
 _Code 2. SOL query results in our lab_

The next stage uses PowerShell to reflectively load a payload downloaded from a JPEG image hosted on a public website with a base64 payload.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1265f_6a92a1dea2f46752fd00b276_6a2a7f3d777d393c53814427.webp)

_Figure 16. PowerShell code run for the latest stage_

This loading technique through the process “AddInProcess32” triggers our rule “[Suspicious PowerShell Keywords](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/powershell_suspicious_keywords.yml)” precisely on the “[System.Reflection.Assembly]::Load()” call.

Finally the remote access trojan (RAT) channel to its command and control server (C2) is fully established.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1262f_6a92a1d1dae089660dfbc997_6a2a7f3d777d393c538143fd.webp)

_Figure 17. Connection to the AsyncRAT C2_

## Defense Evasion

After the BAT file has completed the Python part installation, some cleanup and defensive evasion is done. The script action can be flagged by the common Sigma rule “[Hiding Files With Attrib.exe](https://github.com/SEKOIA-IO/Community/tree/main/sigma_rules/host/attrib_hiding_files.yml)”, detecting the usage of the Windows command “attrib.exe” with the parameters allowing to change the Python folders properties to mark it as a hidden one for Windows file system (in that case “Extracted” and “Print”).

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1263b_6a92a1df4538ee1e1c2e42a7_6a2a7f3d777d393c5381442a.webp)

_Figure 18. Attrib commands to hide installation folders_

That technique is frequently used as well by legitimate software, but could help as a weak signal in that case. The fact it would occur several minutes after the initial infection could be difficult to correlate with the attack, but the used folder paths are an indicator as they look very suspicious.

## Command and Control

Almost all previously mentioned files are hosted in the attacker infrastructure, which is the suspicious URI using the **“Cloudflare tunnel infrastructure”** relying on the TryCloudflare service with the WebDAV protocol. Off note, from our latest tests, we observed that the fake PDF invoice file, which was displayed to the user, is not always hosted in this infrastructure.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd1264a_6a92a1da16f788fda8e44c92_6a2a7f3d777d393c5381441b.webp)

_Figure 19. TryCloudflare hosted files_

As this attacker infrastructure is under our continuous watch, we were able to detect the actual detonation network connection to this domain by our CTI feed.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12659_6a92a1d716f788fda8e44bec_6a2a7f3d777d393c5381440f.webp)

_Figure 20. WebDAV connections from the infected host_

The intermediate image file for the reflective DLL was hosted on a compromised website which was not known to us as an attacker infrastructure but which has a very suspicious file name: “ENCRYPTION01.jpg”. The exact same technique has been used in other infection chains. We will not detail it in this report, but we will continue to monitor it.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6b22bff9b3e51fadcf16a0_blog-suspicious-image-and-the-hidden-base64-code.webp)

_Figure 21. Suspicious image and the hidden base64 code_

The last network accesses to the AsyncRAT C2, are hosted to public IP addresses resolving to domain names using the “dyndns.org” service. This is detected both by our CTI feed (AsyncRAT C2 are tracked), and by our Sigma rule based on CTI enrichment “[Dynamic DNS Contacted](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/network/dynamic_dns_domain.yml)”.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5619f9b7f8b2cd12647_6a92a1e3fd507e2a51b97570_6a2a7f3e777d393c5381443d.webp)

_Figure 22. Dynamic DNS Contacted related events_

While this rule is a very effective way to find suspicious C2 connections, it can be challenging to implement in environments where this type of activity is common.

## Conclusion

This report delves into the intricate details of a multi-stage attack that has been exploiting a resilient network infrastructure, referred to as **“Cloudflare tunnel infrastructure to deliver multiple RATs”** since February 2024.

The mentioned infection chain is trying to bypass security defenses in various and complicated ways. One could be surprised that such techniques are being used by attackers in 2025, when efficient security products combined with in depth security measures should prevent such attacks. This example illustrates how **cyber threat intelligence** (CTI) combined with **detection rules** enhances detection capabilities. Indeed, our resilience to the evolving infection chains of attackers is hopefully maintained by our detection rules strategy. This strategy uses a mixture of CTI and in-depth coverage of the possible attacker steps, from basic TTPs to a combination of several TTPs.

**Sekoia TDR** team is committed to ongoing monitoring of similar attacks and will bolster proactive defense strategies by evaluating the efficiency of existing detection methods.

## IoCs & Technical details

## Command and Control servers

`malawi-light-pill-bolt[.]trycloudflare[.]com  
  
players-time-corresponding-th[.]trycloudflare[.]com  
  
spaces-corner-notices-battery[.]trycloudflare[.]com  
  
xi-if-grows-valued[.]trycloudflare[.]com  
  
phvnmarch8787[.]duckdns[.]org  
`

## Files hashes

`0d8d46ec44e737e6ef6cd7df8edf95d83807e84be825ef76089307b399a6bcbb (mslibrary attachment)  
  
c935cc41342794c23d640333a1ddd511f9c51e5b790261dc848ec5f7ac28650a (ben.bat)  
  
47453b0ad93f60254ffb30a0964e0b8b6f1979e199d707b971c6ab6277fe0185 (jmb.hta)  
  
5d932bfda0ffd31715700de2fd43fc89c0f1d89eeabac92081ebe2062da84152 (pws1.vbs)  
  
0d7cee0c13374181a23e8f605b32f2969c9c490b83c7891318f26bd17777fd7c (PWS.vbs)  
  
e0e0f9a1082b641acff2cb225454342ca54109d01001b0e20b4fac0c9d5501a4 (RE_0059038327392.pdf.lnk)  
  
c458a21ae510f81fd76affb147ce84008c66b9dab246f6a2322e0f3b137e0539 (RE_070362683042.pdf.lnk)  
  
33feae2e66e25f1b2d5905e0ce7b837bdeb6e8e9782ab39ff06b2243a7c4b5e7 (RE_1047389392.pdf.lnk)  
  
a0a446acd5540772ab9a3ae2f78f94f9a203cae06249d9e70710d7f797ff9da9 (startupppp.bat)  
  
0ff5dd1787acc886a586282858112c6f73b48c31093080d2d8a6e66f018ce8c7 (ENCRYPTION01.jpg)  
`

## Sigma rules

  * [Suspicious Email Attachment Received](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/network/email_suspicious_attachment_received.yml)
  * [Mshta Suspicious Child Process](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/mshta_suspicious_child.yml)
  * [HTA Infection Chains](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/correlation_lnk-hta_infection_chain.yml)
  * [ISO LNK Infection Chain](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/correlation_lnk-hta_infection_chain.yml)
  * [Suspicious PowerShell Keywords](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/powershell_suspicious_keywords.yml)
  * [Hiding Files With Attrib.exe](https://github.com/SEKOIA-IO/Community/tree/main/sigma_rules/host/attrib_hiding_files.yml)
  * [Dynamic DNS Contacted](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/network/dynamic_dns_domain.yml)