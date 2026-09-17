# FSB’s matryoshka #3/3: Gamaredon's Gammasteel Infostealer

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/fsbs-matryoshka-3-3-gamaredons-gifts-that-keeps-unpacking-gammasteel
- **Date :** 2026-06-04

---

This investigation is published in three parts. Follow the links below to navigate through our findings:

  * [FSB’s matryoshka #1/3](/blog/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm) \- **GammaPhish** and **GammaWorm**
  * [FSB’s matryoshka #2/3](/blog/fsbs-matryoshka-2-3-gamaredons-gifts-that-keeps-unpacking-gammaload) \- **GammaLoad**
  * FSB’s matryoshka #3/3 - **GammaSteel**(this article)



## Introduction

The Sekoia.io **Threat Detection & Research** (TDR) team continuously monitors **Gamaredon**(aka UAC-0010, Armagedon), an **FSB operated Russian intrusion-set historically targeting Ukrainian governmental and critical infrastructure**. In our last report FSB’s matryoshka #2/3, we detailed the middle stages of their January 2026 infection chain, focusing specifically on their staging mechanisms.

Tracking Gamaredon’s ongoing campaigns presents **significant challenges** due to the rapid development cycle and the cybersecurity industry's fragmented naming conventions. Over the past decade, their espionage arsenal has heavily evolved, shifting from the **Pteranodon** framework to highly modular, standalone payloads tracked under various names. To cut through this complexity and bring clarity to their current capabilities, **Sekoia.io aligns with CERT-UA’s taxonomy** , grouping the malware by its primary function: 

  * **GammaPhish**(initial access)
  * **GammaLoad**(intermediary loaders)
  * **GammaWorm**(worm)
  * **GammaSteel**(stealer)
  * **GammaWipe**(wiper)



_Note: We use the term loader when the execution chain remains entirely in-memory without writing files to disk, whereas dropper refers to stages where a file is written to the file system._

Building upon our initial publication, and thanks to over 70 artifacts retrieved by a trusted partner alongside our own live interactions with Gamaredon’s C2 staging infrastructure, we are continuing our series documenting Gamaredon 2026 arsenal. This third report focuses on **GammaSteel** , the **global infrastructure** used across the infection chain, and an analysis of the **obfuscation and anti-analysis** techniques.

## Infection chain

### GammaSteel

A final payload in this infection chain is a stealer. Its primary objective is to exfiltrate user personal documents to a C2 infrastructure. It performs the following actions:

  * **Fileless registry staging:** operates almost entirely from memory. It uses Windows DPAPI to encrypt and stage 71 distinct payload functions directly inside the `HKCU\Printers` registry key.
  * **Data acquisition:** a central orchestrator function actively hunts for targeted documents using three concurrent methods: recurring scans of local and network drives, monitoring for newly inserted USBs, and real-time surveillance of files as they are saved or modified.
  * **Exfiltration:** to minimize network noise, candidate files are locally deduplicated against a log of previously exfiltrated MD5 hashes. The data is then systematically uploaded to legitimate S3-compatible cloud storage (Tebi.io).
  * **Backdoor:** if the primary cloud infrastructure fails, the stealer falls back to operator-controlled C2 servers or scrapes Dead Drop Resolvers to recover fresh credentials. The fallback C2 channel operates bidirectionally, allowing the operator to execute arbitrary remote code delivered in the HTTP responses.



We successfully acquired this payload by replaying active network requests from GammaLoad analysed in the second report of this series. The payload is an obfuscated PowerShell script that acts as a dropper for the stealer. The code employs Base64 encoding combined with a XOR cipher, a few functions, but for the most part it consists of 71 functions.

Upon execution, the script defines a toolkit of helper functions designed to obfuscate the infection process. A decryption routine first handles the unpacking of embedded payloads by decoding Base64 strings and applying a second XOR operation using a hardcoded key. This process unpacks the initial code segments directly into memory.

#### Gamaredon is now using DPAPI 

Following the initial decryption, the script employs a specific mechanism to re-encrypt the function using the Windows Data Protection API (DPAPI). By leveraging the ConvertTo-SecureString and ConvertFrom-SecureString functions without specifying a key, the code binds the encryption to the current user’s session. This ensures that the generated registry payloads can only be decrypted by the logged-in user on the compromised host, complicating forensic analysis if the registry hives are exfiltrated without the user's master keys. 

**This is the first time Gamaredon is using this TTP.**

The execution logic iterates through 71 distinct PowerShell functions contained within the script, which collectively craft the stealer. Each function is sequentially passed through the deobfuscation, DPAPI encryption, and registry writing functions. This results in the storage of 71 encrypted functions within the `HKCU\Printers\` registry key. At this moment, the code is fully staged within the registry waiting to be executed.

#### The orchestrator

A specific function is acting as an orchestrator for the stealer. Like other functions, it is stored within the `HKCU\Printers` under the key `KeZdDboas5kpxbkgxxvBx`. This component is responsible for managing the other 70 staged functions. Before detailing its internal logic, it is worth noting the methodology employed to trigger this orchestrator, ensuring both immediate execution and long-term persistence.

To initiate the orchestrator, the code instanciates a detached and hidden PowerShell window process using the following command:

`Start-Process -FilePath "powershell" -ArgumentList "-noexit", 'powershell.exe -nol -nop -enc [PAYLOAD EXECUTING ORCHESTRATOR]' -WindowStyle Hidden;`

The encoded payload instructs this new child process to read the registry, retrieve the orchestrator function, decrypt it via DPAPI and execute it in memory. This effectively split the orchestrator from the initial dropper, allowing it to run as an independent, hidden background task.

Simultaneously, the code establishes persistence by installing a task designed to relaunch the orchestrator upon system startup. It writes a specific PowerShell command into the `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` key, using the operating system name (`$env:os`) as the value name to blend in. 

`powershell.exe -w hidden -command "$a='HKCU:\Printers'; $b=Get-ItemProperty -Path $a -Name 'YxwHku2chu0bznt3kkyAB'; $c=$b.YxwHku2chu0bznt3kkyAB; $d=[scriptblock]::Create($c); &$d"`

Rather than storing the full payload in the Run key, this entry acts as a pointer. It reconstructs the obfuscated path to `HKCU\Printers`, retrieves the orchestrator code stored in the separate `HKCU\Printers\YxwHku2chu0bznt3kkyAB` key, and executes it.

On the other hand, it reads this newly created registry key and executes it using the following code:

`powershell.exe -w hidden -command "$HIBdqts3rtuonnvozqAjU = (Get-ItemProperty -Path 'HKCU:\Printers' -Name 'YxwHku2chu0bznt3kkyAB').YxwHku2chu0bznt3kkyAB; $zCZZm1uyck0njfsnFPli = [scriptblock]::Create($HIBdqts3rtuonnvozqAjU); Invoke-Command -ScriptBlock $zCZZm1uyck0njfsnFPli"`

This persistence mechanism is mirrored for immediate effect within the dropper itself. The code explicitly retrieves the same registry key and executes it.

This sequence of configuring the persistence registry key `HKCU\Printers\YxwHku2chu0bznt3kkyAB` and forcing the immediate execution of its content is encapsulated within a final variable block triggered by an invoke-expression command at the very end of the script.

This creates a redundancy where the orchestrator is triggered not only via the detached process mentioned earlier, but is also injected directly into the memory of the current process, maximizing the probability of successful infection.The orchestrator also initialises a **mutex** named `Global\assembly307`.

### Data acquisition

Having established the execution flow of the orchestrator, we can now analyse the data acquisition capabilities of the stealer before exfiltration. The orchestrator operates as a centralised surveillance hub, deploying three concurrent mechanisms.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a65128af_6a92a1354c776939a1e0a860_6a2a809db97c48a61ea7720c.webp)

_Note: the letters used are for illustrative purposes only._

These mechanisms are designed to target data in three specific states: data at rest (stored files), data in transit (physical transfer via USB), and data in use (files currently being edited). To achieve this full-spectrum coverage, the code initialises three distinct listeners:

  * **Files drive exploration** : a time-based routine that scans local hard disks and network shares for static files.
  * **USB drive monitoring** : a hardware event listener specifically targeting USB mass storage devices to intercept physical data transfer.
  * **Real-Time file surveillance** : an active watcher that monitors fixed drives for any immediate user activity, such as saving or modifying a document.



#### Files drive exploration

The orchestrator establishes a time-based persistence mechanism designed to execute a specific payload at regular intervals. It initialises a `System.Timers.Timer` object configured with a duration of 3,600,000 milliseconds (one hour). By setting the `AutoReset` property to `True`, the orchestrator ensures this is a recurring cycle rather than a single event. 

`$UAIPh3lmau2x0g34RcX = New-Object System.Timers.timer;  
$UAIPh3lmau2x0g34RcX.Interval = 3600000;  
$UAIPh3lmau2x0g34RcX.AutoReset = $true;  
Register-ObjectEvent -InputObject $UAIPh3lmau2x0g34RcX -EventName "Elapsed" -Action {  
Start-Process -FilePath "powershell" -ArgumentList '[PAYLOAD IN HKCU:\rinters\plLmfuh4uctxjtrQSXC' -WindowStyle Hidden;  
}  
$UAIPh3lmau2x0g34RcX.Start();  
`

This operation spawns a new detached PowerShell process using the `-WindowStyle Hidden` parameter that will execute the payload in `HKCU\Printers\plLmfuh4uctxjtrQSXC`.

The function `plLmfuh4uctxjtrQSXC` conducts a reconnaissance phase to map all available local hard disks and network shares for static files. This process is divided into two distinct mechanisms designed to explore and exfiltrate data on system partition, secondary partition, network share shares or external drive.

**The first mechanism** targets user-specific data residing on the system partition. The script queries the WMI class with `gwmi win32_userprofile` to enumerate all profiles present on the machine. To ensure it targets legitimate users rather than system accounts, it implements a filter on the Security Identifier (SID) starting with `S-1-5-21`. This effectively excludes built-in accounts such as LocalService (`S-1-5-19`) or NetworkService (`S-1-5-20`). For every matching profile identified, the script extracts the LocalPath property (_e.g._ , `C:\Users\JohnDoe`) and passes this path directly to an exfiltration function.

**The second mechanism** enumerates all mounted filesystems (system partition, secondary partition, network share shares or external drive) to capture data residing on secondary partitions or network shares. It executes `Get-PSDrive -PSProvider FileSystem | Sort-Object Name -Descending`, sorting the results in descending alphabetical order to prioritise non-system drives (_e.g._ , `Z:` before `C:`). For each discovered drive letter, the code fingerprints the hardware type by executing a specific WMI query: `Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='[Drive Letter]:'"`. 

Based on the integer returned in the `DriveType` property, the code adapts its logic. If the `DriveType` is `2` (for USB), the execution is diverted to a dedicated USB staging function rather than its own exfiltration function (described later in the USB drive monitoring section). For fixed disks (`DriveType = 3`) or network drives (`DriveType = 4`), the script performs a de-confliction check by comparing the drive root against the `$env:userprofile` environment variable. 

If the drive matches the system partition (typically `C:`), the scan is aborted to prevent overlap with the first mechanism described above. On the other hand, if the drive is identified as a distinct data volume (such as a secondary data drive `D:\` or a network share `Z:\`), its root path is immediately sent to the exfiltration function.

#### USB drive monitoring

The orchestrator establishes a listener for USB mass storage. The code uses `Register-WmiEvent` to subscribe to all the event notifications where the drive is a USB flash drive.

`Register-WmiEvent -Query "select * from __InstanceCreationEvent within 5 where TargetInstance ISA 'Win32_LogicalDisk' and TargetInstance.DriveType = 2" -Action $cjObc0rpxzoo55zghAOT -SourceIdentifier USBFlashDrive;`

It spawns a hidden PowerShell process that retrieves and executes a function from the registry. 

Once an external USB drive is identified, the function iterates through a hardcoded list of target extensions : `*.doc`, `*.docx`, `*.dot`, `*.xls`, `*.xlsx`, `*.ppt`, `*.pptx`, `*.pps`, `*.xps`, `*.wpd`, `*.wll`, `*.psd`, `*.ai`, `*.vsd`, `*.rtf`, `*.odt`, `*.ods`, `*.odp`, `*.txt`, `*.pdf`, `*.md`, `*.csv`, `*.rar`, `*.zip`, `*.7z`, `*.mdb`, `*.jpg`, `*.jpeg`, `*.tmp`.

For each matching file, the function initiates a replication. Rather than exfiltrating directly from the external media, the function constructs a covert staging directory on the host's system drive, retrieved via `$env:userprofile` (or `$env:programdata` as fallback). This directory is located within `%UserProfile%` (or `%ProgramData%`) and is named using the first 15 characters of the machine's GUID, retrieved from `HKLM\SOFTWARE\Microsoft\Cryptography`. The directory is explicitly hidden using the `attrib +h` command.  
Once the files are successfully duplicated to this hidden staging folder, the function starts exfiltration function. This function iterates through the staging folder and exfiltrates each file. If the exfiltration is successful, the local copy file in the staging folder is deleted using `Remove-Item`.

#### Real-Time file surveillance

Beyond these timed and hardware events, the orchestrator also deploys an active file monitoring system. First it , use the following command:

`Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -ne 2 };`

This command iterates through all non-USB logical disks, _e.g._ fixed drives including both the system partition and any secondary local disks or network shares. Then, the orchestrator attaches a `System.IO.FileSystemWatcher` to the root of each drive. This watcher is configured to listen for any changes to files matching the exact same extension as the USB drive monitoring.

`$heSTrjgbmmwf31pvTqeN = New-Object IO.FileSystemWatcher;  
$heSTrjgbmmwf31pvTqeN.NotifyFilter = [IO.NotifyFilters]"FileName, DirectoryName, Attributes, Size, LastWrite, Security";  
$heSTrjgbmmwf31pvTqeN.EnableRaisingEvents = $true;  
$heSTrjgbmmwf31pvTqeN.IncludeSubdirectories = $true;  
  
$VKynhi5axdxmalgZmv = Register-ObjectEvent $heSTrjgbmmwf31pvTqeN -EventName "Changed" -Action {[EXFILTRATION]}  
`

This watcher is configured to operate recursively and listens specifically for the event called Changed, meaning it triggers the moment a user saves or modifies a targeted file. When captured, the full path is retrieved via `$Event.SourceEventArgs.FullPath` and sent to the exfiltration function.

### Exfiltration

The function of exfiltration orchestrates deduplication of target files to ensure only unique and high-value data is exfiltrated to the C2 infrastructure. This function is called on every mechanism of the data acquisition.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a65128b2_6a92a1336568d7e2b407c9da_6a2a809db97c48a61ea771f7.webp)

Upon receiving a candidate file path, the function converts the string to lowercase and validates it against a hardcoded exclusion list. To prevent the collection of system binaries or non-user data, paths containing windows, appdata, public, all users, default, or prog (that will catch Program Files for example) are discarded.

To maintain operational stealth and efficiency, the function implements a local deduplication mechanism. It generates a tracking file located in `%UserProfile%` (or `%ProgramData%` as a fallback), named using the first ten characters of the machine's GUID with no file extension, for example `C:\Users\Admin\d1a84c20-5`. This flat text file acts as an history log, containing a list of MD5 hashes for previously exfiltrated content. Before initiating an exfiltration, the function calculates the MD5 hash of the candidate file using the `Get-FileHash -Algorithm MD5` function and queries this local database using `Select-String`. If the hash is present, the file is ignored; if new, the script proceeds to the exfiltration stage.

Exfiltration is attempted across a tiered infrastructure comprising legitimate cloud storage, hardcoded fallback servers, and dynamic endpoints resolved via DDR. 

The primary method involves an HTTP PUT request to an S3-compatible object storage service. The specific provider is determined by a decrypted configuration string within the registry. In the analysed sample, this value resolves to `tebi`, directing traffic exclusively to `s3.tebi[.]io`. The function checks if the configuration was set to set, it would use `de-fra.i3storage[.]com`; any other value is interpreted as a specific region subdomain, injected in `hxxps://s3.[VALUE].wasabisys[.]com`.

For the first requests on an S3, the function injects the metadata directly into the URL. The schema employed to construct this PUT request is structured as follows:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a65128a0_6a92a130c5553634ac94296d_6a2a809cb97c48a61ea771d6.webp)

The distinct components comprising the S3 object key and associated headers are detailed in the table below. Note that it forces the `Content-Type` to `text/plain` regardless of the actual file format, likely to bypass content-based filtering policies.

**FieldPattern / ValueUSER_ID** Concatenation of the computer name and the hexadecimal Volume Serial Number (e.g., DESKTOP-5A_182392).**MD5** MD5sum of the stolen file**FILENAME** The original filename, truncated to the last 100 characters.**RELATIVE_PATH** The parent directory path, stripped of the user root (C:\Users\Admin) and drive letter colons. Truncated to 170 characters (e.g., \Documents\ProjectX).**Content-Type** text/plain (hardcoded)

If the exfiltration is successful, the stolen file's hash is appended to the local tracking file to avoid future re-uploads. However, if the S3 upload fails due to network restrictions or revoked credentials, the function triggers a fallback mechanism. It queries the local registry configuration for a domain and IP address, which default to the hardcoded endpoints `hxxps://justsstop[.]ru/` and `hxxps://165.22.170[.]129/`.  
Unlike the S3 routine, which exposes metadata in the URL, this fallback mechanism obfuscates the metadata within a multipart/form-data structure. The request masquerades as an iPhone device using an hardcoded User-Agent string. The schema for this POST request is defined as follows:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a651289d_6a92a133a2f46752fd0069fb_6a2a809cb97c48a61ea771f2.webp)

