# Engineering Detection Around Microsoft Defender

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/engineering-detection-around-microsoft-defender
- **Date :** 2023-08-31

---

## Introduction

This blogpost slightly introduces Microsoft Defender different products and the confusion that can be made between them mainly because they were renamed over the years. Then it focuses on **detection engineering** around **Microsoft Defender Antivirus** (MDAV) by discussing why detection rules on MDAV being disabled or tampered are important but also discussing detection opportunities such as AMSI and MDAV logs.

For our detection opportunities, if you did not read our **previous blogpost** explaining how we build and test our detection rules, we would recommend reading it to have a better understanding of this blogpost.

As a quick reminder, Sekoia.io ingests over**two billion events** per day from European companies with facilities **all over the world**. Our detection environment is composed of multiple detection engines:

![Sekoia.io detection environment is composed of multiple detection engines: Sigma engine, Sigma correlation engine, Anomaly engine, Sekoia.io CTI](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a60b4c776939a1e1148b_6a92a37be17eff730b6590af_6a2a7c0be2d8f7e583ca3e16.webp)

Sekoia.io detection environment is composed of multiple detection engines: Sigma engine, Sigma correlation engine, Anomaly engine, Sekoia.io CTI

Using **Sigma** language on top of **ECS** (Elastic Common Schema) allows us to have detection rules working for multiple logs sources across all of our customers.

## Windows Defender? Microsoft Defender for Endpoints? Microsoft Defender Antivirus? 

**Microsoft Defender Antivirus** (MDAV) is basically what you get when having a classic Windows 10 Pro machine for instance but don’t pay for any Microsoft specific license. MDAV alone acts as a classic antivirus, meaning it can block and quarantine threats but also has the capability to reduce the attack surface on your host through the “Controlled Folder Access” feature and the Attack Surface Reduction (ASR) rules. MDAV is a **protection component** of Microsoft Defender for Endpoint.

**Microsoft Defender for Endpoint (MDE)** is “an enterprise endpoint security platform designed to help enterprise networks prevent, detect, investigate, and respond to advanced threats” as described by Microsoft. To summarize, it can be seen as an EDR that can also work on MacOS and Linux. It is integrated in [Microsoft 365](/blog/userauthenticationmethod-microsoft-365-decode) Defender.

**Microsoft 365 Defender** can be seen as the “XDR of Microsoft”, and is an upgrade of MDE. It covers a larger scope than MDE as it provides an interface to coordinate with this component but also other Microsoft products, including Cloud ones.

In this blogpost we will focus mainly on **Microsoft Defender Antivirus (MDAV)**.

## MDAV and detection engineering

## Real-time protection

**Real-time protection** is the main feature of MDAV. Its job is to continuously scan files, processes, and the Windows Registry to protect the user with signature based protection and behavior analysis. This is the main feature **attackers** commonly**try to disable**.  
While most of MDAV’s features can be modified within the Registry, most of them are not modifiable as local Administrator. The “Real-time protection” registry key is one of those features and can be disabled with the **TrustedInstaller** permissions:

# Required rights: TrustedInstaller   
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection" -Name "DisableRealTimeProtection" -Value 1

However Real-time protection can be disabled as **local Administrator** using the Set-MpPreference command.

### Set-MpPreference

This command has many different options to **configure preferences for MDAV**. These options could be used to **disable or tamper MDAV** , which will not all be listed and explained. For instance, one option allows to **disable Real-time protection** :

# Required rights: Administrator   
Set-MpPreference -DisableRealtimeMonitoring $true

Unlike the registry modification, this command works as **local Administrator**. This is straightforward but attackers sometimes want to be stealthier and could use the Add-MpPreference command instead.

## Add-MpPreference

This command performs similar actions as the Set-MpPreference command in a tinier scope. Instead of configuring preferences for MDAV, it is used to **modify settings in MDAV**. For instance, there is an option to exclude a directory from the MDAV’s protection:

# Required rights: Administrator   
Add-MpPreference -ExclusionPath 'C:\Temp'

This command also works as a **local Administrator** and, while not as efficient as the Set-MpPreference command, it is still useful and sometimes stealthier. 

Both “Add-MpPreference” and “Set-MpPreference” commands are often **used** for **legitimate purposes**. Therefore, detecting these commands or their options raises too many false positives, which is painful for detection engineers. Because of that, the rules we share in this blogpost are solely based on the base64 variants and not on the non-encoded ones. The non-encoded ones require great effort from companies to activate them and have low false positives rate therefore we prefer not to share these detection rules.

Sekoia.io provides two Sigma rules to detect the base64 variants: _“Windows Defender Disabled Base64 Encoded”_ and _“Windows Defender Set-MpPreference Base64 Encoded”_.

