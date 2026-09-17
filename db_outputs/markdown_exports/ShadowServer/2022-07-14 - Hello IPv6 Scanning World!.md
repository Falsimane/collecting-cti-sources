# Hello IPv6 Scanning World!

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/hello-ipv6-scanning-world/
- **Date :** 2022-07-14

---

# Hello IPv6 Scanning World!

July 14, 2022

### **Introduction**

In recent months, Shadowserver has been systematically rolling out IPv6 scanning of services. Blindly scanning the full IPv6 space is of course, completely unfeasible. Total IPv6 space is about **3.4×10^38** unique addresses (that’s 340 trillion trillion trillion addresses). With our current capabilities, it would take roughly **2×10^25 years** to scan the **entire IPv6** space. Compare that to scanning all of IPv4 space (only about 4.3 billion, out of which we scan 3.7 billion addresses), which nowadays typically takes us minutes!

A variety of techniques have been proposed to solve the IPv6 scanning problem, all essentially boiling down to finding ways to narrow down potential IPv6 address deployments to allow for more targeted scanning. For an introduction to IPv6 scanning please read [RFC 7707 “Network Reconnaissance in IPv6 networks”](https://datatracker.ietf.org/doc/html/rfc7707). Since that time, [ much more literature on this topic has become available.](https://www.google.com/search?q=ipv6+scanning+strategies&sxsrf=ALiCzsbobWhjcuySOOG90OKsxWf58mjZJQ%3A1657629235475&ei=M2rNYu20HMeP9u8P1YucyAs&ved=0ahUKEwitmv-NrvP4AhXHh_0HHdUFB7kQ4dUDCA4&uact=5&oq=ipv6+scanning+strategies&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABOgcIABBHELADOgcIIRAKEKABOgQIIRAVOgcIIxCwAhAnSgQIQRgASgQIRhgAUPEEWNcQYOISaAJwAHgAgAGJAYgBjASSAQMzLjKYAQCgAQHIAQjAAQE&sclient=gws-wiz)

At the 2022 FIRST.org conference in June in Dublin, we gave a [talk on Internet Spelunking: IPv6 Scanning and Device Fingerprinting](https://www.first.org/conference/2022/program#pInternet-Spelunking-IPv6-Scanning-and-Device-Fingerprinting), which forms the basis of this article. You can find the [slides here](/wp-content/uploads/2022/07/Internet-Spelunking-FIRST-2022-Public.pdf).

### **How we scan**

We chose to conduct our IPv6 scanning based on **hitlists of IPv6 addresses** **observed being used in the wild**. We compile such a list of /128 addresses from various internal and external sources, which include:

  * DNS AAAA records (passive DNS)
  * Certificate transparency streams
  * The IPv6 hitlist (see <https://ipv6hitlist.github.io>)
  * Sinkholes
  * Other lists sourced from partners



These combined sources form **our IPv6 hitlist** , which currently contains up to **1 billion individual (/128) IPv6 addresses.** Once an IPv6 address enters our hitlist, it stays there for 30 days before dropping out, unless it generates scanning hits (i.e. that IPv6 address responds positively to at least one of our scans)

IPv6 scanning is still in its infancy. As such, far fewer scanning tools options are available than for IPv4.

For our scanning we use an IPv6 aware version of _zmap_ – [zmap6](https://github.com/tumi8/zmap/) – as well as [zgrab](https://github.com/zmap/zgrab)/[zgrab2](https://github.com/zmap/zgrab2). The latter two tools both feature native IPv6 support.

### **Observations on tool performance**

We find IPv6 scanning to be slower than IPv4 since it requires more gentle timings than IPv4. We start experiencing potential packet loss at **100 000 pps for IPv6** compared to**500 000 pps for IPv4**. For IPv6, we start to experience packet loss at **1500 concurrent senders,** versus **3500** for IPv4.

The average number of IPs/second that can be processed by _zmap6_ on our scanning infrastructure is as follows:

  * IPv4: 243 116 IPs/second
  * IPv6: 58 542 IPs/second



As can be seen above, _zmap_ IPv6 scanning is over 4 times slower than IPv4.

If we include all the scanning and processing of data (not just _zmap_) across our corpus of IPv4 and IPv6 scans, the numbers for IPv6 look even slower:

  * IPv4: 116 348 IPs/second
  * IPv6: 11 009 IPs/second



### **Results**

As of 2022-07-13 we scan for 9 different services on IPv6 (11 different ports):

  * SSL (HTTPS) (443/tcp, 8443/tcp)
  * SMTP (25/tcp)
  * TELNET (23/tcp)
  * SSH (22/tcp)
  * HTTP (80/tcp, 8080/tcp)
  * MySQL (3306/tcp)
  * FTP (21/tcp)
  * PostgreSQL (5432/tcp)
  * RDP (3389/tcp)



![](https://www.shadowserver.org/wp-content/uploads/2022/07/2022-07-11-IPv6-services-responding.png)

IPv6 services responding on 2022-07-11

Data on all the above is shared daily in our [free threat feeds](/what-we-do/network-reporting/), filtered by a subscribers network or constituency.

For scans that we consider to be just “**population** ” scans (ie. not reporting usage of vulnerable or weak protocols) like HTTP, SSL (HTTPS), SSH etc, **we find the highest exposure by far to be in the United States (119.6M), followed by Denmark (1.37M), Germany (657K) and the Netherlands (455K)**.

![](https://www.shadowserver.org/wp-content/uploads/2022/07/2022-07-11-IPv6-population-map.png)

Accessible SSL/HTTP/SSH services (population scan) by unique IPv6 (2022-07-11)

![](https://www.shadowserver.org/wp-content/uploads/2022/07/2022-07-11-IPv6-population-statistics-tree-map.png)

Accessible SSL/HTTP/SSH services (population scan) by unique IPv6 (2022-07-11)

For **exposed/vulnerable services** , we find the **highest exposure to be in the United States (636.8K), followed by the Netherlands (366K), Singapore (273.5K) and Germany (250.7K).**

![](https://www.shadowserver.org/wp-content/uploads/2022/07/2022-07-11-IPv6-vulnerable-exposed-map.png)

Accessible vulnerable/abusable or exposed services by unique IPv6 (2022-07-11)

![](https://www.shadowserver.org/wp-content/uploads/2022/07/2022-07-11-IPv6-vulnerable-exposed-statistics-tree-map.png)

Accessible vulnerable/abusable or exposed services by unique IPv6 (2022-07-11)

### **Observations on results**

Here are a few observations on how services compare between IPv4 and IPv6.

**SSL**

  * **Fewer hosts with really old ciphers (SSLv3, TLSv1.0, TLSv1.1) on IPv6**
  * 3.86% IPv4 vs 0.04% IPv6



**FTP**

  * **Far higher ratio of FTP+SSL on IPv6**
  * 55% IPv4 vs 91% IPv6



**MySQL**

  * **Far fewer hosts with deny rules on IPv6**
  * 42% IPv4 vs 4% IPv6



**RDP**

  * **Interestingly, we uncover around 22 000 RDP services accessible on IPv6**. This is an area of **security concern** , as exposed RDP instances are often exploited by bad actors. We still see over 3.2M exposed RDP instances on IPv4. While IPv6 amounts are much lower, the number is still significant.
  * Based on SSL certificate comparison with RDP scans for IPv6 hitlists and the entirety of IPv4, we find only around SSL **1 500** certificates that overlap. This may suggest many of the hosts found on IPv6 are **uniquely exposed on IPv6 only**.



**TELNET vs SSH**

  * **Lower ratio of TELNET vs SSH suggesting less legacy equipment on IPv6**
  * TELNET vs. SSH ratio 0.1 on IPv4 vs 0.03 on IPv6



### **Secure and monitor your IPv6 traffic and infrastructure!**

**Large scale IPv6 scanning is feasible**. You should not assume that your IPv6 infrastructure will never be found by attackers, hence you are “safe”. Securing and monitoring IPv6 and open IPv6 services on your network is critical, otherwise **you may be leaving gaping “holes” in your network that a bad actor may exploit**. Unfortunately tools for IPv6 security are not at the same level of maturity as for IPv4. Human analysts are also much less experienced/skilled dealing with IPv6.

We encourage all organizations to make sure they also focus on securing their IPv6 infrastructure, implement their own specific IPv6 monitoring program and of course subscribe to our free daily feeds to stay alert on their IPv6 attack surface exposure.

### **Subscribe to our new reports**

If you are an existing subscriber you will get the above mentioned IPv6 scan reports should any IPv6 be found in your network/constituency.

If you are not already a [subscriber to Shadowserver’s public benefit daily network reports](/what-we-do/network-reporting/) and would like to receive IPv6 scan reports and our other existing IPv6/IPv4 report types (covering not just other scan results, but observations from sinkholes, honeypots, darknets, sandboxes, blocklists and other sources), then [please sign up to our free daily public benefit network remediation feed service](/what-we-do/network-reporting/get-reports/).

For more information on our scanning efforts, check out [our Internet scanning summary page](/news/the-scannings-will-continue-until-the-internet-improves/).

**If you have an active feed of IPv6 addresses you can share with us, please let us know! This helps us become aware of other blocks of in use IPv6 space. We can expand out our hitlists and better protect everyone.**

For any questions, please [contact us](/contact/).

IPv6 scanning has been enabled by Shadowserver as part of the [EU CEF VARIoT project](https://www.variot.eu/).

  * [ASN](/topics/asn/)
  * [Geo Locations](/topics/geo-locations/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Statistics](/topics/statistics/)
  * [Threat Intelligence](/topics/threat-intelligence/)



[« Back to News & Insights](/news-insights/)

### Recent Articles

  * #### [Shadowserver 2025: Highlights of the Year in Review](/news/shadowserver-2025-highlights-of-the-year-in-review/)

September 7, 2026

A review of Shadowserver’s 21st year as the world’s largest provider of free, timely, actionable, daily cyber threat… [Read more »](/news/shadowserver-2025-highlights-of-the-year-in-review/)

  * #### [Shadowserver Critical Community Infrastructure Cyber Resilience Project](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

August 5, 2026

The Shadowserver Critical Community Infrastructure (CCI) Project is designed to improve the cybersecurity posture of essential… [Read more »](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

  * #### [StealC Historical Bot Infection Special Report](/news/stealc-historical-bot-infection-special-report/)

June 25, 2026

On Wednesday 24th June 2026, international law enforcement partners announced additional successful cyber crime disruption… [Read more »](/news/stealc-historical-bot-infection-special-report/)

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)