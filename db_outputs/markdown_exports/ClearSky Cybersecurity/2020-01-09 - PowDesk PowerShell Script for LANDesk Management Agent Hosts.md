# PowDesk: PowerShell Script for LANDesk Management Agent Hosts

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/powdesk/
- **Date :** 2020-01-09

---

PowDesk is a simple PowerShell-based script for hosts that run LANDesk Management Agent.   
This script is compatible with both 32-bit and 64-bit systems and exfiltrates the computer’s name through a PHP page stored at a certain domain name. After analyzing the script behavior, we assess that potential attackers might create a whitelist of companies that use LANDesk management software.

### **File Analysis**

The sample has been uploaded and scanned to Virus Total repository for the first time on December 13th, 2019 from the US through an API account, and was detected as malicious by 26 AntiVirus vendors:

![](https://www.clearskysec.com/wp-content/uploads/2020/01/vt-powdesk-550x178.jpg)

**File name** : CBA8REINSTALL[1].EXE  
**File type** : Win32 EXE  
**File size** : 66.50 KB  
**Creation date** : 21/01/2017

**MD5** : 2de2e528991ac2d85aa8f12fce5351ad  
**SHA-1** : 7e14e661a577e7cb502717e9570c6651932ab4b8  
**SHA-256** : 8406ca490c60ec41569b35f31f1860ff4663bba44d1daac64760ecdfe694203d

After the initial executable’s run, a PowerShell file is dropped in the %TEMP% folder. At every run of the initial file, the PowerShell file will be dropped under a different name which contains a combination of four random capital letters and numbers, and consequentially with a different hash value. 

The PowerShell script was initially uploaded to VirusTotal on December 23th and no engines detected the file as malicious:

![](https://www.clearskysec.com/wp-content/uploads/2020/01/vt-powdesk-clear-550x264.jpg)

However, a day afterward, three engines detected the script as malicious:

![](https://www.clearskysec.com/wp-content/uploads/2020/01/vt-powdesk-2-550x276.jpg)

PowDesk contains a validation mechanism of the end station. The results of the check are sent to a certain domain name. The checks performed with this mechanism might be used to verify companies that use the LANDesk Management Agent. Below you can see the PowDesk run command:

![](https://www.clearskysec.com/wp-content/uploads/2020/01/Powershell-550x38.jpg) [![](https://www.clearskysec.com/wp-content/uploads/2020/01/code-powdesk-1-e1578587317107.jpg)](https://www.clearskysec.com/wp-content/uploads/2020/01/PowDesk-full-code.png)PowDesk malware source code

The first assigned variables defined in the PowerShell code are “$ld32” and “$ld64”. The values given to those variables are the Program Files’ folders, according to the system’s version (32-bit or 64-bit). The folder name in both is “LANDesk”. After that, a number of functions are activated:

#### **The “Send-Results” function**

[![](https://www.clearskysec.com/wp-content/uploads/2020/01/Send-Result-Powdesk.png)](https://www.clearskysec.com/wp-content/uploads/2020/01/Send-Result-Powdesk.png)

This function checks whether a service named “cba8” exists and is active on the attacked computer and checks if the LANDesk folder exists at the destination defined in the aforementioned variables. After those checks, the results are sent to the C&C server with predefined answers affixed to the attacked computer’s name. The results are sent with an HTTP request to a URI at lcepos[.]com, following this pattern:

> **hXXp://lcepos[.]com/php/reclaimlandesk[.]php?devicename=$name &result=$result**

The predefined answers appear to filter out the targets that don’t have the LANDesk Agent installed. The following table details the answers:

**Predefined answer** | **Meaning**  
---|---  
Result = Su**c** essful | The LANDesk Agent is installed at the station. Note the typo.   
Result = Failed | The “cba8” service stopped.   
Result = Missing CBA8 | The “cba8” service doesn’t exist. In the source code, the last condition checks whether the service under that name is absent, but there is a LANDesk Agent executable; if the condition is true, a service named “cba8” is created.   
Result = Missing LANDesk Agent | The infected end station doesn’t have LANDesk installed – an answer designed to filter infected targets which are not valuable for further infection.   
  
During our investigation, we tried to bypass those verification mechanisms, however, the C&C server has denied communication in the lab environment anyway. We assess that the attackers have created at the server a whitelist of IP ranges of the attacked companies, or with low probability, of specific computers’ names.

![](https://www.clearskysec.com/wp-content/uploads/2020/01/WireShark-Powdesk.png)Screenshot from WireShark which documents the C&C communication ![](https://www.clearskysec.com/wp-content/uploads/2020/01/CC-answers-page.png)C&C answer’s page

Further in the source code, one can see a condition whereas if LANDesk’s folder indeed exists on the attacked computer at the defined location, four variables will be defined, which we assess to belong to legitimate components[3] of the LANDesk Agent system and will be used later in the process.

[![](https://www.clearskysec.com/wp-content/uploads/2020/01/Send-Result-Powdesk-If.png.jpg)](https://www.clearskysec.com/wp-content/uploads/2020/01/Send-Result-Powdesk-If.png.jpg)Defining the variables $exe, $Invscan, $reg, $pol which update the system components’ place

#### **The “Start-LDProcesses” function**

[![](https://www.clearskysec.com/wp-content/uploads/2020/01/Start-LDProcesses.jpg)](https://www.clearskysec.com/wp-content/uploads/2020/01/Start-LDProcesses.jpg)

At the first stage, the function looks for two processes that should exist in the infected environment – sdclient and vulscan – and stops them. The “sdclient”[[4]](https://www.clearskysec.com/wp-admin/post.php?post=3226&action=edit#_ftn3) process enables the administration interface to run an inventory scan or vulnerability scan at the end station.

After that, the function activates the “brokerconfig.exe”[5] process with the command “/r”, which asks for a certificate from a cloud-based administration server of LANDesk Management Suite. 

Next, the “ldiscn32.exe”[6] process will be activated with the commands “/sync” and “/noui”, to synchronize with the system’s database. The “/noui” command is responsible for carrying out the actions in the background, without the user’s notice.

Finally, the “policysync.exe”[7] process, responsible for rules’ synchronization, will run.

#### **Malware activation mechanism**

[![](https://www.clearskysec.com/wp-content/uploads/2020/01/Get-Service-cba8.jpg)](https://www.clearskysec.com/wp-content/uploads/2020/01/Get-Service-cba8.jpg)

At the bottom of the PowerShell file, one can find the main checks which verify the run status of the “cba8” service, which belongs to the LANDesk Management Agent.

First, a check whether the “cba8” service’s status is “running”. If so, the “Send-Results” function is activated to update the attacker’s C&C server.

If the service is not “running”, the file will activate it and the “Start-LDProcesses” function too.

If the service is not present on the attacked system at all, the “residentAgent.exe”[8[9](https://www.clearskysec.com/wp-admin/post.php?post=3226&action=edit#_ftn9)[]](https://www.clearskysec.com/wp-admin/post.php?post=3226&action=edit#_ftn9) process will be activated with the “/register” command, which will install the LANDesk Management Agent Service. Then “cba8” will be activated, along with relevant system processes.

### **Attribution** – Update 26/01/2020

After we received a request from Ivanti, we checked again our attribution and we now believe that this script does not point to APT groups. We cannot verify in this stage who uploaded this script, or whether it can be used by malicious threat actor.

### IOCs

SHA-256:

  * 8406ca490c60ec41569b35f31f1860ff4663bba44d1daac64760ecdfe694203d



Domain:

  * lcepos[.]com



URL:

  * hxxp://lcepos[.]com/php/reclaimlandesk[.]php?devicename=$name&result=$result



**A list of IOCs is available below and on PassiveTotal. For subscribers of the ClearSky threat intelligence service, MISP event number 1834.**

* * *

[3] <https://forums.ivanti.com/s/article/List-of-Executables-and-Services-run-on-Client>

[4]  <https://forums.ivanti.com/s/article/About-SDCLIENT-based-communications>

[5] <https://forums.ivanti.com/s/article/About-switches-for-Brokerconfig?t=1557417319926>

[6] <https://forums.ivanti.com/s/article/About-Inventory-Scanner-Switches>

[7] <https://forums.ivanti.com/s/article/About-PolicySync-exe-Switches>

[8] <https://forums.ivanti.com/s/article/How-to-manually-install-and-remove-LANDesk-services>