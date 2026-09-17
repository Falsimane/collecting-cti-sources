# Increase in supply chain attacks will continue to occur

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/software-supply-chain-attacks-gained-traction-in-2017-and-are-likely-to-continue/
- **Date :** March 20, 2018

---

# Software Supply Chain Attacks Gained Traction in 2017 and Are Likely to Continue

March 20, 2018

• [ Michael Busselen](/en-us/blog/author.michael-busselen/ "Posts by Michael Busselen") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


One of the important topics covered in the [CrowdStrike® 2018 Global Threat Report](/en-us/resources/reports/2018-crowdstrike-global-threat-report-blurring-the-lines-between-statecraft-and-tradecraft/) is the increase in supply chain attacks in 2017. This topic was also highlighted in a [recent webcast featuring](/en-us/resources/crowdcasts/2018-crowdstrike-global-threat-report/) CrowdStrike VP of Intelligence Adam Meyers, who joined with CTO Dmitri Alperovitch to offer an in-depth analysis of the findings in this year’s report. Meyers began his discussion of supply chain attacks by commenting, “This is probably the thing that keeps me up at night when I look at what has changed in 2017.” He goes on to explain that the industry has long talked about supply chain attacks as a potential vector. “In a lot of people’s minds, they were thinking of hardware and chips — like microprocessors. But what we found in 2017 was that software as a supply chain attack became something that was realistic and viable,” Meyers said. Meyers stated that the magnitude of such an attack vector is what makes it so terrifying. Virtually every organization in the world, whether in the public or private sector, depends on third-party software, which can include a wide-range of applications. Imagine the multitude of different types of software used for accounting, HR and countless other specialized functions. He explained what makes things worse is that many of these programs were developed by small vendors that aren’t necessarily using the security development lifecycle (SDLC) process. [SDLC](https://www.crowdstrike.com/cybersecurity-101/secops/software-development-lifecycle-sdlc/) is a step-by-step process designed to help developers build more secure software and ensure security compliance requirements are being met. Software supply chain attacks are also challenging because the vulnerabilities in many of these software programs are difficult to detect. “The attackers are exploiting software and trust that existed well before the vulnerability is identified or the attack takes place. This makes it very difficult to nail down the problem or figure out how it occurred,” Meyers said. He explained that most organizations use legitimate software that updates automatically and silently — making it difficult to verify and see what activity is occurring. He also warned that the effectiveness of software supply chain attacks in 2017 puts the supply chain at greater risk going forward as these tactics are leveraged by more actors, particularly those associated with nation-states. The CrowdStrike Falcon® Intelligence™ team analyzed a number of software supply chain attacks in 2017 that were tied to nation-state threat actors. The following is an overview of some major global incidents:

  * [NetSarang](https://www.scmagazine.com/shadowpad-attack-sabotaged-netsarang-software-with-backdoor/article/682295.html)/[CCleaner:](/en-us/blog/protecting-software-supply-chain-deep-insights-ccleaner-backdoor/) Both of these back-door attacks on legitimate applications point to China-nexus threat actors, and used the technique of compiling malware directly into the compromised software. In CCleaner, the attacker modified a function so the execution flow was routed to a custom function meant to decode and load the malware. The intel team observed that NetSarang delivered PlugX linked to WICKED PANDA. Similarities between these attacks, such as command-and-control tactics and code overlaps, suggest they are connected to the same threat actor.
  * M.E. Doc: This attack was aimed at a tax-accounting application, M.E. Doc, made by a Ukrainian company, and began when threat actors comprised the company’s update server and sent [NotPetya](/en-us/blog/petrwrap-technical-analysis-part-2-further-findings-and-potential-for-mbr-recovery/) to unsuspecting victims. XDATA ransomware was also distributed via M.E. Doc in June 2017 and possibly as early as April, when access to the infected update services became available.
  * [PyPi:](https://arstechnica.com/information-technology/2017/09/devs-unknowingly-use-malicious-modules-put-into-official-python-repository.html) This attack compromised the popular Python programming language by replacing libraries on PyPi servers with packages altered to include a check-in beacon. Although the attribution for this attack remains unclear, Falcon Intelligence analysis suggests this was possibly a proof-of-concept or gray-hat incident. Regardless of its origins, it underscores the supply chain threat to user-curated systems.



Get an in-depth analysis of other information in the threat report including valuable insights that can inform your security strategy for 2018 and beyond:

  * Download the [CrowdStrike 2020 Global Threat Report ](/resources/reports/2020-crowdstrike-global-threat-report.html)



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)