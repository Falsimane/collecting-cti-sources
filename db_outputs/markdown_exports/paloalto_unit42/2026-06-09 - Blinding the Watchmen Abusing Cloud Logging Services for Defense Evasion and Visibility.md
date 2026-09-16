# Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/
- **Date :** 2026-06-09

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")



[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 12 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Yahav Festinger](https://unit42.paloaltonetworks.com/author/yahav-festinger/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:June 9, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/)
    * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/)
    * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/)
    * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/)
    * [Log poisoning](https://unit42.paloaltonetworks.com/tag/log-poisoning/)
    * [Log router](https://unit42.paloaltonetworks.com/tag/log-router/)
    * [Log storage](https://unit42.paloaltonetworks.com/tag/log-storage/)
    * [S3](https://unit42.paloaltonetworks.com/tag/s3/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Blinding%20the%20Watchmen:%20Abusing%20Cloud%20Logging%20Services%20for%20Defense%20Evasion%20and%20Visibility&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-logging-defense-evasion%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-logging-defense-evasion%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-logging-defense-evasion%2F&title=Blinding%20the%20Watchmen:%20Abusing%20Cloud%20Logging%20Services%20for%20Defense%20Evasion%20and%20Visibility "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-logging-defense-evasion%2F&text=Blinding%20the%20Watchmen:%20Abusing%20Cloud%20Logging%20Services%20for%20Defense%20Evasion%20and%20Visibility "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-logging-defense-evasion%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Blinding%20the%20Watchmen:%20Abusing%20Cloud%20Logging%20Services%20for%20Defense%20Evasion%20and%20Visibility%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-logging-defense-evasion%2F "Share in Mastodon")



## Executive Summary

Cloud logging services provide comprehensive visibility into actions performed within cloud resources, making them essential for security monitoring. However, this reliance also makes logging services a high-value target for attackers. An attacker who exploits these services could create weak spots, evade detection, and in certain scenarios, establish continuous visibility within a target’s environment.

Services such as Amazon Web Services (AWS) CloudTrail and Google Cloud are powerful for defenders, and prime targets for attackers seeking to remain undetected by disrupting the flow of logs. Attack techniques against cloud logging services primarily fall into two categories:

  * **Defense Evasion:** Attackers aim to bypass detection systems, to execute attacks unnoticed. This may involve modifying resources within the cloud logging service.
  * **Continuous Visibility:** Attackers attempt to transfer logs to their own accounts, establishing continuous visibility over the victim's environment.



Understanding these attack scenarios enables organizations to implement the appropriate configurations and detect service misuse.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

  * [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud)



The [Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Cloud](https://unit42.paloaltonetworks.com/tag/cloud/), [Logging](https://unit42.paloaltonetworks.com/tag/logging/), [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/), [AWS, ](https://unit42.paloaltonetworks.com/tag/aws/)[S3 Bucket](https://unit42.paloaltonetworks.com/tag/S3/)**  
---|---  
  
## Cloud Logging Services

Serving as the authoritative system of record for every event, cloud logging services provide complete visibility into all actions within cloud environments. This comprehensive data enables analysis of past behaviors for both operational debugging and security investigations.

Each cloud provider implements logging services in a unique way. Our recent [Cloud Logging for Security](https://unit42.paloaltonetworks.com/cloud-logging-for-security/) article provides an overview of these various services across different cloud providers. In this article, we analyze and demonstrate attack techniques that target the primary logging services within each major cloud provider.

Before examining the logging capabilities offered by major cloud providers, we outline the fundamental components and mechanisms for log delivery. Our analysis focuses on AWS CloudTrail and Google Cloud Logging. Both of these widely used services are designed to provide comprehensive audit trails and operational insights. While this article focuses on specific services, the attack techniques presented may also apply to other cloud logging services.

## Background: How Cloud Service Providers Handle Logs

### AWS CloudTrail

AWS CloudTrail's primary resource for configurable log collection and delivery is known as a [trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-trails). A trail acts as a configuration that specifies how CloudTrail records AWS application programming interface (API) calls and related events in an AWS account. These events include actions taken by users, roles or AWS services.

The main function of a trail is to deliver these captured logs to an Amazon [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html). S3 is a highly scalable, durable, secure object storage service. When a trail is configured, it continuously writes log files containing event records to the designated S3 bucket.

The S3 bucket serves as a centralized, long-term repository for CloudTrail logs. This enables auditing, security analysis and compliance efforts. CloudTrail supports sending native event trails to either the CloudTrail Lake feature, EventBridge or CloudWatch Logs. However, for enterprises with integrations to third-party products, these features might not be relevant or usable.

### Google Cloud Logging

Cloud Logging is a fully managed service that collects logs from all of an organization’s Google Cloud resources. Cloud Logging leverages a resource called a [sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) as the primary mechanism for log delivery. A sink functions as a router that sends log entries to a specific destination. While a sink primarily routes and stores logs in centralized [log buckets](https://docs.cloud.google.com/logging/docs/buckets) for analysis and retention, it also offers the flexibility to export logs to other powerful Google Cloud services. For example, logs can be routed to a cloud storage bucket for cost-effective long-term archival. When a sink is configured, it exports log entries that match specific criteria defined by a filter to a designated log bucket.

## Defense Evasion

Sophisticated techniques enable attackers to remain undetected within a compromised cloud environment. These methods could involve manipulating or evading logging mechanisms, which are crucial for security monitoring and incident response. Obscured activities can extend an attacker's presence, facilitate data exfiltration or inflict more harm before being discovered.

A wide array of security products including the following are fundamentally dependent on this log data to function:

  * Security information and event management (SIEM)
  * Security orchestration, automation and response (SOAR) platforms
  * Specialized cloud security posture management (CSPM) tools



By disabling, altering or deleting these logs, an attacker can effectively hide themselves from these defensive systems, compromising the security integrity of the entire cloud environment. Attackers often use the following five techniques to accomplish this:

  1. Stop logging
  2. Delete the log storage destination
  3. Delete the log router
  4. Impair logging via attacker-controlled encryption key
  5. Log poisoning



### Technique 1: Stop Logging

The most direct method to suspend log flows is to disable the logging mechanism itself. A wide array of security products is fundamentally dependent on this log data to function. By disabling these logs, an attacker can effectively blind defensive systems, compromising the security integrity of the entire cloud environment.

  * In AWS, an attacker with cloudtrail:StopLogging permissions can invoke the stop-logging API call for a specific trail. Once this API is executed, no further logs for that trail are written to the S3 bucket, creating an immediate visibility gap for organizations that created their own trails.
  * In Google Cloud, the equivalent action is disabling the sink. An attacker with logging.sinks.update permissions can set the sink’s disabled field to true to stop logs from being written. The Google Cloud console message shown in Figure 1 reflects this change.

![A screenshot of a dialog box titled "Confirm disable sink." It states the sink to be disabled is "sink-blog-simulation." The message explains that disabling it will stop log export to this sink, and new logs will be lost unless captured by another sink. There are two buttons at the bottom: "Cancel" and "Disable," with a link for more options on log sinks.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-341857-182090-1.png)Figure 1. Message confirming suspension of logs.

### Technique 2: Delete Log Storage Destination

Typically, logs are stored in a cloud storage resource. An attacker who obtains permission to this resource could delete the cloud storage, preventing logs from being written. The following scenarios demonstrate this ability.

  * In AWS, an attacker with s3:DeleteBucket permissions can use the delete-bucket API to delete the S3 bucket; this action also requires the s3:DeleteObject permission to empty the bucket. A few minutes after the action, the associated CloudTrail trail's configuration will indicate this deletion, as the notification in Figure 2 shows.

![A screenshot of a AWS CloudTrail displaying general details for a trail logging configuration. A red error message states "Bucket doesn't exist" with a "Fix policy" link. "Multi-region trail" is set to Yes, while "Apply trail to my organization" is Not Enabled.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-343694-182090-2.png)Figure 2. An indication for the bucket deletion in AWS CloudTrail.

  * In Google Cloud, an attacker with logging.buckets.delete permissions can delete the log bucket. In the case of a log bucket, the deletion is not immediate. Once the delete command is issued, the log bucket enters a DELETE_REQUESTED state, remaining in that state for seven days. After this period, the bucket is deleted.  
Google Cloud offers a [mechanism](https://docs.cloud.google.com/logging/docs/buckets#locking-logs-buckets) to protect against this deletion by providing the ability to lock the logging bucket. Once a bucket is locked, its retention policy becomes permanent and irreversible, meaning the bucket cannot be deleted by any user until every log entry within it has fulfilled the specified retention period.



### Technique 3: Delete Log Router

Another defense evasion tactic involves deleting the log routing resource – for example, an AWS trail or a Google Cloud sink. Once deleted, new logs will cease to be written to the designated destination. An attacker can delete a log router by using the delete-trail AWS API or the google.logging.v2.ConfigServiceV2.DeleteSink Google Cloud method.

### Technique 4: Impair Logging via Attacker-Controlled Encryption Key

​​An attacker could potentially render cloud logs unreadable by modifying their encryption key. An attack flow using AWS could unfold as follows:

  * When a trail is created in AWS, one of the configuration parameters is the key management service (KMS) key, which is used to encrypt the logs delivered by CloudTrail.
  * An attacker could prevent legitimate access to this key by updating the trail to use an attacker-controlled KMS key and then removing access to the key.
  * Consequently, logs will not be written to the bucket due to the inability to encrypt them with the unusable key.
  * To perform this attack, an attacker first creates an external KMS key with the policy shown in Figure 3 to ensure that the key is accessible to CloudTrail.

![A code snippet showing a JSON policy configuration for AWS. The configuration permits CloudTrail access to a key.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-345545-182090-3.png)Figure 3. Policy to create a KMS key with external access.

  * The attacker uses the update-trail API to modify the KMS key used to encrypt the logs in the S3 bucket.
  * Next, the attacker removes CloudTrail's access to the key by either deleting the key or removing the Allow CloudTrail to access the key statement from the policy. Subsequently, CloudTrail will indicate that there is a configuration issue due to denied bucket access, even though the bucket is correctly configured.
  * From this point on, logs will not be written to the bucket because the KMS key will be inaccessible. Figure 4 shows the message that is displayed after access is disabled.

![A screenshot of AWS settings page displaying "General details." It shows "Trail logging" with a red icon and the message "Bucket access denied" with a link to "Fix policy." "Multi-region trail" is set to Yes, while "Apply trail to my organization" is Not Enabled.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-347506-182090-4.png)Figure 4. Disabling access to the KMS key results in a Bucket access denied error.

Figure 5 shows the attack flow using AWS.

!["A diagram illustrating a three-step attack process on AWS CloudTrail. Step 1: Victim account stores logs in an S3 bucket, encrypted with its own KMS key. Step 2: Attacker uses 'update-trail' API to change the KMS key to one they control. Step 3: Attacker removes CloudTrail access to the original key, preventing victim access to logs.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-349280-182090-5.png)Figure 5. Impair logging via attacker-controlled encryption key attack flow in AWS.

An attack flow using this technique in Google Cloud is as follows:

  * In Google Cloud, a similar attack scenario can be simulated where a log bucket is already pre-configured with customer-managed encryption keys (CMEK). An attacker can then exploit this existing configuration by modifying the CMEK to reference an external key using the following command (the external [CMEK must have encrypt/decrypt access](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#assign-role) granted to the KMS service account): gcloud logging buckets update BUCKET_NAME --location=LOCATION --cmek-kms-key-name FULL_KMS_KEY_NAME



Subsequently, the attacker can remove the permissions granted to the external key. At this point, the victim will be unable to read the logs, as the Google Cloud panel in Figure 6 shows.

![A screenshot of a Google Cloud log analysis interface showing an error message. The left panel displays "Log fields data is unavailable because query is invalid." The main section shows a timeline graph with another message stating, "Log histogram is unavailable because query is invalid." Below the graph, a section reads, "Your input is invalid" with zero results listed.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-351279-182090-6.png)Figure 6. The outcome of an inaccessible encrypted key.

Any attempts to revert the key will result in the error message “rekeying requires that the CMEK service account has decrypt access to the current CMEK key,” as Figure 7 shows.

![A screenshot of a terminal displaying an error message related to Google Cloud. The error indicates a failed precondition due to credentials issues with a Google service account regarding GKE keys.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-353226-182090-7.png)Figure 7. The outcome of an attempt to revert the key.

### Technique 5: Log Poisoning

Another defense evasion technique is the direct modification of logs – known as log poisoning. This is an effective technique when logs are pre-configured to be written to a cloud storage resource. In this case, the logs are stored in JavaScript Object Notation (JSON) format and can be modified by an attacker. If stored logs are deleted, added or modified, there is a high likelihood that Security Operations Center (SOC) personnel or analysts would inadvertently use these poisoned logs to conduct log analysis.

  * In AWS, CloudTrail logs are delivered as objects to an S3 bucket. An attacker with s3:GetObject and s3:PutObject permissions on the bucket could download a log file, remove or alter specific events and then re-upload it, overwriting the original file. This breaks the chain of custody and invalidates the audit trail.
  * Figure 8 shows the response to a query from a scenario where an attacker alters a log to avoid detection, and then the victim inspects the log using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

![A screenshot of response to a query from an attack scenario.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-355229-182090-8.png)Figure 8. Athena query analysis shows the modified log.

  * In Google Cloud, sinks route the logs to cloud storage. An attacker with storage.objects.get and storage.objects.create permissions can perform the same download and overwrite technique.



To mitigate the risk of log poisoning, AWS provides [CloudTrail log file integrity validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html). This feature provides the ability to cryptographically verify whether log files were modified after they were delivered by CloudTrail. This ability is enabled by default when using the AWS Console to create Trails, but not when using the API or command line interface (CLI).

## Continuous Visibility

Upon gaining an initial foothold in a victim environment, an attacker with advanced capabilities would aim to establish long-term, passive visibility into the victim's cloud infrastructure. Instead of running noisy discovery commands that might trigger alerts – or if they lack proper permissions – an attacker can target the log routing mechanism to route logs to their own environment, resulting in real-time visibility. This enables attackers to perform continuous discovery and passively monitor all activity, from new VM deployments and IAM policy changes to sensitive data access. In this way, attackers can map the environment, identify high-value targets, and escalate privileges while potentially remaining invisible to the victim's security monitoring. The following techniques achieve continuous visibility:

  1. Configure new log routing resource
  2. Log redirection



### Technique 1: Configure New Log Routing Resource

A direct method for achieving continuous visibility involves creating a new log routing resource – for example, an AWS trail or a Google Cloud sink. The attacker configures the newly created resource to direct logs to an external, attacker-controlled destination.

  * In AWS, the attacker configures CloudTrail logging to their own S3 bucket by using the create-trail API and specifying their bucket in the \--s3-bucket-name parameter.
  * In Google Cloud, the attacker utilizes the logging.sinks.create API to set the DESTINATION parameter to the attacker’s intended resource.



Both of the above steps result in all logs being directed to the attacker's chosen destination.

For certain AWS accounts, the CreateTrail operation shows up in CloudTrail. If EventBridge is configured upon AWS account set-up, defenders can use EventBridge to alert on creation events. In this setup, subsequent describe calls of CloudTrail configuration will show the attacker's destination bucket. However, for organizations that use third parties or have not applied these configurations, attackers can carry out adversarial activities without being detected.

### Technique 2: Log Redirection

Using this technique, the attacker alters the log routing destination to one within their own environment. This redirects logs to an attacker-controlled resource, enabling the attacker to obtain continuous discovery.

  * In AWS, the attacker updates the \--s3-bucket-name parameter when invoking the update-trail API. After modifying the destination bucket, all logs are directed to the attacker’s bucket, providing continuous discovery capabilities on the victim’s account.
  * In Google Cloud, the attacker uses logging.sinks.update permissions to update the destination parameter, achieving the same ability to redirect logs.



Small enterprises that manage their own alert telemetry may notice that Trails have stopped working in this situation, but larger organizations may not be using AWS-native services that would allow them to detect this behavior.

## Risk and Impact Assessment

Table 1 summarizes the evasion and visibility techniques, the likelihood that the activity is malicious, and the impact on logging services.

**Technique Name** | **Likeliness of Malicious Activity** | **Primary Impact**  
---|---|---  
Stop Logging | High | Total inability to view logs; usually precedes a larger attack.  
Delete Log Storage Destination | Medium | Destruction of forensic evidence and archived log data.  
Delete Log Router | Low | Disruption of the security pipeline.  
Impair Logging via Attacker-Controlled Encryption Key | Medium | Logs exist but are rendered unreadable.  
Log Poisoning | Medium | Degradation of data integrity.  
Configure New Log Routing Resource | Low | Log exfiltration and potential covert persistence.  
Log Redirection | High | Log exfiltration and potential covert persistence.  
  
Table 1. Risk and impact assessment of evasion and visibility techniques.

## Prevention and Awareness

The attack scenarios discussed all stem from modifications to logging service resources. Given the high value of cloud logging service resources, access should be restricted to highly privileged users to help prevent these scenarios. This measure reduces the likelihood of an attacker altering the configuration of such resources.

### Amazon Web Services

For every AWS account there is an immutable 90 day CloudTrail [Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) of all management events. This fallback ensures that these records cannot be deleted or circumvented. However, data and network events do not appear in this history.

In AWS, limit the update-trail API invocation to highly privileged users. Configure the bucket policy of the associated S3 bucket to prevent non-admin users from making configuration modifications. It's also crucial to ensure that only the CloudTrail service can write objects to these buckets.

### Google Cloud

Google Cloud provides a similar safety mechanism to AWS, through its [built-in log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries#system-created). The _Required log bucket serves as an immutable repository for essential logs – such as Admin Activity and System Event audit logs – that cannot be disabled, modified or deleted. Alongside this, the _Default log bucket automatically captures a broader range of log entries for a shorter period of time. When creating logging storage for external integration purposes, these built-in buckets will not be relevant. As a result, those manually configured buckets may remain exposed to the specific attack techniques described in this article.

In Google Cloud, restrict the permissions for logging.sinks.update, and protect the destination resource.

## Conclusion

Cloud logging services are fundamental for maintaining security posture and operational awareness, providing the definitive record of all activities within a cloud environment. The integrity of the logging infrastructure itself is a critical control, and for this reason has become a primary target for threat actors aiming to operate undetected.

The misuse of cloud logging services can have serious negative outcomes, enabling adversaries to cause blind spots for security teams, exfiltrate sensitive data in real-time, or methodically cover their tracks to evade forensics. By understanding the specific TTPs that threat actors use against these services, defenders can build more resilient detection and prevention strategies.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

[Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud) customers are better protected from the topics discussed within this article with cloud [runtime security](https://www.paloaltonetworks.com/cortex/cloud/runtime-security) operations, through the collection, analysis, detection, alerting and prevention of malicious operations on cloud platform and SaaS application audit logs. Using behavioral and static alerting techniques on cloud logs during cloud operations runtime, the techniques discussed within the article can be identified and trigger alerts which provide early warning – and in some cases, prevention operations to prevent further compromise from these attacks.

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

## Additional Resources

  * [CloudTrail concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-trails) – AWS
  * [CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) – AWS
  * [General purpose buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) – AWS
  * [What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) – AWS
  * [Validating CloudTrail log file integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html) – AWS
  * [Aggregated sinks overview](https://cloud.google.com/logging/docs/export/aggregated_sinks_overview) – Google Cloud
  * [Configure CMEK for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#assign-role) – Google Cloud
  * [Log buckets](https://docs.cloud.google.com/logging/docs/buckets) – Google Cloud
  * [Logging Bucket Locking](https://docs.cloud.google.com/logging/docs/buckets#locking-logs-buckets) – Google Cloud
  * [System-created Log Buckets](https://docs.cloud.google.com/logging/docs/store-log-entries#system-created) – Google Cloud
  * [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview) – Google Cloud
  * [Cloud Logging for Security and Beyond](https://unit42.paloaltonetworks.com/cloud-logging-for-security/) – Unit 42



## Cortex XDR Alerts on Cloud Logging Services Misuse

Table 2 shows the Cortex alerts that are triggered by this activity in cloud logging services.

**Alert Name** | **MITRE ATT &CK® Tactic**  
---|---  
[AWS CloudTrail has been stopped](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/AWS-CloudTrail-has-been-stopped) | Defense Evasion (TA0005)  
[AWS CloudTrail modification](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/AWS-CloudTrail-modification) | Defense Evasion (TA0005), Discovery (TA0007)  
[Google Cloud logging sink modification](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/GCP-logging-sink-modification) | Defense Evasion (TA0005), Discovery (TA0007)  
[Google Cloud Logging Bucket Deletion](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/GCP-Logging-Bucket-Deletion) | Defense Evasion (TA0005)  
[CloudTrail logging deletion](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/CloudTrail-logging-deletion) | Defense Evasion (TA0005)  
[Google Cloud logging sink deletion](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/GCP-logging-sink-deletion) | Defense Evasion (TA0005)  
[Logging was impaired via external encryption key](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/Logging-was-impaired-via-external-encryption-key) | Defense Evasion (TA0005), Impact (TA0040)  
[Suspicious activity on logging bucket](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-Analytics-Alert-Reference-by-Alert-name/Suspicious-activity-on-logging-bucket) | Defense Evasion (TA0005)  
  
Table 2. Cortex alerts that indicate malicious activity in cloud logging services.

Back to top

### Tags

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Log poisoning](https://unit42.paloaltonetworks.com/tag/log-poisoning/ "log poisoning")
  * [Log router](https://unit42.paloaltonetworks.com/tag/log-router/ "log router")
  * [Log storage](https://unit42.paloaltonetworks.com/tag/log-storage/ "log storage")
  * [S3](https://unit42.paloaltonetworks.com/tag/s3/ "S3")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/ "Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257")

### Table of Contents

  *   * Executive Summary
  * Cloud Logging Services
  * Background: How Cloud Service Providers Handle Logs
    * AWS CloudTrail
    * Google Cloud Logging
  * Defense Evasion
    * Technique 1: Stop Logging
    * Technique 2: Delete Log Storage Destination
    * Technique 3: Delete Log Router
    * Technique 4: Impair Logging via Attacker-Controlled Encryption Key
    * Technique 5: Log Poisoning
  * Continuous Visibility
    * Technique 1: Configure New Log Routing Resource
    * Technique 2: Log Redirection
  * Risk and Impact Assessment
  * Prevention and Awareness
    * Amazon Web Services
    * Google Cloud
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Additional Resources
  * Cortex XDR Alerts on Cloud Logging Services Misuse



### Related Articles

  * [ Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "article - table of contents")
  * [ Pass the Passkey: A Novel Attack Surface in Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/ "article - table of contents")
  * [ OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat ](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/ "article - table of contents")



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

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

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

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)