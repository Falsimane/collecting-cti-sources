# Cyber Threats Impacting the Financial Sector in 2024: Focus on Main Actors

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/cyber-threats-impacting-the-financial-sector-in-2024-focus-on-the-main-actors
- **Date :** 2025-02-20

---

_This report will dive into cybercrime actors and state-sponsored intrusion sets tracked and documented by Sekoia. As this report is a synthesis of latest 2024 campaigns targeting financial entities, further information on the intrusion sets at the origin of the attacks and mentioned below can be found on the Sekoia.io platform, including a history of their past operations and descriptions of their tactics, techniques and procedures. If additional information is requested on a specific threat actor, please contact us at tdr@sekoia.io._

_This article was originally distributed as a private FLINT report to our customers on 6 February 2025._

## Executive summary

  * **Initial Access Brokers** (IABs) play a critical role in the cybercrime activities impacting the financial sector, enabling large-scale, **multi-layered attacks** by monetising unauthorised network access.
  * **Ransomware and extortion actors** pose a major threat to the financial sector, conducting consistent campaigns that leverage advanced malware, exploit vulnerabilities, disrupt operations, and cause major financial and reputational damage.
  * Prolific **Trojan operators** deploy increasingly **sophisticated banking malware** in targeted campaigns, exploiting desktop and mobile vulnerabilities, including biometric data theft, to compromise financial institutions globally.
  * The large adoption of the **Phishing-as-a-Service** model for Adversary-in-the-Middle (AiTM) campaigns **democratises advanced phishing capabilities** and fuels high-volume, targeted attacks on financial institutions.
  * State-sponsored threat actors are also targeting the financial sector for various motivations, ranging from **making financial gain** to **covert cyber espionage operations** and **destabilisation**.
  * Historical APTs targeting the sector are attributed to North-Korea, which use cyber operations against lucrative targets to **bypass international economic sanctions** and**finance its ballistic missile and nuclear weapons programs**.
  * APTs attributed to Iran and China also targeted the sector and cooperated with cybercrime operators to**improve the cost-benefit tradeoff of strategic cyber operations and cover the tracks of state-sponsored operations.**
  * State-sponsored threat actors sometimes pursue both financial gain and intelligence gathering. This dual motive is partly driven by some governments **outsourcing** segments of their cyber operations to **private entities**. These profit-driven private actors have been observed exploiting accesses used for strategic operations for their own benefit afterwards.



## An overview of the cybercrime actors impacting the financial sector

Discussing the lucrative cybercrime actors specifically targeting the financial sector is challenging due to their opportunistic nature and ability to rapidly adapt to evolving opportunities for expanding the attack surface. The continuous expansion of the **Malware-as-a-Service (MaaS)** and, more broadly, the **Cybercrime-as-a-Service (CaaS) ecosystems** , further blurs the lines between distinct intrusion sets, making the **attribution** of cybercrime campaigns to specific groups or individuals **increasingly difficult**. This fragmentation specific to the cybercriminal ecosystem also complicates efforts to analyse and cluster specific actors.

In this section, we will provide a breakdown of the most prevalent actors in the cybercrime landscape that were observed conducting campaigns impacting the financial sector.

### Initial Access Brokers (IABs)

The **Initial Access Brokers** (IABs) are individuals or groups that specialise in gaining **unauthorised access** into networks and systems, often through phishing attacks, exploitation of vulnerabilities, or compromising Remote Desktop Protocols (RDP). They commonly **sell access** on cybercrime forums and marketplaces to other malicious actors, often to the highest bidder. In other instances, access brokers are consolidated intrusion sets closely collaborating with a limited number of actors. These interactions highlight increasingly complex correlations among attackers, enabling numerous intrusion sets to bypass the initial access phase to focus on monetising the further steps of their operations. 

![Example of an IAB selling unauthorised initial access](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aa98ef92d9dbcbd71b4a312_blog-example-of-an-iab-selling-unauthorised-initial-access.webp)

Example of an IAB selling unauthorised initial access

The **impact** of IABs extends beyond the immediate consequences of a breach. They act as key enablers of large-scale cybercrime campaigns by facilitating access to critical systems. The proliferation of initial accesses sold by IABs on different platforms significantly**reduced the entry barrier** for subsequent compromises, leading to**increasing volume and diversity of attacks** , often involving coordinated, multi-layered campaigns. 

