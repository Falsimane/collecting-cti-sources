# 2021 Year In Review

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2022/03/07/2021-year-in-review/
- **Date :** March 7, 2022

---

![](https://thedfirreport.com/wp-content/uploads/333333-scaled.png)

[Uncategorized](https://thedfirreport.com/category/uncategorized/)

# 2021 Year In Review

March 7, 2022 

As we come to the end of the first quarter of 2022, we want to take some time to look back over our cases from 2021, in aggregate, and look at some of the top tactics, techniques and procedures (TTP’s) we observed. In total, we reported on 20 incidents in 2021, the vast majority were initial access broker malware (Trickbot, IcedID, BazarLoader, etc.), which often lead to full domain compromise and ransomware.

This report will contain details from all of our public reports over 2021, this is not comprehensive of overall threat actor activity, as there is always inherit sampling and collection bias. However, reviewing these common activities can help a defender prioritize their time and budget, to protect against some of the most common threat actor behaviors.

### Shout out to our analysts who put this report together!

Report lead unnamed contributor 4 (UC4)

Contributing analysts [@ICSNick](https://twitter.com/IcsNick), [@yatinwad](https://twitter.com/yatinwad), [@_pete_0](https://twitter.com/_pete_0) and 1 unnamed contributor

### Services

We offer multiple services including a [Threat Feed](https://thedfirreport.com/services/) service which tracks Command and Control frameworks such as Cobalt Strike, Metasploit, Empire, PoshC2, etc. More information on this service and others can be found [here](https://thedfirreport.com/services/).

We also have artifacts available from our cases such as pcaps, memory captures, files, event logs including Sysmon, Kape packages, and more, under our [Security Researcher and Organization](https://www.patreon.com/thedfirreport) services.

## Intrusion statistics aligned to the MITRE ATT&CK framework

### Initial Access

Over the last year, we have witnessed numerous intrusions where malware variants such as Trickbot, Hancitor, Bazar, and IcedID have been utilized as an entry point for ransomware attacks. In the majority of the intrusions, the malware was distributed in the form of non-targeted phishing, such as mass malware spam campaigns.

Initial Access Sources 2021.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-01.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-01.png)

Our reports tend to focus on instances where phishing is the initial vector, as was the case in 16 of 20 reports. Although we still experience cases of threat actors compromising vulnerable web-facing applications, those cases do not always turn into a large-scale intrusion.. Our report on [Exchange Exploit Leads to Domain Wide Ransomware](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/), was the only case where the threat actors actively sought to deploy ransomware after getting access through a vulnerable application. The other two cases ([All that for a Coinminer?](https://thedfirreport.com/2021/01/18/all-that-for-a-coinminer/) and [WebLogic RCE Leads to XMRig](https://thedfirreport.com/2021/06/03/weblogic-rce-leads-to-xmrig/)) are a good representation of less impactful malicious activity, where the threat actors installed cryptominers. However, we believe that these intrusions can signal vulnerabilities that need immediate patching and remediation before being exploited by a threat actor seeking larger scale objectives.

Phishing was the main initial access vector for our cases in 2021. The malware vectors we saw in 2021 were:

  1. [TrickBot](https://thedfirreport.com/category/trickbot/)
  2. [Bazar](https://thedfirreport.com/category/bazar/)
  3. [IcedID](https://thedfirreport.com/category/icedid/)
  4. [Hancitor](https://thedfirreport.com/category/hancitor/)



The below graphic displays the tools/methods used by threat actors after getting initial access via the initial access malware listed above.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-02.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-02.png)

### Persistence

After execution of the initial access malware, many threat actors deploy persistence mechanisms, such as the creation of scheduled tasks, deployment of web shells, remote access software and registry “Run” Keys.

Scheduled Task Example ([reference](https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/))

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-03.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-03.png)

Add New User Example ([reference](https://thedfirreport.com/2021/10/04/bazarloader-and-the-conti-leaks/))[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-04.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-04.png)

Registry Run Key Example ([reference](https://thedfirreport.com/2021/06/03/weblogic-rce-leads-to-xmrig/))[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-05.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-05.png)

In 14 of 20 cases, persistence was observed. Scheduled tasks were the most common persistence method observed in our intrusions. In most, if not all cases, scheduled tasks, bits-jobs, and registry run keys were executed from the initial malware vector. When we look at the later stages of the attack, during post-exploitation activities, we can see that the threat actors favor new user additions and third-party remote access software as the main persistence techniques.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-06.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-06.png)

In some cases, we did not observe any typical form of persistence during the entire intrusion. However, we found that these threat actors seem to prefer to broaden their access throughout the network by launching several Cobalt Strike beacon sessions. In this way, they can maintain their presence even if one or more compromised workstations become inaccessible. Servers are often chosen during this beacon deployment phase, which is more likely to remain online compared to a typical workstation.

Another common method observed to maintain access is by installing third-party remote access software such as AnyDesk, TeamViewer, Splashtop and Atera. An interesting observation is that the majority of this activity occurred on compromised domain controllers.

Here’s an example from the [Conti Leaks](https://twitter.com/TheDFIRReport/status/1498642505646149634) that show the process of how they install AnyDesk:

> "Anydesk"  
>   
> cmd.exe /c C:ProgramDataAnyDesk.exe –install C:ProgramDataAnyDesk –start-with-win –silent  
>   
> "And then we log in with a local admin or a domain account and use the charms of Anydesk  
> You can also download / upload to / from the victim's machine…"[#ContiLeaks](https://x.com/hashtag/ContiLeaks?src=hash&ref_src=twsrc%5Etfw) [pic.twitter.com/2nUm0XdLMW](https://t.co/2nUm0XdLMW)
> 
> — The DFIR Report (@TheDFIRReport) [March 1, 2022](https://x.com/TheDFIRReport/status/1498672358843953152?ref_src=twsrc%5Etfw)

This AnyDesk activity was also observed in our [Diavol Ransomware](https://thedfirreport.com/2021/12/13/diavol-ransomware/) case.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-07.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-07.png)

### Privilege Escalation/Credential Access

With respect to credential access, multiple techniques were utilized by the threat actors. Some of the notable ones are: Dumping of LSASS using Task Manager and Procdump, creation of a copy of NTDS.dit using ntdsutil.exe and extraction of SAM, SECURITY and SYSTEM hives.

Depending on the level of access, threat actors are looking to escalate privileges on the beachhead host to leverage high integrity Beacon sessions. Having high integrity access allows them to access credentials from the host using various methods. Below, we highlight the privilege escalation and credential access methods observed across our 2021 reports.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-36.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-36.png) [![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-35.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-35.png)

Accessing the LSASS process is the method that we see used by threat actors in the majority of the cases. Using Cobalt Strike, attackers can extract credentials from the LSASS process either with the use of Mimikatz or by accessing the security hives. We covered related detections in our [Cobalt Strike, a Defender’s Guide](https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/).

Threat actors can also use third-party tools such as ProcDump or even Task Manager in cases where remote interactive access is possible. These methods allow them to dump the LSASS process to disk and take it offline to extract the credentials.

ProcDump Example ([reference](https://thedfirreport.com/2021/08/16/trickbot-leads-up-to-fake-1password-installation/))

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-10.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-10.png)

Task Manager Example ([reference](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/))

![](https://thedfirreport.com/wp-content/uploads/2022/03/today.png)

### Defense Evasion

When it comes to defense evasion, we noticed that process injection techniques were very common among threat actors. This allows them to establish additional Beacons on the already compromised hosts, to avoid detection.

In five separate cases, we encountered threat actors disabling security tools using various methods. One of the most notable cases was the [IcedID to XingLocker Ransomware in 24 hours](https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/) case. In that case, the attackers used multiple batch files to disable well-known AV and EDR agents on the host. The batch scripts came from the first revision of [Revisions · quick-disable-windows-defender.bat · GitHub](https://gist.github.com/anadr/7465a9fde63d41341136949f14c21105/revisions), which was used by the ransomware operators without making any changes.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-12.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-12.png)

Masquerading Example ([reference](https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/))

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-13.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-13.png)

Obfuscation Example ([reference](https://thedfirreport.com/2021/08/01/bazarcall-to-conti-ransomware-via-trickbot-and-cobalt-strike/))

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-14.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-14.png)

### Discovery

Once access is established, threat actors then need to enumerate the victim environment. Common initial discovery tools include Windows built-in utilities (net.exe, nltest.exe, systeminfo, ipconfig, whoami, etc) and the [AdFind](https://www.joeware.net/freetools/tools/adfind/) tool. In a few cases, adversaries attempted to get a listing of open ports/running services on remote hosts by performing port scans using tools such as Advanced IP Scanner and KPortScan 3.0.

The first thing we observe from hands-on keyboard operators is usually additional discovery activity. We see threat actors concentrate on searching for the Domain Controllers and general environmental information.

The statistics below illustrate the most used Windows tools for enumerating the environment. We compare each tool to the total percent of cases investigated.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-15.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-15.png)

We see the enumeration commands executed in a short time span, between 1-5 seconds. The execution is usually done through post-exploitation frameworks (Cobalt Strike in most cases).

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-16.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-16.png)

_Example screenshot is taken from the case:_[From Zero to Domain Admin](https://thedfirreport.com/2021/11/01/from-zero-to-domain-admin/)
    
    
    C:\Windows\system32\cmd.exe /C net time 
    C:\Windows\system32\cmd.exe /C ping [Domain Controller] 
    C:\Windows\system32\cmd.exe /C nltest /dclist:[Domain Name] 
    C:\Windows\system32\cmd.exe /C Net group "Domain Admins" /domain \
    C:\Windows\system32\cmd.exe /C nslookup 
    C:\Windows\system32\cmd.exe /C ping 190.114.254.116 
    C:\Windows\system32\cmd.exe /C net group /domain 

### Lateral Movement

Lateral movement is a vital component of threat actor TTPs. Once they get the lay of the land through the discovery methods we outlined above, we repeatedly see them move laterally across the network. Domain Controllers, file shares and similarly high-value servers are primary targets.

The number one post-exploitation framework of choice, Cobalt Strike, allows threat actors to leverage different techniques for the purpose of lateral movement.

Other common choices for threat attackers include Remote Desktop connections, remote WMI execution of transferred binaries, and the Sysinternals tool PsExec.

![](https://cdn.discordapp.com/attachments/891776008280219699/950485109247717397/unknown.png)

(updated 3/7/22 @ 1330 UTC)

WMIC Lateral Movement Example ([reference](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/))

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-18.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-18.png)

Psexec Example ([reference](https://thedfirreport.com/2021/05/12/conti-ransomware/))

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-19.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-19.png)

### Command and Control

One common theme seen across the majority of the intrusions has been the reliance on Cobalt Strike for performing post-exploitation activities. In almost all cases, the initial access brokers such as Trickbot and Bazar, dropped multiple Cobalt Strike beacons across the victim environment.

For an in-depth breakdown of some of the network operations of Cobalt Strike see our [recent report on the topic](https://thedfirreport.com/2022/01/24/cobalt-strike-a-defenders-guide-part-2/).

### Exfiltration

While exfiltration of data was not a common sight in our data set, we observed exfil in 6 of the 20 cases. In the cases where data exfiltration was observed, the threat actors used tools such as RClone, FileZilla, or WinSCP to transfer the data to their controlled servers. In many other cases, threat actors downloaded sensitive data via Cobalt Strike Beacons.

One notable case for the year was the [Diavol Ransomware](https://thedfirreport.com/2021/12/13/diavol-ransomware/). Ransomware operators used [ufile.io](http://ufile.io) to upload the LSASS dump file they extracted from one of the domain controllers.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-20.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-20.png)

To wrap up this chapter, we’d like to provide an overview of the tools that we’ve seen attackers employ this year. We included the tools in their respective phases of attack after seeing them in action. We used the MITRE ATT&CK framework to show how these tools work at various phases of an attack.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-21.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-21.png)

## Indicators of Attack/Behavior-based information focusing on the human element

In our cases, we frequently observe hands-on keyboard activity by the threat actor during the intrusion. This provides a unique insight into the human side of the attack – how they conduct operations, respond to challenges, and how they use the tooling to achieve effects. This provides additional detection opportunities – in addition to Indicators of Compromise (IoC) and Indicators of Activity (IoA).

It is impressive to see that, in some instances, threat actors have adapted their tools, techniques, and procedures (TTPs) to evade detection. In other cases, we’ve observed operator mistakes, errors of judgement, and operational security (OPSEC) failures. We have also witnessed some of the challenges they encounter during intrusions.

Looking into the early Cyber Kill Chain steps of the intrusions, we see that some tasks are automated. However, once an attacker is within a target’s operating environment, many activities often require hands-on keyboard intervention by the operator in order to continue with their objectives. During this period, all the attacker’s hands-on keyboard activities can bring risk of detection or bring them one step closer to their objectives. Some of the typical hands-on keyboard activities include:

  * Discovering security audit tools
  * Overcoming security tools by disabling them all together
  * Encountering lateral movement barriers and seeking alternative approaches, etc.



We looked into our most popular and unusual activities related to attackers’ activities, which we will discuss below, from attackers’ tooling configurations, to usage, and conduct during intrusions.

### Cobalt Strike

A common trend observed in our cases is the use of Cobalt Strike which is usually configured with a standard malleable C2 profile. A malleable C2 profile specifies a number of parameters, such as user agent string, spawn to process, jitter etc. Most of the default profiles are well known and can be detected by host and network monitoring rules.

Cobalt Strike continues to be the top post-exploitation tool favored by most threat actor groups, with the most popular malleable c2 profile observed this year being ‘jquery-3.3.1.min.js’ with the relevant Beacon spawning under Rundll32.exe. The chart below illustrates the most popular spawn-as executable types and some rare ones, such as calc.exe that we saw in 2021.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-22.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-22.png)

For further information on Cobalt Strike malleable C2 profiles and possible avenues for detection, check out our second Cobalt Strike report – [Cobalt Strike, a Defender’s Guide – Part 2](https://thedfirreport.com/2022/01/24/cobalt-strike-a-defenders-guide-part-2/).

### Thou shall follow the playbook

Following the playbook in the literal sense, copying and pasting commands are more common than expected. We have observed cases where operators kept entering misspelled commands taken from documentation. In [one case](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/), we observed the operator copying and pasting commands from a script, neglecting to provide the actual IPv4 addresses as the required parameter:

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-23.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-23.png)

In the case [BazarLoader and the Conti Leaks](https://thedfirreport.com/2021/10/04/bazarloader-and-the-conti-leaks/), the operator accidentally entered a Cobalt Strike command via the Windows command line:

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-24.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-24.png)

We can only assume that the operators attempted to invoke a [Cobalt Strike aggressor script](https://github.com/harleyQu1nn/AggressorScripts/blob/master/AVQuery.cna) to enumerate and discover the installed AV. Later on, in 2021, the Conti playbooks were leaked, allowing us to link this activity with the operator’s hands-on keyboard-related task. We were then able to reference many of the observed activities in our previous cases and provide insights through our Twitter account:

> This content looks VERY familiar…<https://t.co/wxgeovLjE1>  
>   
> 1\. "Initial Actions"  
> 2\. rclone config using Mega  
> 3\. rclone instructions  
> 4.Powerview/UserHunter instructions  
>   
> Thanks [@vxunderground](https://x.com/vxunderground?ref_src=twsrc%5Etfw)!! [pic.twitter.com/9Dgi8SGatG](https://t.co/9Dgi8SGatG)
> 
> — The DFIR Report (@TheDFIRReport) [August 5, 2021](https://x.com/TheDFIRReport/status/1423361119926816776?ref_src=twsrc%5Etfw)

### BYOT (Bring Your Own Tools)

We are astonished by the number of tools brought into an intrusion. Along with third-party tooling, living-off-the-land techniques are routinely observed – especially during the discovery phase. Bringing tools into an environment introduces several risks for the operator and opportunities for the defender from a detection point of view. Some of those risks include detection and blocking by AV, software incompatibilities, software restriction policies, etc. As discussed in the sections above, the most popular tool observed this year is AdFind. AdFind is the usual suspect in almost every intrusion we report. In 2020, we published a whole article covering [this tool](https://thedfirreport.com/2020/05/08/adfind-recon/).

Other tools and scripts we have encountered during the past year across a number of published cases are illustrated below:

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-25.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-25.png)

Occasionally, we observe threat actors making changes to their tool configurations inside the infected host. Below is an example where threat actors made the necessary changes before a successful ransomware execution.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-26.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-26.png)

_Case:[CONTInuing the Bazar Ransomware Story](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)_

### Every Contact Leaves a Trace

Every case provides us with a range of artifacts that are left behind on hosts, either intentionally (threat actor bringing own tools) or as a byproduct (execution of commands via prefetch). Artifacts can include scripts, tools, beacons, staged files, etc.

A common trend observed, is that there is very little effort to remove traces during and after the intrusion. Some examples from our cases include:

Running beacons that have failed to call home, resulting in persistent DNS callback requests from processes that wouldn’t be expected to make high volume of requests. Look for domain traffic, where the polling requests have a consistent trend profile. In this example, a beacon is sending heartbeats to an unreachable C2 server, notice that the requests per-hour and per-day are consistent. 

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-27.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-27.png)

Results of various Tools/scripts are left behind along with the tools themselves, i.e. text files containing collected host details from discovery, executable beacons in user folders etc.

[BloodHound files dropped to disk](https://thedfirreport.com/wp-content/uploads/2021/09/f8a41ed862e52a8a240ae0e7e197ca06389099229378e60d56feab93acf96f67)

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-28.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-28.png)

[AdFind results written to disk](https://thedfirreport.com/2021/08/01/bazarcall-to-conti-ransomware-via-trickbot-and-cobalt-strike/)

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-29.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-29.png)

[Task Manager dumping Lsass](https://thedfirreport.com/2021/12/13/diavol-ransomware/)

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-30.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-30.png)

### Attacker Infrastructure

We have observed several instances where the threat actor’s infrastructure becomes exposed during the intrusion. One example includes the operator’s source machine during a remote desktop session – [CONTInuing the Bazar Ransomware](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/).

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-31.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-31.png)

Another case, was during what we believed to have been a technical issue – a hosted beacon, was remotely pulled (out of band coms) – rather than through the standard C2 that was already established – [BazarCall to Conti Ransomware via Trickbot and Cobalt Strike](https://thedfirreport.com/2021/08/01/bazarcall-to-conti-ransomware-via-trickbot-and-cobalt-strike/). The payload was available from a public facing IP, and pulled using the curl command (evident by the Curl user agent string).\

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-32.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-32.png)

Not all intrusions are successful; sometimes, attackers come across technical issues. Some issues include tooling that doesn’t function as expected and other environmental-specific challenges that would slow down expansion within the network.

### Fingerprinting

Fingerprinting threat actors’ craftsmanship is one of the more fascinating conclusions made when investigating artifacts. In the case of [CONTInuing the Bazar Ransomware Story](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/) the use of profanity was embedded within the HTA file.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-33.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-33.png)

These can be useful IoCs in and of themselves. In other circumstances, threat actors spend considerable effort developing bespoke software, only to leave identifiers such as helpful group names and version numbers.

[![](https://thedfirreport.com/wp-content/uploads/2022/03/2021-34.png)](https://thedfirreport.com/wp-content/uploads/2022/03/2021-34.png)

## 

## Final Advice for Defenders

From a defender’s perspective, each of the above points provides various detection opportunities. These could include recognizing outlier behavior, such as binaries executing from non-standard locations, or detecting outlier activity, such as a high frequency of crashes within a short period of each other.

Reducing your attack surface and regular patching can have some big wins and avoid some common scenarios we have seen in 2021, such as initial compromises through Log4j and ProxyShell/ProxyLogon exploits. Disabling macros and forcing scriptable files to open in notepad will also provide a high level of return on investment.

We would like to highlight a few guides that CISA has released that can assist defenders and organizations in getting their attack surface under control.

[Stuff off Search](https://www.cisa.gov/publication/stuff-off-search)

By using various online search platforms it is possible to get an understanding of what services, assets and devices are exposed on the internet. Reducing this footprint limits the adversaries’ potential entries into the organization’s network.

[Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities) & [Top Routinely Exploited Vulnerabilities in 2021](https://www.cisa.gov/uscert/ncas/alerts/aa21-209a)

Using these resources along with [“S.O.S”](https://www.cisa.gov/publication/stuff-off-search) defenders and organizations can identify the vulnerabilities associated with their exposed assets. By prioritizing assets that have known vulnerabilities which are actively exploited, the organization can remediate risk quicker and focus on things that provide a high return on investment.

CISA, ASD/ACSC, Mandiant, Microsoft and the UK NCSC have plenty of information and guides regarding protecting against ransomware and general best practices for logging, network architecture and tips for everyday users.

  * [CISA – Ransomware Guide](https://www.cisa.gov/sites/default/files/publications/CISA_MS-ISAC_Ransomware%20Guide_S508C_.pdf)
    * Ransomware Prevention Best Practices
    * Ransomware Response Checklist
  * [UK NCSC – Mitigating malware and ransomware attacks](https://www.ncsc.gov.uk/guidance/mitigating-malware-and-ransomware-attacks)
    * How to defend organizations against malware or ransomware attacks
  * [ASD/ACSC ](https://www.cyber.gov.au/ransomware/protect-yourself-against-ransomware-attacks)[– Protect yourself against ransomware attacks](https://www.cyber.gov.au/ransomware/protect-yourself-against-ransomware-attacks)
    * How people can protect themselves against ransomware attacks
  * [Microsoft – Rapidly protect against ransomware and extortion](https://docs.microsoft.com/en-us/security/compass/protect-against-ransomware#:~:text=This%20phase%20is%20designed%20to,attack%20without%20paying%20the%20ransom.)
    * How to protect your organization from ransomware
  * [Mandiant – Ransomware Protection and Containment Strategies](https://www.fireeye.com/content/dam/fireeye-www/current-threats/pdfs/wp-ransomware-protection-and-containment-strategies.pdf)
    * Practical Guidance for Endpoint Protection, Hardening and Containment



Many of the ransomware TTPs are not complex or stealthy. One of the primary reasons behind this is that they do not need to be stealthy to achieve their goals. We commonly see threat actors use Cobalt Strike more than other implants due to the ease of use and the fact that it is a really powerful post-exploitation framework.

We have released a two-part guide about Cobalt Strike to assist defenders in understanding more, and hopefully; are better equipped to detect this framework. The guide can be found here:

  * <https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/>
  * <https://thedfirreport.com/2022/01/24/cobalt-strike-a-defenders-guide-part-2/>



## Outlook

There is no magic bullet to make ransomware disappear, and we anticipate that ransomware-based attacks will continue while incentives remain. Across the globe, multiple countries like USA, Australia and Netherlands have announced task forces to focus on the ransomware threat.

Australia specifically announced their “Ransomware Action Plan” and planned to achieve part of it using offensive cyber capabilities [1]. The Netherlands has also announced similar efforts [2]. Ransomware actors may become risk-averse and select their targets more carefully to avoid being attacked by such operations. We hope to see more ransomware groups brought down in the following year, as well, as a consequence of such operations.

[1] <https://www.homeaffairs.gov.au/cyber-security-subsite/files/ransomware-action-plan.pdf>

[2] <https://securityaffairs.co/wordpress/123113/security/the-netherlands-war-ransomware-operations.html>

### Resources

  * <https://www.cisa.gov/stopransomware>
  * <https://www.ncsc.gov.uk/ransomware/home>
  * <https://www.cyber.gov.au/ransomware>



## References

  * OpSec for Russians – <https://grugq.github.io/presentations/Keynote_The_Grugq_-_OPSEC_for_Russians.pdf>
  * A Deep Dive into Cobalt Strike Malleable C2 – <https://posts.specterops.io/a-deep-dive-into-cobalt-strike-malleable-c2-6660e33b0e0b>



##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2022/03/07/2021-year-in-review/&t=2021%20Year%20In%20Review)
  * [Share on X](https://x.com/share?text=2021%20Year%20In%20Review&url=https://thedfirreport.com/?p=5706)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2022/03/07/2021-year-in-review/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=2021%20Year%20In%20Review&url=https://thedfirreport.com/2022/03/07/2021-year-in-review/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2022/03/07/2021-year-in-review/&title=2021%20Year%20In%20Review)
  * [Share by Mail](/cdn-cgi/l/email-protection#7d420e081f17181e09404f4d4f4c584f4d24181c0f584f4d3413584f4d2f180b14180a5b5e4d4e45461f121904401509090d0e475252091518191b140f0f180d120f09531e1210524f4d4f4f524d4e524d4a524f4d4f4c5004181c0f501413500f180b14180a52)