# Rapid7 Detection Coverage for Iran-Linked Cyber Activity

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-detection-coverage-iran-linked-cyber-activity/
- **Date :** 2026-03-11

---

The tension arising out of the conflict in Iran is beginning to show signs of expanding beyond a strictly regional crisis. Following our recent published advisories, this communication is intended to outline and summarize the detection and enrichment coverage available to Rapid7 customers, broadly assess the macro cyber threat landscape, and demonstrate the specific actions undertaken within the Rapid7 portfolio to assure our customers of the protection they receive and can expect moving forward. For a research-driven companion piece from Rapid7 Labs, dive into****[**_Iran’s Cyber Playbook in the Escalating Regional Conflict_**](/blog/post/tr-iran-cyber-playbook-escalating-regional-conflict/)**.**

##  Tracking the campaigns associated with the current conflict 

There exists a number of threat campaigns (both directly and indirectly) associated with groups associated with Iranian APT actors. In order to track details of these campaigns, any relevant indicators of compromise will be made available within [Intelligence Hub](/platform/threat-intelligence-tip/).

![collective-campaign-_Intelligence-Hub.png](https://www.rapid7.com/cdn/images/blt7126a55c736bf850/69b182db13aa3d5be1e37d45/collective-campaign-_Intelligence-Hub.png) _Figure 1: A screenshot of the collective campaign available within Intelligence Hub._

⠀

As additional intelligence is identified and verified this campaign (and any others) will be incorporated and made available both within the detection stack across the Rapid7 portfolio, but equally for enrichment purposes within Intelligence Hub.

## Hacktivist activity and Digital Risk Protection (DRP) coverage 

Since the regional military escalations began in late February 2026, Rapid7 Labs has tracked a significant and ongoing spike in retaliatory cyber activity targeting regional and Western infrastructure. What we're seeing falls into two broad buckets. The first is state-directed operations, primarily espionage and data exfiltration, carried out by actors like:

  * MuddyWater/Seedworm (MOIS)

  * CyberAv3ngers (IRGC)

  * The Handala persona (assessed as being maintained by Void Manticore under MOIS direction). 




The second is a much noisier layer of hacktivist activity, stemming from groups that lack sophistication but generate outsized visibility through DDoS campaigns and public breach claims. These groups include:

  * Keymous+

  * DieNet

  * NoName057(16).




A major theme across this escalation is fabrication. Many of the breach claims circulating on Telegram and dark web forums are exaggerated or outright fake. Threat actors, especially on the hacktivist side, are recycling old leaked datasets, overstating their access, and running what amount to psychological operations aimed at causing panic and reputational damage. That said, where state-directed actors are involved, legitimate data theft is a real concern, and there is a strong likelihood that stolen material will be weaponized publicly and quickly.

Rapid7's [Digital Risk Protection platform](/products/threat-command/) is purpose-built to cover exactly these kinds of threats. Here is how our coverage maps to the current activity:

  * **Dark web and forum monitoring** — The coordination and announcements driving these campaigns are happening across Telegram, X (formerly Twitter), and dark web leak sites. DRP continuously monitors clear, deep, and dark web sources, with proprietary crawlers, inspecting tens of millions of pages. This gives us visibility into restricted forums and early warning when campaigns begin targeting specific organizations or sectors.

  * **Data leakage detection and claim verification** — With so many unsubstantiated breach claims in circulation, the ability to quickly distinguish real exposures from fabricated ones is critical. DRP monitors threat actor dumps and leak sites for exposed company assets and correlates what it finds against each customer's digital footprint, giving organizations a clear answer on whether a claimed breach actually affects them.

  * **Brand security and phishing defense** — Threat actors are exploiting public confusion to register lookalike domains, clone websites, and create impersonation profiles on social media. DRP identifies these phishing and impersonation threats and supports the takedown of the attacker's infrastructure.

  * **Analyst-verified intelligence** — Our threat intelligence analysts investigate and triage what surfaces through the platform to ensure customers receive only intelligence that has been verified and is actionable. When a real compromise or data exposure is confirmed, our team works directly with the affected organization to assess the impact and support remediation.




## CVE intelligence 

To fuel the data leak and psychological operations discussed above, state-directed actors like MuddyWater and Void Manticore are actively weaponizing recently disclosed, high-impact vulnerabilities. Rather than focusing on a single product, these APTs are broadly targeting a combination of internet-facing edge devices, enterprise management infrastructure, and client productivity software to gain their initial foothold.

The vulnerabilities being leveraged in these campaigns all provide either authentication bypass or remote code execution, giving attackers a direct path into the environment. Once inside, the goal is the same every time: establish persistence and get data out. As noted above, any legitimate data stolen during these intrusions is highly likely to be handed off to hacktivist personas and weaponized publicly to support the broader disinformation campaigns.

The following CVEs have been identified as actively exploited or assessed as high-priority targets in the current threat environment:

  * **CVE-2026-1281**

    * **Description:** A critical command injection vulnerability in Ivanti Endpoint Manager Mobile (EPMM) that grants unauthenticated attackers root-level remote code execution. This has been leveraged as a zero-day vulnerability to compromise mobile endpoint management environments.  
**Tied to:** MuddyWater (MOIS)

    * **Metasploit Module:**[ https://github.com/rapid7/metasploit-framework/pull/20932](https://www.google.com/search?q=https://github.com/rapid7/metasploit-framework/pull/20932)

  * **CVE-2024-4577**

    * **Description:** A critical OS command injection vulnerability in PHP running in CGI mode on Windows. By exploiting Windows "Best-Fit" encoding behaviors, attackers can bypass escape mechanisms and execute arbitrary code on the host server.  
**Tied to:** Void Manticore (the MOIS-affiliated actor that maintains the Handala hacktivist persona)

    * **Metasploit Module:**[ https://github.com/rapid7/metasploit-framework/pull/19247](https://github.com/rapid7/metasploit-framework/pull/19247)

  * **CVE-2025-32433**

    * **Description:** A pre-authentication remote command execution (RCE) flaw in Erlang-based SSH servers. Threat actors can execute arbitrary root commands by sending specially crafted SSH packets, bypassing authentication entirely.

    * **Metasploit Module:** [https://www.rapid7.com/db/modules/exploit/linux/ssh/ssh_erlangotp_rce/](https://www.rapid7.com/db/modules/exploit/linux/ssh/ssh_erlangotp_rce/)

  * **CVE-2025-52691**

    * **Description:** An unauthenticated file upload flaw in SmarterTools SmarterMail. Attackers exploit a path traversal weakness via the guid variable to drop malicious files, such as webshells or malicious cron jobs.

    * **Metasploit Module:**[ https://github.com/rapid7/metasploit-framework/pull/20866](https://www.google.com/search?q=https://github.com/rapid7/metasploit-framework/pull/20866)

  * **CVE-2025-9316**

    * **Description:** An unauthenticated session bypass vulnerability impacting N-able N-Central. Attackers frequently chain this with an XML External Entity (XXE) vulnerability to read highly sensitive local configuration and backup files from the host infrastructure.

    * **Metasploit Module:** [https://github.com/rapid7/metasploit-framework/pull/20713](https://github.com/rapid7/metasploit-framework/pull/20713)

  * **CVE-2026-21514**

    * **Description:** A security feature bypass vulnerability in Microsoft Word that allows an unauthorized attacker to bypass Object Linking & Embedding (OLE) mitigations locally. Exploitation requires user interaction to open a maliciously crafted document.

    * **Rapid7 Coverage:** Analyzed extensively in Rapid7's[ Patch Tuesday - February 2026](/blog/post/em-patch-tuesday-february-2026/) blog post and prioritized for customer patching due to active exploitation




## Detection and Response for Rapid7 customers 

Rapid7’s Threat Hunting team has been actively hunting for activity related to Iranian actors since the regional conflict began. We are utilizing threat intelligence related to new indicators of compromise and known tactics, techniques, and procedures to conduct these hunts. If we have validated findings, the MDR SOC will investigate and communicate the details of findings using the standard notification processes.

_Additional reading from Rapid7 Labs:_[**_Iran’s Cyber Playbook in the Escalating Regional Conflict_**](/blog/post/tr-iran-cyber-playbook-escalating-regional-conflict/)

## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)
  * [Detection and Response](/blog/tag/detection-and-response/)