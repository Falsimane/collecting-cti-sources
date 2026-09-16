# LABYRINTH CHOLLIMA Evolves into Three Adversaries | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/labyrinth-chollima-evolves-into-three-adversaries/
- **Date :** January 29, 2026

---

# LABYRINTH CHOLLIMA Evolves into Three Adversaries

January 29, 2026

• [ Rob Bruner](/en-us/blog/author.rob-bruner/ "Posts by Rob Bruner") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


  * LABYRINTH CHOLLIMA has evolved into three distinct adversaries with specialized malware, objectives, and tradecraft: GOLDEN CHOLLIMA and PRESSURE CHOLLIMA now likely operate separately from the core LABYRINTH CHOLLIMA group.

  * GOLDEN CHOLLIMA and PRESSURE CHOLLIMA target cryptocurrency entities and are distinguished by the scale and scope of their operations; core LABYRINTH CHOLLIMA operations continue to focus on espionage, targeting industrial, logistics, and defense companies.

  * Despite operating independently, these three adversaries share tools and infrastructure, indicating centralized coordination and resource allocation within the DPRK cyber ecosystem.




LABYRINTH CHOLLIMA is among the most prolific DPRK-nexus adversaries that CrowdStrike Intelligence tracks and is responsible for some of North Korea’s most notable intrusions including destructive attacks against South Korean and U.S. entities, and the global _WannaCry_ ransomware incident. 

CrowdStrike Intelligence assesses that three distinct, highly specialized operational subgroups have emerged since 2018, each with specialized malware, objectives, and tradecraft. This assessment reflects a comprehensive re-evaluation of historical data and a deliberate challenge to our previous LABYRINTH CHOLLIMA attribution framework. We now track these subgroups as GOLDEN CHOLLIMA, PRESSURE CHOLLIMA, and the core LABYRINTH CHOLLIMA group. Effective intelligence demands we constantly reassess established assumptions, relentlessly pursuing an objective, actionable depiction of the threat landscape. 

## LABYRINTH CHOLLIMA’s History and Evolution

LABYRINTH CHOLLIMA activity originates from the _KorDLL_ malware framework (active 2009-2015), a source code repository containing implant templates, command-and-control (C2) protocols, libraries for common tasks, and code for various obfuscation techniques. This framework spawned several epoch-defining malware families, including _Dozer_ , _Brambul_ , _Joanap_ , _KorDLL Bot_ , and _Koredos_ , and would evolve into the _Hawup_ and _TwoPence_ frameworks used by LABYRINTH CHOLLIMA and STARDUST CHOLLIMA, respectively.

[ ![Labyrinth Chollima malware framework family tree diagram](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-CHOLLIMA-Fig1?wid=946&hei=729&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) ](/content/dam/crowdstrike/marketing/en-us/images/blog/2026/01/Blog-CHOLLIMA-Fig1.png "Figure 1. KorDLL malware framework evolution \(click to enlarge\)") Figure 1. KorDLL malware framework evolution (click to enlarge)

Three operational subgroups emerged from the _Hawup_ framework between 2018-2020, each distinguished by sustained malware development paths, targeting patterns, and operational objectives (Figure 1). While infrastructure and tool sharing occurs, operational differences support tracking these groups as distinct adversaries rather than specialized groups under the LABYRINTH CHOLLIMA umbrella (Figure 2). The proliferation of these malware frameworks across the DPRK cyber ecosystem likely reflects coordination among the DPRK intelligence community or personnel as DPRK adversaries share successful TTPs and code elements.1

[ ![Chollima cyber threat groups comparison chart ](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-CHOLLIMA-Fig2?wid=833&hei=805&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) ](/content/dam/crowdstrike/marketing/en-us/images/blog/2026/01/Blog-CHOLLIMA-Fig2.png "Figure 2. LABYRINTH CHOLLIMA successors \(click to enlarge\)") Figure 2. LABYRINTH CHOLLIMA successors (click to enlarge)

