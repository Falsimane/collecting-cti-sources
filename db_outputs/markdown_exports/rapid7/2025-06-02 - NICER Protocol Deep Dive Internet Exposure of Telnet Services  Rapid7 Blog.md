# NICER Protocol Deep Dive: Internet Exposure of Telnet Services | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/08/21/nicer-protocol-deep-dive-internet-exposure-of-telnet-services/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## Telnet (TCP/23)

It wasn't the first console protocol, but it's the stickiest.

### TLDR

**WHAT IS IT?**  
One of the oldest remote console applications in use today on the internet.

**HOW MANY?**  
2,829,555 discovered nodes  
389,528 (13.7%) have Recog fingerprints for 36 total service families

**VULNERABILITIES:**  
Oddly, there are few remote code execution-style vulnerabilities, but plenty of default credentials and opportunities to eavesdrop on the same.

**ADVICE:**  
Never, ever expose Telnet to the internet.

**ALTERNATIVES:**  
SSH (Secure Shell) is the most straightforward alternative to Telnet, but consider the wisdom of exposing console access to the internet in the first place.

**GETTING:**  
Better! There was a 13% reduction from 2019 exposure.

#### Discovery details

Way back in RFC 15 (September 1969), Telnet was first described as “a shell program around the network system primitives, allowing a teletype or similar terminal at a remote host to function as a teletype at the serving host.” It is obvious from this RFC that this was intended to be a temporary solution and that "more sophisticated subsystems will be developed in time," but to borrow from Milton Friedman, there is nothing quite so permanent as a temporary solution. Remote console access is still desirable over today's internet, and since Telnet gets the job done at its most basic level, it persists to this day, 50 years later.

## Exposure information

Technically, despite its half-century of use, Telnet (as a server) has suffered relatively few killer vulnerabilities; a quick search of the CVE corpus finds only 10 vulnerabilities with a CVSS score of 5 or higher. However, Telnet suffers from a few foundational flaws. For one, it is nearly always a cleartext protocol, which exposes both the authentication (username and password) and the data to passive eavesdropping. It's also relatively easy to replace commands and responses in the stream, should attackers find themselves in a privileged position to [man-in-the-middle (MITM)](/fundamentals/man-in-the-middle-attacks/) the traffic. Essentially, Telnet makes little to no security assurances at all, so paradoxically, the code itself tends to remain relatively vulnerability-free.

The bigger issue with Telnet is the fact that, in practice, default usernames and passwords are so common that it's assumed to be the case whenever someone comes across a Telnet server. This is the central hypothesis of the Mirai worm of 2016, which used an extremely short list of common default Telnet usernames and passwords and, for its trouble, managed to take down internet giants like Twitter and Netflix, practically by accident.

The chart below shows that China alone has a pretty serious Telnet problem, followed by Argentina and the United States.

