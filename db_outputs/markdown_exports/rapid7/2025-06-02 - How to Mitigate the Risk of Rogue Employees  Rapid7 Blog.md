# How to Mitigate the Risk of Rogue Employees | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2025/01/16/perfect-fit-or-business-threat-how-to-mitigate-the-risk-of-rogue-employees/
- **Date :** 2025-06-02

---

Rogue employees present significant financial and cybersecurity risks to organizations. Rapid7 threat researchers and penetration testers are actively observing how malicious actors exploit hiring pipelines to infiltrate businesses. This blog highlights real-world tactics, including:

  * **Insider Reconnaissance:** Rogue applicants leveraging interviews to map office layouts, identify vulnerable devices, and even plant malware during site visits.
  * **Tech Tricks:** The use of deepfake technology, AI-generated photos, and VoIP to fake identities, bypass background checks, and mask locations.
  * **North Korean Operations:** State-sponsored actors posing as remote IT workers with fake resumes and stolen identities to fund illicit activities like missile development.
  * **Hiring Weaknesses:** Gaps in hiring processes—such as 43% of organizations skipping background checks—leaving businesses vulnerable to exploitation.



Read on to discover how to fortify your hiring and onboarding practices against this business risk.

## Understanding the threat

Rogue employees have long been an issue for hiring departments. The [Occupational Fraud 2024: A Report to the Nations](https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf) study reported worldwide losses of more than $3.1 billion from 1,921 fraud cases. Other studies suggest that a typical business may lose as much as 5% of their annual revenue due to this problem. Sadly, the days of “only” having to worry about employees who show up late every day, or tell a few small tales on their work history record, are but a distant memory.

