# The Shadowserver Foundation Threat Report: A Spotlight on Africa

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/the-shadowserver-foundation-threat-report-a-spotlight-on-africa/
- **Date :** 2020-04-30

---

# The Shadowserver Foundation Threat Report: A Spotlight on Africa

April 30, 2020

Here at The Shadowserver Foundation, we like to regularly drill down into our [datasets](https://www.shadowserver.org/what-we-do/) to provide our global partners with a wider and deeper insight into our scan and threat visibility for their regions. This insight can then be used to better drive our outreach activities. Most importantly, it can hopefully allow [National CSIRTs](https://www.shadowserver.org/who-we-serve/national-csirts/) in the region, as well as numerous other [ authorities/partners and private enterprises](https://www.shadowserver.org/who-we-serve/industry-sectors/), to enhance their incident response coordination and share information from our [public benefit victim remediation network reports](https://www.shadowserver.org/what-we-do/network-reporting/) with local communities in a more effective manner. There is also a significant, direct benefit to us: through feedback and collaboration with our report recipients, we get to see how useful our reports are at ground level and gain a better understanding of the local challenges faced in combating Internet security threats. In the long run, this allows us to improve our public services to the Internet defender community.

This blog is the first in a series in which we will take a look at different world regions in order to demonstrate what taking a more holistic view of our data can reveal – starting with the African continent.

Over the past few years, we have taken a particular interest in Africa as we seek to increase our reporting services, especially to the continent’s National CERT/CSIRTs and ISP communities. In order to look at the African threat landscape and to achieve the above objectives, we have partnered with our good friends at [AfricaCERT](https://www.africacert.org/). In doing so, we open up the opportunity to engage with multiple nations and ensure that these countries make the best possible use of our free reporting services. We are also happy to attend training events to share our understanding and insights with the community as a whole, once the global COVID-19 situation allows!

# **Key findings**

In order to paint the current threat picture for Africa, we **collated various IPv4-based datasets** held within our repository, including an **analysis of malware infections**(primarily through sinkhole data); **exposed services** (some of which may be vulnerable) discovered by our **daily scanning** ; **amplification DDoS attacks**(obtained from honeypots); as well as**reputation IP blacklists**.

## **Malware infections in Africa**

Our malware infection statistics come from data collected from **sinkholes** , **honeypots** , **network telescopes** and other sources, operated by either ourselves or our partners. Example [network report types](https://www.shadowserver.org/what-we-do/network-reporting/) that contain this data include: [Botnet Drone Report](https://www.shadowserver.org/what-we-do/network-reporting/drone-botnet-drone-report/), [HTTP Sinkhole Report](https://www.shadowserver.org/what-we-do/network-reporting/sinkhole-http-drone-report/), [Microsoft Sinkhole Report](https://www.shadowserver.org/what-we-do/network-reporting/microsoft-sinkhole-report/), [Brute Force Attack Report](https://www.shadowserver.org/what-we-do/network-reporting/brute-force-attack-report/) and the [Darknet Report](https://www.shadowserver.org/what-we-do/network-reporting/darknet-report/).

Based on these datasets, we see in **total up to 600,000 malware infected IP addresses per day in Africa.** However, it should be noted that observed activity by malware family is biased towards the threats that Shadowserver and its partners are currently sinkholing or otherwise have visibility of (around **400** malware families/variants).

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Time-Series-Threats-Seen-Africa-2020-March-April.png)

Absolute number of malware infections per day by counted daily IP addresses in Africa – March/April 2020

The graph above shows the absolute numbers of infections seen over the past month. Different colors represent different countries – for ease of understanding we have only labelled “**Egypt”** and “**Algeria”** above (as the most infected in absolute numbers), with the rest of the countries grouped into “Other African States”.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Top-Countries-Infected-Africa-2020-04-16.png)

Top 20 Most Malware Infected Countries in Africa by Counted Daily IP addresses – 16th April 2020

Perhaps unsurprisingly, the amount of infections by unique IPs tend to be higher in absolute numbers in more populous countries and/or countries with better Internet infrastructure. In Africa, we see that, currently, most malware infections are in North African countries (such as **Egypt, Algeria and Morocco**). South of the Sahara, the countries with the greatest number of infections include **Nigeria and South Africa**.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-Top20-Threats-2020-04-16.png)

