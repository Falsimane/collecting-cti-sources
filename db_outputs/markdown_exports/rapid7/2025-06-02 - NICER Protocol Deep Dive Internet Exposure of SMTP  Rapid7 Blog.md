# NICER Protocol Deep Dive: Internet Exposure of SMTP | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/10/02/nicer-protocol-deep-dive-internet-exposure-of-smtp/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## SMTP (25/465/587)

_The “Simple” in SMTP is intended to be ironic._

#### TLDR

  * **WHAT IT IS:** A usually cleartext, text-based standard for delivering email between networks.
  * **HOW MANY** : 5,805,012 discovered nodes on port 25 and 4,007,931 on port 587. SMTPS on port 465 comes in with 3,494,067. All together, that's 13,307,010 distinct service nodes. 3,023,486 (52%) have Recog fingerprints (43 total service families)
  * **VULNERABILITIES:** The natively cleartext nature of email is the primary concern around the security of this protocol. Email is also the most popular method for phishing users into revealing passwords and running malware. Finally, there are at least two serious vulnerabilities in popular mail servers Exim and Microsoft Exchange deployed today.
  * **ADVICE:** Mail administrators need to be fanatical about applying security patches as they become available, and should implement DMARC anti-spoofing controls yesterday.
  * **ALTERNATIVES:** Outsourcing email to a cloud provider, such as Google or Microsoft, is often the right choice when comparing the costs of effectively maintaining this critical internet infrastructure.
  * **GETTING:** Better (25/587)! Fewer crazy people are hosting their own mail.



### SMTP discovery details

While SMTP is traditionally cleartext with an optional secure protocol negotiation called STARTTLS, we're seeing more SSL-wrapped SMTP, also known as SMTPS, in the world today. The following charts and tables illustrate the distribution of SMTP over port 25, SMTP on port 587 (which is intended for SMTP-to-SMTP relaying of messages), and SMTPS on port 465.

