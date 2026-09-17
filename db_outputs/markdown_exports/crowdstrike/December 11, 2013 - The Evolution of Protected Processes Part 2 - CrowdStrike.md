# The Evolution of Protected Processes Part 2 - CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/evolution-protected-processes-part-2-exploitjailbreak-mitigations-unkillable-processes-and/
- **Date :** December 11, 2013

---

# The Evolution of Protected Processes Part 2: Exploit/Jailbreak Mitigations, Unkillable Processes and Protected Services

December 11, 2013

• [ AlexI](/en-us/blog/author.alexi/ "Posts by AlexI") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

In this continuing series on the improvements of the protected process mechanism in Windows, we’ll move on past the single use case of

[LSASS protection and pass-the-hash mitigation](http://www.alex-ionescu.com/?p=97 "The Evolution of Protected Processes Part 1: Pass-the-Hash Mitigations in Windows 8.1")

through the Protected Process Light (PPL) feature, and into generalized system-wide use cases for PPLs. In this part, we’ll see how Windows uses PPLs to guard critical system processes against modification and how this has prevented the Windows 8 RT jailbreak from working on 8.1. We’ll also take a look at how services can now be configured to run as a PPL (including service hosts), and how the PPL concept brings yet another twist to the unkillable process argument and semantics. **System Protected Processes** To start the analysis, let’s begin with a simple WinDBG script (you should collapse it into one line) to dump the current PID, name, and protection level of all running processes: 

| 
    
    
    lkd> !for_each_process "
    r? @$t0 = (nt!_EPROCESS*) @#Process;
    .if @@(@$t0->Protection.Level) 
    {
    .printf /D "%08x <b>  
  
---  
  
[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)