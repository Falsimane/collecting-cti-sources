# Exploring the (Not So) Secret Code of Black Hunt Ransomware | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/02/05/exploring-the-not-so-secret-code-of-blackhunt-ransomware-2/
- **Date :** 2025-06-02

---

### 

It seems like every week, the cybersecurity landscape sees the emergence of yet another ransomware variant, with Black Hunt being one of the latest additions. [Initially](https://twitter.com/RakeshKrish12/status/1597839380558716928) reported by cybersecurity researchers in 2022, this new threat has quickly made its presence known. In a recent incident, Black Hunt ransomware wreaked havoc by compromising around 300 companies in Paraguay.

Rapid7 Labs consistently monitors emerging threats, and this new ransomware variant caught our attention for several reasons. The behavior and potential impact of this new variant raised concerns among our team, prompting us to conduct a thorough analysis to better understand its capabilities and potential risks.

During our analysis we found notable similarities between Black Hunt ransomware and LockBit, which suggested that it uses leaked code of Lockbit. In addition, it uses some techniques similar to REvil ransomware.

### Technical Analysis

In this analysis we examined the Black Hunt sample shared on X (formerly Twitter), by [MalwareHunterTeam](https://twitter.com/malwrhunterteam/status/1744499152011104549). In our investigation we found some interesting techniques and features used by this malware. The recent Black Hunt sample is a C++ executable, which widely reuses the leaked Lockbit ransomware code and shares similarities with several other recently spotted ransomware families.The execution of the ransomware on an infected machine starts with a check for a file named Vaccine.txt under directory C:\ProgramData path

![Screenshot-2024-02-05-at-10.29.13-AM.png](https://www.rapid7.com/cdn/images/blt46c4778d12bbfa07/683ddd776b437b11e14fa51c/Screenshot-2024-02-05-at-10.29.13-AM.png)

If the file is found, malware terminates its execution. This file detection acts as an anti-exploitation flag for the ransomware. As this is not a well-known anti-sandbox/anti-VM technique, we assume that this file is in use by the threat actor (TA) itself. It is either created by the victim which is instructed to create it after the ransom is paid or dropped by the decryptor, if one is sent to the victim to decrypt the [encrypted data](/fundamentals/data-encryption/). Adding that check is logical if the ransomware operators consider scenarios where their persistence mechanism and the ransomware binary remain on the system even after the ransom is paid and files are decrypted. Moreover, the fact that all files dropped by the ransomware are placed in the C:\ProgramData directory further supports our assessment that this file is associated with the Black Hunt operation.

Next, the malware adjusts the following privileges to processes Access Token by using the `AdjustTokenPrivileges` API function:

Privilege Setting| Description  
---|---  
SeDebugPrivilege| Monitor and manipulate other processes.  
SeRestorePrivilege| Bypass file system security to restore files.  
SeBackupPrivilege| Read any file, regardless of permissions.  
SeTakeOwnershipPrivilege| Take control of critical system resources.  
SeAuditPrivilege| Manipulate security audit logs.  
SeSecurityPrivilege| Modify security settings of objects.  
SeIncreaseBasePriorityPrivilege| Gives service privilege to increase scheduling priority.  
  
After modifying process privileges, the malware hides its window by invoking the `ShowWindow` function with the `nCmdShow` parameter set to 0, which corresponds to `SW_HIDE`. This action ensures that the malware's window is not visible to the user, allowing it to operate stealthily in the background without drawing attention.

![Screenshot-2024-02-05-at-10.31.02-AM.png](https://www.rapid7.com/cdn/images/blt98f24b149eefa0ab/683ddd9d70aa95ddb5fe2f8d/Screenshot-2024-02-05-at-10.31.02-AM.png)

The execution flow continues as the malware invokes the `GetCommandLineW` function. This function retrieves the command-line string for the current process, including the program name and any arguments passed during startup. This function is commonly used by malware and helps to gather information about command-line flags. Following this, another function call is made to `CMD_ARGS`.

![Screenshot-2024-02-05-at-10.31.40-AM.png](https://www.rapid7.com/cdn/images/bltb227b89df644908c/683dddc23323a570c080a811/Screenshot-2024-02-05-at-10.31.40-AM.png)

The function processes a command-line string and checks if any of the following arguments were passed:

Argument| Description  
---|---  
-local| If passed, the ransomware will skip shared or network drives encryption.  
-network| If passed, the ransomware will encrypt only the network drives  
-biggame| If passed, the ransomware will only encrypt the files that contain .4dd, .4dl, .accdb, .accdc, .accde, .accdr, .accdt, .accft, .adb, .ade, .adf, .adp, .arc, .ora, .alf, .ask, .btr, .bdf, .cat, .cdb, .ckp, .cma, .cpd, .dacpac, .dad, .dadiagrams, .daschema, .db, .db-shm, .db-wal, .db3, .dbc, .dbf, .dbs, .dbt ,.dbv, .dbx, .dcb, .dct, .dcx, .ddl ,.dlis, .dp1 ,.dqy, .dsk, .dsn, .dtsx, .dxl, .eco, .ecx, .edb, .epim, .exb, .fcd, .fdb, .fic, .fmp, .fmp12, .fmpsl, .fol, .fp3, .fp4, .fp5, .fp7, .fpt, .frm, .gdb, .grdb, .gwi, .hdb, .his, .ib, .idb, .ihx, .itdb, .itw, .jet, .jtx, .kdb, .kexi, .kexic, .kexis, .lgc, .lwx, .maf, .maq, .mar, .mas, .mav, .mdb, .mdf, .mpd, .mrg, .mud, .mwb, .myd, .ndf, .nnt, .nrmlib, .ns2, .ns3, .ns4, .nsf, .nv, .nv2, .nwdb, .nyf, .odb, .oqy, .orx, .owc, .p96, .p97, .pan, .pdb, .pdm, .pnz, .qry, .qvd, .rbf, .rctd, .rod, .rodx, .rpd, .rsd, .sas7bdat, .sbf, .scx, .sdb, .sdc, .sdf, .sis, .spq, .sql, .sqlite, .sqlite3, .sqlitedb, .te, .temx, .tmd, .tps, .trc, .trm, .udb, .udl, .usr, .v12, .vis, .vpd, .vvv, .wdb, .wmdb, .wrk, .xdb, .xld, .xmlff, .abcddb, .abs, .abx, .accdw, .adn, .db2, .fm5, .hjt, .icg, .icr, .kdb, .lut, .maw, .mdn, .mdt extensions.  
-backup| If passed, the ransomware will only encrypt the files with .000, .cab, .zip and .rar extensions.  
-noencrypt| if passed, the malware will skip encryption.  
-p| If passed, specifies a path to be encrypted  
-nologs| If passed - If the flag is not set, the ransomware creates a log file named #BlackHunt_Logs.txt under C:\ProgramData directory. Otherwise no log files will be created.  
-status| If passed, sets the ransomware console windows to ‘SW_SHOW’ and shows the encryption status in the ransomware console window. The status information contains the System ID, running time, the amount of encrypted files and encrypted volume, as well as errors, alive workers and the code location. The status window constantly updated by the ransomware as long as it runs  
-update| If passed, the ransomware shows a fake Window Update screen  
-kill| If passed, the ransomware terminates processes from hardcoded process list and stops services from hardcoded service list  
-scanner| If passed, the ransomware scans for network shares  
-cipher| If passed, when all the encryption process is completed the ransomware uses Windows tool Cipher.exe on all drives to overwrite the deleted data. Same capability was utilized by Vohuk ransomware.  
-restart| if set in the end of encryption the following command will be executed to restart the pc ‘shutdown /r /t 15 /f’  
  
The ransomware accepts additional arguments that modify its behavior, including disabling spreading capabilities, adjusting encryption speed, thread count for encryption, skipping mutex creation, and enabling debug mode to collect more information in the log file.

After verifying passed arguments and ensuring the absence of the -nomutex flag, the ransomware proceeds to create a `BLACK_HUNT_MUTEX`. Next, it elevates its process priority to `HIGH_PRIORITY_CLASS` using the `SetPriorityClass` API function.

The ransomware made 200 attempts to load `Fake.dll`, likely as a tactic to slow up/evade the execution in the sandbox. Following this, it employs the `IsDebuggerPresent` API call to detect if debugging is in progress. If a debugger is detected, the ransomware terminates.

Further analysis revealed that Black Hunt maintains a whitelist of 15 countries, as detailed in the table below.

Language Code| Language| Country  
---|---|---  
2092| Azeri (Cyrillic)| Azerbaijan  
1068| Azeri (Latin)| Azerbaijan  
1067| Armenian| Armenia  
1059| Belarusian| Belarus  
1079| Georgian| Georgia  
1071| Macedonian| North Macedonia  
1088| Kyrgyz| Kyrgyzstan  
2073| Moldovan| Moldova (Russian language)  
1064| Tajik (Cyrillic)| Tajikistan  
1090| Turkmen| Turkmenistan  
2115| Uzbek (Cyrillic)| Uzbekistan  
1091| Uzbek (Latin)| Uzbekistan  
1058| Ukrainian| Ukraine  
1065| Persian| Iran  
1055| Turkish| Turkey  
  
The malware uses the `GetSystemDefaultUILanguage` function to identify one of 15 hardcoded languages. If it detects any of these languages, it terminates execution.

![Screenshot-2024-02-05-at-10.36.10-AM.png](https://www.rapid7.com/cdn/images/bltd5f9a0f4f28d0a5e/683ddde8ca9dfc0a8d5265d6/Screenshot-2024-02-05-at-10.36.10-AM.png)

Following language detection, the malware attempts to establish an internet connection by calling the `getaddrinfo` function to resolve the domain ip-api.com.

The ransomware checks if `BlackKeys` mutex exists, and if not, it creates it by using `CreateMutexA` API.

Next,the malware begins a key initialization process. First, it attempts to load a key by using `CryptImportKey` with a buffer containing the key. It looks for the key in files named C:\ProgramData\\#BlackHunt_Public.key and C:\ProgramData\\#BlackHunt_Private.key, and also verifies the presence of C:\ProgramData\\#BlackHunt_ID.txt. If the key loading fails, the malware switches to generating a 128-bit RSA key pair.

After initializing encryption keys, the ransomware creates a HKEY_LOCAL_MACHINE\Software\Classes\\.Hunt2 registry key to define settings for files with `.Hunt2` extension.It adds a `DefaultIcon` registry key under `.Hunt2` and assigns a default value to the dropped icon file.

Next, the ransomware creates a new {2C5F9FCC-F266-43F6-838DAE269E11} value under HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run registry key and sets it data to C:\ProgramData\\#BlackHunt_ReadMe.hta that will make the `.hta` file be executed on reboot.This file is a Black Hunt ransom note. Here we can notice additional proof of reuse of Lockbit ransomware code by BlackHunt operators, the value name is identical to the one LockBit 2.0 used in their attacks. 

The Black Hunt ransomware makes several modifications to the Windows registry to disable security measures, alter system functionality, and potentially limit user control over the system. Below are the commands used

Command| Action  
---|---  
/c reg add "HKEY_LOCAL_MACHINE\Software\Classes.Hunt2" /f"| Adds a registry key .Hunt2 under HKEY_LOCAL_MACHINE\Software\Classes\  
/c reg add "HKEY_LOCAL_MACHINE\Software\Classes.Hunt2\DefaultIcon" /ve /t REG_SZ /d   
"C:\ProgramData#BlackHunt_Icon.ico" /f");| Sets the default icon for .Hunt2 files to C:\ProgramData#BlackHunt_Icon.ico  
/c reg add "HKEY_LOCAL_MACHINE\Software\Classes\Hunt2" /f");| Adds a registry key Hunt2 under HKEY_LOCAL_MACHINE\Software\Classes\  
/c reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run" /v| Adds an entry to the Windows startup registry key to run C:\ProgramData#BlackHunt_ReadMe.hta  
/c reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run"   
/v "{2C5F9FCC-F266-43F6-BFD7-838DAE269E11}"   
/t REG_SZ /d "C:\ProgramData#BlackHunt_ReadMe.hta" /f");| Adds an entry to the Windows startup registry key to run C:\ProgramData#BlackHunt_ReadMe.hta  
SHChangeNotify(0x8000000, 0, 0, 0);| Notifies the system of changes that might require refreshing icons or interface elements  
  
The list of modified registries can be found in the IOC section or on the Rapid7 Labs GitHub page.

Afterward, the malware checks for various command-line arguments, and its execution flow depends on which arguments are set.

`-p` flag

If set, it proceeds to sets persistence by creating scheduled tasks to execute the malware upon system startup using the command /c SCHTASKS.exe /Create /RU "NT AUTHORITY\SYSTEM" /sc onstart /TN "Windows Critical Update" /TR "%s" /F.

`-safemode` flag 

If it is, the malware configures the safe mode setting to ensure its execution after the system boots in safe mode, after which it restarts the machine. For more information on that technique check the Safe Mode section of this article. 

If the `-safemode` flag is not set, the malware creates ransom note, primary and secondary contact emails `[[email protected]](/cdn-cgi/l/email-protection)` and `[[email protected]](/cdn-cgi/l/email-protection)`, respectively, a placeholder ID for infected machines, and the Tor address http[:]//sdif9821kjsdvcjlksaf2kjhlksvvnktyoiasuc921f. 

`-update` flag 

If set, the malware drops `#BlackHunt_Update.hta` to the C:\ProgramData directory and executes it. The purpose of that flag is to create a fake Windows Update screen while encrypting the victim's data. After that, the malware empties the recycle bin by calling `SHEmptyRecycleBinW`.

`-kill` flag

If set, the malware enumerates running processes and terminates 130 predefined processes and services. The full list of processes and services can be found in the IOC section or on the Rapid7 Labs GitHub page.

After completing its service termination routine, the malware tries to access the registry key SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System, known for storing system policies such as User Account Control (UAC) settings. If successful, it modifies two registry values: `EnableLUA` and `EnableLinkedConnections`.

![Screenshot-2024-02-05-at-10.39.57-AM.png](https://www.rapid7.com/cdn/images/blt450ba0ae37c8f857/683dde133beff0698ca7c363/Screenshot-2024-02-05-at-10.39.57-AM.png)

By setting`EnableLUA` to 0, the malware effectively disables this security feature, granting itself elevated privileges without user intervention. Additionally, the malware sets the `EnableLinkedConnections` registry key, allowing any user to see network drives that were mapped for other users. This gives ransomware the ability to gain access to sensitive network resources.The malware invokes the `RefreshPolicyEx` API function to enforce the modifications made.

Next, the malware manipulates shadow storage. For conventional disk types, such as DRIVE_FIXED, it executes commands like /c vssadmin resize shadowstorage /for=C:\ /on=C:\ /maxsize=401MB. For disk types not explicitly specified, such as DRIVE_RAMDISK, it uses /c vssadmin resize shadowstorage /for=C:\ /on=C:\ 

Afterwards , the malware removes the shadow copies using vssadmin.exe Delete Shadows /all /quiet and disables automatic repair by executing bcdedit /set {default} recoveryenabled No.

![Screenshot-2024-02-05-at-10.40.33-AM.png](https://www.rapid7.com/cdn/images/bltd53bb15134648337/683dde422cfe32adffdc1596/Screenshot-2024-02-05-at-10.40.33-AM.png)

Next, the attackers execute a sequence of commands to clean up the system and implement critical modifications.

Command| Description  
---|---  
bcdedit /set {default} bootstatuspolicy IgnoreAllFailures| Adjusts boot status policy for normal booting despite failures, blocking access to System Image Recovery  
fsutil.exe usn deletejournal /disks (D and C)| Deletes Volume USN Journal on disks D and C, disrupting file system change tracking  
wbadmin.exe delete catalog -quiet| Silently removes backup catalogs, erasing backup data  
Disables System Restore tasks with sc| Halts System Restore functionality, limiting recovery options  
  
If the `-scanner` flag is set the ransomware will attempt to retrieve the ARP cache table and scan the addresses using the servername as a parameter. This function utilizes `NetShareEnum` to gather information about network shares on a given server.

Finally, the encryption routine starts. Encrypted files renamed with `.Hunt2` extension. After the encryption, the ransomware deletes itself, and the ransom note is displayed to the user.

![Screenshot-2024-02-05-at-10.41.36-AM.png](https://www.rapid7.com/cdn/images/blt955e885f3d64cc45/683dde742cfe32f223dc15a6/Screenshot-2024-02-05-at-10.41.36-AM.png)

### Additional functionality

**Spreading mechanism**

Ransomware tries to enumerate shares on the localhost (127.0.0.1) using `NetShareEnum`. If shares are found and no error occurs, the malware tries to process drive paths. It checks each path for specific conditions met and that the path is not a remote path. If these conditions are met, it processes the argument as a local drive path by extracting the drive letter and formatting it as \127.0.0.1{drive_letter}. 

The malware attempts to locate a NAS server and paths to files on removable drives. Additionally, it searches for shared folders and attempts to spread by enumerating local shared folders using `NetShareEnum`. If a network share is found, it copies itself to the share using `CopyFileW`. After spreading, it clears setup event logs by executing cmd /c wevtutil.exe.

Safe mode

If the `-safemode` argument is set, the malware executes the encryption process in Safe Mode. To ensure execution after rebooting in Safe Mode, the malware sets up the system as follows:

1) Obtains a user environment variable.

2) Executes the net user username `Black_Hunt_2.0` command to set a new user password.

3) Adds a new `AutoAdminLog` value under the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon and sets it to 1, enabling auto login in Windows.

4) Creates a `DefaultUserName` value under the same registry key and sets it.

5) Creates a `DefaultPassword` registry value and sets it to the changed password.

6) Executes the /c bootcfg /raw /a /safeboot:network /id 1 and /c bcdedit /set {current} safeboot network commands to force the computer to boot into Safe Mode with Networking.

7) Creates a new`BackToNormal` value under HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce and sets it to bcdedit /deletevalue {current} safeboot" /f.

8) Sets an additional value under the `RunOnce` key named `BlackHunt` and sets it to the current malware running path.

9) Finally, restarts the system by executing shutdown /r /t 7 /f

