# Observations on cyber threat activity and vulnerabilities in the Gulf Region

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/observations-on-cyber-threats-and-vulnerabilities-in-the-gulf-region/
- **Date :** 2023-05-31

---

# Observations on cyber threat activity and vulnerabilities in the Gulf Region

May 31, 2023

## Introduction

Shadowserver has recently been funded by the [UK Foreign, Commonwealth & Development Office (FCDO)](https://www.gov.uk/government/organisations/foreign-commonwealth-development-office) to provide more detailed and tailored cyber threat insight support to countries in the**Gulf Region** , specifically **Kuwait, Bahrain, the United Arab Emirates (UAE), Saudi Arabia, Oman and Qatar** (“**the Gulf** “). These activities included obtaining a better understanding of the device makeup of the publicly exposed attack surface in those countries, vulnerability exposure (especially relating to emerging threats) and observed attacks/infected devices – coming both from and directed at the region. The intention is to enrich Shadowserver’s [free daily threat feeds](/what-we-do/network-reporting/) and public benefit services to the region, providing National CSIRTs and other system defender entities (organizations that are network owners) with a better awareness of their threat and vulnerability landscape, thus helping them to improve their cybersecurity posture.

This work with the FCDO builds on our previous global outreach to Africa, Indo-Pacific, Central and Eastern Europe (CEEC) to shine a cyber security spotlight on the Gulf Region with a specific focus on **Kuwait, Bahrain, the UAE, Saudi Arabia, Oman and Qatar**. For a review of previous FCDO supported activities please read:

  1. [UK Foreign, Commonwealth & Development Office funds Shadowserver surge in Africa and Indo-Pacific regions](/news/uk-foreign-commonwealth-development-office-funds-shadowserver-surge-in-africa-and-indo-pacific-regions/)
  2. [Continuing Our Africa and Indo-Pacific Regional Outreach](/news/continuing-our-africa-and-indo-pacific-regional-outreach/)
  3. [More Free Cyber Threat Intelligence For National CSIRTs](/news/more-free-cyber-threat-intelligence-for-national-csirts/)
  4. [Shadowserver’s New Public Dashboard](/news/shadowservers-new-public-dashboard/)
  5. [Observations on cyber threat activity and vulnerabilities in Indonesia, Malaysia, Philippines and Thailand](/news/observations-on-cyber-threat-activity-and-vulnerabilities-in-indonesia-malaysia-philippines-and-thailand/)



## Device Fingerprinting

As part of these activities, Shadowserver engaged in adding detection fingerprints for devices observed in the region during our [daily Internet scanning](/news/the-scannings-will-continue-until-the-internet-improves/). This includes identifying the vendor, type and model of publicly exposed devices, so that Internet defenders in those countries will be better aware of their exposed assets when a potential new threat appears. Note we make no assessment of device vulnerability, only exposure.

The bar chart below ([taken from our public dashboard](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=other&d1=2023-03-01&d2=2023-04-30&geo=BH&geo=KW&geo=OM&geo=QA&geo=SA&geo=AE&dataset=count&limit=20&group_by=vendor&count_as=avg&style=bar_chart)) shows the top 20 device vendors by volume identified across the region, including some well known vendors such as **Huawei, Fortinet, Cisco and MikroTik** :

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top-device-exposure-Gulf.png)

Top 20 exposed device vendors found across the Gulf countries (average daily scan results from 2023-03-01 to 2023-04-30)

Drilling down into the publicly exposed devices by country, we observe that the above mentioned vendors form the majority of the (exposed) population in the region, with the exception being Oman, where there is almost a monopoly of **Huawei devices** (over 74k devices, with **Fortinet** less than 1.2k as the second highest device vendor observed by volume).

As displayed in the bubble diagram below, the [top exposed device vendor for **Bahrain** is the Cloud Native Computing Foundation](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=other&d1=2023-03-01&d2=2023-04-30&geo=BH&dataset=count&limit=20&group_by=vendor&count_as=avg&style=bubble_diagram) who maintain the open source **Kubernetes** platform. Kubernetes is a popular open-source system for automating deployment, scaling, and management of containerized applications:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top-device-exposure-Bahrain.png)

