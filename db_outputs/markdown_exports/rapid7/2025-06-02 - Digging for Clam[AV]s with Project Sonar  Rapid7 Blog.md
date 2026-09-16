# Digging for Clam[AV]s with Project Sonar | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/06/28/digging-for-clamavs-with-project-sonar/
- **Date :** 2025-06-02

---

A little over a week ago some [keen-eyed folks discovered a feature/configuration weakness](http://seclists.org/nmap-dev/2016/q2/198) in the popular ClamAV malware scanner that makes it possible to issue administrative commands such as SCAN or SHUTDOWN remotely—and without authentication—if the daemon happens to be running on an accessible TCP port. Shortly thereafter, Robert Graham unholstered his [masscan](https://github.com/robertdavidgraham/masscan) tool and did a s[ummary blog post](http://blog.erratasec.com/2016/06/scanning-for-clamav-0day.html) on the extent of the issue on the public internet. The ClamAV team (which is a part of Cisco) did [post a response](http://blog.clamav.net/2016/06/regarding-use-of-clamav-daemons-tcp.html), but the reality is that if you're running ClamAV on a server on the internet and misconfigured it to be listening on a public interface, you're susceptible to a trivial application denial of service attack and potentially susceptible to a file system enumeration attack since anyone can try virtually every conceivable path combination and see if they get a response.

Given that it has been some time since the initial revelation and discovery, we thought we'd add this as a regular scan study to [Project Sonar](https://sonar.labs.rapid7.com/) to track the extent of the vulnerability and the cleanup progress (if any). Our first study run was completed and the following are some of the initial findings.

Our study found 1,654,211 nodes responding on TCP port 3310. As we pointed out in our recent [National Exposure research](https://information.rapid7.com/national-exposure-index.html) (and as Graham noted in his post) a great deal of this is "noise". Large swaths of IP space are configured to respond "yes" to "are you there" queries to, amongst other things, thwart scanners. However, we only used the initial, lightweight "are you there" query to determine targets for subsequent full connections and ClamAV VERSION checks. We picked up many other types of servers running on TCP pot 3310, including nearly:

  * 16,000 [squid](https://www.squid-cache.org/) proxy servers
  * 600 [nginx](https://www.nginx.com/resources/wiki/) servers (20,000 HTTP servers in all)
  * 500 database servers
  * 600 SSH servers



But, _you_ came here to learn about the ClamAV servers, so let's dig in.

## Clam Hunting

We found **5,947** systems responding with a proper ClamAV response header to the VERSION query we submitted. Only having around 6,000 exposed nodes out of over 350 million PINGable nodes is nothing to get really alarmed about. This is still an egregious configuration error, however, and if you have this daemon exposed in this same way on your internal network it's a nice target for attackers that make their way past your initial defenses.

5,947 is a small enough number that we can easily poke around at the data a bit to see if we can find any similarities or learn any lessons. Let's take a look at the distribution of the ClamAV versions:

![found_servers.png](https://www.rapid7.com/cdn/images/blt10ce6be78359d52e/683de453abf2adfd883c4507/found_servers.png) You can click on that chart to look at the details, but it's primarily there to show that virtually every ClamAV release version is accounted for in the study, with some dating back to 2004/2005. If we zoom in on the last part of the chart, we can see that almost half (2,528) of the exposed ClamAV servers are running version 0.97.5, which itself dates back to 2012. While I respect Graham's guess that these may have been unmaintained or forgotten appliances, there didn't seem to be any real pattern to them as we looked at DNS PTR records and other host metadata we collected. These all do appear to have been just "set and forgot" installs, reinforcing our findings in the National Exposure report that there are virtually no barriers to entry for standing up or maintaining nodes on the internet.

![lastbit.png](https://www.rapid7.com/cdn/images/blt8757ba04edb882af/683de4802a9b682e2e2bd370/lastbit.png)

## A Banner Haul

Now, not all VERSION queries respond with complete banner information but over half did and said response banner contains both the version string _and_ the last time the scanner had a signature update. Despite the poor network configuration of the nodes, 2,930 (49.3%) of them were at least current with their signatures, but 346 of them weren't, with a handful being over a decade out of "compliance." We here at Rapid7 strive to stay within the rules, so we didn't poke any deeper to try to find out the signature (or further vulnerability) status of the other ClamAV nodes.

![hygiene.png](https://www.rapid7.com/cdn/images/blt80236849ce511b49/683de4b3abf2ad83333c451b/hygiene.png)

As we noted above, we performed post-scan DNS PTR queries and WHOIS queries for these nodes, but this exercise proved to be less than illuminating. These are nodes of all shapes and sizes sitting across many networks and hosting providers. There _did_ seem to be a large commonality of these ClamAV systems running on hosts in "mom and pop" ISPs and we did see a few at businesses and educational institutions, but overall these are fairly random and probably (in some cases) even accidental ClamAV deployments.

As a last exercise, we grouped the ClamAV nodes by autonomous system (AS) and tallied up the results. There was a bit of a signal here that you can clearly see in this list of the "top" 10 ASes:

AS| AS Name| Count| %  
---|---|---|---  
4766| KIXS-AS-KR Korea Telecom, KR| 1,733| 29.1%  
16276| OVH, FR| 513| 8.6%  
3786| LGDACOM LG DACOM Corporation, KR| 316| 5.3%  
25394| MK-NETZDIENSTE-AS, DE| 282| 4.7%  
35053| PHADE-AS, DE| 263| 4.4%  
11994| CZIO-ASN - Cruzio, US| 251| 4.2%  
41541| SWEB-AS Serveisweb, ES| 175| 2.9%  
9318| HANARO-AS Hanaro Telecom Inc., KR| 147| 2.5%  
23982| SENDB-AS-KR Dongbu District Office of Education in Seoul, KR| 104| 1.7%  
24940| HETZNER-AS, DE| 65| 1.1%  
  
Over 40% of these systems are on networks within the Republic of Korea. If we group those by country instead of AS, this "geographical" signal becomes a bit stronger:

| Country| Count| %  
---|---|---|---  
1| Korea, Republic of| 2,463| 41.4%  
2| Germany| 830| 14.0%  
3| United States| 659| 11.1%  
4| France| 512| 8.6%  
5| Spain| 216| 3.6%  
6| Italy| 171| 2.9%  
7| United Kingdom| 99| 1.7%  
8| Russian Federation| 78| 1.3%  
9| Japan| 67| 1.1%  
10| Brazil| 62| 1.0%  
  
What are some takeaways from these findings?

  * Since there was a partial correlation to exposed ClamAV nodes being hosted in smaller ISPs it might be handy if ISPs in general offered a free or very inexpensive "hygiene check" service which could provide critical information in understandable language for less tech-savvy server owners.

  * While this exposure is small, it does illustrate the need for implementing a robust configuration management strategy, especially for nodes that will be on the public internet. We [have tools](/products/nexpose/) that can really help with this, but adopting solid DevOps principles with a security mindset is a free, proactive means of helping to ensure you aren't deploying toxic nodes on the internet.

  * Patching and upgrading go hand-in-hand with configuration management and it's pretty clear almost 6,000 sites have not made this a priority. In their defense, many of these folks probably don't even know they are running ClamAV servers on the internet.

  * Don't forget your security technologies when dealing with configuration and patch management. We cyber practitioners spend a great deal of time pontificating about the need for these processes but often times do not heed our own advice.

  * Turn stuff off. It's unlikely the handfuls of extremely old ClamAV nodes are serving any purpose, besides being easy marks for attackers. They're consuming precious IPv4 space along with physical data center resources that they just don't need to be consuming.

  * Don't assume that if your ClamAV (or any server software, really) is "just internal" that it's not susceptible to attack. Be wary of leaving egregiously open services like this available on any network node, internally or externally.




## Fin

Many thanks to [Jon Hart](/blog/author/jon-hart/), Paul Deardorff & Derek Abdine for their engineering expertise on Project Sonar in support of this new study. We'll be keeping track of these ClamAV deployments and hopefully seeing far fewer of them as time goes on.

Drop us a note at [[email protected]](/cdn-cgi/l/email-protection#53213620363221303b132132233a37647d303c3e) or post a comment here if you have any questions about this or future studies.

## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)
  * [Labs](/blog/tag/labs/)
  * [Research](/blog/tag/research/)