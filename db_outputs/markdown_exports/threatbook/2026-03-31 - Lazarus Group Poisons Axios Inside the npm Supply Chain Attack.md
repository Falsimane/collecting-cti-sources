# Lazarus Group Poisons Axios: Inside the npm Supply Chain Attack

- **Source :** threatbook
- **URL :** https://threatbook.io/blog/lazarus-group-poisons-axios-inside-the-npm-supply-chain-attack
- **Date :** 2026-03-31

---

4 min read 

# Lazarus Group Poisons Axios: Inside the npm Supply Chain Attack

[ ![Picture of ThreatBook Research Team](https://threatbook.io/hubfs/Brand%20Resources/favicon-192x192.png) ThreatBook Research Team ](https://threatbook.io/blog/author/threatbook-research-team) :  Updated on March 31, 2026 

[Threat Research](https://threatbook.io/blog/tag/threat-research)

**Table of Contents**

Sample Analysis

Attribution Analysis

Appendix

Regarding yesterday's [Axios npm supply chain poisoning incident](/blog/openclaw-users-at-risk-axios-on-npm-backdoored-with-cross-platform-rat), ThreatBook has conducted in-depth sample analysis and attack tracing. Drawing on long-term threat intelligence accumulated through tracking key APT organizations, **we attribute this attack campaign to the Lazarus Group, and have pivoted from existing intelligence to identify additional associated infrastructure and attack indicators (IOCs listed in theappendix).**

This incident has had significant impact. As one of the most foundational dependencies in the JavaScript ecosystem, Axios has over 3.6 billion annual downloads and more than 174,000 projects that directly or indirectly depend on it. A number of users have already been infected with malicious code while installing OpenClaw and related software. Windows, macOS, and Linux are all affected. Users are advised to immediately check for callbacks to `sfrclak.com`.

## Sample Analysis

In this attack, Lazarus hijacked an Axios maintainer account to publish malicious versions, covertly planting the malicious dependency `plain-crypto-js@4.2.1`. This package uses a postinstall hook to automatically execute a script that downloads a remote access trojan, enabling device compromise and data theft. The attack flow is as follows:

![](https://threatbook.io/hs-fs/hubfs/image-png-3.png?width=1532&height=688&name=image-png-3.png)

`plain-crypto-js@4.2.1` was poisoned in the Axios npm repository, affecting Axios versions 1.14.1 and 0.30.4. The `package.json` introduces a postinstall trigger that executes the malicious `setup.js` file.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-36-06-9840-PM.png?width=608&height=93&name=undefined-Mar-31-2026-04-36-06-9840-PM.png)   


The `setup.js` that runs is obfuscated JavaScript code.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-36-18-2972-PM.png?width=1914&height=415&name=undefined-Mar-31-2026-04-36-18-2972-PM.png)The function of this JS file is to detect the platform of the host, use the relevant `packages.npm.org/` URL as a parameter to download the payload appropriate for the host system, and execute the download of the subsequent trojan carrying the attacker's `C2_url` parameter. `C2_url`: `http://sfrclak.com:8000/6202033`.

Platform | Download Location | POST Request Parameter  
---|---|---  
Linux | `/tmp/ld.py` | `packages.npm.org/product2`  
Windows | `%TEMP%\6202033.ps1` | `packages.npm.org/product1`  
macOS | `/Library/Caches/com.apple.act.mond` | `packages.npm.org/product0`  
  
File hashes for the subsequent payloads by OS are listed in the "Previously Disclosed IOCs" section of the appendix.

The analysis below uses the macOS payload `/Library/Caches/com.apple.act.mond` as the primary example. This trojan is developed in C++ and exists in two versions: one for ARM architecture and one for x86_64.

After the trojan runs with the `C2_url`, it first collects basic host information including hostname, username, OS type and version, CPU information, system time, and the user process list. ![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-36-53-1718-PM.png?width=1343&height=716&name=undefined-Mar-31-2026-04-36-53-1718-PM.png) It then beacons to the C2 provided in the parameters — `http://sfrclak.com:8000/6202033` — using the hardcoded UA: `mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)`.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-37-10-7043-PM.png?width=851&height=457&name=undefined-Mar-31-2026-04-37-10-7043-PM.png)

The trojan's main function supports parsing C2 commands and executing the corresponding basic remote control functions: process termination, shell execution, process injection (`DoActionIjt`), script execution (`DoRunScpt` / `DoActionScpt`), and collection of directory information from specified paths (`DoActionDir`).

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-37-21-2671-PM.png?width=1293&height=740&name=undefined-Mar-31-2026-04-37-21-2671-PM.png)

