# Critical CVEs in Outdated Versions of Atlassian Confluence & VMware | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/01/19/etr-critical-cves-in-outdated-versions-of-atlassian-confluence-and-vmware-vcenter-server/
- **Date :** 2025-06-02

---

Rapid7 is highlighting two critical vulnerabilities in outdated versions of widely deployed software this week. Atlassian [disclosed](https://confluence.atlassian.com/security/cve-2023-22527-rce-remote-code-execution-vulnerability-in-confluence-data-center-and-confluence-server-1333990257.html) CVE-2023-22527, a template injection vulnerability in Confluence Server with a maxed-out CVSS score of 10, while VMware pushed a fresh update to its October 2023 vCenter Server [advisory](https://www.vmware.com/security/advisories/VMSA-2023-0023.html) on CVE-2023-34048 to note that the vulnerability has now been exploited in the wild. As of January 21, CVE-2023-22527 is also being exploited in the wild. 

VMware and Atlassian technologies are mainstays in many corporate environments, and they have [historically](/blog/post/2023/02/06/ransomware-campaign-compromising-vmware-esxi-servers/) [been](/blog/post/2023/11/06/etr-rapid7-observed-exploitation-of-atlassian-confluence-cve-2023-22518/) [targeted](/blog/post/2020/11/11/vmware-esxi-openslp-remote-code-execution-vulnerability-cve-2020-3992-and-cve-2019-5544-what-you-need-to-know/) [by](/blog/post/2022/06/02/active-exploitation-of-confluence-cve-2022-26134/) a wide range of adversaries, including in large-scale ransomware campaigns. Rapid7 urges customers to ensure that they are using **supported,** fixed versions of vCenter Server and Confluence Server in their environments, and that, wherever possible, they are adhering to a high-urgency patching schedule for these products. 

### VMware vCenter Server CVE-2023-34048

CVE-2023-34048 is a critical out-of-bounds write vulnerability that affects VMware vCenter Server and VMware Cloud Foundation. The vulnerability arises from an out-of-bounds write flaw in vCenter’s implementation of DCERPC, which, if exploited successfully, could lead to remote code execution. It was originally disclosed in October 2023 alongside fixed versions, including for several end-of-life products. Earlier this week, VMware updated their [advisory](https://www.vmware.com/security/advisories/VMSA-2023-0023.html) to note that exploitation of CVE-2023-34048 has been observed in the wild. Fixed versions of vCenter Server that remediate CVE-2023-34048 have been available since October 2023. 

Per VMware’s [advisory](https://www.vmware.com/security/advisories/VMSA-2023-0023.html), all versions of vCenter Server are vulnerable to CVE-2023-34048 **except** the following **fixed versions**(or later)**:**

  * [8.0U2](https://customerconnect.vmware.com/downloads/details?downloadGroup=VC80U2&productId=1345&rPId=110105)
  * [8.0U1d](https://customerconnect.vmware.com/downloads/details?downloadGroup=VC80U1D&productId=1345&rPId=112378)
  * [7.0U3o](https://customerconnect.vmware.com/downloads/details?downloadGroup=VC70U3O&productId=974&rPId=110262)



Customers should update on an emergency basis if they have not done so before now. Patches are also available for the following end-of-life versions of vCenter Server: [6.7U3](https://customerconnect.vmware.com/en/downloads/details?downloadGroup=VC67U3T&productId=742&rPId=112241), [6.5U3](https://customerconnect.vmware.com/en/downloads/details?downloadGroup=VC65U3V&productId=614&rPId=111937), and [VCF 3.x](https://kb.vmware.com/s/article/95194). VMware has information on applying individual product updates to Cloud Foundation environments [here](https://kb.vmware.com/s/article/88287). 

For more information, see VMware’s original [advisory](https://www.vmware.com/security/advisories/VMSA-2023-0023.html) and [FAQ](https://core.vmware.com/resource/vmsa-2023-0023-questions-answers). A list of vCenter Server versions and builds is [available here](https://kb.vmware.com/s/article/2143838). 

### Atlassian Confluence Server and Data Center CVE-2023-22527

CVE-2023-22527 is a critical template injection vulnerability in Atlassian Confluence that allows for unauthenticated remote code execution when exploited successfully in vulnerable target environments. As of January 22, [multiple](https://isc.sans.edu/diary/30576) [sources](https://x.com/TheDFIRReport/status/1749066611678466205?s=20) are reporting exploitation of this vulnerability. Rapid7 Labs has also observed attempted exploitation in both honeypot and production environments.

Affected versions from Atlassian’s [advisory](https://confluence.atlassian.com/security/cve-2023-22527-rce-remote-code-execution-vulnerability-in-confluence-data-center-and-confluence-server-1333990257.html): 

  * 8.0.x
  * 8.1.x
  * 8.2.x
  * 8.3.x
  * 8.4.x
  * 8.5.0-8.5.3



The **most recent supported versions** of Confluence Server (as of January 16, 2024) are not affected. Fixed versions for Confluence Server are 8.5.4 and 8.5.5, both of which are on long-term support. For Confluence Data Center, fixed versions are 8.6.0, 8.7.1, and 8.7.2, all of which apply to Confluence Data Center only. 

**We strongly recommend that Atlassian Confluence customers update to the latest version in their product’s version stream.** Customers should refer to the [vendor advisory](https://confluence.atlassian.com/security/cve-2023-22527-rce-remote-code-execution-vulnerability-in-confluence-data-center-and-confluence-server-1333990257.html) as the source of truth on affected products and fixed versions.

## Rapid7 customers

Vulnerability checks [for CVE-2023-34048](/db/vulnerabilities/vmsa-2023-0023-cve-2023-34048-vcenter/) have been available to InsightVM and Nexpose customers since October 27, 2023. Vulnerability checks [for CVE-2023-22527](/db/vulnerabilities/atlassian-confluence-cve-2023-22527/) have been available to InsightVM and Nexpose customers since January 17, 2024. 

A Velociraptor artifact to hunt for evidence of Confluence CVE-2023-22527 exploitation is [available here](https://docs.velociraptor.app/exchange/artifacts/pages/confluence_cve_2023_22527/). 

## Updates

**January 22, 2024:** As of January 22, [multiple](https://isc.sans.edu/diary/30576) [sources](https://x.com/TheDFIRReport/status/1749066611678466205?s=20) are reporting exploitation of Atlassian Confluence Server and Data Center CVE-2023-22527. 

**January 23, 2024:** Noted that Rapid7 Labs has observed attempted exploitation of Atlassian Confluence CVE-2023-22527 in both honeypot and production environments.

**January 26, 2024:** Added Velociraptor [artifact](https://docs.velociraptor.app/exchange/artifacts/pages/confluence_cve_2023_22527/) for detecting evidence of Confluence Server exploitation.

## Article tags

  * [Emergent Threat Response](/blog/tag/emergent-threat-response/)
  * [Research](/blog/tag/research/)