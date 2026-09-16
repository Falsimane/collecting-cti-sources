# [Research] NICER Protocol Deep Dive: Secure Shell (SSH) | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/08/28/nicer-protocol-deep-dive-secure-shell-ssh/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## Secure Shell (SSH) (TCP/22)

It’s got “secure” right in its name!

### TLDR

**WHAT IT IS:** SSH is usually a secure alternative to Telnet, but it also can wrap virtually any protocol in a warm, comforting blanket of cryptographic security. 

**HOW MANY:** 17,875,456 discovered nodes  
17,073,109 (95.5%) have Recog fingerprints (21 total service families)

**VULNERABILITIES:** As with Telnet, the usual exposures associated with SSH stem from default passwords and password reuse. Also, SSH tends to surface vulnerabilities present in a given operating system's cryptographic libraries.

**ADVICE:** Deploy SSH judiciously, and have a system in place for generating and maintaining secure passwords or private keys. 

**ALTERNATIVES:** There are certainly alternatives to SSH, but it is free, open source, and well-maintained by a network of academic and commercial software developers. It is hard to imagine a reasonable alternative to SSH, especially given that SSH can wrap otherwise insecure protocols.

**GETTING:** Better? There was a 14% increase over 2019, but we’re not convinced that’s a good thing.

## Discovery details

Secure Shell, commonly abbreviated to SSH, was designed and deployed in 1995 as a means to defend against passive eavesdropping on authentication that had grown common against other cleartext protocols such as Telnet, rlogin, and FTP. While it is usually thought of as simply a cryptographically secure drop-in replacement for Telnet, the SSH suite of applications can be used to secure or replace virtually any protocol, either through native applications like SCP for file transfers, or through SSH tunneling.

One of the bright spots of this report analysis is the fact that SSH deployment has now outpaced Telnet exposure at a rate of six to one—it seems the world has gotten the message that, while direct console access from the internet might not be the wisest move in the world, about 85% of those exposed shells are secure shells, which takes whole classes of eavesdropping, spoofing, and in-transit data manipulation attacks off the table. Good job, internet, and especially the American network operators around the country—the United States exposes a ratio of 28:1 SSH servers (6.6 million) than Telnet servers (a mere 232,000). Compare this to the 3:1 ratio in China, which is 2.4 million SSH to 734,161. Given that SSH provides both console access and the capability of securing other protocols, whereas Telnet is used almost exclusively for console access, that United States ratio is pretty outstanding.

