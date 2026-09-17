# Over 380 000 open Kubernetes API servers

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/over-380-000-open-kubernetes-api-servers/
- **Date :** 2022-05-17

---

# Over 380 000 open Kubernetes API servers

May 17, 2022

### **Introduction**

We have recently started scanning for accessible [Kubernetes](https://kubernetes.io/) API instances that respond with a _200 OK HTTP_ response to our probes. Kubernetes is a popular open-source system for automating deployment, scaling, and management of containerized applications.

We find over 380 000 Kubernetes API daily that allow for some form of access, out of over 450 000 that we are able to identify. Data on these is shared daily in our [Accessible Kubernetes API Server Report](/what-we-do/network-reporting/accessible-kubernetes-api-server-report/).

While this does not mean that these instances are fully open or vulnerable to an attack, it is likely that this level of access was not intended, and these instances are an unnecessarily exposed attack surface. They also allow for information leakage on version and builds.

### **How we scan**

We scan daily with a HTTP GET request using the **/version** URI. We scan all of the IPv4 space on ports _6443_ and _443_. We include only Kubernetes servers that respond with a 200 OK (with accompanying JSON response), and hence disclose version information in their response. We do not perform any intrusive checks to determine the level of access that can be obtained.

### **Scan results**

A scan result for 2022-05-16 uncovers **381,645 unique IPs** responding with a 200 OK HTTP response to our probes. This is out of the **454,729** Kubernetes API instances we see. The “open” API instances thus constitute nearly**84%** of all instances that we can scan for on the Ipv4 Internet.

Most accessible Kubernetes API servers are found in the United States – **201,348**(nearly **53%**).

![](https://www.shadowserver.org/wp-content/uploads/2022/05/kubernetes-map-2022-05-16.png)

Accessible Kubernetes API servers by unique IP (2022-05-16)

![](https://www.shadowserver.org/wp-content/uploads/2022/05/kubernetes-chart-2022-05-16.png)

Country-level breakdown of accessible Kubernetes API servers by unique IP (2022-05-16)

**Accessible Kubernetes major/minor version breakdown:**
    
    
    1.2 4
    1.5 90
    1.6 6
    1.7 4
    1.8 53
    1.9 41
    1.10 95
    1.11 199
    1.12 497
    1.13 383
    1.14 1542
    1.15 1310
    1.16 3678
    1.17 34918
    1.18 33877
    1.19 50902
    1.20 65487
    1.21 148645
    1.22 33221
    1.23 9518
    1.24 585
    1.25 4
    

**Top accessible platforms:**
    
    
    linux/amd64 384240
    linux/arm64 683
    linux/ppc64le 134
    linux/s390x 8
    linux/arm 4
    
    

### **Mitigation**

If you are notified of an instance that is accessible, please consider implementing authorization for access or block at the firewall level to reduce your exposed attack surface.

You can read more on securing access to the Kubernetes API in this official [guide](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/).

If your Kubernetes API endpoint is available on an IP you were not expecting, and you use kube-proxy in IPVS mode see <https://github.com/kubernetes/kubernetes/pull/108460>

For more information on our scanning efforts, check out our [Internet scanning summary page.](https://www.shadowserver.org/news/the-scannings-will-continue-until-the-internet-improves/)

### **Subscribe to get free data on accessible Kubernetes instances in your network or constituency!**

Details about the format of the new report being shared can be found in the [Accessible Kubernetes API server report.](/what-we-do/network-reporting/accessible-kubernetes-api-server-report/) If you are an existing subscriber you will get the report daily should any IP be found in your network/constituency.

For a mapping of all Kubernetes API services on your network/constituency (including ones that do not allow for any form of access) check out our [Device Identification Report](/what-we-do/network-reporting/device-identification-report/).

If you are not already a subscriber to [Shadowserver’s public benefit daily network reports](/what-we-do/network-reporting/) and would like to receive this new report and our other existing report types (covering not just **other scan results** , but observations from **sinkholes, honeypots, darknets, sandboxes, blocklists and other sources**), then [please sign up to our free daily public benefit network remediation feed service](/what-we-do/network-reporting/get-reports/).

  * [ASN](/topics/asn/)
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