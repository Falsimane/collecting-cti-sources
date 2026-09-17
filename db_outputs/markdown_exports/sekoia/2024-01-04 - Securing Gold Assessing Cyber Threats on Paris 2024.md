# Securing Gold: Assessing Cyber Threats on Paris 2024

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/securing-gold-assessing-cyber-threats-on-paris-2024
- **Date :** 2024-01-04

---

## Introduction

The next Olympic Games hosted in Paris will take place from **26 July to 11 August 2024** , while the Paralympic Games will be carried out from **28 August to 8 September 2024**. The Olympic and Paralympic Games, which bring together all the nations around sport competitions **every two years,** is a showcase for States in front of the world. The hosting country is in the spotlight for **almost two months** , its image being at stake depending on the success or the good proceedings of the event, including **on the cyber front.**

Despite the willingness to make this event a peaceful moment during which States put aside their geopolitical tensions and observe **the Olympic Truce** , it remains a **place of strategic confrontation.** Indeed, geopolitical hostilities are often manifested through **hybrid means** , including cyberspace operations, to ensure **ambiguity and harden attribution**.

In addition, the Olympics remain a popular event and **one of the most watched events worldwide.** Paris 2024 estimated the number of spectators for the next edition to be **9,7 million on 40 Olympics sites.** To welcome this number of people and to provide a reliable infrastructure, the Olympics set up numerous services specifically for the occasion, like **ticketing, betting, or travelling**. All of which **extend the attack surface** related to the Games. The attractivity of the Olympics is highly likely to be leveraged by **opportunistic cybercrime operators** who will try to take advantage of the appeal of the public to lure their victims and **steal data or money** from them. 

Based on these observations and given the **constantly evolving cyber threat landscape** , we analysed cyber threats affecting previous editions of the Olympics, as well as the current geopolitical context to understand potential motivations of malicious actors to target this event, **ranging from destabilisation to financial gain** , and the techniques they leverage. In a **prospective approach** , we analysed the different cyber operations likely to impact the 2024 Olympics depending on the objective of malicious groups. 

This report details our findings based on open-source research. It intends to be complementary to the ANSSI [report](https://www.cert.ssi.gouv.fr/cti/CERTFR-2023-CTI-005/) on the cyber threats affecting major sport events, which provided guidelines for our analysis.

## Executive summary

  * Past Olympics Games have been targeted by offensive cyber operations since at least Beijing 2008, for intelligence gathering, destabilisation purposes, political claims or lucrative operations. Sekoia.io has conducted an **inventory** of all open-source **reported cyber operations** , including Olympic Destroyer, a sabotage operation aimed to disrupt the opening ceremony of PyeongChang 2018 Winter Olympics in South Korea.


  * The **current geopolitical context** is likely to have an impact on Paris 2024, as Olympic Games were already targeted in the past by state-nexus cyber operations over geopolitical conflicts. Nationalist hacktivist groups, as widely seen active for instance in the Russia-Ukraine war, are as well a possible threat.


  * Paris 2024 can be impacted by multiple types of malicious cyber operations, from **destabilisation-driven campaigns** leveraging hack-n-leak, destructive malware and influence operations, to **disruption-driven campaigns** (DDoS, defacement) impacting the host reputation by interrupting service disponibility for a period of time. More covert operations, such as **espionage campaigns** , can also be leveraged by state-sponsored threat groups in order to defend strategic interests.


  * **Cybercrime** -related operations are a **persistent threat** to the Olympics. Such operations are often opportunistic, leveraging the event’s popularity, to target various victims, from the public to partners and organisers of the event. Lucrative campaigns luring spectators are likely to leverage Olympics-related phishing themes, malicious apps, fake typosquatted websites mimicking reselling, ticketing or betting platforms.



## History of cyber operations impacting Olympic Games

To truly assess the potential cyber threats faced by the Paris 2024 Olympics, it's crucial to examine cyber campaigns that targeted previous Olympic events, from the first reported operations impacting Beijing 2008 to the last Winter 2022 Olympics, in Beijing again. It is worth noting that such assessment presents limits, as it is based on open-source reporting. 

State-sponsored operations, in particular, are often kept secret by government services, meaning we might, for instance, not be aware of any major destructive attempts on previous Olympics. Another bias is open-source reporting which mostly originates from Western-based research entities, underlining cyber offensive operations from Western competitors actors.

### The Olympics: a timeline of cyber operations

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a6b369dfca546ea2c6a259a_blog-olympic-games-cyber-operations-timline.webp)

Figure 1. The Olympics: a timeline of cyber operations. Source: Sekoia.io Threat Detection & Research

‍ _‍_

####  _Beijing 2008_

