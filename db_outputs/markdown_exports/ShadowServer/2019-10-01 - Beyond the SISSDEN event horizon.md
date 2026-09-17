# Beyond the SISSDEN event horizon

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/beyond-the-sissden-event-horizon/
- **Date :** 2019-10-01

---

# Beyond the SISSDEN event horizon

October 1, 2019

Between May 2016 and April 2019, The Shadowserver Foundation participated in the [SISSDEN EU Horizon 2020 project](https://cordis.europa.eu/project/id/700176/reporting) (Grant Agreement [700176](https://cordis.europa.eu/project/rcn/202679/factsheet/en)). The main goal of the project was to improve the cybersecurity posture of EU entities and end users through the development of situational awareness and sharing of actionable information. For a quick introduction to the project please check out our [3 minute SISSDEN project video](https://vimeo.com/shadowserver/sissden-overview):

The primary benefit for Shadowserver subscribers was the addition of **five** new report types in our [free daily feeds](https://www.shadowserver.org/what-we-do/) for National CSIRTs and network owners. This blog post explains Shadowserver’s role in the project, the honeypot deployment framework architecture, data collected, new report types and our future honeypot sensor work beyond SISSDEN.

#### What was The Shadowserver Foundation’s role in the SISSDEN project?

The Shadowserver Foundation’s main contribution to the project was the creation of a new worldwide network of over **250** sensors (each containing many types of honeypots), operated from within the EU. These sensors logged unsolicited attack traffic directed at them into a new EU based high-throughput data processing centre. The primary passive threat data collection mechanisms (honeypots and darknets) deployed by the project were complemented by behavioural analysis of malware and multiple external data sources, both handled by other project partners. Actionable information produced by SISSDEN was then used for the purposes of no‐cost victim notification and remediation via organizations such as National CSIRTs, ISPs, hosting providers etc, via Shadowserver’s free daily victim remediation feeds. **Five** [new report types](https://www.shadowserver.org/news/recent-additions-to-our-available-free-daily-network-report-types/) were created.

#### What attacks can be observed using SISSDEN honeypot sensors?

The SISSDEN project was focused on observing client to server attacks that utilize various forms of scanning as an element of their propagation strategy. This observation of attacks was performed using **honeypots** and **darknets (also known as network telescopes)**. Attacks that can be observed in this manner include various techniques used by botnets, worms and mass exploitation tools to compromise devices. Examples are various exploits against specific application vulnerabilities allowing for remote code execution, brute force attacks, exploitation of configuration errors, etc. Many attacks against IoT devices propagate in this manner. Large scale honeypot networks are therefore uniquely positioned to observe IoT attacks at scale. Common threats observed include **Mirai** and its variants, as well as worms such as **Wannacry** (those Wannacry variants that have had their binaries patched to use different kill-switch domains). Other types of attacks that can be observed include **port scanning** , **reflected amplification DDoS** attacks and attempts to send**spam** through open relays. Aside from simply observing the attacks themselves, the multiple honeypots deployed per sensor location had the capability to collect malicious **artifacts** associated with a successful attack – this malware can then be subsequently analyzed in **sandboxes** , which can lead to the discovery and mapping out of the **underlying botnet** or **malware C &C** infrastructure involved in attacks.

#### SISSDEN Honeypot Sensor overview (World) at Project End (April 2019)

![](https://www.shadowserver.org/wp-content/uploads/2019/09/SISSDEN_Sensor_IP_World_Map_April2019.png)

Figure 1: IP address allocation of the SISSDEN honeypot sensor network

The primary data collection mechanism at the heart of the SISSDEN project was a sensor network composed of many honeypots. As of the end of the project in April 2019, **257** individual sensor nodes have been delivered, located in **59** countries. These sensors had **974** IP addresses allocated to them, from **119** different ASNs, and had interfaces present in **383** unique /24 (Class C) network ranges. Figure 1 illustrates the IP distribution of the sensors worldwide. Countries in green host at least **1** sensor IP. The darker the shade of green the more sensor IP address are hosted in that country.

#### The SISSDEN Platform Architecture

![](https://www.shadowserver.org/wp-content/uploads/2019/09/SISSDEN_Honeypot_Network_Architecture.png)

Figure 2. High level overview of the SISSDEN honeypot platform architecture

The SISSDEN sensor network was composed of Virtual Private Server (**VPS)** provider hosted nodes, procured at a cost from the VPS providers, and nodes **donated** to the project by third-parties, all acting as endpoints. These VPS nodes are not the actual honeypots themselves. Instead, they act as **transparent layer 2 Ethernet tunnels** to the SISSDEN European **datacenter**. Attack traffic directed at IP addresses assigned to the VPS nodes was delivered via these transparent layer 2 tunnels to corresponding VMs in the datacenter which ran the actual honeypots themselves, in the form of **dockerized** containers. The honeypots in the datacenter then responded to attacks against the tunnelled IP addresses from the VPS nodes. From the point of view of the attacker, this layer 2 tunneling was invisible and it appeared that all network communications came from the VPS nodes themselves.

The architecture deployed allowed for easier management of the honeypots. Instead of having to remotely manage (and remotely maintain) honeypots at the individual VPS provider locations, all honeypots could be **standardized** and centrally managed in one datacenter instead.

The Shadowserver Foundation developed specialist VPS and honeypot management software that allows **fast and semi-automated deployment** and **management of honeypots** on a large scale. SISSDEN also carried out **improvements or extensions to multiple honeypot technologies** to standardize the way log event data or other object related data was recorded. Multiple sets of open source honeypot code changes have already been accepted by the corresponding authors of the relevant code and integrated in their respective upstream main releases. The software we developed managed the technical configuration, deployment, OS and application software packages, and security patching of the procured VPS nodes, as well as communication with the VPS providers. Most importantly, it **enabled a near seamless point and click deployment** of new honeypots by an operator through a web-based management interface.

Multiple types of honeypot systems were deployed within SISSDEN, in the form of multiple **VM instances running honeypots** packaged in **docker containers**. Each honeypot VM emulated different services with one or more potential vulnerabilities and collected data about attacks observed against those services. Honeypots located in the SISSDEN backend had a **standard configuration** and **standard data collection formats** , and were injected into appropriate transparently tunneled network VLANs to collect attack data using the IPv4 addresses that were transparently layer 2 tunneled from the target VPS Provider network.

Honeypot event data was live streamed to a publish/subscribe (pub/sub) message broker system ([HPFeeds](https://github.com/hpfeeds/hpfeeds)). Multiple clients push and pull data from these message broker channels in real time, such as for ingesting published event data into the backend data storage systems. The **Amazon S3** protocol was used to transport binary object data (such as **malware** or **PCAP** files) to the locally hosted backend (rather than the Amazon cloud).

The honeypots deployed were modified to support **HPFeeds** (for events) and/or Amazon S3 (for binary object transfer) when necessary. In the case of HPFeeds, there must be appropriate event data generated that can be sent to a particular channel; in the case of Amazon S3, the honeypot must capture malware binaries or packet capture files which can be stored on the backend using a locally hosted [Pithos](http://pithos.io/) S3 instance (rather than the Amazon cloud). Shadowserver has heavily contributed to HPFeeds development through the SISSDEN project, improving the broker’s resilience and scalability, as well as merging multiple bugfixes into the official HPFeeds version. On average, the SISSDEN HPFeeds broker processed around **250-300** live honeypot detected events per second.

The main backend data storage component was implemented using two open source software solutions: [Elasticsearch](https://www.elastic.co) (for storing event data) and [Pithos](http://pithos.io/) S3 (a locally hosted, on premises version of Amazon S3, for storing binary object data). Access to these systems was exposed using their respective native APIs. A single sign-on (SSO) and access control solution was developed to authenticate and proxy all connections to these APIs. The SSO proxy handled on average around **100** connections per second.

All traffic to the honeypots was captured at a network level using [Moloch](https://molo.ch), an open source, large scale, full packet capturing, indexing, and database system. Network event data captured by Moloch was stored in the main SISSDEN Elasticsearch cluster. Moloch saved PCAP data to the SISSDEN Pithos S3 cluster, allowing multiple capture nodes to scale PCAP storage through the central S3 object store cluster. The locations of stored S3 PCAP files were indexed in Elasticsearch, allowing easy search and data retrieval. The Suricata IDS was deployed as part of Moloch to enrich the dataset with IDS alerts. **150-200** GBytes of PCAP data to sensors was captured on an average day.

#### What honeypot types were deployed?

The honeypots deployed as part of the core sensor network at the end of the H2020 SISSDEN project pilot included:

**Honeypot Type** | **Description** | **Instances running (as of 28th April 2019)** | **Attack events collected (from 1st May 2018 to 28th April 2019)** | **Official Pilot Data collection start (note some honeypots were deployed earlier)**  
---|---|---|---|---  
[**CiscoASA**](https://github.com/Cymmetria/ciscoasa_honeypot) | **Cisco ASA honeypot** | **25** | **13 784** | **May 2018**  
[**Conpot**](https://github.com/mushorg/conpot) | **ICS/SCADA honeypot** | **94** | **3 342 793** | **May 2018**  
[**Cowrie**](https://github.com/cowrie/cowrie) | **SSH/Telnet honeypot** | **94** | **463 004 791** | **May 2018**  
[**Dionaea**](https://github.com/DinoTools/dionaea) | **Multipurpose honeypot** | **94** | **7 687 933** | **February 2019**  
[**Django-admin**](https://github.com/dmpayton/django-admin-honeypot) | **Django honeypot** | **10** | **1** | **April 2019**  
[**Elasticpot**](https://github.com/Jc2k/ElasticpotPY) | **Elasticsearch honeypot** | **94** | **104 555** | **May 2018**  
[**Glastopf**](https://github.com/mushorg/glastopf) | **Web honeypot** | **94** | **39 653 356** | **May 2018**  
[**Heralding**](https://github.com/johnnykv/heralding) | **Credential catching honeypot** | **94** | **552 161 401**  
**(auth logs)** | **November 2018**  
[**Honeypy**](https://github.com/foospidy/HoneyPy) | **Multipurpose honeypot** | **10** | **199 562 984** | **March 2019**  
[**MICROS**](https://github.com/Cymmetria/micros_honeypot) | **MICROS honeypot** | **15** | **47 873** | **January 2019**  
[**Rdpy**](https://github.com/citronneur/rdpy) | **Remote desktop honeypot** | **10** | **45 140** | **April 2019**  
**Spampot** | **Spam catching honeypot** | **90** | **811 393 073** | **May 2018**  
[**Struts**](https://github.com/Cymmetria/StrutsHoneypot) | **Apache Struts Honeypot** | **10** | **21 245** | **February 2019**  
[**Weblogic**](https://github.com/Cymmetria/weblogic_honeypot) | **Weblogic honeypot** | **15** | **7028** | **January 2019**  
  
For the period from May 1st 2018 till project end, the honeypots deployed as part of the SISSDEN sensor network collected over **2,000,000,000** attack events. Note that in the table above, the amounts of events collected by honeypots cannot be easily compared to each other, as some honeypots logged whole sessions as attack events, while other honeypots logged each individual action that was carried out.

#### Report types introduced

[Free victim remediation reports](https://www.shadowserver.org/what-we-do/) to the security community worldwide are the core output of the SISSDEN Project.

The honeypots deployed as part of the core sensor network or partner systems, as well as one of the darknets, have contributed directly to the main objective of the SISSDEN project – delivery of **new free daily victim remediation feeds** to National CSIRTs and network owners via The Shadowserver Foundation.

The Horizon 2020 SISSDEN project enabled **5** new report types, **4** of which are created from honeypot deployments and **1** from a network telescope (darknet) deployment. The full list of new SISSDEN reports sent out by The Shadowserver Foundation is as follows:

  * The [Brute Force](/what-we-do/network-reporting/brute-force-attack-report/) report (on IPs performing brute force attacks coming primarily from IoT botnets)
  * The [HTTP Scanner](/what-we-do/network-reporting/http-scanners-report/) report (on IPs performing HTTP-based scanning and/or exploitation)
  * The [ICS Scanner](/what-we-do/network-reporting/ics-scanners-report/) report (on IPs targeting ICS/SCADA protocol aware devices)
  * The [Amplification DDoS Victim](/what-we-do/network-reporting/amplification-ddos-victim-report/) report (on IPs that are victim of DDoS Amplification Attacks)
  * The [Darknet](/what-we-do/network-reporting/darknet-report/) report (a darknet based report that fingerprints IPs exhibiting Mirai-like activity)



Additionally, an older [Spam-URL](/what-we-do/network-reporting/spam-url-report/) report offered by Shadowserver that includes data from spam messages that have a URL embedded in them has also been enhanced with SISSDEN data.

Up to **31 million** attack events were reported to the report recipients worldwide from May 1st 2018.

While the Horizon 2020 SISSDEN project has now been completed, a number of other Shadowserver honeypot sensor networks are now also contributing to the still active Drone Brute Force Report. The Amplification DDoS Victim report continues to go out courtesy of [CISPA](https://cispa.saarland/). The other new reports will be re-enabled once a new post-Horizon 2020 SISSDEN project honeypot sensor network is up and running (see “Future work” below).

Anyone wishing to subscribe to the above reports and more should apply for our [free daily remediation feeds](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/).

#### Future work

Although the Horizon 2020 SISSDEN Project formally ended in April 2019, Shadowserver has successfully partnered with [NASK](https://nask.pl), one of the original SISSDEN partners, to obtain additional EU funding through the EU CEF calls to build a new sensor network. This deployment will be based on updated SISSDEN technology and a new sensor network should be operational from October 2019. In addition to contributing to feeds, the new network will serve as the basis for offering a **Honeypots-as-a-Service (H-a-a-S)** framework to EU National CSIRTs. Stay tuned for more updates on this new sensor network and H-a-a-S soon! In the meantime, if you would like to contribute honeypot technology to the new project or host a sensor, please [contact us](https://www.shadowserver.org/contact/) to discuss potential collaboration.

  * [ASN](/topics/asn/)
  * [Botnets](/topics/botnets/)
  * [Bots](/topics/bots/)
  * [DDoS](/topics/ddos/)
  * [Geo Locations](/topics/geo-locations/)
  * [Honeypots](/topics/honeypots/)
  * [Malware](/topics/malware/)
  * [Reports](/topics/reports/)
  * [Shadowserver](/topics/shadowserver/)
  * [Statistics](/topics/statistics/)
  * [Technology](/topics/technology/)
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