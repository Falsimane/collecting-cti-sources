# WebDAV-as-a-Service: The Infrastructure Behind Emmenhtal

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/webdav-as-a-service-uncovering-the-infrastructure-behind-emmenhtal-loader-distribution
- **Date :** 2024-09-19

---

_This report was originally published for our customers on 30 August 2024._

## **Introduction**

Since December 2023, Sekoia TDR team monitored a specific infrastructure involved in the distribution of the Emmenhtal loader. Emmenhtal is a stealthy malware loader known for its effectiveness in distributing various commodity infostealers worldwide. This loader has attracted attention from cybersecurity researchers, with detailed analyses provided by [Orange Cyberdefense](https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide) and [Google Cloud's Threat Intelligence team](https://cloud.google.com/blog/topics/threat-intelligence/peaklight-decoding-stealthy-memory-only-malware?hl=en).

The Emmenhtal loader, also known as PeakLight, operates in a memory-only manner, making it difficult to detect and analyse. It is primarily used to distribute other malicious payloads, including well-known infostealers that target sensitive information.

This blogpost begins by examining the use of WebDAV technology in hosting malicious files related to the Emmenhtal loader, then analyses the various final payloads delivered through this infrastructure, and concludes by exploring the possibility that the infrastructure is being offered as-a-service to multiple threat actors.

## **Use of WebDAV technology for malicious file hosting**

In our investigation of the infrastructure distributing the Emmenhtal loader, TDR analysts identified the use of WebDAV (Web Distributed Authoring and Versioning) technology to host malicious files. WebDAV, an extension of the HTTP protocol, allows for the management of files on web servers, including uploading, editing, and deleting files remotely. Even though WebDAV has legitimate applications in collaborative environments, threat actors have increasingly leveraged this technology to facilitate malicious activities.

The Emmenhtal loader, first detailed by Orange Cyberdefense for its role in distributing commodity infostealers, was later analysed by Google Cloud’s Threat Intelligence team, which uncovered its sophisticated memory-only execution strategy under the name PeakLight. These analyses underscore the significant and evolving threat posed by Emmenhtal as it continues to deliver new infostealers.

In one of the infection chains described by Orange Cyberdefense and Google, the user is initially redirected to the WebDAV server through a drive-by compromise while visiting some websites. This process results in a preview of an _explorer.exe_ window connected to the WebDAV server, where the malicious files are hosted. Since the end of 2023, **Sekoia.io identified more than 100 malicious WebDAV servers from this infrastructure**.

In the infrastructure Sekoia analysed, the malicious files were hosted within the "/Downloads" directory on a WebDAV server, an open directory where all files are accessible. The files predominantly consisted of "" files, which were weaponised to download further malicious payloads using the "_mshta.exe_ " binary, a legitimate Microsoft executable designed to execute Microsoft HTML Application (HTA) files.

The use of "mshta.exe" to download and execute malicious payloads is a known technique among cybercriminals. By utilising a trusted system binary like "mshta.exe", threat actors can bypass certain security controls and achieve a higher degree of stealth in their operations. Once the "" file is executed, "_mshta.exe_ " is invoked to retrieve the Emmenhtal loader, which is most often hosted on separate infrastructure, adding complexity to the attack chain.

This method of using WebDAV to host malicious ".lnk" files that trigger the download of Emmenhtal via "_mshta.exe_ " represents an evasive tactic. The separation of the hosting server for the initial "" files and the payload server hinder detection and attribution efforts, making it a preferred strategy among advanced threat actors.

## **Detailed analysis of malware delivered** via WebDAV

Our analysis uncovered a wider range of malware distributed via this infrastructure than previously reported. The malware families identified, such as SelfAU3, DarkGate, and Amadey, demonstrate the infrastructure’s versatility. Each payload was identified as being delivered through WebDAV-hosted ".lnk" files, with the malicious URLs adjusted to avoid direct exposure. Below is a table of the identified malware families and the corresponding URLs:

Malware family| URL  
---|---  
SelfAU3| 
    
    
    91[.]92[.]251[.]35/Downloads/solaris-docs[.]lnk  
  
DarkGate| 
    
    
    206[.]188[.]196[.]28/Downloads/example[.]lnk  
  
Amadey| 
    
    
    147[.]45[.]79[.]82/Downloads/qqeng[.]pdf[.]lnk  
  
Lumma| 
    
    
    91[.]92[.]243[.]198:81/Downloads/test[.]lnk  
  
Remcos| 
    
    
    89[.]23[.]107[.]244/Downloads/Test[.]lnk  
  
MeduzaStealer| 
    
    
    94[.]156[.]64[.]74/Downloads/SecretTeachings[.]pdf[.]lnk  
  
DANABOT| 
    
    
    151[.]236[.]17[.]180/Wire%20Confirmation/WireConfirmation[.]pdf[.]lnk  
  
ACR Stealer| 
    
    
    62[.]133[.]61[.]104/Downloads/test[.]pdf[.]lnk  
  
Asyncrat| 
    
    
    62[.]133[.]61[.]101/Downloads/Invoice[.]pdf[.]lnk  
  
Stealit| 
    
    
    62[.]133[.]61[.]37/Downloads/config[.]txt[.]lnk  
  
Cryptbot| 
    
    
    89[.]23[.]103[.]56/Downloads/Videof/Full%20Video%20HD%20%281080p%29[.]lnk  
  
XWORM| 
    
    
    62[.]133[.]61[.]73/Downloads/Photo[.]lnk  
  
Bash File Dropping ZgRAT, DCRAT, PureLogs, XWORM| 
    
    
    147[.]45[.]50[.]214/Downloads/demo[.]pdf[.]lnk  
  
DEERSTEALER| 
    
    
    92[.]118[.]112[.]253/Downloads/releaseform[.]pdf[.]lnk  
  
Guloader| 
    
    
    89[.]23[.]107[.]67/Downloads/2023-Documents%20Shared[.]lnk  
  
Redline| 
    
    
    147[.]45[.]50[.]57/Downloads/INVOICE%20340138551[.]pdf[.]lnk  
  
Malware families and their corresponding URLs 

The discovery of these additional malware families highlights the evolving nature of the threat landscape associated with the Emmenhtal loader.

## **Infrastructure assumptions and observations**

Based on our analysis and the diversity of malware observed, it is plausible that the WebDAV infrastructure described above is part of a broader cybercriminal operation offering "Infrastructure-as-a-Service" (IaaS) to other threat actors. This hypothesis is supported by several key observations:

  1. **Diversity of final payloads** : The wide range of malware families delivered through this infrastructure suggests that multiple threat actors are utilising the same service. The distribution of various malware, such as SelfAU3, DarkGate, and Amadey, among others, indicates a shared infrastructure being rented or leased to different cybercriminals with varying objectives.
  2. **Presence of test files** : Since December 2023, we have consistently observed the presence of "test" files within the infrastructure. These files likely represent attempts by clients to validate the reliability and effectiveness of the service before deploying their actual payloads. The use of test files is common in IaaS models, where customers wish to ensure the functionality of the infrastructure they are purchasing.
  3. **Consistency in autonomous systems (AS)** : There has been a notable consistency in the Autonomous Systems (AS) used to host the WebDAV servers associated with this infrastructure. This consistency further supports the theory of a centralised service being offered. Below is a list of the AS providers and the approximate date they were first observed: 
     * **Terasyst Ltd (AS31420)** : Observed from February 2024
     * **Zonata - Natskovi & Sie Ltd. (AS34368)**: Observed from February 2024
     * **BL Networks (AS399629)** : Observed from February 2024
     * **ICDSoft Ltd. (AS8739)** : Observed from March 2024
     * **OOO Freenet Group (AS2895)** : Observed from April 2024
     * **Perviy TSOD LLC (AS48430)** : Observed from April 2024
     * **GLOBAL INTERNET SOLUTIONS LLC (AS207713)** : Observed from May 2024



The repeated use of specific AS providers over several months suggests that the threat actor(s) behind this infrastructure have established a reliable hosting arrangement, potentially as part of a larger IaaS offering. This consistency in hosting environments might also be indicative of a deliberate choice to evade detection by rotating among a select group of trusted providers.

## Conclusion

The findings presented in this report suggest that the infrastructure used to distribute the Emmenhtal loader is likely part of a commercial service offered by a cybercriminal group. The presence of multiple malware payloads, consistent testing activities, and the reuse of specific Autonomous Systems for hosting all point towards a sophisticated operation designed to cater to multiple clients. As this infrastructure continues to evolve, it poses a significant and ongoing threat, necessitating continued vigilance and targeted defensive measures by cybersecurity professionals.

Our clients can access detailed information on the observed activities, related threat indicators, and ongoing monitoring efforts directly through our platform. We remain committed to tracking this infrastructure over time and will provide continuous updates as new developments emerge.