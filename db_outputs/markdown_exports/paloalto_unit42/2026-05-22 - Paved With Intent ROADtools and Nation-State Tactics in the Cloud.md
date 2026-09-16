# Paved With Intent: ROADtools and Nation-State Tactics in the Cloud

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/
- **Date :** 2026-05-22

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")



[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Paved With Intent: ROADtools and Nation-State Tactics in the Cloud

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 14 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Bill Batchelor](https://unit42.paloaltonetworks.com/author/bill-batchelor/)
    * [Eyal Rafian](https://unit42.paloaltonetworks.com/author/eyal-rafian/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:May 22, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/)
    * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/)
    * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/)
    * [Microsoft graph API](https://unit42.paloaltonetworks.com/tag/microsoft-graph-api/)
    * [Midnight Blizzard](https://unit42.paloaltonetworks.com/tag/midnight-blizzard/)
    * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/)
    * [ROADtools](https://unit42.paloaltonetworks.com/tag/roadtools/)
    * [UTA0355](https://unit42.paloaltonetworks.com/tag/uta0355/)
    * [Void Blizzard](https://unit42.paloaltonetworks.com/tag/void-blizzard/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Paved%20With%20Intent:%20ROADtools%20and%20Nation-State%20Tactics%20in%20the%20Cloud&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Froadtools-cloud-attacks%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Froadtools-cloud-attacks%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Froadtools-cloud-attacks%2F&title=Paved%20With%20Intent:%20ROADtools%20and%20Nation-State%20Tactics%20in%20the%20Cloud "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Froadtools-cloud-attacks%2F&text=Paved%20With%20Intent:%20ROADtools%20and%20Nation-State%20Tactics%20in%20the%20Cloud "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Froadtools-cloud-attacks%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Paved%20With%20Intent:%20ROADtools%20and%20Nation-State%20Tactics%20in%20the%20Cloud%20https%3A%2F%2Funit42.paloaltonetworks.com%2Froadtools-cloud-attacks%2F "Share in Mastodon")



## Executive Summary

ROADtools is a publicly available toolkit for offensive and defensive security purposes that attackers have integrated into cloud attacks. The tool is designed to:

  * Enumerate Entra ID
  * Register devices in Entra ID
  * Acquire, exchange and manipulate Microsoft Entra ID tokens



[ROADtools](https://github.com/dirkjanm/ROADtools) is an open-source framework written in Python and built for red-teaming and research. It primarily targets the identity and authentication layers of Azure, and focuses on how accounts, applications and tokens operate in tenants.

To avoid detection, ROADtools operates through legitimate Microsoft APIs and can mimic typical traffic. Further defense evasion can be achieved by configuring request attributes such as user-agent strings. These capabilities have made ROADtools a valuable asset for attackers. Nation-state threat actors have used it in recent cloud intrusions for discovery, persistence and defense evasion. Attackers involved in a [targeted phishing campaign](https://www.volexity.com/blog/2025/04/22/phishing-for-codes-russian-threat-actors-target-microsoft-365-oauth-workflows/) in early 2025 used tooling that matches ROADtools' token management capabilities.

We provide an accessible overview of ROADtools, including how it evades detection and how nation-state threat actors and other adversaries misuse it. To aid defenders in protecting organizations against this threat, we also provide:

  * Straightforward hunting queries that can reveal ROADtools usage
  * Practical recommendations to detect and prevent the effectiveness of ROADtools within an environment



Palo Alto Networks customers are better protected from the threats described here through the following products and services:

  * [Cortex Cloud](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud)
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud) and [XSIAM](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud)
  * The [Unit 42 Cloud Security Assessment](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/), [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/), [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/)**  
---|---  
  
## Tool Overview

ROADtools is able to interact with Entra ID via legitimate APIs, and to customize user-agent strings — both of which help it to evade detection. The tool includes several modules — two of which we discuss in this article - and a set of shared libraries.

### The ROADrecon Module

The [roadrecon](https://github.com/dirkjanm/ROADtools/wiki/Getting-started-with-ROADrecon) module is designed for internal discovery and enumeration. It gathers organizational data and identity information from Entra ID (formerly Azure Active Directory), including:

  * Users
  * Groups
  * Roles
  * Devices
  * Service principals
  * Applications
  * Directory configurations



Results are stored in a local SQLite database that can be viewed through a custom web interface. This provides a graphical way to navigate the tenant and identify relationships or privileged objects that attackers could use for persistence or escalation. Figure 1 shows Entra ID Groups within the ROADrecon graphical web interface.

![A screenshot of the ROADrecon interface displays a menu on the left with options like Home, Users, and Administrative Units. The main area shows a list with headings: Name, Description, Group type, and Group source. The list includes groups such as "All Users" and others.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-336300-181397-1.png)Figure 1. Entra ID Groups in the ROADtools web interface.

The roadrecon module originally queried the Azure AD Graph API to enumerate Azure AD resources. However, Microsoft has stated the Azure AD Graph API is being retired and [all new or existing applications must migrate to Microsoft Graph API](https://urldefense.proofpoint.com/v2/url?u=https-3A__learn.microsoft.com_en-2Dus_graph_migrate-2Dazure-2Dad-2Dgraph-2Doverview&d=DwMGaQ&c=V9IgWpI5PvzTw83UyHGVSoW3Uc1MFWe5J8PTfkrzVSo&r=_lIJbiuLEsecGC88yMz56rH6l-Y5OB28uwt-Y9Xz4rE&m=yo6tyUYrspO2VsHW_5TInS8MihQ4I9VA6SKK-9L0Rys5ZHzIwKU7zl0xtE5SLfVs&s=POvA4ehlh4k_iOM9BqSgr926rWcBQqBtgmONdmyjf38&e=), which breaks a fundamental component of the original roadrecon functionality.

As of May 2026, an [msgraph branch](https://github.com/dirkjanm/ROADtools/tree/msgraph) exists in the official ROADtools Github repository but has not been updated since April 2025. Subsequent development has continued in a separate, [community-maintained fork](https://github.com/Tom2Byrne/ROADtools), where partial roadrecon functionality has been implemented using the Microsoft Graph API. This fragmentation means users might encounter inconsistent functionality, while attackers can still enumerate Entra ID accounts and resources, as described in the Discovery section below.

### The Token eXchange (roadtx) Module

The [roadtx](https://github.com/dirkjanm/ROADtools/wiki/ROADtools-Token-eXchange-\(roadtx\)) module facilitates token acquisition and exchange, enabling attackers to interact with Entra ID’s authentication endpoints. It supports several OAuth 2.0 and OpenID Connect authentication flows (sign-in methods), including:

  * Entering a device code from another device (device code flow)
  * Reusing a refresh token to get new access
  * Allowing an application to request access on behalf of a user (known as an on-behalf-of or [OBO flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow))



The output of roadtx is typically a set of OAuth 2.0 access and refresh tokens in JSON format, which can be used to authenticate against Microsoft cloud services. The roadtx module can be used to register devices with Entra ID, replay stolen tokens and manipulate token lifecycles. This capability allows attackers to persist in an environment and bypass multi-factor authentication (MFA).

Supporting both roadrecon and roadtx is roadlib, the library layer that handles low-level authentication and API requests. The roadlib module provides the core functionality for ROADtools. It abstracts much of Microsoft’s authentication complexity, allowing an attacker or researcher to script token requests and API calls without having to know every OAuth detail.

This module is flexible and can be pointed at different API endpoints, including custom or non-Microsoft endpoints. This feature makes ROADtools easy to adapt to other security tooling and enables it to target a wider range of authentication systems.

With the above functionality in mind, the rest of this article explains how adversaries leverage ROADtools to perform their operations and what defenders can do to protect against ROADtools.

## Threat Actor Usage and Industry Targeting

The use of ROADtools has evolved from a red-team utility to an attack tool. Industry reports illustrate that various nation-state threat actors are leveraging the tool to conduct malicious activity:

  * Early observation of a nation-state actor operationalizing the ROADtools framework came in late 2021, when [Microsoft reported on activity](https://www.microsoft.com/en-us/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/) by [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/) (aka Midnight Blizzard or APT29). The group’s campaigns began with highly targeted spear phishing to gain initial access. Cloaked Ursa subsequently leveraged ROADtools to conduct discovery and enumerate victims’ Azure AD (now Entra ID) environments.
  * Microsoft reported the Iranian state-sponsored threat actor [Curious Serpens](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2025/) (aka Peach Sandstorm, APT33) [using ROADtools in malicious operations](https://www.microsoft.com/en-us/security/blog/2023/09/14/peach-sandstorm-password-spray-campaigns-enable-intelligence-collection-at-high-value-targets/) in 2023. After gaining initial access through password spray attacks, the threat actor used tools, including ROADtools for internal discovery.~~~~
  * [Volexity reported in 2025 on a targeted](https://www.volexity.com/blog/2025/04/22/phishing-for-codes-russian-threat-actors-target-microsoft-365-oauth-workflows/) phishing campaign during which a state-affiliated threat actor, which it calls UTA0355, was able to register a rogue device with Entra ID. Attackers were able to acquire a new token with full access to the Microsoft Graph API. The tooling Volexity reported matched the roadtx module’s token management capabilities.



## MITRE ATT&CK® Tactics

MITRE ATT&CK provides a structured way to describe how attackers operate. Organizing findings by MITRE ATT&CK Tactics, Techniques and Procedures enables defenders to:

  * Map attacker behaviors to a common language
  * Compare those behaviors across intrusions
  * Prioritize detections and mitigations based on the actions attackers take



In the sections that follow, we reference specific MITRE techniques to show how ROADtools components enable those behaviors, including:

  * Persistence: [T1098.005](https://attack.mitre.org/techniques/T1098/) Account Manipulation – Device Registration
  * Defense Evasion: [T1550](https://attack.mitre.org/techniques/T1550/) Use Alternate Authentication Material
  * Discovery: [T1087](https://attack.mitre.org/techniques/T1087/) Account Discovery



### Persistence

Technique: T1098.005 Account Manipulation – Device Registration (Figure 2).

![Callout box showing a laptop with malware bug on the screen, accompanied by text stating, "By registering devices they control, attackers can create persistent access."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-339217-181397-2.png)Figure 2. MITRE ATT&CK technique T1098.005.

The ROADtools roadtx module can register new devices in Entra ID. Attackers [register or join devices](https://learn.microsoft.com/en-us/entra/identity/devices/overview) to gain a durable means of persistence through a controlled account. Registration allows a rogue device to appear as a legitimate object in the Entra ID device inventory. Depending on the Entra ID configuration, a registered or joined device may also enable attackers to bypass MFA and conditional access policies ([CAPs](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)).

To register a device using roadtx, an attacker must first obtain valid credentials. The attacker can then use these credentials with roadtx to authenticate via one of the supported authentication flows, to acquire an access token for the [Azure device registration service](https://learn.microsoft.com/en-us/entra/identity/devices/device-registration-how-it-works) (urn:ms-drs:enterpriseregistration.windows[.]net).

After authentication, the attacker runs roadtx again, which calls the Azure device registration API to create a new device entry. The roadtx module writes the device certificate and key to the local file system and registers the device in Entra ID. Note that roadtx has default values for some command parameters. Unless specified otherwise, the devices will be registered as:

  * OS: Windows
  * OS Version: 10.0.19041.928
  * Name: DESKTOP-<RANDOM 8 DIGITS>



While these default values can be useful for detection purposes, they are also simple to change. All defaults can be viewed by running roadtx device -h from the command line, or by viewing them in the [roadtx source code](https://github.com/dirkjanm/ROADtools/blob/master/roadtx/roadtools/roadtx/main.py).

Figure 3 shows how an attacker uses a previously acquired refresh token to authenticate to the Azure device registration service and register a new device with the name mydevice.

![Terminal window displaying commands for obtaining and saving tokens for 'mydevice' using 'roadtx,' a private key, and device ID starting. The process includes requesting a token from enterprise registration on a Windows network and saving a device certificate.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-341558-181397-3.png)Figure 3. An example of roadtx access token acquisition and device registration.

### Defense Evasion

Technique: T1550 Use Alternate Authentication Material (Figure 4).

![Callout box with an icon of a cloud with circuit lines and the biohazard symbol paired with text that reads, "roadtx turns stolen credentials into access that can bypass controls."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-344184-181397-4.png)Figure 4. MITRE ATT&CK technique T1550.

Attackers try to acquire tokens because those tokens let them access company data and cloud services on behalf of a user or service, often without triggering a new interactive sign-in, enabling activity that blends in with legitimate API usage. Tokens allow attackers to move laterally, copy data and obtain persistent access in a target environment, bypassing interactive controls like MFA.

By leveraging a Primary Refresh Token ([PRT](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token?tabs=windows-prt-issued%2Cbrowser-behavior-windows%2Cwindows-prt-used%2Cwindows-prt-renewal%2Cwindows-prt-protection%2Cwindows-apptokens%2Cwindows-browsercookies%2Cwindows-mfa)), an attacker can maintain access to cloud applications by silently obtaining new access tokens in the background, which are then used in subsequent API requests, eliminating the need for repeated logins. The roadtx prt command allows attackers to acquire such a PRT. Full details of the process for registering a device and PRT acquisition are [described by the ROADtools author](https://dirkjanm.io/phishing-for-microsoft-entra-primary-refresh-tokens/).

Using roadtx, attackers can automate the misuse of a stolen PRT. This automation involves performing the token exchange and API call workflows that are needed in order to acquire fresh user access tokens and to call services such as Microsoft Graph non-interactively. A single device-bound PRT compromise can provide an attacker with persistent, programmatic access across the tenant.

### **Discovery**

Technique: T1087 Account Discovery (Figure 5).

![Callout box with an icon of a face, followed by the text: "Once tokens are obtained, roadrecon can quickly translate them into actionable intelligence."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-346885-181397-5.png)Figure 5. MITRE ATT&CK technique T1087.

Attackers perform account discovery to map an environment, identify high-value accounts and find lateral movement or privilege escalation targets. Ongoing efforts within the ROADtools community to adopt the Microsoft Graph API have enabled continued use of roadrecon for account discovery.

To use roadrecon for discovery, attackers must first authenticate to acquire the refresh and access tokens that allow access to the Microsoft Graph API. The authentication must use a client ID that has the necessary permissions for all the Microsoft Graph API endpoints that they wish to enumerate.

The Microsoft Graph API version supports a new roadrecon command-line parameter -mg that points the code to the Microsoft Graph API to enumerate resources such as:

  * /users
  * /groups
  * /devices
  * /servicePrincipals
  * /applications



This enumeration enables attackers to harvest account names, devices, roles, group membership and service-principal metadata. These are written to the local SQLite database as previously noted.

Figure 6 below lists devices registered in Entra ID as shown in the ROADtools custom web interface. This example is from a test environment but serves to illustrate the ease of discovering resources in the environment. Note the OS Version 10.0.19041.928 circled in red. As described earlier, this is currently the default value that roadtx uses when registering a device, and is different than the OS version for the other hosts, making it a good indicator of ROADtools activity.

![A screenshot of the ROADReconf interface displaying a list of devices. Each entry includes columns for name, manufacturer, enabled status, model, operating system, and trust type. One entry is highlighted in red showing the OS version.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-350333-181397-6.png)Figure 6. ROADtools custom web interface.

## Defender Perspective

The discussion so far has focused on how adversaries can misuse ROADtools. It is equally important to understand what defenders can do in response. Preventive controls and active threat hunting offer organizations multiple opportunities to detect and disrupt these techniques.

### **Preventive Controls to Limit Token Misuse**

ROADtools is challenging for defenders to detect because it operates within expected behavior. It does not exploit buffer overflows or drop binaries onto hosts, but instead uses the authentication flows and APIs that organizations rely on every day. Implementing layered identity defenses can limit how attackers misuse ROADtools. Defenders should consider the following controls:

  * **Enable Entra ID token protection:** Enabling [token protection](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) reduces the value of stolen refresh tokens. Binding refresh tokens to a specific device (token protection/“client claims”) is one of the most direct ways to [prevent the replay or misuse of tokens](https://learn.microsoft.com/en-us/entra/identity/devices/protecting-tokens-microsoft-entra-id) obtained by roadtx. This makes it harder for adversaries to export and reuse tokens from other hosts.
  * **Restrict device code flow via conditional access:**[CAPs can restrict risky flows](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows), such as device code, where they are not needed. Attackers use roadtx to misuse [device code flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code) because it works well for script-based attacks. Blocking or restricting this flow to only trusted scenarios (like registered devices, trusted IP address ranges or specific apps) cuts off an attack path.
  * **Audit OAuth apps regularly:**[Auditing applications for delegated and application permissions](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions) that have been granted helps eliminate excessive privileges that attackers target. Attackers can use roadtx to obtain tokens for any registered app if permissions are in place. Custom or abandoned apps with overly broad Microsoft Graph, SharePoint or Exchange permissions are prime targets. A cloud security posture management (CSPM) or cloud-native application protection platform (CNAPP) solution can help defenders conduct regular reviews, to reduce the attack surface.
  * **Limit privilege exposure:** Even if an attacker manages to obtain a token, organizations can greatly reduce potential damage by using privileged identity management (PIM) or privileged access management (PAM) to limit standing privileges and conditional access to [require step-up authentication](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant). These measures enforce least privilege and minimize the impact of a compromised account.
  * **Correlate logs across multiple sources:** Detection and threat hunting depend on event correlation. Prepare for this by bringing Azure audit logs, [Microsoft Graph API activity logs](https://www.paloaltonetworks.com/blog/security-operations/detecting-threats-with-microsoft-graph-activity-logs/), sign-ins and Office 365 activity together into a security information and event management (SIEM) platform to provide the visibility needed to spot anomalous API usage.



These controls help prevent and detect common attack techniques and lay the groundwork for effective threat hunting. With these controls in place, defenders can more effectively search for suspicious token usage, authentication flows or discovery activity before they escalate into compromise.

An attacker using roadtx for authentication is using valid credentials. As such, defenders must establish a baseline of normal activity for that user or resource to understand whether a sign-in is malicious or legitimate.

Microsoft Entra ID Protection provides two important reports for this purpose:

  * [Risky sign-in reports](https://urldefense.proofpoint.com/v2/url?u=https-3A__portal.azure.com_-23view_Microsoft-5FAAD-5FIAM_SecurityMenuBlade_-7E_RiskySignIns&d=DwMGaQ&c=V9IgWpI5PvzTw83UyHGVSoW3Uc1MFWe5J8PTfkrzVSo&r=_lIJbiuLEsecGC88yMz56rH6l-Y5OB28uwt-Y9Xz4rE&m=4-qQhuKma8thzIZvlSLW8DmApFbwqnw0UZEso5tA_83yeyvOrEPIR7y-_WpUu-_w&s=WeVUppuI_j-zNq3KVx0nI6zG4QDE6YrFfDMfZIoGeM0&e=) surfaces attempted and successful user access activities where the legitimate owner might not have performed the sign-in
  * [Risky user reports](https://urldefense.proofpoint.com/v2/url?u=https-3A__portal.azure.com_-23view_Microsoft-5FAAD-5FIAM_SecurityMenuBlade_-7E_RiskyUsers&d=DwMGaQ&c=V9IgWpI5PvzTw83UyHGVSoW3Uc1MFWe5J8PTfkrzVSo&r=_lIJbiuLEsecGC88yMz56rH6l-Y5OB28uwt-Y9Xz4rE&m=4-qQhuKma8thzIZvlSLW8DmApFbwqnw0UZEso5tA_83yeyvOrEPIR7y-_WpUu-_w&s=CGePElKdqJQaLd4nVEmz6BKuHlgvB4LRKDdiCUgV7ag&e=) surfaces user accounts that might have been compromised (e.g., a leaked credential that was detected or the user signing in from an unexpected location in the absence of planned travel)



### Hunting ROADtools Activity

With preventive controls in place, the next step is to actively look for signs of misuse. Threat hunting in this context goes beyond reviewing alerts. It requires systematically searching for anomalous patterns in device joins and registrations, and for token issuance and Graph API calls that could indicate suspicious roadtx or roadrecon activity.

#### Device Registration

Start by looking for evidence that adversaries are running ROADtools to register or join devices into Entra ID. Inspect audit events that relate to device registration, highlighting which users or service principals initiated the action. The broader objective is to detect when an attacker attempts to establish persistence in Entra ID by creating and controlling unauthorized devices.

#### Token Misuse

Next, look for evidence of token misuse. We have discussed how roadtx and roadlib are designed to acquire and refresh tokens programmatically. To defenders, that activity looks different from a standard browser or app sign-in. These differences include:

  * Scripted user agents
  * Service principals authenticating outside of expected patterns
  * Automated sign-in behavior that doesn’t resemble human use



The goal is to flag when an attacker is misusing tokens to blend in with legitimate activity while running scripted, malicious roadtx commands against the tenant. For example, an attacker may run roadtx with a version of python-requests (a Python library that supports HTTP) that is not usually seen in an organization's environment. Or even simpler, sign-ins via Python might not be expected in an organization at all, or only from certain IP ranges.

#### Microsoft Graph API

Finally, look for evidence of attackers using roadrecon to access the Microsoft Graph API and enumerate users, groups, service principals, applications and devices. These discovery activities are not limited to ROADtools and can be performed directly through Microsoft Graph API calls using custom scripts or other tooling.

For defenders, the key is to watch Microsoft Graph API logs for bursty, repetitive queries against those endpoints. Legitimate administrators rarely perform these actions in bulk. Defenders must migrate any roadrecon detections that rely on Azure AD Graph activity logs to use Microsoft Graph activity logs instead.

## Conclusion

ROADtools is an example of the dual use of security tooling. Released as a framework to interact with Azure AD for offensive and defensive security purposes, attackers have adopted ROADtools as a platform for real-world intrusions against Microsoft cloud environments. We have seen how its features map to MITRE ATT&CK techniques, and identified the alignment with attacker tactics of persistence, defense evasion and discovery.

For defenders, the challenge lies in ROADtools’ use of legitimate APIs and authentication flows. ROADtools activity can easily blend into normal cloud operations. Identifying malicious use of this toolset requires careful attention to anomalies in user agents, IP addresses, activity type and Graph API usage. Mitigations like token protection, conditional access policies, cloud security audits and privileged identity management provide additional layers of defense.

### **Palo Alto Networks Protection and Mitigation**

Palo Alto Networks customers are better protected from the threats described here through the following products and services:

  * [Cortex Cloud endpoint protection](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection) can help protect organizations from threats expressed within this article. [Cortex Cloud 2.1 can](https://www.paloaltonetworks.com/blog/cloud-security/visibility-governance-automation/) detect and prevent malicious operations through the use of behavioral and AI enabled analytics to detect when cloud and container endpoints are targeted. Additionally, it can detect when cloud platform IAM policies associated with those targeted endpoints are being misused and alert teams when assets are vulnerable to these threats.
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) customers can use the hunting, investigation and detection queries below to identify potentially suspicious activity related to the threats discussed in this article. In addition, Cortex [Identity Threat Detection and Response (ITDR)](https://www.paloaltonetworks.com/resources/techbriefs/identity-threat-detection-and-response-module) can help in detecting authentication and credential-based threats by analyzing user activity from multiple data sources including endpoints, network firewalls, Active Directory, identity and access management solutions, and cloud workloads.
  * The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.



If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Hunting, Investigation and Detection Queries

The queries below are designed to help Palo Alto Networks customers hunt for, investigate, and identify potentially suspicious activity using Cortex XDR. Results returned by these queries should not be considered inherently malicious and require further analysis to determine their significance.

### Cortex XQL Queries

#### Device Registration

The XQL query below hunts for threat actors using ROADtools to register or join devices in Entra ID, focusing on audit events that reveal initiating identities and potential attempts to establish persistence through unauthorized device creation. Depending on the environment in which this is run and in what timeframe, the query could return a large set of results. A 24-hour timeframe spanning any suspicious activity is a good starting point. Look for results from unexpected or suspicious locations or identities. Also, look for any device names that do not conform to expected naming conventions in your organization.

dataset = cloud_audit_logs | fields _time, operation_name_orig, operation_name, operation_status, identity_type, identity_name, resource_type_orig, resource_sub_type_orig, referenced_resource_name, referenced_resource, caller_ip, caller_ip_asn_org, caller_ip_geolocation, user_agent, user_agent_data | filter operation_name_orig in ( "Add device", "Add registered owner to device", "Add registered user to device", "Register device") | filter identity_name = "Device Registration Service" or resource_type_orig = "Device Registration Service" | sort asc _time

12345678910111213141516 | dataset = cloud_audit_logs| fields _time,operation_name_orig, operation_name, operation_status,identity_type, identity_name,resource_type_orig, resource_sub_type_orig,referenced_resource_name, referenced_resource,caller_ip, caller_ip_asn_org, caller_ip_geolocation,user_agent, user_agent_data| filter operation_name_orig in ("Add device","Add registered owner to device","Add registered user to device","Register device")| filter identity_name = "Device Registration Service"or resource_type_orig = "Device Registration Service"| sort asc _time  
---|---  
  
#### Token Misuse

The following query looks for evidence of token misuse, as roadtx and roadlib generate authentication patterns that might differ from regular user sign-ins. Focus on anomalies like scripted user agents, unusual service principal activity, and automated sign-in behavior – such as unexpected Python-based access – that may indicate threat actors executing malicious actions.

dataset = cloud_audit_logs | fields _time, raw_log, operation_name_orig, operation_name, operation_status, identity_type, identity_name, resource_type_orig, resource_sub_type_orig, referenced_resource_name, referenced_resource, caller_ip, caller_ip_asn_org, caller_ip_geolocation, user_agent, user_agent_data | filter raw_log contains "Oauth Scope Info" | filter raw_log contains "Directory.ReadWrite.All" or raw_log contains "Device.ReadWrite.All" or raw_log contains "Application.ReadWrite.All" or raw_log contains "AuditLog.ReadWrite.All" or raw_log contains "Policy.ReadWrite.All" | filter lowercase(user_agent) contains "python" or lowercase(user_agent) contains "requests" or lowercase(user_agent) contains "urllib" or lowercase(user_agent) contains "curl" | sort asc _time

12345678910111213141516171819 | dataset = cloud_audit_logs| fields _time, raw_log,operation_name_orig, operation_name, operation_status,identity_type, identity_name,resource_type_orig, resource_sub_type_orig,referenced_resource_name, referenced_resource,caller_ip, caller_ip_asn_org, caller_ip_geolocation,user_agent, user_agent_data| filter raw_log contains "Oauth Scope Info"| filter raw_log contains "Directory.ReadWrite.All"or raw_log contains "Device.ReadWrite.All"or raw_log contains "Application.ReadWrite.All"or raw_log contains "AuditLog.ReadWrite.All"or raw_log contains "Policy.ReadWrite.All"| filter lowercase(user_agent) contains "python"or lowercase(user_agent) contains "requests"or lowercase(user_agent) contains "urllib"or lowercase(user_agent) contains "curl"| sort asc _time  
---|---  
  
#### Microsoft Graph API

The following XQL query looks for roadrecon activity by monitoring Microsoft Graph API logs for high-volume, repeated enumeration of users, groups and applications – behavior uncommon for legitimate administrators. We built the following hunt query to detect this enumeration pattern, revealing when a threat actor is systematically mapping out the directory. The API call threshold should be adjusted to values indicating outliers in your organization.

dataset = cloud_audit_logs | filter operation_name_orig contains "graph.microsoft.com/v1.0" or operation_name_orig contains "graph.microsoft.com/beta" | filter operation_name_orig contains "serviceprincipals" or operation_name_orig contains "applications" or operation_name_orig contains "devices" | filter lowercase(user_agent) contains "python" or lowercase(user_agent) contains "requests" or lowercase(user_agent) contains "urllib" or lowercase(user_agent) contains "curl" | bin _time span = 60m | alter time_bucket = format_timestamp("%Y-%m-%d %H00 UTC", _time) | comp count() as graphApiCalls by identity_name, user_agent, caller_ip, time_bucket | filter graphApiCalls > 100 // adjust to your organization | sort desc graphApiCalls

123456789101112131415 | dataset = cloud_audit_logs| filter operation_name_orig contains "graph.microsoft.com/v1.0"or operation_name_orig contains "graph.microsoft.com/beta"| filter operation_name_orig contains "serviceprincipals"or operation_name_orig contains "applications"or operation_name_orig contains "devices"| filter lowercase(user_agent) contains "python"or lowercase(user_agent) contains "requests"or lowercase(user_agent) contains "urllib"or lowercase(user_agent) contains "curl"| bin _time span = 60m| alter time_bucket = format_timestamp("%Y-%m-%d %H00 UTC", _time)| comp count() as graphApiCalls by identity_name, user_agent, caller_ip, time_bucket| filter graphApiCalls > 100 // adjust to your organization| sort desc graphApiCalls  
---|---  
  
## Indicators

User-Agent string in HTTP headers of network traffic:

  * roadtools
  * python-requests/<version>



## Additional Resources

  * [dirkjanm/ROADtools: A collection of Azure AD/Entra tools for offensive and defensive security purposes](https://github.com/dirkjanm/ROADtools) – GitHub
  * [Microsoft Graph Community Supported Fork for RoadRecon](https://github.com/Tom2Byrne/ROADtools) – GitHub
  * [Block authentication flows with Conditional Access policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows) – Microsoft
  * [Conditional Access: Grant](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant) – Microsoft
  * [How Token Protection Enhances Conditional Access Policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) – Microsoft
  * [How it works: Device registration - Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/devices/device-registration-how-it-works) – Microsoft
  * [Important Update: Azure AD Graph retirement](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/important-update-azure-ad-graph-retirement/4364990) – Microsoft
  * [Microsoft identity platform and the OAuth 2.0 device authorization grant flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code) – Microsoft
  * [Migrate your apps from Azure AD Graph to Microsoft Graph](https://learn.microsoft.com/en-us/graph/migrate-azure-ad-graph-overview) – Microsoft
  * [Protecting Tokens in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/devices/protecting-tokens-microsoft-entra-id) – Microsoft
  * [Review permissions granted to enterprise applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions) – Microsoft
  * [What is device identity in Microsoft Entra ID?](https://learn.microsoft.com/en-us/entra/identity/devices/overview) – Microsoft
  * [Understanding Primary Refresh Token (PRT) in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token) – Microsoft
  * [NOBELIUM targeting delegated administrative privileges to facilitate broader attacks](https://www.microsoft.com/en-us/security/blog/2021/10/25/nobelium-targeting-delegated-administrative-privileges-to-facilitate-broader-attacks/) – Microsoft Security
  * [Peach Sandstorm password spray campaigns enable intelligence collection at high-value targets](https://www.microsoft.com/en-us/security/blog/2023/09/14/peach-sandstorm-password-spray-campaigns-enable-intelligence-collection-at-high-value-targets/) – Microsoft Security
  * [Cloaked Ursa Archives](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/) – Palo Alto Networks Unit 42
  * [Detecting Threats with Microsoft Graph Activity Logs](https://www.paloaltonetworks.com/blog/security-operations/detecting-threats-with-microsoft-graph-activity-logs/) – Palo Alto Networks Unit 42
  * [Threat Brief: Escalation of Cyber Risk Related to Iran (Updated June 30)](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2025/) – Palo Alto Networks Unit 42
  * [Phishing for Codes: Russian Threat Actors Target Microsoft 365 OAuth Workflows](https://www.volexity.com/blog/2025/04/22/phishing-for-codes-russian-threat-actors-target-microsoft-365-oauth-workflows/) – Volexity



Back to top

### Tags

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Microsoft graph API](https://unit42.paloaltonetworks.com/tag/microsoft-graph-api/ "Microsoft graph API")
  * [Midnight Blizzard](https://unit42.paloaltonetworks.com/tag/midnight-blizzard/ "Midnight Blizzard")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")
  * [ROADtools](https://unit42.paloaltonetworks.com/tag/roadtools/ "ROADtools")
  * [UTA0355](https://unit42.paloaltonetworks.com/tag/uta0355/ "UTA0355")
  * [Void Blizzard](https://unit42.paloaltonetworks.com/tag/void-blizzard/ "Void Blizzard")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Tracking TamperedChef Clusters via Certificate and Code Reuse ](https://unit42.paloaltonetworks.com/tracking-tampered-chef-clusters/ "Tracking TamperedChef Clusters via Certificate and Code Reuse")

### Table of Contents

  *   * Executive Summary
  * Tool Overview
    * The ROADrecon Module
    * The Token eXchange (roadtx) Module
  * Threat Actor Usage and Industry Targeting
  * MITRE ATT&CK® Tactics
    * Persistence
    * Defense Evasion
    * Discovery
  * Defender Perspective
    * Preventive Controls to Limit Token Misuse
    * Hunting ROADtools Activity
      * Device Registration
      * Token Misuse
      * Microsoft Graph API
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Hunting, Investigation and Detection Queries
    * Cortex XQL Queries
      * Device Registration
      * Token Misuse
      * Microsoft Graph API
  * Indicators
  * Additional Resources



### Related Articles

  * [ Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "article - table of contents")
  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Iranian Cyber Threat Evolution: From MBR Wipers to Identity Weaponization ](https://unit42.paloaltonetworks.com/evolution-of-iran-cyber-threats/ "article - table of contents")



## Related Cloud Cybersecurity Research Resources

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026 #### [Novel Technique to Detect Cloud Threat Actor Operations ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026 #### [DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of automated detection. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Cloud_cybersecurity_research_Overview_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 14, 2026 #### [Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/ "cloud detection")
  * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/ "DevOps")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection")

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026 #### [Novel Technique to Detect Cloud Threat Actor Operations ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026 #### [DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of automated detection. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Cloud_cybersecurity_research_Overview_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 14, 2026 #### [Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/ "cloud detection")
  * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/ "DevOps")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection")

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026 #### [Novel Technique to Detect Cloud Threat Actor Operations ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of Azure OpenAI DNS resolution issue. Futuristic cityscape illustration with luminous structures and floating cloud elements, showcasing advanced technology and a dynamic, digitally enhanced environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/02_DNS_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 20, 2026 #### [DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)