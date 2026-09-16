# The Signs Were There: What the First Autonomous Ransomware Case Confirms

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/g/autonomous-ransomware.html
- **Date :** 2026-07-24

---

Cyber Threats

# The Signs Were There: What the First Autonomous Ransomware Case Confirms

An AI agent has run a ransomware intrusion on its own for the first time, from break-in to data destruction. The autonomous attacks TrendAI™ Research predicted are beginning to arrive, and defending against them shifts from blocking known indicators to detecting behavior.

By: Jacob Santos 2026/07/24 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

## Key takeaways

  * Security researchers have documented an AI agent running a full ransomware operation on its own against a live production target, planning, adapting, and executing every step from the first exploit through data destruction. This is early real-world evidence of the shift to autonomous criminal operations that our research forecast.
  * Agent-run attacks change what defenders can rely on. They produce disposable, per-victim indicators instead of reusable tools and infrastructure, so the defensive weight shifts from sharing and blocking indicators of compromise onto behavior and technique-based detection.
  * The novelty is automation, not tradecraft. Every weakness the agent used was old and well understood, which concentrates exposure in organizations running internet-facing AI and automation platforms or carrying default and unrotated credentials, and shortens the time available to close those gaps.
  * The monetization layer failed even though the intrusion succeeded. The agent did not save the encryption key it generated and used a placeholder address instead of real payment infrastructure, so the operation could not have produced a payout even if the victim had complied.



