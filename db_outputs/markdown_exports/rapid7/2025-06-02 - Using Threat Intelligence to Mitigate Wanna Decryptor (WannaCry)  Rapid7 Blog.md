# Using Threat Intelligence to Mitigate Wanna Decryptor (WannaCry) | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2017/05/15/using-threat-intelligence-to-mitigate-wanna-decryptor-wncry/
- **Date :** 2025-06-02

---

## Basics of Cyber Threat Intelligence

Cyber Threat Intelligence is **analyzed information about the opportunities, capabilities, and intent of cyber adversaries.** The goal of cyber [threat intelligence](/fundamentals/what-is-threat-intelligence/) is to help people make decisions about how to prevent, detect, and respond to threats against their networks. This can take a number of forms, but the one people almost always turn to is IOCs. IOCs, or indicators of compromise, are technical network artifacts that can alert a defender that their system is compromised. These include things like IP addresses, domain names, hashes, file names, etc. IOCs are often a good way to detect malicious activity, but **they are not the only output of threat intelligence, and often they are not the best output.**

## Threat Intelligence for WannaCry

In the case of WannaCry (get an [overview of the WannaCry vulnerability here](/blog/post/2017/05/12/wanna-decryptor-wncry-ransomware-explained/)) – the primary IOCs available are the hashes and file names of the ransomware samples. By the time you alert on those on your system, it is already too late: the system is already being encrypted. WannaCry also uses a cryptographic loading mechanism that prevents the malicious DLL from ever touching the disk, which means that antivirus will not detect or block it. The hashes are useful from a research perspective, such as identifying new variants or tracking changes to the malware, but they are not useful for detection.

Likewise, there are a few blogs that have published IP addresses that are related to the campaign, but have not provided information as to the nature of those IPs. This makes it hard to know how to handle them or use them in incident detection and response scenarios. Many of the IPs associated with WannaCry are so associated because they have been seen scanning for port 445. We know that WannaCry must scan for that port to identify systems to compromise; however, Wanna Cry is not the only thing that scans the internet, and blocking or alerting on scanning IPs will create a large number of false positives.

The kill switch domain is a good indicator that you have compromised systems on your network that should be remediated. Contact with this domain - **which should be allowed to prevent encryption!** – can be used as a way to track what systems are compromised and launch investigations accordingly. It is not a prevention method, but it can help identify hosts compromised with this variant. The InsightIDR threat community has a threat list that will alert (but not block) this domain to assist with identification of compromised hosts.

## A Better Approach

IOC-based threat intelligence is not the best approach for dealing with WannaCry—a vulnerability-based approach is. The best indicator that you will be compromised is whether or not you are vulnerable to the ETERNAL BLUE exploit that WannaCry uses as an initial attack vector. One researcher put a SMB honeypot up with port 445 open and was exploited in less than 3 minutes. With the way that WannaCry is spreading, if you are vulnerable, you will be compromised. Ensuring that all of your systems are patched, port 445 is not open to the internet, and network segmentation is in place are all far better things to focus on than finding IOCs for WannaCry.

For information on how to scan for, and remediate, MS17-010 with Nexpose and InsightVM, please read this [blog](/blog/post/2017/05/17/scanning-and-remediating-wannacry-in-insightvm-and-nexpose/).

## WannaCry is Just the Beginning...

The reality is that we're likely to see more attacks leveraging this attack vector.

The basic equation for threats is as follows:
    
    
    Threat = opportunity + capability + intent
    

![Screen_Shot_2017-05-15_at_7.35.41_PM.png](https://www.rapid7.com/cdn/images/bltcc4da062f25afeaf/683de51618a55362106871aa/Screen_Shot_2017-05-15_at_7.35.41_PM.png)

For the WannaCry Ransomworm, the equation looks like this:
    
    
    WannaCry = Unpatched flaw in SMB + ETERNAL BLUE with ransomware and worming capabilities + Desire for $$$
    

But we have an almost unending list of _potential threats_ , since the opportunity and capability are both public. It is almost guaranteed that we will see other threats where:

**Opportunity** = Unpatched flaw in SMB

**Capability** = Some variation of ETERNAL BLUE

**Intent** = Money, power, chaos, revenge, etc.

We can monitor for new capabilities that are being developed, we can brainstorm potential threat actor intents to understand whom the threat may target, but what will remain the same across all of these threats is the opportunity that the attacks have. If we can remove that opportunity then the threats will not exist, and will become an _insubstantial threat_ , as the attackers will have no way to leverage their capabilities.

## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)