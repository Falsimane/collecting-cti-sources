# Europol, Microsoft, TrendAI™, and Collaborators Halt Tycoon 2FA Operations

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/c/tycoon2fa-takedown.html
- **Date :** 2026-03-04

---

Cyber Threats

#  Europol, Microsoft, TrendAI™ and Collaborators Halt Tycoon 2FA Operations

Tycoon 2FA was dismantled this week by law enforcement and industry partners including TrendAI™. The phishing-as-a-service platform offered MFA bypass services using adversary-in-the-middle (AitM) proxying.

By: Christopher Boyton, Mayra Rosario Fuentes, Stephen Hilt 2026/03/04 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key Takeaways

  * The operations of phishing-as-a-service (PhaaS) platform Tycoon 2FA was taken offline this week by the combined effort of law enforcement that includes Europol and other partner agencies, as well as private industry organizations including CloudFlare, Coinbase, Crowell, eSentire, Health-ISAC, Intel471, Microsoft, Proofpoint, Resecurity, The Shadowserver Foundation, SpyCloud, and TrendAI™. Experts from TrendAI™ supported the operation with threat intelligence, infrastructure mapping, and actor attribution.
  * Tycoon 2FA uses adversary-in-the-middle (AitM) proxying to bypass traditional multi-factor authentication (MFA) and capture session cookies in real time. The subscription model offered by the service lowers the barrier to entry for criminals by removing the need to build infrastructure, develop tooling, or understand the mechanics of AitM attacks. 
  * Tycoon 2FA operations highlight that traditional MFA without phishing-resistant protections can be bypassed via AitM attacks and how PhaaS campaigns can have cascading impact well beyond the original victim, as stolen sessions and accounts can be reused, resold, and repurposed.
  * This blog offers solutions and recommendations to help organizations defend against phishing attacks. TrendAI™ continues to monitor for the resurfacing of the service and will support ongoing law enforcement efforts, including further investigation of known users to protect customers.



A coordinated disruption effort seized this week the infrastructure tied to the operations of phishing-as-a-service (PhaaS) Tycoon 2FA. Over 300 domains tied to Tycoon 2FA were seized in an operation led by Microsoft and Europol and supported by other law enforcement agencies, as well as private organizations such as CloudFlare, Coinbase, Crowell, eSentire, Health-ISAC, Intel471, Proofpoint, Resecurity, The Shadowserver Foundation, SpyCloud, and TrendAI™. 

Researchers from TrendAI™ have been tracking the infrastructure, as well as the campaigns and operator behaviors that can be linked to Tycoon 2FA to build a clearer picture of how its services was being used at scale. By November 2025, TrendAI™ had collected enough data to link the operation to an actor using the monikers “SaaadFridi” and “Mr_Xaad”, likely the developer/operator of Tycoon 2FA.

Historical activity showed this actor previously focused on web defacements before moving into building and running this phishing toolkit. Intelligence gathered by TrendAI™ also included details on tooling, infrastructure, and activity patterns, which was shared with Europol to support law enforcement action.

Tycoon 2FA first appeared in August 2023 as a PhaaS kit designed to bypass multi-factor authentication (MFA). Aside from stealing usernames and passwords, it also uses an adversary-in-the-middle (AitM) proxy that sits between the victim and the real log in page, allowing it to capture credentials, MFA codes, and session cookies in real time. Attackers can then replay those session cookies to take over accounts even when MFA is enabled. 

