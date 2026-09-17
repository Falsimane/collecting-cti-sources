# Metasploit Wrap-Up 12/10/21 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/12/10/metasploit-wrap-up-142/
- **Date :** 2025-06-02

---

## Word and Javascript are a rare duo.

Thanks to [thesunRider](https://github.com/thesunRider). you too can experience the wonder of this mystical duo. The sole new metasploit module this release adds a file format attack to generate a very special document. By utilizing Javascript embedded in a Word document to trigger a chain of events that slip through various Windows facilities, a session as the user who opened the document can be yours.

## Do you like spiders?

It has been 3 years since SMB2 support was added to smb share enumeration and over a year ago SMB3 support was added, yet the spiders are not done spinning their webs. Thanks to [sjanusz-r7](https://github.com/sjanusz-r7) the spiders have evolved to take advantage of these new skills and the webs can span new doorways. Updates to scanner/smb/smb_enumshares improve enumeration support for the latest Windows targets that deploy with SMB3 only by default.

## New module content (1)

  * [Microsoft Office Word Malicious MSHTML RCE](https://github.com/rapid7/metasploit-framework/pull/15742) by [klezVirus](https://github.com/klezVirus), [lockedbyte](https://github.com/lockedbyte), [mekhalleh (RAMELLA Sébastien)](https://github.com/mekhalleh), and [thesunRider](https://github.com/thesunRider), which exploits [CVE-2021-40444](https://attackerkb.com/topics/6ojqzQoPox/cve-2021-40444?referrer=blog) \- This adds an exploit for CVE-2021-40444 which is a vulnerability that affects Microsoft Word. Successful exploitation results in code execution in the context of the user running Microsoft Word.



## Enhancements and features

  * [#15854](https://github.com/rapid7/metasploit-framework/pull/15854) from [sjanusz-r7](https://github.com/sjanusz-r7) \- This updates the SpiderProfiles option as part of the scanner/smb/smb_enumshares module to now work against newer SMB3 targets, such as windows 10, Windows Server 2016, and above.
  * [#15888](https://github.com/rapid7/metasploit-framework/pull/15888) from [sjanusz-r7](https://github.com/sjanusz-r7) \- This adds anonymised database statistics to msfconsole's debug command, which is used to help developers track down database issues as part of user generated error reports.
  * [#15929](https://github.com/rapid7/metasploit-framework/pull/15929) from [bcoles](https://github.com/bcoles) \- This adds nine new Windows 2003 SP2 targets that the exploit/windows/smb/ms08_067_netapi module can exploit.



## Bugs fixed

  * [#15808](https://github.com/rapid7/metasploit-framework/pull/15808) from [timwr](https://github.com/timwr) \- This fixes a compatibility issue with Powershell read_file on Windows Server 2012 by using the old style Powershell syntax (New-Object).
  * [#15937](https://github.com/rapid7/metasploit-framework/pull/15937) from [adfoster-r7](https://github.com/adfoster-r7) \- This removes usage of SortedSet to improve support for Ruby 3.
  * [#15939](https://github.com/rapid7/metasploit-framework/pull/15939) from [zeroSteiner](https://github.com/zeroSteiner) \- This fixes a bug where the Meterpreter dir/ls function would show the creation date instead of the modified date for the directory contents.



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.1.17...6.1.19](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222021-12-02T11%3A01%3A28-06%3A00..2021-12-09T08%3A35%3A23%2B00%3A00%22)
  * [Full diff 6.1.17...6.1.19](https://github.com/rapid7/metasploit-framework/compare/6.1.17...6.1.19)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
[binary installers](/products/metasploit/download.jsp) (which also include the commercial edition).

## Article tags

  * [Metasploit](/blog/tag/metasploit/)
  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Exploits](/blog/tag/exploits/)
  * [Research](/blog/tag/research/)