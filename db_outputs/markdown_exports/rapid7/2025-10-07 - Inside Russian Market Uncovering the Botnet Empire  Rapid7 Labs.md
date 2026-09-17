# Inside Russian Market: Uncovering the Botnet Empire | Rapid7 Labs

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-inside-russian-market-uncovering-the-botnet-empire/
- **Date :** 2025-10-07

---

_Eliran Alon contributed to this post._

## Inside Russian Market: Key insights from Rapid7 threat research

The online cybercrime marketplace, Russian Market, has evolved from selling Remote Desktop Protocol (RDP) access to becoming one of the most active underground hubs for information-stealing malware logs, where stolen user credentials are traded daily. Each compromised login represents a potential gateway into corporate systems, enabling threat actors to launch credential-based attacks that put businesses, governments, and individuals at risk of account compromise and follow-on cyberattacks. Notably, several high-profile breaches have been traced back to credentials purchased on marketplaces like Russian Market—demonstrating how a single exposed password can lead to significant data loss, financial damage, and reputational harm.

The growing demand for stolen credentials is fueled by widespread campaigns that deploy information-stealing malware, infecting employees both in the office and at home, and silently harvesting logins that may already be circulating underground. This reality significantly raises the likelihood of corporate credentials being exposed, making monitoring for stolen employee logins essential. Russian Market, however, is a gated community that employs anti-scraping measures, creating substantial challenges for defenders trying to track stolen data. By profiling key vendors and malware variants, our research provides a rare inside look at Russian Market’s operations, underscoring why organizations must act now to strengthen credential monitoring and enhance detection capabilities.

### Russian Market at a glance:

  * Russian Market has evolved its operations over time, shifting from selling RDP access to stolen credit card data and, more recently, infostealer logs, in a strategic pivot toward more scalable and potentially lucrative offerings.

  * Stolen credentials originate from organizations worldwide, with 26% originating in the US and 23% in Argentina.

  * Over 180,000 infostealer logs were offered for sale in the first half of 2025, with the marketplace largely dominated by three key vendors: Nu####ez, bl####ow, and Mo####yf.

  * Most sellers have adopted a multi-stealer approach over the years, leveraging various malware variants in their operations, with Lumma emerging as a widely used tool.

  * The most common types of infostealers being used by sellers in Russian Market over the years have been Raccoon, Vidar, Lumma, RedLine, and Stealc, with Rhadamanthys and Acreed gaining popularity in the first half of 2025. 




## How information-stealing malware fuels the underground economy

Information-stealing malware remain among the most persistent threats in today’s cyberthreat landscape, enabling threat actors to extract sensitive credentials and pave the way for high-impact cyberattacks. Credentials harvested through these infostealers are frequently traded on deep and dark web marketplaces, where cybercriminals connect to buy and sell access to compromised accounts and systems.

Among these illicit platforms, the cybercrime marketplace, Russian Market, stands out as one of the most active and enduring. Every day, hundreds of infostealer logs with stolen credentials are put up for sale, fueling a thriving underground economy. Unlike other cybercrime forums and marketplaces, such as BreachForums and XSS, that have been disrupted in recent years, Russian Market has maintained a steady presence since its emergence in early 2020.

This article examines the evolution and current operations of Russian Market, shedding light on its most prolific sellers and assessing its influence within the broader cybercrime ecosystem.

## Russian Market and the dark web economy

With an average of approximately 30,000 “bots” offered for sale each month in the first half of 2025, Russian Market has established itself as the leading cybercrime marketplace for stolen credentials. Its portfolio, however, has evolved significantly over the years, as the platform has undergone multiple transformations since its emergence in the cybercrime ecosystem. Below is a brief overview of these changes:

  * **2020 – 2024 | RDP Access Sales**  
At its inception, Russian Market specialized in selling Remote Desktop Protocol (RDP) access and login credentials to compromised computers. Such access was frequently exploited for ransomware deployment, cyberespionage, or as a launchpad for further attacks from seemingly legitimate systems. From 2020 until the service was discontinued in January 2024, RDP access was commoditized and widely traded within the cybercrime economy.

  * **2021 – Present | Credit Card Offering**  
