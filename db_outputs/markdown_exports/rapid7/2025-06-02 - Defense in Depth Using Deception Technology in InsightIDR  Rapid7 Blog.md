# Defense in Depth Using Deception Technology in InsightIDR | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/07/21/defense-in-depth-using-deception-technology-in-insightidr/
- **Date :** 2025-06-02

---

Welcome to the land of confusion and misdirection! Today, we are diving into the four pieces of [deception technology](/solutions/deception-technology/) that Rapid7 offers through our incident detection and response tool, InsightIDR. These include honeypots, honey users, honey files, and honey credentials. 

To be clear, all of these features and add-ons are under the guise that the attacker has already breached the perimeter and is now looking deeper inside for loot such as personal identifiable information, personal health information, passwords or usernames, etc. 

None of these pieces rely on the other, and all can be implemented individually as well as together. Deploying some or all of these features will bring the most benefit and visibility for many common attack vectors.

When deploying any of these features, creativity and Kung Fu trickery is the name of the game, and the best will normally win! Read on as we go through each feature in detail and give you a few ideas for how to get started.

## Honeypots

[Honeypots](/fundamentals/honeypots/) are virtual appliances that run on Ubuntu 18.04 LTS and are hardened to CIS standards. Honeypots come included in InsightIDR, and the product does not limit how many honeypots you can deploy within your environment. Knowing this, we recommend that you deploy as many as feasible in as many various subnets as possible, such as placing them in the DMZ, various VLANs around the network, Userland, and anywhere you want more visibility as far as network enumeration and active reconnaissance go. 

