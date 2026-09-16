# New Whitepaper: Stealthy BPFDoor Variants are a Needle That Looks Like Hay

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-new-whitepaper-stealthy-bpfdoor-variants/
- **Date :** 2026-04-02

---

## Executive Overview

Advanced persistent threats (APTs) are constantly and consistently changing tactics as network defenders plug holes in defenses. Static indicators of compromise (IoCs) for the BPFDoor have been widely deployed, forcing threat actors to get creative in their use of this particular strain of malware. What they came up with is ingenious.

New research from Rapid7 Labs has uncovered undocumented features leading to the discovery of 7 new BPFDoor variants: a stealthy kernel-level backdoor that uses Berkeley Packet Filters (BPFs) to inspect traffic from right inside the operating system kernel. This essentially creates a silent trapdoor that can be activated by a threat actor once a “magic packet” is tunneled via stateless protocols. The malware is then able to perfectly blend into the target environment, establishing nearly undetectable persistence in global telecom infrastructure.

Our latest research continues the narrative established in our blog __[_BPFdoor in Telecom Networks: Sleeper Cells in the Backbone_](https://www.rapid7.com/blog/post/tr-bpfdoor-telecom-networks-sleeper-cells-threat-research-report/). It involves the analysis of nearly 300 samples and identifies two primary new variants: httpShell and icmpShell. These variants represent a significant leap in operational security, utilizing stateless C2 routing and ICMP relay to bypass multi-million dollar security stacks.

### Rapid7 detection and response strategy:

Rapid7 is actively tracking these variants to ensure our customers remain protected against this evolving threat through the following:

  * **Intelligence Hub:** Customers with access to Rapid7’s Intelligence Hub are receiving continuous updates, including the latest intelligence, YARA rules, and Suricata detection rulesets.

  * **Actionable guidance:** We have released a specialized triage script (rapid7_bpfdoor_check.sh) designed to identify both legacy and modern BPFDoor variants by inspecting active BPF filters and validating masqueraded processes.

  * **Detection engineering:** Our detection strategy focuses on structural header anomalies, such as hardcoded ICMP sequence numbers and invalid protocol codes, rather than transient payload content.




## The strategic shift: Beyond legacy stealth

While BPFDoor has been active for years, its codebase has evolved significantly. The threat actor continues to incorporate minor features into the original [codebase](https://github.com/gwillgues/BPFDoor/blob/main/bpfdoor.c) leaked in 2022, resulting in a "messy" but effective toolkit designed to hinder threat hunting. Given the significant code overlap among BPFDoor variants, we focused on the minor, easily overlooked details the TA (threat actor) added to the leaked codebase.

### From memory to disk

Historically, BPFDoor was known for appearing "fileless" by executing from /dev/shm and deleting itself. However, modern endpoint detection and response (EDR) tools now flag processes running from deleted inodes in temporary filesystems. Recognizing this, the developers of the httpShell variant have eliminated the /dev/shm drop. The malware now resides on disk, using a single, hard-coded process name to blend in as a normal system daemon.

## Technical analysis: httpShell vs. icmpShell

Our research unraveled several undocumented features (some of them were**** not documented for nearly 5 years), leading to the discovery of two primary variants: httpShell and icmpShell.

### httpShell: The "Magic Ruler" of encapsulated traffic

The httpShell variant leverages kernel-level packet filters to perform validation across both IPv4 and IPv6 traffic. It uses HTTP-tunneling to extract hidden commands and features a newly discovered "Hidden IP" (HIP) field for dynamic routing.

  * **Kernel-level decapsulation** : By binding to all interfaces simultaneously, the malware forces the target’s own kernel to decapsulate complex carrier-grade tunnels like GRE or GTP. This allows the BPF filter to easily catch magic bytes hidden inside the inner packets.

  * **The offset evasion** : To survive enterprise proxies and WAFs that shift data positions, attackers use a mathematical padding scheme. They ensure their "9999" marker always lands exactly at the 26th byte offset of the inspected data, allowing the trigger to survive proxy headers.

  * **IPv6 limitations** : The filter assumes the UDP/TCP header starts exactly at byte 40 (standard empty IPv6 header). If an attacker includes IPv6 "Extension Headers," the payload is pushed further down, and the malware fails to wake up.




### icmpShell: The dynamic PTY tunnel

Designed for heavily restricted environments, icmpShell tunnels interactive sessions entirely over ICMP.

  * **PID-bound mutation** : This variant injects a dynamic BPF filter into the kernel that binds specifically to the malware's runtime Process ID (PID). Because the PID changes with every execution, the required "magic knock" signature mutates dynamically, rendering static firewall rules useless.

  * **Multi-mode execution** : Beyond basic shells, it implements bidirectional ICMP tunnels, UDP and ICMP “hole-punching”, and RC4 encryption.




Both variants support relay over ICMP.

## Stateless C2 and the "Hidden IP"

![New-magic-packet-structure.png](https://www.rapid7.com/cdn/images/bltfb7b9673f87f434b/69ce5cab267d5e0e7979f47c/New-magic-packet-structure.png) _Figure 1: New magic packet structure_

⠀

The discovery of the magic_packet_v2 struct featuring the HIP (hidden ip field) used for relay purposes highlights the malware's operational maturity.

### Dynamic C2 routing

One of the most elegant features is the use of a -1 flag (255.255.255.255) in the IP field of the magic packet structure.

  * **Mechanism** : If the flag is set, the malware ignores hardcoded IPs and sends its reverse shell back to the source IP found in the headers of the packet that woke it up.

  * **Strategic purpose** : This makes the attacker's controller completely stateless. Attackers can deploy from behind NAT or VPNs without needing to discover or hardcode their current external IP into the magic payload.




### ICMP lateral movement (the relay)
    
    
    if (auth(mpacket->pass) || mpacket->hip == -1 || !mpacket->hip)

When the above "Gatekeeper Condition" (authentication) is false, the malware transforms the infected machine into an invisible network router.

![ICMP-relay-using-HIP-field.jpg](https://www.rapid7.com/cdn/images/blt1fb22bc8afca0e67/69ce5d4cd43795e2ead0385f/ICMP-relay-using-HIP-field.jpg) _Figure 2: ICMP relay using the HIP field_

⠀

  * **The process** : It extracts an internal target IP from the HIP field, rewrites the trigger flag to ICMP magic bytes (0x5572), and fires a crafted ICMP Echo Request at the internal target.

  * **Loop prevention** : The malware wipes the hop IP to -1 to stop the next BPFDoor instance from forwarding the packet again.


![Rapid7-icmpshell-main-logic-chart.png](https://www.rapid7.com/cdn/images/blt4b8929a403386c6f/69ce5da41604eec835874f9a/Rapid7-icmpshell-main-logic-chart.png) _Figure 3: icmpShell main logic_

⠀

Rapid7 set up a playground lab to test icmpShell. For this scenario, two docker containers simulating an nginx edge proxy and a victim HSS infected with icmpShell have been used, while the attacker executes the trigger sending the magic packet via the newly discovered Rapid7 BPFDoor controller. To interact with the shell we developed the python script icmpshell.py to ensure RC4 state is consistent across echo requests received on the attacker’s side, filtering out also heartbeat echo requests featuring an invalid ICMP code 1.

In the bottom-right pane of the video below, we see the icmpShell variant being run with strace to debug its behavior. The top-left shows the controller triggering the backdoor after entering the new “icmp” password and crafting a magic packet over HTTPS (we will break down HTTPS tunneling and the new Rapid7 controller in a future blog) using magic bytes 0x5293. On the bottom-left pane the icmpshell.py runs to perform the ICMP handshake and handle shell traffic. The connection over ICMP established between the attacker machine (REMnux) and the victim HSS leverages a second BPF filter (13-BPF instructions), installed by the backdoor that uses the reverse shell PID as a fixed ICMP ID, ensuring the capture of shell-related packets. On the upper-right pane, an ICMP tcpdump capture is run.

⠀

⠀

The video ends showing that the backdoor exits after 12s of attacker inactivity, killing the connection. The tcpdump capture shows attacker traffic being sent in cleartext prepending ‘X:’ to commands while the victim response is RC4 encrypted with the key “icmp”.

Below, we can observe the tcpdump screens highlighting ICMP handshake, shell’s data encryption, attacker’s command and the usage of 1234 ICMP sequence number hardcoded in the backdoor.

![icmpshell_flow.jpeg](https://www.rapid7.com/cdn/images/bltd524e40c0f1a8e49/6aa177b65c31263fc244153a/icmpshell_flow.jpeg) _Figure 4: icmpShell encryption/decryption flow_

⠀

![icmpShell-sending-initial-ICMP-hello.png](https://www.rapid7.com/cdn/images/blte235abd3603fa932/69ce606c2c747bce885767b4/icmpShell-sending-initial-ICMP-hello.png) _Figure 5: icmpShell sending initial ICMP hello “X:3458”_

⠀

![attacker-sending-cleartext-command-ICMP.png](https://www.rapid7.com/cdn/images/blted9e411627da3e74/69ce606c78b2b1a73276db6c/attacker-sending-cleartext-command-ICMP.png) _Figure 6: attacker sending cleartext command over ICMP prepending “X:”_

⠀

Figure 7 below shows the heartbeat payload ignored by icmpshell.py acting as an ICMP “hole-punching” to keep the firewall state table active.

![ICMP-hardcoded-hole-punching-heartbeat-icmpshell.png](https://www.rapid7.com/cdn/images/bltc8797a2b45a87fa6/69ce616205b5be6a630124ed/ICMP-hardcoded-hole-punching-heartbeat-icmpshell.png) _Figure 7: ICMP “hole-punching” heartbeat hardcoded in icmpShell_

## Rapid7 variants

The research of new variants is still ongoing. At the time of writing, Rapid7 identified seven new variants featuring new magic bytes and active C2 beaconing summarized below.

Samples **2cc90edd9bc085f54851bed101f95ce2bace7c9a963380cfd11ea0bc60e71e0c** and **de472ed37e33b79e1aa37e67a680ee3a9d74628438c209543a06e916a0a86fba** , which we classify as **R7 variant ‘F’** , increase stealthiness by hiding under /var/run/user/0. By avoiding the usual chmod command, the attacker ensures that no "change mode" event is logged by the kernel's audit system (auditd). Since /run is rarely mounted with the noexec flag (unlike /tmp), the malware bypasses the most common local hardening measure.

⠀

![BPFDoor-running-var-run-user-0.png](https://www.rapid7.com/cdn/images/blt28177f5110d54bdb/69ce61e66e737f69aece19ed/BPFDoor-running-var-run-user-0.png) _Figure 8: BPFDoor running from /var/run/user/0_

⠀

Most samples simply redirect output to /dev/null. This variant goes further by performing a total FD (File Descriptor) wipe. Note the recurring timestomping routine following the old known anti-forensics technique.

![Timestomping-full-fds-wipe.png](https://www.rapid7.com/cdn/images/bltb478f4435630aec8/69ce7a008e8869081f36a5ff/Timestomping-full-fds-wipe.png) _Figure 9: Timestomping and full fds wipe_

⠀

R7 variant ‘F’ exhibits a 26**-** BPF instruction filter featuring new magic bytes. Rapid7 developed a tool to extract BPF bytecode logic and identify variant-specific features. Three samples employed previously unknown magic bytes. Below is the output summarizing the filtering logic (Figure 10: **2cc90edd9bc085f54851bed101f95ce2bace7c9a963380cfd11ea0bc60e71e0c**

**De472ed37e33b79e1aa37e67a680ee3a9d74628438c209543a06e916a0a86fba** ;**** Figure 11**:****757e911edaf45cc135f2498c38d4db8acec39cb6aeb3a1dcc38305ab2d326fa9**).

![Rapid7-variant-F-new-magic-bytes.png](https://www.rapid7.com/cdn/images/blt545264d4680f5f7a/69ce630f6ec44e3609d53611/Rapid7-variant-F-new-magic-bytes.png) _Figure 10: Rapid7 variant F new magic bytes_

⠀

The BPF filtering can be expressed using libcap syntax:
    
    
    udp[8:2] == 0x3182 or (icmp[8:2] == 0x1051 and icmp[icmptype] == icmp-echo) or tcp[((tcp[12]&0xf0)>>2):2] == 0x3321

⠀

![R7-variant-F-new-magic-bytes.png](https://www.rapid7.com/cdn/images/blt9f598a4302a068f3/69ce63a922934a6e7744a7b9/R7-variant-F-new-magic-bytes.png) _Figure 11: Rapid7 variant F new magic bytes_

⠀
    
    
    udp[8:2] == 0x2048 or (icmp[8:2] == 0x1155 and icmp[icmptype] == icmp-echo) or tcp[((tcp[12]&0xf0)>>2):2] == 0x5433

Earlier versions used SOCK_RAW when creating the AF_PACKET socket. When using SOCK_RAW, the kernel delivers the entire packet, including the link-layer header, while with SOCK_DGRAM the Ethernet header is discarded. This change directly impacts the way packets are parsed.

### Multi-protocol parallel sniffing

One new variant sample, which we named **variant ‘G’** , utilizes a multi-threaded architecture to ensure triple-redundant capture of "wake-up" packets. The malware spawns three independent threads, each responsible for monitoring a specific transport protocol at the raw IP layer.

This is achieved by invoking the socket() system call with protocol-specific parameters for TCP, UDP, and ICMP:

  * **TCP:** socket(AF_INET, SOCK_RAW, IPPROTO_TCP)

  * **UDP:** socket(AF_INET, SOCK_RAW, IPPROTO_UDP)

  * **ICMP:** socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)




The implant achieves simultaneous trigger detection across three protocols by deploying identical BPF filters on protocol-specific raw sockets. This functionality is implemented using three separate threads for protocol capture. This design is crucial: By dedicating a thread to each protocol, the malware prevents high-volume traffic in one protocol from overloading the sniffer and causing it to miss a "magic" trigger arriving via a less-trafficked protocol.

Beyond preventing packet loss, this parallel architecture provides C2 resiliency via built-in fallback channels. Because the BPF filters concurrently sniff TCP, UDP, and ICMP, the threat actor becomes highly resilient to sudden perimeter security changes. If a network defender updates an egress firewall to aggressively block anomalous ICMP or UDP traffic, the attacker can seamlessly switch to sending magic triggers over TCP.

Some samples (Figure 12: **ed768dd922742a597257ad684820d7562bb6be215710ec614bd041a22f3d6863**) exhibit the usage of threads and a new mutex/process name being spoofed like “hpasmlited”:

![hpasmlited-process-name-spoofing.png](https://www.rapid7.com/cdn/images/blta42dd668f978b8fa/69ce7a6005b5be21b201259e/hpasmlited-process-name-spoofing.png) _Figure 12: hpasmlited process name spoofing_

⠀

Then**** start_routine, sub_4089BB, sub_4084F7**** proceeds with the old codebase installing the same BPF filter shared among TM variant D samples; this variant supports ICMP relay.

Below is shown the creation of three different kinds of sockets filtering traffic by TCP, UDP, and ICMP:

![Creating-sockets-handling-TCP-UDP-ICMP.png](https://www.rapid7.com/cdn/images/blt62eecb0870fc9b69/69ce65cf11fa1e2676b55cff/Creating-sockets-handling-TCP-UDP-ICMP.png) _Figure 13: Creation of 3 sockets handling TCP, UDP, and ICMP_

⠀

Note that **a0t** is an array containing three BPF filters, each of them containing the same**** 229**** instructions found in TM variant D. 

### HPE ProLiant-tuned variant: Living off the land

One variant (Figure 14: **9ee77ed38e5bc69f841bdaba7c5e6c3bf30fd9ae94cd2e69f39834e9cec76e82**)_****_ was specifically tailored for HPE ProLiant servers, demonstrating a "living off the land" approach through binary masquerading.

![HPE-Insight-Management-Agents-spoofing.png](https://www.rapid7.com/cdn/images/bltc4b9e8eb6d512bc3/69ce665d99d6c57c497e4b13/HPE-Insight-Management-Agents-spoofing.png) _Figure 14: HPE Insight Management Agents spoofing_

⠀

The process name is set to cmathreshd, with realistic flags like -p 5 -s OK, directly impersonating the HPE Insight Management Agents. The malware checks for /var/run/cma.lock. If found, it kills the legitimate HP agent and takes its place. This displacement prevents resource conflicts that would otherwise alert system administrators. The call to unsetenv("LD_PRELOAD") is designed to disable user-mode security hooks (such as local EDRs or rootkit hunters) that monitor system calls.  
This specific masquerading tactic demonstrates deep environmental awareness. The threat actors recognize they are operating on physical, bare-metal HPE hardware commonly deployed in 4G and 5G core and edge systems (such as Ericsson-style architectures). 

### The active beacon: Guaranteed persistence

Rapid7 variant ‘H’ contrasts with the classic, stealthy BPFDoor sniffer (which generates no outbound traffic). The beacon is proactive and provides guaranteed access by bypassing stateful firewalls that only permit outbound connections. It achieves this via a continuous heartbeat mechanism that resolves dynamic DNS domains, such as ntpussl.instanthq.com and ntpupdate.ddnsgeek.com. By masquerading as Network Time Protocol (NTP) over SSL, the threat actors seamlessly encapsulate their encrypted C2 sessions within what appears to be routine time synchronization or IoT telemetry. This 'hide in plain sight' tactic allows the active beacon to blend into the baseline network noise and establish a direct, unauthenticated connection on port 443 using the old-fashioned statically linked OpenSSL library and RC4-MD5 ciphersuite.

  * **Heartbeat mechanism:** The function actively attempts to resolve the hardcoded C2 domain ntpussl.instanthq.com using the gethostbyname() function. It runs in an infinite loop, attempting to connect if the domain resolves. If the connection fails, it sleeps for a random interval (1 to 2.5 minutes) before trying again — this acts as the Heartbeat.

  * **Masquerading:** The domain ntpussl.instanthq.com mimics NTP (Network Time Protocol) over SSL, blending into standard time-sync or certificate update traffic.

  * **Activation kill switch:** A "Kill Switch" or "Activation" check verifies the IP returned by the DNS query: if ( !strstr(v1, "127.0.0.1") ).

  * **Direct connection:** The malware connects to the resolved IP on port 443 (0x1BB) without requiring authentication.


![Rapid7-variant-H-active-beaconing.png](https://www.rapid7.com/cdn/images/blt41183d8d1dfe5d12/69ce66d278b2b12b1876db8f/Rapid7-variant-H-active-beaconing.png) _Figure 15: Rapid7 variant H active beaconing (sample spoofing the HPEProliant cmathreshd)_

⠀

Stack strings were employed to bypass basic static signature detection:

![Screenshot_2026-04-02_at_9.35.09_AM.png](https://www.rapid7.com/cdn/images/blt11efc08c9532e76e/69ce7b298eac30c5b4a8abba/Screenshot_2026-04-02_at_9.35.09_AM.png) _Figure 16: ca56622773c1b6f648b1578978b57aa668df25a11e0c782be008384a6af6c2c4_

⠀

By encapsulating encrypted shell sessions within what appears to be routine time synchronization or IoT telemetry, the threat actors effectively bypass standard firewall rules. Below is the list of domains observed being used by Chinese TAs during espionage campaigns:

#### "Encrypted" Masquerade

  * **Domain:** ntpussl[.]instanthq.com

  * **Function & analysis: **Encrypted Shell/Tunneling. "ntpussl" recalls an ssl connection with an NTP server. (**195b98211d1ce968669a0740ca08d0ddcf03a2df03a47e2e70550f6c002b49e8** ; **9ee77ed38e5bc69f841bdaba7c5e6c3bf30fd9ae94cd2e69f39834e9cec76e82**).




#### "System Update" Disguise

  * **Domain:** ntpupdate.ddnsgeek[.]com
  * **Function & analysis: **Standard Utility Mimicry. This domain mimics the common ntpdate utility. The use of terms like "geek" or "update" is a social engineering tactic, as security analysts often overlook such domains, assuming they belong to benign OS background processes (**ca56622773c1b6f648b1578978b57aa668df25a11e0c782be008384a6af6c2c4**).



#### "Persistence" Disguise

  * **Domain:** ntpupdate.ygto[.]com
  * **Function & analysis: **Rapid IP Rotation. This domain is employed for dynamic DNS updates, enabling rapid IP rotation. If the primary C2 IP address is blocked, the attackers update the DDNS record at ygto.com to maintain command-and-control access.



#### "IoT/Camera" Disguise

  * **Domain:** ntpd.casacam[.]net
  * **Function & analysis: **Blending with residential traffic. Masquerades as a time check service for IP cameras. Since casacam.net is a legitimate DDNS provider for DVRs, traffic to this domain easily blends into the millions of devices monitored by telecom networks, especially in residential broadband environments.



_Note: The domains ntpupdate.ygto[.]com and ntpd.casacam[.]net are involved in generic trojan/spam campaigns._

###  Rapid7 variants I,J,K and L

Rapid7 **variant “I”** uses an 11-instruction BPF filter targeting TCP port 9999, enforcing a two-step handshake, requiring firstly new magic bytes (0xA9F205C3) in the tcp payload, secondly the presence of a hardcoded magic password (dP7sRa3XwLm29E). Finally, it extracts the attacker’s IP and port to spawn an unencrypted reverse shell.

Rapid7 assigned icmpShell and httpShell variants the letters **J,K** respectively while the letter **L** is reserved for samples exhibiting only the ICMP relay feature. To summarize:

  * **Variant J** : ICMP relay + HTTP tunneling + icmpShell

  * **Variant K** : ICMP relay + HTTP tunneling

  * **Variant L** : ICMP relay




## MITRE ATT&CK Matrix Mapping

### Tactic: Execution

#### T1059.004: Unix Shell

  * **Implementation details:** Hijacks a pseudo-terminal (PTY) utilizing fork() and dup2().
  * **Variation:** Both



### Tactic: Defense Evasion

#### T1036.004: Masquerading

  * **Implementation details:** Alters process arguments to mimic benign daemons like qmgr.
  * **Variation:** Both



#### T1070.003: Clear History

  * **Implementation details:** Injects HISTFILE=/dev/null into environment variables.
  * **Variation:** Both



#### T1027: Obfuscated Files Information

  * **Implementation details:** Stack strings for passwords and paths prevent static extraction.
  * **Variation:** Both



#### T1564: Hide Artifacts

  * **Implementation details:** Uses AF_PACKET sniffing to remain invisible to local netstat/ss.
  * **Variation:** Both



### Tactic: Persistence

#### T1205: Traffic Signaling

  * **Implementation details:** Employs magic bytes and flags like 0xFFFFFFFF as wake-up triggers.
  * **Variation:** Both



### Tactic: Command & Control

#### T1573.001: Symmetric Cryptography

  * **Implementation details:** e.g. Enforces the X: plaintext tag and encrypts the underlying PTY output via an RC4 cipher (using the hardcoded ICMP key).
  * **Variation:** Both



#### T1071.001: Application Layer Protocol

  * **Implementation details:** Blends in by utilizing formatted HTTP POST requests with hardcoded URIs up to 100-byte hexadecimal bodies.
  * **Variation:** httpShell



#### T1095: Non-App Protocol

  * **Implementation details:** Transmits exfiltration via crafted ICMP Echo Requests.
  * **Variation:** Both



#### T1090: Proxy

  * **Implementation details:** Uses ICMP relay to bounce traffic through internal segments.
  * **Variation:** Both



#### T1001: Data Obfuscation

  * **Implementation details:** icmpShell hides its tracking mechanisms directly inside the network layer headers. By truncating the Linux Process ID (PID) and injecting it into the 16-bit ICMP Identifier field, and hardcoding the ICMP Sequence Number to 1234, it obfuscates its session tracking data as standard network metadata.
  * **Variation:** icmpShell



#### T1572: Protocol Tunneling

  * **Implementation details:** ICMP tunneling
  * **Variation:** icmpShell



#### T1090: Proxy

  * **Implementation details:** The BPF filter concurrently sniffs TCP, UDP, and ICMP. If one protocol is blocked by egress filtering, the attacker can seamlessly utilize an alternate protocol to trigger the shell without reconfiguring the implant.
  * **Variation:** Both



## Defensive depth and detection guidance

Detection must shift from looking for payload content to identifying structural anomalies and static protocol markers.

  * **Suricata/NIDS focus** : Target the hardcoded 1234 sequence number used in custom functions and the technically invalid ICMP Code 1 injected by the heartbeat thread.

  * **Host monitoring** : Monitor for processes whose executable path does not exist on disk and spoofed processes running as root (e.g., zabbix_agentd, dockerd).

  * **Auditd rules** : Monitor the creation of AF_PACKET sockets (capturing SOCK_RAW and SOCK_DGRAM) and the setsockopt call used to attach BPF filters.

  * **Rapid7 triage script** : Utilize the rapid7_bpfdoor_check.sh script to check for zero-byte mutex files and active BPF filters attached to packet sockets. Get the complete checklist at [Rapid7’s github.](https://github.com/rapid7/Rapid7-Labs/tree/main/BPFDoor)




## Final takeaways

  * **Kernel-level evasion** : The shift to SOCK_DGRAM allows the malware to simplify magic packet parsing by letting the host kernel decapsulate tunnels.

  * **Layer 7** **camouflage** : Weaponized SSL termination and "magic ruler" padding ensure trigger bytes survive WAF/Proxy interference.

  * **Deep** -**network** **lateral** **movement** : The "Hidden IP" field transforms infected machines into invisible network routers for bidirectional ICMP PTY tunnels.

  * **New Variants** : the newly identified features in BPFDoor samples highlight how TAs are tailoring and reusing BPFDoor’s code to the target environment. The rapid7 variant H (active beacon) stands out as it tries to blend in with the network traffic contacting fake NTP update servers.

  * **Operational security****:** The malware can instruct the infected node to spawn a shell to the source of the magic packet using the signed -1, without embedding the C2 or proxy IP in the packet payload. Furthermore, unlike httpShell, the icmpShell is designed to run without requiring live interaction as it terminates itself after 12s of inactivity, demonstrating how surgical and precise the TA intervention is when accessing the core of the backbone, achieving maximum stealthiness.




For an exhaustive deep dive of the assembly code, BPF bytecode, and exact packet structures used by icmpShell and httpShell variants, please refer to our **technical whitepaper**[**here**](https://www.rapid7.com/cdn/assets/bltd3dbeae8537bb21b/69ce33a499d6c52de57e4a02/unmasking-the-new-stealthy-BPFDoor-variants.pdf). You can also view our**on-demand webinar**[**here**](https://www.brighttalk.com/webcast/10457/665136?utm_source=Rapid7&utm_medium=brighttalk&utm_campaign=665136?utm_source=brighttalk&utm_medium=blog&utm_content=follow-up&utm_campaign=global-pla-q1-2026-project-matrix-webinar-prospect-eng).

## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)
  * [Threat Intel](/blog/tag/threat-intel/)