# Inside CrowdStrike’s Takedown of a Developer-Targeting Botnet

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/inside-crowdstrike-takedown-of-a-developer-targeting-botnet/
- **Date :** May 26, 2026

---

# Disrupting Glassworm: Inside CrowdStrike’s Takedown of a Developer-Targeting Botnet

May 26, 2026

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


On May 26, 2026, at 14:00 UTC, the [CrowdStrike Counter Adversary Operations](https://www.crowdstrike.com/en-us/platform/threat-intelligence/) team executed a coordinated takedown of the Glassworm botnet, a global threat targeting software developers through the open-source supply chain. In collaboration with Google and the Shadowserver Foundation, we struck all four of Glassworm's command-and-control (C2) channels simultaneously, severing the operators from their infected machines and their ability to deliver new malicious payloads.

This takedown matters beyond the botnet. Glassworm marked a significant shift in the threat landscape that should serve as a wake-up call for every organization that ships or consumes software. Adversaries are no longer just targeting products, they're targeting the developers who build them.

## The Threat: Targeting Developers

Since at least early 2025, Glassworm operators have systematically targeted software developers, a population with access to source code repositories, cloud platforms, CI/CD pipelines, and package registries. Developers represent uniquely high-value targets: compromising a single developer's workstation can cascade into a supply-chain compromise that impacts thousands of downstream organizations and users.

![](https://www.crowdstrike.com/content/dam/crowdstrike/marketing/en-us/images/blog/2026/05/Blog-Glassworm-1.png)

Glassworm's operators exploited this reality with a multi-pronged campaign:

  * **Trojanized VSCode extensions** were published to the OpenVSX marketplace, disguised as popular tools like time trackers and code formatters. The malicious extensions targeted not only VSCode but also Cursor, Positron, Windsurf, VSCodium, and more.
  * **Compromised npm and Python packages** introduced malicious code through postinstall hooks and setup scripts — executing silently during routine dependency installation.
  * **More than 300 GitHub repositories** were poisoned using stolen developer credentials harvested from earlier Glassworm infections, with malicious code force-pushed into default branches.



This cross-platform operation affected Windows, macOS, and Linux systems, with capabilities spanning information theft, credential harvesting, and a full-featured Node.js remote access tool dubbed GlasswormRAT.

## A Coordinated Disruption

Glassworm's operators built their infrastructure for resilience. The botnet's C2 architecture relied on four distinct channels designed to resist traditional takedown efforts:

  1. **Solana blockchain** : C2 server addresses are encoded in the memo fields of blockchain transactions, creating an immutable, publicly accessible dead-drop that cannot be taken offline through conventional means.

  2. **BitTorrent Distributed Hash Table (DHT)** : The GlasswormRAT queries the BitTorrent peer-to-peer network for configuration data stored against hardcoded public keys, leveraging a global decentralized network with no single point of failure.

  3. **Public calendar service** : Glassworm uses Google Calendar event titles as dead-drop locations for Base64-encoded C2 paths.

  4. **Direct server connections** : Traditional C2 infrastructure hosted on commercial VPS providers served as the final payload delivery mechanism.




The combination of blockchain, peer-to-peer, and legitimate web services as resolution layers was designed to be resilient against takedowns — a dynamic front protecting the actual C2 servers behind multiple layers of indirection.

![](https://www.crowdstrike.com/content/dam/crowdstrike/marketing/en-us/images/blog/2026/05/Blog-Glassworm-2.png)

Disrupting this architecture required precision and timing. Taking down only one channel would have left the others operational, allowing the operators to quickly reconstitute. All four channels had to be disrupted simultaneously in a coordinated effort. As a result, infected machines can no longer receive new instructions or payloads.

## The Example This Sets

The Glassworm takedown sets a model for how the security community must approach supply-chain threats going forward.

The operators behind Glassworm are well-resourced and persistent. Over the course of more than a year, they continuously evolved: adopting new programming languages (from JavaScript to Rust to Zig), expanding across package ecosystems (VSCode, npm, PyPI, GitHub), and building redundant infrastructure designed to survive takedown attempts. Left unchecked, their access to developer credentials and systems posed ongoing risk of high-impact supply-chain compromises affecting organizations far beyond the initially infected developers.

The criminals are likely based in Russia. The evidence is a classic: The malware checks the victim's locale, language settings, and timezone at runtime, and quietly exits if it determines the machine is in a CIS country, a well-known tactic among cybercriminals in the region who avoid targeting systems close to home. Russian-language comments appear throughout the source code. No single indicator is proof on its own — locale checks can be copied, and code comments may reflect AI tooling rather than a native speaker — but the pattern is clear and consistent across more than a year of observed activity.

This case demonstrates:

  * **Proactive disruption of cyber threats is achievable** , even against infrastructure deliberately designed for resilience.
  * **Precision strikes can cripple criminal operations** without requiring years of judicial process, by targeting the technical dependencies that adversaries cannot easily replace.
  * **Cross-sector collaboration works.** Combining threat intelligence from private industry with law enforcement authority and platform cooperation from technology companies creates the conditions for decisive action.
  * **Disruption liberates victims.** By severing command-and-control, infected machines are freed from adversary control, giving organizations the window they need to detect and remediate compromises.



## How to Identify Infections

To help organizations determine whether they have been affected by Glassworm, we are sharing a key network indicator: All Glassworm-infected machines now beacon to the benign CrowdStrike-operated IP address `164.92.88[.]210`. Organizations should review network logs and endpoint telemetry for connections to this address. Any match indicates a Glassworm infection that requires immediate remediation. The following [YARA](https://virustotal.github.io/yara/) rules can be used to confirm infections on identified hosts:
    
    
    rule CrowdStrike_GlasswormRat_01 : glassworm glasswormrat 
    {
        meta:
            copyright = "(c) 2026 CrowdStrike Inc."
            description = "Characteristic strings in Glassworm's RAT script"
            last_modified = "2026-03-23"
            malware_family = "GlasswormRAT"
        strings:
            $download = "DownloadManager" ascii
            $socks = "start_socks" ascii
            $nodejs = "https://nodejs.org/download/release" ascii
            $dht = "bootstrap" ascii
        condition:
            all of them
    }
    
    rule CrowdStrike_GlasswormDownloader_01 : glassworm 
    {
        meta:
            copyright = "(c) 2026 CrowdStrike Inc."
            description = "Characteristic strings in the obfuscated python installer Glassworm variant"
            last_modified = "2026-03-13"
            malware_family = "Glassworm"
        strings:
            $zlib = "__import__('zlib')" ascii
            $decomp = "decompress(" ascii
            $lambda = "lambda" ascii
            $exec = /exec\(compile\(.{5,20}, '<>', 'exec'\)\)/
        condition:
            all of them and filesize < 10KB
    }
    

## Detection Alone Is Not Enough

The scope of Glassworm's campaign illustrates a hard truth about the state of software supply-chain security: _**Defending against these threats through after-the-fact detection alone is virtually impossible.**_ Malicious packages are installed through dependency updates in seconds, and detections usually happen when the harm is already done.

There are dozens of package ecosystems — npm, PyPI, OpenVSX, GitHub repositories — each with millions of packages and limited built-in security controls. Attackers can publish malicious code and reach thousands of victims within minutes. The Glassworm operators cycled through these package ecosystems while maintaining consistent access to developer machines.

This is why efforts to secure the software supply chain must be combined with a more aggressive posture against already established threats. This requires going beyond detection to actively dismantle the infrastructure that threats like Glassworm depend on.

## Conclusion

This type of supply chain attack seeks maximum scale, minimum effort, and stealth. The software supply chain remains one of the most consequential attack surfaces in modern computing. Adversaries are turning an organization's dependencies on tools, updates, and libraries into weaponized delivery mechanisms and force multipliers. The barrier to poisoning a package or extension is low; the potential blast radius is enormous. As long as developer environments, build pipelines, and code repositories remain under-protected, every organization that consumes software inherits the risk of everyone who produces it. Glassworm demonstrates that attackers know this and are investing in resilient infrastructure to maintain persistent access to developer ecosystems.

The security community — vendors, law enforcement agencies, platform operators, and the open-source ecosystem — must respond with equal determination. We need more operations and coordinated disruptions like this one. CrowdStrike is committed to taking the fight to the adversaries.

#### Additional Resources

  * _Learn more about[CrowdStrike Counter Adversary Operations](https://www.crowdstrike.com/en-us/platform/threat-intelligence/) threat intelligence and threat hunting._
  * _Tune in to the[Adversary Universe podcast](https://www.crowdstrike.com/en-us/resources/adversary-universe-podcast/), where CrowdStrike reveals the threat actors behind the latest cyberattacks. _



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)