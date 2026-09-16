# The Post-RAMP Era: Allegations, Fragmentation, and the Rebuilding of the Ransomware Underground

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-post-ramp-allegations-fragmentation-ransomware-underground-rebuild/
- **Date :** 2026-02-25

---

## Executive summary

The January 2026 seizure of RAMP disrupted a major ransomware coordination hub, but it did not dismantle the ecosystem behind it. Instead, it destabilized trust and accelerated fragmentation across the underground.

Rather than consolidating around a single successor, ransomware actors are redistributing across both gated platforms like T1erOne and accessible forums such as Rehub. This shift reflects adaptation, not decline.

For defenders, visibility into centralized coordination is shrinking. Monitoring must evolve beyond tracking individual forums to identifying actor migration, recruitment signals, and early indicators of regrouping. Disruption rarely eliminates ecosystems; it reshapes them. Organizations that adapt their intelligence strategies accordingly will be best positioned to stay ahead.

## Overview

### The anatomy of the RAMP disruption

Active since 2021, the RAMP (Ransomware and Advanced Malware Protection) forum has established itself as a prominent hub within the cybercrime ecosystem, particularly for [ransomware](/fundamentals/what-is-ransomware/) operators and affiliates coordinating attacks, sharing tooling, and trading access to compromised networks. On 28 January 2026, the Federal Bureau of Investigation (FBI), in coordination with the U.S. Attorney’s Office for the Southern District of Florida and the Computer Crime and Intellectual Property Section of the U.S. Department of Justice (DoJ), seized the forum’s infrastructure (Figure 1).

While public reporting focused primarily on the law enforcement action, the underground reaction revealed a deeper and more consequential development: a collapse of trust and increasing fragmentation within the ransomware community.

⠀

