# Metasploit Wrap-Up: 12/3/21 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/12/03/metasploit-wrap-up-141/
- **Date :** 2025-06-02

---

## Metasploit CTF 2021 starts today

It’s that time of year again! Time for the [2021 Metasploit Community CTF](/blog/post/2021/11/16/announcing-the-2021-metasploit-community-ctf/). Earlier today over 1,100 users in more than 530 teams were registered and opened for participation to solve this year’s 18 challenges. Next week a recap and the winners will be announced, so stay tuned for more information.

## Overlayfs LPE

This week Metasploit shipped an exploit for the recent Overlayfs vulnerability in Ubuntu Linux. The exploit works on Ubuntu 14.04 through 20.10, for both the x64 and aarch64 architectures making it very accessible. The vulnerability leverages a lack of verification within the Overlayfs implementation and can be exploited reliably.

## Older Exploit Improvements

Community member [bcoles](https://github.com/bcoles) made a number of improvements to some older Windows exploits this week. The exploit for MS-03-026 now includes a check method along with modules docs. MS-05-039 was tested and found to be reliable regardless of the target language pack so the target was updated to reflect this. Additionally, MS-07-029 has 13 new targets for different Server 2000 and Server 2003 language packs. This set of improvements will go a long way in helping users test these critical vulnerabilities in older versions of Windows.

## New module content (1)

  * [2021 Ubuntu Overlayfs LPE](https://github.com/rapid7/metasploit-framework/pull/15822) by bwatters-r7 and ssd-disclosure, which exploits [CVE-2021-3493](https://attackerkb.com/topics/2k7PE1nW2p/cve-2021-3493?referrer=blog) \- Adds a module for the CVE-2021-3493 overlay fs local privilege escalation for Ubuntu versions 14.04 - 20.10.



## Enhancements and features

  * [#15914](https://github.com/rapid7/metasploit-framework/pull/15914) from [bcoles](https://github.com/bcoles) \- This improves upon the exploit/windows/dcerpc/ms03_026_dcom module by adding a check method, documentation, and cleaning up the code.
  * [#15915](https://github.com/rapid7/metasploit-framework/pull/15915) from [bcoles](https://github.com/bcoles) \- This renames the Windows 2000 SP4 Languages targets in thems05_039_pnp exploit to Windows 2000 SP4 Universal. It has been tested and was determined to not be language pack dependent.
  * [#15918](https://github.com/rapid7/metasploit-framework/pull/15918) from [bcoles](https://github.com/bcoles) \- This adds 13 new language pack-specific targets to the ms07_029_msdns_zonename exploit.
  * [#15920](https://github.com/rapid7/metasploit-framework/pull/15920) from [smashery](https://github.com/smashery) \- This adds tab completion support to the powershell_import command.
  * [#15928](https://github.com/rapid7/metasploit-framework/pull/15928) from [jmartin-r7](https://github.com/jmartin-r7) \- This updates Metasploit Framework's default Ruby version from 2.7 to 3. There should be no end-user impact.



## Bugs fixed

  * [#15897](https://github.com/rapid7/metasploit-framework/pull/15897) from [timwr](https://github.com/timwr) \- This fixes modules that check the return value of write_file() calls by returning a boolean value instead of nil.
  * [#15913](https://github.com/rapid7/metasploit-framework/pull/15913) from [timwr](https://github.com/timwr) \- This fixes handling for shellwords parsing of malformed user-supplied input, such as unmatched quotes, when interacting with command shell sessions.
  * [#15917](https://github.com/rapid7/metasploit-framework/pull/15917) from [smashery](https://github.com/smashery) \- This fixes a tab completion bug in Meterpreter.



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.1.16...6.1.17](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222021-11-24T18%3A00%3A22-06%3A00..2021-12-02T11%3A01%3A28-06%3A00%22)
  * [Full diff 6.1.16...6.1.17](https://github.com/rapid7/metasploit-framework/compare/6.1.16...6.1.17)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
[binary installers](/products/metasploit/download/) (which also include the commercial edition).

## Article tags

  * [Metasploit](/blog/tag/metasploit/)
  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Exploits](/blog/tag/exploits/)
  * [Research](/blog/tag/research/)