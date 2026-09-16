# DOUBLEPULSAR over RDP: Baselining Badness on the Internet | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/02/04/doublepulsar-over-rdp-baselining-badness-on-the-internet/
- **Date :** 2025-06-02

---

Part of the mission of the Rapid7 Labs team is to help reduce internet exposure-related risk through internet-wide visibility and data collection, analytics, and public collaboration. Our Project Sonar effort tries to understand attacker opportunity by measuring software, versions, and configuration of various services on the internet as well as monitoring how they change over time. Our Project Lorelei fleet of honeypots provides a different perspective in that it helps us observe attacker capabilities and behaviors.

On Tuesday, Feb. 4, Rapid7’s William Vu released a [Development Diary-style blog post](/blog/post/2020/02/04/doublepulsar-rce-2-an-rdp-story/) where he discusses the path he took to create the [newly released Metasploit module](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/rdp/rdp_doublepulsar_rce.rb) for interacting with the DOUBLEPULSAR implant over Microsoft’s Remote Desktop Protocol (RDP). 

In order to provide context for this topic, we wanted to be able to answer two questions:

  * How many internet-accessible RDP services have the DOPU implant installed?
  * How much DOPU-over-RDP traffic do we see being sprayed across the internet?



## Background

[DOUBLEPULSAR (DOPU)](https://en.wikipedia.org/wiki/DoublePulsar) is a kernel-mode implant (backdoor) for Microsoft Windows operating systems. It was released by the [Shadow Brokers](https://en.wikipedia.org/wiki/The_Shadow_Brokers) on April 14, 2017, as part of an exploit toolkit they reportedly stole from the [Equation Group](https://en.wikipedia.org/wiki/Equation_Group). Most people’s knowledge of this toolkit’s contents will be by way of the [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) and Nyetya worms, which used the [E](https://en.wikipedia.org/wiki/EternalBlue)ternalBlue exploit to spread over the Server Message Block (SMB) protocol. Both also deployed the DOPU implant upon successful compromise. In those cases, the malware used the SMB version of DOPU. William’s [recent work](/blog/post/2020/02/04/doublepulsar-rce-2-an-rdp-story/) is related to the RDP variant, which has had very limited coverage.

## A survey of existing compromise

We wanted to measure how many hosts were running an unmodified version of DOPU RDP implant. While it wouldn’t tell us how the implant got there in the first place, it would tell us that a.) the host had been compromised and b.) anyone who can find it and has the correct tools can pretty much do whatever they want with this pre-pwned host.

I want to point out that we’re only measuring **unmodified** versions of DOPU. It isn’t terribly difficult to change the magic bytes used in the DOPU commands so as to make the implant not respond to our probes.

