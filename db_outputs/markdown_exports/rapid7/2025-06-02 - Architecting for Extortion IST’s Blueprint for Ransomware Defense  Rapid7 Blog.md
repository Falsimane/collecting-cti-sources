# Architecting for Extortion: IST’s Blueprint for Ransomware Defense | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/09/02/architecting-for-extortion-acting-on-the-ists-blueprint-for-ransomware-defense/
- **Date :** 2025-06-02

---

Last month, the Institute for Security and Technology’s (IST) Ransomware Task Force (RTF) launched the [Blueprint for Ransomware Defense](https://securityandtechnology.org/ransomwaretaskforce/blueprint-for-ransomware-defense/), a mitigation, response, and recovery plan for small- and medium-sized enterprises. This action plan is a cross-industry document that targets business leaders and protectors to ensure that even resource-strapped organizations can defend against the continued threat of extortion attacks, including [ransomware](/fundamentals/what-is-ransomware/).

Crucially, the RTF understands that most teams are strapped for resources, including time. So while it can be incredibly insightful — and great fun — to sketch out taxonomies of ransomware actors and their TTPs, or do graph analysis on communications networks for cybercrime groups, the blueprint considers what they call “essential cyber hygiene,” the foundational capabilities needed to successfully combat ransomware and other extortion threats.

## A note on terminology

The term “ransomware” refers to a type of malware that encrypts files and demands payment for the key necessary to decrypt the files. A trend pioneered by the Maze ransomware group in 2020, [double extortion](/blog/post/2022/07/27/to-maze-and-beyond-how-the-ransomware-double-extortion-space-has-evolved/), adds a second layer to this by also exfiltrating files and threatening to leak them if the ransom is not paid. We’ve also begun to see a broader trend of hack-and-leak extortion operations typified by the now-defunct LAPSU$ group, where rather than performing double extortion, the attacker simply skips the ransomware step of the operation. 

While the Ransomware Task Force — as its name suggests — has prioritized ransomware, and the blueprint is called the Blueprint for _Ransomware_ Defense, the overwhelming majority of the safeguards are useful against a variety of attacks. Thus, when we say “ransomware,” we specifically mean “an attack in which your files are encrypted and a ransom is demanded” and “extortion” for the broader class of operations.

## How to use the blueprint

The blueprint outlines 40 safeguards: 14 foundational and 26 actionable. The foundational safeguards are the well-trod security advice that protectors are familiar with: Have an asset inventory, have a vulnerability management process, establish a security awareness program, etc. 

Readers who wish to review these safeguards should consult the RTF blueprint directly and particularly consider printing out Appendix A, which nicely lists the category and type of each safeguard while also mapping it to the National Institute of Standards and Technology (NIST) [cybersecurity framework](https://www.nist.gov/cyberframework) function and the [Center for Internet Security (CIS) safeguard](https://www.cisecurity.org/controls/v8) number. There is also a helpful [tools and resources](https://docs.google.com/spreadsheets/d/1kQUb_gawFeNPllGBDrgy7c0uNGyM7Lwt/edit#gid=797732538) spreadsheet linked in the PDF. 

## Safeguards to start implementing today

All of the safeguards chosen by the RTF are designed to be easy to implement and offer good “bang for your buck.” The controls that RTF has identified as important have also been [identified by CIS](https://www.cisecurity.org/insights/blog/ransomware-impacts-and-defense-controls) as crucial for [ransomware prevention](/solutions/ransomware-prevention/). However, some items, such as having a detailed asset inventory, are easier said than done. Of these, a handful are uniquely impactful or easy to implement, so they offer a good starting point.

**1\. R****equire MFA for externally exposed applications, remote network access, and administrative access**

OK, technically this recommendation is three safeguards, but since they’re related, we’re lumping them into one. Lumping these together does not mean that implementation is a one-stop shop. Indeed, each one of these will require its own configuration to get working. However, as our incident response analysts and pentesters can both attest, the number one headache for attackers is multi-factor authentication (MFA). 

MFA may not be a panacea, but it can serve as a roadblock for initial access or lateral movement, and it can provide an early warning that someone is in your environment who does not belong. If your organization is not pushing MFA everywhere, they should be, as most enterprise applications today support it natively or via single sign-on. A variety of free and paid authenticators exist and can be implemented in a straightforward manner. 

**2.****Restrict administrator privileges to dedicated administrator accounts**

Separation of duties is a longstanding core tenet of information security, but between remote work, the increased speed of communications and development, and the general expectation that things Get Done Right Now, we have systematically over-privileged user accounts. Even if global administrators remain rare, users are often local administrators on their machines, permitting the installation of unauthorized software that can be used by attackers and access brokers to establish persistence. This persistence can be leveraged into higher-level access through the use of tools like Mimikatz or techniques like [Kerberoasting](/fundamentals/kerberoasting-attack/), and that higher-level access exposes the enterprise to significant risk. 

By restricting administrator privileges to dedicated accounts, we develop some very clear indicators that something is wrong – no administrator account should ever be logged in multiple places at the same time, and there are some functions that simply should never be performed from a dedicated administrator account. This may add some friction to your IT management, but it’s good friction.

**3.****Use DNS filtering services**

Unlike the two previous suggestions, this is something that not only could you start implementing today – you could probably _finish_ implementing it today. Domain Name System (DNS) filtering services replace the default DNS configuration in your environment. Free options like Quad9 and OpenDNS offer security-friendly domain name lookups, which can defeat [phishing](/fundamentals/phishing-attacks/) attempts, [malvertising](/fundamentals/malvertising/), and [malware](/fundamentals/malware-attacks/) command and control beaconing. 

CIS also offers malicious domain blocking and reporting to members of some organizations. In general, this is a simple configuration update that can be pushed to all computers and will instantly improve your security posture.

## Safeguards for tomorrow

While the three action items for today will offer the greatest return on investment for your time, all of the safeguards in the guide are important. Many are well-understood but can take time to implement. For some controls that aren’t “table stakes” in the way that deploying anti-malware software, establishing a security awareness program, and collecting audit logs are, we offer a bit of advice.

**1.****Manage default accounts on enterprise assets and software**

As Rapid7’s own [Curt Barnard](https://twitter.com/CurtBarnard) demonstrated with Defaultinator this year at [Black Hat](/blog/post/2022/08/19/pushing-open-source-security-forward-insights-from-black-hat-2022/), applications and hardware are still rife with default credentials that never get changed. Defaultinator is one tool that can help evaluate devices that may have default credentials in use. Finding these default accounts can be challenging, but once you have a good asset inventory, managing these default accounts is important to keeping attackers out and your data in.

**2.****Use unique passwords**

Continuing with the notion of credentials, using unique passwords is incredibly important. Password reuse is a common way for attackers to move from a single, potentially unrelated account to your crown jewels. Today, there are myriad password management tools that will even generate unique passwords for users and many of them offer enterprise subscriptions. Of these, nearly all allow for the secure sharing of passwords – if for some reason that is necessary. (Hint: It's almost never actually necessary, but merely a bad habit.) Easily guessable (or easily shareable) passwords often fall victim to brute-force or password-spraying attacks, and with an enterprise password management tool, no user should need to use passwords that aren’t both strong and unique.

**3.****Establish and maintain a data management process**

While we all know the power, benefit, and value of backups – especially when it comes to ransomware – data management is a bit more nuanced. We know that attackers in double extortion or leak-and-extort operations choose the files they steal and leak carefully to put maximum pressure on victims. Thus, the data management process is of increased importance for this category of attack. Categorizing and classifying your data will help inform the particular restrictions that need to be put around that data. Since attackers are targeting and leaking different sorts of data across industries, it’s imperative to know what data is most important to you and [most likely to be targeted by attackers](/info/ransomware-data-disclosure-trends/), and to have a plan to protect it.

While extortion attacks are on the rise and ransomware remains an expensive threat to organizations, action plans like the RTF’s Blueprint for Ransomware Defense serve as great tools to help decision makers, technical leaders, and other protectors mitigate extortion attacks. The safeguards in the report and the details in this blog post can help prioritize and contextualize what needs to be done. After all, we're all targets, but we don’t all have to be victims.

_**Additional reading:**_

  * [_To Maze and Beyond: How the Ransomware Double Extortion Space Has Evolved_](/blog/post/2022/07/27/to-maze-and-beyond-how-the-ransomware-double-extortion-space-has-evolved/)
  * [ _For Finserv Ransomware Attacks, Obtaining Customer Data Is the Focus_](/blog/post/2022/07/07/for-finserv-ransomware-attacks-obtaining-customer-data-is-the-focus/)
  * [ _For Ransomware Double-Extorters, It's All About the Benjamins — and Data From Healthcare and Pharma_](/blog/post/2022/06/28/for-ransomware-double-extorters-its-all-about-the-benjamins-and-data-from-healthcare-and-pharma/)
  * [ _New Report Shows What Data Is Most at Risk to (and Prized by) Ransomware Attackers_](/blog/post/2022/06/16/new-report-shows-what-data-is-most-at-risk-to-and-prized-by-ransomware-attackers/)

  


## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)