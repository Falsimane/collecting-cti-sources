# Falcon Zero-Day Flash Detection

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/falcon-zero-day-flash-detection/
- **Date :** July 27, 2015

---

# Falcon Zero-Day Flash Detection

July 27, 2015

• [ jaronbradley](/en-us/blog/author.jaronbradley/ "Posts by jaronbradley") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

In the wake of the [Hacking Team leaks](http://www.securityweek.com/zero-day-exploits-leaked-hacking-team-breach) in early July, a result of an intrusion into the company’s network, various zero-day vulnerabilities that affect multiple platforms and software configurations were exposed to the public. Vulnerabilities provided to vendors through responsible disclosure mechanisms allow vendors to patch these vulnerabilities before they are exploited in the wild; however in cases such as the Hacking Team leaks, vendors have little chance to patch vulnerabilities before they are exploited by criminal gangs, hacktivists and state sponsored actors.

The Hacking Team example is particularly damaging, as the zero-day vulnerabilities included well documented proof of concepts that are quickly and easily integrated into an attacker's arsenal. When taking into consideration the large arsenal of zero-day vulnerabilities that are currently being sold or exploited by similar companies, we can see that this threat is even greater.

In the case of the leaks, Adobe Flash exploits for [CVE-2015-5119](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5119), [CVE-2015-5122](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5122) and [CVE-2015-5123](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-5123) were seen in the wild within days of the Hacking Team leak, well before Adobe was able to patch the vulnerabilities.

These exploits were linked to Chinese state-sponsored actors, as well as used in public exploit kits employed by criminal actors. Through CrowdStrike's focus on effect-based [Indicators of Attack (IoA)](https://www.crowdstrike.com/en-us/cybersecurity-101/threat-intelligence/indicators-of-attack-ioa/), as opposed to Indicators of Compromise (IoC) signatures, we are not reliant on engaging in the constant arms race that is required to detect and prevent the exploitation of new vulnerabilities and discover IoCs used by adversaries.

This blog provides an example of how Falcon in conjunction with the CrowdStrike Security Operations Center (Falcon Overwatch) was able to detect and disrupt exploitation of our customer base from zero-day Adobe Flash exploits exposed in the Hacking Team leaks. These detections occurred both before and after patches were released for these vulnerabilities in Adobe Flash. The data produced by the Falcon sensor is used extensively by Falcon Overwatch to discover adversary activity using an IoA detection approach. Soon after the Hacking Team leaks, Falcon Overwatch was alerted to an IoA designed to detect exploitation of the Flash plugin within a browser context. The team then observed use of the exploitation, and was able to defeat the attacker as they started to perform network reconnaissance.

Upon exploitation, CrowdStrike observed attackers delivering different malware payloads. Among these were PlugX, Emdivi and IsSpace, all of which are linked to Chinese targeted intrusion operators. In this case the payloads would be dropped in the form of a binary called rdws.exe. A handful of reconnaissance commands were then executed by rdws.exe. These commands were executed in a time frame that indicated that the attackers were hands on keyboard, rather than automated network reconnaissance. [![image01](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image01-1024x482.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image01.jpg) For further analysis we can look to our Endpoint Activity Monitoring (EAM) system. EAM provides an instant indexed search for all real-time and historical execution events monitored by Falcon.

Performing a search for the SHA256 hash for rdws.exe reveals a number of other interesting details in relation to its execution. After execution, rdws.exe was moved to the C:\ProgramData directory and renamed to wmiprivse.exe. Persistence was obtained through the common \Software\Microsoft\Windows\CurrentVersion\Run registry entry using the reg object name of adobeUpdate. [![image2](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image2-1024x80.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image2.jpg) [![image3](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image3-1024x60.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image3.jpg) With the prompt alert from CrowdStrike, the customer immediately acted to prevent any negative impact to the organization from attacker activity. Additional analysis revealed the Flash exploit used to carry out this attack was CVE-2015-5122. The other hosts that were exploited in a similar manner had a binary written to disk with the same filename, but different hash and behavior. Below is a process tree showing the execution of another rdws.exe sample detected at a different customer. [![image4](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image4-1024x466.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image4.jpg) A final instance shows attackers successfully exploiting Flash and once again being halted before the accomplishment of their objectives.[![image5](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image5-1024x314.jpg)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2015/07/image5.jpg)

**Hashes for malicious rdws.exe delivered via these flash exploits**

SHA256| MD5  
---|---  
a6fd2c5cc2ebc034f0cc2fa497f52f1c401a56056783de42840679d85d6d4c83| 5e223ef669acd309697c90cac2f9953f  
a94bf485cebeda8e4b74bbe2c0a0567903a13c36b9bf60fab484a9b55207fe0d| 07aa0340ec0bfbb2e59f1cc50382c055  
bfbf8c4ab1d1555dfa72dc17ebfb1579ec7cab1b21ebb83dd883071902a5fc41| 21c46a95329f3f16050a7421841a92c4  
  
**Malicious adobe.dat dropped by rdws.exe in several instances**

SHA256| MD5  
---|---  
d35f33d11b642ca0e41b1cf79fe97d9acb4fc3280926adea97f0e9084e20e489| b9af5f5fd434a65d7aa1b55f5441c90a  
  
Zero-days prove to be difficult and often impossible to detect using signature-based IOCs.

Maintaining a blacklist of known malicious domains hosting a Flash exploit may allow you to detect potentially infected hosts, but what happens when hosts are infected by a domain that is not known to be malicious? As we’ve demonstrated in this example, the capability to use IOAs to monitor a browser for suspicious Flash behavior allows you to mitigate both zero-day and known Flash exploits. In conclusion, an IOA-based approach that looks at the effects of the execution activity independent of the vulnerability or exploit used is highly effective.

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)