# Kuse Web App Abused to Host Phishing Document

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/d/kuse-web-app-abused-to-host-phishing-document.html
- **Date :** 2026-04-29

---

Cyber Threats

# Kuse Web App Abused to Host Phishing Document

Bad actors took advantage of the legitimate name and services of Kuse, a popular AI-based app designed for workplaces. The attackers exploited the users’ trust in Kuse to carry out a phishing attack.

By: Jed Valderama, Kenneth Polagñe 2026/04/29 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

**Key takeaways**

  * The growing dependence on AI has caused a rapid emergence of AI-based tools. Unfortunately, these applications have also become vectors for malicious actions, as in this case with Kuse.ai.
  * Ordinarily, Kuse is a trusted workplace platform. However, threat actors are always finding new methods of social engineering.
  * In this case, threat actors executed a phishing attack that utilized a fake URL and image manipulation.
  * Organizations therefore have to strengthen their security training and keep reminding employees that an application’s good reputation does not guarantee the trustworthiness of its content.



As AI increases its role in work and daily life, AI apps are also increasing in number. Along with this emergence are expanding attack vectors that threat actors are actively exploring[. AI is reshaping the cybersecurity landscape, introducing both unprecedented opportunities and complex risks](https://www.trendmicro.com/vinfo/tmr/?/us/security/news/threat-landscape/fault-lines-in-the-ai-ecosystem-trendai-state-of-ai-security-report).

On April 9, 2026, the TrendAI Managed Services Team encountered a phishing attack that revealed another vulnerability that enabled attackers to store phishing chains, breach trust, and eventually expose credentials. In this case, attackers abused the storage and sharing features of Kuse, a free AI web app.

This breach involved a [Supply Chain Attack](https://www.trendmicro.com/en/what-is/cyber-attack/supply-chain-attack.html), particularly a Vendor Email Compromise (VEC), wherein a compromised mailbox from a trusted vendor was used to send a specifically crafted phishing email that leveraged the existing relationship level between the two organizations. Because of this, some IOCs are partly redacted in this article due to the usage of specific organization names.__

Due to the breach of trust, a malicious email was forwarded to relevant users for processing, leading to a user clicking on a phishing link and providing credentials to a fake login page.

![Figure 1. Attack diagram](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/kuse-phishing/fig1.png)

Figure 1. Attack diagram

**Kuse.ai**

According to its website,**** Kuse.ai is an agentic AI coworker that uses one’s work context to improve decision-making and execute end-to-end, multi-step workflows. 

![Figure 2. Web UI of Kuse.ai](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/kuse-phishing/fig2.png)

Figure 2. Web UI of Kuse.ai

Upon logging in, users can upload documents or create a markdown note on their folders. They can then ask an AI chatbot to perform tasks using the uploaded files.

![Figure 3. Example AI prompt listing files on the account](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/kuse-phishing/fig3.png)

Figure 3. Example AI prompt listing files on the account

Each file on the account can be shared via a share button, which generates a link hosted under Kuse’s domain, _app[.]kuse[.]ai_. 

![Figure 4. Generating a shareable link through the web app UI.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/kuse-phishing/fig4.png)

Figure 4. Generating a shareable link through the web app UI.

Attackers abused this mechanism to host a fake blurred document that contained a link to a fake login page.

**URL Analysis**

  * hxxps://app[.]kuse[.]ai/sharednote/{vendor company}%20S.L..md/shared_3049184.md



The URL used the legitimate domain _app[.]kuse[.]ai_ and contained spaces, commas, and periods. Moreover, the URL mimicked a legitimate document using the compromised vendor’s company name. These links were presumably put in emails sent from mailboxes belonging to the compromised vendor, aimed at the target organization. This tactic was meant to confuse users and automated scanners.

Because the Markdown file extension (_.md_) is less commonly used in phishing attempts than document (e.g., _.pdf, .docx_) and webpage (e.g., _.html, .aspx_) file extensions, it can bypass filter signatures and heuristic rules that focus on more typical malicious file extensions.

#### **User Experience and Redirection**

After clicking the phishing URL, the user was redirected to the legitimate AI workspace _app[.]kuse[.]ai_. The user then opened the _.md_ page, which was displayed as a blurred document preview. This falsified document preview lured the user into clicking the malicious link below it, thinking it would reveal its full content. The link stated in Spanish “**HAZ CLIC AQUÍ PARA VER EL DOCUMENTO** ”, which translates into English as “**CLICK HERE TO VIEW THE DOCUMENT** ”.

![Figure 5. Blurred fake document with link hosted on Kuse.ai](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/kuse-phishing/fig5.png)

Figure 5. Blurred fake document with link hosted on Kuse.ai

Instead, the hyperlink redirected the user to a fake Microsoft login page to collect user credentials:

  * hxxps://onlineapp[.]ooraikaoo[.]info/?auth2=8rf22euu-2nxkebabDjjILlzldhQq2Pz



![Figure 6. Fake login page](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/kuse-phishing/fig6.png)

Figure 6. Fake login page

Conclusion

Threat actors are always looking for new vectors to exploit the inherent trust placed in legitimate platforms. They abuse the storage and sharing capabilities of free services, as well as the growing interest in AI-powered web applications. Using the Markdown (_.md_) file extension as the delivery format, combined with a VEC to establish trust at the point of delivery, demonstrates a multi-layered social engineering approach designed to evade both automated defenses and human scrutiny, which in turn highlights the need for layered protection and heightened user awareness.

As AI tools become more embedded in business workflows, their sharing and collaboration features present new surfaces for abuse. Similar to how threat actors have previously leveraged file-sharing services, such as [Dracoon](/en/research/23/k/threat-actors-leverage-file-sharing-service-and-reverse-proxies.html), to host intermediary phishing documents and GitHub's trusted reputation to [distribute malware](/en/research/25/c/ai-assisted-fake-github-repositories.html), the abuse of Kuse.ai follows an established pattern: weaponizing platform legitimacy to circumvent security controls. Therefore, organizations must recognize that even highly reputable platforms can host untrustworthy content.

Recommendations

  * Conduct regular user awareness training. Training should go beyond generic phishing awareness and include real-world scenarios involving AI platform abuse, VEC, and blurred document lures. Users should be educated on recognizing social engineering cues regardless of the hosting platform's reputation.
  * Verify links beyond the domain. A legitimate domain (e.g., _app[.]kuse[.]ai_) does not guarantee safe content. Users should scrutinize the full URL path, especially when documents are shared unexpectedly or contain urgency-driven calls to action.
  * Treat VEC as a persistent threat. Emails from trusted vendors should not be exempt from security scrutiny. Organizations should implement policies that require secondary verification (e.g., a phone call or separate messaging channel) before acting on requests that involve clicking links or providing credentials, particularly when the email context is unusual.
  * Enforce Multi-Factor Authentication (MFA) with phishing-resistant methods. Traditional MFA can be bypassed by reverse proxy toolkits. Organizations should adopt phishing-resistant authentication methods, such as FIDO2/WebAuthn hardware keys, to mitigate credential harvesting from fake login pages.
  * Monitor and restrict AI platform sharing features. Security teams should assess which AI tools are in use within the organization and evaluate whether their sharing and external link generation features introduce unmanaged risks. Where possible, outbound access to AI platform sharing URLs that are not business-critical should be restricted or monitored.
  * Implement advanced email and URL filtering. Deploy email security solutions capable of inspecting URLs at time-of-click rather than only-at-delivery. URL sandboxing and real-time reputation checks can help detect phishing pages hosted on otherwise trusted domains.



TrendAI Vision One™ Threat Intelligence Hub

[_TrendAI Vision One™ Threat Intelligence Hub_](/en/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform.

Emerging Threats: [_Kuse AI Web App Abused to Host Phishing Document_](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Kuse%20AI%20Web%20App%20Abused%20to%20Host%20Phishing%20Document)

TrendAI Vision One™ Intelligence Reports (IOC Sweeping) 

[_Kuse AI Web App Abused to Host Phishing Document_](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=Kuse%20AI%20Web%20App%20Abused%20to%20Host%20Phishing%20Document)

Indicators of Compromise (IoCs)

  * 91.92.41[.]64
  * hxxps://onlineapp[.]ooraikaoo[.]info/?auth2=8rf22euu-2nxkebabDjjILlzldhQq2Pz
  * hxxps://app[.]kuse[.]ai/sharednote/<victimcompany>%20S.L..md/shared_3049184.md



Tags

[Web](/en/research.html?category=trend-micro-research:environments/web) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Phishing](/en/research.html?category=trend-micro-research:threats/phishing) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article)

###  Authors 

  * Jed Valderama

Threats Analyst

  * Kenneth Polagñe

Security Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)