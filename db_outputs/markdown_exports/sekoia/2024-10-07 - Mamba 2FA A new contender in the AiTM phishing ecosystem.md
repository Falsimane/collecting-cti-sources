# Mamba 2FA: A new contender in the AiTM phishing ecosystem

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/mamba-2fa-a-new-contender-in-the-aitm-phishing-ecosystem
- **Date :** 2024-10-07

---

## Introduction

In late May 2024, Sekoia’s Threat Detection & Research (TDR) team received an insight from a partner about an ongoing phishing campaign leveraging HTML attachments that mimicked [Microsoft 365](/blog/userauthenticationmethod-microsoft-365-decode) login pages. The phishing pages were able to relay some methods of multi-factor authentication (MFA), and made use of the Socket.IO JavaScript library to communicate via websockets with a backend server. At first, these characteristics look like [the _Tycoon 2FA_ phishing-as-a-service platform](/blog/tycoon-2fa-an-in-depth-analysis-of-the-latest-version-of-the-aitm-phishing-kit), but further inspection found that the campaign leveraged **a previously unknown adversary-in-the-middle (AiTM) phishing kit** , that Sekoia track as **_Mamba 2FA_**.

TDR illuminated the infrastructure hosting the phishing pages and developed detection rules to identify Entra ID accounts compromised via this kit. Retro-hunting uncovered that several Sekoia XDR customers have been targeted by campaigns leveraging _Mamba 2FA_ in the previous months, suggesting a **widespread threat**. Finally, during this investigation we identified that the kit was **sold as**[**phishing-as-a-service**](/blog/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1)**(PhaaS)**.

