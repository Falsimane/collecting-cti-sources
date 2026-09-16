# Overview of the Russian-speaking infostealer ecosystem: the logs

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/overview-of-the-russian-speaking-infostealer-ecosystem-the-logs
- **Date :** 2023-05-11

---

## Introduction

In the [first](/blog/overview-of-the-russian-speaking-infostealer-ecosystem-the-distribution) of the two-part blog post on the Russian-speaking infostealer ecosystem, Sekoia analysts highlighted the main distribution channels used by cybercriminals to spread their infostealers to a large public. In this second part, we share our analysis of the phenomenon of large-scale data theft, notably focusing on “logs”, _i.e._ stolen data collected by the infostealers. Since both financially-motivated and State-nexus threat actors add infostealers to their malware toolset, Sekoia monitors and analyses in-depth this infostealer ecosystem to follow the trends.

This blog post aims at presenting the life cycle of logs, the cybercrime marketplaces dedicated to logs and the noticeable schemes recently used by threat actors to exploit the stolen data. It is based on the monitoring of threat actors’ activities on underground forums and Telegram channels, as well as open source reports.

## Logs’ life cycle

## The log that hides the forest of information

In a cybercriminal context, a log is data collected from a host, compromised by an infostealer. A log usually contains sensitive information stored on, and about, the user machine, including:

  * **System information** : OS version and architecture, computer name, user name, CPU and GPU information, keyboard language, hardware ID and other hardware information;
  * **Network information** : IP address, user-agent, location;
  * **Software information** : installed applications, running processes;
  * **Web browser data** : URLs/cookies, URLs/saved credentials, history, autofill, bookmarks, stored credit card information, browser extension data;
  * **Applications** : local data from installed software, including email clients, messengers, cryptocurrency desktop wallets, FTP, VPN;
  * **Documents** : user’s documents on the computer (often matching a list of extensions and location).



The information contained in a log largely depends on the information stealer family which collects the stolen data and the collection configuration set by the attacker. However, Sekoia observed that the most popular infostealer sold as a Malware-as-a-Service (MaaS) would generally collect the information listed above.

## Log driving

The following figure aims at presenting the logs’ cycle of life as seen used by multiple Russian-speaking cybercriminals.

![Logs’ cycle of life representative of Russian-speaking financially motivated cybercriminals. Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6449f9b7f8b2cd1abf5_6a92a413cd1cab63350cfc0b_6a2a7a5309d93b11a451849e.webp)

Figure 1. Logs’ cycle of life representative of Russian-speaking financially motivated cybercriminals. Source: Sekoia

### **Logs collection** by infostealers

In this whole process,the first step consists in collecting the logs. For this purpose, attackers distribute their infostealer which, once executed on the victims’ machine, gathers and exfiltrates sensitive data to their Command and Control (C2) server. The attackers then access collected logs from the malware administration panel, to download them or to manually browse the data lake to retrieve data of interest. Some other infostealer families abuse legitimate services such as the Telegram and Discord platforms for exfiltration, storage and logs access, with data collection and access modalities similar to those previously described.

![Logs access web page on the Stealc administration panel \(source: XSS cybercrime forum\). Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6449f9b7f8b2cd1abf8_6a92a41651d97c29d2a30c05_6a2a7a5409d93b11a45184aa.webp)

Figure 2. Logs access web page on the Stealc administration panel (source: XSS cybercrime forum). Source: Sekoia

### Logs exploitation

When data of interest is collected by a financially motivated threat actor, the obtained information is either exploited or sold for further exploitation.

For direct exploitation, threat actors generally use authentication information (cookies or login credentials) to transfer money, cryptocurrencies, non-fungible tokens (NFT) or any other valuable item or verifiable record from the victims’ accounts to their own. They can also use stolen account remainder to make purchases on online services such as Amazon or Apple. Sekoia analysts assess with high confidence that some threat actors use their logs to perform other lucrative-oriented attacks, business email compromise (BEC) and ransomware attacks. Some attackers also leverage stolen accounts from social media to conduct [phishing campaigns](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers) or spread malware, notably to commit fraud.