Here is the table that describe the variables used:

**FieldPattern / ValueUser-Agent** Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1 (Hardcodé)**Body field metadata**[PREFIX_1] + y + [SUFFIX], where PREFIX_1 is 5 random chars, and SUFFIX is 5-10 random chars**Body field Payload**[RANDOM]::1000::[RANDOM]::[FOLDER:]::[RANDOM]::[MODIFICATION_DATE]::[RANDOM]::[SIZE_BYTES]::[RANDOM]::[USER_ID]::[RANDOM]::[MD5_FILE]::[RANDOM]A Base64-encoded string containing the victim ID, file path, and timestamps with random "junk" data and :: delimiters.**Body field file**[PREFIX_2] + z + [SUFFIX] , where PREFIX_2 is 5 random chars, and SUFFIX is 5-10 random chars**Filename** A random string of 5 to 10 characters (e.g., Kjm19.dat).

The following reconstruction demonstrates the format of the POST request with randomized values generated by the function:

This fallback channel operates bidirectionally. Beyond data exfiltration, the code can read the HTTP response to execute any arbitrary VBScript code on the victim's machine. Indeed, upon completing the upload, the function searches the C2’s response body for the specific string literal on error. If this delimiter is detected, the script extracts all content preceding it. This payload is written to a temporary file in `C:\Users\[USER]\AppData\Local\Temp\tmp[XXXX].tmp` (via `[System.IO.Path]::GetTempFileName())` and execute it using `wscript.exe [TEMP_FILE_PATH] //e:vbscript //b`. 

