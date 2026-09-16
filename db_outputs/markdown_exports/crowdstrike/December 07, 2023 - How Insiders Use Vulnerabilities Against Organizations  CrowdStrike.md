# How Insiders Use Vulnerabilities Against Organizations | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-malicious-insiders-use-known-vulnerabilities-against-organizations/
- **Date :** December 07, 2023

---

# How Malicious Insiders Use Known Vulnerabilities Against Their Organizations

December 07, 2023

• [ Jaime Duque - Bobby Dean - Alex Merriam - Damon Duncan - Nicolas Zilio](/en-us/blog/author.jaime-duque---bobby-dean---alex-merriam---damon-duncan---nicolas-zilio/ "Posts by Jaime Duque - Bobby Dean - Alex Merriam - Damon Duncan - Nicolas Zilio") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


  * Between January 2021 and April 2023, CrowdStrike Counter Adversary Operations and the CrowdStrike Falcon® Complete managed detection and response (MDR) team identified multiple incidents in which an internal user either exploited or sought to exploit a known vulnerability, or deploy offensive security tooling against their enterprise environment.
  * Approximately 55% of the identified insider threat incidents involved unauthorized use or attempted use of privilege escalation exploits.
  * Approximately 45% of insider threat incidents involved insiders who unwittingly introduced risk to their environment through the unauthorized download of exploits or by downloading other offensive security tools for testing or training purposes.
  * Given overlaps in vulnerability use and typical actions on objectives, many methods that detect and mitigate targeted intrusion and eCrime activity are also applicable to insider threat activity.



We are well aware of the devastating effect insiders can have when using their legitimate access and knowledge to target their own organization. These incidents can result in significant monetary and reputational damages. Entities small and large, across all sectors, can fall victim to [insider threats](/en-us/cybersecurity-101/identity-protection/insider-threat/). Insider-led cybersecurity incidents are growing more frequent — and more expensive: Reports report from the Ponemon Institute state the number of insider threat events increased by 44% from 2020 to 2022. The average cost per malicious and non-malicious incident climbed to $648,000 USD and $485,000 USD, respectively.1 These incidents can also result in brand and reputational damages that, while hard to quantify, have a significant impact.

> **What Is an Insider Threat?**

> For the purposes of this article, an insider threat is defined as an individual with the potential to wittingly or unwittingly use their access to negatively affect the confidentiality, integrity or availability of their organization's information or information technology (IT) systems. Within this context, an unauthorized user leveraging a privilege escalation exploit — to gain the permissions necessary to delete network logs or conceal their hands-on-keyboard activity — represents an example of a willing insider threat. Meanwhile, an individual who has permission to use exploits as part of their duties but inadvertently uses the wrong computer/system, or fails to follow the proper safe-handling standard operating procedures, represents an example of an unwitting insider threat. _Source: https://insights.sei.cmu.edu/blog/cert-definition-of-insider-threat-updated/_

Since 2021, CrowdStrike Intelligence has observed insider threats achieve their goals through the exploitation of known vulnerabilities. While these activities are hard to detect, not all is doom and gloom. An intelligence-driven review of known cases shows that many defensive actions used to detect and mitigate targeted intrusion and eCrime adversaries are also effective at stopping insider threat activity, given overlaps in vulnerability usage and post-exploitation activity. Falcon Complete can help detect and contain these threats, protecting customers from both insider threats and external adversaries.

## Insiders’ Commonly Exploited Vulnerabilities

CrowdStrike Counter Adversary Operations and CrowdStrike Falcon Complete analyzed incidents from January 2021 to April 2023 to deduce the most prevalent vulnerabilities leveraged without authorization by internal users in their enterprise environment. This is a high-confidence qualitative assessment based on observed behaviors consistent with attempted or successful exploitation based on Falcon Complete incident data. These incidents fall into two broad categories:

  * Unauthorized exploitation to escalate privileges and support follow-on objectives
  * Unauthorized testing of exploits or downloading of offensive tools for defensive or training purposes



