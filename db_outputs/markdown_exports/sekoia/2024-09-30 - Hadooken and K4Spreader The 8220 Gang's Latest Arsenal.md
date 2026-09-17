# Hadooken and K4Spreader: The 8220 Gang's Latest Arsenal

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/hadooken-and-k4spreader-the-8220-gangs-latest-arsenal
- **Date :** 2024-09-30

---

_This report was originally published for our customers on 24 September 2024._

## **Introduction**

On 17 September 2024, Sekoia’s Threat Detection & Research (TDR) team identified a notable infection chain targeting both Windows and Linux systems through our Oracle WebLogic honeypot. The attacker exploited CVE-2017-10271 and CVE-2020-14883 Weblogic vulnerabilities to deploy Python and Bash scripts, executing the **K4Spreader** malware, which then delivered the **Tsunami** backdoor and a **cryptominer**. For Windows systems, the attacker attempted to execute a PowerShell script designed to install a cryptominer via a .NET-based loader.

In a publication from 12 September 2024, [AquaSec](https://www.aquasec.com/blog/hadooken-malware-targets-weblogic-applications/) revealed that the Hadooken malware served as the primary threat in an attack chain targeting WebLogic servers. The attacker exploited a configuration vulnerability to remotely execute code, deploying shell and Python scripts to download the **Hadooken** payload. This payload installed a cryptominer and the Tsunami malware.

The Aquasec case and the intrusion on our honeypot share many similarities. Indeed, the analysis of the payloads, TTPs (Tactics, Techniques, and Procedures) and indicators of compromise, including the Monero wallet, points to the **8220 Gang** intrusion setas the perpetrator of these attacks.

First documented in 2018 by [Cisco Talos](https://blog.talosintelligence.com/cryptomining-campaigns-2018/), the intrusion set commonly known as 8220 Gang is allegedly based in China and primarily exploits vulnerable cloud environments to deploy cryptomining malware. Its objective is to hijack system resources to mine Monero cryptocurrency (XMR). In 2018, Talos estimated their earnings at $200,000 in Monero.

This blogpost covers these different infection chains, the connections with the 8220 Gang, and the cross-references with the Hadooken case previously documented by Aquasec.

## **Initial access**

Our WebLogic honeypot has been active for several weeks, detecting multiple exploitation attempts since its deployment in august 2024. The first notable intrusion, matching the Hadooken infection chain, occurred on 17 September 2024. The attacker primarily exploited the CVE-2020-14883 vulnerability, occasionally leveraging of CVE-2017-10271. 

Within a span of 24 hours, 15 exploitation attempts were logged, all originating from the same IP address: _77.221.151[.]174_. This IP address is owned by Aeza Group Ltd, AS 216246 (Autonomous System), the same ASN and AS owner linked to the IPs mentioned in the AquaSec article.

### **CVE-2017-10271**

This critical vulnerability in Oracle WebLogic Server allows remote code execution. The flaw lies in the WebLogic WLS component, where an attacker can send a specially crafted request to exploit an XML decoder, bypassing authentication. This vulnerability can be exploited remotely without any login credentials, enabling attackers to execute arbitrary code and potentially take control of the affected system.

In the observed cases, the attacker consistently targeted 4 WLS-WSAT endpoints to execute a shell command designed to download and run a script. 

![pcap of the CVE-2017-10271 exploitation](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554ad_6a92a26a65cc84bc266e8e39_6a2a7e24e02555536e69ffc3.webp)

pcap of the CVE-2017-10271 exploitation

 _Figure 1. pcap of the CVE-2017-10271 exploitation_

In addition to wget or curl, the command also uses the less common _lwp-download_ binary to fetch the next stage, marking a distinct TTP. The downloaded file, a shell script named "_2.gif_ ," is saved in the /tmp directory, employing a typical masquerading technique to bypass filename based detection. 

The use of _lwp-download_ , the script name ("_c_ "), and its behaviour closely align with the TTPs outlined in the AquaSec article.

### **CVE-2020-14883**

This critical Remote Code Execution (RCE) vulnerability in Oracle WebLogic Server, affecting the administration console. Attackers can exploit this flaw without authentication by sending specially crafted HTTP requests, allowing them to execute arbitrary commands on the affected server.

We observed two distinct exploitation attempts: one targeting Linux (_m.xml_) and another one targeting Windows (_m1.xml_). 

  * In the Linux case, the m.xml file executes a command to download the "_c_ " file, saving it in /tmp, and includes a base64 string that decodes and downloads another file named "_y_ " via Python. This behaviour mirrors what AquaSec described.



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554b0_6a92a2674b4041c693422bb4_6a2a7e24e02555536e69ffb9.webp)

_Figure 2. extract of m.xml_

  * In the Windows case, the _m1.xml_ file runs a PowerShell command to download and execute a script named _bin.ps1_.



In all observed exploitation attempts, the attacker targeted both Linux and Windows systems, indicating an opportunistic approach without any prior reconnaissance.

## **Infection routine**

The infection chain related to the vulnerability exploitation can be summarised as follows: a WebLogic vulnerability is exploited to execute a script, which downloads a loader that deploys a cryptominer. While the infection routines for Windows and Linux are generally quite similar, there are however some differences between the two, as outlined below.

## **Windows**

The script carries out two main tasks:

  * It downloads and runs a PowerShell script (amsi_patch.ps1) from [GitHub](https://github.com/Chainski/AES-Encoder), designed to bypass AMSI, preventing antivirus detection of further scripts.
  * Afterward, it decrypts, decompresses, and executes a base64-encoded string in multiple stages. Eventually, it runs a PowerShell script that drops and executes a C# binary called _CCleaner64.exe_. This binary is a loader that downloads, decrypts, and loads a cryptocurrency miner.



Apart from the use of a third-party script to bypass AMSI, this infection chain is very similar to the one documented by [TrendMicro](https://www.trendmicro.com/en_us/research/24/f/water-sigbin-xmrig.html) and attributed to Gang 8220.

![Windows infection routine by 8220 gang intrusion set](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554bf_6a92a26ba2f46752fd010fcc_6a2a7e24e02555536e69ffc7.webp)

Windows infection routine by 8220 gang intrusion set

 _Figure 3. Windows infection routine_

### **Loader**

CCleaner is a loader written in .NET that performs the following actions:

  * It downloads a file from a specified URL : "_hxxp://154.213.192[.]44/Ueordwfkay.pdf_ "
  * The file is loaded into memory and decrypted using 3DES, resulting in a .NET DLL.
  * A class from the DLL is then loaded. While the exact invocation is unclear, this process downloads and executes an encrypted payload from "_hxxp://154.213.192[.]44/plugin3.dll_ ".
  * Finally it launches the cryptominer.



### **Cryptominer**

The cryptominer mines Monero through a private mining pool with the IP address _51.222.111[.]116:80_ , using a wallet identified as : _46E9UkTFqALXNh2mSbA7WGDoa2i6h4WVgUgPVdT9ZdtweLRvAhWmbvuY1dhEmfjHbsavKXo3eGf5ZRb4qJzFXLVHGYH4moQ_. [Ahnlab](https://asec.ahnlab.com/en/51568/) Security Emergency Response Center, in an April 2023 report, documented a similar infection chain involving this same wallet, linking it to the **8220 Gang**.

![pcap of the mining activity - Windows case](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554aa_6a92a26819d5c5953769b41e_6a2a7e24e02555536e69ffbc.webp)

pcap of the mining activity - Windows case

 _Figure 4. pcap of the mining activity - Windows case_

## **Linux**

The infection starts with the execution of two scripts: a shell script named "_c_ " and a Python script named "_y_ ".

  * The "**_c_** "script carries out three main tasks: disabling cloud protection tools like Aliyun, downloading and executing the Hadooken payload, and attempting to spread across the internal network using SSH. To move laterally, the script inspects various files, including the bash history, "/etc/hosts" and ".ssh/config". It then builds up lists to iterate through to attempt SSH brute force. If successful, it downloads and executes the initial infection script (“c” script).
  * The "**_y_** "script simply downloads and runs the Hadooken malware.



![Linux infection routine by 8220 Gang intrusion set with K4Spreader malware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554b9_6a92a26ca2f46752fd011090_6a2a7e24e02555536e69ffca.webp)

Linux infection routine by 8220 Gang intrusion set with K4Spreader malware

 _Figure 5. Linux infection routine_

### **K4Spreader**

K4Spreader is a Go-based malware, named Goku in the observed case, likely a reference to the character from the Dragon Ball manga. In its report, AquaSec suggests that the name "Hadooken" is a reference to the "Surge Fist" attack from the Street Fighter game. Similarly, the name "Goku" follows the same thematic connection.

The malware performs several malicious actions:

  * disabling various cloud security mechanisms;
  * searching for and terminates competing cryptomining processes to take control of the resources;
  * deploying additional malware, including the Tsunami backdoor and a PwnRig cryptominer, likely for Monero;
  * establishing persistence using cron jobs by creating two crontab entries: one that executes itself every 2 minutes and another that downloads "_c_ " script on "**_hxxp://sck-dns[.]cc/c_** " and runs it every 5 minutes.



In June 2024, [XLab](https://blog.xlab.qianxin.com/8220-k4spreader-new-tool-en/), a Chinese cybersecurity firm, also reported on the 8220 Gang's use of K4Spreader.

The analysed malware is not obfuscated, and the function names are notably clear and descriptive. While most are labelled in English, some are in Portuguese, which is unexpected considering that the intrusion set is believed to be of Chinese origin.

### **Tsunami**

Tsunami, is a Linux-based malware primarily used as a DDoS (Distributed Denial of Service) bot. It originated as Kaiten but evolved into Tsunami, which attackers use to launch large-scale [DDoS attacks](/blog/following-noname05716-ddosia-projects-targets) by flooding a target with traffic from infected machines. Once a system is compromised, Tsunami provides remote control capabilities, allowing attackers to issue commands, often leveraging the infected machine in botnets. It uses Internet Relay Chat (IRC) as its primary command and control (C2) protocol.

Three IRC C2 servers are configured with the IRC chan **_ircbot456@_** :

  * **_c4k-ircd.pwndns[.]pw_** : is an alias for _pwn.oracleservice[.]top_ and points to IP address 80.78.24[.]30. Numerous suspicious domains are linked to this IP, but the C2 appears inactive.
  * **_play.sck-dns[.]cc_** : the domain points to IP address _77.221.149[.]212_ and is functional. Its return banner includes the pattern "**_irc.bashgo[.]pw_** ".
  * IP address** _51.255.171[.]23_** : this server is also active and returns the same "**_irc.bashgo[.]pw_** " pattern.



C2s are based on UnrealIRCd software version 3.2.10.6. This is an old version released in December 2015 of this open source IRC server. By leveraging this information and the patterns found in the login banner, C2 servers can be tracked using the Censys engine. Upon analysis, the search results exclusively return C2s identified from the malware configuration.

Both K4Spreader and Hadooken use the "**_sck-dns[.]cc_** " domain for persistence by downloading the "_c_ " script. However, Tsunami uses the same domain as its command and control server. The IP address linked to this domain belongs to AS 210644, operated by Aeza. Notably, the attacking IPs are also from this AS, highlighting a potential connection between the operations and the infrastructure used in these attacks.

In an article from July 2022, [Sentinel One](https://www.sentinelone.com/blog/from-the-front-lines-8220-gang-massively-expands-cloud-botnet-to-30000-infected-hosts/) already associated these IOCs with Tsunami and the 8220 Gang intrusion set.

### **PwnRig**

The cryptominer deployed is PwnRig, a variant of XMRig. It is used to mine Monero through a private proxy mining pool reachable on "**_run.on-demand[.]pw_** ". This domain name points to three IP addresses (at the time of analysis):

  * _198.199.85[.]230_
  *  _64.227.170[.]227_
  *  _157.230.29[.]135_



In both Windows and Linux cases, the IP addresses configured as proxies for the mining pool are based on the same tool available on GitHub, xmr-node-proxy. These proxies can be tracked using the Censys tool, based on the default banner or TLS certificate define on [Dockerfile](https://github.com/Snipa22/xmr-node-proxy/blob/master/Dockerfile). The search returns approximately fifty servers.

![Censys overview of the TLS certificate for mining proxy](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554b6_6a92a2696568d7e2b40870cb_6a2a7e24e02555536e69ffc0.webp)

Censys overview of the TLS certificate for mining proxy

 _Figure 6 : Censys overview of the TLS certificate for mining proxy_

PwnRig establishes persistence using **cron jobs** , and also leverages **/etc/init.d/** and **systemd** services for maintaining persistence on infected systems even after reboots. The same wallet as for the Windows case is used : _46E9UkTFqALXNh2mSbA7WGDoa2i6h4WVgUgPVdT9ZdtweLRvAhWmbvuY1dhEmfjHbsavKXo3eGf5ZRb4qJzFXLVHGYH4moQ_. 

![pcap of mining activity - Linux case](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554b3_6a92a266db65986262ade7b7_6a2a7e23e02555536e69ffb3.webp)

pcap of mining activity - Linux case

 _Figure 7 : pcap of mining activity - Linux case_

Estimating the intrusion set’s current earnings is challenging. The wallet has been banned from certain mining platforms, such as XMRPool, due to suspicious activity. This suggests that, in addition to using mining proxies, the group may be operating its own mining pool, further complicating efforts to assess their financial gains.

## **Overlap with Hadooken case**

There are many parallels between this infection chain and the Hadooken case reported by AquaSec.

  * **Initial Access** : both intrusions target WebLogic servers, originating from the same AS, with similar script names ("_c_ " and "_y_ ") and using the unusual lwp-download binary.
  * **Infection Chain** : the "_c_ " script deploys the main malware (Hadooken or K4Spreader) and attempts SSH propagation, while "_y_ " drops the central malware. Both payloads deploy PwnRig and Tsunami.
  * **Payloads** : 
    * Both Hadooken and K4Spreader establish persistence via crontab to download c script on "_hxxp://sck-dns[.]cc/c_ ". 
    * PwnRig payload has the same hash in both cases and uses the same proxies "_run.on-demand[.]pw_ ", and wallet.



Based on the similarities observed in the infection chain, targeting methods, and payloads used, it is highly likely that the same intrusion set is behind both the Hadooken and K4Spreader campaigns. The use of similar matching script names ("_c_ " and "_y_ "), the shared mining proxies, the identical payload hashes, and the same Monero wallet point to one unique operation. 

A comparative analysis of Hadooken and K4Spreader suggests that they are two distinct Go-based malware variants with similar functionalities. While Hadooken's code does not contain any Portuguese terms, the presence of the K4Spreader pattern in Hadooken's strings indicates a connection that is unlikely to be coincidental. A more extensive analysis on a larger sample is necessary to determine whether there are any connections between these malware variants.

## **Victimology**

Joining the Tsunami IRC channel allowed us to identify the number of potentially compromised machines and view the IP addresses of those entering or leaving the channel. A comprehensive monitoring over several days indicates that the victim count fluctuates between 200 and 250 machines, 155 being identified over the last 5 days.

![Locating IPs infected by Tsunami](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a0c4c3270826c554bc_6a92a26dc5553634ac946c1d_6a2a7e24e02555536e69ffef.webp)

Locating IPs infected by Tsunami

 _Figure 8 : Locating IPs infected by Tsunami_

The IP addresses involved are primarily associated with cloud hosting services. A significant number of IPs belong to Oracle Cloud, which aligns with the attackers' focus on exploiting vulnerable servers.

According to Shodan scans, several IP addresses do not host any WebLogic services. However, we identified other vulnerable software that is known to be targeted by the 8220 Gang.

An analysis of several IPs using the Shodan search engine did not detect any WebLogic services. However, we observed the presence of other vulnerable software such as Drupal or Apache Struts, which is also known to be targeted by the 8220 Gang

Excluding the major cloud providers such as Amazon or Oracle Cloud, it becomes clear that Asia is the primary region affected. This is consistent with the activities of 8220 Gang, a Chinese intrusion set, potentially explaining the higher concentration of victims in Asia.

South America, particularly Brazil, appears to be more significantly impacted. This may be linked to the presence of Portuguese function names in the K4Spreader code. Sekoia assesses with low confidence that a South American operator, probably Brazilian, might have joined the 8220 Gang, potentially explaining the higher concentration of victims in this region. Given that our honeypot infected with the K4Spreader is located in Brazil, the concurrent campaigns involving K4Spreader and Hadooken could suggest that K4Spreader might be used by Brazilian operators, while Hadooken may be deployed by incumbents. However, this remains a working hypothesis, as Sekoia has no concrete proof, and further verification is needed to confirm this assumption.

## **Conclusion**

The tactics, techniques, procedures, payloads, and indicators of compromise observed in the intrusion on our honeypot strongly suggest the involvement of the 8220 Gang. The tools and methodologies used in the compromise are consistent with the group's known patterns. The malicious activity and infrastructure identified in this case align with previously documented campaigns attributed to the 8220 Gang.

Further cross-referencing with the Hadooken compromise documented by AquaSec strengthens the links to the 8220 Gang. Both compromises share common elements, including similar TTPs, payloads like cryptomining malware, and IOCs. These parallels provide strong evidence that the same intrusion set is responsible for both attacks, further solidifying the connection to 8220 Gang's activities.

The victimology suggests a particular focus on South America by the intrusion set, potentially due to the more recent involvement of a Brazilian operator who may have joined the team. However, this remains a working hypothesis that requires further validation.

These cases highlight that the 8220 Gang remains active and continues to evolve its techniques and payloads. Their ongoing exploitation of cloud environments, combined with their ability to adapt and enhance their malware tools, shows that they are still an opportunistic threat.

## **IoCs**

The list of IoCs is available on [Sekoia.io GitHub repository](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/8220Gang/8220_Gang_iocs_20242409.csv)

Thank you for reading this blogpost. **We welcome any reaction, feedback or critics about this analysis. Please contact us on tdr[at]sekoia.io**.