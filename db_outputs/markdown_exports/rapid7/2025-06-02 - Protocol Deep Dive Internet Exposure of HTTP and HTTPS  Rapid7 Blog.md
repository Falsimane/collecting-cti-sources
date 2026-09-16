# Protocol Deep Dive: Internet Exposure of HTTP and HTTPS | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/01/29/nicer-protocol-deep-dive-internet-exposure-of-http-and-https/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## HTTP (TCP/80) & HTTPS (TCP/443)

_One protocol to bring them all, and in the darkness, bind them._

### TLDR

  * **WHAT IT IS: HTTP:** Pristine, plaintext Hypertext Transfer Protocol communications. **HTTPS:** Encrypted HTTP.
  * **HOW MANY:** 51,519,309 discovered HTTP nodes. 36,141,137 discovered HTTPS nodes. We’re going to be talking a bit differently about fingerprinting in this blog post, so raw, generic counts will have no context.
  * **VULNERABILITIES:** Hoo boy! Many! But, do you mean vulnerabilities in core web servers themselves? The add-ons folks build into them? The web applications they serve? As many users of Facebook might say, “it’s complicated.”
  * **ADVICE:** Go back to Gopher! Seriously, though, please continue to build awesome things using HTTPS. Just build them in such a way that folks who install and operate web servers can easily configure them securely, see patch status, and upgrade quickly and confidently.
  * **ALTERNATIVES:**[QUIC](https://tools.ietf.org/html/draft-tsvwg-quic-protocol-02), or “Quick UDP Internet Connection,” which is a “new multiplexed and secure transport atop UDP, designed from the ground up and optimized for HTTP/2 semantics.” While HTTP[S] will be with us for a Very Long Time, QUIC is its successor and will usher in whole new ways to deliver content securely and efficiently (and undoubtedly, exploit the same).



We’re going to talk about both HTTP and HTTPS combined (for the most part) as we identify what we found, some core areas of [exposure](/fundamentals/what-is-exposure-management/), and opportunities for attackers. It’ll be a bit different than all the previous blogs, but that’s just part of the quirky nature of HTTP in general.

### Discovery details

Way back in our Email blogs, we compared encrypted and unencrypted services. We’ll do the same here, but will be presenting a “top 12” for countries since that is the set combination between HTTP and HTTPS.

There are 30% more devices on the internet running plaintext HTTP versus encrypted HTTPS web services. The U.S. dwarfs all other countries in terms of discovered web service, very likely due to the presence of so many cloud services, hosting providers, and routers, switches, etc. in IPv4 space allocated to the U.S.

Germany and Ireland each expose 9% more HTTPS nodes than HTTP, and both the Netherlands and U.K. are quickly closing their encryption disparity as well.

We’ll skip cloud counts since, well, everyone knows cloud servers are full of web servers and we’re not sure what good it will do letting you know that Amazon had ~640K Elastic Load Balancers (version 2.0!) running on the day our studies kicked off. 

![image4.png](https://www.rapid7.com/cdn/images/blt149f99bcbb387b80/683de5004b2b7f7918e16270/image4.png)

## Exposure information

To understand exposure, we need to see what is running on these web servers. That’s not as easy as you might think with just lightweight scans. For example, here are the top 20 HTTP servers by vendor/family and port:

Vendor| Family| HTTPS (80)| % of HTTP| | HTTPS (443)| % of HTTPS  
---|---|---|---|---|---|---  
Microsoft| IIS| 5,273,393| 10.24%| | 2,096,655| 5.80%  
Apache| Apache| 4,873,517| 9.46%| | 2,595,714| 7.18%  
nginx| nginx| 3,938,031| 7.64%| | 2,495,667| 6.91%  
Amazon| Elastic Load Balancing| 644,862| 1.25%| | 386,751| 1.07%  
Squid Cache| Squid| 381,224| 0.74%| | 8,649| 0.02%  
ACME Laboratories| mini_httpd| 125,708| 0.24%| | 82,427| 0.23%  
Oracle| GoAhead Webserver| 48,505| 0.09%| | 40,501| 0.11%  
Apache| Tomcat| 40,702| 0.08%| | 32,271| 0.09%  
Taobao| Tengine| 37,626| 0.07%| | 14,130| 0.04%  
Eclipse| Jetty| 29,750| 0.06%| | 50,763| 0.14%  
Mbedthis Software| Appweb| 23,463| 0.05%| | 19,470| 0.05%  
Virata| EmWeb| 22,354| 0.04%| | 7,179| 0.02%  
Embedthis| Appweb| 17,235| 0.03%| | 32,629| 0.09%  
Microsoft| Windows CE Web Server| 14,012| 0.03%| | 1,027| 0.00%  
TornadoWeb| Tornado| 13,637| 0.03%| | 10,151| 0.03%  
Tridium| Niagara| 9,772| 0.02%| | 564| 0.00%  
TwistedMatrix| Twisted Web| 7,481| 0.01%| | 4,984| 0.01%  
Caucho| Resin| 5,168| 0.01%| | 1,812| 0.01%  
Mort Bay| Jetty| 5,079| 0.01%| | 2,033| 0.01%  
SolarWinds| Serv-U| 3,232| 0.01%| | 6,421| 0.02%  
  
Remember, we’re just counting what comes back on a `GET` request to those two ports on each active IP address, and the counts come from Recog signatures (which are great, but far from comprehensive). For some servers, we can get down to the discrete version level, which lets us build a [Common Platform Enumeration](https://nvd.nist.gov/products/cpe) identifier. That identifier lets us see how many CVEs a given instance type has associated with it. We used this capability to compare each version of each service family against the number of CVEs it has. While we do not have complete coverage across the above list, we do have some of the heavy(ier) hitters:

![image2-2.png](https://www.rapid7.com/cdn/images/blteb16894aa37f82e6/683de528ca9dfc71285267b6/image2-2.png)

We limited the view to a service family having at least having 10 or more systems exposed and used color to encode the CVSS v2 scores. 

The most prevalent CVE-enumerated vulnerabilities are listed in the table below. While it's technically possible that these CVEs have been mitigated through some other software control, patching them out entirely is really the best and easiest way to avoid uncomfortable conversations with your vulnerability manager.

And, the top 30 most prevalent are:

CVE| Number  
---|---  
CVE-2017-8361| 336  
CVE-2013-2275| 202  
CVE-2012-1452| 186  
CVE-2016-1000107| 184  
CVE-2016-6440| 184  
CVE-2012-0038| 168  
CVE-2012-1835| 165  
CVE-2016-8827| 165  
CVE-2011-3868| 164  
CVE-2011-0607| 160  
CVE-2007-6740| 154  
CVE-2013-4564| 150  
CVE-2016-0948| 149  
CVE-2016-0956| 149  
CVE-2009-2047| 146  
CVE-2015-5670| 145  
CVE-2017-8577| 143  
CVE-2014-0134| 135  
CVE-2015-5355| 135  
CVE-2012-5932| 127  
CVE-2014-8089| 120  
CVE-2015-5685| 118  
CVE-2016-1000109| 118  
CVE-2015-5672| 114  
CVE-2016-5596| 112  
CVE-2016-5600| 112  
CVE-2016-4261| 111  
CVE-2016-4263| 111  
CVE-2016-4264| 111  
CVE-2016-4268| 111  
  
While we expect to see traditional web servers, there are other devices connected to the internet that expose web services or administrative interfaces (which we’ve partially enumerated below):

Vendor| Device| HTTP (80)| HTTPS (443)  
---|---|---|---  
Cisco| Firewall| 123| 986,766  
AVM| WAP| 1,942| 604,890  
Asus| WAP| 1| 177,936  
Synology| NAS| 61,796| 50,531  
Check Point| Firewall| 16,059| 30,773  
SonicWALL| VPN| 7,413| 16,061  
Ubiquiti| WAP| 0| 11,813  
HP| Printer| 16,247| 9,178  
MikroTik| Router| 289,026| 8,056  
Tivo| DVR| 6,400| 6,779  
Philips| Light Bulb| 4,785| 3,349  
Polycom| VoIP| 369| 3,079  
Ubiquiti| Web cam| 955| 922  
HP| Lights Out Management| 601| 708  
ARRIS| Cable Modem| 350| 217  
Fortinet| Firewall| 1,221| 159  
Xerox| Printer| 1,575| 29  
Canon| Multifunction Device| 124| 14  
Netwave| Web cam| 6,420| 7  
HeiTel| DVR| 2,734| 2  
Samsung| DVR| 53,053| 2  
Merit LILIN| DVR| 2,565| 1  
Fidelix| Industrial Control| 545| 0  
FUHO| DVR| 1,249| 0  
Shenzhen Reecam Tech. Ltd.| Web cam| 1,902| 0  
Ubiquiti| DVR| 675| 0  
Yamaha| Router| 9,675| 0  
  
For instance, we found nearly a million Cisco ASA firewalls. That fact is not necessarily “bad,” since they can be configured to provide remote access services (like VPN). Having 123 instances on port 80 is, however, not the best idea.

Unlike Cisco, most MikroTik routers seem to be exposed sans encryption, and over 75% of them are exposing the device’s admin interface. What could possibly go wrong?

Upward of 50,000 Synology network-attached storage devices show up as well, and the File Sharing blog posts talked at length about the sorry state of exposure in these types of devices. They’re on the internet to enable owners to play local media remotely and access other files remotely.

There are printers, and light bulbs; DVRs and home router admin interfaces; oh, and a [few thousand entire building control systems](https://www.fidelix.com/building-automation/).In short, you can find pretty much anything with a web interface hanging out on the internet.

### Attacker’s view

There are so many layers in modern HTTP[S] services that attackers likely are often paralyzed by not knowing which ones to go after first. Attacking HTTP services on embedded systems is generally one of the safest paths to take, since they’re generally not monitored by the owner nor the network operator and can be used with almost guaranteed anonymity.

Formal web services—think Apache Struts, WebLogic, and the like—are also desirable targets, since they’re usually associated with enterprise deployments and, thus, have more potential for financial gain or access to confidential records. HTTP interfaces to firewalls and remote access systems (as we saw back in the Remote Access blog posts) have been a major focus for many attacker groups for the past 18–24 months since once compromised, they can drop an adversary right into the heart of the internal network where they can (usually) quickly establish a foothold and secondary access method.

![image1-2.png](https://www.rapid7.com/cdn/images/blt0cafecd4a0eef47d/683de54870aa951a5ffe31a0/image1-2.png) ![image3-1.png](https://www.rapid7.com/cdn/images/blt8ad78645034db99a/683de5adaaf6201d6479dfd7/image3-1.png)

You’re also more likely to see (at least for now) more initial probes on HTTP (80), as noted by both the unique source IPv4 and total interaction views (above). It’s hard to say “watch 80 closely, and especially 80→443 moves by clients,” since most services are still offered on both ports and good sites are configured to automatically redirect clients to HTTPS. Still, if you see clients focus more on 80, you may want to flag those for potential further investigation. And, definitely be more careful with your systems that only talk HTTP (80).

## Our advice

**IT and IT security teams** should build awesome platforms and services and put them on the internet over HTTPS! Innovation drives change and progress—plus, the internet has likely done more good than harm since the first HTTP request was made. Do keep all this patched and ensure secure configuration and coding practices are part of the development and deployment lifecycles. Do not put administrative interfaces to anything on the internet if at all possible and ensure you know what services your network devices and “Internet of Things” devices are exposing. Finally, disable `Server:` banners on everything and examine other HTTP headers for what else they might leak and sanitize what you can. Attackers on the lookout for, say, nginx will often move on if they see Apache in the Server header. You’d be surprised just how effective this one change can be.

**Cloud providers** should continue to offer secure, scalable web technologies. At the same time, if pre-built disk images with common application stacks are offered, keep them patched and ensure you have the ability to inform users when things go out-of-date.

**Government cybersecurity agencies** should keep reminding us not to put digital detritus with embedded web servers on the internet and monitor for campaigns that are targeting these invisible services. When there are major issues with core technologies such as Microsoft IIS, Apache HTTP, or nginx, processes should be in place to notify the public and work with ISPs, hosting, and cloud providers to try to contain any possible widespread damage. There should be active programs in place to ensure no critical telecommunications infrastructure has dangerous ports or services exposed, especially router administrative interfaces over HTTP/HTTPS.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)