# The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/
- **Date :** 2026-06-22

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")



[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 13 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Yahav Festinger](https://unit42.paloaltonetworks.com/author/yahav-festinger/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:June 22, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [AWS](https://unit42.paloaltonetworks.com/tag/aws/)
    * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/)
    * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/)
    * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/)
    * [CSPs](https://unit42.paloaltonetworks.com/tag/csps/)
    * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/)
    * [IAM](https://unit42.paloaltonetworks.com/tag/iam/)
    * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/)
    * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=The%20Global%20Namespace%20Risk:%20Universal%20Bucket%20Hijacking%20Technique%20for%20Cloud%20Data%20Exfiltration&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-bucket-hijacking-risks%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-bucket-hijacking-risks%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-bucket-hijacking-risks%2F&title=The%20Global%20Namespace%20Risk:%20Universal%20Bucket%20Hijacking%20Technique%20for%20Cloud%20Data%20Exfiltration "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-bucket-hijacking-risks%2F&text=The%20Global%20Namespace%20Risk:%20Universal%20Bucket%20Hijacking%20Technique%20for%20Cloud%20Data%20Exfiltration "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-bucket-hijacking-risks%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=The%20Global%20Namespace%20Risk:%20Universal%20Bucket%20Hijacking%20Technique%20for%20Cloud%20Data%20Exfiltration%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fcloud-bucket-hijacking-risks%2F "Share in Mastodon")



## Executive Summary

We recently identified a bucket hijacking technique impacting multiple services across major cloud service providers (CSPs). The attack technique exploits a fundamental architectural flaw that is common across cloud providers and could potentially affect other cloud providers as well.

Our research reveals that an attacker can silently compromise an organization's active data streams by rerouting data into an external storage bucket. Because a storage bucket name is globally unique, an attacker can simply delete the bucket and then recreate it under the attacker's own account using the same name. This therefore creates a global namespace risk. This bucket hijacking reroutes critical logs and sensitive data directly to the attacker’s environment.

We have shared these findings with Google Cloud, Amazon Web Services (AWS), and Microsoft Azure.

We have not yet identified a real-world threat actor using this attack technique. However, we recommend organizations take steps now to head off the potential impact, particularly since we anticipate that real-world attempts to use this attack technique would be difficult to detect.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

  * [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud)



[Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) can help turn cloud complexity into actionable security insights.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Cloud Logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/), [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/), [AWS](https://unit42.paloaltonetworks.com/tag/aws/), [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/)**  
---|---  
  
## Key Architectural Elements Enabling the Attack

Before detailing the attack methodology, it’s important to understand several architectural elements that, when combined, make bucket hijacking possible.

### Data Stream Overview

A data stream is an automated, continuous pipeline designed for high-volume data movement between services. Once configured, these streams operate autonomously in the background to push telemetry, audit logs or objects from a source environment to a designated storage destination for processing and long-term retention.

Major CSPs facilitate automated data streams. These streams serve as critical nodes for routing, processing and backing up data within an organization's infrastructure, such as:

  * A [cloud logging sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview) in Google Cloud acts as a router for log entries, directing them to a chosen destination. While primarily used to route and store logs in centralized log buckets for purposes like analysis and retention, a sink can also export logs to a Google Cloud Storage (GCS) bucket.
  * [Bucket replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) in AWS is a feature that automatically duplicates data from a source S3 bucket to a designated destination S3 bucket.



### Global Uniqueness of Bucket Names

Cloud environments often stream data into buckets such as an S3 bucket in AWS or a GCS bucket in Google Cloud. Because bucket names are typically unique across the entire cloud provider, no two users can have the same bucket name. This design simplifies data stream establishment by providing a single, predictable target. However, it also creates a shared namespace where a destination's identity is tied solely to its name, rather than to a specific, immutable account owner. This characteristic is the foundational logic behind our discovery.

### Permissions to Modify Data Stream Destinations

The data stream is frequently defined by a routing resource that is configured with a specific destination. To legitimately modify this destination, the user must possess specific, granular identity and access management (IAM) update permissions for that resource.

For example, modifying the destination for a cloud logging sink requires the logging.sinks.update permission. This routes logs to a bucket. Our research found that certain permissions outside of this traditional update purview could be leveraged to reroute data streams.

## The Bucket Hijacking Attack

We now turn to discussing the attack flow before any mitigations were provided by the affected CSPs. After compromising a cloud environment and securing the permissions required to delete a target bucket, an attacker was effectively positioned to intercept and redirect a cloud data stream. By deleting the original bucket and immediately recreating a new bucket with the same name within their own account, the attacker could have redirected the data stream. This could have led to the exfiltration of the target's data to the attacker's account.

Figure 1 shows the attack flow diagram.

![A three-part digram showing the bucket hijacking attack flow. The first step shows a cloud platform with a target project. It includes a resource labeled "Router" and a bucket labeled "target-storage." The middle step illustrates a cloud platform with the "target-storage" bucket removed. In the final step, the diagram shows two projects: a target project with the "Router" resource and an attacker project with a new "target-storage" bucket.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-569293-182610-1.png)Figure 1. The bucket hijacking attack flow.

### Simulating Bucket Hijacking in Google Cloud Logging

We simulated the bucket hijacking technique in Google Cloud Logging. In the simulation, we used a sink that routes logs to a cloud storage resource, as shown in Figure 2.

![A screenshot of Google Cloud's "Sink details" page showing configurations for a Cloud Storage bucket. The screen includes fields like Name, Resource name, Description, Service, Destination, and Writer identity, with some text redacted. There are also options for "Inclusion filter" and "Exclusion filter\(s\)." Buttons labeled "Cancel" and "Edit sink" are at the bottom.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-571277-182610-2.png)Figure 2. An existing sink referencing a GCS bucket.

After routing the logs, the original cloud storage bucket was deleted, as Figure 3 shows.

![A screenshot of a confirmation dialog for deleting a Google Cloud storage bucket/ A warning indicates that this action will permanently delete the bucket and its contents. There is a text box for typing "DELETE" to confirm the action, with "DELETE" already entered. Options for "Cancel" and "Delete" are at the bottom.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-573103-182610-3.png)Figure 3. Deleting the targeted bucket used by the sink.

We then created a new bucket with the same name in an attacker-controlled environment, as shown in Figure 4.

![A screenshot of creating a storage bucket in Google Cloud Platform. The interface shows options for naming the bucket, selecting a data region, and configuring access and protection settings. On the right, pricing information and configuration tips are displayed.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-575125-182610-4.png)Figure 4. Recreating the bucket in an external project.

Subsequently, logs were routed to this external cloud storage bucket, allowing the attacker to obtain extensive information about the compromised environment, as shown in Figure 5. The required permissions the attacker needed to have are storage.objects.delete (to empty the bucket) and storage.bucket.delete (to delete the bucket).

![A screenshot of a Google Cloud Storage browser interface displaying a bucket. The list view includes multiple folders named after popular websites and companies, such as "en.wikipedia.org" and "linkedin.com." The interface shows columns for "Type," "Created," "Storage class," "Last modified," and more. Some folders have public access settings.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-577281-182610-5.png)Figure 5. Logs written into the attacker’s controller bucket.

## The Expansion to Multiple Services Within Google Cloud

Data streaming into a GCS bucket is not unique to cloud logging. There are many other Google Cloud services in which data can be streamed into cloud storage. We identified and tested a representative subset of potentially vulnerable services, specifically [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) and [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview), to confirm the systemic prevalence of this security risk.

### Pub/Sub

Pub/Sub is an asynchronous messaging service that decouples upstream event producers from downstream processing services. It allows applications to broadcast messages to a [topic](https://docs.cloud.google.com/pubsub/docs/create-topic), which are then distributed to one or more [subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview) for consumption by downstream systems.

This architecture enables scalable, event-driven communication. This allows disparate components such as log aggregators, data pipelines and real-time analytics engines to exchange information reliably without needing direct, synchronous connections.

The Pub/Sub architecture has three core components:

  1. **Publishers** (producers) send messages to a named logical channel called a topic, without needing to know who or what will receive them.
  2. **Topics** act as a buffer or distribution hub, holding the messages until they can be delivered.
  3. **Subscribers** (consumers) listen to specific topics via a subscription. When a message arrives in the topic, the Pub/Sub service pushes it to the subscribers (push model) or the subscribers actively request it (pull model).



To simulate a bucket hijacking attack on Pub/Sub, we took the following steps:

  1. We created a new Pub/Sub topic and a subscription linked to a GCS bucket
  2. We configured the GCS bucket with the [necessary permissions](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription) to grant access to the service agent: 
     1. Storage object creator (roles/storage.objectCreator)
     2. Storage legacy bucket reader (roles/storage.legacyBucketReader)
  3. We published a message to the topic, which was successfully delivered to the initial bucket
  4. We deleted the original bucket and created a new bucket with the same name in a different project (the attacker's project)
  5. When a message was published manually again, we found that the service exfiltrated the message to the attacker's environment



The successful redirection of the message stream proved that the bucket hijacking attack technique was directly applicable to the Pub/Sub service, allowing an attacker to exfiltrate data by deleting and recreating the destination bucket.

### Storage Transfer Service

Storage Transfer Service is a managed data migration tool designed to automate the movement of large volumes of data into, out of or between cloud storage environments. It allows organizations to schedule and manage massive data transfers from external sources (like AWS S3 or on-premises systems) to GCS buckets, or to synchronize data between different cloud storage projects.

The service handles the underlying infrastructure, retries and checksum validation. It provides a way to populate data lakes or perform large-scale disaster recovery backups.

The Storage Transfer Service architecture operates as a centralized orchestration engine that manages the movement of data between a designated source and sink. When a user defines a transfer job, they specify the source, the destination and the scheduling parameters. The source can be an S3 bucket, a URL list or another GCS bucket.

To simulate a bucket hijacking attack on Storage Transfer Service, we took the following steps:

  1. We configured a new transfer job with a GCS bucket as the source and another GCS bucket as the destination
  2. We assigned the [necessary permissions](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#grant_the_required_permissions) to the buckets to grant access to the service agent: 
     1. Source bucket: Storage Object Viewer (roles/storage.objectViewer) and Storage Legacy Bucket Reader (roles/storage.legacyBucketReader)
     2. Destination bucket: Storage Object Admin (roles/storage.objectAdmin)
  3. The user then initiated the transfer job
  4. We deleted the destination bucket and then immediately re-created it in a different project (the attacker's environment)
  5. We wrote a new object into the source bucket
  6. After a period determined by the job's scheduling parameter, the object appeared in the newly hijacked destination bucket, which was under the attacker's control



The impact of this risk was significantly magnified by its broad applicability across numerous services. The permissions storage.buckets.delete and storage.objects.delete could be used to bypass the granular update permissions required for specific resources to redirect sensitive data streams such as logging.sinks.update, pubsub.subscriptions.update and storagetransfer.jobs.update.

## The Expansion to Another Cloud Provider: AWS

The architectural flaw of global bucket name uniqueness is not exclusive to Google Cloud. AWS S3 buckets operate under the same design logic. Given this commonality, we investigated whether we could apply the same hijacking technique within the AWS ecosystem.

We successfully simulated the bucket hijacking attack using the S3 bucket replication feature. This feature enables the configuration of a source and destination bucket, where all objects written to the source bucket are automatically replicated to the destination bucket. The simulation followed these steps:

  1. We created a bucket in our environment with a replication rule targeting a second bucket within the same account
  2. We deleted the bucket and immediately recreated a new one using the same name within an external account
  3. We uploaded a file to the source bucket
  4. We observed the file appearing in the destination bucket located in the external account



Like in Google Cloud, we identified that this was not a localized issue, but applied to a number of AWS data stream services. We simulated the same technique using [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) (where the destination is an S3 bucket) and observed the same behavior.

## Cross-Subscription Data Exfiltration in Azure

Finally, we tested Azure’s environment for the same attack technique. Azure platform limitations prevent the immediate reuse of storage account names across different tenants for several days after deletion. However, we were able to simulate a cross-subscription attack technique.

This scenario was particularly relevant if an attacker gained permission to delete a storage account in one subscription and intended to reroute data to another. This allowed them to move data to a subscription where they maintained higher privileges and persistence, or perhaps where they previously lacked data access permissions. Ultimately, this technique relied on the fact that a storage account must be created with soft-delete disabled to ensure the name was released and could be promptly reclaimed.

We used [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview) to demonstrate this attack. Diagnostic settings in Azure Monitor can be configured to export resource logs (e.g., metrics and audit events) to an Azure storage account. While the configuration stores the destination via its Azure Resource Manager (ARM) Resource ID, the internal pipeline resolves the storage account at runtime using its DNS name ({accountname}.blob.core.windows.net).

This architectural behavior facilitated the execution of the attack. If an attacker deleted a destination storage account and recreated it with an identical globally unique name in a different subscription within the same tenant, the diagnostic pipeline would continue to write logs to the attacker-controlled storage account.

The attack was less severe in Azure than in AWS or Google Cloud because it was limited to a cross-subscription scope rather than a cross-tenant one.

## Exploitation Scenarios and Excessive Permissions Risks

The practical execution of bucket hijacking relies on specific exploitation vectors that are often facilitated by the widespread use of over-privileged administrative roles.

### Exploitation Scenarios and Detection Challenges

We identified two distinct scenarios that could enable an attacker to execute a bucket hijacking operation:

  1. **Privilege escalation** : As demonstrated in our simulations, a compromised identity with the permission to delete a bucket could misuse this access to redirect data streams to the attacker's own bucket. The widespread application of storage administrator roles significantly increased the risk of this attack technique and overcame the need for the more granular logging.sinks.update permission (as shown later).
  2. **Dangling router resources** : In a similar exploit not demonstrated in this article, if someone deleted a bucket and failed to remove the associated router resource, an attacker could create a new bucket using the same name in their own environment. This action effectively redirects the data to the attacker's bucket, granting the attacker access to the victim's ongoing data.



Detecting these attack scenarios is particularly challenging. In scenarios where destination resources are used primarily for long-term retention or backup, the target may not detect the initial deletion of the original storage bucket. Because the data stream continues to operate autonomously, the sink configuration in Google Cloud appears valid upon inspection as shown in Figure 6. This allows the hijacking and subsequent data exfiltration to remain largely undetected.

![A screenshot showing Google Cloud Storage with a checkbox selected for a bucket, with a URL. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-579835-182610-6.png)Figure 6. The sink configuration remains intact and operational after recreating the bucket.

### How Over-Privileged Roles Increase the Risk

Cloud providers frequently offer broad storage administration roles that grant wide-reaching deletion privileges by default, which significantly increases the practical risk of this attack technique.

For example, in Google Cloud the common storage admin role provides the storage.buckets.delete permission. However, as Figure 7 shows, it does not include granular permissions to modify data stream configurations like:

  * logging.sinks.update
  * pubsub.subscriptions.update
  * storagetransfer.jobs.update

![A screenshot of a Google Cloud documentation page describing the "Storage Admin" role. Includes details about granted permissions, emphasizing full control over objects and buckets, with items like "storage.buckets.*" highlighted. The list contains various operations related to storage and administrative actions.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-581683-182610-7.png)Figure 7. The predefined Google Cloud storage admin role includes bucket deletion permission (highlighted in red) but lacks granular update permissions for data stream resources.

## Mitigation Strategies

Google has adjusted how router resources interact with target storage resources since the time of our initial research.

Microsoft recommended that Azure users review documentation and tooling on addressing dangling DNS for subdomain takeovers (see Additional Resources).

Users can also employ additional defense strategies.

Mitigating the bucket hijacking technique requires a two-pronged approach focusing on preventative guardrails and proactive monitoring. Prevention starts with the principle of least privilege. Organizations must strictly limit the IAM permissions for deletion actions, specifically:

  * Storage.buckets.delete in Google Cloud
  * DeleteBucket in AWS
  * Microsoft.Storage/storageAccounts/delete in Azure



These permissions should be restricted to a minimal set of administrative roles and should never be assigned to service accounts or applications without rigorous justification.

In addition, the following mechanisms help to prevent the bucket hijacking technique:

  * Organizations can prevent bucket hijacking for data exfiltration by enforcing data perimeter controls that restrict resource access to stay within a trusted organizational boundary. 
    * In AWS, [data perimeter policies](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) — implemented through service control policies (SCPs) and virtual private cloud (VPC) endpoint policies — can ensure that workloads within the organization are unable to write data to S3 buckets that belong to external accounts. This can effectively block the exfiltration path even if an attacker substitutes a malicious bucket, though the approach has some limitations.
    * Similarly, in Google Cloud, [VPC Service Controls](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) define a security perimeter around projects and services, to block any API call attempting to access Cloud Storage buckets outside the perimeter.



Deploying these controls as a baseline ensures that data cannot leave the trusted environment boundary, neutralizing the core mechanism of this attack technique.

  * AWS offers [account regional namespaces for S3 buckets](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html), which scope bucket names to the owning account and region rather than to a single global namespace. This directly eliminates the bucket hijacking vector. If a bucket is deleted, no other account can reclaim its name. This prevents attackers from intercepting traffic by re-registering abandoned bucket names.



For detection, organizations must implement robust monitoring solutions that specifically alert on the attempted deletion of a storage bucket. Security teams should prioritize high-severity alerts for storage deletion API calls, focusing specifically on resources that house sensitive information.

Given the high frequency of storage deletion events in large-scale environments, leveraging data security posture management (DSPM) capabilities is essential. It is particularly important to prioritize monitoring and to focus specifically on high-value, sensitive assets, as shown in a Cortex XSIAM alert in Figure 8.

![A screenshot of a dashboard showing a notification about the deletion of a GCP storage bucket containing sensitive data. It includes a security domain case with an alert icon linked to "GCP Storage Bucket.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/word-image-583763-182610-8.png)Figure 8. Cortex XSIAM alert: Deletion of a high-sensitivity bucket detected.

## Conclusion

The bucket hijacking technique detailed in this research exploits the global uniqueness of storage resource names in the major cloud providers. We have demonstrated how a configure-and-forget approach to data streams can lead to silent, long-term data exfiltration.

Reliance on a globally unique, static resource name for buckets is an architectural design common across cloud providers. As such, this technique could be portable to other cloud services and providers not covered in this research.

Our findings underscore two primary lessons for the security community:

  * **Architecture defines the security boundary:** Fundamental design choices made by cloud providers directly influence the security boundaries of our environments. A robust mitigation strategy must include awareness of these architectural nuances and the implementation of guardrails.
  * **A cross-cloud exploitation methodology:** While cloud providers are often managed as distinct ecosystems, their shared design philosophies allow identical attack techniques to be applied across providers. Our simulations prove that a specific architectural observation can evolve into a universal methodology for hijacking sensitive data streams. We encourage the security industry to adopt a cloud-agnostic mindset. A design flaw discovered in one provider could be a blueprint for exploiting another.



## Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

  * [Cortex Cloud](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) customers are better protected from the techniques discussed in this article with cloud [runtime security](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) operations through the collection, analysis, detection, alerting and prevention of malicious operations on cloud platform and SaaS application audit logs. Cortex has several out-of-the-box rules built into the Analytics module that detect data movement to external buckets. Using behavioral and static alerting techniques on cloud logs during cloud operations runtime, the techniques discussed within the article can be identified. When this occurs, they trigger alerts, which provide early warning and, in some cases, prevention operations to prevent further compromise from these attacks.
  * Cortex Cloud [Identity Security](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) can also protect organizations from the techniques discussed in the article. Identity Security encompasses: 
    * Cloud Infrastructure Entitlement Management (CIEM)
    * Identity Security Posture Management (ISPM)
    * Data Access Governance (DAG)
    * Identity Threat Detection and Response (ITDR)
  * These tools provide the necessary capabilities to improve identity-related security requirements within cloud environments. This includes: 
    * Accurately detecting misconfigurations
    * Identifying unwanted access to sensitive data
    * Conducting real-time analysis surrounding usage and access patterns



[Unit 42 Cloud Security Assessment](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) can help turn cloud complexity into actionable security insights.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107
  * South Korea: +82.080.467.8774



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://start.paloaltonetworks.com/contact-unit42.html).

## Additional Resources

  * [Aggregated sinks overview](https://start.paloaltonetworks.com/contact-unit42.html) – Google Cloud
  * [Bucket Replication](https://start.paloaltonetworks.com/contact-unit42.html) \- AWS
  * [Pub/Sub](https://start.paloaltonetworks.com/contact-unit42.html) \- Google Cloud
  * [Pub/Sub Topic](https://start.paloaltonetworks.com/contact-unit42.html) \- Google Cloud
  * [Pub/Sub Subscription](https://start.paloaltonetworks.com/contact-unit42.html) \- Google Cloud
  * [Storage Transfer Service](https://start.paloaltonetworks.com/contact-unit42.html) \- Google Cloud
  * [Amazon Data Firehose](https://start.paloaltonetworks.com/contact-unit42.html) \- AWS
  * [Azure Monitor](https://start.paloaltonetworks.com/contact-unit42.html) \- Azure
  * [Prevent subdomain takeovers with Azure DNS alias records and Azure App Service's custom domain verification | Microsoft Learn](https://start.paloaltonetworks.com/contact-unit42.html)
  * [Azure-Network-Security/Cross Product /DNS - Find Dangling DNS Records](https://start.paloaltonetworks.com/contact-unit42.html) \- GitHub
  * [Building a Data Perimeter on AWS](https://start.paloaltonetworks.com/contact-unit42.html) \- AWS
  * [Overview of VPC Service Controls](https://start.paloaltonetworks.com/contact-unit42.html) \- Google Cloud
  * [Account regional namespaces for Amazon S3 general purpose buckets](https://start.paloaltonetworks.com/contact-unit42.html) \- AWS



Back to top

### Tags

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [CSPs](https://unit42.paloaltonetworks.com/tag/csps/ "CSPs")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

### Table of Contents

  *   * Executive Summary
  * Key Architectural Elements Enabling the Attack
    * Data Stream Overview
    * Global Uniqueness of Bucket Names
    * Permissions to Modify Data Stream Destinations
  * The Bucket Hijacking Attack
    * Simulating Bucket Hijacking in Google Cloud Logging
  * The Expansion to Multiple Services Within Google Cloud
    * Pub/Sub
    * Storage Transfer Service
  * The Expansion to Another Cloud Provider: AWS
  * Cross-Subscription Data Exfiltration in Azure
  * Exploitation Scenarios and Excessive Permissions Risks
    * Exploitation Scenarios and Detection Challenges
    * How Over-Privileged Roles Increase the Risk
  * Mitigation Strategies
  * Conclusion
  * Palo Alto Networks Protection and Mitigation
  * Additional Resources



### Related Articles

  * [ Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "article - table of contents")
  * [ Pass the Passkey: A Novel Attack Surface in Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/ "article - table of contents")
  * [ Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy ](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)