# Protocol Deep Dive: Internet Exposure of MySQL | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/11/13/nicer-protocol-deep-dive-internet-exposure-of-mysql/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

### TLDR

  * **WHAT IT IS:** A wildly popular open source relational database management system with a fragmented history.
  * **HOW MANY:** 2,826,541 discovered nodes. 2,817,028 (99.66%) have Recog fingerprints (4 total vendor families)
  * **VULNERABILITIES:** Um, over 1,000 (O_O) with CVSS scores all over the place.
  * **ADVICE:** Use it! But, not on the internet, please, and keep it patched.**ALTERNATIVES:** PostgreSQL, Microsoft SQL Server, Oracle proper, and a host of other RDBMS.



We could write an entire paper on the fragmented history of MySQL. It started off as an open source, unified codebase and—since being acquired by Oracle—has variants such as [MariaDB](https://mariadb.org/), [Percona](https://www.percona.com/), [Google Cloud SQL](https://cloud.google.com/sql), and a few others. They all “speak” MySQL, but versioning works a bit differently for each of them. When we do slice and dice by vendor, we’ll be focusing on the official Oracle MySQL variant and MariaDB, since they make up 98.8% of discovered nodes.

### Discovery details

Poland barely passes Germany to fall into third position due to hosting provider Home.pl (thanks to Home.pl's aforementioned affinity for, well, less-than-great default configurations as detected with our FTP studies). The United States accounts for 34% of all exposed MySQL, with China being a distant 15%.

![mysql-1.png](https://www.rapid7.com/cdn/images/blt39a729663d2cd622/683ddc6c2a9b68995b2bd118/mysql-1.png)

[Alibaba](https://www.alibabacloud.com/product/apsaradb-for-rds-mysql) has both images with Oracle MySQL and MariaDB, but also has its own MySQL-flavored offering in its AsparaDB managed service. [Amazon](https://aws.amazon.com/rds/mysql/) has a similar situation, and [OVH](https://www.ovh.co.uk/cloud-databases/) also has targeted MySQL offerings. It’s strange to see them be in the top 3 of cloud exposure, as each provider does a pretty good job of offering secure defaults for the images and services they provide and have good documentation on securing MySQL. This means folks either go out of their way to make MySQL appear on the internet or really mess up the configuration.

![mysql-2.png](https://www.rapid7.com/cdn/images/blt37e1c523ae0a3d63/683ddc953e68ee8ecd889820/mysql-2.png)

Because we chose to focus on cloud providers and not “hosting” providers or co-location companies for the majority of this report, we need to add some color to this section, since co-location company [Unified Layer](https://www.unitedlayer.com/) accounts for 145,967 exposed instances (beating OVH) and hosting provider GoDaddy accounts for 101,775 exposed instances (beating every other provider).

There are 17,876 autonomous systems exposing MySQL instances, with a median exposure of three servers and a mean of 156 servers, so there’s plenty of exposure finger-pointing to go around.

### Exposure information

There are 1,006 vendor+version combinations in the corpus, and that’s if we aggregate vendors into Oracle, MariaDB, Google, Percona, and “Other” buckets. With over 2 million instances on the internet, we may have a sufficient surveyed corpus for it to be safe to say that nobody manages MySQL well on their own. Yes, we’re looking right at you, now. Go ahead, type `mysqld --version` at your laptop’s command prompt or a server you regularly interact with (you know you’re running one somewhere). One of our authors—that crazy guy with the shield—did it and even he is two patch points behind the latest MariaDB release.

We get it. Patch management is hard. But not patching a local laptop instance only exposed to `localhost` and not patching a MySQL instance directly connected to the internet are two vastly different situations.

Still, you likely want to know what the version distribution looks like. We had to get a bit creative for this one (given the huge spread), so we’ve made a word cloud superimposed on the MariaDB logo, because seals are awesome:

![mysql-.png](https://www.rapid7.com/cdn/images/bltbc5c56c21f8ea2e3/683ddcb918a553b752686ebd/mysql-.png)

Version 5.7.26 was released on April 25, 2019 (Oracle version, which all the other ones mostly flow from).

Version 5.7.26 has 13 moderate vulnerabilities, while 5.7.30 was released on April 27, 2020, so it is relatively current as of this report writing. Oracle maintains official branches for 8.0.x (which is really 5.8.x), 5.7.x, and 5.6.x due to fairly major technical differences between each of those versions. To keep things confusing, MariaDB jumped from 5.6.x to 10.0.x, with the most prominent 10.x release in the corpus as 10.2.31, which was released in January 2020 and has been superseded by 10.2.32 (released in May). MariaDB itself maintains version 10.0.x through 10.4.x.

If you had trouble following that paragraph, you now have a more perfect understanding of how hard database patch management is, since it's all a twisty maze of similar-but-different multi-decimal numbers. So, stop putting MySQL on the internet!

### Attacker’s view

Heisenberg has no MySQL honeypots, and the nature of MySQL connection attempts make it difficult to tell spurious connections from directed attacks or deliberate (albeit, misconfigured) attempts to legitimately communicate with something someone thought they owned. This means any charts we could have shown here would just result in more questions than answers.

Suffice it to say, Heisenberg generally sees 10,000–30,000 TCP connection attempts daily on TCP/3306 from a median of approximately 250 distinct source IPv4s. A handful of these (daily) are from other researchers scanning for MySQL, and between 5% and 15% are misconfigured clients, as our honeypot nodes are mostly in cloud IP space.

We can let you know that back in 2019, attackers launched ransomware campaigns against internet-facing MySQL servers and that there are billions of credentials out there for malicious actors to try against the 2+ million MySQL servers we found, so you really should think twice about putting MySQL on a public server.

### Our advice

**IT and IT security teams** should never host MySQL on a public IP address and should strongly consider picking one flavor of MySQL vendor+version and make it standard across your entire enterprise (and keep it patched). MySQL often comes bundled with “appliances,” and you should work with your procurement team to ensure the vendor communicates which version is bundled with their solution and also that they provide timely updates when new MySQL releases are announced.

**Cloud providers** should continue to offer secure, managed MySQL-compatible offerings to help mitigate the threats associated with customers hosting their own MySQL infrastructure. Vendor-managed disk images with MySQL distributions on them should be updated immediately when there are new releases and vendors should communicate with customers to inform them they need to update their legacy versions.

**Government cybersecurity agencies** should provide meaningful guidance on how to host MySQL securely and provide timely notifications when new attacker campaigns are discovered. Furthemore, an effort should be made to work with cloud providers, hosting providers, and ISPs to prevent MySQL from being connected to the public internet.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)