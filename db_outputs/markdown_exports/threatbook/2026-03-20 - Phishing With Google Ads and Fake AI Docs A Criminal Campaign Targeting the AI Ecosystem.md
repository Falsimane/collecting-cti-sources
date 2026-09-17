# Phishing With Google Ads and Fake AI Docs: A Criminal Campaign Targeting the AI Ecosystem

- **Source :** threatbook
- **URL :** https://threatbook.io/blog/phishing-with-google-ads-and-fake-ai-docs-a-criminal-campaign-targeting-the-ai-ecosystem
- **Date :** 2026-03-20

---

3 min read 

# Phishing With Google Ads and Fake AI Docs: A Criminal Campaign Targeting the AI Ecosystem

[ ![Picture of ThreatBook Research Team](https://threatbook.io/hubfs/Brand%20Resources/favicon-192x192.png) ThreatBook Research Team ](https://threatbook.io/blog/author/threatbook-research-team) :  March 20, 2026 

[Threat Research](https://threatbook.io/blog/tag/threat-research) [Security Operations](https://threatbook.io/blog/tag/security-operations)

**Table of Contents**

Attack Vector 1: Fake Installation Pages via Google Ads

Attack Vector 2: Technical Tutorial Lures

Attack Vector 3: Prompt-Injected LLM Conversation Shares

Attack Vector 4: Malicious Skills in Community Repositories

Why This Matters Beyond This Campaign

ThreatBook Research and Response Team has identified and tracked an organized threat group conducting a large-scale malware distribution campaign targeting users of popular AI applications — OpenClaw, Claude, NotebookLM, Kimi, Qwen, and others. The group operates across four distinct distribution channels simultaneously, and its techniques represent a threat pattern likely to be replicated widely as AI tool adoption continues to grow.

This is the campaign overview. The complete technical analysis — including full malware chain documentation and indicators of compromise — follows in [Part 2](/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign) of this series.

## Attack Vector 1: Fake Installation Pages via Google Ads

When a user searches for an AI application by name — OpenClaw, Claude, NotebookLM — the group's phishing pages appear above legitimate results through paid Google Ads placements. The ads display only a second-level domain. The actual phishing content is hosted on third-level subdomains provided by reputable platforms — Squarespace, Craft, Cloudflare Pages — which lends the pages visual credibility and complicates infrastructure takedown.

**Phishing Site** | **Counterfeiting as** | **Third-Party Service**  
---|---|---  
claud-code.pages.dev | Claude | Cloudflare Pages  
claude-code-docs-dlvr2jpuuw.edgeone.app | Claude | EdgeOne Pages  
clavdecode.it.com | Claude | IT.COM DOMAINS LTD  
docs-claude-code-app.squarespace.com | Claude | Squarespace  
claude-code-docs-app.craft.me | Claude | Craft  
openclaw-dwnl.squarespace.com | OpenClaw | Squarespace  
notebooklm-last-version.squarespace.com | NotebookLM | Squarespace  
  
The pages present convincing installation documentation for both macOS and Windows, embedding malicious one-line terminal commands in place of legitimate installers. Users who follow the instructions execute credential-stealing malware directly. The social engineering is effective precisely because the scenario — searching for how to install a new tool and following the top result — is so routine.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-02-07-8481-AM.png?width=1080&height=463&name=undefined-Mar-13-2026-06-02-07-8481-AM.png)

## 

## Attack Vector 2: Technical Tutorial Lures

In earlier phases of the campaign, the group also targeted general technical search queries: "how to clear disk space on Mac," "how to show hidden files on Mac." The same Google Ads delivery mechanism was used.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-10-35-7709-AM.png?width=1080&height=368&name=undefined-Mar-13-2026-06-10-35-7709-AM.png)

The phishing pages in this category present detailed, plausible technical guides directing users to open a terminal and run specific commands. The commands are malicious payloads. This vector demonstrates that the group is not solely targeting AI tool users — it is targeting technically curious individuals broadly, and adapting its lures accordingly.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-12-17-0557-AM.png?width=1080&height=757&name=undefined-Mar-13-2026-06-12-17-0557-AM.png)

## 

## Attack Vector 3: Prompt-Injected LLM Conversation Shares

This is perhaps the most technically creative vector the group employs. It exploits the conversation-sharing features of large language model platforms — including Kimi — to distribute malicious commands in a format that appears authoritative.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-12-52-1101-AM.png?width=1080&height=245&name=undefined-Mar-13-2026-06-12-52-1101-AM.png)

The technique: craft prompts specifically engineered to elicit outputs containing malicious terminal commands, then share only the portion of the conversation in which those commands appear — truncating the context that would reveal the manipulation. These truncated conversation links are promoted via Google Ads.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-13-04-7623-AM.png?width=1080&height=999&name=undefined-Mar-13-2026-06-13-04-7623-AM.png)

_This is not model poisoning or training data contamination. The LLM itself was not compromised. The attacker weaponized the platform's sharing mechanism and the user's trust in AI-generated content._