Top 20 exposed device vendors found in Bahrain (average daily scan results from 2023-03-01 to 2023-04-30)

We published a blog about [Kubernetes API exposure in 2022](https://www.shadowserver.org/news/over-380-000-open-kubernetes-api-servers/). A new [Kubernetes security audit performed by the NCC Group](https://raw.githubusercontent.com/kubernetes/sig-security/main/sig-security-external-audit/security-audit-2021-2022/findings/Kubernetes%20v1.24%20Final%20Report.pdf) has recently identified a number of bugs around user and network permissions (related to access control and authentication).

Over 1.4k exposed Kubernetes instances represent a substantial potential attack surface (relative to total exposure in the Gulf), and while we do not specifically identify any vulnerabilities, reducing the attack surface would be good practice.

Looking at **Kuwait** , [we observe](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=other&d1=2023-03-01&d2=2023-04-30&geo=KW&dataset=count&limit=20&group_by=vendor&count_as=avg&style=bubble_diagram) that perhaps surprisingly, Huawei devices are not seen in high numbers, with Fortinet, Cisco and TP-Link being the most common vendors:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top-device-exposure-Kuwait.png)

Top 20 exposed device vendors found in Kuwait (average daily scan results from 2023-03-01 to 2023-04-30)

We share actionable, detailed and IP-specific data about exposed devices in your network/constituency in the Gulf and around the world [in the Device Identification report](/what-we-do/network-reporting/device-identification-report/).

## Critical Vulnerabilities (in exposed infrastructure)

One of the most important elements of our free public benefit scans is detection and reporting of critical vulnerabilities in public facing Internet infrastructure to National CSIRTs and network defenders. The critical vulnerabilities we report on allow remote code execution on multiple Internet facing services (which can potentially lead to breaches and ransomware attacks). In the following analysis, we will typically focus on HTTP related vulnerabilities, but we will also mention an older but still critical SNMP issue. These vulnerabilities are typically exploited in the wild, either through ubiquitous or targeted attacks, and often result in security breaches and sometimes ransomware deployment.

We find that [Fortinet CVE-2022-42475 (FortiOS SSL-VPN heap based buffer overflow vulnerability) remains a prevalent weakness across the region](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-03-01&d2=2023-04-30&source=http_vulnerable&source=http_vulnerable6&tag=cve-2022-42475%2B&tag=cve-2022-42475%3Bfortinet&geo=BH&geo=KW&geo=OM&geo=QA&geo=SA&geo=AE&group_by=geo&style=stacked). This is unfortunately consistent with other global regions in terms of a critical volume of detected devices that still remain unpatched.

The **UAE** is most vulnerable to **CVE-2022-42475** , accounting for approximately one-third of all publicly-exposed, critically vulnerable instances in the Gulf Region.

Nevertheless, as shown in the chart below, substantial volumes of vulnerable Fortinet devices remain in all 6 Gulf Region countries. It is clear that action on those devices is still urgently needed:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/fortinet-cve-Gulf.png)

Fortinet CVE-2022-42475 vulnerable devices in the Gulf (daily scan results from 2023-03-01 to 2023-04-30), Y-Axis = unique IP address count

In **Bahrain** , [we also observe CVE-2023-27898](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-03-01&d2=2023-04-30&source=http_vulnerable&source=http_vulnerable6&tag=cve-2023-27898%2B&tag=cve-2023-27898%3Bhttp&geo=BH&geo=KW&geo=OM&geo=QA&geo=SA&geo=AE&group_by=geo&style=stacked) (a vulnerability in the Jenkins open source automation server which could lead to code execution on targeted systems) in a small volume:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/jenkins-cve-Gulf.png)

Jenkins CVE-2023-27898 vulnerable devices in the Gulf (daily scan results from 2023-03-01 to 2023-04-30), Y-axis is unique IP address count

In addition, we [find a number of exposed git configurations](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-03-01&d2=2023-04-30&source=http_vulnerable&source=http_vulnerable6&tag=git-config-file&geo=BH&geo=KW&geo=OM&geo=QA&geo=SA&geo=AE&group_by=geo&style=stacked). Git source code management system configuration data can potentially reveal sensitive information and, as such, should be made secure as a priority for all operators:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/git-cve-Gulf.png)

