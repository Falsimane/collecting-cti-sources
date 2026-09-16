# Metasploit Wrap-Up: Feb. 11, 2022 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/02/11/metasploit-wrap-up-148/
- **Date :** 2025-06-02

---

## Welcome, Little Hippo: PetitPotam

Our very own [@zeroSteiner](https://github.com/zeroSteiner) [ported](https://github.com/rapid7/metasploit-framework/pull/16136) the [PetitPotam](https://github.com/topotam/PetitPotam) exploit to Metasploit this week. This module leverages [CVE-2021-36942](https://attackerkb.com/topics/TEBmUAfeCs/cve-2021-36942?referrer=blog), a vulnerability in the Windows Encrypting File System (EFS) API, to capture machine NTLM hashes. This uses the EfsRpcOpenFileRaw function of the Microsoft’s Encrypting File System Remote Protocol API ([MS-EFSRPC](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-efsr/08796ba8-01c8-4872-9221-1000ec2eff31)) to coerce machine authentication to a user-controlled listener host. Metasploit's [SMB capture server](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/server/capture/smb.rb) module can be used for this. The captured hashes are typically used as part of a NTLM relaying attack to take over other Windows hosts. Note that Microsoft has published some [guidance](https://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429) about how to mitigate NTLM relay attacks.

## QEMU Human Monitor Interface RCE

Contributor [@bcoles](https://github.com/bcoles) added an exploit [module](https://github.com/rapid7/metasploit-framework/pull/16151) that abuse QEMU's Monitor Human Monitor Interface (HMP) TCP server to execute arbitrary commands by using the migrate HMP command. Furthermore, since the HMP TCP service is reachable from emulated devices, it is possible to escape QEMU from a guest system using this module. Note that it doesn't work on Windows hosts since the migrate command cannot spawn processes on this platform.

## New module content (2)

  * [PetitPotam](https://github.com/rapid7/metasploit-framework/pull/16136) by [GILLES Lionel](https://github.com/topotam) and [Spencer McIntyre](https://github.com/zeroSteiner), which exploits [CVE-2021-36942](https://attackerkb.com/topics/TEBmUAfeCs/cve-2021-36942?referrer=blog) \- This adds a new auxiliary scanner module that ports the PetitPotam tool to Metasploit andleverages CVE-2021-36942 to coerce Windows hosts to authenticate to a user-specific host, which enables an attacker to capture NTLM credentials for further actions, such as relay attacks.
  * [QEMU Monitor HMP 'migrate' Command Execution](https://github.com/rapid7/metasploit-framework/pull/16151) by [bcoles](https://github.com/bcoles) \- This adds a module that can exploit the QEMU HMP service to execute OS commands. The HMP TCP service is reachable from emulated devices, so it is possible to escape QEMU by exploiting this vulnerability.



## Enhancements and features

  * [#16010](https://github.com/rapid7/metasploit-framework/pull/16010) from [lap1nou](https://github.com/lap1nou) \- This updates the zabbix_script_exec module with support for Zabbix version 5.0 and later. It also adds a new item-based execution technique and support for delivering Linux native payloads.
  * [#16163](https://github.com/rapid7/metasploit-framework/pull/16163) from [zeroSteiner](https://github.com/zeroSteiner) \- Support has been added for the ClaimsPrincipal .NET deserialization gadget chain, which was found by [jang](https://github.com/testanull). An exploit which utilizes this enhancement will arrive shortly.
  * [#16125](https://github.com/rapid7/metasploit-framework/pull/16125) from [bcoles](https://github.com/bcoles) \- This module can exploit GXV3140 models now that an ARCH_CMD target has been added.



## Bugs fixed

  * [#16121](https://github.com/rapid7/metasploit-framework/pull/16121) from [timwr](https://github.com/timwr) \- This fixes an exception caused by exploits that call rhost() in Msf::Post::Common without a valid session.
  * [#16142](https://github.com/rapid7/metasploit-framework/pull/16142) from [timwr](https://github.com/timwr) \- This fixes an issue with Meterpreter's getenv command that was not returning NULL when querying for a non-existing environment variable.
  * [#16143](https://github.com/rapid7/metasploit-framework/pull/16143) from [sjanusz-r7](https://github.com/sjanusz-r7) \- This fixes an issue where a Cygwin SSH session was not correctly identified being a Windows device, due to a case sensitivity issue
  * [#16147](https://github.com/rapid7/metasploit-framework/pull/16147) from [zeroSteiner](https://github.com/zeroSteiner) \- This fixes a bug where ssh_enumusers would only use one source in the generation of its user word list if both USERNAME and USER_FILE options were set. The module now pulls from all possible datastore options if they are set, including a new option DB_ALL_USERS.
  * [#16160](https://github.com/rapid7/metasploit-framework/pull/16160) from [zeroSteiner](https://github.com/zeroSteiner) \- This fixes a crash when msfconsole is unable to correctly determine the hostname and current user within a shell prompt.



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.1.28...6.1.29](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222022-02-03T12%3A28%3A59%2B00%3A00..2022-02-09T14%3A46%3A38-06%3A00%22)
  * [Full diff 6.1.28...6.1.29](https://github.com/rapid7/metasploit-framework/compare/6.1.28...6.1.29)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
[binary installers](/products/metasploit/download/) (which also include the commercial edition).

## Article tags

  * [Metasploit](/blog/tag/metasploit/)
  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Penetration Testing](/blog/tag/penetration-testing/)
  * [Research](/blog/tag/research/)