## GOLDEN CHOLLIMA

GOLDEN CHOLLIMA targets economically developed regions with significant cryptocurrency and fintech presence, including the U.S., Canada, South Korea, India, and Western Europe. The adversary typically conducts smaller-value thefts at a more consistent operational tempo, suggesting responsibility for ensuring baseline revenue generation for the DPRK regime. 

The adversary’s malware originates with _Jeus_ in 2018 (and its macOS variant, _AppleJeus_), which originally masqueraded as a cryptocurrency application purportedly developed by the fictitious company Celas Limited. CrowdStrike Intelligence has observed eight different _Jeus_ and _AppleJeus_ variants in campaigns targeting cryptocurrency entities as well as shellcode overlaps between _PipeDown_ , _DevobRAT_ , _HTTPHelper_ , and _Anycon_ — forming a specialized fintech targeting toolkit.

GOLDEN CHOLLIMA’s recent operations demonstrate cloud-focused tradecraft. In late 2024, the adversary delivered malicious Python packages via recruitment fraud to a European fintech company. They pivoted to the victim’s cloud environment to access IAM configurations and associated cloud resources, and ultimately managed to divert the victim’s cryptocurrency to adversary-controlled wallets. 

CrowdStrike Intelligence has also observed GOLDEN CHOLLIMA leveraging Chromium zero-days to deliver malware, and CrowdStrike OverWatch threat hunting detected several deployments of _SnakeBaker_ and its JS variant _NodalBaker_ at fintech firms throughout June 2025.

## PRESSURE CHOLLIMA

PRESSURE CHOLLIMA conducted the DPRK’s highest-profile cryptocurrency heists, including the two largest cryptocurrency thefts on record. Public reporting links additional high-value thefts ranging from $52 million USD to $120 million USD to PRESSURE CHOLLIMA based on reused cryptocurrency wallets.2

Unlike GOLDEN CHOLLIMA’s consistent operations, PRESSURE CHOLLIMA pursues high-payout opportunities regardless of geography, focusing on organizations with significant digital asset holdings. PRESSURE CHOLLIMA deploys sophisticated, low-prevalence implants and has evolved into one of the DPRK’s most technically advanced adversaries.

PRESSURE CHOLLIMA operations likely diverged from LABYRINTH CHOLLIMA in February 2019 with experimental _SwDownloader_ deployment, quickly replaced by _SparkDownloader_ (tracked publicly as _TraderTraitor_). Recent campaigns leverage malicious Node.js and Python projects to deliver _Scuzzyfuss_ and _TwoPence Electric_ malware. 

## LABYRINTH CHOLLIMA Moving Forward

CrowdStrike Intelligence now tracks LABYRINTH CHOLLIMA more narrowly as espionage operations using malware with a _Hoplight_ lineage. Modern LABYRINTH CHOLLIMA operations emerged in 2020, coinciding with GOLDEN and PRESSURE CHOLLIMA’s divergence, likely indicating that blockchain malware experts and intelligence collection specialists moved into separate units.

The 2022 emergence of _FudModule_ represents a significant development for LABYRINTH CHOLLIMA’s malware capabilities. _FudModule_ employs direct kernel manipulation for stealth and has leveraged zero-day exploits in vulnerable drivers, Chrome, and Windows. GOLDEN CHOLLIMA has also reportedly used _FudModule_ , indicating shared tool access despite operational separation.3

LABYRINTH CHOLLIMA operations prioritize targets in the manufacturing and defense sectors, particularly European defense entities and U.S., Japanese, and Italian manufacturing organizations. Throughout 2024 and into 2025, LABYRINTH CHOLLIMA persistently targeted European aerospace corporations using employment-themed lures and exploited zero-day vulnerabilities against defense manufacturers. In the first half of 2025, CrowdStrike Intelligence also observed a growing interest by LABYRINTH CHOLLIMA in logistics and shipping companies. The adversary has also targeted U.S.-based manufacturing companies, including critical infrastructure entities in specialized areas such as hydroelectric power. 