The PhaaS platform has approximately 2,000 users as of writing. Research and monitoring show that it has used over 24,000 domains since it first appeared in 2023. Its kit has been reported by [Proofpoint](https://www.proofpoint.com/us/blog/email-and-cloud-threats/tycoon-2fa-phishing-kit-mfa-bypass) to have been used in large-scale campaigns targeting Microsoft 365 and Google.

Tycoon 2FA stood out as a platform for its scale and accessibility: its ready-to-use phishing toolkit provided attackers with fake login pages, a proxy layer, and basic campaign tooling with minimal setup required. Newer [versions](https://www.scworld.com/news/tycoon-2fa-phishing-kit-adds-stealth-expands-to-mobile-devices) have added simple evasion features to deter bots and hinder analysis, making detection and takedown efforts more difficult. These service features and modifications fit into a broader trend where phishing kits are becoming cheaper, more accessible, and easier to operate even for low-skill attackers. 

![Figure 1. A screenshot of the Tycoon 2FA domain prior to the service being disrupted](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/phaas-takedown/fig1-phaas-takedown.png)

Figure 1. A screenshot of the Tycoon 2FA domain prior to the service being disrupted

Phishing enabled by phishing kits is often overshadowed by ransomware in the threat landscape in terms of risk posed, but it should not be underestimated. Phishing enabled by phishing kits is one of the most impactful attacks any enterprise can face: not only does it enable initial access, platforms like Tycoon 2FA also plugs into the broader cybercrime economy. 

Credentials and session cookies harvested through AitM campaigns can be resold in established credential marketplaces or passed to access brokers, who specialize in monetizing footholds into corporate environments. That access is then frequently reused for follow-up activity such as business email compromise (BEC), data theft, or ransomware deployment.

In this model, Tycoon 2FA functions as an entry point rather than a complete attack chain, feeding a wider ecosystem of criminal services. The result is that a single successful phishing campaign can have cascading impact well beyond the original victim, as stolen sessions and accounts can be reused, resold, and repurposed across multiple operations.

The potential to extend damage well beyond the initial compromise makes the ability to intercept authentication flow and harvest session cookies creates a high-impact risk for organizations, especially as identity becomes the primary security perimeter. 

Successfully taking down an operation like Tycoon 2FA can be hard for any single organization to do alone because the infrastructure, hosting, and victims involved are spread across many countries and networks. No single vendor or agency has full visibility and disruption at this scale requires coordination between private sector teams who see the technical indicators, and public sector partners who have the authority to act on them. A joint effort to coordinate tracking, analysis, and disruption efforts makes it harder for operations to rebuild and reuse tools or move to a new platform without being noticed at least in the short to medium term. 

TrendAI™ had been investigating Tycoon 2FA after detecting the threat actor targeting its customers. TrendAI™ provided this existing data along with its on-going surveillance as actionable intelligence to Europol during the period of research and close monitoring that preceded the Tycoon 2FA takedown this week.

![Figure 2. A distribution by country of domains targeted by Tycoon 2FA in 2026](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/phaas-takedown/Fig-2-phaas-takedown.jpg)

Figure 2. A distribution by country of domains targeted by Tycoon 2FA in 2026

A splash screen, shown in Figure 2, was served to all the criminal customers of the service confirming the seizure of the Tycoon 2FA infrastructure, and listed the coalition partners involved in the action, including TrendAI™. 

![Figure 3. The splash screen served to all the criminal customers of the service confirming the seizure of the Tycoon 2FA infrastructure by the collaborative effort of law enforcement agencies and private organizations shown  ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/phaas-takedown/phaas-takedown-newsplash.jpeg)

Figure 3. The splash screen served to all the criminal customers of the service confirming the seizure of the Tycoon 2FA infrastructure by the collaborative effort of law enforcement agencies and private organizations shown 

The disruption of Tycoon 2FA shows what happens when threat intelligence is operationalized trough cross-industry coordination for real-world impact: this operation did not just take down one service, it raises the cost and risk for the people running these operations and helped protect a much wider set of victims. 

However, taking down the platform is not the end of the work. Operators have always been known to adapt, rebuild, and migrate to new infrastructure. Known and suspected users of Tycoon 2FA can attempt to continue operations, and previously stolen credentials and session cookies remain in circulation.

TrendAI™ will continue to monitor for signs of the service resurfacing, support follow-up effort and investigation of the identified users and administrators involved in Tycoon 2FA and share relevant intelligence with law enforcement and industry partners. Disruption raises the cost for attackers, but sustained pressure powered by intelligence sharing is necessary to keep it high.

Protect yourself against phishing-as-a-service attacks

Phishing kits like Tycoon 2FA facilitate initial access for cybercriminals and connect to a broader ecosystem where stolen credentials and session cookies are resold or leveraged by access brokers. This enables follow-up attacks such as BEC, data theft, or ransomware, resulting in a single successful phishing campaign having far-reaching consequences across multiple operations. To safeguard your organization, it’s essential to adopt a layered defense strategy that combines technology, training, and proactive monitoring:

  *     * Leverage [TrendAI Vision One™ Email and Collaboration Security](https://www.trendmicro.com/en/business/products/email-and-collaboration.html). As part of the broader TrendAI Vision One™ platform, this solution uses layers of AI powered monitoring to detect advanced threats such as lateral phishing, advanced phishing, and domain and brand impersonation, while also providing sandbox malware analysis, document exploit detection, and data loss prevention across platforms like SharePoint, OneDrive, Box, and Google Drive.
      *         * Enable URL and web content inspection. Deliver real-time alerts to your IT team when employees engage with fake websites. Powered by computer vision and Visual AI, the system scans web content, forms, and images, with advanced webpage analysis detecting, prioritizing, and scoring high-risk elements to identify phishing and BEC threats.
        * Use AI-driven writing and impersonation analysis. TrendAI™ uses Writing Style DNA technology that helps determine if an email is legitimate by using machine learning to check a user's writing style based on past emails and then comparing suspicious emails against it, helping to catch business email compromise (BEC) and executive impersonation attempts.
  * Implement Identity Security Posture Management (ISPM). [TrendAI Vision One™ Cyber Risk Exposure Management](https://www.trendmicro.com/en_us/business/products/cyber-risk-exposure-management.html) (CREM) allows organizations to track employee behavior changes based on metrics like the overall risk of account compromise and the number of accounts with weak authentication, with automated workflows that can deploy training to employees based on selected risk events and conditions. 
  * Run [phishing simulation assessments and security awareness training](https://www.trendmicro.com/en_us/business/products/cyber-risk-exposure-management/security-awareness.html). Regularly test employees with simulated phishing campaigns to identify human risk and use the results to drive targeted security awareness training, turning users into an active line of defense rather than a vulnerability.
  * 


Acknowledgements

TrendAI™ extends its gratitude to the law enforcement that includes Europol and other partner agencies, and private industry collaborators that include CloudFlare, Coinbase, Crowell, eSentire, Health-ISAC, Intel471, Microsoft, Proofpoint, Resecurity,The Shadowserver Foundation, and SpyCloud that made this disruption operation a success. 

TrendAI™ firmly believes that collaboration is critical to disrupting cybercrime at scale. By working hand-in-hand with partners worldwide, we make cyberspace safer for individuals, businesses, and governments alike.

Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Phishing](/en/research.html?category=trend-micro-research:threats/phishing) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Christopher Boyton

Adversary Hunter

  * Mayra Rosario Fuentes

Senior Threat Researcher

  * Stephen Hilt

Senior Threat Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)