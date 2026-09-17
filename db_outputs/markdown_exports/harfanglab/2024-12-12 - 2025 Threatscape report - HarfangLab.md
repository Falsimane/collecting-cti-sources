# 2025 Threatscape report - HarfangLab

- **Source :** harfanglab
- **URL :** https://harfanglab.io/insidethelab/2025-cyber-threatscape-predictions/
- **Date :** 2024-12-12

---

Looking ahead to 2025, we acknowledge that predicting the future is never an exact science. However, by analyzing emerging trends and patterns, we aim to anticipate the risks that could shape the cybersecurity landscape in the year to come, with a particular focus on Europe.

Rather than reiterating obvious or widely discussed predictions, this report delves into nuanced and underexamined possibilities that could have significant implications. By identifying these potential risks, we aim to provide decision-makers at all levels with thoughtful and informed perspectives to better prepare for the challenges ahead.

This report is structured into three key sections. First, we review our predictions from last year, evaluating how they materialized. Next, we examine the blindspots — emergent threats that we did not foresee but have since come to light. Finally, we present our predictions for 2025, focusing on complex and overlooked risks to help decision-makers navigate an increasingly uncertain environment.

In brief:

  * **Internet Balkanization will intensify** as national-technological identities continue to solidify, driving further fragmentation of the global internet.
  * **Agentic AI solutions** gaining traction in the industry will likely become a target for attackers, who may also leverage these systems in their operations.
  * **Internet’s foundational knowledge increasingly hurt** as threat actors leverage AI to insert bias and influence narratives across the internet, poisoning the same datasets that others use for training AI.
  * **The near-miss open-source supply chain attack of 2024** could inspire more threat actors to exploit the open-source model, integrated into widely used software ecosystems.
  * **Seemingly inconsequential large-scale cyberattacks from 2024** may be repurposed in 2025 as strategic tools in hybrid warfare campaigns.
  * **Private companies and civil organizations** will play an increasingly prominent role as proxies in conflicts, reflecting their growing influence in the cybersecurity landscape.
  * **Network manipulation will escalate** , with state and private actors exploiting control over internet infrastructure to manipulate, intercept, or disrupt traffic.



## Reviewing last year’s predictions

As we enter 2025, it’s important to first reflect on our predictions from the previous year before exploring new and emerging threats. Our 2024 predictions1 proved accurate in several key areas, though some threats unfolded in ways we didn’t fully anticipate.

### More cyber information operations influencing public opinion (and more cyber attacks in support of such operations)

Our 2024 prediction about increased cyber-enabled information operations proved accurate with significant developments documented throughout the year. The Doppelgänger operation showed unprecedented growth, with publications covering their activities increasing from 7 in 2023 to 25 in 20242. We documented their operation in our report3 covering their mid-year activities. This surge highlights the operation’s adaptability and persistence, showing continued infrastructure adaptation to evade detection. By October 2024, the UK sanctioned4 key stakeholders of the Doppelgänger network, including the Social Design Agency (SDA). This move followed previous sanctions in the US 5, and the exposure of Doppelgänger operations earlier in this year through leaked SDA documents6, revealing tactical insights and operational structure, though their self-reported effectiveness metrics warrant significant skepticism7.

The Paris 2024 Olympics became a focal point for information operations. VIGINUM identified 43 distinct information operations targeting the Games8. While Russian actors posed the highest risk, leveraging cyberattacks to disrupt the event and amplify disinformation narratives related to their exclusion9, Chinese state-sponsored actors presented a distinct threat through cyber espionage operations10. Iranian actors also participated, targeting Israeli athletes parcticipating in the Olympics with threats attributed to a fabricated French far-right group11.

Conclusion: Fulfilled ✅

### Hacktivist serving as an extension of state-sponsored cyber capabilities

The forecasted blurring of lines between hacktivist groups and state-sponsored actors materialized significantly throughout 2024, particularly in relations to geopolitical conflicts such as the Russia-Ukraine and the Israel-Hamas wars. Analysis revealed that Russian military group Sandworm cultivated multiple personas to claim responsibility for wartime disruptive operations and amplify narratives of successful disruption12. Other notable examples of state-sponsored hacktivism include the pro-Iran CyberAv3ngers, which the US government linked directly to the Islamic Revolutionary Guard Corps (IRGC), and the pro-Israel “Gonjeshke Darande” (Predatory Sparrow), which Iranian authorities attributed to Israel.

The scale of hacktivist operations has grown substantially, often used to conceal state operations13. ENISA’s 2024 report14 highlighted nearly 3,662 hacktivist incidents, many linked to the Russia-Ukraine war, alongside a surge in groups aligned with Iranian interests, targeting Western entities.