Top 20 Threats Seen in Africa by Daily Unique IP addresses – 16th April 2020

Top infections within the scope of our visibility include very well known and current **Crimeware-As-A-Service and botnet infrastructures** such as [**Andromeda**](https://www.shadowserver.org/news/avalanche-123/)****(which was taken down as part of the international [**Avalanche**](https://www.europol.europa.eu/newsroom/news/andromeda-botnet-dismantled-in-international-cyber-operation) operation) and [**Mirai**](https://www.shadowserver.org/news/mirai-botnet-14-1-million-german-customers-disrupted-liberia-taken-off-line-and-now-the-culprit-has-been-convicted/)**. Instances of infection with both of these malware strains were observed** across the whole continent, which is consistent with global trends. The recently disrupted [**Necurs** ](https://www.shadowserver.org/news/has-the-sun-set-on-the-necurs-botnet/)spam botnet also features in the Top 10. An Illustration of the top threats seen per African country for a given day (16th April 2020) is given below.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Northern-Africa-Top-Threats-2020-04-16.png)

Northern Africa: Top Threats Seen Per Country (where top is understood as most unique IP addresses seen daily) – 16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Southern-Africa-Top-Threats-2020-04-16.png)

Southern Africa: Top Threats Seen Per Country (where top is understood as most unique IP addresses seen daily) – 16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-Map-Top-Threats-Legend-2020-04-16-300x130.png)

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Andromeda-in-Africa-Ratio-2020-04-16.png)

Relative Ratio of Avalanche Andromeda Malware Distribution in Africa – 16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Necurs-in-Africa-Ratio-2020-04-16.png)

Relative Ratio of Necurs Malware Distribution in Africa – 16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Mirai-in-Africa-Ratio-2020-04-16.png)

Relative Ratio of Mirai Malware Distribution in Africa – 16th April 2020

However, what makes Africa stand out in comparison to other regions is the relatively **high prevalence of Android threats** vs other Windows x86 infections.

We see Android trojan malware infections, such as [ **android.backdoor.prizmes**](https://fortiguard.com/encyclopedia/virus/8084143), [**ghost-push**](https://blog.checkpoint.com/2016/11/30/1-million-google-accounts-breached-gooligan/) and [**android.iop**](https://blog.avira.com/goldilocks-hummingbad-android-malware/)**,** in quite substantial volumes.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Android-Backdoor-Prizmes-2020-04-16.png)

Relative Ratio of Android Prizmes Malware Distribution in Africa – 16th April 2020

Like virtually everywhere else in the world, devices infected with **legacy malware** , for example [**Virut**](https://malpedia.caad.fkie.fraunhofer.de/details/win.virut), [**Conficker**](https://malpedia.caad.fkie.fraunhofer.de/details/win.conficker)**and**[**Lethic**](https://malpedia.caad.fkie.fraunhofer.de/details/win.lethic)**,** continue to be observed, which indicates that multiple African victims have been suffering from long-term infections.

## **Exposed services in Africa**

Aside from collecting data about infected machines, for example, via sinkholing, **we also scan the entire IPv4 Internet** on **48 services/protocols** each day in order to find exposed services (i.e. services that can be accessed externally). This does not mean that these services are necessarily vulnerable to attack. Our scans are, rather, **a combination of searching for accessible services, identification of misconfigurations or specific vulnerabilities, finding services that can be abused or misused in some way (for example for amplification scans), detecting (but not exploiting) backdoors, etc**. Our goal is to alert network defenders to the fact that services are exposed or abusable in some way and could be used to harm either their own networks, or those of the wider public Internet. We do not generate reports from all of our scans, as in some cases, we do not think that having a service exposed immediately signals danger – so, for example, we refrain from reporting on SSH servers listening on TCP port 22. We generate [43 different types of reports based on our daily IPv4 scans ](https://www.shadowserver.org/what-we-do/data-collection/)out of 77 reports in total.

**Our scan statistics for Africa total 1.4 million IP addresses daily**. A range of IPv4 devices are revealed each day with multiple services exposed externally, which could therefore potentially be vulnerable to cyber crime exploitation.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Time-Series-Exposed-Services-Africa-2020-04-16.png)

Absolute number of Exposed Services per day by counted daily IP addresses in Africa – March/April 2020

The graph above shows the number of exposed services seen over the last month. Different colors represent different countries – for ease of understanding we have only labelled “South Africa”, “Tunisia”, “Egypt” and “Morocco” above (as the most exposed in absolute numbers), with the rest of the countries grouped into “Others”.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Northern-Africa-Top-Scan-no-SSL-and-SSH-2020-04-16.png)

Top Exposed Services Per Country without SSL and SSH services (where top is  
understood as most daily unique IP addresses seen) –  
16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Southern-Africa-Top-Scan-no-SSL-and-SSH-2020-04-16.png)