In 2021, Russian Market shifted its focus and rapidly emerged as a dominant player in the stolen credit card trade. Driven by an aggressive expansion strategy and a prevailing sense of impunity, the platform grew quickly, at its peak overshadowing other carding forums and marketplaces.

  * **Late 2021 – Present | The Credentials Era**  
Later in 2021, Russian Market launched a new product line: _“Bots.”_ These are not traditional botnets of infected devices, but rather data logs exfiltrated from compromised machines, typically using information-stealing malware (_“infostealers”_). Each bot typically contains:

    * Cookies

    * Credentials

    * Autofill data

    * Session tokens




Today, beyond the sheer volume of its offerings, a defining feature that distinguishes Russian Market from competitors is its usability. Within the “Logs” section, buyers can filter results by geography, operating system, infostealer, and vendor to identify bots relevant to their needs quickly. Additionally, the “links” field enables searches for bots containing credentials tied to specific domains or even individual email addresses (Figure 1).

⠀

![Figure_1.png](https://www.rapid7.com/cdn/images/bltdbfcd93ed822597f/68e687b6c43e2f98697bda45/Figure_1.png)

_Figure 1 - List of bots for sale on Russian Market_

⠀

While the associated geographies differ in breadth, the bots predominantly contain credentials for users in the United States, with Argentina and Brazil following. This distribution further reflects the global spread of infostealer infections (Figure 2).

⠀

![Figure_2_V2.png](https://www.rapid7.com/cdn/images/bltbdad17bf1865cadb/68e68938f0b3bd8302593075/Figure_2_V2.png)

_Figure 2 - 20 most targeted countries by bot count_

⠀

It should be noted that each bot typically contains credentials for multiple domains. The number of credentials is often correlated with the bot’s size, with larger bots generally storing more data. In the first half of 2025, bot sizes ranged from 0.05 to 0.3 megabytes, with an average size of 0.14 megabytes. Figure 3 below represents the 30 most common bot sizes in descending order per bot count.

⠀

![Figure_3_V3.png](https://www.rapid7.com/cdn/images/blt94f780cfce5ce8f3/68e68938758f5b4594d9e5b6/Figure_3_V3.png)

_Figure 3 - Bot size distribution_

⠀

In the first half of 2025, bots were typically listed for sale on Russian Market at around $10, a price that remained consistent across vendors. Historically, however, bot prices on the marketplace have ranged from $1 to $100, depending on factors such as geolocation, browser session quality, and the validity of login data.

## Key vendors behind Russian Market's botnet empire

Despite the large number of bots available for sale on Russian Market, the marketplace is dominated by just a few sellers. Since bots were first introduced in 2021, three vendors, operating under the aliases Mo####yf, de####nt, and Nu####ez, have been responsible for nearly 70% of all detected bot listings (Table 1).

⠀

![Table_1_V2.png](https://www.rapid7.com/cdn/images/bltdb831ab7a62451bc/68e6893955fd274f60d8ad66/Table_1_V2.png)

_Table 1 - Top sellers per market share_

⠀

While Mo####yf and Nu####ez continued to hold a strong presence on Russian Market in the first half of 2025, de####nt’s market share plummeted to just 0.23%. At the time of writing, no bots are attributed to this seller, suggesting they were likely banned or removed from the platform (Figure 4). Such removals are not unusual, as administrators of dark web marketplaces frequently restrict or expel members who appear to violate platform rules.

⠀

![Figure_4.png](https://www.rapid7.com/cdn/images/bltcafd18f04decf0cf/68e687b532b3a97aaff21703/Figure_4.png)

_Figure 4 - Search results for de####nt_

⠀

In the first half of 2025, new sellers using the aliases bl####ow, sm####ez, and co####er gained prominence on Russian Market (Figure 5). During this period, Nu####ez remained the leading vendor with a 38% market share, followed by bl####ow at 24% and Mo####yf at 19%. It is worth noting that the activity levels of all sellers, even the most dominant, fluctuated from month to month (Figure 6).

⠀

![Figure_5_V2.png](https://www.rapid7.com/cdn/images/bltd649beaba635a7d8/68e689387173c483c8eb8af2/Figure_5_V2.png)

_Figure 5 - Bot count per seller_

⠀

![Figure_6_V2.png](https://www.rapid7.com/cdn/images/bltdcc114e253bb59e7/68e68938c124d37b3a05cb2c/Figure_6_V2.png)

_Figure 6 - Seller’s monthly activity_

⠀

Reputation, a critical trust-building mechanism across cybercrime platforms, also plays a central role in Russian Market. The marketplace implements a structured reputational system designed to assess the perceived reliability of vendors, despite their reliance on pseudonymous aliases. Each seller is assigned a numerical score calculated from two primary factors: the volume of items offered for sale and the feedback provided by buyers following transactions. This score is then aggregated into an overall vendor rating on a five-point scale, complemented by a tiered status system. Vendors exceeding a score of 10,000 are assigned a “Diamond” status, while those below this threshold are designated “Platinum.” Such reputation tiers not only influence buyer trust and purchasing decisions but also serve as a competitive differentiator among sellers, incentivizing sustained activity and positive feedback generation.

Each of the prominent vendors in the first half of 2025, namely Nu####ez, bl####ow, Mo####yf, sm####ez, and co####er, is presented further in more detail.

### Nu####ez

Active since at least January 2024, Nu####ez currently holds a “Diamond” status with an overall score of 4.41 (Figure 7). In 2025, the vendor was observed leveraging multiple infostealers, primarily Lumma, Rhadamanthys, and Acreed, to harvest credentials. Previously, in 2024, Nu####ez had relied on Vidar and Stealc. The consistent use of diverse infostealers, combined with the vendor’s heightened activity, indicates an intent to sustain and expand offerings despite fluctuations in infostealer availability, such as those caused by law enforcement disruptions. This behavior may also reflect deliberate experimentation, allowing Nu####ez to evaluate and compare the effectiveness of different infostealers in terms of output and reliability.

⠀

![Figure_7.png](https://www.rapid7.com/cdn/images/blta690dae0c0185a3a/68e687b59975a5019197a30e/Figure_7.png)

_Figure 7 - Nu####ez’s profile on Russian Market_

###  bl####ow 

Active since at least October 2024, bl####ow currently holds a “Diamond” status with an overall score of 4.78 (Figure 8). In contrast to vendors such as Nu####ez, who diversify their operations across multiple infostealers, bl####ow appears to rely exclusively on Lumma for credential harvesting. While this heavy dependence on one malware variant makes bl####ow potentially susceptible to disruptions, the vendor’s heightened activity in 2025 suggests that Lumma has thus far demonstrated resilience and operational consistency.

⠀

![Figure_8.png](https://www.rapid7.com/cdn/images/blt3c0dbec0d8dbda33/68e687b5c7f3775c743fb3e7/Figure_8.png)

_Figure 8 - bl####ow’s profile on Russian Market_

###  Mo####yf 

Active since at least April 2023, Mo####yf currently holds a “Diamond” status with an overall score of 4.50 (Figure 9). Initially, the vendor appears to have offered credit card data, but later shifted their attention to bot sales, which remained their primary focus. In 2025, Mo####yf primarily relied on Lumma for credential harvesting, while in 2024, the vendor had utilized Stealc and Vidar. This shift in tooling indicates a flexible and adaptive approach to infostealer selection, likely driven by factors such as performance, reliability, and operational efficiency.

⠀⠀

![Figure_9.png](https://www.rapid7.com/cdn/images/blt9923f568898a92ae/68e687b6c2504ec9dd1fe8a6/Figure_9.png)

_Figure 9 - Mo####yf’s profile on Russian Market_

###  sm####ez

Active since at least July 2023, sm####ez currently holds a “Diamond” status with an overall score of 4.48 (Figure 10). In 2025, the vendor primarily relied on Lumma for credential harvesting, whereas in 2024, they employed a combination of Vidar, RedLine, and Stealc. This multi-stealer approach likely enabled sm####ez to evaluate and compare the performance of different tools before settling on Lumma as the primary infostealer. The use of multiple infostealers and the resulting variability in operational outcomes likely contributed to fluctuations in user feedback during that period.

⠀

![Figure_10.png](https://www.rapid7.com/cdn/images/blt6184212bab4ed720/68e687b54f6743d3644773d5/Figure_10.png)

_Figure 10 - sm####ez’s profile_

###  co####er

Active since at least January 2025, co####er currently holds a “Platinum” status with an overall score of 4.38 (Figure 11). The vendor primarily relies on Lumma for credential harvesting, though Stealc has also been used in select cases. Co####er’s use of a widely adopted and reliable infostealer likely contributed to their rapid rise, positioning them among the most active sellers on Russian Market in 2025.

⠀

![Figure_11.png](https://www.rapid7.com/cdn/images/blte3328510b8fd226c/68e687b56c0dd2e379d37ea6/Figure_11.png)

_Figure 11 - co####er’s profile_

## Russian Market's top infostealer families

The sellers on Russian Market usually utilize similar types of information-stealing malware, with some of the most frequent ones being the following. As detailed further, all infostealers share similar traits and the same end goal: exfiltrating sensitive data from targeted servers. The table below lists the most common infostealers used by Russian Market sellers since 2021 (Table 2).

⠀

![Table_2_V3.png](https://www.rapid7.com/cdn/images/blt7efe4ab7cde8be7c/68e689386c0dd24079d37ec4/Table_2_V3.png)

_Table 2 - Most common infostealers used by Russian Market sellers since 2021_

####  Raccoon

The Raccoon information-stealing malware (AKA Mohazo, Racealer) was first observed by cybersecurity researchers in April 2019. Globally distributed as a malware-as-a-service (MaaS), Raccoon has infected hundreds of thousands of Windows devices in countries such as the United States, the United Kingdom, France, Germany, Italy, India, and Australia. The malware is considered by some as the successor of the now-defunct Azorult infostealer.

The malware, written in C++, is usually distributed through malvertising or phishing email message campaigns. It was also observed spreading through lure web pages redirecting users to landing sites containing exploit kits (e.g., Fallout and RIG exploit kits) or exhorting them to download seemingly legitimate software. Once installed, the infostealer connects to a command and control (C2) server and downloads a specific DLL file that is required for the exfiltration process. It then starts to collect sensitive information, such as system information, user credentials, and web browser information, including cookies, autocomplete data, history logs, and credit card information. It can also take screenshots, harvest cryptocurrency, and serve as a dropper for other malicious files. Raccoon deletes itself at the end of the exfiltration process.

Some members of the underground community attribute Raccoon to a user nicknamed “glad0ff,” who is the developer of other malware, such as Decrux, Acrux, and the Mimosa RAT. Other members link it to other infostealer malware, such as Vidar and Baldr, due to many similarities between them.

In March 2022, the Raccoon operators announced that they had suspended their activities after one of the malware developers died during the war in Ukraine (Figure 12). However, the threat actors resumed their operation a few months later with a new version of Raccoon.

⠀

![Racoon.png](https://www.rapid7.com/cdn/images/blt296f852908050c5e/68e68c01c7f3772e133fb429/Racoon.png)

_Figure 12 - Raccoon’s operation suspension message_

####  Vidar

Vidar is a malware family, distributed mainly as an infostealer, that has been active since at least October 2018. The infostealer, whose name originates from Norse mythology, is based on Arkei stealer and is one of the first infostealers that is capable of obtaining information on two-factor authentication (2FA) software and the Tor browser.

Vidar usually spreads through phishing email messages, soliciting the victims to download and execute it. In addition, it was observed spreading through direct messages on social networks and false advertisements in various gaming forums. The malware is used to steal various types of sensitive information, such as documents, cookies, system information, user credentials, and money from cryptocurrency wallets. In addition, it can take screenshots of the victim’s machine. The stolen information is then exfiltrated to a corresponding C2 server.

The infostealer has been used as part of numerous malvertising campaigns that even involved the deployment of ransomware, such as GandCrab, Zeppelin, and DeathRansom. 

#### Lumma****

The Lumma Stealer malware (AKA LummaC2) was first observed in August 2022, being sold by the threat actor, Shamel (AKA Lumma), on a Russian underground forum. Distributed as malware-as-a-service (MaaS), the infostealer is used by various threat actors in multiple campaigns around the world. Lumma Stealer seems to be based on Mars Stealer and Arkei.

Lumma Stealer, written in C, is primarily spread through malicious websites that promote illegal programs, such as software cracks and keygens. It was also observed being delivered using phishing email messages with malicious links. Once deployed (sometimes injected using PureCrypter), the malware collects general system information (for example, CPU name, physical memory, and system language) and harvests TXT files, cryptocurrency information, two-factor authentication (2FA) tokens, and web browser data (such as browser history, login information, and network cookies). The stolen information is then packed in a ZIP archive, which is exfiltrated to a C2 server over HTTP POST. To evade detection, Lumma Stealer performs anti-sandbox and anti-debugging checks while also being equipped with string and code obfuscation.

In May 2025, a coordinated law enforcement activity successfully disrupted Lumma Stealer’s operation. The authorities seized approximately 2,300 domains and part of Lumma Stealer’s infrastructure backbone based in Europe and Japan. However, only two months later, it was reported that the malware operation was gradually resuming activities.

#### RedLine****

The RedLine Stealer malware was first detected in February-March 2020 during the COVID-19 pandemic. It was part of a malspam campaign that encouraged victims to help fight the Coronavirus by installing a “legitimate” application on their system. The malware has been offered for sale on several Russian underground forums, with its price varying depending on the version (standalone/subscription) and other customization services sold by the threat actor.

RedLine Stealer, written in C#, is constantly improving its capabilities and efficiency. Its main purpose is to harvest information from the victims’ infected machines, such as saved login credentials, credit card numbers, FTP servers, web browser data, instant messaging clients, and cryptocurrency wallet numbers. The malware can bypass security products, steal downloaded files, execute commands, and send all the collected data to a remote C2 server.

#### Stealc****

The Stealc information-stealing malware was first reported by cybersecurity researchers in February 2023 after it was promoted on a Russian-speaking underground forum by a user named “Plymouth.” The malware’s code, written in C, is based on the following infostealers: Vidar, Raccoon, Mars, and RedLine. 

Like other infostealers, Stealc is assumed to be distributed through malicious installers for allegedly cracked software. Once deployed, the malware deobfuscates its strings (mostly obfuscated with RC4 and Base64) and checks that it is not operating in a virtual environment or sandbox. When this passes, Stealc dynamically loads WinAPI functions and establishes a connection to a C2 server. Then, the infostealer starts collecting general system information and harvesting data from web browsers (for example, cookies, autofill data, and browsing history), extensions, cryptocurrency wallets, and different installed apps, such as Discord, Telegram, Outlook, and Steam. In addition, Stealc retrieves a custom file grabber to steal certain file types that are predetermined by its operators. The data is then exfiltrated to the C2 server over HTTP POST, and all traces of the malware are wiped from the system.

In October 2024, the Dutch National Police seized the network infrastructure for RedLine as part of Operation Magnus. However, the infostealer’s operation seems to continue despite these law enforcement activities. 

### 2025 overview of infostealers

Examining the most frequently utilized infostealers in Russian Market in the first half of 2025 (Figure 13), we can see that, besides the four infostealers mentioned earlier, two additional infostealers recently turned popular among sellers, Rhadamanthys and Acreed. This is in parallel with the decline in the use of Raccoon. Lumma Stealer has dominated the infostealers market in the first four months of the year, but there is a noticeable decline in its supremacy since the law enforcement activities against it in May 2025. 

⠀

![Figure_13_V3.png](https://www.rapid7.com/cdn/images/blt39d9885fbabd04ce/68e68938c124d35b4705cb28/Figure_13_V3.png)

_Figure 13 - Most frequently utilized infostealers in Russian Market in the first half of 2025_

####  Rhadamanthys

The Rhadamanthys information-stealing malware has been active since at least August 2022. The malware-as-a-service (MaaS) was discovered after it was put on sale on underground hacking forums. 

Rhadamanthys spreads through malicious Google Ads or phishing email messages that lead the victims to seemingly legitimate websites of popular software, such as Zoom, AnyDesk, and Notepad++. Once executed, Rhadamanthys collects general system information (e.g., computer name, username, and OS version) using Windows Management Instrumentation (WMI) queries and then starts harvesting data from web browsers (e.g., browsing history, cookies, and login credentials), cryptocurrency wallets and extensions, and other applications, such as FTP and email clients, file managers, password managers, and messaging platforms. In addition, it can take screenshots of the victim’s machine. All the collected data is exfiltrated to a remote C2 server that is accessed through a dedicated panel. 

#### Acreed

The Acreed information-stealing malware has been active since at least February 2025. Cybersecurity researchers assert that the use of Acreed soared following the downturn of Lumma Stealer, as a result of law enforcement activities.

Acreed is distributed through phishing email messages with malicious attachments or links, malvertising campaigns promoting malware-embedded installers for legitimate software, ClickFix attacks using fake CAPTCHA, or malicious tutorials on social platforms, such as YouTube and TikTok. Once executed, the malware exfiltrates general system information (for example, username, IP addresses, and HWID), web browser data, including cookies and saved passwords, cryptocurrency information, and session tokens from cloud platforms, such as Microsoft 365, Google, AWS, Azure, and Salesforce. At the end of the collection process, the infostealer produces a JSON file that details the number of files gathered from each type of data (Figure 14).

⠀

![Figure14.png](https://www.rapid7.com/cdn/images/blt89d283718789f899/68e68cbf758f5b1bced9e5c7/Figure14.png)

_Figure 14 - An example of content harvested by Acreed and sold on Russian Market_

## What organizations should do

Russian Market manifests a dynamic and persistent cybercrime ecosystem that has become a dominant hub for stolen user credentials and information-stealing malware logs. The marketplace’s unconventional endurance, compared to other major underground venues, makes it a primary generator of cybercriminal activity, fueling a wide array of cyberattacks globally. Despite law enforcement efforts targeting cybercrime marketplaces and malware operations, the core operations of Russian Market and its prolific sellers continue, demonstrating the resilience and adaptability of these illicit platforms.

Analyzing the main forces that function in this unlawful domain reveals a very short list of entities facilitating the entire operation, with only one or two major players joining the fray each year. The same goes for the infostealers they use, which are replaced every once in a while due to law enforcement activity, but are generally drawn from the same, closed set. 

For organizations, the pervasive trade of stolen credentials on platforms, such as Russian Market, necessitates robust defenses, including multi-factor authentication, continuous monitoring for compromised accounts, and proactive threat intelligence. Understanding the mechanics and key players within Russian Market is crucial for developing effective strategies to combat the escalating threat of credential-based cyberattacks. 

## Detections for Rapid7 customers

There are multiple detections currently in place for our MDR Customers to identify and alert on the common infostealer threat actor behaviors described in this blog, including Redline, Lumma, Vidar/Stealc, and Raccoon. Specifically:

#### Redline

  * ET MALWARE RedLine Stealer - CheckConnect Response

  * ET MALWARE Redline - GetArguments Request




#### Lumma

  * Suspicious Process - Lumma Stealer Related Process Executed

  * Suspicious Web Request - Lumma Stealer URL Observed

  * IDS (ET MALWARE) related detections




#### Vidar/Stealc

  * Suspicious Process - Vidar/Stealc Related Binary Executed

  * Suspicious Web Request - Vidar/Stealc Stealer URL Observed

  * IDS (ET MALWARE) related detections




#### Raccoon

  * IDS (ET MALWARE) related detections for C2 domains




### Intelligence Hub 

Customers leveraging Rapid7’s Intelligence Hub can access indicators of compromise (IOCs) related to Vidar and Lumma, as well as the latest developments and associated campaigns.

In addition to the above, there are multiple detections in place for Threat Command and MDRP customers to identify and alert on the threat actor behaviors described in this blog. Specifically, Threat Command monitors dark web activity, including company credentials harvested with infostealers and sold on Russian Market. Relevant bots are flagged based on the customer’s assets—such as domains, brand names, company names, external IP addresses, or login pages. When a bot containing these assets is identified, a “Bot Data for Sale” alert is issued (Figure 15). In addition to notifying customers of credential exposure, these alerts enable them to quickly and securely acquire the detected bot through the “Ask an Analyst” service.

⠀

![Screenshot_2025-09-30_at_14.04.49.png](https://www.rapid7.com/cdn/images/blt5af21cdeef2e5d42/68ee4729c43e2f25c57bf501/Screenshot_2025-09-30_at_14.04.49.png)

_Figure 15 - Example of an alert about a bot available for sale on Russian Market_

## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)
  * [Malware](/blog/tag/malware-latest-news/)