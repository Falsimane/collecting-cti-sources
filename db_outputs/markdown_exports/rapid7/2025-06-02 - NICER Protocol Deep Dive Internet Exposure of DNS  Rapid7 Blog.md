# NICER Protocol Deep Dive: Internet Exposure of DNS | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/01/05/nicer-protocol-deep-dive-internet-exposure-of-dns/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## Domain Name System (DNS) (UDP/53)

_"The Achilles Heel of the Internet" - Sir Tim Berners-Lee_

### TLDR

  * **WHAT IT IS:** Domain Name System (DNS): The globally distributed address book of services on the internet.
  * **HOW MANY:** 4,717,658 discovered nodes. 3,498,439 (74.1%) have Recog fingerprints (15 total vendor+service families)
  * **VULNERABILITIES:** Around 200 across all service families with every CVSS score imaginable.
  * **ADVICE:** You kinda have no other choice but to use it.
  * **ALTERNATIVES:** DNS over TLS (DoH), DNS over HTTPS (DoH), DNS over QUIC (DoQ); downgrade to Novell Netware.
  * **GETTING:** Used about as much as last year, which kind of makes sense since DNS makes the internet work.



Nobody wants to memorize IP addresses in order to get to network resources, nor does anyone want to maintain a giant standalone list of hostname to IP address mappings. However, nobody also wants to wait forever to get a response to the request for the IP address of, say, example.com. Thus was the atmosphere that begat what we posit is the most ubiquitous user-facing but also most user-overlooked service on the internet: the Domain Name System (DNS).

## Discovery details

[Project Sonar](/research/project-sonar/) discovered nearly 5 million DNS servers via UDP requests on port 53. This is a far fewer number than the total sum of, say, web servers, but it is a non-trivial number of systems and the reasons for that make sense. ISPs provide DNS services to home and small-business users, organizations host their own DNS to maintain control of their brand namespace, and vendors provide customized DNS services in either an outsourcing capacity or to provide enhanced services such as malware and other types of content filtering. Finally, large technology companies such as Google, Cloudflare, IBM (via Quad9), and others also provide centralized DNS services for various good (?) reasons. This is all to say, outside of the giant centralized DNS providers, the global DNS footprint tends to track very closely with the allocated country IPv4 space; the more IP allocations a given country has, the more DNS servers are there to keep track of them all.

