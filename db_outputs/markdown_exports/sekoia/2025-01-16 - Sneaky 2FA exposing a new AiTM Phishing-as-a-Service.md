# Sneaky 2FA: exposing a new AiTM Phishing-as-a-Service

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/sneaky-2fa-exposing-a-new-aitm-phishing-as-a-service
- **Date :** 2025-01-16

---

## Introduction

In December 2024, during our daily threat hunting routine, we uncovered **a new Adversary-in-the-Middle (AiTM) phishing kit targeting Microsoft 365 accounts**. These phishing pages have been circulating since at least October 2024, and during that period, we identified potential compromises through the Sekoia.io telemetry.

Our analysis showed that this kit is being **sold as**[**Phishing-as-a-Service**](/blog/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1)**(PhaaS)** by the cybercrime service “ _Sneaky Log”_ , which operates through a fully-featured bot on Telegram. Customers reportedly receive access to a licensed obfuscated version of the source code and deploy it independently. Currently, Sneaky 2FA’s phishing pages are hosted on compromised infrastructure, frequently involving WordPress websites, and other domains controlled by the attacker.

Sekoia’s Threat Detection & Research (TDR) team obtained the leaked source code for further analysis. During our investigation, we discovered that the phishing kit includes some source code from the W3LL Panel OV6, an AiTM phishing kit reported by Group-IB1 in September 2023.

This blog post provides an overview of the Sneaky 2FA phishing kit, explaining its functionality and the related cybercrime service operating on Telegram. Additionally, it shares detection opportunities, as well as Indicators of Compromise (IoCs) associated with Sneaky 2FA’s phishing campaigns.

## Characteristics of Sneaky 2FA

The following analysis is based on Sneaky 2FA phishing campaigns identified in the wild, as well as its purported source code.

### URL patterns

#### Autograb

Sneaky 2FA implements the _autograb_ functionality to automatically prefill the Microsoft phishing page with the victim’s email address. To achieve this, the phishing URL includes the email address as a parameter, either in plain text or encoded in base64. For example:

`hxxps://mysilverfox.com[.]my/00/#victim[@]example[.]com  
  
hxxps://highnationservices[.]com/n/#victim[@]example[.]com  
`

The server then extracts the email address and inserts it into the username field of the fake Microsoft authentication page presented to the victim.

#### Fake Microsoft authentication pages

Sneaky 2FA phishing URLs are generated using 150 alphanumeric characters, followed by the path `/index`, `/verify` and `/validate`. This pattern offers opportunities for tracking.

We observed that most customers of the phishing kit service deploy the server in a dedicated repository, named `/auth/` by default.

Below are examples of Sneak Log phishing URLs identified in December 2024:

`hxxps://kagumigroup[.]id/wp-content/plugins/well/auth/j9P8KGpfDZyoHplo5XdnHOw79OCkDYo2l7TQcrrnclSz2XGLzmtCghFJwIWR1AaW33Rk36Z0ymZc6DIgMy4EFqTsiiqAKEBIN5jiTbYAUk1BfG4uoVhetLa2XWebUSShQOFq7L8Mpx1vf4Pum0xBVx/verify  
  
hxxps://mysilverfox.com[.]my/00/7N0tV3XAh1yp4NFo9X6YsH3cOam6DYJhmMEXRky24mzGUuTE2RpwIIlI4olBypVCEYqiKFPDTAsRvKrS8bgiKBOZiPOUnxoCSHveA0zk5hcdjQ1UltSxdw7rdgZoo7HDWorfj9CzN8gc0q5PQ19nZe/index  
  
hxxps://highnationservices[.]com/n/uswDOVS70y9sjyPwtLieCJdZiEUGhokxRUvY7JApYlFo35Sb9o66AvhK8oNrHPTgj9aaJDHItTWDnPOo3t4mz8Tfhf7GBem0YE1cqx8O13VoKuWIbN4knGg6fRrvMIZXRQ2xgdEFzj2mVBzwSbpe5c/validate  
`

### Anti-bot and anti-analysis features

#### Cloudflare Turnstile page

Sneaky 2FA phishing pages can be protected by Cloudflare Turnstile2 or reCAPTCHA pages to determine whether the user behaves like a human rather than a bot. As of December 2024, we only observed the use of Cloudflare Turnstile prior to accessing fake Microsoft authentication pages.

