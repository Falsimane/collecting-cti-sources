# Exposed DICOM Servers in UK Healthcare: Patient Safety and Cybersecurity Risks

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-mri-hidden-risks-exposed-dicom-servers-uk-healthcare/
- **Date :** 2026-02-25

---

Hospitals invest heavily in physical security: Clinical areas are access-controlled, sensitive rooms are locked, and patient records are governed by strict handling procedures. Network exposure does not always receive the same level of scrutiny.

Rapid7 Labs identified more than 30 UK-based systems responding to DICOM requests over Port 104, the default port used for medical imaging traffic. These systems were reachable from the public internet at the time of observation. Project Sonar was used to confirm service responsiveness only; no attempt was made to access patient records or exploit the systems.

When Port 104 is reachable from outside trusted networks without VPN restriction or encryption, the imaging service can be detected through routine internet scanning. This type of exposure matters because protocols like DICOM were developed for use within protected clinical environments where network access is already controlled. 

Research into medical imaging infrastructure has found that when security best practices are not implemented, imaging systems and their acquisition gateways are placed on networks in ways that expose them to cybercriminal discovery. In one study of publicly accessible PACS (picture archiving and communication systems) servers, researchers reported that systems using default configurations or lacking appropriate network controls responded to internet scans and contained metadata such as patient identifiers, and the lack of basic protocol safeguards made them susceptible to data reconstruction and modification.

## Why should DICOM not be internet-facing?

DICOM, or digital imaging and communications in medicine, is the international standard used to format, store, and transmit medical imaging data. It governs both the image itself and associated metadata, which can include patient identifiers, study details, acquisition parameters, and device information. Imaging modalities such as CT scanners and MRI machines use DICOM to send studies to Picture Archiving and Communication Systems (PACS), where images are stored and later retrieved by radiologists and clinicians.

DICOM operates at the application layer. Port 104 is the traditional default port associated with DICOM services, but the protocol is not limited to that port. PACS systems and imaging services may also communicate over web ports such as 80 or 443, and in some cases expose web-based or administrative interfaces over additional ports. In our broader research, we identified more than 15 PACS devices that were externally reachable, including systems accessible over standard web ports.

⠀

