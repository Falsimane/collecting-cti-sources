# StealC Historical Bot Infection Special Report

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/stealc-historical-bot-infection-special-report/
- **Date :** 2026-06-25

---

# StealC Historical Bot Infection Special Report

June 25, 2026

Last week we [wrote about new activity](https://www.shadowserver.org/news/socgholish-compromised-wordpress-sites-special-report/) by our international Law Enforcement and private sector partners in [Operation Endgame](https://www.operation-endgame.com/) – the largest international operation ever undertaken to combat cyber crime enablers globally. The first part of that action to go public was the successful disruption of the SocGholish malware framework, which resulted in Shadowserver running a one-off [SocGholish Compromised WordPress Sites Special Report](https://www.shadowserver.org/what-we-do/network-reporting/critical-socgholish-compromised-wordpress-sites-special-report/) on 2026-06-18 that shared remediation data about ~1.4 million compromised legitimate WordPress sites with National CSIRTs (nCSIRTs) and network owners worldwide.

Yesterday (2026-06-24), the next episode of “Season 3.0” of Operation Endgame was [publicly announced,](https://www.europol.europa.eu/media-press/newsroom/news/global-cyber-strike-disrupts-socgholish-amadey-and-stealc-malware-networks) covering additional joint action taken by law enforcement from Canada (Royal Canadian Mounted Police – RCMP), Denmark (Danish Police – Politi), Germany ([Federal Criminal Police Office – BKA](https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2026/Presse2026/260624_Endgame.html)), the Netherlands ([National High Tech Crime Unit – NHCTU](https://www.politie.nl/nieuws/2026/juni/24/11-operatie-endgame-opnieuw-twee-infostealers-offline.html)), the United Kingdom (National Crime Agency – NCA), and the United States (Federal Bureau of Investigation – FBI), plus private partners including [Microsoft](https://blogs.microsoft.com/on-the-issues/2026/06/24/scaling-cybercrime-disruption-through-innovation-and-ai/), The Shadowserver Foundation, the Registrar of Last Resort (RoLR), [Bitsight](https://www.bitsight.com/blog/bitsight-aids-disruption-efforts-on-amadey-malware-and-stealc-malware), [ESET](https://www.welivesecurity.com/en/eset-research/eset-takes-part-operation-endgame-disrupt-amadey-stealc/), [IBM X-Force](https://www.ibm.com/think/x-force/stealc-you-later-proofpoint-x-force-support-operation-endgame-disruptions), [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/stealc-you-later-proofpoint-and-ibm-x-force-support-operation-endgame), Infoblox, NorthWave, Bitdefender, Have I Been Pwned (HIBP) and Spamhaus. International activity was coordinated by [Europol](https://www.europol.europa.eu/media-press/newsroom/news/global-cyber-strike-disrupts-socgholish-amadey-and-stealc-malware-networks) and [Eurojust](https://www.eurojust.europa.eu/news/operation-endgame-continues-international-coalition-takes-malware-offline).

The goal of this combined action was to disrupt the “assembly lines” cyber criminals use to launch ransomware, financial fraud, and make attacks on critical infrastructure. In a coordinated operation during the week of 15-19th June 2026, key elements of multiple criminal infrastructures behind ransomware and malware operations such as SocGholish, Amadey, and StealC were dismantled as part of this major public-private effort.

Outcomes included:

  * 326 servers and 142 domains were simultaneously actioned by law enforcement and private sector partners
  * Cyber criminal crypto assets valued at over 41 million EUR (47 million USD) were identified, flagged, and thereby restricted from use
  * 27 million stolen login credentials were recovered as part of the operation.



### **Cybercrime-as-a-Service Disruption**

The malware families targeted in this “season” of Operation Endgame were offered as Cybercrime-as-a-Service, enabling other cyber criminals to target victims – such as for use in deploying ransomware or exfiltrating data. They included:

  * **SocGholish** – a malware dropper/loader that allowed unauthorised parties to gain access to computer systems by distributing fake browser updates via compromised websites. Instead of the update, internet users inadvertently installed the malware. This approach was primarily executed by compromising legitimate WordPress sites and infecting them with malware. The unauthorised access was then exploited for further crimes, such as installing ransomware for the purpose of digital extortion. Details and data analysis was already [provided last week](/news/socgholish-compromised-wordpress-sites-special-report/), so won’t be repeated here again.
  * **StealC** – information stealing malware, one of the most pervasive and impactful threats across the cyber crime ecosystem. Spread through multiple attack vectors, this was primarily designed to extract sensitive information such as passwords, stored access data and digital identities from compromised computers, and to make them available for subsequent illicit use, especially data trading and fraudulent use. This can lead to theft of corporate virtual private network (VPN) credentials, single sign-on (SSO) tokens, and session cookies that could allow an attacker to bypass multi-factor authentication (MFA).
  * **Amadey** – a malware dropper/loader that was mainly disseminated through phishing campaigns. It thus served as the first link in a larger attack chain and was capable of introducing additional malware into compromised systems. The malware also had information stealer capabilities and could therefore retrieve sensitive data.



A new [Season 3.0 Episode 5 StealC “Grand Theft Info” video](https://www.operation-endgame.com/videos/S03E04_STEALC.mp4) covering this latest disruption activity was added to the [Operation Endgame website](https://www.operation-endgame.com/):

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260624_Op_Endgame_S03E04_StealC-1024x731.png)](https://www.operation-endgame.com/videos/S03E04_STEALC.mp4)

For StealC, clients of this criminal service (also called _affiliates_) purchase a Linux-based installer for the C2 panel, which is used to build malware samples and distribute them to steal sensitive data from victims. Microsoft and partners used a mix of civil court orders, domain seizures, registrations, and provider notifications to primarily tackle StealC’s US Command and Control (C2) domains. In parallel, Shadowserver and the Registrar of Last Resort (RoLR) worked with our international Law Enforcement partners to seize and sinkhole other non-US StealC C2 domains.

For more technical details about how these infostealers operated, and how to defend against them, see [Microsoft’s comprehensive write up](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/) and their Digital Crimes Unit Assistant General Counsel Steven Masada’s post about how Microsoft [scaled their disruption approach using AI](https://blogs.microsoft.com/on-the-issues/2026/06/24/scaling-cybercrime-disruption-through-innovation-and-ai/). Microsoft’s “John Doe” civil court orders are [available here](https://www.microsoft.com/en-us/corporate-responsibility/customer-security-trust/digital-crimes-unit/notice-of-pleadings/amadey-stealc/). For details of other private industry partners supporting technical activities, see the supporting StealC blog posts by [IBM XForce](https://www.ibm.com/think/x-force/stealc-you-later-proofpoint-x-force-support-operation-endgame-disruptions) and [ProofPoint](https://www.proofpoint.com/us/blog/threat-insight/stealc-you-later-proofpoint-and-ibm-x-force-support-operation-endgame).

### **New StealC Historical Bot Infections Special Report**

As part of this disruption operation, overnight (2026-06-24) we ran a new one-off [StealC Historical Bot Infection Special Report](/what-we-do/network-reporting/critical-stealc-historical-bot-infections-special-report/). The purpose is to notify system owners and nCSIRTs if a computer has been infected with the StealC information stealer malware, so they can change their stolen credentials and reduce their risk of data loss. Technical details about the content of that report and sample data can be found [here](/what-we-do/network-reporting/critical-stealc-historical-bot-infections-special-report/).

If you have received a StealC Historical Bot Infections Special Report from Shadowserver, and you need more information, please [contact us](https://www.shadowserver.org/contact/), and we can provide more details or put you in touch with the Law Enforcement investigating officers if required.

### **StealC Historical Bot Infections – Data Analysis**

Our new one-off StealC Historical Bot Infections Special Report contained information provided by the Dutch National High Tech Crime Unit (NHTCU) covering the period between 4th July 2025 and 16th June 2026. The Special Report covered **29,475,727** individual StealC information stealer events corresponding to **9,886,903 unique logins** and **9,624,328 unique password hashes** associated with **5,787,992 unique URLs** , stolen from **352,906 Windows computer names** belonging to **384,781 different hardware device IDs** with **364,057 unique victim IP addresses** , which were spread across 16,477 different Autonomous System Numbers (ASNs) in 231 countries or territories globally.

For each of the images inline, you can click it to view a higher resolution version.

The world maps below show the total number of IP-geolocated StealC Historical Bot Infections per county. Note that a relatively small number of IP addresses (6,967 of 364,425) do not IP-geolocate to a country, so the displayed number is slightly lower than the actual total:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260624_Stealc_Worldmap_Linear-1024x739.png)](/wp-content/uploads/2026/06/20260624_Stealc_Worldmap_Linear.png)

(_StealC Historical Bot Infections per country – linear scale._Link to[public Dashboard 2026-06-24](https://dashboard.shadowserver.org/statistics/combined/map/?date_range=other_value&day=2026-06-24&map_type=std&source=special&data_set=count&scale=lin&auto_update=on))__

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260624_Stealc_Worldmap_Log-1024x739.png)](/wp-content/uploads/2026/06/20260624_Stealc_Worldmap_Log.png)

(_StealC Historical Bot Infections per country – logarithmic scale._Link to[public Dashboard 2026-06-24](https://dashboard.shadowserver.org/statistics/combined/map/?date_range=other_value&day=2026-06-24&map_type=std&source=special&data_set=count&scale=log&auto_update=on))__

Looking at the data in a different way, the tree map below shows the relative ratio of StealC Historical Bot Infections:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260624_Stealc_Treemap-1024x486.png)](/wp-content/uploads/2026/06/20260624_Stealc_Treemap-scaled.png)

_(IP-geolocated StealC Historical Bot Infections _. Link to[public Dashboard 2026-06-24](https://dashboard.shadowserver.org/statistics/combined/tree/?date_range=other_value&day=2026-06-24&source=special&data_set=count&scale=log&auto_update=on))__

Data for credentials stolen by StealC usually contain a _URL_ field (the website a set of credentials is associated with), a _login_ field for that website (which could be a user name such as “johndoe”, an email address such as “john.doe@gmail.com”, or some other identifier such as a telephone number or numeric ID number) and a _password_ field. Focusing only on logins with the format _somestring@some.domain_ , which are therefore more likely to be an email address, it is clear that major email service providers are the top sources of domains for those email addresses (potentially suggesting compromised personal rather than business email addresses). There is then a very long tail with a lower number of compromised accounts per domain for a large number of different domains, including many individual business, education and government entities.

We can visualize the relative ratios of stolen credentials across users of different email services. Looking at the top 100 associated domains for those compromised email addresses (ensuring that any domains for individual non-email service provider victim organisations are labelled as _REDACTED)_ as a treemap it is clear that the major service providers dominate:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260624_StealC_Logins_Top100_Domains_Treemap-1024x546.png)](/wp-content/uploads/2026/06/20260624_StealC_Logins_Top100_Domains_Treemap.png)

_(Top 100 StealC Historical Bot Infections domains from email-like logins)_

The graph below shows more detail, with counts per top 100 domain (note – there are multiple probable variations of typos of gmail included in the data, highlighting that infostealer data can often be relatively noisy and error prone – for both cyber criminal actors and data analysts):

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260624_StealC_Logins_Top100_Domains_Graph-1024x540.png)](/wp-content/uploads/2026/06/20260624_StealC_Logins_Top100_Domains_Graph.png)

