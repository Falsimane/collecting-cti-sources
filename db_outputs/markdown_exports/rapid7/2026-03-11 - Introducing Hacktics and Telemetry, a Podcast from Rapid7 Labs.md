# Introducing Hacktics and Telemetry, a Podcast from Rapid7 Labs

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-introducing-hacktics-telemetry-podcast-rapid7-labs/
- **Date :** 2026-03-11

---

If you spend your days building, shipping, defending, or fixing systems, you already know how this goes. A new technique shows up in a research thread, someone drops a _“has anyone checked if we’re exposed?”_ comment, and suddenly you’re juggling risk, patches, logging gaps, and whatever tool is in the blast radius this week.

That day-to-day reality is why Rapid7 Labs is launching [Hacktics and Telemetry](https://youtu.be/lIQ-Wy6q4bI), a bi-weekly video and audio podcast with episodes built to fit into a lunch break or a commute. It’s hosted by Rapid7's [Douglas McKee](https://www.linkedin.com/in/douglas-mckee-77460677/), bringing to the pod years of deep technical and leadership experience, then co-hosted by [Jonah ‘CryptoCat’ Burgess](https://www.linkedin.com/in/cryptocat/) – a strong researcher with a solid pulse on the cybersecurity community.

The format stays consistent on purpose. Each episode starts with a scan of what’s emerging, shifts into a guest conversation, then closes with a short segment that ties the story back to mitigation and tooling. The goal is simple: move past theory, show what’s happening with real examples, and leave you with something you can act on.

## Episode 1: OpenClaw Risks, RCEs, and Metasploit Pro Updates

Doug and Jonah open by digging into two AI-centric stories from the past week. The first is PhoneLeak, described as data exfiltration in Gemini via phone call. It’s the kind of uncomfortable example that forces practical questions: how do you defend against mobile clickjacking when it's disguised as a routine CAPTCHA? When an AI assistant has deep extensions into a user's workspace, how do you prevent malicious prompts from quietly accessing sensitive data like 2FA codes? And perhaps most importantly, how do defenders anticipate and monitor for bizarre, out-of-the-box exfiltration methods—like an AI bypassing SMS confirmations to leak data via DTMF tones on a phone call?

The second story comes from the other side of the AI conversation: an AI agent reportedly identifying an RCE in BeyondTrust remote support, plus discussion of older privileged remote access versions. More automation can mean faster discovery, which shrinks the window between “interesting finding” and “you need to patch this.” That changes how defenders think about exposure, patch prioritization, and what “good enough” means (and looks like) when it comes to monitoring.

In the guest segment, [Greg Richardson](https://www.linkedin.com/in/gregorypkrichardson/) (Global Advisory CISO & AI Thought Leader, 6 Levers AI) walks through how he uses AI agents in his workflow while keeping control tight. He talks about setting tasks while he sleeps, but the constraints are the point: access is locked down, the agent only touches files he explicitly provides, communication is limited, and token limits help cap the size of any mistake. He also makes a strong case for starting small, with one task at a time, instead of trying to automate dozens of things on day one.

To close out this inaugural episode, the team hits on a SolarWinds Help Desk vulnerability, then shares a quick look at [Metasploit Pro 5.0 updates](https://www.rapid7.com/blog/post/pt-announcing-metasploit-pro-5-penetration-testing-evolving/) – including more granular payload selection and a walkthrough of the new UI.

If your idea of useful content includes threat trade-offs, concrete mitigations, and a bit of candid “how this actually plays out,” you’re in the right place.

Catch the full episode below:

⠀

## Article tags

  * [Podcast](/blog/tag/podcast/)
  * [Hacking](/blog/tag/hacking/)
  * [Emerging Threats](/blog/tag/emerging-threats/)