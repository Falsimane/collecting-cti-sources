# Guidelines for selecting and disseminating Sekoia IOCs from CTI sources

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/guidelines-for-selecting-and-disseminating-sekoia-io-iocs-from-cti-sources
- **Date :** 2024-03-07

---

In the ever-evolving landscape of cybersecurity, the battle against threats demands a multi-faceted approach. Organizations, now more than ever, need to leverage comprehensive Threat Intelligence to stay ahead of adversaries. At the forefront of this defense is Sekoia, a leading cybersecurity vendor offering a cutting-edge CTI platform (Cyber Threat Intelligence).

Sekoia relies on one of the most experienced teams of CTI researchers in Europe and has built capabilities to produce comprehensive intelligence covering the global cyber threat, from a strategic to a technical perspective.

This work is conducted by our Threat Detection & Research team (TDR) composed of CTI researchers and analysts working full-time on CTI production. TDR includes former members of governmental agencies, military and major private organizations.

TDR team is committed to producing exclusive intelligence. To do so, TDR has curated a dynamic ecosystem that combines its proprietary intelligence with curated and contextualized third-party OSINT (Open-Source Intelligence) sources, ensuring a holistic and informed information management strategy.

When it comes to the quality of our intelligence, there is no doubt, the numbers speak for themselves: In 2023,Sekoia revoked only 223 IoCs over a total of around 3 millions, which corresponds to a revocation rate of 0,01%.

This article will help you understand the process of manipulating your CTI, especially the diverse data sources present within the Sekoia SOC platform.

For starters, let’s investigate the main data sources leveraged by the platform and find out how they relate to your dissemination use cases.

## **Volume and typology of IOCs from our TOP-10 CTI sources**

Overall, **Sekoia’s intelligence is derived from more than 400 sources and encompasses more than 8 million indicators of compromise**. Many of these sources reflect exclusive Sekoia capabilities; some are third-party sources.

Regarding third-party sources, Sekoia analysts conduct extensive qualification and contextualization of intelligence. The gathering of data is aligned with the strategic objectives of our intelligence. Pieces of data coming from a third-party source are carefully integrated to fit the existing intelligence database.

The following table displays the number and types of IoCs produced in 2023, coming from our top sources:

Source| # of IOCs in 2023| IOCs breakdown  
---|---|---  
Sekoia exclusive sources| 763 775| 47% file hashes21% URLs17% domains13% IPs  
tria[.]ge| 403 831| 90% file hashes4% IPs3% URLs3% domains  
PhishTank| 102 787| 100% URLs  
ThreatFox| 93 184| 47% URLs36% IPs15% domains1% file hashes  
MalwareBazaar| 80 206| 100% file hashes  
URLhaus| 26 966| 100% URLs  
phishunt[.]io| 8 806| 100% URLs  
Total 2023 (for these 10 sources)| 1 479 555| 55% file hashes24% URLs11% domains10% IPs  
  
Categories of IOCs coming from our TOP-10 sources in 2023 (jan.-dec.) 

The following tables present, by category of IoC, the sources that have provided the most of these IoCs types, in 2023. They can help you understand which sources generate specific IoCs and guide you in selecting sources for your dissemination use cases.

Source| # of IP addresses in 2023  
---|---  
Sekoia exclusive sources| 101 705  
ThreatFox| 33 992  
tria[.]ge| 16 035  
  
Source| # of domains in 2023  
---|---  
Sekoia exclusive sources| 132 656  
ThreatFox| 13 724  
tria[.]ge| 12 924  
  
Source| # of URLs in 2023  
---|---  
Sekoia exclusive sources| 164 647  
PhishTank| 102 787  
ThreatFox| 44 209  
URLhaus| 26 966  
tria[.]ge| 13 284  
phishunt[.]io| 8 806  
  
Source| # of file hashes in 2023  
---|---  
Sekoia exclusive sources| 363 957  
tria[.]ge| 361 449  
MalwareBazaar| 80 206  
Sekoia[.]io| 16 044  
ThreatFox| 1 240  
  
Repartition of the categories of IOCs coming from our TOP-10 sources in 2023 (jan.-dec.) 

## **Disseminating Sekoia intelligence**

