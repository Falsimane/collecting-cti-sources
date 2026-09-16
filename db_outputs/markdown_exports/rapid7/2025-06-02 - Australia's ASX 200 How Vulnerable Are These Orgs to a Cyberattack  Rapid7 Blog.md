# Australia's ASX 200: How Vulnerable Are These Orgs to a Cyberattack? | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/03/11/rapid7-introduces-industry-cyber-exposure-report-asx-200/
- **Date :** 2025-06-02

---

Today, Rapid7 released our second Industry Cyber-Exposure Report, examining the overall exposure of the ASX 200 family of companies. The ASX 200 is a market-capitalisation-weighted and float-adjusted stock market index of stocks listed on the Australian Securities Exchange. The index is maintained by [Standard & Poor's](https://www.spglobal.com/spdji/en/indices/equity/sp-asx-200/#overview) and is considered the benchmark for Australian equity performance. It is based on the 200 largest ASX-listed stocks, which together account for about 82% (as at March 2017) of Australia’s market capitalisation.

The report reveals that even among very large, mature, and well-resourced organisations, we see evidence of cybersecurity basics being missed or deployed insufficiently. This hints at the complexity and breadth required for a comprehensive security program, which is a never-ending challenge in which there is always more that can be done, constrained by limited resources and time, regardless of the size of the organisation. If this challenge cannot be comprehensively met by these very large, high-revenue organisations, just imagine how much worse it is for smaller organisations with far fewer resources to apply to security. Sure, you might think smaller organisations are less likely to be targeted by attackers, but that’s probably not significantly the case. For one thing, everyone is a target for so-called untargeted “drive-by” attacks or [internet-wide malware infections, such as NotPetya](/blog/post/2017/06/27/petya-ransomware-explained/), now officially deemed the most costly cyberattack of all time.

In addition, many small- to medium-size businesses represent a very tasty target for attackers due to their intellectual property (for example, startups with cool new technology or techniques), relationship with their customers (for example, the HVAC vendor that had access to Target’s corporate network), or involvement in processing sensitive or financial data (for example, the many law firms that handle complex mergers and acquisitions between much larger companies).

The report highlights how hard it is for all organisations to adequately address cybersecurity, and the need for greater awareness of challenges and support from business leaders.

The key findings of the research include the following:

  * ASX 200 organisations, on average, expose a public attack surface of 29 servers/devices, with many companies exposing 200–300+ systems/devices.
  * Severely vulnerable services such as Telnet and Windows file-sharing were not prevalent for the most part, which is positive. However, most organisations in every sector had serious issues with patch/version management of business-critical internet-facing systems.
  * Of the appraised ASX 200 organisations, 134 (67%) have weak or nonexistent anti-phishing defenses (i.e., DMARC) in the public email configuration of their primary email domains.
  * Every industry sector in the ASX 200 signals how many and which cloud service providers they use in their public domain name system (DNS) metadata, with 144 organisations using between two and five cloud service providers and some using 10 or more. This information can be used to craft highly effective, targeted attacks, among other actions.
  * All industry sectors had at least one organisation with malware compromises, with the Consumer Discretionary and Information Technology sectors showing daily signs of ongoing compromise. These compromises ranged from company resources being co-opted into denial-of-service (DoS) amplification attacks to signs of EternalBlue-based campaigns similar to WannaCry and NotPetya.



## Painting an international picture of cyber-hygiene

This is the second Rapid7 Industry Cyber-Exposure Report. Much of the methodology used in the ASX 200 edition parallels what was employed in the Fortune 500 edition, both of which build upon the foundational techniques used to produce the annual National Exposure Index (NEI) reports. The ASX 200 edition also includes a new section that illuminates the state of web server configuration and [vulnerability management](/solutions/vulnerability-management/) across industries.

Data from [Project Sonar](/research/project-sonar/) is used to evaluate exposure based on attack surface using raw numbers of internet-based services combined with a tally of insecure and obsolete protocols. Sonar’s [FDNS study](https://opendata.rapid7.com/sonar.fdns_v2/) provides all the raw data necessary for our researchers to dig through DNS TXT records to see which domains have DMARC configured, a control highlighted in the United Kingdom’s Active Cyber Defence program as one of the most effective ways to combat email spoofing used by phishers. Finally, our [Project Lorelei](/research/project-lorelei/) global network of honeypots lets us round out the exposure analysis by enumerating the extent of malicious and misconfigured connections we see coming from ASX 200 hosts and networks.

## Expanding exposure measurement capabilities with new methodologies

There are fewer ASX 200 organisations with named IP blocks both in total and percentage-wise than in the Fortune 500 list. When possible, the Rapid7 Labs team used similar name-based record linkage models to identify owned internet blocks, then used the results of the extensive FDNS queries—which were validated and expanded upon with the help of SecurityTrails—to directly identify owned assets and infer IP blocks that were likely tied directly to an ASX-member organisation. Once the record linkage, asset identification, and IP block inference was complete, it was merely a matter of picking apart the data collected from Sonar, Heisenberg, and our DNS crawlers and seeing what was happening in the largest, best-resourced companies on the Australian Securities Exchange.

The results of this new methodology are promising, as the report catalogued many diverse assets per organisation/industry and provided a comprehensive view into configuration and patch management practices for key internet-facing assets. The results are promising enough to use the new methodology as a starting point for future industry-focused exposure as we continue to examine the state of exposure across the globe.

## Dive in!

We’re excited to present another industry-centric view of exposure and are setting our sights on other major indices of companies around the world to paint a more complete global, industry-centric picture of exposure. If you have a professional or personal interest in how Australian companies handle their internet exposure, take a moment to grab the free report. Reading through it, you will learn:

  * The average cyber-exposure of the ASX 200, and how this statistic relates to baseline attack surface
  * Which industries are unwittingly spreading malicious traffic such as EternalBlue-based exploits and distributed denial-of-service (DDoS) amplification attacks
  * The exposure inherent in relying on third-party, cloud-based services
  * How far along Australian companies are when it comes to DMARC-based anti-spoofing



## Article tags

  * [Research](/blog/tag/research/)
  * [Project Sonar](/blog/tag/project-sonar/)
  * [Project Lorelei](/blog/tag/project-lorelei/)