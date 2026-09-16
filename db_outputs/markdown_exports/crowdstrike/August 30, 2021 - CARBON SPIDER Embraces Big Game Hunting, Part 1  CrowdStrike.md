# CARBON SPIDER Embraces Big Game Hunting, Part 1 | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/carbon-spider-embraces-big-game-hunting-part-1/
- **Date :** August 30, 2021

---

# CARBON SPIDER Embraces Big Game Hunting, Part 1

August 30, 2021

• [ Eric Loui - Josh Reynolds](/en-us/blog/author.eric-loui---josh-reynolds/ "Posts by Eric Loui - Josh Reynolds") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Throughout 2020, [CARBON SPIDER](https://adversary.crowdstrike.com/en-US/adversary/carbon-spider.html) dramatically overhauled their operations. In April 2020, the adversary abruptly shifted from narrow campaigns focused entirely on companies operating point-of-sale (POS) devices to broad, indiscriminate operations that attempted to infect very many victims across all sectors. The goal of these campaigns was to conduct [big game hunting (BGH)](https://www.crowdstrike.com/cybersecurity-101/cyber-big-game-hunting/) operations using PINCHY SPIDER’s _REvil_ ransomware.

CARBON SPIDER deepened their commitment to BGH in August 2020 by using their own ransomware, _Darkside_. In November 2020, the adversary took another step into the world of BGH by establishing a [ransomware-as-a-service (RaaS)](/en-us/cybersecurity-101/ransomware/ransomware-as-a-service-raas/) affiliate program for _Darkside_ , allowing other actors to use the ransomware while paying CARBON SPIDER a portion of the ransom received.

Part One of this two-part blog series details how CrowdStrike Intelligence attributed _Darkside_ to CARBON SPIDER. Part Two will look at CARBON SPIDER’s re-emergence after the Colonial Pipeline attack, which led to the shutdown of _Darkside_ RaaS and the creation of _BlackMatter_ RaaS.

## Background

CARBON SPIDER, commonly referred to as FIN7 and active since 2013, is one of the oldest continuously operating eCrime groups. Between 2015 and 2020, the adversary conducted low-volume campaigns targeting company POS devices, primarily in the hospitality sector. These campaigns featured a variety of malware, including the [_Sekur_ (_Carbanak_) RAT, _VB Flash_ , _Bateleur_ and _Harpy_ (_GRIFFON_)](/en-us/blog/arrests-put-new-focus-on-carbon-spider-adversary-group/). Using POS malware, including _PILLOWMINT_ , the adversary harvested credit card track data and sold this data on criminal forums such as Joker’s Stash.

## April 2020: Target Scope Widens

In April 2020, CARBON SPIDER abruptly shifted from narrow campaigns focused entirely on companies operating POS devices to broad, indiscriminate operations that attempted to infect large numbers of victims across all sectors. The first of these occurred on April 14, 2020, when the adversary likely compromised a legitimate email distribution service to conduct a broad spam campaign targeting thousands of recipients across numerous verticals.

This campaign used malicious links that led to a ZIP archive hosted on `https<:>//colahasch<.>com/portal/app/CommerceNetwork/ view/9b25068f2941618fb9b08d6d089a47faae552c93f` The ZIP archive contained a _Leo VBS_ , which refers to a family of obfuscated scripts that download and execute a remote payload. The _Leo VBS_ performs an HTTP GET request to `https<:>//alphalanding<.>com/successfully/warranty.eml?uid=` and writes a _JSS Loader_ binary to `%TEMP%\PaintHelper.exe`. _JSS Loader_ , which has both .NET and C++ versions, has multiple capabilities, including the ability to load additional executables, PowerShell (PS) and JavaScript (JS) files. The observed JSS Loader infection led to the download and execution of a setup VBScript from `https<:>//petshopbook<.>com`. This script installs a custom _Sekur_ PS stager to `%LOCALAPPDATA%\Microsoft\WindowsDefender\ClearTemp.ps1` and establishes persistence for this stager with a second VBS that is launched by a scheduled task. Since this campaign, CARBON SPIDER has maintained an opportunistic target scope, using phishing attachments and links to deliver _Harpy, Leo VBS, JSS Loader, Domenus VBS_ and _Domenus JS_. _Domenus VBS_ and _JS_ are backdoors (written in VBS and JS, respectively) that enumerate a variety of system information, capture screenshots and browser history, and can download secondary payloads from a command-and-control (C2) server. Secondary payloads can include JS, Portable Executables (PEs), DLLs and PS scripts.

CrowdStrike Intelligence observed numerous _Domenus VBS/JS_ phishing campaigns that made use of compromised and legitimate services to host _Domenus_ toolchain payloads, including compromised WordPress installations, compromised SharePoint services, compromised web servers and Google Docs.

## REvil Ransomware Campaigns

On April 28, 2020, CrowdStrike Intelligence observed a _Domenus VBS_ distribution campaign that used a spear-phishing email containing a Google Docs link. The resulting Google Docs page contained a second link that, when clicked, directed the user to `https<:>//chauvinistable<.>com/perfsecure`, ultimately redirecting to a compromised SharePoint site. Here, the victim encountered a ZIP file containing a _Domenus VBS_ file that, once opened, downloaded and executed _Harpy_ from `https<:>//electroncador<.>com/info`.

The redirect URL provided from the Google Docs page `https<:>//chauvinistable<.>com/perfsecure` was hosted on the same IP address (`185.163.45<.>249`) resolving to a domain used by multiple _Cobalt Strike_ samples sharing key configuration metadata with _Cobalt Strike_ samples used in several _REvil_ incidents. These _Cobalt Strike_ samples were also observed in tandem with the custom PowerShell stager for _Sekur_. Separate reporting by Symantec further indicated that similar _Cobalt Strike_ samples were used in campaigns delivering _REvil_. Based on these multiple overlaps, CrowdStrike Intelligence assesses with moderate confidence that CARBON SPIDER was responsible for certain _REvil_ campaigns, likely stemming from _JSS Loader_ or _Domenus VBS/JS_ infections.

## Darkside Ransomware Campaigns + RaaS

On July 1, 2020, CARBON SPIDER sent a phishing email with the subject “Notification: Package Status Fail.” The email purports to be from a customer who received an email from the U.S.-based delivery company UPS (Figures 1 and 2). The message body attempts to impersonate a UPS notification, but contains several grammar errors and non-idiomatic terms (e.g., “waybill”).

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/08/Picture1-8.png)Figure 1. CARBON SPIDER phishing email

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/08/Picture2-3.png)Figure 2. CARBON SPIDER phishing email (continued)

