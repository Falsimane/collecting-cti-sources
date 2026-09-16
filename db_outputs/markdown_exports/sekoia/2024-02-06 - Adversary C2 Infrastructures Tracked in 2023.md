# Adversary C2 Infrastructures Tracked in 2023

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/adversary-c2-infrastructures-tracked-in-2023
- **Date :** 2024-02-06

---

## Context

Throughout 2023, Sekoia.io’s Threat Detection & Research (TDR) team actively tracked and monitored adversary C2 infrastructures set up and used by lucrative and state-sponsored intrusion sets to carry out malicious cyber activities.

Our analysts identified more than **85,000 IP addresses used as C2 servers in 2023** , an increase of more than 30% compared to 2022. These IP addresses were found through searches based on proactive scanning for more than **260 threats, such as OST servers, malware C2, phishing clusters, delivery infrastructure** , _etc_.

## Overview of the main threats tracked by Sekoia.io C2 Trackers

We initiated our Sekoia.io C2 Trackers project at the end of 2019 to enhance our monitoring capabilities. Since the project was set up, it has undergone significant evolution, playing a crucial role in our proactive tracking of malicious activities. Sekoia.io C2 Trackers substantially contributes to our capacity to detect possible compromises within the network traffic of assets monitored by our Sekoia.io SOC platform. While in this part of the report we focus on IP addresses we spotted, our team also identifies malicious URLs and domains.

### Evolution since 2022 TOP 10

![Number of detected IP addresses between 2020 and 2023. Source: Sekoia.io C2 Trackers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5ac_6a92a2ade17eff730b654a0c_6a2a7cd3c5337e0183cf0ae2.webp)

Number of detected IP addresses between 2020 and 2023. Source: Sekoia.io C2 Trackers

Number of detected IP addresses between 2020 and 2023 

The TOP 10 threats monitored in 2022 remained highly active throughout 2023. Notably, **we observed a significant increase for Ramnit and EvilProxy servers**. These two threats were only added to our tracking capabilities at the end of 2022, which explains the great difference in tracking when comparing the two periods.

