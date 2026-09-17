# XDR vs Ransomware: Everything You Need to Know

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/xdr-vs-ransomware-en
- **Date :** 2022-04-22

---

Ransomware are still boasting a first rank among cyber threats in 2022 for all companies from SMEs to large groups, and even in the public sector. Yet this threat, albeit very real and dangerous, is no longer unavoidable thanks to open XDR.

![Attaques par ransomware rendues publiques en 2021](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6701584be1e5d9dd5a4_6a92a48532517fc402606ff9_6a2a790593217eae509be547.webp)

Ransomware attacks made public in 2021 (Source: Sekoia DarkWeb Monitoring)

## Use Case: Beating ransomware with Sekoia XDR

[Ransomware groups](/blog/ongoing-roaming-mantis-smishing-campaign-targeting-france) deploy a [diverse arsenal of tools, techniques and malware](/blog/the-story-of-a-ransomware-builder-from-thanos-to-spook-and-beyond-part-2) to carry out their attacks. The sophistication level is also quite heterogeneous depending on attackers and their targets' maturity level.

If the advantage seems to reside with attackers, the defence can still rely on various opportunities to detect and block the attack before any data gets exfiltrated or the ransomware spreads to the entire information system.

The Kill Chain displays the various stages of a computer intrusion. It lists the numerous [tactiques, techniques and procedures that attackers use](/blog/an-insider-insights-into-conti-operations-part-one). It also offers defenders as many possibilities to block the intrusion before impacts get too large.

![MITRE ATT&CK Kill Chain](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6701584be1e5d9dd5ad_6a92a4848d1115926b20c1d9_6a2a790493217eae509be53f.webp)

MITRE ATT&CK Kill Chain

At Sekoia we adapted this Kill chain to counter-ransomware operations:

![Sekoia ransomware kill chain](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6701584be1e5d9dd5aa_6a92a48ddae089660dfd5f8f_6a2a790593217eae509be565.webp)

Sekoia ransomware kill chain

Here are a couple of [examples](/blog/nobeliums-envyscout-infection-chain-goes-in-the-registry-targeting-embassies) to better grasp how Sekoia XDR can detect and block such ransomware attacks:

### **Initial access**

Ransomware operators can rely on several means to breach their victims' information system:

  * **Exploiting a vulnerability on an internet-exposed piece of equipment (VPN, Microsoft Exchange and Sharepoint, Citrix, etc.)** The Sekoia XDR catalogue of rules is regularly updated with new rules that can detect the actual exploitation of the most in-use vulnerabilities. Detecting the exploitation of such vulnerabilities as soon as possible enables to stop or slow down the attackers, who will have to find another point of entry into your information system.



![Exemple de règlesdisponibles dans le catalogue de Sekoia XDR](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6701584be1e5d9dd5b5_6a92a488dc307112383348bf_6a2a790593217eae509be553.webp)

Example of rules detecting the exploit of CVEs, available from the Sekoia XDR rules catalogue

  * **Attack attempt by brute force on RDP accesses** : Sekoia XDR can also rely on an anomaly detection engine [FR] enabling the creation of statistical rules based on the "normal" behaviour of the information system. These rules then provide a baseline to detect abnormal behaviour. For instance: A higher-than-usual count of failed authentication attempts on an internet-facing service (such as RDP) will trigger an alert.



![Sending a phishing e-mail with a booby-trapped attachment carrying malware such as Emotet, QBot, or even BazarLoader. Source: Sekoia SOC platform](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6711584be1e5d9dd5be_6a92a48751d97c29d2a32a1d_6a2a790593217eae509be54d.webp)

Sending a phishing e-mail with a booby-trapped attachment carrying malware such as Emotet, QBot, or even BazarLoader. Source: Sekoia SOC platform

  * **Sending a phishing e-mail with a booby-trapped attachment carrying malware such as Emotet, QBot, or even BazarLoader** : In the case where a user would have opened a malevolent attachment containing malware such as Emotet, its execution will leave numerous traces. These can offer several [detection opportunities](/blog/improving-threat-detection-with-sigma-correlations). This is where [Cyber Threat Intelligence (CTI)](/blog/hatching-triage-to-enhance-sekoia-io-cyber-threat-intelligence) enters the stage. Knowing and following the QBot threat on a daily basis enables the availability of the most fresh Indicators of Compromise (IOC) in order to detect, for instance, communications between the Emotet instance and the attackers Command & Control (C2) servers.



