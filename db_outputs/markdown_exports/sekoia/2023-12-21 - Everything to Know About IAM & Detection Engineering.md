# Everything to Know About IAM & Detection Engineering

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/iam-detection-engineering
- **Date :** 2023-12-21

---

## Introduction 

In the ever-changing cybersecurity landscape, [Identity and Access Management (IAM)](/glossary/iam) stands as the cornerstone of an organisation's digital asset protection. IAM solutions play an essential role in managing user identities, controlling access to resources and ensuring compliance. As the digital threat landscape is constantly increasing in complexity, the need for visibility of IAM events has become paramount to detect attacks as early as possible before impact. This blog post explores the importance of IAM event detection, explaining why it is essential in today's cybersecurity world and how it can enable organisations to proactively protect their systems, data and sensitive information.

## Did you say “IAM” ?

Frequently seen as a single sign-on (SSO) solution, IAM enables users to log in once to access all the applications to which they are entitled. However, IAM goes further than SSO, since it also acts as a universal directory, simplifying the management of accounts from various sources, while supervising access rights beyond the authentication stage.

In operational terms, [IAM facilitates identity and access management](/glossary/iam) by providing IT administrators with the tools they need to efficiently and securely manage users' digital identities and access privileges. It grants administrators the ability to define and modify user roles, track and report on user activity, and enforce regulatory and corporate compliance policies to protect data security and privacy.

## Weaknesses

While IAM-based technologies have numerous advantages, they still have some weaknesses. As a cloud-based solution, it can be exposed to attacks on authentication, such as brute force or session cookie reuse attacks. For example, in October 2023, attackers managed to retrieve session cookies from Okta customers, exploiting this data to access the dashboard of the customers concerned.

