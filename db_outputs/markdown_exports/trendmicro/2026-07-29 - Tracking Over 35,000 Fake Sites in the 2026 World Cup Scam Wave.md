# Tracking Over 35,000 Fake Sites in the 2026 World Cup Scam Wave

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/g/tracking-fake-sites-in-the-2026-world-cup-scam-wave.html
- **Date :** 2026-07-29

---

Cyber Threats

# Tracking Over 35,000 Fake Sites in the 2026 World Cup Scam Wave

Between January and June 2026, TrendAI™ tracked more than 35,000 fake sites exploiting the 2026 FIFA World Cup, spanning counterfeit merchandise shops, cloned ticket pages, and bogus free-streaming sites, which together drew roughly 1.48 million visits from Japan.

By: Kenichiro Motono 2026/07/29 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key takeaways

  * Between January and June 2026, TrendAI™ identified 35,538 malicious sites tied to the FIFA World Cup, which together drew roughly 1.48 million visits from Japan alone.
  * The activity falls into three main types: fake shops selling counterfeit merchandise, near-perfect clones of official ticket sites, and fake live-streaming pages that never actually show a match.
  * The cloned ticket sites are the most dangerous, harvesting credit card details and one-time passwords in real time so attackers can push through fraudulent payments even when multi-factor authentication is in place.
  * The best defense is caution: users should navigate directly to official websites, treat words such as "free" and "official" with suspicion, and never enter a one-time password on a page reached from a search result or ad.



# Introduction

From June 11 to July 19, 2026, the 2026 FIFA World Cup took place, co-hosted by the United States, Canada, and Mexico, drawing attention from fans around the world. Large-scale events like this are prime targets for cybercriminals, and online scams exploiting the tournament have been observed worldwide. This article explains the scam techniques TrendAI™ has identified and what internet users should watch out for.

It bears emphasizing that these scams merely impersonate FIFA, its affiliated organizations, official tournament partners, and legitimate broadcasters and video streaming services, none of which are in any way involved in the scams themselves.

# Tens of thousands of scam sites, millions of visits

In May 2026, the FBI's Internet Crime Complaint Center (IC3) issued a public service announcement ([I-052726-PSA](https://www.ic3.gov/PSA/2026/PSA260527)) warning of scams exploiting the tournament.

Between January and June 2026, we identified **35,538 malicious sites (scam, phishing, and similar sites), as well as suspicious sites whose safety could not be verified** , all containing the keywords "fifa" or "worldcup." We also confirmed that these sites were **accessed approximately 1.48 million times from within Japan**. That traffic surged as the tournament got underway, showing that Japanese users are among the primary targets.

In May 2026, the FBI's Internet Crime Complaint Center (IC3) issued a public service announcement ([I-052726-PSA](https://www.ic3.gov/PSA/2026/PSA260527)) warning of scams exploiting the tournament.

[ ![Figure 1. Visits from Japan to malicious and suspicious FIFA World Cup sites \(first half of 2026\). The sharp June rise coincides with the tournament kickoff on June 11.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/fig1.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/fig1.png)

Figure 1. Visits from Japan to malicious and suspicious FIFA World Cup sites (first half of 2026). The sharp June rise coincides with the tournament kickoff on June 11.

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/fig1.png)

The following sections examine the fake and scam sites we identified more closely.

# Fake shops selling fake merch

