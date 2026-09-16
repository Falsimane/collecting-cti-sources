# Invasion of Ukraine – what implications in cyberspace ?

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/invasion-of-ukraine-what-implications-in-cyberspace
- **Date :** 2022-02-24

---

_A first version of this blogpost was released as a FLINT (Flash Intelligence Report) by Sekoia Threat & Detection Research Team on February 16, 2022. This is an updated version, in light of the latest developments related to the invasion of Ukraine by Russia._

## Summary

For several months, there has been an increasing concentration of Russian troops close to its border with Ukraine, but also on the Belarus border with Ukraine. Military exercises were also conducted by overseas military task forces of the Russian Armed Forces in Transnistria, which is an unrecognised breakaway state on the Moldova-Ukraine border. By December, more than one hundred thousand troops were in place near the border. 110 Russian battalion tactical groups and over 150,000 soldiers were in place around Ukraine by mid-February, according to western officials.

In December 2021, Russia issued a set of demands which included a ban on Ukraine entering NATO. The U.S. and other NATO allies rejected these demands. In February, 2022, NATO countries troops were bordering countries such as Poland and Romania.

Following a prolonged phase of military tensions between Russia and Ukraine, on February 23, ESET, SentinelOne and Symantec began observing a new wiper malware (dubbed HermeticWiper) actively used against Ukrainian organizations.

On February 24, Russia launched a full-scale invasion of Ukraine.

### Multiple cyberattacks precede Russian invasion

Under the currently prevailing geopolitical climate, the use of cyberattacks as a weapon and a key part of the Russian offensive strategy is to be considered as an actual threat. This has already happened during the 2008 military campaign against Georgia and in the context of the Crimea 2014 crisis.

