# Detection Engineering at Scale: One Step Closer (part two)

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/detection-engineering-at-scale-one-step-closer-part-two
- **Date :** 2025-02-04

---

In this article, we will build upon the [previous discussion](/blog/detection-engineering-at-scale-one-step-closer-part-one) of our detection approach and associated challenges by detailing the regular and automated actions implemented through our CI/CD pipelines.

## The catalyst: an approach to detection engineering at scale

Our approach serves as a catalyst to help you scale efficiently with minimal challenges; however, it is not a universal solution to all problems. It demands careful attention and expertise from detection engineers and is designed to align closely with practices commonly employed by developers and DevOps teams.

This methodology is structured around five key steps, as outlined below:

![The catalyst: an approach to detection engineering at scale](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a577e9a71d422840d6ac_6a92a20e51d97c29d2a2f57f_6a2a7ee3587ea886e0841fd2.webp)

The catalyst: an approach to detection engineering at scale

We will now take a closer look at each step.

## Detection rule creation

This may seem like an obvious step, but the details involved are often less straightforward. A detection rule, irrespective of the language used, comprises two key components: the metadata and the detection pattern.

At Sekoia.io, we use Sigma as our detection language, meaning the files are written in YAML. Each file is a detection rule, composed of selections that are evaluated based on a condition defined at the end. While this approach is effective, it poses a challenge: if a detection engineer wants to add a filter to exclude a false positive, the modification will affect the entire detection pattern. This limitation is common across most detection languages, where filters are not separated from the core detection logic. This is a crucial consideration for the "Continuous Tests" section of this blog, as it necessitates testing the syntax and the logic of the detection rule after every single change.

