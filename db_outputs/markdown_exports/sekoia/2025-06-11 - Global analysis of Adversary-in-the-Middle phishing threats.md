# Global analysis of Adversary-in-the-Middle phishing threats

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/global-analysis-of-adversary-in-the-middle-phishing-threats
- **Date :** 2025-06-11

---

## Introduction

In recent years, organisations have increasingly encountered **massive and more sophisticated phishing attacks** that primarily target Microsoft 365 and Google accounts**using Adversary-in-the-Middle (AitM) technique**. This growing trend has been amplified by the **proliferation of Phishing-as-a-Service (PhaaS) offerings in the cybercrime ecosystem.** These services provide access to advanced phishing kits for a wide range of cybercriminals, including those with limited technical skills, at a lower cost.

AitM phishing kits mainly aim to **harvest session cookies** from targeted services to **bypass the Multi Factor Authentication (MFA) process during subsequent logins**. To achieve this, AitM phishing servers relay user inputs, including usernames, passwords and MFA codes, to the legitimate authentication API while intercepting the returned session cookie. With that cookie, an attacker can replay the session, and access the victim’s account without needing to perform any further authentication. Such compromises frequently lead to **significant financial losses via Business Email Compromise (BEC) operations** , financial fraud, or even Big Game Hunting ransomware attacks.

The Sekoia Threat Detection & Research (TDR) team closely monitors the AitM phishing attacks and regularly provides technical reports on emerging kits that we uncover through our daily threat hunting routine. This **global report delves into the threat posed by AitM phishing** , offering both contextual and operational insights. Using our telemetry data and research findings, this report explores current trends in the AitM phishing landscape and the prevalence of leading kits.

Additionally, the report delivers valuable and actionable intelligence to help analysts detect, identify and investigate the AitM phishing threat. It highlights detection opportunities and includes concise sheets for the eleven most widespread AitM phishing kits as of Q1 2025.

## Glossary of AitM terminology

Understanding Adversary-in-the-Middle (AitM) phishing involves grasping several technical concepts. To facilitate this comprehension, we have compiled a glossary of key terms associated with this threat.

### Phishing**-as-a-Service (PhaaS)**

Phishing-as-a-Service is a subscription-based model that provides cybercriminals with access to phishing kits and associated services. Most PhaaS platforms also offer additional features, such as anti-bot webpages, HTML and SVG attachment templates, and data forwarding to Telegram bots.

### Operator

In the PhaaS model, the operators are responsible for managing the entire service. This includes maintaining the kit’s source code, operating the shared infrastructure, advertising and selling the service, and providing customer support.

### Affiliate

Affiliates are cybercriminals who subscribe to PhaaS service. They usually pay a licence fee to access either a version of the kit’s source code or a web-based platform for managing phishing pages. Affiliates’ activities involve building target lists, conducting email campaigns, and monetising successful phishing attacks through Business Email Compromise (BEC).

### Reverse proxy

A reverse proxy server acts as an intermediary between the user’s device and the legitimate authentication service, relaying traffic and capturing sensitive user data in the process. This AitM method enables attackers to replicate authentication pages and intercept user requests. Phishing kits such as Evilginx, EvilProxy, and NakedPages use reverse proxy servers.

### Synchronous relay

The synchronous relay method involves phishing kits cloning legitimate authentication webpages to harvest user data, which is then forwarded to the legitimate authentication service in real time. Synchronous relay servers enable attackers to customise phishing pages. PhaaS platforms like Tycoon 2FA, Sneaky 2FA and Mamba 2FA employ synchronous relay servers.**‍**

### Centralised infrastructure

Within the PhaaS model, phishing kits generally rely on two types of infrastructure: servers that host phishing pages and servers that manage centralised functions such as licence verification and authenticating interactions with the legitimate services. While phishing pages are primarily hosted on servers controlled by affiliates, operators manage the centralised infrastructure.

### Anti-bot capabilities

Most phishing kits are equipped with anti-bot capabilities to prevent their pages from being detected by automatic scanners. These capabilities include CAPTCHA pages requiring human interaction, traffic filtering based on device fingerprinting (such as operating system, browser, IP address), code obfuscation, and URL randomisation.

## Adversary-in-the-Middle (AitM) phishing attacks

Threat actors increasingly conduct AitM phishing attacks, employing continuously evolving spearphishing techniques and leveraging a variety of kits available within the cybercrime ecosystem. Our analysis, along with open-source reporting, indicates that most AitM attacks rely on a common set of tactics, techniques, and procedures (TTPs).

