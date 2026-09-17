# Beware of what you download. Recent purported CEIEC document dump booby-trapped.

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/beware-of-what-you-download-recent-purported-ceiec-document-dump-booby-trapped/
- **Date :** 2012-04-16

---

# Beware of what you download. Recent purported CEIEC document dump booby-trapped.

April 16, 2012

In recent weeks thousands documents have been released online by a hacktivist going by the online moniker of “[Hardcore Charlie](https://twitter.com/#!/HardcoreCharle).” These documents appear to have potentially been sourced and possibly stolen from various businesses and governments in different countries including the United States, the Philippines, Myanmar, Vietnam, and others. In particular Hardcore Charlie has been attempting to draw attention to some of the documents that apparently relate to U.S. military operations in Afghanistan. The twist in all of this is that the documents are purported to have been stolen by Hardcore Charlie from the Beijing based military contractor China National Import & Export Corp (CEIEC). If true, that would mean that the documents were stolen at least twice. These are allegations that CEIEC has strongly denied and condemned in a post on [their website](http://www.ceiec.com/news/554).

This entire turn of events has raised more questions than they have answered. Are the documents legitimate? Where were they originally stolen from? If these were really stolen twice, who stole them first? We unfortunately do not have the answer to any of these questions. However, one thing we do have are words of caution and some interesting information about a handful of the documents found in this dump. Within the document dump in a folder related to Vietnam are 11 malicious documents (8 unique) that exploit vulnerabilities (CVE-2010-3333 and CVE-2009-3129) in Microsoft Office to install malware. These documents installed four different types of backdoors that reported back to six distinct command and control servers. Two of the backdoors were unfamiliar two us and the other two were the well known Poison Ivy RAT and the Enfal/Lurid. At least one hostname could be tied back to a known set of persistent actors engaged in cyber espionage.

## Malicious Documents Details

The initial file CEIECOWNED_PT1.rar contained over 1200 documents split up into multiple folders. All 11 of the malicious documents were found in a folder named MONRE_VIETNAM_PT1. Below are the details of each of the malicious documents along with the hostname or IP address that the dropped backdoors attempt to communicate with. Note that each command and control server that used DNS utilized a free China or US-based dynamic DNS provider.
    
    
    **Filename:** CV gui bao cao LD.doc
    **File size:** 49980 bytes
    **MD5 hash:** 2e454ea0c0d3fadfc478e8695400df40
    **SHA-1 hash:** 0dc324cf2efae2bc7dc29fe26f616decd765d66a
    **SHA-256 hash:** 8c26bf867e70f2e3511bd295c2c56abca51ab008b88d7a9e80b99ca240f79773
    **Exploit:** CVE-2010-3333
    **Additional Filename:** CV gui bao cao LD(1).doc
    **CALLBACK/C2:** kullywolf.gicp.net:81
    
    **Filename:** Danh sach.doc
    **File size:** 53052 bytes
    **MD5 hash:** 32f5ad4f09135fcdde86ecd4c466a993
    **SHA-1 hash:** d3311b97aa10d759bbf704c0a3c4c2cef3f997a6
    **SHA-256 hash:** 15f9f9f3e617d84083e6ac3652dfa9090f236ca8879a66654464a5b781318df5
    **Exploit:** CVE-2010-3333
    **CALLBACK/C2:** congtytancang.uicp.net:81	
    
    **Filename:** Computer virus attacks on rise.doc
    **File size:** 71931 bytes
    **MD5 hash:** d824988793146a25d026eb12759dbab0
    **SHA-1 hash:** 3ce24923dc478afb30d8105303f51c958856da52
    **SHA-256 hash:** e4e123a6757e041a5c1c053e2770f89b08ad2b58661e0044b29965d480f5100e
    **Exploit:** CVE-2010-3333
    **CALLBACK/C2:** www.ollay011.zyns.com:7000
    
    **Filename:** Danh sach can bo tham gia du tuyen thac sy 2011.xls
    **File size:** 87063 bytes
    **MD5 hash:** 1423113c5b7176cef19f989f76a020c4
    **SHA-1 hash:** 608ed5cb5b8497f3bc483d1c2a91a34a09abd828
    **SHA-256 hash:** 761d8cbb4cd95bf520584ca5ec3036ae9fd9a9cefdf4ae9e79b060db3a673b28
    **Exploit:** CVE-2009-3129
    **CALLBACK/C2:** 64.56.70.254:80 (Backup: 173.252.204.85:8089, 216.70.255.201:8089, 216.70.128.124:8089, 58.137.153.115:8089, 64.56.70.253:80)'''
    
    **Filename:** De an 928.doc
    **File size:** 250880 bytes
    **MD5 hash:** cd80a451990f17f6684d5b100de6ece0
    **SHA-1 hash:** 436047e74948181d8a2ba91f0c044c4b4e9e1865
    **SHA-256 hash:** 51f495acd08195a04671fb7eb808a5697f3be8877e9d5254d38241147d2b51f1
    **Exploit:** CVE-2010-3333
    **CALLBACK/C2:** l1x.lflinkup.net:80
    
    **Filename:** Hop dong cung cap thiet bi(done).doc
    **File size:** 162304 bytes
    **MD5 hash:** 2332ebd103a963d5494ddb431e8b05b7
    **SHA-1 hash:** bc289ea12d9afdae9f7503309a9d142b0c247ca7
    **SHA-256 hash:** cff1035db0c190081fc78dde2323a04a39ded675b2029f2572b3c084240aaedb
    **Exploit:** CVE-2010-3333
    **CALLBACK/C2:** www.ollay011.zyns.com:7000
    
    **Filename:** bao_cao_cong tac_thang 2&ke_hoach_cong_tac thang_3.doc
    **File size:** 89916 bytes
    **MD5 hash:** 336420283e047155bec94a549cd60ac8
    **SHA-1 hash:** 4b8d6693dc6c127ac9f649f3428de6cd6f8aa8e7
    **SHA-256 hash:** 2c28cf467d9e42f0182174943ec9e8dc467901020465b2354fdb27ccdaafa0c0
    **Exploit:** CVE-2010-3333
    **Additional Filename 1:** bao_cao_cong tac_thang 2&ke_hoach_cong_tac thang_3(1).doc
    **Additional Filename 2:** tong hop nhan su bo nhiem cap phong cap vu.doc
    **CALLBACK/C2:** front11.gicp.net:81
    
    **Filename:** tt_cap nhat danh sach moi.doc
    **File size:** 66364 bytes
    **MD5 hash:** d916409f960d3fc3263b32fe32b4bf20
    **SHA-1 hash:** 42a767745bff3e8a1f5f42d1340eb4db4ed3e57c
    **SHA-256 hash:** 8e8f15980af335727dec14d9c2fed218cbc699aa7f41dae42d9cf96e7b663da4
    **Exploit:** CVE-2010-3333
    **CALLBACK/C2:** front11.gicp.net:81

## A Look at the Dropped Malware

### Poison Ivy

Two out of the nine unique samples installed the popular Poison Ivy RAT upon successful exploitation. Both samples beacon back to **www.ollay011.zyns.com** , which at the time of this writing and since last Thursday has resolved to **64.71.138.240** (Hurricane Electric, US). A closer look at the configuration of this Poison Ivy instance shows that it was setup to use the default password of ‘admin’, wrote itself to C:\WINDOWS\explorer.exe and started a keylogger that gets saved as C:\WINDOWS\explorer.

### Enfal/Lurid

One of the samples installed the far less common, but very well known, Enfal/Lurid trojan. This particular trojan has been frequently associated with targeting of the Tibetan community, the India Government, and other governments and industries in specific geo-locations. It’s previously been discussed over the last four years in the [ISC Sans Diary](https://isc.sans.edu/diary.html?storyid=4177), the [Shadows in the Clouds Report](http://www.nartv.org/mirror/shadows-in-the-cloud.pdf), and the Trend Micro [Lurid Downloader Report](http://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp_dissecting-lurid-apt.pdf). The sample from these files used **l1x.lflinkup.net** as the command and control server to report in information about this system. At the time of this writing the hostname resolved to **123.120.105.120** , a dynamic IP address pool in China. Tracking this hostname back for several months, we can see it has resolved to numerous other short-lived dynamic IP addresses in China. It is also interesting to note that along with the Vietnamese file names, this malware samples installed itself as C:\Program Files\UniKey 2000\UniKey.exe. UniKey is a software-based Vietnamese keyboard for Windows. We can speculate that there is likely actors utilizing the Enfal/Lurid trojan to engage in persistent targeting of Vietnamese interests.

### Unknown/Unnamed

A backdoor for which we do not have a name was observed in six out of the nine samples, all using the CVE-2010-3333 exploit to drop their payloads. Once installed the malware seemed to copy itself into the User’s Application Data folder, as well as at least one other location on the system (often in Program Files). The malware always appears to write a configuration file with the name name msgslang.db. A search for this file name on the web shows several other similar or related samples. The samples that installed this backdoor all beaconed back to one of these DNS names **front11.gicp.net** , **congtytancang.uicp.net** , or **kullywolf.gicp.net**. Only the last two have resolved recently congtytancang.uicp.net and kullywolf.gicp.net has actively changed IP addresses several times since last week. At the time of this writing the two hosts names resolve to **112.112.147.16** and **222.172.238.174** respectively. It is worth noting the the third-level of the DNS name **congtytancang.uicp.net** , appears to be written in Vietnamese and may translate back to something having to do with “Newport” or “Seaport” in English.

### Unknown/Tantouma

The single Microsoft Excel exploit in the packet dropped malware that beaconed back to **64.56.70.254** and likely a variety of other embedded IP addresses. This malware samples was not one that we recognized. However, the sample contains several interesting strings, to include “**Welcome To TANTOUMA Version 2.2 BY ICU @20110210** ” and others that indicate the backdoor is designed to collect information from an infected system and provide remote access to it. The sample also had www.google.com.vn in its strings output, lending further credence that some of the files may be related to concerted efforts to persistently target the Vietnamese.

## Connection to the Google and RSA Breaches

Did your eyes just get big or roll? Good. Sorry we are just kidding — there’s no connection.

## Vietnamese Targeting and Timeline

These nine unique samples from the document dump from Hardcore Charlie appear to lead to multiple different attack campaigns targeting Vietnamese interests. The malicious documents have Vietnamese names and will open legitimate clean versions of the documents in Vietnamese upon successful exploitation. At least one of the trojan samples even saves itself as a file that might blend in on a Vietnamese computer. Another has strings related to the Vietnamese version of Google, while another uses a DNS name that is in Vietnamese as well. We would suspect this may just be the tip of the ice berg.

As for timing — several indicators seem to point to these documents being approximately a year old. The most obvious and more tamper proof piece of evidence being a [VirusTotal submission](https://www.virustotal.com/file/15f9f9f3e617d84083e6ac3652dfa9090f236ca8879a66654464a5b781318df5/analysis/) from April 2011. You may note the document from this submission was named BC cua chi binh voi BCS.doc. However, this file has the same MD5 hash of of32f5ad4f09135fcdde86ecd4c466a993, which matches the file was saw named Danh sach.doc. This indicates that his activity is not new and these files may have been unknowingly included in this document dump.

## Conclusion

These malicious documents within the data dump raise several questions and can lead to plenty of speculation. Were these malicious documents resident on victim systems from previous targeted APT campaigns and exfiltrated alongside the legitimate documents as part of another cyber espionage operation? Could it be that they were intentionally placed into this data dump? Anything is possible and we do not have all the answers. However, we can tell you that a few of the malware samples had previously been submitted to VirusTotal in early 2011. Additionally meta data of the clean documents dropped by a few of the malware payloads showed that the documents were also created in 2011, indicating that the malicious documents have likely been circulating in the wild for more than year.

Although many questions remain, the following facts are clear:

  * A small subset of the documents contained in the purported CEIEC dump are malicious.
  * These malicious documents drop a mix of malware families including Poison Ivy, Enfal/Lurid and two unnamed families.
  * Some of the malware samples extracted from the CEIEC dump connect to infrastructure used in previous APT campaigns.



These documents just go to show that malicious files can end up pretty much anywhere. We are stating the obvious but remember to exercise caution when viewing files you downloaded from the Internet. Microsoft patched the two vulnerabilities used in these attacks quite some time ago. They patched CVE-2009-3129 with [MS09-067](https://technet.microsoft.com/en-us/security/bulletin/MS09-067) and CVE-2010-3333 with [MS10-087](https://technet.microsoft.com/en-us/security/bulletin/MS10-087). Malicious documents that exploit vulnerabilities in Microsoft Office, Adobe Acrobat [Reader], or components loaded by these pieces of software are still some of the most common ways in which cyber espionage attacks are conducted. Staying current with the latest versions and security patches for any software you run is highly recommended.

  * [Malware](/topics/malware/)
  * [Threat Intelligence](/topics/threat-intelligence/)



[« Back to News & Insights](/news-insights/)

### Recent Articles

  * #### [Shadowserver 2025: Highlights of the Year in Review](/news/shadowserver-2025-highlights-of-the-year-in-review/)

September 7, 2026

A review of Shadowserver’s 21st year as the world’s largest provider of free, timely, actionable, daily cyber threat… [Read more »](/news/shadowserver-2025-highlights-of-the-year-in-review/)

  * #### [Shadowserver Critical Community Infrastructure Cyber Resilience Project](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

August 5, 2026

The Shadowserver Critical Community Infrastructure (CCI) Project is designed to improve the cybersecurity posture of essential… [Read more »](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

  * #### [StealC Historical Bot Infection Special Report](/news/stealc-historical-bot-infection-special-report/)

June 25, 2026

On Wednesday 24th June 2026, international law enforcement partners announced additional successful cyber crime disruption… [Read more »](/news/stealc-historical-bot-infection-special-report/)

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)