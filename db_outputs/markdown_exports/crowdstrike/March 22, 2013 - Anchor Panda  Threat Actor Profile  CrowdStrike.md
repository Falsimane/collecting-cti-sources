# Anchor Panda | Threat Actor Profile | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/whois-anchor-panda/
- **Date :** March 22, 2013

---

# Who is Anchor Panda

March 22, 2013

• [ AdamM](/en-us/blog/author.adamm/ "Posts by AdamM") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Anchor Panda is an adversary that CrowdStrike has tracked extensively over the last year **targeting both civilian and military maritime operations in the green/brown water regions primarily in the area of operations of the South Sea Fleet of the PLA Navy**. In addition to maritime operations in this region, Anchor Panda also **heavily targeted western companies in the US, Germany, Sweden, the UK, and Australia, and other countries involved in maritime satellite systems, aerospace companies, and defense contractors.** Not surprisingly, embassies and diplomatic missions in the region, foreign intelligence services, and foreign governments with space programs were also targeted. We won't share too many details about this adversary - we don't want to make it too easy for them - but we will share some signatures specific to Anchor Panda.

These signatures will help you find Anchor Panda, just remember to change the Signature ID (sid). `alert tcp $VICTIM any -> $CONTROLLER any (msg: " ANCHOR PANDA - Adobe Gh0st Beacon"; flow: established, to_server; content: "Adobe"; offset: 0; depth: 5; content: "|e0 00 00 00 78 9c|"; distance: 4; within: 15; sid: xxx; rev: 1; reference: url,http://blog.crowdstrike.com/whois-anchor-panda/index.html; )`

`alert tcp $CONTROLLER any -> $VICTIM any (msg: " ANCHOR PANDA - Poison Ivy Keep-Alive - From Controller"; dsize: 48; flow: established, from_server; content: "|54 90 1d b0 18 1b 7c ce f4 5b 24 2f ec c7 d2 21|"; depth: 16; sid: xxx; rev: 1; reference: url,http://blog.crowdstrike.com/whois-anchor-panda/index.html; )`

`alert tcp $VICTIM any -> $CONTROLLER any (msg: " ANCHOR PANDA - Poison Ivy Keep-Alive - From Victim"; dsize: 48; flow: established, to_server; content: "|af c0 bb 65 5d 07 e0 0d 

bf ab 75 2f 82 79 ae 26|"; depth: 16; 

sid: xxx; rev: 1; reference: url,http://blog.crowdstrike.com/whois-anchor-panda/index.html; )`

`alert tcp $VICTIM any -> $CONTROLLER any (msg: " ANCHOR PANDA Torn RAT Beacon Message Header Local"; 

flow: established, to_server; dsize: 16; content: "|00 00 00 11 c8 00 00 00 00 00 00 00 00 00 00 00|"; depth: 16; flowbits: set,toread_header; flowbits: noalert; sid: xxx; rev: 1; reference: url,http://blog.crowdstrike.com/whois-anchor-panda/index.html; )`

`alert tcp $VICTIM any -> $CONTROLLER any (msg: " ANCHOR PANDA Torn RAT Beacon Message"; dsize: 200; flow: to_server,established; flowbits: isset,toread_header; content: "|40 7e 7e 7e|"; offset: 196; depth: 4; sid: xxx; rev: 1; reference: url, http://blog.crowdstrike.com/whois-anchor-panda/index.html; )`

## Other Known China-based Adversaries

  * [Deep Panda](/en-us/blog/ironman-deep-panda-uses-sakula-malware-target-organizations-multiple-sectors/)
  * [Goblin Panda](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-august-goblin-panda/)
  * [Mustang Panda](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-june-mustang-panda/)
  * [Samurai Panda ](/en-us/blog/whois-samurai-panda/)

_**Curious about other nation-state adversaries?**_ _Visit our[threat actor hub](/blog/meet-the-adversaries.html) to learn about the new adversaries that the CrowdStrike team discovers._

Be sure to follow [@CrowdStrike](http://twitter.com/Crowdstrike) on Twitter as we continue to provide more intelligence and adversaries over the coming weeks. 

If you have any questions about these signatures or want to hear more about Anchor Panda and their tradecraft, please contact: intelligence@crowdstrike.com and inquire about our intelligence-as-a-service solutions.

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)