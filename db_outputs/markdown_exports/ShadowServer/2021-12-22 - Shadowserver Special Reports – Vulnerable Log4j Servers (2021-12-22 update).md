# Shadowserver Special Reports – Vulnerable Log4j Servers (2021-12-22 update)

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/shadowserver-special-reports-vulnerable-log4j-servers-2021-12-22-update/
- **Date :** 2021-12-22

---

# Shadowserver Special Reports – Vulnerable Log4j Servers (2021-12-22 update)

December 22, 2021

We send out Special Reports whenever we are able to share one-time, high value datasets that we feel should be reported responsibly for maximum public benefit. Although the events included in these Special Reports fall outside of our [usual 24 hour daily reporting window](https://www.shadowserver.org/what-we-do/), we believe that there would still be significant benefit to our constituents in receiving and hopefully acting on the retrospective data.

In response to the major ongoing global security incident relating to [Apache Log4j 2](https://logging.apache.org/log4j/2.x/) that began on December 9th, we published a [one off Special Report on Vulnerable Log4j Servers](https://www.shadowserver.org/news/shadowserver-special-reports-vulnerable-log4j-servers/) on December 15th 2021. That Special Report provided National CSIRTs and network owners with information about Internet facing systems detected on their networks that were potentially vulnerable to [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228). We also blogged initial observations from our honeypot sensor network relating to [Log4j and attempted CVE-2021-44228 exploitation](https://www.shadowserver.org/news/log4j-scanning-and-cve-2021-44228-exploitation-latest-observations-2021-12-16/). We encourage you to read our previous posts for background, initial analysis and remediation information.

# CVE-2021-44228: Update 2021-12-22

During the week since our first Special Report, security vulnerabilities in Log4j have continued to [make headlines](https://www.washingtonpost.com/technology/2021/12/20/log4j-hack-vulnerability-java/) in the [mainstream media](https://edition.cnn.com/2021/12/15/tech/log4j-vulnerability/index.html) as well as in the cyber security industry. [Multiple Log4j 2 patches have been released](https://logging.apache.org/log4j/2.x/security.html) by the Apache Foundation to address the original CVE-2021-44228 vulnerability, as well as other subsequently discovered additional vulnerabilities [CVE-2021-45046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45046) (remote code execution – RCE) and [CVE-2021-45105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45105) (Denial of Service – DoS) too. Software product/platform/service [assessments](https://github.com/NCSC-NL/log4shell/tree/main/software) and code reviews have discovered [many impacted software packages](https://therecord.media/google-more-than-35000-java-packages-impacted-by-log4j-vulnerabilities/), requiring large scale remediation activities world-wide. Internet-wide mass scanning and exploitation of the vulnerabilities on exposed systems has continued, including by [alleged nation state actors](https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/#nation-state) and [ransomware operators](https://www.zdnet.com/article/conti-ransomware-attacking-vmware-vcenter-servers-through-log4j-vulnerability/). The US Cybersecurity and Infrastructure Security Agency (CISA) has [ordered](https://www.zdnet.com/article/cisa-orders-federal-civilian-agencies-to-patch-log4j-vulnerability-by-december-24/) all civilian Federal agencies to patch the critical Log4j vulnerability by December 24 and system defenders are still racing to patch the vulnerability in the run up to Christmas.

At the time of writing (December 22nd 2021 22:00 UTC) we have seen **174,068** scan/exploit events from **2,344** unique IP addresses across **433** ports. That compares with **38,638** scan/exploit events from **1,939** unique IP addresses across **272** ports at the time of our initial report (December 14th 2021 23:00 UTC). Scan/exploit events rates detected by our global honeypot sensor network peaked on December 20th and have since fallen slightly:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypots-1024x283.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypots.png)

The top source countries observed in our original report (December 14th 2021 23:00 UTC) were:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Countries-1024x402.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Countries.png)

Compared with the current top source countries at the time of writing (December 22nd 2021 22:00 UTC):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypot_Countries-1024x376.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypot_Countries.png)

Combined for comparison:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Countries_Compared-1024x469.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Countries_Compared.png)

There has been a significant shift in the distribution of top CVE-2021-44228 scan/exploiter locations, which is more marked at the Autonomous System Number (ASN) level.

