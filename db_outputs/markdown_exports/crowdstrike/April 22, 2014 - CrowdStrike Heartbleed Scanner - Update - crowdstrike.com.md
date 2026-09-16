# CrowdStrike Heartbleed Scanner - Update - crowdstrike.com

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/crowdstrike-heartbleed-scanner-update/
- **Date :** April 22, 2014

---

# CrowdStrike Heartbleed Scanner - Update

April 22, 2014

• [ Robin](/en-us/blog/author.robin/ "Posts by Robin") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

**_This is a followup to our original blog post for the[CrowdStrike Heartbleed Scanner](/en-us/blog/new-community-tool-crowdstrike-heartbleed-scanner/)._** Due to popular demand and acting on feedback we have received, today we have updated our free _Heartbleed Scanner_ vulnerability detection tool that was released last Friday. The new version is 1.1.0.0 and is [available for download on the Community Tools](/en-us/community-tools/index/) page. Here are the main additions and changes: 

  * Added _STARTTLS_ support for common services.
  * Added ability to specify a list of default ports as opposed to just a single one.
  * If you double click a vulnerable entry in the results window it will open up an Explorer window and navigate to the binary data file associated with the entry.
  * Fixed an issue with parsing supplied URLs.
  * Fixed an issue with sorting the vulnerability results table when clicking the headers.
  * Fixed issue with tool not adhering to specified timeout value.
  * More robust and accurate vulnerability checking.
  * Simplified HTML output format.
  * Rearranged the UI elements.

With the ability to supply more than a single default port we have provided a sample port list of commonly used SSL-enabled service ports as follows: 
  * 443 HTTPS
  * 465 SMTP over SSL/TLS
  * 563 NNTP over SSL/TLS
  * 636 LDAP over SSL/TLS
  * 990 FTP over SSL/TLS
  * 993 IMAP over SSL/TLS
  * 995 POP3 over SSL/TLS
  * 3306 MySQL (SSL/TLS)
  * 5432 PostgreSQL (SSL/TLS)

If you are only interested in scanning HTTP websites you would probably want to just keep port 443 and have the scan run faster, but for full thoroughness our default list is a good start. For the new STARTTLS feature we attempt to handle the following protocols: 
  * 21 FTP ("_AUTH TLS_ ")
  * 25 SMTP ("_STARTTLS_ ")
  * 110 POP3 ("_STLS_ ")
  * 143 IMAP ("_STARTTLS_ ")
  * 587 Message Submission ("_STARTTLS_ ")

More information can be seen in the tool's _About..._ section. As always keep an eye out for updates to our tools as we continue to enhance them. 

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)