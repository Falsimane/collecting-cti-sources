# Metasploit Wrap-Up: 11/19/21 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/11/19/metasploit-wrap-up-139/
- **Date :** 2025-06-02

---

## Azure Active Directory login scanner module

Community contributor [k0pak4](https://github.com/k0pak4) added a new [login scanner module for Azure Active Directory](https://github.com/rapid7/metasploit-framework/pull/15755). This module exploits a [vulnerable](https://attackerkb.com/topics/rZ1JlQhXhc/cve-2020-16152?referrer=blog) authentication endpoint in order to enumerate usernames without generating log events. The error code returned by the endpoint can be used to discover the validity of usernames in the target Azure tenant. If a tenant's domain is known, the module can also be used to brute-force login credentials by providing a list of usernames and passwords.

## Aerohive NetConfig RCE module

Also new this week, community contributor [Erik Wynter](https://github.com/ErikWynter) added an [exploit module for Aerohive NetConfig](https://github.com/rapid7/metasploit-framework/pull/15700), versions 10.0r8a build-242466 and below. These versions are [vulnerable](https://attackerkb.com/topics/rZ1JlQhXhc/cve-2020-16152?referrer=blog) to local file inclusion and log poisoning, as they rely on a version of PHP 5 that is affected by string truncation attacks. This allows users to achieve unauthenticated remote code execution as root on vulnerable systems.

## 2021 Metasploit community CTF

In case you missed the [announcement earlier this week](/blog/post/2021/11/16/announcing-the-2021-metasploit-community-ctf/), the 2021 edition of the Metasploit community CTF is set to kick off [two weeks from today](https://time.is/1100AM_03_Dec_in_CT?Metasploit_community_CTF_Start)! Registration starts Monday, November 22 for up to 750 teams, with capacity for an additional 250 teams once play starts on Friday, December 3. Many thanks to TryHackMe for sponsoring the event and providing some great [prizes](/blog/post/2021/11/16/announcing-the-2021-metasploit-community-ctf/#prizes). Find some teammates and mark your calendars, because this year's event should be a great challenge and a lot of fun for both beginners and CTF veterans!

## New module content (4)

  * [Jetty WEB-INF File Disclosure](https://github.com/rapid7/metasploit-framework/pull/15843) by Mayank Deshmukh, cangqingzhe, charlesk40, h00die, and lachlan roberts, which exploits [CVE-2021-28164](https://attackerkb.com/topics/jp2jbsKGkp/cve-2021-28164?referrer=blog) \- This adds an auxiliary module that retrieves sensitive files from Jetty versions 9.4.37.v20210219, 9.4.38.v20210224, 9.4.37-9.4.42, 10.0.1-10.0.5, and 11.0.1-11.0.5 . Protected resources behind the WEB-INF path can be accessed due to servlet implementations improperly handling URIs containing certain encoded characters.
  * [Microsoft Azure Active Directory Login Enumeration](https://github.com/rapid7/metasploit-framework/pull/15755) by Matthew Dunn - k0pak4 - This adds an auxiliary scanner module that leverages Azure Active Directory authentication flaw to enumerate usernames without generating log events. The module also supports brute-forcing passwords against this tenant.
  * [Aerohive NetConfig 10.0r8a LFI and log poisoning to RCE](https://github.com/rapid7/metasploit-framework/pull/15700) by Erik Wynter and Erik de Jong, which exploits [CVE-2020-16152](https://attackerkb.com/topics/rZ1JlQhXhc/cve-2020-16152?referrer=blog) \- This change adds a new module to exploit LFI and log poisoning vulnerabilities (CVE-2020-16152) in Aerohive NetConfig, version 10.0r8a build-242466 and older in order to achieve unauthenticated remote code execution as the root user.
  * [Sitecore Experience Platform (XP) PreAuth Deserialization RCE](https://github.com/rapid7/metasploit-framework/pull/15858) by AssetNote and gwillcox-r7, which exploits [CVE-2021-42237](https://attackerkb.com/topics/g2wzJERRtL/cve-2021-42237?referrer=blog) \- This adds an exploit for CVE-2021-42237 which is an unauthenticated RCE within the Sitecore Experience Platform. The vulnerability is due to the deserialization of untrusted data submitted by the attacker.



## Enhancements and features

  * [#15796](https://github.com/rapid7/metasploit-framework/pull/15796) from [zeroSteiner](https://github.com/zeroSteiner) \- Support for pivoted SSL server connections as used by capture modules and listeners has been added to Metasploit. The support works for both Meterpreter sessions and SSH sessions.
  * [#15851](https://github.com/rapid7/metasploit-framework/pull/15851) from [smashery](https://github.com/smashery) \- Update several modules and core libraries so that now when sending HTTP requests that include user agents, the user agents are modernized, and are randomized at msfconsole start time. Users can also now request Rex to generate a random user agent from one of the ones in the User Agent pool should they need a random user agent for a particular module.
  * [#15862](https://github.com/rapid7/metasploit-framework/pull/15862) from [smashery](https://github.com/smashery) \- Updates have been made to Linux Meterpreter libraries to support expanding environment variables in several different commands. This should provide users with a smoother experience when using environment variables in commands such as cd, ls, download, upload, mkdir and similar commands.
  * [#15867](https://github.com/rapid7/metasploit-framework/pull/15867) from [h00die](https://github.com/h00die) \- The example modules have been updated to conform to current RuboCop rules and to better reflect recent changes in the Metasploit Framework coding standards, as well as to better showcase various features that may be needed when developing exploits.
  * [#15878](https://github.com/rapid7/metasploit-framework/pull/15878) from [smashery](https://github.com/smashery) \- This fixes an issue whereby tab-completing a remote folder in Meterpreter would append a space onto the end. This change resolves that by not appending the space if we're potentially in the middle of a tab completion journey, and adding a slash if we've completed a directory, providing a smoother tab completion experience for users.



## Bugs fixed

  * [#15875](https://github.com/rapid7/metasploit-framework/pull/15875) from [smashery](https://github.com/smashery) \- This fixes an issue with the reverse Bash command shell payloads where they would not work outside of the context of bash.
  * [#15879](https://github.com/rapid7/metasploit-framework/pull/15879) from [jmartin-r7](https://github.com/jmartin-r7) \- Updates batch scanner modules to no longer crash when being able to unable to correctly calculate a scanner thread's batch size



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.1.14...6.1.15](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222021-11-11T11%3A51%3A19-06%3A00..2021-11-17T15%3A27%3A48-06%3A00%22)
  * [Full diff 6.1.14...6.1.15](https://github.com/rapid7/metasploit-framework/compare/6.1.14...6.1.15)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
[binary installers](/products/metasploit/download.jsp) (which also include the commercial edition).

## Article tags

  * [Metasploit](/blog/tag/metasploit/)
  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Exploits](/blog/tag/exploits/)
  * [Research](/blog/tag/research/)