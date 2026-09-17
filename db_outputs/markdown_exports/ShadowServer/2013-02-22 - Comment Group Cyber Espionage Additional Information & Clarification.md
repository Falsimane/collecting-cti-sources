# Comment Group Cyber Espionage: Additional Information & Clarification

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/comment-group-cyber-espionage-additional-information-clarification/
- **Date :** 2013-02-22

---

# Comment Group Cyber Espionage: Additional Information & Clarification

February 22, 2013

## The Comment Group – Long Term Cyber Espionage

_By Steven Adair_

A cyber espionage threat group, frequently known as the **Comment Group** , has recently received a good bit of extra attention in the last few days. On Monday (February 18, 2013) Mandiant [released a report](http://intelreport.mandiant.com/) detailing a substantial amount of information on the group. In particular it listed a large number of domain names, IP addresses (both command & control and administrative ranges), a very large list of their trojan families (with MD5 hashes to boot), a bit of attribution aimed at outing the group as part of a particular unit within China’s People Liberation Army (PLA), and some of the group’s general tactics techniques and procedures (TTPs). There is a staggering amount of information for people to sift through and as a result there have been many questions raised and confusion around some of the data. In this post I am hoping to add some clarity to the information and clear up some confusion that might help defenders, incident responders, and researchers make more effective use of this data.

As someone who has been looking at, researching, and often combating the Comment Group out of networks for the past 6+ years as either part of my day job, work at Shadowserver, or in my spare time, it is a bit fun to see the spotlight shine on these guys a little bit. It is quite accurate to say that they are one of the largest and certainly the most prolific cyber espionage groups targeting networks worldwide. Like all organizations they are a mix of good and bad. There has been some of the worst and funniest stuff we have ever seen attributed to these guys, and we have also seen some all stars who are absolute wizards on the command prompt. One thing is for certain, the Comment Group has been quite successful at breaching hundreds (likely thousands) of organizations in the past few years. In most cases their method for breaching organizations is fairly “low-tech”, however, it works quite well and easily beats millions upon millions of dollars of layered security measures employed at many organizations ranging from mom & pop shops to the largest companies and government organizations in the world.

### Command & Control: Domains, Dynamic DNS, and Compromised Websites

#### Domains: Threat Actor vs Security Researcher vs Domain Parking

The Comment Group, like most notable threat groups, employs a variety of techniques when it comes to spear phishing and victim command and control. Of note was the recently released list of 107 domain names that are or **were** at one point controlled by the Comment Group. It should be noted that this list is not (and likely was not meant to be) comprehensive and a substantial number of domains in the list have been taken over or re-registered post domain expiration. The idea that these domains may no longer be in control of the Comment Group’s control is referenced in the APT1 report. We feel that due to the significant number of hostnames that are no longer in the Comment Group’s control, this point is worth re-addressing here. Interaction with these domains may still represent an infected device, although the end server would likely not be part of the Comment Group’s infrastructure. In order to help clarify portions of this, a partial list of the hostnames that have expired, been re-registered, or have been taken over are listed below. It should also be noted that for these domain lists, they were controlled by the Comment Group. This means that you should focus your efforts on the domain itself and worry less about the subdomain. For example, if you see activity to any subdomain on purpledaily.com, this should trigger alarms of concern. Do not focus on a specific list of subdomains, which may not be comprehensive. It is also worth noting that many of the subdomains on the list have not been used or have not been in the zonefile related to a particular domain for several years in some cases.

In particular, we took note last week that 26 Comment Group domains registered with GoDaddy appear to have been taken over on February 13, 2013 (and in some cases late January). Each one of these domain names had their name servers modified and then began to resolve to different IP addresses spread out over different IP addresses at Linode. This does not appear to have been a move by the Comment Group and is likely related to security research and/or potentially this past Monday’s report release. The follow is a list of the updated name servers, domain names that were modified, and the IP addresses to which they resolve(d).

New name servers:

  * **NS1.BUILDATOP.COM – 198.74.51.202**
  * **NS2.BUILDATOP.COM – 178.79.171.141**



Domain Names:

  * **aoldaily.com**
  * **aunewsonline.com**
  * **canadatvsite.com**
  * **canoedaily.com**
  * **cnndaily.com**
  * **cnndaily.net**
  * **defenceonline.net**
  * **downloadsite.me**
  * **e-cardsshop.com**
  * **hvmetal.com**
  * **jobsadvanced.com**
  * **mcafeepaying.com**
  * **micyuisyahooapis.com**
  * **nationtour.net**
  * **newsonlinesite.com**
  * **onefastgame.net**
  * **pop-musicsite.com**
  * **satellitebbs.com**
  * **symanteconline.net**
  * **syscation.com**
  * **tibethome.org**
  * **todayusa.org**
  * **usabbs.org**
  * **usnewssite.com**
  * **usnftc.org**
  * **voiceofman.com**
  * **yahoodaily.com**



Also on these same name servers, but newly registered (not taken over) are the following:

  * **copporationnews.com**
  * **maltempata.com**
  * **usnftc.org**



Related IP addresses (not necessarily hostile destinations but traffic to them should be considered suspect):

  * **106.186.16.96**
  * **106.186.19.222**
  * **106.186.19.25**
  * **106.186.21.158**
  * **106.186.21.187**
  * **106.187.45.184**
  * **151.236.220.199**
  * **173.255.201.81**
  * **173.255.228.165**
  * **176.58.110.112**
  * **178.79.171.6**
  * **178.79.179.226**
  * **192.155.90.150**
  * **192.155.92.64**
  * **192.155.93.57**
  * **192.81.129.132**
  * **198.58.104.183**
  * **198.58.96.236**
  * **50.116.18.118**
  * **50.116.42.33**
  * **66.175.210.225**
  * **66.228.48.134**
  * **66.228.53.110**
  * **66.228.54.200**
  * **96.126.108.231**



Additional comment group domains that have expired/been re-registered (e.g. not Comment Group controlled):

  * **bigdepression.net**
  * **blackberrycluter.com**
  * **blackcake.net**
  * **chileexe77.com**
  * **cnnnewsdaily.com**
  * **conferencesinfo.com**
  * **dnsweb.org**
  * **earthsolution.org**
  * **globalowa.com**
  * **hkcastte.com**
  * **infosupports.com**
  * **issnbgkit.net**
  * **lksoftvc.net**
  * **mediaxsds.net**
  * **msnhome.org**
  * **nirvanaol.com**
  * **olmusic100.com**
  * **pcclubddk.net**
  * **progammerli.com**
  * **regicsgf.net**
  * **safalife.com**
  * **searchforca.com**
  * **softsolutionbox.net**
  * **sportreadok.net**
  * **tfxdccssl.net**
  * **worthhummer.net**



As you can see this list already cover about 50% of the domains in the released list. Just keep this in mind before you treat some of the IP addresses involved as hostile actors. Another thing to note is that your organization could have easily been victimized and never seen traffic to any of these domains. At any given point in time there are often no more than a handful of victims that will be pointed at a particular fully qualified domain name (FQDN). These FQDNs are transient and typically only used for a short period of time. The rest of command and control activity is often either done using other domains, dynamic DNS, or legitimate compromised websites (continue reading).

#### Dynamic DNS: Non-hostile Domains but Dangerous Subdomains

Many threat groups use dynamic DNS services in order to control their victims. There is always a trade off for a threat actor when it comes to using their own domains, free dynamic DNS services, or skipping DNS altogether and going direct to IP addresses. There are advantages and disadvantages to each one, and many threat groups leverage a mix of each. The Comment Group is no different. In fact, a sizable amount of their infrastructure and malware utilize free dynamic DNS services. In particular the Comment Group makes heavy use of ChangeIP.com and Afraid.org. They have and continue to use other providers too (CN99: 3322.org, 6600.org, 8800.org, etc, No-IP, DynDNS, and others). Keeping a close eye on dynamic DNS service activity in your network would be prudent.

Just a quick handful of examples of Comment Group dynamic DNS usage (some fairly old) that you can see in public malware reports for are listed below:  
**back.sux.ms** – http://www.threatexpert.com/report.aspx?md5=920ff39210be3565a25842c32b9446f6  
**effection.ddns.us** – http://www.threatexpert.com/report.aspx?md5=b29556856203049b9e7b05e01f5ae73f  
**conference.ddns.us** – http://urlquery.net/report.php?id=255027  
**finance.acmetoy.com** – https://www.virustotal.com/en/file/e9ab61c6c9673698defece13789ee02d8b8806ca77ee14c4ef182e4260b6574e/analysis/

Sample of other related dynamic DNS host name:

**activation.ddns.us**  
**armyconference.acmetoy.com**  
**cnndaily.acmetoy.com**  
**documents.ddns.info**  
**documents.longmusic.com**  
**documents.myftp.info**  
**download.onmypc.net**  
**effection.acmetoy.com**  
**updating.ddns.info**

#### Legitimate Compromised Websites

A favored technique of the Comment Group is the use of legitimate compromised websites to host spear phishing files (usually ZIPs with an EXE or CHM file in them) or stage one command and control. In case it wasn’t clear, the Comment Group gets their name from a substantial amount of their malware receiving its commands from parsing HTML files (sometimes ASP and other file extensions as well) with embedded HTML comment tags in them “**<!–**” and “**– >**“. The commands are presented in a variety of ways ranging from cleartext, to simple base64, on up to using multiple encoding formats that involve real encryption. A substantial portion of this activity and victim management occurs over legitimate websites that have been compromised. These are often referred to in the Comment Group malware directly by IP address or by actual legitimate domain names hosted on the compromised web server. In the last few years we have encountered hundreds of compromised websites used for Comment Group command and control. Many of them are often short-lived, but others have remained in use for quite some time as well. The best way to detect this activity is to look for network traffic that contains many of the referenced patterns. Additional, various header items from HTTP GET and POST requests and particularly a variety of invalid User-Agents can be used for detection.

### IP Address Ranges

One thing also worth addressing that appears to be causing some confusion are some of the IP ranges that are often used by the Comment Group for administrative functionality. There are few things to note on these ranges. The first is that most of these ranges in China (not including Hong Kong) are dynamic and short-lived. An IP address in these ranges will not likely belong to a particular person for longer than a few days. This means if a particular IP address was used for RDP, FTP, in an htran connection, or anywhere else that it will not likely be a good indicator beyond a few hours to days following observation of active use. It should also be noted that there are plenty of normal non-APT actors in these same IP address ranges that are infected with Conficker and other malware that scans the Internet just like everyone else. In particular for some of the more prolific ranges, if you see connections from them, please take it with a grain of salt:

  * **223.166.0.0 – 223.167.255.255**
  * **58.246.0.0 – 58.247.255.255**
  * **112.64.0.0 – 112.65.255.255.**
  * **139.226.0.0 – 139.227.255.255**



In particular it is worth noting that the Comment Group has not been observed using 58.246.0.0 – 58.247.255.255 for several months now. The threat actors that were observed using this IP address space were updated to us 223.166.0.0 – 223.167.255.255. That range should be considered legacy at this point.

### Devastating Impact?

Will the outing of so much of the Comment Group’s infrastructure have a devastating impact on their operation? Time will tell the answer, but in the short term I would answer with a resounding, **no**. That’s not to say the Comment Group has not made changes. A number of changes have already been observed. Several domains and dynamic DNS hostnames are now pointing to loopback or parking addresses. A few of the domain names have received, what appears to be threat actor controlled, WHOIS information updates. In particular the domain name **hugesoft.org** has had its registrant information changed. The new e-mail address for this domain is now **anonymous@anonymous.com**. Something tells me they don’t have control of that mailbox, but then again it wouldn’t surprise me if they did.

Most notably is that from other global vantage points we can see it is _business as usual_ with the Comment Group. They are continuing operations and even continue to work from IP address ranges that were outed in the APT1 report. This includes IP ranges listed in the previous section. We have also learned that ISPs have begun contacting some of the owners of IP blocks that Comment Group command and control has been occurring from telling them that they have put 72-hour blocks to the address in place. It remains to be seen how effective those steps may be, especially when some of the information they are working from is a bit outdated. I’d expect that more and more of their infrastructure will be outed by security researchers, AV companies, and other players in the coming weeks. We will just have to kick back and see what happens. It will be interesting to see what else the Comment Group might change in the next few months, but I am not expecting them to shut down and close up shop any time soon.

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