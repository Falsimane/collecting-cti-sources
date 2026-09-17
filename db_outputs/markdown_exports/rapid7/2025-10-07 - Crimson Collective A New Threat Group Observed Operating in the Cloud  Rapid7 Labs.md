# Crimson Collective: A New Threat Group Observed Operating in the Cloud | Rapid7 Labs

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-crimson-collective-a-new-threat-group-observed-operating-in-the-cloud/
- **Date :** 2025-10-07

---

## Introduction

Over the past few weeks, Rapid7 has observed increased activity of a new threat group attacking AWS cloud environments with the goal of data exfiltration and subsequent extortion of the victim. This threat group refers to itself as ‘Crimson Collective’ and has recently [announced](https://www.darkreading.com/application-security/red-hat-widespread-breaches-private-gitlab-repositories) that it is behind an attack on Red Hat, wherein it claims to have stolen private repositories from Red Hat’s GitLab.

Rapid7 observed the Crimson Collective in two cases in September. The threat group’s activity has been observed to start with compromising long-term access keys and leveraging privileges attached to the compromised IAM (Identity & Access Management) accounts. The threat group was observed creating new users and escalating privileges by attaching policies. When successful, the Crimson Collective performed reconnaissance to identify valuable data and exfiltrated them via AWS services. In case of the successful exfiltration of data, an extortion note is received by the victim.

Based on the available information, the Crimson Collective appears to be mostly focusing on collection and exfiltration of databases, project repositories, and other valuable data, putting at risk companies’ products and customers’ information.

The Crimson Collective was observed operating from multiple IP addresses across multiple compromised accounts in the same environment. They refer to themselves as “we” in the extortion note. This is suggesting the presence of multiple individuals behind the operation. However, the group’s composition remains unclear. The group was using the same sets of IP addresses across the observed cases.

## Technical analysis

![CC1.png](https://www.rapid7.com/cdn/images/blte3497b7e522fab3f/68e566b5758f5bf3c4d9df8b/CC1.png)

_Figure 1: Diagram of the attack_

###  Initial access and persistence

Based on the evidence from the available cloud logs, the Crimson Collective is using an open source tool called TruffleHog to find leaked AWS credentials. TruffleHog is a legitimate tool that can be used by security teams to verify the presence of forgotten long-term access keys in code repositories or other storage locations. In case such a credential is found, TruffleHog uses it to authenticate and call GetCalletIdentity API, which returns details about the IAM entity calling the operation. 

If TruffleHog receives a successful response, it returns the credential as valid. As of now it remains unclear where the group executed TruffleHog to search for the credentials used in the observed compromises. Nevertheless, analysis of CloudTrail logs confirmed usage of user agent TruffleHog as the initial step for all compromised accounts.

⠀

![CC2.png](https://www.rapid7.com/cdn/images/blt64317d66110b62b3/68e566b5c2504edff91fe304/CC2.png)

_Figure 2: TruffleHog - demo from the_[ _tool's official Github repository_](https://github.com/trufflesecurity/trufflehog)

⠀

Following the TruffleHog usage on the compromised accounts, further analysis uncovered the threat group attempting to establish persistence in the environment by creating a new user via API call CreateUser and subsequent CreateLoginProfile, which creates a password for the newly created user. Also, creation of new access keys via the CreateAccessKey API call followed. The user creation attempt was observed on every account compromised by the attacker. 

Accounts, which were not privileged enough to create new users were either disregarded and no follow up activity was observed on them, or in some cases the threat actor performed a SimulatePrincipalPolicy API call to simulate how policies attached to the IAM account work against provided API calls, thereby testing the extent of attached privileges.

### Privilege escalation and discovery

In an environment where the threat group successfully created a new user, they proceeded to elevate privileges via AttachUserPolicy API call, attaching arn:aws:iam::aws:policy/AdministratorAccess policy to the newly created account. AdministratorAccess is an AWS managed policy which grants full access to AWS services and resources.

With these newly created accounts and AdministratorAccess policy attached, the threat group moved to the discovery stage. Analysis of the CloudTrail logs uncovered extensive mapping of the AWS infrastructure and data. The threat group was observed to gather information about EC2 instances and their Security Groups, EBS volumes and snapshots, VPCs, Route Tables, Databases, Cost and Usage metrics for the account, Alarms, information about the account, and IAM roles. They also scoped service quotas for Amazon SES and SMS, both of which can be misused to send out malicious emails or SMS messages from the compromised AWS account.

Rapid7 found that the threat group used the following API calls across different AWS Services in the discovery phase:

**Identity and access management:**

  * ListRoles

  * ListIdentities

  * ListAccountAliases

  * GetUser

  * GetAccount




**EC2 (Elastic Compute Cloud):**

  * DescribeHosts

  * DescribeInstanceTypes

  * DescribeInstanceStatus

  * DescribeLaunchTemplates

  * DescribeTags




**EBS (Elastic Block Store):**

  * DescribeSnapshots

  * DescribeVolumes

  * DescribeVolumeStatus




**S3 (Simple Storage Service):**

  * ListBuckets

  * GetBucketLocation




**Network level information:**

  * DescribeRouteTables

  * DescribeLoadBalancers

  * DescribeVpcs

  * DescribeSubnets

  * DescribeRouteTables

  * DescribeInternetGateways

  * DescribeSecurityGroups

  * DescribeAvailabilityZones

  * GetHostedZoneCount

  * ListDomains




**RDS (Relational Database Service):**

  * DescribeDBInstances

  * DescribeDBSnapshots

  * DescribeDBSubnetGroups

  * DescribeDBEngineVersions

  * DescribeValidDBInstanceModifications

  * DescribeDBClusters

  * DescribeGlobalClusters

  * DescribeTenantDatabases

  * DescribeDBRecommendations

  * DescribePendingMaintenanceActions

  * DescribeDBProxies

  * DescribeExportTasks

  * DescribeBlueGreenDeployments

  * DescribeOrderableDBInstanceOptions




**Monitoring and alerts:**

  * DescribeAlarms

  * DescribeAlarmsForMetric

  * DescribeEventAggregates

  * ListNotificationEvents

  * DescribeEvents

  * GetCostAndUsage

  * GetCostForecast




**Messaging:**

  * GetSMSAttributes

  * GetSendQuota




**Application discovery:**

  * ListApplications




### Data collection and exfiltration

The Crimson Collective used the gathered information about the infrastructure and proceeded to the data collection stage. The first observed actions were aimed at the Relational Database Service (RDS) that was discovered by the attackers in the previous stage. RDS is designed to simplify the creation, deployment, and management of databases in the cloud. The threat group used an API call ModifyDBInstance to modify the master user password for the database instance. Master user password is an administrator password that would allow attackers to log in to the live database and perform operations like running queries and dumping database tables.

Crimson Collective was further observed performing CreateDBSnapshot API call, which is used to create a snapshot of an RDS. The attacker followed this action with StartExportTask, which they used to export the snapshot of the database to an S3 bucket, preparing it for exfiltration.

The threat group also performed multiple CreateSnapshot actions, creating snapshots of existing EBS volumes. EBS volumes are storage devices that can be attached to EC2 instances — the virtual machines running in the cloud. By creating these snapshots, the threat actor potentially collected valuable data. In the next step, they created their own EC2 instances via RunInstances API call with their own security groups via CreateSecurityGroup. Security groups are virtual firewalls that control inbound and outbound communication with the EC2 instance. No EC2 instance can be created without one, and making them overly permissive allows threat actors to exfiltrate data from EC2 instances easily.

Following this, the threat actor attached previously created snapshots of EBS to the newly created EC2 instance via AttachVolume API call, making the compromised data available through an EC2 instance with permissive security groups. This was all done via the newly created account with AdministratorAccess policy attached to it, which enabled the attackers to manipulate and use all the resources.

The threat group leveraged initially compromised accounts which were privileged enough to access S3 buckets for exfiltration of the data they previously exported and also the data already existing there. For this operation, the attacker used a GetObject API call which allowed them to perform exfiltration of selected objects in S3 buckets.

### Extortion note

In the case of successful exfiltration of data, Crimson Collective sends an extortion note informing the victim about the extent of exfiltrated data. To send this note, the threat group was observed to be leveraging Simple Email Service on the victim’s AWS infrastructure as well as an external email. 

⠀

![CC3.png](https://www.rapid7.com/cdn/images/bltaa6688016ee7896b/68e566b553699424543afd1d/CC3.png)

_Figure 3: Extortion note sent to the victim_

## Conclusion

The Crimson Collective appears to be a newly emerging threat group focusing on data exfiltration and extortion. Rapid7 observed this group operating in AWS environments, using leaked long-term access keys and leveraging overly permissive configurations of IAM entities. Rapid7 recommends avoiding usage of long-term credentials wherever possible and using roles with temporary credentials instead. 

As part of proactive measures, the least privilege principle should be implemented together with monitoring and alerting on suspicious activity. Scanning for secrets in code repositories and restricting access to important resources only to known IP addresses where possible is recommended.

## Rapid7 customers

**InsightIDR and Managed Detection and Response (MDR)** customers have existing detection coverage through Rapid7’s expansive library of detection rules. These detections are deployed and will alert on the behaviors described in this technical analysis.

### Intelligence Hub

Customers leveraging Rapid7’s Intelligence Hub can track the latest developments surrounding the Crimson Collective actor group and associated campaigns/indicators. 

## Indicators of compromise (IOCs)

### Network indicators

45.148.10[.]141

195.201.175[.]210

5.9.108[.]250

3.215.23[.]185

## MITRE TTPs

ATT&CK ID| Name  
---|---  
T1078.004| Valid Accounts: Cloud Accounts  
T1136.003| Create Account: Cloud Account  
T1578.001| Modify Cloud Compute Infrastructure: Create Snapshot  
T1578.002| Modify Cloud Compute Infrastructure: Create Cloud Instance  
T1578.005| Modify Cloud Compute Infrastructure: Modify Cloud Compute Configurations  
T1087.004| Account Discovery: Cloud Account  
T1069.003| Permission Groups Discovery: Cloud Groups  
T1580| Cloud Infrastructure Discovery  
T1526| Cloud Service Discovery  
T1619| Cloud Storage Object Discovery  
T1021.007| Remote Services: Cloud Services  
T1530| Data from Cloud Storage  
T1074.002| Data Staged: Remote Data Staging  
T1213.003| Data from Information Repositories: Code Repositories  
T1567| Exfiltration Over Web Service  
  
## Article tags

  * [Emerging Threats](/blog/tag/emerging-threats/)
  * [Cloud Security](/blog/tag/cloud-security/)
  * [AWS](/blog/tag/aws-cloud-security/)