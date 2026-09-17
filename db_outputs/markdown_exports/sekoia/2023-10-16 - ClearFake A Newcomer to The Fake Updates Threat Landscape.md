# ClearFake: A Newcomer to The "Fake Updates" Threat Landscape

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/clearfake-a-newcomer-to-the-fake-updates-threats-landscape
- **Date :** 2023-10-16

---

ClearFake is a new malicious JavaScript framework deployed on compromised websites to deliver further malware using the drive-by download technique. This blogpost aims at presenting a technical analysis of the ClearFake installation flow, the malware delivered by ClearFake, the C2 infrastructure and tracking opportunities.

## Introduction

On 26 August 2023, cybersecurity researcher Randy McEoin published1 an analysis of a new malicious JavaScript framework deployed on compromised websites to deliver further malware using the drive-by download technique. The newly discovered malware was named ClearFake due to the clear text JavaScript injected into the compromised website, which was not obfuscated in the early version as is usually the case for Javascript malware.

ClearFake is another “fake updates” threat leveraging social engineering to trick the user into running a fake web browser update, as for SocGholish and FakeSG malware. By linking the “fake updates” lure to the watering hole technique, ClearFake operators target a wide range of users and conduct effective, scalable malware distribution campaigns.

From our telemetry and customers’ feedback, we observed an increasing number of communications to ClearFake infrastructure at the end of September 2023. At the same time, we identified several hundred websites injected by ClearFake.

Sekoia.io’s Threat & Detection Research (TDR) team investigated this emerging threat and shares in this blog post our analysis of ClearFake, the malware delivered, as well as tracking opportunities.

## ClearFake installation flow

Here is an overview of the infection chains’ stages observed distributing commodity malware via ClearFake:

![ClearFake installation flow, as of 30 September 2023](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaaa6029806294b5e00f266_ClearFake%20installation%20flow%2C%20as%20of%2030%20September%202023.webp)

ClearFake installation flow, as of 30 September 2023

### Injected JavaScript code

ClearFake operators compromised WordPress sites, acting as water holes, to inject malicious JavaScript code into the HTML page.

In the early ClearFake version, the injected code was base64-encoded JavaScript from a _data-url_ attribute, downloading another JavaScript payload from an attacker-owned domain (_brewasigfi1978.workers[.]dev_) and executing it using the _eval()_ function, _e.g._ :

![Injected JavaScript code by ClearFake operators. Source: Sekoia.io](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e09c_6a92a3643e6167cebbf673c5_6a2a7c30bf2797708e089f63.webp)

Injected JavaScript code by ClearFake operators. Source: Sekoia.io

Since 28 September 2023, **to download the next stage, ClearFake have used a different technique, relying on smart contract from the Binance Smart Chain**. The _result_ value of the requested smart contract contains an obfuscated JavaScript, encoded in base64 and converted in hexadecimal.

Annex 1 includes the obfuscated and deobfuscated injected JavaScript used prior to and after 28 September 2023, as well as an example of the response of the smart contract.

### Next stage JavaScript payloads

The first payload is an obfuscated JavaScript aiming at downloading and executing the second payload. Here is an example of the deobfuscated JavaScript using deobfuscate.io:

![Example of JavaScript code injected by ClearFake operators. Source: Sekoia.io](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e0ac_6a92a363e17eff730b65861c_6a2a7c30bf2797708e089f5f.webp)

Example of JavaScript code injected by ClearFake operators. Source: Sekoia.io

The first obfuscated payload is available in Annex 2.

The second payload is a clear-text JavaScript **creating an _iframe_ element to host the fake update interface** and to cover the entire document object model (DOM) of the web documents, setting:

  * the _iframe_ width and height to 100%;
  * the _z-index_ , an attribute specifying the stack order of the element, to 99999999999.



It then downloads the fake update interface. Here is an example of the second payload:

![Example of JavaScript code injected by ClearFake operators. Source: Sekoia.io](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e0af_6a92a36ae17eff730b6589a1_6a2a7c30bf2797708e089f83.webp)

