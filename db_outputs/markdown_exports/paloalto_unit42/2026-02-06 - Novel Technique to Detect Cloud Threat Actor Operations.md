# Novel Technique to Detect Cloud Threat Actor Operations

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/
- **Date :** 2026-02-06

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")



[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Novel Technique to Detect Cloud Threat Actor Operations

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 19 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Nathaniel Quist](https://unit42.paloaltonetworks.com/author/nathaniel-quist/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:February 6, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [API](https://unit42.paloaltonetworks.com/tag/api/)
    * [IAM](https://unit42.paloaltonetworks.com/tag/iam/)
    * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/)
    * [Muddled Libra](https://unit42.paloaltonetworks.com/tag/muddled-libra/)
    * [Silk Typhoon](https://unit42.paloaltonetworks.com/tag/silk-typhoon/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/?pdf=download&lg=en&_wpnonce=252a1929a6 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/?pdf=print&lg=en&_wpnonce=252a1929a6 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Novel%20Technique%20to%20Detect%20Cloud%20Threat%20Actor%20Operations&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Ftracking-threat-groups-through-cloud-logging%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Ftracking-threat-groups-through-cloud-logging%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ftracking-threat-groups-through-cloud-logging%2F&title=Novel%20Technique%20to%20Detect%20Cloud%20Threat%20Actor%20Operations "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ftracking-threat-groups-through-cloud-logging%2F&text=Novel%20Technique%20to%20Detect%20Cloud%20Threat%20Actor%20Operations "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Ftracking-threat-groups-through-cloud-logging%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Novel%20Technique%20to%20Detect%20Cloud%20Threat%20Actor%20Operations%20https%3A%2F%2Funit42.paloaltonetworks.com%2Ftracking-threat-groups-through-cloud-logging%2F "Share in Mastodon")



## Executive Summary

Cloud-based alerting systems often struggle to distinguish between normal cloud activity and targeted malicious operations by known threat actors. The difficulty doesn’t lie in an inability to identify complex alerting operations across thousands of cloud resources or in a failure to follow identity resources, the problem lies in the accurate detection of known persistent threat actor group techniques specifically within cloud environments.

In this research, we hypothesize how a new method of alert analysis could be used to improve detection. Specifically, we look at cloud-based alerting events and their mapping to the MITRE ATT&CK® tactics and techniques they represent. We believe that we can show a correlation between threat actors and the types of techniques they use, which will trigger specific types of alerting events within victim environments. This distinct, detectable pattern could be used to identify when a known threat actor group compromises an organization.

To prove this method of alert analysis, Unit 42 researchers focused on two known threat actor groups that use two fundamentally different types of operational techniques to compromise their victims’ cloud environments. These groups are the cybercrime group [Muddled Libra](https://unit42.paloaltonetworks.com/tag/muddled-libra/) and the nation-state group [Silk Typhoon](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/silk-typhoon). Both threat actor groups are known to target cloud operations.

  * We analyzed cloud alerting events across 22 industries between June 2024 and June 2025.
  * The research was conducted by pairing the cloud-related MITRE ATT&CK techniques known to be used by Muddled Libra and Silk Typhoon with the specific security alerts they are known to trigger in cloud environments.



The test confirmed, as you will see within the remainder of this article, that security teams can successfully distinguish unique alerting patterns between Muddled Libra and Silk Typhoon based solely on the types of alerts observed.

Additionally, the results show a clear link between threat actors’ cloud-focused operations and the industries those groups target. Therefore, at times when one of the groups was known to be attacking certain industries, we can see those patterns appear in our data.

The confirmation that our detection method works as expected opens the door to the possibility of automated prevention capabilities for complex cloud architectures.

Cortex Cloud is designed to detect and prevent the malicious operations, configuration alterations and exploitations discussed in this article, by associating events with MITRE tactics and techniques. These capabilities help organizations to maintain runtime detection of events.

Organizations can gain help assessing cloud security posture through the [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/resources/datasheets/unit-42-cloud-security-assessment).

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Muddled Libra](https://unit42.paloaltonetworks.com/tag/muddled-libra/) (related to [**Scattered Spider**](https://unit42.paloaltonetworks.com/tag/scattered-spider/)**)** , [API](https://unit42.paloaltonetworks.com/tag/api-attacks/), [IAM](https://unit42.paloaltonetworks.com/tag/iam/)**  
---|---  
  
## Another Lens on Cloud Alert Trends

Following our previous article on [cloud alert trends](https://unit42.paloaltonetworks.com/2025-cloud-security-alert-trends/), we conducted another analysis of cloud alert statistics.

As part of the effort to determine whether we could identify threat groups, this time we analyzed the data in terms of the industries in which cloud alerts were triggered. Adding industry telemetry to the analysis allowed us to focus our efforts on identifying the techniques, and thus the resulting alerts, used by these threat actors as a control parameter. Using alert data pulled between June 2024 and June 2025, we identified the industries that saw the highest number of unique alert types as well as the highest average number of daily alerts. We then correlated these trends with the activities and targets of two threat groups: Muddled Libra and Silk Typhoon.

This article presents our analysis of Muddled Libra and Silk Typhoon operational techniques and the associated alert analysis.

## Glossary: Mapping Techniques to Alerts

The research was conducted by analyzing cloud-related MITRE ATT&CK techniques known to be used by Muddled Libra and Silk Typhoon and pairing them with the specific security alerts they are known to trigger in cloud environments. The following glossary will assist readers in understanding the results we present.

  * **Mapping MITRE Techniques to Alerts:** A single MITRE technique can potentially trigger multiple unique security alerts, and conversely, a single alert can map to one or more MITRE techniques and tactics. For example, the alert Remote command line usage of serverless function’s token in the Cortex Cloud platform correlates to the MITRE tactic [Credential Access](https://attack.mitre.org/tactics/TA0006/), and the MITRE techniques [Steal Application Access Token](https://attack.mitre.org/techniques/T1528/) and [Unsecured Credentials](https://attack.mitre.org/techniques/T1552/).
  * **Unique Alert Count:** We counted each alert rule only once for the basis of this research. For example, we identified nearly 70 different unique alerting rules that could be attributed to at least one of the 11 different cloud-related MITRE techniques known to be used by Muddled Libra. For Silk Typhoon, we found just over 50 unique alerting rules that could be attributed to at least one of their 12 known cloud-related MITRE techniques. Additionally, we found that only three unique alert rules were present in both Muddled Libra and Silk Typhoon alert rule sets. In some cases, these alerting rules triggered multiple times within our data across multiple organizations, but when we refer to unique alerts within an industry, we are only considering whether an alert triggered at all during the specified period.
  * **Average Daily Occurrences:** If a threat actor used the MITRE technique [Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/) (T1530), one of the resulting unique Cortex alert rules might be Suspicious identity downloaded multiple objects from a bucket. If this alert is triggered 1,000 times in a single day, it counts as a single unique alert, but the 1,000 occurrences of that alert in that day will be calculated in the average daily occurrences. When we report average alerts per day by industry in the article below, we take the average for each organization within that industry vertical.



To use a metaphor to help explain how we considered alerts, if each alert rule was a type of fruit, we would see that Muddled Libra holds a very different basket of fruit than Silk Typhoon does. In fact, the baskets are so diverse, that out of the nearly 70 different types of fruit Muddled Libra has, and the more than 50 different types of fruit Silk Typhoon has, they only have 3 types of fruit in common.

When we look at alerts triggered within an industry, we might see a variety of fruit scattered about — maybe 10 oranges, 14 lemons and so on. When we analyze the fruit trail in terms of the types of fruit found within a particular industry, compared with the types of fruit found in the baskets we know Muddled Libra or Silk Typhoon to be holding, we can make a reasonable determination of which threat actor was involved.

## Methodology

We collected alerts between June 2024 and June 2025 that were triggered on a combination of platforms, including:

  * Cloud service providers
  * Container environments
  * Cloud-hosted applications
  * SaaS platforms



We then analyzed the alerts based on their unique naming, originating platform, alert date and metadata such as:

  * Industry
  * Region
  * Frequency of occurrence
  * Average number of occurrences in each organization



As described above, we integrated the correlation of the MITRE ATT&CK framework, by pairing each alert with its corresponding MITRE technique.

We also analyzed the correlation between the targeted organization’s industry and region and the severity level of the alerts they experienced. This helped to identify the types of alerts that are more likely to occur, based on these factors.

## Threat Actor Profiles

### Muddled Libra

#### Background

[Muddled Libra](https://unit42.paloaltonetworks.com/muddled-libra/) (also known as Scattered Spider, or UNC3944) is a cybercrime group that has been active since 2021.

Known for its use of [social engineering](https://unit42.paloaltonetworks.com/2025-unit-42-global-incident-response-report-social-engineering-edition/), including making calls to organizations’ help desks, Muddled Libra has also been known to partner with ransomware-as-a-service (RaaS) programs. By continually [updating its approach](https://unit42.paloaltonetworks.com/muddled-libras-strike-teams/), the group has successfully used social engineering techniques, including smishing (SMS phishing), vishing (voice phishing) and spear phishing (directly targeting an employee).

Upon successfully compromising an organization, the group uses several tools, including ransomware variants such as [DragonForce](https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-and-partners-release-updated-advisory-scattered-spider-group) – a subscription-based RaaS framework created by a group of the same name, tracked by Unit 42 as Slippery Scorpius. The group also [uses cloud enumeration tools](https://www.halcyon.ai/blog/scattered-spider-tactics-observed-amid-shift-to-us-targets) such as [ADRecon](https://github.com/sense-of-security/ADRecon), an open source Active Directory reconnaissance tool.

#### Targeted Industries and Techniques

While [Muddled Libra’s](https://unit42.paloaltonetworks.com/threat-group-assessment-muddled-libra-2024/) targeted industries have evolved since 2022, the following sectors have been consistently reported:

  * Aerospace and defense
  * Financial services
  * High technology
  * Hospitality
  * Media and entertainment
  * Professional and legal services
  * Telecommunications
  * Transportation and logistics
  * Wholesale and retail



Muddled Libra employs multiple offensive [techniques](https://attack.mitre.org/groups/G1015/) to compromise and maintain access within a victim’s environment. We analyzed the group’s known techniques, and extracted those techniques that specifically focus on cloud infrastructure, as Table 1 shows. Together, these form a sort of “fingerprint” that we can use to identify the group within cloud alert data.

**MITRE Tactics** | **MITRE Techniques** | **MITRE Technique Name**  
---|---|---  
Collection | [T1530](https://attack.mitre.org/techniques/T1530/) | Data from Cloud Storage  
Defense Evasion | [T1578.002](https://attack.mitre.org/techniques/T1578/002/) | Modify Cloud Compute Infrastructure: Create Cloud Instance  
Defense Evasion, Persistence, Privilege Escalation, Initial Access | [T1078.004](https://attack.mitre.org/techniques/T1078/004/) | Valid Accounts: Cloud Accounts  
Discovery | [T1069.003](https://attack.mitre.org/techniques/T1069/003/) | Permission Groups Discovery: Cloud Groups  
Discovery | [T1087.004](https://attack.mitre.org/techniques/T1087/004/) | Account Discovery: Cloud Account  
Discovery | [T1526](https://attack.mitre.org/techniques/T1526/) | Cloud Service Discovery  
Discovery | [T1538](https://attack.mitre.org/techniques/T1538/) | Cloud Service Dashboard  
Discovery | [T1580](https://attack.mitre.org/techniques/T1580/) | Cloud Infrastructure Discovery  
Lateral Movement | [T1021.007](https://attack.mitre.org/techniques/T1021/007/) | Remote Services: Cloud Services  
Persistence, Privilege Escalation | [T1098.001](https://attack.mitre.org/techniques/T1098/001/) | Account Manipulation: Additional Cloud Credentials  
Persistence, Privilege Escalation | [T1098.003](https://attack.mitre.org/techniques/T1098/003/) | Account Manipulation: Additional Cloud Roles  
  
Table 1. Known Muddled Libra cloud tactics and techniques.

#### Methodology Walkthrough

Even though each MITRE Technique is relatively granular in terms of scope of operation, there can be multiple types of computational events from a cloud platform or software-as-a-service (SaaS) application which can fall under the purview or scope of a single MITRE technique.

For example, the MITRE technique T1078.004 - Valid Accounts: Cloud Accounts is focused on the operational event of a valid cloud account. This can have a wide scope in the types of event which can be counted, such as:

  * Unusual resource modification from a newly seen IAM user
  * Deletion of multiple cloud resources by a newly created IAM role
  * A suspicious identity created or updated password for an IAM user



Each of these can be linked to a valid cloud account but each one could have vastly different root causes.

Additionally, when looking specifically at an individual alert type, such as Unusual resource modification from a newly created IAM role, this event could be considered to align not only with the MITRE tactic Initial Access, but it could also align with the MITRE tactics Defense Evasion or even Persistence.

When we expanded our scope to include potential alerting events that could be triggered by any of the MITRE techniques known to be used by Muddled Libra, we found nearly 70 alerting events that could be attributed to at least one of these MITRE techniques.

We collected all of these alerts, which were associated with each of the MITRE techniques known to be used by Muddled Libra. We then distilled those alerts to identify the number of unique alerts that were present within each industry. We also tracked the number of average daily occurrences for each organization within those industries. To use our fruit analogy, we identified the number of unique fruit that the threat actors left at each respective industry (unique alerts), then we also counted how many of each fruit type were present at each organization within that industry (average alert count).

As explained in the Glossary section, we were able to use these numbers to build patterns.

#### Industry and Technique Analysis

Comparing the triggered alerts and their associated MITRE techniques with the targeted industries shows a correlation between the industries targeted according to public reports and the alerts triggered by Muddled Libra operations. Figure 1 shows this correlation by ranking industries from the highest to the lowest based on the number of unique alerts related to the MITRE techniques listed within Table 1, between June 2024 and July 2025. Industries that were publicly reported as targeted are shown in red.

![Bar chart titled "Muddled Libra Unique Alerts" displaying various sectors on the vertical axis and alert counts on the horizontal. "HighTechnology" leads with the highest alerts, followed by "Wholesale & Retail Trade" and "Financial Services." The chart continues with sectors like "Real Estate" and "Federal Government" showing fewer alerts. Bars are colored red and blue where red indicates Muddled Libra.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/chart-10-scaled.png)Figure 1. Count of unique alerts by industry from June 2024-June 2025. Red bars indicate the industries publicly reported as targeted by Muddled Libra.

Figure 2 shows the average daily number of alerts that occurred during the same timeframe.

![Bar chart displaying average alerts per day across various industries. X-axis lists industries such as Transportaion and Logistics, Pharmaceuticals and Life Sciences, Retail, and Telecommunications. Y-axis ranges from 0 to 8 alerts. Bars in blue and red vary in height, with the highest being Transportaion and Logistics at 7 alerts and the lowest being Media and Entertainment at 2 alerts.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/chart-2-2-scaled.png)Figure 2. Count of the average daily alerts by industry from June 2024-June 2025. Red bars indicate the industries publicly reported as targeted by Muddled Libra.

Figure 2. Count of the average daily alerts by industry from June 2024-June 2025. Red bars indicate the industries publicly reported as targeted by Muddled Libra.

While the highest volume of unique alerts (shown in Figure 1) aligns perfectly with Muddled Libra’s most-reported targets — specifically high technology, wholesale and retail, financial, and professional and legal services—the presence of a number of signature alerts in other sectors shouldn't be ignored. When an industry like manufacturing or pharma and life sciences or state and local government shows a significant subset of Muddled Libra’s "fingerprint" (for instance, 16 or more unique alert types), it suggests the group could have an active interest in these environments even if we haven’t seen headlines about it. Security teams in these "middle-tier" industries should treat these clusters of unique alerts as early warning signs that these industries are witnessing a significant number of the group's known operational techniques.

The unique alert data (Figure 1) should be considered alongside average daily alert data (Figure 2) to distinguish between a threat actor’s strategic breadth and their operational persistence. For instance, transportation and logistics serves as a primary example of high-intensity targeting; it ranks sixth in unique alert variety but first in average daily volume, showing a 25% spike in unique alerts in June 2025 alone. This combination indicates that Muddled Libra is not only using a wide array of its signature techniques in this sector but is doing so with higher frequency. We will take a deeper dive into transportation and logistics in the next section.

In contrast, telecommunications and media and entertainment were some of the first and most frequent targets of Muddled Libra in 2022 and 2023, but their standings as the last two positions for average daily alerts in 2024-2025 suggest that these two industries in particular have experienced a saturation effect. Namely, the targeting of these groups may be aging off. They no longer appear to be the key focus of the Muddled Libra actors. The other industries that could also fall into this category are hospitality and aerospace and defense.

For a defender, this data provides a threshold for proactive investigation. A high count of unique alerts (the "variety" of the fruit basket) typically signals a sophisticated, multi-stage intrusion attempt, whereas a high daily average (the "quantity" of fruit) may point to automated scanning or persistent credential stuffing. If your organization sees more than 10 unique Muddled Libra-associated alerts within a 30-day window, it is time to look deeper, regardless of whether your specific industry is currently "trending" in threat intelligence circles. The goal is to move from reactive patching to proactive defense by identifying these actor-specific patterns before they escalate to data exfiltration.

#### Focused Analysis: Aviation

Reports that Muddled Libra was [targeting the aviation industry](https://industrialcyber.co/transport/fbi-raises-alarm-over-scattered-spider-targeting-airline-sector-with-social-engineering-schemes/) initially surfaced in June 2025. Unit 42 does not track aviation as a singular category. Instead, aviation organizations appear under our transportation and logistics category.

When looking at the transportation and logistics industry alerts, we found an increase in the number of unique alerts based on the MITRE techniques used by Muddled Libra during this same timeframe.

It is important to note that here we are looking at the number of unique alert rules for this analysis and breaking this out by month, as opposed to the whole year view shown in Figure 1. We arrive at “unique alerts” for the industry by taking the average number of unique alerts seen for each organization tracked in that category over a monthly timeframe.

Figure 3 shows that the average number of unique alerts per organization in the transportation industry increased by 25% from May-June 2025. What makes this finding important is that Muddled Libra made several headlines during June 2025 for its operations targeting airline organizations.

![Bar chart that shows alerts from June 2024 to June 2025. Each month from June to May has 10-12 alerts in blue bars, and June has 15 alerts in a red bar, indicating Muddled Libra.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/chart-1-1-scaled.png)Figure 3. Unique alerts by month for the transportation industry. The bar for June is red because it is the period publicly reported to have the highest targeting of the aviation industry.

As illustrated in Figure 3, June 2025 saw the highest number of unique alerts for the transportation industry, with 15 unique alerts.

#### The Verdict on the Fingerprinting Effort

Looking at the correlation, there does appear to be a fingerprint capability that could be used as a detection pattern. This pattern could help organizations identify if they are potentially targeted and take mitigative steps. Additionally, this could also assist organizations in developing an early warning detection trigger. For example, if defenders witness an increase in the number of daily average occurrences alerts from known Muddled Libra techniques, this could indicate reconnaissance or discovery activity occurring against their infrastructure. This then provides an opportunity to proactively prepare for future operations.

#### Top 10 Alerts from Muddled Libra Techniques

Table 2 lists the top 10 alerts that we observed in association with Muddled Libra’s MITRE techniques.

**Alert Names** | **MITRE Techniques** | **Tactics**  
---|---|---  
Azure sensitive resources enumeration activity using Microsoft Graph API | [T1526](https://attack.mitre.org/techniques/T1526/) | Discovery  
Microsoft 365 storage services exfiltration activity | [T1530](https://attack.mitre.org/techniques/T1530/) | Collection, Exfiltration  
Multi region enumeration activity | [T1580](https://attack.mitre.org/techniques/T1580/) [T1535](https://attack.mitre.org/techniques/T1535/) [T1526](https://attack.mitre.org/techniques/T1526/) | Discovery  
Storage enumeration activity | [T1619](https://attack.mitre.org/techniques/T1619/) [T1530](https://attack.mitre.org/techniques/T1530/) [T1526](https://attack.mitre.org/techniques/T1526/) | Discovery, Collection  
Cloud Identity Queried Cost or Usage Information | [T1087.004](https://attack.mitre.org/techniques/T1087/004/) [T1580](https://attack.mitre.org/techniques/T1580/) | Discovery  
A cloud identity invoked IAM related persistence operations | [T1098](https://attack.mitre.org/techniques/T1098/) [T1136](https://attack.mitre.org/techniques/T1136/) [T1078.004](https://attack.mitre.org/techniques/T1078/004/) | Defense Evasion, Persistence, Privilege Escalation, Initial Access  
Cloud infrastructure enumeration activity | [T1580](https://attack.mitre.org/techniques/T1580/) [T1526](https://attack.mitre.org/techniques/T1526/) | Discovery  
Suspicious identity downloaded multiple objects from a bucket | [T1530](https://attack.mitre.org/techniques/T1530/) [T1020](https://attack.mitre.org/techniques/T1020/) | Collection, Exfiltration  
Suspicious cloud infrastructure enumeration activity | [T1580](https://attack.mitre.org/techniques/T1580/) [T1526](https://attack.mitre.org/techniques/T1526/) | Discovery  
ML model discovery | [T1526](https://attack.mitre.org/techniques/T1526/) | Discovery  
  
Table 2. The top 10 alerts associated with Muddled Libra’s MITRE techniques.

As outlined in Table 2, Muddled Libra has an extensive history of targeting Microsoft Azure [environments](https://techcommunity.microsoft.com/blog/microsoftsecurityexperts/octo-tempest-hybrid-identity-compromise-recovery/4166783) using [Graph API](https://learn.microsoft.com/en-us/graph/use-the-api), a RESTful API that enables access to Azure cloud resources. This type of activity correlates with the MITRE techniques used by Muddled Libra and the alerts triggered by their operations. The most frequent alert between June 2024 and June 2025, in relation to the MITRE techniques used by Muddled Libra, was resource enumeration using Microsoft Graph API. The next most common alert was for exfiltration activity from Microsoft 365 storage services. While discovery operations represented the bulk of the remaining alert types, collection and exfiltration operations were the second most frequent alert type.

### Silk Typhoon

#### Background

Silk Typhoon (also known as [HAFNIUM](https://www.microsoft.com/en-us/security/blog/2021/03/02/hafnium-targeting-exchange-servers/)) is a China-nexus threat actor group that has been in operation since at least 2021. This group has historically [exploited](https://unit42.paloaltonetworks.com/china-chopper-webshell/) multiple vulnerabilities on Microsoft Exchange Servers. In recent years, the group appears to be shifting targets towards [cloud environments](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/), using compromised credentials obtained via vulnerable public-facing VPN endpoints to move laterally through cloud environments. The group relies on remote monitoring and management (RMM) tools to maintain persistent access and leverages Microsoft’s Graph API to enumerate cloud resources.

#### Targeted Industries and Techniques

Cybersecurity researchers have identified that the industries most commonly targeted, primarily located within the U.S., include:

  * Education
  * High technology
  * Federal governments
  * Financial services
  * Nongovernmental organizations (NGOs)
  * Professional and legal services
  * State and local governments
  * Utilities and energy



Silk Typhoon has employed several offensive [techniques](https://attack.mitre.org/groups/G0125/) to compromise and maintain access within a victim’s environment. Using the same methodology that was employed during the Muddled Libra analysis above, we analyzed the techniques and identified those that focus on cloud infrastructure, as Table 3 shows. We found that between Silk Typhoon and Muddled Libra’s known employed technique usage, only three techniques were employed by both threat actor groups, T1530, T1078.004 and T1098.001. This provides a basis on which to compare and contrast the results between both groups’ operations and, more importantly, on the types of alerts witnessed by organizations in the industries they target.

**MITRE Tactics** | **MITRE Techniques** | **MITRE Technique Name**  
---|---|---  
Collection | [T1119](https://attack.mitre.org/techniques/T1119/) | Automated Collection  
Collection | [T1530](https://attack.mitre.org/techniques/T1530/) | Data from Cloud Storage  
Credential Access | [T1555.006](https://attack.mitre.org/techniques/T1555/006/) | Credentials from Password Stores: Cloud Secrets Management Stores  
Defense Evasion, Lateral Movement | [T1550.001](https://attack.mitre.org/techniques/T1550/001/) | Use Alternate Auth Material: Application Access Token  
Defense Evasion, Persistence, Privilege Escalation, Initial Access | [T1078.004](https://attack.mitre.org/techniques/T1078/004/) | Valid Accounts: Cloud Accounts  
Discovery | [T1619](https://attack.mitre.org/techniques/T1619/) | Cloud Storage Object Discovery  
Exfiltration | [T1567.002](https://attack.mitre.org/techniques/T1567/002/) | Exfiltration Over Web Service: Exfiltration to Cloud Storage  
Impact | [T1485](https://attack.mitre.org/techniques/T1485/) | Data Destruction  
Initial Access | [T1190](https://attack.mitre.org/techniques/T1190/) | Exploit Public-Facing Application  
Initial Access | [T1199](https://attack.mitre.org/techniques/T1190/) | Trusted Relationship  
Persistence | [T1136.003](https://attack.mitre.org/techniques/T1136/003/) | Create Account: Cloud Account  
Persistence, Privilege Escalation | [T1098.001](https://attack.mitre.org/techniques/T1098/001/) | Account Manipulation: Additional Cloud Credentials  
  
Table 3. Known Silk Typhoon cloud tactics and techniques.

#### Methodology Walkthrough

As a brief recap to the methodology of our research, we analyzed the types of alerting events that could be associated with each of the MITRE Techniques known to be used by Silk Typhoon. When we included potential alerting events that could be triggered by any of the MITRE Techniques known to be used by Silk Typhoon, we found just over 50 alerting events that could be attributed to at least one of these MITRE Techniques.

We collected all of these alerts and distilled those alerts to identify the number of unique alerts that were present within each industry and the number of average daily occurrences of those alerts for each organization within those industries.

To use the same analogy as above, we wanted to identify what types of fruit Silk Typhoon brought to the party, and how many pieces of fruit they typically deploy when attacking.

#### Industry and Technique Analysis

We compared the total number of unique alerts for each month from June 2024 to June 2025 with the industries from which those alerts were triggered. This comparison confirmed that we were able to see the “fingerprints” of Silk Typhoon in the alerts triggered in industries that the group was known to be targeting.

As mentioned, Silk Typhoon had just over 50 unique alerts associated with their known technique usage, where Muddled Libra had nearly 70.

In contrast, we saw higher numbers of unique alerts within each industry when examining our Silk Typhoon data than we did in our Muddled Libra data.

In other words, Silk Typhoon may be holding a basket with fewer types of fruit (50) than in Muddled Libra’s (70), but the threat actor seems to use more types from the basket in its operations (i.e. as many as 27 unique alerts as opposed to 22).

The graph in Figure 4 shows our observations of alerts by industry over the period studied.

![Bar chart showing various industries by unique alerts by industry. High Technology, Financial Services, and Wholesale and Retail have the highest alert counts. Other sectors like Federal Government and Real Estate show fewer alerts. Red bars indicate the industries publicly reported as targeted by Silk Typhoon.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/chart-3-1-scaled.png)Figure 4. Count of unique alerts and average daily alerts by industry. Red bars indicate the industries public reported as targeted by Silk Typhoon.![Bar chart displaying alert averages across various industries. The chart shows the Federal Government with the most alerts, followed by sectors like Agriculture, Pharma and Life Sciences, and High Technology. Healthcare, Media and Entertainment, and Real Estate have the fewest alerts. Bars are colored in red and blue where red indicates Silk Typhoon.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/chart-5-1-scaled.png)Figure 5. Count of the average daily alerts by industry. Red bars indicate the industries publicly reported as targeted by Silk Typhoon.

While the highest volume of unique alerts aligns with Silk Typhoon’s most-reported targets—specifically high technology, financial services, and professional and legal services—the presence of signature alerts in other sectors is equally telling. When an industry like wholesale and retail or manufacturing shows a significant subset of Silk Typhoon’s "fingerprint" (for instance, 18 or more unique alert types), it indicates that the group could be actively deploying their offensive techniques against these industry environments. This could be occurring even if public reporting is minimal or nonexistent at this date. Security teams in these "middle-tier" industries should treat these clusters of unique alerts as evidence that they are witnessing a broad spectrum of the group's known operational techniques, rather than isolated incidents.

The unique alert data for Silk Typhoon (Figure 4) should be considered alongside average daily alert data (Figure 5) to distinguish between a threat actor’s strategic breadth and their operational persistence. To return to our metaphor, Silk Typhoon holds a "basket" with fewer types of fruit (50) than Muddled Libra (70), but they tend to use more of what is in their basket at any given time. For example, we witnessed as many as 27 unique alerts in a single sector compared to Muddled Libra’s 22.

The federal government serves as a primary example for high-intensity targeting. This industry ranks last in the number of unique alerts, or rather in variety, ie. the "types of fruit" in its basket, but first in average daily volume, peaking at 7.28 alerts per day (the "quantity of fruits witnessed"). This suggests that while Silk Typhoon may use a narrower set of techniques against government targets, it deploys those specific tactics with relentless frequency. Conversely, high technology shows a "worst-of-both-worlds" scenario, ranking first in unique tactical variety and near the top for daily volume. This indicates campaigns that are both sophisticated and persistent.

Similar to our comments on unique alerts, when we see a high level of activity possibly related to the threat group, it may be worth defenders' threat hunting for other known alerts related to Silk Typhoon, out of an abundance of caution. High levels of average alert activity could signify threat groups trying to gain initial access, but not yet succeeding in deploying their full toolset.

For a defender, this data provides a threshold for proactive investigation: a high count of unique alerts (the "variety" of the fruit basket) typically signals a sophisticated, multi-stage intrusion attempt, whereas a high daily average (the "quantity" of fruit) may point to automated scanning or persistent exploitation of specific vulnerabilities. If an organization observes more than 10 unique Silk Typhoon-associated alerts within a month, it is time to look deeper, regardless of whether a specific sector is making headlines as a common target.

#### Top 10 Alerts from Silk Typhoon Techniques

Table 4 lists the alerts most commonly seen in relation to the MITRE techniques used by Silk Typhoon.

**Alert****Names** | **MITRE****Techniques** | **Tactics**  
---|---|---  
Microsoft O365 storage services exfiltration activity | [T1530](https://attack.mitre.org/techniques/T1530/) | Collection, Exfiltration  
Process execution with a suspicious command line indicative of the Spring4Shell exploit | [T1190](https://attack.mitre.org/techniques/T1190/) | Initial Access  
Storage enumeration activity | [T1619](https://attack.mitre.org/techniques/T1619/) | Discovery  
A cloud identity invoked IAM related persistence operations | [T1098](https://attack.mitre.org/techniques/T1098/) | Persistence, Privilege Escalation  
Suspicious identity downloaded multiple objects from a bucket | [T1530](https://attack.mitre.org/techniques/T1530/) [T1020](https://attack.mitre.org/techniques/T1020/) | Collection, Exfiltration  
Suspicious identity downloaded multiple objects from a backup storage bucket | [T1530](https://attack.mitre.org/techniques/T1530/) [T1020](https://attack.mitre.org/techniques/T1020/) | Collection, Exfiltration  
An identity performed a suspicious download of multiple cloud storage objects | [T1530](https://attack.mitre.org/techniques/T1530/) [T1020](https://attack.mitre.org/techniques/T1020/) | Collection, Exfiltration  
An identity performed a suspicious download of multiple cloud storage objects from multiple buckets | [T1530](https://attack.mitre.org/techniques/T1530/) [T1020](https://attack.mitre.org/techniques/T1020/) | Collection, Exfiltration  
Massive code file downloads from SaaS service | [T1530](https://attack.mitre.org/techniques/T1530/) | Collection  
Deletion of multiple cloud resources | [T1485](https://attack.mitre.org/techniques/T1485/) | Impact  
  
Table 4. The top 10 alerts associated with Silk Typhoon’s MITRE techniques.

As outlined in Table 4, collection and exfiltration techniques were the most common alerts associated with Silk Typhoon’s MITRE techniques. Microsoft 365 storage services exfiltration was the most frequently observed alert. Other alerts identified include cloud storage enumerations and suspicious downloads of cloud storage objects.

## Industry Cloud Alert Trends

Perhaps the most striking result of our research came to light when we compared general cloud alerting trends with the trends we discovered while performing the fingerprinting analysis of Muddled Libra and Silk Typhoon.

The industry of high technology was consistently the top ranked industry when considering general cloud alerting trends, as well as the two threat actor groups’ alerting trends. However, the remaining industries we studied did not follow a uniform pattern. As shown in Figure 6, we found that the order of the most targeted industries shifted when we only counted alerts from Muddled Libra and Silk Typhoon operations.

![Comparison of industry ranking shifts in unique cloud alerts for general trends versus Muddled Libra and Silk Typhoon operations.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/Flowchart-1-scaled.png)Figure 6. Ranking of the top industries by unique alert counts for all alerts, Muddled Libra and Silk Typhoon.

As stated above, the high technology industry is in first place across both threat actor group findings, as well as the top ranking industry when looking at all cloud alerts by industry.

However, the remaining industry ranks do not mirror the same results. Looking at the wholesale retail industry illustrates a key finding. This industry is the second highest for Muddled Libra alerting events and third highest for Silk Typhoon, but is 14th on the industry list for all alerts.

This indicates that the fingerprinting analysis on these alerting operations does not reflect the same pattern as the general noise of all alerting trends. It appears that the distinct operations performed by the threat actors against the industries they target carry their own unique trends.

## Conclusion

Our analysis confirms the capacity to leverage the alerts triggered as a fingerprint detection pattern for the malicious techniques used by Muddled Libra and Silk Typhoon. This distinct detection capacity offers a new pathway for organizations to implement predictive and proactive cloud defense strategies.

Our research successfully differentiated the MITRE tactic and technique operations used by Muddled Libra, notably the aviation industry’s 25% increase in the number of unique alerts compared to the previous month, and Silk Typhoon’s increased higher than average number of daily alerts within the Federal and State Government industry.

By identifying the alert patterns that each threat actor’s techniques have on the alerting events within cloud environments, threat researchers can identify the threat actors most likely to target certain industries using specific techniques. This can then help defenders to proactively prepare defenses against those types of threats. Through the analysis of threats based on the types of attack techniques they leverage, organizations can create a defense methodology built specifically for their industry vertical.

Proper implementation of these defense controls can be effective in defending against targeted threat actor scenarios through the creation of tailored defensive alerting. Additionally, these controls can provide the capability to detect early warning scenarios and techniques, such as initial access operations, enabling prevention operations to block malicious cloud operations before they escalate to execution, impact or exfiltration.

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

Cortex Cloud customers can help secure and protect their cloud environments through compliance guardrails, application security monitoring and prevention techniques and through the proper placement of Cortex Cloud [XDR endpoint agent](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection) and [serverless agents](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Premium-Documentation/Serverless-function-security) within a cloud environment. Cortex Cloud is designed to identify cloud events witnessed on cloud platforms, to protect cloud posture and runtime operations. By associating events with MITRE tactics and techniques, Cortex Cloud helps detect and prevent the malicious operations, configuration alterations and exploitations discussed within this article.

Organizations can gain help assessing cloud security posture through the [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/resources/datasheets/unit-42-cloud-security-assessment).

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

  * [Updated Advisory on Scattered Spider Group](https://www.cisa.gov/news-events/alerts/2025/07/29/cisa-and-partners-release-updated-advisory-scattered-spider-group) – U.S. Cybersecurity and Infrastructure Security Agency
  * [Scattered Spider Tactics Observed Amid Shift to US Targets](https://www.halcyon.ai/blog/scattered-spider-tactics-observed-amid-shift-to-us-targets) – Halcyon
  * [Silk Typhoon targeting IT supply chain](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/) – Microsoft
  * [HAFNIUM targeting Exchange Servers with 0-day exploits](https://www.microsoft.com/en-us/security/blog/2021/03/02/hafnium-targeting-exchange-servers/) – Microsoft
  * [Scattered Spider](https://attack.mitre.org/groups/G1015/) – MITRE
  * [MITRE Cloud Techniques](https://attack.mitre.org/matrices/enterprise/cloud/) – MITRE
  * [Cloud Threats on the Rise](https://unit42.paloaltonetworks.com/2025-cloud-security-alert-trends/) – Unit 42, Palo Alto Networks
  * [Muddled Libra Threat Assessment](https://unit42.paloaltonetworks.com/threat-group-assessment-muddled-libra-2024/) – Unit 42, Palo Alto Networks
  * [Muddled Libra - Further and Faster](https://unit42.paloaltonetworks.com/muddled-libra/) – Unit 42, Palo Alto Networks
  * [Threat Actor Groups Tracked by Palo Alto Networks Unit 42](https://unit42.paloaltonetworks.com/threat-actor-groups-tracked-by-palo-alto-networks-unit-42/) – Unit 42, Palo Alto Networks
  * [Active Exploitation of Multiple Zero-Day Microsoft Exchange Vulnerabilities](https://www.volexity.com/blog/2021/03/02/active-exploitation-of-microsoft-exchange-zero-day-vulnerabilities/) – Volexity



Back to top

### Tags

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")
  * [Muddled Libra](https://unit42.paloaltonetworks.com/tag/muddled-libra/ "Muddled Libra")
  * [Silk Typhoon](https://unit42.paloaltonetworks.com/tag/silk-typhoon/ "Silk Typhoon")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: The Shadow Campaigns: Uncovering Global Espionage ](https://unit42.paloaltonetworks.com/shadow-campaigns-uncovering-global-espionage/ "The Shadow Campaigns: Uncovering Global Espionage")

### Table of Contents

  *   * Executive Summary
  * Another Lens on Cloud Alert Trends
  * Glossary: Mapping Techniques to Alerts
  * Methodology
  * Threat Actor Profiles
    * Muddled Libra
      * Background
      * Targeted Industries and Techniques
      * Methodology Walkthrough
      * Industry and Technique Analysis
      * Focused Analysis: Aviation
      * The Verdict on the Fingerprinting Effort
      * Top 10 Alerts from Muddled Libra Techniques
    * Silk Typhoon
      * Background
      * Targeted Industries and Techniques
      * Methodology Walkthrough
      * Industry and Technique Analysis
      * Top 10 Alerts from Silk Typhoon Techniques
  * Industry Cloud Alert Trends
  * Conclusion
  * Additional Resources



### Related Articles

  * [ Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "article - table of contents")
  * [ The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "article - table of contents")
  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")



## Related Cloud Cybersecurity Research Resources

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026 #### [DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of automated detection. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Cloud_cybersecurity_research_Overview_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 14, 2026 #### [Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/ "cloud detection")
  * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/ "DevOps")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection")

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026 #### [DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of automated detection. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Cloud_cybersecurity_research_Overview_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 14, 2026 #### [Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/ "cloud detection")
  * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/ "DevOps")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection")

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026 #### [DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)