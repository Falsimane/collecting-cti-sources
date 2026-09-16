# The 2016 Verizon DBIR Summary - The Defender's Perspective | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/04/29/the-2016-verizon-data-breach-investigations-report-the-defenders-perspective/
- **Date :** 2025-06-02

---

Verizon has released the [report](https://www.verizon.com/business/resources/reports/dbir/) of their annual Data Breach Investigations Report (DBIR). Their crack team of researchers have, once again, produced one of the most respected, data-driven reports in cyber security, sifting through submissions from 67 contributors and taking a deep dive into 64,000 incidents—and nearly 2,300 breaches—to help provide insight on what our adversaries are up to and how successful they've been.

The DBIR is a highly anticipated research project and has valuable information for many groups. Policy makers use it to defend legislation; pundits and media use it to crank out scary articles; other researchers and academics take the insights in the report and identify new avenues to explore; and vendors quickly identify product and services areas that are aligned with the major findings. Yet, the data in the report is of paramount import to _defenders_. With over 80 pages to wade through, we thought it might be helpful to provide some way-points that you could use to navigate through this year's breach and incident map.

## Bigger is…Better?

There are a couple "gotchas" with data submitted to the DBIR team. The first is that a big chunk of data comes from the U.S. public sector where there are mandatory reporting laws, regulations, and requirements. The second is the YUGE number of _Unknowns_. The DBIR acknowledges this, and it's still valuable to look at the data when there _are_ _"knowns"_ even with this grey (okay, ours is green below) blob of uncertainty in the mix. You can easily find your industry in DBIR Tables 1 & 2 (pages 3 & 4) and if we pivot on that data we can see the distribution of the percentage of incidents that are breaches:

![2016-verizon-data-breach-report-fig-1-1.png](https://www.rapid7.com/cdn/images/blt58cb85f9ea72ac54/683ddea82a7686d713bc83cd/2016-verizon-data-breach-report-fig-1-1.png)

We've removed the "Public (92)" industry from this set to get a better sense of what's happening across general industries. For the DBIR, _there were more submissions of incidents with confirmed data disclosure for smaller organizations than large_ (i.e. be careful out there SMBs), but there's also a big pile of _Unknowns_ :

![2016-verizon-data-breach-report-fig-2-1.png](https://www.rapid7.com/cdn/images/blt28d52de6bfc0e5c9/683dded32a76860dd2bc83df/2016-verizon-data-breach-report-fig-2-1.png)

We can also take another, discrete view of this by industry:

![2016-verizon-data-breach-report-fig-3-1.png](https://www.rapid7.com/cdn/images/blt6c8d10ce14db0aa1/683ddefbcc60421eba20671e/2016-verizon-data-breach-report-fig-3-1.png)

As defenders, you should be reading the report with an eye for your industry, size, and other characteristics to help build up _your_ threat profiles and help benchmark _your_ security program. Take your incident to breach ratio (you _are_ using VERIS to record and track everything from anti-virus hits to full on breaches, _right_?) and compare it to the corresponding industry/size.

## The Single Most Popular Valuable Chart In The World! (for defenders)

When it comes right down to it, you're usually fighting an economic battle with your adversaries. This year's report, Figure 3 (page 7) shows that the motivations are still primarily financial and that Hacking, Malware and Social are the weapons of choice for attackers. We'll dive into that in a bit, but we need to introduce our take on DBIR Figure 8 (page 10) before continuing:

![2016-verizon-data-breach-report-fig-4-1.png](https://www.rapid7.com/cdn/images/bltfb9cef64f1de97de/683ddf212cfe327511dc15c8/2016-verizon-data-breach-report-fig-4-1.png)

We smoothed out the rough edges from the 2016 Verizon Data Breach Report to figure to paint a somewhat clearer picture of the overall trends, and used a complex statistical transformation (i.e. subtraction) to just focus on the smoothed gap:

![2016-verizon-data-breach-report-fig-5-1.png](https://www.rapid7.com/cdn/images/blte56a5023336fdc61/683ddf4dff6aa9536a0ea7f2/2016-verizon-data-breach-report-fig-5-1.png)

Remember, the DBIR data is a biased sample from the overall population of cyber security incidents and breaches that occur and every statistical transformation introduces more uncertainty along the way. That means your takeaway from "Part Deux" should be _"we're not getting any better"_ vs _"THE DETECTION DEFICIT TOPPED 75% FOR THE FIRST TIME IN HISTORY!"_

So, our adversaries are accomplishing their goals in _days or less at an ever-quickening success rate_ while defenders are just not keeping up at all. Before we can understand what we need to do to reverse these trends, we need to see what the attackers are doing. We took the data from DBIR Figure 6 (page 9) and pulled out the top threat actions for each year, then filtered the result to the areas that match both the major threat action categories and the areas of concern that Rapid7 customers have a keen focus on:

![2016-verizon-data-breach-report-fig-6-1.png](https://www.rapid7.com/cdn/images/bltdf0161125fd9290c/683ddf71c26e07b3ad28e6f8/2016-verizon-data-breach-report-fig-6-1.png) Some key takeaways:

  * Malware and hacking events dropping C2s are up
  * Key loggers are making a comeback (this may be an artifact of the heavy influence of Dridex in the DBIR data set this year)
  * Malware-based exfiltration is back to previously seen levels
  * Phishing is pretty much holding steady, which is most likely supporting the use of compromised credentials (which is trending up)



Endpoint monitoring, kicking up your awareness programs, and watching out for wonky user account behavior would be wise things to prioritize based on this data.

### Not all Cut-and-Dridex

The Verizon Data Breach Report mentions [Dridex](https://www.theguardian.com/technology/2015/oct/14/what-is-dridex-how-can-i-stay-safe) _13 times_ and was very up front about the bias it introduced in the report. So, how can you interpret the data with "DrideRx" prescription lenses? Rapid7's Analytic Response Team notes that Dridex campaigns involve:

  * Phishing
  * Endpoint malware drops
  * Establishment of command and control (C2) on the endpoint
  * Harvesting credentials and shipping them back to the C2 servers



This means that—at a minimum—the data behind the Data Breach Investigations Report, Figures 6-8 & 15-22, impacted the overall findings and Verizon itself warns about broad interpretations of the _Web App Attacks_ category:

"Hundreds of breaches involving social attacks on customers, followed by the Dridex malware and subsequent use of credentials captured by keyloggers, dominate the actions."

So, when interpreting the results, keep an eye out for the above components and factor in the Dridex component before tweaking your security program too much in one direction or another.

## Who has your back?

When reading any report, one should always check to make sure the data presented doesn't conflict with itself. One way to add a validation to the above detection deficit is to look at DBIR Figure 9 (page 11) which shows (when known) how breaches were discovered over time. We can simplify this view as well:

![2016-verizon-data-breach-report-fig-7-1.png](https://www.rapid7.com/cdn/images/blt5c755943b6a9ff3e/683ddf944b2b7f0ad5e160f3/2016-verizon-data-breach-report-fig-7-1.png) In the significant majority of cases, defenders have law enforcement agencies (like the FBI in the United States) and other external parties to "thank" for letting them know they've been pwnd. As our figure shows, we stopped being able to watch our own backs half a decade ago and have yet to recover. This should be a wake-up call to defenders to focus on identifying how attackers are getting into their organizations and instrumenting better ways to detect their actions.

Are you:

  * Identifying critical assets and access points?
  * Monitoring the right things (or anything) on your endpoints?
  * Getting the right logs into the right places for analysis and action?
  * Deploying honeypots to catch activity that should not be happening?



If not, these may be things you need to re-prioritize in order to force the attackers to invest more time and resources to accomplish their goals (remember, this is an battle of economics).

## Are You Feeling Vulnerable?

Attackers are continuing to use stolen credentials at an alarming rate and they obtain these credentials through both social engineering and the exploitation of vulnerabilities. Similarly, lateral movement within an organization also relies—in part—on exploiting vulnerabilities. DBIR Figure 13 (page 16) shows that as a group, defenders are staying on top of current and year-minus-one vulnerabilities fairly well:

![dbirfig13.png](https://www.rapid7.com/cdn/images/blt1a2586496366a2ab/683ddfb98ac17c652f29ad8c/dbirfig13.png)

We're still having issues patching or mitigating older vulnerabilities, many of which have tried-and-true exploits that will work _juuuust_ fine. Leaving these attack points exposed is not helping your economic battle with your adversaries, as letting them rely on past R&D means they have more time and opportunity. How can you get the upper-hand?

  * Maintain situational awareness when it comes to vulnerabilities (i.e. scan with a plan)
  * Develop a strategy patching with a holistic focus, not just react to "Patch Tuesday"
  * Don't dismiss mitigation. There are legitimate technical and logistic reasons that can make patching difficult. Work on developing a playbook of mitigation strategies you can rely on when these types of vulnerabilities arise.



"Threat intelligence" was a noticeably absent topic in the 2016 DBIR, but we feel that it can play a key role when it comes to defending your organization when vulnerabilities are present. Your vuln management, server/app management, and security operations teams should be working in tandem to know where vulnerabilities still exist and to monitor and block malicious activity that is associated with targets that are still vulnerable. This is one of the best ways to utilize all those threat intel feeds you have gathering dust in your SIEM.

## There and Back Again

This post outlined just a few of the interesting markers on your path through the Verizon Data Breach Report. Keep a watchful eye on the Rapid7 Community for more insight into other critical areas of the report and where we can help you address the key issues facing your organization.

## Article tags

  * [Verizon DBIR](/blog/tag/verizon-dbir/)
  * [Research](/blog/tag/research/)