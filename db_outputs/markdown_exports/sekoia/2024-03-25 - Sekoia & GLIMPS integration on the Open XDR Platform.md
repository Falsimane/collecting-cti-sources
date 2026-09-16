# Sekoia & GLIMPS integration on the Open XDR Platform

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/sekoia-io-and-glimps-a-new-example-of-interoperability-within-the-open-xdr-platform
- **Date :** 2024-03-25

---

_This blogpost was written by_[ _Glimps_](https://www.glimps.fr/) _and_[ _Sekoia._](/)

The Open XDR Platform is an alliance of specialized, complementary cybersecurity solution providers, that provide a rapid, coordinated response to the ever-increasing number and sophistication of cyberattacks.

This modular, customizable approach provides analysts and security managers with the components they need to better deliver their day-to-day business. This alliance is based on the development of connectors between the various players that enrich one another. With this in mind, and to take advantage of the synergies offered by the Open XDR Platform, Sekoia and GLIMPS have been working on the interoperability of their solutions. 

## First use case: The Sekoia connector in GLIMPS Malware

The GLIMPS Malware Expert natively integrates a Sekoia connector, providing a first level automatic enrichment for analyses. This integration provides Malware Expert users an overview of the contextual information that relates to malware identified by GLIMPS and known to Sekoia.

![GLIMPS Malware Expert natively integrates a Sekoia connector, enabling an initial level of automatic enrichment for certain analyses.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63fcd1cab63350d8202_6a92a40ae9a71d4228405e61_6a2a7a82bf2797708e071981.webp)

GLIMPS Malware Expert natively integrates a Sekoia connector, enabling an initial level of automatic enrichment for certain analyses.

### **And in practice?**

When an alert is sent after analysis by the GLIMPS Malware Expert, the full characterization is displayed in the GLIMPS Malware Expert view. In addition a first level of information on the threat is displayed : the presentation of the malware known by Sekoia Intelligence. With a single click, Sekoia Intelligence customers can pivot their investigation through the Sekoia platform, benefitting from known STIX objects that are associated with the malicious code analyzed by GLIMPS. Such intelligence may include the modus operandi, targets, or indicators of compromise (IOC). Making it easy for analysts to choose the right actions that detect and remediate the threat.

![Sending an alert following analysis by GLIMPS Malware Expert within the Sekoia XDR platform.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63fcd1cab63350d81ff_6a92a40e6568d7e2b4095622_6a2a7a83bf2797708e07199f.webp)

Sending an alert following analysis by GLIMPS Malware Expert within the Sekoia XDR platform.

![Analysis of an alert by GLIMPS via the Sekoia XDR platform](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63fcd1cab63350d81fc_6a92a40d6568d7e2b4095528_6a2a7a83bf2797708e07199c.webp)

Analysis of an alert by GLIMPS via the Sekoia XDR platform

### **What added value?**

The use of Sekoia operational intelligence enables the analyst to immediately understand the threat identified by the GLIMPS detection engine. By doing so supports analysts to :

  * Federate cross-referenced data on the threat in a single interface


  * Accelerate tactical decision-making and operational responses by providing context



The combination of GLIMPS's detection power and Sekoia Intelligence's knowledge enables the analyst to immediately understand the scale of the threat ; the Mean Time to Detect (MTTD) is greatly accelerated.

Switching over to the full Sekoia interface to access Sekoia Intelligence, enables customers to benefit from the full CTI knowledge of the identified threat and support mitigating responses. This time, the "Mean Time to React" (MTTR) has improved significantly.

## **Second use case: integrating GLIMPS Malware into Sekoia SOC platform (XDR)**

The aim of this integration is to automate the investigation and in-depth analysis of files linked to alerts from different sources, directly in the Sekoia SOC platform console.

The GLIMPS connector in Sekoia Defend can be configured in a matter of seconds using two elements:

  * The URL of a GLIMPS Malware instance
  * A GLIMPS API key



Once configured, an enrichment and analysis playbook is then available in Sekoia Defend, making it easy to call up GLIMPS Malware to access existing analyses.

![Use case for integrating GLIMPS Malware into the Sekoia XDR platform](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63fcd1cab63350d8208_6a92a40bbd6424423eef598a_6a2a7a83bf2797708e071993.webp)

Use case for integrating GLIMPS Malware into the Sekoia XDR platform

In just a few seconds, a "simple" result is obtained, including :

  * File status: Malicious |Suspect | Safe
  * Threat score
  * Malware family
  * Link to the full GLIMPS interface



![The use of GLIMPS’ eXtended Malware Analysis Platform within the Sekoia Defend XDR.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63fcd1cab63350d8205_6a92a40c6568d7e2b4095491_6a2a7a83bf2797708e071997.webp)

The use of GLIMPS’ eXtended Malware Analysis Platform within the Sekoia Defend XDR.

### **What added value?**

The use of GLIMPS Malware in the Sekoia XDR enables :

  * **Speed up decision-making** : the in-depth file analysis provided by GLIMPS contributes to a rapid understanding of the threat and access to a very precise level of detail on each detected threat. The information extracted and shared on the platform also facilitates the implementation of security rules.
  * **Automate alert processing:** with this integration, all alerts showing signs of suspicious files can be automated. For example, as soon as an alert is identified, the file associated with the alert can be automatically transmitted to GLIMPS for in-depth analysis and characterization of the threat.
  * **Optimize resources:** by automating redundant tasks and simplifying malware analysis, security teams can concentrate on the most complex threats, and reduce the time spent triaging alerts and raising doubts.
  * **Facilitate incident response:** once the malware analysis is received by the Sekoia playbook, further corrective actions can be automated via the Sekoia platform. For example, if a system is identified as being infected by a specific ransomware, the Sekoia SOC platform can automatically trigger containment measures to isolate the infected system from the rest of the network, preventing the threat from spreading.



If you'd like to find out more and discover all the possibilities offered by integrations within the platform, such as, Sekoia, HarfangLab, Vade, Gatewatcher, Pradeo, Wallix and GLIMPS. Please visit the [Open XDR Platform](https://www.openxdrplatform.io/) to learn more.

And to find out more about GLIMPS, it's here! 👇

### **Discover GLIMPS and boost the intelligence of your lines of defense**

With over 10 years' expertise in AI and reverse engineering, GLIMPS is the French specialist in deep file analysis for detecting and characterizing the most sophisticated threats in a matter of seconds. GLIMPS has developed a technology that sets itself apart from traditional detection techniques by focusing code analysis. Its Deep Learning-based Artificial Intelligence engine detects any form of Malware within any type of file by code comparison, even if it has undergone significant evolution. This scientifically recognized technology is known as Code Conceptualization.

GLIMPS offers 3 solutions based on its xMAP to meet different needs and profiles:

  * GLIMPS Malware Kiosk: is a user portal through which any employee, whatever their cybersecurity knowledge, can test all the files they receive on a daily basis and quickly obtain a verdict.
  * GLIMPS Malware Detect enables advanced detection and rapid characterization of malware. After analysis, GLIMPS Malware Detect returns a first level of information to users.
  * GLIMPS Malware Expert is a true expert tool for alert and threat qualification, investigation and incident response.



For more information, visit the [GLIMPS website](https://www.glimps.re/en/).