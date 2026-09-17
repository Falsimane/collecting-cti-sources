# 5 Holiday Tips to Secure Your Organization from Access Brokers

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/five-holiday-tips-to-defend-against-access-brokers/
- **Date :** November 16, 2023

---

# 5 Tips to Defend Against Access Brokers This Holiday Season

## Access brokers are decking the halls with advanced social engineering scams and vulnerability exploits to blend in with normal users and make a quick profit by selling credentials and other access methods.

November 16, 2023

• [ Bart Lenaerts-Bergmans](/en-us/blog/author.bart-lenaerts-bergmans/ "Posts by Bart Lenaerts-Bergmans") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


The holiday season brings a shift in how people and businesses operate: Some companies may partially shut down, leaving only a skeleton crew to manage their IT environments, while others head into their busiest time of year. This seasonal change in staffing and business operations, combined with the general holiday distraction, often creates risk and makes organizations more vulnerable to cybercrime.

Access brokers — the threat actors who gain and sell access to organizations and simplify eCrime for other cybercriminals — are especially active during this time of year. CrowdStrike data reveals spikes in access broker activity toward year’s end. They capitalize on these seasonal shifts to craft holiday social engineering campaigns, steal more information and make more money by selling their findings to threat actors on underground forums.

Here, we discuss how the threat landscape typically changes during the holidays, how access brokers fit into the cybercrime ecosystem and adapt their activity for this busy time of year, and how organizations can prepare for a safe and secure season.

## Meet the Access Brokers

Access brokers have become a pivotal part of the eCrime ecosystem by selling victim access to other threat actors and facilitating myriad criminal activities. Their operations continue to grow: [CrowdStrike observed](/en-us/resources/reports/threat-hunting-report/) a 147% increase in access broker advertisements across criminal underground communities from July 2022 to June 2023.

Many access brokers have relationships with [big game hunting](/en-us/cybersecurity-101/ransomware/big-game-hunting/) (BGH) ransomware operators and affiliates of prolific [ransomware-as-a-service (RaaS)](/en-us/cybersecurity-101/ransomware/ransomware-as-a-service-raas/) programs. The holiday season is a prime opportunity for ransomware operators to launch ransomware campaigns, extort victims and find potential targets. Access brokers support ransomware operators with this last task by capitalizing on holiday changes to breach organizations and sell access to other adversaries.

In order to defend against access brokers, you must first understand how they operate.

Many access brokers carefully study their victims. They analyze organizations’ attack surfaces to find vulnerabilities they can exploit or use sophisticated social engineering techniques to trick employees and steal credentials. Access brokers seek the path of least resistance into an organization and have quickly adapted as endpoint detection and response (EDR) capabilities have evolved to better detect them. The use of custom malware to gain initial access has dropped substantially — [71% of intrusions in 2022 were malware-free](/en-us/global-threat-report/) — as threat actors favor more subtle attack methods.

Access brokers are highly organized. They advertise access to victims on underground forums, often categorizing their offerings with contextual details such as business vertical, revenue and asset exploitation. This information is especially valuable to big game hunters selecting their next victim. In some cases, access brokers may eliminate upfront costs for downstream ransomware operators using a profit sharing model. These announcements strengthen the collaboration between access brokers and big game hunters, making the eCrime ecosystem a formidable opponent for all organizations.

## Why Access Brokers Welcome the Holidays

Over the past year, access broker advertisements peaked right before and after the holiday season. Spikes were also observed the week before Easter as well as the beginning of the new academic year. While this pattern is not set in stone, access brokers seem to be more active during these moments for several reasons:

  * **Leaner staff:** IT and security teams may have a skeleton staff during the holidays, leaving fewer people to handle detection tuning, threat hunting or patching. As a result, access brokers have more opportunities to break in unnoticed. Dwell time (the time before getting detected) is likely longer during these low-staff moments, giving access brokers a bigger window of opportunity to get in, steal more data and sell it.
  * **It’s vacation time:** Employees often take time off during this time of year. Some may have forgotten their passwords by the time they come back from a week’s holiday. When requesting new credentials, users are more vulnerable to phishing attacks. Access brokers know when users come back and have greater success when many users request new credentials.
  * **More distractions:** IT support or help desk teams may cover only the bare essentials, skipping regular security best practices. Access brokers have recently impersonated regular users and opened support calls to obtain access. If the IT team doesn’t properly validate their information, for example, the attacker will have an easier path in.
  * **Business is booming:** Industries such as the retail, hospitality and travel sectors enter one of their busiest times of the year. They are in a weaker position during the extortion process because they need to keep business running during the busy season and avoid regulatory violations. With this knowledge in mind, access brokers will advertise access to these organizations at the right moment, with adjusted pricing, knowing other adversaries will want to strike.



Let’s take a closer look at the most popular tactics access brokers use to gain entry into victim organizations.

### Well-crafted Social Engineering Campaigns

One of the most notorious actors discovered in 2023, known for both access brokerage and big game hunting, used advanced [social engineering](/en-us/cybersecurity-101/social-engineering/) to harvest credentials. The actor targeted multiple verticals such as consumer goods, telecommunications and real estate. In many cases, ransomware was deployed.

