# STARDUST CHOLLIMA | Threat Actor Profile | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-april-stardust-chollima/
- **Date :** April 06, 2018

---

# Meet CrowdStrike’s Adversary of the Month for April: STARDUST CHOLLIMA

April 06, 2018

• [ AdamM](/en-us/blog/author.adamm/ "Posts by AdamM") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


**STARDUST CHOLLIMA is a targeted intrusion adversary with a likely nexus to the Democratic People’s Republic of Korea (DPRK).** This adversary is typically involved in operations against financial institutions with the intention of generating liquid assets for the DPRK. Previous activity tied to this adversary includes campaigns focused on abusing Society for Worldwide Interbank Financial Telecommunication (SWIFT) systems, as well as intrusions against global banking networks via strategic web compromise operations.

## Methods & Techniques

STARDUST CHOLLIMA uses several implants that share a code framework tracked by CrowdStrike® as “TwoPence.” This actor also uses techniques such as code protection tools like Enigma protector, password protected executables and secure deletion functions to remain hidden on target system for long periods of time by avoiding legacy security products. Recent Falcon Intelligence™ reporting has been published to customers assessing that STARDUST CHOLLIMA is suspected of targeting Latin America-based organizations since mid-2017.

## Targets

STARDUST CHOLLIMA primarily targets its victims with the aim of acquiring funds. CrowdStrike has not directly observed STARDUST CHOLLIMA conducting intelligence-gathering or destructive operations. It is not known at this time whether the TwoPence framework is used exclusively by STARDUST CHOLLIMA or if elements of it are shared between other related DPRK adversaries such as LABYRINTH CHOLLIMA, RICOCHET CHOLLIMA or SILENT CHOLLIMA. Currency generation represents an additional mission of DPRK actors beyond destructive attacks and espionage; this may reflect the impact of sanctions levied against the DPRK by the international community and the 2017 banning of the DPRK from [SWIFT.](https://www.reuters.com/article/us-northkorea-banks-swift/swift-messaging-system-bans-north-korean-banks-blacklisted-by-u-n-idUSKBN16F0NI)

CrowdStrike identified earlier attempts at revenue generation by SILENT CHOLLIMA prior to tracking STARDUST CHOLLIMA, which leveraged unique tools and infrastructure; however, no overlap between the two actors was identified. In addition to financial sector targeting, there is some technical overlap between the [Wannacry ransomware](/en-us/blog/falcon-intelligence-report-wanna-ransomware-spreads-rapidly-continually-encrypts-victim-files/), which began self propagating in May 2017, and both STARDUST CHOLLIMA and LABYRINTH CHOLLIMA. The earliest observed version of WannaCry, created in February 2017, generates a custom TLS handshake message as part of its C2 protocol that is sent before actual payload data is transmitted. This handshake message selects a random number of cipher suite constants from a hard-coded array, resulting in changing patterns of network traffic. Some variants of Hawup also generate a fake TLS header with a random selection of cipher suite identifiers that is prepended to actual C2 traffic. While the code is not the same, the concept and structure are similar enough to assume a relation. All WannaCry samples, many Hawup variants, and many tools based on the TwoPence library were compiled using Microsoft Visual Studio 6, which is rarely observed almost 19 years after its release. A hypothesis explaining these similarities is that the different actor groups have access to the same development resources, perhaps even a shared code library, but they engage in different types of attacks according to their respective missions. Community or industry names Lazarus Group, and Bluenoroff have been associated with this actor.

## Learn More

  * _**Curious about other nation-state adversaries?**_ Visit our [threat actor center](/blog/meet-the-adversaries.html) to learn about the new adversaries that the CrowdStrike team discovers.
  * To learn more about how to incorporate intelligence on [threat actors](https://www.crowdstrike.com/cybersecurity-101/threat-actor/) like STARDUST CHOLLIMA into your security strategy, please visit the [Falcon Intelligence product page](/content/crowdstrike-www/locale-sites/us/en-us/endpoint-security-products/falcon-x-threat-intelligence/?ctm_source=Website&ctm_medium=Blog&ctm_campaign=Blog-Inline-Copy).
  * **Want the insights on the latest adversary tactics, techniques, and procedures (TTPs)?** Download the _[CrowdStrike 2020 Global Threat Report](/resources/reports/2020-crowdstrike-global-threat-report.html)_



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)