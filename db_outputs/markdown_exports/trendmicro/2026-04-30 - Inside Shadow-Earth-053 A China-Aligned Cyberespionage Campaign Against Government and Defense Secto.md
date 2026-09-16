# Inside Shadow-Earth-053: A China-Aligned Cyberespionage Campaign Against Government and Defense Sectors in Asia

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/d/inside-shadow-earth-053.html
- **Date :** 2026-04-30

---

APT & Targeted Attacks

# Inside Shadow-Earth-053: A China-Aligned Cyberespionage Campaign Against Government and Defense Sectors in Asia

A China-aligned threat group is exploiting unpatched Microsoft Exchange vulnerabilities to conduct cyberespionage against government and critical infrastructure targets across Asia and beyond.

By: Daniel Lunghi, Lucas Silva 2026/04/30 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key takeaways

  * A newly identified set of China-aligned campaigns is targeting government entities and critical infrastructure across South, East, and Southeast Asia, as well as one NATO member state. We are currently tracking this activity under the temporary intrusion set designation SHADOW-EARTH-053.
  * Nearly half the targets were also compromised by a related intrusion set (SHADOW-EARTH-054), sharing identical tool hashes and overlapping TTPs, though evidence suggests independent exploitation of the same vulnerabilities rather than direct operational coordination.
  * The group exploits N-day vulnerabilities in internet-facing Microsoft Exchange and Internet Information Services (IIS) servers (e.g., ProxyLogon chain), then deploys web shells (GODZILLA) for persistent access and stages ShadowPad implants via DLL sideloading of legitimate signed executables.
  * These older Microsoft Exchange vulnerabilities continue to serve as effective initial access vectors. SHADOW-EARTH-053's successful exploitation of these long-patched issues confirms that organizations still running legacy or unpatched Exchange servers remain at significant risk of mailbox compromise, credential theft, and prolonged attacker access.



# Summary

Through ongoing analysis of ShadowPad implants targeting South and Southeast Asia, TrendAI™ Research has uncovered a series of new related campaigns that are tracked under a temporary intrusion set (a provisional cluster of related activity pending formal attribution) designated SHADOW-EARTH-053, which we assess to be aligned with China's [broader strategic interests](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/2025-apt-report-staying-ahead-of-the-modern-threat-landscape). Our telemetry indicates that this group has targeted government entities and critical infrastructure sectors across at least eight countries over the past year.

Activity attributed to SHADOW-EARTH-053 has been traced back to at least December 2024, indicating the group has been operational for over a year. Our investigation yielded detailed insight into the attacker’s tactics, techniques, and procedures (TTPs), including the attack flow, initial access vectors, and covert communication channels.

While most observed targets were concentrated in Asia, the group's footprint extends beyond these areas: a European government belonging to NATO was also targeted. Given the target profiles, we assess that these operations are likely aimed at cyberespionage and intellectual property theft.

