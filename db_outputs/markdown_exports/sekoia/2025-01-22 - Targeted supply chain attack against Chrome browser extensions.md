# Targeted supply chain attack against Chrome browser extensions

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/targeted-supply-chain-attack-against-chrome-browser-extensions
- **Date :** 2025-01-22

---

## Context

On 26 December 2024, the data security company Cyberhaven informed its users about a compromise of their Chrome browser extension. The **attacker exploited the extension developer's permissions** , which had been previously **gained through a targeted phishing attack, to upload a malicious version of Cyberhaven to the Chrome Web Store**.

Investigations into the adversary’s infrastructure revealed that during December 2024, the threat actor **compromised a dozen Chrome extensions, potentially affecting hundreds of thousands of end users**. The malicious code injected into these **compromised extensions aimed to harvest sensitive data from users’ web browsers**. The targeted data include API keys, session cookies, and other authentication tokens from websites such as **ChatGPT and Facebook for Business**.

After reporting this supply chain attack to the developers of the compromised extensions, Sekoia analysts were able to retrieve the initial phishing emails. This enabled us to **understand the entire attack and uncover an infrastructure used by the attacker** since at least 2023, and possibly even earlier.

This blog post provides an overview of the supply chain attack, detailing the targeted phishing attacks and the malicious code added to the compromised extensions. Additionally, it shares insights into the adversary’s infrastructure, as well as recommendations for remediation and Indicator of Compromise (IoCs).

_This blog post was originally sent to our clients on 10 January 2025._

## Supply chain attack overview

The following analysis focuses on the two parts of the uncovered supply chain campaign:

  * The spearphishing emails targeting Chrome extension developers, successfully compromising dozens of them since mid-November 2024.


  * The compromise of approximately a dozen Chrome extensions since early December 2024, allegedly infecting hundreds of thousands of extensions’ users.



Sekoia analysts assess with high confidence that during 2023 and 2024, the threat actor conducted additional campaigns targeting Chrome extensions, using similar techniques, along with additional ones. The section below provides an analysis of the most recent campaign, which was active until 30 December 2024.

### Targeted phishing attacks against the extension developers

To gain the necessary permissions to publish new versions of legitimate extensions on the Chrome Web Store, the threat actor sent phishing emails to the developers, attempting to persuade them to authorise access to a malicious OAuth Google application.

![Phishing email about a fake violation related to the Chrome extension.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57919d5c5953769bc46_6a92a210fd507e2a51b97e79_6a2a7edbb97c48a61ea62055.webp)

Phishing email about a fake violation related to the Chrome extension.

_Figure 1.Phishing email claiming a fake violation related to a Chrome extension, targeted at the extension developers (source: Sekoia)_

The phishing emails had the following characteristics:

  * **Email subjects** : 
    * _Action Request: <EXTENSION NAME> requires the use of a developer account to accept the Chrome Web Store policy_
    *  _Action Required: <EXTENSION NAME> Requires Changes to Comply with Chrome Web Store Policy_


  * **Sender email addresses** : 
    * _chromewebstore-noreply[@]chromeforextension[.]com_
    *  _chromewebstore-noreply[@]supportchromestore[.]com_


  * **Display name** : 
    * _Webstore Extension_



Of note, it is highly likely that the attacker gathered the developers’ email addresses from the extension pages on the Chrome Web Store, as this information is publicly available.

Clicking on the “ _Go To Policy_ ” button redirects to the adversary’s infrastructure, for example:

  * _hxxps://app.checkpolicy[.]site/extension-privacy-policy?e=victime[@]example[.]com_
  *  _hxxps://app.checkpolicy[.]site/accept-terms-policy?e=victim[@]example[.]com_



These URLs redirect to a legitimate Google Accounts webpage, where victims are asked to allow the malicious OAuth application access to their Google account.

![Malicious OAuth application “Privacy Policy Extension” requesting access to update the Chrome Web Store extensions \(Source: Cyberhaven\).](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57919d5c5953769bc3d_6a92a21232517fc4025f7194_6a2a7edbb97c48a61ea62070.webp)

Malicious OAuth application “Privacy Policy Extension” requesting access to update the Chrome Web Store extensions (Source: Cyberhaven).

