# CrowdStrike Falcon® Platform Identifies Supply Chain Attack via a Trojanized Comm100 Chat Installer

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/new-supply-chain-attack-leverages-comm100-chat-installer/
- **Date :** September 30, 2022

---

# CrowdStrike Falcon® Platform Identifies Supply Chain Attack via a Trojanized Comm100 Chat Installer

September 30, 2022

• [ CrowdStrike Intelligence Team](/en-us/blog/author.crowdstrike-intelligence-team/ "Posts by CrowdStrike Intelligence Team") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")• [From The Front Lines](/en-us/blog/category.from-the-front-lines/ "From The Front Lines")


  * The CrowdStrike Falcon® platform, leveraging a combination of advanced machine learning and artificial intelligence, identified a new supply chain attack during the installation of a chat-based customer engagement platform.
  * The CrowdStrike® Falcon OverWatch™, Falcon Complete™ and CrowdStrike Intelligence teams confirmed that the supply chain attack involved a trojanized installer for the Comm100 Live Chat application being deployed.
  * Malware was delivered via a signed Comm100 installer that could be downloaded from the company’s website as recently as the morning of September 29, 2022.
  * CrowdStrike Intelligence assesses with moderate confidence that the actor responsible for this activity likely has a China nexus.
  * Based on CrowdStrike’s responsible disclosure, Comm100 has released an updated installer (10.0.9).
  * The Falcon platform helps protect organizations of all sizes from sophisticated breaches, including supply chain attacks of this nature.



The market-leading CrowdStrike Falcon® platform, applying a combination of advanced machine learning (ML), artificial intelligence (AI) and deep analytics across the trillions of security events captured in the CrowdStrike Security Cloud, has identified a new supply chain attack pattern during the installation of a chat based customer engagement platform.

The Falcon platform helps to protect organizations of all sizes from sophisticated breaches, including supply chain attacks of this nature, by using a defense-in-depth approach, applying advanced AI to the vast telemetry of the CrowdStrike Security Cloud to power detections and provide real-time mitigation.

Leveraging insights from the Falcon platform, the CrowdStrike® Falcon OverWatch™, CrowdStrike Falcon® Complete™ and CrowdStrike Intelligence teams confirmed that the supply chain attack involved a trojanized installer for the Comm100 Live Chat application. This attack occurred from at least September 27, 2022 through the morning of September 29, 2022. The trojanized file was identified at organizations in the industrial, healthcare, technology, manufacturing, insurance and telecommunications sectors in North America and Europe. CrowdStrike Intelligence assesses with moderate confidence that the actor responsible for this attack likely has a China nexus.

## CrowdStrike Detection and Protection

The [Falcon platform](/en-us/falcon-platform/) helps to protect its customers from a supply chain attack of this nature by detecting the suspicious activity of the trojanized installer and blocking the second-stage activities using ML and multiple behavior-based indicators of attack (IOAs). The Falcon platform takes a defense in-depth approach to protecting customers by leveraging incoming telemetry to power detections and provide real-time mitigation for customers. In addition, the Falcon OverWatch team of elite threat hunters relentlessly search to detect and disrupt [ongoing exploitation attempts](/en-us/services/experienced-a-breach/). As can be seen in Figure 1, CrowdStrike's ML model identifies the weaponized file when it is written to disk.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/09/Fig1.png)](/content/dam/crowdstrike/www/en-us/wp/2022/09/Fig1.png)Figure 1. CrowdStrike’s ML model identifies and blocks the impacted file (Click to enlarge)

In Figure 2, you can see how the Falcon platform generates multiple behavior-based IOAs covering second-stage activity.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/09/Fig2.png)](/content/dam/crowdstrike/www/en-us/wp/2022/09/Fig2.png)Figure 2. Detection of post-compromise activity if applicable (Click to enlarge)

## Attack Details

Malware is delivered via a signed Comm100 installer that was downloadable from the company’s website. The installer was signed on September 26, 2022 at 14:54:00 UTC using a valid Comm100 Network Corporation certificate. CrowdStrike Intelligence can confirm that the Microsoft Windows 7+ desktop agent hosted at https<:>//dash11.comm100<.>io/livechat/electron/10000/Comm100LiveChat-Setup-win.exe that was available until the morning of September 29 was a trojanized installer. Comm100 has since released an updated installer (10.0.9).

