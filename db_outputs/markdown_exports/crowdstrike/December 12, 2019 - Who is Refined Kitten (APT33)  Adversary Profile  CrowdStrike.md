# Who is Refined Kitten (APT33)? | Adversary Profile | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/who-is-refined-kitten/
- **Date :** December 12, 2019

---

# Who is REFINED KITTEN?

December 12, 2019

• [ AdamM](/en-us/blog/author.adamm/ "Posts by AdamM") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


## Common Aliases

REFINED KITTEN may also be identified by the following pseudonyms:

 __

  * **_APT33_**
  * ** _Elfin_**
  * ** _Magnallium_**
  * ** _Holmium_**



## REFINED KITTEN’s Origins

REFINED KITTEN is a nation-state-based threat actor whose actions are likely tied to the objectives of the **Islamic Revolutionary Guard Corps (IRGC) of the Islamic Republic of Iran**. The adversary has been involved in conducting primarily espionage-oriented operations since at least 2013. Although intelligence gathering is REFINED KITTEN’s main focus, there have been suspected links between this adversary and the destructive [Shamoon malware attacks](https://www.cshub.com/attacks/news/incident-of-the-week-shamoon-virus-cripples-hundreds-of-computers).**

** Historically, REFINED KITTEN has employed both custom-made and open-source remote access tools (RATs) to acquire intelligence from its victims. More recently, however, REFINED KITTEN **has increasingly relied on mainstream open-source malware frameworks** , such as PoshC2 and PowerShell Empire. 

## REFINED KITTEN’s Targets

REFINED KITTEN’s ’s complete victim scope is unknown, but its activities tend to concentrate on a specific set of nations and industries – likely reflecting its changing intelligence requirements at any given time. 

### Target Nations

REFINED KITTEN’s targeting typically concentrates on entities in Saudi Arabia, the United Arab Emirates, and the United States; all of these countries are related to standing interests of the IRGC. Most recently, heightened tension between the U.S. and Iran during the summer of 2019 was likely a catalyst of the uptick in activities targeting financial and government organizations in the U.S. 

### Target Industries

While this adversary is unlikely to shy away from any particular industry, REFINED KITTEN’s efforts are most prevalent in the following industries: 

  * **Aerospace**
  * **Defense**
  * **Energy**
  * **Oil and Gas**

Recently, it appears this adversary has set its sights on the defense industry, as REFINED KITTEN has been observed spoofing job postings for defense contractors. 

## REFINED KITTEN’s Methods

REFINED KITTEN heavily relies on spear-phishing as its method of malware delivery. Victims are likely sent an email that contains a Hypertext Application File (HTA) which is typically used to display spoofed domains hosting a variety of job-themed content. Recently, these spoof domains and their hosted content have defense contractor themes and invite a victim to complete a decoy job application. In this recent activity, victims are prompted to complete a decoy job application by first taking an action (e.g. complete a CAPTCHA) that downloads additional PowerShell commands from command-and-control (C2) URLs. These additional PowerShell commands have been observed delivering open-source post-exploitation frameworks as payloads (e.g., PoshCh2, Koadic). 

## Other Known “ADVERSARIES”

REFINED KITTEN is just one of many adversaries tracked by CrowdStrike® Intelligence. Some of the other threat actors that CrowdStrike monitors include the following: 

  * [HELIX KITTEN](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/)
  * [FANCY BEAR ](/en-us/blog/who-is-fancy-bear/)
  * [MYTHIC LEOPARD](/en-us/blog/adversary-of-the-month-for-may/)
  * [GOBLIN PANDA](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-august-goblin-panda/)

_Curious about other eCrime, hacktivist or nation-state adversaries? Visit our_[ _threat actor center_](/en-us/blog/meet-the-adversaries/) _to learn more about threat actors that the CrowdStrike_[ _threat Intelligence_](/en-us/epp-101/threat-intelligence/) _team tracks._

## Learn More About the Cyber Threat Landscape

**Want more insights on the latest adversary tactics, techniques, and procedures (TTPs)?

**

  * Download: [CrowdStrike 2020 Global Threat Report](/resources/reports/2020-crowdstrike-global-threat-report.html).
  * To learn more about how to incorporate intelligence on threat actors like REFINED KITTEN into your security strategy, please visit the [CrowdStrike Falcon® Intelligence Threat Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/).
  * [Get a full-featured free trial of CrowdStrike Falcon® Prevent™ ](https://go.crowdstrike.com/try-falcon-prevent.html)and learn how true next-gen AV performs against today’s most sophisticated threats.



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)