Throughout these incidents, the adversary was consistent in using social engineering tactics to bypass [multifactor authentication (MFA)](/en-us/cybersecurity-101/identity-protection/multifactor-authentication-mfa/). They relied on a combination of [credential-harvesting](/en-us/cybersecurity-101/cyberattacks/credential-harvesting/) websites, [SMS phishing](/en-us/cybersecurity-101/social-engineering/phishing-attack/smishing-attack/), SIM swapping, MFA push-notification fatigue and social engineering via vishing to obtain initial access. Once inside, the adversary avoided using unique malware, instead favoring a wide range of legitimate remote management tools to maintain persistent access.

This actor succeeded because they very carefully studied their victims and knew how to impersonate them later. During the holidays, when users are more relaxed and staff is short, access brokers using similar tactics can increase their chance of success.

### Web Exploitation and Living-off-the-Land

Another common access broker method involves exploitation of public-facing applications and remote code execution vulnerabilities to gain access. Once inside, the threat actor becomes persistent by deploying standard web shell mechanisms to harvest information related to machine identities (SSH keys, RSA keys). Using standard command-line tools, the actor can even clear system logs to evade detection.

## How to Defend Against Access Brokers During the Holidays and Beyond

  1. **Understand your environment:** The age-old adage **“** You can’t protect what you can’t see” has never been so true. Over the past few years, organizations have accelerated their use of cloud infrastructure, resulting in a larger digital footprint. Security teams must gain an outside-in view of their full [enterprise attack surface](/en-us/products/exposure-management/falcon-exposure-management/) in order to identify areas of exposure and close security gaps. Don’t wait for the adversary to strike. Map your assets, visualize attack paths and address them.


  2. **Prioritize identity protection:** The rise in malware-free attacks, social engineering and similar attempts to steal and use credentials drives the need for [strong identity protection](/en-us/products/identity-protection/). [CISA’s Shields Up](https://www.cisa.gov/shields-up) initiative urges organizations to enforce MFA and identify and quickly assess unusual network behavior. Conditional risk-based access policies are advised to reduce the burden of MFA for legitimate users.



Social media training is crucial: Don’t announce department shutdowns or IT service changes on social media, and instruct employees to refrain from sharing personal data on social channels. Train staff to avoid sharing credentials in support calls, emails or tickets. And finally, don’t publish executive or IT contact details on the company website — it may aid adversaries in impersonation efforts.

  3. **Strengthen cloud protection:**[The number of observed cloud exploitation cases grew by 95% year-over-year in 2022](/en-us/global-threat-report/). Adversaries are aggressively targeting cloud infrastructure and using a broad array of tactics, techniques and procedures to compromise critical business data and applications in the cloud. Stopping cloud breaches requires agentless capabilities to protect against misconfigurations, control-plane and identity-based attacks, and also runtime security to protect cloud workloads.


  4. **Know your adversary:** Organizations spend vast amounts of time and money fighting ghosts and noisy alerts, never knowing the “who, why and how” behind cyberattacks. If you don’t understand your adversary, you are poorly prepared to face them.



Invest in threat intelligence that exposes the humans behind the attack, as well as their motivation, capabilities and tools. Use threat intelligence that continuously scans underground forums for exposed identities and leaked data, and notifies the security team when company credentials are detected. Monitor for websites or newly created domains that mimic your organization. If you don’t have time or resources, work with a third party to mitigate the risk of these look-alike websites.

  5. **Practice makes perfect:** Encourage an environment that routinely performs tabletop exercises and red/blue teaming to identify gaps and eliminate weaknesses in your cybersecurity practices and response.



Prepare how to outpace the adversary with comprehensive visibility into what’s happening on your endpoints. Hunt for hidden intruders by looking for web shells and remote monitoring tools that may be active in your environment. Seek support from expert teams that know access brokers and their tools to help mitigate hidden threats.

Access brokers continue to conduct advanced exploitation, social engineering and spear-phishing attacks to gain and sell credentials throughout the year. The end of the year is an ideal time for them to act: IT support organizations are distracted, security teams have a skeleton staff and users request new credentials when they return. Implement strong defenses and don’t let access brokers stuff their stockings with your credentials during the holidays.

#### Additional Resources

  * _Learn more about the adversaries targeting your business in the[CrowdStrike Adversary Universe](/content/crowdstrike-www/locale-sites/us/en-us/adversaries)._
  * _Check out the[Adversary Universe podcast](/en-us/resources/adversary-universe-podcast/) to listen to “The Rise of Access Brokers.”_
  *  _Read more about adversaries and their tactics, techniques and procedures in the[ CrowdStrike 2023 Global Threat Report](/en-us/global-threat-report/) and in the [CrowdStrike 2023 Threat Hunting Report](/en-us/resources/reports/threat-hunting-report/)._
  * _[Watch this demo to see CrowdStrike Falcon® Intelligence in action](/en-us/products/threat-intelligence/falcon-intelligence-automated-intelligence/)._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)