Beijing 2008 was the first Olympic Games during which malicious cyber operations were publicly reported. Also, even if it is not clear if the Games were the final objective, a cyber **espionage** campaign “Operation Shady Rat” was reported by [McAfee](https://icscsi.org/library/Documents/Cyber_Events/McAfee%20-%20Operation%20Shady%20RAT.pdf) targeting notably the International Olympic Committee (IOC) for a month in October 2007, as well as multiple Western and Asian Olympic Committees during the year prior to Beijing 2008. This long-lasting campaign - estimated 2006-2011 - also targeted the World Anti-Doping Agency (WADA) in August 2009 for 14 months. This operation was later [associated](https://www.washingtonpost.com/national/national-security/report-identifies-widespread-cyber-spying/2011/07/29/gIQAoTUmqI_story.html) with China, likely aiming at information gathering. 

The event was also impacted by **hacktivists** \- individuals or groups leveraging cyber operations for political or social activism purposes. Indeed, website [defacement campaigns were reported](https://www.smh.com.au/world/protesters-hack-into-olympics-website-20080807-3rjm.html), notably impacting the Chinese Olympic Games’ whose titles were coloured in orange by international human rights activists in order to protest against human rights violations in China. It had no major operational or physical impact, but reputational. **Lucrative** malicious [operations](https://www.networkworld.com/article/904360/security-the-olympic-games-were-hacked.html) such as fraudulent ticket websites, spear phishing and deceptive streaming platforms were also reported and attributed to opportunist intrusion sets, leveraging the major economic opportunity of the Games.

#### _London 2012_

Based on open source reporting, London 2012 **did not experience any significant cyber operation**. Yet, a 40-minute Distributed Denial-of-service**(DDoS) attack** shaked the Olympic Park’s power systems on the second day of the Olympics. Hacktivist groups called to more DDoS attacks, coordinating their efforts via the X (formerly Twitter) hashtag . According to Rand Corporation, these operations had [no major impact](https://www.rand.org/content/dam/rand/pubs/research_reports/RR2300/RR2395/RAND_RR2395.pdf) thanks to efficient cybersecurity measures. 

**Lucrative** malicious operations conducted by opportunistic actorsimpacted the public with phishing campaigns luring people over a chance to win free airline tickets for the London Summer Olympic Games by filling in their personal data on a fake survey. [GFI](https://www.siliconrepublic.com/enterprise/cyber-criminals-take-on-mobile-phone-users-with-london-2012-olympics-scams-report) Software analysts also reported that Russia-based cybercrime operations tried to lure individuals by spoofing the London 2012 official mobile game application.

#### _Sochi 2014_

Shortly after the Winter Olympics held in Russia, a **cyber espionage**[**campaign**](https://www.themoscowtimes.com/2014/02/06/fsb-makes-eavesdropping-an-olympic-event-a31823)was reported in open source, accusing Russian Intelligence services of gathering information on Olympics organisations, judges, journalists, spectators and athletes.

**Hacktivist groups** were [reported](https://www.cnbc.com/2014/02/07/sochi-security-warning-of-cyber-attacks-as-hackers-target-olympics.html) conducting website defacement operations and DDoS attacks for political revendications. The campaigns aimed to affirm the historical belonging of the Sochi region to the Caucasus while condemning the 19th-century deportation of numerous Circassian natives from the area by the Russian Empire. The DDoS attacks impacted websites of the Sochi airport, the sponsors such as Sberbank, the Russian Olympic Committee, as they were unavailable for several hours. Defacement campaigns impacted 700+ websites that displayed the following message: “We warned you Russia”.

#### _Rio 2016_

Rio Olympics were impacted by an advanced **cyberespionage campaign** led by APT28, an intrusion set linked to the Russian military intelligence (GRU), as [reported](https://www.theguardian.com/sport/2016/sep/13/wada-russian-cyber-attack-espionage-group) by the World Anti-Doping Agency (WADA) two months after Rio 2016. Confidential medical data and test results of 41 athletes were exfiltrated from WADA. Sekoia.io assess, like other cybersecurity editors, that the operation is **highly likely correlated** to the ban of Russian athletes from participating in the Rio Olympics after WADA accusation of a state-organised doping system during Sochi 2014.

The event was also impacted by **hacktivist groups** such as _Anonymous Brazil_ in [campaigns](https://www.silicon.co.uk/security/rio-olympics-ddos-attacks-196998) targeting the Brazilian Federal government and the Ministry of Sports, leading to the leak of personal and financial data. Anonymous Brazil protested against the Games pointing to a lack of investments in favelas and excessive investment in Rio2016. **Cybercrime operations** were also reported, targeting the public and organisations affiliated with the Rio Olympics. Fortinet analysts reported a 83% increase in phishing URLs in Brazil before the Olympics compared to a 13% increase for the rest of the world.

#### _Pyeongchang 2018_

The 2018 Winter Olympics in South Korea were the first Games that reported being targeted by a large-scale **destructive cyber operation - Olympic Destroyer** , impacting multiple systems during the opening ceremony (see the focus section below). The event was also impacted by **lucrative cyber operations** as already seen on anterior games.

##### **Focus on Olympic Destroyer (PyeongChang 2018 Winter Olympics)**

In February 2018, the Winter Olympics in Pyeongchang, in South Korea, were impacted by a large-scale cyber attack during its **opening ceremony**. The operation caused disruptions across [various systems](https://www.theguardian.com/sport/2018/feb/10/winter-olympics-investigating-if-technical-problems-were-cyber-attack), including televised feeds within the Olympic Stadium, RFID-based security gatessystems and the official Olympics app for digital ticketing. Despite the rapid restoration of essential services, some information systems required a complete rebuild after the attack. Dubbed “Olympic Destroyer” by [Talos](https://blog.talosintelligence.com/olympic-destroyer/) CTI research team, the **destructive malware** presented worm-specific automatic replication capabilities and presented technical **similarities with BadRabbit and NotPetya destructive malware** , both leveraged by intrusion sets attributed to the Russian military intelligence service GRU. The malware was designed to conduct sabotage on information systems by deleting backup files, event logs, and attempting to lateralise across networks using specific tools like PsExec & WMI.

Of note, **intentional false flags** initially pointed to the North Korean intrusion set Lazarus, a group previously known for its extensive history of targeting South Korea. This deliberate misdirection served a **dual purpose** of diverting attention away from the true perpetrators while fortifying the narrative of North Korean involvement due to historical tensions between the two nations. Further technical investigations by [cybersecurity vendors](https://web.archive.org/web/20190131032535/https:/securelist.com/olympicdestroyer-is-here-to-trick-the-industry/84295/) and government agencies finally led to the **attribution to Sandworm** (aka Hades, BlackEnergy), an intrusion set operated by **Russian military intelligence’ (GRU)** Main Center for Special Technologies, unit 74455. Six GRU officers were later [indicted](https://www.justice.gov/opa/pr/six-russian-gru-officers-charged-connection-worldwide-deployment-destructive-malware-and) by the US Department of Justice over disruptive actions, including campaigns targeting the 2018 Games.

Sekoia.io assesses that Sandworm likely conducted the operation **as part of Moscow’s retaliatory measures** after the International Olympic Committee (IOC) [banned](https://www.nytimes.com/2017/12/05/sports/olympics/ioc-russia-winter-olympics.html) the Russian Olympic Committee from the 2018 and 2020 Olympics over **state-sponsored doping in Sochi 2014**. 

Given the fact Russia is still banned from Paris 2024, such operation is **likely to be conducted again** , especially by GRU-operated intrusion sets such as Sandworm, but also APT28 or Ember Bear. 

#### _Tokyo 2020_

The 2020 Tokyo Olympics, which were postponed and took place in 2021 due to the Covid-19 pandemic, did not welcome any spectators. One year before the Games, British cyberdefense agency [NCSC](https://www.ncsc.gov.uk/news/uk-and-partners-condemn-gru-cyber-attacks-against-olympic-an-paralympic-games) reported on an **espionage campaign** targeting officials and organisations involved in the Tokyo Olympics that was attributed to Sandworm (Russian Intelligence GRU). Tokyo 2020 events faced **attempted destructive cyber attacks** , still not attributed today, deploying [wipers](https://therecord.media/wiper-malware-targeting-japanese-pcs-discovered-ahead-of-tokyo-olympics-opening) configured to target only Japanese-set computers and erase specific files. Based on open-source reporting, the operation failed due to the discovery of the malware two days before the Games. 

**Lucrative cyber operations** led by opportunistic malicious actors targeted the public and organisations linked to the Games through phishing campaigns, also leveraging [credential](https://www.zdnet.fr/actualites/450-millions-de-tentatives-de-cyberattaques-pendant-les-jeux-olympiques-de-tokyo-39931213.htm) theft technique and fake [broadcasting](https://www.trendmicro.com/fr_fr/research/21/h/tokyo-olympics-leveraged-in-cybercrime-attack.html) websites.

#### _Beijing 2022_

Based on open-source reporting, Beijing 2022 **did not experience any significant cyber operation** , although a probable cyber surveillance operation was reported by [Citizen Lab](https://citizenlab.ca/2022/01/cross-country-exposure-analysis-my2022-olympics-app/) before the Games. The researchers highlighted vulnerabilities in the **Chinese application My2022** that all attendees had to set up on their mobile devices during the Olympics. If exploited, these vulnerabilities could allow access to personal and medical data. Like every past Olympic Games since 2008, opportunist **lucrative** cyber operations were reported, such as phishing campaigns.

### Decoding the trends across previous Olympic editions

Based on previously reported cyber operations impacting past Olympics, distinct trends have emerged, providing foresight into potential threats to the upcoming Paris 2024 Olympics.

  * **Lucrative operations** conducted by cybercrime-related actors represent the **most frequent** and recursive cyber operations observed during the Olympics. Such operations leverage the Olympics subject to conduct campaigns such as phishing attacks, fraud schemes such as fake ticketing or online betting solutions. We assess most of these intrusion sets are relatively low advanced, so **they do not represent a major operational threat** to the organisers’ information systems themselves.


  * Olympics events are often **targeted bystate-sponsored** cyber operations**, both** to **collect intelligence** and to **conduct sabotage** aiming to disrupt the event. These operations, requiring months of preparation, are typically related to geopolitical tension implying host and participating countries.


  * **Hacktivism campaigns, namely** the use of cyber operation for political or social activism purposes**,** pose an increasing threat, the Olympics being leveraged as a tribune for political claims.


  * The **opening ceremony** is **commonly targeted** by cyber operations, as it is the most viewed event in every edition.



## Olympics cyber threats related to geopolitics

The 2024 Olympic Games in Paris will occur in a **particular geopolitical context** characterised by **several open conflicts,** ongoing as of December 2023, which oppose countries participating in the event. The Russia-Ukraine conflict led to the first ever [decision of the International Olympic Committee](https://olympics.com/ioc/media/q-a-on-solidarity-with-ukraine-sanctions-against-russia-and-belarus-and-the-status-of-athletes-from-these-countries) (IOC) to **ban countries from participating in the competition** for failing to respect the territorial integrity of other participants. Geopolitical tensions are likely to be translated into the cyber space and to impact the cyber threat landscape amid this global sport event.

### Current geopolitical tensions and their implications for Paris 2024

#### Russia-Ukraine conflict

#####  _Russia and Belarus ban from Paris 2024_

Between 2018 and 2022, Russia was banned from competing in the Olympics under its flag due to the [state-sponsored ](https://www.lemonde.fr/sport/article/2020/12/17/dopage-la-russie-exclue-des-deux-prochains-jeux-olympiques_6063754_3242.html)**doping system** of Russian athletes in Sochi 2014. The decision made by the IOC and the World Anti-Doping Agency (WADA) in 2014 echoes **Paris 2024 ban** of Russia and Belarus for the 2022 invasion of Ukraine. Accordingly, the Russian Olympic Committee was suspended because it placed [under its authority](https://www.france24.com/en/live-news/20231205-sports-bodies-ask-ioc-to-allow-russians-as-neutrals-for-2024-olympics) several sport organisations from four occupied Ukrainian regions. Russia and Belarus athletes are however [allowed](https://olympics.com/ioc/news/strict-eligibility-conditions-in-place-as-ioc-eb-approves-individual-neutral-athletes-ains-for-the-olympic-games-paris-2024) by the IOC to compete as a “Neutral Individual Athlete”.

##### _Retaliation over France supporting Ukraine_

As France amid NATO and Western states is supporting Ukraine in its defensive war against Russia, it is **possible** that the 2024 Paris Olympicswill be targeted by Russian and/or Belarus cyber operations as a **retaliation measure -** such as disruption and sabotage - to **undermine the reputation of France**. In a previous blogpost, Sekoia.io assessed the cyber implications of the Russo-Ukrainian war one year after the beginning of the conflict, exposing multiple Russia-nexus intrusion sets leveraging worms and wipers, malware that could be used against French interests.

**Russian hacktivists groups** are also likely to target the Paris Olympics with DDoS attacks, websites defacements or hack-and-leaks as a contribution to the Russian effort to undermine France.

#### Israël - Hamas conflict

The ongoing war between Hamas and Israel after the 7 October 2023 attack might have repercussions on the Paris Olympics. If the conflict is still ongoing in July and August 2024, and **if the French diplomatic posture is perceived by Palestine-supporters as pro-Israel** , it might induce hacktivist cyber disruptive operations looking for political claim. 

In addition, states and political entities supporting Palestine, such as **Iran** , Yemen, **Hezbollah militia** or the Hamas itself, can potentially use their cyber offensive capabilities to impact the Olympics. For more information about their capacities, Sekoia.io reported on AridViper, an intrusion set likely operated by Hamas operatives, and on Iran cyber offensive capabilities.

#### Azerbaïdjan - Armenia conflict

The 2023 war and ongoing tensions between Azerbaijan and Armenia might as well impact the Paris Olympics. After the capitulation of Armenia and the annexation of the Artsakh region in September 2023, France renewed its support to Armenia, including [military cooperation](https://www.defense.gouv.fr/actualites/france-renforce-sa-relation-defense-larmenie), a position highly criticised by Azerbaijan. As Bakou destabilisation operations were already [reported](https://www.lemonde.fr/international/article/2023/11/14/des-acteurs-proches-de-l-azerbaidjan-derriere-une-campagne-de-boycott-des-jo-de-paris_6200083_3210.html), it is possible that the Paris Olympics might be targeted by malicious cyber or influence operations.

#### Inner French political context

As seen during the Rio 2016 Olympics, media attention can be leveraged by domestic hacktivist groups for political, social or ecological activism. However, as the French government communicated about working on making the Games sustainable and inclusive, it lowers the probability of domestic cyber threat.

### Potential destabilisation-driven cyber operations

As observed during previous Olympics editions, the geopolitical context has a confirmed impact on the cyber threat landscape which takes advantage of this major event to conduct operations, often going beyond sportive issues. 

Due to the heightened visibility and high-level profiles attending the Olympics, the cost-benefit trade-off of cyberattacks has shifted, making destabilisation operations more profitable in terms of impact. Disruption operations can target essential services and key players through sabotage, denial of services, or cyberespionage on critical targets, but also aim at shaping public opinion with influence operations.

#### **_Sabotage and destructive cyber operations_**

A sabotage or destructive cyber operation consists of the destruction of hardware or information systems, possibly leading to a loss of data in the absence of back-ups, the information system unavailability for an indefinite period, and implying repair or replacement costs. To conduct such operations, threat actors often use **wiper malware** to erase critical data on infected systems. 

Wipers are a type of malware dating back to at least 2012, with the reporting of the infamous Shamoon. **Their use has become more frequent through 2022 and 2023** , especially since the beginning of the war in Ukraine. Russian state-sponsored intrusion sets deployed at least **six different wipers** \- mostly attributed to Sandworm - during the six first months of the invasion to contribute to Russian efforts to destabilise the Ukrainian state and to weaken the capacity of response of Ukrainian forces. 

Given the political situation between Paris and Moscow, Sekoia.io assess it is**possible** that **Russia-nexus intrusion sets will try to conduct destructive operations on Olympics-related information systems** , as a retaliation against France's support to Ukraine. 

If a Russian destructive operation is planned, it will **likely be conducted** by **GRU-operated** intrusion sets, notably **Sandworm and APT28** known for their past sabotage operations. Xenotime (aka Triton) and Ember Bear, as well as FSB-operated DragonFly 2.0, may possibly use wiper malware as well, although these intrusion sets are less likely to conduct large scale destructive operations.

Of note, Sandworm was also observed leveraging **pseudo-ransomware used as wipers** to conduct destructive operations, as the ransomware data encryption process can be diverted from its intended purpose by deleting the decryption key, thus making the data permanently inaccessible. Prestige ransomware was, for instance, employed by Sandworm in campaigns against Ukraine and Poland and illustrates a **scheme of plausible deniability** behind the false-flag of cybercrime-related operations.

Russia put aside, the number of **intrusion sets able to develop** and operate wipers is also **increasing**. In the context of the Israel/Hamas war, a pro-Hamas intrusion set was observed using the [BiBi wiper](https://blogs.blackberry.com/en/2023/11/bibi-wiper-used-in-the-israel-hamas-war-now-runs-on-windows) to target Israeli critical infrastructure on [Linux ](https://blogs.blackberry.com/en/2023/11/bibi-wiper-used-in-the-israel-hamas-war-now-runs-on-windows)and [Windows ](https://www.linkedin.com/pulse/bibi-wiper-gaza-war-now-goes-windows-dmitry-bestuzhev-yftze%3FtrackingId=rRIvxyD4Ty2qqqBACwM6dg%253D%253D/?trackingId=rRIvxyD4Ty2qqqBACwM6dg%3D%3D)in October 2023. Such capacity could be used against Olympics-related information system as a retaliation to a perceived pro-Israel French position. 

The availability of ransomware-as-a-service (RaaS) on cybercrime forums and the leak of ransomware’s source code, such as Conti, can also be used for destructive sabotage operations.

![Figure 2. Wiper timeline: a history of sabotage operations \(click to enlarge\) ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5ec4538ee1e1c2e7062_6a92a327e36224e46e90d133_6a2a7c92009bb67f3ecf19f1.webp)

Figure 2. Wiper timeline: a history of sabotage operations (click to enlarge) 

#### **_Nationalist hacktivist groups looking for disruption and media attention_**

**Hacktivist groups** , which are non-state actors, may take advantage of the media coverage of the Olympics to promote propaganda narrative.

This threat is specifically relevant for the last two years as Sekoia.io, in line with other cyber security vendors, observed a **rise of malicious activities from nationalist hacktivist groups** starting from 2022, in the context of the Russia-Ukraine war. Their operations consist of mostly**DDoS and defacement attacks** , almost always accompanied by a highly active communication about the attacks to relay political messages.

Despite their**relatively low level of sophistication and their short-term impacts** , DDoS attacks can affect the **reputation** of the targeted organisation or country. For instance, several hours after the beginning of confrontations between Israel and the Hamas, pro-Palestinian hacktivists reacted: the [group **AnonGhost** disrupted for several hours the Israeli RedAlert system](https://cybernews.com/cyber-war/israel-redalert-breached-anonghost-hamas/), used for real-time warning of strikes. In addition to the immediate impact on the communication to citizens, this likely spreads doubts among the population about the capacity of their country to ensure their security.

In the case of the Olympics, such attacks could be used to **discredit Franceand its capacity to ensure security on its own territory**. This strategy was already used by pro-Russia hacktivists, such as [**NoName057**](/blog/following-noname05716-ddosia-projects-targets), who launched massive DDoS campaigns against NATO countries to shake the trust of the population in the capacity of their governments to protect them against a potential invasion. (cf. Figure X). This technique was notably leveraged by the **DDoSia project** , a DDoS toolkit created in 2022 and which was documented by Sekoia.io analysts.

![Figure 3. Screenshot of NoName057\(16\) English Telegram Channel ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5ec4538ee1e1c2e7066_6a92a328dc30711238327058_6a2a7c92009bb67f3ecf1a35.webp)

Figure 3. Screenshot of NoName057(16) English Telegram Channel 

‍

####  _Threat related to botnets_

In April 2022, the [US Department of Justice ](https://www.justice.gov/opa/pr/justice-department-announces-court-authorized-disruption-botnet-controlled-russian-federation)(DoJ) dismantled a botnet attributed to the GRU and relying on vulnerable internet-connected firewall devices on WatchGuard and Asus network with Cycloc Blinks malware. In June 2022, another Russia-nexus botnet, called RSOCKS, [was disabled](https://www.justice.gov/usao-sdca/pr/russian-botnet-disrupted-international-cyber-operation) according to the US DoJ. It functioned as a proxy service to compromise internet-connected devices. However, rather than providing customers with IP addresses legitimately leased from internet service providers (ISPs), it offered IP addresses that had been assigned to compromised devices.  
Such botnets could be used to specifically target entities involved in the Olympics for destabilisation purposes. 

Even if most documented DDoS operations have been conducted against websites, they can also affect **APIs of mobile apps**. In the context of Paris 2024, apps dedicated to ticketing or transport could therefore be a target for destabilisation. 

This threat can be **amplified** by the **cooperation between several hacktivist groups**. Indeed, in June 2023, the **Turkey Cyber Army** already claimed its solidarity with **Killnet** , which targeted France for its support to Ukraine several times since its creation in March 2022.

Hacktivism can also be involved in **hybrid strategies** of destabilisation. On 17 January 2023, CERT-UA investigated a Sandworm destructive operation impacting Ukrinform, the National News Agency of Ukraine, using two wipers among other tools: CaddyWiper and ZeroWipe. The operation occurred in December 2022 and January 2023. Shortly after the compromise, [Mandiant](https://www.mandiant.com/resources/blog/gru-rise-telegram-minions) reported that CyberArmyofRussia_Reborn, a Telegram channel operated by a Russian nationalist hacktivist group, published leaked data from the victim, suggesting that this hacktivist group is coordinating itself with Sandworm, or at least the GRU.

Due to its capacity to launch massive attack campaigns, hacktivism can also be used to **draw attention away from more sophisticated, state-sponsored operations**.

#### **_Information warfare and cyber influence operations_**

Influence operations can be defined as operations affecting the logical layer of cyberspace to shape attitudes, decisions and behaviours of a [targeted audience](https://ccdcoe.org/uploads/2018/10/Art-08-Influence-Cyber-Operations-The-Use-of-Cyberattacks-in-Support-of-Influence-Operations.pdf). Because of the Olympics' significant visibility and popularity, they can serve as a theme for campaigns that aim to either support political claims or discredit the host country.

Influence campaigns targeting France and the Olympics have already been identified. Le Parisien conducted an [investigation](https://www.leparisien.fr/video/video-munich-1-972-paris-2024-ces-tags-menacants-qui-nont-sans-doute-existe-que-sur-les-reseaux-sociaux-30-11-2023-UEUMHWJSJVFD3LJZ6PI7ZSGMFE.php) on tweets relaying **tags in Paris’ streets** making a**parallel between the Olympics of Munich 1972 and of Paris**. In 1972, Israeli athletes were taken hostage by Palestinian members of the September Noir organisation. Of them, eleven were assassinated to protest against the Israeli occupation on Palestinian territories. Le Parisien found out that **these tags never existed** and that **posts on social media** relaying the pictures of these tags can be **linked** to accounts known to be part of the**Russian propaganda**.

In May 2023, France was especially targeted by a Russian influence operation called [**Reliable Recent News** (RRN)](https://www.sgdsn.gouv.fr/publications/maj-19062023-rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et) running from September 2022. The identity of the French Ministry of Foreign Affairs was spoofed to share Russian propaganda and controversial topics. In July 2023, an operation linked to the Azerbadjanese company **Mediamark Digital Agency** also targeted France by sharing contents calling for the [boycott of the 2024 Paris Olympics](https://www.sgdsn.gouv.fr/publications/maj-19062023-rrn-une-campagne-numerique-de-manipulation-de-linformation-complexe-et).

Influence operations can also be used or amplified in the cyber sphere as part of a **hybrid offensive strategy.** For instance, in November 2023, NoName057 targeted French services of the transportation sector in retaliation to Paris' support to Ukraine, aiming at creating doubts in the public opinion about how the funds are used by Kiev. This refers to a narrative pushed by pro-Russian propaganda saying Ukraine used foreign donations to fund child abuse.

#### **_Individual espionage for intelligence purposes_**

During the Olympics, delegations with high-profile individuals, ranging from famous athletes, CEOs to diplomats and political personalities, will attend the event. They represent targets of choice for intelligence services looking for strategic information. As these individuals will be concentrated at the same place, it makes physical compromission of their devices easier for cyber espionage operations. Cyber espionage campaigns can also take advantage of the attention concentrated on most visible threats during the Olympics to remain under radar and compromise critical targets. Discrete by nature, this kind of operation is unlikely to immediately impact the course of the event, but can result in major consequences over the medium and long term.

In 2022 and 2023, Europe was particularly targeted by Chinese espionage campaigns relying on **USB-drive** and **third parties** to gain initial access to strategic networks. It was the case in 2022 when Mustang Panda compromised a Greek Ministry to infect the diplomatic network of the European Union used to carry out strategic information between member States.

Therefore, among state-sponsored intrusion sets likely to conduct individual espionage for intelligence purposes, Chinese APTs account for the most active threat, looking both for industrial and political critical information to support China’s strategic objectives.

## Cybercrime-related threats on Paris Olympics

The Olympic Games, as every major mediatic event, are typically leveraged by lucrative intrusion sets to maximise their profit. The scope of potential targets is wide, from organisers and partners to the competitors and the public attempting the games.

### Lucrative campaigns luring spectators

Lucrative threats such as phishing and typosquatting are most likely to leverage the Olympics topic in massive campaigns directed at individuals attending the Games or interested in it. Indeed, [Paris 2024](https://www.paris2024.org/en/the-olympic-games-paris-2024/) announced 9,7 million spectators, 10,500 athletes, and billions of television viewers worldwide. They represent a target of choice for cybercriminals, which operate by launching **massive campaigns of attack** to ensure great benefit. Expected themes used for lucrative campaigns related to the Olympics are **betting, ticketing and travel**. Such campaigns can rely on different techniques to **steal credentials or exfiltrate data to monetise it either by selling the stolen information or by extorting money** from victims.

#### **_Phishing targeting spectators_**

Phishing scams are largely used to extort money or steal data from individuals. This technique requires few resources while generating important financial gains when distributed massively. It notably leverages popular events, such as sport competitions, for a greater impact. During the 2018 Football World Cup, phishing incidents referencing tickets increased by 1000% during the four weeks of competition. 

These campaigns can also specifically target France. In 2023,[ Group-IB](https://www.group-ib.com/blog/cryptoslabs-investment-scams/) uncovered the CryptoLabs campaign directed against French-speaking users and impersonating brands (40 different ones) to steal money from its victims. Group-IB estimated losses related to this campaign at 480 million euros. The **callback phishing** is another technique used to lure victims, especially in targeted campaigns, and could be used against high-level profiles during the Olympics.

#### **_Malicious apps behaving as trojan_**

Trojanized apps mimicking legitimate ones that give access to media broadcasting of the competition, to the program of the Olympics, or to travel and transportation facilities, may be used by lucrative intrusion sets to lure their victims and deliver malicious payloads. In August 2023, [X ads for fake voice AI websites](https://twitter.com/Gi7w0rm/status/1727324182223151558) were identified as a vector to deliver the Lumma infostealer. Lumma was first seen in 2022 and is sold on Russian-speaking underground forums as a malware-as-a-service. It targets browsers to steal passwords, cookies, autofills and credit cards. It can also compromise desktop cryptocurrency wallets.

#### _F_** _ake websites relying on typosquatting_**

At the dawn of the 2024 Olympics, [SOCRadar](https://socradar.io/possible-cyber-threats-in-the-2024-olympics/) identified domain addresses mimicking Paris 2024 themed legitime ones and linked to a website looking like a travel agency. This website seems to be used to lure victims and extort money. As of late 2023, Olympic cyber security authorities already registered several domain addresses related to Paris 2024 as a proactive measure to prevent typosquatting, nevertheless it remains a major concern as fake websites are easy to create both in terms of human and financial resources.

#### _Reselling platforms_

Reselling platforms of tickets are largely used by cybercrime operators to lure fans and spectators to extort money during major events. For instance, during the 2023 Rugby World Cup, malicious Telegram channels reselling tickets for the event were identified. The organising committee explicitly warned about the risk of fraudulent sales of tickets for the event. This type of technique is certain to be used during the Olympics.

### Ransomware and extortion threats aimed at Olympics’ and partners’ infrastructure

In 2023, Sekoia.io analysts [observed](/blog/sekoia-io-mid-2023-ransomware-threat-landscape/) a significant increase in the activity of lucrative ransomware and extortion groups impacting organisations. Moreover, we noticed that the ransomware ecosystem continuously enhances its **professionalisation, expands the attack surface** and develops**custom tooling** , making the detection and protection against this type of attack more complex.

**Ransomware and extortion groups** are likely to increasingly leverage the Olympics in campaigns against **key partners and organisation** s. It is likely driven by the significant pressure on victims that are related to the event, as it allows attackers to make greater benefits.

This concurs with the view of Vincent Strubel, the general director of the French National Cybersecurity Agency (ANSSI), which characterised the Olympics as “[the sales'' for cybercriminals](https://www.leparisien.fr/high-tech/securite-informatique-pendant-les-jo-2024-ce-sera-la-periode-des-soldes-pour-la-cybercriminalite-22-11-2023-HALUTC7CPNHPTEU23WH3BEMSKU.php) due to the fact that the **cost of launching lucrative campaigns will be trivialised, given the expected profit** they can make by thriving on the pressure of the Olympics on essential partners.

Lucrative campaigns that will take advantage of the 2024 Olympics are likely to leverage the following techniques:

  * **_Simple Extortion Ransomware_**
    * Simple extortion ransomware are encrypting victims’ systems and asking for a ransom. Such attacks can disrupt the availability of a service and its delivery for as long as the victim refuses to pay the ransom. It is facilitated by the growing market of ransomware-as-a-service and the [democratisation of the ransomware threat](/blog/sekoia-io-ransomware-threat-landscape-second-half-2022/) observed by Sekoia.io analysts since 2022.


  * **_Double Extortion Ransomware_**
    * In addition to encrypting the victim’s systems, operators conducting double extortion proceed to **data exfiltration,** which involves unauthorised access to sensitive information with the intent to steal or exploit it for malicious purposes. Indeed, once exfiltrated, data can be used by ransomware operators to negotiate the ransom with the victim or to make additional gains by selling them on illegal platforms.
    * Double extortion ransomware has been massively adopted since mid-2022 with the establishment of data leak websites by prolific ransomware groups such as Lockbit, Mallox, MedusaLocker or Trigona. This trend continues in 2023 with the active use of custom exfiltration tools. In the second quarter of 2023, [ReliaQuest ](https://www.reliaquest.com/blog/ransomware-q2-2023-victim-count-hits-new-heights/)documented 1,378 victims reported on ransomware data-leak websites, signifying a 64.4% surge from the previous record set in [Q1 2023 ](https://www.reliaquest.com/blog/2023-ransomware-attacks-q1/)with 838 organisations. Comparable evolutions were noted by [Orange Cyberdefense](https://www.orangecyberdefense.com/global/white-papers/cy-xplorer-2023), [Talos](https://blog.talosintelligence.com/talos-ir-q2-2023-quarterly-recap/), and [Dragos](https://www.dragos.com/blog/dragos-industrial-ransomware-attack-analysis-q2-2023/). 
    * As an example, three months ahead of the 2023 World Rugby Cup, the French Rugby Federation was targeted by [Play ransomware](https://www.numerama.com/cyberguerre/1424330-la-federation-francaise-de-rugby-piratee-les-hackers-auraient-derobe-des-donnees-confidentielles.html), leading to the encryption of part of its systems and data theft including personal information. It did not have a visible impact on the course of the event but it affected financially and reputationally the Federation.


  * **_RansomDDoS_**
    * A RansomDDoS (RDDoS) attack, or DDoS extortion, occurs when cybercrime groups threaten a targeted entity to conduct an impactful Distributed Denial-of-service attack unless a ransom is paid. Given the criticality of potential disrupted service during the Olympics, especially during the opening ceremony, RansomDDoS is a technique that can impact Paris 2024.



## Conclusion

The Olympics **bring a spotlight on the host country** and its sportive agenda, but also on the related economic ecosystems. On the cyber front, previous Olympics editions highlighted the **recurrence of cyber threat** s affecting this major sporting event. **Lucrative operations remain the most frequently observed** , while **sabotage and espionage campaigns are more persistent** , conducted notably by state-sponsored intrusion sets willing to defend geopolitical claims. 

Hosting more than 200 delegations, Paris 2024 will likely be a target of choice for**state-sponsored threat actors** , willing to **attempt at France’s reputation or to collect strategic information**. Looking forward to summer 2024, the geopolitical context is likely to be marked by tensions opposing countries taking part in the Games. Confrontations between Russia and Ukraine, Israel and Hamas, are likely to be still ongoing, while frozen confrontations, such as territorial tensions between Azerbaijan and Armenia, will remain. These hostilities are likely to spill over the Olympics, and to be replicated in cyberspace.

The **increased use of wipers** and the**rise of nationalist hacktivism** since 2022 have been identified by Sekoia.io analysts as major threats that could be used against the Games. More insidious operations likely to occur are **influence campaigns or espionage** , which are likely to generate less immediate consequences, but instead to cause major damages to the interests of the host country in the long term. **Influence operations targeting France and Paris 2024 have already been reported.**

In addition, **cybercrime operators** will leverage the Games **opportunistically** as a theme for lucrative campaigns. According to previous Olympics editions, **cybercrime-related threats differ depending on the targets** , ranging from the public to Olympic’ infrastructure, but remain a persistent threat affecting the Games. In the backdrop of **escalating ransomware activity in 2023 and the ongoing professionalisation** of the cybercrime ecosystem, Sekoia.io analysts especially identified simple and double extortion ransomware, along with ransomDDoS, as the predominant operations likely to be employed for financial gain against Olympics’ and partners’ infrastructure.

To conclude, previous editions of the Olympic and Paralympic Games pointed out the recurrence of cyber operations for different motives. Paris 2024 will not be an exception, which is why anticipating potential threats is necessary. Sekoia.io analysts assess another major issue remains the important number of actors involved, ranging from the public, to partners and third parties of larger entities, which multiplies the entry points for malicious operations.