Despite its [takedown announced in August 2023](https://www.europol.europa.eu/media-press/newsroom/news/qakbot-botnet-infrastructure-shattered-after-international-operation), **Qakbot botnet was more active over this year than the previous ones**. Moreover, we identified some active servers even after the takedown operation, which is consistent with [Microsoft](https://twitter.com/MsftSecIntel/status/1735856754427047985)’s observations.

### Offensive Security Tools - OST

![OST continues to be very popular among threat actors. Here is the ranking of the top 10 OST in 2023. Source: Sekoia.io C2 Trackers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e04b4041c69343859b_6a92a301693fca262e1b5c51_6a2a7cd3c5337e0183cf0aee.webp)

OST continues to be very popular among threat actors. Here is the ranking of the top 10 OST in 2023. Source: Sekoia.io C2 Trackers

The TOP 10 ranking represented above did not evolve much from 2022, as **OST continued to be highly popular among threat actors**. According to our observations, no game-changing OST was released during 2023, yet the well-known, most used ones, continued to be updated during the year. As of late 2023, **CobaltStrike is still a first choice from cybercriminals** especially given its customization possibilities with MalleableC2. 

### Malicious code

![TOP 10 Malicious code in 2023. Source: Sekoia.io C2 Trackers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e04b4041c69343859e_6a92a2fe2e47a1e9fe0dd1d7_6a2a7cd3c5337e0183cf0ae5.webp)

TOP 10 Malicious code in 2023. Source: Sekoia.io C2 Trackers

Two newcomers have made their place to this TOP 10:

  * NakedPages
  * StealC



We will detail the work done on these threats in later parts of this report.

### NakedPages, Gophish, EvilProxy: Phishing is king

In 2023, Sekoia.io observed a trend towards the **democratisation of phishing kits capable of relaying MFA challenges**. While this technique was already implemented in open-source tools such as _evilginx_ , the emergence of [Phishing-as-a-Service](/blog/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1) offerings, such as EvilProxy and NakedPages, progressively reduced the technical difficulty of conducting this type of _adversary-in-the-middle_ attacks, making them accessible to a wider range of threat actors.

As organisations gradually deprecate legacy authentication protocols and roll-out multi-factor authentication, _credential stuffing_ and _password spraying_ attacks have become less effective, leading threat actors to favour this new approach. In the second half of the year, our XDR telemetry shows that _adversary-in-the-middle_ phishing is the leading source of [Microsoft 365](/blog/userauthenticationmethod-microsoft-365-decode) account compromise.

A growing trend among Phishing-as-a-Service platforms is to hide infrastructure behind Cloudflare’s content distribution network, making proactive identification more challenging. **The most prominent kits tracked by Sekoia.io that rely on this method are Caffeine, Dadsec, and Tycoon 2FA,** the latest being relatively new as it emerged in the last quarter of the year.

## Follow up on 2023 publications

In this second part of the report, we illustrate the results of our continuous monitoring of 2023 investigations and share our analysis of the results and trends related to our tracking routine.

### Unveiling of a large resilient infrastructure distributing information stealers

In the first month of 2023, our team published a report detailing a large and resilient infrastructure used to distribute Raccoon and Vidar stealers. At the time of publication, the associated infection chain leveraged an infrastructure of over 250 domains hosting malicious SEO poisoned websites, redirection domains and web pages providing instructions for downloading the disguised malware. In January 2023, Sekoia.io reported more than a hundred malicious domains to registrars Namecheap, Namesilo and OVH, resulting in a partial takedown of the distribution infrastructure.

Subsequently, the TDR team continued monitoring the infrastructure and found over a hundred new domains that were active during 2023. We observed that **the intrusion set consistently maintained and updated its infrastructure** , including new domain names, IP addresses and websites. These changes involved the introduction of new templates for fake cracked software and download instruction websites, as well as the addition of new redirect URL patterns.

A noteworthy change also pertained to the malware family distributed by this infrastructure, as it transitioned to the prevalent Lumma stealer. **This shift aligns with the observed trend of threat actors increasingly adopting Lumma stealer** , as identified by Sekoia.io through our monitoring of the cybercriminal ecosystem and C2 infrastructures.

Our predictions regarding the medium-term resilience of this large infrastructure have been confirmed. We will continue to monitor the use of fake download pages of all sorts.

### Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity

In January 2023, through our Dark Web monitoring routine, Sekoia.io identified a new information stealer advertised as Stealc. The malware expanded quickly and became one of the most widespread infostealers of 2023. 

Following our analysis published in February 2023, we actively tracked Stealc C2 servers through our Sekoia.io C2 Trackers project. Over the year, we confidently identified **over 680 unique IP addresses hosting a Stealc C2** , with a peak of activity in August 2023 with **more than 120 active C2 simultaneously** , as shown in the figure below. Notably, we assess with high confidence that the Stealc C2 infrastructure is decentralised, indicating that each Stealc customer is responsible for hosting its own C2 server. Consequently, the number of active C2 servers provides a reasonable approximation of the number of threat actors using Stealc at any given time.

![Evolution of active Stealc C2 infrastructure / C2 servers in 2023. Source: Sekoia.io C2 Trackers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e04b4041c6934385a4_6a92a3003e6167cebbf6337b_6a2a7cd3c5337e0183cf0aeb.webp)

Evolution of active Stealc C2 infrastructure / C2 servers in 2023. Source: Sekoia.io C2 Trackers

Our findings revealed that the Stealc C2 infrastructure is constantly and rapidly renewed, as the majority of detected IP addresses were not active for more than two consecutive months. **Infrastructure updates is a common deliberate tactic employed by adversaries to evade network-based detection** , strategically staying ahead of security measures and minimising the risk of exposure.

Of note, TDR analysts identified three major modifications in the default configuration of Stealc C2 servers, around March, July and December 2023, which led us to update our heuristics so that we can continue to monitor them proactively. Two main hypotheses explaining these changes can be considered. Firstly, it is highly likely that the **Stealc operator hardened the C2 server configuration** , to prevent their infrastructure from being easily illuminated, as discussed in the [FLINT 2023-033 - Tracking the C2 infrastructures of the prevalent infostealer families](https://app.sekoia.io/intelligence/objects/report--1b3f4bf9-e607-48ca-a7a6-f0abb972aba2). Secondly, it is plausible that the **changes are a result of updates in the functionalities of Stealc C2 servers** , without any intention to fortify their infrastructure.

### Malvertising, fake websites and drive-by-download

In April 2023, our analysis of the Russian-speaking infostealer ecosystem delved into prevalent distribution techniques leveraged to spread malware. Among them, the Sekoia.io **TDR team observed a significant increase in the use of malvertising to promote malicious websites impersonating legitime ones** , which often led the victim to download an infostealer or a loader, disguised as a software installer.  
Afterwards, we started to **track the fake websites impersonating some of the most targeted software** , including AnyDesk, Brave, ChatGPT, Slack, WinRAR and Zoom. Our tracking heuristics mainly identify websites using content, design, title or favicon similar to the legitimate ones but with non-official domain names. This approach led to finding typosquatting domains redirecting users to download malware. Indicator of Compromises (IoCs) collected by the Sekoia.io C2 Trackers projects are accessible to our customers in the infrastructure object “[Landing pages impersonating legitimate software sites to distribute malware](https://app.sekoia.io/intelligence/objects/infrastructure--1bee45cb-4fa6-4192-ac14-cab58fdff723)”.

Our observations unveiled the continuous use of these TTPs throughout 2023, with a peak occurrence in the first half of the year. This decline is likely due to Google reinforcing security measures related to their advertising service. Consequently, conducting a successful malvertising campaign now demands a higher level of sophistication.

When monitoring the fake websites trends in the last semester of 2023, we noticed an uptick in the number of fake video games download websites. Following our report dedicated to this campaign, we identified more malware distributed by those websites: **CrealStealer, CStealer in addition to BByStealer, Nova Stealer, Epsilon Stealer and Doenerium**. 

By the end of December 2023, we identified more than 50 new domains mimicking games websites being used by the attackers.

### ClearFake: a newcomer to the “fake updates” threats landscape

In October 2023, the Sekoia.io TDR team published an in-depth analysis of the emerging “fake updates” threat ClearFake, as named by the cybersecurity researcher Randy McEoin. **ClearFake is a malicious JavaScript framework deployed on compromised websites** to deliver further malware using the drive-by download technique.

Our analysis introduced a heuristic based on the common name of the TLS certificate to proactively track ClearFake C2 servers hosting malicious JavaScript payloads. At the time of writing, this heuristic resulted in 6 IP addresses controlled by ClearFake operators.

Subsequently, we continued to monitor the ClearFake infrastructure and detected changes in the TLS common name (CN), as well as in the URL patterns. The CN values were as follows:

**TLS common name**| **Date of first use**  
---|---  
      
    
    921hapudyqwdvy[.]com

| 2023-09-07  
      
    
    02w65ijjohr1frm[.]com

| 2023-10-19  
      
    
    acotechgh[.]com

| 2023-11-28  
  
TLS common name used for ClearFake infrastructure 

The IP addresses resolve several domain names used by the ClearFake framework to retrieve the next-stage malicious payloads. Since the beginning of our monitoring, **we collected over 80 C2 domain names**.

At the end of December 2023, our observations indicated that the ClearFake C2 infrastructure remained active, with a few websites compromised to inject the ClearFake framework. We assess with high confidence that the ClearFake operator has stopped updating the infrastructure, potentially redirecting its focus to other activities.

### DDoS attacks: monitoring of the DDoSia project target infrastructure NoName057(16)

In 2023, DDoSia became a familiar name in the hacktivist world. This tool designed to facilitate Distributed Denial of Service (DDoS) attacks **was and is still used by the pro-Russian hacktivist group**[**NoName057(16)**](/blog/following-noname05716-ddosia-projects-targets)**as of January 2024.** Their focus involves attacks towards entities perceived to be associated with countries critical to the Russian invasion of Ukraine. Since May 2023, Sekoia.io analysts automated**the collection of targets in real time**. Although the list of victims is obfuscated for users of the malicious software, a thorough analysis of this list provides insights into the malicious group's intentions towards several countries, particularly NATO member countries . We observed a constant growth of user numbers: the group now has over 60,000 participants, almost double compared to numbers at the beginning of 2023, and they are still increasing.

Sekoia.io's analysts use both C2 Trackers and manual monitoring to track the infrastructure delivering targets to its users, due to the dual behavior of the infrastructure throughout 2023. 

For most of the year until November 2023, the C2 servers were consistently hosted in Latvia. During this period, we detected five IP address changes, typically occurring at intervals of two months or more.

However, on 26 November 2023, a new version was released, introducing a new target transmission mechanism. By using reverse engineering techniques, Sekoia.io's analysts were quickly able to update our real-time monitoring of the targets being transmitted. In January 2024, we noticed **NoName057(16)'s difficulties in maintaining the stability of their C2 servers over time**. With each of these changes, the group is required to republish the new version on its Telegram channel, necessitating download and installation by users to continue participating in the attacks, and receiving remuneration. Despite occasional unavailability of the DDoS infrastructure for a few hours, this has not stopped the NoName057(16) group from claiming responsibility for their daily attacks with a global impact. For the year 2023, we have seen the following countries targeted, as shown in the diagram below.

![Countries targeted by DDoSia in 2023. Source: Sekoia.io C2 trackers project](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e04b4041c6934385aa_6a92a302693fca262e1b5e89_6a2a7cd3c5337e0183cf0af3.webp)

Countries targeted by DDoSia in 2023. Source: Sekoia.io C2 trackers project

Since our previous analysis of the most targeted countries, included in the blogpost on NoName057(16), there has been no change in the TOP 3 most targeted countries. **Ukraine, Poland and Lithuania continue to be highly impacted**. Although the focus is on NATO countries, we observed that the attacks are **mainly directed at Eastern European countries** , including Finland and the Czech Republic. The next in the ranking is Western Europe, with Germany, Italy and France. These countries are primarily targeted due to their repeated announcements throughout 2023 regarding plans to provide strategic aid to Ukraine. However, the group does not hesitate to target countries relevant to its current events, even if the subject is unrelated to the conflict in Ukraine. The following image shows the group's claim of DDoS attacks on French city websites on 25 January 2024, during farmers' protests.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e04b4041c6934385a1_6a92a2ffdae089660dfc6231_6a2a7cd3c5337e0183cf0ae8.webp)

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e04b4041c6934385a7_6a92a30369291914889995d9_6a2a7cd3c5337e0183cf0af6.webp)

The group’s emphasis on exploiting current events within a country underscores its willingness to use any pretext to attempt to destabilise a nation. As the number of users increases over time, this threat to the reputation of companies and public authorities remains one that we will closely monitor.

## Conclusion

The thorough tracking and monitoring efforts led by Sekoia.io's Threat & Detection Research (TDR) team throughout 2023 have provided critical insights into the evolving landscape of cyber threats. The significant increase in identified C2 servers, totaling more than 85,000 IP addresses, underscores the escalating complexity of malicious cyber activities. The evolution of our C2 Trackers project, initiated in late 2019, has played a pivotal role in enhancing our proactive tracking capabilities, contributing substantially to our ability to detect compromises within the network traffic of assets monitored by the Sekoia.io SOC platform.

The democratisation of phishing kits, particularly those capable of relaying Multi-Factor Authentication (MFA) challenges, has become a dominant trend. Phishing-as-a-Service platforms like EvilProxy and NakedPages have lowered the technical barriers for conducting _adversary-in-the-middle_ attacks, with a notable rise in Microsoft 365 account compromises observed in the latter half of the year.

Our continuous monitoring and analysis of 2023 publications have unveiled resilient infrastructures distributing information stealers, such as the persistent use of malvertising, fake websites, and drive-by-download techniques.

We anticipate a consistent growth of threats and an increasing number of OST users in 2024, so Sekoia.io remains committed to closely monitoring and adapting to the ever-changing cybersecurity landscape. Our insights and proactive measures aim to equip organisations with the knowledge and tools needed to mitigate risks and safeguard against emerging cyber threats.