It is important to emphasise that we have deliberately [chosen](https://docs.sekoia.com/xdr/FAQ/intelligence/Detection_qa/#have-you-created-rules-for-specific-vulnerabilities-cves-why-not) to avoid creating certain types of detection rules that are excessively complex to manage over time and offer relatively low usefulness. Our focus is exclusively on detecting Technics, Tactics and Procedures (TTPs), as we strongly believe these will remain relevant regardless of the specific circumstances. For instance, when a new vulnerability emerges, a detection rule is created only if it is deemed highly critical, such as the case of ZeroLogon in the past.

Similarly, we refrain from creating what we refer to as "IoC detection rules", where a specific file name is flagged for a particular intrusion set. This decision is based on two key considerations. First, our CTI feed is capable of handling such detections, and we believe it is more effective to manage them in the STIX format. STIX allows us to add validity dates to an indicator, furthermore our CTI feed can be consumed separately, allowing us to protect more customers. Second, from a long-term perspective, these rules tend to be cumbersome to maintain and manage, making them less practical in our approach to scalable detection engineering.

The metadata associated with detection rules are equally as important as the detection patterns themselves, particularly for automation purposes. In the process of creating detection rules, it is highly recommended to carefully consider the metadata based on your specific automation requirements. In essence, ask yourself: what metadata will be necessary for newly created detection rules? Additionally, what information should be maintained or updated with each modification of an existing detection rule?

All this metadata is then used in CI/CD pipelines to automatically generate documentation and testing frameworks, which is described later in this article.

Once a detection rule is created - or more often, concurrently - the detection engineer documents their research in an **Alerting and Detection Strategy** file.

### Alerting and Detection Strategy Framework (ADS)

This framework, developed by Palantir and slightly adapted to suit our needs, is designed to encourage detection engineers to carefully consider various aspects when creating detection rules and to document their thought process. We will not go into detail about this framework, as it is thoroughly documented [here](https://github.com/palantir/alerting-detection-strategy-framework/blob/master/ADS-Framework.md). This approach benefits rule reviewers and provides valuable context for future detection engineers who may need to work with rules that are several years old.

Every aspect of this framework is important, but the **Validation** and **False Positives** steps are particularly critical for us. 

Detection engineers must thoroughly document how their detection rule was validated. This documentation is essential not only for confirming the rule's functionality but also for enabling others to replicate the validation process. In some instances, particularly with certain products, conducting a lab test may not be feasible. In such cases, it is crucial to specify whether the validation was performed in a reproducible test environment or achieved otherwise.

Documenting observed false positives, including their frequency and the query used to identify them, is equally important. This information is critical for thorough rule reviews prior to moving them into production and remains valuable in the long term. A rule that performs well in year _n_ may degrade significantly by year _n+1_. This degradation can result from various factors, such as changes in your customer base and their environments or the introduction of new products in the market that execute previously unobserved actions.

### CI/CD and versioning

To enable detection engineers to scale effectively and sustainably over the long term, CI/CD and versioning are essential. At Sekoia.io, we leverage GitHub alongside GitHub Actions to automate the generation of documentation and conduct continuous testing. The diagram below provides an overview of our CI/CD process:

![To enable detection engineers to scale effectively and sustainably over the long term, CI/CD and versioning are essential.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a577e9a71d422840d6af_6a92a20fdae089660dfbe88c_6a2a7ee4587ea886e0841fd6.webp)

To enable detection engineers to scale effectively and sustainably over the long term, CI/CD and versioning are essential.

As shown in the diagram, several tests and the generation of documentation, represented in the upper part of the diagram, are executed only when a new pull request is created, while two specific tests are performed on a daily basis. Finally, we utilise instant messaging to send notifications. This approach aligns with our goal of adopting best practices from development and DevOps.

With this overview in mind, let’s delve deeper to understand the reasoning behind these practices.

### Continuous tests

As shown above, several tests are performed during our CI/CD process. To understand the purpose of each one, we think it is better to proceed with some use cases.

#### Use case 1: adding a filter to a detection rule

This scenario is a common occurrence among detection engineering teams: a false positive has been identified and needs to be excluded.

Whether the exclusion involves a simple or complex filter, the impact on the detection rule is fundamentally the same. As previously mentioned, any change affects the entire rule pattern, making the first and most obvious step the **verification of the rule’s syntax** to ensure it remains valid on a grammatical level.

Once the syntax has been validated, the next step is to test the logic of the rule. However, before proceeding, it is essential to establish whether the appropriate tests are in place. Much like in software development, ensuring **comprehensive test coverage** is crucial. Every logical condition of the rule must be tested to confirm that it functions as intended and aligns with the detection engineer’s objectives.

For detection engineers using Sigma for instance, simply verifying that the “filter” selection works correctly after adding an exclusion is insufficient. Changes to the condition could potentially break the rule, and inadvertent modifications or omissions could introduce regressions. Thorough **testing of both the syntax and logic is therefore imperative**.

Once test coverage is confirmed, we proceed to **testing the detection rule’s logic**. This begins by retrieving events—either from our lab, where the detection engineer creates and tests the rule to ensure it triggers an alert, or, if not feasible, to retrieve an event provided by the editor.

However, one significant challenge remains: the test events are captured at the time the detection rule is created, meaning the tests are static and do not adapt over time. This raises a critical question: what happens to our rules if a log parser is modified? Yes, such changes could potentially break the rules.

This leads us to use case number 2.

#### Use case 2: log parser update

Fortunately, the original log is preserved within these test events. To address this issue, the **original log is replayed against the parsers** daily to ensure the rule continues to function as expected. 

Ideally, your organisation has a pre-production environment where test events can be replayed against parsers before any changes impact detection rules in production. This is the approach we follow, in addition to replaying these events in the production environment as a precautionary measure.

Here is a summary of all the tests continuously performed through the CI/CD process:

  1. **Rule Syntax Checking** : Ensuring the detection rule is grammatically correct.
  2. **Test/Code Coverage** : Verifying comprehensive test coverage for the rule's logic.
  3. **Execution of Tests with Real Events** : Running tests using real events created by the detection engineer.
  4. **Replaying Original Logs in Pre-Production** : Using the original logs (unparsed message) from the test events to validate them against log parsers in a pre-production environment.
  5. **Replaying Original Logs in Production** : Similar to step 4, but executed in the production environment to ensure continued functionality.



This approach provides a robust and scalable testing framework for your detection rules, seamlessly integrated into the CI/CD pipeline. The trade-off, however, is that detection engineers must exercise meticulous attention to detail, which may require additional time when creating a detection rule.

It leaves one final crucial step in the process: the automatic generation of documentation.

### Automatically built documentation

Most of the documentation needs were enumerated earlier in this article: 

  * Identifying which detection rules are compatible with which log source.
  * Providing a comprehensive MITRE ATT&CK matrix that includes all rules, along with individual matrices for each log source (such as [this one for ProofPoint TAP](https://docs.sekoia.com/integration/categories/email/proofpoint_tap/#related-built-in-rules) for instance), as some detection rules apply only to certain log sources.
  * [Listing the EventIDs](https://docs.sekoia.com/xdr/features/detect/built_in_detection_rules_eventids/) used by our detection rules, enabling customers to prioritize their configuration efforts accordingly. _These eventIDs are retrieved from the detection rule pattern as well as the “test events”._
  * [Maintaining a changelog](https://docs.sekoia.com/xdr/features/detect/rules_changelog/) for each rule to keep customers informed of updates. We opted not to rely on Git commits to allow for greater flexibility.



All of this is performed automatically, thanks to the rigorous initial process, which ensures seamless integration with the CI/CD pipeline.

## Conclusion

To conclude this second article in our series, implementing detection engineering at scale while adopting best practices from software development serves as a cornerstone for enhancing the efficiency and reliability of detection efforts. 

In the final part of this series, we will discuss the significance of integrating ongoing monitoring and review into the detection engineering process.

Thank you for reading this blog post. Please don’t hesitate to provide your feedback on our publications. You can contact us at tdr[at]sekoia.io for further discussions, always good to have feedbacks from peers.