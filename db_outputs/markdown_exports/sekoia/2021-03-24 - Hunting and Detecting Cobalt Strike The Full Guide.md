# Hunting and Detecting Cobalt Strike: The Full Guide

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/hunting-and-detecting-cobalt-strike
- **Date :** 2021-03-24

---

In the [last](https://medium.com/@Sekoia_team/analysis-and-detection-of-mitm-phishing-attacks-bypassing-2fa-o365-use-case-cf0ffdae9cae) Sekoia Threat & Detection Lab we dealt with a Man-in-the-middle (MITM) phishing attack leveraging Evilginx2, an offensive tool allowing two-factor authentication bypass. Here, we are tackling a much bigger threat given the frequency it is abused by diverse threat actors. In this blog post, we describe step by step how to ensure a **proactive and defensive posture** against Cobalt Strike, one of the most powerful pentesting tools hijacked by attackers in their numerous [campaigns](/blog/log4shell-the-defenders-worst-nightmare). We show examples of how to track Cobalt Strike command and control servers (C2) and Malleable profiles by focusing on their SSL certificates and HTTP responses. We also describe ways to detect: (i) Cobalt Strike payloads such as the DNS beacon based on the nature and volume of Cobalt Strike DNS requests, (ii) Cobalt Strike privilege escalation with the Cobalt Strike built-in service svc-exe, (iii) Cobalt Strike lateral movement with the Cobalt Strike built-in service PsExec and (iv) Cobalt Strike beacons communication through named pipes.

## Why should defenders focus on Cobalt Strike hunting and detection ?

What do [APT29](/blog/nobeliums-envyscout-infection-chain-goes-in-the-registry-targeting-embassies), APT32, APT 41, APT19, UNC2452, FIN6, Wizard Spider and most of the cybercriminals have in common in their toolset?

![Figure: example of threat actors leveraging Cobalt Strike in their attacks](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a35531_6a92a4044b4041c69342ebd0_6a2a7aaf7807cafb511315c0.webp)

Example of threat actors leveraging Cobalt Strike in their attacks

Well, as shown on the figure above, the answer is Cobalt Strike.

### What is Cobalt Strike ?

Cobalt Strike is a commercial, post-exploitation agent, designed to allow pentesters to execute attacks and emulate post-exploitation actions of advanced threat actors. It aims at mimicking threat actors’ tactics, techniques and procedures to test the defenses of the target. However, over the last years, it’s purposes were hijacked by attackers who managed to crack its official versions and leverage them in their attacks thus taking advantage of Cobalt Strike’s remote access and defense evasion capabilities. 

Cobalt Strike is now widely being used by threat actors regardless of their capabilities, skill sets, the sophistication of their attacks or the objectives of their campaigns. To mention just a few examples, it has been leveraged in the recent advanced and state-sponsored [SolarWinds supply chain attacks](https://www.microsoft.com/en-us/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/), as well as in the frequent and offensive campaigns conducted by different [cybercriminal groups](/blog/ongoing-roaming-mantis-smishing-campaign-targeting-france) such as [Wizard Spider](https://thedfirreport.com/2021/01/31/bazar-no-ryuk/) (see also [Trickbot](https://thedfirreport.com/2021/01/11/trickbot-still-alive-and-well/)), and the [Egregor group](https://www.sentinelone.com/labs/egregor-raas-continues-the-chaos-with-cobalt-strike-and-rclone/) ultimately delivering ransomware payloads.

In 2020, it was seen as one the most leveraged pentesting tools by attackers, alongside Mimikatz and PowerShell Empire. Overall, in Q4 of 2020, 66% of all [ransomware attacks](/blog/an-insider-insights-into-conti-operations-part-two) involved [Cobalt Strike payloads.](https://blog.talosintelligence.com/ctir-quarterly-trends-q4-2020/)

Therefore, all these data highlight our need as a defender to be aware and up to date regarding the threat posed by the use of Cobalt Strike for malicious purposes.

## In a few words, how does Cobalt Strike work?

Cobalt Strike works in a client/server mode. The server is known as the Team Server, it runs on a Linux system, controls the beacon payload and receives all information from the infected hosts. The client software (known as the Aggressor) runs on multiple operating systems and enables the user to connect to different Team Servers in order to configure the beacon, deliver the payload and fully use all of Cobalt Strike’s features remotely.

Beacon is the Cobalt Strike payload, highly configurable through the so-called “Malleable C2 profiles” allowing it to communicate with its server through HTTP, HTTPS or DNS. It works in asynchronous or interactive mode, and can build stageless or staged payload, offering overall considerable flexibility.

Once connected to its C2 server, the user configures a “listener” (HTTP, DNS …) and a stageless or staged beacon (Windows PE, PowerShell …). The beacon delivery can be directly achieved from the Cobalt Strike server or through another user tool.

This tool is straightforward to use and very [well documented](https://www.cobaltstrike.com/support) which explains its increasing popularity.

To adopt a proactive posture and protect our customers from attacks leveraging Cobalt Strike, we have focused on both tracking Cobalt Strike servers and implementing up-to-date rules capable of detecting each version of Cobalt Strike.

Attacks performed with leaked versions of Cobalt Strike are generally carried out with old versions depending on how easy it is to find these leaks. For this lab session we chose to use the version 4.2 (released the 06/11/2020), which has been leaked on hacker forums and was easy to stumble upon.

The latest 4.3 version was just released (03/03/2021). Aside from the usual new features and bug fixes for each release, we have witnessed some efforts to fix the most specific technical details that help detect Cobalt Strike. We discuss some of them in this article, but it is undoubtedly a never ending game.

## This is how we hunt for Cobalt Strike C2 servers

We currently possess more than 50 trackers for Cobalt Strike C2 servers and Malleable profiles, which enabled us to feed, with high confidence, our Intelligence database with more than 10.000 IPs in 2020, that detected Cobalt Strike intrusions. To know more about our hunting results, you can read our analysis following this link.

You will find below an example of three features you can track to spot Cobalt Strike servers. Several trackers are valid for old versions of Cobalt Strike. But as you will notice when considering the number of servers we still detect by dint of these trackers, they are still effective. As said previously, threat actors usually use leaked versions which are not necessarily the most recent ones.

## Keep a close eye on default certificates

Cobalt Strike servers come with a default certificate displaying specific values for the serial number, the issuer, the subject and the certificate validity as shown below.

![Extract of a default Cobalt Strike certificate, the relevant information is highlighted in white color.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a3552e_6a92a4033e6167cebbf6cb8a_6a2a7aaf7807cafb511315bb.webp)

Extract of a default Cobalt Strike certificate, the relevant information is highlighted in white color.

If they have not been modified by the attackers, these servers can be easily spotted using a shodan request. At the time of writing, 700 servers match this certificate serial number.

![Example of Cobalt Strike servers with default certificate](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a3551b_6a92a4076568d7e2b4095274_6a2a7ab07807cafb511315ce.webp)

Example of Cobalt Strike servers with default certificate

## What does the HTTP response tell us?

For Cobalt Strike versions prior to [version 3.13](https://download.cobaltstrike.com/releasenotes.txt), the http response displays an extraneous space at the end of the http status.

![Figure: the extraneous space is highlighted in black](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a35524_6a92a3ffa2f46752fd01ffd3_6a2a7aaf7807cafb511315ae.webp)

The extraneous space is highlighted in black

At the time of writing, we can still catch 30 servers using this tracker. The same detection could be done using Snort rules.

## Let’s check a malleable C2 profile

As mentioned earlier, Malleable C2 profiles allow to customize Cobalt Strike, which also means that some public configuration could be used to track C2 servers.

Here is an example of a malleable C2 profile, with a [self-signed certificate](https://github.com/rsmudge/Malleable-C2-Profiles/blob/master/normal/microsoftupdate_getonly.profile) that we can hunt using shodan.

![The relevant information is highlighted in white](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a3551e_6a92a4008d1115926b208b50_6a2a7aaf7807cafb511315b1.webp)

The relevant information is highlighted in white

The certificate issuer information (common name, organization, organization unit, location, and country) matched with 116 servers online in 2020.

## How can we detect Cobalt Strike with our SIEM?

We performed some attacks using Cobalt Strike beacons in laboratory conditions, so we could figure out [some ways to detect it with our SIEM Sekoia](/solutions/siem-replacement).

For this blog post, we chose to focus on an attack that was carried out using a DNS beacon as a first stage listener and the SMB beacon for lateral movement. We then managed to detect each step using either Cobalt Strike leaked source code or the generated logs.

To detect it using the following rules you will need to have access these events logs:

  * Microsoft-Windows-Sysmon/Operational (and the relevant symon config, especially for Named Pipe)
  * Microsoft-Windows-Windows Defender/Operational (or any other AntiVirus logs)
  * DNS and Proxy logs



Here is an explanation of rules that can be implemented into your [SIEM](/glossary/siem) to specifically detect this attack.

DNS beaconing is a very useful feature, which allows to bypass any other HTTP filtering or proxy inspection that may exist in the targeted company.

Last year the Cobalt Strike source code (4.0 version) was leaked, and a security researcher quickly spotted some interesting characteristics for DNS beaconing: 

The mentioned source code reveals that Cobalt Strike is using three constant DNS labels in pair with DNS question type: “cdn” for A type, “api” for TXT type and “www6” for AAAA type. That means that at some point when the beacon will try to reach its C2 server, aside from two random labels and the one chosen by the user, that constant string will be used: it is very convenient in terms of detection and enables us to build this kind of rule:

`(dnsquery.value LIKE ‘www6.%’ AND dnsquery.type = ‘AAAA’) OR (dnsquery.value LIKE ‘cdn.%’ AND dnsquery.type = ‘A’) OR (dnsquery.value LIKE ‘api.%’ AND dnsquery.type = ‘TXT’)`

Using this rule we were able to detect the first stage of our attack that leveraged the DNS beacon as shown below.

![Alert displayed on Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a3553d_6a92a40563e0c17b5dad943a_6a2a7ab07807cafb511315c8.webp)

Alert displayed on Sekoia

The rule needs some exceptions (_e.g._ cdn.onenote.net, cdn.fwupd.org) in order to avoid possible false positives in your DNS traffic, but seems reliable. Latest Cobalt Strike 4.3 version brings new options to override the default values through a [Malleable C2 profile](https://download.cobaltstrike.com/releasenotes.txt). With the previous versions attackers will need to modify the source code or patch their beacon binaries.

## Beaconing network traffic

Another behavior that can be detected relies on the interval value between two beacon network requests, which has no “sleep” time by default. This configuration could be modified with a Malleable C2 profile. Therefore, working with Cobalt Strike in interactive mode will generate a considerable amount of network requests especially with some beacon (_e.g._ DNS) when it comes to downloading/uploading files. That could be leveraged for detection using classical behavior rules.

During our attack, we observed that for both DNS and HTTP beacons, even with only the beacon activity (no exfiltration or command), the total DNS/HTTP requests from the infected host exceeded 200 requests by minutes.

The rule could take this form:

`selection DNS/HTTP requests | count() by minute src_ip > 200`

## Detects when an attacker elevate its privileges using svc-exe and move laterally using PsExec

We managed to elevate our privileges within the victim system. We chose to achieve this using svc-exe, which is a built-in Cobalt Strike exploit. 

It will drop an executable that runs a payload, create a service to run it, assume control of the payload, and cleanup the service and executable. Thus allowing us to get SYSTEM.

![Privilege elavation configuration](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a35521_6a92a401e9a71d4228405a8d_6a2a7aaf7807cafb511315b4.webp)

Privilege elavation configuration

Then, we wanted to perform a lateral movement and jump to the new targeted host. We chose to do so leveraging an SMB beacon which is a good candidate frequently leveraged in attacks.  
We ran a command on Cobalt Strike that leverages psexec64 as follows:

`$ jump psexec64 <host-ip> <name-of-our-SMB-beacon-listener>`

This is one of the features that make Cobalt Strike a strong and efficient tool. It relies on native Windows APIs and not a third-party protocol stack, thus increasing its defense evasion capabilities. Hence, Cobalt Strike has a built-in PsExec, which strength lies in its ability to launch interactive command-prompts on remote systems. It can be run on the victim’s system since it uses native Windows components. 

![Logs events displayed on Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a35534_6a92a406fd507e2a51b99f70_6a2a7ab07807cafb511315cb.webp)

Logs events displayed on Sekoia

We observed that these operations resulted in a service creation. They both spawned rundll32.exe that initiated a network connection, which is the event ID 3 of the Microsoft-Windows-Sysmon/Operational journal. What makes it different from the usual behavior of rundll32, is that the dll is run without any command line arguments.

This behavior is anchored in Cobalt Strike. Unless attackers wisely decide to change this configuration in the source code, this surely will spot many other attacks.

## Pipes to detect them all

A pipe is a section of shared memory that processes use for communication. The process that creates a pipe is the pipe server. The one that connects to a pipe, is the pipe client. A process writes information to the pipe, while the other process reads the information from the pipe.

There are two types of pipes: named and anonymous pipes.

Named pipes are one-way or duplex pipes that are used for network interprocess communication that can take place between a pipe server and one or more pipe clients. Multiple pipe clients can use the same named pipe simultaneously in the same instance. 

Anonymous pipes are unnamed, one-way pipes that are used for interprocess communications between a parent and a child process, only on a local computer. 

Cobalt Strike has the ability to pivot over named pipes. It uses pipes to allow a beacon to receive its commands and send its ones to another beacon. In this situation, both beacons will communicate over pipe channels as highlighted by the orange arrow in the pivot graph shown below. Cobalt Strike also uses TCP sockets and SSH sessions to connect a beacon session to another.

![Cobalt Strike’s pivot graph](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a35537_6a92a3fe3e6167cebbf6c655_6a2a7aad7807cafb51131598.webp)

Cobalt Strike’s pivot graph

Hence, when we connected a listener (_e.g._ DNS beacon) with another beacon (_e.g._ SMB beacon) to perform lateral movement, we observed the creation of the sysmon event ID 17 “Pipe created”, in our logs. 

![Logs events displayed on Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a35528_6a92a4084c776939a1e0df51_6a2a7ab07807cafb511315fb.webp)

Logs events displayed on Sekoia

During our various tests, we observed that the created pipe displayed the same pattern that can be detected by this regex:

`MSSE-[0-9]{4}-server`

Cobalt Strike users cannot change the default value of these pipes without accessing and modifying the source code configuration of Cobalt Strike.  
It is important to distinguish the pipes that are created to allow beacons to communicate, from the named pipes that are generated specifically for the SMB beacon, and which default value is in the form of: _msagent_39_ as shown below. Unlike the MSSE pipes, the default value of the pipe name of the SMB beacon can be easily modified on the attack interface.

![Default Pipename for SMB beacon](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a63c51d97c29d2a3552b_6a92a402fc97352943872ce4_6a2a7aaf7807cafb511315b7.webp)

Default Pipename for SMB beacon

## Default payload

For a lot of user interactions, Cobalt Strike displays a default value, and especially for the payload naming. Of course it is a very weak detection indicator, but a mistake is always possible and defenders only need one.  
During our lab tests with different use cases, we had theses default binaries names:

`beacon.{bin|exe|dll|ps1}, artifact.{dll|exe}, payload.{java|ps1|py|rb|vba}`

Anti-virus logs at that point could also be an easy win: most AVs have specific signatures that could be used to trigger an alert in your SIEM, and detect an attacker who forgot to use its custom payload.  
More globally, binaries’ other characteristics (on disk or in memory), could also be used as detection indicators. That is why Cobalt Strike’s editor advises to customize it with a Malleable C2 profile or the Artifact Kit [10].   
Many public [Yara rules](/blog/playbooks-yara-rules-iocs-explanation-about-the-news) exist in order to precisely do that, and try to follow [existing payload available in the wild](https://maynier.eu/blog/2020/12/20/analyzing-cobalt-strike-for-fun-and-profit/). This is recommended if you have an [EDR](/blog/xdr-is-not-edr) capability.

## How to mitigate Cobalt Strike?

As said before, most of Cobalt Strike beacons characteristics can be customized. Either directly on the user interface for some of them, through a malleable profile or by directly reversing the source code. Hence, it is essential to be as exhaustive as possible regarding the detection capacity.

Furthermore, it seems that Cobalt Strike designer made it one of its priority to always ensure that its tool can not be detected, releasing a new version each time the last version was well documented by defenders. Highlighting for us the need to be up to date regarding the new versions characteristics. Since, attackers mostly used leaked versions, we are still a step ahead in detecting the latest threats.

Given the volumes of attacks performed with Cobalt Strike, combining both C2 server hunting and beacon detection as shown in this article, is definitely a good way to ensure the best protection and tighten the net around that threat.

  1. **Use a real-time detection solution** : To be protected against it, we highly recommend you to rely on a real-time detection solution fuelled by cyber threat intelligence.**‍**
  2. **Carry out memory forensics** : If you have been infected by Cobalt Strike, it is recommended to carry out memory forensics. The tool CobaltStrikeScan available on github scan for files and process memory for Cobalt Strike beacons and parse their [configuration](https://github.com/Apr4h/CobaltStrikeScan). It scans Windows process memory for evidence of DLL injection.**‍**
  3. **Besides having an up-to-date SIEM, there are also these evident course of actions that defenders could leverage:** Cobalt Strike can be dropped in victims systems following [phishing campaigns](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers) leveraging VBS scripts. It is recommended to disable document macro in MS office. Training users to notice malicious emails should also be performed on a regular basis.  
Cobalt Strike payload can be delivered as a powershell script. It is recommended to restrict powershell script execution to allow signed scripts only.  
Some Cobalt Strike payload signatures can be identified by antivirus. It is recommended to have a good antivirus product.  
Cobalt strike beacons generate abnormal behaviors that can be hunted using Sysmon, Security, PowerShell and WMI logs.  
It is recommended to hunt for parent processes spawning unexpected child processes.  
Monitor suspicious modifications to registry keys, startup folders, task scheduler and service execution.