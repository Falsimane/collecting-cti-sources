# Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/
- **Date :** 2026-04-07

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 13 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI Security Assessment](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Ori Hadad](https://unit42.paloaltonetworks.com/author/ori-hadad/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:April 7, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/)
    * [Agentcore runtime](https://unit42.paloaltonetworks.com/tag/agentcore-runtime/)
    * [AWS](https://unit42.paloaltonetworks.com/tag/aws/)
    * [DNS tunneling](https://unit42.paloaltonetworks.com/tag/dns-tunneling/)
    * [GenAI](https://unit42.paloaltonetworks.com/tag/genai/)
    * [Sandbox](https://unit42.paloaltonetworks.com/tag/sandbox/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/?pdf=download&lg=en&_wpnonce=252a1929a6 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/?pdf=print&lg=en&_wpnonce=252a1929a6 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Cracks%20in%20the%20Bedrock:%20Escaping%20the%20AWS%20AgentCore%20Sandbox&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fbypass-of-aws-sandbox-network-isolation-mode%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbypass-of-aws-sandbox-network-isolation-mode%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbypass-of-aws-sandbox-network-isolation-mode%2F&title=Cracks%20in%20the%20Bedrock:%20Escaping%20the%20AWS%20AgentCore%20Sandbox "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbypass-of-aws-sandbox-network-isolation-mode%2F&text=Cracks%20in%20the%20Bedrock:%20Escaping%20the%20AWS%20AgentCore%20Sandbox "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbypass-of-aws-sandbox-network-isolation-mode%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Cracks%20in%20the%20Bedrock:%20Escaping%20the%20AWS%20AgentCore%20Sandbox%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fbypass-of-aws-sandbox-network-isolation-mode%2F "Share in Mastodon")



## Executive Summary

When researching the boundaries of cloud services, two of the main aspects that come to mind are network and identity. In this two-part series, we present our research into the boundaries and resilience of Amazon Bedrock AgentCore. In this first part, we explore how AgentCore’s Code Interpreter sandbox network isolation mode could be bypassed in a way that allows sending and receiving of data from external endpoints via DNS tunneling. In the second part, we explore the identity side, and how an attacker can leverage weaknesses in default identities and permissions to compromise other AgentCore agents within an AWS account and exfiltrate sensitive data from other services.

To support the growing adoption of AI agents, AWS announced global availability of [Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-agentcore-code-interpreter/) in late 2025. AgentCore is a framework that allows organizations to build, deploy and manage AI agents. It protects one of its most useful resources, Code Interpreters, that allows AI agents to dynamically execute code by isolating it from external network access using sandbox mode. Our discovery showed that this isolation is incomplete. We outline the steps we took to identify the sandbox bypass.

We also identified a critical security regression where the [AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) utilized a microVM Metadata Service (MMDS) that lacks session token enforcement. Prior to our disclosure and AWS's fixes, this configuration could have allowed an attacker to exploit standard web vulnerabilities, such as server-side request forgery ([SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)), to directly extract sensitive credentials, putting the entire environment at risk.

We responsibly disclosed all findings to the AWS Security team. Following their review, AWS introduced the necessary internal remediations and outlined several important mitigation strategies for customers. Users cannot patch the managed environment directly, but can leverage the platform-level controls AWS provides.

As reliance on these services grows, understanding their internal mechanics is crucial for maintaining security.

Palo Alto Networks customers are better protected from the threats discussed in this article through the following products and services:

  * [Cortex AI-SPM](https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management)
  * Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security)
  * The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)
  * The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Cloud](https://unit42.paloaltonetworks.com/tag/cloud/), [DNS Tunneling](https://unit42.paloaltonetworks.com/tag/dns-tunneling/), [Sandbox](https://unit42.paloaltonetworks.com/tag/sandbox/), **  
---|---  
  
## Investigation Overview: Scope, Methodology and Key Findings

Our investigation focused on the Code Interpreter service provided by [AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html), which offers an isolated sandbox compute environment for AI agents to execute their code. The sandbox mode promises an easy way to implement restrictions on network access, which serves as an important containment layer for untrusted code. This restriction is critical to the security model of AgentCore. Originally, AWS [described sandbox mode](https://web.archive.org/web/20250731114200/https:/docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-create.html) as providing “complete isolation with no external access.” Our research revealed that the restrictions of sandbox mode were not as complete as originally described. We analyzed the robustness of this architecture, to determine the efficacy of the sandbox isolation boundaries and the scope of access available from within the sandbox.

After performing environmental reconnaissance, we observed the existence of external network connectivity, which directly conflicted with the stated "no external network access" policy of the sandbox mode. We tested the network permeability by mapping the boundaries of the DNS resolution capability through incremental testing and discovered a channel for data exfiltration: [DNS tunneling](https://www.paloaltonetworks.com/cyberpedia/what-is-dns-tunneling).

Watching our DNS server logs, we saw the query arrive instantly, establishing a covert bi-directional channel out of the sandbox. We had successfully turned a "secure, offline" environment into a potential privileged data exfiltration pipeline.

After sharing our findings with AWS, they updated their [developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-resource-management.html) to state that the sandbox mode provides limited external network access, increasing transparency for users.

## Technical Analysis

We set out to test whether AgentCore’s network isolation contained hidden egress paths that are necessary for internal AWS operations. We first studied the system’s architecture to select core components for deep analysis. Following this, we performed internal reconnaissance and metadata inspection to map potential vulnerabilities. These steps ultimately allowed us to validate our hypothesis by successfully demonstrating DNS tunneling. In the following sections, we detail the step-by-step methodology we used to execute this exploit.

### AgentCore Architecture and Isolation

Our research focused on two aspects of AgentCore’s services: the Code Interpreter tool and the AgentCore Runtime. [AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html) is one of several built-in tools for AI agents, designed specifically to execute code, often generated dynamically by large language models (LLMs). The service supports three network configurations:

  * **Public mode** : Provides external internet access for fetching data or libraries.
  * **Sandbox mode** : A strictly isolated environment with no external network connectivity.
  * **Virtual Private Cloud (VPC) mode:** Provides the ability to connect the Code Interpreter to a customer-controlled VPC.



We chose to examine the sandbox mode, as this configuration is considered to be entirely isolated from external networks. This means that if the Code Interpreter configured with sandbox mode is compromised, it still should not be possible to exfiltrate data or to use the interpreter as part of a command and control (C2) channel. Figure 1 shows the Sandbox mode description.

![A screenshot of instructions from the AWS console webpage, detailing steps to create a Code Interpreter. Key points include navigating to the Built-in tools, selecting a Tool name and Description, and choosing Network settings. Sandbox, highlighted in red, is noted as a secure option with no external network access.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-155351-177263-1.png)Figure 1. AgentCore Code Interpreter documentation, prior to AWS's update.

[AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) is a managed environment that executes the core logic of a deployed AI agent. Each interaction with an AI agent goes through an instance of AgentCore Runtime, making it a central pillar of the agent architecture.

To fully understand the risks of escaping the sandbox mode or abusing the Runtime environment, we first needed to understand how their underlying metadata is managed. Both services operate on ephemeral microVMs, which are lightweight, hardened virtualization units created per session to ensure distinct isolation between tasks. A critical aspect of this architecture is how these microVMs maintain context. They use a microVM Metadata Service (MMDS), which is structurally similar to the well-known EC2 Instance Metadata Service ([IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)). Just as IMDS provides credentials and metadata to an EC2 instance, MMDS serves as the internal metadata server for the microVM.

With a clear understanding of the architecture and metadata management in place, we can now walk through the chronological phases of our investigation.

### Phase 1: Internal Reconnaissance

Our analysis commenced with a baseline scenario: executing arbitrary code within the Code Interpreter. This is the intended functionality of the service, as users and AI agents are designed to execute dynamic scripts in this environment. Upon establishing this context, we began our environmental reconnaissance by investigating the microVM architecture and MMDS accessibility.

In modern AWS EC2 environments, accessing metadata usually defaults to IMDSv2 (although IMDSv1 is not actually disabled by default), which mandates a session token (HTTP PUT request) to mitigate SSRF attacks. However, we observed that the microVM’s MMDS endpoint was configured to accept standard HTTP GET requests without requiring a session token, as Figure 2 shows.

![A screenshot of a code editor with Python code involving AWS metadata querying. A portion of the code is highlighted. Below, the formatted JSON response with AWS credentials is displayed. Sensitive data in the JSON is blurred for security.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-158022-177263-2.png)Figure 2. MMDS response containing the executing role credentials.

Not requiring a session token posed serious implications for the runtime environment. AgentCore Runtime hosts the AI agent's application logic and is not designed for arbitrary user code execution. However, if an AI agent contains a standard web vulnerability like SSRF, the absence of token enforcement leads to the same risks that are found in [legacy EC2](https://blog.qualys.com/vulnerabilities-threat-research/2024/09/12/totalcloud-insights-unmasking-aws-instance-metadata-service-v1-imdsv1-the-hidden-flaw-in-aws-security) IMDSv1 configurations. A simple SSRF vector could allow an external actor to retrieve the AI agent's identity and access management (IAM) role credentials directly, posing a significant security risk for the entire environment.

In the Code Interpreter environment, where arbitrary code execution is an intended feature, this same configuration primarily simplifies the retrieval of credentials and does not function as a vulnerability in itself, regardless of whether v1 or v2 MMDS protocols are used.

With credential access confirmed locally, our investigation shifted to the integrity of the network boundaries. Under the sandbox mode's design specifications, the absence of an outbound network route effectively neutralizes the risk of data exfiltration, effectively trapping the compromised credentials within the microVM.

### Phase 2: The Clue in the Metadata

We extended our metadata analysis to identify additional configuration parameters that are exposed within the MMDS hierarchy. A systematic traversal of the latest/meta-data/tags/instance/ path revealed two undocumented endpoints:

  * http[:]//169.254.169[.]254/latest/meta-data/tags/instance/aws_presigned-log-url
  * http[:]//169.254.169[.]254/latest/meta-data/tags/instance/aws_presigned-log-kms-key



Querying these endpoints returned a pre-signed URL for an S3 bucket and a corresponding Key Management Service (KMS) Key ID. These resources appeared to belong to an internal AWS account, likely used by the backend infrastructure for log aggregation.

While the URLs themselves were a secondary concern, their existence provided a critical clue about the network architecture and its connectivity. The provision of an S3 pre-signed URL implies a functional requirement for the microVM to transmit data to Amazon S3. Since standard S3 endpoints (such as bucket.s3.region.amazonaws[.]com) are resolved via DNS resolution, the environment might theoretically have a mechanism to resolve and route traffic to external DNS servers and to these S3 endpoints.

This observation presents an architectural conflict with the originally stated "no external network access" policy of the sandbox mode. The necessity to support S3 traffic suggests that the isolation is not absolute, but rather conditionally permeable. Such behavior implies the presence of an allow-list or a transparent proxy designed to facilitate specific AWS service interactions.

This observation directed our analysis to the foundation of the network stack: DNS.

### Phase 3: The Great Escape

To validate our hypothesis of the network’s permeability, we executed a series of targeted tests within the Code Interpreter. Our objective was to map the boundaries of the DNS resolution capability through incremental testing.

#### Test 1: Internal Service Resolution (Control)

We began by querying a standard AWS service endpoint. Given that the endpoint is likely used for log aggregation, we anticipated that this query would succeed:

socket.gethostbyname_ex("s3.us-east-1.amazonaws[.]com")

1 | socket.gethostbyname_ex("s3.us-east-1.amazonaws[.]com")  
---|---  
  
As expected, the environment successfully resolved the internal AWS endpoint.

#### Test 2: External Domain Resolution

Next, we attempted to resolve an external public domain completely unrelated to AWS infrastructure. In a strictly isolated sandbox environment, DNS queries are typically restricted. The code below shows how we attempted to resolve google[.]com from within the sandbox.

socket.gethostbyname_ex("google[.]com")

1 | socket.gethostbyname_ex("google[.]com")  
---|---  
  
The query resolved successfully, confirming that although the sandbox blocks direct TCP/UDP data traffic to these IP addresses, it might permit recursive DNS queries to arbitrary public domains.

#### Proof of Concept: Exploiting the DNS Egress Vector

This sandbox design reveals a channel for data exfiltration: DNS tunneling. Even in environments where direct internet access is severed, the ability to resolve arbitrary domain names allows for bidirectional communication via the DNS protocol itself.

To demonstrate the feasibility of the egress vector, we configured an authoritative nameserver for a domain under our control: dnshook[.]site. We then designed a proof-of-concept (PoC) payload to validate the communication path.

The PoC is executed according to the following logic:

  1. Identify sensitive information: my-secret.
  2. Append the data as a subdomain to the controlled domain: my-secret.dnshook[.]site.
  3. Trigger a DNS resolution request from within the Code Interpreter.
  4. The sandbox's recursive resolver forwards the query to our authoritative nameserver, where the "subdomain" – the leaked data – is logged.



Figure 3 details the PoC script.

![A screenshot of a Python script using the socket library. The script defines a function that takes a domain as an argument and attempts to retrieve its canonical name, aliases, and IP addresses. If resolution fails, it prints an error message. The function is called with a sample domain at the bottom.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-161273-177263-3.png)Figure 3. A PoC script to escape the sandbox via DNS tunneling.

Upon execution, our authoritative nameserver immediately received the query, confirming that the data had successfully traversed the sandbox boundary, as shown in Figure 4.

![A screenshot of a webpage from Webhook site. It displays request details like IP address, location, date, time, size, and ID. On the left, there are DNS entries and timestamps.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-163280-177263-4.png)Figure 4. Confirming the DNS server received the DNS query.

Finally, as shown in Figure 5, performing a Whois lookup on the incoming IP address confirmed the traffic originated directly from AWS infrastructure, validating that the Code Interpreter environment was the source of the transmission.

![a screenshot of IP information. The IP is located in Ashburn, Virginia, and is associated with Amazon Data Services. It includes the ASN number, and the net range with CIDR. The IP status is listed as "Direct Allocation".](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-165160-177263-5.png)Figure 5. Whois lookup results.

Video 1 shows the PoC in action.

&lt;span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start"&gt;﻿&lt;/span&gt;&lt;span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start"&gt;﻿&lt;/span&gt;&lt;br /&gt; 

Video 1. Escaping the sandbox PoC.

#### The Impact

Watching our DNS server logs, we saw the query arrive instantly, establishing a covert channel out of the sandbox.

Crucially, this vector is not limited to data exfiltration; it establishes a bidirectional communication channel capable of both outbound and inbound traffic.

  1. **Exfiltration (outbound):** An attacker can encode sensitive data – such as environment variables, source code, or the IAM credentials retrieved in Phase 1 – into Base64 subdomains and tunnel them out.
  2. **C2 (inbound):** The code inside the sandbox can receive instructions or payloads from the attacker's server in the form of DNS response. This effectively enables a full C2 loop over DNS.



To summarize so far, this capability is particularly dangerous in the context of identity. Because users trust the "sandbox" guarantee, they often attach highly privileged IAM roles to these interpreters – permissions they would never grant to a public mode Code Interpreter.

### Phase 4: Beyond the Sandbox

Following the confirmation of DNS egress and credential accessibility, the analysis returned to the metadata anomalies identified in Phase 2. As previously noted, the MMDS traversal revealed two undocumented endpoints:

  * http[:]//169.254.169[.]254/.../instance/aws_presigned-log-url
  * http[:]//169.254.169[.]254/.../instance/aws_presigned-log-kms-key



Upon closer inspection, these endpoints represent a distinct finding. We confirmed that code executing within the Code Interpreter (or AgentCore Runtime) can query these paths to retrieve a valid S3 pre-signed URL and a corresponding KMS Key ID. The returned URL targets an internal, AWS-controlled S3 bucket, as displayed in Figure 6.

![A screenshot of a terminal with command-line text. The code includes a command to run a Python script. There are various URLs, identifiers, and data strings visible. One section is highlighted in red. The background is dark, consistent with a typical coding environment.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-167070-177263-6.png)Figure 6. Presigned URL and KMS Key response from MMDS.

#### Scoped S3 ObjectWrite

The combination of the pre-signed URL and the KMS Key ID provides the necessary components to construct a valid HTTP PUT request that could be sent to the target bucket.

It is important to note that this write access appears to be scoped, and not arbitrary. The pre-signed URL restricts uploads to a specific object key path. This restriction prevents writing to arbitrary paths and limits the impact radius. AWS confirmed that AWS’s own service code uses this pre-signed URL to upload service-related logging information to a specific location owned by the service.

#### Infrastructure Leak

Interacting with these endpoints revealed internal infrastructure details. When sending a malformed request (by breaking the signature) to the pre-signed URL, the server responds with a SignatureDoesNotMatch error.

This server error message includes the AWSAccessKeyID of the signing identity, as Figure 7 shows.

!["A screenshot of a terminal window displaying an error message from Amazon Web Services \(AWS\). The message indicates a signature mismatch, with a section highlighted around the text `AWSAccessKeyId`. It includes a CURL command that failed, along with details of the error response.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-169930-177263-7.png)Figure 7. An error that reveals AWS Access Key ID.

After extracting this Key ID, we used the AWS Security Token Service ([STS](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)) command-line interface to show information about the Key ID:

$ aws sts get-access-key-info --access-key-id ASI...X6L

1 | $ aws sts get-access-key-info \--access-key-id ASI...X6L  
---|---  
  
The response revealed the owning account:

{ "Account": "209...9" }

123 | { "Account": "209...9"}  
---|---  
  
This confirmed that we were interacting with account 209...9, which appears to be an internal AWS environment that is hidden behind the service abstraction, separate from our own environments.

## Mitigation and Collaboration With AWS

After we shared our findings, AWS clarified that the AgentCore Code Interpreter offers three network modes: Sandbox, Public network, and VPC. AWS recommends [VPC Mode](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html) for customers requiring complete network isolation. To specifically mitigate DNS-based exfiltration, customers using VPC Mode can implement Amazon Route 53 Resolver DNS Firewall. AgentCore has since updated its [developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-resource-management.html) to explicitly clarify sandbox mode’s capabilities, noting that “the code interpreter can access Amazon S3 for data operations and perform DNS resolution.”

In response to our research regarding the S3 pre-signed URLs and metadata exposure, AWS confirmed that this represents expected behavior. The access keys and account IDs are part of the backend infrastructure, do not belong to customer accounts, and the pre-signed URLs are narrowly scoped to their intended logging function.

AWS also informed us that they have made a number of improvements to the behavior of MMDS in AgentCore. Specifically, as of Feb. 14, 2026, any AWS account in which customers had not previously utilized Runtime, Browser or Code Interpreter microVMs will launch new runtimes and tools with MMDSv2 only. Even for accounts that had been using these capabilities prior to that date, all newly deployed agents will launch with MMDSv2 only.

The Browser and Code Interpreter tools now have both MMDSv1 and v2 available by default.

We appreciate the transparent collaboration with the AWS Security team in assessing these findings.

### Disclosure Timeline

  * Nov. 17, 2025 – We responsibly reported to the AWS Security team.
  * Nov. 18, 2025 – AWS Security team responded that they are investigating.
  * Dec. 14, 2025 – AWS Security team reached out for more details.
  * Jan. 28, 2026 – AWS Security team provided clarifications regarding our findings and commitment for internal remediations.
  * Feb. 14, 2026 – AWS set MMDSv2 as the default for new agents, provided an API for disabling v1 on older agents, and made v2 available in AgentCore tools.



## Conclusion

Our research into AWS AgentCore reveals that despite the "sandbox" label, the underlying mechanisms of cloud, network and identity still apply – and their integrity can still be broken. Developers must adopt a shared responsibility mindset when utilizing sandbox environments. It is critical to maintain the principle of least privilege for agent permissions, and to view a sandbox environment as a boundary, rather than an absolute security guarantee.

The discovery of internal S3 write access and the leakage of backend Account IDs highlight that the abstraction layer between the tenant and the cloud provider offers less isolation than anticipated. Our research shows that cloud providers sometimes use customer-facing features to enable capabilities like log collection, and accept the risk inherent in this setup.

By chaining together DNS Tunneling and the legacy MMDSv1 configuration, we demonstrated a complete attack:

  1. **Break out:** Escaping the network sandbox using DNS recursion.
  2. **Break in:** Accessing the AI agent’s identity via an unprotected metadata service.
  3. **Exfiltrate:** Tunneling sensitive IAM credentials to an external attacker.



The impact of this attack defeats the primary purpose of an isolated environment. It allows an attacker to bypass network controls, exfiltrate credentials and execute remote commands without triggering standard network alarms. A successful exploit allows attackers to establish a persistent bidirectional C2 channel, turning a trusted AI agent into an internal threat vector.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

Organizations are better equipped to [close the AI security gap](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/close-ai-security-gap) through the deployment of [Cortex AI-SPM](https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management), which helps to provide comprehensive visibility and posture management for AI agents across AWS and Azure environments. Cortex AI-SPM is designed to mitigate critical risks, including over-privileged AI agent access, misconfigurations and unauthorized data exposure. Cortex AI-SPM helps enable security teams to enforce compliance with NIST and OWASP standards, monitor for real-time behavioral anomalies, and secure the entire AI lifecycle within a unified cloud security context.

Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security) encompasses Cloud Infrastructure Entitlement Management (CIEM), Identity Security Posture Management (ISPM), Data Access Governance (DAG) and Identity Threat Detection and Response (ITDR). It provides clients with the necessary capabilities to improve their identity-related security requirements by providing visibility into identities, and their permissions, within cloud and container environments. This helps accurately detect misconfigurations and unwanted access to sensitive data. It also allows real-time analysis surrounding usage and access patterns.

The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment) can help empower safe AI use and development.

The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

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

  * [What is Amazon Bedrock AgentCore?](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) – AWS documentation
  * [Understanding Credentials Management in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security-credentials-management.html) – AWS documentation
  * [What Is DNS Tunneling?](https://www.paloaltonetworks.com/cyberpedia/what-is-dns-tunneling) – Palo Alto Networks
  * [When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/) – Unit 42
  * [AWS IMDSv1 Vulnerability Exposed: Insights from TotalCloud](https://blog.qualys.com/vulnerabilities-threat-research/2024/09/12/totalcloud-insights-unmasking-aws-instance-metadata-service-v1-imdsv1-the-hidden-flaw-in-aws-security) – Qualys



Back to top

### Tags

  * [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/ "agentcore")
  * [Agentcore runtime](https://unit42.paloaltonetworks.com/tag/agentcore-runtime/ "agentcore runtime")
  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [DNS tunneling](https://unit42.paloaltonetworks.com/tag/dns-tunneling/ "DNS tunneling")
  * [GenAI](https://unit42.paloaltonetworks.com/tag/genai/ "GenAI")
  * [Sandbox](https://unit42.paloaltonetworks.com/tag/sandbox/ "Sandbox")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Understanding Current Threats to Kubernetes Environments ](https://unit42.paloaltonetworks.com/modern-kubernetes-threats/ "Understanding Current Threats to Kubernetes Environments")

### Table of Contents

  *   * Executive Summary
  * Investigation Overview: Scope, Methodology and Key Findings
  * Technical Analysis
    * AgentCore Architecture and Isolation
    * Phase 1: Internal Reconnaissance
    * Phase 2: The Clue in the Metadata
    * Phase 3: The Great Escape
      * Test 1: Internal Service Resolution (Control)
      * Test 2: External Domain Resolution
      * Proof of Concept: Exploiting the DNS Egress Vector
      * The Impact
    * Phase 4: Beyond the Sandbox
      * Scoped S3 ObjectWrite
      * Infrastructure Leak
  * Mitigation and Collaboration With AWS
    * Disclosure Timeline
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Additional Resources



### Related Articles

  * [ The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "article - table of contents")
  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ That AI Extension Helping You Write Emails? It’s Reading Them First ](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/)