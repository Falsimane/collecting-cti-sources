# We’re Still Terrible at Passwords; Making it Easy for Attackers | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/10/20/new-research-were-still-terrible-at-passwords-making-it-easy-for-attackers/
- **Date :** 2025-06-02

---

Passwords, amirite? We all have them. Probably a lot of them. And they are among the most important lines of defense against nefarious attackers seeking access to our online accounts. Sadly, as we all know too well, password health isn’t exactly our collective strong suit and too often we hear about breaches coming from loosely or poorly managed passwords. 

At Rapid7, we are constantly conducting original research into the latest trends in attacker behavior, vulnerabilities, and cyber security trends that could lead to the next big breach (or the next big goal line save). In our latest report, [Good Passwords for Bad Bots](/info/good-passwords-for-bad-bots/), we took a look at two of the most popular protocols used for remote administration, SSH and RDP, to get a sense of how attackers are taking advantage of weaker password management to gain access to systems. What we found in many ways confirmed our assumptions 1) attackers aren’t “cracking” passwords on the internet; and 2) we still collectively stink at password management. 

Here’s how we did it. 

As a cybersecurity company we are sometimes called upon to dabble in the “dark arts” in order to better prepare ourselves and our customers for the types of attacks they can expect to see in the real world. Sometimes that means penetration testing (hire us to hack into your systems, trust us, it’s fun). And sometimes we deploy honeypots to entice and capture behavior of attackers in a risk-free environment in order to study them. 

For this report, we used our network of honeypots (a few hundred of them) to monitor SSH and RDP login attempts. Once we zeroed in on authentication attempts (as opposed to vulnerability exploit attempts, low-touch scans, and the like) we found 512,002 unique passwords were attempted to be used by attackers. 

We then turned to the rockyou2021.txt list to determine how many of those passwords existed in this industry-standard list of exposed passwords. Prepare to be shocked: nearly all of them were. In fact, we found just 14 of the passwords being brute forced into our honeypots were NOT found in the rockyou2021.txt file. And we think those were likely errors as they included a string of the honeypots’ IP addresses in them. Unless they are signs of some dastardly attack that we haven’t seen before <cue dramatic music> they are likely insignificant.

But if attackers were using automated tools to “crack” passwords online we’d see more of them, a lot more. There are something to the tune of 8.4 billion passwords on the rockyou2021.txt file. We found less than half a million in our honeypots. What’s more likely to happen is attackers still rely on the human connection to security infrastructure which is notoriously one of the weakest links in the chain. [Social engineering](/fundamentals/social-engineering/), like phishing for passwords, and credential stuffing (ie. trying known passwords across other targeted platforms to catch someone reusing identical usernames and passwords) are still stronger ways for attackers to gain access to passwords than cracking them automatically. 

What this tells us in practicality is that it’s not terribly hard to avoid this class of attack. In fact, some of the most attacked credentials were ones that should make any internet-literate person facepalm hard. The three most popular user names for RDP were “administrator,” “user,” and “admin.” The three most common passwords? Brace yourselves: “root,” “admin,” and “nproc.” One of the most popular passwords was literally “123456” which is definitely not the combination to our luggage. So, yeah, we’re not doing well enough with our passwords. 

But as we said earlier, it’s not that hard to beat this kind of attack. You don’t even have to have a particularly strong password in order to protect yourself, just one with randomness in it. Maybe throw in a few strange characters. Don’t reuse it for multiple logins. And above all don’t use default passwords. All of these things would be covered by the use of password manager services that create unique, random passwords for every one of your online accounts. We’re not getting paid by these services to say this, I assure you, they just happen to be a strong but underutilized way to have good credential hygiene. 

If you want to learn more, download our new report [Good Passwords for Bad Bots](/info/good-passwords-for-bad-bots/). And then, go change your passwords. All of them. You’ll be glad you did. 

## Article tags

  * [Research](/blog/tag/research/)