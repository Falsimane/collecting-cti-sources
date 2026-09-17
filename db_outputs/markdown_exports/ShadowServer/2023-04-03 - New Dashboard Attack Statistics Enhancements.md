# New Dashboard Attack Statistics Enhancements

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/new-dashboard-attack-statistics-enhancements/
- **Date :** 2023-04-03

---

# New Dashboard Attack Statistics Enhancements

April 3, 2023

We are happy to announce multiple enhancements to [our public Dashboard](https://dashboard.shadowserver.org), particularly to the [Exploited Vulnerability](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=monitoring&statistic=unique_ips) data collected by our server-side honeypot sensors, thanks to funding provided by the [UK Foreign Commonwealth and Development Office (FCDO)](https://www.gov.uk/government/organisations/foreign-commonwealth-development-office). We [launched](/news/shadowservers-new-public-dashboard/) our [public Dashboard](https://dashboard.shadowserver.org) in September 2022, supported by UK FCDO funding, and subsequently [extended the data visualizations to encompass IoT related scan results and exploited vulnerability tracking](/news/new-dashboard-extensions-iot-device-fingerprinting-and-attack-statistics/), gathered through [EU CEF VARIoT project](https://variot.eu) funding. We have now added a number of extra features and improvements as demonstrated below.

## CISA Known Exploited Vulnerabilities (KEV) catalog filtering

Shadowserver operates thousands of sensors globally that include honeypots designed to track attempted exploitation of known software vulnerabilities. Exploitation activity as observed by these sensors is updated daily on our Dashboard in the form of a [Top Exploited Vulnerability list](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=monitoring&statistic=unique_ips).

The US Cybersecurity & Infrastructure Agency (CISA) maintains an authoritative list of vulnerabilities confirmed as being exploited in the wild, called the [CISA Known Exploited Vulnerability catalog](https://www.cisa.gov/known-exploited-vulnerabilities). All US federal civilian executive branch (FCEB) agencies are required to remediate vulnerabilities included in the CISA KEV catalog within prescribed timeframes, under a binding operational directive aimed at improving cybersecurity. CISA strongly recommend patching these vulnerabilities immediately.

As part of our latest Dashboard update, we have now [added a new feature to the list of displayed results](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=monitoring&statistic=unique_ips&cisa_kev=yes) that matches each of the Common Vulnerabilities and Exposures ([CVEs](https://cve.mitre.org)) detected by our honeypots with the [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). This potentially enables better prioritization of which CVEs should be triaged and handled by your constituency or network.

![](https://www.shadowserver.org/wp-content/uploads/2023/03/exploited-vulns-CISA-KEV-2023-03-28.png)

Exploited vulnerabilities filtered by presence in the CISA KEV

## Country level filtering

Another newly added feature allows for filtering the exploited vulnerability list by country. For example, the [following query](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=top&statistic=unique_ips&geo=US) displays the most common CVE exploitation sourced from US networks.

![](https://www.shadowserver.org/wp-content/uploads/2023/03/exploited-vulns-US-2023-03-28.png)

Exploited vulnerabilities attempted from IP addresses geo-locating to the US

This filter also includes the option of viewing anomalies per country as well, which are updated daily. For example, the [following query](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=anomaly&statistic=unique_ips&geo=US) displays volume based anomalies in CVE exploitation sourced from US networks.

![](https://www.shadowserver.org/wp-content/uploads/2023/03/exploited-vulns-anomalies-US-2023-03-28.png)

Anomalies in CVE exploitation sourced from US networks

## IoT vulnerability filtering

You can now also track exploited vulnerabilities by whether they affect Internet of Things (IoT) devices or not, by selecting an [IoT filter](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=monitoring&statistic=unique_ips&iot=yes). This should help improve situational awareness in the community of the types of devices under threat.

![](https://www.shadowserver.org/wp-content/uploads/2023/03/exploited-vulns-iot-2023-03-28.png)

Exploited vulnerabilities filtered for only IoT devices

## 

## Improved filtering of CVE vulnerability scan tags

Aside from the exploited vulnerability enhancements, we have also improved filtering functionality in other areas of the dashboard. It is now much easier to filter the results of our scans using CVE numbers (or other) tags. When selecting [vulnerable HTTP instances](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=90&source=http_vulnerable&source=http_vulnerable6&group_by=geo&style=stacked) or [Microsoft Exchange Server instances](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=90&source=exchange&source=exchange6&group_by=geo&style=stacked) you can now select CVE tags with ‘+’ as a suffix. The values for tags with the ‘+’ suffix would be the sum of the rows containing that CVE (e.g. tag like ‘%cve-2021-26855%’). For example, to track Exchange servers vulnerable to CVE-2021-26855 you would [use this query.](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=90&source=exchange&source=exchange6&tag=cve-2021-26855%2B&group_by=geo&style=stacked)

![](https://www.shadowserver.org/wp-content/uploads/2023/03/exchange-CVE-2021-26855-tag-example.png)

Exchange instances vulnerable to CVE-2021-26855

We hope the updates provide new insights into attacks seen on the Internet and improve the usability of our Dashboard. We would like to thank the UK FCDO for their continued support.

If you have not done so yet, [please sign up](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) for our [free daily threat feeds](https://www.shadowserver.org/what-we-do/network-reporting/) that will provide you specific, actionable IP information about threats or vulnerabilities seen on your network(s). These will be filtered for your networks/domains or constituency (or country, for National CSIRTs).

Please also consider [joining our Alliance](/sponsor/), which will provide you with additional insights, details into threats that we see and other benefits (as well as helping to ensure financial sustainability for all of Shadowserver’s free public benefit services).

For any questions, please [contact us](/contact/).

  * [Alliance](/topics/alliance/)
  * [Botnets](/topics/botnets/)
  * [Bots](/topics/bots/)
  * [DDoS](/topics/ddos/)
  * [Geo Locations](/topics/geo-locations/)
  * [Honeypots](/topics/honeypots/)
  * [Malware](/topics/malware/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Shadowserver](/topics/shadowserver/)
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