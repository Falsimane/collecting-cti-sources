# Accessible CoAP Report – Exposed Constrained Application Protocol Services on the Internet

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/accessible-coap-report-scanning-for-exposed-constrained-application-protocol-services/
- **Date :** 2020-06-24

---

# Accessible CoAP Report – Exposed Constrained Application Protocol Services on the Internet

June 24, 2020

We have recently enabled a new daily CoAP scan and [Accessible CoAP Report](https://www.shadowserver.org/what-we-do/network-reporting/accessible-coap-report/). This is the third **IoT** related IPv4 Internet-wide scan and report implemented (after the [Open MQTT scan](https://www.shadowserver.org/what-we-do/network-reporting/open-mqtt-report/) and [Open IPP scan](https://www.shadowserver.org/what-we-do/network-reporting/open-ipp-report/)) as part of our ongoing work in the [EU CEF VARIoT project](https://variot.eu/).

The new **IoT** scan is aimed at uncovering devices that have an exposed [CoAP](https://coap.technology/) service running on port **5683/UDP**. [CoAP](https://coap.technology/) is a specialized web transfer protocol (similar to HTTP) for use with constrained nodes and constrained networks. As described in [RFC 7252](https://tools.ietf.org/html/rfc7252), CoAP is designed for use in machine-to-machine (M2M) applications such as smart energy and building automation.

#### How we scan

We scan by sending out a**21-byte CoAP CoRE Resource Discovery request** : we send a CoAP GET request for **/.well-known/core** to the default port (**5683/UDP)** on all ~4 billion routable IPv4 addresses every day. The relative URI **/.well-known/core** acts as the default entry point for requesting the list of links about resources and returns a set of links to available services from the CoAP server (if any) using the **CoRE Link Format** ([RFC 6690](https://tools.ietf.org/html/rfc6690)). We report only responses that have the CoAP response code set to 2.05 (“Content”).

#### What are the main threats associated with exposed CoAP services?

One of the main threats associated with exposed CoAP services is their possible usage as reflectors for DDoS amplification attacks (RDDoS). The **average amplification factor** of CoAP services has been quantified in the past [at around 34](https://www.netscout.com/blog/asert/coap-attacks-wild). Our average measured response size to the **21-byte payload CoRE Resource Discovery request** has been **569 bytes** (without UDP overheads), which is roughly **27 times** of the inbound request.

We also found that many of these CoAP services can leak information (including authorization credentials to services, such as wifi networks). For certain devices, in some cases, it may even be possible to issue remote instructions using CoAP.

There have also been [software vulnerabilities](https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=coap&search_type=all) in the past in CoAP implementations/libraries which could also potentially be abused for remote code execution on some of these exposed devices.

An in-depth study of CoAP (and MQTT) security considerations can be found [in a paper](https://documents.trendmicro.com/assets/white_papers/wp-the-fragility-of-industrial-IoTs-data-backbone.pdf?v1&_ga=2.29467007.1927089215.1592829165-31848736.1589537255) published by Trend Micro.

#### Scan results

**464,159** hosts responded to our IPv4 Internet-wide scan on the 21st of June 2020. By far, most of the responding services were from the Philippines, China and Russia. Together they accounted for **nearly 93%** of all the exposed instances.

![](https://www.shadowserver.org/wp-content/uploads/2020/06/Exposed-CoAP-World-Map-2020-06-21.png)

Exposed CoAP Services Around the World (21st June 2020)

![](https://www.shadowserver.org/wp-content/uploads/2020/06/Legend-Exposed-CoAP-World-Map-2020-06-21-300x115.png)

![](https://www.shadowserver.org/wp-content/uploads/2020/06/Top-Exposed-CoAP-by-Country-2020-06-21.png)

Top Countries with Exposed CoAP Services (21st June 2020)

The predominant CoAP responses returned in the Philippines and China show Qlink resources (now [rebranded](https://medium.com/qlc-chain/we-have-rebranded-into-qlc-chain-55814604756b) as [QLC Chain](https://qlcchain.org/)) a “next generation public chain for Network-as-a-Service (NaaS).” In Russia (and the Ukraine), most of the CoAP responses are from devices apparently containing [NDM Systems](https://ndmsystems.com/) embedded software (described on its website as “a smart router software company”).

#### What can be done to improve the security of the exposed instances?

We hope that the data being shared in our new accessible CoAP device report will lead to a reduction in the number of exposed CoAP-aware devices on the Internet, as well as raise awareness to the dangers of exposing such devices to unauthenticated scanners/attackers. As described in [RFC 7252](https://tools.ietf.org/html/rfc7252):  
_“CoAP itself does not provide protocol primitives for authentication or authorization; where this is required, it can either be provided by communication security (i.e., IPsec or DTLS) or by object security (within the payload)”._

While the RFC makes a number of provisions for securing CoAP (elaborating on the above), it is unclear how many of these have actually been adopted in practice. At the very least CoAP instances should therefore be either firewalled to only communicate with necessary devices and/or [DTLS (Datagram Transport Layer Security)](https://tools.ietf.org/html/rfc6347) with certificates employed where possible.

#### How can I receive the free new daily CoAP report?

Details about the **format** of the new report being shared can be found in the [new Accessible CoAP Report page](https://www.shadowserver.org/what-we-do/network-reporting/accessible-coap-report/). All existing Shadowserver report subscribers are now automatically receiving the [Accessible CoAP Report](https://www.shadowserver.org/what-we-do/network-reporting/accessible-coap-report/) if any exposed CoAP services are identified within their networks and countries (for national CSIRTs).

If you are not already a subscriber to Shadowserver’s public benefit daily network reports and would like to receive this [new Accessible CoAP report](https://www.shadowserver.org/what-we-do/network-reporting/accessible-coap-report/) and our [other existing 78 report types](https://www.shadowserver.org/what-we-do/network-reporting/), then please [sign up to our free daily public benefit network remediation feed service](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/).

You can check the latest daily CoAP scan results on [our dedicated CoAP scan page.](https://scan.shadowserver.org/coap/)

  * [DDoS](/topics/ddos/)
  * [Geo Locations](/topics/geo-locations/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Statistics](/topics/statistics/)
  * [Threat Intelligence](/topics/threat-intelligence/)



[« Back to News & Insights](/news-insights/)

### Recent Articles

  * #### [Shadowserver 2025: Highlights of the Year in Review](/news/shadowserver-2025-highlights-of-the-year-in-review/)

September 7, 2026

A review of Shadowserver’s 21st year as the world’s largest provider of free, timely, actionable, daily cyber threat… [Read more »](/news/shadowserver-2025-highlights-of-the-year-in-review/)

  * #### [Shadowserver Critical Community Infrastructure Cyber Resilience Project](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

August 5, 2026

The Shadowserver Critical Community Infrastructure (CCI) Project is designed to improve the cybersecurity posture of essential… [Read more »](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

  * #### [StealC Historical Bot Infection Special Report](/news/stealc-historical-bot-infection-special-report/)

June 25, 2026

On Wednesday 24th June 2026, international law enforcement partners announced additional successful cyber crime disruption… [Read more »](/news/stealc-historical-bot-infection-special-report/)

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)