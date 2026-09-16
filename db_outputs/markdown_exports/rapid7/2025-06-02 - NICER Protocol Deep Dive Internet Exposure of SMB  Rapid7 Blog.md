# NICER Protocol Deep Dive: Internet Exposure of SMB | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/09/18/nicer-protocol-deep-dive-internet-exposure-of-smb/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## SMB (TCP/445)

_Choosy worms choose SMB._

#### TLDR

**WHAT IT IS:** SMB is the Windows everything protocol, but is usually used for Windows-based file transfers.

**HOW MANY:** 593,749 discovered nodes

**VULNERABILITIES:** The most destructive internet worms in history use SMB in some way.

**ADVICE:** Direct access to SMB outside of an unroutable, local network should be prohibited as a general rule.

**ALTERNATIVES:** HTTPS-based file sharing is usually the answer for whatever file hosting SMB was intending, but most SMB exposures seem to be accidental.

**GETTING:** Better! ZOMGOSH! Thanks mostly to ISPs, there was a 16% decrease in exposure from 2019.

### SMB discovery details

SMB is a continued source of heartache and headaches for network operators the world over. Originally designed to operate on local area network protocols like NetBEUI and IPX/SPX, SMBv1 was ported to the regular TCP/IP network that the rest of the internet runs on. Since then, SMBv2 and SMBv3 have been released. While SMB is primarily associated with Windows-based computers for authentication, file sharing, print services, and process control, SMB is also maintained for non-Windows operating systems in implementations such as Samba and Netsmb. As a binary protocol with negotiable encryption capabilities, it is a complex protocol. This complexity, along with its initial proprietary nature and deep couplings with the operating system kernel, makes it an ideal field for discovering security vulnerabilities that can enable remote code execution (RCE). On top of this, the global popularity of Windows as a desktop operating system ensures it remains a popular target for bug hunters and exploiters alike.