On 26 June 2024, [ANY.RUN published an analysis of a phishing campaign](https://any.run/cybersecurity-blog/analysis-of-the-phishing-campaign/) that matched the characteristics and infrastructure of _Mamba 2FA_. Since then, and likely in reaction to this publication, the phishing kit and associated infrastructure have undergone several significant changes.

## Characteristics of _Mamba 2FA_ phishing pages

### URL structure and domain names

As of October 2024, the URLs of _Mamba 2FA_ phishing pages have the following structure:

`https://{domain}/{m,n,o}/?{Base64 string}`

For example:

`https://tubope[.]com/n/?c3Y9bzM2NV8xX25vbSZyYW5kPVZFUnhiR1k9JnVpZD1VU0VSMjUwOTIwMjRVMDgwOTI1NTk=`

The phishing page is displayed only if a valid Base64 parameter is present. If the parameter is absent or invalid, the page is blank.

However, the phishing kit also tries to detect automated web browsers and security sandboxes. In this case, the visitor is redirected to `https://google.com/404/`.

### Base64-encoded parameter

Once decoded, the Base64 parameter follows the structure of a URL query string, with 3 field-value pairs. For example:

`sv=o365_1_nom&rand=VERxbGY=&uid=USER25092024U08092559`

  * `sv` controls the appearance of the phishing page
  * `rand` is a Base64-encoded pseudo-random string, whose function is unknown
  * `uid` is presumed to be a unique identifier for each customer of the PhaaS platform



#### Targeted email address

The email address targeted by the phishing attempt can be added at the end of the URL, separated from the Base64 parameter by the string `N0123N`, or by a `#` (URL fragment). If present, this address will be automatically pre-filled in the login form. This email address is optionally Base64-encoded. The four examples below are equivalent:

`https://tubope[.]com/n/?c3Y9bz...TI1NTk=N0123Nsatyan@microsoft.com  
https://tubope[.]com/n/?c3Y9bz...TI1NTk=N0123Nc2F0eWFuQG1pY3Jvc29mdC5jb20=  
https://tubope[.]com/n/?c3Y9bz...TI1NTk=#satyan@microsoft.com  
https://tubope[.]com/n/?c3Y9bz...TI1NTk=#c2F0eWFuQG1pY3Jvc29mdC5jb20=  
`

#### Appearance of the phishing pages

The appearance of the phishing page can be one of four types, depending on the `sv` parameter:

  * `sv=o365_#_one` imitates OneDrive
  * `sv=o365_#_nom` is a generic Microsoft sign-in page
  * `sv=o365_#_sp` mimics a SharePoint Online secure link
  * `sv=o365_#_voice` purports to be a voice mail, then displays a generic Microsoft sign-in page after a click



(where `#` is a number, usually `1` in recent weeks, whose function is unknown)

![Mamba 2FA OneDrive phishing page](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a599dc3071123833df0f_6a92a257dae089660dfc0b4d_6a2a7e40e02555536e6a0a83.webp)

Mamba 2FA OneDrive phishing page

![Mamba 2FA SharePoint Online phishing page](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a599dc3071123833df09_6a92a2586c2fbffe9c24fb8e_6a2a7e40e02555536e6a0a86.webp)

Mamba 2FA SharePoint Online phishing page

![Mamba 2FA generic Microsoft 365 phishing page](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a599dc3071123833df06_6a92a259e9a71d42283fc7bc_6a2a7e40e02555536e6a0a8a.webp)

Mamba 2FA generic Microsoft 365 phishing page

![Mamba 2FA voice mail phishing page](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a599dc3071123833df12_6a92a2556929191488994e6e_6a2a7e40e02555536e6a0a7d.webp)

Mamba 2FA voice mail phishing page

Screen captures of the four known phishing page variants of _Mamba 2FA_. 

## Capabilities of the Mamba 2FA phishing platform

The _Mamba 2FA_ phishing platform features similar capabilities to the other popular AiTM phishing-as-a-service offerings of the cybercrime ecosystem:

  * It handles two-step verifications for non-phishing-resistant MFA methods such as one-time codes and app notifications;
  * It supports Entra ID, AD FS, third-party SSO providers, and consumer Microsoft accounts;
  * For enterprise accounts, it dynamically reflects the organisation’s custom login page branding (logo, background image);
  * The stolen credentials and cookies are instantly sent to the attacker via a Telegram bot;
  * The kit attempts to block visits to the page by security scanning services.



## Commercialisation of Mamba 2FA phishing pages

The _Mamba 2FA_ phishing pages are sold on Telegram on a subscription model. At the price of $250 for 30 days, customers are given access to a Telegram bot that allows them to generate phishing links and HTML attachments on demand.

The operator of the service maintains the infrastructure that hosts the phishing pages. The servers and domain names are not attributed to a specific customer but rather used as a shared pool for several or all customers.

_Mamba 2FA_ has been advertised on Telegram since at least March 2024. However, according to data from public URL and file analysis sandboxes, the kit has been used in phishing campaigns since November 2023. The operator of the service had a long-standing presence on ICQ until this messaging platform shut down in June 2024, and this may be where _Mamba 2FA_ was primarily sold before shifting to Telegram.

## HTML attachments

Since its inception, the _Mamba 2FA_ service featured the ability for customers to generate HTML files meant to be distributed as email attachments in phishing campaigns, or hosted on object storage services such as Cloudflare R2 or IPFS.

The content of these HTML files has significantly evolved over time, as the service’s developer tries to evade defensive controls. As of October 2024, these files are often filled with benign content, surrounding a small snippet of JavaScript code that redirects to the actual phishing page. The content is made invisible via CSS, causing the document to appear blank until the redirection happens. The filler content used changes frequently and is usually taken from seemingly random websites. The URL of the phishing page is Base64-encoded in the script.

`<body style="display:none;">  
// benign filler content  
<script>  
window.location.href = atob("aHR0cHM6Ly...") + "#" + "[EMail]";  
</script>  
// benign filler content  
</body>  
` Structure of a typical _Mamba 2FA_ HTML attachment as of October 2024. 

## Mamba 2FA Architecture

As of October 2024, the _Mamba 2FA_ infrastructure consists of two layers: the _link domains_ and the _relay servers_.

![Architecture of the Mamba 2FA phishing kit. Source : Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a599dc3071123833df0c_6a92a256bf29df41da0f59d1_6a2a7e40e02555536e6a0a80.webp)

Architecture of the Mamba 2FA phishing kit. Source : Sekoia TDR Team

Architecture of the _Mamba 2FA_ phishing kit. 

### Link domains

The link domains are used in the phishing page URLs described earlier in this article. The main role of these domains is to perform “antibot” detection. If the visitor is identified as a potential security solution or automated activity, they are redirected to a benign page (`https://google.com/404/`). However, if not identified as a bot, the servers would display a minimal HTML document, which looks like this:

`<!DOCTYPE html>  
<html id='html' sti='VlZORl...' vic='{target email}' lang='en'>  
  
<head>  
<script src='https://cdn.socket.io/4.7.5/socket.io.min.js'></script>  
</head>  
  
<body id='allbody'>  
  
</body>  
  
<script src='{template script}'></script>  
</html>  
  
` Structure of the HTML document returned by link domains, as of October 2024. 

The `sti` attribute of the `<html>` tag contains the _Mamba 2FA_ customer’s unique identifier (`USER…`), Base64-encoded twice. The `vic` attribute contains the target email address, if it was specified, optionally Base64-encoded.

The page doesn’t have any content (`<body>` is empty). Instead, it loads two JavaScript files: the Socket.IO library and a _template script_.

#### Template scripts

The _template script_ that is included in the page controls the appearance of the phishing page. As described earlier, _Mamba 2FA_ currently offers four page templates. As of October 2024, the names of the scripts are:

  * `jsdrive.js`: OneDrive template (`sv=o365_#_one`)
  * `jsnom.js`: generic Microsoft sign-in page (`sv=o365_#_nom`)
  * `jssp.js`: SharePoint template (`sv=o365_#_sp`)
  * `jsv.js`: voice mail template (`sv=o365_#_voice`)



Once loaded, the template script injects into the page the HTML content required to render the phishing page. This script also contains the domain name of a _relay server_. Using the Socket.IO library, the template script establishes a bidirectional connection to the relay server.

Socket.IO is a JavaScript library that makes it easy for developers to establish bidirectional network communications between a web browser and a server. In modern browsers, this connection is established over WebSockets. If this protocol is not available the library falls back to HTTP long-polling.

From this point onward, every action performed by the visitor on the page (_e.g._ submitting an email address or a password) is communicated to the relay server. The relay server sends back commands that update the phishing page's appearance (_e.g._ display an error message or an MFA challenge).

### Socket.IO protocol

The template script of the phishing page can send three commands (_events_) to the relay server:

event| parameters  
---|---  
`new-session`| `uid`: Mamba 2FA customer unique identifier  
`email`: victim’s email address  
`ua`: web browser User Agent  
`timeZone`: web browser timezone  
`browserLanguage`: web browser language  
`password_command`| `password`: user’s password  
`otp_command`| `phish_otp`: user’s MFA input  
  
The relay server sends commands to update the phishing page in response to the user’s actions:

event| signification  
---|---  
`s2c`| general page updates  
`s2c_cookies`| cookies captured, redirect to `endUrl`  
`s2c_restart`| timeout or error, reload page  
  
The `s2c` event has a large list of parameters that are used at different stages of the phishing session:

  * `phish_state`: tracks the current stage of the phishing session. Values include `RQ_EMAIL`, `RQ_PASSWORD`, `RQ_OTP_NOPASS_APP`, `RQ_OTP_APP`, `RQ_OTP_APP_CODE`, `RQ_OTP_PHONE`.
  * `email_type`: values include ADFS and O365
  * `bannerLogo`, `backgroundImage`, `boilerText`: organisation’s custom login page branding
  * `email_exist`, `CORRECT_PASSWORD`, `OTP_TYPE`, `CORRECT_OTP`
  * `endUrl`: URL where the victim is redirected once the cookies have been captured
  * `phish_id` and `phish_groupid`: internal parameters, unknown function



### Relay servers

The relay servers host the core adversary-in-the-middle functionality of _Mamba 2FA_. Using the credentials received from the phishing page via Socket.IO, they perform requests to the Microsoft authentication servers to sign in as the victim.

### Domain names lifetime

The link domains, being used in the URLs of the phishing pages, are easily visible to the victims and get usually reported and blocked by security solutions after a few days of use. For this reason, the operator of _Mamba 2FA_ maintains around a dozen link domains at any time and replaces them about every week.

On the other hand, the domain names used for the relay servers are less exposed, and it is common for them to last several weeks.

### Proxy servers

Until late September 2024, the relay servers were connecting directly to the Entra ID servers when performing authentications with victim's credentials. As a result, the IP addresses of the relay servers were exposed in the authentication logs of the targeted tenants. However, starting October 2024, the developers of _Mamba 2FA_ implemented an additional indirection layer, utilising proxy servers sourced from a commercial provider (IPRoyal). In consequence, the IP addresses appearing in authentication logs since October 2024 are those of the datacenter proxies, not the relay servers. (These proxy servers are not pictured on the architecture schema above).

## Mamba 2FA Indicators of compromise

 _If you are a SOC or CERT, we can share additional detection opportunities with you under TLP:GREEN. Please contact tdr [ at ] sekoia [ dot ] io._

### Relay server IP addresses

Since October 2024, Entra/M365 sign-ins from IP addresses of IPRoyal proxies used by _Mamba 2FA_ (non-exhaustive list):

`23.26.35[.]67  
23.26.206[.]99  
45.86.54[.]206  
45.9.153[.]102  
`

Between August and October 2024, Entra/M365 sign-ins from IP addresses of _Mamba 2FA_ relay servers:

`2607:5500:3000:1cab::2 (since 2024-08-28)  
2607:5500:3000:7bc::2 (since 2024-09-10)  
2607:5500:3000:312::2 (since 2024-09-24)  
2607:5500:3000:7a5::2 (2024-09-20 – 2024-09-26)  
2607:5500:3000:a8c::2 (2024-09-06 – 2024-09-22)  
2607:5500:3000:fea::2 (2024-07-03 – 2024-09-07)  
2607:5500:3000:b16::2 (2024-07-03 – 2024-08-30)  
`

The following IP addresses were used previously, between November 2023 and July 2024 (non-exhaustive list):

45.61.130[.]11 45.61.169[.]4 172.86.64[.]212 172.86.96[.]84 172.86.96[.]128 172.86.97[.]78 172.86.97[.]165 172.86.104[.]33 172.86.104[.]64 172.86.104[.]178 172.86.105[.]59 172.86.105[.]72 172.86.106[.]94 

### Relay server domain names

Outgoing connection to domains of _Mamba 2FA_ relay servers:

`drensyoons1sedt[.]com (since 2024-10-07)  
sandoom2notnt[.]com (since 2024-10-07)  
grastoonm3vides[.]com (since 2024-10-07)  
ccokies1cakes[.]com (2024-09-23 – 2024-10-08)  
ccokies2mangoes[.]com (2024-09-23 – 2024-10-08)  
ccokies3tomatoes[.]com (2024-09-23 – 2024-10-08)  
m1tis-apicookies[.]com (since 2024-08-12)  
m2fes-apicookies[.]com (since 2024-08-12)  
m3mas-apicookies[.]com (since 2024-09-10)  
winss0conect[.]click (2024-07-22 – 2024-08-12)  
winstnet80nss[.]cfd (2024-07-22 – 2024-08-12)  
tenetur[.]top (2024-06-26 – 2024-07-22)  
tenetur[.]xyz (2024-06-26 – 2024-07-22)  
`

The following domains were used previously, between November 2023 and July 2024:

hypexfinancial[.]com voltampereactive[.]com planchereserver[.]com thirdmandomavis[.]com fourthmanservice[.]com sithchibb[.]com copelustration[.]xyz copefood[.]xyz seven-oranges[.]com onemanforest[.]com twomancake[.]com threemanshop[.]com fourmanchurch[.]com fivemanchool[.]com sixmanteams[.]com sevenmanjungle[.]com 88mansession[.]com fiveradio-newbam[.]com nine9manforest[.]com 10decadesmen[.]com 11cyclesforest[.]com 1messisnfarm[.]com 2moniunesson[.]com 3alphabetjay[.]com 4sessionmoon[.]com 5poleanalhy[.]com 6treesmangle[.]com 7motionmansa[.]com 8boomandool[.]com 9cantronnfit[.]com 10trioneyue8ss[.]com 11beamgools[.]com