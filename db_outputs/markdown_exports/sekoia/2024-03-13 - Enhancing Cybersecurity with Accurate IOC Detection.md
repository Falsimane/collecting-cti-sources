# Enhancing Cybersecurity with Accurate IOC Detection

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/enhancing-security-with-ioc-detection
- **Date :** 2024-03-13

---

**Indicators of Compromise (IOCs)** serve as signals, hinting at potential security breaches or ongoing cyberattacks. These indicators consolidated in a single database range from IP addresses to file hashes and act as early warning signs, enabling organizations to detect and mitigate threats before they escalate.

At Sekoia, the IOC database is maintained and enriched by the Threat Detection & Research (TDR) team. This team consists of researchers and analysts with former experience in governmental agencies, military, and major private organizations. Their expertise and commitment to producing exclusive intelligence yield impressive results:**TDR revoked only 223 IoCs over a total of around 3 millions, which corresponds to a revocation rate of 0.01%**. 

Although indicators are integral to the Security Operations Center (SOC) and threat intelligence, they’re only one component in the system empowering teams to monitor and respond to threats. In this blog post, we’ll focus on different detection capabilities of the Sekoia SOC platform and answer the following questions:

  * Why are IOC detection rules the backbone of cybersecurity defense strategies?
  * How does IOC detection work?
  * Why do Sigma, Anomaly detection, and CTI rules complement each other? 



## **Understanding IOC Detection**

IOCs are red flags that help identify, trace, and block malicious activity. Any IOC has a limited lifetime and can be categorized depending on its type. Classic IOCs are domain names, IP addresses, hashes, email addresses, ports, URLs, filenames, processes, services, etc. However, IOCs may include non-IT artifacts like a bank account or phone number.

Sekoia maintains **the CTI database with millions of IOCs** ; any new ingested event is scanned against our CTI database. When the indicator is detected, the Sekoia Intelligence Feed rule immediately alerts users. In this way, IOC detection helps to identify potential security threats targeting systems. 

By leveraging sophisticated algorithms, IOC detection scans both past and present events to verify their authenticity against a comprehensive database of known threat indicators. Therefore, any suspicious activity, whether a new attack or a recurring threat, is promptly identified and addressed.

> Supporting a wide range of IOCs may be challenging, though our TDR team constantly monitors the database and applies different expiration rules to ensure IOCs are always up to date. This commitment results in accurate threat detection with a low rate of indicators revokation: 223 IoCs were revoked out of a total of 3 million IoCs in 2023. 

**Erwan Chevalier, Security Engineer - Threat Detection & Research Team **

## **The Sekoia SOC platform: A beacon of security**

IOCs created by our Threat Detection & Research team are smoothly integrated into the platform. In addition, we offer users the ability to import indicators from various sources and create **IOC Collections**. These collections provide detailed telemetry data for users to apply in their detection methods. IOC Collections simplify the integration of external threat intelligence and are easily accessible from the Intelligence Center menu. 

Furthermore, the Sekoia SOC platform supports creating and applying **Sigma** , **Anomaly Detection** , and **CTI rules**. 

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5c969291914889b1956_6a92a2dadae089660dfc4fec_6a2a7d29236382abd52fce7e.webp)

## **How does the Sekoia detection engine work?**

The process begins with the Sekoia TDR team meticulously curating a structured and contextualized database of IOCs gleaned from their extensive research efforts. These IOCs encompass a wide range of threat indicators, including IP addresses, domains, URLs, file hashes, and email addresses.

As events are ingested into the Sekoia SOC platform, they undergo rigorous scanning against this comprehensive database. Any matches trigger the built-in Sekoia Intelligence Feed or other rules that immediately raise an alert, allowing organizations to take swift action against potential threats. Note that the CTI rule is built-in to detect malicious activity based on a list of IOCs from Sekoia.io's own Intelligence feed, continuously updated by our Threat Detection & Research team (**Sekoia’s intelligence is based on more than 400 sources and more than 8 million of IOCs**). 

### **Sekoia's Retrohunt Engine**

What sets Sekoia apart is its innovative Retrohunt engine, a groundbreaking feature that ensures no threat goes unnoticed. Whenever a new indicator appears in the IOC database, Sekoia SOC performs retroactive hunting across historical events, effectively combing through past data for any signs of malicious activity. 

Our IOC detection includes retrohunting based on the time frame of the indicator. By default, we always extend retrohunting by 5 additional days from the start date. If the start date of an indicator is unspecified, retrohunting will commence 5 days before the current date. Sekoia initiates retrohunting as promptly as possible, contingent on available resources. We carefully schedule this operation to minimize any impact on user experience. 

This proactive approach bolsters your defenses against ongoing attacks and provides invaluable insights into past security incidents. For organizations seeking additional customization and control, Sekoia offers to import their curated lists of IOCs for retrohunting. This feature empowers SOC teams to tailor their detection strategies to specific threat landscapes, ensuring comprehensive coverage across all fronts. Sekoia's IOC collections support a diverse array of indicator types, and each event is meticulously verified against these indicators to detect various threat vectors.

_In 2024, the significance of IOC detection in fortifying digital assets comes to the forefront. To support accurate IOC detection, Sekoia scrutinizes a myriad of event fields, helping organizations to detect potential threats, proactively safeguard their systems against malicious attacks, and stay one step ahead of adversaries._