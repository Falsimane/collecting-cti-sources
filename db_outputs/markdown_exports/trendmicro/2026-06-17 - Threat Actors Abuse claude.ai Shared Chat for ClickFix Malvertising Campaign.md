# Threat Actors Abuse claude.ai Shared Chat for ClickFix Malvertising Campaign

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/f/claudeai-shared-chat-abused-in-malvertising.html
- **Date :** 2026-06-17

---

Malware

# Threat Actors Abuse claude.ai Shared Chat for ClickFix Malvertising Campaign

Cybercriminals hijacked Google Ads searches for popular AI developer tools to funnel over 2,000 victims toward malicious download pages before quietly moving their operation onto claude.ai's own platform, turning the trusted domain into a delivery mechanism for credential-stealing malware.

By: Fyodor Yarochkin, Joshua Paul Ignacio, Ryan Flores 2026/06/17 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

**Key takeaways:**

  * TrendAI™ Research tracked 106 unique malicious hostnames deployed across six distinct attack waves over just seven weeks, with operators continuously rotating infrastructure and testing new AI brand lures to optimize the campaign’s performance.
  * The campaign made a significant tactical leap by shifting to and weaponizing claude.ai's shared chat feature; Victims landed on a fully legitimate, trusted domain that rendered browser warnings, URL inspection, and Safe Browsing heuristics easier to evade.
  * The Asia-Pacific region bore the brunt of the campaign, accounting for 67.2% of all confirmed victims, with Taiwan alone representing 30.5% of total traffic, a concentration that points to deliberate geographic ad targeting rather than opportunistic spread.
  * **Upon being notified by TrendAI™ Research, Anthropic investigated and banned the accounts responsible, disabled the malicious shared conversations, and is implementing additional abuse mitigations for its shared chat feature**.



