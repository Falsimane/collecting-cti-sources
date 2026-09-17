# Malicious Spear-Phishing Campaign Targets Upcoming Winter Olympics in South Korea

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/malicious-spear-phishing-campaign-targets-upcoming-winter-olympics-in-south-korea/
- **Date :** January 10, 2018

---

# Malicious Spear-Phishing Campaign Targets Upcoming Winter Olympics in South Korea

January 10, 2018

• [ Falcon Intelligence Team](/en-us/blog/author.falcon-intelligence-team/ "Posts by Falcon Intelligence Team") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


A malicious campaign has been identified targeting suspected victims involved in or supporting the February 2018 Olympic Winter Games in Pyeongchang, South Korea. [Open source reporting](https://securingtomorrow.mcafee.com/mcafee-labs/malicious-document-targets-pyeongchang-olympics.html) indicates this campaign used several sophisticated techniques, such as an in-memory implant using PowerShell scripts, along with a newly released steganography tool to increase obfuscation. 

### **Technical Analysis**

The observed malicious [spear-phishing](/en-us/cybersecurity-101/social-engineering/phishing-attack/) message spoofs a sender address belonging to South Korea’s National Counter-Terrorism Center (대테러센터), info<@>nctc.go.kr, but it is sent from an IP address associated with cloud-hosted infrastructure in Singapore—43.249.39<.>152\. The message contains a Microsoft Word attachment (SHA256 hash: 41ce9e7c8ec4a5f399247d26087a37ad13b4fc8fc9ee62a1d2211b743b2f403a) titled 농식품부, 평창 동계올림픽 대비 축산악취 방지대책 관련기관 회의 개최.doc, which translates as “organized by Ministry of Agriculture and Forestry and Pyeongchang Winter Olympics.” Upon execution, it prompts the victim to enable content allowing the document to be opened in the user’s version of Word. Once opened, the document contains an obfuscated Visual Basic macro that launches a PowerShell script to download and read an image file from the **URL: https://www.thlsystems.forfirst <.>cz/images/adv_s3.png**, which is likely hosted on a compromised legitimate website. The image file has been created using the open-source steganography tool [_Invoke-PSImage_](https://github.com/peewpw/Invoke-PSImage) to embed a malicious PowerShell loader. The extracted PowerShell script is heavily obfuscated using several string format techniques. The script beacons to the **URL: https://www.thlsystems.forfirst <.>cz:443/components/com_tags/views/login/process.php**, to receive encrypted scripts that are decrypted using RC4 with a key constructed from the first four bytes of data concatenated with the string 09adcc4403832a5c22cfb6621c2942da. Decrypted scripts are evaluated directly. In addition to receiving scripts, the implant attempts to download payloads from **URLs:

http://200.122.181<.>63/os** and **https://www.thlsystems.forfirst <.>cz/components/com_tags/views/access_log**. Scheduled tasks are then created for these downloaded payloads with the names WindowsMediaServiceCore and WindowsMediaServiceCoreInit, respectively, and are set to run each day. A second document (SHA256 hash: d88ea493cdd719ff2e2c02cea66dd15d358f914ea8741d6d6d3dd60b66adf923) was identified that also contains an instance of the obfuscated PowerShell payload. Instead of using macros to pull the payload, the DOCX file utilizes OLE streams and relies on the victim double-clicking the embedded object. Once clicked, the payload will write out the file Error 733 .hta and execute it. The PowerShell payload is included in this .hta file. Interestingly, this document appears to be associated with warnings over the H5N6 bird flu that prompted South Korea in late 2017 to raise the bird flu alert level to its highest ranking. South Korea has struggled with bird flu outbreaks over the last year — particularly in Gangwon Province (강원도) where Pyeongchang is located — and the threat remains a viable concern in the lead up to the Olympic games. 

### **Target Scope**

Analysis of the spear-phishing message revealed that 320 users within 36 organizations were recipients of this malicious campaign. The vast majority of these targets are located in South Korea and will likely provide venue, lodging, transportation and/or infrastructure support for the event. The victims span the following verticals: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2018/01/chart-4.png) While the majority of targets are located in South Korea, the CrowdStrike®Falcon

Overwatch™ team identified recent activity with similar characteristics at a customer operating in the global technology sector. Therefore, this campaign is possibly broader than the observed spear-phishing effort. The adversary association is unclear, however, given the current heightened tensions on the Korean Peninsula and the high value of targets present at the event, Falcon Intelligence™ assesses that the 2018 Pyeongchang Olympics will likely be the context for numerous targeted intrusion efforts, most notably by the Democratic People’s Republic of Korea (DPRK) and Russia. Adversaries with a nexus to the DPRK are potential threat actors for this target scope and may be interested in information pertaining to this event as they decide whether or not to participate. Russia-based adversaries may be interested in targeting entities involved in this event because of the recent ruling by the International Olympic Committee stating that Russian athletes may not compete under the Russian flag in the 2018 Winter Olympics.While the majority of targets are located in South Korea, the CrowdStrike Falcon® Overwatch™ team identified recent activity with similar characteristics at a customer operating in the global technology sector. Therefore, this campaign is possibly broader than the observed spear-phishing effort. 

### CrowdStrike

Falcon Intelligence

CrowdStrike

Falcon Intelligence will continue to monitor and report on cyber threats associated with the 2018 Winter Olympics, which start on February

9, 2018. For more information on this subscription-only service, please visit [ https://falcon.crowdstrike.com/intelligence/reports/subscriptions](https://falcon.crowdstrike.com/intelligence/reports/subscriptions). Learn more about [CrowdStrike Falcon® Intelligence](/en-us/products/falcon-intelligence/).

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)