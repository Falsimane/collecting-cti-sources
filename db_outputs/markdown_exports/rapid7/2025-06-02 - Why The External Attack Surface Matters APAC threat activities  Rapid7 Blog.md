# Why The External Attack Surface Matters: APAC threat activities | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/03/21/why-the-external-attack-surface-matters-an-analysis-into-apac-related-threat-activities/
- **Date :** 2025-06-02

---

_Co-authors are Robin Long and Raj Samani_

Considerable focus within the cybersecurity industry has been placed on the attack surface of organizations, giving rise to [external attack surface management (EASM)](/fundamentals/external-attack-surface-management-easm/) technologies as a means to monitor said surface. It would appear a reasonable approach, on the premise that a reduction in exposed risk related to the external attack surface reduces the likelihood of compromise and potential disruption from the myriad of ransomware groups targeting specific geographies and sectors.

But things are never quite that simple. The challenge, of course, is that the exposed external risks extend beyond the endpoints being scanned. With access brokers performing the hard yards for ransomware affiliates gathering information, identifying initial entry vectors is more than a simple grab of banners.

[Rapid7 Labs](/research/)’s recent analysis looked at the external access surface of multiple sectors within the APAC region over the last half of 2023, with considerable data available well beyond open RDP and unpatched systems. What is revealing is the scale of data that appears to be aiding the access brokers, such as the exposure of test systems or unmaintained hosts to the internet, or the availability of leaked credentials. Each of these gives the multitude of ransomware actors the opportunity to conduct successful attacks while leveraging the hard work of access brokers.

What is interesting as we consider these regionally-targeted campaigns is that the breadth of threat groups is rather wide, but the group which is most prevalent does vary based on the targeted geography or sector. (Please note that this data predates the possible [exit scam](https://www.reuters.com/technology/cybersecurity/blackcat-ransomware-site-claims-it-was-seized-uk-law-enforcement-denies-being-2024-03-05/) reported and therefore does not take it into account.)

The following graphic shows the sectors targeted, and the various threat groups targeting them, within Australia:

![Screenshot-2024-03-21-at-12.47.00-PM.png](https://www.rapid7.com/cdn/images/bltb51b0d7afe865d7e/683dea137f8603d34e230a49/Screenshot-2024-03-21-at-12.47.00-PM.png)

If we compare the most prevalent groups in Japan, however, the landscape does change somewhat:

![Screenshot-2024-03-21-at-12.48.05-PM.png](https://www.rapid7.com/cdn/images/bltb0dfc842d98e9273/683dea247f8603dab1230a51/Screenshot-2024-03-21-at-12.48.05-PM.png)

All of which does focus the mind on this concept of actionable intelligence. Typically organizations have taken a one-size-fits-all approach to risk prioritization; however, a more nuanced approach could be to consider the threat groups targeting the given sector of an organization as a higher priority.

The need to move into this new world of intelligence led security operations is very clear, and it’s felt on an almost daily basis. Within a year we have witnessed such a fundamental increase in the level of capabilities from threat groups whose previous modus operandi was entrenched in the identification of leaked credentials, yet will now happily burn 0days with impunity.

Our approach within Rapid7 Labs is to provide context wherever possible. We strongly urge readers to leverage resources such as [AttackerKB](https://attackerkb.com/) to better understand the context of these CVEs, or the likes of Metasploit to validate whether the reports from their external scan warrant an out-of-cycle security update. These, of course, are just the tip of the iceberg, but our approach remains constant: context is critical, as is agility. We are faced with more noise than ever before, and any measures that can be used to filter this out should be a critical part of security operations.

## Article tags

  * [Research](/blog/tag/research/)