# Naming Adversaries And Why It Matters To Your Security Team | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/naming-adversaries-and-why-it-matters-to-security-teams/
- **Date :** May 31, 2022

---

# Naming Adversaries and Why It Matters to Your Security Team

May 31, 2022

• [ Bart Lenaerts-Bergmans](/en-us/blog/author.bart-lenaerts-bergmans/ "Posts by Bart Lenaerts-Bergmans") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


What is it with these funny adversary names such as [FANCY BEAR](https://adversary.crowdstrike.com/en-US/adversary/cozy-bear.html), [WIZARD SPIDER](https://adversary.crowdstrike.com/en-US/adversary/wizard-spider.html) and [DEADEYE JACKAL](https://adversary.crowdstrike.com/en-US/adversary/deadeye-jackal.html)? You read about them in the media and see them on CrowdStrike t-shirts and [referenced by MITRE](https://attack.mitre.org/groups.html) in the ATT&CK framework.

Why are they so important to cyber defenders? How is an adversary born? You may think you have a problem with [ransomware](/en-us/cybersecurity-101/ransomware/), bots or distributed denial of service (DDoS) attacks but you would be wrong. Because humans are behind every cyberattack, what you really have is an adversary problem. Understanding the adversaries most likely to target your business is critical because it helps you focus your resources and better prepare your defenses to defeat them. CrowdStrike currently tracks and profiles over 180 adversaries, having added 21 new adversaries in 2021 alone. So let’s dive into the world of adversaries and understand why attribution and an adversary-focused approach to cybersecurity is crucial to defending against modern cyberattacks.

## Attribution 101: What’s in a Name?

Every adversary is motivated by a specific objective whether it is financial, espionage or political gain. CrowdStrike uses a two-part cryptonym so adversaries can be easily identified based on these three critical motivating factors:

  * SPIDERs are cybercriminals motivated by monetary gain 
  * Nation-states perform espionage and are identified by their country of origin's national animal such as BEAR (Russia) or PANDA (China) 
  * Hacktivists, looking to create political disruption, are JACKALS



The honor of providing the name used for the first part of the cryptonym goes to the CrowdStrike threat intelligence analyst or team who attributed the activity to a specific threat actor or group. While this part of the name may be arbitrary, CrowdStrike analysts are typically influenced by prominent tools and techniques they have observed being used by the actor.

### Identifying Activity Clusters

As you have probably guessed, observing related activity or “activity clusters” is a crucial aspect of CrowdStrike’s threat research that helps determine attribution. The first step in identifying an activity cluster is to collect the right data in order to expose illicit actions. Only CrowdStrike has access to the trillions of events per day collected by the [CrowdStrike Falcon®® platform](/en-us/falcon-platform/), which protects millions of endpoints across the globe and provides visibility into real-time and zero-day attacks.

In addition, CrowdStrike Intelligence collects raw intelligence from several other sources including incident response engagements, millions of malware samples processed per day, the deep and dark webs, underground communities, social media, open source and much more. This is where CrowdStrike has a distinct advantage, confirmed by having the highest score across all vendors in the [Forrester Wave™ External Threat Intelligence Services, Q1 2021](/en-us/resources/reports/forrester-wave-external-threat-intelligence-services/) for the criteria “raw intelligence collection.” The second step is analyzing this data using machine-based analytics as well as human intelligence analysts. CrowdStrike Intelligence analysts are organized into cells of cyber threat expertise such as adversarial pursuit, tactical malware analysis, geopolitics, threat campaign analysis and others. CrowdStrike produces comprehensive threat insights across multiple dimensions such as attack motivation, techniques and threat operations tactics.

Activity clusters are typically based on one or more related technical attack techniques, tools or infrastructure that are leveraged by the adversary. For nation-state-sponsored adversaries, CrowdStrike’s intelligence analysts overlay an understanding of the geopolitical nexus of all observed activities to raise the confidence level from a cluster to a named state-sponsored adversary. The process is slightly different for cybercrime, where intel analysts focus on adversarial tooling, tradecraft and infrastructure, with careful emphasis on actor threat operations such as usage of “as-a-service” frameworks, shared infrastructure or inclusion of public commodity tooling during the attack steps.

### Maintaining Rigorous Naming Standards

CrowdStrike has defined rigid analytic integrity standards that are routinely reinforced among the analytic cadre. All intelligence analysts are trained to ensure proper use of estimative language, bias awareness and elimination, and on using analytic tools such as “alternative competing hypotheses.”

Throughout the attribution process, integrity is maintained through an extended judicious review among the different CrowdStrike teams holding threat expertise. Only after a series of rigid analytic steps will an actor be given a name and added to CrowdStrike’s list of named adversaries.

## How Defenders Benefit from an Adversary-Focused Approach

Adversary attribution enables defenders to understand the “who, how and why” behind the cyberattacks targeting their business. By understanding their adversaries’ motivation, tools and tactics, defenders can apply proactive and preventative actions.

For instance, targeted attacks may be driven by [espionage](/en-us/cybersecurity-101/threat-intelligence/cyber-espionage/), which indicates the threat will most likely be persistent and comprise multiple sophisticated attacks that can be expected to attempt to gain access to your sensitive company data. Knowing this about the espionage-motivated adversary provides guidance on where to place defensive “[shields-up](https://www.cisa.gov/shields-up)” measures and how you can best prepare. This could include proactively patching vulnerabilities or blocking file hashes or IP addresses at the perimeter, defensive tactics based upon attack vendors the adversary is known to have used in the past. Attribution enables security teams to understand their true risk posture by defining who could come after them and how, and preemptively adjust their security strategy.

Adversary attribution also enables security teams to reduce noise by filtering an overload of security data to focus on specific tactics. The CrowdStrike Intelligence team’s profiling of over 180 global threat actors across cybercrime, nation-state and hacktivist adversaries enables you to search for just those actors most likely to attack your organization. A good place to start is to filter security data according to adversaries’ preferred targets, typically by industry and geographic region. Security analysts can focus on this much smaller subset instead of focusing on lower-risk, commodity attacks that are blocked by the security controls they have in place.

In addition, once a known, sophisticated adversary has been spotted inside your organization’s infrastructure, alert levels can be raised, shields-up declared, and the available intel on the adversary can drive the threat hunting process to find and expel the adversary. Without this knowledge, security operations center (SOC) analysts waste time and resources, playing “whack a mole” in chasing every commodity attack or being blind to adversary activity that may be seen as normal activity without the context provided by threat intelligence.

While attribution provides the information that helps security teams prepare, there is additional intrinsic value in taking an adversary-focused approach to security. Attribution enables the entire team — proactive and reactive defenders alike — to orient their actions toward specific actors that target the organization, create their behaviors and tools, and begin to communicate across all teams with a common language including the adversary’s name, attack steps and point of view. This approach helps teams step away from tool- or process-heavy tactics and build strategies to increase the effectiveness of their security efforts. In addition, security organizations are often split into operational silos, with each silo focusing on specific detection or protective tools. This structure with attention to “tools in use” and “small-team objectives” is not always advantageous. Focusing instead at a higher level — fighting the adversaries that are trying to breach your defenses — changes the dynamics for the entire team and starts with knowing the adversary, which benefits the individual security practitioner as well as the entire organization.

#### Additional Resources

  * _Visit the[ CrowdStrike Adversary Universe](https://adversary.crowdstrike.com/en-US.html) to learn more about 10 prominent adversaries._
  * _Download the[ 2022 CrowdStrike Global Threat Report](/en-us/resources/reports/global-threat-report/)._
  * _Better understand the adversaries that target your business by requesting a[ free threat briefing](https://go.crowdstrike.com/threat-intelligence-briefing.html) with a CrowdStrike Intelligence expert._
  * _Find out more about how to incorporate intelligence on threat actors into your security strategy, visit the[ CrowdStrike Falcon® Intelligence™ Threat Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Get a full-featured[ free trial](https://go.crowdstrike.com/try-falcon-prevent.html) of CrowdStrike Prevent and CrowdStrike Falcon Intelligence and learn how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)