Sekoia analysts observed that the ecosystem around the collection and exploitation of infostealer logs is increasingly structured, notably through cybercriminals specialising in exploiting stolen data for profit. Thus, multiple cybercriminals sell their logs on various platforms or marketplaces, which are presented in the logs marketplace section.

Over the past year, we observed multiple cybercrime threat groups using or deploying infostealer during their campaigns, including the Royal ransomware gang with Vidar stealer or former Conti/Trickbot affiliates with Nemesis stealer. There is also evidence of the use of infostealer by Russian-speaking hacktivists, notably illustrated by a partnership between Killnet and Titan stealer. More recently and for the first time in open sources, Google TAG reported on Russia-nexus intrusion set Sandworm’s use of the Rhadamanthys stealer for strategic intelligence collection purposes.

### **Logs processing**

The quality, recency and accuracy of the stolen data sold observed on marketplaces is very heterogeneous. This likely stems from the fact that there is a high amount of logs sold on platforms, whose format largely differs depending on the used infostealer. As cybercriminals are inherently ill-intended, there is also a great risk of scams, with vendors offering false listings for sale. 

Moreover, manipulating databases of thousands or even hundreds of thousands of raw data and files is complex. Hence, to facilitate the qualification and exploitation of stolen data for threat actors, tools and services to parse, check and sort logs are frequently advertised or shared in the cybercriminal Russian-speaking ecosystem. Offered tools or services mainly aim at:

  * Parsing logs generated by multiple stealers to normalise their format;
  * Filtering logs based on domain patterns or keywords pertaining to specific topics (cryptocurrency, bank, social network, casino, video games);
  * Checking the validity of authentication information (cookies or login credentials);
  * Checking for duplicates with other log databases;
  * Sorting log files, folders;
  * Clearing log files based on their extension.



Well known logs parsers advertised on cybercrime forums or Telegram channels include Crystal, BLTools, Paranoid Checker and Profit Maker.

Over the last year, Sekoia observed the **emergence of tools with more advanced capabilities, designed to facilitate, optimise and enrich the exploitation of stolen data** , including:

  * Checking online accounts’ balances;
  * Checking the number of followers on social media;
  * Checking any subscription on accounts;
  * Searching seed phrases for cryptocurrency wallets;
  * Checking for wallet balances;
  * Verifying [2FA](/blog/sneaky-2fa-exposing-a-new-aitm-phishing-as-a-service) activation;
  * Checking for valuable items in video game accounts.



As some online services implement protection mechanisms to detect access from a suspicious location, more advanced tools such as BLTools (see figure 3) use proxy servers to request the online accounts from an IP address located in the same country as the victim.

![Interface of the BLTools logs checking. Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6449f9b7f8b2cd1abf2_6a92a414dae089660dfd158d_6a2a7a5309d93b11a45184a1.webp)

Figure 3. Interface of the BLTools logs checking. Source: Sekoia

### **Logs sale**

The value chain of stolen data is quite wide, mainly due to the diversity of involved threat actors and the heterogeneity of stolen data. These activities are notably streamlined through multiple platforms such as cybercrime forums, fraudulent marketplaces or Telegram channels. Sekoia categorises them into two types: centralised and decentralised platforms.

## Logs marketplaces

### Centralised marketplaces: the cookie monsters!

#### Dedicated marketplaces

Russianmarket, 2easy, and now defunct Genesis Market are prominent centralised marketplaces dedicated to logs harvested by infostealers. Regularly advertised on cybercrime forums, these marketplaces provide threat actors a platform to sell and buy individual logs. Logs are generally **qualified, and exclusive stolen data** are sold between $5 and $100 depending on the volume of authentication data, associated accounts, the location of the victim, and the accuracy of the log.

![Logs sold on Genesis Market as in March 2023 \(before the seizure of the platform\) detailing domains associated to compromised accounts. Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6449f9b7f8b2cd1abfe_6a92a41551d97c29d2a30bbf_6a2a7a5309d93b11a45184a5.webp)

Figure 4. Logs sold on Genesis Market as in March 2023 (before the seizure of the platform) detailing domains associated to compromised accounts. Source: Sekoia

