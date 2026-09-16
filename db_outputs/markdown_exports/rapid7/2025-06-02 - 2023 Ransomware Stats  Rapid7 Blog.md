# 2023 Ransomware Stats | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/01/12/2023-ransomware-stats-a-look-back-to-plan-ahead/
- **Date :** 2025-06-02

---

![Screenshot-2024-01-10-at-11.18.46-AM.png](https://www.rapid7.com/cdn/images/blt6f4790aa92b52f13/683de877bc38b1bbe2477f33/Screenshot-2024-01-10-at-11.18.46-AM.png)

Last year was not a year for the faint of heart. Organizations of every size found themselves faced with [ransomware attacks](/fundamentals/what-is-ransomware/) at varying levels of sophistication, yet every one of them was damaging. And as we step into 2024, the first victims of ransomware attacks are already being reported. What can the 2023 ransomware stats tell us about the year that was, and how can we use them to plan for the year ahead?  


In this blog we will dissect the multifaceted dimensions of ransomware attacks observed in 2023, providing insights and looking a bit forward to what 2024 might bring. For our data analytics, we make use of publicly available data (like posts from the ransomware groups themselves) and 2023 ransomware incident data from our MDR team, both of which we’ve enriched with context from the data gathered in Rapid7 Labs.   


**The 2023 Ransomware Landscape**

Most ransomware groups have leak sites where they announce victims of their campaigns. These leak sites are a tactic to put more pressure on their victims to pay the ransom; if the ransom is not paid, they will leak the compromised data via that site. The frequency of posts is a good indicator of how often and which groups are active, but the ransomware landscape is larger than that.   


The number of unique ransomware families these groups utilized in 2023 decreased by more than half, from 95 new families in 2022 to 43 in 2023. This tells us that the “current” ransomware families and models are working/profitable and there's no need to develop something brand new.  


Our combined sources uncovered nearly 5200 reported ransomware cases throughout the course of 2023. In reality, we believe that number was actually higher because it doesn’t account for the many attacks that likely went unreported.  


Coveware, a security consulting firm, found that the [average ransom payment](https://www.coveware.com/blog/2023/10/27/scattered-ransomware-attribution-blurs-focus-on-ir-fundamentals) for Q3 2023 was $850,700 USD. That is only the amount paid for the ransom; the real costs for recovering of a ransomware incident are based on a range of factors that include:

  * Downtime
  * Damage to reputation
  * Lost business
  * Labour hours
  * Increased insurance coverage costs
  * Legal counseling and settlement fees



The same report mentioned a staggering 41% of victims opted to pay the ransom.

The below scatter plot shows the number of ransomware incidents attributed to the top 20 ransomware groups for 2023, based on leak site communications, public disclosures, and Rapid7 incident response data.  


![Top_20_groups_posts_frequency_High.png](https://www.rapid7.com/cdn/images/blt0a2290878ce5c6fb/683de8904c5a090bd65e0da1/Top_20_groups_posts_frequency_High.png)

Zooming in on the most active groups (supported by a large ecosystem of initial access brokers), the top 5 groups we identified are:  


  * Alphv aka BlackCat ransomware
  * BianLian
  * Cl0P
  * Lockbit(3)
  * Play  




The below polar-bar chart visualizes these groups’ frequency of postings per month on their leak sites:

![Screenshot-2024-01-10-at-3.08.36-PM.png](https://www.rapid7.com/cdn/images/blt1aba24c19034f627/683de8a5aaf620730879e0c0/Screenshot-2024-01-10-at-3.08.36-PM.png)

## 2023 Ransomware Attacks

Rapid7 Labs conducted an analysis of the 2023 ransomware attacks using data sourced from both external and internal reports. We compared the modus operandi of these attacks and mapped them out against the MITRE ATT&CK model. The results are visualized in the following diagram:

![Screenshot-2024-01-10-at-5.22.21-PM.png](https://www.rapid7.com/cdn/images/blt6269e33dba2c6b78/683de8bbabf2ade0e03c4644/Screenshot-2024-01-10-at-5.22.21-PM.png)

This diagram effectively encapsulates the common patterns and methodologies observed in the majority of ransomware attacks. It serves as a visual representation, outlining the sequence of steps typically followed by attackers from initial breach to final ransom demand. In our statistics, exploiting a public facing application and having a valid account are the top initial attack vectors we observed in ransomware-focused attacks in 2023.

## Ransomware Groups That Came and Went

In 2023, several ransomware groups ceased their operations or underwent significant transformations. Hive ransomware marked the year's start with its disruption in January. BlackByte, after briefly reappearing with a new white logo, went offline for the last two months of 2023.

Royal ransomware rebranded itself as Black Suit, as evidenced by the matching binaries.They took down their victim portal and started posting more on their Black Suit leak site.

Vice Society, another group, became inactive for over three months, taking down their main and backup leak sites.

NoEscape, previously known as Avaddon, executed an exit scam, further indicating the volatile and shifting landscape of ransomware groups in 2023. An "exit scam" is a fraudulent scheme where a business or individual collects funds or assets from customers or investors and then suddenly ceases operations, disappearing with the collected funds.

## Who To Watch For in 2024

We anticipate that the top 5 groups mentioned will still be active in 2024; however, during the course of 2023, new groups surfaced that are interesting to watch. In random order: Cactus, Rhysida, 8base, Hunters International, Akira, and the recently surfaced Werewolves group are those to keep an eye out for.

[**Read Rapid7's Ransomware Radar Report**](/research/report/ransomware-radar-report/) ▶︎

## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)