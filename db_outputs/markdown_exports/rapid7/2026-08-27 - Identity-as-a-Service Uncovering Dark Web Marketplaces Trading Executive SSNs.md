# Identity-as-a-Service: Uncovering Dark Web Marketplaces Trading Executive SSNs

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-identity-as-a-service-dark-web-marketplaces-executive-ssn/
- **Date :** 2026-08-27

---

## Introduction

Despite modern verification controls, identity theft remains one of the most pervasive threats to both individuals and enterprise organizations. U.S. Federal Trade Commission statistics show over 1 million identity theft reports annually, with related fraud and imposter scams accounting for billions in financial losses each year. While stolen credit cards enable rapid, short-term monetization, Social Security numbers (SSNs) represent a far more permanent and dangerous tier within the cybercrime ecosystem, because unlike payment cards, they cannot simply be deactivated. Once exposed, an SSN can support enabling unauthorized lines of credit, synthetic identity fraud, and sophisticated tax scams.

When exposed identity data belongs to corporate executives, board members, and other high-profile employees, the risk can extend beyond the individual. Threat actors target these high-profile individuals not just for their premium credit profiles, but to leverage their compromised identities for executive impersonation, corporate espionage, and downstream extortion. Rapid7’s recent alert telemetry underscores the severity of this targeted exposure: since early 2026 alone, we identified 476 instances of compromised SSN records across 395 unique corporate personnel. Over 73% of these exposures directly targeted top-level leadership, with C-suite executives comprising 44.6% of affected profiles and Presidents making up another 28.6%. Unsurprisingly, given the geographical nature of SSNs, 95.6% of these leaks stemmed from U.S.-headquartered organizations, concentrated heavily in high-value sectors like Financials (over 25%) and Industrials (17%).

In this blog, we explore the operational mechanics of the underground identity economy, focusing on three dominant SSN marketplaces tracked by Rapid7: Xilo, Bankom, and PeopleFinder, which together account for 81.5% of all executive SSN leaks in our dataset (led by Xilo at 40.8%, Bankom at 21.8%, and PeopleFinder at 18.9%). Using Rapid7 alert telemetry from the past year, we look at the profiles of affected corporate executives, how these marketplaces operate, and highlight how proactive dark web monitoring can mitigate upstream identity exposure before it is weaponized.

## Why stolen SSNs retain their value

Not all stolen data retains its value for the same length of time. Leaked credentials can be reset, payment cards can be cancelled, and session tokens eventually expire. While these data types remain highly sought after by cybercriminals, their usefulness often depends on acting quickly before the victim or service provider invalidates them.

SSNs differ as they are effectively permanent, serving as a core identity attribute. Once exposed, they can remain valuable for years, enabling a wide range of fraud schemes long after the original breach. When combined with other personally identifiable information (PII), such as a victim's name, date of birth, address, phone number, and employment history, an SSN becomes the foundation of a comprehensive identity profile that can be bought, sold, and repeatedly abused across the criminal ecosystem.

These identity profiles enable far more than traditional identity theft. Threat actors use them to open fraudulent financial accounts, create synthetic identities, bypass identity verification processes, file fraudulent tax or government benefit claims, and support highly targeted social engineering campaigns. Rather than serving a single purpose, a complete identity record becomes a reusable asset that can be monetized multiple times by different threat actors.

For corporate executives and other high-profile employees, exposed identity data can also create risk for the organization they represent. Publicly available information, from regulatory filings to corporate biographies and social media, can be combined with stolen identity data to build highly detailed profiles. These enriched records increase the credibility of phishing, business email compromise (BEC), and executive impersonation attacks, allowing threat actors to target not only the individual but also the organization they represent.

This durability has fueled a thriving underground economy where identity records are treated as searchable, reusable inventory rather than one-time commodities. The marketplaces examined in this research demonstrate just how mature and accessible this ecosystem has become.

## Anatomy of an SSN marketplace

