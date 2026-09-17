# Tycoon2FA Phishing-as-a-Service Platform Persists After Takedown

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/tycoon2fa-phishing-as-a-service-platform-persists-following-takedown/
- **Date :** March 20, 2026

---

# Tycoon2FA Phishing-as-a-Service Platform Persists Following Takedown

March 20, 2026

• [ Falcon Complete Team - Counter Adversary Operations](/en-us/blog/author.falcon-complete-team---counter-adversary-operations/ "Posts by Falcon Complete Team - Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")• [From The Front Lines](/en-us/blog/category.from-the-front-lines/ "From The Front Lines")


On March 4, 2026, Europol [announced](https://www.europol.europa.eu/media-press/newsroom/news/global-phishing-service-platform-taken-down-in-coordinated-public-private-action?mtm_campaign) the technical disruption of _Tycoon2FA_ , a subscription-based phishing-as-a-service (PhaaS) platform that enabled cybercriminals to bypass multifactor authentication (MFA) and compromise email accounts. Law enforcement authorities from six countries worked with industry partners to seize 330 domains that formed the platform’s core infrastructure.

Infrastructure takedowns are a challenging and important aspect of adversary disruption and a centerpiece of law enforcement and private sector cooperation in cybersecurity. In situations where direct physical enforcement actions such as arrests are infeasible, disrupting bad actors' operational means can often be the most efficacious and direct way to impose costs on criminals who otherwise act with relative impunity. Nonetheless, law enforcement bodies and their industry partners often go into these technically complicated efforts knowing full well that adversaries are resilient and will likely ultimately overcome or circumvent technical disruptions and reemerge as threats once again.

CrowdStrike applauds Europol and its partners in their disruption efforts against _Tycoon2FA_. CrowdStrike has often joined law enforcement partners in conducting similar disruption efforts and will continue to do so in the future. As a part of this collaborative spirit, CrowdStrike also stands ready to help provide visibility into the efficacy of disruption operations and help provide "long-tail support" to its customers and the public when criminals attempt to reconstitute their infrastructure in the wake of disruptions.

Since the date of the _Tycoon2FA_ takedown, the CrowdStrike Falcon® Complete Next-Gen MDR team and CrowdStrike Counter Adversary Operations team observed a short-term decrease in the volume of _Tycoon2FA_ campaign activity; however, the volume of cloud compromises has since increased to levels previously observed by Falcon Complete. This resumed campaign volume — and the continuation of previously observed _Tycoon2FA_ tactics, techniques, and procedures (TTPs) — suggests the actors responsible for the PhaaS are likely to remain active in the threat landscape in the short to medium term and warrant continued vigilance by defenders. 

_Tycoon2FA_ is a clear example of how today's adversaries operate; they are highly adaptive, technically capable, and persistent in pursuing their objectives. Even as the threat landscape shifts, actors behind platforms like these continue to evolve their TTPs and find ways to maintain pressure on defenders. Staying ahead of that persistence requires continuous visibility across the full attack surface, the ability to correlate signals across domains in real time, and the expertise to act on them decisively. The AI-native CrowdStrike Falcon® platform and the expert defenders in Counter Adversary Operations and Falcon Complete give organizations the speed and depth of coverage needed to detect, disrupt, and respond before adversaries achieve their objectives.

## Impact of Disruption

_Tycoon2FA_ began its operations in 2023 and provided a subscription-based toolkit that intercepted live authentication sessions using adversary-in-the-middle (AITM) techniques. In mid-2025, the platform was responsible for 62% of all phishing attempts blocked by [Microsoft](https://blogs.microsoft.com/on-the-issues/2026/03/04/how-a-global-coalition-disrupted-tycoon/); _Tycoon2FA_ purportedly generated more than 30 million malicious emails in a single month. Given this prominence, the attempt at disrupting the tool was notable as an effort by law enforcement to disrupt a key component of the PhaaS ecosystem.

The March 4th _Tycoon2FA_ disruption was the result of coordinated action between Europol’s European Cybercrime Centre (EC3) and law enforcement authorities in Latvia, Lithuania, Portugal, Poland, Spain, and the United Kingdom, alongside industry partners. The coordinated effort targeted 330 domains comprising the platform’s infrastructure. Additional actions against the individuals related to the PhaaS operation have not yet been reported. 

This _Tycoon2FA_ takedown follows law enforcement’s September 2025 targeting of _RaccoonO365_ , which operated as _Tycoon2FA_ ’s primary competitor and also enabled threat actors (with minimal technical expertise) to conduct sophisticated phishing campaigns. 

Falcon Complete observed numerous Tycoon2FA incidents in 2024, 2025, and 2026, with TTPs that include:

  * Using phishing emails to direct victims to _Tycoon2FA_ CAPTCHA pages
  * Stealing victims’ session cookies upon CAPTCHA validation
  * Extracting victims’ email addresses via a JavaScript (JS) file
  * Populating fake Microsoft 365 or Google login pages, which are hosted on a _Tycoon2FA_ domain
  * Proxying victims’ credentials to a legitimate Microsoft 365 cloud account via an obfuscated JS file 
  * Authenticating to the victim’s cloud environment using the stolen cookies and credentials



## Tycoon2FA Resurgence

Falcon Complete observed a short-term decrease in the volume of _Tycoon2FA_ campaign activity following the takedown, with daily volumes on March 4 and March 5, 2026, reducing to 25% of pre-disruption levels. However, this volume subsequently returned to pre-disruption levels, with daily levels of cloud compromise active remediations returning to early 2026 levels. Additionally, _Tycoon2FA_ ’s TTPs have not changed following the takedown, indicating that the service's operations may persist beyond this disruption. 

Falcon Complete has continued to observe a diversity of phishing techniques associated with discrete phishing actors following the date of law enforcement disruption subsequent to March 3, 2026. These include business email compromise (BEC) phishing targeting personal and enterprise users, email thread hijacking, cloud account takeover, and the compromise of SharePoint and cloud environments for the dissemination of malicious URLs that redirect to the _Tycoon2FA_ phish kit. Post-disruption campaigns have leveraged:

  * Malicious URLs
  * URL shortener services
  * Links to legitimate presentation software that include malicious redirects to _Tycoon2FA_ infrastructure
  * Threat actor-registered infrastructure impersonating construction entities
  * Compromised SharePoint infrastructure from known contacts that retrieves XLSX and PDF files, including malicious redirect URLs to _Tycoon2FA_ infrastructure



In one instance, Falcon Complete observed an active email campaign that attempted to utilize a version of the _Tycoon2FA_ phish kit leveraging Cloudflare `r2[.]dev` and `workers[.]dev` infrastructure associated with public reporting on the [Salty2FA phish kit](https://medium.com/@anyrun/salty2fa-tycoon2fa-hybrid-a-new-phishing-threat-to-enterprises-6e2c0a5f7036). These campaigns were unsuccessful as they retrieved Cloudflare suspected phishing page HTML responses consistent with the claims of takedown. This may possibly indicate continued efforts by industry partners like Cloudflare post-disruption to impact the operation of the _Tycoon2FA_ service. 

Following initial cloud compromise Falcon Complete continues to see pre-BEC activity including the creation of suspicious inbox rules and the creation of folders to conceal the transmission of BEC or financial fraud emails from compromised Microsoft Exchange environments.

Between 4 March 2026 and 6 March 2026, Falcon Complete responded to at least 30 suspected _Tycoon2FA_ -enabled phishing incidents comprising at least 12 decoy and credential-capture pages. _Tycoon2FA_ operators typically leverage generative AI to quickly create convincing decoy webpages hosted at a combination of threat actor-controlled domains, which are returned if users fail geofencing profiling measures. Customers of the _Tycoon2FA_ phish kit leverage compromised legitimate domains and abused legitimate hosting services to achieve redirection to _Tycoon2FA_ phishing infrastructure. Some of the domains hosting _Tycoon2FA_ pages have been active since 2025, likely indicating that they have not been subject to the 2026 law enforcement operation. Domains hosting _Tycoon2FA_ pages in March 2026 include:

Table 1. Tycoon2FA phishing domains**Phishing Domain**| **Parent Domain Control**| **Parent Domain Registered**| **Phishing Domain First Observed**  
---|---|---|---  
`811inboard[.]aeroprimelink[.]za[.]com`| Threat actor| August 10, 2025| March 6, 2026  
`annotation[.]hanoufra[.]ltd`| Threat actor| February 9, 2026| March 4, 2026  
`awssecrets[.]saidiosea[.]dev`| Threat actor| January 17, 2026| March 4, 2026  
`electron[.]c8zoeh[.]com`| Threat actor| December 18, 2025| March 4, 2026  
`hub[.]thadrodrai[.]business`| Threat actor| February 9, 2026| March 5, 2026  
`omegaenergy[.]com[.]np`| Threat actor| June 12, 2025| March 5, 2026  
`pass[.]aeroprimelink[.]za[.]com`| Third party; compromised domain| Prior to September 2012| March 6, 2026  
`pub-9ee1bf400ea645748830bc408aa2b88a[.]r2[.]dev`| Cloudflare; shared developer infrastructure  Inactive at the time of delivery, indicating successful takedown | N/A| March 5, 2026  
`traelyst[.]dk`| Third party; compromised domain| November 20, 2024| March 6, 2026  
`twig[.]lifeworkinc[.]com`| Threat actor| June 20, 2025| March 6, 2026  
  
![Figure 1. AI-generated Tycoon2FA decoy pages returned after failing geocheck](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-Tycoon-1?wid=1156&hei=902&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 1. AI-generated Tycoon2FA decoy pages returned after failing geocheck

Upon successful credential and MFA token capture, the _Tycoon2FA_ platform automatically logs in to the victim’s Microsoft EntraID account. The automated logins typically originate from IPv6 addresses owned by Romania-based ISP M247 Europe SRL. _Tycoon2FA_ activity in March 2026 included automated logins originating from at least 11 IP addresses (Table 2). Eight of the IP addresses were first observed on or after March 1, 2026, indicating that the threat actor likely acquired them after the disruption operation. One of the IP addresses, however, has been associated with _Tycoon2FA_ since at least January 9, 2026, indicating that some threat actor-controlled infrastructure likely survived the disruption operation.

Table 2. Tycoon2FA automated login IP addresses**IP Address**| **Hosting Provider**| **First Observed Tycoon2FA Incident**  
---|---|---  
`2a0d:5600:8:94::440:e534`| M247 Europe SRL| January 9, 2026  
`2a0d:5600:8:2e:0:1:62fe:e6b9`| M247 Europe SRL| February 2, 2026  
`2a0d:5600:8:2e:0:1:d823:a25a`| M247 Europe SRL| February 3, 2026  
`2a0d:5600:8:2e:0:1:25dd:3b4a`| M247 Europe SRL| March 1, 2026  
`2a0d:5600:8:2e:0:1:7d4:e433`| M247 Europe SRL| March 2, 2026  
`2a0d:5600:8:2e:0:1:65f4:6a3c`| M247 Europe SRL| March 2, 2026  
`2a0d:5600:8:2e:0:1:3f55:3b5c`| M247 Europe SRL| March 2, 2026  
`2a0d:5600:8:94::d439:3ac9`| M247 Europe SRL| March 2, 2026  
`2a0d:5600:8:2e:0:1:1d6e:ff40`| M247 Europe SRL| March 5, 2026  
`2a0d:5600:8:94::f2cd:9d43`| M247 Europe SRL| March 9, 2026  
  
The newly observed _Tycoon2FA_ activity in March 2026 indicates that _Tycoon2FA_ began to recover from this disruption within the same day of the announcement. However, a leading global cloud services provider hosted infrastructure as code (IaC) Workers’ domains related to _Salty2FA_ landing pages appear most affected by the disruption, likely as a byproduct of Cloudflare participating in this disruption.

The efforts by Europol and private industry partners to degrade the operations of _Tycoon2FA_ will likely have a positive impact on the eCrime landscape overall, even if temporary. The service's disruption likely set back current customers of the service by impeding phishing operations and damaged the long-term reputation of the PhaaS provider in the crimeware landscape. Nonetheless, disruption efforts have historically proven challenging when law enforcement is restricted from pairing technical operations with arrests or other physical asset seizures. Those joint operations can greatly assist in reducing adversarial operating capabilities.

Crowdstrike’s findings are consistent with this trend, as some core malicious activities have continued, demonstrating the _Tycoon2FA_ operators' likely resilience to takedown efforts. In CrowdStrike's visibility, domain registration associated with credential harvesting and session cookie theft remains active and ongoing, and the threat actors have continued to register new domains and develop AI-generated decoy pages at their typical, pre-disruption pace. Most notably, daily volumes of successful cloud account compromises achieved through the _Tycoon2FA_ phish kit show no material decline, and infrastructure procurement for IPv6 addresses used in authentication activities continues unchanged, demonstrating the service's operational resilience despite disruption efforts.

## Outlook

While _Tycoon2FA_ continues to operate after the temporary disruption of its infrastructure by the coordinated industry and law enforcement operation, CrowdStrike nonetheless applauds the efforts by Europol and its partners to disrupt this threat actor's operations. 

When cross-domain disruption avenues are unavailable to law enforcement bodies, infrastructure disruption — even if only temporary — can serve to frustrate, slow down, and confuse adversaries. As recovery from such disruptions occurs, CrowdStrike and other industry partners must stand ready to orient themselves to the evolving nature of these threats.

Falcon Complete continues to detect and prevent threats such as those described in this blog at the phishing, DNS resolution, cloud authentication, and BEC Exchange inbox level through CrowdStrike Falcon® Next-Gen SIEM and the Falcon platform. Threat actors like those who operate _Tycoon2FA_ likely readily adapt to disruptions by developing rapid recovery mechanisms and leveraging jurisdictional safe havens to maintain operations. It is also highly likely that the operators will continue to evolve TTPs to try to evade detection and defenders, including the use of new ASNs. Customers of the _Tycoon2FA_ phish kit continue to transmit emails with successful compromises, which requires enterprises to continue to employ defense-in-depth approaches to combat AITM PhaaS actors in the threat landscape.

Staying ahead of adversaries requires continuous visibility across the full attack surface, real-time signal correlation across domains, and the expertise to act decisively. In the face of resilient adversaries who work to mitigate the impacts of disruption efforts, CrowdStrike combines its AI-native platform with expert human defenders in Counter Adversary Operations and Falcon Complete to empower organizations to stay ahead of threats, effectively disrupting and neutralizing attacks before adversaries can achieve their objectives.

#### Additional Resources

  * _Visit the[Counter Adversary Operations](https://www.crowdstrike.com/en-us/platform/threat-intelligence/) webpage to learn about CrowdStrike’s threat intelligence and hunting solutions._
  * _Learn how[Falcon Complete](https://www.crowdstrike.com/en-us/services/falcon-complete-next-gen-mdr/) helps stop breaches faster. _
  *  _Read the[CrowdStrike 2026 Global Threat Report](https://www.crowdstrike.com/en-us/global-threat-report/) for the latest insights on adversaries, tradecraft, and activity._



_Technical analysis of the Tycoon2FA infrastructure was written by Michael Raggi, Principal Threat Response Specialist, Falcon Complete._

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)