AitM phishing pages predominantly target Microsoft 365 and, to a lesser extent, Google accounts - platforms that are prevalent in professional environments. Compromising these cloud accounts allows attackers to steal operational information from email inboxes, calendars, document storage, as well as to impersonate their victims.

The following section outlines the typical approaches used by attackers, from social engineering lures to Business Email Compromise (BEC) attacks.

### Social engineering lures

AitM phishing campaigns primarily target employees in finance, sales, human resources, and executive roles, capitalising on their connection to financial operations to facilitate BEC and other fraud. These large-scale campaigns now hit organisations worldwide.

The lures used in email phishing campaigns typically involve corporate matters, such as:

  * **Financial** : bonus distribution, invoice queries, benefits enrollments, compensation adjustment, tax reviews, contract renewals.


  * **Human resources** : vacations, salaries, payrolls notification, policy agreements, employee handbooks.


  * **IT and security** : policy updates, secured documents, messages, signature reviews.



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55369291914889ad0ba_6a92a1b52b0ef7af46bc37ec_6a2a7f6a4452dad8088e15ad.webp)

_Figure 1. Most frequently used words in attachment names of AitM phishing campaigns, as observed by Sekoia (January-April 2022)_

These phishing emails often use either attachments, such as PDF, SVG and HTML documents, or embed links in the email body that redirect users to malicious websites.

To trick victims, attackers commonly rely on the following social engineering strategies:

  * **Impersonation of trusted entities**



To establish trust, attackers spoof the sender’s display name or email address to pose as legitimate services such as Microsoft, Google, Adobe and DocuSign, or to impersonate organisation's departments, or executives.

  * **Urgency**



To prompt immediate action and defeat potential scepticism, the content of the phishing email highlights the urgency of the required action, often using a deadline or a potential restriction.

  * **Confidentiality requirement**



To prevent internal communication about the phishing email and isolate the victim, the message may invoke a privacy policy or claim that a personal document should not be shared.

  * **Security guarantee**



To gain confidence, the email may include a footer indicating a security scan that supposedly certified the email is safe, creating a false sense of confidence.

Many AitM phishing emails combine one or more of these strategies to maximise effectiveness.

### Common TTPs

As with other social engineering lures, most attackers follow similar TTPs during the stages leading up to a fake authentication page, including the initial malicious email, incorporating one or more redirection steps, and deploying anti-bot features.

In 2023, Sekoia analysts identified that adversaries had largely adopted the tactic of embedding **QR codes within documents** to redirect users to AitM phishing pages. By mid-2025, this technique remained widespread, even as security products became more effective at detecting phishing links distributed through QR codes.

Since 2024, we have seen a rise in the **use of HTML attachments** that directly execute JavaScript to render phishing pages. Two factors contribute to the emergence of this trend: these attachments are potentially less detectable by email security tools, resulting in higher success rate for email spamming campaigns. Additionally, several PhaaS providers, such as Mamba 2FA, Tycoon 2FA and Greatness, now offer ready-to-use HTML phishing templates to their customers, accelerating the adoption of this technique.

In early 2025, we noted a significant surge in the use of **malicious SVG attachments** leveraged to redirect victims to AitM phishing pages. First observed at the end of 2024, this technique involves SVG files that contain either JavaScript or an _xlink:href_ attribute. By April 2025, we observe that cybercriminals are making extensive use of malicious SVG attachments for both phishing and malware distribution, likely reflecting improved distribution and compromise rates. 

Regardless of whether attackers begin with QR code, HTML attachments, or documents-embedded links, the final stage is to redirect users to a final phishing page. To evade email filters and prevent scanners from accessing malicious domains, adversaries frequently insert one or more redirection steps. These steps often make use of legitimate domain names to build user trust and avoid detection by automated scanning tools. Attackers commonly exploit the **“open redirect” vulnerabilities** , injecting malicious URL into user-controlled parameters within legitimate applications to redirect visitors to arbitrary websites. In specific terms, open redirects rely on a URL parameter that specifies the destination link for the user.

Redirection pages controlled by adversaries often incorporate **traffic filtering mechanisms** , ensuring that the phishing page is displayed only to likely targets. This filtering may rely on either custom or commercialised traffic distribution systems (TDS) or on checks of users’ device characteristics. Typically, these mechanisms verify that the user's IP address originates from a residential internet service provider (ISP), and that the operating system and web browser are consistent with those used in corporate environments. For example, the Tycoon 2FA PhaaS integrates the BlackTDS service to prevent distributing phishing pages from being served to bots and analysis environments, while Mamba 2FA uses Adspect TDS for similar purposes.

