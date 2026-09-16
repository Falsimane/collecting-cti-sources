# CrowdStrike’s Fight Against the Rise of Identity-Based Attacks

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/crowdstrikes-fight-against-identity-based-attacks/
- **Date :** August 24, 2023

---

# Amid Sharp Increase in Identity-Based Attacks, CrowdStrike Unveils New Threat Hunting Capability

## New managed identity threat hunting service addresses rapid increase in Kerberoasting and other identity-based attacks

August 24, 2023

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Adversaries are doubling down on identity-based attacks. According to _[Nowhere to Hide: CrowdStrike 2023 Threat Hunting Report](/en-us/resources/reports/threat-hunting-report/)_ , we’ve seen an alarming 583% year-over-year increase in Kerberoasting attacks — a form of identity-based threat — and a 147% increase in access broker advertisements on the dark web. Adversaries are evolving their tradecraft, building custom tooling and leveraging more than usernames and passwords to breach your environments. Are you ready to defend against these types of attacks?

Against this backdrop, [CrowdStrike Counter Adversary Operations](/en-us/blog/crowdstrike-debuts-counter-adversary-operations-team/) recently introduced a new identity threat hunting capability as part of [CrowdStrike Falcon® OverWatch Elite™](/en-us/services/managed-services/falcon-overwatch-threat-hunting/elite/). Available at no additional charge to customers of Falcon OverWatch Elite and CrowdStrike Falcon® Identity Protection, the Falcon OverWatch Elite Identity Threat Hunting capability offers a new level of cross-environment visibility and early detection of compromised credentials to stop breaches.

## Trends Explained

What’s driving the need for identity threat hunting? Let’s examine two identity-related attack trends from the CrowdStrike 2023 Threat Hunting Report.

### Trend #1: 583% increase in Kerberoasting attacks

[Kerberoasting](/en-us/cybersecurity-101/cyberattacks/kerberoasting/) is a technique adversaries use to obtain valid credentials for Active Directory (AD) service accounts. These accounts are hot targets because they often provide higher privileges and allow attackers to lurk undetected for longer stretches of time. They’re also notoriously difficult to detect amid everyday telemetry, further increasing their popularity with cybercriminals.

The sudden spike in Kerberoasting attacks follows several notable events that happened within a three-month span:

  * The disclosure of CVE-2022-33679, a new Kerberos vulnerability published on Sept. 13, 2022, which targets Windows domain accounts with pre-authentication disabled and attempts an encryption downgrade attack
  * The release of a proof-of-concept script exploiting this vulnerability by Bdenneu on GitHub on Nov. 2, 2022, allowing unauthenticated Kerberoasting
  * The release of Orpheus, a Kerberos attack tool that acts as a wrapper for a modified version of Impacket’s GetUserSPNs.py script, on Nov. 16, 2022



