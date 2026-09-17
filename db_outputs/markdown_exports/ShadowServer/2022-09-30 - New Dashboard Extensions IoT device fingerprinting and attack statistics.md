# New Dashboard Extensions: IoT device fingerprinting and attack statistics

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/new-dashboard-extensions-iot-device-fingerprinting-and-attack-statistics/
- **Date :** 2022-09-30

---

# New Dashboard Extensions: IoT device fingerprinting and attack statistics

September 30, 2022

We are happy to announce the first major extension to our newly launched [Dashboard](https://dashboard.shadowserver.org) – the addition of [IoT device statistics ](https://dashboard.shadowserver.org/statistics/iot-devices/map/) and [server-side attack statistics](https://dashboard.shadowserver.org/statistics/honeypot/map/), data sets that have been collected as part of the [HaDEA EU CEF VARIoT project](https://variot.eu).

### IoT Device Statistics

Shadowserver has been fingerprinting IoT devices worldwide through its full IPv4 space and IPv6 hitlist-based daily scans. Data from all our daily scans is classified by an internal scan rule engine by device vendor, model and type. The classification is based on multiple scan data features, such as various protocol banners returned, SSL/TLS certificate fields, HTTP body content, HTTP cookies, SNMP strings etc.

You can now get a unique view of IoT devices and other devices that are exposed on the Internet. Of course, this does not encompass all IoT devices, just those that are reachable by our scans and those we were able to fingerprint. Currently we identify the device manufacturer and model for nearly 200 different vendors. More fingerprints are constantly being added, so that number is sure to grow!

Please note this is population level data and no vulnerability assessment is being made, though likely many of these devices should not be externally accessible!

Example queries:

<https://dashboard.shadowserver.org/statistics/iot-devices/map/>

![](https://www.shadowserver.org/wp-content/uploads/2022/09/IoT-Device-Stats-World-2022-09-28.png)

Top exposed devices by country – 2022-09-28

<https://dashboard.shadowserver.org/statistics/honeypot/tree/>

![](https://www.shadowserver.org/wp-content/uploads/2022/09/IoT-Device-Top-Vendors-Treemap-World-2022-09-28.png)

Top identified exposed devices by vendor – World (2022-09-28)

[https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=1&geo=Europe&dataset=count&limit=1000&group_by=geo&count_as=avg&style=bubble_diagram](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=1&geo=Europe&dataset=count&limit=1000&group_by=geo&count_as=avg&style=bubble_diagram)

![](https://www.shadowserver.org/wp-content/uploads/2022/09/IoT-Device-Top-Vendors-Bubble-Europe-2022-09-28.png)

Top identified exposed devices by vendor in Europe (2022-09-28)

Curious how many Roomba vacuum cleaners are exposed on the Internet? Click [here to find out!](https://dashboard.shadowserver.org/statistics/iot-devices/tree/?day=2022-09-28&vendor=irobot&model=roomba&geo=all&data_set=count&scale=log)

### Attack Statistics

Shadowserver maintains a large-scale honeypot network originally developed as part of the [EU Horizon 2020 SISSDEN project](/news/beyond-the-sissden-event-horizon/). Under VARIoT and FCDO UK funding this network has continued to evolve. It consists of a variety of honeypots, including web-based ones. These web–based honeypots are used to identify and classify various server-side attacks by the vulnerability that is being exploited. This is done by assigning [CVE](https://cve.mitre.org), [EDB](https://www.exploit-db.com), [CNVD](https://en.wikipedia.org/wiki/Chinese_National_Vulnerability_Database) or other tags. As a result we can get an overview of different server-side attacks that can be observed. New tags are constantly being added.

Aside from map, treemap, time series and other standard views, we have also created a Top category of currently known exploited vulnerabilities as well as an anomaly detector to show current exploit trends.

[https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=monitoring&statistic=unique_ips](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=monitoring&statistic=unique_ips)

![](https://www.shadowserver.org/wp-content/uploads/2022/09/Top-Exploited-Vulnerabilities-2022-09-28.png)

Top Exploited Vulnerabilities seen in our web honeypot sensors – 2022-09-28

We have also added a view of the trends related to the most common devices used for attacks and the top devices seen attacking. Information about the attacking devices is obtained through our IoT device fingerprinting scans. When an IP address is then seen attacking our honeypot sensors or darknet (aka. “network telescope”) systems we check it against the latest scan results for that IP address and infer the device manufacturer and model. Please note that this assessment is not necessarily 100% accurate due to device churn and port forwarding (multiple device types responding on different ports). The attack may also originate from a device behind the device IP address identified through scanning, that is actually infected or used for attacks (using network address translation (NAT)).

[https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=anomaly&statistic=unique_ips](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=anomaly&statistic=unique_ips)

![](https://www.shadowserver.org/wp-content/uploads/2022/09/Anomaly-Attacking-Device-2022-09-28.png)

Anomalies in observed attacking devices by vendor – 2022-09-28

In all cases, attacking device anomalies are calculated by comparing a weekly moving average with the last day.

Find out [here](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips) what the top infected device is!

### Daily Data sharing

Statistics for identified IoT devices and infected devices are shared as [CSV files in the European Data Portal daily](https://data.europa.eu/data/datasets/infected-and-exposed-iot-device-statistics?locale=en). You can also visit all other VARIoT datasets in [EDP here](https://data.europa.eu/data/datasets?keywords=variot&locale=en&page=1&sort=modified%2Bdesc,%20relevance%2Bdesc,%20title.en%2Basc).

IP data with results from these scans is shared daily in the [Device Identification Report.](/what-we-do/network-reporting/device-identification-report/) This is a device population report – no assessment is made on the vulnerability state of the device, though many of the devices on the list should not be externally accessible and may be an unnecessarily exposed attack surface.

IP data with detected web-based honeypot attack data is shared daily in the [Honeypot HTTP Scanner Events Report](/what-we-do/network-reporting/honeypot-http-scanner-events/).

As always, the IP data is filtered by a subscribers network, domain or constituency/country.

We are always interested in collaboration and will be adding more data sets to the Dashboard over time, as it becomes our go-to landing place for exploring data about new and emerging threats. We hope to eventually provide our constituents with authenticated access to more granular views of our data about their own individual networks/country through expanded, private dashboards. Join our [new Shadowserver Alliance](https://www.shadowserver.org/partner/) to help influence future research direction and gain additional behind the scenes insight on threats to global cyber security.

If you operate a network or CSIRT and don’t already subscribe to Shadowserver’s [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/), please [sign up here](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/).

  * [Botnets](/topics/botnets/)
  * [Bots](/topics/bots/)
  * [Geo Locations](/topics/geo-locations/)
  * [Honeypots](/topics/honeypots/)
  * [Malware](/topics/malware/)
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