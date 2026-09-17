# 8 Tips for Securing Networks When Time Is Scarce | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/03/22/8-tips-for-securing-networks-when-time-is-scarce/
- **Date :** 2025-06-02

---

_"At this particular mobile army hospital, we're not concerned with the ultimate reconstruction of the patient. We only care about getting the kid out of here alive enough for someone else to put on the fine touches. We work fast and we're not dainty, because a lot of these kids who can stand 2 hours on the table just can't stand one second more. We try to play par surgery on this course. Par is a live patient." - Hawkeye, M*A*S*H_

Recently, CISA released their [Shields Up](https://www.cisa.gov/shields-up) guidance around reducing the likelihood and impact of a cyber intrusion in response to increased risk around the [Russia-Ukraine conflict](/blog/post/2022/03/04/russia-ukraine-cybersecurity-updates/). This week, the White House echoed those sentiments and released a statement about potential impact to Western companies from Russian threat actors. The White House guidance also included a fact sheet identifying urgent steps to take.

Given the urgency of these warnings, many information security teams find themselves scrambling to prioritize mitigation actions and protect their networks. We may not have time to make our networks less flat, patch all the vulnerabilities, set up a backup plan, encrypt all the data at rest, and practice our incident response scenarios before disaster strikes. To that end, we’ve put together 8 tips for “emergency field security” that defenders can take **right now** to protect themselves.

## 1\. Familiarize yourself with CISA’s KEV, and prioritize those patches

CISA’s [Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (KEV) catalog enumerates vulnerabilities that are, as the name implies, known to be exploited in the wild. This should be your first stop for patch remediation. 

These vulns are known to be weaponized and effective — thus, they’re likely to be exploited if your organization is targeted and attackers expose one of them in your environment. CISA regularly updates this catalog, so it’s important to subscribe to their update notices and prioritize patching vulnerabilities included in future releases.

## 2\. Keep an eye on egress

Systems, especially those that serve customers or live in a DMZ, are going to see tons of inbound requests – probably too many to keep track of. On the other hand, those systems are going to initiate very few outbound requests, and those are the ones that are far more likely to be command and control. 

If you’re conducting hunting, look for signs that the calls may be coming from inside your network. Start keeping track of the outbound requests, and implement a default deny-all outbound rule with exceptions for the known-good domains. This is especially important for cloud environments, as they tend to be dynamic and suffer from “policy drift” far more than internal environments.

## 3\. Review your active directory groups

Now is the perfect time to review active directory group memberships and permissions. Making sure that users are granted access to the minimum set of assets required to do their jobs is critical to making life hard for attackers. 

Ideally, even your most privileged users should have regular accounts that they use for the majority of their job, logging into administrator accounts only when it’s absolutely necessary to complete a task. This way, it’s much easier to track privileged users and spot anomalous behavior for global or domain administrators. Consider using tools such as [Bloodhound](https://github.com/chryzsh/awesome-bloodhound) to get a handle on existing group membership and permissions structure.

## 4\. Don’t laugh off LOL

[Living off the land (LOL)](/fundamentals/living-off-the-land-attack/) is a technique in which threat actors use legitimate system tools in attacks. These tools are frequently installed by default and used by systems administrators to do their jobs. That means they’re often ignored or even explicitly allowed by antivirus and endpoint protection software. 

You can help protect systems against LOL attacks by configuring logging for Powershell and adding [recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) for these binaries unless they are necessary. Refer to the regularly updated (but not comprehensive, as this is a constantly evolving space) list of these at [LOLBAS](https://lolbas-project.github.io/).

## 5\. Don’t push it

If your organization hasn’t mandated multi-factor authentication (MFA) yet, now would be a very good time to require it. Even if you already require MFA, you may need to let users know to immediately report any notifications they did not initiate. 

Nobelium, a likely Russian-state sponsored threat actor, has been [observed](https://arstechnica.com/information-technology/2021/12/solarwinds-hackers-have-a-whole-bag-of-new-tricks-for-mass-compromise-attacks/) repeatedly sending MFA push notifications to users' smartphones. Though push notifications are considered more secure than email or SMS notifications due to the need for physical access, it turns out that sending enough requests means many users eventually – either due to annoyance or accident – approve the request, effectively defeating the two-factor authentication.

When you do enable MFA, be sure to regularly review the authentication logs, keeping an eye out for accounts being placed in “recovery” mode, especially for extended periods of time or repeatedly. Also consider using tools or services that monitor the MFA configuration status of your environment to ensure configuration drift (or attackers) have not disabled MFA.

## 6\. Stick to the script

Often, your enterprise’s first line of defense is the help desk. Over the next few days, it's important that these people feel empowered to enforce your security policies.

Sometimes, people lose their phone and can't perform their MFA. Other times, their company laptop just up and dies, and they can't get at their presentation materials on the shared drive. Or maybe they’re sure what their password should be, but today, it just isn’t. It happens. Any number of regular disasters can befall your users, and they’ll turn to your help desk to get them back up and running. Most of the time, these aren’t devious social engineering attacks. They just need help.

Of course, the point of a help desk is to help people. Sometimes, however, the “users” are attackers in disguise, looking for a quick path around your security controls. It can be hard to tell when someone calling in to the help desk is a legitimate user who is pressed for time or an attacker trying to scale the walls. Your help desk folks should be extra wary of these requests — and, more importantly, know they won’t be fired, reprimanded, or retaliated against for following the standard, agreed-upon procedures. It might be a key executive or customer who's having trouble, and it might not be.

You already have a procedure for resets and re-enrollments, and exceptions to that procedure need to be accompanied by exceptional evidence.

## 7\. Call for backup

Now is the time to make sure you have solid offline backups of:

  * Business-critical data
  * Active Directory (or your equivalent identity store)
  * All network configurations (down to the device level)
  * All cloud service configurations



Continue to refresh these backups moving forward. In addition, make sure your backups are integrity-tested and that you can (quickly) recover them, especially for the duration of this conflict.

## 8\. Practice good posture

While humans will be targeted with phishing attacks, your internet-facing components will also be in the sights of attackers. There are numerous attack surface profiling tools and services out there that help provide an attacker’s-eye view of what you’re exposing and identify any problematic services and configurations — [we have one](/research/project-doppler/) that is free to all Rapid7 customers, and CISA [provides a free service](https://www.cisa.gov/cyber-hygiene-services) to any US organization that signs up. You should review your attack surface regularly to ensure there are no unseen gaps.

While security is a daunting task, especially when faced with guidance from the highest levels of the US government, we don’t necessarily need to check all the boxes today. These 8 steps are a good start on “field security” to help your organization stabilize and prepare ahead of any impending attack.

**_Additional reading:_**

  * [_Russia-Ukraine Cybersecurity Updates_](/blog/post/2022/03/04/russia-ukraine-cybersecurity-updates/)
  * [ _The Top 5 Russian Cyber Threat Actors to Watch_](/blog/post/2022/03/03/the-top-5-russian-cyber-threat-actors-to-watch/)
  * [ _Conti Ransomware Group Internal Chats Leaked Over Russia-Ukraine Conflict_](/blog/post/2022/03/01/conti-ransomware-group-internal-chats-leaked-over-russia-ukraine-conflict/)
  * [ _New US Law to Require Cyber Incident Reports_](/blog/post/2022/03/10/new-us-laws-to-require-cyber-incident-reports/)

  


## Article tags

  * [Cybersecurity](/blog/tag/cybersecurity/)
  * [Security Strategy](/blog/tag/security-strategy/)
  * [Research](/blog/tag/research/)