A large-scale cyber attack on critical infrastructure is often referred to as a precursor to a conventional military offensive. At the date of writing, a series of allegedly [Russian cyberattacks continue to target Ukraine](https://www.sekoia.com/blog/a-war-on-multiple-fronts-the-turbulent-cybercrime-landscape).

  * ‍**On January 13, 2022** , Microsoft communicated about a destructive malware targeting multiple organizations in Ukraine.**‍**
  * **On February 14, 2022** , the SSU (Security Service of Ukraine) issued a statement on Ukraine being targeted by a “massive wave of hybrid warfare”. According to the source, Ukrainian security services have recently dismantled numerous bot farms. Operations were also carried out to expose agent networks of hostile intelligence services and prevent sabotage and terrorist attacks.**‍**
  * **On February 15, 2022** , a [DDoS (Distributed Denial of Service) attack](/blog/following-noname05716-ddosia-projects-targets) targeted several Ukrainian government agencies (including websites of the Ukrainian army) and two major banks.**‍**
  * **On February 23, 2022** , a new data wiper dubbed as HermeticWiper was used in destructive attacks against Ukrainian networks. The websites of the Ukrainian parliament, Ministry of Foreign Affairs, and Council of Ministers, (including all individual ministerial sites), and the Security Service of Ukraine were affected by a presumed DDoS campaign. It happened after Vladimir Putin recognised the independence of the breakaway regions in Eastern Ukraine DNR and LNR, and Russia moved troops in multiple regions in Ukraine.



Surfbeam2 blackout, what happened with KA-SAT?

### Risks of collateral damage

European regulators invited the public and private sector organisations in the EU to improve their overall attack resilience, based on the “continuously increasing threat level”. The banks were invited to prepare for a possible Russian-sponsored cyber attack, according to sources cited by Reuters. CNN has also quoted sources within the United States Department of Homeland Security to warn about Russia considering a possible attack on the US homeland during a secondary assault.

Authorities and security experts warn that the following industries would be more likely to be targeted by a Russian attack in the upcoming time:

  * the banking sector,
  * the defence industry,
  * the communication services,
  * the energy sector.



**Any country and business can be a collateral victim of any potential Ukraine-directed malicious campaign.** To remind the 2017 NotPetya attack (initially designed to target companies in Ukraine), the threat ended up having a global impact.

One major issue in the ongoing Ukrainian border conflict is the NATO expansion into Eastern Europe.

**It is therefore possible that Russia tries to destabilize NATO countries – or their allies – and that coordinated cyber attacks accompany military campaigns involving nations beyond Ukraine.** If such an attack occurs, it could impact the entire region and the Eastern Europe in particular. There is a higher risk for NATO alliance member states such as Poland or Romania to be targeted. There is also a great risk for the East Coast of the United States to be involved in offensive Russian cyber operations.

“Intensified actions in Poland” have already been observed, [according to](https://www.express.co.uk/news/science/1571053/poland-under-attack-cyber-russia-invasion-ukraine-world-war-3-putin) Poland’s Government spokesman Piotr Müller.

In these circumstances, Joe Biden declared that the U.S. are “ _prepared to respond if Russia attacks the United States or our allies through disruptive cyberattacks against our companies or critical infrastructure_ ”. UK officials declared they also are ready to launch retaliatory cyber-attacks on Russia.

Nevertheless, a massive offensive campaign launched by Russian cyber forces that would directly target European or American infrastructures seems to be less likely than cyber repercussions caused to businesses and institutions worldwide via a targeted campaign against Ukraine.

The impact could range from denials-of-service against critical assets (authoritative nameservers, emergency services, telecommunications infrastructure) to cyber espionage and destructive attacks targeting critical infrastructure. We also have to mention that Russian APT groups such as Gamaredon have already been conducting massive prepositioning campaigns on Ukrainian infrastructures for a while.

Even if no immediate attack happens, there are already signs of information warfare affecting Ukrainian [cyberspace](https://www.sekoia.com/blog/sekoia-is-a-leader-in-european-cybersecurity) and – just as the Security Service of Ukraine have stated – aimed to “sow panic, spread fake information and distort the real state of affairs”.

### Cybercrime opportunities

Yet it isn’t all about the state sponsored actors – there are also opportunistic cybercriminal activities which should be taken into account. **Cybercriminal syndicates which are sympathetic to Russia’s political speech can either be easily mobilized by government agencies (to preserve an opportunistic appearance of attacks), or be enticed to follow a larger tendency and hit the same targets as the state-coordinated campaigns. It should also be remembered that cybercriminals take advantage of major crises such as the Russian invasion of Ukraine to distribute commodity malware or**[**phishing campaigns**](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers)**.**

**Malicious campaigns against western companies are expected to intensify, amplified by the sanctions on Russia announced by European and American authorities.**

While we cannot establish a causal link with the current geopolitical issues, we have noticed an increase in the number of campaigns against the energy, aviation and media industries in Europe since early February. These include attack campaigns from the groups operating RansomExx, LockBit, Hive, BlackCat, BlackByte and Conti ransomware. These groups are considered to involve [threat actors](https://www.sekoia.com/blog/eternityteam-a-new-prominent-threat-group-on-underground-forums) of Russian or other Russian-speaking country origin and many sources pointed, over time, to their affiliation with Russian intelligence agencies. Nevertheless, it is necessary to remain prudent about false-flag scenarios.

## Courses of action

  * We recommend you to be cautious with regards to your regional branches, supply-chain providers and your counterparts located or with systems in Ukraine and in the Eastern Europe, including NATO member countries. Be vigilant about their connections with their headquarters’ information system in France.
  * Use the provided IOCs to check for potential compromise of your network and prevent future attacks. Be aware of the Russian state-supported threat actors and their activity.
  * Refer to security alerts and recommendations issued by French, European and other regional public bodies and authorities related to your industry.



## Indicators of Compromise

` import "pe"  
rule wiper_HermeticWiper_variants {  
meta:  
id = "102ecf15-167e-49e4-932c-6334e3cdcc69"  
version = "1.0"  
malware = "HermeticWiper"  
description = "Matches HermeticWiper and possible variants"  
source = "SEKOIA"  
creation_date = "2022-02-24"  
modification_date = "2022-02-24"  
classification = "TLP:WHITE"  
strings:  
$ = "SeLoadDriverPrivilege" wide  
$ = "\\\\.\\PhysicalDrive" wide  
$ = "::$INDEX_ALLOCATION" wide  
$ = "CrashDumpEnabled" wide  
condition:  
2 of them and  
pe.characteristics and  
pe.number_of_signatures == 1 and  
pe.number_of_resources > 2 and  
for 2 i in (0..pe.number_of_resources - 1):  
( uint32be( pe.resources[i].offset+15 ) == 0x4D5A9000 and  
uint16be( pe.resources[i].offset ) == 0x535A )  
}  
`

## HermeticWiper hashes

`MD5  
3f4a16b29f2f0532b7ce3e7656799125  
84ba0197920fd3e2b7dfa719fee09d2f  
  
SHA1  
61b25d11392172e587d8da3045812a66c3385451  
912342f1c840a42f6b74132f8a7c4ffe7d40fb77  
  
SHA256  
1bc44eef75779e3ca1eefb8ff5a64807dbc942b1e4a2672d77b9f6928d292591  
0385eeab00e946a302b24a91dea4187c1210597b8e17cd9e2230450f5ece21da  
  
Ms-compressed resources dropped by HermeticWiper:  
(DRV_X64, DRV_X86, DRV_XP_X64 and DRV_XP_X86)  
  
MD5  
eb845b7a16ed82bd248e395d9852f467  
095a1678021b034903c85dd5acb447ad  
231b3385ac17e41c5bb1b1fcb59599c4  
a952e288a1ead66490b3275a807f52e5   
  
SHA1  
ee764632adedf6bb4cf4075a20b4f6a79b8f94c0   
9c2e465e8dfdfc1c0c472e0a34a7614d796294af   
0231721ef4e4519ec776ff7d1f25c937545ce9f4   
5ceebaf1cbb0c10b95f7edd458804a646c6f215e   
  
SHA256  
fd7eacc2f87aceac865b0aa97a50503d44b799f27737e009f91f3c281233c17d   
b6f2e008967c5527337448d768f2332d14b92de22a1279fd4d91000bb3d4a0fd  
b01e0c6ac0b8bcde145ab7b68cf246deea9402fa7ea3aede7105f7051fe240c1  
e5f3ef69a534260e899a36cec459440dc572388defd8f1d98760d31c700f42d5  
`

## References

  *  _[Symantec] Ukraine: Disk-wiping Attacks Precede Russian Invasion_ 👉 https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ukraine-wiper-malware-russia, accessed February 24, 2022
  *  _[SentinelOne]_[_HermeticWiper | New Destructive Malware Used In Cyber Attacks on Ukraine_](https://www.sentinelone.com/labs/hermetic-wiper-ukraine-under-attack/)
  * [ _[ESET] HermeticWiper: New data‑wiping malware hits Ukraine_](https://www.welivesecurity.com/2022/02/24/hermeticwiper-new-data-wiping-malware-hits-ukraine/)
  *  _[BleepingComputer]_[_New data-wiping malware used in destructive attacks on Ukraine_](https://www.bleepingcomputer.com/news/security/new-data-wiping-malware-used-in-destructive-attacks-on-ukraine/)
  * [ _[Sekoia.io] HermeticWiper in the Intelligence Center_](https://app.sekoia.io/intelligence/objects/malware--61ebda13-8e90-4657-a1e0-cb9700d8e041)
  * [ _[CISA, NCSC, NSA] New Sandworm malware Cyclops Blink replaces VPNFilter_](https://www.cisa.gov/sites/default/files/publications/AA22-054A%20New%20Sandworm%20Malware%20Cyclops%20Blink%20Replaces%20VPN%20Filter.pdf)
  * [ _[Bellingcat] Attack on Ukrainian Government Websites Linked to Russian GRU Hackers_](https://www.bellingcat.com/news/2022/02/23/attack-on-ukrainian-government-websites-linked-to-russian-gru-hackers/)
  * [ _[Independent.co.uk] Ukraine: UK ready to launch retaliatory cyber-attacks on Russia_](https://www.independent.co.uk/news/uk/politics/russia-ukraine-cyber-attack-ben-wallace-b2019836.html)
  * [ _[ANSSI] TENSIONS INTERNATIONALES : RENFORCEMENT DE LA VIGILANCE CYBER_](https://www.ssi.gouv.fr/actualite/tensions-internationales-renforcement-de-la-vigilance-cyber/)
  * [ _[Microsoft] Destructive malware targeting Ukrainian organizations_](https://www.microsoft.com/en-us/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/)
  * [ _[ENISA and CERT-EU] Boosting your Organisation’s Cyber Resilience_](https://www.enisa.europa.eu/publications/boosting-your-organisations-cyber-resilience)
  * [ _[Reuters] European, U.S. regulators tell banks to prepare for Russian cyberattack threat_](https://www.reuters.com/markets/europe/european-us-regulators-tell-banks-prepare-russian-cyberattack-threat-2022-02-09/)
  * [ _[CNN] DHS warns of potential Russia cyberattacks amid tensions_](https://edition.cnn.com/2022/01/24/politics/russia-cyberattack-warning-homeland-security/index.html)
  * [ _[The Guardian] Russia issues list of demands it says must be met to lower tensions in Europe_](https://www.theguardian.com/world/2021/dec/17/russia-issues-list-demands-tensions-europe-ukraine-nato)
  * [ _[Washington Post] Russian Government hackers have likely penetrated critical Ukrainian computer systems, U.S. says_](https://www.washingtonpost.com/national-security/2022/02/15/russia-ukraine-cyber-attacks/)
  * [ _[Security Service of Ukraine] SSU STATEMENT ON HYBRID WARFARE IN INFORMATION SPACE_](https://ssu.gov.ua/en/novyny/zaiava-sbu-shchodo-proiaviv-hibrydnoi-viiny-v-informatsiinomu-prostori)
  * [ _[Ministry of Defence of Ukraine] Announcement about a DDoS attack targeting the Ministry of Defence of Ukraine_](https://twitter.com/DefenceU/status/1493628291844083723)