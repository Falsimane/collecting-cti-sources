# Likely eCrime Actor Capitalizing on Falcon Sensor Issues | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/likely-ecrime-actor-capitalizing-on-falcon-sensor-issues/
- **Date :** July 20, 2024

---

# Likely eCrime Actor Uses Filenames Capitalizing on July 19, 2024, Falcon Sensor Content Issues in Operation Targeting LATAM-Based CrowdStrike Customers

July 20, 2024

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


## Summary

On July 19, 2024, an issue present in a single content update for the CrowdStrike Falcon® sensor impacting Windows operating systems was identified, and a fix was deployed.1

CrowdStrike Intelligence has since observed threat actors leveraging the event to distribute a malicious ZIP archive named `crowdstrike-hotfix.zip`. The ZIP archive contains a _HijackLoader_ payload that, when executed, loads _RemCos_. Notably, Spanish filenames and instructions within the ZIP archive indicate this campaign is likely targeting Latin America-based (LATAM) CrowdStrike customers.

## Details

On July 19, 2024, a ZIP archive named `crowdstrike-hotfix.zip` (SHA256 hash: `c44506fe6e1ede5a104008755abf5b6ace51f1a84ad656a2dccc7f2c39c0eca2`) was uploaded to an online malware-scanning service by a Mexico-based submitter. 

The ZIP file’s accompanying Spanish-language instructions appear to pose as a utility for automating recovery for the content update issue. The instructions prompt the user to run `Setup.exe` (SHA256 hash: `5ae3838d77c2102766538f783d0a4b4205e7d2cdba4e0ad2ab332dc8ab32fea9`) to start the patch installation.

![Figure 1. Content of instrucciones.txt](https://www.crowdstrike.com/wp-content/uploads/2024/07/Intel-blog-2-Fig-1-907x1024.png)

Figure 1. Content of instrucciones.txt

When executed, `Setup.exe` will load and execute the _HijackLoader_ first-stage inside `madBasic_.bpl` (SHA256 hash: `d6d5ff8e9dc6d2b195a6715280c2f1ba471048a7ce68d256040672b801fda0ea`) via DLL search-order hijacking. 

_HijackLoader_ — advertised as a private crypting service, _ASMCrypt_ — is a modular multi-stage loader highly focused on evading detection. The _HijackLoader_ configuration file named `maidenhair.cfg` (SHA256 hash: `931308cfe733376e19d6cd2401e27f8b2945cec0b9c696aebe7029ea76d45bf6`) contains data that the loader leverages to execute the final _RemCos_ payload, which contacts the command-and-control (C2) server at `213.5.130[.]58[:]433`.

Following the content update issue, several typosquatting domains impersonating CrowdStrike have been [identified](/content/crowdstrike-www/locale-sites/us/en-us/blog/falcon-sensor-issue-use-to-target-crowdstrike-customers/). This campaign marks the first observed instance in which a threat actor has capitalized on the Falcon content issue to distribute malicious files targeting LATAM-based CrowdStrike customers. 

## Recommendations

CrowdStrike Intelligence recommends that organizations ensure they are communicating with CrowdStrike representatives through official channels and adhere to technical guidance the CrowdStrike support teams have provided.

### Falcon LogScale Queries

This Falcon LogScale query detects the activity described in this report:
    
    
    // Hunting query for indicators (CSA-240835)
    
    case { in("SHA256HashData", values=["931308cfe733376e19d6cd2401e27f8b2945cec0b9c696aebe7029ea76d45bf6", "c44506fe6e1ede5a104008755abf5b6ace51f1a84ad656a2dccc7f2c39c0eca2", "48a3398bbbf24ecd64c27cb2a31e69a6b60e9a69f33fe191bcf5fddbabd9e184", "d6d5ff8e9dc6d2b195a6715280c2f1ba471048a7ce68d256040672b801fda0ea"]); in("RemoteAddressIP4", values=["213.5.130.58"]) } | table([cid, aid, #event_simpleName, ComputerName])
    

### Indicators of Compromise (IOCs)

**Nombre del Archivo**| **SHA256 Hash**  
---|---  
Crowdstrike-hotfix.zip | c44506fe6e1ede5a104008755abf5b6ace51f1a84ad656a2dccc7f2c39c0eca2  
sqlite3.dll| 02f37a8e3d1790ac90c04bc50de73cd1a93e27caf833a1e1211b9cc6294ecee5  
vclx120.bpl| 2bdf023c439010ce0a786ec75d943a80a8f01363712bbf69afc29d3e2b5306ed  
instrucciones.txt| 4f450abaa4daf72d974a830b16f91deed77ba62412804dca41a6d42a7d8b6fd0  
maddisAsm_.bpl| 52019f47f96ca868fa4e747c3b99cba1b7aa57317bf8ebf9fcbf09aa576fe006  
Setup.exe| 5ae3838d77c2102766538f783d0a4b4205e7d2cdba4e0ad2ab332dc8ab32fea9  
datastate.dll| 6010e2147a0f51a7bfa2f942a5a9eaad9a294f463f717963b486ed3f53d305c2  
madexcept_.bpl| 835f1141ece59c36b18e76927572d229136aeb12eff44cb4ba98d7808257c299  
maidenhair.cfg (_HijackLoader_ configuration)| 931308cfe733376e19d6cd2401e27f8b2945cec0b9c696aebe7029ea76d45bf6  
rtl120.bpl| b1fcb0339b9ef4860bb1ed1e5ba0e148321be64696af64f3b1643d1311028cb3  
vcl120.bpl| b6f321a48812dc922b26953020c9a60949ec429a921033cfaf1e9f7d088ee628  
battuta.flv| be074196291ccf74b3c4c8bd292f92da99ec37a25dc8af651bd0ba3f0d020349  
madBasic_.bpl (_HijackLoader_ first-stage _)_ | d6d5ff8e9dc6d2b195a6715280c2f1ba471048a7ce68d256040672b801fda0ea  
 _RemCos_ Payload| 48a3398bbbf24ecd64c27cb2a31e69a6b60e9a69f33fe191bcf5fddbabd9e184  
 _RemCos_ C2 Address| 213.5.130[.]58[:]443  
  
Table 1. Campaign IOCs

#### Additional Resources

  * _For more information, this blog post is being updated regularly:[ Statement on Falcon Content Update for Windows Hosts](/content/crowdstrike-www/locale-sites/us/en-us/blog/statement-on-falcon-content-update-for-windows-hosts/)._
  * _Read this message from George Kurtz, CrowdStrike Founder and CEO:[ To Our Customers and Partners](/content/crowdstrike-www/locale-sites/us/en-us/blog/our-statement-on-todays-outage/)._
  * _For technical information, see this blog post:[Technical Details: Falcon Content Update for Windows Hosts.](/content/crowdstrike-www/locale-sites/us/en-us/blog/technical-details-on-todays-outage/)_
  * _Read another blog post from CrowdStrike Intelligence regarding the Falcon content issue:[ Falcon Sensor Content Issue from July 19, 2024, Likely Used to Target CrowdStrike Customers.](/content/crowdstrike-www/locale-sites/us/en-us/blog/falcon-sensor-issue-use-to-target-crowdstrike-customers/)_



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)