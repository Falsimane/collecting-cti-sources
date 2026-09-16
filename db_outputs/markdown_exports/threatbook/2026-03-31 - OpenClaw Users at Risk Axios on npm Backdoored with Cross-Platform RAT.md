# OpenClaw Users at Risk: Axios on npm Backdoored with Cross-Platform RAT

- **Source :** threatbook
- **URL :** https://threatbook.io/blog/openclaw-users-at-risk-axios-on-npm-backdoored-with-cross-platform-rat
- **Date :** 2026-03-31

---

3 min read 

# OpenClaw Users at Risk: Axios on npm Backdoored with Cross-Platform RAT

[ ![Picture of ThreatBook Research Team](https://threatbook.io/hubfs/Brand%20Resources/favicon-192x192.png) ThreatBook Research Team ](https://threatbook.io/blog/author/threatbook-research-team) :  Updated on March 31, 2026 

[Threat Research](https://threatbook.io/blog/tag/threat-research)

**Table of Contents**

Incident Summary

Attack Timeline (UTC)

Technical Analysis

Remediation Steps

Detection Coverage

IOCs

Axios — one of the most foundational dependencies in the JavaScript ecosystem, with over 3.6 billion annual downloads — was compromised on npm on March 31, 2026. Malicious versions 1.14.1 and 0.30.4 were published using a stolen maintainer account, and automatically download and execute a remote access trojan (RAT) upon installation. The attack affects Windows, Linux, and macOS.

ThreatBook's OneSEC EDR platform detected malicious code executing in real time on machines running OpenClaw. The malicious packages have since been removed by npm, but any environment that installed either affected version should be treated as compromised.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-05-51-29-9739-AM.png?width=1080&height=213&name=undefined-Mar-31-2026-05-51-29-9739-AM.png) ![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-31-2026-05-51-37-6180-AM.png?width=1080&height=387&name=undefined-Mar-31-2026-05-51-37-6180-AM.png)

**If you see any callback to[`sfrclak.com`](https://i.threatbook.io/research/sfrclak.com) in your network logs, your host is compromised. Block this domain immediately and follow the remediation steps below.**

**![](https://threatbook.io/hs-fs/hubfs/image-png-2.png?width=2450&height=1496&name=image-png-2.png)**

## Incident Summary

Field | Details  
---|---  
**Incident** | Axios npm supply chain poisoning — cross-platform RAT delivery  
**Affected Package** | axios (3.6+ billion annual downloads)  
**Affected Versions** | 1.14.1 and 0.30.4 (removed); safe version is 1.14.0 or earlier  
**Discovery** | March 31, 2026, ~00:05 UTC (Socket.dev automated detection)  
**Packages Removed** | March 31, 2026, ~04:00 UTC  
**Platforms Affected** | Windows, Linux, macOS  
**C2 Domain** | sfrclak.com  
**Potential Blast Radius** | All Node.js and browser applications making HTTP requests — React frontends, CI/CD tooling, server-side APIs  
  
## Attack Timeline (UTC)

  * **March 30, 23:59:12** — Attackers publish malicious dependency package `plain-crypto-js@4.2.1` to npm.
  * **March 31, ~00:00** — Using a stolen Axios maintainer npm account, attackers bypass GitHub Actions CI/CD and manually publish `axios@1.14.1` and `axios@0.30.4`, both referencing the malicious dependency.
  * **March 31, 00:05:41** — Socket.dev automated scanning flags `plain-crypto-js` as anomalous.
  * **March 31, 04:00:00** — npm removes `plain-crypto-js@4.2.1`, `axios@1.14.1`, and `axios@0.30.4` from the registry.



## Technical Analysis

### Infrastructure Setup

On March 30, attackers registered the malicious domain `sfrclak.com` in preparation for the attack. This domain serves as both the C2 server and payload delivery endpoint.

### The Poisoned Dependency: `plain-crypto-js@4.2.1`

The attack chain flows through a malicious transitive dependency. Both backdoored Axios versions reference `plain-crypto-js@4.2.1` in their `package.json`. This package includes a `postinstall` hook in its own `package.json` that triggers execution of `setup.js` immediately upon installation — before the developer ever runs any application code.

![](https://threatbook.io/hs-fs/hubfs/download-png.png?width=608&height=93&name=download-png.png)

### The Loader: `setup.js`

`setup.js` is an obfuscated JavaScript loader. Its function is straightforward: fingerprint the host operating system, then fetch and execute the appropriate platform-specific payload from the attacker's server:

`http://sfrclak[.]com:8000/6202033`

`![](https://threatbook.io/hs-fs/hubfs/download%20\(1\)-png.png?width=1914&height=415&name=download%20\(1\)-png.png)`

This cross-platform targeting — Windows, Linux, and macOS — makes this attack significantly broader in scope than typical supply chain incidents, which often focus on a single OS.

![](https://threatbook.io/hs-fs/hubfs/download%20\(2\)-png.png?width=1456&height=368&name=download%20\(2\)-png.png)

ThreatBook's Cloud Sandbox S and OneSandbox platforms have confirmed detection of this behavior. The downstream payload is no longer retrievable for analysis, as the delivery URL has been taken down.

### OneSEC EDR Detection

ThreatBook's OneSEC EDR detected the malicious code executing during OpenClaw installation on both Windows and macOS endpoints, providing real-time visibility into the attack at the point of execution.

## Remediation Steps

**1\. Check for network callbacks to`sfrclak.com`**

Any connection to `sfrclak.com` — inbound or outbound — confirms that the malicious loader executed on that host. Treat the host as compromised and escalate immediately.

**2\. Block malicious domains at the network layer**

  * `sfrclak.com`
  * `callnrwise.com`



**3\. Audit your Axios version**

Check whether your project uses `axios@1.14.1` or `axios@0.30.4`:

`bash`  
`npm list axios`

![](https://threatbook.io/hs-fs/hubfs/download%20\(3\)-png.png?width=1248&height=129&name=download%20\(3\)-png.png)

If either affected version is present, remove it and pin to `1.14.0` or an earlier known-good version.

**4\. Check for`plain-crypto-js` in `node_modules`**

The presence of the `plain-crypto-js` directory in `node_modules` is sufficient to confirm the `setup.js` loader executed — even if the directory contents appear clean. The stub files may have been replaced after execution.

![](https://threatbook.io/hs-fs/hubfs/download%20\(4\)-png.png?width=1251&height=87&name=download%20\(4\)-png.png)

![download \(5\)-png](https://threatbook.io/hs-fs/hubfs/download%20\(5\)-png.png?width=1251&height=417&name=download%20\(5\)-png.png)

**5\. Treat CI/CD pipelines as compromised**

Any pipeline that ran an install of `axios@1.14.1` or `axios@0.30.4` should be considered compromised. Rotate all secrets and tokens injected into those pipelines immediately.

**6\. Check for RAT artifacts on affected systems**

Audit running processes and persistence mechanisms on any host where the affected versions were installed. Engage your security team for a full forensic review.

## Detection Coverage

ThreatBook's **OneSEC** endpoint security platform detected malicious code execution during OpenClaw installation on Windows and macOS hosts in real time.

The following ThreatBook platforms also support detection and blocking of the IOCs listed below:

  * **Cloud Sandbox S**
  * **OneSandbox** (Sandbox Analysis Platform)



* * *

## IOCs

Indicator | Notes  
---|---  
`sfrclak.com` | C2 domain; RAT callback and payload delivery  
`callnrwise.com` | Associated attacker infrastructure  
`142.11.196.73` | Suspected attacker-controlled asset  
`142.11.199.73` | Suspected attacker-controlled asset  
`plain-crypto-js@4.2.1` | Malicious npm package (postinstall loader)  
`axios@1.14.1` | Backdoored Axios release  
`axios@0.30.4` | Backdoored Axios release  
  
_The IPs listed above were identified through ThreatBook Research Team's pivot analysis as "highly likely" attacker-controlled assets.__Organizations may wish to proactively block these at their discretion._

  *   * Share
  * 


[ ![Fastjson RCE \(≤1.2.83\): Active Exploitation Detected — Detection & Mitigation](https://threatbook.io/hubfs/featured-hubspot-1200x630.svg) ](https://threatbook.io/blog/fastjson-rce-1.2.83-active-exploitation-detected-detection-mitigation)

1 min read 

#### [Fastjson RCE (≤1.2.83): Active Exploitation Detected — Detection & Mitigation](https://threatbook.io/blog/fastjson-rce-1.2.83-active-exploitation-detected-detection-mitigation)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 22 July 2026, 12:07 PM

A remote code execution vulnerability in Fastjson affects every version up to and including 1.2.83. A remote attacker can run arbitrary code on a...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/fastjson-rce-1.2.83-active-exploitation-detected-detection-mitigation)

[ ![How a Malicious Plugin Turned OpenClaw Into a Credential Stealer](https://threatbook.io/hubfs/How%20a%20Malicious%20Plugin%20Turned%20OpenClaw%20Into%20a%20Credential%20Stealer.jpeg) ](https://threatbook.io/blog/how-a-malicious-plugin-turned-openclaw-into-a-credential-stealer)

1 min read 

#### [How a Malicious Plugin Turned OpenClaw Into a Credential Stealer](https://threatbook.io/blog/how-a-malicious-plugin-turned-openclaw-into-a-credential-stealer)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 18 March 2026, 08:03 AM

Last week, ThreatBook's endpoint detection product, OneSEC EDR, identified and fully captured an active attack targeting OpenClaw users. The attack...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/how-a-malicious-plugin-turned-openclaw-into-a-credential-stealer)

[ ![Hong Kong's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/hubfs/Blog%20Images/Hong%20Kong%20Cyber%20Threat%20Landscape%202025.png) ](https://threatbook.io/blog/hong-kongs-cyber-threat-landscape-inside-the-2025-data)

1 min read 

#### [Hong Kong's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/blog/hong-kongs-cyber-threat-landscape-inside-the-2025-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 16 March 2026, 12:03 AM

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/hong-kongs-cyber-threat-landscape-inside-the-2025-data)