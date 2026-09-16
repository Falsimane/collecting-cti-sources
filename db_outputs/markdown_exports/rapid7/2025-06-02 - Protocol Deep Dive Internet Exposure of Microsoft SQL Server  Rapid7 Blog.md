# Protocol Deep Dive: Internet Exposure of Microsoft SQL Server | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/11/23/nicer-protocol-deep-dive-internet-exposure-of-microsoft-sql-server-ms-sql-udp-1434/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## Microsoft SQL Server (MS SQL) (UDP/1434)

_SELECT TOP 1 * FROM quippy_subtitles;_

### TLDR

  * **WHAT IT IS:** A relational database management system developed by Microsoft. Note, the database proper operates over TCP (usually port 1433), but the MS SQL Discovery service (which points to where MS SQL actually is) was used for this survey.
  * **HOW MANY:** 98,771 discovered nodes  
98,771(100%) returned version and other configuration information over an unauthenticated request.
  * **VULNERABILITIES:** 86 since 1999—21 with a CVSS score of 8.5 or higher, and 45 with remote code execution flaws.
  * **ADVICE:** Use it! But, never, ever, ever let it sit on the internet.
  * **ALTERNATIVES:** PostgreSQL, MySQL, Oracle, and a cadre of other relational database management systems.
  * **GETTING:** Complacent. Virtually no change over 2019.



Microsoft SQL Server 1.0—a 16-bit server for the OS/2 operating system—was first released in 1989 (so, it’s older than many of you who are reading this report!). The first version on a Microsoft Windows operating system (NT) was SQL Server 4.2, released in 1993. Presently, Microsoft supports five different major versions of SQL Server: 2012, 2014, 2016, 2017, and 2019, along with its Azure cloud database offering. If you’re in a large enterprise, it’s almost guaranteed that you have MS SQL Server running somewhere supporting some business process/task.

### Discovery details

Despite the fact that one should never expose any database service to the internet (unless it is via some deliberate API offering), [Project Sonar](/research/project-sonar/) found nearly 99,000 of them more than willing to give us many details about their services (without any authentication). This is a tiny number compared to what you saw in the section on MySQL—two orders of magnitude tiny—which is likely due to the fact that MS SQL Server costs money and MySQL is, well, free.

![udp-1.png](https://www.rapid7.com/cdn/images/blte91fc13bbeef9a91/683de0922cfe3262ecdc164d/udp-1.png)

It’s unusual for Turkey to break into these top 10 lists, let alone take the No. 2 spot away from larger countries, so we dug into the results a bit, and it turns out customers of hosting providers in Turkey love to expose Microsoft SQL Server to the internet! Fifteen providers account for 75% of Turkey’s exposure, with an impressive variety of SQL Server versions on display. Similarly, 20 hosting companies in India account for 75% of SQL Server exposure there (35 total SQL Server versions). Poland is worth a mention, since it exposes nearly as much SQL Server as Germany. Orange Polska—a large ISP and hosting provider—accounts for 50% of the SQL Server exposure in Poland, with one, large sales, accounting, and HR management SaaS firm accounting for 35% of exposure from Orange’s network.

![udp-2.png](https://www.rapid7.com/cdn/images/blteaa7f358a4171751/683de0b930073e6d20eb184f/udp-2.png)

We suspect there's a very popular database management course in some Istanbul university or training facility that's encouraging people to expose Microsoft SQL server. If you know of it, please let us know so we can convince them to stop it!

You’d think Microsoft would have come in first when it came to Microsoft SQL Server exposure in our in-scope cloud providers, but if we step back a bit and remember that Microsoft Azure has an [Azure Database Service](https://azure.microsoft.com/en-us/services/sql-database/) offering, it’s easier to see why it may not be exposing as many SQL Server instances to the internet, since it’s likely very difficult to talk to the Azure Database Service from the outside.

[OVH](https://www.ovhcloud.com/en/bare-metal/os/) makes a big deal out of providing cost-effective, ready-made images for SQL Server, as does [Amazon](https://aws.amazon.com/sql/), but OVH seems to cost less than the other two when it comes to self-hosting MS SQL, which is what likely gave it the top spot.

![udp-3.png](https://www.rapid7.com/cdn/images/blt29bdc3dac1800603/683de0de4c5a0908d85e0b1d/udp-3.png)

### Exposure information

We found 54 unique versions of Microsoft SQL Server across those systems, 20 of which make up 95% of the exposure. Red cells indicate that the SQL Server main version is no longer supported. “Vintage” signifies the release date for the listed version.

![Screen-Shot-2020-11-22-at-5.05.11-PM.png](https://www.rapid7.com/cdn/images/blt722da442855614e3/683de1033323a539b280a93a/Screen-Shot-2020-11-22-at-5.05.11-PM.png)

We must note that none of the supported versions are at the latest patch release. Granted, anyone who is recklessly exposing MS SQL to the internet likely does not have the greatest cyber-hygiene by default, so it is somewhat optimistic to expect to see these folks keeping up with patches.

### Attacker’s view

Attackers regularly set their sights on SQL Server, but they’ve gone above and beyond since October 2019 (in reality, going back to 2018, but they really stepped things up in 2019) with a [relentless credential stuffing and SQL execution campaign](https://www.guardicore.com/2020/04/vollgar-ms-sql-servers-under-attack/).

![udp-4.png](https://www.rapid7.com/cdn/images/bltc462a29ad05da9a9/683de129aaf6202a9179deb4/udp-4.png)

Our high-interaction MS SQL honeypots in [Project Lorelei](/research/project-lorelei/) were literally overwhelmed with this activity starting shortly after [outlets started reporting on a possible backdoor](https://www.scmagazine.com/home/security-news/gaming/skip-2-0-backdoor-malware-provides-magic-password-to-access-mssql-accounts/) in some less-than-legitimate distributions of MS SQL Server. Each day saw over 63 million credential access attempts, followed by various SQL command sequences (when the honeypots allowed the attackers to log in). Rapid7 Labs has yet to correlate the drop in February to any known, public actions, but this campaign is far from over (though it may have changed hands since Guardicore broke the story).

If this doesn’t convince you to be extra careful about not hanging MS SQL Servers directly off the internet, we’re not sure what else would.

### Our advice

**IT and IT security teams** should never, ever, ever, ever, ever put MS SQL Server instances directly on the internet and should do a much better job than the folks responsible for these ~32,000 have when it comes to patch management. Those responsible for managing access to internal SQL Server instances should track credential breaches and force password resets for any accounts that match usernames in those in the credential dumps. We know we shouldn’t have to say this, but given both the attacker campaign and the sorry state of SQL Server on the internet, you should never leave default accounts enabled and never use default credentials.

**Cloud providers** should continue to offer secure, private Microsoft SQL Server managed services and ensure their provider’s managed images are always at the latest patch level. Customers who use out-of-date and especially out-of-support images should receive regular communications regarding the hazards associated with lack of attention to this matter.

**Government cybersecurity agencies** should track campaigns against MS SQL Server and provide timely notifications to individuals, organizations, and their constituents with sufficient detail to help them detect possible attacks. Extra focus should be made on providing education and awareness regarding the need to keep MS SQL Server patched and ensure it does not sit directly on the public internet.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)