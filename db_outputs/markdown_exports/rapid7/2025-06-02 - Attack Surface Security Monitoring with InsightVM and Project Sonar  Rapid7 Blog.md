# Attack Surface Security Monitoring with InsightVM and Project Sonar | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/06/18/attack-surface-monitoring-with-project-sonar/
- **Date :** 2025-06-02

---

## Why you should care about your expanding attack surface

An [attack surface](/fundamentals/attack-surface/) in the realm of information security is the variety of ways a given asset can be interacted with and, therefore, potentially attacked. Maintaining a minimal attack surface is a fundamental part of any information security program.

As organizations evolve and related infrastructure becomes more complex, it is challenging to keep track of one’s internet-connected assets. In the past, it may have been sufficient to simply walk into a server closet and count, or utilize an asset inventory system to produce a list of assets. With virtualization, cloud computing, mergers and acquisitions, bring-your-own-device (BYOD), the Internet of Things (IoT), and other advancements in rapid development and technology, information security professionals are facing complicated asset sprawl. An increase in the number, diversity, and complexity of assets results in an increased attack surface and therefore more potential risk to organizations.

Fortunately, Rapid7 has something that can help: Attack Surface Monitoring with [Project Sonar](https://opendata.rapid7.com/about/).

## What is Project Sonar?

Project Sonar is an internet scanning project that regularly examines assets exposed on the public internet. For several years, the project has been collecting vast troves of metadata related to assets on the public internet. The metadata is collected from two different sources: endpoint scanning and the global domain name system (DNS).

### Metadata from endpoint scanning

With endpoint scanning, Sonar connects to a given port and protocol on all public IP addresses —for example, 80/TCP for default HTTP—and then interacts with the service. The results of these interactions include metadata that can be helpful in identifying the service or the asset exposing the service. These endpoint scans occur on a regular basis and, at last count, Sonar had observed over 232 million unique assets exposing services on hundreds of unique port and protocol combinations.

### Metadata from the global DNS:

For Sonar’s DNS work, it uses a catalog of over 4 billion DNS names and attempts to resolve a variety of common DNS record types for all of these names. These names come from a variety of sources, including domain registrars and metadata collected during the endpoint studies that might include names such as SSL certificates, HTML links in HTTP responses, service banners, and more. Current Sonar DNS studies identify nearly 8 billion unique DNS records covering 80 different DNS record types on a weekly basis.

## Leveraging Sonar to reduce and monitor your attack surface

With knowledge of which assets are exposed, what the assets are exposing, as well as the DNS records and names observed, Sonar’s data can assist in efforts related to the attack surface of the public internet.

Data collected by Sonar is made available to the public through [Rapid7’s Sonar Data](https://opendata.rapid7.com/), where we provide access to over 25 terabytes of data collected since Sonar’s launch over five years ago. This data can be used by practitioners to identify publicly exposed portions of their infrastructure, academics looking for large, rich security datasets, and researchers participating in bug bounty programs, among other use cases. 

## Integrating Attack Surface Monitoring with Project Sonar with InsightVM

Rapid7 customers using [InsightVM](/products/insightvm/) or [Nexpose](/products/nexpose/) for their vulnerability management efforts can take advantage of the [Attack Surface Monitoring with Project Sonar integration](https://docs.rapid7.com/insightvm/setting-up-a-sonar-query/) to identify known and unknown assets that they may be responsible for securing. In this mode, customers simply provide domain names or IP address ranges they are interested in and the integration will return the relevant assets discovered by Sonar that can then be assessed in an automated fashion.

As an example, here is a screenshot of this functionality being used for the rapid7.com domain, where with no other input other than the name, the Sonar integration automatically discovered thousands of assets that Rapid7 has to monitor:

![insightvm.png](https://www.rapid7.com/cdn/images/blt38ed556e35e28b55/683de5322a76862300bc859d/insightvm.png)

By combining this discovery functionality with the [automated actions](https://docs.rapid7.com/insightvm/automating-security-actions-in-changing-environments/) functionality in InsightVM, customers can ensure that new assets will be discovered and assessed as they are exposed on the public internet.

## Interested in learning more?

We are partnering with SC Media on June 21, 2019 and SANS on June 26, 2019 to host a webinar, “Gaining Complete Visibility of Your Environment with Attack Surface Monitoring.” We hope to see you there!

## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)