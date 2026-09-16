# Metasploit Wrap-Up 8/6/21 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/08/06/metasploit-wrap-up-124/
- **Date :** 2025-06-02

---

## Desert heat (not the 1999 film)

This week was more quiet than normal with Black Hat USA and DEF CON, but that didn’t stop the team from delivering some small enhancements and bug fixes! We are also excited to see two new modules [#15519](https://github.com/rapid7/metasploit-framework/pull/15519) and [#15520](https://github.com/rapid7/metasploit-framework/pull/15520) from researcher [Jacob Baines’](https://twitter.com/Junior_Baines) DEF CON talk [​​Bring Your Own Print Driver Vulnerability](https://www.youtube.com/watch?v=vdesswZYz-8) already appear in the PR queue. Keep an eye out for those modules in the near future!

Our very own [Simon Janusz](https://github.com/sjanusz-r7) enhanced the CommandDispatcher and SessionManager to support using a negative ID with both the jobs and sessions commands. Quickly access the last job or session by passing -1 to the command. The change allows users to upgrade the most recently opened session to meterpreter using the command sessions -u -1, thus removing the need to run the post/multi/manage/shell_to_meterpreter module.

In addition, our very own [Alan David Foster](https://github.com/adfoster-r7) updated the PostgreSQL scanner/postgres/postgres_schemadump module so that it does not ignore the default postgres database. That default database might contain valuable information after all! The enhancements also introduce a new datastore option, IGNORED_DATABASES, to configure a list of databases ignored during the schema dump.

## Enhancements and features

  * [#15492](https://github.com/rapid7/metasploit-framework/pull/15492) from [sjanusz-r7](https://github.com/sjanusz-r7) \- Adds support for negative session and job ids.
  * [#15498](https://github.com/rapid7/metasploit-framework/pull/15498) from [adfoster-r7](https://github.com/adfoster-r7) \- Updates the PostgreSQL schema_dump module to no longer ignore the default postgres database which may contain useful information, and adds a new datastore option to configure ignored databases.



## Bugs fixed

  * [#15500](https://github.com/rapid7/metasploit-framework/pull/15500) from [agalway-r7](https://github.com/agalway-r7) \- Fixes a regression issue for gitlab_file_read_rce and cacti_filter_sqli_rce where the modules failed to run
  * [#15503](https://github.com/rapid7/metasploit-framework/pull/15503) from [jheysel-r7](https://github.com/jheysel-r7) \- A bug has been fixed in the Cisco Hyperflex file upload RCE module that prevented it from properly deleting the uploaded payload files. Uploaded payload files should now be properly deleted.



## Get it

As always, you can update to the latest Metasploit Framework with msfupdate  
and you can get more details on the changes since the last blog post from  
GitHub:

  * [Pull Requests 6.0.55...6.0.56](https://github.com/rapid7/metasploit-framework/pulls?q=is:pr+merged:%222021-07-29T12%3A01%3A27-05%3A00..2021-08-04T11%3A50%3A27%2B01%3A00%22)
  * [Full diff 6.0.55...6.0.56](https://github.com/rapid7/metasploit-framework/compare/6.0.55...6.0.56)



If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest.  
To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the  
[binary installers](/products/metasploit/download) (which also include the commercial edition).

## Article tags

  * [Metasploit](/blog/tag/metasploit/)
  * [Metasploit Weekly Wrapup](/blog/tag/metasploit-weekly-wrapup/)
  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Exploits](/blog/tag/exploits/)
  * [Research](/blog/tag/research/)