Also contributing to the rise in Kerberoasting is the sheer popularity of Microsoft Active Directory (AD): [90% of Fortune 1000](https://www.frost.com/frost-perspectives/active-directory-holds-the-keys-to-your-kingdom-but-is-it-secure/\)) companies use Active Directory. The abuse of Active Directory mechanisms to gain access, escalate privileges and persist in target environments undetected is a common theme among today’s more advanced cyberattacks. Even organizations with mature cybersecurity programs and intimate knowledge of Active Directory [can still be breached](/en-us/blog/observations-from-the-stellarparticle-campaign/), heightening the need to hunt for identity threats.

A closer look at the techniques involved in identity-based attacks reveals how attackers are relying on older tactics while exploring new ones. Kerberoasting is an old and well-understood technique — however, our experts also observed the abuse of network provider dynamic link libraries (DLLs) as a means to harvest valid credentials. A network provider DLL enables the Windows operating system to communicate with other types of networks by supporting different networking protocols.

This newly documented sub-technique sees adversaries operate without the need to interact with services that are often highly monitored by security tools, including the Windows Local Security Authority Subsystem Service (LSASS). It provides an evasive way for them to access valid account data.

### Trend #2: 147% increase in access broker advertisements on the dark web

In the past 12 months, CrowdStrike Falcon® Intelligence observed a 147% increase in access broker advertisements in criminal or underground communities, a notable jump from the 112% increase reported in the [CrowdStrike 2023 Global Threat Report](/en-us/global-threat-report/) published early this year. These advertisements often sell compromised credentials that adversaries can purchase and use to breach target organizations.

This increasing supply of compromised credentials indicates a growing demand among adversaries looking to buy these credentials for follow-on activity. Why the demand? By purchasing valid credentials, adversaries don’t need to leverage traditional vulnerability exploits to breach organizations. Instead, they can simply log in to victim environments and move laterally toward their objectives.

Given how easy initial access has become, it’s no wonder that 62% of all interactive intrusions involve the abuse of valid accounts, with 34% of intrusions specifically involving the use of domain accounts or default accounts, according to the [CrowdStrike 2023 Threat Hunting Report](/en-us/resources/reports/threat-hunting-report/).

## Stop Identity Attacks with CrowdStrike

The onslaught of identity-related attacks requires new defensive countermeasures. Identity threat hunting is a nascent practice that uses identity telemetry to identify potential intrusions and safeguard an organization's network and systems. By continuously monitoring user behaviors, access controls and authentication mechanisms, threat hunters can detect threats that specifically target user credentials, allowing organizations to undertake proactive mitigation and defensive actions

Here’s what CrowdStrike Falcon OverWatch Identity Threat Hunting capabilities can do:

### Detect Compromised Credentials

Supplementing endpoint telemetry with identity telemetry empowers organizations to monitor for and detect compromised user accounts. By analyzing user identity data, login patterns and authentication data, Falcon OverWatch threat hunters can promptly identify signs of compromised credentials, such as brute-force attacks, account takeover, privilege escalation or suspicious login activities from unfamiliar locations or devices. This early detection allows us to take immediate action to mitigate the impact of unauthorized access in customer environments, including fast, closed-loop communications and direct phone escalations.

### Threat Hunt with the Power of the Crowd

With access to trillions of telemetry events from the AI-powered CrowdStrike Falcon® platform, CrowdStrike uses the power of the crowd to quickly identify potential indicators of compromise and detect sophisticated attacks such as advanced persistent threats. This approach improves the accuracy and efficiency of our identity threat detection, helping organizations outpace adversaries.

### Identify Lost or Stolen Credentials on Deep Dark Web

Lost or stolen credentials on the dark web pose a significant risk as adversaries exploit this information for unauthorized access. We leverage Falcon Intelligence victimology data to identify compromised credentials on the dark web and use it as a lead with Falcon OverWatch Identity Threat Hunting. This integrated approach strengthens our ability to detect and respond to potential breaches, mitigating the risk of credential-based attacks.

## Get Peace of Mind with 24/7 Coverage

Today’s adversaries have their sights set on identity. With our new Falcon OverWatch Identity Threat Hunting capability, CrowdStrike is leading the way in managed threat hunting, giving customers peace of mind with an always-on service to help them outpace rampant identity threats.

#### Additional Resources

  * _Experience the power of the Falcon platform at Fal.Con 2023, the cybersecurity industry’s most anticipated annual event.[ Register now](/en-us/events/fal-con/) and meet us in Las Vegas, Sept. 18-21._
  * _Visit the[ Falcon OverWatch Elite webpage](/en-us/endpoint-security-products/falcon-overwatch-threat-hunting/elite/) to learn more about managed threat hunting._
  * _Explore the latest threats in[ Nowhere to Hide: CrowdStrike 2023 Threat Hunting Report](/en-us/resources/reports/threat-hunting-report/)._
  * _Learn more about[ CrowdStrike Counter Adversary Operations](/en-us/press-releases/crowdstrike-unleashes-new-counter-adversary-operations/)._
  * _See CrowdStrike Counter Adversary Operations in action in this[ 3-minute demo](/en-us/resources/videos/crowdstrike-counter-adversary-operations-demo/)._
  * _Listen to the Counter Adversary Operations[ episode](/en-us/resources/adversary-universe-podcast/) of the Adversary Universe podcast.

_



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)