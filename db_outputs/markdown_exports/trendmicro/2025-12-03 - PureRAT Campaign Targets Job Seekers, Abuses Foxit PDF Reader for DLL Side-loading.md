# PureRAT Campaign Targets Job Seekers, Abuses Foxit PDF Reader for DLL Side-loading

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/25/l/valleyrat-campaign.html
- **Date :** 2025-12-03

---

Malware

# PureRAT Campaign Targets Job Seekers, Abuses Foxit PDF Reader for DLL Side-loading

Job seekers looking out for opportunities might instead find their personal devices compromised, as a PureRAT campaign propagated through email leverages Foxit PDF Reader for concealment and DLL side-loading for initial entry.

By: Sarah Pearl Camiling, Junestherry Dela Cruz, Jacob Santos, Sophia Nilette Robles, Maristel Policarpio, Raymart Yambot 2025/12/03 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

## Key takeaways

  * PureRAT targets job seekers in a campaign spreading through email, disguising itself behind a weaponized Foxit PDF reader and performing dynamic-link library (DLL) side-loading to gain a foothold in the system.
  * As a remote access trojan (RAT), a PureRAT attack can lead to threat actors gaining control of systems, monitoring activity, and stealing sensitive data.
  * The campaign targets job seekers and can also potentially affect those working in human resources (HR), such as recruiters and sourcing specialists.
  * Trend Vision One™ detects and blocks the indicators of compromise (IoCs) discussed in this blog. Trend Micro customers can also access tailored hunting queries, threat insights, and intelligence reports to better understand and proactively defend against this campaign.



**_Update on December 12, 2025, 7:30 AM UTC:_**  
_We initially attributed the findings in this report to ValleyRAT based on the preliminary indicators observed during our investigation. However, following additional analysis and valuable feedback from the cybersecurity research community, we have verified that these campaigns should be correctly attributed to PureRAT instead. We apologize for this initial misattribution and any confusion it may have caused. We extend our sincere gratitude to the researchers who provided critical feedback and additional intelligence that enabled us to make this correction._

Cybercriminal operations continue to escalate in both aggressiveness and sophistication, achieving greater impact through the strategic integration of multiple methods. The campaign investigated in this article demonstrates a layered application of tried-and-tested techniques: social‑engineering lures targeting job seekers, obfuscation through deeply nested directory paths, and execution via DLL sideloading.

Recent observations show that beyond phishing campaigns targeting travelers worldwide using ClickFix that impersonates popular travel booking websites, PureRAT actors now appear to be going after jobseekers in general as well, as evidenced by filename of attachments from emails.

Because job seekers constantly watch out for new opportunities, they might download attachments quickly and overlook warning signs. The emotional strain of the job search can reduce caution, making them more inclined to trust messages that appear to come from potential employers.

One common entry vector we’ve observed is email-based job lures. Archive files, with filenames such as Overview_of_Work_Expectations.zip, Candidate_Skills_Assessment_Test.rar, or Authentic_Job_Application_Form.zip, are deliberately crafted to take advantage of the curiosity and sense of urgency among job seekers.

To bypass initial scrutiny, these compressed files often masquerade as legitimate HR documents while actually containing malicious payloads.

Likewise, this PureRAT campaign also abuses Foxit. The archive file from the email lure contains a renamed version of FoxitPDFReader.exe, designed to make the attack more stealthy and provide a controlled way to load malicious code. For example, the file analyzed in this article is Compensation_Benefits_Commission.exe, still named with a recruitment-related bait. This executable also uses the Foxit logo as its icon to look more convincing.

Upon seeing the Foxit logo, most users would assume that the file is in the popular PDF (.pdf) format and might not notice that it is actually an executable (.exe). Cybercriminals often abuse .exe files to exploit the Windows DLL search order mechanism for DLL side-loading.

The screenshot below shows what the users see after clicking the malicious file from the archive. The PDF which is bundled in the package, displays job details and salary information, probably fake or merely copied from job boards:

![Figure 1. Decoy file containing details of a job opening](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig02.png)

Figure 1. Decoy file containing details of a job opening

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig02.png)