Top Exposed Services Per Country without SSL and SSH services (where top is  
understood as most daily unique IP addresses seen) –  
16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-Top-Scan-Legend-2020-04-16-300x130.png)

Our scan statistics which include also general population scans (see below) show that the services most exposed by unique IP addresses in Africa include **CWMP (port 7547/TCP and 30005/TCP), SSL (port 443/TCP) and SSH (port 22/TCP).** As we explain below, this does not mean these are all vulnerable!

[**CWMP** ](https://cwmp-data-models.broadband-forum.org/) (**CPE WAN Management Protocol** – a protocol used by ISPs to auto-configure their customer-premises equipment devices, such as DSL routers and cable modems) has had flaws in the past that have been exploited by IoT malware (such as [Mirai Botnet #14 and a TR-069 zeroday vulnerability](https://www.shadowserver.org/news/mirai-botnet-14-1-million-german-customers-disrupted-liberia-taken-off-line-and-now-the-culprit-has-been-convicted/)). There is no reason to have **CWMP** services exposed publicly to non-trusted, potentially hostile IP addresses.

**SSL** – number 2 on our list – is the name tag that we apply to all HTTPS services exposed on port 443. While most of these are, of course, not vulnerable by default, and their exposure is usually necessary for business reasons, the statistic does give an overview of web-enabled services in Africa. In general, the more advanced the Internet infrastructure, the greater the number of enabled Web services.

There is nothing inherently wrong with having **SSH** enabled and exposing the service publicly on TCP port 22. Nevertheless, misconfigurations in **SSH,** or the use of default or weak passwords, could lead to the compromise of devices (which could include servers, routers or IoT devices). Indeed, **password brute-forcing attacks** against **SSH** are very common, as they also are for **telnet**. Both services are regularly targeted by IoT malware. Unlike **SSH** , there is usually **no good reason to have non-encrypted** **telnet** services exposed publicly.

A number of UDP-based services that can be exploited for [amplification DDoS attacks ](https://www.shadowserver.org/news/the-scannings-will-continue-until-the-internet-improves/), such as [**DNS**](https://www.shadowserver.org/what-we-do/network-reporting/dns-open-resolvers-report/)**or NTP**(see our [NTP monitor](https://www.shadowserver.org/what-we-do/network-reporting/ntp-monitor-report/) and [NTP version](https://www.shadowserver.org/what-we-do/network-reporting/ntp-version-report/) reports) were also found to be prominent.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Top20-Exposed-Services-Africa-2020-04-16.png)

Top 20 Exposed Services Seen in Africa by daily unique IP addresses – 16th April 2020

In general, we observed that countries with greater quantities of IPv4 space tended to harbor more infections and to have a greater number of exposed/accessible services. This trend is much the same throughout the entire world, and is not unique to Africa.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Top20-Exposed-Services-By-Country-Africa-2020-04-16.png)

Top 20 Countries in Africa with Exposed Services by counted daily IP addresses – 16th April 2020

To provide some further insight into the above distribution by country, we took the top 3 scan results (without SSL and SSH) and mapped them to specific countries in Africa.

**Top 3 Open or Vulnerable Services Seen By Country**

In this analysis, we focus on the Top 3 services whose exposure we consider problematic – that is, these are unnecessarily open or vulnerable to abuse. For this reason, we skip **SSL** and **SSH,** which commonly must be exposed as is also often the case with **FTP**.

**CWMP**

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Top10-Exposed-CWMP-Africa-2020-04-16.png)