This installer (SHA256 hash: `ac5c0823d623a7999f0db345611084e0a494770c3d6dd5feeba4199deee82b86`) is an Electron application that contains a JavaScript (JS) backdoor within the file main.js of the embedded Asar archive.

The backdoor downloads and executes a second-stage script from URL http<:>//api.amazonawsreplay<.>com/livehelp/collect.

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/09/Screen-Shot-2022-09-30-at-7.43.50-AM.png)Figure 3. Initial JS Backdoor in main.js

The second-stage script consists of obfuscated JS containing a backdoor that gathers host information before providing the actor with remote shell functionality by spawning a new instance of cmd.exe.

The script also uses the command-and-control (C2) domain api.amazonawsreplay<.>com. As part of likely follow-on activity, the actor installed additional malicious files on the affected host, including a malicious loader DLL named MidlrtMd.dll executed by a legitimate copy of a Microsoft Metadata Merge Utility (mdmerge.exe) binary via DLL search-order hijacking. The loader DLL decrypts a payload file named license using a customized variant of RC4 encryption with the hard-coded key U9ELetx8eMR8pd5koFamoOyuf9tTRTPG. The decrypted payload consists of shellcode that is executed in memory and injects an embedded payload into a new instance of notepad.exe. The injected payload connects to the malicious C2 domain api.microsoftfileapis<.>com, which resolved to the IP address 8.219.167<.>156 at the time of the incident. Based on CrowdStrike’s responsible disclosure, Comm100 has released an updated installer. Impacted Comm100 customers can download the latest exe version (10.0.9). Comm100 further indicated it was performing a root cause analysis to obtain additional information.

**If you are a Comm100 customer without CrowdStrike and are unsure if you've been impacted, contact**[**CrowdStrike Services**](/en-us/services/experienced-a-breach/)**or**[**CrowdStrike Sales**](/en-us/contact-us/)**.**

## Assessment

The payload delivered in this supply chain attack differs from payloads identified in previous incidents related to the same actor, targeting online gambling entities in Asia. Additionally, the recent activity differs from activity targeting online gambling in both the target scope and the supply chain attack mechanism delivering a trojanized app via Comm100’s website.

Despite these differences, CrowdStrike Intelligence assesses that the actor responsible for previously identified online gambling targeting is also likely responsible for these recent incidents. This assessment is made with moderate confidence based on the following factors:

  * The use of chat software to deliver malware

The use of the Microsoft Metadata Merge Utility binary to load a malicious DLL named MidlrtMd.dll

  * C2 domain-naming convention using Microsoft and Amazon-themed domains along with api. subdomains

  * C2 domains hosted on Alibaba infrastructure




Furthermore, CrowdStrike Intelligence assesses with moderate confidence that this actor likely has a China nexus. This assessment is based on the presence of Chinese-language comments in the malware, aforementioned tactics, techniques and procedures (TTPs), and the connection to the targeting of online gambling entities in East and Southeast Asia — a previously established area of focus for China-nexus targeted intrusion actors. CrowdStrike Intelligence customers have access to additional [reporting](/en-us/resources/data-sheets/crowdstrike-falcon-adversary-intelligence-premium/) related to this actor.

## Hunting in CrowdStrike Falcon®

