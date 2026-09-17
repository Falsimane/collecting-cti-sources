# Ransomware Increases the Back-to-School Blues | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/ransomware-attacks-increase-during-back-to-school/
- **Date :** September 17, 2019

---

# Ransomware Increases the Back-to-School Blues

September 17, 2019

• [ AdamM](/en-us/blog/author.adamm/ "Posts by AdamM") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


As students all over the United States donned their backpacks and packed their lunches to go back to school this year, the all-to-familiar impact of [ransomware](/epp-101/what-is-ransomware.html) created confusion and disarray for school districts. In June, reports of [WIZARD SPIDER](/en-us/blog/wizard-spider-lunar-spider-shared-proxy-module/) targeting school districts with [Ryuk ransomware](/en-us/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/) began to emerge; victims of Ryuk receive ransom demands ranging from hundreds of thousands to millions of dollars to unlock encrypted files. Unfortunately, the trend of large-scale ransomware attacks, dubbed “big game hunting,” has become pervasive across the internet with multiple threat actors such as [PINCHY SPIDER](/en-us/blog/pinchy-spider-adopts-big-game-hunting/), [INDRIK SPIDER](/en-us/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/), [DOPPEL SPIDER](/en-us/blog/doppelpaymer-ransomware-and-dridex-2/), and WIZARD SPIDER dominating the space. 

## Adversaries Focus on Operational Sensitivity

Big game hunting adversaries over the last 18 months have focused on organizations with an operational sensitivity, where downtime is particularly problematic. [CrowdStrike® Intelligence ](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)has identified targets in many sectors, including healthcare, manufacturing, managed services and media. This summer, the trend has focused on state and local governments and has most recently impacted public library systems and school districts. The operational imperative for these targets, combined with budgetary restrictions and the widespread lack of cybersecurity resources, has led to an escalating series of attacks and disrupted services. All across the United States we have observed cities, counties, towns and schools report that their systems were compromised and their services suspended or they are operating in an ad hoc capacity. 

## Increasing the Pressure to Pay

The targeting of school districts during the summer and fall does not appear to be a random occurrence. Cybercriminals look for compelling events to increase the pressure on the victim to pay the ransom, and the back-to-school time frame, when districts are beginning to open their doors and welcome students, is the perfect time to maximize this pressure. Ransomware impacts the computers of administrators and students alike. In some cases telecommunication systems and even the ability to pay for school lunches have been disrupted. Also, the targeting of schools in the U.S. has not been geographically concentrated. There have been attacks reported across the U.S. and there could be more that have not garnered public attention or been publicly reported. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2019/09/US-map-ransomware-attacks-schools-copy-1.png) The CrowdStrike Intelligence eCrime team has identified that in many cases the threat actors appear to have coordinated these ransomware attacks before the first day of school to maximize the impact and compel the victims to pay. In addition, the window of time between the attack and the first day of school is getting smaller with the latest attacks reported just last week. 

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2019/09/chart-of-schools2-1.png) Breach Information Sourced from Public Reporting

Schools appear to be the current, preferred target of big game hunting adversaries, but it is important to consider the trends of these actors and the calendar of events throughout the year. Events such as the elections in November and holiday celebrations in December provide appealing opportunities for these threat actors to continue to prey on state and local government targets and to amplify the pressure on victims to avoid disruption by paying the ransom. 

## Malware Loaders and Banking Trojans

As has been previously reported by CrowdStrike, big game hunters often leverage malware loaders and banking Trojans to gain an initial foothold into victim environments before deploying ransomware. In Q2 2019, CrowdStrike Intelligence reported that nearly 75 percent of all eCrime observed fit into these three categories with a direct correlation between some of them, such as the use of Trickbot and Ryuk by the threat actor tracked as WIZARD SPIDER. This adversary has also sometimes employed Emotet, operated by MUMMY SPIDER, to distribute Trickbot. 

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2019/09/eCrime-Types-Chart-1.png) Distribution of eCrime Threat Types in Q2 2019

## The 1-10-60 Rule

Once the adversary gains their initial access to the target environment, the clock is ticking. This is where the [CrowdStrike 1-10-60 rule](https://www.fifthdomain.com/thought-leadership/2018/08/17/why-you-should-follow-the-1-10-60-rule-of-cybersecurity/) becomes critical: **detecting the breach within one minute, investigating in under 10 minutes, and remediating the threat within 60 minutes**. The [CrowdStrike Falcon®® OverWatchTM](/en-us/endpoint-security-products/falcon-overwatch-threat-hunting/) managed hunting team has observed that threat actors can, on average, “break out" within 58 minutes, meaning these adversaries can jump from an initially compromised machine to escalate privileges and move across the enterprise within an hour, after which remediation becomes much more complicated. 

## Visibility is Key

The solution to this problem comes down to visibility. If you cannot see your endpoints or workloads and what is happening on them, then investigation and remediation become infinitely more complicated. 

#### Additional Resources

  * _Learn how the CrowdStrike Falcon® platform protects schools and government entities from ransomware and other damaging threats by visiting the[Falcon for Public Sector webpage. ](/en-us/solutions/government-public-sector/)_
  *  _For more information on how to incorporate intelligence on dangerous threat actors into your security strategy, please visit the[CrowdStrike Falcon® Intelligence product page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Download the[CrowdStrike 2020 Global Threat Report.](/resources/reports/2020-crowdstrike-global-threat-report.html)_
  * _Test CrowdStrike next-gen AV for yourself. Start your[ free trial of Falcon Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) today._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)