Finally, in most AitM phishing campaigns, the malicious page is protected by a **CAPTCHA requiring human interaction**. These anti-bot webpages are usually provided by the PhaaS and integrate legitimate services (such as Cloudflare Turnstile, reCAPTCHA, hCaptcha), open-source solutions (like IconCaptcha), or custom CAPTCHAs.

Only after successfully navigating all these steps, users land on the AitM phishing page, which typically mimics either a Microsoft 365 or a Google authentication portal.

### Business Email Compromise (BEC) attacks

Upon compromising cloud accounts, attackers use gained access to conduct further BEC attacks, mainly focused on financial fraud, including:

  * **Internal and external spearphishing** : using a compromised employee account to impersonate them in a follow-up phishing campaign.
  * **Data exfiltration** : extracting documents from email inboxes and cloud storage.
  * **Various fraudulent transactions** : modifying banking details, issuing fake invoices, or instructing employees to transfer funds.



Successful financial fraud demands a comprehensive understanding of the victim's role, the organisation’s workflow, and both internal and external people interactions. Adversaries may spend days or weeks on reconnaissance.

To maintain access, attackers often add their own 2FA method after compromising the account, ensuring they can still access it even if session cookies are revoked. They may also create email forwarding rules that automatically redirect incoming messages to an attacker controlled email address, enabling continued information gathering even after the victim resets their account.

It is essential to note AitM phishing is also leveraged by espionage groups, such as the Russian state-sponsored intrusion set Calisto, as well as various Chinese groups. Their motivations, goals and TTPs differ from those of financially motivated intrusion sets and are not detailed in this report.

## Phishing-as-a-Service ecosystem

The PhaaS model lowers the entry barrier for threat actors by providing AitM phishing capabilities without requiring significant technical expertise or resources. This enables cybercriminals to achieve a quick return on investment.

The following section provides an overview of the current PhaaS ecosystem, highlighting the primary strategies employed by the PhaaS operators.

### Typology of PhaaS offerings

AitM phishing kits are typically **sold via monthly subscription plans** , ranging from $100 to $1,000. PhaaS platforms offer a **variety of features** , including email and **attachment templates** , **anti-bot capabilities** , an administration panel for managing campaigns and harvested data, and data forwarding to Telegram. The quality and completeness of these offerings enable cybercriminal services to differentiate themselves from competitors.

While most PhaaS providers offer customers source code that partially or fully implements AitM capabilities, requiring deployment on the client’s own infrastructure, other PhaaS operators host fully operational phishing pages on behalf of their clients. This type of service makes AitM phishing kits even more accessible to cybercriminals with limited technical skills.

**Sales and distribution of PhaaS** offerings typically **occur via Telegram channels** and private groups. These cybercrime services frequently use Telegram bots integrated with cryptocurrency payment gateways to streamline transactions and manage affiliate licences. PhaaS operators also use these channels to publish product changelogs and provide tutorials or videos that guide affiliates through onboarding and adopting new platform features.

Some PhaaS operators organise Telegram groups to foster a community where affiliates can seek help, discuss their operations, and trade data or services.

Additionally, we observed the use of secured messaging applications like Signal, Session, SimpleX, and Tox for similar purposes, although far less popular.

To illustrate the PhaaS model described above, the following figure examines the main operations conducted by the operator of Sneaky 2FA through Telegram.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55369291914889ad0c0_6a92a1b6878de395f10e8e28_6a2a7f6b4452dad8088e15b1.webp)

**_Figure 2. Typical Phishing-as-a-Service (PhaaS) operations for AitM phishing kits_**

### Timeline of prominent PhaaS

Over the past few years, we have witnessed the emergence and widespread adoption of multiple PhaaS platforms. The following section presents a graphical overview of their evolution, along with relevant background information.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55369291914889ad0b4_6a92a1b419d5c59537699939_6a2a7f6a4452dad8088e15aa.webp)

_Figure 3. Timeline of prominent Phishing-as-a-Service offering AitM phishing kits, between 2020 and 2025 as monitored by Sekoia_

**EvilProxy** has been offered as-a-service on the _Exploit_ cybercrime forum since August 2020, later expanding to the _XSS_ forum (July 2022), as well as on Telegram. The operator promoted the kit using terms such as “Phishing-as-a-Service” and “reverse proxy”.