Falcon will detect and prevent the indicators and behaviors included in this article. The indicators can be retroactively searched back one year — regardless of Falcon retention period — by leveraging Falcon Indicator Graph: [US-1](https://falcon.crowdstrike.com/intelligence/graph?indicators=hash%3A%27ac5c0823d623a7999f0db345611084e0a494770c3d6dd5feeba4199deee82b86%27%2Cdomain%3A%27amazonawsreplay.com%27%2Cdomain%3A%27api.amazonawsreplay.com%27%2Cdomain%3A%27comm100.io%27%2Cdomain%3A%27dash11.comm100.io%27%2Cdomain%3A%27domainapi.microsoftfileapis.com%27%2Cdomain%3A%27microsoftfileapis.com%27%2Cip%3A%278.219.167.156%27) | [US-2](https://falcon.us-2.crowdstrike.com/intelligence/graph?indicators=hash%3A%27ac5c0823d623a7999f0db345611084e0a494770c3d6dd5feeba4199deee82b86%27%2Cdomain%3A%27amazonawsreplay.com%27%2Cdomain%3A%27api.amazonawsreplay.com%27%2Cdomain%3A%27comm100.io%27%2Cdomain%3A%27dash11.comm100.io%27%2Cdomain%3A%27domainapi.microsoftfileapis.com%27%2Cdomain%3A%27microsoftfileapis.com%27%2Cip%3A%278.219.167.156%27) | [EU](https://falcon.eu-1.crowdstrike.com/intelligence/graph?indicators=hash%3A%27ac5c0823d623a7999f0db345611084e0a494770c3d6dd5feeba4199deee82b86%27%2Cdomain%3A%27amazonawsreplay.com%27%2Cdomain%3A%27api.amazonawsreplay.com%27%2Cdomain%3A%27comm100.io%27%2Cdomain%3A%27dash11.comm100.io%27%2Cdomain%3A%27domainapi.microsoftfileapis.com%27%2Cdomain%3A%27microsoftfileapis.com%27%2Cip%3A%278.219.167.156%27) | [Gov](https://falcon.laggar.gcw.crowdstrike.com/intelligence/graph?indicators=hash%3A%27ac5c0823d623a7999f0db345611084e0a494770c3d6dd5feeba4199deee82b86%27%2Cdomain%3A%27amazonawsreplay.com%27%2Cdomain%3A%27api.amazonawsreplay.com%27%2Cdomain%3A%27comm100.io%27%2Cdomain%3A%27dash11.comm100.io%27%2Cdomain%3A%27domainapi.microsoftfileapis.com%27%2Cdomain%3A%27microsoftfileapis.com%27%2Cip%3A%278.219.167.156%27). All software signed with Comm100’s code-signing certificate (`d65cdc6b3a6738951f59d4ec8cc7d42f330c6d59`) can be scoped using the following: **Event Search** `index=json ExternalApiType=Event_ModuleSummaryInfoEvent SubjectCertThumbprint=d65cdc6b3a6738951f59d4ec8cc7d42f330c6d59 | stats values(AuthorityKeyIdentifier) as AuthorityKeyIdentifier, values(SubjectCN) as SubjectCN, values(SubjectDN) as SubjectDN, values(SubjectCertThumbprint) as SubjectCertThumbprint by SHA256HashData | lookup local=true appinfo.csv SHA256HashData OUTPUT FileName, ProductName, ProductVersion | fillnull value="Unknown" FileName, ProductName, ProductVersion` ******Falcon LogScale** `ExternalApiType=Event_ModuleSummaryInfoEvent | SubjectCertThumbprint = d65cdc6b3a6738951f59d4ec8cc7d42f330c6d59 | groupby(, function=stats(), limit=max)`

### Profiling Comm100 DNS Activity

The Comm100 Chat binary can be profiled to look for anomalous DNS requests. The following queries can be used to determine what Comm100 Chat.exe binary regularly resolves for domain names: **Event Search** `(event_platform=win event_simpleName=ProcessRollup2 FileName="Comm100 Live Chat.exe") OR (event_platform=win event_simpleName=DnsRequest) | eval falconPID=coalesce(TargetProcessId_decimal, ContextProcessId_decimal) | stats dc(event_simpleName) as eventCount, values(ParentBaseFileName) as parentFile, values(FileName) as fileName, values(DomainName) as domainNames by cid, aid, falconPID | where eventCount > 1 | stats values(domainNames) as domainNames by fileName` ******Falcon LogScale** `#event_simpleName=ProcessRollup2 ImageFileName=/\\Comm100\sLive\sChat\.exe/i | join({#event_simpleName=DnsRequest}, key=, field=, include=) | ImageFileName=/.*\\(?<fileName>.*\..*)/ | table() | groupBy()` Once baselined, a Custom IOA can be created to detect or prevent variances from expected behavior: `Rule Type: Domain Name (Windows)` `Action To Take: <choose>` `Severity: <choose>` `GRANDPARENT IMAGE FILENAME: .*` `GRANDPARENT COMMAND LINE: .*` `PARENT IMAGE FILENAME: .*` `PARENT COMMAND LINE: .*` `IMAGE FILENAME: .*\\Comm100\sLive\sChat\.exe$` `COMMAND LINE: .*` `DOMAIN NAME: .*` `<select add exclusion>` `DOMAIN NAME – EXCLUDE: .*\.comm100\.io` Be sure to add additional domain names you **DO NOT** want to alert on in the “DOMAIN NAME - EXCLUDE” section (e.g., your SSO provider, if configured). Enable the Custom IOA and assign it to the desired prevention policy.

**Unsure if you've been impacted?**  
---  
If you are a Comm100 customer without CrowdStrike and are unsure if you've been impacted, contact [CrowdStrike's Services team](/en-us/services/experienced-a-breach/) now or [start a free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html).  
  
