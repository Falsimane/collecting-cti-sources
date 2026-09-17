# Remote Desktop Protocol (RDP) Exposure | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2017/08/09/remote-desktop-protocol-exposure/
- **Date :** 2025-06-02

---

The Remote Desktop Protocol, commonly referred to as RDP, is a proprietary protocol developed by Microsoft that is used to provide a graphical means of connecting to a network-connected computer. RDP client and server support has been present in varying capacities in most every Windows version since [NT](https://en.wikipedia.org/wiki/Windows_NT). Outside of Microsoft's offerings, there are RDP clients available for most other operating systems. If the nitty gritty of protocols is your thing, Wikipedia's [Remote Desktop Protocol](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol) article is a good start on your way to a trove of TechNet articles.

RDP is essentially a protocol for dangling your keyboard, mouse and a display for others to use. As you might expect, a juicy protocol like this has a variety of knobs used to control its security capabilities, including controlling user authentication, what encryption is used, and more. The default RDP configuration on older versions of Windows left it vulnerable to several attacks when enabled; however, newer versions have upped the game considerably by requiring Network Level Authentication (NLA) by default. If you are interested in reading more about securing RDP, UC Berkeley has put together a helpful [guide](https://security.berkeley.edu/resources/best-practices-how-articles/securing-remote-desktop-rdp-system-administrators), and Tom Sellers, prior to joining Rapid7, [wrote](https://fadedlab.wordpress.com/2015/05/23/hardening-microsoft-remote-desktop-services-rds/) about specific risks related to RDP and how to address them.

RDP's history from a security perspective is varied. Since at least 2002 there have been 20 Microsoft security updates specifically related to RDP and at least 24 separate CVEs:

  * [MS99-028: Terminal Server Connection Request Flooding Vulnerability](/db/vulnerabilities/WINDOWS-HOTFIX-MS99-028)
  * [MS00-087: Terminal Server Login Buffer Overflow Vulnerability](/db/vulnerabilities/WINDOWS-HOTFIX-MS00-087)
  * [MS01-052: Invalid RDP Data Can Cause Terminal Service Failure](/db/vulnerabilities/windows-hotfix-ms01-052)
  * [MS02-051: Cryptographic Flaw in RDP Protocol can Lead to Information Disclosure](/db/vulnerabilities/WINDOWS-HOTFIX-MS02-051)
  * [MS05-041: Vulnerability in Remote Desktop Protocol Could Allow Denial of Service](/db/vulnerabilities/WINDOWS-HOTFIX-MS05-041)
  * [MS09-044: Vulnerabilities in Remote Desktop Connection Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS09-044)
  * [MS11-017: Vulnerability in Remote Desktop Client Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS11-017)
  * [MS11-061: Vulnerability in Remote Desktop Web Access Could Allow Elevation of Privilege](/db/vulnerabilities/WINDOWS-HOTFIX-MS11-061)
  * [MS11-065: Vulnerability in Remote Desktop Protocol Could Allow Denial of Service](/db/vulnerabilities/WINDOWS-HOTFIX-MS11-065)
  * [MS12-020: Vulnerabilities in Remote Desktop Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS12-020)
  * [MS12-036: Vulnerability in Remote Desktop Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS12-036)
  * [MS12-053: Vulnerability in Remote Desktop Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS12-053)
  * [MS13-029: Vulnerability in Remote Desktop Client Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS13-029)
  * [MS14-030: Vulnerability in Remote Desktop Could Allow Tampering](/db/vulnerabilities/WINDOWS-HOTFIX-MS14-030)
  * [MS14-074: Vulnerability in Remote Desktop Protocol Could Allow Security Feature Bypass](/db/vulnerabilities/WINDOWS-HOTFIX-MS14-074)
  * [MS15-030: Vulnerability in Remote Desktop Protocol Could Allow Denial of Service](/db/vulnerabilities/WINDOWS-HOTFIX-MS15-030)
  * [MS15-067: Vulnerability in RDP Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS15-067)
  * [MS15-082: Vulnerabilities in RDP Could Allow Remote Code Execution](/db/vulnerabilities/WINDOWS-HOTFIX-MS15-082)
  * [MS16-017: Security Update for Remote Desktop Display Driver to Address Elevation of Privilege](/db/vulnerabilities/WINDOWS-HOTFIX-MS16-017)
  * [MS16-067: Security Update for Volume Manager Driver](/db/vulnerabilities/WINDOWS-HOTFIX-MS16-067)



In more recent times, the Esteemaudit exploit was found as part of [the ShadowBrokers leak](/blog/post/2017/04/18/the-shadow-brokers-leaked-exploits-faq/) targeting RDP on Windows 2003 and XP systems, and was perhaps the reason for the most recent RDP vulnerability addressed in [CVE-2017-0176](/db/vulnerabilities/msft-cve-2017-0176).

RDP is disabled by default for all versions of Windows but is very commonly exposed in internal networks for ease of use in a variety of duties like administration and support. I can't think of a place where I've worked where it wasn't used in some capacity. There is no denying the convenience it provides.

RDP also finds itself exposed on the public internet more often than you might think. Depending on how RDP is configured, exposing it on the public internet ranges from suicidal on the weak end to not-too-unreasonable on the other. It is easy to simply suggest that proper firewall rules or ACLs restricting RDP access to all but trusted IPs is sufficient protection, but all that extra security only gets in the way when Bob-from-Accounting's IP address changes weekly. Sure, a VPN might be something that RDP could hide behind and be considerably more secure, but you could also argue that a highly secured RDP endpoint on the public internet is comparable security-wise to a VPN. And when your security-unsavvy family members or friends need help from afar, enabling RDP is definitely an option that is frequently chosen. There have also been reports that scammers have been using RDP as part of their attacks, often convincing unwary users to enable RDP so that “remote support” can be provided. As you can see and imagine, there are all manner of ways that RDP could end up exposed on the public internet, deliberately or otherwise.

It should come as no surprise, then, to learn that we've been doing some poking at the global exposure of RDP on the public IPv4 internet as part of Rapid7 Labs' [Project Sonar](https://sonar.labs.rapid7.com/). Labs first looked at the abuse of RDP from a honeypot's perspective as part of the [Attackers Dictionary research](https://information.rapid7.com/attackers-dictionary.html) published last year. Around the same time, in early 2016, Sonar observed 10.8 million supposedly open RDP endpoints. As part of the research for Rapid7's [2016 National Exposure Index](https://information.rapid7.com/national-exposure-index.html), we observed 9 million and 9.4 million supposedly open RDP endpoints in our two measurements in the second quarter of 2016. More recently, as part of the 2017 National Exposure Index, in the first quarter of 2017, Sonar observed 7.2 million supposedly open RDP endpoints.

Exposing an endpoint is one thing, but actually exposing the protocol in question is where the bulk of the risk comes from. As part of running Sonar, we frequently see a variety of honeypots, tarpits, IPs or other security devices that will make it appear as if an endpoint is open when it really isn't—or when it really isn't speaking the protocol you are expecting. As such, I'm always skeptical of these initial numbers. Surely there aren't really 7-10 million systems exposing RDP on the public internet. Right?

Recently, we launched a Sonar study in order to shed more light on the number of systems actually exposing RDP on the public internet. We built on the previous RDP studies which were simple [zmap](https://zmap.io/) SYN scans, followed up with a full connection to each IP that responded positively and attempted the first in a [series of protocol exchanges](https://msdn.microsoft.com/en-us/library/cc240452.aspx) that occur when an RDP client first contacts an RDP server. This simple, preliminary protocol negotiation mimics what modern RDP clients perform and is similar to what [Nmap](https://raw.githubusercontent.com/nmap/nmap/master/nmap-service-probes) uses to identify RDP. This 19-byte RDP negotiation request should elicit a response from almost every valid RDP configuration it encounters, from the default (less secure) settings of older RDP versions to the NLA and SSL/TLS requirements of newer defaults:

![RDP-1.png](https://www.rapid7.com/cdn/images/blt0434b857871c286d/683de9022cfe320fbadc18c7/RDP-1.png)

We analyzed the responses, tallying any that appeared to be from RDP speaking endpoints, counting both error messages indicating possible client or server-side configuration issues as well as success messages.

11 million open 3389/TCP endpoints,and 4.1 million responded in such a way that they were RDP speaking of some manner or another. This number is shockingly high when you remember that this protocol is effectively a way to expose keyboard, mouse and ultimately a Windows desktop over the network. Furthermore, any RDP speaking endpoints discovered by this Sonar study are not applying basic firewall rules or ACLs to protect this service, which brings into question whether or not any of the other basic security practices have been applied to these endpoints.

Given the myriad of ways that RDP could end up exposed on the public Internet as observed in this recent Sonar study, it is hard to say why any one country would have more RDP exposed than another at first glance, but clearly the United States and China have something different going on than everyone else:

![RDP-2.png](https://www.rapid7.com/cdn/images/bltcee0c66ce7814110/683de9162a9b687b3c2bd4bd/RDP-2.png)   
  
Looked at from a different angle, by examining the organizations that own the IPs with exposed RDP endpoints, things start to become much more clear:

![RDP-3.png](https://www.rapid7.com/cdn/images/blt03a61c018dc18ec7/683de92b237ea63d0891c4b6/RDP-3.png)

The vast majority of these providers are known to be cloud, virtual, or physical hosting providers where remote access to a Windows machine is a frequent necessity; it's no surprise, therefore, that they dominate exposure.

We can draw further conclusions by examining the RDP [responses](https://msdn.microsoft.com/en-us/library/cc240506.aspx) we received. Amazingly, over 83% of the RDP endpoints we identified indicated that they were willing to proceed with CredSSP as the security protocol, implying that the endpoint is willing to use one of the more secure protocols to authenticate and protect the RDP session. A small handful in the few thousand range selected SSL/TLS. Just over 15% indicated that they didn't support SSL/TLS (despite our also proposing CredSSP…) or that they only supported the legacy “Standard RDP Security”, which is susceptible to man-in-the-middle attacks. Over 80% of exposed endpoints supporting common means for securing RDP sessions is rather impressive. Is this a glimmer of hope for the arguably high number of exposed RDP endpoints?

Areas for potential future research could include:

  * Security protocols and supported encryption levels. Nmap has [an NSE script](https://nmap.org/nsedoc/scripts/rdp-enum-encryption.html) that will enumerate the security protocols and encryption levels available for RDP. While 83% of the RDP speaking endpoints support CredSSP, this does not mean that they don't also support less secure options; it just means that if a client is willing, they can take the more secure route.
  * When TLS/SSL or CredSSP are involved, are organizations following best practices with regard to certificates, including self-signed certificates (perhaps leading to MiTM?), expiration, and weak algorithms?
  * Exploring the functionality of RDP in non-Microsoft client and server implementations



Rapid7's [InsightVM](/products/insightvm/) and [Metasploit](/products/metasploit/) have fingerprinting coverage to identify RDP, and InsightVM has vulnerability coverage for all of the above mentioned RDP vulnerabilities.

Interested in this RDP research? Have ideas for more? Want to collaborate? We'd love to hear from you, either in the comments below or at [[email protected]](/cdn-cgi/l/email-protection#9fedfaecfafeedfcf7dfedfeeff6fba8b1fcf0f2).

## Article tags

  * [Research](/blog/tag/research/)