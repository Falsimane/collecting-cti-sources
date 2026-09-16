# NICER Protocol Deep Dive: Internet Exposure of FTP | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/09/04/nicer-protocol-deep-dive-internet-exposure-of-ftp/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## FTP (TCP/21)

_A confusing data channel negotiation sequence and totally cleartext—what could go wrong?_

### TLDR

**WHAT IT IS:** FTP was first standardized in RFC 114, and like most protocols of that era, it relies on cleartext exchanges for authentication and data transfer. Traditionally, FTP uses TCP/21 as its control channel, and the client and server negotiates a second channel for the actual data transfer in either “active” or “passive” modes, thus confounding an entire generation of firewall administrators.

**HOW MANY:** 12,991,544 discovered nodes  
6,645,633 (51%) have Recog fingerprints (20 total service families)

**VULNERABILITIES:** The majority of the fingerprinted versions have DoS and auth/unauth RCE-documented vulnerabilities with associated exploit code, and some have documented backdoors.

**ADVICE:** All of the above arguments against Telnet apply to FTP. When you discover FTP on a publicly exposed network, you can be fairly certain the organization involved is running on an ancient legacy of public computing and does not enjoy the benefits of a mature security program.

**ALTERNATIVES:** Today, there are several useful alternatives to FTP. SFTP is essentially FTP wrapped in SSH, while FTP/S is wrapped in an SSL layer much like HTTPS. For file transferring in general, SCP and rsync over SSH tunnelling are perfectly delightful solutions, and of course, HTTPS-based file sharing applications are well established in today's enterprise networks the world over. This is all to say, there is no good reason to stick with this legacy protocol.

**GETTING:** Stuck. There was no statistically significant change over 2019.

### Discovery details

