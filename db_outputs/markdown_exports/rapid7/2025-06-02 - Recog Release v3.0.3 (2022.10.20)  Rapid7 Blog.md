# Recog Release v3.0.3 (2022.10.20) | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2023/01/12/recog-release-v3-0-3-2022-10-20/
- **Date :** 2025-06-02

---

Recog Release v3.0.3, which is available now, includes updated fingerprints for Zoho ManageEngine PAM360, Password Manager Pro, and Access Manager Plus; Atlassian Bitbucket Server; and Supervisord Supervisor. It also includes new fingerprints and a number of bug fixes, all of which are detailed below.

Recog is an open source recognition framework used to identify products, operating systems, and hardware through matching network probe data against its extensive fingerprint collection. Support for Recog is part of Rapid7’s ongoing commitment to open source initiatives.

### Zoho ManageEngine PAM360, Password Manager Pro, and Access Manager Plus

Fingerprints for these three Zoho ManageEngine products were added shortly after Cybersecurity and Infrastructure Security Agency (CISA) added [CVE-2022-35405](https://attackerkb.com/topics/9IKNFYh9Wl/cve-2022-35405?referrer=blog) to their [Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) on September 22nd, 2022. Favicon, HTML title, and HTTP server fingerprints were created for both [PAM360](https://www.manageengine.com/privileged-access-management) and [Password Manager Pro](https://www.manageengine.com/products/passwordmanagerpro), and favicon and HTML title fingerprints were created for [Access Manager Plus](https://www.manageengine.com/privileged-session-management). PAM360 version 5500 (and older) and Password Manager Pro version 12100 (and older) are both vulnerable to an unauthenticated remote code execution (RCE) vulnerability, and Access Manager Plus version 4302 (and older) is vulnerable to an authenticated remote code execution (RCE) vulnerability. In addition, [Grant Willcox](https://github.com/gwillcox-r7) contributed the Metasploit [Zoho Password Manager Pro XML-RPC Java Deserialization](https://github.com/rapid7/metasploit-framework/pull/16852) exploit module which is capable of exploiting the unauthenticated vulnerability via the XML-RPC interface in Password Manager Pro and PAM360 and attaining RCE as the NT AUTHORITY\SYSTEM user.

More recently, on January 4th, 2023, Zoho released details of a SQL injection vulnerability ([CVE-2022-47523](https://www.manageengine.com/privileged-session-management/advisory/cve-2022-47523.html)) in PAM360 version 5800 (and older), Password Manager Pro version 12200 (and older) and Access Manager Plus version 4308 (and older). From a quick analysis of internet scan data there appears to be only about 76 Password Manager Pro and 21 PAM360 instances on the internet.

![PMP-login.png](https://www.rapid7.com/cdn/images/blt575764cb481ee245/683ddf25ff6aa91c860ea7ea/PMP-login.png) ![PAM360-login.png](https://www.rapid7.com/cdn/images/bltadebb69b95f1ef8c/683ddf4fbc38b19ade477c7d/PAM360-login.png)

### Atlassian Bitbucket Server

Favicon, HTML title and HTTP cookie fingerprints for the [Atlassian Bitbucket server](https://www.atlassian.com/software/bitbucket) were added shortly after our Emergent Threat Response for [CVE-2022-36804](/blog/post/2022/09/20/cve-2022-36804-easily-exploitable-vulnerability-in-atlassian-bitbucket-server-and-data-center/) was published on September 20th, 2022 in response to the command injection vulnerability in multiple API endpoints of both Bitbucket Server and Data Center. An adversary with access to either a public repository or read permissions on a private repository can perform remote code execution simply through a malicious HTTP request. [Shelby Pace](https://github.com/space-r7) contributed the Metasploit [Bitbucket Git Command Injection](https://github.com/rapid7/metasploit-framework/pull/17042) exploit module which is capable of exploiting the unauthenticated command injection. Bitbucket Server and Data Center versions 7.6 prior to 7.6.17, 7.17 prior to 7.17.10, 7.21 prior to 7.21.4, 8.0 prior to 8.0.3, 8.1 prior to 8.1.3, 8.2 prior to 8.2.2 and 8.3 prior to 8.3.1 are vulnerable. From a quick analysis of internet scan data there appears to be just under a thousand of these exposed on the internet.

![Bitbucket-login.png](https://www.rapid7.com/cdn/images/bltd18d02236ce1b6e9/683ddf7573c845df60e8c30d/Bitbucket-login.png)

### Supervisord Supervisor

Favicon and HTML title fingerprints were added for anyone interested in locating unsupervised [Supervisor](http://supervisord.org/) instances on their networks. The web interface for the process control system allows users to restart or stop processes under the software’s control, and even tail the standard output and error streams. There might be some interesting information in those streams! From a quick analysis of internet scan data there appears to be only about 165 instances on the internet.

![Supervisor-status.png](https://www.rapid7.com/cdn/images/blt7ba6a490cc473d74/683ddf984c5a0988655e0a98/Supervisor-status.png)

### New fingerprints (23)

  * Add Python BaseHTTP fingerprint by [@mkienow-r7](https://github.com/mkienow-r7) in [#473](https://github.com/rapid7/recog/pull/473)
  * More DHCP-based fingerprints by [@dmoinescu-r7](https://github.com/dmoinescu-r7) in [#476](https://github.com/rapid7/recog/pull/476)
  * Add Talend Restlet Framework fingerprint by [@mkienow-r7](https://github.com/mkienow-r7) in [#475](https://github.com/rapid7/recog/pull/475)
  * Add Gunicorn with no version fingerprint by [@mkienow-r7](https://github.com/mkienow-r7) in [#477](https://github.com/rapid7/recog/pull/477)
  * Add Python WSGIServer fingerprint by [@mkienow-r7](https://github.com/mkienow-r7) in [#479](https://github.com/rapid7/recog/pull/479)
  * Add OpenKM Document Management System fingerprint by [@mkienow-r7](https://github.com/mkienow-r7) in [#480](https://github.com/rapid7/recog/pull/480)
  * Add Atlassian Bitbucket fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#482](https://github.com/rapid7/recog/pull/482)
  * Add Mayan EDMS document management system fingerprint by [@mkienow-r7](https://github.com/mkienow-r7) in [#481](https://github.com/rapid7/recog/pull/481)
  * Add SalesAgility SuiteCRM fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#483](https://github.com/rapid7/recog/pull/483)
  * Add ManageEngine PAM360 fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#484](https://github.com/rapid7/recog/pull/484)
  * Add ManageEngine Password Manager Pro fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#485](https://github.com/rapid7/recog/pull/485)
  * Add ManageEngine Access Manager Plus fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#486](https://github.com/rapid7/recog/pull/486)
  * Add Crow C++ framework for web services fingerprint by [@mkienow-r7](https://github.com/mkienow-r7) in [#487](https://github.com/rapid7/recog/pull/487)
  * New dhcp vendor class fingerprints by [@modoyle-r7](https://github.com/modoyle-r7) in [#488](https://github.com/rapid7/recog/pull/488)
  * Add Papermerge document management system fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#489](https://github.com/rapid7/recog/pull/489)
  * Add Medusa extensible Internet server framework fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#490](https://github.com/rapid7/recog/pull/490)
  * DHCP vendor_class Xerox Printer updates by @modoyle-r7 in [#491](https://github.com/rapid7/recog/pull/491)
  * Add Amazon OpenSearch fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#492](https://github.com/rapid7/recog/pull/492)
  * Add Supervisord Supervisor web interface fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#494](https://github.com/rapid7/recog/pull/494)
  * Add qdPM fingerprints by [@mkienow-r7](https://github.com/mkienow-r7) in [#495](https://github.com/rapid7/recog/pull/495)
  * More fingerprints for the Polycom VVX family by [@dmoinescu-r7](https://github.com/dmoinescu-r7) in [#497](https://github.com/rapid7/recog/pull/497)
  * DHCP fingerprints for Polycom SoundStation IP by [@dmoinescu-r7](https://github.com/dmoinescu-r7) in [#496](https://github.com/rapid7/recog/pull/496)
  * DHCP fingerprint for Avaya device by [@dmoinescu-r7](https://github.com/dmoinescu-r7) in [#499](https://github.com/rapid7/recog/pull/499)



### Bugs fixed (3)

  * Temporary fix to restore rspec progress formatter by [@mkienow-r7](https://github.com/mkienow-r7) in [#474](https://github.com/rapid7/recog/pull/474)
  * Restore non-capturing groups to fix anchored regex issue by [@mkienow-r7](https://github.com/mkienow-r7) in [#478](https://github.com/rapid7/recog/pull/478)
  * Add missing IMAP CAPABILITY string by [@mkienow-r7](https://github.com/mkienow-r7) in [#498](https://github.com/rapid7/recog/pull/498)



### Get the release

You can get the [v3.0.3 Recog Ruby gem](https://rubygems.org/gems/recog/versions/3.0.3) from RubyGems, the [v3.0.3 Recog content archive](https://github.com/rapid7/recog/releases/download/v3.0.3/recog-content-3.0.3.zip) from the [Recog v3.0.3 release](https://github.com/rapid7/recog/releases/tag/v3.0.3) page, and you can get more details on the changes since the last release from GitHub:  


  * [Full diff recog v3.0.2...v3.0.3](https://github.com/rapid7/recog/compare/v3.0.2...v3.0.3)
  * [Full diff recog-ruby v3.0.2...v3.0.3](https://github.com/rapid7/recog-ruby/compare/v3.0.2...v3.0.3)



## Article tags

  * [Open Source](/blog/tag/open-source-news/)
  * [Research](/blog/tag/research/)