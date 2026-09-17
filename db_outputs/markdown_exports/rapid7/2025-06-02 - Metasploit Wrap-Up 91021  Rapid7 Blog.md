# Metasploit Wrap-Up: 9/10/21 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/09/10/metasploit-wrap-up-129/
- **Date :** 2025-06-02

---

## Confluence Server OGNL Injection

Our own wvu along with [Jang](https://twitter.com/testanull) added a module that exploits an OGNL injection ([CVE-2021-26804](https://attackerkb.com/topics/Eu74wdMbEL/cve-2021-26084-confluence-server-ognl-injection))in Atlassian Confluence's WebWork component to execute commands as the Tomcat user. CVE-2021-26804 is a critical remote code execution vulnerability in Confluence Server and Confluence Data Center and is actively being exploited in the wild. Initial discovery of this exploit was by Benny Jacob (SnowyOwl).

## More Enhancements

In addition to the module, we would like to highlight some of the enhancements that have been added for this release. Contributor [e2002e](https://github.com/e2002e) added the OUTFILE and DATABASE options to the zoomeye_search module allowing users to save results to a local file or local database along with improving the output of the module to provide better information about the target. Our own [dwelch-r7](https://github.com/dwelch-r7) has added support for fully interactive shells against Linux environments with shell -it. In order to use this functionality, users will have to enable the feature flag with features set fully_interactive_shells true. Contributor [pingport80](https://github.com/pingport80) has added powershell support for write_file method that is binary safe and has also replaced explicit cat calls with file reads from the file library to provide broader support.

## New module content (1)

  * [Atlassian Confluence WebWork OGNL Injection](https://github.com/rapid7/metasploit-framework/pull/15645) by wvu, [Benny Jacob](https://twitter.com/bennyyjacob), and [Jang](https://twitter.com/testanull), which exploits [CVE-2021-26084](https://attackerkb.com/topics/Eu74wdMbEL/cve-2021-26084-confluence-server-ognl-injection?referrer=blog) \- This adds an exploit module targeting an OGNL injection vulnerability (CVE-2021-26084) in Atlassian Confluence's WebWork component to execute commands as the Tomcat user.



## Enhancements and features

  * [#15278](https://github.com/rapid7/metasploit-framework/pull/15278) from [e2002e](https://github.com/e2002e) \- The zoomeye_search module has been enhanced to add the OUTFILE and DATABASE options, which allow users to save results to a local file or to the local database respectively. Additionally the output saved has been improved to provide better information about the target and additional error handling has been added to better handle potential edge cases.
  * [#15522](https://github.com/rapid7/metasploit-framework/pull/15522) from [dwelch-r7](https://github.com/dwelch-r7) \- Adds support for fully interactive shells against Linux environments with shell -it. This functionality is behind a feature flag and can be enabled with features set fully_interactive_shells true
  * [#15560](https://github.com/rapid7/metasploit-framework/pull/15560) from [pingport80](https://github.com/pingport80) \- This PR add powershell support for write_file method that is binary safe.
  * [#15627](https://github.com/rapid7/metasploit-framework/pull/15627) from [pingport80](https://github.com/pingport80) \- This PR removes explicit cat calls and replaces them with file reads from the file library so that they have broader support.



## Bugs fixed

  * [#15634](https://github.com/rapid7/metasploit-framework/pull/15634) from [maikthulhu](https://github.com/maikthulhu) \- This PR fixes an issue in exploit/multi/misc/erlang_cookie_rce where a missing bitwise flag caused the exploit to fail in some circumstances.
  * [#15636](https://github.com/rapid7/metasploit-framework/pull/15636) from [adfoster-r7](https://github.com/adfoster-r7) \- Fixes a regression in datastore serialization that caused some event processing to fail.
  * [#15637](https://github.com/rapid7/metasploit-framework/pull/15637) from [adfoster-r7](https://github.com/adfoster-r7) \- Fixes a regression issue were Metasploit incorrectly marked ipv6 address as having an 'invalid protocol'
  * [#15639](https://github.com/rapid7/metasploit-framework/pull/15639) from [gwillcox-r7](https://github.com/gwillcox-r7) \- This fixes a bug in the rename_files method that would occur when run on a non-Windows shell session.
  * [#15640](https://github.com/rapid7/metasploit-framework/pull/15640) from [adfoster-r7](https://github.com/adfoster-r7) \- Updates modules/auxiliary/gather/office365userenum.py to require python3
  * [#15652](https://github.com/rapid7/metasploit-framework/pull/15652) from [jmartin-r7](https://github.com/jmartin-r7) \- A missing dependency, py3-pip, was preventing certain external modules such as auxiliary/gather/office365userenum from working due to requests requiring py3-pip to run properly. This has been fixed by updating the Docker container to install the missing py3-pip dependency.
  * [#15654](https://github.com/rapid7/metasploit-framework/pull/15654) from [space-r7](https://github.com/space-r7) \- A bug has been fixed in lib/msf/core/payload/windows/encrypted_reverse_tcp.rb whereby a call to recv() was not being passed the proper arguments to receive the full payload before returning. This could result in cases where only part of the payload was received before continuing, which would have resulted in a crash. This has been fixed by adding a flag to the recv() function call to ensure it receives the entire payload before returning.
  * [#15655](https://github.com/rapid7/metasploit-framework/pull/15655) from [adfoster-r7](https://github.com/adfoster-r7) \- This cleans up the MySQL client-side options that are used within the library code.



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.1.3...6.1.5](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222021-09-02T10%3A13%3A16-05%3A00..2021-09-08T18%3A07%3A57-05%3A00%22)
  * [Full diff 6.1.3...6.1.5](https://github.com/rapid7/metasploit-framework/compare/6.1.3...6.1.5)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
[binary installers](/products/metasploit/download/) (which also include the commercial edition).

## Article tags

  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Metasploit](/blog/tag/metasploit/)
  * [Exploits](/blog/tag/exploits/)
  * [Vulnerability Management](/blog/tag/vulnerability-management/)
  * [Research](/blog/tag/research/)