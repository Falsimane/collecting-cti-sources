# Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/
- **Date :** 2026-08-31

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 13 min read 

Related Products

[![Advanced DNS Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced DNS Security](https://unit42.paloaltonetworks.com/product-category/advanced-dns-security/ "Advanced DNS Security")[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Idira icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/idira_RGB_logo_Icon_Color-e1787069105644.png)Idira](https://unit42.paloaltonetworks.com/product-category/panw-idira/ "Idira")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Noam Sala](https://unit42.paloaltonetworks.com/author/noam-sala/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:August 31, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/)
    * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/)
    * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/)
    * [Payload](https://unit42.paloaltonetworks.com/tag/payload/)
    * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/)
    * [Remote Access Trojan](https://unit42.paloaltonetworks.com/tag/remote-access-trojan/)
    * [Spoof](https://unit42.paloaltonetworks.com/tag/spoof/)
    * [Vishing](https://unit42.paloaltonetworks.com/tag/vishing/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Spring%20Ring:%20An%20Inside%20Look%20at%20Voice%20Phishing%20Campaigns%20in%20Microsoft%20Teams&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fspring-ring-voice-phishing-campaigns%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fspring-ring-voice-phishing-campaigns%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fspring-ring-voice-phishing-campaigns%2F&title=Spring%20Ring:%20An%20Inside%20Look%20at%20Voice%20Phishing%20Campaigns%20in%20Microsoft%20Teams "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fspring-ring-voice-phishing-campaigns%2F&text=Spring%20Ring:%20An%20Inside%20Look%20at%20Voice%20Phishing%20Campaigns%20in%20Microsoft%20Teams "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fspring-ring-voice-phishing-campaigns%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Spring%20Ring:%20An%20Inside%20Look%20at%20Voice%20Phishing%20Campaigns%20in%20Microsoft%20Teams%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fspring-ring-voice-phishing-campaigns%2F "Share in Mastodon")



## Executive Summary

Between January and April 2026, we uncovered a coordinated social engineering operation that leveraged external Microsoft Teams accounts to masquerade as IT help desk personnel. Our telemetry reveals that this operation targeted more than 150 employees across at least 10 companies in various industries. We call this activity Spring Ring.

What seems like a benign chat is in fact a voice phishing (vishing) call, during which adversaries try to coerce victims into executing remote monitoring and management (RMM) tools or custom malware. In a more advanced variant, attackers transitioned from a vishing call to a full-blown Microsoft NT LAN Manager (NTLM) relay attack aimed at an organization's domain controller (DC).

We provide a technical breakdown of this operation’s attack lifecycle across two observed campaigns, both illustrating vishing manipulation that resulted in the attempted payload delivery via two distinct attack vectors.

These two campaigns demonstrate the weaponization of communication platforms as identity becomes a primary attack vector.

Palo Alto Networks customers are better protected from the threats described here through the following products and services:

  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security)
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM)
  * [Cortex Advanced Email Security](https://www.paloaltonetworks.com/cortex/advanced-email-security)
  * [Cortex Cloud Identity Threat Detection](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-identity-security/what-is-cortex-cloud-identity-security)
  * [Idira Threat Detection and Response (ITDR)](https://docs.cyberark.com/detect-and-respond/latest/en/content/get-started/what-is-detect-and-respond.htm)
  * [Idira Endpoint Privileged Manager (EPM)](https://docs.cyberark.com/epm/latest/en/content/intro/introduction.htm)
  * [Idira Privileged Access Management (PAM)](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1)
  * [Idira Secure Infrastructure Access (SIA)](https://docs.cyberark.com/pam-self-hosted/latest/en/content/pasimp/integrate-with-sia.htm)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Phishing](https://unit42.paloaltonetworks.com/tag/phishing/), [Identity](https://unit42.paloaltonetworks.com/tag/identity/), [Social Engineering](https://unit42.paloaltonetworks.com/tag/social-engineering/)**  
---|---  
  
## Overview: The Trust Gap

Spring Ring’s activity mirrors a broader trend in the threat landscape toward social engineering campaigns. According to our recently published [Insights blog](https://unit42.paloaltonetworks.com/microsoft-teams-phishing/), threat actors have increasingly moved away from traditional phishing techniques toward trusted collaboration tools.

In the first four months of 2026, phishing alerts from collaboration tools represented 42% of all phishing alerts in Cortex, up from 30% of all phishing alerts in the preceding four months. In addition, according to KnowBe4’s Phishing Threat Trends Report, Teams-based attacks [rose by 41% [PDF]](https://www.knowbe4.com/hubfs/Phishing_Threat_Trends_Report_Vol7_en-US.pdf) between October 2025 and March 2026. They note that this surge is driven by attackers exploiting the platform's default “[Chat with Anyone](https://learn.microsoft.com/en-us/microsoftteams/chat-with-people-not-using-teams)” feature to initiate direct chats with users outside their organization.

Previous Teams-based attacks, such as those by Cloaked Ursa (aka [APT29](https://insidersecurity.co/apt29-midnight-blizzard-phishing-attacks-via-microsoft-teams-tactics-techniques-and-prevention/)), focused on credential harvesting and group chat-based social engineering. They often relied on malicious links or fake Entra ID tenants to appear legitimate.

Spring Ring’s approach relies on active human voice interaction. In this way, attackers can evade detection without a software exploit. Instead, they rely on exploiting the trust that employees place in software as a service (SaaS) collaboration platforms.

### SaaS Applications: The New High-Value Target

SaaS applications are essential for business operations, storing an organization’s most critical and sensitive data. Unlike email, where users are trained to look for external sender banners or suspicious links, communications platforms provide a closed loop that attackers exploit by:

  * **Leveraging platform trust:** People are more likely to engage with a message from a help desk identity than a random email from an external domain
  * **Exploiting human interaction:** A professional voice on an audio call creates a level of trust that is difficult to manufacture in text, making the victim more susceptible to manipulation
  * **Bypassing the monitoring gap:** Voice calls are often less monitored, recorded or documented than employees’ digital file operations or email histories, providing attackers with a secluded environment to execute their lures



### The Evolution of Collaboration Attacks

The Spring Ring operation represents an evolution from previous campaigns by merging vishing into the Teams workflow. This shift moves the attack from a passive click-and-harvest model to a real-time engagement.

Attackers can then pivot based on the victim's responses. Once the trust gap is crossed, the path to domain-level privileges via open-source tools like [PetitPotam](https://github.com/topotam/PetitPotam) is short.

Figure 1 shows an example of the warning that Teams users get when an external identity creates a chat with them.

![A screenshot of Microsoft Team's notification about being added to a group chat. A warning message indicates the person is from outside the organization, advising caution against sharing account information. Options to "Delete" or "Accept" are available.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-28307-186248-1.png)Figure 1. External chat created, Delete/Accept screen.

## Anatomy of Spring Ring: How Attackers Masquerade as Internal Support

The Spring Ring campaigns are a coordinated operation that relies on impersonating corporate IT structures. Attackers can drop their lures into a victim's primary communication channel using external Microsoft Teams accounts.

### The Discovery: Spotting the Pattern

Our investigation into this activity began after the release of a new [detection suite for Microsoft Teams](https://www.paloaltonetworks.com/blog/security-operations/cortex-itdr-cyber-threats-in-microsoft-teams-and-their-detection/). By monitoring these alerts, we identified a suspicious pattern of chat creation across multiple tenants. Further investigation into these alerts led to the initial discovery of 26 distinct identities approaching targets across different organizations.

### The Initial Hook: Crafted Personas and Domains

The attack begins with creating a Microsoft Teams chat using identities designed to mirror legitimate internal support units. The attackers opt for professional, urgency-focused display names such as help desk, IT assistance or support staff.

To strengthen the impression of legitimacy, the attackers operate from external .onmicrosoft[.]com tenants. These are meant to resemble legitimate corporate infrastructure. They are used by attackers to provision Microsoft 365 tenants. The subdomains are controlled by the adversaries.

Threat actors frequently abuse or subvert legitimate products for malicious purposes. This does not indicate that the product itself is flawed or compromised. Unit 42 has no evidence of any compromise or vulnerability within Microsoft's product related to this campaign.

Here are examples of these subdomains:

  * ithelp@InternalSystemsDaily[.]onmicrosoft[.]com
  * HelpDesk@ITProtectionDepartment[.]onmicrosoft[.]com
  * itadmin@MandatoryNetworkMonitoring[.]onmicrosoft[.]com
  * Internal@InternalUSAHelpDeskIT[.]onmicrosoft[.]com
  * ithelpdesk@CertifiedUpdateNetwork[.]onmicrosoft[.]com



In some instances, the actors went beyond generic role names and used specific names to increase the perceived authenticity of the technician on the other end of the line:

  * patrick[..]@infrastructureopsdesk.onmicrosoft[.]com
  * robert[..]@systemdeploymentcenter.onmicrosoft[.]com
  * clara[..]@systemsupportoperations.onmicrosoft[.]com



Names have been partially redacted because the attackers used specific names of legitimate industry personnel. The use of these names does not indicate a compromise of their accounts.

After the chat is created, the attacker initiates a voice call (the vishing element) to coerce the victim. After establishing a connection with what the victim believes is their own IT department, the attacker guides targeted employees through the steps to grant them remote control or execute malicious payloads.

### The Scale of Spring Ring

Our telemetry reveals that these attackers often make several attempts — including leaving voicemails — before establishing a connection. We observed the attackers engaging victims in calls that varied in duration:

  * Many calls last only a few seconds or they are missed by the victim as the attacker cycles through targets
  * Successful calls often last between 10 and 15 minutes



Figure 2 shows several vishing attempts made by the same attacker identity on six different targets, with different conversation durations.

![A screenshot of a table showing attacker call logs. Columns include Attacker Identity, Display Name, IP, and Call Duration. All Attacker Identities and Display Names are the same, with an IP address from Mullvad. Call Duration includes completed calls, missed calls, and voicemail, with times listed in hours, minutes, and seconds.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-30780-186248-2.png)Figure 2. Examples of an attacker initiating calls with different targets, and different time durations.

The reach of these campaigns is significant:

  * **More than 10 tenants were attacked** : We observed the campaigns targeting many organizations across different industries
  * **More than 150 targets were approached** : The attackers contacted more than 150 individual employees
  * **Persistent activity** : We tracked the campaigns since January 2026 over a period of several weeks. According to our telemetry, these campaigns were active up until April 2026.



## Technical Deep Dive: The RMM and Custom Dropper Combination

Once the attacker establishes trust through the initial vishing call, the Spring Ring campaigns transitioned into a technical execution phase designed to gain a permanent foothold. We provide a detailed analysis of two campaigns (Campaign A and Campaign B) that both began with a Microsoft Teams lure. They then diverged in their payload delivery, tool complexity and post-compromise activities.

Figure 3 shows the full attack flow of the two campaigns' attack methods.

![a diagram illustrating Spring Ring attack flow, starting with creating a chat lure in Microsoft Teams. Two campaigns are shown: Campaign A leads to convincing the target to download RMM tools, then downloading obfuscated PowerShell-based malware. Campaign B involves convincing the target to download malware from a cloud endpoint, leading to persistence and environment enumeration, followed by attempted lateral movement using PetitPotam.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-32993-186248-3.png)Figure 3. Full attack flow of the two Spring Ring campaigns.

### Campaign A: From Support Tools to Obfuscated Payloads

In Campaign A, the attacker used a bring-your-own-tool approach, luring the victim to execute legitimate RMM software. The attacker posing as a technician walked the employee through launching built-in Windows tools like Quick Assist or downloading third-party RMM software. Once the RMM tool ran, the attacker could request remote control of the victim’s machine.

After gaining remote control, the attacker performed a series of basic enumeration commands to gain information on the host and domain. We observed them executing:

whoami /groups net group /dom

12 | whoami /groupsnet group /dom  
---|---  
  
After confirming the environment's value, the attacker pivots to payload delivery. The attacker used a PowerShell command line to download an obfuscated PowerShell-based remote access Trojan (RAT) from the attacker-controlled domain, san-sid[.]com. This malware used variable manipulations and arithmetic obfuscation designed to evade automated security analysis and sandbox detection.

By leveraging advanced AI and pattern-matching algorithms, we were able to de-obfuscate the RAT. We started by stripping away anti-analysis bloat from the code that was used to cause a time-out for deobfuscation tools.

The actual payload is a tiny, nine-line command and control (C2) stager. The script disables Antimalware Scan Interface (AMSI) via the amsiInitFailed flag and executes a test scan to verify the bypass. Upon verification, the script encrypts host data and beacons out to san-sid[.]com to download and execute further payloads.

Figure 4 shows a snippet of the obfuscated PowerShell-based RAT.

![A screenshot of the obfuscated PowerShell-based RAT code snippet with various programming elements such as loops, conditional statements, and arithmetic operations. The code includes variable names, mathematical calculations, and logical operators.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-35140-186248-4.png)Figure 4. A snippet from the obfuscated PowerShell-based RAT.

This campaign was blocked by automated Cortex XDR Agent protections during the malware's execution phase.

### Campaign B: The Tailored Cloud Execution Chain

The second campaign used a more customized delivery method. During the vishing call, the attacker directed the victim to a cloud endpoint. The attackers tailored the cloud infrastructure and filenames to match the targeted organization and the specific user, for example:

<company_name>-org-filters-update-<victim_name>.s3.us-west-2.amazonaws[.]com

When the victim clicked a link containing their own company's name and downloaded <company_name>-org-filters-update-<victim_name>[.]exe, it triggered an execution chain:

  1. **Staging and persistence** : The executable moved itself to the \Temp\ directory and spawned copies (e.g., vhlp-*.exe and scnr-*.exe) as a persistence mechanism
  2. **Browser hijacking** : The malware launched a hidden, headless instance of Microsoft Edge, and the attackers wrote to the disk and sideloaded an Edge extension
  3. **Lateral movement and authentication coercion** : The attackers used Python (C:\ProgramData\IntegrityData\python.exe) to initiate a lateral movement sequence: 
     1. **SMB scanning** : Initiated port 445 traffic targeting internal servers
     2. **NTLM authentication** : Generated NTLM traffic targeting the organization's DC
     3. **PetitPotam exploitation** : The attacker attempted a PetitPotam attack to coerce the DC into authenticating back to an attacker-controlled machine. This NTLM relay attack was designed to grant the attacker domain-level privileges



After attempting to coerce the DC, the attacker's domain-takeover attempt was blocked by [Unit 42 Managed Detection and Response](https://www.paloaltonetworks.com/unit42/respond/managed-detection-response).

### Summary of Tactical Divergence

By comparing the two campaign paths, we can better understand the diversity of threats targeting collaboration platforms. Table 1 compares the campaigns' specific methods of attack.

**Feature** | **Campaign A** | **Campaign B**  
---|---|---  
**Initial Lure** | Microsoft Teams vishing | Microsoft Teams vishing  
**Primary Delivery** | RMM tools | Tailored hosting infrastructure executables  
**Stealth Mechanism** | Obfuscated PowerShell | Headless Microsoft Edge and sideloaded extension  
**Lateral Movement** | Basic enumeration only | PetitPotam NTLM relay  
  
Table 1. Comparing the two campaigns’ methods.

This comparison highlights an important point for defenders. A simple vishing hook can lead to either a standard malware infection, or to a serious domain-level breach if the attacker pivots to payload delivery.

## Identifying Teams Impersonation and Identity-Based Anomalies

Recognizing campaigns like Spring Ring requires a strategy of profiling external and internal entity behaviors. The attackers behind these campaigns operate within a legitimate ecosystem, so detection hinges on identifying small anomalies in how external identities interact with your organization.

### Profiling the Identity

The first line of defense is recognizing the markers of the external actor. Our research into these campaigns highlights several consistent patterns:

  * **Spoofed domain naming** : Attackers mostly use external .onmicrosoft[.]com tenants that include keywords like internal, certified, network or infrastructure to project authority
  * **Persona mimicry** : They use professional display names, like IT help desk or admin, to increase the perceived authenticity of the technician during vishing calls
  * **Infrastructure red flag** : The source IP addresses for these connections often originate from commercial VPN services to mask the attacker's true location



### Behavioral Metrics of the Interaction

Our researchers were able to identify key markers of Spring Ring activity by analyzing the metadata of these interactions, despite the deceptive nature of the attacker’s initial lures:

  * **The chat-to-call ratio** : A primary indicator is the rapid transition from a 1:1 chat request to an unsolicited audio call
  * **Call curation profiling** : Attackers cycle through targets quickly. We observed call patterns ranging from 30-second initial attempts to 15-minute sessions.
  * **Multiple approaches** : These actors demonstrate high operational volume, often approaching 5-6 identities within a matter of minutes using one of their spoofed identities



### Recognizing Post-Compromise Behavior

Upon a successful compromise, we observed endpoint activity characterized by:

  * Atypical execution of RMM tools by users who do not require remote support
  * Access to unknown links, including cloud storage URLs or other file hosting servers that victims might be lured to access



Organizations can identify the Spring Ring lifecycle before the attacker transitions from a chat to a domain-level attack, by profiling these signals, the origin of the tenant and the subsequent attack flow.

Figure 5 shows one example of a Cortex alert on a new suspicious conversation created in Microsoft Teams. This alert is based on behavioral and metadata analysis of a newly created chat.

![A screenshot of a Cortex alert in an application interface. The alert is titled "An external user started a conversation in Microsoft Teams with a suspicious user or chat name." It shows details like the description of the incident, occurrence count, and affected assets. The description mentions a user creating a Microsoft Teams chat with two users in the organization. Status and assignee fields are visible, but not filled. Other tabs include Overview, Resolution, War Room, and XDR Analytics.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-37791-186248-5.png)Figure 5. Example of a Cortex alert on the creation of a suspicious chat in Microsoft Teams.

## Conclusion

The Spring Ring campaigns demonstrate a strategic pivot in social engineering, where attackers move beyond email phishing to enterprise collaboration tools. Attackers turn an important productivity tool into a conduit for domain-level exploitation, masquerading as internal help desk personnel through vishing calls.

This activity highlights an important shift in the security landscape. Identity is now a primary perimeter, and the platforms we rely on for daily communication are being weaponized.

Looking forward, attackers might further refine their ability to operate within SaaS ecosystems. These platforms are not just an initial access vector, they contain sensitive documentation, workflows and communication logs that could allow an adversary to advance their attack chain.

Our analysis of the Spring Ring operation reinforces several key lessons:

  * **Trusted SaaS applications are not inherently safe** : Attackers exploit the confidence that employees place in communications platforms
  * **Attack vectors are simple and scalable** : By using seemingly legitimate external tenants and professional vishing lures, attackers can target hundreds of employees across many industries with minimal friction
  * **Adaptability is key** : Attackers are evolving their methods, shifting from basic credential harvesting to human-led lateral movement



As these threats evolve, organizations must prioritize user education regarding unsolicited external communication across collaboration platforms. Robust behavioral monitoring can help identify identity-based anomalies before they escalate to lateral movement.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) identify known domains and URLs associated with this activity as malicious.
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) can help prevent the execution of both known and unknown malware through Behavioral Threat Protection and machine learning powered by the Local Analysis module. Beyond stopping initial execution via malicious droppers, Cortex XDR actively halts post-exploitation activities, such as PetitPotam NTLM relay attacks, before adversaries can achieve lateral movement.
  * [Cortex Cloud Identity Threat Detection ](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-identity-security/what-is-cortex-cloud-identity-security) can help deliver real-time protection against identity-based threats across cloud providers, IdPs, and SaaS applications. Using advanced behavioral analytics on real-time telemetry, ITDR baselines access patterns to detect anomalies, track complex attack chains—such as the Spring Ring lifecycle and trigger automated responses to contain compromised credentials.
  * The [Cortex Advanced Email Security](https://www.paloaltonetworks.com/cortex/advanced-email-security) module can help extend the power of the Cortex platform into cloud-hosted email environments, providing a scalable, AI-driven layer for detection, investigation, and response. By automatically stopping email threats and malicious communications across enterprise environments, it provides seamless protection across one of your most vulnerable attack vectors.
  * [Idira Threat Detection and Response](https://docs.cyberark.com/detect-and-respond/latest/en/content/get-started/what-is-detect-and-respond.htm) can help enable security teams to counter identity-based attacks targeting Idira Next Generation Identity (NGI) Platform and the identities it secures. Using near real-time detection, powered by CORA AI, and leveraging Idira’s visibility across multiple contexts (like PAM, authentication, SSO, cloud, endpoints, browsers, and more), Idira ITP can apply automated, tailored non-disruptive in-session response to contain and minimize potential identity-based threats.
  * [Idira Endpoint Privilege Manager ](https://docs.cyberark.com/epm/latest/en/content/intro/introduction.htm)can help enable enterprises to reduce risk, satisfy compliance, and streamline operations. It helps implement least privilege via policy-driven elevation and removal of standing admin rights, and blocks risky actions, such as execution of unvetted applications and access to memory of other processes, while providing audit-ready evidence and unified identity governance. Automation and consolidation improve efficiency and support Zero Trust strategies, strengthening security without slowing the business.
  * [Idira Privileged Access Management ](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1)can help unify privileged access across human, machine, and agentic identities to secure cloud access across multi-cloud environments. Building on proven PAM, it delivers centralized secrets management alongside modern controls like Just-in-Time access and Zero Standing Privileges. This enforces consistent least-privilege security across on-premises, cloud, and SaaS targets.
  * [Idira Secure Infrastructure Access ](https://docs.cyberark.com/pam-self-hosted/latest/en/content/pasimp/integrate-with-sia.htm)can help enforce Zero Standing Privileges (ZSP) through Just-in-Time (JIT) provisioning which grants temporary, tightly scoped access only as needed. Backed by continuous session recording and real-time command monitoring, SIA can detect high risk actions before an attacker compromises critical systems.



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

### Attacker Identities Used in Vishing Attempts – Generic

  * helpcenter@ithelpcenter365[.]onmicrosoft[.]com
  * helpdesk@itprotectiondepartment[.]onmicrosoft[.]com
  * helpdesk@newsystemmaintenance[.]onmicrosoft[.]com
  * helpdesk@officedesk365[.]onmicrosoft[.]com
  * helpdesk@officesecures[.]onmicrosoft[.]com
  * helpdesk@tbcsschid[.]onmicrosoft[.]com
  * internal@internalusahelpdeskIT[.]onmicrosoft[.]com
  * it_assistance@teams0137[.]onmicrosoft[.]com
  * it@infrastructurefirewall[.]onmicrosoft[.]com
  * itadmin@mandatorynetworkmonitoring[.]onmicrosoft[.]com
  * itassistant@bilelonellc[.]onmicrosoft[.]com
  * ithelp@certifiednetworksec[.]onmicrosoft[.]com
  * ithelp@internalsystemsdaily[.]onmicrosoft[.]com
  * ithelp@itprotectiondepartment[.]onmicrosoft[.]com
  * ithelp@mandatorynetworkmonitoring.onmicrosoft[.]com
  * ithelpdesk@certifiedupdatenetwork[.]onmicrosoft[.]com
  * support@bilelonellc[.]onmicrosoft[.]com



### Attacker Identities Used in Vishing Attempts – Usernames

Names have been partially redacted to protect the users associated with accounts that were impersonated by the attackers.

  * andreas[..]@idigitalserviceoperation.onmicrosoft[.]com
  * andrew[..]@hapsinfrastructureops.onmicrosoft[.]com
  * brandon[..]@devsitoperationhub.onmicrosoft[.]com
  * brian[..]@appssupportsys.onmicrosoft[.]com
  * christopher[..]@adevpsitplatformops.onmicrosoft[.]com
  * christopher[..]@itplatformops.onmicrosoft[.]com
  * christopher[..]@helpaphelpitinfraops.onmicrosoft[.]com
  * clara[..]@systemsupportoperations.onmicrosoft[.]com
  * daniel[..]@opsnetsupportit.onmicrosoft[.]com
  * daniel[..]@apsitsupporthub.onmicrosoft[.]com
  * emily[..]@apsitechsupportdesk.onmicrosoft[.]com
  * eric[..]@appopshelp.onmicrosoft[.]com
  * henrik[..]@enterpriseoperationsflo.onmicrosoft[.]com
  * james[..]@helpitsupportcore.onmicrosoft[.]com
  * james[..]@itcoretechhelp.onmicrosoft[.]com
  * jonathan[..]@itservicedesk.onmicrosoft[.]com
  * justin[..]@techopshelpsupp.onmicrosoft[.]com
  * kevin[..]@itopsupportdesk.onmicrosoft[.]com
  * kevin[..]@netopsdeskhelp.onmicrosoft[.]com
  * leon[..]@netcorevdapp.onmicrosoft[.]com
  * lucas[..]@applicationoperationsunit.onmicrosoft[.]com
  * martin[..]@syslanevdapp.onmicrosoft[.]com
  * matthew[..]@supportopsupp.onmicrosoft[.]com
  * michael[..]@appdeploymentservices.onmicrosoft[.]com
  * michael[..]@infratechopsdesk.onmicrosoft[.]com
  * michael[..]@itopsdeskhelp.onmicrosoft[.]com
  * patrick[..]@infrastructureopsdesk.onmicrosoft[.]com
  * rachel[..]@ioseccloudsupport.onmicrosoft[.]com
  * rebecca[..]@infrastructureopsservice.onmicrosoft[.]com
  * robert[..]@systemdeploymentcenter.onmicrosoft[.]com
  * ryan[..]@apstechopsdeskdev.onmicrosoft[.]com
  * ryan[..]@helpssupportcloudops.onmicrosoft[.]com
  * ryan[..]@seqhelpitsuppnetops.onmicrosoft[.]com
  * sarah[..]@secinfrahelpdesk.onmicrosoft[.]com
  * sarah[..]@apsscloudopsdesk.onmicrosoft[.]com
  * sarah[..]@helpitdevsupportops.onmicrosoft[.]com
  * sarah[..]@itdevsupportops.onmicrosoft[.]com
  * scott[..]@cloudinfrastr.onmicrosoft[.]com
  * steven[..]@ittechnologyopsitdesk.onmicrosoft[.]com
  * thomas[..]@networkoperationsec.onmicrosoft[.]com
  * thomas[..]@seqapsitsupportops.onmicrosoft[.]com



### Infrastructure Used in Vishing Attempts (VPNs and Proxies)

  * 193.32.248[.]251
  * 193.138.7[.]142
  * 185.65.134[.]209
  * 178.130.47[.]46
  * 5.181.3[.]106
  * 2.56.172[.]214
  * 185.234.67[.]53
  * 45.8.157[.]185
  * 80.66.72[.]215
  * 136.0.20[.]6
  * 185.213.155[.]226
  * 185.155.99[.]161
  * 92.118.232[.]131
  * 45.182.189[.]80
  * 185.65.133[.]51
  * 45.33.22[.]47



### Malicious Files From Post-Compromise Activity (Campaign A)

  * **SHA256 hash:** 24ab9fe5d5be62d3bf055a0ca4508e8bca2996b6d78649dce8145d8a27bc1c5b (obfuscated PowerShell payload)



File description: Obfuscated PowerShell RAT dropper downloaded via Invoke-WebRequest

  * **URL:** hxxps[:]//san-sid[.]com/owners



Description: URL hosting obfuscated PowerShell payload used as RAT dropper

### Cortex XDR Alerts and MITRE ATT&CK® Techniques

Table 2 lists the Cortex XDR alerts and the associated MITRE ATT&CK techniques these alerts detect.

**Alert Name** | **Alert Source** | **MITRE ATT &CK Technique**  
---|---|---  
External user started a Microsoft Teams conversation | XDR Analytics, Identity Threats | [Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)  
External user created a Microsoft Teams conversation with suspicious operations | XDR Analytics, Identity Threats | [Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)  
External user added a link to a Microsoft Teams chat | XDR Analytics, Identity Threats | [Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)  
External user call via Microsoft Teams | XDR Analytics, Identity Threats | [Phishing: Spearphishing Voice (T1566.004)](https://attack.mitre.org/techniques/T1566/004/)  
Rare process execution by user | XDR Analytics, UEBA | [User Execution (T1204)](https://attack.mitre.org/techniques/T1204/)  
Rare process execution in organization | XDR Analytics, UEBA | [User Execution (T1204)](https://attack.mitre.org/techniques/T1204/)  
Multiple rare process executions in organization | XDR Analytics, UEBA | [User Execution (T1204)](https://attack.mitre.org/techniques/T1204/)  
A process connected to an atypical rare cloud resource | XDR Analytics | [Exfiltration Over Web Service: Exfiltration to Cloud Storage (T1567.002)](https://attack.mitre.org/techniques/T1567/002/)  
Uncommon local scheduled task created | XDR Analytics | [Scheduled Task/Job (T1053)](https://attack.mitre.org/techniques/T1053/)  
A browser was forced to load an extension using a special command-line argument | XDR Analytics | [Software Extensions: Browser Extensions (T1176.001)](https://attack.mitre.org/techniques/T1176/001/)  
Uncommon browser extension loaded | XDR Analytics | [Software Extensions: Browser Extensions (T1176.001)](https://attack.mitre.org/techniques/T1176/001/)  
SMB traffic from non-standard process | XDR Analytics | [Network Service Discovery (T1046)](https://attack.mitre.org/techniques/T1046/)  
Rare NTLM access by user to host | XDR Analytics, UEBA | [Use Alternate Authentication Material (T1550)](https://attack.mitre.org/techniques/T1550/)  
Unusual Encrypting File System Remote Protocol call (EFSRPC) to domain controller | XDR Analytics, UEBA | [Forced Authentication (T1187)](https://attack.mitre.org/techniques/T1187/) [Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay (T1557.001)](https://attack.mitre.org/techniques/T1557/001/)  
Possible authentication coercion to a sensitive server | XDR Analytics, UEBA | [Forced Authentication (T1187)](https://attack.mitre.org/techniques/T1187/) [Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay (T1557.001)](https://attack.mitre.org/techniques/T1557/001/)  
Possible Distributed File System Namespace Management (DFSNM) abuse | XDR Analytics | [Forced Authentication (T1187)](https://attack.mitre.org/techniques/T1187/) [Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay (T1557.001)](https://attack.mitre.org/techniques/T1557/001/)  
Possible authentication coercion | XDR Analytics, UEBA | [Forced Authentication (T1187)](https://attack.mitre.org/techniques/T1187/) [Adversary-in-the-Middle: LLMNR/NBT-NS Poisoning and SMB Relay](https://attack.mitre.org/techniques/T1557/001/)[ (T1557.001)](https://attack.mitre.org/techniques/T1557/001/)  
  
Table 2. Cortex XDR alerts and MITRE techniques.

## Additional Resources

  * [When “Hi, This Is IT” Comes Through Microsoft Teams](https://unit42.paloaltonetworks.com/microsoft-teams-phishing/) – Unit 42, Palo Alto Networks
  * [Cortex ITDR: Cyber Threats in Microsoft Teams and Their Detection](https://www.paloaltonetworks.com/blog/security-operations/cortex-itdr-cyber-threats-in-microsoft-teams-and-their-detection/) – Palo Alto Networks
  * [Quick, You Need Assistance!](https://fieldeffect.com/blog/quick-you-need-assistance) – Fieldeffect
  * [PetitPotam](https://github.com/topotam/PetitPotam) – by topotam on GitHub
  * [APT29 Phishing Attacks via Microsoft Teams: Tactics, Techniques, and Prevention](https://insidersecurity.co/apt29-midnight-blizzard-phishing-attacks-via-microsoft-teams-tactics-techniques-and-prevention/) – InsiderSecurity
  * [Phishing Threat Trends Report [PDF]](https://www.knowbe4.com/hubfs/Phishing_Threat_Trends_Report_Vol7_en-US.pdf) – KnowBe4
  * [Cross‑tenant helpdesk impersonation to data exfiltration: A human-operated intrusion playbook](https://www.microsoft.com/en-us/security/blog/2026/04/18/crosstenant-helpdesk-impersonation-data-exfiltration-human-operated-intrusion-playbook/#risk-to-enterprise-environments) – Microsoft



Back to top

### Tags

  * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")
  * [Payload](https://unit42.paloaltonetworks.com/tag/payload/ "payload")
  * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")
  * [Remote Access Trojan](https://unit42.paloaltonetworks.com/tag/remote-access-trojan/ "Remote Access Trojan")
  * [Spoof](https://unit42.paloaltonetworks.com/tag/spoof/ "Spoof")
  * [Vishing](https://unit42.paloaltonetworks.com/tag/vishing/ "Vishing")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Perturbation Probing: A New Diagnostic for the Fragility of LLM Safety ](https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/ "Perturbation Probing: A New Diagnostic for the Fragility of LLM Safety")

### Table of Contents

  *   * Executive Summary
  * Overview: The Trust Gap
    * SaaS Applications: The New High-Value Target
    * The Evolution of Collaboration Attacks
  * Anatomy of Spring Ring: How Attackers Masquerade as Internal Support
    * The Discovery: Spotting the Pattern
    * The Initial Hook: Crafted Personas and Domains
    * The Scale of Spring Ring
  * Technical Deep Dive: The RMM and Custom Dropper Combination
    * Campaign A: From Support Tools to Obfuscated Payloads
    * Campaign B: The Tailored Cloud Execution Chain
    * Summary of Tactical Divergence
  * Identifying Teams Impersonation and Identity-Based Anomalies
    * Profiling the Identity
    * Behavioral Metrics of the Interaction
    * Recognizing Post-Compromise Behavior
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Indicators of Compromise
    * Attacker Identities Used in Vishing Attempts – Generic
    * Attacker Identities Used in Vishing Attempts – Usernames
    * Infrastructure Used in Vishing Attempts (VPNs and Proxies)
    * Malicious Files From Post-Compromise Activity (Campaign A)
    * Cortex XDR Alerts and MITRE ATT&CK® Techniques
  * Additional Resources



### Related Articles

  * [ Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "article - table of contents")
  * [ The npm Threat Landscape: Attack Surface and Mitigations (Updated July 15) ](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/ "article - table of contents")
  * [ OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat ](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)