![smb-1.png](https://www.rapid7.com/cdn/images/blt9fe74e1c19ae82be/683de529da5c306cf8a83624/smb-1.png) ![smb-2.png](https://www.rapid7.com/cdn/images/blt7d15b8b601bf2731/683de54a2cfe321abfdc178c/smb-2.png)

### Exposure information

Many of the most famous vulnerabilities, exploits, and in-the-wild worms have leveraged SMB in some way. WannaCry and [NotPetya](/security-response/petya/) are two of the most recent events that centered on SMB, both for exploitation and for transmission. Prior SMB-based attacks include the Nachi and Blaster worms (2003–2005), and future SMB-based attacks will likely include [SMBGhost](https://attackerkb.com/topics/2LCXe3EPAZ/cve-2020-0796---smbghost). In addition to bugs, intended features of SMB—notably, automatic hash-passing—make it an ideal mechanism to steal password hashes from unsuspecting victims, and SMB shares (network-exposed directories of files) continue to be accidentally exposed to the internet via server mismanagement and too-easy-to-use network-attached storage (NAS) devices.

As expected, the preponderance of SMB services available on the internet are Windows-based, but the table below shows there is also a sizable minority of non-Windows SMB available.

SMB Server Kind| Count  
---|---  
Windows (Server)| 298,296  
Linux/Unix/BSD/SunOS (Samba)| 170,095  
Windows (Desktop)| 110,340  
QNAP NAS Device| 10,164  
Other/Honeypot| 1,914  
Apple Time Capsule or macOS| 1,465  
Windows (Embedded)| 703  
Keenetic NAS| 647  
Printer| 386  
Zyxel NAS| 6  
EMC NAS| 5  
  
As you can see, these non-Windows nodes are typically some type of NAS system used in otherwise largely Windows environments, and are responsible for maintaining nearline backup systems. While these devices are unlikely to be vulnerable to exactly the same exploits that dog Windows systems, the mere fact that these **backups are exposed to the internet** means that, eventually, these network operators are Going To Have A Bad Time if and when they get hit by the next wave of ransomware attacks.

### Unattended installs

Of the Windows machines exposed to the internet, we can learn a little about their provenance from the Workgroup strings that we're able to see from [Sonar scanning](/research/project-sonar/). The list below indicates that the vast majority of these machines are using the default WORKGROUP workgroup, with others being automatically generated as part of a standard, unattended installation. In a magical world where SMB is both rare and safe to expose to the internet, we would expect those machines to be manually configured and routinely patched.

This is not the case, though—these Windows operating systems were very likely installed and configured automatically, with no special care given to their exposed-to-the-internet status, so the [exposure](/fundamentals/what-is-exposure-management/) is almost certainly accidental and not serving some special, critical business function. Additionally, these aftermarket-default WORKGROUPS are also giving away hints about which specific Windows- or Samba-based build is being used in production environments, and can give attackers ideas about targeting those systems.

Workgroup| Count  
---|---  
WORKGROUP| 204,014  
WIN-<string e.g. 4RGO6K0U19F>| 98,153  
MICROSO-<string e.g. HCBD8KK>| 27,213  
SERVER[####]| 15,721  
HK-<number e.g. 2723>| 12,823  
IP Address| 10,367  
DESKTOP-<string e.g. HUDL8UO>| 7,203  
HKSRV[####]| 6,160  
RS-<string e.g. A2-084| 6,017  
XR-<string e.g. 20190714REWT>| 4,448  
QNSERVER[####]| 4,067  
PC-<string e.g. HCBD8KK>| 4,034  
CCSERVER[####]| 3,807  
SVR-<number e.g. 20191106VUM>| 3,303  
MYGROUP| 3,269  
MSHOME| 3,060  
SRV*| 2,910  
SERVER| 2,476  
VM*| 2,186  
TKO[####]| 2,088  
  
### Attacker’s view

Regardless of the version and configuration of cryptographic and other security controls, SMB is inappropriate for today's internet. It is too complex to secure reliably, and critical vulnerabilities that are attractive to criminal exploitation continue to surface in the protocol. With that said, SMB continues to be a critical networking layer in office environments of any size, and since it’s native to TCP/IP, network misconfigurations can inadvertently expose SMB-based resources directly to the internet. **Every organization should be continually testing its network ingress and egress filters for SMB traffic** —not only to prevent outsiders from sending SMB traffic to your accidentally exposed resources, but to prevent internal users from accidentally leaking SMB authentication traffic out into the world.

Approximately 640,000 unique IP addresses visited our high-interaction SMB honeypots over the measured period, but rather than think of this as a horde of SMB criminals, we should recall that the vast majority of those connections are from machines on the internet that were, themselves, compromised. After all, that's how worms work. Very few of these connections were likely sourced from an attacker's personally owned (rather than pwned) machine. With this in mind, our honeypot traffic gives us a pretty good idea of which countries are, today, most exposed to the next SMB-based mega-worm like WannaCry: Vietnam, Russia, Indonesia, Brazil, and India are all at the top of this list.

![smb-3.png](https://www.rapid7.com/cdn/images/blt57fd45ada99629d4/683de5703323a5ac9080aa7f/smb-3.png)

Among the cloud providers, things are more stark. EternalBlue, the exploit underpinning WannaCry, was responsible for about 1.5 million connections to our honeypots from Digital Ocean, while Microsoft Azure was the source of about 8 million (non-EternalBlue) connections (of which, about 15%, or 1.2 million or so, were accidental connections due to a misconfiguration at Azure). We're not yet sure why this wild discrepancy in attack traffic versus accidental traffic exists between Digital Ocean and Azure, but we suspect that Microsoft is much more aggressive about making sure the default offerings at Azure are patched against MS17-010, while Digital Ocean appears to be more hands-off about patch enforcement, leaving routine maintenance to its user base.

![smb-4.png](https://www.rapid7.com/cdn/images/blt5cf0deb24350112b/683de59b4c5a09327e5e0caf/smb-4.png)

### Our advice

**IT and IT security teams** should prohibit SMB access to, or from, their organization over anything but VPN-connected networks, and regularly scan their known, externally facing IP address space for misconfigured SMB servers. 

**Cloud providers** should prohibit SMB access to cloud resources, and at the very least, routinely scrutinize SMB access to outside resources. Given that approximately 15% of our inbound honeypot connections over SMB from Microsoft Azure are actually misconfigurations, rather than attacks or research probes, Azure should be especially aware of this common flaw and make it difficult to impossible to accidentally expose SMB at the levels that are evident today.

**Government cybersecurity agencies** should be acutely aware of their own national exposure to SMB, and institute routine scanning and notification programs to shut down SMB access wherever it surfaces. This is especially true for those countries that are at the top of our honeypot source list.

  


## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)