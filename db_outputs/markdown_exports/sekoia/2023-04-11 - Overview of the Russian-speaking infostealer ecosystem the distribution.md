# Overview of the Russian-speaking infostealer ecosystem: the distribution

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/overview-of-the-russian-speaking-infostealer-ecosystem-the-distribution
- **Date :** 2023-04-11

---

## Introduction

Among the infostealer families spread in the wild, a significant number is sold as a Malware-as-a-Service (MaaS) in the Russian-speaking cybercrime ecosystem. These activities allow threat actors to steal sensitive data (commonly named _logs_) in large amounts, which are then sold in centralised or decentralised marketplaces. Thus, multiple financially motivated cybercriminals specialised in the distribution of infostealers.

This blog post aims at presenting the main techniques, tools and social engineering schemes used by the cybercriminals from the Russian-speaking infostealer ecosystem and observed by Sekoia analysts in the past year. It is based on the monitoring of threat actors’ activities on underground forums and Telegram channels and the tracking of multiple distribution channels leveraged to distribute infostealers.

## Context

Over the past years, the cybercriminals in the Russian-speaking infostealer ecosystem leveraged multiple distribution channels to spread their malware to a large audience. Observed infection chains mainly combine social engineering on different mediums, and technical resources accessible with a low effort level.

The social engineering schemes used by threat actors responsible for redirecting user’s traffic to malicious content, commonly known as “[traffers](/blog/traffers-a-deep-dive-into-the-information-stealer-ecosystem)”, notably leverage fake installers of legitimate software, cracked versions of commercial software, and fake updates or business related documents. These lures are suitable for a high number of potential victims, including individuals on their personal machines, to employees on corporate networks. The social engineering schemes aim at gaining the trust of potential victims and redirect them to the adversary controlled resources.

Identified adversary controlled resources include landing webpages, websites or the malicious payload directly. These resources can be hosted on virtual private servers (VPS), compromised servers or legitimate abused web services. Some threat actors leverage traffic distribution systems (TDS) or content delivery networks (CDN _)_ such as Cloudflare to protect their server and to restrict access to the malicious content.

In addition to the social engineering methods, cybercriminals use techniques such as malvertising, SEO-poisoning, malspam and redirection from legitimate forum posts to lead victims on their resources. While malvertising and SEO poisoning aim to rank the malicious websites at the top of search engines results to widely relay a website, malspam and forum redirecting are used to target a specific range of potential victims.

The threat actors often discuss these techniques, tools and social engineering on underground forums, and share feedback, tips and tutorials. The following sections aim at presenting these TTPs, illustrate their use and share mitigation techniques.

## Malvertising and SEO-poisoning to spread malicious websites

### Large-scale malvertising

In the second half of 2022, Sekoia analysts observed multiple malicious websites impersonating legitimate webpages of popular software and promoted by trusted advertising services (such as Google Ads). This technique is usually named malvertising or malicious advertising.

Attackers take advantage of trusted advertising services to:

  * Ensure their websites rank as search engine top results, usually even before the impersonated legitimate website;


  * Gain the victim’s trust - as Google, Facebook, Bing and others are trusted third-parties for most of its users;
  * Widely relay their websites - as search engines are the most visited websites;
  * Target users based on their location or language - as most advertising services allow Pay-Per-Click advertising service customers to customise the targeting of their campaigns.



For example, in January 2023, an advertising campaign abusing Google Ads service spread a malicious website (_zoomdowndesktop[.]store_) impersonating the official Zoom website. The malicious website redirected the visitor to download a Vidar stealer payload.

![Google Ads is the service most abused by Russian cybercriminals to distribute infostealers.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a646adf0bb92a6517cb9_6a92a41ae9a71d422840649a_6a2a7a3bb97c48a61ea47031.webp)

Figure 1. Google Ads is the service most abused by Russian cybercriminals to distribute infostealers.

Based on our observations, Google Ads is the service most abused by cybercriminals to distribute infostealers. While less usual, the threat actors also use advertisements on other platforms with similar objectives and benefits. Sekoia analysts identified that cybercriminals abused advertising services also include those of Facebook, Instagram, Bing, Yahoo, Twitter, YouTube, TikTok, LinkedIn and Pinterest.

Mitigating malvertising technique is possible, notably through the installation of ad blocking browser extensions.

### A look at the use of Google Ads by Russian-speaking cybercriminals

While monitoring Russian-speaking cybercriminals on underground forums and Telegram channels, Sekoia identified procedures used by threat actors to exploit the Google Ads service for malicious purposes.

Cybercriminals use stolen or “ _warmed up_ ” Google accounts (_i.e._ accounts created and used in a legitimate way at first, and later leveraged to distribute malicious content). To warm up a newly created Google account, cybercriminals usually perform several operations to create a non-suspect Google profile. They first use a proxy address in the targeted country and then generate legitimate traffic from an anti-detect browser to create cookies from classic web browsing. A few days later, they create a new Google account and generate activities for several days from Google services, _e.g._ Drive, Calendar, Maps, Youtube.