This confirms that the hardcoded C2 endpoints serve a dual purpose: they act as a receiver for stolen documents when the primary cloud storage is inaccessible, and simultaneously function as a gateway for remote code execution.

If both the primary S3 exfiltration channel and the fallback hardcoded C2 endpoints are unreachable, the function initiates a configuration recovery function. This function leverages a DDR technique, querying legitimate and high-reputation public platforms to retrieve fresh C2 and S3 credentials.

The script sequentially executes HTTP GET requests four hardcoded URLs hosted on Telegra.ph, Write.as, Rentry[.]co, and Mastodon. The function terminates upon the first successful retrieval of valid configuration data. Each of these pages hosts encoded strings containing the necessary components to update the S3 exfiltration credentials (Access key, Secret key, Provider and Bucket name) alongside a domain and IP address for the fallback requests. We observe that the configurations hosted on Telegra.ph, Write.as, and Rentry[.]co are identical. However, the Mastodon payload serves a distinct configuration, pointing to a different S3 bucket (`set4` versus `set3`) and a modified secret key.

Upon successful parsing, these elements overwrite the function’s current configuration within the registry. Consequently, the next exfiltration cycle will utilise a fresh infrastructure.

If all DDR requests fail, the function executes a final failsafe: it performs a reset of the configuration. It hardcodes the IP `165.22.170[.]129` and the domain `justsstop[.]ru` back into the registry. This logic is interesting; it mitigates the risk of the stealer being stranded with an obsolete DDR configuration (_e.g_., a deleted Mastodon post) by reverting to the initial default infrastructure, hoping that it has returned online.

