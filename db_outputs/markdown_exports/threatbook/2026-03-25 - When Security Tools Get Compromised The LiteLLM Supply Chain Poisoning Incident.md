# When Security Tools Get Compromised: The LiteLLM Supply Chain Poisoning Incident

- **Source :** threatbook
- **URL :** https://threatbook.io/blog/when-security-tools-get-compromised-the-litellm-supply-chain-poisoning-incident
- **Date :** 2026-03-25

---

3 min read 

# When Security Tools Get Compromised: The LiteLLM Supply Chain Poisoning Incident

[ ![Picture of ThreatBook Research Team](https://threatbook.io/hubfs/Brand%20Resources/favicon-192x192.png) ThreatBook Research Team ](https://threatbook.io/blog/author/threatbook-research-team) :  Updated on March 25, 2026 

[Threat Research](https://threatbook.io/blog/tag/threat-research)

**Table of Contents**

Incident Summary

Attack Timeline (UTC)

Supply Chain Analysis

Version 1.82.7

Version 1.82.8

Malicious Code Behavior

Remediation Steps

Detection Coverage

IOCs

On March 24, 2026, ThreatBook Research Team detected a large-scale supply chain attack targeting LiteLLM — a core component widely used across the AI ecosystem.

Two versions of the package (1.82.7 and 1.82.8) published to PyPI were found to contain attacker-implanted backdoors. Although the malicious versions were removed within 46 minutes, LiteLLM's download volume of over 3 million per day and nearly 100 million per month means the blast radius across downstream AI projects is substantial. The threat actor, TeamPCP, has publicly claimed to have exfiltrated data from hundreds of thousands of devices.

* * *

## Incident Summary

Field | Details  
---|---  
**Incident** | LiteLLM supply chain poisoning — credential and sensitive data theft  
**Affected Package** | LiteLLM (approx. 97 million monthly downloads)  
**Affected Versions** | 1.82.7 and 1.82.8 (removed); safe version is 1.82.6  
**Discovery Window** | March 24, 2026, 10:39–11:25 UTC (46 minutes)  
**Threat Actor** | TeamPCP  
**Root Cause** | LiteLLM's CI/CD pipeline used a compromised version of the Trivy security scanner, leading to the exposure of PyPI publishing credentials  
**Impact** | Theft of SSH keys, cloud credentials (AWS/GCP/Azure), Kubernetes secrets, CI/CD tokens, crypto wallets, and more  
  
* * *

## Attack Timeline (UTC)

  * **Late February** — Attackers compromise Trivy, a widely-used open-source vulnerability scanning tool, planting malicious code within it.
  * **Early-to-Mid March** — LiteLLM's CI/CD pipeline runs the compromised version of Trivy. PyPI publishing credentials are silently stolen.
  * **March 24, 10:39** — Attackers use the stolen credentials to upload two backdoored LiteLLM releases (1.82.7 and 1.82.8) to PyPI.
  * **March 24, 11:25** — Both malicious versions are removed from PyPI. Total exposure window: 46 minutes.



**Key finding: Malicious code targets Linux environments only. Windows and macOS systems are effectively unaffected.**

**![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-33-22-9301-AM.png?width=616&height=51&name=undefined-Mar-25-2026-07-33-22-9301-AM.png) **

* * *

## Supply Chain Analysis

![](https://threatbook.io/hs-fs/hubfs/undefined-1.png?width=649&height=123&name=undefined-1.png)

### Version 1.82.7

In version 1.82.7, attackers injected a base64-encoded malicious payload into `proxy/proxy_server.py`. The backdoor executes automatically upon importing LiteLLM's proxy library.

Three variants of the malicious code were found within `proxy_server.py` — two commented out, one active. Analysis confirms all three variants are functionally identical in terms of data exfiltration targets and C2 communication; the only differences are in encryption method.

![](https://threatbook.io/hs-fs/hubfs/undefined-2.png?width=650&height=117&name=undefined-2.png)

### Version 1.82.8

Version 1.82.8 escalates the attack. In addition to the injection in `proxy_server.py`, attackers introduced a malicious `litellm_init.pth` file. This exploits Python's `.pth` file mechanism, which executes code automatically at Python runtime — enabling silent, stealthy execution independent of whether the proxy module is ever imported.

![](https://threatbook.io/hs-fs/hubfs/undefined-3.png?width=649&height=306&name=undefined-3.png)

Code comparison confirms the payload in `litellm_init.pth` is identical to the uncommented payload in `proxy_server.py`. Our analysis focuses on the `.pth` variant as the primary execution vector.

![](https://threatbook.io/hs-fs/hubfs/undefined-4.png?width=649&height=200&name=undefined-4.png)

* * *

## Malicious Code Behavior

The backdoor follows a three-stage execution flow:

**Stage 1 — Data exfiltration.** The payload harvests a wide range of sensitive data from the compromised host:

  * System information and environment variables (`printenv`)  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-35-16-9111-AM.png?width=650&height=141&name=undefined-Mar-25-2026-07-35-16-9111-AM.png)
  * SSH keys and Git credentials  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-33-45-3938-AM.png?width=650&height=141&name=undefined-Mar-25-2026-07-33-45-3938-AM.png)
  * AWS, GCP, and Azure credentials  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-33-56-0891-AM.png?width=650&height=435&name=undefined-Mar-25-2026-07-33-56-0891-AM.png)
  * Kubernetes secrets
  * Docker configuration  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-34-01-5736-AM.png?width=650&height=482&name=undefined-Mar-25-2026-07-34-01-5736-AM.png)
  * Package manager configurations
  * WireGuard keys
  * CI/CD secrets and webhook tokens  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-34-10-5899-AM.png?width=649&height=308&name=undefined-Mar-25-2026-07-34-10-5899-AM.png)
  * Database credentials  
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-34-18-2653-AM.png?width=650&height=326&name=undefined-Mar-25-2026-07-34-18-2653-AM.png)
  * Shell history
  * Cryptocurrency wallets 



**Stage 2 — Persistence.** The malware downloads a persistence script to the host. It is saved as `sysmon.py` and installs a `sysmon.service` systemd unit to ensure the script runs persistently across reboots. The script is stored at `/host/root/.config/sysmon/sysmon.py`. 

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-34-21-6409-AM.png?width=649&height=175&name=undefined-Mar-25-2026-07-34-21-6409-AM.png)

