# Cyber Espionage & Strategic Web Compromises – Trusted Websites Serving Dangerous Results

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/cyber-espionage-strategic-web-compromises-trusted-websites-serving-dangerous-results/
- **Date :** 2012-05-15

---

# Cyber Espionage & Strategic Web Compromises – Trusted Websites Serving Dangerous Results

May 15, 2012

_By Steven Adair and Ned Moran_

In the last year, attackers engaged in cyber espionage have increasingly turned to the web to distribute their malware via drive-by exploits. The idea of distributing malware via drive-by exploits is not new at all. Internet users are constantly at risk from a daily barrage of exploits across the web as a result of mass SQL injections, malicious advertisements, stored cross site scripting (XSS), compromised web servers, etc. In most cases the miscreant’s goal is to serve malicious exploits to as many people as possible from as many locations as they can. This is where the advanced attackers engaged in cyber espionage campaigns tend to set themselves apart from the others and narrow their focus through what we call _strategic web compromises._

The goal is not large-scale malware distribution through mass compromises. Instead the attackers place their exploit code on websites that cater towards a particular set of visitors that they might be interested in. In the past few years we have witnessed several strategic web compromises of organizations in a variety of fields with a recurring focus on those involved with freedom of speech, human rights, defense, foreign policy and foreign relations. In these cases, normally trusted websites have been compromised to serve up malicious code designed to give backdoor access into the systems of unsuspecting visitors. In general a well patched system will be immune from many of the attacks, but in several cases previously unknown 0-day exploits (no available patch) have found their way onto these sites — in short the average visitor may not have much of a chance to defend themselves.

A simple one line code addition to a website, such as those seen below, can set off a chain reaction that can spell disaster for an organization.