**Microsoft Defender Antivirus (MDAV) Disabled Base64 Encoded**  
detection:  
selection1:  
process.command_line|wide|base64offset|contains:  
\- 'DisableBehaviorMonitoring'  
\- 'DisableRealtimeMonitoring'  
\- 'Add-MpPreference'  
\- 'DisableIntrusionPreventionSystem'  
\- 'DisableIOAVProtection'  
\- 'DisableScriptScanning'  
\- 'EnableControlledFolderAccess'  
\- 'EnableNetworkProtection'  
\- 'MAPSReporting'  
\- 'SubmitSamplesConsent'  
selection2:  
action.properties.ScriptBlockText|wide|base64offset|contains:  
\- 'DisableBehaviorMonitoring'  
\- 'DisableRealtimeMonitoring'  
\- 'Add-MpPreference'  
\- 'DisableIntrusionPreventionSystem'  
\- 'DisableIOAVProtection'  
\- 'DisableScriptScanning'  
\- 'EnableControlledFolderAccess'  
\- 'EnableNetworkProtection'  
\- 'MAPSReporting'  
\- 'SubmitSamplesConsent'  
condition: selection1 or selection2 

**Microsoft Defender Antivirus (MDAV) Set-MpPreference Base64 Encoded**  
detection:  
selection1:  
process.command_line|wide|base64offset|contains:  
\- 'Set-MpPreference'  
\- 'set-mppreference'  
\- 'Add-MpPreference'  
\- 'add-mppreference'  
selection2:  
action.properties.ScriptBlockText|wide|base64offset|contains:  
\- 'Set-MpPreference'  
\- 'set-mppreference'  
\- 'Add-MpPreference'  
\- 'add-mppreference'  
condition: selection1 or selection2

False positives are sometimes triggered from these rules but they are easy to filter out. The caveat of the rules is that they **only detect base64 encoded versions** and not the non-encoded commands. This had to be done so the rules do not raise many false positives, and, considering the Sekoia.io detection model, to have rules with a low effort level, enabling our customers to easily activate them.

## Remove MDAV’s signatures

In many attack scenarios, it would be stealthier to let MDAV running, and prevent it from comparing attackers’ implant against the signature base. To achieve that, a quick way would be to**remove the signatures embedded in MDAV** :

# Required rights: Administrator   
"C:\ProgramData\Microsoft\Windows Defender\Platform\<your Defender version>\MpCmdRun.exe" -RemoveDefinitions -All 

The command works as a local Administrator and removes all the signatures embedded in MDAV, making it unable to detect anything. Furthermore, it uses “MpCmdRun.exe”, a **legitimate executable** from the MDAV suite.

Sekoia.io provides a detection rule for the suspicious usage of the MpCmdRun command based on the command’s options:

**Microsoft Defender Antivirus (MDAV) Signatures Removed With MpCmdRun**  
detection:  
selection:  
process.command_line|contains:  
\- 'removedefinitions'  
\- 'removedynamicsignature'  
condition: selection 

We observed 58 hits in 30 days, mostly because of the “removedynamicsignature” string detected by the rule. To narrow down the number of false positives, detection can be focused only on “removedefinitions” instead, as it is the most commonly used option. We would rather detect both, as false positives can be easily filtered out (often one software to whitelist), and allows us to have a more generic rule.

## Or just stop the services!

MDAV relies on three services to fully work:

  * **Sense** : Microsoft Defender Advanced Threat Protection
  * **WinDefend** : Microsoft Defender Antivirus Service
  * **WdNisSvc** : Microsoft Defender Antivirus Network Inspection Service



The most straightforward way to disable MDAV is to **stop these services**. Several techniques can perform that such as PowerShell, registry changes or even the classic “sc” command:

# Required rights: TrustedInstaller   
sc stop WinDefend  
sc stop Sense  
sc stop WdNisSvc

To execute these commands the attacker needs to be **TrustedInstaller** first, which explains why this technique is not the most widely used. Furthermore, if the command is used without the correct permissions, MDAV will raise an alert:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a60b4c776939a1e11488_6a92a379dae089660dfcace7_6a2a7c0ae2d8f7e583ca3d87.webp)

Sekoia.io provides a Sigma rule to detect the usage of this technique:

**Microsoft Defender Antivirus (MDAV) Disable Services**  
detection:  
# Stop services  
powershell_command_stop_service:  
action.properties.ScriptBlockText|contains|all:  
\- 'Get-Service'  
\- 'Stop-Service'  
cmd_command_stop_service:  
process.command_line|contains|all:  
\- 'sc'  
\- 'stop'  
cmd_command_disable_service:  
process.command_line|contains|all:  
\- 'sc'  
\- 'config'  
\- 'start=disabled' powershell_service_name:  
action.properties.ScriptBlockText|contains:  
\- 'WinDefend'  
\- 'WdNisSvc'  
\- ' Sense'  
cmd_service_name:  
process.command_line|contains:  
\- 'WinDefend'  
\- 'WdNisSvc'  
\- ' Sense'  
# Modify registry Start value (detect from command line)  
powershell_modify_registry:  
action.properties.ScriptBlockText|contains|all:  
\- 'Set-ItemProperty'  
\- 'CurrentControlSet'  
\- 'Services'  
\- 'Start'  
cmd_modify_registry:  
process.command_line|contains|all:  
\- 'reg'  
\- 'add'  
\- 'currentcontrolset'  
\- 'service'  
\- 'start'  
condition: (powershell_command_stop_service and powershell_service_name) or (cmd_command_stop_service and cmd_service_name) or (cmd_command_disable_service and cmd_service_name) or (powershell_modify_registry and powershell_service_name) or (cmd_modify_registry and cmd_service_name)

