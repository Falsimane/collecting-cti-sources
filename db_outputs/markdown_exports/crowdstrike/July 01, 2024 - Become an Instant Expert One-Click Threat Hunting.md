# Become an Instant Expert: One-Click Threat Hunting

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/instant-expert-one-click-threat-hunting/
- **Date :** July 01, 2024

---

# CrowdStrike’s One-Click Hunting Simplifies Threat Hunting for Security Teams

## CrowdStrike’s one-click hunting empowers security teams to more easily identify new or evolving threats.

July 01, 2024

• [ Bart Lenaerts-Bergmans](/en-us/blog/author.bart-lenaerts-bergmans/ "Posts by Bart Lenaerts-Bergmans") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Adversaries are not breaking in; they are logging in. The [CrowdStrike 2024 Global Threat Report](https://www.crowdstrike.com/resources/reports/crowdstrike-2024-global-threat-report/) highlights an alarming trend: In 75% of cyberattacks detected in 2023, adversaries gained initial access through malware-free methods. This means they acquired valid credentials via techniques such as password spraying or phishing — or they simply purchased them off the dark web. The report also revealed a 60% year-over-year increase in hands-on “interactive intrusions,” where adversaries use legitimate tools and commands to accomplish their objectives.

This advancement in adversary tradecraft is particularly alarming, as it is designed to evade traditional software defenses. Unlike malware attacks that depend on the deployment of easily detected malicious tooling and scripts, interactive intrusions leverage the creativity and problem-solving of human adversaries. When adversaries blend in as legitimate users, it’s extremely difficult for automated solutions to differentiate between benign activity and a cyberattack.

To counteract these threats, security teams must assume the adversary is already in their environment and initiate a proactive threat hunting and detection engineering program. It takes intuition, expertise and lots of data to track adversaries — especially as they successfully hide and evolve their techniques. For most organizations, however, threat hunting and detection engineering can be difficult and expensive, as is the process of running a threat intelligence and research team.

CrowdStrike, an industry leader in threat intelligence, has a new capability to help. We recently released “one-click hunting” to eliminate the cost and complexity of tracking down adversaries.

## One-Click Hunting with CrowdStrike Threat Hunting Libraries

One-click hunting is now included in [CrowdStrike Falcon® Adversary Intelligence Premium](https://www.crowdstrike.com/products/threat-intelligence/adversary-premium/). As CrowdStrike’s elite threat researchers identify new or evolving threats, they publish prebuilt threat hunting queries that you can simply click to determine if the particular threat exists in your environment.

Intelligence-led one-click hunting enables security teams to perform turnkey threat hunts based on real-time data and conduct advanced searches within the AI-native CrowdStrike Falcon® platform to pinpoint potentially malicious activity in their environment. With single-click activation, the prebuilt hunting library streamlines the threat hunting process; reduces the need for upfront research, query creation and data visualization; and boosts the overall effectiveness of threat hunting exercises.

There are several benefits to security teams, including the following.

**Greater threat hunting effectiveness:** Threat hunting missions are often measured in weeks or months. CrowdStrike cuts this down to minutes by combining the required threat research and query creation into a single action. This enables security analysts to pivot from newly discovered attack techniques, as described in threat reports, to instantly detecting malicious activities in their environments. By enhancing the efficiency of these operations, CrowdStrike not only accelerates response time but significantly reduces the effort and cost associated with threat hunting.

**Streamlined hunting processes:** Advanced security teams have an average of nearly 50 security tools installed in their environment,1 making threat hunting costly and complex. CrowdStrike’s unified platform eliminates the need for additional tools, integrating threat hunting workflows, threat intelligence and critical data spanning endpoint, identity and cloud within the Falcon platform.

**Stronger security posture:** Running a threat hunting program often leads to finding improperly configured controls, inadequate in-house telemetry or gaps in security information and event management (SIEM) data collection. By increasing threat hunting frequency and proactively searching for the most sophisticated threats, organizations can strengthen their overall security posture and better prepare for the next wave of adversary techniques.

**Ability to operationalize proactive security:** Falcon Adversary Intelligence Premium, part of the Falcon AI-native platform, enables organizations to instantly operationalize industry-leading threat intelligence into an intel-led threat hunting program without the need to deploy, maintain or administer additional systems.

## Example: Hunting for Remote Monitoring and Management Tools

After gaining access to a victim’s network, adversaries can masquerade as legitimate users. In many cases, they attempt to exfiltrate data with standard file-sharing tools and install popular remote monitoring and management (RMM) tools. Use of these RMM tools increased 312% year-over-year, the [CrowdStrike 2023 Threat Hunting Report](https://www.crowdstrike.com/resources/reports/threat-hunting-report/) found.

Identifying systems compromised via RMM communications can be challenging because they look identical to legitimate RMM use. Separating the signals from the noise requires up-to-date information on the latest adversary techniques. It requires research to create a hypothesis and then skill to craft the appropriate hunting queries to prove or disprove your theory. In many cases, you may not find the threat immediately, but the results will provide insight to inform other queries. Each iteration may take hours or days, repeated often to detect rapidly evolving threats.

To streamline the hunting process, Falcon Adversary Intelligence Premium’s one-click hunting provides prebuilt queries based on CrowdStrike adversary research. Using the CrowdStrike Query Language (CQL), with a one-click action, threat hunters can run a search against data within the Falcon platform.

In the example below, the one-click hunting query immediately detects potentially malicious RMM communication within Microsoft Visual Studio (VS) Code Server. This example illustrates how the one-click hunting process eliminates the need for upfront research as well as the creation and testing of hunting queries.

### Step 1: Identify a threat hypothesis

Every year, CrowdStrike publishes thousands of finished intelligence reports, including daily threat alerts, in-depth technical analysis and strategic reports.

In a recent threat alert (CSA-240541), CrowdStrike identified how malicious insiders evade detection by using trusted developer utilities like Visual Studio Code to set up rogue remote tunnels and gain full remote control. Threat alerts like this offer a great opportunity for hunters to form a hypothesis.

[![Figure 1. The summary section of a CrowdStrike threat alert written to describe the malicious usage of Visual Studio Code](https://www.crowdstrike.com/wp-content/uploads/2024/07/Figure1.png)](https://www.crowdstrike.com/wp-content/uploads/2024/07/Figure1.png)

Figure 1. The summary section of a CrowdStrike threat alert written to describe the malicious usage of Visual Studio Code

### Step 2: Select prebuilt hunting queries and start the hunt

Using Falcon Adversary Intelligence Premium’s new hunting library, users can quickly locate predefined hunting queries related to the recently identified malicious usage of Visual Studio Code remote development extensions. These queries are formatted in CQL.

[![](https://www.crowdstrike.com/wp-content/uploads/2024/07/Figure2.png)](https://www.crowdstrike.com/wp-content/uploads/2024/07/Figure2.png)

Figure 2. “One-click” hunting queries related to the CrowdStrike alert

### Step 3: Review results

After the query executes, the results are displayed for further examination. In the example shown in Figure 3, we see an endpoint that has been identified as running the Visual Studio Code remote development extensions. The blue bars represent activity spikes over the specified time interval, and the search results table provides the exact moment when Visual Studio Code remote development extensions were active, along with each command executed over the remote connection.

As indicated in the threat alert (Step 1), commands executed through remote development extensions via Visual Studio Code Server pose a high risk, as they may go undetected when used by adversaries.

[![](https://www.crowdstrike.com/wp-content/uploads/2024/07/Figure3.png)](https://www.crowdstrike.com/wp-content/uploads/2024/07/Figure3.png)

Figure 3. Hunting query, time interval and search results

### Step 4: Mitigate risk

Using the evidence from the threat hunt, the security analyst can now dive deeper into potential adversary activity by analyzing the suspicious commands for the presence of intrusion activity, such as creating new users, moving laterally within the environment or installing additional code. The identified computer name in the threat hunt results allows responders to contact the IT asset owner and request the disabling of the Visual Studio Code Remote Tunnel extension, thereby eliminating the risk of abuse by adversaries.

## Summary

Adversaries evolve their tactics rapidly to evade detection, and continuous threat hunting with up-to-date queries is critical to stopping breaches.

CrowdStrike’s one-click hunting eliminates barriers to threat hunting, such as lack of threat expertise, tool sprawl and time-consuming creation of hunting queries. Prepopulated hunting libraries are available to all customers of [Falcon Adversary Intelligence Premium](https://www.crowdstrike.com/products/threat-intelligence/adversary-premium/). This approach both reduces the complexity and costs associated with threat hunting and strengthens organizational security posture against sophisticated threats.

#### Additional Resources

  * _To find out more about how to incorporate threat intelligence into your security strategy, visit the[CrowdStrike Falcon Adversary Intelligence page](https://www.crowdstrike.com/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Read about the cybercriminals tracked by CrowdStrike Counter Adversary Operations in the[CrowdStrike 2024 Global Threat Report](https://www.crowdstrike.com/resources/reports/global-threat-report/)._
  * _[Request a free trial](https://www.crowdstrike.com/free-trial-guide/) of the industry-leading Falcon platform._



1 [IDC, “How Many Security Tools Do Organizations Have, and What Are Their Consolidation Plans?” Document number #US51973524, Mar 2024](https://www.idc.com/getdoc.jsp?containerId=US51973524)

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)