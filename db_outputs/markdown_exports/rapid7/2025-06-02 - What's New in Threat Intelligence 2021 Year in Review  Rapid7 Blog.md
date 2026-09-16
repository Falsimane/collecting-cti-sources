# What's New in Threat Intelligence: 2021 Year in Review | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/01/07/whats-new-in-threat-intelligence-2021-year-in-review/
- **Date :** 2025-06-02

---

_This post was originally published on the IntSights blog._

Last year marked a huge milestone with the [acquisition of IntSights by Rapid7](/rapid7-acquires-intsights/). The IntSights team is very excited to join a company committed to simplifying and improving security outcomes for its customers. Rapid7's focus is a great complement to the IntSights core mission to “democratize threat intelligence" for all. We look forward to continuing in this mission as part of the Rapid7 family, as our external [threat intelligence solutions](/products/threat-command/) are incorporated within the Insight platform.

Threat Intelligence solutions compete in an increasingly crowded marketplace. Our solution stands out from others by removing the inherent complexity of threat intelligence while helping organizations of any size or maturity minimize their external risk while significantly reducing their workload. Over the course of 2021, we continued to deliver on this core promise by adding additional value to our products through:

  * Expanding detection coverage and sources across the clear, deep, and dark web
  * Helping customers speed their response processes through an expanded investigation toolset
  * Continuously improving the user experience, ensuring our solutions deliver immediate value out of the box

** _“IntSights' competitive advantage lies in its simplicity."_****__**_\- Dave Estlick, CISO, Chipotle_

## 2021 IntSights External Threat Protection Suite highlights

### Expanded threat coverage

Over the course of 2021, we increased our Threat Command detections coverage in several key areas to offer customers additional protection and value. These expanded capabilities include:

  * **Phishing websites** : Detection and alert coverage for additional Phishing feeds including AlienVault, OpenPhish, Phishing Domain Database, PhishStats, and PhishTank
  * **Public repositories** : Expanded coverage for leaked secrets in both GitHub and GitLab
  * **Leaked databases:** Alerts on leaked databases that contain organization-specific PII data (such as phone number, physical address, date of birth)
  * **Black markets coverage** : Expanded detections of customer products offered for sale in dark web black markets and ability for customers to view decision parameters to understand why specific threats were elevated to alerts
  * **BOT data for sale** : Option to use the new "Bot price" condition to trigger alerts based on bot prices and easily initiate bot purchase requests from the Threats __ page

** _“IntSights gives us the ability to see a more granular view of our threats in a very easy-to-use fashion."_****__**_\- Zac Hinkel, Global Cyber Threat Manager, Hogan Lovells_

### Proactive phishing detection

In 2021, we offered a new solution called **Phishing Watch** that offers advanced and preemptive phishing detection capabilities that help customers identify attacks before phishing websites emerge. Phishing Watch employs a lightweight snippet installed on customer-facing websites that proactively detects the copying or redirection of legitimate/official websites to an illegitimate (and potentially phishing) website. Customers receive proactive notice of any phishing scams before they are employed, including the details required to enable automatic takedown of the phishing website and eradicate any threats in the early stages.

### Expanded research and investigation capabilities

This year, we also greatly enhanced the investigation capabilities and content within our Threat Intelligence Platform (TIP) to accelerate customers' ability to research and triage threats. The enhancements enable customers to easily understand the intent associated with indicators and prioritize those that pose the greatest risk. Features include:

  * Improved user interface that helps customers quickly investigate IOC and common cyber attack details
  * Expanded and accelerated investigation functionality including attack context, mapping tools, notes, and export functionality
  * Ability to easily share information on specific indicators with teams to enable better coordination and more proactive security posturing
  * Ability to analyze and understand the correlation of a CVE to cyber terms, view which feed reported the malware or actor, and see the first and last report date for better visibility and context on reported threats

