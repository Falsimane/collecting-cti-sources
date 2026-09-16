# Improved ECX Model Shows Increasing Relevance of Access Broker Market

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/increasing-relevance-of-access-broker-market-shown-in-improved-ecx-model/
- **Date :** April 22, 2021

---

# Increasing Relevance of Access Broker Market Shown in Improved ECX Model

April 22, 2021

• [ CrowdStrike Intelligence Team](/en-us/blog/author.crowdstrike-intelligence-team/ "Posts by CrowdStrike Intelligence Team") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


The eCrime ecosystem is an active and diverse economy of financially motivated threat actors

that engage in a myriad of criminal activities in order to generate revenue. With the _[eCrime Index](https://adversary.crowdstrike.com)_ (ECX), CrowdStrike’s Intelligence team maintains a composite score to track changes to this ecosystem, including changes in eCrime activity, risk and related costs. In recent weeks, the Intel team has observed a notable shift in advanced [ransomware](/en-us/cybersecurity-101/ransomware/) operations: Access brokers have increased their prices for stolen credentials that provide access to victim organizations, indicating that threat actors are receiving a greater return on their investment. The ECX is composed of several key observables covering different aspects of criminal activity that are combined using a mathematical model. To best express the state of cybercrime, this model is consistently improved. An update in April 2021 accounts for a bias that can inflate an index value: When expressing changes as percentages of the previous observed value, increases were overrepresented compared to decreases. The updated model corrects this bias, resulting in a more robust index value.

## Criminal Activity Is Increasing in 2021

Looking at how the updated ECX has behaved since the beginning of 2021, a steady increase can be identified. Figure 1 shows the plot points and a trend line for values since January.

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/04/Screen-Shot-2021-04-22-at-3.24.40-PM-1-1024x625.png)Figure 1. Trend in the eCrime Index (ECX) in 2021

One of the main factors responsible for this trend is an increase in prices charged for access to vulnerable devices, services or stolen credentials on underground forums. Advanced, targeted ransomware operations, referred to as _big game hunting_ (BGH), leverage this access to encrypt data and extort large sums from victim organizations in exchange for decryption keys, creating a lucrative market for access brokers.

## Access Brokers Are Profiting

Access brokers are threat actors that gain backend access to targeted victim organizations with the intent of selling it to other threat actors. This access is commonly obtained through the use of credentials collected by commodity [malware](/en-us/cybersecurity-101/malware/), password brute-forcing or exploiting unpatched vulnerabilities. Advertisements of access to target organizations are often similar in structure and contain information about an entity that allows potential buyers to assess the value, such as the business vertical, the publicly reported revenue or the estimated number of employees. In some cases, the actor will also advertise the access method, such as RDP or VPN, and whether the access includes escalated privileges, frequently announced as “domain administrator” or “full access.”

## Prices Are Rising

In recent months, CrowdStrike Intelligence has observed advertisements for access to corporate entities listed from five figures to as much as 10 BTC (currently valued at about $568,000 USD; see Figure 2). Pricing is typically based on the target’s publicly stated revenue as well as its geographic tiers. Tier 1 includes the United States, Canada, Australia, New Zealand and the United Kingdom; Tier 2 covers Europe and Southeast Asia; and Tier 3 includes the Middle East, Japan and South Korea.

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/04/ECX-figure-2.png)Figure 2. Access broker advertisement requesting a six-figure price

Access broker pricing used in the ECX is taken from advertised prices across various underground forums. While changes in the advertised prices often occur during negotiations with interested parties in private communications channels where visibility is limited, they still indicate general trends. These trends are corroborated by several confirmed cases in which threat actors paid up to $100,000 USD for access to one target organization, which indicates that buyers are willing to pay six figure amounts for this service. The observed cases are not related to the advertisement in Figure 2.

## What Does It Mean?

There is a lucrative market for access brokers who gain initial access to entities through stolen credentials, and then advertise this access on underground forums for a price. These prices fluctuate based on the nature of the access and the value of the compromised organization: While the vast majority of access is sold at lower prices, higher-priced offerings increase the average rate, as reflected in the ECX. An increase in the purchasing price for access indicates that threat actors receive a return on their investment. With ransom demands in the tens of millions of dollars, prices for access to target organizations are unfortunately expected to increase further. To make sure you stay up-to-date on eCrime trends, monitor the ECX regularly in the [Adversary Universe](https://adversary.crowdstrike.com).

#### Additional Resources

  * _Learn how[ CrowdStrike Falcon® Intelligence Recon](/en-us/products/threat-intelligence/falcon-x-recon/) mitigates digital risk from the deep, dark web and beyond._
  * _Read about big game hunting adversaries tracked by CrowdStrike Intelligence in 2020 in the[ CrowdStrike 2021 Global Threat Report](/en-us/resources/reports/global-threat-report/)._
  * _To find out how to incorporate intelligence on threat actors into your security strategy, visit the[ CROWDSTRIKE FALCON® INTELLIGENCE™ Threat Intelligence page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Learn about the powerful, cloud-native[ CrowdStrike Falcon® platform by visiting the product webpage.](/en-us/endpoint-security-products/)_
  * _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html)and learn how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)