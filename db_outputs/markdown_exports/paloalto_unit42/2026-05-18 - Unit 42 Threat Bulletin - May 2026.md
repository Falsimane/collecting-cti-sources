# Unit 42 Threat Bulletin - May 2026

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/threat-bulletin/may-2026/
- **Date :** 2026-05-18

---

![CATEGORY](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/04_Security-Technology_Category_1920x900.jpg)

MAY 18TH, 2026

#  Unit 42 Threat Bulletin - May 2026 

The May edition of the Unit 42 Threat Bulletin is live. Find new content and expert perspectives on the latest threats in this packed issue.

On April 17, 2026, we announced Palo Alto Networks was [conducting early testing](https://www.paloaltonetworks.com/blog/2026/04/defenders-guide-frontier-ai-impact-cybersecurity/) of the latest frontier AI models, including Anthropic’s Mythos model as part of Project Glasswing and OpenAI’s latest models as part of Trusted Access for Cyber program. We’ve continued testing and on May 13,[ we provided an update](https://www.paloaltonetworks.com/blog/2026/05/defenders-guide-frontier-ai-impact-cybersecurity-may-2026-update/) on our ongoing research, our learnings uncovered in the process, and the approach we’re taking to protect our customers. 

The results are the full, initial scan of over 130 products across all three platforms. The May 13 advisory covers 26 CVEs (representing 75 issues) versus our usual volume (typically less than 5 CVEs in a month); none of which are being exploited in the wild. 

As of the announcement, we’ve patched all important vulnerabilities in our SaaS delivered products, and all customer-operated products now have patches available. We intend to fix every vulnerability we find before advanced AI capabilities become widely available to adversaries. To help organizations prepare, we outline four steps in the announcement every organization needs to take immediately. 

Separately, this month’s Threat Bulletin focuses on how the supply chain has become one of the most effective paths into the enterprise. It also doesn’t look like a traditional attack surface anymore.

This isn’t just about vulnerabilities being exploited. Attackers are operating through the same software paths organizations rely on every day. Updates, dependencies, and build pipelines are becoming execution channels.

We also look at how far that shift has gone. Supply chain now extends beyond code into SaaS integrations, vendor management planes, and identity-driven access. One upstream issue can impact many downstream environments, often without raising immediate concern.

And in some cases, there are no exploits at all. Just vishing, valid credentials, and SSO. Once inside, access expands quickly across systems that already trust the user, which makes detection much harder.

Across all three, the issue is the same. The problem is no longer just stopping a breach. It’s understanding what your environment already trusts, how far that trust reaches, and what happens when it’s used against you.

![author image](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/Mitch-Insights-1.png)

Mitch Mayne, Principal, Security Research 

Get the monthly   
Unit 42 Threat Bulletin.

Subscribe ![Right Arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/right-arrow.svg)

## Intel and Insights

When Trusted Software Becomes the Attack Path

Recent incidents involving software updates, open-source dependencies, and build pipelines point to a shift in how attackers operate. They are not just exploiting vulnerabilities to gain access. They are executing through software paths that are already trusted.

To understand what’s changing and what it means for security leaders, I spoke with Justin Moore, a Senior Threat Intelligence Researcher here at Unit 42. We take a look at how these attacks are evolving and where organizations are most exposed.

**Mitch Mayne: **We’ve talked about supply chain risk for years. What’s actually different about what we’re seeing now?

**Justin Moore:** What’s changed is where the attacker operates. In the past, the focus was on getting in. Exploiting a vulnerability, gaining access, and then moving laterally. That still happens, but in these cases, the attacker is operating inside systems that are already trusted.

They are compromising the paths software uses to move and run. That includes updates, dependencies, and build pipelines, and then using those same paths to execute. So instead of something that looks like an intrusion, it looks like normal activity. Software updating, code being pulled, jobs running.

That changes the dynamic. Once an attacker is inside a trusted path, they are not working against controls in the same way. They inherit trust, and with that comes scale. In some recent cases, that scale is not just passive distribution. Compromised packages and pipelines are being used to propagate malicious code further across ecosystems, turning trusted software paths into active distribution channels. A single compromise can propagate quickly because it is moving through systems designed to distribute and execute by default.

**MM:** When an attacker operates through a trusted update, dependency, or pipeline, how does that change the risk compared to a more traditional intrusion?

**JM:** It changes both visibility and impact.

In a traditional intrusion, the attacker has to work for each step. They move laterally, escalate privileges, and try to avoid detection, so there are multiple chances to catch them.

When they operate through something your environment already trusts, much of that friction disappears. The activity itself looks legitimate. A package install, an update, a pipeline run. That makes it harder to detect and often slower to respond.

The bigger shift is impact. A single compromise does not stay contained. It can spread across systems and environments, depending on how widely that software is trusted and distributed. In more advanced cases, that spread is not just a byproduct of trust. Attackers are designing multi-stage campaigns that can move through dependencies or pipelines and extend their reach automatically, including stealing credentials or modifying additional components to continue propagation. At that point, the blast radius is no longer defined by what was initially compromised. It is defined by how much trust that system had and where it was allowed to execute.

**MM: **Where is this showing up today? Which parts of the software lifecycle are becoming the highest-risk execution paths?

**JM:** It shows up anywhere software is allowed to move and execute with minimal friction.

Updates are a clear example. They are designed to be automatic and widely distributed, so when something is compromised there, it moves fast.

Organizations pull in packages they trust, often indirectly, and those packages get executed as part of normal operations, sometimes extending that trust beyond a single environment through shared dependencies or developer access. 

Build pipelines are another area to watch. They are highly automated, which is what enables speed, but it also means that once something is inserted there, it can flow all the way through to production.

The common thread is not the specific component. It is the function. These systems are built to distribute and execute, which is exactly what makes them high risk when they are compromised.

**MM: **So if this activity often looks legitimate, what does a strong security model look like? What needs to change in how organizations think about trust and control?

**JM:** The biggest shift is moving away from treating trust as binary. These systems are trusted by design, so the focus has to be on what they are allowed to do.

That means putting tighter controls around identity and permissions, and being more deliberate about how far that trust extends. If something is compromised, the priority is limiting how much it can affect and how far it can go.

It also puts more pressure on visibility. Much of this activity happens inside automated workflows, so organizations need to be able to see and act quickly when something deviates from expected behavior.

The goal is not to prevent every compromise. It is to contain it before it spreads, especially as some of these attacks are designed to extend their reach through the same systems organizations rely on to build and distribute software. 

![author](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/Justin.png)

Justin Moore, Senior Threat Intelligence Researcher 

[Read more by Justin Moore](https://unit42.paloaltonetworks.com/author/justin-moore)

YouTube

## CISO Unscripted

Supply chain risk has outgrown its original definition. It’s no longer solely about vulnerable code in a vendor’s product; it now spans the open-source libraries developers pull from every day, the SaaS integrations enterprises depend on, and the build pipelines designed to move fast. Richard Emerson, leader of Unit 42’s Reactive Intelligence Team, explains why a single upstream compromise can hit hundreds of downstream environments before a single alert fires, and why the activity is so hard to catch: it looks completely legitimate as it crosses the wire. The conversation covers what zero trust actually means when applied to the software supply chain, and what organizations need to inventory, lock down and monitor before the next bad actor finds the gap.

> “When we looked at the origin of all that malicious activity, we saw that all of those commands were executed by a process of Visual Studio Code. It was a super legit, signed, verified process. Nothing unusual stuck out to us.” 

— Tom Fakterman, Senior Threat Researcher, Palo Alto Networks

Podcast

## Threat Vector

[ ![apple](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/apple-podcast.svg) ](https://podcasts.apple.com/us/podcast/threat-vector-by-palo-alto-networks/id1725324656) [ ![rss feed](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/rss-feed.svg) ](https://feeds.megaphone.fm/unit42threatvector) [ ![spotify](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/spotify.svg) ](https://open.spotify.com/show/676BEZwcsufFf620HdzbUo) [ ![youtube](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/youtube.svg) ](https://www.youtube.com/playlist?list=PLqATPiC_Bcl9U_7PyEdRC_DowIz3d33oj) [ ![overcast](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/overcast.svg) ](https://overcast.fm/itunes1725324656/threat-vector-by-palo-alto-networks)

![podcast default icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/podcast-icon-white.svg)

Play Pause

![podcast default icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/podcast-icon-white.svg)

Hunting Threats in Developer Environments

Seek Slider

15s 30s

volume-slider

_00:00_ _00:00_

## Behind the Research

I sat down with Matt Brady, Sr. Principal Researcher, and Cuong Dinh, Consulting Director, to walk through the BlackFile data theft and extortion activity, and what stood out right away is how little “hacking” is actually involved. There are no exploits here. Just vishing a user, capturing credentials, and logging in through SSO to move through the environment. We talked through how identity becomes the entry point, how access expands once attackers are in, and why so much of this blends in as normal activity. It raises a bigger question: if everything looks legitimate, how do you differentiate between normal and malicious activity?

**Mitch Mayne: **Matt, Cuong, in the BlackFile activity you’re tracking, initial access isn’t coming from exploits. It’s coming through vishing and SSO. What does that shift tell you about how attackers are approaching enterprise environments right now? 

**Matt Brady and Cuong Dinh:** We track BlackFile under the activity cluster CL-CRI-1116. What we’ve observed is that the attackers are logging in via SSO using valid credentials obtained through vishing, not breaking in via exploits. This lines up with what we saw in the [2026 Unit 42 Global Incident Response Report](https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report): identity abuse is becoming one of the most frequent ways attackers get into enterprise environments.

Once they’re authenticated, they can operate inside systems the organization already trusts. They don’t need to exploit a vulnerability or drop malware. They can use legitimate access, workflows, and platforms to move through the environment.

That’s the shift. The attack path is becoming less about breaking into systems and more about abusing the trust already built into them.

**MM: **A lot of this activity looks like legitimate access, like valid credentials, normal workflows. From what you’ve seen, why are these attacks so difficult for organizations to detect in real time? 

**MB/CD:** They aren’t using malware or custom tooling that might set off alerts in traditional security appliances – they’re abusing internal resources and living off the land to fly under the radar.

So nothing they’re doing looks obviously wrong. They’re logging in, opening files, using internal systems—things that employees do every day.

Once they’re in, they know what they’re looking for. They’ll spend time figuring out where sensitive data lives and start pulling it together. That can look like normal access, such as someone grabbing files, moving data, using tools they already have permission to use.

So in the moment, there’s no clear signal that says “this is an attack.” It just looks like benign user activity.

**MM: **If attackers don’t need to break into systems and just need to inherit trust, how should security leaders rethink what they trust across the environment?

**MB/CD:** This forces you to rethink what “trusted” really means. In these cases, the attacker is operating as a trusted user. They’ve logged in, they’ve bypassed MFA, and now they’re operating inside systems exactly the way a legitimate user is supposed to. 

A lot of environments are still too permissive. Once you’re in, there’s broad access across applications and data that isn’t getting revalidated. That’s what enables this threat activity.

So the shift is toward continuously validating that access. Zero trust isn’t optional here. You have to reduce standing privilege, limit what accounts can actually reach, and require stronger, phishing-resistant authentication when something changes, like a new device, new location, or different user behavior.

**MM: **What follow-on attack types are these threat actors using to pressure victims into paying a ransom as a double extortion technique? What does this mean in terms of the importance for the alignment of cyber and physical teams?

**MB/CD:** They’re looking for anything that creates pressure, like customer records, internal communications, sensitive files, and staging it for exfiltration. At that point, they don’t need to encrypt systems. This is prime extortion without encryption, another trend we saw jump in frequency in the 2026 IR Report. The leverage comes from what they’ve taken and what they can do with it.

That’s the shift from traditional ransomware. It’s not about locking you out. It’s about putting you in a position where you have to respond because of the impact if that data is exposed, such as loss of consumer trust and regulatory fines.

In some cases, they’re taking it even further. We’ve seen swatting of executives and other employees as an added technique to pay ransoms–such as making false emergency calls to send law enforcement to their homes. That’s where this moves beyond the cyber domain and becomes a physical security issue. Cyber teams must be partnering with their physical security peers to ensure executive and employee monitoring is in place. Because now the pressure isn’t just in the digital domain, it’s also in the physical world. 

![author](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/Matt.png)

Matt Brady, Senior Principal Researcher 

[Read more by Matt Brady](https://unit42.paloaltonetworks.com/author/matt-brady)

![author](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/Final-Cuong-Dinh.png)

Cuong Dinh, Consulting Director 

[Read more by Cuong Dinh](https://unit42.paloaltonetworks.com/author/cuong-dinh)

## Editor's Outlook

The common thread this month: trust is the vulnerability.

Software updates, dependencies, SaaS integrations, identity systems–these are all built for speed and friction-free execution. That’s the upside. But it’s also why they scale quickly when compromised. The activity looks legitimate. The blast radius expands fast.

This is structural, not perimeter. Stop treating trust as static. Know what’s connected, what it can touch, and what it’s doing in real time. Enforce least privilege everywhere, including identities, integrations,and build pipelines. Assume breach in the systems designed to distribute and execute.

The new baseline: control how trust propagates through your environment, or someone else will.

![author image](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/Mitch-Insights-1.png)

Mitch Mayne, Principal, Security Research 

×

## Previous Bulletins

![Pictorial representation of an interview between two individuals containing a microphone, their hands, a wooden table, and a white brick wall.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/01_Interview_Category_1505x922-718x440.jpg)

November, 2025 #### [Unit 42 Threat Bulletin – November 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/november-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/november-2025/ "Unit 42 Threat Bulletin – November 2025")

![Pictorial representation of a smiling woman on her phone set against a dark background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/03_Opinion_Category_1505x922-718x440.jpg)

October, 2025 #### [Unit 42 Threat Bulletin - October 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/october-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/october-2025/ "Unit 42 Threat Bulletin - October 2025")

![Dynamic digital waves in orange and blue.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/01_General_Overview_1920x900-786x368.jpg)

September, 2025 #### [Unit 42 Threat Bulletin – September 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/september-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/september-2025/ "Unit 42 Threat Bulletin – September 2025")

![Pictorial representation of the ARC OT lab.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/1A_unit-42_ARC_web_hero_desktop_1920x900-786x368.jpg)

June, 2026 #### [OT Threat Research ](https://unit42.paloaltonetworks.com/threat-bulletin/ot-threat-research-arc/)

  * [Operational Technology](https://unit42.paloaltonetworks.com/tag/operational-technology/ "Operational Technology")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/ot-threat-research-arc/ "OT Threat Research")

![Pictorial representation of hands typing on a keyboard.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/01_Opinion_Overview_1920x900-786x368.jpg)

April, 2026 #### [Unit 42 Threat Bulletin - April 2026 ](https://unit42.paloaltonetworks.com/threat-bulletin/april-2026/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/april-2026/ "Unit 42 Threat Bulletin - April 2026")

![Pictorial representation of Airstalk malware. A person typing on a laptop with digital graphics of binary code and light beams emanating from the screen, representing data transfer or cyber activity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/07_Security-Technology_Category_1920x900-786x368.jpg)

March, 2026 #### [Unit 42 Threat Bulletin - March 2026 ](https://unit42.paloaltonetworks.com/threat-bulletin/march-2026/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/march-2026/ "Unit 42 Threat Bulletin - March 2026")

![Pictorial representation of a man with glasses viewing a monitor of code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/03_Interview_Category_1505x922-718x440.jpg)

February, 2026 #### [Unit 42 Threat Bulletin - February 2026 ](https://unit42.paloaltonetworks.com/threat-bulletin/february-2026/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/february-2026/ "Unit 42 Threat Bulletin - February 2026")

![Pictorial representation of an interview between two individuals containing a microphone, their hands, a wooden table, and a white brick wall.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/01_Interview_Category_1505x922-718x440.jpg)

November, 2025 #### [Unit 42 Threat Bulletin – November 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/november-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/november-2025/ "Unit 42 Threat Bulletin – November 2025")

![Pictorial representation of a smiling woman on her phone set against a dark background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/03_Opinion_Category_1505x922-718x440.jpg)

October, 2025 #### [Unit 42 Threat Bulletin - October 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/october-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/october-2025/ "Unit 42 Threat Bulletin - October 2025")

![Dynamic digital waves in orange and blue.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/01_General_Overview_1920x900-786x368.jpg)

September, 2025 #### [Unit 42 Threat Bulletin – September 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/september-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/september-2025/ "Unit 42 Threat Bulletin – September 2025")

![Pictorial representation of the ARC OT lab.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/1A_unit-42_ARC_web_hero_desktop_1920x900-786x368.jpg)

June, 2026 #### [OT Threat Research ](https://unit42.paloaltonetworks.com/threat-bulletin/ot-threat-research-arc/)

  * [Operational Technology](https://unit42.paloaltonetworks.com/tag/operational-technology/ "Operational Technology")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/ot-threat-research-arc/ "OT Threat Research")

![Pictorial representation of hands typing on a keyboard.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/01_Opinion_Overview_1920x900-786x368.jpg)

April, 2026 #### [Unit 42 Threat Bulletin - April 2026 ](https://unit42.paloaltonetworks.com/threat-bulletin/april-2026/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/april-2026/ "Unit 42 Threat Bulletin - April 2026")

![Pictorial representation of Airstalk malware. A person typing on a laptop with digital graphics of binary code and light beams emanating from the screen, representing data transfer or cyber activity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/07_Security-Technology_Category_1920x900-786x368.jpg)

March, 2026 #### [Unit 42 Threat Bulletin - March 2026 ](https://unit42.paloaltonetworks.com/threat-bulletin/march-2026/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/march-2026/ "Unit 42 Threat Bulletin - March 2026")

![Pictorial representation of a man with glasses viewing a monitor of code.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/03_Interview_Category_1505x922-718x440.jpg)

February, 2026 #### [Unit 42 Threat Bulletin - February 2026 ](https://unit42.paloaltonetworks.com/threat-bulletin/february-2026/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/february-2026/ "Unit 42 Threat Bulletin - February 2026")

![Pictorial representation of an interview between two individuals containing a microphone, their hands, a wooden table, and a white brick wall.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/11/01_Interview_Category_1505x922-718x440.jpg)

November, 2025 #### [Unit 42 Threat Bulletin – November 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/november-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/november-2025/ "Unit 42 Threat Bulletin – November 2025")

![Pictorial representation of a smiling woman on her phone set against a dark background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/03_Opinion_Category_1505x922-718x440.jpg)

October, 2025 #### [Unit 42 Threat Bulletin - October 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/october-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/october-2025/ "Unit 42 Threat Bulletin - October 2025")

![Dynamic digital waves in orange and blue.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/01_General_Overview_1920x900-786x368.jpg)

September, 2025 #### [Unit 42 Threat Bulletin – September 2025 ](https://unit42.paloaltonetworks.com/threat-bulletin/september-2025/)

[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-bulletin/september-2025/ "Unit 42 Threat Bulletin – September 2025")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)