While organizations have been aware of the broad risk from bogus hires for some years, many are playing catch-up with hitherto unknown cybersecurity implications, particularly when state-sponsored actors are at the helm. For example, the FBI issued warnings about remote North Korean workers [sending funds to the regime back in 2022](https://www.theguardian.com/world/2022/may/17/dont-accidentally-hire-a-north-korean-hacker-fbi-warns), and estimated the number of fake North Korean workers to be in the thousands. These workers generate revenue for ballistic missile development, and according to a [2022 advisory](https://ofac.treasury.gov/media/923126/download?inline) “...may share access to virtual infrastructure, facilitate sales of data stolen by DPRK cyber actors, or assist with the DPRK’s money laundering and virtual currency transfers.”

Multiple examples of other DPRK-centric malicious employment fraud have gone public over the past year. Security education firm KnowBe4 highlighted the [detection and removal of a North Korean worker](https://blog.knowbe4.com/how-a-north-korean-fake-it-worker-tried-to-infiltrate-us), who’d bypassed various checks at the hiring stage and attempted to deploy malware. In October 2024, an unnamed firm [revealed a similar ploy](https://www.bbc.co.uk/news/articles/ce8vedz4yk7o) where a remote IT worker faked employment history, downloaded data, and issued a ransom demand. A few months prior to this, a Tennessee resident was arrested for his [alleged involvement](https://www.justice.gov/opa/pr/justice-department-disrupts-north-korean-remote-it-worker-fraud-schemes-through-charges-and) in a DPRK-centric laptop farm involving stolen identities and software installed without permission.

Even without North Korean involvement, there are many other ways rogue hires can cause security issues across a business. [What else lies in wait for the unwary hiring department](https://www.reddit.com/r/recruiting/comments/1ezcz1o/youve_heard_of_scam_jobs_but_what_about_scam/)? More importantly, how can your organization combat these threats?

## Rogue hire archetypes

Rogue hires fall into certain categories. Some are potentially more damaging to a business than others, with some overlap in terms of tactics and objectives. If you run into any of the below, then this is what you can expect them to be doing.

  * **Malicious applicants** : They may be [working alone](https://www.lewissilkin.com/insights/2020/04/01/morrisons-not-liable-for-misuse-of-personal-data-by-rogue-employee), or as [part of a team](https://techcrunch.com/2020/09/23/shopify-data-merchant-breach/) to steal financial or customer data. The incentive may be financial or tied to data exfiltration, but the attack’s starting point could involve phishing, malware deployment, or BEC (business email compromise). They may intend to continue as a rogue employee if hired, or plan to compromise a business at the physical interview stage and never be seen again.
  * **State-sponsored threat actors** : These are commonly encountered as [freelance workers from North Korea](https://www.darkreading.com/vulnerabilities-threats/doj-targets-north-koreas-widespread-it-freelance-scam-operation) (albeit not exclusively), targeting positions in general IT support, mobile development, virtual currency exchanges, and firmware development across the US, Europe, and East Asia. They often present themselves as being Chinese, South Korean, and Japanese, while making use of forged or stolen identity documents. The FBI believes that most engage in non-malicious IT work, though some make use of privileged systems access to enable malicious cyber intrusions.
  * **Proxy employees** : They receive one-off or continued payments from a real would-be employee in return for fielding the interviews. The proxy may also take on work-related tasks on behalf of the employee assuming the latter is ultimately hired. The FBI has [previously warned](https://mashable.com/article/deepfake-job-interviews-fbi) that deepfake technology is often used for multiple remote work scams, with available positions granting access to “...customer PII (personal identifying information), financial data, corporate IT databases and/or proprietary information.”



## The malicious applicant game plan

Malicious applicants may operate alone, but have the potential to be backed by groups or nations with access to a wide range of resources denied to more common fraudsters. These resources could include fake or stolen identity documents, or unknown malware and vulnerabilities. Their interests are frequently financial, but may veer into data exfiltration should the opportunity arise.

Some rogue hires may not intend to take on employment; instead, the interview is used as a pretext for more direct reconnaissance and malware deployment. To illustrate how a typical malicious applicant could exploit an interview process, a [Rapid7 penetration tester](/services/security-consulting/penetration-testing-services/) shared their experience of a workplace infiltration assignment that they participated in:

_**“Standard OSINT techniques revealed several open interviews available while I was going to be on location. I typically review job postings for technology stacks the organization uses, in case I want to fall back on phishing campaigns. I also vet for potentially vulnerable endpoint software which may be in use. They did at least have a sign-in sheet and a guard to lead me to the interview.”**_

It’s worth noting that a penetration tester's objectives and methods will differ from more targeted, state-sponsored attempts to compromise organizations for specific espionage or other goals. However, there will be some overlap across different groups and individuals.

_**“I was taken through a variety of rooms and offices, granting me a handy mental map of layout, equipment, possible locations of important devices like servers or network access. During the interview, I asked if I could visit the bathroom and was permitted to walk freely in the office. An unattended logged-in device could be susceptible to malware on a USB stick; I might find physical employee directories, or post-it note passwords. I’m wearing office clothes. If there’s no lanyard requirement enforced, who would suspect anything?”**_

A networked printer could be a launchpad for [malware outbreaks or firmware manipulation](https://www.itpro.com/security/the-humble-printer-is-still-a-leading-cause-of-cyber-attacks). An unguarded stack of expense paper could help to pave the way for BEC once the interviewee has left the premises.

Seemingly innocent interview questions about standard business operations can lead to password reset phishing campaigns, designed to resemble familiar email login pages and MFA (multi-factor authentication) systems. From here, the attacker can use compromised accounts to perform social engineering, or gain deeper access into the network.  
  
Fictitious HR workers can be deployed to send malware-laden hiring or policy documents via email domains imitating the real thing. There is a very real possibility in this scenario of long-term compromise and data exfiltration. Should the attacker decide to escalate further, they may turn to ransomware and double extortion, leading to blackmail and public data exposure.

Now that we’ve highlighted some of the worst-case scenarios from an interview gone wrong, we’ll explore in detail where the hiring pipeline is at its most exposed.

## The riskiest stages of hiring

Assuming you’ve posted your job description, the key stages of ingress for bogus hires are now exposed to the wild. The three main areas of interaction are:

  * Screening and shortlisting.
  * The interview(s).
  * Onboarding of successful hires.



Providing barriers to entry at each stage will increase the likelihood of catching rogue personnel.

Businesses most commonly search an [applicant’s employment history, perform criminal record checks, and verify their education history](https://www.acfe.com/-/media/files/acfe/pdfs/rttn/2024/2024-report-to-the-nations.pdf) [PDF, page 48]. Checks on social media, directorship searches, and specialist vetting are all less likely. However, an astonishing 43% of organizations surveyed said no background checks were run on perpetrators prior to hiring.

This piecemeal approach to hiring gives opportunists a direct line to your organization’s most valuable assets. Those fake HR workers mentioned earlier could just as easily have been bogus IT administrators, responsible for rolling your patches out to users of your software. Now you’re a compromised third-party vendor, enabling the flow of a supply chain attack to multiple customers. They, too, could be at risk from further network ingress, malware, and data exfiltration—all because you failed to perform any background checks on a potential hire.   
  
Beyond this, most businesses do not generally vet staff once employed. This is why precautions are still advisable during initial hire or onboarding. KnowBe4 issuing a [limited access laptop](https://blog.knowbe4.com/north-korean-fake-it-worker-faq) to the North Korean IT hire is one reason for the would-be attacker’s lack of success.

## Screening and shortlisting

What they want to do:

  * Present a convincing and comprehensive overview of experience and work history.
  * Spread a veneer of credibility on the resume that dissuades further investigation.



## What you need to do:

  * **Use an applicant tracking system (ATS)**. An ATS is invaluable for weeding out potential fakes. They’re very good at [finding reused names, emails, or even phone numbers across multiple profiles](https://www.reddit.com/r/recruiting/comments/1bffeiu/comment/kv081n3/). This is especially useful considering a typical job post can receive hundreds of applications an hour on LinkedIn alone.  

  * **Third-party background checks**. Many services offer to take on the responsibility of background checks from the employer, with some all-in-one solutions offering 100+ types of background check.  
  
**Explore LinkedIn data**. If you suspect the candidate’s photograph is a stock image or AI generated, reverse image search and AI checking tools can help. In the KnowBe4 incident, the fake employee used AI to alter a stock photograph. Note that many other tricks exist to bypass checks, such as flipping the photograph horizontally or altering the colors.



  
You should also consider the authenticity of the profile. Has it been created very recently but boasts many years of work? Does the candidate claim 5 to 10 years of experience despite having few or no reputable contacts in the industry you work in? Are recommendations from co-workers entirely absent?

## The interview

In an ideal situation for fraud, fake employees want to:

  * Stay off camera.
  * Answer your questions via a third-party through headset or offscreen.
  * Use VoIP to mask their real location.
  * Avoid discussing anything related to their background.



The interview: what you need to do  


  * **Create phone and video rules**. Insist on a VoIP-free phone call during the hiring process, whether landline or mobile. This, alongside other data gathered, can help you to decide if a candidate really is located in France, Belgium, or Scotland. For web calls, make camera interaction mandatory. Ask for blurred backgrounds (or similar features) to be disabled so you can see where the candidate really is.  
  
Using cameras has many additional benefits, such as impeding the flow of a [proxy hire](https://www.reddit.com/r/jobs/comments/17lwsgt/remote_job_through_proxies/) (someone who is [paid to take interviews](https://www.reddit.com/r/developersIndia/comments/175yrsk/comment/k4k8kcp/) on the potential employee’s behalf.) It’s much more difficult for fraudsters to [take instructions from a headset](https://www.reddit.com/r/recruiting/comments/1bffeiu/comment/kv2797k/) or even [mime](https://www.reddit.com/r/recruiting/comments/1ezcz1o/comment/ljjng3r/)(!) if you can see the candidate at all times. Being able to see candidates means there’s also less chance of [totally different people showing up to subsequent interviews](https://www.reddit.com/r/recruiting/comments/1f4dpjn/comment/lko0noy/).  
  

  * **Build a consistent picture**. Are you permitted to use conferencing tools which allow you to view/log IP addresses or other relevant system information? Fraudsters (particularly proxy hires) use multiple people at different stages of the interview often separated by large distances. These small digital pointers could build up a very different picture of who you think you’re dealing with.  
  

  * **Dig into background details**. Select 2 or 3 pieces of information from a resume. This could be their hometown, a previous employer, or perhaps their area of expertise. Ask about what it was like growing up in the city they mention, or places of interest they enjoy in their hometown. Faltering answers may be a big clue.



  
If multiple interviews are planned, record these answers and have subsequent interviewers reuse a few questions. If the candidate is making it up as they go, then the story will quickly fall to pieces.

## Onboarding

Even if a rogue has bypassed screening and interviews, you still have a chance to catch them in the act. Here’s what you can do at this stage:

  * Restricting laptop or equipment pickup to a depot where valid identification is required will [help prevent it from falling into the wrong hands](https://blog.knowbe4.com/north-korean-fake-it-worker-faq).
  * Ensure the device is running all required security tools, does not grant admin permissions, and provides access only to work-essential tools such as email, comms, and day-to-day necessities. The device should be “bare-bones” and not come with company data stored locally on the system.
  * Do not allow the new hire any facility to upload files outside of necessities such as old payslips, ID, proof of address/utility bills, and tax details.
  * If you use tools like Slack or Microsoft Teams, ensure the new hire is restricted from accessing channels they don’t need.



Someone who successfully passes the 3 interview steps above has a wealth of options at their disposal. They might immediately try to compromise systems or data before being discovered. Alternatively, they may spend weeks or months exfiltrating data and social engineering other employees. Initial knowledge of common business practices for laptops and remote security, system updates, and authentication can potentially make it easier for them to try and bypass measures in place. It’s a much better idea to not let them get anywhere near this stage in the first place.

## Hire with confidence

Rogue workers of all types are a very real threat to your data security and business revenue. From security organizations to [blockchain firms](https://www.coindesk.com/tech/2024/10/02/how-north-korea-infiltrated-the-crypto-industry), anyone is potentially at risk from a bad hire. Adapting the above hiring practices and combining them with a defense-in-depth approach will help you proactively and confidently deal with these threats to your network, and the people using it.  


  


## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)