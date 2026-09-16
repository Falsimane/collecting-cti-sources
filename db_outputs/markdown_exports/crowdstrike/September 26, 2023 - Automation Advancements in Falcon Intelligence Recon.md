# Automation Advancements in Falcon Intelligence Recon

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/falcon-intelligence-recon-automation-advancements/
- **Date :** September 26, 2023

---

# Automation Advancements in Falcon Intelligence Recon: Disrupt the Adversary and Reduce Risk

## As security workloads continue to increase, automation becomes a must to maintain operational efficiency.

September 26, 2023

• [ Bart Lenaerts-Bergmans](/en-us/blog/author.bart-lenaerts-bergmans/ "Posts by Bart Lenaerts-Bergmans") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Adversaries are continuing to expand their attacks by adding tactics like domain abuse, multifactor authentication (MFA) fatigue and unique crafted exploit kits acquired from underground forums. Typosquatted domains pose a risk for any organization as they are used at the start of the attack chain, with the goal of misdirecting users to a look-alike site to steal their identities. Once the attacker obtains access, the race is on to obtain lateral movement (i.e., find new targets) within the victim environment. The [CrowdStrike 2023 Threat Hunting Report](/en-us/resources/reports/threat-hunting-report/) indicated an average breakout time of 79 minutes, with a fastest observed breakout of just 7 minutes — meaning security teams need to take immediate action, quickly and decisively, not just during business hours but any day or time of the week to eliminate further escalation into a breach.

## Don’t Ignore Early Warnings from Digital Risk Protection (DRP)

As a result, digital risk protection (DRP) is no longer an option. It has become a must-have tool, enabling security teams to discover the adversaries outside the perimeter during the pre-attack phase. One critical DRP use case is detecting when the attacker stands up malicious infrastructure with the intention to steal identities. Another use case is providing the ability to continuously scan for exposed credentials on the dark web or exposed data sources. While setting up monitoring for these two use cases is relatively easy, it can also result in a substantial new level of effort to an already overloaded security operations staff. Depending on the threat actor's creativity and the volume of discovered exposed credentials, dozens or even hundreds of new alerts can be generated in a matter of hours. Tracking and acting on all of these alerts require human effort and may involve the use of multiple tools to mitigate the risk. The complexity and time to remediate gives the adversary an extended opportunity to succeed. To ensure security teams don’t miss these critical events and can immediately take the right action, CrowdStrike has added multiple automation features directly into [CrowdStrike Falcon® Intelligence Recon](/en-us/products/threat-intelligence/falcon-intelligence-recon/) digital threat monitoring. Falcon Intelligence Recon users now have access to multiple integration triggers and conditions within Falcon Fusion, CrowdStrike’s extensible security orchestration automation and response (SOAR) framework built to simplify enterprise workflows, customize automation, and streamline IT and security operations.

## Use Case 1: Block Typosquatting Domains

As mentioned earlier, typosquatting domains pose a risk for all organizations, and security teams must take immediate action to reduce risks from brand abuse. While a “takedown” is typically a logical remediation step, it is often slow and unsuccessful, especially if the malicious infrastructure is outside the control capabilities of a legitimate organization. Falcon Intelligence Recon has introduced a new “Report to blocklist” capability, which enables security analysts to report the unsafe domain to industry “blocklists” used by CrowdStrike and its partners to prevent users from interacting with the domain.

These blocklists provide data about potential threats to third-party technology providers, including email and web browser providers, registrars and hosting providers, and industry working groups. Reporting to these blocklists allows security and application providers to block the domains within their own products and protect their downstream users. Blocklisting domains is faster than traditional domain takedowns and is more effective than firewall-based blocking alone within an organization.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/09/Figure1-4.png)](/content/dam/crowdstrike/www/en-us/wp/2023/09/Figure1-4.png)Figure 1. Falcon Intelligence Recon “Report to blocklist” feature (showing simulated demo domain) (click to enlarge)

## Use Case 2: Instantly Mitigate Exposed Credentials

In July 2023, [Falcon Intelligence Recon](/en-us/products/threat-intelligence/falcon-intelligence-recon/) extended its capabilities to send exposed passwords to [CrowdStrike Falcon® Identity Protection](/en-us/products/identity-protection/) modules. Falcon Identity Threat Detection and Falcon Identity Threat Protection enable hyper accurate threat detection and real-time prevention of identity-based attacks, combining the power of advanced AI, behavioral analytics and a flexible policy engine to enforce risk-based conditional access.

The automation between Falcon Intelligence Recon and Falcon Identity Protection modules enables security teams to detect and instantly mitigate exposed identities fully automated or with minimal manual intervention