The Microsoft Threat Intelligence team reported that phishing campaigns employing AitM capabilities have significantly increased since mid-2021, possibly using the EvilProxy service and the open-source tool Evilginx.

In 2022, the services **Caffeine** , **NakedPages** and **Greatness** were released and sold on Telegram. The same year, W3LL integrated AitM capabilities into its phishing kit to target Microsoft 365 accounts. Although all three AitM phishing kits have been used for several years, NakedPage and Greatness remain among the most prevalent in 2024 and early 2025.

In a June 2023 report on AitM phishing and BEC attacks, Microsoft Threat Intelligence mentioned a new synchronous AitM phishing kit operated by a threat actor tracked as **Storm-1167**. TDR has been monitoring the related adversary infrastructure and assess with high confidence that the Storm-1167 phishing kit is part of a PhaaS offering with hundreds of customers as of April 2025.

In October 2023, we analysed the new **Dadsec OTT** phishing kit sold as-a-service, which emerged in May 2023 and was quickly adopted by threat actors. By the end of that year, it became one of the most popular phishing pages platforms. We believe this PhaaS was rebranded as **Rockstar 2FA** around December 2023.

Later in 2023, while analysing the trendy QR code phishing campaigns, TDR analysts uncovered the new **Tycoon 2FA** phishing pages operated by the Tycoon Group’s PhaaS, which partially reused the Dadsec OTT source code. Since then, Tycoon 2FA has become the most widely used PhaaS.

We also published findings on another new AitM phishing kit, dubbed **Mamba 2FA** , which has been in use since at least November 2023. Following our in-depth analysis, we concluded that Mamba 2FA was sold as-a-service to dozens of affiliates.

In 2024, several new AitM phishing kits, including **Sneaky 2FA** , **CEPHAS** , **Gabagool** , **Saiga 2FA** and **Legions 2FA** entered the market, allegedly under the PhaaS model. Although phishing pages associated with these emerging services are not as widespread as those of established players, they are gradually gaining ground. For instance, our SOC platform recorded a surge in Sneaky 2FA detections during Q1 2025, nearing those of the top 5 AitM phishing threats.

### Tools and services to set up phishing attacks

In addition to PhaaS offerings, various **tools and services are available in the cybercrime ecosystem to facilitate the set up of phishing attacks**. These resources support AitM techniques, as well as more generic phishing activities.

To operate their spamming email campaigns, threat actors use email sending software, often referred to as “sender” or “mailer”, or delivery services that bundle multiple capabilities. These capabilities include generating email content, attachments, and headers, but also sending bulk emails and managing SMTP configurations. Cybercriminals use both legitimate email sending tools or services, such as SendGrid, Mailgun, and Mailchimp, and custom tools that offer features better suited for phishing activities. These features may include proxy servers rotation, obfuscation of attachments, and email spoofing.

To maximise deliverability, cybercriminals might purchase services to “warm up” SMTP domains and servers for weeks or months before launching their spamming campaigns. This warming service involves SMTP infrastructure for benign activities initially, helping them build reputation and prevent their phishing traffic from being flagged or blocked by security solutions. 

Additionally, adversaries can purchase the following from specialised threat actors:

  * Mailing list data, also known as “leads”
  * “SMTP checkers” to verify and parse lists of email addresses
  * Access to compromised email address within specific domain names 
  * Pre-configured or compromised SMTP servers
  * Attachment templates or code for anti-bot or redirection infrastructure
  * Traffic Distribution System (TDS) services



## Investigating AitM phishing threats: methods and findings

Since 2023, the TDR team has actively monitored AitM phishing threats by developing detection rules, creating tracking heuristics, uncovering phishing infrastructures, and unveiling campaigns using malicious attachments, URLs, or redirection steps.

The following section outlines the monitoring techniques we employ, discussing their advantages and limitations, and provides an overview of prominent phishing kits as of early 2025.

### TDR monitoring of AitM phishing threats

#### Detection and CTI production

To ensure broad coverage of AitM phishing threats, the TDR team primarily focuses on writing detection rules and tracking the adversaries’ infrastructure.

Our detection efforts concentrate on anomalies and characteristic patterns in Microsoft Entra ID authentication logs to identify successful AitM phishing attempts. Synchronous phishing kits often contain inconsistencies in User-Agent and Application ID values during authentication, which we correlate using Sigma detection rules. Further details on detection opportunities can be found in the section titled “Detection opportunities”.

