# R7-2014-17: NAT-PMP Implementation and Configuration Vulnerabilities | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2014/10/21/r7-2014-17-nat-pmp-implementation-and-configuration-vulnerabilities/
- **Date :** 2025-06-02

---

## Overview

In the summer of 2014, Rapid7 Labs started scanning the public Internet for NAT-PMP as part of [Project Sonar](https://community.rapid7.com/community/infosec/sonar). NAT-PMP is a protocol implemented by many SOHO-class routers and networking devices that allows firewall and routing rules to be manipulated to enable internal, assumed trusted users behind a NAT device to allow _external_ users to access internal TCP and UDP services for things like Apple's Back to My Mac and file/media sharing services. NAT-PMP is a simplistic but useful protocol, however the majority of the security mechanisms rely on proper implementation of the protocol and a keen eye on the configuration of the service(s) implementing NAT-PMP. Unfortunately, after performing these harmless scans across UDP port 5351 and testing theories in a controlled lab environment, it was discovered that 1.2 million devices on the public Internet are potentially vulnerable to flaws that allow interception of sensitive, private traffic on the internal and external interfaces of a NAT device as well as various other flaws.

No CVEs have been assigned for any of these, however CERT/CC has been involved and allocated [VU#184540](http://www.kb.cert.org/vuls/id/184540).

## Vulnerability Summary

During our research, we identified approximately 1.2 million devices on the public Internet that responded to our external NAT-PMP probes. Their responses represent two types of vulnerabilities; malicious port mapping manipulation and information disclosure about the NAT-PMP device. These can be broken down into 5 specific issues, outlined below:

  * Interception of Internal NAT Traffic: ~30,000 (2.5% of responding devices)
  * Interception of External Traffic: ~1.03m (86% of responding devices)
  * Access to Internal NAT Client Services: ~1.06m (88% of responding devices)
  * DoS Against Host Services: ~1.06m (88% of responding devices)
  * Information Disclosure about the NAT-PMP device: ~1.2m (100% of responding devices)



In [RFC 6886](https://tools.ietf.org/html/rfc6886), it states:

The NAT gateway MUST NOT accept mapping requests destined to the NAT gateway's external IP address or received on its external network interface. Only packets received on the internal interface(s) with a destination address matching the internal address(es) of the NAT gateway should be allowed.

This is a critical requirement given that the source IP address of incoming NAT-PMP messages is what is used to create the mappings as stated in RFC 6886:

The source address of the packet MUST be used for the internal address in the mapping.

The root cause of these issues is that some vendors are violating these portions of the RFC.

## What is NAT-PMP?

NAT-PMP is a simple UDP protocol used for managing port-forwarding behavior of NAT devices. While it has been around since approximately 2005, it was formally defined in [RFC 6886](https://tools.ietf.org/html/rfc6886), which was pushed largely by Apple in 2013 as a better replacement for the Internet Gateway Device (IGD) Standard Device Control Protocol, a part of UPnP. NAT-PMP clients and libraries are available for nearly all operating systems and platforms. NAT-PMP servers are similarly available. An unknown but likely large portion of servers, and perhaps less so for clients, are based on [miniupnp](https://miniupnp.free.fr/).

To understand what NAT-PMP does and why the vulnerabilities we will describe are both real and significant, you must first understand how NAT-PMP works.

NAT-PMP is designed to be deployed on NAT devices assumed to have at least two network interfaces, one listening on a private, often RFC1918 network and another on a public, generally Internet-facing network. Clients behind the NAT device may wish to expose local TCP or UDP services to hosts on the public network (again, usually Internet) and can use NAT-PMP to achieve this.

Assume the following setup:

![nat-pmp.png](https://www.rapid7.com/cdn/images/blta02beabae4484c93/683de4262a768643b7bc856d/nat-pmp.png)

While it is absolutely possible to use different setups, for example with all private addresses, all public addresses, etc, NAT-PMP was designed to be deployed similar to what is shown above. Even in these nonstandard deployments, however, many of the same security vulnerabilities may still exist.

NAT-PMP really offers only two types of operations:

  * Obtain the external address of the NAT-PMP device
  * Establish mappings of a TCP or UDP port such that a service on the private network can be reached from the public Internet and then subsequently destroy this mapping



To achieve this, a NAT-PMP implementation needs to know:

  * Its external IP address, which is ultimately where hosts on the public Internet will try to connect to mapped TCP and UDP ports
  * Where to listen for NAT-PMP messages



Using the setup described earlier, if private client 192.168.0.2 wants to allow hosts on the public Internet to connect to a game server it is hosting on 192.168.0.2:1234/UDP, the following (simplified) messages are exchanged:

  1. Client requests "Please map UDP port 1234 from the outside to my UDP port 1234"
  2. The NAT device responds with either:  

     * "OK, port 1234/UDP has been forwarded to your port 1234/UDP", if the exact mapping was possible
     * "OK, port 5678/UDP has been forwarded to port 1234/UDP", if the exact match wasn't possible but another was; in this case NAT-PMP has chosen port 5678 instead
  3. Client requests "What is your public IP address?"
  4. NAT device responds "My public IP address is a.b.c.d"



Now the client can advertise a.b.c.d:1234/UDP as a way for hosts from the public Internet to connect to the server it is running.

Exactly how this is achieved under the hood of a NAT-PMP device depends on the implementation, but generally it interacts directly with the firewall, routing, and/or NAT capabilities of the NAT-PMP device and inserts new rules to allow the traffic to flow. For example, on Linux implementations of NAT-PMP, iptables or ipchains are often used, ipfw is used on OS X and derivatives, etc. The resulting traffic flow would look like:
    
    
    external client -> a.b.c.d:1234/UDP -> 192.168.0.1:1234/UDP
    

The destination address of the resulting traffic flow corresponds to the IP address of the client that requested the mapping.

It is important to note that the traffic flows created here are meant to control how traffic _**to the external address**_ is handled. Furthermore, it is important to understand that the external address is not necessarily the public/external address of the NAT-PMP device, but rather what the NAT-PMP device _thinks_ it is. In a properly deployed setup, however, the external address as reported by NAT-PMP will be identical to the public/external IP address of the device.

## Security Features

NAT-PMP is designed to be simple, lightweight and used only on networks where the clients are reasonably trusted, and as such there are no security capabilities currently built into the protocol itself. In fact, the RFC goes as far as to say that if you care, use IPsec.

Many NAT-PMP implementations, however, offer capabilities that may include:

  * Restricting what networks/interfaces it will listen on and respond on for NAT-PMP messages
  * Restricting what clients can forward to/from using IP address, port and protocol restrictions



## Vulnerability Details

## Malicious NAT-PMP Port Mapping Manipulation

When improperly configured to listen for and respond to NAT-PMP messages on an untrusted interface, in the absence of ACLs controlling what clients can forward, attackers can create malicious NAT-PMP port mappings that can allow:

  * Interception of TCP and UDP traffic from internal, private NAT clients destined to the internal, private address of the NAT-PMP device itself. This can allow for interception of sensitive internal services such as DNS and HTTP/HTTPS administration.
  * Interception of TCP and UDP traffic from external hosts to the external address of the NAT-PMP device or the private NAT clients.
  * Access to services provided by clients behind the NAT device by spoofing NAT-PMP port mapping requests
  * DoS against the NAT-PMP device itself by requesting an external port mapping for a UDP or TCP service already listening on that port, including the NAT-PMP service itself.



We will now explore each of these in a little more depth.

### Interception of Internal Traffic

If a NAT-PMP device is incorrectly configured and sets its NAT-PMP external interface to be the _internal_ interface that the NAT clients use as their gateway and listens for NAT-PMP messages on both the internal and external interfaces, it is possible for remote attackers from **outside** to intercept arbitrary TCP and UDP traffic destined _to_ (**not** _through_) the NAT-PMP device's internal interface _from_ internal NAT clients. In this attack, traffic destined to the NAT-PMP device's internal interface is forwarded out of the NAT network to an external attacker, and would likely target a service that could be leveraged for further exploitation, such as DNS or HTTP/HTTPS administrative services on the NAT-PMP device itself.

To demonstrate this, a NAT-PMP implementation running on a Linux system has been installed with iptables and two interfaces -- one external, listening on the public internet with address 192.0.2.1 (thanks, [RFC 5737](http://tools.ietf.org/html/rfc5737)!) and another internal, listening on 172.16.0.1 from [RFC1918](http://tools.ietf.org/html/rfc1918) space. This device is purposely misconfigured, listens on all addresses for NAT-PMP, and incorrectly set miniupnpd's external interface to be the internal interface. This system also hosts a simple HTTP administration page for internal use only, as seen when browsing to http://172.16.0.1:

![1-1.png](https://www.rapid7.com/cdn/images/blt11e5ecd53be9ef3d/683de44aabf2ad10703c44ff/1-1.png)

Then, utilizing Metasploit's [natpmp_map](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/admin/natpmp/natpmp_map.rb) module, we attack the external, public address and establish a mapping to intercept the HTTP administration requests, forwarding 80/TCP on the NAT-PMP device to our IP address:

![1-2.png](https://www.rapid7.com/cdn/images/blt15039f55c73f64c1/683de4773beff092bba7c577/1-2.png)

Inspecting the firewall rules on the target, we can see that firewall rules were established that _should_ forward any HTTP traffic destined to the NAT-PMP device's internal address, 172.16.0.1, to our IP, 192.0.2.100 :

![1-4.png](https://www.rapid7.com/cdn/images/blt429b2710ba5a537e/683de4aada5c3097d6a835e6/1-4.png)

Finally, we confirm this by navigating to http://172.16.0.1 again. Notice that the login is now different ("HOME NAT Interception"):

![1-3.png](https://www.rapid7.com/cdn/images/blt5629df5831b5cafc/683de4d4237ea60be191c394/1-3.png)

To take this even further, oftentimes NAT clients are configured to utilize their NAT device as their DNS server. By establishing a mapping for DNS that redirects to a malicious host, we can control DNS responses and use this to launch further attacks against the NAT clients, including client-side attacks. First, we establish the mapping for DNS on 53/UDP:

![dns.png](https://www.rapid7.com/cdn/images/blt1c56d406869a0bf2/683de50bbc38b1aae3477e3e/dns.png)

Then, utilizing Metasploit's [fakedns](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/server/fakedns.rb) module, we reply with 1.2.3.4 for any requests for example.com's A record:

![1-7.png](https://www.rapid7.com/cdn/images/blt34ab40e5f6c4d6bb/683de52fcc6042641520690a/1-7.png)

Finally, showing that example.com now resolves the address we specified, 1.2.3.4:

![1-8.png](https://www.rapid7.com/cdn/images/blt38727ecd456d95d7/683de5534b2b7f4084e1628f/1-8.png)

By intercepting and controlling DNS requests for these private NAT clients, we can redirect arbitrary HTTP/HTTPS requests to arbitrary, assume malicious hosts on the public Internet which will allow all manner of further attack vectors.

### Interception of External Traffic

If a NAT-PMP device is _incorrectly_ configured, sets its NAT-PMP external interface to be the _external_ interface that faces the public Internet and listens for NAT-PMP messages on both the internal and external interfaces, it is possible for remote attackers from **outside** to intercept arbitrary TCP and UDP traffic destined from external hosts _to_ and perhaps _through_ the NAT-PMP device's external interface. In this attack, traffic destined to the NAT-PMP device's external interface is forwarded back out to the attacker, in effect bouncing requests from the NAT-PMP device's external interface to an attacker.

Devices vulnerable to this will report the external address to be something external, often the public IPv4 address on the Internet.

The attack scenarios are similar to the previous internal-targeted attack, however this time they would typically target services legitimately exposed externally. Target services could again include HTTP/HTTPS and other administrative services, except in this case the potential victim of the traffic intercept would be anyone trying to administer the device remotely, which could include ISPs who expose HTTP/HTTPS services to the world but protect it with a password.

This attack can also be used to cause the NAT-PMP device to respond to and forward traffic for services it isn't even listening on. For example, if the NAT-PMP device does _not_ have a listening HTTP service on the external interface, this same flaw could be used to redirect inbound HTTP requests to another external host, making it appear that HTTP content hosted on the external host is hosted by the NAT-PMP device.

### Access to Internal NAT Client Services

Because NAT-PMP utilizes the source IP address as the target to which traffic will be forwarded, as the previous two attack scenarios demonstrate it is critical to control where NAT-PMP listens for messages as well as what IP addresses are allowed to create mappings. If, however, ACLs exist that restrict which clients can create mappings but NAT-PMP is incorrectly configured to listen for NAT-PMP messages on an untrusted interface such was a WAN interface connected to the Internet, it is still possible to create mappings by spoofing NAT-PMP mapping requests, using a source address that matches a valid, internal network range served by the NAT-PMP device.

Practically speaking, this attack is considerably more difficult due to things like BCP38 and others that are used to thwart attacks that rely on spoofed source IP addresses.

### DoS Against Host Services

Taking the attack scenarios described in the first vulnerability, it is possible to turn them into DoS conditions against the NAT-PMP device itself by creating mappings for other services already listening on the NAT-PMP device, presumably internally. For example, using the same setup as in vulnerabilities 1-2, if we request a mapping for the NAT-PMP service itself, we can redirect any NAT-PMP messages to a host of our choosing, in turn preventing any further mappings from being created.

First, we act like a legitimate client on the private NAT network and request a forwarding for 1234/UDP, which works:

![4-1.png](https://www.rapid7.com/cdn/images/blt72994e95231bf885/683de57d2a76868294bc85c5/4-1.png)

Then, we attack from the outside and establish a bogus mapping for the NAT-PMP service itself:

![4-2.png](https://www.rapid7.com/cdn/images/blta141d4e682edb557/683de5a33d7b5ee50013679b/4-2.png)

Finally, we again act as a legitimate client on the private NAT network and against request a forwarding for 1234/UDP, which now fails:

![4-3.png](https://www.rapid7.com/cdn/images/blt6534135efb068717/683de5c6ca9dfc9edf5267e8/4-3.png)

## NAT-PMP Information Disclosure

If improperly deployed, NAT-PMP can disclose:

  * The "external address" if listening on the public Internet. This can often include an internal, RFC1918 address if the external interface is incorrectly set to the internal, private interface. Metasploit's [natpmp_external_address module](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/gather/natpmp_external_address.rb) can be used to demonstrate this.
  * The ports the NAT-PMP device is listening on without having to scan those ports directly. By requesting a mapping with an external port that corresponds to a port that the NAT-PMP device is already listening on, for example for another common NAT service such as DNS, HTTP/HTTP, SSH or Telnet, some NAT-PMP implementations most notably OS X, will respond in a positive manner but indicating that a different external port was used. Metasploit's [natpmp_portscan module](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/scanner/natpmp/natpmp_portscan.rb) can be used to demonstrate this.
  * Similarly, ports already forwarded or in use by another NAT client



These information disclosure vulnerabilities present relatively little risk, however in the spirit of even [disclosing research that doesn't result in huge security implications](/blog/post/2014/10/03/adventures-in-empty-udp-scanning/) I figured it was worth discussing them here. If nothing else, they are a fun exercise and may open future areas.

Now for some miscellany.

### External Address and Response Code Analysis

Using the first information disclosure and applying it to our Sonar data set, we discovered the following breakdown in terms of the types of external addresses returned:

  * 1,032,492 devices responded with an external IP address identical to the IP address Sonar contacted them on
  * 104,183 devices responded with status code 3 indicating that the NAT device itself hasn't received an IP address from DHCP, presumably on the truly internal network
  * 34,187 devices responded with 0.0.0.0, usually indicating that the other interface hasn't received an IP address yet
  * 24,927 devices responded with an RFC1918 address (10.0.0.0/8, 192.168.0.0/16 and 172.16.0.0/12 had 17810, 4139 and 3608 devices, respectively)
  * 7,400 devices responses were from a single ISP in Israel that responds to unwarranted UDP requests of any sort with HTTP responses from nginx. Yes, HTTP over UDP:



![http.png](https://www.rapid7.com/cdn/images/blt2280172ebe23175b/683de5eada5c30a045a83660/http.png)

  * 2,974 devices responded with an external address that wasn't identical to the IP address Sonar contacted it on, wasn't loopback or RFC1918, and wasn't in an obviously similar network
  * 1,037 devices responded with an external address allocated for Carrier Grade NAT (CGN) address space, a private space set aside for large-scale NAT deployments in [RFC6598](http://tools.ietf.org/html/rfc6598). Yes, there are 1037 "carrier grade" devices out there with an almost trivially exploitable gaping vulnerability allowing traffic interception. CGN is Inception-style NAT. NAT within NAT, because even ISPs have more customers than they do usable IPv4 space. Because each address in CGN in theory fronts hundreds, thousands or perhaps even more customers, each with their own RFC1918 networks with untold numbers of devices, the potential for impact here could be tremendous.
  * 845 devices responded with an external IP address different from the IP address Sonar contacted them on, but in the same /16
  * 240 devices responded with a loopback address in 127.0.0.0/8. Does this imply that we could intercept loopback traffic? Oh, the horrors.
  * 128 devices responded with an external IP address different from the IP address Sonar contacted them on, but in the same /24



### Side-channel Port Scanning

Using the second information disclosure issue above, you can gain a deeper understanding of these systems. For example, on an Apple Airport, using the second technique, we can discover all sorts of fun ports that are apparently used internally on the airport but don't appear to be open from the outside:

![map.png](https://www.rapid7.com/cdn/images/blt217fc7ad830caaa9/683de60a237ea674d691c3e4/map.png)

Some of these have obvious explanations, but others don't. What are these services? Why would the Airport not allow me to map some of these ports but the ports shows as closed in a portscan? Is the Airport actively using them? If so, _who_ can connect to them if it isn't me, the owner of the device?

### Are They Backwards?

If you think about how most SOHO-style routers/firewalls are built, they are generally some sort of embedded-friendly operating system, perhaps even a stripped-down Linux install, running a DHCP client on a WAN interface and a DHCP server on the internal interface(s). What if some number of the devices responding to NAT-PMP on the public Internet were simply cabled backwards, literally the WAN connection being plugged into the LAN port and vice versa? Could it really be that simple? Theoretically, if the devices firewalling/routing capabilities can handle any arbitrary WAN or LAN port asking for or serving DHCP leases, for example, but the NAT-PMP implementation couldn't, in effect every address on the public Internet is technically _behind_ these NAT devices and may have all of the NAT-PMP capabilities that legitimate clients in a proper NAT-PMP deployment would have, including, creating firewall and routing rules.

### Deep in the Bowels of Carrier Networks, Lurking RFC1918 Hipsters or Patterns of Problems

How often have you, for example, tracerouted through or to a particular network, only to see RFC1918 addresses show up in the responses? It definitely happens, and ISPs and other carriers have been known to utilize RFC1918 address space internally for all number of legitimate reasons. So, does this mean that these NAT-PMP responses with RFC1918 external addresses are coming from ISP and carrier equipment?

Or, are there really 568 people out there deciding "You know, using the first available address in this RFC1918 address space is too popular, I'm going to pick 10.11.14.2 for the address of my device"?

Or, are the hosts returning RFC1918 addresses in the NAT-PMP external address probes displaying patterns in the addresses themselves? For each of the 3 RFC1918 address spaces, we observed the following breakdown in terms of the top 5 addresses returned from each space:

#### 192.168.0.0/16

**NAT-PMP External Address**| **Count**  
---|---  
192.168.0.50| 784  
192.168.1.64| 334  
192.168.1.2| 152  
192.168.100.2| 118  
192.168.1.100| 40  
  
#### 10.0.0.0/8

**NAT-PMP External Address**| **Count**  
---|---  
10.11.14.2| 565  
10.10.10.10| 27  
10.0.0.3| 17  
10.0.0.4| 11  
10.10.14.2| 10  
  
#### 172.16.0.0/12

**NAT-PMP External Address**| **Count**  
---|---  
172.17.0.10| 11  
172.20.20.2| 10  
172.16.225.114| 3  
172.16.18.131| 3  
172.16.1.11| 3  
  
Using these popular addresses and a search engine, you'll very quickly find there may be particular devices that typically use these addresses -- for example if they come with a hard-coded RFC1918 address that must be changed.

### Country Analysis

Rather than looking at the external address reported by NAT-PMP, if you instead take the public IPv4 address that responded and look at the country and organization of origin, you start to seem some interesting results. A significant portion of the responses come from ISPs and telecom companies in large countries where the number of public IPv4 addresses allocated to that country is small relative to the number of people and devices looking for Internet access. Furthermore, a number of them are primarily mobile phone/data providers operating in areas where the easiest option to provide Internet access to its customers is to do it wirelessly in some way.

**Country**| **Responding IPs**  
---|---  
Argentina| 145866  
Russian Federation| 133126  
China| 119043  
Brazil| 110007  
India| 99168  
Malaysia| 89934  
United States| 64182  
Mexico| 50662  
Singapore| 49713  
Portugal| 18863  
  
## Affected Vendors

Incorrect miniupnp configurations are likely to blame for most occurrences of these issues as miniupnp is available for almost every platform that would ever connect to the Internet in some way. There are upwards of 1.2 million devices on the public Internet that exhibit signs of being vulnerable to one or more of the previously described vulnerabilities. To be clear, though, even though there are almost certainly miniupnp NAT-PMP instances out there that are vulnerable to the issues we are disclosing, these likely stem from misconfigurations of miniupnp rather than a flaw in miniupnp itself. Furthermore, it is likely that many of the vulnerable NAT-PMP instances are not based on miniupnp and may have more or different vulnerabilities.

During the initial discovery of this vulnerability and as part of the disclosure process, Rapid7 Labs attempted to identify what specific products supporting NAT-PMP were vulnerable, however that effort did not yield especially useful results. To attempt to identify these products, we used the results of Sonar's probes to identify misconfigured or misimplemented hosts and then correlated that with other data that Sonar collects. While things did seem promising at first when our correlation started hinting that the problem was widespread across dozens of products from a variety of vendors, upon acquiring a representative subset of these products and performing the testing in our lab we were unable to identify situations in which these products could be vulnerable to the NAT-PMP vulnerabilities discussed in this advisory. Furthermore, because of the technical and legal complexities involved in uncovering the true identity of devices on the public Internet, it is entirely possible, perhaps even likely, that these vulnerabilities are present in popular products in default or supported configurations.

Because of the potential impact of these vulnerabilities and the difficulty in identifying what products are vulnerable, Rapid7 Labs opted to engage CERT/CC to handle the initial outreach to potentially affected vendors and organizations.

## Conclusions

The vulnerabilities disclosed in this advisory are not theoretical, however how many devices on the public Internet are actually vulnerable to the more severe traffic interception issues is unknown. Vendors producing products with NAT-PMP capabilities should take care to ensure that flaws like the ones disclosed in this document are not possible in normal and perhaps even abnormal configurations. ISPs and entities that act like ISPs should take care to ensure that the access devices provided to customers are similarly free from these flaws. Lastly, for consumers with NAT-PMP capable devices on your network, you should ensure that all NAT-PMP traffic is prohibited on un-trusted network interfaces.

Thanks to Rapid7 for supporting this research, CERT/CC for assisting with coordinated, responsible disclosure, and [Austin Hackers Anonymous (AHA!)](http://takeonme.org/), where I initially presented some of the beginnings of this research back in 2011.

## Updates

  * 10/22/2014: CERT-CC informed us that the miniupnp project has taken measures to prevent most of the issues described here. In particular, NAT-PMP messages arriving on a WAN interface will now be logged and discarded ([commit 16389fda3c5313bffc83fb6594f5bb5872e37e5e](https://github.com/miniupnp/miniupnp/commit/16389fda3c5313bffc83fb6594f5bb5872e37e5e)) , the default configuration file must now be configured by anyone running miniupnp, and this file now has more commentary around the importance of selecting the correct external interface and ACLs for mappings ([commit 82604ec5d0a12e87cb5326ac2a34acda9f83e837](https://github.com/miniupnp/miniupnp/commit/82604ec5d0a12e87cb5326ac2a34acda9f83e837)).



## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)
  * [Labs](/blog/tag/labs/)