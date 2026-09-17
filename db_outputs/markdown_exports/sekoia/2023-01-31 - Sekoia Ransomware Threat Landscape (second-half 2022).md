# Sekoia Ransomware Threat Landscape (second-half 2022)

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/sekoia-io-ransomware-threat-landscape-second-half-2022
- **Date :** 2023-01-31

---

## Background and evolutions

The ransomware threat marked a very high level in the second half of 2022, similar to the previous year. Based on publicly available data, **LockBit was the most prolific ransomware group** , currently spreading the LockBit Black version of its software. **Royal ransomware** \- a newcomer on the double extortion scene - showed a noticeable increase in its activity in the last months.

Ransomware incidents impacting Latin American countries surged in Q2 2022, most likely to broaden the conventional target areas, as a decline in ransom payments was [reported](https://blog.chainalysis.com/reports/crypto-ransomware-revenue-down-as-victims-refuse-to-pay/) in 2022.

Another notable observation is the **emergence of multiple LockBit- and Conti-derived ransomware families**. It is highly likely this comes after malware source code and internal handbooks were leaked and became available to the entire cybercrime community.

Most of the threat actors who reused the leaked source code currently run simple extortion ransomware campaigns without data exfiltration and use generic ransom notes and extensions. Such examples are ScareCrow, Meow and Putin ransomware crews.

For post-exploitation, threat actors increasingly use the **Brute Ratel framework**. This almost certainly stems from the fact that a cracked version was shared in September 2022.

These evolutions emphasise the **democratisation of the ransomware threat** at an almost unprecedented level. It also leads to more ransomware affiliates not being restricted to deploy a single piece of malicious code, but using different ransomware for different purposes. This is complementary to the trend of [affiliate rotation](https://www.trendmicro.com/en_us/research/22/l/conti-team-one-splinter-group-resurfaces-as-royal-ransomware-wit.html) between different Ransomware-as-a-Service (RaaS) groups.

## Evolving Tactics, Techniques and Procedures

### It's your call. Callback phishing attacks - a rising initial access method

The **callback phishing** method is a spearphishing tactic that impersonates legitimate platforms or businesses sending emails claiming the victim was or will be charged for a service, and urging victims to call a listed phone number for further clarifications. Calling this number directs the victim to a call centre service hired by the threat actors. Then, a “customer service representative” seeks to gain remote access and to distribute malware and/or to steal data from the victim’s network. This initial infection vector uses relatively advanced social engineering tricks, interfering with those of tech-support scams, and implies a **higher involvement of the human factor**.

This method (initially known as BazarCall aka BazaCall) emerged in early 2021 and was originally used by Ryuk (later Conti) operation. Its use among threat actors is still growing at present. Based on an Agari [research](https://www.agari.com/blog/whaling-phishing-email-fraud), hybrid phishing cases where the target interacts on the phone with an actual human being increased by 625% in volume in Q2 2022 compared to Q1 2021.

Starting from March 2022 and later on, **presumed former members of the Conti ransomware** group [began](https://www.advintel.io/post/bazarcall-advisory-the-essential-guide-to-call-back-phishing-attacks-that-revolutionized-the-data)**[1]** conducting callback [phishing campaigns](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers) on behalf of other ransomware operations they just founded or joined: **Luna Moth** (aka Silent Ransom aka TG2729), **Quantum** , and **Roy/Zeon** (aka Royal). It is highly likely that these experienced ransomware actors brought their expertise from the now closed Conti operation and adopted callback phishing as their primary method of gaining initial access and delivering ransomware under new group identities.

As IDs distributed in the phishing emails are [unique](https://www.bleepingcomputer.com/news/security/bazarcall-malware-uses-malicious-call-centers-to-infect-victims/) for each victim and focused on high-profile organisations, Sekoia analysts assess **documented campaigns leveraging this technique were targeted**. This is of particular interest as most cybercriminal activities are considered opportunistic in nature.

Over the second half of 2022, threat actors developed new, **derived forms of BazaCall technique** (_e.g._[Jörmungandr](https://www.advintel.io/post/bazarcall-advisory-the-essential-guide-to-call-back-phishing-attacks-that-revolutionized-the-data), leveraged by the Quantum group and employing individuals specialised in spamming, open-source intelligence, design, and call centre operations). Sekoia analysts assess more personalised versions of callback phishing campaigns will possibly emerge in the future for greater efficiency, possibly hindering tracking and detection efforts.

So far, the publicly documented incidents involving callback phishing led to the infection of Windows hosts. It is now uncertain whether this threat will expand to other Operating Systems such as Linux, as other cybercrime threats regularly do. We assess that conducting callback phishing attacks on Linux would require more advanced social engineering techniques, as Linux users would tend to be more aware of cyber–related risks.

While sending fake subscription notices by email remains the prevalent entry point for callback phishing attacks, in July 2022 CrowdStrike [reported](https://www.crowdstrike.com/blog/callback-malware-campaigns-impersonate-crowdstrike-and-other-cybersecurity-companies/) a new phishing lure used in a callback phishing campaign: emails impersonating prominent cybersecurity companies implied the recipient’s company was breached and insisted the victim call the included phone number.

Callback phishing campaigns remain an efficient way of bypassing existing security solutions. It is highly likely due to the fact that phishing messages do not include malicious components _per se_. Sekoia analysts assess the progressive adoption of the callback phishing technique provides further evidence of the **specialisation within the ransomware ecosystem** in recent times.

It was [reported](https://unit42.paloaltonetworks.com/luna-moth-callback-phishing/) ransomware groups invest in their own call centres, and there are also multiple call service providers on cybercrime forums who can notably offer malware distribution and ransomware negotiation. Sekoia analysts assess it is also likely that **ransomware groups outsource part of their callback phishing activities** to call centre services managed by other specialised threat actors.

Sekoia assess it is highly likely the callback phishing method will be routinely used by an increasing number of cybercrime groups in 2023. The leaked Conti’s internal manuals containing guidelines for ransomware affiliates would also facilitate the transfer of these methods to other threat groups. Highly organised cybercrime groups and human-operated ransomware operations are the most likely to adopt this method.

### Less is more. New ransomware operations opt for intermittent encryption

Ransomware actors recently resumed the **intermittent encryption** tactic (first [used by LockFile](https://news.sophos.com/en-us/2021/08/27/lockfile-ransomwares-box-of-tricks-intermittent-encryption-and-evasion/) in 2021) to encrypt files faster and evade detection solutions based on statistical analysis.

Ransomware operations emerging by mid-2022 ([**Agenda** , **Qyick** , **Play**](https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/) and [**Royal**](https://www.bleepingcomputer.com/news/security/bazarcall-malware-uses-malicious-call-centers-to-infect-victims/)) were reported opting for intermittent encryption in their campaigns. Moreover, the technique gained popularity and was recently [**adopted**](https://www.sentinelone.com/labs/crimeware-trends-ransomware-developers-turn-to-intermittent-encryption-to-evade-detection/)**by established ransomware groups** including BlackCat and Black Basta.

Encrypting the victim's files and/or system faster is likely a priority for the ransomware operators, as it reduces the risk of getting caught up in and stopped in the process. At the same time, intermittent encryption still allows threat actors to retain data in absence of a decryptor. So, ransomware groups can still achieve their primary goal of getting the ransom while the attack is performed in a shorter period of time. This also proves that Big Game Hunting ransomware groups are highly responsive to evolutions within the cybercrime and the information security ecosystems and tend to quickly adapt to emerging trends.

### Do you speak Rust? More ransomware groups expand to alternative programming languages

Multiple ransomware operations were recently reported converting their malware code from traditional programming languages to Rust. **Ransomware operators increasingly**[**develop**](https://www.zscaler.com/blogs/security-research/nokoyawa-ransomware-rust-or-bust)**cross-platform functionalities** for their operations, and moving to Rust is part of this trend.

The BlackCat ransomware group was reportedly the first major ransomware operation to adopt Rust in 2021. Earlier this year, the Hive ransomware operations rewrote its malware in Rust. Then in the second half of 2022, at least four ransomware operations - [**Agenda**](https://www.trendmicro.com/en_us/research/22/l/agenda-ransomware-uses-rust-to-target-more-vital-industries.html), [**RansomEXX**](https://securityintelligence.com/posts/ransomexx-upgrades-rust/), [**Luna**](https://securelist.com/luna-black-basta-ransomware/106950/) and [**Nokoyawa**](https://www.zscaler.com/blogs/security-research/nokoyawa-ransomware-rust-or-bust) \- joined the trend.

This programming language is becoming increasingly popular among developers for several reasons. First, Rust is a cross-platform language with a large selection of platforms supported. As a compiled language with a single compiler, it requires smaller adjustments to adapt the binaries to each of these platforms (to compare, C++ requires multiple compilers).

This feature is of great interest to malware developers, who normally seek to broaden their target audience with relatively little effort. From an attacker’s point of view, cross-platform programming languages allow customisation of attacks to different victim environments.

The rewriting of ransomware in a new programming language is highly likely indicative of a group’s evolving techniques to enhance the capabilities of its malware and to evade detection, as few security solutions are capable of analysing Rust for the time being. Once threat actors make this effort, we assess it is worth considering a possible growth of the related threat.

Sekoia expects Rust will become increasingly more appealing to malware developers, as it becomes increasingly popular. It is likely this will come with more documentation resources available in the future and better support, a bigger developer base, more freely available pieces of code _etc_.

## Stronger together. Ransomware actors and their dark web allies

As mentioned in Sekoia mid-2022 Ransomware Threat Landscape, ransomware groups are established players of the Dark Web ecosystem.

The ransomware ecosystem kept on professionalising in the second half of 2022 by further splitting tasks within their groups, and by cooperating with other threat actors.

Hereafter, we outline some of the Dark Web actors and service providers that partner with ransomware groups and are leveraged in ransomware operations.

### Who’s calling? Fraudulent call centres and other calling services

As seen previously in the callback phishing part, **fraudulent call centres** were originally seen leveraged in scam and fraud business schemes. Their offerings evolved the last two years, mirroring the evolving cybercriminal threat landscape, and are now used by more advanced threat actors.

By mid-2022 when the callback phishing campaigns regained popularity, Sekoia analysts observed fraudulent call centre offers flourishing on the Dark Web.

We assess it is almost certain that most fraudulent call centres work closely with ransomware groups. This most likely includes callback phishing campaigns to gain initial access, malware distribution campaigns and negotiations with ransomware victims.

![A threat actor looking for an affiliate to call corporations and distribute allegedly malicious emails](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a64ee9a71d4228410cc3_6a92a430693fca262e1bf5cb_6a2a7a0d9d93c6b6fdb02826.webp)

A threat actor looking for an affiliate to call corporations and distribute allegedly malicious emails

Although the use of call centres by ransomware groups is not new to the threat landscape, Sekoia analysts observed **call services specifically aimed at businesses** being advertised on the Dark Web starting from March 2022. This time frame matches the resurgence of the callback phishing technique as documented in open sources. We found that both their number and their activity level increased since mid-2022.

One such example is CorpCalls (previously ApprovedCalls) - an outsourcing call centre launched in mid-May 2022 on a cybercrime forum and actively promoted throughout Q2 2022. In their multiple messages on the forum, threat actors claim “greatly improving payments of corporations”. They also claim “many successful cases, working with serious partners and making the best calls”. It is highly likely this call service is leveraged by ransomware actors to pressure victims to pay ransom after a successful attack.

![A threat actor looking for an affiliate to call corporations and distribute allegedly malicious emails](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a64ee9a71d4228410cbd_6a92a432c5553634ac948f60_6a2a7a0e9d93c6b6fdb0282e.webp)

A threat actor looking for an affiliate to call corporations and distribute allegedly malicious emails

To be competitive, such services tend to cover as many clients’ needs as possible, sometimes not to charge for missed or failed calls, to operate 24/7 to cover all time zones, to hire operators speaking more languages, _etc_. Of note, Sekoia analysts are aware of female operators being in the minority, so they are particularly needed in these call centres and valued in the forum advertisements, likely in an attempt to appear more legitimate.

### Ransomware-as-a-Service affiliate programs

Public RaaS operations continued to recruit partners throughout the Q2 2022. However, there is evidence that ransomware group's activity on cybercriminal forums is more decentralised and more segmented than it used to be.

The latest RaaS to be launched are barely recruiting on Dark Web forums the way other ransomware gangs used to do - which was to clearly display the affiliate program name, to build a strong corporate identity and to have one representative explicitly advertising and recruiting for the whole group. In contrast, to bypass restrictions on advertising ransomware on certain cybercrime forums, threat actors now implicitly look for affiliates through **covert announcements**. Then from Sekoia observations, the discussions are mostly carried out via private messages.

### Ransomware and Initial Access Brokers (IABs) as intrusion facilitators

IABs are definitely a key element of the RaaS supply chain. By providing ransomware groups with initial access points into corporate networks, IABs facilitate the task of a ransomware operator and shorten the attack cycle time. BlackCat, Everest, LockBit, AvosLocker, RTM Team, SolidBit are **known ransomware groups using the services of the IABs**.

In 2022 we observed a continuous growth of this threat, alongside a few evolutions in the IABs modus operandi. We noticed an increasing number of IABs who are no longer acting as independent actors (individuals), but instead are forming **well-organised syndicates**. This is likely indicative of a quite advanced maturity level reached within the fraudulent initial access market.

Also, there is a new distribution rate seen between the offer and the demand on the market. While originally the IABs landscape was mostly composed of access sellers, today we also see an **increasingly structured demand for accesses**. This is reflected in the rise of threat actors (mostly organised in groups) who focus on buying initial accesses in bulk on a regular basis. It is likely most of them are RaaS affiliates or cooperate with ransomware operators.

One such example is the “buy-corps” threat actor. It operates on underground forums as an access buyer interested in high-profile companies from Canada and the United States of America, except education and healthcare sectors. It declares owning a “private soft” and is particularly interested in Domain Admin accesses. It is highly likely this threat actor refers to a private ransomware program. After analysing its activities on the forum, Sekoia assess with medium confidence it is a ransomware operator running Big Game Hunting campaigns.

!["Buy-corps" threat actor looking for specific initial accesses](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a64ee9a71d4228410cc0_6a92a431a2f46752fd022688_6a2a7a0d9d93c6b6fdb0282a.webp)

&quot;Buy-corps&quot; threat actor looking for specific initial accesses

## Conclusion

The evolutions Sekoia analysts observed within the ransomware landscape in the last six months reveal a higher level of professionalisation of ransomware groups. They typically tend to broaden their scope and to be highly profitable while reducing the time needed to perform an attack.

From our observations, a growing number of existing ransomware groups switched to the Big Game Hunting league in the second half of 2022. This is mainly reflected by existing ransomware groups adopting the double extortion technique and the set up of Data Leak Sites since mid-2022. Such examples monitored by Sekoia analysts are MedusaLocker, Mallox, Trigona and Nokoyawa ransomware.

It is likely that ransomware groups will increasingly use double or triple extortion schemes to put more pressure on victims and to improve the chances of getting paid.

We observe that data encryption is no longer the ultimate argument leveraged by ransomware groups to pressure victims to pay ransom. Data exfiltration and data leakage is increasingly used as (sometimes the only) extortion technique after an intrusion. This leads to the issue of the evolving pattern of extortion techniques leveraged by threat groups - particularly groups claiming to conduct supposedly ransomware attacks while they are actually not encrypting data - and how this can impact on naming conventions and the way we define threats.