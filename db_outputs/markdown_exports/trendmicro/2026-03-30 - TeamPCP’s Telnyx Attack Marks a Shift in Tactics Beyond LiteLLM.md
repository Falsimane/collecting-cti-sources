# TeamPCP’s Telnyx Attack Marks a Shift in Tactics Beyond LiteLLM

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/c/teampcp-telnyx-attack-marks-a-shift-in-tactics.html
- **Date :** 2026-03-30

---

Malware

# TeamPCP’s Telnyx Attack Marks a Shift in Tactics Beyond LiteLLM

Moving beyond their LiteLLM campaign, TeamPCP weaponizes the Telnyx Python SDK with stealthy WAV‑based payloads to steal credentials across Linux, macOS, and Windows.

By: John Rainier Navato 2026/03/30 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key takeaways

  * Attackers published tainted Telnyx versions 4.87.1 and 4.87.2 to PyPI, activating on import via injected code in _client.py.
  * The payload uses split file injection, runtime Base64 decoding, and WAV-based steganography to hide credential stealing malware.
  * Unlike the earlier LiteLLM incident, the Telnyx variant adds Windows support with Startup folder persistence alongside Linux and macOS execution.
  * Any system that installed the affected versions should be treated as fully compromised; users are strongly advised to downgrade to the last known clean release, Telnyx 4.87.0, as soon as possible.



