# Open IPP Report – Exposed Printer Devices on the Internet

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/open-ipp-report-exposed-printer-devices-on-the-internet/
- **Date :** 2020-06-10

---

# Open IPP Report – Exposed Printer Devices on the Internet

June 10, 2020

Since July 2019, The Shadowserver Foundation has been participating in a EU CEF (Connecting Europe Facility) funded project called [VARIoT](https://variot.eu/). The main goal of the VARIoT (Vulnerability and Attack Repository for IoT) project is to create new services that provide actionable security-related information about the Internet of Things (IoT). One of The Shadowserver Foundation’s roles in the project involves expanding our internet wide daily port scanning capability to enable the mapping of exposed IoT devices on the Internet. The aim is to alert National CSIRTs and network owners of exposed and potentially vulnerable IoT devices, as well as to build higher level statistics about IoT device types observed on a per-country level, which can be shared via the [European Data Portal](https://www.europeandataportal.eu/en) with the general public.

Our new [Internet Printing Protocol (IPP) scan](https://www.shadowserver.org/what-we-do/network-reporting/open-ipp-report/) is the second (after the [Open MQTT scan](https://www.shadowserver.org/news/open-mqtt-report-expanding-the-hunt-for-vulnerable-iot-devices/)) IPv4 Internet-wide scan that we have enabled as part of our VARIoT efforts. It is aimed at uncovering printing devices which use [IPP](https://istopwg.github.io/standards.html) (a HTTP POST based protocol) that have been connected to the Internet without adequate access controls or authorization mechanisms in place. This could allow for a potential range of different types of attacks, from information disclosure and service disruption/tampering, to, in some cases, remote command execution. Network connected printers have been with us since the Internet was born (and long before the IoT term was coined!), but their security aspects are often still misunderstood or completely ignored by many end users.

We scan by sending an **IPP Get-Printer-Attributes** request to **TCP port 631**. We started regular scanning of all 4 billion routable IPv4 addresses on the 5th of June 2020 and added [Open IPP reporting](https://www.shadowserver.org/what-we-do/network-reporting/open-ipp-report/) as part of our [daily public benefit remediation network reports](https://www.shadowserver.org/what-we-do/network-reporting/) on the **8th of June 2020**. Our IPP scans uncover **around 80,000 open devices (printers) per day**. Obviously these counts only represent devices that are not firewalled and allow direct querying over the IPv4 Internet.

The IP-geolocated country breakdown of the above reachable IPP responses is as follows:

![](https://www.shadowserver.org/wp-content/uploads/2020/06/IPP-Worldmap-of-Exposded-Devices-7June2020.png)

Exposed IPv4 IPP services by country (7th June 2020)

![](https://www.shadowserver.org/wp-content/uploads/2020/06/IPP-Map-Legend-7June2020-300x132.png)

The Top countries affected are as follows:

![](https://www.shadowserver.org/wp-content/uploads/2020/06/IPP-Top-Countries-With-Devices-Exposed-7Jun2020.png)

Top countries with exposed IPP services – out of 79,174 services on that day (7th of June 2020)

One of the most common observed implementations of IPP is [CUPS](https://www.cups.org/), which is a well known printing system for Unix-like operating systems. Out of **79,174** results on June 7th 2020 **58,091** devices returned a CUPS version:

CUPS Version Returned | IPv4 Count  
---|---  
CUPS/2.0 | 29017  
CUPS/2.1 | 16774  
CUPS/1.5 | 3935  
CUPS/1.4 | 2937  
CUPS/1.7 | 2309  
CUPS/2.2 | 1862  
CUPS/1.6 | 1118  
CUPS/2.3 | 128  
CUPS/1.2 | 4  
CUPS/2.2.10 | 2  
CUPS/2.1.2 | 2  
CUPS/1.3 | 2  
CUPS/2.3.0 | 1  
  
Out of the roughly 80,000 exposed services, a large percentage returned additional printer information attributes, such as **printer names, locations, models, firmware versions, organizational units** and even **printer wifi ssids**.

For example, the **Top 20 printer make-and-model attribute values** returned for the 7th of June 2020 was as follows (**21,875 entries in total returned**):

Printer make-and-model | IPv4 Count  
---|---  
Local Raw Printer | 2893  
Samsung C48x Series | 899  
Samsung M267x 287x Series | 399  
Brother DCP-1200 – CUPS+Gutenprint v5.2.10 | 327  
CNMF633C/635C | 249  
Samsung M2070 Series | 236  
HP Business Inkjet 2200 – CUPS+Gutenprint v5.2.10 | 232  
HP ColorLaserJet MFP M278-M281 | 215  
Samsung M332x 382x 402x Series | 211  
HP LaserJet M402dn | 190  
SINDOH D410 | 187  
CNMF230 Series | 187  
HP LaserJet MFP M129-M134 | 182  
SINDOH D410 | 182  
Samsung X3220 Series | 180  
Samsung M337x 387x 407x Series | 163  
Samsung C43x Series | 160  
Epson Artisan 50 – CUPS+Gutenprint v5.2.10 | 154  
HP LaserJet Pro MFP M127fn | 149  
HP Color LaserJet MFP M477fdw | 143  
  
Exposing printer devices with anonymous, publicly queryable vendor names, models and firmware versions obviously **makes it much easier for attackers to locate and target populations of devices vulnerable to specific vulnerabilities**.

We hope that the data being shared in our new open IPP device report will lead to a reduction in the number of exposed IPP-enabled printers on the Internet, as well as raise awareness of the dangers of exposing such devices to unauthenticated scanners/attackers. It is unlikely that many people need to make such a printer accessible to everyone – **these devices should be firewalled and/or have an authentication mechanism enabled.**

Details about the format of the new report being shared can be found in the [new Open IPP Report page](https://www.shadowserver.org/what-we-do/network-reporting/open-ipp-report/). All existing Shadowserver report subscribers are now automatically receiving the [Open IPP Report](https://www.shadowserver.org/what-we-do/network-reporting/open-ipp-report/) if any open IPP services are identified within their networks and countries (for national CSIRTs).

If you are not already a subscriber to Shadowserver’s public benefit daily network reports and would like to receive this [new open IPP report](https://www.shadowserver.org/what-we-do/network-reporting/open-ipp-report/) and [our other existing 77 report types](https://www.shadowserver.org/what-we-do/network-reporting/), then please sign up to our [daily public benefit network remediation feed service](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/).

You can also check the updated statistics for this scan on our [dedicated IPP scan page](https://scan.shadowserver.org/ipp/).

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