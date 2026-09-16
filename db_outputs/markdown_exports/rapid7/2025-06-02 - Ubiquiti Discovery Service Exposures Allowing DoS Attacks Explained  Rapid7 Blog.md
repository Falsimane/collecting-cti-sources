# Ubiquiti Discovery Service Exposures Allowing DoS Attacks Explained | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/02/01/ubiquiti-discovery-service-exposures/
- **Date :** 2025-06-02

---

## Introduction

On Jan. 29, the Rapid7 Labs team was informed of an [interesting tweet](https://twitter.com/troutman/status/1090212243197870081) by Jim Troutman indicating that Ubiquiti devices were being exploited and used to conduct [denial-of-service (DoS) attacks](/fundamentals/denial-of-service-attacks) using a service on 10001/UDP. Quick sleuthing by the security community showed that this issue has been [brewing since the summer of 2018](https://community.ubnt.com/t5/airMAX-General-Discussion/Possible-Exploit-Losing-access-to-SSH-and-HTTP-HTTPS-on-CPEs/td-p/2411064). [Ubiquiti recently acknowledged](https://community.ubnt.com/t5/airMAX-General-Discussion/airOS-airMAX-and-management-access/td-p/2654023) that this was an issue, has released a workaround, and is in the process of putting together an official fix.

Research has learned that this service is used for a variety of things, including device discovery to facilitate easily locating of Ubiquiti devices in a managed environment. At least this portion of the protocol is quite simple, requiring a simple 4-byte message that elicits a large response including the name, model, firmware version, IPs, MACs, and sometimes the ESSID if it is a wireless device of some manner. A simple POC of this functionality can be seen below when run against a mostly default Ubiquiti mFi device:
    
    
    $  echo -ne "\x01\x00\x00\x00" | socat -t 1 udp:10.6.67.25:10001 - | hexdump -C
    00000000  01 00 00 5b 02 00 0a f0  9f c2 4c 50 51 0a 06 43  |...[......LPQ..C|
    00000010  19 01 00 06 f0 9f c2 4c  50 51 0a 00 04 00 7e da  |.......LPQ....~.|
    00000020  da 0b 00 09 6d 46 69 34  63 35 30 35 31 0c 00 03  |....mFi4c5051...|
    00000030  50 38 55 0d 00 00 0e 00  01 02 03 00 22 4d 46 2e  |P8U........."MF.|
    00000040  61 72 39 33 33 78 2e 76  32 2e 30 2e 32 35 2e 31  |ar933x.v2.0.25.1|
    00000050  32 33 38 2e 31 34 30 36  32 34 2e 31 33 35 36     |238.140624.1356|
    

Because this is UDP, this protocol unfortunately suffers from UDP amplification vulnerabilities, as [warned previously by Rapid7](/blog/post/2016/10/31/understanding-udp-amplification-vulnerabilities-through-rapid7-research/) and [US-CERT](https://www.us-cert.gov/ncas/alerts/TA14-017A), among others. The amplification factor is 30-35x but does not appear to suffer from multi-packet responses, at least with what is known today. With such a large quantity of potentially vulnerable devices exposed, a DoS harnessing the available bandwidth and power of these systems could be used to conduct an attack in excess of 1Tbps, which is a crippling amount of traffic to all but the most fortified infrastructure.

It is unclear what other capabilities exist in this service, but it would not be surprising if there were other management capabilities baked in or nearby.

## Exposure

In order to understand more about this issue and inform fellow defenders in the information security community, we performed a [Sonar](https://sonar.labs.rapid7.com) study of port 10001/UDP, where we collected and analyzed the responses by parsing out the distinct fields returned in UDP payload. This showed 498,624 unique IPv4s with port 10001/UDP open, 487,021 unique IPv4s confirmed to be speaking this discovery protocol, and 486,388 unique physical devices based on MAC address tuples found in the responses. That is a _lot_ of devices.

Examining where these devices live shows that Brazil is home to more than half of these, with large chunks in the U.S., Spain, and elsewhere:

![Geographic_Distribution.jpg](https://www.rapid7.com/cdn/images/blt1f8cc74c1a63c713/683de88c543b8d532fbf1420/Geographic_Distribution.jpg)

Similar analysis by registered owning organization shows that many of these are ISPs, many of which are probably wireless ISPs (WISPs).

By decoding the responses, we are able to learn about the nature of these devices and clues as to how or why they are exposed publicly. For example, by grouping by the model names returned by these responses, we see big clusters around all sorts of Ubiquiti models/devices:

Product| n  
---|---  
NanoStation| 172,563  
AirGrid| 131,575  
LiteBeam| 43,673  
PowerBeam| 40,092  
NanoBeam| 21,360  
NanoBridge| 20,440  
miMo| 15,115  
LiteAP| 15,035  
EdgeRouter| 10,229  
Bullet| 7,125  
Rocket| 3,284  
mFi| 2,575  
BaseStation| 2,218  
PowerStation| 2,075  
EdgeSwitch| 583  
AirFiber| 496  
AirCam| 433  
UniFi AP| 353  
Wave AC| 174  
UniFi Video Camera| 88  
EdgePoint| 86  
ToughSwitch| 79  
Unifi AC| 33  
HotSpot| 23  
LiteStation| 11  
AirFoil| 8  
IsoStation| 8  
Netonix WISP Switch| 8  
AirVision| 7  
AirRouter| 1  
SunMax| 1  
  
In some cases, the discovery response includes the ESSID of the device if it is wireless-enabled. The patterns observed seem to reinforce the smaller ISP/WISP theory, as many of them seem to map back to defaults correlating popular ISPs around the world.

By inspecting the name of the device, which will generally default to something based on the model name or whatever is configured at initial install, we see even more troubling patterns:

Name| n  
---|---  
AirGrid M5 HP| 12,299  
UBNT| 9,249  
HACKED-ROUTER-HELP-SOS-HAD-DUPE-PASSWORD| 9,146  
NanoStation Loco M5| 6,395  
ubnt| 5,973  
AirRouter| 3,982  
HACKED-ROUTER-HELP-SOS-WAS-MFWORM-INFECTED| 3,891  
AirRouter HP| 3,844  
LiteBeam M5| 3,208  
NanoStation M5| 2,217  
WOM5AMiMo| 1,777  
HACKED-ROUTER-HELP-SOS-DEFAULT-PASSWORD| 1,628  
UBNT-NOR| 1,359  
HACKED-ROUTER-HELP-SOS-VULN-EDB-39701| 1,168  
HACKED-ROUTER-HELP-SOS-HAD-DEFAULT-PASSWORD| 1,096  
PowerBeam M5 300| 1,078  
PowerBeam M5 400| 1,043  
Licensed| 1,012  
NanoBridge M5| 874  
Simnet| 852  
NanoBeamM5 300| 827  
  
It seems that attackers have already identified additional problems with these devices and have exploited over 17,000 of them, as evinced by the defaced hostnames.

![Product_Version_Table.jpg](https://www.rapid7.com/cdn/images/blt09ae856adc16b9a8/683de8a22cfe32a72cdc189d/Product_Version_Table.jpg)

We can also see from the product version table above that along with being exposed to attackers, most of the devices in each product family are running outdated versions. This may explain the exploitation we described previously given the dangerous combination of service exposure, unpatched vulnerabilities, and default credentials (some of the hacker-changed device names noted the presence of default credentials).

The port 10001 exposure also reveals the internal network IP addressing scheme of behind the target devices. 192.168.0.0/16 addresses are the clear favorite, though some owners have chosen to mix it up a bit:

![Distribution.jpg](https://www.rapid7.com/cdn/images/blt2f1eb1650c84f371/683de8b818a5537e9e6872e2/Distribution.jpg)

Examining the global honeypots that we monitor as part of [Project Heisenberg](/research/project-heisenberg), we have been seeing traffic destined to this UDP port for over a year, the vast majority of which appears to be traffic similar in nature to the discovery mechanism we described above.

## Recommendations

Given the known possibility for abuse of this protocol in DoS attacks and the evidence and reports of active exploitation, Rapid7 suggests that all affected entities audit their external exposure for these devices and restrict or control access to this service as appropriate, which could include firewall or ACL rules, or disabling the affected service using [recommendations from Ubiquiti](https://community.ubnt.com/t5/EdgeRouter/UDP-broadcasts-on-port-10001/td-p/461223).

Rapid7 communicated these findings with US-CERT (VU#993645) and has reached out to CERT Brazil, as well as Ubiquiti.

The raw data from this study is available on [Rapid7 Opendata](https://opendata.rapid7.com/), along with all of our [UDP](https://opendata.rapid7.com/sonar.udp/) and other studies. [Metasploit modules](https://github.com/rapid7/metasploit-framework/pull/11338) and Nexpose/InsightVM coverage are in the works for discovering Ubiquiti devices using this method.

Rapid7 will continue to monitor this situation and will update here/elsewhere as appropriate. We welcome any feedback on this topic and encourage collaboration. Reach out to us via the comments, on Twitter ([@rapid7](https://twitter.com/rapid7)), or via [[email protected]](/cdn-cgi/l/email-protection#33415640565241505b734152435a57041d505c5e).

## Updates

We have several updates to share on this topic since our original post nearly two weeks ago:

### Community response

There have been [several](https://community.ubnt.com/t5/EdgeRouter/Understanding-Ubiquiti-Discovery-Service-Exposures/m-p/2659060/highlight/true#M239271) [updates](https://community.ubnt.com/t5/UniFi-Routing-Switching/Ubiquiti-Discovery-Protocol-Information-Disclosure/m-p/2658972/highlight/true#M130667) from the Ubiquiti community and a [Twitter response from Ubiquiti](https://twitter.com/ubnt/status/1091466759771549696) that suggest that these devices are exposed due more to poor security hygiene than anything else—failure to update, use secure passwords, or follow vendor recommendations with regards to security best practices. A [ZDNet article](https://www.zdnet.com/article/over-485000-ubiquiti-devices-vulnerable-to-new-attack/#comment-4323241658) has another report indicating that disabling this service is problematic and may have been the cause of some of this exposure, which may explain why [Ubiquiti’s original response](https://community.ubnt.com/t5/airMAX-General-Discussion/airOS-airMAX-and-management-access/td-p/2654023) to the security implications of this issue seem to have gone silent. Shortly after our original publication earlier this month, Ubiquiti [posted an article](https://help.ubnt.com/hc/en-us/articles/204976244-EdgeRouter-UBNT-Device-Discovery) that describes this discovery functionality and how to disable it, if desired.

This research also received mentions in the [700th episode of GRC’s Security Now!](https://www.grc.com/sn/sn-700.htm) podcast, [SANS Daily Network Security Podcast (Stormcast)](https://isc.sans.edu/podcastdetail.html?id=6356) for Monday, Feb. 4, 2019, among others.

### Exposure changes

In our original post on this two weeks ago, we reported 487,021 unique IPv4s advertising this service. A follow-up scan on Feb. 2, 2019, saw a small 1% drop, which could easily be natural internet fluctuation and oddities—however, our most recent survey in preparation for this update discovered a significant drop of 25%! Digging into both of these decreases in exposed systems, we immediately discovered this was caused entirely by updates to systems or infrastructure in Brazil. As you may recall from our original post on this, we identified Brazil as being responsible for more than half of the exposed Ubiquiti systems worldwide and noted that we had been in communication with the [Brazil CERT](https://www.cert.br/en/) in an effort to remedy this exposure. It is an encouraging sign that these numbers improved so dramatically.

### Improved coverage

The Metasploit team landed a PR that added the  
[auxiliary/scanner/ubiquiti/ubiquiti_discover](https://rapid7.com/db/modules/auxiliary/scanner/ubiquiti/ubiquiti_discover) module, which can be used to locate or discover affected Ubiquiti devices using this service. Seen here running against a test lab, we were able to discover the name, MAC, model, and firmware version of the remote devices:

![Metasploit-1.png](https://www.rapid7.com/cdn/images/blt2346ef234e54bdc1/683de8d05619a15a0ac6ecc5/Metasploit-1.png)

Customers of Rapid7’s Nexpose or InsightVM products can obtain fingerprint and [other coverage](https://rapid7.com/db/vulnerabilities/ubiquiti-amplification) for this by updating to product version 6.5.51 or later.

We use Nmap and zmap heavily in our research and wanted to ensure that support was trued up there as well. Tom Sellers has added a [discovery probe to Nmap](https://github.com/nmap/nmap/pull/1454) as well as an [Nmap script](https://github.com/nmap/nmap/pull/1457) that can be used to extract the name, model, firmware, and other metadata from discovered Ubiquiti devices. Additionally zmap landed a [PR ](https://github.com/zmap/zmap/pull/547) that adds similar coverage.

### Discovery version 2

As part of adding coverage as mentioned above, Tom Sellers discovered a slightly newer and different version of this discovery protocol. This protocol, like the earlier version, operates on 10001/UDP but uses a different discovery probe: \x02\x08\x00\x00. From the responses, we can extract information such as model, firmware, UniFi SDN version, MAC address, internal IP address, and the management state (adopted vs. unmanaged).

This newer protocol appears to primarily be in use by Ubiquiti’s Cloud Key management devices. Ubiquiti’s UniFI SDN Controller software is used to manage UniFi family devices on a network. The software can run on Linux, macOS, and Windows. The Cloud Key product simplifies running the Controller software by providing a cost-effective appliance to run the software as opposed to provisioning a discrete computer or virtual machine.

Our study of this newer protocol detected 347 devices on the internet that responded correctly. Interestingly, six of the devices that responded were switches manufactured by Netonix. We saw their gear show up in our original surveys, which is reflected in the table above.

The tables below provide some insight into the population of devices that responded:

Model| n  
---|---  
UCK-v2| 208  
UCK-v3| 97  
UCK| 26  
UCKP| 5  
UCKG2| 5  
WS-6-MINI| 4  
WS-12-250B| 1  
WS-12-250-AC| 1  
  
  
  


Firmware (top 15)| n  
---|---  
UCK.mtk7623.v0.12.0.29a26c9.181001.1444| 106  
UCK.mtk7623.v0.13.2.3b3276a.190131.0959| 52  
UCK.mtk7623.v0.12.4.99ad9db.190118.1139| 50  
UCK.mtk7623.v0.12.2.ac6742e.181220.1824| 23  
UCK.mtk7623.v0.13.4.410e9b6.190213.1205| 16  
UCK.mtk7623.v0.11.4.a7e4cad.180629.1434| 16  
UCK.mtk7623.v0.11.10.ab8d5ec.180818.1118| 14  
UCK.mtk7623.v0.10.1.417b59e.180403.1128| 8  
UCK.mtk7623.v0.11.12.650c948.180907.1648| 7  
UCK.mtk7623.v0.10.0.cc913ee.180306.1543| 7  
UCK.mtk7623.v0.7.3.5d239c6.170728.1449| 6  
SW.ar7240.v1.3.9.17252.130424.1604| 6  
UCK.mtk7623.v0.8.10.b829a2d.180126.1247| 3  
UCK.mtk7623.v0.6.9.50d7aef.170531.1723| 3  
UCK.mtk7623.v0.6.0.9b60a01.170208.1122| 3  
  
  
  


The oldest firmware that we observed was one instance of UCK.mtk7623.v0.3.4.9c350a9.**151019**.1212. The release date is included in the firmware name, so that version looks to have been released in October 2015.

UniFi SDN Controller version| n  
---|---  
5.9.29| 177  
5.10.12| 59  
5.10.17| 37  
5.8.28| 11  
5.8.24| 8  
5.7.23| 8  
5.8.30| 7  
null**| 6  
5.5.20| 6  
5.7.20| 5  
  
  
  


** Field not supported by Netonix

Management State| n  
---|---  
managed/adopted| 333  
default/unmanaged| 8  
null**| 6  
  
  
  


** Field not supported by Netonix

## Article tags

  * [Vulnerability Management](/blog/tag/vulnerability-management/)
  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Research](/blog/tag/research/)
  * [Project Sonar](/blog/tag/project-sonar/)