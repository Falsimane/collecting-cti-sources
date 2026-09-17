# Shadow syndicate infrastructure illumination

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/shadow-syndicate-infrastructure-illumination/
- **Date :** 2025-07-30

---

#### Key findings

We found a new heuristic allowing us to keep tracking the attack infrastructure of the infamous ShadowSyndicate known to leverage a wide range of top-tier Ransomware-as-service.

  * ShadowSyndicate used the same Secure Shell (SSH) fingerprint on many servers (138 at the time of writing). It matches a previous TTP reported by GroupIB in September 2023
  * ShadowSyndicate works with numerous ransomware groups and affiliates of ransomware programs including RansomHub
  * We found connections between ShadowSyndicate infrastructure and Cl0p/Truebot substantiating previous findings of GroupIB
  * We found connections between ShadowSyndicate infrastructure and Citrix Bleed attack infrastructure that spread Lockbit ransomware
  * We assess with moderate confidence that ShadowSyndicate has access to a network of private bulletproof hosts (BPHs) in Europe that exhibit traits of Intelligence Agencies hosting (IAH)
  * The global resilience against takedowns is ensured via a high level of imbrication of those BPHs, registered in offshore jurisdiction, spanning different countries but operated from Russia. We found links of interests with the Kremlin for some of them
  * BPHs are blurring lines by appearing as VDS | VPS | VPN | (residential) proxy platforms and even sometimes an additional obfuscation layer via a DDOS protection provider
  * With lower confidence, we found a hack and leak operation targeting Hunter Biden, the son of the former President of the United States, seeking to influence 2024 presidential elections. The goal is to weaken representative governments perceived as democracies and weaken unaligned candidates with the Kremlin's interests. Using proxies such as ransomware programs and/or an IAB shields from prosecution in return for “plausible deniability for state-backed cyber operations
  * We found connections between ShadowSyndicate infrastructure and Amos Stealer infrastructure (moderate confidence) as well as though with lower confidence, with ToneShell backdoor



**As of this writing, the attack infrastructure remains active, with threat actors continuously scanning for vulnerabilities and distributing new malicious payloads to victims.**

We would like to express our sincere appreciation for our collaboration with [Group-IB](https://www.group-ib.com/), for their peer reviewing, insightful discussions, and valuable contributions. The opportunity to cross-correlate data using their telemetry has been especially valuable, enabling us to validate findings and enhance the overall accuracy and depth of our analysis. This partnership underscores the importance of collective intelligence in tackling today's complex threat landscape.

NB Names of persons and organizations within this presentation are included for completeness. No implication of guilt or association should be implied.

##### Introduction

ShadowSyndicate (aka Infra Storm [GroupIB](https://www.group-ib.com/blog/shadowsyndicate-raas/)) is a recent intrusion set reportedly active since July 2022. It has demonstrated the use of multiple top tier **Ransomware-as-a-Service** (RaaS) brands such as **AlphaV/Blackcat, Lockbit, Play, Royal, Cl0p, Cactus and Ransomhub**. GroupIB in 2023 conjectured that **ShadowSyndicate** is more likely a **new Ransomware-as-a-Service** (RaaS) affiliate rather than an **Initial access broker** (IAB).

Overlaps were also found with **TrickBot, Ryuk/Conti, FIN7** , and [TrueBot](https://thehackernews.com/2023/06/alarming-surge-in-truebot-activity.html) (also known as [Silence.Downloader](https://malpedia.caad.fkie.fraunhofer.de/details/win.silence)) malware operations (linked to the **Silence group** [overlapping](https://thehackernews.com/2023/06/alarming-surge-in-truebot-activity.html) **Russian intrusion set Evil Corp** [directed by FSB](https://www.nationalcrimeagency.gov.uk/who-we-are/publications/732-evil-corp-behind-the-screens/file) to conduct cyber espionage against NATO allies).

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



Follow us on [LinkedIn](https://www.linkedin.com/company/intrinsec/) and [X](https://twitter.com/Intrinsec)

[ Download the full report content ](https://www.intrinsec.com/wp-content/uploads/2025/10/TLP-CLEAR-31072025-ShadowSyndicate-infrastructure-illumination-EN.pdf)

#### Articles by category 

Select a category News Vulnerability notice Analysis Report CERT SSI Council Cyber Threat Intelligence Engineering Safety Assessment Event Partnership Research and Development Red Teaming part-time CISO Soc as a Service SOC Operational Security Testimonials Penetration test Threat Intelligence Report Security Watch