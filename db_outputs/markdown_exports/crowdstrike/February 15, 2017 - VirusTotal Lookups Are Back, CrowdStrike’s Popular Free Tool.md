# VirusTotal Lookups Are Back, CrowdStrike’s Popular Free Tool

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/virustotal-lookups-are-back-in-crowdinspect-crowdstrikes-popular-free-tool/
- **Date :** February 15, 2017

---

# VirusTotal Lookups Are Back in CrowdInspect, CrowdStrike’s Popular Free Tool

February 15, 2017

• [ Robin](/en-us/blog/author.robin/ "Posts by Robin") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


CrowdStrike _CrowdInspect_ version 1.5.0.0 has arrived. Many of you are 

familiar with CrowdInspect, a simple-to-use and understand Windows application that lists processes running on your computer, along with details of any network connections those processes make. Additional useful information includes reputation of the domain the process is connected to from [WoT](https://www.mywot.com)

; whether the process is known to be malicious ([Team Cymru Malware Hash Registry](https://www.team-cymru.org)); and virus details from [VirusTotal](https://www.virustotal.com). CrowdInspect was the first tool of its kind to offer such services. Due to the popularity of CrowdInspect _,_ we eventually were forced to remove the VirusTotal feature last year, since we frequently exceeded our allotted query quota. The tool continued to operate without this functionality, but it was sorely missed by our users. Today we can announce that with this new version, VirusTotal lookups are back! The kind folks at VirusTotal have provided us with unrestricted API access via direct connection to their servers. We would like to thank them very much for this ability that now provides you with free, fast virus information from VirusTotal’s vast database. The new VirusTotal API only provides an overall score for the file in question, not the detailed list of AV vendors that we had provided previously. For the majority of users, this should suffice. 

However, if you wish to see all of the details about the file, we provide a link in the details window, which will open your web browser to the associated page at[ www.virustotal.com](http://www.virustotal.com) where you will find every detail. (To access the page, right click an item in the list and select “ _View VT Test Results_ ,” or click the toolbar icon.) In addition to the new built-in direct VirusTotal lookup feature, we have added the ability to provide your own personal key to query the public API. This provides the same details as the old version of CrowdInspect, however, queries are rate-limited by VirusTotal to four per minute, which means 

population of the VT column in the tool will take longer. For this reason, we recommend that you stay with the built-in custom API option. By default, when an unknown file is encountered, the built-in custom VirusTotal option uploads the file to their servers and adds it to their collection for analysis. Options to control this behavior can be found in the _About_ section of the CrowdInspect tool. Access to it is presented after accepting the EULA on first start, and it can be reached again by clicking the _About_ toolbar icon when the application is running. ![crowdinspect](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2017/02/CrowdInspect.png) When switching between the two VirusTotal options, only newly appearing processes will reflect the change in results. As previously mentioned, the built-in custom API only provides overall scores, whereas the personal API key (using the VT public API) will provide a list of how each individual AV vendor marked the file. It is recommended that you restart the application to provide the level of detail you require for all processes. We hope you enjoy the tool and its new features. It can be downloaded from

our [CrowdInspect](/resources/community-tools/crowdinspect-tool.html) Page. Learn more about CrowdStrike Falcon®’s powerful endpoint protection platform and the benefits of replacing your legacy AV solution -- register for

our

webcast today: 

[How to Replace Your Legacy Antivirus Solution with CrowdStrike](/en-us/resources/crowdcasts/time-come-replace-antivirus-solution/).

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)