_Figure 2. Malicious OAuth application “Privacy Policy Extension” requesting access to update the Chrome Web Store extensions (source: Cyberhaven)_

Once the application, named “Privacy Policy Extensions”, was granted access, the threat actor was able to deploy a new version of the extension that contained malicious code. As shown in the figure above, the OAuth application requires permissions to “ _see, edit, update, or publish_ ” the Chrome Web Store extensions, enabling the attacker to hijack them.

### Compromised extensions

By misusing the OAuth application, the attacker successfully gained access and compromised a dozen Chrome extensions in the supply chain attack of December 2024. Sekoia analysts identified the compromised extensions during this campaign primarily by analysing their source code, associating them with the adversary’s domain names, and using information shared by the cybersecurity researcher John Tuckner:

**Chrome extension**| **Identifier**| **Compromise date**| **C2 domains**  
---|---|---|---  
Proxy SwitchyOmega (V3)| hihblcmlaaademjlakdpicchbjnnnkbo| 30/12/2024| proxyswitchyomega[.]pro  
GraphQL Network Inspector| ndlbedplllcgconngcnfmkadhokfaaln| 29/12/2024| graphqlnetwork[.]pro  
YesCaptcha assistant| jiofmdifioeejeilfkpegipdjiopiekl| 29/12/2024| yescaptcha[.]pro  
Castorus| mnhffkhmpnefgklngfmlndmkimimbphc| 26/12/2024| castorus[.]info  
Uvoice| oaikpkmjciadfpddlpjjdapglcihgdle| 26/12/2024| uvoice[.]live  
VidHelper – Video Download Helper| egmennebgadmncfjafcemlecimkepcle| 26/12/2024| videodownloadhelper[.]pro  
ParrotTalks| kkodiihpgodmdankclfibbiphjkfdenh| 25/12/2024| parrottalks[.]info  
Bookmark Favicon Changer| acmfnomgphggonodopogfbmkneepfgnh| 25/12/2024| bookmarkfc[.]info  
Internxt VPN| dpggmcodlahmljkhlmpgpdcffdaoccni| 25/12/2024| internxtvpn[.]pro  
Vidnoz Flex| cplhlgabfijoiabgkigdafklbhhdkahj| 25/12/2024| vidnozflex[.]live  
Cyberhaven| pajkjnmeojmbapicmbpliphjmcekeaac| 24/12/2024| cyberhavenext[.]pro  
Wayin AI| cedgndijpacnfbdggppddacngjfdkaca| 19/12/2024| wayinai[.]live  
Reader Mode| llimhhconnjiflfimocjggfjdlmlhblm| 18/12/2024| readermodeext[.]info  
Primus (prev. PADO)| oeiomhmbaapihbilkfkhmlajkeegnjhe| 18/12/2024| primusext[.]pro  
TinaMind| befflofjcniongenjmbkgkoljhgliihe| 15/12/2024| tinamind[.]info  
VPNCity| nnpnnpemnckcfdebeekibpiijlicmpom| 12/12/2024| vpncity[.]live  
  
Other Chrome extensions may have been compromised during this supply chain campaign, being linked to the following domains registered by the threat actor. However, as of early January 2025, we cannot confirm this hypothesis, as the extensions that appeared to be associated with these domains are either no longer available on the Chrome Web Store or their latest versions do not include malicious code.

**C2 domains**| **Creation date**  
---|---  
dearflip[.]pro| 25/12/2024  
iobit[.]pro| 25/12/2024  
ultrablock[.]pro| 25/12/2024  
yujaverity[.]info| 24/12/2024  
censortracker[.]pro| 23/12/2024  
wakelet[.]ink| 20/12/2024  
pieadblock[.]pro| 13/12/2024  
locallyext[.]ink| 13/12/2024  
moonsift[.]store| 06/12/2024  
  
### Extensions’ malicious code

