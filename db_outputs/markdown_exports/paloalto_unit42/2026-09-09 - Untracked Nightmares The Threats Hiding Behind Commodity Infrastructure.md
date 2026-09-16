# Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/
- **Date :** 2026-09-09

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 18 min read 

Related Products

[![Advanced DNS Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced DNS Security](https://unit42.paloaltonetworks.com/product-category/advanced-dns-security/ "Advanced DNS Security")[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Advanced WildFire icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced WildFire](https://unit42.paloaltonetworks.com/product-category/advanced-wildfire/ "Advanced WildFire")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Rem Dudas](https://unit42.paloaltonetworks.com/author/rem-dudas/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:September 9, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/)
    * [C2](https://unit42.paloaltonetworks.com/tag/c2/)
    * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/)
    * [Docro Hijacker](https://unit42.paloaltonetworks.com/tag/docro-hijacker/)
    * [Pay-per-install](https://unit42.paloaltonetworks.com/tag/pay-per-install/)
    * [Payload](https://unit42.paloaltonetworks.com/tag/payload/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Untracked%20Nightmares:%20The%20Threats%20Hiding%20Behind%20Commodity%20Infrastructure&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fppi-network-malware-campaign-analysis%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fppi-network-malware-campaign-analysis%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fppi-network-malware-campaign-analysis%2F&title=Untracked%20Nightmares:%20The%20Threats%20Hiding%20Behind%20Commodity%20Infrastructure "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fppi-network-malware-campaign-analysis%2F&text=Untracked%20Nightmares:%20The%20Threats%20Hiding%20Behind%20Commodity%20Infrastructure "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fppi-network-malware-campaign-analysis%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Untracked%20Nightmares:%20The%20Threats%20Hiding%20Behind%20Commodity%20Infrastructure%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fppi-network-malware-campaign-analysis%2F "Share in Mastodon")



## Executive Summary

A recent Unit 42 investigation into seemingly low-priority enterprise infections demonstrates how the most effective camouflage in cybercrime is not necessarily in the use of sophisticated techniques, but in how unremarkable the threat appears. The activities that we investigated would typically not require escalation or further inquiry. But upon closer inspection, we discovered a massive cybercrime campaign largely targeting young gamers. Tracked as CL-CRI-1171, in accordance with [Unit 42’s attribution framework](https://unit42.paloaltonetworks.com/unit-42-attribution-framework/), the group behind this cluster has operated under the radar for at least two years, distributing an indeterminate number of payloads.

The group behind CL-CRI-1171 provides an infection service for other threat actors who want to spread their malware indiscriminately. This pay-per-install (PPI) marketplace drove hundreds of infections through YouTube channels and a parallel search engine optimization (SEO)-poisoning funnel, all using the same custom loader.

We observed at least eleven YouTube channels that had hundreds of thousands of followers. We notified YouTube of these channels, which it promptly terminated.

These channels were actively interacting with viewers to promote gaming content laced with links to download malware. Content in the channels included advice on improving frame rates, fixing game crashes and adjusting settings on game platforms. Although the videos provided real content for gamers, they also served as the delivery vehicle for infection, prompting viewers to download malicious tools.

The SEO funnel targeted a more professional audience, promoting trojanized software that resulted in malware deployment on corporate endpoints, including critical infrastructure and even government entities. We identified three independent payloads delivered by the same loader between July 2025 and April 2026: two never publicly reported, Docro Hijacker and ARKTunnel, and a new variant of a previously unnamed backdoor, which we dubbed Insomnia remote access Trojan (RAT).

These infections represent only a small sample of a much larger deployment campaign. We have identified more than 10,000 distinct loader samples, each capable of delivering unique payload combinations.

We provide an overview of the cybercrime cluster and its loader infrastructure, and a technical analysis of three recently delivered malware strains.

Palo Alto Networks customers are better protected from the threats discussed in this article through the following:

  * [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire)
  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security)
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[SEO Poisoning](https://unit42.paloaltonetworks.com/tag/seo-poisoning/), [Browser Hijacking](https://unit42.paloaltonetworks.com/tag/browser-hijacking/), [RATs](https://unit42.paloaltonetworks.com/tag/remote-access-trojan/)**  
---|---  
  
## Overview of CL-CRI-1171 Activity

Our discovery of two separate infections delivering three entirely distinct malware families revealed one common denominator: a shared loader. By tracing this infrastructure, we mapped the broader activity of CL-CRI-1171, ultimately tying the cluster to a PPI marketplace responsible for delivering countless payloads over the last two years.

This operation uses at least two funneling mechanisms to route traffic to the malware landing pages: a network of YouTube channels and [SEO poisoning](https://attack.mitre.org/techniques/T1608/006/). The shared infrastructure between the YouTube and SEO funnels, consistent use of the same loader and a rotational domain pattern observed over an eight-month window all pointed to a single sustained operation, which we track as CL-CRI-1171.

### The PPI Ecosystem: An Infection Marketplace

PPI networks operate as underground marketplaces. An operator compromises machines and auctions access to multiple buyers, each buyer deploying their own independent payloads through the same dropper. The result is a single infection that conceals multiple payloads from unrelated threat actors on the same endpoint, each with its own C2 infrastructure and objectives. Because the loader is designed to be disposable and generic, it rarely attracts the scrutiny needed to uncover its subsequent payloads.

### Tracking CL-CRI-1171: The PPI Operation Behind the Payloads

The investigation began with two identical and seemingly routine infections at separate organizations. Both events involved trojanized software downloads — one a Bluetooth driver, the other [WinDirStat](https://en.wikipedia.org/wiki/WinDirStat) — and both affected machines executed an identical post-exploitation chain. The loader was unnamed, untracked and generic enough to be dismissed as commodity adware.

But our discovery of a shared payload chain raised a question. How were two unrelated organizations infected by the same unnamed loader delivering the same set of payloads, just one week apart?

Pivoting on the loader's C2 infrastructure revealed a sprawling network of rotational domains — over 200 unique hostnames following a distinctive two-word compound naming pattern (including bubbleslip, churchpail, dinosaursjam), rotating across .xyz, .cfd, .space and .info top-level domains (TLDs).

### Unpacking the Delivery Infrastructure

The payloads delivered through CL-CRI-1171's infrastructure are not fixed, enabling the simultaneous delivery of unrelated malware families. In April 2026, two incidents initiated this investigation. They shared a single loader that delivered three separate malware families: Insomnia RAT, ARKTunnel and Docro Hijacker. A subsequent infection, observed in June 2026, delivered two entirely different payloads: GCleaner and Socks5Systemz.

Figure 1 illustrates the structure of the operational architecture and the observed rotational malware bundles.

![A diagram illustrating CL-CRI-1171 infrastructure with connections from YouTube and SEO funnels, listing several attack vectors.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-540459-186615-1.png)Figure 1. Illustration of CL-CRI-1171 infrastructure.

Our in-depth analysis explores three operations that were spotted in two intrusion sets during April 2026. By examining the campaign’s trackers, we found that these operation payloads were in rotation from July 2025 to April 2026. This discovery provides a valuable snapshot of the group’s deployment capabilities and the variety of payloads they have been entrusted to deliver.

Although the observed rotation appears to be highly structured, the discovery of over 10,000 unique OfferLoader samples points to a much larger distribution pipeline. It is very likely that the loader has delivered numerous other malware families.

The SEO poisoning path was the first delivery channel we identified. Unsuspecting users searching for legitimate software landed on file-hosting lure pages that displayed a fake virus-scan animation before delivering the trojanized archive via a chain of redirectors into the PPI gate.

A reconstructed example download page from the SEO poisoning funnel is shown in Figure 2.

![A screenshot of a webpage displaying a file download section. There’s a large green button labeled "Download File" and an option to "Check viruses." The footer includes links to hosting details and mentions of partner sites.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-543539-186615-2.png)Figure 2. Reconstruction of the trojanized WinDirStat download page.

Analysis of the gate's tracker URLs revealed a critical detail. Each URL contained a click_id parameter: a Base64-encoded fingerprint containing the victim's operating system (OS), browser, the referring domain, the exact search keyword that led them to the lure and their public IP address, as Table 1 shows.

**Operating System** | **Browser** | **Referring SEO Domain** | **Search Keyword** | **Victim IP**  
---|---|---|---|---  
Windows_10 | Chrome | atthelake[.]info | hwidspoofer | 5.xxx.xx.xxx  
Windows_10 | Chrome | atthelake[.]info | combatwarriorsGit | 2.xx.xxx.xx  
  
Table 1. Example of a deobfuscated click_id.

The gate uses this fingerprint to decide who receives the payload: a valid, fresh click_id forwards the visitor to the malware/loader download. This is an evasion tactic used to ensure that only real targets are infected, and to protect the actor’s infrastructure: scanners, crawlers or analysts receive a decoy clone of the legitimate WinRAR download page or broken links. This is why the campaign has almost no public footprint despite being highly active: automated URL scanners rarely pass the gate.

Decoding hundreds of these fingerprints, with the assistance of AI, exposed the full names of YouTube video titles and their associated channels. Alongside search keywords for cracked software and game cheats, the q= field – which tracks which search query led to the infection – contained strings like "CS2 Potato Graphics Settings - Maximum FPS Boost for Low-End PC (2026 Guide) - Velvox."

### The YouTube Funnel

Searching for titles derived from the fingerprints led us to uncover a chain of gaming optimization YouTube channels. Their content included tips on boosting frames per second (FPS), fixing game crashes and tweaking settings on popular game platforms. While the videos provided authentic, engaging content for young gamers, they ultimately served as an infection delivery vehicle, prompting viewers to download a malicious “tool” or “optimization pack” via links in the description, as Figure 3 shows.

![A screenshot of a YouTube video titled by ADEX with 18.7K subscribers. The video has 168 views as of June 22, 2026. Hashtags include #CPUBottleneck and #LowGPUUsage. Two links are provided: one short link and a GearUp Booster product link.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-546830-186615-3.png)Figure 3. A YouTube video from the ADEX channel directing viewers to a download link.

Those links pass through intermediary sites, such as Blogspot, which contain social-engineering instructions that lead the victim to the same PPI gate infrastructure serving the SEO path. An example blog page is shown in Figure 4.

![A screenshot of a website page showing two featured articles. The first article discusses fixing high ping and packet loss for improved downloads. The second article is about optimizing SSD performance. Both articles include bold headlines and colorful images.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-549785-186615-4.png)Figure 4. The download link leads to a Blogspot page.

We identified 11 channels connected to CL-CRI-1171, which collectively had hundreds of thousands of subscribers and millions of views.

## Technical Analysis

Our investigation revealed three malware strains delivered by the group behind CL-CRI-1171 between June 2025 and April 2026. The following sections explain the technical aspects of the loader used by this cybercrime group and the deployed malware payloads:

  * **OfferLoader** – The delivery mechanism behind all recorded intrusions, an Inno Setup trojanized installer that sets up the other payloads.
  * **Operation A: Insomnia RAT** – A dual-payload, cross-platform backdoor that brings its own environment to ensure survival. Targeting both Windows and macOS using Node.js, paired with a twin Python agent.
  * **Operation B: ARKTunnel** – A previously unreported WebSocket tunneling RAT unpacks itself from a bitmap image using steganography. We found 50 samples spanning over a year of development, operating across four fictitious corporate-identity rotations.
  * **Operation C: Docro Hijacker** – A Chrome backdoor that revives a [browser-hijacking technique](https://www.malwarebytes.com/blog/news/2015/05/winyahoo-pup-modifies-chrome-secure-preferences) first seen in 2015, re-engineered to bypass modern integrity protections. This campaign represents the first observation of this modern variant in the wild.



### Initial Access Vector in Intrusions

We discovered two intrusion sets that began in the same way: a user searched for a legitimate utility, clicked a top search result that led to a malicious domain, and downloaded what appeared to be a legitimate application. Both infections delivered the same three payloads.

  * **First intrusion set** : Downloaded Bluetooth Driver for Windows 10.exe from a file-sharing archive. The installer was a trojanized Inno Setup package carrying the PPI loader with affiliate ID CID=2855.
  * **Second intrusion set** : Browsed to noiseship[.]cfd, a domain registered just 39 days earlier, and downloaded a trojanized windirstat.exe installer. This package carried the PPI loader with affiliate ID CID=3075.



### The OfferLoader Execution Chain

The operator's code and C2 communication designate each payload slot as an "offer," tracking variables as offer_execution, offer_execution_fail and offer_exists. Based on the naming convention, we track this loader as OfferLoader. OfferLoader uses chained Inno Setup (a legitimate installation packager) packages to deliver multiple payloads. Figure 5 shows the infection chain.

![A Cortex XSIAM infecton chain diagram illustrating the process of payload prevention by Advanced WildFire. It shows a main circle labeled "Installer" leading to another node. Three red X-marked paths branch indicate prevention. Advanced WildFire logo is present at the top.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-552145-186615-5.png)Figure 5. Cortex XSIAM view of the infection chain. In this case, Advanced WildFire blocked the payloads.

OfferLoader is delivered in a ZIP file, with the source download site providing the social engineering instructions required to guide users through downloading and executing an extraction tool. Based on our analysis of the collected samples, we observed the loader being delivered alongside a legitimate version of WinRAR, renamed to .store. The installer contains no embedded application files; all malicious logic is contained in the compiled Pascal [Code] section, which triggers when the installation page is displayed.

In two separate intrusion sets we discovered that the ZIP file contained OfferLoader masquerading as a windirstat.exe installer that initiates the compromise by unpacking windirstat.tmp. This temporary file transmits an initial tracking beacon to voyagemist[.]space. This is another gating mechanism: depending on the structure of the beacon, one of two text files will be retrieved. They either contain “no” to signal that the loader should not unpack further stages, or “ok” to signal all offers will be deployed. Following this check-in, the process spawns three child processes: eld0.exe, eld1.exe and eld2.exe. Each child process corresponds to a different malware campaign. The loader passes specific affiliate-tracking parameters to each process via a command line.

Figure 6 illustrates the entire OfferLoader infection chain at the time of the intrusion.

![A diagram showing an OffLoader attack chain process. The "Victim" is redirected to a domain, followed by the download of a file. This is unpacked into another file, which gates into a different domain. Three operations branch out: Operation A involves Insomnia RAT, Operation B involves ARKTunnel, and Operation C involves Docro Hijacker.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-554807-186615-6.png)Figure 6. Example of an OfferLoader infection chain.

OfferLoader's role ends once the three offers are spawned. From this point forward, each child process operates as an independent malware campaign with its own infrastructure, C2 protocol and objectives. The following sections analyze what each offer delivers.

### Operation A: Insomnia RAT – A Cross-Platform Backdoor

Insomnia RAT simultaneously distributes two payloads:

  * An upgraded variant of a Node.js backdoor (reported by [Walmart Global Tech](https://medium.com/walmartglobaltech/nodejs-backdoors-delivering-proxyware-and-monetization-schemes-1562917ed107) in 2025)
  * A complementary Python backdoor



We have dubbed these twin payloads Insomnia RAT, due to the user-agent string used for C2 communications: insomnia/2023.4.0 Windows.

Figure 7 shows the full infection chain that delivers Insomnia RAT’s twin payloads.

![A flowchart illustrating the new Insomnia RAT variant infection chain. It starts with a file loading.The flow continues through a domain, then to a hidden PowerShell downloader. The diagram also includes components like Node.js and Python 3.12. Arrows show how these components connect, with persistence strategies and rotating command and control \(C2\) server domain.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-557367-186615-7.png)Figure 7. The new Insomnia RAT variant infection chain.

Eld0.exe drops the a.dll payload and spawns a hidden PowerShell process to download and execute t.ps1. This double-stage installer script disables Windows Defender protections, adds the entire C:\ drive as an exclusion, suppresses security notifications and deploys the two Insomnia RAT backdoors. t.ps1 also downloads and sets up the environment needed to execute both backdoors by installing Python and Node.js on the victim’s machine. Node.js is hidden from the system's Add/Remove Programs list by setting SystemComponent=1 in the registry.

The first part of Insomnia RAT is a Node.js agent downloaded from stryper[.]info/aa.js. While the prior variant targeted Windows, Linux and FreeBSD with a single payload, this iteration targets Windows and macOS using platform-specific C2 server lists. It also deploys a companion Python agent as a redundant fallback, ensuring persistent access if one runtime environment is detected or removed.

The backdoor collects the victim's MachineGuid, universally unique identifier (UUID), hostname and operating system details. It then contacts its C2 servers via an HTTPS POST request to /d using a User-Agent string, insomnia/2023.4.0 Windows to disguise itself. The C2 server responds with a JSON array containing commands. These specify a payload type (node, cmd, ps1, sh, or ow for a self-update) and a download URL. Results are reported back to the /e endpoint.

To establish persistence, the installer registers a scheduled task named Maps Performance Task under \Microsoft\Windows\Maps\. This mimics a legitimate Windows task, executing the backdoor hourly and at system startup under the SYSTEM account.

The same t.ps1 script installs a second, redundant agent. This Python script is downloaded from aa.amazingshield[.]xyz. The installer downloads a legitimate Python distribution and registers a second scheduled task, OOBETaskScheduler, under \Microsoft\Windows\Servicing\.

The Python agent is simpler than its Node.js sibling, but follows the same C2 protocol pattern: POST requests to /d for tasks and POST requests to /e for error reporting. The agent collects the MachineGuid, OS product name, hostname and processor architecture.

The Python agent used crowdstri[.]com as its C2 domain. This appears to be a deliberate typosquat of crowdstrike[.]com, designed to blend into logs and evade quick security reviews.

### Operation B: ARKTunnel – A WebSocket RAT Hidden in a Bitmap

The eld1.exe chain terminates in a previously undocumented tunnel payload. The chain uses [least-significant-bit (LSB) steganography](https://medium.com/@renantkn/lsb-steganography-hiding-a-message-in-the-pixels-of-an-image-4722a8567046) to deploy the final payload. Figure 8 shows the full infection chain of Operation B.

![A flowchart illustrating the ARKTunnel infection chain, a sequence of events involving multiple software entities. The flowchart highlights processes such as persistence, host reconnaissance, and the use of an autorun.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-559922-186615-8.png)Figure 8. The ARKTunnel infection chain.

Rather than dropping an executable directly to disk, eld1.exe extracts a ZIP archive from a BMP image resource using LSB steganography. The result is the payload archive, ProcorTrex.zip, which contains wscl.exe, a previously unreported WebSocket-based tunneling RAT. We named this RAT ARKTunnel, based on the attacker's fabricated company name rotation of EarthKark and TamarkLark.

ARKTunnel installs itself as a Windows service named wscl-13 or msvcsrvc with a delayed autostart configuration. The RAT supports TCP and UDP tunneling, as well as file execution.

The C2 server address, reg.pcsdkflyer[.]ca, is decoded from a 39-byte configuration blob using Base64-decoding followed by an XOR decryption routine. The portable executable (PE) metadata of wscl.exe contains a fabricated company name, TamarkLark Corporation, and a fictitious product name, TamarkLark Manager, which led us to suspect that other ARKTunnel samples might use additional fabricated company names.

The investigation revealed at least 50 samples deployed over the course of a year. The developer rotated through at least two fake company identities while maintaining an identical icon, binary structure and deployment pattern:

  * EarthLink in May 2025: EarthLink is the name of a legitimate internet provider, however the attackers used this name coincidentally in the file version information. The attackers did not use or impersonate EarthLink resources or identity.
  * EarthChain from May 2025–April 2026: EarthChain is also real company name that the attackers used coincidentally. Likewise, also they did not use or impersonate the company’s resources or identity.
  * EarthKark: A fake identity, used from February 2026–June 2026
  * TamarkLark: A fake identity, used from March 2026–June 2026



All of the samples share the same wscl.exe filename pattern and GUID-based temp directory extraction pattern, indicating that they are variants of the same family.

Despite 50 samples spanning a full year of development and four identity rotations, ARKTunnel has attracted no public reporting or dedicated tracking, with each sample individually flagged as a generic Trojan rather than recognized as a tunneling implant.

### Operation C: Docro Hijacker – Reviving Old Techniques

The eld2.exe payload installs a Chrome browser hijacker that we have named Docro Hijacker. The hijacker revives a [browser-hijacking technique](https://www.malwarebytes.com/blog/news/2015/05/winyahoo-pup-modifies-chrome-secure-preferences) that has resurfaced periodically since 2015, now re-engineered to bypass updates to Chrome's integrity protections. While this iteration closely mirrors a proof-of-concept detailed by [Synacktiv](https://www.synacktiv.com/en/publications/the-phantom-extension-backdooring-chrome-through-uncharted-pathways) in 2025, this campaign marks the updated technique’s first documented instance of in-the-wild deployment.

Figure 9 shows the Docro Hijacker installation chain.

![A flowchart illustrating the Docro Hijacker infection chain. The flow includes tampering with Chrome secure preferences. The process installs "Docro Hijacker," which connects to four domain indicating various malicious activities like script injection and telemetry.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-562486-186615-9.png)Figure 9. The Docro Hijacker infection chain.

eld2.exe is an Inno Setup package, and much like its loader, it extracts and runs eld2.tmp which contacts the affiliate’s extentrack[.]com install tracker.

eld2.tmp drops and loads Adblock.dll, which bypasses Chrome's Secure Preferences HMAC-SHA256 integrity check. The DLL extracts Chrome's HMAC key from resources.pak, computes valid HMAC signatures for the modified preference values and writes them directly to the Secure Preferences file. This file functions as an anti-tamper mechanism for browsers by storing a validated copy of the user's settings.

This manipulation allows the malware to execute two primary actions:

  * **Search hijacking** : Changes the default search provider to mqsearch[.]com, a domain that masquerades as a search engine
  * **Extension installation** : Installs the docro extension, a Chrome Manifest V3 extension located at C:\ProgramData\DocsHelper\docro\



The docro extension uses Chrome's declarativeNetRequest API to dynamically rewrite network requests. Upon installation, it contacts vendralo[.]info to retrieve a unique per-victim UUID and fetch a set of network rewriting rules that are refreshed hourly.

These rules are used to hijack and monetize search results in the victim's browser. When the victim performs an internet search, across any of more than 190 [Google country-code domains](https://blog.google/products-and-platforms/products/search/country-code-top-level-domains/), the extension loads a script from drelto[.]info/farlix into the search results page. Because the script runs within the search engine's own origin context, it has full access to the page content. This enables the operator to inject advertisements into organic search results, rewrite affiliate links to capture referral revenue and/or redirect clicks to attacker-controlled destinations. These actions are functionally transparent to the user and visually indistinguishable from the legitimate search page.

The extension also checks vendralo[.]info for updates via /extensionInstaller/updateChromeExtension, allowing the operator to silently rotate to a new extension version at any time. Install telemetry is reported to finersto[.]com and extentrack[.]com.

With more than 50 unique samples contacting mqsearch[.]com according to VirusTotal, Docro Hijacker appears to be a mature, independent monetization module.

## Conclusion

The actors behind CL-CRI-1171 did not use sophisticated evasion techniques, but focused their efforts on building a loader that is exceptionally difficult to track due to its clever gating mechanisms.

Our investigation highlights how the authors of OfferLoader, by being intentional about its simplicity and by hiding all of its functions as bytecode within a package, designed the malware to evade scrutiny while quietly building a massive, mature infection funnel.

Although OfferLoader was easy for defenders and security products to miss, its gating mechanisms were not, and the sheer number of them was our first clue that more widespread activity was occurring.

While a loader that just drops a payload is seemingly routine, this mechanism allowed possibly thousands of rotational malware bundles, including entirely new and undocumented malware families, to remain hidden from standard security attention. Ultimately, this case serves as a critical reminder for defenders: Treating commodity loader infections as minor, routine events overlooks the dangerous payloads and campaigns that might be tied to them.

## Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected against the threats described in this report through the following products and services:

  * The [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire) machine-learning models and analysis techniques have been reviewed and updated in light of the indicators shared in this research. Through continuous cloud-based analysis, Advanced WildFire is designed to proactively identify and block OfferLoader samples as well as downstream payloads, including Insomnia RAT, ARKTunnel, and Docro Hijacker.
  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) identify known domains and URLs associated with this activity as malicious.
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) can help detect and prevent the OfferLoader chain and all three payload branches described in this article. Cortex customers benefit from multiple layers of protection against this threat, including: 
    * YARA-based signatures targeting the OfferLoader family and its staged payloads
    * Behavioral detection rules that help prevent: 
      * Malicious Chrome extension setup
      * Untrusted service installations used for persistence
      * Trojanized installer execution patterns



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

## Indicators of Compromise

### Initial Access and OfferLoader

SHA256 hash: 7f792c45de1e28fd42ac44c9444f157a2161742d130bac336c0e991aabbb112c  
File name: windirstat.exe  
File type: PE32 executable, Inno Setup 6.7.1  
File description: OfferLoader trojanized WinDirStat installer delivered via SEO-poisoning

SHA256 hash: fc485882626512e7ff82a1d7cd8e8fb3e9751b026d97e682d6908aefff1f2d73  
File name: windirstat.tmp  
File type: PE32 executable, Inno Setup unpacked stage  
File description: Unpacked WinDirStat stage

### Operation A: Insomnia RAT

SHA256 hash: 3052bd320a34e12ee694811ed0578797477dfd480c664491e509ed15ce1a6961  
File name: eld0.exe  
File type: PE32 executable, Inno Setup 6.3.0 SetupLdr  
File description: Insomnia RAT initial loader

SHA256 hash: 25558ea78c4aa0fdd0f45fafcaa546d3115dc5806809d144a5801a40e48fd4c5  
File name: eld0.tmp  
File type: PE32 executable, Inno Setup unpacked stage  
File description: Unpacked loader stage

SHA256 hash: 9b0d9cbc0fd4a7bae8b78a15dfbe63052779414ad725845732c4a0083008da69  
File name: a.dll  
File type: PE32 DLL  
File description: Executes the PowerShell downloader for the Node.js and Python second stages

SHA256 hash: ceb30a5eb9ad9d9c6712c80726df16f96f99d9fc0753be241b00b4d636eb576e  
File name: t.ps1  
File type: PowerShell  
File description: Insomnia RAT PowerShell loader

SHA256 hash: cf184d04ca31fb2b6b7efd85399c29c1136b539153e137ceb3877b1b905791de  
File name: <guid>.py  
File type: Python script  
File description: the Python-based component of the Insomnia RAT dual payload.

SHA256 hash: 62d49d0c78207ec2452cc8a30501db771c9edbae89889e41a7dd227551243e8e  
File name: aa.js  
File type: JavaScript  
File description: the Node.js-based component of the Insomnia RAT dual payload.

URL: hxxps[:]//stryper[.]info/t.ps1  
Description: Stage-2 PowerShell installer for the Node.js and Python agents

URL: hxxps[:]//stryper[.]info/aa.js  
Description: Stage-3 Node.js agent

URL: hxxp[:]//aa.amazingshield[.]xyz/33244556546.py  
Description: Stage-3 Python agent

Domain: stryper[.]info  
Description: Second-stage PowerShell and Node.js agent host

Domain: aa.amazingshield[.]xyz  
Description: Python agent host

Domain: crowdstri[.]com  
Description: CrowdStrike-typosquat C2 for the Python agent

### Operation B: ARKTunnel

SHA256 hash: aaebc8c07de485be6d1bfa956668c5e18aa1ff5588dfe84672e20ae90b4560f1  
File name: eld1.exe  
File type: PE32 executable  
File description: LSB-steganography dropper. The attacker forged the PE version-info resource to mimic a popular test proctoring application.

SHA256 hash: e05bc22afbc5ddd50b49c85ee169dd13318000d38286de2b8bcff98217256a8d File size: 92,657 bytes  
File name: procorTrex.zip  
File location: C:\Users\Public\procorTrex.zip  
File type: ZIP archive  
File description: ZIP carved from the eld1.exe BMP steganography payload

SHA256 hash: b367762140ae7f5098230b8a5da738c9241f286281ec9439dd6ca581fc87989c File size: 245,248 bytes  
File name: wscl.exe  
File type: PE32 executable  
File description: WebSocket tunneling RAT

ARKTunnel resource icons:  
SHA256 hash: d8d783f8e050a6e394f3c0aa5e2bc73a38d822e55fbc39c0648cbff566de3cdf  
File description: Resource Icon shared across ARKTunnel samples

SHA256 hash: 06e0afd01bbc6c9d5dc16c3165089b233dc071e1f251abd06235d1b9166cdac5  
File description: Resource Icon shared across ARKTunnel samples

Domain: reg.pcsdkflyer[.]ca  
Description: wscl.exe WebSocket RAT C2

### Operation C: Docro Hijacker

SHA256 hash: 2c6e11027b011042c9a118fc20728f8f4ebb6be8795cc84cc9a45622c297d354  
File name: eld2.exe  
File type: PE32 executable, Inno Setup installer  
File description: Branch C installer that drops Adblock.dll and the docro Chrome extension

SHA256 hash: 553ce594c9c6afdd4794fddc28c194e3bc3c1b052310e5099c58ac15bab72104  
File name: eld2.tmp  
File type: PE32 executable  
File description: Inno Setup unpacked stage

SHA256 hash: fdcc95b7791c0d6590dcf1a412dc9fcc92ad2095818d1b78368b31efad012007  
File size: 3,041,280 bytes  
File name: Adblock.dll  
File location: %TEMP%\Adblock.dll  
File type: PE32 DLL  
File description: Chrome Secure Preferences HMAC-SHA256 bypass DLL that sideloads the docro extension and hijacks the default search provider

Docro extension path:  
File location: C:\ProgramData\DocsHelper\docro  
File description: Manifest V3 Chrome extension sideloaded by Adblock.dll

Domain: vendralo[.]info  
Description: Per-victim UUID and hourly rule delivery

Domain: finersto[.]com  
Description: Extension install and start telemetry

Domain: drelto[.]info  
Description: SERP-injection script host

Domain: mqsearch[.]com  
Description: Hijacked the default search provider endpoint

Domain: extentrack[.]com  
Description: Docs Helper install-success and install-failure callback

### CL-CRI-1171 Rotational Infrastructure

#### Initial-Access Lure and SEO File-Locker Hosts

**Domain** | **Role**  
---|---  
noiseship[.]cfd | SEO-poison domain  
atthelake[.]info | Top referring SEO-poison domain  
uy.basesfiles[.]com | Fake file host  
basesfile[.]com | Sibling fake file host  
igk.filexspace[.]com ikx.filexspace[.]com | SEO file-locker lure hosts  
filexstorage[.]site | SEO file-locker lure host  
filescloud[.]pro | SEO file-locker lure host  
zippyfiles[.]net | SEO file-locker lure host  
mifilesx[.]site | SEO file-locker lure host  
dw.xrsdownload[.]com | SEO file-locker lure host  
storage.ggclicker[.]com | SEO file-locker / referrer host  
watchadvance[.]com | SEO-poisoning domain  
  
#### Domains Used to Confirm OfferLoader Installations

#### Domain:

  * animalview[.]xyz
  * trickflag[.]info
  * suitstraw[.]info
  * connect.fuelleg[.]info
  * vesselsystem[.]xyz
  * minewave[.]info
  * collartitle[.]info
  * boardmagic[.]info
  * placespoon[.]xyz
  * needcherries[.]online



#### Payload-Handoff and Second-Stage Hosts

#### Install-Tracker Beacons (Operator Panel)

**Domain** | **Role**  
---|---  
voyagemist[.]space | PPI affiliate install tracker  
statementtouch[.]xyz | PPI affiliate install tracker  
chawton[.]info | PPI affiliate install tracker  
  
#### YouTube Funnel – Burner Blogs and Custom-Domain Sites

**Domain Name** | **Persona** | **Type**  
---|---|---  
velfps.blogspot[.]com | Velvox | Blogspot burner  
velvoxlab.blogspot[.]com | Velvox | Blogspot burner  
venrx.blogspot[.]com | Venrx | Blogspot burner  
venrxhub.blogspot[.]com | Venrx | Blogspot burner  
venrx[.]xyz | Venrx | Custom-domain burner  
ravexoffical.blogspot[.]com | Ravex | Blogspot burner  
adex-blog.blogspot[.]com | Adex | Blogspot burner  
  
Please note: While Velvox is a real company, the attackers used its name coincidentally. They did not use or impersonate the company’s resources or identity.

## Additional Resources

  * [“WinYahoo” PUP Modifies Chrome Secure Preferences](https://www.malwarebytes.com/blog/news/2015/05/winyahoo-pup-modifies-chrome-secure-preferences) – Malwarebytes
  * [NodeJS backdoors delivering proxyware and monetization schemes](https://medium.com/walmartglobaltech/nodejs-backdoors-delivering-proxyware-and-monetization-schemes-1562917ed107) – Walmart Global Tech blog



## Appendix A: CL-CRI-1171 Full Discovered Infrastructure Tables

**Indicator** | **Role**  
---|---  
achievershelf[.]space | Gate/landing  
activitymeal[.]space | Gate/landing  
additionplot[.]cfd | Gate/landing  
adviceturn[.]xyz | Gate/landing  
afternoonscrew[.]space | Gate/landing  
agreementjuice[.]space | Gate/landing  
airplaneiron[.]xyz | Gate/landing  
airtwig[.]xyz | Gate/landing  
amountfuel[.]icu | Gate/landing  
animalrecord[.]xyz | Gate/landing  
apparatustruck[.]xyz | Gate/landing  
apparelplate[.]space | Gate/landing  
archairport[.]xyz | Gate/landing  
authoritykittens[.]info | Gate/landing  
babyvein[.]xyz | Gate/landing  
badgewing[.]xyz | Gate/landing  
bagcare[.]space | Gate/landing  
basinpleasure[.]xyz | Gate/landing  
basketballyear[.]xyz | Gate/landing  
baskethumor[.]xyz | Gate/landing  
bedroomdesire[.]xyz | Gate/landing  
beliefpicture[.]xyz | Gate/landing  
bellplayground[.]xyz | Gate/landing  
bikesdonkey[.]info | Gate/landing  
birthdaymagic[.]xyz | Gate/landing  
boatthought[.]xyz | Gate/landing  
boundarychickens[.]xyz | Gate/landing  
boytank[.]xyz | Gate/landing  
branchmorning[.]xyz | Gate/landing  
breathdoctor[.]xyz | Gate/landing  
bubbleslip[.]xyz | Gate/landing  
cabbagemeasure[.]xyz | Gate/landing  
cablecanvas[.]xyz | Gate/landing  
cardgrape[.]xyz | Gate/landing  
cattlegold[.]xyz | Gate/landing  
celeryerror[.]xyz | Gate/landing  
centscarf[.]xyz | Gate/landing  
chalkprose[.]xyz | Gate/landing  
cherriestruck[.]space | Gate/landing  
chesstail[.]xyz | Gate/landing  
chickensmine[.]space | Gate/landing  
churchpail[.]xyz | Gate/landing  
clothcrib[.]xyz | Gate/landing  
clothcurrent[.]xyz | Gate/landing  
coatberry[.]xyz | Gate/landing  
connect.activitykitty[.]xyz | Install tracker  
connect.apparatustaste[.]xyz | Install tracker  
connect.armcard[.]xyz | Install tracker  
connect.badgeterritory[.]xyz | Install tracker  
connect.baitmetal[.]xyz | Install tracker  
connect.beefteeth[.]xyz | Install tracker  
connect.believesisters[.]xyz | Install tracker  
connect.boundaryfly[.]xyz | Install tracker  
connect.bubbleappliance[.]xyz | Install tracker  
connect.cableland[.]xyz | Install tracker  
connect.chinexpert[.]xyz | Install tracker  
connect.conditiongrade[.]xyz | Install tracker  
connect.coppersummer[.]xyz | Install tracker  
connect.creatorcreator[.]xyz | Install tracker  
connect.dresstent[.]xyz | Install tracker  
connect.dropjeans[.]xyz | Install tracker  
connect.edgeplayground[.]xyz | Install tracker  
connect.exchangeclub[.]xyz | Install tracker  
connect.existencediscussion[.]info | Install tracker  
connect.expansionsalt[.]info | Install tracker  
connect.fangstitch[.]xyz | Install tracker  
connect.fogparcel[.]info | Install tracker  
connect.foodhook[.]info | Install tracker  
connect.forkcountry[.]xyz | Install tracker  
connect.geesepurpose[.]xyz | Install tracker  
connect.giantsdogs[.]info | Install tracker  
connect.giraffetoothpaste[.]xyz | Install tracker  
connect.guitarrobin[.]xyz | Install tracker  
connect.halllunch[.]info | Install tracker  
connect.harborclam[.]xyz | Install tracker  
connect.holecompany[.]info | Install tracker  
connect.knifesea[.]icu | Install tracker  
connect.monthsmoke[.]info | Install tracker  
connect.nosegovernor[.]xyz | Install tracker  
connect.pagesubstance[.]xyz | Install tracker  
connect.poisonblade[.]xyz | Install tracker  
connect.prosesalt[.]xyz | Install tracker  
connect.purposethings[.]info | Install tracker  
connect.quiltgirls[.]xyz | Install tracker  
connect.reactionbit[.]info | Install tracker  
connect.rewardrun[.]xyz | Install tracker  
connect.riceapparel[.]xyz | Install tracker  
connect.seashoreletters[.]info | Install tracker  
connect.selectiondogs[.]xyz | Install tracker  
connect.shapeboot[.]info | Install tracker  
connect.shoptax[.]xyz | Install tracker  
connect.stopfinger[.]info | Install tracker  
connect.structurekiss[.]xyz | Install tracker  
connect.tanksuggestion[.]xyz | Install tracker  
connect.thingbrass[.]xyz | Install tracker  
connect.thoughtslave[.]xyz | Install tracker  
connect.threadfuel[.]xyz | Install tracker  
connect.trailcontrol[.]xyz | Install tracker  
connect.trickbushes[.]info | Install tracker  
connect.vacationthought[.]xyz | Install tracker  
connect.viewschool[.]xyz | Install tracker  
connect.voyagelaugh[.]xyz | Install tracker  
connect.woolreward[.]xyz | Install tracker  
connect.yearicicle[.]xyz | Install tracker  
connect.zebratransport[.]xyz | Install tracker  
controlprice[.]xyz | Gate/landing  
coughcoal[.]icu | Gate/landing  
countrypipe[.]space | Gate/landing  
cowsfoot[.]xyz | Gate/landing  
crackfood[.]space | Gate/landing  
creamfurniture[.]space | Gate/landing  
creditchickens[.]xyz | Gate/landing  
crediteducation[.]cfd | Gate/landing  
crimestreet[.]xyz | Gate/landing  
crimesupport[.]cfd | Gate/landing  
curvebite[.]xyz | Gate/landing  
deathrock[.]xyz | Gate/landing  
deathshop[.]xyz | Gate/landing  
decisionreaction[.]xyz | Gate/landing  
dinosaursjam[.]cfd | Gate/landing  
distancebedroom[.]xyz | Gate/landing  
distributiontheory[.]cfd | Gate/landing  
dolldebt[.]xyz | Gate/landing  
doorsoap[.]cfd | Gate/landing  
dustprotest[.]icu | Gate/landing  
expansionsalt[.]info | Gate/landing  
fallbeginner[.]xyz | Gate/landing  
fangbear[.]xyz | Gate/landing  
filescenter[.]cloud | Gate/landing  
filesilo[.]cloud | Gate/landing  
fingerbasketball[.]xyz | Gate/landing  
flavorwood[.]xyz | Gate/landing  
fleshfrog[.]xyz | Gate/landing  
fleshplants[.]xyz | Gate/landing  
fleshproduce[.]xyz | Gate/landing  
foodrock[.]space | Gate/landing  
forkmice[.]xyz | Gate/landing  
friendjewel[.]cfd | Gate/landing  
geeseairport[.]xyz | Gate/landing  
girlsgrain[.]xyz | Gate/landing  
glassmove[.]xyz | Gate/landing  
goldsteel[.]cfd | Gate/landing  
governmentyard[.]cfd | Gate/landing  
grandfatherquiver[.]xyz | Gate/landing  
gripcollar[.]xyz | Gate/landing  
gripsleep[.]xyz | Gate/landing  
gunbear[.]xyz | Gate/landing  
hairreward[.]xyz | Gate/landing  
hatescale[.]info | Gate/landing  
healthiron[.]space | Gate/landing  
holemuscle[.]xyz | Gate/landing  
homecub[.]cfd | Gate/landing  
homefireman[.]xyz | Gate/landing  
honeyfear[.]xyz | Gate/landing  
ilesilo[.]cloud | Gate/landing  
instrumentvolcano[.]space | Gate/landing  
kittenschalk[.]xyz | Gate/landing  
kittensgrade[.]cfd | Gate/landing  
kittensrobin[.]info | Gate/landing  
landerror[.]xyz | Gate/landing  
lesilo[.]cloud | Gate/landing  
liptendency[.]info | Gate/landing  
liquidtoes[.]xyz | Gate/landing  
liquidwrench[.]cfd | Gate/landing  
lockettrail[.]xyz | Gate/landing  
lumberbaseball[.]xyz | Gate/landing  
memorycompany[.]xyz | Gate/landing  
micesisters[.]xyz | Gate/landing  
milkname[.]xyz | Gate/landing  
minuteblade[.]xyz | Gate/landing  
mountainsurprise[.]cfd | Gate/landing  
mouthfruit[.]cfd | Gate/landing  
noiseship[.]cfd | Gate/landing  
northbox[.]xyz | Gate/landing  
partpipe[.]xyz | Gate/landing  
partyfriends[.]cfd | Gate/landing  
passengerbrake[.]space | Gate/landing  
peacejewel[.]xyz | Gate/landing  
peacetongue[.]xyz | Gate/landing  
petminister[.]xyz | Gate/landing  
pictureporter[.]cfd | Gate/landing  
pieplant[.]space | Gate/landing  
pizzasthread[.]xyz | Gate/landing  
pleasurewaves[.]info | Gate/landing  
popcornregret[.]xyz | Gate/landing  
porterdebt[.]xyz | Gate/landing  
powerbushes[.]xyz | Gate/landing  
profitfact[.]xyz | Gate/landing  
prosetoothbrush[.]xyz | Gate/landing  
quincepage[.]xyz | Gate/landing  
raintexture[.]xyz | Gate/landing  
rakepurpose[.]xyz | Gate/landing  
raterake[.]cfd | Gate/landing  
readingscience[.]xyz | Gate/landing  
reasonachiever[.]xyz | Gate/landing  
recessgiraffe[.]xyz | Gate/landing  
recordhistory[.]xyz | Gate/landing  
regretsquirrel[.]xyz | Gate/landing  
restbucket[.]xyz | Gate/landing  
ricestar[.]xyz | Gate/landing  
rifledog[.]xyz | Gate/landing  
ringsparcel[.]xyz | Gate/landing  
roadyear[.]xyz | Gate/landing  
rockcredit[.]space | Gate/landing  
rollglass[.]xyz | Gate/landing  
roofbattle[.]xyz | Gate/landing  
roofreaction[.]xyz | Gate/landing  
rosegrip[.]xyz | Gate/landing  
routeletters[.]xyz | Gate/landing  
runhouses[.]xyz | Gate/landing  
scarecrowcare[.]xyz | Gate/landing  
scentrod[.]info | Gate/landing  
screwbirth[.]xyz | Gate/landing  
seatlace[.]space | Gate/landing  
seaword[.]xyz | Gate/landing  
servantadvice[.]xyz | Gate/landing  
shiptank[.]cfd | Gate/landing  
shirtexample[.]xyz | Gate/landing  
shoesearthquake[.]xyz | Gate/landing  
sinkwash[.]space | Gate/landing  
skirtloss[.]xyz | Gate/landing  
slipvegetable[.]xyz | Gate/landing  
smokecar[.]space | Gate/landing  
songtheory[.]xyz | Gate/landing  
spadeleg[.]xyz | Gate/landing  
sparkrice[.]space | Gate/landing  
sparkrub[.]xyz | Gate/landing  
spoonducks[.]cfd | Gate/landing  
springdogs[.]xyz | Gate/landing  
spybaseball[.]space | Gate/landing  
startmonkey[.]cfd | Gate/landing  
statementservant[.]xyz | Gate/landing  
statementtouch[.]xyz | Gate/landing  
steamhouses[.]cfd | Gate/landing  
stopzinc[.]xyz | Gate/landing  
structurelinen[.]xyz | Gate/landing  
suggestioncemetery[.]xyz | Gate/landing  
suitsoap[.]xyz | Gate/landing  
suitstraw[.]info | Gate/landing  
swimrest[.]xyz | Gate/landing  
tablechess[.]info | Gate/landing  
tailsilk[.]xyz | Gate/landing  
territorycaption[.]xyz | Gate/landing  
texturebadge[.]xyz | Gate/landing  
thrillducks[.]xyz | Gate/landing  
throneback[.]xyz | Gate/landing  
tinsofa[.]xyz | Gate/landing  
toespiders[.]xyz | Gate/landing  
toothpastesense[.]xyz | Gate/landing  
toothpastesun[.]xyz | Gate/landing  
townquiver[.]xyz | Gate/landing  
trampdonkey[.]icu | Gate/landing  
treesboard[.]xyz | Gate/landing  
truckpig[.]cfd | Gate/landing  
truckshat[.]xyz | Gate/landing  
turnclass[.]xyz | Gate/landing  
umbrellavessel[.]xyz | Gate/landing  
vacationengine[.]xyz | Gate/landing  
vesselsystem[.]xyz | Gate/landing  
vestthings[.]cfd | Gate/landing  
volcanopin[.]xyz | Gate/landing  
voyagemist[.]space | Gate/landing  
wastereading[.]xyz | Gate/landing  
wasteturkey[.]xyz | Gate/landing  
wastewine[.]xyz | Gate/landing  
wavepan[.]xyz | Gate/landing  
whistlebook[.]cfd | Gate/landing  
whistlesong[.]xyz | Gate/landing  
wormspark[.]xyz | Gate/landing  
woundsecretary[.]xyz | Gate/landing  
wrenobservation[.]xyz | Gate/landing  
yamsmell[.]xyz | Gate/landing  
yardvalue[.]cfd | Gate/landing  
zephyrhall[.]cfd | Gate/landing  
  
## Appendix B: YouTube Channels Linked to CL-CRI-1171 Activity

(Channels were taken down after we notified Google.)

**Persona** | **Channel**  
---|---  
Velvox | @VelvoxYT  
Venrx | @Venrx  
Ravex | @RAVEX-wu1pg  
Adex | @adex915  
Ripex | @ripex  
HASNZ TWEAKS | @hasnzyt  
Ontrendytt | @OnTrendd  
Trend Rise | @trendrise  
Reknotic Lab | @Reknotic  
NowFixTutorials | @NowFixTutorials  
f4fix | @f4fix  
  
Back to top

### Tags

  * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")
  * [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")
  * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")
  * [Docro Hijacker](https://unit42.paloaltonetworks.com/tag/docro-hijacker/ "Docro Hijacker")
  * [Pay-per-install](https://unit42.paloaltonetworks.com/tag/pay-per-install/ "pay-per-install")
  * [Payload](https://unit42.paloaltonetworks.com/tag/payload/ "payload")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")

### Table of Contents

  *   * Executive Summary
  * Overview of CL-CRI-1171 Activity
    * The PPI Ecosystem: An Infection Marketplace
    * Tracking CL-CRI-1171: The PPI Operation Behind the Payloads
    * Unpacking the Delivery Infrastructure
    * The YouTube Funnel
  * Technical Analysis
    * Initial Access Vector in Intrusions
    * The OfferLoader Execution Chain
    * Operation A: Insomnia RAT – A Cross-Platform Backdoor
    * Operation B: ARKTunnel – A WebSocket RAT Hidden in a Bitmap
    * Operation C: Docro Hijacker – Reviving Old Techniques
  * Conclusion
  * Palo Alto Networks Protection and Mitigation
  * Indicators of Compromise
    * Initial Access and OfferLoader
    * Operation A: Insomnia RAT
    * Operation B: ARKTunnel
    * Operation C: Docro Hijacker
    * CL-CRI-1171 Rotational Infrastructure
      * Initial-Access Lure and SEO File-Locker Hosts
      * Domains Used to Confirm OfferLoader Installations
      * Domain:
      * Payload-Handoff and Second-Stage Hosts
      * Install-Tracker Beacons (Operator Panel)
      * YouTube Funnel – Burner Blogs and Custom-Domain Sites
  * Additional Resources
  * Appendix A: CL-CRI-1171 Full Discovered Infrastructure Tables
  * Appendix B: YouTube Channels Linked to CL-CRI-1171 Activity



### Related Articles

  * [ Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "article - table of contents")
  * [ The npm Threat Landscape: Attack Surface and Mitigations (Updated July 15) ](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/ "article - table of contents")
  * [ TuxBot v3: Inside an IoT Botnet Framework With LLM-Assisted Development ](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)