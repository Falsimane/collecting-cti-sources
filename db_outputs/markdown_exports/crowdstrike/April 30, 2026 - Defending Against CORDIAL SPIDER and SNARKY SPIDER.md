# Defending Against CORDIAL SPIDER and SNARKY SPIDER

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/defending-against-cordial-spider-and-snarky-spider-with-falcon-shield/
- **Date :** April 30, 2026

---

# Defending Against CORDIAL SPIDER and SNARKY SPIDER with Falcon Shield 

April 30, 2026

• [ Falcon Shield - Counter Adversary Operations](/en-us/blog/author.falcon-shield---counter-adversary-operations/ "Posts by Falcon Shield - Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Since October 2025, CrowdStrike Counter Adversary Operations has observed a shift in intrusion tradecraft: Threat actors are executing high-speed, SaaS-centric attacks that bypass traditional endpoint visibility. CORDIAL SPIDER and SNARKY SPIDER exemplify this evolution as distinct adversaries conducting rapid data theft and extortion campaigns with striking operational similarities. 

In most cases, these adversaries use voice phishing (vishing) to direct targeted users to malicious, SSO-themed adversary-in-the-middle (AiTM) pages, where they capture authentication data and pivot directly into SSO-integrated SaaS applications. By operating almost exclusively within trusted SaaS environments, they minimize their footprint while accelerating time to impact. The combination of speed, precision, and SaaS-only activity creates significant detection and visibility challenges for defenders. 

This blog details how these adversaries operate and how CrowdStrike Falcon® Shield identifies and disrupts their attacks.

## How AiTM Pages Enable Initial Access

During vishing calls, CORDIAL SPIDER and SNARKY SPIDER impersonate IT support and create urgency around account issues or security updates to direct employees to fraudulent AiTM pages. These domains closely mimic legitimate corporate login portals (e.g., <companyname>sso[.]com, my<companyname>[.]com, <companyname>id[.]com, <companyname>internal[.]com). When users enter their credentials, the adversaries capture authentication data and active session tokens in real time. Because the AiTM proxy relays authentication to the legitimate service, users often see a normal login experience and remain unaware of the compromise.

In most observed cases, these credentials grant access to the organization’s identity provider (IdP), providing a single point of entry into multiple SaaS applications. By abusing the trust relationship between the IdP and connected services, the adversaries bypass the need to compromise individual SaaS apps and instead move laterally across the victim's entire SaaS ecosystem with a single authenticated session.

Falcon Shield is built to detect these anomalous sign-in attempts. While adversaries attempt to blend in with legitimate activity by aligning source location, device fingerprint, and working hours, Falcon Shield applies advanced anomaly detection to surface subtle deviations. By combining a deep understanding of authentication flows with visibility into network characteristics, anonymization services, and session-clustering methods, Falcon Shield reliably identifies malicious access attempts. 

![Figure 1. This Falcon Shield detection details a suspicious sign-in pattern consistent with AiTM phishing attacks.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-1?wid=1308&hei=1120&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 1. This Falcon Shield detection details a suspicious sign-in pattern consistent with AiTM phishing attacks.

![Figure 2. This Falcon Shield detection identifies geographic anomalies when users access platforms from locations inconsistent with their baseline behavior.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-2?wid=1304&hei=1160&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 2. This Falcon Shield detection identifies geographic anomalies when users access platforms from locations inconsistent with their baseline behavior.

## Persistence Through MFA Manipulation

Following initial access, CORDIAL SPIDER and SNARKY SPIDER establish persistence by registering adversary-controlled multifactor authentication (MFA) devices to compromised accounts. This allows them to maintain access while appearing to authenticate from a newly “trusted” device and reduces the need to repeatedly interact with the victim’s legitimate MFA factors.

In many cases, the adversaries first remove existing MFA devices before registering their own. When performing this technique, SNARKY SPIDER almost exclusively enrolls a Genymobile Android emulator for MFA, which enables them to operate connected Android devices across Linux, Windows, and macOS devices.1 CORDIAL SPIDER, by contrast, has used a broader mix of mobile devices and a Windows Quick Emulator (QEMU) device for MFA.

Notably, in some instances, adversary-controlled devices were the first MFA device registered to long-standing accounts where MFA had not previously been enabled. In other instances, the same MFA device was enrolled across multiple compromised accounts, further streamlining adversary access and persistence.

![Figure 3. This Falcon Shield detection identifies suspicious device registration patterns where a single device is added to multiple accounts.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-3?wid=1310&hei=1032&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 3. This Falcon Shield detection identifies suspicious device registration patterns where a single device is added to multiple accounts.

![Figure 4. This Falcon Shield detection identifies suspicious MFA enrollments originating from Android emulator platforms. Attackers exploit emulated environments to register malicious MFA factors and maintain persistent access.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-4?wid=1296&hei=994&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 4. This Falcon Shield detection identifies suspicious MFA enrollments originating from Android emulator platforms. Attackers exploit emulated environments to register malicious MFA factors and maintain persistent access.

## Defense Evasion Through Notification Suppression

Immediately after enrolling attacker-controlled MFA devices, the adversaries move to suppress user-facing indicators of compromise (IOCs). This often includes deleting automated security emails that notify users of suspicious activity, preventing discovery of unauthorized device registration, and conducting other malicious follow-on activities.

SNARKY SPIDER maintains their evasion efforts by systematically deleting security-related communications. The adversary creates inbox rules to automatically delete incoming messages containing keywords such as "alert," "incident," "MFA," and other security terms, effectively filtering out security notifications before they reach the user. By removing these signals at the source, the adversary reduces the likelihood of detection and prolongs unauthorized access.

![Figure 5. This Falcon Shield detection identifies manual deletion of security-related emails by users whose activity originates from flagged ASNs. This behavior typically indicates post-compromise cleanup activities, insider threat evidence destruction, or malicious actors covering data exfiltration traces.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-5?wid=1278&hei=1034&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 5. This Falcon Shield detection identifies manual deletion of security-related emails by users whose activity originates from flagged ASNs. This behavior typically indicates post-compromise cleanup activities, insider threat evidence destruction, or malicious actors covering data exfiltration traces.

![Figure 6. This detection identifies suspicious inbox rules patterns commonly used by threat actors to evade detection or maintain persistent to compromised accounts.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-6?wid=649&hei=682&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 6. This detection identifies suspicious inbox rules patterns commonly used by threat actors to evade detection or maintain persistent to compromised accounts.

## Targeted Discovery: Identifying High-Value SaaS Data

CORDIAL SPIDER and SNARKY SPIDER conduct targeted searches across SaaS platforms to identify high-value sensitive data. Observed search queries include terms such as "confidential," "SSN," "contracts," and "VPN," reflecting a focus on business-critical documents, internal communications, proof-of-concept materials, and infrastructure access credentials.

This search-driven approach enables the adversaries to quickly prioritize sensitive content and accelerate their progression from initial access to data exfiltration.

![Figure 7. This Falcon Shield detection identifies users conducting targeted searches for sensitive terms. This behavior is often associated with reconnaissance or data discovery activities.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-7?wid=1304&hei=1156&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 7. This Falcon Shield detection identifies users conducting targeted searches for sensitive terms. This behavior is often associated with reconnaissance or data discovery activities.

![Figure 8. This Falcon Shield detection identifies users who performed searches for sensitive content following an anomalous sign-in. This behavior is often associated with reconnaissance or data discovery activities.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-8?wid=986&hei=849&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 8. This Falcon Shield detection identifies users who performed searches for sensitive content following an anomalous sign-in. This behavior is often associated with reconnaissance or data discovery activities.

## High-Volume Exfiltration Across SaaS Environments

![Figure 9. SNARKY SPIDER begins exfiltration in under an hour](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-9?wid=1400&hei=490&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 9. SNARKY SPIDER begins exfiltration in under an hour

The primary objective of both CORDIAL SPIDER and SNARKY SPIDER is large-scale data exfiltration across SaaS platforms, including SharePoint, HubSpot, Google Workspace, and more. Once access is established, they move quickly to aggregate and download diverse datasets from all accessible SaaS services.

These compromises are not the result of security vulnerabilities in the SaaS platforms themselves, but rather, weaknesses in customer configurations. Common issues include the absence of phishing-resistant MFA and access controls that grant overly permissive access to sensitive data. 

Falcon Shield provides comprehensive guidance to identify and remediate these misconfigurations, helping organizations reduce exposure and strengthen defenses against SaaS-focused attacks. 

![Figure 10. This Falcon Shield detection identifies when a user downloads a large number of files while connected from an IP address that is unusual for both the user and the organization.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-10?wid=1328&hei=1224&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 10. This Falcon Shield detection identifies when a user downloads a large number of files while connected from an IP address that is unusual for both the user and the organization.

![Figure 11. This Falcon Shield detection identifies when a user downloads files at a volume or velocity that significantly deviates from their established baseline behavior.](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Shield-11?wid=1308&hei=1016&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 11. This Falcon Shield detection identifies when a user downloads files at a volume or velocity that significantly deviates from their established baseline behavior.

## Infrastructure Behind the Campaigns

Throughout these campaigns, CrowdStrike identified network indicators tied to commercial VPN services and residential proxy networks. Unlike traditional VPNs that route traffic through data center IP addresses, residential proxies leverage IPs assigned to real home users, making malicious activity appear as legitimate residential traffic. 

CORDIAL SPIDER and SNARKY SPIDER rely heavily on these services to evade IP-based detection and blend in with normal user behavior. Observed providers include Mullvad, NetNut, 9Proxy, Infatica, and NSOCKS. 

Falcon Shield's infrastructure detection capabilities enable defenders to identify and track these high-risk connection sources, exposing adversary activity that would otherwise appear benign.

## Built for Modern Attacks: Falcon Shield Detections

CORDIAL SPIDER and SNARKY SPIDER highlight a growing detection gap. While many organizations have strengthened endpoint defenses against data exfiltration, fewer have the visibility required to detect adversaries operating within the IdP and SaaS layers.

## The Three Detection Pillars of Falcon Shield

  1. **Deep SaaS expertise:** The Falcon Shield detection engineering team has built a deep understanding of SaaS platforms, including authentication flows, user behaviors, and platform-specific entities and configurations. This expertise enables precise, high-fidelity detections tailored to each supported SaaS application.
  2. **Advanced anomaly detection:** Falcon Shield applies advanced anomaly detection to distinguish malicious activity from legitimate use, using its visibility across the entire SaaS stack, enhanced with additional CrowdStrike Falcon® platform modules. By leveraging statistical models and entity-aware analysis — across users, service accounts, OAuth applications, API tokens, and more — Falcon Shield evaluates each action in context. This includes factors such as network artifacts, zero trust network access solutions, device telemetry, and historical behavior across SaaS providers.
  3. **New-age network intelligence:** Falcon Shield extends beyond traditional IOC-based detection by identifying and classifying anonymization services, clustering adversarial infrastructure, and flagging non-enterprise-grade servers used as access points. Through active scanning, integration with CrowdStrike reputation systems, and proactive engagement with malicious infrastructure, Falcon Shield delivers precise attribution of suspicious activity to attacker-controlled proxy nodes.



Together, these three pillars provide a robust and adaptable detection framework, and minimize noise while surfacing high-confidence activity in real time. In addition to its detection capabilities, [Falcon Shield](https://www.crowdstrike.com/en-us/platform/falcon-shield/) delivers SaaS security posture management (SSPM) to proactively and continuously monitor identities, access controls, and configuration settings. This enables organizations to address weaknesses before they can be exploited and prioritize the most critical issues for remediation, strengthening overall SaaS security posture.

To see these innovations in action, request a free [Falcon Shield risk review](https://www.crowdstrike.com/en-us/platform/falcon-shield/saas-security-risk-review/) or [try it free for 15 days](https://www.crowdstrike.com/en-us/products/trials/try-falcon-shield/). [Contact](https://www.crowdstrike.com/en-us/contact-us/) your representative to explore how CrowdStrike can empower your business to thrive in today’s dynamic and SaaS-first digital landscape.

#### Additional Resources

  * _Dive deeper into topics like this at[Fal.Con 2026](https://www.crowdstrike.com/en-us/events/fal-con/las-vegas/?utm_medium=evt&utm_source=blog&utm_campaign=fal-con-26&utm_term=crwdblogs&utm_language=en-us) with expert-led sessions, hands-on training, and real-world insights._
  * _Read the[CrowdStrike 2026 Global Threat Report](https://www.crowdstrike.com/en-us/global-threat-report/) for the latest insights on adversaries, tradecraft, and activity._
  * _Learn more about Falcon Shield by visiting the[product page](https://www.crowdstrike.com/en-us/platform/falcon-shield/). _
  *  _Visit the[Counter Adversary Operations](https://www.crowdstrike.com/en-us/platform/threat-intelligence/) webpage to learn about CrowdStrike’s threat intelligence and hunting solutions._



1 https[:]//github[.]com/genymobile/scrcpy

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)