_(Top 100 StealC Historical Bot Infections domains from email-like logins _– logarithmic scale)__

The IP-geolocated locations of each StealC Historical Bot Infection can be displayed on heat maps (note that since there can be multiple malware infections installations active on/behind a single IP address, these visualizations show unique geolocated IP addresses and may, therefore, under-represent the actual distribution globally). For the entire world during the period between 4th July 2025 and 16th June 2026 and then by multiple regions:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_world_bmng_200407-test1-2px-1-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_world_bmng_200407-test1-2px-1.jpg)

_(IP-geolocated StealC Historical Bot Infections – Worldwide)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_eu_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_eu_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Europe)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_na_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_na_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – North America)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_sa_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_sa_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – South America)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_oc_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_oc_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – East Asia)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_af_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_af_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Africa)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_benelux_bmng_200404-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_benelux_bmng_200404-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – UK/Europe)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_sca_bmng_200407-test1-8px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_sca_bmng_200407-test1-8px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Scandinavia)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_us_bmng_200407-test1-8px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_us_bmng_200407-test1-8px.jpg)

_(IP-geolocated StealC Historical Bot Infections – USA)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_can_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_can_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Canada)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_ca_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_ca_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Central America)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_me_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_me_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Middle East)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_naf_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_naf_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – North Africa)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_in_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_in_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – India)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_cn_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_cn_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – China)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_jpkr_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_jpkr_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Japan/Korea)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_aunz_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/StealCStealC_Historical_Bot_Infections-20250704-20260616-winkel_tripel_aunz_bmng_200407-test1-6px.jpg)

