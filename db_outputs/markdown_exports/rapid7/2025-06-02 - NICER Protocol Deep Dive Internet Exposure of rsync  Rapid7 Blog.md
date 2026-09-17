# NICER Protocol Deep Dive: Internet Exposure of rsync | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/09/25/nicer-protocol-deep-dive-internet-exposure-of-rsync/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## rsync (873)

_Almost an accident of early internet engineering._

### TLDR

**WHAT IT IS:** Cleartext file/directory transfer service with or without [encrypted] authentication.

**HOW MANY:** 208,882 discovered nodes. 208,882 (100%) have Recog version fingerprints

**VULNERABILITIES:** The rsync service has had a few high-profile vulnerabilities over the years, but the biggest one is users exposing it to the internet either without requiring credentials or with weak credentials and/or unencrypted credentials, followed closely by using it to transfer sensitive files that aren’t self-encrypted.

**ADVICE:** Use it! But, only over SSH tunnels, since that way you have end-to-end encryption and are exposing one less service to the internet.

**ALTERNATIVES:** While there are some, rsync-over-SSH is a great, secure way to perform backups and transfer files from one system to another, so you should strongly consider it over services such as FTP or FTPS and, especially, legacy tools such as RCP.

**GETTING:** Better! Nearly 11% fewer rsunked systems are exposed this year compared to last year.

## Discovery details