Only 6 false positives in a 30 days time range were observed.

## What about AMSI?

AMSI (AntiMalware Scan Interface) is a system designed to **enhance Windows protection** against malware. It is agnostic of antimalware vendors and is integrated in many Windows components. Developers can easily interact with AMSI using the API and can register to process any content submitted to AMSI. 

Example of AMSI application:

![Example of AMSI application:](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a60b4c776939a1e11484_6a92a37adae089660dfcadba_6a2a7c0ae2d8f7e583ca3d8a.webp)

Example of AMSI application:

MDAV is a **registered** AMSI anti-malware **service provider** and a threat actor may want to bypass this feature without disabling MDAV itself, since most of MDAV detection comes from AMSI.

To know your AMSI provider, you just have to check the registry key at "HKLM:\SOFTWARE\Microsoft\AMSI\Providers\". The name of the key is the ID of the provider, for example, MDAV is {2781761E-28E0-4109-99FE-B9D127C57AFE}. 

How AMSI exactly works is quite complex and this would deserve a blogpost on its own. Thankfully, RedCanary published a blogpost in July 2022, covering great details on AMSI internals.  
For the blogpost we focus on one of the most known AMSI bypass, by loading .NET Assembly in PowerShell:

# Required rights: Administrator   
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)

There are other ways to bypass AMSI, and many ways to obfuscate the above command. The website AMSI fail gives several examples of **AMSI bypasses and obfuscation techniques**.

Sekoia.io provides **two rules** to detect some AMSI bypass techniques: _"PowerShell AMSI Deactivation Bypass Using .NET Reflection" and "PowerShell AMSI Bypass_ ".

**PowerShell AMSI Deactivation Bypass Using .NET Reflection**  
detection:  
selection:  
\- process.command_line|contains: 'amsiinitfailed'  
\- action.properties.ScriptBlockText|contains: 'amsiinitfailed'  
selection_base64encoded:  
\- process.command_line|wide|base64offset|contains: 'amsiInitFailed'  
\- action.properties.ScriptBlockText|wide|base64offset|contains: 'amsiInitFailed'  
condition: selection or selection_base64encoded 

**Powershell AMSI Bypass**  
detection:  
selection:  
action.properties.ScriptBlockText|contains: 'NonPublic,Static'  
condition: selection 

Please note these are not bullet-proof rules detecting all kinds of AMSI bypasses but instead good rules to cover most common ways to perform AMSI bypass. Only two hits for both rules in a 30 days time range were observed.

## MDAV is not always disabled

Detecting MDAV being disabled is not the only useful detection that comes with MDAV. Defenders should also retrieve the **alerts raised by MDAV** as in most cases they are relevant. To raise these alerts, MDAV uses several event IDs, such as the **event IDs 1116 or 1117**. 

All the event IDs related to MDAV being tampered raise a high number of events, making it hard to have a rule for them. However the threats detected by MDAV are a real good addition to a classic detection environment and here is a rule, simply based on the event IDs, for that purpose:

**Microsoft Defender Antivirus (MDAV) Threat Detected**  
detection:  
selection:  
action.id:  
\- '1006'  
\- '1007'  
\- '1008'  
\- '1015'  
\- '1116'  
\- '1117'  
\- '1118'  
\- '1119'  
\- '1125'  
\- '1126'  
event.provider: 'Microsoft-Windows-Windows Defender'  
condition: selection

Sekoia.io also provides other rules for its customers based on the MDAV threat name in the alerts. While it is also based on the event IDs 1116 and 1117, it allows our customers to have a direct view of what has been detected and therefore know if it is highly critical or not.

## Conclusion

Microsoft Defender AntiVirus is a great product itself but building detection rules around it is even better. Attackers often disable it using different techniques which is why defenders have to follow and be updated on these techniques. In this blogpost we presented some techniques by explaining how they could be performed by attackers but also by providing detection rules for them that we use in our production environment. You can have a rough idea if the rules can be appropriate to your environment as we provided the false positives number generally in a 30 days time range. Sekoia.io hopes this information and the provided detection rules, available in our public GitHub repository, will be useful to many companies. 

Sekoia.io provides more rules related to Microsoft Defender (and not just MDAV) for our customers :

![rules in sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a60a4c776939a1e11481_6a92a37c878de395f10eb5d8_6a2a7c0be2d8f7e583ca3e25.webp)

Rules available in Sekoia