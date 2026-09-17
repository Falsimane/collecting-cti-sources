# Falcon Intelligence Recon+ and the Dark Web | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/falcon-intelligence-recon-and-dark-web/
- **Date :** June 09, 2023

---

# Making Sense of the Dark Web with Falcon Intelligence Recon+

June 09, 2023

• [ Ben Termeer - Brian Bunyard - Keith Mason](/en-us/blog/author.ben-termeer---brian-bunyard---keith-mason/ "Posts by Ben Termeer - Brian Bunyard - Keith Mason") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


The vastness of the deep and dark web can easily turn attempts to monitor for cyber threats into a firehose of useless information. Part of the problem is the nature of the data streams that need to be monitored. Every day, more credentials are stolen and exposed. Illegal criminal forums are full of repeated spamming of illicit advertisements. Thousands of new domain names are registered daily, including many that can be considered [typosquatted](/en-us/blog/how-crowdstrike-protects-against-domain-impersonations/). All of this data can generate significant numbers of matches on even well-structured and finely tuned monitoring programs.

As experts in managed digital risk protection, the CrowdStrike Falcon® Intelligence Recon+ team leverages CrowdStrike’s technology to sift through many notifications to find only relevant hits for our customers. In 2022, the Falcon Intelligence Recon+ team triaged hundreds of thousands of notifications. In this blog, we cover several illustrative use cases reflecting the team’s work throughout the year.

## Notifications by Industry

Figure 1 provides a breakdown of total Falcon Intelligence Recon+ notifications by customer verticals for 2022. The industries with the most actionable alerts were retail, technology and manufacturing.

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/06/OW-Japan-blog-1.png)

Figure 1. Percentage of total notifications by industry

## Falcon Intelligence Recon+ Analysis

The analysis shown in Figure 2 and 3 is based solely on observations from the Falcon Intelligence Recon+ team and the sources’ effects on our current customer base.

### Credential Leaks

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/06/OW-Japan-blog-3.png)

Figure 2. Total credential leaks by month in 2022

The Falcon Intelligence Recon+ team triaged approximately 3,000 credential leak notifications over the course of 2022. We observed a significant increase in credential leaks in June. Upon closer examination of June data, we noticed that the normal number of credential leaks in the manufacturing, healthcare and media industries doubled for the month. This also coincides with observations of multiple adversaries testing the [KoloVeeman](https://falcon.crowdstrike.com/intelligence-v2/reports/csa-220662-multiple-ecrime-adversaries-observed-using-veeam-credential-harvesting-tool) credential harvester. The increase observed in December cannot be attributed to any particular industry, with the entire Falcon Intelligence Recon+ customer set affected. It is possible that threat actors were trying to take advantage of the holidays with workers potentially being out of office.

### Top Five Actionable Sources

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/06/Recon-blog-Fig-4.png)

Figure 3. Top true positive sources

## Russian Market Analysis

The Russian market is where Falcon Intelligence Recon+ analysts observed the most actionable alerts generated. This marketplace posts hundreds of access-broker-type notifications daily. The majority of these credentials were harvested using either _Redline_ , _Vidar_ or _Raccoon_ malware. Of the 20,000+ Russian market notifications, we observed 50% of the monitored domains had stolen credentials.

An example of a poster on the Russian market is an author who uses the handle _Mo####yf_ <_Diamond_ _>_. The Falcon Intelligence Recon platform showed that this threat actor posted more than 800,000 times in 2022, with posts in English, German, Portuguese, Italian, Spanish, Malay, Turkish, Dutch, Czech and Romanian. This threat actor posted credentials related to more than 90% of the monitored identities. The stealer of choice for the threat actor is _Raccoon_ , which was used in 63% of notifications, followed by _Vidar_ at 34% and _Redline_ at 3%.

## Telegram Analysis

### Refund Fraud

Falcon Intelligence Recon identified social engineering techniques used to undermine refund methodologies to scam online retail merchants. Malicious threat actors discerned fake tracking ID (FTID) methods that work for specific merchants and traded that information. Commonly, threat actors requested mail-in refunds following expensive purchases, and they returned a package with the correct label but would not put the appropriate item in the box. With this technique, they attempted to either undermine the refund facility or the carrier; while the refund facility can be trained in what to look for, an outline would need to be provided to the carrier. Another method identified was using a legitimate shipping label but obfuscating the relevant information on the label that would identify the person or the order information.

### Credential Leaks

Telegram is also used by adversaries to post new and old email/password combinations. Some of the most common Telegram channels we observed posting exposed data are: Unsafe Internet Chat (1524907442), Maill Access (1368931502), Retard Cloud (1587335634) and OPENBULLET(1706265433).

## Market BlackPass Analysis

Market BlackPass is used predominantly for selling identity theft information. Considering the intended use, we noticed the retail sector’s customer base and retail organizations’ executive staff as the main victims of information posted on the market. Authors posted personally identifiable information (PII) for sale, including name, date of birth, social security number and even debit/credit card information. Victim information was sold for between $1 and $7 USD per victim.

## Typosquatting Analysis

Falcon Intelligence Recon+ analysts researched more than 100,000 typosquatting notifications and identified GoDaddy, NameCheap, Sav<.>com, Google, and Alibaba as the top five registrars associated with typosquatting. The most common fraudulent domains that we encountered were set up to conduct phishing and harvesting campaigns.

## Pastebin Analysis

Pastebin is similar to Telegram in the variety of types of data that gets shared maliciously. Throughout 2022, we observed different types of exposures on Pastebin, from account credential leaks and discounted brand vouchers to illegal live streaming of televised programs. Pastebin differs from the majority of the other sources in that most of the notifications deemed to be true positive are posted with “guest” being the identity of the author. This can sometimes make it more difficult to determine connections between posts, but it does not hinder our ability to provide our customers with actionable intelligence.

## How Falcon Intelligence Recon+ Can Help

Since Falcon Intelligence Recon+ works with deep and dark web data every day, we know which sites to focus on and which ones are less concerning. A customer’s assigned Falcon Intelligence Recon+ analyst provides a managed digital risk protection service. We handle the hunting for external threats to brands, employees and sensitive data, allowing customers’ cyber professionals to devote their time to handling actionable data rather than hunting through a complex and ever-changing data set.

#### Additional Resources

  * _Watch this[short demo](https://www.youtube.com/watch?v=0PjOLMuLIrA) to see how Falcon Intelligence Recon enables organizations to proactively uncover fraud, data breaches and phishing campaigns to protect their brand from online threats that target their organization._
  * _To find out more about how to incorporate threat intelligence into your security strategy, visit the[CrowdStrike Falcon® Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Read about the cybercriminals tracked by CrowdStrike Intelligence in the[CrowdStrike 2023 Global Threat Report](/en-us/resources/reports/global-threat-report/)._
  * _[Request a free trial](/en-us/free-trial-guide/) of the industry-leading CrowdStrike Falcon® platform._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)