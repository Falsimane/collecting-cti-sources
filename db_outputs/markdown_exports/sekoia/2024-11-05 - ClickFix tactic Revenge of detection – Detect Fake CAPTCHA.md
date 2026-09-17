# ClickFix tactic: Revenge of detection – Detect Fake CAPTCHA

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/clickfix-tactic-revenge-of-detection
- **Date :** 2024-11-05

---

_This report on ClickFix was originally published for our customers on 22 October 2024._

## Context

In May 2024, a new social engineering tactic called ClickFix emerged, featuring a ClearFake cluster that the Sekoia Threat Detection & Research (TDR) team closely monitored and analysed in a private report. This tactic involves displaying fake error messages in web browsers to deceive users into copying and executing a given malicious PowerShell code, finally infecting their systems.

The previous blog post '"[ClickFix tactic: The Phantom Meet](/blog/clickfix-tactic-the-phantom-meet)" outlines the ClickFix cluster, which leverages fake video conferencing pages (such as Google Meet or Zoom) to distribute infostealers. A private report released shortly after, describes a larger cluster that uses fake CAPTCHAs pages for the same purpose.

In this blog post, we delve into the various infection chains and highlight detection opportunities based on the available data sources in addition to threat intelligence.

## ClickFix principle

Regardless of the template used (Google Meet, Captcha, etc.), the infection process is consistent. The user is guided through a series of steps that ultimately compromise their machine. The sequence of events is as follows:

  1. The user is instructed from the web page to press "Windows + R", a keyboard shortcut to open the Run command dialog box;
  2. Press "Ctrl + V" to paste a malicious command previously copied from the clipboard via JavaScript function; 
  3. Press “Enter” to execute the command, mainly PowerShell or Mshta, which is designed to download and run a payload.



From the workstation’s perspective, using the "Windows + R" shortcut ensures that the process executing the malicious command runs under Explorer.exe as its parent process. This makes the activity appear more legitimate, and from the attacker's perspective, reducing the risk of detection.

The infection chains may vary, but three main scenarios emerge: one targeting macOS and two affecting Windows.

  * For macOS, clicking the "fix it" button triggers the direct download and execution of malware - in this case, Amos Stealer -) in the form of a .dmg file.
  * On the Windows side, the infection chains differ depending on the ClickFix cluster being used, whether it's through fake meeting pages (e.g., Phantom Meet) or deceptive CAPTCHAs. Each cluster utilizes a distinct approach to deliver its payload. In the first scenario, the infection chain starts with the execution of a malicious **mshta** command. In the second scenario, **PowerShell** is used to initiate the infection process.



![ClickFix infection routine](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58b12f236c0e864f4e2_6a92a2395538c880c252feb8_6a2a7e7186e50b3f6152d26c.webp)

ClickFix infection routine

 _Figure 1. ClickFix infection routine_

## Phantom Meet case

We discovered several websites masquerading as the homepage of a Google Meet video conference. The sites displayed pop-up windows falsely indicating problems with the microphone and headset, as shown on the figure below.

![ClickFix cluster masquerading Google Meet video conference displaying a pop-up faking technical issues](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58b12f236c0e864f4e5_6a92a23832517fc4025f8ae0_6a2a7e7186e50b3f6152d269.webp)

ClickFix cluster masquerading Google Meet video conference displaying a pop-up faking technical issues

 _Figure 2. ClickFix cluster masquerading Google Meet video conference displaying a pop-up faking technical issues_

In this instance, as outlined in our previous blog post, the command copied from ClickFix executes a VBScript. This is achieved through an HTML Application embedded in an HTML page, which is downloaded by mshta.exe. The VBScript performs the following actions:

  1. Terminates its parent process (mshta.exe).
  2. Downloads executables using bitsadmin.exe.
  3. Retrieves the victim's public IP address using the api.ipify[.]org service and sends this, along with the execution status, to the C2 server.



The resulting process tree is particularly noticeable and serves as a strong indicator of compromise.

### Behavioural detection - Endpoint

  * ProcessTree detection



A quick win is to detect PowerShell or bitsadmin processes where the parent process is mshta.exe and the command line contains a URL.

`detection:  
selection:  
process.parent.name: 'mshta.exe'  
process.parent.command_line|contains:   
- 'http://'  
- 'https://'  
process.name:   
- 'bistadmin.exe'  
- 'timeout.exe'  
- 'cmd.exe'  
condition: selection  
`

