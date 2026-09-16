# Discover Activities Linked to the DPRK-nexus Intrusion Sets

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/the-dprk-delicate-sound-of-cyber
- **Date :** 2022-12-16

---

This blog post aims at contextualising and analysing trends pertaining to cyber malicious activities associated to the Democratic People’s Republic of Korea-nexus Intrusion Sets reported in open sources in 2022.

Associated with the development of a ballistic, nuclear, and bacteriological arsenal, the cybernetic component, called "secret war" by Pyongyang, is part of the North Korean offensive approach since at least 2004. DPRK offensive cyber activities include cyberespionage and lucrative campaigns and are resolutely asymmetrical and a force multiplier in subverting international sanctions and funding Pyongyang’s economy. These facets contribute to the survival of the North Korean state, as well as maintaining its position within the international system as a “small great power.”

DPRK malicious cyber activities involve multiple state organisations, including the Ministry of State Security (MSS aka Bowibu) and the Reconnaissance General Bureau. Associated Intrusion Sets include Lazarus, Bluenoroff, Andariel, Reaper, and Kimsuky.

‍

![DPRK malicious cyber activities involve multiple state organisations, including the Ministry of State Security \( MSS aka Bowibu\) and the Reconnaissance General Bureau.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62ccd1cab63350d7daf_6a92a3d02e47a1e9fe0e5441_6a2a7b6893217eae509c6cf9.webp)

DPRK malicious cyber activities involve multiple state organisations, including the Ministry of State Security ( MSS aka Bowibu) and the Reconnaissance General Bureau.

‍

## **A saucerful of secrets**

### Let there be more spies

All North-Korea-associated Intrusion Sets continued carrying out **cyberespionage activities** throughout the year, with a particularly **high tempo of activity** demonstrated by Lazarus and Kimsuky. Targeted sectors notably included a strong **focus on cryptocurrency-related entities and the aerospace and defence industry** (operation DreamJob). Additional sectors of interest include technology, civil society (journalists, activists, defectors), academia, think tanks, media, and diplomacy, notably pertaining to nuclear policy, Korean Peninsula and Asia-Pacific subject matters. Reported malicious activities suggest a **renewed interest in targeting international organisations** [1] [2] for strategic intelligence collection.

