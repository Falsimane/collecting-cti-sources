# Meet Sekoia TDR: Our Threat Detection & Research Team

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/introducing-sekoia-tdr
- **Date :** 2024-05-29

---

This time, we're not revealing a new cyber threat investigation or analysis, but I want to share some insights about the team behind all Sekoia Threat Intelligence and Detection Engineering reports. Let me introduce you to the **Sekoia TDR team**.

## **An operational and research team**

**TDR** is the **Threat Detection & Research team** at Sekoia. Our main mission is to protect our Sekoia SOC Platform customers and partners by producing native and exclusive Cyber Threat Intelligence (CTI) and developing our integrated detection rules catalogue.

As cybersecurity is a collaborative effort, we regularly cooperate and share intelligence with our MSSP and technology partners, various other cybersecurity vendors, and their CTI teams. 

We also regularly collaborate with cybersecurity authorities, CERT communities, and law enforcement agencies (including Europol) to fight cybercrime globally.

![The new TDR badge](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7d8eb7c63a873a2a1b50_TDR-badge.svg)

The new TDR badge

The new TDR badge, thanks to Valériane! 

## **Our organisation**

Founded in 2020, **TDR** is a multidisciplinary team of around twenty passionate analysts with a wide range of expertise: detection engineering, technical and strategic analysis, threat hunting, reverse engineering, DevOps, etc. Our analysts have experience in defensive security from SOCs and CERTs, but some also have background in geopolitics or offensive security. They are primarily based in our offices in Rennes and Paris, while part of the team works fully remotely from various cities across France.

**TDR** is organised around 2 threat-themed squads and 4 chapters of expertise. Each squad is staffed by at least one analyst from each chapter to provide a 360° view of threats by tracking, contextualising, technically analysing and detecting them.

![TDR Organisation](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7d8fb7c63a873a2a1b6e_ORGA-TDR.svg)

TDR Organisation

Figure 1: TDR Organisation 

### The Squads

🐙The **‘Octopus’ squad** focuses on state-sponsored and strategic threats, such as cyber mercenaries and hacktivists. 

🦊The **‘Fox’ squad** tracks down financially motivated cybercriminal threats, such as Ransomware-as-a-Service, Business Email Compromise, Phishing-as-a-Service, loader, etc.

### The Chapters

#### **Strategic**

**The Strategic Chapter** is composed of analysts with a **geopolitical** background. They provide context on cyber threats and the ecosystem around them from a geographical and sectoral perspective.

![Discover our latest strategic threat landscape: Guarding Democracy - Assessing Cyber Threats to 2024 Worldwide Elections](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b59d_6a92a2b34b4041c693424cf6_6a2a7d8fb7c63a873a2a1b6a.webp)

Discover our latest strategic threat landscape: Guarding Democracy - Assessing Cyber Threats to 2024 Worldwide Elections

Discover our latest strategic threat landscape: [Guarding Democracy - Assessing Cyber Threats to 2024 Worldwide Elections](/blog/guarding-democracy-assessing-cyber-threats-to-2024-worldwide-elections)

#### Track

The **Track & Investigation Chapter** is staffed by technical threat intelligence analysts who track down attackers' C2 servers and the related malware and tools. They aim to provide fresh and exclusive indicators of compromise (IOCs) to the [Sekoia SOC Platform](/) via the Sekoia C2 Tracker, Sekoia YARA Tracker and Sekoia Malware Watcher internal sources.

![Sekoia C2 Trackers statistics \(between 2020 and 2023\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5ac_6a92a2ade17eff730b654a0c_6a2a7cd3c5337e0183cf0ae2.webp)

Sekoia C2 Trackers statistics (between 2020 and 2023)

Figure 2: Sekoia C2 Trackers statistics (between 2020 and 2023) 

Check out [our annual report](/blog/adversary-c2-infrastructures-tracked-in-2023) to learn more about adversary C2 infrastructure tracking!

#### Detect

The **Detection & Hunting Chapter** comprises detection engineers whose main task is to create and update the detection rules (Sigma, Sigma Correlation and Anomaly) available in the catalogue that is integrated into the Sekoia SOC Platform. To do this, they use our TDR Lab to simulate tools / malware or to replay attacks, analysing the logs left behind to create relevant rules for detecting malicious behaviour. They are also in charge of various TDR honeypot projects.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5a6_6a92a2ad3e6167cebbf6025d_6a2a79f21d83277227ac14eb.webp)

#### Reverse

Finally, the **Reverse Engineering Chapter** is formed by reverse engineers who technically analyse malicious code to better understand, track, and detect it. They are particularly responsible for creating malware configuration extractors to automate the production of IOCs.

Find out more about our reverse engineering work, with this [in-deph technical analysis report on the DiceLoader malware](/blog/unveiling-the-intricacies-of-diceloader).

## **The day-to-day life of TDR analysts**

The day-to-day work of TDR analysts varies according to their core expertise but can be categorised into two main activities:

### **Threat Intelligence**

