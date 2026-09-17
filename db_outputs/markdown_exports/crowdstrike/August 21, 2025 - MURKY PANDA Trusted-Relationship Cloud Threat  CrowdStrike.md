# MURKY PANDA: Trusted-Relationship Cloud Threat | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/murky-panda-trusted-relationship-threat-in-cloud/
- **Date :** August 21, 2025

---

# MURKY PANDA: A Trusted-Relationship Threat in the Cloud

August 21, 2025

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


  * Since late 2024, CrowdStrike Counter Adversary Operations has observed significant activity conducted by [MURKY PANDA](https://www.crowdstrike.com/adversaries/murky-panda/), a China-nexus adversary that has targeted government, technology, academic, legal, and professional services entities in North America.
  * MURKY PANDA has previously conducted trusted-relationship compromises in the cloud and demonstrates extensive knowledge of cloud environments and custom application logics.
  * The adversary has also shown considerable ability to quickly weaponize n-day and zero-day vulnerabilities and frequently achieves initial access to their targets by exploiting internet-facing appliances. 
  * MURKY PANDA has deployed web shells including _Neo-reGeorg_ during their cyberespionage operations and has access to a low-prevalence malware family tracked by CrowdStrike Counter Adversary Operations as _CloudedHope_.
  * MURKY PANDA operations are likely driven by intelligence-collection objectives to gain access to sensitive information. The adversary has previously exfiltrated emails and other sensitive documents from high-profile targets.



Since 2023, CrowdStrike Services and CrowdStrike Counter Adversary Operations have investigated multiple intrusions conducted by MURKY PANDA, a sophisticated adversary leveraging advanced tradecraft to compromise high-profile targets.

MURKY PANDA, active since at least 2023, is a cloud-conscious adversary with a broad targeting scope; the adversary’s operations have particularly focused on government, technology, academia, legal, and professional services entities in North America. MURKY PANDA is likely motivated by intelligence-collection requirements to gain access to sensitive information; the adversary’s activity aligns with China-nexus targeted intrusion activity tracked by industry sources as [_Silk Typhoon_](https://www.microsoft.com/en-us/security/security-insider/silk-typhoon).

MURKY PANDA’s significant capabilities include their ability to access low-prevalence malware and rapidly weaponize n-day and zero-day vulnerabilities in their cyberespionage operations. The adversary has leveraged trusted-relationship compromises in the cloud and demonstrated a high level of operations security (OPSEC), including modifying timestamps and deleting indicators of their presence in victim environments to avoid detection and hinder attribution efforts. 

Similar to other China-nexus adversaries, MURKY PANDA has exploited internet-facing appliances for initial access and has likely compromised small office/home office (SOHO) devices to use as infrastructure for their operations. 

## Tactics, Techniques, and Procedures (TTPs) and Compromises in the Cloud

### Operational TTPs, Malware, and Tools

MURKY PANDA heavily relies on exploiting internet-facing appliances to gain initial access and has frequently deployed web shells — including the _Neo-reGeorg_ web shell frequently used by China-nexus adversaries — to establish persistence. The adversary also has access to the low-prevalence custom malware family _CloudedHope_. 

**CloudedHope**  
---  
 _CloudedHope_ is a statically linked 64-bit ELF executable developed in Golang and designed to target Linux-based systems; developers likely obfuscated _CloudedHope_ using the open-source tool garble. The executable implements basic remote access tool (RAT) functionality while leveraging multiple anti-analysis and OPSEC measures, including checksum-based comparisons for environment variables and command-line arguments as well as a decoy action to perform should these checksum-based comparisons fail.  
  
The adversary has quickly weaponized n-days and zero-days. They have gained initial access to victim systems by exploiting several vulnerabilities, including [CVE-2023-3519](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX561482) — a vulnerability affecting Citrix NetScaler ADC and NetScaler Gateway. 

MURKY PANDA has likely used compromised SOHO devices geolocated in a given targeted country as their operations’ final exit nodes. Other China-nexus adversaries such as [VANGUARD PANDA](https://www.crowdstrike.com/adversaries/vanguard-panda/) have leveraged this TTP, likely to hinder detection and disruption by law enforcement by masking their malicious activity on the victim system as legitimate activity originating from the same country in which the victim is located.

The adversary has used RDP, web shells, and on rare occasions, malware such as _CloudedHope_ to move laterally within and establish persistence on compromised networks. Frequently, they have pivoted to cloud environments, likely to gain access to sensitive information stored in the cloud.

### Lateral Movement to Downstream Victims via Trusted-Relationship Compromises in the Cloud

MURKY PANDA is currently one of a few tracked adversaries that conduct trusted-relationship compromises in the cloud. Due to the activity’s rarity, this initial access vector to a victim's cloud environment remains relatively undermonitored compared to more prominent initial access vectors such as valid cloud accounts and exploiting public-facing applications. Leveraging this niche initial access vector, MURKY PANDA likely intends for their access to downstream victims to remain undetected, enabling prolonged access.

#### Lateral Movement to Downstream Victims via Compromising SaaS Providers

In at least two cases analyzed by CrowdStrike, MURKY PANDA exploited zero-day vulnerabilities to achieve initial access to software-as-a-service (SaaS) providers’ cloud environments. Following the compromise, MURKY PANDA determined the compromised SaaS cloud environments' logic, enabling them to leverage their access to that software to move laterally to downstream customers.

At least one SaaS provider victim was using Entra ID to manage its SaaS application’s access to its downstream customers’ data. In this intrusion, MURKY PANDA almost certainly obtained access to the SaaS provider’s application registration secret, which the adversary then leveraged to authenticate as the service principals of that application and log into downstream customers’ environments. Next, leveraging their control over those service principals, MURKY PANDA accessed emails at the downstream customers.

**Application Registration Compared to Service Principals**  
---  
In Entra ID, SaaS applications are defined by a type of template — referred to as an application registration — living in the Entra tenant of an application’s creator (e.g., a SaaS provider).  
When a SaaS application is used (e.g., by a customer), that application is represented via a service principal living in the Entra tenant of the application’s current user. [Service principals](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals) are entities with permissions that grant them access to specific data.  
To properly function, the application needs to access the user's data. To this end, the creator (i.e., the SaaS provider) can add secrets to the application registration. By leveraging the same secret, the creator can then authenticate as the service principals of that application registration in all downstream customers, and thus can access all downstream customers’ data.  
  
#### Lateral Movement to Downstream Customers by Compromising Cloud Solution Providers

In another intrusion, MURKY PANDA compromised a Microsoft cloud solution provider. A [cloud solution provider](https://learn.microsoft.com/en-us/partner-center/enroll/csp-overview) is a participant in Microsoft's partner program; as such, cloud solution providers must provide [support to their downstream customers](https://learn.microsoft.com/en-us/partner-center/customers/customer-support), requiring the former to have access to the latter's Entra tenant. To facilitate this cross-tenant access, cloud solution providers commonly use delegated administrative privileges ([DAP](https://learn.microsoft.com/en-us/partner-center/customers/customers-revoke-admin-privileges#delegated-admin-privileges-in-microsoft-entra-id)) or the newer granular delegated administrative privileges ([GDAP](https://learn.microsoft.com/en-us/partner-center/customers/gdap-introduction)).

In the analyzed MURKY PANDA exploitations, the compromised cloud solution provider had cross-tenant access to a downstream customer via DAP. DAP recognizes two special groups in the cloud solution provider's Entra tenant:

  * **Helpdesk Agent** : assigned `Helpdesk Administrator` privileges
  * **Admin Agent** : assigned `Global Administrator` privileges



Members of these groups obtain the respective privileges in all downstream customers’ Entra tenants.

MURKY PANDA had compromised a user in the Admin Agent group, and thus had `Global Administrator` privileges in all downstream customers' tenants. Leveraging that compromised user account, MURKY PANDA temporarily created a new user in a downstream victim's tenant and added this newly created backdoor user to several preexisting groups. One of those preexisting groups granted the backdoor user `Application Administrator` privileges, allowing MURKY PANDA to add secrets to preexisting service principals.

With control over those newly added secrets, MURKY PANDA successfully authenticated as those service principals, thereby escalating their privileges to those of the backdoored service principals. Backdoored service principals included those with privileges to read emails, likely supporting MURKY PANDA's intelligence-collection requirements, as well as those with privileges to add secrets to application registrations and service principals — thus establishing a second persistence point on the victim system.

## Recommendations

These recommendations can be implemented to help protect against the activity described in this blog.

### Service Principal Credential Management

  * Audit Entra ID service principals’ credentials, particularly newly added credentials (Entra ID audit log: `Add service principal credentials`)



### Service Principal Activity Monitoring

  * Enable [Microsoft Graph activity logs](https://learn.microsoft.com/en-us/graph/microsoft-graph-activity-logs-overview) to improve the visibility of the resources accessed via Microsoft Graph and which service principal accessed those resources. These logs can then be ingested, correlated, and hunted against in CrowdStrike Falcon® Next-Gen SIEM.
  * Hunt for service principal activities that deviate from expected actions (e.g., accessing unexpected resources, such as emails)
  * Hunt for Entra ID service principal sign-ins from unexpected networks (e.g., a service principal who typically signs in from a Microsoft-associated IP address suddenly originates from a different network)
  * Analyze sign-in patterns of the Entra ID tenant’s service principals. If service principals tend to log in on a regular schedule, treat deviations from that schedule as suspicious.
  * For successful [service principal sign-ins](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aadserviceprincipalsigninlogs), review the `sessionId` to understand the activity conducted by that service principal during this session and determine whether this activity is abnormal. For example, if a backup application that typically accesses numerous objects to create backups instead accesses only a few objects, that activity is suspicious.
  * CrowdStrike Falcon® Shield can detect service principal sign ins from abnormal networks, service principals signing in with suspicious (e.g. newly added) credentials, and the backdooring of service principals and app registrations via credentials.



### Microsoft Cloud Solution Provider Monitoring

  * Audit the addition of new users by cloud solution provider accounts (Entra ID Audit Logs: Add `user` with `callerIPAddress` containing at least one `X` character, which indicates that the given cloud solution provider accesses downstream customers via cross-tenant access)
  * Use Entra ID sign-in logs to verify whether cloud solution provider accounts use MFA (`CrossTenantAccessType: serviceProvider`); Microsoft is increasingly [mandating](https://learn.microsoft.com/en-us/partner-center/security/partner-security-requirements-mandating-mfa#partner-center) MFA for cloud solution providers



### General Recommendations

  * Regularly update software in the cloud environment to ensure vulnerabilities are patched in a timely manner, and regularly assess hosted applications for flaws in application design and implementation. Prioritize patching known remote code execution (RCE) and server-side request forgery (SSRF) vulnerabilities in public-facing applications running in the cloud.
  * Maintain all edge devices at a recent software level and follow vendor guidelines
  * Closely monitor devices prone to exploitation; investigate unusual login activity



## Outlook

MURKY PANDA is a sophisticated adversary that uses advanced tradecraft to target cloud environments and compromise high-profile targets. The adversary is knowledgeable of custom application logic as well as niche Entra ID concepts, and evades victim system defenses by targeting rarely monitored access vectors. MURKY PANDA’s OPSEC, which focuses on sanitizing logs on victim systems, further underscores their operations’ sophistication.

MURKY PANDA poses a significant threat to government, technology, legal, and professional services entities in North America and to their suppliers with access to sensitive information. 

Organizations that rely heavily on cloud environments are innately vulnerable to trusted-relationship compromises in the cloud. China-nexus adversaries such as MURKY PANDA continue to leverage sophisticated tradecraft to facilitate their espionage operations, targeting numerous sectors globally.

#### Additional Resources

  * _Learn how CrowdStrike’s[Threat Intelligence and Hunting](https://www.crowdstrike.com/en-us/platform/threat-intelligence/) solutions are transforming security operations to better protect your business._
  * _Tune into the[Adversary Universe Podcast](https://www.crowdstrike.com/en-us/resources/adversary-universe-podcast/), where CrowdStrike experts discuss today’s threat actors — who they are, what they’re after, and how you can defend against them._
  * _Download the[CrowdStrike 2025 Global Threat Report](https://www.crowdstrike.com/en-us/global-threat-report/) and [CrowdStrike 2025 Threat Hunting Report](https://www.crowdstrike.com/en-us/resources/reports/threat-hunting-report/) to learn more about the latest adversary trends and TTPs._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)