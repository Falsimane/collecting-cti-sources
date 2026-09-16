# Technical Analysis of the WhisperGate Malicious Bootloader | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/technical-analysis-of-whispergate-malware/
- **Date :** January 19, 2022

---

# Technical Analysis of the WhisperGate Malicious Bootloader

January 19, 2022

• [ CrowdStrike Intelligence Team](/en-us/blog/author.crowdstrike-intelligence-team/ "Posts by CrowdStrike Intelligence Team") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


On Jan. 15, 2022, a set of malware dubbed _WhisperGate_ was reported to have been deployed against Ukrainian targets. The incident is widely reported to contain three individual components deployed by the same adversary, including a malicious bootloader that corrupts detected local disks, a Discord-based downloader and a file wiper. The activity occurred at approximately the same time multiple websites belonging to the Ukrainian government were defaced. This blog covers the malicious bootloader in more detail.

## Details

The installer component for the bootloader has an SHA256 hash of  `a196c6b8ffcb97ffb276d04f354696e2391311db3841ae16c8c9f56f36a38e92` and contains a build timestamp of 2022-01-10 10:37:18 UTC. It was built using MinGW, similar to the file-wiper component. This component overwrites the master boot record (MBR) of an infected host with a malicious 16-bit bootloader with a SHA256 hash of  `44ffe353e01d6b894dc7ebe686791aa87fc9c7fd88535acc274f61c2cf74f5b8` that displays a ransom note when the host boots (Figure 1) and, at the same time, performs destructive operations on the infected host’s hard drives.

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/01/Screen-Shot-2022-01-19-at-12.19.18-PM-1024x281.png) Figure 1. Fake ransom note

The destructive wiping operation has the following pseudocode:
    
    
    for i_disk between 0 and total_detected_disk_count do
       for i_sector between 1 and total_disk_sector_count, i_sector += 199, do
          overwrite disk i_disk at sector i_sector with hardcoded data
       done
    done
    

At periodic offsets, the bootloader overwrites sectors of an infected host’s entire hard drive, with a message similar to the ransom note, padded with additional bytes (Figure 2).

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/01/Screen-Shot-2022-01-19-at-1.36.57-PM-1024x702.png) Figure 2. Hexadecimal dump of the pattern written to the disks of an infected host

The data consists of the string `AAAAA`, the index of the infected drive, the ransom note and the MBR footer magic value `55 AA`, followed by two null bytes. The bootloader accesses the disk via BIOS interrupt `13h` in logical block addressing (LBA) mode and overwrites every 199th sector until the end of the disk is reached. After a disk is corrupted, the malware overwrites the next in the detected disk list.

This process is unsophisticated but reminiscent of the more evolved implementation of _NotPetya_ ’s malicious MBR that masqueraded as the legitimate `chkdsk` disk-repair utility while actually corrupting the infected host’s file system. The bootloader installer does not initiate a reboot of the infected system, as has been observed in past intrusions such as _BadRabbi t_ and _NotPetya_. The lack of forced reboot suggests the threat actor took other steps to initiate it (e.g., via a different implant) or decided to let users perform the reboot themselves. A delayed reboot may allow other components of the _WhisperGate_ intrusion to run (e.g., the file wiper).

## Assessment

The _WhisperGate_ bootloader malware complements its file-wiper counterpart. Both aim to irrevocably corrupt the infected hosts’ data and attempt to masquerade as genuine modern ransomware operations. However, the _WhisperGate_ bootloader has no decryption or data-recovery mechanism, and has inconsistencies with malware commonly deployed in ransomware operations.

The displayed message suggests victims can expect recovery of their data, but this is technically unachievable. These inconsistencies very likely indicate that _WhisperGate_ activity aims to destroy data on the impacted assets. This assessment is made with moderate confidence as technical analysis of the _WhisperGate_ activity continues. The activity is reminiscent of [VOODOO BEAR](https://falcon.crowdstrike.com/intelligence-v2/actors/voodoo-bear)’s destructive _NotPetya_ malware, which included a component impersonating the legitimate `chkdsk` utility after a reboot and corrupted the infected host’s Master File Table (MFT) — a critical component of Microsoft’s NTFS file system. However, the _WhisperGate_ bootloader is less sophisticated, and no technical overlap could currently be identified with VOODOO BEAR operations.

## CrowdStrike Intelligence Confidence Assessment

**High Confidence:** Judgments are based on high-quality information from multiple sources. High confidence in the quality and quantity of source information supporting a judgment does not imply that that assessment is an absolute certainty or fact. The judgment still has a marginal probability of being inaccurate. **Moderate Confidence:** Judgments are based on information that is credibly sourced and plausible, but not of sufficient quantity or corroborated sufficiently to warrant a higher level of confidence. This level of confidence is used to express that judgments carry an increased probability of being incorrect until more information is available or corroborated. **Low Confidence:** Judgments are made where the credibility of the source is uncertain, the information is too fragmented or poorly corroborated enough to make solid analytic inferences, or the reliability of the source is untested. Further information is needed for corroboration of the information or to fill known intelligence gaps.

#### Additional Resources

  * _Find out how to stop adversaries targeting your industry —[ schedule a free 1:1 intel briefing with a CrowdStrike threat intelligence expert today](https://go.crowdstrike.com/threat-intelligence-briefing.html)._
  * _Learn about the powerful, cloud-native[ CrowdStrike Falcon® platform by visiting the product webpage. ](/en-us/endpoint-security-products/)_
  *  _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) to see for yourself how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)