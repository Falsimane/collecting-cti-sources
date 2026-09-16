# RCE to Sliver: IR Tales from the Field | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2024/02/15/rce-to-sliver-ir-tales-from-the-field/
- **Date :** 2025-06-02

---

_*Rapid7 Incident Response consultants Noah Hemker, Tyler Starks, and malware analyst Tom Elkins contributed analysis and insight to this blog.*_

Rapid7 Incident Response was engaged to investigate an incident involving unauthorized access to two publicly-facing Confluence servers that were the source of multiple malware executions. Rapid7 identified evidence of exploitation for [CVE-2023-22527](/blog/post/2024/01/19/etr-critical-cves-in-outdated-versions-of-atlassian-confluence-and-vmware-vcenter-server/) within available Confluence logs. During the investigation, Rapid7 identified cryptomining software and a Sliver Command and Control (C2) payload on in-scope servers. Sliver is a modular C2 framework that provides adversarial emulation capabilities for red teams; however, it’s also frequently abused by threat actors. The Sliver payload was used to action subsequent threat actor objectives within the environment. Without proper security tooling to monitor system network traffic and firewall communications, this activity would have progressed undetected leading to further compromise.

## Rapid7 customers

Rapid7 consistently monitors [emergent threats](/blog/tag/emergent-threat-response/) to identify areas for new detection opportunities. The recent appearance of Sliver C2 malware prompted Rapid7 teams to conduct a thorough analysis of the techniques being utilized and the potential risks. Rapid7 InsightIDR has an alert rule Suspicious Web Request - Possible Atlassian Confluence CVE-2023-22527 Exploitation available for all IDR customers to detect the usage of the text-inline.vm consistent with the exploitation of CVE-2023-22527. A [vulnerability check](/db/vulnerabilities/atlassian-confluence-cve-2023-22527/) is also available to InsightVM and Nexpose customers. A Velociraptor artifact to hunt for evidence of Confluence CVE-2023-22527 exploitation is available on the Velociraptor Artifact Exchange [here](https://docs.velociraptor.app/exchange/artifacts/pages/confluence_cve_2023_22527/). Read Rapid7’s blog on [CVE-2023-22527](/blog/post/2024/01/19/etr-critical-cves-in-outdated-versions-of-atlassian-confluence-and-vmware-vcenter-server/).

## Observed Attacker Behavior

Rapid7 IR began the investigation by triaging available forensic artifacts on the two affected publicly-facing Confluence servers. These servers were both running vulnerable Confluence software versions that were abused to obtain Remote Code Execution (RCE) capabilities. Rapid7 reviewed server access logs to identify the presence of suspicious POST requests consistent with known vulnerabilities, including CVE-2023-22527. This vulnerability is a critical OGNL injection vulnerability that abuses the text-inline.vm component of Confluence by sending a modified POST request to the server.

Evidence showed multiple instances of exploitation of this CVE, however, evidence of an embedded command would not be available within the standard header information logged within access logs. Packet Capture (PCAP) was not available to be reviewed to identify embedded commands, but the identified POST requests are consistent with the exploitation of the CVE.  
The following are a few examples of the exploitation of the Confluence CVE found within access logs:

Access.log Entry  
---  
POST /template/aui/text-inline.vm HTTP/1.0 200 5961ms 7753 - Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36  
POST /template/aui/text-inline.vm HTTP/1.0 200 70ms 7750 - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15  
POST /template/aui/text-inline.vm HTTP/1.0 200 247ms 7749 - Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0  
  
Evidence showed the execution of a curl command post-exploitation of the CVE resulting in the dropping of cryptomining malware to the system. The IP addresses associated with the malicious POST requests to the Confluence servers matched the IP addresses of the identified curl command. This indicates that the dropped cryptomining malware was directly tied to Confluence CVE exploitation.  
As a result of the executed curl command, file w.sh was written to the /tmp/ directory on the system. This file is a bash script used to enumerate the operating system, download cryptomining installation files, and then execute the cryptomining binary. The bash script then executed the wget command to download javs.tar.gz from the IP address 38.6.173[.]11 over port 80. This file was identified to be the XMRigCC cryptomining malware which caused a spike in system resource utilization consistent with cryptomining activity. Service javasgs_miner.service was created on the system and set to run as root to ensure persistence.

The following is a snippet of code contained within w.sh defining communication parameters for the downloading and execution of the XMRigCC binary.

![Screenshot-2024-02-15-at-11.36.41-AM.png](https://www.rapid7.com/cdn/images/bltd857642ab9d8ad9c/683de0662a7686862abc8463/Screenshot-2024-02-15-at-11.36.41-AM.png)

Rapid7 found additional log evidence within Catalina.log that references the download of the above file inside of an HTTP response header. This response registered as ‘invalid’ as it contained characters that could not be accurately interpreted. Evidence confirmed the successful download and execution of the XMRigCC miner, so the above Catalina log may prove useful for analysts to identify additional proof of attempted or successful exploitation.

Catalina Log Entry  
---  
WARNING [http-nio-8090-exec-239 url: /rest/table-filter/1.0/service/license; user: Redacted ] org.apache.coyote.http11.Http11Processor.prepareResponse The HTTP response header [X-Cmd-Response] with value [http://__38.6.173.11/xmrigCC-3.4.0-linux-generic-static-amd64.tar.gz xmrigCC-3.4.0-linux-generic-static-amd64.tar.gz... ] has been removed from the response because it is invalid  
  
Rapid7 then shifted focus to begin a review of system network connections on both servers. Evidence showed an active connection with known-abused IP address 193.29.13[.]179 communicating over port 8888 from both servers. netstat command output showed that the network connection’s source program was called X-org and was located within the system’s /tmp directory. According to firewall logs, the first identified communication from this server to the malicious IP address aligned with the timestamps of the identified X-org file creation. Rapid7 identified another malicious file residing on the secondary server named X0 Both files shared the same SHA256 hash, indicating that they are the same binary. The hash for these files has been provided below in the IOCs section.

A review of firewall logs provided a comprehensive view of the communications between affected systems and the malicious IP address. Firewall logs filtered on traffic between the compromised servers and the malicious IP address showed inbound and outbound data transfers consistent with known C2 behavior. Rapid7 decoded and debugged the Sliver payload to extract any available Indicators of Compromise (IOCs). Within the Sliver payload, Rapid7 confirmed the following IP address 193.29.13[.]179 would communicate over port 8888 using the mTLS authentication protocol.

![Screenshot-2024-02-15-at-11.38.04-AM.png](https://www.rapid7.com/cdn/images/bltdb870b0a3451587e/683de0895619a15c06c6ea79/Screenshot-2024-02-15-at-11.38.04-AM.png)

After Sliver first communicated with the established C2, it checked the username associated with the current session on the local system, read etc/passwd and etc/machine-id and then communicated back with the C2 again. The contents of passwd and machine-id provide system information such as the hostname and any account on the system. Cached credentials from the system were discovered to be associated with outbound C2 traffic further supporting this credential access. This activity is consistent with the standard capabilities available within the GitHub release of Sliver hosted [here](https://github.com/BishopFox/sliver/tree/master).

The Sliver C2 connection was later used to execute wget commands used to download Kerbrute, Traitor, and Fscan to the servers. Kerbute was executed from dev/shm and is commonly used to brute-force and enumerate valid Active Directory accounts through Kerberos pre-authentications. The Traitor binary was executed from the var/tmp directory which contains the functionality to leverage Pwnkit and Dirty Pipe as seen within evidence on the system. Fscan was executed from the var/tmp directory with the file name f and performed scanning to enumerate systems present within the environment. Rapid7 performed containment actions to deny any further threat actor activity. No additional post-exploitation objectives were identified within the environment.

## Mitigation guidance

To mitigate the attacker behavior outlined in this blog, the following mitigation techniques should be considered:

  * Ensure that unnecessary ports and services are disabled on publicly-facing servers.

  * All publicly-facing servers should regularly be patched and remain up-to-date with the most recent software releases.

  * Environment firewall logs should be aggregated into a centralized security solution to allow for the detection of abnormal network communications.

  * Firewall rules should be implemented to deny inbound and outbound traffic from unapproved geolocations.

  * Publicly-facing servers hosting web applications should implement a restricted shell, where possible, to limit the capabilities and scope of commands available when compared to a standard bash shell.




## MITRE ATT&CK Techniques

Tactics| Techniques| Details  
---|---|---  
Command and Control| Application Layer Protocol (T1071)| Sliver C2 connection  
Discovery| Domain Account Discovery (T1087)| Kerbrute enumeration of Active Directory  
Reconnaissance| Active Scanning (T1595)| Fscan enumeration  
Privilege Escalation| Setuid and Setgid (T1548.001)| Traitor privilege escalation  
Execution| Unix Shell (T1059.004)| The Sliver payload and follow-on command executions  
Credential Access| Brute Force (T1110)| Kerbrute Active Directory brute force component  
Credential Access| OS Credential Dumping (T1003.008)| Extracting the contents of /etc/passwd file  
Impact| Resource Hijacking (T1496)| Execution of cryptomining software  
Initial Access| Exploit Public-Facing Application (T1190)| Evidence of text-inline abuse within Confluence logs  
  
## Indicators of Compromise

Attribute| Value| Description  
---|---|---  
Filename and Path| /dev/shm/traitor-amd64| Privilege escalation binary  
SHA256| fdfbfc07248c3359d9f1f536a406d4268f01ed63a856bd6cef9dccb3cf4f2376| Hash for Traitor binary  
Filename and Path| /var/tmp/kerbrute_linux_amd64| Kerbrute enumeration of Active Directory  
SHA256| 710a9d2653c8bd3689e451778dab9daec0de4c4c75f900788ccf23ef254b122a| Hash for Kerbrute binary  
Filename and Path| /var/tmp/f| Fscan enumeration  
SHA256| b26458a0b60f4af597433fb7eff7b949ca96e59330f4e4bb85005e8bbcfa4f59| Hash for Fscan binary  
Filename and Path| /tmp/X0| Sliver binary  
SHA256| 29bd4fa1fcf4e28816c59f9f6a248bedd7b9867a88350618115efb0ca867d736| Hash for Sliver binary  
Filename and Path| /tmp/X-org| Sliver binary  
SHA256| 29bd4fa1fcf4e28816c59f9f6a248bedd7b9867a88350618115efb0ca867d736| Hash for Sliver binary  
IP Address| 193.29.13.179| Sliver C2 IP address  
Filename and Path| /tmp/w.sh| Bash script for XMrigCC cryptominer  
SHA256| 8d7c5ab5b2cf475a0d94c2c7d82e1bbd8b506c9c80d5c991763ba6f61f1558b0| Hash for bash script  
Filename and Path| /tmp/javs.tar.gz| Compressed crypto installation files  
SHA256| ef7c24494224a7f0c528edf7b27c942d18933d0fc775222dd5fffd8b6256736b| Hash for crypto installation files  
Log-Based IOC| "POST /template/aui/text-inline.vm HTTP/1.0 200" followed by GET request containing curl| Exploit behavior within Confluence access.log  
IP Address| 195.80.148.18| IP address associated with exploit behavior of text-inline followed by curl  
IP Address| 103.159.133.23| IP address associated with exploit behavior of text-inline followed by curl  
  
## Article tags

  * [Incident Response](/blog/tag/incident-response/)
  * [Managed Detection and Response (MDR)](/blog/tag/mdr-managed-detection-response/)
  * [Detection and Response](/blog/tag/detection-and-response/)
  * [Emergent Threat Response](/blog/tag/emergent-threat-response/)
  * [Research](/blog/tag/research/)