The second-stage payload is fetched via [`checkmarx.zone/raw`](https://i.threatbook.io/research/checkmarx.zone). At the time of analysis, this URL had been redirected to a benign site by the attacker — a common tactic to hamper forensic investigation.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-31-30-1388-AM.png?width=649&height=456&name=undefined-Mar-25-2026-07-31-30-1388-AM.png)

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-31-20-7413-AM.png?width=650&height=542&name=undefined-Mar-25-2026-07-31-20-7413-AM.png)   
![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-30-54-4463-AM.png?width=1080&height=289&name=undefined-Mar-25-2026-07-30-54-4463-AM.png)

**Stage 3 — Exfiltration.** Collected data is written to a temporary file, encrypted, and packaged into `tpcp.tar.gz`. This archive is uploaded to `models.litellm.cloud` — a lookalike domain deliberately registered to mimic the legitimate `litellm.ai`. The use of a typosquatted domain is a deliberate obfuscation technique to avoid triggering network anomaly detection.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-30-44-3767-AM.png?width=650&height=229&name=undefined-Mar-25-2026-07-30-44-3767-AM.png)

**Encryption note:** Across all three code variants, the same RSA public key is used to encrypt exfiltrated data — confirming they share common infrastructure. Two of the variants use RC4 symmetric encryption to obfuscate the execution script, with a hardcoded key. The choice of key reflects explicit ideological content consistent with racist intent on the part of the attacker.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-30-34-7226-AM.png?width=545&height=278&name=undefined-Mar-25-2026-07-30-34-7226-AM.png)

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-30-03-0116-AM.png?width=650&height=281&name=undefined-Mar-25-2026-07-30-03-0116-AM.png)

* * *

## Remediation Steps

**1\. Check for affected versions**

On Linux hosts, run:

`bash`

`pip show litellm`

If the output shows version `1.82.7` or `1.82.8`, immediately stop all services using LiteLLM, uninstall the package, and isolate the affected host from the network.

**2\. Block malicious domains at the network layer**