We assess that the main reason for using stolen or “ _warmed up”_ accounts is that an existing account with activities, longevity and transaction history gain increased trust from a Google advertising policy point of view.The more human-like interactions the Google account has, the more credible it is from the vantage point of anti-bot algorithms, and the less likely it is to be detected.

For stolen and “ _warmed up_ ” Google accounts, the attackers then follow a Google Ads farming process, which consists in setting the profile with the identity of a real person, the IP address of the targeted country, a user-agent of a computer operating system, a phone number (excluding toll-free numbers) and the payment method which must be located in the target geolocation. The cybercriminals then pay for a first advertisement, which should be legitimate, and are encouraged to advertise “ _white offer_ ” (_i.e._ advertising redirecting to legitimate websites) to keep the trust of the check’ algorithms. 

The farming process is inevitable for threat actors to keep a good reputation and avoid bans, as well as to maintain a high billing rate and minimise the number of payments marked as suspicious. Sekoia analysts assess it is likely this technique is used by threat actors familiar with advertising platforms, and leveraged as operational security procedures to ensure that their campaigns are not hindered. Thus, they are not accessible to all criminals distributing _infostealers_.  
For landing pages impersonating legitimate software websites, some cybercriminals first set the Google ads with the original link of the impersonated website, and change it to the link of the malicious landing page after a few days. It is highly likely this technique would prevent the Google advertising service to detect and shutdown the [malicious advertisement](/blog/clearfake-a-newcomer-to-the-fake-updates-threats-landscape), and therefore ban the associated account.

### Business of _warmed-up_ and stolen Google accounts

Needed resources and complexity of making _warm-up_ and stolen Google accounts operational for the advertisement of malicious landing pages, are at the root of an underground business of Google Ads accounts. Some threat actors specialise in selling those.

Below is an offer of a Google Ads account put for sale in a specialised Telegram channel. Based on the capture of the threat actor’s Google Ads interface, the stolen account is active, credited every month with €1,000, located in Germany and used since 2018. These characteristics make this account particularly valuable, hence the amount of $2,500 set by the seller. We observed that the prices of ready-to-use Google Ads accounts can range from $100 to several thousand dollars. 

![Google Ads account sold in December 2022 on a Telegram channel dedicated to the distribution of infostealers by Russian cybercriminals.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a646adf0bb92a6517cb6_6a92a41951d97c29d2a30dad_6a2a7a3bb97c48a61ea4702e.webp)

Figure 2. Google Ads account sold in December 2022 on a Telegram channel dedicated to the distribution of infostealers by Russian cybercriminals.

Companies using Google Ads to advertise their products or services should be aware that threat actors hijack Google accounts to discreetly promote malicious websites. While compromised accounts are not easy to detect, monitoring advertising campaigns can contribute to identifying abuse of an associated account.

### SEO poisoning still in use to distribute infostealers

[SEO poisoning](/glossary/seo-poisoning) is a mechanism that consists in positioning a website at the top of search engine results, by abusing the ranking algorithms. In 2022, Sekoia observed this technique was still commonly used to distribute infostealers. 

Sekoia analysts notably identified SEO poisoning leveraged to deploy several loader malware families, including BatLoader, GootLoader, [PrivateLoader](/blog/privateloader-the-loader-of-the-prevalent-ruzki-ppi-service) or NullMixer, as well as widespread infostealers such as Redline, Raccoon and Vidar.

SEO poisoning remains one of the most effective and reliable technique for cybercriminals to:

  * Efficiently lure potential victims - as users intentionally search for the website, the conversion rate is therefore high;
  * Generate traffic on a long-term basis - poisoned websites can remain at the top of search engine results for several months or years;
  * Avoid detection - SEO poisoning is a complex threat to detect and mitigate.



As it requires a good knowledge of SEO and web development skills, Optimising search engine indexing is more challenging to implement than other traffic sources. Indeed, the threat actors should design and build a website with high-quality content, relevant keywords, multiple references to create user engagement and traffic. Sekoia analysts this almost certainly explains why this technique is leveraged by fewer, more advanced threat actors.

Websites leveraged through this technique are usually stealthier and more persistent over time, as detailed in our January 2023 [blog post](/blog/unveiling-of-a-large-resilient-infrastructure-distributing-information-stealers).

We therefore assess that SEO poisoning is a technique adopted by cybercriminals to operate long-term stealth distribution campaigns.

## Landing pages used by Russian cybercriminals to lure victims

In the second half of 2022 and early 2023, Sekoia analysts observed a resurgence of landing pages impersonating legitimate websites of popular software, such as Anydesk, Brave, Slack, TeamViewer and Zoom. We also track several infrastructures using landing page templates of cracked or legitimate free software catalogues to distribute commodity malware.