While this article covers specific vulnerabilities, it is not intended to conclusively identify all vulnerabilities potentially related to insider threat activities. Depending on the intended target and objectives, numerous other vulnerabilities with existing public proof-of-concept exploits could accomplish similar objectives.

### Unauthorized Exploitation to Escalate Privileges and Support Follow-on Objectives

Privilege escalation is typically the intermediate step between initial access and reaching the actual objective in a cyber intrusion. It is considered a critical stage in the attack chain, since many of the subsequent steps — such as defense evasion and manipulating sensitive programs/systems — require an elevated privilege level. This is especially relevant to insiders who usually possess low-level access to the target environment as part of their duties.

An insider user that escalates privileges without authorization is abusing their access and, at a minimum, attempting to bypass the [principle of least privilege (POLP)](/en-us/cybersecurity-101/identity-protection/principle-of-least-privilege-polp/). According to this principle, users and processes are only granted the minimum permissions required to perform their assigned tasks. POLP is widely considered to be one of the most effective practices for strengthening an organization’s cybersecurity posture, and it allows organizations to control and monitor network and data access.2

Fifty-five percent of the insider threat incidents identified by CrowdStrike Counter Adversary Operations involved attempted local privilege escalation (LPE) to support follow-on actions. For example, insiders sought higher privileges to download unauthorized software, remove forensic evidence or troubleshoot IT systems. By attempting to escalate privileges, these internal users wittingly or unwittingly introduced risk to their network, and as a result, these incidents fall under the insider threat umbrella regardless of malicious intent (see Figure 1).

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/12/Figure1.png)](/content/dam/crowdstrike/www/en-us/wp/2023/12/Figure1.png)Figure 1. Hypothetical example of an insider threat leveraging a local privilege escalation (LPE)

These incidents leveraged six well-known vulnerabilities that have publicly available exploit proof-of-concept (POC) code on GitHub and are included in the United States Cybersecurity and Infrastructure Security Agency (CISA) catalog of [known exploited vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). The broad range of vulnerabilities used highlights the large number of potential attack vectors and the breadth of the attack surface.

**CVE Number**| **CVE Name**| **Targeted OS**| **In CISA KEV**  
---|---|---|---  
CVE-2017-0213| Windows Component Object Model (COM) Elevation of Privilege Vulnerability| Windows| Yes  
CVE-2022-0847| Linux Kernel Privilege Escalation Vulnerability (aka DirtyPipe)| Linux| Yes  
CVE-2021-4034| Polkit Out-of-Bounds Read and Write Vulnerability (aka PwnKit)| Linux| Yes  
CVE-2019-13272| Linux Kernel Improper Privilege Management Vulnerability| Linux| Yes  
CVE-2015-1701| Microsoft Win32k Privilege Escalation Vulnerability| Windows| Yes  
CVE-2014-4113| Microsoft Win32k Privilege Escalation Vulnerability| Windows| Yes  
  
_Table 1. Vulnerabilities observed being leveraged by insiders to escalate privileges_

#### CVE-2017-0213 Incidents

In early April 2023, CrowdStrike Falcon Complete detected and blocked an internal user’s attempt to exploit a Windows Component Object Model (COM) privilege escalation vulnerability (CVE-2017-0213) at a Western Europe-based retail entity. Specifically, the internal user leveraged the WhatsApp messenger application to download an exploit targeting CVE-2017-0213 in an attempt to escalate privileges and install the uTorrent file-sharing application as well as unauthorized games.

Successful exploitation of CVE-2017-0213 allows an authenticated attacker to run arbitrary code with elevated privileges. Since April 2022, CrowdStrike Falcon Complete has detected six other incidents involving internal users attempting to leverage CVE-2017-0213 to conduct unauthorized follow-on activities. Notably, in late July 2022, a terminated employee at a U.S.-based media entity unsuccessfully attempted to leverage this vulnerability to conduct unauthorized activities.

#### Other Incidents

