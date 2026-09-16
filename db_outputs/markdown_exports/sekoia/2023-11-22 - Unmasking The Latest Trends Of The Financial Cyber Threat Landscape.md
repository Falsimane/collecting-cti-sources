# Unmasking The Latest Trends Of The Financial Cyber Threat Landscape

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/unmasking-the-latest-trends-of-the-financial-cyber-threat-landscape
- **Date :** 2023-11-22

---

This report aims at depicting recent trends in cyber threats impacting the financial sector worldwide. It focuses on principal tactics, techniques and procedures used by lucrative and state-sponsored intrusion sets by providing an analysis of evolutions observed in campaigns against financial organisations.

Cyber threats represent a systemic risk to the financial system, primarily due to the interconnection of financial institutions and to the potential financial stability and integrity implications of a cyberattack. Moreover, financial organisations face significant financial, regulatory and reputational consequences associated with the insufficient protection of consumers’ data.

## Executive summary

  * The financial sector represents a **prime target for lucrative intrusion sets**. The critical nature of most financial services and operations, the increasing digitalisation and the sector's reliance on critical third-party service providers highly likely make the financial organisations high-value targets for fraud, phishing, ransomware and extortion campaigns.
  * The financial sector is **the most impacted by phishing** campaigns worldwide, highly likely due to the **massive adoption of the Phishing-as-a-Service (PhaaS) model**.
  * An **increasing number of QR code phishing campaigns** associated with PhaaS such as **Dadsec OTT** , **Tycoon** and **W3LL Panel** targeted financial organisations in 2023.
  * **Business Email Compromise** (BEC) campaigns leverage**novel TTPs** such as third party targeting and indirect proxy use for a **greater impact** on financial organisations.
  * Major **Brazilian banking malware** expand beyond Latin American borders and persist in targeting banks in **Europe**.
  * **Android spyware** expand beyond traditional targeting and are**increasingly used for bank fraud** in 2023.
  * The financial sector is **increasingly impacted by open-source software supply chain** campaigns, while **targeted** attacks towards the **banking** vertical emerged in 2023.
  * The financial sector is one of the top five sectors most impacted by **ransomware** in 2023, reporting **impacts** such as **unavailable systems** , **disrupted operations** , **reputational damage** and **financial loss**.
  * The digitalisation of the financial sector resulted in new banking services that can be used as a vector for malicious initial access. It was the case with financial **aggregators**.
  * The financial sector is the **fourth most targeted sector** by North Korea intrusion sets, which especially conduct operations against **decentralised finance** (DeFI) **services** , such as bridges, to make profit.
  * State-sponsored intrusion sets conduct **lucrative operations** against financial entities **to masquerade cyberespionage** campaigns.



## Lucrative cybercrime threats

The financial sector is a prime target for financially-motivated threat groups. This is highly likely due to the rapid transformation of financial services (accelerated by the COVID-19 pandemic), to the criticality of most financial services and operations, to the highly interconnected financial ecosystem, and to its dependency on critical third party service providers. 

In recent years, financial organisations faced an increasingly specialised and sophisticated, mostly opportunistic, threat landscape. Cybercrime-related threats impacting the financial sector are highly lucrative and include, but are not limited to, phishing campaigns, infostealer and ransomware infections, supply chain attacks, data breach incidents, crypto-related attacks and DDoS campaigns.

### Evolving phishing techniques

The phishing threat is a prime initial access vector across industries worldwide and was identified as the top digital crime over 2022 as per number of victims, based on [FBI data](https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf).

