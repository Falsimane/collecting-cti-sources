# What Is the Instructure Canvas Breach? Impact, Risks, and What Institutions Should Do

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/e/What-Is-the-Instructure-Canvas-Breach.html
- **Date :** 2026-05-10

---

Cyber Threats

# What Is the Instructure Canvas Breach? Impact, Risks, and What Institutions Should Do 

The Instructure Canvas breach affects universities, K–12 school districts, and teaching hospitals globally. This blog entry intends to provide context and practical guidance.

By: Johnny Hand 2026/05/10 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

**_Summary_**

_In May 2026, SHADOW-AETHER-015 exposed data from 8,809 Canvas customers across 50 countries in what appears to be a backend compromise of parent company Instructure’s platform. The breach affects universities, K–12 school districts, and teaching hospitals globally, including eight Ivy League institutions. Because Canvas stores sensitive personal disclosures, for example, medical accommodation requests and private advisor conversations, the primary risk is highly targeted spear‑phishing using real institutional context. The immediate risk is follow‑on social engineering, credential abuse, and targeted phishing campaigns._

When a learning management system is breached, the impact isn’t just technical. Canvas is where students share medical needs, seek support from advisors, and navigate some of the most personal moments of their academic lives. The confirmation of a breach at Instructure - Canvas’s parent company - means that sensitive information entrusted to those systems may now be in the wrong hands. We want to help you understand what happened, what it means in practice, and what to do next.

Security and IT teams across thousands of institutions running Canvas are already in response mode. This update is intended to support that work with clear intelligence, honest context, and practical guidance.

What is the Instructure Canvas breach?

Canvas is the learning management system of choice for tens of millions of students and educators worldwide. It is used for distributing coursework, recording grades, managing API integrations with dozens of third-party tools, and - critically - facilitating private conversations between students and faculty, advisors, and support staff.

According to [TrendAI™ Research](/en/about/threat-research.html), threat actor SHADOW-AETHER-015 has released a document containing 8,809 educational institution names - almost certainly a dump of Canvas LMS customer accounts and instances. The full scope of what was accessed is still being established, but the nature of Canvas’s role in institutional life makes this data exposure more sensitive than a typical platform breach.

**8,809**  
institutions in leaked data | **50**  
countries affected | **1,616**  
K–12 districts confirmed | **8**  
Ivy League universities  
---|---|---|---  
  
Why is the Canvas breach serious?

Not all data breaches are equal. These warrants close attention for several reasons: 

  * Canvas holds unusually sensitive personal information. Students disclose medical conditions for accommodation requests, share personal circumstances with advisors, and communicate with advocates. 
  * The breach enables highly convincing follow-on attacks. Threat actors now potentially have real names, institutional email addresses, course context, and private message history - making it possible to craft phishing messages nearly indistinguishable from legitimate institutional communications.
  * API integrations amplify the impact. Because Canvas connects to dozens of third-party applications via API keys, the breach forced institutions to re-authorize all external integrations - disrupting tools many depended on during final exam periods.
  * The reach is global and cross-sector. Canvas is embedded across K–12, higher education, and - through medical school programs - healthcare institutions. The downstream risk does not stop at one institution type or one region.



How many institutions are affected by the Canvas breach?

TrendAI™ analysis of the data released by SHADOW-AETHER-015 reveals the full scale of this breach. The leaked list spans thousands of institutions across 50 countries and 6 continents -making this one of the most geographically widespread education sector exposures on record.

Region | Institutions | Share of Total  
---|---|---  
North America | ~8,361 | 94.9%  
Europe | ~196 | 2.2%  
Asia-Pacific | ~175 | 2.0%  
Latin America | ~55 | 0.6%  
Middle East & Africa | ~12 | 0.1%  
  
The United States accounts for 94.6% of affected institutions (8,335). Australia (122), the United Kingdom (70), and Brazil (29) are the most significantly impacted countries outside North America. In total, 46 countries are represented.

Of the 8,809 entries, confirmed figures include 2,514 higher education institutions - among them all eight Ivy League universities, major state university systems, and internationally recognized institutions including Oxford, Cambridge, NUS, and the University of Melbourne - and 1,616 K–12 school districts, including large urban systems such as Clark County (Las Vegas), Houston ISD, and Miami-Dade.

The presence of development, UAT, and staging instances in the data points toward backend infrastructure access or a platform-level compromise - a detail that distinguishes this from a surface-level attack.

How did SHADOW-AETHER-015 carry out the attack?

The extortion group demonstrates medium-to-high capability, with the ability to extract large-scale platform data indicating backend system access or sophisticated API exploitation.