TrendAI™ Research tracked a sustained malvertising campaign that abused Google Ads to deliver ClickFix social engineering attacks disguised as popular [AI](https://www.trendmicro.com/en_us/what-is/ai.html) developer tools. The campaign impersonated at least six legitimate brand names, including ChatGPT Codex, Perplexity, Cursor IDE, JetBrains, Claude AI, and claude.ai, and simultaneously ran Mac utility scam lures.

By leveraging paid search ads targeting users actively seeking AI development tools, the attackers were able to target technically proficient users who are more likely to interact with command-line instructions without suspicion. This marks a sophisticated evolution of the [ClickFix social engineering technique,](/en/research/26/e/installfix-and-claude-code.html) where victims are tricked into manually executing malicious commands, typically by copying and pasting PowerShell or terminal commands under the guise of "fixing" a problem or completing a software installation.

The threat actors used 92 unique malicious hostnames across GitLab Pages. Because GitLab Pages provides free static site hosting under the trusted _*.gitlab.io_ domain, abusing it bypasses security filters by appearing legitimate to security-conscious users. The attackers created dozens of subdomains mimicking legitimate software download pages, rotating them rapidly to evade detection and blocking.

Later, the campaign pivoted to abuse claude.ai's shared chat feature to host the ClickFix social engineering instructions. Upon being notified by TrendAI™ Research, Anthropic investigated and banned the accounts responsible, disabled the malicious shared conversations, and is implementing additional abuse mitigations for its shared chat feature.

Our analysis covered campaign activity from April 8 to June 14, 2026. TrendAI™ Research continues to monitor for further activity.

![Figure 1. Infection chain of the Claude malvertising campaign ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig1.jpg)

Figure 1. Infection chain of the Claude malvertising campaign 

How attackers used AI developer tools as lures

![Figure 2. A breakdown of campaign lure themes by impersonated brand or tool category](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig2.jpg)

Figure 2. A breakdown of campaign lure themes by impersonated brand or tool category

Most of the campaign (82.8% of all traffic counts) targeted users searching for AI development tools. The targeting of multiple AI brands in rapid succession suggests the operators are keyword-testing across the AI tool ecosystem to identify which brands generate the most engagement:

  * **Claude AI (Anthropic):** The primary target throughout the campaign. Variants used in the campaign included "Claude Code," "Claude Desktop," and "Claude Desktop LM," different products Anthropic offers; this suggests that the attackers closely studied the product lineup.
  * **ChatGPT Codex (OpenAI):** Introduced in Wave 3 and expanded in Wave 4, capitalizing on interest in OpenAI's code generation tools.
  * **Perplexity AI:** A single but persistent lure (_perplexity-platform.gitlab.io_) targeting users of the AI search engine.
  * **Cursor IDE:** A targeted lure for users of the AI-native code editor, indicating awareness of developer tool trends.
  * **JetBrains:** A targeted lure for professional developers using established IDE products, broadening beyond AI-native tools.



Running alongside the AI-themed attacks, the same infrastructure served Mac utility scam pages, a classic malvertising category. Hostnames like _mac-clean-storage_ , _fixmymac_ , and _mac-support_ suggest that the threat actors target users searching for disk cleanup or system maintenance tools. The co-occurrence of both themes from the same campaign identifiers strongly suggests a single operator diversifying their lure portfolio.

Campaign timeline

![Figure 3. Daily traffic count showing five distinct campaign waves](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig3.jpg)

Figure 3. Daily traffic count showing five distinct campaign waves

TrendAI™ Research monitoring found weekly campaigns since April 8, with each week introducing new pages, keyword, and geographic targeting. 

**Wave 1: initial wave (April 8–13)**

**_753 traffic hits and 18 hostnames_**

The campaign launched with _claude-code-app.gitlab[.]io_ as the primary lure (486 traffic counts), supported by _claudeapp.gitlab[.]io_. Simultaneously, Mac utility-themed lures (_mac-clean-storage.gitlab[.]io_ , _mac-guide-tool.gitlab[.]io_) were also found to have been deployed, suggesting the same actor operated parallel campaigns.

A single Google Ads campaign ID (23736589328) drove the majority of the traffic, heavily targeting Taiwan (194 traffic counts), Malaysia (36), and Japan (34). This wave achieved the highest daily peak of the entire campaign at 192 traffic counts on April 10.

**Wave 2: diversification (April 14–21)**

**_246 traffic hits and 23 hostnames_**

In Wave 2, new Claude-themed variants appeared under _gitlab.io_ domain (claude-tool-app, claud-desktop-app, claudesktop, claude-desktop-apps) alongside expanded Mac utility lures (macsupp-group, macsupp-usb, jetbrains-apps-group). The introduction of "jetbrains" as a lure theme indicates deliberate targeting of professional software developers.

**Wave 3: peak infrastructure (April 22–28)**

**_652 traffic hits and 28 hostnames_**

This wave introduced _perplexity-platform.gitlab.io_ (33 traffic counts) and _chatgpt-codex.gitlab[.]io_ (12 traffic counts), expanding brand impersonation beyond Claude to other AI platforms. The domains _claude-desktop-lm.gitlab[.]io_ (203 traffic counts) and _cladesktop.gitlab[.]io_ (135 traffic counts) were also created and received more traffic, which suggests that more people are searching for Claude-related keywords compared to Perplexity or ChatGPT.

**Wave 4: ChatGPT and Codex pivot (April 29–May 5)**

**_248 traffic hits and 26 hostnames_**

The operators pivoted significantly toward ChatGPT and Codex branding with _codexgpt.gitlab[.]io_ (43 traffic counts), _chatgpt-codex-app.gitlab[.]io_ (23 traffic counts), and _chatgpt-codex-lm.gitlab[.]io_ (20 traffic counts).

Meanwhile, the Claude-themed attacks continued with _claudecode-desktop.gitlab[.]io_ (112 traffic counts) and _claudecode-download.gitlab[.]io_ (19 traffic counts).

**Wave 5: claude.ai platform abuse (May 6–14)**

**_294 traffic hits; shifted to claude.ai_**

In this wave, the campaign moved from self-hosted GitLab Pages to abusing claude.ai's legitimate shared chat feature. The attackers created weaponized "shared chats” on claude.ai (at least 45 unique share IDs observed) and ran Google Ads pointing directly to these URLs. The majority of the traffic in this wave was attributed to claude.ai’s shared chat feature (289 traffic hits).

This represents a significant escalation: victims now landed on claude.ai itself—a fully legitimate, trusted domain—making the attack virtually indistinguishable from genuine content.

The geographic targeting broadened in this wave, with victims who fell for the social engineering campaign coming from Singapore (43), Taiwan (35), India (23), Italy (21), and France (20).

**Wave 6: The complete shift to claude.ai’s shared chat feature (May 21–June 14)**

**_337 traffic hits; all observed activity occurred within claude.ai shared chat feature_**

In this wave, the campaign fully abused the claude.ai's legitimate shared chat feature. Atleast 61 unique shared IDs and 33 new Google campaign IDs were discovered in this wave.

This shift is particularly dangerous because every traditional defensive signal collapses: there is no suspicious domain to flag, no typographical errors for filters to catch, and no low-reputation host for security tools to block. The lure now lives on the same trusted infrastructure as the legitimate product, leaving defenders with no automated control to fall back on except end-user vigilance as the last and often least reliable barrier.

# How claude.ai shared chat was abused

The campaign's pivot to claude.ai shared chat on May 6 represents a significant tactical innovation in malvertising. The attackers leveraged claude.ai _'_ s "Share" feature to create persistent, publicly accessible URLs on a fully trusted domain. This section details how the threat actors used the shared chat as a new vector.

  * **The victim searches for an AI assistant**



The lure relies on the visitor already trusting both Google's sponsored placement and the claude.ai and _gitlab.io_ domains that follows. A _site:claude.ai_ search is enough to surface ads that look indistinguishable from organic results. 

While we could not directly replicate the “sponsored results”,TrendAI™ Research has observed that search queries for “claude”, “claude download” redirected to the previously mentioned malicious /share/ urls. 

  * **The victim’s click lands on a real claude.ai share URL**



The ad redirects to a Claude shared-chat URL of the form _claude[.]ai/share/ <uuid>?gad_source=1&gad_campaignid=<id>&gbraid=…&gclid=…. _Because the page is hosted on claude.ai with a valid certificate, security filters such as browser indicators, URL inspection, and even Safe Browsing-style heuristics see nothing wrong. 

  * **A fake support chat tells the user to open Terminal**



The shared chat impersonates "Apple Support" or "Corda Team" with a polished page title, an inline disclaimer, and step-by-step instructions to open Terminal and paste a command. Our analysis has seen at least two visual variants shown in figures 5 to 7.

![Figure 4. "Apple Support" variant — Shared by Apple Support, titled "Running Claude Code on Mac"](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig5.png)

Figure 4. "Apple Support" variant — Shared by Apple Support, titled "Running Claude Code on Mac"

![Figure 5. "Apple Support" variant — Shared by Apple Support, titled “Clearing disk space on macOS” ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig6.png)

Figure 5. "Apple Support" variant — Shared by Apple Support, titled “Clearing disk space on macOS” 

![Figure 6. "Corda Team" variant — same payload, slightly different framing. ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig7.png)

Figure 6. "Corda Team" variant — same payload, slightly different framing

  * **The prompt to paste a command**



The instruction looks innocuous: a single curl piped through  _base64 -d_. The encoded blob in the screenshots decodes to: 

**_hxxps://loserrq0j1sha8[.]com/debug/loader.sh?build=a39427f9d5bfda11277f1a58c89b7c2d_**

Upon visiting the website, _another zsh script_ with _base64_ -encoded data will be decoded and executed. 

![Figure 7. Snippet of initial script from the base64-decoded URL](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig8.png)

Figure 7. Snippet of initial script from the base64-decoded URL

The decoded data will first check if the Russian keyboard layout or input method is enabled on a macOS system. If it is enabled, it will write 'TRUE' to _IS_CIS_ and will not proceed with its main objective, which is executing the MacSync infostealer. 

![Figure 8. Code snippet of KeyboardLayout checking](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig9.png)

Figure 8. Code snippet of KeyboardLayout checking

If the value of _IS_CIS_ is “FALSE”, the loader script fetches and executes the MacSync infostealer. This malware harvests browser credentials and cookies, SSH keys, and cryptocurrency wallet files before exfiltrating the data to a second-stage host. 

![Figure 9. Code snippet of how MacSync infostealer was retrieved and executed ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig10.png)

Figure 9. Code snippet of how MacSync infostealer was retrieved and executed 

![Figure 10. Code snippet of MacSync infostealer ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig11.png)

Figure 10. Code snippet of MacSync infostealer 

At least 45 unique shared conversation IDs were observed, with the most heavily trafficked (_498818d9-1ddc-4fbb-9fa7-56dfb84840b0_) receiving 55 confirmed traffic counts across multiple countries.

Geographic impact

![ Figure 11. Top 10 countries affected by number of confirmed victim interactions](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/f/clickfix-malvertising/clickfix-fig12.jpg)

Figure 11. Top 10 countries affected by number of confirmed victim interactions

The campaign's geographic distribution reveals deliberate targeting of the Asia-Pacific region, which accounted for 67.4% of all confirmed victim traffic. Taiwan stands out dramatically with 772 traffic counts (30.5% of all traffic), far exceeding the next-highest countries Japan (201) and Singapore (188). This concentration suggests either geographic ad targeting settings favoring APAC or greater engagement rates from users in these regions with AI tool advertising. 

The shift to claude.ai abuse in Wave 5 shows geographic broadening: Singapore rose to the top spot, while India, France, and Italy saw increased targeting. This may reflect the attackers' ability to fine-tune Google Ads geographic targeting as they collected performance data across waves. 

**Conclusion and security recommendations**

This campaign demonstrates the continued evolution of malvertising tactics, specifically tailored to exploit the increased interest and adoption of AI. By combining paid search ads, the abuse of trusted hosting infrastructure, and the impersonation of multiple AI brands, the threat actors achieved broad global reach while maintaining an appearance of legitimacy that bypassed traditional security controls. 

The shift to abuse claude.ai's shared conversation feature marks a concerning new vector where threat actors weaponize AI platform features as social engineering delivery mechanisms. As AI tools become ubiquitous in developer workflows, TrendAI™ Research expects threat actors will increasingly exploit the trust users place in AI platforms. 

TrendAI™ Research continues to monitor this campaign and will provide updates as new activity or tactics emerge. We recommend the following best practices to minimize your organization’s risk:

****For organizations****

  * Educate developers about ClickFix attacks specifically targeting AI tool installation workflows. 
  * Monitor for execution of unexpected PowerShell or terminal commands following web browsing sessions. 
  * Deploy endpoint detection for the identified payload hashes and associated behavioral indicators. 



****For end users****

  * Always navigate directly to official product websites rather than clicking search ads for software downloads. 
  * Be suspicious of any "installation" process that requires copying and pasting commands from a web page, especially if the commands contain unreadable strings. 
  * Verify URLs carefully: even  _*.gitlab.io_ and claude.ai links can host malicious content. 
  * Use official package managers (pip, npm, brew, apt) for installing developer tools rather than following web-based instructions. 



****For platform providers****

  * GitLab: Consider additional vetting or rate-limiting of Pages sites that exhibit characteristics of phishing/social engineering content. 
  * Anthropic (claude.ai): Implement abuse detection for shared conversations that contain terminal commands, download instructions, or ClickFix patterns being linked from paid ads. 
  * Google Ads: Strengthen verification requirements for ads directing to *.gitlab.io subdomains or shared conversation URLs on AI platforms. 



**TrendAI Vision One™ Threat Intelligence Hub**

[TrendAI Vision One™ Threat Intelligence Hub](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. 

Emerging Threats: [ClickFix Malvertising Campaign Exploits AI Hype: From GitLab Pages to Claude.ai Abuse](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=ClickFix%20Malvertising%20Campaign%20Exploits%20AI%20Hype%3A%20From%20GitLab%20Pages%20to%20Claude.ai%20Abuse)

**TrendAI Vision One™ Intelligence Reports (IOC Sweeping)**

[https://portal.xdr.trendmicro.com/index.html#``/app/ti/intelligence``?intrusionSet=ClickFix%20Malvertising%20Campaign%20Exploits%20AI%20Hype%3A%20From%20GitLab%20Pages%20to%20Claude.ai%20Abuse](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=ClickFix%20Malvertising%20Campaign%20Exploits%20AI%20Hype%3A%20From%20GitLab%20Pages%20to%20Claude.ai%20Abuse)

**TrendAI Vision One™ XDR Data Explorer App**

TrendAI Vision One™ customers can use the XDR Data Explorer App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

More hunting queries are available for TrendAI Vision One™ with Threat Intelligence Hub entitlement enabled. 

**Indicators of Compromise**

Indicators of compromise can be found [here](https://documents.trendmicro.com/assets/txt/Indicators%20of%20Compromise%20\(IOCs\)-n9ZfTcK.txt).

Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Malware](/en/research.html?category=trend-micro-research:threats/malware) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article)

###  Authors 

  * Fyodor Yarochkin

Senior Threat Researcher

  * Joshua Paul Ignacio

Threats Analyst

  * Ryan Flores

Senior Manager, Threat Research




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)