The financial sector is reported to be the most impacted by phishing campaigns. According to the [Anti-Phishing Working Group](https://docs.apwg.org/reports/apwg_trends_report_q3_2022.pdf) (APWG), 27.7% of all phishing attacks conducted in 2022 were directed specifically at the financial sector. Moreover, financial services is the most impersonated vertical, representing 34% of all phishing pages [analysed](https://www.vadesecure.com/en/blog/phishers-favorites-2022-year-in-review-google-phishing-sharply-increases) by Vade in 2022. Prominent financial entities such as PayPal, MTB, Crédit Agricole, and La Banque Postale are among the most frequently impersonated brands across all sectors worldwide.

The wide adoption of the Phishing-as-a-Service (Phaas) model and the continuous evolution of Business Email Compromise (BEC) and phishing delivery techniques highly likely contributed to the proliferation of phishing campaigns against the financial sector over the past years.

#### Phishing-as-a-Service is a fast-growing phenomenon 

Based on our observations, threat actors continued to massively adopt the Phishing-as-a-Service (PhaaS) model throughout 2023. The PhaaS toolsets offer malicious actors the advantages of customised phishing templates and accurate targeting. This not only increases the efficacy of campaigns, but also facilitates less advanced threat actors in conducting large-scale operations.

During our threat monitoring and tracking routine, we continuously detect PhaaS kits that sell prebuilt phishing pages impersonating financial organisations, mostly designed to collect Microsoft 365 login credentials. Stolen credentials are typically leveraged to access a user’s email account, cloud resources, contact information, _etc_.

One such recent example is NakedPages PhaaS, which currently provides phishing pages impersonating financial organisations, such as the online accounting software Quickbooks. Another example includes BulletProftLink, a long-running, large-scale PhaaS service selling decentralised phishing and BEC sites on a subscription model. Notably, we observed this service targeting numerous major banks. Of note, eight people linked to BulletProftLink were [arrested](https://intel471.com/blog/malaysian-police-disrupt-the-phisherman) in early November 2023 as a result of an international operation. We assess it will highly likely lead to (full or partial) disruption of BulletProftLink infrastructure and to its users moving to other well-established or emerging PhaaS services such as NakedPages or Dadsec.

Based on our observations, the most actively used PhaaS toolsets over the past year include EvilProxy, Gophish, NakedPages, Dadsec, Caffeine, NakedPages and Greatness. We observed that most of them include financially themed phishing pages to their lures.

#### QR code phishing campaigns target financial institutions

During the second half of 2023, Sekoia.io analysts observed an increasing number of QR code phishing campaigns associated with emergent PhaaS platforms.

In recent months, we analysed several large-scale QR code phishing (aka “quishing”) campaigns associated with the Dadsec OTT PhaaS platform. Active since mid-2023, it was one of the most frequently observed kits in Q3 of 2023. We observe that financial organisations such as banks are regularly impersonated via phishing pages sold on this platform.

![Figure 1. Phishing pages and email templates \("letters"\) impersonating banks sold on the Xleettool marketplace linked to the Dadsec developer ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fb16f788fda8e5101a_6a92a35a32517fc4026027ab_6a2a7c50b7830b74300a4651.webp)

Figure 1. Phishing pages and email templates ("letters") impersonating banks sold on the Xleettool marketplace linked to the Dadsec developer 

In October 2023, Sekoia.io unveiled a different QR code phishing campaign targeting investment organisations, among others. This campaign leveraged an emerging PhaaS kit known as Tycoon. The attackers leveraged PDF and XLSX email attachments containing a QR code that redirected victims to a phishing link, to collect Microsoft 365 session cookies.

More recently, we identified a QR code phishing campaign targeting a U.S.-based financial organisation. The phishing pages displayed a copy of the Microsoft 365 authentication page and aimed at stealing the victim's user credentials. We associated this campaign with the W3LL Panel phishing kit, sold on illicit Telegram communities as a PhaaS platform. As [reported](https://go.group-ib.com/hubfs/report/group-ib-w3ll-done-threat-report-2023.pdf) by Group-IB in September 2023, the financial services sector is the third most impacted in campaigns leveraging W3LL tools.

Sekoia.io assess QR code phishing will be increasingly leveraged by threat actors, notably due to their effectiveness in evading detection and circumventing email protection solutions. Compromised credentials obtained in successful QR code phishing campaigns are most likely leveraged by the intrusion sets to conduct further compromises such as internet scams, financial fraud or Business Email Compromise (BEC) campaigns. 

#### BEC campaigns expand their attack targets and leverage novel TTPs

Sekoia.io actively tracks Business Email Compromise (BEC) campaigns across multiple verticals, including the financial sector. BEC is a specific type of phishing attack (spear phishing) that leverages social engineering methods for impersonation. It typically consists of enticing victims into sharing financial information or engaging in actions such as inadvertently transferring funds to accounts controlled by money mules, facilitating fraudulent money transfers by malicious actors. 

Over the past years, BEC posed an increasing threat to both large enterprises and small and medium-sized businesses (SMBs). It was [identified](https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf) by the FBI as the second most profitable digital crime type in 2022 (behind investment scams). As of 2023, it continues to be a preferred method for attackers to achieve financial gains - BEC attacks increased by 55% between January and June 2023 according to open source [reporting](https://abnormalsecurity.com/blog/bec-vec-attacks-2023).

In 2023, BEC-related threat actors are [reported](https://www.tripwire.com/state-of-security/business-email-compromise-statistics) to expand their target list to include third parties (notably vendors), besides traditional impersonation of executives in top positions within a company.

One such campaign impacting the financial sector was recently [uncovered](https://www.microsoft.com/en-us/security/blog/2023/06/08/detecting-and-mitigating-a-multi-stage-aitm-phishing-and-bec-campaign/) by the Microsoft Defender team. In June 2023, the source reported on a sophisticated, multi-stage AiTM (adversary-in-the-middle) phishing and BEC attack specifically targeting banking and financial services organisations that originated from a compromised trusted vendor. To launch a massive campaign involving 16,000 emails, the attackers used an AiTM phishing kit developed, maintained, and operated by a previously unknown intrusion set that Microsoft tracks as Storm-1167.

This campaign is notable for the use of indirect proxy rather than the typical reverse proxy techniques. The resources on the page are loaded from an attacker-controlled server, which provides to attackers a better control and more flexibility in tailoring the phishing pages to their targets. Moreover, this is indicative of ever-evolving and increasingly complex phishing ang BEC threats, adopting novel TTPs to circumvent traditional security measures.

### Lucrative supply chain attacks

#### The (open-source) software supply chain is at risk

Over the past few years, open source reports [revealed ](https://www.sonatype.com/resources/state-of-the-software-supply-chain-2022/introduction)an exponential growth of software supply chain attacks of 742% per year between 2019 and 2022. Google also [noted ](https://blog.google/technology/safety-security/why-google-supports-the-us-securing-open-source-software-act/)a similar trend in late 2022. Moreover, in 2023 Sonatype [reported ](https://www.sonatype.com/state-of-the-software-supply-chain/introduction)twice as many software supply chain attacks as the cumulative numbers in previous years. 

Of particular concern are open-source software supply chain attacks, as a large number of software projects implemented by organisations rely on multiple open-source libraries and components. Organisations in the financial sector particularly report an extensive use of open source tooling and technology. The FINOS’ (the Fintech Open Source Foundation) “[2023 State of open source in financial services](https://www.finos.org/state-of-open-source-in-financial-services-2023)”, based on a worldwide survey conducted from June to August 2023, states that 94% of organisations in the financial sector worldwide use open source components in their digital products or services. 

Therefore, compromising open-source components can potentially affect a large number of financial systems and organisations. This related to the actors within the financial industry considering that [security concerns are the biggest obstacle to open source usage](https://www.finos.org/state-of-open-source-in-financial-services-2023).

Notable supply chain campaigns leveraging open-source tools include the exploitation of Log4Shell (CVE-2021-44228), a critical vulnerability in the Java logging component Log4j, integrated in numerous applications across most sectors. The vulnerability was exploited as soon as it was disclosed on 9 December 2021.

From our observations throughout 2023, most lucrative supply chain attacks targeting open-source software were opportunistic and impacted organisations in nearly all sectors.

#### Supply chain attacks specifically target the banking sector

In the first half of 2023, there were [reported ](https://checkmarx.com/blog/first-known-targeted-oss-supply-chain-attacks-against-the-banking-sector/)several software supply chain attacks specifically targeting the banking sector. Notably, Checkmarx identified two unrelated campaigns - conducted in February and April 2023 - that leveraged the npm open-source software platform to target specific components of the victims' web assets. The documented attacks were conducted by two distinct, unidentified, advanced intrusion sets that are highly likely motivated by financial gain.

As per Checkmarx researchers, it was the first time such incidents occurred, considering the sector-specific targeting.

In 2023, software supply chain [remains ](https://www.sonatype.com/state-of-the-software-supply-chain/Introduction)one of the fastest growing vectors for adversaries to execute malicious code. Given the wide use of open source software within the financial sector, the increasing number of open source projects published every year (a [29% growth](https://www.sonatype.com/state-of-the-software-supply-chain/Introduction) between 2022 and 2023) and the ever increasing threat of tailor-made malicious packages (which [tripled ](https://www.sonatype.com/state-of-the-software-supply-chain/Introduction)in 2023), it is highly likely that advanced threat actors will persist in explicitly targeting the banking sector’s software supply chain. Such campaigns aiming at exploiting externally facing vulnerable software can typically lead to mass data exfiltration, ransomware and/or extortion campaigns, _etc_.

### Malware targeting financial assets

Malware designed to target financial assets mainly aim at retrieving financial and cryptocurrency data from banks and other financial institutions, commonly impacting their customers. Such malware include desktop and mobile banking trojans, malware for ATMs and payment terminals, and others. Banking trojans are one of the most used malware against the financial sector. Trojans typically have functionalities of capturing and stealing data or enabling remote control of a system.

Of particular concern are mobile threats, as the number of detected mobile banking trojans [doubled ](https://securelist.com/mobile-threat-report-2022/108844/)in 2022 compared to the previous year, and [continues ](https://securelist.com/it-threat-evolution-q2-2023-mobile-statistics/110427/)to grow through 2023. This is highly likely due to the increasing use of mobile devices for financial services (mobile finance applications, mobile payments, _etc_).

#### Top-tier Brazilian banking malware expands to banks in Europe

Banking trojans are a malware family reported as traditionally [originating ](https://www.virusbulletin.com/uploads/pdf/conference/vb2023/papers/Looking-into-TUTs-tomb-the-universe-of-threats-in-LATAM.pdf)from and targeting Latin American countries. Most banking malware particularly target users and organisations in Brazil, and increasingly target victims in Mexico, highly likely due to the broad [adoption](https://www.proofpoint.com/us/blog/threat-insight/copacabana-barcelona-cross-continental-threat-brazilian-banking-malware) of online banking offers in these countries.

While there have been [indications ](https://vblocalhost.com/uploads/VB2020-Soucek-Jirkal.pdf)that these malware expand beyond Latin American borders since at least 2020, this trend accelerated in 2023. For example, a new version of Grandoreiro malware was recently [observed ](https://www.proofpoint.com/us/blog/threat-insight/copacabana-barcelona-cross-continental-threat-brazilian-banking-malware)implementing the same infrastructure and payload while targeting Mexico and Spain simultaneously. Of note, previously, threat clusters leveraging Grandoreiro were previously only seen in campaigns targeting bank customers in Brazil and Mexico at the same time. Proofpoint assess intrusion sets that have traditionally targeted Portuguese and Spanish speakers in Brazil, Mexico, and other parts of the Americas, and that currently target Spain, have been unusual in frequency and volume in 2023, compared to previous activity.

#### Spyware are increasingly used for bank fraud

Spyware is a category of malware that includes keyloggers, password stealers, banking trojans, infostealers, _etc_. While spyware are typically leveraged to collect information about the users of an infected device, in both lucrative and espionage-driven campaigns, these malware are also increasingly used for bank fraud since early 2023.

One such example is SpyNote - an Android spyware capable of monitoring, managing, and modifying resources on a targeted device, abusing the Accessibility services permissions granted by the victim during the installation.

SpyNote’s most recent variant (“SpyNote C”) [targets ](https://www.threatfabric.com/blogs/spynote-rat-targeting-financial-institutions)banking applications starting from October 2022, following the release of its source code in open source. This development was quite uncommon for an Android spyware at that time, indicating a possible gradual blurring between spyware and banking malware functionalities. 

This trend was confirmed over 2023 along with a [campaign ](https://www.cleafy.com/cleafy-labs/spynote-continues-to-attack-financial-institutions)leveraging SpyNote malware to perform banking fraud. It was “one of the most aggressive SpyNote campaigns in recent times” as per Cleafy. The attackers targeted customers of different banks across Europe to perform Account Takeover attacks (ATO) and on-device fraud (ODF). Fraud operations were executed via Teamviewer directly on the victim’s device, by leveraging social engineering techniques. 

Of note, Revive RAT was also reported in mid-2022 as being developed based on an open source spyware called Teardroid, and then customised so it could be used in fraud operations against a top-tier Spanish bank.

Sekoia.io assess lucrative intrusion sets will increasingly use spywaresuch as SpyNote for bank fraud, mainly due to the spyware’s extended functionalities such as the keylogging, SMS collection and 2FA bypass.

### Ransomware and extortion threat

For several years now, the ransomware threat landscape has experienced a significant growth in the number of claimed attacks, active ransomware variants, emerging ransomware actors and illicit transactions. This is particularly applicable to ransomware groups targeting businesses rather than individuals.

![Evolution of publicly disclosed ransomware attacks since early 2021 \(Sources: Sekoia.io, Reliaquest\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fb16f788fda8e51026_6a92a3544c776939a1e0bd67_6a2a7c50b7830b74300a463c.webp)

Figure 2. Evolution of publicly disclosed ransomware attacks since early 2021 (Sources: Sekoia.io, Reliaquest) 

#### The ransomware threat proliferates and increasingly impacts the financial sector

Financial entities are constantly impacted by ransomware campaigns. While ransomware actors are opportunistic in their targeting across all sectors, the banking vertical was the [most impacted](https://www.trendmicro.com/vinfo/in/security/news/ransomware-by-the-numbers/lockbit-blackcat-and-clop-prevail-as-top-raas-groups-for-1h-2023) by ransomware in the first half of 2023. More recently, the financial sector was [identified ](https://www.reliaquest.com/wp-content/uploads/2023/10/Q323RansomwareThreatReport.pdf)as one of the top five sectors [most impacted ](https://www.guidepointsecurity.com/resources/grit-ransomware-report-2023-q3/)by ransomware during the third quarter of 2023.

Comparitech [observed ](https://www.comparitech.com/blog/vpn-privacy/ransomware-finance-sector/)225 financial organisations worldwide were directly impacted by ransomware attacks between 2018 and June 2023, with ransom demands varying from $180,000 to $40 million. The source reports an overall cost of downtime of $32.3 billion. This only represents the volume of the attacks known in open source, thus the real number of ransomware victims should be estimated significantly higher.

![Ransomware attacks on the finance sector from 2018 to June 2023. Source: Comparitech. Source: Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fb16f788fda8e5101d_6a92a357e36224e46e90e9cb_6a2a7c50b7830b74300a4648.webp)

Figure 3. Ransomware attacks on the finance sector from 2018 to June 2023. Source: Comparitech 

The reason the financial sector is an attractive target for major ransomware groups could be the large number of entities it involves (including large corporations), the large attack surface, the criticality of services that organisations provide, its high reliance on supply chain operations, and the considerable volume of financial transactions it handles. All this highly likely translates into higher ransom demands and extortion payments.

Most of the prominent ransomware groups impacting the financial sector in 2023 typically leverage the double-extortion technique, meaning that they exfiltrate data before encryption. Such examples are LockBit (that dominated the financial ransomware landscape over 2023), BlackCat, 8Base, Play and Akira, among others.

One recent, prominent ransomware campaign impacted the U.S. branch of the Industrial & Commercial Bank of China Ltd. - one of the largest banks in the world. The LockBit Ransomware-as-a-Service (RaaS) group, which is the most prolific ransomware group as of late 2023, claimed the attack shortly after it was first reported in open sources. The attack was reported to have disrupted trades in the U.S. Treasury market as of 10 November 2023, the victim switching to manual processes to perform trades. 

Earlier this year, a global financial software provider - Ion Group - was also victim of a notable ransomware campaign claimed by the LockBit group. The attack led to one week of only partially operational systems, it affected at least 42 of Ion’s clients, including some of the world's biggest banks, brokerages and hedge funds. Thus, it forced several European and U.S. banks to revert to manual processes.

Besides the unavailable systems and disrupted operations, there were also reported impacts such as data exfiltration, social impact (data leakage concerning the general public’s IDs, social security numbers, addresses _etc._) and reputational impacts. Of note, the financial vertical is [one of the most concerned](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2022) by reputational impacts following ransomware attacks. Also, the financial sector had some of the [highest impacts](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2022) related to economic losses in 2022. According to a [Sophos survey](https://www.sophos.com/en-us/content/state-of-ransomware), 46% of financial services entities reported losses of “a lot of business/revenue” in 2022.

#### Extortion groups increasingly leverage data exfiltration technique

Over the last year, known ransomware groups impacting the financial sector, such as BianLian, were [reported ](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-136a)shifting to the exfiltration-based extortion without encrypting the victim's system and data.

TA505 is another major actor of the ransomware ecosystem that turned to the extortion model based on data exfiltration only. This was notably the case with the exploitation of the vulnerability identified as CVE-2023-34362 in internet-facing MOVEit Transfer installations. 

This is indicative of the growing interest of extortion groups in collecting victim’s sensitive data, likely to avoid encryption problems at scale during mass compromise campaigns. Moreover, this is likely in line with the fact that financial entities typically operate on highly regulated markets, leading to wider implications on regulatory compliance standards in case of public release of exfiltrated data - which might be an additional argument to pressure victims.

## State-sponsored threats

The financial sector also represents an enticing target for state-sponsored intrusion sets. Their campaigns typically target financial entities to overcome international economic sanctions, to achieve political goals, to perform disruption, as well as to collect strategic information for future attacks. 

This is partly due to the fact that financial entities host (highly) sensitive information about clients, organisations, States and their economy. They are also responsible for producing, storing, and transferring money at a large scale. Therefore, the sector has a strategic dimension that makes it a potential target for state-sponsored threat groups.

While the state-sponsored threats are less visible compared to the lucrative ones, monitoring them is essential, as their attacks can generate critical consequences. Therefore, this report focuses on emerging trends in state-sponsored activities that we observed along our day-to-day monitoring of cyber threats affecting the financial sector.

### Supply chain attacks targeting financial aggregators

Financial aggregators are evolving due to the multiplication of financial assets consumed by users. Highly interconnected and sharing information with various actors of the financial sector, they represent a potential vector of vulnerability for supply chain attacks conducted by state-sponsored intrusion sets.

#### Financial aggregator's security is at risk

As the financial sector evolves towards a growing digitalisation, new actors are emerging to offer cutting-edge services. Financial aggregators are part of these newcomers. They provide a unique platform that gathers information from different financial services and enables to manage all of them. This proves particularly helpful for users who tend to diversify their consumption of financial assets, expanding beyond traditional investments in fiat currencies to include the buying and exchanging of diverse cryptocurrencies.

![Orion Aggregator](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fb16f788fda8e51029_6a92a3592e47a1e9fe0e087c_6a2a7c50b7830b74300a464e.webp)

Figure 4. [Orion Aggregator](https://blog.orionprotocol.io/)

Financial aggregators are fintech companies evolving in a very competitive and dynamic market. They developed quickly to respond to the digitalisation of the financial sector and to offer innovative services at the best price. Nevertheless, they are not submitted to the same level of regulation as traditional banking entities and are supported by technologies with potential vulnerabilities. According to the [International Monetary Fund](https://www.elibrary.imf.org/view/journals/063/2023/004/article-A001-en.xml), “the provision of cloud computing [to fintechs] has the potential to shift risks from regulated financial institutions to entities that are not as well regulated, such as BigTechs” or “APIs with poor security architecture could lead to leaks of potentially sensitive data”.

Below are listed various potential vulnerabilities that could be exploited to target financial aggregators:

  * Vulnerabilities in API and process of data transmission
  * Vulnerabilities in the software used by aggregators
  * Risks associated with third-party dependencies
  * Injection attacks for data interception
  * Vulnerabilities impacting cloud services



#### Recent attacks

Such attacks were already observed in February 2023 with the compromise of [Dexible](https://blog.solidityscan.com/dexible-hack-analysis-never-blindly-trust-smart-contracts-c2aee7943c1a), a decentralised exchange aggregator. Attackers abused the selfSwap function that authorises the app to move the tokens of users independently. This function enables a user to provide the address of a router and call data associated with to swap tokens. Nevertheless, the function lacks a list of pre approved routers in the code. Therefore, attackers oriented the tokens of users towards their own smart contract. Then, tokens were withdrawn through Tornado Cash into unknown BNB wallets.

While this attack was not attributed in open sources, it highlights how state-sponsored intrusion sets can rely on aggregators to affect the financial sector, taking advantage of technical vulnerabilities brought by less regulated actors. Indeed, Lazarus, a North Korea-nexus intrusion set, was identified exploiting the [JumpCloud](https://jumpcloud.com/blog/security-update-incident-details) vulnerability (CVE-2022-0543) to target cryptocurrency users in a supply chain attack in June 2023. It resulted in the force-rotation of all API keys to protect customers.

#### Why is it critical?

Since the SolarWinds attack in 2020, state-sponsored intrusion sets increasingly conduct supply chain attacks to compromise strategic victims, as demonstrated in the following graph.

![upply Chain Attacks over the past year \(December 2022 - November 2023\). Source: Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fb16f788fda8e51020_6a92a3564c776939a1e0be0d_6a2a7c50b7830b74300a4645.webp)

Figure 5. Supply Chain Attacks over the past year (December 2022 - November 2023) Source: Sekoia TDR Team

Consequently, it is important to anticipate new potential vectors for supply chain attacks targeting the financial sector to prevent operations against financial institutions that rely on third parties. 

Indeed, financial aggregators share sensitive data with financial entities, which can be used to steal the credentials of customers or to gain malicious access to API. According to [Akamai Security Intelligence](https://www.akamai.com/blog/security/attack-trends-in-financial-services#:~:text=Executive%20summary,as%20pathways%20for%20initial%20intrusion), “web application and API attacks in the financial services industry grew by 65% when comparing Q2 2022 with Q2 2023, accounting for 9 billion attacks in 18 months”. These techniques are mostly used by cybercriminals, but could also be exploited by state-sponsored intrusion sets to conduct supply chain operations.

### State-sponsored intrusion sets increasingly target Decentralised Finance (DeFi) platforms

In 2023, Sekoia.io observed a new trend in cyber threats impacting DeFi, especially targeting blockchain bridge services. Already well documented, including by Sekoia.io, most state-sponsored cyber operations impacting the financial sector are conducted by North Korea-associated groups. Blockchain bridges make no exception.

#### What are DeFi and bridges?

DeFi is based on blockchain technology and aims at providing open financial services without centralised traditional intermediaries. As blockchains became more popular, DeFi evolved to offer various peer-to-peer (P2P) services, which applied to cryptocurrency assets, and traditionally provided by the banking sector.

Cryptocurrencies are based on different blockchains, which are closed environments that cannot communicate with each other. To circumvent this problem, interoperability solutions have emerged, such as cross-chain bridges and atomic swaps. These solutions are based on smart contracts, which are parts of code that execute the transfer of tokens depending on the validation of specific conditions. 

In terms of volume of attacks against the financial sector,Democratic People’s Republic of Korea (DPRK) state-sponsored threats are the most prolific. According to TRM, North Korean campaigns conducted against the cryptocurrency industry in 2023 generated gains ten times larger than other actors, a focus Sekoia.io observes as well, based on our technical investigations, attack infrastructure tracking and open-source victimology gathering.

#### DPRK state-sponsored intrusion sets particularly target DeFi in 2023

During the last years, financially motivated cyberattacks attributed to DPRK-nexus intrusion sets continued to rise. Cyberattacks against cryptocurrencies were estimated at $0.5 billion in 2020, $3.3 billion in 2021 and $3.8 billion in 2022 according to [Chainanalysis](https://www.chainalysis.com/blog/2022-biggest-year-ever-for-crypto-hacking/). In 2023, finance was the fourth most targeted sector by DPRK operators. 

Over the past year, such attacks followed a trend already observed by Sekoia.io in 2022, among other cyber security vendors, which is the targeting of DeFi platforms, services, and developers.

In November 2023, [Elastic Security](https://www.elastic.co/security-labs/elastic-catches-dprk-passing-out-kandykorn) documented the KandyKorn malware, which was used in an espionage campaign targeting blockchain engineers working for a cryptocurrency exchange platform. Attackers impersonated members of a blockchain engineers Discord community to convince victims to download a malicious zip file named “Cross-platform Bridges.zip”. The zip archive was disguised as an arbitrage bot designed to capitalise on variations in cryptocurrency rates across different platforms and used to deploy the new macOS malware KandyKorn. It has a full-custom range of functionalities for accessing and extracting data from the victim's computer.

Among major incidents affecting DeFi platforms in 2023 was the campaign against Atomic Wallet, which led to the heist of $35 million in [June](https://hub.elliptic.co/analysis/north-korea-s-lazarus-group-likely-responsible-for-35-million-atomic-crypto-theft/). Over the same period, the crypto payment services [Alphapo ](https://www.bleepingcomputer.com/news/security/lazarus-hackers-linked-to-60-million-alphapo-cryptocurrency-heist/)and [CoinPaid ](https://www.bleepingcomputer.com/news/security/coinspaid-blames-lazarus-hackers-for-theft-of-37-300-000-in-crypto/)were also targeted, leading respectively to the theft of $60 million and $37 million. The three campaigns were attributed to Lazarus in open sources, which is a cluster of activity attributed to the 3rd Department of the Reconnaissance General Bureau of North Korea and that encapsulates several intrusion sets. Sekoia.io analysts identified TEMP_Hermit, Andariel and Bluenoroff as sub-groups part of the Lazarus’ umbrella.

In these attacks, the initial access is typically gained using fake job offers to lure employees and steal account credentials from crypto firms. This technique was notably used in the DreamJob Operation that started in 2020 and that is still ongoing as of late 2023. To ensure stealthiness once the crypto asset has been stolen, operators usually relied on crypto-mixing services, such as Sinbad, [Tornado Cash](https://hub.elliptic.co/analysis/the-100-million-horizon-hack-following-the-trail-through-tornado-cash-to-north-korea/), and Blender. The last two were closed by US authorities.

Typosquatting of various financial entities, especially in DeFi, is also used to lure the victims and steal credentials. Sekoia.io analysts actively monitor the evolution of typosquatting campaigns of Bluenoroff, as well as Indicators of Compromission of other DPRK-nexus intrusion sets.

![Tracking of Bluenorof's typosquatting campaigns by TDR analysts. Source: Unmasking the latest trends of the Financial Cyber Threat Landscape.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fb16f788fda8e5102c_6a92a3584538ee1e1c2e6ee6_6a2a7c50b7830b74300a464b.webp)

Tracking of Bluenorof's typosquatting campaigns by TDR analysts. Source: Unmasking the latest trends of the Financial Cyber Threat Landscape.

[US authorities](https://www.dni.gov/files/CTIIC/documents/products/North-Korean-TTPs-for-Revenue-Generation.pdf) also warned about IT workers who applied for job offers in digital payment services and freelance work platforms to steal sensitive data. Acting as insiders, they support DPRK cyber operations.

#### A trend that aligns with traditional targets of DPRK threat actors

Bluenoroff and Andariel are known to be highly specialised in targeting the financial sector, especially cryptocurrency assets. Their campaigns aim at helping the regime bypass international economic sanctions and possibly directly financing the nuclear missiles program of Pyongyang, according to the [United Nations](https://www.reuters.com/world/asia-pacific/north-korea-developing-nuclear-weapons-evading-sanctions-2023-un-report-2023-08-10/).

In February 2016, Lazarus was designated as the perpetrator of the campaign against the Bank of Bangladesh. The attackers deployed malware to compromise the bank and to target SWIFT systems. Then, they initiated fraudulent fund transfer requests to the Federal Reserve Bank of New York and stole $81 million, which were laundered through Philippine casinos.

In March 2022, the attack of the [Ronin network bridge of Axie Infinity](https://www.bleepingcomputer.com/news/cryptocurrency/620-million-in-crypto-stolen-from-axie-infinitys-ronin-bridge/), which is a blockchain-based game, was attributed to Bluenoroff and Lazarus by the [FBI ](https://twitter.com/FBI/status/1514724462431817736)and considered as the largest crypto hack in history. It led to a heist estimated at $620 million. 

The range of DPRK-nexus intrusion sets conducting operations against financial entities also increased. In 2023, Reaper, which usually focuses on espionage and sabotage cyber operations, was identified broadening its scope of attack by targeting cryptocurrency consumers using a recent WinRAR vulnerability (CVE-2023-38832).

According to Microsoft’s 2023 Digital Defense Report, DPRK would dedicate one-half of its defence budget to cyber operations, which confirms the observed tendency of the escalating number of cyberattacks attributed to DPRK intrusion sets.

![Figure 7. 2023’s DPRK intrusion sets and campaigns targeting fintechs and cryptocurrencies ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fb16f788fda8e51023_6a92a355a2f46752fd019658_6a2a7c50b7830b74300a463f.webp)

Figure 7. 2023’s DPRK intrusion sets and campaigns targeting fintechs and cryptocurrencies 

### Espionage operations disguised as lucrative

In 2022, Sekoia.io TDR analysts observed state-sponsored intrusion sets conducting strategic espionage campaigns targeting the financial sector under the cover of lucrative motivations. This is the first time Sekoia.io analysts have observed such operations.

#### Chinese intrusion sets camouflaging their final goal

Over the past years, Chinese Advanced Persistent Threats (APTs) have broadened their scope of attack by conducting [ransomware ](https://www.bleepingcomputer.com/news/security/cheerscrypt-ransomware-linked-to-a-chinese-hacking-group/)attacks. Nevertheless, lucrative ransomware campaigns remain unusual in the Chinese threat landscape.

In 2022, [Secureworks ](https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader)identified China-nexus intrusion sets Bronze Riverside and Bronze Starlight conducting ransomware attacks using the HUI loader to hide cyberespionage operations. These attacks notably impacted two financial institutions in the United States. 

According to Secureworks, this type of campaign disguised as financially motivated is used to hide strategic operations related to espionage. Sekoia.io TDR analysts assess it can also be a way to reduce the cost of strategic operations in the context of the current Chinese economic crisis. This trend was previously observed within the North Korean state-sponsored threat landscape.

#### American spyware disguised as a crypto miner

In 2022, [Kaspersky ](https://securelist.com/stripedfly-perennially-flying-under-the-radar/110903/)found unusual detections within the WININIT.EXE process, revealing an older code associated with the Equation malware, initially misclassified as a cryptocurrency miner in 2017. Further analysis uncovered that the cryptocurrency miner was an element of a more complex malware entity. This malware, called StripedFly, utilised a custom EternalBlue SMBv1 exploit publicly disclosed by the Shadow Brokers group in April 2017. Notably, the worm stood out due to its discreet propagation method, allowing it to evade detection, and enabling the remote execution of commands in the victim’s systems.

## Conclusion

The expanding threat of Phishing-as-a-Service continues to impact the financial sector, emerging PhaaS kits including a large number of financially-themed pages and websites.

The ongoing trend of QR code phishing campaigns will highly likely persist in the next months, due to its effectiveness in evading detection and bypassing email protection solutions.

The evolving landscape of malware targeting financial assets involves the expansion of top-tier Latin American banking trojans to European banks, as well as the use of spyware in bank fraud campaigns.

The financial sector faces an increasing risk of lucrative supply chain attacks, as stressed by the surge in supply chain campaigns particularly targeting open-source components. 

The ransomware and extortion threats are continuously expanding, increasingly impacting financial organisations. Prominent ransomware groups mostly leverage the double-extortion techniques in campaigns against the financial vertical. The consistent attackers' interest in collecting sensitive data from victims prompts a growing shift towards extortion groups prioritising data exfiltration over encryption.

The development of fintechs to aggregate financial services or in DeFi, offers new opportunities for cyberoperations due to their less restrictive regulation framework compared to traditional financial entities and to their important number, which reduces the consumer's capacity to differentiate trusted services versus malicious. 

Among state-sponsored intrusion sets, DPRK-nexus ones remain the most active. They mostly focus on the crypto assets industry entities and entities located in Asia and the United States, rather than on European traditional banking institutions. Other state-sponsored intrusion sets also take advantage of the noise made by lucrative operations to disguise their cyberespionage campaigns.