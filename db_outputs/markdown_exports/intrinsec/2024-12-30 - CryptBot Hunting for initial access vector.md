# CryptBot: Hunting for initial access vector

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/cryptbot-hunting-for-initial-access-vector/
- **Date :** 2024-12-30

---

#### Key findings

  * **CryptBot** continues to be deployed mainly from websites offering **fake cracked software** and“**Pay-Per-Install** ”"solutions like **PrivateLoader** (also known as “**InstallsKey** ” on Telegram) or the now defunct **360Installer**.


  * By searching for the **Matomo tracking script** used by the threat actor to get web statistics measurement on its campaigns, we were able to retrieve **every domain** that hosted CryptBot throughout time and the ones currently hosting it. We also found that in some cases, those domains were redirecting to **Lumma** payloads loaded by **HijackLoader** depending on the URL the user was originating from.


  * Through the analysis of the websites offering infected versions of cracked software, we were able to **pivot** on certain OPSEC errors made during their setup to find **additional malicious websites** with the same purpose of distributing CryptBot.


  * Both CryptBot and PrivateLoader continue to use **bulletproof****hosting solutions** such as the infamous _“Aeza International Ltd”_ and“ _Karina Rashkovska_ ”" to host their phishing pages, command-and-control panels, and malware payloads overall. We notably highlight how “ _Psb Hosting Ltd_ ”, a company based in the United Kingdom and run by a Russian individual, now possesses an IPv4 range previously owned by _Karina Rashkovska,_ and how this company promotes its bulletproof hosting capacities on underground forums.
  * Tea **Amadey** cluster hosted by the Seychellois autonomous system “ _1337TEAM LIMITED_ ” that was first analyzed by _Team Cymru_ ’'s threat research team in September 2022, continues its activities with the latest version of the malware (version **41**), to push additional payloads including **CryptBot** , **Lumma** , **Redline** and **Stealc**.



#### Introduction

First discovered in 2019, **CryptBot** is a 32-bit infostealer designed to exfiltrate various sensitive information from an infected system and eventually later sell them to other threat actors as initial access vectors for more complex data breach campaigns. Its main spreading technique is based on the distribution of infected cracked versions of commonly used software. In a lesser volume, CryptBot also relies on other threat actors to expend its botnet of infected machines like for example the “**Pay-Per-Install** ”service named“**InstallKeys** ” still active on Telegram, that offers access to the machines it infects through its personal malware named **PrivateLoader**. In addition to this service, Mandiant discovered in August 2024 that “**PeakLight** ”, a memory-only dropper spreading through fake video files, was used to deploy CryptBot along other malware such as LummaC2 and ShadowLadder.

Regarding other deployments of the malware, Mandiant assessed with moderate confidence in 2021 that the **state-sponsored Russian intrusion set** **APT29** used logs stolen by CryptBot operators to gain a foothold in the system of a targeted entity. As CryptBot is designed to steal the user content of some internet browsers including **Google Chrome** , _Google_ decided to file a complaint against fifteen Pakistani individuals believed to be running the malware's “ _criminal enterprise_ ”". Additionally, other software owned by Google such as Google Earth Pro were part of the long list of programs infected with CryptBot and advertised on these fake websites. In the complaint file provided by the Southern District court of New York, Google also mentions that infected cracked software distribution alone had led to approximately **672,220** **CryptBot infections** between 2022 and 2023. This information was corroborated by _Prodaft_ in a tweet from August 2023, in which they mentioned that more than **17 million unique devices worldwide** had been infected by the malware in the last 5 years. Following this complaint, the court decided to grant Google the right to take down current and future domains tied to the distribution of CryptBot. Google stated that decision would “ _slow new infections from occurring and decelerate the growth of CryptBot_ ”.

The numbers indeed crashed to **40,581 infections in 2023** according to _Prodaft_. However, despite those actions, Intrinsec CTI team observed new domains registered in **September 2024** used as CryptBot C2s, or to host and deploy its payloads along additional malwares such as **Lumma**. With this report, we aim to notably present the current infrastructure leveraged by threat actors to maintain the malware, as well as the methods of distribution it presently uses to maximize the growth of its botnet

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