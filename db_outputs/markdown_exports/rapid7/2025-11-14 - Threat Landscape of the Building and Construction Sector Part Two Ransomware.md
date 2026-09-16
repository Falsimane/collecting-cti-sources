# Threat Landscape of the Building and Construction Sector Part Two: Ransomware

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-building-construction-sector-threat-landscape-ransomware/
- **Date :** 2025-11-14

---

In this second installment of our two-part series on the construction industry, Rapid7 is looking at the specific threat ransomware poses, why the industry is particularly vulnerable, and ways in which threat actors exploit its weaknesses to great effect. You can catch up on the first part here: [_Initial Access, Supply Chain, and the Internet of Things._](https://www.rapid7.com/blog/post/tr-building-construction-sector-threat-landscape-initial-access-supply-chain-iot/)

## Ransomware and the construction industry 

The construction sector is increasingly vulnerable to ransomware attacks in 2025 due to its complex ecosystem and distinctive operational challenges. Construction projects typically involve a web of contractors, subcontractors, suppliers, and consultants, collaborating through shared digital platforms and exchanging sensitive documents such as blueprints, contracts, and timelines. 

While essential for project delivery, this interconnectedness creates numerous digital entry points that attackers can exploit, mainly as many firms rely on outdated software and insufficient cybersecurity protocols. Adding to the challenge, construction companies often operate under tight deadlines and financial constraints, leaving little room for prolonged IT outages or data recovery efforts. 

Ransomware attackers take advantage of this urgency, knowing that even short disruptions can halt entire job sites, delay multimillion-dollar projects, and damage reputations, making companies more likely to pay ransoms quickly.

Compounding the problem, many construction organizations lack dedicated cybersecurity staff and robust employee training, making them susceptible to phishing, weak passwords, and other basic attack vectors, as we talked about in part one of this series. The sector’s dependency on third-party vendors, who may have weaker security, amplifies the risk by widening the potential attack surface. 

Together, these factors make it difficult for construction firms to detect, prevent, and recover from[ ransomware](/fundamentals/what-is-ransomware/) incidents, leaving the industry facing financial losses, operational chaos, legal consequences, and growing pressure to modernize its approach to digital security.

⠀

![TL1.png](https://www.rapid7.com/cdn/images/blt247c826670ca3925/69173e26accf611f1cf6e5ed/TL1.png)

_Monthly comparison of ransomware attacks against the construction industry 2024 vs. 2025_

⠀

The construction industry is ranked among the top 3 most attacked sectors in 2025.

⠀

![TL2.png](https://www.rapid7.com/cdn/images/bltec441c669b1dd553/69173e25accf6111fcf6e5e9/TL2.png)

_Top 10 targeted sectors in 2025_

⠀

The majority of attacks are against companies in the United States, followed by Canada, the United Kingdom, and Germany. 

⠀

![TL3.png](https://www.rapid7.com/cdn/images/bltb5c1b2b700b12b4f/69173e258cc78643496b068c/TL3.png)

_Top 10 targeted countries in the construction industry in 2025_

⠀

In 2025, the ransomware groups that targeted construction companies most frequently were Play, Akira, Qilin (AKA Agenda), SafePay, RansomHub, Lynx, DragonForce, Medusa, WorldLeaks, and INC Ransom. Notably, RansomHub is [no longer active](https://www.rapid7.com/blog/post/q2-2025-ransomware-trends-analysis-boom-and-bust/) in its original form. 

⠀

![TL4.png](https://www.rapid7.com/cdn/images/blt00b6f39551994ac4/69173e254bc8f686f7d32b33/TL4.png)

_Top ransomware groups targeting the construction industry in 2025_

⠀

## Why the construction sector is attractive to ransomware groups 

The reasons why ransomware groups have zeroed in on this sector are diverse and include the following:

### High-value, time-sensitive projects

Construction projects are high-stakes endeavors, often involving multi-million (or even billion) dollar budgets and strict delivery deadlines. Even a brief disruption, whether caused by ransomware, data breaches, or system outages, can lead to costly project delays and penalties. Attackers know this, and they exploit the sector’s reliance on tight timelines to extort higher ransoms, banking on the urgency to restore operations.

### Complex, interconnected supply chains

Few industries are as dependent on an intricate web of subcontractors, vendors, and service providers. Each connection in this sprawling supply chain presents a potential vulnerability. A compromised partner can serve as a gateway for attackers, enabling threats like supply chain attacks and lateral movement across multiple organizations. Securing every link is a significant challenge, especially when third-party cybersecurity practices vary widely.

### Low cybersecurity maturity

While sectors like finance and healthcare have long invested in cybersecurity, many construction firms are only beginning their journey. Legacy systems, limited IT budgets, and a traditional focus on physical rather than digital risks have left gaps in defenses. As a result, attackers often find weaker security controls, outdated software, and unpatched systems, making this sector a prime target.

### Accelerated digitalization and IoT adoption

Adopting cloud platforms, Building Information Modeling (BIM), IoT sensors, and smart machinery is revolutionizing project management and delivery. However, each new digital innovation adds to the attack surface. IoT devices, in particular, often lack robust security controls, providing attackers with novel entry points that are difficult to monitor and defend.

### Exposure of sensitive intellectual property

Construction firms handle more than just blueprints. Proprietary architectural designs, bid documents, financial plans, and sensitive client data are all highly valuable and highly sought after by cybercriminals. The theft or exposure of this information can have devastating consequences, from reputational damage and loss of competitive advantage to implications for critical infrastructure and national security.

## Commonly exploited vulnerabilities

Commonly exploited vulnerabilities by the above-mentioned ransomware groups include:

  * [**CVE-2025-31324**](https://www.rapid7.com/blog/post/2025/04/28/etr-active-exploitation-of-sap-netweaver-visual-composer-cve-2025-31324/) \- The SAP NetWeaver Visual Composer file upload flaw. It enables unauthenticated threat actors to send specially crafted POST requests to the /developmentserver/metadatauploader endpoint, leading to unrestricted malicious file upload and full system compromise.

  * [**CVE-2024-21887**](https://www.rapid7.com/blog/post/2024/01/11/etr-zero-day-exploitation-of-ivanti-connect-secure-and-policy-secure-gateways/) \- The Ivanti Connect Secure and Policy Secure command injection flaw enables authenticated administrators to execute arbitrary commands on the appliances by sending specially crafted requests.

  * [**CVE-2024-21762**](https://www.rapid7.com/blog/post/2024/02/12/etr-critical-fortinet-fortios-cve-2024-21762-exploited/) is a Fortinet FortiOS out-of-bounds write flaw that allows threat actors to gain super-admin privileges, bypassing the authentication mechanism, leading to remote code execution (RCE).

  * [**CVE-2024-55591**](https://www.rapid7.com/blog/post/2025/01/16/etr-fortinet-firewalls-hit-with-new-zero-day-attack-older-data-leak/) \- The Fortinet FortiOS and FortiProxy authentication bypass flaw enables threat actors to remotely gain super-admin privileges by making malicious requests to the Node.js websocket module. Attackers were observed leveraging the flaw to create randomly generated admin or local users and add them to existing SSL VPN user groups or newly created ones. In addition, they add or modify firewall policies and other settings and log into the SSL VPN using these rogue accounts to allow network tunneling.

  * [**CVE-2024-40711**](https://www.rapid7.com/blog/post/2024/09/09/etr-multiple-vulnerabilities-in-veeam-backup-and-replication/) \- The Veeam Backup and Replication deserialization flaw allows unauthenticated threat actors to initiate RCE.

  * [**CVE-2024-40766**](https://www.rapid7.com/blog/post/2024/09/09/etr-cve-2024-40766-critical-improper-access-control-vulnerability-affecting-sonicwall-devices/) \- The SonicWall SonicOS and SSLVPN improper access control flaw. It enables unauthorized threat actors to access resources and, under certain conditions, cause firewall crashes. 




## What to do next

In 2025, the construction industry faces unprecedented digital opportunities and rising cyber risk. [IoT, BIM, and cloud platforms have boosted efficiency but expanded attack surfaces](https://www.rapid7.com/blog/post/tr-building-construction-sector-threat-landscape-initial-access-supply-chain-iot/), making firms vulnerable to ransomware, supply chain breaches, and IP theft. These risks, driven by fragmented supply chains, legacy systems, human error, and insecure devices, are systemic, not isolated. Cybersecurity must now be treated as a core pillar of project management, equal to safety, cost, and schedule, requiring board-level commitment and industry-wide collaboration.

To build resilience, firms should modernize legacy systems, secure supply chains, protect connected devices, and train all staff in cyber defense. Proactive measures like risk assessments, secure-by-design technologies, unified frameworks, and incident response playbooks must replace piecemeal defenses. By embedding security into daily operations and culture, the industry can turn cyber resilience into a competitive advantage, ensuring that innovation and protection move together to secure construction’s future.

## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)