While platforms like Xilo, Bankomat, and PeopleFinder present a highly organized, user-friendly storefront, they operate strictly as downstream clearinghouses rather than original creators of their inventory. The vast supply of SSNs flooding these networks relies on a distinct, multi-tiered underground supply chain. The massive volume driving these platforms is primarily fueled by large-scale institutional network breaches, where wholesale hackers compromise data aggregators, healthcare systems, and financial providers. These massive SQL databases are sold in bulk on deep-web forums, where marketplace administrators purchase, parse, and upload them into their searchable storefronts. According to annual telemetry from the Identity Theft Resource Center, billions of individual data records are exposed annually through these mega-breaches, accounting for the vast majority of the inventory available online.

Another source of identity data comes from infostealer malware and targeted phishing campaigns. While mass breaches provide wholesale numbers, infostealers scrape highly contextual local data, such as saved browser forms and PDF documents like tax returns or corporate onboarding paperwork stored on unmanaged personal devices. When these localized logs are parsed by marketplace administrators, they yield the fresh, high-value identity profiles that allow buyers to target specific corporate leaders.

Although these platforms tap into a similar upstream supply chain, how they package and monetize this data varies significantly. To stand out in a maturing, highly competitive cybercrime market, each marketplace focuses on its own operational niche, ranging from ultra-low pricing and identity enrichment features to multi-asset carding integration and legacy data consistency. The following sections provide a deep dive into each marketplace, highlighting their specific functionalities, user interfaces, and distinct market advantages.

### Xilo 

Xilo has been active since at least March 2025. The marketplace is hosted as a Tor hidden service, while also maintaining mirror sites on the clear web to improve accessibility and resilience.

Users can search for specific individuals by name, state, country (US or Canada), or year of birth (Figure 1). They can also request records that include phone numbers and email addresses in addition to the victim's SSN. This can increase the value of the records by reducing the need for threat actors to source additional PII elsewhere. During our analysis, however, we did not identify any records that included email addresses, while records containing phone numbers were available at the same price as standard SSN records. Search results can also be sorted by price, although the cost appears to be fixed at $0.25 per SSN record.

