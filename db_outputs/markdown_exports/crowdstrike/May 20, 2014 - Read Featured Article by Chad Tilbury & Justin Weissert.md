# Read Featured Article by Chad Tilbury & Justin Weissert

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/new-crowdresponse-modules/
- **Date :** May 20, 2014

---

# New CrowdResponse Modules

May 20, 2014

• [ ChadJustin](/en-us/blog/author.chadjustin/ "Posts by ChadJustin") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

During his talk at this year’s RSA conference, George Kurtz introduced a new free community tool named CrowdResponse.

CrowdResponse is a robust data-gathering platform that we intend to continue improving with new modules and data acquisition capabilities.

Today we are releasing three additional modules for CrowdResponse – Drivers, Handles, and Strings. These modules focus on memory analysis and are extremely pertinent to detecting much of the malware that we have been discussing lately. **The New Modules** One of the key themes of April’s [“Going Beyond the Indicator” CrowdCast](https://vimeo.com/90687936) was hunting and detecting.

We outlined techniques to hunt for webshells and memory-resident malware. 

An increasing amount of malware is taking steps to reduce the disk footprint.

While YARA scans can be particularly useful for finding signatures in memory, sometimes you need more data to verify your results.

Thus, we chose to focus this month on adding memory-related modules into CrowdResponse.

The following modules are now part of the free v1.0.2.0 release: 

  * Drivers (@Drivers) - Information on Win32 drivers
  * Handles (@Handles) – Enumerate process handles
  * Process Strings (@PSStrings) – Extraction of strings from the memory of running processes

These modules provide the incident responder with the following data: **@Drivers**

  * Name of driver
  * Base address of driver
  * Full file details (as with @Pslist)
  * Optional verification of digital certificates (-c)

**@Handles**

  * Dump handle IDs, type and name from all processes
  * Optional dumping 

by specified process ID (-p)

**@PSStrings**

  * Extract ASCII strings from process memory
  * Extract Unicode (double-byte) strings from process memory
  * Identify the process ID for each string (-p to operate on individual PIDs)
  * Option to specify minimum and maximum string lengths
  * Option to specify character set to use
  * Ability to ignore strings containing certain characters
  * Optional ability to show memory offsets where strings are found
  * XOR process strings with a one byte key



## CrowdResponse in Action

We [previously](/en-us/blog/mo-shells-mo-problems-web-server-log-analysis/index/) described several methods to identify webshells on a system.

While webshells are notoriously difficult to find initially, they are often vulnerable to subsequent signature-based detection.

To illustrate this, we will use a ASP.NET webshell attributed to the Deep Panda adversary group.

Attacker capabilities are often hard to conceptualize through blog posts, reports, or even webinars. Whether you are a visual learner or just prefer to see things live, our Services team recorded a quick video to highlight one of the more advanced webshells we have seen in the wild.  [Web Shells](http://vimeo.com/95300159) from [CrowdStrike](http://vimeo.com/crowdstrike) on [Vimeo](https://vimeo.com). The video shows how the webshell uses authentication mechanisms to evade detection as well as some actions it can execute once installed.

While not all of the webshell capabilities were captured in the video, you can read an in-depth analysis of the webshell [here](/en-us/blog/mo-shells-mo-problems-deep-panda-web-shells/) and see the interface in Figure 1 below.

[![Figure1](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure1.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure1.png) Figure 1. ASP.NET Webshell Screen Capture

Since we are celebrating the first release of additional capabilities within CrowdResponse, we thought it would be interesting to demonstrate how you could use the new modules to help detect this webshell. Step one: YARA.

To build a YARA signature we analyzed two files associated with the webshell:

**system_web.aspx** and **App_Web_6bl2f3yv.dll.

** The attackers left behind the former, and the webserver created the latter.

When working with Microsoft IIS and ASP.NET, it is important to understand that the web server does not run .aspx pages natively.

IIS compiles the page upon its first request to increase performance and stability.

After its first use, IIS largely ignores the .aspx file and instead loads and executes the compiled DLL file when the webshell is used. When building signatures for these types of files, you will want to make sure you can detect both the original .aspx file for file-system detection and the .dll for both memory and file system detection.

Since we have new memory modules to play with, we’ll focus on the .dll file in this example.

In fact, the compiled file signatures can be more valuable because attackers often leave the .dll files behind after performing cleanup. In this example, we found the compiled version of **system_web.aspx** within the following folder: C:WindowsMicrosoft.NETFramework64v2.0.50727Temporary ASP.NET Files [![Figure2](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure2.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure2.png) Figure 2. Compiled ASP.NET Pages

Notice the file **system_web.aspx.33154034.compiled** displayed in Figure 2.

This is a XML file created during ASP.NET compilation and records the mapping between a specific .aspx page and its corresponding .dll.

Analysis of **App_Web_6bl2f3yv.dll** identified several strings used to build the following YARA signature: rule CrowdStrike_CSIT_14004_02 : loader backdoor bouncer { 

meta:

description = "Deep Panda Compiled ASP.NET <http://ASP.NET> Webshell"

last_modified = "2014-04-25"

version = "1.0"

report = "CSIT-14004"

in_the_wild = true

copyright = "CrowdStrike, Inc"

actor = "DEEP PANDA"

strings:

$cookie = "zWizx00" wide

$cp = "es-DN" wide

$enum_fs1 = "File system: {0}" wide

$enum_fs2 = "Available: {0} bytes" wide

$enum_fs3 = "Total space: {0} bytes" wide

$enum_fs4 = "Total size: {0} bytes" wide

condition:

($cookie and $cp) or all of ($enum*) } The first two strings are from the webshell’s authentication checks: looking for a specific cookie name (zWiz) and the browser’s preferred language (es-DN).

The “$enum” references are labels used in a function within the original code.

With our YARA signature in place, we can run a quick scan of our web servers using the following command line:

CrowdResponse.exe @yara -a

-b -o -v -y <location-of-yarafiles>

This command scans process memory and, as seen in Figure 3, our new signature hits on the w3wp.exe process that handles web requests for IIS. [![Figure3](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure3.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure3.png) Figure 3. CrowdResponse @yara Hit in w3wp.exe Process

The scan produced a second hit due to the inclusion of the (-o) operator which also scans the loaded modules of active processes.

In this case, it identifies the compiled dll loaded from the Microsoft.NET folder (Figure 4). [![Figure4](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure4.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Figure4.png) Figure 4. YARA Hit in Loaded Modules of Process w3wp.exe **HANDLES** An alternative way to find the compiled webshell is to review files handles for the w3wp.exe process.

Handles tell us what resources a process has open, and in the case of the w3wp.exe process, they should identify recent content served.

We can use the new handles module in CrowdResponse with this command (for process ID 3196): 

CrowdResponse.exe @handles -p 3196

Table 1 shows several results from the Handles output for the w3wp process, including the full path of the compiled webshell. 

[![Table1](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Table1.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Table1.jpg) Table 1: CrowdResponse @handles Output

**STRINGS** Extracting the strings of a process allows verification of the YARA signature hit and can provide additional clues as to what was executing within the process.

The new @PSStrings module can gather this information for us. 

CrowdResponse.exe @psstrings -p 3196

In the output, we see several code fragments we targeted in our YARA signature.

The full path of the webshell and its compilation files are also present.

Reviewing this output may help identify other malicious activity on the system, including attacker page requests and returned output. [![Table2](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Table2.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Table2.jpg) Table 2: CrowdResponse @ psstrings Unicode Output for w3wp.exe process

[![Table3](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Table3.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/05/Table3.jpg) Table 3: CrowdResponse @psstrings Unicode Output Validating Signature Hits

## Conclusion

Using some old and new CrowdResponse capabilities, we identified a compromised system, verified our hits, and identified files comprising a webshell.

Next steps might include running the @dirlist module to get more detailed information on the webshell files, and taking a memory/disk image.

Keep in mind that all of the CrowdResponse commands can (and should) be scripted via a simple config file.

We did not demonstrate @drivers (driver information) in this post, but full details can be found in the user guide. The CrowdStrike team is committed to developing and delivering [free community tools](/en-us/community-tools/index/) like CrowdResponse, CrowdInspect, Tortilla, and the new Heartbleed Scanner.

If you have any questions or would like additional information on our [services](http://services.crowdstrike.com), [products](/en-us/technology/index/), or [intelligence](/en-us/intelligence/index/) offerings, please reach out to us directly. For immediate assistance with an Incident Response, the CrowdStrike Services team can be contacted at 1.855.CROWDIR (276-9347) or via our [contact ](http://services.crowdstrike.com/contact/index.html)page. 

## CrowdResponse v1.0.2.0 Details

**Download CrowdResponse v1.0.2.0**[**here**](/en-us/community-tools/index/)**.** In the downloaded ZIP file, you will find a number of files: ·

**CrowdResponse.exe

**

o

The host data gathering tool ·

**Config.txt**

o

An example configuration file for _CrowdResponse_ intended to show usage of the various options and functions 

o

In addition to the Derusbi rules from the last release, we’ve added new YARA rules to detect the Deep Panda .NET webshell. ·

**CRconvert.exe**

o

A tool used to convert the native XML output from _CrowdResponse_ into different formats ·

**readme.html**

o

Detailed syntax and usage descriptions for the _CrowdResponse_ tool ·

**readme-crconvert.html**

o

Detailed syntax and usage descriptions for the _CRconvert_ tool ·

**EULA.rtf**

o

The CrowdStrike End User License Agreement for _CrowdResponse_ ·

**CrowdResponse User Guide.pdf**

o

The detailed user guide for _CrowdResponse_

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)