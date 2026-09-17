# Defending Against APTs: A Learning Exercise with Kimsuky | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/07/16/defending-against-apts-a-learning-exercise-with-kimsuky/
- **Date :** 2025-06-02

---

The “evolving threat landscape” is a term we often hear within webinars and presentations taking place across the cybersecurity industry. Such a catch-all term is intended to capture the litany of threat groups and their evolving tactics, but in many ways it fails to truly acknowledge the growth in their capabilities. This is particularly true of APT groups who have for years demonstrated a remarkable increase in their capabilities to remain undetected and carry out instructions from those orchestrating the broader campaigns under which they operate.

The latest [research paper](/globalassets/_pdfs/whitepaperguide/rapid7-Kimsukys-Phishing-and-Payload-Tactics_wp.pdf) coming out of Rapid7 Labs examines the tactics of North Korea’s Kimsuky threat group. It is published to serve as a learning on the evolving capabilities of a highly adept and industrious threat group, and, more importantly, to provide the necessary insights for supporting security teams in the implementation of defensive strategies.

In this post I will cover some of the key insights to be found in this new research.

## Targeting capabilities

The paper details Kimsuky’s delivery method as largely focused on email, but of course, a key component of this is determining who to target and what the most effective lure is likely to be. Historically, this threat group has been particularly successful at the latter with considerable time and expense taken to identify “individuals” on whom their attention should be focused.

It is all too easy to shrug and comment on the need for security awareness as the panacea control to prevent all such initial entry vectors. The reality is that we all remain susceptible, given the right hook. And the ability of this threat group to target and compromise individuals around the globe reveals an alarming level of capability to elicit a response from victims.

## Evolving technical capabilities

As detailed earlier this year, we are seeing technical innovation borne from the need to evade security controls within the victim environment. In this instance we detail the use of .LNK file payloads derived from an LNK builder proof of concept. This, however, is just the tip of the iceberg, with many other payloads delivered using alternate methods.

What this reveals — with a very high degree of confidence — is that there is an element to continual tooling improvements. Much like a component of this group dedicated to strong OSINT (as above), there is likely a subset of the group dedicated to technical innovation as a means to evade detection.

This allows the group to develop an arsenal of malware, for example, that can be used at will; but more importantly, it can be built upon and developed as defensive techniques improve.

## Always on the move

The historic dependency upon reputations as a vehicle to identify malicious infrastructure is fast becoming less than effective. Politely put — and as demonstrated within the paper — we see Kimsuky establish infrastructure across the globe but quickly leverage new domains as needed. This is just another example of how this group understands and develops the ability to quickly move as it identifies new targets.

Subsequently, the publication provides tactical, actionable insights into the defensive measures that can be taken. For example, full details of coverage are included within the paper, as well as persistence measures undertaken by the threat actor, which are a critical indicator of compromise during retroactive threat hunts. All TTPs detailed within the paper are also incorporated into detection coverage across the Rapid7 portfolio, as detailed within the final section.

[Click here to read the research paper now.](/globalassets/_pdfs/whitepaperguide/rapid7-Kimsukys-Phishing-and-Payload-Tactics_wp.pdf)

## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)