From a seller’s point of view, these platforms facilitate the sale of "logs" to individuals and groups, making the data theft economy more accessible,**lowering the entry barrier of the infostealer ecosystem** , and further illustrating the **professionalisation** of cybercrime.

From a buyer’s perspective,buying harvested data avoids both reconnaissance and initial access efforts, which can require significant resources. Additionally, these marketplaces are gold mines for [Initial Access Brokers](/blog/bumblebee-a-new-trendy-loader-for-initial-access-brokers) (IAB), _i.e._ threat actors specialised in providing access to victims’ networks, generally leveraged to further compromise the whole network and resulting in a ransomware deployment. More broadly, multiple cybercriminals trade on these platforms to leverage stolen credentials in follow-up attacks.

It is worth noting that these platforms also allow threat actors to search for combinations of domains associated with the stolen cookie or username and password, making it (too) easy to find valuable information, such as VPN credentials, administrator accounts, cybersecurity monitoring solutions or sign-in services. Centralised marketplaces also allow attackers to search harvested credentials associated with named targets. It is therefore likely that State-nexus threat actors and intrusion sets purchase credentials associated with the target victim organisation on these fraudulent marketplaces.

A notorious example in leveraging stolen credentials in follow-up attacks is the compromise of the video game company Electronic Arts Inc.'s network by the Lapsus$ threat group in 2021, whose initial intrusion vector was a cookie harvested using an infostealer. A Lapsus$ representative declared they bought the said cookie on Genesis Market. The cookie allowed the attacker to log into an EA’s Slack account and then trick EA's IT support into granting access to the company's internal network. This attack led to the leak of Battlefield, FIFA, and The Sims video games, and the theft of game source code and related EA internal tools.

#### The Genesis Market seizure

Recent events show that **authorities show increasing interest in the ecosystem around data theft** , the root of many cyberattacks. Last year, operations involving the cooperation between law enforcement agencies, police organisations and judicial systems of several countries led to the arrest of several cybercriminals involved in this Russian-speaking infostealer ecosystem. It includes the arrest of a presumed [Raccoon Stealer](/blog/raccoon-stealer-v2-part-1-the-return-of-the-dead) developer by the law-enforcement authorities in Netherlands in March 2022, and the arrest of over a hundred of cybercriminals going along with the seizure of Genesis Market in April 2023.

Dubbed “Operation Cookie Monster”, the joint operation to seize the fraudulent marketplace involved over a dozen international law enforcement agencies (Australia, Canada, Denmark, Estonia, Finland, France, Germany, Iceland, Italy, the Netherlands, Poland, Spain, Switzerland, the US, the UK, Romania, Eurojust and Europol) and private cybersecurity firms. Sekoia analysts expect that the takedown of a major marketplace in the field of stolen data will temporarily slow down malicious activities of threat actors using Genesis Market in the near future. However, it is likely that other centralised marketplaces such as 2easy and Russianmarket will increase their activities to accommodate Genesis Market’s former users. 

The Operation Cookie Monster is also likely to **reinforce the trend and the popularity of decentralised marketplaces** , which have increased in recent years, notably on Telegram.

### Decentralised marketplaces on the rise

At Sekoia, we consider the decentralised marketplaces to be a combination of multiple private or public marketplaces, each**of them operated by a threat actor which itself fills its own marketplace with logs and defines the terms of sale**. In contrast, centralised marketplaces regroup logs from multiple individuals and are controlled by a small community of cybercriminals (administrators) that sets unique rules for all sellers.

#### Clouds of logs

Clouds of logs are private communities usually consisting of a dozen of cybercriminals, regularly hosting bulks of credentials put up for sale by the owner of the platform himself. Customers purchase a paid subscription to a cloud of logs to access thousands of stolen data daily. The pricing of such service is between $200 to $900 a month, depending on the quality and quantity of logs. Clouds of logs are often advertised by their owner in Russian-speaking [cybercrime forums](/blog/a-war-on-multiple-fronts-the-turbulent-cybercrime-landscape) or on Telegram channels dedicated to the infostealer business.

