# Shadowserver Special Reports – Cyclops Blink

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/shadowserver-special-reports-cyclops-blink/
- **Date :** 2022-02-23

---

# Shadowserver Special Reports – Cyclops Blink

February 23, 2022

**UPDATE 2022-04-21:** Fifth special report sent overnight containing 511 IPs likely still infected with Cyclops Blink, corresponding to 270 ASNs in 60 countries. Remediation continuing.  


**UPDATE 2022-04-13:** Overnight 2022-04-12/13 we sent out a fourth special report with 537 IPs likely infected with Cyclops Blink, corresponding to 281 ASNs in 61 countries. The top countries were still United States (154), Canada (58), Sweden (38), Russia (26), Germany (25). A mix of Watchguard and ASUS devices. Remediation continuing, but more patching required.  


**UPDATE 2022-04-08:** Overnight 2022-04-07/08 we sent out a third special report with an additional 553 IPs likely infected with Cyclops Blink, corresponding to 285 ASNs in 61 countries. The top countries were United States (157), Canada (58), Sweden (38), Russia (27), Germany (26).  


**UPDATE 2022-04-06:** US [DoJ announcement](https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-disruption-botnet-controlled-russian-federation) about disruption action against Cyclops Blink infected devices.

**UPDATE 2022-04-01:**[ASUS released updated firmware](https://www.asus.com/content/ASUS-Product-Security-Advisory/) for devices impacted by Cyclops Blink.

**UPDATE 2022-03-25:**[ASUS released a security advisory](https://www.asus.com/content/ASUS-Product-Security-Advisory/) about Cyclops Blink impacting ASUS devices.

**UPDATE 2022-03-17:** [Trend Micro published research](https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html) detailing ASUS devices also being impacted by Cyclops Blink (some ASUS device IPs were included in our second special report, but not explicitly called out at that time, since details were not public).

**UPDATE 2022-03-03:** On 2022-03-03 we sent out a second special report with an additional 673 IPs likely infected with Cyclops Blink, observed on 2022-02-24. These IPs are different to those sent out in the first report. Countries with top infections: USA (188), France (92), Italy (65), Canada (55), Germany (39).

## **Original Article**

On May 23rd 2018, the US Department of Justice (DoJ), Federal Bureau of Investigation (FBI) and Cisco Talos publicly [announced](https://www.justice.gov/opa/pr/justice-department-announces-actions-disrupt-advanced-persistent-threat-28-botnet-infected) the disruption of a novel multi-stage modular malware platform called **VPNFilter**. This was designed to infect small office and home office (SOHO) routers and other network devices. At the time, VPNFilter was believed to be operated by the threat actor known as APT28 (also known as Fancy Bear, Pawn Storm, Sandworm, Sofacy Group, Sednit X-Agent, STRONTIUM and Tsar Team), which was allegedly associated with the Russian military intelligence agency (GRU). You can read more about that sinkholing effort in our original [2018 blog post](https://www.shadowserver.org/news/vpnfilter-fbi-sinkholing/), which includes links to supporting technical information.

Since then, we have continued notifying VPNFilter victims about infected devices worldwide via [Shadowserver’s free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/).

In January 2021, we [collaborated](https://twitter.com/Shadowserver/status/1351563113716453376) with partner Trend Micro on a [joint analysis of the remaining global VPNFilter victim population](https://www.trendmicro.com/en_us/research/21/a/vpnfilter-two-years-later-routers-still-compromised-.html). This added some further scan-based insights about third stage victim prevalence into our daily datasets.

From our vantage point as sinkhole operators, the peak day for VPNFilter infections globally was 2018-07-24, which saw 14,966 unique IP addresses being observed hitting the sinkhole. After the initial fairly rapid (by global Internet response standards) remediation of infected devices, a typical long tail of not yet remediated victims still remains today:

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/20220223-VPNFilter-Sinkhole-Graph-1024x150.png)](/wp-content/uploads/2022/02/20220223-VPNFilter-Sinkhole-Graph.png)

_Figure 1 – Unique sinkholed VPNFIlter IP address per day_

Note the lack of variation in the daily/weekly number of detected IP addresses. As expected, this suggests that the infected devices are always-on routers (which is unlike the typical overnight or weekend patterns of change we usually see in sinkholed home or office PCs).

The IP-geolocated distribution of sinkholed VPNFilter unique IP addresses on that peak day was:

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/20180724-VPNFilter-Sinkhole-Treemap-1024x483.png)](/wp-content/uploads/2022/02/20180724-VPNFilter-Sinkhole-Treemap.png)

_Figure 2 – Unique sinkholed VPNFIlter geolocated IP addresses (2018-07-24)_

With Ukraine having by far and away the most infected victim devices.

This compares to the current sinkholed VPNFilter IP address distribution observed yesterday:

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/20220222-WatchGuard-Sinkhole-Treemap-1024x483.png)](/wp-content/uploads/2022/02/20220222-WatchGuard-Sinkhole-Treemap.png)