Both types of landing pages are social engineering techniques commonly used by cybercriminals to lure visitors and in most observed cases redirect them to download and execute an infostealer. From an attacker’s point of view, these websites are simple and fast to set up. When combined with efficient traffic generation techniques, these social engineering schemes can be complex to detect.

### Landing pages impersonating legitimate websites of popular software

Among all impersonated software, video games or authentication webpages, a new decoy appeared _en masse_ in early 2023: landing pages impersonating the OpenAI website. Indeed, the webpage introducing ChatGPT, an artificial intelligence chatbot developed by OpenAI, was actively used to trick users into downloading a malicious program masquerading as ChatGPT. This lure was notably used to distribute [Aurora](/blog/aurora-a-rising-stealer-flying-under-the-radar) and [Stealc](/blog/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-1) stealers.

![Legitimate webpage introducing ChatGPT and malicious one impersonated it containing a Download button. This technique is part of the infection chain system used by Russian cybercriminals. Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a646adf0bb92a6517cbc_6a92a41c2e47a1e9fe0e5ea0_6a2a7a3bb97c48a61ea47059.webp)

Figure 3. Legitimate webpage introducing ChatGPT and malicious one impersonated it containing a Download button. This technique is part of the infection chain system used by Russian cybercriminals. Source: Sekoia

Of note, Sekoia analysts observed malvertising campaigns using malicious landing pages that impersonate legitimate websites protected behind a traffic distribution system on multiple occasions, see the section Traffic Distribution System to generate high-quality traffic. Sekoia also observed that multiple threat actors leverage Cloudflare service as a proxy, to hide the origin server and restrict the access.

### Threat actors’ services selling landing pages on Russian-speaking underground forums

Landing page templates are commonly found in the Russian-speaking underground forums such as XSS and Zelenka, as well as on Telegram channels. They are notably sold by threat actors for a few dozen dollars, or offered as a priced service to develop landing web pages or websites.

Below is an example of a landing page service advertised on Telegram.

![Landing page template or development sold in a Telegram channel specializing in the distribution of infostealers by Russian cybercriminals. Source: Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a646adf0bb92a6517cb3_6a92a41bfd507e2a51b9a38e_6a2a7a3bb97c48a61ea47034.webp)

Figure 4. Landing page template or development sold in a Telegram channel _(hxxps://t[.]me/TrafLand)_ specializing in the distribution of infostealers by Russian cybercriminals. Source: Sekoia

 _(translated from Russian)_‍__

 __Landing pages for pouring out__  
 _Order a strait band: Designed (by template) - $10-15, Created from scratch - $20-40, Turnkey landing - $35-50 (+ hosting and domain)_  
_Additional services: Steal a ready-made landing page - from $25, Installation on hosting - $10_

In the above example, the threat actor going by the handle _nightiks_ sells already designed templates for a small fee. The templates pertain to respectively a catalogue of free Adobe software and the download webpage of OBS Studio. The threat actor clearly states that these landing pages aim at “pouring out”, which means spreading malware.

## Traffic Distribution System to generate high-quality traffic

More advanced threat actors leverage a **traffic distribution system (TDS) to protect their infrastructure** that hosts or redirects to malicious content and to select the targeted traffic. In the Russian-speaking cybercrime ecosystem, this technique is commonly referred to as “ _клоака_ ”, translated as _cloak_ , _cloaca_ or _cloaking_.

The TDS acts as an intermediate that filters incoming traffic to show different content to specific audience segments. A TDS redirects the human-like requests from the targeted audience to the adversary infrastructure, and redirects bot requests and unwanted traffic to an insignificant resource.

As for the SEO poisoning or the advertising, while this technique is not malicious _per se_ , it is used for malicious purposes by several threat actors.

The threat actors take advantage of TDS to generate high-quality traffic, allowing them to:

  * Target specific geographic locations, as the stolen data of users from some countries (_e.g._ US, Europe) is more valuable than others;
  * Prevent their infrastructure from being scanned, analysed, and detected, as TDS can reject requests of bots, scanners, or else based on specific user-agents, IP addresses, response time.



## Conclusion

Infostealers sold with this business model are accessible to a large number of threat actors at a lower cost. Since these infostealers are designed as turnkey solutions, operating them requires low technical skills. Monitoring the distribution channels in the wild or on [cybercrime forums](/blog/a-war-on-multiple-fronts-the-turbulent-cybercrime-landscape) allows Sekoia analysts to have an overall view of the most widespread, emerging and new infostealers distributed by cybercriminals from the Russian-speaking ecosystem. 

Multiple threat actors with heterogeneous levels of skills share similar techniques, tools and social engineering schemes with the aim of compromising large numbers of victims. To provide our customers with actionable intelligence, Sekoia tracks some of the most operated infection chains by proactively searching for webpages that reuse characteristics of the legitimate ones and templates of free or cracked software catalogues.