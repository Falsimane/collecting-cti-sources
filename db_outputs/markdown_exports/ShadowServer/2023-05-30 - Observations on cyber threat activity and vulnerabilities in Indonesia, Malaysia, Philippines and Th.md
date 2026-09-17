# Observations on cyber threat activity and vulnerabilities in Indonesia, Malaysia, Philippines and Thailand

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/observations-on-cyber-threat-activity-and-vulnerabilities-in-indonesia-malaysia-philippines-and-thailand/
- **Date :** 2023-05-30

---

# Observations on cyber threat activity and vulnerabilities in Indonesia, Malaysia, Philippines and Thailand

May 30, 2023

## Introduction

Shadowserver has recently been funded by the UK Foreign, Commonwealth & Development Office (FCDO) to provide more detailed and tailored cyber threat insight support to countries in the Association of Southeast Asia Nations (ASEAN), specifically **Indonesia, Malaysia, Philippines and Thailand**. These activities included obtaining a better understanding of the device makeup of the exposed attack surface in those countries, vulnerability exposure (especially relating to emerging threats) and observed attacks/infected devices – coming both from and directed at the region. The intention is to enrich Shadowserver’s [free daily threat feeds](/what-we-do/network-reporting/) and public benefit services to the region, providing National CSIRTs and other system defender entities (organizations that are network owners) with a better awareness of their threat and vulnerability landscape, thus helping them to improve their cybersecurity posture.

This work with the FCDO builds on our previous global outreach to Africa, Indo-Pacific, Central and Eastern Europe (CEEC) to shine a cyber security spotlight on the ASEAN region with a specific focus on **Indonesia, Malaysia, Philippines and Thailand**. For a review of previous FCDO supported activities please read:

  1. [UK Foreign, Commonwealth & Development Office funds Shadowserver surge in Africa and Indo-Pacific regions](/news/uk-foreign-commonwealth-development-office-funds-shadowserver-surge-in-africa-and-indo-pacific-regions/)
  2. [Continuing Our Africa and Indo-Pacific Regional Outreach](/news/continuing-our-africa-and-indo-pacific-regional-outreach/)
  3. [More Free Cyber Threat Intelligence For National CSIRTs](/news/more-free-cyber-threat-intelligence-for-national-csirts/)
  4. [Shadowserver’s New Public Dashboard](/news/shadowservers-new-public-dashboard/)



## Device Fingerprinting

As part of these activities, Shadowserver engaged in adding detection fingerprints for devices observed in the region during our [daily Internet scanning](/news/the-scannings-will-continue-until-the-internet-improves/). This includes identifying the vendor, type and model of publicly exposed devices, so that Internet defenders in those countries will be better aware of their exposed assets when a potential new threat appears.

The following chart shows the top 20 device vendors identified in the 4 countries under study (for devices that are exposed on the public Internet and possible to identify, but not necessarily vulnerable to an attack):

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top20-device-exposure-IMPacT.png)

Top 20 exposed device vendors found across Indonesia, Malaysia, Philippines, Thailand (average daily scan results from 2023-02-01 to 2023-04-30)

For comparison, across the ASEAN countries, the Top 20 device vendor populations are as follows:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top20-device-exposure-ASEAN.png)

Top 20 exposed device vendors found across the ASEAN countries (average daily scan results from 2023-02-01 to 2023-04-30)

You can explore the above charts interactively using our [public Dashboard](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&geo=ID&geo=MY&geo=PH&geo=TH&dataset=count&limit=20&group_by=vendor&count_as=avg&style=bar_chart) as filtered for both [Indonesia, Malaysia, Philippines and Thailand,](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&geo=ID&geo=MY&geo=PH&geo=TH&dataset=count&limit=20&group_by=vendor&count_as=avg&style=bar_chart) as well [as for all of ASEAN.](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&geo=ASEAN&dataset=count&limit=20&group_by=vendor&count_as=avg&style=bar_chart)