The rsync service is almost old enough to rent a car in the U.S., given that it turned 24 this year. Unlike many network protocols, rsync has no IETF RFC for the protocol itself, but when uniform resource identifiers (URI, but you can think of them as URLs and we won’t judge you) became a thing, this venerable protocol achieved at least partial RFC status for its [URI scheme](https://tools.ietf.org/html/rfc5781). It does [have documentation](https://rsync.samba.org/tech_report/) and is widely used on the modern internet for keeping software and operating system mirrors populated, populating filesystems, performing backups, and—as we’ll see later—exposing a non-insubstantial number of home network-attached storage (NAS).

Rapid7's Jon Hart and Shan Sikdar took an [in-depth look at rsync exposure](/blog/post/2018/12/21/rsunk-your-battleship-an-ocean-of-data-exposed-through-rsync/) back in 2018, and only a tiny bit has changed since then, so we’ll focus more on the changes than reinvent the wheel.

![rsync-countries.png](https://www.rapid7.com/cdn/images/blt5750782c2c21d014/683de688237ea6a9ba91c418/rsync-countries.png) ![rsync-cloud.png](https://www.rapid7.com/cdn/images/blte9b44625b48d4f3b/683de6adbc38b185c7477eba/rsync-cloud.png)

If you’re wondering why [Alibaba](https://www.alibabacloud.com/help/doc-detail/54016.htm%3E;%20%3Chttps://www.alibabacloud.com/blog/speeding-up-network-file-transfers-with-rsync_594337) of China and [OVH](https://us.ovhcloud.com/public-cloud/cloud-archive/) of France both have a more significant rsync presence than the other providers, look no further than their documentation, which most folks new to “the cloud” will rely on to get jump-started. Unfortunately, both clouds default to plain ol’ rsync but do at least mention that you can run it more securely through an SSH tunnel.

## rsync exposure information

Over half (~57%) of the exposed rsync systems are running with a 10-year-old protocol (version 30), which is an indicator the operating systems are potentially over 10 years old and riddled with other vulnerabilities. While protocol version 31 is most current, this can be a bit misleading. Version 31 was released in 2013. Outside of versions 30 and 31 of the protocol, there is a steep drop-off to the truly ancient versions of the protocol.

rsync Protocol Version| Count  
---|---  
30| 117,629  
31| 80,391  
29| 7,596  
26| 2,654  
28| 510  
31.14| 45  
27| 36  
24| 8  
34| 7  
32| 2  
20| 1  
25| 1  
29| 1  
31.12| 1  
  
As far as we can tell, 31.14 and 31.12, the only versions with decimal numbers, are unique to Buffalo NAS devices. We have no idea why they mark these this way.

Over 20% of rsync exposure lies in residential ISP space (top 25 providers listed below). Most of these are NAS devices with brand names you’ve likely seen in online stores or big-box electronic retailers.

ISP| Count  
---|---  
HiNet| 5,316  
Korea Telecom| 5,300  
China Unicom| 4,583  
China Telecom| 4,528  
Vodafone| 4,389  
Orange| 4,274  
Deutsche Telekom| 2,245  
Comcast| 1,994  
Tata Communications| 1,355  
Charter Communications| 1,306  
Swisscom| 810  
Verizon| 732  
NTT Communications| 727  
Telia| 643  
Virgin Media| 626  
China Mobile| 550  
Cogent| 489  
Rostelecom| 473  
AT&T| 412  
Rogers| 394  
Cox Communications| 383  
CenturyLink| 193  
Hurricane Electric| 165  
Level3| 102  
China Tietong| 92  
  
The core rsync service has no encryption, so all operations—including authentication—operate over cleartext. This makes it just as bad as Telnet and FTP. The protocol has been extended to support using non-cleartext credentials, but all file transfers still happen in cleartext, so any prying eyes in the right network position can still grab your data.

One of the real dangers of exposing rsync, though, is that you’re letting attackers know you have files for the taking and have some operating system that may be worth taking over.

## Attacker’s view on rsync

Since rsync is a big, neon sign saying “I’ve got files!” and since a large portion of exposed rsync is on residential ISP networks, attackers can correlate other services running on those IP addresses to get an idea of the type of system that’s being exposed.

Why are these residential rsync systems sitting on the internet? Vendors such as QNAP need to make these NAS devices easy to use, so they create services such as “myQNAPcloud,” which lets consumers create a “nameyouwant.myqnapcloud.com” to access their devices over the internet (meaning they have to punch at least one hole in their home router to do so). It even has handy mobile apps that let them watch saved videos and listen to saved music. Our Sonar FDNS study found over 125,000 myqnapcloud.com entries, and it is super easy for attackers to collect that data as well. That means over 125,000 QNAP NAS device users just gave attackers their home (IP) addresses and placed a quaint “Welcome” mat out for them.

Unfortunately, QNAP (and a cadre of other NAS vendors) have a terrible track record when it comes to vulnerabilities, including seven unauthenticated, remote code execution vulnerabilities, [the most recent of which is a doozy](https://medium.com/bugbountywriteup/qnap-pre-auth-root-rce-affecting-450k-devices-on-the-internet-d55488d28a05). While these vulnerabilities are not exposed over rsync, the presence of rsync is a leading indicator that a NAS device is very likely present.

Attackers use these devices as launch points for other malicious activities on the internet (such as DDoS attacks) and can lock up all the files on these devices for consumer-grade ransomware attacks.

As you can see, exposing one innocent service such as rsync can ultimately get you into a world of trouble.

Our Heisenberg honeypot fleet does not have a high-interaction honeypot for rsync, but we do watch for all connection attempts on TCP/873 and see regular inventory scans (the blue spikes in the figure below) by researchers and attackers looking for new rsync endpoints to conquer.

![rsync-heisenberg.png](https://www.rapid7.com/cdn/images/blt2f5e773b9d05267d/683de6d42a9b68d09c2bd3e6/rsync-heisenberg.png)

## Our advice on rsync

**IT and IT security teams** should never use vanilla rsync and should always opt to wrap it in a tasty chocolate secure shell (i.e., only use it when tunnelling over certificate-based, authenticated SSH sessions). There is no other safe way to use rsync for confidential information. None.

**Cloud providers** should know better than to offer rsync services over anything but certificate-based, authenticated SSH. Existing insecure services should be phased out as soon as possible. The most obvious path toward this brave new world of encryption everywhere is to offer excellent, well-maintained, easy-to-find documentation, with examples, on how exactly to "get started" with rsync over SSH, and on the flip side, little to no documentation on how to run rsync naked (users who are determined to do the wrong thing can fight through man pages like we used to in the old days).  
  
**Government cybersecurity agencies** should regularly and strongly encourage consumers, cloud providers, and organizations to only use certificate-based, authenticated SSH-tunnelled rsync services and work with cloud providers and NAS vendors to eradicate the scourge of rsync exposure from those platforms.  


## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)