![ssh-countries-r7.png](https://www.rapid7.com/cdn/images/blt29e5ab5e8b1e7c63/683de9f33e68ee0846889c65/ssh-countries-r7.png) ![ssh-cloud-provider-r7.png](https://www.rapid7.com/cdn/images/blt27f95a003b45736f/683dea0eff6aa9095a0eab27/ssh-cloud-provider-r7.png)

## Exposure information

Being more complex and making more explicit security guarantees, SSH is not without its own [vulnerabilities](/fundamentals/vulnerabilities-exploits-threats/). Occasionally, traditional stack-based buffer overflows surface as with other network applications written in memory-unsafe languages. In addition, new vulnerabilities in implementations tend to present themselves in non-default combinations of configuration options, or are surfaced in SSH through vulnerabilities in the cryptographic libraries used by SSH to ensure secure communications. Most commonly, though, vulnerabilities in SSH are often associated with unchangeable, vendor-supplied usernames, passwords, and private keys that ship with IoT devices that (correctly) have moved away from Telnet. This is all to say that Secure Shell is not magically secure just due to its use of cryptography—password reuse is weirdly common in SSH-heavy environments, so protecting passwords and private keys is an important part of maintaining a truly secure SSH-based infrastructure.

As mentioned above, administrators and device manufacturers alike are strongly encouraged to adopt the open, free standards of SSH over their cleartext counterparts whenever possible. IoT, OT, and ICS equipment, in particular, is often cited as not having enough local resources to deal with the cryptographic overhead of running secure services, but if that is actually the case, these devices should never be exposed to an internet-connected network in the first place. As mentioned above, it is also not enough to simply move insecure practices such as default, reused passwords from a cleartext protocol to a “secure” protocol—the security offered by cryptography is only as good as the key material in use.

Of the SSH services discovered on the internet, the below table accounts for well over 99.9% of all offerings (only those fingerprintable services with at least 1,000 or more shown here.)

Service Family| Count| Percentage  
---|---|---  
OpenSSH| 15,747,821| 92.238%  
Dropbear| 1,250,254| 7.323%  
SSH| 37,884| 0.222%  
WinSSHD| 10,408| 0.061%  
WeOnlyDo| 6,510| 0.038%  
iLO| 6,495| 0.038%  
Secure FTP Server| 3,507| 0.021%  
NetScreen| 2,298| 0.013%  
Embedded SSH Server| 2,044| 0.012%  
SSH Tectia Server| 1,942| 0.011%  
libssh| 1,586| 0.009%  
VShell| 1,064| 0.006%  
  
## Attacker’s view

SSH provides console access in a better way than Telnet, but it is still just a piece of software with many features, including one that drops you to a command prompt after a successful login, so attackers perform credential stuffing (which can include using stolen certificates, too, for SSH) and vulnerability exploits against the service itself. As such, we’d be just repeating much of the same content as we did in Telnet (and we value your time too much to do that).

What we can do is focus more on two things: vulnerabilities associated with exposed SSH services and how much information exposed SSH services give to attackers.

The most prevalent version of OpenSSH is version 7.5. It turns four years old in December and has nine CVEs. Every single version in the top 20 has between two and 32 CVEs, meaning there’s a distinct lack of patch management happening across millions of systems exposed to the cold, hard internet.

Version| Count| Released| Number of CVEs  
---|---|---|---  
7.4| 4,784,909| 2016-12-19| 9  
7.6p1| 2,286,132| 2017-10-03| 8  
7.2p2| 1,928,745| 2016-03-10| 13  
5.3| 1,535,299| 2009-10-01| 32  
7.4p1| 1,023,278| 2016-12-19| 8  
6.6.1| 609,661| 2014-03-15| 22  
6.6.1p1| 558,341| 2014-03-15| 22  
6.7p1| 485,255| 2014-10-06| 22  
7.9p1| 341,816| 2018-10-19| 2  
7.5| 271,083| 2017-03-20| 9  
8| 195,587| 2019-04-17| 2  
4.3| 161,884| 2006-02-11| 40  
6.0p1| 145,874| 2012-04-22| 26  
7.9| 141,982| 2018-10-19| 7  
8.1| 99,243| 2019-10-09| 2  
5.9p1| 88,520| 2011-09-06| 26  
6.4| 79,966| 2013-09-08| 28  
7.7| 79,399| 2018-04-02| 9  
7.8| 67,960| 2018-08-24| 8  
8.2| 59,804| 2020-02-14| 3  
  
You may be saying, “So what?” (a question we try to ask ourselves regularly when we opine about exposure on the internet). Another exposure view may help answer said question:

![cves-per-os.png](https://www.rapid7.com/cdn/images/blt867170d291f9e209/683dea1f2a9b6862bf2bd520/cves-per-os.png)

The above figure packs quite a bit of information into it, so let’s dig in as we hit our second point (how much information [exposed SSH services](https://github.com/rapid7/recog/blob/master/xml/ssh_banners.xml) give to attackers).

The left panel says “Operating Systems,” which means we can figure out which operating system is in use just from the data we get back from our Sonar SSH connections (enumerated below). Each dot represents one operating system version, the position on the X axis represents how many servers we found, and the position on the Y axis represents the number of CVEs that have been assigned to it. The color represents the highest severity. There is quite a bit of CVSS 8+ on that chart, which means there are quite a few high-priority vulnerabilities on those systems (at the operating system level).

The right panel is the same, just for SSH versions (one of which we enumerated above). The count difference is due to both [recog coverage](https://github.com/rapid7/recog/blob/master/xml/ssh_banners.xml) and the fact that a single operating system version can run different versions of SSH, so the aggregation up to operating system category will be higher. There are fewer major vulnerabilities within the SSH services but there are more above 7 than below, which means they’re also pretty high-priority.

Adversaries can use this information to plan which attack path they plan on taking and map vulnerabilities to exploits to add to their arsenal. Overall, we’d say attackers could have quite a bit of fun with this particular SSH corpus.

OS| Version| Count| | OS| Version| Count| | OS| Version| Count  
---|---|---|---|---|---|---|---|---|---|---  
Ubuntu| 18.04| 2,220,456| | Debian| 9| 975,722| | FreeBSD| 11.2| 23,503  
Ubuntu| 16.04| 1,890,981| | Debian| 8| 436,149| | FreeBSD| 12| 19,360  
Ubuntu| 14.04| 533,725| | Debian| 10| 274,752| | FreeBSD| 9| 17,646  
Ubuntu| 19.1| 52,026| | Debian| 7| 137,363| | FreeBSD| 11.1| 4,687  
Ubuntu| 12.04| 48,705| | Debian| 6| 46,054| | FreeBSD| 9.2| 4,193  
Ubuntu| 19.04| 36,451| | Debian| 7.8| 38,543| | FreeBSD| 8.1| 3,681  
Ubuntu| 10.04| 16,757| | Debian| 4| 17,279| | FreeBSD| 7.1| 2,468  
Ubuntu| 17.1| 9,467| | Debian| 5| 13,526| | FreeBSD| 10.4| 2,179  
Ubuntu| 15.04| 7,086| | Debian| 3.1| 3,089| | FreeBSD| 8.3| 1,939  
Ubuntu| 17.04| 5,183| | Debian| 11| 1,361| | FreeBSD| 8.4| 1,627  
Ubuntu| 16.1| 3,536| | Debian| 3| 362| | FreeBSD| 10| 937  
Ubuntu| 8.04| 3,314| | | | | | FreeBSD| 8| 656  
Ubuntu| 12.1| 2,408| | MikroTik| 2.9| 419| | FreeBSD| 6| 521  
Ubuntu| 11.04| 2,276| | | | | | FreeBSD| 4.9| 312  
Ubuntu| 10.1| 2,201| | vxWorks| 5.1.0p1| 911| | FreeBSD| 5.3| 155  
Ubuntu| 18.1| 2,192| | vxWorks| 6.9.0| 288| | FreeBSD| 4.11| 110  
Ubuntu| 13.04| 2,131| | vxWorks| 1.10.0| 285| | FreeBSD| 4.7| 74  
Ubuntu| 14.1| 2,117| | vxWorks| 1.8.4| 47| | FreeBSD| 5.5| 63  
Ubuntu| 11.1| 1,807| | vxWorks| 6.8.0| 40| | FreeBSD| 4.8| 43  
Ubuntu| 9.1| 1,234| | vxWorks| 1.12.0| 24| | FreeBSD| 5.2| 21  
Ubuntu| 9.04| 861| | vxWorks| 6.5.0| 22| | FreeBSD| 5| 14  
Ubuntu| 15.1| 860| | vxWorks| 6.0.9| 14| | FreeBSD| 4.6| 14  
Ubuntu| 8.1| 393| | vxWorks| 6.6.0| 8| | FreeBSD| 5.1| 11  
Ubuntu| 6.04| 303| | vxWorks| 6.0.2| 7| | FreeBSD| 4.5| 7  
Ubuntu| 7.1| 285| | vxWorks| 7.0.0| 2| | FreeBSD| 4.3| 6  
Ubuntu| 7.04| 195| | | | | | FreeBSD| 4.4| 4  
Ubuntu| 5.1| 29| | | | | | | |   
Ubuntu| 5.04| 5| | | | | | | |   
  
## Our advice

**IT and IT security teams** should be actively replacing cleartext terminal and file transfer protocols with SSH alternatives whenever and wherever they are discovered. If such replacements are impossible, those devices should be removed from the public internet.

**Cloud providers** should provide SSH as an easy default for any sort of console or file transfer access, and provide ample documentation on how customers can wrap other protocols in SSH tunnels with specific examples and secure-by-default configurations.

**Government cybersecurity agencies** should actively promote the use of SSH over unencrypted alternatives, especially when it comes to IoT. These organizations can also help encourage industrial use of SSH in areas where Telnet and FTP are still common. In addition, cybersecurity experts can and should encourage good key management and discourage vendors from shipping SSH-enabled devices with long-lived, default passwords and keys.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)