LABYRINTH CHOLLIMA’s 2025 operations have demonstrated diverse delivery mechanisms. WhatsApp messaging — which the adversary has used to deliver malicious ZIP files containing trojanized applications — has emerged as a primary initial compromise vector. Likely due to the method’s high success rate, the adversary has used employment-themed social engineering in multiple campaigns, tailoring lures to target specific industries and roles.

## Outlook

CrowdStrike Intelligence assesses these three groups very likely operate as distinct organizational units within the DPRK cyber apparatus. This assessment is made with high confidence and supported by specialized malware development, distinct targeting patterns, and differences in operational tempo. 

Shared infrastructure elements and tool cross-pollination indicate these units maintain close coordination. All three adversaries employ remarkably similar tradecraft — including supply chain compromises, HR-themed social engineering campaigns, trojanized legitimate software, and malicious Node.js and Python packages — that reflects their common origins in the _KorDLL_ and _Hawup_ frameworks. 

LABYRINTH CHOLLIMA’s segmentation into specialized operational units represents a strategic evolution that enhances the DPRK regime’s ability to simultaneously pursue multiple objectives.

The financial motivation for GOLDEN CHOLLIMA and PRESSURE CHOLLIMA operations will likely intensify as international sanctions continue to cripple the DPRK's economy. Despite improving trade relations with Russia, the DPRK requires additional revenue to fund ambitious military plans that include constructing new destroyers, building nuclear-powered submarines, and launching additional reconnaissance satellites.4

These three adversaries remain fundamentally interconnected through shared tactical DNA and collaborative infrastructure. The cross-pollination of tools such as _FudModule_ in GOLDEN CHOLLIMA and LABYRINTH CHOLLIMA operations, combined with malware families’ code similarities among these adversaries, demonstrates how these adversaries continue to operate as components of a unified strategic apparatus despite their distinct mission sets. 

Organizations in the cryptocurrency, fintech, defense, and logistics sectors should practice heightened vigilance for DPRK social engineering campaigns, particularly employment-themed lures and trojanized legitimate software delivered via messaging platforms.

## Recommendations

These recommendations are designed to help protect against the activity described and are customized to address the specific tradecraft and objectives of GOLDEN CHOLLIMA, PRESSURE CHOLLIMA, and LABYRINTH CHOLLIMA.

### Mitigate Social Engineering

  * Implement strict validation for all incoming communication, especially for job-related or external inquiries. Train employees to be highly suspicious of unsolicited messages via platforms like WhatsApp and unexpected recruitment emails containing attachments or links to trojanized software.

  * Enforce a security policy that prohibits the download and execution of software from untrusted sources, particularly third-party versions of legitimate software like SumatraPDF or TightVNC clients.

  * Address supply chain and open-source abuse:

    * Scan and vet all third-party and open-source dependencies (e.g., malicious Node.js and Python packages) before deployment. Utilize tools that analyze package metadata, author reputation, and code for malicious or obfuscated functionality.

    * Implement software supply chain security practices to monitor for unauthorized changes in build and deployment environments.




### Cloud and Identity Security

  * Monitor CloudTrail and GuardDuty logs for suspicious activity related to the adversary’s common post-compromise actions, such as:

    * Unusual usage of the cloud environment command line interface.

    * Abnormal enumeration or modification of cloud-based identity and access management (IAM) users, roles, or policies.

    * Unexpected access patterns to cloud file storage, Kubernetes clusters, and cloud compute instances.

  * Enforce the principle of least privilege across all cloud-based IAM users and service roles to limit the blast radius of a compromised credential.

  * Implement multifactor authentication (MFA) for all cloud accounts, especially for root and administrative users.