[FTP](https://tools.ietf.org/html/rfc354) (the TCP/21 variant) dates back to 1972 and was intended “to satisfy the diverse needs of users of maxi-HOSTs, mini-HOSTs, TIPs, and the Datacomputer, with a simple, elegant, and easily implemented protocol design.” It is a cleartext, short command-driven protocol that has truly outlived its utility, especially now that the two main browser developers (Google and Mozilla) are dropping or have dropped support for it.

![ftp-top-10-countries.png](https://www.rapid7.com/cdn/images/blt4ca8f7b71899e138/683ddd1c3323a516c380a7cd/ftp-top-10-countries.png)

Project Sonar found just under 13 million active FTP sites (12,991,544), which is down from over 20 million from our previous National Exposure Index study. The United States leads the pack when it comes to exposing FTP to the internet with ~3.9 million hosts awaiting your OPEN.

![FTP-cloud-provider.png](https://www.rapid7.com/cdn/images/blt698e9bef4026f650/683ddd45a38fc503b6031f6e/FTP-cloud-provider.png)

Somewhat surprisingly, there is a large FTP presence in cloud environments, with Alibaba, Amazon, OVH, and Azure hosting around 13.5% of discovered nodes.

When we looked into this a bit more, we discovered that Alibaba generously provides detailed documentation on how to “Build an FTP site” on both [Linux](https://www.alibabacloud.com/help/doc-detail/92048.htm) and [Windows](https://www.alibabacloud.com/help/doc-detail/92046.htm), and that [Amazon](https://aws.amazon.com/blogs/aws/new-aws-transfer-for-ftp-and-ftps-in-addition-to-existing-sftp/) has a brand-new FTP service offering. Similarly, both [OVH](https://www.ovh.co.uk/web-hosting/ftp.xml) and [Microsoft](https://docs.microsoft.com/en-us/azure/app-service/deploy-ftp) have documentation on FTP, and OVH goes so far as to actively encourage customers to use it to manage files for their web content.

Furthermore, all the providers have base images that either ship with FTP available or easily installable (via the aforementioned helpful documentation!), so the extent of FTP exposure in cloud environments should really come as no surprise.

### FTP exposure information

In 2020, there is a single acceptable use of FTP, which is providing an [anonymous FTP](https://tools.ietf.org/html/rfc1635) download service of more or less public data. In this application, and only this application, cleartext credentials won't be exposed (but data in transit will be). Any other use should be considered insecure and unsafe, and should be avoided. Even this use case is edging into unacceptable territory, since FTP doesn't provide any native checksumming or other error checking on file transfers, making [man-in-the-middle alterations](/fundamentals/man-in-the-middle-attacks/) of any data in transit fairly trivial.  
That said, there are millions of FTP servers on the internet. We're able to [fingerprint several](https://github.com/rapid7/recog/blob/master/xml/ftp_banners.xml), and the table below illustrates with fairly high fidelity the state of the FTP universe, authenticated and anonymous alike.

Service| Count  
---|---  
Pure-FTPd| 3,102,834  
ProFTPD| 1,011,310  
IIS| 823,696  
vsFTPd| 661,034  
Bftpd| 420,023  
FileZilla FTP Server| 415,147  
Firewall-1| 66,686  
Serv-U| 55,392  
Multicraft| 29,610  
SmbFTPD| 15,800  
Gene6| 10,260  
ucftpd| 6,928  
Twisted| 6,826  
inetutils| 4,239  
WS_FTP| 4,231  
TBS FTP Server| 4,199  
AOS| 3,548  
Unified Security Gateway| 3,401  
Nepenthes (Honeypots)| 303  
JetDirect| 166  
  
Yes, you read that last line of the table correctly: 166 _printers_ are exposing their FTP service to the internet. Perhaps more disconcerting are 3,401 Ubiquiti Unified Security Gateway (firewalls) with FTP exposed. 

Fourteen of the FTP server types make it somewhat easy to fingerprint version numbers, and vsFTPd, ProFTPD, Bftpd, and Filezilla account for 95% of that corpus (which is ~2.1 million FTP servers, i.e., ~17% of exposed systems). We’ve put the top five versions of each below along with some commentary, as including the entire version summary table for each would take a few reams of e-paper.

vsFTPd| Count  
---|---  
3.0.2| 221,481  
3.0.3| 165,776  
2.2.2| 164,761  
2.0.5| 43,347  
2.3.5| 16,598  
  
 _Version 3.0.3 is current and appears safe from an RCE perspective, but 3.0.2 has_[ _one moderate remote exploit CVE_](https://attackerkb.com/topics/SLwQqWdCzX/cve-2015-1419) _. Version 2.2.2 dates back to 2011 and has a_[ _DoS CVE_](https://attackerkb.com/topics/pMUfmyuiTA/cve-2011-0762) _. Version 2.0.5 harkens back to 2008 with an_[ _edgy, remote (authenticated) CVE_](https://attackerkb.com/topics/nqTIyFr916/cve-2007-5962) _._

ProFTPD| Count  
---|---  
1.3.5a| 118,672  
1.3.5b| 100,941  
1.3.4a| 59,089  
1.3.5| 57,364  
1.3.5e| 45,756  
  
 _Three most prevalent versions of ProFTPD—1.3.5/a/b—just happen to have a_[ _super-dangerous CVE_](https://attackerkb.com/topics/1Qhi2ndx91/cve-2015-3306) _that allows remote attackers to read and write arbitrary files. 1.3.4.a has a nasty_[ _DoS CVE_](https://attackerkb.com/topics/YdjqLThxIh/cve-2013-4359) _, followed by 1.3.5e, with a_[ _low-severity CVE_](https://attackerkb.com/topics/g2r203lfxR/cve-2017-7418) _that gives authenticated attackers the ability to reconfigure directory structures under certain configurations._

Bftpd| Count  
---|---  
2.2| 310,906  
3.8| 90,088  
1.6.6| 12,733  
4.4| 1,725  
2.2.1| 1,713  
  
 _Version 2.2 (which turns 11 years old in November) has a_[ _handy DoS CVE_](https://attackerkb.com/topics/DybJGgFgGI/cve-2009-4593) _, with the remaining ones having a_[ _memory corruption CVE_](https://attackerkb.com/topics/ShHL7hn1QT/cve-2017-16892) _exploitable by logged-in users._

FileZilla| Count  
---|---  
0.9.60 beta| 190,673  
0.9.41 beta| 138,349  
0.9.46 beta| 9,500  
0.9.59 beta| 9,030  
0.9.53 beta| 8,017  
  
 _Shockingly, the top five FileZilla versions are CVE-free, but are incredibly old._

### Attacker’s view

Project Heisenberg does not have an FTP honeypot, but we do capture all connection attempts on TCP/21, and there are often quite a few:

![ftp-heisenberg-activity.png](https://www.rapid7.com/cdn/images/blt5cf338734d1c5722/683ddd6b4c5a0947095e09d2/ftp-heisenberg-activity.png)

This activity includes attackers looking for an exploitable service on a node they can add to their C2 inventory, or both attackers and researchers searching for documents they can plunder. In either scenario, you’re much better off not giving them one more system to conquer.

### Our advice

**IT and IT security teams** should avoid using FTP (TCP/21) both internally and externally. This cleartext protocol is inherently unsafe, and there are far safer and just better modern alternatives. For system-to-system file transfers, the “S” (FTPS/SFTP) versions of FTP or (preferably) SCP are all safer and often faster replacements that have widespread client and server support. For more interactive use, there are many commercially available or open source file sharing solutions that work over HTTPS. If you truly need to FTP firmware updates to infrastructure components, you should at the very least ensure those endpoints are not internet-facing and consider putting them behind an internal VPN gateway to keep prying eyes from seeing those credentials. 

FTP should also be flagged during vulnerability sweeps and in public attack surface monitoring. During procurement processes, vendors should be asked whether their solutions support, include, or require FTP and use that information to help pick safer products and services.

**Cloud providers** should discourage use of FTP by only providing base images that do not come with FTP installed or enabled by default, rather than providing friendly and helpful documentation on how to set up a woefully insecure service. Service documentation and other instructional materials should actively discourage the use of FTP, and providers should consider performing regular service scans with associated notifications to customers when they find FTP exposed. If possible, the FTP protocol itself and/or TCP/21 should be blocked by default and definitely not be part of a standard SaaS offering.

**Government cybersecurity agencies** should provide guidance on the dangers of FTP with suggestions for alternative services. As noted in the Exposure section, there are unauthenticated RCE vulnerabilities in a sizable population of internet-facing FTP systems, making them choice targets for attackers and an inherent weakness in public infrastructure of each country with exposed FTP services.

  


## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)