Our priority is to provide actionable intelligence on cyber adversaries, their motivation, their victimology, the malware they use, the vulnerabilities they exploit and their TTPs (Tactics, Techniques and Procedures) to better understand and detect malicious activities. 

  * Monitoring through a wide range of internal, commercial and open sources
  * Capitalising and modelling in [**STIX 2.1**](https://oasis-open.github.io/cti-documentation/stix/intro.html) of the most relevant reports from the cyber community on the threats we track with priority. Most of these reports are also enriched with YARAs and new IOCs based on pivots.



![OSINT report modelisation \(STIX2.1\) in Sekoia SOC Platform](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5a3_6a92a2b1bd6424423eeefc27_6a2a7d8fb7c63a873a2a1b63.webp)

OSINT report modelisation (STIX2.1) in Sekoia SOC Platform

Figure 3: OSINT report modelisation (STIX2.1) in Sekoia SOC Platform 

  * Monitoring and tracking of intrusion sets, threat actors and their tools and malware
  * Investigating using open sources (including deep and dark web) and our exclusive telemetry
  * Writing private Threat Intelligence reports (**FLINTs - Sekoia FLash INTelligence reports**) and blog posts to share emerging threats, new attack campaigns or trends enriched with technical and strategic analysis.



![Sekoia FLINT report](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5a9_6a92a2b2693fca262e1b291e_6a2a7d8fb7c63a873a2a1b66.webp)

Sekoia FLINT report

Figure 4: A Sekoia FLINT report 

### **Detection Engineering**

We aim to provide our users with the most comprehensive catalogue of detection rules, enabling them to quickly detect the TTPs most commonly used by adversaries. Our rule creation efforts focus on the following areas: endpoint for workstations and servers, network outbound/inbound connections, cloud office applications, and identity management.

  * Creating **Sigma** and **Sigma Correlation** detection rules or Anomaly rules to detect the TTPs most commonly used by attackers to compromise Windows, Linux, Mac or Cloud (AWS, Azure, Google Cloud Platform) environments.
  * Updating catalogue rules to improve quality (reducing the number of false positives, for example).
  * Implementing and maintaining the rule creation workflow (CI/CD pipeline). For further details, see our dedicated [blog post on XDR detection engineering at scale](/blog/xdr-detection-rules-at-scale).
  * Creating a managed threat-hunting capability for our customers and partners.
  * Writing reports and blog posts.



![Sekoia SOC Platform built-in Rules Catalog](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5a0_6a92a2b06568d7e2b4089633_6a2a7d8eb7c63a873a2a1b5e.webp)

Sekoia SOC Platform built-in Rules Catalog

Figure 5: Sekoia SOC Platform built-in Rules Catalog 

To find out more about the **TDR detection strategy** , we have documented [the most frequently asked questions in the Sekoia documentation](https://docs.sekoia.com/xdr/FAQ/Detection_qa/).

## **Our R &D and publications**

**TDR** is an operational team responsible for producing on a daily basis the Sekoia exclusive CTI and the detection rules for our SOC Platform. In addition, we also operate as a research team dedicated to investigating and detecting the latest cyber threats alongside developing our own R&D projects to improve our knowledge of cyber threats and their tracking/detection. R&D also includes developing internal tools analysts use to conduct investigations and to manage various **honeypots** projects.

### Tooling

To discover new threats, speed up investigations and help non-technical analysts, we continue to develop new, in-house applications and projects such as honeypots (Windows, Linux, Edge devices/ IOT). All these internal tools are interconnected with our Sekoia SOC Platform and with third-party services to make life easier for analysts. For example, with **ASTRA** , we have a Cloud lab for easily detonating malware and collecting logs / raising alerts in our SOC Platform. Reversers also use it to carry out their malware analysis work. **ARIANE** is an online rule editor (**YARA, Suricata, Sigma**) who helps analysts write effective rules. We also share some of our tools, such as various [Maltego transforms](https://github.com/SEKOIA-IO/Community/tree/main/MaltegoTransforms) thanks to Félix.

![ASTRA, our Automatic Sandbox for Threat Research Analysis](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5af_6a92a2ae32517fc4025fcf50_6a2a7d8eb7c63a873a2a1b57.webp)

ASTRA, our Automatic Sandbox for Threat Research Analysis

Figure 6: ASTRA, our Automatic Sandbox for Threat Research Analysis 

### Sharing is Caring

As **sharing** is one of our core values, we regularly publish the results of our **TLP:CLEAR** research on the Sekoia blogand on our [Twitter/X](https://x.com/sekoia_io) account. IOCs, Sigma, and YARA rules are also available in the [Sekoia Community on GitHub](https://github.com/SEKOIA-IO/Community).

## Example of successful sharing

In September 2023, we successfully sinkholed a command and control server linked to the PlugX worms. We observed in 6 months of sinkholing more than 2,5M unique IPs connecting to it. We have shared with the authorities of the countries concerned the data on their compromised IPs and our help with a potential "sovereign" disinfection operations. 

To find out all about our PlugX sinkhole, read our [report](/blog/unplugging-plugx-sinkholing-the-plugx-usb-worm-botnet) and listen to Félix and Charles' [talk in BotConf](https://youtu.be/oega_kLTch0?si=YncFkIpawtkGzi6c) ! 

Last but not least, some of our research work has also been presented at **international cybersecurity conferences** such as [BotConf](https://youtu.be/oega_kLTch0?si=S5oAlt2atUTZzkF3) and [Virus Bulletin](https://youtu.be/lxFqvZGAmpI?si=U9CVKIFJHFiTaFqK).

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5b83e6167cebbf7b5cc_6a92a2afdae089660dfc3a7b_6a2a7d8eb7c63a873a2a1b5a.webp)