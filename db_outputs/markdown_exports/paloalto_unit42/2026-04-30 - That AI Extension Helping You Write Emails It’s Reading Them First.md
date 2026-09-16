# That AI Extension Helping You Write Emails? It’s Reading Them First

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/
- **Date :** 2026-04-30

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# That AI Extension Helping You Write Emails? It’s Reading Them First

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 13 min read 

Related Products

[![Advanced DNS Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced DNS Security](https://unit42.paloaltonetworks.com/product-category/advanced-dns-security/ "Advanced DNS Security")[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Advanced WildFire icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced WildFire](https://unit42.paloaltonetworks.com/product-category/advanced-wildfire/ "Advanced WildFire")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Prisma AIRS icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma AIRS](https://unit42.paloaltonetworks.com/product-category/prisma-airs/ "Prisma AIRS")[![Prisma Browser icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Browser](https://unit42.paloaltonetworks.com/product-category/prisma-browser/ "Prisma Browser")[![Secure Access Service Edge \(SASE\) icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Secure Access Service Edge (SASE)](https://unit42.paloaltonetworks.com/product-category/secure-access-service-edge/ "Secure Access Service Edge \(SASE\)")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Shresta Bellary Seetharam](https://unit42.paloaltonetworks.com/author/shresta-bellary-seetharam/)
    * [Nabeel Mohamed](https://unit42.paloaltonetworks.com/author/nabeel-mohamed/)
    * [Billy Melicher](https://unit42.paloaltonetworks.com/author/billy-melicher/)
    * [Oleksii Starov](https://unit42.paloaltonetworks.com/author/oleksii-starov/)
    * [Qinge Xie](https://unit42.paloaltonetworks.com/author/qinge-xie/)
    * [Fang Liu](https://unit42.paloaltonetworks.com/author/fang-liu/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:April 30, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [AI browser](https://unit42.paloaltonetworks.com/tag/ai-browser/)
    * [Browser extension](https://unit42.paloaltonetworks.com/tag/browser-extension/)
    * [GenAI](https://unit42.paloaltonetworks.com/tag/genai/)
    * [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/)
    * [Malware](https://unit42.paloaltonetworks.com/tag/malware/)
    * [Remote Access Trojan](https://unit42.paloaltonetworks.com/tag/remote-access-trojan/)
    * [Search hijacker](https://unit42.paloaltonetworks.com/tag/search-hijacker/)
    * [Spyware](https://unit42.paloaltonetworks.com/tag/spyware/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=That%20AI%20Extension%20Helping%20You%20Write%20Emails?%20It’s%20Reading%20Them%20First&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fhigh-risk-gen-ai-browser-extensions%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fhigh-risk-gen-ai-browser-extensions%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fhigh-risk-gen-ai-browser-extensions%2F&title=That%20AI%20Extension%20Helping%20You%20Write%20Emails?%20It’s%20Reading%20Them%20First "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fhigh-risk-gen-ai-browser-extensions%2F&text=That%20AI%20Extension%20Helping%20You%20Write%20Emails?%20It’s%20Reading%20Them%20First "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fhigh-risk-gen-ai-browser-extensions%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=That%20AI%20Extension%20Helping%20You%20Write%20Emails?%20It’s%20Reading%20Them%20First%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fhigh-risk-gen-ai-browser-extensions%2F "Share in Mastodon")



## Executive Summary

We found 18 AI browser extensions marketed as productivity tools that are not as they seem. This group includes extensions such as:

  * One that surveils your emails as you compose them
  * Another that intercepts ChatGPT prompts
  * A third that exfiltrates passwords



Leveraging the rise of generative AI (GenAI), these extensions deliver remote access Trojans (RATs), meddler-in-the-middle (MitM) attacks and infostealers that target prompts, user behavior and browser sessions. Attackers blend the following established techniques with AI productivity lures:

  * API interception
  * Passive Document Object Model (DOM) observation
  * Traffic proxying
  * HTTPS response decryption



Multiple samples contained AI-generated code, indicating that threat actors employed large language models (LLMs) to accelerate malware production.

We specifically reported 18 high-risk extensions to Google. Google either removed the extensions or sent a warning to the owners of the extensions to address policy violations.

Organizations and individual users should exercise caution by sourcing extensions only from trusted providers and adhering to the principle of least privilege. Users must scrutinize requested permissions, as granting broad access to browser data can authorize the interception of sensitive credentials and proprietary session information.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering)
  * [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security)
  * [Prisma Browser](https://www.paloaltonetworks.com/sase/prisma-browser)
  * [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire)
  * [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[GenAI](https://unit42.paloaltonetworks.com/tag/genai/), [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/), [Remote Access Trojan](https://unit42.paloaltonetworks.com/tag/remote-access-trojan/)**  
---|---  
  
## Examples of Extensions Disguised as AI Tools

We identified multiple extensions that appeared to be AI tools delivering RATs and MitM campaigns, which we disclosed via timely threat intelligence (TTI) posts. These include:

  * AI-powered summary extensions exfiltrating sensitive data to low-reputation domains (August 2025)
  * Adware campaigns using hidden iframes ([August 2025](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2025-08-18-IOCs-for-Chrome-extensions-leading-to-thank-you-pages-for-unwanted-content.txt))
  * Cursor customization extensions delivering potentially unwanted programs (PUPs) ([August 2025](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2025-08-19-IOCs-for-Chrome-extensions-leading-to-adware-or-PUP.txt))
  * Prompt and search hijackers redirecting queries to attacker-controlled domains ([September 2025](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2025-09-24-IOCs-for-AI-prompt-hijacker-extensions.txt))
  * Most recently, a Model Context Protocol (MCP)-themed RAT targeting AI developers ([February 2026](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-02-11-IOCs-for-RAT-disguinsed-as-AI-based-browser-extension.txt?utm_campaign=tti_maliciousextension))



## Browser Extensions Expand the Client-Side Attack Surface

​Browser extensions operate within the browser's trusted process with user-granted permissions. They can read and modify web content, intercept network requests, access cookies and communicate with external servers. These capabilities are shared with legitimate tools like ad blockers, password managers and developer tools.

Deceptive extensions exploit this privileged position. An extension can override network request APIs before calls leave the page. It can passively monitor DOM changes in targets like Gmail or Notion. It can configure browser proxy settings to route traffic through attacker infrastructure. It can attach the Chrome Debugger Protocol to read decrypted HTTPS response bodies.

GenAI amplifies the risk. When users type prompts into AI services, they routinely share proprietary code, draft communications and strategic plans. An extension positioned between the user and an AI service intercepts sensitive data. This data is far more valuable than the browsing metadata targeted by typical browser malware. Our retrospective analysis of detected high-risk extensions revealed the recurring techniques listed in Table 1.

**Technique** | **Description** | **Technical Characteristics** | **Requires Extension Privilege**  
---|---|---|---  
WebSocket-based C2 channels | Persistent bidirectional communication for command dispatch and session management | Maintains an open connection that automatically reconnects on network interruption. Persists across browser restarts. Uses standard WebSocket protocol over HTTPS. | No. Typical malware can establish WebSocket C2 channels. The extension advantage is appearing as legitimate browser traffic and persistence across browser restarts without process injection.  
Browser API hooking | Intercepting JavaScript API calls before network transmission | Replaces browser's native window.fetch or XMLHttpRequest functions. Operates in a JavaScript context before data is encrypted for transmission. No interception-layer traffic required. | Yes. Content scripts inject code into the page context with API modification privileges. Typical malware would typically require browser process injection.  
[DOM](https://learn.microsoft.com/en-us/dotnet/standard/data/xml/xml-document-object-model-dom)-based exfiltration | Extracting page content through observation rather than network interception | Reads content from the rendered page DOM. The extension generates no network requests for data collection. Operates entirely within the browser process. | Yes. Content scripts have direct read access to the page DOM. Typical malware would require accessibility APIs, screen scraping or browser process memory access.  
Dynamic proxy configuration | Remote proxy auto-configuration (PAC) script updates for selective traffic routing | Downloads and applies proxy configuration from a remote server. Can be updated without extension store approval. Applies routing rules per-domain or per-URL pattern. | Partially. Typical malware can modify system proxy settings but lacks the chrome.proxy API for programmatic, extension-scoped, dynamic updates without OS-level permissions.  
Cross-storage persistence with active restoration | Redundant identifier storage across multiple APIs with automated recreation on deletion | Stores identifiers in chrome.storage.sync, cookies and localStorage. Monitors storage-change events. Recreates deleted identifiers from remaining copies. Syncs across devices via Chrome profile. | Yes. Requires chrome.storage.sync API for cross-device persistence and chrome.cookies.onChanged API for real-time monitoring. Typical malware cannot access these browser-internal storage mechanisms.  
Misuse of one-time extension events | Install-time payload execution via chrome.runtime.onInstalled | The code executes once when the extension installs or updates. The event fires before the user interacts with the extension. Does not repeat on subsequent browser sessions. | Yes. The chrome.runtime.onInstalled event is extension-specific. No equivalent in typical malware.  
  
Table 1. Recurring techniques seen in GenAI high-risk extensions.

As GenAI becomes the primary interface for professional and creative workflows, these extensions can potentially gain direct access to sensitive user information. If operated within the same execution context as the AI interface, these extensions pose a significant risk to enterprises.

We placed detections from campaigns targeting AI users into six distinct malware categories based on their primary operational objective, as shown below in Figure 1. We derived these categories from manual analysis of extension code and network behavior.

![Table titled "Six Malware Categories Observed in GenAI Browser Extensions." It lists categories, names, extension IDs, users, and versions. Categories include Remote Access Trojan, InfoStealer, Search Hijacker, Brand Impersonator, Spyware, and Adversary in the browser. Various extensions with significant user numbers are detailed.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-737124-179576-1.png)Figure 1. Six distinct malware categories observed across the analyzed GenAI browser extensions.

The following sections present case studies of these six high-risk GenAI browser extensions.

## A RAT: MCP Server AI Automation Extension

A RAT is malware that grants an attacker complete remote control over a victim's system through a persistent command and control (C2) channel. This case study is for an extension named Chrome MCP Server - AI Browser Control that acts at a RAT.

  * Extension ID: fpeabamapgecnidibdmjoepaiehokgda
  * SHA256 hash: 0cbf101e96f6d5c4146812f07105f8b89bd76dd994f540470cd1c4bc37df37d5



RATs generally require victims to download and execute suspicious files, actions that security software typically detects as clear indicators of compromise. This GenAI-era adaptation disguises the RAT as an “AI browser automation tool” using the MCP framework, as shown in its Chrome Web Store listing in Figure 2. The listing deceptively states, “100% local processing - your data never leaves your browser” and “No external servers required for core functionality.”

![Screenshot of the Chrome Web Store featuring the "Chrome MCP Server - AI Browser Control" extension. The page shows details like user reviews and a section with screenshots, highlighting features of the extension.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-740228-179576-2.png)Figure 2. Deceptive malicious extension Chrome MCP Server listing on the Chrome Web Store.

Attackers lead victims to believe that extreme permissions are necessary (debugger, <all_urls>, webRequest, scripting) for AI to control the browser. The extension hardcodes a WebSocket connection to a remote C2 server, as noted in the code snippet in Figure 3.

![Code snippet from a file showing configuration settings for connecting to a remote server. The settings include host name, port number, and related URL paths for server configuration and HTTP. Reconnection intervals and maximum attempts are also specified.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-743852-179576-3.png)Figure 3. Extension’s background source code showing C2 server configuration.

From this server, it accepts over 30 remote commands, including:

  * Executing arbitrary JavaScript via new Function()
  * Chrome Debugger Protocol attachment for HTTPS traffic interception
  * Filling out forms
  * Capturing screenshots
  * Accessing browsing history



When a victim clicks Connect in the pop-up, the extension establishes a persistent WebSocket connection to a remote server, as noted from the source code snippets in Figure 4. This generates the connection to wss[:]//mcp-browser.qubecare[.]ai/chrome. Once connected, the extension reestablishes the C2 channel across network disconnections or browser restarts and the [service worker](https://developer.chrome.com/docs/extensions/develop/concepts/service-workers) restarts indefinitely.

![Two screenshots showing code snippets. The left side highlights an extension manifest with permissions that enable full browser control. The right side emphasizes a background process that initiates a persistent C2 connection via WebSocket. Below, an arrow points to a response from a C2 server containing a session ID.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-747321-179576-4.png)Figure 4. Chrome MCP Server extension source code and active WebSocket connection to the C2 server.

The extension uses a new Function() pattern to execute JavaScript code received from the remote server over the WebSocket. It then executes the code as JavaScript in the context of the victim's active tab, as noted below in Figure 5. If the victim is logged into their bank, corporate VPN, email or any other service, the remote operator can execute code in that authenticated context.

![Code snippet showing a function named `handleExecuteScript` using asynchronous JavaScript. It includes a `try` block to query active Chrome tabs and executes a script. Results are processed and errors handled with a catch statement.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-751530-179576-5.png)Figure 5. handleExecuteScript function showing remote code execution via new Function().

## Adversary in the Browser (AitB): Supersonic AI

AitB occurs when extensions read sensitive data directly from the rendered page DOM rather than intercepting network traffic, bypassing network-level security controls entirely. This case study is for an extension named Supersonic AI that performs AitB.

  * Extension ID: eebihieclccoidddmjcencomodomdoei
  * SHA256 hash: ac0a312398b3bf6b3d7c5169687ca72f361838bc5a90f2c0dbce2dc8e2094a02



Supersonic AI markets itself as an AI-powered email assistant for Gmail and Outlook. It includes features like one-click AI-generated replies and email summaries. To deliver these features, the extension needs to read email content. We examined how the extension subsequently handled this content.

As illustrated in Figure 6, a content script is used to collect comprehensive email data and send the data to an external server. This broad data collection poses a severe security and privacy risk, as it captures and sends highly sensitive information in plaintext. This means all the emails from the victim's account, including those that are read, sent or displayed.

![Code snippet illustrating a fetch API call. The method is POST, with JSON stringified body parameters including subject, from, to, body, and threadId.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-754388-179576-6.png)Figure 6. Snippet from content script.

Figure 7 demonstrates this in action within our sandbox environment, showing a social media platform one-time password (OTP) being exposed during the exfiltration process. Our [Virus Bulletin 2025 paper](https://arxiv.org/pdf/2512.10029) provides a detailed technical analysis of this extension's Gmail exfiltration behavior.

![Screenshot of a split screen. On the left is a Gmail inbox with an email highlighted, containing the number 756843. On the right is a browser's DevTools displaying a JSON response with the key "content" and the value mentioning a LinkedIn account verification code, also showing the number 756843.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-756924-179576-7.png)Figure 7. OTP exfiltration as seen in sandbox network logs.

## Infostealer: Reverse Recruiting — AI Job Application Assistant

An infostealer is malware designed to harvest sensitive information such as credentials, authentication tokens and personal data from a victim's browser. This case study covers an extension named Reverse Recruiting - AI Job Application Assistant. In addition to stealing information such as salary expectations, it also targets a new class of credentials, AI API keys.

  * Extension ID: iefpkdilnfhogjbkhgnliaomoldgkdlj
  * SHA256 hash: 604c7aef72892b56ac23ad54744376574239c8f0651e95dd5b6cf540eb70f7c3



Reverse Recruiting is an AI job application assistant, as noted in Figure 8. It autofills forms across job portals and generates tailored resumes using OpenAI, Gemini and Claude. Its permission set is consistent with a cross-site autofill and AI assistant tool, including content script injection into all page frames via <all_urls>. However, the extension uses these permissions for activities well beyond its stated purpose.

![Screenshot of a browser window displaying an AI job application assistant titled "Reverse Recruiting." The interface includes a dashboard overview with sections for applications, activity, and results analytics. There is an extension button on the right labeled "Install Extension," and options for sharing, accessing tools, and user information on the left.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-760327-179576-8.png)Figure 8. Reverse Recruiting - AI Job Application Assistant extension’s listing on the Chrome store.

When a victim provides their OpenAI, Gemini or Claude API key to power the extension's AI features, it does not use those keys locally. A component of this extension named optimized-api.js reads all three of these keys from chrome.storage.sync and forwards them to the developer's backend in custom HTTP headers on every request (Figure 9). ​

The victim also provides information for the job application assistant. The extension's profile-sync.js script then transmits the user's name, email, phone, LinkedIn URL, salary expectations, education and resume to a remote endpoint at api.reverserecruiting[.]io/v1/profile/sync.

![Screenshot snippet of JavaScript code is displayed, focusing on retrieving and handling API keys for OpenAI, Gemini, and Claude within a storage system. The code also includes a fetch request to an API endpoint.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-763193-179576-9.png)Figure 9. A code snippet that reads the user's OpenAI, Gemini and Claude API keys and forwards them to a remote server.

## Search Hijacker: Chat AI for Chrome

A search hijacker is malware that modifies browser search settings to redirect user queries through attacker-controlled servers, enabling search traffic interception and persistent tracking. This case study is for a browser extension named Chat AI for Chrome:

  * Extension ID: jhhjbaicgmecddbaobeobkikgmfffaeg
  * SHA256 hash: dfe307d957724ebe32331f92d53e366b7fa85968a9564c2285c5a0142ac9e1bb



The search hijacker changes and controls the default search engine as noted in Figure 10.

![Screenshot of Google Chrome settings under "Search engine" section. It shows an option managed by "Chat AI for Chrome," with buttons to manage or disable it. Options to manage search engines and site search are visible on the sidebar.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-765449-179576-10.png)Figure 10. Chat AI for Chrome extension controlling the search engine in Chrome.

Chat AI for Chrome generates a unique user identifier on installation and stores it in three persistence layers:

  * chrome.cookies
  * window.localStorage
  * chrome.storage.sync (syncs across all Chrome instances signed into the same Google account)



It then registers a listener on Chrome's cookie change events, as noted in the code snippet in Figure 11.

![Screenshot of a code snippet for managing cookies in a web browser extension. It adds a listener to changes in cookies and sets a new cookie with the name "tracking_id" if a specific condition is met.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-768396-179576-11.png)Figure 11. Snippet showing extension’s persistent tracking cookie behavior.

When the user deletes the tracking cookie, the extension recreates the deleted cookie. Because the ID is also stored in chrome.storage.sync, it persists across devices signed into the same Google account. Clearing cookies on one device does not eliminate the tracking. The identifier is restored from synced storage.

The persistent tracking enables a parallel attack. The extension silently replaces the victim's default search engine via chrome_settings_overrides as noted in Figure 12.

![Screenshot of a code snippet showing a JSON configuration for Chrome settings overrides. It specifies a search provider with a search URL pointing to chatgptforchrome.com and includes a key "is_default" set to true.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-771030-179576-12.png)Figure 12. Manifest snippet showing search engine hijacking via chrome_settings_overrides.

All user searches are routed through chatgptforchrome[.]com and correlated with the persistent tracking ID, building a cross-device search history profile that standard cookie-clearing practices cannot disrupt. The only effective remediation is complete uninstallation.

## Brand Impersonator: AI Photo and Video Editor

A brand impersonator is malware that mimics legitimate software brands to exploit user trust and bypass skepticism during installation. This case study is for an extension named that impersonates a popular graphics editing brand.

  * Extension ID: hmkcidjcpomiegnklmplkimmbcbklglb
  * SHA256 hash: 4e38bee33237a8c8b17a2504013e506ca7cbf667a7f68a2d94d75db505c2149f



It exploits the onInstalled listener that opens a “thank you” page immediately after installation, as noted in Figure 13. Figure 14 shows the result of the thanks.html page.

![Screenshot of a code snippet showing a script for a Chrome extension. It adds a listener to open "thanks.html" upon installation, with comments in English and Polish explaining the function.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-773348-179576-13.png)Figure 13. Snippet showing onInstalled listener opening a forced tab for thanks.html.![Screenshot showing a webpage with two sections. The left side displays a blurred image with a 3.5-star rating and an overview text. The right side promotes Opera GX with features like tech and privacy tools, a seamless extension support, and quick setup steps.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-775719-179576-14.png)Figure 14. (Left) Impersonating graphics extension (right) Thank you page, on install it drives traffic to third-party browser install.

Of note, the thanks.html file communicated with a URL hosted on xuix[.]top, which redirected to the newextensioninstallweb[.]com/2025 URL noted in Figure 14.

## Spyware: 会译:一站式 AI 翻译 Agent｜对照式DeepL翻译｜DeepSeek划词翻译｜免费

Spyware is malware designed to covertly monitor and collect user activity, browsing behavior and personal data without explicit consent. This case study is for a Chinese language extension from Huiyi named 会译:一站式 AI 翻译 Agent｜对照式DeepL翻译｜DeepSeek划词翻译｜免费 that acts as spyware.

  * Extension ID: dgeiaiglmhdhajbpfbmajaajdlfdinpi
  * SHA256 hash: c9754454efede2dec2fcb856faa40424b8df378706b664a5ae4847fcd0336b53



This extension provides functional Chinese-English translation. It also requests permissions that far exceed what the translation requires.

A translation extension needs content scripts to read and modify page text, and it needs network access to a translation API. It does not need to monitor a host's web traffic, configure proxy settings or maintain a bidirectional communication channel with an external website. This extension requests all of these permissions as noted in Figure 15.

![Screenshot of a code snippet listing permissions required for browser extensions. It includes permissions like storage, scripting, context menus, and web requests. Host permissions allow access to all URLs, and external connectivity matches a specific URL pattern.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-779533-179576-15.png)Figure 15. Manifest snippet showing broad permissions and external connectivity to huiyiai[.]net.

The extension registers 

chrome.webRequest.onCompleted

listeners that trigger for every completed HTTP request across all websites. Additionally, the extension downloads a proxy auto-configuration (PAC) script from 

hxxps[:]//yiban[.]io/extension/proxy.pac?t=huiyi

on startup and applies it via 

chrome.proxy.settings.set()

as noted in Figure 16.

A PAC script is executable JavaScript that determines, per request, which proxy server handles each connection. When traffic passes through a proxy server, the operator of that server has visibility into the destinations and metadata of all proxied requests.

![Screenshot of a code snippet showing JavaScript configuration for a proxy script. The script fetches a PAC file and sets it using Chrome proxy settings.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-782491-179576-16.png)Figure 16. Snippet showing malicious proxy hijacking via dynamically fetched content.

As noted in Figure 16, the extension fetches a PAC script (proxy.pac) from the URL at yiban[.]io. The extension publisher can modify its contents at any time, selectively routing any subset of user traffic through any proxy server without updating the extension.

## AI-Accelerated Campaigns

Beyond malware discovery, we observed an increasing trend in threat actors using LLMs to produce high-risk extensions. One example is a 10xprofit affiliate hijacking campaign [documented in a threat research article by Socket](https://socket.dev/blog/malicious-chrome-extension-performs-hidden-affiliate-hijacking).

The campaign runs six extensions that silently inject affiliate tags into several popular online retailers or fast fashion brands without user consent. Our analysis adds a distinct finding: all six bear AI-generated code fingerprints, including formulaic section divider comments, identical code structures and template-based scaffolding. This is despite targeting different e-commerce platforms. Figure 17 below shows an example of the code structure.

![Screenshot of a code snippet showing a configuration for links in a JavaScript object with comments detailing different sections: Configuration, State, Functions, and Init. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-784697-179576-17.png)Figure 17. Extension code showing AI-generated indicators from the 10xprofit affiliate hijacking campaign.

## Conclusion

The extensions uncovered in our research represent more than isolated incidents. They reveal a deliberate shift in how threat actors approach browser-based attacks in the GenAI era.

Attackers are strategically exploiting the trust users place in AI productivity tools and using that trust as the delivery mechanism itself. Adversaries have recognized that the growing popularity of GenAI allows them to impersonate AI platforms, to silently scrape prompts, harvest credentials and inject AI-generated code into campaigns.

Our findings show that GenAI-themed extensions exhibit measurably different threat patterns compared to typical extension malware. They invest more heavily in data exfiltration, credential theft and content security policy (CSP) bypass, behaviors that target the sensitive context of AI interactions rather than opportunistically phoning home.

Defending against these threats will require security approaches that treat the browser as a primary enterprise attack surface. Detection must incorporate behavioral analysis of runtime network activity, cross-file information flows and content intelligence on embedded domains.

Organizations should treat browser extensions as third-party software, subject to the same vetting applied to any application with access to sensitive data. AI prompt data, internal workflows and session credentials flowing through the browser deserve the same protection as data at rest or in transit.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

  * [Advanced URL Filtering](https://www.paloaltonetworks.com/network-security/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) identify known domains and URLs associated with this activity as malicious.
  * [Prisma Browser](https://www.paloaltonetworks.com/sase/prisma-browser) provides protection against malicious browser extensions, including examples described in this article, with the integrated advanced extension security. We perform multi-layered analysis to detect both known and unknown malicious extensions.
  * [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) is designed to provide layered, real-time protection for AI systems by detecting and blocking threats, preventing data leakage and enforcing secure usage policies across a variety of AI applications.
  * The [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire) machine-learning models and analysis techniques have been reviewed and updated in light of the indicators shared in this research.



If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107
  * South Korea: +82.080.467.8774



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Acknowledgments

We’d like to thank the entire Unit 42 team for supporting us with this article. Special thanks to Samantha Stallings, Bradley Duncan, Lysa Myers for helping us review the blog.

## Indicators of Compromise

Table 2 lists 18 high-risk Chrome extensions masquerading as AI applications.

**User Count** | **Extension ID** | **Extension Name** | **Version** | **Associated URL, Domain or Server**  
---|---|---|---|---  
1000 | fpeabamapgecnidibdmjoepaiehokgda | Chrome MCP Server - AI Browser Control | 1.0.1 | mcp-browser.qubecare[.]ai  
30000 | oaldjcdohhhibelagdhoahbedekfjjjf | browser cash | 1.0.3 | browser[.]cash  
7000 | nbflcljmdbibeoaipongjgfmbapanipm | Anker AIME Copilot | 1.0.2 | 172.16.18[.]184:5443/web-info  
4000 | ffocfibjgakneigiajpccfcdmomlbapo | Nano Banana | 1.3.0 | banana.summarizer[.]one/quota  
5000 | npifianbfjhobabjjpfdjjihgbdnbojh | Text Summarizer | 1.1.0 | ws[:]//158.160.66[.]115:40000/summary  
2000 | pfdmleklaejjccgfhoeafapbhkjipcnj | Google AI | 1.2 | N/A  
20000 | dgeiaiglmhdhajbpfbmajaajdlfdinpi | 会译:一站式 AI 翻译 Agent｜对照式DeepL翻译｜DeepSeek划词翻译｜免费 | 1.6.16 | N/A  
1000 | hnppehcgmflfkcdkbkaeemjfngffmeag | AI Agent | 1.9 | 199.80.55[.]27:3130  
3000 | ljlhpcabhpjdlcjhbmgjigfceppgabmk | Notion中文版 | 1.1.0 | notionapp[.]cn  
1511 | pdahnbohfcekobflehebdkoemnmmempk | Notion中文版 | 1.0.6 | N/A  
192 | jndldoeopjgmpakgmieaeeelhnjnfgkj | NotionAI插件 | 1.1.4 | N/A  
563 | bonhfflnjgdbnhcpjemkknlhimceckgb | Agent Risk Reminder Remover - CNFans, ACBuy & More | 1.0.1 | N/A  
1 | iefpkdilnfhogjbkhgnliaomoldgkdlj | Reverse Recruiting - AI Job Application Assistant | 0.3.0 | api.reverserecruiting[.]io/  
2000 | jhhjbaicgmecddbaobeobkikgmfffaeg | Chat AI for Chrome | 1.1.2 | chatgptforchrome[.]com  
579 | hmkcidjcpomiegnklmplkimmbcbklglb | [_Redacted_]: AI Photo, Video | 1.0 | xuix[.]top  
1000 | cjmhegifablecgkkncjddcgkjmgoacfd | Ask AI - GPT chat | 1.1 | vomet[.]ru  
608 | dcjfbgppfdokmjgajnnkgdmkdeiloigh | Picsart: AI Photo Video Editor | 1.1 | pic-editor-chromeextension[.]uno  
17 | eebihieclccoidddmjcencomodomdoei | Supersonic AI | 1.0.6 | gosupersonic[.]email  
  
Table 2. Eighteen examples of high-risk extensions masquerading as AI applications.

## Additional Resources

  * [Malicious GenAI Chrome extensions: unpacking data exfiltration and malicious behaviours](https://www.virusbulletin.com/conference/vb2025/abstracts/malicious-genai-chrome-extensions-unpacking-data-exfiltration-and-malicious-behaviours/) – Shresta B.Seetharam, Mohamed Nabeel and William Melicher, presented at Virus Bulletin 2025



Back to top

### Tags

  * [AI browser](https://unit42.paloaltonetworks.com/tag/ai-browser/ "AI browser")
  * [Browser extension](https://unit42.paloaltonetworks.com/tag/browser-extension/ "browser extension")
  * [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
  * [Infostealer](https://unit42.paloaltonetworks.com/tag/infostealer/ "Infostealer")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [Remote Access Trojan](https://unit42.paloaltonetworks.com/tag/remote-access-trojan/ "Remote Access Trojan")
  * [Search hijacker](https://unit42.paloaltonetworks.com/tag/search-hijacker/ "search hijacker")
  * [Spyware](https://unit42.paloaltonetworks.com/tag/spyware/ "spyware")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: TGR-STA-1030: New Activity in Central and South America ](https://unit42.paloaltonetworks.com/new-activity-central-south-america/ "TGR-STA-1030: New Activity in Central and South America")

### Table of Contents

  *   * Executive Summary
  * Examples of Extensions Disguised as AI Tools
  * Browser Extensions Expand the Client-Side Attack Surface
  * A RAT: MCP Server AI Automation Extension
  * Adversary in the Browser (AitB): Supersonic AI
  * Infostealer: Reverse Recruiting — AI Job Application Assistant
  * Search Hijacker: Chat AI for Chrome
  * Brand Impersonator: AI Photo and Video Editor
  * Spyware: 会译:一站式 AI 翻译 Agent｜对照式DeepL翻译｜DeepSeek划词翻译｜免费
  * AI-Accelerated Campaigns
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Acknowledgments
  * Indicators of Compromise
  * Additional Resources



### Related Articles

  * [ Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "article - table of contents")
  * [ Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "article - table of contents")
  * [ Identity Abuse Through Trusted Communication Channels ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "article - table of contents")



## Related Malware Resources

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

![Pictorial representation of a magnifying glass illuminating a glowing orange circular digital circuit interface on a dark, high-tech background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) September 16, 2026 #### [Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS \(AMOS\) Stealer Activity")

![Pictorial representation of post-exploitation identity misuse in SPIFFE/SPIRE. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 10, 2026 #### [The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [Cryptographic](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")

![Pictorial representation of a pay-per-install threat group campaign prodiving infection service for spreading malware. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip, symbolizing data processing and transfer. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 9, 2026 #### [Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

  * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")
  * [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")
  * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")

![Pictorial representation of attackers using AI tools to target Latin American organizations. A vibrant cityscape with silhouettes of numerous people walking along a bustling street. The scene is illuminated by bright urban lights and digital-like particles, creating a dynamic and futuristic atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2026 #### [Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")

![Pictorial representation of vishing campaigns in Microsoft Teams. A digital image of a skull formed by blue binary code on a black background, with scattered ones and zeros and digital noise, symbolizes how stealthy prompt injection attacks can exploit AI logic to bypass security controls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 31, 2026 #### [Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

  * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")

![Pictorial representation of AI-enabled malware. A vibrant digital interface displaying various icons and graphs, resembling a futuristic network or data analysis dashboard. The scene is illuminated with glowing lights and patterns.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 25, 2026 #### [The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

  * [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")
  * [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
  * [DLL hijacking](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")

![Pictorial representation of identity abuse through trusted communication channels. Close-up view of a digital screen displaying a glitched and pixelated image of a skull-like shape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 20, 2026 #### [Identity Abuse Through Trusted Communication Channels ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

  * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")
  * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

![Pictorial representation of a magnifying glass illuminating a glowing orange circular digital circuit interface on a dark, high-tech background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) September 16, 2026 #### [Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS \(AMOS\) Stealer Activity")

![Pictorial representation of post-exploitation identity misuse in SPIFFE/SPIRE. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 10, 2026 #### [The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [Cryptographic](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")

![Pictorial representation of a pay-per-install threat group campaign prodiving infection service for spreading malware. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip, symbolizing data processing and transfer. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 9, 2026 #### [Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

  * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")
  * [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")
  * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")

![Pictorial representation of attackers using AI tools to target Latin American organizations. A vibrant cityscape with silhouettes of numerous people walking along a bustling street. The scene is illuminated by bright urban lights and digital-like particles, creating a dynamic and futuristic atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2026 #### [Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")

![Pictorial representation of vishing campaigns in Microsoft Teams. A digital image of a skull formed by blue binary code on a black background, with scattered ones and zeros and digital noise, symbolizes how stealthy prompt injection attacks can exploit AI logic to bypass security controls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 31, 2026 #### [Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

  * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")

![Pictorial representation of AI-enabled malware. A vibrant digital interface displaying various icons and graphs, resembling a futuristic network or data analysis dashboard. The scene is illuminated with glowing lights and patterns.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 25, 2026 #### [The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

  * [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")
  * [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
  * [DLL hijacking](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")

![Pictorial representation of identity abuse through trusted communication channels. Close-up view of a digital screen displaying a glitched and pixelated image of a skull-like shape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 20, 2026 #### [Identity Abuse Through Trusted Communication Channels ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

  * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")
  * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/)