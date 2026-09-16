# Lucky Mouse: Incident Response to Detection Engineering

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/lucky-mouse-incident-response-to-detection-engineering
- **Date :** 2022-12-01

---

## Introduction

This blogpost discusses how the Tactics, Techniques and Procedures (TTPs) used by the APT27 (Lucky Mouse) intrusion set in the [last incident reported by Intrinsec](https://www.intrinsec.com/apt27-analysis/?cn-reloaded=1),**a Sekoia Managed Security Service Provider (MSSP) partner** , are detected using Sekoia. We therefore publicly share a few detection rules available in our platform, and explain the logic behind each of them. For that purpose, we specifically focus on our telemetry and how we sometimes had to adapt the rules to make them more specific or more generic. As [we use SIGMA, the rules can be easily adapted to another environment, the only specificity we have is the use of Elastic Common Schema (ECS) for the detection rules fields](/blog/xdr-detection-rules-at-scale). For that reason, if a Sekoia rule is relatively similar to an existing SIGMA rule, we will link the SIGMA rule instead.

## Interactive shells & process spawning techniques

A few general techniques can be detected based on Intrinsec’s observations. 

The first one is the probable use of [**wmiexec.py** from the Impacket](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py) suite (or a tool that produces similar patterns), used by APT27 to execute most commands:

_`cmd.exe /Q /c […………] 1> \\127.0.0.1\ADMIN$\__[UNIX_EPOCH_DATETIME] 2>&1`_

![screenshot of the pattern](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd036605_6a92a3f0e9a71d4228404fcc_6a2a7b4ba3074ddacfe8a61f.webp)

![screenshot of the module](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365f9_6a92a3ee2b0ef7af46bd49e2_6a2a7b4ba3074ddacfe8a61c.webp)

Although this pattern can be detected in different ways, Sekoia provides [one detection rule](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/impacket_wmiexec.yml) specific to WMI related activities, based on the _"wmiprvse.exe"_ parent process _._ It is tough to build a good generic rule here without having several false positives, which is why our rule has several conditions. Each condition is rather specific but the rule covers most of the tool's execution even when it is not executed "as is".

Based on Sekoia telemetry, the rule raises no false positive (FP) and requires no specific configuration other than logging command-line activity, hence the Effort Level set to "elementary".

A second technique used by APT27 throughout their attack is the following:

_`wmic /node:127.0.0.1 process call create cmd`_

![A second technique used by APT27 throughout their attack is the following: a simple, well-known technique to create a new process using "wmic".](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365f0_6a92a3e04c776939a1e0d07f_6a2a7b49a3074ddacfe8a5c3.webp)

![A second technique used by APT27 throughout their attack is the following: a simple, well-known technique to create a new process using "wmic".](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365f6_6a92a3e1a49553afbaf386bb_6a2a7b49a3074ddacfe8a5c6.webp)

A second technique used by APT27 throughout their attack is the following: a simple, well-known technique to create a new process using &quot;wmic&quot;.

It is a simple, well-known technique to create a new process using ["wmic"](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic). 

Sekoia provides [a simple rule](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/wmic_process_call_create.yml) solely based on the _"process call create"_ command line parameters. The only FP observed in our telemetry on Windows was the process _"crashpad_handler.exe"_. Since we are vendor-agnostic in our rules as well, we also had to filter out _"/bin/rm"_ that triggered several false positives. While the filter on these two false positives are still a weakness in our rule, it avoids lots of alerts and prevents alert fatigue of SOC analysts.

You may be aware of similar SIGMA, publicly available, rules to detect this activity and wonder why we did not link them instead. Most rules have two major blind spots: the process name is "hardcoded" in the rule and there are whitespaces before or after at least one of the command line parameters. This is great to avoid FPs and most of them definitely matches APT27 current activity as documented by Intrinsec. However, the "hardcoded" process name means the rule relies on an unrenamed _"wmic.exe"_ process or "OriginalFileName" always catching _"wmic.exe"_ being renamed. The whitespaces could lead to missing a non-default usage of wmic commands (usage of quotes before and after each parameter for instance).

Although the attack described by Intrinsec could be detected mainly with these two rules, we will still study each part of the attack in depth to try detecting each technique.

## Windows Defender Exclusions

A classic technique, APT27 used PowerShell to disable Windows Defender, more specifically to exclude a folder from Windows Defender scope, using the following command:

_`powershell Add-MpPreference -ExclusionPath C:\Windows\temp`_

![APT27 uses PowerShell to disable Windows Defender, more specifically to exclude a folder from Windows Defender scope.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd036602_6a92a3ed2e47a1e9fe0e5b9c_6a2a7b4ba3074ddacfe8a617.webp)

![APT27 uses PowerShell to disable Windows Defender, more specifically to exclude a folder from Windows Defender scope.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365e7_6a92a3e8fc9735294387251a_6a2a7b4ba3074ddacfe8a608.webp)

![APT27 uses PowerShell to disable Windows Defender, more specifically to exclude a folder from Windows Defender scope.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365ed_6a92a3ea692919148899fb18_6a2a7b4ba3074ddacfe8a60b.webp)

APT27 uses PowerShell to disable Windows Defender, more specifically to exclude a folder from Windows Defender scope.

There are many ways to disable or tamper Windows Defender. The good news is that there are also many ways to detect that, which means multiple rules can be triggered.

[The rule named "Windows Defender Disabled"](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/disable_windows_defender.yml) is triggered based on command line specific strings of or if any change occurs in the Windows Defender registry key. Of note, it does not look at ScriptBlockText, as this would raise significantly more FPs. More specific rules related to ScriptBlock logging suspicious keywords are available in the Sekoia platform. Furthermore, we provide other rules for Windows Defender being tampered and for the same commands as this rule but base64 encoded -[the detection capability uses the built-in SIGMA "|base64" value modifier.](https://github.com/SigmaHQ/sigma-specification/)

Depending on your environment, for instance, if using PyCharm or some Anti-Virus / EDRs solutions (BitDefender for example), a few FPs can still occur, but those are easy to filter which is why the Effort Level is “intermediate”.

The SIGMA rule titled "Windows Defender Exclusions Added"1 (similar to our rule) is based on the Windows Defender [EventID 5007](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide), narrowed down to specific values. This rule is great since it directly relies on Defender itself, not the command lines. 

## Exchange mailboxes export

According to Intrinsec, APT27 used the following command to export mailboxes from Exchange servers:_`powershell -exec bypass -command Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn;Get-Mailbox | format-table Name,WindowsEmailAddress`_

![According to Intrinsec, APT27 used the following command to export mailboxes from Exchange servers.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365e4_6a92a3e43e6167cebbf6b8b3_6a2a7b49a3074ddacfe8a5cc.webp)

![According to Intrinsec, APT27 used the following command to export mailboxes from Exchange servers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365f3_6a92a3e21f3e07bff481b663_6a2a7b49a3074ddacfe8a5c9.webp)

According to Intrinsec, APT27 used the following command to export mailboxes from Exchange servers

This technique is well-known and has been used by several intrusion-sets. 

[Sekoia provides an efficient rule](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/powershell_exchange_snapin_mailbox.yml) with no observed false positives to date. However this rule is quite specific since it uses regex for the ScriptBlockText pattern and could be bypassed quite easily by using base64 encoding for instance. Therefore we have other rules that would detect the base64 encoding for this command line as well, just like our Defender rules.

## Usage of SysInternals tools

In the described activity, APT27 used two SysInternals tools. The first one is [PsLoggedOn](https://learn.microsoft.com/en-us/sysinternals/downloads/psloggedon), to identify where specific users are logged in. While this tool is well-known in the community as being used for offensive purposes, Sekoia analysts did not see this tool being used by intrusion sets before. Therefore not much research time has been spent on this tool and we are unable to provide an efficient rule, except just detecting the process name or the accepteula parameter which are both easy to bypass, for the time being. We will update our GitHub repository if we find a proper way to detect this tool.

The second Sysinternal tool used by APT27 is [ProcDump](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump), often used by intrusion-sets to dump LSASS’s process memory to then extract credentials. The command used is : 

 _`C:\Windows\Temp\error.log -accepteula -ma lsass.exe c:\windows\temp\error.dmp`_

![The second Sysinternal tool used by APT27 is ProcDump, often used by intrusion-sets to dump LSASS’s process memory to then extract credentials. Sekoia use two rules to detect such behaviour.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365fc_6a92a3e732517fc4026035e9_6a2a7b4ba3074ddacfe8a605.webp)

![The second Sysinternal tool used by APT27 is ProcDump, often used by intrusion-sets to dump LSASS’s process memory to then extract credentials. Sekoia use two rules to detect such behaviour.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd036608_6a92a3ed6568d7e2b4094165_6a2a7b4ba3074ddacfe8a614.webp)

The second Sysinternal tool used by APT27 is ProcDump, often used by intrusion-sets to dump LSASS’s process memory to then extract credentials. Sekoia use two rules to detect such behaviour.

As you may notice, it was renamed but still has the same command-line parameters. Therefore we have two rules to detect such behaviour. [The first rule ](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/procdump_args.yml)detects _"accepteula"_ combined with _"-ma"_ and a _".dmp"_ file or _"lsass"_ as it is often used. It can be bypassed but raises no false positives based on our telemetry, which is a huge quick win.

[The second rule](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/non_legit_use_eula_parameter.yml) is recent and was built following the Intrinsec blogpost, as we found the logic quite interesting: the usage of _"-accepteula"_ with a binary neither originating from the Sysinternals toolsuite, nor known as legitimate. With the provided rule we observed no false positives, based on ~40 days of telemetry.

In addition to our detection rules, we retrieve hashes for ProcDump releases automatically, which allows us to detect its usage (if not modified), even when renamed. We only advise to do that when the tools are not often used for legitimate purposes.

## Ntdsutil to dump ntds.dit database

The intrusion-set also used the famous [ntdsutil ](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc753343\(v=ws.11\))to dump _"ntds.dit"_ database on Domain Controllers with the following command:

_`ntdsutil ac i ntds ifm create full c:\\windows\\temp\\winstore\\ quit quit`_

![The intrusion-set also used the famous ntdsutil to dump “ntds.dit” database on Domain Controllers with the following command.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd036614_6a92a3f1dae089660dfcfa9e_6a2a7b4ba3074ddacfe8a624.webp)

![The intrusion-set also used the famous ntdsutil to dump “ntds.dit” database on Domain Controllers with the following command.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365ea_6a92a3e49d3b9ef4d8bbd28f_6a2a7b4ba3074ddacfe8a5fc.webp)

The intrusion-set also used the famous ntdsutil to dump “ntds.dit” database on Domain Controllers with the following command.

While the command line itself could be detected, there is a specific Windows EventID for when the _"ntds.dit"_ database is created: EventID 325, from the Event Provider [ESENT](https://github.com/NVISOsecurity/sigma-public/blob/master/rules/windows/process_creation/win_susp_ntdsutil.yml). This EventID also raises events when other databases are created therefore a looking for the string _"ntds.dit"_ is necessary. 

To detect _"ntdsutil"_ usage, a general rule can be made on the usage of _"ntdsutil.exe"_ process, like [this SIGMA rule](https://github.com/NVISOsecurity/sigma-public/blob/master/rules/windows/process_creation/win_susp_ntdsutil.yml). It’s fine to have this rule, but having [the other SIGMA rule with the EventIDs](https://github.com/SigmaHQ/sigma/blob/8b749fb1260b92b9170e4e69fa1bd2f34e94d766/rules/windows/builtin/application/win_esent_ntdsutil_abuse.yml) is really necessary. Even if EventIDs can be disabled, we think it is always best to rely on them rather than command lines or process name since it is even easier to rename ntdsutil.exe before using it. With the two rules, both scenarios are covered. 

Although legitimate backup operations can sometimes trigger these rules, we rarely observe false positives and strongly advise to activate the rules.

## RAR to compress and encrypt folders & files

According to Intrinsec, RAR was used to compress and encrypt folders & files using a password with several commands, such as:

`rar.exe a -r -y -hp[PASSWORD] -df c:\windows\temp\error.rar c:\windows\temp\winstore\`

![According to Intrinsec, RAR was used to compress and encrypt folders & files using a password with several commands, such as this.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd03660b_6a92a3e7a2f46752fd01eb5a_6a2a7b4ba3074ddacfe8a602.webp)

According to Intrinsec, RAR was used to compress and encrypt folders & files using a password with several commands, such as this.

![According to Intrinsec, RAR was used to compress and encrypt folders & files using a password with several commands, such as this.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd036611_6a92a3e5dc3071123832deee_6a2a7b4ba3074ddacfe8a5ff.webp)

According to Intrinsec, RAR was used to compress and encrypt folders & files using a password with several commands, such as this.

[Sekoia provides a simple but efficient rule](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/data_compressed_with_rar_with_password.yml), relying on whitespaces before and after the _"a"_ command line argument to avoid false positives but, as written earlier, could be a blind spot in the detection. Thanks to these whitespaces, the rule Effort Level is set to only "intermediate". The rule also covers this command being used within a PowerShell script through the ScriptBlock Logging (but needs the default name _"rar.exe"_ to prevent too many false positives).

## SOCKS tunneling with Chisel

Lucky Mouse also leveraged [Chisel, an open-source tunneling tool](https://github.com/jpillora/chisel), renamed _"veamGues.exe"_ , to run a Chisel server listening on port 9080 and allowing Chisel clients to access the SOCKS5 proxy: 

 _`cmd /c c:\Windows\Temp\veeamGues.exe server -p 9080 –socks5`_

![Lucky Mouse also leveraged Chisel, an open-source tunneling tool, renamed "veamGues.exe", to run a Chisel server listening on port 9080 and allowing Chisel clients to access the SOCKS5 proxy](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd0365e1_6a92a3ea5538c880c2532624_6a2a7b4ba3074ddacfe8a60e.webp)

![Lucky Mouse also leveraged Chisel, an open-source tunneling tool, renamed "veamGues.exe", to run a Chisel server listening on port 9080 and allowing Chisel clients to access the SOCKS5 proxy.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a634a2f46752fd03660e_6a92a3ecdae089660dfcf636_6a2a7b4ba3074ddacfe8a611.webp)

Lucky Mouse also leveraged Chisel, an open-source tunneling tool, renamed &quot;veamGues.exe&quot;, to run a Chisel server listening on port 9080 and allowing Chisel clients to access the SOCKS5 proxy.

Chisel was only renamed but the attackers did not change the default command line, which is quite unique (or at least relative to most SOCKS5 tunneling tools). Therefore, [our rule](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/socks_tunneling_tool.yml) is mainly based on the usage of _"socks4"_ or _"socks5"_ in the command line, _"socks"_ alone giving way too many false positives.

We still have some false positives in our telemetry with this rule, related to the fact that developers used _"chrome.exe"_ for instance to set up the SOCKS proxy. When doing so, it triggers the following command: 

 _`"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --user-data-dir="%USERPROFILE%\proxy-profile" --proxy-server="socks5://localhost:9090"`_

Therefore it triggers our rule as well. It could be a True Positive and it’s often related to a few, if not single, user(s) therefore we recommend activating this rule and adding some filters depending on your environment. Again, a simple but efficient rule! 

## Conclusion

Incident response publications like Intrinsec’s one are a gold mine for defenders and can be used to improve or create detection rules. This blogpost shows our detection logic when looking at this kind of publication and also gives information on our telemetry to ease the integration of our rules without having unexpected false positives within your environment.

## Sekoia shared detection rules

  1. [GitHub - Data Compressed With Rar With Password](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/data_compressed_with_rar_with_password.yml)
  2. [GitHub - Disable Windows Defender](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/disable_windows_defender.yml)
  3. [GitHub - Impacket Wmiexec](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/impacket_wmiexec.yml)
  4. [GitHub - Powershell Exchange Snapin Mailbox](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/powershell_exchange_snapin_mailbox.yml)
  5. [GitHub - Non Legit Use Eula Parameter](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/non_legit_use_eula_parameter.yml)
  6. [GitHub - Procdump Args](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/procdump_args.yml)
  7. [GitHub - Socks Tunneling Tool](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/socks_tunneling_tool.yml)
  8. [GitHub - Wmic Process Call Create](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/host/wmic_process_call_create.yml)
  9. [GitHub - Win Defender Exclusions](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/windefend/win_defender_exclusions.yml)



Discover our:

  * [CTI platform](/platform/intelligence)
  * [SIEM platform](/platform/defend)
  * [AI SOC platform](/platform)