Unknown to the user, as they pore over the details of the document, the PureRAT payload has begun running silently in the background.

## PureRAT techniques

![Figure 2. PureRAT infection chain](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/purerat-figure2.jpg)

Figure 2. PureRAT infection chain

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/purerat-figure2.jpg)

This diagram above traces the entire stealthy infection path—starting with a malicious archive file containing a FoxitPDFReader.exe disguised as a document, loading a malicious msimg32.dll, and ending with PureRAT, stitched together by DLL side-loading, script executions, and .NET reflection loading.

Besides FoxitPDFReader.exe, the archive file contains a malicious hidden msimg32.dll, along with other files and folders intended to enhance the deception. There is also another hidden folder named "Document".

![Figure 3. Contents of the archive file](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig04.png)

Figure 3. Contents of the archive file

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig04.png)

Viewing the file through its folder tree shows, besides the disguised executable and the DLL file, other concealed files. Typical-looking project folders coexist with a hidden Document directory containing a long chain of underscore-named subfolders, ending in files like Shortcut.lnk and “document” files, showing attempts for obfuscation or concealment.

![Figure 4. Folder tree showing a disguised executable ](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig05.png)

Figure 4. Folder tree showing a disguised executable 

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig05.png)

The batch file, document.bat, uses the document.docx file to extract the contents of the document.pdf file. The document.docx file is actually a disguised 7zip executable, allows the extraction of an archived Python environment hidden within the document.pdf file. 

![Figure 5. The “document” files facilitating the extraction of the Python environment](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig06.png)

Figure 5. The “document” files facilitating the extraction of the Python environment

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig06.png)

![Figure 6. Hidden document.bat within the nested directory path](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig07.png)

Figure 6. Hidden document.bat within the nested directory path

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig07.png)

This method ensures that the Python script can be executed on the target system even if Python is not pre-installed, leveraging the document.bat script to automate the process. Such tactics demonstrate the attackers' ingenuity in bypassing security measures and executing their payload with minimal user awareness.

Following extraction, the batch file invokes the Python interpreter to execute the malicious Python script, facilitating payload deployment.

![Figure 7. Execution of document.bat](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig08.png)

Figure 7. Execution of document.bat

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig08.png)

After the batch file extracts the content of document.pdf (Python environment) using document.docx (7zip.exe), an encoded base64 is downloaded from 196[.]251[.]86[.]145, containing the Python script that serves as a shellcode loader.

The python.exe was renamed as “zvchost.exe” and runs the script using the “-c” parameter, as can be seen in the pseudocode. It also creates an autorun registry entry to make it persistent in the system.

![Figure 8. The shellcode loader uses Win32 API functions to run a shellcode that will be decoded first from base64](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig09.png)

Figure 8. The shellcode loader uses Win32 API functions to run a shellcode that will be decoded first from base64

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig09.png)

![Figure 9. Strings in memory show the command and control \(C&C\) IP address and port of PureRAT](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig10.png)

Figure 9. Strings in memory show the command and control (C&C) IP address and port of PureRAT

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig10.png)

The attack steals data from the user’s internet browsers.

![Figure 10. In-memory strings](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig11.png)

Figure 10. In-memory strings

[ download ](/content/dam/trendmicro/global/en/research/25/l/valleyrat-campaign/valleyrat_fig11.png)

The above in-memory strings reference Chromium-based browswer profiles. This behavior is similar to those seen from prior research by other researchers.

Probing the malicious file’s certificate that was captured in network logs of sandbox analysis tool, to exhibits characteristics commonly seen in certificates used by PureRAT SSL as part of its secure communication. These include a self-signed structure, a randomized common name, outdated TLS versions (TLSv1), and an extremely long validity period (valid until December 31, 9999 at 23:59 UTC), which are traits frequently produced by automated certificate generators built into the RAT builders.

