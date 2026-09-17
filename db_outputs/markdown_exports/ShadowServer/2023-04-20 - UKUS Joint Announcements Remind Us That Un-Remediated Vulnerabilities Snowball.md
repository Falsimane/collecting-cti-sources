# UK/US Joint Announcements Remind Us That Un-Remediated Vulnerabilities Snowball

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/uk-us-joint-announcements-remind-us-that-un-remediated-vulnerabilities-snowball/
- **Date :** 2023-04-20

---

# UK/US Joint Announcements Remind Us That Un-Remediated Vulnerabilities Snowball

April 20, 2023

The [UK’s National Cyber Security Centre (NCSC)](https://www.ncsc.gov.uk/news/uk-and-us-issue-warning-about-apt28-actors-exploiting-poorly-maintained-cisco-routers) and the [US Cybersecurity and Infrastructure Security Agency (CISA)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-108) issued an alert on nation-state sponsored exploitation of router infrastructure.

The [“UK and US issue warning about APT28 actors exploiting poorly maintained Cisco routers” alert](https://www.ncsc.gov.uk/news/uk-and-us-issue-warning-about-apt28-actors-exploiting-poorly-maintained-cisco-routers) called out SNMP public exposure and one vulnerability in particular – [CVE-2017-6742](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170629-snmp) which relates to a long known “remote code execution” opportunity on certain Cisco routers. Bad actors who find this vulnerability available to them can use it to execute any piece of code they choose. You can read more details [here](https://www.ncsc.gov.uk/news/apt28-exploits-known-vulnerability-to-carry-out-reconnaissance-and-deploy-malware-on-cisco-routers).

This alert is a timely reminder for all with unpatched equipment to think broadly!

Don’t just consider your computer when patching – remember any device in your network (including your router) that connects to the Internet should be checked with a view to patching if a patch is available. If you fail to do this you are leaving yourself and your network’s users potentially vulnerable.

In this case good advice is [available from Cisco themselves](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170629-snmp), who have even provided a software checker to see if your version of software is impacted on the link above.

This reporting reminds us that just because a CVE is old, it does not mean attackers will not try to exploit it if they can find it present on a system (be they nation state, criminal or both). In short – vulnerable devices remain so until the owner/operator changes the situation. Vulnerabilities simply do not ‘age off’, rather they just add to the attackers’ available arsenal if left unaddressed.

Whilst we do not scan the Internet for this specific vulnerability at present – [our dashboard does give a feel for how many exposed SNMP devices](https://dashboard.shadowserver.org/statistics/combined/tree/?day=2023-04-19&source=scan&source=scan6&tag=snmp&geo=all&data_set=count&scale=log) are out there.

Plus we are also [able to see the distribution of Cisco devices (not just for SNMP exposure)](https://dashboard.shadowserver.org/statistics/iot-devices/tree/?day=2023-04-19&vendor=cisco&geo=all&data_set=count&scale=log) are out there.

We share IP level data (filtered by your network/constituency) on the above in our [Open SNMP](/what-we-do/network-reporting/open-snmp-report/) and [Device Identification](/what-we-do/network-reporting/device-identification-report/) reports.

You can also view the list of CVEs that we see [being systematically exploited](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vulnerability/?category=monitoring&statistic=unique_ips) on our dashboard as well as [lists of compromised device types](https://dashboard.shadowserver.org/statistics/honeypot/monitoring/vendor/?category=monitoring&statistic=unique_ips) that are spreading attacks.

We encourage you to follow the [UK NCSC’s clear heightened threat guidance](/news/uk-us-joint-announcements-remind-us-that-un-remediated-vulnerabilities-snowball/http:/\[https:/www.ncsc.gov.uk/guidance/actions-to-take-when-the-cyber-threat-is-heightened/) published shortly before Russia’s invasion of Ukraine last year. The guidance includes suggested actions to ensure basic cyber hygiene, including a recommendation to “check your Internet footprint” by performing “an external vulnerability scan of your whole Internet footprint and check that everything you need to patch is patched.” This is all sound advice and we would endorse it as good practice.

Also – remember that in addition to providing free country-level data to the National CSIRTs of 175 countries globally, Shadowserver also provides more than 7,000 subscribers with free daily threat reports directly. These can help network owners identify potential vulnerabilities in their network as a part of our continuing mission to raise the bar of baseline cyber security globally.

If you own a network and would like to receive Shadowserver’s free daily network threat reports, [you can subscribe here](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/).

If you like what we do and want to **join the growing Shadowserver Alliance** – please feel free to [explore the options here](https://www.shadowserver.org/partner/).

Making a sound base level of cyber security awareness available for free to **ALL** so those who need it most are not disadvantaged, benefits **ALL** who rely on the Internet. You may want to review those who demonstrate they understand this by funding our altruistic mission. We thank them all and ask you to too.

  * [Alliance](/topics/alliance/)
  * [Botnets](/topics/botnets/)
  * [Bots](/topics/bots/)
  * [Funding](/topics/funding/)
  * [Honeypots](/topics/honeypots/)
  * [Malware](/topics/malware/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Shadowserver](/topics/shadowserver/)
  * [Statistics](/topics/statistics/)
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