### General Recommendations

  * Patch management:

    * Prioritize the patching of known remote code execution (RCE) and server-side request forgery (SSRF) vulnerabilities, particularly in public-facing applications and commonly targeted software like web browsers (e.g., Chromium).

    * Maintain all operating systems, hypervisors, drivers, and edge devices at a recent, supported software level to mitigate zero-day exploitation of kernel-level vulnerabilities (e.g., _FudModule_).

  * Cryptocurrency defense:

    * For organizations dealing with digital assets, implement multi-signature wallet requirements and time-locked transfers to increase the difficulty and detection time for large-scale crypto thefts.

    * Isolate cryptocurrency management systems from the corporate network and apply the most stringent security controls to these environments.




## IOCs

Exemplar samples of malware mentioned in this blog are provided below to enable community tracking of GOLDEN CHOLLIMA, PRESSURE CHOLLIMA, and LABYRINTH CHOLLIMA activity.

**Malware** | **Attribution** | **Exemplar SHA256 Hash**  
---|---|---  
_Dozer_ | LABYRINTH CHOLLIMA | `7dee2bd4e317d12c9a2923d0531526822cfd37eabfd7aecc74258bb4f2d3a643`  
_Brambul_ | LABYRINTH CHOLLIMA | `d2359630e84f59984ac7ddebdece9313f0c05f4a1e7db90abadfd86047c12dd6`  
_Joanap_ | LABYRINTH CHOLLIMA | `4fe3c853ab237005f7d62324535dd641e1e095d1615a416a9b39e042f136cf6b`  
_KorDLL Bot_ | LABYRINTH CHOLLIMA | `73edc54abb3d6b8df6bd1e4a77c373314cbe99a660c8c6eea770673063f55503`  
_Koredos_ | LABYRINTH CHOLLIMA | `a795964bc2be442f142f5aea9886ddfd297ec898815541be37f18ffeae02d32f`  
_Hawup RAT_ | LABYRINTH CHOLLIMA | `453d8bd3e2069bc50703eb4c5d278aad02304d4dc5d804ad2ec00b2343feb7a4`  
_Hoplight_ | LABYRINTH CHOLLIMA | `05feed9762bc46b47a7dc5c469add9f163c16df4ddaafe81983a628da5714461`  
_Manuscrypt_ | LABYRINTH CHOLLIMA | `dced1acbbe11db2b9e7ae44a617f3c12d6613a8188f6a1ece0451e4cd4205156`  
_HTTPHoplight_ | LABYRINTH CHOLLIMA | `ceccb2339088fa2d6337082704bbf67f84eeb0d0b60ce5ab0ab7e1824002fa4c`  
_OpenSSL Downloader_ | LABYRINTH CHOLLIMA | `f749c7e84809ffc3939eaed06ad90e15b0e11375f98d7348c0aa1bf35d3f0b8e`  
_UnderGroundRAT_ | LABYRINTH CHOLLIMA | `f9586fdf4e0a65b17ee32bc3c3f493a055409abde373720d594d27fd24adffa0`  
_NedDnLoader_ | LABYRINTH CHOLLIMA | `512877c98fd83cd51bb287da4462b44f9d276d7ce51890f4ded1b915a6d2d5e1`  
_Stackeyflate_ | LABYRINTH CHOLLIMA | `d2e743216d17e97c8d1913d376d46095b740015f26a3c62a05e286573721d26c`  
_HiberRAT_ | LABYRINTH CHOLLIMA | `58f2972c6a8fc743543f7b8c4df085c5cf2c6e674e5601e85eec60cd269cfb3c`  
_WinWebDown_ | LABYRINTH CHOLLIMA | `fc885b323172106ab6f2f0cc77b609987384a38e3af41ad888d5389610d29daf`  
_FudModule_ | LABYRINTH CHOLLIMA, GOLDEN CHOLLIMA | `cbd1634cf7c638f2faf5e3ec79137db6704ec9de8df798fc46aeeed38de3da9b`  
_Scuzzyfuss_ | PRESSURE CHOLLIMA | `b9f6a9d4f837f5b8a5dc9987a91ba44bc7ae7f39aa692b5b21dba460f935a0ae`  
_MataNet_ | PRESSURE CHOLLIMA | `357c9daf6c4343286a9a85a27bc25defdc056877ce1be2943d2e8ede3bce022c`  
_SwDownloader_ | PRESSURE CHOLLIMA | `a61ecbe8a5372c85dcf5d077487f09d01e144128243793d2b97012440dcf106e`  
_SparkDownloader_ | PRESSURE CHOLLIMA | `9ba02f8a985ec1a99ab7b78fa678f26c0273d91ae7cbe45b814e6775ec477598`  
_TwoPence Electric_ | PRESSURE CHOLLIMA | `081804b491c70bfa63ecdbe9fd4618d3570706ad8b71dba13e234069648e5e48`  
_MagikCookie_ | PRESSURE CHOLLIMA | `1579347265f948f9646931335d57e7960fe65dd429394be84b4ae15bca73dfde`  
_StatusSymbol_ | PRESSURE CHOLLIMA | `666c50b8b772101b0e2e35ff1de52a278c2727027b54858e457571d296fec50b`  
_GhostShip_ | PRESSURE CHOLLIMA | `56e51244e258c39293463c8cf02f5dddb085be90728fab147a60741cf014aa4d`  
_AlertConf_ | PRESSURE CHOLLIMA | `e0aa5ef3af26681a8c8b46d95656580779d0ff3c2fe531b95a59ee918686e443`  
_Jeus_ | GOLDEN CHOLLIMA | `fe948451df90df80c8028b969bf89ecbf501401e7879805667c134080976ce2e`  
_HTTPHelper_ | GOLDEN CHOLLIMA | `ff32bc1c756d560d8a9815db458f438d63b1dcb7e9930ef5b8639a55fa7762c9`  
_SnakeBaker_ | GOLDEN CHOLLIMA | `b6995c31a7ee88392fc25fd6d1a3a7975b3cb4ec3a9a318c3fcfaaf89eb65ce1`  
_NodalBaker_ | GOLDEN CHOLLIMA | `0518a163b90e7246a349440164d02d10f31d514a7e5cce842b6cf5b3a0cc1bfa`  
_PipeDown_ | GOLDEN CHOLLIMA | `2ef212f433b722b734d80b41a2364a41ca0453dbfe3e6ec8b951eca795075a02`  
_DevobRAT_ | GOLDEN CHOLLIMA | `fde50c3a373ebc2661e08c99c1cb50dc34efc022a3880c317ab5b84108ef83aa`  
_Anycon_ | GOLDEN CHOLLIMA | `2110a6e89d98a626f846ec8deccbac057300d194933ae0cbf1ef4831a4cc829e`  
_CitriLoader_ | GOLDEN CHOLLIMA | `d0cf9c1f87eac9b8879684a041dd6a2e1a0c15e185d4814a51adda19f9399a9b`  
  
#### Sources

1\. <https://reports.dtexsystems.com/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf>

2\. <https://www.halborn.com/blog/post/explained-the-bingx-hack-september-2024> || <https://www.halborn.com/blog/post/explained-the-phemex-hack-january-2025>

3\. <https://www.microsoft.com/en-us/security/blog/2024/08/30/north-korean-threat-actor-citrine-sleet-exploiting-chromium-zero-day/>

4\. <https://www.reuters.com/business/aerospace-defense/new-pier-completed-north-korea-rocket-launch-site-satellite-imagery-shows-2025-07-17/> || <https://kcnawatch.org/newstream/1753150192-897597368/let-us-remain-true-to-our-partys-line-of-building-military-giant-by-building-mighty-new-type-warship-nampho-shipyard-vows-to-build-choe-hyon-class-destroyer-no-3-till-wpk-founding-anniversary-of-nex/>

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)