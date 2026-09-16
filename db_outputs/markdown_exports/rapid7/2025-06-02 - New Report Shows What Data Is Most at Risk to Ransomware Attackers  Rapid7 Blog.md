# New Report Shows What Data Is Most at Risk to Ransomware Attackers | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/06/16/new-report-shows-what-data-is-most-at-risk-to-and-prized-by-ransomware-attackers/
- **Date :** 2025-06-02

---

[Ransomware](/fundamentals/what-is-ransomware/) is one of the most pressing and diabolical threats faced by cybersecurity teams today. Gaining access to a network and holding that data for ransom has caused [billions](https://cybersecurityventures.com/global-ransomware-damage-costs-predicted-to-reach-250-billion-usd-by-2031/) in losses across nearly every industry and around the world. It has stopped critical infrastructure like [healthcare services](https://www.pewtrusts.org/en/research-and-analysis/blogs/stateline/2022/05/18/ransomware-attacks-on-hospitals-put-patients-at-risk) in its tracks, putting the lives and livelihoods of many at risk.

In recent years, threat actors have upped the ante by using “double extortion" as a way to inflict maximum pain on an organization. Through this method, not only are threat actors holding data hostage for money – they also threaten to release that data (either publicly or for sale on dark web outlets) to extract even more money from companies.

At Rapid7, we often say that when it comes to ransomware, we may all be targets, but we don't all have to be victims. We have means and tools to mitigate the impact of ransomware — and one of the most important assets we have on our side is data about ransomware attackers themselves. [[Rapid7 Ransomware Prevention Solution](/solutions/ransomware-prevention/)]

Reports about trends in ransomware are pretty common these days. But what isn't common is information about what kinds of data threat actors prefer to collect and release.

[A new report](/info/ransomware-data-disclosure-trends/) from Rapid7's Paul Prudhomme uses proprietary data collection tools to analyze the disclosure layer of double-extortion ransomware attacks. He identified the types of data attackers initially disclose to coerce victims into paying ransom, determining trends across industry, and released it in a first-of-its-kind analysis.

"Pain Points: Ransomware Data Disclosure Trends" reveals a story of how ransomware attackers think, what they value, and how they approach applying the most pressure on victims to get them to pay.

The report looks at all ransomware data disclosure incidents reported to customers through our Threat Command threat intelligence platform (TIP). It also incorporates threat intelligence coverage and Rapid7's institutional knowledge of ransomware threat actors.

From this, we were able to determine:

  * The most common types of data attackers disclosed in some of the most highly affected industries, and how they differ
  * How leaked data differs by threat actor group and target industry
  * The current state of the ransomware market share among threat actors, and how that has changed over time



## Finance, pharma, and healthcare

Overall, trends in ransomware data disclosures pertaining to double extortion varied slightly, except in a few key verticals: pharmaceuticals, financial services, and healthcare. In general, financial data was leaked most often (63%), followed by customer/patient data (48%).

However, in the [financial services sector](/blog/post/2022/05/10/whats-changed-for-cybersecurity-in-banking-and-finance-new-study/), customer data was leaked most of all, rather than financial data from the firms themselves. Some 82% of disclosures linked to the financial services sector were of customer data. Internal company financial data, which was the most exposed data in the overall sample, made up just 50% of data disclosures in the financial services sector. Employees' personally identifiable information (PII) and HR data were more prevalent, at 59%.

In the healthcare and pharmaceutical sectors, internal financial data was leaked some 71% of the time, more than any other industry — even the financial services sector itself. Customer/patient data also appeared with high frequency, having been released in 58% of disclosures from the combined sectors.

One thing that stood out about the pharmaceutical industry was the prevalence of threat actors to release intellectual property (IP) files. In the overall sample, just 12% of disclosures included IP files, but in the pharma industry, 43% of all disclosures included IP. This is likely due to the high value placed on research and development within this industry.

## The state of ransomware actors

One of the more interesting results of the analysis was a clearer understanding of the state of ransomware threat actors. It's always critical to know your enemy, and with this analysis, we can pinpoint the evolution of ransomware groups, what data the individual groups value for initial disclosures, and their prevalence in the "market."

For instance, between April and December 2020, the now-defunct Maze Ransomware group was responsible for 30%. This "market share" was only slightly lower than that of the next two most prevalent groups combined (REvil/Sodinokibi at 19% and Conti at 14%). However, the demise of Maze in November of 2020 saw many smaller actors stepping in to take its place. Conti and REvil/Sodinokibi swapped places respectively (19% and 15%), barely making up for the shortfall left by Maze. The top five groups in 2021 made up just 56% of all attacks with a variety of smaller, lesser-known groups being responsible for the rest.

## Recommendations for security operations

While there is no silver bullet to the ransomware problem, there are silver linings in the form of best practices that can help to protect against ransomware threat actors and minimize the damage, should they strike. This report offers several that are aimed around double extortion, including:

  * Going beyond backing up data and including strong encryption and network segmentation
  * Prioritizing certain types of data for extra protection, particularly for those in fields where threat actors seek out that data in particular to put the hammer to those organizations the hardest
  * Understanding that certain industries are going to be targets of certain types of leaks and ensuring that customers, partners, and employees understand the heightened risk of disclosures of those types of data and to be prepared for them



To get more insights and view some (well redacted) real-world examples of data breaches, [check out the full paper](/info/ransomware-data-disclosure-trends/).

_**Additional reading:**_

  * [_Complimentary GartnerⓇ Report "How to Respond to the 2022 Cyberthreat Landscape": Ransomware Edition_](/blog/post/2022/06/15/complimentary-gartner-report-how-to-respond-to-the-2022-cyberthreat-landscape-ransomware-edition/)
  * [ _3 Takeaways From the 2022 Verizon Data Breach Investigations Report_](/blog/post/2022/05/31/3-takeaways-from-the-2022-verizon-data-breach-investigations-report/)
  * [ _A Year on from the Ransomware Task Force Report_](/blog/post/2022/05/24/a-year-on-from-the-ransomware-task-force-report/)
  * [ _What's Changed for Cybersecurity in Banking and Finance: New Study_](/blog/post/2022/05/10/whats-changed-for-cybersecurity-in-banking-and-finance-new-study/)

  


## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)
  * [Threat Intel](/blog/tag/threat-intel/)