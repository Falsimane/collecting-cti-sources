# How Rsync on the Public Internet Puts Your Data at Risk | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2018/12/21/rsunk-your-battleship-an-ocean-of-data-exposed-through-rsync/
- **Date :** 2025-06-02

---

_This blog was co-written by Jon Hart and Shan Sikdar._

[Rsync](https://rsync.samba.org/) is primarily a utility for synchronizing files between systems in an efficient manner and is frequently used for archival and backup purposes as well as data distribution and sharing tasks. Rsync also has the ability to operate in a daemon mode where it listens on port 873/TCP. In the remainder of this research, when we refer to rsync, we mean rsync operating in daemon mode unless otherwise noted.

[Rapid7 Labs](/research/) recently decided to take a fresh look at rsync, this time focusing on exposure of rsync globally on the public internet. Deploying rsync in daemon mode is tricky from a security perspective as history has shown and our research will help solidify.

The primary focus of this research was to understand more about what is exposing rsync, including anything that could speak to the security of these instances, with the goal being outreach, education, and [security awareness](/fundamentals/security-awareness-training/). Analysis of the data collected about exposed rsync instances on the public internet resulted in a variety of findings; some were expected, some were not.

## Background

In daemon mode, rsync organizes files using modules, which are just symbolic names and descriptions that point to a specific directory reachable by the user running the rsync daemon. As an example of what a client sees from the module level, when we look at the rsync instance used to distribute rsync itself—rsync.samba.org—we see eight modules presented after a brief greeting or “message of the day,” as seen below:

![Welcome1.jpg](https://www.rapid7.com/cdn/images/blt2ce66f4753a8b4f8/683ddc36da5c306440a83357/Welcome1.jpg)

The rsync daemon has had a variety of security capabilities layered in since its original release in 1996, including host- and file-level ACLs, chroot, and the ability to prevent a module from showing up in the listing, such as in the example above. Rsync also has the ability to require authentication at varying stages of the process, which is achieved with a 128-bit, MD4-based challenge response system, but it doesn’t natively provide encryption of any of the data transferred over the rsync connection. The usual workaround to this shortcoming is to use Secure Shell (SSH) to tunnel the rsync communication, rather than exposing rsync directly, which mitigates most of the risk we are discussing.

Rsync has had eight CVEs assigned to it at last count, the most severe of which are vulnerabilities related to access-control bypass problems similar to [CVE-2017-17433](/db/vulnerabilities/debian-cve-2017-17433).

A different, more fundamental class of vulnerabilities has existed since the original release of rsync. Just like any other file sharing, synchronization, or similar service, the files and directories shared by the service in question may be accessible for reading or possibly even writing by unauthorized parties if they are improperly secured using available authentication and authorization mechanisms. The true level of exposure depends on the files and directories being served by the rsync daemon.

The first report of this may have been [CVE-2014-2927](/db/vulnerabilities/f5-big-ip-cve-2014-2927), which describes a near-complete compromise of F5 BIG-IP devices under abnormal situations in which the rsync daemon didn’t require authentication and gave remote attackers read/write capabilities for arbitrary files on the device. In [CVE-2015-0932](https://nvd.nist.gov/vuln/detail/CVE-2015-0932), [Cylance](https://www.cylance.com) reported a vulnerability affecting ANTLabs InnGate routers, which were used in hotels worldwide. In this case, a lack of authentication once again left these systems open to attack due to read-write access by anyone who chose to look. [CVE-2016-7560](https://nvd.nist.gov/vuln/detail/CVE-2016-7560), which affected Fortinet’s FortiWLC wireless controllers, describes a slight variation of this vulnerability in which a hardcoded account gave read-write access to a portion of the system. Despite just three CVEs upon cursory inspection, it is assumed that there have been and will continue to be more specific exposures of this nature.

## Methodology

Using [Project Sonar](/research/project-sonar/), we have been scanning the public internet looking for systems with the rsync daemon exposed on 873/TCP. We achieve this by first identifying systems claiming to have the 873/TCP port open using [ZMap](https://zmap.io). For every system claiming to have this port open, we attempt to negotiate the rsync protocol and list the available modules using a modified version of the rsync client utility that disconnects and notes when authentication is required for any operations.

In an effort to better understand the security of these rsync instances, the Sonar study also obtains a listing for every module available that contains the timestamps, permissions, file size, file name, and directories available in the first level of the directory that maps to the module. Using rsync.samba.org again as an example, if we list the contents of the rsyncftp module, we are presented with the file system permissions, size, and modification date of every file and directory within that first level:

![Welcome2.jpg](https://www.rapid7.com/cdn/images/blt6bfc4033b8a33171/683ddc5c237ea629d091c127/Welcome2.jpg)

For a variety of reasons, we are unable to probe further to understand whether the contents of these rsync modules are truly readable or writable, but fortunately, we are able to identify which systems and modules _might_ be at risk of exposure by determining whether each module can have its contents listed.

## Common patterns

Our exploration of rsync uncovered some common patterns among the thousands of exposed rsync servers scattered across the internet. In this section, we’ll discuss the overall availability of rsync, common module names, and contents, the presence of authentication, the ability to list modules, and some clues as to the device identities through SSL certificate analysis on the hosting IP addresses.

### Rsync footprint

Of the approximately 3.3 million IPv4 addresses claiming to be listening on port 873/TCP, presumably for rsync, 92% are not actually rsync at all. This is a pattern we see regularly on almost every other TCP study performed by Project Sonar. For any given port where we expect to see a given service, we also see millions of IPs that claim to be but are not actually listening at all, or are offering up an entirely different service, such as HTTP, SSH, and other services.

As rsync has evolved over the years, newer versions of the protocol have been developed to support newer features. With these advancements, there tends to be changes in the version numbers advertised by the daemons. Examining the versions advertised by confirmed rsync endpoints in regular Sonar scans shows that the majority—170,000— are speaking a version that was current 10 years ago, version 30.0.

For the approximately quarter million IPv4 addresses confirmed to be running rsync in some way, the United States, China, and Germany hold the top three positions:

![Global_Distribution.jpg](https://www.rapid7.com/cdn/images/bltdea1a59ce3463c60/683ddc822a7686b977bc82f7/Global_Distribution.jpg)

### Module name clues

Looking at the names of the unique module groups offered by confirmed rsync endpoints, clusters of several thousand endpoints reported module groups such as the following:

  * Pmta,Web
  * root
  * 9fc81642102bf60d
  * backup
  * squid
  * chap,pptp
  * etc,www
  * f1man
  * changes
  * chap



Examining the nearly 150,000 unique names of the modules offered by these systems, this pattern clarifies:

![Distribution_of_Modules.jpg](https://www.rapid7.com/cdn/images/blt62c81f346fbad89f/683ddca82a9b681b902bd128/Distribution_of_Modules.jpg)

Additional analysis showed that there were in excess of 300 systems exposing modules over rsync that appear to be related to the Debian, CentOS, and Gentoo projects, as well as various open source efforts, which are all known to use rsync to distribute their software. These systems are deliberately exposed like this on the public internet, and that is mostly OK—functionally, these instances are pretty similar to an HTTP web server that is merely offering read-only access to files intended for public distribution.

Overall, the names of these modules suggest that most of these publicly available rsync instances are being used for backup and archival purposes, which is not surprising given rsync’s purpose and history. However, it is initially worrying to see modules such as root, home, surveillance, www, and data, all of which sound like they contain potentially sensitive information. For the systems exposing the root module, there are eerie similarities to some of the previously mentioned CVEs.

### Authentication

Almost 18% of the systems confirmed running rsync require authentication after connecting before the list of modules is available. This is not the default setting, but not requiring authentication at this stage is perfectly acceptable if the modules are intended to be public, such as in the case of rsync instances being used for software distribution, as we discovered.

Revisiting the previous track of inspecting the module names, we discovered that with the vast majority of the modules that sounded very sensitive—home, NetBackup, homes, surveillance, and even that mysterious 9fc81642102bf60d module—almost all required authentication before being able to list the contents of the directory and presumably before being able to read or write the contents within.

### Module listing

Nearly one-fifth of the systems confirmed to be running rsync don’t advertise any modules. There are several possible explanations for this. First, it could be that these rsync instances truly have no modules, in which case there is likely no reason for them to be offering the service in the first place. It could also be the case that the rsync instances do have modules but all are configured to not be listed, which is an option but is off by default.

For the remaining systems running rsync that do not require authentication to list the modules, Sonar also attempted to list the contents of each module, as described earlier. A positive listing indicates that the module is possibly at risk for unauthorized reading or writing of the contents within.

Merely listing the contents of a module without authentication isn’t necessarily a risk unless the name of the module or the names of the files and directories within are somehow sensitive. The more severe risk comes from when these potentially sensitive files are readable—or worse, writable—without authentication.

If a module’s contents are listable, a few factors control whether they are susceptible to unauthorized read or write access. One possibility is the non-default read-only and write-only options for rsync daemon. Another is file system permissions relative to the user running rsync, which is generally a root or similar privileged user, anyway, leaving most systems with ineffective protections against unauthorized reading or writing.

As of late November 2018, there are approximately 14,000 IPv4 addresses exposing rsync with one or more listable modules and therefore _possibly_ at risk of exposure of unauthorized reading or writing of the contents within:

![Listable_Modules.jpg](https://www.rapid7.com/cdn/images/blt53fa0117d69bdcc9/683ddccdca9dfc639b526577/Listable_Modules.jpg)

### SSL certificates

As part of other studies, Sonar collects the SSL certificates presented by a variety of SSL/TLS-enabled services on the public internet, including dozens of [HTTPS](https://opendata.rapid7.com/sonar.ssl/) ports and [mail services](https://opendata.rapid7.com/sonar.moressl/).

After correlating the IPv4 addresses that were confirmed to be offering rsync with the SSL certificate data that was obtained in routine HTTPS and other SSL/TLS studies across dozens of ports, we see that a significant number of the devices running rsync appear to be QNAP, Synology, Buffalo, and ASUS backup/storage/media devices, with approximately 20,000 each for QNAP and Synology alone.

### Module contents

For every module that Sonar was able to successfully list, it recorded a one-level-deep listing that includes the name, size, permissions, and time metadata for every file within. This gives us a closer look at the true contents of these rsync instances and may hint at the risk. Even with just the one-level-deep listing, the 14,000 systems described previously contain in excess of 5.3 million files.

As you might guess given the clues so far about the types of devices running rsync, there is a pile of data exposed that is hard to really get a grasp on.

The most popular file name being exposed is, ironically, rsyncd.conf. The next several clusters of approximately 1,800 systems all have similar patterns that indicate some sort of root file system or similarly sensitive content is exposed:

  * passwd
  * hostname
  * rc.boot
  * main.conf
  * vpn.net



File extensions weave an interesting story, too.

Purely based on file counts, 2.1 million of the files—by far the largest contributor—have the mp4 extension. Even before we discovered the mp4 extension commonality, it was easy to see what most of these mp4 files were: pornography and pirated movies. The one-level-deep inspection that Sonar conducted as part of this research identified approximately 566TB of data alone with the mp4 extension.

## Root causes

As previously mentioned, exposing rsync itself is not necessarily an appreciable risk. There are legitimate reasons to expose rsync and a variety of methods to help secure it. However, seeing such large quantities of specific devices and other patterns does raise questions related to how this is happening. There are several possibilities, including some we outline below:

### Documentation

At least part of the answers are a quick Google search away: [QNAP](https://www.qnap.com/en/how-to/tutorial/article/how-to-set-up-remote-replication-on-qnap-nas/), [Synology](https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Backup_Restore/How_to_back_up_Linux_computer_to_Synology_NAS), and [Buffalo](https://www.buffalotech.com/knowledge-base/backup-terastation-to-linux-rsync-server) all have documentation that describes how to configure their backup devices to use rsync in a variety of ways. A cursory inspection shows that they all mention creating a username and password. This is about the best you can do with rsync from an authentication perspective—assuming, of course, that the password isn’t a commonly known one, such as one mentioned in documentation.

### NAT and UPnP

It is also possible that in some scenarios, rsync exposure on the public internet could be a side effect of UPnP or other NAT-tunneling technologies. QNAP’s documentation mentions “Forward the port 873 on your NAT router to the LAN IP address of the remote NAS,” which explains their prevalence on the internet. Buffalo’s [documentation](https://www.buffalotech.com/knowledge-base/configuring-webaccess-on-a-buffalo-airstation) shows how to enable remote access to their devices, including enabling UPnP, presumably to automatically expose the rsync daemon or other services externally in the likely case of network address translation (NAT). It is likely that Synology and any other affected vendors either have similar documentation or the devices were exposed by similar means: operator misconfiguration.

### Backup clouds and dynamic DNS

Rsync’s old age doesn’t mean it can’t find its way into the cloud in some way, and most vendors offer a variety of cloud-based or other services for remotely accessing your devices.

QNAP offers a service called QNAPCloud, which is a dynamic DNS (DDNS) service that enables remote device access using a custom name in the myqnapcloud.com domain. A search of the past 30 days of Sonar DNS results identified approximately 85,000 names and IPs in this space. Each name belongs to a specific QNAP device, meaning there are that many QNAP devices participating in the QNAP cloud. Further digging shows that the [documentation](http://qnapsupport.net/qnapcloud-upnp-router-problem-i-can-access-nas-via-cloudlink-but-name-myqnapcloud-com-doestn-work/) for debugging problems when remotely accessing your QNAP device via the myqnapcloud.com vanity domain includes ensuring you forwarded the correct ports and that list of ports includes 873/TCP for rsync.

Synology offers similar capabilities. Its devices have DDNS capabilities, and a synology.me domain exists for uniquely naming and remotely accessing Synology devices. A search of the same Sonar DNS data shows over 75,000 names, indicating there are approximately that many Synology devices connected to the internet in some way.

Buffalo has a similar explanation in its [documentation](https://www.buffalotech.com/knowledge-base/configuring-webaccess-on-a-buffalo-airstation), which describes how to make your device accessible remotely, including configuring a DDNS name. Because DDNS services for Buffalo devices are handled by third parties that are not specific to Buffalo, we can’t readily estimate the number that might be exposed in some way remotely.

It is easy to see how even well-intentioned and otherwise good documentation can lead users astray. For example, it is understandable that, nestled behind a firewall, many users might even disable authentication entirely for their backup system or use default or easily guessed credentials. Combined with enabling remote access, as previously described, accidental exposure is just a misclick away.

### Service provider misconfigurations

As part of all endpoint studies, Project Sonar stores information about the IP in question at the time of study, including geographic metadata and the organization that owns the IP. Both of these are largely ASN-based, adding some level of bias to any analysis based on this data.

After identifying which IP addresses offered one or more modules that could have their contents listed, the organizations responsible for the largest groups of IPs suggest that there are various service providers—cloud or otherwise—that are exposing rsync in a seemingly dangerous manner. A quick look through the data for the top handful quickly identified instances in which hundreds of systems were exposing backups with sensitive-looking contents, including hundreds of root file systems. This likely represents a situation similar to what caused the three CVEs mentioned previously.

## Recommendations

There was a time when it was fine to expose rsync on the public internet. But given some of the inherent weaknesses in rsync, the myriad ways rsync could end up listening on untrusted networks like the public internet, and the massively evolved threat landscape in general, rsync on the public internet is no longer OK. The only remotely acceptable use case for sync nowadays in daemon mode on the public internet is for public file distribution purposes, and even that comes with the risk inherent in any cleartext protocol, including snooping and man-in-the-middle opportunities.

If you absolutely must use rsync in daemon mode on the public internet, the rsyncd.conf configuration file has a variety of options that could help, including numerous authentication and authorization knobs. There are also specific options related to listing, reading, and writing of module contents—though as we’ve described in this research, many of the issues we observed with rsync are caused at least in part by faulty or minsterpretted documentation. Writing yet more documentation on how to secure rsync would just add to the problem, particularly given that we are not necessarily rsync experts.

Perhaps this is the only real recommendation we can solidly give: Do not run rsync in daemon mode attached to any untrusted networks, including the public internet.

## Conclusions

Early on in this research, it became clear there was a class of problems with rsync being exposed on the public internet. However, in hindsight, this should be obvious. Previous experience can leave security folks with a jaded—albeit unfortunately accurate—mindset that this situation was inevitable. The data that rsync holds tends to have a higher level of inherent sensitivity. When combined with the challenges of securing rsync, much of what we’ve described here in terms of the problem and what might be at risk mirrors what we see with other services: “If you build it, they will misconfigure it.”

Our desire for an always-on, always-accessible, dirt-cheap, and easy-to-use solution for everything is partially to blame as well, as evidenced in our research by the tens of thousands of storage, backup, and archive solutions typically used in the end-user and small-business market. In the rush to meet this demand, companies have developed a variety of solutions that either suffer from inherent weaknesses or are easy to misconfigure and leave data unknowingly exposed on the public internet. The result is 14,000 systems exposing in excess of 5.3 million files at possible risk of unauthorized read or write.

In many ways, we have just scratched the surface of the possibilities related to rsync’s true exposure and risk. It is likely that there is a vast, unexplored treasure trove of sensitive data exposed by simple misconfigurations of rsync-enabled storage, backup, and archive devices.

We welcome any feedback on this topic and encourage collaboration. Reach out to us via the comments, on Twitter ([@rapid7](https://twitter.com/rapid7)), or via [[email protected]](/cdn-cgi/l/email-protection#502235233531223338102231203934677e333f3d). Also, check out another view of rsync exposure from our friends over at BinaryEdge.

####   
Like security research? Learn more about our other research projects. 

[Get Started](/research/)

  


## Article tags

  * [Research](/blog/tag/research/)
  * [Project Sonar](/blog/tag/project-sonar/)