Sekoia strives to offer CTI that fully supports the operational objectives of security teams. The intelligence is designed to enhance detection and hunting capabilities. Therefore, Sekoia relies on time-tested [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html) standards for CTI modeling. These standards are developed by the OASIS foundation (Sekoia is a [member of the OASIS foundation](https://www.oasis-open.org/members/)). 

STIX is the language analysts use to exchange their data transparently and enable its use in vendor-agnostic security systems. At Sekoia, we believe STIX is the best way to offer interoperable intelligence consolidated in a single database.

Disseminating data to your security solutions is key to leveraging the benefits of Sekoia CTI. We offer different methods you can use. Please check [our public documentation](https://docs.sekoia.com/cti/features/integrations/) for more information on CTI dissemination and available APIs.

### **How to choose the method to disseminate CTI**

There are three main methods you can use to operate the dissemination. Please note that the methods are only briefly described, and you can contact your Sekoia representative for more information.

  * **Method 1** : Using one of the native connectors available for the following solutions: OpenCTI, MISP, Anomali ThreatStream, ThreatQuotient, Cortex Analyzer, Microsoft Sentinel, Splunk, Cortex XSOAR, etc.
  * **Method 2** : Using our TAXII 2.1 server (standard protocol for sharing STIX 2.1-modeled CTI bundles) to consume our intelligence, filtered or not. You can find more information in [this documentation.](https://docs.sekoia.com/cti/features/integrations/taxii/)
  * **Method 3** : Using our APIs directly to consume the intelligence ofSekoia under various formats and filters or with different inputs and parameters for your requests. 



_Using Method 2 or 3 might require you to build a script that will query our APIs, consume our intelligence, and organize its dissemination in your equipment. An example of such a Python script can be found_[ _on this page_](https://docs.sekoia.com/cti/features/integrations/api/) _._

Keep in mind that there is a specific API that allows you to consume raw lists of a given category of indicators returned in a CSV file. This API enables you to access raw lists of IPV4, IPV6, or domain names (with no associated context) that can be useful in some scenarios–for example, using network IOCs for a firewall blocklist.

It’s also important to note another benefit for customers using our platform: IOCs coming from the CTI are **automatically** leveraged for detection on the logs sent to the SOC platform. 

## **Disseminating filtered intelligence to your security solutions**

Sometimes, you might need to consume only a restricted list of IOCs from Sekoia CTI instead of the millions of objects in the database.

Whereas method 1 (native connectors) will generally not include filtering capabilities, methods 2 and 3 (TAXII server or APIs) will provide many options for consuming the intelligence with filters.

Filtering can be done on the sources of the IOCs to select only a subset of IOCs coming from some specific sources (see more details on source selection in the next section).

Our “feed” feature will allow you to use filtering within our SOC platform. Once you have created your feed, you can use the API or TAXII URL to consume the intelligence and access the required IOCs.

With these feeds, you can :

  * Filter on specific sources you want to disseminate
  * Filter on specific IOC types you want to disseminate
  * Choose the format returned by the API (JSON, CSV, etc.)
  * Introduce incremental updates (by using a script to consume the API associated with your feed)



**Sekoia CTI is fully contextualized, and all the objects are linked. However, filtering on specific types of IOCs or sources might cause this contextualization to be lost. Other methods should be used if your use case requires disseminating IOCs and their context.**

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5cf69291914889b1cd0_6a92a2e8db65986262adf8a2_6a2a7d15b7c63a873a29e581.webp)

Our feed functionality relies on one of our APIs that is documented here. This API allows consuming the objects (IOCs, malware, etc.) selected on a feed.

By default, when using this API (directly or through a feed), it will include expired and revoked indicators.

If you need to consume only valid indicators, you can query this API. However, you will need to change the parameters of your request to exclude expired and revoked indicators:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5cf69291914889b1cd3_6a92a2e9a2f46752fd015ae5_6a2a7d15b7c63a873a29e566.webp)

If you need to consume all theSekoia CTI with relationship links between CTI objects, our “default feed” will be useful here. This feed is suitable for any subscription and includes all the objects presented in the Sekoia CTI database, including relationships.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5cf69291914889b1ccd_6a92a2e64b4041c6934269fd_6a2a7d15b7c63a873a29e563.webp)

The consumption of this “default feed” can also be adjusted to include or exclude revoked and expired objects.

As you can see, Sekoia allows you to filter the intelligence you want to disseminate based on different criteria. For example, you can decide to disseminate only specific types of IOCs or IOCs coming from particular sources.

As this article intends to provide insights into our top IOC sources, we will present suggestions for disseminating IOCs from specific sources to specific security equipment.

## **Disseminating intelligence coming from specific sources**

If you want to disseminate IOCs coming from specific sources, you can use our “feed” functionality and select the required “observables types” and “sources” in the feed configuration. You can then consume this “feed” through an API or a TAXII URL.

### **Important considerations**

  * The following only represents suggestions to illustrate how you can organize your IOCs dissemination.
  * The selection of sources presented below represents only suggestions, not guidelines.
  * Consider filtering on specific sources only if you have specific constraints on costs, volume, etc.
  * When selecting IOCs from specific sources, you might lose the native contextualization provided by Sekoia on these IOCs.



Keep in mind that the Sekoia Defend Plan (Sekoia XDR capabilities) includes native leverage of the Sekoia CTI: real-time IOC detection, retrohunt, contextualization of security operations, and much more.

## **Disseminating IOCs from specific sources to a SIEM**

A common use case foresees leveraging IOCs to feed SIEM and enhance or expand its detection capabilities. Sekoia intelligence will allow you to add quantities of IOCs to your SIEM.

Due to specific limitations or constraints related to costs or resources, you might need to limit the volume of IOCs you are disseminating to your SIEM. In such a scenario, you will need to proceed to arbitrage within the intelligence you will disseminate to your SIEM.

Since SIEMs are used for correlation and aggregation of security events coming from diverse sources, providing strict guidelines on which types of IOCs shall be used would be irrelevant.

A good practice could be to select a relevant panel of IOCs that align with the organization's threat landscape, security context, and SIEM configuration. However, SIEMs are used to monitor network and endpoint activities and will then require a variety of IOCs to enhance detection capabilities.

On a SIEM, where analysts conduct security investigations, you might want to use contextualized IOCs (attached to malware, for example). If so, please consider other solutions to consume our IOCs instead of source-based filtering. For instance, you can use native connectors or the default feed.

**Possible types and associated sources of IOCs to use**

  * Recommended 
    * IPs (Sekoia C2 Tracker, ThreatFox, Tria.ge, Sekoia Malware Watcher, Sekoia)
    * Domain names (Sekoia C2 tracker, ThreatFox, Tria.ge, Sekoia)
    * URLs (Sekoia C2 Tracker, PhishTank, ThreatFox)
    * File hashes (Tria.ge, Sekoia YARA Tracker, Sekoia Malware Watcher)



## **Disseminating IOCs from specific sources to a Firewall**

When disseminating IOCs to firewalls, it's essential to focus on network IOCs: IP addresses, URLs, and domain names. Consider the criticality of assets and networks, directing attention to high-value targets. Some firewalls might include URLs and DNS traffic, so consider that before choosing which IOCs you will disseminate.

Sekoia IOCs will enhance your network rules based on your security network policies to allow or block specific network activity.

Furthermore, you must ensure that the IOCs you are using are regularly updated and reassessed to stay ahead of evolving threats. In that sense, make sure that your dissemination methods include regular updates of IOC lists. Automation is vital in supporting that objective.

Methods to disseminate IOCs to firewalls depend on your firewall capabilities and how it is designed to consume IOCs. A solid option is to build a simple Python script that will fetch Sekoia CTI and organize the export of retrieved IOCs to your blacklists or whitelists.

Disseminating the CTI context is generally irrelevant in firewalls since you will only use IOCs to enforce your network rules and conduct basic allow or deny actions.

**Possible types and associated sources of IOCs to use**

  * Recommended 
    * IPs (Sekoia C2 Tracker, ThreatFox, Tria.ge, Sekoia Malware Watcher, Sekoia)
  * Optional (depending on your detection strategy) 
    * Domain names (Sekoia C2 tracker, ThreatFox, Tria.ge, Sekoia)
    * URLs (Sekoia C2 Tracker, PhishTank, ThreatFox)



## **Disseminating IOCs from specific sources to an EDR**

For Endpoint Detection and Response (EDR) systems, the selection and dissemination of IOCs should be tailored to the unique characteristics of endpoint security.

You will need to prioritize file hashes, malicious URLs, and domain names most relevant to potential endpoint threats. Also, choose IOCs that are indicative of advanced persistent threats, malware, or suspicious activities that may manifest on individual devices.

Then, integrate IOCs into the EDR solution, configuring it to alert, block, or quarantine as necessary. Consider the diverse nature of endpoints within your organization, ensuring that selected IOCs are applicable to the various devices and operating systems in use.

To adapt to the changing threat landscape, you will need to regularly update EDR policies and IOCs. Customizing IOC feeds and refining them continuously based on the organization's specific requirements contribute to an effective and adaptive endpoint security strategy.

**Possible types and associated sources of IOCs to use**

  * Recommended 
    * File hashes (Tria.ge, Sekoia YARA Tracker, Sekoia Malware Watcher)
  * Optional (depending on your detection strategy) 
    * URLs (Sekoia C2 Tracker, PhishTank)
    * Domain names (Sekoia C2 Tracker, ThreatFox)
    * IPs (Sekoia C2 Tracker, ThreatFox)



## **Conclusion**

Sekoia SOC platform allows you to access top-notch threat intelligence to cover and mitigate threats. This intelligence needs to be leveraged and operationalized in your security systems.

Sekoia offers many options to perform this operationalization, and one of the options is to disseminate IOCs coming from specific intelligence sources.