Some of the most well-documented IABs that are known for targeting financial institutions in their campaigns are **TA577** , **TA569** , **TA570** , **Hive0145** , [**Prophet Spider**](https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2022GTR.pdf) (_aka_ UNC961 _aka_ Gold Melody), among others. Intrusions conducted by those IAB actors over the past few years commonly ended up with ransomware deployment. Yet, there is increasing evidence of state-sponsored actors closely cooperating with other IABs or even acting as IABs (_e.g._ the Iran-nexus APT33, as detailed later in this report).

So, the emergence of IABs led to the commoditisation of cybercrime, with access to financial assets becoming a transactional good that can be sold to multiple actors. As financial institutions store vast amounts of sensitive data and operate critical infrastructure, such attacks can finally lead to disruptions, reputational damage, and substantial financial losses. Moreover, the interconnected nature of the financial ecosystem amplifies the risks of supply chain compromises.

### Ransomware and extortion actors

Ransomware and extortion-related intrusion sets represent a **significant and persistent threat** to the financial sector. As we [outlined](/blog/unmasking-the-latest-trends-of-the-financial-cyber-threat-landscape) in the first part of our financial cyber threat landscape, dated November 2023, the financial industry was identified as **one of the most impacted by ransomware** campaigns in recent years.

Financial institutions, including banks, insurance providers, and payment processors, represent attractive targets due to several factors. Their widespread presence, critical operational functions, reliance on third-party supply chain vendors, and access to sensitive data make them lucrative for attackers. Disruptions in this sector not only causes operational downtime but also risks significant reputational damage and financial loss.

During 2024, numerous ransomware groups such as **RansomHub, Scattered Spider, Qilin**(_aka_ Agenda),**LockBit,** and **Meow,** publicly claimed financial entities as victims. These intrusion sets **most often conducted lucrative, opportunistic campaigns**. Yet, in isolated cases, ransomware intrusion sets can conduct campaigns of economic sabotage, or else affiliates of Ransomware-as-a-Service (RaaS) operations can prove to be members of state-sponsored groups.

