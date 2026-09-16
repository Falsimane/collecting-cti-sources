# The Top 5 Russian Cyber Threat Actors to Watch | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/03/03/the-top-5-russian-cyber-threat-actors-to-watch/
- **Date :** 2025-06-02

---

_This post was updated on March 10, 2022 to include a section on the Conti Ransomware Group._

As we continue to monitor the situation between Russia and Ukraine – and the potential for global cybersecurity impacts – we realize that our customers and other business and industry stakeholders may be interested in additional information and context to help them understand the landscape. An important part of the equation we are studying is the activity of cyber threat actors.

In an effort to help our clients know what to look for in their environments and anticipate potential attacks, this post provides guidance on the top 5 Russian threat actors and their known tactics and techniques, based on information from the Threat Library within [Threat Command](/products/threat-command/). 

The following threat actors are identified by our Threat Intelligence Research team as the most likely (i.e., highest risk) to carry out cyberattacks against European and US companies.

## 1\. The UAC-0056 threat group (AKA TA471, SaintBear, and Lorec53)

The UAC-0056 threat group has been active since at least March 2021. The group was observed attacking government and critical infrastructure organizations in Georgia and Ukraine. UAC-0056’s targets are aligned with the interests of the Russian government, although it is unknown whether it is state-sponsored.

The threat actors gain initial access via the sending of spear phishing email messages that contain either Word documents (with malicious macro or JavaScript codes) or PDF files (with links leading to the download of ZIP archives embedded with malicious LNK files). These are used to install and execute first-stage malware loaders that fetch other malicious payloads, such as the OutSteel document stealer and the SaintBot loader. The latter is used to download even more payloads by injecting them into spawned processes or loading them into memory.

UAC-0056 hosts its malicious payloads on Discord’s content delivery network (CDN). They are often obfuscated and have anti-analysis mechanisms.

