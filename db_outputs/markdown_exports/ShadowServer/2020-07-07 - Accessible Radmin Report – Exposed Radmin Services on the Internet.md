# Accessible Radmin Report – Exposed Radmin Services on the Internet

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/accessible-radmin-report-exposed-radmin-services-on-the-internet/
- **Date :** 2020-07-07

---

# Accessible Radmin Report – Exposed Radmin Services on the Internet

July 7, 2020

We have recently enabled a new IPv4 Internet-wide scan and [report for accessible Radmin services](https://www.shadowserver.org/what-we-do/network-reporting/accessible-radmin-report/) on port **4899/TCP**. [Radmin](https://www.radmin.com/) is a remote access software product commonly in use today.

We scan by sending a **Radmin connection request** to port **4899/TCP**. Our daily scans uncover around **50,000** accessible Radmin services on port **4899/TCP**.

If you would like to test your own device to see if it has Radmin accessible, try the **nmap** command: “`nmap -v -sV -p 4899 [IP]`“.

While Radmin is in general considered a secure mechanism for remote access, **care should be taken as with all similar types of services to ensure no misconfiguration has taken place**. It is recommended to consider carefully whether every Radmin service should be accessible from the Internet at large or whether it should instead be **restricted to only trusted IP addresses** , thus limiting an **organization’s potential exposed attack surface to a minimum**. The scan is also intended to **raise awareness of any unexpected Radmin instances** that may accidentally have been left accessible.

Of the **50,631** Radmin services that responded to our scan on the **6th July 2020** , the version breakdown was as follows:

Radmin Version Obtained | IPv4 Count  
---|---  
Radmin v3.X Radmin Authentication | 36381  
Radmin (Details Unknown) | 7074  
Radmin v3.0 Windows | 3973  
Radmin v3.X Source IP blocked | 1253  
Radmin v3.3 Windows | 1024  
Radmin v3.X Windows Authentication | 746  
Radmin v2.X Windows Authentication | 152  
Radmin v2.X Radmin Authentication | 28  
  
The country breakdown of **50,631** accessible Radmin services that responded to our probe on the **6th of July 2020** is shown below.

![](https://www.shadowserver.org/wp-content/uploads/2020/07/2020-07-06-Radmin-Exposed-Services-Map.png)

Exposed Radmin services around the world (6th July 2020)

![](https://www.shadowserver.org/wp-content/uploads/2020/07/2020-07-06-Radmin-Legend-300x109.png)

![](https://www.shadowserver.org/wp-content/uploads/2020/07/2020-07-06-Radmin-Treemap.png)

Top Countries with exposed Radmin services (6th July 2020)

Details about the format of the new report being shared can be found in the new [Accessible Radmin Report page](https://www.shadowserver.org/what-we-do/network-reporting/accessible-radmin-report/). All existing Shadowserver report subscribers are now automatically receiving the [Accessible Radmin Report](https://www.shadowserver.org/what-we-do/network-reporting/accessible-radmin-report/) if any exposed Radmin services are identified within their networks and countries (for national CSIRTs).

If you are not already a subscriber to Shadowserver’s public benefit daily network reports and would like to receive this [new accessible Radmin report](https://www.shadowserver.org/what-we-do/network-reporting/accessible-radmin-report/) and our [other existing 79 report types](https://www.shadowserver.org/what-we-do/network-reporting/), then [please sign up to our free daily public benefit network remediation feed service.](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/)

You can also check the updated daily statistics for this scan on our [dedicated Radmin scan page.](https://scan.shadowserver.org/radmin/)

  * [ASN](/topics/asn/)
  * [Geo Locations](/topics/geo-locations/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Statistics](/topics/statistics/)
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