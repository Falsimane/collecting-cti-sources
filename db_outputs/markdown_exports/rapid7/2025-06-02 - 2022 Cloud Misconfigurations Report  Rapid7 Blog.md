# 2022 Cloud Misconfigurations Report | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/04/20/2022-cloud-misconfigurations-report-a-quick-look-at-the-latest-cloud-security-breaches-and-attack-trends/
- **Date :** 2025-06-02

---

Every year, Rapid7's team of cloud security experts and researchers put together a report to review data from publicly disclosed breaches that occurred over the prior year. The goal of this report is to unearth patterns and trends in cloud-related breaches and persistent exposures, so organizations around the world can better protect against threats and address [cloud misconfigurations](/fundamentals/cloud-misconfigurations/) in their own environments.

In the 2022 Cloud Misconfigurations Report, we reviewed 68 accounts of breaches from 2021. Let's take a brief look at some of the findings from this report, including what industries are being targeted, what the bad guys are looking to gain, and what you can do to shore up your cloud security.

[**Get the 2022 Cloud Misconfigurations Report**](/info/cloud-misconfigurations-research-report/) ▶︎

## What industries are being targeted?

In the subset of breaches we studied, there was a broad distribution of affected industries. Our sample had the following industries represented:

  * Information
  * Healthcare
  * Public administration
  * Retail
  * Professional services
  * Arts and entertainment
  * Manufacturing
  * Finance
  * Educational services
  * Transportation
  * Real estate
  * Accommodation and food services
  * Utilities



This is a notable swath of industries, especially considering the sample size. Among the organizations affected by breaches, some were prominent brands and even staples of the Fortune 500, not just startups operating on shoestring budgets. These organizations have the resources and expertise to establish the gold standard of [cloud security best practices](/fundamentals/what-is-cloud-security/), so it just goes to show that anyone is susceptible to breaches due to cloud misconfigurations.

While we found that breaches can hit any organization, no matter their size and prestige, organizations in high-risk industries — like information, healthcare, and public administration — should be especially cautious. The information industry, in particular, was represented at the top of our list, with a considerable lead of nearly double the amount of breaches than reported by the healthcare industry (the second-most affected industry).

## What are the bad guys looking for?

So we know that a variety of industries are being targeted, with a particular focus on organizations that store highly sensitive information. Next, let's take a look at what exactly bad actors are trying to gain by exploiting cloud misconfigurations.

For starters, we found that details on physical location (such as addresses or latitude/longitude details), names, and email were the most commonly lost resources. Other highly sought after data included:

  * Identifier information
  * Passwords
  * Health details
  * Social data
  * Financial information
  * Phone numbers



That's not all: We also saw that personal, legal, and technical information was stolen, as well as authentication and even media data.

Depending on your industry, you may not store all these data types, but the overall set of details lost represents a gold mine for bad actors who want to carry out social engineering attacks. In the hands of a skilled social engineer, this data can be leveraged to craft incredibly convincing phishing attempts. Passwords, identifiers, and authentication data could also be used by a bad actor to infiltrate a network and extract even more valuable information.

All in all, the data compromised isn't always the expected high-value nuggets, like credit card information or Social Security numbers. Simple data on names, locations, and email addresses can be powerful weapons, so it's critical to keep these seemingly less important tidbits of information safe.

####   
Learn more about how InsightCloudSec can help secure your cloud and multi-cloud environments.

[Get Started](/products/insightcloudsec/)

  


## What can you do to stay secure?

Better [cloud security](/solutions/cloud-security/) doesn't have to be hard. Many of the breaches we reviewed tended to be caused by avoidable circumstances, such as using unsecured resources or users relaxing security permissions. As a result, you can take a few easy steps to better defend your environment and even discover misconfigurations faster.

Rapid7 maintains a globally distributed honeypot network called [Project Lorelei](/research/project-lorelei/). These honeypot instances are set up on various cloud vendors, waiting for inbound connections, which helps in identifying a misconfiguration or some type of malicious activity. Bad actors will often scan the internet looking for exposed resources to exploit, so this is one way we get a view into what they're trying to take advantage of.

Thanks to this data, we know that far too many breaches happen as a result of users manually relaxing security settings on cloud resources or making simple mistakes, like typing in the wrong IP address when connecting to a network resource. As such, keeping cloud resources safe can sometimes be as easy as leaving the default security settings intact. (Also, seriously, stop deploying unencrypted instances on the cloud.)

Misconfigurations and lapses in security can also be addressed by:

  * Providing better user training
  * Implementing systems and controls to discourage the relaxing of security mechanisms
  * Conducting reviews of identified resources for appropriate configurations



Breaches are out there — and they're pervasive — but that doesn't mean you have to be a target, and keeping your organization safe may be simpler than you think, so long as you know how to keep an eye out for misconfigurations and follow industry-standard best practices for cloud security.

Curious to learn more about the cloud misconfigurations and breaches that happened last year? Check out the full [2022 Cloud Misconfigurations Report](/info/cloud-misconfigurations-research-report/).

_**Additional reading:**_

  * [_InsightCloudSec Supports the Recently Updated NSA/CISA Kubernetes Hardening Guide_](/blog/post/2022/04/14/insightcloudsec-supports-the-recently-updated-nsa-cisa-kubernetes-hardening-guide/)
  * [ _Stay Ahead of Threats With Cloud Workload Protection_](/blog/post/2021/12/10/stay-ahead-of-threats-with-cloud-workload-protection/)



## Article tags

  * [Research](/blog/tag/research/)
  * [Cloud Security](/blog/tag/cloud-security/)