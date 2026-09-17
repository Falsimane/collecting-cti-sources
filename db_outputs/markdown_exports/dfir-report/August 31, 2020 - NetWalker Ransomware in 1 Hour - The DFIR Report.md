# NetWalker Ransomware in 1 Hour - The DFIR Report

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2020/08/31/netwalker-ransomware-in-1-hour/
- **Date :** August 31, 2020

---

![](https://thedfirreport.com/wp-content/uploads/image-42.png)

[adfind](https://thedfirreport.com/category/adfind/)

# NetWalker Ransomware in 1 Hour

August 31, 2020 

The threat actor logged in through RDP, attempted to run a Cobalt Strike Beacon, and then dumped memory using ProcDump and Mimikatz. Next, they RDPed into a Domain Controller, minutes before using PsExec to run the NetWalker ransomware payload on all Domain joined systems. The entire intrusion took ~1 hour.

## What is NetWalker?

> NetWalker, as a ransomware strain, first appeared in August 2019. In its initial version, the ransomware went by the name of Mailto but rebranded to NetWalker towards the end of 2019.
> 
> The ransomware operates as a closed-access RaaS — a ransomware-as-a-service portal. Other hacker gangs sign up and go through a vetting process, after which they are granted access to a web portal where they can build custom versions of the ransomware.
> 
> The distribution is left to these second-tier gangs, known as affiliates, and each group deploys it as they see fit.
> 
> [Catalin Cimpanu](https://www.zdnet.com/meet-the-team/us/catalin.cimpanu/) – <https://www.zdnet.com/article/netwalker-ransomware-gang-has-made-25-million-since-march-2020/>

For more info on NetWalker check out the following posts:

[https://labs.sentinelone.com/netwalker-ransomware-no-respite-no-english-required](https://labs.sentinelone.com/netwalker-ransomware-no-respite-no-english-required/)[/](https://labs.sentinelone.com/netwalker-ransomware-no-respite-no-english-required/)

<https://news.sophos.com/en-us/2020/05/27/netwalker-ransomware-tools-give-insight-into-threat-actor/>

<https://threatpost.com/netwalker-ransomware-29m-march/158036/>

<https://go.crowdstrike.com/rs/281-OBQ-266/images/ReportCSIT-20081e.pdf>

## Exploitation

We saw multiple RDP logins around the time of the attack but we believe [198.181.163[.]103](https://www.ultratools.com/tools/ipWhoisLookupResult) (possibly IPVanish VPN) to be the source of this intrusion. We will include other IPs that logged into the honeypot on this day in the IOCs section.

The threat actor logged in using the DomainName\Administrator account.

## Command & Control

c37.ps1 was dropped and run about 16 minutes after initial login. There didn’t appear to be any network connections made while running this script which makes us wonder if the script works or not.

The script is heavily obfuscated but still looks like Cobalt Strike. When we uploaded the script to VT, Thor said it may also contain Windshield or SplinterRAT.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-30-1024x303.png)

c37.ps1 has a very low detection rate even after 7+ days.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-39-1024x364.png)

Minutes later they ran c37.exe, which copies itself to a temp directory and then stops. This binary includes Neshta as well as many capabilities as seen below:

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-12.png)[capa](https://www.fireeye.com/blog/threat-research/2020/07/capa-automatically-identify-malware-capabilities.html)

After further analysis and a comment from [@GaborSzappanos](https://twitter.com/GaborSzappanos), we were able to confirm that both of these are indeed Cobalt Strike and connect to 173.232.146[.]37 over 443.

![](https://thedfirreport.com/wp-content/uploads/2020/09/image-1.png)

The Cobalt Strike server at 173.232.146.37 is using the [default cert ](https://www.recordedfuture.com/cobalt-strike-servers/)([146473198](https://community.riskiq.com/search/certificate/serialNumber/146473198)) and oddly enough could not be MiTM. We tried to MiTM this connection multiple times and kept getting an error stating SSL session did not authentication successfully.

![](https://thedfirreport.com/wp-content/uploads/2020/09/image-2.png)

We attempted to run c37.ps1 and c37.exe in a few sandboxes and none of them captured the network traffic which tells us that these Beacons include sandbox evasion techniques. Here are a couple runs – <https://capesandbox.com/analysis/54494/> <https://app.any.run/tasks/4524fb0c-8e17-4255-8582-35b0e206ff3f/> <https://capesandbox.com/analysis/54493/>

The c37.exe binary includes shared code from Neshta, poison, BazarBackdoor, XMRig and a large portion from CobaltStrike according to Intezer.

![](https://thedfirreport.com/wp-content/uploads/2020/09/image-1024x434.png)

## Discovery

AdFind was dropped alongside a script named adf.bat. We’ve seen this script in the past and wrote about it [here](https://thedfirreport.com/2020/05/08/adfind-recon/).

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-19.png)

We can see from these lnk files that they opened a few of the txt files output by AdFind. We can also see that domains.txt and ips.log were opened minutes after AdFind being run.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-34.png)[LECmd ](https://binaryforay.blogspot.com/2016/02/introducing-lecmd.html)– Tool by EricZimmerman

A few minutes after AdFind was run, a command prompt was opened and the following commands were either copy and pasted slowly or manually typed.
    
    
    nltest /dclist:
    net group "Domain Computers" /DOMAIN
    net groups "Enterprise Admins" /domain
    net user Administrator

Shortly after that, a script named pcr.bat was dropped and executed.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-23.png)

This script pings a list of hostnames (domains.txt) and writes the output to ips.log. The ping command they use sends one ping and forces IPv4. This domains.txt file most likely came from the above AdFind command using the domainlist parameter.

## Credential Access

Mimikatz was dropped and then a minute later procdump64.exe was dropped. The threat actors then used Procdump to dump lsass using the following command:
    
    
    procdump64.exe -ma lsass.exe lsass.dmp

This procdump64 binary appears to be compiled with Delphi and does not match known hashes. It appears the threat actors rolled their own but included the original instructions.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-46.png)

Mimikatz was run about a minute later.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-20.png)

## Lateral Movement

The threat actor RDPed into a Domain Controller (DC) after dumping credentials. Shortly after accessing the DC they dropped ip.list.txt, P100119.ps1, and PsExec.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-38.png)

The threat actor was now ready to execute it’s objective.

## Objectives

The threat actor used PsExec to mount a share on all systems as the Domain Administrator and then execute the ransomware payload using PowerShell. NetWalker was delivered to all online Domain joined systems in the honeypot via the below command:

C:\psexec.exe @ip-list.txt -d cmd /c “(net use q: /delete /y &; net use q: \\\DomainController\DomainName /user:DomainName\administrator ThisWasThePassword &; powershell -ExecutionPolicy ByPass -NoLogo -NoProfile -windowstyle hidden -NoExit -File q:\P100119.ps1”

After the PowerShell script runs you are left with the following ransom note.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-40.png)

The NetWalker operators asked for $50k within 7 days or $100k after. They were talked down to $35k after the time expired.

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-44.png)

## Timeline

![](https://thedfirreport.com/wp-content/uploads/2020/08/image-43.png)

Enjoy our report? Please consider donating $1 or more to the project using [Patreon](https://www.patreon.com/thedfirreport). Thank you for your support!

## Detections

ET POLICY PsExec service created

PsExec Service Start – <https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_psexesvc_start.yml>

Suspicious Use of Procdump – <https://github.com/Neo23x0/sigma/blob/master/rules/windows/process_creation/win_susp_procdump.yml>

Mimikatz Use – <https://github.com/Neo23x0/sigma/blob/master/rules/windows/builtin/win_alert_mimikatz_keywords.yml>

Detects AdFind usage from our case:
    
    
    title: AdFind Recon
    description: Threat Actor using AdFind for reconnaissance.
    author: The DFIR Report
    date: 2019/8/2
    references:
    - https://thedfirreport.com/2020/08/03/dridex-from-word-to-domain-dominance/
    tags:
    - attack.remote_system_discovery
    - attack.T1018
    logsource:
    category: process_creation
    product: windows
    detection:
    selection_1:
    CommandLine|contains:
    - adfind -f objectcategory=computer
    selection_2:
    CommandLine|contains:
    - adfind -gcb -sc trustdmp
    condition: selection_1 or selection_2
    falsepositives:
    - Legitimate Administrator using tool for Active Directory querying
    level: medium
    status: experimental

Yara rule for Mimikatz <https://github.com/gentilkiwi/mimikatz/blob/master/kiwi_passwords.yar>

## IOCs

[https://misppriv.circl.lu/](https://misppriv.circl.lu/events/view/73574)[events](https://misppriv.circl.lu/events/view/73574)[/view/73574](https://misppriv.circl.lu/events/view/73574)

<https://otx.alienvault.com/pulse/5f4c3eb15ea4e24eb5b43a49>
    
    
    c37.ps1 8e030188e0d03654d5e7a7738a9d6a9a e0a37d0c26b351b789caffc8c90b968269982d 5536be48e4eac81ad77aeade20b28ff8b72275832e6833f5e1b692eb99f312fd13
    
    
    c37.exe 531c0c5e943863b00c7157c05603113a caa18377e764a3a27c715b3d69ba2258ee4eb0b2 4f7dd00a005caf046dd7e494fea25be2264974264d567edfc89122242b7c41bc 
    
    
    adf.bat 96e1849976d90425e74f075ed6bf8c30 1296a1f8887753ef87910b544727de76ce2adcc5 e56d45628f0c2bda30ab235657704aac50a8433bdb4215c77a2e0f52f0f31a49 
    
    
    mimikatz.exe 5af5e3426926e551ed3acc5bea45eac6 e24a174fff19d873df0fa5eddd9ec534617ed9d7 f743c0849d69b5ea2f7eaf28831c86c1536cc27ae470f20e49223cbdba9c677c
    
    
    pcr.bat 81c965ff526e7afd73c91543fee381a3 b9b83b17fd6d89807dcab7772b1416fa90ca4b0e ae431797c551c20fe2f3fe1adc08a566edfabf45abbd924f0c8da06381ab6e48 
    
    
    P100119.ps1 0d890fc8e761b764ba3a04af07197e20 21c0ed7abaafbfd14c777aa370f397e4351654a6 5ae06a8d117e876476832245039715825fbfbefc0d2463ab6c30295dd1d4afa6
    
    
    procdump64.exe 3b447099ca280dabd22d36f84ebfd3bb 49fd831a738b21ee0a1b3b62cd15801abe8c32d5 6a511d4178d6d2f98f8af34311d0e15dc8dc1c4b643e6943f056da6ce242e70d 

Yara – embedded_win_api – A non-Windows executable contains win32 API functions names – Author: nex

RDP logins on the day of the intrusion
    
    
    184.58.243.205
    173.239.199.73
    176.126.85.39
    198.181.163.103
    141.98.81.191
    93.179.69.154
    173.232.146.37

internal case 1003

##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2020/08/31/netwalker-ransomware-in-1-hour/&t=NetWalker%20Ransomware%20in%201%20Hour)
  * [Share on X](https://x.com/share?text=NetWalker%20Ransomware%20in%201%20Hour&url=https://thedfirreport.com/?p=723)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2020/08/31/netwalker-ransomware-in-1-hour/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=NetWalker%20Ransomware%20in%201%20Hour&url=https://thedfirreport.com/2020/08/31/netwalker-ransomware-in-1-hour/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2020/08/31/netwalker-ransomware-in-1-hour/&title=NetWalker%20Ransomware%20in%201%20Hour)
  * [Share by Mail](/cdn-cgi/l/email-protection#be81cdcbdcd4dbddca83f0dbcae9dfd2d5dbcc9b8c8eecdfd0cdd1d3c9dfccdb9b8c8ed7d09b8c8e8f9b8c8ef6d1cbcc989d8e8d8685dcd1dac783d6cacacecd849191cad6dbdad8d7ccccdbced1ccca90ddd1d3918c8e8c8e918e86918d8f91d0dbcac9dfd2d5dbcc93ccdfd0cdd1d3c9dfccdb93d7d0938f93d6d1cbcc91)