![Sneaky 2FA page embedding a Cloudflare Turnstile challenge](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57ba54c8f443fa4ddbe_6a92a21916f788fda8e46cc4_6a2a7ecde2d8f7e583cbb413.webp)

Figure 1. Sneaky 2FA page embedding a Cloudflare Turnstile challenge

Cloudflare Turnstile pages have the following characteristics:

  * Initially, it returns an HTML page with food-related content, titled “Gourmet Delights and Beverage”. This page uses the JavaScript function `window.location.reload()` to load the Cloudflare Turnstile webpage. This page is not visible to the victim and likely serves to present a benign page to scans.


  * The HTML title is randomly selected from the following list:



Verify your account  
Verify your identity  
Verify your credentials  
Verify your informations  
Verify your email  
Verify your login  
Confirm your account  
Confirm your identity  
Confirm your credentials  
Confirm your information  
Confirm your email  
Confirm your login  
Signin to your account 

  * The favicon is a base64-encoded Microsoft logo (SHA256: `5d91563b6acd54468ae282083cf9ee3d2c9b2daa45a8de9cb661c2195b9f6cbf`)


  * The page’s background is a transparent colour variant with Microsoft colours, also base64-encoded in the HTML body (SHA256: `8c4e78b1bc0a0923fccc0cd2d7ca06023b6ab15af079e6b19d7d5d2fddc5488d`)


  * JavaScript code loads the Cloudflare Turnstile challenge.



#### Anti-debugging techniques

Sneaky 2FA pages use anti-debugger techniques to prevent analysis using web browser developer tools. Some of these techniques are described in the TRAC Lab’s report3, which analyses a campaign distributing the WikiKit phishing kit, that we identified as Sneaky 2FA.

#### HTML and JavaScript obfuscation

HTML and JavaScript code are partially obfuscated using the following techniques:

  * HTML tags: The fake Microsoft authentication pages embed HTML tags that separate text copied from legitimate Microsoft pages. This obfuscation is invisible to victims but is likely intended to prevent security scans from detecting that Sneaky 2FA pages are impersonating Microsoft. For instance, the HTML code below displays the texts “No account?” and “Sign in”:



`N<a class="kzoNmrYqOS"></a>o a<a class="kzoNmrYqOS"></a>cc<a class="kzoNmrYqOS"></a>ou<a class="kzoNmrYqOS"></a>nt?  
  
S<b></b>i<b></b>g<b></b>n in  
`

  * Images: Some pages embed text as images, and all images are embedded in the HTML code as base64-encoded data. These techniques may help evade security tools that scan for known text or image patterns.


  * Junk data: The HTML code includes junk data within the body, which is not visible to the victim.



#### Traffic filtering

Sneaky 2FA attempts to determine whether a visitor's IP address originated from a data center, cloud provider, bot, proxy, VPN, or is associated with known abuse. If the IP address meets any of these criteria, the visitor is redirected to a Wikipedia page.

#### Redirection to Wikipedia pages

If the server considers that the visitor’s traffic does not match that generated by targeted victims, the phishing kit redirects the visitor to a Microsoft-related Wikipedia page using the href[.]li redirection service.

This service is likely used to remove HTTP headers data, therefore attempting to anonymise the redirection to the Wikipedia pages.

`https://href.li/?https://en.wikipedia.org/wiki/Category:Office_365  
https://href.li/?https://en.wikipedia.org/wiki/Client_access_license  
https://href.li/?https://en.wikipedia.org/wiki/Email  
https://href.li/?https://en.wikipedia.org/wiki/Email_client  
https://href.li/?https://en.wikipedia.org/wiki/Internet_Explorer_11  
https://href.li/?https://en.wikipedia.org/wiki/List_of_Microsoft_365_Applications  
https://href.li/?https://en.wikipedia.org/wiki/Microsoft_365  
https://href.li/?https://en.wikipedia.org/wiki/Microsoft_Exchange_Server  
https://href.li/?https://en.wikipedia.org/wiki/Microsoft_Office_Mix  
https://href.li/?https://en.wikipedia.org/wiki/Windows_Server_2016  
https://href.li/?https://en.wikipedia.org/wiki/Windows_Server_2019  
https://href.li/?https://id.wikipedia.org/wiki/Berkas:Logo_Microsoft_Office_365_(2013-2019).svg  
`

