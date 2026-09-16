# Advent of Configuration Extraction - Part 1: Kaiji Configuration

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/advent-of-configuration-extraction-part-1-pipeline-overview-first-steps-with-kaiji-configuration-unboxing
- **Date :** 2025-12-01

---

This article is the opening chapter of a four-part **_Advent of Configuration Extraction_** series. The series outlines the methodology we employ at Sekoia’s Threat Detection & Research (TDR) team to automate the extraction of malware configuration data, from initial analysis to the production of usable intelligence. Each post of the series focuses on a different scenario, such as analysing .NET malware or using Capstone for disassembly, to show how the approach applies across various families and techniques.

This first article introduces **Assemblyline** _,_ the analysis pipeline used by TDR and more specifically the configextractor service. To illustrate the workflow, we will use a simple case: the extraction of configuration data from **Kaiji,** an IoTbotnet malware. This article provides a straightforward demonstration of how the pipeline operates and how the configuration extraction service interacts with the rest of the system.

## How Assemblyline Organises Malware Analysis

[Assemblyline](https://github.com/CybercentreCanada/assemblyline) is an open-source malware analysis platform developed by the Canadian Centre for Cyber Security (CCCS). It structures analysis into a set of services, each responsible for a specific task in the processing chain. Among these services is the configuration extraction service, which identifies and processes configuration elements embedded within malware samples.

### Overview and Workflow

Assemblyline operates as a staged pipeline. Each submitted file is processed by one or more services, selected according to predefined rules and service metadata. Services are grouped by stage, which determines the order in which they run. This allows earlier services to prepare or transform the input before later ones act on it. For example, a decompression or unpacking service can run in an early stage to expand an archive or extract inner components. The resulting files are then passed to downstream services, such as the configuration extractor, which can analyse them in their final, usable form. This staged approach ensures that each service receives the most relevant data and that the overall workflow remains predictable and modular.

Assemblyline provides several APIs that allow external systems to submit files for analysis and control how they are processed. Submissions can use predefined analysis templates that specify which services should run and in what configuration. At TDR, files are collected through various channels, including sharing malware samples platform, honeypots and open directory monitoring, and are automatically submitted to Assemblyline through these APIs. The samples are analysed by various Assemblyline services, including the configuration extractor, which produces indicators of compromise that are ingested directly into our threat intelligence database, ensuring that newly identified activity is quickly reflected in detection and monitoring workflows.

![TDR malware analysis pipeline](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a53e2b0ef7af46bda0e0_6a92a17b11d85a04e9418acd_6a2a7fd3a3074ddacfe9def7.webp)

TDR malware analysis pipeline

 _TDR malware analysis pipeline_

### Automated Configuration Extraction Frameworks

The [**ConfigExtractor**](https://github.com/CybercentreCanada/assemblyline-service-configextractor) service in Assemblyline is dedicated to extracting malware configuration data such as C2 domains, IPs, URLs or cryptographic material from analysed samples. It leverages the open‑source [ConfigExtractor](https://github.com/CybercentreCanada/configextractor-py) Python library also maintained by CCCS. While the service supports several extraction frameworks such as MWCP, MACO, and CAPE, our extractors are built using MACO. To keep up with new malware families, the service includes an updater component that pulls extractors from a private Git repository, dynamically loads them, and installs their dependencies as needed. By default, the service also pulls some public Git repositories.

[**MACO**](https://github.com/CybercentreCanada/Maco/tree/main) (Malware Analysis Configuration Objects) is a framework designed to standardise the extraction of malware configuration data across different families and formats. It provides a structured approach to define parsers for specific malware, specifying which elements to extract and how to normalise them. Within Assemblyline, the ConfigExtractor service integrates MACO parsers to process samples. When a parser matches a given malware type via YARA rules, MACO extracts the relevant configuration fields and returns them in a consistent, structured format. This allows downstream systems to automatically consume the data, such as feeding indicators of compromise into threat intelligence platforms, without requiring custom handling for each malware family.

All scripts used for configuration extraction by the service are called modules and follow a structured workflow.

  * **Library Imports** : Load necessary libraries, including MACO, for parsing and structuring configuration data.
  * **Extractor Class** : Define a class that calls the extraction logic and includes a **YARA rule** to identify relevant samples. When a sample matches the YARA rule, the extractor triggers the dedicated parsing logic.
  * **Extraction Logic** : A set of dedicated functions or classes parse the sample and retrieve configuration fields. Placing this logic outside the main extractor class improves portability and allows reuse across different extractors or projects.
  * **Mapping to MACO Model** : Extracted data is converted into a structured MACO model and returned to Assemblyline.



## From Binary to C2: String-Based Configuration Extraction in Kaiji

**Kaiji** is a botnet malware written in the Go programming language, primarily targeting Linux systems and IoT devices. Originally, it spread via **SSH brute‑force attacks** , trying to guess credentials on exposed root accounts. Via our honeypots, we also observed Kaiji spreading through vulnerability exploitation, notably targeting [CVE‑2024‑7954](//nvd.nist.gov/vuln/detail/CVE-2024-7954) and [CVE‑2023‑1389](https://nvd.nist.gov/vuln/detail/CVE-2023-1389).

This evolution is particularly notable in the Chaos variant, a next‑generation successor analysed by [Lumen](https://blog.lumen.com/chaos-is-a-go-based-swiss-army-knife-of-malware/), which not only retains Kaiji’s DDoS capabilities and reverse‑shell modules but also incorporates built-in vulnerability exploitation to target known CVEs, along with additional functionalities such as cryptocurrency mining.

### Kaiji’s C2 Configuration Access Logic

To develop a configuration extractor, a preliminary manual analysis of multiple samples is required in order to identify the logic implemented by the malware to access and parse its configuration. For the present study, a static analysis was performed on sample _695909032488e34315857ef6da0c23eb1f6bba491c3c467a75e78228e0f289e4_. Using IDA, it becomes immediately apparent that the binary is not obfuscated: the symbols remain intact and provide insight into the program’s structure. Among these, the function **_main_connect_** stands out as the component responsible for establishing the connection with the command‑and‑control (C2) infrastructure.

The first instructions within this function reveal the mechanism used to obtain the C2 address. The malware loads a Base64‑encoded string and decodes it using the Go runtime’s **_(*Encoding).DecodeString_** method. The returned byte slice is subsequently converted into a Go string through **_runtime_slicebytetostring_**. The resulting string is then split using the delimiter "**_|(odk)/*-_** ", with the portion appearing before the delimiter corresponding to the **_C2:Port_** tuple used for outbound communication.

A broader examination of the sample’s embedded strings provides additional context: the Base64‑encoded configuration string is consistently preceded by the marker "**_use ParseCertificate_** ", a pattern that has been observed across several related samples.

### Automating the Configuration Extraction

Based on this analysis, it becomes possible to implement a Python‑based configuration extractor. For this purpose, the [FLOSS](https://github.com/mandiant/flare-floss) library is used and specifically its **_strings_** module, which provides the **_strings.extract_ascii_strings_** method for extracting all ASCII strings from a binary and returning them as a list. The extractor operates as follows:

  * It uses this method to build a complete list of strings extracted from the binary.
  * It iterates over this list and, using a regular expression, searches for and extracts the string prefixed with "**_use ParseCertificate_** ".
  * It decodes the retrieved Base64 value, splits it using the delimiter "**_|(odk)/*-_** ", and retains only the first element, which corresponds to the **_C2:Port_** tuple.



The tuple is then further processed to isolate the C2 address and the port. A validation step determines whether the C2 value is an IP address or a domain name, allowing the extractor to select the appropriate macro context (**_server_ip_** or **_server_domain_**).

[The extractor](https://github.com/SEKOIA-IO/Community/blob/main/Configuration_extractors/kaiji.py) contains two YARA rules designed to identify Ares as well as Chaos variant. Below the configuration extraction service output, as shown in Assemblyline, for the analysed sample.

![Configuration extraction service output in Assemblyline](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a53e2b0ef7af46bda0dd_6a92a17ac5553634ac943cf4_6a2a7fd3a3074ddacfe9def4.webp)

Configuration extraction service output in Assemblyline

 _Configuration extraction service output in Assemblyline_

## Final words

This article introduced the analysis pipeline used by TDR, with a particular focus on the methodology applied to extract malware configurations through Assemblyline. The process was illustrated using a first, relatively simple case: extracting the C2 information from the Kaiji variant malware, which relies primarily on parsing strings embedded in the binary. 

Despite its simplicity, this example provides a clear understanding of how the **ConfigExtractor** service operates, its YARA‑based signature logic, its extraction workflow, and the formatting of results into the MACO schema.

In Part 2, we will continue this exploration by examining configuration extraction for .NET‑based malware, using the case of QuasarRAT as a more advanced and structured example.