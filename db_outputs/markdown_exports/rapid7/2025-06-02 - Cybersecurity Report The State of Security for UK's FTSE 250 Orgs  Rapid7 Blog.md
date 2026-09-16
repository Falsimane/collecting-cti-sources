# Cybersecurity Report: The State of Security for UK's FTSE 250 Orgs | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/06/11/rapid7-releases-industry-cyber-exposure-report-ftse-250/
- **Date :** 2025-06-02

---

Today, Rapid7 released our third Industry Cyber-Exposure Report (ICER) examining the overall exposure of the companies listed in the FTSE 250 index. The FTSE 250 is a capitalisation-weighted index of organisations listed on the [London Stock Exchange](https://www.londonstockexchange.com/) maintained by the FTSE Group. The index is based on the 101st to the 350th largest companies, which account for nearly 12% of the UK GDP (as of April 2019), with aggregate employment reaching over 10 million individuals globally. Furthermore, over 50% of these organisations are incorporated in the UK, enabling the creation of a UK-centric view of exposure.

The report reveals that even among very large, mature, and well-resourced organisations, we see evidence of cybersecurity basics being missed or deployed insufficiently. This hints at the complexity and breadth required for a comprehensive security program, which is a never-ending challenge in which there is always more that can be done, constrained by limited resources and time, regardless of the size of the organisation. If this challenge cannot be comprehensively met by these very large, high-revenue organisations, just imagine how much worse it is for smaller organisations with far fewer resources to apply to security.

Sure, you might think smaller organisations are less likely to be targeted by attackers, but that’s probably not significantly the case. For one thing, everyone is a target for so-called untargeted “drive-by” attacks or [internet-wide malware infections, such as NotPetya](/blog/post/2017/06/27/petya-ransomware-explained/), now officially deemed the most costly cyberattack of all time.

In addition, many small- to medium-size businesses represent a very tasty target for attackers due to their intellectual property (for example, startups with cool new technology or techniques), relationship with their customers (for example, the HVAC vendor that had access to Target’s corporate network), or involvement in processing sensitive or financial data (for example, the many law firms that handle complex mergers and acquisitions between much larger companies).

The report highlights how hard it is for all organisations to adequately address cybersecurity, and the need for greater awareness of challenges and support from business leaders.

The key findings of the research report include the following:

  * FTSE 250+ organisations, on average, expose a public attack surface of 35 servers/devices, with many companies exposing over 1,000 systems/devices.
  * Of the appraised FTSE 250+ organisations, 231 (88%) have weak or nonexistent anti-phishing defences (i.e., DMARC) in the public email configuration of their primary email domains. This is the weakest anti-phishing showing of all the Rapid7 Industry Cyber-Exposure Reports (ICERs) to date.
  * SSL/TLS security is not enforced on the primary websites of 19% of FTSE 250+ organisations. This leaves visitors open to a wide array of common and potentially devastating attacks by adversaries in a position to modify web content as it is being transmitted.
  * All industry sectors had at least one organisation with malware infections, with Administrative and Professional organisations showing monthly signs of regular compromise. Incidents across industries ranged from company resources being co-opted into [denial-of-service (DoS) amplification attacks](/fundamentals/denial-of-service-attacks/) to signs of [EternalBlue-based campaigns](/blog/post/2017/04/18/the-shadow-brokers-leaked-exploits-faq/) similar to WannaCry and NotPetya.
  * Many organisations across industry sectors in the FTSE 250+ signal how many and which cloud service providers they use in their public domain name system (DNS) metadata, with 114 organisations using between two and seven cloud service providers. This information can be used to craft highly effective, targeted attacks, among other actions.
  * Severely vulnerable services such as Telnet and Windows SMB file-sharing were present in only a few organisations, which is positive. However, most organisations in every sector had serious issues with patch/version management of business-critical internet-facing systems.



## Exposure across our industry-focused threat reports

Having measured the exposure of organisations in three separate industry indices—The United States' Fortune 500 threat report, Australasia’s ASX 200 report, and our latest threat report focused on the United Kingdom’s FTSE 250 Index—it’s possible to do some comparisons across these lists.

While the distribution of individual industry sectors differs across the lists, in aggregate they each paint a fairly robust exposure picture. We can use the aggregate lists to get a feel for exposure by region.

### A web of exposure

Virtually every corporation has some sort of web presence, so we can use this knowledge to see how each index stacks up when it comes to maintaining current versions of some of the most widely used web servers: Apache, nginx, and IIS.

The release dates of Apache and nginx web servers can be used as a proxy for how well organisations keep current with this component of their internet-facing tech stacks. The older the component, the more technical debt is accumulated as the difficulty level of just “dropping in” a new version increases (sometimes substantially) over time.

FTSE 250+-member organisations appear to have the same version-maintenance profile of their [ASX 200](/blog/post/2019/03/11/rapid7-introduces-industry-cyber-exposure-report-asx-200/) cousins with a diverse array of exposed Apache and nginx servers. All three lists have fairly long tails, but Fortune 500 organisations seem to be stuck in the past in a much larger way than the other two indices.

![Web.png](https://www.rapid7.com/cdn/images/blt2efb71dd148b7b96/683de1c83323a54c1380a984/Web.png)

Three different features stand out for the Microsoft IIS server version view of this temporal technical debt. First, all sectors have seriously old versions of IIS attached to the public internet, which is absolutely not a good idea. Microsoft does not maintain any version of IIS below 7.0 as of the publication date of this report, and 7.0 sunsets in less than half a year.

The next feature is the common distribution profiles of IIS versions 7.0–8.5. There could be many reasons for this, such as a common deployment pattern for services such as webmail and SharePoint. Thankfully, Microsoft provides regular patches for vulnerabilities found in these versions.

The final noticeable feature is that both FTSE and ASX companies are better at keeping very current with IIS than their Fortune 500 counterparts.

![IIS.png](https://www.rapid7.com/cdn/images/bltf73533ebc815de8d/683de1ed65b8eaea1fcc8d37/IIS.png)

We’ve got tons more information on the FTSE 250+ industry sectors, including a fairly shocking statistic on the number of organisations that do not auto-upgrade website request to HTTPS from HTTP.

## Have a gander!

We’re excited to present another industry-centric view of exposure and continue to set our sights on other major indices of companies around the world to paint a more complete global, industry-centric picture of exposure. If you have a professional or personal interest in how UK companies handle their internet exposure, take a moment to grab the free report. Reading through it, you will learn:

  * The average cyber-exposure of the FTSE 250+, and how this statistic relates to baseline attack surface
  * Which industries are unwittingly spreading malicious traffic such as EternalBlue-based exploits and distributed denial-of-service (DDoS) amplification attacks
  * The exposure inherent in relying on third-party, cloud-based services
  * How far along UK companies are when it comes to DMARC-based anti-spoofing



## Article tags

  * [Research](/blog/tag/research/)
  * [Project Lorelei](/blog/tag/project-lorelei/)
  * [Project Sonar](/blog/tag/project-sonar/)