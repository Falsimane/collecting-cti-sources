# When Wi-Fi Encryption Fails: Protecting Your Enterprise from AirSnitch Attacks

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/
- **Date :** 2026-04-22

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# When Wi-Fi Encryption Fails: Protecting Your Enterprise from AirSnitch Attacks

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 12 min read 

Related Products

[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Industrial and Operational Technology icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Industrial and Operational Technology](https://unit42.paloaltonetworks.com/product-category/industrial-operational-technology/ "Industrial and Operational Technology")[![IoT Security icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)IoT Security](https://unit42.paloaltonetworks.com/product-category/iot-security/ "IoT Security")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Emmanuel Zhou](https://unit42.paloaltonetworks.com/author/emmanuel-zhou/)
    * [Adam Robbie](https://unit42.paloaltonetworks.com/author/adam-robbie/)
    * [Rick Wyble](https://unit42.paloaltonetworks.com/author/rick-wyble/)
    * [Zhutian Liu](https://unit42.paloaltonetworks.com/author/zhutian-liu/)
    * [Zhiyun Qian](https://unit42.paloaltonetworks.com/author/zhiyun-qian/)
    * [Zhaowei Tan](https://unit42.paloaltonetworks.com/author/zhaowei-tan/)
    * [Srikanth V. Krishnamurthy](https://unit42.paloaltonetworks.com/author/srikanth-v-krishnamurthy/)
    * [Mathy Vanhoef](https://unit42.paloaltonetworks.com/author/mathy-vanhoef/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:April 22, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [AirSnitch](https://unit42.paloaltonetworks.com/tag/airsnitch/)
    * [MitM](https://unit42.paloaltonetworks.com/tag/mitm/)
    * [Network security](https://unit42.paloaltonetworks.com/tag/network-security/)
    * [Port stealing](https://unit42.paloaltonetworks.com/tag/port-stealing/)
    * [WiFi encryption](https://unit42.paloaltonetworks.com/tag/wifi-encryption/)
    * [Wireless](https://unit42.paloaltonetworks.com/tag/wireless/)
    * [WPA2](https://unit42.paloaltonetworks.com/tag/wpa2/)
    * [WPA3](https://unit42.paloaltonetworks.com/tag/wpa3/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=When%20Wi-Fi%20Encryption%20Fails:%20Protecting%20Your%20Enterprise%20from%20AirSnitch%20Attacks&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fair-snitch-enterprise-wireless-attacks%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fair-snitch-enterprise-wireless-attacks%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fair-snitch-enterprise-wireless-attacks%2F&title=When%20Wi-Fi%20Encryption%20Fails:%20Protecting%20Your%20Enterprise%20from%20AirSnitch%20Attacks "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fair-snitch-enterprise-wireless-attacks%2F&text=When%20Wi-Fi%20Encryption%20Fails:%20Protecting%20Your%20Enterprise%20from%20AirSnitch%20Attacks "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fair-snitch-enterprise-wireless-attacks%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=When%20Wi-Fi%20Encryption%20Fails:%20Protecting%20Your%20Enterprise%20from%20AirSnitch%20Attacks%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fair-snitch-enterprise-wireless-attacks%2F "Share in Mastodon")



## Executive Summary

Enterprises have long trusted Wi-Fi encryption and client isolation to secure their wireless infrastructure. However, we conducted research presented at the NDSS Symposium 2026 that reveals that these safeguards can be breached by a novel set of attack techniques that we call AirSnitch. These techniques exploit subtle security issues in protocol-infrastructure interactions to undermine the security guarantees offered by standard protocols like WPA2 and WPA3-Enterprise.

Due to the widespread adoption of these protocols, the impact is industry-wide, affecting Wi-Fi devices from several major vendors. Major operating systems, including Android, macOS, iOS, Windows and Ubuntu Linux, also rely on these protocols.

WPA2 and WPA3-Enterprise protocols authenticate and encrypt most global IEEE 802.11 wireless traffic. They act as the primary cryptographic barrier for legacy cleartext application-layer protocols (e.g., DNS, HTTP), preventing unauthorized packet interception at the data link layer (Layer 2) of the [OSI model](https://www.ibm.com/think/topics/osi-model).

However, AirSnitch breaks this barrier. Unlike more commonly known threats, AirSnitch focuses on exploiting the wireless infrastructure itself rather than just client devices, fundamentally shifting our assumptions of wireless security. By subverting how networks handle low-level states (e.g., the MAC address table), attackers can break client isolation to intercept traffic or inject packets, completely bypassing Wi-Fi encryption.

This creates a critical risk to enterprise data confidentiality, potentially exposing sensitive credentials and backend systems to both malicious insiders and external over-the-air attackers. These security issues exist within the core logic of how Wi-Fi handles data. As a result, they represent a fundamental security gap that undermines protections across all Wi-Fi encryption standards, from the original WEP algorithm to modern WPA2/3 protection. This security gap stems from two primary factors: some attacks, such as Port Stealing, exploit fundamental Wi-Fi design errors that are difficult or impossible to patch within the existing protocol standards, necessitating the conservative treatment of these protocols as inherently insecure. Additionally, other exploits, like Gateway Bouncing, rely on diverse, organization-specific network configurations, making universal vendor testing and coordinated responsible disclosure impractical. Therefore, these findings are being released publicly to accelerate threat mitigation and security improvement across all impacted enterprises.

Importantly, AirSnitch also serves as a foundational building block for more sophisticated higher-layer attacks. By compromising the integrity of the lower protocol layers, an attacker can launch complex exploits against the upper protocol layers that were previously thought to be shielded by WPA.

Our research on AirSnitch leads us to urge the Wi-Fi industry to adopt rigorous, standardized security for complex modern Wi-Fi networks.

To counter these pervasive risks within individual organizations, security professionals must move beyond the assumption that WPA2/3-Enterprise provides robust protection. This article provides a concise overview of the attack mechanisms and offers actionable mitigation steps. Key defense steps include implementing robust network segmentation, enhancing spoofing prevention and updating firewall configurations to protect the integrity of both wired and wireless enterprise environments.

Palo Alto Networks customers are better protected from AirSnitch attacks discussed in this post with the following products and services:

  * [Next-Generation Firewall (NGFW)](https://www.paloaltonetworks.com/network-security/next-generation-firewall)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Network Security](https://unit42.paloaltonetworks.com/tag/network-security/), [MitM](https://unit42.paloaltonetworks.com/tag/mitm/)**  
---|---  
  
## The AirSnitch Threats: A New Security Paradigm

For years, the standard Wi-Fi threat model focused on an attacker targeting a single device or a specific network segment (e.g., basic service set identifier (BSSID)/service set identifier (SSID)). AirSnitch attacks challenge this assumption with a more multifaceted approach. These attacks:

  * Operate across different wireless network segments (basic service set (BSS))
  * Engage multiple access points (APs)
  * Can collude with malicious remote servers.



AirSnitch attacks exploit security issues across Wi-Fi encryption, switching and routing layers. These attacks manipulate underlying network states such as interface port (OSI Layer 1) mappings, to bypass Wi-Fi client isolation and encryption.

Unlike previous styles of attacks (e.g., address resolution protocol ([ARP) poisoning](https://www.okta.com/identity-101/arp-poisoning/)), AirSnitch works at even lower networking layers and restores meddler-in-the-middle (MitM) capabilities in current Wi-Fi networks. This effectively breaks the security perimeter that enterprises rely on, making even a properly configured WPA2/3-Enterprise network vulnerable to insider and outsider threats.

The threat model in AirSnitch differs from a typical Wi-Fi threat model, where a wireless attacker tries to compromise a single SSID/BSSID. AirSnitch takes into consideration all possible sources of attacks, and even how different attackers cooperate to inject or leak wireless traffic protected by WPA2/3.

As shown in Figure 1, an attacker can:

  * Deliver frames directly over the air to the victim (①)
  * Attempt to inject packets to the victim through the same AP (②) 
    * From within the network (③)
    * Through a different AP (④)
  * Launch attacks from the internet (⑤)

![A diagram comparing two threat models. The "Traditional Threat Model" depicts a router connected to a masked figure icon labeled "Malicious Actor." The "AirSnitch Threat Model" shows various interconnected components, including a globe, router, and multiple masked figure icons labeled "Malicious Actor," each with numbered connections indicating different threat paths.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-96430-178804-1.png)Figure 1. The classic Wi-Fi threat model versus the threat model in AirSnitch.

AirSnitch is the first public research to propose all five attack channels.

## The Anatomy of AirSnitch Attacks: Starting With Wi-Fi Fundamentals

AirSnitch attacks circumvent standard Wi-Fi security by exploiting weaknesses in the interplay between encryption, switching and routing layers, despite WPA2/3 encryption being designed to secure over-the-air traffic. Below, we begin by analyzing Wi-Fi fundamentals to demonstrate how WPA2/3 can be broken.

### Injecting and Decrypting Packets by Misusing Shared Keys

In the classic [WPA four-way handshake](https://web.stanford.edu/class/cs259/WWW04/projects/project04/04%20-%20Slides.pdf), a client blends AP and client randomness (i.e., nonces exchanged over the air) with the Pairwise Master Key (PMK) to derive the unicast session's Pairwise Transient Key (PTK). In WPA2-Personal, the client PMK is derived from the Wi-Fi passphrase. Thus, for WPA2-Personal networks, possession of a shared passphrase (common in public settings like restaurants and coffee shops) allows a [meddler-on-the-side](https://www.sophos.com/en-us/blog/Own-the-Router-Own-the-Traffic) attacker to derive session keys, just as legitimate clients do. This allows an attacker to passively decrypt and inject traffic, breaking client isolation.

Due to the [Dragonfly handshake](https://wpa3.mathyvanhoef.com/) added right before the four-way handshake, meddler-on-the-side attacks are no longer effective for the WPA3-Personal protocol. However, if attackers know the WPA3 passphrase, they can still set up a fake or cloned WPA3-Personal AP and then lure clients to this cloned AP. This would allow them to bypass client isolation on real APs to capture victim traffic. These attack methods reveal that keeping WPA2/3-Personal passphrases confidential is key to enforcing Wi-Fi client isolation.

The WPA four-way handshake also distributes the AP Group Temporal Key (GTK) to clients under the same BSSID, according to the Wi-Fi standard. The purpose of distributing GTK is to enable broadcast/multicast communications. However, we found that even for WPA2/WPA3-Enterprise networks, an insider attacker can misuse the shared GTK to wrap unicast IP traffic inside broadcast/multicast frames encrypted with the GTK. This enables an attacker to inject packets directly to victims, bypassing client isolation on target enterprise APs.

To better illustrate this, Figure 2 shows that, as a symmetric key, GTK is always shared between WPA clients and the AP. It is also distributed to clients during the classical WPA four-way handshake. Normally, client operating systems are responsible for managing this GTK. Normal applications won’t (and shouldn’t) know this shared GTK.

![A diagram of a Wi-Fi network showing a router labeled "SSID: Test" connected to three clients: a smartphone, a computer, and a tablet, each with a yellow key icon.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-98501-178804-2.png)Figure 2. GTK is shared among the AP and clients connected to the same BSSID.

However, the publicly available AirSnitch tool intentionally extracts this GTK by modifying the internal workings of wpa_supplicant, an open-source Wi-Fi client. As a result, a malicious client can bypass OS restrictions and obtain GTKs. After this, the attacker can spoof broadcast/multicast frames like APs do, by encrypting spoofed frames with GTK.

While some security-aware implementations enforce per-client GTKs to prevent shared GTKs and maximize isolation, certain Wi-Fi standard handshakes (group key, FT, FILS, WNM-Sleep) still expose the real GTK. Moreover, Integrity GTKs (IGTKs, another shared group key for management purposes) are never randomized. This enables an attacker to choose a GTK for a victim to use, also enabling packet injections. For a more in-depth analysis of these techniques within the Wi-Fi standard, you can refer to [our academic publication](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf).

## The Broader Context of Wi-Fi Client Isolation

To further understand how AirSnitch bypasses client isolation, it's important to grasp the broader context of Wi-Fi client isolation. Client isolation is a set of mechanisms designed to block direct communication between clients on the same Wi-Fi network. However, client isolation is not a standardized feature of the IEEE 802.11 standards, leading to unclear security guarantees.

Our [research](https://www.ndss-symposium.org/wp-content/uploads/2026-f1282-paper.pdf) identifies four typical, yet often flawed, mechanisms used for client isolation:

  * **Wi-Fi encryption protocols** (e.g., WEP, TKIP, CCMP, GCMP) are intended to prevent decryption of other clients' over-the-air traffic. For example, Wi-Fi encryption protocols prevent one mobile client from directly monitoring another's cleartext wireless traffic over the air. Such encryption also protects important unencrypted protocols, including HTTP and DNS.
  * **Intra-BSSID isolation** drops frames that are sent directly between clients on the same BSSID. In most AP configurations and the open-source hostapd Wi-Fi daemon, this is referred to as ap_isolate=1.
  * **Inter-BSSID isolation** blocks traffic between clients on different BSSIDs within the same network. For instance, ideally, a 2.4GHz BSSID of a Wi-Fi AP should not connect internally to a 5GHz BSSID on the same AP to provide robust client isolation. However, our research shows this is often not the case.
  * **Guest network configurations** assign untrusted clients to separate, restricted SSIDs, forcing them to use guest credentials to connect. However, these often fail to provide complete isolation. For example, many enterprises often deploy guest SSIDs with no encryption at all (i.e., Open System authentication), or weak encryption (i.e., passphrase authentication), along with WPA2/3-Enterprise for privileged employees. We show that those guest SSIDs, without sound client isolation, might allow attackers to harm privileged employees’ WPA2/3-Enterprise connections.



The core issue is that many vendors only implement a subset of these mechanisms, or they implement them incorrectly. For example, isolation might be enforced at the MAC layer (OSI Layer 2, with ap_isolate=1) but not the IP layer (OSI Layer 3), creating a bypass with “Gateway Bouncing” as we illustrate below.

## One Step Further: Dissection of Selected Novel MitM Primitives in AirSnitch

AirSnitch introduces several novel MitM primitives that exploit the often incomplete client isolation. We illustrate three of them:

  * Gateway bouncing
  * Port stealing
  * Broadcast reflection



### Gateway Bouncing

Attacks can use gateway bouncing to exploit the failure to enforce isolation at the IP layer in home and enterprise networks. An attacker sends a packet with the victim's Layer 3 IP address as the destination but uses the network gateway's MAC address as the Layer 2 destination. The AP accepts and forwards the packet to the gateway, which then routes it to the victim. This process effectively bypasses Layer 2 isolation, such as ap_isolate=1 in hostapd on Wi-Fi APs.

As shown in Figure 3, even with ap_isolate=1 enabled on both AP1 and AP2, AP1 forwards the injected packet because it sees the router as the Layer 2 destination. The router then identifies the packet's IP destination address on the AP2 side and bounces the packet to AP2, ultimately reaching the victim.

![A flow chart showing a network attack scenario. It includes an attacker device connected to AP1 \(access point 1\), which is connected to a router. The router connects to AP2 \(access point 2\) and then to a victim device. Arrows indicate the flow of network packets between the entities.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-100233-178804-3.png)Figure 3. Flow chart of an attacker exploiting the routing infrastructure to inject packets toward a victim.

### Port Stealing

An attacker can use port stealing to spoof a victim's MAC address toward a different BSSID of the same AP (see Figure 4 below), or toward a separate AP within the same wireless/wired infrastructure.

![A diagram showing two types of port stealing. On the left, the diagram shows data flow from a cloud to an AP, then to a hacker figure, bypassing a user. On the right, the diagram displays data flow reversed from a user to an AP, then diverting to the hacker figure before reaching the cloud.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-101937-178804-4.png)Figure 4. Flow charts of downlink and uplink port stealing in Wi-Fi networks.

The network's internal switches or APs will then mistakenly update their forwarding tables (i.e., Layer 1 interface port-to-MAC-address mappings), associating the victim's MAC address with the BSSID the attacker is exploiting. As a result, all traffic meant for the victim is redirected to the attacker's device and encrypted with the attacker's session key (i.e., PTK). This is also effective for hijacking uplink traffic by spoofing the MAC address of the gateway itself toward the wireless AP.

  * Importantly, without inter-BSSID isolation on a target AP, an attacker can spoof the gateway MAC address on a different BSSID. This allows them to intercept the first RADIUS/UDP authentication packet generated by the victim’s AP daemon. This allows an attacker to brute force and learn the victim's BSSID’s RADIUS secret, further compromising enterprise Wi-Fi security.
  * Wi-Fi port stealing compromises Wi-Fi security at a networking layer below ARP, operating between the physical layer (Layer 1) and the data link layer (Layer 2). This means that all unencrypted networking protocols carried by Wi-Fi, such as ARP, DNS, TCP and HTTP, can fall victim to Wi-Fi port stealing. Even encrypted protocols like TLS can expose IP addresses through port stealing.



### Broadcast Reflection

Broadcast reflection is a subtle injection method that bypasses the need for an attacker to know or predict the GTK. The attacker crafts a Wi-Fi frame that looks like a broadcast but contains a unicast IP layer payload for the victim. Upon receiving the broadcast frame, the AP re-encrypts it with the GTK associated with the victim's BSSID and broadcasts it to all clients, including the victim. This allows the attacker to inject traffic from a completely separate BSSID, without knowing the GTK for a target BSSID (see Figure 5 below).

![A diagram showing a network setup. An AP connects to two bands: 2.4G, with an icon blocking a suspicious individual, and 5G, linking to a smartphone, desktop, and monitor.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-103681-178804-5.png)Figure 5. Broadcast reflection allows an attacker to inject IP packets from a different BSSID on the same AP.

Our full paper also introduces other techniques that facilitate the manipulation of low-level port states within the target Wi-Fi network. As a result, an attacker can actively decrypt WPA2/3-Enterprise traffic and become a MitM, intercepting bi-directional traffic (i.e., both to and from a Wi-Fi client).

## Putting It Together: Chaining Primitives, Executing Cross-AP Attacks and Enabling Higher-Layer Attacks

A key insight of our AirSnitch research is its demonstration of combining different attack primitives into MitM attack chains. For example, an attacker might first use port stealing to intercept downlink traffic meant for a victim, and then apply GTK misuse to directly inject those stolen frames over the air to the victim.

Our research even reveals the possibility of cross-AP attacks. In this scenario, the attacker targets a Wi-Fi AP located at a different physical location than the victim to leak traffic belonging to the victim. This escalates the threat beyond traditional local attacks, as it breaks the assumption that physically separate APs provide effective isolation.

By hijacking MAC-to-port mappings at the distribution switch level (i.e., internal wired switches of enterprise networks), an attacker can manipulate traffic across AP boundaries even if those APs are broadcasting different network names (SSIDs). For example, Figure 6 shows that without strict isolation, an attacker could exploit a faraway AP’s guest SSID to steal WPA2/3-Enterprise traffic belonging to a client located inside an office building.

![A person in an office building is visibly frustrated while using a laptop connected to "Internal Wi-Fi Client." A diagram shows a connection between the laptop and a "WPA2/3-Enterprise WLAN," which links to a distant "Faraway AP \(Guest SSID\)" on a telecommunications tower. Nearby, a cloaked figure holds a device, suggesting they are accessing the network.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/word-image-105479-178804-6.png)Figure 6. An attacker can exploit a faraway AP to steal traffic from a Wi-Fi client inside a protected building.

Once an attacker establishes a bi-directional MitM through these methods, they can facilitate higher-layer attacks that were previously thought impractical in isolated networks. These possibilities include:

  * **Rogue enterprise APs:** In enterprise settings, attackers can steal RADIUS packets to brute force RADIUS authentication passphrases, eventually setting up rogue enterprise access points to harvest secret data.
  * **Traffic decryption:** Attackers can exploit vulnerabilities in unpatched Datagram TLS (DTLS) implementations to decrypt HTTPS connections and compromise sensitive user data. Wi-Fi port stealing also serves as a powerful primitive to more sophisticated attacks, such as traffic analysis.
  * **Address poisoning:** By decrypting Wi-Fi, an adversary can perform DNS or DHCP poisoning, modifying gateway addresses or poisoning ARP caches to maintain long-term control over the victim's traffic.



## How to Mitigate the AirSnitch Attacks for Enterprise Wi-Fi Networks

To protect against AirSnitch attacks, enterprises must move beyond simple, vendor-specific client isolation settings and adopt a more holistic security approach.

We suggest a simple security checklist before introducing more specialized solutions:

  1. Does your enterprise strictly separate guest SSIDs from WPA2/3-Enterprise SSIDs on Wi-Fi APs?
  2. Does your enterprise ever use firewall policies in core networks to provide network isolation between guest Wi-Fi and WPA2/3-Enterprise, and block attacks including gateway bouncing?
  3. Does your enterprise use weak RADIUS passphrases on Wi-Fi APs?
  4. Does your enterprise update endpoint operating systems to newer, patched versions?
  5. Does your enterprise use robust, secure virtual private network (VPN) solutions for even intranet access?
  6. Does your enterprise harbor legacy or orphaned APs that remain physically uplinked to the core network despite being phased out of active management?



Our AirSnitch research also suggests more specialized solutions to nullify the attacks:

  * **Improve network isolation with virtual local area networks (VLANs)**. Implement VLANs to logically separate network segments. Placing untrusted BSSIDs (e.g., guest networks) in their own VLAN prevents an attacker from launching port-stealing attacks to redirect traffic from a trusted network.
  * **Implement spoofing prevention**. 
    * **MAC spoofing** : Configure APs to prevent a single MAC address from being used on multiple BSSIDs simultaneously. This feature, seen on certain devices, directly prevents the cross-BSSID port-stealing attacks.
    * **IP spoofing** : Enable IP spoofing prevention to block traffic where the source IP address does not belong to the sender. This defense can stop gateway bouncing by preventing the attacker from injecting packets that appear to originate from an external server.
  * Enhance group key security. You can stop GTK misuse attacks by configuring APs to use per-client randomized GTKs. The [Passpoint (Hotspot 2.0) specification](https://wballiance.com/passpoint-feature-user-format/) includes a mechanism called downstream group-addressed forwarding (DGAF), which allows access points to control or disable forwarding of multicast/broadcast traffic to clients. This is important because such traffic typically relies on a shared group key (GTK), that could introduce potential attack vectors. By disabling downstream group-addressed forwarding, APs can prevent these risks and, in some implementations, convert essential group traffic into unicast transmissions per client. Examine whether your enterprise APs support these options.
  * **Adopt device-to-device encryption**. For better security, use a protocol like **MACsec (IEEE 802.1AE)**. MACsec establishes secure, end-to-end encryption at the link layer between devices. This ensures that even if an attacker manages to intercept traffic, they cannot read or tamper with it. At most, they can cause a denial of service. This option is available on Linux distributions like Ubuntu.



## Conclusion

The AirSnitch attacks illustrate a fundamental fact about modern Wi-Fi networks. Client isolation, as currently implemented, is an inconsistent and unreliable defense.

The lack of standardization has led to ad hoc and incomplete solutions that fail to protect against sophisticated insider and outsider threats. By exploiting security issues across the encryption, switching and routing layers, an attacker can achieve a full MitM position, even in enterprise-grade networks. Our research on AirSnitch leads us to urge the Wi-Fi industry to adopt rigorous, standardized security for complex modern Wi-Fi networks.

### Palo Alto Networks Protection and Mitigation

[Next-Generation Firewall (NGFW)](https://docs.paloaltonetworks.com/ngfw) is designed to prevent known and unknown threats, block exploits and enforce granular security policies.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107
  * South Korea: +82.080.467.8774



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Indicators of Compromise

  * Unexpected changes in MAC address-to-port mappings within the AP's forwarding table
  * Detection of an attacker device with a spoofed MAC address of a legitimate client or gateway
  * High volume of multicast/broadcast frames containing unexpected unicast payloads, especially from internal Wi-Fi clients
  * Unexpected re-negotiation of session keys or GTK updates outside of standard periodic intervals



## Additional Resources

  * [AirSnitch: Demystifying and Breaking Client Isolation in Wi-Fi Networks](https://www.ndss-symposium.org/ndss-paper/airsnitch-demystifying-and-breaking-client-isolation-in-wi-fi-networks/) \- Network and Distributed System Security (NDSS) Symposium



Back to top

### Tags

  * [AirSnitch](https://unit42.paloaltonetworks.com/tag/airsnitch/ "AirSnitch")
  * [MitM](https://unit42.paloaltonetworks.com/tag/mitm/ "MitM")
  * [Network security](https://unit42.paloaltonetworks.com/tag/network-security/ "network security")
  * [Port stealing](https://unit42.paloaltonetworks.com/tag/port-stealing/ "port stealing")
  * [WiFi encryption](https://unit42.paloaltonetworks.com/tag/wifi-encryption/ "WiFi encryption")
  * [Wireless](https://unit42.paloaltonetworks.com/tag/wireless/ "wireless")
  * [WPA2](https://unit42.paloaltonetworks.com/tag/wpa2/ "WPA2")
  * [WPA3](https://unit42.paloaltonetworks.com/tag/wpa3/ "WPA3")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Fracturing Software Security With Frontier AI Models ](https://unit42.paloaltonetworks.com/ai-software-security-risks/ "Fracturing Software Security With Frontier AI Models")

### Table of Contents

  *   * Executive Summary
  * The AirSnitch Threats: A New Security Paradigm
  * The Anatomy of AirSnitch Attacks: Starting With Wi-Fi Fundamentals
    * Injecting and Decrypting Packets by Misusing Shared Keys
  * The Broader Context of Wi-Fi Client Isolation
  * One Step Further: Dissection of Selected Novel MitM Primitives in AirSnitch
    * Gateway Bouncing
    * Port Stealing
    * Broadcast Reflection
  * Putting It Together: Chaining Primitives, Executing Cross-AP Attacks and Enabling Higher-Layer Attacks
  * How to Mitigate the AirSnitch Attacks for Enterprise Wi-Fi Networks
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Indicators of Compromise
  * Additional Resources



### Related Articles

  * [ Know Ourselves Before Knowing Our Enemies: Threat Intelligence at the Expense of Asset Management ](https://unit42.paloaltonetworks.com/asset-management/ "article - table of contents")
  * [ Detecting Vulnerability Scanning Traffic From Underground Tools Using Machine Learning ](https://unit42.paloaltonetworks.com/machine-learning-new-swiss-army-suite-tool/ "article - table of contents")
  * [ Meddler-in-the-Middle Phishing Attacks Explained ](https://unit42.paloaltonetworks.com/meddler-phishing-attacks/ "article - table of contents")



## Related Malware Resources

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

![Pictorial representation of a magnifying glass illuminating a glowing orange circular digital circuit interface on a dark, high-tech background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) September 16, 2026 #### [Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS \(AMOS\) Stealer Activity")

![Pictorial representation of post-exploitation identity misuse in SPIFFE/SPIRE. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 10, 2026 #### [The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [Cryptographic](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")

![Pictorial representation of a pay-per-install threat group campaign prodiving infection service for spreading malware. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip, symbolizing data processing and transfer. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 9, 2026 #### [Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

  * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")
  * [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")
  * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")

![Pictorial representation of attackers using AI tools to target Latin American organizations. A vibrant cityscape with silhouettes of numerous people walking along a bustling street. The scene is illuminated by bright urban lights and digital-like particles, creating a dynamic and futuristic atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2026 #### [Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")

![Pictorial representation of vishing campaigns in Microsoft Teams. A digital image of a skull formed by blue binary code on a black background, with scattered ones and zeros and digital noise, symbolizes how stealthy prompt injection attacks can exploit AI logic to bypass security controls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 31, 2026 #### [Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

  * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")

![Pictorial representation of AI-enabled malware. A vibrant digital interface displaying various icons and graphs, resembling a futuristic network or data analysis dashboard. The scene is illuminated with glowing lights and patterns.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 25, 2026 #### [The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

  * [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")
  * [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
  * [DLL hijacking](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")

![Pictorial representation of identity abuse through trusted communication channels. Close-up view of a digital screen displaying a glitched and pixelated image of a skull-like shape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 20, 2026 #### [Identity Abuse Through Trusted Communication Channels ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

  * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")
  * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

![Pictorial representation of a magnifying glass illuminating a glowing orange circular digital circuit interface on a dark, high-tech background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) September 16, 2026 #### [Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS \(AMOS\) Stealer Activity")

![Pictorial representation of post-exploitation identity misuse in SPIFFE/SPIRE. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 10, 2026 #### [The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [Cryptographic](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")

![Pictorial representation of a pay-per-install threat group campaign prodiving infection service for spreading malware. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip, symbolizing data processing and transfer. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 9, 2026 #### [Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

  * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")
  * [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")
  * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")

![Pictorial representation of attackers using AI tools to target Latin American organizations. A vibrant cityscape with silhouettes of numerous people walking along a bustling street. The scene is illuminated by bright urban lights and digital-like particles, creating a dynamic and futuristic atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2026 #### [Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")

![Pictorial representation of vishing campaigns in Microsoft Teams. A digital image of a skull formed by blue binary code on a black background, with scattered ones and zeros and digital noise, symbolizes how stealthy prompt injection attacks can exploit AI logic to bypass security controls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 31, 2026 #### [Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

  * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")

![Pictorial representation of AI-enabled malware. A vibrant digital interface displaying various icons and graphs, resembling a futuristic network or data analysis dashboard. The scene is illuminated with glowing lights and patterns.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 25, 2026 #### [The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

  * [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")
  * [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
  * [DLL hijacking](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")

![Pictorial representation of identity abuse through trusted communication channels. Close-up view of a digital screen displaying a glitched and pixelated image of a skull-like shape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 20, 2026 #### [Identity Abuse Through Trusted Communication Channels ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

  * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")
  * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/air-snitch-enterprise-wireless-attacks/)