The remaining incidents involved internal users leveraging five privilege escalation vulnerabilities to gain elevated privileges in order to conduct unauthorized follow-on operations. Notably, in mid-July 2022, an internal user at an Australia-based technology entity attempted to execute an exploit for CVE-2021-4034 (PwnKit) to gain administrative rights and troubleshoot their host machine. Also, in mid-October 2022, an internal user at a U.S.-based technology entity leveraged CVE-2015-1701, a Microsoft Win32k privilege escalation vulnerability, to gain the necessary permissions to bypass internal controls and allow for the unauthorized installation of a Java virtual machine.

### How Insider Threats Unintentionally Put Organizations At Risk

Forty-five percent of the insider threat incidents identified by CrowdStrike Counter Adversary Operations involved insiders who unwittingly introduced risk to their environment via the unauthorized download of exploits or by downloading other offensive security tools for testing or training purposes. In these incidents, the insiders, who may be responsible for using exploits and offensive tools as part of their regular duties, unwittingly introduced risk to their environment by not following safe-handling procedures (see Table 2). For example, in some of the incidents, the insider users should have downloaded the exploits in virtual machines or other specific hosts to provide better network segmentation between testing and production environments.

There are several ways this could cause damage. Testing exploits on unauthorized systems could disrupt operations, as some exploits could cause system crashes or other unintended negative actions. Additionally, an adversary with a foothold on the insider threats’ network could leverage these exploits or tools to support their own malicious activity. Finally, downloading unvetted code can introduce backdoors or other malicious artifacts into the internal user’s network. Below are some of the vulnerabilities involved in cases of insider threats unintentionally putting their organization at risk.

**CVE Number**| **CVE Name**| **Targeted OS**| **In CISA KEV**  
---|---|---|---  
CVE-2021-42013| Apache HTTP Server 2.4.49 and 2.4.50 Path Traversal| Mac| Yes  
CVE-2021-4034| Polkit Out-of-Bounds Read and Write Vulnerability (aka PwnKit)| Linux| Yes  
CVE-2020-0601| Windows CryptoAPI Spoofing Vulnerability| Windows| Yes  
CVE-2016-3309| Windows Kernel Privilege Escalation Vulnerability| Windows| Yes  
CVE-2022-21999| Windows Print Spooler Elevation of Privilege Vulnerability| Windows| Yes  
N/A| Metasploit Framework| N/A| N/A  
N/A| ElevateKit| N/A| N/A  
  
_Table 2. Vulnerabilities observed being leveraged by insiders for testing/defensive purposes_

#### CVE-2021-42013 Incident

In October 2022, CrowdStrike Falcon Complete detected and contained a script leveraging CVE-2021-42013 to launch an Apache reverse shell at a U.S.-based technology entity. Successful exploitation of CVE-2021-42013 allows an unauthenticated attacker to execute code remotely. In this incident, the internal user leveraged this vulnerability without permission to exploit a server as part of a Capture-the-Flag (CTF) competition. This incident highlights the importance of properly scoping and communicating any restrictions regarding CTF and similar exercises in corporate networks.

#### Other Vulnerability Incidents

Other incidents involved internal users exploiting individual vulnerabilities for testing and/or training purposes. While these users — often in security roles — are permitted to test exploits as part of their job duties, they were not authorized to conduct that activity in the specific hosts that triggered the CrowdStrike Falcon® sensor. For example, in February 2023, an internal user at a United States-based technology entity attempted to download an exploit for CVE-2016-3309, a Windows kernel privilege escalation vulnerability, on their corporate computer instead of on the approved system for these types of activities (a separate virtual machine). The Falcon Complete team was able to quickly triage event logs recorded using Falcon's Endpoint Activity Monitoring (EAM) application to provide additional context surrounding the initial download of the CVE-2016-3309 exploit.

#### Metasploit Framework

From May 2022 to February 2023, Falcon Complete observed multiple incidents involving the unauthorized deployment of the Metasploit Framework on Windows and Linux hosts by insider users. The Metasploit Framework is a well-known penetration testing framework that can be used for exploitation, enumeration, post-exploitation and other offensive activities. This tool is commonly used by security teams for testing and executing exploits — however, it can also provide insiders a readily available mechanism for conducting pre- and post-exploitation activities. While each incident was assessed to be related to defense-focused testing activity, the unauthorized deployment of the Metasploit Framework by an internal user introduces risks to the enterprise network.

