# How eCriminals Impersonate School Staff to Steal Paychecks

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/ecriminals-use-payroll-bec-to-steal-paychecks/
- **Date :** September 07, 2023

---

# eCriminals Share Ways to Impersonate School Staff to Steal Paychecks

September 07, 2023

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


CrowdStrike Counter Adversary Operations monitors for and attempts to disrupt eCrime threat actors across a broad spectrum of malicious activity, ranging from sophisticated ransomware campaigns to simpler but often highly effective forms of fraud.

From October 2022 through the summer of 2023, CrowdStrike observed a significant and steady increase in various eCrime threat actors discussing conducting payroll [business email compromise (BEC)](/en-us/cybersecurity-101/threat-intelligence/business-email-compromise-bec/), including specific mentions of targeting U.S.-based private schools. Payroll BEC is a shorter, simpler fraud technique than traditional BEC. This technique involves threat actors contacting an organization's payroll department while impersonating an employee in an effort to change direct deposit information to an account controlled by the threat actor.

As the U.S. school year gets underway, human resources and finance personnel in the academic sector should be aware of the warning signs of payroll BEC campaigns, as well as the methods to mitigate this simple yet effective form of fraud.

## Anatomy of a Payroll BEC Campaign

eCrime actors share payroll BEC tutorials in Telegram channels and on clear or darknet forums. Below are examples of such tutorials, which detail the complete payroll BEC process:

  1. Research and Target Identification
     1. The threat actor suggests using popular search engines to obtain an organization’s staff directory and identify its payroll officer. They recommend targeting the U.S. academic sector due to the vast amount of schools in the U.S.
     2. In the same staff directory, threat actors can obtain names and email addresses associated with various school employees that they could impersonate.
  2. Employee Impersonation
     1. In order to masquerade as an organization’s employee, the threat actor recommends readers use a webmail account and create an “identity” matching the employee they intend to impersonate.
     2. By using the impersonated employee’s name and email address, but placing the threat actor-controlled email address in the “reply to” header, the actor hopes to trick the recipient into believing replies would go directly to the employee.
  3. Target Interaction
     1. The tutorial shares a template with aspiring payroll BEC conductors, recommending they greet the payroll officer and write the following: “I have recently changed my banks, can you update my payroll direct deposit information? Previous account on record will be inactive a few days before next pay day.”
  4. Change of Direct Deposit Information 
     1. Payroll officers may require information from the threat actor in order to change the direct deposit information. This may include an account number, routing number and type of account (checking or savings), or a voided check with the routing and account number. The tutorial recommends that threat actors find sample checks online and edit them in order to satisfy the officer’s request.
  5. Cashing Out
     1. The tutorial suggests threat actors can “use any bank or prepaid to receive salary, there no exceptions.” However, other actors state the name on the receiving account must match the name of the impersonated employee.
     2. If needed, payroll actors can partner with other criminal ecosystem members who provide either personally identifiable information (PII) lookup services — enabling a threat actor to obtain the necessary PII to create an account under the impersonated employee’s name — or offer to create accounts in an individual’s name.



[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2023/09/BEC.png)](/content/dam/crowdstrike/www/en-us/wp/2023/09/BEC.png)Figure 1. Anatomy of a successful payroll BEC campaign (click to enlarge)

## Methods to Mitigate the Risk of Payroll BEC Social Engineering

Organizations looking to reduce their payroll department’s likelihood of diverting employee paychecks to a threat actor may consider implementing the following procedures.

First, payroll officers should examine the “Reply-To” headers of incoming emails regarding direct deposit changes to confirm that responses to the email would only go to the employee's internal corporate email address. Given payroll BEC’s reliance on spoofing legitimate email addresses, this step can help confirm whether a payroll officer is interacting with the legitimate employee.

Second, payroll officers or human resources employees should be wary of email bodies that are nearly identical to the sample email wording in this blog. Due to the popularity of prominent payroll BEC tutorials, CrowdStrike assesses with high confidence that threat actors have almost certainly used phrases such as “I have recently changed my banks” or “Previous account on record will be inactive a few days before next pay day” in numerous campaigns, with threat actors copying the text exactly. Therefore, organizations can implement spam filters for emails in which the body of the text matches these phrases.

Third, due to threat actors’ reliance on requesting payroll diversion via email, organizations that use a separate platform to conduct all payroll operations are inherently more protected from this type of fraud. A threat actor would need to obtain an employee’s credentials (likely through a [phishing campaign](/en-us/cybersecurity-101/social-engineering/phishing-attack/)) and potentially defeat or subvert [multifactor authentication (MFA)](/en-us/cybersecurity-101/identity-protection/multifactor-authentication-mfa/) to log into this type of payroll platform. Therefore, unless there’s a vulnerability within the payroll platform, a threat actor attempting a typical payroll BEC campaign would likely fail.

Tune in to our [Adversary Universe podcast](/en-us/resources/adversary-universe-podcast/), **Ransomware Actors Mark Their Calendars for Back-to-School** , for more about spikes in eCrime activity when students and teachers start the school year.

#### Additional Resources

  * _Learn more about today’s adversaries and how to combat them at Fal.Con 2023, the cybersecurity industry’s most anticipated annual event.[ Register now](/en-us/events/fal-con/) and meet us in Las Vegas, Sept. 18-21._
  * _See CrowdStrike Counter Adversary Operations in action in this[ 3-minute demo](/en-us/resources/videos/crowdstrike-counter-adversary-operations-demo/)._
  * _Learn about the latest threats in[ Nowhere to Hide: CrowdStrike 2023 Threat Hunting Report](/en-us/resources/reports/threat-hunting-report/)._
  * _Explore the adversaries that may be targeting your region or business sector in the[ CrowdStrike Adversary Universe](/en-us/adversaries/)._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)