In the rule above, the selection criteria are deliberately strict to correspond to the ClickFix phantom case scenario. However, it would be beneficial to detect a wider list of child processes, including powershell.exe or rundll32.exe.

  * Bitsadmin



**bitsadmin.exe** is a command-line tool used to manage Background Intelligent Transfer Service (BITS) jobs in Windows. BITS is a service designed for asynchronous, prioritised, and throttled file transfers, which allows large files to be downloaded or uploaded in the background without interrupting the user's network experience.

Threat actors have abused bitsadmin.exe for malicious purposes such as downloading malware. Its use is part of a broader strategy in which attackers leverage legitimate Windows tools, a technique referred to as "living off the land”, to avoid detection by traditional security systems.

Bitsadmin is commonly used for legitimate purposes, such as distributing software updates. However, in the ClickFix case, the command line exhibits distinctive patterns of misuse. These include saving the malicious payload in the user's AppData Temp directory, a behaviour often associated with threat activity.

`detection:  
selection:  
process.name: 'bitsadmin.exe'  
process.command_line|contains|all:   
- 'http'  
- 'transfert'  
- 'download'  
- 'AppData'  
- 'Temp'  
condition: selection  
`

### Network

The previous detection method relies on detailed monitoring of workstations through a Sysmon agent or EDR (Endpoint Detection and Response), which may not always be available. Alternatively, telemetry might be limited to process execution data. In such cases, it can be helpful to correlate with other data sources, such as network logs (firewall or proxy).

In this scenario, network activity serves as a strong indicator of compromise. From a network perspective, the infection chain unfolds as follows:

  * mshta.exe accesses a specific URL. When mshta.exe makes a web request, it typically uses a default User-Agent string that corresponds to the version of Internet Explorer installed on the system, as mshta.exe relies on the same underlying rendering engine.
  * Bitsadmin is then used to download two malicious binaries.
  * Finally, Wscript, using WinHttpRequest, retrieves the victim's public IP address and transmits it to the command-and-control (C2) server.



Each of these binaries initiates a web request within a short time frame, using a distinct UserAgent. This pattern of behaviour can be detected through correlation rules based on the sequence and timing of these network events.

`name: mshta  
detection:  
selection:  
source.ip: '*'  
user.agent|startswith: 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT'   
condition: selection   
---  
name: bits  
detection:  
selection:  
source.ip: '*'  
user.agent|startswith: 'Microsoft BITS'   
condition: selection  
---   
name: wscript  
detection:  
selection:  
source.ip: '*'  
ua:  
user.agent|contains: 'WinHttp.WinHttpRequest'  
lookup:  
sekoiaio.any_tag: 'iplookup'  
condition: selection and (ua or lookup)  
---   
action: correlation  
type: temporal  
rule:   
- mshta  
- bits  
- wscript  
group-by:  
- source.ip  
timespan: 5m  
ordered: false  
`

 _N.B._ : In this rule, the **sekoiaio.any_tag** field is used in conjunction with the lookup value. During indexing, Sekoia XDR automatically enriches specific fields, such as domain names or IP addresses, using data from its threat intelligence database. This enables the addition of the lookup tag to events when a resolution or connection to a domain linked to tools that reveal a public IP address—such as the **api.ipify** site—is detected. If such fields are unavailable, the rule can also filter based on a list of URLs.

As an alternative to the previous rule, the file MIME type could be used as the primary criterion. Data sources such as proxies and firewalls can reveal this kind of information. In this case, MIME type offers a valuable detection method by identifying machines that first access an application/hta file (triggered by mshta.exe) and shortly afterward download a binary using bitsadmin. However, this detection method requires network devices capable of providing MIME type information and inspecting TLS traffic, as ClickFix primarily uses HTTPS URLs, which encrypt the traffic and hide such details without decryption capabilities.

## CAPTCHAs case

One significant delivery chain for fake reCAPTCHA pages leverages GitHub's widespread use among developers. As detailed in a report by [McAfee](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/behind-the-captcha-a-clever-gateway-of-malware/), on 18 September 2024, threat actors have exploited GitHub's trusted environment by creating numerous issues that falsely claimed a security vulnerability. These issues may have tricked developers into engaging with what appears to be a standard troubleshooting process.

We identified another delivery chain for the fake CAPTCHA ClickFix tactic that involves intricate redirection sequences, particularly from dubious websites providing cracked software or film streaming. Users navigating on these sites are often redirected through a series of domains that lead to promoted websites, which may include online shops, surveys or malicious websites, such as these fake reCAPTCHA pages that open in a new tab.

