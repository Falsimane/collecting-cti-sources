# Protecting Employees' Sensitive Data on the Web | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/protecting-sensitive-employee-data-on-the-web/
- **Date :** April 18, 2024

---

# Secure Your Staff: How to Protect High-Profile Employees' Sensitive Data on the Web

April 18, 2024

• [ Ben Termeer - Brian Bunyard - Keith Mason](/en-us/blog/author.ben-termeer---brian-bunyard---keith-mason/ "Posts by Ben Termeer - Brian Bunyard - Keith Mason") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Organizations are increasingly concerned about high-profile employees’ information being exposed on the deep and dark web. The CrowdStrike Counter Adversary Operations team is often asked to find fake social media accounts and personally identifiable information (PII) that might be exposed.

Impersonations and leaked PII can unravel lives and ruin the reputations of individuals and their organizations. Through surface, deep and [dark web monitoring](/en-us/cybersecurity-101/threat-intelligence/dark-web-monitoring/), CrowdStrike is able to provide timely alerts to our customers, helping them take quick action to mitigate the potential damage caused by these posts.

The CrowdStrike [Counter Adversary Operations team](/en-us/cybersecurity-101/threat-intelligence/counter-adversary-operations-cao/) has created thousands of monitoring rules that protect our customers, and nearly 20% of them focus solely on high-profile employees. In this blog, we break down the data source categories that generate the most actionable notifications — including the type of data being posted — and name the [actors](/en-us/cybersecurity-101/threat-intelligence/threat-actor/) that are posting most frequently on those sites.

## CrowdStrike Counter Adversary Operations Analysis

The analysis and graph below represent only the true positive notifications from the Counter Adversary Operations team. A true positive notification is one that has been determined to be malicious in nature and actionable for customers.

By analyzing true positive notifications, we can identify the top actionable sources and their effects on organizations.

### Actionable Source Types

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2024/04/Figure1-2-1024x701.png)](/content/dam/crowdstrike/www/en-us/wp/2024/04/Figure1-2.png)

Figure 1. Percentage of true positives by source type, February 2021-February 2024

## Chat Mediums

The most common chat site with true positives seen in our monitoring is Telegram.

Telegram included data that could be used to target high-profile employees and potentially their organizations. Telegram, unlike other sites, is not the most directly targeted source — high-profile employee data is found within the site, but this data is within combined lists of millions of other people's data, so it is unlikely the author knows they have captured the sensitive data of high-profile employees. Otherwise, actors would individualize the credentials for purchase at a premium price. The majority of the sensitive data identified within Telegram includes email addresses and passwords for third-party applications. Although this does not directly tie into targeting high-profile employees to undermine their companies’ technical infrastructure, if these employees use the same password for their personal and corporate accounts, it can have catastrophic consequences.

There are numerous authors on Telegram posting what we would classify as true positive notifications for high-profile employees. These notifications typically include email and password combinations that are currently being used by the high-profile employees.

## Criminal Marketplaces

Like Telegram, criminal marketplaces include data that could have an immediate impact on high-profile employees. Specifically, the majority of the exposed data on criminal marketplaces comes from multiple large breaches of credit card information, and threat actors look to sell credit card data individually and indiscriminately. Threat actors parse the data individually by credit card owner name and list each one for sale, typically for less than $1 USD.

Threat actors do not appear to do research based on the accounts they are selling, which leads us to believe that bot farms are being used to perform automated collection. For instance, if a threat actor knew they had a working credit card — along with the purchasing information of a CEO or high-ranking official — they would likely either raise the price for that individual or attempt to further exploit the information.

“Carder Market” is a broker site that sells exposed credit card information, including the PII data needed to make online transactions. The site is nondiscriminatory and lists all accounts available after a purchase of $0.25 USD. This alludes to bot behavior, which is confirmed when attempting to identify the perpetrators — in this case, the perpetrator is one account identified as “Admin.” Though accounts are indiscriminately posted, high-profile employees could be targeted by searching for a specific name and suspected home of record within the data.