#### ElevateKit

In December 2022, Falcon Complete observed an incident involving an internal user downloading and staging _ElevateKit_ , a privilege escalation framework commonly leveraged alongside _Cobalt Strike. ElevateKit_ registers modules with the _Cobalt Strike_ Beacon payload to allow for privilege escalation using publicly available exploits.3 In addition to _ElevateKit_ , the user also staged _Mimikatz_ and _PowerLurk_ , two tools also commonly used in penetration testing engagements for credential dumping and establishing persistence via Windows Management Instrumentation (WMI). While this incident was later determined to be related to unauthorized security testing preparation, a threat actor could potentially abuse these previously deployed tools to escalate privileges, move laterally or establish persistence.

## Non-Exploit Based Insider Threat Activity

Internal users are not limited to exploiting vulnerabilities to achieve their results. In addition to using their own credentials, insider threats could leverage various other methods to escalate privileges, evade defenses and/or execute arbitrary code. The following is a non-exhaustive list of other potential approaches and methods:

  * [DLL hijacking](/en-us/blog/4-ways-adversaries-hijack-dlls/)
  * Insecure file system permissions
  * Insecure service configurations
  * Exploitation through removable media
  * Windows accessibility features bypass 
  * Image file execution options injection



## Recommendations

The inherent difficulty in identifying insider threat activity, and the limited sample size, preclude definitive and granular observations. However, a review of the incidents and vulnerabilities associated with insider threats from January 2021 to April 2023 highlights several factors that may aid in preventing and detecting future insider threat activity.

Many of the vulnerabilities described in this article have also been exploited by targeted intrusion and eCrime adversaries. Thus, many of the popular [defense-in-depth](/en-us/cybersecurity-101/exposure-management/defense-in-depth/) measures applied by network defenders to detect and mitigate targeted intrusion or eCrime activity will help identify and neutralize insider threats, given similar overlaps in observed tactics, techniques and procedures and desired actions on objective (e.g., data exfiltration, data destruction, etc.).

CrowdStrike Counter Adversary Operations assesses that more than half of the identified insider threat incidents involved internal users unauthorized use or attempted use of privilege escalation exploits to support follow-on objectives. This assessment is made with high confidence based on available forensic data and observed hands-on-keyboard activity. While each user’s individual calculus for selecting specific vulnerabilities to leverage remains unknown, the chosen vulnerabilities have publicly available exploits on GitHub and have been exploited in the wild. As such, restricting or monitoring the download of exploits from GitHub and other online code repositories from personnel who do not require that access as part of their regular duties could mitigate this threat — limiting access to ready-to-use exploits can hinder insider threats from conducting malicious activity.

The use of older vulnerabilities, some disclosed as early as 2015, underscores that vulnerabilities can remain useful to all attackers (internal or external) until patched or mitigated. This is particularly relevant to internal systems that may be under a slower patching cycle than that of internet-exposed systems. Internal users are particularly well positioned to leverage older local privilege escalation vulnerabilities, as they often already possess the low-level privileges and/or credentials needed to successfully run these exploits, have a better understanding of the host environment and can conduct basic reconnaissance commands with lesser risk of discovery than a remote attacker.

Approximately 45% of the insider threat incidents involved insiders ostensibly expected to leverage exploits and offensive tools as part of their regular duties who unwittingly introduced risk to their environment by the unauthorized download of exploits or other offensive security tools. Not following proper procedures related to the handling of exploits and other offensive tooling can cause system crashes or other negative effects to the host environment. Although CrowdStrike Counter Adversary Operations has not observed this so far, a resourceful adversary with a foothold in the internal user’s network could also leverage these offensive tools or exploits for their own operations.

## Mitigation Options

### Vulnerability Management

It is critical to ensure timely vulnerability patching in order to protect enterprise devices. [CrowdStrike Falcon Exposure Management](/en-us/products/exposure-management/falcon-exposure-management/) provides real-time, instant visibility into new and emerging vulnerabilities by using scanless vulnerability assessment technology integrated with the CrowdStrike Falcon® sensor. This prioritizes risks based on an advanced AI model and integrates threat intelligence provided by the CrowdStrike Intelligence team to provide insight into trending threats.