The top source ASNs observed in our original report (December 14th 2021 23:00 UTC) were:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Networks-1024x386.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Networks.png)

Compared with the current top source ASNs at the time of writing (December 22nd 2021 22:00 UTC):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypot_ASNs-1024x376.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypot_ASNs.png)

Selectel in Russia has now become the top CVE-2021-44228 scan/exploit source observed by our honeypots.

The top TCP ports where CVE-2021-44228 scan/exploit attempts were observed by our honeypots to date were:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypot_Ports-1024x379.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Honeypot_Ports.png)

As per our[![](https://www.shadowserver.org/wp-content/uploads/2021/12/AlphaStrike_Logo_original-300x88.jpg)](/wp-content/uploads/2021/12/AlphaStrike_Logo_original.jpg) previous Special Report and own policies, Shadowserver are not ourselves scanning IPv4 /0 for exposed Log4j vulnerabilities. But [**Alpha Strike Labs**](https://www.alphastrike.io), who kindly provided scan data used in our original Special Report, have completed a second major scan and have once again kindly offered to share their scan data with us in order to help more National CSIRTs and network owners be quickly notified about potentially vulnerable Log4j systems. This scan data was included in a second run of our Special Report that was sent to Shadowserver’s 132 National CSIRTs in 173 countries and territories and over 6000 network owners worldwide overnight on December 22nd. You can find more detail on the report format [here](https://www.shadowserver.org/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/). We would like to thank **Alpha Strike Labs** for once again sharing their data and helping the Internet community respond to this serious ongoing cyber security threat.

**CVE-2021-44228 Data Analysis**

The data provided for this second Special Report was collected by Alpha Strike Labs between December 16th and 22nd 2021. Their scan once again generated an outbound DNS response from vulnerable systems through the JNDI interface. The latest Special Report includes **10951** identified vulnerable Log4j instances on **8472** unique Internet facing IP addresses across **1500** ASNs in **116** countries (it is possible for an IP address to have an exposed log4j instance on more than one listening port). That compares to **13294** identified vulnerable Log4j instances on **13294** unique Internet facing IP addresses across **1602** ASNs in **109** countries in the original scan.

The ports and instance counts included in the second scan data set were:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_Ports.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_Ports.png)

The top HTTP headers that returned a response when queried were:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_HTTP_Header_Responses.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_HTTP_Header_Responses.png)

The IP-geolocated distribution of CVE-2021-44228 vulnerable IP addresses still features an unusual mix of countries, potentially showing how widely log4j is used internationally. The rate of remediation between individual countries is visibly different after one week.

Global distribution of vulnerable IP addresses per country in our original report (December 15th):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Worldmap-1024x659.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Worldmap.png)

Global distribution of vulnerable IP addresses per country at the time of writing (December 22nd):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_log4j_Special2_Global-1024x574.png)](/wp-content/uploads/2021/12/2021-12-22_log4j_Special2_Global.png)

Distribution of vulnerable IP addresses per US county in our original report (December 15th):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_USA_Counties-1024x563.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_USA_Counties.png)

Distribution of vulnerable IP addresses per US county at the time of writing (December 22nd):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_US_Counties-1024x551.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_US_Counties.png)

Global distribution of vulnerable IP addresses per country in our original report (December 15th):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Treemap-1024x477.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Treemap.png)

Global distribution of vulnerable IP addresses per country at the time of writing (December 22nd):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_Treemap-1024x465.png)](/wp-content/uploads/2021/12/2021-12-22_CVE-2021-44228_Scan_Treemap.png)

Global distribution of vulnerable IP addresses per country in our original report (December 14th):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Bubblemap-1024x813.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Bubblemap.png)

Global distribution of vulnerable IP addresses per country at the time of writing (December 22nd):

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-22_log4j_Special_Global_Bubble-1024x548.png)](/wp-content/uploads/2021/12/2021-12-22_log4j_Special_Global_Bubble.png)

Although starting from a higher number of exposed vulnerable Log4j servers, remediation efforts in countries such as the US, Ireland and Germany have reduced the number of vulnerable systems significantly, whereas Iran show only limited change in the number of systems detected by scanning. The number of detected systems in China, South Korea, Russia and Hong Kong has increased (although note that this could be due to more effective and complete scanning for the vulnerability).