> [![Amnesty Internatlion Hong Kong \(CN Language Pages\) iframe](https://www.shadowserver.org/wp-content/uploads/2018/06/aihk-iframe1.png)](/wp-content/uploads/2018/06/aihk-iframe1.png)
> 
> Flash Exploit iFrame Link 1
> 
> [![CDI iframe](https://www.shadowserver.org/wp-content/uploads/2018/06/cdi-iframe.png)](/wp-content/uploads/2018/06/cdi-iframe.png)
> 
> Flash Exploit iframe Link 2

## Exploit de Jour

Right now, as you read this, there are a few recent exploits that are being heavily used by attackers engaged in cyber espionage to take a foothold onto various networks. In particular, in the past two weeks, we have seen several strategic web compromises utilize the most recent Oracle Java (CVE-2012-0507) and Adobe Flash (CVE-2012-0779) vulnerabilities. The Java vulnerabilities have been exploited to install malware on both Mac and Windows systems. Macs have been hit fairly hard in [recent months](http://news.drweb.com/show/?i=2341&lng=en&c=14), most notably with crimeware via a variant of malware dubbed FlashBack. However, advanced threat malware targeting Human Rights organizations and those in the foreign policy space have also been observed utilizing this exploit to target both OS in more limited attacks.

### WARNING: Live Flash and Java Exploits on the Loose

In the last few weeks there has been a notable increase in strategic web compromises used to serve the most recent Flash exploit (targeting Windows users). At the time of this writing, several high profile websites are still compromised and serving the most recent Flash exploit. If successful the exploit will drop malware from attackers typically labeled as the advanced persistent threat or “APT.”

We must warn against visiting the exploit sites listed in this blog as well as the compromised websites (until clean) as well. At the time of this writing (the morning of May 14, 2012) the websites for the Center for Defense Information, Amnesty International Hong Kong, and the Cambodian Ministry of Foreign Affairs ASEAN 2012 are compromised and serving one of the hostile iFrames. Visiting these websites can initiate a chain reaction in which malicious code is loaded from multiple websites and results in a system compromise for vulnerable systems without other mitigating factors.

### Amnesty International Hong Kong (AIHK)

Last week Websense [reported](http://community.websense.com/blogs/securitylabs/) that the main page of the Amnesty International United Kingdom (AIUK) website was compromised and serving Java exploits. Working with Websense we happened upon a Flash exploit site hosted on the webserver of a Library in Romanian (seen in iFrame picture above). We were able to track this exploit site back to an iFrame on the Amnesty International Hong Kong’s (AIHK) Chinese Language pages (_www.amnesty.org.hk/chi_). The main website no longer appears to be serving exploit code, however, the portion of the website that is in Chinese serves up this new Flash exploit code. While we do not have any direct ties between the attackers that compromised the AIUK website last week, we can see a clear connection between the attackers that have currently compromised the AIHK website and the attackers that compromised the AIUK website late last year. The AIUK compromise was detailed in a [report](https://krebsonsecurity.com/2011/12/amnesty-international-site-serving-java-exploit/) by Brian Krebs late last year. In this most recent attack, malicious HTML is loaded by the AIHK website from **www.bjc.ro** (**86.122.14.140**). The page in turn makes a connection to **71.6.131.8:80** and then downloads an XOR (0x95) encoded executable from **www.bjc.ro**. The malicious executable drops a backdoor that phones home to **glogin.ddns.us**.

### Center for Defense Information (CDI)

The website of the Center for Defense Information (CDI), _www.cdi.org_ , a DC-based NGO that researches Defense and Security policy has been compromised multiple times in the last few weeks. The CDI website is currently serving up a malicious Flash exploit that ties back attackers known to engage in cyber espionage. This threat group appears to be interested in targets with a tie to foreign policy and defense activities. Also interesting is that the website housing the malicious Flash exploit ties back to Gannet Company, Inc. and USA Today (**159.54.62.92**). Additional components of the exploit chain are located on systems that reside in Korea (**222.239.73.36:443**) and Austria (**www.audioelectronic.com/213.33.76.135**). Ultimately, if the exploit chain is successful, a variant of the popular Poison Ivy remote access trojan (RAT) is installed on the system. The Poison Ivy RAT phones home to **windows.ddns.us**(currently hosted on the Korean IP address **222.122.68.8**).

**Note:** The main websites related to USA Today and Gannet Company, Inc do not appear to be affected.

The image below details the exploit chain for this particular compromise. It can be used a general guidance to understand how these exploits work in general as well.

[![CDI Exploit Chain](https://www.shadowserver.org/wp-content/uploads/2018/06/cdi-flash-exploit.png)](/wp-content/uploads/2018/06/cdi-flash-exploit.png)

cdi.org Exploit Chain (click to enlarge)

A prior compromise of the CDI website redirected victims, via a hidden iframe, to Java exploit (CVE-2012-0507) host at **194.183.224.73**. This exploit chain dropped a Poison Ivy RAT that connected to a command and control server at **ids.ns01.us**.

### Cambodian Ministry of Foreign Affairs (MFA) – ASEAN 2012

The website for the Cambodian Ministry of Foreign Affairs (MFA),  _www.asean2012.mfa.gov.kh_ , has also been compromised to point to both Flash and Java exploits. Both the Flash and Java exploits were identical to those hosted on the CDI website.

(UPDATE: We’d like to extend a special thanks to our friend Kurt Baumgartner at Kaspersky Labs for providing details related to this compromised website.)

### International Institute for Counter-Terrorism (ICT)_  
_

The websites for the International Institute of Counter-Terrorism at the Interdisciplinary Center (IDC) in Herzliya, Israel,  _www.ict.org.il_ , is also currently compromised and is housing a Java exploit (CVE-2012-0507). In this attack the website has a JavaScript file that has been modified to contain obfuscated script that points to an exploit file hosted on the website of the U.S.-based Auto Association. If the exploit is successful another Poison Ivy RAT is installed on the system. The malware from this installation calls back to **javaup.updates.dns05.com**. The keylogger for the RAT is not enabled by default.

### Other Recent Compromises by Same Attackers

In the past few weeks there have been several other websites that have been compromised by the same set of attackers responsible for the malicious code listed above. The primary exploits used in these attacks again targeted CVE-2012-0779 and CVE-2012-0507. These websites appear to have been cleaned up at the time of this writing. We would also like to note that while investigating the AIHK compromise, we found artifacts indicating that APT attackers are likely targeting the International Service for Human Rights (ISHR). We proactively scanned through three websites associated with ISHR in Germany (DE), Switzerland (CH), and the United States (US) and did not find any indication of compromise. However, we urge people from this organization and similar organizations to remain vigilant for web and e-mail based attacks.

### American Research Center in Egypt (ARCE)

Google-cache results indicate that the American Research Center in Egypt, www.acre.org, was briefly compromised last week with an iframe pointing the the Gannett/USA Today site that had also been found on the CDI website. The compromised page’s content is still in Google’s cache and is dated May 7, 2012.

### Institute for National Security Studies (INSS)_  
_

Earlier this month the Israeli website for the Institute for National Security Studies (INSS), _www.inss.org.il_ , fell victim to APT attackers and was housing JavaScript that loaded the same iFrame code that is currently on the Cambodian MFA ASEAN 2012 website. The compromise was detailed by [Websense](http://community.websense.com/blogs/securitylabs/archive/2012/05/02/the-israeli-institute-for-national-security-studies-lead-to-a-posionivy-infection-flow.aspx) on May 2, 2012. As previously noted, this exploit would load malicious code from a Belgium webserver located at the IP address **194.183.224.73**.

### The Centre for European Policy Studies (CEPS)_  
_

Earlier this month the Centre for European Policy Studies (CEPS), _www.ceps.eu,_ was also compromised with the same code that pointing back to the malicious Belgium server located at **194.183.224.73**. This website also appears to have been cleaned since and has not been observed hosting Flash exploits.

## A Closer Look at the Most Recent Flash Exploit (CVE-2012-0779)

On May 4, 2012, [Adobe Product Security Bulletin 12-09](https://www.adobe.com/support/security/bulletins/apsb12-09.html) (APSB12-09) was released patching a critical vulnerability in Adobe Flash. At the time of this patch release, there were already reports of this exploit being used in the wild in targeted attacks. Since this time we have observed this exploit being used in several different targeted attacks, many of which are detailed above in this post. The exploit has some interesting similarities to a previous Flash exploit that was used in targeted attackers (CVE-2011-2110). We previously detailed this exploit in a blog post last June. We will detail the exploit by breaking down the exploit chain as seen in the CDI compromise image above in six different steps (step 0 – 5). Additional we will denote some other interesting artifacts discovered from decompiling the Flash exploit file.

#### Step 0:

The initial step in the process is for the attacker to compromise their strategically determined website. This may be done as a target of opportunity (several sites of interest but only one with a vulnerability), as a result of already having a foothold in a particular infrastructure (compromised internal infrastructure or web admin), or due to heavy scanning and targeting of a specific selected website until access is gained (vulnerability, cracked password, misconfiguration, etc.). The attackers frequently either have full control of the website or perfor SQL injection attacks to add links to their malicious code. In the case of the CDI website, we do not know how the attackers gained access to the websites. However, they were able to place the most recent iframe link at the very top of the homepage.

#### Step 1:

Unsuspecting user visits the website _www.cdi.org_. Along with all of the legitimate content of the website, malicious iframe pointing to http://159.54.62.92/images/image.html is sent to the user’s browser.

#### Step 2:

The user’s browser will make a request for “/images/image.html” on the 159.54.62.92 webserver. This in turn will check the user’s browser to see if they have particular versions of Windows:

[![](https://www.shadowserver.org/wp-content/uploads/2018/06/159-vercheck.png)](/wp-content/uploads/2018/06/159-vercheck.png)

OS Version Check Script

As seen in the snippet above, the Flash file (**BrightBalls.swf**) has two parameters: _“Elderwood_ ” and _“birthday_ “. Both parameters appear to have hex values. However, these values do not simpl decode back to readily strings. The first parameter, Elderwood, is identical to what we saw with CVE-2011-2110. The value is an address that has been ZLIB compressed and then XOR encoded with 0x7A. The Elderwood value decodes to **222.239.73.36:443**. The second parameter, birthday, is a URL that is XOR encoded with 0xE2 and decodes to **_http://www.audioelectronic.com/download/images/f/flash.gif_**.

#### Step 3:

The unsuspecting user’s Flash decodes the aforementioned Elderwood value and initiates a Real Time Messaging Protocol (RTMP) connection to **222.239.73.36** on TCP port 443. The attacker must have the server listening and responding to complete the exploit chain for it to move on to the next step. The communication on port 443 is not encrypted or SSL/TLS and would stand out if looking through network traffic. The Elderwood value can decode to an IP or DNS port pair and is not restricted to any particular port.

#### Step 4:

After successfully completing the RMTP communications, the _birthday_ parameter from the SWF file is decoded and the system downloads _/download/images/f/flash.gif_ from www.audioelectronic.com. Needless to say, this GIF file is not actually an image. It is an EXE file that has been XOR’d with 0x95.

#### Step 5:

Once the system has XOR’d the flash.gif file, it now has a valid Poison Ivy RAT binary. The RAT is installed to the system and begins to beacon to **windows.ddns.us** on TCP port 443.

## A Look into the SWF File

The malicious SWF file found on each exploit site referenced above (as well as a few not listed) are all the same file. The details of the file are as follows:

> Filename: BrightBalls.swf  
>  File Size: 8884  
>  MD5: 1EC5141051776EC9092DB92050192758  
>  SHA1: 5523b0d94d4ed3ddbb3eb6ad40640ded318c8ea7

A closer look into this file reveals some interesting information. We we able to use two different basic techniques to extract the metadata from these flash files. The first technique leveraged the free tool flasm available at http://www.nowrap.de/flasm.html. Running this tool with the –d parameter will disassemble the specified flash file. Alternatively, as a second technique, we were able to use 7zip to extract the raw flash file with the metadata still intact.

> $ flasm -d BrightBalls.swf > BrightBalls.out

The following metadata can be observed from the output:

> <dc:title>Encrypted by DoSWF</dc:title>  
>  <dc:description>Version:5.0.3\r\nUsername:nxianguo1985@163.com.fr\r\n  
>  Index:http://www.doswf.com\r\nAuthor:http://www.laaan.cn</dc:description>

This metadata indicates that the flash exploit was encrypted with **DoSWF** – a program designed to encrypt Flash files marketed and sold by Yushi High Technology Limited in Beijing, China. There is no reason to believe that this company was involved in the creation of this exploit. However, it appears that the username of nxianguo1985@163.com.fr is the email addressed used to register the particular licensed software installation that produced the malicious flash files. This email address might therefore provide a clue to the identity of an individual involved in the creation of the exploit. However, based on other instances where various clues or artifacts have purposefully been left behind, it is very well possible that this item is a red herring.

## Ties to Flash Exploits Found in Microsoft Word Documents

We have also observed CVE-2012-0779 being exploited via Microsoft Word documents. In these examples, Flash code is downloaded and executed from the web and used to carve a malicious binary out of the Word document. Inspection of the Flash files used in these attacks reveals the same metadata to those observed from the strategic web compromises. The example below is from a Microsoft Word document was used in a targeted attack:

> Filename: Upcoming Key Dates.doc  
>  File size: 183906  
>  MD5: 2A93EDCD8DA17511D8ADC6D4A93DB829  
>  SHA1: 6821a3ba27dbb561e819f5d84e3f87721967539e

This Word document contained JavaScript that downloaded a CVE-2012-0779 flash exploit from **www.support-office-microsoft.com**. The downloaded flash exploit had the following properties:

> File: essais.swf  
>  Size: 8005  
>  MD5: 509EE9B8E2BA13B878BFB3CBBA05283D  
>  SHA1: 786087bd6672e58a4920b4f3c642ee1a9d185e7c

While the flash exploit file used in this attack had different properties then the above file used in the drive-by attacks, it had the same metadata linking it to nxianguo1985@163.com.fr and was likely developed by the same author.

## Conclusion

In recent months we have continued to observe 0-day vulnerabilities emerging following discovery of their use in the wild to conduct cyber espionage attacks. Frequently by the time a patch is released for the vulnerabilities, the exploit has already been the wild for multiple weeks or months — giving the attackers a very large leg up. Individuals and organizations must keep their software patched and updated as frequently as possible. Many of these attackers are quite skilled at moving laterally within and organization and will take advantage of any entry point they have into a network. We recommend that you keep systems patched automatically if possible and are doing so for both the Operating System (OS) and Applications. Add-ons/plug-ins for browsers and e-mail clients should also be kept up-to-date. Additionally moving to one of the most recent operating systems on Mac, Windows, and Linux and consider installing the 64-bit platform, if possible, is recommended. Users and organizations should consider deploying Microsoft’s [Enhanced Mitigation Experience Toolkit (EMET)](https://support.microsoft.com/en-us/help/2458544/the-enhanced-mitigation-experience-toolkit).

Cyber Espionage attacks are not a fabricated issue and are not going away any time soon. These attackers are not spreading malware through strategically compromised websites to make friends. They are aiming to expand their access and steal data. Communications (primarily e-mail), research and development (R&D), intellectual property (IP), and business intelligence (contracts, negotiations, etc) are frequently targeted and stolen. Take the cyber espionage threat seriously and not as just something you read about occasionally. The problem is vastly understated. Considered boosting your defenses in any way possible and putting extra protection mechanisms around your most valued assets. While all of the above activity can be characterized as related to advanced threats or APT, it is important to note that there is not a single monolithic group responsible for all of these attacks. Although detailing each of these groups is beyond the scope of this post, we feel that the indicators provided here should give you the information required to detect these most recent threats and provide additional considerations for mitigating these threats.

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