# What We Learned from 2025's Biggest Hacks: 4 Takeaways - TeamT5

- **Source :** teamt5
- **URL :** https://teamt5.org/en/posts/what-we-learned-from-2025-s-biggest-hacks-4-takeaways/
- **Date :** 2025-12-17

---

Products & Services

SubscribeRSS

# What We Learned from 2025's Biggest Hacks: 4 Takeaways

2025.12.17Product Management

Share: 

## The Offense is Moving at AI Speed

When we talk about cybersecurity, the conversation often defaults to defense: patch your systems, enable multi-factor authentication, and encrypt your data. While these measures are crucial, recent intelligence from late 2024 and 2025 reveals a starkly different reality. Cyberattacks have fundamentally changed. The offense is now operating at the speed of AI.

To build a modern defense, you must first understand the modern offense. This principle has never been more relevant, as threat actors leverage artificial intelligence to shrink their attack cycles from weeks to minutes.

No defense is meaningful without first understanding the offense.

This post cuts through the noise to analyze the new threat landscape. Based on intelligence from recent state-sponsored campaigns and advanced threat groups, we will explore how this shift manifests in four key areas: the weaponization of trust in our supply chains, the erosion of human intuition through deepfakes, the systematic acceleration of the entire attack lifecycle, and the industrialization of geopolitical propaganda.

We’re going to talk 4 cyber threat trend in this article -

  1. Your Biggest Vulnerability Isn't Your Firewall—It's Your Trusted Partners

  2. The Job Interview Might Be with a Deepfake

  3. AI Is Supercharging Every Stage of an Attack

  4. Propaganda Is Now an Automated, AI-Driven Machine




Let’s start.

## 1\. Your Biggest Vulnerability Isn't Your Firewall—It's Your Trusted Partners

In 2025, attackers have shifted their focus from direct infiltration to "weaponizing trust." By compromising a single trusted service provider or an unpatched edge device, threat actors can bypass the robust perimeter defenses of high-value targets.

This strategy was demonstrated in a recent campaign, the Chinese-speaking APT cluster tracked as UAT-7237 exploited unpatched web infrastructure in Taiwan to breach multiple internet-facing servers and repurpose them as persistent footholds in high-value environments[1]. The group’s operations emphasize long-term access using customized open-source tooling and bespoke loaders, illustrating how compromises of foundational web infrastructure can be leveraged to support deeper malicious activity across affected enterprises.

Moreover, reported APT cases across the Asia-Pacific region describe a mix of intrusion techniques, including the abuse of exposed edge devices and remote access infrastructure alongside spear-phishing campaigns delivering malicious files via cloud services and messaging platforms. Several cases involve Taiwan-based organizations, where edge and perimeter systems compromise features, while additional incidents span government, manufacturing, and chemical across Japan and Southeast Asia[2].

## 2\. The Job Interview Might Be with a Deepfake

This weaponization of trust isn't just happening at the network level; it's now targeting the human level with terrifying sophistication, as seen in the rise of AI-driven recruitment scams. North Korean hacking groups like TA444 have engineered an alarming social engineering campaign that combines remote work, cryptocurrency, and AI-generated deepfakes[3].

The process is a masterclass in exploiting human trust with AI:

  1. **Fake Identities** : Hackers use AI tools to generate completely fake but highly believable professional identities, complete with custom resumes and polished LinkedIn profiles.

  2. **Legitimate Front** : They establish fake US shell companies to appear credible, specifically targeting high-value remote workers like cryptocurrency developers.

  3. **The Deepfake Interview** : To build rapport and seal the deal, the hackers conduct job interviews over Zoom. During the video call, the "hiring executive" is an AI-generated deepfake, indistinguishable from a real person.

  4. **The Malware Payload** : After the victim accepts the job offer, they are instructed to install "onboarding software" to get started. This software is actually malware designed to steal credentials and data.




This sophisticated tactic resulted in millions of dollars in stolen cryptocurrency and gave the attackers persistent access to corporate cloud accounts on platforms like AWS and Google Cloud. AI is systematically breaking the human element we rely on to spot scams, erasing the subtle cues that would normally give an imposter away.

## 3\. AI Is Supercharging Every Stage of an Attack

Artificial intelligence is not just another tool in the hacker's arsenal; it is a force multiplier that revolutionizes the entire attack lifecycle, often framed by the Cyber Kill Chain. AI provides four key advantages to attackers: **efficiency, scalability, hyper-personalization, and polymorphism** —the ability to constantly change form to evade detection.

Here is how AI enhances several key stages of a modern cyberattack:

  * **Reconnaissance** : Previously a labor-intensive manual process, reconnaissance is now automated. Attackers use tools like OSINT-GPT[4], which combines Large Language Models (LLMs) with open-source intelligence. This represents a revolution in **efficiency** and **scalability** , generating a detailed, personalized target profile in minutes—a task that used to take weeks.

  * **Weaponization** : Malicious LLMs like WormGPT[5] and FraudGPT[6] dramatically lower the technical barrier for entry into cybercrime. By generating convincing phishing text and attack scripts for non-experts, these tools enable unprecedented scalability for criminal operations.

  * **Delivery** : AI enables **hyper-personalization** in delivery. Not only does it craft more persuasive, context-aware phishing emails, but deepfake video calls are also being used to impersonate executives and trick employees into authorizing fraudulent multi-million dollar wire transfers.

  * **Exploitation** : The gap between a vulnerability's discovery and its weaponization has collapsed to almost zero thanks to Automatic Exploit Generation (AEG). Research on frameworks like PwnGPT showed it nearly doubled the exploit creation success rate from 26.3% to 57.9% (like GPT o1 model)[7]. This rapid weaponization achieves a form of **polymorphism** , as defenses can't keep up with the speed of new threats.

  * **Command & Control (C2)**: To stay hidden and achieve evasion, attackers now route their malicious communications through legitimate AI cloud services. Projects like Claude-C2[8] demonstrate how C2 traffic can be disguised as normal business API calls, making it incredibly difficult for network defenses to detect and achieve the goal of **polymorphism**.




