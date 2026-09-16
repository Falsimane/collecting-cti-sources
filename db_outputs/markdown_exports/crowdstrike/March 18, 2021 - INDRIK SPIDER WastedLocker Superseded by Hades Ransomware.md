# INDRIK SPIDER: WastedLocker Superseded by Hades Ransomware

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/hades-ransomware-successor-to-indrik-spiders-wastedlocker/
- **Date :** March 18, 2021

---

# INDRIK SPIDER Supersedes WastedLocker with Hades Ransomware to Circumvent OFAC Sanctions

March 18, 2021

• [ Adam Podlosky - Brendon Feeley](/en-us/blog/author.adam-podlosky---brendon-feeley/ "Posts by Adam Podlosky - Brendon Feeley") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


## Introduction

In December 2019, the U.S. Treasury Department’s Office of Foreign Assets Control (OFAC) took [action](https://home.treasury.gov/news/press-releases/sm845) against the Russia-based cybercriminal group INDRIK SPIDER, also known as Evil Corp, a sophisticated eCrime ([ECX](https://adversary.crowdstrike.com) 357.19) adversary notorious for conducting numerous schemes against a variety of targets beginning in 2014. This adversary is best known for their [Dridex banking trojan](https://us-cert.cisa.gov/ncas/alerts/aa19-339a), which was prolific from June 2014 through early 2020, and their Bitpaymer crypter used in [big game hunting (BGH) attacks beginning in 2017](/en-us/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/). The OFAC action consisted of sanctions that prohibit the facilitation of significant payments to the organization, such as those involved in BGH ransom payments.

In addition to OFAC’s action against INDRIK SPIDER, the U.S. Department of Justice (DOJ) charged two key members of the group — Maksim Yakubets and Igor Turashev — with criminal infringements, and the U.S. Department of State announced a reward of up to $5 million USD for any information leading to the capture or conviction of INDRIK SPIDER’s leader. Following the OFAC sanctions and the unsealing of the indictment, INDRIK SPIDER went through significant periods of downtime and continued to develop their MO, TTPs and tradecraft in an attempt to evade the sanctions placed upon them — the latest evolution is Hades, which first reared its head after the OFAC action was announced.

## INDRIK SPIDER’s Reaction

Subsequent to the announcement of the sanctions against the group, INDRIK SPIDER disappeared for a short while until reappearing in January 2020, when BitPaymer was once again observed being used in a BGH operation against a victim conglomerate spanning multiple verticals. This BitPaymer operation was one of the first identified examples of INDRIK SPIDER using a variant of Gozi ISFB as a part of their toolset instead of their Dridex banking trojan. Following a short hiatus from March to May 2020, INDRIK SPIDER significantly increased their efforts to move away from their existing tools and introduced WastedLocker — the successor to their BitPaymer ransomware. Approximately six months after the OFAC sanctions and the unsealing of the indictment against Yakubets and Turashev, WastedLocker was used in the first BGH campaign, marking a new era for INDRIK SPIDER, as they also began using a variant of Gozi ISFB in their operations. This further operational shift was highly likely an attempt to distance themselves from their infamous Dridex and BitPaymer tools. In June 2020, the trend of moving away from their typical infection chain continued, and INDRIK SPIDER began using fake browser updates to deliver the Cobalt Strike red-teaming tool. INDRIK SPIDER extensively used [Cobalt Strike](/en-us/blog/getting-the-bacon-from-cobalt-strike-beacon/) to establish an initial foothold and [move laterally](/en-us/cybersecurity-101/cyberattacks/lateral-movement/) within the victim network. Once control over the enterprise environment was established, WastedLocker would subsequently be executed in their BGH campaigns. INDRIK SPIDER continued with their usual operational tempo, infecting organizations across more than a dozen sectors — predominantly in the U.S. — until late 2020.

## WastedLocker to Hades Evolution

Based on significant code overlap, CrowdStrike Intelligence has identified Hades ransomware as INDRIK SPIDER’s successor to WastedLocker. Hades ransomware — first publicly identified by [security researchers in December 2020](https://twitter.com/demonslay335/status/1339324224029274118) — was named for a Tor hidden website that victims are instructed to visit; however, Hades is merely a 64-bit compiled variant of WastedLocker with additional code obfuscation and minor feature changes. The WastedLocker-derived Hades ransomware is unrelated to a similarly named ransomware family, Hades Locker, identified by security firms in 2016. Hades ransomware shares the majority of its functionality with WastedLocker; the ISFB-inspired static configuration, multi-staged persistence/installation process, file/directory enumeration and encryption functionality are largely unchanged. Hades did receive minor modifications, and the removed features included those that were uniquely characteristic of INDRIK SPIDER’s previous ransomware families — WastedLocker and BitPaymer. At the time of this publication, CrowdStrike has identified the following changes INDRIK SPIDER made to the WastedLocker-derived Hades ransomware variant:

  * Hades is now a 64-bit compiled executable with additional code-obfuscation, likely to disguise the minimal changes, evade existing signature-based detections and hinder reverse engineering efforts.
  * The majority of standard file and registry Windows API calls were replaced with their system call counterparts (i.e., the user-mode Native APIs exported from NTDLL).
  * Hades employs a different User Account Control (UAC) bypass than WastedLocker; however, both implementations are taken directly from the open-source UACME project (https<:>//github<.>com/hfiref0x/UACME).
  * Hades writes a single ransom note named `HOW-TO-DECRYPT-.txt` to traversed directories, as opposed to WastedLocker’s and BitPaymer’s approach of creating a note for each encrypted file.
  * Hades ransomware now stores the key information in each encrypted file rather than the ransom note. Both WastedLocker and BitPaymer stored the encoded and encrypted key information in the file-specific ransom notes.
  * While Hades still copies itself to a generated subdirectory in `Application Data`, it no longer uses the `:bin` Alternate Data Stream (ADS). The use of the `:bin` ADS path was characteristic of both WastedLocker and BitPaymer.

INDRIK SPIDER’s move to this ransomware variant also came with another shift in tactics: the departure from using email communication and the possibility of exfiltrating data from victims to elicit payments. The Hades ransom note (shown in Figure 1) directs victims to a Tor hidden site. The identified ransom notes do not identify the victim company, as was often observed with WastedLocker and BitPaymer.

![ransomware note](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/03/Picture1-1-1024x628.png) Figure 1. Hades ransomware (WastedLocker variant) ransom note

The Tor website (shown in Figure 2) is unique for each victim and states that data has been exfiltrated from their network. The only provided means of contact is a Tox-identifier for communication with the Tox peer-to-peer instant messenger (https<:>//tox<.>chat/)

![ransomware note](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/03/Picture2-1-1024x591.png) Figure 2. Hades ransomware (WastedLocker variant) Tor site

## Conclusion

Since the OFAC sanctions and DOJ indictments against the group and its members, INDRIK SPIDER’s continued diversification has demonstrated the group’s significant resources and operational resilience. INDRIK SPIDER’s ability to adapt and overcome adversity has been illustrated in their continual advances in their campaigns, implementation of new tools, and adoption of third-party products and services. The development of their tradecraft has almost certainly been prompted by the legal action taken against them. The continued development of WastedLocker ransomware is the latest attempt by the notorious adversary to distance themselves from known tooling to aid them in bypassing the sanctions imposed upon them. The sanctions and indictments have undoubtedly significantly impacted the group and have made it difficult for INDRIK SPIDER to successfully monetize their criminal endeavors.

### Indicators of Compromise

**Description**| **SHA256 Hash**  
---|---  
Hades ransomware, variant of WastedLocker| `fe997a590a68d98f95ac0b6c994ba69c3b2ece9841277b7fecd9dfaa6f589a87`  
  
#### Additional Resources

  * _Read more about big game hunting adversaries tracked by CrowdStrike Intelligence in 2020 in the[ CrowdStrike 2021 Global Threat Report](/en-us/resources/reports/global-threat-report/)._
  * _Check out the[ Global Threat Report resource hub](/en-us/global-threat-report/) to learn more about today’s adversaries._
  * _To find out more about how to incorporate intelligence on threat actors into your security strategy, visit the[ CROWDSTRIKE FALCON® INTELLIGENCE™ Threat Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Learn more about the powerful, cloud-native[ CrowdStrike Falcon® platform by visiting the product webpage. ](/en-us/endpoint-security-products/)_
  *  _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html)and learn how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)