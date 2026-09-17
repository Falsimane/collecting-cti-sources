# Free Community Tool: CrowdInspect

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/free-community-tool-crowdinspect/
- **Date :** February 28, 2013

---

# Free Community Tool: CrowdInspect

February 28, 2013

• [ Robin](/en-us/blog/author.robin/ "Posts by Robin") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

CrowdInspect is a free community tool for Microsoft Windows systems from CrowdStrike aimed to help alert you to the presence of potential malware that communicates over the network that may exist on your computer. It is a host-based process inspection tool utilizing multiple sources of information, including [VirusTotal](http://www.virustotal.com), [Web of Trust (WOT)](http://www.mywot.com), and Team Cymru's Malware Hash Registry to detect untrusted or malicious network-active processes. CrowdInspect can be used during Incident Response process to rapidly identify potential malicious running processes on a machine. The tool runs on both 32 bit and 64 bit versions of Windows from XP and above. Beyond simple network connections, CrowdInspect associates the connection entry with the process that is responsible for that activity. It can display the process name as a simple file name or as as an optional full file path. In addition to the process name, the entry's process ID number, local port, local IP address, remote port, remote IP address and reverse resolved DNS name of the remote IP address is shown. The tool accommodates both IPv4 and IPv6 addresses. CrowdInspect records details of any entry that is associated with a remote IP address and maintains a chronological list of these accessed by clicking the "Live/History" toolbar button to switch between the regular live netstat window and the history list window. Perhaps the most useful aspect of CrowdInspect though is its ability to utilize several sources of information that can be used to determine the reputation of the process using the network connection and the reputation of the domain it is connecting to. This is achieved through the use of the following technologies and services: **Thread Injection Detection** Detection of code injection using custom proprietary code Many pieces of malware achieve part of their goal by manipulating already running applications and injecting themselves into those processes. Regular antivirus products that only act upon the actual physical file contents would not identify this behavior. CrowdInspect features experimental detection of such behavior and the results of this test on each process can be seen in the “Inject” column.

  * \--

(o Gray icon)
    * Not applicable/not available. No process is not able to be tested.



  * ??

(o Gray icon)
    * The process did not allow us to test for code injection.



  * OK

(o Green)
    * The process did not appear to have any evidence of thread injection.



  * !!

(o Red icon)
    * The entry appeared to have had a thread injected into its process. This is generally not a good thing or something usually encountered. Note though that there may be some classes of specialized software that does exhibit this behavior. The process/application should be investigated further.



**VirusTotal** Multiple antivirus engine analysis results queried by SHA256 file hash <http://www.virustotal.com> Shown in the "VT" column of the tool are the basic summary results of querying the VirusTotal service against the file in question (actually the SHA256 hash of the file contents). VirusTotal utilizes multiple antivirus engines to analyze submitted files and we query its database to see if the file hash is in the database and if so, how the antivirus engines rated it. The value here can be one of the following:

  * \--

(o Gray icon)
    * Not applicable/not available. No connection to the VirusTotal database was made or the process is not associated with a file.



  * ??

(o Gray icon)
    * The entry does not exist in the VirusTotal database. This is probably good!



  * 0% ... 100%

(o Green ... o Red icons)
    * The file is known to the VirusTotal database. This is the virus score. 0% means no antivirus vendor reported an issue with the process (very good). 100% means every antivirus vendor reported the process as problematic (very bad!)



More extensive details for the particular selected entry in the list can be seen by either clicking the "AV Results" toolbar button or selecting "View AV Test Results" from the right-click context menu for the selected item. Note that it may take a short while before the results appear for each entry in the list due to rate throttling of connections to the service. **Team Cymru - Malware Hash Repository** Repository of known malware queried by MD5 file hash http://www.teamcymru.com Shown in the "MHR" column, Team Cymru maintains a repository of known malware that can be queried given an MD5 hash of the file contents. In this case we are simply querying for a yes/no answer so the results can be one of the following:

  * \--

(o Gray icon)
    * Not applicable/not available. No response was received from the Team Cymru service or the process is not associated with a file.



  * ??

(o Gray icon)
    * The entry does not exist in the MHR database. This is probably good, although the absence of a positive response doesn't necessarily mean the process is not malware.



  * !!

(o Red icon)
    * The entry DOES exist in the MHR database. The process is known to be malware. This is bad.



**Web of Trust** Crowd-sourced domain name reputation system <http://www.mywot.com> Shown in the "WOT" column column of the tool are the basic summary results of querying the Web of Trust service against the reverse resolved domain name associated with the remote IP address of the connection's entry. The value here can be one of the following:

  * \--

(o Gray icon)
    * Not applicable/not available. No connection to the WoT database was made or the entry's remote IP address does not have a usable valid domain name associated with it.



  * ??

(o Gray icon)
    * The entry does not exist in the WoT database.



  * 0% ... 100%

(o Red ... o Green icons)
    * The WoT reputation score. 0% means that everybody who has rated this domain thinks it is untrustworthy. 100% means that everybody who has rated this domain thinks it is reputable and can be trusted.



To avoid unnecessary querying of the above services all results are cached such that no unique process or domain is ever queried more than once for the duration the tool is running. See the images below showing how to use the tool’s many features. Main live window of the CrowdInspect tool showing toolbar usage ![](https://lh5.googleusercontent.com/scy7d6cFxA4wyF8-_I8am3BVGaJEsnnJ4CBMMY-I37BvbKJGD_0RPsFkw1-foFj-0TfyBu8Xh3NJus1wuZEH6R1g3zfTdTW2xfhHebCSs_yDHINmT3ZN_HMpKw) The History window of the CrowdInspect tool showing chronological record of connections and context menu ![](https://lh3.googleusercontent.com/txzJTq9GQwye6v1ewgrFms31iDIIV103m1CK9W1UgqT1n1JpJe0dUs8P293MCXb53SPFZbc5eCJeQcizuZaQe_JbbuFXdsNAfoM5Y2gAhg_e2uq8KhdMq8aZqA) CrowdInspect showing detailed AV results for the selected item ![](https://lh6.googleusercontent.com/5IPHtxo87eTeOYm7oYbikIAZ17iaTw6n6LDcukZVXpCpqwQ4jEi_lh6WatzoQeWJsAUCR0ejQYd35P4Zt4r0sLwZQdm8QJunY9xVaNk2yuBfxy_ODV2mtsn9jg)

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)