Add the following domains to your deny list:

  * [`models.litellm.cloud`](https://i.threatbook.io/research/models.litellm.cloud)  
**![image-png-1](https://threatbook.io/hs-fs/hubfs/image-png-1.png?width=2452&height=1358&name=image-png-1.png)**
  * [`checkmarx.zone`](https://i.threatbook.io/research/checkmarx.zone)  
![](https://threatbook.io/hs-fs/hubfs/image-png.png?width=2450&height=1342&name=image-png.png)



**3\. Check for malicious artifacts on disk**

Look for and remove the following if present:

  * `/tmp/pglog`
  * `/tmp/.pg_state`
  * `/host/root/.config/sysmon/sysmon.py`
  * `tpcp.tar.gz` (any location)
  * Any `.pth` file in Python library paths with a SHA256 matching the IOC below



Also audit for any newly created `sysmon.service` systemd unit unrelated to legitimate monitoring infrastructure.

**4\. Rotate all credentials on affected hosts**

Given the breadth of data targeted — SSH keys, cloud credentials, CI/CD tokens, database passwords, crypto wallets — a full credential rotation is strongly recommended for any host where affected LiteLLM versions were installed. Engage your security team to assess the full scope of potential exposure.

* * *

## Detection Coverage

ThreatBook's endpoint security platform **OneSEC** provides precise detection for the malicious code behaviors described in this report. Users are advised to monitor endpoint logs for data exfiltration events and unauthorized access to sensitive files.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-25-2026-07-29-21-0630-AM.png?width=1080&height=282&name=undefined-Mar-25-2026-07-29-21-0630-AM.png)

Additionally, the following ThreatBook platforms all support detection and blocking of the IOCs listed below:

  * **TDP** (Threat Detection Platform)
  * **OneSIG** (Threat Defense System)
  * **OneDNS** (Internet Security Access Platform)
  * **Cloud Sandbox S**
  * **OneSandbox** (Sandbox Analysis Platform)



* * *

## IOCs

Indicator | Type  
---|---  
`d2a0d5f564628773b6af7b9c11f6b86531a875bd2d186d7081ab62748a800ebb` | litellm-1.82.8.whl  
`71e35aef03099cd1f2d6446734273025a163597de93912df321ef118bf135238` | litellm_init.pth  
`a0d229be8efcb2f9135e2ad55ba275b76ddcfeb55fa4370e0a522a5bdee0120b` | proxy_server.py  
`8395c3268d5c5dbae1c7c6d4bb3c318c752ba4608cfcd90eb97ffb94a910eac2` | litellm-1.82.7.whl  
`models.litellm.cloud` | Sensitive data exfiltration endpoint  
`checkmarx.zone` | Persistence script download source  
  
* * *

_ThreatBook Research Team monitors active threats in real time. For questions about this report or ThreatBook's detection capabilities, contact your regional ThreatBook representative._

  *   * Share
  * 


[ ![Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/hubfs/Blog%20Images/Singapore%20Cyber%20Threat%20Landscape%202025.png) ](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

1 min read 

#### [Singapore's Cyber Threat Landscape: Inside the 2025 Data](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 16 March 2026, 12:03 AM

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/singapores-cyber-threat-landscape-inside-the-2025-data)

[ ![APAC's Cyber Threat Landscape: Inside the 2026 Mid-Year Data](https://threatbook.io/hubfs/blog-header-1600x840.png) ](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

1 min read 

#### [APAC's Cyber Threat Landscape: Inside the 2026 Mid-Year Data](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 21 July 2026, 07:07 AM

ThreatBook Labs recorded 15,205 security incidents across Asia-Pacific between June 2025 and June 2026. Read one at a time, they look like an...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

[ ![Lazarus Group Poisons Axios: Inside the npm Supply Chain Attack](https://threatbook.io/hubfs/Inside%20the%20npm%20Supply%20Chain%20Attack.png) ](https://threatbook.io/blog/lazarus-group-poisons-axios-inside-the-npm-supply-chain-attack)

1 min read 

#### [Lazarus Group Poisons Axios: Inside the npm Supply Chain Attack](https://threatbook.io/blog/lazarus-group-poisons-axios-inside-the-npm-supply-chain-attack)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 1 April 2026, 12:04 AM

Regarding yesterday's Axios npm supply chain poisoning incident, ThreatBook has conducted in-depth sample analysis and attack tracing. Drawing on...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/lazarus-group-poisons-axios-inside-the-npm-supply-chain-attack)