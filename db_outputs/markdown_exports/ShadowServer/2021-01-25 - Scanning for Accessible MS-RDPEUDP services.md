# Scanning for Accessible MS-RDPEUDP services

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/scanning-for-accessible-ms-rdpeudp-services/
- **Date :** 2021-01-25

---

# Scanning for Accessible MS-RDPEUDP services

January 25, 2021

Last week we enabled a new IPv4 Internet-wide scan for accessible [Microsoft RDPEUDP ](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpeudp/2744a3ee-04fb-407b-a9e3-b3b2ded422b1) services on **port 3389/UDP**. This **UDP service** is an extension to the classic Microsoft Remote Desktop Protocol service ([RDP](https://docs.microsoft.com/en-us/troubleshoot/windows-server/remote/understanding-remote-desktop-protocol)) over TCP on port 3389.

We scan by sending a 16 byte RDP UDP connection request to port 3389/UDP. Our scan results in around**12 000 unique IPv4 addresses on a given day responding**. We report our findings daily in a new [Accessible MS-RDPEUDP report](/what-we-do/network-reporting/accessible-ms-rdpeudp/) as part of our free daily remediation feeds.

RDP as a remote access service has long had a number of security risks associated with it, which includes weak credentials being brute-forced by attackers to gain remote access as well as past vulnerabilities such as Bluekeep ([CVE-2019-0708](https://nvd.nist.gov/vuln/detail/CVE-2019-0708)) that allow for remote code execution by unauthenticated attackers.

The number of exposed RDP-UDP services is much _lower_ than for RDP-TCP which currently has over [3.5M distinct IPs](https://scan.shadowserver.org/rdp/) responding daily.

However, as a UDP service, the RDP-UDP extension can in addition **be abused to perform reflected amplification DDoS attacks**. A response to a RDP-UDP connection request with a spoofed IP source address is amplified **around 28 times** , with the protocol allowing for 3 such responses, for a [total amplification factor of over 84 times](https://github.com/Phenomite/AMP-Research/tree/master/Port%203389%20-%20RDP).

As of January 2021, exposed MS-RDPEUDP services are being [actively abused for amplification DDoS attacks](https://www.netscout.com/blog/asert/microsoft-remote-desktop-protocol-rdp-reflectionamplification).

The country breakdown of accessible RDPEUDP services that responded to our request probe on the 20th of January 2021 **(around 12 000 IPv4 addresses)** is shown below. As can be seen, nearly a half of all exposed services are found in the United States and China.

![](https://www.shadowserver.org/wp-content/uploads/2021/01/Accessible_MSRDPEUDP_2021-01-20.png)

Exposed MS RDPEUDP services (port 3389/UDP) around the world (20th January 2021)

![](https://www.shadowserver.org/wp-content/uploads/2021/01/Accessible_MSRDPEUDP_2021-01-20-Legend-300x111.png)

![](https://www.shadowserver.org/wp-content/uploads/2021/01/Accessible_MS-RDPEUDP_treemap-2021-01-20.png)

Top Countries with exposed MS-RDPEUDP services (20th January 2021)

Details about the format of the new report being shared can be found in the new [Accessible MS-RDPEUDP Report](/what-we-do/network-reporting/accessible-ms-rdpeudp/) page. All existing Shadowserver report subscribers are now automatically receiving the [Accessible MS-RDPEUDP Report](/what-we-do/network-reporting/accessible-ms-rdpeudp/) if any exposed MS-RDPEUDP services are identified within their networks and countries (for national CSIRTs).

To avoid being abused for reflected DDoS attacks, network owners should revert to RDP-TCP services unless UDP support is explicitly required. As suggested [in the detailed research here](https://github.com/Phenomite/AMP-Research/tree/master/Port%203389%20-%20RDP), it is [also possible](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdpeudp/aea14a52-baa1-4486-bcd8-f30505ec707d) to select a RDP-UDP-L Mode (“Best-Efforts”) for the service instead of the default RDP-UDP-R Mode (“Reliable”), which stops the protocol from re-transmitting packets, and hence lowers the amplification factor.

Network owners exposing RDP services should consider if exposing them to the wider Internet is absolutely necessary and firewall where possible or protect these services behind VPNs. RDP services should use 2FA mechanisms for authentication. Further security considerations can be found [here](https://www.cloudflare.com/learning/access-management/rdp-security-risks/).

For additional insight into the complexities of the RDP protocol, check out this blog on [analyzing encrypted RDP connections](https://corelight.blog/2020/05/13/analyzing-encrypted-rdp-connections/).

If you are not already a subscriber to Shadowserver’s public benefit daily network reports and would like to receive this new report and our [other existing report types](https://www.shadowserver.org/what-we-do/network-reporting/) (covering not just other scan results, but also many observations from sinkholes, honeypots, darknets and sandboxes), then [please sign up to our free daily public benefit network remediation feed service.](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/)

  * [ASN](/topics/asn/)
  * [DDoS](/topics/ddos/)
  * [Geo Locations](/topics/geo-locations/)
  * [Reports](/topics/reports/)
  * [Scans](/topics/scans/)
  * [Shadowserver](/topics/shadowserver/)
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