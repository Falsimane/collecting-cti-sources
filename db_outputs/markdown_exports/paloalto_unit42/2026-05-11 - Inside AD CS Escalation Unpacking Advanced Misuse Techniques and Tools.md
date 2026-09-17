# Inside AD CS Escalation: Unpacking Advanced Misuse Techniques and Tools

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/
- **Date :** 2026-05-11

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Inside AD CS Escalation: Unpacking Advanced Misuse Techniques and Tools

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 14 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Stav Setty](https://unit42.paloaltonetworks.com/author/stav-setty/)
    * [Tom Fakterman](https://unit42.paloaltonetworks.com/author/tom-fakterman/)
    * [Shachar Roitman](https://unit42.paloaltonetworks.com/author/shachar-roitman/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:May 11, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Active Directory](https://unit42.paloaltonetworks.com/tag/active-directory/)
    * [AD CS attacks](https://unit42.paloaltonetworks.com/tag/ad-cs-attacks/)
    * [Certificate template](https://unit42.paloaltonetworks.com/tag/certificate-template/)
    * [Certipy](https://unit42.paloaltonetworks.com/tag/certipy/)
    * [ESC1](https://unit42.paloaltonetworks.com/tag/esc1/)
    * [Fighting Ursa](https://unit42.paloaltonetworks.com/tag/fighting-ursa/)
    * [Microsoft](https://unit42.paloaltonetworks.com/tag/microsoft/)
    * [PKI](https://unit42.paloaltonetworks.com/tag/pki/)
    * [Shadow credentials](https://unit42.paloaltonetworks.com/tag/shadow-credentials/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/?pdf=download&lg=en&_wpnonce=252a1929a6 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/?pdf=print&lg=en&_wpnonce=252a1929a6 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Inside%20AD%20CS%20Escalation:%20Unpacking%20Advanced%20Misuse%20Techniques%20and%20Tools&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Factive-directory-certificate-services-exploitation%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Factive-directory-certificate-services-exploitation%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Factive-directory-certificate-services-exploitation%2F&title=Inside%20AD%20CS%20Escalation:%20Unpacking%20Advanced%20Misuse%20Techniques%20and%20Tools "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Factive-directory-certificate-services-exploitation%2F&text=Inside%20AD%20CS%20Escalation:%20Unpacking%20Advanced%20Misuse%20Techniques%20and%20Tools "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Factive-directory-certificate-services-exploitation%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Inside%20AD%20CS%20Escalation:%20Unpacking%20Advanced%20Misuse%20Techniques%20and%20Tools%20https%3A%2F%2Funit42.paloaltonetworks.com%2Factive-directory-certificate-services-exploitation%2F "Share in Mastodon")



## Executive Summary

Active Directory Certificate Services (AD CS) is a foundational component of Windows enterprise infrastructure, responsible for managing public key infrastructure (PKI) and issuing certificates that enable authentication and encryption across networks. Despite its critical role in the enterprise identity infrastructure, AD CS is often undermined by insecure default configurations and design complexities, resulting in exploitable attack surfaces. Due to misconfigured templates and overly permissive enrollment rights, AD CS has emerged as a high-impact, under-monitored vector for privilege escalation and unauthorized identity impersonation in modern environments.

Unlike traditional vulnerability exploitation, AD CS attacks rarely rely on zero-day vulnerabilities or malware. Instead, adversaries misuse native certificate issuance to impersonate privileged accounts, escalate privileges and establish persistence. Unit 42 observations and industry reporting show that these weaknesses are actively exploited by both financially motivated [ransomware groups](https://thedfirreport.com/2025/04/28/navigating-through-the-fog/) and [state-sponsored actors](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a).

We provide a technical deep-dive into advanced AD CS exploitation, including certificate template misconfigurations and shadow credential misuse. Our findings present a comprehensive breakdown of the attacker’s toolkit and their evolving operational behaviors.

By studying behavioral analytics, event log correlation and linking offensive techniques to actionable telemetry, it is possible to create dynamic and comprehensive detection strategies. Our detection methods reveal patterns and methods that extend beyond traditional signature-based approaches. We aim to provide defenders with unique ways to uncover stealthy AD CS abuse and address a persistent gap in enterprise security.

[Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr?_gl=1*13pmp8e*_ga*NzQyNjM2NzkuMTY2NjY3OTczNw..*_ga_KS2MELEEFC*MTY2OTczNjA2MS4zMS4wLjE2Njk3MzYwNjEuNjAuMC4w) and [XSIAM](https://www.paloaltonetworks.com/resources/datasheets/cortex-xsiam-aag) customers are protected from this activity with [Cortex User Entity Behavior Analytics (UEBA](https://www.paloaltonetworks.com/cyberpedia/what-is-user-entity-behavior-analytics-ueba)) and [Cortex Cloud Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Premium-Documentation/What-is-Cortex-Cloud-Identity-Security).

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Active Directory](https://unit42.paloaltonetworks.com/tag/active-directory/), [Fighting Ursa, ](https://unit42.paloaltonetworks.com/tag/fighting-ursa/)[Microsoft](https://unit42.paloaltonetworks.com/tag/microsoft/)**  
---|---  
  
## Introduction: The Critical Role (and Risk) of AD CS

AD CS is the backbone of enterprise public key infrastructure ([PKI](https://learn.microsoft.com/en-us/windows/win32/seccertenroll/public-key-infrastructure)). At its core is the certificate authority ([CA](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview)), the service responsible for issuing and managing [digital certificates](https://support.microsoft.com/en-us/office/digital-signatures-and-certificates-8186cd15-e7ac-4a16-8597-22bd163e8e96). These certificates are cryptographic identity cards that prove that a user, device or service is what it claims to be. Organizations rely on AD CS for:

  * **User authentication** : Certificates enable single sign-on and client authentication across services
  * **Service authentication** : Internal services and domain controllers validate identity using PKI
  * **Encryption** : Certificates underpin secure communications within and outside the enterprise



The same capabilities that make AD CS indispensable also create risk. To manage certificate issuance, AD CS uses [certificate templates](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/certificate-template-concepts), which define who can request certificates, what they can be used for, and the permissions required. When misconfigured, these templates may grant long-lived authentication or privileged access, effectively providing complete control over a network.

Certificate issuance is an expected administrative function that often appears as normal network activity. This makes AD CS a powerful adversarial tool, because exploitation frequently evades detection.

In the AD CS issuance workflow, the CA issues certificates according to the policies defined in certificate templates, and users and services use the resulting certificates for authentication and encryption. Figure 1 illustrates this flow.

![Diagram titled "Server Side AD CS Infrastructure" showing three sections. First section: "Certificate Authority" with an icon of servers, labeled "issues certificates." Second section: "Certificate Templates" with a document icon, labeled "define policies." Third section: "Issued Certificates" with a certificate icon, labeled "provide authorization and encryption." Below, a "Client Side" section shows icons of a person and a database labeled "User" and "SQL Server," with "consume certificates.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-50860-180347-1.png)Figure 1. PKI architecture showing CA → Templates → Certificates → Users and Services.

For additional background on AD CS fundamentals, see [Detecting AD CS Abuse](https://www.paloaltonetworks.com/blog/security-operations/detecting-active-directory-certificate-services-abuse-with-cortex-xdr/).

## Ongoing Exploitation and Blind Spots

Despite years of research highlighting AD CS risks, certificate services remain a significant attack surface. Key contributing factors include:

  * **Widespread misconfigurations** : Organizations often deploy AD CS with default or overly permissive settings.
  * **Complexity breeding mistakes** : Consistently securing each configuration surface is a daunting task when combined with the need to manage dozens of certificate templates, enrollment policies and delegated permissions. Because certificate services support critical authentication workflows, security teams can be hesitant to modify legacy templates or tighten permissions, for fear of disrupting production systems.
  * **Limited monitoring** : Few tools natively detect certificate misuse.



Recent incident response investigations show attackers leveraging AD CS to escalate from low-privileged accounts to full domain dominance. Exploiting certificate services is no longer rare; it has become a standard step in sophisticated intrusions.

In August 2024, [Rapid7](https://www.rapid7.com/blog/post/2024/08/12/ongoing-social-engineering-campaign-refreshes-payloads/) described a social engineering campaign in which attackers attempted to escalate privileges by exploiting [CVE-2022-26923](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26923). This vulnerability allows a lower-privileged user to elevate their privileges by acquiring a certificate from the AD CS. The attackers tried to exploit it by dropping and executing a file named update6.exe.

Figure 2 shows a Cortex XDR alert that is triggered when update6.exe attempts to exploit CVE-2022-26923. The alert highlights a mismatch between the requesting machine and the issued certificate’s identity — a behavioral signal that is consistent with certificate-based privilege escalation. These inconsistencies can reveal AD CS abuse even when no malware signatures are present.

![Cortex XDR alert with diagram showing a file named update6.exe. Text indicates a machine certificate was issued with a mismatch, indicating abuse related to CVE-2022-26923. Some identifying information is redacted. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-52968-180347-2.png)Figure 2. An alert on the detection and prevention of CVE-2022-26923, as seen in Cortex XDR.

## Phase Breakdown: How AD CS Attacks Work

The AD CS exploitation lifecycle typically encompasses five phases:

  1. **Initial access** : Compromising low-privileged accounts via phishing, credential theft or other vectors
  2. **Discovery** : Enumerating CA servers, certificate templates, enrollment permissions and account keys
  3. **Exploitation** : Misusing misconfigured templates to request certificates or register cryptographic keys for privileged accounts
  4. **Privilege escalation and lateral movement** : Using certificates or keys with public key cryptography for initial authentication ([PKINIT](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pkca/d0cf1763-3541-4008-a75f-a577fa5e8c5b)) to request [Kerberos tickets](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview) and impersonate privileged users
  5. **Persistence** : Maintaining access through [shadow credentials](https://specterops.io/blog/2021/06/17/shadow-credentials-abusing-key-trust-account-mapping-for-account-takeover/), key trust misuse and certificate renewal



Figure 3 illustrates this sequence of operations, demonstrating how AD CS acts as a force multiplier that turns a single compromised account into long-term access across an enterprise.

![Flowchart of the Active Directory CS attack chain in five stages: Initial Access \(Compromise user\), Discovery \(Enumerate templates\), Exploitation \(Request certificate\), Privilege Escalation \(Use certificate to Kerberos\), and Persistence \(Shadow credentials, renewals\). Arrows indicate the sequence from Initial Access to Persistence.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-55781-180347-3.png)Figure 3: AD CS attack lifecycle diagram.

## Deep Dive: Key AD CS Attack Techniques​​

The key adversarial tactics, techniques and procedures (TTPs) that target AD CS include certificate template misconfigurations and shadow credential abuse.

### **Certificate Template Misuse and Misconfigurations**

Certificate templates define how AD CS issues certificates, including who can request them and what privileges the certificates grant. Exploiting misconfigurations in certificate templates is one of the most common ways that attackers escalate privileges.

Common misconfigurations include:

  * **Low-privileged users allowed to enroll in high-privileged templates:** This effectively lets attackers mint authentication certificates for accounts that they should not control
  * **Dangerous template flags enabled:** For example, the “Supply in the request” option ([ENROLLEE_SUPPLIES_SUBJECT](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-crtd/1192823c-d839-4bc3-9b6b-fa8c53507ae1)) lets the requester define the certificate subject in the [certificate signing request](https://learn.microsoft.com/en-us/azure/key-vault/certificates/create-certificate-signing-request?tabs=azure-portal) (CSR), enabling impersonation
  * **Broad group enrollment rights:** Assigning rights to groups like Domain Users or Authenticated Users allows any authenticated user to abuse certificate enrollment



Figure 4 highlights a dangerous template configuration that allows the requester to supply the subject, enabling account impersonation.

![A screenshot titled "Vulnerable template Properties" displaying settings tabs. The "Subject Name" tab is open, showing options. A selection is highlighted by a red box around "Supply in the request.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-57991-180347-4.png)Figure 4. Template setting with the “Supply in the request” (ENROLLEE_SUPPLIES_SUBJECT) specification enabled.

#### ESC1 Walkthrough

In their 2021 [Certified Pre-Owned: Abusing Active Directory Certificate Services [PDF]](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) whitepaper, SpecterOps researchers Will Schroeder and Lee Christensen identified and categorized eight primary AD CS escalation techniques, designated ESC1 through ESC8. Since then, several additional ESC techniques have been discovered.

ESC1 stands out as the most consistently observed and widely utilized escalation method. This technique exploits template vulnerabilities, enabling low-privileged users to request certificates as high-privileged accounts.

An ESC1 attack can be conducted when a certificate template is configured with the following settings:

  * Low-privileged users have enrollment rights
  * Requesters can specify a [subject alternative name (SAN)](https://learn.microsoft.com/en-us/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/add-san-to-secure-ldap-certificate) (ENROLLEE_SUPPLIES_SUBJECT)
  * Manager approval is disabled
  * No authorized signatures are required
  * The enhanced key usage ([EKU](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ppsec/651a90f3-e1f5-4087-8503-40d804429a88)) allows authentication — for example, Client Authentication



A typical ESC1 attack begins with an adversary enumerating available certificate templates using tools such as Certify or Certipy to identify misconfigurations. Once a vulnerable template is discovered, the attacker submits a certificate request impersonating a high-privileged account. The issued certificate can then be used to authenticate to services or obtain Kerberos tickets as the target account, resulting in privilege escalation.

Figure 5 shows output from Certipy, a Python tool used to enumerate certificate templates and exploit misconfigurations, highlighting flags that enable the ESC1 attack path.

![A screenshot of a code snippet displaying JSON configuration related to a Vulnerable template with different sections highlighted in red. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-60099-180347-5.png)Figure 5. Example of Certipy output highlighting ESC1 flags such as ENROLLEE_SUPPLIES_SUBJECT, Client Authentication and Manager Approval.

### **Shadow Credentials and Key Trust Exploitation**

Attackers often turn to shadow credentials to gain stealthy, persistent access, authenticating as a target user without ever needing their password. Unlike traditional credential theft, shadow credentials leverage cryptographic keys that are linked directly to user accounts. This method enables long-term access that is resistant to common defenses like password resets or account lockouts.

A central enabler of this attack is [Key Trust](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/deploy/#trust-types), a modern authentication mechanism used by [Windows Hello for Business](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/) and smartcards. Key Trust leverages PKINIT in Kerberos to allow users to authenticate to Active Directory using public key certificates instead of passwords.

The [msDS-KeyCredentialLink](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/f70afbcc-780e-4d91-850c-cfadce5bb15c) attribute stores public keys associated with a user account and is intended to support legitimate, key-based authentication. However, attackers can misuse this attribute to register their own key credentials as high-privileged accounts, effectively creating a shadow credential.

#### How Shadow Credentials Work

  1. **Key registration** : The attacker adds key credentials to the target account’s msDS-KeyCredentialLink attribute, usually through AD manipulation or elevated access
  2. **PKINIT authentication** : Using the key, the attacker requests Kerberos tickets without needing to provide the account password



Even if the account password is changed or previously issued certificates are revoked, the attacker can continue authenticating as the target account.

#### Integration With Other AD CS Exploits

Shadow credentials are particularly powerful when combined with certificate template misuse, such as ESC1. For example, an attacker might:

  * Exploit a misconfigured template to request a certificate for a privileged account
  * Use the certificate to elevate privileges and gain domain admin access
  * Register a key in msDS-KeyCredentialLink for persistent, passwordless access
  * Continue lateral movement or maintain stealthy persistence without creating new accounts or relying on stolen passwords



This combination of template exploitation and shadow credential misuse represents one of the most persistent and hard-to-detect attack paths in modern Windows environments.

## The Attacker Toolkit for AD CS Exploitation

A growing set of open-source tools makes AD CS misuse more accessible. Table 1 lists commonly-used tools for AD CS exploitation and their primary use cases.

**Tool** | **Primary Use Case** | **Notes**  
---|---|---  
[Certify](https://github.com/GhostPack/Certify) | Enumerates and exploits AD CS templates | C# tool, supports multiple ESC-style attack paths  
[Certipy](https://github.com/ly4k/Certipy) | Certificate template exploitation and AD enumeration | Python-based, covers ESC1-ESC16 attack paths  
[PKINIT tools](https://github.com/dirkjanm/PKINITtools) | Misuse PKINIT for Kerberos Ticket Granting Ticket (TGT) requests | Supports certificate-based Kerberos authentication  
[Whisker](https://github.com/eladshamir/Whisker) | Shadow credentials and Key Trust misuse | C# tool, manipulates the msDS-KeyCredentialLink attribute  
[pyWhisker](https://github.com/ShutdownRepo/pywhisker) | Shadow credentials and Key Trust misuse | Python equivalent of the Whisker tool  
  
Table 1. Common AD CS attack tools.

Each of the tools listed plays a distinct role in the AD CS attack chain. Certify and Certipy are the primary utilities for enumerating and exploiting AD CS objects such as vulnerable certificate templates and CAs. For example, a common first step in AD CS attacks is the use of Certify to enumerate CAs in an Active Directory environment, as Figure 6 shows.

![The image shows a computer screen with a program called "Certify" in ASCII art text. Below, instructions are given to find certificate authorities using the search base "CN=Configuration,DC=env12,DC=local". It displays a list under "Root CAs" with details such as certificate thumbprints and serial numbers, along with date and time stamps.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-62147-180347-6.png)Figure 6. Using Certify to enumerate CAs in the Active Directory environment.

The operational use of Certipy has been observed in ransomware activity. The [DFIR Report](https://thedfirreport.com/2025/04/28/navigating-through-the-fog/) identified an exposed toolkit associated with the [Fog ransomware](https://malpedia.caad.fkie.fraunhofer.de/details/win.fog) group, highlighting the role of AD CS abuse in modern ransomware operations. Figure 7 shows a Cortex XDR alert detecting Certipy LDAP queries against certificate templates and other AD CS objects, illustrating reconnaissance activity during an AD CS attack.

![The image is a diagram displaying a cybersecurity alert in Cortex XDR. The alert involves "LDAP AD CS Enumeration via Attack Tool" with the command `certipy.exe`. The path shows a flow from "certipy.exe" to a triangle containing an exclamation mark, which indicates a warning or critical point. Descriptions and potential sources of the alert are on the left. Some identifying information is redacted. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-64361-180347-7.png)Figure 7. Detection and prevention of Certipy, as seen in Cortext XDR.

PKINITtools extends misuse into Kerberos by leveraging certificate-based authentication to request TGTs. For persistence, Whisker and pyWhisker specialize in shadow credential and Key Trust attacks, enabling stealthy long-term access by manipulating the msDS-KeyCredentialLink attribute. Figure 8 demonstrates the use of pyWhisker to add malicious key credentials to a user account for persistence.

![Command line interface displaying text related to managing certificates and keys. It involves generating and updating credentials. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-67240-180347-8.png)Figure 8. Using pyWhisker to add key credentials to a user account.

The availability of these open-source tools lowers the barrier of entry to complex AD CS exploitation. What once required deep expertise can now be executed by moderately skilled attackers, a shift that has accelerated adoption of these techniques across the threat landscape.

## Conclusion

As organizations harden traditional attack surfaces, adversaries increasingly turn to AD CS as a stealthy and under-monitored path to privilege escalation and persistence. Neglecting certificate services leaves a critical security gap, allowing serious exploitation methods to remain effectively unguarded.

To combat the evolution of AD CS compromise techniques and the expansion of attack toolkits, defenders must maintain secure certificate template configurations, monitor unusual certificate and key activity and maintain visibility across authentication paths. Strong configuration hygiene, combined with behavioral detection, enables organizations to identify and respond to stealthy AD CS exploitation before it results in privilege escalation or persistent access.

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

### Cortex XDR and XSIAM

[Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) are designed to prevent the execution of known malicious malware and prevent the execution of unknown malware using Behavioral Threat Protection and machine learning based on the Local Analysis module.

### Cortex User Entity Behavior Analytics (UEBA)

[Cortex User Entity Behavior Analytics (UEBA](https://www.paloaltonetworks.com/cyberpedia/what-is-user-entity-behavior-analytics-ueba)) helps to detect authentication and credential-based threats by analyzing user activity from multiple data sources including endpoints, network firewalls, Active Directory, identity and access management solutions, and cloud workloads. Cortex builds behavioral profiles of user activity over time with machine learning.

By comparing new activity to past activity, peer activity and the expected behavior of the entity, Cortex detects anomalous activity that may be indicative of credential-based attacks.

### Cortex Cloud Identity Security

[Cortex Cloud Identity Security encompasses ](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Premium-Documentation/What-is-Cortex-Cloud-Identity-Security)Cloud Infrastructure Entitlement Management (CIEM), Identity Security Posture Management (ISPM), Data Access Governance (DAG) as well as Identity Threat Detection and Response (ITDR) and provides clients with the necessary capabilities to improve their identity-related security requirements.

By providing visibility into identities and their permissions within cloud environments, Cortex Cloud Identity Security helps to accurately detect misconfigurations and unwanted access to sensitive data, and provides real-time analysis of usage and access patterns.

If you think you may have been compromised or have an urgent matter, get in touch with the[ Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107
  * South Korea: +82.080.467.8774



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

  * [Threat Actor Insights: Navigating Through The Fog](https://thedfirreport.com/2025/04/28/navigating-through-the-fog/) – The DFIR Report
  * [Certipy - AD CS Attack & Enumeration Toolkit](https://github.com/ly4k/Certipy) – GitHub
  * [Certify: Active Directory certificate abuse](https://github.com/GhostPack/Certify) – GitHub
  * [Certifried: Active Directory Domain Privilege Escalation (CVE-2022–26923)](https://research.ifcr.dk/certifried-active-directory-domain-privilege-escalation-cve-2022-26923-9e098fe298f4) – Oliver Lyak, Institut For Cyber Risk
  * [Fog Malware Family](https://malpedia.caad.fkie.fraunhofer.de/details/win.fog) – Malpedia
  * [What is Active Directory Certificate Services?](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview) – Microsoft Learn
  * [Detecting Active Directory Certificate Services Abuse with Cortex XDR™](https://www.paloaltonetworks.com/blog/security-operations/detecting-active-directory-certificate-services-abuse-with-cortex-xdr/) – Blog, Palo Alto Networks
  * [Certified Pre-Owned: Abusing Active Directory Certificate Services [PDF]](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) – Will Schroeder and Lee Christensen, SpecterOps
  * [Shadow Credentials: Abusing Key Trust Account Mapping for Account Takeover](https://posts.specterops.io/shadow-credentials-abusing-key-trust-account-mapping-for-takeover-8ee1a53566ab) – SpecterOps
  * [Fighting Ursa Archives](https://unit42.paloaltonetworks.com/tag/fighting-ursa/) – Unit 42, Palo Alto Networks
  * [Fluttering Scorpius](https://unit42.paloaltonetworks.com/threat-actor-groups-tracked-by-palo-alto-networks-unit-42/#:~:text=Wholesale%20and%20Retail-,Fluttering%20Scorpius,-Also%20Known%20As) – Unit 42, Palo Alto Networks



## Appendix A: Detection Strategies: Beyond Signatures

Attackers exploit native PKI and Active Directory features in ways that can blend into normal operations. Detecting AD CS misuse requires more than just monitoring individual events; effective detection involves:

  * Correlating multiple event types
  * Tracking unusual patterns
  * Applying a baseline for user activity



Table 2 lists the specific Windows Event IDs essential for detecting AD CS-related anomalies and providing the necessary telemetry for threat hunting operations.

### Key Event IDs

**Log** | **Event ID** | **Description**  
---|---|---  
Security | 4886 | Certificate services received a certificate request  
Security | 4887 | Certificate services approved a certificate request and issued a certificate  
Security | 4898 | Certificate services loaded a template  
Security | 5136 | A directory service object was modified  
Security | 4768/4769 | Kerberos TGT and service ticket requests  
Microsoft-Windows-LDAP-Client | 30 | LDAP client search  
Microsoft-Windows-ActiveDirectory_DomainService | 1644 | LDAP server search  
  
Table 2. Key Event IDs for AD CS monitoring.

**Note:** To maximize detection capabilities, all relevant audit policies must be enabled and configured correctly, using resources such as the [Cortex XDR AD CS Event Setup](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-3.x-Documentation/Additional-setup-for-Active-Directory-Certificate-Services-ADCS-events) documentation.

### LDAP Activity Monitoring

Lightweight Directory Access Protocol ([LDAP](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/ldap/what-is-ldap)) queries are a critical indicator of reconnaissance and exploitation in AD CS attacks. Attackers often enumerate certificate templates, group memberships, and msDS-KeyCredentialLink attributes via LDAP before attempting privilege escalation. High volumes of queries, repeated requests for sensitive objects, or unusual patterns from accounts that don’t usually perform administrative lookups should be treated as suspicious.

Correlating LDAP activity with certificate issuance events or directory modifications can help detect adversarial activity early, including ESC-style template misuse and shadow credential registration.

Monitoring the following LDAP queries is instrumental in identifying adversarial reconnaissance and the initial stages of AD CS infrastructure enumeration:

  * objectClass=pKICertificateTemplate
  * objectCategory=CN=PKI-Enrollment-Service
  * msDS-KeyCredentialLink attributes



Tools like Certify and Certipy perform broad and repeated LDAP queries across users, groups and certificate templates, making this activity a strong early warning signal.

Figure 9 highlights an LDAP event where an attacker queried for sensitive AD CS attributes such as msDS-KeyCredentialLink.

![The image shows a screenshot of an Event 1644 from Active Directory Domain Service. The event details include an internal client event.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-69620-180347-9.png)Figure 9. Windows Event 1644 showing an LDAP query targeting the msDS-KeyCredentialLink attribute.

An example from recent years of an attacker using this technique in the wild is described in a 2025 advisory from the U.S. Cybersecurity and Infrastructure Security Agency (CISA) which describes a [cyberespionage campaign](https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-141a) attributed to [Fighting Ursa](https://unit42.paloaltonetworks.com/tag/fighting-ursa/) (also known as APT28, Fancy Bear, Forest Blizzard). In this campaign, the threat actor used tools such as [ADExplorer](https://learn.microsoft.com/en-us/sysinternals/downloads/adexplorer) and Certipy to collect certificate services and Active Directory data from target environments prior to further exploitation.

Figure 10 shows an alert detecting ADExplorer enumerating AD CS objects. This type of behavior, including mass queries of certificate templates and AD objects, can indicate early-stage reconnaissance and warrants investigation.

![Cortex XDR alert for "Possible LDAP Enumeration Tool Usage." It includes sections labeled "Description," "Source," and "Module," with text partially masked. On the right, a diagram features a circular element connected to a red triangle with an exclamation mark, indicating an alert. "ADExplorer.exe" and "CGO" are displayed below the diagram. Some identifying information is redacted. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-72149-180347-10.png)Figure 10. Screenshot from a Cortex XDR alert on the detection and prevention of ADExplorer.exe.

### Template Misuse – ESC Attacks

Monitoring template usage helps detect attacks across the ESC1–ESCn spectrum, where overly permissive templates are exploited. Event ID 4898 indicates that a certificate template was loaded. Signs of misuse include:

  * msPKI-RA-Signature = 0: No authorized signatures required
  * CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT: Requester can specify the SAN in the CSR
  * msPKI-Enrollment-Flag = 0x0 (0): Manager approval is disabled



Together, these conditions point to misconfigurations that attackers turn into privilege escalation paths.

#### Monitoring Certificate Service Activity

The following Event IDs can reveal unusual request patterns:

  * 4886: Received certificate request
  * 4887: Certificate issued



For example, a low-privileged account requesting certificates from high-privileged templates may be an indication of ESC-style template misuse. To differentiate legitimate activity from attacks, track enrollment rights, SAN usage and EKU flags.

#### Directory Modifications and Shadow Credentials

To detect shadow credential attacks, focus on unexpected modifications to the msDS-KeyCredentialLink attribute. Given that attackers use this attribute to silently add their own credentials to privileged accounts, even small changes should be investigated. Event ID 5136 records changes to directory objects.

Figure 11 shows a directory modification event indicating a potential shadow credential attack.​

![Screenshot of a Microsoft Windows security auditing event log for event ID 5136. The active directory domain service is "env12.local" with various distinguished names \(DNs\) and a GUID partially blurred. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/word-image-74725-180347-11.png)Figure 11. Event 5136 detecting a change in the msDS-KeyCredentialLink attribute.

#### Kerberos Ticket Requests and Lateral Movement

Monitoring Kerberos TGT and service ticket events can help detect potential privilege escalation and lateral movement attempts – Event IDs 4768 and 4769. When correlated with suspicious certificate issuance or key registration activity, PKINIT authentication requests can reveal attackers leveraging stolen or shadow credentials to impersonate users without triggering password alerts.

## Appendix B: Cortex XDR/XSIAM Alerts on AD CS Activity

Table 3 outlines the Cortex XDR/XSIAM alerts that detect AD CS-related malicious behaviors across multiple attack stages.

**Alert Name** | **Alert Source** | **MITRE ATT &CK Technique**  
---|---|---  
Vulnerable certificate template loaded | XDR Analytics BIOC, Identity Analytics | Steal or Forge Authentication Certificates (T1649)  
Suspicious certificate template modification | XDR Analytics BIOC, Identity Analytics | Steal or Forge Authentication Certificates (T1649)  
Key credential attribute modification | XDR Analytics BIOC, Identity Analytics | Modify Authentication Process (T1556)  
PKINIT TGT authentication request | XDR Analytics BIOC, Identity Analytics | Use Alternate Authentication Material (T1550)  
LDAP AD CS Enumeration via Attack Tool | XDR Analytics BIOC, Identity Analytics | Account Discovery (T1087)  
Discovery of misconfigured certificate templates using LDAP | XDR Analytics BIOC | File and Directory Discovery (T1083)  
A user queried AD CS objects via LDAP | XDR Analytics BIOC, Identity Analytics | Steal or Forge Authentication Certificates (T1649)  
A suspicious process queried AD CS objects via LDAP | XDR Analytics BIOC, Identity Analytics | Steal or Forge Authentication Certificates (T1649)  
A user certificate was issued with a mismatch | XDR Analytics BIOC, Identity Analytics | Steal or Forge Authentication Certificates (T1649)  
A machine certificate was issued with a mismatch | XDR Analytics BIOC, Identity Analytics | Valid Accounts: Domain Accounts (T1078.002)  
Unusual CertLog Remote File Write | XDR Analytics BIOC, Identity Analytics | Steal or Forge Authentication Certificates (T1649)  
Privileged certificate request via certificate template | XDR Analytics BIOC, Identity Analytics | Valid Accounts: Domain Accounts (T1078.002)  
PowerShell pfx certificate extraction | XDR Analytics BIOC | Unsecured Credentials: Credentials In Files (T1552.001)  
Deletion of AD CS certificate database entries | XDR Analytics BIOC, Identity Analytics | Indicator Removal (T1070)  
Suspicious Certutil AD CS contact | XDR Analytics BIOC | Steal or Forge Authentication Certificates (T1649)  
Certutil pfx parsing | XDR Analytics BIOC | Data from Local System (T1005)  
The CA policy EditFlags was queried | XDR Analytics BIOC | Valid Accounts (T1078)  
A suspicious process enrolled for a certificate | XDR Analytics BIOC | Steal or Forge Authentication Certificates (T1649)  
A user created a pfx file for the first time | XDR Analytics BIOC, Identity Analytics | Unsecured Credentials: Credentials In Files (T1552.001)  
A user modified the CA audit policy | XDR Analytics BIOC, Identity Analytics | Impair Defenses: Disable Windows Event Logging (T1562.002)  
User set insecure CA registry setting for global SANs | XDR Analytics BIOC, Identity Analytics | Impair Defenses: Disable or Modify Tools (T1562.001)  
A user logged on to multiple workstations via Schannel | XDR Analytics, Identity Analytics | Steal or Forge Authentication Certificates (T1649)  
  
Table 3. Cortex XDR/XSIAM alerts on AD CS activity.

Back to top

### Tags

  * [Active Directory](https://unit42.paloaltonetworks.com/tag/active-directory/ "Active Directory")
  * [AD CS attacks](https://unit42.paloaltonetworks.com/tag/ad-cs-attacks/ "AD CS attacks")
  * [Certificate template](https://unit42.paloaltonetworks.com/tag/certificate-template/ "certificate template")
  * [Certipy](https://unit42.paloaltonetworks.com/tag/certipy/ "certipy")
  * [ESC1](https://unit42.paloaltonetworks.com/tag/esc1/ "ESC1")
  * [Fighting Ursa](https://unit42.paloaltonetworks.com/tag/fighting-ursa/ "Fighting Ursa")
  * [Microsoft](https://unit42.paloaltonetworks.com/tag/microsoft/ "Microsoft")
  * [PKI](https://unit42.paloaltonetworks.com/tag/pki/ "PKI")
  * [Shadow credentials](https://unit42.paloaltonetworks.com/tag/shadow-credentials/ "shadow credentials")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/ "Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution")

### Table of Contents

  *   * Executive Summary
  * Introduction: The Critical Role (and Risk) of AD CS
  * Ongoing Exploitation and Blind Spots
  * Phase Breakdown: How AD CS Attacks Work
  * Deep Dive: Key AD CS Attack Techniques​​
    * Certificate Template Misuse and Misconfigurations
      * ESC1 Walkthrough
    * Shadow Credentials and Key Trust Exploitation
      * How Shadow Credentials Work
      * Integration With Other AD CS Exploits
  * The Attacker Toolkit for AD CS Exploitation
  * Conclusion
    * Cortex XDR and XSIAM
    * Cortex User Entity Behavior Analytics (UEBA)
    * Cortex Cloud Identity Security
  * Additional Resources
  * Appendix A: Detection Strategies: Beyond Signatures
    * Key Event IDs
    * LDAP Activity Monitoring
    * Template Misuse – ESC Attacks
      * Monitoring Certificate Service Activity
      * Directory Modifications and Shadow Credentials
      * Kerberos Ticket Requests and Lateral Movement
  * Appendix B: Cortex XDR/XSIAM Alerts on AD CS Activity



### Related Articles

  * [ How We Added WebAuthn to a Browser-Based RDP Client ](https://unit42.paloaltonetworks.com/webauthn-added-to-browser-based-rdp/ "article - table of contents")
  * [ 2026 World Cup: Discussing The World’s Biggest Game’s Attack Surface ](https://unit42.paloaltonetworks.com/fifa-world-cup-attack-surface/ "article - table of contents")
  * [ Microsoft WSUS Remote Code Execution (CVE-2025-59287) Actively Exploited in the Wild (Updated November 3) ](https://unit42.paloaltonetworks.com/microsoft-cve-2025-59287/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/)