**Rapid7 Customers**

For Rapid7 MDR and InsightIDR customers, the following Attacker Behavior Analytics (ABA) rules are currently deployed and alerting on the activity described in this blog:

  * Suspicious Process - Delete File Shadow Copies With PowerShell
  * Attacker Technique - Rundll32 Running DLL in Root of ProgramData
  * Suspicious Process - Regsvr32.exe Registering DLL in ProgramData
  * Persistence - Run Key Added by Reg.exe
  * Suspicious Registry Event - Unusual Registry Run Keys
  * Attacker Technique - Disabling UAC Remote Restrictions
  * Suspicious Registry Edit - Shell\Open\Command Edited, Possible UAC Bypass
  * Attacker Technique - Reg.exe disabling the User Access Control (UAC) remote restriction
  * Suspicious Process - Possible UAC Bypass via MMC.exe
  * Attacker Technique - Svchost.exe Spawns cmd.exe Executing Scheduled Task
  * Persistence - SchTasks Creating A Task Pointed At Users Temp Or Roaming Directory
  * Ransomware - LockBit Command-Line Arguments
  * Suspicious Process - VSSADMIN List and Create Shadow Commands (MVD detection)
  * Suspicious Registry Event - BCDEDIT Safeboot Minimal
  * UAC Bypass - Notepad Launching CMD or PowerShell
  * Defense Evasion - Disabling Multiple Security or Backup Products (MVD detection)
  * Suspicious Process - Diskshadow (Windows Server) Delete Shadow Copies
  * Attack technique - Creation of Suspicious Files Associated with BalckHunt Ransomware
  * Attack Technique: Registry Modification by Black Hunt Ransomware



