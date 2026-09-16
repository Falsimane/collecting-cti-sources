# Pwn2Own Berlin 2026: On the Ground with ZDI's Biggest AI Showdown Yet

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/f/pwn2own-berlin-2026.html
- **Date :** 2026-06-01

---

Exploits & Vulnerabilities

# Pwn2Own Berlin 2026: On the Ground With TrendAI™ ZDI's Biggest AI Showdown Yet

47 zero-days fell at Pwn2Own Berlin 2026 for US$1,298,250 in payouts. TrendAI™ was on the ground all three days — here's what we saw. 

By: Scott Graham 2026/06/01 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key takeaways

  * In Pwn2Own Berlin, researchers found 47 unique zero-days across ten target categories, with payouts totaling US$1,298,250, a new event record.
  * AI sub-categories (Coding Agents, Local Inference, AI Databases, NVIDIA) dominated the first day. Products including OpenAI Codex, LiteLLM, LM Studio, and NVIDIA Megatron Bridge all fell, each exploited at the boundary where the AI product unconditionally trusts an external tool or protocol (the "trust boundary" problem).
  * Classic enterprise bugs persisted. Microsoft Exchange (SYSTEM RCE), SharePoint (pre-authentication RCE), and Edge (four-bug sandbox escape) all fell to well-understood vulnerability classes. VMware ESXi produced a cross-tenant guest-to-host escape with multi-tenant infrastructure implications.
  * TrendAI™ shipped nine TrendAI™ TippingPoint™ filters by May 19 (ahead of vendor patches), covering LiteLLM, Edge, Exchange, and SharePoint vulnerabilities. Endpoint-layer detection via TrendAI Vision One™ is the recommended control for AI-category vulnerabilities where wire-level inspection is not viable.__



# The contest: what it is, and what happened in Berlin

## What is Pwn2Own?

Pwn2Own is the world’s most prestigious hacking competition, run by the TrendAI™ Zero Day Initiative™ (ZDI), the world's largest vendor-agnostic bug bounty program. Now in its 19th year, the contest invites security researchers to register, develop working exploits against fully patched, production versions of widely deployed software, and then demonstrate these exploits live on stage during the three-day event. Vendors are notified in advance of the target categories but not the specific vulnerabilities, with the intention that by the time a bug is demonstrated on stage, it is genuinely unknown to the world.

The rules are structured to reward both novelty and complexity. Each successful demonstration earns the contestant cash and "Master of Pwn" points. At the end of the competition, the team or individual with the most points is crowned the Master of Pwn and receives, along with their prize money, the unique Master of Pwn jacket for that event.

All the vulnerabilities demonstrated at Pwn2Own are then disclosed to the affected vendors, who have 90 days to issue patches before TrendAI™ ZDI publishes the full technical details. In the meantime, our security teams work to develop threat detection and mitigation coverage for the demonstrated vulnerabilities, providing TrendAI™ customers a layer of protection during the window between disclosure and vendor patch.

This coordinated model is central to TrendAI™ ZDI's mission: the contest finds and fixes critical vulnerabilities through a structured mechanism, protecting customers before attackers can exploit these flaws.

## Pwn2Own Berlin 2026

The 2026 competition was [colocated with OffensiveCon in Berlin](https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026), marking the second consecutive year that TrendAI™ ZDI has brought Pwn2Own to Germany. This year, the event was co-sponsored by Amazon Web Services (AWS), a partnership that allowed TrendAI™ ZDI to offer increased rewards for bugs in Firecracker.

