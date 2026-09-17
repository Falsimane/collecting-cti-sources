# COVID-19 Cyber Threats | Weekly Updates | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/covid-19-cyber-threats/
- **Date :** March 24, 2020

---

# Situational Awareness: Cyber Threats Heightened by COVID-19 and How to Protect Against Them

March 24, 2020

• [ Adam Meyers](/en-us/blog/author.adam-meyers/ "Posts by Adam Meyers") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


**Please Note: Check this blog for frequent updates on adversary activity related to COVID-19.** **June 24, 2020: Observed Activity Update** As the COVID-19 pandemic continues to take hold in various geographical locations, government and businesses are rapidly changing how and where they operate to ensure the safety and health of their employees, customers and partners. This environment is dynamic, and the continually shifting paradigm has significant consequences on organizational security posture. “Work from home” is becoming the new normal for organizations hoping to flatten the curve of the pandemic. For some organizations, remote work has been ongoing for several years, and the new push is simply a matter of scaling up existing solutions and policies. In many other environments, work from home is a foreign concept; technology, operations and policies are not prepared for this new reality, and several challenges are being encountered such as:

  * Use of personal devices and email for business or handling sensitive information
  * Provisioning corporate assets to support remote working arrangements
  * Proper deployment and configuration of remote services, corporate VPNs and related two-factor authentication methods



Adversaries are keenly aware of these challenges and the opportunities for abusing this situation to their advantage. This blog provides an overview of tactics and observed cyber threats beginning in January 2020 through publication.

## Tactic Highlight: Phishing

[Phishing](/cybersecurity-101/phishing.html) remains the primary initial access vector for a variety of [threat actors](/en-us/blog/meet-the-adversaries/). Successful phishing attacks frequently play to greed or fear in the victim. The infamous “Nigerian Prince” schemes are an example of the use of greed, where the promise of riches entices the victim to do things they ordinarily wouldn’t do. In the case of the COVID-19 pandemic, fear abounds, and the awareness of the pandemic itself is global. Phishing attacks promise new information about the virus or updates on official guidance. In addition to what has been observed, CrowdStrike® Intelligence assesses with high confidence that it is likely for additional **phishing campaigns to make use of lures aligned with health guidance, containment and infection-rate news** to increase over the next few months. In addition to phishing lures leveraging health-related interest, there is also a possibility that actors could take advantage of more employees working from home, and move toward lures attempting to spoof company guidance and procedures, human resource correspondence and company information technology (IT) issues and resources. While such exploitative operations have not been directly observed at this time, targeted intrusion adversaries in particular have relied on job-themed and human resource-themed lure documents over the last few months. In a situation where employees will increasingly rely on email communications to continue business operations, the threat of phishing campaigns attempting to mimic official business communications will likely increase.

### Observed Activity: eCrime

As the pandemic continues to evolve, CrowdStrike has observed sustained eCrime activity across the board, including some with COVID-19 themes. Campaigns have been observed in multiple languages, using multiple attachment types and various levels of COVID-19 information, demonstrating that the scope of these campaigns has been and is likely to remain wide. COVID-19-themed activity has followed the path of the virus as it has moved from Asia across the world. As news about the situation in various locales emerges, the themes and targets change — for example, with recent news of the desperate situation in Italy, WIZARD SPIDER was observed deploying dynamic web inject files that solely target customers of Italian financial institutions, with the intent of stealing credentials for accounts. One of the earliest eCrime actors to capitalize on the COVID-19 outbreak was [MUMMY SPIDER](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-february-mummy-spider/) in late January 2020. This actor used Japanese-language spam [spoofing](/cybersecurity-101/spoofing-attacks.html) a public health center in order to distribute the Emotet downloader malware, which subsequently led to the download and install of [WIZARD SPIDER’s TrickBot](/en-us/blog/wizard-spider-lunar-spider-shared-proxy-module/). CrowdStrike Intelligence has continued to identify multiple campaigns distributing additional eCrime threats, such as Gozi ISFB, Nemty ransomware, SCULLY SPIDER’s DanaBot, GRACEFUL SPIDER’s GetAndGo Loader and the Latin America-targeted malware Kiron. There have also been instances of eCrime **actors attempting to sell COVID-19-themed tools** , including a phishing method using a payload preloader masked as a COVID-19 map.

### Observed Activity: Targeted Intrusion

Despite the impact of COVID-19 on their respective countries, CrowdStrike Intelligence has observed multiple nation-state-affiliated targeted intrusion adversaries remaining active with [spear-phishing campaigns](/epp-101/spear-phishing.html) throughout the last few months. Moreover, many of these adversaries have already been observed using COVID-19-themed operations: China-based PIRATE PANDA was observed using COVID-19-themed lure documents in February 2020; Democratic People’s Republic of Korea (DPRK) adversary VELVET CHOLLIMA has also remained active and recently leveraged a COVID-19-themed lure document to deliver its unique BabyShark malware against South Korea-based organizations.

## Tactic: Targeting Remote Services

