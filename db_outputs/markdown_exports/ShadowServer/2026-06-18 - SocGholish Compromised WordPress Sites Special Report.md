# SocGholish Compromised WordPress Sites Special Report

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/socgholish-compromised-wordpress-sites-special-report/
- **Date :** 2026-06-18

---

# SocGholish Compromised WordPress Sites Special Report

June 18, 2026

We have previously [written about](https://www.shadowserver.org/search/?q=endgame) Shadowserver’s support for our international Law Enforcement and private sector partners in [Operation Endgame](https://www.operation-endgame.com/) – the largest international operation ever undertaken to combat cyber crime enablers globally, including discussing our live sinkholing of multiple malware families and running multiple one-off Special Reports to notify victims of historical infections from analyzed seized criminal infrastructure. So for brevity we will not re-cap [Operation Endgame Seasons 1.0, 2.0 and 3.0](https://www.shadowserver.org/news/rhadamanthys-historical-bot-infections-special-report/) again here.

### **Malicious Traffic Delivery via Compromised Legitimate WordPress Sites**

**RECOMMENDATION: All WordPress users should read this post and follow the guidance below.**

WordPress is the one of the most widely used platforms for deploying websites. [According to WordPress.org](https://en-gb.wordpress.org/about/features/), in June 2026, more than 43% of all Internet websites are powered by WordPress. It is particularly popular with individuals, community groups and small/medium enterprises worldwide.

The threat actors SocGholish (also known as DEV-0206, GOLD PRELUDE, Mustard Tempest, TA569 and UNC1543) compromise legitimate WordPress sites and use Traffic Direction/Distribution Systems (TDS) to redirect visitors to webinjects hosted there (sometimes referred to as “FakeUpdates” since they impersonate web browser updates) and trick end users into drive by downloading of malware. Since at least 2018, SocGholish have allegedly provided initial access to victims for cyber criminal groups such as the Russian[ Evil Corp](https://www.nationalcrimeagency.gov.uk/who-we-are/publications/732-evil-corp-behind-the-screens/file) (also known as Indrik Spider), who are associated with Zeus-variant and Dridex malware and are also associated with several large‑scale ransomware and money‑laundering operations, which resulted in being sanctioned multiple times by the [UK](https://www.gov.uk/government/news/uk-sanctions-members-of-notorious-evil-corp-cyber-crime-gang-after-lammy-calls-out-putins-mafia-state), [US](https://home.treasury.gov/news/press-releases/sm845) and [Australian](https://www.foreignminister.gov.au/minister/penny-wong/media-release/cyber-sanctions-imposed-russian-citizens-cybercrime) Governments (and the subject of the recent BBC World Service “[Cyber Hack” series](https://www.bbc.co.uk/programmes/w27vqsst)).

Legitimate WordPress sites have been compromised – possibly through password spraying (brute force guessing of common values); leaked or reused credentials; exploitation of vulnerabilities in the hosting platform, content management system (CMS) or installed plugins, themes or templates; data exfiltrated from credential stealing malware; or by exploiting third-party services used by the site. In this context, compromised means that usernames and passwords for the WordPress sites were confirmed to be in the possession of the SocGholish threat actors. Many WordPress instances have been modified to include criminal infrastructure operated by SocGholish.

The abuse also includes the use of a process known as “Domain Shadowing”. This is a technique where a threat actor gains access to the authoritative DNS provider or registrar account panel for a legitimate domain, and uses their access to quietly create additional subdomains beneath the main (“apex”) domain. These malicious subdomains are often given common host names that hide in plain sight and blend in with the domain owner’s legitimate DNS infrastructure, but will point to criminal-operated external malicious infrastructure – effectively piggybacking on a domain’s established reputation and making it harder for defenders to easily detect or block illicit activity.

### **SocGholish Disruption**

On June 18th 2026, Law Enforcement [announced](https://www.politie.nl/en/news/2026/juni/18/11-international-law-enforcement-initiate-hunt-on-malware-group-socgholish.html) another joint action week under the [Operation Endgame](https://www.operation-endgame.com/) banner. Officers from the [Netherlands (NHCTU),](https://www.politie.nl/en/news/2026/juni/18/11-international-law-enforcement-initiate-hunt-on-malware-group-socgholish.html) [Canada (RCMP)](https://rcmp.ca/en/news/2026/06/4354276), the [United States (FBI)](https://www.linkedin.com/posts/fbicyber_today-as-part-of-operation-endgame-the-activity-7473389516691587072-hE3f) and Germany (BKA), with support from Europol and Eurojust, as well as private sector partners such as [Infoblox](https://www.infoblox.com/blog/threat-intelligence/hot-take-operation-endgame-vs-socgholish/), [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation) and The Shadowserver Foundation, successfully targeted SocGholish’s criminal infrastructure – a key infection chain used by other cyber criminals. The outcomes included:

  * 14,971 compromised legitimate WordPress sites infected with SocGholish malware **remediated**
  * 106 servers and domains taken down worldwide, disrupting the SocGholish botnet
  * A new [Season 3.0 Episode 3 SocGholish “Don’t be Evil” video](https://www.operation-endgame.com/videos/S03E03_SOCGHOLISH.mp4) was added to the [Operation Endgame website](https://www.operation-endgame.com/)



### [![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260618_Op_Endgame_S03E03_SocGholish-1024x732.png)](https://www.operation-endgame.com/videos/S03E03_SOCGHOLISH.mp4)

### **New SocGholish Compromised WordPress Sites Special Report**

As part of the disruption operation, we have today (2026-06-18) run a new one-off [SocGholish Compromised WordPress Sites Special Report.](https://www.shadowserver.org/what-we-do/network-reporting/critical-socgholish-compromised-wordpress-sites-special-report) The purpose is to notify legitimate WordPress site owners if their site has been compromised, so they can change their credentials and remediate the problems. Technical details about the content of that report and sample data can be found [here](https://www.shadowserver.org/what-we-do/network-reporting/critical-socgholish-compromised-wordpress-sites-special-report).

If you have received a SocGholish Compromised WordPress Sites Special Report from Shadowserver and you need more information, please [contact us](https://www.shadowserver.org/contact/), and we can provide more details or put you in touch with the Law Enforcement investigating officers if required.

### **Advice for All WordPress Site Owners**

The Dutch police have removed backdoors and malware from 14,971 compromised legitimate WordPress sites infected with SocGholish malware. The owners of these sites have been informed, and they are urged to:

  * Immediately change their login credentials
  * Enable multi‑factor authentication (MFA/2FA)
  * Check for and delete any unknown additional WordPress accounts that have been added
  * Patch their WordPress site and keep their software and plugins up‑to‑date in the future



Many sets of compromised credentials were available to the threat actors. If you have a WordPress site but did not receive a notification, you can prevent yourself from becoming a victim in the future by still applying the above security steps.

We also recommend that you [subscribe](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/) to Shadowserver’s [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/) to ensure you are automatically informed of potential threats to your site.

For more technical information about how SocGholish’s criminal platform operated and its evolution over time, please read the detailed blogs by our operational partners [Infoblox](https://www.infoblox.com/blog/threat-intelligence/hot-take-operation-endgame-vs-socgholish/) and [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation).

### **Advice For Computer Users**

SocGholish is also known as “FakeUpdates”. Their malware is distributed via fake software updates, for example, for internet browsers. When someone installs a fake update, the malware opens a connection to the attackers, who subsequently gain access to the victim’s computer system. Using this initial access, even more dangerous software can then be installed.

Tips to prevent infection:

  * Never trust pop‑ups that appear in your web browser
  * Do not trust updates that are overly flashy and scream for immediate action
  * Ensure your virus scanner is updated and always have it enabled during the installation of new software
  * A genuine software update always comes from the official source, for example, via your system settings or the official app store. Avoid installing updates from unknown/untrusted/third party sources.



Watch the (translated) Dutch Police explainer video for end users on YouTube [here](https://www.youtube.com/watch?v=TL0im7xOwlk).

### **SocGholish Compromised WordPress Sites – Data Analysis**

Our new one-off SocGholish Compromised WordPress Sites Special Report contained information provided by the Dutch National High Tech Crime Unit (NHTCU) about 1,441,695 instances of compromised legitimate WordPress sites that were available for use by SocGholish between 2023-05-17 and 2026-05-25. The Special Report covered compromised legitimate WordPress sites hosted on 1,134,542 domains and 271,176 unique IP addresses, spread across 7,550 different Autonomous System Numbers (ASNs) in 187 countries or territories globally.

For each of the images inline, you can click it to view a higher resolution version.

The world maps below show the total number of IP-geolocated SocGholish Compromised WordPress Sites per county:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_Worldmap_linear-1024x742.png)](/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_Worldmap_linear.png)

_(IP-geolocated SocGholish Compromised WordPress Sites per country – linear scale. Link to[public Dashboard 2026-06-18](https://dashboard.shadowserver.org/statistics/combined/map/?date_range=other_value&day=2026-06-18&map_type=std&source=special&data_set=count&scale=lin&auto_update=on))_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_Worldmap_log-1024x742.png)](/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_Worldmap_log.png)

_(IP-geolocated SocGholish Compromised WordPress Sites per country – logarithmic scale. Link to[public Dashboard 2026-06-18](https://dashboard.shadowserver.org/statistics/combined/map/?date_range=other_value&day=2026-06-18&map_type=std&source=special&data_set=count&scale=log&auto_update=on))_

Looking at the data in a different way, the tree map below shows the relative ratio of SocGholish Compromised WordPress Sites. Note that a small number (24) of IP addresses do not IP-geolocate to a country, so the displayed number is slightly lower than the actual total:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_Treemap-1024x495.png)](/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_Treemap-scaled.png)

_(IP-geolocated SocGholish Compromised WordPress Sites. Link to[public Dashboard 2026-06-18](https://dashboard.shadowserver.org/statistics/combined/tree/?date_range=other_value&day=2026-06-18&source=special&data_set=count&scale=log&auto_update=on))_

Looking at the data from the perspective of which Top Level Domain (TLD) each domain belongs to, the treemap below shows the relative ratio of SocGholish Compromised WordPress Sites during the period 2023-05-17 and 2026-05-25 split by TLD:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_tld-treemap-1024x819.png)](/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_tld-treemap.png)

_(SocGholish Compromised WordPress Sites treemap by TLD)_

In chart form, the top 25 total number of SocGholish Compromised WordPress Sites during the period 2023-05-17 and 2026-05-25, and the percentage of the total per TLD, was:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260618_SocGholish_Top25Countries-1024x822.png)](/wp-content/uploads/2026/06/20260618_SocGholish_Top25Countries.png)

_(SocGholish Compromised WordPress Sites by TLD and percentage of total per top 25 country. Link to[public Dashboard 2026-06-18](https://dashboard.shadowserver.org/statistics/combined/visualisation/?date_range=other_value&day=2026-06-18&source=special&dataset=unique_ips&limit=100&group_by=geo&count_as=avg&vis_scale=lin&style=bar_chart&auto_update=on) (by unique IP address, not TLD)_

In grid form, the visualization below shows the number of SocGholish Compromised WordPress Sites during the period 2023-05-17 and 2026-05-25 split by TLD:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_tld-counts-columns-1024x747.png)](/wp-content/uploads/2026/06/20260618_SocGholish_Compromised_WordPress_Sites_tld-counts-columns.png)

_(SocGholish Compromised WordPress Sites grid by TLD)_

The IP-geolocated locations of each SocGholish Compromised WordPress Site can be displayed on heat maps (note that since there can be multiple WordPress installations active on a single IP address, these visualizations show unique geolocated IP addresses and may therefore under-represent the actual distribution globally). For the entire world during the period 2023-05-17 and 2026-05-25 and then by multiple regions:

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_world_bmng_200407-test1-2px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_world_bmng_200407-test1-2px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Worldwide)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_eu_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_eu_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Europe)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_na_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_na_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – North America)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_sa_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_sa_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – South America)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_oc_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_oc_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – East Asia)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_af_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_af_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Africa)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_benelux_bmng_200404-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_benelux_bmng_200404-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – UK/Europe)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_sca_bmng_200407-test1-8px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_sca_bmng_200407-test1-8px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Scandinavia)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_us_bmng_200407-test1-8px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_us_bmng_200407-test1-8px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – USA)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_can_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_can_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Canada)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_can_bmng_200407-test1-6px-1-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_can_bmng_200407-test1-6px-1.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Central America)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_me_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_me_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Middle East)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_naf_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_naf_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – North Africa)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_in_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_in_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – India)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_in_bmng_200407-test1-6px-1-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_in_bmng_200407-test1-6px-1.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – China)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_jpkr_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_jpkr_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Japan/Korea)_

[![](https://www.shadowserver.org/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_aunz_bmng_200407-test1-6px-1024x626.jpg)](/wp-content/uploads/2026/06/SocGholishSocGholish_Compromised_WordPress_Sites-20230517-20260525-winkel_tripel_aunz_bmng_200407-test1-6px.jpg)

_(IP-geolocated SocGholish Compromised WordPress Sites – Australia/New Zealand)_

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

  * #### [StealC Historical Bot Infection Special Report](/news/stealc-historical-bot-infection-special-report/)

June 25, 2026

On Wednesday 24th June 2026, international law enforcement partners announced additional successful cyber crime disruption… [Read more »](/news/stealc-historical-bot-infection-special-report/)