A particularly noteworthy trend is the fluid alignment of these groups with multiple causes. For instance, following Hamas’ October 7 attack on Israel, several Russia-aligned hacktivist groups expressed pro-Palestinian support and initiated cyber attacks against Israel, while pro-Palestinian groups began targeting countries perceived as Ukrainian allies. A notable example from late 2024 is the significant DDoS campaign against France which began on August 26, 2024, following the arrest of Telegram CEO Pavel Durov by French authorities. The campaign involved both pro-Russian and pro-Palestinian hacktivist groups targeting over 50 French organizations, including government agencies and private companies. The groups used hashtags like #FreeDurov and #opDurov, with some expressing support for Telegram while others cited patriotic motives in defense of a Russian national15.

Conclusion: Fulfilled ✅

![Faketivists Illustration](https://harfanglab.io/medias/2024/12/hacktivists-2.png)

### More direct attribution of cyber attacks

Our 2024 prediction that state actors would become more direct in attributing cyber operations has been fulfilled — not through states openly claiming responsibility, but through significant changes in attribution dynamics. Attribution has become faster, more assertive, and increasingly reliant on less publicly available evidence, particularly in the context of the ongoing war in Ukraine, where it is used as a strategic and political tool.

CERTs and CSIRTs have played a key role in this shift, frequently publishing reports linking cyberattacks to specific states or threat actors16,17,18,19. Overall, attribution has become more strategically focused, particularly during wartime. Conflicts like the war in Ukraine have lowered the evidentiary threshold for attribution claims, enabling states to use attribution as a tool to support diplomatic or strategic objectives — such as imposing sanctions — with even less technical evidence than traditionally offered. This shift reflects a growing emphasis on leveraging attribution to shape narratives and advance geopolitical agendas.

Attribution has also grown faster and more precise when it comes to information operations (IO). Coordinated efforts by the US, EU, and UK have rapidly identified actors behind influence campaigns20, with sanctions imposed swiftly. By reducing the evidentiary requirements for public attribution, states have made it a more accessible and flexible tool for advancing geopolitical strategies.

Conclusion: Partially fulfilled ➕➖

### State-Sponsored retaliation against Cybersecurity entities

Following last year’s targeting of private sector security companies, we anticipated seeing more incidents of such attacks reported. While there were follow-up attacks21 in early 2024 on Microsoft, initiated by NOBELIUM in last November 2023, there were no widely reported breaches or retaliatory campaigns specifically targeting cybersecurity firms in 2024.

In a related development, 2024 revealed a significant risk of DPRK agents infiltrating Western companies. Reports indicated that “Dozen of Fortune 100 organizations have unknowingly hired IT workers from North Korea”22, particularly in the U.S. tech sector23. While the primary goal of this operation was to generate revenue for North Korea and circumvent sanctions, some cases went further. For instance, one insider attempt to deploy malware24 was stopped early, and there were reports of DPRK IT workers stealing data and demanding ransom25.

Conclusion: Not fulfilled ❌

### Escalating destructive attacks and the revival of jamming tactics

In 2023, we predicted an “uptick in the use of destructive malware, increasingly employed as non-kinetic weapons in conflicts” along with a “resurgence in more traditional electronic warfare”. In 2024 we’ve seen significant developments in both aspects. A notable example emerged in January when the FrostyGoop malware targeted Ukraine’s energy infrastructure26. This malware was particular significant as the first ICS-focused malware using the Modbus protocol to cause physical disruptions to operational technology systems. March 2024 brought another sophisticated attack when an updated version of AcidRain, dubbed AcidPour, was deployed against Ukrainian ISPs27. In September 2024, a hybrid (kinetic and electronic warfare) attack detonated thousands of pagers and walkie-talkies used by Hezbollah28 via POCSAG29. This operation showcased how exploiting communication systems and supplychains can achieve both physical destruction and psychological disruption.

Hybrid attacks escalated throughout 2024, driven by the ongoing war between Ukraine and Russia30,31. These operations combined drones, missiles and destructive cyberattacks targeting critical infrastructure. Similarly, the war between Israel and Iranian proxies mirrored this hybrid war with the use of missiles, drones strikes32 and cyberattacks on missile alert systems. The increasing reliance on drones has made electronic warfare (EW) a pivotal aspect of modern conflicts. For example, Russian forces deployed advanced drone jamming systems33, which Ukraine later countered with the help of U.S.-made jam-resistant drones34.

As we mentioned above, 2024 saw a rise in state-sponsored destructive and disruptive attacks. Ransomware attacks surged to unprecedented levels35, and while many attacks were financially motivated, state-sponsored actors increasingly used it as a cover for destructive operations.

While destructive cyberattacks have clearly escalated and EW played a central role in hybrid warfare, these efforts remained concentrated in active military theaters.

Conclusion: Fulfilled ✅

### More attacks leveraging off-radar devices, such as SOHO devices

The attack surface of IoT and SOHO devices has expanded significantly in 2024, with reports indicating a YoY spike of over 100%36,37. Critical vulnerabilities have been identified across multiple vendors’ network devices38, which were exploited for both espionage39 and disruption40 purposes – as DDoS botnets, providing attackers with scalable and stealthy infrastructure. For instance, Chinese APT40 was reported41 to have shifted its staging infra to compromised SOHO devices rather than compromising legitimate websites, reflecting a broader trend.

The challenge of securing these devices is exacerbated by the growing number of internet-facing devices reaching their end of life42 status. In early 2024, the U.S. DoJ announced43 that it disrupted an ORB network used by the Chinese APT “Volt Typhoon”. However, the group reportedly44 rebuilt and restored its ORB network. Similarly, in February 2024, the U.S. DoJ disrupted45 a botnet operated by APT28, following our report46 of related activity. In this case as well, we believe that the threat actor has rebuilt its capacity by now.

Conclusion: Fulfilled ✅

![Compromised network device](https://harfanglab.io/medias/2024/12/soho-3.png)

### Widespread destructive attacks reaching smartphones

While there have not been widespread or highly sophisticated destructive attacks on smartphones, there has been a notable incident involving a mobile wiper. The WIRTE group47, affiliated with Hamas, utilized an Android wiper supporting Hamas, as we reported48 in February.

Conclusion: Partially fulfilled➕➖

### The rise of open-source AI models and the expanding AI attack surface

In 2023, we anticipated widespread adoption of open-source AI models and predicted an increase in the discovery and exploitation of AI vulnerabilities. While 2024 saw significant adoption of AI models, particularly GPTs, across industries, the integration of open-source AI projects was more measured than expected. However, the expansion of the AI attack surface and research into its vulnerabilities accelerated significantly, validating part of our prediction.

Research into AI security vulnerabilities accelerated significantly in 2024. A noteworthy case is the creation of “Morris II”, the first AI worm targeting generative AI systems, demonstrating how AI services could be exploited to spread itself, infect new systems and steal data through adversarial self-replicating prompts. 49. Prompt injection attacks50 remained a persistent issue, exemplified by the Microsoft 365 Copilot vulnerability that allowed exfiltration of sensitive company data51. Critical vulnerabilities in AI tools continued to emerge throughout the year52, though primarily identified through bug bounty programs rather than discoveries in active exploitation.

Interestingly, more APT groups began leveraging AI models for cyber operations. For example, a report by OpenAI highlighted how APTs used proprietary generative models to enhance influence campaigns and conduct cyberattacks53. This showcases that AI is not only a target but also a tool for malicious actors.

Conclusion: Partially fulfilled ➕➖

### A constantly adapting and ever-growing ransomware threat

As anticipated, ransomware incidents surged dramatically in 2024 with a notable increase in both frequency and sophistication. Attack tactics became more aggressive54, with some attackers employing triple extortion – not only encrypting and leaking data but also targeting customers or business partners. The average ransom demand reached unprecedented levels54, likely incentivized by economic sanctions and inflation.

The landscape was expected to shift significantly following the takedown of LockBit in February55 and the disruption to ALPHV in December 202356. While LockBit resurfaced within a week, ALPHV likely executed an exit scam, stiffing their affiliates57. These events contributed to a fragmentation of the ecosystem, with at least 27 new ransomware groups emerging58. The Ransomware-as-a-Service (RaaS) model continued to drive activity, enabling less technically skilled attackers to launch campaigns and received up to 85% of the ransom proceeds. Naturally, there are likely a magnitude of ransomware attacks going unreported59.

Conclusion: Fulfilled ✅

### Critical Infrastructure in the crosshairs and the need for protection frameworks

In 2024, there has been significant global progress in addressing the vulnerabilities of critical infrastructure, particularly in response to the increasing threats posed by geoplotical tensions and cyberattacks. Countries and international organizations have enhanced the security posture of critical assets vital for both civilian and military purposes. For instance, the EU has implemented the “KRITIS umbrella law”60, which encompasses three major directives: the Critical Entities Resilience (CER)61 directive, the Cyber Resilience Act (CRA) and NIS2 (Network and Information Security Directive 2)62. These directives are now coming into effect, aiming to protect critical infrastructure from physical damage by considering all potential risks, including natural hazards, terrorist attacks, insider threats, and sabotage. These initiatives follow past incidents like the Nord Stream pipeline sabotage63 and more recent fibreoptic cable sabotage in the Baltic Sea. The impact of these events has reached as far as Hong Kong, which is on the verge of its first cybersecurity law targeting critical infrastructure64.

A prime example of dual-use communication system is Starlink, the satelite service provided by SpaceX. It was initially activated at Ukraine’s request shortly after Russia’s invasion in 2022, with exceptions for Russian-occupied territories like Crimea, as SpaceX refused to allow its use in combat operations65. Nonetheless, Ukrainan forces have leveraged Starlink to control drones for surveillance and combat operations, prompting SpaceX to create a new business unit called “Starshield”, to cater to military uses of Starlink satellites. This dual-use capability has drawn criticism from Russia, which has reportedly attempted to disrupt Starlink through EW tactics and illegally acquiring terminal to improve their own combat capabilities66.

Conclusion: Fulfilled ✅

## Blind Spots: Unforeseen Emergent Threats

While our 2024 predictions accurately captured multiple emerging threats, several significant developments emerged that few in the threat intelligence community anticipated. These blind spots serve not only as critical learning opportunities but also as a humbling reminder that predicting future threats as well as the year they will materialize with certainty is impossible.

### LibLZMA/XZ Utils Compromise

The discovery of a sophisticated backdoor in XZ Utils in 202467 revealed a concerning blind spot in the security community’s approach to supply chain security: many small, yet critical components of software infrastructure are taken for granted and not subjected to security scrutiny. This widely-used compression utility, pre-installed on most Linux and macOS systems, had been compromised through a meticulously planned operation that went undetected until a Microsoft engineer noticed unusual CPU consumption patterns in SSHD processes.

This incident stands out not only for its technical sophistication but also for its strategic implications. The attackers demonstrated exceptional patience and operational security, orchestrating changes across multiple independent open-source projects to implement their backdoor. The complexity and scope of this operation strongly suggested state-sponsored involvement, although this remained unconfirmed.

This compromise serves a reminder that even seemingly minor software components can pose substantial risks. Perhaps the most sobering realization is that similar compromises could exist in other widely-deployed libraries, remaining undetected for years.

### Cloud Thunderstorms: The Perils of Cloud Security Dependencies

Two significant incidents in 2024 exposed a critical blind spot in cloud security: the dangerous imbalance between organizational dependencies on cloud providers and the reality of shared security responsibilities.

The Snowflake incident68, where a threat actor dubbed UNC5537 exploited stolen credentials to breach multiple customer tenants, revealed how organizations often overlook their security responsibilities while relying heavily on cloud provider capabilities. This incident was initially mischaracterized as a breach of Snowflake itself, though it was actually a coordinated attack on multiple customers through compromised credentials, affecting hundreds of millions of users and resulting in massive data losses.

Similarly, when Storm-0558 exploited vulnerabilities in Microsoft’s cloud infrastructure, as detailed in the CSRB report69, it highlighted how even major providers can fall short of security expectations. The incident’s global impact demonstrated the risks of concentrated dependencies on cloud services, while subsequent Congressional hearings70 emphasized growing concerns about the adequacy of current security standards and practices.

These events expose a systemic issue: organizations increasingly transfer critical data and operations to private cloud providers without always understanding or implementing their part of the shared responsibility model. Additionally, while cloud providers advertise sophisticated security features, the security efforts they implement themselves might not be up to the cumulated customers’ value they hold. As a result, the assumption that providers alone can guarantee security creates a dangerous gap between perceived and actual security postures. This misalignment of security responsibilities, combined with the growing concentration of critical assets in cloud environments, represents an emerging threat that requires urgent attention from both providers and customers.

![Cloud computing thunderstorms](https://harfanglab.io/medias/2024/12/cloud-1.png)

## 2025 Predictions

Drawing from the trends we’ve observed and the lessons learned over the past year, this section presents our key predictions for the cybersecurity landscape in 2025, focusing on emerging threats and evolving challenges.

### Further Internet Balkanization and Technonationalism

Internet balkanization71 and technonationalism, long-discussed topics in global digital discourse, are poised to gain increased prominence in 2025. This trend is driven by geopolitical conflicts and regulatory challenges that highlight the growing divide in how nations manage their digital ecosystems. Recent events, such as the war in Israel, have demonstrated how cyberattacks can lead to digital isolation. During the conflict, Israeli websites faced relentless DDoS attacks among other threats, prompting many to implement geofilters that blocked access from outside the country, thereby safeguarding their services72,73. This approach mirrors past responses to regulatory challenges like the European GDPR, where some U.S. websites opted to block European visitors rather than comply with cumbersome privacy requirements.

China’s “Great Firewall” exemplifies this trend by creating a parallel controlled internet environment that insulates its digital ecosystem from foreign influence, prioritizing digital sovereignty and control. This strategy proved effective during the global CrowdStrike IT outage in 2024, as China avoided major disruptions by relying on domestic providers74. Such measures are part of a broader technonationalism strategy, where countries like China and the U.S. implement strict technological restrictions to protect national interests and maintain control over their digital landscapes75,76.

This trend is not limited to nations; tech giants within these countries are also affected. Companies facing sanctions or operating in conflict zones may find technology lock-in – initially a commercial strategy — becoming a necessity as they replace foreign technologies with domestic alternatives. This shift is driven by both security concerns and the need for technological self-reliance.

As geopolitical tensions rise and state-sponsored actors increasingly leverage destructive cyberattacks, countries and organizations may resort to digital isolation as a defense mechanism. This could lead to a more fragmented internet landscape where access is restricted based on geographic or political considerations. The implications of such balkanization are significant, potentially affecting global communication, commerce and information exchange. Consequently, businesses and governments will need to navigate these complexities balancing security and self-reliance with openness and accessibility.

### More open-source supply chain attacks discovered

We expect that more open-source supply chain attacks will be uncovered in 2025, building on the lesson learned from incidents like the XZ Utils backdoor67,77 and the CSRF-MAGIC compromise78. These cases highlight vulnerabilities inherent in open-source ecosystems, where trust, collaboration, and limited resources leave project exposed to sophisticated attacks. The XZ Utils backdoor, as discussed above, was a highly advanced attack leveraging social engineering and technical obfuscation to insert malicious code into a widely used compression library. Similarly, the CSRF-MAGIC incident demonstrated how subtle backdoors can remain hidden for extended periods, impacting downstream users without detection.

These attacks underscore the systemic risks posed by open-source software, which is deeply integrated into nearly all modern applications. Attackers may increasingly target open-source projects due to their ubiquity and the potential for widespread impact. By compromising a single component, malicious actors can infiltrate countless downstream systems, as seen in prior supply chain compromises (SolarWinds and 3CX).

The feasibility of such attacks has been discussed for over a decade, including in thought experiments like the 2014 FOSDEM keynote79. Recent incidents, however, have proven that these scenarios are not only realistic but achievable. Advanced techniques such as dependency confusion, typo-squatting, and social engineering combined with the inherent trust model of open-source development creates a fertile ground for exploitation.

These developments raise critical questions about the security of open-source software and its role as the backbone of modern technology. Without significant investment in auditing, monitoring, and securing these projects, 2025 could see more open-source supply chain attacks with far-reaching consequences.

### Agentic AI leveraged in attacks

Agentic AI refers to independent decision-making and adaptive execution with minimal human oversight. These systems can autonomously perform complex tasks, making them a valuable tool for automating operations across various environments. However, their proliferation is rapidly expanding and many deployments lack adequate protective measures80.

This autonomy poses substantial risks, as their advanced capabilities make them lucrative targets for threat actors. If security measures are insufficient, these systems can be exploited to execute unauthorised actions, access sensitive data, or disrupt operations81. Additionally, the complexity of Agentic AI complicates compliance with stringent data protection laws such as GDPR, challenging organizations to maintain clear audit trails and accountability.

### Well poisoning to support IO campaigns

The rise of AI-driven technologies and their reliance on web-scale data introduces a new threat: data poisoning, or “well poisoning”. In this technique, attackers inject false or malicious information into potential dataset sources to manipulate AI systems. This technique could play as a key tool for long-term information operations (IO), enabling adversaries to influence public narratives and disrupt fact-checking processes, and erode trust in AI-generated outputs.

Data poisoning exploits the dependence of AI models on open-source datasets scraped from the internet. Attackers can manipulate these datasets by posting and amplifying public content. For instance, researchers have shown that poisoning just 0.01% of training data can significantly alter the behaviour of large language models (LLMs)82. This low-cost, high impact method makes it an attractive tactic for adversaries.

The implications are far-reaching. Poisoned AI systems could provide harmful medical advice, fail to detect fraud in financial systems, or ignore specific threats in cybersecurity tools. Such attacks threaten not only the integrity of AI technologies but also critical sectors reliant on accurate decision-making. As AI becomes more autonomous and integral to public discourse and operations, organizations must prioritize securing training datasets and implementing robust validation mechanisms.

### Strategic malware deployments pre-positioned for 2025 operations

As we approach 2025, the potential for strategic cyberattacks leveraging pre-positioned malware is a pressing concern. The RomCom malware, attributed to a Russia-aligned actor, has been deployed in recent campaigns across Europe and North America83,84. These operations exploited two zero-day vulnerabilities in Mozilla FireFox and Windows, chained together to enable an almost zero-interaction infection through malvertising.

The large-scale deployment of RomCom might have actually served as a strategic pre-positioning, offering attackers the statistical advantage of possibly infiltrating systems of interests and establishing footholds within target organizations. The absence of immediate impact — despite the use of multiple high-value zero-days — suggests that this campaign is laying the groundwork for future operations rather than delivering immediate results. This deliberate choice may also serve as a smokescreen (the same vulnerability chain could have been used to deploy a few distinct stealthier payloads), deterrence or a warning signal.

Given the ongoing war in Ukraine and heightened geopolitical tensions, these compromises could later be mobilized into large-scale attacks in 2025, targeting critical sectors like energy during high-stake periods, such as Europe’s winter energy peak.

![Europe illuminated](https://harfanglab.io/medias/2024/12/strategic-3.png)

### Proxies in Cyberwarfare: Private companies and civil organizations

In 2025, we anticipate a growing reliance on private companies, security firms, and civil organizations as proxies in cybersecurity operations. Governments, political parties, intelligence agencies, and corporations are likely to increasingly utilize these privately-owned entities to disrupt adversary operations. This could involve strategic information disclosures to NGOs, journalists, or media outlets, either transparently or covertly orchestrated, to “burn” adversary assets or influence public opinion. Such tactics allow sponsoring states to maintain plausible deniability while alleviating the burden of dealing with official processes and resource allocation in achieving these tasks.

At the same time, frustration over perceived inaction by governments or law enforcement agencies may drive private companies and civil organizations to act independently against cyber threats and information operations. These actions could include exposing cybercriminals, disrupting state-sponsored campaigns, or even engaging in counter-hacktivism. With their growing capabilities, these non-state actors now have the means to take significant actions on their own initiative. In some cases, they may receive covert support or funding from political parties, intelligence services, or corporations affected by cyberattacks.

However, this trend raises critical concerns about accountability and legality. Independent actions — particularly those involving hackback tactics or unregulated offensive measures — blur the lines between legitimate defensive measures and rogue behaviour, creating potential risks for escalation and unintended consequences in the global cybersecurity landscape.

### Shaping the Internet: Network-level attacks in 2025

In 2025, we expect an increase in the use of network assets — controlled by either state actors or private entities — to manipulate, intercept, or disrupt internet traffic. While Border Gateway Protocol (BGP) hijacking remains a prominent example, this threat extends beyond BGP to include broader tactics leveraging control over internet routing and infrastructure.

For instance, state-owned ISPs may throttle or block access to specific services during politically sensitive events, while rerouting traffic through adversarial networks could be leveraged to intercept unencrypted data or analyze metadata. Cryptocurrency transactions also remain a lucrative target, with attackers using traffic redirection to steal funds, as seen in past incidents involving forged BGP announcements targeting blockchain networks85. These evolving tactics highlight the strategic value of traffic manipulation in modern hybrid warfare.

Both nation-states and private entities, including ISPs, smaller Autonomous Systems (AS), and hosting providers with high concentrations of malicious infrastructure may abuse their connections to major networks for purposes such as espionage, censorship, financial gain, or disruption.

Historically, BGP hijacking has been used for various purposes, including espionage and theft86,85. In 2024, for example, a European mobile carrier suffered a BGP hijack due to compromised credentials, causing hours of service disruptions87.

Nation-states like Russia have demonstrated the strategic value of controlling network traffic during conflicts. In April 2023, a large-scale BGP hijack redirected traffic from over 200 major cloud providers and content delivery networks through Russia’s state-owned telecom provider Rostelecom, disrupting services for hours88. While efforts to improve BGP security began in earnest in 202489, the protocol remains fundamentally vulnerable, leaving it susceptible to exploitation by both state and non-state actors.

* * *

  1. <https://harfanglab.io/insidethelab/2024-cyber-threatscape-predictions/> ↩

  2. <https://www.disinfo.eu/doppelganger-operation/> ↩

  3. <https://harfanglab.io/insidethelab/doppelganger-operations-europe-us/> ↩

  4. <https://www.gov.uk/government/news/uk-sanctions-putins-interference-actors> ↩

  5. <https://home.treasury.gov/news/press-releases/jy2195>, <https://www.justice.gov/opa/pr/justice-department-disrupts-covert-russian-government-sponsored-foreign-malign-influence> ↩

  6. <https://vsquare.org/leaked-files-putin-troll-factory-russia-european-elections-factory-of-fakes/> ↩

  7. <https://www.foreignaffairs.com/russia/lies-russia-tells-itself> ↩

  8. <https://www.sgdsn.gouv.fr/files/files/Publications/20240919_NP_SGDSN_VIGINUM_Summary%20information%20threat%20Paris2024Games_EN_0.pdf> ↩

  9. <https://blogs.microsoft.com/on-the-issues/2024/06/02/russia-cyber-bots-disinformation-2024-paris-olympics/> ↩

  10. <https://cloud.google.com/blog/topics/threat-intelligence/cyber-threats-2024-paris-olympics> ↩

  11. <https://www.ic3.gov/CSA/2024/241030.pdf> ↩

  12. <https://services.google.com/fh/files/misc/apt44-unearthing-sandworm.pdf> ↩

  13. <https://cloud.google.com/blog/topics/threat-intelligence/global-revival-of-hacktivism> ↩

  14. <https://www.enisa.europa.eu/publications/enisa-threat-landscape-2024> ↩

  15. <https://blog.checkpoint.com/security/hacktivists-call-for-release-of-telegram-founder-with-freedurov-ddos-campaign/> ↩

  16. <https://www.verfassungsschutz.de/SharedDocs/publikationen/DE/cyberabwehr/2024-02-28-joint-cyber-security-advisory.pdf> ↩

  17. <https://cert.pl/en/posts/2024/05/apt28-campaign/> ↩

  18. <https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents> ↩

  19. <https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/apt40-advisory-prc-mss-tradecraft-in-action> ↩

  20. <https://www.gov.uk/government/news/uk-sanctions-putins-interference-actors> ↩

  21. <https://msrc.microsoft.com/blog/2024/01/microsoft-actions-following-attack-by-nation-state-actor-midnight-blizzard/> ↩

  22. <https://www.linkedin.com/posts/charlescarmakal_mandiant-part-of-google-cloud-just-published-activity-7244027392610955267-qw1o/> ↩

  23. <https://cloud.google.com/blog/topics/threat-intelligence/mitigating-dprk-it-worker-threat> ↩

  24. <https://blog.knowbe4.com/how-a-north-korean-fake-it-worker-tried-to-infiltrate-us> ↩

  25. <https://thehackernews.com/2024/10/north-korean-it-workers-in-western.html> ↩

  26. <https://hub.dragos.com/hubfs/Reports/Dragos-FrostyGoop-ICS-Malware-Intel-Brief-0724_r2.pdf?hsLang=en> ↩

  27. <https://www.sentinelone.com/labs/acidpour-new-embedded-wiper-variant-of-acidrain-appears-in-ukraine/> ↩

  28. <https://en.wikipedia.org/wiki/2024_Lebanon_electronic_device_attacks> ↩

  29. <https://en.wikipedia.org/wiki/Radio-paging_code_No._1> ↩

  30. <https://therecord.media/russian-hackers-target-energy-facilities-ukraine> ↩

  31. <https://www.recordedfuture.com/research/russian-sabotage-activities-escalate-amid-fraught-tensions> ↩

  32. <https://en.wikipedia.org/wiki/October_2024_Iranian_strikes_against_Israel> ↩

  33. <https://www.newgeopolitics.org/2024/06/10/ukrainian-drones-vs-russian-jamming/> ↩

  34. <https://www.defenseone.com/technology/2024/10/us-made-jam-resistant-drones-are-helping-ukrainians-cut-through-russia-ew/400735/> ↩

  35. <https://jumpcloud.com/blog/ransomware-attacks-in-2024> ↩

  36. <https://www.forescout.com/resources/2024-riskiest-connected-devices/> ↩

  37. <https://www.sonicwall.com/blog/sonicwall-2024-mid-year-cyber-threat-report-iot-madness-powershell-problems-and-more> ↩

  38. <https://unit42.paloaltonetworks.com/cve-2024-0012-cve-2024-9474/> ↩

  39. <https://www.microsoft.com/en-us/security/blog/2024/10/31/chinese-threat-actor-storm-0940-uses-credentials-from-password-spray-attacks-from-a-covert-network/> ↩

  40. <https://www.f5.com/labs/articles/threat-intelligence/2024-ddos-attack-trends> ↩

  41. <https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/apt40-advisory-prc-mss-tradecraft-in-action> ↩

  42. <https://www.bleepingcomputer.com/news/security/d-link-wont-fix-critical-bug-in-60-000-exposed-eol-modems/> ↩

  43. <https://www.justice.gov/opa/pr/us-government-disrupts-botnet-peoples-republic-china-used-conceal-hacking-critical> ↩

  44. <https://www.computerweekly.com/news/366615485/Chinas-Volt-Typhoon-rebuilds-botnet-in-wake-of-takedown> ↩

  45. <https://www.justice.gov/opa/pr/justice-department-conducts-court-authorized-disruption-botnet-controlled-russian> ↩

  46. <https://harfanglab.io/insidethelab/compromised-routers-infrastructure-target-europe-caucasus/> ↩

  47. <https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/> ↩

  48. <https://harfanglab.io/insidethelab/samecoin-malware-hamas/> ↩

  49. <https://arxiv.org/abs/2403.02817> ↩

  50. <https://arxiv.org/abs/2402.12959> ↩

  51. <https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/> ↩

  52. <https://protectai.com/threat-research/2024-october-vulnerability-report> ↩

  53. <https://cdn.openai.com/threat-intelligence-reports/influence-and-cyber-operations-an-update_October-2024.pdf> ↩

  54. <https://www.trmlabs.com/post/ransomware-in-2024-latest-trends-mounting-threats-and-the-government-response> ↩ ↩

  55. <https://www.justice.gov/opa/pr/us-and-uk-disrupt-lockbit-ransomware-variant> ↩

  56. <https://www.justice.gov/opa/pr/justice-department-disrupts-prolific-alphvblackcat-ransomware-variant> ↩

  57. <https://thehackernews.com/2024/03/exit-scam-blackcat-ransomware-group.html> ↩

  58. <https://cyberint.com/blog/research/ransomware-trends-2024-report/> ↩

  59. <https://www.blackfog.com/the-state-of-ransomware-2024/> ↩

  60. <https://www.openkritis.de/it-sicherheitsgesetz/german_cip_infrastructure_kritis.html> ↩

  61. <https://home-affairs.ec.europa.eu/news/critical-entities-resilience-directive-enters-application-ensure-protection-critical-infrastructure-2024-10-23_en> ↩

  62. <https://www.europarl.europa.eu/RegData/etudes/BRIE/2021/689333/EPRS_BRI(2021)689333_EN.pdf> ↩

  63. <https://mc.nato.int/media-centre/news/2024/nato-officially-launches-new-nmcscui> ↩

  64. <https://www.sb.gov.hk/eng/CI/protection.html> ↩

  65. <https://en.wikipedia.org/wiki/Starlink_in_the_Russo-Ukrainian_War> ↩

  66. <https://www.nytimes.com/2024/05/24/technology/ukraine-russia-starlink.html> ↩

  67. <https://en.wikipedia.org/wiki/XZ_Utils_backdoor> ↩ ↩

  68. <https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion> ↩

  69. [https://www.cisa.gov/sites/default/files/2024-03/CSRB_Review_of_the_Summer_2023_MEO_Intrusion_Final_508c.pdf](https://www.cisa.gov/sites/default/files/2024-03/CSRB%20Review%20of%20the%20Summer%202023%20MEO%20Intrusion%20Final_508c.pdf) ↩

  70. <https://homeland.house.gov/hearing/a-cascade-of-security-failures-assessing-microsoft-corporations-cybersecurity-shortfalls-and-the-implications-for-homeland-security/> ↩

  71. <https://en.wikipedia.org/wiki/Splinternet> ↩

  72. <https://blog.cloudflare.com/cyber-attacks-in-the-israel-hamas-war/> ↩

  73. <https://www.akamai.com/blog/security/akamai-blocked-419-tb-of-malicious-traffic> ↩

  74. <https://www.bbc.com/news/articles/c3g01y047pdo> ↩

  75. <https://www.csis.org/analysis/sovereignty-and-evolution-internet-ideology> ↩

  76. <https://www.csis.org/analysis/balancing-ledger-export-controls-us-chip-technology-china> ↩

  77. <https://www.wired.com/story/xz-backdoor-everything-you-need-to-know/> ↩

  78. <https://www.sonatype.com/blog/the-curious-case-of-csrf-magic-a-case-study-in-supply-chain-poisoning> ↩

  79. <http://freebsd.dk/pubs/FOSDEM_2014.pdf> ↩

  80. <https://unit42.paloaltonetworks.com/privilege-escalation-llm-model-exfil-vertex-ai/> ↩

  81. <https://www.theregister.com/2024/10/02/ai_agent_trashes_pc/> ↩

  82. <https://arxiv.org/html/2410.08811v1> ↩

  83. <https://blog.talosintelligence.com/uat-5647-romcom/> ↩

  84. <https://www.welivesecurity.com/en/eset-research/romcom-exploits-firefox-and-windows-zero-days-in-the-wild/> ↩

  85. <https://blog.coinbase.com/celer-bridge-incident-analysis-895a9fc77e57> ↩ ↩

  86. <https://blog.cloudflare.com/cloudflare-1111-incident-on-june-27-2024/> ↩

  87. <https://deploy.equinix.com/blog/detect-and-prevent-bgp-hijacking-best-practices/> ↩

  88. <https://www.darkreading.com/cyber-risk/101-why-bgp-hijacking-just-won-t-die> ↩

  89. <https://www.theregister.com/2024/09/03/white_house_bgp_security/> ↩




[ ![Gamaredon_Pterodo](https://harfanglab.io/medias/2025/04/chatgpt-image-15-avr-2025-10-15-24-424x283.png) Identifier: TRR250401. Proactively hunting for Russian-nexus threats, we identified samples from the Pterodo malware family, commonly associated with Gamaredon, uploaded to a public malware analysis platform between late 2024 and mid-March 2025. Notably, related Gamaredon Dead Drop Resolvers (DDR) are… ](https://harfanglab.io/insidethelab/gamaredons-pterolnk-analysis/)[ ![MuddyWater_Ongoing_RMM_Campaign](https://harfanglab.io/medias/2024/04/image-3-424x283.png) Identifier: TRR240402. Summary We have been closely monitoring the activities of the Iranian state-sponsored threat actor MuddyWater since the beginning of 2024. Our investigations reveal an active campaign that has been ramping up since October 2023, aligning with the Hamas… ](https://harfanglab.io/insidethelab/muddywater-rmm-campaign/)[ ![A comprehensive analysis of I-Soon's commercial offering](https://harfanglab.io/medias/2024/02/isoon-heading-424x283.png) Identifier: TRR240301. Key Findings I-Soon’s commercial offering reveals that their main issue is processing collected data, not breaching their targets in the first place. Their products leverage deep learning to help them sort and classify stolen documents. The company appears… ](https://harfanglab.io/insidethelab/isoon-leak-analysis/)[ ![suspected_grasshopper_header](https://harfanglab.io/medias/2024/06/suspected-grasshopper-header-424x283.png) Identifier: TRR240601. Summary Hunting for malicious infrastructure possibly targeting the Israeli government, we identified a previously unreported, long-standing and suspicious domain. The latter is still active at the time of this report, and is leveraged as a command and control… ](https://harfanglab.io/insidethelab/supposed-grasshopper-operators-impersonate-israeli-gov-private-companies-deploy-open-source-malware/)