In February 2022, amidst the geopolitical tension between Russia and Ukraine, the Computer Emergency Response Team of Ukraine (CERT-UA) [attributed](https://thecyberwire.com/newsletters/research-briefing/4/9) UAC-0056 with an attack against a Ukrainian energy organization. The threat actors used spear phishing email messages, allegedly on behalf of the National Police of Ukraine, suggesting that a certain individual (Belous Alexei Sergeevich) had committed a crime. This attack was associated with a larger campaign that was initiated by the group against Ukrainian entities from the beginning of 2021

UAC-0056 is actively targeting Ukraine. Their previous cyberattacks demonstrated the use of a spoofing phishing technique to reach their targets. This technique could be used to target various companies in Europe or the United States.

**Targeted industries/sectors**

  * Government
  * Energy



## 2\. Sandworm Team 

Sandworm Team, also called Black Energy, BlackEnergy , ELECTRUM, Iron Viking, Quedagh

Sandworm, TeleBots, TEMP.Noble, or VOODOO BEAR, is a group of Russian hackers that have been behind the major cyber campaign targeting foreign-government leaders and institutions, especially Ukrainian ones, since 2009. They may also have been involved in the cyberattacks launched against Georgia during the 2008 Russo-Georgian confrontation.

Sandworm Team is known to have a strong interest in US and European critical systems. In one campaign, Sandworm Team [used a zero-day exploit](https://thehackernews.com/2014/10/microsoft-windows-zero-day_13.html), CVE-2014-4114. In that campaign, they targeted Ukrainian government officials, members of the EU, and NATO.

Sandworm Team's previous activity in Europe and the United States exposed their interest in targeting critical systems and indicated preparation for cyber attacks. 

In February 2022, the United States’ and United Kingdom's cybersecurity and law enforcement agencies [uncovered a novel botnet](https://www.wired.com/story/sandworm-cyclops-blink-hacking-tool/) that has been used by Sandworm since June 2019. The malware, dubbed Cyclops Blink, targets WatchGuard Firebox and other Small Office/Home Office (SOHO) network devices, and grants the threat actors remote access to networks. Cyclops Blink leverages the legitimate firmware update process and maintains system access and persistence by injecting malicious code and installing repacked firmware images. In addition, the malware is deployed along with modules that are developed to download and execute additional files from a remote command and control (C2) server, collect and send general system information, and update the malware. Cyclops Blink is estimated to affect approximately 1% of all active Watchguard firewall appliances in the world.

**Targeted industries/sectors**

  * Government
  * Critical systems (energy, transportation, healthcare)  




## 3\. Gamaredon Group

Active since at least 2013, Gamaredon Group is a Russian state-sponsored APT group. In 2016, the Gamaredon Group was responsible for a cyber espionage campaign, tracked as [Operation Armageddon](https://natoassociation.ca/phishing-on-the-dnieper-russian-offensive-cyber-operations-in-ukraine/) (an operation that has been active since at least mid-2013), targeting the Ukrainian government, military, and law enforcement officials. The Security Service of Ukraine (SSU) [blamed Russia’s](https://therecord.media/ukraine-discloses-identity-of-gamaredon-members-links-it-to-russias-fsb/) Federal Security Service (FSB) for the cyberattacks. Furthermore, [evidence](https://www.securityweek.com/gamaredon-group-uses-custom-malware-ukraine-attacks) found by researchers suggested that the malware used by the threat actor had been built on a Russian operating system. The Gamaredon group leveraged spear-phishing emails to deliver common remote access tools (RATs), such as UltraVNC and Remote Manipulator System (RMS).

Gamaredon Group is known to use strikingly off-the-shelf tools in their hacking activities. At the beginning of 2017, the Gamaredon Group made a shift to custom-developed malware instead of common RATs, showing that the group has improved its technical capabilities.

For their custom-built malware distribution, Gamaredon Group primarily makes use of compromised domains, dynamic DNS providers, Russian and Ukrainian country code top-level domains (ccTLDs), and Russian hosting providers. The new malware is very sophisticated, and it is able to avoid the detection of security solutions.

While Gamaredon has started using new malware, it also relies on self-extracting archives (SFX) and much of the same infrastructure as when its activities were first analyzed.

In January 2022, Symantec researchers [reported](https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/shuckworm-gamaredon-espionage-ukraine) that Gamaredon initiated a campaign between July and August 2021, targeting Ukrainian organizations. The campaign included the sending of spear phishing email messages embedded with malicious macro codes. Once the macro was enabled, it executed a VBS file that dropped the group's custom backdoor, Pteranodon. In addition, Gamaredon used 8 other malicious payloads that were dropped from 7-zip SFX self-extracting binaries. These payloads had different functionalities, such as creating scheduled tasks, connecting to a C2 server, and downloading additional files.

In February 2022, cybersecurity researchers [reported](https://venturebeat.com/2022/02/03/cyberattack-was-attempted-against-a-western-government-entity-in-ukraine-researchers-say/) that on January 19, 2022, Gamaredon attempted to compromise an undisclosed Western government entity operating in Ukraine. This was done as part of a phishing campaign, in which the threat actors leveraged a Ukrainian job search and employment platform to upload a malware downloader masquerading as a resume for a job ad that was posted by the targeted organization.

In addition, the researchers discovered another Gamaredon campaign that took place in December 2021 and targeted the State Migration Service (SMS) of Ukraine. The threat actors used weaponized Word documents that deployed an open-source UltraVNC virtual network computing (VNC) software for maintaining remote access to the compromised systems. Gamaredon was observed to use an infrastructure of more than 700 malicious domains, 215 IP addresses, and over 100 samples of malware. The group was also found to recycle its used domains by consistently rotating them across new infrastructure, which is unique among threat actors.

**Targeted Industry / Sector**

  * Government
  * TechnologyStay vigilant



## 4\. APT29 (AKA Dukes or Cozy Bear)

APT29 is a well-resourced, highly dedicated, and organized cyberespionage group. Security researchers [suspect](https://www.gov.uk/government/news/uk-condemns-russian-intelligence-services-over-vaccine-cyber-attacks) that the group is a part of the Russian intelligence services. The group has been active since at least 2008, and its main purpose is to collect intelligence in support of foreign and security policy decision-making.

APT29 primarily targets Western governments and related organizations, such as government ministries and agencies, political think tanks, governmental subcontractors, diplomatic, healthcare organizations, and energy targets.

APT29 engages in targeted campaigns, utilizing different toolsets. The targets and timing of these campaigns appear to align with the known foreign and security policy interests of the Russian Federation at those times.

The group frequently uses publicly available exploits to conduct widespread scanning and exploitation against vulnerable systems, likely in an effort to obtain authentication credentials to allow further access. This broad targeting gives the group potential access to a large number of systems globally, many of which are unlikely to be of immediate intelligence value. The group may maintain a store of stolen credentials in order to access these systems in the event that they become more relevant in the future.

In addition to targeted attacks, APT29 has engaged in apparently biannual large-scale spear-phishing campaigns against hundreds or even thousands of recipients associated with governmental institutions and affiliated organizations. These campaigns involve a fast but noisy break-in followed by a rapid collection and exfiltration of as much data as possible. If the compromised target is discovered to be of value, APT29 switches the toolset used and moves to using stealthier tactics focused on persistent compromise and long-term intelligence gathering.

Throughout 2020, APT29 has [targeted](https://media.defense.gov/2020/Jul/16/2002457639/-1/-1/0/NCSC_APT29_ADVISORY-QUAD-OFFICIAL-20200709-1810.PDF) various organizations involved in COVID-19 vaccine development in Canada, the United States, and the United Kingdom, most likely with the intention of stealing information and intellectual property relating to the development and testing of COVID-19 vaccines. 

**Targeted industries/sectors**

  * Telecom
  * Technology
  * Pharmaceutical  




## 5\. APT28 (AKA Fancy Bear)

APT 28, also called Group 74, Pawn Storm, SNAKEMACKEREL, STRONTIUM, Sednit, Sofacy, Swallowtail, TG-4127, Threat Group-4127, or Tsar Team, is a state-sponsored hacking group associated with the Russian military intelligence agency GRU. The group has been active since 2007 and usually targets privileged information related to government, military, and security organizations. Among the Russian APT groups, Fancy Bear dominated in 2017, especially at the end of that year.

Between February 10 and 14, 2015, during the ceasefire in Donbass (East Ukraine), APT 28 [scanned](https://www.researchgate.net/publication/330071595_Analysis_and_Triage_of_Advanced_Hacking_Groups_Targeting_Western_Countries_Critical_National_Infrastructure_APT28_RED_October_and_Regin_Theories_Methods_Tools_and_Technologies) 8,536,272 Ukrainian IP addresses for possible vulnerabilities. After February 14, 2015, APT28 shifted its attention to the west. They have also scanned for vulnerabilities in Spain, the UK, Portugal, USA, and Mexico.

According to the UK foreign secretary, Dominic Raab, APT28 was responsible for the 2015 cyber attacks on Germany’s Parliament. The official also [said](https://www.reuters.com/article/uk-security-britain-russia/uk-to-enforce-sanctions-on-russian-gru-officers-over-cyber-attacks-on-germany-idUSKBN2772BT), “The UK stands shoulder to shoulder with Germany and our European partners to hold Russia to account for cyberattacks designed to undermine Western democracies. This criminal behavior brings the Russian Government into further disrepute.”

In August 2020, a joint [report](https://media.defense.gov/2020/Aug/13/2002476465/-1/-1/0/CSA_DROVORUB_RUSSIAN_GRU_MALWARE_AUG_2020.PDF) of the NSA and the FBI was released, in which they attributed a new malware to APT28 named Drovorub. Drovorub is a Linux malware consisting of an implant coupled with a kernel module rootkit, a file transfer, and port forwarding tool, and a command and control (C2) server.

When deployed on a victim machine, the Drovorub implant (client) provides the capability for direct communications with the actor-controlled C2 infrastructure, file download and upload capabilities, execution of arbitrary commands as "root," and port forwarding of network traffic to other hosts on the network.

On August 9, 2020, the QuoIntelligence team [disseminated](https://quointelligence.eu/2020/09/apt28-zebrocy-malware-campaign-nato-theme/) a warning to its government customers in Europe about a new APT28 campaign. This campaign targets government bodies of NATO members (or countries cooperating with NATO). The researchers discovered a malicious file uploaded to VirusTotal, which ultimately drops a Zebrocy malware and communicates with a C2 in France.

In September 2020, Microsoft researchers [reported](https://www.nytimes.com/2020/09/10/us/politics/russian-hacking-microsoft-biden-trump.html) that state-sponsored Russian hacking group APT28 was observed targeting organizations and individuals involved in the US presidential election. According to the researchers, the group’s efforts are focused on stealing the targets' credentials and compromising their accounts to potentially disrupt the elections and to harvest intelligence to be used as part of future attacks.

**Targeted industries/sectors**

  * Military
  * Security
  * Government
  * Press



## UPDATE [March 10, 2022]: Conti Ransomware Group

At the time of this blog post’s publication on March 3, 2022, the future of the Conti Ransomware Group seemed uncertain. It's now clear that the group remains a major and formidable threat.

Conti is a ransomware and extortion group that has been active since at least December 2019. The group largely targets corporate networks and is notable for their sophistication and the professional quality of their “support” following a successful attack. Furthermore, Conti’s level of association with other known cybercrime organizations such as Ryuk and Trickbot goes beyond what is typical for ransomware groups. Conti follows a so-called “double extortion” approach, not only encrypting victim files with ransomware and demanding a ransom – to be paid in bitcoin – for the key but also stealing sensitive files and threatening their release on a leak site if the ransom demand is not met.

Conti generally operates by gaining initial access via phishing or exploitation of internet-facing vulnerabilities. They then use techniques like [Kerberoasting](/fundamentals/kerberoasting-attack/) or Mimikatz to allow for lateral movement in a victim network. They have also been seen using Cobalt Strike in their attacks. 

Conti has hacked a number of high-profile victims, including [the Fourth District Court of Louisiana in September 2021](https://www.darkreading.com/attacks-breaches/ransomware-hits-us-district-court-in-louisiana) and [Ireland’s National Health Service in January 2021](https://www.bleepingcomputer.com/news/security/irelands-health-services-hit-with-20-million-ransomware-demand/). The Conti group is quick to adopt new vulnerabilities, as we learned from [a leaked “playbook”](https://www.bleepingcomputer.com/news/security/translated-conti-ransomware-playbook-gives-insight-into-attacks/) in September 2021, in which a number of exploits that were only weeks old had already been put into standard documentation.

No stranger to leaks, [Conti’s internal chat logs were released](/blog/post/2022/03/01/conti-ransomware-group-internal-chats-leaked-over-russia-ukraine-conflict/) on February 27, 2022 following an internal schism over the Russia-Ukraine conflict. The logs included a substantial amount of information about Conti’s internal operations including their interview process, how affiliates are paid, and details of operations. Notably, Conti’s primary bitcoin address was leaked in the chats, revealing Conti’s war chest of roughly $2 billion USD in bitcoin. The chats also referenced “FSB” and “Navalny,” presumably a reference to an alleged hack of media outlet Bellingcat in order to obtain information about Russian opposition leader Alexei Navalny on behalf of Russian state intelligence. 

Following the leaks, Conti was observed taking down their known operational infrastructure. As of March 9, 2022, Conti’s leak site has resumed normal operations.

## Notable cyber adversaries

Based on their previous cyber operations against Western countries and due to their direct or indirect implication in the current Russian/Ukrainian cyber conflict, we’ve identified these APT groups as potential cyber threats. The sophistication of their attacks and the fact that they often target European countries and the US make them a higher risk. We, along with the rest of the cybersecurity community, will continue to monitor the activities of these threat actors, and we recommend security teams worldwide do the same.

_**Additional reading:**_

  * [_Conti Ransomware Group Internal Chats Leaked Over Russia-Ukraine Conflict_](/blog/post/2022/03/01/conti-ransomware-group-internal-chats-leaked-over-russia-ukraine-conflict/)
  * [ _Russia/Ukraine Conflict: What Is Rapid7 Doing to Protect My Organization?_](/blog/post/2022/02/25/russia-ukraine-conflict-what-is-rapid7-doing-to-protect-my-organization/)
  * [_Staying Secure in a Global Cyber Conflict_](/blog/post/2022/02/25/russia-ukraine-staying-secure-in-a-global-cyber-conflict/)
  * [ _Prudent Cybersecurity Preparation for the Potential Russia-Ukraine Conflict_](/blog/post/2022/02/15/prudent-cybersecurity-preparation-for-the-potential-russia-ukraine-conflict/)

  


## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)