### Authentication with Microsoft API

Once the victim has passed the checks, the phishing server redirects them to the fake Microsoft authentication page.

#### Background images

The Sneaky 2FA phishing kit employs several blurred images as the background for its fake Microsoft authentication pages. By using screenshots of legitimate Microsoft interfaces, this tactic is intended to deceive users into authenticating themselves to gain access to the blurred content.

![Background blurred images used by Sneaky 2FA](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57ba54c8f443fa4ddc1_6a92a21616f788fda8e46ba1_6a2a7ecde2d8f7e583cbb408.webp)

Figure 2. Background blurred images used by Sneaky 2FA

#### Communications

##### Victim side

To detail the Sneaky 2FA communications, the following is the steps for an authentication using the Microsoft Authenticator application as a two-factor authentication (2FA) method.

****| **Step**| **HTTP method**| **URI**| **Parameters**  
---|---|---|---|---  
1| Cloudflare Turnstile check| GET``| /# or `/` |   
2| Email-based redirection*| GET``| /?cf-turnstile-response= |   
3| CAPTCHA check*| GET``| /[a-zA-Z0-9]{150}/index?a= |   
4| Fake Microsoft authentication page| GET``| /[a-zA-Z0-9]{150}/verify |   
5| Login (password)| POST``| /[a-zA-Z0-9]{150}/validate| em=&pa=  
6| 2FA method selection| POST``| /[a-zA-Z0-9]{150}/validate| em=&auth=<2fa_method>  
7| 2FA resolution| POST``| /[a-zA-Z0-9]{150}/validate| em=&auth=<2fa_method>&code=  
  
_* step invisible to victims_ Table 1. Sneaky 2FA’s main steps to authenticate to Microsoft 365 API 

  1. The phishing process generally starts with a webpage embedding a Cloudflare Turnstile challenge, as detailed above. It sends two GET requests: 
     * The first retrieves benign HTML code containing minimal JavaScript code to reload the actual page.
     * The second gets the custom page embedding the Cloudflare Turnstile challenge.
  2. Once the challenge is successfully passed, the phishing URL (`/index`) is constructed, by adding the victim’s email address if present. This step also includes an initial benign HTML code for reloading the page, as well as anti-debugging JavaScript code.
  3. It then simply checks whether the CAPTCHA has been passed and then redirects to the next phishing URL (`/verify`).
  4. This returns the fake Microsoft authentication page containing JavaScript code that handles the authentication steps. The HTML code is obfuscated with the methods mentioned above. When the victim enters the credentials, it processes them and displays the next page.
  5. The victim’s email address and password are sent to the phishing server via an HTTP POST to `/validate`. The server responds to the victim's data, including the available 2FA method(s) for the Microsoft 365 account.
  6. The chosen 2FA method is sent to the phishing server, including `verify_app` for the Microsoft Authenticator, `verify_code` for the one-time password code, and `verify_sms` for SMS. For Microsoft Authenticator, the server returns a code for entry in the Microsoft Authenticator, which is displayed to the victim on the fake Microsoft authentication page.
  7. Finally, the phishing page regularly polls the server to update the status once the authentication is complete.



##### Server side

In Adversary-in-the-Middle phishing attacks, the authentication steps with the legitimate service are executed from the attacker’s side.

In the case of the Sneaky 2FA phishing kit, communications with Microsoft 365 API are handled directly by the phishing server, unlike other AiTM phishing kits that use proxies for these requests.

Sekoia analysts identified that, for the communications with Microsoft API, the Sneaky 2FA’s User-Agent values are inconsistent with an usual authentication attempt. Indeed, the phishing kit uses a different User-Agent for almost every request, as shown by the following table.

HTTP Method| URI| Sneaky 2FA User-Agent| Request type  
---|---|---|---  
POST| /login| Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1| Login:login  
POST| /SAS/BeginAuth| Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36| SAS:BeginAuth  
POST| /SAS/ProcessAuth| Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0| SAS:ProcessAuth  
POST| /SAS/EndAuth| Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0 OS/10.0.22635| SAS:EndAuth  
POST| /kmsi| Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0| Kmsi:kmsi  
  
Table 2. Sneaky 2FA’s User-Agent values to authenticate to Microsoft 365 API 

