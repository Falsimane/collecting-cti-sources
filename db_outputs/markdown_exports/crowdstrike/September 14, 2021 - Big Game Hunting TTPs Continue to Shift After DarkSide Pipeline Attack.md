# Big Game Hunting TTPs Continue to Shift After DarkSide Pipeline Attack

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-big-game-hunting-ttps-shifted-after-darkside-pipeline-attack/
- **Date :** September 14, 2021

---

# Big Game Hunting TTPs Continue to Shift After DarkSide Pipeline Attack

September 14, 2021

• [ CrowdStrike Intelligence Team](/en-us/blog/author.crowdstrike-intelligence-team/ "Posts by CrowdStrike Intelligence Team") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


The eCrime ecosystem is an active and diverse economy of financially motivated threat actors

engaging in a myriad of criminal activities to generate revenue. With the [CrowdStrike eCrime Index](https://adversary.crowdstrike.com) (ECX), CrowdStrike’s Intelligence team maintains a composite score to track changes to this ecosystem. The ECX is composed of several key observables covering different aspects of criminal activity that are combined using a mathematical model. In recent weeks, the Intelligence team observed a notable shift in [big game hunting (BGH)](https://www.crowdstrike.com/cybersecurity-101/cyber-big-game-hunting/) activity and tactics, techniques and procedures (TTPs) that resulted in a downward trend of the ECX. As noted in a previous CrowdStrike Intelligence blog, the intense attention surrounding the Colonial Pipeline and JBS incidents had a significant impact [on the criminal marketplace and the political landscape](/en-us/blog/how-ransomware-adversaries-reacted-to-the-darkside-pipeline-attack/). Get more Intel updates on the latest eCrime activity and TTPs at Fal.Con, our annual cybersecurity conference, Oct. 12-14 — [register for free today](/en-us/falcon/).

## ECX Suggests Downward Trend in Ransomware Operations Following Colonial Pipeline Attack

By the time of the Colonial Pipeline attack on May 7, 2021, observed BGH ransomware incidents had reached a yearly high. However, publicly observable BGH activity declined throughout early June 2021, immediately after the incident, amid reports of mounting U.S. pressure to pursue BGH actors. A similar decline was also observed in the number of specific leaks posted to adversaries’ dedicated leak sites (DLS). Despite the decline in the ECX, there has been sustained ransomware activity, likely indicating that a number of adversaries are remaining active despite the dismantling of other groups.![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/09/Picture1-4.png)

## BGH Actor Developments

BGH adversaries responded to the Colonial Pipeline ransomware incident and the resulting widespread media coverage in many ways. Some named actors shuttered [ransomware-as-a-service (RaaS)](/en-us/cybersecurity-101/ransomware/ransomware-as-a-service-raas/) affiliate programs — at least publicly — while others have continued deploying ransomware.

[CARBON SPIDER](https://falcon.crowdstrike.com/intelligence/actors/carbon-spider) (operators of _DarkSide_ ransomware) continues to create active command-and-control (C2) servers to deploy their _Domenus PS_ backdoor and _Cobalt Strike_ post-exploitation framework. The activation of new C2 servers demonstrates that CARBON SPIDER has not halted activities despite allegedly losing control of _DarkSide_ -related infrastructure and having their ransomware funds seized by the U.S. government.1 However, in late July 2021, CrowdStrike Intelligence observed a new ransomware called _BlackMatter_ being distributed. Code overlaps indicate that _BlackMatter_ is highly likely the successor of CARBON SPIDER’s _DarkSide_ ransomware. CARBON SPIDER has also created a Linux version of _BlackMatter_ that resembles the Linux version of _DarkSide_ in multiple ways. After taking a short break, CARBON SPIDER reinstated their BGH operations involving this RaaS and have stated that they have an interest in purchasing and executing unauthorized access to corporate networks. [RIDDLE SPIDER](https://falcon.crowdstrike.com/intelligence/actors/riddle-spider) (operators of _Avaddon_ ransomware) closed down their operations in late June. Earlier in June 2021, media sources allegedly received emails containing a password and links to 7zip files containing _Avaddon_ ransomware decryption keys.2 RIDDLE SPIDER’s DLS also went offline in June. While CrowdStrike Intelligence cannot confirm RIDDLE SPIDER’s motivations for closing down the _Avaddon_ RaaS, the decision was likely influenced by the Colonial Pipeline incident and its resulting effects throughout the ransomware industry. [GRACEFUL SPIDER](https://falcon.crowdstrike.com/intelligence/actors/graceful-spider) had several members of their group arrested on June 16, 2021, by a joint international law enforcement operation.3 These members were involved in laundering cryptocurrency funds acquired through the use of GRACEFUL SPIDER’s _Clop_ ransomware.

The immediate impact to GRACEFUL SPIDER operations resulting from these arrests is currently unclear. GRACEFUL SPIDER’s DLS site remains active after the arrests, with two new listings in June, indicating they have not ceased their activity. [PINCHY SPIDER](https://falcon.crowdstrike.com/intelligence/actors/pinchy-spider) (developers and operators of the popular _REvil_ RaaS) continued operating at a high pace throughout June and early July 2021, and the group introduced a new ransomware named _REvix,_ which is used to target ESXi and Linux environments. However, on the morning of July 13, 2021, PINCHY SPIDER’s _REvil_ infrastructure supporting their DLS and payment portal went offline. On the same day, the forum administrator of the Russian-language criminal forum XSS banned the actor _Unknown_ (aka _UNKN_), who has acted as the public spokesperson for PINCHY SPIDER since 2019. PINCHY SPIDER had released _REvil_ version 2.08 a few days prior, confirming the ransomware was under active development, and version 1.2 of _REvix_ was observed on July 23.

On Sept. 7, after an approximately three month hiatus, CrowdStrike Intelligence observed PINCHY SPIDER’s _REvil_ infrastructure come back online. Financial activity in terms of BTC transactions from previously identified _REvil_ addresses was also detected on Sept. 5. On June 4, a sample of [INDRIK SPIDER](https://falcon.crowdstrike.com/intelligence/actors/indrik-spider)’s _Hades_ ransomware was identified using the name _PAYLOADBIN_ , similar to _Babuk Locker_ ’s DLS site Payload.bin. INDRIK SPIDER likely switched the names in an effort to avoid attribution by law enforcement and therefore avoid Office of Foreign Assets Control (OFAC) sanctions. Prior to this recent name change, INDRIK SPIDER attempted to change the names of _Hades_ and their _Phoenix CryptoLocker_ ransomware at least one other time to avoid OFAC sanctions. The changes made to avoid these sanctions indicates that INDRIK SPIDER desires to continue their deployment of [ransomware](/en-us/cybersecurity-101/ransomware/). In July 2021, CrowdStrike Intelligence determined that _Grief_ ransomware is developed by [DOPPEL SPIDER](https://falcon.crowdstrike.com/intelligence/actors/doppel-spider), likely as an intended successor to _DoppelPaymer_ ransomware. The cessation in _DoppelPaymer_ activity coincided with the emergence of the _Grief_ DLS that was first observed in May. Analysis of recently identified _Grief_ samples indicates a number of technical overlaps with DOPPEL SPIDER’s wider toolset that provides a definitive link to the adversary. [WIZARD SPIDER](https://falcon.crowdstrike.com/intelligence/actors/wizard-spider) continues to actively deploy _Conti_ ransomware and update the _Conti_ DLS. In June 2021, WIZARD SPIDER continued to target large entities in Europe and the United States, including organizations in real estate, education and local government. Recent developments related to the Colonial Pipeline and JBS incidents have not slowed down WIZARD SPIDER’s ransomware operations. This indicates WIZARD SPIDER remains largely unaffected by external pressure, similar to their response to the September 2020 [takedown efforts targeting _TrickBot_ infrastructure](/en-us/blog/wizard-spider-adversary-update/).

## Outlook

The confluence of U.S. and international law enforcement pressure and forum bans on ransomware activity has led to a highly fluid and chaotic situation in the eCrime ecosystem. The ECX has indicated a change in BGH activity May through June 2021 as well as the persistence of ongoing BGH incidents at a level observed in the first quarter of 2021. However, the downward trend in BGH victims posted to DLSs in June likely indicates that some BGH actors have shifted TTPs to make tracking their activity more difficult. Numerous adversaries have shown themselves keen to take advantage of the situation and to attract new affiliates. These adversaries have explicitly expressed their intent to continue ransomware operations despite reports of possible U.S.-Russian collaboration — or more aggressive unilateral enforcement actions by the U.S. — in response to incidents, suggesting that a complete drop in BGH activity is highly unlikely to occur in the near future.

The ECX remains a valuable tool used to identify significant events affecting the eCrime ecosystem. The ECX provides an easily referenced index to mark areas of disruption or change in the eCrime ecosystem in real time. Monitor the ECX regularly in the [CrowdStrike Adversary Universe](https://adversary.crowdstrike.com) to make sure you stay up-to-date on eCrime trends.

#### Endnotes

  1. https<:>//www.justice<.>gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside
  2. https<:>//www.bleepingcomputer.com/news/security/avaddon-ransomware-shuts-down-and-releases-decryption-keys/
  3. https<:>//www.npu.gov<.>ua/news/kiberzlochini/kiberpolicziya-vikrila-xakerske-ugrupovannya-u-rozpovsyudzhenni-virusu-shifruvalnika-ta-nanesenni-inozemnim-kompaniyam-piv-milyarda-dolariv-zbitkiv/



#### Additional Resources

  * _Learn how[ CrowdStrike Falcon® Intelligence Recon™](/en-us/products/threat-intelligence/falcon-x-recon/) mitigates digital risk from the deep, dark web and beyond._
  * _Read about BGH adversaries tracked by CrowdStrike Intelligence in 2020 in the[ CrowdStrike 2021 Global Threat Report](/en-us/resources/reports/global-threat-report/)._
  * _To find out how to incorporate intelligence on threat actors into your security strategy, visit the[ CROWDSTRIKE FALCON® INTELLIGENCE™ Threat Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Learn about the powerful, cloud-native[ CrowdStrike Falcon® platform by visiting the product webpage. ](/en-us/endpoint-security-products/)_
  * _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) and learn how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)