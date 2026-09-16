# AWS Detection Engineering: Logs Sources & Events Guide

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/aws-detection-engineering
- **Date :** 2024-04-18

---

## Introduction

To enhance our threat intelligence, improve detection and identify new threats, Sekoia.io analysts perform continuous hunting and detection engineering every day to give our customers more options to protect themselves. Sekoia.io Threat Detection & Research (TDR) team is there to fill our SOC platform with detection rules and CTI. While Sekoia.io wants to be vendor-agnostic, some rules need to be vendor-specific to keep high-quality and high-fidelity detection in our platform.

This is the case for AWS where the logs are highly specifics, and our customers' environments differ a lot depending on the usage.

This short article will present the main logs sources for AWS, along with some relevant events defenders could use to detect attackers. This is overall non exhaustive and is more targeted for detection engineers that are just starting with AWS.

## Three main logs sources from AWS

AWS is composed of many different services, some of them act as log sources and most of them send their logs through **AWS CloudTrail**. To monitor S3, EC2, IAM, or other commonly used services, only CloudTrail is mandatory to retrieve the required logs for security purposes. In fact, an important amount of logs is sent with events that are not meaningful for detection. To avoid impacting performance while still being able to detect attacks, at Sekoia.io a choice was made to ignore some logs for specific API calls as there were millions, even billions of them, which are not useful for detection purposes.

However to have more insights and protection of your AWS tenants, two other sources are often good to have: **AWS Flow Logs** and **AWS GuardDuty**.

Flow Logs is right in the name: these logs are simply netflow within your AWS tenant. It is nice to have, especially with Threat Intelligence capabilities to spot malicious contacted IPs or domain names. The main caveat for Flow Logs is that they often send way too many events, like most netflows, making it hard for an XDR editor to retrieve everything without impacting performances.

GuardDuty is the AWS threat detection service. It is therefore highly specialized and good to have to improve detection of your AWS tenants overall. While having detection rules on CloudTrail and CTI on Flow Logs is really nice, this service is a great addition to have better coverage against AWS-related threats. This service logs are mainly “alerts” therefore it sends a few logs compared to Flow Logs and CloudTrail.

## Building detection for these sources

### GuardDuty

For GuardDuty the “easy way” was chosen, as it is already a detection product that is great and does not fire too many false positives, an alert is created whenever GuardDuty creates one, depending on the criticality level.

### FlowLogs

For AWS Flow Logs, as the logs are netflows, building actual SIGMA detection rules is tough as an editor that can’t really fine-tune the rules for each customer’s environment. However, since our team also tracks attackers’ infrastructure to put IOCs in our platform, the decision was to not make any specific detection rule for Flow Logs. Instead Sekoia.io CTI matches on the parsed fields and therefore malicious activity could be spotted through that.

### AWS relevant events

In this section, a quick overview by TTP of some relevant events for AWS detection engineering will be given. This is of course not an exhaustive list as there are many.

#### Initial Access

** _AttachUserPolicy_** is a great event to find out which Policy was attached to an user, and there is one parameter that is highly relevant for detection purposes: **_AWSCompromisedKeyQuarantineV2_**. This means that AWS detected that your access key was compromised. When this detection occurs, AWS limits the key accesses to remove most of the rights and therefore the key becomes not usable for an attacker. Still, it is worth firing alerts on this event because the way AWS detects a compromised key means you should take actions. Indeed, most of the time it comes from a leak of the access key online. For instance, AWS scans public GitHub repositories continuously and if it detects your access key it will fire that event and take actions right away. This means you have an online leak and should be taken seriously to remove sensitive information.

#### Persistence

There are many ways on AWS for an attacker to establish persistence on a tenant. One very easy common way is to create a KeyPair for a highly-privileged user to allow SSH connections. An attacker can also use that specifically to connect to an EC2 instance. To perform these actions, several events can be logged, mostly the following ones:

**_CreateKeyPair_ , _SendSSHPublicKey_ , _SendSerialConsoleSSHPublicKey_. **

There are a few false positives due mainly to administrative actions, but these are nice events to catch and check.