The link “Check” led to a Google Docs page, which contained a link that redirected to a ZIP file. The ZIP file was hosted on a likely compromised SharePoint account and contained _Domenus VBS_ , which downloads _Harpy_ from `https<:>//fashionableeder<.>com/info`. At one victim, CARBON SPIDER subsequently deployed the aforementioned custom PS _Sekur_ stager and profiled the Active Directory environment using the utility _ADFind_.

In this incident, CARBON SPIDER also used the _KillACK_ PS backdoor, executing the malware using both PowerShell and PowerShell ISE. _KillACK_ sends host information to a C2 server (in this case, `againcome<.>com` or `besaintegration<.>com`) and executes provided PS script blocks. Multiple _KillACK_ modules have been observed by CrowdStrike Intelligence, including modules for conducting self-propagation and AMSI hot-patching, as well as for executing _Cobalt Strike_ stagers and enumerating network information. On Aug. 9, 2020, CARBON SPIDER attempted to run the _Darkside_ ransomware with the filename `sleep.exe`. This filename may reflect an attempt to masquerade as the legitimate Windows executable with the same name. Following this incident, CrowdStrike Intelligence identified numerous similar _Darkside_ campaigns featuring distinctive CARBON SPIDER tooling, including _Harpy, Domenus VBS/JS, KillACK_ and _Sekur_. The adversary also used the commodity _Cobalt Strike_ framework and _Plink_ tunneling tool in many of these campaigns. After achieving initial access, the adversary consistently seeks to harvest valid administrative credentials to enable lateral movement and uses a variety of tools and techniques for this purpose, including CrackMapExec, Kerberoasting, Mimikatz, PowerSploit and SessionGopher. In one incident, the adversary likely exploited the [ZeroLogon vulnerability (CVE-2020-1472)](/en-us/blog/new-zerologon-dashboard-offers-greater-visibility-into-cve-2020-1472/) against a domain controller. Using valid credentials, CARBON SPIDER moves laterally through victim environments using RDP and occasionally SSH. The adversary typically uses PS to run _Cobalt Strike_ but occasionally writes _Cobalt Strike_ stagers or _KillACK_ backdoors to disk. Occasionally, CARBON SPIDER has deployed the legitimate _GoToAssist_ or _TightVNC_ tools to provide redundant control of hosts. Similar to many other ransomware operators, CARBON SPIDER not only encrypted victim files using _Darkside_ , but also exfiltrated data for publication on a dedicated leak site (DLS) hosted on Tor. For exfiltration, CARBON SPIDER primarily leveraged the _MEGASync_ client for hosting provider MEGA but also employed _GoToAssist_. Further, CARBON SPIDER frequently conducted _hypervisor jackpotting_ by [encrypting ESXi servers using a version of _Darkside_ specifically designed for ESXi](/en-us/blog/carbon-spider-sprite-spider-target-esxi-servers-with-ransomware/). On Nov. 10, 2020, CARBON SPIDER announced the establishment of the _Darkside_ RaaS affiliate program. The announcement, posted on two major Russian-language forums, states that the operators of _Darkside_ are looking for Russian-speaking affiliates who understand how to recognize and delete backups. On Nov. 11, 2020, CARBON SPIDER added a new message to their DLS concerning the new affiliate program. This announcement claims “we created the perfect product for ourselves,” indicating that _Darkside_ was originally exclusive to one group and not shared. CrowdStrike Intelligence assesses that _Darkside_ ransomware campaigns prior to this announcement were likely conducted by CARBON SPIDER, and that CARBON SPIDER was responsible for creating _Darkside_ and introducing the RaaS affiliate program. This assessment carries moderate confidence, based on:

  * Multiple separate _Darkside_ incidents attributable to CARBON SPIDER
  * Low overall volume of _Darkside_ campaigns
  * The Nov. 11, 2020 announcement described above indicating _Darkside_ was initially exclusive to one group
  * The Oct. 10, 2020 press release indicating _Darkside_ is operated by a single group



