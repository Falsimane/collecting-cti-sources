# Research: Cyber Health of the FTSE 350 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2023/04/13/anarchy-in-the-uk-not-quite-a-look-at-the-cyber-health-of-the-ftse-350/
- **Date :** 2025-06-02

---

The [attack surface](/fundamentals/attack-surface/) of the United Kingdom's 350 largest publicly traded companies has—drum roll, please—improved. But it could be better. Those are the high level findings of the latest in Rapid7's looks at the cybersecurity health of companies tied to some of the globe's largest stock indices. This is the second time in more than two years that [we looked at the FTSE 350](/info/2023-ftse-350-cyber-attack-surface/) to gauge how well the entire UK's business arena is faring against cyber threats. Turns out, they've improved in that time, and are on par with the other big indices we've looked at, though in some specific places, there is definitely room for improvement.

We chose the FTSE 350 as a benchmark in determining the cyber health of UK businesses because they are by and large some of the largest companies in the country and are not as resource constrained as some other, smaller, companies might be. This gives us a pretty even playing field on which to analyze their health and extrapolate out to the overall health of the region. We've done this with several other indices (most recently the ASX 200) and find it works well to provide a snapshot of what's going on in the region.

In this report, we looked first at the overall attack surface of the FTSE 350 companies, broken down by industry. We also looked at the overall health of their email and web server security. All three areas showed improvement, as well as points for concern.

## Attack Surface

By and large, the attack surfaces of the companies that make up the FTSE 350 was quite limited and in line with other major indices around the world. But, when you look at the individual industries that make up the FTSE you start to see some red flags.

For instance, financial and technology companies have by far the largest vulnerability through high risk ports exposed to the internet. Technology companies averaged well over 1000 ports with internet exposure and financial companies averaged nearly 800. That is 4 and 5 times the next highest industry (respectively). When it comes to particularly high risk ports, the financial sector is the biggest offender with an average of 12 high risk ports. For comparison, the technology sector had three.

## Email Security

Email security is one area where we've seen some laudable improvement over the last time we looked at the FTSE 350. For instance, use of Domain-based Message Authentication, Reporting & Conformance (DMARC) policy is up 29%. However, the implementation of Domain Name System Security Extensions (DNSSEC) is at just 4% of the 350 companies that make up the index. Sadly, this too is on par with other indices. They should all seek improvements (alright, we'll get off our soapbox).

## Web Server Security

Going after vulnerable web servers is a favorite vector for attackers. When looking at the status of FTSE 350 company web servers we found that of the three most common types (NGinx, Apache, and IIS), not all were running high enough percentages of supported or fully patched versions. For instance, some 40% of NGinx servers were supported or fully patched, whereas 89% of Apache and 80% of IIS servers were. That's a pretty big discrepancy. Thankfully, Apache and IIS are the dominant servers in this region, minimizing the overall risk.

If you want to take a look at our report you can [read it here](/info/2023-ftse-350-cyber-attack-surface/). If you'd like to check out the report we conducted for Australia's ASX 200 it is available [here](/research/report/2021-industry-cyber-exposure-report-anz/).

## Article tags

  * [Research](/blog/tag/research/)