_Figure 3 – Unique sinkholed VPNFIlter geolocated IP addresses (2022-02-22)_

## Cyclops Blink replaces VPNFilter

On February 23rd 2022, the [UK National Cyber Security Centre](https://www.ncsc.gov.uk/news/joint-advisory-shows-new-sandworm-malware-cyclops-blink-replaces-vpnfilter) (NCSC), the [Cybersecurity and Infrastructure Security Agency](http://cisa.gov/uscert/ncas/alerts/aa22-054a) (CISA), the [National Security Agency](https://media.defense.gov/2022/Feb/23/2002943421/-1/-1/0/CSA_NEW_SANDWORM_MALWARE_CYCLOPS_BLINK_REPLACES_VPNFILTER_20220223.PDF) (NSA) and the Federal Bureau of Investigation (FBI) jointly announced that they had identified that the threat actor known as Sandworm or Voodoo Bear has deployed a new, large-scale modular malware framework which is affecting network devices. They have named the malware **Cyclops Blink**. The NCSC, CISA, FBI and NSA have previously attributed the Sandworm threat actor to the Russian GRU’s Main Centre for Special Technologies GTsST.

The Cyclops Blink malware is believed to be a more advanced replacement for VPNFilter. It is installed on exploited network devices as part of a legitimate firmware upgrade, allowing persistence between reboots. The UK NCSC’s analysis explains that it is possible to recalculate the Hash-based Message Authentication Code (HMAC) value for the modified firmware image because the WatchGuard FireBox devices use a hard-coded key to initialize the hash calculation. This allows their malware to pass checks and appear to be legitimate, vendor-supplied firmware updates.

Infected victims’ devices are grouped into clusters, each with a list of Command and Control (C2) servers. They communicate with their operators using Transport Layer Security (TLS) running over The Onion Router ([Tor](https://www.torproject.org)) network. To date, Cyclops Blink malware is believed to have been primarily deployed onto [WatchGuard](https://www.watchguard.com) firewall devices (which are Linux ELF 32-bit PowerPC big-endian platforms), and all C2 servers identified to date have been for WatchGuard firewalls. However, the assessment published today indicates that it is likely that the Cyclops Blink malware could also be compiled and deployed onto other architectures and firmware. This botnet appears to have been active since at least June 2019.

A detailed technical analysis of Cyclops Blink by the UK NCSC can be found [here](https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf), which includes Indicators of Compromise (IoCs) and YARA signatures to assist in detection.

## Cyclops Blink Malware Remediation

WatchGuard have provided remediation information for system owners infected with the Cyclops Blink malware:

[https://detection.watchguard.com](https://detection.watchguard.com/)

WatchGuard [estimate](https://www.watchguard.com/uk/wgrd-news/blog/important-detection-and-remediation-actions-cyclops-blink-state-sponsored-botnet-0) that Cyclops Blink malware may have infected approximately 1% of WatchGuard firewall devices. They advise that the default configuration is to prevent access to their management interface from the Internet, so this configuration must be manually enabled by the system administrator.

All WatchGuard device owners should follow each step in these instructions to ensure that devices are patched to the latest version and that any infection is removed.

  * If your device is identified as infected with Cyclops Blink, you should assume that any passwords present on the device have been compromised and replace them immediately.
  * You should ensure that the management interfaces of your network devices are not exposed to the Internet.



**UPDATES 2022-03-25 and 2022-04-01** : Asus have also provided [remediation information](https://www.asus.com/content/ASUS-Product-Security-Advisory/) and [updated firmaware](https://www.asus.com/content/ASUS-Product-Security-Advisory/) for impacted customers.

## Shadowserver Cyclops Blink Special Report

We send out Special Reports whenever we are able to share one-time, high value datasets that we feel should be reported responsibly for maximum public benefit. Although the events included in these Special Reports sometimes fall outside of our [usual 24-hour daily reporting window](https://www.shadowserver.org/what-we-do/), we believe that there would still be significant benefit to our constituents in receiving and hopefully acting on the data.

On February 23rd 2022, we sent out a new Special Report covering network devices that are believed to be likely infected with the Cyclops Blink malware. This one off Cyclops Blink Special Report contained:

  * **1,573** unique victim IP addresses in **495** different Autonomous System Numbers (ASNs) across **70** different countries
  * **25** Command and Control (C2) server IP addresses in **19** different Autonomous System Numbers (ASNs) in **7** different countries



A direct link to the Cyclops Blink Special Report format is [here](/what-we-do/network-reporting/cyclops-blink-special-report/).

## Cyclops Blink Data Visualisation

The data contained in this new Cyclops Blink Special Report was provided to Shadowserver to disseminate rapidly to National CERTs/CSIRTs and network owners globally, to maximise remediation efforts.

Of the 1,573 IPv4 addresses included in the Cyclops Blink Special Report, the majority of likely infected network devices IP-geolocate as being located in the United States, Canada and Central Europe:

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/Cyclops-Blink-img-4c-1024x689.png)](/wp-content/uploads/2022/02/Cyclops-Blink-img-4c.png)

_Figure 4 – Map of likely Cyclops Blink infected devices (2022-02-23)_

Looking at the data in another way, more than half of the network devices believed to be infected with Cyclops Blink malware are located in the United States, France, Italy, Canada and Germany:

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/Cyclops-Blink-img5-1024x557.png)](/wp-content/uploads/2022/02/Cyclops-Blink-img5.png)

_Figure 5 – Tree Map of likely Cyclops Blink infected devices (2022-02-23)_

Shadowserver conducts daily Internet-wide scanning of all IPv4 /0, which includes identification of Internet facing devices, where possible, thanks to the EU HaDEA [VARIoT project](https://variot.eu). We began making this information available to National CERT/CSIRTs and Network Owners who [subscribe](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) to our [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/) in the form of our [Daily Device Identification Report](https://www.shadowserver.org/news/announcing-the-device-identification-report/) in September 2021, which can be used to establish your exposed attack surface. We highly recommend [subscribing](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) and reviewing this report for your network, since this is the same profile an attacker scanning to perform reconnaissance from the outside will also see.

The location of the likely Cyclops Blink infected devices generally matches our scan-based understanding of the global distribution WatchGuard firewall devices which are currently exposed to the Internet:

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/20220222-WatchGuard-Devices-e1645650595577-1024x700.png)](/wp-content/uploads/2022/02/20220222-WatchGuard-Devices.png)

_Figure 6 – Identified WatchGuard firewall devices detected – World (2022-02-22 IPv4 /0 scan)_

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/Cyclops-Blink-img7-1024x568.png)](/wp-content/uploads/2022/02/Cyclops-Blink-img7.png)

