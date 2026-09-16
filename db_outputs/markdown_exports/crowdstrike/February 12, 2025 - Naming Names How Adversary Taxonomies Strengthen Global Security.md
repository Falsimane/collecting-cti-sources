# Naming Names: How Adversary Taxonomies Strengthen Global Security

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-adversary-taxonomies-strengthen-global-security/
- **Date :** February 12, 2025

---

# Naming Names: How Adversary Taxonomies Strengthen Global Security

February 12, 2025

• [ Rob Sheldon - Adam Meyers](/en-us/blog/author.rob-sheldon---adam-meyers/ "Posts by Rob Sheldon - Adam Meyers") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Last month, during [testimony on global cyber threats](https://homeland.house.gov/hearing/unconstrained-actors-assessing-global-cyber-threats-to-the-homeland/) before the U.S. Committee on Homeland Security, a longstanding debate resurfaced: Why do vendors name different cyber threat actors, and can’t we directly call out those responsible? 

Industry veterans will recognize that a discourse on this topic tends to pop up in vendor, media, and public policy circles every few years. But for the less initiated, let’s review the evolution of, and [rationale](https://www.crowdstrike.com/en-us/blog/naming-adversaries-and-why-it-matters-to-security-teams/) for, common threat actor naming practices to clarify why this system endures. 

### The Vague Old Days

A couple of decades ago, most of the people tracking cyber threats were in defense and national security circles. Unsurprisingly, classification issues plagued open discussion of specific breaches. Researchers operating within trusted relationships might sometimes talk around classified information, but these discussions were necessarily limited. _“Did you hear about that Defense Industrial Base breach last week? Seems like it could be the same crew that hit that National Lab last year … no, the other National Lab … no, the other crew."_

At that time, it was already commonplace for insiders to refer to state-sponsored attacks as advanced persistent threats (APTs). But by the mid- to late-2000s, multiple states were hacking — and the techniques weren’t necessarily sophisticated. Something more specific was necessary.

The cybersecurity industry grew significantly over this period. In describing threat activity, some would use one-off names, often based on code artifacts or tactics, techniques, and procedures (TTPs). While these names often stuck, there was no structure, and vendors and researchers used different approaches to naming. Some named actors, some named malware, and some named specific breaches or campaigns. 

As recently as 15 years ago, the field still lacked consensus on whether it was even possible to attribute cyberattacks. Many people thought even attempting to do so was a distraction from more practical concerns, like finding and patching bugs. It wasn’t until 2014, when the U.S. [indicted](https://www.justice.gov/iso/opa/resources/5122014519132358461949.pdf) five members of the China’s People’s Liberation Army (the [documents](https://www.justice.gov/opa/pr/us-charges-five-chinese-military-hackers-cyber-espionage-against-us-corporations-and-labor) [for which](https://www.justice.gov/iso/opa/resources/5122014519132358461949.pdf) came complete with full names and pictures) that this misconception changed durably. 

### Why Security Requires More than Country of Origin 

Threat actors can be attributed, even to the level of the individual. Yet, major cybersecurity vendors still use different code names, even for the same threat actors. Why? There’s a bit of [prior](https://cyb3rops.medium.com/the-newcomers-guide-to-cyber-threat-actor-naming-7428e18ee263) [art](https://threadreaderapp.com/thread/1167098838907314176.html) on this question, but we’ll highlight some key reasons.

First, attribution is challenging. At this point, quite a few vendors have some ability to cluster threats (e.g., those responsible for a given breach also appear to be responsible for two historic breaches, or a given breach appears linked to an ongoing campaign of similar breaches). But very few vendors have the ability to credibly perform “last mile” attributions, which can confidently characterize that activity and link it to actual people or an institution. 

Second, disparate visibility across industry players complicates agreement. A telecom provider and content delivery network operator might share an overlapping vantage on a threat, making it straightforward to correlate distinct bodies of research. But a smartphone OEM or operating system provider may see very different pieces of the puzzle. CrowdStrike might make a determination linking threats based on endpoint telemetry, incident response, or identity information that’s unavailable — and indeed unintelligible — to a legacy firewall company. 

Third, industry players want to quickly share information that can help people. Threat actor names allow vendors to iteratively produce and circulate research without waiting for definitive attribution or industrywide consensus. Codenames enable stakeholders to discuss specific groups over time, which is especially important prior to credible “last-mile” attributions. 

Fourth, there are legitimate barriers to reconciling threat information. Different providers have unique restrictions, such as customer data protection obligations and intellectual property considerations, that may impede sharing data with other entities. Notably, the cybersecurity industry is global, and some players are from different countries with uneven track records on confidentiality and different legal and regulatory environments.

Most importantly, in intelligence, analytic rigor is essential. CrowdStrike uses extremely rigorous processes to designate named adversaries. We would not accept another organization’s attribution determination without independently verifying it. When our CEO, George Kurtz, testified to the Senate Select Committee on Intelligence following the breach of SolarWinds in February 2021, he referred to [the activity cluster _StellarParticle_](https://www.intelligence.senate.gov/sites/default/files/documents/os-gkurtz-022321.pdf) rather than Russia (or a particular BEAR actor) due to this policy.

### Adversary Codenames Provide a Structured Taxonomy for Security Teams

Naming threat actors addresses these problems head on, but there’s still the matter of why names differ so widely. Indeed, many systems have arisen over time. Google Mandiant’s numeric naming designation (e.g., APT28 and APT29) has the advantage of scaling infinitely. However, it’s linear and carries little embedded information for those not familiar with specific reporting. The numbers are also high at this point and challenging to remember. 

Microsoft’s recently retired element-based system (e.g., BARIUM, BORON) couldn’t scale with the proliferation of adversaries, as there are only 118 chemical elements on the periodic table. They [shifted to a new](https://www.microsoft.com/en-us/security/blog/2023/04/18/microsoft-shifts-to-a-new-threat-actor-naming-taxonomy/) weather-based system in April 2023, which explains recent media reporting about typhoons (e.g., SALT TYPHOON). Changes along these lines can be somewhat disruptive to industry stakeholders. 

For our part, when CrowdStrike launched in 2011, we innovated a [cryptonym-based system](https://web.archive.org/web/20190331222146/https://www.crowdstrike.com/blog/meet-the-adversaries/) that yielded names like OPERATOR PANDA. Each name has two parts. The first (“OPERATOR”) references the specific group; it is often based on an existing community identifier or otherwise indicates targeting or TTP information. The second (“PANDA”) indicates the actor’s country of origin or motivation. In this case, the actor is a China nation-state actor that targets the telecommunications sector. 

This system has a number of strengths:

  * It embeds highly useful information about the threat actor motivation (e.g. criminal, hacktivist, or nation-state — and which nation-state). 
  * It can accommodate situations where multiple actors have _the same_ “last mile” attribution, such as when several distinct groups are associated with a bureaucracy like the Chinese Ministry of State Security (MSS).
  * It allows flexibility for those “last-mile” attributions to be _updated over time_ as new information becomes available or after state bureaucracies (or criminal groups, as in the case of SPIDERS) reorganize, move to a different scheme, or leverage a new ransomware-as-a-service (RaaS) platform.
  * It enables useful discussion _across information or confidence asymmetries_ , such as between a law enforcement organization with specific classified attribution information, a victim organization, and a third-party incident response provider.
  * It enables researchers and policymakers to _toggle_ between discussion of specific actors (e.g., “SLIPPY SPIDER”) and categories (e.g., “SPIDERs”). 



### Tracking Adversaries with Precision to Stop Breaches

The use of threat actor codenames is not an attempt to avoid naming and shaming specific adversaries, like Russia or China. It’s a technocratic measure analysts utilize to get _more_ specific than just a country, while enabling the flexibility to update “last mile” attribution based on new information. Recent critiques of this practice are misguided.

That said, industry stakeholders can do more to align reporting. We actively work to strengthen partnerships to this end. For the most serious threats, we’d also favor a periodic collaborative analytic process modeled off the U.S. Intelligence Community’s National Intelligence Estimate (NIE) system.

Policymakers can and should do more to drive accountability for foreign actors attacking American business, government, and critical infrastructure. We’ve long encouraged a more active approach to government targeting of threat actors through coordinated law enforcement operations and infrastructure disruptions and takedowns. At the geopolitical level, either more effective diplomacy or a more muscular approach to states like China, Russia, Iran, and North Korea is overdue. 

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)