![Xilo-search-interface.png](https://www.rapid7.com/cdn/images/blteda19dbdc405f202/6a90417460f7951d49d75eb7/Xilo-search-interface.png) _Figure 1 – Xilo search interface_

⠀

Search results typically display the victim's full name, physical address, and date of birth before purchase. This information alone can help threat actors identify specific individuals for targeted campaigns, while the SSN is revealed only after the purchase is completed (Figure 2).

![xilo-search-results.png](https://www.rapid7.com/cdn/images/blt5b7d664480dc4a31/6a9041c00a3bbeb38059e261/xilo-search-results.png) _Figure 2 – Xilo search results_

⠀

In addition to standard searches, Xilo offers a reverse lookup service that accepts an SSN or phone number and returns additional PII, including the victim's full name and phone number (Figure 3). This service costs $0.50 per lookup, suggesting that enriching an existing identity profile is considered more valuable than purchasing an SSN alone. Threat actors can use this functionality to expand records obtained through the standard search, increasing the amount of PII associated with a single individual and, consequently, the potential for identity fraud.

![xilo-reverse-search.png](https://www.rapid7.com/cdn/images/bltffe316bdd83f65d5/6a9041f5d05d4c308e580ae5/xilo-reverse-search.png) _Figure 3 – Xilo reverse search_

⠀

The marketplace is supported by a Telegram channel used to announce technical updates and new domains. Although activity on the channel has been relatively limited, it has attracted more than 500 subscribers, providing an indication of interest in the service. Like many established cybercriminal services, Xilo appears prepared for domain disruptions by maintaining alternative access points and communicating them through Telegram, adopting the kind of resilience and service-continuity practices more commonly associated with legitimate online services.

Xilo accepts several cryptocurrencies, including Bitcoin, Litecoin, Monero, Ether, and Tether (USDT). Support for USDT is relatively uncommon among underground marketplaces and may reflect the marketplace's focus on US-based identity data. The minimum deposit is just $1, lowering the barrier to entry for new users, while bonuses are offered for deposits exceeding $100 to encourage larger account balances.

Beyond its own infrastructure, Xilo actively advertises on well-known cybercrime forums, including XSS, as well as carding communities such as WWH-Club and Altenens (Figure 4). This marketing strategy is common among underground marketplaces seeking to expand their customer base. More notably, Xilo's presence on carding-focused forums highlights the close relationship between stolen payment data and identity information, illustrating how different segments of the cybercrime ecosystem increasingly overlap and complement one another.

![Xilo-advertisement_-Altenens.png](https://www.rapid7.com/cdn/images/blt7b8f2bd1df6fa1de/6a9042b20a3bbe812a59e279/Xilo-advertisement_-Altenens.png) _Figure 4 – Xilo advertisement on Altenens_

### Bankomat

Active since at least March 2022, Bankomat is one of the more established marketplaces operating in the underground identity theft ecosystem. The platform is accessible as a Tor hidden service while maintaining multiple clear web domains to improve availability. Its emergence coincided with the shutdown of several prominent carding and PII marketplaces, including Joker's Stash and SSNDOB Marketplace, suggesting that Bankomat sought to capitalize on the resulting gap by combining identity data sales with traditional carding services.

The marketplace prominently lists its active domains and encourages users to save its onion address, describing it as the most reliable way to access the service. This reflects an awareness of the operational challenges faced by long-running underground marketplaces, particularly the risk of domain seizures and takedowns. By maintaining multiple access points and actively directing users toward its Tor service, Bankomat demonstrates the operational maturity needed to retain its customer base despite infrastructure disruptions.

Users can search for individuals by first and last name, combined with an additional identifier such as state, city, ZIP code, or date of birth (Figure 5). The search functionality is free, allowing users to identify potential victims before deciding whether to purchase a record. Search results display the victim's full name, date of birth, and physical addresses, while the SSN is revealed only after purchase at a fixed cost of $4 per record. Unlike Xilo, however, Bankomat does not offer additional identity enrichment services or the ability to purchase supplementary PII directly through the platform.

![Bankomat-search-bar.png](https://www.rapid7.com/cdn/images/blt906858a51dc885cc/6a9043058433ee1e2e840353/Bankomat-search-bar.png) _Figure 5 – Bankomat search bar_

⠀

Beyond SSN records, Bankomat also functions as a traditional carding marketplace by offering stolen payment card details for sale, obtained through third-party sellers. The platform supports card validation services, including Viper and 4chk, allowing buyers to verify whether stolen payment cards remain active before using or reselling them. Similar functionality is offered by established carding marketplaces, such as Findsome and UltimateShop.

This combination of identity records, payment card data, and validation tools positions Bankomat as a one-stop marketplace for financially motivated threat actors. Rather than sourcing stolen identities and payment data from separate platforms, buyers can acquire multiple data types associated with the same victim through a single service. While SSN records cost $4, stolen payment card details are typically advertised for approximately $10, suggesting that Bankomat places greater commercial emphasis on its carding business, likely reflecting both higher profit margins and sustained demand within the underground economy (Figure 6).

![bankomat-credit-card-listings.png](https://www.rapid7.com/cdn/images/bltb5ce8efb1b13a40a/6a904338d62e1184b0e364ce/bankomat-credit-card-listings.png) _Figure 7 – PeopleFinder SSN listings_

⠀

Bankomat currently accepts payments exclusively in Bitcoin, in contrast to newer marketplaces that increasingly support a wider range of cryptocurrencies to appeal to a broader customer base.

### PeopleFinder

Active since at least February 2023, PeopleFinder is a successor to the SSNDOB Marketplace, whose primary domains were seized by law enforcement in June 2022. Following that takedown, the service re-emerged through a network of lookup mirrors using clear-web-sounding domain names such as “PeopleFinder.” The connection is also visible in the source code, where the front-end login page retains the original “ssndob” title text and logo. Through this infrastructure, the platform provides access to the same legacy database of more than 24 million compromised U.S. PII records.

To maintain a steady customer stream, PeopleFinder actively advertises its database on high-profile cybercrime and carding forums like WWH-Club and Exploit. This deliberate marketing keeps the service highly visible to financially motivated threat actors seeking verification tools for downstream fraud.

The layout itself is highly streamlined, featuring a basic search bar that closely mirrors Bankomat's interface. Users can search the platform's database by name, date of birth, or physical address completely free of charge. The initial search output displays the victim's full name, date of birth, and associated physical addresses, allowing a threat actor to confirm they have targeted the correct corporate executive before paying for the record (Figure 7).

![peoplefinder-ssn-listings.png](https://www.rapid7.com/cdn/images/bltc6ad5198e8f326a6/6a9043f060f7958996d75ece/peoplefinder-ssn-listings.png) _Figure 7 – PeopleFinder SSN listings_

To reveal the hidden SSN, users must pay a fixed cost of $1.50 per lookup, putting its pricing structure right between Xilo and Bankomat. This strict, hyper-commoditized focus solely on core SSN details directly mirrors the operational blueprint of the original SSNDOB model. Rather than expanding into supplementary data types like phone numbers or credit cards, the operators chose to preserve their highly efficient, legacy pay-per-lookup infrastructure. The platform relies exclusively on Bitcoin transactions.

## What Rapid7 telemetry reveals about the executive threat landscape

By monitoring dark web SSN marketplaces, Rapid7 actively alerts clients when leaked records of their executives or designated employees are discovered.

Since the beginning of 2026, our telemetry has identified 476 instances of compromised SSN records, representing 395 unique individuals, as several monitored personnel were affected by multiple exposures. Within this sample, most of the leaked SSNs were recorded in Xilo (40.8%), followed by Bankom (21.8%) and PeopleFinder (18.9%) (Figure 8).

![leaked-ssns-by-marketplace.png](https://www.rapid7.com/cdn/images/blt9c8deb9f4e41851d/6a904441d4aaa70e0b7f0e80/leaked-ssns-by-marketplace.png) _Figure 8 – The sample distribution of leaked SSNs by marketplace_

⠀

Given that SSNs are issued within the United States, the overwhelming majority of compromised records in our dataset, 95.6%, were linked to organizations headquartered in the U.S., with others located in Spain, Canada, and Japan, trailing significantly behind (Figure 9).

![leaked-ssns-by-country.png](https://www.rapid7.com/cdn/images/blt7c4c10ea9f65329d/6a9044770a3bbeb4e859e287/leaked-ssns-by-country.png) _Figure 9 – The sample distribution of leaked SSNs by country_

⠀

Financials represented the largest sector in our sample, accounting for more than a quarter of organizations whose monitored executives appeared in leaked SSN records, followed by Industrials at 17% (Figure 10). One possible reason for the concentration in Financials is the volume and sensitivity of customer and employee data these organizations hold, including PII and tax-related information, which can make exposed identities particularly valuable to threat actors. Industrials may also present attractive targets because of their interconnected supply chains, where compromised identities can potentially support broader fraud, impersonation, or access attempts across partner ecosystems.

![leaked-ssns-by-sector.png](https://www.rapid7.com/cdn/images/blt3858d7be6ddf8240/6a9044cac8ced9499c056239/leaked-ssns-by-sector.png) _Figure 10 – The sample distribution of leaked SSNs by sector_

⠀

A closer analysis of the roles of targeted personnel reveals that C-suite executives (such as Chief Executive Officers and Chief Financial Officers) make up the largest portion at 44.6%. Presidential positions represent the second-largest segment at 28.6%, while functional management and administrative roles account for 13.9% of the compromised profiles.

These findings may reflect a natural monitoring bias, since organizations are more likely to prioritize senior personnel whose compromise poses a greater security risk. Even with that caveat, the concentration among senior leadership reinforces why executive identity exposure deserves specific attention.

Compromised executive PII can support targeted phishing, impersonation, and other social engineering campaigns against both the individual and the organization they represent.

**Role Category**| **Key Roles Included**| **Unique Target Count**| **% of Unique Targets**  
---|---|---|---  
Executive Leadership (C-Suite)| CEO, CFO, COO, CTO, CIO, Chief Revenue/Human Resources Officers| 176| 44.6%  
Presidents & Vice Presidents| President, SVP, EVP, Regional Vice Presidents| 113| 28.6%  
Functional Management & Admin| Directors, Heads of Departments, Managers, Executive Assistants| 55| 13.9%  
Legal, Partner & Advisory| Managing Members, Partners, Corporate/Securities Attorneys| 33| 8.4%  
Board, Governance & Officials| Board Trustees, Directors of the Board, State Senators, Vice Chairs| 18| 4.6%  
Total Unique Individuals|   
| 395| 100.0%  
  
## From detection to action: Responding to exposed executive PII

Because SSNs cannot simply be reset after exposure, organizations need a way to identify compromised executive PII early and determine what action can reduce the resulting risk.

These alerts are triggered using customer-defined assets, specifically the names of designated VIPs. When a potential match is flagged, Rapid7 analysts conduct preliminary OSINT verification, checking biographical details such as the VIP's date of birth and primary locations, to confirm the listing's accuracy before issuing an alert to the customer.

Once alerted, customers can choose to purchase the exposed SSN record directly through the "Ask-an-Analyst" service using their allocated dark web purchase credits (Figure 11). This capability allows security teams to inspect the full record, verify whether the exposed SSN is genuine, and determine whether additional protective measures are necessary for the affected executive. Furthermore, on platforms like Xilo, purchasing the listing removes the record from the marketplace entirely, actively taking it off the shelf before other threat actors can acquire it.

![Rapid7-Platform-alert-leaked-executive-details.png](https://www.rapid7.com/cdn/images/blt1fa48534d153c2ed/6a90458f0897905f31efa75d/Rapid7-Platform-alert-leaked-executive-details.png) _Figure 11 – Rapid7 Platform alert about the leaked details of a company executive_

## Conclusion and strategic defense actions

The illicit marketplaces examined by Rapid7 show how cheaply and efficiently stolen identity data can now be searched, purchased, and enriched. For executives and other high-profile employees, an exposed SSN can remain useful to threat actors long after the original compromise and may support identity fraud, social engineering, executive impersonation, or business email compromise. Because that information cannot simply be reset, organizations should treat executive identity exposure as an ongoing security risk.

To reduce that risk, executive protection and security teams should consider the following actions:

  * Monitor executive exposure on the dark web: Use digital risk protection capabilities configured with executive names, known locations, titles, and other relevant identifiers to detect compromised PII across illicit marketplaces and underground channels.

  * Use removal or takedown options where available: Where supported, work with security providers to acquire or remove exposed identity records before they are purchased and reused by other threat actors.

  * Reduce executives’ public digital footprint: Review public records, data-broker listings, corporate biographies, and social media profiles to limit unnecessary exposure of information such as dates of birth, home addresses, and phone numbers that can be used to enrich stolen records.

  * Require out-of-band verification for sensitive requests: Introduce mandatory secondary confirmation for financial transactions, access requests, or administrative changes involving executive accounts to reduce the risk of successful impersonation.

  * Provide targeted phishing and impersonation training: Give C-suite members, board members, and executive assistants focused guidance on how attackers can combine leaked PII with social engineering to make phishing and impersonation attempts more convincing.




The persistence of SSNs means the risk does not end when the original breach is discovered. Ongoing monitoring, rapid validation, and stronger verification controls can help organizations identify exposure earlier, reduce the value of stolen identity data, and make it harder for threat actors to turn compromised executive information into a wider attack against the business.

## Article tags

  * [Dark Web](/blog/tag/dark-web/)
  * [Phishing](/blog/tag/phishing/)