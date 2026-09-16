# Law Enforcement Takes Down Kratos/Sneaky2FA Phishing Service, With an Assist From TrendAI™

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/g/kratos-takedown.html
- **Date :** 2026-07-22

---

Cyber Crime

# Law Enforcement Takes Down Kratos/Sneaky2FA Phishing Service, With an Assist From TrendAI™

Kratos, the phishing-as-a-Service (PhaaS) platform behind a large share of recent Microsoft 365 credential theft, has been taken offline by the BKA and ZIT in an operation dubbed Olympus Blade.

By: Christopher Boyton, Stephen Hilt 2026/07/22 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

Key takeaways

  * Kratos, the phishing-as-a-service (PhaaS) platform behind a large share of recent Microsoft 365 credential theft, has been taken offline by the BKA and ZIT (working with US authorities) in an operation dubbed Olympus Blade. The developer and technical administrator was arrested in Indonesia. This platform evolved from Sneaky2FA, a phishing kit targeting Microsoft accounts since October 2024.
  * Over 1,800 criminal subscribers had rented access to Kratos and used it to run an estimated 15,000 phishing campaigns a month. More than 200 servers were shut down, and victims across more than 30 countries, concentrated in Europe and the United States, add up to hundreds of thousands since late 2024.
  * TrendAI™ supported the investigation by providing threat intelligence, infrastructure fingerprinting, victimology, and analysis of the actors behind Kratos. This information was provided to the BKA starting in 2025.
  * The subscription model made Kratos scalable: affiliates could rent the kit and rely on the service to support phishing operations. That is why this takedown matters beyond one arrest: it disrupted the infrastructure and business model that enabled lower-skill operators to run high-volume credential theft campaigns.



Introduction

On July 20, 2026, Germany's Bundeskriminalamt (BKA) and the Frankfurt-based Central Office for Combating Internet Crime (ZIT), working with US authorities, [took down the central infrastructure behind Kratos](https://www.bka.de/SharedDocs/Kurzmeldungen/DE/Kurzmeldungen/260720_Schlag_gegen_Phishing_Gruppierung_Kratos.html), a phishing-as-a-service (PhaaS) platform used to steal Microsoft 365 credentials at scale. Indonesian authorities also arrested the developer and technical administrator of the service. More than 200 servers were shut down, and the platform’s infrastructure was taken fully offline.

Over 1,800 criminal subscribers had purchased access to Kratos and used it to run an estimated 15,000 phishing campaigns a month, each capable of reaching thousands of recipients. Victims spanned across more than 30 countries (concentrated in Europe and the United States), and the total number of victims since late 2024 runs into the hundreds of thousands. BKA and ZIT stated the group had earned more than €300,000 (approximately 342,000 USD) since 2024.

![Figure 1. Seizure banner displayed on former Kratos infrastructure, as part of the joint FBI/BKA/ZIT action \(Operation Olympus Blade\).](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/kratos-takedown/olympus-blade-banner.png)

Figure 1. Seizure banner displayed on former Kratos infrastructure, as part of the joint FBI/BKA/ZIT action (Operation Olympus Blade).

[ download ](/content/dam/trendmicro/global/en/research/26/g/kratos-takedown/olympus-blade-banner.png)

# **A short history: From Sneaky2FA to Kratos**

Kratos is not a new kit. It is the direct evolution of Sneaky2FA, an adversary-in-the-middle (AiTM) phishing kit that has targeted Microsoft 365 accounts since October 2024. Sneaky2FA relayed live authentication sessions between a victim and Microsoft's real login servers, letting the operator capture both credentials and session tokens as they passed through, which is what let the kit defeat MFA rather than just harvest a password.

Sold through a Telegram-based subscription model, the kit gave affiliates a ready-made service: this included phishing domains and antibot checks (Cloudflare Turnstile among them). In November 2025, browser-in-the-browser (BitB) login windows were added that were convincing enough to fool users who had been trained to check the address bar. That business model, renting the kit and letting someone else run the campaign, is what allowed low-skill operators to reach the volume the BKA and ZIT described this week.

# **Actions against Kratos**

TrendAI™ has tracked Sneaky2FA and its evolution into Kratos since December 2024 and has shared intelligence with the BKA since 2025. Over that period, we provided methodologies for fingerprinting Kratos infrastructure and identifying phishing panels, along with observed victimology and regular infrastructure updates.

In March 2025, we observed a Telegram channel advertising the Kratos phishing-as-a –Service offering. Further investigation found that Kratos was likely a rebrand of Sneaky2FA. We conducted an in-depth investigation into the operators and associates and shared our findings with the BKA to support its investigation.

This is the same model of cooperation that supported the March 2026 disruption of [Tycoon 2FA](/en/research/26/c/tycoon2fa-takedown.html), where threat intelligence gathered through ongoing monitoring was provided to Europol ahead of that action. Sustained tracking of a kit's infrastructure and its generational changes over time is what makes it possible to hand law enforcement something they can act on, rather than a single snapshot.

Taking a platform with this footprint offline in a single coordinated action, including the arrest of its developer, is a meaningful result. Carsten Meywirth, BKA’s cybercrime division head, called it a pioneering effort and a clear signal to other cyber actors. We agree with that assessment and congratulate the BKA and its partners. As with many other cybercrime disruptions, the strongest outcomes come from cooperation between law enforcement and the private security industry. TrendAI™ is proud to be a long-standing and active member of that community, helping make the world safer for the exchange of digital information.

Tags

[Cyber Crime](/en/research.html?category=trend-micro-research:threats/cyber-crime) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Christopher Boyton

Adversary Hunter

  * Stephen Hilt

Senior Threat Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)