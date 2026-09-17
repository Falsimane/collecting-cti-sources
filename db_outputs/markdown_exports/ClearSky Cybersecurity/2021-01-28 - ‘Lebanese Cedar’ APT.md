# ‘Lebanese Cedar’ APT

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/cedar/
- **Date :** 2021-01-28

---

In early 2020, suspicious network activities and hacking tools were found in a range of companies. Comprehensive forensic research of the infected systems revealed a strong connection to a threat actor we call ‘Lebanese Cedar’, ‘Lebanese Cedar’ APT has been operating since 2012. These operations were first discovered by [Check-Point](https://blog.checkpoint.com/2015/03/31/volatilecedar/) researchers and [Kaspersky labs](https://securelist.com/sinkholing-volatile-cedar-dga-infrastructure/69421/) in 2015. Since 2015 Lebanese Cedar APT – also referred to as “Volatile Cedar” – maintained a low profile and operated under the radar.

**Read the full report:[“Lebanese Cedar” APT – Global Lebanese Espionage Campaign Leveraging Web Servers](https://www.clearskysec.com/wp-content/uploads/2021/01/Lebanese-Cedar-APT.pdf)**

In the comprehensive forensic research, a new version of the “Explosive” V4 RAT (Remote Access Tool) or “Caterpillar” V2 WebShell was found within the victim’s networks.

[![](https://www.clearskysec.com/wp-content/uploads/2021/01/image-41.png)](https://www.clearskysec.com/wp-content/uploads/2021/01/image-41.png)_Lebanese Cedar Timeline_

Based on a modified JSP file browser with a unique string that the adversary used to deploy ‘Explosive RAT’ into the victims’ network, we found some 250 servers that were apparently breached by Lebanese Cedar. This file was installed in vulnerable Atlassian (JIRA) and Oracle 10g servers. In order to install the JSP in the vulnerable server, Lebanese Cedar exploit 1-day publicly known vulnerabilities such as CVE-2012-3152.

Our report reveals a partial list of the companies that the group has attacked. The target companies are from many countries including: The United States, the United Kingdom, Egypt, Jordan, Lebanon, Israel, and the Palestinian Authority. We assess that there are many more companies that have been hacked and that valuable information was stolen from these companies over periods of months and years.

[![](https://www.clearskysec.com/wp-content/uploads/2021/01/image-43-550x344.png)](https://www.clearskysec.com/wp-content/uploads/2021/01/image-43.png)Modified JSP File Browser – Scanned world-wide

According to Check-Point’s report, the group is motivated by political and Ideological interests, targeting individuals, companies, and institutions worldwide. We endorse Check Point’s strong case attributing Lebanese Cedar APT to the Lebanese government or a political group in Lebanon. Moreover, there are [several indications](https://www.csmonitor.com/World/Passcode/2015/0601/Cyberattack-tied-to-Hezbollah-ups-the-ante-for-Israel-s-digital-defenses) that link Lebanese Cedar APT to the Hezbollah Cyber Unit.

“Caterpillar WebShell” was found in most of the victims we investigated, in many of the systems we also found traces of “Explosive” RAT. We identified the specific open-source JSP file browser that was modified for the hackers’ purposes. We found that Lebanese Cedar deployed the payload of Explosive RAT into the victims’ network. **Lebanese Cedar is the only known threat actor that uses this code**.

[![](https://www.clearskysec.com/wp-content/uploads/2021/01/image-42-550x258.png)](https://www.clearskysec.com/wp-content/uploads/2021/01/image-42.png)Lebanese Cedar Modus Operandi