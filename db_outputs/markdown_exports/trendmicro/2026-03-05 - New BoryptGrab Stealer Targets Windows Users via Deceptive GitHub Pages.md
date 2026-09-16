# New BoryptGrab Stealer Targets Windows Users via Deceptive GitHub Pages

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/c/boryptgrab-stealer-targets-users-via-deceptive-github-pages.html
- **Date :** 2026-03-05

---

Malware

# New BoryptGrab Stealer Targets Windows Users via Deceptive GitHub Pages

The BoryptGrab campaign uses fake SEO‑optimized GitHub repositories and deceptive download pages to distribute a data‑stealing malware family that delivers multiple payloads, including a reverse SSH backdoor, to Windows users.

By: Mingyue Shirley Yang 2026/03/05 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key Takeaways

  * BoryptGrab is a newly identified stealer that harvests browser data, cryptocurrency wallet information, and system information. It is also capable of capturing screenshots, collecting common files, and extracting Telegram information, Discord tokens, and passwords.
  * The malware is distributed through a large number of public Github repositories that purport to offer software tools for free, using SEO keywords to attract victims. The infection chain is initiated when ZIP file is downloaded from a fake GitHub download page.
  * Malware code from different stages of the attack contains Russian-language comments and/or log messages. IP addresses associated with the campaign are also located in Russia, suggesting a possible origin for the attacker. Different builds of the malware have also been observed in the campaign.
  * TunnesshClient is a new backdoor delivered during the attack chain. It is a PyInstaller executable that establishes a reverse SSH tunnel to communicate with the attacker and acts as a SOCKS5 proxy. This campaign can also deliver variants of the existing Vidar stealer with code obfuscation.



# Introduction

We recently found the existence of a new stealer binary that collects browser and cryptocurrency wallet data, system information, and common files, among others. We designated this new stealer BoryptGrab. Certain variants of the stealer can download a PyInstaller backdoor, which we refer to as TunnesshClient. TunnesshClient establishes a reverse Secure Shell (SSH) tunnel to enable comunication with the attacker.

By tracing the infection chain, we were able to observe several ZIP archive files in the wild (all with similar naming conventions) that masquerade as common software tools (including gaming cheat hacks). As the “ _github-io_ ” patterns in some ZIP file names suggest, searching for the software tool patterns leads to over a hundred public Github repositories delivering malware. The earliest ZIP file we identified dates to late 2025, while the initial commit of the earliest GitHub repository account was made in April 2025.

The following list is a sample of ZIP files without “github-io” in their filename:  


  * valorant-perfomance-boost-fps-booster_5.4.9.zip
  * voicemod-pro-download-tool_8.2.1 (1).zip
  * wondershare-info-feel_8.4.3.zip
  * sk1nchangerforcs24pc_5.8.0.zip
  * cod-black-ops-6-aimbot-with-esp-tool_4.2.4.zip
  * abi-free-esp-tool-download_9.0.0.zip
  * arenabreakoutcheat_8.6.2.zip
  * git-deployer-app_7.7.2.zip
  * valorant-skin-tool_4.1.3.zip
  * filmora-watermark-remover_8.6.7.zip
  * sk1nchangerforcs24pc_2.9.5.zip
  * r6siege-free-esp-tool_1.8.9.zip



Meanwhile, the following are examples of ZIP files with “github-io” in their filename:

  * vmware-download-github-io-4.83.4.zip
  * passathook-cs2-github-io-1.96.4.zip
  * meta-skins-github-io-6.98.9.zip
  * cs2-skin-changer-premium-github-io-1.88.9.zip
  * passathook-cs2-github-io-2.56.2.zip



In the following sections, we will provide detailed analysis for the delivered BoryptGrab stealer, the TunnesshClient backdoor, and other malware observed in the campaign. We will also include in-depth analysis of the attack chains and delivery routes of the malware. The Russian comments, log messages, and IP addresses found during different stages of the attack chain indicates potential a Russian background for the threat actor.

# Attack diagram