## 4\. Propaganda Is Now an Automated, AI-Driven Machine

AI's impact extends beyond financial crime and corporate espionage into the realm of geopolitical influence and cognitive security. The "GoLaxy files" leak provided an unprecedented look into China's state-sponsored, AI-driven propaganda machine.

This is far more advanced than simple social media bots. The leak exposed the “Tianji” Intelligent Propaganda System, also known as GoPro[9] [10]. What sets this system apart is its scale and automation. GoPro uses generative AI to automate the creation, customization, and distribution of persuasive content across social media platforms with minimal human oversight.

The system has already been operated through a sophisticated, tiered architecture:

  * **GoIN (Intelligent Intelligence Analysis System)** : The "brain" of the operation, consisting of **"Wenqu"** (文曲) for data integration, **"Tianluo"** (天罗) for real-time monitoring, and the **"Magic Mirror"** (魔镜) for cognitive analysis and strategic decision-making.

  * **GoPro ("Tianji" Intelligent Propaganda System)** : A generative AI system that automates the creation, customization, and distribution of persuasive content across social media.

  * **Global Multi-Platform Account Management System** : A large-scale system designed to "nurse" and manage thousands of fake accounts to mimic genuine public discourse.




While the GoLaxy leak provides the technical blueprint, we are also seeing the real-world effects of other similar mechanisms in regional disputes:

  * **Okinawa** : Inauthentic networks on X and linked sites are amplifying Okinawan independence and anti-militarization narratives. Originally targeting Chinese speakers, the activity then uses Japanese-language content to weaponize local grievances, specifically aiming to undermine the Japan–US alliance rather than promoting direct anti-Japan sentiment[11].

  * **Taiwan Election** : During Taiwan’s 2024 election, AI-generated audio and avatars impersonated political figures to spread scandals. While detectable through forensic flaws and contextual absurdities, a coordinated volume produced in under 30 minutes overwhelms fact-checking capacity. This scalability, especially involving foreign subjects where local context is missing, presents a challenge driven by distribution speed rather than technical perfection[12].




## Conclusion: How Do You Defend at the Speed of AI?

Across this year’s biggest breaches, one pattern stands out: **AI has amplified every phase of the attack cycle** , accelerating reconnaissance, sharpening exploitation, and shrinking the defender’s reaction window to almost zero.

In this environment, defense is no longer just about deploying tools or tightening controls. It requires understanding how attackers think, operate, and adapt — especially as they increasingly rely on automation, dark-web resources, and AI-driven capabilities. Only by grasping these shifts can organizations judge real risk, prioritize action, and make confident decisions under pressure.

In the end, these incidents remind us of a simple truth: **No defense is meaningful without first understanding the offense.** Understanding the adversary isn’t optional, it’s the starting point for any defense that aims to hold up in the AI era.

> For podcast version, you may listen here: <https://youtu.be/Il8OH2LYBSQ?si=jKvlzypB9husJ14n>

#### Source:

[1] [The Hacker News, Taiwan Web Servers Breached by UAT-7237 Using Customized Open-Source Hacking Tools, April 2025](https://thehackernews.com/2025/08/taiwan-web-servers-breached-by-uat-7237.html)  
[2] [Day 1, Main Track presentations, JSAC 2025](https://blogs.jpcert.or.jp/en/2025/03/jsac2025day1.html)  
[3] [The Hacker News, 'BlueNoroff Deepfake Zoom Scam', June 2025](https://securelist.com/bluenoroff-apt-campaigns-ghostcall-and-ghosthire/117842/)  
[4] [Tool: OSINT-GPT by estebanpdl (GitHub)](https://github.com/gigz/gpt-osint)  
[5] [The Dual-Use Dilemma of AI: Malicious LLMs](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/)  
[6] [Netenrich Threat Research Team, 'FraudGPT: The Villain Avatar of ChatGPT', July 2023](https://netenrich.com/blog/fraudgpt-the-villain-avatar-of-chatgpt)  
[7] [Peng et al., 'PwnGPT: Automatic Exploit Generation Based on Large Language Models', ACL Anthology, 2025](https://aclanthology.org/2025.acl-long.562/)  
[8] [Tool: Claude-C2 (Proof of Concept) by dmcxblue. For defensive testing only.](https://github.com/dmcxblue/Claude-C2)  
[9] ThreatVision Report: TeamT5, Bi-Weekly Update 2025 September H2  
[10] [The Record by Recorded Future, 'The GoLaxy Papers'](https://therecord.media/golaxy-china-artificial-intelligence-papers)  
[11] [DFRLab, Japan’s technology paradox: the challenge of Chinese disinformation, March 2025](https://dfrlab.org/2025/03/25/japan-tech-chinese-disinformation/)  
[12] [Taiwan FactCheck Center, Seeing is not believing (part II) – AI videos spread during the 2024 presidential election in Taiwan, February 2024](https://en.tfc-taiwan.org.tw/en_tfc_294/)  


2025.12.17Product Management

Share: 

![](https://teamt5.org/en/posts/what-we-learned-from-2025-s-biggest-hacks-4-takeaways/)