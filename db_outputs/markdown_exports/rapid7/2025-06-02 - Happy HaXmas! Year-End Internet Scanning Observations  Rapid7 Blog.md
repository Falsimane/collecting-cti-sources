# Happy HaXmas! Year-End Internet Scanning Observations | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/01/04/happy-haxmas-year-end-internet-scanning-observations/
- **Date :** 2025-06-02

---

_This blog is the 12th and final post in our annual_[ _12 Days of HaXmas_](/blog/tag/haxmas/) _series._

As we wrap up 2018 and forge ahead into 2019, reflection is beneficial. My role here on the [Rapid7 Labs](/research/) team includes a significant amount of time related to internet scanning with [Project Sonar](https://opendata.rapid7.com/about/) and the sharing of scan data and related collaboration through [Opendata](https://opendata.rapid7.com/). What follows are several observations from the last year that related to these efforts:

## Hyper HTTP

The HyperText Transfer Protocol ([HTTP](https://www.w3.org/Protocols/)) is extensively documented, full of useful features and functionality, easily interpreted or interacted with given its largely plain text representation (excluding HTTP/2+), and is one of the most common and interesting protocols from a security perspective. It is also our most common study type in Sonar, with nearly 60 ports studied several times per month between our [HTTP](https://opendata.rapid7.com/sonar.http/) and [HTTPS](https://opendata.rapid7.com/sonar.https/) studies.

In 2018, Sonar observed nearly 260 million distinct IPv4 addresses offering one or more HTTP services. Breaking this down by port, it is unsurprising that most of this exposure is due to the standard HTTP endpoint on 80/TCP (144 million) and HTTPS endpoint on 443/TCP (88 million). Non-standard but common alternative ports such as 8080 (28 million) and 8443 (8 million) also make up large chunks of this exposure, which is expected given the myriad ways products, services, and devices use and abuse HTTP today.

HTTP can be a rather verbose protocol, and this chattiness allows many opportunities for understanding more about the systems speaking HTTP, primarily through inspection of the headers sent by both ends of an HTTP conversation as well as the body of the HTTP messages. Applying these techniques to Sonar’s HTTP study data, it is hard not to get distracted by the results. Some disappointing highlights include:

  * Over 28 million devices are exposing ports primarily used by the [TR-069](https://en.wikipedia.org/wiki/TR-069) protocol, which in addition to being a swamp of acronym soup is just an HTTP protocol used by ISPs and other service providers to manage customer-premises equipment (CPE), like DSL and cable modems and routers. Expanding this concept to other CPE management ports and protocols, there are at least another 11 million endpoints exposed.
  * Over 25 million devices are exposing ports used by the Universal Plug and Play (UPnP) protocol’s HTTP SOAP services. Because this service can be used to perform a variety of sensitive operations that might reveal asset information or allow manipulation of port forwarding rules to expose sensitive internal assets, it should not generally be exposed directly to the Internet without additional protections. [Rapid7 warned about UPnP](/blog/post/2013/01/29/security-flaws-in-universal-plug-and-play-unplug-dont-play/) exposures in early 2013.



## Encryption

Encryption and the larger topic of cryptography come up frequently in our research, including in our yearly National Exposure Reports— so much so that the topic could have its own section on our blog.

As part of any research studies done through Sonar, if the protocol in question uses encryption in the form of Secure Sockets Layer (SSL) or Transport Layer Security (TLS), we track metadata related to the digital certificates offered by the SSL endpoints. In the hope of fostering collaboration and enabling research, Rapid7 Opendata provides access to Sonar’s SSL/TLS certificate metadata from [HTTP-based services](https://opendata.rapid7.com/sonar.ssl/) and [non-HTTP-based services](https://opendata.rapid7.com/sonar.moressl/).

Examining the certificate metadata from over 30 different SSL/TLS-speaking endpoints currently studied by Sonar, we can make several high-level observations:

  * Over 40 million IPv4 addresses offered one or more SSL/TLS encrypted services. The vast majority of those come from HTTPS on 443/TCP, accounting for over 38 million uniques, and the remainder are shared in roughly equal parts among SSL or STARTTLS-enabled mail protocols such as SMTP, POP and IMAP, as well as common alternate HTTPS ports.
  * Out of all of the IPv4 addresses offering one or more SSL/TLS encrypted services, over 13%—5.3 million—have expired certificates. This has a range of implications, from negatively impacting service availability to training bad user behavior through repeatedly accepting browser or other certificate expiration warning messages.
  * An SSL/TLS certificate has a cryptographic checksum that is used to uniquely identify the certificate. A duplicate cryptographic checksum indicates that a certificate has been reused. This is normal in some situations, like load balancing, but is often the result of a security misconfiguration—for example, where services and devices are deployed with default SSL certificates unchanged from vendor defaults. This can lead to situations in which unauthorized parties could potentially decrypt traffic from other devices. Looking for clusters of duplicate certificate fingerprints, we see several patterns:  

    * 192.168.1.1 and other similar [RFC1918](https://tools.ietf.org/html/rfc1918) private IP addresses are the most common subject, indicating the service in question is behind some sort of NAT or other network device.
    * Clusters of several hundred thousand subjects exist for products made by QNAP, Huawei, Cisco, and WatchGuard.



## DNS

The Domain Name System (DNS) is one of several core components of the modern internet, mapping IPs to names, names to IPs, and so much more.

DNS has been a focus of our Sonar studies from the beginning of the project. On a weekly basis, we resolve one or more DNS record types for an ever-increasing list of syntactically valid names that _might_ represent actual names in the global DNS. We obtain these names from a variety of sources, including paid services provided by various registration authorities as well as from metadata observed in Sonar endpoint studies, such as HTML links or SSL/TLS certificate subject common names (CN). We closed out 2018 with over 3.5 billion of these names.

Prior to 2018, we had three different [forward DNS studies](https://opendata.rapid7.com/sonar.fdns_v2/) that looked at these names from the perspective of different record types:

  * ANY: Any records for the given name known by the DNS server in question. This is notably different than returning all records. Furthermore, it is complicated by the fact that responding to the ANY request is an arguable security issue and, as such, is prohibited by several DNS products.
  * A: All IPv4 addresses for the given name, which may be numerous in the case of load-balancing and similar technologies.
  * AAAA: All IPv6 addresses for the given name.



We’ve also historically had a [reverse DNS study](https://opendata.rapid7.com/sonar.rdns_v2/) that studies the DNS from an IP perspective rather than by name, resolving the PTR record types for all public IPv4 addresses, with over 1.2 billion records being observed weekly.

In response to feedback and work with Opendata users, we added in 2018 several new forward DNS studies that run regularly:

  * CNAME: Any other names that the given name might be an alias for.
  * MX: The mail servers used to accept mail for the given name/domain.
  * TXT: Associates arbitrary text values with the name in question, used for the Sender Policy Framework ([SPF](https://en.wikipedia.org/wiki/Sender_Policy_Framework)), among other things
  * For every MX record found, A and TXT record studies of names specific to Domain-based Message Authentication, Reporting and Conformance ([DMARC](https://en.wikipedia.org/wiki/DMARC)), and SMTP MTA Strict Transport Security ([MTA-STS](https://datatracker.ietf.org/doc/rfc8461/))



The result is a ton of data from almost any angle. Highlights include:

  * Over 6 billion records are resolved per week.
  * Over 7 terabytes (compressed!) of the results from all of these studies are available on Opendata.
  * Approximately 70 different record types are observed weekly, thanks largely in part to the ANY study.



## Improved fingerprinting via Recog

[Recog](https://github.com/rapid7/recog) is an open source fingerprinting utility that is used by several Rapid7 products, including [Metasploit](/products/metasploit/), [Nexpose](/products/nexpose/), and [InsightVM](/products/insightvm/). We utilize data obtained from Sonar studies to regularly update Recog to ensure that this fingerprinting is accurate, and we are always on the lookout for ways to improve Recog’s coverage or capabilities.

In 2018, we added Telnet and Apache module fingerprinting to our suite of supported fingerprintable databases in Recog. We also added Common Platform Enumeration ([CPE](https://nvd.nist.gov/products/cpe)) 2.3 support to many of our fingerprints, which can be useful—for example, when attempting to identify exposures to vulnerabilities based on [CVEs](https://cve.mitre.org/).

Just before ringing in the new year, we witnessed the [100th release of Recog](https://github.com/rapid7/recog/releases/tag/v2.1.41) after a large push to improve the fingerprinting of FTP, HTTP, MDNS, SIP, SSH, Telnet, and UPnP, adding coverage for commonly available devices and products that are interesting either because of volume or sensitivity. This highlighted an alarming but unsurprising number number of phones, teleconferencing devices, printers, DVRs, cameras or similar surveillance devices, multimedia devices including speakers, microphones, and TVs, as well as hordes of NAS devices offering services on the public internet.

The patterns in Recog’s databases help us identify or fingerprint a given service, operating system, or device, which might include vendor, product and family names, versions, as well as other metadata like system name, local time, and device type/function. This information is hugely valuable when understanding exposure, which is a common theme in much of our research.

## Conclusion

Last year showed lots of improvements in Rapid7 Labs Internet scanning and related research efforts, some of which I touched on above. A common element among many of the areas discussed is that seemingly everywhere you look or how you look at it, there are serious exposure issues on the public internet today. It seems like we are adding or at least considering adding a study for yet another protocol weekly, and it is impossible to not get distracted when rummaging through existing study data that is simply rife with security issues waiting to happen.

In 2019, we expect to continue this momentum of providing data and services to empower the security community through projects like Sonar and Recog, as well as supporting research derived from the data and collaboration efforts via Opendata.

Interested in this topic? Have comments or questions? We’d love to hear your feedback over Twitter ([@Rapid7](https://twitter.com/rapid7)) or via email at [[email protected]](/cdn-cgi/l/email-protection#bac8dfc9dfdbc8d9d2fac8dbcad3de8d94d9d5d7).

## Article tags

  * [Haxmas](/blog/tag/haxmas/)
  * [Research](/blog/tag/research/)
  * [Project Sonar](/blog/tag/project-sonar/)