[ ![Figure 1. Attack chain for the BoryptGrab campaign](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig1.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig1.png)

Figure 1. Attack chain for the BoryptGrab campaign

# Initial distribution

The malware was initially distributed through public Github repositories offering free, seemingly legitimate software tools. The README files for some of these repositories contain SEO keywords designed to increase their ranking for results returned by search engines. An example is a repository is located at _hxxps://github[.]com/Voicemod-Pro-Download-Tool_ , which delivers a fake Voicemod Pro tool. The Google search rankings for this repository was just below the legitimate result.****

[ ![Figure 2. README page for the malicious Voicemod Pro Github repository](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig2.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig2.png)

Figure 2. README page for the malicious Voicemod Pro Github repository

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig2.png)

The README of the fake Voicemod Pro Github repository contains the download link to the _hxxps://voicemod-pro-download-tool.github[.]io/.github/_ page. The source code for this download page is located at _hxxps://github[.]com/Voicemod-Pro-Download-Tool/.github_ , where it masquerades as a legitimate _.github_ directory.

[ ![Figure 3. Code for the fake download tool in the “.github” repository](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig3.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig3.png)

Figure 3. Code for the fake download tool in the “.github” repository

The _index.htm_ web page contains Russian comments and redirects to the _home.html_ page. The _home.html_ page fetches and decodes a base64-encoded URL from a link hardcoded in its source code (i.e. _hxxps://kiamatka[.]com/kaiok.kakman_ in the current sample). It then redirects to the decoded URL.

[ ![Figure 4. Fetch and base64-decode a URL used for redirection in home.html](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig4.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig4.png)

Figure 4. Fetch and base64-decode a URL used for redirection in home.html

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig4.png)

Finally, the intermediate URL redirects to the _hxxps://best-tinted[.]com/github-download.html_ web page that generates a ZIP file to deliver the malware.

[ ![Figure 5. Fake Github download page that generates the malicious ZIP file](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig5.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig5.png)

Figure 5. Fake Github download page that generates the malicious ZIP file

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig5.png)

Although the hardcoded links in the source code and the fetched intermediate URLs vary across the GitHub repositories we identified, similar Russian-language comments and URL-fetching logic were also present in other GitHub repositories we found for this campaign. Many of these repositories also fake different tools , which lead to the same web pages that generate malicious ZIP files. The _index.html_ files in some GitHub variants (e.g. _hxxps://github[.]com/PassFab-4WinKey-Windows-Password-Reset_) send tracking information to the attacker.

Commit history for a few GitHub repositories (such as _hxxps://github[.]com/Yim-Mod-Menu/.github_) show the deletion of a _script.js_ file. The deleted file fetches a URL from an intermediate link and then redirects to the fetched URL.

In other GitHub repositories, _scripts.js_ files are used to fetch, AES-decrypt, and redirect to a URL (such as _hxxps://github[.]com/Arena-Breakout-Infinite-ESP/.github_). The _scripts.js_ files use Base64-encoded links to fetch the encrypted URLs.

There were also several GitHub repository variants (e.g. _hxxps://github[.]com/Graphic-Editor-Krita/.github_) with recent commits that added Python scripts to simulate the download process.

A list of GitHub repositories we discovered for this campaign is included in the IoC section.

# Download route 1: DLL side-Loading and encrypted launcher payload

The distributed ZIP file variants can contain an executable that side-loads a _libcurl.dll_ file (SHA256: fa767391b99865f8533efc1fe6dfa6175215718679fb00ca85fc13c3bd4ae4b7).

The _libcurl.dll_ file (SHA256: fa767391b99865f8533efc1fe6dfa6175215718679fb00ca85fc13c3bd4ae4b7) loads a payload (SHA256: d295720bc0c1111ce1c3d8b1bc1b36ba840f103b3ca7e95a5a8bf03e2cc44fe5) from its resource section. It then decrypts a launcher payload from its resource section using XOR operations and the AES algorithm in CBC mode.

[ ![Figure 6. The launcher payload is loaded from its resource section by libc.dll ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig6.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig6.png)

Figure 6. The launcher payload is loaded from its resource section by libc.dll 

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig6.png)

[ ![Figure 7. The launcher payload is decrypted by libc.dll](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig7.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig7.png)

Figure 7. The launcher payload is decrypted by libc.dll

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig7.png)

The _libcurl.dll_ file executes the _EntryWrapper_ export function from the decrypted launcher payload.

The decrypted launcher payload, which uses XOR-decryption to obfuscate the URLs for its download targets, downloads the BoryptGrab stealer (:5466/api/chromelevator).

Some launcher payload variants contain build names (with some differing from each other) . The launcher payload passes the build name as the “-b” argument when executing the BoryptGrab stealer it downloads. As an example, the build name shown in the following figure is “ _Shrek_ ”.

[ ![Figure 8. The launcher payload sends the build name argument to the downloaded BoryptGrab stealer](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig8.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig8.png)

Figure 8. The launcher payload sends the build name argument to the downloaded BoryptGrab stealer

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig8.png)

The launcher variants can send requests with a hardcoded build name to download other files (_:5466/api/custom_exe?build={BUILD_NAME}_). These files are variants of the Vidar stealer (as discussed in later sections).

[ ![Figure 9. Traffic from launcher to download Vidar stealer](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig9.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig9.png)

Figure 9. Traffic from launcher to download Vidar stealer

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig9.png)

Several build names have been observed in the wild for the “ _/api/custom_exe?build={BUILD_NAME}_ ”requests to download Vidar variants:

  * CryptoByte
  * Kassay
  * Leon
  * NeoWho
  * Shrek
  * Sonic
  * Yaropolk
  * Yarostnick



The launcher payload also downloads a Pyinstaller executable from the attacker’s server (:5466/api/client) which we named TunnesshClient. The launcher payload schedules tasks that use .xml files at _%TEMP%\client_task_system.xml_ and _%TEMP%\client_task_user.xml_ to execute the downloaded TunnesshClient.

[ ![Figure 10. The launcher creates a scheduled task for the downloaded TunnesshClient](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig10.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig10.png)

Figure 10. The launcher creates a scheduled task for the downloaded TunnesshClient

The launcher payload can also download an executable **—** a binary written in Golang (which we dubbed as HeaconLoad) from “ _:5466/api/lodik_ ”. It further downloads and runs another executable.

[ ![Figure 11. Traffic from the launcher to download HeaconLoad](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig11.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig11.png)

Figure 11. Traffic from the launcher to download HeaconLoad

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig11.png)

# Download route 2: VBS Script to download launcher EXE

Some ZIP file variants can contain a VBS downloader that further delivers other malware. We used one VBS downloader script containing unused variables as junk code for obfuscation (SHA256: 1bd605ef84b6767df74bd6290f1468eed5a88264df23fcf70b6a75d5bdcf7d76) for demonstration.

The VBS script uses integer arrays to represent strings. It contains a function "A" that converts integer arrays to their corresponding strings. The script also includes a function named _EnsureElevatedPrivileges_ for privilege escalation.

The strings converted from integer arrays are encoded PowerShell payloads. The final decoded command in the VBS script downloads and Base64-decodes a binary executable from _hxxps://botshield[.]vu/kFcjld_.

[ ![Figure 12. VBS downloader downloads and executes file from attacker](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig12.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig12.png)

Figure 12. VBS downloader downloads and executes file from attacker

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig12.png)

The final deobfuscated commands in the VBS script can also set Microsoft Defender exclusions to prevent the _C:\_ drive from performing anti-virus scanning.

[ ![Figure 13. The VBS downloader configures exclusion path for Windows Defender](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig13.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig13.png)

Figure 13. The VBS downloader configures exclusion path for Windows Defender

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig13.png)

The file downloaded and decoded by the VBS script is a C/C++ launcher binary that further downloads the BoryptGrab stealer by sending an HTTP request (_/api/{BUILD_NAME}_) with a build name. The following image shows the HTTP request from a C/C++ launcher variant (SHA256:15de71073f44c657c23f5f97caa11f1b12e654d4d17684bfc628cc1e5b6bcdd5) with the build name “CryptoByte”. Different build names have also been observed for different launcher variants. These build names correspond to the build name values hardcoded in the BoryptGrab samples as described in later sections.

[ ![Figure 14. Traffic from the launcher binary to download the BoryptGrab stealer](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig14.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig14.png)

Figure 14. Traffic from the launcher binary to download the BoryptGrab stealer

In this attack chain, variants of the downloaded BoryptGrab (SHA256: 4e90d386c1c7d3d1fd4176975795a2f432d95685690778e09313b4a1dbab9997) can download TunnesshClient themselves rather than letting the launcher binary download it.

# Other download routes

In some variants, a .NET executable (SHA256: 4264a88035aa0b63e9aef96daa78a58114d60a344ea10168a8ef5ef36bf8edbd) is used to decode and run a Base64-encoded VBS downloader (SHA256: 433a13cc70396f80dc29d1150c050339d78964fdc91bcdc3f40c67a77add1476). In the sample we analyzed, the VBS downloader downloads and executes a binary executable from “ __hxxps://botshield[.]vu/KKRkm9__ ”.

[ ![Figure 15. The .NET binary embeds a Base64-encoded VBS downloader](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig15.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig15.png)

Figure 15. The .NET binary embeds a Base64-encoded VBS downloader

Variants of the launcher (SHA256: 7f2315b89fb9a47e1516def136844d617bfcdce19000a1b0436706692dbe166c) can download files from “ _:5466/api/app_ ” or “ _:5466/api/app.zip_ ” depending on its privilege. Meanwhile, another launcher variant (SHA256: 449f528f5ceae8c3f8336d0d8e3e3ec9031d1ad67c31ee7311b67e01d5fdf225) can also download the payload from “ _:5466/api/payload_ ”. A third variant we analyzed (SHA256: c40b9913e79c5dd09751b1afb03aaa98658bab61bacf27a299abd84fd44fe707) can also download TunnesshClient at “ _:5466/api/client2_ ”.

Meanwhile, some ZIP file variants can directly contain the HeaconLoad downloader to deliver malware.

# HeaconLoad: Golang downloader

The HeaconLoad sample (SHA256: 2abe0ef88ba92db79d82cde4c0ed1f382bb347517a54ea82084c841d0f955518) achieves persistence by adding a registry entry under the _Run_ key and creating a scheduled task.

[ ![Figure 16. HeaconLoad achieves persistence](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig16.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig16.png)

Figure 16. HeaconLoad achieves persistence

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig16.png)

HeaconLoad sends beacon messages to the attacker via HTTP POST requests at “ _:8088/healthcheck_ ”. Each beacon message contains collected system information along with a build tag value hardcoded in the HeaconLoad sample.

[ ![Figure 17. HeaconLoad sends a beacon message with build tag “yaropolk” to check for status of the bundle to download](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig17.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig17.png)

Figure 17. HeaconLoad sends a beacon message with build tag “yaropolk” to check for status of the bundle to download

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig17.png)

The following are different hardcoded build tag values we have observed from HeaconLoad variants:

  * kylka
  * leon
  * shrek
  * sonic
  * voblya
  * yaropolk
  * yarostnick
  * yasno



HeaconLoad then checks fields such as “ _bundle_available_ ” and “ _bundle_hash_ ” in the attacker’s response to its HTTP POST request. These two fields respectively indicate whether a bundle is available for download and provide the hash value of the bundle to download for verification.

[ ![Figure 18. HeaconLoad checks the “bundle_available” field from attacker’s response](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig18.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig18.png)

Figure 18. HeaconLoad checks the “bundle_available” field from attacker’s response

When a bundle is available, HeaconLoad further downloads and unzips a bundle archive from the attacker’s server. It executes the first executable found in the unzipped archive.

We observed Russian log messages in HeaconLoad samples.

[ ![Figure 19. Russian-language log message in HeaconLoad \(translated as “data marshaling error”\)](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig19.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig19.png)

Figure 19. Russian-language log message in HeaconLoad (translated as “data marshaling error”)

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig19.png)

# Custom build exe: Vidar variant with code obfuscation

The binary executables downloaded from “ _/api/custom_exe?build={BUILD_NAME}_ ” are variants of the existing Vidar stealer with code obfuscation.

The sample (SHA256: 2050468744e44554fac17fb83f1515c95f2f2236716e2b5267a81c2b94205e6a) possesses a functionality that sends HTTP POST requests with traffic patterns used by the Vidar stealer. It uses XOR-encrypted strings and contains opaque predicates with redundant code for obfuscation.

[ ![Figure 20. Vidar variant sends information.txt to the attacker via POST request](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig20.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig20.png)

Figure 20. Vidar variant sends information.txt to the attacker via POST request

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig20.png)

The Vidar variant also dynamically resolves its API for obfuscation and can also perform code injection or APC injection.

# BoryptGrab: C/C++ Stealer

BoryptGrab takes an optional "--output-path"/"-o" argument that specifies the output directory to hold data it collects. Depends on the build, some variants of BoryptGrab (SHA256: fe4e5fb28d2c2b3a640112b6b125ce8c4afa8be28342e3bfda097ad9dd2ef9ee) also take an optional “--build-name”/“-b” command line argument as input. This input argument is used as the value of the “ _BUILD NAME_ ” field when BoryptGrab outputs user information to the _UserInformation.txt_ file. When no “--build-name” argument is provided, the BoryptGrab variant uses the default build name “No_name”.

[ ![Figure 21. Arguments parsed by BoryptGrab](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig21.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig21.png)

Figure 21. Arguments parsed by BoryptGrab

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig21.png)

Meanwhile, some variants of BoryptGrab use hardcoded values for the “BUILD NAME” field in _UserInformation.txt_ instead of parsing the “--build-name”/“-b” argument.

[ ![Figure 22. Hardcoded build name “CryptoByte” in BoryptGrab](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig22.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig22.png)

Figure 22. Hardcoded build name “CryptoByte” in BoryptGrab

Note that there are also BoryptGrab variants that do not contain hardcoded the “BUILD NAME” and do not parse the “--build-name”/“-b”. command line argument. They also do not write the “BUILD NAME” field to the _UserInformation.txt_ file.

The following shows a list of build name values hardcoded in the BoryptGrab variants we have observed in the wild:

  * CryptoByte
  * Crypto_Byte
  * Data
  * Kassay
  * Leon
  * Pisechka
  * Shrek
  * Sonic
  * Sonic2
  * Sonic_new1
  * Sonic_new2
  * Yaropolk
  * Yarostnick
  * Yasno
  * bigdick
  * wm_detect



BoryptGrab detects whether it is executed in a virtual machine environment by querying registry entries and checking VM-related files.

As part of its anti-analysis check, BoryptGrab also compares the names of running processes against a predefined list. It also attempts to execute with elevated privilege.

When the "--output-path"/"-o" argument is not given, BoryptGrab formats a default output path name using the current time, public IP address, and country code. Later, a directory with this output path name is created to stage collected data.

BoryptGrab collects information from a list of browsers. It uses Chrome App Bound Encryption techniques and contains code from the following public GitHub repositories:

  * https://github[.]com/00nx/Chrome-App-Bound-Encryption-Bypass
  * https://github[.]com/xaitax/Chrome-App-Bound-Encryption-Decryption



The following are the list of browsers BoryptGrab collects information from:

  * Brave Browser
  * CentBrowser
  * Chromium
  * Google Chrome
  * Microsoft Edge
  * Mozilla Firefox
  * Opera
  * Vivaldi
  * Yandex Browser



BoryptGrab uses code similar to the loadAndDecryptPayload function in https://github[.]com/00nx/Chrome-App-Bound-Encryption-Bypass, while also containing a binary with an encrypted resource named “PAYLOAD_DLL”, as used by the GitHub repository.

The decrypted PAYLOAD_DLL resource in BoryptGrab contains logic from the Chrome-App-Bound-Encryption-Bypass public Github repository. The decrypted resource payload in BoryptGrab also contains functionality that collects browser data from Yandex and Firefox.

[ ![Figure 23. PAYLOAD_DLL payload in BoryptGrab collects passwords from the Yandex browser](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig23.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig23.png)

Figure 23. PAYLOAD_DLL payload in BoryptGrab collects passwords from the Yandex browser

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig23.png)

The decrypted PAYLOAD_DLL payload also contains hardcoded timestamp information. It writes the timestamp along with installed application information to the “ _installed_applications.txt_ ” file.

[ ![Figure 24. The PAYLOAD_DLL payload writes the hardcoded timestamp along with the installed applications](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig24.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig23.png)

Figure 24. The PAYLOAD_DLL payload writes the hardcoded timestamp along with the installed applications

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig24.png)

To help collect browser data, BoryptGrab downloads a Chromium helper (SHA256: ed1745cc49b929e499966d87e163219fe0f24069fe88dfacbd69c0ebab85a640) from “ _hxxp://45.93.20[.]61:5466/api/x32_chromium_ ” __ and saves it to _%TEMP%\ x32_chromium.exe_.

Aside from browser data, BoryptGrab can harvest information from both desktop cryptocurrency wallet applications and browser extensions. BoryptGrab then captures a screenshot and collects system information.

[ ![Figure 25. Log messages for cryptocurrency wallet information in BoryptGrab](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig25.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig25.png)

Figure 25. Log messages for cryptocurrency wallet information in BoryptGrab

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig25.png)

The following cryptocurrency wallet directories are targeted by BoryptGrab:

  * Armory Wallet
  * Atomic
  * AtomicDEX
  * Binance
  * Bitcoin Core
  * BitPay
  * Blockstream Green
  * Chia Wallet
  * Coinomi
  * Copay
  * Daedalus Mainnet
  * Dash Core
  * Dogecoin
  * Electron Cash
  * Electrum
  * ElectrumLTC
  * Ethereum
  * Exodus
  * GreenAddress
  * Guarda
  * Jaxx Desktop
  * Komodo Wallet
  * Ledger Live
  * Ledger Wallet
  * Litecoin Core
  * MEW Desktop
  * MultiDoge
  * MyEtherWallet
  * NOW Wallet
  * Raven Core
  * StakeCube
  * Trezor Suite
  * Wasabi Wallet



BoryptGrab also contains a “File Grabber” ability, where it collects files with specified extensions under common directories. It contains a misspelled word: “Filegraber”.

[ ![Figure 26. Examples of file extensions harvested by BoryptGrab](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig26.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig26.png)

Figure 26. Examples of file extensions harvested by BoryptGrab

Finally, BoryptGrab collects Telegram files and browser passwords, with newer variants of BoryptGrab being able to gather Discord tokens.

After data collection, BoryptGrab archives and uploads its collected data to the attacker’s server.

Some BoryptGrab variants download and execute TunnesshClient from the attacker’s server. However, not all BoryptGrab variants have this functionality, and in some attack chains, TunnesshClient is delivered by other downloaders instead.

[ ![Figure 27. Traffic from BoryptGrab variant to download TunnesshClient](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig27.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig27.png)

Figure 27. Traffic from BoryptGrab variant to download TunnesshClient

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig27.png)

# TunnesshClient: PyInstaller executable with reverse SSH Tunnel

TunnesshClient is a PyInstaller executable that conducts traffic forwarding and executes the attacker’s commands through a reverse SSH tunnel. It contains Russian text in its comments and log messages, indicating possible origins. The TunnesshClient sample used in this blog for demonstration (SHA256: 576692df4bf1c7d8927d3a183f5219a81c3bff3dd22971691f8af6889f80c5a0) connects to the attacker’s server at 193.143.1[.]104.

TunnesshClient first retrieves SSH credentials by sending HTTP POST requests (_/api/get_challenge_ , _/api/get_credentials_) to hxxp://193.143.1[.]104:5000. It solves the attacker’s challenge by computing a SHA256 hash to retrieve an encrypted response. It then decrypts the response to obtain SSH credentials in JSON format.

[ ![Figure 28. TunnesshClient sends HTTP POST requests to retrieve SSH credentials from the attacker](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig28.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig28.png)

Figure 28. TunnesshClient sends HTTP POST requests to retrieve SSH credentials from the attacker

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig28.png)

TunnesshClient then sends system information to the attacker at “ _/api/get_port_ ”. It retrieves a port number for remote port forwarding from the attacker’s response, then creates a reverse SSH tunnel using its previously retrieved SSH credentials and traffic-forwarding port number to communicate with the attacker’s server.

TunnesshClient can execute commands provided by the attacker. It receives an integer value from the attacker’s connection, which represents the operation type of the command to execute.

[ ![Figure 29. Operation types parsed by TunnesshClient variant](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig29.png) ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig29.png)

Figure 29. Operation types parsed by TunnesshClient variant

[ download ](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/Fig29.png)

The following table lists the operation types supported by the TunnesshClient sample and their corresponding commands:

**Operation type** | **Description**  
---|---  
5 | Act as SOCKS5 proxy  
83 | Execute shell command  
76 | List specified files  
68 | Send victim’s file to attacker in base64 encoding  
85 | Save Base64-encoded file content from attacker to victim’s machine  
70 | Search for file with specified query  
90 | Send victim’s folder to the attacker in a Base64-encoded ZIP archive  
  
Table 1. Operation types supported by the TunnesshClient sample and their corresponding commands

Another variant of TunnesshClient (SHA256: 0434437a073a3f3a49e84d5ecb20c99dd551bacc32bf100fbb8cf67a50642181) sets up a local SSH server on the victim machine. It sends the username and password for local SSH connection to the attacker through an HTTP POST request (hxxp://45.93.20[.]195:5000).

When the operation type is 83, this TunnesshClient variant forwards the attacker’s traffic to the local SSH server. This variant only accepts operation type 5 and 83, and does not execute the attacker’s commands as the previous variant does.

Operation type | Description  
---|---  
5 | Act as SOCKS5 proxy  
83 or other values | Local SSH forwarding  
  
# Conclusion

The BoryptGrab campaign illustrates an evolving threat ecosystem targeting users through deceptive software downloads and fake GitHub repositories. Across its many variants, the stealer demonstrates extensive data‑harvesting capabilities, with its ability to dynamically stage payloads, bypass analysis through anti‑VM and anti‑debug checks and offload sensitive operations to encrypted payloads showing a level of engineering sophistication that continues to increase.

The campaign’s reliance on SEO‑optimized GitHub repositories and fake “free tool” download sites underscores an important trend: threat actors increasingly exploit trust in legitimate developer platforms and open‑source ecosystems. With dozens of repositories, shifting payloads, and numerous build names observed in the wild, the operation’s scale indicates an active and ongoing threat.

# Proactive security with TrendAI Vision One™ 

[TrendAI Vision One™](/en/business/products/one-platform.html) is the industry-leading AI cybersecurity platform that centralizes cyber risk exposure management, security operations, and robust layered protection.

# TrendAI Vision One™ Threat Intelligence Hub 

[TrendAI Vision One™ Threat Intelligence Hub](/en/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. 

Emerging Threats: [From Fake GitHub Download Repositories to Reverse SSH Backdoors: Examining the BoryptGrab Stealer](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=From%20Fake%20GitHub%20Download%20Repositories%20to%20Reverse%20SSH%20Backdoors%3A%20Examining%20the%20BoryptGrab%20Stealer "From Fake GitHub Download Repositories to Reverse SSH Backdoors: Examining the BoryptGrab Stealer")

## TrendAI Vision One™ Intelligence Reports (IOC Sweeping) 

[From Fake GitHub Download Repositories to Reverse SSH Backdoors: Examining the BoryptGrab Stealer](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=From%20Fake%20GitHub%20Download%20Repositories%20to%20Reverse%20SSH%20Backdoors%3A%20Examining%20the%20BoryptGrab%20Stealer)

# Hunting queries 

## TrendAI Vision One™ Search App 

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

**Detection of BORYPTGRAB samples**

malName: *BORYPTGRAB* AND eventName: MALWARE_DETECTION AND LogType: detection

More hunting queries are available for TrendAI Vision One™ [with Threat Intelligence Hub](/en/business/products/threat-intelligence.html) entitlement enabled. 

**TrendAI Vision One™ Network Security**

  * 46934: HTTP: Trojan.Win64.BoryptGrab.A Runtime Detection
  * 46935: HTTP: Trojan-Downloader.Win64.HeaconLoad.A Runtime Detection
  * 46937: HTTP: Backdoor.Python.TunnesshClient.A Runtime Detection



# Indicators of Compromise (IoCs)

The indicators of compromise for this entry can be found [here](/content/dam/trendmicro/global/en/research/26/c/boryptgrab/20260309_IOCs_BoryptGrab.txt).

Tags

[Malware](/en/research.html?category=trend-micro-research:threats/malware) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats)

###  Authors 

  * Mingyue Shirley Yang

Malware Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)