_(IP-geolocated StealC Historical Bot Infections – Australia/New Zealand)_

If you have any questions, please[ contact us](https://www.shadowserver.org/contact/), although there may be limitations on what information can be shared at this time due to the ongoing LE investigations.

This activity is a another great example of the success that can be achieved in public/private partnerships when sustainable non-profit funding is available. Thank you to the UK [Foreign, Commonwealth and Development Office (FCDO)](https://www.gov.uk/government/organisations/foreign-commonwealth-development-office) and UK [Integrated Security Fund](https://www.gov.uk/government/organisations/uk-integrated-security-fund) (ISF) for supporting The Shadowserver Foundation’s public benefit mission in UK FY25-26, thereby enabling us to provide free support to our international Law Enforcement partners on another successful cyber crime disruption operation.

  * [Botnets](/topics/botnets/)
  * [Bots](/topics/bots/)
  * [Geo Locations](/topics/geo-locations/)
  * [Malware](/topics/malware/)
  * [Reports](/topics/reports/)
  * [Sinkholes](/topics/sinkholes/)
  * [Statistics](/topics/statistics/)
  * [Takedowns](/topics/takedowns/)
  * [Threat Intelligence](/topics/threat-intelligence/)



[« Back to News & Insights](/news-insights/)

### Recent Articles

  * #### [Shadowserver 2025: Highlights of the Year in Review](/news/shadowserver-2025-highlights-of-the-year-in-review/)

September 7, 2026

A review of Shadowserver’s 21st year as the world’s largest provider of free, timely, actionable, daily cyber threat… [Read more »](/news/shadowserver-2025-highlights-of-the-year-in-review/)

  * #### [Shadowserver Critical Community Infrastructure Cyber Resilience Project](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

August 5, 2026

The Shadowserver Critical Community Infrastructure (CCI) Project is designed to improve the cybersecurity posture of essential… [Read more »](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)