# Measuring AI Security: What MCP Exposure Really Shows

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-measuring-ai-security-mcp-exposure/
- **Date :** 2026-02-10

---

The conversation around [AI security](https://www.rapid7.com/fundamentals/artificial-intelligence/) is full of anxiety. Every week, new headlines warn of jailbreaks, [prompt injection](/fundamentals/prompt-injection-attack/), agents gone rogue, and the rise of LLM-enabled cybercrime. It’s easy to come away with the impression that AI is fundamentally uncontrollable and dangerous, and therefore something we need to lock down before it gets out of hand.

But as a security practitioner, I wasn’t convinced. Most of these warnings are based on hypothetical examples or carefully engineered demos. They raise important questions, but rarely answer the most basic one: _What does the real attack surface of today’s AI systems actually look like?_

So instead of offering another opinion, I ran the numbers.

## The method: Focused, real-world measurement

To ground the conversation in reality, I focused on MCP, the [Model Context Protocol](https://www.rapid7.com/fundamentals/model-context-protocol-mcp/). This framework is widely used to help language models interact with tools, APIs, and external systems. It’s open source, replicated across many environments, and built for practical integration. That makes it an ideal test case for understanding actual exposure.

No adversarial prompting. No artificial exploits. Just a measurement of what real MCP servers expose. We used SDK import analysis to locate active repositories, filtered out those that wouldn’t run, and examined the tool schemas to understand what each was capable of.

## What the data tells us

The MCP servers that met our criteria showed a familiar pattern. They exposed well-understood primitives used throughout modern software systems.

**Observed capability classes:**

  * Filesystem access

  * HTTP requests

  * Database queries

  * Local script or process execution

  * Orchestration and tool chaining

  * Read-only API search




These are not exotic capabilities unique to AI. They’re already embedded in cloud automation, infrastructure-as-code, and modern DevOps stacks. MCP simply gives them structure.

### The frequency of high-severity risk is low

One of the most unexpected findings was the rarity of arbitrary code execution. Despite warnings in the media, this turned out to be the least common capability among all operational MCP servers analyzed.

This matters. It suggests that real-world deployments of AI tooling are not as reckless as some narratives claim. The most common issues are the ones we’ve known for years: weak defaults, excessive permissions, and poor input handling. There’s no mystery there (and that’s encouraging).

### Where the real risk builds: Composition

The problem arises when those primitives are combined. Individually, most of the MCP servers we studied were low risk. But when orchestration enters the picture, the attack surface expands.

**Some real-world examples we observed:**

  * HTTP fetch + filesystem write = persistence or content injection

  * Database query + orchestration = stealthy exfiltration

  * Filesystem write + planning = poisoned output or config hijacking

  * HTTP + planning + execution = multi-stage agent attacks




These combinations reflect what adversaries already do in non-AI environments. MCP just reduces friction in putting the pieces together.

## A critical counterpoint: The 'best effort' reality

The focus on constraining the model via schema and architecture is essential for '[secure by design](https://www.rapid7.com/blog/post/2024/05/15/ai-trust-risk-and-security-management-why-tackle-them-now/),' yet a critical counterpoint must be considered as the industry evolves: We may not be able to stop many insecure AI applications (e.g., those built on architectures like OpenClaw or Claude Code) from shipping with insecure design choices. Similarly, the insecure design path for AI could force security teams to rely on non-deterministic, 'best effort' prompt injection defenses to prevent data exfiltration and remote code execution, rather than influencing developers toward inherently secure application design.

While the secure boundary _is_ the schema, and we must influence application developers to adopt secure-by-design principles, the future suggests there will be many cases where this influence fails. This means security leaders must also prepare for a hybrid reality of championing architectural security while also building and operating robust, best effort runtime defenses to manage the fallout from the inevitable wave of insecure AI applications.

## A shift in where security happens

As we embed AI deeper into operational systems, the control points change. Historically, we validated inputs at the UI layer, enforced roles through IAM, and wrapped logic in application code.

With AI agents, those controls now live in:

  * The orchestration layer

  * Tool composition workflows

  * Schema contracts

  * Execution sandboxes




Security needs to follow the shift. That means auditing tool chains, setting strict schema policies, isolating execution contexts, and applying existing practices like least privilege and defense in depth to this new architecture.

## What security teams should do now

Security and architecture leaders can start applying pressure in the right places today:

  * **Map AI tooling to known primitives**  
Don’t treat these systems as unknowns. Most expose capabilities like file handling, HTTP fetches, or basic shell commands - all of which are familiar territory for teams leveraging threat intelligence effectively.

  * **Assess schema design before worrying about prompts**  
The schema defines what tools the AI can call and how. Poorly scoped parameters, such as unbounded URLs or file paths, are far more dangerous than clever prompts.

  * **Limit orchestration where possible**  
Composability increases risk. If orchestration is required, monitor it like critical automation infrastructure.

  * **Audit your environment for capability sprawl**  
Look for AI-connected services that may expose multiple sensitive capabilities together. Risk scales when these tools are combined.

  * **Apply existing enterprise controls**  
[ Network segmentation](https://www.rapid7.com/fundamentals/network-segmentation/), credential scoping, logging, and behavioral detections still work. Least privilege access is especially relevant in AI-integrated environments where tool chaining can escalate access unintentionally. AI requires adaptation, not reinvention.




## Understanding the risk of AI without the hype

This blog condenses findings from my recent research, where I set out to answer a straightforward question: what are AI systems actually exposing in the real world today? Instead of relying on hypotheticals or fear-driven narratives, I looked at real, runnable Model Context Protocol (MCP) servers and measured their exposed capabilities and architectural design.

If you're looking for the technical deep dive, including methodology, data sets, and schema-level breakdowns, you can read the original research published on [HackerNoon](https://hackernoon.com/everyone-says-ai-is-insecure-so-i-measured-it). You can also explore more of our ongoing threat analysis and security research on the[ Rapid7 Research Hub.](https://www.rapid7.com/research/)

The bottom line: AI introduces complexity and scale, but the fundamental security principles remain the same. The real challenge is whether security teams can adapt traditional controls to new environments and influence developers toward inherently secure application design, rather than being forced to rely on non-deterministic, 'best effort' defenses like prompt injection mitigation.

## Article tags

  * [Artificial Intelligence](/blog/tag/artificial-intelligence/)
  * [Research](/blog/tag/research/)