In summary, this tiered failover mechanism ensures long-term operational resilience by diversifying the infrastructure supply chain. Furthermore, the ability to execute arbitrary VBScript via the fallback C2, indicates that the operator intends not only to maintain data theft capabilities but also preserves a channel for the deployment of additional payloads.

## Analysis of the infrastructure

### Dead Drop Resolvers (DDR)

The infrastructure established for this campaign demonstrates a blend of Dead Drop Resolvers, legitimate social media platforms, and operator-controlled servers. **Gamaredon relies heavily on DDRs** to facilitate communication for worm, loaders and stealer, using these services to **retrieve C2 configurations and staging details** (such as IP addresses, domains, and services like TryCloudflare or `workers[.]dev` or to**host secrets including tokens** for S3 cloud storage.

Identified services used in this campaign include Telegram, Telegraph, Teletype, Lesma.eu, check-host.net, Rentry[.]co, Write.as, and Mastodon.

For platforms such as Telegram, check-host.net, and Lesma.eu, the hosted payloads typically consist of domains, URLs, or IP addresses sometimes protected by basic obfuscation, which is cleared using VBScript regular expressions. 

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a65128ac_6a92a134cd1cab63350c0912_6a2a809db97c48a61ea771fb.webp)

In the case of Lesma.eu, the specific URL recovered during real-time analysis was unresponsive. On the other hand, the check-host.net implementation revealed the use of actor-controlled domains, specifically `norosta[.]ru` and randomized subdomains of `selltosell[.]ru`, to resolve C2 or staging IP.   
Conversely, Rentry[.]co, Write.as, and Mastodon served a broader purpose, hosting both network indicators and S3 bucket credentials, specifically the access key, secret key, provider name, and bucket ID. The following screenshots shows the user-facing view of the targeted URLs (and not the one requested by the function in API mode):

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a65128a9_6a92a131a2f46752fd006966_6a2a809cb97c48a61ea771d9.webp)

