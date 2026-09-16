# Comment l'IA facilite la vie des acteurs de la menace

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/ia-offensive-llm-cyberattaques/
- **Date :** 2026-07-02

---

## From phishing to AI-driven intrusion: a critical shift

The integration of Large Language Models (LLMs) into attackers' workflows is no longer limited to simply generating phishing attacks. We are now witnessing a critical shift: AI is becoming a technical execution engine that drastically lowers the bar for conducting intrusions of varying complexity. By acting as a real-time expert assistant, LLM enables **operators with limited skills to overcome their technical shortcomings and operate at a level of sophistication previously reserved for seasoned players**. Two recent use cases, documented by [OALabs](https://research.openanalysis.net/claude/codex/hacking/ai%20hacking/llm/redteam/policy%20violation/2026/06/16/compromised-claude-hacking.html) And [Dragos](https://www.dragos.com/blog/ai-assisted-ics-attack-water-utility) with prompt journals as a key element, perfectly illustrate this trajectory, going from opportunistic use to the industrialization of the attack.

### Offensive AI: When a novice operator pilots a full-scale intrusion with Claude

Analysis of the logs of an attacker based in Ethiopia reveals a modus operandi where the AI (primarily Claude) not only suggests code but also manages the entire intrusion. To circumvent LLM safeguards, the operator used a well-known technique: disguising its actions as a legitimate red team operation, complete with a "Pentest Report." Ultimately, Claude only became truly concerned about these requests when they crossed the line, such as helping to monetize the stolen assets.

![Prompt malveillant pour contourner les rèlges d'usage du LLM](https://www.intrinsec.com/wp-content/uploads/2026/07/image-1024x238.png)Malicious prompt to bypass LLM usage rules (source: OALabs)

Overall, **Prompts are often vague** ("recon this", "get a shell"), allowing the agent to orchestrate vulnerability research, the writing of exploits based on public CVEs, and access validation. What is striking in this case is the operator's limited technical expertise, compensated by the LLM's ability to translate simple intentions into precise technical actions. The attacker was able to compromise around fifteen companies by using AI to automate reconnaissance and exfiltration, proving that **Mastering an AI agent is now sufficient to conduct successful intrusion campaigns without being an expert in cybersecurity.**.

However, this intellectual crutch didn't protect him from a series of OPSEC errors that allowed OALabs to link this attacker to a name and geographic location. It must be said that the attacker used the same Claude instance to carry out cyber intrusions and update his LinkedIn profile, which isn't exactly a good idea. And this reveals his true nature: that of a beginner.

### **OT/SCADA Targeting: The Industrialization of AI-Assisted Attacks**

While the OALabs case demonstrates tactical use, the intrusion into a Mexican water authority analyzed by Dragos reveals a structural escalation. The adversary used Claude to design a complete attack framework, dubbed "BACKUPOSINT v9.0 APEX PREDATOR." It comprises 17,000 lines of Python code and 49 specialized modules (enumeration, credential harvesting, Active Directory querying, etc.).

Even more significantly: AI enabled the attacker **to identify and prioritize critical OT-type assets** (SCADA/IIoT vNode management interfaces) without prior knowledge of industrial systems. The LLM analyzed the environment, identified the strategic value of the OT interface, and generated targeted password lists to attempt to bridge the IT-OT boundary. This represents a significant leap forward: **AI makes it possible to attack niche areas (ICS/OT) that previously required years of experience and specialized expertise.**

![Réponse d'un LLM lors d'une opération d'intrusion informatique](https://www.intrinsec.com/wp-content/uploads/2026/07/image-1-1024x454.png)The LLM indicates to the malicious actor a particularly interesting OT target (source: Dragos)

One caveat must be added. While this framework seems impressive at first glance, it is actually quite noisy and would only allow the compromise of highly exposed or poorly protected resources. According to Dragos, Claude did not develop _«"a new or particularly effective offensive arsenal"»_ , but he rather _«"concentrated and accelerated a wide range of capabilities"»_. This doesn't necessarily mean that Claude wouldn't be capable of doing better, but it also depends on the human oversight. In this specific case, we can assume that the prompts were probably not precise enough or that certain tests in a lab environment were not carried out.

### A new paradigm: attackers "augmented" by AI rather than "sophisticated" ones«

These examples confirm that **AI acts as a skills accelerator**. Whether for an opportunistic attacker or a group seeking to target critical infrastructure, LLM reduces tool development time and the need for specialized expertise. For defenders, this means that the threat no longer comes solely from inherently sophisticated actors, but from AI-augmented actors capable of conducting relatively precise operations with minimal effort.

## **How Intrinsec protects you against the rise of offensive AI**

### **Test before the attacker**

Our teams [Audit and offensive security](https://www.intrinsec.com/en/red-team/) We simulate "augmented" attack scenarios, using the same frameworks and agents as adversaries. We test the resilience of your environments—including your IT-OT gateways—to identify and remediate critical access paths before an AI-assisted operator discovers them. The lowering threshold for technical expertise necessitates an agile defensive response capable of countering attacks whose speed and precision are now exponentially increased by LLM.

### **Detect manipulation in real time**

Faced with attackers who automate reconnaissance and exploitation, static analysis is obsolete. Our [SOC and our MDR services](https://www.intrinsec.com/en/soc-securite-operationnelle/) deploy contextual and behavioral monitoring, capable of detecting weak signals of an agent-driven intrusion, even when the tools used are generic or polymorphic.

### **Anticipating changes in operating methods**

Our team [Cyber Threat Intelligence](https://www.intrinsec.com/en/cti/) We continuously analyze the emergence of new AI-generated attack frameworks and the vulnerabilities of autonomous agents. We transform this intelligence into actionable detection rules to protect your most critical assets.

The strength of our approach lies in **the interconnection of these areas of expertise** The CTI identifies new offensive AI tools, the audit and offensive security teams validate their impact on your infrastructure, and the SOC provides continuous monitoring. A complete cycle to counter a threat that is constantly accelerating.

**[Let's discuss your security challenges in relation to AI.](https://www.intrinsec.com/en/securite-intelligence-artificielle/)**

#### Articles by category 

Select a category News Vulnerability notice Analysis Report CERT SSI Council Cyber Threat Intelligence Engineering Safety Assessment Event Partnership Research and Development Red Teaming part-time CISO Soc as a Service SOC Operational Security Testimonials Penetration test Threat Intelligence Report Security Watch