This is how it works. As Falcon Intelligence Recon discovers an organization's exposed credential by monitoring forums on the dark web, it passes the credential to Falcon Identity Protection, significantly raising the risk score for the user. Based on a user configured policy, Falcon Identity Protection will take action — for example, by forcing a password reset or enforcing [multifactor authentication (MFA)](/en-us/cybersecurity-101/identity-protection/multifactor-authentication-mfa/) for the user. The actions provide both awareness about the risk as well as automated remediation of the risk.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/09/Figure2-5.png)](/content/dam/crowdstrike/www/en-us/wp/2023/09/Figure2-5.png)Figure 2. Integration of Falcon Intelligence Recon and Falcon Identity Protection (click to enlarge)

It is important to understand that this capability does NOT require any additional SOAR tool, configuration or setup. It is simply enabled as part of the Falcon platform. Falcon Intelligence Recon and Falcon Identity Protection customers automatically gain the benefit of mitigating risk posed by exposed credentials.

## Use Case 3: Automated Ticketing and Notification

To enhance collaboration and remediation, security teams often use ticketing tools such as Jira or ServiceNow. Notifications from Falcon Intelligence Recon can now be forwarded into these tools to improve workflow and tracking of issues by IT asset owners.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/09/Figure3-3.png)](/content/dam/crowdstrike/www/en-us/wp/2023/09/Figure3-3.png)Figure 3. Falcon Intelligence Recon automated workflows (click to enlarge)

By leveraging Falcon Fusion for automated playbooks, the combined solution provides integration and automation flexibility via a broad series of webhooks (APIs) to external systems such as third-party ticketing systems, where many organizations initiate and coordinate alert triage and response. Covered use cases include forwarding of Falcon Intelligence Recon notifications such as identified access broker credential sales, discovered typosquatting domains and exposed data located on the dark web to ticketing systems.

## Benefits

Adversaries move fast, so protectors need to move even faster. Too often, complex and time-consuming tasks drown security teams and reduce the overall effectiveness of the security program. Workflow simplification, streamlining and task automation are required to disrupt the actor. The new automation features in Falcon Intelligence Recon offer security teams the following benefits:

**Enhanced speed and cost savings:** Automation enables cybersecurity processes to be executed quickly and accurately with minimal or without manual intervention. Tasks that would otherwise take hours or days to complete can now be accomplished within seconds. Speed is crucial when it comes to keeping the security operations team efficient and effective in their fight against adversaries. Access to automated security systems, built into the Falcon platform, also drives cost savings, requiring less human interaction while eliminating costly integration development, testing and maintenance. Falcon Intelligence Recon automation capabilities are predesigned and handled within the same environment, and setup time is minimal.

**Consistency and accuracy:** Human error and lack of expertise are inherent risks in manual processes. By automating cybersecurity tasks, organizations can achieve greater consistency and accuracy in executing security measures. Automated systems consistently follow predefined rules and procedures, reducing the risk of human error. Automation allows cybersecurity measures to be applied uniformly and consistently across a large number of systems and devices, enabling organizations to manage security at scale without sacrificing effectiveness.

**Reduced risk to safeguard reputation:** Automated incident response workflows help teams to act faster, resulting in quicker containment or mitigation of the attack. As adversaries achieve faster breakout times, security teams need every advantage they can get to lower their threat risk profile, avoid the financial repercussions caused by data breaches and minimize organizational downtime.

## Stop Breaches and Disrupt the Adversary with the Falcon Platform

Adversaries move fast. Stealing identities for initial access can happen in minutes. The new automation advancements built into Falcon Intelligence Recon underscore how CrowdStrike’s industry-leading Falcon platform plays a vital role in strengthening an organization's security posture and enhances efficiency in the fight against the adversary.

#### Additional Resources __

  * _To learn more, visit the[ Falcon Intelligence Recon webpage](/en-us/products/threat-intelligence/falcon-intelligence-recon/)._
  * _Watch this[ short demo](https://www.youtube.com/watch?v=0PjOLMuLIrA) to see how Falcon Intelligence Recon enables organizations to proactively uncover fraud, data breaches and phishing campaigns to protect their brand from online threats that target their organization._
  * _Attend a[ Falcon Encounter Hands-On Lab](https://criminalunderground.splashthat.com) to experience Falcon Intelligence Recon and monitor activity across criminal forums, domain registrations and underground communities to gain early warnings on emerging threats to your business._
  * _Join this on-demand CrowdCast to see how you can start monitoring the broad eCrime ecosystem to prevent your organization from becoming the next victim:[ Exposing the Adversary Beyond the Perimeter](/en-us/resources/crowdcasts/exposing-the-adversary-beyond-the-perimeter/)._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)