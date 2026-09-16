# High-Risk Vulnerabilities in ConnectWise ScreenConnect | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/02/20/etr-high-risk-vulnerabilities-in-connectwise-screenconnect/
- **Date :** 2025-06-02

---

On February 19, 2024 ConnectWise disclosed two vulnerabilities in their ScreenConnect remote access software. Both vulnerabilities affect ScreenConnect 23.9.7 and earlier. Neither vulnerability had a CVE assigned at time of disclosure, but as of February 21, CVEs have been assigned to both issues mentioned in ConnectWise’s [advisory](https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8): 

  * [**CVE-2024-1709**](https://nvd.nist.gov/vuln/detail/CVE-2024-1709)**:** An authentication bypass using an alternate path or channel (CVSS 10)
  * [**CVE-2024-1708**](https://nvd.nist.gov/vuln/detail/CVE-2024-1708)**:** A path traversal issue (CVSS 8.4)



ScreenConnect is popular remote access software used by many organizations globally; it has also been [abused by adversaries](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-025a) in the past. There appear to be some [7,500+ instances](https://www.shodan.io/search?query=%22Server%3A+ScreenConnect%22) of ScreenConnect exposed to the public internet. The vulnerabilities were not**** known to be exploited in the wild when they were disclosed, but as of the evening of February 20, **ConnectWise has**[**indicated**](https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8)**they have confirmed compromises arising from exploitation of these vulnerabilities**. Rapid7 Managed Detection and Response (MDR) has also observed successful exploitation in customer environments. 

Security news media and security vendors are raising strong alarms about the ScreenConnect vulnerabilities, largely because of the potential for attackers to exploit vulnerable ScreenConnect instances to then push ransomware to downstream clients. This may be a particular concern for managed service providers (MSPs) or managed security services providers (MSSPs) who use ScreenConnect to remotely manage client environments.

### Mitigation guidance

All versions of ConnectWise ScreenConnect before 23.9.8 are vulnerable to these (CVE-less) issues. Customers who have on-premise ScreenConnect instances in their environments should apply the 23.9.8 update **on an emergency basis** , per [ConnectWise’s guidance](https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8). The vendor has also published several indicators of compromise (IOCs) in their advisory that organizations can hunt for. Rapid7 strongly recommends looking for signs of compromise even after the patch has been applied.

ConnectWise have also removed licensing restrictions to allow partners to update to supported systems, and they have [updated their advisory](https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8) to note the following: "ConnectWise has rolled out an additional mitigation step for unpatched, on-premise users that suspends an instance if it is not on version 23.9.8 or later. If your instance is found to be on an outdated version, an alert will be sent with instructions on how to perform the necessary actions to release the server."

### Rapid7 customers

InsightVM and Nexpose customers can assess their exposure to these vulnerabilities with authenticated vulnerability checks available in the February 21 content release. 

InsightIDR and Managed Detection and Response customers have existing detection coverage through Rapid7's expansive library of detection rules. Rapid7 recommends installing the Insight Agent on all applicable hosts to ensure visibility into suspicious processes and proper detection coverage. Below is a non-exhaustive list of detections deployed and alerting on activity related to these vulnerabilities:

  * Suspicious Web Requests - Possible ConnectWise ScreenConnect Exploitation
  * Attacker Technique - Remote Access Via ScreenConnect
  * Attacker Technique - Command Execution Via ScreenConnect
  * Suspicious Process - ScreenConnect with RunRole Argument
  * Attacker Technique - ConnectWise ScreenConnect Exploit Adding a New User



 _**Note:**___ In order for Rapid7 to alert on the rule Attacker Technique: ConnectWise ScreenConnect Exploit Adding a New User, customers will have to ensure that a host's Advanced Security Audit Policy Settings for Kernel Object is configured to log Windows EventID 4663 and have a SACL set on ScreenConnect's directory. More information on how to configure the Advanced Audit Policy is available [here]( https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn319064\(v=ws.11\)).

A Velociraptor artifact is [available here](https://docs.velociraptor.app/exchange/artifacts/pages/screenconnect/) to assist in hunting for indicators of compromise. A Metasploit module is [available here](https://github.com/rapid7/metasploit-framework/pull/18870) (pending final merge and release).

## Updates

**February 21, 2024:** Updated to include CVEs (CVE-2024-1708, CVE-2024-1709) and to note [exploitation in the wild](https://www.connectwise.com/company/trust/security-bulletins/connectwise-screenconnect-23.9.8). Rapid7 MDR has also observed exploitation in customer environments. Updated with availability of vulnerability checks to InsightVM and Nexpose customers.

**February 22, 2024:** New detection rule added for InsightIDR and MDR customers (Attacker Technique: ConnectWise ScreenConnect Exploit Adding a New User)

**February 23, 2024:** Velociraptor artifact now available, Metasploit module in development. Changes to ConnectWise advisory guidance have been added to the Mitigation guidance section of this blog.

## Article tags

  * [Vulnerability Management](/blog/tag/vulnerability-management/)
  * [Emergent Threat Response](/blog/tag/emergent-threat-response/)
  * [Research](/blog/tag/research/)