It is possible that companies will increase the use of software as a service (SaaS) and cloud-based remote connectivity services in order to enable and support employees working from home. Standing up remote working services could pose a potential security risk when combined with possible human-error-enabled security lapses. Criminal actors in particular continually seek to collect credentials for these services, potentially allowing them to gain access to these SaaS accounts and victim organization data. The eCrime big game hunting (BGH) ransomware industry in particular leverages Remote Desktop Protocol (RDP) brute forcing or password spraying for initial entry. As many sophisticated BGH actors remain highly active at present, they will likely attempt to capitalize on possible staffing disruptions COVID-19 may bring to organizations, as well as attempt to compromise employee devices while they work remotely.

## Tactic: Vishing Robocall and Tech Support Scams

As employees shift to flexible work arrangements such as telecommuting, they will increasingly rely on phone communications to maintain and continue business operations. Adversaries will likely take advantage of this situation and conduct malicious operations attempting to mimic official business communications. Such operations could include voice phishing or “vishing” and robocall scams, as well as technical support scams. Criminals have been observed using the COVID-19 outbreak as a theme in vishing and robocall scams. A portion of these calls have initially focused on targets on the U.S. West Coast, as well as industries affected by the outbreak, such as transportation and travel. In some cases, vishing can be combined with smishing (text message phishing) in order to perpetrate such scams or load malicious content onto mobile devices. Technical support scams use various delivery methods including phone calls, pop-up warnings or redirects. Although the theme of these scams may not be directly related to COVID-19, the increase in office workers transitioning to remote work in the near term poses the risk of increased tech support scams targeting those individuals, who may not be adept at or self-sufficient in remote computing.

## Recommendations for Defending Against COVID-19 Scams

As the global COVID-19 outbreak grows, CrowdStrike assesses that malicious cyber threat actors will continue to take advantage of the situation. As such, it is imperative that businesses and employees remain aware of the potential cyber threats they face while they make transitions to alternative business continuity plans, and that they are informed of the immediate steps they can take to mitigate potential risks. CrowdStrike recommends adopting a strong defensive posture by ensuring that remote services, VPNs and multifactor authentication solutions are fully patched and properly integrated, and by providing security awareness training for employees working from home. In order to help customers cope with these new and unexpected developments, CrowdStrike is offering [two limited-time programs.](/en-us/blog/new-programs-to-secure-remote-workers-during-covid19-crisis/) They address the challenges introduced by the large number of managed and unmanaged devices being used by newly remote workers.

## Observed Activity Update: Wednesday, June 24

In the past week, CrowdStrike Intelligence observed the following notable threats using COVID-19 themes.

  * CrowdStrike Intelligence continues to observe eCrime adversaries using [social engineering techniques](/cybersecurity-101/social-engineering-attacks.html) and malicious documents referencing COVID-19. The following table provides an overview of notable criminal malware from the past week that referenced COVID-19 in malicious filenames.

**MALWARE FAMILY**| **FILENAME**  
---|---  
Thanos Ransomware| `crédito covid-19.exe`  
CoViper| `covid-19.exe`  
AgentTesla| `covid19.pdf`  
FormBook| ```covid-19 circular.com```````  
  
The volume of malicious COVID-19 files has declined for two consecutive weeks.![black graph with orange line](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2020/03/June-22-chart1-1.png)

  * CrowdStrike Intelligence recently identified a COVID-19-themed spam campaign targeting Spain-based victims to deliver the Latin American Culebra Variant Trojan. The email addresses the alleged misuse of masks in public places. (The use of masks in Spain is currently mandatory in locations where social distancing cannot be maintained.) Culebra Variant currently targets financial institutions in Brazil, Chile, and Spain. Additional analysis of Culebra Variant confirms it is likely based on the same source code as Culebra malware, whose code has likely been leaked, raising the potential for new Culebra-associated variants appearing in the wild.



## Observed Activity Update: Monday, June 15

In the past week, CrowdStrike Intelligence observed the following notable threats using COVID-19 themes.

  * In early June 2020, CrowdStrike Intelligence observed a phishing campaign targeting a broad scope of organizations in various sectors and geographies involved in the COVID-19 pandemic response. The campaign relies on a large number of phishing URLs associated with a Russia-based IP address. Additional analysis confirms the following tactics:
    * Malicious HTM files sent as attachments in phishing emails

    * HTM files display a message telling the user to log in, review, and authorize a company policy. Most referred to the company’s “Reimbursement Policy,” but one file referred to the company’s “Covid-19 Relief Plan”
    * The messages spoof the target company’s Human Resources Department

    * The HTM file redirects the user to malicious actor-controlled infrastructure hosting a phishing page for Microsoft credentials



The likely intent is to obtain access to organizations by compromising legitimate accounts. Stolen credentials can then be used to perform account takeovers, from which additional phishing campaigns can be launched. Public reporting has listed a German-based multinational corporation as one of the targeted entities. CrowdStrike Intelligence has identified additional victims in the technology, industrials and engineering, financial, retail, energy, and healthcare sectors.

  * CrowdStrike Intelligence continues to observe eCrime adversaries using social engineering techniques and malicious documents referencing COVID-19. The following table provides an overview of notable criminal malware from the past week that referenced COVID-19 in malicious filenames.