![Alerte contextualisée liée à Emotet](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6711584be1e5d9dd5b8_6a92a48a3e6167cebbf70ba2_6a2a790593217eae509be559.webp)

One contextualised alert based on a malevolent Emotet communication

### **Credential access**

To obtain higher permissions throughout their victims' information systems, [ransomware operators](/blog/vice-society-a-discreet-but-steady-double-extortion-ransomware-group) use various techniques and tools such as Mimikatz to procure accounts credentials with elevated privileges.

![détection des outils de collecte d’identifiants](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6701584be1e5d9dd5a7_6a92a48c69291914889a5ae7_6a2a790593217eae509be562.webp)

Detecting credential stealers

With Sekoia XDR, these techniques and tools are swiftly detected thanks to rules and IOCs dedicated to such TTPs. A remediation playbook, combined with an EDR such as HarfangLab offers an easy way to stop the [threat](/blog/bumblebee-a-new-trendy-loader-for-initial-access-brokers).

### **Defense evasion**

Attackers generally reuse the same techniques across their intrusions. One of their favourite actions consists in deactivating the antivirus (notably Microsoft Defender) or the log generation on compromised machines.

![le catalogue de Sekoia XDR](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6711584be1e5d9dd5c1_6a92a48bcd1cab63350d2b2c_6a2a790593217eae509be55f.webp)

The Sekoia XDR catalog

The [Sekoia XDR](/platform/defend) catalog contains around 50 rules to detect the deactivation of security tools.

### **Lateral movement**

After compromising at least one machine, the attackers will pursue lateralisation. This means that they will move through the victims' information systems in order to reach other workstations or servers, and thus extend their privileges or find confidential data.

![Intelligence center of Sekoia. Investigation about Cobalt Strike.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6701584be1e5d9dd5b2_6a92a486bd6424423eef6bfa_6a2a790593217eae509be54a.webp)

Intelligence center of Sekoia. Investigation about Cobalt Strike.

To that end, they generally use turnkey tools such as Cobalt Strike, or even native Microsoft tools such as PsExec that can be routinely used by legit system administrators. This is why contextualisation is paramount. Without it, activity that is legitimate when wielded by an administrator could be indistinguishable from malevolent business. IOCs alone cannot make that distinction.

### **Exfiltration**

When attackers look for confidential information, they pursue one single objective: exfiltrate this data. This is the jist of what is called double extortion. Firstly, the victim is demanded a payment to liberate their system; secondly, exfiltrated data are held hostage under the threat of public divulgation. This is why [ransomware groups proceed to exfiltrate as much sensitive data](/blog/sekoia-io-mid-2023-ransomware-threat-landscape) as possible: before cyphering data in place, they secure their back.

![An anomaly detection rule](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6711584be1e5d9dd5be_6a92a48751d97c29d2a32a1d_6a2a790593217eae509be54d.webp)

An anomaly detection rule

An anomaly detection rule will identify an unusual peak in the output feed of an information system, notably during week-ends or holidays. These are privileged periods for ransomware groups to carry on their attacks.

More classical rules will detect the use of tools such as RClone: such tools are in wide use among certain [ransomware groups](/blog/an-insider-insights-into-conti-operations-part-two).

### **Command & Control**

All along their intrusion, the tools that attackers use such as [Cobalt Strike](/blog/hunting-and-detecting-cobalt-strike) are communicating from within the victim's network towards malevolent servers.

![La cyber threat intelligence de Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6711584be1e5d9dd5bb_6a92a48e9f9b7f8b2cd0bb8a_6a2a790593217eae509be556.webp)

Sekoia's cyber threat intelligence

Thanks to Sekoia's [CTI](/glossary/cti) that tracks the C2 servers of hundreds of malevolent codes such as Cobalt Strike, these communications can be quickly detected and blocked. Bespoke rules designed from the careful lab analysis of malware samples will complete or confirm the initial detection.

## To conclude

Sekoia XDR leverages a balanced catalogue of interfaces and rules that can seize attacks at any point along the kill chain, thus deterring further impacts on a target's information system. This is made possible by the cross-domain observability and actionnability that only [open XDR](/blog/xdr-is-not-edr) provides, and the accuracy and relevancy that only highly [contextualised Threat Intelligence](/blog/threat-intelligence-is-not-only-on-a-spectrum) is capable of.