# How CrowdStrike Protects Against Domain Impersonations

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-crowdstrike-protects-against-domain-impersonations/
- **Date :** November 14, 2022

---

# Evicting Typosquatters: How CrowdStrike Protects Against Domain Impersonations

November 14, 2022

• [ jackie.abrams](/en-us/blog/author.jackie-abrams/ "Posts by jackie.abrams") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


Threat actors constantly unleash phishing attacks that use emails or text messages containing domains or URLs, all designed to impersonate well-known companies and trick users into visiting fake websites and entering their logon or other confidential information. Unfortunately, many users fall prey to such attacks, unknowingly giving threat actors access to their work or personal accounts. The results are stark — according to Cisco’s [2021 Cybersecurity Threat Trends report](https://umbrella.cisco.com/info/2021-cyber-security-threat-trends-phishing-crypto-top-the-list), about 90% of data breaches result from [phishing](/en-us/cybersecurity-101/social-engineering/phishing-attack/).

Domain impersonation, aka “typosquatting” — wherein a threat actor either registers a website or URL designed to impersonate a company or brand, or takes over a legitimate website or URL — has long been a key part of phishing attacks, but its implementation has evolved. Originally used to capture unwary users who mistyped the URL of a website they wanted to visit, domain impersonation is now used to drive business email compromise and SMS-based phishing attacks, and even to conceal command-and-control (C2) servers during malware attacks.

The uses of domain impersonation have evolved, including the availability of generic top-level domains (gTLDs) and the ability to use foreign character sets with visually similar characters when constructing domains for launching attacks — commonly known as punycode attacks. Identifying malicious infrastructure before it can be used in an attack is crucial for protecting targeted organizations and their customers.

## Falcon Intelligence Recon Now Detects Domain Impersonations

[CrowdStrike Falcon Intelligence Recon™](/en-us/services/managed-services/managed-digital-risk-protection/) can now detect instances of typosquatting. This new feature enables security teams and threat intel analysts to create monitoring rules that analyze domains for key terms associated with an organization or brand, and to alert when malicious infrastructure has been created or updated potentially for use in an impersonation attack. A new “loosely” match operator looks for variations of a single word, such as character additions, subtractions and substitutions, including the use of characters in other languages. Monitoring rules can also look for matches on words that are part of longer domains and TLDs.

After Falcon Intelligence Recon detects such infrastructure, it sends users a notification with a full profile of the detected domain — including WhoIs information, IP addresses, name servers MX records, SSL certificates and email addresses — sourced from all available data, including Start of Authority records.

[**Watch Falcon Intelligence Recon in action in this quick demo.**](https://www.youtube.com/watch?v=Co-P7myklMU)

This new Falcon Intelligence Recon capability can help users make an informed decision about the threat, identify organizations responsible for hosting the threat and identify the potentially malicious actors that created the infrastructure.

### Common Attack Examples

**widget.com**|  Actual Site  
---|---  
**w1dget.com**|  Typosquatting leveraging substitution  
**widgett.com**|  Typosquatting leveraging addition  
**widgt.com**|  Typosquatting leveraging subtraction  
**widget-account-recovery.com**|  Typosquatting leveraging hyphens  
**widget.com.accountlogin.com**|  Typosquatting leveraging subdomains  
**widget.com.login**|  Typosquatting leveraging gTLDs  
**wid.get**|  Typosquatting leveraging gTLDs  
**log.in/widget**|  Typosquatting leveraging URLs  
  
### Example with Foreign Character Sets

**widget.com**|  Actual Domain  
---|---  
**widget.com**|  Site with Cyrillic “e” _Note: Sites leveraging international characters may be displayed in punycode by some browsers, which displays domains with characters from non-latin alphabets with a 4-character prefix of “xn--” and the unicode translated to ASCII Compatible Encoding (ACE)_  
  
With the average cost of a breach reaching an estimated [$4.35 million USD in 2022](https://www.ibm.com/reports/data-breach), it’s more important than ever that businesses take steps to mitigate the risk of domain impersonation attacks. By using Falcon Intelligence Recon to monitor for emerging and active typosquatting threats, companies can be forewarned of malicious activity and take steps to protect their employees and customers, and, in turn, protect their companies’ systems, assets and reputation.

#### Additional Resources

  * _[Watch this introductory video](https://www.youtube.com/watch?v=0PjOLMuLIrA) and register for a free[ hands-on Lab](https://criminalunderground.splashthat.com) to see Falcon Intelligence Recon in action._
  * _Learn more about the adversaries CrowdStrike tracks by exploring the[ Adversary Universe](https://adversary.crowdstrike.com) — and experience it for yourself during the [CrowdStrike Adversary Universe World Tour 2022](/en-us/events/adversary-universe-world-tour/)._
  * _To stay ahead of today’s adversaries, read the[ CrowdStrike 2022 Global Threat Report](/en-us/global-threat-report/)._
  * _[Request a free trial](/en-us/free-trial-guide/) of the industry-leading CrowdStrike Falcon® platform._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)