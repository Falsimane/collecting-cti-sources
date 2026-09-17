# Happy YARA Christmas: How Sekoia TDR Uses YARA Rules!

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/happy-yara-christmas
- **Date :** 2024-12-19

---

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5866568d7e2b409bb67_6a92a22ba7a0bb1897156bca_6a2a7e96b97c48a61ea60cc8.webp)

In the ever-evolving landscape of cybersecurity, effective threat detection is paramount. Since its creation, YARA stands out as a powerful tool created to identify and classify malware. Originally developed by Victor Alvarez of VirusTotal, **YARA has become a vital tool for security professionals seeking to streamline their threat-hunting processes**.

The Sekoia.io Threat Detection and Research (TDR) team incorporates YARA into its threat hunting workflow addressing various needs such as **identifying threats** , **tracking the evolution of malware families** , **infection chains** , and **uncovering suspicious files from unknown threats**. This article outlines the daily use of YARA at TDR and the tools that we use. More than making YARA rules our own, **we are sharing most of the created rules with our customers and partners via our platform** , it helps them in their investigations, triage process and DFIR engagements.

This blog post on our use of YARA rules is also an opportunity for us to announce [**the release of hundreds of our YARA rules on GitHub**](https://github.com/SEKOIA-IO/Community/tree/main/yara_rules), which are now **directly integrated into VirusTotal for detection**. The community has contributed many ideas for detection rules, so it's our turn to share a part of our own rules.

## What is YARA?

YARA is a **pattern-matching engine** designed to help security analysts in the identification and classification of malware samples. "YARA" stands for "Yet Another Recursive Acronym". It uses a flexible and powerful rules-based approach to match patterns in files and processes, allowing for the detection and **identification of malware quickly in large data sets**.

This technology allows users to create rules that describe the characteristics of any file, literally ANY file. These rules can include strings, binary and regex patterns. The matching condition in YARA rules is highly customisable and can include logical operators and modifiers, making it possible to create precise and complex detection criteria.

By writing signatures that capture the unique attributes of a file, any malware researcher can detect known threats in files, volatile memory, network packets and even logs (yes...) ! 

Of course, **using YARA alone from the command line is not so fancy and customisable**. It reveals its full potential integrated with other security tools and frameworks, enhancing its utility in comprehensive malware analysis and incident response workflows. Several programming and scripting languages offer a library for dealing with YARA rules. This enables them to be integrated into SIEM, IDS/IPS or EDR systems, for example.

## YARA rules at Sekoia.io

The Threat Research and Detection team uses YARA rules to achieve one of its main objectives: track threats actively. The main goal behind this mission is to get new Indicators of Compromise (IoCs) related to infection vectors, malware, tools and threat actor’s infrastructure to feed our XDR and Threat Intelligence customers. 

The YARA rules that we are using to track threats are shared with our customers but also used on other third party services to notify us when a rule is triggered. Among the wildly available services that we use: [**VirusTotal**](https://virustotal.com), [**Triage**](https://tria.ge/), or the [**YARAify**](https://yaraify.abuse.ch/) project from Abuse.ch. These services allow users to submit a file to identify whether it can be trusted. This file is scanned by security products and by detection rules submitted by analysts.

When a rule is triggered by a file, the file attributes are received and processed in-house, enriching the matched file with a context, for example, linking it in STIX to a known intrusion set, campaign, malware and/or tool. Some files can be retrieved and stored in our malware zoo by using [**AssemblyLine**](https://cybercentrecanada.github.io/assemblyline4_docs/) for further analysis, such as extracting their configuration. Some parts of the extracted configurations such as C2s, file paths, mutexes etc. can then be transformed into STIX new indicators for detection. 

More than feeding **Sekoia.io’s threat intelligence** with IoCs, TDR's analysts often use YARA for hunting purposes. In fact, **YARA also serves to discover anomalies in files** , which can lead to discovery of new malware, exploits, or parts of infection chains, such as decoy documents, malicious archives, emails etc.

**Being creative to draft hunting rules is the most challenging part of YARA** rule creation. However, it's also the most interesting as this shows you **the limitless of YARA capabilities when it comes to match any kind of file**. 

#### Would you like to learn more about how we investigate code using YARA?

Charles Meslay presented this year at [**SSTIC'24**](https://www.sstic.org/2025/news/) how pivots can be made between codes by using YARA. This talk, in French, shows the philosophy and the methodology that we use at TDR to sign malicious binaries. You can watch it below.

## Rule creation process

In our day-to-day work as CTI analysts, we enrich and capitalise in STIX 2.1 format all the relevant reports published in open source, incidents spotted by partners or our XDR telemetry. This work involves looking at heuristics in order to track adversaries infrastructures, and **sign each malware** , **tool** , or **atoms of infection chains** described in these reports to improve our adversaries tracking. 

**Any adversary activity which is written on disk or loaded in memory can be signed using a YARA rule.** Therefore we try to create YARA rules on:

  * **Infection chains** : including exploits, malicious documents, archives, emails, validators etc. - as many adversaries don’t modify their whole infection chain when it comes to target several victims and between campaigns. 
  * **Malicious codes** : including binary files, shellcodes, malware modules, configuration, OSTs, interpreted scripts (such as VBS, PowerShell, JScript, Bash etc.) - as most of the adversaries don’t use disposable or victim-specific implants. 
  * **Tools and exploits:** including reconnaissance, lateralization, EoP exploits and exfiltration tools - open sourced or not - dropped by the adversary in the victim’s network. 



When creating a YARA rule we try to be **more flexible as possible in order to catch the evolutions of the malicious codes** , but not too flexible to prevent false positives. 

Our YARA creation process is pretty simple, when we come around a new file, we sign it. Depending on the nature of the file, we can create different signatures. For example, if an LNK is using a new Lolbin technique, we will strictly sign the LNK as associated with a specific threat actor, and we will create a more generic rule for LNKs using this rule for pure hunting. 

The first rule to keep in mind when creating YARA rules for standard infection chains is to always **sign the content (malicious file) and the container (e.g. archive, email, droppers etc.)**. Each malicious atom, file, of the infection chain needs to be signed. 

### **Use of metadata**

The YARA format allows analysts to enrich their rules with metadata. Metadata are not implied in the process of matching files, but are essential when an analyst has to interpret and use the result of a rule. 

At Sekoia.io, **we have standardised these metadata to document the rule’s creation and the description of the matched file**. We have also standardised several extra metadata fields to automatically integrate the matched file to our platform and modelize its relationships into STIX. 

**Standard metadata** :

  * Rule ID (uuid) - Mandatory;
  * Rule description (description) - Mandatory;
  * Rule creation date (creation_date) - Mandatory;
  * Author’s trigram (author) - Mandatory;
  * External reference (reference) - Not mandatory;
  * Matched files hashes (hash) - Not mandatory;



**Extended metadata for STIX modelization - not mandatory:**

  * Intrusion set (intrusion_set)
  * Tool’s name (tool)
  * Malware’s name (malware)
  * Attack pattern (attack_patern)
  * Attack campaign (campaign)



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5866568d7e2b409bb6a_6a92a22cdc30711238320d07_6a2a7e96b97c48a61ea60ccc.webp)

### **Use of rule tags**

The YARA format also allows the integration of tags. These tags are simple keywords following the rule’s name. It allows malware researchers to sort their rules. **We use YARA rule tags at Sekoia.io to indicate to our automated process what to do with the results of our rules**. Two tags are mainly used by analysts:

  * TESTING: The rule is in testing, every day our automated process will create a "Pull Request" in our intelligence base and attribute the task to **manually** verify the outcome to a CTI analyst responsible for this rule. After a couple of weeks, if there are no false positives, the analyst can change the tag to “STABLE”.
  * STABLE: The rule is stable, and we are confident that it will not produce any false positives. Every day, the automated process will collect the results of this rule, enrich them and merge the indicators automatically to our TIP**without human verification**



The phase where a detection rule is in 'TESTING' mode is crucial, as this is when an analyst manually verifies that it does not produce any false positives. Through this rigorous process, we ensure that the indicators provided to our clients are accurate and relevant.

## Custom tooling

Using YARA solely through its command-line interface is not ideal for creating rules on a daily basis. To assist analysts in the rule creation process, we have developed two tools: Ariane and Gemini. We are also using AssemblyLine (AL4) to manage our malware zoo and automated malware analysis pipeline.

### Ariane

Ariane is an **ergonomic web interface designed to help our analysts to create YARA** , Suricata and Sigma rules. It comes as our main tool when dealing with YARA rules creation. Ariane has multiple features and provides a stable and central rule creation environment. By using this tool, **all analysts rely on the same set of libraries** when creating their rules, preventing some versioning conflicts. 

Ariane allows an analyst to work on malware samples in a secure environment, simply **by drag'n dropping the samples in the interface or by providing a list of hashes**. If one of the samples is not stored in our internal malware zoo, it is downloaded from public or private sources. The samples are stored in a temporary directory by the tool during the time of the analysis.

When a sample is downloaded, **Ariane checks inside the SEKOIA YARA repository if an existing YARA rule matches the sample**. This simple feature regularly saves us a lot of time, preventing us from duplicating the work of someone else in the team.

Depending on the types of the submitted files, **Ariane provides quick hints that can be used to create reliable YARA rules**. An example of YARA condition will be given to the analyst, explaining how this characteristic can be signed and some file magics and metadata are completed automatically.

Ariane is not LLM-driven and will not be, but it definitely is a great ergonomic tool to write our daily YARA rules, quickly and efficiently.

If the analyst is lost when looking at common characteristics between submitted files, we developed Gemini, another powerful tool which can be launched from Ariane to help the analysts.

### Gemini

Gemini is another simple tool, but very helpful when it comes to writing a YARA rule. Its goal is to find similarities in files submitted from Ariane or a CLI interface that can be used to create YARA rules. Gemini extracts metadata of the submitted files and, depending on the file type, i**t looks at similarities between files** and **extracts all relevant strings to compare them**. 

If the condition allows it, Gemini provides a simple interface to **check if a file's characteristic is very common or very specific by providing a VirusTotal search**. This helps analysts to know, for example, if an element (imphash, icon, section, embedded resource etc.) is really discriminant or is widely shared among malicious and legitimate software. 

At the end, **this tool provides to the analyst an HTML report, containing all useful information to create a reliable YARA rule with concrete examples** to write his own rule. 

![Gemini is a simple tool, but very helpful when it comes to writing a YARA rule. Its goal is to find similarities in files submitted from Ariane or a CLI interface that can be used to create YARA rules. Gemini extracts metadata of the submitted files and, depending on the file type, it looks at similarities between files and extracts all relevant strings to compare them.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5866568d7e2b409bb6d_6a92a22aadf0bb92a650d955_6a2a7e96b97c48a61ea60cc5.webp)

Gemini is a simple tool, but very helpful when it comes to writing a YARA rule. Its goal is to find similarities in files submitted from Ariane or a CLI interface that can be used to create YARA rules. Gemini extracts metadata of the submitted files and, depending on the file type, it looks at similarities between files and extracts all relevant strings to compare them.

Each time a new method of file structure correlation is discovered by an analyst, that method is implemented in Gemini to be automatically made available to every analyst. Aiming to be both engaging and educational, each method is documented in the final report generated by the tool and condition examples are provided.

### AssemblyLine

[AssemblyLine](https://cybercentrecanada.github.io/assemblyline4_docs/fr/) (AL4) is an open-source tool developed by the Canadian Cyber Centre, designed to help the detection and analysis of malicious software. This automated malware analysis pipeline uses state-of-the-art technologies to swiftly process and assess vast quantities of potentially harmful files. 

The Sekoia.io TDR team primarily uses AL4 to run configuration extractors from previously analysed malware families. Additionally, AL4 enables us to store samples in our malware zoo and to test new YARA rules against known samples, assisting analysts in identifying them or gaining further insights from general rules capable of recognizing packers and suspicious functions.

The integration of these tools has greatly enhanced our tracking capabilities. Ariane simplifies our work by creating a reliable rule template, and checking whether a rule already exists for the samples we are analysing, while Gemini finds all the specific characteristics of a malicious file with a single click, allowing us to use them in our rules. 

AssemblyLine further accelerates the automated analysis of malicious samples, allowing us to extract malware configuration and apply YARA rules to a wide range of potential threats. 

## Conclusion

YARA is today the keystone of malware signatures, as Sigma for log processing or Suricata for network flows. It allows threat researchers, reverse engineers, incident responders and analysts to discover and categorise malicious files, with rules templates from the simplest to the complex one when it comes to file structure and mathematical operations.

As Sekoia.io definitely loves using YARA and the community around**, we decided to share hundreds of our stable rules in our**[**Community Github repository**](https://github.com/SEKOIA-IO/Community/tree/main/yara_rules). This repository will be updated in the future with new rules and will also be available as a crowdsourced rules on VirusTotal. **Merry Christmas!**