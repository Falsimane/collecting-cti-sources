# Analyste CTI et LLM: exemple d'une collaboration fructueuse

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/analyste-cti-et-llm/
- **Date :** 2026-06-05

---

In a recent CTI investigation, we worked on a sophisticated campaign targeting blockchain developers through a fake recruitment process. The scenario was convincing: a fake company, a carefully prepared GitHub repository, a seemingly legitimate project, and then several mechanisms of compromise hidden within the development environment. Upon opening the repository in VS Code, a malicious task could execute automatically. Simultaneously, a booby-trapped npm dependency introduced a second infection vector. Behind this facade, the analysis revealed a multi-stage staging chain, ephemeral JWTs, behavioral filtering on the C2 side, and an infrastructure designed to resist investigation.

It is precisely in this type of case that the use of an LLM becomes interesting. Not because it "does the investigation for" the analyst, but because it allows for the much faster absorption of a significant amount of technical material, particularly in **static code analysis**. Thus, the model made it possible to quickly examine a large GitHub repository, displaying 574 commits, and to isolate four malicious artifacts hidden in configuration and dependency files within 40 minutes: `tasks.json`, `settings.json`, `package.json` And `config.env.example`.

![](https://www.intrinsec.com/wp-content/uploads/2026/06/image-8-1024x667.png)

The LLM then analyzed these codes and produced, in just over an hour, **a complete mapping of the attack chain** : identification of the three infection vectors, reconstruction of the four-step staging chain, extraction of IOCs, decoding of the base64-encoded C2 URL, partial deobfuscation of `parser.js` (obfuscation algorithm obfuscator.io, array rotation 62 iterations, custom base64 alphabet, XOR key). This cover would have taken a full day for a human analyst working alone.

AI also ensured the entirety of the **structured writing** The plan is divided into 13 sections, includes MITRE ATT&CK mapping across 30 techniques, IOC tables, cryptographic hashes, and reporting recommendations. The final deliverable—this report—is a direct result of this work.

## The analyst decides, the LLM executes

But what about the human element in this story? **Its role is that of steering, decision-making and interpretation.** Thus, it was the analyst who identified the suspicious deposit and decided to inspect it. And it is the analyst who guides the LLM through the tasks to be performed, via continuous prompt engineering. Each reformulation of instructions, each course correction, each investigative decision is a pilot interaction whose quality directly determines the quality of the AI outputs.

At certain points, the analyst's skillful interpretation helped resolve issues. For example, during attempts to reconstruct the staging chain, the AI interpreted the failure of HTTP requests to the stage-2 C2 server as an IP block—a plausible but incorrect hypothesis. It was the human analyst who identified the true cause: the C2 server was filtering on the User-Agent, requiring a hash in npm format. This type of error is characteristic of the limitations of probabilistic reasoning in AI. **Humans have managed to break free from the framework**.

In the end, in this example, the LLM and the analyst will have "worked" roughly the same amount of time, three hours each. Therefore, in the space of six hours, it was possible to produce a report that would likely have required two to three days of work alone.

This experiment validates a collaborative model where AI acts as a **execution capacity multiplier** and not as a replacement for the analyst. In this model:

  * The CTI analyst doesn't waste time reading 50 JavaScript files line by line — the AI does it.
  * The CTI analyst retains the role of **decision-maker** What deserves further investigation? Which hypothesis is false? When should a lead be abandoned?
  * THE **prompt engineering** becomes an analytical skill in its own right — correctly structuring a question for AI is as intellectually demanding as formulating the right investigative hypothesis.
  * AI failures (like the blacklisted IP hypothesis) are not bugs — they are signals. They indicate areas where the model reaches the limits of its training space, and therefore precisely where human expertise is irreplaceable.



## Conclusion

This experiment validates a collaborative model where AI acts as a multiplier of execution capacity, not as a replacement for the analyst. Six hours of combined work for a deliverable that would have required two to three hours alone: the gain is real, but it depends entirely on the quality of human guidance.

This is, in fact, the most important lesson of this case. The AI's error—interpreting User-Agent filtering as IP blocking—is not a flaw to be corrected, but a boundary to be mapped. It indicates precisely where probabilistic reasoning ends and where human expertise remains irreplaceable. When used correctly, LLM does not dilute the CTI analyst's role; it shifts its focus to what matters most: deciding what to investigate, recognizing a false hypothesis, and knowing when to step outside the established framework.

## To go further

This case study illustrates our approach: AI accelerates execution, but the analyst leads, interprets, and makes the final decision. This human oversight is what makes the difference in threat intelligence. Our CTI team supports organizations over the long term—anticipating threats, conducting dedicated investigations, and delivering actionable insights. 

[Discover our support services](https://www.intrinsec.com/en/cyber-threat-intelligence/)

#### Articles by category 

Select a category News Vulnerability notice Analysis Report CERT SSI Council Cyber Threat Intelligence Engineering Safety Assessment Event Partnership Research and Development Red Teaming part-time CISO Soc as a Service SOC Operational Security Testimonials Penetration test Threat Intelligence Report Security Watch