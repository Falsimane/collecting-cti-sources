# Signal to Noise in Internet Scanning Research | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/11/18/signal-to-noise-in-internet-scanning-research/
- **Date :** 2025-06-02

---

We live in an interesting time for research related to Internet scanning.

There is a wealth of data and services to aid in research. Scanning related initiatives like [Rapid7's Project Sonar](https://sonar.labs.rapid7.com/), [Censys](https://censys.io/), [Shodan](https://www.shodan.io/), [Shadowserver](https://www.shadowserver.org/) or any number of other public/semi-public projects have been around for years, collecting massive troves of data. The data and services built around it has been used for all manner of research.

In cases where existing scanning services and data cannot answer burning security research questions, it is not unreasonable for one to slap together some minimal infrastructure to perform Internet wide scans. Mix the appropriate amounts of zmap or masscan with some carefully selected hosting/cloud providers, a dash of automation, and a crash-course in the legal complexities related to "scanning" and questions you ponder over morning coffee can have answers by day's end.

So, from one perspective, there is an abundance of signal. Data is readily available.

There is, unfortunately, a significant amount of noise that must be dealt with.

Dig even slightly deep into almost any data produced by these scanning initiatives and you'll have a variety of problems to contend with that can waylay researchers. For example, there are a variety of snags related the collection of the scan data that could influence the results of research:

  * Natural fluctuation of IPs and endpoint reachability due to things like DHCP, mobile devices, or misconfiguration.
  * When blacklists or opt-out lists are utilized to allow IP "owners" to opt-out from a given project's scanning efforts, how big is this blacklist? What IPs are in it? How has it changed since the last scan?
  * Are there design issues/bugs in the system used to collect the scan data in the first place that influenced the scan results?
  * During a given study, were there routing or other connectivity issues that affected the reachability of targets?
  * Has this data already been collected? If so, can that data be used instead of performing an additional scan?



Worse, even in the absence of any problems related to the collection of the scan data, the data itself is often problematic:

  * Size. Scans of even just a single port and protocol can result in a massive amount of data to be dealt with. For example, a simple HTTP GET request to every 80/TCP IPv4 endpoint currently results in a compressed archive of over 75G. Perform deeper HTTP 1.1 vhost scans and you'll quickly have to contend with a terabyte or more. Data of this size requires special considerations when it comes to the storage, transfer and processing.
  * Variety. From Internet-connected bovine milking machines, to toasters, *** toys, appliances and an increasingly large number of "smart" or "intelligent" devices are being connected to the Internet, exposing services in places you might not expect them. For example, pick any TCP port and you can guarantee that some non-trivial number of the responses will be from HTTP services of one type or another. These potentially unexpected responses may need to be carefully handled during data analysis.
  * Oddities. There is not a single TCP or UDP port that wouldn't yield a few thousand responses, regardless of how seemingly random the port may be. 12345/TCP? 1337/UDP? 65535/TCP? Sure. You can believe that there will be something out there responding on that port in some way. Oftentimes these responses are the result of some security device between the scan source and destination. For example, there is a large ISP that responds to any probe on any UDP port with an HTTP 404 response over UDP. There is a vendor with products and services used to combat DDoS that does something similar, responding to any inbound TCP connection with HTTP responses.



Lastly there is the issue of focus. It is very easy for research that is based on Internet scanning data to quickly venture off course and become distracted. There is seemingly no end to the amount of strange things that will be connected in strange ways to the public IP space that will tempt the typically curious researcher.

Be careful out there!

## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)
  * [Research](/blog/tag/research/)