![clarify-pacs-login-screen.png](https://www.rapid7.com/cdn/images/blt1933ad177a53b96f/699f23443b580eba7a24a94e/clarify-pacs-login-screen.png) _Figure 1: Clarify – PACS admin login portal._

⠀

In standard hospital deployments, DICOM services are intended to operate within segmented and trusted clinical networks. The protocol historically assumed that the surrounding network would provide access control and protection. When imaging systems or PACS services are reachable from public IP space, whether over Port 104 or web-based interfaces, they may respond to protocol negotiation or HTTP requests and disclose service-level information. In some configurations, metadata or system details can be retrieved without strong authentication controls.

That condition does not necessarily imply full access to imaging archives. It does mean that clinical infrastructure is externally discoverable and capable of interaction beyond its intended network boundary. The risk arises from that exposure, particularly when it is unintended or unmonitored.

## Exposed DICOM servers in the UK: What Rapid7 Labs found

Using [Project Sonar](/research/project-sonar/), Rapid7’s internet-wide exposure monitoring framework, we identified more than 30 UK-based healthcare systems responding to DICOM-related requests, including services associated with Port 104. The exposure was not limited to that port. Additional PACS and related healthcare systems were observed to be reachable over web ports such as 80 and 443, with more than 15 PACS devices directly accessible from public IP space.

⠀

![DICOM-medical-devices-exposed-UK-map.png](https://www.rapid7.com/cdn/images/blt74d5b3f6408e68f6/699f237fb009386b1a8334c4/DICOM-medical-devices-exposed-UK-map.png) _Figure 2: UK-based exposed Healthcare systems to the Internet._

⠀

This methodology does not exploit systems or access patient records. It confirms whether a service is reachable and actively responding.

For healthcare organizations navigating increased regulatory scrutiny and rising cyber threats, this kind of medical device exposure is unnecessary risk.

## The cybersecurity risks of exposed medical imaging systems

When a DICOM server is exposed to the internet, and the risk extends beyond technical misconfiguration, it introduces three primary threat categories:

### Patient data exposure and healthcare identity theft

DICOM files typically contain structured metadata fields, which may include:

  * Patient name.

  * Date of birth.

  * Study identifiers.

  * Referring clinician information.




If a system allows metadata queries without authentication or encryption, those identifiers may be retrievable. Healthcare data retains long-term value because it cannot be reissued in the way payment credentials can.

### Medical image manipulation and clinical integrity risks

Imaging workflows depend on trusted transmission between modalities, PACS servers, and diagnostic workstations. Research has shown that medical images can be altered using machine learning techniques under controlled conditions. 

Exploitation requires access and technical capability, but exposure beyond intended network boundaries increases the potential attack surface. Clinical confidence depends on assurance that imaging data has not been modified in transit.

### Ransomware entry points via PACS and imaging systems

Medical imaging systems like DICOM connect to PACS servers. If an exposed DICOM service provides a foothold, attackers may attempt lateral movement inside the network.

An exposed PACS server can quickly become operational ground zero - delaying procedures, disrupting diagnostics, and impacting patient care. As healthcare continues to face ransomware targeting across the UK and EU, edge systems and externally visible services are often initial access points.

## UK healthcare attack surface exposure: DICOM is part of a wider pattern

The exposure of 30+ DICOM systems is concerning. But it is not isolated. A broader review of UK healthcare-associated IP space shows externally visible infrastructure including:

  * Cisco edge devices.

  * BigIP appliances.

  * Check Point firewalls.

  * Citrix NetScaler instances.

  * Ivanti Endpoint Manager Mobile.

  * SSL VPN portals.




**Search for NHS registered names and filter on UK/GB:**

**System Tech**| **Count**  
---|---  
[ ciscoSystems](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22ciscoSystems%22)| 153  
[BigIP](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22BigIP%22)| 36  
[Check Point Firewall](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Check+Point+Firewall%22)| 30  
[Check Point SVN foundation httpd](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Check+Point+SVN+foundation+httpd%22)| 26  
[Cisco ASA SSL VPN](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Cisco+ASA+SSL+VPN%22)| 6  
[Connectra Check Point Web Security httpd](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Connectra+Check+Point+Web+Security+httpd%22)| 6  
[Citrix Netscaler](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Citrix+Netscaler%22)| 4  
[Ivanti Endpoint Manager Mobile (EPMM)](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Ivanti+Endpoint+Manager+Mobile+%28EPMM%29%22)| 4  
[Cisco IOS http config](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Cisco+IOS+http+config%22)| 2  
[Fortinet FortiGate](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Fortinet+FortiGate%22)| 1  
[Fortinet FortiGate-100E](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Fortinet+FortiGate-100E%22)| 1  
[Fortinet FortiGate-40F](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Fortinet+FortiGate-40F%22)| 1  
[SonicWall](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22SonicWall%22)| 1  
[Sophos SSL VPN User Portal](https://www.shodan.io/search?query=country%3A%22GB%22+org%3A%22NHS%22+product%3A%22Sophos+SSL+VPN+User+Portal%22)| 1  
  
 _Table 1:__Externally visible technologies identified across UK healthcare-associated IP space._

⠀

These technologies are standard components of modern IT environments. The concern arises when exposure is unintended, unmonitored, or paired with delayed remediation. Public reporting in 2025 shows that ransomware groups continue to target healthcare following disclosure of vulnerabilities in edge appliances and remote access technologies. In several documented cases, exploitation occurred within days of vulnerability publication.

When more than 30 imaging systems are externally reachable, the underlying issue is unlikely to be a single isolated configuration error. It suggests incomplete visibility into which services are accessible from outside the organisation at any given moment.

⠀

![NHS-product-trends-over-time-graph.png](https://www.rapid7.com/cdn/images/blt80dd00001c6429e8/699f250da2156840331096fb/NHS-product-trends-over-time-graph.png) _Figure 3: Visibility of selected healthcare technologies over time._

## External asset visibility and healthcare IT complexity 

Healthcare IT environments evolve incrementally, with legacy protocols remaining operational because imaging equipment has long service lifecycles. This slow evolution can cause complications like: 

  * Vendor default configurations are often inherited from initial deployment. 

  * Third-party integrations extending network connectivity beyond hospital campuses.

  * Broad remote access supporting distributed clinical teams. 

  * Cloud services introducing additional infrastructure layers that may not be consistently mapped alongside on-premise systems.




⠀

![UK-DICOM-top-ransomware-groups-graph.png](https://www.rapid7.com/cdn/images/blt11a93509d5eadc6f/699f261e56ca115149bb5704/UK-DICOM-top-ransomware-groups-graph.png) _Figure 4: Ransomware groups observed targeting UK/EU healthcare in 2025._

⠀

![UK-DICOM-monthly-ransomware-activity-graph.png](https://www.rapid7.com/cdn/images/blt138272a2aa980cdf/699f261e883c6379c54d848f/UK-DICOM-monthly-ransomware-activity-graph.png) _Figure 5: Ransomware group activity observed around UK/EU healthcare in 2025._

Within this context, continuous external visibility becomes challenging. Many organisations do not maintain a real-time inventory of internet-facing services across all owned IP ranges. And so, without deliberate intent, a DICOM server or medical device can become externally reachable., Until specifically identified, the exposure can persist. The lesson?Infrastructure designed for ease of deployment can accumulate risk when oversight is periodic rather than continuous.

## How to reduce DICOM and medical device exposure

As ransomware groups accelerate and exploitation windows shrink, it would be easy to frame exposure as oversight. But that diagnosis would miss the point.

The issue is not a lack of cybersecurity awareness within the NHS. It is the structural complexity of modern healthcare IT environments, with legacy protocols continuing to operate alongside newer systems. 

  * Vendor-default configurations are often inherited rather than re-architected. 

  * Third-party integrations expand the digital perimeter beyond the hospital campus. 

  * Remote access services enable flexible care delivery, while cloud adoption accelerates faster than traditional governance models can adapt.




In this kind of environment, many organizations lack continuous visibility into which services are externally exposed at any given moment. If you do not know a medical device or DICOM server is accessible from the internet, you cannot secure it. What was once ‘plug and play’ infrastructure can quietly become ‘plug and prey’.

## Securing DICOM servers in healthcare

Organizations reviewing imaging system security should confirm whether Port 104 is accessible from outside trusted networks. Where external access is operationally required, it should be restricted through VPN controls and strong authentication. DICOM traffic should be encrypted where supported.

Additional steps include:

  * Reviewing firewall rules governing PACS and modality communication.

  * Conducting periodic external service discovery across owned IP ranges.

  * Verifying vendor default configurations during deployment and upgrade cycles.

  * Monitoring newly exposed services following infrastructure or cloud changes.




These measures focus on aligning network exposure with clinical intent. The objective is straightforward: Ensure that imaging systems are reachable only by the parties that need them.

## Healthcare cyber resilience starts with visibility

Imaging systems play a central role in diagnosis and care planning, with operational disruption creating immediate clinical consequences.. As regulatory scrutiny of healthcare cybersecurity continues to increase, confirming that DICOM services operate within intended network boundaries is a practical and measurable step toward reducing risk.

The identification of more than 30 exposed systems highlights a visibility gap rather than a failure of awareness. Addressing that gap begins with systematic review of external-facing infrastructure and sustained monitoring over time.

## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)
  * [Healthcare Security](/blog/tag/healthcare/)