Like the "impossible travel" technique that consists in detecting malicious authentication attempts based on different locations, we can detect Sneaky 2FA communications based on the User-Agent anomalies, “impossible device shift”, as detailed in section _Detection and tracking opportunities_.

This detection approach is relevant for multiple AiTM PhaaS, such as Dadsec (missing User-Agent), Tycoon 2FA (very rare User-Agent values), W3LL OV6 (inconsistent browser versions among User-Agent values), and others.

#### Final redirection

When the authentication is successful, the victim is redirected to a legitimate Office365 URL, which is `hxxps://outlook.office365[.]com/Encryption/ErrorPage.aspx?src=0&code=10&be=DM8PR09MB6088&fe=1` by default.

## Business and operations of Sneaky Log

The following analysis focuses on the identification of the cybercrime business behind this phishing kit and its operations on Telegram.

### Phishing kit connections

#### Association to the Sneaky Log PhaaS

Analysis of the leaked PHP code showed that the phishing kit relies on a check with a central server, allegedly that of the operator of the service, based on an API key stored in the configuration file `config.php`. This check ensures that the API licence has not expired, and suggests that **this phishing kit would be sold to customers by an operator managing subscription license via API**.

The licence checking URLS found for the two source code are:

  * `hxxps://sneakylog[.]store/api/key`
  * `hxxp://185.125.100[.]81/api/key`



The domain `sneakylog[.]store` was created on 3 September 2024, but was no longer active by December 2024. As of December 2024, the IP address `185.125.100[.]81` hosts an HTTP service named “Sneaky Log”. These elements suggest that **the Phishing-as-a-Service could be either named _Sneaky_ or _Sneaky Log_**. Consequently, we have chosen to name this phishing kit “Sneaky 2FA”.

#### W3LL OV6 variant

Additionally, we found a reference to a W3LL OV6 domain in the code in charge of the authentication with Microsoft API. According to Group-IB4, W3LL OV6 is an Adversary-in-the-Middle phishing kit which was sold by W3LL's BEC-focused criminal enterprise.

![Excerpt of Sneaky 2FA source code authenticating to Microsoft 365 API, including a reference to the W3LL OV6 domain “w3ll\[.\]store”](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57ba54c8f443fa4ddca_6a92a214dc3071123832039e_6a2a7ecce2d8f7e583cbb3e1.webp)

Figure 3. Excerpt of Sneaky 2FA source code authenticating to Microsoft 365 API, including a reference to the W3LL OV6 domain “w3ll[.]store”

This reference suggests that **Sneaky 2FA source code is based on W3LL OV6**.

The monetisation model of W3LL OV6 is similar to that of Sneaky 2FA: customers download an archive of obfuscated code that they deploy on their own infrastructure, and the kit requires a license key that is checked periodically by contacting a central server.

Multiple OV6 code archives uploaded to VirusTotal since 2022 provide insight into the codebase's evolution. These archives contain version strings apparently based on release dates, establishing a development timeline.

The Microsoft authentication relay implementation in Sneaky 2FA shares several identical characteristics with OV6, including:

  * Use of specific User-Agent strings and request parameters in the authentication process
  * Identical usage patterns of the GuzzleHttp library for cookie handling
  * Nearly identical custom cookie parsing function implementations



Timeline analysis narrows down which OV6 version likely served as Sneaky 2FA's foundation:

  * Certain unique strings in Sneaky 2FA, like the UUID `9799cd88-6ea7-4cfc-aeb2-4dcb20034a03` used in Microsoft authentication requests, appear only in OV6 versions predating `OV6-6-20-23` (June 20, 2023)
  * Key implementation features, such as GuzzleHttp library usage and cookie parsing functions, first appear in OV6 versions after `OV6-5-9-23` (May 9, 2023)



This evidence places the source OV6 version between May 9 and June 20, 2023. However, code reuse appears limited to the Microsoft authentication relay component, with no significant similarities found elsewhere in the kit.

Sneaky 2FA also uses PNG image files found in W3LL OV6, specifically the blurred background images for Microsoft services landing pages (Outlook, Excel, OneDrive, SharePoint, Office 365). These images share identical hashes and filenames between the two kits, though they were only incorporated into OV6 around October 2023, several months after the presumed code source version.

### Sneaky Log’s operations on Telegram