Example of JavaScript code injected by ClearFake operators. Source: Sekoia.io

The third payload is an HTML page serving as a fake update interface and downloading the fake update content for the appropriate web browser. An example of the third payload is provided in Annex 2.

The HTML page downloads the final fake update page (HTML) from the URL path stored in the HTML element _href_ and modified using the decoded value of the Javascript variable _blank_ , _e.g._ “ _/lander/firefox_1695214415/_index.php_ ”.

Here is an example of the source code of the fake update page on urlscan: <https://urlscan.io/responses/a70b72efd8cd83f2b79cc9b9823112930e8ffa49edeb6bb5d2b1bbcabccefafb/>

### Fake update web page

The fake update page displays a realistic copy of the web browser download page for Chrome, Edge and Firefox, as shown in the following figure.

![ClearFake fake update pages for Chrome, Edge and Firefox web browsers. 
Source: Sekoia.io](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e09f_6a92a3628d1115926b20553b_6a2a7c2fbf2797708e089eff.webp)

ClearFake fake update pages for Chrome, Edge and Firefox web browsers.   
Source: Sekoia.io  


It also contains JavaScript code aiming at **fingerprinting the victims’ web browser and initiating the download module**. Here is an overview of the executing capabilities of the fake update page:

  * Import the jQuery library used by the following Javascript;
  * Define the infamous module named _FingerprintJS_ 2 aiming at generating unique fingerprints for browsers based on various attributes and features. The module contains mathematical, fingerprint generation, utility, feature detection functions, as well as audio and font fingerprinting;
  * Set the JavaScript _onclick_ event for the download button;
  * Define functions related to handling cookies and extracting values from the URL parameters;
  * Generate the visitor fingerprint and exfiltrate it to “ _hxxps://stats-best[.]site/fp.php_ ”;
  * Generate the download URL using “ __lp_ ”, “ _FPID_ ”, “ _DownloadMouse_ ”, “ _D_ ” and _“_token_ ” parameters when the _onclick_ event is executed.



## Malware delivered by ClearFake

On 30 September 2023, Sekoia.io analysts ran the infection chain until retrieving the final payload downloaded by the victim.

### Suspicious filename

For Microsoft Edge’s visitors, ClearFake delivered a malicious Windows Application Packaging Project (APPX file) from Dropbox.

The payload’s name “ _MlсrоsоftЕdgеSеtup.appx_ ” is a masquerading of the legitimate Microsoft Edge installer and uses UTF-8 Cyrillic character for the characters “c”, “e”, “o” and “E”. Escaping unicode characters returns the following result:

`Ml\u0441r\u043Es\u043Eft\u0415dg\u0435S\u0435tup.appx`

**ASCII**| **Unicode**| **Name**  
---|---|---  
 _с_|  \u0441| Cyrillic Small Letter Es  
e| \u0435| Cyrillic Small Letter Ie  
 _о_|  \u043E| Cyrillic Small Letter O  
 _Е_|  \u0415| Cyrillic Capital Letter Ie  
  
Cyrillic characters are invisible to the user. Sekoia.io assess with high confidence that the **use of lookalike characters aims at avoiding static detection patterns** based on the filename, without raising the potential victim’s suspicions.

It is interesting to note that **SocGholish operators successfully leveraged this technique in 2022** , as identified by Red Canary3. As this obfuscation method is not widely used, it is legitimate to ask ourselves if the SocGholish operators are also behind the new ClearFake malware.

### APPX file

Windows Apps are ZIP archive files that store executable files and other additional ones including XML (_AppxManifest.xml_ and _AppxBlockMap.xml_), P7X (_AppxSignature.p7x_), as well as other optional files and repositories.

The APPX file delivered by ClearFake (MD5: _a7900cdbb2912d76aa6329c5c41d8609_) is signed by “ _STECH CONSULTANCY LIMITED_ ” and contains in particular the following executables:

  * \MlсrоsоftЕdgеSеtup\AI_STUBS\AiStubX64.exe (MD5: _e89f448e8f41a590c51d34948bdc9c1e)_
  * \MlсrоsоftЕdgеSеtup\VFS\AppData\\.exe (MD5: _d113b3debc7e0a2da4369dd8d1dbad53_)