The contest hit maximum capacity for the first time in its history, and scheduling limits forced TrendAI™ ZDI to close submissions ahead of the planned deadline. As we will discuss in more detail in part 2, this is indicative of the changes that [AI agents](https://www.trendmicro.com/en_us/what-is/ai.html) are introducing into the industry, resulting in both a broadening of attack surfaces and an expansion of the tools available to attackers and researchers for finding and exploiting vulnerabilities.

## The leaderboard

The DEVCORE Research Team [took the Master of Pwn title decisively](https://www.zerodayinitiative.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn), with 50.5 points and US$505,000 in prize money, with the team’s Orange Tsai demonstrating some of the most technically ambitious exploit chains of the week. Meanwhile, STARLabs SG finished second with 25 points and US$242,500, and Out of Bounds claimed third with 12.75 points and US$95,750.

# Targets, techniques, and the AI security reckoning

## AI moves from sideshow to center stage

When TrendAI™ ZDI first introduced AI as a Pwn2Own category in 2025, it was a forward-looking bet. In 2026, it became the center of the competition. For 2026, the single "AI" category was [split into four sub-categories](https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026): AI Databases, Coding Agents, Local Inference, and NVIDIA.

AI's influence on the contest didn't stop at the target list. Speaking with teams across the three days, we saw a clear pattern: most of the contestants used AI agents as active tools in developing their attacks. Across attack surface evaluation, vulnerability discovery, and exploit development, AI assistance was the norm rather than the exception; only a small number of teams worked entirely without it. This is a shift from two years ago, with real implications for the pace at which novel vulnerabilities will be found. The same tools that are expanding the enterprise attack surface are also accelerating attackers' ability to find and exploit weaknesses in that surface.

The takeaway was twofold. First, AI tooling has become a serious enterprise attack surface, and the vulnerabilities in it are not edge cases but architectural. Second, AI is now a standard part of the offensive researcher's toolkit, compressing the time between a new product shipping and a working exploit.

## The trust boundary problem in AI tooling

The most consistent finding across every AI product that fell during the week was what we are calling the "trust boundary problem." Modern AI coding agents, inference proxies, and local LLM platforms do not operate in isolation. They interact with external tools, protocols, SDKs, and services, and tend to inherit the trust assumptions of everything they touch, without independently validating that the input arriving at those trusted interfaces is safe.

This pattern showed up repeatedly across the four AI categories. Among the disclosures that we observed, OpenAI Codex and LiteLLM were both successfully attacked by three different teams that found ways to exploit trust boundaries in interactions with external tools or services, all arriving at root-level code execution. Similarly, we witnessed one team exploit LM Studio and NVIDIA Megatron Bridge to execute attacker-controlled code. In each case, the AI product wasn't broken in isolation, but rather at the interface where it met a tool or protocol it trusted.

Organizations deploying these tools should treat them with the same scrutiny as any network-accessible service: network segmentation, endpoint behavioral monitoring, process-lineage alerting (particularly for unexpected shell spawns from AI agent processes), and file-system integrity monitoring on directories where an agent has write access. Defense in depth remains critical for these applications. The network inspection window is narrow for these products, and broad protection requires additional investment in endpoint and runtime behavioral detection.

The TrendAI Vision One™ platform addresses these needs by combining XDR-driven endpoint and process telemetry, including process-lineage visibility well-suited to detecting anomalous shell spawns from AI agent runtimes, with TrendAI Vision One™ Server and Workload Security (SWP) for file-system integrity monitoring and runtime behavioral controls.

# Enterprise stalwarts still falling to classic bugs

While AI targets defined much of the contest's character, traditional enterprise infrastructure was also well represented, with several high-value targets falling to well-understood vulnerability classes.

**[Microsoft Exchange](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results)** yielded a SYSTEM-level remote code execution chain from Orange Tsai of DEVCORE Research Team, [earning the maximum US$200,000 award](https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results). The three-bug chain resulted in full server compromise from a low-privileged domain machine, providing an easy way for attackers to leverage an initial foothold in the environment to gain high-level privileges.

**[Microsoft SharePoint](https://www.zerodayinitiative.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)** was compromised by splitline of DEVCORE Research Team, earning US$100,000. The contestant was able to leverage an unauthenticated HTTP request to achieve remote code execution on a default SharePoint installation.

**[Microsoft Edge](https://www.zerodayinitiative.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results)** was targeted by the prolific Orange Tsai on the first day of the contest, chaining four logic bugs, none individually catastrophic, to achieve a full sandbox escape, [earning US$175,000](https://www.zerodayinitiative.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results). The result is a one-visit compromise with no user interaction beyond loading a page.

**[VMware ESXi](https://www.zerodayinitiative.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn)** produced arguably the most consequential moment of the week when Nguyen Hoang Thach of STARLabs SG completed a full guest-to-host escape with the cross-tenant code execution add-on bonus, [earning US$200,000](https://www.zerodayinitiative.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn). Starting from inside a guest virtual machine, the chain broke out to the bare-metal hypervisor and then reached across to modify a separate guest on the same host, a scenario with direct implications for multi-tenant hosting environments.

There were also successful attempts in a variety of other products including Claude, Cursor, NVIDIA Container Toolkit, Oracle AI Database, Windows 11, Red Hat Enterprise Linux, and more. As of writing, TrendAI™ ZDI and TrendAI™ Labs Threat Response are still evaluating the cases to provide detection guidance and will be disclosing more information as appropriate.

Since the contest involves multiple attempts running in parallel across several rooms over three days, we were unable to attend every disclosure firsthand. The writeups above cover the attempts our team was present for; many other noteworthy results landed in parallel sessions that we will continue to review in the weeks ahead.

# Vulnerability patterns

Across the targets covered at this year's event, a short list of vulnerability patterns recurs. **Trust boundary failures** and **architectural misdesign** dominated the AI category; every AI product that fell did so because it unconditionally trusted input arriving through an external tool or protocol. Authentication and credential-handling weaknesses dominated the Microsoft server category. Memory safety failures defined the ESXi result. Browser security failures came from accumulated small mistakes in vendor-specific extensions to the Chromium engine baseline — perhaps most surprisingly, all four of the bugs used in the Microsoft Edge attempt were logic bugs, no memory corruption in sight.

# TrendAI™ solutions

TrendAI™ ZDI and product security teams have tracked the vulnerabilities demonstrated at Pwn2Own Berlin 2026 from the moment they were disclosed to us. For targets covered by TrendAI™ TippingPoint™ network security filters, our teams developed and shipped protections within days of the competition and well ahead of vendor patches.

The following filters have already been shipped **as of May 19, 2026** , providing network-level coverage for customers ahead of vendor remediation, with additional coverage currently being developed as of writing:

Filter ID | ZDI Case Vendor Product  
---|---  
47426 | ZDI-CAN-31305 LiteLLM LiteLLM  
47427 | ZDI-CAN-31432 LiteLLM LiteLLM  
47428 | ZDI-CAN-31263 Microsoft Edge  
47429 | ZDI-CAN-31430 Microsoft Edge  
47430 | ZDI-CAN-31431 Microsoft Edge  
47435 | ZDI-CAN-31482 LiteLLM LiteLLM  
47436 | ZDI-CAN-31484 LiteLLM LiteLLM  
47437 | ZDI-CAN-31481 Microsoft Exchange Server  
47438 | ZDI-CAN-31490 Microsoft SharePoint  
  
Table 1. TrendAI™ TippingPoint™ network security filters

LiteLLM accounts for four filter entries because three independent teams demonstrated distinct exploitation paths against it during the competition. The coverage also spans the four-bug Microsoft Edge sandbox escape chain, the Exchange SYSTEM-level RCE, and the pre-authentication SharePoint RCE. Customers running TippingPoint with an up-to-date filter package are protected against these vulnerabilities at the network level while awaiting vendor patches.

All the vulnerabilities demonstrated at Pwn2Own 2026 were disclosed to the vendors as part of the contest. The vendors now have 90 days to create and publish patches for all the vulnerabilities used in the competition. In the meantime, TrendAI™ has already published the previously mentioned detections for these vulnerabilities and will continue to evaluate and release further guidance as it becomes available.

# The race is getting faster

Pwn2Own Berlin 2026 revealed patterns that will shape enterprise security priorities for the year ahead. The headline lesson is speed: AI-assisted research, broader attack surfaces, and a record-capacity field are compressing the time between a product shipping and a working exploit, shrinking the window defenders have to respond.

The trust boundary problem exposed in AI tooling this week is not just a temporary growing pain. As agent ecosystems expand and AI products integrate with more external tools, protocols, and services, the attack surface will grow with them. Every new integration is a potential seam where inherited trust assumptions can be exploited. Organizations adopting AI agents should expect this attack surface to scale alongside their deployments and plan their security architectures accordingly.

The VMware ESXi guest-to-host escape, with its cross-tenant code execution, delivered a pointed reminder about hypervisor security in cloud environments. Virtualization remains the foundational isolation layer for multi-tenant infrastructure. When that layer breaks, the blast radius extends beyond a single customer to every tenant on the affected host. Cloud providers and enterprises running shared virtualization infrastructure should treat this result as a signal to renew investment in hypervisor hardening, segmentation, and behavioral monitoring at the host level.

Another key data point from the event: the registration deadline had to be moved up due to capacity limits. The global offensive research community is larger, better-tooled, and more active than at any point in Pwn2Own's 19-year history. AI-assisted vulnerability discovery is compressing the timeline between product release and working exploit. The volume of research means that vulnerabilities are being found faster than ever, whether by researchers participating in coordinated disclosure or by adversaries who are not.

In response, TrendAI™ is prioritizing three areas: expanding detection coverage for AI agent behavioral anomalies at the endpoint level through **[TrendAI Vision One™ Endpoint Security](/en/business/products/endpoint-security.html)** , which delivers process-lineage telemetry and behavioral alerting directly relevant to the coding agent attack patterns that defined this year's contest; deepening network inspection capabilities for AI-to-tool protocol traffic via **[TrendAI Vision One™ XDR for Networks](/en/business/products/network.html) **and **[TrendAI Vision One™ Cloud IPS](/en/business/products/hybrid-cloud.html)** ; and accelerating the turnaround time from Pwn2Own disclosure to shipping protection. Initial protections were published within days of the competition, but our broader goal is ensuring that TrendAI™ customers have layered defenses in place before vulnerabilities become incidents.

Pwn2Own exists to find critical vulnerabilities before adversaries do and to give vendors and defenders a head start. Pwn2Own Berlin 2026 made clear that the gap between disclosure and exploitation is closing. The question for every security team is whether their detection and response capabilities are keeping pace.

Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Exploits & Vulnerabilities](/en/research.html?category=trend-micro-research:threats/exploits-and-vulnerabilities)

###  Authors 

  * Scott Graham

Sr. Threat Response Engineer




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)