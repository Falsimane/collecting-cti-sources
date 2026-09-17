# Ransomware-driven data exfiltration: techniques and implications

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/ransomware-driven-data-exfiltration-techniques-and-implications
- **Date :** 2024-11-27

---

## Introduction

This report focuses on the **exfiltration techniques** leveraged by **ransomware and extortion groups** in lucrative campaigns. It aims to provide a comprehensive analysis of the techniques and tools used during the exfiltration phase and the **impacton affected organisations**. It also includes observations relating to the collection tactic, which we consider essential for a comprehensive understanding of exfiltration campaigns.

First, we will explore the **progressive adoption** of the exfiltration technique by ransomware and extortion groups and the **motivations** behind their campaigns. Second, we will analyse the different **categories of targeted data** during the exfiltration phase.

Next, we will focus on the **tools leveraged by lucrative intrusion sets** to gather valuable data from a victim’s environment. Finally, we will provide insights into **detecting different tools** and techniques associated with data exfiltration.

While this report focuses on opportunistic, ransomware-driven intrusion sets and campaigns, it is worth noting that a wide range of distinct financially motivated intrusion sets employ exfiltration tactics. This includes operators of infostealers, remote access trojans (RATs), spyware, credit card skimmers, backdoors, and other types of malicious software. Moreover, state-sponsored actors also largely leverage the exfiltration tactic in information-gathering campaigns. While we may reference these categories of actors in our analysis, they are not the primary focus of our study.

Our research involved both open-source reporting and in-house investigations.

## Executive summary

  * **Data exfiltration** became a **critical element** in ransomware campaigns, in line with the widespread adoption of the double extortion technique between 2019 and 2024. 


  * Attackers**leverage stolen data** to maximise**financial and reputational impact** through public exposure on dedicated leak sites, while also potentially selling the data to other threat actors or using it for additional extortion and subsequent attacks. 


  * These motivations, along with factors like reduced effort and the circumvention of encryption-related challenges, led some ransomware groups to **focus partially or exclusively on data exfiltration** for extortion, without encrypting files.


  * Besides lucrative ransomware and extortion groups, exfiltration is also**leveraged by state-sponsored intrusion sets** during ransomware operations, likely to misdirect attribution, conduct covert intelligence gathering campaigns, and generate revenue.


  * Over the past five years, ransomware operators increasingly refined their extortion techniques to **maximise leverage for double extortion**. They adopted a more strategic approach by **pre-qualifying and triaging collected data**. This involves **targeted searches** aimed at extracting high-value, sensitive files, such as financial information, personal and medical records, classified documents, IT-related and network data and other highly sensitive information.


  * Ransomware groups use a combination of**custom and publicly available tools** to facilitate data exfiltration. This is according to their specific features and their intended use in exfiltration campaigns: **enumeration** , **compression, uploading** , etc.


  * Advanced intrusion sets increasingly develop and use **custom exfiltration tools** to enhance efficiency, precision, and stealth. Ransomware operators occasionally leverage **commodity malware** , including infostealers and Malware-as-a-Service (MaaS) tools, to streamline the data exfiltration processes. However, their use remains limited compared to publicly available alternatives.


  * **Legitimate and publicly available tools** are widely leveraged to facilitate stealthy and cost-effective data exfiltration while blending in with legitimate activities to evade detection.


  * To mitigate the impact of data theft and ransomware deployment, companies should prioritise **early detection** of data exfiltration attempts through a **multimethod strategy** , including monitoring suspicious behaviour, file access patterns, and the use of known exfiltration tools, while focusing on critical files and directories to detect potential data movement.



![Tools most used by main ransomware operations to facilitate exfiltration in lucrative campaings, from 2022 to November 2024, based on open-source reporting.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5876568d7e2b409bbe4_6a92a22edb65986262add648_6a2a7e8c560f30ed64ac1528.webp)

Tools most used by main ransomware operations to facilitate exfiltration in lucrative campaings, from 2022 to November 2024, based on open-source reporting.

‍

## Read the full version of this article in PDF

The full version of this article is [available in PDF format](https://0H3WGygmjL.flowdrivecdn.com/VxyGLCRkf4l0CnbpSWdeW). Feel free to read it and share it with your network.

‍