# Cloud Perimeter Security: Attacks & Detection

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/securing-cloud-perimeters
- **Date :** 2024-04-22

---

The global shift towards cloud computing is undeniable. According to [Statista](https://www.statista.com/statistics/273818/global-revenue-generated-with-cloud-computing-since-2009/), the worldwide public cloud computing market continues to grow and is expected to reach an estimated 679 billion U.S. dollars in 2024. AWS, Azure and Google Cloud services dominate the market and offer businesses scalability and cost-effectiveness. Nevertheless, everything becomes more complicated when it comes to security. 

Сloud providers offer different security features and operate under a shared responsibility model. This means that the provider is responsible for the security "of" the cloud, including the infrastructure, hardware, software, networking, and facilities that run the cloud services. On the other hand, the customer is responsible for security "in" the cloud, which includes securing their data, applications, identity and access management, and client-side encryption. 

As cyber threats are becoming more sophisticated, organizations often seek specialized solutions to enhance their security posture. While AWS, Azure, and Google Cloud provide foundational security capabilities, integrating with the Sekoia SOC platform offers advanced, tailored security operations capabilities.

In this article, we explain different types of attacks on cloud perimeters and focus on how the Sekoia SOC platform helps protect the cloud perimeters. 

## **Types of attacks on cloud perimeters**

Attacks on cloud perimeters aim to exploit vulnerabilities in cloud configurations, applications, and networks to gain unauthorized access, extract sensitive data, or disrupt services. Here are some common types of attacks targeting cloud perimeters:

### **1\. Credential Theft and Misuse**

Attackers may use phishing, brute force attacks, or exploit weak passwords to steal credentials, gaining unauthorized access to cloud resources.

### **2\. API Exploits**

APIs are critical for cloud services operation, and exploiting vulnerabilities in APIs can allow attackers to bypass security measures, access sensitive information, or perform unauthorized actions.

### **3\. Distributed Denial of Service (DDoS) Attacks**

[DDoS attacks](/blog/following-noname05716-ddosia-projects-targets) can overwhelm cloud resources with excessive traffic, making services unavailable to legitimate users. Cloud platforms are high-value targets for such disruptions.

### **4\. Man-in-the-Middle (MitM) Attacks**

Attackers can intercept and alter communications between two parties in a cloud environment, potentially capturing sensitive data transmitted over the network.

### **5\. Misconfiguration Exploitation**

Improperly configured cloud resources, such as storage buckets or databases set to public, can be easily discovered and exploited by attackers to access or leak data.

### **6\. Insider Threats**

Malicious insiders or compromised employee accounts can misuse their access to cloud resources, leading to data theft, vandalism, or other security breaches.

### **7\. Side-Channel Attacks**

These attacks exploit the shared nature of cloud computing resources to extract information from a victim's processes. This is particularly concerning in multi-tenant cloud environments.

### **8\. Malware and Ransomware**

Cloud infrastructure can be infected with malware or ransomware, leading to data theft, encryption, and ransom demands. Attackers might exploit cloud services to spread malware across networks.

### **9\. Zero-Day Exploits**

Attackers may exploit unknown or unpatched vulnerabilities in cloud services or applications. These zero-day exploits are particularly dangerous because there may be no immediate defense available.

### **10\. Cross-Site Scripting (XSS) and SQL Injection**

Cloud-based applications are susceptible to XSS and SQL injection attacks, where attackers inject malicious scripts or queries to steal data or deface web applications.

### **11\. Account Hijacking**

Attackers may hijack cloud service accounts to manipulate data, launch other attacks, or create a base for future attacks by leveraging the cloud resources.

## **Integration of the Sekoia SOC platform with cloud platforms**

Even though cloud providers incorporate built-in security features, Sekoia.io stands out for its simplicity, cost-effectiveness, and flexibility. It extends the native security capabilities of cloud platforms by offering advanced detection rules and multi-source correlation, making it an attractive choice for businesses already using Sekoia for endpoint or network detection.

Sekoia.io can use push modes (HTTPS, Syslog, Relp) and retrieve logs and data from cloud platforms, including Microsoft Azure, Amazon Web Services, Google Cloud, etc. To consume this type of data, as prerequisites, you need to define a location to centralize data coming from your managed services on your cloud provider:

  * AWS S3
  * Azure Event Hub
  * Google Pub/Sub



The Sekoia team has developed multiple integrations that include out-of-the-box connectors, known as triggers, responsible for collecting data. These triggers can be easily configured in [Sekoia playbooks](https://docs.sekoia.com/xdr/features/automate/) with just a few clicks. This versatility enables organizations to centralize their data efficiently and tailor their security measures through configurable triggers in Sekoia.io playbooks.

Setting up Sekoia.io involves defining a centralized data location on your cloud provider and configuring the necessary triggers for data collection. Detailed documentation and support guide you through deploying the data collection architecture, ensuring a smooth integration process. Whether you're leveraging AWS, Azure, or Google Cloud, Sekoia provides end-to-end documentation for setting up and retrieving logs. 

Moreover, our Threat Detection & Research (TDR) team is there to fill our SOC platform with detection rules and CTI. While Sekoia.io wants to be vendor-agnostic, some rules need to be vendor-specific to keep high-quality detection in our platform. This is the case for AWS where the logs are explicit, and our customers’ environments differ a lot depending on the usage.

## **AWS detection engineering insights**

The Sekoia.io TDR team's insights into AWS log sources illuminate the complexity of [securing AWS environments](https://www.sekoia.com/blog/aws-detection-engineering). CloudTrail, AWS Flow Logs, and GuardDuty are identified as the primary log sources for monitoring and detecting threats within AWS. CloudTrail is essential for capturing logs across different AWS services, but its voluminous data requires strategic filtering to focus on security-relevant events. AWS Flow Logs and GuardDuty offer additional layers of insight, with the former providing network flow data and the latter specializing in threat detection.

For AWS Flow Logs, the challenge lies in sifting through massive amounts of netflow data without impacting performance. Meanwhile, GuardDuty's specialized threat detection capabilities complement CloudTrail and Flow Logs, offering a more focused approach to identifying AWS-related threats. 

### **Fortifying against threat actors: Important rules and events**

Sekoia.io offers plenty of rules to detect threat actors targeting cloud service providers. For example, the **AWS GuardDuty High Severity Alert** canindicate that an EC2 instance or a _set of IAM user sign-in credentials is compromised and used for unauthorized purposes_. However, the **AWS GuardDuty High Severity Alert** can be caused by other reasons as well. 

The **AWS CloudTrail EC2 Startup Script Changed** rule detects _changes to the EC2 instance startup script_. In this case, the shell script may be executed as root/SYSTEM every time the specific instances are booted up.

To detect a c _ompromised access key_ , Sekoia.io relies on the **AttachUserPolicy** event. The **AWSCompromisedKeyQuarantineV2** parameter in the Policy allows the detection of the compromised access key. Although AWS limits key access to remove most of the rights, making the key unusable for an attacker, the Sekoia SOC platform fires alerts on this event and enables quick actions. 

Attackers may also leverage different approaches to _establish persistence on a tenant_. One common way they follow is creating a KeyPair for a highly privileged user to allow SSH connections. An attacker can also use that specifically to connect to an EC2 instance. To detect such threats, it’s important to analyze the following events: CreateKeyPair, SendSSHPublicKey,SendSerialConsoleSSHPublicKey. 

Also, to _establish persistence on a tenant,_ attackers can create or update an identity provider, a SAML, or an OpenID. These actions are also logged, and several events can be raised, such as AddClientIDToOpenIDConnectProvider, CreateOpenIDConnectProvider, CreateSAMLProvider, and UpdateSAMLProvider, to name a few. 

Moreover, an attacker can cover his tracks by deleting them, which also raises events such as DeleteSAMLProvider. There are many other ways to establish persistence like creating new users or changing passwords, evade defense by disabling logging or security tools. For instance, attackers can disable GuardDuty, CloudTrail and FlowLogs with the correct rights for the tenant. Depending on how stealthy they want to be, they could also update a trail to remove just a specific logging capability. With the Sekoia SOC platform, it’s possible to leverage [built-in detection rules](https://docs.sekoia.com/xdr/features/detect/built_in_detection_rules/), take the right actions, and neutralize attacks. 

Sekoia's strategy involves leveraging log sources and in-depth event analysis to build sophisticated detection rules and integrate CTI for a comprehensive defense against cloud-based threats. This approach enhances AWS security and offers valuable lessons for securing cloud environments across different platforms.

### **Wrapping up**

As cloud computing continues to prosper, the importance of robust security measures cannot be overstated. The shared responsibility model underlines the need for collaboration between providers and customers in safeguarding data and applications. Through its advanced integrations and security capabilities, Sekoia.io offers a comprehensive solution to protect against a wide array of threats, ensuring that organizations can leverage the cloud's benefits without compromising security. Moreover, Sekoia.io offers reliable tools to automate cybersecurity operations within the cloud.