Top 10 Countries in Africa with CWMP exposure

Clearly, **Tunisia** currently has the greatest number of accessible CWMP servers. As already mentioned, this can unnecessarily provide an attack vector for malicious actors should a vulnerability be found in CWMP server implementations.

**(Open) DNS**

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Top10-Exposed-DNS-Africa-2020-04-16.png)

Top 10 Countries in Africa with (abusable) Open DNS exposure

**Morocco, South Africa** and**Tunisia** have the greatest quantity of exposed**open DNS servers**. These services can be abused for amplification DDoS attacks. It is important to fix the configuration of these services if possible. More information on amplification DDoS attacks can be found in the paper [“Amplification Hell: Abusing Network Protocols for DDoS”](https://christian-rossow.de/articles/Amplification_DDoS.php) by Christian Rossow and on [our open resolver scan page.](https://scan.shadowserver.org/dns/)

**Telnet**

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Top10-Exposed-telnet-Africa-2020-04-16.png)

Top 10 Countries in Africa with telnet service exposure

**South Africa** has the greatest quantity of exposed **telnet** services, with larger amounts seen also in **Kenya** and **Egypt.** Using telnet is a dangerous security practice, as the traffic can be sniffed and credentials along with all the traffic content exposed. Additionally, the telnet service is very often the target of brute force attacks carried out by various variants of malware. It is likely most of these services are actually running on home routers or other IoT devices. If remote access is necessary, a properly secured SSH service should be configured instead.

## **Amplification DDoS overview in Africa**

Together with our partners, such as [CISPA](https://cispa.saarland/), we monitor amplification DDoS attacks across the world using **honeypots** , see for example, our joint participation in the EU H2020 SISSDEN project. These attacks **primarily exploit UDP-based services** – including DNS and NTP services that have been highlighted in the discussion of our scan datasets above.

We found that these types of attacks are currently, reasonably uncommon against African infrastructure compared to the rest of the world. This does not mean that such attacks do not happen. When they do occur, they can have devastating effects on the target infrastructure, potentially even felt at a country level (as was the case, for example, in the [infamous Mirai Botnet #14 attacks that affected Liberia](https://krebsonsecurity.com/2016/11/did-the-mirai-botnet-really-take-liberia-offline/) in 2016/2017).

Our statistics currently show**roughly 20** to **60** IPv4 devices being targeted by amplification DDoS attacks in Africa per day.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Time-Series-Africa-DDoS-March.png)

Amplification DDoS Targets in Africa in March 2020 (Unique IP per day)

The highest number of attacks in a single day in March 2020 was seen on the **27th of March – 54** IP addresses were targeted, with most being located in **Morocco**.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-DDoS-Legend-Screenshot-March-127x300.png)

Country breakdown of DDoS amplification attack targets on March 27th 2020

## **African IP addresses on public blacklists**

One other category of sources Shadowserver monitors are [public blacklists](https://www.shadowserver.org/what-we-do/data-collection/) (we currently draw upon over 110 different sources) of malicious IP addresses. We bundle all of the data from these sources into our [blacklist report](https://www.shadowserver.org/what-we-do/network-reporting/blacklist-report/). Over the past few months, **we have typically seen 2 million to 3 million entries for African IP addresses per day present on these types of blacklists**. Note that sudden zero entries appearing on the charts is usually the result of a data collection failure on our side.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Time-Series-Africa-Blacklist-2020-04-16.png)

Number of IP entries geolocated to Africa on public blacklists – March/April 2020. Note that an IP may appear on multiple lists and thus be counted more than once.

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Relative-ratio-of-IP-blacklist-presence-in-Africa-by-country-2020-04-16.png)

Top Countries in Africa Blacklisted IP addresses (by unique daily IP addresses) – 16th April 2020

As can be seen on the tree map above, **Mauritius** and **Seychelles** IPv4 addresses have a very high profile presence on these lists, unlike in the previous datasets we explored.

A breakdown of the top observed IP blacklist source per country is shown on the maps below:

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Northern-Africa-Top-Blacklist-2020-04-16.png)

