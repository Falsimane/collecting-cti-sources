# Rapid7 Analysis: Multiple vulnerabilities in Citrix XenMobile Server

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/ra-multiple-vulnerabilities-in-citrix-xenmobile-server-analysis/
- **Date :** 2026-06-16

---

## Description

Citrix published [a security bulletin](https://support.citrix.com/article/CTX277457) on Wednesday, August 12, citing five vulnerabilities in XenMobile Server, their Citrix Endpoint Management (CEM) on-premise instances. The CVEs assigned are CVE-2020-8208 through CVE-2020-8212. CVE-2020-8208 and CVE-2020-8209 are both critical. CVE-2020-8209 is a [path traversal vulnerability](https://www.ptsecurity.com/ww-en/about/news/citrix-fixes-xenmobile-vulnerability-found-by-positive-technologies/) in the XenMobile Server and stands out for its potential impact. Successful exploitation would allow unauthenticated attackers who follow a specially-crafted URL to read arbitrary files outside the web root directory, including configuration files and encryption keys.

CVSSv3 scores are unknown as of August 12, 2020, and no further details on the vulnerabilities were immediately available.

## Affected products

Products affected by critical vulnerabilities:

  * XenMobile Server 10.12 before RP2 ([rolling patch](https://support.citrix.com/article/CTX277473))
  * XenMobile Server 10.11 before RP4 ([rolling patch](https://support.citrix.com/article/CTX277698))
  * XenMobile Server 10.10 before RP6 ([rolling patch](https://support.citrix.com/article/CTX279101))
  * XenMobile Server before 10.9 RP5 ([rolling patch](https://support.citrix.com/article/CTX279098))



Versions affected by low- and medium-severity vulnerabilities:

  * XenMobile Server 10.12 before RP3
  * XenMobile Server 10.11 before RP6
  * XenMobile Server 10.10 before RP6
  * XenMobile Server before 10.9 RP5



Citrix has said that remediations have already been applied to cloud versions, but that users with on-premise versions will need to apply upgrades. The latest information on versions and patch availability can be found in [Citrix’s security bulletin here](https://support.citrix.com/article/CTX277457).

## Rapid7 analysis

Other critical Citrix vulnerabilities this year have seen quick and sustained exploitation—the company [noted in a blog](https://www.citrix.com/blogs/2020/08/11/citrix-provides-security-update-on-citrix-endpoint-management/) that “while there are no known exploits as of this writing, we do anticipate malicious actors will move quickly to exploit.” Rapid7 research teams have no reason to think otherwise, and the availability of patches will likely accelerate malicious actors’ ability to develop and refine successful attacks.

A note on CVE-2020-8209 specifically: In many cases, arbitrary file reads are exploitation primitives with limited utility unto themselves. In this case, however, successful exploitation of CVE-2020-8209 would allow attackers to read the target server’s configuration files, which may disclose domain and/or database credentials and other sensitive information with high utility for executing multi-stage attacks against a corporate environment. As far as primitives go, CVE-2020-8209’s value to both penetration testers and adversaries is high.

## Guidance

Citrix customers should apply the latest rolling patches for XenMobile versions affected by critical vulnerabilities as soon as possible. [Citrix has advised](https://www.citrix.com/blogs/2020/08/11/citrix-provides-security-update-on-citrix-endpoint-management/) that any XenMobile Server versions prior to 10.9.x must be upgraded to a supported version with the latest rolling patch; their recommendation is that customers should upgrade to 10.12 RP3, the latest supported version. There are no known workarounds or mitigations as of August 12, 2020.

## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)
  * [Rapid7 Analysis](/blog/tag/rapid7-analysis/)