Regarding Mastodon, it is interesting to note that posts history can be traced back to the creation of the user account `@6o786d68hu`. These messages date back to 6 October 2025 and were likely generated during the development phase of the chain:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a65128a3_6a92a12e693fca262e1a2ac2_6a2a809cb97c48a61ea771cd.webp)

The content hosted on these DDRs undergoes **frequent modification, multiple times daily**. To analyze the update cadence, **we monitored the specific Mastodon account** hardcoded within the stealer’s data exfiltration function, polling for changes every minute between January and February 2026. We observed a clear pattern of automation:**posts were consistently updated** four times per day at uniform intervals with a variance of only a few minutes. This pattern indicates an **automated mechanism** ; update times remain consistent within a five-minute window.

It is worth noting a possible correlation between the **one-day pause** in Gamaredon's automated data exfiltration activity on 13 February and **Ukrainian drone strikes conducted the day prior**. On 12 February, Ukrainian drone units reportedly [targeted a data centre in Prymorsk](https://militarnyi.com/en/news/unmanned-systems-forces-data-center-airbase/), a facility contributing to Russian telecommunications infrastructure across occupied southern and eastern Ukraine, including [Crimea](https://euvsdisinfo.eu/russias-information-grip-on-ukraines-occupied-territories/). This geography is consistent with Gamaredon's suspicion of an operational base: In November 2021, Ukraine's Security Service (SBU) [publicly identified](https://ssu.gov.ua/en/novyny/sbu-vstanovyla-khakeriv-fsb-yaki-zdiisnyly-ponad-5-tys-kiberatak-na-derzhavni-orhany-ukrainy) five members of the group as officers of the FSB's Crimean branch, assessed to operate from Sevastopol and acting on orders from FSB Center 18 in Moscow. While a direct causal link remains unconfirmed, **kinetic damage to these power and communications facilities may have temporarily disrupted the**[**local network infrastructure**](https://www.rnbo.gov.ua/files/2023_YEAR/CYBERCENTER/Gamaredon_activity.pdf)**on which the group relies**. This disruption appears to have been short-lived, as automated activity resumed shortly after the single-day gap.

Over this one-month observation, we extracted 115 unique IP addresses, four domains, and five distinct sets of S3 credentials (bucket name, access key, and secret key) all linked to a single provider: Tebi.io. Notably, Tebi.io is scheduled to cease operations in late March 2026, [a detail reportedly communicated](https://judis.id/cloud/tebi-io-shutdown-2026-migrasi-cloud-storage/) to users via email rather than a public announcement.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a51cadf0bb92a65128a6_6a92a12f3e6167cebbf544e1_6a2a809cb97c48a61ea771d0.webp)

Given that the infection chain appears to have been active since late December 2025, the selection of this provider suggests a deliberate operational choice rather than mere opportunism. 

Finally, it is also worth noting that Rentry[.]co includes a view counting feature. For instance, the URL `hxxps://rentry[.]co/hwzrmfkx` retrieved on 23 January 2026, registered over 2890 views. While Rentry’s documentation [lacks specific detail](https://rentry.co/what) beyond stating that views are “ _updated every 10 minutes_ ”, it is highly probable that this metric represents a raw view count, incrementing even upon page refreshes.

### DDNS and Cloud service

A part of the infrastructure relies on Dynamic DNS (DDNS) services provided by [No-IP](https://www.noip.com/). Domains such as `serveirc[.]com`, `webhop[.]me`, `serveftp[.]com`, and `myvnc[.]com` are primarily observed during the initial access phase, with only a single occurrence noted within the first-stage loader. 

Furthermore, Gamaredon leverages Supabase to host its payloads, exploiting the platform's positive reputation to evade basic security filters. As a legitimate Backend-as-a-Service provider, Supabase offers an infrastructure attractive for short-term operational use. In this campaign, the service is used to host a decoy PDF file embedded with malicious VBScript.

### Operator-controlled infrastructure

Throughout the infection chain, the operator leverages its **own infrastructure** comprising dedicated IP addresses and domains. The primary function of this infrastructure is to **receive victim fingerprints** transmitted via HTTP headers. Depending on the specific stage of the infection chain, these servers are also configured to **deliver VBScript payloads** , provide**updated network configuration URLs** , or **act as exfiltration endpoint** for documents harvested by GammaSteel.

For example, **we mapped the deployment of new hosts** between 16 January and 28 January 2026. During this period, 55 new servers were provisioned. The average operational lifespan of these hosts is approximately 24 hours, with the exception of two IP that remained active for nearly the entire period, and who do not appear to behave any differently from others. This high-frequency rotation demonstrates that **Gamaredon possesses a resilient distributed infrastructure and the capability to rapidly provision new hosts.** The deployment pattern, typically yielding between three and eight new servers every 48 hours, strongly suggests **an automation** and a focus on **operational persistence**.

To compare the infrastructure actively provisioned by the operator against the servers explicitly tasked within the infection chain, **we analysed the daily volume of unique hosts** distributed via the previously mentioned Mastodon account during the same period. These servers are designated to be used by **GammaSteel as C2 or exfiltration endpoint**. A total of **61 new servers were created**. This equates to a consistent deployment rate of **four new servers per day** , reinforcing our previous assessment that the operator's infrastructure pipeline is automated. Consequently, we assess that **newly deployed servers are immediately operationalised** and integrated into this campaign.

## Obfuscation, anti-analysis and persistence made-in FSB

Gamaredon’s operations are characterized by **an industrial-scale effort** to evade detection and **maintain long-term access**. The volume of noise generated both within the local system code and across network deployments demonstrates an **advanced understanding of defensive mechanisms**. This infection chain is explicitly designed for anti-analysis, exhausting defenders through complexity and evasion rather than relying on sophisticated zero-day exploits.

A defining characteristic of this campaign is its overwhelming reliance on VBScript. Without the stealer written in PowerShell, GammaPhish, GammaWorm, GammaLoad are coded in VBScript using native Windows COM API. **The execution flow operates much like a Russian matryoshka doll.** When local storage becomes necessary, the operator injects VBScript functions into ADS attached to standard user profiles or temporary directories. There are currently very few popular analysis frameworks dedicated to VBScript execution and **we assess that Gamaredon intentionally developed this infection chain in VBScript to blind sandboxes and slow manual reverse-engineering**.

To further complicate triage, Gamaredon deploys obfuscation designing every component to blend into the background noise of a standard Windows environment. Every function we analyzed features constant variants from previous online investigations; variables change, logic structures are slightly shifted, and hardcoded noise is randomized, **making it difficult to track the chain's evolution**. The in-memory VBScript payloads often exceed 20,000 lines, heavily padded with dynamically generated junk code and fake variables to break static signatures and disrupt dynamic analysis.

Beyond script obfuscation, **Gamaredon has weaponized the Windows registry**. GammaLoad continuously updates and reads the registry to store live network configurations, caching DDR outputs and staging or C2 servers to ensure the infection loop never breaks. The registry also literally hosts GammaSteel, including its 71 distinct PowerShell functions directly within the `HKCU\Printers\` key. In a major shift in TTPs, **Gamaredon uses the Windows DPAPI** to encrypt these registry-staged functions. By using the `ConvertTo-SecureString` method without a specified key, the encryption is tied strictly to the user’s active session. Notably, **this TTP strongly overlaps with the historical behaviors of the InvisiMole intrusion-set in 2020** , an FSB-linked operator previously observed cooperating with Gamaredon, as detailed by ESET in their report [InvisiMole: The Hidden Part of the Story](https://web-assets.esetstatic.com/wls/2020/06/ESET_InvisiMole.pdf). Finally, this complex staging is complemented by an **opportunistic backdoor capability** built into the communication flow. At almost **every network interaction step** , whether a loader querying a DDR or for every file that are exfiltrated in the stealer with its fallback C2, it parses the HTTP response and executes it blindly if it contains VBScript code. This ensures the operator retains the ability to **push arbitrary remote code execution** at any point during the infection lifecycle, allowing them to **deploy new payloads on the fly** or potentially **troubleshoot the system** if the exfiltration pipeline breaks.

## Conclusion

In this long-term campaign, Gamaredon continues its relentless focus on Ukrainian targets, particularly government entities. The infection chain is **resilient, massive and highly likely to be reused** and evolved in the coming months thanks to its highly obfuscated, modular design.

This operation marks a technical step up over Gamaredon's previously documented attacks. The transition to a nearly entirely fileless, **VBScript-driven "matryoshka" architecture** combined with the heavy abuse of **NTFS Alternate Data Streams (ADS)** , demonstrates a concerted effort to bypass automated sandboxes and exhaust defenders. Furthermore, we observed novel evasion methods, most notably the weaponization of the Windows Registry to stage a PowerShell stealer. The use of the **Windows Data Protection API (DPAPI)** to securely encrypt these payloads directly within the registry is a technique never before seen in Gamaredon’s activity. This specific capability strongly **overlaps with the historical TTPs of the FSB-linked InvisiMole intrusion-set** , suggesting a potential sharing of tools or operational methodologies between Russian state-sponsored actors.

To maximize its espionage capabilities, the stealer orchestrates three concurrent listening mechanisms targeting data across all three distinct states:

  * at rest (via hourly drive exploration)
  * in transit (via the USB drive monitoring)
  * and in use (via the real-time file surveillance)



This multi-layered architecture effectively eliminates operational blind spots and provides significant redundancy. This transforms the infected host into a persistent listening device, actively **leaking high-value intelligence regardless of the storage medium**.

Gamaredon’s operational flexibility is further highlighted by its **automated and diversified infrastructure**. By blending legitimate cloud services, such as Supabase and Tebi.io, with public Dead Drop Resolvers, the operators ensure an unbreakable command and control loop. Combined with the backdoor capability allowing the arbitrary execution of VBScript from almost every HTTP response, **Gamaredon maintains control over compromised hosts** , enabling them to update configurations or deploy new payloads on the fly.

Gamaredon now wields a hardened, industrial-scale toolset that **abuses native Windows features** and **legitimate public infrastructure** to evade detection and **maintain long-term espionage operations**. 

This report is the final one in this series of three reports on Gamaredon. Sekoia.io’s TDR team will continue to track this campaign closely and enhance our detections to anticipate its next evolutions.

## IOCs

The URLs below represent a subset of the hundreds of IOCs identified during this investigation. Complete IOCs list, including network indicators (IPs, C2 infrastructure, URLs and domains) is available via the [**Sekoia Intelligence feed**](https://app.sekoia.io/objects) and to **Sekoia Defend** customers.

We welcome peer-to-peer collaboration. If you are an analyst tracking this intrusion-set and wish to exchange data, please contact us at **tdr[at]sekoia.io**.

### GammaSteel

Hash-based IOCs are not provided for the x71 PowerShell functions because their names vary dynamically, and the plaintext code is encrypted at rest using DPAPI, only to be decrypted on-the-fly when called by GammaSteel.

#### DDR

hxxps://api.telegra[.]ph/getPage/Hello-01-23-161

hxxps://write[.]as/api/posts/1nei1af6dnw8q

hxxps://rentry[.]co/hwzrmfkx

hxxps://mastodon[.]social/api/v1/statuses/115942411657067215

#### **Operator-controlled exfiltration hosts**

justsstop[.]ru

165.22.170[.]129