_Figure 7 – Identified WatchGuard firewall devices detected – US States (2022-02-22 IPv4 /0 scan)_

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/Cyclops-Blink-img8-1024x568.png)](/wp-content/uploads/2022/02/Cyclops-Blink-img8.png)

_Figure 8 – Identified WatchGuard firewall devices detected – US Counties (2022-02-22 IPv4 /0 scan)_

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/Cyclops-Blink-img9-1024x545.png)](/wp-content/uploads/2022/02/Cyclops-Blink-img9.png)

_Figure 9 – Identified WatchGuard firewall devices detected – World (2022-02-22 IPv4 /0 scan)_

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/20220222-WatchGuard-Models-1024x483.png)](/wp-content/uploads/2022/02/20220222-WatchGuard-Models.png)

_Figure 10 – Identified WatchGuard firewall device models – World (2022-02-22 IPv4 /0 scan)_

Shadowserver’s daily scanning will obviously not detect all WatchGuard devices. However, comparing the 1,573 unique IP addresses reported out as potentially infected with Cyclops Blink malware to the number of publicly exposed systems identified through scanning, does represent similar orders of magnitude to the 1% infection ratio suggested by WatchGuard.

## Cyclops Blink C2 Server Distribution

In addition to the 1,573 IPv4 addresses corresponding to likely infected victim network devices included in our Cyclops Blink Special Report, 25 Cyclops Blink C2 servers have also been identified:

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/Cyclops-Blink-img11-1024x563.png)](/wp-content/uploads/2022/02/Cyclops-Blink-img11.png)

_Figure 11 – Cyclops Blink C2 Server Location Map (2022-02-23)_

[![](https://www.shadowserver.org/wp-content/uploads/2022/02/Cyclops-Blink-img12-1024x556.png)](/wp-content/uploads/2022/02/Cyclops-Blink-img12.png)

_Figure 12 – Cyclops Blink C2 Server Location Countries (2022-02-23)_

## Not Yet Subscribed to Shadowserver’s Free Daily Reports?

If you missed this [Special Report](/what-we-do/network-reporting/cyclops-blink-special-report/) because you were not yet a subscriber to our [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/), do not worry: simply [subscribe for your network or country now](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) and specifically request all recent Shadowserver Special Reports. We will resend the [Special Report](/what-we-do/network-reporting/cyclops-blink-special-report/) specifically for your network or country (for National CERT/CSIRTs).

If you have a data set which you feel could also be of benefit to National CERT/CSIRTs and network owners world-wide to help protect victims of cybercrime, please [get in touch](https://www.shadowserver.org/contact/) and discuss the options for using Shadowserver’s proven reporting systems for distribution and remediation.

  * [Botnets](/topics/botnets/)
  * [Bots](/topics/bots/)
  * [Malware](/topics/malware/)
  * [Sinkholes](/topics/sinkholes/)
  * [Takedowns](/topics/takedowns/)
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