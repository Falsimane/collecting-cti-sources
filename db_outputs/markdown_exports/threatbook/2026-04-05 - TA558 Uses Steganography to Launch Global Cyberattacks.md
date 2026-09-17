# TA558 Uses Steganography to Launch Global Cyberattacks

- **Source :** threatbook
- **URL :** https://threatbook.io/blog/ta558-uses-steganography-to-launch-global-cyberattacks
- **Date :** 2026-04-05

---

5 min read 

# TA558 Uses Steganography to Launch Global Cyberattacks

[ ![Picture of ThreatBook Research Team](https://threatbook.io/hubfs/Brand%20Resources/favicon-192x192.png) ThreatBook Research Team ](https://threatbook.io/blog/author/threatbook-research-team) :  Updated on April 14, 2026 

[Threat Research](https://threatbook.io/blog/tag/threat-research)

**Table of Contents**

Overview

Threat Actor Analysis

Threat Actor Profile

Attack Methods

Initial Intrusion: Highly Disguised Phishing Emails

Payload Hosting: Image Steganography on Legitimate Websites

Final Payload: Publicly Available Trojan Families

Sample Analysis

Sample 1

Sample 2

IOCs

C2 IP Addresses

C2 Domains

Hashes

## Overview

TA558 (also known as "SteganoAmor") is a financially motivated cybercriminal organization that has been active since 2018. Its attacks are centered on Latin America and have spread to North America, Western Europe, Russia, and numerous other regions worldwide. Initially focused on the hospitality and tourism sectors, the group has since expanded its targeting to include finance, government, energy, education, and other critical industries.

  * The group's primary attack vector is highly disguised phishing emails, crafted with carefully designed lure content to trick victims into opening attachments. These attachments follow two attack paths: on one hand, Office documents carrying malicious macros or exploit code for silent initial compromise; on the other, compressed archives containing malicious scripts that prompt victims to manually extract and trigger the infection.

  * During the payload execution phase, the group innovatively employs steganography techniques to deeply conceal malicious code within images disguised as MSI installer files. This campaign lasted over five months, involved more than 1,400 malicious image storage URLs, and leveraged legitimate cloud storage services — including public image/video platforms and public data websites — as payload distribution channels, significantly reducing detection probability by security products.

  * After a successful compromise, the group deploys mature remote access trojans and information stealers such as AgentTesla and XWorm on victim endpoints, enabling comprehensive theft of sensitive system data including keystrokes, browser credentials, and FTP accounts, while establishing remote control channels to continuously monitor and operate the compromised devices.

  * ThreatBook Research Team conducted source tracing analysis of related samples, IPs, and domains and extracted multiple relevant IOCs for threat intelligence detection. ThreatBook TDP, TIP, Threat Intelligence Cloud API, Cloud Sandbox S, OneSandbox, OneDNS, OneSIG, and OneSEC all support detection and protection against this attack campaign.




## Threat Actor Analysis

### Threat Actor Profile

**Platform** | Windows  
---|---  
**Attack Targets** | Highly concentrated in Latin America, with broad reach across North America, Western Europe, Russia, and other global regions. Initially targeted the hospitality, tourism, and related industries; current attack scope has expanded to finance, government, energy, education, IT, pharmaceuticals, transportation, and more.  
**Threat Actor** | "Broad net" global attacker, suspected to have ties to the Latin American region  
**Attack Objective** | The group's core motivation is financial crime. By deploying remote access trojans (RATs), spyware, and information stealers, they aim to steal sensitive data (such as credit card information, user credentials, and keystroke logs), gain remote control over victim systems, and ultimately cause financial losses.  
  
### Attack Methods

TA558 is highly adept at combining social engineering with technical exploits to breach defenses. The group shows a clear pattern of "evolving in response to defensive environments," with a core attack methodology of highly specialized spear-phishing combined with multi-layered steganography and commercial remote access trojans.

#### Initial Intrusion: Highly Disguised Phishing Emails

TA558 attacks almost always begin with a carefully crafted phishing email. Subject lines typically include terms such as "reservation," "booking confirmation," "invoice," or "tax notice." To increase credibility, emails are primarily written in Portuguese and Spanish (targeting the Latin American region), but English is also used for global attacks. To bypass spam filters, the group leverages compromised legitimate SMTP servers to send emails, making them appear to originate from trusted, legitimate domains.

**MD5** | **Screenshot**  
---|---  
9013d44684344d09d98b4491fbe653e3 | ![Phishing email sample 1](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-001.png)  
83d5d99d4140546e45a837d8c566e7b7 | ![Phishing email sample 2](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-002.png)  
178bb5c829814e1a0eb5b10622eb755b | ![Phishing email sample 3](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-003.png)  
736b076c24262b319eba990001b1392a | ![Phishing email sample 4](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-004.png)  
92c529984b5c9fe07a75774371ddeecc | ![Phishing email sample 5](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-005.png)  
30cca0257bc7e3d24a3b91594e2fe029 | ![Phishing email sample 6](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-006.png)  
  
Malicious files typically take the form of compressed archives or spreadsheet documents. Compressed archives contain Windows scripts in various formats including JS, PowerShell, HTA, VBE, VBA, and BAT.

**Document Filenames** | **Scripts Inside Archives**  
---|---  
EUR_20260820103321.xls E26MAE7F2TU61410 .xls DHL Receipt_57216218402.xls BL613863421.xls WRONG INVOICE.xlam Purchase Order.xls Purchase Order and company details.xls |  Purchase Order-PO567990.vbs Reservation Order List.js Payment Referenced Invoice.vbe Or der_Request_16-02-2026.pdf.vbs Invoice-pandingpayme ntrequrstpayment-298323921234.js Contract_09023192.hta Agreement Number CEMC-01-26-0354.hta  
  
#### Payload Hosting: Image Steganography on Legitimate Websites

The most distinctive characteristic of TA558's recent attack campaigns (such as the operation codenamed "SteganoAmor") is the concealment of malicious PowerShell code or payloads within seemingly innocuous JPG images. After a malicious script runs, it extracts the image file and uses a specific algorithm to extract the hidden malicious code embedded within the image — code that is typically executed after Base64 decoding. The group is currently using MSI images to conceal code.

![Steganography overview diagram](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-007.png)

By hunting for images used by this group, ThreatBook Research Team found that the group began using this technique heavily in early December 2025 and has continued through April 2026, and remains active to this day. The group will continue to use this method for payload hosting in the future.

![Timeline of steganographic image usage](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-008.png)

Analysis of the payload hosting sites reveals that TA558 hosts malicious software payloads on reputable cloud storage services such as Google Drive. In this particular campaign, the group primarily used the archive.org data platform and the Cloudinary video platform.

![Payload hosting distribution by platform](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-009.png)

#### Final Payload: Publicly Available Trojan Families

Once an attack succeeds, TA558 deploys multiple types of malware on victim machines — including AsyncRAT, LodaRAT, RevengeRAT, XWorm, and AgentTesla — for remote computer control and information theft. The two samples analyzed below use AgentTesla and XWorm respectively for command-and-control communication.

## Sample Analysis

### Sample 1

Sample details are shown in the table below:

**SHA256** | 46a5898ae6c4343598af3bc69a5c7b29f5fb24fb75eaaa7699d2d9d3a61743d8  
---|---  
**SHA1** | a67d92fda293ebbe222ca363dc819fc97ab70c23  
**MD5** | 9013d44684344d09d98b4491fbe653e3  
**File Type** | EML email  
**File Size** | 400.24 KB  
**Filename** | __ DRAFT BILL OF LADING 613863421_ MSDS_LSUHPG25111289SZ.eml  
**Description** | EML delivers a malicious XLS file; the XLS exploits CVE-2017-0199 to download an HTA script, which then downloads a steganographic image, decrypts and memory-executes a loader, and the loader ultimately executes the AgentTesla family for email-based C2 communication.  
**First Seen** | 2026-02-17  
  
The email uses the deceptive filename "__ DRAFT BILL OF LADING 613863421_ MSDS_LSUHPG25111289SZ.eml" — in Chinese, this translates to "Draft Bill of Lading (No. 613863421) and Material Safety Data Sheet (MSDS, No. LSUHPG25111289SZ)" — designed to lure victims by simulating legitimate logistics and chemical industry documents.

![Sample 1 phishing email view](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-010.png)

The XLS file in the email attachment exploits CVE-2017-0199. Once opened in an affected version of Office, the vulnerability is triggered and the document automatically downloads and executes malicious content from a remote link.

![XLS file exploit analysis](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-011.png)

Unpacking and analyzing the XLS file reveals that an embedded OLE object contains a malicious link pointing to "http://0022053061234/...php". Upon resolution, this URL uses a decimal-encoded IP address that actually points to server 144.172.98.156. The attacker uses this encoding obfuscation technique to evade static signature detection and blacklist blocking by security gateways.

![OLE object URL analysis](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-012.png)

The downloaded file is a JavaScript script. After deobfuscation (shown in the figure on the right), its core logic is designed to invoke and execute a Base64-encoded PowerShell command.

![JavaScript deobfuscation](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-013.png)

The initially decoded PowerShell script still contains some obfuscated code. After deep deobfuscation analysis (shown below), its core logic is: download a specified file from "ia600603.us.archive.org/13/items/msi-pro-with-b-64_202602/MSI_PRO_with_b64.png," extract hidden data between the "BaseStart-" and "-BaseEnd" markers, decode via Base64, and execute with a string array as parameters.

![PowerShell deobfuscation analysis](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-014.png)

The decrypted file is a DLL library compiled in C# and protected with the Eazfuscator obfuscator to evade static analysis.

![DLL analysis showing Eazfuscator obfuscation](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-015.png)

The sample's core functions include: environment detection, UAC bypass, establishing persistence, and downloading and executing the final malicious payload from a URL passed in as a parameter.

![Loader core functionality analysis](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-016.png)

The malicious payload download source points to "https://144.172.98.156/web/covertilojjdufhhf.txt." While this link is currently inactive, ThreatBook Research Team proactively captured and successfully decrypted the related payload (MD5: ba5b84d759be847d16c0b6728fcc40e3). In-depth analysis confirmed it belongs to the AgentTesla malware family.

![AgentTesla payload identification](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-017.png)

After completing information theft, the malicious payload uses built-in SMTP credentials to exfiltrate data via email. The sender address, authorization password, and recipient address are shown below:

![AgentTesla SMTP exfiltration credentials](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-018.png)

### Sample 2

Sample details are shown in the table below:

**SHA256** | 57bd03d1dd4544de6cbfa6219dbc250ba195876caca7c07d4e2f115288c2d556  
---|---  
**SHA1** | 1756e4fb9340085cc026df3ebb2e7b57fbce60e0  
**MD5** | 736b076c24262b319eba990001b1392a  
**File Type** | EML email  
**File Size** | 70.50 KB  
**Filename** | RV_ Final Quotation Request- AHPR91 Our Ref BR 4837.msg  
**Description** | EML delivers a malicious compressed file containing a JS script, which then downloads a steganographic image, decrypts and memory-executes a loader, and the loader ultimately executes the XWorm family for C&C communication.  
**First Seen** | 2026-02-16  
  
The malicious email uses the highly deceptive filename "RV_Final Quotation Request-AHPR91 Our Ref BR 4837.msg" (meaning "Final Quotation Request - AHPR91 Our Reference No. BR 4837"). The email body is disguised as a business confirmation letter inquiring whether the attachment contains the final quotation, to lure victims into opening the attachment.

![Sample 2 phishing email view](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-019.png)

The compressed archive in the email attachment contains a JavaScript file with extensive obfuscated code. After deobfuscation analysis, the script's core logic is to copy itself to the Downloads directory, then decode specific strings and invoke PowerShell to execute the final command.

![JavaScript deobfuscation for Sample 2](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-020.png)

The PowerShell command's primary purpose is to download a file from the URL "bafybeibfoyi7ruuyoncarf4xr55qa3lthsjjjgrktk4ia4z3upesawb4ry.ipfs.w3s.link/optimized_MSI.png," which is disguised as an MSI image.

![PowerShell downloading IPFS-hosted MSI image](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-021.png)

The script extracts data located between the "BaseStart-" and "-BaseEnd" markers within the PNG file, decodes it via Base64, and executes it with a string array as parameters.

![Base64 extraction from PNG file](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-022.png)

The decrypted and executed sample — like Sample 1 — functions as a loader, designed to download the file at "bafybeiabfircpl4sbrunr3obevliyfeayzhivpasfokaj4xpivedq2w4ni.ipfs.w3s.link/ConvertedFile.txt," decrypt it, and execute it.

![Loader downloading ConvertedFile.txt](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-023.png)

The loader decrypts a PE file using a reversal + Base64 method.

![PE file decryption via reversal and Base64](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-024.png)

The PE file is an unencrypted XWorm trojan, version 6.0, with the C2 address hustleathem.duckdns.org:1111.

![XWorm v6.0 C2 configuration](https://threatbook.io/hubfs/Blog%20Images/ta558-uses-steganography-to-launch-global-cyberattacks/article-img-025.png)

## IOCs

### C2 IP Addresses

  * [144.172.100.220](https://i.threatbook.io/ip/144.172.100.220)
  * [104.168.5.54](https://i.threatbook.io/ip/104.168.5.54)
  * [198.23.177.203](https://i.threatbook.io/ip/198.23.177.203)
  * [107.172.135.4](https://i.threatbook.io/ip/107.172.135.4)
  * [198.12.83.76](https://i.threatbook.io/ip/198.12.83.76)
  * [83.172.138.151](https://i.threatbook.io/ip/83.172.138.151)
  * [172.245.155.116](https://i.threatbook.io/ip/172.245.155.116)
  * [193.142.58.41](https://i.threatbook.io/ip/193.142.58.41)
  * [107.174.33.21](https://i.threatbook.io/ip/107.174.33.21)



### C2 Domains

  * [hostphpwindowsapps.ydns.eu](https://i.threatbook.io/domain/hostphpwindowsapps.ydns.eu)
  * [hostphpwindowsappsconect.ydns.eu](https://i.threatbook.io/domain/hostphpwindowsappsconect.ydns.eu)
  * [msimasidownload.duckdns.org](https://i.threatbook.io/domain/msimasidownload.duckdns.org)
  * [wormteste.shop](https://i.threatbook.io/domain/wormteste.shop)
  * [apicrypter.store](https://i.threatbook.io/domain/apicrypter.store)
  * [uniworldrivercruises-co.uk](https://i.threatbook.io/domain/uniworldrivercruises-co.uk)



### Hashes

  * 1baca1251cec1782a586a84af929763ec1909ffb3866dc1f515ace4493816a30
  * 46a5898ae6c4343598af3bc69a5c7b29f5fb24fb75eaaa7699d2d9d3a61743d8
  * 07fcc4d56aece8e87d9cdddb44cd5b15308b4d18142fd30b06c6520f5ef0288e
  * 0f1eb4c6a961e1c87313a268ebdab8edf11e3ae77d7f0cf635394786724c1f4e
  * 1827141cdd047966034b857bc31c94e1f30d0adc552a91acbcd5069a0dbf5155
  * 57bd03d1dd4544de6cbfa6219dbc250ba195876caca7c07d4e2f115288c2d556
  * 2b14bc3ff87f77468ee948ad24c3c4591f3060231931db72d883143c393afa23
  * 9819ae0ed7af0bdca615b8d581212c0f7235ba5bff5a599e471424a7816f2e0e
  * 6740808845e4b2eb87f638b921bd401be94c1640609ead6d1a6a7cae44123f2d



  * [Tweet](https://twitter.com/share)
  * Share
  * 


[ ![Phishing With Google Ads and Fake AI Docs: A Criminal Campaign Targeting the AI Ecosystem](https://threatbook.io/hubfs/Phishing%20With%20Google%20Ads%20and%20Fake%20AI%20Docs%20A%20Criminal%20Campaign%20Targeting%20the%20AI%20Ecosystem.jpeg) ](https://threatbook.io/blog/phishing-with-google-ads-and-fake-ai-docs-a-criminal-campaign-targeting-the-ai-ecosystem)

1 min read 

#### [Phishing With Google Ads and Fake AI Docs: A Criminal Campaign Targeting the AI Ecosystem](https://threatbook.io/blog/phishing-with-google-ads-and-fake-ai-docs-a-criminal-campaign-targeting-the-ai-ecosystem)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 20 March 2026, 08:03 AM

ThreatBook Research and Response Team has identified and tracked an organized threat group conducting a large-scale malware distribution campaign...

[Threat Research](https://threatbook.io/blog/tag/threat-research) [Security Operations](https://threatbook.io/blog/tag/security-operations)

[Read More](https://threatbook.io/blog/phishing-with-google-ads-and-fake-ai-docs-a-criminal-campaign-targeting-the-ai-ecosystem)

[ ![Suspected North Korea-Linked Hackers Conduct Targeted Attack Campaign Against Uzbekistan](https://threatbook.io/hubfs/Blog%20Images/suspected-north-korea-linked-hackers-conduct-targeted-attack-campaign-against-uz/blog-banner-v2.jpg) ](https://threatbook.io/blog/suspected-north-korea-linked-hackers-conduct-targeted-attack-campaign-against-uzbekistan)

3 min read

#### [Suspected North Korea-Linked Hackers Conduct Targeted Attack Campaign Against Uzbekistan](https://threatbook.io/blog/suspected-north-korea-linked-hackers-conduct-targeted-attack-campaign-against-uzbekistan)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 25 November 2025, 12:11 AM

Overview In November 2025, ThreatBook Research Team identified two suspected targeted attack campaigns against targets within Uzbekistan. We...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/suspected-north-korea-linked-hackers-conduct-targeted-attack-campaign-against-uzbekistan)

[ ![APAC's Cyber Threat Landscape: Inside the 2026 Mid-Year Data](https://threatbook.io/hubfs/blog-header-1600x840.png) ](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

1 min read 

#### [APAC's Cyber Threat Landscape: Inside the 2026 Mid-Year Data](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 21 July 2026, 07:07 AM

ThreatBook Labs recorded 15,205 security incidents across Asia-Pacific between June 2025 and June 2026. Read one at a time, they look like an...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data)