SHADOW-AETHER-015 was also involved in a 2025 compromise of Instructure’s Salesforce environment, according to [SecurityWeek](https://www.securityweek.com/hundreds-of-salesforce-customers-allegedly-targeted-in-new-data-theft-campaign/), resulting in millions of data records being compromised and leaked. Their documented approach is often to exploit a trusted third-party integration to reach a higher-value target.

What cyber attacks should Canvas institutions expect next?

The most significant risk from this breach is not what happened - it is what comes next. The weeks following a large-scale data exposure typically bring:

  * Spear-phishing campaigns using real institutional context - referencing actual courses, advisors, and student circumstances - targeting faculty, staff, and students
  * Credential abuse attempts against institutional systems, particularly where Canvas credentials overlap with other internal accounts
  * Targeted social engineering of individuals whose sensitive personal disclosures were captured in Canvas messages, including medical and personal circumstances



Institutions with large graduate and professional programs face elevated risk. Medical institutions on the list - including Weill Cornell Medical College, the University of Nebraska Medical Center, and several Brazilian hospital systems - should treat HIPAA implications as part of their response planning. K–12 institutions must address FERPA and COPPA obligations given that minor children’s data is involved.

How can institutions protect themselves after the Canvas breach?

Detecting post-breach social engineering requires correlating communication behavior across the entire attack surface - not just filtering for known malicious indicators, which will not appear in attacks built from legitimate compromised institutional data.

Any organization holding critical and sensitive data needs a proactive approach: a way to discover their entire attack surface, identify and prioritize risk assets, gain visibility into the attack paths a threat actor could take, and implement mitigating controls that lower the risk of breach.

What comes next won't arrive with obvious warning signs. It will look like a message from a familiar name, referencing a real course or a real conversation. The best defense isn't faster filtering - it's broader visibility, connecting the signals across the environment to spot what doesn't fit before it becomes a problem.

TrendAI™ customers are already being monitored for Canvas-related activity

TrendAI™ Research is actively tracking the spear-phishing campaigns, credential abuse patterns, and social engineering activity that typically follow large-scale education data exposures. That intelligence feeds directly into [TrendAI Vision One™](/en/business/products/one-platform.html) protection - so customers benefit from what our research teams are seeing across the global threat landscape, not just what is happening inside their own environment.

About TrendAI™ Research

Decades of human intelligence, now accelerated by nearly 20 years of applied AI in cybersecurity, give our teams an unusually deep view of how adversaries operate - who they target, how they move, and what they do with what they find. That foresight is what we bring to situations like this: not just to understand what happened, but to help organizations stay ahead of what comes next.

Frequently Asked Questions: The Instructure Canvas Breach

The following questions address what institutions, students, and security teams are asking about the Canvas breach.

**Is my university or school affected by the Canvas breach?**

TrendAI™ Research has identified 8,809 institutions in the leaked data, spanning 50 countries. All eight Ivy League universities are confirmed in the list, along with major US state university systems, 1,616 K–12 school districts, and international institutions including Oxford, Cambridge, NUS, and the University of Melbourne. 

**What data was stolen in the Instructure Canvas breach?**

The data exposed is what institutions and users had stored and exchanged within Instructure’s Canvas platform. This likely includes personally identifiable information (PII), and - given Canvas’s role in education - may include medical accommodation requests, private advisor conversations, and sensitive personal disclosures. It does not include access to institutions’ internal IT systems.

**Did the Canvas breach expose student medical records?**

Canvas is commonly used by students to disclose medical conditions for accommodation requests and to communicate privately with advisors and advocates. Those communications are likely within the scope of the breach. Institutions should treat this as a potential exposure of sensitive personal information and communicate accordingly with their communities.

**Is my institution’s internal network compromised?**

No. The breach is of Instructure’s Canvas platform, not of institutional internal systems. Threat actors do not have direct access to your internal environment because of this breach. However, the stolen data enables highly convincing phishing and social engineering attacks that could lead to credential compromise if not addressed.

**What should institutions do after the Canvas breach?**

Immediately: alert staff, faculty, and students to expect highly convincing phishing emails referencing real course and advisor names. Review and re-authorize Canvas API integrations. Audit whether Canvas credentials overlap with other internal systems and enforce MFA. K–12 and medical institutions should begin FERPA, COPPA, and HIPAA communications planning. Engage TrendAI™ to monitor for downstream threat activity.

**Who is the threat actor SHADOW-AETHER-015?**

SHADOW-AETHER-015 demonstrates medium-to-high capability. Their approach involves exploiting trusted third-party integrations to reach higher-value targets. TrendAI™ Research is actively tracking this group.

Tags

[Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article)

###  Authors 

  * Johnny Hand

VP, AI Operational Excellence




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)