**Version** | **TLSv1**  
---|---  
Subject | CN=Zbtrprwgxex  
Issuer | CN=Zbtrprwgxex  
Valid from | 02.04.2025, 17:01  
Valid to | 31.12.9999, 23:59  
Fingerprint | 7e:3f:5a:c9:0b:81:54:af:50:70:f0:1c:05:b6:a4:ce:63:3c:58:ee  
JA3 | fc54e0d16d9764783542f0146a98b300  
JA3 Full string | 769,49162-49161-49172-49171-53-47-10,10-11-35-23-65281,29-23-24,0  
Table 1. Certificate details

The analysis highlights how PureRAT operators exploit the emotional and psychological vulnerabilities of job seekers, preying on their eagerness to secure employment. Their tactics also involve misusing legitimate software like Foxit Reader through DLL sideloading and deceptive techniques.

By understanding these methods, users can better identify potential threats and take proactive steps to safeguard their systems. Robust security awareness training plays a vital role in helping individuals detect and avoid such sophisticated attacks, ultimately reducing the likelihood of compromise.

Proactive security with Trend Vision One™

[Trend Vision One™](https://www.trendmicro.com/en_us/business/products/security-operations.html) is the only AI-powered enterprise cybersecurity platform that centralizes cyber risk exposure management and security operations, delivering robust layered protection across on-premises, hybrid, and multi-cloud environments.

Trend Vision One™ Threat Intelligence

To stay ahead of evolving threats, Trend customers can access [Trend Vision One™ Threat Insights,](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) which provides the latest insights from Trend™ Research on emerging threats and threat actors. 

**Trend Vision One Threat Insights**

  * Emerging Threats: [Analysis of the PureRAT Campaign: Leveraging Foxit PDF Reader DLL Sideloading for Initial Compromise](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Analysis%20of%20the%20PureRAT%20Campaign%3A%20Leveraging%20Foxit%20PDF%20Reader%20DLL%20Sideloading%20for%20Initial%20Compromise)



**Trend Vision One Intelligence Reports (IOC Sweeping)**

  * [Analysis of the PureRAT Campaign: Leveraging Foxit PDF Reader DLL Sideloading for Initial Compromise](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence?intrusionSet=Analysis%20of%20the%20PureRAT%20Campaign%3A%20Leveraging%20Foxit%20PDF%20Reader%20DLL%20Sideloading%20for%20Initial%20Compromise)



Hunting Queries 

**Trend Vision One Search App**

Trend Vision One customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment. 

**_Suspicious Command — Executable/BAT in Deep Underscore Path_**  
**_processCmd: /(\\\\_){10,}\\\\.*(exe|bat)/_**  
More hunting queries are available for Trend Vision One customers with [Threat Insights entitlement enabled](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html). 

Indicators of Compromise (IoC) 

**SHA1** | **SHA256** | **Detection** | **Description**  
---|---|---|---  
ebcfc4f6c6e63b75dc407f5e76c9d96c69c3c1b6 | a32fa6ba08db96ebd611f6ee06da44b419d569a6bac43ed00c68d6ca674004c3  | Backdoor.MSIL.PURERAT.THKBFBE | .NET exe in memory (PureRAT)  
5cb888c87b15ec998c638892ad382dc68efb7f94 | 7e8415e2744be160b7d7c600a401de41554c1357c2d2d35c85f8be8068cbc649 | Trojan.MSIL.PURERAT.THKBFBE | .NET DLL loader  
65fec70eaca638cbd10a6774e4e67f2d55f63959 | 9b0afe79696ccb263b8a00c75c021d115f152283714c0e4c5075aad4e52b94f9 | Trojan.BAT.PURERAT.THKBFBE | document.bat  
9eb12480a9e3be552c88960d45beeacfb3b2444b  
0227738e5a98622ea88a2f09527618a6fc4b9be9 37a9972e667dc479bbbd586803d809b56b00ffcf a2f95e24cb46a0a1edba7d1ff4f7fa2789ee2325 c52473f4e858e91dfd769a1774e5821750b8c8e2 9857742e8f10595111be8cf813f4b83c6e8d7bc5 da24feaa3f0fc9a326905afab295324944fb0f03 678045a8b05e4bf36c7bb0338612bcbfc2376dd8 3776c0df00a24f9152b6cb44c0fa05ef410f747b 191a7e68ca0d15af4283844aa4916f8f73fe6be2 2ed9043c9eaf0cccb96711ca05a07add8a10ec88 e43daace2965439f2b1574b903d08af427f9307d 21f6eb9e582043af0be06dbdb2819e9642ca991a 1c796a576e1f30ed0a672b30b0d2644aebe7f739 7dab6af4c90599ddba656bec8e258d08e9e8ffe6 df86e5d1a2d614c762704dc8842874fad27de978 2afde2c2a7773f68de691fe4f4e835fe530a3471 784468f153fd9b1676504f51bce1bbd9237373f2 2336179beb8a8d4c9a23771cc0ae31f2a146fbbd 763b0273c03053405806722df9fe3c9e270c8d55 | 074400e2f09312081c29e905a9d24f70cfc5f535cd1dcaaca31e33586c7b01bc cabd71a7a4df7fa6b5ffe0f22354953b5d278c5b2626af8bfba0ba726acc59ef 3b2d397f308e00f6ef5ae4a368b6ec9a1b5791b883583d104949d80711f5789f c3f09771a248daede16382ec9484c6a626e2f289c095164eea97170f3e4a6769 8a18b8826daafc4a84d49299013c5cabe95dd9159ea5d5f1fb5872a6d70666e6 28fb1c360663b13a4f918b76a12bdc6f7532896eabf8200bddb63319c92bad26 ff84bb121533144fc87c314a9d50c16dd15bb7d8f036c777e0a6c1dc7395e000 99af1fe7e00d4d82bc6ae4440ad3528202a8a6234038fcde15e78dfea79dac2a 6266d87b93e8129b0b606971f0c9e00214abadbc758769bd9cf456c6e0ad8b6e e65b359519b912139ae7ab3ac77c667c5411d2264a1d75166ae2dfffefe2efaa 0010c5caa8311201cd3b0e335a3936e7d1143362d98f4b5a57ef780dcdc1ca5a 8046fe163a0ab581df7ea7c86788d7dca42f70fac95023dfb36d9281ad3463d9 2261efb7516dd49edd3bface0c769a531c37ce0ca6832871768f622abb0f1f71 cb30d5b932a461601deaf2ef76476e216c7d2a99ea7c280cadbe6510b2997080 6ec18bf62078bb2661b2d0cadf0314ea44fc67da786c28456869b0102eea235c 6351649b644eafe5c27317251bd466a8eab265defb58ab34c20feec60304a861 f75c4d6c989c03c339ead7708227f22d30b9a5f4f433bbe29391a1003aa85d85 bb21ec0bb2b94c5471ed7c768cc999808a42e985955384f6af360caa0c640d6c 216cd0ccc129a612082bddf2502a58aef6b1c22ea07a18a58e4e8315d6ea3fbb f49ba5d85a7be63599346097278c1af49ab6c1bea82e422462057c78641d54d4 | N/A | Archive files bundling the FoxitReader executable alongside a malicious msimg32.dll, leveraging a DLL side-loading technique  
de263d9374d90fb7f51b19a036cb75a3d2072342 | ce1be9e4b2fd0f3958720f9bc2ae9d545bc0e27dcf1042b64a70f1fc62884610 | Trojan.Win64PURERAT.THKBFBE | msimg32.dll  
196[.]251[.]86[.]145/huna  
  
|  | 79-Disease Vector | Download links  
51[.]79[.]214[.]125/huna |  | Malware Accomplice |   
154[.]90[.]58[.]164[:]56001 |  | 91-C&C Server | Related C&C server  
  
Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Malware](/en/research.html?category=trend-micro-research:threats/malware) | [Research](/en/research.html?category=trend-micro-research:article-type/research) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article)

###  Authors 

  * Sarah Pearl Camiling

Senior Threat Researcher

  * Junestherry Dela Cruz

Threats Analyst

  * Jacob Santos

Senior Threat Researcher

  * Sophia Nilette Robles

Threat Analyst

  * Maristel Policarpio

Threat Analyst

  * Raymart Yambot

Threats Analyst




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)