**MALWARE FAMILY**| **FILENAME**  
---|---  
AgentTesla| 

  * `covid19.doc`
  * `covidsample.exe`
  * `covid19.pdf`

  
GuLoader| 

  * `boe-4596-covid19-3943.lha`

  
FormBook| 

  * `rfq covid-19 civil relief order 0216.exe`

  
Virgo exploit document| 

  * `covid-19 funding eligibility form.doc`

  
njRAT| 

  * `covid2020.exe`

  
LokiBot| 

  * `covid19.doc`

  
  
  * The volume of malicious COVID-19-themed files remains relatively steady when compared with previous weeks, as indicated in the chart below.



## ![chart with blue line](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2020/03/June-15-chart2-1.png)

## Observed Activity Update: Monday, June 8

  * CrowdStrike Intelligence continues to observe eCrime adversaries using social engineering techniques and malicious documents referencing COVID-19. The following table provides an overview of notable criminal malware from the past week that referenced COVID-19 in malicious filenames.

**MALWARE FAMILY**| **FILENAME**  
---|---  
RM3| `1015floopydiskonlinecovidvirus.bin`  
GuLoader| `distribucija zaštitne opreme covid-19 (ministarstvo zdravlja srbije) 2020 (136 kb)`  
AgentTesla| `covid-19 testing kits.xls.exe`  
  
  * Threat actors continue to use COVID-19 themes heavily. While file volume fluctuates between weeks, the pandemic remains relevant despite some countries relaxing social distancing guidelines.



## ![graph with blue line indicating malicious coronavirus-themed files per week](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2020/03/CSWR-20021-Figure-1-1.png)

## Observed Activity Update: Thursday, June 4

In the past week, CrowdStrike Intelligence observed the following notable threats using COVID-19 themes.

  * A new ransomware variant named F*ckUnicorn began targeting victims in Italy via spam campaigns with a COVID-19 theme. The ransomware, which is a variant of the open-source Hidden Tear ransomware, was circulated using lures referring to the Italian government’s rollout for their COVID-19 track-and-trace application. The ransomware is of below average sophistication and contains numerous cryptographic weaknesses that may allow for the free recovery of files. Based on the use of the Italian language and structure, CrowdStrike Intelligence assesses that the author is likely a native Italian speaker.

The following table provides an overview of indicators used in the spam campaign.



**TYPE**| **INDICATOR**  
---|---  
Domains| 

  * `Fofl<.>it`
  * `www.fofl.it`

  
Phishing Download URLs| 

  * `https://www.fofl<.>it/IMMUNI.exe`
  * `https://www.fofl<.>it/IMMUNI.rar`

  
IP/C2 IP| 

  * `116.203.210<.>127`
  * `http://116.203.210<.>127/write.php`

  
SHA256 Hash| 

  * `7980ef30b9bed26a9823d3dd5746cdefe5d01de2b2eb2c5e17dbfd1fd52f62bf`

  
  
  * In the blog post, “[MalSpam in the time of COVID-19](/en-us/blog/covid19-and-malspam/),” the CrowdStrike data science team examines five different malicious email spam (MalSpam) campaigns.

This blog examines the social engineering methods used to deliver the payload and examine the behavior of the delivered malware.



## Observed Activity Update: Tuesday, May 26

  * Since March, CrowdStrike Intelligence has repeatedly observed eCrime adversaries using COVID-19 as a theme for socially engineered phishing campaigns. The malicious payloads have included a mixture of commodity malware and loaders, with several variants dominating the threat landscape — namely AgentTesla, LokiBot, NanoCore and FormBook. A common tactic has been to directly reference COVID-19 in the name of the malicious spam email file attachment. Previously detected examples include:
    * `COVID-19_UPDATE.jpg.lnk`
    * `CoronaVirusSafetyMeasures_pdf.exe`
    * `Coronavirus Disease (COVID-19) CURE.zip`
    * `COVID-19 Communication to corporate Clients.rar`
A reduced detection rate of these files over the past three weeks indicates the tactic may be on the decline — potentially as intended victims have become more aware of the phishing threats. Instead, CrowdStrike Intelligence has detected a slight shift toward techniques and lure themes that make less obvious COVID-19-related references, and include more generic file attachment names. Popular among these emerging techniques is the use of fake invoice and purchase order invoices, asking the recipient to interact with an attached file that has a generic name (e.g., `PO and DETAILS7657.doc` or `OVERDUE INVOICES.rar`), and making only a passing reference to the pandemic within the email body. This shift in social engineering techniques does not necessarily reduce the threat — as the final payloads have remained consistent — but demonstrates the evolving nature of socially engineered phishing attacks.
  * On May 19, 2020, an affiliate of LUNAR SPIDER distributed a spam campaign that uses a COVID-19-themed lure to deliver the commodity banking malware BokBot (aka IcedID). The sample identified by CrowdStrike Intelligence makes reference to a change in legislation regarding requests for employee leave under the U.S. Family and Medical Leave Act (FMLA) during the pandemic, and claims to originate from “COVID-19 CENTER” using a spoofed email address. The email has a Microsoft Office Word (.doc) attachment titled `FMLAINSTRUCTIONS.doc`, which purportedly contains further information. Opening this document and enabling macros triggers the extraction, writing and running of an executable file (`PFSDNSKDF.EXE`).



