# Threat Actor Distributes Python-Based Info Stealer Using Fake Update

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/threat-actor-distributes-python-based-information-stealer/
- **Date :** July 23, 2024

---

# Threat Actor Distributes Python-Based Information Stealer Using a Fake Falcon Sensor Update Lure

July 23, 2024

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


## Summary

On July 23, 2024, CrowdStrike Intelligence identified a malicious ZIP file containing a Python-based information stealer now tracked as _Connecio_. A threat actor distributed this file days after the July 19, 2024, single content update for CrowdStrike’s Falcon sensor — which impacted Windows operating systems — was identified and a fix was deployed. The ZIP file uses the filename `CrowdStrike Falcon.zip` in an attempt to masquerade as a Falcon update. CrowdStrike Intelligence does not currently attribute the analyzed activity to any named adversary.

## Technical Analysis

Technical analysis is based on the ZIP archive (SHA256 hash: `5ba542fcfa45d50c0d65dda4dbbd7a28f737a2fc53841ddaab7f68ae1cdf5183`) that was uploaded to a public malware repository on `2024-07-23 12:09 UTC` with the filename `CrowdStrike Falcon.zip`. This archive contains the files shown in Table 1.

**Filename**| **SHA256 Hash**  
---|---  
`Readme.txt`| `56cbd8ce60f18d4cececfa703a92c0188dd81ed97b4de12e3f120d7ce736225a`  
`CrowdStrike Falcon.exe`| `21653e267a6c7e4f10064ad2489dba54e04612cc7ce4043b8c8dcaf8b39210d6`  
  
**Table 1. Archive CrowdStrike Falcon.zip content**

The file `CrowdStrike Falcon.exe` is a self-extracting RAR (SFX) that contains and executes a Python-compiled executable; this executable contains the _Connecio_ information stealer.

The text file `Readme.txt` contains instructions for potential victims to disable Windows Defender and execute the malicious executable present in the archive (Figure 1).

