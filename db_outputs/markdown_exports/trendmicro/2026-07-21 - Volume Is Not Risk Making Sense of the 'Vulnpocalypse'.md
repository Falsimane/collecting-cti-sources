# Volume Is Not Risk: Making Sense of the 'Vulnpocalypse'

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/g/making-sense-of-the-vulnpocalypse.html
- **Date :** 2026-07-21

---

Exploits & Vulnerabilities

# Volume Is Not Risk: Making Sense of the 'Vulnpocalypse'

A briefing for security leaders on separating vulnerability disclosure volume from exploitable risk in 2026.

By: Johnny Hand 2026/07/21 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

Around 66,000 common vulnerabilities and exposures (CVEs) are projected to be disclosed this 2026, according to the [FIRST 2026 Mid-Year Vulnerability Forecast](https://www.first.org/newsroom/releases/20260615). Vulnerability researcher Jerry Gamblin revealed that disclosures in the first half of the year ran [nearly 50% ahead of the same window in 2025](https://jerrygamblin.com/2026/07/01/3528/), which itself finished at a record [48,185 CVEs](https://jerrygamblin.com/2026/01/01/2025-cve-data-review/). His analysis draws on National Vulnerability Database (NVD) and CVE Program data. The steep climb from the roughly 40,000 CVEs recorded in 2024 might make the “vulnpocalypse” panic justified. 

![Figure 1. The steep climb of vulnerability disclosures from 2024, 2025, and the projected figure in 2026. ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/vulnpocalypse/Vulnpocalypse-Fig-1.jpg)

Figure 1. The steep climb of vulnerability disclosures from 2024, 2025, and the projected figure in 2026. 

The data: Volume vs. exploitable risk

Separating disclosure volume from dangerous risk is a key strategy in facing the forecasted overwhelming volume. As the raw count balloons, the share of critical vulnerabilities has roughly halved, falling from approximately 13% in 2024 to 7% in 2025 based on an analysis by [Zafran](https://www.zafran.io/resources/the-2025-spike-in-vulnerabilities-isnt-the-full-story) that draws on National Institute of Standards and Technology (NIST) National Vulnerability Database data. The slice that is actively exploited in the wild remains remarkably stable at [well under 1%](https://www.businesswire.com/news/home/20260225646974/en).

Metric | 2024 | 2025 | 2026 (Projected)  
---|---|---|---  
Total disclosed CVEs | ~40,000 | 48,185 | ~66,000  
New CISA KEV entries | ~186 | 245 | ~290 – 300 pace  
Critical severity share | ~13% | ~7% | Trending lower  
Actively exploited | <1% | <1% | <1%  
  
Table 1. Disclosure counts (NIST NVD) and CISA KEV entries (FIRST full-year projection)

According to the [FIRST Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/), only around 5% of all published CVEs are ever observed being exploited. The CISA KEV catalog grew meaningfully, from 1,239 entries at the end of 2024 to 1,484 at the end of 2025, but that is a rounding error against the tens of thousands of new disclosures.

The challenge lies in the massive triage bottleneck that the vulnpocalypse will create; the NVD fully analyzed only about 28% of newly disclosed CVEs in 2025, but not a proportional explosion of exploitable risk, according to the Zafran analysis. [NIST](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth#:~:text=This%20change%20is%20driven%20by%20a%20surge%20in%20CVE%20submissions%2C%20which%20increased%20263%25%20between%202020%20and%202025.%20We%20don%E2%80%99t%20expect%20this%20trend%20to%20let%20up%20anytime%20soon.%20Submissions%20during%20the%20first%20three%20months%20of%202026%20are%20nearly%20one-third%20higher%20than%20the%20same%20period%20last%20year.) itself confirms the strain: the agency reported a 263% jump in submissions since 2020 and is now triaging enrichment by risk tier rather than analyzing every CVE.

Why the raw number is exploding

It should be noted that the surge in CVEs is not a sign that software suddenly became dramatically less secure, rather, it is driven by three structural factors:

**AI-assisted discovery**  
Autonomous bug-hunting is pointing frontier models at decades of legacy code. Models such as Anthropic’s Mythos and OpenAI GPT 5.5 are highly effective at surfacing latent stability bugs. However, volume is not risk: the Linux kernel alone now accounts for more than 5,800 CVEs because its CVE Naming Authority (CNA) assigns an identifier to nearly every bugfix, even where no security impact is demonstrated. The real-world exploitation rate across that set sits near zero (on the order of 0.02%). Finding a flaw and having it weaponized are very different events.

**Changes in structural reporting**  
The discovery and cataloging infrastructure is catching up, inflating counts without changing actual exposure. This includes a roughly 449% year-over-year jump in GitHub Security Advisory volume and a large backlog of previously unassigned vulnerabilities finally being cataloged.

**Product sprawl**  
The number of distinct products with tracked vulnerabilities has grown by orders of magnitude. More software simply means more CVEs. This also applies to code: as more code is written into existence by AI and coding agents, more bugs are also written into existence. 

The real threat is speed, not volume

The metric that actually matters is speed. The window between disclosure and exploitation is collapsing from weeks to hours, and a rising share of exploitation now begins before a vendor patch is even public. In response, CISA recently retired its flat 14-day KEV remediation deadline in favor of a risk-based model that can demand action in as little as three days for the highest-risk combinations.

This is where AI Operational Excellence and proactive intelligence become mandatory. [The TrendAI™ Zero Day Initiative™ (ZDI)](https://www.zerodayinitiative.com/) exists to close this gap on the front end. Supported by more than 19,000 contributing researchers, TrendAI™ ZDI accounted for roughly 60% of the world’s coordinated disclosures in [a 2023 independent tally](https://www.trendaisecurity.com/explore/omdia-research/2672-ns-en-rpt), including [57% of critical-severity flaws](https://www.trendmicro.com/en_us/research/24/f/omdia-vulnerabilities-report.html), and turns those findings into protection that reaches customers an average of 115 days ahead of the vendor patch. When attackers weaponize zero-days against edge devices on day zero, pre-disclosure protection is no longer optional.

An action plan for security leaders

To weather what 2026 is set to bring, security programs must shift from counting raindrops to neutralizing the flood. Security leaders should be asking, “Are we still reporting CVE counts, or have we pivoted our metrics to exploitability?” The teams that succeed in 2026 will not be the ones who patched the most; they will be the ones who knew exactly what to patch first. The following best practices are recommended to minimize overwhelm and address vulnerabilities strategically: 

**Stop reporting raw CVE counts to the board**  
Raw numbers frighten without informing. Report the actionable slices and trends based on the data on hand.

**Triage KEV-first, then EPSS**  
Confirmed exploitation is the sharpest filter available. Patch the top exploitability percentiles at zero-day urgency, and let the rest follow standard cadences.

**Buy back time with virtual patching and containment**  
When exploitation outpaces the fix or a vendor patch does not yet exist, shielding vulnerable systems at the network or workload layer neutralizes the exploit path without waiting on a code change. Virtual patching and containment turn the disclosure-to-patch gap from an open exposure window into a managed one, and they matter the most for exactly the small set of actively exploited flaws that triage surfaces.

**Invest in automation, not a bigger patch treadmill**  
Enrichment and triage loads are doubling while urgent live-system patching remains flat. Budget for intelligence that cuts through the noise.

**Close the metadata gap**  
A large share of new CVEs arrive without complete severity or product data. Lean on exploitability intelligence rather than raw catalog fields.

Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Exploits & Vulnerabilities](/en/research.html?category=trend-micro-research:threats/exploits-and-vulnerabilities)

###  Authors 

  * Johnny Hand

Global Chief Information Security Officer




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)