Moreover data centralisation makes identity and access management (IAM) solutions attractive targets for attackers. A successful IAM access could open the door to interconnected applications. Nevertheless, as evidenced by the Okta incident, a robust access policy can limit users to their specific authorisations, preventing victims from experiencing lateral movements to other IAM-related applications, as already reported by [1Password](https://blog.1password.com/files/okta-incident/okta-incident-report.pdf).

## How does it work?

Basically an IAM solution works within following steps:

![How an IAM solution works](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5efc5553634ac94f15e_6a92a32d6568d7e2b408e53b_6a2a7c7fe2d8f7e583ca9283.webp)

How an IAM solution works

In the next part of this blog post, we will look at how Sekoia set up detection rules for Okta and JumpCloud technologies.

‍

## Okta and JumpCloud: the big picture

Okta and JumpCloud are two major IAM solutions, offering powerful features for organisation’s identity management.

Okta stands out for its user-centric approach, offering a seamless, fluid experience. This IAM solution offers seamless application integration and single sign-on (SSO) to simplify access to resources. Okta also focuses on access management for cloud environments, facilitating the transition to cloud-based architectures.

JumpCloud stands out for its serverless, cloud-oriented approach. This IAM solution offers centralised identity management in a variety of environments, whether on-premises, in the cloud or on devices. JumpCloud is particularly suited to organisations seeking to effectively manage access to a diverse range of resources, from applications to operating systems.

Both Okta and JumpCloud offer a user-friendly interface, giving users access to a centralised dashboard, from which they can find and launch their applications. These user portals simplify the experience by providing easy, unified access to the resources needed.

On the administrator side, both solutions also offer comprehensive admin panels. These admin interfaces enable administrators to configure security policies, manage users and monitor the environment centrally. They offer control over permissions, security settings and specific configurations, providing robust management of the entire IAM system.

### Key differences

Although both solutions aim to simplify identity and access management, there are some key differences worth highlighting. Okta focuses on the user experience, offering seamless application integration, while JumpCloud stands out for its versatility, adapting to heterogeneous environments.

Okta specialises in providing a complete solution for cloud-based enterprises, while JumpCloud offers enhanced flexibility, suitable for both cloud and on-premises environments.

### System Log

Okta and JumpCloud log the majority of actions performed by users in a rather clear way. Both IAMs provide detailed logs of every action performed on the user portal, covering authentication processes as well as policy enforcement. Each log records the action taken, the user concerned, any policies involved, and the result of the action (success or failure). This wealth of information is essential for an in-depth understanding of events, facilitating the detection of malicious behaviour.

At Sekoia, we've integrated these technologies into [our SOC platform](/glossary/soc) so that our customers can find their events. Here is an example of my administrator who connects to the administration panel for both IAMs : 

![Integration of IAM solutions \(Okta and JumpCloud\) into the "Sekoia" SOC platform](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5efc5553634ac94f15b_6a92a32edae089660dfc7d40_6a2a7c7fe2d8f7e583ca9286.webp)

Integration of IAM solutions (Okta and JumpCloud) into the &quot;Sekoia&quot; SOC platform

We can see that much information is contained in fields and it will help us to create detection rules as precise as it can be.

## Detection Mechanism

The basic principles of threat detection encompass the recognition of unusual behaviour patterns and the constant monitoring of [indicators of compromise (IoCs)](/glossary/ioc). These elements work together towards the overall goal of prevention, early detection and rapid response to threats, to ensure proactive protection.

At Sekoia we already cover a wide range of IoCs thanks to our [CTI feed](/glossary/cti), so we're going to focus the search for detection rules on behavioural analysis. Here we'll look at how we're trying to cover the techniques we've identified in the mitre attack matrix in relation to what we find in IAM technology.

## Identity management

Identity management within an IAM system is crucial for preserving the security and confidentiality of information. This essential component aims to effectively administer user access to sensitive data and resources. Here are a few key points relating to identity management in an IAM system:

### 1\. Creating and managing user accounts

Identity management begins with the creation and management of user accounts. IAM administrators are responsible for assigning unique identifiers to each user, as well as administering the associated access rights. This ensures that each individual only has the authorizations needed to perform his or her tasks.

Sekoia has created a set of rules covering basic action behaviour that an attacker might try to perform on the user account. This ranges from the creation of user accounts to their deletion or deactivation. 

### 2\. Granting and revoking privileges

The user's access needs may evolve over time. Identity management therefore includes the initial allocation of privileges, as well as their adjustment according to the user's responsibilities. Similarly, prompt revocation of privileges for users who change roles or leave the company is crucial for minimising security risks. However, these are administration functions which, in the wrong hands, can lead to very powerful attack actions such as privilege elevation. Fortunately, these actions are always logged and we can detect them.

## Access Management

### 1\. Authentication and verification mechanisms

Access management requires robust authentication mechanisms, including the use of secure passwords, two-factor authentication, or other advanced [authentication methods](/blog/userauthenticationmethod-microsoft-365-decode). These measures are designed to ensure that only authorised people can access protected resources. Consequently, this is crucial to monitor when a user attempts to bypass these authentication or to enforce them.

Here is an example of detecting brute force behaviour on JumpCloud using a [Sigma correlation rule](https://docs.sekoia.com/xdr/features/detect/sigma/#correlation): 

`correlation: |  
name: login_failed  
detection:  
selection:  
action.outcome: 'failure'  
event.category: 'authentication'  
event.action: 'user_login_attempt'  
condition: selection  
---  
name: login_success  
detection:  
selection:  
action.outcome: 'success'  
event.category: 'authentication'  
event.action: 'user_login_attempt'  
condition: selection  
---  
name: many_failed_logins  
action: correlation  
type: event_count  
rule: login_failed  
group-by: source.user.name  
timespan: 5m  
condition:  
gte: 10  
---  
action: correlation  
type: temporal  
rule:  
- many_failed_logins  
- login_success  
group-by: source.user.name  
timespan: 5m  
ordered: true  
`

Sekoia also provides other rules to detect malicious authentication such as MFA brute force or spamming password reset for exemple.

### 2\. Session cookies

Session cookies are a set of temporary data stored in a single browser file on the user's system when visiting a website. They are crucial for maintaining session status and ensuring a smooth user experience. In the context of IAM, they are essential for secure interaction management, maintaining authentication and storing rights information. However, an attacker who gets hold of a session cookie can then gain access to an account without authenticating, bypassing the login, password and MFA steps. This is known as a session cookie reuse attack.

### 3\. API tokens

API Tokens play a central role in Identity and Access Management (IAM), providing a secure method of authorising and authenticating applications, services or users within integrations.

API tokens serve as an authentication and authorization mechanism when accessing resources or services. They ensure that only authorised entities can interact with IAM systems, reinforcing the security of exchanges. Keeping an eye on how these are handled is essential, given their importance in the system especially their creation and revocation.

### 4\. Policies

Security policies are a set of rules and guidelines that define authorizations and access restrictions for users, applications and services within an IT environment. They specify the permissions granted to each user or group of users. They also define roles with specific sets of permissions, simplifying authorization management. Every manipulation of these permissions needs to be monitored, as attackers can use them to access unauthorized resources.

Here is a straightforward example of detection policy modified on Okta: 

`detection:  
action:  
event.action:  
- "policy.lifecycle.update"  
- "policy.lifecycle.delete"  
condition: action  
`

This basic rule is especially useful for companies with a minimum of control over their Information System. In fact, it can generate numerous false positives when administrators create policies. That's why Sekoia lets you filter rules on many fields.

### 5\. Applications Access

IAMs enable centralised management of application access. Users can be authenticated centrally, and access rights are managed consistently, independently of specific applications. Access rights are defined at application integration, and operate in conjunction with security policies and user groups.

Here is an example of detection for which a user tries to access several applications in a short space of time. This activity could suggest that potential intruder logged into their account and tried to retrieve as much information as possible: 

`correlation: |  
name: app_launched  
detection:  
selection:  
event.action: "user.authentication.sso"  
okta.system.target.type : "AppInstance"  
condition: selection  
---  
action: correlation  
type: value_count  
rule: app_launched  
group-by: okta.system.actor.alternate_id  
timespan: 5m  
field: okta.system.target.alternateId  
condition:  
gte: 6  
`

## IAM detection rules: revealing efficiency and strengthening security

It is essential to take the time to reflect on the effectiveness of these simple but crucial detection rules. These rules focus on identifying fundamental behaviours, often performed by administrators. While it is necessary to recognize the possibility of false positives, it is equally vital to acknowledge that attacker's actions in these scenarios can be highly destructive and pose a serious threat to the system.

The aim is to strike a balance between effectively identifying potential threats and minimising false positives. An effective approach to this evaluation is to use test tools, such as [Dorothy](https://github.com/elastic/dorothy), in a simulated environment. This method provides a concrete validation of the rules' performance in the face of suspicious behaviour.

![Dorothy is a free and open source tool that offers various modules simulating the actions of an attacker in an Okta environment, aligned with MITRE ATT&CK tactics](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaab625de070f3e0b74c74a_Dorothy.webp)

Dorothy is a free and open source tool that offers various modules simulating the actions of an attacker in an Okta environment, aligned with MITRE ATT&CK tactics

Dorothy is a free and open source tool that offers various modules simulating the actions of an attacker in an Okta environment, aligned with MITRE ATT&CK tactics. It aims at helping defenders evaluate their visibility and security controls. It does not allow initial access or privilege escalation, but it provides many commands related to Discovery, Defense Evasion, Persistence and Impact : The use of Dorothy requires a valid Okta API token with administrative roles. The user-friendly shell interface, accompanied by context-sensitive help, facilitates navigation and intrusion simulation. Additional features include configuration profiles and detailed logging with event indexing in Elasticsearch, ensuring full traceability of actions performed with Dorothy. The following figure shows how Sekoia rules matched when played a Dorothy scenario performing discovery and defense evasion activities on an Okta tenant :

![how Sekoia rules matched when played a Dorothy scenario](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5efc5553634ac94f161_6a92a32f9d3b9ef4d8bbbcc5_6a2a7c7fe2d8f7e583ca9289.webp)

How Sekoia rules matched when played a Dorothy scenario

Our thinking goes beyond simple technical validation, encompassing aspects such as the accuracy, responsiveness and adaptability of the rules. By testing these rules in a controlled environment, we strive to offer a practical perspective on how they work. It was with this approach that we established our first rules that can be applied and adapted to IAM environments.

## Conclusion

Identity and access management is crucial to cybersecurity, providing essential solutions to protect digital assets. While solutions such as Okta and JumpCloud have their advantages, weaknesses persist, such as the exploitation of cookies in the Okta incident. Implementing robust access policies remains essential. Sekoia integrates Okta and JumpCloud into its SOC platform, demonstrating its commitment to full visibility of IAM events for proactive measures. This blog post has presented techniques used by attackers, accompanied by detection rules active in our production environment. Sekoia hopes that this information, together with the rules available on our public GitHub repository, will benefit many companies.