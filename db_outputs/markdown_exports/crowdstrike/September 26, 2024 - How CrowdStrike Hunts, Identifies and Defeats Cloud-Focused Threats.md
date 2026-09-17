# How CrowdStrike Hunts, Identifies and Defeats Cloud-Focused Threats

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-crowdstrike-hunts-identifies-and-defeats-cloud-threats/
- **Date :** September 26, 2024

---

# How CrowdStrike Hunts, Identifies and Defeats Cloud-Focused Threats

## To discover and mitigate attack activity, organizations must understand how adversaries are adopting cross-domain tactics, infiltrating cloud environments and conducting attacks.

September 26, 2024

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Adversaries’ persistent efforts to evade advancements in threat awareness and defense have shaped a cyber threat landscape dominated by their stealthy, fast-moving tactics. As they expand into the cloud environments where most organizations now operate, the need to hunt and remediate threats has become crucial. 

The [CrowdStrike 2024 Threat Hunting Report](https://www.crowdstrike.com/resources/reports/threat-hunting-report/) examines how adversaries are increasingly targeting cloud environments as they adopt cross-domain techniques, which span several domains across an organization’s infrastructure. The report can help organizations learn how to strengthen their defenses through the use of cloud threat hunting and greater visibility into the runtime environments of critical cloud infrastructures and cloud control planes.

The cloud control plane is the backbone of cloud operations. It serves as a command center to manage and secure cloud environments by allowing users to interact with the cloud and the resources in it. Over the past 12 months, the cloud control plane has become a key target for adversaries seeking full access to an organization’s cloud infrastructure — and the broader enterprise. From there, they can run commands to deploy backdoors or establish persistence by creating additional accounts. Security teams must understand the value of the cloud control plane to modern adversaries.

Cloud-focused threats are accelerating: Cloud intrusions increased by 75% and cloud-conscious cases increased by 110% from 2022 to 2023, according to the [CrowdStrike 2024 Global Threat Report](https://www.crowdstrike.com/global-threat-report/). By understanding these threats and the adversaries behind them, organizations can better detect, identify and remediate attacks in the cloud. 

## Prolific Adversaries Operate in Cloud Environments

[CrowdStrike Falcon® Adversary OverWatch](https://www.crowdstrike.com/platform/threat-intelligence/adversary-overwatch/) threat hunters have identified two adversaries that move across domains and primarily target cloud infrastructure. [SCATTERED SPIDER](https://www.crowdstrike.com/adversaries/scattered-spider/) is a financially motivated threat actor capable of infiltrating all major cloud service providers; [COZY BEAR](https://www.crowdstrike.com/adversaries/cozy-bear/) is a Russia state-nexus adversary that often targets Azure services for data theft.

Both adversaries aim to find or steal credentials to directly access poorly configured cloud environments while bypassing the need to compromise heavily defended endpoints. From there, they can find over-privileged users to further exploit cloud environments or use their access to descend into endpoint environments. They can then deploy remote management tools, an increasingly common method for maintaining persistence while evading detection. 

SCATTERED SPIDER and COZY BEAR are noteworthy because they have honed their cross-domain proficiency, which allows them to quickly and confidently navigate multiple operating systems and security platforms.

The CrowdStrike 2024 Threat Hunting Report examines the specific cloud-focused tactics of each group, and their behavioral differences, in greater detail.

## Case Study: SCATTERED SPIDER’s Cross-Domain Attack

Falcon Adversary OverWatch observed an incident involving SCATTERED SPIDER that exemplifies how cross-domain attacks are a threat to cloud environments. This adversary is the most prominent in cloud-based intrusions, conducting 29% of all associated activity in 2023. 

In May 2024, SCATTERED SPIDER was observed establishing a foothold on a cloud-hosted virtual machine (VM) instance via a cloud service VM management agent. To launch this attack, they compromised existing credentials to authenticate to the cloud control plane via an identified phishing campaign. After authenticating to the cloud console, the adversary established persistence by executing commands on the cloud-hosted VM via the management agent. 

After establishing an initial connection, the ping command was executed against several domains within and outside of the target organization to identify their level of access and visibility. The adversary ran several tests to identify domain controllers of interest and the programs currently installed on the host. Finally, persistence was established by creating a new user on the host and attempting to download FleetDeck remote access software.

What makes this attack noteworthy is it took place across three domains: email, then cloud management, then within a VM. By using this approach, the detectable footprint of this activity in any single detection domain was very low and difficult to conclusively identify. Fortunately, this attack was quickly detected by using knowledge about SCATTERED SPIDER from CrowdStrike’s extensive threat intelligence and prior experience with this adversary. Combining this information with telemetry from the control plane, and correlating it against detections from within the VM, made it possible to quickly recognize an intrusion was underway. 

## The Value of Cloud-Based Threat Hunting

Cloud threat hunting is an important weapon in a security team’s arsenal. It adds human investigation to search for anomalous and new attacker activity, which is often necessary to identify cutting-edge cloud attack techniques. Adding full insight into telemetry that spans endpoint, identity and cloud environments is a force multiplier for threat hunting.

Falcon Adversary OverWatch's cloud-based threat hunting offers expanded visibility into the runtime environments of critical cloud infrastructures and cloud control planes. It can identify impacted hosts, identities and workloads at the earliest opportunity, whether the threat originates in the cloud or the adversary attempts to move into a cloud environment. The team tirelessly hunts for post-exploitation behaviors, and adversaries are detected very quickly regardless of the initial access vector. As a result, the team most often observes techniques in the discovery phase, when adversaries are still orienting themselves in a network.

## Guarding Against Threats to Cloud Environments

To mitigate intrusion techniques similar to those demonstrated by SCATTERED SPIDER and other cloud-focused adversaries, CrowdStrike recommends the following measures: 

  * Gain a comprehensive understanding of any cloud platform running on a network. Many organizations only understand pieces of their cloud environment — not the entire setup.
  * Standardize and validate cloud resource configurations before deployment and regularly monitor for deviations from approved standards. This involves posture management and ensuring you can set standards and monitor for deviations, which are the anomalies that could indicate an attack.
  * Apply the same security policies to cloud workload servers as any other server, and deny outbound connections initiated from any server that does not link to allowlisted endpoints. These policies should be applied across the board by implementing ingress and egress filtering and monitoring your cloud assets.
  * Monitor cloud assets and vulnerability implementation, and mitigate risks in a timely manner. Keep an eye on any new vulnerabilities or configuration changes.
  * Apply the principle of least privilege to cloud infrastructure by evaluating credentials and configurations to ensure access is provided only to necessary resources.



#### Additional Resources

  * _Get a free[Cloud Security Health Check](https://go.crowdstrike.com/google-cloud-security-health-check.html) with Google Cloud and get a one-on-one review with a cloud security expert._
  * _[Stop breaches from code to cloud](https://www.crowdstrike.com/platform/cloud-security/) — see and secure everything across your clouds, your applications and your data._
  * _Learn more about CrowdStrike Falcon Cloud Security —[the only CNAPP to stop breaches](https://www.crowdstrike.com/platform/cloud-security/cnapp/) with definitive protection for everything you build and run in the cloud._
  * _Learn how CrowdStrike's[threat intelligence and threat hunting solutions](https://www.crowdstrike.com/platform/threat-intelligence/) are transforming security operations to better protect your business. _



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)