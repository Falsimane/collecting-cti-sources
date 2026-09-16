# Threat Intelligence Foundations: Crawl, Walk, Analyze - Part 1 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/03/09/threat-intelligence-foundations-crawl-walk-analyze-part-1/
- **Date :** 2025-06-02

---

_This is the first post in a three-part series on threat intelligence foundations, discussing the fundamentals of how threat intelligence can be used in security operations._

There is a consensus among many in [threat intelligence](/fundamentals/what-is-threat-intelligence/) that the way the community has approached threat intelligence in the past - i.e, the “Threat Data → SIEM → Magical Security Rainbows” approach has left something to be desired, and that something is usually analysis. Rick Holland (@rickhholland) warned us early on that we were on the wrong track with his 2012 post [My Threat Intelligence Can Beat Up Your Threat Intelligence](https://www.forrester.com/blogs/12-05-22-my_threat_intelligence_can_beat_up_your_threat_intelligence/) where he wrote “The real story on threat intelligence is your organization's ability to develop your own."

There are ways that we can take advantage of the threat intelligence that currently exists while learning how to better leverage the threat intelligence in our own networks. Doing this requires an understanding of intelligence fundamentals and how they can be applied in security operations. This series is designed to help those interested in threat intelligence -whether just starting out or re-evaluating their existing programs - understand the underlying fundamentals of threat intelligence and intelligence analysis.

In the first part of this three-part series we will discuss the levels of intelligence and the various ways threat intelligence can be utilized in operations.

## Threat Intelligence Levels in Security Operations: Crawl

When an organization is determining how to best integrate threat intelligence into their security operations it is helpful to have a framework detailing the different ways that intelligence can be effectively utilized.

Traditionally, intelligence levels have aligned to the levels of warfare: strategic, operational, and tactical. There are several reasons for this alignment: it can help identify the decision makers at each level; it identifies the purpose of that intelligence, whether it is to inform policy and planning or to help detect or deter an attack; it can help dictate what actions should be taken as a result of receiving that intelligence.

At any level of intelligence it is critical to assess the value to your organization specifically. Please answer this for yourself, your team, and your organization, “How does this information add perspective to our security program? What decisions will this information assist us in making?”

## Strategic intelligence

Strategic intelligence is intelligence that informs the board and the business. It helps them understand broader trends that are facing their organizations and other similar organizations in order to assist in the development of a strategy. Strategic Intelligence comes from analyzing longer term trends, and often takes the shape of analytic reports such as the DBIR and [Congressional Research Service (CRS) reports](https://www.fas.org/sgp/crs/misc/R42507.pdf). Strategic intelligence assists key decision makers in determining what threats are most impactful to their businesses and future plans, and what long-term efforts they may need to take to mitigate them.

The key to implementing strategic intelligence in your own business is to apply this knowledge in the context of your own priorities, data, and attack surface. No commercial or annual trend report can tell you what is important to your organization or how certain threat trends may impact you specifically.

#### Strategic intelligence - like all types of intelligence - is a tool that can be used to shape future decisions, but it cannot make those decisions for you.

## Operational Intelligence

Operational intelligence provides intelligence about specific attacks that may impact an organization. Operational intelligence is rooted in the concept of military operations - a series of plans or engagements that may take place at different times or locations, but have the same overarching goal. It could include identified campaigns targeting an entire sector, or it could be hacktivist or botnet operations targeting one specific organization through a series of attacks.

[Information Sharing and Analysis Centers (ISACs)](http://www.nationalisacs.org/) and [Organizations (ISAOs)](https://www.cisa.gov/information-sharing-and-analysis-organizations-isaos) are good places to find operational intelligence.

Operational intelligence is geared towards higher-level security personnel, but unlike strategic intelligence it dictates actions that need to be taken in the near to mid-term rather than the long term. It can help inform decisions such as whether to increase security awareness training, how to staff a SOC during an identified adversary operation, or whether to temporarily deny requests for exceptions to the firewall policy. Operational intelligence is one of the best candidates for information sharing. If you see something that is going on that may impact others in the near term, *please* share that information. It can help other organizations determine if they need to take action as well.

#### Operational intelligence is only useful when those receiving the intelligence have the authority to make changes to policies or procedures in order to counter the threats.

## Tactical Intelligence

Tactical Intelligence focuses on the the “what” ([Indicators of Compromise](/fundamentals/indicators-of-compromise-iocs/)) and the “how” ([Tactics, Techniques, and Procedures](http://ryanstillions.blogspot.com/2014/04/on-ttps.html)) of an attacker's actions with the intent of using that knowledge to prevent, detect, or respond to incidents. Do attackers tend to use a particular method to gain initial access, such as social engineering or vulnerability exploitation? Do they use a particular tool or set of tools to escalate privilege and move laterally? What indicators of compromise might allow you to detect these activities? For a good list of various source of tactical intelligence check out [Herman Slatman's list of threat intelligence resources.](https://github.com/hslatman/awesome-threat-intelligence)

Tactical intelligence is geared towards security personnel who are actively monitoring their environment and gathering reports from employees who report anomalous activity or social engineering attempts. Tactical Intelligence can also be used in hunt operations, where we are looking to identify attacker behaviors that vary only slightly from a typical user's behavior. This type of intelligence requires more advanced resources, such as extensive logging, user behavioral analytics, endpoint visibility, and trained analysts. It also requires a security-conscious workforce, as some indicators may not be captured or alerted on without first being reported by an employee. You will always have more employees than attack sensors…listen to them, train them, gather the information they can provide, analyze it, and then act upon it.

#### Tactical threat intelligence provides specific, but perishable, information that security personnel can act on.

Understanding how threat intelligence operates at different levels can help an organization understand where it needs to focus their efforts and what it can do with the threat intelligence it has access to. It can also help guide how the organization should approach intelligence in the future. The intelligence you can generate from your own network will always be the most actionable intelligence, regardless of the level.

**For more information on the levels of intelligence and the levels of warfare, check out these resources:**

  * [The State of Security: Cyber Threat Intelligence](https://www.tripwire.com/state-of-security?f%5B0%5D=topic%3A2275)



## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)