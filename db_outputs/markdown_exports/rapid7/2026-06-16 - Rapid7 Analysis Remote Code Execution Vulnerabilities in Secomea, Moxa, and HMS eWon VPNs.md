# Rapid7 Analysis: Remote Code Execution Vulnerabilities in Secomea, Moxa, and HMS eWon VPNs

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/ra-remote-code-execution-vulnerabilities-in-secomea-moxa-and-hms-ewon-vpns-analysis/
- **Date :** 2026-06-16

---

On Wednesday, July 29, security firm Claroty [published details](https://www.claroty.com/2020/07/28/vpn-security-flaws/) on multiple remote code execution (RCE) vulnerabilities affecting VPN implementations primarily used in industrial control system (ICS) and operational technology (OT) networks. Claroty’s research includes six separate CVEs affecting Secomea, Moxa, and HMS eWon industrial VPNs. Successful exploitation may result in a remote, unauthenticated attacker gaining direct access to critical systems and field devices, including programmable logic controllers (PLCs) and input/output (IO) devices.

Rapid7 Labs has details on public-facing attack surface area [here](https://blog.rapid7.com/2020/07/29/remote-code-execution-risks-in-secomea-moxa-and-hms-ewon-ics-vpn-vulnerabilities-what-you-need-to-know/).

### Affected products

  * Secomea GateManager (CVE-2020-14500, CVE-2020-14508, CVE-2020-14510, CVE-2020-14512)
  * Moxa EDR-G902/3 industrial VPN servers (CVE-2020-14511)
  * HMS Networks eCatcher VPN clients (CVE-2020-14498)



### Secomea GateManager unauthenticated RCE

The most severe of the four flaws affecting Secomea products is CVE-2020-14500, a critical remote code execution vulnerability in the GateManager component of Secomea remote access servers that results from improper handling of client-provided HTTP request headers. Successful exploitation may allow remote attackers full access to a Secomea customer’s internal network, including the ability to decrypt all traffic that passes through the VPN. CVE-2020-14500 carries a CVSSv3 base score of 10.0.

Secomea released a [patch](https://kb.secomea.com/helpdesk/KB/View/25546482-downloads-gatemanager) on July 10, 2020. CISA has a detailed advisory here: https://us-cert.cisa.gov/ics/advisories/icsa-20-210-01

### Moxa EDR-G902/3 industrial VPN servers unauthenticated RCE

CVE-2020-14511 is a stack-based overflow vulnerability in the web server component of Moxa VPN routers that results from the web server’s failure to verify the length of user-supplied HTTP cookies. Successful exploitation may allow an unauthenticated attacker to remotely execute code on affected devices by sending it a maliciously crafted HTTP request. CVE-2020-14511 carries a CVSSv3 base score of 9.8. Claroty [published separate details on the vulnerability](https://www.claroty.com/2020/07/15/cve-2020-14511/) earlier in July.

Moxa published their [advisory](https://www.moxa.com/en/support/support/security-advisory/edr-g902-g903-series-secure-routers-vulnerabilities) on July 16, which links to patches for their [EDR-G902](https://www.moxa.com/en/support/product-support/software-and-documentation/search?psid=48053) and [EDR-G903](https://www.moxa.com/en/support/product-support/software-and-documentation/search?psid=48063) series routers. CISA has published ICS advisory [ICSA-20-196-02](https://us-cert.cisa.gov/ics/advisories/icsa-20-196-02) for CVE-2020-14511.

### HMS Networks eCatcher VPN client RCE

CVE-2020-14498 is a vulnerability in VPN _client_ software, in contrast to the server-side vulnerabilities described above. It can be triggered by enticing a user with the VPN client installed to visit a malicious or compromised website, or to open an email that contains malicious HTML. Successful exploitation may allow a remote attacker to execute arbitrary code on an affected system, including gaining access to the user’s VPN credentials. These credentials may then be used to further compromise the network. CVE-2020-14498 carries a base CVSSv3 score of 9.6 and affects all versions of the eCatcher VPN client prior to 6.5.5.

HMS has a security advisory available [here](https://cdn.hms-networks.com/docs/librariesprovider6/cybersecurity/hms-security-advisory-2020-07-15-001---ewon-ecatcher.pdf?sfvrsn=c0ab32d7_4) which links to their [downloads page](https://ewon.biz/technical-support/pages/all-downloads) with the patched software. CISA has published ICS advisory [ICSA-20-210-03](https://us-cert.cisa.gov/ics/advisories/icsa-20-210-03) for CVE-2020-14498.

### Rapid7 Analysis

Organizations should be prepared to see an increase in potentially critical attacks against ICS and OT networks. Remote code execution vulnerabilities in internet-exposed VPN implementations like Secomea’s GateManager component and Moxa’s VPN server are a boon to well-resourced adversaries and should take extremely high priority for systems operators and administrators in the OT and ICS spaces. Successful attacks on either gateway component yield high-privileged access for adversaries, with the potential for physical damage to PLCs or field devices. While sophisticated threat actors may not necessarily seek to cause attention-grabbing noise or damage as a matter of course, we expect that the combination of a high-value but relatively small target population and the news coverage accompanying these vulnerabilities will mean an increased volume of opportunistic scanning and attacks.

In addition to the exploitation opportunities explicitly called out in vulnerability details, we expect increased scrutiny from both advanced and commodity threat actors, which may in turn lead to new attack vectors or other low-hanging opportunities for exploitation in the affected products. For instance, Rapid7 Labs has observed roughly 1,900 Moxa VPN gateways exposing their Telnet administration port to the internet— most of which provide version, MAC address, and other configuration information, and a small percentage of which do not require passwords to completely access or reconfigure the systems. Rapid7 has [in-depth information on internet exposure here](https://blog.rapid7.com/2020/07/29/remote-code-execution-risks-in-secomea-moxa-and-hms-ewon-ics-vpn-vulnerabilities-what-you-need-to-know/).

### Guidance

Network segmentation is a commonly recommended best practice for high criticality environments, including OT and ICS networks; these VPN flaws seriously weaken the benefits provided by isolating the devices. Bringing operational remote access devices down for unscheduled maintenance can be difficult and may cause outages that are disruptive to operations. Bearing the severity of these vulnerabilities in mind, emergency action is likely warranted depending on the fault tolerance, mitigating controls, and availability requirements of individual organizational deployments and risk models. Rapid7 emphasizes the importance and urgency of patching these vulnerabilities. Further guidance for OT and ICS teams that may not be able to immediately patch is below.

Remediation of the vulnerability is the goal but utilizing mitigating controls can be an effective step if leveraging a patching and testing procedure is not possible in the short term. Time is of extreme essence for any vulnerability exposed via a public network where remote code execution and default credentials are involved. To manage any emerging threat situation like this, there are a series of steps operators should consider taking very quickly, some of which are outlined here.

  * Stand up a triage team to act as the central source of truth and coordination and to facilitate rapid, informed decision-making.
  * Treat your response like a cyber incident—especially if you do not know if the vulnerability has already been exploited. In addition to the cybersecurity team, your response should ideally include subject matter experts from: Emergency Services (Emergency Operations Center), Operations and systems/security/network operations center, Impacted business unit(s), Compliance/Regulatory, Legal, External Affairs/Communications, Information Technology.
  * Connect with your respective ISAC(s). This will create the dialogue needed to build regulatory safeguards around availability and fault tolerance considerations.
  * Where necessary, involve your regulatory entity, regional authority, and independent system operator. Get their formal opinion on steps and procedures to take. Get their buy-in to move forward on taking down access especially for covered assets.
  * Capture the inventory of all affected devices. For those regulated by NERC CIP, this should be a lighter lift.
  * Identifying the devices that are connected to the SIS and environmental monitoring systems would be a critical priority. This could leave an opening to overriding safety and.or environmental controls potentially creating kinetic third and fourth tier effects.
  * Monitor traffic to those devices. Through baselining, the Operations Control Center as well as Security Operations Center will be able to identify any anomalous traffic and report it.
  * Leverage your organization’s Emergency Operations team to decide when and how to take action. Firmware updates may need to be tested per specific regulations before deployment, so consider alternate approaches such as hardware replacement and fail-over.
  * Communication flow is essential within an emergency action like this. Defining timelines, reporting, and milestones for progress will help increase the success of the remediation and keep accountability for all teams involved.



## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)
  * [Rapid7 Analysis](/blog/tag/rapid7-analysis/)