#### A fully-featured bot

Sekoia analysts discovered that the Phishing-as-a-Service operates a bot (_@SneakyLog_bot_) advertising and selling phishing tools on Telegram.

![Overview of the Sneaky Log’s Telegram bot, including description, first bot message, menu, and cryptocurrency options](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57ba54c8f443fa4ddcd_6a92a2156017750314a4946f_6a2a7ecde2d8f7e583cbb405.webp)

Figure 4. Overview of the Sneaky Log’s Telegram bot, including description, first bot message, menu, and cryptocurrency options

As of December 2024, the tools sold with this bot include:

  * _365 Cookie Page_ \- the AiTM phishing kit
  *  _B2B Sender_ \- an email sender featured for spam
  *  _Redirect & Attachment_



![Details about the three tools sold by Sneaky Log’s Telegram bot.
Source : Sekoia TDR Team investigation about Sneaky 2FA](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57ba54c8f443fa4ddc4_6a92a218dae089660dfbec7e_6a2a7ecde2d8f7e583cbb410.webp)

Figure 5. Details about the three tools sold by Sneaky Log’s Telegram bot.  
Source : Sekoia TDR Team investigation about Sneaky 2FA  


Our technical analysis is fully aligned with the features advertised by the operator.

Sneaky Log’s AiTM phishing kit is priced at $200 per month, with increasing reductions for longer subscriptions. This price is comparable to competitors such as Tycoon 2FA and Mamba 2FA but is slightly cheaper.

#### Sneaky Log support

In addition to the Sneaky Log’s main bot, the operator employs another bot, named _SneakySupport_Bot_ (_@SneakySupport_bot_), to manage the service support operations. The bot seems to be an interface in front of a ticketing system, as interacting with the bot creates a ticket with a unique identifier, _e.g. #T000365_.

Like many cybercrime services, including Maware-as-a-Service, Crypter-as-a-Service, and Phishing-as-a-Service, **Sneaky Log’s operator abuses the Telegram capabilities** to fully **automate the advertisement and sale of its phishing kit** , as well as **managing the support operations**.

Following the change of Telegram’s privacy policy in September 2024, Sekoia analysts assess that cybercriminals will gradually shift from Telegram to other platforms for operating their illegal activities, in the medium to long term future.

### Cryptocurrency transactions

The Sneaky Log Telegram bot implements a multi-cryptocurrency payment system supporting five digital assets: Bitcoin (BTC), Tether USD on TRON (USDT-TRC20), Ethereum (ETH), Litecoin (LTC), and Tether USD on BNB Chain (USDT-BEP2).

Analysis of the payment system reveals distinct address management strategies. For BTC and LTC payments, the bot assigns a new, unused address for each payment attempt. Blockchain analysis confirms these addresses have no prior transaction history. This pattern of using fresh addresses makes it significantly more difficult to trace payment flows through traditional blockchain analysis techniques.

For USDT-TRC20 and ETH payments, the bot employs a different strategy. While the addresses vary across payment attempts, blockchain analysis reveals substantial historical activity: each address contains between 40 to 100+ transactions, with histories extending back several years. This pattern suggests these addresses are selected from an existing pool of well-established addresses, rather than being generated for each payment.

While USDT-BEP2 remains listed as a payment option in the bot's interface, attempting to select it results in an error message. This aligns with the documented shutdown of the BNB Chain platform in December 2024.

Analysis of the cryptocurrency transactions reveals several patterns suggesting the use of a transaction obfuscation mechanism. When users initiate a payment through the Telegram bot, they are systematically instructed to send an amount 10% higher than their requested credit (for example, a $110 payment for a $100 credit).

For USDT-TRC20 and ETH transactions, blockchain analysis shows that incoming payments to the provided addresses are systematically followed by outgoing transfers. These outbound transfers are approximately 1% smaller than the received amount and are sent to various addresses that maintain their own transaction histories. Based on these patterns, Sekoia analysts hypothesise that Sneaky Log could be leveraging a third-party cryptocurrency laundering service. This would explain both the initial 10% fee and the subsequent 1% reductions as service fees at different stages of the obfuscation process. However, further analysis would be needed to confirm this assessment.

## Detection and tracking opportunities

### Detecting impossible device shift

