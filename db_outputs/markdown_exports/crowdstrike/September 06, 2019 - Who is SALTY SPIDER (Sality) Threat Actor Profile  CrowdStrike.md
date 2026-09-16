# Who is SALTY SPIDER (Sality)?| Threat Actor Profile | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/who-is-salty-spider/
- **Date :** September 06, 2019

---

# Who is Salty Spider (Sality)?

September 06, 2019

• [ AdamM](/en-us/blog/author.adamm/ "Posts by AdamM") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


## Common Aliases

SALTY SIDER is most commonly identified with the botnet it maintains (Sality) and it’s associated pseudonyms:

__

  * _KuKu_
  *  _SalLoad_
  *  _Kookoo_
  *  _SaliCode_
  *  _Kukacka_****



## SALTY SPIDER’s Origins

**SALTY SPIDER is an eCrime group whose actions likely indicate that it’s operating out of Russia** – specifically in the Republic of Bashkortostan, a region close to the Kazakhstan border. This adversary has been linked to a botnet known as Sality, which is a polymorphic file infector first discovered in 2003. Since 2008, the initial botnet has been superseded by at least three more advanced peer-to-peer (P2P) versions. Beginning in the Summer of 2017, the botnet’s population grew significantly when it began exploiting the ETERNALBLUE vulnerability. **Today, the latest versions of Sality are still both prevalent and formidable.**

****

****

## SALTY SPIDER’s Targets

The pervasiveness of Salty Spider’s attacks has resulted in a long list of victims across the globe. While it seems, for the most part, that **this adversary doesn’t single out particular nations and industries** , there do appear to be a few pockets where SALTY SPIDER may be more prevalent.

### Target Nations

Generally, SALTY SPIDER does not appear to be selective when it comes to the nations it targets — the group’s activities have been observed worldwide. However, **CrowdStrike has observed higher volumes of Sality v3 infections in Romania and high volumes of v4 activity in Venezuela.** The reasoning for these higher pockets of activity in Romania and Venezuela remains unknown.

### Target Industries

In 2017, SALTY SPIDER ceased propagation of traditional proxy and spambot payloads, and shifted its sights towards the **mining and theft of cryptocurrencies**. This shift is likely an indicator that the cryptocurrency industry has proven to be a more lucrative area for monetizing Sality.

## SALTY SPIDER’s Methods

The main goal of the Sality P2P botnet is quite straightforward — infect the machine and propagate secondary payloads. This allows Sality malware to forgo extensive built-in functionality. In fact, the malware is only known to maintain the infection and manage the connection between the machine and the botnet. Once a machine has been compromised by the polymorphic file infector, which adds the malware through legitimate executables, operators can then instruct the device to download and execute payloads. Due to SALTY SPIDER’s affinity for cryptocurrencies, these payloads have been observed querying the machine’s clipboard for strings matching Bitcoin or Ethereum addresses. Matching strings are then replaced with the actor’s own Bitcoin or Ethereum address.

## Other Known “SPIDERS”

SALTY SPIDER is just one of many eCrime adversaries tracked by CrowdStrike Intelligence. Some of other cyber criminal groups that CrowdStrike monitors include the following:

  * [COBALT SPIDER](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-september-cobalt-spider/)
  * [DUNGEON SPIDER](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-october-dungeon-spider/)
  * [MUMMY SPIDER](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-february-mummy-spider/)
  * [WICKED SPIDER](/en-us/blog/meet-crowdstrikes-adversary-of-the-month-for-july-wicked-spider/)



_Curious about other eCrime, hacktivist or nation-state adversaries? Visit our_[ _threat actor center_](/en-us/blog/meet-the-adversaries/) _to learn about the new adversaries that the CrowdStrike team discovers._

## Learn More About the Cyber Threat Landscape

**Want more insights on the latest adversary tactics, techniques, and procedures (TTPs)?** Download the CrowdStrike® 2019 Global Threat Report: Adversary Tradecraft and The Importance of Speed: **Download:[CrowdStrike 2020 Global Threat Report](/resources/reports/2020-crowdstrike-global-threat-report.html).** To learn more about how to incorporate intelligence on [threat actors](https://www.crowdstrike.com/cybersecurity-101/threat-actor/) like SALTY SPIDER into your security strategy, please visit the [Falcon Threat Intelligence page](/content/crowdstrike-www/locale-sites/us/en-us/endpoint-security-products/falcon-x-threat-intelligence/?ctm_source=Website&ctm_medium=Blog&ctm_campaign=Blog-Inline-Copy).

#### Additional Resources

  * _Read the[report on CrowdStrike Falcon® Intelligence Automated Threat Intelligence](/en-us/resources/data-sheets/crowdstrike-falcon-adversary-intelligence/) to learn what contextualized, actionable threat intelligence can add to your security effectiveness._
  * _Learn more about comprehensive endpoint protection with the CrowdStrike Falcon® ® platform by [visiting the product page](/endpoint-security-products/falcon-platform.html)._
  * _Test CrowdStrike next-gen AV for yourself. Start your[free trial of Falcon Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) today._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)