The ransomware campaigns conducted by major threat groups in 2024 against the financial sector and other industries are relatively advanced, with an increasing incidence of attacks exploiting zero-day vulnerabilities, supply chain attacks, and double extortion tactics. One notable example is the [exploitation](https://www.huntress.com/blog/threat-advisory-oh-no-cleo-cleo-software-actively-being-exploited-in-the-wild) of at least two zero-day vulnerabilities in file transfer software developed by Cleo. First identified in December 2024, this campaign was [claimed](https://www.bleepingcomputer.com/news/security/clop-ransomware-claims-responsibility-for-cleo-data-theft-attacks/) by TA505, a well-established intrusion set known to deploy the Cl0p ransomware, that engaged in post-exploitation activity. TA505 is a major ransomware and extortion actor that repeatedly conducted massive vulnerability exploitation campaigns, including supply chain attacks, affecting a wide range of sectors worldwide.

#### RansomHub

Another example of highly prolific ransomware actors in 2024 is **RansomHub** , a RaaS and extortion group first observed in February 2024. Since its emergence, it quickly [became](https://www.rapid7.com/blog/post/2025/01/27/the-2024-ransomware-landscape-looking-back-on-another-painful-year/) one of the most active and impactful intrusion sets in the ransomware threat landscape. Its rise was likely fuelled by the takedown of LockBit and the scam exit of the BlackCat operation shortly beforehand.

RansomHub develops and distributes its own **custom ransomware** , which is also utilised by other advanced intrusion, including **CosmicBeetle, Scattered Spider,** and **Evil Corp**. RansomHub stands out for its diverse evasion techniques, particularly its capabilities to **bypass EDR systems**. This includes the deployment of a custom malware known as **EDRKillShifter** , designed to disable or manipulate EDR solutions and increase the success rate of its campaigns. Based on Trend Micro [data](https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-ransomhub), the financial sector represented 8,6% of RansomHub’s victims between July 2023 and September 2024.

#### Scattered Spider

Another prominent intrusion set reported deploying several ransomware strains is **Scattered Spider** , active since at least May 2022. The intrusion set’s campaigns leveraging ransomware such as **RansomHub, BlackCat and Qilin** impacted a wide range of industries over time, including the financial sector. Notably, EclecticIQ reported on a long-term Scattered Spider campaign **targeting cloud infrastructures** within the insurance and financial sectors up to Q2 2024. 

One of most notable techniques leveraged by Scattered Spider is targeted phishing. Starting from mid-September 2024, Sekoia analysts [identified](https://app.sekoia.io/objects/infrastructure--77a45e35-fcd2-4c93-b4a2-89885f099070) a new website template used by the intrusion set to create phishing pages impersonating specific organisations.These phishing pages mimic the Okta login portal and are hosted in the AS 39287 (ABSTRACT, FI). They use almost empty HTML pages, loading JavaScript and a fake authentication page. 

Part of this infrastructure targets financial assets, such as the Revolut banking platform. Examples include domains like okta-revolut[.]com and revolut-okta[.]com, that target Revolut employees. This is persistent with Reliaquest’s [observations](https://www.reliaquest.com/blog/report-finds-50-of-scattered-spider-phishing-domains-targeted-finance-insurance/), reporting that 20–25% of domains impersonated by Scattered Spider in the second half of 2024 targeted the finance and insurance sectors, while 25–30% impersonated cryptocurrency platforms, collectively representing 50–55% of their activity.

![Typosquatted domain and phishing page](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aa99169e52ccabc328c7017_blog-typosquatted-domain-and-phishing-page.webp)

Typosquatted domain and phishing page

### Prolific Trojan operators

Malware targeting banking assets, notably desktop and mobile banking trojans, are one of the **longest-standing threats faced by the financial sector**. The malicious codes used, along with the groups deploying them, are increasingly sophisticated and, above all, continue to expand their scope of operations.

#### Solar Spider

**Solar Spider** is one such advancedintrusion set distributing a **custom** JavaScript Remote Access Trojan (RAT) known as **JSOutProx**. The malware is continuously updated to expand its capabilities and broaden its scope of use, with a new version deployed to an extended list of targets starting in early 2024.

Unlike many cybercriminal actors whose activities are largely opportunistic, such as ransomware or infostealer operators, **Solar Spider** engages in **targeted campaigns**. According to open-source reports dating back to 2019, the intrusion set’s **targeting** consists mainly of **financial entities**. While Solar Spider operations initially focused on small and medium-sized businesses within the Asia-Pacific (APAC) region, they **expanded their campaigns into the Middle East and North Africa** (MENA) region, significantly amplifying their cybercriminal activities.

In 2024, analysis by Resecurity [indicated](https://www.resecurity.com/blog/article/the-new-version-of-jsoutprox-is-attacking-financial-institutions-in-apac-and-mena-via-gitlab-abuse) with moderate confidence that JSOutProx may have been developed by actor(s) from China or those affiliated with it.

#### GoldFactory

**GoldFactory** is another advanced intrusion set actively targeting financial institutions to deliver **custom mobile malware** since mid-2023. GoldFactory develops and deploys a range of highly sophisticated **banking Trojans** , including GoldPickaxe, GoldKefu, GoldDigger, and GoldDiggerPlus.

While the GoldFactory victims over 2023 and 2024 were mainly located in the APAC region, Group-IB analysts [assess](https://www.group-ib.com/blog/goldfactory-ios-trojan/) that **GoldFactory’s geography** of operations may **extend** beyond the initially targeted countries, which were Vietnam and Thailand.

One of the main intrusion set’s deployed malware is **GoldPickaxe** , an advanced mobile Trojan which includes versions for iOS and Android. GoldPickaxe's purpose is to gather personal information from victims,**along with biometric data such as facial recognition**. The stolen data is leveraged to create deepfakes in order to autonomously access the victim’s banking application. 

The GoldFactory malware is notable for being the first iOS Trojan **harvesting facial recognition data used for unauthorized access to bank accounts**. This development is closely related to adoption of facial authentication as a security measure for money transfers applied in the target countries.

As of February 2024, Group-IB has not identified any instances of these malware being sold on cybercrime forums and marketplaces. Therefore, it is challenging to determine whether the above-mentioned banking malware could be adopted for wider distribution within the cybercriminal ecosystem.

GoldFactory is reported being almost certainly **composed of Chinese-speaking members** , along with local cybercriminals from the targeted countries such as Vietnam and Thailand. Moreover, the group includes distinct development and operational teams, each focusing on specific regions. These findings align with the expansion of the Chinese-speaking cybercriminal ecosystem observed over the past five years, possibly extending their targeting from China to other regions.

It is worth noting that while the Trojan operators mentioned above are reportedly expanding their target regions beyond APAC, traditional Banking Trojans are now rarely, if ever, used against Western entities. These Trojans primarily relied on web injection techniques to manipulate data in web browsers, particularly on banking websites. However, modern browsers become increasingly secure, progressively incorporating features to prevent such attacks.

Furthermore, the widespread adoption of two-factor authentication (2FA) makes it difficult to exploit stolen credentials obtained through basic phishing pages. Enhanced processes, tools, and security measures have likely rendered these attacks less effective for organisations. As for individuals, most bank transfers now take place via mobile applications, which are generally secure enough to prevent such threats.

### Phishing-as-a-Service: An increasingly specialised cybercriminal ecosystem

Based on Sekoia data, the most prevalent phishing-related threats as of early 2025 include Tycoon 2FA, NakedPages, Sneaky 2FA, Storm-1167 and Evilginx. This aligns with recent [observations](https://x.com/anyrun_app/status/1881582706636493281) from ANY.RUN which also highlights Mamba 2FA**.** At least three of these (Tycoon, Mamba, Sneaky) represent major **Adversary-in-the-Middle (AiTM) phishing kits** distributed under the Phishing-as-a-Service (PhaaS) model, while Evilginx is an open-source AiTM kit available on GitHub. The PhaaS model allows phishing kit developers to provide pre-built phishing tools and infrastructure to other operators, notably pertaining to the cybercriminal lucrative ecosystem.

The adoption of the **PhaaS model typically amplifies the threat** by offering ready-to-use, scalable phishing kits, thereby lowering the barrier to entry for cybercriminals. This typically results in a higher volume of attacks and poses attribution challenges. Furthermore, PhaaS frameworks are often highly customisable, enabling targeted campaigns that frequently focus on specific industries, including financial institutions.

#### Tycoon 2FA phishing kit 

Storm-1747 is an intrusion set that develops and operates the Tycoon 2FA phishing kit since at least mid-2023. The phishing kit has since been sold and distributed in the wild under the PhaaS model. As of early 2025, Tycoon is the most widespread phishing kit, based on Sekoia telemetry.

The phishing kit leverages the AiTM technique, using an attacker-controlled reverse proxy server to host the phishing webpage, intercept victims’ inputs, relay them to the legitimate service, and prompt the MFA request. Once the user completes the MFA challenge and authentication is successful, the server captures session cookies, enabling attackers to hijack the session and bypass MFA, even if credentials are later updated. By successfully mimicking login pages, Tycoon makes it more difficult for end-users to identify phishing attempts, increasing the likelihood of successful attacks.

#### Sneaky 2FA phishing kit

Sneaky 2FA is one of the latest notable newcomers to the PhaaS ecosystem, operating as an AiTM phishing kit and distributed in the wild since at least October 2024. As of December 2024, Sneaky 2FA phishing pages were hosted on compromised infrastructure, including hijacked WordPress websites and other attacker-controlled domains.

Sneaky 2FA is sold to other cybercriminal actors via Telegram channels by a persona known as**"Sneaky Log"** (also referred to as Sneaky Support). Sekoia analysts assess**with high confidence** that the Sneaky developer adapted portions of code from the W3LL OV6 phishing kit, previously documented by Group-IB. This highlights the continuous interconnectivity within the Cybercrime-as-a-Service ecosystem, where code sharing and repurposing among cybercriminals enable rapid innovation and expansion of malicious capabilities.

## An overview of APTs targeting the financial sector

This section focuses on a second category of threat actors targeting the financial sector, which are the state-sponsored Advanced Persistent Threats (APTs). These are malicious clusters operated, contracted or financed by a state’s intelligence service to support its strategic objectives. These groups can be made up of military units, state bureaus, but also private companies’ employees, and civilians recruited from universities or hacker communities.

Conventionally, the primary motivation of APT groups is intelligence gathering. Accessing data from financial institutions can serve for individual surveillance purposes, but also for exercising political pressure on another country. 

However, given the critical role of financial services for populations and their inherent access to massive money flows, the **principal objective of state-sponsored operations targeting this sector is either lucrative or disruptive**. This particularity of APTs operations targeting the financial sector will be further developed in this section.

### Motivations behind state-sponsored campaigns targeting the financial sector

State-sponsored threat actors’ operations are motivated by **strategic objectives**. Due to the ability of a state to invest massively in cyber capabilities to achieve a specific political goal, state-sponsored operations are characterised by their **high-level of sophistication** and their **precise targeting**. 

As far as the financial sector is concerned, there are a number of strategic objectives for conducting cyber operations. 

First, state-sponsored actors can be tasked with generating **financial gain** to bypass international sanctions or to fund strategic plans. These motivations are found in particular in campaigns conducted by **North Korean** APTs, which target **financial entities as well as cryptocurrencies,** and by **Iranian** APTs, which focus mainly on**financial entities** in the **Middle East**. To a lesser extent, when state-sponsored operations are outsourced to private companies, civilian employees can use the access gained for the operation to make profit and complete their revenue. This was especially observed for APTs attributed to **China** , such as APT41.

Second, state-sponsored cyber operations can serve **espionage purposes** , such as gaining information about individuals or about a targeted entity (a company, a country). This was especially the case for APTs attributed to **Iran** targeting Israeli entities and to **China** in South East Asia targeting neighboring countries ahead of negotiations for commercial policies in the region.

Finally, cyber operations attributed to a state can target financial entities for disruptive purposes such as APTs related to **Russia** , which targeted Ukrainian banks to destabilise the country in the context of the war.

### North Korean APTs historically targeting the financial sector

Historically, **North Korean intrusion sets** are the most active in targeting financial entities. They mostly focused on luring individuals to access networks of strategic entities and conducting supply chain attacks, including banks. They also largely target decentralised finance (DeFi) and cryptocurrencies.

North Korea has leveraged cyber operations for strategic purposes since at least 2004, including **cyberespionage** , **lucrative** campaigns, **destructive** and **disruptive** attacks. This country [adapted its strategy in 2014](https://home.treasury.gov/news/press-releases/sm774) to focus on targeting banks, cryptoassets entities and financial technology companies in order to maintain its economy despite international sanctions and finance its ballistic missile and nuclear weapons programs. 

![DPRK-nexus intrusion sets](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aa9940aca56b5e313e4cedd_blog-dprk-nexus-intrusion-sets.webp)

DPRK-nexus intrusion sets

North-Korean intrusion sets conducting operations against financial institutions are concentrated in the **Reconnaissance General Bureau (RGB)** , which is part of the State Affairs Commission. Of note, **Lazarus** is one of the most active intrusion sets operating the RGB lucrative campaigns for the purpose of North Korea’s military development, followed by **Andariel** and **Bluenoroff** , two Lazarus sub-groups.

Lazarus has been active since at least 2009 and is known to encompass a broad range of activity from cyberespionage and destructive operations to lucrative campaigns. Its operations focus mainly on the defence industry as well as finance and cryptocurrencies platforms and users. Lazarus campaigns are particularly sophisticated due to their creative spearphishing techniques to lure victims and the constant evolution of their tools, techniques, and procedures.

Lazarus **has used fake job offers several times** to target high-profile individuals and infect strategic companies’ networks like banks. It was the case with the **Operation Dreamjob** discovered in 2020, and more recently with the**VMConnect campaign** identified in August 2023. [During the VMConnect campaign](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html), the attacker impersonated a major US financial services firm, CapitalOne, recruiting individuals working in the financial sector. 

In a fake process of recruitment, jobseekers have to complete a Python exercise provided via a link sent on LinkedIn and directing to a GitHub repository. In a short time, the candidate has to find a bug, resolve it and push changes that address the bug, leading the victim to execute the project on his/her machine. Once executed, it delivers a Python backdoor sending HTTP POST requests to a C2 and executing Python commands.

These operations, ongoing since at least 2019, are targeting critical sectors, such as defense, IT, finance, and especially developers and engineers. This aims at taking profit of human error to conduct**supply chain attacks** on widely used products and compromise critical targets. 

These malicious campaigns are well-documented by security vendors and translate the **constant evolution of tools, techniques, and procedures** of this intrusion set. [In a 2024 report](https://securelist.com/lazarus-new-malware/115059/), Securelist researchers analysed the evolution of the Operation Dreamjob. They highlighted that between 2023 and 2024, the infection chain of this campaign totally changed. Even if Lazarus still heavily rely on weaponised open-source software, such as VNC and PuTTY, latest investigations unveiled it switched to malicious ISO files instead of ZIP files to evade detection, and used new malicious programs or variants, like [MISTPEN](https://cloud.google.com/blog/topics/threat-intelligence/unc2970-backdoor-trojanized-pdf-reader?hl=en), [LPEClient](https://securelist.com/unveiling-lazarus-new-campaign/110888/#lpeclient), [RollMid](https://decoded.avast.io/luiginocamastra/from-byovd-to-a-0-day-unveiling-advanced-exploits-in-cyber-recruiting-scams/), and [CookiePlus](https://securelist.com/lazarus-new-malware/115059/).

#### Lazarus

Lazarus is an umbrella under which other sub-groups conducting operations against financial institutions are located. Among them is **Bluenoroff** , a North Korea-nexus intrusion set who has been active since at least 2014 and subordinated to the**RGB 121 bureau.** Itconducts financially-driven campaigns against banks, ATMs, cryptocurrency exchanges and venture-capital related entities [in line with North Korea's strategic objective of sanction evasion](https://home.treasury.gov/news/press-releases/sm774). Their targets are from various parts of the world, as Bluenoroff's objective is to maximise the profit of its operations, instead of collecting precise information. It explains why it has a particularly broad victimology compared to other APTs.

This intrusion set especially developed [macOS malware](https://www.sentinelone.com/labs/bluenoroff-hidden-risk-threat-actor-targets-macs-with-fake-crypto-news-and-novel-persistence/) to target financial institutions. This is a three-stage malware dubbed **RustBucket** , which allows C2 communication and the execution of various payloads. First seen in 2022, it was leveraged by Bluenoroff in the [**SnatchCrypto campaign**](https://www.elastic.co/fr/security-labs/DPRK-strikes-using-a-new-variant-of-rustbucket) to target companies dealing with cryptocurrencies, DeFi, blockchains, and smart contracts, as well as the FinTech industry. The threat actor infiltrated internal and external business communications to map the interactions and identify topics of interest. The objective of the campaign was to collect credentials, as well as stealing cryptocurrencies.

#### Bluenoroff

In 2024, Bluenoroff was also considered**responsible for the largest crypto hack of the year,** according to [the FBI, the Defense Department and the National Police Agency of Japan](https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom). Indeed, the theft of **$308 million in cryptocurrency** from the Japanese platform DMM has been attributed to Bluenoroff and leveraged the **TraderTaitor** malware. First seen in 2022, TraderTraitor is a malicious application derived from various open-source projects. It pretends to be cryptocurrency trading or price prediction tools to lure the victims. 

TraderTraitor campaigns feature websites with modern design advertising the alleged features of the applications. An “update” function downloads a payload using a HTTP POST request to a PHP script hosted on the C2. Among payloads executed are included **updated macOS and Windows variants of Manuscrypt** , allowing to collect system information, execute arbitrary commands and download payloads.

#### Andariel

Another sub-group under the Lazarus umbrella is**Andariel.** It isan intrusion set related to the**RGB 3rd Bureau** whohas evolved from conducting destructive attacks against US and South Korean entities, to cyber espionage and ransomware operations. One of its **principal objectives is to collect information for Pyongyang’s nuclear and defence programs** , while ransomware campaigns serve to fund its espionage activity. It already targeted financial institutions with ransomware attacks because of the**lucrative nature of financial activities.**

While investigating [a 2024 Play ransomware incident](https://unit42.paloaltonetworks.com/north-korean-threat-group-play-ransomware/), researchers from Unit42 assessed with high confidence that the initial access was obtained by Andariel in May. It indicated that the North Korean APT would proceed as an**IAB** or an **affiliate of the Play ransomware group** and shift towards a deeper involvement in the cybercrime ecosystem. Indeed, this incident brought to light the first case of**known collaboration** between this intrusion set and a ransomware group. The Play ransomware group declared on its leak site that it does not provide a Ransomware-as-a-service ecosystem (RaaS). If this is true, Andariel might only have acted as an IAB, according to Unit42. In any case, the involvement of sophisticated North Korean APTs in ransomware campaigns represents an emerging trend potentially leading to more damaging attacks.

### APTs and cybercrime operators collaboration

As well as North-Korea-nexus intrusion sets, other state-sponsored threat groups turned to financially-motivated operations against the financial sector in addition to cyberespionage. These lucrative campaigns aim at bypassing international sanctions, but also at taking profit from the cybercrime ecosystem to**improve the cost-benefit tradeoff of strategic cyber operations.**

#### APT33

In August 2024, the [FBI and CISA reported](https://www.cisa.gov/sites/default/files/2024-08/aa24-241a-iran-based-cyber-actors-enabling-ransomware-attacks-on-us-organizations_0.pdf) that **APT33,** an **Iran-nexus intrusion set** active since at least 2013,was conducting**IAB** campaigns under the aliases "Br0k3r" and "xplfinder" on cybercrime forums and marketplaces. Acting as an IAB, APT33 focused on gaining and maintaining technical access to victim networks to facilitate future ransomware attacks. The Iranian cyber actors’ role extends beyond providing access. The FBI identified that these actors worked directly with ransomware affiliates, assisting in encryption operations in exchange for a share of the ransom payments. Documented incidents revealed APT33 collaborating with ransomware groups such as **NoEscape, Ransomhouse, and BlackCat**.

**APT33** is an Iranian state-sponsored threat group active since at least 2013. It has targeted organisations in the United States, Saudi Arabia, and South Korea, with a strong focus on the aviation and energy sectors. Given its destructive capabilities, overlapping activities with other Iranian APTs, and shared victimology, it has been attributed to the **Islamic Revolutionary Guard Corps (IRGC)**. APT33, as other groups subordinated to the IRGC, pass contracts to operate under the guise of a private company to harden attribution. Among them is **Danesh Novin Sahand** , who is associated with the APT33’s sub-group **Fox Kitten**.

Historically, APT33 has been associated with **hack-and-leak campaigns** , such as the **Pay2Key operation** in late 2020, an information warfare operation designed to undermine the cybersecurity of Israeli infrastructure. In the case of APT33’s ransomware activities, they appear to be primarily focused **on stealing sensitive information**.

#### ChamelGang

On a different model from Iran-nexus intrusion sets,several **state-sponsored cyber threats attributed to China** rely on the cybercrime ecosystem for their malicious campaigns.

**ChamelGang** , a China-nexus intrusion set active since at least March 2021, was observed carrying out cyberespionage campaigns against critical infrastructure in various countries. In addition, [Positive Technologies](https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/new-apt-group-chamelgang#id3-1), [Sentinel One](https://assets.sentinelone.com/sentinellabs/chamelgang-friends-en) and [TeamT5](https://stillu.cc/assets/slides/2023-08-Unmasking%20CamoFei.pdf) assessed that this APT pursues objectives beyond intelligence gathering, like Personally Identifiable Information (PII) theft and financial gain operations. For that purpose, it was reported that ChamelGang used the **CatB ransomware**. 

Indeed, since at least 2022, this intrusion set leveraged ransomware to target high-level victims, such as the major Indian healthcare institution AIIMS and the Presidency of Brazil. The use of RaaS by state-sponsored threat actors can be interpreted as a way to **make additional profit** , but also as **a way to distract victims from its cyberespionage focus**. Indeed, it can help to cover the track of a compromise, as well as leading to misattribution of cyber espionage campaigns to cybercrime operators. As ChamelGang used to deploy ransomware at the end of its operations, an hypothesis is that it is used as a cover for intelligence gathering.

### Double motivation due to outsourcing of cyber capabilities in APT operations

The dual interest of some APTs for intelligence gathering and financial gain can be explained by the hack-for-hire ecosystem. In China, state units are known to **outsource part of their cyber operations to private companies**. Companies operating part of state-sponsored operations can then use the access for their own benefits, explaining this double objective.

Indeed, the**2024 I-SOON leaks** revealed that several cyber range businesses operate part of state-sponsored cyber campaigns. For instance, I-SOON proceeds by gaining access to various systems and selling them to state entities, especially to Provincial and City-level State Security Bureaus, for strategic operations. This profit-driven way of operating is likely to be adopted by other companies similar to I-SOON, such as **Chengdu 404, Integrity Technology, and Sichuan Silence**. 

Chengdu 404 and I-SOON are operating for State Security Bureaus, under the Ministry of State Security (MSS), and linked to **APT41**. This intrusion set is known for conducting both intelligence gathering, as well as financial gain campaigns. An hypothesis is that private companies operating for state-sponsored operations attributed to APT41 also use access, malware and tools for their own profit and complete their revenues.

## An overview of hacktivism activities impacting the financial sector

Hacktivism nowadays can refer to two types of actors. The first one refers to malicious cyber campaigns, mainly leveraging DDoS or data leaks, conducted by individuals or groups **to promote political or ideological agendas**. These threat actors typically target governments, corporations or entities they oppose, aiming to disrupt operations, spread propaganda, or cause reputational harm.

The second type of hacktivism is what we call **nationalist hacktivism** , conducting the same kind of operations on political entities, in order to support the interests of their own country. Those groups are often partially supported by intelligence services (financially, access, targeting). Nationalist hacktivism rose on a larger scale starting from 2022, in conjunction with Russia’s invasion of Ukraine. Over this period, multiple groups such as KillNet, Anonymous Sudan or NoName conducted hacktivism-like operations to support Moscow. Moreover, it was further amplified by other major events, in particular political and geopolitical ones such as the Israel-Hamas war.

Over the past years, the **hacktivist threat expanded across most sectors, including the financial industry**. From July 2023 to June 2024, banking and insurance [represented](https://www.enisa.europa.eu/sites/default/files/2024-11/2024%20Report%20on%20the%20State%20of%20the%20Cybersecurity%20in%20the%20Union.pdf) the third most targeted sector by hacktivists groups within the European Union.

![Screenshot of a NoName057\(16\) Telegram post claiming DDoS attacks against UK websites, showing browser error pages and listing targets including UK Finance, Money Advice Service, local councils, and a site labelled “SWIFT card authorization.”](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aa9996d8692befc0013263a_blog-noname057\(16\)-telegram-post.webp)

NoName057(16) Telegram post

The hacktivist groups most actively targeting the financial sector were DDoSia and Killnet, which is in line with the global landscape of the hacktivist activities. In 2024, DDoSia targeted around 140 financial related entities among the millions of targets in Europe of its DDoS campaigns. However, it is worth noting that cybersecurity teams regularly face DDoS attacks that remain unclaimed and therefore harder to attribute.

A significant event occurred in January 2024 when DDoSia launched a DDoS attack against a website labeled “SWIFT card authorization.” Interestingly, the targeted website was unrelated to the Society for Worldwide Interbank Financial Telecommunication (SWIFT), the secure messaging network enabling financial institutions to exchange transaction data. Instead, the attack targeted a website associated with a bus card system named SWIFT. This incident highlights that, beyond the operational disruption caused by a DDoS attack on financial entities, such cyberattacks can result in substantial reputational damage, even affecting entities that experience no technical issues with their services.

Beyond the operational concerns related to targeted services’ unavailability, another expected impact is the erosion of public confidence in these services, which could be critical to the functioning of democratic institutions.

Nevertheless, the intensity of the hacktivist rhetoric claiming massive campaigns against financial assets are often followed by**limited or isolated impact**. This is likely indicative of the financial entities’ resilience, alongside anticipated cybersecurity measures.

## Conclusion

This report summarises the latest intelligence on key cybercrime and state-sponsored intrusion sets conducting malicious campaigns against the financial sector.

The advanced intrusion sets conducting lucrative campaigns are consistently expanding their capabilities along with their targeted areas. Among them, the most prolific are IABs, Trojan operators, phishing, ransomware and extortion actors. 

The report also dived into the various motivations of state-sponsored threat actors to target financial entities, ranging from intelligence gathering, to financial gain and destabilisation. APTs attributed to North Korea historically targeted the sector to sustain their economy and develop their ballistic nuclear missile program. 

In parallel, other APTs are collaborating with cybercrime operators, especially IABs and RaaS, to optimise the cost-benefit of their operations and cover their tracks in targeted systems. 

Finally, the outsourcing of part of APT’s operations to private entities also leads profit-driven actors to take advantage of the access to strategic targets to extort money.

## Read the full version of this article in PDF

The full version of this article is [available in PDF format](https://0H3WGygmjL.flowdrivecdn.com/tCocpzWxtBxaqR39ovVqn). Feel free to read it and share it with your network.