Meanwhile, the Linux `ld.py` payload and the Windows `temp.ps1` are different-language versions of the same trojan with completely identical functionality.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-37-27-5583-PM.png?width=1630&height=757&name=undefined-Mar-31-2026-04-37-27-5583-PM.png)

ThreatBook Research Team used the above trojan's characteristics to conduct threat hunting, identifying multiple additional samples involved in this incident. Details are in the "New IOCs" section of the appendix.

## Attribution Analysis

ThreatBook's analysis finds that the trojan discovered in this incident is highly similar to the WAVESHAPER trojan used by the Lazarus APT organization — as disclosed by Mandiant in February 2026 — in terms of TTPs, trojan behavior and associated hunting rules, network communication UA, subsequent payload drop paths, host information collection methods, and API call parameters. We can confirm they share a common origin. Detailed analysis follows.

### 1\. Lazarus Historical Attack TTP Correlation

In this attack, the binary trojan that first lands on macOS victims is at the path:

`/Library/Caches/com.apple.act.mond`

Comparing this to the WAVESHAPER trojan drop path reported by Mandiant in their February 2026 disclosure of UNC1069 activity (attributed to Lazarus by ThreatBook):

`/Library/Caches/com.apple.mond`

The two paths are completely identical, and the filenames are highly similar.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-37-36-6837-PM.png?width=2222&height=1692&name=undefined-Mar-31-2026-04-37-36-6837-PM.png)Reference: [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence/unc1069-targets-cryptocurrency-ai-social-engineering)

In a Lazarus attack campaign captured by ThreatBook in the second half of 2025, the Nukesped trojan drop path was `/Library/Caches/System Settings` — consistent with the trojan drop directory in this supply chain poisoning incident. Furthermore, the command and parameters used by the trojan to collect the macOS user process list (`sh -c ps -eo user,pid,command`) are completely identical.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-38-16-0483-PM.png?width=993&height=498&name=undefined-Mar-31-2026-04-38-16-0483-PM.png)  _Image: Process list collection by the com.apple.act.mond trojan in this incident_

### 2\. WAVESHAPER Trojan Correlation

ThreatBook was temporarily unable to obtain the WAVESHAPER sample referenced in Mandiant's disclosure report (MD5: `c91725905b273e81e9cc6983a11c8d60`). However, comparing the trojan behavior and associated hunting rules described in that report, we find that the `com.apple.act.mond` trojan in the current incident is highly similar to the WAVESHAPER trojan — both are C++ macOS trojans with essentially identical basic host information collection functionality.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-38-36-6221-PM.png?width=847&height=710&name=undefined-Mar-31-2026-04-38-36-6221-PM.png)

_Image: Mandiant's disclosure of WAVESHAPER, and its functions and features._

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-38-49-5756-PM.png?width=757&height=331&name=undefined-Mar-31-2026-04-38-49-5756-PM.png)

_Image: Host information collection in the com.apple.act.mond trojan's main function_

Further comparison against Mandiant's published YARA detection rule (`G_Backdoor_WAVESHAPER_1`):
    
    
    rule G_Backdoor_WAVESHAPER_1 {  
    	meta:  
    		author = "Google Threat Intelligence Group (GTIG)"  
    		date_created = "2025-11-03"  
    		date_modified = "2025-11-03"  
    		md5 = "c91725905b273e81e9cc6983a11c8d60"  
    		rev = 1  
    	strings:  
    		$str1 = "mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)"  
    		$str2 = "/tmp/.%s"  
    		$str3 = "grep \"Install Succeeded\" /var/log/install.log | awk '{print $1, $2}'"  
    		$str4 = "sysctl -n hw.model"  
    		$str5 = "sysctl -n machdep.cpu.brand_string"  
    		$str6 = "sw_vers --ProductVersion"  
    	condition:  
    		all of them  
    }  
    

