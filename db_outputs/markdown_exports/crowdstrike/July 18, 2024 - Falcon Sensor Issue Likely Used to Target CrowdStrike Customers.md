# Falcon Sensor Issue Likely Used to Target CrowdStrike Customers

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/falcon-sensor-issue-use-to-target-crowdstrike-customers/
- **Date :** July 18, 2024

---

# Falcon Sensor Content Issue from July 19, 2024, Likely Used to Target CrowdStrike Customers

July 18, 2024

• [ Counter Adversary Operations](/en-us/blog/author.counter-adversary-operations/ "Posts by Counter Adversary Operations") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


_Updated 2024-07-26 1830 UTC_

On July 19, 2024, an issue present in a single content update for the CrowdStrike Falcon® sensor impacting Windows operating systems was identified, and a fix was deployed.1

CrowdStrike Intelligence has monitored for malicious activity leveraging the event as a lure theme and received reports that threat actors are conducting the following activity:

  * Sending phishing emails posing as CrowdStrike support to customers
  * Impersonating CrowdStrike staff in phone calls
  * Posing as independent researchers, claiming to have evidence the technical issue is linked to a cyberattack and offering remediation insights
  * Selling scripts purporting to automate recovery from the content update issue



Figure 1 provides a list of domains identified on July 19, 2024, that impersonate CrowdStrike’s brand. Some domains in this list are not currently serving malicious content or could be intended to amplify negative sentiment. However, these sites may support future social-engineering operations.

`  
crowdstrike0day[.]com  
crowdstrikebluescreen[.]com  
crowdstrike-bsod[.]com  
crowdstrikeupdate[.]com  
crowdstrikebsod[.]com  
www.crowdstrike0day[.]com  
www.fix-crowdstrike-bsod[.]com  
crowdstrikeoutage[.]info  
www.microsoftcrowdstrike[.]com  
crowdstrikeodayl[.]com  
crowdstrike[.]buzz  
www.crowdstriketoken[.]com  
www.crowdstrikefix[.]com  
fix-crowdstrike-apocalypse[.]com  
microsoftcrowdstrike[.]com  
crowdstrikedoomsday[.]com  
crowdstrikedown[.]com  
whatiscrowdstrike[.]com  
crowdstrike-helpdesk[.]com  
crowdstrikefix[.]com  
fix-crowdstrike-bsod[.]com  
crowdstrikedown[.]site  
crowdstuck[.]org  
crowdfalcon-immed-update[.]com  
crowdstriketoken[.]com  
crowdstrikeclaim[.]com  
crowdstrikeblueteam[.]com  
crowdstrikefix[.]zip  
crowdstrikereport[.]com`

_Figure 1. Identified malicious domains_

CrowdStrike Intelligence recommends that organizations ensure they are communicating with CrowdStrike representatives through official channels and they adhere to technical guidance the CrowdStrike support teams have provided.2

The following CrowdStrike Falcon® LogScale query hunts for domains provided in Figure 1.
    
    
    // Potentially malicious domains impersonating CrowdStrike (CSA-240832)
    // hunting rule for indicators (CSA-240832)
    in("DomainName", values=["crowdfalcon-immed-update.com", "crowdstrike-bsod.com", "crowdstrike-helpdesk.com", "crowdstrike.buzz", "crowdstrike0day.com", "crowdstrikebluescreen.com", "crowdstrikeblueteam.com", "crowdstrikebsod.com", "crowdstrikeclaim.com", "crowdstrikedoomsday.com", "crowdstrikedown.com", "crowdstrikedown.site", "crowdstrikefix.com", "crowdstrikefix.zip", "crowdstrikeodayl.com", "crowdstrikeoutage.info", "crowdstrikereport.com", "crowdstriketoken.com", "crowdstrikeupdate.com", "crowdstuck.org", "fix-crowdstrike-apocalypse.com", "fix-crowdstrike-bsod.com", "microsoftcrowdstrike.com", "whatiscrowdstrike.com", "www.crowdstrike0day.com", "www.crowdstrikefix.com", "www.crowdstriketoken.com", "www.fix-crowdstrike-bsod.com", "www.microsoftcrowdstrike.com"]) | table([cid, aid, #event_simpleName, ComputerName])
    

_Figure 2. Falcon LogScale Query_

#### Additional Resources

  * _For more information, this blog post is being updated regularly:[ Statement on Falcon Content Update for Windows Hosts](https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/)._
  * _Read this message from George Kurtz, CrowdStrike Founder and CEO:[ To Our Customers and Partners](https://www.crowdstrike.com/blog/our-statement-on-todays-outage/)._
  * _For technical information, see this blog post:[ Technical Details: Falcon Content Update for Windows Hosts.](https://www.crowdstrike.com/blog/technical-details-on-todays-outage/)_
  * _Read another blog post from CrowdStrike Intelligence regarding the Falcon content issue:[Likely eCrime Actor Uses Filenames Capitalizing on July 19, 2024, Falcon Sensor Content Issues in Operation Targeting LATAM-Based CrowdStrike Customers.](http://www.crowdstrike.com/blog/likely-ecrime-actor-capitalizing-on-falcon-sensor-issues/)_



  1. <https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/>
  2. Ibid.



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)