Top Blacklist presence per country by unique daily IP addresses – 16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Southern-Africa-Top-Blacklist-2020-04-16.png)

Top Blacklist presence per country by unique daily IP addresses – 16th April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Top-Blacklist-Legend-2020-04-16-300x132.png)

# **Recommended Actions**

The following is a list of actions we believe may have an impact on the state of operation security on the African continent.

First and foremost, we want to continue to deliver – and to extend – **our public benefit****[remediation network reports](https://www.shadowserver.org/what-we-do/network-reporting/)** to more of the right kind of defender entities in Africa. This includes not only National and Government CSIRTs, but also ISPs/Domain Registries operating within the continent, as well as other private or public enterprises and network owners. As our reporting maps show below, our current National CSIRT report coverage could be improved. The number of network owners that directly receive our feeds is also low in comparison to other continents.

Secondly, we believe that a **data-driven approach** to **improving the resilience of the African Internet** is a good way to move forward. For example, **dedicated malware awareness and eradication** campaigns focused on threats like **Andromeda or IoT-related malware** , could be effective in leading to an increase in resilience of African networks. Focusing on Android malware and general Android security awareness would also be beneficial. However, these initiatives would require a collaboration with a large set of stakeholders. We are happy to explore any options in this regard. If you can help, or know someone who can, please [reach out on social media](https://twitter.com/Shadowserver) and help get the message out, or [get in touch by email](https://www.shadowserver.org/contact/).

Thirdly, collaboration with ISPs on **reducing the footprint of exposed services** (for example, focusing on **CWMP** or **Open DNS** or **telnet**) would also be a step forward in terms of improving network resilience.

# **Conclusion & Next Steps**

As with nearly every region around the world, Africa has its own specific threat profile. There is much work that can be done both against legacy-threat malware and newer variants to make the region more secure for the benefit of all Internet users. Spambots, such as Necurs, and malware droppers, such as Andromeda, have powered waves of past attacks against many global targets, while Mirai-infected devices have powered huge DDoS attacks. Infected systems are likely to also be infected by (or become infected with) similar current and future threats too.

Much the same can also be said of the exposed protocols and potentially abusable services that are most at risk of cyber exploitation uncovered by our scans. **Our ultimate goal is to improve the resilience of African network security** and thus see our map and time series charts reflect a reduction in volumes of detected devices. We can **only achieve this goal by working together, through continued and expanded collaboration** between ourselves and our ever growing constituent base.

In terms of National CERT/CSIRT coverage (reflected in our coverage map below), only a small number of these organisations subscribe to our public benefit daily feeds. In total, we have**13 National CSIRTs** in Africa receiving our feeds at a country level and **139 network owners** that subscribe to our feeds directly, **out of 109 National CSIRTs in 138 countries and 4900+ network owners that receive our data worldwide**. **We would encourage all African network owners to subscribe and act on our reports** , and stand ready to supply any National CSIRT in the region with data.

As a community appeal, if you hold any contacts in Africa, we would be most grateful if you could help us out with an introduction in order to enable us to build new relationships with the right partners!

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-National-CSIRTs-April-2020.png)

National CSIRTs in Africa subscribing to Shadowserver public benefit feeds – April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-CSIRTs-Legend-300x231.png)

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-Network-Report-Recipients-April-2020.png)

Direct recipients of Shadowserver reports in Africa – April 2020

![](https://www.shadowserver.org/wp-content/uploads/2020/04/Africa-Direct-Network-Reports-LegendScreenshot-300x94.png)

Whether in Africa or not, if you are not already a subscriber to [Shadowserver’s public benefit daily network reports ](https://www.shadowserver.org/what-we-do/network-reporting/)but would like to receive [our existing 77 report types](https://www.shadowserver.org/what-we-do/network-reporting/), then please [sign up](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) to our free daily remediation feed service.

  * [Bots](/topics/bots/)
  * [Coverage](/topics/coverage/)
  * [DDoS](/topics/ddos/)
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