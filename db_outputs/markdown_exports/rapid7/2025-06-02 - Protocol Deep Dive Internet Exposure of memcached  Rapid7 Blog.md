# Protocol Deep Dive: Internet Exposure of memcached | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/12/07/nicer-protocol-deep-dive-internet-exposure-of-memcached/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## memcached (UDP/11211)

_It's an easy-to-use DDoS Howitzer AND a NoSQL database!_

### TLDR

  * **WHAT IT IS:** An in-memory key-value store, used usually in caching website assets for geographically distributed websites.
  * **HOW MANY:** 68,337 discovered nodes. 68,337 (100%) have version fingerprints
  * **VULNERABILITIES:** 13 CVEs since 2011, but it has a wicked amplification DDoS issue we cover in the Exposure Information section.
  * **ADVICE:** Use it! Just don’t expose it to the internet.**ALTERNATIVES:** Redis and etcd are two similar, alternative in-memory key-value stores with characteristics similar to memcached.



Memcached is an in-memory key-value store for small chunks of arbitrary data (i.e., strings, binary objects) from results of database calls, API calls, or web page rendering. Its simple design has made it wildly popular, as it promotes quick deployment and ease of development.

### Discovery details

Project Sonar found 68,337 exposed memcached hosts, and we did a double-take when we saw that South Africa is in third place, since we don’t often find it in any other top 10 lists of exposure. Most (97%) of these SA nodes are in two autonomous systems: Icidc Network (87%) and Internet Keeper Global (10%), and a majority of hosts in each autonomous system appear to have similar exposure counts in both nginx and SSH.

![memcached-1.png](https://www.rapid7.com/cdn/images/blt755cb636bb06c0a9/683de5f118a553fda468720e/memcached-1.png) ![memcached-2.png](https://www.rapid7.com/cdn/images/bltbe9e0984c128daf7/683de6117f86036ac023092c/memcached-2.png)

As noted in our section on Redis, Amazon has a cloud “cache” service offering that can also be configured to use memcached directly or emulate the exquisitely diminutive memcached protocol, and [Alibaba has a managed memcached service offering](https://www.alibabacloud.com/product/apsaradb-for-memcache), so it is no surprise finding some in those environments, but it is somewhat disconcerting that these instances are exposed to the internet. What’s more surprising is that [OVH](https://docs.ovh.com/gb/en/dedicated/securing-server-with-memcached-service/) goes out of its way to help you secure memcached and, yet, ~1,500 folks apparently did not get that rather crucial memo.

### Exposure information

Why all the fuss about memcached? Well, way back in 2018, an [“Insufficient Control of Network Message Volume” vulnerability in the UDP portion of memcached](https://attackerkb.com/topics/KM2uX55z24/cve-2018-1000115-major-amplification-ddos-vulnerability) was used to launch the largest distributed denial-of-service amplification attack ever, and disrupted many major internet services. [Cloudflare](https://blog.cloudflare.com/memcrashed-major-amplification-attacks-from-port-11211/) summed up the flaw quite well in its blog at that time:

"There are absolutely zero checks, and the data WILL be delivered to the client, with blazing speed! Furthermore, the request can be tiny and the response huge (up to 1MB)."

Rapid7 Labs keeps an eye on memcached in the hopes we won’t find any, and, as seen in the previous section, said hopes are constantly dashed. Of the 68,337 nodes discovered, 68,044 return a valid version number (so ~300 folks think they’re being awfully clever). If the valid version numbers are correct, 47% of them (~32,000) are below the fixed release version of 1.5.6, but the “fix” in 1.5.6 and above was to disable UDP by default. Our study uses UDP and sends the stats query command and receives a full reply, so all these hosts can potentially be used in other amplification attacks.

Oh, and since we get a full response from that stats inquiry, it is good to see that most of these servers restart at least once a month:

![memcached-3.png](https://www.rapid7.com/cdn/images/blt308afc2a0e5ac2bc/683de63930073e380feb1a22/memcached-3.png)

### Attacker’s view

While we do not have a memcached honeypot, we can see connection attempts on UDP 11211 and peek at the packet captures to see if memcached commands (most often, the stats one we use, though we occasionally see what look like misconfigured clients that are connecting to what they think are their memcached servers). The daily memcached command connections we see are mostly from [Shadowserver](https://www.shadowserver.org/), which is (correctly) self-described as a “nonprofit security organization working altruistically behind the scenes to make the internet more secure for everyone,” despite their scary name. They also scan the internet every day to try to get a handle on exposure and help organizations (for free) get a picture of their attack surface. We heart Shadowserver.

During the first third of 2020, we saw spikes of near 80,000 data-less UDP connections on 11211 across a handful of days, but none of this appears truly malicious in nature.

### Our advice

**IT and IT security teams** should never expose memcached to the internet, and should ensure via playbooks and automation that development, test, and production memcached environments are rigidly controlled.

**Cloud providers** should continue to offer secure service alternatives to self-hosted memcached, ensure their provider-maintained machine images are kept patched with a default configuration of memcached only available on non-internet-exposed interfaces, and—frankly—not allow memcached to be exposed to the internet on host in their sphere of network control.

**Government cybersecurity agencies** should provide regular reminders about the dangers of memcached, offer guidance on how to run memcached safely, monitor for malicious use of memcached, and strongly encourage ISPs and cloud providers to block connections to memcached’s default port.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)