### MITRE ATT&CK Techniques

|

Tactic| Technique| **Details  
---|---|---  
Execution| Native API (T1106)| The ransomware may execute its malicious activities by interacting with system APIs.  
| |   
Persistence| Scheduled Task/Job: Scheduled Task (T1053.005 )| Black Hunt sets persistence by creating scheduled tasks to execute the malware upon system startup using the command  
Persistence| Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder (T1547.001)| Modifies the Windows Registry to establish persistence, ensuring it runs automatically upon system startup.  
Privilege Escalation| Abuse Elevation Control Mechanism: Bypass User Account Control (T1548.002 )| Black Hunt grants itself elevated privileges without user intervention by modifying registry values: EnableLUA and EnableLinkedConnections.  
Defense Evasion, Privilege Escalation| Access Token Manipulation (T1134)| Black Hunt manipulate access tokens, granting itself privileges to perform various actions on the system  
Defense Evasion| Modify Registry (T1112)| Modifies registry keys to disable security features, alter system configurations, and establish persistence.  
Defense Evasion| Impair Defenses: Disable or Modify Tools (T1562.001)| Black Hunt disables security tools to avoid possible detection of their malware/tools and activities  
Defense Evasion| File Deletion ( T1070.004 )| Black Hunt empties the Windows Recycle Bin to permanently delete files and prevent recovery attempts.  
Defense Evasion| Indicator Removal on Host: Clear Windows Event Logs (T1070.001)| The ransomware clears Windows Event Logs to erase evidence.  
Defense Evasion| Impair Defenses: Safe Mode Boot (T1562.009)| Black Hunt disable endpoint defenses  
Defense Evasion| Hide Artifacts: Hidden Window (T1564.003)| Black Hunt uses a hidden window to conceal malicious activity from the plain sight of users.  
Discovery| Network Service Discovery (T1046)| Black Hunt lists services running on the local network  
Discovery| System Location Discovery: System Language Discovery (T1614.001)| Black Hunt gather information about the system language of a host in order to infer the geographical location of that host  
Discovery| Network Share Discovery (T1135)| Black Hunt enumerates shared network drives and folders to access other systems  
Discovery| File and Directory Discovery (T1083)| Black Hunt enumerates files and directories to identify whether certain objects should be encrypted  
Discovery| Process Discovery (T1057)| Black Hunt performs process discovery/enumeration to terminate processes that could interfere with the encryption process.  
Impact| Inhibit System Recovery (T1490)| Deletes backups, volume shadow copies, and disables automatic repair and recovery features.  
Impact| Data Encrypted for Impact (T1486)| Black Hunt is capable for encrypting victim’s files  
Impact| Service Stop (T1489)| Stops certain services, such as those related to backup, security software, and others  
  
