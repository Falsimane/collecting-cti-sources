# Chrysalis, Notepad++, and Supply Chain Risk: What it Means, and What to Do Next

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-chrysalis-notepad-supply-chain-risk-next-steps/
- **Date :** 2026-02-05

---

When Rapid7 published its [analysis of the Chrysalis backdoor](https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/) linked to a compromise of Notepad++ update infrastructure, it raised understandable questions from customers and security teams. The investigation showed that attackers did not exploit a flaw in the application itself. Instead, they compromised the hosting infrastructure used to deliver updates, allowing a highly targeted group to selectively distribute a previously undocumented backdoor associated with the Lotus Blossom APT.

Subsequent reporting from outlets including [BleepingComputer](https://www.bleepingcomputer.com/news/security/notepad-plus-plus-update-feature-hijacked-by-chinese-state-hackers-for-months/), [The Register](https://www.theregister.com/2026/02/02/notepad_plusplus_intrusion/), [SecurityWeek](https://www.securityweek.com/notepad-supply-chain-hack-conducted-by-china-via-hosting-provider/), and [The Hacker News](https://thehackernews.com/2026/02/notepad-official-update-mechanism.html) has helped clarify the scope of the incident. What’s clear is that this was a supply chain attack against distribution infrastructure, not source code. The attackers maintained access for months, redirected update traffic selectively, and limited delivery of the Chrysalis payload to specific targets, helping them stay hidden and focused on espionage rather than mass compromise.

## What does the Notepad++ incident mean?

This incident highlights how modern supply chain attacks have evolved. Rather than targeting application code, attackers abused shared hosting infrastructure and weaknesses in update verification to quietly deliver malware. The broader takeaway is that supply chain risk now extends well beyond build systems and repositories. Update mechanisms, hosting providers, and distribution paths have become attractive targets, especially when they sit outside an organization’s direct control.

## Was Notepad++ itself compromised?

Based on public statements from the Notepad++ maintainer and independent reporting, there is no evidence that the application’s source code or core development process was compromised. The risk stemmed from the update delivery infrastructure, reinforcing that even trusted software can become a delivery mechanism when upstream systems are abused.

## Who was behind the Chrysalis backdoor & Notepad++ attack?

Rapid7 was the first to publish attribution linking this activity to Lotus Blossom, a Chinese state-aligned advanced persistent threat (APT) group. Based on our analysis, we assess with moderate confidence that this group is responsible for the Notepad++ infrastructure compromise and the deployment of the [Chrysalis backdoor.](https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/)

Lotus Blossom has been active since at least 2009 and is known for long-running espionage campaigns targeting government, telecommunications, aviation, critical infrastructure, and media organiations, primarily across Southeast Asia, and more recently, Latin America.

The tactics, tooling, and infrastructure used in this campaign - including the abuse of update infrastructure, the use of selective targeting, and the deployment of custom malware, are consistent with the group’s historical tradecraft. As with any attribution, this conclusion is based on observed behaviors and intelligence correlations, not a single, definitive indicator.

## What should organizations do right now?

Based on what we know today, there are several immediate actions organizations should take:

  * **Check and update Notepad++ installations.** Ensure any instances are running the latest version, which includes improved certificate and signature verification.

  * **Review historical telemetry.** Even though attacker infrastructure has been taken down, organizations should scan logs and environments going back to **October 2025** for [indicators of compromise](https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/) associated with this campaign.

  * **Hunt, don’t just scan.** This activity was selective and low‑volume. Absence of alerts does not guarantee absence of compromise.

  * **Use available intelligence.** Rapid7 Intelligence Hub customers have access to the Chrysalis campaign intelligence, along with follow‑up indicators provided by partners such as Kaspersky, to support targeted hunting across endpoints and network telemetry.




## Why does this matter beyond Notepad++?

This incident is a case study in how trust is exploited in modern environments. The attackers didn’t rely on zero days or noisy malware. They abused update workflows, hosting relationships, and assumptions about trusted software. That same approach applies across countless tools and platforms used daily inside enterprise environments.

It also reinforces a broader trend we’ve seen over the last year: attackers are patient, selective, and focused on long‑term access rather than immediate impact. That has implications for detection strategies, incident response planning, and supply chain risk management.

## What does this mean for software supply chain security?

For defenders, this incident reinforces several lessons:

  * Supply chain security must include distribution and hosting infrastructure, not just source code.

  * Update mechanisms should enforce strong signature and metadata validation by default.

  * Shared hosting environments represent an often overlooked risk, especially for widely deployed tools.

  * Trust in software must be continuously validated, not assumed.




The Chrysalis incident is not just about a single tool or a single campaign. It reflects a broader shift in how advanced threat actors think about access, persistence, and trust. Software supply chains are no longer just a development concern. They are an operational and security concern that extends into hosting providers, update mechanisms, and the assumptions organizations make about what is “safe.”

As attackers continue to favor selective targeting and long‑term access over noisy, large‑scale compromise, defenders need to adapt accordingly. That means moving beyond basic scanning, validating trust continuously, and treating update and distribution infrastructure as part of the attack surface.

## Learn more: Watch the full Chrysalis debrief webinar

If you’d like to hear directly from the researchers behind this discovery, watch the full [Chrysalis: Inside the Supply Chain Compromise of Notepad++ webinar](https://www.brighttalk.com/webcast/10457/661975?utm_source=blog&utm_medium=webcast&utm_content=blog-2-chrysalis-registration&utm_campaign=global-mdr-2026-q1-webinar-prospect-eng), now available on BrightTALK. In this detailed session, Christian Beek (Senior Director, Threat Analytics) and Steve Edwards (Director, Threat Intel & Detection Engineering) walk through the full attack chain, from initial compromise to malware behavior, attribution to Lotus Blossom, and what organizations can do right now to assess exposure and strengthen supply chain security. [[Watch Now]](https://www.brighttalk.com/webcast/10457/661975?utm_source=blog&utm_medium=webcast&utm_content=blog-2-chrysalis-registration&utm_campaign=global-mdr-2026-q1-webinar-prospect-eng)

## Article tags

  * [Emerging Threats](/blog/tag/emerging-threats/)
  * [Threat Intel](/blog/tag/threat-intel/)
  * [Research](/blog/tag/research/)