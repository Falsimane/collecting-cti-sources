# From espionage to PsyOps: Tracking operations and bulletproof providers of UACs in 2025

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/from-espionage-to-psyops-tracking-operations-and-bulletproof-providers-of-uac/
- **Date :** 2025-03-28

---

#### Key findings

  * Russia-aligned intrusion sets **UAC-0050** and **UAC-0006** actively continue to launch **financially** and **espionage motivated spam campaigns** in both January and February 2025, against worldwide entities, but with a strong focus on Ukraine. The nature of the targets ranked from **governmental entities** to critical companies operating in the **defense** gold **energy** and **gas** industry. Additionally, some **journalists** and the Ukrainian branch of **NGOs involved in the war** have also been targeted by those campaigns
  * **Psychological operations** , and in particular **bomb threats** and **terrorist threats** were used in mails sent to Ukrainian entities and allies of the country such as **Switzerland** , **Germany** , **Poland** , and **France** throughout December 2024. Some of those mails shared similarities with the UAC-0050 branch operating PsyOps under the “Fire Cells Group” brand.
  * Since the beginning of 2025, UAC-0050 switched to **NetSupport Manager** for its malware operations in both January and February. The intrusion sets notably used **Ukrainian IPs managed criminal networks **such **Karina Rashkovska** and **Virtualine**(AS215789 and AS214943), to host the infrastructure of its latest campaigns. Virtualine currently leverages a shell company based in Kentucky named Railnet LLC of which the registered agent, White Label Networks LLC, is an Israeli company known for its links with illicit hosting networks
  * IPs from **Global Connectivity Solutions LLP**(AS215540), a UK-based autonomous system leveraged by UAC-0006, are currently routed by Stark Industries (AS44477). This AS could be linked to another **Russia-based bulletproof network , Global Internet Solutions LLC **(AS207713), from which IPs were moved to this new infrastructure. Both serve as legal fronts for the bulletproof hosting provider “**4vps.su** ”". IPs from those networks have been used by ransomware groups such as **Black Basta** , **Cactus** and **RansomHub**. Additionally, the company operating this network **shares the same two LLP officers **based in **Seychelles** as **Zservers** , a BPH provider that was recently **sanctioned by the US Treasury **for its collaboration with the ransomware group **LockBit**. We notably assess with a high level of confidence that some IPv4 prefixes announced by Zservers' autonomous system were moved to new abusive networks located in Russia or offshore countries, including **AS213194** , **AS61336** and **AS213010**.



#### Introduction

In addition to UAC-0010, UAC-0050 and UAC-0006 were the most active cyber threat clusters identified by the Cyber Incident Response Center of Ukraine in 2024, representing respectively 17,5% (99 incidents) and 30,8% (174 incidents) of observed incidents.[[1]](https://scpc.gov.ua/api/files/72e13298-4d02-40bf-b436-46d927c88006)

Regarding UAC-0050, CERT-UA describes it as a “mercenary group associated with Russian law enforcement agencies”"They also assess with a high level of confidence that they operate their activities under an agency named “DaVinci Group”, created a few days before the Russian invasion in 2022.[[2]](https://cert.gov.ua/article/6277822) Additionally, they state that UAC-0050 operators are mainly focused on financial theft: “[UAC-0050] made at least 30 attempts to steal money from the accounts of Ukrainian enterprises and individual entrepreneurs by generating/forging financial payments through remote banking systems. The amount of thousands such payments varies from tens of to several million hryvnias [monetary unit of Ukraine].”[[3]](https://cert.gov.ua/article/6281009) In some cases, as evidenced by the results of computer forensic investigations operated by the CERT-UA, it may take no more than an hour from the moment of the initial attack to the theft of the funds.

In addition to their financial motives, UAC-0050 has been operating information theft (cyber espionage) and psychological operations. The group has also been linked to other intrusion sets, such as UAC-0096.[[4]](https://cert.gov.ua/article/3863542) In this report, we notably highlight how this intrusion set switches from one malware to the other such as Remcos, Load and NetSupport Manager, throughout the campaigns it operates. We also expose how it historically used SystemBC to manage the proxies located in Ukraine to avoid blocklists that would launch the malspam campaigns.

UAC-0006 is a financially motivated threat actor active since at least 2013. They primarily target Ukrainian organizations, particularly accountants' computers (which are used to support financial activities, such as access to remote banking systems), with phishing emails containing the SmokeLoader malware. As for UAC-0050 operators, this intrusion set creates unauthorized payments (in some cases using an HVNC bot directly from the compromised computer).[[5]](https://cert.gov.ua/article/4555802)

Based on the infrastructure analysis of these campaigns, we assess with a high level of confidence that both intrusion sets strongly rely on bulletproof hosting providers that often move their infrastructure through different networks and recreate new companies fronted by offshore organizations to blur their tracks. These providers also depend on bigger networks transiting their traffic to the internet, such as Stark Industries (AS44477), precisely chosen for their tendency to turn a blind eye on the activities of their clients. While investigating UAC-0006's infrastructure, we noticed that it leveraged IPs from AS215540 – Global Connectivity Solutions LLP. Based in the United Kingdom, both of its LLP officers are front companies based in Seychelles that are also leveraged by Zservers, a Russia-based bulletproof hosting services provider that was recently sanctioned by the US Treasury department for its role in supporting LockBit ransomware attacks.[[6]](https://home.treasury.gov/news/press-releases/sb0018)

**With this report, we aim at providing an in-depth analysis of both inrusion sets' latest TTPs and infrastructure, used to operate their spamming campaigns that were not reported by CERT-UA, between the end of 2024 and early 2025.**

[](/en/#_ftnref3)[[1] https://scpc.gov.ua/api/files/72e13298-4d02-40bf-b436-46d927c88006](https://scpc.gov.ua/api/files/72e13298-4d02-40bf-b436-46d927c88006\[1\]\[1\])

[[2] https://cert.gov.ua/article/6277822](/en/#_ftnref3)

[[3] https://cert.gov.ua/article/6281009](/en/#_ftnref3)

[[4] https://cert.gov.ua/article/3863542](/en/#_ftnref4)

[[5] ](/en/#_ftnref4)[https://cert.gov.ua/article/4555802 ](https://cert.gov.ua/article/4555802)

[[6] https://home.treasury.gov/news/press-releases/sb0018](/en/#_ftnref4)

#### Intrinsec's CTI services

Organizations are facing a rise in the sophistication of threat actors and intrusion sets. To address these evolving threats, it is now necessary to take a proactive approach in the detection and analysis of any element deemed malicious. Such a hands-on approach allows companies to anticipate, or at least react as quickly as possible to the compromises they face.

For this report, shared with our clients in July 2023, Intrinsec relied on its Cyber Threat Intelligence service, which provides its customers with high value-added, contextualized and actionable intelligence to understand and contain cyber threats. Our CTI team consolidates data & information gathered from our security monitoring services (SOC, MDR, etc.), our incident response team (CERT-Intrinsec) and custom cyber intelligence generated by our analysts using custom heuristics, honeypots, hunting, reverse-engineering & pivots.

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