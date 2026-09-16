# How a Malicious Plugin Turned OpenClaw Into a Credential Stealer

- **Source :** threatbook
- **URL :** https://threatbook.io/blog/how-a-malicious-plugin-turned-openclaw-into-a-credential-stealer
- **Date :** 2026-03-18

---

2 min read 

# How a Malicious Plugin Turned OpenClaw Into a Credential Stealer

[ ![Picture of ThreatBook Research Team](https://threatbook.io/hubfs/Brand%20Resources/favicon-192x192.png) ThreatBook Research Team ](https://threatbook.io/blog/author/threatbook-research-team) :  March 18, 2026 

[Threat Research](https://threatbook.io/blog/tag/threat-research)

**Table of Contents**

How the Attack Worked

Beyond Malicious Plugins: The Broader OpenClaw Risk Surface

What to Do

Last week, ThreatBook's endpoint detection product, OneSEC EDR, identified and fully captured an active attack targeting OpenClaw users. The attack exploited OpenClaw's Skills plugin mechanism to deliver a credential-stealing trojan — without any user action beyond loading a third-party Skill.

This was not an isolated incident. ThreatBook assesses it as part of a broader, organized campaign by a financially motivated threat group. A full threat actor profile is covered in our companion pieces in this series. Here, we document the attack chain in detail — because understanding what happened is the first step toward not letting it happen again.

## How the Attack Worked

Skills are plugin configuration files used by AI coding agents to extend their capabilities. They are increasingly shared through community repositories, downloaded and activated in the same way a developer might install a package from a public registry. The attack exploited this trust chain entirely.

[Note: OneSEC EDR is currently only available in Chinese. Explanation is provided in English above the screenshots.]

**Step 1 — Malicious Skill execution**

The attacker distributed a crafted Skills plugin containing Base64-obfuscated instructions embedded in the plugin's Prerequisites section. When OpenClaw loaded the Skill as part of its normal initialization, it executed the embedded payload. The user saw nothing unusual.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-30-32-8329-AM.png?width=1080&height=341&name=undefined-Mar-13-2026-06-30-32-8329-AM.png)

**Step 2 — Malware download initiated**

The Skill triggered a download of secondary malware from an attacker-controlled server. OneSEC traced the download path back to the originating OpenClaw process, establishing the chain of custody needed to attribute the intrusion.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-30-45-7110-AM.png?width=1080&height=389&name=undefined-Mar-13-2026-06-30-45-7110-AM.png)

**Step 3 — Trojan execution in a temporary directory**

The downloaded binary executed from the system's temporary storage path, spawning malicious child processes designed to blend into normal system activity and evade conventional detection.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-31-01-5588-AM.png?width=1080&height=364&name=undefined-Mar-13-2026-06-31-01-5588-AM.png)

**Step 4 — Credential harvesting via spoofed system dialog**

The trojan used AppleScript to generate a dialog window visually indistinguishable from a legitimate macOS system authentication prompt — asking the user to re-enter their login credentials due to a fictitious system requirement.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-31-17-7920-AM.png?width=1080&height=432&name=undefined-Mar-13-2026-06-31-17-7920-AM.png)

**Step 5 — Password validation and exfiltration**

The malware used macOS's built-in dscl utility to verify the entered password against the local account database — confirming correctness before exfiltrating it to attacker infrastructure. The victim received no indication anything was wrong.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-31-28-5572-AM.png?width=1080&height=332&name=undefined-Mar-13-2026-06-31-28-5572-AM.png)

_OneSEC detected and reconstructed the complete attack chain across all five stages. The full process — from Skill load to credential exfiltration — executed in under two minutes._

## Beyond Malicious Plugins: The Broader OpenClaw Risk Surface

Malicious Skills are one category of OpenClaw-related risk. Organizations should also account for:

  * Unpatched vulnerabilities — certain OpenClaw versions contain CVE-2026-25253, a zero-click remote code execution flaw requiring no user interaction to exploit.
  * Misconfigured deployments — instances deployed with default settings may expose administrative consoles directly to the public internet.
  * Autonomous agent behavior — OpenClaw can misinterpret instructions and take consequential actions without explicit authorization, including deleting files or transmitting sensitive data to external platforms.



## What to Do

Any Skills file sourced from outside of verified, trusted channels should be submitted to a sandbox environment for analysis before being loaded. ThreatBook's OneSandbox supports this workflow and can be integrated into pre-deployment review processes.

For broader governance, ThreatBook's OneSEC platform now includes dedicated OpenClaw controls: automated asset inventory, department-level and version-specific access policies, and time-based usage restrictions — giving security teams the ability to enable AI productivity tools without accepting unmanaged risk.

  * [Tweet](https://twitter.com/share)
  * Share
  * 


[ ![APAC's Cyber Threat Landscape: Inside the 2026 Mid-Year Data](https://threatbook.io/hubfs/blog-header-1600x840.png) ](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

1 min read 

#### [APAC's Cyber Threat Landscape: Inside the 2026 Mid-Year Data](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 21 July 2026, 07:07 AM

ThreatBook Labs recorded 15,205 security incidents across Asia-Pacific between June 2025 and June 2026. Read one at a time, they look like an...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

[ ![Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/hubfs/Blog%20Images/Singapore%20Cyber%20Threat%20Landscape%202025.png) ](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

1 min read 

#### [Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 16 March 2026, 12:03 AM

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

[ ![SilverFox: Not an Organization, But a Tool - Uncovering the Underground Ecosystem](https://threatbook.io/hubfs/Silver_Fox.png) ](https://threatbook.io/blog/silver-fox-not-an-organization-but-a-tool-uncovering-the-underground-ecosystem)

1 min read 

#### [SilverFox: Not an Organization, But a Tool - Uncovering the Underground Ecosystem](https://threatbook.io/blog/silver-fox-not-an-organization-but-a-tool-uncovering-the-underground-ecosystem)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 1 July 2023, 03:07 PM

Executive Summary For months, the cybersecurity community tracked what appeared to be a sophisticated cybercrime organization dubbed "SilverFox"....

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/silver-fox-not-an-organization-but-a-tool-uncovering-the-underground-ecosystem)