Another way to establish persistence is to create or update an identity provider, whether a SAML one or an OpenID one. These actions are also logged and several events can be raised such as **_AddClientIDToOpenIDConnectProvider_ , _CreateOpenIDConnectProvider_ , _CreateSAMLProvider_ , _UpdateSAMLProvider_** to name a few. And an attacker can cover his tracks by deleting them, which also raises events such as **_DeleteSAMLProvider_**.

There are many other ways to establish persistence like creating new users or changing passwords. These actions raise events and could be catched as well.

#### Defense Evasion

For systems-oriented attacks, threat actors trying to evade defense by disabling logging or security tools like AntiVirus are common techniques. Same goes for AWS. Attackers can disable GuardDuty, CloudTrail and FlowLogs easily with the correct rights in the tenant.

They could also simply update a trail to remove just a specific logging capability, depending how stealthy they want to be. Thankfully for defenders, several events can be monitored. DeleteFlowLogs is a good one to monitor for FlowLogs as the name states. Other events like **_DeleteTrail_** , **_StopLogging_** or **_UpdateTrail_** for CloudTrail logs are great to monitor as well. For GuardDuty, **_DeleteDetector_** , **_UpdateDetector_** or **_CreateIPSet_** are nice events to look at. The first two have explicit names but the last one can be trickier and forgotten. This event allows monitoring when someone is updating the list of the GuardDuty trusted IP addresses. An attacker can use this to whitelist its C2’s IP addresses to avoid detection.

#### Discovery

Several events related to discovery are logged by AWS CloudTrail. This is really useful for investigations but hard to build detection rules upon these events since, just like for Windows discovery, it fires lots of legitimate events.

To build detection rules for discovery, many reports were studied and an AWS HoneyPot was built to check what’s the most used discovery commands by attackers. From that, Sekoia.io analysts managed to create a correlation rule based on a few _Describe*_ events: 

  * ** _DescribeInstances_**


  * ** _DescribeInstanceTypes_**


  * ** _DescribeInstanceTypeOfferings_**


  * ** _DescribeAccountAttributes_**


  * ** _DescribeSecurityGroups_**


  * ** _DescribeKeyPairs_**


  * ** _DescribeCapacityReservations_**


  * ** _DescribeAvailabilityZones_**


  * ** _DescribeRegions_**


  * ** _DescribeLaunchTemplates_**


  * ** _DescribeHostReservations_**


  * ** _DescribeImages_**


  * ** _DescribeSnapshots_**



Despite this and the correlation capability that looks for 10 of these events in 30min, this needs fine-tuning for each environment (whitelisting some users mostly) as it can still fire several alerts each day.

#### Exfiltration

Exfiltration is often done on the EC2 instances, not on a “tenant-level”. Exfiltration on EC2 instances can be done in a classic way by attackers just like defenders are used to on common OS. However one event is interesting to look at: **_CreateInstanceExportTask_**. This event is EC2 specific and reports when someone is trying to export an AWS EC2 instance. It’s not performed that often by companies and could be a great easy catch for defenders.

#### Impact

One notable feature with AWS when creating/modifying an EC2 instance is the [Userdata configuration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-launch-instance-wizard). A very common threat abusing this technique is cryptomining. TDR was able to monitor an attacker, on our AWS Honeypot, creating new instances, with malicious payload being configured (through a simple bash script) in the User data instance part. This would be detected through the **_RunInstances_** event, however UserData are considered as sensitive by CloudTrail (which is correct as there can be private information about the user like private keys). Therefore the data is removed by CloudTrail, making it impossible to base detection on that. Still though, if you have a strict policy and not many RunInstances events, you could combine that with the userData parameter being present to build detection.

## Conclusion

With this short introduction to AWS detection engineering, the main things to remember are that different logs sources contribute to detect attacks: CloudTrail, FlowLogs and GuardDuty to name the most commonly used. For each source there are different events that should be studied by detection engineers. Some events are really simple without false positives in a corporate environment. Others are complex and need to be studied in depth (in the requests and response parameters for CloudTrail most of the time) to be useful for detection. Sekoia.io customers are protected against the AWS threats described in this blogpost. As the other detection rules, AWS detection rules are available in the Rules Catalog. Sekoia.io TDR team is committed to update this catalog regularly to improve existing detection rules or create new ones to always provide the best protection against cyber threats.