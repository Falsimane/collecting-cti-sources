# Gremlin Stealer's Evolved Tactics: Hiding in Plain Sight With Resource Files

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/
- **Date :** 2026-05-15

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Gremlin Stealer's Evolved Tactics: Hiding in Plain Sight With Resource Files

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 7 min read 

Related Products

[![Advanced DNS Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced DNS Security](https://unit42.paloaltonetworks.com/product-category/advanced-dns-security/ "Advanced DNS Security")[![Advanced Threat Prevention icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced Threat Prevention](https://unit42.paloaltonetworks.com/product-category/advanced-threat-prevention/ "Advanced Threat Prevention")[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Advanced WildFire icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced WildFire](https://unit42.paloaltonetworks.com/product-category/advanced-wildfire/ "Advanced WildFire")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Pranay Kumar Chhaparwal](https://unit42.paloaltonetworks.com/author/pranay-kumar-chhaparwal/)
    * [Mark Lim](https://unit42.paloaltonetworks.com/author/mark-lim/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:May 15, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [API](https://unit42.paloaltonetworks.com/tag/api/)
    * [Cryptocurrency](https://unit42.paloaltonetworks.com/tag/cryptocurrency/)
    * [Gremlin stealer](https://unit42.paloaltonetworks.com/tag/gremlin-stealer/)
    * [Obfuscation](https://unit42.paloaltonetworks.com/tag/obfuscation/)
    * [Payload](https://unit42.paloaltonetworks.com/tag/payload/)
    * [Telegram](https://unit42.paloaltonetworks.com/tag/telegram/)
    * [VirusTotal](https://unit42.paloaltonetworks.com/tag/virustotal/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/?pdf=download&lg=en&_wpnonce=252a1929a6 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/?pdf=print&lg=en&_wpnonce=252a1929a6 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Gremlin%20Stealer's%20Evolved%20Tactics:%20Hiding%20in%20Plain%20Sight%20With%20Resource%20Files&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgremlin-stealer-evolution%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgremlin-stealer-evolution%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgremlin-stealer-evolution%2F&title=Gremlin%20Stealer's%20Evolved%20Tactics:%20Hiding%20in%20Plain%20Sight%20With%20Resource%20Files "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgremlin-stealer-evolution%2F&text=Gremlin%20Stealer's%20Evolved%20Tactics:%20Hiding%20in%20Plain%20Sight%20With%20Resource%20Files "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgremlin-stealer-evolution%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Gremlin%20Stealer's%20Evolved%20Tactics:%20Hiding%20in%20Plain%20Sight%20With%20Resource%20Files%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgremlin-stealer-evolution%2F "Share in Mastodon")



## Executive Summary

This article examines new obfuscation techniques the Gremlin stealer malware uses to conceal malicious payloads within embedded resources. We analyze a variant protected by a sophisticated commercial packing utility that employs instruction virtualization, transforming the original code into a custom, non-standard bytecode executed by a private virtual machine.

[Gremlin stealer](https://unit42.paloaltonetworks.com/new-malware-gremlin-stealer-for-sale-on-telegram/) siphons sensitive information from compromised systems and exfiltrates it to attacker‑controlled servers for potential publication or sale. It targets web browsers, system clipboard and local storage to exfiltrate sensitive information like:

  * Payment card details
  * Browser cookies
  * Session tokens
  * Cryptocurrency wallet data
  * FTP and VPN credentials



This threat has rapidly evolved, incorporating new anti-analysis safeguards into recent builds.

Palo Alto Networks customers are better protected from Gremlin Stealer through our [Network Security](https://www.paloaltonetworks.com/network-security) solutions and [Cortex](https://www.paloaltonetworks.com/cortex) line of products, including:

  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM)
  * [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire)
  * [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration)
  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering/administration) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Infostealer](https://unit42.paloaltonetworks.com/tag/Infostealer), [Telegram](https://unit42.paloaltonetworks.com/tag/telegram/), [Cryptocurrency](https://unit42.paloaltonetworks.com/tag/cryptocurrency/)**  
---|---  
  
## New Gremlin Site for Publishing Data

Using data from our internal threat intelligence, we identified a new Gremlin stealer variant. This variant exfiltrates stolen data to a newly deployed site at hxxp[:]194.87.92[.]109 as shown in Figure 1.

![Screenshot of a computer screen displaying a login interface for "GREMLIN" on a dark background. It includes input fields for username and password, with a prominent green "Login" button. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-328655-180614-1.png)Figure 1. New Gremlin site.

At the time of discovery, VirusTotal showed zero detection for this new Gremlin site hxxp[:]194.87.92[.]109, its associated URLs or any retrieved artifacts. There were no block list entries, community reports or malicious categorizations as shown in Figure 2.

![Screenshot of a VirusTotal webpage analyzing a URL. The analysis shows 0 out of 71 security vendors flagged the URL as malicious. Status is 200 with the content type listed. Tabs for details, relations, content, telemetry, and community are visible.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-330539-180614-2.png)Figure 2. Gremlin Stealer’s new site detection on VirusTotal.

After data theft, the malware bundles harvested artifacts into a ZIP archive, including:

  * Browser cookies
  * Session tokens
  * Clipboard contents
  * Cryptocurrency wallet data
  * FTP and VPN credentials



The malware names the file using the victim’s public IP address to identify the source, and then uploads it to the attacker-controlled site, as shown in Figure 3.

![Screenshot of a dashboard interface of the "Gremlin" application displaying statistics such as the number of online devices \(11\), data usage \(0.83 MB\), and uptime \(12:40:52\). The interface includes sections with buttons labeled in Russian for each device, showing options to "Online" and "Delete.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-332412-180614-3.png)Figure 3. Gremlin site published data.

## Technical Analysis

In this section, we present a comparative analysis of older and newer Gremlin stealer variants, highlighting the key changes and describing our process for extracting the final-stage payloads.

### Hiding Payload in Resource

The latest iteration of the Gremlin stealer has an increased focus on stealth, specifically designed to evade static analysis tools. In this version, the malware authors have shifted the malicious payload into the .NET Resource section, masking it with XOR encoding to bypass signature-based detection and heuristic scanning.

Figure 4 shows how the resource section appears as an opaque block of data, hiding strings and API calls that would otherwise trigger alerts.

![Screenshot of a hex editor displaying hexadecimal code on the right pane and a directory tree on the left, including folders like "Version Info" and "Configuration Files." The displayed code includes both hexadecimal and ASCII representations.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-335072-180614-4.png)Figure 4. Resource section.

By applying a single-byte XOR decryption routine, we recovered the plain-text configuration. Figure 5 shows that this reveals the hard-coded command-and-control (C2) URLs and exfiltration paths.

![Screenshot of a text document showing a process for XOR decryption and URL extraction. The text notes successful URL findings with keys 20, 31, and 49. The process concludes with a message stating "Decryption and URL extraction complete".](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-337023-180614-5.png)Figure 5. XOR decryption on resource section.

Gremlin stealer uses the resource section to mirror the tactics of several high-profile malware families that frequently use this area for payload obfuscation, including:

  * [Agent Tesla](https://www.stormshield.com/news/agent-tesla-campaign/)
  * [GuLoader](https://www.crowdstrike.com/en-us/blog/guloader-malware-analysis/)
  * [LokiBot](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/)
  * [Quasar RAT](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/)



#### Comparison with Older Version

Comparing past and present versions reveals a clear evolution in Gremlin stealer’s anti-analysis techniques. Legacy samples (shown in Figure 6) lacked obfuscation, leaving function exports and internal symbols intact.

![Two side-by-side screenshots of code editors. The left screenshot displays an older version with a list of entities like "AesCrypto," "Armory," "Asset," and others under the namespace "SHAPP." The right screenshot shows the latest version, also under "SHAPP," with a longer list including additional entries or modified ones. Both have red outlines highlighting the lists.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/Figure-6-771x440.png)Figure 6. Gremlin older version vs. latest version.

The current iteration implements a staged loading mechanism. Each critical function is decrypted and mapped into memory from the .NET resource section only when needed. This method forces analysts to perform dynamic debugging to observe any meaningful program behavior.

#### Key Enhancements in the Latest Variant

Gremlin stealer’s evolution from a basic credential harvester to a modular toolkit is evident in several key architectural upgrades:

  * **Expanded target scope** : Gremlin stealer includes a dedicated Discord token extraction module, which signifies a pivot toward targeting digital identity and social engineering.
  * **Active financial fraud** : The latest variant shifts from passive data theft to active financial interference. This crypto clipper functionality continuously monitors the system clipboard for strings matching cryptocurrency wallet patterns. When it detects a match, the malware replaces the victim's address with the attacker’s wallet in real time, diverting funds during transactions.
  * **Advanced persistence** : The WebSocket-based session hijacking module represents its most significant technical upgrade. This allows Gremlin stealer to hijack active, live browser sessions and bypass modern cookie protections by requesting the data directly from the running browser process.



### **Sample Packed Using a Complex Commercial Packing Utility**

We uncovered an iteration of Gremlin stealer (SHA256 2172dae9a5a695e00e0e4609e7db0207d8566d225f7e815fada246ae995c0f9b) packed using a packing utility, as shown in Figure 7 below.

![Screenshot of Exeinfo PE software window displaying file information. The header shows version 0.0.9.0 by A.S.L. The main section includes details about a file named '217.exe', such as entry point, file offset, and subsystem. A section below highlights "\(PACKED mode\)". Various buttons and icons are visible on the right](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-342240-180614-7.png)Figure 7. Packed Gremlin variant.

Let’s discuss the obfuscation and anti-analysis techniques this variant uses.

#### Code Obfuscation and Anti Analysis

##### Identifier Renaming (The “No-Labels” Technique)

Imagine trying to cook in a kitchen where every can, box and spice jar has its label replaced with a random, short name like a, b, c, hf or ze. The malware authors applied this technique to the variant’s code.

  * What it is: They replaced every meaningful name for a class, method or variable with a meaningless one.
  * Why it's effective: It removes all context. A method originally named StealPasswordsFromChrome might become a(). A variable named decryptionKey might become b. This forces an analyst to manually trace every single function call to figure out its purpose, which is incredibly time-consuming.
  * Example: In the file hf.cs, the main orchestrator class is named hf, and its primary methods are a, b and c. In bb.cs, the class for stealing browser data is BrowserCredentialStealer, but in the original obfuscated code, it was just bb.



##### String Encryption (The “Secret Decoder Ring” Technique)

In this technique, malware authors made readable strings appear as gibberish. Instead of writing a word like password or a URL like hxxps://api[.]telegram[.]org directly in the code, the malware stores them encrypted.

  * What it is: All important strings are hidden. The code only contains numbers that act as a key to a secret decoder function. When the program needs a string, it passes these numbers to the decoder, which then returns the real string.
  * The decoder ring function: The secret decoder is the method _003CModule_003E.c(int, int, int). 
    * It takes three integers as input
    * It uses these numbers to calculate an offset and a length
    * It opens an embedded resource file (named resource in the .csproj file) which contains all the encrypted strings
    * It seeks the calculated offset, reads the specified number of encrypted bytes and uses the third integer as a key to decrypt them
    * It returns the final, readable string
  * Why it's effective: It completely hides the malware's intentions from static analysis. Analysts cannot simply search the code for suspicious keywords like Telegram, wallet.dat or api.ipify[.]org because they don't exist in plain text. Instead, analysts must either run the program in a debugger to see what strings are produced or reverse-engineer the decoder function.
  * Example: A line like this from the original code:



csharp

 _// This is what the obfuscated code looks like_

string url = global::_003CModule_003E.c(18829, 2178, 23);

When executed, the c() function would run its decoding operation, and the URL variable would then contain: csharp

 _// This is the real value at runtime_

string url = "http://api.ipify.org/?format=json";

##### Control-Flow Obfuscation (The “Maze of Useless Roads” Technique)

This technique makes the code's logic intentionally confusing, like turning a straight road into a maze of dead ends and pointless loops that all eventually lead to the same place.

  * What it is: The decompiler output is filled with complex and nonsensical if-else statements, goto jumps and mathematical operations that don't actually affect the outcome. These are designed to confuse both human analysts and automated analysis tools.
  * Why it's effective: It breaks the logical flow that a person would expect to see. It makes it hard to determine which path the code will _actually_ take, even though in many cases, there's only one real path. This significantly increases the time and effort required for reverse engineering.
  * Example: There are many switch statements and goto labels (e.g., IL_00c8, IL_0138) that create a tangled web of execution, even though the underlying logic is a simple sequence of await Task.Run(...).



## Conclusion

While the core architecture and exfiltration methods via private web panels or the Telegram Bot API remain consistent, this latest variant of Gremlin stealer represents an evolution into a more complex threat. By transitioning from a simple data exfiltration tool to a more advanced modular stealer, Gremlin now targets Chromium-based browsers. It uses memory-resident techniques to hijack active session tokens and sensitive data directly from running processes, rather than relying solely on static database files.

This threat’s scope has broadened, as evidenced by a dedicated Discord token stealer. This module scans multiple paths and uses regex validation to compromise modern communication platforms.

The malware’s author has also added a clipboard hijacker. This new monetization feature enables persistent financial fraud. It continuously monitors the clipboard, replacing cryptocurrency wallet addresses with attacker-controlled ones.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

  * The [Advanced WildFire](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) machine-learning models and analysis techniques have been reviewed and updated in light of the IoCs shared in this research.
  * [Advanced URL Filtering](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) and [Advanced DNS Security](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) identify known domains and URLs associated with this activity as malicious.
  * [Advanced Threat Prevention](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) has an inbuilt machine learning-based detection that can detect exploits in real time.
  * [Cortex XDR](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) and [XSIAM](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) are designed to: 
    * Prevent the execution of known malicious malware, and also prevent the execution of unknown malware using Behavioral Threat Protection and machine learning based on the Local Analysis module.
    * Protect against credential gathering tools and techniques using the new Credential Gathering Protection available from Cortex XDR 3.4.
    * Detect post-exploit activity, including credential-based attacks, with behavioral analytics, through Cortex XDR Pro.



If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 00080005045107



## Indicators of Compromise

SHA256 hashes of the Gremlin stealer samples analyzed for this article:

  * 2172dae9a5a695e00e0e4609e7db0207d8566d225f7e815fada246ae995c0f9b
  * 9aab30a3190301016c79f8a7f8edf45ec088ceecad39926cfcf3418145f3d614
  * 971198ff86aeb42739ba9381923d0bc6f847a91553ec57ea6bae5becf80f8759
  * ab0fa760bd037a95c4dee431e649e0db860f7cdad6428895b9a399b6991bf3cd
  * f76ba1a4650d8cafb6d3ff071688c5db6fd37e165050f03cece693826f51d346
  * a9f529a5cbc1f3ee80f785b22e0c472953e6cb226952218aecc7ab07ca328abd
  * 691896c7be87e47f3e9ae914d76caaf026aaad0a1034e9f396c2354245215dc3
  * 281b970f281dbea3c0e8cfc68b2e9939b253e5d3de52265b454d8f0f578768a2
  * 9fda1ddb1acf8dd3685ec31b0b07110855832e3bed28a0f3b81c57fe7fe3ac20
  * d11938f14499de03d6a02b5e158782afd903460576e9227e0a15d960a2e9c02c
  * 1bd0a200528c82c6488b4f48dd6dbc818d48782a2e25ccd22781c5718c3f62f5



URLs

  * hxxp[:]194.87.92[.]109/i.php



## Additional Resources

  * [Gremlin Stealer: New Stealer on Sale in Underground Forum](https://blog.talosintelligence.com/a-deep-dive-into-lokibot-infection-chain/) — Unit 42, Palo Alto Networks



Back to top

### Tags

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [Cryptocurrency](https://unit42.paloaltonetworks.com/tag/cryptocurrency/ "Cryptocurrency")
  * [Gremlin stealer](https://unit42.paloaltonetworks.com/tag/gremlin-stealer/ "gremlin stealer")
  * [Obfuscation](https://unit42.paloaltonetworks.com/tag/obfuscation/ "obfuscation")
  * [Payload](https://unit42.paloaltonetworks.com/tag/payload/ "payload")
  * [Telegram](https://unit42.paloaltonetworks.com/tag/telegram/ "Telegram")
  * [VirusTotal](https://unit42.paloaltonetworks.com/tag/virustotal/ "VirusTotal")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Inside AD CS Escalation: Unpacking Advanced Misuse Techniques and Tools ](https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/ "Inside AD CS Escalation: Unpacking Advanced Misuse Techniques and Tools")

### Table of Contents

  *   * Executive Summary
  * New Gremlin Site for Publishing Data
  * Technical Analysis
    * Hiding Payload in Resource
      * Comparison with Older Version
      * Key Enhancements in the Latest Variant
    * Sample Packed Using a Complex Commercial Packing Utility
      * Code Obfuscation and Anti Analysis
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Indicators of Compromise
  * Additional Resources



### Related Articles

  * [ The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "article - table of contents")
  * [ Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "article - table of contents")
  * [ Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "article - table of contents")



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
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")
  * [Unit 42](https://unit42.paloaltonetworks.com/tag/unit-42/ "Unit 42")



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
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")
  * [Unit 42](https://unit42.paloaltonetworks.com/tag/unit-42/ "Unit 42")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/)