Between January and June 2026, we identified **6,251 fake shopping sites** containing the keyword "FIFA" or the Japanese terms for "World Cup" (ワールドカップ, W杯) or "Japan national team" (日本代表). Many of these had been set up well before the tournament began. To draw users in, attackers rely on techniques such as [SEO poisoning](https://www.trendmicro.com/ja_jp/research/25/i/fake-shopping-sites.html), which pollutes search engine results.[SEO poisoning](https://www.trendmicro.com/ja_jp/research/25/i/fake-shopping-sites.html), which pollutes search engine results.

[ ![Figure 2. The number of fake shopping sites related to the FIFA World Cup \(first half of 2026\)](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig2.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig2.png)

Figure 2. The number of fake shopping sites related to the FIFA World Cup (first half of 2026)

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig2.png)

[ ![Figure 3. Example of a fake shopping site](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig3.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig3.png)

Figure 3. Example of a fake shopping site

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig3.png)

These sites display soccer jerseys, tournament merchandise, and other goods, and their overall appearance and layout closely resemble those of legitimate Japanese online stores, but the attackers use various tricks to defraud users of their personal information and payments. Items purchased on these sites often never arrive, and when they do, they may be counterfeit or shoddy goods.

# Bogus ticket sites and card-skimming clones

## A near-perfect clone of the official site

We found a fake website that almost completely replicates the official FIFA hospitality site, where fans can purchase match tickets and hospitality packages. The fake site copies the official site's brand logo and page design, and it goes further: to appear more credible, it loads videos and images directly from the official site's servers and links to FIFA's official social media accounts and policy documents. It even has a built-in automatic translation feature, meaning users across many languages (including Japanese) are potential targets.

The fake site has a login page, but it has no real connection to FIFA's account system. If a user is tricked into entering their email address and password, the credentials are sent directly to the attackers.

[ ![Figure 4. An example of a fake site impersonating the official FIFA hospitality site](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig4.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig4.png)

Figure 4. An example of a fake site impersonating the official FIFA hospitality site

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig4.png)

[ ![Figure 5. Login screen on the fake site](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig5.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig5.png)

Figure 5. Login screen on the fake site

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig5.png)

### Real-time phishing to steal credit card details and one-time passwords

Going through with the checkout on this fake site can expose the user's credit card details and lead to direct financial loss. The whole process is designed to look and feel just like a normal online purchase, so it is hard to notice anything is wrong.

  1. The user enters their credit card details on the fake site's payment page
  2. The attacker obtains the card details in real time
  3. The attacker uses the card details to attempt a fraudulent payment elsewhere
  4. The user receives a one-time password for identity verification from their card company or bank, via SMS or other means
  5. The user enters the one-time password on the fake site's payment screen
  6. The attacker immediately uses the one-time password to complete the fraudulent payment
  7. The user is shown a fake order-confirmation screen



Identity verification with one-time passwords (multi-factor authentication) is an effective defense against payment fraud, but this technique bypasses it because victims enter the one-time password into the fake site themselves.

# Fake match streams, real profits for scammers

## Luring Japanese users to fake live-streaming sites

We confirmed that results for the Japanese search phrase "fifa ワールドカップ 2026 無料配信" (FIFA World Cup 2026 free streaming) led users to fake live-streaming sites. Here too, the attackers used SEO poisoning to game search rankings. Near the top of the video results sat the compromised website of a research institute at a US university. Those results were packed with Japanese-language titles posing as Japanese broadcasters and streaming services, and a single compromised site held multiple embedded fake pages, one for each match.

[ ![Figure 6. Fake pages \(on a compromised website\) displayed in Japanese search results](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig6.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig6.png)

Figure 6. Fake pages (on a compromised website) displayed in Japanese search results

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig6.png)

[ ![Figure 7. Multiple fake pages embedded in a compromised website](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig7.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig7.png)

Figure 7. Multiple fake pages embedded in a compromised website

[ ![Figure 8. Example of a fake live-streaming site \(1\)](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig8.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig8.png)

Figure 8. Example of a fake live-streaming site (1)

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig8.png)

[ ![Figure 9. Example of a fake live-streaming site \(2\)](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig9.png) ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig9.png)

Figure 9. Example of a fake live-streaming site (2)

[ download ](/content/dam/trendmicro/global/en/research/26/g/world-cup-scams/Fig9.png)

# What the fake-stream operators are really after

Clicking one of these search results carries the user from the compromised website, through relay pages hosted on blogging platforms, and on to a fake live-streaming site. The destination site poses as a sports-focused streaming service and offers pages named after real matches in the actual tournament schedule. A video-player mock-up on the page makes it look as though the match is about to start, but throughout our investigation we never saw any actual footage play.

The fake live-streaming sites have a malicious ad network (an advertising delivery network) built in, so each time the user clicks or taps the fake play button, they are redirected to a different site. The destinations included account-opening pages for legitimate financial trading services and major e-commerce sites. These legitimate businesses are themselves likely unwitting victims of ad fraud, with their affiliate advertising abused through the same malicious ad network.

Some of the fake streaming sites also flash a message that "registration is required to watch," sending users to a sign-up page. That page then harvests personal information and credit card details, or quietly enrolls victims in unrelated subscriptions that keep charging them on an ongoing basis. Whenever a major tournament, concert, or other high-profile event comes around, the attackers swap out their infrastructure and tactics and run the same fake live-streaming scam all over again.

# Staying a step ahead of the scammers

Cybercriminals exploit whatever topics and news attract the most public attention to deceive users. Don't take words such as "free" or "official" at face value. With a bit of calm judgment and the right security measures, they can protect their personal information and assets.

  * Shoppers should buy tickets, merchandise, and other goods by navigating directly to the official website, not through links in search results or social media ads.
  * When users do land on a site from a search, they should check the URL (domain) carefully. They should be wary of listings with unnatural titles, such as those stuffed with symbols.
  * Viewers should watch matches through official broadcasters and video streaming services. If an unofficial site advertising "free streaming" asks them to register an account or enter credit card details, they should not comply.
  * Even legitimate payments may redirect users to their card company's page for identity verification (3-D Secure) and ask for a one-time password sent by SMS. They should check that the merchant and amount in the SMS match the purchase they are actually making. If anything looks off, such as an unfamiliar amount or merchant, they should stop without entering the code and contact their card company or bank.
  * Users should use a different password for each service. If they reuse the same password across multiple services, a single password entered into a fake site can lead to the takeover of their other accounts.
  * Installing trusted security software, and making use of its advanced anti-scam features, is another effective safeguard.



# Proactive security with TrendAI™ products

[Trend Micro ScamCheck](https://shop.mmea.trendmicro.com/en_us/products/trend-micro-check.asp), a mobile app dedicated to scam protection, combines several AI technologies to protect users from increasingly sophisticated scams.

Its Web Threat Protection feature blocks access to malicious websites, including fake and scam sites. Its Scam Check feature uses generative AI to assess scams for users: from a screenshot of a suspicious email, advertisement, or social media post, it can determine whether a scam site is likely involved. For PC users, the same Web Threat Protection feature is built into [Trend Micro Maximum Security](https://www.trendmicro.com/en_us/forHome/products/maximum-security.html).

TrendAI™' security products help stop constantly evolving, increasingly sophisticated scams before they cause harm, letting defenders move toward proactive, AI-powered security.

**Research contributions**

  * Shingo Matsugaya (TrendLife Threat Research)
  * Makoto Shimamura (TrendLife Threat Research)



Tags

[Research](/en/research.html?category=trend-micro-research:article-type/research) | [Phishing](/en/research.html?category=trend-micro-research:threats/phishing) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Kenichiro Motono

Chief Fraud Prevention Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)