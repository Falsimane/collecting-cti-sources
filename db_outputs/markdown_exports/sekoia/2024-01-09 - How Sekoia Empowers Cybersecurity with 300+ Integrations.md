# How Sekoia Empowers Cybersecurity with 300+ Integrations

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/sekoia-io-empowers-cybersecurity-with-170-security-integrations
- **Date :** 2024-01-09

---

Sekoia.io recognizes the significant investment and effort that organizations have put into their existing security infrastructures. We also realize the flexibility needed to choose the best new tools for safeguarding critical assets and data.

To enable this flexibility and streamline security operations, Sekoia.io adheres to a technology-agnostic approach and offers**integrations with 300+ tools and third-party platforms**. Our methods, including open APIs, cloud-to-cloud connectors, SOAR, Data Streaming, and log forwarders, equip organizations with unique detection and investigation capabilities. We enable building a holistic approach to threat detection and response by offering a large set of security integrations with Cloud and SaaS platforms, Identity and Access Management solutions, Endpoints, and Networks.

_In this article, we explain:_

  * How we prioritize and develop integrations to tackle challenges faced by security executives and meet the operational demands of SOC teams.
  * Why we foster a culture of collaboration and openness when it comes to integration development.
  * What our integration ecosystem is, and how it helps to achieve full visibility while preserving data integrity, confidentiality, and availability.



## **Significance of security integrations**