![telnet-top-10.png](https://www.rapid7.com/cdn/images/blt05c00684b25fcd1e/683de89b4b2b7fa9b4e163a7/telnet-top-10.png)

While we would prefer to see no Telnet among cloud service providers, we see that good progress seems to have been made here. Microsoft Azure tops the list with about 7,000 exposures, which is a little weird since Windows platforms don't normally have a built-in Telnet server.

![telnet-top-10-cloud.png](https://www.rapid7.com/cdn/images/blt6155152812a162e8/683de8b03323a5304280ab89/telnet-top-10-cloud.png)

Of the Telnet instances found on the internet that we could confidently identify by vendor, the table below describes those services from vendors that appear in [Sonar](/research/project-sonar/) (Rapid7’s security research project that conducts internet-wide scans across different services and protocols to gain insight into global exposure to common vulnerabilities) with at least 10,000 responsive nodes.

Vendor| Count  
---|---  
Cisco| 278,472  
Huawei| 108,065  
MikroTik| 73,511  
HP| 70,821  
Ruijie| 17,565  
ZTE| 15,558  
  
What's interesting about these figures is that we can see right away that the vast majority of Telnet services exposed to the internet are strongly associated with core networking gear vendors. Cisco and Huawei, two of the largest router manufacturers on Earth, dominate the total count of all Telnet services. Furthermore, sources indicate that about 14% of Cisco devices and 11% of Huawei devices are accessible, today, using default credentials. This lack of care and maintenance of the backbone of thousands of organizations the world over is disappointing, and every one of these devices should be considered compromised in some way, today.  


While Telnet is still prevalent far and wide across the internet, we can see that some ISPs are more casual about offering this service than others. The table below shows those regional ISPs that are hosting 10,000 or more Telnet services in their network. Furthermore, the vast majority of these exposures are not customer-based exposures, but are hosted instead on the core routing and switching gear provided by these ISPs. This practice (or oversight), in turn, puts **all** customers’ network traffic originating or terminating in these providers at risk of compromise.

ISP/Provider| Count| Discovered ASNs Allocated To  
---|---|---  
Telecom Argentina| 1,320,360| AR  
China Telecom| 282,897| BY, CN, GB, HK  
China Unicom| 183,290| CN, GB, HK  
Tencent| 130,620| CN  
Korea Telecom| 81,392| KR  
Cox Communications| 78,442| US  
Arteria Networks| 68,598| JP  
LG UPlus| 56,434| KR  
British Telecom| 53,020| GB, NL  
AT&T| 43,517| BR, CZ, DM, MR, RO, TH, US  
HiNet| 42,150| TW  
Guangdong Mobile| 39,197| CN  
Claro| 37,469| BR, CL, ES, MX, PA  
Uninet| 37,204| AZ, MX  
VNPT| 35,640| VN  
China Mobile| 35,247| CN, HK, RU  
Hathway IP Over Cable Internet| 33,428| IN  
Telefonica Brazil| 30,270| BR  
Columbia Telecom| 27,865| RU  
CenturyLink| 26,998| US  
NTT Communications| 26,757| AU, BR, HK, JP, MM, MY, SG, US  
Total Pay Telecom| 26,448| MX  
Alestra| 23,679| MX  
Algar| 23,546| BG, BR  
Charter Communications| 23,124| US  
Irideos| 22,570| IT  
RCS & RDS| 22,422| RO  
Indonesia Telecom| 19,920| ID  
Rostelecom| 19,597| RU  
Orange| 19,562| BD, BE, BF, BR, CD, CF, CI, CM, ES, EU, FR, GN, GW, IN, MD, MG, ML, NE, PL, RO, RU, SK, TN, UG  
Corbina Telecom| 19,071| RU  
Vodafone| 18,760| AU, CZ, DE, EG, ES, EU, FJ, GB, GH, GR, HU, IE, IN, IS, IT, MT, NL, NZ, PT, QA, RO, TR  
Daisy Communications| 18,028| GB  
FreeBit Co.,Ltd.| 17,590| JP  
Turk Telekom| 17,446| TR  
Telecom Italia| 17,042| IT, SM  
Triple T Broadband| 16,936| TH  
Primus Telecommunications Canada Inc| 16,732| CA  
Comcast| 15,980| DO, US  
Verizon| 15,926| GB, US, ZA  
True Internet| 15,394| TH  
Compañía Dominicana de Teléfonos S. A.| 15,317| DO  
TalkTalk| 15,120| GB  
TekSavvy Solutions Inc.| 15,041| CA  
Telefonica De Espana| 14,366| ES  
Hong Kong Broadband Network LTD| 13,839| HK  
Level 3| 13,008| BD, HK, US  
HGC Global| 12,222| HK  
SK Broadband| 11,972| KR  
Cable & Wireless| 11,550| EU, GB, PA, SC  
  
## Attacker’s view

Telnet’s complete lack of security controls, such as strong authentication and encryption, makes it totally unsuitable for the internet. Hiding Telnet on a non-standard port is also generally useless, since modern Telnet scanners are all too aware of Telnet lurking on ports like 80 and 443, simply because firewall rules might prohibit port 23 exposure. Today, Telnet is most commonly associated with low-quality IoT devices with weak to no security hardening, so exposing these devices to the internet is, at the very least, a signal that there is no security rigor in that organization.

Judging from our honeypot network ([Project Lorelei](/research/project-lorelei/)), attackers continue to actively seek out Telnet services, even four years after the Mirai attacks that took several hundred thousand offline. Approximately 90% of the traffic shown below represents basic access attempts using common usernames and passwords. The spikes represent concentrated credential stuffing attacks, using new username and password combinations pulled from publicly available dumps of other credentials.

![telnet-heisenberg-activity.png](https://www.rapid7.com/cdn/images/blt6fb6405a26d7c0f9/683de8c92cfe32308bdc18b1/telnet-heisenberg-activity.png)

## Our advice

**IT and IT security teams** should prohibit Telnet traffic both to and from their networks, both through blocking standard Telnet ports and through deep packet inspection (DPI) solutions, whenever possible. They should continuously monitor their network for Telnet services, and track down offending devices and disable Telnet connectivity. There is no reason to expose Telnet to the modern internet, ever. In the rare case a network operator wants someone to log in to a text-based console over the internet, a well-maintained SSH server will be far more reliable, flexible, and secure.

**Cloud providers** should operate similarly to the above organizations. They should, by default, prohibit all Telnet traffic through automatic, technical means. It's possible that some customers are relying on Telnet today, but those customers should be gently, but firmly, moved to SSH-based alternatives. After all, Telnet clients are not available by default on modern versions of Windows, OSX, or Ubuntu Linux for a reason, so it would seem that few future clients will suffer from its absence on their hosted machines.

**Government cybersecurity agencies** should actively pursue those ISPs that are offering an egregious amount of Telnet access to their core network operations hardware, and give those operators a stern talking-to, along with migration documentation on how to set up SSH, if needed. ISPs, at this point, should know better.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)