[Thailand](https://dashboard.shadowserver.org/statistics/iot-devices/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&geo=TH&dataset=count&limit=20&group_by=vendor&count_as=avg&style=bar_chart) has an unusually high number of exposed ZTE devices. In addition to Huawei and Mikrotik devices that are commonly seen in the region, it also has a relatively high number of TP-Link and Fortinet devices exposed:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top20-device-exposure-Thailand.png)

Top 20 exposed device vendors found across Thailand (average daily scan results from 2023-02-01 to 2023-04-30)

In comparison, Indonesia features a [very high concentration of MikroTik devices, the third highest in the world](https://dashboard.shadowserver.org/statistics/iot-devices/tree/?day=2023-04-30&vendor=mikrotik&geo=all&data_set=count&scale=log). Misconfigured or unpatched MikroTik devices are often one of the top targets for attackers:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/MikroTik-Treemap.png)

Publicly exposed MikroTik devices worldwide (by unique IP address) on 2023-04-30

It is also worth noting the uniquely high number of [Hughes Network Systems](https://www.hughes.com/) devices (used for satellite broadband Internet) – [the largest in the world ](https://dashboard.shadowserver.org/statistics/iot-devices/tree/?day=2023-04-30&vendor=hughes&geo=all&data_set=count&scale=log)(though interestingly, we did not observe any malware infections related to those IP addresses):

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top20-device-exposure-Indonesia.png)

Top 20 exposed device vendors found across Indonesia (average daily scan results from 2023-02-01 to 2023-04-30)

Malaysia’s device exposure is dominated by Huawei devices, as well as QLC Chain – a “next generation public chain for Network-as-a-Service (NaaS)”, which now appears to be unmaintained. QLC Chain device detections are mostly the [result of CoAP exposure.](https://www.shadowserver.org/news/accessible-coap-report-scanning-for-exposed-constrained-application-protocol-services/) Constrained Application Protocol (CoAP) is a specialized web transfer protocol for use with constrained nodes and constrained networks such as in the Internet of Things (IoT):

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top20-device-exposure-Malaysia.png)

Top 20 exposed device vendors found across Malaysia (average daily scan results from 2023-02-01 to 2023-04-30)

Exposed QLC Chain devices dominate in the Philippines as well:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/top20-device-exposure-Philippines.png)

Top 20 exposed device vendors found across Philippines (average daily scan results from 2023-02-01 to 2023-04-30)

To help system defenders identify devices that are unnecessarily exposed on the public Internet, we share free, actionable, detailed and IP-specific data on exposed devices in your network/constituency in our daily [Device Identification report](/what-we-do/network-reporting/device-identification-report/).

## Critical Vulnerabilities (in exposed infrastructure)

As part of its core activities, Shadowserver also scans and alerts system owners and National CSIRTs about critical vulnerabilities in their Internet infrastructure, especially those that enable unauthenticated remote code execution on high value resources. These vulnerabilities often result in breaches, which may lead to ransomware deployment.

It is worth noting that a relatively high number of likely vulnerable devices remain publicly exposed in the region. These include Fortinet devices vulnerable to [CVE-2022-42475](https://nvd.nist.gov/vuln/detail/cve-2022-42475), a FortiOS SSL-VPN heap based buffer overflow vulnerability, with [nearly 900 Fortinet installations across the region (with almost half of those in Thailand)](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-01-01&d2=2023-04-30&source=http_vulnerable&source=http_vulnerable6&tag=cve-2022-42475%3Bfortinet&tag=fortinet%3Bcve-2022-42475&geo=ID&geo=MY&geo=PH&geo=TH&group_by=geo&style=stacked):

![](https://www.shadowserver.org/wp-content/uploads/2023/05/Fortinet-CVE.png)

Fortinet CVE-2022-42475 in Indonesia, Malaysia, Philippines and Thailand (2023-01-01 to 2023-04-30), Y-axis shows unique IP address count

Multiple VMware related vulnerabilities in VMWare vSphere and ESXi hypervizors – [CVE-2021-21972](https://www.vmware.com/security/advisories/VMSA-2021-0002.html), [CVE-2021-21974](https://nvd.nist.gov/vuln/detail/CVE-2021-21974) (CVSS 8.8), [CVE-2020-3992](https://nvd.nist.gov/vuln/detail/CVE-2020-3992) (CVSS 9.8), [CVE-2019-5544](https://nvd.nist.gov/vuln/detail/CVE-2019-5544) (CVSS 9.8) remain, [with over 1800 likely vulnerable installations (and >50% of those in Thailand)](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-01-01&d2=2023-04-30&source=http_vulnerable&source=http_vulnerable6&tag=vmware%2B&geo=ID&geo=MY&geo=PH&geo=TH&group_by=geo&style=stacked):

[![](https://www.shadowserver.org/wp-content/uploads/2023/05/VMware-CVEs.png)](/wp-content/uploads/2023/05/VMware-CVEs.png)

VMware CVE-2021-21972, CVE-2021-21974, CVE-2020-3992, CVE-2019-5544 in Indonesia, Malaysia, Philippines and Thailand (2023-01-01 to 2023-04-30), Y-axis shows unique IP address count

As can be seen in the lack of decay curve in the graph, remediation of these vulnerabilities appears to have stalled. Note: these vulnerabilities were speculated to have been behind the recent ESXiArgs ransomware campaign (see [CERT-FR advisory](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2023-ALE-015/) for more information), so these devices may represent a continuing risk.

Another potentially serious vulnerability is related to exposed Zimbra collaboration servers. [CVE-2022-37042](https://nvd.nist.gov/vuln/detail/CVE-2022-37042) is an often exploited unauthenticated remote code execution vulnerability. [Over 1384 vulnerable installations remain exposed in the region as of 30th April 2023, most of those in Indonesia (nearly 1000)](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-01-01&d2=2023-04-30&source=http_vulnerable&source=http_vulnerable6&tag=cve-2022-37042%2B&geo=ID&geo=MY&geo=PH&geo=TH&group_by=geo&style=stacked):

![](https://www.shadowserver.org/wp-content/uploads/2023/05/Zimbra-CVE.png)

Zimbra CVE-2022-37042 (CVE-2022-27925) in Indonesia, Malaysia, Philippines and Thailand (2023-01-01 to 2023-04-30), Y-axis shows unique IP address count

Another target that is often attacked is Microsoft Exchange. Shadowserver scans the entire Internet daily for multiple Microsoft Exchange vulnerabilities, including:

  * [CVE-2020-0688](https://nvd.nist.gov/vuln/detail/CVE-2020-0688)
  * [CVE-2021-26855](https://nvd.nist.gov/vuln/detail/CVE-2021-26855)
  * [CVE-2021-27065](https://nvd.nist.gov/vuln/detail/CVE-2021-27065)
  * [CVE-2022-41082](https://nvd.nist.gov/vuln/detail/CVE-2022-41082)
  * [CVE-2023-21529](https://nvd.nist.gov/vuln/detail/CVE-2023-21529)



We still observe [nearly 650 installations exposed in the region that are likely vulnerable to one or more of the above vulnerabilities](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=90&source=exchange&source=exchange6&tag=cve-2020-0688%2B&tag=cve-2021-26855%2B&tag=cve-2021-27065%2B&tag=cve-2022-41082%2B&tag=cve-2023-21529&geo=ID&geo=MY&geo=PH&geo=TH&group_by=geo&style=stacked), most in Thailand and Indonesia:

![](https://www.shadowserver.org/wp-content/uploads/2023/05/Exchange-CVE.png)

Microsoft Exchange servers in Indonesia, Malaysia, Philippines and Thailand (2023-01-01 to 2023-04-30), Y-axis shows unique IP address count.

It is also worth noting many Microsoft Exchange servers remain infected with cryptominers, such as [DLTminer (around a 1000), particularly in Malaysia and Indonesia](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2023-02-01&d2=2023-04-30&source=sinkhole&source=sinkhole6&tag=DLTminer&geo=ID&geo=MY&geo=PH&geo=TH&style=stacked). You can read more on the background story of DLTMiner and Microsoft Exchange infections in this [ESET report](https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/):

![](https://www.shadowserver.org/wp-content/uploads/2023/05/Dltminer.png)

Microsoft Exchange servers infected with DLTminer in Indonesia, Malaysia, Philippines and Thailand (2023-02-01 to 2023-04-30), Y-axis shows unique IP count.

We share actionable, detailed and IP-specific information about vulnerable HTTP services (including the Fortinet, VMware and Zimbra vulnerabilities highlighted above) and vulnerable Microsoft Exchange in your network/constituency in our free daily [Vulnerable HTTP](/what-we-do/network-reporting/vulnerable-http-report/) and [Vulnerable Exchange reports](/what-we-do/network-reporting/vulnerable-exchange-server-report/).

Aside from HTTP related vulnerabilities, it is also important to keep track of critical vulnerabilities related to other network protocols. We also scan for many of those. A recent example is an SNMP-related [CVE-2017-6736](https://nvd.nist.gov/vuln/detail/CVE-2017-6736) vulnerability in Cisco routers which, while old, is known to have been recently abused by threat actor APT28 – as reported by NCSC UK in “[APT28 exploits known vulnerability to carry out reconnaissance and deploy malware on Cisco routers](https://www.ncsc.gov.uk/news/apt28-exploits-known-vulnerability-to-carry-out-reconnaissance-and-deploy-malware-on-cisco-routers)” (see also our blog [UK/US Joint Announcements Remind Us That Un-Remediated Vulnerabilities Snowball).](https://www.shadowserver.org/news/uk-us-joint-announcements-remind-us-that-un-remediated-vulnerabilities-snowball/) On 2023-05-16 we observed **652** routers in the ASEAN region as still potentially vulnerable. Remediation advice can be found [from Cisco](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170629-snmp).

![](https://www.shadowserver.org/wp-content/uploads/2023/05/CVE-2017-6736-ASEAN-map.png)

Cisco routers by unique IP address vulnerable to CVE-2017-6736 in ASEAN (on 2023-05-16)

## Infected (attacking) devices

Shadowserver also attempts to identify devices detected attacking its honeypot sensors (and attempting to utilize the sensor to perform Distributed Denial of Service (DDoS) attacks). You can track these [attacks on our Dashboard (updated daily),](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips) and filter by country as well.

[ For Thailand](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d2=2023-04-30&geo=TH), we typically see attacking infected devices to be MikroTik and also devices running the Boa webserver (these may actually be multiple vendors). Development of Boa webserver was discontinued in 2005(!), but the unsupported software continues to be used by multiple manufacturers. For more background on Boa related attacks, see the [Microsoft article “Vulnerable SDK components lead to supply chain risks in IoT and OT environments”](https://www.microsoft.com/en-us/security/blog/2022/11/22/vulnerable-sdk-components-lead-to-supply-chain-risks-in-iot-and-ot-environments/).

[For Indonesia](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d2=2023-04-30&geo=ID), MikroTik infections are unsurprisingly prevalent due to the high concentration of those devices in the country. We also see a significant number of Fortinet infections.

In addition, we see Ubiquiti Unifi controllers and Zimbra servers used for DDoS attacks (note the vulnerable population of Zimbra servers in Indonesia compared to other countries discussed earlier).

[In Malaysia](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d2=2023-04-30&geo=MY), MikroTik are the most commonly observed infected devices, followed by embedded Boa devices and FiberHome devices.

[The Philippines](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips&d2=2023-04-30&geo=PH) is the only country that breaks the daily majority MikroTik pattern, with FiberHome and Huawei Home Gateway devices typically occupying the top classifications of infected devices.

Note, however, that for DDoS attacks originating in this region, we predominantly observe MikroTik devices attacking from the Philippines.

Finally, it is worth noting that Hikvision and HiSilicon based DVRs are the most commonly infected video system devices in the region.

## Exploited CVEs

Shadowserver also tracks [Common Vulnerability Exposure (CVE)](https://cve.mitre.org) exploitation attempts in the region and the world, primarily focusing on exposed HTTP resources. CVE signatures supported by our sensors were also enhanced as part of the recent FCDO-funded project, with a focus on CVEs being used in attacks against resources in the region.

In the period between 2023-02-01 and 2023-04-30, the most common CVE exploitation attempt (by unique source IP address) observed originating from each country was [CVE-2017-17215](https://nvd.nist.gov/vuln/detail/cve-2017-17215) (targeting Huawei HomeGateway devices). This is an old CVE used in many Mirai-based botnets. However, in general, [software vulnerability exploitation attacks observed coming from the region are surprisingly few](https://dashboard.shadowserver.org/statistics/honeypot/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&host_type=src&geo=ID&geo=MY&geo=PH&geo=TH&dataset=unique_ips&limit=1000&group_by=vulnerability&count_as=avg&style=table).

Of more interest are the exploits used to attack our sensors in particular countries. The [most common attack (by connection) against Thailand-based sensors](https://dashboard.shadowserver.org/statistics/honeypot/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&host_type=dst&geo=TH&dataset=connections&limit=10&group_by=vulnerability&count_as=avg&style=table) is one dedicated to SugarCRM ([CVE-2023-22952](https://nvd.nist.gov/vuln/detail/CVE-2023-22952)), which we first [reported on 16th January 2023.](https://twitter.com/Shadowserver/status/1614975159471046657) [For Malaysia](https://dashboard.shadowserver.org/statistics/honeypot/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&host_type=dst&geo=MY&dataset=connections&limit=10&group_by=vulnerability&count_as=avg&style=table) and [Indonesia](https://dashboard.shadowserver.org/statistics/honeypot/visualisation/?date_range=other&d1=2023-02-01&d2=2023-04-30&host_type=dst&geo=ID&dataset=connections&limit=10&group_by=vulnerability&count_as=avg&style=table), the most common attack was Unisharp laravel-filemanager [CVE-2022-40734](https://nvd.nist.gov/vuln/detail/CVE-2022-40734). For the Philippines, it was TP-Link [CVE-2017-16959](https://nvd.nist.gov/vuln/detail/CVE-2017-16959)

## Summary

We see a significant attack surface exposed in Indonesia, Malaysia, Philippines and Thailand, especially related to home router brands and video systems. This is an area where focused remediation and awareness campaigns may help in reducing that exposure. Many of these devices are infected and in use in DDoS botnets. Additionally, critical vulnerabilities in Microsoft Exchange, Fortinet, VMware and Zimbra installations remain, making them easily discoverable points of entry for ransomware operators and APT groups. It is also potentially problematic that one of the highest exposures appears related to a now defunct QLC Chain project, which is unlikely to receive security updates.

We hope that our observations above demonstrate that it is possible to obtain a view into the exposed Internet infrastructure of a country, not just on exposed services but on the actual (vulnerable) device makeup. This device makeup can have an impact on Internet defenders (and, of course, attackers). Some of the devices may not need to be accessible to external queries from the public Internet. Exposing them unnecessarily in this way may pose additional security risks, which we have also illustrated specifically for the selected countries. Obtaining situational awareness about the vendor makeup of externally accessible devices on a network of responsibility may allow for more efficient incident response and patch roll out processes, should any new vulnerabilities be announced in these devices. Additionally, National CSIRTs that wish to be more proactive should focus on mitigating the exposed attack surface created – especially by the known vulnerable devices, which are continuously compromised by multiple threat actors and used for staging other types of potentially more serious attacks.

All the data discussed in the article is shared daily for free with National CSIRTs in Indonesia, Malaysia, Philippines and Thailand, other ASEAN states, as well as with specific network owners/operators who have subscribed directly to Shadowserver’s public benefit services.

If you have not yet already done so, [please sign up](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) for our [free daily threat feeds](https://www.shadowserver.org/what-we-do/network-reporting/) that will provide you with specific, actionable IP information about threats or vulnerabilities seen on your network(s). These will be filtered for your networks/domains or constituency (or country, for National CSIRTs).

Please also consider [joining our Alliance](/partner/), which will provide you with additional insights, details into threats that we see and other benefits (as well as helping to ensure financial sustainability for all of Shadowserver’s free public benefit services).

For any questions, please [contact us](/contact/).

**We would like to thank the UK FCDO for their continued support, in line with the UK National Cyber Strategy – Pillar 4, Objective 1: to strengthen the cyber security and resilience of international partners.**

  * [Alliance](/topics/alliance/)
  * [Botnets](/topics/botnets/)
  * [DDoS](/topics/ddos/)
  * [Funding](/topics/funding/)
  * [Geo Locations](/topics/geo-locations/)
  * [Honeypots](/topics/honeypots/)
  * [Malware](/topics/malware/)
  * [Ransomware](/topics/ransomware/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Sinkholes](/topics/sinkholes/)
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