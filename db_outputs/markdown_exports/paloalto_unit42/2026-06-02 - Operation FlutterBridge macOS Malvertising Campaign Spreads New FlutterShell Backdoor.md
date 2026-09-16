# Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/
- **Date :** 2026-06-02

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Operation FlutterBridge: macOS Malvertising Campaign Spreads New FlutterShell Backdoor

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 17 min read 

Related Products

[![Advanced WildFire icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced WildFire](https://unit42.paloaltonetworks.com/product-category/advanced-wildfire/ "Advanced WildFire")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Ido Asher](https://unit42.paloaltonetworks.com/author/ido-asher/)
    * [Noa Dekel](https://unit42.paloaltonetworks.com/author/noa-dekel/)
    * [Tom Fakterman](https://unit42.paloaltonetworks.com/author/tom-fakterman/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:June 2, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [CL-CRI-1089](https://unit42.paloaltonetworks.com/tag/cl-cri-1089/)
    * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/)
    * [Malvertising](https://unit42.paloaltonetworks.com/tag/malvertising/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Operation%20FlutterBridge:%20macOS%20Malvertising%20Campaign%20Spreads%20New%20FlutterShell%20Backdoor&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fflutterbridge-new-fluttershell-backdoor%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fflutterbridge-new-fluttershell-backdoor%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fflutterbridge-new-fluttershell-backdoor%2F&title=Operation%20FlutterBridge:%20macOS%20Malvertising%20Campaign%20Spreads%20New%20FlutterShell%20Backdoor "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fflutterbridge-new-fluttershell-backdoor%2F&text=Operation%20FlutterBridge:%20macOS%20Malvertising%20Campaign%20Spreads%20New%20FlutterShell%20Backdoor "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fflutterbridge-new-fluttershell-backdoor%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Operation%20FlutterBridge:%20macOS%20Malvertising%20Campaign%20Spreads%20New%20FlutterShell%20Backdoor%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fflutterbridge-new-fluttershell-backdoor%2F "Share in Mastodon")



## Executive Summary

We are tracking an increasingly widespread malvertising campaign targeting macOS. This campaign appears to be the next stage of a previous campaign known as JSCoreRunner, which was first identified in August 2025. In recent months, the financially-motivated attackers behind these campaigns transitioned from delivering standard adware, to delivering adware with full backdoor capabilities. We designate this campaign Operation FlutterBridge, and we call the payload that it delivers FlutterShell.

Built using the Flutter framework, FlutterShell infects targets with adware via malicious desktop applications. In addition to its adware functionality, the payload possesses backdoor capabilities, including shell command execution and file system manipulation. Some variants weaponize artificial intelligence (AI) summarization features for data exfiltration by routing documents through an attacker-controlled server before processing them. The FlutterShell malware strain appears to be under active development, with new improvements being rapidly integrated into the code.

Operation FlutterBridge targets a global audience through an extensive Google Ads campaign, with an emphasis on Anglophone and Western European markets, distributed via hundreds of Google-verified advertisements. Our research indicates that the attackers behind this cluster distributed the ads using a series of shell companies, to bypass ad-network vetting and orchestrate these attacks at scale.

We reported these advertisers to Google, which provided the following statement:

_Malware has no place on our platforms, and we’ve suspended these advertiser accounts for violating our policies._

We track Operation FlutterBridge and the JSCoreRunner campaign under a cluster of activity that we refer to as [CL-CRI-1089](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/).

This article provides a technical overview of the FlutterShell macOS malware and the delivery network behind the malvertising campaigns.

Palo Alto Networks customers are better protected from the threats described in this article through the following products and services:

  * [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire)
  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security)
  * [Cortex Agentix](https://www.paloaltonetworks.com/cortex/agentix) Threat Intel Agent
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | [**macOS**](https://unit42.paloaltonetworks.com/tag/macos/), **[Malvertising](https://unit42.paloaltonetworks.com/tag/malvertising/)**  
---|---  
  
## Campaign Background

CL-CRI-1089 is a cybercrime cluster of activity that has been operational since at least 2023. The attackers behind this cluster are responsible for spreading malicious payloads via [malvertising](https://www.imperva.com/learn/application-security/malvertising/) campaigns, targeting both Windows and macOS users through separate, ongoing operations.

The attackers’ modus operandi is consistent across these operations: They distributed malicious advertisements using a network of Google-verified shell companies. These ads were designed to trick targets into deploying malware that masquerades as legitimate desktop applications. While in-the-wild observations suggest the malware functions primarily as adware, it possesses capabilities for far more dangerous behavior, effectively functioning as a backdoor.

Operations attributed to this cluster include the [RecipeLister](https://www.bluevoyant.com/blog/recipelister-a-recipe-for-disaster) and [Calendaromatic](https://medium.com/@rabbit_knight/when-your-calendar-wants-to-steal-your-tokens-a-look-at-calendaromatic-81c15bb7ed9e) Windows campaigns, as well as the [JSCoreRunner](https://9to5mac.com/2025/08/27/mosyle-identifies-new-mac-malware-that-evades-detection-through-fake-pdf-conversion-tool/) macOS campaign. The Windows activity was previously tracked by other vendors under the broader “TamperedChef” designation, before Unit 42 researchers [deconstructed](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/) the activity into distinct clusters. In late 2025, the attackers expanded their operations with Operation FlutterBridge, deploying a new macOS backdoor identified as FlutterShell.

## Overview of the FlutterShell Malware

FlutterShell is a macOS backdoor developed using the [Flutter framework](https://flutter.dev/) and designed to masquerade as legitimate software. FlutterShell’s authors implemented a WebView-based architecture that utilizes a JavaScript-to-native bridge. This design allows the attackers to host malicious logic on an external website, rather than hardcoding it into the binary. This enables the attackers to dynamically alter FlutterShell's behavior in real time, without needing to recompile or redistribute the application.

FlutterShell has a set of built-in commands that provide attackers with the following capabilities:

  * Arbitrary command execution
  * File system interaction
  * Environment variables exfiltration



During our investigation, we observed FlutterShell being used as adware. Upon execution, the malware modifies Google Chrome configuration files to hijack the browser, forcing all traffic through an attacker-controlled, ad-filled intermediary site.

We identified several versions of FlutterShell that did not yet contain malicious code. Additionally, an examination of the JavaScript logic hosted on the attackers’ infrastructure revealed multiple unfinished functions. These findings, combined with the frequent appearance of new variants, indicate that the malware is likely under active development.

The use of the Flutter framework presents specific analytical hurdles. The Flutter engine compiles [Dart](https://dart.dev/) code into a dynamic library and uses an [Object Pool](https://www.geeksforgeeks.org/java/object-pool-design-pattern/) to store data. This separates the code from the strings and variables it uses, making it difficult for security analysts to see how the malware actually functions. This feature also makes tracing the execution flow of a Flutter application via static analysis particularly challenging. To overcome these challenges, we used a custom version of [Worawit Wangwarunyoo's blutter tool](https://github.com/worawit/blutter) to disassemble the Dart binary and reconstruct the application logic.

### FlutterShell Deployment and Masquerading

We encountered three versions of FlutterShell in which the malware posed as a podcast player and two different PDF viewers. These desktop applications were fully functional, effectively concealing the malicious logic executing in the background. Figure 1 shows two of the applications on macOS hosts.

![A screenshot of a computer screen split into two main sections. On the left, a podcast application displays a selection of podcast covers, including "The Daily," "Pardon My Take," and "Science Vs." On the right, a PDF viewer application is open, displaying a password-protected file message prompting to unlock the PDF. The background shows a forest scene with tall trees.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-497587-181830-1.png)Figure 1. FlutterShell masquerading as a legitimate podcast player and PDF viewer application.

All observed samples were signed with valid Apple Developer IDs and successfully passed notarization, meaning Apple's automated security checks did not flag them as malicious at the time of submission. Figure 2 shows the legitimate signature of FlutterShell’s binaries and its successful notarization by Apple.

![A screenshot of a notarization confirmation window for the application "podcasts_lounge," signed by Apple Dev ID. It includes details about the file path, entitlements, and signing authorities. The window features buttons for viewing hashes and entitlements, and a close button.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-505156-181830-2.png)Figure 2. FlutterShell is signed with valid Apple Developer IDs and successfully passed notarization.

At the time of analysis, all three applications containing FlutterShell had zero detections on VirusTotal, as shown in Figure 3 for the PodcastsLounge application.

![A screenshot of a security check from VirusTotal indicating a file is safe. It shows a score of 0/65, meaning no security vendors flagged the file as malicious. The file details include a string of alphanumeric characters and the name ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-507934-181830-3.png)Figure 3. Malware analysis conducted on VirusTotal.

### FlutterShell Technical Analysis

#### FlutterShell’s Malicious WebView Architecture

The FlutterShell backdoor logic is not hardcoded into the binary. Instead, FlutterShell employs a WebView-based architecture utilizing a JavaScript-to-native bridge.

In WebView-based architecture, a native application uses an embedded web browser component to display content. The JavaScript-to-native bridge acts as a communication channel between this web content and the host native application, allowing them to exchange data and cross-invoke functionality.

Consequently, the malicious logic of FlutterShell is stored on the attackers’ website and is only triggered when the application loads the specific web content. Figure 4 demonstrates how the application converts web content to native commands.

![A diagram illustrates the flow of code execution in an application. It includes a WebView Engine that requests and returns web content, a JavaScript Bridge, and the main components of macOS. The setup interacts with a network, performs command execution, and accesses the file system. The bridge facilitates code execution from WebView to native macOS components.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-509919-181830-4.png)Figure 4. WebView architecture to native OS code execution graph.

Upon initial execution, FlutterShell waits for a specific duration received dynamically from the command and control (C2) server before contacting the attackers’ website — which contains the malicious JavaScript code — to avoid analysis and build user trust. More details about the backdoor’s delay routine are provided in Appendix A.

#### JavaScript Bridge Injection Technique

The primary payload of FlutterShell is embedded within the main webpage and a /update-thanks.html subdirectory of the attacker-controlled site. Figure 5 shows the website's landing page.

![A software update screen for Podcast Lounge shows a success message. The update features version 1.0.1, with an update date of January 1, 2026, and the status is "Up to Date." The background is a gradient from purple to blue.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-512234-181830-5.png)Figure 5. “Thank You for Updating!” landing page that hides the malicious logic of FlutterShell.

To facilitate communication between the remote attacker-controlled webpage and the infected local system, the malware injects a JavaScript bridge. This bridge uses a message channel named flutterInvoke to pass JSON-formatted commands from the WebView context into the native Dart environment.

The remote webpage acts as the execution environment for the JavaScript-to-native bridge. By loading the external content, the attackers can send JSON-formatted commands to the application, which are then translated into native system calls and operations on the infected machine.

The main webpage and the /update-thanks.html subdirectory retrieve the core malicious logic from external endpoints: /getConfig and /getUpdateThanksConfig, respectively. These scripts contain the JavaScript code that defines which commands should be executed and configures the supported functionality. This architecture allows the attackers to modify the code in /getConfig and /getUpdateThanksConfig at any moment, dynamically altering FlutterShell's behavior without requiring a software update. Figure 6 shows the HTML page presented to the targeted end-user, followed by the subsequent JavaScript code executed by the payload.

![A screenshot of JavaScript code. The function `loadConfig\(\)` loads a script dynamically. If the loading succeeds, a console message confirms success, and a button's text changes to indicate success. If it fails, an error message is logged, the button is enabled, and the text changes to prompt a retry.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-515967-181830-6.png)Figure 6. JavaScript code in /update-thanks.html responsible for retrieving the malicious logic.

At the time of investigation, the call to /getConfig was either commented out on the main page or the endpoint was unreachable. We also noticed that /getUpdateThanksConfig contained setup functions for commands that were not yet implemented in the FlutterShell binary. The observed inactivity and disabled functions strongly indicate that the malware was still under active development.

### Variants and Evolution of FlutterShell

Our investigations up until February 2026 revealed three main variants of the FlutterShell backdoor, each advertised approximately one month apart. The first variant masqueraded as a podcast app named PodcastsLounge while the subsequent variants appeared as PDF viewers named PDF-Brain and PDF-Ninja.

While the three variants masqueraded as different applications, the malicious code and execution flow embedded within them have only minor differences. Notably, the internal package name of the PDF-Brain variant was still labeled podcasts_lounge, revealing its connection to the earlier version.

With each new variant released, we observed developments in the obfuscation used by the attackers behind the campaign. The second variant (PDF-Brain) had some of its strings obfuscated, and the third variant (PDF-Ninja) utilized Flutter’s native \--obfuscate flag, which strips debug information and randomizes symbol names, making reverse engineering significantly more difficult. Furthermore, the attackers renamed the malicious commands to mimic legitimate PDF library operations, likely in an attempt to bypass static analysis and Apple's notarization process.

The main differences and overlaps between the three variants are listed in Table 1.

**Feature** | **Variant: PodcastsLounge** | **Variant: PDF-Brain** | **Variant: PDF-Ninja**  
---|---|---|---  
**Execution Command** | exec_sync | pdf_sync | renderPDF  
**Command Naming Scheme** | Descriptive naming  (e.g: read_file, write_file) | Descriptive naming  (e.g: read_file, write_file) | Deceptive naming  (e.g: read_pdf, write_pdf)  
**String Storage** (/bin/sh**)** | Plaintext | Base64-encoded | Plaintext (regression)  
**Binary Obfuscation** | None | None | Flutter \--obfuscate enabled  
**C2 Domain** | atsheisdomestic[.]org | etoftheappyrince[.]org | healightejustb[.]org  
  
Table 1. Feature comparison matrix of FlutterShell variants.

Another feature differentiating the PDF-Brain and PDF-Ninja variants is an AI summarization tool that doubles as a data exfiltration vector. Instead of sending the file content directly to an AI Agent, FlutterShell forwards the content to the attackers’ C2 server, at the https://[attacker_domain]/summarize-text endpoint. The server functions as an intermediary, forwarding the request to the AI agent. This means that while the user receives an AI summary, the attackers can simultaneously harvest and exfiltrate the entire content of every document processed.

Additionally, we observed that the download sites for PodcastsLounge and PDF-Brain malicious applications share a nearly identical design structure, indicating that the attackers reused the web assets for both campaigns. Figure 7 shows screenshots from both sites.

![Two screenshots of side-by-side website interface designs. The left side is for "Podcasts Lounge," featuring options to listen, discover, and manage podcasts, with highlighted buttons for exploring and downloading. The right side is for "App Denise," focusing on viewing and editing PDFs, with options to download and learn more. Both interfaces have prominent color schemes and feature navigational buttons and text.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-518136-181830-7.png)Figure 7. PodcastsLounge delivery website (left) and PDF-Brain delivery website (right).

We also encountered versions of these macOS applications that did not contain any malicious code.

We also noted that the attackers behind CL-CRI-1089 offered Windows versions for all FlutterShell applications. However, up to early February 2026 the Windows versions did not appear to contain any embedded malicious logic. The absence of malicious code in both the macOS and Windows applications may suggest a phased deployment strategy, a technique designed to bypass automated detection.

#### FlutterShell’s Adware Payload

According to our telemetry, the attackers’ primary goal appeared to be browser hijacking. Upon installation, FlutterShell fingerprints the machine by collecting the hardware’s universally unique identifier (IOPlatformUUID) value using the following command:

ioreg -rd1 -c IOPlatformExpertDevice | grep IOPlatformUUID | sed 's/.*"IOPlatformUUID" = "//; s/"//g'

Next, the malware targets the Google Chrome “Secure Preferences” file. This file functions as an anti-tamper mechanism by storing a validated copy of the user's settings.

FlutterShell modifies the default_search_provider_data block within this file, specifically changing the url and new_tab_url values to the attacker-controlled domain sinterfumesco[.]com. This modification ensures that every time a user with an infected machine performs a search or opens a new tab, the request is hijacked and sent to the attackers’ domain. Figure 8 shows the modified Secure Preferences file.

![A screenshot of code displaying JSON data is shown. Red boxes highlight changes made to two fields: "new_tab_url" and "url," with both values altered.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-520778-181830-8.png)Figure 8. The modified Secure Preferences file.

To apply the URL and domain changes, FlutterShell terminates the Google Chrome process using killall "Google Chrome" and immediately relaunches the process with the following arguments:

Google Chrome "hxxps[:]//sinterfumesco[.]com/search?utn=[Tracking Data]=&q=starttt" --restore-last-session --hide-crash-restore-bubble --noerrdialogs --disable-session-crashed-bubble

These flags force Chrome to connect to sinterfumesco[.]com while suppressing the crash restoration warnings (“Chrome did not shut down correctly”) that would normally appear after a forced termination.

This sequence enables attackers to generate revenue by funneling targeted users through an ad-filled intermediary site or showing ads in the background, before finally redirecting the users to a legitimate search engine. Figure 9 shows the detection of suspicious FlutterShell activity, including executing fingerprinting commands and browser hijacking.

![A diagram shows a flow of actions related to the "podcasts_lounge" app. It consists of nodes connected by lines with arrows. Annotations detail commands for executing a fingerprint command and launching Google Chrome with a specific URL. The bottom includes a table listing file actions involving Google Chrome preferences and login data.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-523021-181830-9.png)Figure 9. FlutterShell browser hijacking activity, as seen in Cortex XDR.

## CL-CRI-1089: Campaign Infrastructure and Evolving Tradecraft

We examined the evolution of CL-CRI-1089’s tactics and tradecraft across multiple campaigns since early 2025.

### CL-CRI-1089 Ads Delivery Network

Our investigation tracked the activity cluster CL-CRI-1089 through a far-reaching network of Google and YouTube advertisements, both of which are controlled by Google Ads. While Google apparently remediated several ads linked to previous campaigns, the advertiser remained active, and FlutterShell continued to be distributed via hundreds of active advertisements with new instances throughout February 2026.

#### Verified Shell Entities

Verified Google Ads accounts were the primary distribution vehicle for FlutterShell in this campaign, using verified shell companies AdsParkPro LTD and Advantage Web Marketing LLC. We also observed that this cluster used a different shell entity called SOFT WE ART LIMITED in past Windows campaigns. At first glance, these companies appeared to be legitimate Ukraine and UK-based enterprises, registered years before the malicious activity ever started. Figure 10 shows advertisements by Advantage Web Marketing LLC in the Google Ads Transparency Center.

![A webpage displaying advertisement details for "Advantage Web Marketing LLC," based in Ukraine. There are four ad examples listed: "View Template \(PDF\)," "Print Now \(Calendar\)," "Printable PDF \(Free\)," and "Start Download \(Free\)." Each ad is associated with Convert Flow - Advanced PDF Software.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-525908-181830-10.png)Figure 10. Tracking Advantage Web Marketing LLC advertisements in Google Ads Transparency Center.

However, although the accounts were verified by Google Ads, a closer look into the three companies revealed the hallmarks of a shell corporation designed for ad-fraud and malware delivery:

  * All three companies have a minimal digital presence beyond their company websites. The websites themselves have minimal functionality and utilize templated structures, likely designed to create an impression of legitimacy.
  * Similar patterns in corporate filings revealed one Ukrainian-based and two UK-based companies led by Ukrainian nationals with no verifiable professional history or digital identity.
  * We identified an approximate one-year latency between the initial Google Ads registration and the first recorded ad spend. This suggests a maturation strategy, in which the attackers allow a legal entity to age, in order to bypass initial fraud-detection filters.



Given the apparent absence of legitimate commercial activity, we assess that these companies were created as a vehicle for this malicious advertising infrastructure.

During our research, we saw proof of the attackers' agility in real-time: AdsParkPro LTD's advertisements were entirely removed from the Google Ads Transparency Center on January 19, 2026. Simultaneously, online business records were modified to list the company as dormant. However, just two weeks later, the actor re-emerged with a new FlutterShell variant, promoted via another verified advertiser, Advantage Web Marketing LLC.

Advantage Web Marketing LLC has been [observed](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/) not only spreading malicious advertisements but also acting as the signatory for Windows adware variants associated with the CL-CRI-1089 cluster. This suggests that the other identified shell entities (AdsParkPro LTD and SOFT WE ART LIMITED) could also be leveraged in the future to sign malicious binaries.

#### Adversary Tradecraft and OpSec Failures

Despite the scale and reach of the campaign, the attackers exhibited poor attention to detail in their creative assets. Many advertisements used nonsensical or poorly translated content and generic unpolished visuals. We also observed several instances of cross-contamination, where the actor inadvertently linked the logo of a previous malicious product with the current masqueraded application. Figure 11 shows that PodcastsLounge advertisements display graphics relating to a PDF viewer.

![An advertisement with text offering to start a free download, featuring the names "Podcasts Lounge" and "AdsParkPro LTD," alongside a "View PDF" button. Another section repeats "Download \(free\)" with a "Print Manual" icon.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-528296-181830-11.png)Figure 11. Cross-contamination between two different malicious ads.

The targeting strategy of the advertisements is broad, but deliberate. While most ads were accessible globally, we identified specific geographic clusters where the actor focused their budget. These included Western European markets (notably France and Germany) and English-speaking regions, including the U.S., Canada and Australia. We identified multiple infected hosts targeted by this threat from correlating regions.

### Connecting the Dots Behind CL-CRI-1089 Campaigns

This section details the connection between FlutterShell and the two Windows malware strains operated by the attackers behind CL-CRI-1089, and the strong links between FlutterShell and its predecessor JSCoreRunner. This relationship is evident across their infrastructure, architecture and operational behavior.

#### The CL-CRI-1089 Connection

By pivoting on infrastructure related to the ad-filled intermediary site used in the FlutterShell campaign, we linked the current macOS campaign to two Windows malware strains: [RecipeLister](https://www.bluevoyant.com/blog/recipelister-a-recipe-for-disaster) and [Calendaromatic](https://medium.com/@rabbit_knight/when-your-calendar-wants-to-steal-your-tokens-a-look-at-calendaromatic-81c15bb7ed9e). Both of these strains were distributed via malvertising campaigns, and are tracked as part of the CL-CRI-1089 cluster of activity. High traffic rankings for these related domains indicate a wide distribution of the adware.

Calendaromatic and RecipeLister also share technical similarities with FlutterShell, including a WebView-based code architecture that allows dynamic payload changes. In the case of the RecipeLister and Calendaromatic malware strains, the actor encoded content within hidden characters or date synonyms. In FlutterShell, the attacker directly embedded the commands in the website’s content.

All of the malicious applications hijack the victim's browser, redirecting it to similarly structured websites, which present the user with icons linked to well-known brands.

When looking into RecipeLister, we found yet another shell entity responsible for spreading malicious adware — SOFT WE ART LIMITED. This company shares commonalities with other shell companies tied to Operation FlutterBridge: a UK-based entity with one Ukrainian member of personnel who could not be traced to any known real employees. The company’s current website remains active, and shares content and phrasing similarities with AdsParkPro LTD’s previous digital footprint, which has transitioned across three distinct domains since 2024.

#### The JSCoreRunner Connection

In addition to its connection with Windows-based campaigns, our analysis identified significant links between FlutterShell and the previously documented [JSCoreRunner](https://9to5mac.com/2025/08/27/mosyle-identifies-new-mac-malware-that-evades-detection-through-fake-pdf-conversion-tool/) (also known as FileRipple).

As mentioned in a report by Moonlock Labs, JSCoreRunner was also distributed by the [same verified publisher](https://moonlock.com/jscorerunner-fake-pdf-converters) — AdsParkPro LTD. This shared distribution point is the first key indicator that the campaigns are connected. Furthermore, the technical characteristics of both strains confirm a shared origin; they both utilize a specialized JavaScript-to-native bridge and exhibit clear similarities in command structure and functionality. These similarities are discussed in further detail in Appendix B.

Figure 12 shows an example of a Cortex XDR alert that successfully flagged FlutterShell activity by identifying browser hijacking activity similar to its predecessor, JSCoreRunner.

![A screenshot of Cortex XDR dashboard with a high-priority security alert titled "Staged Malware Activity." Below the title are three tabs: Overview, War Room, and Work Plan. The description notes activity similar to the "JSCoreRunner Browser Hijacker.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-530314-181830-12.png)Figure 12. Cortex XDR alert for FlutterShell activity flagged as similar to JSCoreRunner.

## Conclusion

The evolution from JSCoreRunner to FlutterShell represents a significant increase in technical depth for the attackers behind CL-CRI-1089. By transitioning to the Flutter framework and adopting a dynamic, WebView-based architecture, the attackers have effectively separated their malicious logic from the binary. This shift not only complicates static analysis, but allows the attackers to modify the malware's behavior on the fly, turning what appears to be a nuisance adware strain into a fully functional backdoor.

Furthermore, the scale of the distribution network, coupled with the verified shell entities used to bypass ad-network vetting, highlights the persistent danger of malvertising. The coordination of multiple shell entities, and the rapid development and delivery of new FlutterShell variants, indicates that this campaign is far from over. Up until late March, we continued to witness the distribution of FlutterBridge malware variants. As the attackers behind CL-CRI-1089 continue to refine their JavaScript-to-native bridge techniques, we expect to see this architecture deployed in future campaigns targeting both macOS and Windows environments.

### Palo Alto Networks Protection and Mitigation

#### Advanced WildFire

The [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire) machine-learning models and analysis techniques have been reviewed and updated in light of indicators associated with this malware.

#### Advanced URL Filtering and Advanced DNS Security

[Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) identify known domains and URLs associated with this activity as malicious.

#### Cortex XDR and XSIAM

Cortex XDR and XSIAM help to prevent the threats described in this article, by employing the Malware Prevention Engine. This approach combines several layers of protection, including Advanced WildFire, Behavioral Threat Protection and the Local Analysis module, to prevent both known and unknown malware from causing harm to endpoints. The mitigation methods implement malware protection based on the different operating systems – Windows, macOS and Linux.

#### How the Agentic Assistant Supported the Investigation

Cortex’s [AgentiX](https://docs-cortex.paloaltonetworks.com/r/Cortex-AgentiX/Cortex-AgentiX-Documentation/Get-Started-with-Cortex-AgentiX) Agentic Assistant streamlined the investigation by allowing the team to query the data using natural language, providing deeper context and insights, and suggesting clear recommendations on what should be done next. Figure 13 shows the AgentiX interface when finding processes that communicate with a malicious domain used in the FlutterBridge operation.

![A screenshot of AgentiX dashboard displaying communication paths. It details access over the last 90 days, with endpoints listed along with dates and times. Sections include 'Plan,' 'Endpoint Investigation,' and 'Summary.' The entries describe interactions between Agentic Assistant and paths. The summary highlights specific access instances.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-532404-181830-13.png)Figure 13. Finding processes that communicated with atsheisdomestic[.]org, using AgentiX.

## Indicators of Compromise

### SHA256 Hashes of Malicious Files From FlutterShell Activity (PodcastsLounge)

  * Hash: 021666417de8b9972c179783fe60d4c4ad2d93224e3a0f16137065c960b1b845
  * File name: PodcastsLounge.dmg
  * File description: Disk Image (DMG) installer for the malicious PodcastsLounge application
  * Hash: 363923500ce942bf1a953e8a4e943fbf1fb1b5ed6e5d247964c345b3ad5bfc34
  * File name: podcasts_lounge.app
  * Bundle ID: com.app.podcastsLounge
  * Developer ID: Yasar Sever (UBZDAAV97Y)
  * File description: Main application executable for PodcastsLounge
  * Hash: 8421c902364980e3d762ec6dbbe6b0f40577c27bd79b48c57d098328b2533109
  * File description: Dynamic library (dylib) associated with the PodcastsLounge application



### SHA256 Hashes of Malicious Files From FlutterShell Activity (PDF-Brain)

  * Hash: 644fc49fa1006a2a2acace694e5fb83753164e2617051ece6d9dc9ea32329e70
  * File name: PDF-Brain.dmg
  * File description: Disk Image (DMG) installer for the malicious PDF-Brain application.
  * Hash: 9053e8ddaecca1f960c041c944ca8799fc71dc86a4b50d2639ee4e0d2cb82f47
  * File name: PDF-Brain.app
  * Bundle ID: com.app.pdfBrain
  * Developer ID: Batuhan Dabag (FW9NHQ8922)
  * File description: Main application executable for PDF-Brain
  * Hash: b60074d1ea2008a581f432f2dee5f84f78668d9dd8e66f75d03c42dabd89bdea
  * File description: Dynamic library (dylib) associated with the PDF-Brain application.



### SHA256 Hashes of Malicious Files From FlutterShell Activity (PDF-Ninja)

  * Hash: 9425e8e39fa8a7212cdd07f0917cb3dfde38a90b87297de2c82a5850aff1e4de
  * File name: PDF-Ninja.dmg
  * File description: Disk Image (DMG) installer for the malicious PDF-Ninja application
  * Hash: 30448686ec900d5213d74f08f0d2b7924c5336a29445b2a434aba8d8b19d7530
  * File name: PDF-Ninja.app
  * Bundle ID: com.pdfninja.app
  * Developer ID: Yusuf Bal (B73CHZ24Y8)
  * File description: Main application executable for PDF-Ninja
  * Hash: 48047c34bbd57fe1e24bc538bc2ce9e0ac4c4eb48d3b0c195b414f0379dc0745
  * File description: Dynamic library (dylib) associated with the PDF-Ninja application



### Infrastructure and C2 Traffic

  * URL: hxxps[:]//atsheisdomestic[.]org/update-thanks.html
  * Domain: atsheisdomestic[.]org
  * Description: PodcastsLounge C2
  * URL: hxxps[:]//etoftheappyrince[.]org/update-delay
  * Domain: etoftheappyrince[.]org
  * Description: PDF-Brain C2
  * URL: hxxps[:]//healightejustb[.]org/checkupdateTO.js
  * Domain: healightejustb[.]org
  * Description: PDF-Ninja C2
  * Domain: sinterfumesco[.]com
  * Description: Adware site



### Actor-Related Websites

  * Domain: ads-parkpro[.]com
  * Description: Website previously associated with AdsParkPro LTD
  * Domain: adsparkpro[.]top
  * Description: Website previously associated with AdsParkPro LTD
  * Domain: adsparkpro[.]net
  * Description: Website previously associated with AdsParkPro LTD
  * Domain: softwe[.]art
  * Description: Website associated with SOFT WE ART



## Additional Resources

  * [RecipeLister: A Recipe for Disaster](https://www.bluevoyant.com/blog/recipelister-a-recipe-for-disaster) – BlueVoyant
  * [Dart Client-Optimized Language](https://dart.dev/) – dart.dev
  * [Flutter Open-Source Framework](https://flutter.dev/) – flutter.dev
  * [B(l)utter Flutter Mobile Application Reverse Engineering Tool](https://github.com/worawit/blutter) – GitHub
  * [What is Malvertising](https://www.imperva.com/learn/application-security/malvertising/) – Imperva
  * [Widespread Installation of Calendaromatic Adware Includes Homoglyph Channel](https://www.kroll.com/en/publications/cyber/widespread-installation-calendaromatic-adware-homoglyph-channel) – Kroll
  * [Browser Hijackers](https://www.malwarebytes.com/blog/threats/browser-hijacker) – Malwarebytes
  * [New Malware JSCoreRunner is Spreading via Fake PDF converters](https://moonlock.com/jscorerunner-fake-pdf-converters) – Moonlock Labs
  * [Mosyle Identifies New Mac Malware That Evades Detection Through Fake PDF Conversion Tool](https://9to5mac.com/2025/08/27/mosyle-identifies-new-mac-malware-that-evades-detection-through-fake-pdf-conversion-tool/) – Mosyle
  * [Intelligence Insights: October 2025](https://redcanary.com/blog/threat-intelligence/intelligence-insights-october-2025/) – Red Canary
  * [When Your Calendar Wants to Steal Your Tokens: A Look at Calendaromatic](https://medium.com/@rabbit_knight/when-your-calendar-wants-to-steal-your-tokens-a-look-at-calendaromatic-81c15bb7ed9e) – Rabbit Knight, Medium
  * [Sparkle Project](https://sparkle-project.org/) – sparkle-project.org



## Appendix A: Analysis of Additional FlutterShell Features

### Loading the WebView

FlutterShell initiates the WebView and loads the attackers’ website in the following cases:

  * **Initial execution:** Automatically, following a calculated delay received dynamically from the C2.
  * **User Interaction:** When the targeted user clicks the About or Update buttons in the application settings.



Upon initial execution, FlutterShell waits for a specific duration before contacting the attacker-controlled website. This delay is non-deterministic and is calculated during the application's startup routine:

  1. Immediately after launch, FlutterShell sends an HTTP GET request to [attacker_domain]/api/update-delay to fetch the delay duration in seconds.
  2. If this endpoint is unreachable, the malware defaults to a 600 second (10 minute) delay. If the server responds, but the delay field is null, it defaults to a 1200 second (20 minute) delay.
  3. Once the timer expires, FlutterShell forces the application to the foreground and presents the webpage [attacker_domain]/update-thanks.html.



This calculated delay suggests a deliberate strategy to evade automated sandbox environments, which typically time out within a few minutes. Simultaneously, it builds user trust by maintaining a period of “normal” application behavior before the malicious window appears.

If the user clicks the About or Update buttons in the application settings, FlutterShell loads the attackers’ main website page or the update-thanks.html page, respectively. In both scenarios, the loaded webpages contain JavaScript code that executes immediately upon loading.

### FlutterShell’s Update Mechanism via the Sparkle Framework

The FlutterShell backdoor uses the [Sparkle](https://sparkle-project.org/) software update framework for macOS applications in its update mechanism. However, it significantly deviates from the standard Sparkle protocol, to avoid detection.

In a legitimate implementation, once Sparkle finishes downloading an update to the cache, it triggers a user interface (UI) prompt, such as “A new version is available. Install and Relaunch?”. The update process halts here until the user manually clicks the button to approve the restart. To bypass this user interaction, FlutterShell interrupts the flow the moment the download completes.

Our analysis of this sequence reveals the following flow:

  1. **Callback reception** : The malware listens for the update completion signal in the function SparkleUpdateService:_handleMethodCall() marked as the string onUpdateCycleFinished from the native macOS layer.
  2. **Installation verification** : If the update completed without errors, the code checks for the existence of the Sparkle installation directory: $HOME/Library/Caches/com.app.[appname]/org.sparkle-project.Sparkle/Installation/.
  3. **Manual execution** : Rather than waiting for the user to authorize the install, the malware programmatically executes the open command on the staged app bundle found in the cache.
  4. **Forced termination:** It immediately executes dart:io exit(), killing the old running process instantly.



This sequence effectively “swaps”" the malware version in real time, without ever showing a dialog box. This ensures that the updated malware begins running without any UI interaction, allowing the attackers to upgrade the backdoor's capabilities silently.

### Supported FlutterShell Commands Analysis

FlutterShell’s built-in commands provide full backdoor capabilities, allowing the attackers to execute shell commands and manipulate files on the system. Table 2 lists the commands and capabilities of FlutterShell found collectively within the three identified variants — PodcastsLounge, PDF-Brain and PDF-Ninja.

**Category** | **Commands and Features** | **Description**  
---|---|---  
**Variant** | PodcastsLounge | PDF-Brain | PDF-Ninja |   
**Execution** | exec_sync | pdf_sync | renderPDF | Executes arbitrary shell commands with current user permissions  
**Filesystem** | 

  * read_file
  * write_file 
  * read_dir 
  * exists
  * get_home_dir

| 

  * read_pdf
  * write_pdf 
  * read_pdf_dir 
  * pdf_exists
  * get_pdf_dir

| 

  * Read files 
  * Write files 
  * Get directory structure 

  
**Harvesting** | get_env | Extracts environment variables. These may contain high-value assets like plaintext API keys for secondary access.  
**UI Manipulation** | close_webview, setSize | Resize the application’s windows, likely to reduce user suspicion.  
  
Table 2. An example of FlutterShell’s backdoor capabilities.

We also saw that some variants of FlutterShell have the com.apple.security.files.downloads.read-write macOS entitlement, which gives the malware the capability to read and write to files in the user’s Downloads directory.

## Appendix B: Technical Similarities Between JSCoreRunner and FlutterShell

The architectural fingerprints of both JSCoreRunner and FlutterShell malware families are nearly indistinguishable. Both rely on a specialized JavaScript-to-native bridge, using JavaScript as a high-level conductor to trigger low-level system operations.

The most compelling evidence of a shared lineage is the backdoor primitives. We found a set of six identical core commands embedded in both JSCoreRunner and FlutterShell, as Table 3 shows.

**Capability** | **FlutterShell** | **JSCoreRunner**  
---|---|---  
**Check File/Dir Existence** | exists/existsSync | _fsExistsSync  
**Execute Command** | exec_sync/pdf_sync | _execSync  
**File Reading** | read_file | _fsReadFileSync  
**File Writing** | write_file | _fsWriteFileSync  
**Dir Enumeration** | read_dir | _fsReaddirSync  
**Get Home Directory** | get_home_dir | _osHomedir  
  
Table 3. Function name comparison between JSCoreRunner and FlutterShell.

Operationally, the campaign objectives remain consistent. Both have been observed primarily as browser hijackers, with a specific focus on compromising Google Chrome installations to inject ads or scrape sensitive session data.

While the fundamental architecture is the same, FlutterShell represents a significant tactical evolution over JSCoreRunner. The primary shift lies in their different payload delivery methods — while JSCoreRunner’s logic is embedded statically in the binary, FlutterShell’s logic is received dynamically from the C2 server at runtime.

This shift has significant implications for detection and response. Dynamic delivery means attackers can decouple the binary from its logic by updating their logic without needing to recompile the application. In addition, dynamic content delivery allows the attacker to use geofencing and avoid certain regions and entities to download the malware’s payload, thus hindering analysis even more.

Back to top

### Tags

  * [CL-CRI-1089](https://unit42.paloaltonetworks.com/tag/cl-cri-1089/ "CL-CRI-1089")
  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Malvertising](https://unit42.paloaltonetworks.com/tag/malvertising/ "malvertising")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: 2026 World Cup: Discussing The World’s Biggest Game’s Attack Surface ](https://unit42.paloaltonetworks.com/fifa-world-cup-attack-surface/ "2026 World Cup: Discussing The World’s Biggest Game’s Attack Surface")

### Table of Contents

  *   * Executive Summary
  * Campaign Background
  * Overview of the FlutterShell Malware
    * FlutterShell Deployment and Masquerading
    * FlutterShell Technical Analysis
      * FlutterShell’s Malicious WebView Architecture
      * JavaScript Bridge Injection Technique
    * Variants and Evolution of FlutterShell
      * FlutterShell’s Adware Payload
  * CL-CRI-1089: Campaign Infrastructure and Evolving Tradecraft
    * CL-CRI-1089 Ads Delivery Network
      * Verified Shell Entities
      * Adversary Tradecraft and OpSec Failures
    * Connecting the Dots Behind CL-CRI-1089 Campaigns
      * The CL-CRI-1089 Connection
      * The JSCoreRunner Connection
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
      * Advanced WildFire
      * Advanced URL Filtering and Advanced DNS Security
      * Cortex XDR and XSIAM
      * How the Agentic Assistant Supported the Investigation
  * Indicators of Compromise
    * SHA256 Hashes of Malicious Files From FlutterShell Activity (PodcastsLounge)
    * SHA256 Hashes of Malicious Files From FlutterShell Activity (PDF-Brain)
    * SHA256 Hashes of Malicious Files From FlutterShell Activity (PDF-Ninja)
    * Infrastructure and C2 Traffic
    * Actor-Related Websites
  * Additional Resources
  * Appendix A: Analysis of Additional FlutterShell Features
    * Loading the WebView
    * FlutterShell’s Update Mechanism via the Sparkle Framework
    * Supported FlutterShell Commands Analysis
  * Appendix B: Technical Similarities Between JSCoreRunner and FlutterShell



### Related Articles

  * [ Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "article - table of contents")
  * [ Vidar Stealer Unmasked: Code Signing Abuse, Go Loaders and File Inflation ](https://unit42.paloaltonetworks.com/vidar-stealer-xmrig-miner-campaign-analysis/ "article - table of contents")
  * [ Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector ](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/flutterbridge-new-fluttershell-backdoor/)