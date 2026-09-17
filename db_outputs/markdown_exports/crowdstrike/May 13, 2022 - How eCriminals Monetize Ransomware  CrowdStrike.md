# How eCriminals Monetize Ransomware | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-ecriminals-monetize-ransomware/
- **Date :** May 13, 2022

---

# Follow the Money: How eCriminals Monetize Ransomware

May 13, 2022

• [ Bart Lenaerts-Bergmans](/en-us/blog/author.bart-lenaerts-bergmans/ "Posts by Bart Lenaerts-Bergmans") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


The transaction details and monetization patterns of modern eCrime reveal critical insights for organizations[ defending against ransomware](/en-us/cybersecurity-101/ransomware/ransomware-detection/) attacks.

Cybercrime has evolved over the past several years from simple “spray and pray” attacks to a sophisticated criminal ecosystem centered around highly effective monetization techniques that enable adversaries to maximize success and profitability.

Monetization is the

step attackers take to receive a payout when an operation is complete. Threat actors are constantly evolving their methods through trial and error to avoid getting caught. A greater understanding of how this process works — including transaction details, value of recent compromises and participating adversaries — can help organizations fight modern threat actors.

CrowdStrike threat intelligence offers IT and security decision-makers insights into eCrime monetization through our eCrime Index intelligence reports. Here, we dig into our recent observations and share key takeaways for defenders.

## Cryptocurrency Is King

Bitcoin is the cryptocurrency of choice in ransomware campaigns for a few reasons; namely, it is easiest to obtain and broadly available. Bitcoin wallets don’t require personally identifiable information, so demanding a ransom in Bitcoin makes it easy for victims to pay up while letting adversaries stay anonymous.

Not all of the details of Bitcoin are hidden, however. The value of each transaction and Bitcoin wallet is publicly viewable, allowing attackers and law enforcement alike to follow payments to their final destinations. And while a wallet holder’s identity is hidden, Bitcoin can be exchanged for fiat currency at any number of cryptocurrency exchanges, where the adversary’s identity may be exposed.

To boost anonymity, attackers often use “mixing services,” which redistribute Bitcoin from various sources across different addresses to conceal the original source of the funds and hinder analysis of the transaction. Another method used to ensure anonymity and prevent tracing of funds is to “jump chains,” in which cybercriminals convert currency to another format such as Monero (XMR) — a form of cryptocurrency many attackers prefer for its anonymity.

## Ransom Demands Vary — A Lot

The value of suspicious activity reported in ransomware-related Suspicious Activity Reports during the first six months of 2021 was $590 million USD, compared with $416 million reported in all of 2020, according to [data from the U.S. Treasury Department’s Financial Crimes Enforcement Network (FinCen)](https://www.fincen.gov/sites/default/files/2021-10/Financial%20Trend%20Analysis_Ransomware%20508%20FINAL.pdf). CrowdStrike experts also saw an increase: Our [intelligence team calculated](/en-us/press-releases/crowdstrikes-annual-threat-report-exposes-evolution-of-ecrime-ecosystem/) an average ransom demand of $6.1 million USD in 2021 — a 36% jump from 2020.

## Access Brokers Make Their Own Price Lists

Access brokers breach victims’ infrastructure then sell illicitly obtained credentials or other access methods in underground communities. Malware operators or affiliates buy access information so they don’t have to break in themselves — leading to faster and more-targeted attacks.

The cost of this access varies. CrowdStrike’s Intelligence team has seen prices ranging from $100 to $64,000 USD (the highest identified to date). The factors determining cost may include the level of privilege granted, estimated annual revenue of the target company, number of endpoints, potential amount of data available for exfiltration and reputation of the broker.

## Unpaid Attackers May Auction Your Data

If the victim of ransomware refuses to meet adversaries’ demands, their exfiltrated data may be auctioned on the dark web or a dedicated leak site. This tactic allows the threat actor to make money if their first attempt to monetize is unsuccessful — or increase their profit even if the victim pays. Sometimes the data is sold to other adversaries, who may use it to find new victims or gain personally identifiable information to commit fraud or plan out attacks.

## Ecosystem Supporting eCrime Continues to Thrive

Ransomware may be the most popular source of income for cybercriminals; however, many still rely on other forms of money-making. CrowdStrike Intelligence found multiple traditional methods attackers still use to generate funds. Actors offer various services to support the broader underground economy including spambots, monetization services, pay-per-install and exploit kits.

An example of this is EcoPanel, a customizable web panel that enables users to manage the various steps of reshipping fraud as a way to monetize eCrime. As part of this process, attackers use stolen data to buy high-value goods and ship them to intermediaries in the U.S. or Europe. These “mules” reship them to eCrime actors, who sell the goods in local markets for funds.

## Takeaways for Defenders

Learning how cybercriminals monetize ransomware campaigns is an important step in defending against them. Below are three key lessons IT and security teams can learn:

**Lesson 1:** **Your data will help define your strategy**. Adversaries are after your sensitive corporate data — and if they get it, your organization may be exposed to extortion and other threats further down the road. You must determine the value of your data and where it resides in order to build a multi-layered security strategy that prioritizes data as your most valuable asset and protects it using proper identity management and principles of Zero Trust. The ability to create a layered defense, and plan contingencies around potential failure of its components, is essential to protecting sensitive data.

**Lesson 2** : **Threat intelligence is essential to track eCrime monetization**. The continuous monitoring process requires actionable threat intelligence to understand who might be targeting your data, how they might attack it and the value of your data within the cybercrime ecosystem, so you can determine how to best invest in monitoring solutions.

**Lesson 3** :**The****CrowdStrike eCrime Index (ECX)****helps track eCrime monetization**. [The ECX](https://adversary.crowdstrike.com/en-US/ecrime-index-ecx.html) is based on a range of cybercrime data such as ransomware victims, big game hunting data leaks, attack activities and cryptocurrency rates, all weighted by impact. The ECX is useful to better understand the broader trends of the eCrime ecosystem, and these can be a factor in determining threat activity.

The cybercrime business model is constantly evolving to make room for new eCrime tactics. Learning about these techniques can help IT and security teams better understand their adversaries and, in doing so, strengthen their defenses.

#### Additional Resources

  * _Learn more about common ransomware monetization tactics and the eCrime ecosystem in[ this white paper](/en-us/resources/white-papers/).

_
  *  _Visit the[ CrowdStrike Adversary Universe](https://adversary.crowdstrike.com/en-US.html) to learn more about threat actors and the [CrowdStrike eCrime Index (ECX)](https://adversary.crowdstrike.com/en-US/ecrime-index-ecx.html)._
  * _Learn how to incorporate intelligence on dangerous threat actors into your security strategy by visiting the[ CrowdStrike CROWDSTRIKE FALCON® INTELLIGENCE™ product page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Request a free[ CrowdStrike Intelligence threat briefing](https://go.crowdstrike.com/threat-intelligence-briefing.html?utm_campaign=threatintelligence&utm_content=us&utm_medium=sem&utm_source=goog&utm_term=cyber%20threat%20intelligence&_bt=465670942471&_bk=cyber%20threat%20intelligence&_bm=e&_bn=g&_bg=108022039334&gclid=EAIaIQobChMIqsSdwZ-j7AIV9R6tBh23rQErEAAYASAAEgKc8fD_BwE&_ga=2.145914102.359113952.1606756854-1198667695.1606243810) and learn how to stop adversaries targeting your organization._
  * _Learn more about the[ CrowdStrike Falcon® platform by visiting the product webpage.](/en-us/endpoint-security-products/falcon-platform/)_
  * _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) to see for yourself how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)