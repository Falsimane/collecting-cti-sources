# APT Threat Landscape in APAC 2023: New Strategy, New Normal, New Techniques, and New Territory - TeamT5

- **Source :** teamt5
- **URL :** https://teamt5.org/en/posts/apt-threat-landscape-in-apac-2023/
- **Date :** 2024-01-09

---

Threat Intelligence

SubscribeRSS

# APT Threat Landscape in APAC 2023: New Strategy, New Normal, New Techniques, and New Territory

2024.01.09Cyber Threat Intelligence

Share: 

TeamT5 is a leading brand in delivering Asia Pacific intelligence. In this article, we summarize the threat landscape of advanced persistent threats (APT) in the Asia-Pacific region in 2023, not only provide annual observations, but also point out the cyber threats worth paying attention to in 2024.

> **This article is an excerpt version which summarizes key statistics. To obtain the complete threat intelligence report, you may fill up the form at the bottom to obtain the “APT Threat Landscape in APAC 2023” report.**
> 
> This article is adapted from "2023 H2 Campaign Tracking Report: APT Threat Landscape in Asia". To discover similar cyber threat intelligence which is focused in Asia-Pacific region, please sign up for the trial of our threat intelligence platform ThreatVision. Please indicate on the [ThreatVision page](https://teamt5.org/en/products/threatvision/?utm_source=blogs&utm_medium=website) that you would like to apply for trial.

## Preface

TeamT5’s cyber threat intelligence research based on well-built data collection and analysis flow. We collect data from multiple sources - malware databases, sandboxes, crawlers, and our threat forensic analysis platform ThreatSonar etc. With careful and rigorous analysis, we come up with intelligence reports for clients and the public to notify potential threats.

**For 2023, based on TeamT5 data collection and analysis, we found:**

  * 411 attack operations in 39 countries

  * 60 known adversary groups tracked

  * 210 malware / hacking tools used


  


![01_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/01_apt-threat-landscape-in-apac-2023.jpg)   


## Closer Look at Exploits

In 2023, we have observed at least 37 CVE exploits that were abused in the wild by threat actors. We see a tendency that more and more exploits targeting edge devices appear, which we marked with color yellow in the right table. These edge devices have no security products to monitor them so threat actors could effectively intrude their target network environments.

There are still lots of attacks achieved spear phishing emails but the corresponding tricks are old fashioned, such as:

  * Template Injection

  * Microsoft LNK

  * CHM

  * Macro documents

  * Phishing

  * CVE-2018-0798, CVE-2022-30190, CVE-2023-38831


  


![02_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/02_apt-threat-landscape-in-apac-2023.jpg)   


## Closer Look at Malwares

We listed the malware distribution in all attacks. Below is the ranking of **Top 10 Malwares in 2023 H1** and **Top 15 Malwares in 2023 H2**.

  


![03_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/03_apt-threat-landscape-in-apac-2023.jpg)   


We compare these two ranks with 4 aspects - Shared tools, Webshell, Cross platform RAT, Shared Quartermaster of Chinese APT. Here is our analysis.

**1\. About shared tools**

There are more and more threat actors adopting public or open source tools in their operations. This could effectively reduce their effort to develop their own weapons and also increase the barrier for researchers like us to achieve an effective attribution.

  


![04_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/04_apt-threat-landscape-in-apac-2023.jpg)   


**2\. About Webshell**

Web server exploitations have become more and more common nowadays and the importance of webshell keeps increasing. Godzilla, a full featured webshell made by Chinese threat actors, has become the favorite of Chinese APT. It is usually deployed jointly with a small webshell like China Chopper to effectively bypass detections.

  


![05_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/05_apt-threat-landscape-in-apac-2023.jpg)   


**3\. About Cross Platform RAT**

There are more and more cross platform or multi platform RAT. The reason behind is nowadays threat actors don’t only focus on Windows platform but will intrude from every possible platform like Linux, MacOS or even Android or iOS.

  


![06_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/06_apt-threat-landscape-in-apac-2023.jpg)   


**4\. Shared Quartermaster of Chinese APT**

We have observed an interesting code or feature sharing between different malware used by Chinese APT. This kind of finding makes us highly suspect there is an entity or even private company that is responsible for producing all these remote administration tools and distributing them secretly to various Chinese APT groups.

  


![07_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/07_apt-threat-landscape-in-apac-2023.jpg)   


## Closer Look at Targeted Countries / Regions by APT Groups

From countries / regions aspects, our data shows Taiwan, South Korea, and Japan are the most targeted countries by APT groups. Following them are countries in South or Southeast Asia, such as Vietnam, Philippine, Thailand, or Malaysia, etc.

  


![08_09_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/08_09_apt-threat-landscape-in-apac-2023.jpg)   


Based on this statistic, we will discuss 3 different victim areas and corresponding active threat actors, they are Taiwan, Northeast Asia, and South/Southeast Asia.

### No.1 Targeted Country / Region: Taiwan

Taiwan is the most targeted country in Asia Pacific. This chart shows the distribution of targeted industry sectors. Compared with our data in the past 2 years (2021-2022), we don’t see dramastic changes. Government, IT, education, or critical infrastructure are still on the top list.

People might wonder why APT actors are so interested in the IT sector. We believe the reason is that there are more and more supply chain attacks and these IT companies possess good channels or privileges to access big companies or government entities. It makes the IT sector a perfect hopping point.

And one interesting phenomena we have observed is the surging attack against the healthcare industry. We suspect the reason behind the attacks are the Taiwanese government’s effort to join WHA, or China’s ambition to collect personal identification information.

  


![10_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/10_apt-threat-landscape-in-apac-2023.jpg)   


In the threat actors' part, there are at least 21 known groups aiming at Taiwan in 2023. Among them are Huapi, Amoeba, and Polaris - they are old faces that are on the top list hitting Taiwan. In the meantime, there is a new face, SLIME13 (also known as FlaxTyphoon by Microsoft).

SLIME13’s operations became so wild in 2023 that we have observed more than 100 victim entities in Taiwan. This APT group also aggressively expands their attacks to other countries such as Hong Kong, Japan or South Korea, etc.

  


![11_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/11_apt-threat-landscape-in-apac-2023.jpg)   


### No.2 Targeted Country / Region: Northeast Asia

In the Northeast Asia region, the geopolitical situation has changed dramatically in the past 2 years because Japan and South Korea are united together with the U.S. to defend against their enemies in the neighborhood.

For this reason, the topmost targeted sectors include government, think tank, and education. These sectors often hold political documents or do sensitive research for their governments. Another interesting phenomena would be China’s attacks against South Korea which were stealthy and low profile in the past. But now China’s attacks turned to become high profile and public, threat actors such as 曉騎營 or 騰蛇 are some good example. Cryptocurrency sectors in this area are targeted and infiltrated by North Korean actors.

  


![12_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/12_apt-threat-landscape-in-apac-2023.jpg)   


For the threat actors part, China and North Korea actors dominate this area. North Korean actors are busy collecting geopolitical intelligence and another mission: earning money for their country. In contrast, Chinese APT operations become more stealthy and harder to detect; there are several big campaigns of Barracuda, Fortigate, Citrix or ArrayVPN vulnerabilities. Many of the events are still under investigation or even uncovered yet.

  


![13_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/13_apt-threat-landscape-in-apac-2023.jpg)   


### No.3 Targeted Country / Region: South Asia & Southeast Asia

The third target country / region is the South Asia and Southeast Asia region. Our observations show attacks in this area are driven by issues of the South China Sea, border issues or belt & road and shift of international organization’s factory. That was reflected in the most targeted sectors - military and critical infrastructure are all closely bundled with these issues.

In the southeast Asia region, threat actors from China such as Polaris, Amoeba, Gudiao and Vietnam originated groups such as SLIME43 or OceanLotus are very active in these regions. The interesting part regarding Vietnamese APT groups is that they are not only a big concern of neighboring countries but also the domestic people in Vietnam. Our engagement with Vietnamese customers shows their great fear of being intruded by OceanLotus.

  


![14_apt-threat-landscape-in-apac-2023.jpg\)](https://uploads.teamt5.org/upload/original/14_apt-threat-landscape-in-apac-2023.jpg)   


In the South Asia region, China is also busy attacking and monitoring their neighbors. People might consider Pakistan to be a good friend of China so they could be spared. In contrast, our data shows Pakistan to be highly targeted and infiltrated by China. Another interesting thing is that India and Pakistan both have their own cyber actors and they are fighting with each other a lot.

  


![15_apt-threat-landscape-in-apac-2023.jpg](https://uploads.teamt5.org/upload/original/15_apt-threat-landscape-in-apac-2023.jpg)   


## Conclusion

2023 is a busy year, both for threat actors and defenders. Also, more tensions in geopolitics will keep bringing more cyber attacks.

New technology might solve human’s problems, but not for attack and defense scenarios. New technology becomes a new opportunity for attackers as well (e.g. cloud services, AI). The reason is that targeted attacks are human-driven; defenders should address human problems by adopting threat intelligence.

No one can be spared in the war in the cyber world, so be prepared!

  
  


> **This article is an excerpt version which summarizes key statistics. To obtain the complete threat intelligence report, you may fill up the form at the bottom to obtain the “APT Threat Landscape in APAC 2023” report.**
> 
> This article is adapted from "2023 H2 Campaign Tracking Report: APT Threat Landscape in Asia". To discover similar cyber threat intelligence which is focused in Asia-Pacific region, please sign up for the trial of our threat intelligence platform ThreatVision. Please indicate on the [ThreatVision page](https://teamt5.org/en/products/threatvision/?utm_source=blogs&utm_medium=website) that you would like to apply for trial.

2024.01.09Cyber Threat Intelligence

Share: 

### Related Post

[ThreatVision Resources2023.08.27](/en/posts/why-threatvision/)

#### [Why ThreatVision - Threat Intelligence Platform Empowering Organizations to Make Informed Decisions](/en/posts/why-threatvision/)

cyber threat intelligence

![](https://teamt5.org/en/posts/apt-threat-landscape-in-apac-2023/)