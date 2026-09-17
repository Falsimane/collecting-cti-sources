# Shadowserver Special Reports – Vulnerable Log4j Servers

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/shadowserver-special-reports-vulnerable-log4j-servers/
- **Date :** 2021-12-15

---

# Shadowserver Special Reports – Vulnerable Log4j Servers

December 15, 2021

We send out Special Reports whenever we are able to share one-time, high value datasets that we feel should be reported responsibly for maximum public benefit. Although the events included in these Special Reports fall outside of our [usual 24 hour daily reporting window](https://www.shadowserver.org/what-we-do/), we believe that there would still be significant benefit to our constituents in receiving and hopefully acting on the retrospective data.

[Log4j 2](https://logging.apache.org/log4j/2.x/) is an open-source Java logging library developed by the [Apache Foundation](https://www.apache.org) which is widely used in many applications. It is frequently included as a default log handler in enterprise Java applications and is commonly included as a dependency component in other Java projects (including in over [470,000 other open source projects](https://github.com/apache/log4j/network/dependents)). Log4j 2 is also used in many Software-as-a-Service (S-a-a-S) and cloud services. Applications using log4j 2 may be Internet facing or found within internal networks.

**On December 9th 2021** , a vulnerability in Apache Log4j versions 2.0-beta9 to 2.14.1 with the **maximum** Common Vulnerability Scoring System ([CVSS](https://www.first.org/cvss/)) score of **10.0** out of a possible **10.0** was made public as Common Vulnerability Exposure ([CVE](https://cve.mitre.org)) number [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228). Remote exploitation is unusually simple, easy for attackers to deliver to target systems, can be used pre-authentication/anonymously and can result in remote code execution (RCE) in vulnerable systems – which could allow an attacker to gain full control of them. A simple input string merely needs to be introduced into the application logs and be processed to result in RCE, hence the vulnerability being named “**Log4Shell** ”. Given the large number of platforms and systems potentially impacted worldwide, the [potential attack surface](https://github.com/NCSC-NL/log4shell/tree/main/software) may be very high.

Shadowserver quickly updated our [global honeypot sensor network](https://www.shadowserver.org/news/beyond-the-sissden-event-horizon/) over the weekend to support rapid detection of CVE-2021-44228 on arbitrary ports and we have [tweeted observations](https://twitter.com/Shadowserver), as well as including the observed scanning IP addresses in our [Honeypot HTTP Scanner Events Report.](https://twitter.com/Shadowserver/status/1470305480962678784) We also added a [new report type for malware URLs](https://twitter.com/Shadowserver/status/1470695172359045120) that includes the log4j exploit payload URLs that we are seeing being dropped. Similarly to what we saw with the [Microsoft Exchange 0day in March](https://www.shadowserver.org/news/shadowserver-special-report-exchange-scanning-5/), early adopters included attackers dropping cryptocurrency miners such as Kinsing or Mirai style malware. Given the ease of scanning and exploitation, we expect many more threat actors to rapidly adopt this too.

In a similar situation to the [Heartbleed](https://heartbleed.com) and [Shellshock](https://en.wikipedia.org/wiki/Shellshock_\(software_bug\)) vulnerabilities, scanning for vulnerable log4j systems requires the scanner to cause the target system to execute commands or otherwise beacon out to be detected. Shadowserver continued with our [usual policy](https://twitter.com/Shadowserver/status/1470459893245165581) of not scanning the entire IPv4 space for these type of vulnerabilities. That means we have not been including CVE-2021-44228 / log4j / log4shell data in our [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/).

From our honeypot data, it is clear that other organizations are actively scanning the entire Internet for vulnerable log4j instances. At the time of writing (December 14th 2021 23:00 UTC) we have seen **38,638** scan/exploit events from **1,939** unique IP addresses across **272** ports. The top source countries observed so far were:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Countries-1024x402.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Countries.png)

and the top Autonomous System Numbers ([ASNs](https://en.wikipedia.org/wiki/Autonomous_system_\(Internet\))) so far were:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Networks-1024x386.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Honeypot_Networks.png)

In [response](https://twitter.com/AlphaStrikeLabs/status/1470477574073630720) to one of our tweets, [Alpha Strike Labs](https://www.alphastrike.io) have kindly offered to share their CVE-2021-44228 scan data with us in order to help more National CSIRTs and network owners be quickly notified about potentially vulnerable log4j systems. Their data is being included in a new Special Report that was sent to Shadowserver’s 132 National CSIRTs in 173 countries and territories and over 6000 network owners worldwide overnight on December 14th. You can find more detail on the report format [here](/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/). We would like to thank **Alpha Strike Labs** for sharing their data and helping the Internet community respond to this serious cyber security incident.

**CVE-2021-44228 Data Analysis**

The data provided for this Special Report was collected by Alpha Strike Labs between December 11-13th 2021, using a seed list of ~300 million already known responding IP addresses across 16 common ports. Their scan generated an outbound DNS response from vulnerable systems through the JNDI interface. The Special Report includes **13,294** identified vulnerable Internet facing unique IP addresses across **1602** ASNs in **109** countries. The IP-geolocated distribution of CVE-2021-44228 vulnerable IP addresses features an unusual mix of countries, potentially showing how widely log4j is used internationally.

Global distribution of vulnerable IP addresses per country:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Worldmap-1024x659.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Worldmap.png)

Distribution of vulnerable IP addresses per US county:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_USA_Counties-1024x563.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_USA_Counties.png)

Global distribution of vulnerable IP addresses per country:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Treemap-1024x477.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Treemap.png)

Global distribution of vulnerable IP addresses per country:

[![](https://www.shadowserver.org/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Bubblemap-1024x813.png)](/wp-content/uploads/2021/12/2021-12-14_CVE-2021-44228_Bubblemap.png)

**Log4j CVE-2021-44228 Remediation**

Technical details about the CVE-2021-44228 vulnerability in log4j works and good remediation advice has been provided by a number of trusted sources:

<https://logging.apache.org/log4j/2.x/>

<https://www.ncsc.gov.uk/news/apache-log4j-vulnerability>

<https://us-cert.cisa.gov/apache-log4j-vulnerability-guidance>

<https://www.govcert.ch/blog/zero-day-exploit-targeting-popular-java-library-log4j/>

Apache Mitigations are available for version 2.10 and higher. Patches and mitigations and patches should be applied to all internet and internally facing log4j systems **immediately** since this vulnerability represents the maximum risk/impact possible and is being actively exploited at scale now.

Direct link to the Special Report format is [here](/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/).

If you missed this [Special Report](/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/) because you were not yet a subscriber to our [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/), do not worry: simply [subscribe for your network or country now](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) and specifically request all recent Shadowserver Special Reports. We will resend the [Special Report](/what-we-do/network-reporting/vulnerable-log4j-servers-special-report/) specifically for your network or country (for National CERT/CSIRTs).

If you have a data set which you feel could also be of benefit to National CERT/CSIRTs and network owners world-wide to help protect victims of cybercrime, please [get in touch](https://www.shadowserver.org/contact/) and discuss the options for using Shadowserver’s proven reporting systems for distribution and remediation.

  * [Honeypots](/topics/honeypots/)
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