# 2020 Verizon Data Breach Report: Top Themes and Takeaways | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/05/19/dancing-with-the-breaches-a-quick-step-through-the-2020-verizon-data-breach-investigations-report-dbir/
- **Date :** 2025-06-02

---

The [Verizon Data Breach Investigations Report (DBIR)](https://enterprise.verizon.com/resources/reports/dbir/) has been released, reporting its annual summary of (this year) 32,002 incidents, 3,950 of which are confirmed breaches. As in years past, the Rapid7 Labs team has you covered with our annual Reader’s Guide and cherry-picked smattering of key insights.

We had the privilege, once again, to contribute anonymized incident and breach data from our [Managed Detection and Response (MDR) Services](/services/managed-detection-and-response-mdr/) and have been waiting with bated breath for the release of the complete report.

Let’s get started!

## How to get the most out of the Verizon DBIR

Topping out at 119 pages, the 2020 DBIR is more of a seven-course meal than a quick bite at your favorite fast-food restaurant. Many new CISOs and information security professionals may find the entire report a bit difficult to digest at first. With that in mind, here are some suggestions for how to absorb the contents to get the information nutrition you need to help shape your security programs:

### Cheat to win

There is an _invaluable_ cheat sheet right at the beginning of the report, and we highly suggest keeping those pages handy as you work your way through each section, since tables, text, and charts will use them frequently, and the DBIR team is precise to a fault. Quick tip: Your PDF reader will let you copy those pages out and keep them on a second screen/desktop for reference. Our industry has tons of jargon, and this will let you keep concepts straight. 

If those 1.5 pages are too much to skim, just make sure you’re on the lookout for two words near every table or chart:

  * **Incident:** “A security event that compromises the integrity, confidentiality or availability of an information asset.”
  * **Breach:** “An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party).”



### Read the Methodology section

There are two reasons for this. First, you really do want to know how the sausage is made, since you’re likely going to use portions of this report to defend budget requests—plus, there are always those you’ll likely come into contact with who may not represent the data in the report as faithfully as you might. You’ll be armed when someone tries to call BS on you and you can, in turn, call BS on those who attempt to misuse the report. 

The second one is that it contains links to high-resolution versions of all the figures in the report, so you can pepper your internal PowerPoint justification slides with super-crisp images instead of hastily selected screenshots.

### Be the captain of your industry

