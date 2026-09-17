# Qakbot Historical Bot Infections Special Report

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/qakbot-historical-bot-infections-special-report/
- **Date :** 2023-09-08

---

# Qakbot Historical Bot Infections Special Report

September 8, 2023

As [covered in our previous blog post](https://www.shadowserver.org/news/qakbot-botnet-disruption/), on Tuesday 29th August 2023, the [US Department of Justice (DoJ)](https://www.justice.gov/usao-cdca/pr/qakbot-malware-disrupted-international-cyber-takedown) and [US Federal Bureau of Investigation (FBI)](https://www.fbi.gov/news/stories/fbi-partners-dismantle-qakbot-infrastructure-in-multinational-cyber-takedown), together with other global law enforcement partners, announced a disruption action against the [Qakbot](https://malpedia.caad.fkie.fraunhofer.de/details/win.qakbot) botnet.

This activity has been [widely reported](https://www.bleepingcomputer.com/news/security/how-the-fbi-nuked-qakbot-malware-from-infected-windows-pcs/) on, and involved the FBI deleting the Qakbot malware from infected victim computers under [US court order](https://www.justice.gov/usao-cdca/divisions/national-security-division/qakbot-resources) (to reduce the risk of further harm).

Since the Qakbot malware was deleted from the victim systems during this law enforcement action, the traditional sinkhole-based approach of detecting infected devices via observed command and control traffic, and then reporting these victim systems out to network owners and National CSIRTs for remediation, will not be possible.

However, as part of their operation, the FBI acquired a copy of the threat actor’s database of historical Qakbot infections, which covered the period July 2019 to August 2023. This database contains a record of over 700,000 discrete Qakbot bot infections, covering victims systems in 230 countries.

At the request of the FBI, The Shadowserver Foundation are sharing elements of this dataset with system defenders in the following manner:

  * **National CSIRTs** will receive a one-off ‘Special Report’ about historical Qakbot infected devices in their country, containing victim IP addresses and supporting meta data to allow system identification, filtered by geographical region. Shadowserver currently has 201 nCSIRTs in 175 countries and territories receiving our data globally, and are working to help countries who do not yet have a National CSIRT to develop that capability.
  * **Network owners** will receive a one-off ‘Special Report’ about historical Qakbot infected devices in their own networks of responsibility, containing victim IP addresses and supporting meta data to allow system identification. Over 8000 organizations are currently directly subscribed to Shadowserver’s [free data network reports](https://www.shadowserver.org/what-we-do/network-reporting/). This includes organizations responsible for more than 59% of IPv4 network space in the United States.



This [Qakbot Historical Bot Infections Special Report](/what-we-do/network-reporting/qakbot-historical-bot-infections-special-report/) will be disseminated overnight on September 7th 2023. The supporting web page for this Special Report can be found [here](/what-we-do/network-reporting/qakbot-historical-bot-infections-special-report/).

Anyone who has not yet signed up for Shadowserver’s [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/) can [subscribe and register their network space here](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/). If you sign up after the dissemination date, you can request a back dated Qakbot Historical Bot Infections Special Report for your network (or country, for new nCSIRTs).

This reporting is provided in partnership with the FBI, at no cost, as a public benefit service, and is part of [Shadowserver’s mission](https://www.shadowserver.org/what-we-do/) to make the Internet more secure for all users.

## **Secondary Malware Infections**

It is important to note that Qakbot has been used to drop additional malware on infected systems, so although the FBI have deleted live Qakbot infections, **other malware infections may still be active on these systems and require further local remediation efforts**. These victim systems may also have been used in historic or recent intrusions and ransomware incidents.

We are aware of cases where Qakbot was a secondary infection to Emotet and has been seen in conjunction with other criminal activity (such as the unauthorised deployment of Cobalt Strike, likely as a precursor to ransomware attacks). We therefore ask all recipients of these Special Report notifications to **not just consider Qakbot in their incident response activities, but also the possibility of secondary infections and/or indication of wider lateral movement**.

If you have received a Qakbot Historical Bot Infections Special Report and you need more information about a specific infection, please [contact us](https://www.shadowserver.org/contact/) and we can provide more details, or put you in touch with the law enforcement investigating officers, if required.

It should be noted that some IP addresses can be associated with multiple Qakbot infections over that time period. A subset of the recorded Qakbot “victims” are likely to actually be security researchers or sandbox systems, but these events have been included for completeness (hopefully, those people know who they are, and what they have been doing).

## **Qakbot Historical Bot Infections – Data Analysis**

We are publicly sharing some high level analysis of the Qakbot historical bot infections dataset from the period between July 2019 to August 2023. For each of the images below you can click on it to view a higher resolution version.

The world maps below show the total number of Qakbot infections logged per country:

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Worldmap_Linear-1024x670.png)](/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Worldmap_Linear.png)_(Qakbot infections per country – linear scale)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Worldmap_Log-1024x670.png)](/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Worldmap_Log.png)_(Qakbot infections per country – logarithmic scale)_

The IP-geolocated locations of each logged Qakbot infection (note that since there can be multiple bot infections behind a single IP address, these visualizations show unique geolocated IP addresses and may therefore under-represent the actual victim distribution globally):

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_world-2px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_world-2px.jpg)_(IP-geolocated Qakbot infections – Worldwide)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_us-8px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_us-8px.jpg)_(IP-geolocated Qakbot infections – USA)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_na-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_na-6px.jpg)_(IP-geolocated Qakbot infections – North America)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_ca-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_ca-6px.jpg)_(IP-geolocated Qakbot infections – Central America)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_sa-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_sa-6px.jpg)_(IP-geolocated Qakbot infections – South America)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_eu-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_eu-6px.jpg)_(IP-geolocated Qakbot infections – Europe)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_benelux-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_benelux-6px.jpg)_(IP-geolocated Qakbot infections – UK/Europe)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_sca-8px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_sca-8px.jpg)_(IP-geolocated Qakbot infections – Scandinavia)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_me-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_me-6px.jpg)_(IP-geolocated Qakbot infections – Middle East)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_af-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_af-6px.jpg)_(IP-geolocated Qakbot infections – Africa)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_cn-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_cn-6px.jpg)_(IP-geolocated Qakbot infections – East Asia)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_oc-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_oc-6px.jpg)_(IP-geolocated Qakbot infections – Oceania)_

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_aunz-6px-1024x626.jpg)](/wp-content/uploads/2023/09/Qakbot_Historic_Bot_Infections-20190719-20230824_aunz-6px.jpg)_(IP-geolocated Qakbot infections – Australia/New Zealand)_

Looking at the data in a different way, the tree map below shows the relative ratio of Qakbot infections logged per country to the total. Note that a small number (398) of IP addresses do not geolocate to a country, so the displayed number is slightly lower than the actual total:

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Treemap-1024x641.png)](/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Treemap.png)_(Qakbot infections per country)_

In chart form, the total number of Qakbot infections logged during the period July 2019 to August 2023, and the percentage of the total per country, was:

[![](https://www.shadowserver.org/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Top30_Countries_background-1024x890.png)](/wp-content/uploads/2023/09/20230824_Qakbot_Historical_Bot_Infections_Top30_Countries_background.png)

_(Qakbot infections and percentage of total per country)_

If you have any questions, please [contact us](https://www.shadowserver.org/contact/), although there may be limitations on what information can be shared at this moment due to the ongoing LE investigations.

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

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)