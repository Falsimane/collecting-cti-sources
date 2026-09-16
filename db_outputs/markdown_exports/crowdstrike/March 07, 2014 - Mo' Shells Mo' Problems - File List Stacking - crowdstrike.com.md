# Mo' Shells Mo' Problems - File List Stacking - crowdstrike.com

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/mo-shells-mo-problems-file-list-stacking/
- **Date :** March 07, 2014

---

# Mo' Shells Mo' Problems - File List Stacking

March 07, 2014

• [ RyanJ](/en-us/blog/author.ryanj/ "Posts by RyanJ") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")• [From The Front Lines](/en-us/blog/category.from-the-front-lines/ "From The Front Lines")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

**Disclaimer:** CrowdStrike derived this information from investigations in non-classified environments.

Since we value our clients’ privacy and interests, some data has been redacted or sanitized. In our first blog post, “Mo’ Shells Mo’ Problems: Deep Panda Web Shells - Part 1”, we discussed two web shells leveraged by a Chinese threat group we call Deep Panda.

In case you forgot, a web shell is a file containing backdoor functionality written in a web scripting language such ASP, ASPX, PHP, JSP or CFM.

When a web shell is hosted on an internet facing victim system, an adversary can remotely access the system to perform malicious actions. Today we’ll cover one of three ways to help hunt for web shells in your environment: file stacking.

We often use this method during investigations to help identify web shells in environments where they would normally go unnoticed.

An adversary typically creates web shells on only a small number of servers in a victim environment, providing us with a “needle in many haystacks” problem.

Luckily, most servers in an organization have very little end user interaction and contain far less user artifacts than a typical workstation.

As a result, it is typically easier to identify anomalies on servers. The main goal of file stacking is to identify outliers.

By identifying uncommon files across a set of servers, we hope to find the most uncommon file type of all, malware. In the case of web shells, there are certain search criteria we may want to adopt to speed up our efforts: 

  * If the environment is a mix of Windows Server and other web hosting solutions (such as Apache Tomcat and Adobe Cold Fusion), search for extensions of ASP, ASPX, JSP, PHP and CFM.
  * Focus searches on %systemdrive%Inetpubwwwroot, %programfiles%Apache Software Foundation, %systemdrive%ColdFusion<version> and other file paths to 3rd party web hosting solutions in your environment. 
  * If the environment is Windows based with no other 3rd party web hosting solutions, limit search to %systemdrive%Inetpubwwwroot and search for extensions ASP and ASPX.



This will restrict to searching only for scripts that are accessible externally from the internet. 

**File Stacking with Timestamps**

To illustrate file stacking, consider the following real world network: 

  * Predominately Windows environment 
  * About 200 Servers 
  * Usage of third party web hosting solutions 



In this example, the wide variety of custom web applications causes many legitimate and unique web scripts across the enterprise.

It would be extremely difficult to identify web shells solely based upon file occurrences in this environment.

However, by restricting the search to the aforementioned criteria and sorting by file creation time, we can identify uncommon web scripts not created at similar times to one another.

We would normally expect groupings of web scripts to be created in succession if they are part of a normal deployment by an administrator or part of an installation.

Files that do not adhere to this model are worth looking at further.

Our method of filtering by file path and extension, coupled with sorting by file creation time, helps identify suspicious outliers.

Pretty straightforward, right? Here’s how it looks in this network: Ignoring my previous search criteria advice and searching for all the aforementioned extensions, results in 179,231 files found on the 200 servers in our example environment.

I don’t know about you, but I don’t often have the time to sift through 179,231 web scripts.

Limiting our search criteria to specific directories results in 1,671 files, a significant improvement.

Timestamp analysis can be used to further reduce this set, and we were most interested in files created between April and November 2013. The below table shows an abbreviated listing of the file stacking results for the 200 windows servers in the sample victim organization, sorted by file creation time: [![fls table1](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/03/fls-table1.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/03/fls-table1.png) Referencing Table 1, the web scripts on Servers 1 and 4-6 appear to be created contemporaneous with one another and all reside in the same directories.

This type of activity is likely a result of legitimate installation of a 3rd party application or other custom applications used for legitimate purposes within the organization.

However, you can also see two particular web scripts that stand out: 

  * C:inetpubwwwrootaspnet_clientsystem_web<VERSION>system_web.aspx 
  * C:Inetpubwwwroot_wmcscertificationPassportRedirector.aspx 



Both of these scripts were created at isolated times from all other web scripts created between our target dates of April 2013 and November 2013.

Further investigation of PassportRedirector.aspx, showed it to be a false positive related to the Windows Rights Management – Account Certification Service. Taking a closer look at System_web.aspx shows us it was created at an atypical time of 3:35:17 UTC (Roughly 23:35:17 EDT).

This suggests it may not have been created by an administrator during normal business hours.

Upon further inspection, this file indeed was a web shell covered in our first post “Mo Shells Mo’ Problems: Deep Panda Web Shells - Part 1”. 

**File Stacking with File Paths**

We can also search on full file path, using the same data above, to identify web scripts that are not grouped with others.

Additionally, we’ll be on the lookout for files in unusual or unique locations. Table 2 shows an abbreviated listing of the file stacking results for the 200 windows servers in our sample victim organization, sorted by full file path: [![fls table2](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/03/fls-table2.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/03/fls-table2.png) In Table 2, the web scripts on Servers 1 and 3 appear to be consistently residing in the same subdirectories.

This type of activity suggests that these web scripts may have been part of a 3rd party installation or custom application.

We can also reference the file creation times and see that these scripts were all consistently created around the same time as one another. Looking again at Server 2, you can see our malicious Deep Panda web shell stand out: 

C:inetpubwwwrootaspnet_clientsystem_web<VERSION>system_web.aspx System_web.aspx is the only file across all 200 systems that resides in that specific subdirectory. We can also perform similar sanity checks on individual servers.

If we look at all files with web script extensions on Server 2, there are a total of 616 files returned.

Table 3 shows an abbreviated listing of these results. [![fls table3](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/03/fls-table3.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/03/fls-table3.png) Interestingly, System_web.aspx was the only web script located in C:inetpubwwwroot.

This directory is publicly accessible through the internet and it is extremely unlikely that an application would only have one web script to provide its functionality to an end user.

If this location is legitimate, where are the other scripts?

The fact that System_web.aspx was the only web script hosted publicly by this web server is highly suspicious. 

**Summary**

  * Focus searching on only web servers in an environment 
  * Filter for extensions ASP, ASPX, JSP, PHP and CFM 
  * Limit searches to: - %systemdrive%\Inetpub\wwwroot - %programfiles%\Apache Software Foundation - %systemdrive%\ColdFusion<version> \- Other 3rd party web hosting solutions 
  * Sort by file creation time 
  * Sort by full file path In our next post, we will dissect web logs to help identify web shells in your environment.



In the meantime, **[register now](https://attendee.gotowebinar.com/register/8497096584722200321) **for the April 1st CrowdCast.

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)