![ClickFix cluster masquerading as a Google reCAPTACHA and displaying verification steps to infect users](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58b12f236c0e864f4eb_6a92a2375538c880c252fe05_6a2a7e7186e50b3f6152d266.webp)

ClickFix cluster masquerading as a Google reCAPTACHA and displaying verification steps to infect users

 _Figure 3. ClickFix cluster masquerading as a Google reCAPTACHA and displaying verificationsteps to infect users_

On both case, the command copied from ClickFix page is a straight forward PowerShell script, containing only two instructions:

  * **Invoke-Expression** (alias IEX) to execute the downloaded payload.
  * **Invoke-WebRequest** (alias IWR) to download the payload.



It is worth noting that the command line can be encoded in base64. 

The simplicity of the command line, combined with the frequent use of IWR and IEX commands, makes detection challenging. A rule based solely on these keywords or their base64-encoded equivalents, would likely generate numerous false positives in most organisational environments.

### ClickFix behavioural detection - Endpoint

While detecting the PowerShell command line alone without generating false positives is challenging, it is possible to identify this threat by analysing the operation of the script typically involves the following actions:

  1. **Connecting to a website** : A PowerShell process with a command line containing IWR, IEX (or their aliases or base64-encoded versions) that connects to an IP address over a port associated with web traffic or through an enterprise proxy.
  2. **Remote instructions:** The PowerShell command line accesses this website to download a ZIP archive, save it to the machine, extract its contents, and execute the binary contained within.



![remote instruction exec by powershell](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58c12f236c0e864f4ee_6a92a235dae089660dfbf7c8_6a2a7e7086e50b3f6152d25c.webp)

remote instruction exec by powershell

 _figure 4: remote instruction exec by powershell_

  1. **Saving a file on the machine** : The PowerShell command line saves a ZIP file in the user AppData Temp folder. After decompression, the command line command also saves the decompressed files (DLL, EXE) in this folder.
  2. **Executing the payload** : Finally, the command line executes the payload from the user's AppData directory.



The retrieval of instructions from a third-party website is not always consistent; in some cases, the archive is downloaded directly. However, this does not alter the overall sequence of actions.

By using Sigma correlation, this behaviour can be detected by creating individual detection rules for each action (network connection, file saving, and binary execution) and correlating them based on the hostname and PID on a 5 minutes time frame.

`name: network  
detection:  
selection:  
event.type: '*'  
destination.ip: '*'  
process.pid: '*'  
process.name: 'powershell.exe'  
cmd1:  
process.command_line|contains:  
- 'iex'  
- 'iwr'  
- 'Invoke-WebRequest'  
- 'Invoke-Expression'  
cmd2:  
process.command_line|wide|base64offset|contains:  
- 'iex'  
- 'iwr'  
- 'Invoke-WebRequest'  
- 'Invoke-Expression'  
filters1:  
process.command_line|contains:  
- '.ps1'  
- 'chocolatey'   
condition: selection and (cmd1 or cmd2) and not filters1  
---  
name: file  
detection:  
selection:  
event.type: '*'  
file.path: '*'  
process.pid: '*'  
process.name: 'powershell.exe'  
file.extension:   
- 'exe'  
- 'dll'  
- 'zip'  
cmd1:  
process.command_line|contains:  
- 'iex'  
- 'iwr'  
- 'Invoke-WebRequest'  
- 'Invoke-Expression'  
cmd2:  
process.command_line|wide|base64offset|contains:  
- 'iex'  
- 'iwr'  
- 'Invoke-WebRequest'  
- 'Invoke-Expression'  
filters1:  
process.command_line|contains:  
- '.ps1'  
- 'chocolatey'   
condition: selection and (cmd1 or cmd2) and not filters1  
---   
name: exec  
detection:  
selection:  
event.type: '*'  
process.parent.pid: '*'  
process.parent.name: 'powershell.exe'  
process.command_line|contains:  
- 'appdata'  
- 'temp'  
condition: selection  
---   
action: correlation  
type: temporal  
rule:   
- network  
- file  
- exec  
aliases:  
correlpid:  
network:  
- process.pid  
file:  
- process.pid  
exec:  
- process.parent.pid  
group-by:  
- host.name  
- correlpid  
timespan: 5m  
ordered: true  
`

 _N.B._ : 

  *  _Filters are primarily added to limit the number of events that need to be aggregated._
  * _An alias is needed to link the PID of the PowerShell process to the PID of the parent process that executes the binary._



### ClickFix behavioural detection - Multisource

As explained in section 2.2, the above rules are based on endpoint logs, which are not systematically available. In such cases, it can be helpful to correlate with other data sources, such as network logs from a firewall or proxy.