Once executed, the Windows App reads the APPX manifest’s entry point containing the _AiStubX64_ executable and then executes it. The _AiStubX64.exe_ process **copies the _KSPSService_ executable located in the Virtual File System (VFS) and then launches it**. The payload (_KSPSService.exe_) deployed by the APPX file **turned out to be a sample of HijackLoader**. More technical information on this execution flow can be found in the Microsoft documentation4 and FINSIN’s analysis5.

The APPX file also contains a legitimate Microsoft Edge installer (_MicrosoftEdgeUpdateSetup.exe_ MD5: _58d8d75b0ca5e316862ed81cdb2d0c67_) and a PowerShell script (_chrome.ps1_ MD5: _bfe16fc5d100757bd9dec4ef1aa42913_), downloading a legitimate Edge installer from transfer[.]sh and executing it. Both codes are executed when the user runs the Windows App file. Sekoia.io analysts believe that installing the legitimate web browser alongside the malware once again avoids any suspicion from the victim.

As mentioned by SentinelOne6, APPX files are regularly used in malware campaigns to deploy the payload on the infected host, including BazarBackdoor, Emotet or Magniber ransomware. **Although this technique is not new, Sekoia.io believes its use improves the rate of successful compromise** by reducing the detection of the malicious payload’s execution.

### Overview of HijackLoader

First observed in the wild in July 2023 by Zscaler ThreatLabz7, **HijackLoader is a modular loader downloading and executing an obfuscated payload**. It implements several evasion techniques, including code injection, use of syscalls, Windows API hashing and Heaven’s gate. In recent months, HijackLoader delivered numerous commodity malware, including Danabot, Lumma, Raccoon, Redline, Remcos, SystemBC and Vidar.

Once executed, the HijackLoader sample deployed through the APPX file downloads its obfuscated payload from the adversary infrastructure “ _hxxps://server2-slabx.ocmtancmi2c5t[.]live/osmesis/1829973585.png_ ”. The payload loaded by HijackLoader is a Raccoon sample communicating with its Command & Control (C2) server “ _128.140.101[.]125_ ”.

In August 2023, Rapid7 observed8 that the new **IDAT Loader malware was delivered by ClearFake**. Based on the code similarities between IDAT Loader and HijackLoader, and given the overlap in the C2 infrastructures, **Sekoia.io assess with high confidence that the same threat group operates both loaders**.

## ClearFake C2 infrastructure and tracking opportunities

### ClearFake C2 communications

ClearFake stages use hardcoded URLs to download the next stage payloads from its C2 infrastructure. URL patterns have not changed since the threat first appeared in July 2023.

The URLs observed on 30 September 2023 are:

  * hxxps://ojhggnfbcy62[.]com/vvmd54/
  * hxxps://ojhggnfbcy62[.]com/ZgbN19Mx
  * hxxps://ojhggnfbcy62[.]com/lander/firefox_1695214415/_index.php



