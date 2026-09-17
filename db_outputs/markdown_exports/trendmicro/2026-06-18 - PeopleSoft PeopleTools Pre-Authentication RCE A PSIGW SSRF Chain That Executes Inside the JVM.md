# PeopleSoft PeopleTools Pre-Authentication RCE: A PSIGW SSRF Chain That Executes Inside the JVM

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/f/PeopleTools.html
- **Date :** 2026-06-18

---

Cyber Threats

# PeopleSoft PeopleTools Pre-Authentication RCE: A PSIGW SSRF Chain That Executes Inside the JVM

A pre-authentication remote code execution (RCE) chain in Oracle PeopleSoft PeopleTools abuses the Integration Broker's PSIGW gateway to execute code inside the application server's Java virtual machine (JVM), evading behavioral and network sensors.

By: Jacob Santos 2026/06/18 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

## Key takeaways

  * A pre-authentication remote code execution (RCE) chain in Oracle PeopleSoft PeopleTools reaches an internal-only management servlet through a server-side request forgery (SSRF) in the PSIGW gateway, then gains code execution through Java XMLDecoder deserialization. Oracle assigned [CVE-2026-35273](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html) (CVSS 9.8) and released an out-of-band patch on June 10, 2026.
  * The chain affects PeopleTools 8.61, and 8.62, including installations that were fully patched before the out-of-band advisory, because Oracle’s prior serialization-filter hardening does not cover this XMLDecoder code path.
  * The chain is **behaviorally quiet** : Its final step executes inside the WebLogic JVM on a web-tier restart, with no spawned child process and no required outbound beacon. Detection logic that watches for “Java spawns a shell” or for an on-the-wire exploit signature will, in the common case, see nothing.
  * TrendAI™ protections address this threat across the network and endpoint layers, including TrendAI™ Deep Discovery rules and TrendAI™ TippingPoint, TrendAI Vision One™ Server and Workload Protection (SWP), and TrendAI™ Deep Security filters. More guidance may be found in this entry’s recommendations section.



Enterprise resource planning systems handle some of the most sensitive data an organization holds, but they are also deeply connected to internal infrastructure. When a pre-authentication remote code execution (RCE) chain surfaces in one of the most widely deployed ERP platforms and is already being exploited in the wild, it warrants close attention. In this blog entry, TrendAI™ Research details a technical analysis of an active pre-authentication exploitation chain in Oracle PeopleSoft PeopleTools, the development platform used to build and maintain PeopleSoft applications. PeopleSoft PeopleTools versions 8.61, and 8.62 are affected, per Oracle’s advisory.

