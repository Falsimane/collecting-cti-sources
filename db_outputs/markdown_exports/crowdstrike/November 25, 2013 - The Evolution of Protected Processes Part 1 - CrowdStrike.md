# The Evolution of Protected Processes Part 1 - CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/evolution-protected-processes-part-1-pass-hash-mitigations-windows-81/
- **Date :** November 25, 2013

---

# The Evolution of Protected Processes - Part 1: Pass-the-Hash Mitigations in Windows 8.1

November 25, 2013

• [ AlexI](/en-us/blog/author.alexi/ "Posts by AlexI") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

It was more than six years ago that I [first posted](http://www.alex-ionescu.com/?p=34 "Why Protected Processes Are A Bad Idea") on the concept of protected processes, making my opinion of this poorly thought-out DRM scheme clear in the title alone: “Why Protected Processes Are A Bad Idea”. It appears that Microsoft took a long, hard look at the mechanism (granted, an impenetrable user-mode process can have interesting security benefits — if we can get DRM out of the picture), creating a new class of process yet again: the _Protected Process Light_ , sometimes abbreviated PPL in the kernel.

Unlike its “heavy” brother, the protected process light actually serves as a type of security boundary, bringing in three useful mitigations and security enhancements to the Windows platform. Over the next three or four blog posts, we’ll see how each of these enhancements is implemented, starting this week with [Pass-the-Hash](https://www.crowdstrike.com/cybersecurity-101/pass-the-hash/) (PTH) Mitigation.

We’ll talk about LSASS’ role in the Windows security model, followed by the technical details behind the new PPL model. And since it’s hard to cover any new security advancement without delving in at least a few other inter-related internals areas, we’ll also talk a little bit about Secure Boot and protected variables. Perhaps most importantly, we’ll also see how to actually enable the PtH mitigation, as it is currently disabled by default on non-RT Windows versions.

**The LSASS Process**

In Windows, local user accounts are hashed using a well-known algorithm ([NTLM](http://msdn.microsoft.com/en-us/library/windows/desktop/aa378749\(v=vs.85\).aspx)) and stored in a database called the [SAM](http://technet.microsoft.com/en-us/library/cc756748\(v=ws.10\).aspx) (Security Accounts Manager), which is in itself a registry hive file. Just like with other operating systems, a variety of offline, and online attacks exist in order to obtain, reset, or otherwise reuse the hashes that are stored in the SAM, going from the usual “Password Reset” boot [emergency disks](http://pogostick.net/~pnh/ntpasswd/), to malicious privilege escalation. Additionally, a variety of other cryptographic data is also stored in the SECURITY database, yet another registry hive file. This data includes information such as secrets, saved plain-text passwords, and more.

A process called the [Local Security Authority](http://technet.microsoft.com/en-us/library/cc961760.aspx) (LSASS) manages the run-time state of this information, and is ultimately responsible for all logon operations (including remote logon over Active Directory). Therefore, in order to obtain access to this data, two primary mechanisms are used:

1) File-based attacks: the SAM/SECURITY hives are accessed, either offline, or online through tricks such as [using Volume Shadow Copies](http://bernardodamele.blogspot.com/2011/12/dump-windows-password-hashes.html), and the hashes + secrets extracted. This mechanism has disadvantages in that the storage formats can change, detailed registry knowledge is needed, and LSASS will often obfuscate much of the data (such as plain-text cached passwords).

2) Process-based attacks: since the hash and secret data from #1 above is neatly loaded by LSASS in readable form (and accessible thanks to easy-to-use [query APIs](http://msdn.microsoft.com/en-us/library/Windows/desktop/ms721811\(v=vs.85\).aspx)), it is often much more preferable to simply inject code into the LSASS process itself, which is then used to dump hashes or secrets, as well as to create tokens based on those hashes. Additionally, researchers such as Gentil Kiwi have even discovered that LSASS contains plain-text passwords using reversible symmetric cryptography (with the key stored in the LSASS process itself). Tools now exist today to not only [pass-the-hash](http://en.wikipedia.org/wiki/Pass_the_hash), but to also pass-the-pass. In a default Windows 8 installation, both the local user account password, as well as the Microsoft Live Services password, is available in a plaintext-retrievable way.

Obviously, both this file and the process are protected such that only the SYSTEM account can access them. But once running as Administrator, this is a simple hurdle — and since most users still run as Administrators (albeit with UAC, but that’s not a security boundary), exploits only have to escape whatever local sandbox they’re running in, get admin rights, get a system token, and inject into LSASS. And of course, in a shared computer environment, another admin on the machine can get the passwords of all the users.

What’s changed in Windows 8.1? Run Mimikatz or other pass-the-hash attacks and they still work out-of-the-box. But on a Windows 8.1 RT system (supposing one can compile for ARM), they won’t — in fact, even attempting to attach a debugger to the LSASS process will fail, regardless of user-mode permissions. The title of this blog post gives it away: in Windows 8.1 RT, LSASS is now a _protected process light_. And with Registry Editor and the right key/value pair, your Windows 8.1 installation (non-RT) can take advantage of this too.

**Protected Process Light Internals**

Before taking a look at how to enable the mitigation, let’s see what makes a PPL tick. Unlike the simple “ProtectedProcess” bit in EPROCESS that I documented in Vista, a Windows 8.1 EPROCESS structure now has a “Protection” field of the following type:
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    _PS_PROTECTION
      +0x000 Level            : UChar
      +0x000 Type             : Pos 0, 3 Bits
      +0x000 Audit            : Pos 3, 1 Bit
      +0x000 Signer           : Pos 4, 4 Bits
      
  
---|---  
  
Where type can be one of the following:
    
    
    1
    2
    3
    4
    5
    

| 
    
    
    _PS_PROTECTED_TYPE
      PsProtectedTypeNone = 0n0
      PsProtectedTypeProtectedLight = 0n1
      PsProtectedTypeProtected = 0n2
      PsProtectedTypeMax = 0n3
      
  
---|---  
  
and Signer can be one of these (excited about some of these other values? future blog posts will uncover more on signers and PPLs):
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

| 
    
    
    _PS_PROTECTED_SIGNER
      PsProtectedSignerNone = 0n0
      PsProtectedSignerAuthenticode = 0n1
      PsProtectedSignerCodeGen = 0n2
      PsProtectedSignerAntimalware = 0n3
      PsProtectedSignerLsa = 0n4
      PsProtectedSignerWindows = 0n5
      PsProtectedSignerWinTcb = 0n6
      PsProtectedSignerMax = 0n7
      
  
---|---  
  
Let’s do some quick math and see if the LSASS process on my hardened Windows 8.1 system matches:

lkd> !process 0 0 lsass.exe PROCESS **ffffe000049ab900**

lkd> ?? ((nt!_EPROCESS*)**0xffffe000049ab900**)->Protection.Level

unsigned char 0x41'

Because the bits are essentially nibbles, it’s easy to read 0×41 as Lsa (0×4) + PPL (0×1). Once a process is in the PPL state, all the protections in my [previous blog post](http://www.alex-ionescu.com/?p=34 "Why Protected Processes Are A Bad Idea") are in effect — the system protects both types of protected processes in the same way, preventing any handle open for all but a few limited rights. Additionally, the memory manager will prevent loading of DLLs that are not signed appropriately, using the Code Integrity improvements in Windows 8 that I covered in [my talk](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&ved=0CDgQFjAB&url=http%3A%2F%2Fruxconbreakpoint.com%2Fassets%2FUploads%2Fbpx%2Falex-breakpoint2012.pdf&ei=r8KPUqzgCtDnoASjnYDoCw&usg=AFQjCNGNjRCsmNw-vHoRwj9gp15NB1pF1Q&sig2=O3nehmZKE5etgoXNfBbDFA&bvm=bv.56988011,d.cGU) at BreakPoint last year — something I plan to revisit in this blog at a later time.

Finally, although I didn’t mention this back in the Vista days, the [application compatibility database](http://www.alex-ionescu.com/?p=39) is also disabled for these processes — an interesting attack vector that is blocked thanks to this.

**Enabling the Pass-the-Hash Mitigation**

Now that we know about this improvement to the security architecture, how can one take advantage of it on a non-RT Windows 8.1 computer ? By looking at the updated flow of Wininit.exe, the process in charge for launching LSASS, one can see that the _[ExecSystemProcesses](https://www.alex-ionescu.com/wp-content/uploads/2013/11/execsystem.png) _routine now calls _[GetLsaProtectionLevel](https://www.alex-ionescu.com/wp-content/uploads/2013/11/getlsa.png)_ which does a registry key read of _**HKLMSYSTEMCurrentControlSetControlLsa**_ for the value **RunAsPPL**. Before reading the registry however, it also calls _[ReadLsaConfigEnvironmentVariable](https://www.alex-ionescu.com/wp-content/uploads/2013/11/readlsa.png) _– the importance of which we’ll see in a bit.

Either way, as long as one of these two things is set (the environment variable or the registry key), _[ExecSystemProcesses](https://www.alex-ionescu.com/wp-content/uploads/2013/11/execsystem.png) _will call _[StartSystemProcess](https://www.alex-ionescu.com/wp-content/uploads/2013/11/start.png) _with the CREATE_PROTECTED_PROCESS flag. In turn, the routine will utilize the new Vista Process/Thread Attribute List functionality to add attribute 0x2000B — documented as the new Windows 8.1 “[Protection Level Attribute](http://msdn.microsoft.com/en-us/library/windows/desktop/ms686880\(v=vs.85\).aspx)“. As you can expect, the level is set to 4, which matches the “LSA Signer” enumeration value above. And just like that, LSASS is now a PPL, and protected against even an admin (or even SYSTEM) attacker. And no, not even SE_DEBUG_PRIVILEGE will get you through. Clicking on any of the linked function names will reveal Hex-Rays output to match this flow.

As a side note, is this all you need to launch as process as protected light — a protection level in a new attribute? Astute readers have probably already dumped the EPROCESS for Wininit.exe by now and noticed that, it too, is a PPL process (albeit, with a different Level!). The security model isn’t stupid — a PPL can only be launched by another PPL (or a PP, which is even more protected), and there’s a hierarchy in the levels as well, which we’ll see in a later post. Obviously, this means that Smss.exe (Wininit’s parent) must also be a PPL, and evidently the kernel has been running as a Protected Process since Vista. You could call this a user-mode protected chain of trust. These processes aren’t the only PPLs — we’ll see a lot more in a future post, and their purpose and configurability.

Should you run off and set that registry key? Yes and no. Once LSASS runs as a PPL, this will break any 3rd party software that might be attempting to inject or modify LSASS state. And sadly, at work, I’ve seen a number of these. Additionally, LSASS has a number of extensibility points, some used as ASEPs by attackers, others used legitimately to provide enhanced security or cryptographic services. Without the right signature and EKU (which right now means a WHQL signature with Microsoft as the signer — not just any Authenticode garbage!), those DLLs, plugins, and extensions will stop working. In certain IT scenarios, this can be a catastrophic compatibility problem, no doubt why Microsoft has chosen to keep this disabled for now.

But on a home computer, where you know you don’t have specialized software, and you firmly believe that AV (and others) should leave your LSASS alone? I’d say go for it. A number of helpful event log entries in the Security log will warn you of any DLLs that failed to load in case you’re curious.

**Enhanced LSASS Mitigation With Secure Boot**

Leaving the endless debate and controversy around Secure Boot aside, running Windows 8.1 on an UEFI-compatible machine with Secure Boot turned on will add an additional layer of security. Set the registry key as indicated above, reboot, watch LSASS run as a PPL, and now try deleting the registry key — then reboot again. LSASS will still run as a PPL. In fact, you can even re-install Windows 8.1, and LSASS will still run as a PPL. This is because Microsoft realized — if the attacker runs as Admin/SYSTEM and can inject into LSASS, but a registry key prevents this — why wouldn’t the Admin/SYSTEM attacker simply delete the key? Outside of active-key-monitoring shenanigans (which some parts of the kernel do employ, mostly licensing), not much. And definitely an offline attacker will have no problem editing the hive directly (unless BitLocker is also active).

This changes with Secure Boot however, as Windows has the ability to use the standard UEFI system variable runtime routines and set a value directly in the firmware store using _SetFirmwareEnvironmentVariableExAPI_ (and its kernel equivalents such as the _NtSetSystemEnvironmentVariableEx_ and _ExSetFirmwareEnvironmentVariable_ routines). To be fair, this is standard UEFI behavior; what Secure Boot brings to the table is the Namespace GUID that Windows can use — which if you were paying attention you saw in the _[ReadLsaConfigEnviromentVariable](https://www.alex-ionescu.com/wp-content/uploads/2013/11/readlsa.png) _snippet earlier.

This GUID, {77FA9ABD-0359-4D32-60BD-28F4E78F784B}, is the “Protected Store” that Windows can use to store certain system properties it wants to protect. In this case, it stores a variable named _**Kernel_Lsa_Ppl_Config**_ that is associated with the _**RunAsPPL**_ value in the registry (to be 100% accurate, “it” here refers to Winload.efi, which upon loading the registry executes the [OslFwProtectSecConfigVars](https://www.alex-ionescu.com/wp-content/uploads/2013/11/wininit.png) routine). As soon as this variable is set, the registry values no longer matter — PPL is enabled for LSASS.

What prevents a user from simply deleting this variable, or setting it to zero? Witness the following snippet in the _NtSetSystemEnvironmentVariableEx_ system call, which executes for user-mode callers:
    
    
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    

| 
    
    
    i = 0;
    while (VendorGuid<i> == ExpSecureBootVendorGuid<i>)
    {
        ++i;
        if (i == 4)
        {
            if (!_wcsnicmp(CapturedVarName, L"Kernel_", 7))
            {
                ExFreePoolWithTag(CapturedVarName, 0#41;;
                return STATUS_ACCESS_DENIED;
            }
            **break** ;
        }
    }
      
  
---|---  
  
The intent is clear — any variables stored in the Secure Boot GUID, that start with Kernel_, are inaccessible from userspace — meaning that no Windows application can attempt to reset the protection. In fact, the only way to reset the protection is to boot into a [special UEFI application](http://www.microsoft.com/en-us/download/details.aspx?id=40897) written by Microsoft, which will wipe the environment variable based on the user’s input. An impressive security boundary, to say the least.

**Conclusion**

At the end of the day, what does running as PPL really mean for your system? Based on the limited access rights that protected processes (and PPLs) provide, a process, regardless of its token, can no longer open a handle for injection and/or modification permissions toward the LSASS process. Since this is critical for injecting the DLLs and/or threads that process-based PtH tools use, their use is thwarted. Additionally, attempts to load DLLs into LSASS through other means (such as AppInit_DLLs or LSA extensions) are also blocked, since the required digital signatures are missing. It’s important to mention that file-based hash attacks are not affected by these enhancements — at the end of the day, if someone has local console access to your unlocked, non-encrypted machine, it’s not your machine anymore.

With Windows 8.1, Protected Processes have evolved — taking on additional capabilities and now working to enhance security and protect users, instead of doing the bidding of the MPAA. One such new capability is the Pass-the-Hash mitigation and general hardening of the LSASS process — but there are a lot more. It’s one of the first of many general security and cryptographic enhancements in Windows 8.1 which provide additional boundaries around Microsoft’s code — separating it from other people’s code. But just like Apple’s entitlement system, it’s not a fully walled garden. Further posts will explore not only additional uses of PPLs by Windows’ own binaries, but also (supported) options available for 3rd parties.

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)