![image--3--2.png](https://www.rapid7.com/cdn/images/blt0e769f6fdf1be81c/683de7f5a38fc5d56303227c/image--3--2.png)

The top industries have concise snapshots that are invaluable since they cover a more useful (to you) set of incidents and breaches than the corpus as a whole might. So, diving in there first will help ground you and provide some solid context for the rest of the report. One recurring feature of the report that we 💙are these vulnerability dwell time charts, which will let you benchmark your own performance against that of your peers (and will either be something to brag about or use as fodder for improvement plans).

The DBIR team has also helped you out a bit and repeated some definitions throughout the industry sections to help avoid page flipping.

### Plan your path through the topics

The report covers everything from details on threat actors to what those actors did, as well as deep dives on topics such as malware, ransomware, and the plethora of errors that were in the report this year. Ideally, you should first study the sections that track with what your own organization had to deal with in 2019, then move on to the remainder of the categories.

Keep in mind that the main goal for organizations (versus, say, vendors) is to leave the DBIR properly informed so you can improve your program and gain some ground on attackers. Reading it is not a race, and you should very much consider coming back to the report in the coming months, as you’ll likely find new insights to use throughout the year.

## Key themes in the 2020 DBIR

### Reducing dwell time is not enough

The increased use of specialty firms (like us!) to handle incidents and breaches has helped close the gap on what was a dismal statistic regarding how long it takes to detect and contain an incident or breach. We’ll avoid cutting and pasting _every_ chart from the DBIR and just look at the breaches version of the time-to-discover:

![image--5-.png](https://www.rapid7.com/cdn/images/bltb7dc1b4dd1d048eb/683de80eff6aa9d5a40eaa9f/image--5-.png)

Astute/regular readers will see that this tracks well with our own MDR statistics and is a bit of good-if-not-great news in an otherwise doom-filled _document_. Unfortunately, it doesn’t take much time for ransomware (which has its own DBIR section) to inflict painful damage in an organization. So, as we defenders have gotten better at detection, this speed improvement is likely one big reason ransomware has been so prevalent and will likely continue to be even more prevalent for quite some time.

### Watch those buckets!

As previously noted, the 2020 DBIR is full of errors. No, the incredibly talented DBIR team did not mess up—we did. Or, rather, workers who were entrusted to keep secrets secret did.

![image--4-.png](https://www.rapid7.com/cdn/images/blt32fb80fb8fbdd28f/683de82b590d7f6fc9de1df0/image--4-.png)

Misconfigured S3 buckets and wide-open databases have replaced the “sent SSN/medical info to the wrong customer/patient” publishing errors of previous years (ah, the good ol’ days), which again tracks well with what we measure daily with [Project Sonar](/research/project-sonar/). Massive service exposure is a problem for organizations of every shape and size and should be something you can get a handle on without spending too much of your ever-diminishing budgets. If you do need some extra lift, our new teammates from DivvyCloud have got you covered.

### Zombie credentials never die

![figure-20-21.png](https://www.rapid7.com/cdn/images/blt3f6d3d28281bebfb/683de8443a1c5aa1f44baace/figure-20-21.png)

You know how it seems like there’s been security news about a credential dump like every week for the past three years? Well, that’s because there kind of has been, and attackers have amassed billions of credentials to try against your web apps, Citrix servers, VPN gateways, remote desktops (RDP), and more. Just before May, the Rapid7 Labs team finally saw a significant reduction in SQL Server credential stuffing attacks, with upward of 60 million unique login combinations (combination of username, password, and other connection login setup parameters) _per day_ , though we’re hoping it’s not just another brief respite, as we saw in February.

![image--8-.png](https://www.rapid7.com/cdn/images/bltbf7031de2153fb6b/683de85e6b437b9dc14fa861/image--8-.png)

If you haven’t done so already, your organization absolutely needs to have a transition plan in place **this year** to migrate to multi-factor authentication for all critical services. This is for both employees and customers/patients. We’re just starting to make some serious headway on many fronts but, for some reason, plain ol’ username- and password-based credential logins are not being retired fast enough.

First, level up your safety messaging and help your workforce understand they absolutely should not use their work email when registering for personal services (like genealogy sites, which we mention because corporate email addresses were ridiculously prevalent in the MyHeritage.com breach). Then, let them know that regardless of the context, they should never reuse a password, ever (_ever_).

Finally, pick a multi-factor, risk-based solution and start implementing it. More detailed advice is beyond the scope of this post, but you can hit up [[email protected]](/cdn-cgi/l/email-protection#addfc8dec8ccdfcec5eddfccddc4c99a83cec2c0) if you want more pointers.

The bottom line is that once these credentials die in a breach, they don’t remain dead for long. They’ll keep coming back to life again and again in regular zombie surges at your doorstep.

## Looking forward to 2021!

There are more insights left to glean in the 2020 DBIR, but we’re especially looking forward to 2021 (which is ~12 years away in COVID-time). Why? Well, a great deal has changed when it comes to “work” in 2020, and we’re super-curious as to gain a more complete picture (than our MDR incident and breach data) how attackers have adjusted. We will be so bold as to say that if you can learn some lessons from the 2020 DBIR and make some improvements, you can do your part to ensure your organization will not be part of the 2021 corpus.

If you have questions about the 2020 DBIR, don’t hesitate to drop a note in the comments or (preferably) to [[email protected]](/cdn-cgi/l/email-protection#65170016000417060d251704150c01524b060a08). Happy reading!

## Article tags

  * [Verizon DBIR](/blog/tag/verizon-dbir/)