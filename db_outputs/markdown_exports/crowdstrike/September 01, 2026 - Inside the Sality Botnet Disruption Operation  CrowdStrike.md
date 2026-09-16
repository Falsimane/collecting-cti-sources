# Inside the Sality Botnet Disruption Operation | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/inside-sality-botnet-disruption-operation/
- **Date :** September 01, 2026

---

# Peer Pressure: Inside the Sality Botnet Disruption Operation

## CrowdStrike collaborated with international law enforcement and industry partners to execute a coordinated disruption of the Sality peer-to-peer botnet.

September 01, 2026

• [ CrowdStrike Counter Adversary Operations](/en-us/blog/author.crowdstrike-counter-adversary-operations/ "Posts by CrowdStrike Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


On August 31, 2026, CrowdStrike's Counter Adversary Operations team, in collaboration with international law enforcement and industry partners, executed a coordinated disruption of the Sality peer-to-peer (P2P) botnet, a criminal infrastructure that has operated with seeming impunity for more than two decades.

The botnet enabled the operator to distribute malicious payloads to over 33,000 infected machines worldwide. We executed a peer-to-peer sinkholing operation that isolates infected machines, rendering the criminal's command channel inert.

This action was carried out in partnership with the U.S. Department of Justice (DOJ), the Federal Bureau of Investigation (FBI), the Department of Defense Office of Inspector General’s Defense Criminal Investigative Service (DCIS), and the Shadowserver Foundation, with support from Europol, Eurojust, and law enforcement agencies in Bulgaria, Hungary, and Romania. We also acknowledge additional unnamed partners whose contributions were essential to the success of this operation.

Active disruption of criminal infrastructure is a necessary component of a modern response to cyber threats. CrowdStrike is committed to taking the fight to the adversaries, regardless of how long they have operated or how resilient their infrastructure appears.

![Figure 1. Locations of machines infected with Sality](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Sality-1?wid=1519&hei=668&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 1. Locations of machines infected with Sality

## Background: What Is Sality?

Sality is a file-infecting malware that evolved from a traditional botnet into a sophisticated P2P botnet over its more-than-20-year lifespan. First observed in 2003, it has been one of the most persistent threats on the internet, not because of its payloads but because of the robustness of its architecture.

### A Persistent Threat

Two independent P2P networks, known as version 3 and version 4, remained active until this week. They shared the same codebase and were operated by the same threat actor, but used incompatible protocol versions and different cryptographic keys.

Sality persisted for two fundamental reasons:

  1. **Peer-to-peer resilience:** Unlike botnets that depend on traditional command-and-control (C2) servers, Sality's P2P architecture had no single point of failure. Infected machines communicated directly with each other, forming a self-sustaining network that routes tasking without centralized infrastructure.
  2. **File infection spreading:** Sality was a polymorphic file infector. It attached itself to executable files on infected systems and spread via network shares, removable drives, and file sharing. This meant infections regenerated continuously without requiring phishing campaigns, exploit kits, or any active effort from the operator.



### Low-Effort Monetization

Sality's sole technical capability was to deploy additional payloads to infected machines. Throughout its history, Sality distributed a wide variety of distinct malware families spanning credential theft, spam distribution, proxy services, network exploitation, and distributed denial-of-service (DDoS) attacks. For the past eight years, the primary payload has been EggJagger, a clipjacking tool that monitors the clipboard for cryptocurrency wallet addresses and silently replaces them with addresses controlled by the operator. When a victim copies a Bitcoin or Ethereum address to make a payment, the funds are redirected.

![Figure 2. Total cryptocurrency stolen by Sality's EggJagger payload, in rubles](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Sality-2?wid=1271&hei=518&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 2. Total cryptocurrency stolen by Sality's EggJagger payload, in rubles: ₽12M in actual damages; ₽147M in peak value; nominally ~$1.35M, but roughly the real purchasing power of $4M USD in a Western capital

CrowdStrike estimates the operator stole at least ₽12.1M rubles (~$150,000 USD) in cryptocurrency through this technique. The never-spent portfolio value peaked at ~₽147M in January 2025, enough to sustain a single criminal actor operating with minimal overhead to maintain an infrastructure that runs itself. This estimate only considers the EggJagger payload family; other payloads provide additional revenue streams.

### Occasional DDoS Attacks

Sality's operations were primarily financially motivated, but three notable DDoS campaigns reveal the operator was willing to weaponize the botnet for personal or political purposes on short notice. **Arabic Financial Forum Attack (April 2016):** An early DDoS payload targeted `forex2030[.]com`, an Arabic-language website covering natural resource trading companies. The attack successfully rendered the site unresponsive. The motivation remains unclear; possibly extortion or suppression of unfavorable information about a listed company. **Ukrainian Forum Attack (February 2022):** On February 25, 2022, one day after Russia's full-scale invasion of Ukraine, Sality distributed a DDoS payload targeting `kharkovforum[.]com`, a Ukrainian web forum hosting a thread where users discussed real-time events related to Russia's military offensive against Kharkiv. The payload generated massive HTTP traffic to overwhelm the forum, in an apparent attempt to suppress discussion of the invasion. This activity likely aligned with patriotic motivations. **Cryptocurrency Exchange Attack (September 2023):** A DDoS payload targeted _AvanChange_ , a Russian cryptocurrency exchange platform. The payload was compiled seconds before being uploaded to the distribution infrastructure, suggesting an impulsive reaction to a personal grievance, possibly a dispute over a transaction or account issue. The operator likely used such exchanges to convert stolen cryptocurrency to fiat currency.  
---  
  
## Disruption Operation

The criminal behind Sality has lost the ability to communicate with infected machines. The disruption operation isolates all peers in the network from their control. Once isolated, bots can no longer receive URL packs (payload download instructions) or file packs (direct payload transfers), rendering the botnet unable to carry out new tasking.

### Turning the Architecture Against Itself

The same properties that made Sality resilient also created the conditions for its undoing. Together, these properties are fatal. The protocol cannot be hardened against attack, and the network cannot exclude an active defender who speaks its language. The operation exploited this through **peer list manipulation** , the same class of technique used in the [2014 GameOver Zeus](https://www.crowdstrike.com/en-us/blog/gameover/) and [2017 Kelihos](https://www.crowdstrike.com/en-us/blog/inside-the-takedown-of-zombie-spider-and-the-kelihos-botnet/) botnet disruptions, adapted here for Sality's specific protocol behavior.

Sality's P2P protocol cannot be patched. Unlike conventional malware that can receive code updates from a C2 server, Sality's spreading mechanism is a file infector: It propagated by attaching itself to executables on disk. Releasing an updated variant would mean competing with the existing strain for the same host files, fragmenting the botnet rather than upgrading it. The protocol behavior that bots exhibit today is the same it exhibited 20 years ago. Every weakness in that protocol is permanent.

Sality bots trusted the network without verifying who was in it. Any machine that was publicly reachable and responded correctly to the P2P handshake was accepted as a legitimate peer. There was no authentication, no cryptographic identity, no allowlist. The only requirement was availability. This meant anyone could join the network as a full participant, indistinguishable from a genuinely infected machine.

### Peer List Manipulation

In practice, the operation targeted the data structure at the heart of every bot's network awareness: its peer list. Every Sality bot maintains a finite list of known super peers, which are publicly reachable infected machines that form the backbone of the P2P network. Every 40 minutes, it verifies whether its stored peers are still online. Peers that respond accumulate reputation; those that fail to respond lose reputation and are eventually purged. The disruption took advantage of this maintenance cycle by:

  1. **Removing legitimate peers:** Protocol-level manipulation during peer verification allows legitimate super peer entries to be invalidated in each bot's peer list, progressively isolating infected machines from the operator's network.
  2. **Inserting sinkhole entries:** Purpose-built sinkholes are injected into the emptied peer lists, providing visibility into the operation's progress and enabling infection tracking and victim notification.



The disruption targets super peers first, as they form the network's communication backbone. Once isolated, both URL packs and file packs stop propagating. The majority of infections sit behind firewalls or network address translation (NAT) and cannot be directly contacted. For these machines, we apply a more passive approach: When they contact sinkhole nodes during their normal maintenance cycles, their peer lists are purged, leaving them permanently isolated.

From the operator’s perspective, infected machines simply disappear.

### Payload URL Takedowns

In parallel with the P2P sinkhole operation, we coordinated with international law enforcement to take down the URLs currently hosting Sality payloads. These URLs are distributed via URL packs, which are lists pointing to files on compromised or operator-maintained web servers. Disrupting Sality’s ability to download these files ensures that bots still carrying active URL packs cannot retrieve new payloads during the transition period.

## Identifying Infections

All Sality-infected machines now beacon to CrowdStrike-operated sinkholes. Organizations should review network logs and endpoint telemetry for UDP traffic to the following “lighthouse” IP address. Any match indicates a Sality infection requiring remediation.
    
    
    188.166.101[.]148
    

### Indicators of Compromise

The following are the last URL packs distributed before the disruption. Attempts to access any of these URLs indicates a Sality infection:
    
    
    http[:]//theunforgiven.p8[.]hu/img/top.gif
    http[:]//painelwebradiodigital.awardspace[.]info/v3/readme.pdf
    http[:]//sgwebdesigner.free[.]fr/left.gif
    http[:]//www.yonelco[.]com/icon.png
    http[:]//pozdravizbeograda[.]com/readme.pdf
    http[:]//highclass.atspace[.]com/styles.gif
    http[:]//situluimihai.3x[.]ro/top.png
    

_Sality v3 URL pack version 25202_
    
    
    http[:]//gatheredovertime[.]com/nb4
    http[:]//imagebucket[.]biz/nv4
    

_Sality v4 URL pack version 31010_

### YARA Rules for Memory Scanning

The following YARA rules detect active Sality infections by scanning running processes for the botnet's hardcoded RSA public keys, which are used to verify payload signatures:
    
    
    rule CrowdStrike_Salityv3_01 : p2p sality version3
    {
        meta:
            copyright = "(c) 2026 CrowdStrike Inc."
            description = "Sality Version 3"
            version = "202608181745"
            last_modified = "2026-08-18"
            actor = "SALTY SPIDER"
            malware_family = "Sality"
        strings:
            $ = "IPFILTERDRIVER"
            $ = {
                99 65 40 34 cd ae 9d b3  af f5 82 ad 8c 2e 63 51
                e1 34 53 fa 47 54 e4 70  97 4c a5 3d 3c a3 9b 57
                29 02 49 89 46 4c f2 76  b1 ad 8e 79 5d b2 41 28
                4f 2a a5 9a 13 18 c0 1d  ed da e4 52 98 16 7f b3
                a9 d7 7a e4 c4 6f 51 f6  38 fe a6 fb ad 8c 64 1d
                23 b5 a4 9d 40 20 74 61  be 81 c3 eb 3d 24 01 75
                13 07 58 c5 f0 56 09 94  58 e7 6b c3 f3 8c 70 73
                4e f5 0b 2d 88 0b 9a bd  18 e4 36 72 26 1a 32 9b
            }
        condition:
            all of them
    }
    

_YARA rule matching the Sality v3 embedded RSA public key_
    
    
    rule CrowdStrike_Salityv4_01 : p2p sality version4
    {
        meta:
            copyright = "(c) 2026 CrowdStrike Inc."
            description = "Sality Version 4"
            version = "202608181745"
            last_modified = "2026-08-18"
            actor = "SALTY SPIDER"
            malware_family = "Sality"
        strings:
            $ = "IPFILTERDRIVER"
            $ = {
                bb d2 96 8e ed 0b 93 8a  82 e4 e9 bc c3 c5 32 72
                4c 08 aa 56 9f 2d 64 0f  1b 86 68 0e 2b 62 e9 c6
                35 6d 75 b6 32 2d 4f a8  b8 d9 2a 44 8b f0 7f e0
                d9 8e be 66 9d a6 7a 9a  6d e1 45 f1 d3 48 01 0d
                39 2e 9d 2a 45 fb 0b fb  1d 96 f3 b7 4f 55 e5 e1
                16 5b f7 a1 cc 7c 87 c0  c8 9c ef 4e ce 29 58 e2
                99 bd 8a 7a 55 be b4 1c  d9 79 52 25 d8 28 86 7b
                81 39 98 5f 2c 6f 14 bb  a5 6b ce 44 e5 91 93 38
                8b 9a c1 74 46 84 e1 26  ec 04 94 96 75 09 e3 b5
                88 d6 08 f0 4a b7 84 d3  13 2f 00 cc d5 2a 8c 17
                07 09 de 6f b0 d3 d6 2b  c6 a6 9d 38 18 8c 74 9d
                86 16 d5 48 6e 97 32 db  e1 4e f8 04 a6 00 7c 16
                2e 70 1c 23 37 dd 5a 52  76 62 70 d4 86 66 6e df
                0c e9 a1 68 f9 5e e8 dd  09 0c 02 7d 35 d0 54 e7
                00 c0 14 9f ce 4a 9f f3  99 50 1a 0b cd cc ff 05
                b9 04 12 e2 11 76 2f ff  a4 6e 64 18 e0 d0 7b 3b
            }
        condition:
            all of them
    }
    

_YARA rule matching the Sality v4 embedded RSA public key_

## Conclusion

After more than two decades of continuous operation, CrowdStrike, together with international law enforcement and industry partners, conducted a successful disruption operation against the Sality botnet, which is now no longer under the operator's control.

This operation demonstrates that P2P architecture, long considered a shield against disruption, is not invincible. With sufficient technical investment, precise understanding of protocol behavior, and coordination with law enforcement and industry partners, even the most resilient criminal infrastructure can be dismantled.

Network defenders should use the indicators provided in this post to identify Sality infections in their environments. Any UDP traffic to the lighthouse IP address confirms an active infection. While the disruption prevents new payloads from reaching infected machines, existing malware already installed on those systems remains active and should be removed. We encourage organizations to scan running processes with the provided YARA rules, monitor for connections to the listed URLs, and remediate any confirmed infections.

Active disruption is a necessary element of modern cyber defense. Detection informs; disruption protects. Organizations cannot simply observe threats and hope they recede. They must be confronted, their infrastructure destroyed, and their operators held accountable.

To the Sality operator and criminals like them: Operating for decades without consequence does not mean operating without risk. The calculus has changed. We will find you, we will dismantle your infrastructure, and we will impose costs that make the enterprise untenable.

CrowdStrike's Counter Adversary Operations team remains committed to taking the fight to the adversary.

#### Additional Resources

  * _Learn more about[CrowdStrike Counter Adversary Operations](https://www.crowdstrike.com/en-us/platform/threat-intelligence/) threat intelligence and threat hunting._
  * _Tune in to the[Adversary Universe podcast](https://www.crowdstrike.com/resources/adversary-universe-podcast/), where CrowdStrike reveals the threat actors behind the latest cyberattacks._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/) [ ![Inside Astaroth's New Spambot Component](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Scattered-Spider?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Jul 29, 2026  Inside Astaroth's New Spambot Component ](/en-us/blog/inside-astaroths-new-spambot-component/)