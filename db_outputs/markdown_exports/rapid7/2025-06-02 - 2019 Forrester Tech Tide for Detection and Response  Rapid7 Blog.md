# 2019 Forrester Tech Tide for Detection and Response | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/03/14/forrester-tech-tide-for-detection-and-response-is-2019-the-year-of-convergence/
- **Date :** 2025-06-02

---

If you’ve been researching threat detection and response solutions, try not to be blinded by the dazzling array of vendors, analytics, and claims raiding your inboxes and phones. It feels like there’s an offering for each segment of your network—get this for your endpoints, get that for log management, layer this module for better analytics, and oh, definitely get this to secure your cloud services and infrastructure.

To help make sense of this ever-changing landscape, Forrester analysts Josh Zelonis and Joseph Blankenship co-authored a new report, “The Forrester Tech Tide™: Zero Trust Threat Detection and Response, Q1 2019.”.

![Maturity.png](https://www.rapid7.com/cdn/images/blt7e1d883b7fd47dfe/683de42818a5532f3c68715c/Maturity.png)

The report covers 18 (!) different technologies and highlights what each technology does, where it’s going, and which vendors represent it. As shown above, each technology is categorized by level of business value, as well as its maturity. For example, many readers are familiar with the mature space of intrusion detection and prevention systems (IDS/IPS). Forrester recommends a divest, noting, “With the decreasing emphasis on detection at the network gateway, the majority of security teams prefer to replace these legacy devices with next-generation firewalls (NGFWs).”

As for how Rapid7 maps to this matrix, we are proud to note that we were recognized for capabilities spanning the five following categories:

Security user behavior analytics (SUBA)  
Security analytics (SA)  
[Deception technology](/solutions/deception-technology/)  
[Security automation and orchestration (SAO)](/solutions/security-orchestration-and-automation/)  
[File integrity monitoring (FIM)](/solutions/file-integrity-monitoring/)

We believe this is because our approach focuses on outcomes, not on defined technology categories. Our cloud security analytics solution, InsightIDR, makes it easy to do these three things:

  1. Unify security data, wherever it is
  2. Detect common and targeted threats
  3. Respond with the best action, both when stopping threats and reporting on progress



In this post, let’s take a quick trip back in time to review the evolution of InsightIDR:

### 1\. Pioneering security user behavior analytics (SUBA)

The year was 2013. Our penetration testing services team advised that persistent, undetected access continued to come from stealing a user’s credentials and impersonating them. The Verizon Data Breach Investigations Report began to list the use of stolen credentials as the top attack vector behind confirmed breaches—a position this threat action would hold for the next six years (and counting!). Our first offering was a user behavior analytics tool, UserInsight, which we launched in August 2013.

This SUBA engine combined Active Directory with DHCP, endpoint, and cloud service data to build user profiles for every person within an organization. In a world of tuning correlation rules, manual log search, and lengthy investigations, customers found it to be a breath of fresh air for identifying risky users and detecting the use of stolen credentials and anomalous lateral movement.

### 2\. Security analytics

While customers loved the user behavior analytics and detections, they didn’t want the burden of maintaining an existing SIEM/SIM as well: “You’re ingesting our important logs already—can you make them searchable and meet compliance needs?”

Following our acquisition of LogEntries in October 2015, we incorporated its powerful search technology and launched InsightIDR in February 2016. With a cloud-native architecture, InsightIDR had fast log search, real-time dashboards, and contextual investigations, all without scaling, infrastructure management, and convoluted search queries.

![InsightIDR.png](https://www.rapid7.com/cdn/images/blt9b5b5d50da3be72a/683de44dcc60421fb22068d0/InsightIDR.png)

### 3\. Deception technology (and Attacker Behavior Analytics)

Since we launched our [Managed Detection and Response service](/services/managed-detection-and-response-mdr/) in October 2015, there have been continuous investments in our ability to detect threats. There were two notable milestones that allowed InsightIDR to detect malicious activity outside of log files: deception technology and Attacker Behavior Analytics

Many traces of an adversary are not found in log analysis alone. InsightIDR now includes four distinct traps—honeypots, honey credentials, honey users, and honey files—that you can deploy to deceive and expose attackers.

Our Attacker Behavior Analytics library of more than 615 detections (mostly targeted at endpoints) continues to be built and maintained by our [security operations centers (SOCs)](/fundamentals/security-operations-center/) and threat intelligence teams. As we discover new attacker behaviors from our research, customers, and community, detections are created, tested, and made available to all InsightIDR customers.

The result? Reliable detections for common and targeted threats that directly reduce the impact of phishing, malware, and the use of stolen credentials.

### 4\. Automation and orchestration

Infosec’s responsibility is to find compromise, but it usually takes a team effort with IT to take action. When internal departments are siloed, it will take a flurry of tickets—and precious time—to contain a threat by disabling a user account, isolating a machine, or killing malicious processes. Taking the right action (and at scale) is the spirit behind SAO. We acquired Komand in July 2017, then released InsightConnect and started the rollout of new built-in orchestration capabilities for InsightIDR in September 2018.

For a three-minute detection to response scenario, check out the video below:

Play Video

![Vidyard video](https://play.vidyard.com/4528xwN6vUmm1ETdZgJitq.jpg)

****

### 5\. File integrity monitoring (FIM)

While blue teams must prepare for the unexpected, the yearly compliance audit is a known challenge. This month, we’re excited to [roll out file integrity monitoring (FIM)](/solutions/file-integrity-monitoring/), which will be available at no additional cost with your InsightIDR subscription.

This provides important file-level visibility for critical assets, as FIM is either mandated or recommended across PCI DSS, HIPAA, SOX, GDPR, and many other compliance frameworks. With this addition, you can meet multiple compliance mandates with InsightIDR, including the following:

  * Centralized log management and audit logging
  * User monitoring (e.g., privileged, remote, and executive users)
  * Breach detection
  * File integrity monitoring



Whew! That brings us to the present day, where we are quickly approaching 1,000 organizations that leverage Rapid7 for our detection and response needs. Combined with our continued coordination with our incident response and pentesting teams, the Metasploit Project, and our broader customer community, our evolution will continue so that you can unify, detect, and respond against the attacks of the future.

## Article tags

  * [Detection and Response](/blog/tag/detection-and-response/)
  * [Forrester Wave](/blog/tag/forrester-wave/)