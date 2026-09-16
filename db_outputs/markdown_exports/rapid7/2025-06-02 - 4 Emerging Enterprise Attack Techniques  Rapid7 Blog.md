# 4 Emerging Enterprise Attack Techniques | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/09/02/sans-experts-4-emerging-enterprise-attack-techniques/
- **Date :** 2025-06-02

---

In a recent report, a panel of SANS Institute experts broke down key takeaways and emerging attack techniques from this year’s RSA Security Conference. The long and short of it? This next wave of malicious methodologies isn’t on the horizon — it’s here.

When it comes to supply-chain and [ransomware attacks](/fundamentals/what-is-ransomware/), bad actors seem to have migrated to new ground over the last 2 years. The SANS Institute report found that government, healthcare, and retail (thanks in large part to online spending at the height of the pandemic) were the sectors showing the largest spike from the first quarter of 2020 to this year, in terms of finding themselves in attackers’ crosshairs. As larger incidents increase in frequency, let’s take a look at 4 specific attack formats trending toward the norm and how you can stay ahead of them.

## 1\. Cracks in the facade of software integrity

Developers are under greater pressure to prioritize security (i.e., shift left) within the [Continuous Integration/Continuous Delivery (CI/CD)](/fundamentals/cicd/) lifecycle. This would seem to be at stark odds with the number of applications built on open-source software (OSS). And, if a security organization is part of a supply chain, how many pieces of OSS are being used at one time along that chain? The potential is huge for an [exponential jump in the number of vulnerabilities](/blog/post/2021/09/08/security-at-scale-in-the-open-source-supply-chain/) in that group of interdependent organizations. 

There are ways to mitigate these seemingly unstoppable threats. Measures like file integrity monitoring (FIM) surface changes to critical files on your network, alerting you to suspicious activity while also providing context as to the affected users and/or assets. Threat hunting can also help to expose vulnerabilities. 

Used with a cloud-native, [extended detection and response](/fundamentals/extended-detection-response/) (XDR) approach, Rapid7’s proactive threat-hunting capabilities leverage multiple security and telemetry sources to act on fine-grained insights and empower teams to quickly take down threats.

## 2\. Do you have a token to get into that session?

Commonly, applications make use of tokens to identify a person wishing to access secure data, like banking information. A user’s mobile app will exchange the token with a server somewhere to verify that, indeed, this is the actual user requesting the information and not an attacker. Improper session handling happens when the protocols according to which these applications are working don’t properly secure identifying tokens. 

The issue of improper user authentication was exacerbated by the onslaught of the pandemic, as companies raced to secure — or not — enterprise software for a quickly scaled-up remote workforce. To resolve this issue, individual users can simply make it a best practice to always hit that little “log off/out” button once they’re finished. Businesses can also do this by setting tokens to automatically expire after a predetermined length of time. 

At the enterprise level, security organizations can use a comprehensive application-testing strategy to monitor for weak session handling and nefarious attacker actions like: 

  * Guessing a valid session token after only short-term monitoring
  * Using static tokens to target users, even if they’re not logged in
  * Leveraging a token to delete user data without knowing the username/password



## 3\. Turning the machines against us

No, that’s not a _Terminator_ reference. If someone has built out a machine-learning (ML) algorithm correctly, it should do nothing but assist an organization in accomplishing its business goals. When it comes to security, this means being able to recognize traffic patterns that are relatively unknown and classifying them according to threat level. 

However, attackers are increasingly able to corrupt ML algorithms and trick them into labeling malicious traffic as safe. Another sophisticated method is for attackers to purchase their own ML products and use them as training grounds to produce and deploy malware. InsightIDR from Rapid7 leverages user-behavior analytics (UBA) to stay ahead of malicious actions against ML algorithms.

Understanding how your ML product functions is key; it should build a baseline of normal user behavior across the network, then match new actions against data gleaned from a combination of machine learning and statistical algorithms. In this way, UBA exposes threats without relying on prior identification in the wild.

## 4\. Ramping up ransomware

Let’s face it: Attackers all over the world are essentially creating repositories and educational platforms in how to evolve and deploy ransomware. It takes sophistication, but ransomware packages are now available more widely to the non-tech set to, for lack of a more apt phrase, plug and play. 

As attack methodologies ramp up in frequency and size, it’s not just data at risk anymore. Bad actors are threatening companies with wide public exposure and potentially a catastrophic loss to reputation. But there are opportunities to learn offensive strategies, as well as how attacker techniques can become signals for detection.

  * **Evaluate your security plan:** The Cybersecurity Maturity Assessment provides a view of your current security posture and a guide to strategic planning.
  * **Consult with Rapid7 on security improvements:** Sustainable programs — from [vulnerability management](/fundamentals/vulnerability-management-and-scanning/) to [incident response](/fundamentals/incident-response/) — are the backbone of success. Create processes and collateral to run any facet of your security program.



## Target shifts

If the data in the SANS report tells us anything, it’s that attackers and their evolving methodologies — like those mentioned above — are constantly searching not just for bigger targets and paydays, but also easier paths to their goals.

Targeted industry shifts in year-over-year data show that the company or sector you’re in clearly makes no difference. Perhaps the biggest factor in bad actors’ strategies is the degree of ease with which they get what they want — and some industries still fall woefully behind when it comes to security and attack readiness. 

## Article tags

  * [Research](/blog/tag/research/)
  * [Cloud Security](/blog/tag/cloud-security/)