### IOCs

Attribute| Value| Description  
---|---|---  
mutex| BLACK_HUNT| Mutex used by the ransomware  
mutex| BaseNamedObjects\BlackKeys| Mutex used by the ransomware  
sha256| C25F7B30D224D999CE337A13224C1CDE9FFB3F415D7113548DE9914A1BB3F123| #BlackHunt_Update.hta file  
primary email| Teikobest@gmail dot com| Primary contact email for ransom  
secondary email| Loxoclash@gmail dot com| Secondary contact email for ransom  
Tor address| http[://]sdif9821kjsdvcjlksaf2kjhlksvvnktyoiasuc921f|   
sha256| 74df3452a6b9dcdba658af7a9cf5afb09cce51534f9bc63079827bf73075243b| Black Hunt ransomware  
sha256| 35619594724871138875db462eda6cf24f2a462e1f812ff27d79131576cd73ab| Black Hunt ransomware  
sha256| 32877793a1e0d72235e9e785e1f55592c32c9f08b73729815b8103b09a54065f| Black Hunt ransomware  
sha256| 7eea62dcae4e2e5091dd89959529ae047071415a890dda507db4c53b6dcab28b| Black Hunt ransomware  
sha256| 13a5c3b72f81554e04b56d960d3a503a4b08ec77abb43756932a68b98dac1479| Black Hunt ransomware  
  
### Registry Modified by Black Hunt Ransomware

Registry Modification| Description  
---|---  
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run {2C5F9FCC-F266-43F6-BFD7-838DAE269E11} REG_SZ C:\ProgramData#BlackHunt_ReadMe.hta| Adds a startup entry to run a file at system startup  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender DisableAntiSpyware REG_DWORD 1| Disables Windows Defender anti-spyware protection  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Real-Time Protection DisableRealtimeMonitoring REG_DWORD 1| Disables Windows Defender real-time monitoring  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Spynet SubmitSamplesConsent REG_DWORD 2| Sets the consent level for submitting samples to Microsoft  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Threats Threats_ThreatSeverityDefaultAction REG_DWORD 1| Sets default actions for threats detected by Windows Defender  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Threats\ThreatSeverityDefaultAction Low, Medium, High, Severe REG_DWORD 6| Sets default actions for threats of different severities  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\UX Configuration Notification_Suppress REG_DWORD 1| Suppresses Windows Defender notifications  
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer NoClose, StartMenuLogOff REG_DWORD 1| Disables the ability to close the Start Menu and log off  
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System DisableChangePassword, DisableLockWorkstation, NoLogoff, DisableTaskMgr REG_DWORD 1| Disables various system functionalities such as changing password, locking workstation, logging off, and task manager  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\SystemRestore DisableConfig, DisableSR REG_DWORD 1| Disables System Restore configuration and functionality  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\WinRE DisableSetup REG_DWORD 1| Disables Windows Recovery Environment setup  
HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Backup\Client DisableBackupLauncher, DisableRestoreUI, DisableSystemBackupUI, DisableBackupUI REG_DWORD 1| Disables various backup client functionalities  
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer NoRun REG_DWORD 1| Disables the ability to run programs  
  
### References

<https://twitter.com/RakeshKrish12/status/1597839380558716928>

<https://twitter.com/malwrhunterteam/status/1744499152011104549>

<https://blog.sonicwall.com/en-us/2021/09/lockbit-2-0-the-ransomware-behind-the-accenture-breach/>

<https://blog.sonicwall.com/en-us/2023/02/vohuk-ransomware-uses-cipher-exe-making-files-recovery-impossible/>

  


### Rapid7 Labs GitHub

<https://github.com/rapid7/Rapid7-Labs/blob/main/IOCs/BlackHunt.txt>

[**Read Rapid7's Ransomware Radar Report**](/research/report/ransomware-radar-report/) ▶︎

## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)