Additionally, some detection strategies are based on the URL and subdomain patterns used by certain AitM phishing kits.

Adversary infrastructures Indicators of Compromise (IoCs) collected by TDR include domain names and servers hosting anti-bot and phishing pages, those involved in exfiltration of harvested data, and IP addresses communicating with legitimate authentication services, notably the Microsoft API.

Our methodology involves proactive heuristics to identify active servers by analysing HTTP responses, HTML pages, and URL patterns. To achieve this, we rely on both scanning search engines like Censys, urlscan.io, Virus Total, or conducting targeted scanning campaigns on phishing endpoints.

### Sekoia.io telemetry

By analysing telemetry data from our detection rules alongside actionable CTI on the Sekoia SOC platform, we gain valuable insights into the most widespread kits. Before presenting the results, we outline some strengths and limitations of Sekoia.io telemetry.

  * **CTI-based telemetry**



The Sekoia SOC platform records hits of Indicators of Compromise (IoCs) derived from our tracking heuristics. This metric measures phishing kits’ prevalence by observing network logs in environments monitored by Sekoia.io. The main advantage is the proactive monitoring of adversary infrastructures, such as anti-bot and phishing domains and exfiltration servers, detected through network monitoring.

For self-hosted phishing kits, monitoring the number of active servers gives a good insight into how many affiliates are using a given PhaaS offering.

However, coverage bias can arise due to different levels of complexity in tracking the servers for different phishing kits. Additionally, this telemetry relies on scans which may be delayed by a few days compared to the actual infrastructure deployment.

  * **Pattern-based telemetry**



Detections generated by our rules on customer logs, primarily leveraging anomalies in Microsoft Entra ID audit logs. This real-time detection approach relies on unique rules, often resilient over time with low false positive rates, that catch most AitM phishing attacks for a given kit.

The main limitation is the reliance on identifiable anomalies specific to the phishing kit, that are mostly introduced by the developer for synchronous AitM phishing kits.

General biases of our telemetry include the predominance of data from European-based organisations with a certain cybersecurity maturity to collect Entra ID logs and ingest them into the SOC platform.

The figure below presents insights from for both CTI and detection-based telemetry in the Sekoia SOC platform.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55369291914889ad0b7_6a92a1b3e17eff730b64ee7d_6a2a7f6a4452dad8088e15a7.webp)

_Figure 4. Telemetry of prominent AitM phishing kits from Sekoia SOC platform_

#### Hunting AitM phishing campaigns in the wild

To offset biases in our telemetry, we engage threat hunting by employing multiple tracking strategies across various services to monitor AitM phishing campaigns in the wild.

Since the widespread adoption of QR codes redirecting to AitM phishing pages in 2023, we have been actively monitoring attachments embedding these QR codes. By searching for documents (PDF, HTML, DOC, _etc._) that embed QR codes redirecting to CAPTCHA services like Cloudflare Turnstile, hCaptcha or reCAPTCHA we can identify numerous attachments used in AitM phishing campaigns. These documents typically redirect users to anti-bot webpages. By analysing the resulting URLs, we can identify which phishing kits are being used and to map prevailing trends. Moreover, this proactive approach helps uncover emerging phishing kits.

While most PhaaS implementations rely on anti-bot webpages using CAPTCHA services with human interaction checks, some - like Mamba 2FA or Greatness - do not use them. Therefore, this approach does not cover all AitM phishing kits.

We also use signatures to detect malicious SVG and HTML files, which are widely used in early 2025, as well as anti-bot and lure webpage templates, that are commonly employed by various cybercriminals.

This proactive threat hunting provides a comprehensive overview of various phishing campaigns targeting organisations worldwide, and supplements our insights obtained with Sekoia.io CTI and detection telemetry.

### Most relevant phishing kits

By using the methodologies described above, our monitoring of AitM phishing threats from January to April 2025 resulted in the following prevalence table.

For each AitM phishing kit, we assigned a score (out of 5) to assess its prominence based on observations from our telemetry, adversary infrastructure monitoring, and threat hunting activities.

