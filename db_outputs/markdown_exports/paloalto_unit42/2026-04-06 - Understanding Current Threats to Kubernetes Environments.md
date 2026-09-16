# Understanding Current Threats to Kubernetes Environments

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/modern-kubernetes-threats/
- **Date :** 2026-04-06

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Understanding Current Threats to Kubernetes Environments

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 20 min read 

Related Products

[![Advanced DNS Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced DNS Security](https://unit42.paloaltonetworks.com/product-category/advanced-dns-security/ "Advanced DNS Security")[![Advanced Threat Prevention icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced Threat Prevention](https://unit42.paloaltonetworks.com/product-category/advanced-threat-prevention/ "Advanced Threat Prevention")[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Advanced WildFire icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced WildFire](https://unit42.paloaltonetworks.com/product-category/advanced-wildfire/ "Advanced WildFire")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Cortex Xpanse icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Xpanse](https://unit42.paloaltonetworks.com/product-category/cortex-xpanse/ "Cortex Xpanse")[![Next-Generation Firewall icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Next-Generation Firewall](https://unit42.paloaltonetworks.com/product-category/next-generation-firewall/ "Next-Generation Firewall")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Eyal Rafian](https://unit42.paloaltonetworks.com/author/eyal-rafian/)
    * [Bill Batchelor](https://unit42.paloaltonetworks.com/author/bill-batchelor/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:April 6, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Audit logs](https://unit42.paloaltonetworks.com/tag/audit-logs/)
    * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/)
    * [Containers](https://unit42.paloaltonetworks.com/tag/containers/)
    * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/)
    * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/)
    * [Queries](https://unit42.paloaltonetworks.com/tag/queries/)
    * [React server](https://unit42.paloaltonetworks.com/tag/react-server/)
    * [React2shell](https://unit42.paloaltonetworks.com/tag/react2shell/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Understanding%20Current%20Threats%20to%20Kubernetes%20Environments&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fmodern-kubernetes-threats%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmodern-kubernetes-threats%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmodern-kubernetes-threats%2F&title=Understanding%20Current%20Threats%20to%20Kubernetes%20Environments "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmodern-kubernetes-threats%2F&text=Understanding%20Current%20Threats%20to%20Kubernetes%20Environments "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fmodern-kubernetes-threats%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Understanding%20Current%20Threats%20to%20Kubernetes%20Environments%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fmodern-kubernetes-threats%2F "Share in Mastodon")



## Executive Summary

The rapid adoption of container orchestration has positioned Kubernetes as a high-value target for adversaries seeking to compromise enterprise-scale environments. Our telemetry reveals that Kubernetes-related threat actor operations, including stealing Kubernetes tokens, increased 282% over the last year. The IT sector was the most heavily targeted, representing over 78% of observed activity.

We look beyond traditional [container escape](https://unit42.paloaltonetworks.com/container-escape-techniques/) scenarios, and demonstrate how high-profile threat actors abuse Kubernetes identities and exposed attack surfaces to escalate privileges, pivoting from initial access to sensitive backend cloud infrastructure. Using two real-world case studies, we break down the mechanics of these attacks and the tradecraft that made them possible:

  * **Stolen service account tokens:** Suspicious activity related to potential service account token theft was observed in 22% of cloud environments in 2025. We explore how attackers compromised Kubernetes identities to move laterally from a production cluster into the core financial systems of a cryptocurrency exchange.
  * **React2Shell (CVE-2025-55182):** Attacks targeting cloud services were observed within two days of the public disclosure of this critical vulnerability. We provide a breakdown of how threat actors exploited this public-facing application vulnerability to execute commands inside Kubernetes workloads. Leveraging this vulnerability, attackers were able to install backdoors and steal sensitive information, such as cloud credential files and database passwords.



Together, these cases illustrate a common attack pattern:

  * Exploiting misconfigurations or vulnerabilities to achieve remote code execution in the container.
  * Stealing Kubernetes identities from the container.
  * Using the stolen identities to escalate privileges across clusters and cloud services.



We map these patterns to MITRE ATT&CK® techniques and examine threat actor tradecraft, to provide practical configuration, detection and monitoring strategies that disrupt attack paths before cluster-wide compromise occurs. Most security failures stem from misconfigured environments and overprivileged identities. To secure Kubernetes against attacks, defenders must implement validated settings, deep runtime visibility, and strictly limited permissions. These approaches help to transform Kubernetes from a potential exposure point into a highly resilient and defensible platform.

Palo Alto Networks customers are better protected from the threats described in this article through the following products and services:

  * [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire)
  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security)
  * [Next-Generation Firewall](https://docs.paloaltonetworks.com/ngfw) with the [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration) security subscription
  * [Cortex Xpanse](https://www.paloaltonetworks.com/cortex/cortex-xpanse) is designed to identify exposed devices and applications on the public internet and escalate these findings to defenders. This includes devices vulnerable to CVE-2025-55182.
  * [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud) has detection capabilities for cloud resource vulnerability and runtime operations discussed in this article.



The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/), [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/), [Containers](https://unit42.paloaltonetworks.com/tag/containers/), [Logging](https://unit42.paloaltonetworks.com/tag/logging/)**  
---|---  
  
## The Kubernetes Cloud Attack Surface

Kubernetes is widely used to orchestrate microservice-based applications at scale. It provides automated deployment, service discovery and workload isolation across cloud environments. Like many open-source systems, Kubernetes is also a high-value attack surface that threat actors attempt to exploit in a variety of ways.

  * Public-facing workloads that are exposed through ingress controllers and load balancers provide a potential entry point for [application-layer exploitation](https://attack.mitre.org/techniques/T1190/).
  * Misconfigurations in role-based access control (RBAC), pod security settings, and service account permissions can facilitate rapid post-exploitation escalation.
  * After gaining remote code execution within a container, threat actors can directly interact with the Kubernetes API using the pod’s mounted service account token, often without triggering traditional perimeter [defenses](https://www.paloaltonetworks.com/blog/cloud-security/kubernetes-attack-detection-response/).



Threat actors can leverage these misconfigurations and externally exposed services using a combination of opportunistic vulnerability exploitation, identity misuse and automation.

The workflow of the attackers’ operations follows a distinct pattern:

  * Enumerating the runtime environment
  * Extracting [service account tokens](https://attack.mitre.org/techniques/T1528/)
  * Testing API permissions
  * Pivoting to higher-value workloads or cloud services



When these operations are combined, even small misconfigurations – overly permissive tokens, exposed APIs, or insufficient workload and namespace isolation – could enable threat actors to gain full cluster administrator privileges by leveraging a single compromised pod.

## Threat Actor Activity

Recently, Unit 42 researchers witnessed the increased use of Kubernetes clusters as operational infrastructure for credential theft, lateral movement and cloud-level compromise. The following cases demonstrate how stolen credentials and application-layer exploitation lead to similar post-exploitation workflows, leveraging Kubernetes identities to obtain access to sensitive backend systems.

### **Case 1: Token Theft and Lateral Movement in a Crypto Platform**

In the middle of 2025, Unit 42 researchers witnessed an intrusion at a cryptocurrency exchange. This intrusion is connected to a campaign of recent cryptocurrency heists by the North Korean state-sponsored threat group known as [Slow Pisces](https://unit42.paloaltonetworks.com/slow-pisces-new-custom-malware/) – also known as [Lazarus](https://unit42.paloaltonetworks.com/threat-actor-groups-tracked-by-palo-alto-networks-unit-42/#:~:text=Utilities%20and%20Energy-,Slow%20Pisces,Also%20Known%20As,-Dark%20River%2C%20DEV) and TraderTraitor.

#### Earlier Campaign Activity

This threat group's evolving capabilities were demonstrated in the February 2025 [Bybit](https://www.ic3.gov/psa/2025/psa250226) heist. Attackers stole approximately $1.5 billion in Ethereum (ETH), making this the largest digital theft in history. The tactics employed in this breach closely mirror identity-scraping techniques that are used to penetrate and pivot within cloud-native environments.

In the Bybit operation, Slow Pisces actors targeted a developer at the exchange’s multi-signature platform provider and successfully exfiltrated AWS session tokens. By leveraging these stolen identity tokens, the group gained administrative access to the exchange’s cloud infrastructure. This unauthorized access allowed them to manipulate the platform’s smart contract and reroute massive volumes of financial assets.

Slow Pisces was also suspected in the [BitoPro](https://www.bitopro.com/ns/en-US/announcements/1226) Taiwanese cryptocurrency exchange intrusion in May 2025. Threat actors social-engineered a cloud‑operations employee, harvested AWS session tokens, and assumed privileged access within the company’s cloud environment. They then pushed malicious scripts to the hot‑wallet host and activated them during a maintenance window, enabling fraudulent transfers to blend in with routine operations.

In both operations, Slow Pisces leveraged stolen cloud identity tokens to assume administrative roles, enabling direct control over smart contract logic and hot-wallet scripts.

#### From One Exchange to Another

In mid-2025, we observed a sophisticated intrusion at another cryptocurrency exchange. This attack involved a Kubernetes post-exploitation credential scraping operation that led to a cloud environment compromise and the theft of millions in cryptocurrency funds. While there is no indication that the Slow Pisces actors used a specific offensive toolkit, several observed behaviors aligned with techniques [previously described](https://www.sysdig.com/blog/scarleteel-2-0) in Kubernetes security research, including those illustrated in penetration testing frameworks such as [Peirates](https://github.com/inguardians/peirates). Figure 1 shows the progression of the intrusion.

![A flowchart outlining a multi-stage cyberattack scenario. It includes six stages: 1. Initial Access, 2. Kubernetes Entry Point, 3. Token Extraction, 4. Kubernetes Post-Exploitation, 5. Cloud Lateral Movement and 6. Impact: Compromise of data and financial theft. Each stage is briefly explained with connecting arrows indicating progression.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-310261-177112-1.png)Figure 1. Cryptocurrency incident flow with Kubernetes compromise.

After gaining persistence on the developer's workstation through spearphishing, the threat actor leveraged the developer’s active, privileged cloud session to deploy a malicious pod to the production Kubernetes cluster. This pod was designed to expose the mounted service account token. This technique mirrors service account token [extraction](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/) concepts that are widely discussed in Kubernetes post‑exploitation [research](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms).

The retrieved token belonged to a high-privileged management service account with broad RBAC permissions, used by a common CI/CD automation and cluster orchestration system. With this overly permissive identity, the threat actor authenticated directly to the Kubernetes API server and enumerated secrets, interacted with workloads across namespaces, and dropped a backdoor into a production pod to maintain persistent access within the cluster. These actions reflect several well‑known Kubernetes post‑compromise patterns, including secret enumeration, token harvesting and cloud metadata interaction.

Using the privileges granted by the stolen token, the threat actor moved laterally from Kubernetes into the wider cloud platform. They accessed the exchange's cloud hosted backend systems, retrieved sensitive credentials, and ultimately reached the financial infrastructure of the exchange. The progression from malicious pod deployment to cloud‑level compromise demonstrated how Kubernetes identities serve as a powerful pivot point when RBAC is misconfigured or overly permissive.

### **Case 2: Exploitation of React2Shell, CVE-2025-55182**

Another high-profile exploitation of the Kubernetes-to-cloud attack surface was the recent React2Shell vulnerability. This incident reveals how a single application-layer exploit can result in cluster compromise, cloud account exposure and direct financial impact when Kubernetes workloads are over-privileged or insufficiently isolated.

Initially disclosed on Dec. 3, 2025, React2Shell ([CVE-2025-55182](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)) provided threat actors with a direct path from the public internet to execution inside Kubernetes workloads – and ultimately into the cloud hosting environment. The earliest cloud targeting operations that leveraged this CVE occurred between Dec. 5 and 7, 2025. By exploiting insecure deserialization in the React Server Components (RSC) Flight protocol, threat actors executed arbitrary code inside application containers running behind ingress controllers and cloud load balancers. In Kubernetes environments, this translated into immediate access to the pod runtime – including its filesystem, environment variables, network context, and mounted identities. Such access effectively eliminates the boundary between an exposed web application and the cluster itself.

[Unit 42 coverage of React2Shell](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/) shows that various threat groups used this pod runtime access to rapidly extract value from compromised Kubernetes environments. After gaining execution, threat actors enumerated cluster resources, harvested mounted service account tokens and queried the Kubernetes API to determine the scope of privileges granted via RBAC. In multiple cases, threat actors collected cloud credentials that were exposed in environment variables and cloud metadata services, using them to pivot beyond Kubernetes into the underlying cloud account. This access supported follow-on activity, including cryptomining deployment, backdoor installation, and credential theft targeting databases and backend services.

The following commands show threat actors attempting to exfiltrate cloud credentials from compromised containers by Base64-encoding credential files and transmitting them via outbound HTTP requests using tools such as curl. We extracted the examples below from telemetry from multiple environments. They illustrate a pattern of cloud credential and environment variable exfiltration that is consistent with the cloud and Kubernetes intrusions that we observed during this event, as noted in Figure 2.

![A screenshot showing a code snippet of a shell script designed to execute `curl` commands, targeting specific URLs. The script uses `base64` encoding to handle outputs from credentials and environment files.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-312689-177112-2.png)Figure 2. Exfiltration from an intrusion we observed during this event.

Figure 3 shows an example of an attempt observed by Unit 42 to download, execute and subsequently delete a backdoor masquerading as a Vim editor.

![A screenshot of a code snippet showing a shell script command using wget to download a file from an IP address, assigning execution permissions, running it in the background, and then deleting the file.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-314685-177112-3.png)Figure 3. Attempt involving a backdoor masquerading as Vim.

## Tooling and TTPs

Threat actor activity in Kubernetes environments closely mirrors the techniques and workflows that are documented in publicly available post-exploitation frameworks. Rather than relying on novel tooling, threat actors often reuse established tradecraft that focuses on identity discovery, API interaction and misuse of legitimate Kubernetes functionality.

This section maps observed behaviors to specific MITRE ATT&CK® techniques and tooling, illustrating how threat actors chain initial access ([T1190](https://attack.mitre.org/techniques/T1190/)) and token theft ([T1528](https://attack.mitre.org/techniques/T1528/)) to create repeatable attack paths. Understanding these techniques – and how tools like Peirates ([S0683](https://attack.mitre.org/software/S0683/)) model them – provides defenders with a practical lens for anticipating threat actor behavior and designing controls that interrupt escalation early in the attack lifecycle.

### T1190 Exploit Public-Facing Application

Exploiting vulnerabilities such as React2Shell allows threat actors to bypass authentication and execute code directly inside an application container, establishing initial access within the cluster without requiring credentials or user interaction. Threat actors use the T1190 Initial Access MITRE Technique to convert unauthenticated internet access into execution within a target environment. Kubernetes-based deployments of public-facing applications exposed through ingress controllers or cloud load balancers are potential entry points.

After achieving code execution within a pod, threat actors treat the compromised pod as an initial foothold for follow-on operations. Common actions include enumerating containers and namespaces, inspecting mounted service account tokens, querying the mounted service account’s effective RBAC scope and mapping internal cluster networking. As described in Case 2, Unit 42 observed threat actors chaining this access with web shell deployment, credential harvesting from environment variables and configuration files, and delivery of secondary payloads such as cryptominers or backdoors.

Figure 4 shows an example of a React2Shell exploitation attempt that we observed.

![A screenshot of a code snippet displaying a command for downloading and executing a script from an IP address using wget and curl in a bash shell.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-316633-177112-4.png)Figure 4. React2sahell exploitation attempt we observed.

In this example, the threat actor attempted to retrieve and execute a generic dropper script to deliver second-stage payloads.

This pattern of exploit and follow-on activity is used as the initial access vector that enables subsequent discovery, lateral movement, credential access and persistence within Kubernetes and connected cloud environments.

### T1528 Steal Application Access Token

Stealing application access tokens is another technique favored by threat actors. After gaining access to a Kubernetes pod, one of their first objectives is to identify the pod’s associated identity, to determine what permissions it holds within the cluster. By default, pods automatically mount a Service Account Token (SAT) at /var/run/secrets/kubernetes.io/serviceaccount/token. The SAT is a JSON web token (JWT) that serves as the pod's digital signature for authenticating with the Kubernetes API. To a threat actor, gaining access to this file provides immediate and often unrestricted access.

Recent threat activity observed in late 2025 and early 2026 shows that this technique is increasingly used for automated threat actor credential harvesting. The alert data reflecting this activity is detailed in Appendix A.

Modern malware frameworks now perform environment harvesting at execution time to specifically hunt for these associated identities. For instance, the [TeamPCP](https://flare.io/learn/resources/blog/teampcp-cloud-native-ransomware) (PCPcat, ShellForce, and DeadCatx3) worm uses scripts like proxy.sh to detect whether they are running within a Kubernetes cluster. If so, they branch into a separate execution path to drop kube.py, a specialized payload designed to harvest cluster credentials and discover resources via the API.

Similarly, the recent [VoidLink](https://www.ontinue.com/resource/voidlink-dissecting-an-ai-generated-c2-implant/) malware cloud framework demonstrates a sophisticated, cross-cloud approach. Rather than opportunistically discovering tokens, it is built with dedicated plugins (like k8s_privesc_v3) specifically to target the /var/run/secrets/directory. These tools treat the Kubernetes SAT as a launchpad for multi-cloud exploitation, exfiltrating not only the token, but also environment variables and cloud metadata to pivot across AWS, GCP and Azure.

With access to the pod, the threat actor – or their automated implant – reads the token and tests what it can do. The token could belong to a low‑privileged workload, but in [many real‑world attacks](https://unit42.paloaltonetworks.com/google-kubernetes-engine-privilege-escalation-fluentbit-anthos/), RBAC misconfigurations result in the token having far more power than intended. The threat actor can use the token to interact with the Kubernetes API as the stolen identity, listing secrets, probing other namespaces and mapping out which doors are now open to them.

This is where the escalation begins. The stolen token becomes the threat actor’s new identity key, allowing them to deploy additional malicious pods, access sensitive data, or reach cloud metadata nodes that expose additional credentials. The workflow mirrors the post‑compromise path demonstrated in tools like Peirates, but with the added speed of AI-assisted malware frameworks. An example of such a framework is VoidLink, which creates a risk score of the targeted environment and throttles the malware’s behavior to evade detection while it drains secrets.

From here, the threat actor's escalation path becomes clear. They move from compromising a pod and stealing the token to using the stolen identity for broader control of the cluster's most critical assets. As the crypto and React2Shell cases demonstrate, the final steps of this path bring the threat actors to the cloud platform that hosts the container cluster.

### S0683 Peirates

Peirates is a Go-based open-source framework, originally created to help red teams and defenders understand how a compromised container can be leveraged to explore a cluster, escalate privileges and pivot into cloud services. Once it is running inside a pod, the tool demonstrates how a threat actor might enumerate service accounts, inspect secrets, switch namespaces and query cloud metadata endpoints.

Although intended for defensive research, Unit 42 and others have reported the misuse of Peirates by threat groups like [SCARLETEEL](https://www.sysdig.com/blog/scarleteel-2-0) to enumerate resources and [TeamTNT](https://unit42.paloaltonetworks.com/teamtnt-operations-cloud-environments/) for reconnaissance operations.

Peirates has a number of available techniques, grouped logically by function:

  * **Namespaces, service accounts and roles**



Identity and context discovery techniques to enumerate namespaces, pods, and service accounts, switch execution contexts, and test alternative authentication methods, including assumed identity and access management (IAM) roles and certificate-based access.

  * **Steal service accounts**



Credential theft techniques to enumerate Kubernetes secrets, retrieve service account tokens and acquire cloud credentials via AWS and GCP metadata services and cluster management backends such as [kOps](https://kops.sigs.k8s.io/).

  * **Interrogate/misuse cloud APIs**



Techniques to use stolen cloud credentials outside Kubernetes. Threat actors can validate and misuse access to cloud services – for example, listing AWS S3 buckets and their contents.

  * **Compromise**



Techniques to transition from workload compromise to cluster or host compromise. Threat actors can execute commands across pods, dump tokens via kubelets, deploy malicious pods with hostPath mounts and exploit container runtime vulnerabilities to gain node-level access.

  * **Node attacks**



Targets the underlying Kubernetes node once access is achieved and enables threat actors to read sensitive files directly from the node filesystem, including credentials and configuration data.

  * **Off-menu**



General-purpose post-exploitation utilities. Allows threat actors to run arbitrary kubectl commands across multiple authorization contexts, issue raw HTTP requests, perform network scanning and DNS enumeration and execute shell or filesystem commands.

Figure 5 shows a sample interactive Peirates menu with a truncated list of techniques that can be run with the tool.

![An image of a command-line interface for a tool called Peirates, developed by InGuardians and Peirates Open Source Developers. It includes ASCII art of the tool's name at the top. The interface lists commands related to namespaces, service accounts, and roles, such as listing service account contexts and changing namespaces.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-318369-177112-5.png)Figure 5. Sample Peirates menu.

## Kubernetes Threat Detection

The tactics used in recent breaches provide a basis for defense strategies. To secure Kubernetes environments, organizations must prioritize validated configurations, runtime visibility and restricted access controls. Leveraging log data, runtime telemetry, behavioral analysis and strategic threat hunting allows organizations to detect Kubernetes misuse before it escalates into a full environment compromise. The following sections detail these requirements.

### **Log Data Sources: Kubernetes Audit Logs**

Despite their importance, improperly configured Kubernetes environments may run with audit logging disabled, leaving defenders unable to see the earliest stages of an intrusion.

[Kubernetes audit logs](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) provide a record of API activity inside a cluster, capturing every request to the API server and its outcome. This makes them essential for understanding how a threat actor gained access, what they interacted with and how far they moved. Because the API server mediates all user and service account activity, its logs can reveal the earliest signs of intrusion, including anonymous requests that appear when insecure configurations allow unauthenticated access to the API or kubelet. These entries often signal the onset of internal discovery, as threat actors begin probing the cluster to map out exploitable identities and permissions.

As threat actors expand their activity, audit logs reveal the earliest deviations from normal operations. These include unexpected activity concerning [RBAC](https://www.sentinelone.com/blog/climbing-the-ladder-kubernetes-privilege-escalation-part-1/), such as attempts to modify [ClusterRoleBindings](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-and-clusterrolebinding), service account tokens originating from unusual IP addresses, or pods appearing in sensitive namespaces. These patterns often precede more advanced techniques such as malicious admission controller deployment, CoreDNS manipulation or the creation of writable volume mounts that provide direct access to the underlying node. Each of these actions leaves a distinct trace in the audit logs, indicating changes to Kubernetes resources, unexpected API verbs, or identities performing operations outside their normal behavior.

Monitoring identity-driven changes and the creation of suspicious resources allows defenders to detect privilege escalation and lateral movement early, often before a threat actor achieves full administrative control of the cluster.

For more information and guidance, see our [Cloud Logging for Security](https://unit42.paloaltonetworks.com/cloud-logging-for-security/) article.

### Runtime Telemetry and Behavioral Analysis

In the recent exploitation of React2Shell (CVE-2025-55182), threat actors gained code execution inside containers, including Kubernetes, through an application-layer exploit or other exposed service. Once a threat actor gains code execution inside a container, their activity quickly shifts from exploitation to post-exploitation. They use tools such as Peirates to enumerate privileges, steal tokens and escalate access. These actions result in process execution, host resource access, and outbound connectivity – all of which generate log footprints.

Workload runtime monitoring makes these behaviors visible by observing what containers actually do at execution time, rather than what they were intended to do upon deployment. Commercial workload protection and XDR platforms enable this visibility. These tools detect when a workload spawns unexpected shells or utilities, exhibits sustained high CPU usage consistent with cryptomining, or initiates outbound connections to unfamiliar destinations.

For example, Figure 6 shows an attempted exploit on a managed Docker environment that is orchestrated by Kubernetes and is vulnerable to React2Shell.

![A flowchart diagram showing a process flow with nodes and triangular warning symbols. The "PROCESS INFORMATION" section lists path, command line, SHA256, username, signature, and running time details, with some information redacted.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-320231-177112-6.png)Figure 6. Attempted reverse shell (CVE-2025-55182), blocked by Cortex XDR.

Runtime monitoring correlates these signals in real time to detect threat actor post-exploitation tooling. Depending on configuration, workload protection platforms can also automatically terminate malicious processes and even shut down compromised pods when necessary. This limits the "dwell time" a threat actor has to move from the application layer to the cluster control plane.

### Threat Hunting and Alerting with Cortex XQL

A threat actor who has gained access to a compromised pod will often try to extract the [service account token](https://unit42.paloaltonetworks.com/third-party-supply-chain-token-management/) assigned to it – a tactic previously observed in [attacks in the wild](https://www.aquasec.com/blog/kubernetes-exposed-exploiting-the-kubelet-api/). The example command below illustrates MITRE ATT&CK technique T1528: Steal Application Access Token. The command reads the token from the pod’s filesystem and exfiltrates it to a remote command and control (C2) server. The token is embedded inside an HTTP header to make the traffic look like a normal authenticated request, as shown below in Figure 7.

![A screenshot of a code snippet showing a command using `curl` to send an HTTP request with an authorization token, retrieving a Kubernetes service account token from a path and sending it to an attacker control server URL.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-323083-177112-7.png)Figure 7. Command with service account token embedded into the HTTP header.

By exfiltrating this token, the threat actor gains the ability to authenticate to the Kubernetes API as that service account. Depending on how permissive the RBAC configuration is, this can allow the threat actor to list secrets, deploy new workloads, escalate privileges or move laterally across the cluster, effectively turning a single compromised pod into full cluster access.

[Cortex XQL queries](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Documentation/Cortex-XSIAM-XQL) give defenders the ability to drill into Kubernetes telemetry and expose subtle indicators of malicious activity within containerized environments. The following XQL query can be used to hunt in Cortex XSIAM for specific instances of curl or wget being used to exfiltrate a service account token.

dataset = xdr_data | filter actor_process_image_name in ("curl", "wget") | filter actor_process_command_line contains "/var/run/secrets/kubernetes.io/serviceaccount/token"

123 | dataset = xdr_data | filter actor_process_image_name in ("curl", "wget")| filter actor_process_command_line contains "/var/run/secrets/kubernetes.io/serviceaccount/token"  
---|---  
  
Figure 8 illustrates how suspicious Kubernetes events appear in real telemetry. The example shows an alert triggered by token‑access behavior inside a compromised pod misused by Peirates.

![A screenshot of Cortex XDR dashboard showing a sequence of running processes. The sequence includes icons and labels for "CGO," "python," "sh," and "peirates." Below, a table lists events with columns for timestamp, initiated by, action, and description. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-324785-177112-8.png)Figure 8. Peirates service account token access, detected by Cortex XDR.

For more information on detection capabilities for Kubernetes-related techniques, please see Appendix B.

## Practical Kubernetes Configurations for Security Teams

Events leading to Kubernetes compromise generally do not originate from a single, critical flaw. Instead, threat actors exploit small weaknesses which, when compounded, provide a foothold that can be leveraged for broad cluster or cloud-level compromise. These weaknesses may include overly permissive access, long-lived credentials and gaps in runtime behavior visibility.

Protecting modern Kubernetes clusters requires security teams to focus on controls that directly disrupt these attack paths:

  * Restricting what workloads can do
  * Expiring credentials quickly
  * Detecting malicious behavior as it happens



The following considerations outline practical steps that defenders can take to reduce impact radius, interrupt post-compromise workflows and gain important visibility when threat actors operate inside a cluster.

### 1\. Enforce Least Privilege Through Strict RBAC and Pod Security Standards

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/Blank-diagram-2-1-786x156.png)

Applying the principle of least privilege can prevent a single compromised application from escalating into full cluster control. Defenders enforce this principle by tightly controlling application actions through RBAC and constraining runtime behavior with Pod Security Standards ([PSS](https://kubernetes.io/docs/concepts/security/pod-security-standards/)). Broad RBAC permissions and permissive pod settings may simplify development and subsequent operations, but they remove the guardrails that inhibit threat actor activity after initial access.

Threat actors routinely exploit inadequate permission controls to move laterally after establishing a foothold. When RBAC roles allow wildcard permissions or pods run with elevated privileges, a single compromised container can expose sensitive APIs, credentials and cluster-wide resources. By enforcing narrowly-scoped RBAC roles and adopting the Restricted Pod Security profile, defenders isolate breaches and prevent threat actors from chaining small exploits into a full cluster takeover.

### 2\. Use Short-Lived, Projected Service Account Tokens

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/Blank-diagram-3-786x153.png)

Service account tokens act as identity badges for applications running inside Kubernetes. Historically, these tokens persisted for long periods and remained valid indefinitely, which made them prime targets for threat actors seeking stealthy persistence.

Application operators and developers can disrupt malicious token use by issuing short-lived, projected service account tokens. By binding tokens to a pod’s lifetime and limiting their validity window, teams significantly reduce the value of token theft. Threat actors who steal projected tokens gain only brief, narrowly-scoped access before the credentials expire and become unusable elsewhere.

### 3\. Improve Runtime Defense Through Continuous Monitoring

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/Blank-diagram-4-786x154.png)

Even well-hardened Kubernetes environments cannot prevent every exploit – especially as new vulnerabilities emerge. Runtime defense addresses this reality by monitoring workload behavior after deployment and identifying malicious activity that configuration checks and pre-deployment scans miss.

Modern runtime defense platforms, such as XDR solutions, detect abnormal process execution, unexpected network connections and unauthorized access to sensitive system paths from inside running containers. These tools can automatically terminate malicious pods the moment they deviate from expected behavior. This response limits threat actor dwell time, disrupts cryptomining and C2 activity, and preserves a forensic record of the threat actor’s actions.

Together, these controls directly undermine common Kubernetes post-exploitation frameworks such as Peirates. These frameworks depend on overly permissive configurations and limited runtime visibility to rapidly enumerate privileges, steal credentials, and escalate access after initial compromise. Detection hinges on visibility – especially into Kubernetes audit logs – for identifying and reconstructing threat actor activity.

## Conclusion

Modern threat actors continue to evolve their techniques for misusing Kubernetes environments. While previous campaigns from groups like SCARLETEEL and TeamTNT only targeted Kubernetes resources, newer campaigns – such as Slow Pisces activity – are using Kubernetes to expand access into the cloud and identity environments.

The recent cases highlighted in this article show just how quickly a single compromised identity can escalate into full cluster and cloud compromise. Security programs will increasingly need to treat cluster identity, workload behavior and API‑level visibility as core components of their defensive strategy.

Defenders require visibility that goes beyond container runtime events and into the identity‑driven behaviors happening inside the cluster. By combining Kubernetes audit logs with cloud telemetry and leveraging cloud runtime protection to correlate suspicious patterns, security teams can detect these techniques early and disrupt the threat actor’s progression before meaningful damage occurs. The goal isn’t just to spot a single command; it’s to understand the sequence, the intent and the identity behind it. Effective controls drastically reduce the Kubernetes attack surface, shifting the environment from a liability to a secure, governed asset.

### Palo Alto Networks Protection and Mitigation

The [Advanced WildFire](https://docs.paloaltonetworks.com/wildfire) machine-learning models and analysis techniques have been reviewed and updated in light of the indicators shared in this research.

[Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Advanced DNS Security](https://docs.paloaltonetworks.com/dns-security) identify known URLs and domains associated with this activity as malicious

The [Next-Generation Firewall](https://docs.paloaltonetworks.com/ngfw) with the [Advanced Threat Prevention](https://docs.paloaltonetworks.com/advanced-threat-prevention/administration) security subscription can help block attacks related to CVE-2025-55182 via Threat Prevention signatures 96779, 96780 and 96787, applied with best practices.

Palo Alto Networks Cortex Cloud provides several products which can assist organizations in protecting their Kubernetes and cloud environments.

  * [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud) customers are better protected by placing the [XDR endpoint agent throughout their](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection) cloud environment and on Kubernetes hosts. Cortex Cloud’s [runtime security](https://www.paloaltonetworks.com/cortex/cloud/runtime-security) operations include collection, analysis, detection, alerting and prevention of malicious operations on cloud platforms and SaaS application audit logs. Using behavioral and static alerting techniques on cloud logs during cloud operations during runtime, the techniques discussed within the article can be identified. Cortex Cloud can also trigger alerts which provide early warning and, in some cases, initiate prevention operations to prevent further compromise from these attacks.
  * Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security) encompasses Cloud Infrastructure Entitlement Management (CIEM), Identity Security Posture Management (ISPM), Data Access Governance (DAG) and Identity Threat Detection and Response (ITDR). It provides clients with the necessary capabilities to improve their identity-related security requirements by providing visibility into identities, and their permissions, within cloud and container environments. This helps accurately detect misconfigurations and unwanted access to sensitive data. It also allows real-time analysis surrounding usage and access patterns.
  * Cortex Cloud’s [Vulnerability Management](https://www.paloaltonetworks.com/cortex/cloud/vulnerability-management) identifies and manages the base images for cloud virtual machine and containerized environments, allowing for the identification and alerting of vulnerabilities and misconfigurations. The Cortex Cloud Agent can provide remediation tasks for identified base level container images.
  * Cortex Cloud uses the Known Exploited Vulnerabilities ([KEV](https://www.paloaltonetworks.com/blog/security-operations/cortex-xpanse-identify-cisa-kev/)) module to detect potential cloud vulnerabilities that don’t require file writes or changes to the state of service. This can include the usage of default credentials, operating system detection exposures, domain takeover operations and exposed or unmanaged cloud asset discovery. KEVs are the most likely to lead to a real exploitation operation. Cortex Cloud assists organizations in getting high-confidence alerts on the vulnerabilities discussed within this article.



The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Indicators of Compromise

  * 104.238.149[.]198
  * 45.76.155[.]14
  * 23.235.188[.]3
  * hxxp[:]//104.238.149[.]198:12349/BVN0VEdddye5odDFVR
  * hxxp[:]//45.76.155[.]14/vim



**VoidLink Binary**

  * 05eac3663d47a29da0d32f67e10d161f831138e10958dcd88b9dc97038948f69



**TeamPCP proxy.sh**

  * 7d2c9b4a3942f6029d2de7f73723b505b64caa8e1763e4eb1f134360465185d0



**TeamPCP kube.py**

  * bb470a803b6d7b12fb596d2e4a18ea9ca91f40fd34ded7f01a487eed9a1d814d



## Additional Resources

  * [BitoPro Statement & Progress Update: June 19, 2025](https://www.bitopro.com/ns/en-US/announcements/1226) – BitoPro
  * [Threat Alert: TeamPCP, An Emerging Force in the Cloud Native and Ransomware Landscape](https://flare.io/learn/resources/blog/teampcp-cloud-native-ransomware) – Flare
  * [inguardians/peirates - Kubernetes Penetration Testing tool](https://github.com/inguardians/peirates) – GitHub
  * [North Korea Responsible for $1.5 Billion Bybit Hack](https://www.ic3.gov/psa/2025/psa250226) – Internet Crime Complaint Center (IC3)
  * [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) – Kubernetes
  * [Understanding the threat landscape for Kubernetes and containerized assets | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2025/04/23/understanding-the-threat-landscape-for-kubernetes-and-containerized-assets/) – Microsoft Security
  * [Exploit Public-Facing Application, Technique T1190 - Enterprise](https://attack.mitre.org/techniques/T1190/) – MITRE ATT&CK®
  * [Steal Application Access Token, Technique T1528 - Enterprise | MITRE ATT&CK](https://attack.mitre.org/techniques/T1528/)
  * [Peirates, Software S0683](https://attack.mitre.org/software/S0683/) – MITRE ATT&CK®
  * [VoidLink: Dissecting an AI-Generated C2 Implant](https://www.ontinue.com/resource/voidlink-dissecting-an-ai-generated-c2-implant/) – Ontinue
  * [Kubernetes Privilege Escalation: Excessive Permissions in Popular Platforms](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms) – Palo Alto Networks
  * [Critical Security Vulnerability in React Server Components](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components) – React
  * [Climbing The Ladder | Kubernetes Privilege Escalation (Part 1)](https://www.sentinelone.com/blog/climbing-the-ladder-kubernetes-privilege-escalation-part-1/) – SentinelOne
  * [SCARLETEEL 2.0: Fargate, Kubernetes, and Crypto](https://www.sysdig.com/blog/scarleteel-2-0) – Sysdig
  * [Container Breakouts: Escape Techniques in Cloud Environments](https://unit42.paloaltonetworks.com/container-escape-techniques/) – Unit 42, Palo Alto Networks
  * [Exploitation of Critical Vulnerability in React Server Components (Updated December 12)](https://unit42.paloaltonetworks.com/cve-2025-55182-react-and-cve-2025-66478-next/) – Unit 42, Palo Alto Networks
  * [Hildegard: New TeamTNT Cryptojacking Malware Targeting Kubernetes](https://unit42.paloaltonetworks.com/hildegard-malware-teamtnt/) – Unit 42, Palo Alto Networks
  * [Managing Permissions with Kubernetes RBAC](https://www.paloaltonetworks.com/cyberpedia/kubernetes-rbac) – Unit 42, Palo Alto Networks
  * [Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms](https://unit42.paloaltonetworks.com/kubernetes-privilege-escalation/) – Unit 42, Palo Alto Networks
  * [Roles Here? Roles There? Roles Anywhere: Exploring the Security of AWS IAM Roles Anywhere](https://unit42.paloaltonetworks.com/aws-roles-anywhere/) – Unit 42, Palo Alto Networks
  * [TeamTNT Operations Actively Enumerating Cloud Environments](https://unit42.paloaltonetworks.com/teamtnt-operations-cloud-environments/) – Unit 42, Palo Alto Networks
  * [Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/) – Unit 42, Palo Alto Networks
  * [Exploiting Monitoring and Service Mesh Configurations and Privileges in GKE to Gain Unauthorized Access in Kubernetes](https://unit42.paloaltonetworks.com/google-kubernetes-engine-privilege-escalation-fluentbit-anthos/) – Unit 42, Palo Alto Networks



## Appendix A: Alert Activity Data

Based on our telemetry, Table 1 represents total Kubernetes alerts (Severity ≥ Low), where the activity took place within a Kubernetes environment and the MITRE ATT&CK technique ID was related to token theft. The December 2025 increase is attributed to the high volume of activity related to CVE-2025-55182 React2Shell.

**Year** | **Jan** | **Feb** | **Mar** | **Apr** | **May** | **Jun** | **Jul** | **Aug** | **Sep** | **Oct** | **Nov** | **Dec** | **Total**  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
**2024** | 37,778 | 9,318 | 10,870 | 10,269 | 11,526 | 10,882 | 11,130 | 1,916 | 2,383 | 2,946 | 4,158 | 9,289 | **122,465**  
**2025** | 13,322 | 14,835 | 13,472 | 14,895 | 17,499 | 11,171 | 14,986 | 28,357 | 19,728 | 24,924 | 19,259 | 275,210 | **467,658**  
  
Table 1. Kubernetes alert counts in 2024 and 2025.

Table 2 shows a sector breakdown based on the top 50 tenants by alert volume, representing 97.6% of total alert volume.

**GICS Sector** | **Percent of Alerts**  
---|---  
Information Technology | 78%  
Communication Services | 7%  
Consumer Discretionary | 6%  
Industrials | 4%  
Financials | 2%  
Energy | 1%  
Health Care | 1%  
Public Sector | <1%  
  
Table 2. 2025 alert volume by sector, top 50 tenants.

## Appendix B: Cortex Detections

**MITRE Technique** | **Cortex Alert Names**  
---|---  
T1528 - Steal Application Access Token T1552.001 - Unsecured Credentials: Credentials In Files | 

  * Suspicious Kubernetes service account token read by an unusual process
  * Suspicious Kubernetes service account file read by an unusual process
  * Suspicious Kubernetes service account token read

  
T1552.007 - Unsecured Credentials: Container API | 

  * Kubernetes secret enumeration activity from a host

  
T1613 - Container and Resource Discovery | 

  * Unusual Kubernetes API server communication from a pod
  * Unusual Kubernetes API server communication from within a pod performed by curl process

  
T1609 - Container Administration Command | 

  * Unusual exec into a Kubernetes Pod

  
T1134 - Access Token Manipulation | 

  * Execution of command from within a Kubernetes pod using kubelet credentials

  
T1609 - Container Administration Command | 

  * Remote code execution into Kubernetes Pod
  * Suspicious container runtime connection from within a Kubernetes Pod using the curl client

  
T1610 - Deploy Container T1611 - Escape to Host | 

  * Suspicious container runtime connection from within a Kubernetes Pod
  * Kubernetes pod creation from unknown container image registry
  * Kubernetes Pod Created With Sensitive Volume

  
T1078.001 - Valid Accounts: Default Accounts | 

  * A Kubernetes API operation was successfully invoked by an anonymous user

  
T1552.005 - Unsecured Credentials: Cloud Instance Metadata API | 

  * Unusual cloud Instance Metadata Service (IMDS) access

  
T1059.004 - Command and Scripting Interpreter: Unix Shell | 

  * Run downloaded script using pipe in a Kubernetes pod

  
T1098.006 - Account Manipulation: Additional Container Cluster Roles | 

  * A Kubernetes cluster role binding was created or deleted

  
  
Back to top

### Tags

  * [Audit logs](https://unit42.paloaltonetworks.com/tag/audit-logs/ "audit logs")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/ "Kubernetes")
  * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")
  * [Queries](https://unit42.paloaltonetworks.com/tag/queries/ "queries")
  * [React server](https://unit42.paloaltonetworks.com/tag/react-server/ "react server")
  * [React2shell](https://unit42.paloaltonetworks.com/tag/react2shell/ "react2shell")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications ](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/ "When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications")

### Table of Contents

  *   * Executive Summary
  * The Kubernetes Cloud Attack Surface
  * Threat Actor Activity
    * Case 1: Token Theft and Lateral Movement in a Crypto Platform
      * Earlier Campaign Activity
      * From One Exchange to Another
    * Case 2: Exploitation of React2Shell, CVE-2025-55182
  * Tooling and TTPs
    * T1190 Exploit Public-Facing Application
    * T1528 Steal Application Access Token
    * S0683 Peirates
  * Kubernetes Threat Detection
    * Log Data Sources: Kubernetes Audit Logs
    * Runtime Telemetry and Behavioral Analysis
    * Threat Hunting and Alerting with Cortex XQL
  * Practical Kubernetes Configurations for Security Teams
    * 1\. Enforce Least Privilege Through Strict RBAC and Pod Security Standards
    * 2\. Use Short-Lived, Projected Service Account Tokens
    * 3\. Improve Runtime Defense Through Continuous Monitoring
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Indicators of Compromise
  * Additional Resources
  * Appendix A: Alert Activity Data
  * Appendix B: Cortex Detections



### Related Articles

  * [ Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "article - table of contents")
  * [ Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "article - table of contents")
  * [ Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/)