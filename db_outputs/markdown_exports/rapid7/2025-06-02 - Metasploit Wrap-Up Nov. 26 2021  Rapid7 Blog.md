# Metasploit Wrap-Up: Nov. 26 2021 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/11/26/metasploit-wrap-up-140/
- **Date :** 2025-06-02

---

## Self-Service Remote Code Execution

This week, our own @wvu-r7 added an exploit [module](https://github.com/rapid7/metasploit-framework/pull/15874) that achieves unauthenticated remote code execution in ManageEngine ADSelfService Plus, a self-service password management and single sign-on solution for Active Directory. This new module leverages a REST API authentication bypass vulnerability identified as [CVE-2021-40539](https://attackerkb.com/topics/DMSNq5zgcW/cve-2021-40539?referrer=blog), where an error in the REST API URL normalization routine makes it possible to bypass security filters and upload arbitrary files on the target. wvu’s new module simply uploads a Java payload to the target and executes it, granting code execution as SYSTEM if ManageEngine ADSelfService Plus was started as a service.

## Storm Alert

Warning, this is not a drill! A critical unauthenticated command injection vulnerability is approaching the Nimbus service component of Apache Storm and has been given the name [CVE-2021-38294](https://attackerkb.com/topics/xvmqwPRnm5/cve-2021-38294?referrer=blog). A new exploit [module](https://github.com/rapid7/metasploit-framework/pull/15866) authored by our very own [zeroSteiner](https://github.com/zeroSteiner) has landed and will exploit this vulnerability to get you OS command execution as the user that started the Nimbus service. Please, evacuate the area immediately!

## Metasploit Community CTF 2021

We're happy to announce this year’s CTF will start on Friday, December 3, 2021! Similar to last year, the game has been designed to be accessible to beginners who want to learn and connect with the community. Keep in mind that while a team can have unlimited members, only 1,000 team spots are available, and once they’re gone you will have to join someone else’s team. You can find the full details in our [blog post](/blog/post/2021/11/16/announcing-the-2021-metasploit-community-ctf/).

## New module content (2)

  * [Apache Storm Nimbus getTopologyHistory Unauthenticated Command Execution](https://github.com/rapid7/metasploit-framework/pull/15866) by [Alvaro Muñoz](https://github.com/pwntester) and [Spencer McIntyre](https://github.com/zeroSteiner), which exploits [CVE-2021-38294](https://attackerkb.com/topics/xvmqwPRnm5/cve-2021-38294?referrer=blog) \- This adds an exploit for CVE-2021-38294 which is an unauthenticated remote command execution vulnerability within the getTopologyHistory() RPC method that is provided by the Nimbus service which is a component of the Apache Storm project. In order to be exploitable, at least one topology must have been submitted to the Storm cluster. It may be active or inactive but one must be present.
  * [ManageEngine ADSelfService Plus CVE-2021-40539](https://github.com/rapid7/metasploit-framework/pull/15874) by wvu, [Antoine Cervoise](https://github.com/cervoise), [Wilfried Bécard](https://github.com/wilfried-becard), and [mr_me](https://github.com/stevenseeley), which exploits [CVE-2021-40539](https://attackerkb.com/topics/DMSNq5zgcW/cve-2021-40539?referrer=blog) \- This adds an exploit for CVE-2021-40539 which is an unauthenticated RCE within the ManageEngine ADSelfService application.



## Enhancements and features

  * [#15887](https://github.com/rapid7/metasploit-framework/pull/15887) from [smashery](https://github.com/smashery) \- The path expansion code has been expanded to support path-based tab completion. Users should now tab-complete things such as cat ~/some_filenam<tab>.
  * [#15889](https://github.com/rapid7/metasploit-framework/pull/15889) from [dwelch-r7](https://github.com/dwelch-r7) \- An update has been made to library code so that terminal resize events are only sent if the Meterpreter client supports it. Additionally, extra feedback is now provided to users on whether or not terminal resizing is handled automatically or if they should adjust it manually.
  * [#15898](https://github.com/rapid7/metasploit-framework/pull/15898) from [jmartin-r7](https://github.com/jmartin-r7) \- Ruby 3.x removes support for URI.encode and URI.escape. This PR replaces uses of these functions in modules with calls to URI::DEFAULT_PARSER.escape so that Ruby 3 can run these modules instead of raising errors about missing functions.
  * [#15899](https://github.com/rapid7/metasploit-framework/pull/15899) from [dwelch-r7](https://github.com/dwelch-r7) \- This improves the user experience when shell is invoked from a Meterpreter session. Now, when the fully_interactive_shells feature is enabled, a message is displayed to inform the operator that a fully interactive TTY is supported. Note that you can start it by invoking shell -it.



## Bugs fixed

  * [#15864](https://github.com/rapid7/metasploit-framework/pull/15864) from [timwr](https://github.com/timwr) \- A bug has been fixed whereby the sessions -u command would not return a x64 Meterpreter session on a x64 Windows host, and would instead return a x86 session. This issue has now been addressed so that sessions -u will determine the architecture of the target host prior to upgrading and will generate a new Meterpreter session of the appropriate architecture.



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.1.15...6.1.16](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222021-11-17T15%3A27%3A48-06%3A00..2021-11-24T18%3A00%3A22-06%3A00%22)
  * [Full diff 6.1.15...6.1.16](https://github.com/rapid7/metasploit-framework/compare/6.1.15...6.1.16)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
binary installers (which also include the commercial edition).

## Article tags

  * [Metasploit](/blog/tag/metasploit/)
  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Exploits](/blog/tag/exploits/)
  * [Research](/blog/tag/research/)