These devices are imitating the Holy Grail of all hosts because all well-known ports are open—however, it is nearly impossible to break in or log in to this virtual appliance, even from an administrator perspective. However, we do have a [troubleshooting honeypot](https://docs.rapid7.com/insightidr/troubleshooting-honeypots/) available, but it is purely a network troubleshooting tool and is not meant for production. Once you configure this machine, (proxy or static IP; DHCP?; Default Gateway; Subnet Mask), it utilizes a set-it-and-forget-it-type technology. These can be seen as enumeration landmines, so the more you have, the higher the probability of catching the attacker.  
When it comes to naming honeypots, we recommend following the naming convention that is already in place, then throwing some in the mix that are outside the normal spectrum, such as DC01-DNS, FinanceDB-Internal, or SQLDB-Customers. Naming your honeypots is critical, since this is what the attacker will be privy to. This also enables security professionals using InsightIDR to bring more visibility to network-based attacks and potentially malicious behavior on the network.

## Honey users

Next, we will look at [honey users](/blog/post/2018/06/21/deception-technology-in-insightidr-setting-up-honey-users/). This is another important tool to leverage in your environment, and the amount of users you can create is unlimited. This feature serves several best practices over several security standards, the first being default accounts (admin, administrator, root, superadmin, sqladmin). The majority of them are known in the attacker space or are only a quick Google search away, so removing these from production and allowing them to become honey users can bring more visibility into the low-hanging fruit. 

One fairly popular example is [SecLists](https://github.com/danielmiessler/SecLists), which has over a billion entries when it comes to usernames, passwords, phrases, leaks, etc. There are plenty of these lists all over the World Wide Web, so it is best to take precautionary measures against attackers leveraging default accounts. Honey users can serve as one of those measures. Once you stop using the default accounts internally, they can be brought in as honey users and start bringing visibility to their usage. 

Second, when it comes to users, there are plenty of PowerShell commands you can use to find more information about the target accounts, their level of access, and their activity. This series of blog posts by Oxford SBS Guy goes into great detail on various simple commands you can use to gather information that can be pivotal to reaching domain admin or the next level in the attack plan.

A third idea would be to set up cron jobs or scheduled tasks to periodically access the account so it seems active. You can mimic regular account templates so they don’t seem too obvious, or even create fake social media accounts to further the narrative that this is a real employee, not a decoy user account. 

Here is an example of running PowerShell commands against Active Directory, and the type of information you can extract:

![](https://lh5.googleusercontent.com/RVUmcH9vHKZ2l0cn_9aCWjEG4DO8lMTC4h8eaFPfhPQNzBr_QKUpx_HrTqyrqrb9RCn7MNn47ovTPQHSz4joxkuEuG6z7Mj2Po8bHHrWh1BJrDV3eAqT3QZPtAwn10-49co3KDR_)Image source

Another suggestion for honey users could fall under board members, consultants or contractors, building maintenance, and the executive team (such as the CEO, CIO, CFO, etc). These folks normally behave a bit differently than the majority of end users. For example, some consultants may only be on projects for particular time frames throughout the year or until a project is done, which means their account winds up lingering far after their completion or departure. These accounts also find themselves with non-expiring passwords, which can pose another threat if employees aren’t properly trained on best practices around password generation. 

The best way to figure out what attackers might be able to see is to put yourself in their shoes and use your own OSINT capabilities to evaluate your company’s public footprint. If you can find LinkedIn accounts and/or leaked databases that contain company information, this would be what attackers are able to see. Depending on what is available publicly already, that is a great place to start with the types of traps we plan to set. Plenty of tools exist to enumerate from the outside, such as [MX Toolbox](https://mxtoolbox.com/), [AbuseIPDB](https://www.abuseipdb.com/), and [urlscan.io](https://urlscan.io), to name a few. 

Here is another example of filtering out user Group information via PowerShell:

![](https://lh6.googleusercontent.com/l0fPtY7QCmUHK3zKa_iiwKTrtUtwFT7lSVrAK5UyxCPZjsyE-DJkBfmI8V14YfmGGXkDcs7tfQWWNkxFJbNQ1bDEB0bHtMwk55iFQzB52eaUDyndDbiq3nnTYr71rBIfSWBUzZmV)Image source

## Honey files

Next, we’ll break down [honey files](https://docs.rapid7.com/insightidr/honey-files/), which are also highly recommended and equally as valuable as the other deception features. Honey files can be leveraged to help detect or inform the team that something malicious could be brewing. For example, ransomware or any worm-like virus that is going to touch a lot of network files in a short amount of time does not demonstrate normal, human-like behavior, which would indicate some form of a script or automated attack in play. 

Similar to other InsightIDR deception technology features, there is no limit on how many honey files you can deploy. You can also choose any file extension you desire, such as .pdf, .doc, /db, or .xls. 

Another example would be password manager applications such as KeePass. KeePass uses password database files, and there are known exploits for applications of this nature out there, as well as automated tools that search for particular file extensions and attempt to auto-exploit. This would be an easy catch for the honey file, as any access to these is reported to the platform. 

While this does place some decoys around the environment, another attack vector to consider are insider threats. Placing a few appealing documents/files across our network servers may lead to blocking a possible data exfiltration attack or a disgruntled employee looking to bring harm to the company/colleagues.

## Honey credentials

Finally, that brings us to [honey credentials](https://docs.rapid7.com/insightidr/honey-credentials/). These are one of the easiest features to deploy, as they do not require any configuration from you other than deploying the Insight Agent to your Windows assets. This is an opt-in feature as well, so you would need to reach out to a Rapid7 resource such as a customer success manager to have this enabled. 

When you opt in to the honey credential, a honeyhash will be inserted into memory on all your endpoints (Windows and Agent installed), for the avenue of someone running a memory scraping tool, such as Mimikatz, and then spraying and praying with those hashes as authorization using psexec and/or pass-the-hash attacks. 

There is not a way to pick and choose which assets receive the honeyhash, as it is an all-or-nothing feature. This may interfere with third-party applications that may detect this type of behavior, it is simple to whitelist the process generated from this. If you want to see how easy running a memory scraping tool such as Mimikatz is, you can test it out following the instruction posted by [Black Hills Infosec](https://www.blackhillsinfosec.com/your-password-is-wait-for-it-not-always-encrypted/).

The common methods attackers use are still easily tripped up by adding some additional obstacles in your internal environment. It’s not enough to solely depend on the perimeter firewall—it’s time to start looking at the internal network that we can control. Most of the attacks carried out originate from the inside, whether that be disgruntled employees or unintentional attackers who may not even know they have been compromised. Keeping a good grasp of the assets and vulnerabilities is only part of the mission—and having these additional four elements is a must when handling today’s cyber-landscape.  


## Article tags

  * [InsightIDR](/blog/tag/insightidr/)
  * [Detection and Response](/blog/tag/detection-and-response/)
  * [Incident Detection](/blog/tag/incident-detection/)
  * [Incident Response](/blog/tag/incident-response/)
  * [Honeypots](/blog/tag/honeypots/)
  * [Project Lorelei](/blog/tag/project-lorelei/)