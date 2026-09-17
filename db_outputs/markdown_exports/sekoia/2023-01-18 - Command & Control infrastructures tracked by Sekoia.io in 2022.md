# Command & Control infrastructures tracked by Sekoia.io in 2022

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/command-control-infrastructures-tracked-by-sekoia-io-in-2022
- **Date :** 2023-01-18

---

## Introduction

Throughout 2022, Sekoia.io's Threat & Detection Research (TDR) team continued to proactively track and monitor the Command & Control (C2) infrastructures set up and used by cybercriminal or state sponsored intrusion sets to carry out malicious cyber activities. Our analysts identified more than 65,000 IP addresses used as C2 servers in 2022, an increase of almost 50% compared to 2021. These IP addresses were found through more than 1,200 searches of internet scan results for more than 180 threats.

These infrastructures host server side code linked to malware and multiple open source and/or commercial post-exploitation tools favoured by cyberattackers.

Sekoia.io CTI makes it possible to anticipate and track the campaign related to the most active threats to detect and block unauthorised actions.

Command & Control servers detected by Sekoia.io are continuously added to our Intelligence Center platform and are available to all our customers. The validity dates of our vetted IOCs are critical, therefore the validity period by default of IP addresses in our platform is very short and is renewed if the server is still active.

In this year's report, we compare results with past year’s and explain newly observed trends.

## Evolution since 2021 TOP 10

![Number of detected IP addresses between 2020/2021 Top 10 and 2022 data. Source: Sekoia.io C2 Trackers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a625348f7b8ed0f56d4b_6a92a3be692919148899df93_6a2a7b898b996da41be9c11b.webp)

Number of detected IP addresses between 2020/2021 Top 10 and 2022 data. Source: Sekoia.io C2 Trackers

The TOP10 threats monitored last year were still very active in 2022. **We can notice a significant bump for Gophish and BeEF servers**.

As mentioned in our 2021 report, **Gophish is used by both red teams and multiple intrusion sets**. It is presented by its main author, Jordan Wright, as a tool to conduct phishing test campaigns for companies and hackers. The increase for Gophish is almost certainly due to our increased visibility since implementing new research methods at the end of 2021. **We currently possess a great coverage of Gophish servers**.

BeEF stands for Browser Exploitation Framework, it is a penetration testing tool that focuses on the web browser. We assess with high confidence that the release of the BeEF tool on the Linode marketplace and its advertisement on social media is the main reason for this significant increase.

**The upward trend for Qakbot reflects that the malware was very popular this year among cybercriminals**. Qakbot is a well-documented and actively developed banking trojan used since 2008. Qakbot is known for collecting browsing data as well as banking credentials and other financial information from victims. The malware is popular among threat actors, particularly among Initial Access Brokers (IABs).

