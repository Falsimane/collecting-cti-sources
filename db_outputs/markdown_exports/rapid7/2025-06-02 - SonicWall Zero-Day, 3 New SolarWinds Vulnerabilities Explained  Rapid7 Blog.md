# SonicWall Zero-Day, 3 New SolarWinds Vulnerabilities Explained | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/02/03/sonicwall-snwlid-2021-0001-zero-day-and-solarwinds-2021-cve-trifecta-what-you-need-to-know/
- **Date :** 2025-06-02

---

Not content with the beating it laid down in January, 2021 continues to deliver with an unpatched zero-day exposure in some SonicWall appliances and three moderate-to-critical CVEs in SolarWinds software. We dig into the details below.

## Urgent mitigations required for SonicWall SMA 100 Series appliances

On Jan. 22, 2021, SonicWall published [an advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0001) and [in-product notification](https://www.sonicwall.com/support/product-notification/urgent-security-notice-sonicwall-confirms-sma-100-series-10-x-zero-day-vulnerability-feb-3-6-a-m-cst/210122173415410/) that they had identified a coordinated attack on their internal systems by highly sophisticated threat actors exploiting probable [zero-day vulnerabilities](/fundamentals/zero-day-attack/) on certain SonicWall secure remote access products.

Specifically, they identified Secure Mobile Access (SMA) version 10.x running on the following physical SMA 100 appliances running firmware version 10x, as well as the SMA 500v virtual appliance:

  * SMA 200
  * SMA 210
  * SMA 400
  * SMA 410



On Jan. 31, 2021, NCC Group Research & Technology [confirmed and demonstrated exploitability](https://twitter.com/NCCGroupInfosec/status/1355850304596680705?ref_src=twsrc%5Etfw) of a possible candidate for the vulnerability and detected indicators that attackers were exploiting this weakness.

On Feb. 3, 2021, SonicWall [released a patch](http://www.mysonicwall.com) to firmware version SMA 10.2.0.5-29sv, which all impacted organizations should apply immediately.

SonicWall has recommended removing all SMA 100 Series appliances for SMA 500v virtual appliances from the internet until a patch is available. If this is not possible, organizations are strongly encouraged to perform the following steps:

  * Enable multi-factor authentication. SonicWall has indicated this is a “critical” step until the patch is available.
  * Reset user password for all SMA 100 appliances.
  * Configure the [web application firewall on the SMA 100 series](https://www.sonicwall.com/support/knowledge-base/how-to-configure-web-application-firewall-waf-on-the-sma-100-series/210202202221923/), which has been updated with rules to detect exploitation attempts (SonicWall indicates that this is normally a subscription-based software, but they have automatically provided 60-day complementary licenses to organizations affected by this vulnerability).



If it’s not possible to perform these steps, SonicWall recommends that organizations downgrade their SMA 100 Series appliances to firmware version 9.x. They do note that this will remove all settings and that the devices will need to be reconfigured from scratch.

## Urgent patching required for SolarWinds Orion and Serv-U FTP products  


On Feb. 3, 2021, Trustwave published a [blog post](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/full-system-control-with-new-solarwinds-orion-based-and-serv-u-ftp-vulnerabilities/) providing details on two vulnerabilities in the SolarWinds Orion platform and a single vulnerability in the SolarWinds Serv-U FTP server for Windows.

The identified Orion platform weaknesses include:

  * CVE-2021-25274: Trustwave discovered that improper/malicious use of Microsoft Message Queue (MSMQ) could allow any remote, unprivileged attacker to execute arbitrary code in the highest privilege.
  * CVE-2021-25275: Trustwave discovered that credentials are stored insecurely, allowing any local user to take complete control over the SOLARWINDS_ORION database. This could lead to further information theft, and also enables attackers to add new admin-level users to all SolarWinds Orion platform products.



The identified SolarWinds Serv-U FTP server for Windows weakness enables any local user to create a file that can define a new Serv-U FTP admin account with full access to the C:\ drive, which will then give them **access or replace any directory or file on the server**.

Trustwave indicated they have private, proof-of-concept code that will be published on Feb. 9, 2021.

SolarWinds Orion Platform users can upgrade to version [2020.2.4](https://documentation.solarwinds.com/en/Success_Center/orionplatform/content/release_notes/orion_platform_2020-2-4_release_notes.htm). SolarWinds ServU-FTP users can upgrade to version [15.2.2 Hotfix 1](https://downloads.solarwinds.com/solarwinds/Release/HotFix/Serv-U-15.2.2-Hotfix-1.zip).

Rapid7 vulnerability researchers have identified that after the Orion Platform patch is applied, there is a digital signature validation step performed on arrived messages so that messages having no signature or not signed with a per-installation certificate are not further processed. On the other hand, the MSMQ is still unauthenticated and allows anyone to send messages to it.

## Rapid7 response

Rapid7 Labs is keeping a watchful eye on [Project Lorelei](/research/project-lorelei/) for indications of widespread inventory scans (attackers looking for potentially vulnerable systems) and will provide updates, as warranted, on any new developments.

[InsightVM](/products/insightvm/) and Nexpose customers can assess their exposure to these CVEs with remote vulnerability checks. 

  


## Article tags

  * [Emergent Threat Response](/blog/tag/emergent-threat-response/)
  * [Project Lorelei](/blog/tag/project-lorelei/)
  * [Zero-Day](/blog/tag/zero-day/)
  * [Research](/blog/tag/research/)