We wrote our scanner for Project Sonar, deployed the infrastructure, scanned the Internet, and found ... nothing. Every time we scan for some form of badness we always find something, but not this time. Sure, we found Windows XP hosts and hosts that didn’t leverage [Network Level Authentication (NLA)](https://en.wikipedia.org/wiki/Network_Level_Authentication) for security, but we didn’t find any hosts we thought were legitimately running the implant. It was so atypical that we thought the code was broken. We retested everything locally and across the internet, but we turned out the same results. We checked for RDP and the implant over several non-standard ports such as 80, 443, 3388, 3390, 8888, etc. We found RDP but no implant.  


![](https://lh3.googleusercontent.com/2deQ7zRIBXZiz5G2KsK2c3ddfAl28iEVb6CExfQnVf1gHpe_3nLpc5ytFdvIGlglnwxluk13vJTVJNAbVYF5vX4OGKRK9pP-G1_PljoUvNEsm-C_njutw5z2kqiEbgGdpVsx2j1a)

  


That’s good news, right? Well, I’d say that’s a qualified “yes.” As I mentioned, it’s easy to change the implant so that it doesn’t respond to the normal magic bytes and we simply wouldn’t see it. Also, DOPU doesn’t survive a system restart, which means that hosts could have been compromised and backdoored in the past but that the backdoor isn’t currently active.

Irrespective of the results, data provides us with a baseline that we can compare future scans against to know how things are changing.

## Observations of DOPU traffic

Another way that Rapid7 Labs provides context is via visibility into what tools and techniques attackers use against our honeypots and what they do once they get in. We know that attempts to locate DOPU over **SMB** are common. How common? Our honeypots saw 375,000 DOPU PING (discovery / are you there?) commands yesterday alone. 

That number isn’t an anomaly: We haven’t seen a day much below 200,000 going back six months.

![](https://lh6.googleusercontent.com/GaWYmWXb7FGPczfQ5AhY6pehJPG_DfiRAm-ptB-m8eIDA5qi5MVTaMCBfmuhscIt3nJW_tCXhp5hKxJSFiZOsLW1ouXV0n9dJWzvavqfKS0gXx8Or9aQFEXeJiJEodKR3odT5Ybj)

That volume can likely be attributed to the widespread infection of hosts by WannaCry and other malware that then installed DOPU-over-SMB. Given how prevalent that malware was, searching for a host that already had the SMB version of DOPU is likely to be worth an attacker’s time to code into tooling or implement in future malware.

With that in mind, to provide a similar view for RDP we added explicit DOPU-over-RDP coverage to our honeypots in December and looked back over the prior months for some artifacts that the Equation Group tools and certain third-party scripts were known to leave behind. 

The only traffic we saw were our own scanners. That’s great news and not terribly surprising given the lack of tooling for (and general awareness of) DOPU over RDP. As in the case of the Sonar, scans like this provide us with a baseline to work with going forward.

## Practical guidance

Normally, we like to leave people with practical guidance related to the risk that we are discussing. In this case, it will be a bit more general than normal since we’re not talking about a vulnerability that can be patched but rather a backdoor that was left behind once someone had already gotten in.

### Prevention

Disable RDP anywhere it isn’t used. This is pretty standard guidance for any service you don’t need. Attackers can’t walk through a door that doesn’t exist.

Don’t expose RDP to the internet. Leverage a VPN or gateway technology to enable access to RDP services if possible. If you must expose RDP to the internet, use network Access Control Lists (ACLs) to limit which network addresses can connect.

Enable [Network Level Authentication (NLA)](https://en.wikipedia.org/wiki/Network_Level_Authentication). This setting requires authentication prior to connecting to RDP services. It breaks many RDP-related exploits and attacker tools while also improving the service’s overall security by requiring TLS and strong authentication methods. Our Sonar studies show that a significant number of RDP services still use Standard RDP or TLS security.  


![](https://lh5.googleusercontent.com/tybVlZxCOyMHmpgO0QccAaZTjaefwM7PjIbgvFwFA-V5EZe7ejKqcTmbKjDLwa-wHYuUnay66_4Q7bwnzko5a2Va8YnrHZoTPUnGv4-5tVKynUhC9qPRHGvD1Z2EvMi6Bk0dLq1k)![](https://lh5.googleusercontent.com/TGFzcHBSALA5M7UwRWZLRdDMWbARb3wk5r5UfZulxj9dR46D7xuAkaTJSrHNNDglxjOeZ3XepOwVkVauNrmw5-t5BUs8cAiKB0xExFORFGb3gHNqDktEEviF0sVDlVlr-8H8e4nU)

  


Finally, implement a risk management program to deploy patches and implement mitigating controls in a timely manner. It’s generally better to spend resources on patch management and other risk mitigation than in triage, incident response, and recovery. Internet-facing hosts should generally be among the first production systems to be addressed.

### Detection

Detection of DOPU traffic is sort of a mixed bag. While there appears to be good coverage for detecting network traffic related to DOPU over **SMB** , I don’t see the same level of IDS/IPS coverage for DOPU over **RDP**. There’s also the complication that an attacker can try to leverage TLS Security instead of Standard security and the sensor will not be able to see the attack. That last part applies to pretty much all RDP exploits.

You can use William Vu’s new [DOPU-over-RDP Metasploit module ](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/windows/rdp/rdp_doublepulsar_rce.rb)to scan your networks. You can use the **check** function to find the hosts and the **Neutralize implant** target to remove the DOPU implant. You can also reboot the host as the implant won’t survive a restart.

Interested in this research? Looking to collaborate? Questions? Comments? Leave them below or reach out via [email protected]!

## Article tags

  * [Research](/blog/tag/research/)
  * [Metasploit](/blog/tag/metasploit/)
  * [Project Lorelei](/blog/tag/project-lorelei/)
  * [Project Sonar](/blog/tag/project-sonar/)
  * [Honeypots](/blog/tag/honeypots/)
  * [Labs](/blog/tag/labs/)