Integrations are pivotal in creating a seamless and proactive security environment. According to [Ernst & Young](https://assets.ey.com/content/dam/ey-sites/ey-com/en_us/topics/alliances/ey-how-does-rationalizing-cybersecurity-tools-enhance-security-effectiveness-and-efficiency.pdf), many large companies deploy numerous tools from various vendors, often reaching **100 tools from 35 or more providers**. This sprawl not only increases costs but also undermines agility and impacts the enterprise risk profile.

As the number of tools is soaring, enterprises aim to integrate with these tools and automate workflows to identify weak points. We address this need by developing robust and adaptable integrations. Thorough investigation, prioritization, and collaboration allow us to build purposeful integrations that have significant advantages.

### **Enhanced comprehensive visibility**

Integrations bring together diverse security tools, such as endpoint detection and network monitoring. This amalgamation provides a unified view of the security landscape: Sekoia.io XDR relies on integrations to detect threats that leave footprints and impact multiple layers or facets of infrastructure, including network, endpoints, cloud, applications, IAM, etc. Security teams, in turn, can trace activities across different channels, pinpointing anomalies and intricated threats with greater accuracy.

### **Streamlined threat investigation and response**

The correlation of logs and data from different sources significantly simplifies threat investigation. Integrations also help aggregate and analyze data from multiple points, offering insights into the causality and progression of threats. This facilitates quicker identification of the root causes and enables faster responses to security incidents.

### **Proactive security measures**

Security integrations simplify implementing automated responses to detected threats and establishing proactive defenses. By synthesizing data from various sources, we can develop more sophisticated detection rules and response strategies, staying ahead of evolving cyber threats.

### **Unified security posture**

Integration leads to a cohesive security approach, eliminating silos and ensuring all systems work in harmony.

### **Improved threat intelligence**

By combining insights, companies get detailed and contextual information about potential threats. In this way, integrations address the need for data correlation and analysis, helping to uncover patterns, threat actors, and techniques they use.

![Significance of security integrations. Source: Sekoia.io](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5eaa54c8f443fa4f908_6a92a3253e6167cebbf64a54_6a2a7ca6a684a8e4e0ff8734.webp)

Significance of security integrations. Source: Sekoia.io

With all the above-mentioned advantages, security integrations appear to be a significant enhancement for any SaaS platform with XDR/CTI capabilities. However, their development may be associated with challenges. Each tool has its unique interfaces and protocols, and some platform ecosystems aren’t as open to integrations.

The Sekoia.io team needs to normalize and harmonize the semantics of each product to ensure that events produced by two EDRs edited by different vendors become comparable. To reach this goal, we conduct a thorough investigation and work closely with experts, partners, and vendors. By adopting this approach, we overcome challenges, validate and refine integrations, and enhance our integration ecosystem.

## **Sekoia’s integration ecosystem & development**

[Sekoia.io's integration ecosystem](/integrations) is both extensive and evolving, currently boasting over 300+ integrations with continuous work on new ones. This diverse range includes our sought-after integrations, namely:

  * Office365
  * Fortinet
  * Windows
  * Proofpoint
  * Crowdstrike
  * Salesforce
  * SentinelOne
  * [Zscaler](https://blog.sekoia.io/integrating-zscaler-zia-with-sekoia-io/)
  * Azure Active Directory (Microsoft Entra ID)



When developing these integrations, we adhere to a precise integration development workflow to achieve the integrity of systems, streamline response time, and facilitate maintenance. Therefore, the roadmap consists of several mandatory phases, with the initial research as a starting point. 

### **Initial research and prioritization**

Requests for integration development come from our clients and partners. Different teams involved in assessing needs and typical use cases decide which integrations to prioritize. When establishing priorities, we focus on aligning integrations with customer requirements and enhancing our capability to detect and mitigate threats.

Once priorities are set, our team gathers information about the technology, its exact name, version, and type. We also sign legal documents required by other vendors, such as NDA, TPA, etc., if needed.

By establishing multiple legal-backed, official partnerships with vendors and building durable relationships within our ecosystem, we support a collaborative foundation of work. This ensures that we start development with all necessary tools and resources–for example, documentation, access to a test instance to validate the integration, and a technical point of contact to support our development team.

### **Requirements and specifications**

The second phase involves a detailed assessment of requirements, specifications, and data flow. It’s crucial to ensure that event logs will be accurately ingested, normalized under the ECS format, analyzed, and indexed by the parser.

Our team undertakes an in-depth study of API specifications, log format, and log examples. If all prerequisites are met, we set a clear blueprint, guiding the development process towards creating a security integration that aligns with the intended objectives.

### **Design and implementation**

This phase involves careful architecture and system integration design, followed by meticulous implementation. At first, a new integration and public documentation become available in a _BETA version_. Our team communicates the availability of this version to the customer. After getting feedback, we analyze if the integration needs improvement.

The integration becomes _generally available_ only after required improvements and thorough testing. We aim to build fully documented, reliable, and secure integrations, keeping **test coverage at the 90%**. 

### **Evaluation and maintenance**

The post-implementation phase includes evaluation and maintenance of the integration. Upon customer requests, our team can check the parser to add and normalize new fields, update field names, and enhance smart descriptions.

Whenever possible, Sekoia.io builds technical partnerships with vendors to guarantee that the integration works as expected. By reacting to any technical changes made on the vendor side, we adapt and customize integrations in a timely manner. 

![Integration Development Steps at Sekoia.io](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5eaa54c8f443fa4f905_6a92a3266568d7e2b408e1c9_6a2a7ca6a684a8e4e0ff8737.webp)

Integration Development Steps at Sekoia.io

Once integrations are released, our research team (TDR) can create detection rules based on TTP patterns and the specific technologies we integrate. These rules help detect suspicious activity. 

## **Challenges and future of integrations development at Sekoia**

Integration development often involves overcoming challenges such as compatibility issues, data mapping, API changes, and evolving specifications. Sekoia.io addresses these challenges through a combination of expertise, advanced technology, and a collaborative approach. We also rely on feedback and contributions from our community, partners, and clients to enhance and refine our integrations. Customer feedback plays a significant role in shaping our integration roadmap and building solutions that meet the evolving needs of the cybersecurity community.

> _In 2024, I envision not only expanding our catalog to a robust 250-300 integrations but also ensuring that each one operates flawlessly. We're committed to an ongoing process of testing and refining our integrations to guarantee uninterrupted service and focus on enhancing our API documentation for greater user-friendliness_.  
> —**Sebastien Quioc, Head of Integrations at Sekoia**

To continue nurturing and promoting a collaborative development approach, we actively inviting partners and other entities to contribute to our integration ecosystem. This is facilitated through:

  * **Community Contributions:** Our open GitHub repositories, such as the [Intake Formats](https://github.com/SEKOIA-IO/intake-formats) and the [Sekoia Automation SDK](https://github.com/SEKOIA-IO/automation-library), invite contributions for developing high-quality parsers and automation modules. The collaborative environment ensures that the information extracted from events optimally serves for decision-making.
  * **Educational Support:** We offer targeted e-learning training for partners on integration development, complemented by comprehensive public documentation. This educational framework encourages partners to participate in the development process, thereby enhancing the relevance and effectiveness of our integrations.
  * **Intake Parsers:** The intake parsers are a critical component of our integration process, designed to extract and normalize key information from events. By engaging community to participate in their development, we ensure the quality of these parsers and thought-out pipeline structure.



Beyond traditional integrations, Sekoia.io places significant emphasis on playbooks and automation. Our SDK enables the creation of modules that define triggers and actions for automated responses to cybersecurity events. This capability is particularly beneficial for SOC teams, allowing them to implement automated workflows that enhance their strategic focus and operational efficiency.

As we look towards the future, Sekoia.io is dedicated to expanding its integration ecosystem with a strong focus on the accuracy and ongoing maintenance. We anticipate a future where integrations are increasingly shaped by the diverse and evolving cybersecurity needs, helping both our partners and clients to eliminate data fragmentation and get actionable knowledge.

_This article has been updated; it originally stated Sekoia has 170 integrations. As of July 2026, it now has over 300 integrations._