Sekoia analysts noticed Kimsuky refocusing on their traditional assigned locations, namely the United States (U.S.), Japan, and the Republic of Korea (aka RoK and South Korea), and refocusing on military intelligence collection, as well as expanding their victimology to target the [shipping industry](https://www.welivesecurity.com/2021/04/08/are-you-afreight-dark-watch-out-vyveva-new-lazarus-backdoor/) and a company involved in [carbon credits](https://blog.cluster25.duskrise.com/2022/01/03/konni-targets-the-russian-diplomatic-sector). Last reported in April 2022, DPRK-nexus Intrusion Set **Reaper** was seen carrying out **targeted surveillance operations** against human rights activists, journalists, and defectors from North Korea notably leveraging the [Chinotto malware](https://securelist.com/scarcruft-surveilling-north-korean-defectors-and-human-rights-activists/105074/), Goldbackdoor, a variant of the BlueLight malware, and newly discovered CloudMensis, a spyware based on RokRAT and designed to target Windows and [MacOS systems](https://www.welivesecurity.com/2022/07/19/i-see-what-you-did-there-look-cloudmensis-macos-spyware/).

Additional DPRK-aligned cyberespionage activities include the targeting of the [energy and military sectors](https://www.security.com/threat-intelligence/stonefly-north-korea-espionage), as well as energy providers in Canada, Japan, and the United States between [February and July 2022](https://blog.talosintelligence.com/lazarus-three-rats/). Of note, energy-related targeting is a consistent longstanding assignment for the Andariel Intrusion Set. Additionally, **Andariel** was reported deploying their signature [Maui ransomware](https://securelist.com/andariel-deploys-dtrack-and-maui-ransomware/107063/) on at least one occasion in 2022. Based on available information, it is not clear whether the deployment of Maui was part of a lucrative objective and / or an anti-forensic effort from the Intrusion Set. It is also plausible [ransomware operations](/blog/sekoia-io-mid-2023-ransomware-threat-landscape) carried out by Andariel are part of **moonlighting activities for personal gain or selffunding**.

### You get a good (Dream)job

2022 saw the **continuation of DreamJob** (aka ShowState, DeathNote, Operation In(ter)ception), a two-fold campaign run by Lazarus since March 2019. DreamJob encompasses the targeting of aerospace and defence related organisations and individuals, security researchers, and cryptocurrency related entities for cyberespionage and lucrative objectives.

Lazarus continued relying on **social engineering** , including leveraging social networks and messaging applications (notably LinkedIn, WhatsApp and Slack) [masquerading as recruiters](https://www.malwarebytes.com/blog/threat-intelligence/2022/01/north-koreas-lazarus-apt-leverages-windows-update-client-github-in-latest-campaign) from defence and cryptocurrency high profile companies. Recent victimology notably includes defence contractors in France, Belgium, Italy, Spain, Germany, Czech Republic, the Netherlands, Poland, Ukraine, Turkey, South Africa, Qatar, [and Brazil](https://www.eset.com/uk/about/newsroom/press-releases/eset-research-lazarus-attacks-aerospace-and-defence-contractors-worldwide-while-misusing-linkedin-a/).

Sekoia analysts assess the targeting of security researchers observed in this campaign likely provides Lazarus with knowledge to improve their Tactics, Techniques and Procedures (TTPs), notably those pertaining to persistence, defence evasion and anti-forensics efforts. This activity also possibly aims at contributing to capacity building for Lazarus, providing them with new tools and malware for follow-up operations.

## The DPRK side of the mo(o)ney

DPRK-nexus Intrusion Sets, including Lazarus and Bluenoroff continued carrying out **lucrative cyber campaigns** , notably targeting cryptocurrency and financial technology-related activities. As previously mentioned, this includes part of Operation DreamJob conducted by Lazarus, whose financially motivated aspect was notably illustrated by the targeting of a Brazilian cryptocurrency company [with NukeSped](https://twitter.com/ESETresearch/status/1559553324998955010). Of note, Sekoia assess it is likely that Brazil “Bitcoin Law” debates occurring [in October 2021](https://decrypt.co/82675/brazilian-lawmaker-bitcoin-legal-payment-currency) renewed Lazarus’ interest in targeting this country in lucrative motivated campaigns.

![DPRK-nexus Intrusion Sets, including Lazarus and Bluenoroff continued carrying out lucrative cyber campaigns. \(SEKOIA.IO\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62ccd1cab63350d7da6_6a92a3cedae089660dfcdf4a_6a2a7b6893217eae509c6ced.webp)

DPRK-nexus Intrusion Sets, including Lazarus and Bluenoroff continued carrying out lucrative cyber campaigns. (Sekoia)

### Apples and Oranges

Lazarus also continued running the **AppleJeus campaign** , targeting cryptocurrency and fintech platforms and users with backdoored cryptocurrency trading applications, active since [at least 2018](https://blog.google/threat-analysis-group/countering-threats-north-korea/). The U.S. Cybersecurity and Infrastructure Security Agency (CISA) publicly attributed the malicious campaign against decentralized finance (DeFi) platform Ronin Network (Axie Infinity) that occurred in March [to Lazarus](https://therecord.media/us-agency-attributes-540-million-ronin-hack-to-north-korean-apt-group).

### Snatch that cash

Another long-running campaign called **SnatchCrypto**(aka CryptoCore, DangerousPassword) carried out by [**Bluenoroff**](https://securelist.com/the-bluenoroff-cryptocurrency-hunt-is-still-on/105488/)**** since 2017 was still active through 2022. From Sekoia analysts’ vantage point, this campaign notably includes **TraderTraitor activities** , a series of malicious applications masquerading as trading or price prediction tools, using the Electron framework and cross-platform JavaScript code to deliver the [Manuscrypt RAT](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-108a). This campaign appears **opportunistic** in nature, victimology notably includes Europe, Asia, the U.S., and the UAE.

Financially motivated campaigns are a trademark of DPRK-nexus Intrusion Sets, almost certainly to evade economic sanctions and funding of follow-up cyber malicious campaigns. Open-source reports also indicate funding of nuclear weapons through the Reconnaissance General Bureau (RGB), specifically Bureau 121, which Lazarus, Andariel and Bluenoroff are allegedly subordinated to. However, recent reporting indicates that DPRK-nexus Intrusion Sets tend to hold stolen cryptocurrency for several years, possibly as part of their monetary policy. Another hypothesis is that unlaundered cryptocurrency funds could possibly result from an operator error.

![DPRK-nexus Intrusion Sets 2022 activities. Source : Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62ccd1cab63350d7dac_6a92a3d19d3b9ef4d8bbcbc3_6a2a7b6893217eae509c6cfd.webp)

DPRK-nexus Intrusion Sets 2022 activities. Source : Sekoia

## The peek at the gates

Based on reported TTPs and malware analysis provided in open sources, Sekoia analysts observed North Korea-nexus Intrusion Sets strong and**continued efforts in selectively targeting their victims and improving their stealthiness**.

Besides advanced reconnaissance efforts, Intrusion Sets can further screen their targets before delivering their payload. For instance, Kimsuky was recently observed using an **IP validation method** as part of its [GoldDragon infection mechanism](https://securelist.com/kimsukys-golddragon-cluster-and-its-c2-operations/107258/). The same Intrusion Set also newly implemented a **geofencing** mechanism in their signature malware [Konni RAT](https://asec.ahnlab.com/en/31089/), and similar behaviour was observed in the [FastSpy infection chain](https://medium.com/s2wblog/unveil-the-evolution-of-kimsuky-targeting-android-devices-with-newly-discovered-mobile-malware-280dae5a650f). In a recent campaign Kimsuky also used a file exfiltrator component to find and collect specific files of interest via filelists hosted on a [remote server](https://blog.talosintelligence.com/kimsuky-abuses-blogs-delivers-malware/).

![Based on reported TTPs and malware analysis provided in open sources, SEKOIA.IO analysts observed North Korea-nexus Intrusion Sets strong and continued efforts in selectively targeting their victims and improving their stealthiness.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62ccd1cab63350d7da9_6a92a3cf9d3b9ef4d8bbcb29_6a2a7b6893217eae509c6cf5.webp)

Based on reported TTPs and malware analysis provided in open sources, Sekoia analysts observed North Korea-nexus Intrusion Sets strong and continued efforts in selectively targeting their victims and improving their stealthiness.

While North Korea-nexus Intrusion Sets traditionally reuse their infrastructure, they demonstrate increased efforts to achieve stealthiness, notably through obfuscation, defence evasion mechanisms as well as regularly updating their infection chain. Of note, spearphishing remains the principal observed vector of intrusion in these Intrusion Sets malicious cyber activities.

In a campaign against South Korean diplomacy and security-related entities, Kimsuky impersonated a South Korean institution to engage in an email exchange, sending a malicious URL only if the recipient responds positively to the initial email. Similarly, Lazarus was observed hosting a ZIP file containing a malicious document to bypass recent changes made by [Microsoft for Office macros](https://www.malwarebytes.com/blog/news/2022/01/microsoft-is-now-disabling-excel-4-0-macros-by-default). Also increasingly reported is the **hosting of malicious Command and Control (C2) on open-source hosting services** such as DropBox, GitHub or Blogspot.

Of particular interest and documented as a **first seen in the wild in 2022** (although leveraged at least since October 2021 as part of Operation DreamJob), Lazarus’ **Bring Your Own Vulnerable Driver (BYOVD)** technique to deploy [BLINDINGCAN](https://asec.ahnlab.com/en/40830/). Lazarus was also observed leveraging CVE-2022-0609, a 0-day remote code execution vulnerability in Google Chrome web browser to target cryptocurrency and fintech entities through spearphishing, fake websites, or compromised legitimate websites.

These TTPs are a sign of adaptability by North Korea-nexus Intrusion Sets, and Sekoia analysts assess this is almost certainly a way to preserve their offensive capabilities. 

## Household objects

Over the course of this year, North Korea-nexus Intrusion Sets continuously dedicated efforts to **update and / or renew their toolsets**. Notable changes to Sekoia analysts include:

  * Lazarus recent development of **KiTTY** , a weaponized PuTTY fork, as part of its [BLINDINGCAN infection chain](https://www.microsoft.com/en-us/security/blog/2022/09/29/zinc-weaponizing-open-source-software/).
  * **MagicRAT** , a new C++ malware delivered after exploitation of publicly exposed [VMware Horizon platforms](https://blog.talosintelligence.com/lazarus-magicrat/).
  * As touched upon before, Kimsuky was observed leveraging new Android malware known as **FastFire, FastViewer, and FastSpy**. Another interesting malicious web browser extension used by Kimsuky is [**Sharpext**](https://www.volexity.com/blog/2022/07/28/sharptongue-deploys-clever-mail-stealing-browser-extension-sharpext/), used by Kimsuky a post-exploitation tool since 2021.



## **Is there anybody out there?**

#### **Us and them**

In 2022, open-source reports mentioned overlaps between DPRK Intrusion Sets and cybercriminal groups, including:

#### Suspected links between Lazarus and Wizard Spider

Based on infrastructure links, security researchers initially assessed a potential connection between Russia-based cybercriminal group Wizard Spider and Lazarus. Based on the report documenting the Exotic Lily Initial Access Broker (IAB), Sekoia assess **it is likely that Lazarus resorted to IAB services** , including Exotic Lily’s, and entertain connections with the cybercriminal ecosystem.

#### Connections between Quantum Builder and Lazarus

A report published in open sources in June 2022 mentioned a possible use of the .lnk builder Quantum Software / Quantum Builder [by Lazarus](https://cyble.com/blog/quantum-software-lnk-file-based-builders-growing-in-popularity/). Upon script comparison, it was observed the PowerShell script deobfuscation loop and initialization of variables were similar. As Lazarus increasingly resorted to .lnk since the second half of 2020, Sekoia analysts assess **it is plausible they use Quantum Builder as part of their toolset**.

#### Connections between DEV-0530 and Andariel

Tracked under the DEV-0530 alias, the cybercriminal group which developed the H0lyGh0st ransomware is assessed to be originating from [the DPRK](https://www.microsoft.com/en-us/security/blog/2022/07/14/north-korean-threat-actor-targets-small-and-midsize-businesses-with-h0lygh0st-ransomware/). Microsoft security researchers assess that DEV-0530 “has connections” with Andariel. This assessment is notably based on the observation of communication between DEV-0530 email accounts and Andariel accounts, infrastructure links, as well as DEV0530’s use of tools exclusively used by Andariel. Sekoia analysts concur with Microsoft hypothesis of moonlighting activities. **It is likely that DEV-0530 is an offshoot of Andariel**.

## Wish you were here

In 2022, the **DPRK cyber offensive strategy continued relying on the physical layer**.

![It is almost certain that military intelligence, strategic intelligence, and economic intelligence collection and surveillance will remain strong drivers for DPRK-originating cyberespionage campaigns. \(SEKOIA.IO\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62ccd1cab63350d7da3_6a92a3ce693fca262e1bc008_6a2a7b6893217eae509c6cf1.webp)

It is almost certain that military intelligence, strategic intelligence, and economic intelligence collection and surveillance will remain strong drivers for DPRK-originating cyberespionage campaigns. (Sekoia)

In April 2022, two South Korean individuals, the CEO of a virtual asset investment company and an active-duty officer, were charged with violating the South Korea National Security Act for leaking military information to a suspected [North Korean agent](https://www.yna.co.kr/view/AKR20220428120500004). The operation reportedly involved a camera watch and a [PoisonTap USB device](https://samy.pl/poisontap/) to infiltrate a South Korean military base and gain access to a military laptop between January and March 2022.

In May 2022, the U.S. Department of State issued an advisory, alerting organisations against [hiring North Korean IT workers](https://ofac.treasury.gov/media/923126/download?inline).

This highlights that North Korean intelligence operatives continue leveraging individuals, including insider threats, that will notably assist in obtaining access to systems of interest. Sekoia assess that part of stolen cryptocurrency plausibly contributes to fund incentives for such operations. Furthermore, it is also possible that North Korean IT workers abroad could leverage the acquired skills to carry out malicious campaigns in line with Pyongyang interests.

## The sanction bell

In 2022, DPRK-associated cyber malicious activities garnered **increased attention, in a context of heightened tensions in the Korean Peninsula**.

In January, North Korea’s Internet was hit by two waves of [Distributed Denial of Service (DDoS) attacks](https://www.reuters.com/world/asia-pacific/nkorean-internet-downed-by-suspected-cyber-attacks-researchers-2022-01-26/) which turned out to be a hackback carried out by a hacker in retaliation to [Lazarus DreamJob campaign](https://www.wired.com/story/north-korea-hacker-internet-outage/).

In addition, Nation-State political and economic measures were undertaken. Sekoia analysts notably observed a more coordinated, time-constrained approach to the attribution process and efforts to hinder malicious cyber activities. U.S. agencies officially attributed the TraderTraitor campaign to Bluenoroff, the [Maui ransomware to Andariel](https://www.cisa.gov/news-events/cybersecurity-advisories/aa22-187a), and the Ronin Network cryptocurrency theft to Lazarus.

In March 2022, the [U.S. Department of Treasury sanctioned](https://home.treasury.gov/news/press-releases/jy0916) Blender.io, a virtual currency mixer, used by Lazarus to launder USD 20.5 million (out of the USD 620 million stolen) on the account of financially supporting DPRK [38]. In August 2022, the U.S. also blacklisted [Tornado Cash](https://www.fiod.nl/arrest-of-suspected-developer-of-tornado-cash/), a virtual currency mixer used by Lazarus to launder at least USD 7 billion worth of virtual currency since its creation in 2019. This was followed by the arrest of a Tornado Cash developer in the Netherlands by the [Fiscal Information and Investigation Service (FIOD)](https://www.nknews.org/2022/10/japan-sanctions-5-north-korean-companies-following-us-and-south-koreas-lead/).

## Assessments

Based on DPRK-nexus Intrusion Sets reported activities, Sekoiaanalysts assess the following:

  * It is almost certain **financially motivated cyber campaigns will remain a high priority for Pyongyang**. DPRK-nexus Intrusion Sets lucrative activities will continue in the short-to-medium term, with a consistent targeting of cryptocurrency and fintech related entities and individuals. It is likely Lazarus and Bluenoroff wil**l expand their victimology to include countries inclined to legalise cryptocurrency and / or where cryptocurrency is a legal tender** (i.e., Ecuador, Central Africa, Salvador).
  * It is almost certain that military intelligence, strategic intelligence, and economic intelligence collection and surveillance will remain strong drivers for DPRK-originating cyberespionage campaigns. This notably includes continuation of the long-running campaign DreamJob.
  * While ongoing sanction measures are likely to slow down DPRK Intrusion Sets activities in the short-term, Sekoia analysts assess this is **unlikely to disrupt cyber malicious campaigns orchestrated by Pyongyang**.



Sekoia will continue monitoring and tracking Intrusion Sets associated to DPRK and welcome any feedback and / or additional input to further contribute to understanding and countering this threat.