## Public Repositories

Unlike chat mediums and criminal marketplaces, public repositories include highly targeted information. On public repositories, Counter Adversary Operations observed data of three types of high-profile employees: government officials, influential figures and C-suite personnel. The exposed PII included residence addresses, phone numbers, IP addresses, Social Security numbers, personal email addresses, detailed credit card information (including expiration date and security code) and vehicle plate numbers.

With the abundance of information included on these sites, bad actors have a higher potential to exploit high-profile employees either by harassing them or using their credit card/SSN information.

The public repositories we observed included Doxbin, Pastebin and GitHub. All three public repositories allow users to post anonymously (and high-profile employee material was posted anonymously), allowing bad actors to easily obfuscate themselves and their intentions.

## Forums

Malicious forum posts observed by our team are largely used to create and spread conspiracy theories or make derogatory statements related to individuals who have high name recognition. These posts are meant to degrade the reputation of an individual, but we rarely see posts containing sensitive data that could compromise the individual’s corporate credentials.

For this category, the source that generated the most true positive notifications is 4chan. All true positive notifications on 4chan are posted under _anonymous_ accounts. These posts are not limited to PII, as with other source categories. Many 4chan posts concerning high-profile employees are antisemitic in nature and usually end up being linked to an existing conspiracy theory. Something that is also unique to 4chan is the posts almost always target CEOs and additional executive employees.

Counter Adversary Operations has witnessed cyber threats turn into physical acts of targeting on 4chan. For example, our team observed a political discourse that devolved into the author posting their disagreement with an individual's political views, resulting in a call to arms where the home of the individual was targeted by a picket line.

## Social Media

Social media sites also included targeted notifications where actors directly targeted high-profile individuals. However, this medium is less prone to data leaking than public repositories. Social media posts include direct harassment of individuals — in most cases, the harassment revolves around a political discourse that led to hate speech from individual actors. Unlike chat mediums, which can be listed privately, social media sites reach a higher swath of application users, and author discourse appears to be a popular topic to gain notice.

The most common site on which Counter Adversary Operations observed this behavior was X (formerly Twitter). Counter Adversary Operations has aided customers in preparing documentation to take down X profiles that are attempting to impersonate high-profile employees' accounts. These impersonating accounts used employees’ profile photos and names, making them more convincing.

The takedown process for social media accounts requires ample evidence of malicious behavior, not just the use of a name and photo. This can create a barrier for the affected user in getting the account taken down.

## How CrowdStrike Counter Adversary Operations Can Help

CrowdStrike Falcon® Adversary Intelligence enables customers to monitor these sites and immediately alerts customers when activity against a high-profile employee is detected. And because CrowdStrike Counter Adversary Operations works with surface, deep and dark web data every day, the team knows which sites to focus on and which are less concerning. CrowdStrike offers an option to add an assigned Counter Adversary Operations analyst to help customers hunt for external threats to brands, employees and sensitive data, allowing their cyber professionals to devote their time to handling actionable data rather than hunting through a complex and ever-changing criminal ecosystem.

#### Additional Resources

  * _Watch this[ short demo](https://www.youtube.com/watch?v=0PjOLMuLIrA) to see how Falcon Adversary Intelligence enables organizations to proactively uncover fraud, data breaches and phishing campaigns to protect their brand from online threats that target their organization._
  * _To find out more about how to incorporate threat intelligence into your security strategy, visit the[ CrowdStrike Falcon Adversary Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Read about the cybercriminals tracked by CrowdStrike Counter Adversary Operations in the[ CrowdStrike 2024 Global Threat Report](/en-us/resources/reports/global-threat-report/)._
  * _[Request a free trial](/en-us/free-trial-guide/) of the industry-leading CrowdStrike Falcon® platform._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)