Basic heuristics based on the URL pattern stem from the ClearFake C2 communications. Sekoia.io used similar queries on urlscan:

  * [page.url:"/vvmd54/"](https://urlscan.io/search/#page.url%3A%22%2Fvvmd54%2F%22)
  * [page.url:"/ZgbN19Mx"](https://urlscan.io/search/#page.url%3A%22%2FZgbN19Mx%22)
  * [page.url.keyword:/.*\/lander\/(chrome|firefox|edge).*\/_index\\.php/](https://urlscan.io/search/#page.url.keyword%3A%2F.*%5C%2Flander%5C%2F\(chrome%7Cfirefox%7Cedge\).*%5C%2F_index%5C.php%2F)



Using urlscan and other URL scanning search engines, we retrieved 39 domain names:

921hapudyqwdvy[.]com  
98ygdjhdvuhj[.]com  
adqdqqewqewplzoqmzq[.]site  
bgobgogimrihehmxerreg[.]site  
boiibzqmk12j[.]com  
bookchrono8273[.]com  
borbrbmrtxtrbxrq[.]site  
bpjoieohzmhegwegmmuew[.]online  
cczqyvuy812jdy[.]com  
ewkekezmwzfevwvwvvmmmmmmwfwf[.]site  
gkrokbmrkmrxtmxrxr[.]space  
indogervo22tevra[.]com  
indogevro22tevra[.]com  
ioiubby73b1n[.]com  
kjniuby621edoo[.]com  
komomjinndqndqwf[.]store  
lminoeubybyvq[.]com  
nbvyrxry216vy[.]com  
ngvcfrttgyu512vgv[.]net  
nmbvcxzasedrt[.]com  
oekofkkfkoeefkefbnhgtrq[.]space  
oiouhvtybh291[.]com  
oiqwbuwbwqznjqsdfsfqhf[.]site  
oiuugyfytvgb22h[.]com| oiuytyfvq621mb[.]org  
ojhggnfbcy62[.]com  
omdowqind[.]site  
ooinonqnbdqnjdnqwqkdn[.]space  
opkfijuifbuyynyny[.]com  
opmowmokmwczmwecmef[.]site  
owkdzodqzodqjefjnnejenefe[.]site  
pklkknj89bygvczvi[.]com  
poqwjoemqzmemzgqegzqzf[.]online  
pwwqkppwqkezqer[.]site  
reedx51mut[.]com  
sioaiuhsdguywqgyuhiqw[.]org  
sioaiuhsdguywqgyuhuiqw[.]org  
ug62r67uiijo2[.]com  
vcrwtttywuuidqioppn1[.]com  
vvooowkdqddcqcqcdqggggl[.]site  
weomfewnfnu[.]site  
wffewiuofegwumzowefmgwezfzew[.]site  
wnimodmoiejn[.]site  
wsexdrcftgyy191[.]com  
ytntf5hvtn2vgcxxq[.]com  
zasexdrc13ftvg[.]com  
ziucsugcbfyfbyccbasy[.]com  
znqjdnqzdqzfqmfqmkfq[.]site  
---|---  
  
### Pivot on IP addresses

By pivoting on the IP addresses resolving the previous attacker-owned domains, we listed the following C2 servers that we assess with high confidence as being exclusively associated with the ClearFake infrastructure.

109.248.206[.]49  
109.248.206[.]83  
109.248.206[.]101  
109.248.206[.]118  
109.248.206[.]196  
135.181.211[.]230  
---  
  
5 of them belong to the autonomous system (AS) “YACOLO-AS” (AS203493) located in Russia, and the last one belongs to the HETZNER AS (AS24940), favoured by numerous threat actors.

For all C2 servers, the common name (CN) of the TLS certificates exposed on port 443 is “ _921hapudyqwdvy.com_ ”, allowing us to unveil the ClearFake infrastructure using scanning search engines, such as Shodan or Censys. Sekoia.io used a similar query on Shodan to identify and proactively track the ClearFake C2 infrastructure:

[ssl:"921hapudyqwdvy.com"](https://beta.shodan.io/search?query=ssl%3A%22921hapudyqwdvy.com%22)

**ClearFake operators run the Keitaro traffic distribution system (TDS)** on C2 servers to protect their infrastructure that hosts malicious content and to select the targeted traffic.

TDR believes that **ClearFake operators are likely to improve the stealth of malware C2 communication in the near future**. They could also harden their C2 server configuration, to prevent their infrastructure from being so easily illuminated.

## Conclusion

First seen in the wild in July 2023, **ClearFake is another “fake updates” threat that quickly became widespread** due to the effective lure targeting a wide audience, as well as the watering hole technique used to distribute the malware via numerous compromised websites.

Given the **ongoing development and the use of cutting-edge techniques** , such as the blockchain technology to store malicious payloads, this **threat must be closely monitored by organisations** , as the malware delivered by ClearFake can be used to gain access to the victim’s network.

The **tactics, techniques and procedures leveraged by the ClearFake operators overlap with those of SocGholish ones** (tracked as TA569), in particular the use of watering holes, “fake updates'' lures, Keitaro TDS, Dropbox file hosting service and the masquerading of filename with cyrillic characters. Considering this, **Sekoia.io further assess ClearFake and SocGholish are possibly operated by the same threat group. Gathering additional evidence may help to confirm or refute this hypothesis**.

To provide our customers with actionable intelligence, we will continue to monitor the evolution of ClearFake and other malware it delivers.

## ClearFake IoCs & Technical Details

### IoCs

The list of IoCs is available on [Sekoia.io github repository](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/clearfake/clearfake_iocs_20231016.csv).

### ClearFake C2 domains

921hapudyqwdvy[.]com  
98ygdjhdvuhj[.]com  
adqdqqewqewplzoqmzq[.]site  
bgobgogimrihehmxerreg[.]site  
boiibzqmk12j[.]com  
bookchrono8273[.]com  
borbrbmrtxtrbxrq[.]site  
bpjoieohzmhegwegmmuew[.]online  
brewasigfi1978[.]workers[.]dev  
cczqyvuy812jdy[.]com  
ewkekezmwzfevwvwvvmmmmmmwfwf[.]site  
gkrokbmrkmrxtmxrxr[.]space  
indogervo22tevra[.]com  
indogevro22tevra[.]com  
ioiubby73b1n[.]com  
kjniuby621edoo[.]com  
komomjinndqndqwf[.]store  
lminoeubybyvq[.]com  
nbvyrxry216vy[.]com  
ngvcfrttgyu512vgv[.]net  
nmbvcxzasedrt[.]com  
oekofkkfkoeefkefbnhgtrq[.]space  
oiouhvtybh291[.]com  
oiqwbuwbwqznjqsdfsfqhf[.]site  
oiuugyfytvgb22h[.]com| oiuytyfvq621mb[.]org  
ojhggnfbcy62[.]com  
omdowqind[.]site  
ooinonqnbdqnjdnqwqkdn[.]space  
opkfijuifbuyynyny[.]com  
opmowmokmwczmwecmef[.]site  
owkdzodqzodqjefjnnejenefe[.]site  
pklkknj89bygvczvi[.]com  
poqwjoemqzmemzgqegzqzf[.]online  
pwwqkppwqkezqer[.]site  
reedx51mut[.]com  
sioaiuhsdguywqgyuhiqw[.]org  
sioaiuhsdguywqgyuhuiqw[.]org  
stats-best[.]site  
ug62r67uiijo2[.]com  
vcrwtttywuuidqioppn1[.]com  
vvooowkdqddcqcqcdqggggl[.]site  
weomfewnfnu[.]site  
wffewiuofegwumzowefmgwezfzew[.]site  
wnimodmoiejn[.]site  
wsexdrcftgyy191[.]com  
ytntf5hvtn2vgcxxq[.]com  
zasexdrc13ftvg[.]com  
ziucsugcbfyfbyccbasy[.]com  
znqjdnqzdqzfqmfqmkfq[.]site  
---|---  
  
### ClearFake IP addresses

109.248.206[.]49  
109.248.206[.]83  
109.248.206[.]101  
109.248.206[.]118  
109.248.206[.]196  
135.181.211[.]230  
---  
  
### ClearFake infection chain

IoC| Description  
---|---  
hxxps://hello-world-broken-dust-1f1c.brewasigfi1978.workers[.]dev/| Download URL of the first JavaScript payload  
hxxps://ojhggnfbcy62[.]com/vvmd54/| Download URL of the second JavaScript payload  
hxxps://ojhggnfbcy62[.]com/ZgbN19Mx| Download URL of the first HTML payload  
hxxps://ojhggnfbcy62[.]com/lander/firefox_1695214415/index.php| Download URL of the second HTML payload  
hxxps://stats-best[.]site/fp.php| C2 URL for the fingerprinting data  
hxxp://ojhggnfbcy62[.]com/?_lp=1&_token=uuid_1ubo22l1dqqlm_1ubo22l1dqqlm6518291d817043.55797095| Redirect URL to the HijackLoader payload (APPX)  
hxxps://www.dropbox[.]com/e/scl/fi/6gtsp3qjf54lsec0piwvq/Ml-r-s-ft-dg-S-tup.appx?rlkey=hdm3apoi4n31v2rxruiosvtaa&dl=1| Download URL of the HijackLoader payload (APPX)  
b583d86c4abc6d6ca57bde802b7e9d8143a249aed6a560a4626e79ae13f6209d| HijackLoader payload (APPX)  
d60d4da2cfe120138a3fde66694b40ae2710cfc2af33cb7810b3a0e9b1663a4f| HijackLoader paylaod (EXE)  
hxxps://server2-slabx.ocmtancmi2c5t[.]live/osmesis/1829973585.png| HijackLoader hosting payload URL  
ocmtancmi2c5t[.]live| HijackLoader hosting payload domain  
128.140.101[.]125| Raccoon C2 server  
  
## MITRE ATT&CK TTPs

Tactic| Technique  
---|---  
Resource Development| T1584 – Compromise Infrastructure  
Execution| T1059.007 – Command and Scripting Interpreter: JavaScript  
Initial Access| T1189 – Drive-by Compromise  
Defense Evasion| T1027 – Obfuscated Files or Information  
Defense Evasion| T1132.001 – Data Encoding: Standard Encoding  
Defense Evasion| T1036 – Masquerading  
Defense Evasion| T1140 – Deobfuscate/Decode Files or Information  
Command and Control| T1041 – Exfiltration Over C2 Channel  
Command and Control| T1071.001 – Application Layer Protocol: Web Protocols  
Command and Control| T1105 – Ingress Tool Transfer  
  
## Annexes

The ClearFake scripts are available on [Sekoia.io github repository](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/clearfake/clearfake_malicious_script_content.md).

### Annex 1 - Injected Javascript codes

Injected JavaScript used before 28 September 2023:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e0a5_6a92a3654b4041c69342a936_6a2a7c30bf2797708e089f66.webp)

The script decodes to:

![Injected JavaScript code by ClearFake operators](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e099_6a92a367e9a71d42284020f9_6a2a7c30bf2797708e089f6c.webp)

Injected JavaScript code by ClearFake operators

Injected JavaScript used since 28 September 2023:

![Injected JavaScript code by ClearFake operators](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaaa66eb43a8714c003c331_Injected%20JavaScript%20code%20by%20ClearFake%20operators.webp)

Injected JavaScript code by ClearFake operators

The script decodes to:

![Injected JavaScript code by ClearFake operators](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaaa6f24db7f1f0e032888e_Injected%20JavaScript%20code%20by%20ClearFake%20operators.webp)

Injected JavaScript code by ClearFake operators

Response of the Binance Smart Chain:

![Injected JavaScript code by ClearFake operators](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e0a2_6a92a3684b4041c69342a9c8_6a2a7c30bf2797708e089f6f.webp)

Injected JavaScript code by ClearFake operators

### Annex 2 - Next stage payloads

First next stage payload downloaded by the injected JavaScript from the Binance Smart Chain:

![Injected JavaScript code by ClearFake operators](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaaa54c81c23739c0e6b555_Injected%20JavaScript%20code%20by%20ClearFake%20operators.webp)

Injected JavaScript code by ClearFake operators

The script decodes to:

![Injected JavaScript code by ClearFake operators](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6033e6167cebbf7e0b2_6a92a3663e6167cebbf67608_6a2a7c30bf2797708e089f69.webp)

Injected JavaScript code by ClearFake operators

Third next stage payload serving as a fake update interface and downloading the fake update content:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6aaaa7484db7f1f0e032e6d4_Injected%20JavaScript%20code%20by%20ClearFake%20operators.webp)

Injected JavaScript code by ClearFake operator