The following analysis is based on the compromised version 2.22.6 of the GraphQL Network Inspector extension, which includes two new malicious JavaScript files located at the root of the extension code:

  * **_background.js_** (SHA256: _b0827dc54349b10098a7370ada4ea44ba668b264ccca2db5676be1c32e6cc154_ , available on GitHub Gist at <https://gist.github.com/qbourgue/4e42ac21ed5898fd75221a2f1164a107>): This script operates in the background, as specified in the _background_ field of the manifest JSON file.


  * **_context_responder.js_**(SHA256: _d303047205dabec8e2d34431e920ebe3478ca80a18f57bf454da094aca0e10aa_ , available on GitHub Gist at <https://gist.github.com/qbourgue/b4690045862e6c21fb180dd6dcb6b6b3>): This script is injected at the beginning of each page, before any other script is run, for every URLs, as specified in the _content_scripts_ section using the document_start by the manifest.



#### Background script

The background script, a key component of a Chrome extension, serves as the main event handler for the extension. It listens for incoming messages and executes various operations based on the specified action property.

The action types include:

  * _graphqlnetwork-completions_ : This action sends a POST request to _hxxps://chatgpt[.]com/status/_ with an HTTP header containing an API key. It then processes the response accordingly.


  * _graphqlnetwork-redirect_ : This action fetches a URL and processes the response. It is possibly used to retrieve a redirection URL.


  * _graphqlnetwork-validate_ : This action sends a POST request to the URL and processes the response. It is used to send data to a URL and possibly check the validity of a token.


  * _graphqlnetwork-rtext_ and _graphqlnetwork-rjson_ : These actions fetch a URL to retrieve text or JSON, and process the response. They are used to retrieve and process data further. 


  *  _graphqlnetwork-check-errors_ : This action modifies HTTP headers of a POST request, constructs a base64-encoded payload with input data, and sends a POST request. It is very likely to exfiltrate data to the C2 server.



Furthermore, the background script attempts to fetch a configuration file from the C2 server at _hxxps://graphqlnetwork[.]pro/ai-graphqlnetwork_ , storing it in browser local storage under the key _graphqlnetwork_ext_manage_.

This configuration includes URLs intended for harvesting credentials. On 27 December 2024, all tested C2 domains returned a configuration file specifically targeting ChatGPT.

Here is an example for GraphQL Network Inspector extension:

`{  
"code": 2000,  
"graphqlnetworka": "https://chatgpt.com/api/*",  
"graphqlnetworkb": "https://chatgpt.com/public-api/conversation_limit",  
"graphqlnetworkc": "http://chatgpt.com",  
"graphqlnetworkd": "sk-<OpenAI API Key>",  
"graphqlnetworke": "backend-api/me",  
"graphqlnetworkf": "https://chatgpt.com",  
"graphqlnetworkg": "https://chatgpt.com/backend-api/compliance",  
"graphqlnetworkh": "https://chatgpt.com/api/auth/session",  
"graphqlnetworki": "auth",  
"graphqlnetworkk": "https://chatgpt.com"  
}  
`

Based on the listed endpoints and patterns, along with the implemented actions, we assess with high confidence that this JSON configuration is used to **target OpenAI API keys** , **user authentication data** from the URIs _/api/auth/session_ and _/backend-api/me_ (including user email, phone number, and access token), and **service usage data** from the URI _/public-api/conversation_limit_.

In their incident response report, Cyberhaven shared another configuration file targeting Facebook Business users. This configuration is designed to harvest sensitive data from Facebook Business accounts, which are used for managing advertisements on the Meta platform. The targeted data types include Facebook API keys, emails, passwords, session cookies, User-Agent values, and additional user data. These compromised accounts could be exploited to distribute malicious content using Facebook Ads, such as websites that spread malware or engage in various fraudulent schemes.

#### Inject script

According to the manifest JSON file, the _context_responder.js_ script is injected into all URLs before any script is run.

`{  
"all_frames": false,  
"js": [ "context_responder.js" ],  
"matches": [ "hxxp://*/*", "hxxps://*/*" ],  
"run_at": "document_start"  
}  
`

This script primarily attempts to read the configuration file stored in Chrome's local storage under _graphqlnetwork_ext_manage_.

If the configuration file is successfully retrieved and matches the code _2000_ , and if the current URL meets the pattern specified in the configuration file (_e.g.hxxp://chatgpt[.]com_), the script interacts with the background script to execute various actions, including setting up an event listener, initiating network requests and collecting targeted data.

If the current URL does not match _hxxp://chatgpt[.]com_ , the JavaScript code calls the background actions _graphqlnetwork-redirect_ and _graphqlnetwork-completions_.

Notably, based on our analysis of these JavaScript codes, the exfiltration URL is expected to be stored in the key _graphqlnetworkb_. However, this key contains the ChatGPT URL _hxxps://chatgpt[.]com/public-api/conversation_limit_. It is likely that this compromised version of the GraphQL Network Inspector extension was unable to correctly exfiltrate the harvested data.

As part of a Chrome extension, the two malicious scripts embedded in the compromised source code primarily aim to fetch a configuration file from a C2 URL, and interact with the browser URLs to harvest credentials and user data when it meets the configuration.

Most of the malicious code is designed separately from the targeted service, since patterns are retrieved from a configuration file from the adversary’s infrastructure. We assume that this code flexibility may allow the attacker to target data from multiple services in different extensions or versions. As of early January 2025, only configurations targeting ChatGPT and Facebook Business were publicly identified.

## Adversary’s infrastructure

![Overview of the supply chain attack targeting Chrome browser extensions and the adversary's infrastructure.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57919d5c5953769bc40_6a92a211a2f46752fd00d385_6a2a7edbb97c48a61ea6206a.webp)

Overview of the supply chain attack targeting Chrome browser extensions and the adversary's infrastructure.

_Figure 3. Overview of the supply chain attack and the adversary’s infrastructure_

### Phishing domains for initial access

#### SMTP servers

The domain names used to send the initial phishing emails to Chrome extension developers are _chromeforextension[.]com_ and _supportchromestore[.]com_. These domains share several characteristics:

  * Registration with Namecheap
  * Mail exchanger (MX) record set to Google (_smtp.google[.]com_)
  * MX domain's TTL record to 1799
  * No DNS A record



By searching for domain names that meet these criteria and include the words “ _chrome_ ” or “ _extension_ ”, we discovered another domain: _chromewebstore-noreply[.]com_. We assess with high confidence that this domain also belongs to the attacker’s infrastructure and was possibly used in the initial phishing campaign as part of this supply chain attack.

chromewebstore-noreply[.]com,2024-12-25  
chromeforextension[.]com,2024-12-12  
supportchromestore[.]com,2024-12-04  
---  
  
The domain _extensionbuysell[.]com_ meets all these criteria except the DNS A record. We believe that the threat actor registered this domain name and used it in a previous campaign or for testing purposes.

#### Redirection infrastructure

The initial phishing emails retrieved from the extension developers redirect to the domain _app.checkpolicy[.]site_ , which is hosted at _136.244.115[.]219_ (AS 20473, VULTR).

Using passive DNS resolutions on this IP address, we discovered other domains employing similar naming patterns that were highly likely leveraged in the initial phishing campaign. All of them have the subdomain “ _app._ ” resolving _136.244.115[.]219_.

extensionpolicyprivacy[.]com,2024-12-21  
policyextension[.]info,2024-12-11  
extensionpolicy[.]net,2024-11-29  
checkpolicy[.]site,2024-11-20  
136.244.115[.]219,2024-03-14  
---  
  
Since March 2024, _extensionbuysell[.]com_ and other possible attacker-controlled domains have resolved to this IP address. We assess with high confidence that they have been used in other campaigns involving web browser extensions conducted by the same threat actor.

### Command & Control infrastructure

#### Configuration file hosting

All domain names used as C2 server for hosting the configuration file were hosted at _149.28.124[.]84_ or _45.76.225[.]148_(AS 20473, VULTR). By using passive DNS resolutions on these IP addresses, we were able to discover possibly all the domains used in this supply chain attack. Based on their name, we could deduce which Chrome extensions were compromised by this threat actor.

graphqlnetwork[.]pro,2024-12-28  
yescaptcha[.]pro,2024-12-27  
videodownloadhelper[.]pro,2024-12-27  
bookmarkfc[.]info,2024-12-26  
castorus[.]info,2024-12-26  
proxyswitchyomega[.]pro,2024-12-26  
uvoice[.]live,2024-12-25  
iobit[.]pro,2024-12-25  
primusext[.]pro,2024-12-25  
dearflip[.]pro,2024-12-25  
ultrablock[.]pro,2024-12-25  
cyberhavenext[.]pro,2024-12-25| parrottalks[.]info,2024-12-24  
internxtvpn[.]pro,2024-12-24  
yujaverity[.]info,2024-12-24  
censortracker[.]pro,2024-12-23  
vidnozflex[.]live,2024-12-22  
wakelet[.]ink,2024-12-20  
pieadblock[.]pro,2024-12-13  
vpncity[.]live,2024-12-12  
tinamind[.]info,2024-12-12  
locallyext[.]ink,2024-12-12  
wayinai[.]live,2024-12-11  
moonsift[.]store,2024-12-06  
readermodeext[.]info,2024-12-05  
---|---  
  
To identify additional possible C2 servers, we listed the services and their characteristics hosted on the two servers:

  * SSH on port 22
  * HTTP on port 80, with the default Nginx 404 response
  * HTTPS on port 443, with the JARM _1dd40d40d00040d00042d43d000000e1ea2a807a629b496b664cf07ad7c08d_
  * REDIS on port 6379.



Using these criteria and filtering on the autonomous system (AS) 20473, we wrote a heuristic on Censys to find **C2 servers used by the same attacker in previous campaigns** :

45.76.225[.]148,2024-12-06 (December campaign, configuration)  
137.220.48[.]214,2024-07-21  
149.248.44[.]88,2024-05-29  
149.28.124[.]84,2024-05-11 (December campaign, configuration)  
140.82.45[.]42,2024-04-03  
136.244.115[.]219,2024-03-14 (December campaign, redirection webpage)  
155.138.253[.]165,2024-03-09  
108.61.23[.]192,2024-03-06  
149.248.2[.]160,2024-02-07 (December campaign, exfiltration)  
---  
  
Passive DNS on these IP addresses returns multiple domain names, most of them are themed around Ads blockers and AI. This confirms that the previous IP addresses are associated with our threat actor.

#### Exfiltration

Malicious code in the compromised extension exfiltrates the collected data to a subdomain “ _app._ ” of the C2 domain. The “ _app._ ” fully qualified domain names (FQDNs) are all hosted at _149.248.2[.]160_.

Notably, this IP address meets our previous characteristics but includes an additional MySQL service on port 3306. We assess with high confidence that **this C2 server hosts a MySQL database to store the large volume of data harvested during this supply chain attack**.

### Attacker’s domain names

For this supply chain attack and the previous campaigns, the threat actor registered a significant number of domain names. The use of the same registrar, consistent DNS setups and TLS configurations across the infrastructure made it straightforward for us to identify these domains.

Most of the domains share the following characteristics:

  * Registrar: Namecheap
  * Top-level domains: co, com, info, ink, io, live, net, pro, site 
  * Hosting provider: AS 20473 (VULTR)
  * JARM fingerprint: _1dd40d40d00040d00042d43d000000e1ea2a807a629b496b664cf07ad7c08d_
  * DNS A record TTL: 1799



By searching for domains meeting these criteria, we identified the following domains, which we associate with high confidence to the threat actor’s infrastructure. Some of these domains had already been identified during the analysis of the December 2024 supply chain attack, while others were likely used in earlier campaigns:

linewizeconnect[.]com,2024-10-14  
savgptforchrome[.]pro,2024-10-08  
gptdetector[.]live,2024-08-02  
bardaiforchrome[.]live,2024-07-29  
searchcopilot[.]co,2024-07-17  
chatgptextent[.]pro,2024-07-16  
youtubeadsblocker[.]live,2024-06-20  
geminiaigg[.]pro,2024-06-16  
chataiassistant[.]pro,2024-05-29  
aiforgemini[.]com,2024-05-26  
chatgptextension[.]site,2024-05-21  
blockforads[.]com,2024-05-10  
ytbadblocker[.]com,2024-04-22  
geminiforads[.]com,2024-04-10  
savegptforyou[.]live,2024-04-03| searchgptchat[.]info,2024-03-28  
savechatgpt[.]site,2024-03-20  
adskiper[.]net,2024-03-14  
savegptforchrome[.]com,2024-03-13  
chatgptforsearch[.]com,2024-03-09  
searchaiassitant[.]info,2024-03-03  
goodenhancerblocker[.]site,2024-02-19  
internetdownloadmanager[.]pro,2024-02-01  
openaigptforgg[.]site,2024-01-16  
adsblockforyoutube[.]site,2024-01-10  
promptheusgpt[.]info,2023-12-27  
gpt4chrome[.]live,2023-12-22  
savegpt[.]pro,2023-12-16  
gptforads[.]info,2023-12-13  
gptforbusiness[.]site,2023-12-11  
---|---  
  
Among the domain names used in former campaigns, we identified a **cluster of fake websites that redirected users to download extensions from the Chrome Web Store**. As of December 2024, these extensions have been removed from the store, possibly flagged as malicious by Google.

![Attacker websites impersonating AI and Ads Block solutions](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57919d5c5953769bc43_6a92a2132b0ef7af46bc6d9f_6a2a7edbb97c48a61ea62074.webp)

Attacker websites impersonating AI and Ads Block solutions

 _Figure 4. Attacker websites impersonating AI and Ads Block solutions_

The domain naming convention and their creation dates indicate that the attacker’s campaigns have been active since at least December 2023. It is possible that the websites redirecting to allegedly malicious Chrome extensions were promoted through SEO-poisoning or malvertising.

Sekoia analysts believe that this **threat actor has specialised in spreading malicious Chrome extensions to harvest sensitive data**. At the end of November 2024, the attacker shifted his modus operandi from distributing his own malicious Chrome extensions via fake websites to compromising legitimate Chrome extensions by phishing emails, malicious OAuth applications, and malicious code injected into compromised Chrome extensions.

## Conclusion

This supply chain attack, which targeted a dozen Chrome browser extensions, **potentially affected hundreds of thousands of end users with minimal effort or sophistication**. Although targeting credentials via browser extensions is relatively rare, this campaign is notable for the large number of potential victims. As a reminder, the supply chain attacks and the compromise of web browser extensions could represent major threats to organisations.

In this attack, the threat actor **conducted a targeted email phishing against the extension developers** using a malicious OAuth application to gain permissions on their extension. The objective of the campaign was to harvest credentials and user data from at least two services, ChatGPT and Facebook for Business.

By analysing the adversary's infrastructure, we discovered that this **threat actor is persistent in distributing malicious Chrome extensions** since at least 2023. We assess with high confidence that this supply chain attack is a shift from its former modus operandi that consisted in distributing fake websites to redirect users to download malicious Chrome extensions.

Harvested data from ChatGPT or Facebook Business users can be sold or used by the threat actor itself in further campaigns. Indeed, we believe that the stolen API keys can be abused by illegitimate services. As for users' personal data, it could be used in other cyber attacks.

To provide our customers with actionable intelligence, Sekoia will continue to actively monitor the threat actor’s infrastructure as well as other supply chain attacks on Chrome browser extensions.

## Remediation

If a user’s browser is or was infected with a compromised Chrome extension, the following measures should be taken:

  * **Investigation** : to determine whether user data and credentials were harvested  

    * Check if the configuration was successfully fetched by searching for a file named _*_ext_manage_ in Chrome’s local storage or by checking for communications with the configuration file C2 server (_149.28.124[.]84_ or _45.76.225[.]148_).
    * Check if there was any communication with the exfiltration C2 server (_149.248.2[.]160_).


  * **Mitigation** :  

    * Update the Chrome extension to a clean version or remove it entirely.
    * Revoke any potentially compromised credentials, such as API keys and authentication tokens.
    * Revoke session cookies and change the password for the potentially compromised accounts.
    * Monitor activity on any accounts that may have been compromised.
    * Enhance awareness of phishing attempts that may exploit the harvested data targeting affected users.



## IoCs & Technical details

 _The indicators listed below are available in CSV format in_[ _the SEKOIA-IO/Community GitHub repository_](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/compromised_chrome_extensions_dec24/compromised_chrome_extensions_iocs_20250122.csv) _._

**Phishing domains** :

chromewebstore-noreply[.]com,2024-12-25  
chromeforextension[.]com,2024-12-12  
supportchromestore[.]com,2024-12-04  
---  
  
**Redirection pages** :

extensionpolicyprivacy[.]com,2024-12-21  
policyextension[.]info,2024-12-11  
extensionpolicy[.]net,2024-11-29  
checkpolicy[.]site,2024-11-20  
136.244.115[.]219,2024-03-14  
---  
  
**Compromised extensions and C2 domains** :

**Chrome extension**| **Identifier**| **Compromise date**| **C2 domains**  
---|---|---|---  
Proxy SwitchyOmega (V3)| hihblcmlaaademjlakdpicchbjnnnkbo| 30/12/2024| proxyswitchyomega[.]pro  
GraphQL Network Inspector| ndlbedplllcgconngcnfmkadhokfaaln| 29/12/2024| graphqlnetwork[.]pro  
YesCaptcha assistant| jiofmdifioeejeilfkpegipdjiopiekl| 29/12/2024| yescaptcha[.]pro  
Castorus| mnhffkhmpnefgklngfmlndmkimimbphc| 26/12/2024| castorus[.]info  
Uvoice| oaikpkmjciadfpddlpjjdapglcihgdle| 26/12/2024| uvoice[.]live  
VidHelper – Video Download Helper| egmennebgadmncfjafcemlecimkepcle| 26/12/2024| videodownloadhelper[.]pro  
ParrotTalks| kkodiihpgodmdankclfibbiphjkfdenh| 25/12/2024| parrottalks[.]info  
Bookmark Favicon Changer| acmfnomgphggonodopogfbmkneepfgnh| 25/12/2024| bookmarkfc[.]info  
Internxt VPN| dpggmcodlahmljkhlmpgpdcffdaoccni| 25/12/2024| internxtvpn[.]pro  
Vidnoz Flex| cplhlgabfijoiabgkigdafklbhhdkahj| 25/12/2024| vidnozflex[.]live  
Cyberhaven| pajkjnmeojmbapicmbpliphjmcekeaac| 24/12/2024| cyberhavenext[.]pro  
Wayin AI| cedgndijpacnfbdggppddacngjfdkaca| 19/12/2024| wayinai[.]live  
Reader Mode| llimhhconnjiflfimocjggfjdlmlhblm| 18/12/2024| readermodeext[.]info  
Primus (prev. PADO)| oeiomhmbaapihbilkfkhmlajkeegnjhe| 18/12/2024| primusext[.]pro  
TinaMind| befflofjcniongenjmbkgkoljhgliihe| 15/12/2024| tinamind[.]info  
VPNCity| nnpnnpemnckcfdebeekibpiijlicmpom| 12/12/2024| vpncity[.]live  
  
**Additional C2 domains** :

**C2 domains**| **Creation date**  
---|---  
dearflip[.]pro| 25/12/2024  
iobit[.]pro| 25/12/2024  
ultrablock[.]pro| 25/12/2024  
yujaverity[.]info| 24/12/2024  
censortracker[.]pro| 23/12/2024  
wakelet[.]ink| 20/12/2024  
pieadblock[.]pro| 13/12/2024  
locallyext[.]ink| 13/12/2024  
moonsift[.]store| 06/12/2024  
  
**Attacker’s C2 servers** :

45.76.225[.]148,2024-12-06 (December campaign, configuration)  
137.220.48[.]214,2024-07-21  
149.248.44[.]88,2024-05-29  
149.28.124[.]84,2024-05-11 (December campaign, configuration)  
140.82.45[.]42,2024-04-03  
136.244.115[.]219,2024-03-14 (December campaign, redirection webpage)  
155.138.253[.]165,2024-03-09  
108.61.23[.]192,2024-03-06  
149.248.2[.]160,2024-02-07 (December campaign, exfiltration)  
---  
  
140.82.50[.]201,2024-02-19  
45.77.5[.]196,2024-03-27  
149.28.117[.]236,2024-02-01  
65.20.99[.]178,2024-01-16  
45.77.185[.]211,2024-01-12  
149.248.56[.]63,2023-12-29  
185.92.222[.]127,2023-12-27  
136.244.113[.]231,2023-11-24  
144.202.101[.]155,2023-11-03  
---  
  
**Attacker’s domains** :

linewizeconnect[.]com,2024-10-14  
savgptforchrome[.]pro,2024-10-08  
gptdetector[.]live,2024-08-02  
bardaiforchrome[.]live,2024-07-29  
searchcopilot[.]co,2024-07-17  
chatgptextent[.]pro,2024-07-16  
youtubeadsblocker[.]live,2024-06-20  
geminiaigg[.]pro,2024-06-16  
chataiassistant[.]pro,2024-05-29  
aiforgemini[.]com,2024-05-26  
chatgptextension[.]site,2024-05-21  
blockforads[.]com,2024-05-10  
ytbadblocker[.]com,2024-04-22  
geminiforads[.]com,2024-04-10  
savegptforyou[.]live,2024-04-03| searchgptchat[.]info,2024-03-28  
savechatgpt[.]site,2024-03-20  
adskiper[.]net,2024-03-14  
savegptforchrome[.]com,2024-03-13  
chatgptforsearch[.]com,2024-03-09  
searchaiassitant[.]info,2024-03-03  
goodenhancerblocker[.]site,2024-02-19  
internetdownloadmanager[.]pro,2024-02-01  
openaigptforgg[.]site,2024-01-16  
adsblockforyoutube[.]site,2024-01-10  
promptheusgpt[.]info,2023-12-27  
gpt4chrome[.]live,2023-12-22  
savegpt[.]pro,2023-12-16  
gptforads[.]info,2023-12-13  
gptforbusiness[.]site,2023-12-11  
---|---  
  
## MITRE ATT&CK

Tactic| Technique  
---|---  
Reconnaissance| T1589.002 – Gather Victim Identity Information: Email Addresses  
Resource Development| T1583.001 – Acquire Infrastructure: Domains  
Resource Development| T1583.004 – Acquire Infrastructure: Server  
Resource Development| T1586.003 – Compromise Accounts: Cloud Accounts  
Resource Development| T1587 – Develop Capabilities  
Initial Access| T0862 – Supply Chain Compromise  
Initial Access| T1566.002 – Phishing: Spearphishing Link  
Execution| T1059.007 – Command and Scripting Interpreter: JavaScript  
Lateral Movement| T1550.001 – Use Alternate Authentication Material: Application Access Token  
Credential Access| T1528 – Steal Application Access Token  
Credential Access| T1539 – Steal Web Session Cookie  
Defense Evasion| T1036 – Masquerading  
Command and Control| T1071.001 – Application Layer Protocol: Web Protocols  
Command and Control| T1105 – Ingress Tool Transfer  
Exfiltration| T1041 – Exfiltration Over C2 Channel  
  
## External references

  * [[Cybergaven] Cyberhaven’s preliminary analysis of the recent malicious Chrome extension](https://www.cyberhaven.com/engineering-blog/cyberhavens-preliminary-analysis-of-the-recent-malicious-chrome-extension)
  * [[John Tuckner] Google Sheets spreadsheet containing compromised extensions, by John Tuckner from Secure Annex](https://docs.google.com/spreadsheets/d/15xOLbYgz5DQnCWYE6a_LXGcqYC_bNPPzdBqdLofz6-E/)
  * [[Gist] _background.js_ script from the Chrome extension "GraphQL Network Inspector" (_ndlbedplllcgconngcnfmkadhokfaaln_) compromised on 29 December 2024 (code beautified and URL defanged)](https://gist.github.com/qbourgue/4e42ac21ed5898fd75221a2f1164a107)
  * [[Gist] _context_responder.js_ script from the Chrome extension "GraphQL Network Inspector" (_ndlbedplllcgconngcnfmkadhokfaaln_) compromised on 29 December 2024 (code beautified and URL defanged)](https://gist.github.com/qbourgue/b4690045862e6c21fb180dd6dcb6b6b3)



Thank you for reading this blog post. Please don’t hesitate to provide your feedback on our publications. You can contact us at tdr[at]sekoia.io for further discussions, always good to have feedbacks from peers.