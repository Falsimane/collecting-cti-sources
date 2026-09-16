# Multiple Vulnerabilities in Wowza Streaming Engine (Fixed) | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/11/20/multiple-vulnerabilities-in-wowza-streaming-engine-fixed/
- **Date :** 2025-06-02

---

Wowza Streaming Engine below v4.9.1 is vulnerable to multiple vulnerabilities on Linux and Windows. An unauthenticated attacker can poison the Wowza Streaming Engine Manager web dashboard with a stored cross-site scripting (“XSS”) payload. When an administrator views the poisoned dashboard, additional authenticated vulnerabilities will automatically be exploited for remote code execution on the underlying server. The code execution context is privileged: root on Linux, LocalSystem on Windows. These vulnerabilities are tracked as CVE-2024-52052, CVE-2024-52053, CVE-2024-52054, CVE-2024-52055, and CVE-2024-52056. All five were patched on November 20, 2024, with the release of Wowza Streaming Engine v4.9.1.

## Product description

[Wowza Streaming Engine](https://www.wowza.com/streaming-engine) is [media server software](https://www.wowza.com/docs/understanding-wowza-streaming-engine) used by many organizations for livestream broadcasts, video on-demand, closed captioning, and media system interoperability. The Wowza Streaming Engine Manager component is a web application, and it’s [used to](https://www.wowza.com/docs/how-to-find-your-way-around-wowza-streaming-engine-manager) manage and monitor Wowza Media Server instances. At the time of publication, approximately 18,500 Wowza Streaming Engine servers are exposed to the public internet, and many of those systems also expose the Manager web application.

## Credit

These issues were reported to the Wowza Media Systems team by Ryan Emmons, Lead Security Researcher at Rapid7. The vulnerabilities are being disclosed in accordance with [Rapid7's vulnerability disclosure policy](/security/disclosure/). Rapid7 is grateful to the Wowza team for their assistance and collaboration.

## Vulnerability details

The testing target was Wowza Streaming Engine v4.8.27+5, the latest version available at the time of research. Rapid7 identified multiple security vulnerabilities as part of this research project, and those vulnerabilities are outlined in the table below.

CVE| Description| CVSS  
---|---|---  
CVE-2024-52052| An authenticated administrator can define a custom application property and poison a stream target for high-privilege remote code execution.| [9.4](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H)  
CVE-2024-52053| An unauthenticated attacker can inject client-side JavaScript into the administrator dashboard to automatically hijack admin accounts.| [8.7](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)  
CVE-2024-52054| An injection permits an administrator user to create an XML file anywhere on the file system.| [5.1](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N)  
CVE-2024-52055| An injection permits an administrator user to read any file on the file system if the target directory contains an XML file.| [8.2](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:N/VA:N/SC:H/SI:N/SA:N)  
CVE-2024-52056| An injection permits an administrator user to delete any directory on the host system if the target directory contains an XML file.| [6.9](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:L)  
  
Exploitation was tested against Wowza Streaming Engine on two different operating systems: Ubuntu Linux 22.04.1 and Windows Server 2022. Based on information provided by the vendor, the unauthenticated injection vulnerability affects all Wowza Streaming Engine Manager versions, while the four authenticated vulnerabilities were introduced in v4.3.0.

## Vendor statement

“We at Wowza Media Systems are focused on security excellence, and by partnering with trusted researchers like Rapid7, we proactively respond to and fix vulnerabilities to safeguard our customers' interests.”

## Mitigation guidance

Per to the vendor, issues in this disclosure can be remediated by upgrading to Wowza Streaming Engine [version 4.9.1](https://www.wowza.com/docs/wowza-streaming-engine-4-9-1-release-notes) or any future version.

## Rapid7 customers

InsightVM and Nexpose customers can assess their exposure to CVE-2024-52052, CVE-2024-52053, CVE-2024-52054, CVE-2024-52055, and CVE-2024-52056 with authenticated vulnerability checks available as of the November 20, 2024 content release.

## Disclosure timeline

**July 30, 2024 - September 3, 2024:** Rapid7 attempts to contact the vendor to disclose vulnerabilities discovered in Wowza Streaming Engine.  
**September 3, 2024:** Rapid7 makes contact with the vendor, who acknowledges disclosure materials.  
**September 5, 2024 - September 18, 2024:** Rapid7 and vendor discuss coordinated vulnerability disclosure steps and timeline.  
**October 2, 2024:** Vendor communicates Q4 remediation timeline.  
**October 31, 2024:** Patch shared with Rapid7 for testing.  
**November 4, 2024:** Rapid7 confirms the patch is successful.  
**November 5, 2024:** Rapid7 provides CVE IDs.  
**November 15, 2024:** Vendor proposes Wednesday, November 20 for coordinated vulnerability disclosure. Rapid7 agrees.  
**November 20, 2024:** This disclosure.

## Article tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Vulnerability Management](/blog/tag/vulnerability-management/)
  * [Research](/blog/tag/research/)