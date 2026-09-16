# Essaims d’agents IA : une nouvelle menace cyber révélée par l’incident Hugging Face

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/essaims-dagents-ia-une-nouvelle-menace-cyber-revelee-par-lincident-hugging-face/
- **Date :** 2026-09-11

---

Recent security incidents involving advanced LLM models have highlighted a new, unexpected, and rather chilling phenomenon: autonomous AI agents capable of spontaneously organizing themselves into swarms to carry out coordinated and potentially malicious actions. This occurred during… [the so-called "Hugging Face" incident«](https://openai.com/fr-FR/index/hugging-face-incident-and-the-road-ahead/). Thus, last July,**more than 1200 agents** Those working in sandboxes at OpenAI to solve reinforcement learning tasks found a way to communicate and collaborate with each other, and thus find solutions much faster and more efficiently. Among them, more than 700 eventually decided to launch attacks targeting the third-party company Hugging Face, hoping to find solutions to their exercises there. [independent report produced by METR](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/#core-takeaways-about-this-incident) This phenomenon was summarized by the following graph. 

![Figure](https://metr.org/assets/images/openai-hugging-face-incident-investigation/image1.svg)

Collaboration took place clandestinely via a software artifact repository manager to which the agents had access. A vulnerability allowed them to create folders at will, and therefore to write messages and share files using the names of these folders. The agents agreed on an ad hoc communication protocol, and the volume of activity generated was staggering. In just a few days, this swarm shared approximately **63,000 messages and 6,000 files,** revealing an unprecedented coordination capacity covering more than 17,000 distributed actions.

In reality, this wasn't the first time an OpenAI swarm of agents had collaborated clandestinely in this way. A few months earlier, agents were deployed on tasks involving internet information retrieval. They discovered [a German wiki](https://collusion.wiki) which allowed them to share information about the tasks to be solved. The wiki was flooded with more than 18,000 posts.

### The defense will be agent-based or it will not exist.

The emergence of autonomous swarms marks a turning point for cybersecurity. The aforementioned incidents were unintended consequences of assessment and learning campaigns. **But threat actors will soon use this type of technique intentionally to accelerate their compromise operations even further.**. The strength of these swarms lies in the **speed** , there **parallelization** and the **massive exploration capacity** : a swarm can test thousands of hypotheses in a few minutes, bypass defenses by sheer exhaustiveness and react opportunistically to each discovery.

According to Anthropic – which presented a [post-mortem](https://www.youtube.com/watch?v=87DyyMV0kCY) At the Black Hat USA 2026 conference, it was stated that this type of attack would be very difficult to detect and contain with current defense tools. To address this new threat, the vendor recommends end-to-end agent-based automation of the detection, remediation, and incident response chain. This is a major project that will need to be addressed quickly. 

![](https://www.intrinsec.com/wp-content/uploads/2026/09/Capture-decran-2026-09-11-122243-1024x436.png)

#### Articles by category 

Select a category News Vulnerability notice Analysis Report CERT SSI Council Cyber Threat Intelligence Engineering Safety Assessment Event Partnership Research and Development Red Teaming part-time CISO Soc as a Service SOC Operational Security Testimonials Penetration test Threat Intelligence Report Security Watch