Three days after compromising the LiteLLM [AI](https://www.trendmicro.com/en_us/what-is/ai.html) proxy package, TeamPCP struck again. On March 27, 2026, two malicious versions of the Telnyx Python SDK, a cloud communications library with over [700,000 downloads in February](https://pypistats.org/packages/telnyx), were published to PyPI. The payload represents a clear shift in the campaign's tradecraft, combining WAV-embedded credential-stealing code via steganography, split-file code injection to evade visual inspection, and the campaign's first Windows-specific persistence mechanism. PyPI quarantined versions 4.87.1 and 4.87.2 at 10:13 UTC (following roughly 6.5 hours of exposure), according to the [project's GitHub security advisory](https://github.com/team-telnyx/telnyx-python/issues/235).

In this blog entry, we examine the Telnyx compromise and present our technical analysis, detailing how the malicious packages were weaponized, what changed from the earlier LiteLLM incident, and what defenders should watch for. We will update the entry as new information emerges from our monitoring and analysis.

For background on the broader TeamPCP campaign and the LiteLLM compromise, read our prior analysis: [Your AI Gateway Was a Backdoor: Inside the LiteLLM Supply Chain Compromise.](/en/research/26/c/inside-litellm-supply-chain-compromise.html)

# Overview

At 03:51 UTC on March 27, Telnyx versions 4.87.1 and 4.87.2 appeared on PyPI without any corresponding commits in the upstream GitHub repository. Our analysis confirms that malicious code was injected into telnyx/_client.py, with all execution paths triggered at module scope, meaning a simple import telnyx is sufficient to activate the payload.

Attribution to TeamPCP is definitive. Our analysis found multiple elements that are byte-for-byte identical to the LiteLLM payload: the RSA-4096 public key, the tpcp.tar.gz campaign ID, the X-Filename: tpcp.tar.gz exfiltration header, the OpenSSL encryption chain (rand + AES-256-CBC + RSA-OAEP + tar), the temporary file naming convention, and the subprocess stdin pipe execution pattern. This confirms reuse of the same toolchain.

As of writing, we have not been able to determine how TeamPCP obtained the Telnyx project's PyPI publishing credentials. The project's GitHub advisory states that no workflow-level credential exposure was identified, and the PyPI trusted publisher (OIDC) was not configured.

# Split-file injection: Increased evasion

The LiteLLM payload injected a contiguous block of malicious code between two legitimate code sections, making it visible to anyone scrolling through the file. The Telnyx variant improves on this by distributing its malicious components across three widely separated locations in _client.py:

  * A Base64 decode wrapper function (_d()), buried among legitimate imports.
  * The Linux orchestrator and credential harvester as a 4,428-character Base64 string, placed between __all__ and the class definition.
  * The Windows execution path with WAV steganography logic, appended after all legitimate classes at the end of the file.



[ ![Figure 1. Base64 decode wrapper function, buried among legitimate imports](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-1.png) ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-1.png)

Figure 1. Base64 decode wrapper function, buried among legitimate imports

[ download ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-1.png)

[ ![Figure 2. Linux orchestrator and harvester as a 4,428-char Base64 string, placed between __all__ and class definition](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-2.png) ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-2.png)

Figure 2. Linux orchestrator and harvester as a 4,428-char Base64 string, placed between __all__ and class definition

[ download ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-2.png)

All sensitive strings in the Windows path are obfuscated using the _d() wrapper, which Base64-decodes strings at runtime. This differs from LiteLLM where strings remained in plaintext within the Base64-encoded payload. Decoded values include the Startup folder path, the msbuild.exe filename, and the command-and-control (C&C) URL.

[ ![Figure 3. The malware's Windows and Linux Execution path functions, both called at module scope import](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-3.png) ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-3.png)

Figure 3. The malware's Windows and Linux Execution path functions, both called at module scope import

[ download ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-3.png)

# The shift to audio steganography

The most significant change from the LiteLLM attack is that the Telnyx variant no longer embeds the credential harvester in the source code. Instead, it downloads the harvester at runtime, hidden inside structurally valid WAV audio files hosted on the C&C server.

Our analysis of the extraction process shows that the WAV file's raw audio frames are read using Python's wave module, Base64-decoded, then split: the first 8 bytes serve as an XOR key, while the remaining bytes constitute the XOR-encrypted payload. Each byte is XORed against the rotating 8-byte key to recover the cleartext.

[ ![Figure 4 . The decoded Base64 payload for Linux downloading the WAV file, which it then decodes, and runs the resulting payload](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-4.png) ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-4.png)

Figure 4 . The decoded Base64 payload for Linux downloading the WAV file, which it then decodes, and runs the resulting payload

As a result, static analysis of the package source code reveals no harvester logic — the actual credential-stealing script exists only on the C&C server inside audio files. These WAV files pass MIME-type validation as legitimate media, bypass file extension filters, and evade string-based static analysis. This is a significant evasion improvement over the LiteLLM variant, where the full harvester was embedded as a static Base64 blob.

WAV steganography first appeared in the TeamPCP campaign on March 22 in the _kamikaze.sh_ Kubernetes wiper variant, as documented by Aikido. The Telnyx compromise shows the technique maturing from experimental use into production deployment against PyPI, compressing the cycle from prototype to production in just five days.

# Dual-platform targeting

While LiteLLM payload targeted only Linux systems, the the Telnyx variant expands support to include Windows.

## Windows path analysis

The Windows execution path downloads hangup.wav from 83[.]142[.]209[.]203:8080, extracts a PE executable via the XOR steganography technique, and installs it as msbuild.exe in %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ to establish boot persistence. The filename mimics Microsoft's legitimate MSBuild tool.

The executable is launched with the CREATE_NO_WINDOW flag (0x08000000) to suppress any visible window. An anti-replay mechanism checks for msbuild.exe.lock; if the lock file was modified within the last 43,200 seconds (12 hours), execution is skipped. This lock file is hidden via attrib +h, preventing redundant downloads and executions when the package is imported multiple times, reducing network noise and detection risk.

[ ![Figure 5. The anti-replay lock file mechanism checks msbuild.exe.lock modification time, skips if it less than 43,200 seconds \(12 hours\), and hides lock via attrib +h](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-5.png) ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-5.png)

Figure 5. The anti-replay lock file mechanism checks msbuild.exe.lock modification time, skips if it less than 43,200 seconds (12 hours), and hides lock via attrib +h

## Linux/macOS path analysis

In the Linux/macOS path, the base64 payload variable is launched as a detached background process using subprocess.Popen with start_new_session=True and suppressed output. The payload then downloads ringtone.wav from the same C&C server, extracts the credential harvester via the same WAV steganography technique, and feeds it through the standard TPCP exfiltration pipeline (AES-256-CBC + RSA-4096 OAEP -> tpcp.tar.gz -> HTTP POST).

# Infrastructure shift

The Telnyx variant abandons the domain-based HTTPS infrastructure used in LiteLLM and switches to a raw IP address over plaintext HTTP, possibly indicating that the LiteLLM domains were reported and subsequently taken down, forcing the attacker to revert to direct IP addressing. The move to plaintext HTTP also exposes the WAV file downloads and the exfiltrated tpcp.tar.gz archive to network monitoring, creating a potential detection opportunity that was not available with the HTTPS-based LiteLLM infrastructure.

| LiteLLM | Telnyx  
---|---|---  
Exfiltration | `hxxps[://]models[.]litellm[.]cloud/` | `hxxp[://]83[.]142[.]209[.]203:8080/`  
C&C server / payload | `hxxps[://]checkmarx[.]zone/raw` | `hxxp[://]83[.]142[.]209[.]203:8080/` (WAV files)  
Protocol | HTTPS (encrypted) | HTTP (plaintext)  
Addressing | Domain names | Direct IP  
  
Table 1. Infrastructure comparison between the LiteLLM and Telnyx variants

[ ![Figure 6. TeamPCP exfiltration pipeline comparison; LiteLLM \(HTTPS domains\) vs Telnyx \(plaintext HTTP on raw IP\).](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-6.png) ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-6.png)

Figure 6. TeamPCP exfiltration pipeline comparison; LiteLLM (HTTPS domains) vs Telnyx (plaintext HTTP on raw IP).

[ download ](/content/dam/trendmicro/global/en/research/26/c/telnyx/fig-6.png)

# Conclusion and recommendations

The Telnyx compromise indicates a continued change in the techniques used in TeamPCP’s supply‑chain activity, with adjustments to tooling, delivery methods, and platform coverage. In just eight days, the actor has pivoted across security scanners, AI infrastructure, and now telecommunications tooling evolving their delivery from inline Base64 to _.pth_ auto-execution, and ultimately to split-file WAV steganography, while also expanding from Linux-only to dual-platform targeting with Windows persistence.

The shift from HTTPS domains to plaintext HTTP on a raw IP address may signal mounting infrastructure pressure, but it simultaneously introduces a detection opportunity. In affected environments, indicators may include WAV file downloads from non‑media IP addresses over port 8080, unexpected msbuild.exe binaries in user Startup folders, outbound HTTP requests containing the X‑Filename: tpcp.tar.gz header, and file‑hiding activity such as attrib +h applied to .lock files.

As a precautionary measure, organizations should downgrade any installations of Telnyx 4.87.1 or 4.87.2 to the last known clean release (4.87.0) and treat systems that imported the affected versions as exposed. Organizations should also pin all PyPI dependencies by hash and closely monitor CI/CD environments for unexpected audio file downloads,

# Proactive security with TrendAI Vision One™ 

[TrendAI Vision One™](/en/business/products/one-platform.html) is the industry-leading AI cybersecurity platform that centralizes cyber risk exposure management, security operations, and robust layered protection. 

**TrendAI Vision One™ Threat Intelligence Hub**

[TrendAI Vision One™ Threat Intelligence Hub](/en/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. 

**Emerging Threats:** **[TeamPCP Hits Telnyx: WAV Steganography and Windows Targeting](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=TeamPCP%20Hits%20Telnyx%3A%20WAV%20Steganography%20and%20Windows%20Targeting)**

**TrendAI Vision One™ Intelligence Reports (IOC Sweeping)**

**[TeamPCP Hits Telnyx: WAV Steganography and Windows Targeting](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=TeamPCP%20Hits%20Telnyx%3A%20WAV%20Steganography%20and%20Windows%20Targeting)**

**TrendAI Vision One™ Search App**

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

# Hunting Queries

**Detects network connections to the campaign's C &C server **

_eventSubId:201 AND request:"*83.142.209.203*"_

More hunting queries are available for TrendAI Vision One™ with [Threat Intelligence Hub](/en/business/products/threat-intelligence.html) entitlement enabled. 

Indicators of Compromise (IoCs)

The indicators of compromise for this entry can be found [here](/content/dam/trendmicro/global/en/research/26/c/telnyx/ioc-teampcp-telnyx-attack.txt).

Tags

[Malware](/en/research.html?category=trend-micro-research:threats/malware) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * John Rainier Navato

Senior Threat Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)