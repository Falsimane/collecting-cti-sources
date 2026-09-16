# Recruitment Phishing Scam Imitates Hiring Process | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/recruitment-phishing-scam-imitates-crowdstrike-hiring-process/
- **Date :** January 08, 2025

---

# Recruitment Phishing Scam Imitates CrowdStrike Hiring Process

## A newly discovered phishing campaign uses CrowdStrike recruitment branding to convince victims to download a fake application, which serves as a downloader for the XMRig cryptominer.

January 08, 2025

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


On January 7, 2025, CrowdStrike identified a phishing campaign exploiting its recruitment branding to deliver malware disguised as an "employee CRM application." The attack begins with a phishing email impersonating CrowdStrike recruitment, directing recipients to a malicious website. Victims are prompted to download and run a fake application, which serves as a downloader for the cryptominer _XMRig_. 

## How the Scam Works 

The phishing email lures victims by claiming to be part of a recruitment process (Figure 1). It links to a malicious website offering download options for both Windows and macOS (Figure 2). However, regardless of the option selected, a Windows executable written in Rust is downloaded. This executable functions as a downloader for _XMRig_.

![Figure 1. Initial phishing email](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-RecruitmentPhish-1?wid=1106&hei=976&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 1. Initial phishing email

![Figure 2. Impersonated malicious phishing site containing download links for fake “CRM application”](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-RecruitmentPhish-2?wid=1600&hei=888&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 2. Impersonated malicious phishing site containing download links for fake “CRM application”

The downloaded executable performs several environment checks to evade detection and analysis before downloading additional payloads. These checks include: 

  * Detecting if a debugger is attached to the process using the IsDebuggerPresent Windows API 
  * Ensuring the system has a minimum number of active processes 
  * Verifying that the CPU has at least two cores 
  * Scanning the list of running processes for common malware analysis or virtualization software tools, avoiding execution in sandboxed or monitored environments 



If these checks are passed, the executable displays a fake error message pop-up before continuing.

![Figure 3. Fake error message following evasion checks](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-RecruitmentPhish-3?wid=400&hei=245&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Figure 3. Fake error message following evasion checks

Once the basic environment checks are completed and the fake error message is displayed, the executable proceeds to download a text file from the URL:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code1.png)

This file contains configuration information for _XMRig_ in the form of command-line arguments that can be appended to a call to the _XMRig_ miner executable.

The executable then downloads a copy of _XMRig_ from GitHub, from the URL:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code2.png)

The downloaded ZIP file is saved to the following path:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code3.png)

The executable extracts the contents of the ZIP file into the %TEMP%\System\ directory and copies the main _XMRig_ executable to the path:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code4.png)

The malware then runs the _XMRig_ miner, using the command-line arguments inside the downloaded configuration text file:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code5.png)

The executable establishes persistence via the following methods:

  * Drops a Windows batch script to the Start Menu Startup directory, at this path:




![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code6.png)

This batch script executes a dropped copy of the downloaded miner, located at:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code7.png)

The contents of the batch script are the following:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code8.png)

  * The batch script writes a new Windows Registry logon autostart key, located at:



![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code9.png)

This logon autostart entry executes a dropped copy of the original malicious downloader, located at:

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2025/01/Blog-RecruitmentPhish-Code10.png)

## Stay Alert to Stay Safe

This campaign highlights the importance of vigilance against phishing scams, particularly those targeting job seekers. Individuals in the recruitment process should verify the authenticity of CrowdStrike communications and avoid downloading unsolicited files. Organizations can reduce the risk of such attacks by educating employees on phishing tactics, monitoring for suspicious network traffic and employing endpoint protection solutions to detect and block malicious activity.

Outside of this campaign, we are aware of scams involving false offers of employment with CrowdStrike. Fraudulent interviews and job offers use fake websites, email addresses, group chats and text messages. We do not interview prospective candidates via instant message or group chat, nor do we require candidates to purchase products or services, or process payments on our behalf, as a condition of any employment offer. And, in reference to the campaign detailed above, we do not ask candidates to download software for interviews.

Those interested in applying for a role at CrowdStrike should navigate to our [Careers page](https://www.crowdstrike.com/en-us/careers/) to learn about our job openings and begin our official application process. To verify the authenticity of CrowdStrike recruitment communications, please reach out to recruiting@crowdstrike.com.

## Indicators of Compromise

The phishing site, cscrm-hiring[.]com, serves as the base for the attack, hosting the malicious executable and directing victims to download the fake CRM application. The malware establishes its presence by executing in the background, using minimal CPU resources to avoid detection. Key indicators include specific file paths, registry entries and network communication.

### Network Indicators

**Indicator**| **Description**  
---|---  
`cscrm-hiring[.]com`| Domain of phishing site  
`https[:]//cscrm-hiring[.]com/cs-applicant-crm-installer[.]zip`| URL serving malicious executable  
`93.115.172[.]41`| IP used for Threat Actor Pool and data  
`http[:]//93.115.172[.]41/private/aW5zdHJ1Y3Rpb25zCg==.txt`| Text data containing XMRig parameters  
`93.115.172[.]41:1300`| Mining Pool hosted by threat actor  
  
### Host Indicators

**Indicator**| **Description**  
---|---  
`96558bd6be9bcd8d25aed03b996db893ed7563cf10304dffe6423905772bbfa1`| SHA-256 hash of ZIP file containing fake CRM application executable  
`62f3a21db99bcd45371ca4845c7296af81ce3ff6f0adcaee3f1698317dd4898b`| SHA-256 hash of fake CRM application executable  
`7c370211602fcb54bc988c40feeb3c45ce249a8ac5f063b2eb5410a42adcc030`| SHA-256 hash of downloaded XMRig configuration text file  
`%TEMP%\System\temp.zip`| Path to downloaded ZIP file containing XMRig  
`%TEMP%\System\process.exe`| Path to persistent copy of XMRig  
`%LOCALAPPDATA%\System32\config.exe`| Path to persistent copy of fake CRM application executable  
`%LOCALAPPDATA%\System32\process.exe`| Path to persistent copy of XMRig  
`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Maintenance\info.txt`| Path to text file created by fake CRM application executable  
`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\startup.bat`| Path to persistent Batch file  
`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\config`| Registry path of persistent Autorun entry  
  
## Learn More

For additional information on CrowdStrike’s in-depth research and real-time access to indicators of compromise (IOCs) like the ones featured in this blog, visit the CrowdStrike [Counter Adversary Operations website](https://www.crowdstrike.com/platform/threat-intelligence/).  


#### Additional Resources

  * _Read about the adversaries tracked by CrowdStrike Counter Adversary Operations in the[CrowdStrike 2024 Threat Hunting Report](https://www.crowdstrike.com/resources/reports/threat-hunting-report/)._
  * _Tune into the[Adversary Universe podcast](https://www.crowdstrike.com/resources/adversary-universe-podcast/), where CrowdStrike experts discuss today's threat actors — who they are, what they’re after and how you can defend against them. _
  *  _Know the adversaries that may be targeting your region or business sector — explore the[CrowdStrike Adversary Universe®](https://www.crowdstrike.com/en-us/adversaries/)._
  * _Learn how CrowdStrike's[threat intelligence and threat hunting solutions](https://www.crowdstrike.com/platform/threat-intelligence/) are transforming security operations to better protect your business. _



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)