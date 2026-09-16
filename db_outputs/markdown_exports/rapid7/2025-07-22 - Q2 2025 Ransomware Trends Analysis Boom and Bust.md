# Q2 2025 Ransomware Trends Analysis: Boom and Bust

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/q2-2025-ransomware-trends-analysis-boom-and-bust/
- **Date :** 2025-07-22

---

“Tumultous times” would be an accurate summary of Q2 2025 where [ransomware](/fundamentals/what-is-ransomware/) threat actors are concerned. Rapid7’s internal and publicly-available data analysis reveals a dynamic environment where major players come and go, newer groups work their way up the heavy-hitters ladder, and threat actors jostle for top dog status. Plus, there’s law enforcement action thrown in there for good measure.

This blog post highlights the key changes we saw represented in the data: shifting alliances, the disappearing act of a dominant force, and how this vanishing trick has led to a major redistribution of ransomware operations.

## At a glance

Q2 2025 features many of the threat actors [Rapid7 observed in Q1](https://www.rapid7.com/blog/post/2025/04/08/2025-ransomware-business-as-usual-business-is-booming/), with the top four leak site post groups quite a ways out in front of the rest. Qilin leads the pack by some distance, with SafePay and Akira in second place, and Play in third position. Lynx and INC Ransom lead the charge in the lower half of the chart, with DragonForce making its first appearance of the year alongside top 10 newcomers such as double extortionists NightSpire.

In Q1 2025, there were 76 active ransomware groups. Out of those, 17 groups became inactive in Q2 2025, meaning they had no recorded leak posts in April, May, or June. These include (but are not limited to): 8base, BianLian, BlackBasta, Cactus, RansomExx, DarkVault, Zerolockersec, and CrazyHunter Team. 

There were 65 ransomware groups actively attacking in Q2 2025. While this represents a 14.47% decrease from the previous quarter, our data for the first half of 2025 shows an overall count of 96 unique groups — a 41.18% increase over the 68 we saw in 1H 2024.

![April-June-2025-Ransomware-Stats-Graphic.jpg](https://www.rapid7.com/cdn/images/bltab8e5a554a573c36/687f91b5db1c69cb1d45832e/April-June-2025-Ransomware-Stats-Graphic.jpg)

New ransomware groups active since the start of Q2 include (but are not limited to): KaWa4096, Warlock, Devman, Nova, and Dire Wolf, with 11 net new groups in Q2 2025 in total.

  
Notably, power player RansomHub — the most prolific operator [we observed](https://www.rapid7.com/blog/post/2025/01/27/the-2024-ransomware-landscape-looking-back-on-another-painful-year/) in 2024, and leading our Q1 2025 top 10 — ceased operations completely at the beginning of April, with the group’s infrastructure dropping offline. Affiliates primarily moved to other Ransomware-as-a-Service (RaaS) offerings, such as DragonForce and LockBit. Given that RansomHub affiliates are known for exploiting vulnerabilities to gain initial access, followed by double extortion, this could mean a significant ripple of ransomware distributors moving elsewhere.

Popular targets in Q2:

  * Services, healthcare, technology, legal, and finance were the most targeted industries in Q2 2025. The frontrunner this quarter is services, with 44.4% of posts containing these victims’ data. In a distant second place is healthcare (10.6%), followed by technology in third (10.0%). 

  * Top regional targets include the United States (66.0%), the UK in second place with just 6.7%, and Canada (6.6%), Germany (4.2%), and Italy (3.2%) taking the other three top spots. 




## Notable trends

### Affiliate Drift

Q2 has seen plenty of infighting between prominent and up-and-coming threat actors, claims of rivals uniting, and major players hit by arrests. It makes sense, then, that affiliates would be in a state of flux, moving from one RaaS group to another, or even holding off altogether until the dust settles. With so many rebrands and launches of newer, more nimble ransomware groups to choose from, expect to see more affiliates striking out in bold new directions.

### Unstable Alliances

Infighting sits uneasily next to cooperation in Q2, with some groups trying to facilitate bigger and better infrastructure, leak sites, and features offered to potential affiliates. DragonForce is a prime example, using its ransomware alongside other threat actors taking care of the initial access side of things. As we’ll highlight later, DragonForce may have a shaky alliance with what remains of RansomHub — or perhaps it’s something else altogether.

### Post, and Repost Again

In Q1, we took extra care to highlight that our top 10 included two sets of data; groups posting net-new leaks — that is, completely original and never-before-seen leak posts — and those posting reused or repurposed leaks. Well-known threat actors such as FunkSec and LockBit were found to be making use of old leak data, or mixing old data and faked attacks. Adopting new identities and reusing stale data for a quick promotional boost is also something to be wary of when covering ransomware groups and supposed leaks.  
For Q2, we’ve removed threat actors posting old or fake data from the top 10 completely. Q3 will no doubt require the same care and attention when looking to present the most accurate description of ransomware group activity possible.

## Ones to watch

For Q2, our ones to watch are a mix of new and established names. Threat actor arrests, hostile inter-group takeovers, innovative affiliate services, and potentially dangerous ransomware outbreaks in healthcare organizations define a frantic few months.

### Scattered Spider

First observed in 2022, Scattered Spider is a threat actor that often combines nation-state-level tradecraft with aggressive social engineering. It continues to take the spotlight in high-profile incidents, even in the midst of arrests potentially tied to the collective. Experts in weaponizing corporate environments and behaviors, careful attention is paid to the human side of corporate targets when sizing up a potential infiltration.   
This group is closely tied to social engineering techniques where initial access is concerned. Phishing, SIM swapping, and help desk social engineering are what Scattered Spider excels at, which can make early detection difficult.  
Large enterprises in industries such as gaming, telecommunications, and cloud computing are known to be attractive propositions to Scattered Spider. However, the group has also branched out into retail, finance, and the aviation sector. It’s been speculated that they are the group behind the June 30 cyber attack impacting 5.7 million [Qantas airlines](https://www.theguardian.com/business/2025/jul/06/qantas-attack-reveals-one-phone-call-is-all-it-takes-to-crack-cybersecuritys-weakest-link-humans) customers.  
Scattered Spider often partners with RaaS group DragonForce, with the former handling initial access and the latter providing the ransomware; together, they can be a devastating tag team of intrusion and extortion, and one which can lead to confusion between said groups in specific attacks.  
We can’t currently suggest how much impact [recent arrests](https://www.nationalcrimeagency.gov.uk/news/retail-cyber-attacks-nca-arrest-four-for-attacks-on-m-s-co-op-and-harrods) related to several retailer compromises may have on the threat actor. Suspicion of Computer Misuse Act offences, blackmail, money laundering, and participating in organised crime are [not easy charges to shrug off](https://www.theguardian.com/uk-news/2025/jul/10/four-arrested-over-cyber-attacks-marks-and-spencer-co-op-harrods). The “sink or swim” moment for Scattered Spider may already have passed by the time Q3 comes around.

### DragonForce

A new entry to our top 10 groups list, DragonForce (also known as “The DragonForce Ransomware Cartel”) first came to light with a 2023 attack on the Ohio Lottery, impacting roughly 500,000 individuals with claims of [stolen employee and customer data](https://www.securityweek.com/500000-impacted-by-ohio-lottery-ransomware-attack/). 

More recently, a UK retailer, itself a victim of a major attack in April of this year, [attributed the compromise to DragonForce](https://www.bbc.co.uk/news/articles/cvg81m2mdmjo). According to the company’’s chair, the attack, which is expected to impact this year’s profits by around $400m, felt like it was intended to “destroy the business.”

DragonForce is media-savvy and has its own AI generated [calling card](https://bsky.app/profile/joetidy.bsky.social/post/3lu5q7jsp4s2l), occasionally sent directly to BBC journalists to announce what may be new breaches.

To add to the drama surrounding this threat actor, shortly after RansomHub’s leak site went offline in late March, it was defaced with a prominent “R.I.P. 3/3/25” message. In April, DragonForce published a “new projects” portal on their own leak site linking back to that message—and explicitly invited RansomHub to join their newly branded “Ransomware Cartel.” 

Analysts widely interpret this as a hostile takeover; DragonForce also publicly declared on the RAMP dark‑web forum that RansomHub had “decided to move to our infrastructure.” The result is a tangled and dramatic subplot that seems to reflect DragonForce’s strategic push to absorb affiliates and expand its footprint. A messy, convoluted tale with no clear narrative, but perhaps that’s exactly what an up-and-coming threat actor with a view to expansion wants.

### Qilin

In our Q1 2025 ransomware blog, Qilin came fourth in our top 10 list once non-net-new leak posts were excluded. We _did_ say this threat actor was one to watch, and sure enough, Qilin is top of the list once similar non-net new exclusions are applied.

Qilin, working its way through healthcare, financial, and manufacturing businesses since 2022, has had a dramatic few months since we last referenced its activities.

Once more we return to the now-defunct RansomHub, because though absent, the shadow of its presence looms large; even with the increase in leak posts from Qilin in Q2, it would likely have remained in second place behind RansomHub’s prolific output. With the behemoth out of the way, this is now Qilin’s time to shine.

In June, it was revealed that Qilin added a “[call a lawyer](https://thehackernews.com/2025/06/qilin-ransomware-adds-call-lawyer.html)” feature to its affiliate panel. Said lawyer is supposed to be able to assist with ransom negotiations, stolen data assessment, and potential breaking of laws by victims post-compromise. Doubt has been cast with regard to how useful this service would actually be, and an argument could be made that it does sound like something largely designed to attract more affiliates. New, flashy services and features help to put a RaaS offering a cut above the rest, which is surely something Qilin operators have considered when adding this new service.

By the same token, sometimes publicity and making headlines can have the _opposite_ effect where attracting affiliates is concerned. It was [recently confirmed](https://www.theregister.com/2025/06/26/qilin_ransomware_nhs_death/) that a large-scale ransomware attack on one of the NHS’s suppliers in 2024 was a contributory factor — among several others — to the death of a patient. In total, 170 patients suffered “low harm” impact as a result of the Qilin-attributed attack on Synnovis.

With Qilin responsible for [other attacks](https://www.theregister.com/2025/03/05/qilin_ransomware_credit/) in the healthcare industry, it remains to be seen if the threat actor’s [“we don’t care” attitude](https://www.theregister.com/2024/06/20/qilin_our_plan_was_to/) proves a little too rich for would-be affiliates. 

## Tactics

As with Q1, RaaS and double extortion are overwhelmingly favored by the majority of threat actors in our top 10. The volume of leak posts over Q2 is high, with both never-before-seen leaks and rehashed data adding to the total. Additionally, some groups are making use of stealer logs and Initial Access Broker (IAB) forums which provide credentials for the first point of entry into a compromised network.

The risk-reward line in the sand is perhaps making some groups become a little greedy in the rush to snap up new and potentially floating affiliates. Relaxing entry requirements for affiliate schemes, as DragonForce and Cicada3301 have done, may well lower the barrier to entry for wannabes.

Considering how quickly rival groups will go to war with one another over actual or perceived slights, it seems risky to simply hope that new affiliates will play by the rules—or not get themselves caught and expose the inner workings of an operation. In the worst case scenario, a new affiliate not subject to stringent checks could turn out to be a security researcher, law enforcement, or even someone from a rival threat actor. As we said: risk-reward.

## Recommendations

In our [Q1 2025 post](https://www.rapid7.com/blog/post/2025/04/08/2025-ransomware-business-as-usual-business-is-booming/), we highlighted “Five things you can do now” to secure your organization against the ever-present threat of ransomware-centric compromise. Effective multi-factor authentication (MFA) deployment, continuous patch management, and attack surface investigation are all great ways to set about tackling the ransomware scourge. But what can you do when your attacker is a _specific_ threat actor, such as Scattered Spider?

  1. **Lock down the help desk** : An important part of Scattered Spider’s intrusion techniques are help desk scams. Employee data scraped from LinkedIn profiles, combined with a lack of security precautions from the employer often hands Scattered Spider a first rung on the compromise ladder. Train help desk staff to recognize common social engineering techniques, especially around quick “emergency” resets, and enforce strict verification for password and MFA resets. High-privilege accounts may require multi-factor or even multi-person approvals, especially for out-of-band or urgent sounding reset requests.  
Place limits on how many support staffers can reset admin-level accounts, and ensure all such actions are logged with management.

  2. **Deploy and secure your MFA** : Phishing-resistant MFA is crucial for users, especially administrators. For example, the latter in particular should not be using easily compromised SMS messaging for authentication codes, as this is a form of authentication notorious for being hijacked with fake help desk calls. App-based OTP with number matching, or FIDO2 security keys, would be better options here. As Scattered Spider is [known to deploy MFA fatigue techniques](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a), countering this with the limiting of push attempts or number matching should be viewed as an important, if not essential, tool for warding off Scattered Spider attacks.  
No matter which form your MFA takes, quick detection of newly added devices or unusual IP activity can help a security team to prevent further pivots from the attacker.

  3. **Revisit your identity hygiene and least privilege** : With compromised credentials being such an important part of Scattered Spider’s tactics, it makes sense to keep business-critical accounts from everyday activities. High-privilege tasks should be performed by unique accounts, with just-in-time elevation applied to said accounts so that even a compromise cannot lead to immediate escalation without an approval request.

  4. **Tighten cloud security and monitoring** : Scattered Spider’s deep understanding of cloud environments using Amazon Web Services (AWS) Systems Manager Session Manager, EC2 Serial Console, and Identity and Access Management (IAM) role enumeration to pivot and persist within cloud infrastructure spells trouble for organizations with insecure cloud environments.  
Ensure cloud management pathways are locked down, and restrict the use of Systems Manager Session Manager and the EC2 Serial Console to authorized admin users only in AWS. Enable alerts if these features are used by new users or unusual IP addresses. Monitor cloud audit logs for AWS (CloudTrail), Microsoft Entra ID, for any sign of intrusion—this may take the form of IAM role enumeration calls, or unexpected IAM new user creation.  
Behavior analytics can help to pinpoint when a low-privilege user suddenly begins performing admin-level actions. Ensure that a compromised Okta/SSO user cannot by itself administer the entire cloud environment by making use of the [principle of least privilege](https://www.rapid7.com/fundamentals/what-is-least-privilege-access-lpa/).

  5. **Enact a backup and response plan** : Offline and encrypted backups of critical data, alongside regular testing of restoration plans, will ensure there is no eleventh hour panic should the worst happen. As Scattered Spider wastes no time from initial compromise to full domain/admin takeover, an incident response plan is crucial to quickly and safely lock down a Scattered Spider attack.  
Rapid invalidation of active sessions and tokens, forced enterprise-wide password resets, and locking down help desk password resets will work wonders here, as will the deployment of your incident response teams.

  6. **Take it to the table** : Tabletop exercises, which make full use of Scattered Spider’s playbook of known tactics, techniques, and procedures (TTPs), should be a part of any scenario intended to determine how much of a Scattered Spider storm your organization thinks it can weather. Focus on key Scattered Spider techniques, such as a dedicated help desk attack exercise.  
For example: maybe the attacker has already gained an employee’s phone number from LinkedIn, and is attempting a SIM swap social engineering attempt on the help desk technician. Perhaps the attacker has instead compromised the login of the _help desk worker_ via a phishing website, and is looking to create hidden privileged accounts. In this scenario, how would you know the rogue account had been created? What data would you look for to indicate unusual activity, and where would it live? We mentioned multi-person approvals for new account creation up above; what happens if there’s no approval required?




Rapid7 offers more information on Scattered Spider in [this Insights, Observations, and Recommendations post](https://www.rapid7.com/blog/post/scattered-spider-rapid7-insights-observations-and-recommendations/).

## Conclusion

The rise of groups such as DragonForce, as well as Qilin’s newfound dominance in the face of RansomHub’s absence, signals a period of what may be prolonged powerscale rebalancing and affiliate enticement among threat actors. Add to this the uncertain lay of the land with regard to supposed ransomware alliances, and we have a perfect storm of groups working together — yet remaining at odds — while businesses attempt to parse shifting threat actor patterns. 

The sheer chaos of this environment means that it’s never been more important for organizations to make use of threat intelligence and explore what makes these groups tick. Their willingness to exploit new strains of ransomware and affiliate activity, while also leveraging social engineering, is clear to see. A defense-in-depth approach that covers both [detection and response](https://www.rapid7.com/services/managed-detection-and-response-mdr/) and social engineering training to address the human element is crucial. 

Maybe it’s finally time to dust off that tabletop.

## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)