![Seizure-notice-RAMP-domain.png](https://www.rapid7.com/cdn/images/bltc598d4ee01bceb34/699f0050b9f0f2e2673235ae/Seizure-notice-RAMP-domain.png) _Figure 1 - Seizure notice on RAMP’s domain_

⠀

Shortly after, the RAMP’s administrator, known as “Stallman”, confirmed on the cybercrime forums XSS and Exploit the seizure, stating that he would not attempt to rebuild it (Figure 2). The announcement immediately sparked debate. Some users questioned whether the takedown had been staged or was a “PR exit,” while others accused Stallman of cooperating with authorities. RAMP’s nameservers were subsequently observed pointing to infrastructure controlled by the FBI, confirming the seizure by U.S. law enforcement.

⠀

![Stallmans-post-on-XSS.png](https://www.rapid7.com/cdn/images/bltf2c0c4fe686b06dd/699f00fd3b580e9a9224a833/Stallmans-post-on-XSS.png) _Figure 2 - Stallman’s post on XSS_

⠀

Following the announcement, screenshots purporting to show portions of RAMP’s database were circulated via Telegram and reposted across underground forums (Figure 3). These images allegedly contained user email addresses and private messages. Several former RAMP members publicly acknowledged that elements of the leaked data appeared authentic and expressed concern that registration emails, private communications, or operational details could be exposed and potentially leveraged in investigations.

⠀

![Screenshot-of-alleged-RAMP-leak.png](https://www.rapid7.com/cdn/images/blta1553823aa6fb594/699f01416da803534e7b6a26/Screenshot-of-alleged-RAMP-leak.png) _Figure 3 - Screenshot of alleged RAMP leak_

⠀

Stallman denied that any breach had occurred, claiming the forum’s disks were encrypted and that the circulating screenshots were fabricated.

Despite competing claims, underground discussions converged around two primary scenarios:

  * **Scenario A: Prior breach**

    * The database was exfiltrated before the law enforcement seizure, and the subsequent takedown was unrelated to the leak.

  * **Scenario B: Insider access**

    * An individual with administrative privileges exported the database, either before or during the seizure process.




No clear consensus has emerged. However, based on behavioral patterns observed in previous forum seizures and the technical realities involved, pre-seizure database access appears plausible. Even if the database was encrypted, protection at rest does not prevent extraction while a system is actively running.

There are also unverified allegations that Stallman attempted to sell the database for 10 bitcoin, though these claims remain unsubstantiated.

The alleged leak, combined with accusations of selective moderation and inconsistent rule enforcement, fueled speculation that RAMP may have functioned as a honeypot or had been compromised long before its seizure. While there is no public evidence confirming that RAMP was deliberately operated as a law enforcement trap, perception often matters more than proof in underground ecosystems. As such, the honeypot narrative itself accelerates fragmentation and contributes to a shift toward smaller, more tightly controlled ransomware platforms.

With RAMP gone and no official successor announced, forum users quickly began discussing alternatives. Some argued that XSS should reconsider its prohibition on ransomware-related activity. XSS administrators reiterated that ransomware affiliate recruitment remains banned, likely to avoid attracting heightened law enforcement scrutiny. This sparked debate about the forum’s long-term positioning and whether it would maintain its policy stance or adapt to fill the vacuum left by RAMP.  
  
This cycle of centralized growth to sudden disruption and migration toward successor platforms follows a recurring pattern observed after previous underground takedowns. When a dominant forum falls, the immediate effect is fragmentation and suspicion. In the absence of a trusted central marketplace, actors temporarily disperse, debate compromise theories, and test new governance models. Over time, smaller, vetted communities emerge to re-establish trust through higher entry barriers and tighter moderation. 

A prominent precedent is the shutdown of the cybercrime marketplace RaidForums in 2022, which was followed by the rise of BreachForums, a successor platform that inherited much of the user base and continued many of the same discussions and transactions. RAMP’s disruption appears to be following this familiar trajectory, suggesting not an end to coordination, but a restructuring of how and where it occurs.

### Enter T1erOne: A potential successor

The vacuum left by RAMP’s disruption coincided with the emergence of T1erOne in early February, a closed forum with a reputation- and payment-based entry model. Membership requires either verified activity on other underground forums or a $450 payment, emphasizing exclusivity and trust vetting (Figure 4). This structure is designed to reduce the risk of infiltration or exposure, a direct response to the alleged leaks from RAMP.

⠀

![T1erOne-registration.png](https://www.rapid7.com/cdn/images/blt7e240b608a36616a/699f019b6da8033e7d7b6a2a/T1erOne-registration.png) _Figure 4 - T1erOne registration_

⠀

The T1erOne model is further consistent with how RAMP itself operated previously. The forum specifically required proof of activity on other major underground forums or payment of a registration fee to help filter out infiltrators and low-trust actors. While this similarity does not prove T1erOne is RAMP’s direct successor, it makes sense structurally as a model that RAMP veterans would try to replicate.

While closed, paid-entry forums are not new, their emergence immediately after a high-profile seizure suggests defensive adaptation. By raising financial and reputational barriers, administrators reduce infiltration risk while signaling seriousness to high-value actors. If historical patterns hold, the next phase will likely involve smaller clusters of trusted actors consolidating around vetted spaces, with recruitment occurring through referrals rather than open posts. This reduces visibility but increases operational cohesion.

While limited information is available about this forum at the time of writing, it clearly advertises a ransomware offering, suggesting an intention to cover the gap that RAMP left in the cybercrime ecosystem (Figure 5). By openly advertising that ransomware is permitted, T1erOne already differentiates itself from forums like XSS or Exploit, which explicitly ban ransomware discussions or operational planning. This signals to operators that T1erOne is a safe space for ransomware-related activity.

⠀

![T1erOne-ransomware-advertisement.png](https://www.rapid7.com/cdn/images/blt2214e700a198dde5/699f0232ba238fe7352f42a5/T1erOne-ransomware-advertisement.png) _Figure 5 - T1erOne ransomware advertisement_

⠀

Early indicators from underground discussions suggest that ransomware affiliate programs have already been referenced in promotional posts on the forum, implying that affiliates may be evaluating T1erOne as a potential coordination hub. Notably, the ransomware group Qilin appears to have established an early presence on the platform, actively advertising its Ransomware-as-a-Service (RaaS) offering in an effort to attract new affiliates (Figure 6). There are also references to the Cry0 ransomware group engaging on T1erOne. At the time of writing, however, neither group has publicly referenced the forum on their known communication channels, which may indicate that activity remains exploratory or limited to closed recruitment efforts rather than representing a fully endorsed migration.

⠀

![Qilin-RaaS-advertisement-T1erOne.jpg](https://www.rapid7.com/cdn/images/bltf53f61cd5384205d/699f186ebc49c46e138a81c1/Qilin-RaaS-advertisement-T1erOne.jpg) _Figure 6 - Qilin RaaS advertisement on T1erOne_

⠀

T1erOne’s branding does more than advertise ransomware; it signals the continuation of an operational niche designed to fill the gap left in the cybercrime market. For defenders, this underscores a critical reality: The takedown of a public ransomware forum rarely ends operations; it alters where and how they occur. Threat actors migrate to smaller, more controlled communities where similar coordination persists, but with reduced transparency and higher barriers to monitoring. In this environment, disruption does not necessarily translate into deterrence. Rather, it drives a restructuring of the ecosystem into tighter, more resilient clusters, preserving operational continuity for threat actors while diminishing visibility for defenders.

### Rehub: Migration to an existing open forum

In parallel with the emergence of T1erOne, ransomware activity has also been observed on Rehub, an underground forum that predates RAMP’s takedown (Figure 7). Domain records indicate that the platform has been active since August 2025, suggesting it was not created in direct response to RAMP’s disruption. However, its recent activity indicates that it is absorbing at least part of the displaced ecosystem.

⠀

![Rehub-feed-screenshot.png](https://www.rapid7.com/cdn/images/blt60c0fe0a26e480f8/699f02e747c5b08a1bc84dbf/Rehub-feed-screenshot.png) _Figure 7 - Screenshot from Rehub’s feed_

⠀

Unlike T1erOne, Rehub does not operate as a gated or reputation-based community. Registration requires only a username, password, and the answer to a basic security question, making entry significantly less restrictive. This low barrier to access contrasts sharply with T1erOne’s paid or reputation-based vetting model.

Rapid7 researchers independently verified that several ransomware actors are already active on the platform. Notably, LockBit and the Gentlemen have maintained a presence on Rehub since September 2025, well before RAMP’s seizure. DragonForce, meanwhile, joined the forum on the same day RAMP was taken offline (Figure 8). The forum contains multiple posts openly advertising or discussing RaaS offerings (Figure 9).

⠀

![Dragonforce-profile-rehub.png](https://www.rapid7.com/cdn/images/bltf99df53f389c9de7/699f032fb009386dea8333b1/Dragonforce-profile-rehub.png) _Figure 8 - DragonForce’s profile on Rehub_

⠀

![Gentlemens-RaaS-advertisement.png](https://www.rapid7.com/cdn/images/blt0b501120bdaf4eca/699f032f62d13904f0846b02/Gentlemens-RaaS-advertisement.png) _Figure 9 - Gentlemen’s RaaS advertisement_

⠀

Rehub’s activity demonstrates that migration following RAMP’s disruption is not limited to newly established, closed communities. Instead, some actors appear to be leveraging pre-existing, lower-barrier platforms to continue coordination and recruitment.

Taken together, T1erOne and Rehub illustrate that post-disruption ecosystems rarely converge immediately around a single successor. Instead, they fragment across parallel coordination spaces before longer-term consolidation emerges.

## Conclusion: Fragmentation, not finality

The post-RAMP landscape reinforces a familiar reality: Law enforcement can dismantle infrastructure, but it rarely dismantles the ecosystem behind it. Instead, disruption fractures trust and redistributes coordination across multiple platforms.

What has emerged is not a single successor, but diverging migration paths. Gated forums like T1erOne reflect an attempt to rebuild trust through exclusivity, tighter vetting, and higher-entry barriers. At the same time, platforms like Rehub demonstrate that some ransomware actors are leveraging accessible, pre-existing forums to maintain operational continuity and recruitment momentum. This fragmentation suggests adaptation rather than decline. In the immediate aftermath of disruption, dispersion appears to be the dominant pattern, not consolidation.

For defenders, this shift complicates visibility. Monitoring strategies can no longer focus on a single dominant forum. Instead, security teams must track actor migration patterns across multiple environments, identify early RaaS recruitment signals, and correlate underground developments with intrusion activity. As coordination spreads across both gated and open platforms, contextual and timely intelligence becomes critical.

At Rapid7, we continuously monitor underground ecosystems to detect migration trends, emerging coordination spaces, and shifts in affiliate behavior before they scale into campaigns. By combining deep threat intelligence with frontline incident response insights, we help organizations maintain situational awareness even as ransomware coordination becomes more distributed and less predictable.

RAMP’s takedown represents meaningful disruption, but not deterrence. As the ecosystem restructures across both exclusive and open platforms, defenders must adapt just as quickly to maintain the advantage.

## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)