Exposed Git config instances in the Gulf (daily scan results from 2023-03-01 to 2023-04-30), Y-axis is unique IP address count

We also scan for critical vulnerabilities in Microsoft Exchange servers at risk from remote code execution. These include:

  * [CVE-2020-0688](https://nvd.nist.gov/vuln/detail/CVE-2020-0688)
  * [CVE-2021-26855](https://nvd.nist.gov/vuln/detail/CVE-2021-26855)
  * [CVE-2021-27065](https://nvd.nist.gov/vuln/detail/CVE-2021-27065)
  * [CVE-2022-41082](https://nvd.nist.gov/vuln/detail/CVE-2022-41082)
  * [CVE-2023-21529](https://nvd.nist.gov/vuln/detail/CVE-2023-21529)



[CVE-2022-41082 and CVE-2022-41040 ](https://msrc.microsoft.com/blog/2022/09/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/)(collectively known as [ProxyNotShell](https://www.tenable.com/blog/proxynotshell-owassrf-tabshell-patch-your-microsoft-exchange-servers-now)), affect Microsoft Exchange Server 2013, 2016, and 2019. When combined, they allow an authenticated attacker to interact with the Microsoft Exchange Server Powershell backend and remotely execute code.

At the end of April 2023, there were still [around 58K likely vulnerable Microsoft Exchange servers worldwide](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-03-01&d2=2023-04-30&source=scan&source=scan6&tag=exchange&style=stacked).

[In the Gulf Region, the overall numbers are much smaller](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-03-01&d2=2023-04-30&source=exchange&source=exchange6&geo=BH&geo=KW&geo=OM&geo=QA&geo=SA&geo=AE&group_by=geo&style=stacked). The **UAE** has the highest number of vulnerable Microsoft Exchange servers, with an average of 400-450 devices detected daily for this reporting period as shown in the diagram below:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/exchange-cves-Gulf.png)

Vulnerable Microsoft Exchange instances in the Gulf (daily scan results from 2023-03-01 to 2023-04-30), Y-axis is unique IP address count

We share actionable, detailed and IP-specific vulnerable HTTP (covering, amongst others, the above Fortinet, git config and Jenkins vulnerabilities) and vulnerable Microsoft Exchange servers in your network/constituency in our daily [Vulnerable HTTP ](/what-we-do/network-reporting/vulnerable-http-report/)and [Vulnerable Exchange](/what-we-do/network-reporting/vulnerable-exchange-server-report/) reports.

Note that new CVE vulnerability scans are continuously added to our Vulnerable HTTP report, and we recommend all affected National CSIRTs and network owners in the Gulf prioritize remediation of issues from our Vulnerable HTTP and Vulnerable Exchange reports.

Aside from HTTP-related vulnerabilities, it is also important to keep track of critical vulnerabilities related to other protocols. We scan for many of those as well. A recent example is an SNMP-related [CVE-2017-6736](https://nvd.nist.gov/vuln/detail/CVE-2017-6736) vulnerability in Cisco routers which, while old, is known to have been recently abused by **APT28** – as reported by the UK NCSC in [“APT28 exploits known vulnerability to carry out reconnaissance and deploy malware on Cisco routers” ](https://www.ncsc.gov.uk/news/apt28-exploits-known-vulnerability-to-carry-out-reconnaissance-and-deploy-malware-on-cisco-routers)(see also our blog [UK/US Joint Announcements Remind Us That Un-Remediated Vulnerabilities Snowball](https://www.shadowserver.org/news/uk-us-joint-announcements-remind-us-that-un-remediated-vulnerabilities-snowball/)). Remediation advice can be found [from Cisco](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170629-snmp). On 2023-05-16 we observed 136 routers in the Gulf Region that were still vulnerable to CVE-2017-6736:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/CVE-2017-6736-Gulf-map.png)

Cisco routers by unique IP address vulnerable to CVE-2017-6736 (on 2023-05-16)

Finally, it is worth taking a step back to see the general statistics of services with either [vulnerabilities, misconfigurations or simply being unnecessarily exposed in the Gulf Region](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-01-01&d2=2023-05-15&source=scan&source=scan6&geo=BH&geo=KW&geo=OM&geo=QA&geo=SA&geo=AE&group_by=geo&style=stacked).

![](https://www.shadowserver.org/wp-content/uploads/2023/05/Vulnerable-abusable-or-misconfigured-services-Gulf.png)

Vulnerable, abusable, misconfigured or otherwise unnecessarily exposed services in the Gulf (2023-01-01 to 2023-04-30), Y-axis is unique IP count

We see a sharp drop at the end of January ([less CWMP service exposure on Huawei devices in Saudi Arabia](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-01-01&d2=2023-04-30&source=scan&source=scan6&tag=cwmp&geo=SA&style=stacked)), and then a sharp rise in [Middlebox exposure in the UAE that can be abused for DDoS.](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-01-01&d2=2023-04-30&source=scan&source=scan6&tag=ddos-middlebox&geo=AE&group_by=geo&style=stacked) Shown individually:

[![](https://www.shadowserver.org/wp-content/uploads/2023/05/2023-SA-CWMP-Chart.png)](/wp-content/uploads/2023/05/2023-SA-CWMP-Chart.png)

CWMP exposure in Saudi Arabia (2023-01-01 to 2023-04-30), Y-axis is unique IP address count 

![](https://www.shadowserver.org/wp-content/uploads/2023/05/DDoS-middlebox-UAE.png)

Middlebox exposure in the UAE (2023-01-01 to 2023-04-30), Y-axis is unique IP address count

You can read about how this Middlebox vulnerability can be abused in our previous blog post: [Over 18.8 million IPs vulnerable to Middlebox TCP reflection DDoS attacks.](/news/over-18-8-million-ips-vulnerable-to-middlebox-tcp-reflection-ddos-attacks/)

## Infected (Attacking) Devices

Shadowserver also attempts to identify devices which are detected attacking our honeypot sensors (and which attempt to utilize the sensor to perform Distributed Denial of Service (DDoS) attacks). You can track these [attacks on our Dashboard (updated daily),](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips) and filter by country as well.

Looking at attacks coming from [infected devices in Kuwait](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d2=2023-04-30&geo=KW), we observe a number of HTTP scan and brute force attacks being received from infected DVR and IP telephony systems.

[The most common attacking device seen from Bahrain runs an embedded (presumably vulnerable) Boa webserver](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d1=2023-03-01&d2=2023-04-30&geo=BH). Boa webserver development was discontinued in 2005(!), but continues to be used by multiple manufacturers. For more background on Boa related attacks, see the Microsoft article [“Vulnerable SDK components lead to supply chain risks in IoT and OT environments”](https://www.microsoft.com/en-us/security/blog/2022/11/22/vulnerable-sdk-components-lead-to-supply-chain-risks-in-iot-and-ot-environments/). We also see attacks from infected Fortinet and DrayTek devices.

[MikroTik is the most common infected device seen in the UAE](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d1=2023-03-01&d2=2023-04-30&geo=AE) which is used in DDoS, HTTP and brute force type scans against our honeypots, with Ubiquiti, DrayTek and Fortinet Fortigate device infections in lower volumes.

We see infected MikroTik devices used in DDoS attacks in [Saudi Arabia](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d1=2023-03-01&d2=2023-04-30&geo=SA). We also see Huawei Home Gateway infected devices conducting both brute-force attacks and DDoS attacks.

In addition, we see infected Fortinet/Fortigate devices performing DDoS attacks from [Oman.](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d1=2023-03-01&d2=2023-04-30&geo=OM)

[Qatar shows similar attack vectors](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d1=2023-03-01&d2=2023-04-30&geo=QA). Our observations highlight Fortinet/Fortigate brute force attacks and MikroTik DDoS related activity. Attacks are also observed from compromised Hikvision devices.

## Exploited CVEs

Shadowserver tracks [Common Vulnerability Exposure (CVE)](https://cve.mitre.org/) exploitation attempts in the region and the world, primarily focusing on exposed HTTP resources. CVE signatures supported by our sensors were also enhanced as part of the recent FCDO-funded project, with a focus on CVEs being used in attacks against resources in the region.

For the reporting period of our project (March 1st to April 30th 2023), we saw a low frequency of exploits from sources in the region attacking our sensor network.

Overall, [the most common CVE exploitation attempt seen originating from each Gulf country is CVE-2017-17215](https://dashboard.shadowserver.org/statistics/honeypot/visualisation/?date_range=other&d1=2023-03-01&d2=2023-04-30&host_type=src&geo=BH&geo=KW&geo=OM&geo=QA&geo=SA&geo=AE&dataset=unique_ips&limit=1000&group_by=vulnerability&count_as=avg&style=table) (which targets Huawei HomeGateway devices). This is an old CVE used in many Mirai-like botnets.

Other notable exploits used in attacks against our sensor network (again at low frequency) can also be seen from Kuwait using [EDB-41471](https://www.exploit-db.com/exploits/41471), a MVPower DVR Remote Code Execution (RCE) exploit and [CVE-2016-10372, ](https://nvd.nist.gov/vuln/detail/CVE-2016-10372)and RCE in the Eir D1000 modem that is seen most frequently from the UAE.

## Improvements in Saudi Arabia attack surface exposure

It is particularly worth highlighting improvements in the [general attack surface exposure posture of Saudi Arabia, at least seen from our own daily scan perspective](https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?date_range=other&d1=2023-03-01&d2=2023-04-30&geo=SA&group_by=geo&style=stacked). Previously – at the start of 2023 – Saudi Arabia had a very high exposure of Huawei devices (over 800k devices observed per day), which dropped significantly at the start of February. Overall the public exposure of Huawei devices in Saudi Arabia continued to drop steadily after the initial sharp drop:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/device-exposure-timeseries-Gulf.png)

Device exposure over time in the Gulf, with large drop seen for Saudi Arabia. Y-axis shows unique IP address count

## Summary

Overall, we see a relatively small amount of infrastructure in the Gulf Region being publicly exposed (compared to some other regions globally). Nevertheless, we observe some critical vulnerabilities (allowing for remote code execution), which can serve as potential points of entry for ransomware and APT actors into organizations’ networks. We note a steady improvement in the attack surface exposure in Saudi Arabia, as well as a reminder from the UAE that sometimes changes are made on a large scale that can have a potentially negative impact on the security posture of a country (the exposed Middlebox devices described above).

We hope that our observations demonstrate that it is possible to obtain a view into the exposed Internet infrastructure of a country or region, not just on exposed services, but on the actual (vulnerable) device makeup. This device makeup can have an impact on Internet defenders (and, of course, attackers). Some of the devices may not need to be made accessible to external queries from the public Internet. Exposing them unnecessarily in this way may pose additional security risks, which we have also illustrated specifically for the selected countries. Obtaining situational awareness about the vendor makeup of externally accessible devices on a network of responsibility may allow for a more efficient response and patch roll out, should any vulnerabilities be announced in these devices. Additionally, National CSIRTs that wish to be more proactive should particularly focus on mitigating the exposed attack surface caused by the known vulnerable devices, which may be continuously compromised by multiple threat actors and used for staging other types of potentially more serious attacks.

All the data discussed in the article is shared daily for free with National CSIRTs in the Gulf Region and beyond, as well as with specific network owners/operators that have subscribed directly to Shadowserver’s public benefit services.

If you have not yet done so, [please sign up](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) for our [free daily threat feeds](https://www.shadowserver.org/what-we-do/network-reporting/) that will provide you with specific, actionable IP information about threats or vulnerabilities seen on your network(s). These will be filtered for your networks/domains or constituency (or country, for National CSIRTs).

Please also consider [joining our Alliance](/partner/), which will provide you with additional insights, details into threats that we see and other benefits (as well as helping to ensure financial sustainability for all of Shadowserver’s free public benefit services).

For any questions, please [contact us](/contact/).

**We would like to thank the UK FCDO for their continued support** , **in line with the UK National Cyber Strategy – Pillar 4, Objective 1: to********strengthen the cyber security and resilience of international partners.**

  * [Alliance](/topics/alliance/)
  * [Botnets](/topics/botnets/)
  * [DDoS](/topics/ddos/)
  * [Geo Locations](/topics/geo-locations/)
  * [Honeypots](/topics/honeypots/)
  * [Ransomware](/topics/ransomware/)
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