# How CrowdStrike Traces the Evolution of eCrime

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-crowdstrike-traces-the-evolution-of-ecrime/
- **Date :** June 30, 2022

---

# Tales from the Dark Web: How Tracking eCrime’s Underground Economy Improves Defenses

June 30, 2022

• [ Bart Lenaerts-Bergmans](/en-us/blog/author.bart-lenaerts-bergmans/ "Posts by Bart Lenaerts-Bergmans") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Cybercriminals are constantly evolving their operations, the methods they use to breach an organization's defenses and their tactics for monetizing their efforts.

In the [CrowdStrike 2022 Global Threat Report](/en-us/resources/reports/global-threat-report/), we examined how the frequency and sophistication of ransomware attacks has grown in the past year. CrowdStrike Intelligence observed an 82% increase in ransomware-related data leaks in 2021 compared with 2020; further, we found 62% of attacks use hands-on-keyboard activity — indicating adversaries continuously advance their tradecraft to bypass legacy security solutions and extort victims via highly targeted data leaks. What are the forces driving this growth, and how exactly do cybercriminals make money?

## The Fast-Growing, Lucrative Business Model Enabled by RaaS

Ransomware is not new; adversarial groups have relied on compromises for many years. However, over the past 2-3 years, their strategy has started to shift toward a more community based business model enabled by ransomware-as-a-service (RaaS) platforms that allow smaller, less advanced criminals to join a larger operation.

At the top of this model is an operator who sets up a RaaS platform that takes care of multiple technical tasks such as on-demand ransomware packaging, command and control of deployed ransomware, cryptography, data extraction, archiving, online extortion and others.

Less sophisticated cybercriminals with minimal hacking knowledge can join this operation after being vetted; when they do, they’ll receive 70 to 80% of the paid ransom. These emerging criminals are also assisted by access brokers, through which they can acquire access to the infrastructure of a potential victim. The interaction between all these criminal entities — RaaS operators, vetted affiliates, access brokers and other participants — happen via criminal forums, underground markets and anonymous posts. CrowdStrike continuously monitors these environments, and users may receive alerts regarding market and forum activity.

## Access Brokers: How Adversaries Get In

The eCrime kill chain is often enabled by access brokers, the intruders who gain access to an organization’s infrastructure and then sell illicitly obtained credentials and other access methods to buyers in underground communities.

Adversaries buy compromised credentials to make the process of getting into a target organization easier and more efficient. Access brokers sell a broad range of access types, including financial account logins, business email account credentials, remote access to network assets and custom exploits for IT infrastructure.

To advertise compromised credentials and other access methods on the underground, access brokers use particular keywords and target specific marketplaces. However, their posts often leave behind “breadcrumbs” that offer defenders an opportunity to detect compromised accounts or risks of security incidents. For example, an access broker may include attributes such as company details (size, revenue, industry), IT infrastructure details, the malware used to steal credentials, or the access broker’s alias.

The amount of chatter on underground forums is massive. CrowdStrike’s managed service, CrowdStrike Falcon® Intelligence Recon+ provides security teams assistance by offering custom expertise to monitor and triage threats found in these forums on your behalf. CrowdStrike experts can guide organizations of all sizes to identify unwanted data exposure or threats like account takeovers and brand-targeted attacks.

## Distribution Services: A Force Driving Ransomware

CrowdStrike’s analysis of ransomware campaigns by groups such as Pinchy Spider, also known as REvil, Wizard Spider (Conti) and Carbon Spider (DarkSide) has made it clear the operators behind these campaigns no longer work alone, in particular when compromising assets and injecting the ransomware. Ransomware operators advertise on underground forums to recruit affiliates who can help them [distribute ransomware](/en-us/cybersecurity-101/ransomware/how-ransomware-spreads/) and share the profits.

These affiliates leverage RaaS infrastructure from the operators. After targeting and compromising a victim’s assets, they drop ransomware from the RaaS platform, set the ransom demand and get 70 to 80% of the ransom payment in return. Victims are often chosen based on the likelihood they’ll be able to afford a ransom; affiliates often calculate ransom payouts based on company revenue and business impact to maximize their profits.

Operators provide technical services in return for affiliates’ help in distributing ransomware. They may provide a packager to generate customized ransomware so affiliates can distribute over their own channels; cryptographic key management; or internet infrastructure for [data exfiltration](/en-us/cybersecurity-101/cyberattacks/data-exfiltration/) and storage. They may share payment instructions to receive virtual currencies from victims; secret communication channels to hide affiliates when they talk to victims; and even a help desk to aid victims in paying the ransom. These services give a boost to less tech-savvy adversaries, who benefit from access to technically advanced malware at low cost.