## Observed Activity Update: Monday, May 18

  * CrowdStrike Intelligence continues to observe eCrime adversaries using social engineering techniques and malicious documents referencing COVID-19. The following table provides an overview of criminal malware from the past week that referenced COVID-19 in malicious filenames.

**MALWARE FAMILY**| **FILENAME**  
---|---  
NetSupport RAT Dropper| 

  * `covid_usa_nyt_4994.xls`

  
AgentTesla| 

  * `fondos de alivio de covid-19.zip`
  * `B-COVID-19 WHO RECOMENDED V.exe`

  
LokiBot| 

  * `new purchase order for covid-19 shipment_pdf.exe`
  * `new purchase order for covid-19 shipment_pdf.arj`
  * `covid-19_copy of transfer receipt from our bank.eml`

  
GuLoader| 

  * `covid 19 thanh toan.exe`
  * `Pembayaran Covid 19.exe`

  
KPOT Stealer| 

  * `covid-19 relief payment approval.pdf.gz`

  
FormBook| 

  * `COVID-19 UPDATE MSC SINGAPORE BUSINESS CONTINUITY PLAN ANNOUNCEMENT_PDF.exe`

  
  
Some vendors on known criminal marketplaces seek to capitalize on the pandemic by offering phishing kits and scam pages for sale. CrowdStrike Intelligence recently identified a post by a marketplace vendor advertising a job opportunity assisting with editing a COVID-19-related scam page.

Several new domains referencing pharmaceutical companies and COVID-19 were detected on May 13, 2020, by CrowdStrike Intelligence. The naming conventions of the domains were relatively similar, for example:

  *     * `corona.com`
    * `covid.com`
    * `corona.com`
    * `Covid19-.com`