The hardcoded network communication UA in the current trojan (`mozilla/4.0 (compatible; msie 8.0; windows nt 5.1; trident/4.0)`), subsequent payload drop paths, host information collection methods, and API call parameters are all highly consistent. We can confirm that `com.apple.act.mond` and the WAVESHAPER trojan share a common code origin. ![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-38-59-7676-PM.png?width=1048&height=630&name=undefined-Mar-31-2026-04-38-59-7676-PM.png) ![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-39-05-0875-PM.png?width=1261&height=656&name=undefined-Mar-31-2026-04-39-05-0875-PM.png) ![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-39-09-8672-PM.png?width=961&height=441&name=undefined-Mar-31-2026-04-39-09-8672-PM.png)

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-04-39-14-8010-PM.png?width=825&height=439&name=undefined-Mar-31-2026-04-39-14-8010-PM.png)

Based on the above attribution analysis, we assess that the `com.apple.act.mond` trojan used in the current incident is the WAVESHAPER trojan, and that the threat organization behind it is the Lazarus APT Group.

## Appendix

### Previously Disclosed IOCs

**C2**

  * `sfrclak.com`

  * `http://sfrclak.com:8000/6202033`

  * `142.11.206.73`




**Hash**

Platform | SHA256  
---|---  
Linux (`ld.py`) | `fcb81618bb15edfdedfb638b4c08a2af9cac9ecfa551af135a8402bf980375cf`  
Windows (`6202033.ps1`) | `617b67a8e1210e4fc87c92d1d1da45a2f311c08d26e89b12307cf583c900d101`  
Windows persistence (`system.bat`) | `f7d335205b8d7b20208fb3ef93ee6dc817905dc3ae0c10a0b164f4e7d07121cd`  
macOS (`com.apple.act.mond`) | `92ff08773995ebc8d55ec4b8e1a225d0d1e51efa4ef88b8849d0071230c9645a`  
  
###   
New IOCs

**C2**

  * `callnrwise.com`

  * `142.11.196.73`

  * `142.11.199.73`




`**Hash**`

`5b5fbc627502c5797d97b206b6dcf537889e6bea6d4e81a835e103e311690e22 46f5eea70d536f7affe40409d7aaa5fa0009f0dc4538ba2867cb7569737db859 8c8f5f095d65d3f33ce89a77dfbe84a79bb29d2e0073a57a23dcc014d0683c2e 506690fcbd10fbe6f2b85b49a1fffa9d984c376c25ef6b73f764f670e932cab4 4465bdeaddc8c049a67a3d5ec105b2f07dae72fa080166e51b8f487516eb8d07 ed8560c1ac7ceb6983ba995124d5917dc1a00288912387a6389296637d5f815c`  


  *   * Share
  * 


[ ![Inside the Attack: Complete Technical Breakdown of the AI Ecosystem Threat Campaign](https://threatbook.io/hubfs/Inside%20the%20Attack%20Complete%20Technical%20Breakdown%20of%20the%20AI%20Ecosystem%20Threat%20Campaign.jpeg) ](https://threatbook.io/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign)

1 min read 

#### [Inside the Attack: Complete Technical Breakdown of the AI Ecosystem Threat Campaign](https://threatbook.io/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 20 March 2026, 08:03 AM

This is the full technical companion to our campaign overview published in Part 1. It documents the Windows and macOS malware chains in detail, and...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign)

[ ![Apple Libnotify/notifyd Stack Overflow \(CVE-2026-64739\) — Discovered by ThreatBook XGPT](https://threatbook.io/hubfs/featured-hubspot-1200x630.png) ](https://threatbook.io/blog/apple-libnotify-cve-2026-64739)

1 min read 

#### [Apple Libnotify/notifyd Stack Overflow (CVE-2026-64739) — Discovered by ThreatBook XGPT](https://threatbook.io/blog/apple-libnotify-cve-2026-64739)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 28 July 2026, 05:07 PM

On July 27, 2026, Apple released security updates for iOS 26.6 and iPadOS 26.6, fixing vulnerabilities across several components — Accessibility,...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/apple-libnotify-cve-2026-64739)

[ ![Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/hubfs/Blog%20Images/Singapore%20Cyber%20Threat%20Landscape%202025.png) ](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

1 min read 

#### [Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 16 March 2026, 12:03 AM

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)