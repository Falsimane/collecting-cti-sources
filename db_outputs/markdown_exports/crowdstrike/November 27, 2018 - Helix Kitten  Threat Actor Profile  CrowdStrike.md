# Helix Kitten | Threat Actor Profile | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/
- **Date :** November 27, 2018

---

# Meet CrowdStrike’s Adversary of the Month for November: HELIX KITTEN

November 27, 2018

• [ AdamM](/en-us/blog/author.adamm/ "Posts by AdamM") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


HELIX KITTEN is likely an **Iranian-based adversary group** , **active since at least late 2015** , **targeting organizations in the

aerospace, energy, financial, government, hospitality and telecommunications business verticals.** This adversary group is **most commonly associated with a custom PowerShell implant identified as Helminth**. The Helminth implant is routinely delivered through macro-enabled Microsoft Office documents requiring user interaction to execute an obfuscated Visual Basic Script. Additionally, **HELIX KITTEN actors have shown an affinity for creating thoroughly researched and structured spear-phishing messages** relevant to the interests of targeted personnel. In some instances, spear-phishing messages have been sent from compromised accounts of organizations related to the target to further enhance credibility. Information technology (IT) and corporate infrastructure is a common theme of HELIX KITTEN spear-phishing messages. In addition to Helminth, the ISMDoor implant is likely used by the Iran-based adversary to attack targets particularly those in the Middle East region. There are several infrastructure overlaps between ISMDoor and ISMAgent, a tool used exclusively by HELIX KITTEN. The implementation of the DNS transport layer protocol is very similar in both ISMDoor and ISMAgent. ISMDoor is able to exfiltrate data, take screenshots, and execute arbitrary commands on the victim’s machine. Command and control (C2) is performed through a covert channel based on DNS AAAA records. The actor uses dedicated domains to host their C2 infrastructure, as the C2 protocol requires full control over the authoritative DNS server to work. During the summer of 2018, **HELIX KITTEN actors were observed targeting entities in the Middle East** — of note, targets appeared to be located in Bahrain and Kuwait. These incidents involved spear-phishing attacks, which characteristic of HELIX KITTEN, included emails containing malicious PowerShell in their macros that connects to known C2 infrastructure. In early November 2018, CrowdStrike® Falcon OverWatch™ observed activity from the HELIX KITTEN adversary at a customer in the telecommunications vertical. While the adversary leveraged known tooling as well as tactics, techniques, and procedures (TTPs), this activity represented a shift in targeting that could allow HELIX KITTEN to support multiple objectives. HELIX KITTEN’s operations against organizations in the telecommunications industry could allow this adversary to conduct bulk data collection of large amounts of communications data that could be later leveraged in additional intelligence activities. Targeting telecommunications can also allow the adversary to be able to reroute communications to adversary-controlled infrastructure for data collection or malware delivery. The ultimate objective of this activity remains unclear at the time of this writing, but the addition of the telecommunications sector to HELIX KITTEN’s target scope is a notable development. OilRig, Helminth, Clayslide, APT34, IRN2 are community or industry names associated with this actor. 

## **Other Iranian-based Adversaries

**

  * [Clever Kitten](/en-us/blog/whois-clever-kitten/)

_**Curious about other nation-state adversaries?**_ _Visit our[threat actor center](/blog/meet-the-adversaries.html) to learn about the new adversaries that the CrowdStrike team discovers._

#### Additional Resources

  * _To learn more about how to incorporate intelligence on threat actors like HELIX KITTEN into your security strategy, please visit the_[ _Falcon threat intelligence product page_](/content/crowdstrike-www/locale-sites/us/en-us/endpoint-security-products/falcon-x-threat-intelligence/?ctm_source=Website&ctm_medium=Blog&ctm_campaign=Blog-Inline-Copy) _._
  * _[Download the 2020 CrowdStrike Global Threat Report](/resources/reports/2020-crowdstrike-global-threat-report.html)_



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)