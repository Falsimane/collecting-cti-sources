# Metasploit Wrap-Up: 7/23/2021 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/07/23/metasploit-wrap-up-122/
- **Date :** 2025-06-02

---

## Now I Control Your Resource Planning Servers

Sage X3 is a resource planning product designed by Sage Group which is designed to help established businesses plan out their business operations. But what if you wanted to do more than just manage resources? What if you wanted to hijack the resource server itself? Well wait no more, as thanks to the work of [Aaron Herndon](https://www.linkedin.com/in/aaron-herndon-54079b5a/), [Jonathan Peterson](https://www.linkedin.com/in/jonathan-p-004b76a1/), [William Vu](https://twitter.com/wvuuuuuuuuuuuuu), [Cale Black](https://github.com/cblack-r7), and [Ryan Villarreal](https://www.linkedin.com/in/ryanvillarreal/) along with work from community contributor [deadjakk](https://github.com/deadjakk), Metasploit now has an exploit module for [CVE-2020-7388](https://attackerkb.com/topics/q0ETmshZPW/cve-2020-7388) and [CVE-2020-7387](https://attackerkb.com/topics/l1RZYyWf4X/cve-2020-7387), to allow unauthenticated attackers to gain SYSTEM level code execution on affected versions of Sage X3. This module should prove very useful on engagements both as a way to gain an initial foothold in a target network, as well as a way to elevate privileges to allow for more effective pivoting throughout the target network. More information on these vulnerabilities can be found in our detailed writeup post [on our blog](/blog/post/2021/07/07/cve-2020-7387-7390-multiple-sage-x3-vulnerabilities/).

## Help My Server is Raining Keys

Another great module that landed this week was an exploit for [CVE-2021-27850](https://attackerkb.com/topics/32H1tJnyGT/cve-2021-27850) from Johannes Mortiz and Yann Castel aka [Hakyac](https://github.com/Hakyac), which allows attackers to steal the HMAC key from applications that use a vulnerable version of the Apache Tapestry web framework. This HMAC key is particularly important in many applications as it is often used to sign important data within the application. However in the case of Apache Tapestry, one can actually take this even further and use the leaked HMAC key to exploit a separate Java deserialization vulnerability in Apache Tapestry to gain RCE using readily available gadgets such as CommonBeansUtil1 from ysoserial. Therefore this should be one to keep an eye out for and patch if you haven't already.

## PrintNightmare Improvements

Improvements have been made to the PrintNightmare module thanks to [Spencer McIntyre](https://twitter.com/zerosteiner) to improve the way that Metasploit checks if a target is vulnerable or not, as well as to incorporate the \??\UNC\ bypass for the second and most recent patch at the time of writing. Additionally, a separate bug was fixed in Metasploit's DCERPC library to prevent crashes when handling fragmented responses from the target server that could not fit into a single packet. These fixes should help ensure that not only is Metasploit able to better detect servers that are vulnerable to PrintNightmare, but also help target those servers that may not have fully applied all the appropriate patches and mitigations.

## New module content (4)

  * [Apache Tapestry HMAC secret key leak](https://github.com/rapid7/metasploit-framework/pull/15211) by Johannes Moritz and [Hakyac](https://github.com/Hakyac), which exploits [CVE-2021-27850](https://attackerkb.com/topics/32H1tJnyGT/cve-2021-27850) \- This adds an auxiliary module that retrieves the secret HMAC key from applications that use a vulnerable version of the Apache Tapestry web framework. Retrieving this key will allow an attacker to sign objects in order to exploit a separate Java deserialization vulnerability in Apache Tapestry.
  * [Sage X3 AdxAdmin Login Scanner](https://github.com/rapid7/metasploit-framework/pull/15400) by [Jonathan Peterson](https://www.linkedin.com/in/jonathan-p-004b76a1/) \- Added a Sage X3 login scanner.
  * [Wordpress Plugin Backup Guard - Authenticated Remote Code Execution](https://github.com/rapid7/metasploit-framework/pull/15402) by Nguyen Van Khanh, [Ron Jost](https://github.com/Hacker5preme), and [Hakyac](https://github.com/Hakyac), which exploits [CVE-2021-24155](https://attackerkb.com/topics/ufEsuA2DpJ/cve-2021-24155) \- This adds a module that exploits an authenticated file upload vulnerability in the Wordpress plugin, Backup Guard. For versions below v1.6.0, the plugin permits the upload of arbitrary php code due to insufficient checks on the file format. Once the file is uploaded, code execution can be achieved by requesting the file, located under the /wp-content/uploads/backup-guard directory.
  * [Sage X3 Administration Service Authentication Bypass Command Execution](https://github.com/rapid7/metasploit-framework/pull/15400) by [Aaron Herndon](https://www.linkedin.com/in/aaron-herndon-54079b5a/) and [Jonathan Peterson](https://www.linkedin.com/in/jonathan-p-004b76a1/), which exploits [CVE-2020-7388](https://attackerkb.com/topics/q0ETmshZPW/cve-2020-7388)\- Added an exploit for [CVE-2020-7387 + CVE-2020-7388](/blog/post/2021/07/07/cve-2020-7387-7390-multiple-sage-x3-vulnerabilities/).



## Enhancements and features

  * [#15403](https://github.com/rapid7/metasploit-framework/pull/15403) from [pingport80](https://github.com/pingport80) \- This makes changes to the Powershell session type to report its platform using a value consistent with the other session types. It also adds Powershell session support to some methods within the file mixin.
  * [#15409](https://github.com/rapid7/metasploit-framework/pull/15409) from [zeroSteiner](https://github.com/zeroSteiner) \- An update has been made to the PrintNightmare module to improve the way that it checks if a target is vulnerable or not and to now automatically converts UNC paths to use the \??\UNC\host\path\to\dll format to bypass the second and most recent patch at the time of writing. Additionally a bug was fixed in the DCERPC library where data that was read would be incomplete when the response would not fit into a single fragment to ensure that the PrintNightmare module can now read long responses from the target such as when enumerating the installed printer drivers.
  * [#15440](https://github.com/rapid7/metasploit-framework/pull/15440) from [bwatters-r7](https://github.com/bwatters-r7) \- This PR updates the payloads gem to include updates to Kiwi. For more information, see rapid7/mimikatz#5 and rapid7/metasploit-payloads#490



## Bugs fixed

  * [#14683](https://github.com/rapid7/metasploit-framework/pull/14683) from [gwillcox-r7](https://github.com/gwillcox-r7) \- This replaces a cryptic exception raised by msfvenom when an incompatible EXE template file is used with a specific injection technique. The new exception validates whether the EXE is compatible and reports the reason it is not so the user can more easily understand the problem.
  * [#15436](https://github.com/rapid7/metasploit-framework/pull/15436) from [sjanusz-r7](https://github.com/sjanusz-r7) \- Ensure that generated variable names aren't Java keywords
  * [#15443](https://github.com/rapid7/metasploit-framework/pull/15443) from [dwelch-r7](https://github.com/dwelch-r7) \- Adds python3 support for the wmiexec external module auxiliary/scanner/smb/impacket/wmiexec
  * [#15445](https://github.com/rapid7/metasploit-framework/pull/15445) from [zeroSteiner](https://github.com/zeroSteiner) \- Updates msfconsole's output logs to only show the target's ip when an exploit module is run, rather than a host-hash



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.0.53...6.0.54](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222021-07-15T10%3A18%3A50%2B01%3A00..2021-07-22T11%3A58%3A03-05%3A00%22)
  * [Full diff 6.0.53...6.0.54](https://github.com/rapid7/metasploit-framework/compare/6.0.53...6.0.54)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
[binary installers][binary] (which also include the commercial edition).

## Article tags

  * [Metasploit](/blog/tag/metasploit/)
  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Vulnerability Management](/blog/tag/vulnerability-management/)
  * [Exploits](/blog/tag/exploits/)
  * [Research](/blog/tag/research/)