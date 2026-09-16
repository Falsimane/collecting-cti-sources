# Cracks in the Bedrock: Agent God Mode

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/
- **Date :** 2026-04-08

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Cracks in the Bedrock: Agent God Mode

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 8 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI Security Assessment](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Ori Hadad](https://unit42.paloaltonetworks.com/author/ori-hadad/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:April 8, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/)
    * [AI agents](https://unit42.paloaltonetworks.com/tag/ai-agents/)
    * [AWS](https://unit42.paloaltonetworks.com/tag/aws/)
    * [Bedrock](https://unit42.paloaltonetworks.com/tag/bedrock/)
    * [DNS tunneling](https://unit42.paloaltonetworks.com/tag/dns-tunneling/)
    * [Exfiltration](https://unit42.paloaltonetworks.com/tag/exfiltration/)
    * [IAM](https://unit42.paloaltonetworks.com/tag/iam/)
    * [Identity](https://unit42.paloaltonetworks.com/tag/identity/)
    * [Killchain](https://unit42.paloaltonetworks.com/tag/killchain/)
    * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)
    * [Sandbox](https://unit42.paloaltonetworks.com/tag/sandbox/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Cracks%20in%20the%20Bedrock:%20Agent%20God%20Mode&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fexploit-of-aws-agentcore-iam-god-mode%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fexploit-of-aws-agentcore-iam-god-mode%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fexploit-of-aws-agentcore-iam-god-mode%2F&title=Cracks%20in%20the%20Bedrock:%20Agent%20God%20Mode "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fexploit-of-aws-agentcore-iam-god-mode%2F&text=Cracks%20in%20the%20Bedrock:%20Agent%20God%20Mode "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fexploit-of-aws-agentcore-iam-god-mode%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Cracks%20in%20the%20Bedrock:%20Agent%20God%20Mode%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fexploit-of-aws-agentcore-iam-god-mode%2F "Share in Mastodon")



## Executive Summary

[Our first article ](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/)about the boundaries and resilience of Amazon Bedrock AgentCore focused on the Code Interpreter sandbox, and how it can be bypassed using DNS tunneling. In this second part, we delve into the identity and permissions model of AgentCore and the [AgentCore starter toolkit](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-toolkit.html). This toolkit is described by AWS as “a Command Line Interface (CLI) toolkit that you can use to deploy AI agents to an Amazon Bedrock AgentCore Runtime.” This toolkit abstracts backend provisioning complexity by automating the creation of runtimes, Amazon Elastic Container Registry ([ECR](https://aws.amazon.com/ecr/)) images and execution roles. We discovered that the toolkit’s auto-create logic generates identity and access management (IAM) roles that grant privileges broadly across the AWS account, rather than being scoped to individual resources. While the toolkit makes it easy to quick-start with AgentCore, the default deployment configuration model favors this deployment ease over a strict adherence to the principle of least privilege.

​​The starter toolkit’s default deployment configuration introduces an attack vector that we call Agent God Mode, because the overly broad IAM permissions effectively grant an individual agent the “omniscient” ability to escalate privileges and compromise every other AgentCore agent within the AWS account.

Our investigation uncovered a multi-stage attack chain that exploits this excessive access. We found that an attacker who compromises an agent could:

  * Exfiltrate proprietary ECR images
  * Access other agents’ memories
  * Invoke every code interpreter
  * Extract sensitive data



We disclosed our findings to the AWS Security team. Following our disclosure, the AWS [documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-permissions.html) was updated to include a security warning, stating that the default roles are "designed for development and testing purposes" and are not recommended for production deployment, as shown in Figure 1.

![A screenshot of a webpage section titled "Use the starter toolkit" from Amazon Bedrock AgentCore. It explains the IAM policy's purpose and emphasizes that it is for development and testing. A note highlighted with an exclamation icon warns users about the unsuitability of these permissions for production and suggests creating custom IAM policies.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-665123-177420-1.png)Figure 1. AWS starter toolkit updated documentation warning note.

Palo Alto Networks customers are better protected from the threats discussed in this article through the following products and services:

  * [Cortex AI-SPM](https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management)
  * Cortex Cloud [Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security)
  * The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment)
  * The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Cloud](https://unit42.paloaltonetworks.com/tag/cloud/), [IAM](https://unit42.paloaltonetworks.com/tag/iam/), [Privilege Escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)**  
---|---  
  
## Technical Analysis

Identity and permissions are two of the most critical pillars of setting boundaries and maintaining isolation in cloud workloads and applications. We explain the default IAM roles and permissions that are provisioned by the AgentCore starter toolkit, to demonstrate how compounding attack primitives ultimately enables a full attack chain.

### The Default Deployment Architecture

We began our analysis by evaluating the default IAM roles that the toolkit’s setup process automatically generates. The agentcore launch command automates the infrastructure provisioning required for an AI agent. Based on the user's configuration, the toolkit creates:

  * The AgentCore Runtime
  * A memory store
  * An ECR Repository
  * An IAM execution role



Figure 2 shows this configuration, created with the Agent Name ori_agent_01.

![A screenshot showing configuration details of an agent deployment. The list includes a region and mentions an obscured account number. Key configuration settings are highlighted and the memory retention is set to 30 days.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-667275-177420-2.png)Figure 2. Starter toolkit configuration.

Upon execution, the toolkit confirms the deployment and associated resources, as shown in Figure 3.

![A screenshot of a deployment success message displaying details about an agent. It includes an Agent ARN, an ECR URI with AWS and Amazon's domains, and ARM64 container deployment confirmation to Bedrock AgentCore.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-669339-177420-3.png)Figure 3. Starter toolkit deployment.

Although the toolkit simplifies the setup, the auto-create configuration for the execution role introduces a significant security risk.

### Cross-Agent Data Access

AgentCore agents rely on memory resources to store both long and short-term conversation state and context. An attacker who gains read access to this resource could exfiltrate sensitive interaction data between the AI agent and its users. The default IAM policy generated by the toolkit reveals the permission set, as Figure 4 shows.

![A screenshot of a code snippet displaying a JSON policy configuration for AWS. The policy allows specific actions related to "bedrock-agentcore," such as creating events, getting events, and managing memory records. The resource is specified, followed by redacted content.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-671326-177420-4.jpeg)Figure 4. BedrockAgentCoreMemory policy statement.

The policy applies actions such as GetMemory and RetrieveMemoryRecords to the wildcard memory resource arn:aws:bedrock-agentcore:*:memory/*. This effectively allows the agent whose role was assigned with this policy to read the memories of all other agents in the account.

Since the default role permits access to “*”, any AI agent can read or poison the state of any other AI agent in the account. The last piece required for exploitation is the knowledge of the target’s unique MemoryID.

### Indirect Privilege Escalation

[AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) utilizes [Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html) to execute dynamic logic. Crucially, these interpreters operate under their own distinct IAM roles, separate from Agent Runtime. This means that when an agent invokes the interpreter, the resulting actions are performed using the interpreter's permissions, not the agent's. The default policy indicates that the InvokeCodeInterpreter action is granted on all Code Interpreter resources (*), as Figure 5 shows.

![A screenshot of a code snippet showing AWS IAM policy permissions for Bedrock's agent core code interpreter. The policy includes actions like creating, starting, invoking, stopping, and deleting code interpreter sessions. Specific AWS resource ARNs are referenced.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-673352-177420-5.png)Figure 5. BedrockAgentCoreCodeInterpreter policy statement.

These permissions introduce the risk of a direct exploitation cycle. Using a compromised AI agent, an attacker could perform reconnaissance to list available interpreters, identify a high-privileged target, and attempt to pivot by executing code within that context.

### ECR Exfiltration

Perhaps the most critical finding relates to the Elastic Container Registry (ECR). As AgentCore Runtimes are distributed as Docker images, the default policy grants the AI agent unrestricted ability to pull images from any repository (arn:aws:ecr:*:repository/*) within the account. Figure 6 details this specific part of the policy.

![A screenshot of a JSON code snippet showing AWS IAM permissions. The code includes actions such as "BatchGetImage" and "GetAuthorizationToken" for Amazon Elastic Container Registry \(ECR\). Certain values, such as a repository identifier, are blurred for privacy.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-678243-177420-6.png)Figure 6. ECR policy statements.

This configuration creates a high-risk exfiltration vector. From a compromised agent, an attacker could generate an authentication token to download source code, proprietary algorithms, internal files and other sensitive data from images of other agents and unrelated workloads across the entire account.

First, the attacker retrieves a valid ECR authorization token, as Figure 7 shows.

![A screenshot of a code editor and a terminal. The code editor contains a Python script with an import statement for BedrockAgentCEP and code to connect to a service using boto3 for an agent. Below, a terminal displays a command being executed using `agentcore`, along with a network endpoint and response details.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-681411-177420-7.jpeg)Figure 7. Retrieve authorization token using agent’s role.

With these credentials, the attacker authenticates the Docker CLI and pulls the image of a target agent – or any other container in the registry – as detailed in Figure 8.

![A screenshot of a terminal displaying code and error messages related to Docker login and image pulling. It shows attempts to access a repository from Amazon's Elastic Container Registry. The error message indicates access denial. There are also multiple lines displaying "Pull complete" with corresponding hashes.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-683495-177420-8.png)Figure 8. Pulling another agent’s image using a previously retrieved token.

After downloading the image, the attacker has full read access to the target's file system, as Figure 9 shows.

![Screenshot of a server file management interface displaying directory contents. The highlighted folder is "app," sized at 0 Bytes. The interface shows activity status as "Running".](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-687656-177420-9.png)Figure 9. Exploring image content.

### Bypassing the Memory ID Barrier

As noted in the Cross-Agent Data Access section, the primary barrier to cross-agent memory poisoning is the obscurity of the target's MemoryID. The ECR exfiltration vulnerability eliminates this constraint. As Figure 10 shows, an attacker can recover configuration details that are baked into the container or environment files, by performing static analysis on the downloaded Docker image.

![A screenshot of a command line interface showing a directory with a folder named "Files" highlighted. A portion of code at the bottom shows configuration details, including paths and an identifier.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-689802-177420-10.png)Figure 10. Extracting memory ID.

The env-output.txt file that can be found within the image contains the following target identifier:

BEDROCK_AGENTCORE_MEMORY_ID=ori_agent_01_mem-AsDiQiDikR

### The Kill Chain

By abusing the default permission configurations, an attacker could:

  1. **Exfiltrate:** Leverage ECR permissions to download the image of a high-value target.
  2. **Extract:** Recover the MemoryID from the container's static configuration.
  3. **Execute:** Use the ID to dump or poison the target's conversation history.



This completes the attack vector. The AgentCore starter toolkit God Mode permissions allow an attacker who compromises an initial agent to exfiltrate the source code of a target, extract the specific resource IDs and hijack the target's memory state, without restriction.**  
**

### Invoking Other Agents

In addition, we observed that the policy scope extends to the runtime API, granting InvokeAgentRuntime permissions on the arn:aws:bedrock-agentcore:*:runtime/* resource. This effectively allows any agent in the account to trigger the execution of any other agent, as Figure 11 demonstrates.

![A screenshot of a JSON code snippet showing permissions for "BedrockAgentCoreRuntime." The "Effect" is set to "Allow," with several "Actions"" included. The "Resource" specifies an AWS ARN in a specified region.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-691803-177420-11.jpeg)Figure 11. BedrockAgentCoreRuntime policy statement.

This architecture allows an agent designed for non-sensitive data access or non-administrative tasks to invoke another agent that has higher privileges.

## Conclusion

While building and deploying AI agents on other platforms can require significant effort, AWS has effectively streamlined this process with the AgentCore starter toolkit. Following our communication with AWS, the AWS security team provided the following statement: “It is important for anyone using the toolkit to understand that the IAM roles generated by the auto-create feature provide a flat permission structure that does not align with the principle of least privilege, and should never be used in a production system.”

Our analysis of the automatically attached IAM policy revealed the presence of an overly permissive IAM role. Instead of scoping permissions to the specific AI agent resources, the policy grants the agent's role the ability to perform actions on wildcard resources (*) in Bedrock AgentCore and ECR. This exposes the environment to unauthorized cross-resource access.

The overly permissive IAM policies create the following security risks:

  * **Source code exposure:** Unrestricted ECR access allows full retrieval of container images.
  * **Data compromise:** Wildcard permissions on memory resources facilitate cross-agent data leakage.
  * **Privilege escalation:** Unchecked access to Code Interpreters enables lateral movement.



As recommended by the AWS Security team, customers should always create a custom, least-privilege IAM role for production agents. This is the most effective mitigation to limit the potential impact of a compromised agent. Following our collaboration with AWS, their Security team made updates to documentation, to enhance transparency and promote safer deployment practices for all users.

### Disclosure Timeline

  * Nov. 17, 2025 – We responsibly reported to the AWS Security team.
  * Nov. 18, 2025 – AWS Security team responded that they are investigating.
  * Dec. 14, 2025 – AWS Security team reached out for more details.
  * Jan. 28, 2026 – AWS Security team provided clarifications regarding our findings.



### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

Organizations are better equipped to[ close the AI security gap](https://www.paloaltonetworks.com/apps/pan/public/downloadResource?pagePath=/content/pan/en_US/resources/whitepapers/close-ai-security-gap) through the deployment of [Cortex AI-SPM](https://www.paloaltonetworks.com/cortex/cloud/ai-security-posture-management), which helps to provide comprehensive visibility and posture management for AI agents across AWS and Azure environments. Cortex AI-SPM is designed to mitigate critical risks including, over-privileged AI agent access, misconfigurations, and unauthorized data exposure. Cortex AI-SPM helps enable security teams to enforce compliance with NIST and OWASP standards, monitor for real-time behavioral anomalies, and secure the entire AI lifecycle within a unified cloud security context.

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

  * [Creating an AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-create.html) – AWS documentation
  * [Get started with the Amazon Bedrock AgentCore starter toolkit in Python](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-toolkit.html) – AWS documentation
  * [Using Amazon Bedrock with an AWS SDK](https://docs.aws.amazon.com/bedrock/latest/userguide/sdk-general-information-section.html) – AWS documentation
  * [Bedrock AgentCore Starter Toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit) – GitHub
  * [When an Attacker Meets a Group of Agents: Navigating Amazon Bedrock's Multi-Agent Applications](https://unit42.paloaltonetworks.com/amazon-bedrock-multiagent-applications/) – Unit 42



Back to top

### Tags

  * [Agentcore](https://unit42.paloaltonetworks.com/tag/agentcore/ "agentcore")
  * [AI agents](https://unit42.paloaltonetworks.com/tag/ai-agents/ "AI agents")
  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bedrock](https://unit42.paloaltonetworks.com/tag/bedrock/ "bedrock")
  * [DNS tunneling](https://unit42.paloaltonetworks.com/tag/dns-tunneling/ "DNS tunneling")
  * [Exfiltration](https://unit42.paloaltonetworks.com/tag/exfiltration/ "exfiltration")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [Identity](https://unit42.paloaltonetworks.com/tag/identity/ "identity")
  * [Killchain](https://unit42.paloaltonetworks.com/tag/killchain/ "killchain")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
  * [Sandbox](https://unit42.paloaltonetworks.com/tag/sandbox/ "Sandbox")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox ](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/ "Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox")

### Table of Contents

  *   * Executive Summary
  * Technical Analysis
    * The Default Deployment Architecture
    * Cross-Agent Data Access
    * Indirect Privilege Escalation
    * ECR Exfiltration
    * Bypassing the Memory ID Barrier
    * The Kill Chain
    * Invoking Other Agents
  * Conclusion
    * Disclosure Timeline
    * Palo Alto Networks Protection and Mitigation
  * Additional Resources



### Related Articles

  * [ Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "article - table of contents")
  * [ The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "article - table of contents")
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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/exploit-of-aws-agentcore-iam-god-mode/)