![encrypted-vs-unencrypted.png](https://www.rapid7.com/cdn/images/bltc7545a8d44f5b7ef/683de91ecc6042b5b7206a6a/encrypted-vs-unencrypted.png)

Country| SMTP (25)| SMTP (587)| SMTPS (465)  
---|---|---|---  
United States| 1,467,077| 1,456,598| 1,253,805  
Germany| 637,569| 373,266| 375,526  
Japan| 589,222| 382,133| 222,633  
France| 398,390| 212,937| 196,177  
Poland| 306,368| 289,522| 284,297  
Spain| 291,844| 44,435| 48,694  
Russia| 245,814| 104,709| 95,972  
United Kingdom| 193,073| 121,902| 122,069  
Netherlands| 189,456| 129,690| 115,211  
Canada| 137,342| 146,323| 132,133  
  
![encrypted-unencrypted-cloud.png](https://www.rapid7.com/cdn/images/blt8f4a4ffae8e4153b/683de934c26e07af7228ea26/encrypted-unencrypted-cloud.png)

Provider| SMTP (25)| SMTP (587)| SMTPS (465)  
---|---|---|---  
OVHcloud| 317,584| 248,695| 236,772  
Amazon| 95,175| 32,579| 31,438  
DigitalOcean| 74,097| 46,521| 41,234  
Scaleway| 30,876| 15,332| 12,594  
QuadraNet| 29,282| 18,200| 8,667  
Google| 29,030| 50,422| 50,561  
Microsoft| 14,945| 5,576| 2,790  
Rackspace| 8,459| 2,511| 1,841  
Alibaba| 5,729| 3,863| 3,826  
Oracle| 1,274| 509| 345  
  
As far as top-level domains are concerned, we see that the vast majority of SMTP lives in dot-com land—we counted over 100 million MX records in dot-com registrations, with a sharp drop-off in dot-de, dot-net, and dot-org, with about 10 million MX records in each.

### SMTP exposure information

There are dozens of SMTP servers to choose from, each with their own idiosyncratic methods of configuration, spam filtering, and security. The top SMTP server we're able to fingerprint is Postfix, with over a million and a half installs, followed by Exim, Exchange, and trusty Sendmail. The table below is the complete list of every SMTP server we positively identified—mail administrators will recognize the vestiges of old, little-used mail servers, such as the venerable Lotus Domino and ZMailer. If these are your mail servers, think long and hard about why you’re still running these as opposed to simply farming this thankless chore out to a dedicated mail service provider.

SMTP Family| Count  
---|---  
Postfix| 1,679,222  
exim| 759,799  
Exchange Server| 182,263  
Sendmail| 180,812  
Mail Server| 84,262  
IIS| 58,720  
Ecelerity Mail Server| 25,206  
MDaemon| 14,404  
Connect| 10,447  
IMail Server| 5,354  
Pro| 3,462  
IBM Domino| 3,445  
Twisted| 1,999  
UTM| 1,926  
WinWebMail| 1,879  
Email Security| 1,867  
ListManager| 1,785  
Lotus Domino| 1,734  
David| 1,490  
PowerMTA| 1,239  
CCProxy| 675  
MailSite| 305  
Post.Office| 275  
VPOP3| 245  
ZMailer| 205  
GroupWise| 176  
Check Point| 78  
WinRoute| 43  
Messaging Server| 40  
VOPMail| 24  
IntraStore| 22  
Internet Mail Server| 18  
NTMail| 17  
Mercury Mail Transport System| 15  
FWTK| 9  
SLMail| 8  
FTGate| 4  
Internet Mail Services| 4  
VM| 3  
Mail-Max| 2  
AppleShare IP Mail Server| 1  
MERCUR| 1  
WebShield| 1  
  
Finally, let's take a quick look at the Exim mail server. Like most other popular software on the internet, we can find all sorts of versions. Unlike other popular software, Exim versioning moves pretty quickly—the current version of Exim at the time of scanning was v 4.93, and has already incremented to 4.94 by the time of publication. However, the popularity of the latest version (4.93) versus next-to-latest (4.92.x) is in the 100,000 range, and given the intense scrutiny afforded to Exim by national intelligence agencies, this delta can be pretty troubling. It’s so troubling that the [American National Security Agency issued an advisory](https://media.defense.gov/2020/May/28/2002306626/-1/-1/0/CSA%20Sandworm%20Actors%20Exploiting%20Vulnerability%20in%20Exim%20Transfer%20Agent%2020200528.pdf) urging Exim administrators to patch and upgrade as soon as possible to avoid exploitation by the “Sandworm team.” Specifically, the vulnerability exploited was CVE-2019-10149, and affects versions 4.87 through 4.91—as of the time of our scans, we found approximately 87,500 such servers exposed to the internet. While this is about a fifth of all Exim servers out there, exposed vulnerabilities in mail servers tend to shoot to the top of any list of “must patch now” vulns.

### Attacker’s view

Given the high value attackers tend to assign to SMTP vulnerabilities, it’s no surprise that we see fairly consistent scanning action among threat actors in our SMTP honeypots.

![project-heisenberg-smtp.png](https://www.rapid7.com/cdn/images/bltf71e0a6df44a8d63/683de9483e68ee9420889c35/project-heisenberg-smtp.png)

Date| SMTP Port| Count| Percentage| Provider  
---|---|---|---|---  
2020-02-15| 25| 518| 12.92%| Sprint (Poland)  
2020-02-15| 25| 514| 12.82%| China Telecom  
2020-02-15| 25| 409| 10.20%| Tele Asia Hosting  
2020-02-15| 465| 4,337| 99.18%| DigitalOcean  
2020-02-15| 587| 4,568| 99.65%| DigitalOcean  
2020-02-26| 25| 32,495| 73.97%| Hostwinds  
2020-02-26| 25| 6,504| 14.81%| Sprint (Poland)  
2020-02-26| 25| 2,730| 6.21%| Tamatiya Eood Hosting  
2020-02-26| 465| 851| 69.36%| DigitalOcean  
2020-02-26| 465| 344| 28.04%| Web Hosted Group  
2020-02-26| 587| 948| 94.33%| DigitalOcean  
2020-03-25| 25| 4,930| 41.55%| Microsoft 365  
2020-03-25| 25| 1,481| 12.48%| Locaweb Hosting  
2020-03-25| 25| 509| 4.29%| Hurricane Electric  
2020-03-25| 465| 415| 95.62%| DigitalOcean  
2020-03-25| 587| 408| 97.14%| DigitalOcean  
2020-05-09| 25| 1,180| 58.13%| Vietnam Telecom  
2020-05-09| 25| 195| 9.61%| Zumy Communications  
2020-05-09| 25| 159| 7.83%| China Telecom  
2020-05-09| 465| 6,641| 94.91%| Microsoft 365  
2020-05-09| 465| 326| 4.66%| DigitalOcean  
2020-05-09| 587| 316| 95.18%| DigitalOcean  
  
### Our advice around SMTP

**IT and IT security teams** should seriously consider converting over to an established email provider such as Microsoft's Office 365 or Google's G Suite. Running your own email remains one of the more truly painful network administration tasks, since outages, patch management, and redundant backups can be tricky even in the best of times, to say nothing of the constant drain of resources in the fight against spam and phishing. Established providers in this space have a proven track record of handling both spam and phishing, as well as achieving remarkable uptimes.

**Cloud providers** should provide rock-solid documentation on how to set up SMTP services for their customers, starting with SSL-wrapped SMTP as a default configuration. This is one case where we wouldn't be opposed to providers such as Microsoft and Google inserting a little adver-docu-tizing pushing customers over to their hosted mail solutions.

**Government cybersecurity agencies** should recognize that everyone is challenged by running merely serviceable email infrastructure, and very few organizations are truly excellent at it at any reasonable scale. As far as content-based attacks are concerned, these experts should continue pressing for minimum technical defenses, such as DMARC, and user education in recognizing and avoiding phishing scams.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)