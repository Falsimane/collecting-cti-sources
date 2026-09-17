# Operation Quicksand

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/operation-quicksand/
- **Date :** 2020-10-15

---

During September 2020, we identified a new campaign targeting many prominent Israeli organizations. The campaign was attributed to the Iranian threat actor ‘MuddyWater’ (also known as TEMP.Zagros, Static Kitten and Seedworm). **MuddyWater was previously exposed as a contractor for the IRGC (Islamic Republic Guard Corps).**

**ClearSky and Profero** comprehensively researched this campaign. During the campaign, the group attempted to install a variant of the “PowGoop”, a malicious replacement to Google update dll. Based on PaloAlto report[1], “PowGoop” is a loader for a variant of Thanos ransomware with destructive capabilities.

Read the full report: [Operation Quicksand – MuddyWater’s Offensive Attack Against Israeli Organizations](https://www.clearskysec.com/wp-content/uploads/2020/10/Operation-Quicksand.pdf)

**We assess that the group is attempting to employ destructive attacks (the likes of the NotPetya attack from 2017), via a disguised as ransomware attacks**. Although we didn’t see execution of the destruction in the wild, due to the presence of the destructive capabilities, the attribution to nation-state sponsored threat actor, and the realization of this vector in the past, a destructive purpose is more likely than a ransomware that is being deployed for financial goals.

On September 4th, PaloAlto published a report about this destructive variant of Thanos ransomware without attributing it to any known threat actor. However, the organizations that were targeted in the campaign were state-run organizations in the Middle East and North Africa. The loader of this variant dubbed ‘PowGoop’, is a fake Google Update mechanism and was attributed to MuddyWater based on code similarities with the MoriAgent / PudPoul dll loader.

In our analysis, we identified two primary attack vectors:

  * The first vector entailed sending a malicious decoy document (PDF or Excel) that communicates over OpenSSL with a malicious C2 server and downloads files, which later deploy the “PowGoop” payload.
  * The second vector involves exploiting CVE-2020-0688 and deploying the same payload via aspx file (WebShell). The attacker will create an internal socket tunneling between compromised machines in the network. The attacker used a modified SSF (Socket) for it. Then, the attacker downloads the PowGoop as well. Recently, Microsoft revealed that MuddyWater had been leveraging the ZeroLogon vulnerability as well (CVE-2020-1472)[1].



In ‘Operation Quicksand’ we uncovered the first known instance of a potentially destructive attack executed by MuddyWater, focusing on prominent organizations in Israel and in other countries around the world. 

![](https://www.clearskysec.com/wp-content/uploads/2020/10/image-1-550x51.png)

We identified a repetitive PDB path in the networks that were researched containing the word ‘Covic’. This may indicate a **covid-19** inspiration and suggests the possible dates in which MuddyWater might have developed the malware.

* * *

[1] <https://www.zdnet.com/article/microsoft-says-iranian-hackers-are-exploiting-the-zerologon-vulnerability/>

* * *

[1] <https://unit42.paloaltonetworks.com/thanos-ransomware/>