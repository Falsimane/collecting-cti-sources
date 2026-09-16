# DUNGEON SPIDER | Threat Actor Profile | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-october-dungeon-spider/
- **Date :** October 26, 2018

---

# Meet CrowdStrike’s Adversary of the Month for October: DUNGEON SPIDER

October 26, 2018

• [ AdamM](/en-us/blog/author.adamm/ "Posts by AdamM") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


DUNGEON SPIDER is a criminal group operating the ransomware most commonly known as _Locky_ , which has been active since February 2016 and was last observed in late 2017. Locky is a ransomware tool that encrypts files using a combination of cryptographic algorithms: RSA with a key size of 2,048 bits, and AES with a key size of 128 bits. Locky targets a large number of file extensions and is able to encrypt data on shared network drives. In an attempt to further impact victims and prevent file recovery, Locky deletes all of the Shadow Volume Copies on the machine. Locky uses a set of hard-coded IP addresses for C2 (command and control) communications, and once the victim has been infected, an initial HTTP POST is made using a file path of `/checkupdate` appended to the C2s. Locky will then continue to communicate with the hard-coded IP addresses thereafter, or it will resort to its domain generation algorithm (DGA), if they become unreachable. Some variants of Locky also have the ability to operate offline, meaning they do not require internet connectivity or C2s to encrypt a victim’s files. Each victim is assigned a personal identification number that is generated upon infection, sent back to the C2s, and used to provide the victim-specific decryption key should the ransom be paid. Once infected with Locky, so-called “help files” are dropped onto the victim machine, providing details of how to pay the ransom for file recovery. The Locky ransom payment portal URL has remained the same for some time: `g46mbrrzpfszonuk<.>onion/{personal ID number}.` CrowdStrike® CrowdStrike Falcon® IntelligenceTM has not observed distribution or development of Locky since late 2017, with one of the last major developments being the modification of the ransomware to use a file extension of `.diablo6`. Since Locky first came to the criminal market in early 2016, the ransomware quickly made a name for itself when it allegedly infected Hollywood Presbyterian Medical Center, resulting in a reported ransom payment of 40 Bitcoin (BTC). A ransomware variant dubbed PyLocky was observed in September 2018 being distributed by a phishing campaign using an invoicing theme. PyLocky was found to be targeting entities in France and Germany. Of note is the fact that PyLocky claims to be a version of Locky, which as noted above, has not been active for some time. It is Locky’s notoriety that has likely led to the operators of PyLocky choosing to appropriate its name and likeness; mimicking the names of successful ransomware families is a technique often used by criminal actors to gain customers. There is no evidence, as of this writing, that PyLocky is at all related to either Locky ransomware or DUNGEON SPIDER, the developers of Locky. However, the emergence of PyLocky and its attempt to masquerade as a previously prolific and potent version of Locky indicates that adversaries continue to actively develop ransomware, and that it remains a dominant and viable threat vector. DUNGEON SPIDER primarily relies on broad spam campaigns with malicious attachments for distribution. Locky is the community/industry name associated with this actor. 

## Other Known Criminal Adversaries

  * [Cobalt Spider](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-september-cobalt-spider/)
  * [Mummy Spider](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-february-mummy-spider/)
  * [Salty Spider (Sality)](/blog/who-is-salty-spider.html)
  * [Wicked Spider](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-july-wicked-spider/)

_**Curious about other nation-state adversaries?**_ _Visit our[threat actor center](/blog/meet-the-adversaries.html) to learn about the new adversaries that the CrowdStrike team discovers._

#### Learn More:

  * _To learn more about how to incorporate intelligence on threat actors such as DUNGEON SPIDER into your security strategy, please visit the_[ _Falcon Intelligence product page_](/content/crowdstrike-www/locale-sites/us/en-us/endpoint-security-products/falcon-x-threat-intelligence/?ctm_source=Website&ctm_medium=Blog&ctm_campaign=Blog-Inline-Copy)
  *  _Download the[CrowdStrike 2020 Global Threat Report ](/resources/reports/2020-crowdstrike-global-threat-report.html)to get the latest insights on

modern adversaries and their tactics, techniques, and procedures (TTPs)_



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)