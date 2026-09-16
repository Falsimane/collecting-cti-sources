# Identity Abuse Through Trusted Communication Channels

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/communication-channel-identity-risks/
- **Date :** 2026-08-20

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Identity Abuse Through Trusted Communication Channels

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 12 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Idira icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/idira_RGB_logo_Icon_Color-e1787069105644.png)Idira](https://unit42.paloaltonetworks.com/product-category/panw-idira/ "Idira")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Bill Batchelor](https://unit42.paloaltonetworks.com/author/bill-batchelor/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:August 20, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/)
    * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/)
    * [Malware](https://unit42.paloaltonetworks.com/tag/malware/)
    * [MFA](https://unit42.paloaltonetworks.com/tag/mfa/)
    * [Remote access software](https://unit42.paloaltonetworks.com/tag/remote-access-software/)
    * [Social engineering](https://unit42.paloaltonetworks.com/tag/social-engineering/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Identity%20Abuse%20Through%20Trusted%20Communication%20Channels&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcommunication-channel-identity-risks%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcommunication-channel-identity-risks%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcommunication-channel-identity-risks%2F&title=Identity%20Abuse%20Through%20Trusted%20Communication%20Channels "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcommunication-channel-identity-risks%2F&text=Identity%20Abuse%20Through%20Trusted%20Communication%20Channels "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcommunication-channel-identity-risks%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Identity%20Abuse%20Through%20Trusted%20Communication%20Channels%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcommunication-channel-identity-risks%2F "Share in Mastodon")



## Executive Summary

Identity has become a primary security boundary for most organizations, reducing the ability to solely trust other boundaries once associated with corporate networks. Users authenticate to cloud services using enterprise identities that provide access to collaboration platforms, business applications and sensitive data. With the adoption of software-as-a-service (SaaS) on the rise, people are shifting to platforms for communication and collaboration.

Threat actors have adapted to this shift. In addition to typical email-based phishing, attackers increasingly misuse trusted collaboration platforms to conduct identity phishing, impersonation, credential theft, malware delivery and social engineering. Over the last 12 months, our endpoint alerts of malicious activity associated with collaboration tools have more than quadrupled, as Figure 1 shows. This activity could involve compromised accounts, external federated organizations, guest accounts or trusted third-party relationships. In each case, the attackers seek to exploit the trust that people place in enterprise communication platforms.

![A bar chart displaying the number of collaboration tool alerts from July 2025 to June 2026. The bars show a gradual increase over the months, starting at 1490 in July 2025 and peaking at 6799 in June 2026.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/Figure-1.png)Figure 1. Collaboration tool alerts of severity low or higher per month.

This changes the role that collaboration platforms play within enterprise security. They are not just productivity applications, they have become part of the enterprise attack surface. Unit 42 researchers found that 99% of the alerts generated related to chat or voice phishing operations, indicating that attackers often gain access to these environments through targeted phishing operations. After a successful compromise, attackers can then communicate using the identity and privileges of the compromised user. This allows malicious activity to appear as normal collaboration activity.

Security controls typically remain focused on email and authentication events, often providing limited visibility into activity occurring within authenticated collaboration sessions.

We examine how threat actors leverage trusted communication channels and review identity abuse techniques. We also provide practical recommendations for detecting and defending against identity-focused attacks targeting enterprise collaboration platforms.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM)
  * [Idira Endpoint Privilege Manager (EPM)](https://docs.cyberark.com/epm/latest/en/content/intro/introduction.htm)
  * [Idira Secrets Manager](https://docs.cyberark.com/welcome/latest/en/content/welcome/terms.htm)
  * [Idira Privileged Access Management (PAM)](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1)
  * [Idira Secure Infrastructure Access (SIA)](https://docs.cyberark.com/pam-self-hosted/latest/en/content/pasimp/integrate-with-sia.htm)
  * [Idira Secure Cloud Access (SCA)](https://docs.cyberark.com/find-sca-docs/latest/en/content/introduction/sca-new-doc-location.htm)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Phishing](https://unit42.paloaltonetworks.com/tag/phishing/), [Identity](https://unit42.paloaltonetworks.com/tag/identity/), [Credential Theft ](https://unit42.paloaltonetworks.com/tag/credential-theft/)**  
---|---  
  
## Understanding Trusted Communication Channels

Enterprise collaboration platforms have become integral to business operations. Employees use these platforms to exchange messages, share files, coordinate projects and communicate with colleagues, customers and business partners. Organizations typically connect collaboration platform access to their identity provider, and people rely on these platforms for trusted, authenticated communication.

Unlike email, collaboration platforms enable real-time conversations and support features such as external federation, guest access, shared workspaces and third-party integrations. These capabilities improve productivity but also create opportunities for misuse. Attackers can exploit compromised accounts, trusted business relationships or authorized external access to interact with victims through legitimate communication channels. Figure 2 shows common pathways for attackers to compromise identities in enterprise and cloud environments.

![A flowchart illustrating a cyberattack sequence with five stages: "Threat Actor Access Method," "Trusted Communication Channel" \(examples include Slack, Teams\), "Identity-Focused Interaction," "Requested User Action," and "Identity Outcome." Each stage describes actions and examples, connected by red arrows denoting progression.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-40200-185799-2.png)Figure 2. How attackers leverage collaboration platforms to compromise identities.

When a collaboration account is compromised, attackers inherit the identity context of that user, including their permissions, relationships and ongoing conversations. Requests that might appear suspicious in an email can appear routine when delivered through an authenticated collaboration platform. This reduces a target’s suspicion and increases the effectiveness of identity phishing, impersonation, credential theft and social engineering.

As organizations adopt more SaaS collaboration platforms, they should treat these environments as part of the identity attack surface. Protecting them requires both strong authentication, and visibility into how trusted identities and communication channels are used after authentication.

## Real-World Misuse of Collaboration Platforms

Recent campaigns demonstrate that attackers use collaboration platforms in multiple stages of identity-focused attacks, from initial access to post-compromise operations. Table 1 summarizes these intrusion stages.

**Intrusion Technique** | **Campaign Misuse Pattern**  
---|---  
Initial access: Phishing (T1566) | Identity phishing through external collaboration channels  
Stealth: Impersonation (T1684.001) | Impersonation through legitimate platform notifications, hosted content and direct messages  
Persistence: Modify Authentication Process (T1556) | MFA removal and privileged credential exfiltration through a native Slack webhook integration  
  
Table 1. Collaboration platform misuse by MITRE ATT&CK intrusion technique.

### Initial Access

One of the most common techniques is identity phishing through enterprise collaboration platforms. In our Insights article, ["When 'Hi, This Is IT' Comes Through Microsoft Teams"](https://unit42.paloaltonetworks.com/microsoft-teams-phishing/), we discussed how [APT29 used compromised Teams accounts to send links to credential-harvesting pages](https://www.paloaltonetworks.com/blog/sase/a-new-phishing-frontier-from-email-to-saas-collaboration-apps/). We reported that attackers misuse external federation in Teams to initiate conversations with victims while impersonating IT support or other trusted personnel. These campaigns often begin with a request to chat, followed by instructions to visit a phishing site, approve a multifactor authentication (MFA) request, install remote access software or provide credentials.

Okta Threat Intelligence has also documented the technique of [identity phishing through attacker-controlled Slack workspaces](https://www.okta.com/en-sg/blog/threat-intelligence/instant-messaging-services-abused-for-phishing-redirection/). The threat actor behind this activity impersonated administrators and employees from targeted organizations and sent phishing links through direct messages, channel mentions and legitimate notifications. The links redirected victims to adversary-in-the-middle phishing proxies designed to capture corporate credentials and MFA tokens.

Security teams might not detect the initial collaboration message directly. They could instead see the actions that follow. An example of this is shown in a process tree from a malicious chat scenario in Figure 3.

![A process tree diagram showing a communication application launching a system process, which uses an archive utility to extract a DLL from a downloaded archive file.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-42984-185799-3.png)Figure 3. Example of an initial access process tree.

In this case, the threat actor sent a RAR file via a link to a victim in a Teams chat. The victim downloaded the file to their Downloads folder. Note that attackers may avoid sending files through Teams because doing so creates an additional detection point through Safe Links/Safe Attachments, instead directing victims to websites or scripts during calls.

The victim then opened an Explorer window and double-clicked [REDACTED].rar, launching WinRAR.exe to open the archive. WinRAR extracted the malicious lpk.dll, which the victim’s endpoint security agent detected. The extracted lpk.dll is a known, older malicious DLL that masquerades as a legitimate Windows language pack DLL. Attackers use the file for DLL sideloading attacks. This recent event demonstrates that attackers continue to use older malware families in attacks delivered through collaboration platforms.

Unlike commonly-seen email phishing, some collaboration platforms support interactive communication. This enables attackers to respond to targets and adjust their social engineering tactics in real time. If successful, the attacker obtains a valid enterprise identity. The attacker can then access enterprise and cloud services with the privileges and identity context of the compromised user.

### Impersonation and Identity Compromise

Attackers use impersonation to exploit trust in collaboration platforms and gain access to enterprise identities, posing as known individuals, trusted organizations or support personnel.

  * In January 2026, [Fireblocks disclosed a recruitment-themed social engineering campaign](https://www.fireblocks.com/blog/contagious-interview-recruiting-scam) in which attackers impersonated Fireblocks executives, recruiters and hiring managers to target technology workers. The attackers initially contacted targets through social media, provided professionally prepared recruiting materials and then scheduled interviews through Google Meet. During the video interviews, an individual presented as a Fireblocks HR manager discussed the candidate’s experience, compensation and other expected hiring topics before assigning a code review task for a fictitious Fireblocks project. Candidates were instructed to clone a GitHub repository and run standard setup commands, including npm install, which executed malicious code and downloaded malware onto their systems. The campaign used legitimate Google Meet communications and a convincing interview process to reinforce the Fireblocks impersonation and persuade victims to execute malicious code. Fireblocks assessed the activity as closely aligned with the North Korea-linked Contagious Interview campaign pattern.
  * In March 2026, a threat actor used a staged [Slack workspace as part of a targeted social engineering campaign](https://socket.dev/blog/axios-maintainer-confirms-social-engineering-behind-npm-compromise) against the lead maintainer of the Axios npm package. The threat actor impersonated a legitimate company and created a convincing, simulated Slack environment with company branding, channels, users and message history. The interaction later moved to a meeting that was designed to look like Teams. During this meeting, the maintainer was convinced to install software that delivered a remote access Trojan. The threat actor then gained access to the maintainer’s npm account and [published two poisoned Axios versions](https://unit42.paloaltonetworks.com/axios-supply-chain-attack/), causing projects that installed the affected releases to retrieve and execute a malicious dependency.
  * In April 2026, OpenSSF reported a [campaign targeting members of the Linux Foundation TODO Group Slack workspace](https://lists.openssf-vuln.org/g/siren/message/7) and related communities. The threat actor impersonated a known Linux Foundation community leader and contacted targets through Slack direct messages. The messages contained a Google Sites link that led to a fraudulent Google Workspace authentication process. The site requested the target’s email address and verification code. It then instructed the target to install a malicious root certificate. On macOS, the process also downloaded and executed a binary that could provide system access. The campaign used the identity of a recognized community member and an established Slack workspace to support credential collection and malware delivery.



Each of these campaigns used impersonation through trusted collaboration workflows. The attackers relied on recognized identities, legitimate services and familiar business processes to obtain credentials or persuade victims to take actions that enabled identity compromise.

### Persistence

In a more novel approach, attackers have misused trusted collaboration services to maintain their access after identity compromise. In a December 2025 intrusion investigated by CERT Polska, [a threat actor modified compromised firewall-VPN appliances at a manufacturing company in Poland](https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/). The threat actor used the appliances’ built-in scripting mechanism to create weekly scheduled tasks. One script retrieved the password of a privileged identity, and another script modified security settings and disabled two-factor authentication for a privileged account. A third script used the appliances’ native Slack notification capability to send the results to a Slack channel under the threat actor’s control. This activity combined identity persistence and credential exfiltration with a legitimate SaaS integration. It also avoided the need for a separate exfiltration tool. The case demonstrates how attackers can misuse built-in appliance features and trusted collaboration services during post-compromise operations.

The firewall event in Figure 4 shows an example of a Slack webhook request, a similar communication method to the one described in the CERT Polska report. The request used HTTP POST to hooks.slack[.]com with a curl user agent. The example event below is not malicious.

![A screenshot of a desktop screen displaying two overlapping windows. The top window is a terminal displaying a cURL command to send a JSON payload with the text "Hello, World!" to a Slack webhook. The bottom window is Wireshark's "Follow HTTP Stream" feature, displaying HTTP request details for the Slack API.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/word-image-45365-185799-4.png)Figure 4. Webhook firewall event.

Perimeter firewalls provide valuable visibility into webhook-related traffic exiting the organization. Many network and security appliances, including VPN appliances, operate behind a separate perimeter firewall and send outbound webhook requests through the enterprise egress path when configured for external alerting or automation. Security teams should review unexpected Slack webhook traffic, uncommon user agents and webhook activity from systems without an approved Slack integration. This type of activity should also be flagged in Microsoft Teams, which supports similar incoming webhook workflows for posting messages from external services.

These examples of initial access, impersonation and persistence demonstrate how attackers leverage trusted communication channels to support identity-focused attacks. Although the techniques differ, each example leverages legitimate platforms, authenticated identities or authorized communication paths to increase the likelihood of success. The common objective is to misuse the trust, access and identity context associated with enterprise collaboration platforms.

## Defensive Measures for Securing Collaboration Platforms

Organizations should protect collaboration platforms with the same level of scrutiny applied to email and identity infrastructure. Because these platforms are integrated with enterprise identities, security controls should focus on both preventing identity compromise and detecting misuse after authentication.

### Reduce Exposure

The first priority is reducing unnecessary exposure. Collaboration platform administrators should review external federation, guest access and third-party integrations to ensure they support legitimate business requirements. Where possible, limit external communications to trusted organizations, and implement a process to review guest accounts regularly and remove unnecessary access.

### Comprehensive Identity Controls

Identity protections should also extend beyond authentication. MFA, conditional access and session risk evaluation help reduce the likelihood of account compromise, but they do not prevent an attacker from misusing a valid session. Security teams should monitor for behavior that could indicate identity compromise, including unusual messaging activity, unexpected file sharing or communications with unfamiliar external tenants.

### Identity Verification Procedures

Identity and security teams should define and communicate verification procedures for security-sensitive requests received through collaboration platforms. Users should not approve MFA prompts, install remote access tools, share credentials, transfer files or modify access based only on a message. Instruct people to verify high-risk requests through an approved secondary channel, such as a known phone number, ticketing system or documented internal process.

### User Awareness

User awareness remains an important part of effective verification procedures. People should treat collaboration messages, platform notifications and links to hosted content with the same caution as email. This is especially important when a request involves credentials, MFA approval, software installation, remote access tools or sensitive data.

Security training should make clear that content associated with an enterprise collaboration platform is not automatically trustworthy. An attacker can send a direct message, trigger a legitimate platform notification or use content hosted on an approved service to direct victims to a phishing site.

Security awareness teams should include these scenarios in phishing simulations and security awareness exercises. Many people recognize email phishing indicators but might not apply the same scrutiny to collaboration platforms and related notification workflows.

### Active Monitoring

Security teams should incorporate collaboration platform telemetry into routine monitoring and incident response. Authentication logs, messaging activity, file sharing events and external tenant interactions provide valuable context for detecting identity abuse.

Network and security appliances should also be included in monitoring coverage. Firewalls, VPN appliances, load balancers and managed switches increasingly support automation, notification integrations and scheduled tasks. Attackers can potentially use these capabilities for malicious purposes following a compromise. To protect against such activity, security teams should monitor:

  * Administrative activity
  * Configuration changes
  * Outbound webhook usage
  * Unusual connections to collaboration or SaaS services



This telemetry should be ingested into a security information and event management (SIEM) system and correlated with identity, endpoint and collaboration platform data. This can improve visibility into malicious activity that might otherwise appear to originate from legitimate users or approved infrastructure.

Collaboration-based reporting must also be easy for users. Security teams should provide a clear process for reporting suspicious communications, notifications, hosted content and links associated with collaboration platforms. Each report should be triaged using identity telemetry, sign-in activity, endpoint alerts, file-sharing events and external tenant information. This helps to determine whether the activity reflects user error, external misuse or identity compromise.

## Conclusion

Enterprise collaboration platforms are integrated with enterprise identity and access workflows. As organizations rely on these platforms for communication, attackers are exploiting the trust associated with authenticated users and sanctioned communication channels to conduct identity phishing, impersonation, credential theft and post-compromise operations.

Common security strategies have focused on protecting email and authentication systems. While these controls remain essential, they should be complemented by security measures that address collaboration platforms as part of the enterprise identity attack surface. Authentication alone is no longer sufficient to establish trust. Organizations must also understand how authenticated identities are communicating and recognize when trusted communication channels are being misused.

By extending identity security to include collaboration platforms, defenders can better detect identity abuse, reduce opportunities for compromise and strengthen their ability to respond to identity-focused attacks. As collaboration technologies evolve, organizations should monitor and protect them with the same controls they apply to other critical identity infrastructure.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) help to prevent the threats described in this article, by employing the [Malware Prevention Engine](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-4.x-Documentation/Malware-protection). This approach combines several layers of protection, including [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire), Behavioral Threat Protection and the Local Analysis module, to prevent both known and unknown malware from causing harm to endpoints.
  * [Idira Endpoint Privilege Manager (EPM)](https://docs.cyberark.com/epm/latest/en/content/intro/introduction.htm) can enable enterprises to reduce risk, satisfy compliance, and streamline operations. It can help implement least privilege via policy-driven elevation and removal of standing admin rights, and block risky actions, such as execution of unvetted applications and access to memory of other processes, while providing audit-ready evidence.
  * [Idira Secrets Manager](https://docs.cyberark.com/welcome/latest/en/content/welcome/terms.htm) centralizes the API keys, service account passwords, and webhook tokens that appliances, scheduled tasks, and pipelines depend on, so automation retrieves credentials at runtime instead of reading them from local scripts or device configuration. Automated rotation shortens the window in which a stolen credential stays valid, and universal workload identity replaces static credentials with short-lived SPIFFE-based workload identities where the environment supports it.
  * [Idira Privileged Access Management (PAM)](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1) helps unify privileged access across human, machine, and agentic identities to secure cloud access across multi-cloud environments. Building on proven PAM, it delivers centralized secrets management alongside modern controls like Just-in-Time access and Zero Standing Privileges. This enforces consistent least-privilege security across on-premises, cloud, and SaaS targets.
  * [Idira Secure Infrastructure Access (SIA)](https://docs.cyberark.com/pam-self-hosted/latest/en/content/pasimp/integrate-with-sia.htm) can help enforce Zero Standing Privileges (ZSP) through Just-in-Time (JIT) provisioning which grants temporary, tightly scoped access only as needed. Backed by continuous session recording and real-time command monitoring, SIA can detect high risk actions before an attacker compromises critical systems.
  * [Idira Secure Cloud Access (SCA) ](https://docs.cyberark.com/find-sca-docs/latest/en/content/introduction/sca-new-doc-location.htm)can help enforce Zero Standing Privileges (ZSP) across multicloud environments by applying Just-in-Time (JIT) access controls to cloud consoles, command-line interfaces (CLIs), and the modern cloud infrastructure where workloads reside, including Managed Kubernetes clusters and elastic cloud workloads.



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

## Additional Resources

  * [Energy Sector Incident Report - 29 December 2025](https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/) – CERT Polska
  * [Slack Abused for Phishing Redirection](https://www.okta.com/en-sg/blog/threat-intelligence/instant-messaging-services-abused-for-phishing-redirection/) – Okta
  * [Potential Malicious Campaign Underway Targeting Open Source Developers via Slack](https://lists.openssf-vuln.org/g/siren/message/7) – OpenSSF
  * [A New Phishing Frontier: From Email to SaaS Collaboration Apps](https://www.paloaltonetworks.com/blog/sase/a-new-phishing-frontier-from-email-to-saas-collaboration-apps/) – Palo Alto Networks
  * [Threat Brief: Widespread Impact of the Axios Supply Chain Attack](https://unit42.paloaltonetworks.com/axios-supply-chain-attack/) – Palo Alto Networks
  * [When “Hi, This Is IT” Comes Through Microsoft Teams](https://unit42.paloaltonetworks.com/microsoft-teams-phishing/) – Palo Alto Networks
  * [Axios Maintainer Confirms Social Engineering Attack Behind npm Compromise](https://socket.dev/blog/axios-maintainer-confirms-social-engineering-behind-npm-compromise) – Socket
  * [Disrupting a Recruiting Impersonation Scam: Anatomy of Operation Contagious Interview](https://www.fireblocks.com/blog/contagious-interview-recruiting-scam) – Fireblocks



## Threat Hunting Query

The query below is designed to help Palo Alto Networks customers hunt for, investigate and identify potentially suspicious activity using Cortex XDR. Results returned by this query should not be considered inherently malicious and require further analysis to determine their significance.

### Query to Identify Collaboration Tool Spawning a Shell

This XQL query can help to identify where legitimate collaboration platforms — specifically Slack or Teams in this example — are used to execute system shells. The query inspects both the direct process hierarchy and the broader causality chain. It identifies instances where a collaboration tool is either the immediate parent process or an ancestor process that initiated the execution of a shell. Analysts can use this logic to identify:

  * Post-exploitation activity
  * Unauthorized command execution
  * Living-off-the-land techniques that originate from compromised user accounts or application integrations



The query can be modified to search for additional collaboration platforms or system shells.

dataset = xdr_data | filter _time >= "2026-07-08T00:00:00Z" and _time < "2026-07-09T00:00:00Z" | filter ( // Look for Slack/Teams in the causality chain spawning shells (lowercase(causality_actor_process_image_name) contains "slack" or lowercase(causality_actor_process_image_name) contains "teams" or lowercase(actor_process_image_name) contains "slack" or lowercase(actor_process_image_name) contains "teams") and (lowercase(actor_process_image_name) in ("cmd.exe", "powershell.exe", "bash", "sh", "zsh") or lowercase(action_process_image_name) in ("cmd.exe", "powershell.exe", "bash", "sh", "zsh")) ) | fields _time, actor_process_command_line, action_process_image_command_line, causality_actor_process_command_line, actor_process_image_name, action_process_image_name, causality_actor_process_image_name, actor_process_image_sha256, action_process_image_sha256, causality_actor_process_image_sha256, action_file_path, actor_causality_id, causality_actor_process_causality_id, dst_actor_remote_ip, dst_action_external_hostname, action_remote_ip, action_external_hostname | sort asc _time

123456789101112131415161718192021222324252627 | dataset = xdr_data| filter _time >= "2026-07-08T00:00:00Z" and _time < "2026-07-09T00:00:00Z"| filter ( // Look for Slack/Teams in the causality chain spawning shells (lowercase(causality_actor_process_image_name) contains "slack" or lowercase(causality_actor_process_image_name) contains "teams" or lowercase(actor_process_image_name) contains "slack" or lowercase(actor_process_image_name) contains "teams") and (lowercase(actor_process_image_name) in ("cmd.exe", "powershell.exe", "bash", "sh", "zsh") or lowercase(action_process_image_name) in ("cmd.exe", "powershell.exe", "bash", "sh", "zsh")))| fields  _time, actor_process_command_line, action_process_image_command_line, causality_actor_process_command_line, actor_process_image_name, action_process_image_name, causality_actor_process_image_name, actor_process_image_sha256, action_process_image_sha256, causality_actor_process_image_sha256, action_file_path, actor_causality_id, causality_actor_process_causality_id, dst_actor_remote_ip, dst_action_external_hostname, action_remote_ip, action_external_hostname| sort asc _time  
---|---  
  
Back to top

### Tags

  * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")
  * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [MFA](https://unit42.paloaltonetworks.com/tag/mfa/ "MFA")
  * [Remote access software](https://unit42.paloaltonetworks.com/tag/remote-access-software/ "remote access software")
  * [Social engineering](https://unit42.paloaltonetworks.com/tag/social-engineering/ "social engineering")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18) ](https://unit42.paloaltonetworks.com/large-scale-credential-attacks/ "Threat Brief: Mitigating Large-Scale Credential Attacks \(Updated August 18\)")

### Table of Contents

  *   * Executive Summary
  * Understanding Trusted Communication Channels
  * Real-World Misuse of Collaboration Platforms
    * Initial Access
    * Impersonation and Identity Compromise
    * Persistence
  * Defensive Measures for Securing Collaboration Platforms
    * Reduce Exposure
    * Comprehensive Identity Controls
    * Identity Verification Procedures
    * User Awareness
    * Active Monitoring
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Additional Resources
  * Threat Hunting Query
    * Query to Identify Collaboration Tool Spawning a Shell



### Related Articles

  * [ Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "article - table of contents")
  * [ Threat Brief: Mitigating Large-Scale Credential Attacks (Updated August 18) ](https://unit42.paloaltonetworks.com/large-scale-credential-attacks/ "article - table of contents")
  * [ Inside the Modern SOC: The Identity Front Door ](https://unit42.paloaltonetworks.com/soc-identity-front-door/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)