eCrime adversaries frequently use fraudulent domains to serve as phishing pages—one of the newly identified domains included several subdomains with spoof credential login portals, highly likely intended to capture employee credentials. As well as being lucrative targets for attacks by eCrime actors, pharmaceutical companies and their employees are at heightened risk of phishing attacks by targeted intrusion actors conducting intelligence-gathering operations pertaining to COVID-19 response efforts.

  * A Brazilian hacktivist group known as Digital Space is promoting links to their website, which is hosting databases sourced from five separate data breaches. The leaks are being promoted across associated social media accounts alongside the hashtag #Opcovid19. Under this operation name, multiple hacktivist groups have claimed responsibility for conducting attacks against government and health ministry entities. Brazilian hacktivist groups appear to be using a Discord server to centralize and plan operations, which could result in future coordinated operations.
  * On May 15, 2020, Romanian law enforcement, led by Romania's Directorate for Investigating Organized Crime and Terrorism (DIICOT), [arrested four criminals](https://romania.europalibera.org/a/atac-cibernetic-asupra-spitalelor-din-romania-oprit-de-diicot-si-sri/30614118.html) that are reported to be members of a hacking group called PentaGuard. The four individuals were said to be planning to use ransomware against hospitals in Romania. A statement from DIICOT said these individuals “intended to launch ransomware attacks, in the near future, on public health institutions in Romania, generally hospitals, using social engineering by sending a malicious executable application, from the ‘Locky’ or ‘BadRabbit’ (computer virus) families, hidden in an email and in the form of a file that apparently would come from other government institutions, regarding the threat of COVID19.”
  * The ARCHER high-performance computing (HPC) network, a UK academic supercomputer possibly involved in modeling the spread of COVID-19, experienced an exploitation of its login nodes, according to [media reporting](https://www.theregister.co.uk/2020/05/13/uk_archer_supercomputer_cyberattack.html). The exploitation reportedly affected user passwords and SSH keys and has resulted in ARCHER’s system administrators suspending access to the network. Speculation from unnamed sources posited that the HPC would be an “obvious” target for nation-states interested in stealing or disrupting academic research into COVID-19 in the United Kingdom. ARCHER’s administrators indicated in a statement that other academic computers across Europe have also been compromised.



## Observed Activity Update: Monday, May 11

  * eCrime actors continue to use social engineering techniques and malicious documents referring to COVID-19. The following table provides an overview of criminal malware from the past week that referenced COVID-19 in malicious filenames.

MALWARE FAMILY | FILENAME  
---|---  
Metasploit Loader| covid19.exe  
LokiBot| business notification on covid-19 coronavirus documet_pdf.exe  
GuLoader| pago covid-19.exe  
AgentTesla| scan_covid-19-urgent-information-letter.xlxs.iso  
NanoCore| 

  * COVID19 Test kit.z -> COVID 19 test kit.exe
  * action required_ department of health invitation (covid-19 contact tracing).msg

  
Racoon Stealer| covid-19 stop.doc  
Azorult| Drawings_NEW ORDER UNISON_ COVID-19 SUPPLIES.tbz2  
  
  * On April 28, 2020, CrowdStrike Intelligence observed a spam campaign involving a Microsoft Teams-themed lure. The emails redirected victims to a Microsoft-themed phishing page, highly likely seeking to capture users’ credentials. Lures using video conferencing themes are highly likely seeking to capitalize on the COVID-19 pandemic, as more individuals and businesses adopt remote working practices during lockdown conditions. A similar campaign was [observed](https://abnormalsecurity.com/blog/microsoft-teams-impersonation) in mid-April 2019 purporting to originate from an individual attempting to communicate through Microsoft Teams and contained a hyperlink that directed the user to a phishing page.

  * CrowdStrike Intelligence observed a campaign by the Russia-based adversary PRIMITIVE BEAR that was leveraging COVID-19 lures to target suspected Ukrainian officials. The observed spear-phishing messages associated with this campaign appeared to stem from at least mid-April 2020 and contained two attachments. One of the attachments was a malicious document using the Template Injection technique to execute a VBA macro from an additional document retrieved from the internet when a victim opens the file. This delivery chain—based on the Template Injection technique of retrieving templates from DDNS domains hosted at the Russian telecommunications provider Sprinthost—is consistent with previously observed PRIMITIVE BEAR phishing campaigns.
  * In early May 2020, open source reporting described recent credential collection activity targeting Western organizations involved in response efforts for the ongoing COVID-19 pandemic. Reported target organizations include a prominent international public health organization as well as at least one major pharmaceutical company. According to reports, this activity employed spear-phishing emails containing misleading links directing victims to generic adversary-controlled login pages. Based on overlaps with previously-documented operations, CrowdStrike Intelligence attributes this activity with moderate confidence to the Iranian state-nexus adversary CHARMING KITTEN.



## Observed Activity Update: Monday, May 4

  * eCrime actors continue to use social engineering techniques and malicious documents referring to COVID-19. The most popular payload identified continues to be AgentTesla. This commodity [keylogger](https://www.crowdstrike.com/cybersecurity-101/attack-types/keylogger/) has been readily available for purchase on the internet since late 2014. It is customizable, can be calibrated by each user, can also be bound to another file so that when executed, and it gives the impression of being a legitimate executable rather than a malicious file. These are all elements that contribute to the continued popularity of the malware, and likely demonstrate why it has been one of the most readily distributed variants during the COVID-19 pandemic.
  * CrowdStrike Intelligence also observed activity from DOPPEL SPIDER, with a COVID-19-themed spam campaign to distribute DoppelDridex. The email included an attachment named using a pattern of `covid19_<0-9>{6}>.xls`. This Microsoft Excel file contained embedded Excel 4.0 macros.

While not novel, this campaign demonstrates how eCrime actors continue to use both COVID-19 themes and Excel 4.0 macro documents to deliver malware. This campaign was likely opportunistic in scope; identified targets spanned several sectors, including energy, financial services, manufacturing, professional services and retail. It is important to note that DOPPEL SPIDER often uses DoppelDridex infections to gain an understanding of their victims and assess their viability for [DoppelPaymer](/en-us/blog/doppelpaymer-ransomware-and-dridex-2/) ransomware operations.




## Observed Activity Update: Monday, April 27

  * A spam campaign distributing Hancitor used a COVID-19-related lure impersonating a U.S.-based health insurance company and referencing the purchase of a protection plan. A previous Hancitor campaign identified in March 2020 used a similar tactic. Malicious URLs included in the malspam emails hosted Microsoft Excel 4.0 documents containing macros, which triggered the retrieval and execution of Hancitor. The final payloads were identified as Pony and CRE Stealer.
  * On April 21, 2020, CrowdStrike Intelligence detected a phishing kit likely targeting UK-based victims. The kit used a lure referencing COVID-19 and prompted the visitor to enter personally identifiable information (PII), as well as passport details, marital status, and employment status. This information could almost certainly be used to conduct additional phishing attacks or to perform fraudulent activity.

  * CrowdStrike Intelligence has analyzed samples of the COVID-19-themed Master Boot Record (MBR) locker CoViper and determined it possesses no significant destructive capabilities. The malware had been publicly reported as targeting civilian infrastructure entities in the Czech Republic.

  * Netwalker ransomware is developed and operated by the criminal adversary CIRCUS SPIDER. Netwalker ransomware has been actively used by criminal actors since September 2019; earlier names given to this ransomware family were Mailto, Koko, and KazKavKovKiz.

The use of COVID-19 lures and targeting entities in the healthcare sector indicate that the operators of Netwalker are taking advantage of the global pandemic in order to gain notoriety and increase their customer base. 
  * CrowdStrike Intelligence has obtained a malicious macro-enabled Microsoft Word document themed with COVID-19 content that delivers a KonniFTP downloader to victim hosts. CrowdStrike attributes the Konni family of malware to VELVET CHOLLIMA with moderate confidence, and it is likely the described document originated from this adversary. VELVET CHOLLIMA frequently makes use of current events in its lure documents. While this activity does not represent a significant deviation from the threat actor’s previous tactics, techniques or procedures (TTPs), this latest effort highlights that this DPRK adversary remains active.



## Observed Activity Update: Monday, April 20

  * eCrime actors continue to use social engineering techniques and malicious documents referring to COVID-19. Impersonation of the World Health Organization (WHO) remains a popular social engineering technique in phishing campaigns. CrowdStrike Intelligence recently observed a new campaign that used a spoof sender address (`WHO <eurohealthycities@who<.>int>`). The emails delivered the “AgentTesla” information stealer using an exploit document known as “Virgo.” AgentTesla has been one of the most popular final payloads delivered by eCrime adversaries using COVID-19-related lures. WHO did not send these emails, please read this [security alert ](https://www.who.int/about/cybersecurity)for more information.
  * On April 14, 2020, CrowdStrike Intelligence observed a spam campaign distributing Hancitor using a COVID-19-themed lure and Microsoft Excel 4.0 macro documents. The emails purported to be an “invoice message” related to a recent purchase of a COVID-19 protection plan with a link providing additional details. While this is not the first time Hancitor operators have been observed using a COVID-19-themed lure, it is the first time Excel 4.0 macro documents have been used. Similar to past campaigns, Hancitor continues to download final payloads of Pony and CRE Stealer.
  * A new malicious Microsoft Office Word document was identified:![screenshot of Russian text](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2020/03/April-20-update-Russian-1.png)



The translation is: “UN promised assistance to Kyrgyzstan in the fight against coronavirus.rtf.” This file displays Russian-language decoy content related to the Kyrgyzstan government's response to the global COVID-19 pandemic, copied from an April 6, 2020, press release posted on the official government of Kyrgyzstan website `www.president<.>kg`. This document delivers the Chinozy malware associated with an activity cluster tracked by CrowdStrike as StrangeVantage. Similar StrangeVantage activity has been observed by CrowdStrike Intelligence as recently as mid-March 2020. While this activity cluster is currently unattributed, it is assessed with moderate confidence as likely to be associated with China-nexus targeted intrusion operations.

## Observed Activity Update: Monday, April 13

  * On April 9, 2020, CrowdStrike Intelligence identified a phishing email using the spoofed sender alias WHO <eurohealthycities@who<.>int>, referring to the World Health Organization (WHO), which contained the subject “URGENT COVID-19 SUSPECTED AFFECTED VSL”. The World Health Organization (WHO) did not send this email, please read this [security alert ](https://www.who.int/about/cybersecurity)

for more information. 

The message contained two malicious attachments: an Excel Workbook named COVID 19 MEASURES.xlsm, and an Office document named DOCX.doc. DOCX.doc is a Virgo exploit document which exploits CVE-2017-0199 to run an embedded scriplet file. COVID 19 MEASURES.xlsm contains Visual Basic for Applications (VBA) macro code, which when enabled also downloads and runs a file. Both attachments download the same resource, http<:>//93.126.60<.>106/vDBAExRNFm.exe, which is the AgentTesla information stealer.
  * CrowdStrike Intelligence has recently observed an unattributed targeted intrusion activity cluster using Coronavirus 2019 (COVID-19) and Southeast Asia focused lures and themes to distribute the _Chinoxy_ malware implant in March 2020. This activity is tracked by CrowdStrike Intelligence under the StrangeVantage activity cluster; while currently unattributed, CrowdStrike Intelligence assesses with moderate confidence that the StrangeVantage activity cluster is likely associated with Chinese-nexus targeted intrusion operations. 

On March 17, 2020, the malicious document “President discusses budget savings due to coronavirus with Finance Minister.rtf” was submitted to a third-party virus scanning service. Following this submission, several malicious documents with Malaysian-language government decoy and lure content were also identified. While all three documents use vulnerabilities in the Microsoft Equation editor to deploy the Chinoxy implant, there are slight differences in execution and persistence mechanisms.
  * CrowdStrike Intelligence has identified incidents involving the likely malicious use of a publicly available penetration testing tool named Octopus. This tool is available on GitHub and is intended for use in legitimate red team operations. Octopus is a modular tool and includes functionality that allows users to carry out a range of actions on a victim machine. Identified incidents indicate malicious actors have likely been using Octopus since at least early 2020. CrowdStrike assesses it is highly likely this tool will continue to be used in malicious activity due to its public availability and functionality.

Follow-on research into malicious incidents using Octopus led CrowdStrike Intelligence to identify an Octopus PowerShell agent linked to network infrastructure associated with other malicious files. This Octopus agent was configured to communicate with the C2 IP address 212.71.248<.>46\. This IP address has also served as a C2 for two other files: a Microsoft Word document with malicious macros and a malicious executable which has yet to be identified.

The malicious document is named COVID-19 SAFETY TIPS.docm and contains a PowerShell Empire-based malicious macro.
  * On March 26, 2020, public reporting identified multiple Coronavirus Disease 2019 (COVID-19)- themed mobile threats targeting Android-based mobile users. CrowdStrike Intelligence has analyzed a number of these threats, including AdoBot and Cerberus, which aim to take advantage of the COVID-19 pandemic.



## Observed Activity Update: Monday, April 6

  * On March 27, 2020, a COVID-19-themed phishing campaign with the subject “COVID-19 UPDATE !!” was sent to victims, purportedly from the World Health Organization (WHO), with a malicious attachment named "Covid-19_UPDATE_PDF.7z." The 7-zip archive contained an executable sample of the information-stealing malware LokiBot (CSIT-17123). The World Health Organization (WHO) did not send this email; please read this [security alert ](https://www.who.int/about/cybersecurity)for more information.
  * On March 30, 2020, an unattributed adversary sent a phishing message using the spoofed sender alias CDC Health Alert, referring to the U.S. Centers for Disease Control and Prevention (CDC), which contained the subject "CDC-INFO-Corona Virus Viccine found." The message included an attached Gzip archive named "Covid-19 Vaccine.gz." This archive contains the commodity NanoCore RAT, which is widely available in the criminal underground.
  * On March 31, 2020, CrowdStrike Intelligence identified a second email impersonating the CDC to deliver NanoCore. The message body was apparently derived from a publication on the official CDC website. Instead of leveraging an attachment to deliver NanoCore, this email prompts recipients to "download the vaccine" from a Microsoft OneDrive link. The message body additionally advises victims to contact a UK phone number if needed: "If you have more question please sms or Whatsapp me on: on how to use the Vaccine." The use of a contact number is not common in criminal spam campaigns.
  * A lure website referencing COVID-19 (masry-corona<.>com) was identified in use during March 2020 by distributors of the Culebra Variant information stealer to attract internet visitors. The malware is commonly used to capture Latin-America-based banking customers’ credentials.
  * AgentTesla continued its capitalization on the COVID-19 pandemic by distributing a spam campaign purportedly from Group Life and Health with the subject “Important Notice to Our Corporate Clients & Partners - COVID -19.” The spam email contained the RAR archive attachment named "COVID-19 Communication to corporate Clients..rar." The archive file contained an executable file named "COVID-19 Communication to corporate Clients..exe." This executable is a sample of AgentTesla that communicates with the command-and-control (C2) server rajalakshmi<.>co.in.
  * CrowdStrike Intelligence has obtained several Korean-language exploit documents themed with information pertaining to the COVID-19 pandemic in the Republic of Korea (ROK). Upon execution, these documents attempt to deliver two previously unobserved payloads. The exploit used in this activity and the targeting of individuals likely in the ROK is congruent with previously observed Democratic People's Republic of Korea (DPRK) operations; however, the payloads do not have any direct technical overlaps with tools used by any tracked DPRK adversaries. CrowdStrike Intelligence assesses with moderate confidence that it is likely that these exploit documents were deployed by a DPRK-aligned group but does not attribute this new activity to a named adversary at the time of this writing.



## Observed Activity Update: Monday, March 30

  * CrowdStrike Intelligence identified scam emails spoofing the [World Health Organization ](https://www.who.int)(WHO) with requests for financial donations to the COVID-19 Solidarity Relief Fund. The emails copy legitimate communications from WHO regarding the fund, but list an adversary-controlled Bitcoin (BTC) wallet address for payment. The World Health Organization (WHO) did not send this email; please read this [security alert ](https://www.who.int/about/cybersecurity)for more information.
  * A malicious website (corona-virus-map<.>net) posing as a COVID-19 map was identified dropping SCULLY SPIDER’s DanaBot banking trojan. The web inject primarily targeted U.S.-based financial institutions.
  * On March 23, 2020, CrowdStrike Intelligence obtained a phishing message impersonating a U.S. government agency and using the subject line “COVID-19 - nCoV - Special Update - WHO.”

The message contained an attachment named “covid-19 - ncov - special update.doc.” When opened, this file exploits a vulnerability in Microsoft Equation Editor and subsequently issues a GET request to download a file located at http<:>//getegroup<.>com/file.exe that leads to a WarZone remote access tool (RAT) sample. This malware uses phantom101.duckdns<.>org for command and control. WarZone is a commercially available RAT commonly used by cybercriminals.
  * On March 23, 2020, a COVID-19-themed DNS hijacking campaign was identified that reportedly attempts to trick users into downloading Oski Stealer. By altering the DNS settings for D-Link and Linksys routers, users are directed to an actor-controlled site that claims WHO has released a COVID-19 information application.
  * Compromised versions of an Android application called “SM_Covid19” are being distributed to unsuspecting users. The hijacked versions allow for the download and execution of additional malicious code on a user’s device. The original app was developed by an Italy-based company to assist with applying social-distancing protocols during the COVID-19 pandemic.
  * CrowdStrike Intelligence identified a malicious Microsoft Office exploit document with Mongolian-language lure content uploaded to a third-party file-scanning service. When opened, the document displays decoy content bearing Mongolian Ministry of Foreign Affairs (MFA) letterhead, related to a COVID-19 press release by the People's Republic of China (PRC). CrowdStrike Intelligence currently assesses there is an even chance this activity is associated with the KARMA PANDA (aka MysticChess) adversary. Further retrospective analysis has also identified suspected KARMA PANDA activity as early as December 2019.

  * CrowdStrike Intelligence identified a COVID-19-themed lure document being used by VELVET CHOLLIMA to deliver its Konni implant. The file, titled “Keep an eye on North Korean cyber.doc,” uses macros in an attempt to contact C2 infrastructure. VELVET CHOLLIMA has used COVID-19-themed documents several times over the past few weeks and is likely taking advantage of this significant geopolitical event to entice its targets to open malicious documents and execute its malware.
  * Unspecified actors repeatedly targeted the website of Mexico’s official news agency, Notimex, and posted false information regarding the COVID-19 pandemic using the organization’s hijacked social media accounts. The Notimex website and social media account were restored as of March 23, 2020.




## Observed Activity Update: Monday, March 23

  * On March 23, 2020, public reporting announced that some European-based hospitals had fallen victim to a Netwalker ransomware (aka KazKavKovKiz, Mailto, Mailto2 and KoKo) incident. The incident reportedly began on March 22, 2020, and used Coronavirus Disease 2019 (COVID-19) lures.
  * Throughout March 2020, the RedLine information stealer has used COVID-19-themed spam purportedly originating from a project that simulates potential cures for diseases to evaluate their effectiveness.
  * A new TrickBot dynamic web inject was distributed targeting customers of Italy-based financial institutions. It is highly likely that this is a continuation of efforts by WIZARD SPIDER to capitalize on COVID-19 — the group has used COVID-19-themed lures during distribution. The new dynamic web inject is likely seeking to exploit the inevitable increase in online banking by Italian users during the current lockdown conditions.
  * On March 16, 2020, the Australian Cyber Security Centre (ACSC) [reported](https://www.staysmartonline.gov.au/alert-service/covid-19-scam-messages-targeting-australians) a text phishing scam claiming to offer advice on local COVID-19 testing facilities. Interacting with the URL within the text dropped the commodity banking trojan Cerberus via a malicious Android application package.
  * A Nemty ransomware (v2.6) sample was detected on March 18, 2020, targeting a government entity. The lure email spoofed the chief executive office of a healthcare organization and referenced an annual general meeting purportedly scheduled to discuss the pandemic.
  * On March 18, 2020, TWISTED SPIDER announced it will refrain from infecting medical organizations until the pandemic situation stabilizes. Other criminal actors are also reported to be avoiding infections of healthcare sector entities.
  * CrowdStrike Intelligence has observed ongoing MUSTANG PANDA activity since late February 2020 using lure content related to the COVID-19 pandemic. Observed incidents have used malicious shortcut files (LNK) to drop decoy documents in Chinese, English and Vietnamese.
  * CrowdStrike Intelligence anticipates that [hacktivism](/en-us/cybersecurity-101/threat-intelligence/hacktivism/), particularly in Latin America and Europe, is likely to spike during the global COVID-19 pandemic, judging from hacktivist operations over the past week. During the past year, rates of hacktivism in Latin America have already been higher than normal, due mostly to political unrest in much of the region. These campaigns are likely to increase as other protest options narrow, given that widespread demonstrations and other large gatherings are increasingly prohibited in order to slow the spread of the virus.



**Additional Resources**

****

****

****

****

****

**

**

  * _Read a blog on COVID-19 cybersecurity from[CrowdStrike CEO George Kurtz.](/en-us/blog/george-kurtz-addresses-coronavirus-cybersecurity-impact/)_
  * _Learn more about the cybersecurity challenges during COVID-19 and recommendations for securing your remote workforce in blogs by[CrowdStrike CTO Mike Sentonas](/en-us/blog/securing-a-remote-workforce-in-the-time-of-covid-19/) and [Chief Product and Engineering Officer Amol Kulkarni](/en-us/blog/new-programs-to-secure-remote-workers-during-covid19-crisis/)._
  * _Access resources to help you ensure the security of your organization and remote workers by visiting the[CrowdStrike COVID-19 resource webpage.](/en-us/covid19-cybersecurity/)_
  * _Watch an on-demand webcast featuring CrowdStrike Intelligence and endpoint security experts:[“Cybersecurity in the Time of COVID-19.”](/en-us/resources/crowdcasts/cybersecurity-in-the-time-of-covid-19/)_
  *  _Download the[CrowdStrike 2020 Global Threat Report.](/en-us/resources/reports/2020-crowdstrike-global-threat-report/)_



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)