The Microsoft authentication flow is composed of a sequence of steps (_e.g._ password submission, MFA method selection, MFA submission). For each of these steps, the client performs an HTTP request to the Microsoft authentication API, and an event is created in the Microsoft 365 audit log, with the name of the authentication step (RequestType) and the User-Agent string of the client, among other information. All the events from a same authentication attempt can be grouped using the _correlation ID_ , a unique identifier that is generated each time an authentication flow is started.

As detailed earlier, in the _Characteristics of Sneaky 2FA_ section, the phishing kit uses different hardcoded User-Agent strings for the HTTP requests depending on the step of the authentication flow. This behavior is rare in legitimate user authentication, as a user would have to perform successive steps of the authentication from different web browsers. While User-Agent transitions occasionally happen in legitimate situations (_e.g._ authentications initiated in a desktop applications that launch a web browser or webview to handle MFA), the specific sequence of User-Agents used by Sneaky 2FA does not correspond to a realistic scenario, and offers a high-fidelity detection of the kit.

The following Sigma correlation rule looks for a `Login:login` event with a _Safari on iOS_ User-Agent, and a `Login:resume` event with an _Edge on Windows_ User-Agent, both having the same correlation ID, and happening within 10 minutes.

`rule: Microsoft 365 Sign-In Via Known AiTM Phishing Kit (Sneaky 2FA)  
description: >-  
Detects a sign-in attempt with an impossible device shift characteristic of the adversary-in-the-middle phishing kit Sneaky 2FA.  
correlation: |  
name: login_safari_ios  
detection:  
selection:  
office365.auth.request_type: 'Login:login'  
user_agent.original: 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'  
condition: selection  
---  
name: resume_edge_windows  
detection:  
selection:  
office365.auth.request_type: 'Login:resume'  
user_agent.original: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0 OS/10.0.22635'  
condition: selection  
---  
action: correlation  
type: temporal  
rule:  
- login_safari_ios  
- resume_edge_windows  
group-by:  
- office365.context.correlation.id  
timespan: 10m  
ordered: false  
`

### Unveiling Sneaky 2FA phishing pages

The analysis of Sneaky 2FA phishing pages revealed several characteristic patterns, offering opportunities for tracking them.

As of early January 2025, we were able to unveil **around one hundred Sneaky 2FA domains**. Most of them were allegedly registered by the customers of the Sneaky Log service that conducted the phishing campaign. But some of them are legitimate domains compromised to host Sneaky 2FA phishing pages. The full list of IoCs collected is available in the _IoCs & Technical details_ section.

Interestingly, some Sneaky 2FA domains were previously associated with known AiTM phishing kits, such as evilginx2 and Greatness, according to our Sekoia C2 trackers. We suspect that some cybercriminals have recently shifted from well-established PhaaS platforms to the new Sneaky Log PhaaS by reusing existing domain names.

Threat actors are likely to migrate to new Phishing-as-a-Service (PhaaS) platforms like Sneaky Log when they offer improved detection evasion, enhanced services, or more competitive pricing.

## Conclusion

First identified by Sekoia in the wild in December 2024, Sneaky 2FA is an **emerging Adversary-in-The-Middle phishing kit distributed through the Phishing-as-a-Service model**. It mainly aims to **harvest Microsoft 365 session cookies to bypass the MFA process** during subsequent authentication.

Our investigation uncovered that this emerging phishing kit is **sold, advertised and operated on Telegram by the Sneaky Log Phishing-as-a-Service**. As of December 2024, Sneaky 2FA has seen moderate adoption by threat actors, as evidenced by approximately one hundred domain names hosting Sneaky 2FA phishing pages and some ongoing campaigns distributing them.

The cybercriminal ecosystem associated with AiTM phishing and Business Email Compromise (BEC) attacks is continuously evolving, with threat actors opportunistically migrating from one PhaaS platform to another, supposedly based on the quality of the phishing service and the competitive price.

To provide our customers with actionable intelligence and built-in detection rules, Sekoia will continue to actively monitor the Sneaky 2FA threat as well as other emerging AiTM phishing kits.

## Annex

### Annex 1 - Initial email phishing campaign distributing Sneaky 2FA using QR code

On 10 December 2024, during our daily threat hunting routine, we discovered the Sneaky 2FA phishing pages while analysing an email phishing attachment titled `Final Lien Waiver.pdf`, which contains a QR code. This QR code redirects the user to:

  1. An open redirection step:  
