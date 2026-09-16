# Open-Source Security: Getting to the Root of the Problem | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/01/19/open-source-security-getting-to-the-root-of-the-problem/
- **Date :** 2025-06-02

---

The past few weeks have shown us the importance and wide reach of open-source security. In December 2021, public disclosure of the [Log4Shell vulnerability in Log4j](/blog/post/2021/12/10/widespread-exploitation-of-critical-remote-code-execution-in-apache-log4j/), an open-source logging library, caused a cascade of dependency analysis by developers in organizations around the world. The incident was so wide-reaching that representatives from federal agencies and large private-sector companies gathered on January 13, 2022, at a White House meeting to discuss initiatives for securing open-source software.

A large percentage of the software we rely on today is proprietary or closed-source, meaning that the software is fully controlled by the company and closed for independent review. But in most cases, all of the code written to build the proprietary software is not entirely produced by the companies that provide the products and services; instead, they use a third-party library or a component piece of software to help them assemble their solution.

Many of those third-party components are classified as open-source software, meaning the source code is freely available for anyone to use, view, change to correct issues, or enhance to add new functionality. Open-source software projects are frequently maintained by volunteers, and a community of developers and users forms around a shared passion for the software. It’s their passion and collaboration that help projects grow and remain supported. 

## Finding the resources for open-source security

Yet for the majority of open-source projects that do not have a large corporate backer, the role these individuals play is frequently overlooked by software consumers, and as a result, many open-source projects face maintenance challenges.

Limited resources impose a variety of constraints on projects, but the implications are particularly wide-reaching when we look at the challenge of securing open-source software. Vulnerabilities discovered in proprietary software are the responsibility of the software vendor, frequently better funded than open-source software, with teams available to triage and resolve defects. Better **—** or any **—** funding, or broader community participation, may also increase the chance of avoiding vulnerabilities during development or discovering them during quality assurance checks. It can also help developers more quickly identify and resolve vulnerabilities discovered at a future date.

Increasing open-source project funding is a wonderful idea, and it’s in the best interest of companies using such software to build their products and services. However, funding alone won’t increase security in open-source projects, just as the greater source code visibility in open-source hasn’t necessarily resulted in fewer defects or shortened times between defect introduction and resolution. 

For example, the vulnerability in Microsoft’s Server Message Block (SMB) protocol implementation ([CVE-2017-0144](https://attackerkb.com/topics/xI1y9OoEgq/cve-2017-0144-ms17-010?referrer=blog)) was around for many years before the defect was resolved in 2017. Similarly, the Log4Shell ([CVE-2021-44228](https://attackerkb.com/topics/in9sPR2Bzt/cve-2021-44228-log4shell/rapid7-analysis?referrer=blog)) vulnerability in the Log4j project was introduced in 2013, and it remained undiscovered and unresolved until December 2021. There is clearly a massive difference in both funding and available resources to those involved in these projects, and yet both were able to have vulnerable defects exist for years before resolution.

## Solving the problem at the source (code)

Accidental software vulnerabilities share similar root causes whether they’re found in proprietary or open-source software. When developers create new features or modify existing ones, we need code reviews that look beyond feature functionality confirmation. We need to inspect the code changes for security issues but also perform a deeper analysis, with attention to the security implications of these changes within the greater scope of the complete project.

The challenge is that not all developers are security practitioners, and that is not a realistic expectation. The limited resources of open-source projects compound the problem, increasing the likelihood that contribution reviews focus primarily on functionality. We should encourage developer training in secure coding practices but understand that mistakes are still possible. That means we need processes and tooling to assist with secure coding.

Security in open-source software carries some other unique challenges due to the open environment. Projects tend to accept a wide variety of contributions from anyone. A new feature might not have enough of a demand to get time from the primary developers, but anyone who takes the time to develop the feature while staying within the bounds of the project’s goals and best practices may very well have their contribution accepted and merged into the project. Projects may find themselves the target of malicious contributions through covert defect introduction. The project may even be sabotaged by a project maintainer, or the original maintainer may want to retire from the project and end up handing it over to another party that **—** intentionally or not **—** introduces a defect.

It’s important for us to identify open-source projects that are critical to the [software supply chain](/blog/post/2021/10/22/2022-planning-designing-effective-strategies-to-manage-supply-chain-risk/) and ensure these projects are sustainably maintained for the future. These goals would benefit from increased adoption of secure coding practices and infrastructure that ensures secure distribution and verification of software build artifacts.

  


## Article tags

  * [Open Source](/blog/tag/open-source-news/)
  * [Research](/blog/tag/research/)