Subsequent to the creation of the _Darkside_ RaaS program, CrowdStrike Intelligence continued to observe some _Darkside_ campaigns almost certainly conducted by CARBON SPIDER — in addition to other campaigns operated by affiliates — featuring divergent tooling and TTPs. CARBON SPIDER’s campaigns featured the malware discussed above, in addition to heavy use of the _Cobalt Strike_ post-exploitation framework.

## Conclusion

CARBON SPIDER’s shift from POS malware to BGH ransomware attacks exemplifies a broader trend in the eCrime landscape. Numerous adversaries that previously relied on banking trojans (e.g., [INDRIK SPIDER](/en-us/blog/hades-ransomware-successor-to-indrik-spiders-wastedlocker/)) or POS compromises (e.g., GRACEFUL SPIDER) have almost entirely reinvented themselves to focus on [ransomware](/en-us/cybersecurity-101/ransomware/), reflecting how lucrative BGH campaigns are. Until the economics of cybercrime fundamentally change, it is unlikely these adversaries will alter their behavior.

## Indicators of Compromise

**Type**| **Value**  
---|---  
 _Leo VBS_| `8279ce0eb52a9f5b5ab02322d1bb7cc9cb5b242b7359c3d4d754687069fcb7b8`  
 _JSS Loader_| `98fe1d06e4c67a5a5666dd01d11e7342afc6f1c7b007c2ddbfc13779bcc51317`  
 _Sekur_ stager| `bbd1c244c0861c0048d5eccecbb6dee1a6f57764c7d0028a7cbfd87c93d3166b`  
 _Domenus VBS_| `00fb044af4c92bd06699aaf1d83c4e6805e96f501f84ad1d2ff0885384aa3ea1`  
 _Domenus JS_| `5b7115ab612dcff8e84b2258082a6e7c71b5d52237a4ae8a6642baeb36c2aa48`  
 _KillACK_| `4f5eefe93ac2fa5f92c6bd245fff1400f6a61aeee07076c92c66d82f94dc45c3`  
  
Table 1. Exemplar SHA256 hashes of CARBON SPIDER malware

## Explanation of Confidence Rating

  * **High Confidence:**

Judgments are based on high-quality information from multiple sources.

High confidence in the quality and quantity of source information supporting a judgment does not imply that that assessment is an absolute certainty or fact. The judgment still has a marginal probability of being inaccurate.
  * **Moderate Confidence:**

Judgments are based on information that is credibly sourced and plausible, but not of sufficient quantity or corroborated sufficiently to warrant a higher level of confidence.

This level of confidence is used to express that judgments carry an increased probability of being incorrect until more information is available or corroborated.
  * **Low Confidence:**

Judgments are made where the credibility of the source is uncertain, the information is too fragmented or poorly corroborated enough to make solid analytic inferences, or the reliability of the source is untested.

Further information is needed for corroboration of the information or to fill known intelligence gaps.



#### Additional Resources

  * _For more intel about CARBON SPIDER, visit the[ CrowdStrike Adversary Universe](https://adversary.crowdstrike.com/en-US/adversary/carbon-spider.html)._
  * _To find out how to incorporate intelligence on threat actors into your security strategy, visit the[ CROWDSTRIKE FALCON® INTELLIGENCE™ Threat Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Learn about the powerful, cloud-native[ CrowdStrike Falcon® platform by visiting the product webpage. ](/en-us/endpoint-security-products/)_
  * _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) to see for yourself how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)