Following this logic, the first step is to identify PowerShell network activity by filtering based on its User-Agent. To reduce the risk of false positives, additional filters can be applied for websites returning status codes in the 2xx or 3xx range and specific HTTP methods could be added to focus on the functional infection chain. If the network equipment supports it (such as through TLS inspection), it may also be helpful to filter by MIME type, retaining only binary or compressed files. The second step is to detect suspicious processes with PowerShell as the parent process. These two sets of data can then be correlated by common factors, such as the machine’s IP address.

`name: network  
detection:  
selection:  
source.ip: '*'  
user_agent.original|contains: 'WindowsPowerShell'  
http.response.status_code|startswith:  
- '2'  
- '3'  
http.request.method:  
- 'CONNECT'  
- 'GET'  
condition: selection  
---  
name: exec  
detection:  
selection:  
event.type: '*'  
host.ip: '*'  
process.parent.name: 'powershell.exe'  
process.command_line|contains:  
- 'appdata'  
- 'temp'  
condition: selection  
---   
action: correlation  
type: temporal  
rule:   
- network  
- exec  
aliases:  
asset:  
network:  
- source.ip  
exec:  
- host.ip  
group-by:  
- asset  
timespan: 5m  
ordered: true  
`

The field used to group selections may vary in name depending on the data source. To address this, aliases are employed to create a temporary field, allowing selections to be grouped by a shared value.

### Hunting web access

Without endpoint telemetry, detecting a ClickFix compromise becomes more challenging. However, given the nature of its operation, the ClickFix scenario—where PowerShell fetches instructions from a third-party site and then downloads a payload—can still be identified through network logs, as demonstrated in the illustration :

![Log extract of PowerShell connection taken as part of a ClickFix compromise](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a58b12f236c0e864f4e8_6a92a236693fca262e1ad57e_6a2a7e7086e50b3f6152d260.webp)

Log extract of PowerShell connection taken as part of a ClickFix compromise

 _figure 5: log extract of PowerShell connection_

The behaviour is often distinct:

  1. The first transaction retrieves the instructions, which consist of only a few lines of code, resulting in low data volume.
  2. The second transaction, however, is larger, as it involves downloading the payload.



Both requests occur within a short time frame and originate from the same machine.

`name: web1  
detection:  
selection:  
source.ip: '*'  
user_agent.original|contains: 'WindowsPowerShell'  
http.response.status_code|startswith:  
- '2'  
- '3'  
http.response.bytes|lte: 6500  
http.request.method:  
- 'GET'  
- 'CONNECT'  
condition: selection  
---  
name: web2  
detection:  
selection:  
source.ip: '*'  
user_agent.original|contains: 'WindowsPowerShell'  
http.response.status_code|startswith:  
- '2'  
- '3'  
http.response.bytes|gte: 20000000  
http.request.method:  
- 'GET'  
- 'CONNECT'  
condition: selection  
---  
action: correlation  
type: temporal  
rule:  
- web1  
- web2  
group-by:  
source.ip  
user_agent.original  
timespan: 1m  
ordered: true  
`

However, threat hunting can still be conducted using network logs from firewalls or proxies. A focus on monitoring network connections initiated by PowerShell, especially those involving low-prevalence domains or suspicious Top Level Domains (TLDs) can be worthwhile. It may also be valuable to search for connections to domain names that resemble Google or Zoom but are not associated with these companies. The low frequency of these domains can serve as a useful indicator for identifying fraudulent ones.

## Conclusion

ClickFix is an **emerging social engineering** tactic first identified by [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn) in March 2024, used by the initial access broker **TA571** in email phishing campaigns. As of September 2024, **several intrusion sets already adopted it** to widely distribute malware through email [phishing campaigns](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers), compromised websites, and distribution infrastructures. CERT UA recently [issued a report](https://cert.gov.ua/article/6281123) attributing an infection chain to **APT28** that employs the ClickFix tactic.

Most of the rules proposed in this blog post report are highly customized. In contrast, the rules developed by TDR and integrated into Sekoia XDR are broader in scope and more MITRE technique-oriented. XDR customers will not find these specific rules in the catalog, but they have access to many other rules that effectively detect various techniques employed by ClickFix. Combining these detection techniques with threat intelligence strengthens defence mechanisms against these sophisticated social engineering techniques.

As this technique is evolving, Sekoia analysts will continue to track this delivery infrastructure and develop our detection capabilities to mitigate the risks associated with this threat.