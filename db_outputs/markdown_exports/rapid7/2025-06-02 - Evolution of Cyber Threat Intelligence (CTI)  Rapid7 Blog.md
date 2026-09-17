# Evolution of Cyber Threat Intelligence (CTI) | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/08/25/r-evolution-of-the-cyber-threat-intelligence-practice/
- **Date :** 2025-06-02

---

_Co-authored by Yotam Avitan, Deputy Head of Global CSOC at Novartis_

The cyber threat intelligence (CTI) space is one of the most rapidly evolving areas in cybersecurity. Not only are technology and products being constantly updated and evolved, but also methodologies and concepts. One of the key changes happening in the last few years is the transition from threat intelligence as a separate pillar — which disseminates threat reports to the security organization — to [threat intelligence](/fundamentals/what-is-threat-intelligence/) as a central hub that feeds all the functions in the security organization with knowledge and information on the most prioritized threats. This change requires a shift in both mindset and methodology.

Traditionally, CTI has been considered a standalone practice within the security organization. Whether the security organization has dedicated personnel or not, it has been a separate practice that produces reports about various threats to the organization — essentially, looking at the threat landscape and making the **same** threat data accessible to **all** the functions in the security organization.

**Traditional CTI model**

![Evolution-of-CTIP_Traditional.png](https://www.rapid7.com/cdn/images/blte279eae893055bcd/683ddd4ec26e072d9228e648/Evolution-of-CTIP_Traditional.png)

The latest developments in threat intelligence methodologies are disrupting this concept. Effectively, threat intelligence is no longer a separate pillar, but something that should be ingested and considered in every security device, process, and decision-making event. Thus, the mission of the threat intelligence practitioner is no longer to simply create “threat reports,” but also to make sure that every part of the security organization effectively leverages threat intelligence as part of its day-to-day mission of detection, response, and overall [risk management](/fundamentals/what-is-cybersecurity-risk-management/).

## Trends supporting a new CTI workflow

The evolution of threat intelligence is supported by the following primary trends in the cybersecurity space:

  1. **Automation** — Due to a lack of trained human resources, organizations are implementing more automation into their security operations. Supported by adoption of [SOAR technologies](/solutions/security-orchestration-and-automation/), machine-to-machine communication is becoming much easier and more mainstream. Automation allows for pulling data from your CTI tools and constantly feeding it into various security devices and security processes, without human intervention. Essentially, supporting seamless and near-real-time integration of CTI into various security devices, as well as automated decision-making processes.  

  2. **Expanded access to threat intelligence** — Threat intelligence vendors are investing a lot more in solutions that democratize threat intelligence and make it easy for various security practitioners to consume — for example, native applications for [Security Information and Event Management (SIEM)](/fundamentals/siem/) to correlate threat data against internal logs, or browser extensions that inject threat context and risk analysis into the browser. Previously, you had lots of threat data that needed manual labor to review and take action; today, you have actionable insights that are seamlessly integrated into your security devices.



**Updated CTI model**

![Evolution-of-CTIP_Updated.png](https://www.rapid7.com/cdn/images/blte65939fd8ff30577/683ddd737f8603aff32306b2/Evolution-of-CTIP_Updated.png)

## The new mission of the CTI practitioner

The new mission of the CTI practitioner is to tailor threat intelligence to every function in the security organization and make it an integral part of the function’s operations. This new approach requires them to not only update their mission, but also to gain new soft skills that allow them to collaborate with other functions in the security organization.

The CTI practitioner’s newly expanded mindset and skill set would include:

  1. **Developing close relationships with various stakeholders** — It’s not enough to send threat reports if the internal client doesn’t know how to consume them. What looks simple for a CTI specialist is not necessarily simple to other security practitioners. Thus, in order to achieve the CTI mission, it’s important to develop close relationships with various stakeholders so that the CTI specialist can better understand their pain points and requirements, as well as tailor the best solution for them to consume. This activity serves as a platform to raise their awareness of CTI’s value, thereby helping them come up with and commit to new processes that include CTI as part of their day-to-day.
  2. **Having solid knowledge of the company strategy and operations** — The key to a successful CTI program is relevancy; without relevancy, you're left with lots of unactionable threat data. Relevancy is twice as important when you want to incorporate CTI into various functions within the organization. Relevant CTI can only be achieved when the company business, organizational chart, and strategy are clear. This clarity enables the CTI practitioner to realize what intelligence is relevant to each function and tailor it to the needs of each function.
  3. **Deep understanding of the company tech stack** — The CTI role doesn’t require only business understanding, but also deep technical understanding of the IT infrastructure and architecture. This knowledge will allow the CTI specialist to tailor the intelligence to the risks imposed on the company tech stack, and it will support building a plan to correlate internal logs against external threat intelligence.



Following are a few examples of processes the threat intelligence team needs to implement in order to tailor threat intelligence to other security functions and make it an integral part of their operations:

  1. **Third-party breach monitoring** — With the understanding that the weakest link might be your third party, there’s an increasing importance of timely detection of third-party breaches. CTI monitoring supports early detection of those cases and is followed by the IR team minimizing the risk. An example of this is monitoring ransomware gangs’ leak sites for any data belonging to your company that has been leaked from any [third party](/fundamentals/third-party-risk-management-tprm/).
  2. **SOC incident triage** — One of the main missions of the [Security Operations Center (SOC)](/fundamentals/security-operations-center/) is to identify cyber incidents and make a quick decision on mitigation steps. This can be tremendously improved through threat intelligence information to triage the indicators (e.g., domains and IP addresses) of each event. Threat intelligence is the key to an effective and efficient triage of these events. This can be easily achieved through a threat intelligence browser extension that triages the IOCs while browsing in the SIEM.
  3. **Vulnerability prioritization process** — The traditional vulnerability prioritization process relies on the CVSS score and the criticality of the vulnerable assets. This focuses the prioritization efforts on the **impact** of an exploitation of the vulnerabilities and gives very little focus on the **probability** that these vulnerabilities will be exploited. Hacker chatter from the Dark Web and security researchers’ publications can help provide a good understanding of the probability that a certain vulnerability will actually be leveraged by a threat actor to launch a cyberattack. This probability factor is an essential missing piece in the vulnerability prioritization process.
  4. **Trends analysis** — The CTI practitioner has access to a variety of sources, allowing them to monitor trends in the cybersecurity domain, their specific industry, or in the data held in the company. This should be provided to leadership (not only security leadership) in order to allow smart, agile decision-making on existing risks.
  5. **Threat intel and cybersecurity knowledge sharing** — As with “traditional” intelligence, knowledge sharing can be a major force multiplier in cyber intelligence, too. Threat intel teams should aim to create as much external cooperation with other security teams — especially from the industry they work in — as they can. This will allow the team and the security organization to better understand the risks posed to the industry and, accordingly, their company. This information will also allow the CISO better visibility into the threat landscape that's relevant to the company.



## A valuable proposition

While the evolving CTI model is making threat intelligence implementation a bit more complex, as it includes collaboration with different functions, it makes the threat intelligence itself far more valuable and impactful than ever before. The future of cyber threat intelligence is getting a lot more exciting! Learn more about Rapid7's [Threat Intelligence Platform](/platform/threat-intelligence-tip/). 

## Article tags

  * [Cybersecurity](/blog/tag/cybersecurity/)
  * [Detection and Response](/blog/tag/detection-and-response/)
  * [Threat Intel](/blog/tag/threat-intel/)