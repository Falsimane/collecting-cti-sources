# Threat Actor Uses Fake Recovery Manual to Deliver Unidentified Stealer

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/fake-recovery-manual-used-to-deliver-unidentified-stealer/
- **Date :** July 22, 2024

---

# Threat Actor Uses Fake CrowdStrike Recovery Manual to Deliver Unidentified Stealer

July 22, 2024

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


On July 22, 2024, CrowdStrike Intelligence identified a Word document containing macros that download an unidentified stealer now tracked as _Daolpu_. The document impersonates a Microsoft recovery manual.1 Initial analysis suggests the activity is likely criminal.

## Technical Analysis

### Lure Document

The analyzed file,
    
    
    New_Recovery_Tool_to_help_with_CrowdStrike_issue_impacting_Windows.docm
    

(SHA256 hash:
    
    
    803727ccdf441e49096f3fd48107a5fe55c56c080f46773cd649c9e55ec1be61
    

), is a Word document containing malicious macros.

Upon execution, the macro retrieves a second-stage DLL from URL `http[:]//172.104.160[.]126:8099/payload2.txt` that is saved to `%TMP%\mscorsvc.dll`. On 22 July 2024, the URL served a file (SHA256 hash:
    
    
    5eaf0f1c1d23f4372e24eb15ee969552c416a38dbc45e4f2b4af283e3bfb8721
    

) containing a Base64-encoded DLL that, when decoded, executes the novel stealer Daolpu.

A macro decodes the DLL using the Windows utility `certutil`, resulting in another DLL file (SHA256 hash:
    
    
    4ad9845e691dd415420e0c253ba452772495c0b971f48294b54631e79a22644a
    

; build timestamp `2024-07-19 08:10:10 UTC`). Then, the macro runs this DLL using `rundll32` and calls the exported function `DllMain`.

### Daolpu Stealer

Upon execution, _Daolpu_ invokes `taskkill /F /IM chrome.exe` to kill the Chrome process. The malware then collects credentials such as login data and cookies stored in Chrome and Mozilla browsers.

The collected data is saved to `%TMP%\result.txt` and removed after exfiltration. The malware sends the `result.txt` file to the command-and-control (C2) server `http[:]//172.104.160[.]126:5000/Uploadss` in an HTTP POST request, which includes the system MAC address and hardcoded key `Privatekey@2211#$`.

## Recommendations

  * These recommendations can be implemented to help protect against the activity described in this report.
  * Only communicate with CrowdStrike representatives through official channels and adhere to CrowdStrike support teams’ technical guidance
  * Check websites’ certificates on the download page to ensure downloaded software originates from a legitimate source
  * Train users to avoid executing files from untrusted sources
  * Use browser settings to enable download protection that can issue warnings about potentially harmful websites or downloads
  * Hunt for the file `result.txt` in `%TMP%`, which might indicate a _Daolpu_ infection



## Appendix

### YARA Rule

This YARA rule detects host-based artifacts associated with the activity described in this report.
    
    
    rule CrowdStrike_CSA_240838_01 : daolpu stealer 
    {
        meta:
            copyright = "(c) 2024 CrowdStrike Inc."
            description = "C++ stealer delivered via Word documents with macros impersonating CS"
            reports = "CSA-240838"
            version = "202407221342"
            last_modified = "2024-07-22"
            malware_family = "Daolpu"
        strings:
            $ = "C:\\Windows\\Temp\\result.txt"
            $ = "D:\\c++\\Mal_Cookie_x64\\x64\\Release\\mscorsvc.pdb"
        condition:
            all of them
    }
    

### Falcon LogScale Queries

This Falcon LogScale Query detects the activity described in this report.
    
    
    // hunting rule for indicators (CSA-240838)
    case { in("SHA256HashData", values=["00199b4784533a124da96be5d5e472195b0e27be15007dcbd573c0fb29941d99", "3a9323a939fbecbc6d0ceb5c1e1f3ebde91e9f186b46fdf3ba1aee03d1d41cd8", "4ad9845e691dd415420e0c253ba452772495c0b971f48294b54631e79a22644a", "5eaf0f1c1d23f4372e24eb15ee969552c416a38dbc45e4f2b4af283e3bfb8721", "803727ccdf441e49096f3fd48107a5fe55c56c080f46773cd649c9e55ec1be61"]); in("RemoteAddressIP4", values=["172.104.160.126"]) } | table([cid, aid, #event_simpleName, ComputerName])
    

The following Falcon LogScale query detects the `result.txt` file with credentials in `%TMP%`:
    
    
    // Result file with credentials for Daolpu stealer (CSA-240838)
    "event_platform"="Win" | #event_simpleName = "FileOpenInfo" | FileName = "result.txt" | FilePath = /\\Device\\HarddiskVolume\d+\\Windows\\Temp\\$/
    

### Indicators of Compromise (IOCs)

This table details the IOCs related to the information provided in this report.

**Description**| **IOC**  
---|---  
Word document SHA256 hash| `803727ccdf441e49096f3fd48107a5fe55c56c080f46773cd649c9e55ec1be61`  
Macro download URL| `http[:]//172.104.160[.]126:8099/payload2.txt`  
Second-stage file SHA256 hash| `5eaf0f1c1d23f4372e24eb15ee969552c416a38dbc45e4f2b4af283e3bfb8721`  
 _Daolpu_ SHA256 hash| `4ad9845e691dd415420e0c253ba452772495c0b971f48294b54631e79a22644a`  
 _Daolpu_ SHA256 hash| `3a9323a939fbecbc6d0ceb5c1e1f3ebde91e9f186b46fdf3ba1aee03d1d41cd8`  
 _Daolpu_ C2 server| `http[:]//172.104.160[.]126:5000/Uploadss`  
  
_Table 1. IOCs_

### MITRE ATT&CK

This table details the tactics and techniques described in this report.

**Tactic**| **Technique**| **Observable**  
---|---|---  
**Execution**|  T1204 – User Execution| The threat actor relies on users to open the Word document  
**Credential Access**|  T1555 – Credentials from Password Stores|  _Daolpu_ grabs sensitive information from browsers  
**Command and Control**|  T1071.001 – Application Layer Protocol: Web Protocols|  _Daolpu_ exfiltrates data using the HTTP protocol  
**Exfiltration**|  T1041 – Exfiltration Over C2 Channel|  _Daolpu_ exfiltrates collected data to the C2 server  
  
_Table 2. MITRE ATT &CK Table_

#### Additional Resources

_Read other blog posts from CrowdStrike Intelligence regarding the Falcon content issue:_

  * [_Falcon Sensor Content Issue from July 19, 2024, Likely Used to Target CrowdStrike Customers_](/en-us/blog/falcon-sensor-issue-use-to-target-crowdstrike-customers/)
  * [ _Likely eCrime Actor Uses Filenames Capitalizing on July 19, 2024, Falcon Sensor Content Issues in Operation Targeting LATAM-Based CrowdStrike Customers_](/en-us/blog/likely-ecrime-actor-capitalizing-on-falcon-sensor-issues/)



  1. https[:]//techcommunity[.]microsoft[.]com/t5/intune-customer-success/new-recovery-tool-to-help-with-crowdstrike-issue-impacting/ba-p/4196959



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)