**AitM phishing kit**| **CTI telemetry**| **Detection telemetry**| **Number of servers**| **Number of domains**| **Threat hunting**| **Global**  
---|---|---|---|---|---|---  
**Tycoon 2FA**|  _5_|  _5_|  _4_|  _5_|  _5_| **4.8**  
**Storm-1167**|  _5_|  _3_|  _4_|  _5_|  _4_| **4.2**  
**NakedPages**|  _4_|  _2_|  _5_|  _5_|  _4_| **4**  
**Sneaky 2FA**|  _4_|  _2_|  _5_|  _4_|  _3_| **3.6**  
**EvilProxy**|  _5_|  _2_|  _5_|  _4_|  _0_| **3.2**  
**Evilginx – ywnjb**|  _4_|  _2_|  _4_|  _5_|  _1_| **3.2**  
**Saiga 2FA**|  _4_|  _3_|  _NA_|  _3_|  _1_| **2**  
**Greatness**|  _4_|  _0_|  _3_|  _3_|  _0_| **2**  
**Mamba 2FA**|  _2_|  _3_|  _NA_|  _1_|  _0_| **1.75**  
**Gabagool**|  _1_|  _1_|  _3_|  _2_|  _0_| **1.6**  
**CEPHAS**|  _0_|  _0_|  _NA_|  _2_|  _1_| **0.6**  
  
 _Table 1. Prominence of AitM phishing kits according to Sekoia observations from January to April 2025_

 _* Scores are out of 5._

We assess with high confidence that this **ranking accurately represents the most active AitM phishing threats in early 2025**.

In the first months of 2025, the **Tycoon PhaaS** has shown significant activity, with dozens of new domain names being registered daily and protected behind Cloudflare. Additionally, the service updates the Tycoon 2FA source code and anti-bot pages weekly. We believe the frequent rotation of new anti-bot pages is intended to evade detection based on the HTML, potentially extending the time a domain can be used before being flagged as phishing by Cloudflare.

The alleged PhaaS offering the **Storm-1167** phishing kit also provides cybercriminals with a comparable service, featuring a large centralised and frequently renewed infrastructure along with regular updates to anti-bot pages. We estimate that the PhaaS has several hundred active affiliates, inferred from the domain names registered, which are likely associated with unique affiliates.

**NakedPages** and **EvilProxy** are both long-standing PhaaS that have maintained approximately 220 and 280 distinct active servers on average, from January 2024 to April 2025. Although this number fluctuates slightly month to month, we believe it accurately reflects a consistent affiliate base. Both services operate with decentralised infrastructure, allowing each affiliate to install the kit on their own server. Consequently, we estimate that each could have between 150 and 250 customers.

Emerging at the end of 2024, **Sneaky 2FA** and **Saiga 2FA** , both fully-featured PhaaS offerings, have since been widely adopted by threat actors, as evidenced by Sekoia.io’s CTI and signature-based telemetry.

The open-source AitM phishing kit **Evilginx** remains one of the most prevalent as of early 2025. Notably, we identified a Evilginx configuration, also known as “phishlet”, that is likely shared or sold within cybercrime communities and is widely used by threat actors. TDR analysts are tracking the associated infrastructure cluster as “Evilginx - ywnjb” based on the subdomain “ _ywnjb.*_ ”used as a reverse proxy for the legitimate Microsoft FQDN _login.live[.]com_. Of note, _YWNjb_ is “ _acc_ ” encoded in base64, likely corresponding to the term “ _account_ ”.

The **Mamba 2FA** PhaaS ranks 9th in our list of the most prevalent phishing kits in early 2025. We estimate this ranking may be underestimated because our metrics consider the number of active servers and phishing domain names. In contrast, Mamba 2FA employs a decentralised infrastructure with fewer domains compared to other kits. Sekoia.io telemetry indicates that compromises via Mamba 2FA occur fairly frequently.

While the ranking of the most prevalent AitM phishing kits offers valuable insights into prominent threats, it is important to acknowledge that our findings are influenced by our monitoring methodologies, which primarily focus on French and European organisations. Despite this inherent bias, the ranking remains informative and helps prioritise detection and monitoring efforts on the most significant threats.

_For every phishing kit we mention, technical artifacts are available on_[ _the SEKOIA-IO/Community GitHub repository_](https://github.com/SEKOIA-IO/Community/tree/main/IOCs/global-analysis-aitm-phishing-threats) _, including summary sheets, HAR captures, anti-bot page screenshots, and more._

_If you are a SOC or CERT, we can share additional detection opportunities with you under TLP:AMBER. Please contact tdr [ at ] sekoia [ dot ] io.p_

## Read the full version of this article in PDF format

 _This blogpost is an abridged version of the report. The_[ _full version is available as a PDF_](https://0H3WGygmjL.flowdrivecdn.com/Akqb495rvnEUbGCEOpu5E) _._