Insider threats can also leverage non-exploit based attack vectors, suggesting timely patching is alone insufficient to address the potential threats. This is why it’s essential for organizations to implement multiple layers of defense such as [Falcon Complete](/en-us/services/managed-services/falcon-complete/) MDR and [CrowdStrike® Falcon OverWatch™](/en-us/services/managed-services/falcon-overwatch-threat-hunting/) managed threat hunting.

The Falcon Complete team actively monitors for and remediates exploitation and post-exploitation behaviors by analyzing suspicious process characteristics and behaviors, utilizing machine learning to detect malicious payloads, monitoring script execution and more. In addition, the Falcon OverWatch 24/7 threat hunting service provides early [indicators of threat actor activity](/en-us/cybersecurity-101/identity-protection/insider-threat-indicators/) and exploitation attempts. Falcon Overwatch integrates [indicators of compromise (IOCs)](/en-us/cybersecurity-101/threat-intelligence/indicators-of-compromise-ioc/) and threat intelligence provided by CrowdStrike Intelligence to identify, prevent and provide attribution for emerging threats.

### User Behavior Analysis to Detect Insider Threat Activity

User behavior analysis is also a key technique that [CrowdStrike Falcon® Complete Identity Threat Protection](/en-us/resources/data-sheets/falcon-complete-identity-threat-protection/) leverages to detect an adversary that may be using stolen credentials of a legitimate user or identify suspicious activity from an insider. By baselining normal behavior for every user based on authentication/historical data (which machines the user typically accesses, for example), utilizing advanced algorithms and machine learning technologies to auto-classify accounts (users and servers) — such as privileged, stealthy, service accounts, server types like VDI, etc. — and correlating with possible AD attack paths and escalation of privileges, we build detailed behavioral profiles for every entity, ultimately helping the analyst (and the detection engine) understand what is considered normal behavior and what is not. Any deviation from this baseline user behavior would set off a detection of an adversary in the environment or an insider with malicious intent, which can trigger automated responses (alert, multifactor authentication or block) based on pre-created policies.

### Tailored User Training

Given the unwitting nature of many of the incidents discussed in this article, tailored training — for both new and existing employees) on how to properly download, store and execute exploits and offensive tooling for testing and training purposes could almost certainly reduce these occurrences in the future. Multiple incidents involved new employees that were not well-versed on specific company policies related to exploit handling and use of external/virtual machines for testing purposes, suggesting that it is paramount to ensure new employees — particularly those in cybersecurity roles — receive the necessary training during their onboarding process.

Additionally, many of these incidents occurred at organizations in the technology sector, suggesting more tailored training for tech-savvy employees can also help mitigate future occurrences of these types of incidents. Nonetheless, organizations should ensure new and existing security procedures to prevent these types of incidents are not overly restrictive and cumbersome as to drive internal users to find ways to bypass them.

#### Additional Resources

  * _[Watch this demo to see CrowdStrike Falcon® Intelligence in action](/en-us/products/threat-intelligence/falcon-intelligence-automated-intelligence/)._
  * _Learn about our[ threat intelligence and hunting subscriptions](/en-us/products/threat-intelligence/)._
  * _Learn more about adversary tactics, techniques and procedures in the[ CrowdStrike 2023 Global Threat Report](/en-us/global-threat-report/) and in the [CrowdStrike 2023 Threat Hunting Report](/en-us/resources/reports/threat-hunting-report/)._
  * _Experience how the industry-leading CrowdStrike Falcon® platform protects against modern threats.[ Start your 15-day free trial today](https://go.crowdstrike.com/try-falcon-prevent.html)._



#### Sources

  1. https://www.proofpoint.com/us/resources/threat-reports/cost-of-insider-threats |   
https://www.thesasig.com/resources/2020-cost-of-insider-threats-global-report/
  2. https://www.crowdstrike.com/cybersecurity-101/principle-of-least-privilege-polp/
  3. https://github.com/rsmudge/ElevateKit



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)