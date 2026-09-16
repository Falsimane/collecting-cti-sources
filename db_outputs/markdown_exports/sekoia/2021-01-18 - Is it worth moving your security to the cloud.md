# Is it worth moving your security to the cloud?

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/moving-your-security-to-the-cloud
- **Date :** 2021-01-18

---

Cloud security has been a hot topic in recent years. Every indicator shows a stable growth for the next years, but can companies really move all their security into the cloud?

Today’s world is the world of the cloud. According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2017-06-13-gartner-forecasts-worldwide-cloud-based-security-services-to-grow-21-percent-in-2017), cloud-based security services are estimated to be worth $9bn by the year 2020. While there are some enterprises or divisions for whom cloud-based security isn’t on the priority list, the reality for the majority of businesses, especially rapidly growing ones, is that cloud-based security is the only pathway that provides cost efficient security.

This is why the demand for cloud security is continuously growing, especially among mid-size companies.

## Why would CISOs want to move to the cloud?

As mentioned by [Gartner](https://www.gartner.com/en/newsroom/press-releases/2017-06-13-gartner-forecasts-worldwide-cloud-based-security-services-to-grow-21-percent-in-2017), the cloud-based security services are estimated to be worth $9bn by the year 2020. More and more companies are moving into integrated [cybersecurity](/blog/cybersecurity-skills-shortage-4-advices-to-better-deal-with-it) technology platforms. But soon, instead of using various security solutions like [SOAR](/glossary/soar), [SIEM](/glossary/siem), [threat intelligence platforms](/platform/intelligence) from different vendors, they will start using centrally managed solutions. A unified view of all different technologies will enable information security professionals, especially CISO, to better identify threats, stop them in a timely manner, and improve reactions such as forensics activities.

More and more CISOs prefercloud security solutions because they are continuously updated and patched by the vendor. This also relieves the burden of maintenance for the users and allows them to focus on the business issues that matter the most. Let’s take a closer look at the capabilities of operational cloud-based security solutions.

## SIEM (Security Information and Event Management) in the cloud

The [security information and event management (SIEM) tools](/solutions/siem-replacement) provide centralized analysis and the first stages of incident response. SIEM’s fundamental capabilities include:

  * Log Collection
  * Normalizing Logs into a standard format
  * Security Incident Detection
  * Alerts and Notifications



[SIEM](/glossary/siem) in the cloud aggregates data from various types of systems to present a transparent picture of the actionable security duties of the security team. Let’s consider a [host-based intrusion detection system](https://github.com/ossec/ossec-hids) (IDS): this tool monitors suspicious activity on a host. This involves log files, file integrity, rootkit detection, and Windows registry monitoring. This kind of tools provide useful insights for a SIEM. But SIEM can also perform log collection from infrastructure services, including FTP, mail, DNS, database, web, [firewall](/glossary/firewall), and network-based IDS solutions. A number of commercial network services and security solutions are also integrated into most of the SIEM in the market.

With SIEM in the cloud, you can obtain a proactive notification if a user logs into a cloud server directly instead of reaching it via the normal route. This could highlight that this account has been compromised and is used for looking data it isn’t authorized to view. Furthermore, you could discover that an employee increased their privileges from single user to administrator for an hour and obtained access to information related to various parts of the business.

In the case of on-premises SIEM, you have to manage your own unit efficiently. For example, you have to purchase the SIEM tools that you plan to deploy. But that’s the obvious part. Also, you need to reconsider the infrastructure to efficiently run a SIEM on-premise because we are speaking about assembling and monitoring a perimeter that can be huge, generating logs from many many systems. One more crucial thing is the people. Onboarding, training, and maintaining a cybersecurity team is not a small investment. If you’re considering running your SIEM on-prem, make sure you’ve got the budget for it.

Reacting efficiently to a security threat requires constant, meticulous analysis of continuous events and associated alerts. A [cloud-based SIEM](/blog/xdr-is-not-edr) will assist the company to filter better,[detect faster and examine deeper all the data that are related to an attack](/blog/hunting-and-detecting-cobalt-strike). This is because the solution continuously evolves. The SIEM in the cloud gives an efficient mechanism to operate security monitoring for business, especially when business have started to switch into the cloud for different use cases.

## TIP (Threat Intelligence platforms) in the cloud

The cloud-based [threat intelligence](/glossary/cti) platforms need a minimum effort of integration for the import of collection from various sources and the analysis of the data. The use of external sources can help to discover generic [cyber threats](/blog/reduce-cyber-risks-through-automation) that could affect multiple businesses. The seamless integration of these multiple external collections can be used to identify a limited but very accurate set of valuable elements that could be imported into the customer’s system for detection or hunting.

As an example, a cloud honeypots (https://resources.infosecinstitute.com/topic/what-is-a-honey-pot/, accessed January 18, 2021) mimicking customer assets could be an interesting source. Each action on it will become valuable information for the Threat Intelligence Platform and the cloud-to-cloud link make integration seamless. Applying this example, the security team can discover possible attackers, their devices, their methods and systems, and how they would try to bypass the company’s real security restrictions. It is one proactive security intelligence gathering technique. The cloud-based threat intelligence solutions provide the following benefits:

  * Seamless integration with sources speaking of current and emerging threats and attackers.
  * Easy valuation of homemade intelligence tools which interact with other cloud-based solution.
  * Lot of pre configured integrations or connectors with other cloud-based solutions that also work in cloud. These connectors allows to fasten the refining of the information suited with the customer process. Some of them will require an API key to get the required permissions.
  * Security event prioritization considering all different sources and external integrations that contributed to the valuation of data.



As mentioned by TechTarget, [threat intelligence](/blog/threat-intelligence-is-not-only-on-a-spectrum) is engaged at using the previously occurred various cyberattacks and threat data for giving insights into assaults as and when they occur, and even sometimes before they occur. Intelligence platforms give an extra advantage to security experts since they can swiftly monitor trends about specific threats or specific impacts that are of interest for their business. When moved into the cloud, the observation of the signals contributing to this monitoring is of course made easy with natural integration with different sources.

## SOAR (Security Orchestration, Automation and Response) in the cloud

SOAR solutions enable to respond automatically to security events. It substitutes dull, hand-operated interference from traditional security practices with smart decision to build and replies. At its heart, SOAR solutions involves automating various methods in a cybersecurity pipeline. For example, every analyst manages alerts separately, driving to flaws and discrepancies in results. With SOAR, we can reduce this inconsistency as there is an examination route for every alert, thereby keeping compatibility among analysts.

For example, potential phishing emails are regular problems encountered by companies and some of the [most recent data breaches](https://securityboulevard.com/2019/03/2018-summary-data-breaches-and-phishing-attacks-increase-in-severity/) have occurred from meticulously crafted phishing emails. A SOAR solution will be placed where it will be able to process the emails, to extract some information, to allow automatic analysis of associated artifacts, to send attached files for analysis, to get a reputation score on associated urls…

The position of the SOAR component is important as it can be seen as the brain of a security organization, receiving information, processing it and giving orders to other components. The more the company has started to move its IT into the cloud (and is subscribing to different SaaS solutions to provide additional value to its business operation) the more SOAR will make sense to be used into the cloud to interact seamlessly with other sensors and actioners.

The association SIEM-SOAR makes a lot of sense in the cloud. While data compilation is especially important, SIEM solutions often generate more alerts than SecOps units can think about replying to. In this context, specific SOAR workflows will be created to allows the security team to reduce the volume of alert they need to manage and to automate the most painful actions.

## SOC (Security Operation Center) in the cloud

[Security Operations Centers](/glossary/soc) control and analyze activity on networks, servers, endpoints, databases, applications, websites, and other systems, looking for unusual activity that could be suggestive of a security incident or compromise. The [SOC](/blog/augmented-soc-how-to-rethink-your-security-center) is responsible for ensuring that potential security incidents are correctly identified, analyzed, defended, investigated, and reported.

But like clockwork, an on-premise SOC requires continuous maintenance staff to observe alerts, staff to [customize the SIEM tools](/solutions/siem-replacement), staff to maintain security in the face of evolving threats. This complexity means on-premise SOC may not be the best fit when the company is not large enough to sustain this HR complexity.

On the other side, an outsourced SOC really simplifies the management rules. For management, it reduces the complexity of on staff handling and 24/7 clockwork and planning. For HR unit, they don’t have to worry about hiring scarce SOC analyst.

  * Basically, an outsourced SOC solves the following challenges:
  * No need to [create specific work planning](/blog/ideation-process-at-sekoia-io) out of business hours
  * No need to get all level of SOC expertise at home
  * No need to focus on tools expertise with multiple training and dedicated maintenance
  * Better proximity between detection technology (SIEM) and detection service (SOC) when the SOC is handled by same company



A “SOC in the cloud” is a managed and outsourced detection and response capability that provides immediate, actionable, and affordable security to the mid-market and companies looking for agility. It often combines a SIEM with the adapted people and adapted process needed for effective [threat detection](/blog/improving-threat-detection-with-sigma-correlations) and response. When the SIEM uses cloud infrastructure and scalable, [security-optimized architecture to allow instant deployment](/blog/how-we-made-deployments-safer-at-sekoia-io), the SOC uses it intensively to break the tradeoff between security depth, scope, and speed. It provides turnkey security expertise that IT-staff in mid-market companies sorely needs (and sometimes larger groups too). This allows to identify advanced threats that can impact their business.

## All security operations in the cloud

By default, cloud environments are out of the scope of the company. For some, they appear more susceptible to unauthorized access, data exposure, cyber attack, and other threats. Yet the same practices used to secure on-premises environments can be successfully applied to the cloud. One has also to consider a pure cloud provider is 100% committed into its security (by extension, the security of its customers) because its business relies on it.

The cloud solutions will allow to get several benefits compared with usual on-premises installations:

  * ‍**Reduced delay** : When you activate a cloud solution, you are actually creating an instance of a solution that already runs for others. That means that the software will come preconfigured and the support team is trained on the solution. [Configuration steps](/blog/enrich-your-graylog-with-sekoia-io) and on-boarding process that could take months with an internal deployment can be reduced to days or weeks with a the Software as a Service solution.**‍**
  * **Reduced cost** :In the case of cloud solution, you don’t need to worry about the infrastructure investment. Your provider is coming to the table with all the servers , the storage and other stuff to run the solution effectively without having to install any costly hardware on your system or design a complex architecture.**‍**
  * **Easier customization:** Running an on-prem solution means you can customize every aspect of your system if you want. But your team will need to spend a lot of time and energy working on it, continuous trainings will be required for the team. By contrast, a Cloud solution works with your business and provide tailored approaches as a part of their ongoing service platform or solution. That means the calibration of the solution will be made based on proved feedback coming from other customers in some way similar as you. It also means the customer will get custom dashboards almost immediately once the service is up and ready. This ability to configure the solution is made without a significant manpower investment.**‍**
  * **Better scalability** :By default, SIEM in the cloud is designed to be scalable, so it can keep up with the compliance requirements of a business. It also offers the opportunity to start with a low security price for a small business activity and to pay more progressively as the business grows.



## So, should CISOs embrace cloud security?

"Is cloud computing secure?" is usually the main question to a CISO introducing cloud security solutions. And by applying various layers of defense, cloud architecture review, rigorous contract agreement, CISO can assuredly answer: “Yes, it is secure enough to reach our expectations”.

We hear all day long about how critical automation is. But the fact remains that when it comes to security, automation is still not the rule in all circumstances. Because of the complexity of evaluating and responding to security threats, some teams still take a mostly hand-operated approach to security. Yet the reality is that manual security doesn’t work well in the cloud-native era. This is because environments move fast, configurations change too quickly, features are released daily. That makes difficult for your engineers to be able to adapt and react in a timely fashion. Security tools that can generate informed data-based decisions about threats for you and take counter-measure to stop them before they cause damage are required today. Therefore it is crucial for CISOs to consider these evolutions and prepare to embrace cloud security solutions. Hype and big bangs are not a good approach so maybe the move should be made progressively, block after block.

Gartner has predicted that by the year 2022, 50% of all SOCs will move to modern SOCs with integrated [incident response](/glossary/cert), threat intelligence, and threat hunting capabilities. Isn’t it this combination and this trend that will accelerate the switch into cloud approach for security?

In the case of cloud security, the purpose of CISO is to recognize and handle hazards. But what if the greatest hazard would be not adopting the cloud at all, but denying all the benefits it brings?

Ready to try our unified cyber defense platform? Try [Sekoia](/contact) for free!