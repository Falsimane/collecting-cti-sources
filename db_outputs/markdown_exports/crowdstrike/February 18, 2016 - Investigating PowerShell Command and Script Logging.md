# Investigating PowerShell: Command and Script Logging

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/investigating-powershell-command-and-script-logging/
- **Date :** February 18, 2016

---

# Investigating PowerShell: Command and Script Logging

February 18, 2016

• [ ChadT](/en-us/blog/author.chadt/ "Posts by ChadT") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


PowerShell is becoming ubiquitous in the Microsoft ecosystem, and, while it simplifies administration, it opens up a nearly unprecedented suite of capabilities for attackers. Nearly every malicious activity imaginable is possible with PowerShell: privilege escalation, credential theft, lateral movement, data destruction, persistence, data exfiltration, and much more. Malicious PowerShell is being used in the wild, and CrowdStrike has seen an uptick in the number of advanced adversaries employing it during breaches. Dmitri Alperovitch wrote about one of these actors, Deep Panda, in his [article](/en-us/blog/deep-thought-chinese-targeting-national-security-think-tanks/) “Deep in Thought: Chinese Targeting of National Security Think Tanks.” Attackers are leaning more on PowerShell because it is readily available and gets the job done with an added bonus of leaving behind almost no useful forensic artifacts. Jaron Bradley and I previously tackled the subject of command-line auditing in the [CrowdCast](https://vimeo.com/100442934), “What Malware? Hunting Command Line Activity”. I am pleased to report that there have been some significant upgrades to command line logging since that webcast. 

### **Process Creation Events**

Starting with Server 2012R2, Microsoft released a new group policy setting to enable the recording of full command lines in Process Tracking audit events. When released, logging was restricted to Windows 8.1 and Server 2012R2 systems, but it has since been back-ported due to popular acclaim. With the proper patches, any modern Windows system (Win7 and newer) can now enable this feature. One caveat to this significant upgrade is that you still need to enable Process Tracking creation in your audit policy. In fact, Event ID 4688 (Process Creation) is used to record the command lines (see Figure 1). Historically, this has been a tough sell due to the number of events generated, but, even without command line information, these events can be very useful when hunting or performing incident response. We have seen this implemented successfully in multiple large environments through the use of centralized logging. If you do not have this enabled on your sensitive networks, you should absolutely consider it -- before you need it. You can reference the Microsoft Technet article [here](https://technet.microsoft.com/en-us/library/dn535776.aspx). **

[![Event4688_Powershell_Encoded_Final](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/02/Event4688_Powershell_Encoded_Final.jpeg)](/content/dam/crowdstrike/www/en-us/wp/2016/02/Event4688_Powershell_Encoded_Final.jpeg)

** Figure 1: Process creation event recording executed command line 

### **PowerShell Auditing**

I am still astonished that something as omnipotent as PowerShell was baked into the world’s most common operating system without security ramifications being considered or adequate security controls provided. Restricting access to PowerShell is notoriously difficult. As an example, the PowerShell Empire project has a capability to inject the required .NET assemblies into memory, allowing PowerShell functionality even if PowerShell.exe has been removed or blocked on the system. Perhaps the only way to truly prevent malicious PowerShell activity is to stop an attacker from achieving administrative privileges. Since that has proven extremely difficult in most networks, detection is currently your best bet. Unfortunately, until recently, PowerShell auditing was dismal and ineffective. A module logging capability has been present since PowerShell v3, but it is difficult to instrument and very unlikely to be used in most organizations. It was not until the recent PowerShell v5 release that truly effective logging was possible. 

### **All Hail Script Block Logging!**

A script block can be thought of as a collection of code that accomplishes a task. Script blocks can be as simple as a function or as full-featured as a script calling multiple cmdlets. Script block auditing captures the full command or contents of the script, who executed it, and when it occurred. Audits are recorded as event log entries in the Microsoft-Windows-PowerShell/Operational log regardless of how PowerShell was executed – from a command shell, the integrated scripting environment (ISE), or via custom hosting of PowerShell components. Event ID 4104 records the script block contents, but only the first time it is executed in an attempt to reduce log volume (see Figure 2). [![PowerShellLogging](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/02/PowerShellLogging.jpeg)](/content/dam/crowdstrike/www/en-us/wp/2016/02/PowerShellLogging.jpeg) Figure 2: PowerShell v5 Script Block Auditing 

Needless to say, script block auditing can be incredibly helpful when trying to piece together evil PowerShell activity. While logging is not enabled by default, the PowerShell team did sneak in the facility to identify potentially malicious script blocks and automatically log them in the PowerShell/Operational log, even with script block logging disabled. Hence, in environments running PowerShell v5, you should start seeing actionable information populating the Microsoft-Windows-PowerShell/Operational log by default. That, of course, is the only rub – you need to upgrade to PowerShell version 5 to partake. But there is great hope on the horizon for those who get there. 

Learn more about the CrowdStrike Falcon® platform and get full access to CrowdStrike's next-gen antivirus solution for 15 days by visiting the [**Falcon Prevent free trial page**](/content/crowdstrike-www/locale-sites/us/en-us/resources/free-trials/try-falcon-prevent/?ctm_source=Website&ctm_medium=Blog&ctm_campaign=Blog-Inline-Copy).

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)