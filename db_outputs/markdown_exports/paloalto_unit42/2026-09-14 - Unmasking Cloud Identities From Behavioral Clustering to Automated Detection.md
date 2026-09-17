# Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/
- **Date :** 2026-09-14

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")



[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 12 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Cortex XDR icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XDR](https://unit42.paloaltonetworks.com/product-category/cortex-xdr/ "Cortex XDR")[![Cortex XSIAM icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex XSIAM](https://unit42.paloaltonetworks.com/product-category/cortex-xsiam/ "Cortex XSIAM")[![Idira icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/idira_RGB_logo_Icon_Color-e1787069105644.png)Idira](https://unit42.paloaltonetworks.com/product-category/panw-idira/ "Idira")[![Unit 42 Cloud Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Cloud Security Assessment](https://unit42.paloaltonetworks.com/product-category/cloud-security-assessment/ "Unit 42 Cloud Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Osher Jacob](https://unit42.paloaltonetworks.com/author/osher-jacob/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:September 14, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/)
    * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/)
    * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/)
    * [IAM](https://unit42.paloaltonetworks.com/tag/iam/)
    * [SQL](https://unit42.paloaltonetworks.com/tag/sql/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/?pdf=download&lg=en&_wpnonce=252a1929a6 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/?pdf=print&lg=en&_wpnonce=252a1929a6 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Unmasking%20Cloud%20Identities:%20From%20Behavioral%20Clustering%20to%20Automated%20Detection&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fbehavioral-clustering-map-to-cloud-identities%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbehavioral-clustering-map-to-cloud-identities%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbehavioral-clustering-map-to-cloud-identities%2F&title=Unmasking%20Cloud%20Identities:%20From%20Behavioral%20Clustering%20to%20Automated%20Detection "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbehavioral-clustering-map-to-cloud-identities%2F&text=Unmasking%20Cloud%20Identities:%20From%20Behavioral%20Clustering%20to%20Automated%20Detection "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fbehavioral-clustering-map-to-cloud-identities%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Unmasking%20Cloud%20Identities:%20From%20Behavioral%20Clustering%20to%20Automated%20Detection%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fbehavioral-clustering-map-to-cloud-identities%2F "Share in Mastodon")



## Executive Summary

As cloud environments expand to include human, machine and autonomous agent identities, mapping the functional roles of these identities has become a significant security challenge. To address this challenge, we designed a behavioral clustering model that extracts activity patterns from cloud audit logs. By adopting a clustering-based approach to identity mapping, organizations can gain greater visibility into cloud activity and integrate these behavioral patterns into automated threat detection mechanisms.

To create our behavioral clustering model, we examined the behavior of over 40,000 identities from 125 cloud environments over a two-month period, mapping these identities to functional roles. These roles include administrators, backup services, security tooling and development and operations (DevOps).

Identifying these functional roles is rarely straightforward because resource naming conventions or assigned identity and access management (IAM) policies do not always reveal an identity’s true behavior. Attackers routinely use masquerading techniques like pre-existing permission profiles and benign labels to make malicious activity harder to detect.

To illustrate the practical application of our model, we provide an in-depth analysis of the dataset's largest cluster: administrator console users in Amazon Web Services (AWS). We also show how an identity’s behavioral patterns provide richer context for cloud threat detection.

Additionally, we demonstrate how lightweight heuristic logic can be extracted directly from the clustering map, which can be implemented in standard SQL. This allows organizations to classify functional identity roles at scale, delivering continuous operational visibility without the need to continuously run a resource-intensive machine learning pipeline.

The methodology applied in our behavioral clustering model uses unsupervised machine learning algorithms, specifically Uniform Manifold Approximation and Projection ([UMAP](https://umap-learn.readthedocs.io/en/latest/)) and Hierarchical Density-Based Spatial Clustering of Applications with Noise ([HDBSCAN](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html)), to construct a reliable behavioral map. This approach automatically categorizes a vast collection of cloud identities into distinct, clustered groups.

While our research specifically focuses on AWS CloudTrail data, the methodology can be easily extended to audit logs from other cloud providers, software as a service (SaaS), Kubernetes and other environments.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

  * [Cortex Cloud](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud)
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM)
  * [Idira Privileged Access Management (PAM)](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1)
  * [Idira Identity Governance and Administration (IGA)](https://www.paloaltonetworks.com/idira/human/identity-governance)



[Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Cloud](https://unit42.paloaltonetworks.com/tag/cloud-security/), [Identity](https://unit42.paloaltonetworks.com/tag/identity/), [Detection](https://unit42.paloaltonetworks.com/tag/threat-detection/)**  
---|---  
  
## The Identity Challenge

When it comes to accurately detecting malicious activity within cloud environments, context is key. Consider a scenario where a cloud identity enumerates all resources within your environment. Is this a security tool that frequently scans resources as part of its normal routine? Or is it a service identity that usually serves a limited purpose, such as a backup service that only interacts with a single cloud storage bucket? One of these scenarios represents normal operational activity, the other indicates a potential security breach.

This reality forces us to draw a distinction between capabilities and active behavior:

  * **What an identity can do** : Identity permissions dictate the operations that a role is permitted to perform. Although the industry-standard recommendation is to enforce the principle of [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), the reality is that many identities remain heavily over-privileged. This typically happens due to misconfigurations, a lack of visibility or simply a desire to reduce technical friction during rapid development. Attackers can exploit over-privileged identities to execute malicious operations that should have been blocked by tighter access controls. At the same time, many over-privileged identities exist in production for years without ever causing an issue. Security teams use cloud security posture management (CSPM) to audit assigned cloud permissions – but this is only part of the identity puzzle.
  * **What an identity actually does** : This lies within the domain of [cloud detection and response (CDR)](https://www.paloaltonetworks.com/cyberpedia/what-is-cloud-detection-and-response-cdr). Analyzing the practical evidence of operations invoked by different identities is the main focus of this article. To do this we inspect observed API activity such as authentication (ConsoleLogin, GetSigninToken) and discovery (ListBuckets, ListRoles). To interact with the 240 services offered by AWS, there are more than 15,000 possible operations an identity can invoke.



Given that thousands of identities are operating across complex cloud environments, we are left with the following questions:

  * Are there common behavioral patterns that identities naturally follow?
  * How can we reliably differentiate between the footprints of various functional roles such as administrators, DevOps, backup services and security tools?



## Mapping the Landscape: Functional Identity Roles

Analyzing the specific cloud operations an identity invokes, as captured in [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), provides a clear picture of its day-to-day behavior and role. When observing a large enough collection of identities across multiple organizations, a macro-level picture begins to emerge.

A behavioral map visualizes each identity as a distinct data point, where its invoked operations dictate its coordinates. The scatter plot in Video 1 projects a vast array of AWS identities into a two-dimensional space based on their executed operations.

&lt;span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start"&gt;﻿&lt;/span&gt;&lt;br /&gt; 

Video 1. AWS identity behavioral map. 

In this simplified visualization, each dot represents a unique cloud identity, projected into a two-dimensional space where proximity reflects behavioral similarity and colors reflect behavioral clusters.

This map features the 30 largest clusters found in the dataset, representing approximately 20,000 identities. Due to a limited color palette, some colors are reused across the visualization; however, each spatially separated dense region represents its own isolated cluster.

The visual datapoint clustering, along with additional quantitative metrics, indicate that cloud identities have a strong tendency to share similar behavioral traits, often mapping to the same functional roles across different organizations.

### Analytical Methods

To decode the functional role associated with each behavioral cluster, we combined four analytical methods:

  * Operation frequency: Analyzing the most frequent operations invoked within each cluster
  * Class-based scoring (c-TF-IDF): Using [c-TF-IDF scoring](https://maartengr.github.io/BERTopic/api/ctfidf.html) to identify operations that distinguish one cluster from the rest
  * Attribute-based mapping: Highlighting various portions of the map based on specific operations, services and/or string matching
  * Identity naming patterns: Mining common substrings and naming conventions within each cluster



To illustrate these methods, we narrow our analysis to a well-isolated cluster shown in Video 2. Consisting of roughly 5,000 identities spanning over 100 cloud projects, it represents one of the largest, most dense clusters in our dataset: administrative user identities.

&lt;br /&gt; 

Video 2. Detailed view of the administrative identity cluster.

The clustering algorithm we use is hierarchical, allowing us to partition large clusters into distinct sub-behaviors. However, for the purposes of this research, we analyze the cluster at a macro level, focusing on identities operating through the AWS Management Console.

#### Operation Frequency

An analysis of the most frequent operations within this cluster revealed a defining characteristic: roughly 94% of the identities invoked [ConsoleLogin](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.html), an AWS Management Console sign-in event, as Figure 1 shows. For comparison, fewer than 1% of identities in any other cluster performed this operation.

![A chart lists AWS operations with their mean values.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-141084-186821-3.png)Figure 1. The most frequent cloud operations executed within the selected cluster.

We can also see that around 60% of the identities in the cluster invoke additional operations associated with the default AWS Console behavior, such as [GetCostAndUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html) and [GetCostForecast](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostForecast.html).

#### Class-Based Scoring

To look beyond raw frequency and uncover the most distinguishing operations for this group, we examined the cluster using c-TF-IDF scoring, as illustrated in Figure 2. The APIs with the highest op_score serve as behavioral markers, occurring frequently within the selected cluster while remaining relatively rare across the rest of the global dataset.

![A list of AWS operation names related to health, cost optimization, and inspection services, along with corresponding numerical scores.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-143905-186821-4.png)Figure 2. Distinguishing operations of the selected cluster based on c-TF-IDF scores.

The scoring results show that operations that are automatically triggered when logging into the AWS console – such as [ListNotificationHubs](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationHubs.html) – receive higher scores than those based on raw frequency analysis.

#### Attribute-Based Mapping

To further validate the hypothesis that this is a cluster of administrative user identities, we also examined textual metadata. We looked at the entire clustering map and highlighted only the identities whose resource names contain the substring admin. In Video 3, the admin string shows a strong concentration within our selected target group.

&lt;br /&gt; 

Video 3. Global behavioral map, with identities containing the admin substring highlighted in orange.

In addition to highlighting portions of the map based on names, it is also possible to highlight them based on attributes such as specific invoked operations, usage of selected services such as S3, EC2 Lambda or any other measurable attribute.

#### Identity Naming Patterns

Mining common substrings from identity names provides additional context for cluster analysis. While relying on naming conventions of a single identity alone can generate inaccurate results, recurring patterns within a cluster help explain its underlying behavior. Using a [Generalized Suffix Tree](https://en.wikipedia.org/wiki/Generalized_suffix_tree), we algorithmically discovered the cluster's most frequent substrings rather than searching for specific arbitrary keywords like “admin.” Among the top results was [AWSReservedSSO_AdministratorAccess_](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AdministratorAccess.html) – the default prefix generated when assigning AdministratorAccess via AWS IAM Identity Center.

#### Landscape Mapping Summary

Combining these quantitative methods with visual mapping allows us to confidently conclude that this cluster indeed represents administrative users operating primarily through the AWS Management Console.

Repeating this profiling process across our dataset reveals clear, reproducible clusters for both human and machine identities, some of which shown in Figure 3. We were able to identify clusters based on behavioral patterns, including:

  * DevOps
  * Infrastructure as Code (IaaC) runners
  * Continuous integration and continuous delivery (CI/CD) systems
  * Security products
  * Backup agents
  * Networking components
  * FinOps platforms

![A scatter plot displaying clusters marked with names such as "CI/CD," "Console Admins," "Data Lake," "DevOps," and more. Each cluster is denoted by color and encircled by dashed lines, positioned against a grid background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-159648-186821-6.png)Figure 3. Global behavioral map with identified clusters labeled.

## Methodology: The Clustering Pipeline

To build this behavioral map, we constructed a multi-stage data pipeline, as illustrated in Figure 4. The pipeline consists of the following stages:

  * Cloud audit log ingestion
  * Pre-processing and vectorization
  * Dimensionality reduction
  * Clustering

![A flowchart depicting a process involving cloud audit logs. It starts with ingesting cloud audit logs, followed by pre-processing and vectorization to create high-dimensional vectors. These vectors are then processed through UMAP for dimensionality reduction. Projected vectors result in dense embeddings for HDBSCAN, assigning cluster IDs, and 2D visualizations for assigning 2D coordinates.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-162638-186821-7.png)Figure 4. The complete pipeline with its multiple stages.

The process begins by converting raw cloud audit logs into identity vectors that capture each identity's behavior and allow us to measure the distance between them. In this format, each identity is represented as a vector containing information about the specific operations it invoked.

By treating the set of possible operations as a “vocabulary,” we can represent each identity as a boolean vector where positions are marked true if the operation was invoked within the given timeframe. Because this vocabulary spans at least 15,000 [possible operations](https://docs.aws.amazon.com/boto3/latest/reference/services/) — most of which are rarely invoked — the resulting vectors are both large (high-dimensionality) and sparse (mostly filled with zeros), making them challenging to process. Figure 5 shows the data format after this vectorization process, using test identities and data.

![A table showing various AWS IAM roles and users with their associated permissions and activity counts. Columns display counts for security configurations, records, tags, and configuration sets, mostly showing zeros, except for a few entries.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-165143-186821-8.png)Figure 5. Sparse matrix representation of cloud identity behavior using boolean vectors.

We applied the [Uniform Manifold Approximation and Projection (UMAP)](https://umap-learn.readthedocs.io/en/latest/) algorithm to reduce high-dimensional data into a lower-dimensional space while preserving its essential structure. Considering our vector representation, we found that [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) works well as the distance metric for UMAP, as it focuses on the angle between the vectors rather than their magnitude.

We ran this dimensionality reduction on the vectorized data, processing it in two parallel passes:

  * The first pass creates dense embeddings, which are lower-dimensional vectors for the clustering algorithm. This significantly reduces dimensions while preserving enough detail to maintain behavioral information.
  * The second pass compresses the original sparse vectors into a two-dimensional plot specifically for visualization, as shown in Figures 1, 2 and 5.



Figure 6 shows how the format and dimensionality of the data change after applying UMAP in the first pass. The initial large vectors consisting of over 10,000 boolean values are transformed into much smaller, dense vectors with 32 continuous values.

![A diagram illustrating dimensionality reduction using UMAP. The top section shows a table with identity roles "Logger" and "DataResilience" and corresponding permissions, with dimensions over 10,000. An arrow labeled "Dimensionality Reduction \(UMAP\)" points to a lower section, showing the same identities with reduced dimensions labeled d0, d1, and d2, consisting of numerical values.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/word-image-167979-186821-9.png)Figure 6. Illustration of the dimensionality reduction process.

At this stage, we feed the dense embeddings into the [Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN)](https://hdbscan.readthedocs.io/en/latest/how_hdbscan_works.html) algorithm, which groups the identities by detecting dense regions in the dataset.

Once every identity is assigned to a cluster, or labeled as an outlier, we can begin investigating the groups to understand their shared behaviors. This analysis focuses on their common traits and how to distinguish them from identities in other clusters. The resulting groups align closely with standard functional roles in cloud environments, such as Administration, DevOps, Security and CI/CD.

## Automated Detection Mechanics

After discovering the behavioral groups using the above pipeline, we can scale this detection capability to ingest new identities and automatically determine whether they belong to a known cluster.

Instead of running the full pipeline, we train a classifier to evaluate cluster membership for groups of interest. For example, a dedicated classifier can be built to detect DevOps users, while a different classifier can detect security tools.

We found that a simple [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) model trained directly on the original sparse boolean vectors can accurately identify our clusters of choice. Unlike more complex machine learning models that often require additional tools to interpret outputs and decisions, the trained logistic regression model is highly interpretable. This enables us to observe the cloud operations required to infer cluster membership, along with their respective mathematical weights.

In practice, the model's inference logic calculates a weighted sum of the present operations. This means that we can determine how each cloud operation increases or decreases the likelihood that an identity belongs to a target cluster, and which operations are most important for prediction.

Because the vocabulary of possible operations is vast, assigning weights to thousands of mostly irrelevant operations would be unnecessary. To address this challenge, we used L1 regularization, also known as [Lasso](https://en.wikipedia.org/wiki/Lasso_\(statistics\)). This is a penalty that forces the model to reduce the coefficients of irrelevant features to absolute zero, compressing the model to focus exclusively on a small subset of critical, defining operations.

These steps result in a local approximation of our more complex clustering model. By training the classifier on specific groups, the model is essentially distilled into an indicative set of a few dozen operations paired with corresponding coefficients. This concise logic can be used to quickly infer whether an identity belongs to a DevOps, administrative or security product cluster.

Beyond being transparent and explainable, this lightweight logic is simple and efficient enough to be implemented directly within standard SQL queries. By adopting this lightweight approach, organizations can perform accurate role inference at scale, without relying on resource-intensive pipelines.

## Conclusion

While posture management establishes the essential baseline of what an identity is permitted to do, analyzing its behavior reveals what it actually executes in production. Knowing the true functional baseline of an identity allows security teams to quickly spot deviations, flag defense evasion attempts and accelerate incident response.

By utilizing unsupervised machine learning algorithms like UMAP and HDBSCAN, we demonstrated that cloud identities naturally form distinct behavioral clusters. Rather than relying on static assigned permissions, these clusters accurately reflect an identity's true functional role within an environment — such as administrative access, CI/CD pipelines or security scanning services.

After establishing these behavioral clusters, we can efficiently map identities to their functional roles using lightweight logic distilled from our model. This logic can be implemented directly in standard SQL queries, enabling highly scalable identity classification across enterprise environments. This methodology can also be applied to audit logs from other sources of operational data, including different cloud providers, Kubernetes and SaaS.

Enriching standard telemetry with behavioral metadata adds an important layer of context, exposing high-risk anomalies that static analysis could miss, such as a compromised backup service suddenly executing administrative actions.

As cloud environments continue to grow in complexity, a context-aware approach serves as a robust blueprint for future detection strategies, offering a clear path toward more precise, efficient and proactive security operations.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

  * [Cortex Cloud](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud) can help protect cloud posture and runtime operations against identity-driven threats by pairing static permission baselines with deep behavioral context. By embedding the functional identity baselines discussed in this research into our detection engine, Cortex Cloud adds a vital layer of operational context, enabling security teams to filter out noisy false positives and decisively catch threat actors attempting to masquerade, alter configurations, or execute anomalous operations in the environment.
  * [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) are designed to prevent the execution of known malicious malware and prevent the execution of unknown malware using Behavioral Threat Protection and machine learning based on the Local Analysis module.
  * [Idira Privilege Access Management (PAM)](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1) can help unify privileged access across human, machine, and agentic identities to secure cloud access across multi-cloud environments. Building on proven PAM, it delivers centralized secrets management alongside modern controls like Just-in-Time access and Zero Standing Privileges. This enforces consistent least-privilege security across on-premises, cloud, and SaaS targets.
  * [Idira Identity Governance and Administration (IGA)](https://www.paloaltonetworks.com/idira/human/identity-governance) can help automate user access reviews and access provisioning, using AI Profiles to continuously define job-appropriate access rather than relying on static, hard-to-maintain roles. By analyzing entitlements at a granular level, Idira surfaces excessive privilege with less effort, enforces least privilege at scale, and provides the integrated governance foundation for Zero Standing Privilege across all identities.



[Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is an evaluation service that reviews cloud infrastructure to identify misconfigurations and security gaps.

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

  * [BERTopic: Neural topic modeling with a class-based TF-IDF procedure](https://arxiv.org/abs/2203.05794) – Maarten Grootendorst
  * [UMAP: Uniform Manifold Approximation and Projection](https://joss.theoj.org/papers/10.21105/joss.00861) – Leland McInnes, John Healy, Nathaniel Saul, Lukas Großberger
  * [hdbscan: Hierarchical density based clustering](https://joss.theoj.org/papers/10.21105/joss.00205) – Leland McInnes, John Healy, Steve Astels



## Appendix: Cortex XDR/XSIAM Alerts Utilizing Behavioral Roles

Table 1 shows Cortex alerts that use roles assigned from behavioral analysis and the CDR module, mapped to MITRE ATT&CK® techniques.

**Alert Name** | **Alert Source** | **MITRE ATT &CK Technique**  
---|---|---  
AWS SSM send command attempt | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Cloud Administration Command (T1651)  
AWS Password Policy Discovery | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Password Policy Discovery (T1201)  
AWS resource discovery | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Account Discovery: Cloud Account (T1087.004)  
AWS web ACL deletion | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Impair Defenses (T1562)  
Compute activity in dormant cloud region | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Unused/Unsupported Cloud Regions (T1535)  
AWS Backup vault was deleted | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Inhibit System Recovery (T1490)  
Cloud instance creation attempt | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Modify Cloud Compute Infrastructure: Create Cloud Instance (T1578.002)  
AWS Lambda Cross-Account sensitive permissions configured | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Account Manipulation: Additional Cloud Roles (T1098.003)  
AWS IAM Role's Trusted Policy Modification Allows Cross-Account Access | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Account Manipulation: Additional Cloud Roles (T1098.003)  
AWS IAM Role Created with Cross-Account Access | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Account Manipulation: Additional Cloud Roles (T1098.003)  
AWS S3 bucket exposure via ACL / policy modification | XDR Analytics BIOC, Cloud Detection & Response Module (CDR) | Account Manipulation: Additional Cloud Roles (T1098.003)  
  
Back to top

### Tags

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/ "cloud detection")
  * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/ "DevOps")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [SQL](https://unit42.paloaltonetworks.com/tag/sql/ "SQL")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")

### Table of Contents

  * 


### Related Articles

  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "article - table of contents")
  * [ Essential Data Sources for Detection Beyond the Endpoint ](https://unit42.paloaltonetworks.com/detection-beyond-the-endpoint/ "article - table of contents")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/)