In nearly half of the targeted environments, we observed significant overlaps in TTPs and malware usage consistent with another temporary intrusion set, SHADOW-EARTH-054. This intrusion set has some network overlaps with [CL-STA-0049](https://unit42.paloaltonetworks.com/advanced-backdoor-squidoor/) by Unit 42 and [REF7707](https://www.elastic.co/security-labs/fragile-web-ref7707) by Elastic, two other intrusion sets that also have overlaps with [Earth Alux](/en/research/25/c/the-espionage-toolkit-of-earth-alux.html) (we examine these links in the “Attribution” section). While these activities often occurred in the same networks, the SHADOW-EARTH-054-related incidents frequently predated the deployment of ShadowPad implants by a few months. Despite this temporal gap, both intrusion sets share an arsenal of post-compromise tooling and the same initial access vector. A comprehensive analysis of these connections is provided below.

# Attack chain

The following sections provide a detailed technical analysis of SHADOW-EARTH-053, covering its capabilities, TTPs, and operational characteristics.****

##  Initial access

Our telemetry indicates that the group relies on exploiting external services to establish a foothold in target networks. We have observed them targeting server-based N-day vulnerabilities, such as the ProxyLogon chain targeting Microsoft Exchange Server ([CVE-2021-26855](https://www.cve.org/CVERecord?id=CVE-2021-26855), [CVE-2021-26857](https://www.cve.org/CVERecord?id=CVE-2021-26857), [CVE-2021-26858](https://www.cve.org/CVERecord?id=CVE-2021-26858), and [CVE-2021-27065](https://www.cve.org/CVERecord?id=CVE-2021-27065)). Despite their age, these vulnerabilities remain effective exploits in unpatched environments.

After compromising the server, the group used their access to install web shells (such as GODZILLA) and deploy ShadowPad implants. These web shells serve as persistent backdoors, allowing the attacker to maintain access and execute commands on compromised systems. The following is a representative list of common web shell filenames:

  * error.aspx
  * errorFE.aspx
  * signout.aspx
  * warn.aspx
  * data.aspx
  * page.aspx
  * TimeinLogout.aspx
  * timeout.aspx
  * charcode.aspx
  * tunnel.ashx
  * i.aspx
  * 2.aspx



The use of an ._ashx_ HTTP handler represents a minor deviation from the ._aspx_ web shells seen in earlier activity.

These files were frequently found in the following directories:

  * _?:\inetpub\wwwroot\aspnet_client\system_web_
  * _?:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth_



In one instance, ShadowPad samples were delivered via AnyDesk, a legitimate remote administration tool, suggesting the attacker either leveraged a prior compromise or obtained credentials through other means. The limited visibility into this intrusion prevents us from determining whether this represents an alternative initial access method or a later-stage deployment following an unobserved entry point. Separately, we found Linux NOODLERAT samples that were reportedly dropped via the exploitation of CVE-2025-55182 ([React2Shell](/en/research/25/l/CVE-2025-55182-analysis-poc-itw.html)). We attribute these samples to SHADOW-EARTH-053 with low confidence. Related details are in the "Linux NOODLERAT" section.

## Discovery

In one case, the threat actor conducted extensive Active Directory and Exchange infrastructure reconnaissance directly via web shell access. Commands executed by the Internet Information Services (IIS) worker process (_w3wp.exe_) included domain admin group enumeration, domain controller discovery via nltest/dclist, and targeted nslookup queries against multiple internal Exchange servers.

The attacker also deployed _csvde.exe_ (a legitimate Windows utility) to export Active Directory objects to CSV format. It also used PowerView's _Get-DomainUser_ cmdlet to enumerate user accounts and associated email addresses from a domain controller.

We also observed custom binary named _DomainMachines.exe_ enumerating machines in the domain through LDAP, then connecting directly to ports related to SMB (139,445), web server and proxies (80, 443, 8080, 8443), RDP (3389), WinRM (5985, 5986), MySQL (3306), MS SQL (1433), and Kerberos (88). While the tool could not be retrieved for in-depth analysis; however, at only 28 KB, it appears to be a lightweight utility.

# Backdoor access and malware toolkit

## ShadowPad

The main malware family used by SHADOW-EARTH-053 was [ShadowPad](/en/research/25/b/updated-shadowpad-malware-leads-to-ransomware-deployment.html), an advanced modular malware that has been used by APT41 since [2017](https://securelist.com/shadowpad-in-corporate-networks/81432/), before being [shared](https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/) among multiple China-aligned intrusion sets starting in 2019.

The malware has undergone significant evolution over its lifetime; yet the variant used by SHADOW-EARTH-053 lacks the advanced obfuscation and anti-debugging features observed in builds deployed by other groups. This suggests the group has access only to an older builder, rather than the source code itself. This version is compiled for a 32-bit architecture and has been extensively [documented](https://www.pwc.co.uk/services/technology/cyber-security-services/insights/chasing-shadows.html).

Across observed intrusions, the threat actor consistently used the same loading mechanism, composed of three different files:

  * A legitimate and signed file vulnerable to DLL sideloading
  * A malicious DLL that loads the payload from the disk or from the registry
  * The encrypted ShadowPad payload, which is stored in the registry and deleted after its first use



The following four vulnerable executables were abused:

SHA-256 | Original filename | Threat actor filename | Sideloaded DLL | Authenticode signer  
---|---|---|---|---  
4264cfb3980a068ab36d842c7ee0942f40aaf308f31ed48b41e140e59885f5c8 | GameHook.exe | runtimebroker.exe  
nvcontainer.exe | graphics-hook-filter32.dll | ORANGE VIEW LIMITED  
2e8f9fd8213d9f69044101cd029fd1797ec7afbcad40bb1f04eb93d881c04cd2 | imecmnt.exe | RuntimeBroker.exe  
osppsvc.exe | imjp14k.dll | Microsoft Corporation  
8d9433e9734dd629d74abe41ff7024c84b3a28c45671df8f4baed344de733c78 | xReport.exe | _N/A_ | Uxtheme.dll | Mainline Net Holdings Limited  
d67197bf407e74ecd77be89d0da107d5f7d37c21bdf55456c6b57df65cf429b3 | LUManager.EXE | RAVCpl64.exe | MPS.dll | Samsung Electronics CO., LTD.  
  
Table 1. Legitimate executables vulnerable to DLL sideloading abused by SHADOW‑EARTH‑053

## The TosBtKbd.dll registry loader

SHADOW-EARTH-053 uses a legitimate Toshiba Bluetooth Stack executable, renamed to _CIATosBtKbd.exe_ , to sideload a malicious DLL (_TosBtKbd.dll_). This loader employs a multistage evasion technique by retrieving its payload from the Windows Registry rather than embedding it within the binary. Upon execution, the loader calls _GetComputerNameA_ to identify the host and access a machine-specific registry key at _HKEY_CURRENT_USER\Software\\[ComputerName]_. From here, it retrieves a binary value named _scode_ , which contains the shellcode payload.

The malware then allocates memory using VirtualAlloc (configured with _PAGE_EXECUTE_READWRITE_ permissions) and executes the shellcode via callback injection. By passing the shellcode’s address as a callback parameter to the legitimate Windows API function _EnumDesktopsA_ , the malware tricks the operating system into executing the malicious code during standard desktop enumeration. This method avoids direct execution calls that often trigger security monitoring systems. Persistence was achieved via a Scheduled Task named _M1onltor_ , configured to run the sideloaded binary every five minutes with the highest privileges. Note that the specific shellcode payload could not be retrieved for analysis.

## The mdync.exe backdoor

In several attacks, an executable named _mdync.exe_ " was deployed on the victim's network. Although the file could not be retrieved for static analysis, endpoint telemetry reveals that the executable established beaconing connections to 141[.]164[.]46[.]77. We observed that this tool was dropped by the side-loaded DLL **_TosBtKbd.dll_.**

## IOX proxy

We observed the group leveraging the [IOX](https://github.com/EddieIvan01/iox/) proxy by creating local accounts and setting the _LocalAccountTokenFilterPolicy_ value to 1. This configuration grants full administrative privileges to remote connections from all local administrators (and not just the built-in RID 500 account), enabling lateral movement via Pass-the-Hash.

## Additional tunneling and proxy tools

Beyond IOX, we observed SHADOW-EARTH-053 deploying multiple tunneling tools within a single environment, suggesting a layered approach to maintaining covert communication channels. These include:

  * GOST (GO Simple Tunnel): An open-source tunnel written in Go, GOST was used to establish SOCKS5 proxies and WebSocket-based tunnels to external infrastructure. The attacker configured both local SOCKS5 listeners and relay-based reverse tunnels to the IP address 96[.]9[.]125[.]227.
  * Wstunnel: Another open-source tunneling tool deployed as _wt.exe_ , Wstunnel was configured to tunnel SOCKS5 traffic over HTTPS to the same command-and-control (C&C) IP address.



We also saw the threat actor rename a tool from _tunnel-core.exe_ to _code.exe_ and pass a single parameter (_client.toml_) to it. We observed communications to the IP address 96[.]9[.]125[.]227 on port 8067, however the tool itself was not available for further inspection.

The deployment of multiple tunneling tools to the same C&C address suggests operational redundancy, ensuring persistent outbound connectivity even if individual tools are detected and blocked. All tools were staged in C:\Users\Public, consistent with the group's known preference for publicly writable staging directories.

## Linux NOODLERAT

In mid-December 2025, SHADOW-EARTH-053 retrieved one ShadowPad sample from the IP address 194[.]38[.]11[.]3 listening on port 1790. Sandbox telemetry showed Linux samples being retrieved from the same IP and port in early December. These samples were [NOODLERAT](https://www.trendmicro.com/en_us/research/24/f/noodle-rat-reviewing-the-new-backdoor-used-by-chinese-speaking-g.html) ELF files, a malware family that is shared among multiple groups performing espionage or cybercrime, and which we have extensively [covered](https://www.trendmicro.com/en_us/research/24/f/noodle-rat-reviewing-the-new-backdoor-used-by-chinese-speaking-g.html) in previous blog entries.

The NOODLERAT samples used the domain check[.]office365-update[.]com as C&C, which was registered on November 19, 2025. This domain name matches registration patterns found for other recent domain names belonging to SHADOW-EARTH-053. For these reasons, and following our [threat attribution framework](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/threat-attribution-framework-how-trendai-applies-structure-over-speculation), we attribute these samples to SHADOW-EARTH-053 with low confidence. These samples were also observed by [multiple](https://www.sophos.com/en-us/blog/react2shell-flaw-cve-2025-55182-exploited-for-remote-code-execution) [vendors](https://cloud.google.com/blog/topics/threat-intelligence/threat-actors-exploit-react2shell-cve-2025-55182) as part of the active exploitation of [CVE-2025-55182](https://www.microsoft.com/en-us/security/blog/2025/12/15/defending-against-the-cve-2025-55182-react2shell-vulnerability-in-react-server-components/) (React2Shell).

## Defense evasion

**RingQ**

In one targeted environment, we detected a sample of RingQ, which is an open-source tool of Chinese origin available on GitHub that is designed to pack malicious binaries in order to evade detection by security solutions.

The intrusion set also uses domain names that impersonate products, security solution companies, or are related to the DNS protocol, likely to make them appear legitimate.

We also observed the group renaming legitimate Windows system binaries to evade process-based detection. In one incident, _net.exe_ was copied to C:\ProgramData with randomized filenames using a _$[RANDOM].log_ naming pattern (e.g., _$D5PLAA1.log_ , _$9XF5WLD.log_). PowerShell binaries were similarly disguised (e.g., _$C06KCQ2.log_ , _$VMB9AIT.log_ , _$6T8BLJP.log_). This technique targets security solutions that rely on process name matching rather than binary hash verification.

## Lateral movement

SHADOW-EARTH-053 uses Windows Management Instrumentation Command-line (WMIC) for lateral movement, installing backdoors and tools onto additional hosts. We also observed the group deploying a suspected custom remote desktop protocol (RDP) launcher (under the name _smss.exe_) and a C# implementation of SMBExec known as [Sharp-SMBExec](https://github.com/checkymander/Sharp-SMBExec/).

In one environment, the group propagated web shells to additional internal Exchange servers by copying them over administrative shares (e.g., _copy charcode.aspx \\\\[IP]\c$\inetpub\wwwroot\aspnet_client\system_web\_). This technique allows rapid expansion across the Exchange infrastructure without deploying additional tooling, leveraging existing administrative credentials and the compromised web shell as an execution platform.

## Credential access and privilege escalation

The group collects credentials that can be used to further its objectives, notably through the use of the [Evil-CreateDump](https://www.virustotal.com/gui/file/0eb72c1f1605d999488d903021d82a9ff4b937e6c1a1da50c55440f018e83ad9/detection) tool. The tool appears to be based on Microsoft's [_create-dump.exe_](https://fossies.org/windows/misc/PowerShell-7.5.4-win-x64.zip/) utility, likely modified to target LSASS process memory for credential extraction. 

Mimikatz was executed directly via _rundll32.exe_ with command-line arguments for credential extraction (sekurlsa::logonpasswords) and local SAM database dumping (lsadump::sam). These commands were spawned by the IIS worker process (_w3wp.exe_), confirming execution through a web shell.

Additionally, we observed the group dropping and executing a binary called _newdcsync_ , which, based on the command line and filename, was likely used for DCSync attacks.

## Collection and exfiltration

We observed the attacker deploying the RAR executable, and in one instance, we saw the creation of a password-protected RAR archive containing messages (a PST file) from an executive in the targeted company.

In one specific case, SHADOW-EARTH-053 used its access to the victim’s Exchange server to install a snap-in for Exchange management. The process revealed an iterative approach: initial attempts to enumerate mailboxes via Get-Mailbox failed, prompting the attacker to explicitly load the snap-in (_Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn_) and bypass execution policy. Subsequent iterations refined the technique further, switching from Get-Mailbox to Get-User for a broader scope, and adding fields such as userAccountControl and AccountDisabled to identify active high-value accounts. This progression from noisy initial attempts to more refined, stealthier commands was observed within a single session.

Additionally, the threat actor used a custom “ExchangeExport” tool to export the mailbox content of high-profile users via the Exchange Web Services (EWS) API. Microsoft observed similar activity by [Silk Typhoon](https://www.microsoft.com/en-us/security/blog/2025/03/05/silk-typhoon-targeting-it-supply-chain/) (Hafnium). Unfortunately, the tool could not be retrieved for further analysis.

# Victimology

Our investigation indicates that this campaign has a distinct geographic focus, primarily targeting governmental entities, mostly in Asia. Most observed targets were concentrated in South, East, and Southeast Asia, particularly:

  * Pakistan
  * Thailand
  * Malaysia
  * India
  * Myanmar
  * Sri Lanka
  * Taiwan



Note that despite focusing on Asia, the threat actor’s footprint extended beyond this region, with at least one target in Poland. This distribution suggests a strategic interest in Asian geopolitical entities, while the global targets may indicate opportunistic exploitation or a broadening of the group’s scope.

Beyond the government sector, SHADOW-EARTH-053 also targeted the technology industry. In at least two countries, we observed the group focusing on IT consulting firms holding government contracts, particularly those that listed the Ministry of Defense as one of their customers.

Finally, we found limited number of victims within the transportation industry in Southeast Asia.

# Overlaps

Our investigation revealed that multiple targets were compromised up to 8 months before the deployment of ShadowPad, using identical entry points. In these earlier instances, the attackers gained access via vulnerable IIS or Microsoft Exchange servers and subsequently deployed web shells to maintain persistence.

Three possible scenarios may explain the relationship between the groups:

  * **Independent exploitation:** SHADOW-EARTH-053 independently exploited these servers by leveraging the same vulnerabilities previously used by SHADOW-EARTH-054. This scenario matches the "Type A" collaboration from our Premier Pass-as-a-Service model [published](https://www.trendmicro.com/en_us/research/25/j/premier-pass-as-a-service.html) last year. This involves the deployment of backdoors through web shells, exploitation of vulnerable public facing servers, and similar initial access techniques. In such cases, any observed coordination between intrusion sets is likely incidental rather than intentional.
  * **Asset repurposing:** SHADOW-EARTH-053 simply repurposed the web shells left behind from the earlier intrusion by SHADOW-EARTH-054.**__**
  * **Same group** : SHADOW-EARTH-053 and SHADOW-EARTH-054 are a single group using multiple TTPs.**__**



In three recent cases, a malicious loader family attributed to SHADOW-EARTH-054 was detected in organizations previously targeted by SHADOW-EARTH-054 and later by SHADOW-EARTH-053. The same vulnerabilities were exploited again to deliver this loader, with no apparent connection to previously deployed malware. This pattern reinforces our assessment of a Type A collaboration — independent exploitation of the same vulnerabilities, with no evidence of operational coordination between the two intrusion sets. It also renders the third scenario unlikely, as targeting an already-compromised organization using a different malware toolkit would be operationally inconsistent.

In addition to the similarities in initial breach vectors, we identified significant overlap in **post-exploitation capabilities**. Both groups utilized an identical toolkit, leveraging a mix of custom-developed malware and utilities:

  * Evil-CreateDump
  * IOX Proxy



Notably, our analysis confirmed that these artifacts shared **identical file hashes** , indicating the use of the exact same binaries rather than just similar software.

Notably, the following activity sequence was observed at the same endpoints:

  1. Compromise with SHADOW-EARTH-054 malware (late 2024/early 2025).
  2. Deployment of ShadowPad implants by SHADOW-EARTH-053 (mid-2025).
  3. Re-exploitation by SHADOW-EARTH-054 (early 2026).



The following image shows the timeline of events:

[ ![Figure 1. Timeline of SHADOW-EARTH-053 and SHADOW-EARTH-054 activities](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure01.png) ](/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure01.png)

Figure 1. Timeline of SHADOW-EARTH-053 and SHADOW-EARTH-054 activities

[ download ](/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure01.png)

Notably, nearly half of the targets of SHADOW-EARTH-053 were also targeted by SHADOW-EARTH-054, primarily in Malaysia, Sri Lanka, and Myanmar. We also identified targets unique to SHADOW-EARTH-054 in Malaysia, Brazil, and Taiwan, operating in similar industries to those targeted by SHADOW-EARTH-053, plus a telecommunications equipment reseller.

[ ![Figure 2. SHADOW-EARTH-053 and SHADOW-EARTH-054 targets](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure02.png) ](/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure02.png)

Figure 2. SHADOW-EARTH-053 and SHADOW-EARTH-054 targets

[ download ](/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure02.png)

| SHADOW-EARTH-053 | SHADOW-EARTH-054  
---|---|---  
Infection Vector | Microsoft Exchange Vulnerabilities | Microsoft Exchange Vulnerabilities  
Malware Toolkit | ShadowPad  
TosBtKbd.dll registry loader  
mdync.exe malware | Custom loaders  
VShell  
Loader Filenames | RuntimeBroker.exe  
nvcontainer.exe  
osppsvc.exe  
CIATosBtKbd.exe | RuntimeBroker.exe  
SystemEventsBrokerTrustedService.exe  
identity_helper.exe  
Post-Exploitation Toolkit | evil-createdump.exe  
IOX (Named explorer.exe) | evil-createdump.exe  
IOX (Named explorer.exe or svchost.exe)  
Custom Tools for Launching Privileged Processes  
Targeted Regions | South Asia Southeast Asia East Asia Europe | South Asia Southeast Asia East Asia Latin America  
  
Although both groups exhibit significant overlaps in victimology and TTPs, we have chosen to categorize them into two distinct temporary intrusion sets based on the details outlined above.

# Attribution and motivation

The deployment of malware families (most notably ShadowPad) is strongly associated with China-aligned intrusion sets. Both the selected targets and operational timing also align closely with geopolitical events and strategic interests in the region.

During the investigation, we quickly found that two different groups were operating in similar environments. Regarding SHADOW-EARTH-053, we found no strong overlap with any known publicly reported group. Meanwhile, for SHADOW-EARTH-054, we found multiple malware loaders that we could not attribute, and a [VShell](https://blog.nviso.eu/wp-content/uploads/2025/11/VShell.pdf) [sample](https://www.sysdig.com/blog/unc5174-chinese-threat-actor-vshell) that communicates with 209[.]141[.]40[.]254.

This malware family used to be open source and is known for being used by multiple intrusion sets. We also noticed the threat actor issuing a “ping” command to zimbra-beta[.]info. Both the IP address and the domain name are listed in a report on [CL-STA-0049](https://unit42.paloaltonetworks.com/advanced-backdoor-squidoor/), an intrusion set that primarily uses the SQUIDOOR malware (which we call VARGEIT).

The infection vector used by CL-STA-0049 matches what we observed, however none of the other TTPs match, and we found no traces of VARGEIT. Therefore, we chose to use the temporary name SHADOW-EARTH-054.

We know of two other intrusion sets using VARGEIT: [Earth Alux](https://www.trendmicro.com/en_us/research/25/c/the-espionage-toolkit-of-earth-alux.html) and [REF7707](https://www.elastic.co/security-labs/fragile-web-ref7707), where the malware is called [FinalDraft](https://www.elastic.co/security-labs/finaldraft). Again, none of the TTPs from the related reports match the activity we observed from SHADOW-EARTH-054.

[ ![Figure 3. Attribution overlap diagram showing connections between SHADOW-EARTH-054, CL-STA-0049, Earth Alux, and REF7707](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure03.png) ](/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure03.png)

Figure 3. Attribution overlap diagram showing connections between SHADOW-EARTH-054, CL-STA-0049, Earth Alux, and REF7707

[ download ](/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/shadow-earth_figure03.png)

The intrusion set’s ultimate objective remains unclear; the sensitive nature of the targets suggests that this activity is likely related to cyberespionage against foreign countries and intellectual property theft. We also found one instance where SHADOW-EARTH-054 tried to reach the webmail of a Ministry of Defense in Southeast Asia from the environment of a technology customer, suggesting a possible supply chain attack scenario.

# Risk management guidance

The primary entry vector used in this campaign were vulnerabilities in internet-facing IIS applications. Organizations should prioritize applying the latest security updates and cumulative patches to Microsoft Exchange and any web applications hosted on IIS. In scenarios where immediate patching is not feasible, we strongly recommend deploying Intrusion Prevention Systems (IPS) or Web Application Firewalls (WAF) with rulesets specifically tuned to block exploit attempts against these known CVEs (Virtual Patching).

To counter the deployment of web shells, administrators should implement strict File Integrity Monitoring (FIM) on critical web directories (e.g., C:\inetpub\wwwroot or Exchange Client Access paths). Alerts should be configured for the creation or modification of executable server-side scripts (such as ._aspx_ , ._ashx_ , or ._jsp_) in these directories. Affected paths should also be scanned for unreferenced or suspicious files, with particular attention to files with mismatched timestamps or high entropy (indicating obfuscated code).

Organizations can also reduce the attack surface by hardening IIS configurations:

  * **Restrict permissions:** Organizations should ensure that the IIS worker process (_w3wp.exe_) runs with the lowest possible privileges and does not have administrative rights or the ability to write to arbitrary directories.
  * **Disable unused features:** IT and security teams should remove unnecessary IIS modules and handlers that are not required for business operations.
  * **Application whitelisting:** Enterprises should enforce policies that prevent the IIS process from launching unauthorized binaries or script interpreters.



The presence of a web shell often leads to anomalous process execution. Security teams should monitor Endpoint Detection and Response (EDR) telemetry for:

  * **Suspicious child processes:** Organizations should set up alerts for when the IIS worker process spawns command shells (e.g., _cmd.exe_ , _powershell.exe_) or reconnaissance tools (e.g., _whoami.exe_ , _net.exe_). This is a high-fidelity indicator of remote code execution.
  * **Anomalous network traffic:** Security teams should monitor for unexpected outbound connections initiated by the web server, which may indicate C&C communication.
  * **Organizations should also monitor and restrict access to directories commonly used as staging grounds, including C:\ProgramData, C:\Users\Public, C:\PerfLogs, and C:\Windows\Temp**. These locations are frequently exploited by threat actors to drop and execute payloads without requiring immediate administrative privileges, and their broad write permissions make them easy to overlook during routine inspection.



# Conclusion

SHADOW-EARTH-053 represents a persistent and methodical China-aligned threat actor operating across Asia and beyond. By exploiting long-known but still-unpatched vulnerabilities in internet-facing Exchange and IIS servers, the group has successfully compromised government ministries, defense-adjacent contractors, and transportation organizations across at least eight countries, demonstrating that N-day vulnerabilities remain a viable and effective entry point even years after their disclosure.

The relationship between SHADOW-EARTH-053 and SHADOW-EARTH-054 adds a further layer of complexity to the threat landscape. While the two intrusion sets share tooling, initial access methods, and victim overlap, the available evidence points to independent exploitation of the same vulnerabilities rather than coordinated operation. This pattern underscores the scale and persistence of state-sponsored espionage activity targeting Asian government and critical infrastructure sectors.

Organizations operating internet-facing Microsoft Exchange or IIS infrastructure, particularly in the affected regions, should treat this campaign as a strong signal to audit patch levels, review web shell detection capabilities, and scrutinize outbound traffic from web servers. The indicators of compromise and threat hunting queries provided in this report offer a practical starting point for identifying potential exposure.

# Proactive security with TrendAI Vision One™ 

[TrendAI Vision One™](/en/business/products/one-platform.html) platform is the industry-leading AI cybersecurity platform that centralizes cyber risk exposure management, security operations, and robust layered protection. 

# [](https://www.trendmicro.com/en_us/business/products/one-platform.html)TrendAI Vision One™ Threat Intelligence Hub 

[TrendAI Vision One™ Threat Intelligence Hub](/en/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. This research was first reported to Threat Intelligence Hub subscribers in February 2026.

**Emerging Threats:** [SHADOW-EARTH-053 and SHADOW-EARTH-054: Overlapping Cyberespionage Groups Targeting Government Entities in Asia](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Investigating%20SHADOW-EARTH-053%20Activities%20Across%20South%20and%20Southeast%20Asia) __

**Threat Actors:** [SHADOW-EARTH-053](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=SHADOW-EARTH-053 "SHADOW-EARTH-053")

## TrendAI Vision One™ Intelligence Reports (IOC Sweeping) 

[SHADOW-EARTH-053 and SHADOW-EARTH-054: Overlapping Cyberespionage Groups Targeting Government Entities in Asia](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=SHADOW-EARTH-053)

# Hunting Queries

## TrendAI Vision One™ Search App 

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

Possible Webshell: eventSubId: 101 AND objectFilePath: (*.aspx OR *.ashx OR *.jsp) AND processFilePath: *\\\w3wp.exe

More hunting queries are available for TrendAI Vision One™ with [Threat Intelligence Hub](/en/business/products/threat-intelligence.html) entitlement enabled. 

# Indicators of Compromise (IoCs)

The IoCs for the threats discussed in this entry can be found [here](/content/dam/trendmicro/global/en/research/26/d/shadow-earth-053/ioc-report-shadow-earth-053-054_updated_05-28.txt).

Tags

[Malware](/en/research.html?category=trend-micro-research:threats/malware) | [APT & Targeted Attacks](/en/research.html?category=trend-micro-research:threats/apt-and-targeted-attacks) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Daniel Lunghi

Threat Researcher

  * Lucas Silva

Threat Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)