Generally, the bulk of logs are archives of data harvested by infostealers, either directly by the owner of the cloud logs, or by a third party. The owners of the clouds of logs indicate:

  * The source of the logs,_i.e._ through which distribution channel were the victims compromised and where the victims are;
  * The format of the logs, usually depending on the Malware-as-a-Service infostealer that collected them;
  * The type of data: it is indicated whether they include cookies and documents (full logs) in addition to the common “url:login:password”, “domain:login:password” and “email:password”.



Based on our observations, the clouds of logs’ owners share between 1 and 15 thousands of logs per day with their community.

![BSC cloud of logs advertised on Telegram. Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6449f9b7f8b2cd1abfb_6a92a4179f9b7f8b2cd08e7e_6a2a7a5409d93b11a45184ad.webp)

Figure 5. BSC cloud of logs advertised on Telegram. Source: Sekoia

To illustrate, the owner of the BSC cloud of logs allegedly provides 10,000 unique fresh logs daily. A subscription for one month costs $2,299. In December 2022, its cloud of logs contained over 300,000 logs - 25% of them came from European victims, 10% from the US and 65% elsewhere in the world.

Dozens of cloud of logs similar to this one exist on Telegram, with varying levels of reliability. Some of them occasionally offer free bulks of logs to promote their service. We observed that with this selling and sharing model, cybercriminals can easily retrieve the logs from a private group and resell them, which appears to be one of the limitations of decentralised marketplaces under the “cloud” format.

#### Telegram bots

Cybercriminals also sell specific logs on decentralised Telegram channels. For this purpose, they are using Telegram bots to interact with potential customers. Interested customers credit their account to buy a number of logs that matches their search. In the following example a simulation of an interaction with the Omega bot with the term “Lufthansa” yields 500 matching logs, likely originating from compromised accounts of the German airline’s website.

![Interactions with the Omega Request Telegram bot selling logs. Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6449f9b7f8b2cd1abef_6a92a418fd507e2a51b9a2a6_6a2a7a5409d93b11a45184cb.webp)

Figure 6. Interactions with the Omega Request Telegram bot selling logs. Source: Sekoia

From our observations, the number of Telegram bots selling logs is limited compared to the currently available Telegram clouds of logs. However, it is possible that newcomers will emerge, notably to meet the demand created by the takedown of Genesis Market, as the possibilities offered to customers are quite similar.

## Conclusion

The infostealer threat level continuously increased in recent years and the associated Russian-speaking ecosystem became more and more professional, as we regularly illustrate in our FLINTs on this subject. The economy of data harvested by infostealers (from exploitation to sale, through log processing) is not exempt from the professionalisation of the cybercrime ecosystem.

Given the multitude of threat actors involved in the Russian-speaking infostealer ecosystem, this threat must be closely monitored by organisations, as the exploitation of harvested credentials can lead to exposing their systems to follow-up cyber malicious activities. Some security companies provide their customer data leak detection and asset security monitoring to identify potential stolen data on cybercrime marketplaces. Protection is also achieved through anticipation, thanks to the attacker's knowledge and the context provided by the Sekoia’s Threat & Detection Research (TDR) team.

To provide our customers with actionable intelligence, Sekoia analysts will continue to monitor emerging and prevalent infostealers and follow trends related to this Russian-speaking infostealer ecosystem.

Thank you for reading this blog post. Feel free to share your feedback, and read other TDR reports here:

  * [Overview of the Russian-speaking infostealer ecosystem: the distribution](/blog/overview-of-the-russian-speaking-infostealer-ecosystem-the-distribution)
  * [Traffers: a deep dive into the information stealer ecosystem](/blog/traffers-a-deep-dive-into-the-information-stealer-ecosystem)
  * [Stealc: a copycat of Vidar and Raccoon infostealers gaining in popularity – Part 1](/blog/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-1)
  * [Unveiling of a large resilient infrastructure distributing information stealers](/blog/unveiling-of-a-large-resilient-infrastructure-distributing-information-stealers)
  * [Lapsus$: when kiddies play in the big league](/blog/lapsus-when-kiddies-play-in-the-big-league)