`hxxps://b.leadbi[.]com/l/44e234ab-9118-47ed-a1a1-ca66f913c271.html?next=hxxps://highnationservices[.]com/n/#victim[@]example[.]com`
  2. The Sneaky 2FA phishing page:  
`hxxps://highnationservices[.]com/n/#victim[@]example[.]com`



![Malicious QR code attachment redirecting to Sneaky 2FA phishing page](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57ba54c8f443fa4ddc7_6a92a217dc30711238320554_6a2a7ecde2d8f7e583cbb40b.webp)

Figure 6. Malicious QR code attachment redirecting to Sneaky 2FA phishing page

## IoCs & Technical details

### Sneaky 2FA’s phishing pages

 _The indicators listed below are available in CSV format with additional metadata in_[ _the SEKOIA-IO/Community GitHub repository_](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/sneaky2fa/sneaky2fa_iocs_20250116.csv) _._

Attacker-controlled domains:

africanagrirnarket[.]com  
alliedhealthcaresolution[.]com  
allorganicitems[.]com  
allorginichomes[.]xyz  
apppowerappsportals[.]top  
baptihealth[.]com  
bhlergroup[.]com  
claytoncontsruction[.]net  
desirenetwork[.]in  
docuinshare[.]top  
dolh6growth[.]online  
drop-project[.]top  
emailsay[.]com  
emea-nec[.]com  
erhakalip[.]com  
files42[.]com  
florenceorganics[.]us  
glamorouslengths[.]su  
greyscaleal[.]com  
guardiansresearch[.]org  
hsrcxeeae[.]mypi[.]co  
intertrustsgroup[.]com  
lovencareurology[.]in  
matcocomponent[.]com  
may-april[.]com  
metin2odisey[.]com  
ms-consulting-dom[.]fr  
o7t5dgbx-staging[.]dreamwp[.]com  
oempcworlds[.]org  
ohconnects[.]org  
ol[.]advanceplastics-ke[.]com  
omnirayoprah[.]cfd  
organichoicehome[.]com  
outsourcel[.]com[.]au  
portalpowerfiles[.]top  
portalpowerstorages[.]top  
profitminers[.]in  
reintergestna[.]org  
reliant-rehabs[.]com  
rockandrevenue[.]com  
rurrasqueamos[.]click  
stillmanconsulting[.]net  
storageorder[.]sbs  
sysarchirnc[.]com  
thumenectrics[.]es  
tvsyndciate[.]com  
urbanumbrella[.]org  
usfightingsystems[.]com  
webitww[.]com  
welcomehomeproject[.]org  
windstreaim[.]com  
wwgle[.]com  
yushengusa[.]com docsafybeifur2mabbggrihscauthenticnotes[.]online  
historischeverenigingmarum[.]online  
loginoffice365commonauth00000365user1153196333[.]empreendendocomgrafica[.]com  
loginoffice365commonauth00000365user6867620079[.]empreendendocomgrafica[.]com 

Possibly compromised domains:

allorganichome[.]com  
auxin[.]co[.]in aweitapp[.]com  
carpetcleaningmanitoba[.]ca  
cchosting[.]co[.]za  
cnphys[.]com  
coysem[.]com  
drgoelsdmd[.]com  
eto1908[.]org  
forcainvicta[.]com[.]br  
funnelflex[.]co  
globalservicesqtr[.]com  
iziloyer[.]com  
kagumigroup[.]id  
leanstartupatelier[.]co  
meliorahospital[.]com  
mscserv[.]com  
mysilverfox[.]com[.]my  
nashnights[.]com  
pipaltree[.]ngo  
powa[.]co[.]zw  
printserve[.]co[.]ke  
senangwasap[.]com  
snatched-beautybar[.]com  
sukrajclasses[.]com  
thewoodlandretreat[.]in  
unalkardesler[.]net  
vlsbali[.]com  
wordtex[.]com  
www[.]fabribat[.]com  
www[.]northernaid[.]org  
yaharaho[.]com  
yogatrapezepoint[.]com  
yugaljeeautomotive[.]com  


### Sneaky 2FA’s operator servers

`101.99.92[.]124  
185.125.100[.]81  
sneakylog[.]store  
tesla-apply-job[.]com  
`