For a more detailed IP-geolocated view of where detected vulnerable Log4j servers are located, click the small maps for high resolution world and regional images below.

Distribution of vulnerable IP addresses in our original report (December 15th) – Worldwide:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_world_bmng_200407-test1-2px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_world_bmng_200407-test1-2px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – Worldwide:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_world_bmng_200407-test1-2px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_world_bmng_200407-test1-2px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – US:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_us_bmng_200407-test1-8px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_us_bmng_200407-test1-8px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – US:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_us_bmng_200407-test1-8px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_us_bmng_200407-test1-8px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – North America:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_na_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_na_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – North America:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_na_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_na_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th 2021 23:00 UTC) – Central America:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_ca_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_ca_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd 2021 22:00 UTC) – Central America:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_ca_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_ca_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – South America:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_sa_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_sa_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – South America:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_sa_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_sa_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – Europe:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_eu_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_eu_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – Europe:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_eu_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_eu_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – Middle East:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_me_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_me_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – Middle East:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_me_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_me_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – Africa:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_af_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_af_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – Africa:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_af_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_af_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – China:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_cn_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_cn_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – China:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_cn_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_cn_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses in our original report (December 15th) – Oceania:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_oc_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211215-20211215-winkel_tripel_oc_bmng_200407-test1-6px.jpg)

Distribution of vulnerable IP addresses at the time of writing (December 22nd) – Oceania:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_oc_bmng_200407-test1-6px-300x183.jpg)](/wp-content/uploads/2021/12/Log4jLog4j_Vulnerable_Servers_CVE202144228-20211222-20211222-winkel_tripel_oc_bmng_200407-test1-6px.jpg)

**Log4j Remediation**

Technical details about the various vulnerabilities in log4j 2 and good remediation advice has been provided by a number of trusted sources:

<https://logging.apache.org/log4j/2.x/>

<https://www.ncsc.gov.uk/news/apache-log4j-vulnerability>

<https://us-cert.cisa.gov/apache-log4j-vulnerability-guidance>

<https://www.cisa.gov/uscert/ncas/alerts/aa21-356a>

<https://www.govcert.ch/blog/zero-day-exploit-targeting-popular-java-library-log4j/>

Apache Mitigations are available for version 2.10 and higher. Patches and mitigations and patches should be applied to all internet and internally facing log4j systems **immediately** since this vulnerability represents the maximum risk/impact possible and is being actively exploited at scale now.

Direct link to the Special Report format is [here](https://www.shadowserver.org/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/).

If you missed this [Special Report](https://www.shadowserver.org/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/) because you were not yet a subscriber to our [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/), do not worry: simply [subscribe for your network or country now](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) and specifically request all recent Shadowserver Special Reports. We will resend the [Special Report](https://www.shadowserver.org/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/) specifically for your network or country (for National CERT/CSIRTs).

NB: We only send relevant reports for YOUR network/IP addresses – you will not get notifications for networks that you fail to request reports on, or that are not rightfully your responsibility.

If you have a data set which you feel could also be of benefit to National CERT/CSIRTs and network owners world-wide to help protect victims of cybercrime, please [get in touch](https://www.shadowserver.org/contact/) and discuss the options for using Shadowserver’s proven reporting systems for distribution and remediation.

  * [Honeypots](/topics/honeypots/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Threat Intelligence](/topics/threat-intelligence/)



[« Back to News & Insights](/news-insights/)

### Recent Articles

  * #### [Shadowserver 2025: Highlights of the Year in Review](/news/shadowserver-2025-highlights-of-the-year-in-review/)

September 7, 2026

A review of Shadowserver’s 21st year as the world’s largest provider of free, timely, actionable, daily cyber threat… [Read more »](/news/shadowserver-2025-highlights-of-the-year-in-review/)

  * #### [Shadowserver Critical Community Infrastructure Cyber Resilience Project](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

August 5, 2026

The Shadowserver Critical Community Infrastructure (CCI) Project is designed to improve the cybersecurity posture of essential… [Read more »](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

  * #### [StealC Historical Bot Infection Special Report](/news/stealc-historical-bot-infection-special-report/)

June 25, 2026

On Wednesday 24th June 2026, international law enforcement partners announced additional successful cyber crime disruption… [Read more »](/news/stealc-historical-bot-infection-special-report/)

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)