## CrowdStrike Intelligence Confidence Assessment

**High Confidence** : Judgments are based on high-quality information from multiple sources. High confidence in the quality and quantity of source information supporting a judgment does not imply that that assessment is an absolute certainty or fact. The judgment still has a marginal probability of being inaccurate. **Moderate Confidence** : Judgments are based on information that is credibly sourced and plausible, but not of sufficient quantity or corroborated sufficiently to warrant a higher level of confidence. This level of confidence is used to express that judgments carry an increased probability of being incorrect until more information is available or corroborated. **Low Confidence** : Judgments are made where the credibility of the source is uncertain, the information is too fragmented or poorly corroborated enough to make solid analytic inferences, or the reliability of the source is untested. Further information is needed for corroboration of the information or to fill known intelligence gaps.

## Indicators

**SHA256 Hash**| **Comm100 File Version**  
---|---  
6f0fae95f5637710d1464b42ba49f9533443181262f78805d3ff13bea3b8fd45 (CrowdStrike is aware this file contains the same backdoor, but it has not been observed in the wild)| 10.0.72  
ac5c0823d623a7999f0db345611084e0a494770c3d6dd5feeba4199deee82b86| 10.0.8  
  
Table 1. Trojanized Comm100 application executables

**Filename**| **SHA256 Hash**| **Description**  
---|---|---  
C:\ProgramData\Cisco Core\CoreConnect.exe| ac9f2ae9de5126691b9391c990f9d4f1c25afa 912fbfda2d4abfe9f9057bdd8c| Legitimate mdmerge.exe executable  
C:\ProgramData\Cisco Core\MidlrtMd.dll| 6194d57fc3bc35acf9365b764338adefacecfa cf5955b87ad6a5b753fb6081f8| Malicious loader DLL  
C:\ProgramData\Cisco Core\license| c930a28878a5dd49f7c8856473ff452ddbdab 8099acd6900047d9b3c6e88edca| Encrypted payload configured with C2 domain api.microsoftfileapis<.>com  
  
Table 2. Observed implant likely deployed by the actor

**Network Indicators**| **Description**  
---|---  
http<:>//api.amazonawsreplay<.>com/collect_log| JS backdoor logging URL  
http<:>//api.amazonawsreplay<.>com| JS backdoor C2  
http<:>//api.amazonawsreplay<.>com/livehelp/init| JS backdoor C2  
http<:>//api.microsoftfileapis<.>com| Encrypted payload C2 host  
https<:>//selfhelp<.>windowstearns<.>com| Related encrypted payload C2 host  
http<:>//api.amazonawsreplay<.>com/livehelp/collect| Staging URL for JS backdoor  
  
Table 3. Network indicators related to activity described in this alert

**Command Line**| **Description**  
---|---  
reg query \"hklm\\\SOFTWARE\\\Microsoft\\\Windows NT\\\CurrentVersion\" /v ProductId| Used in the JS backdoor to compute a MD5 victim hash  
  
Table 4. Command-line indicators related to activity described in this alert

#### Additional Resources

  * _[Request a free trial](/en-us/free-trial-guide/) of the industry-leading CrowdStrike Falcon® platform.

_
  * _Learn more about how the CrowdStrike Falcon® platform[ protects customers from sophisticated intrusions like supply chain attacks](/en-us/falcon-platform/).

_
  * _Watch an introductory video on the CrowdStrike Falcon® console and register for an on-demand demo of the market-leading CrowdStrike Falcon® platform in action.

_
  * _Request a free CrowdStrike Intelligence threat briefing and learn how to stop adversaries targeting your organization._
  * _Learn more about the adversaries CrowdStrike tracks by exploring the Adversary Universe — and experience it for yourself during the CrowdStrike Adversary Universe World Tour 2022!_
  * _To stay ahead of today’s adversaries, read the CrowdStrike 2022 Global Threat Report._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)