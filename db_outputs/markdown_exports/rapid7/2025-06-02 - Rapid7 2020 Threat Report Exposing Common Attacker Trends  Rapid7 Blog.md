# Rapid7 2020 Threat Report: Exposing Common Attacker Trends | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/03/03/rapid7-2020-threat-report-exposing-common-attacker-trends/
- **Date :** 2025-06-02

---

If you joined Rapid7 at RSAC 2020 just a few days ago, you probably caught wind of Rapid7’s end-of-year threat report. I’m happy to announce that now that the RSAC dust has settled, we’ve released that report [here](/research/report/2020-threat-report/).

In case you don’t quite have the time to read Rapid7’s entire wrap-up of the threats and incidents we saw in customer networks over the course of 2019, here is the shortest of short stories: Organizations continue to host vulnerable, internet-exposed systems that are being targeted by attackers. Simultaneously, attackers are targeting valid user accounts as their preferred method for breaching an environment. These are the two essential sides of the cyber-defense coin that your enterprise should be focused on.

To make the report easier to read and to bring some real, actionable advice to the table, we’ve split up this report into three sections:

### 1\. Focus on threat telemetry

In this section, we make the case that, yes indeed, we’ve hit new-normal high levels of EternalBlue scanning and exploit attempts. While the rate of change has pretty much leveled off, there are still hundreds of thousands of exposed Windows SMB servers left on the internet.

We also saw similar stories for other protocols, such as UPnP, RDP, and a rather significant jump in Microsoft SQL Server (port 1433). Today is the second best time to find your own points of exposure using your favorite asset and [vulnerability management solution](/solutions/vulnerability-management/). (What’s the best time? Yesterday!)

### 2\. Focus on detection telemetry

Here, we present how we go about detecting threats in the environment, discuss attacker dwell time (how long attackers can go without being noticed), and frame up pretty much everything in terms of the wildly popular [MITRE ATT&CK Framework](/fundamentals/mitre-attack-framework/). If you’re at all concerned with incident response as part of your day-to-day, you’ll want to take a look at these figures and analysis.

### 3\. Focus on recommendations

Given what we know attackers are after and how they go after those targets, we offer some succinct, actionable, and weirdly non-vendor-specific advice. (Sorry, Rapid7 sales and marketing! We love you!) Sometimes, it's more effective to take a proactive approach, and sometimes, a reactive strategy is more appropriate; it all depends on the threat and your situation. In all cases though, we make the case that you should be seeking out those low-effort, high-return mitigation and remediation actions, and automating those away so you can move on to the more complicated (fun) stuff.

Anyway, we have some pretty great corroborative data presented full threat report, but hey, if you want to just take the word of some rando security blogger like me, I won't stop you. Well, I'll try to talk you out of it, a little bit. I'm pretty thrilled with this most recent iteration of the Rapid7 Threat Report; I think it does a great job at laying out both the problem space and the solution space, and it should help start some conversations with your management and your individual contributors about how we can all get down to the business of securing the internet. After all, if you're reading this, you certainly work here on the internet, but our kids spend pretty much their whole lives here. So, don't do it for me. Think of the children. Won't you?

## Article tags

  * [Research](/blog/tag/research/)
  * [Threat Intel](/blog/tag/threat-intel/)