CrowdStrike Intelligence analysts found multiple initial access and lateral movement techniques that affiliates use before deploying ransomware. By changing how they distribute ransomware, adversaries can find new ways to bypass security measures. Below are a few examples of how attackers gain initial access:

  * **Buying stolen credentials from access brokers.** Affiliates often use legitimate credentials to gain a foothold. Remote Desktop Protocol (RDP) is a popular entryway.
  * **Spam or social engineering.** Among the most common initial access vectors.
  * **Vulnerability scanning and exploit kits.** These kits can be found on multiple forums and target specific software or systems to gain access and install additional code . Exploit kits can be combined with phishing campaigns to boost their effectiveness.
  * **Loader and botnet usage.** Loaders, often a step between phishing campaigns and ransomware deployment, use malicious documents like macro-enabled spreadsheets to download and execute malicious code.
  * **Post-exploitation tools and “living off the land.”** Adversaries that access a system will explore the network to find critical data or applications that can help further an attack. Some use system tools like PSExec or PowerShell scripts to remain hidden.



A better understanding of adversary techniques can help improve your defenses. Organizations must know which attackers are targeting their region or industry, whether they are recruiting affiliates, and how their ransomware is distributed.By understanding the adversary and their tools, defenders can employ an intelligence-first defense strategy based on the threats they face.

## Monetization: How Cybercrime Pays

Once ransomware is deployed into a victim environment, the prize needs to be split and monetized into other payment forms. CrowdStrike’s observations of the cybercrime ecosystem offer new insights into adversaries, their transactions and valuation of recent compromises — all of which can help defenders understand how money flows in cybercrime and strengthen their security strategies.

Adversaries constantly evolve their monetization techniques to maximize the chance of payment. Their methods are working: reports from the [U.S. Treasury Department’s Financial Crimes Enforcement Network](https://www.fincen.gov/sites/default/files/2021-10/Financial%20Trend%20Analysis_Ransomware%20508%20FINAL.pdf) (FinCen) and the [Office of Foreign Assets Control](https://home.treasury.gov/policy-issues/office-of-foreign-assets-control-sanctions-programs-and-information) (OFAC) underscore how lucrative ransomware has become. FinCen found the value of suspicious activity detailed in ransomware-related suspicious activity reports (SARs) was $590 million USD in the first six months of 2021 — far higher than the $416 million USD reported in all of 2020. Further, CrowdStrike’s Intelligence team also tracks ransomware demands: in 2021, we calculated an average demand of $6.1 million USD, an increase of 36% from 2020.

If a victim refuses to pay ransom, their data may be auctioned by the [threat actor](/en-us/cybersecurity-101/threat-intelligence/threat-actor/) so they can still make money on it by selling it to other parties or adversaries.

Corporate data is valuable to all adversaries. Once they have it, the data can be easily monetized and present increased risk to your organization if other attackers have access to it. Defenders must develop a stronger understanding of cybercriminals’ behavior — and the broader eCrime ecosystem — in order to make smarter security decisions that best protect data as their most valuable asset.

In the “Tales from the Dark Web” white paper series, we explore the increased specialization of adversaries inside the criminal underground. This includes the changing tradecraft for gaining initial access, achieving lateral movement, exfiltrating data and leveraging it to extort their targets. By understanding how adversaries specialize in these critical areas to gain scale and efficiency, organizations can better prepare their defenses.

Rather than simply illustrate the problems defenders face, the insights from these white papers will arm security teams with actionable information, enabling them to better prepare for the attacks emerging from the criminal underground.

#### Additional Resources

  * _Get more insights into ransomware attacks and eCrime activity at Fal.Con 2022, the cybersecurity industry’s most anticipated annual event.[ Register now](/en-us/events/fal-con/) and meet us in Las Vegas, Sept. 19-21! _
  * _Download the Tales from the Dark Web whitepapers:[ Following Threat Actor Bread Crumbs](/en-us/resources/white-papers/distribution-services-secret-behind-ransomware/), [Distribution Services: Secret Force Behind Ransomware, and ](/en-us/resources/white-papers/distribution-services-secret-behind-ransomware/)[How Cybercriminals Monetize Ransomware Attacks.](/en-us/resources/white-papers/)_
  * _Download the[ 2022 CrowdStrike Global Threat Report ](/en-us/resources/reports/global-threat-report/)._
  * _To learn more about how to monitor criminal forums, visit the[ CrowdStrike Falcon® Intelligence Recon™ product page.](/en-us/products/threat-intelligence/falcon-x-recon/)_
  * _Better understand the adversaries that target your business with a[ free threat briefing ](https://go.crowdstrike.com/threat-intelligence-briefing.html)with a CrowdStrike Intelligence expert._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)