On June 10, 2026, Oracle issued an out-of-band security alert for [CVE-2026-35273](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html), a critical unauthenticated remote code execution vulnerability (CVSS 9.8) in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools. The vulnerability was reported to Oracle through the [TrendAI™ Zero Day Initiative™ (ZDI)](https://www.zerodayinitiative.com/)[](https://www.zerodayinitiative.com/). One day later, [Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/) published a report attributing in-the-wild exploitation to SHADOW-AETHER-015 (ShinyHunters), documenting a campaign that ran from May 27 through June 9, 2026, two weeks before the vendor advisory and targeted over 100 organizations, predominantly in higher education.

Pre-authentication RCE on an enterprise application is severe, but not new. The notable property of this vulnerability is not its impact, but its near-total lack of observability. The final code-execution step runs through Java’s XMLDecoder inside the application server’s own Java virtual machine (JVM), fires on a restart rather than on the inbound request, and needs no child process and no outbound beacon to succeed. A defender watching the usual places sees a quiet system.

Our researchers discovered new information about this vulnerability, which was responsibly disclosed to Oracle as part of our investigation. This blog documents the chain step by step, explains the single mechanic that makes it so hard to see, and turns that into concrete guidance for defenders. TrendAI™ also published [Security Alert KA-0023679](https://success.trendmicro.com/en-US/solution/KA-0023679) with an overview and initial detection guidance.

## What PSIGW and PSEMHUB actually are

Oracle PeopleSoft runs human-resources, financials, and campus-management workloads for large enterprises, government agencies, and universities. Two PeopleSoft components matter here:

  * The **Integration Broker** is PeopleSoft’s messaging layer, the machinery that lets PeopleSoft exchange data with other systems. It exposes a public-facing gateway, the **PeopleSoft Integration Gateway (PSIGW)** , and that gateway publishes an unauthenticated listening connector at /PSIGW/HttpListeningConnector. Its job is to accept inbound integration messages.
  * The **PeopleSoft Environment Management Hub (PSEMHUB)** is a separate, internal-only servlet used to manage PeopleSoft environments. It is not meant to be reachable from untrusted networks. Access to it is gated by an IP-based allow-list check named validateClient, which is supposed to ensure only trusted hosts can talk to the hub.



The vulnerability lives between those two components: A public gateway that will faithfully relay a request, and an internal servlet that trusts requests which appear to come from the local host. Bridge that seam and an external, unauthenticated attacker is suddenly talking to an internal management endpoint.

## Methodology

The chain proceeds in six steps. The description below is reconstructed from Trend ZDI reproduction of the exploit and from incident analysis.

**Step 1 - Pre-authentication SSRF at the gateway**

The attacker sends an unauthenticated POST to the Integration Broker’s listening connector:

POST /PSIGW/HttpListeningConnector

The request body is a PeopleSoft **IBRequest** XML message whose ConnectorParam carries a URL that points back at the server itself; for example, http(s)://localhost/PSEMHUB/hub.

**Step 2 - The validateClient bypass**

Because the gateway issues that follow-on request _from itself_ , the inbound call to /PSEMHUB/hub appears to originate from localhost. That satisfies the IP-based validateClient allow-list meant to restrict the hub to trusted hosts. This is a textbook **server-side request forgery (SSRF)** : The attacker borrows the server’s own identity to reach an endpoint they could never reach directly, and they now talk to the PSEMHUB hub servlet pre-authentication.

**Step 3 - Staging on disk**

Through the hub, the attacker writes attacker-controlled content under the transaction staging directory envmetadata/transactions/.

**Step 4 - Persistence as a planted XML object**

A crafted XML payload is written under envmetadata/data/environment/. At this point nothing has executed; the payload sits dormant on disk, waiting.

**Step 5 - Deserialization to code execution**

On the next **web-tier restart** , PSEMHUB’s XMLDecoder deserializes the planted XML and instantiates attacker-chosen objects. That yields **RCE as the web-tier service account** : SYSTEM on Windows, psadm2 on Unix-like hosts. This is the step that earlier patching did not address: Oracle’s prior serialization-filter hardening does not cover the XMLDecoder path, which is why installations that had applied all previous patches remained vulnerable until Oracle's patch.

**Step 6 - Post-exploitation options**

From code execution, the operator chooses what comes next. Two options were seen in analysis:

  * **Web shell.** Drop a JSP web shell into the PSEMHUB.war docroot for interactive, persistent access.
  * **Credential coercion.** Coerce outbound SMB/445 to capture or relay the machine account’s NetNTLM credentials.



## The one mechanic that makes this chain hard to see

The single most important detail for defenders is in Step 5: **The trigger is a restart, and the execution is in-process.**

There is a deliberate time gap between persistence (Steps 3–4) and execution (Step 5). When execution finally happens, it happens _inside the WebLogic JVM_. XMLDecoder deserialization and JSP web shell execution produce no child-process telemetry unless a web shell explicitly runs an operating-system command. A successful exploitation that stops at in-JVM code execution therefore generates none of the parent/child process anomalies that behavioral detection relies on, and the SSRF pivot itself targets localhost — a loopback request that never crosses a network sensor.

This is, by construction, a chain built to leave little behind. In-JVM deserialization and web shell instantiation produce no file or process payload unless an operating-system command runs, and a loopback SSRF produces nothing on the wire. Conventional detection that waits for an on-the-wire exploit signature or a “Java spawns a shell” anomaly will, in the common case, have nothing to fire on — which is precisely why the hunt has to move to the persistence paths and the restart instead.

Two benign patterns can look superficially like the chain, and both must be excluded before anything is called “exploitation”:

  * **Integration Broker east-west traffic flagged by an unrelated signature.** PeopleSoft’s own internal Integration Broker SOAP/XML can trip network signatures written for other products; a Django-exploit signature, for example, will misfire on legitimate PSIGW traffic. Before escalating any PSIGW hit, confirm the source is genuinely external — internal-to-internal Integration Broker chatter is normal east-west traffic, not exploitation.
  * **Legitimate writes under envmetadata/.** PeopleSoft Change Assistant and Veritas NetBackup both write to these paths in normal operation. Any persistence rule that does not allow-list these will drown in false positives.



## MITRE ATT&CK techniques

**Tactic** | **Technique** | **ID** | **How it appears here**  
---|---|---|---  
Initial access | Exploit public-facing application | T1190 | Unauthenticated SSRF at POST /PSIGW/HttpListeningConnector, pivoting to the internal PSEMHUB hub and triggering XMLDecoder code execution  
Persistence | Server software component: web shell | T1505.003 | Optional JSP web shell dropped into the PSEMHUB.war docroot  
Credential access | Forced authentication | T1187 | Optional outbound SMB/445 coercion for NetNTLM capture or relay  
  
Table 1. ATT&CK mapping for the PSEMHUB chain. The server-side deserialization that drives code execution is treated as the mechanism of T1190 rather than a separate technique, because ATT&CK has no clean mapping for server-side XMLDecoder deserialization.

## Recommendations

Oracle released an out-of-band patch on June 10, 2026; apply it immediately on all PeopleTools 8.61 and 8.62 installations. Given that exploitation was observed as early as May 27, 2026, investigate for signs of compromise even after patching. Beyond patching, the following exposure-reduction and detection-engineering measures provide defense in depth:

  1. **Take the listening connector off untrusted networks.** Ensure /PSIGW/HttpListeningConnector is not reachable from the internet, and place the Integration Broker gateway behind network controls that restrict who can reach it.
  2. **Break the SSRF pivot.** Segment the gateway from the environment-management servlet so the PSEMHUB hub cannot be reached by a gateway-originated loopback request, and confirm that validateClient cannot be satisfied by self-originated traffic.
  3. **Watch the persistence paths.** Monitor for unexpected writes under envmetadata/transactions/ and envmetadata/data/environment/, and allow-list PeopleSoft Change Assistant and Veritas NetBackup so legitimate operations do not bury the signal.
  4. **Treat web-tier restarts as security-relevant.** Where an agent can observe JVM class loading, alert on XMLDecoder instantiation in the PSEMHUB context, because the restart is the moment dormant persistence becomes live code execution.
  5. **Hunt the optional artifacts.** Look for new JSP files in the PSEMHUB.war docroot, and restrict outbound SMB/445 from web-tier hosts to defeat the optional credential-coercion step.



Guidance also differs by role:

  * **For defenders:** Assume your behavioral and network sensors will not alert on a successful in-JVM exploitation. Pivot to the persistence-path and restart hunts above, and do not read a quiet SIEM as evidence you are unaffected.
  * **For decision-makers:** Treat this as a high-priority patching emergency. Investigate for signs of prior compromise even after applying the patch. The supplementary exposure question remains: "is our PSIGW gateway reachable from untrusted networks?" Prioritize an exposure review of any internet-facing PeopleSoft.
  * **For incident responders:** Preserve envmetadata/ contents and web-tier restart logs first. The gap between persistence and execution means a planted XML object may sit dormant and fully recoverable before a restart fires it, so disk and restart timing carry more evidentiary value than process trees.



## Conclusion

The vulnerability and its chain are well-sourced, and they describe a sobering pattern: A serious pre-authentication RCE can run end to end while producing almost no telemetry, because its final step lives inside the application’s own JVM and fires on a restart rather than on the inbound request. A quiet system is not a safe one; silence is the predictable shape of a chain built to execute in-process and fire on a restart.

That observability gap is the lasting lesson. The specific vulnerability is now patched, but the pattern of a public-facing gateway relaying requests to an internal servlet, with execution deferred to an in-JVM restart will appear again in other enterprise applications. Defenders who build detection around persistence paths and restart behavior, rather than waiting for process-tree anomalies or network signatures, will be better positioned when it does. 

## TrendAI™ solutions

TrendAI Vision One™ customers can act on this threat through coverage across the network and endpoint layers. The following rules and filters address this chain:

**TrendAI™ Deep Discovery™**

  * Rule 5855, "PeopleSoft PeopleTools Environment Management Hub (PSEMHUB) SSRF Exploit — HTTP (Request)."
  * Rule 5863, "Oracle PeopleSoft HubMBeanPersistance Deserialization of Untrusted Data RCE Exploit — HTTP (Request)."



**TrendAI™ TippingPoint™**

  * Filter 47502, "CVE-2026-35273: HTTP: Oracle PeopleSoft Server-Side Request Forgery Vulnerability."
  * Filter 47529, "ZDI-CAN-31817: Zero Day Initiative Vulnerability (Oracle PeopleSoft)."
  * Filter 47545, "ZDI-CAN-31818: Zero Day Initiative Vulnerability (Oracle PeopleSoft)."



**TrendAI™ Deep Security™, TrendAI Vision One™ Server and Workload Protection (SWP), and TrendAI Vision One™ Endpoint Security IPS**

  * Filter 1012580, "Oracle PeopleSoft PeopleTools SSRF Vulnerability (CVE-2026-35273)."
  * Filter 1012585, "Oracle PeopleSoft Untrusted Data Deserialization Vulnerability (ZDI-CAN-31817)."



## TrendAI Vision One™ Threat Intelligence Hub

[TrendAI Vision One™ Threat Intelligence Hub](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. 

**Emerging threat:** [CVE-2026-35273: Pre-Authentication Remote Code Execution in PeopleSoft PeopleTools (PSEMHUB)](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=CVE-2026-35273%3A%20Pre-Authentication%20Remote%20Code%20Execution%20in%20PeopleSoft%20PeopleTools%20\(PSEMHUB\))

**Threat actor:** [SHADOW-AETHER-015](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=SHADOW-AETHER-015)

**TrendAI Vision One™ Intelligence Reports (IOC sweeping)**

[CVE-2026-35273: Pre-Authentication Remote Code Execution in PeopleSoft PeopleTools (PSEMHUB)](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=CVE-2026-35273%3A%20Pre-Authentication%20Remote%20Code%20Execution%20in%20PeopleSoft%20PeopleTools%20\(PSEMHUB\))

TrendAI Vision One™ customers can hunt for the chain’s footprint using TrendAI Vision One™ XDR Data Explorer App. Because the SSRF body (the IBRequest ConnectorParam URL) is inspected at the network sensor layer, deep request-body matching is best left to dedicated network signatures — the XDR Data Explorer App hunts the observable metadata around it: The request path, the on-disk artifacts, and the outbound SMB. The queries below are a starting set; field availability varies by data source and sensor, so validate field names against your tenant schema before running them.

**Inbound SSRF entry and direct hub access** (Network Activity Data):

request:"/PSIGW/HttpListeningConnector" AND (request:"PSEMHUB/hub" OR request:"localhost" OR request:"127.0.0.1")  
request:"/PSEMHUB/hub"

**On-disk staging and XMLDecoder persistence** (Endpoint Activity Data), with the two known-benign writers excluded:

(objectFilePath:"envmetadata/transactions" OR objectFilePath:"envmetadata/data/environment")  
AND NOT (processFilePath:"ChangeAssistant" OR processFilePath:"NetBackup" OR processFilePath:"bpbkar" OR processName:"psae")

**Optional JSP web shell in the PSEMHUB web application** (Endpoint Activity Data):

objectFilePath:"PSEMHUB.war" AND objectFilePath:".jsp"

**Hunt patterns (detection use — not attacker-owned indicators)**

**Pattern** | **Where** | **Note**  
---|---|---  
POST /PSIGW/HttpListeningConnector | Web/proxy logs, IPS | SSRF entry point  
IBRequest ConnectorParam URL=http(s)://localhost/PSEMHUB/hub | Request body | Loopback pivot bypassing validateClient  
Writes under envmetadata/transactions/ | Filesystem/EDR | Staging — allow-list Change Assistant and Veritas NetBackup  
XML writes under envmetadata/data/environment/ | Filesystem/EDR | XMLDecoder persistence — same allow-list  
New JSP under PSEMHUB.war docroot | Filesystem/EDR | Optional web shell  
Outbound SMB/445 from a web-tier host to an external IP | Network | Optional NetNTLM coercion  
  
Table 2. Hunt patterns for the PSEMHUB chain. These are detection and hunting aids, not attacker-controlled indicators, and several require allow-listing to control false positives.

Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Jacob Santos

Senior Threat Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)