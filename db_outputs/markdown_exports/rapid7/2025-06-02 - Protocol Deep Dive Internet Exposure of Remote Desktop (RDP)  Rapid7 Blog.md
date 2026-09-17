# Protocol Deep Dive: Internet Exposure of Remote Desktop (RDP) | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/10/23/nicer-protocol-deep-dive-internet-exposure-of-remote-desktop-rdp/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## Remote Desktop — RDP (3389)

_It's like VNC, but more Microsofty._

### TLDR

**WHAT IT IS:** A proprietary protocol developed by Microsoft for making graphical user interface (GUI) connections from one system to another. The default port is TCP/3389, but it can be hosted on any open port.

**HOW MANY:** 3,979,356 discovered nodes. 44,540 (1.1%) have Recog operating system fingerprints. 3,974,474 (99.8%) have Recog fingerprints for security scheme

**VULNERABILITIES:** Numerous remote code execution issues including [CVE-2019-0708 (BlueKeep)](https://attackerkb.com/topics/huQasjoVMS/windows-remote-desktop-rdp-use-after-free-vulnerablility-bluekeep) disclosed by Microsoft in the spring of 2019.

**ADVICE:** Place RDP behind a VPN connection if it needs to be “always on.” If RDP can be made intermittently available, ensure all nodes exposing RDP are fully patched, hardened to recommended specifications, and utilize multi-factor authentication.

**ALTERNATIVES:** This is Microsoft’s recommended solution for remotely accessing remote systems. It does what it says on the tin pretty well, so there are no real alternatives. If you need this type of access, follow the guidance in the Advice section.

**GETTING:** Slightly better! We saw almost 5% fewer RDP than we measured in 2019.

### Discovery details

[Project Sonar](/research/project-sonar/) found just under 4 million active RDP nodes, with over a quarter of them in China-homed networks.

![rdp-1.png](https://www.rapid7.com/cdn/images/blt388986e8c16f8d21/683de445da5c30672ca835c0/rdp-1.png)

Unsurprisingly, we also find about a quarter of RDP nodes within our in-scope cloud provider networks—after all, one does need to connect to these remote systems to use them—though we would have expected Microsoft Azure to take the top spot (given, y’know, “Windows”). So, imagine our surprise when we found Azure-hosted RDP came in third. It's a strong third place, though, behind the twin cloud giants Amazon and Alibaba.

RDP is everywhere, with a total population an order of magnitude more than VNC (about 4 million and change versus less than 400,000 for VNC). Apart from the aforementioned “cloud” use case, small businesses use it off of business-class ISP connections; enterprises use it for remote access and administration; retail operations often have RDP enabled on point-of-sale systems for routine management; and, home users, too, find it easy enough to use to take the time to poke holes in their firewalls to enable remote access to home PCs. This ubiquity, along with pervasive misconfigurations and vulnerabilities, make it an ideal target for attackers, which we’ll cover in the next section.

There are [many ways](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpbcgr/5073f4ed-1e93-45e1-b039-6e30c385867c) to configure RDP sessions, and Project Sonar is able to identify three states: “standard” or “legacy,” “network level authentication” (NLA), and transport layer security (TLS). “Standard” is a train wreck waiting to happen, and both NLA and TLS do a fairly good job securing your sessions (provided you’re patching regularly and using safe configurations with multi-factor authentication). And, from the looks of it, most residential and business-class users seem to have received that memo given the high percentage of nodes in the top 10 countries and the fact that clouds are using more secure connection options:

![rdp-2.png](https://www.rapid7.com/cdn/images/blt4303402f323330c7/683de4718ac17c13f129af2f/rdp-2.png) ![rdp-3.png](https://www.rapid7.com/cdn/images/bltbbbe1bba9c9cbf84/683de4a4cc604240762068ec/rdp-3.png)

However, all clouds are not created nearly as equal, with Oracle cloud users limping in dead last (again, by percent of nodes in that cloud) when it comes to use of safer security modes. This is likely due to the default settings when enabling RDP.

### Attacker’s view

This is one protocol we do have robust honeypot coverage for, and we’ll focus on two areas: RDP session establishment and attempts to exploit RDP via BlueKeep.

Despite predictions for cyber-doom and gloom, BlueKeep—the unauthenticated remote code execution flaw in RDP, disclosed by Microsoft in the spring of 2019—pretty much faded into the background, possibly due to folks actually patching and switching to NLA security (as we see in the country and cloud top views and in the fact that 92% of surveyed RDP nodes were using NLA). We posit that the early, and consistent, measured warnings at all levels helped keep BlueKeep from being the nightmare it could have been.

That does not mean there is no evidence of BlueKeep activity; however, we tend to see orders of magnitude more credential stuffing attempts than we do use of BlueKeep:

![rdp-4.png](https://www.rapid7.com/cdn/images/blt1c470b753ccb0f74/683de4ca73c8452bf1e8c47d/rdp-4.png)

There are four takeaways from the above figure:

  1. The BlueKeep volume is super low.
  2. The number of unique source hosts with malicious intent is low.
  3. RDP activity is a constant.
  4. Attackers thought they might get lucky right around the time the U.S. entered lockdown because of the 2020 pandemic.



Between Jan. 1, 2020, and April 30, 2020, Heisenberg caught just over 8,500 distinct source IP addresses trying to use either BlueKeep-based exploits or perform credential stuffing against our honeypot network. Eleven percent (11%) of these unique IPv4 addresses originate from DigitalOcean, but 16% of all malicious RDP traffic comes from Hostkey, a hosting provider in the Netherlands. While those two network sources do stand out, 1,310 distinct autonomous systems (ASes) are hosting sources with malicious intent, so there are plenty of places to wag one’s chastisement finger at.

### Our advice

**IT and IT security teams** should strongly consider putting RDP behind a VPN if they are heck-bent on using RDP for GUI remote access. If you need to place RDP directly on the internet, consider doing so on an as-needed basis and ensuring all systems with RDP exposed are patched and have RDP configured as strongly as possible, backed by multi-factor authentication.

**Cloud providers** should have amazingly secure defaults and regularly warn users if they deploy RDP with weaker settings. Giving users the ability to easily enable RDP for only a certain period of time would go a long way toward helping thwart credential stuffing attacks. To help make the internet a bit safer, providers should also monitor for malicious traffic and work with regional CERTs to shut down malicious nodes as soon as possible.

**Government cybersecurity agencies** should continue to educate their constituents on the dangers of RDP and how to ensure safe use of RDP. Given that there are fairly well-known sources with evil intent, centers should work with regional CERTs and hosting/cloud providers and ISPs to make it easier to stop bad traffic before it compromises remote hosts.

  


## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)