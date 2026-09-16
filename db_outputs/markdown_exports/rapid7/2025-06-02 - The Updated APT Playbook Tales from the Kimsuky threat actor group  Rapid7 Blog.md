# The Updated APT Playbook: Tales from the Kimsuky threat actor group | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/03/20/the-updated-apt-playbook-tales-from-the-kimsuky-threat-actor-group/
- **Date :** 2025-06-02

---

_Co-authors are Christiaan Beek and Raj Samani_

Within [Rapid7 Labs](/research/) we continually track and monitor threat groups. This is one of our key areas of focus as we work to ensure that our ability to protect customers remains constant. As part of this process, we routinely identify evolving tactics from threat groups in what is an unceasing game of cat and mouse.

Our team recently ran across some interesting activity that we believe is the work of the [Kimsuky](https://attack.mitre.org/groups/G0094/) threat actor group, also known as Black Banshee or Thallium. Originating from North Korea and active since at least 2012, Kimsuky focuses primarily on intelligence gathering. The group is known to have targeted South Korean government entities, individuals associated with the Korean peninsula's unification process, and global experts in various fields relevant to the regime's interests. In recent years, Kimsuky’s activity has also expanded across the APAC region to impact Japan, Vietnam, Thailand, etc.

Through our research, we saw an updated playbook that underscores Kimsuky’s efforts to bypass modern security measures. Their evolution in tactics, techniques, and procedures (TTPs) underscores the dynamic nature of cyber espionage and the continuous arms race between threat actors and defenders.

In this blog we will detail new techniques that we have observed used by this actor group over the recent months. We believe that sharing these evolving techniques gives defenders the latest insights into measures required to protect their assets.

### Anatomy of the Attack

Let’s begin by highlighting where we started our analysis of Kimsuky and how the more we investigated, the more we discovered — to the point where we believe we observed a new wave of attacks by this actor.

Following the identification of the target, typically we would anticipate the reconnaissance phase to initiate in an effort to identify methods to allow access into the target. Since Kimsuky’s focus is intelligence gathering, gaining access needs to remain undetected; subsequently, the intrusion is intended to not trigger alerts.

Over the years, we have observed a change in this group’s methods, starting with weaponized Office documents, ISO files, and beginning last year, the abuse of shortcut files (LNK files). By disguising these LNK files as benign documents or files, attackers trick users into executing them. PowerShell commands, or even full binaries, are hidden in the LNK files — all hidden for the end-user who doesn’t detect this at the surface.

Our latest findings lead us to observations that we believe are Kimsuky using CHM files which are delivered in several ways, as part of an ISO|VHD|ZIP or RAR file. The reason they would use this approach is that such containers have the ability to pass the first line of defense and then the CHM file will be executed.

CHM files, or Compiled HTML Help files, are a proprietary format for online help files developed by Microsoft. They contain a collection of HTML pages and a table of contents, index, and full text search capability. Essentially, CHM files are used to display help documentation in a structured, navigable format. They are compiled using the Microsoft HTML Help Workshop and can include text, images, and hyperlinks, similar to web pages, but are packaged as a single compressed file with a .chm extension.

While originally designed for help documentation, CHM files have also been exploited for malicious purposes, such as distributing malware, because they can execute JavaScript when opened. CHM files are a small archive that can be extracted with unzipping tools to extract the content of the CHM file for analysis.

The first scenario in our analysis can be visualized as follows:

![Screenshot-2024-03-18-at-4.33.59-PM.png](https://www.rapid7.com/cdn/images/bltbd84a37854c9b93d/683de84318a55305cb6872c6/Screenshot-2024-03-18-at-4.33.59-PM.png)

### The Nuclear Lure

While tracking activity, we first discovered a CHM file that triggered our attention.

Hash| Value  
---|---  
MD5| 364d4fdf430477222fe854b3cd5b6d40  
SHA1| b5224224fdbabdea53a91a96e9f816c6f9a8708c  
SHA256| c62677543eeb50e0def44fc75009a7748cdbedd0a3ccf62f50d7f219f6a5aa05  
  
Analyzing this file in a controlled environment, we observe that the CHM file contains the following files and structure:

![Screenshot-2024-03-18-at-4.40.44-PM.png](https://www.rapid7.com/cdn/images/blt69c167c958591812/683de85e3a1c5a4c7c4baade/Screenshot-2024-03-18-at-4.40.44-PM.png)

The language of the filenames is Korean. With the help of translation software, here are the file names:

  * North Korea's nuclear strategy revealed in 'Legalization of Nuclear Forces'.html
  * Incomplete.html
  * Factors and types of North Korea’s use of nuclear weapons.html
  * North Korean nuclear crisis escalation model and determinants of nuclear use.html
  * Introduction.html
  * Previous research review.html
  * Research background and purpose.html



These HTML files are linked towards the main HTML file ‘home.html’ — we will return later to this file.

Each filetype has its unique characteristics, and from the area of file forensics let’s have a look at the header of the file:

![Screenshot-2024-03-19-at-10.50.01-AM.png](https://www.rapid7.com/cdn/images/bltbbc788c0f9e1619b/683de8772cfe324783dc1895/Screenshot-2024-03-19-at-10.50.01-AM.png)

Value| Value| Comment  
---|---|---  
0x49545346| ITSF| File header ID for CHM files  
0x03| 3| Version Number  
\---| \---| \---  
skip| |   
\---| \---| \---  
0x1204| 0412| Windows Language ID  
\---| \---| \---  
  
The value 0412 as a language ID is “Korean - Korea”. This can be translated to mean the Windows operating system that was used to create this CHM file was using the Korean language.

When the CHM file is executed, it will showcase the following:

![Screenshot-2024-03-19-at-10.51.10-AM.png](https://www.rapid7.com/cdn/images/blt9ed3c336c5bdfe6d/683de89173c845b036e8c56d/Screenshot-2024-03-19-at-10.51.10-AM.png)

The page in the right pane is the ‘home.html’ file. This page contains an interesting piece of code:

![Screenshot-2024-03-19-at-10.51.47-AM.png](https://www.rapid7.com/cdn/images/blt29dd4d54eab35948/683de8a6e3c8aae58d831001/Screenshot-2024-03-19-at-10.51.47-AM.png) ![Screenshot-2024-03-19-at-10.52.06-AM.png](https://www.rapid7.com/cdn/images/blt54ce9a3ed889d674/683de8bc18a5533d7b6872e6/Screenshot-2024-03-19-at-10.52.06-AM.png)

The provided code snippet is an example of using HTML and ActiveX to execute arbitrary commands on a Windows machine, typically for malicious purposes. The value assigned to a ‘Button’ contains a command line with Base64 code in it as another obfuscation technique and is followed by a living-off-the-land technique, thereby creating persistence on the victim’s system to run the content.

Let’s break it up and understand what the actor is doing:

  1. **Base64 Encoded VBScript Execution (T1059.003)** :


  * _**echo T24gRXJyb3IgUmVzdW1lIE5leHQ...:**___ This part echoes a Base64-encoded string into a file. The string, when decoded, is VBScript code. The VBScript is designed to be executed on the victim's machine. The decoded Base64 value is:

![Screenshot-2024-03-19-at-10.53.57-AM.png](https://www.rapid7.com/cdn/images/blt60bc86c14f1b6ae7/683de8d3237ea6f1b391c496/Screenshot-2024-03-19-at-10.53.57-AM.png)

**2\. Saving to a .dat File** :

  * **_> "%USERPROFILE%\Links\MXFhejJ3c3gzZWRjA.dat":_** The echoed Base64 string is redirected and saved into a .dat file within the current user's Links directory. The filename seems randomly generated or obfuscated to avoid easy detection.



**3\. Decoding the .dat File** :

  * _**start /MIN certutil -decode "%USERPROFILE%\Links\MXFhejJ3c3gzZWRjA.dat" "%USERPROFILE%\Links\MXFhejJ3c3gzZWRjA.vbs"**_ : This uses the certutil utility, a legitimate Windows tool, to decode the Base64-encoded .dat file back into a .vbs (VBScript) file. The /MIN flag starts the process minimized to reduce suspicion.



**4\. Persistence via Registry Modification (T1547.001)**

  * _**:start /MIN REG ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Document /t REG_SZ /d "%USERPROFILE%\Links\MXFhejJ3c3gzZWRjA.vbs" /f**_ _:_ This adds a new entry to the Windows Registry under the Run key for the current user (HKCU stands for HKEY_CURRENT_USER). This registry path is used by Windows to determine which programs should run automatically at startup. The command ensures that the decoded VBScript runs every time the user logs in, achieving persistence on the infected system.



But what is downloaded from the URL, decoded and written to that VBS file? The URL of the Command and Control Server is hosting an HTML page that contains VBS code:

![Screenshot-2024-03-19-at-10.57.43-AM.png](https://www.rapid7.com/cdn/images/blt42c9f7537fe6ea7a/683de8e8ca9dfc2ce25268d2/Screenshot-2024-03-19-at-10.57.43-AM.png)

Analyzing the code, it does several things on the victim’s machine:

![Screenshot-2024-03-19-at-2.54.06-PM.png](https://www.rapid7.com/cdn/images/bltfef3dc5d72c35a85/683de8fcbc38b1722f477f6f/Screenshot-2024-03-19-at-2.54.06-PM.png)

The function ‘SyInf()’ collects basic system information using WMI (Windows Management Instrumentation) and constructs a string with all these details. What is gathered:

  * Computer name, owner, manufacturer, model, system type.
  * Operating system details, version, build number, total visible memory.
  * Processor details, including caption and clock speed.



Other functions in the code collect the running processes on the system, recent Word files, and lists directories and files of specific folders. In our case, the actor was interested in the content of the Downloads folder.

After gathering the requested information from the code, it is all encoded in the Base64 format, stored in the file ‘info.txt’ and exfiltrated to the remote server:

ui = "00701111.000webhostapp.com/wp-extra"

Once the information is sent, the C2 responds with the following message:

![Screenshot-2024-03-19-at-2.55.56-PM.png](https://www.rapid7.com/cdn/images/blt02b5d1525221c49c/683de90f4b2b7fc249e163cd/Screenshot-2024-03-19-at-2.55.56-PM.png)

This C2 server is still active and while we have seen activity since September 2023, we also observed activity in 2024.

### New Campaign Discovered

Pivoting some of the unique strings in the ‘stealer code’ and hunting for more CHM files, we discovered more files — some also going back to H2 2023, but also 2024 hits.

In VirusTotal we discovered the following file:

Hash| Value  
---|---  
MD5| 71db2ae9c36403cec1fd38864d64f239  
SHA1| 5c7b2705155023e6e438399d895d30bf924e0547  
SHA256| e8000ddfddbe120b5f2fb3677abbad901615d1abd01a0de204fade5d2dd5ad0d  
\-------------| \-------------------  
  
The file is a VBS script and it contains similar code to what we described earlier on the information gathering script above. Many components are the same, with small differences in what type of data is being gathered.

The biggest difference, which makes sense, is a different C2 server. Below is the full path of when the VBS script ran and concatenated the path:

_hxxp://gosiweb.gosiclass[.]com/m/gnu/convert/html/com/list.php?query=6_

The modus operandi and reusing of code and tools are showing that the threat actor is actively using and refining/reshaping its techniques and tactics to gather intelligence from victims.

### Still More? Yes, Another Approach Discovered

Using the characteristics of the earlier discovered CHM files, we developed internal Yara rules that were hunting, from which we discovered the following CHM file:

Hash| Value  
---|---  
MD5| f35b05779e9538cec363ca37ab38e287  
SHA1| d4fa57f9c9e35222a8cacddc79055c1d76907fb9  
SHA256| da79eea1198a1a10e2ffd50fd949521632d8f252fb1aadb57a45218482b9fd89  
\----| \---  
  
In this particular case, multiple .bat files and VBS scripts are present:

![Screenshot-2024-03-19-at-3.00.15-PM.png](https://www.rapid7.com/cdn/images/blt61ef21cf733e8011/683de92330073ee90eeb1ae2/Screenshot-2024-03-19-at-3.00.15-PM.png)

In similar fashion, an HTML file in the directory contains hidden code:

![Screenshot-2024-03-19-at-3.00.55-PM.png](https://www.rapid7.com/cdn/images/blta593498e741ec3a9/683de9382cfe32eaaadc18e1/Screenshot-2024-03-19-at-3.00.55-PM.png)

_style="visibility:hidden;" ><param name="Command" value="ShortCut"><param name="Button" value="Bitmap:shortcut"><param name="Item1" value=",hh,-decompile C:\\\Users\\\Public\\\Libraries '+d+'_

The background png file shows (translated) the following information:

![Screenshot-2024-03-19-at-3.02.12-PM.png](https://www.rapid7.com/cdn/images/blt04e224339e9024e7/683de94d543b8d04acbf1460/Screenshot-2024-03-19-at-3.02.12-PM.png)

Once the CHM file is executed, it drops all files in the _C:\\\Users\\\Public\\\Libraries\_ directory __ and starts running. It starts with creating a persistence scheduled task with the “\2034923.bat” file:

![Screenshot-2024-03-19-at-3.03.30-PM.png](https://www.rapid7.com/cdn/images/bltc786209cb637c7c1/683de95f30073ee006eb1af4/Screenshot-2024-03-19-at-3.03.30-PM.png)

The VBS script will create a Service and then the other .bat files are executed, each with different functions.

The “9583423.bat” script will gather information from the system and store them in text files:

![Screenshot-2024-03-19-at-3.04.15-PM.png](https://www.rapid7.com/cdn/images/blt6636e3a799a17b7a/683de96f4c5a09849e5e0de1/Screenshot-2024-03-19-at-3.04.15-PM.png)

In the above code, when information is gathered, the file is called by the ‘1295049.bat’ script, which contains the Powershell code to setup the connection to the C2 server with the right path, Base64 encode the stream, and transfer:

![Screenshot-2024-03-19-at-3.06.02-PM.png](https://www.rapid7.com/cdn/images/blt45f6564321dd8a9a/683de97e2cfe321e6edc1912/Screenshot-2024-03-19-at-3.06.02-PM.png)

Combining the code from previous .bat file and this code, the path to the C2 is created:

hxxps://niscarea[.]com/in.php?cn=[base64]&fn=[DateTime]

The gathered files containing the information about the system will be Base64 encoded, zipped and sent to the C2. After sending, the files are deleted from the local system.

![Screenshot-2024-03-19-at-3.07.16-PM.png](https://www.rapid7.com/cdn/images/blt589f77a2157ae4b9/683de98f4b2b7fa84de16403/Screenshot-2024-03-19-at-3.07.16-PM.png)

The sys.txt file will contain information about the system of the victim such as OS, CPU architecture, etc. Here is a short example of the content:

![Screenshot-2024-03-19-at-3.07.54-PM.png](https://www.rapid7.com/cdn/images/blt5c2ac8a3c1853ff8/683de9a4ca9dfcecaa526900/Screenshot-2024-03-19-at-3.07.54-PM.png)

The overall flow of this attack can be simplified in this visualization:

![Screenshot-2024-03-19-at-3.08.36-PM.png](https://www.rapid7.com/cdn/images/blt6f3e4b9d99d18837/683de9b63d7b5e58a7136936/Screenshot-2024-03-19-at-3.08.36-PM.png)

### Attack Prevalence

Since this is an active campaign, tracking prevalence is based at the time of this writing. However, Rapid7 Labs telemetry enables us to confirm that we have identified targeted attacks against entities based in South Korea. Moreover, as we apply our approach to determine attribution such as the overlap in code and tactics, we have attributed this campaign with a moderate confidence* to the Kimsuky group.

All IoCs are available freely within our [Rapid7 Labs repository here](https://github.com/rapid7/Rapid7-Labs/tree/main/IOCs).

### Rapid7 Customers

InsightIDR and Managed Detection and Response (MDR) customers have existing detection coverage through Rapid7's expansive library of detection rules. Rapid7 recommends installing the Insight Agent on all applicable hosts to ensure visibility into suspicious processes and proper detection coverage. Below is a non-exhaustive list of detections deployed and alerting on activity related to these techniques and research:

Persistence - Run Key Added by Reg.exe

Suspicious Process - HH.exe Spawns Child Process

Suspicious Process - CHM File Runs CMD.exe to Run Certutil

Persistence - vbs Script Added to Registry Run Key

 _*In threat research terms, “moderate confidence” means that we have a significant amount of evidence that the activity we are observing is similar to what we have observed from a specific group or actor in the past; however, there is always a chance someone is mimicking behavior. Hence, we use “moderate” instead of “high” confidence._  


## Article tags

  * [Research](/blog/tag/research/)