# BtHoster: Identifying noisy networks emitting malicious traffic through masscan servers

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/bthoster-identifying-noisy-networks-emitting-malicious-traffic-through-masscan-servers/
- **Date :** 2025-06-10

---

#### Key findings

  * By analyzing the networks that most hit our honeypots, we found two autonomous systems named Skynet Network Ltd (AS214295) and Inside Network LTD (AS215476), which we assess with a high level of confidence to be operated by the bulletproof hosting provider BtHoster, which notably offers pre-configured masscan servers. Both networks are based in the United Kingdom, registered by what we believe to be shell companies.
  * Those two networks happen to transit their traffic through a common upstream provider named UAB Host Baltic (AS209605) based in Lithuania. Digging into the IPs of this network, we observed the presence of hundreds of Mirai variants and other C2s malware such as RisePro, Cobalt Strike, Remcos, Moobot, and HookBot.
  * Multiple IPv4 prefixes previously announced by an Iranian network were dispatched to those abusive networks based in the UK and on an additional one in Serbia. On March 5, a security analyst on X reported that all those networks were involved in BGP and bruteforce attacks. The description and geolocation of the previous Iranian autonomous system prefixes were kept on the new ones, making it look like the attacks came from Iran.
  * A company based in Cyprus named IT HOSTLINE LTD (AS44559) known to be a partner of Stark Industries Solutions and managed by the operator of Proxyline, is providing IPv4 prefixes to abusive networks such as Aeza International(AS210644), Global Internet Solutions(207713), and Global Connectivity Solutions(215540).



#### Introduction

Between February and March 2025, our various honeypots received an increasing number of attacks originating from IPs announced by small autonomous systems composed of only a few IPv4 prefixes such as Skynet Network Ltd – AS214295. In addition to bruteforce attacks and massive scanning, various Mirai botnets and other malware command-and-control servers were found to be hosted on those networks.

By searching for information regarding the nature of those autonomous systems and the companies running them, we discovered that some of them were only **rebrands of a known bulletproof hosting provider named btHoster** that created those new entities to **evade bad reputation** and **blocklists**. This provider notably offers pre-configured **masscan** servers with a routing capacity up to **1300kpps** (Kilo Packets Per Second), matching with the high volume of aggressive networks attacks that we observed on our honeypots originating from the autonomous systems that it operates. Such infrastructure tends to be used by most of threat actors such as **IABs** looking for initial accesses in corporate network through exposed and vulnerable assets. For example, _ElectriclQ_ recently reported on members of the ransomware group **Black Basta** that used _Proton66 OOO_ – **AS198953** , a bulletproof provider based in Russia, to host mass internet scanning and automated brute forcing frameworks[1].

As usual, the actors operating these businesses first create a regular company in their country of origin, that will later be blacklisted as the malicious content hosted on their network increases. They then open a **shell company in the United Kingdom** or any offshore country such as Seychelles, to register a new autonomous system. The IPv4 prefixes from their older network are then transferred. Depending on their financial capacities, such networks can sometimes announce new prefixes to completely erase all traces of the malicious activities hosted on their previous network.

As for any autonomous systems, their traffic needs to transit through bigger ISPs to access the internet. We notably found their provider to be based in Lithuania and named _UAB Host Baltic_ – **AS209605**. This provider is indeed used by those smaller bulletproof networks for its upstream capacities.

With this report, we aim at providing an in-depth analysis of these networks, notably on how their infrastructure is operated, and their ramifications that could enable the finding of additional malicious networks in order to entirely block them.

[[1]](/en/#_ftnref1) [_https://blog.eclecticiq.com/inside-bruted-black-basta-raas-members-used-automated-brute-forcing-framework-to-target-edge-network-devices_](https://blog.eclecticiq.com/inside-bruted-black-basta-raas-members-used-automated-brute-forcing-framework-to-target-edge-network-devices)

[](/en/#_ftnref3)[](/en/#_ftnref4)

#### Intrinsec's CTI services

Organizations are facing a rise in the sophistication of threat actors and intrusion sets. To address these evolving threats, it is now necessary to take a proactive approach in the detection and analysis of any element deemed malicious. Such a hands-on approach allows companies to anticipate, or at least react as quickly as possible to the compromises they face.

For this report, shared with our clients in January 2025, Intrinsec relied on its Cyber Threat Intelligence service, which provides its customers with high value-added, contextualized and actionable intelligence to understand and contain cyber threats. Our CTI team consolidates data & information gathered from our security monitoring services (SOC, MDR, etc.), our incident response team (CERT-Intrinsec) and custom cyber intelligence generated by our analysts using custom heuristics, honeypots, hunting, reverse-engineering & pivots.

Intrinsec also offers various services around Cyber Threat Intelligence:

  * Risk anticipation: which can be leveraged to continuously adapt the detection & response capabilities of our clients' existing tools (EDR, XDR, SIEM, …) through: 
    *       * **an operational feed of IOCs based on our exclusive activities.**
      * **threat intel notes & reports, TIP-compliant.**
  * Digital risk monitoring: 
    *       * **data leak detection & remediation**
      * **external asset security monitoring (EASM)**
      * **brand protection**



For more information, go to [htbqccsz.elementor.cloud/en/cyber-threat-intelligence/](http://www.intrinsec.com/en/cyber-threat-intelligence/).

Follow us on [LinkedIn](https://www.linkedin.com/company/intrinsec/) and [X](https://twitter.com/Intrinsec)

#### Articles by category 

Select a category News Vulnerability notice Analysis Report CERT SSI Council Cyber Threat Intelligence Engineering Safety Assessment Event Partnership Research and Development Red Teaming part-time CISO Soc as a Service SOC Operational Security Testimonials Penetration test Threat Intelligence Report Security Watch