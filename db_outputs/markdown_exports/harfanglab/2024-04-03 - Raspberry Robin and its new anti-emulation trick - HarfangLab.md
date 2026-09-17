# Raspberry Robin and its new anti-emulation trick - HarfangLab

- **Source :** harfanglab
- **URL :** https://harfanglab.io/insidethelab/raspberry-robin-and-its-new-anti-emulation-trick/
- **Date :** 2024-04-03

---

Reported for the first time by [Red Canary](https://redcanary.com/threat-detection-report/threats/raspberry-robin/) in 2021, Raspberry Robin was the 9th most prevalent threat in 2023 according to their “2024 Threat Detection Report”. Starting as a worm, it evolved to become an initial access broker for other threat actors. The success of Raspberry Robin comes from its constantly evolving evasion capabitilies, making it difficult to analyze and detect.

Despite Raspberry Robin being regularly analyzed by various vendors such as [Check Point](https://research.checkpoint.com/2024/raspberry-robin-keeps-riding-the-wave-of-endless-1-days/) and [Avast](https://decoded.avast.io/janvojtesek/raspberry-robins-roshtyak-a-little-lesson-in-trickery/), our team discovered a recent variant featuring interesting and as-of-yet unknown anti-emulation techniques.

## Windows Defender Emulator

During the Black Hat edition of 2018, Alexei Bulazel presented his work on the “Windows Defender Emulator” in a talk titled [“Windows Offender: Reverse Engineering Windows Defender’s Antivirus Emulator”](https://i.blackhat.com/us-18/Thu-August-9/us-18-Bulazel-Windows-Offender-Reverse-Engineering-Windows-Defenders-Antivirus-Emulator.pdf).

This talk was an extensive analysis of the Windows Defender emulator internals. A slide seems to have caught the threat actors’ and Red Teamers’ attention:

![Presentation by Alexei Bulazel of artefacts in the Windows Defender Emulator](https://harfanglab.io/medias/2024/04/vdll-artefact.png) Presentation by Alexei Bulazel of artefacts in the Windows Defender Emulator

## In the wild exploitation history

The first mention of a malware checking the then-published Defender emulator artifact is Arkei Stealer, reported in 2018 by [Siber Vatan](https://www.sibervatan.org/raporlar/dosya/c7a2abcf-1152-4c6b-8a89-8116896febc5.pdf)

![Analysis of Arkei stealer Windows Defender Emulator bypass showing the use of GetComputerNameA and GetUserNameA functions and comparing the output with  the emulator artefacts JohnDoe and HAL9TH](https://harfanglab.io/medias/2024/04/arkei-stealer.png) Analysis of Arkei stealer Windows Defender Emulator bypass

The anti-emulation technique spotted in Arkei was a string comparaison between:

  * The computer name and “HAL9TH”
  * The username and “JohnDoe”



Indeed, in the “Windows Defender Emulator”, the Windows API function `GetComputerName` always returns `HAL9TH` and `GetUsername` the string `JohnDoe`.

Between 2018 and 2022, this technique seemed restricted to stealers and was observed in [Oski](https://www.sibervatan.org/raporlar/dosya/eaa214dc-74d9-41ae-b50d-928049776662.pdf), [Mars](https://3xp0rt.com/posts/mars-stealer/), [StealC](https://www.vmray.com/cyber-security-blog/stealc-a-new-stealer-emerges-in-2023/), [Vidar](https://asec.ahnlab.com/en/44554/), [LOBSHOT](https://www.elastic.co/security-labs/elastic-security-labs-discovers-lobshot-malware) and [Qbot](https://www.trellix.com/blogs/research/demystifying-qbot-malware/). In the latter, Trellix researchers found in 2022 that Qbot was using a new way to detect the Windows Defender emulator.

![Trellix analysis of Qbot showing the use of a new anti-emulation technique](https://harfanglab.io/medias/2024/04/qbot.png) Trellix analysis of Qbot showing the use of a new anti-emulation technique

Instead of checking the current computer and username, Qbot looked for the existence of an emulator-specific file, `C:\INTERNAL\__empty`. If at first glance this check seemed original, this artefact was also disclosed in Bulazel’s talk.

![Slide showing "C:\\INTERNAL\\__empty" in the listed files available in the Window Defender Emulator](https://harfanglab.io/medias/2024/04/vfs.png) Slide showing “C:\INTERNAL\\__empty” in the listed files available in the Window Defender Emulator

## The Raspberry Robin innovation

During an incident detected at one of our clients’, we came across a Raspberry Robin distributor acting as a crack/keygen website.

![Screenshot of a Raspberry Robin distributor website](https://harfanglab.io/medias/2024/04/distribution-platform.png) Screenshot of a Raspberry Robin distributor website

Instead of the advertised piracy software, the website provides zip files containing SFX (self-extracting) archives. The website offers the same file no matter what “crack/keygen” software the user chooses.

Once one of them is executed, 3 malware samples are dropped: two stealers (Pony and AZORULT) and Raspberry Robin. The latter is dropped as a `.cpl` file named `keygen-step-2.cpl`.

![Execution flow of fake cracks distributed on keygenguru\[.\]com](https://harfanglab.io/medias/2024/04/crack-execution-flow.png) Execution flow of fake cracks distributed on “keygenguru[.]com”

When executed, the program runs multiple anti-emulation/sandbox checks. However, one of the checks caught our attention:

![Import of a non-existing function in kernel32](https://harfanglab.io/medias/2024/04/imported-function-vdll.png) Import of a non-existing function in kernel32

The malware tries to dynamically import the function `MpVmp32Entry` from `Kernel32.dll` and if the import succeeds, then the malware exits. However, this function doesn’t normally exist in Kernel32.

Bulazel’s presentation introduced the concept of VDLL. VDLLs are modified Windows system DLLs available only in the emulator, and such DLLs may export functions that don’t otherwise exist (shown in yellow below):

![Presentation by Alexei Bulazelof of VDLL functions](https://harfanglab.io/medias/2024/04/vdll-functions-exported-emulator.png) Presentation by Alexei Bulazelof of VDLL functions

The function `MpVmp32Entry` starts with `Mp`, which indicated that it could be one of the functions available only in the VDLL version of `Kernel32.dll`. We extracted the Kernel32 VDLL from the emulator in order to analyze its exports and found out that this function is indeed exported by the VDLL:

![MpVmp32Entry function available in the Kernel32 VDLL](https://harfanglab.io/medias/2024/04/mpvmp32entry-exported.png) “MpVmp32Entry” function available in the Kernel32 VDLL

Later on, we analyzed a new sample from the same website and discovered that the VDLL function check performed by the malware was different. This time the imported VDLL function used for anti-emulation was `MpReportEventEx`. However, unlike `MpVmp32Entry`, the function `MpReportEventEx` is listed in Bulazel’s presentation.

Raspberry Robin seems to be the first malware to use VDLL specific function import as an anti-emulation trick and could exploit more advanced anti-Defender emulator trick in the future.

In order, to evade IOC-based detection, the Raspberry Robin sample distributed by this website is changed (probably re-packed) every 30 minutes (at the minutes 15 and 45 of every hour). This likely means that a Raspberry Robin sample distributed on this website exists only for 30 minutes. This short lifespan leads to an absence of results when reseaching information based on the file hash making the hunt a little bit harder for the researcher.

## Potential Windows Defender emulator artifacts used for anti-emulation

### Files and directories
    
    
    aaa_TouchMeNot_
    _TouchMeNot_
    __empty
    C:\myapp.exe
    C:\Mirc
    C:\Mirc\mirc.ini
    C:\Mirc\script.ini

### Strings
    
    
    HAL9TH
    JohnDoe
    MpSockVendor
    MPGoodStatus
    MpDisableSehLimit

### VDLL exports
    
    
    NtControlChannel
    ObjMgr_ValidateVFSHandle
    ThrdMgr_GetCurrentThreadHandle
    ThrdMgr_SaveTEB
    ThrdMgr_SwitchThreads
    VFS_CopyFile
    VFS_DeleteFile
    VFS_DeleteFileByHandle
    VFS_FileExists
    VFS_FindClose
    VFS_FindFirstFile
    VFS_FindNextFile
    VFS_FlushViewOfFile
    VFS_GetAttrib
    VFS_GetHandle
    VFS_GetLength
    VFS_MapViewOfFile
    VFS_MoveFile
    VFS_Open
    VFS_Read
    VFS_SetAttrib
    VFS_SetCurrentDir
    VFS_SetLength
    VFS_UnmapViewOfFile
    VFS_Write
    MpAddToScanQueue
    MpCreateMemoryAliasing
    MpCallPostEntryPointCode
    MpCallPreEntryPointCode
    MpDispatchException
    MpExitThread
    MpFinalize
    MpGetCurrentThreadHandle
    MpGetCurrentThreadId
    MpGetLastSwitchResult
    MpGetPseudoThreadHandle
    MpGetSelectorBase
    MpGetVStoreFileHandle
    MpHandlerCodePost
    MpIntHandler
    MpIntHandlerParam
    MpIntHandlerReturnAddress
    MpNtdllDatatSection
    MpReportEvent
    MpReportEventEx
    MpReportEventW
    MpSehHandler
    MpSetSelectorBase
    MpStartProcess
    MpSwitchToNextThread
    MpSwitchToNextThread_WithCheck
    MpSwitchToNextThread_NewObjManager
    MpTimerEvent
    MpTimerEventData
    MpUfsMetadataOp
    MpValidateVFSHandle
    MpVmp32Entry
    MpVmp32FastEnter

## Indicators of compromise (IOCs)

Associated IOCs are also [available on our GitHub repository](https://github.com/HarfangLab/iocs/blob/main/raspberryrobin/).

### Hashes (SHA-256)
    
    
    242851abe09cc5075d2ffdb8e5eba2f7dcf22712625ec02744eecb52acd6b1bf|keygen-step-2.cpl (Raspberry Robin)
    483adf61d7d932003659d5d6242eace29ea8416ec810749333793e0efa91610d|keygen-step-2.cpl (Raspberry Robin)
    50158e22481acabc56d8e3d318d6d709fcb7a9e442e76157b518d19e13f8e520|keygen-step-2.cpl (Raspberry Robin)
    93672d67e8100bb984f866888cb042727567d302b30b91356a2b2bc8cd3f7912|keygen-step-2.cpl (Raspberry Robin)
    b5637231e25aa7da8fe925f5b97a2ccbfd082a5463b2a05d2b3221adb35e43d9|keygen-step-2.cpl (Raspberry Robin)
    b81e857427411577552d1ecdd444efaeab23ec903192812d40ab3dd69df98ec5|keygen-step-2.cpl (Raspberry Robin)
    c8d37df88009122c890cb95dc79d895d39339fe1efdcfa5e033d0aea171ffc3d|keygen-step-2.cpl (Raspberry Robin)
    10b4b7e9469366bfe459c3cd674aeab0692cfd9272fe369ef56d2811623e4866|keygen-step-2.cpl (Raspberry Robin)

### Hostnames
    
    
    keygenguru[.]com|Raspberry Robin distribution platform

### PE information
    
    
    hrtbddd69.dll|DLL name in keygen-step-2.cpl export table
    OsTlhtlohe|Exported function in keygen-step-2.cpl

## Yara rules
    
    
    rule anti_emulation_defender
    {
        meta:
            description = "Research Windows Defender Emulator artefacts that can be used as anti-emulator by malware"
            references = "https://harfanglab.io/en/insidethelab/raspberry-robin-and-its-new-anti-emulation-trick/‎"
            hash = "242851abe09cc5075d2ffdb8e5eba2f7dcf22712625ec02744eecb52acd6b1bf"
            date = "2024-04-03"
            author = "Harfanglab"
            context = "file"
    
        strings:
    
            $s_00 = "aaa_TouchMeNot_" wide ascii nocase
            $s_01 = "_TouchMeNot_" wide ascii nocase
            $s_03 = "C:\\myapp.exe" wide ascii nocase
            $s_04 = "C:\\Mirc\\" wide ascii nocase
            $s_05 = "C:\\Mirc\\mirc.ini" wide ascii nocase
            $s_06 = "C:\\Mirc\\script.ini" wide ascii nocase
            $s_07 = "HAL9TH" wide ascii nocase fullword
            $s_09 = "MpSockVendor" wide ascii nocase fullword
            $s_10 = "MPGoodStatus" wide ascii nocase fullword
            $s_11 = "MpDisableSehLimit" wide ascii nocase fullword
            $s_12 = "NtControlChannel" wide ascii nocase fullword
            $s_13 = "ObjMgr_ValidateVFSHandle" wide ascii nocase fullword
            $s_14 = "ThrdMgr_GetCurrentThreadHandle" wide ascii nocase fullword
            $s_15 = "ThrdMgr_SaveTEB" wide ascii nocase fullword
            $s_16 = "ThrdMgr_SwitchThreads" wide ascii nocase fullword
            $s_17 = "VFS_DeleteFileByHandle" wide ascii nocase fullword
            $s_18 = "VFS_DeleteFile" wide ascii nocase fullword
            $s_19 = "VFS_DeleteFileByHandle" wide ascii nocase fullword
            $s_20 = "VFS_FileExists" wide ascii nocase fullword
            $s_21 = "VFS_FindClose" wide ascii nocase fullword
            $s_22 = "VFS_FindFirstFile" wide ascii nocase fullword
            $s_23 = "VFS_FindNextFile" wide ascii nocase fullword
            $s_24 = "VFS_FlushViewOfFile" wide ascii nocase fullword
            $s_25 = "VFS_GetAttrib" wide ascii nocase fullword
            $s_26 = "VFS_GetHandle" wide ascii nocase fullword
            $s_27 = "VFS_GetLength" wide ascii nocase fullword
            $s_28 = "VFS_MapViewOfFile" wide ascii nocase fullword
            $s_29 = "VFS_MoveFile" wide ascii nocase fullword
            $s_30 = "VFS_Open" wide ascii nocase fullword
            $s_31 = "VFS_Read" wide ascii nocase fullword
            $s_32 = "VFS_SetAttrib" wide ascii nocase fullword
            $s_33 = "VFS_SetCurrentDir" wide ascii nocase fullword
            $s_34 = "VFS_SetLength" wide ascii nocase fullword
            $s_35 = "VFS_UnmapViewOfFile" wide ascii nocase fullword
            $s_37 = "MpAddToScanQueue" wide ascii nocase fullword
            $s_38 = "MpCreateMemoryAliasing" wide ascii nocase fullword
            $s_39 = "MpCallPostEntryPointCode" wide ascii nocase fullword
            $s_40 = "MpCallPreEntryPointCode" wide ascii nocase fullword
            $s_41 = "MpDispatchException" wide ascii nocase fullword
            $s_42 = "MpExitThread" wide ascii nocase fullword
            $s_43 = "MpFinalize" wide ascii nocase fullword
            $s_44 = "MpGetCurrentThreadHandle" wide ascii nocase fullword
            $s_45 = "MpGetCurrentThreadId" wide ascii nocase fullword
            $s_46 = "MpGetLastSwitchResult" wide ascii nocase fullword
            $s_47 = "MpGetPseudoThreadHandle" wide ascii nocase fullword
            $s_48 = "MpGetSelectorBase" wide ascii nocase fullword
            $s_49 = "MpGetVStoreFileHandle" wide ascii nocase fullword
            $s_50 = "MpHandlerCodePost" wide ascii nocase fullword
            $s_51 = "MpIntHandler" wide ascii nocase fullword
            $s_52 = "MpIntHandlerParam" wide ascii nocase fullword
            $s_53 = "MpIntHandlerReturnAddress" wide ascii nocase fullword
            $s_54 = "MpNtdllDatatSection" wide ascii nocase fullword
            $s_55 = "MpReportEvent" wide ascii nocase fullword
            $s_56 = "MpReportEventEx" wide ascii nocase fullword
            $s_57 = "MpReportEventW" wide ascii nocase fullword
            $s_58 = "MpSehHandler" wide ascii nocase fullword
            $s_59 = "MpSetSelectorBase" wide ascii nocase fullword
            $s_60 = "MpStartProcess" wide ascii nocase fullword
            $s_61 = "MpSwitchToNextThread" wide ascii nocase fullword
            $s_62 = "MpSwitchToNextThread_WithCheck" wide ascii nocase fullword
            $s_63 = "MpSwitchToNextThread_NewObjManager" wide ascii nocase fullword
            $s_64 = "MpTimerEvent" wide ascii nocase fullword
            $s_65 = "MpTimerEventData" wide ascii nocase fullword
            $s_66 = "MpUfsMetadataOp" wide ascii nocase fullword
            $s_67 = "MpValidateVFSHandle" wide ascii nocase fullword
            $s_68 = "MpVmp32Entry" wide ascii nocase fullword
            $s_69 = "MpVmp32FastEnter" wide ascii nocase fullword
    
            $filter_00 = "mpengine.pdb" ascii nocase
            $filter_01 = "MsMpEngCP.pdb" ascii nocase
            $filter_02 = "MsMpEngSvc.pdb" ascii nocase
            $filter_03 = "MpGear.pdb" ascii nocase
            $filter_04 = "mrtstub.pdb" ascii nocase
            $filter_05 = "mrt.pdb" ascii nocase
            $filter_06 = "ntoskrnl.pdb" ascii nocase
            $filter_07 = "mscorlib.pdb" ascii nocase
            $filter_08 = "dbghelp.pdb" ascii nocase
            $filter_09 = "msvcrt.pdb" ascii nocase
            $filter_10 = "mrt.exe" wide ascii nocase
            $filter_11 = "PEBMPAT:Obfuscator_EW2" wide ascii
            $filter_12 = "Unimplemented type change to VT_" wide ascii
            $filter_13 = "Initialize engine first!" wide ascii
            $filter_14 = "VirTool:Win32/Obfuscator" wide ascii
            $filter_15 = "VDMConsoleOperation" wide ascii
            $filter_16 = "VDMOperationStarted" wide ascii
            $filter_17 = "sigutils\\vdlls\\" ascii
            $filter_18 = "Microsoft.Windows.MalwareRemovalTool" wide ascii
            $filter_19 = "AppVISVSubsystems32.pdb" ascii nocase
            $filter_20 = "Microsoft.AppV.ClientProgrammability.Eventing.pdb" ascii nocase
            $filter_21 = "AppVISVSubsystems64.pdb" ascii nocase
            $filter_22 = "AppVEntSubsystems.pdb" ascii nocase
            $filter_24 = "shell32.pdb" ascii nocase
            $filter_25 = "version.pdb" ascii nocase
            $filter_26 = "mscoree.pdb" ascii nocase
            $filter_27 = "ws2_32.pdb" ascii nocase
            $filter_28 = "advapi32.pdb" ascii nocase
            $filter_29 = "AppVEntSubsystems64.pdb" ascii nocase
            $filter_30 = "AppVEntSubsystems32.pdb" ascii nocase
            $filter_31 = "AppVISVSubsystems.pdb" ascii nocase
            $filter_32 = "mpengine.dll" ascii wide nocase
            $filter_33 = "VFSAPI_VFS_" ascii wide
    
        condition:
            uint16(0) == 0x5A4D
            and uint32(uint32(0x3C)) == 0x00004550
            and filesize < 5MB
            and 1 of ($s_*)
            and not 1 of ($filter*)
    }

[ ![Compromised routers are still leveraged as malicious infrastructure to target government organizations in Europe and Caucasus](https://harfanglab.io/medias/2024/01/banner-424x283.jpg) Identifier: TRR240101. On 2023-12-28, the Ukrainian government computer emergency and incident response team (CERT-UA) described a malicious espionage campaign that targeted government organizations in Ukraine. CERT-UA attributed the campaign to the APT28 threat-actor (aka Sofacy, Fancy Bear, etc.). The malicious… ](https://harfanglab.io/insidethelab/compromised-routers-infrastructure-target-europe-caucasus/)[ ![Header image for PackXor](https://harfanglab.io/medias/2024/09/image-424x283.png) Summary In early July 2024, the Sentinel Labs researchers released an extensive article1 about “FIN7 reboot” tooling, notably introducing “AvNeutralizer”, an anti-EDR tool. This tool has been found in the wild as a packed payload. In this article, we offer… ](https://harfanglab.io/insidethelab/unpacking-packxor/)[ ![samecoin-header](https://harfanglab.io/medias/2024/02/samecoin-header-424x283.png) Identifier: TRR240201. Summary Following an X post by IntezerLab about an attack campaign that they dubbed “SameCoin”, we analyzed the samples they discovered and found a few identical variants. The infection vector appears to be an email impersonating the Israeli… ](https://harfanglab.io/insidethelab/samecoin-malware-hamas/)[ ![Gamaredon](https://harfanglab.io/medias/2026/05/cover-424x283.png) Identifier: TRR260501. Summary Investigating Gamaredon’s abuse of CVE-2025-8088, we identified a dozen waves of spearphishing emails against Ukrainian state institutions in a campaign that is still active, dating back to September 2025. These emails – spoofed or sent from compromised… ](https://harfanglab.io/insidethelab/gamaredon-gammadrop-gammaload/)