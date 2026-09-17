# Mustang Panda | Threat Actor Profile | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/
- **Date :** June 15, 2018

---

# Meet CrowdStrike’s Adversary of the Month for June: MUSTANG PANDA

June 15, 2018

• [ Adam Meyers](/en-us/blog/author.adam-meyers/ "Posts by Adam Meyers") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


The June 2018 adversary spotlight is on **MUSTANG PANDA, a China-based adversary that has demonstrated an ability to rapidly assimilate new tools and tactics into its operations** , as evidenced by its use of exploit code for CVE-2017-0199 within days of its public disclosure. In April 2017, CrowdStrike® Falcon Intelligence™ observed a previously unattributed actor group with a Chinese nexus targeting a U.S.-based think tank. Further analysis revealed a wider campaign with unique tactics, techniques, and procedures (TTPs). This **adversary targets non-governmental organizations (NGOs) in general** , but uses Mongolian language decoys and themes, suggesting this actor has a specific focus on gathering intelligence on Mongolia. These campaigns involve the **use of shared malware like Poison Ivy or PlugX**. Recently, Falcon Intelligence observed new activity from MUSTANG PANDA, **using a unique infection chain to target likely Mongolia-based victims**. This newly observed activity uses a series of redirections and [fileless](/en-us/blog/key-characteristics-of-modern-fileless-attacks/), malicious implementations of legitimate tools to gain access to the targeted systems. Additionally, MUSTANG PANDA actors reused previously-observed legitimate domains to host files.

## Mustang Panda's Methods

Mustang Panda's unique infection chain often takes the following steps:

  1. **The infection chain used in this attack begins with a weaponized link to a Google Drive folder** , obfuscated using the goo.gl link shortening service.
  2. **When contacted, the Google Drive link retrieves a zip file, which contains a .lnk file** obfuscated as a .pdf file using the double extension trick.
  3. This file **requires the target to attempt to open the .lnk file, which redirects the user to a Windows Scripting Component (.wsc) file** , hosted on an adversary-controlled microblogging page. MUSTANG PANDA has previously used the observed microblogging site to host malicious PowerShell scripts and Microsoft Office documents in targeted attacks on Mongolia-focused NGOs.
  4. **The .lnk file uses an embedded VBScript component to retrieve a decoy PDF file and a PowerShell script** from the adversary-controlled web page.
  5. **The PowerShell script creates a Cobalt Strike stager payload.** This PowerShell script also retrieves an XOR-encoded Cobalt Strike beacon payload from an adversary-controlled domain.
  6. **The Cobalt Strike Beacon implant beacons to the command-and-control (C2) IP address, which is used to remotely control the implant.**



There are no known community or industry names associated with this actor.

## Other Known China-based Adversaries

  * [Anchor Panda](/en-us/blog/whois-anchor-panda/)
  * [Deep Panda](/en-us/blog/ironman-deep-panda-uses-sakula-malware-target-organizations-multiple-sectors/)
  * [Goblin Panda](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-august-goblin-panda/)
  * [Samurai Panda](/en-us/blog/whois-samurai-panda/)



_**Curious about other nation-state adversaries?**_ _Visit our[threat actor hub](/blog/meet-the-adversaries.html) to learn about the new adversaries that the CrowdStrike team discovers._

## Learn More

To learn more about how to incorporate intelligence on threat actors like MUSTANG PANDA into your security strategy, please visit the [_Falcon threat intelligence product page_](/content/crowdstrike-www/locale-sites/us/en-us/endpoint-security-products/falcon-x-threat-intelligence/?ctm_source=Website&ctm_medium=Blog&ctm_campaign=Blog-Inline-Copy) _._ **Want the insights on the latest adversary tactics, techniques, and procedures (TTPs)?** Download the _[CrowdStrike 2020 Global Threat Report.](/resources/reports/2020-crowdstrike-global-threat-report.html)_

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)