[Ransomware](https://www.trendmicro.com/en_us/what-is/ransomware.html) has always had a person behind it. Someone picks the target, buys or builds the access, runs the tools, and extorts the victim for a payout. However, in an intrusion [documented this month by the security firm Sysdig](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion) and dubbed JADEPUFFER, no one did. By their account, a large language model (LLM) agent broke into a live production system, harvested credentials, moved deeper, encrypted a database, destroyed the originals, and left a ransom note. It was choosing and sequencing every step itself in near real time, with no human at the keyboard between the break-in and the damage.

An [artificial intelligence (AI)](https://www.trendmicro.com/en_us/what-is/ai.html) acting as the operator, not the assistant, is the shift Anthropic described in November 2025, when a state-linked group used its Claude model [“not just as an advisor, but to execute the cyberattacks themselves.”](https://www.anthropic.com/news/disrupting-AI-espionage) JADEPUFFER is that same step but aimed at extortion instead of espionage.

This is also the direction TrendAI™ Research has been tracking. Our December 2025 research on [the next phase of cybercrime](https://www.trendaisecurity.com/en-us/resources-insights/research/the-next-phase-of-cybercrime-agentic-ai-and-the-shift-to-autonomous-criminal-operations) called the turn early, pointing out that criminal work would move from “Cybercrime-as-a-Service,” where a human assembles bought capabilities, to “Cybercrime-as-a-Sidekick,” where an agent runs the job. The report calls JADEPUFFER the first agentic ransomware. JADEPUFFER shows how far AI’s role in an intrusion has climbed, from drafting text to running the whole operation (Figure 1).

![Figure 1. The escalating role of AI in an intrusion, from assistant to autonomous operator](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig01.png)

Figure 1. The escalating role of AI in an intrusion, from assistant to autonomous operator

[ download ](/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig01.png)

## The cases that led here

JADEPUFFER is the latest in a two-year progression of AI-enabled attacks. Our January 2026 “[State of Criminal AI](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/the-state-of-criminal-ai)” update found an ecosystem that had industrialized, but still hit hard practical limits. Malware that asks an LLM to write its own code on the fly, for one, dies the moment the provider revokes the key. At the time, we described it as innovative but not yet reliable enough to displace proven methods.

Several separate cases mark the road to this one, and each supplied a piece of what an autonomous ransomware operation would need:

  * LameHug, also tracked as PROMPTSTEAL and reported in July 2025, was the first malware seen querying a live LLM to generate its own commands. It was a human-operated data-theft tool, not a ransomware kill chain.
  * PromptLock, [reported by ESET](https://www.eset.com/us/about/newsroom/research/eset-discovers-promptlock-the-first-ai-powered-ransomware/) in August 2025, carried the “AI-powered ransomware” label but was an academic proof-of-concept that never ran against a real victim.
  * Anthropic’s [November 2025 disclosure](https://www.anthropic.com/news/disrupting-AI-espionage) showed an AI agent executing most of a real intrusion, but as state-directed espionage focused on data theft, not destruction.
  * [Another autonomous, self-correcting intrusion](https://www.sysdig.com/blog/ai-agent-at-the-wheel-how-an-attacker-used-llms-to-move-from-a-cve-to-an-internal-database-in-4-pivots) about seven weeks earlier reached a live victim but stopped at data exfiltration rather than destruction.



JADEPUFFER is the first case where all three elements meet at once, unlike any of the earlier cases. It has a full, end-to-end, agent-driven chain; destructive, extortion-focused impact; and a real production target (Figure 2).

![Figure 2. The continuum of AI-enabled attacks leading to the first autonomous, destructive, real-world case](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig02.png)

Figure 2. The continuum of AI-enabled attacks leading to the first autonomous, destructive, real-world case

[ download ](/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig02.png)

## The agent as operator

The clearest way to see the autonomy is to look at what the agent did without being told to. Our December research laid out a criminal agentic architecture in three layers: An agent layer that acts, an orchestration layer that plans and adapts, and a data layer that informs decisions. Here, the planning and adaptation, the orchestration layer, was the model itself, not a human operator.

According to Sysdig's report, the agent gained entry through an unpatched, unauthenticated remote-code-execution flaw in an internet-facing Langflow instance, an AI workflow platform. That flaw, [CVE-2025-3248](https://nvd.nist.gov/vuln/detail/CVE-2025-3248), carries a Common Vulnerability Scoring System (CVSS) score of 9.8, was fixed in Langflow 1.3.0, and was added to CISA’s Known Exploited Vulnerabilities catalog in May 2025. From there, the agent harvested credentials (including cloud and AI-provider keys), reached a MinIO object store that was still on its default credentials, then pivoted to the Nacos configuration server and its backing production database. It escalated privileges by chaining a 2021 authentication bypass in Alibaba Nacos ([CVE-2021-29441](https://nvd.nist.gov/vuln/detail/CVE-2021-29441)) with a default signing key the target had never rotated, forging an administrator token to plant a backdoor account.

It kept a foothold with a scheduled task that beaconed to its command-and-control server every 30 minutes. It then encrypted about 1,342 Nacos configuration records, deleted the original tables, and inserted a ransom note. A person could have done all of this. According to the report, no person did. One agent carried the whole sequence in a single continuous loop (Figure 3).

![Figure 3. How a single agent collapsed the entire attack chain into one autonomous loop](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig03.png)

Figure 3. How a single agent collapsed the entire attack chain into one autonomous loop

[ download ](/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig03.png)

The agent issued more than 600 distinct, purposeful payloads in a compressed window. When it created the backdoor administrator account and the login failed, it diagnosed the cause (a malformed password hash), deleted the broken account, regenerated the hash correctly, reinserted the account, and confirmed access, all in about 31 seconds. When a storage service returned data in an unexpected format, it rewrote its own parser to handle the response. When an attack path reported that a custom secret was in use, it dropped that path at once.

That pattern of rewriting on the fly to work around each failure isn’t a fixed script or a human working through a checklist, but is more like an operator reasoning about what it’s seeing. Our research warned that this capability , where one decision can now run from access to impact with no human action in between, would collapse the traditional attack chain.

## What agent-run attacks change for defenders

That collapse has three consequences for defenders that matter more than any single indicator, and none is unique to this one operation.

**Agent-run attacks leave almost nothing to block**

Conventional ransomware is generous with evidence. It reuses tools, binaries, and infrastructure, which is why so much of the industry’s defense is built on sharing and blocking indicators of compromise. JADEPUFFER offered almost none of that. There were no file hashes, because the payloads were inline code, effectively unique to this victim. The command-and-control (C&C) address may already be dead. The exfiltration destination named in the code was, on the evidence, invented by the model. The ransom address was a public example copied from documentation.

An agent that writes single-use code and improvises its own infrastructure leaves only disposable, per-victim indicators, shifting the defensive load from indicators onto behavior and technique. The durable signal is the behavior: An application server spawning a process that decodes and runs payloads, a scheduled task beaconing on a fixed interval, or a database process encrypting configuration tables and then dropping them (Table 1).

**Indicator-based defense (degrades against this attack)** | **Behavior-based detection (carries the load)**  
---|---  
**File hashes: none** \- payloads were inline code, unique to each victim | **Payload-decoding child process** \- an application server spawns a process that decodes and runs code  
**C &C address: may be dead** \- single-use infrastructure, likely already offline | **Fixed-interval beacon** \- scheduled outbound calls from that host on a regular cadence  
**Exfiltration IP: hallucinated** \- the model invented it; no data left the network | **Encrypt-then-drop on config tables** \- AES_ENCRYPT() on configuration tables, followed by DROP  
**Ransom wallet: placeholder** \- a public example address, not the attacker's |   
**Disposable, per-victim** | **Constant across the attack**  
  
Table 1. Why agent-run attacks weaken indicator-based defense and shift weight onto behavior

**The agent narrates its own intent, and some of it is false**

This case produced a new kind of evidence. The agent’s payloads were full of plain-language comments explaining what it was doing and why, including a note that tagged one database as “High-ROI” before dropping it. The agent’s intent, written out in its own words, is a kind of evidence defenders have rarely had. It helps with understanding motivation and with reconstructing a timeline.

The same self-narration included claims that were not true, most clearly that data had been exfiltrated to an external server, for which the reporting found no evidence. This looks like hallucination, the same failure mode that leads LLMs to state false information with total confidence. Anthropic saw the same thing in its case, where the model "occasionally hallucinated credentials or claimed to have extracted secret information that was in fact publicly available." An agent's account of itself is a lead, not a fact, so mining it for insight while independently checking every claim is a new skill worth building.

**What’s new, and what failed**

What’s new here isn’t the tradecraft, but that the agent ran the whole operation on its own and fixed its own mistakes along the way. The monetization layer is where it fell apart: The encryption key was generated once, printed to a console, and never saved, so the data could not have been decrypted even if a ransom had been paid. The ransom address was not the attacker’s either; our own analysis found it is a sample address published in public Bitcoin documentation, a value the agent reached for in place of a real payment destination. There was no leak site and no second victim.

Based on the outcome, this was closer to destruction than to a working extortion scheme. That does not make it less important. It makes it an early sign that autonomous ransomware works. The intrusion held up end to end; the payoff never materialized. Strip away the louder framing and the assessment is the same: The capability is real, and it’s only going to improve (Figure 4).

![Figure 4. Separating what is genuinely new in this case from what did not work](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig04.png)

Figure 4. Separating what is genuinely new in this case from what did not work

[ download ](/content/dam/trendmicro/global/en/research/26/g/autonomous-ransomware/autonomous-ransomware_fig04.png)

## Conclusion

JADEPUFFER can be seen as just a failed extortion attempt because although the mechanics worked, the payout never did. However, what’s more significant is that a single report now shows an AI agent running an intrusion start to finish, adapting to obstacles the way a person would, but faster than any person could.

Our [VibeCrime research](https://documents.trendmicro.com/assets/research-reports/crimininal-agentic-ai_research-paper.pdf) argued that criminal adoption of agentic AI would be slow at first, then accelerate once one group proved the approach pays off. JADEPUFFER isn't that moment, but it shows that the moment is within reach. None of the fixes – patch internet-facing platforms, clear out default and unrotated credentials – are new or exotic, but what's really changed is how little time defenders will have once attackers find those same gaps.

The same pressure is building from the enterprise side for a related reason, because companies are now deploying agentic AI deliberately. Agentic systems invoke tools, touch data, and trigger workflows through loops that adapt as they go rather than following a fixed path, which is exactly what makes their outcomes hard to predict, trace, or control. Our research on closing the governance gap in agentic AI treats governance as the control layer for that autonomy, and TrendAI™ is building it into the [Agentic Governance Gateway](https://www.trendaisecurity.com/en-us/resources-insights/research/from-anarchy-to-authority-closing-the-governance-gap-in-agentic-ai), capable of discovering and inventorying agents, observing what they do, understanding intent behind their actions, flagging anomalies, and enforcing policy. A company that can govern its own agents this well is also in a much stronger position to catch a hostile one loose in its environment.

## Recommendations

Autonomous execution compresses the time between an exposed weakness and its exploitation, so the priorities below are ordered to close the gaps this style of attack chains together.

**For defenders:**

  * **Prioritize behavior- and technique-based detection.** Alert on application servers spawning payload-decoding child processes, on fixed-interval beaconing from those hosts, and on bulk AES_ENCRYPT() activity against configuration tables followed by DROP on the same objects.
  * **Patch and inventory internet-facing AI and automation platforms.** Confirm that every Langflow instance is upgraded to 1.3.0 or later, and treat any exposed, unpatched instance as an active risk.
  * **Rotate default and long-unchanged secrets.** Replace shipped signing keys such as the Nacos token.secret.key, and clear default service credentials such as minioadmin:minioadmin. Default and unrotated credentials enabled two separate stages of this operation.



**For decision-makers:**

  * **Apply least-agency principles to AI systems.** Give agents and automation platforms only the access they need, watch how they interact with other systems, and require approval for high-impact actions.



**For incident responders:**

  * **Keep offline, immutable backups of configuration and metadata stores.** This operation showed that in-database backups offer no protection against an attacker with write access.
  * **Treat an agent’s self-narration as unverified during triage.** Its inline commentary is a useful starting point, but as this case showed, some of it is false.



## TrendAI™ protections

[TrendAI Vision One™ Cyber Risk Exposure Management](https://www.trendmicro.com/en_us/business/products/one-platform.html) continuously surfaces and ranks the exposures that agent-run intrusions chain together, such as unpatched internet-facing platforms and default credentials. The vulnerabilities this operation abused were already covered by TrendAI™ protections well before it surfaced, across the network and workload layers:

**TrendAI™ TippingPoint™**

  * **Filter 45744:** HTTP: Langflow Code Injection Vulnerability



**TrendAI™ Deep Discovery™ Inspector**

  * **Rule: 5411:** CVE-2025-3248 - LANGFLOW RCE - HTTP (Request)



**TrendAI™ Deep Security and TrendAI Vision One™ Server and Workload Protection (SWP)**

  * **Rule 1010971:** Alibaba Nacos AuthFilter Authentication Bypass Vulnerability (CVE-2021-29441)



Because the operation left no file-based indicators, behavior-level detection and the hunting queries in this entry's recommendations section carry the rest.

## TrendAI Vision One™ Threat Intelligence Hub

[TrendAI Vision One™ Threat Intelligence Hub](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the [TrendAI Vision One™](https://www.trendaisecurity.com/en/platform?_gl=1*b9qq60*_gcl_au*MzYzOTU2MTU4LjE3ODM4NjgyNTc.*_ga*Mzg1NjU0MTE4LjE3NTk5MDc5OTM.*_ga_J4XSRG212B*czE3ODQ4ODA3MDIkbzE4MSRnMSR0MTc4NDg4MDgyNSRqNTkkbDAkaDA.*_ga_4ZVKMRSC6W*czE3ODQ4ODA3MDIkbzEzOCRnMSR0MTc4NDg4MDgyNCRqNjAkbDAkaDA.) platform. 

**Emerging Threats:**

[JADEPUFFER: Agentic ransomware for automated database extortion](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=JADEPUFFER%3A%20Agentic%20ransomware%20for%20automated%20database%20extortion)

**TrendAI Vision One™ Intelligence Reports (IOC sweeping)**

[JADEPUFFER: Agentic ransomware for automated database extortion](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=JADEPUFFER%3A%20Agentic%20ransomware%20for%20automated%20database%20extortion)

TrendAI Vision One™ customers can retrieve the indicators associated with this activity for retrospective sweeping across their environment.

## **TrendAI Vision One™ XDR Data Explorer App**

Customers using TrendAI Vision One™ can use the XDR Data Explorer App to match the malicious indicators covered in this blog article against data in their own environments for hunting purposes.

**Post-exploitation subprocess execution from a Langflow process:**

eventSubId:2 AND parentFilePath:(*langflow*) AND processCmd:(*base64* OR *curl* OR *wget* OR *crontab*)

**Network connection to known JADEPUFFER C &C infrastructure:**

eventId:3 AND eventSubId:(201 OR 204) AND dst:("45.131.66.106")

More hunting queries are available for TrendAI Vision One™ customers with the Threat Intelligence Hub entitlement enabled.

## Indicators of compromise (IOCs)

This operation produced no file-hash indicators, because every payload was inline code delivered through the exploited interfaces rather than a distributed binary. Read the network indicators below with care: two are the agent’s own unverified narration, and one is a public placeholder rather than attacker infrastructure.

**Indicator** | **Type** | **Role** | **Notes**  
---|---|---|---  
45[.]131[.]66[.]106 | IPv4 | Command and control | Beacon destination on port 4444; may no longer be active  
64[.]20[.]53[.]230 | IPv4 | Claimed exfiltration | Named only in a payload comment; assessed as a likely model hallucination, and hosted on shared infrastructure with an unrelated abuse history  
e*******7[@]proton[.]me | Email | Extortion contact | Sole documented attacker contact channel  
3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy | Bitcoin address | Claimed ransom address | Confirmed as a sample address from public Bitcoin documentation; not attacker-controlled, do not treat as a payment or tracking indicator  
CVE-2025-3248 | CVE | Initial access | Unauthenticated RCE in Langflow; CVSS 9.8; fixed in 1.3.0; CISA KEV May 2025  
CVE-2021-29441 | CVE | Privilege escalation | Nacos authentication bypass, chained with an unrotated default signing key  
  
## MITRE ATT&CK techniques

The behavior maps to the following MITRE ATT&CK techniques. The reporting describes the behavior; the analysis on top of it is ours. Our analysts assigned the ATT&CK identifiers from the reported behavior, built the Search App hunting queries above from that same behavior for proactive telemetry sweeps, and mapped the exploited vulnerabilities to existing TrendAI™ protections.

**Tactic** | **Technique** | **ID** | **Observation**  
---|---|---|---  
Initial Access | Exploit public-facing application | T1190 | Unauthenticated RCE in an internet-facing Langflow instance (CVE-2025-3248)  
Credential Access | Unsecured credentials | T1552 | Cloud and AI-provider keys harvested from the compromised host  
Privilege Escalation | Valid accounts: default accounts | T1078.001 | MinIO object store reached with unchanged default credentials  
Privilege Escalation | Forge web credentials | T1606 | Administrator token forged using an unrotated Nacos signing key  
Persistence | Scheduled task/job: cron | T1053.003 | Cron entry beaconing to command and control every 30 minutes  
Command and Control | Application layer protocol | T1071 | Fixed-interval beacon to the command-and-control server  
Impact | Data encrypted for impact | T1486 | About 1,342 Nacos configuration records encrypted in place  
Impact | Data destruction | T1485 | Original configuration tables deleted after encryption  
  
Tags

[Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Ransomware](/en/research.html?category=trend-micro-research:threats/ransomware) | [Artificial Intelligence (AI)](/en/research.html?category=trend-micro-research:threats/artificial-intelligence-ai)

###  Authors 

  * Jacob Santos

Senior Threat Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)