# The Sharp Taste of Mimo'lette: Mimo Targets Craft CMS

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/the-sharp-taste-of-mimolette-analyzing-mimos-latest-campaign-targeting-craft-cms
- **Date :** 2025-05-27

---

_This article on was originally distributed as a private report to our customers._

## Introduction

Once upon a time, in the land of the CMS honeypot, a curious threat named Mimo crept silently through the digital woods. Unlike your typical fairytale villain, Mimo didn’t leave glass slippers—just suspicious payloads. Between February 28 and May 2, multiple exploitations of the [**CVE-2025-32432**](https://nvd.nist.gov/vuln/detail/CVE-2025-32432) were observed during our daily threat monitoring. This vulnerability is a Remote Code Execution affecting the **Craft** Content Management System. 

This report presents an analysis of the compromise chain initiated by the exploitation of CVE-2025-32432, observed on our honeypot. Our investigation dissects each intrusion phase, from the initial vulnerability exploitation to the deployment of malicious payloads, including a **loader** , a **crypto miner** and a **residential proxyware**. We also explore the intrusion set likely responsible for the campaign. Finally, we highlight several detection opportunities based on the techniques and tactics used by this intrusion set.

## Vulnerability overview

The vulnerability identified as **CVE-2025-32432** was reportedly discovered by [**Orange Cyberdefense**](https://sensepost.com/blog/2025/investigating-an-in-the-wild-campaign-using-rce-in-craftcms/) in mid-February 2025 during an incident response investigation. Officially disclosed on **April 25, 2025** , this vulnerability affects the Content Management System **Craft** and has been classified as a **remote code execution (RCE)** issue that does not require authentication leading to a CVSS score of 10.

It affects multiple versions of the affected CMS, specifically:

  * From **3.0.0-RC1 up to (but not including) 3.9.15** :
  * From **4.0.0-RC1 up to 4.14.15** ;
  * From **5.0.0-RC1 up to 5.6.17**.



According to Orange Cyberdefense’s findings, active exploitation of this vulnerability has been observed since **at least mid-February 2025** , well before its public disclosure. Following the release of the vulnerability, **several proof-of-concept (PoC) exploits** became publicly available on platforms like GitHub.

## Infection chain

### Initial access

The attacker exploited **CVE-2025-32432** to gain unauthorised access to the target system by deploying a webshell to facilitate remote access. This webshell was subsequently used to download and execute an infection script, likely intended to further compromise the system. 

The vulnerability exploitation unfolds in two distinct phases. 

  * **Step 1:** The attacker activates the web shell by injecting PHP code via a specially crafted GET request, manipulating the parameter p=admin/dashboard&a=<?=exec($_GET["cmd"]);die()?>. This action triggers a redirection, thereby prompting the application to **record the return URL** within a server-side **PHP session file**.



Once the webshell is enabled, commands can be executed remotely on the compromised machine, with any system command supplied via the cmd URL parameter being executed directly in the server's shell environment.

  * **Step 2** : The attacker sends a POST request to the index.php?p=actions/assets/generate-transform endpoint with a body that contains an illegitimate field that must start with “as ” (in our exploitation it was “as hack”) - as documented by Orange Cyberdefense - with the filepath to the PHP session file that contains the webshell, the path is obtained from the combination of the default session file location “/varlib/php/sessions/sess_” followed by the session ID obtained in Step 1 from the cookie named CraftSessionID. 



This request included the cmd parameter, containing the desired shell command to be executed, and the JSON data used to trigger the deserialisation bug.

![Mimo POST request to enable and use webshell](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55969291914889ad4c5_6a92a1c2a2f46752fd00a394_6a2a7f576cac9e5521dee6cf.webp)

Mimo POST request to enable and use webshell

### Post Exploitation

The base64-decoded string submitted via the webshell revealed a command designed to fetch and execute a remote shell script named 4l4md4r.sh from a server controlled by the attacker using curl, wget, or python, depending on the available tools on the system and ensures execution by piping the retrieved script directly into bash.

Regarding the use of Python, the attacker imports the urllib2 library under the alias fbi. This unusual naming choice may be an intentional reference — possibly a tongue-in-cheek nod to the American federal agency — and stands out as a distinctive coding choice. This naming convention could serve as a useful indicator for detection, especially in threat hunting or retroactive analysis of suspicious Python activity

#### Infection script

The infection script consists of a sequence of functions, each invoked in a specific order to prepare the environment and ensure successful execution of the malicious payloads:

  * d(): This function first checks whether the machine is already compromised, by scanning process names under /proc for indicators of prior infection.
  * rc(): It clears user startup configuration files (such as .bashrc and .bash_profile) as well as /etc/ld.so.preload, likely to neutralise defensive or competing persistence mechanisms.
  * unins(): Any existing instance of a known cryptominer, specifically c3pool_miner, is uninstalled. The function also terminates all active xmrig processes to eliminate interference from previous infections.
  * kp(): This step is designed to aggressively kill processes related to competing cryptomining tools, such as peer2profit, iproyal, and others. It also targets binaries running from temporary locations like /tmp, /var/tmp, or the current user’s home directory.
  * fd(): A recursive search is performed from the root filesystem (/) to locate directories that are both writable and executable. Once found, the script attempts to drop and execute the payloads within one of these locations.
  * funcGet(): The function attempts to identify a functional curl or wget binary. If necessary, it downloads a copy and creates a symlink to standardise its usage in subsequent steps.
  * get(): Using the downloading tool selected or the one retrieved by funcGet, this function downloads the actual malicious binary named 4l4md4r into the writable directory previously identified by fd() and sets the appropriate execution permissions.



Finally, the script executes the downloaded binary named 4l4md4r.

#### Mimo Loader

The main component deployed by the bash script is a large ELF of 4Mb named **4l4md4r** packed with **UPX**. Fortunately, the attacker uses the packer within its default settings, making it trivial to unpack the binary. The main unpacked payload is developed in **Golang** , the developer made no effort to conceal its intent; the malware is statically compiled and unstripped. 

When the loader starts, it initiates a first task to ensure it has elevated privileges. If it does not, it downloads the binary **su** and then it attempts to call the chmod command wrapped with the su utility. It then downloads a file named **alamdar.so**. A subsequent paragraph is dedicated to explain how this library functions.

The loader have three behaviours:

  1. It hijacks the execution flow using /etc/ld.so.preload to hide the presence of the malware process (filename:**alamdar.so**);
  2. It downloads and executes the Residential Proxy binary IPRoyal (filename: **hezb.x86_64**);
  3. It downloads and executes the XMRig miner (filename: **alamdar**).


  * **LD_Preload - alamdar.so**



To conceal the execution of the final payload, this threat employs a technique to hijack the execution flow by overloading the dynamic linker. This approach ensures that when a binary attempts to list the running processes, the payload name “**alamdar** ” does not appear in the running processes list.

  1. Attacker creates a malicious .so library that redefines functions like readdir, getpid, etc.
  2. They add the path to this library in /etc/ld.so.preload, which is a file read by the dynamic linker on process startup.
  3. When any dynamically-linked binary runs, the **linker loads the attacker's .sofirst** , hijacking execution flow.
  4. The malicious code runs in the context of all affected processes, potentially hiding files, PIDs, or logging data.



As previously mentioned, the loader writes the path to the malicious shared library in the /etc/ld.so.preload file. The malicious library, named **alamdar.so** , redefines two functions readdir its 64-bits version (readdir64). 

![Pseudo C of the retyped function readdir used to hide the malware process](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55969291914889ad4bf_6a92a1c5693fca262e1a8191_6a2a7f586cac9e5521dee6d9.webp)

Pseudo C of the retyped function readdir used to hide the malware process

  * **IPRoyal - hezb payload**



One of the two payloads deployed by the 4l4md4r loader is IPRoyal, a type of malware that registers the infected device on the IPRoyal network. The device is registered with this service in exchange for remuneration and will later be used by the IProyal customer to anonymise their internet connection, usurping a residential IP address. By covertly installing this malware on a compromised server, the attacker effectively **monetises the victim’s internet bandwidth** , redirecting the associated revenue to themselves.

The malicious payload operates very simply; it accepts three parameters: an email address, a password used to authenticate the IPRoyalPawns partner for remuneration, and a request to accept the terms of service (TOS).

![IProyal command line used by Mimo](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55969291914889ad4ce_6a92a1c02b0ef7af46bc3dca_6a2a7f576cac9e5521dee6c9.webp)

IProyal command line used by Mimo

  * **XMRig miner - alamdar payload**



XMRig is also packed using UPX, again with the default setting. The miner’s configuration is embedded directly within the payload, removing the need for external configuration files. It is set up to mine via the public mining pool MoneroOcean.

Additional parameters observed include the following:

  * Wallet: 46HmQz11t8uN84P8xgThrQXSYm434VC7hhNR8be4QrGtM1Wa4cDH2GkJ2NNXZ6Dr4bYg6phNjHKYJ1QfpZRBFYW5V6qnRJN
  * Pass: alamdar



This wallet has been documented in several threat intelligence publications, most notably by [**AhnLab**](https://asec.ahnlab.com/en/60440/), and has been consistently attributed to the **Mimo Intrusion Set**(IS).

## Intrusion set

The various artefacts identified during the investigation—including references to _Hezb_ and a _Monero wallet_ —appear to be connected to the Intrusion Set known as **Mimo** , also referred to as **Hezb**. This group has been active since at least **March 2022** , and is primarily known for exploiting software vulnerabilities to deploy the **XMRig** cryptominer.

Additionally, in 2023, [**AhnLab**](https://asec.ahnlab.com/en/60440/) reported that the IS had shifted tactics in certain campaigns, opting to deploy a ransomware developed in Go strain known as **Minus Ransomware** in place of its usual cryptomining tools. This ransomware has been identified as a **fork of the publicly available MauriCrypt project** , which was initially developed for “educational purposes”.

### Cryptomining

The cryptominer has been configured to operate under a **worker name “alamdar”** on the public **MoneroOcean mining pool** , which provides visibility into mining performance per wallet. Analysis of the wallet associated with the attacker reveals that it is being used by **three distinct workers, with “alamdar” showing the highest hashrate among them.**

The total hashrate remains relatively modest at **approximately 53.44 KH/s** , resulting in an estimated weekly yield of **0.0393 XMR** , equivalent to around **$9.45 USD** at the current exchange rate.

In comparison, a July 2022 report from [**Antiy**](https://www.antiy.cn/research/notice&report/research_report/20220705.html)’s threat intelligence team indicated a significantly higher hashrate of approximately 540 KH/s, linked to the same Mimo’s wallet. This notable decrease suggests that a large number of systems previously compromised by Mimo may have been cleaned or taken offline, leading to reduced mining capacity.

![Mimo’s Monero wallet mining statistic](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55969291914889ad4c8_6a92a1c4bd6424423eee8a10_6a2a7f576cac9e5521dee6d5.webp)

Mimo’s Monero wallet mining statistic

 _Mimo’s Monero wallet mining statistic_

The mining pool also indicates that, since the beginning of its activity, the wallet in question has received a total of **11,307174 XMR** , which corresponds to approximately **$3,114.30 USD** at the current exchange rate. Since Mimo has been active since March 2022, this suggests an average monthly revenue of around $84 USD for this particular wallet.

Such a figure is relatively modest and likely barely sufficient to cover the group’s operational costs, such as server hosting, infrastructure maintenance, or tooling expenses. 

The deployment of IPRoyal Pawns alongside XMRig is likely intended to maximise the financial return from compromised machines by exploiting multiple system resources in parallel. Through this dual setup, the attacker can generate revenue both from CPU-intensive cryptomining activities and by monetising the victim’s network connection via a residential proxy service. This strategy reflects a pragmatic approach to resource monetisation, extracting value from both computational power and bandwidth.

### Ransomware

The Bitcoin wallet documented by AhnLab and attributed to the Mimo ransomware—identified as **15Jz1fmreZx9wG93DKjTXMhuLpPpCgvEQk** —has been involved in a total of **101 transactions** since 6 May 2022 at 18:07:37. The most recent transaction was recorded on 23 August 2024 at 18:06:40.

The ransom note documented in AhnLab’s report indicates that the attacker demanded a payment of 0.01 BTC, which corresponded to just over $400 USD at the exchange rate at the time. Analysis of the incoming transactions to the associated wallet reveals that amounts typically ranged between $400 and $600, suggesting that at least some ransom payments may have been successfully collected.

Although the wallet's current balance stands at zero, a total of **0.37342974 BTC** has been received over the observed period. At the current exchange rate, this corresponds to approximately **$35,363.52 USD**. All funds received into the wallet appear to have been subsequently transferred to other addresses, indicating deliberate efforts to launder or redistribute the proceeds.

Analysis of the 47 outgoing transactions—transfers from the observed Bitcoin wallet to others—shows the involvement of three distinct wallets:

  * Wallet "1JdgXqDpmBSqMjAb3zHia8o8ppQf8pGsac", which received funds in 25 of the outbound transactions,
  * Wallet "3BhtK1j8EBvpFsMpPAiVtZL2WXgjH75Erw", involved in 10 outbound transactions,
  * wallet "1CSfam568zRscwyiYXMwhha9MDmZLo1Ewm", which appears in only two transactions, yet these were the most recent ones.



Further examination of wallet "1CSfam568zRscwyiYXMwhha9MDmZLo1Ewm" indicates that it remains active, with the last recorded transaction dated 3 May 2025. Notably, the amounts received by this wallet in 2025 have been relatively low, typically less than ten US dollars per transaction. Based on this activity pattern, TDR analysts assess with low confidence that wallet "1CSfam568zRscwyiYXMwhha9MDmZLo1Ewm" may be used for processing micro-payments, potentially linked to the IPRoyal service.

### Mimo's operator

#### Etxarny

Analysis of the exploitation attempts originating from the Turkish IP address **85.106.113[.]168** revealed an effort to invoke the web shell by issuing a simple command designed to output the string **“etxarny”** using the echo command. This action is likely indicative of a basic test, intended to confirm both the success of the vulnerability exploitation and the operational status of the deployed web shell.

![etxarny pattern in vulnerability exploitation](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55969291914889ad4c2_6a92a1c1693fca262e1a7fa4_6a2a7f576cac9e5521dee6cc.webp)

etxarny pattern in vulnerability exploitation

Further investigation into the keywords **“etxarny”** and **“4L4md4r”** led to the identification of a **TikTok account** under the username **@etxarny**. This account has published four videos to date, including:

  * a proof-of-concept (PoC) exploit for **CVE-2024-46483** developed in Go, and
  * a Python-based PoC for remote code execution (RCE) targeting **CyberPanel**.



All of these videos were posted using the hashtags **#EtxArny, #N1tr0** and **#4l4md4r** , suggesting a link.

The same account also shared a video clip broadcast initially by Al Jazeera, showing an excerpt from a speech by President Xi Jinping in which he called for a ceasefire in Gaza during the 2024 BRICS Summit held in Russia. The same TikTok account also published a video showing **former Iranian President Ebrahim Raisi** delivering an address to the Russian parliament. In addition, another video was posted which appears to have been filmed in **southern Lebanon** , although its exact context remains unclear.

The term **"Alamdar"** \- **4l4md4r** , of **Persian origin** , is also found in Turkish and Arabic usage, where it carries the meaning “standard-bearer” or “flag bearer.” It often conveys **religious or heroic connotations** , particularly within Shia traditions and historical narratives.

The **TikTok account** operated under the alias **"EtxArny"** appears to incorporate this symbolic pattern in its naming conventions, alongside the use of **"Hezb"** , which—judging by the nature of the content reposted—is likely a shorthand reference to **Hezbollah** , the Lebanese paramilitary and political organisation.

In addition to the ideological indicators, the publication of proof-of-concept (PoC) exploits targeting known vulnerabilities provides an additional link between the TikTok account and the observed attacker behaviour. These elements, taken together, reinforce the hypothesis that the TikTok account owner is the authorof the exploitation attempts observed on our honeypots and could be affiliated with the Mimo intrusion set.

The repeated use of the IP address **85.106.113[.]168** , geolocated in the **Balıkesir area** , Turkey, between 28 April and 2 May 2025, strongly suggests that it is likely associated with the attacker's personal internet connection. This recurring usage pattern may therefore indicate that **EtxArny - Mimo’s operator** is **physically located in Turkey**.

#### N1tr0

Following the analysis of video content shared by the TikTok user EtxArny, further research was conducted into the identifiers “**4l4md4r** ” and “**n1tr0** ”. A Google search combining these two terms led to several noteworthy findings.

Among them were social media profiles, including a **TikTok** account (**@n1tr0_s**) and an X profile (**@n1tr0_S**), as well as a WordPress site hosted at n1tr0[.]online (actually offline), bearing the HTML page title: _“4l4md4r | N1tr0”_. This link is also featured in the biography section of the n1tr0 TikTok account, further reinforcing the connection between this account, the domain n1tr0.online and the pattern “**4l4md4r** ”.

Of particular interest, a TikTok playlist created by the account @nitr0.s contains a single video, which appears to explain a Python PoC exploit for a CVE that was previously published by **EtxArny** , further suggesting a connection between the two profiles.

One of the IOCs associated with the Mimus ransomware, reportedly used by Mimo IS and documented by AhnLab, is windows.n1tro[.]cyou. A Mimus ransomware binary named n1tro.exe was also identified, suggesting that this operator is more directly involved in the ransomware deployment phase.

In light of these indicators, TDR analysts assess with moderate confidence that this profile may correspond to a second Mimo IS operator.

## Detection opportunites

The Go-based loader “alamdar” was executed within a TDR sandbox environment monitored by a Sekoia agent. This execution resulted in four alerts, which were automatically grouped into a single Autocase.

As detailed in the Post-Exploitation section, the infection script attempts to identify a directory with write permissions, typically selecting /tmp. It then writes the payloads to this location, assigns execution rights, and launches them from the same directory. These actions triggered the Sekoia Defend Sigma rules “**Unusual Process Executed in Temporary Directory** ” and “**File and Directory Permissions Modification** ”.

To evade detection and conceal the presence of malicious components, the alamdar loader also employs a technique that hijacks the execution flow by overloading the dynamic linker. This behaviour triggered additional Sekoia Defend Sigma rules, specifically “**Kernel Module Alteration** ” and “**Main Memory Dumping** ”.

![Sekoia Defend \(XDR\) alerts related to Mimo’s Infection chain](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a55969291914889ad4cb_6a92a1c33e6167cebbf5805b_6a2a7f576cac9e5521dee6d2.webp)

Sekoia Defend (XDR) alerts related to Mimo’s Infection chain

It is also possible to identify traces of infection through a **SOL query** , by searching for specific patterns such as **“hezb”, “alamdar” or variants like “4l4mdar”** within **command-line arguments, process names, or file names**. These indicators may point to previous or ongoing compromise attempts associated with the same intrusion set.

## Conclusion

Initially identified in early 2022, the **Mimo** intrusion set has been characterised by its consistent **exploitation of vulnerabilities** for the purpose of **cryptominer** deployment. In January 2024, a report by AhnLab highlighted the use of a ransomware strain dubbed **Minus Ransomware** , attributed to Mimo. This shift suggests a **strategic diversification** likely aimed at increasing the financial returns from compromised systems.

Ongoing investigation confirms that Mimo remains active and operational, continuing to exploit newly disclosed vulnerabilities. Notably, the short timeframe observed between the publication of **CVE-2025-32432** , the release of a corresponding proof-of-concept (PoC), and its subsequent adoption by the intrusion set, reflects a high level of responsiveness and technical agility.

Furthermore, the **simultaneous** deployment of **XMRig** alongside the **IPRoyal Pawns** malware appears to be part of a broader**profit-maximisation strategy** , enabling the threat actor to monetise both processing power and network bandwidth of infected hosts.

The use of distinctive identifiers and repeated patterns has led to the identification of two TikTok profiles that are highly likely to be linked to the Mimo IS. Both accounts appear to belong to individuals whose online activities indicate a strong interest in**Middle Eastern** affairs, with a particular focus on Lebanon and Shiite religion. One of the profiles is likely geolocated in Turkey, based on technical artifacts.While ideological elements are present, the observed behaviour and attack patterns suggest that the **actors’ primary motivation is financial** in nature, rather than political or ideological.

## IoCs

**Files Hashes**

`1aa4d88a38f5a27a60cfc6d6995f065da074ee340789ed00ddc29abc29ea671e - iproyal  
3a71680ffb4264e07da4aaca16a3f8831b9a30d444215268e82b2125a98b94aa - xmrig  
fc04f1ef05847607bce3b0ac3710c80c5ae238dcc7fd842cd15e252c18dd7a62 - alamdar.sh  
7868cb82440632cc4fd7a451a351c137a39e1495c84172a17894daf1d108ee9a - alamdar.so  
2e46816450ad1b4baa85e2a279031f37608657be93e1095238e2b6c36bbb3fd5 - go loader  
`

**Urls**

`1hxxp://15.188.246[.]198/alamdar.so  
hxxp://15.188.246[.]198/alamdar.x86_64  
hxxp://15.188.246[.]198/4l4md4r.sh  
hxxp://15.188.246[.]198/hezb.x86_64  
`

**Others**

`46HmQz11t8uN84P8xgThrQXSYm434VC7hhNR8be4QrGtM1Wa4cDH2GkJ2NNXZ6Dr4bYg6phNjHKYJ1QfpZRBFYW5V6qnRJN - Monero wallet  
4l4md4r[@]proton.me - IPRoyal mimo’s account  
`