![i83KD62gXpLUsp-kDPbBSBtx1lQ47wjX4d6hJPe6Ta5WD1OTONzlFk-g715KGkXJDg6r7s4g6HKj_ro8oztuoM1kt8msuQjdcT8gNXbR9ym9XifMlpU-G9rqoJe6mg--1-.png](https://www.rapid7.com/cdn/images/blt3776f6cc73e08823/683de6df4c5a0948555e0d0f/i83KD62gXpLUsp-kDPbBSBtx1lQ47wjX4d6hJPe6Ta5WD1OTONzlFk-g715KGkXJDg6r7s4g6HKj_ro8oztuoM1kt8msuQjdcT8gNXbR9ym9XifMlpU-G9rqoJe6mg--1-.png)

### IntSights Extend (browser extension)

Introduced earlier this year, IntSights Extend actively parses, enriches, and highlights cyber threat intelligence data from any web-based application, such as a technical blog detailing the latest breach or a raw intelligence feed. It actively scrapes domains, URLs, IP addresses, file hashes, email addresses, and CVEs to deliver contextualized risk-prioritized alerts at the click of a mouse. Additionally, layering real-time enriched threat intelligence over any web-based application allows security practitioners to perform end-to-end investigation and analysis. They can immediately detect if threat indicators are active within their environment and block them directly from the browser. Customers can also easily pivot to the IntSights platform for further analysis, investigation, and action.

### Threat library

Dedicated research analysts work behind the scenes to input up-to-the-minute intelligence. The research team includes detailed information on known threat actors, malware, campaigns, and associated MITRE TIDs to help security analysts spot trends and gain contextual details regarding threats targeting geographic regions, including threat actor engagement and reconnaissance. Security analysts can take immediate action on threats by adding IOCs associated with specific topics to their security devices, without ever leaving the library. The IOCs can also be tagged with malware, threat actor names, campaigns, and/or attack type to accelerate triage across existing security infrastructure.

![-WZO1L8iUI6jKkIVaMMF8_MnyZJj-PdHjsF_OMTw42TbrLkMhbgp6nRl9102Nh3-44MXrccZLbqLm8-at9tJl5Q4XFVrKSAULVGcXgOgll7a9Q1POxVdu7soyZZuRg--1-.png](https://www.rapid7.com/cdn/images/blt85d99d64a6fde4a9/683de6ff4c5a096b315e0d25/-WZO1L8iUI6jKkIVaMMF8_MnyZJj-PdHjsF_OMTw42TbrLkMhbgp6nRl9102Nh3-44MXrccZLbqLm8-at9tJl5Q4XFVrKSAULVGcXgOgll7a9Q1POxVdu7soyZZuRg--1-.png)

Vulnerability Risk Analyzer (VRA) customers can click on specific CVEs to view further details on the Vulnerabilities page. This helps customers prioritize vulnerabilities used in specific campaigns that affect their organization so they can focus on immediate updates and patching for the most relevant CVEs.

#### MITRE ATT&CK mapping

More advanced search capabilities to speed investigation plus details on MITRE ATT&CK framework tactics, techniques, and procedures (TTPs) are now mapped to Threat Library topics, bringing all relevant information related to a threat into one simplified view. Beyond the Threat Library, platform users can view and filter alerts by specific MITRE framework tactics and techniques for more context about threats in the customer environment.

#### IntelliFind

IntelliFind, our comprehensive dark web search tool, enables customers to directly search outside their digital footprint to immediately discover threat actor chatter and potential attacks targeting their organization or industry on the black market, hacking forums, paste sites, and other dark web sources across the attack surface. We offer the largest and most extensive database of these otherwise inaccessible sites.

## Workflow improvements and technology integrations

### Multi-tenant threat management

MSSPs and large enterprises with subsidiaries can now view and manage the threat data associated with all accounts, as well as navigate between customers, from a single dashboard, streamlining account management and saving money, time, and resources.

  * **Threat Command:** Those managing multi-tenant accounts can access each account's Threat Command alerts, remediations, and associated policy options from the tenant view. The expanded functionality also makes it easier for tenants and subsidiaries to consume and act on threat intelligence to improve their digital risk protection and cybersecurity posture. Alerts for multiple accounts can be displayed and managed simultaneously, as well as aggregated by date and category. Multi-tenant account owners can also engage with our expert threat analysts in real time to dig deeper into specific alerts and proactively reduce response time.
  * **TIP:** MSSPs can see each tenant's threat feeds and aggregated and prioritized IOCs from the TIP, as well as set IOC severity for all managed accounts.
  * **IntelliFind:** Using this exclusive dark web search tool, MSSPs gain access to advanced investigation capabilities and can view and manage queries and trigger alerts for multiple tenants via a single login.

**“**** _The new MSSP capabilities allow us to view and manage all of our tenants from a single dashboard. We can switch between our customers' tailored intelligence platforms with the click of a button. Also, we can easily generate reports to share with our customers, documenting the value they receive from Rapid7 threat intelligence."_****_-_**_Royi Biller, CEO, MT Cyber (MSSP)_

### Rapid7 InsightConnect Plugin for IntSights Threat Intelligence

Mutual customers of IntSights and Rapid7 InsightConnect (and InsightIDR or InsightVM) can now leverage contextualized threat alerts, indicators, and vulnerabilities within their Rapid7 SOAR solution, InsightConnect, helping them prioritize incident response and vulnerability management activities. This integration helps organizations gain a 360-degree view of the external threat landscape, align internal security enforcement, and expedite critical areas of security operations. The first ICON Plugin workflow (for Rapid7 InsightIDR) is now available in the Rapid7 Extensions Library. This workflow enriches IDR alerts by performing a lookup on all domains, hashes, URLs, and IPs in the Threat Intelligence _Investigation_ module. In addition, IntSights can now directly trigger an incident response workflow in InsightConnect based on generated alerts, enabling more efficient and effective responses to threats that the IntSights platform detects.

The **IntSights bidirectional app for Splunk** enables customers to bring actionable threat intelligence into their Splunk solution for a holistic view of threats targeting their environment. Building on existing functionality that facilitated the import of prioritized IOCs from the IntSights platform, the app introduced earlier this year enables customers to:

  * Identify attacks in progress on their network by correlating indicators in their environment with IntSights high-severity IOCs
  * Import Threat Command alerts and prioritized vulnerabilities from Vulnerability Risk Analyzer into the Splunk environment to continue triaging external threats directly from the Splunk dashboard
  * Instantly analyze and prioritize credible threats in the IntSights environment. When an alert, IOC, or CVE is found in the customer's Splunk environment, it is flagged simultaneously in Splunk and IntSights so that users can take action in either platform.



**Our native bidirectional application for IBM QRadar** allows customers to leverage the robust enrichment and investigation capabilities of the IntSights TIP in their QRadar environments. Mutual customers can:

  * Detect IOCs found in the network
  * View top malware and threat actors targeting the organization
  * Conduct comprehensive, end-to-end investigations directly within the Qradar environment



## Looking ahead

Looking ahead to 2022, some of the key themes and areas of investment that Rapid7's Threat Intelligence customers will experience include:

  * Delivering more visibility for faster decision-making with a new Strategic Intelligence module and custom reporting capabilities
  * Key integrations with Rapid7 products including the InsightIDR XDR/SIEM solution, the InsightConnect SOAR platform, and the InsightVM vulnerability management solution
  * New pricing and packaging model that scales with customer needs across the maturity spectrum
  * Continued investment in expanding intelligence sources and detections for reduced noise and better protection
  * Driving growth through a more optimized Threat Intelligence experience for MSSP partners



A big thank you to all of our customers and partners for working with us this year. We look forward to delivering even more value to our Threat Intelligence customers as part of the Rapid7 family, as well as sharing more about these investments and additional updates with you in 2022.

  


## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)