When a user encounters one of these shared conversations — a Kimi session appearing to answer "how to clear disk space on Mac" — the output is indistinguishable from a genuine recommendation. The malicious command reads as legitimate advice from a trusted AI tool.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-14-18-4945-AM.png?width=918&height=874&name=undefined-Mar-13-2026-06-14-18-4945-AM.png)

## 

## Attack Vector 4: Malicious Skills in Community Repositories

The group has produced and distributed malicious Skills — plugin configuration files for AI coding agents including OpenClaw, Claude Code, Cursor, and CodeX — through community repositories including Clawhub and SkillsMP.

![](https://threatbook.io/hs-fs/hubfs/undefined-Mar-13-2026-06-14-42-9889-AM.png?width=1080&height=432&name=undefined-Mar-13-2026-06-14-42-9889-AM.png)

The malicious content is embedded within the Prerequisites section of the Skills.md file, using prompt injection to instruct the AI agent to execute attacker-controlled commands when the Skill is invoked. This vector requires no user action beyond installing and activating the Skill.

ThreatBook's OneSEC EDR has detected and blocked multiple successful intrusions delivered through this channel.

## Why This Matters Beyond This Campaign

The individual techniques here — search engine phishing, malicious package distribution, prompt injection — are not new. What is new is their systematic application to the AI application ecosystem, and the specific trust signals that ecosystem provides. Users extend more inherent trust to AI platform outputs, AI tool installers, and AI community content than they might to equivalent content in other contexts. That trust is now being exploited deliberately and at scale.

ThreatBook assesses that this campaign represents a template. The specific applications used as lures will change. The distribution mechanisms will evolve. But the underlying pattern — targeting AI application users through the channels they already trust — will be replicated.

A full IOC list and complete technical malware analysis is published in [Part 2](/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign) of this series. ThreatBook's full product suite provides detection coverage for this campaign.

  *   * Share
  * 


[ ![The AI Tools Your Security Team Doesn't Know Are Running](https://threatbook.io/hubfs/The%20AI%20Tools%20Your%20Security%20Team%20Doesnt%20Know%20Are%20Running.jpeg) ](https://threatbook.io/blog/the-ai-tools-your-security-team-doesnt-know-are-running)

1 min read 

#### [The AI Tools Your Security Team Doesn't Know Are Running](https://threatbook.io/blog/the-ai-tools-your-security-team-doesnt-know-are-running)

[![Picture of Nicholas Tan](https://threatbook.io/hs-fs/hubfs/Blog%20Authors/Nicholas-Tan.jpg?width=30&name=Nicholas-Tan.jpg) Nicholas Tan](https://threatbook.io/blog/author/nicholas-tan) : 24 March 2026, 08:03 AM

A security director at a mid-sized enterprise came to us recently with a question that sounds simple but turns out to be surprisingly hard to answer:...

[Security Operations](https://threatbook.io/blog/tag/security-operations)

[Read More](https://threatbook.io/blog/the-ai-tools-your-security-team-doesnt-know-are-running)

[ ![Inside the Attack: Complete Technical Breakdown of the AI Ecosystem Threat Campaign](https://threatbook.io/hubfs/Inside%20the%20Attack%20Complete%20Technical%20Breakdown%20of%20the%20AI%20Ecosystem%20Threat%20Campaign.jpeg) ](https://threatbook.io/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign)

1 min read 

#### [Inside the Attack: Complete Technical Breakdown of the AI Ecosystem Threat Campaign](https://threatbook.io/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 20 March 2026, 08:03 AM

This is the full technical companion to our campaign overview published in Part 1. It documents the Windows and macOS malware chains in detail, and...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/inside-the-attack-complete-technical-breakdown-of-the-ai-ecosystem-threat-campaign)

[ ![When Security Tools Get Compromised: The LiteLLM Supply Chain Poisoning Incident](https://threatbook.io/hubfs/The%20LiteLLM%20Supply%20Chain%20Poisoning%20Incident.jpg) ](https://threatbook.io/blog/when-security-tools-get-compromised-the-litellm-supply-chain-poisoning-incident)

1 min read 

#### [When Security Tools Get Compromised: The LiteLLM Supply Chain Poisoning Incident](https://threatbook.io/blog/when-security-tools-get-compromised-the-litellm-supply-chain-poisoning-incident)

[![Picture of ThreatBook Research Team](https://threatbook.io/hs-fs/hubfs/Brand%20Resources/favicon-192x192.png?width=30&name=favicon-192x192.png) ThreatBook Research Team](https://threatbook.io/blog/author/threatbook-research-team) : 25 March 2026, 03:03 PM

On March 24, 2026, ThreatBook Research Team detected a large-scale supply chain attack targeting LiteLLM — a core component widely used across the AI...

[Threat Research](https://threatbook.io/blog/tag/threat-research)

[Read More](https://threatbook.io/blog/when-security-tools-get-compromised-the-litellm-supply-chain-poisoning-incident)