![Intrusion Sets using Qakbot \(source: Command and control infrastructures tracked by Sekoia.io in 2022\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a625348f7b8ed0f56d43_6a92a3bc6017750314a4fe54_6a2a7b898b996da41be9c0f7.webp)

Intrusion Sets using Qakbot (source: Command and control infrastructures tracked by Sekoia.io in 2022)

Intrusion Sets using Qakbot (source: Sekoia.io) 

As new threats are now monitored by Sekoia.io it is important to present our 2022 TOP 10:

## 2022 TOP 10

This year, Sekoia.io splits the TOP 10 monitored C2 servers in two distinct figures to illustrate the large use of Offensive Security Tools (OST), including C2 frameworks.

### TOP 10 USED OST

Contrary to past years, we decided not to include servers detected as MalleableC2 in the CobaltStrike count. Indeed, many OSTs now include the functionality to use MalleableC2 profiles in their frameworks. Only 3,492 IP addresses are flagged as just MalleableC2, meaning that more than half of the detected MalleableC2 IPs also exposed characteristics associated with CobaltStrike in 2022.

![2022 used OST Top 10. Source: Sekoia.io C2 Trackers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a625348f7b8ed0f56d48_6a92a3c04b4041c69342db12_6a2a7b898b996da41be9c121.webp)

2022 used OST Top 10. Source: Sekoia.io C2 Trackers

**CobaltStrike is still the most detected threat this year** , although we can notice a slight decrease in the number of servers detected compared to last year. This likely stems from the observed **larger use of tools such as MalleableC2 or some popular C2 frameworks**. This year, Sekoia.io tracked several projects with similar functionalities such as: **Empire, Sliver, BruteRatel, Mythic, Covenant**. As CobaltStrike is under considerable scrutiny by cybersecurity vendors, it is likely that using other tools allow cybercriminals to evade detection.

Our **detection of Sliver significantly improved** over the past year and it is now our **12th most detected threat**. The number of IP detected addresses improved by 400% since last year. This does not come as a surprise to our analysts as this framework is now well known to operators such as APT29 or ransomware operators. The tool is under careful scrutiny from Sekoia.io analysts since our FLINT 2021-090 report of November 2021.

![Known campaigns and infrastructure using Sliver \(source: Command and control infrastructures tracked by Sekoia.io in 2022\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a625348f7b8ed0f56d54_6a92a3bae17eff730b65ab5f_6a2a7b898b996da41be9c0f1.webp)

Known campaigns and infrastructure using Sliver (source: Command and control infrastructures tracked by Sekoia.io in 2022)

### TOP 10 detected malicious code

![TOP 10 detected Malicious code. Source: Sekoia.io C2 Trackers](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a625348f7b8ed0f56d4e_6a92a3bd2b0ef7af46bd35fc_6a2a7b898b996da41be9c118.webp)

TOP 10 detected Malicious code. Source: Sekoia.io C2 Trackers

For this TOP 10, we have new entries for the first two positions: **EvilProxy with more than 3,500 IP addresses** over a 6 month period, and **Ramnit with more than 1,900 IP addresses** over a one month period.

The remaining threats in this TOP 10 illustrate the main threat of the year: ShadowPad and PlugX aside, others are malware used by cybercrime actors. For example Raccoon, whose new version was analysed by Sekoia.io in its [Raccoon Stealer v2 – Part 1: The return of the dead](/blog/raccoon-stealer-v2-part-1-the-return-of-the-dead) blogpost.

#### EvilProxy

EvilProxy was studied by Sekoia.io analysts in FLINT 2022-049 report.  
EvilProxy tool is advertised as a security awareness [Phishing-as-a-Service](/blog/new-widespread-eviltokens-kit-device-code-phishing-as-a-service-part-1) (PhaaS) program since August 2020. It is possible that the tool went through further development since then. While EvilProxy is presented as a security awareness tool, **Sekoia.io assesses it is currently exclusively leveraged by cybercriminals** , likely in an attempt to evade Law Enforcement Agencies scrutiny. However, it remains plausible that EvilProxy could be used for legitimate security training purposes.

In the FLINT 2022-049, we identify campaigns using EvilProxy:

  * Campaign described by Zscaler in August 2022 targeting Microsoft email account;
  * Roasting 0ktapus campaign described by Group-IB aiming at compromising Okta accounts.



#### Ramnit

We assess that IP addresses responding html with the VBScript inclusion detailed in this [tweet](https://twitter.com/r3dbu7z/status/1561284336812433410) are malicious and linked to the Ramnit malware. Ramnit is originally a banking trojan which surfaced in 2010. Over time, the original Ramnit malware was modified so that newer variants include the ability to serve as a backdoor and to communicate with a command and control (C&C) server.

In one month, we detected more than 1,900 IP addresses with this inclusion, more than 95% are located in Asia with 90% in China. Sekoia.io analysts assess this threat mainly targets Asian users.

## Hosting statistics

Geographical distribution of IP addresses detected as malicious by Sekoia.io:

![2022 IP Addresses’ geolocation. Source: Command and control infrastructures tracked by SEKOIA.IO in 2022](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a625348f7b8ed0f56d51_6a92a3bb3e6167cebbf69ace_6a2a7b898b996da41be9c0f4.webp)

2022 IP Addresses’ geolocation. Source: Command and control infrastructures tracked by SEKOIA.IO in 2022

More than **50% of the malicious servers identified are geolocated in China or in the United States**. It doesn’t come as a surprise, given that many hosters and data centers are located in these countries. **France comes at the 10th position with more than 1,400 servers**.

Most used hosting providers are: **Akamai, Tencent, Digital Ocean, Amazon, Alibaba, Constant, Microsoft and OVH**. This list is very close to the one of the last two years of study. Only Akamai is new in this list and most of the malicious threats detected are BeEF framework, as Akamai acquired Linode in 2022.

## Have fun with C2

### Long standing malicious IP addresses

Out of the 65,000 seen through the year, 535 were deemed malicious over the entire year, with the following distribution:

![2022 year-long active threats repartitions. Source: Command and control infrastructures tracked by SEKOIA.IO in 2022](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a625348f7b8ed0f56d57_6a92a3bfcd1cab63350cd9b3_6a2a7b898b996da41be9c11e.webp)

2022 year-long active threats repartitions. Source: Command and control infrastructures tracked by SEKOIA.IO in 2022

### Lord of badness

While studying our data, we came across two servers that hosted at least 6 malicious tools over the year:

`185.158.94[.]217`| CobaltStrike  
Empire  
MalleableC2  
meterpreter  
Mythic  
Sliver  
---|---  
`5.101.4[.]196  
5.101.5[.]196`| DeimosC2  
BeEF  
metasploit  
meterpreter  
PoshC2  
Sliver  
  
One of the servers seems to host two IP addresses: `5.101.4[.]196` / `5.101.5[.]196`.

As the observed configurations are the default ones, those servers highly likely belong to researchers or red teamers. The operators here don't seek stealthiness.

### Evilginx2 tracked with differents methods

The results presented above stem from public internet scanners, and **other in-house tools behind the Sekoia.io C2 Trackers source allow us to expand and enrich our results**.

To stay on phishing tools such as Gopish and EvilProxy, it is important to mention our work on Evilginx2 servers. Evilginx2 is a man-in-the-middle attack framework used for phishing login credentials along with session cookies, which in turn allows MFA bypass. This tool is a successor to Evilginx, released in 2017, which used a custom version of nginx HTTP server to provide man-in-the-middle functionality to act as a proxy between a browser and phished website. Present version is fully written in Go as a standalone application, which implements its own HTTP and DNS server, making it extremely easy to set up and use.

Contrary to the other tracked tools, Evilginx2 servers are harder to detect due to the implemented mechanism. Nevertheless, Sekoia.io analysts were able to **identify more than 2,700 related domains over the year**.

### CALISTO usage of Evilginx2

CALISTO (aka Callisto, COLDRIVER) is suspected to be a **Russian-nexus intrusion set** active since at least April 2017. Although it was not publicly attributed to any Russian intelligence service, past CALISTO operations showed **objectives and victimology that align closely with Russian strategic interests**.

CALISTO mainly focuses on Western countries, especially the United States, and Eastern European countries. The group was observed carrying out [**phishing campaigns**](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers)**aiming at credential theft** , targeting military and strategic research sectors such as NATO entities and a Ukraine-based defense contractor, as well as NGOs and think tanks. Additional victimology includes former intelligence officials, experts in Russian matters, and Russian citizens abroad.

**Some of the Evilginx2 domains were part of recent infrastructure of CALISTO as described in our blogpost published in June** : CALISTO continues its credential harvesting campaign.

## General trends

Our tracking methods established at the end of 2019 are still working and provide Sekoia.io platform exclusive Indicators of Compromise (IoCs) as soon as attackers' servers are scanned.

Sekoia.io analysts regularly study newly published frameworks to write Sekoia.io C2 Tracker heuristics. Offensive Security Tools are always a plebiscite by threat actors and this trend should not change in the near future.

Sekoia.io analysts will continue to study malicious infrastructure to improve our proactive approach and give the best protection to our clients. We will continue sharing with the community, including through VirusTotal comments.