![image2-4.png](https://www.rapid7.com/cdn/images/bltb77bc20524d9227d/683ddd1618a55310b8686ee1/image2-4.png) ![image3-3.png](https://www.rapid7.com/cdn/images/blt9fd04859176e0d34/683ddd3faaf620a65279dd6b/image3-3.png)

Conversely, it really doesn’t make much sense to waste precious (and costly) cloud resources by hosting DNS in there. However, it seems OVH users have plenty of cycles (and money) to burn. Yep, those aren’t just OVH’s DNS servers. We come to that conclusion based on the diversity of DNS vendor software and the version spread. Now, OVH does have the largest data center on the planet and is not just a cloud services provider, so it’s pretty reasonable to see that it can and should be in the top spot.

Given that most small orgs use their ISPs’ external DNS (directly or via recursive DNS) and that the vast majority of home users still use their ISP DNS, you can imagine that autonomous system DNS server distribution has a very long tail.

## Exposure information

DNS has had … challenges … over the years. It is a binary protocol that receives quite a bit of attention paid to it by both researchers and attackers. Because of this, and the nature of the UDP service, it is possible to craft a binary DNS request that ends up being around 60 bytes that asks for a DNS response, which ends up potentially being near 4,000 bytes (~7:1 amplification), making it great for use in [low-to-mid-level amplification DDoS attacks](https://us-cert.cisa.gov/ncas/alerts/TA13-088A). It is also possible to compromise a DNS server via specially crafted binary messages, though that task gets more difficult with each passing year.

**DNS Service Prevalence**

Vendor| Count| Percentage  
---|---|---  
ISC BIND| 2,007,593| 57.39%  
Thekelleys Dnsmasq| 556,228| 15.90%  
NLnet Labs NSD| 520,785| 14.89%  
PowerDNS PowerDNS| 342,143| 9.78%  
Microsoft DNS| 43,185| 1.23%  
NLnet Labs Unbound| 14,158| 0.40%  
Nominum Vantio| 7,596| 0.22%  
DrayTek DNS| 2,674| 0.08%  
cz.nic Knot| 1,897| 0.05%  
Michael Tokarev rbldnsd| 898| 0.03%  
RIPE Atlas Anchor| 614| 0.02%  
ALU DNS| 539| 0.02%  
Incognito DNS| 78| 0.00%  
D J Bernstein djbdns| 45| 0.00%  
Check Point META IP| 6| 0.00%  
  
BIND (now ISC BIND) was the first DNS server and is still the most prevalent one (of those we had Recog fingerprints for), which is likely why it has 119 CVEs (most all of them DoS-related). The picture really isn’t this clean, though. Within ISC BIND alone, we found 550 distinct version strings (most legit, too). We can look at version diversity by vendor across all autonomous systems with DNS servers to see just how crazy the situation really is:

![image1-4.png](https://www.rapid7.com/cdn/images/blt338fab7365668a3f/683ddd65a38fc5e7bd031f80/image1-4.png)

If this were a social media service instead of a serious research paper, now’s about the time we’d post a “Do You Even…?” meme gif with the word “Patch” in it. So, not only do we forget about DNS when we’re using it, we also seem to forget about it when we run it, too. Denial-of-service flaws are found every year in these servers, but when DNS is running, it’s running, and you likely need it to keep running.

### Attacker’s view

We’re not in the DDoS protection services racket market, nor do we have DDoS probes sitting in key locations to be able to detect when [DDoS attacks](/fundamentals/denial-of-service-attacks/) are happening. We see both TCP- and UDP-based DNS traffic in Heisenberg, but they’re mostly inventory scans or misconfigurations. 

This is not to say attackers care not about DNS anymore. Every DDoS mitigation vendor makes a point of reminding us about this a few times a year in their service reports, and Verizon noted a [serious uptick in DoS](https://threatpost.com/verizon-data-breach-report-dos-skyrockets-espionage-dips/155843/) in general in 2019 (in which DNS played a part). And, there are always new, crafty attack vectors being researched and developed.

But, attackers do more with DNS than just DoS. Organizations must register public, top-level domain names and set up various types of records for them so we can all buy things without leaving home. This exposes two potential avenues of for attack: first at the registrar level, which is why it is vital that you protect your domain registration account with multi-factor authentication (preferably app-based for this versus just SMS) and then do the same for your external DNS provider (if you’re using an external DNS provider). In May 2020, the Internet Systems Consortium hosted a webinar on this very topic that should help provide more background information, and [SpamHaus](https://www.spamhaus.org/news/article/797/the-current-state-of-domain-hijacking-and-a-specific-look-at-the-ongoing-issues-at-godaddy) estimates that GoDaddy has around 100 newly hijacked domains daily. 

They who control DNS control who you are on the internet.

## Our advice

**IT and IT security teams** should safeguard registrar and external DNS provider accounts with multi-factor authentication, keep internal and external DNS systems fully patched, relentlessly monitor DNS for signs of abuse and configuration changes, and consider treating DNS like a first-class application in your environment as opposed to the plumbing that sits hidden behind drywall.

**Cloud providers** that offer DNS registration and hosting services should mandate multi-factor authentication be used and have processes in place to detect potential malicious activity (i.e., takeover attempts). All machine images with DNS services installed by default should be updated immediately after new DNS server versions are released and then notify all existing users about the need to upgrade.

**Government cybersecurity agencies** should provide timely notifications regarding DNS attacks of all kinds and have resources available that document how to securely maintain DNS infrastructure.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)