![](https://www.crowdstrike.com/wp-content/uploads/2024/07/Intel-blog-4-Fig-1-Read-Me.png)

Figure 1. Readme.txt content

Upon execution, the malicious file `CrowdStrike Falcon.exe` unpacks and invokes an information stealer written in the Python programming language that collects system information, the system’s external IP address (by making an HTTP `GET` request to the URL `http[:]//ipinfo[.]io/[]?token=7fb82f5925fe8b`), and data from multiple web browsers.

Then, the information stealer resolves its command-and-control (C2) servers by making HTTP `GET` requests to the Pastebin dead-drop URLs shown in Table 2.

**Pastebin Dead-Drop URL**| **Description**  
---|---  
`https[:]//pastebin[.]com/FHfj1fYD`| C2 server configuration  
`https[:]//pastebin[.]com/HeVWATy1`| Simple Mail Transfer Protocol (SMTP) accounts to exfiltrate collected information via email  
`https[:]//pastebin[.]com/2diVWcDQ`| List of cryptocurrency address patterns and potential replacements; the addresses are likely used for clipboard-hijacking cryptocurrency theft, as they match cryptocurrency addresses and the malware uses the Python library `pyperclip` to control the clipboard1  
  
1 https[:]//pypi[.]org/project/pyperclip/

**Table 2. Pastebin dead-drop URLs**

## Recommendations

These recommendations can be implemented to help protect against the activity described in this report.

  * Only accept updates delivered through CrowdStrike official channels and adhere to CrowdStrike support teams’ technical guidance
  * Train users to avoid executing files from untrusted sources
  * Check website certificates on the download page to ensure downloaded software originates from a legitimate source
  * Use browser settings to enable download protection that can issue warnings regarding potentially harmful websites or downloads
  * Block SMTP network connections to unknown servers when not required within the organization
  * Block Pastebin web access when not required within the organization



## Appendix

### YARA Rule

This YARA rule detects common strings for the _Connecio_ information stealer.

`rule CrowdStrike_CSA_240846_01 : connecio python stealer ` `{` `meta:` `copyright = "(c) 2024 CrowdStrike Inc."` `description = "Common strings for Connecio Python stealer"` `reports = "CSA-240846"` `version = "202407231719"` `last_modified = "2024-07-23"` `malware_family = "Connecio"` `strings:` `$ = "C0nn3c+10nz"` `$ = "?token="` `$ = "ACCOUNT(S) INFO COOKIE"` `$ = "Firefox.get_password"` `$ = "Brave.get_password"` `$ = "Chrome.get_password"` `$ = "MACHINE : "` `condition:` `5 of them` `}`  
---  
  
### Falcon LogScale Queries

This Falcon LogScale query detects the activity described in this report.

`// Indicators related to CSA-240846` `case { in("SHA256HashData", values=["21653e267a6c7e4f10064ad2489dba54e04612cc7ce4043b8c8dcaf8b39210d6", "56cbd8ce60f18d4cececfa703a92c0188dd81ed97b4de12e3f120d7ce736225a", "5ba542fcfa45d50c0d65dda4dbbd7a28f737a2fc53841ddaab7f68ae1cdf5183", "d7c1be2d0b7d2714ff710676d228ac751c4eba280309e1241a9f7e441299a177"]); in("DomainName", values=["dshu.xyz", "klaxusonline.com", "mail.dshu.xyz", "theprofits.online", "web3versecoin.com", "xryptbx.com"]); in("RemoteAddressIP4", values=["139.99.232.135", "185.255.114.110", "185.255.114.63"]) } | table([cid, aid, #event_simpleName, ComputerName])`  
---  
  
### Indicators of Compromise (IOCs)

This table details the IOCs related to the information provided in this report.

**Description**| **Value**  
---|---  
C2 IP addresses| `139.99.232[.]135:80`  
`185.255.114[.]110:80``185.255.114[.]63:80`  
SMTP exfiltration-sender accounts| `send@dshu[.]xyz` `logs@web3versecoin[.]com` `logsmaster@xryptbx[.]com`  
SMTP exfiltration-recipient accounts| `logs@theprofits[.]online` `info2024@klaxusonline[.]com` `frank@dshu[.]xyz` `6000@xryptbx[.]com`  
SMTP exfiltration hosts| `mail.dshu[.]xyz:465` `web3versecoin[.]com:465` `xryptbx[.]com:465`  
  
**Table 3. IOCs**

### MITRE ATT&CK

This table details the MITRE ATT&CK® tactics and techniques described in this report.

**Tactic**| **Technique**| **Observable**  
---|---|---  
**Execution**|  T1059.006 – Command and Scripting Interpreter: Python|  _Connecio_ is written in the Python programming language  
T1204.002 – User Execution: Malicious File|  _Connecio_ lures the user into executing the malware executable  
**Command and Control**|  T1102.001 – Web Service: Dead Drop Resolver|  _Connecio_ uses Pastebin dead-drop URLs to resolve its C2 infrastructure  
**Exfiltration**|  T1048 – Exfiltration Over Alternative Protocol|  _Connecio_ exfiltrates information over SMTP  
  
**Table 4. Described _Connecio_ activity MITRE ATT&CK mapping**

### Cryptocurrency Addresses

The following table includes cryptocurrency addresses obtained from the dead-drop configuration URL.

**Address**  
---  
`0x2DCC92C27C4429B506588012CaC53764780f3e3D`  
`0x6c5E3Ea51B382C49839417dAF3c84E3dA603D12f`  
`0xd23896016eC1Ef2D25Fb8899a4a3a38e0a92F9c1`  
`13KadCbGWS4rzXiAyc7HHW2HDopN59hKa6`  
`17tVNxknYnnkrvY3vN4Tw23fXQdSmn7CDU`  
`1Q4V4c1d6Vmr1Bf9BWejixnF8XnfdY6m4s`  
`bc1qfwx6sase663vranpr7mkf485ypz3nzvtl0xtld`  
`bc1qlneepetqamw7vmfludvrjgnk7tjprzlcy5e293`  
`bc1qr9euay9qsfwsgh2edeqfk0rpw90c9zl9f69kfk`  
`bnb10nf3fc0xtfm6f7xfy6vjejnyq88ha7gjc8hx62`  
`bnb130y4jppcnh2vmwc6u4kkktehswldmrk43l7nah`  
`bnb1xg0dn3lj6ggekxptv4mg7u89uqqu73ezpxkhup`  
`CrnP9VWgegWAFgKYHqsrLhxoWwBykAaHQDkz7A8njtMj`  
`DMqCf1f3wCHncDdbHmNZa2AFwyVYDeVSRL`  
`DMX3TTkhnDvB7nbhG3jn85U1bHedVsfgJs`  
`Fep17BczJDfVeSHytKmCS1n2MBM5j6BVdVEkcN5H1eXJ`  
`LcxgZpuNmbji8WfWrEpWHKDA41wGcRxJFe`  
`LLGtBdhMb7DABq9Q1yDEGUXAvtn4CyPGh7`  
`ltc1qg9k9ren5rmu65l9jy69lt7tqrl60s7u8e6gv9m`  
`qz0zv0l5gqz5f69l8ezpwu8mpfhzv8lwruz5dh2h7p`  
`qz9zwucyjf8jw7yhr3dm85ejslaesrrp9y3qh6x2h9`  
`qzanj5umvjs3h6fjplzxh68lnm3hzl7djq9aky0xwn`  
`t1KikBNAhHPWBTvDmzzcoUMJ8CKxo8dm2hF`  
`TAZnA51ca5P2hpcjUwY6eqYvDL9fGzad3M`  
`TFhAp8GYQiyYk3xGgDXoNDokDzKZnMoUuT`  
`XiDCvcyAnTKEr6vQn7rjwpjH6tiwhEPPA5`  
`XkarQqC1GGjuF8eQEhWeBifFTz4UyLG7z3`  
`Xy4yi1Qr7UgEh4hSi8dLv7iANecm11MDGM`  
  
**Table 5._Connecio_ -related cryptocurrency addresses**

#### Additional Resources

_Read other blog posts from CrowdStrike Intelligence regarding the Falcon content issue:_

  * _[Falcon Sensor Content Issue from July 19, 2024, Likely Used to Target CrowdStrike Customers](https://www.crowdstrike.com/blog/falcon-sensor-issue-use-to-target-crowdstrike-customers/)_
  *  _[Likely eCrime Actor Uses Filenames Capitalizing on July 19, 2024, Falcon Sensor Content Issues in Operation Targeting LATAM-Based CrowdStrike Customers](http://www.crowdstrike.com/blog/likely-ecrime-actor-capitalizing-on-falcon-sensor-issues/)_
  *  _[Threat Actor Uses Fake CrowdStrike Recovery Manual to Deliver Unidentified Stealer](https://www.crowdstrike.com/blog/fake-recovery-manual-used-to-deliver-unidentified-stealer/)_



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)