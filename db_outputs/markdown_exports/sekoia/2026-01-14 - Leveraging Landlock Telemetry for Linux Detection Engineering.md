# Leveraging Landlock Telemetry for Linux Detection Engineering

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/leveraging-landlock-telemetry-for-linux-detection-engineering
- **Date :** 2026-01-14

---

## Introduction

During our daily tracking and analysis routine at **SekoiaTDR** team (Threat Detection & Research), we are always searching for new relevant detection opportunities on various perimeters. Given the predominance of Linux-based systems on the server side, we decided to focus the current report on one recent security mechanism called Landlock. 

[Landlock](https://landlock.io) is a relatively new Linux Security Module (LSM), integrated into the kernel since version 5.13. Its main differentiators from other LSMs are summarised in the following table from [this Landlock paper](https://landlock.io/talks/2024-06-06_landlock-article.pdf):

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5364b4041c693434691_6a92a169db65986262adaea4_6a2a800562f00361bfdd9a20.webp)

**_Figure 1._**[**_Comparison_**](https://landlock.io/talks/2024-06-06_landlock-article.pdf)** _of different access control mechanism_**

Landlock allows the creation of sandboxes for your applications, on top of the existing system-wide access control mechanisms. Essentially, any process, whether you trust them or not, whether they are privileged processes or unprivileged ones, can be restricted, adding a valuable layer of defence-in-depth. 

Despite promising capabilities, the relative novelty of Landlock within the Linux kernel raises a critical question for detection engineering. How widely is it actually used?

To answer that question, Landlock creator [listed](https://landlock.io/talks/2025-09-30_landlock-systemd-asg.pdf) several open source projects already leveraging Landlock: _zathura, pacman, cloud hypervisor, suricata, polkadot, wireproxy, gnome localsearch, xz utils._ Several sandbox tools such as _FireJail_ and _setpriv_ have integrated Landlock as well. In addition, multiple private companies have already looked into Landlock for their own usage to harden their applications.

## Landlock for detection engineering

Landlock is a great hardening tool that effectively restricts an application’s actions. However, its application is not limited to system hardening, as it also presents significant value for detection engineering.

Landlock has been fully integrated within the Audit system since [Linux kernel 6.15](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=72885116069abdd05c245707c3989fc605632970). No specific audit rule is needed. By default, the execution of new programs via the `execve()` system call does not generate logs; enabling this behaviour requires passing [specific flags](https://docs.kernel.org/userspace-api/landlock.html#c.sys_landlock_restrict_self) to `sys_landlock_restrict_self()`. This default configuration is intended to mitigate false positives, given the inherent lack of control over the execution flow of the new processes. Furthermore, appropriate access rights must be defined during binary compilation, in accordance with the [official documentation](https://docs.kernel.org/userspace-api/landlock.html#access-rights).

A log being raised means two things: 

  * The application is not used for its original purpose since it was compiled with these Landlock restrictions.
  * It should never be a false positive since the application was designed at its core with the Landlock restrictions.



For detection engineers, this new telemetry opens up new possibilities for crafting precise, behaviour-based detections that can identify threats at runtime with a very low false positive rate. 

The Landlock [sandboxer example](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/samples/landlock/sandboxer.c) in C helps to understand how it works. The program allows the user to execute a process under several user-defined conditions. We can run elementary tests to validate the logging capabilities. 

Every violation attempt of the restrictions applied to a program will be logged if the environment variable `LL_FORCE_LOG` is set to 1. This sets the flag `LANDLOCK_RESTRICT_SELF_LOG_NEW_EXEC_ON`, allowing the execution of new programs via the `execve()` system call.

### Filesystem Landlock rule

We start our “sandboxer” binary with an interactive “bash” shell, and restrict with Landlock the filesystem permissions to be read-only on the “/” path, and read-write on the “/tmp” path.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5364b4041c693434697_6a92a167dae089660dfb9e2d_6a2a800562f00361bfdd9a1a.webp)

**_Figure 2. Shell commands testing Landlock filesystem rule_**

If we try to write anywhere else other than “/tmp”, the audit logging gives us these raw [documented](https://docs.kernel.org/admin-guide/LSM/landlock.html) Landlock audit messages:

`type=UNKNOWN[1423] msg=audit(1764079004.833:1261): domain=1266faee0 blockers=fs.make_reg path="/home/user/sandbox_c" dev="sda1" ino=1183972`

At the time of writing this, the [audit userspace tools](https://github.com/linux-audit/audit-userspace) were not updated with the audit kernel type of messages: the 1423 message code is the following one:

`#define AUDIT_LANDLOCK_ACCESS 1423 /* Landlock denial */`

Using the [go-libaudit library](https://github.com/elastic/go-libaudit), audit messages are reassembled and enriched with system context in a single event that could be used for detection or hunting :

`{"@timestamp":"2025-11-25T13:46:48.03Z","sequence":1228,"category":"mac","record_type":"unknown[1423]","result":"fail","session":"unset","tags":["x86_64"],"summary":{"actor":{"primary":"unset","secondary":"user"},"object":{},"how":"/usr/bin/touch"},"user":{"ids":{"auid":"unset","egid":"1000","euid":"1000","fsgid":"1000","fsuid":"1000","gid":"1000","sgid":"1000","suid":"1000","uid":"1000"},"names":{"egid":"user","euid":"user","fsgid":"user","fsuid":"user","gid":"user","sgid":"user","suid":"user","uid":"user"},"selinux":{"user":"unconfined"}},"process":{"pid":"4480","ppid":"1767","title":"touch password.txt","name":"touch","exe":"/usr/bin/touch"},"data":{"a0":"ffffffffffffff9c","a1":"7ffd04a91331","a2":"941","a3":"1b6","arch":"x86_64","blockers":"fs.make_reg","dev":"sda1","domain":"1266faee0","exit":"EACCES","ino":"1183972","path":"/home/user/sandbox_c","syscall":"openat","tty":"pts1"}}`

### Network Landlock rule

Similarly to our previous example, we start our “sandboxer” binary, still with an interactive “bash” shell, and add some restrictions to limit TCP connections to port 443:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5364b4041c69343469a_6a92a16b2e47a1e9fe0ceb3f_6a2a800562f00361bfdd9a23.webp)

**_Figure 3. Shell commands testing Landlock network rule_**

Then, trying to connect with the “curl” command to “http://google.com” (meaning on port 80). The resulting log event, here for IPv4, is:

`type=UNKNOWN[1423] msg=audit(1764080735.711:1623): domain=1266faef9 blockers=net.connect_tcp daddr=142.250.179.110 dest=80`

And with the go-libaudit library:

`{"@timestamp":"2025-11-25T14:25:35.711Z","sequence":1623,"category":"mac","record_type":"unknown[1423]","result":"fail","session":"unset","tags":["x86_64"],"summary":{"actor":{"primary":"unset","secondary":"user"},"object":{},"how":"/usr/bin/curl"},"user":{"ids":{"auid":"unset","egid":"1000","euid":"1000","fsgid":"1000","fsuid":"1000","gid":"1000","sgid":"1000","suid":"1000","uid":"1000"},"names":{"egid":"user","euid":"user","fsgid":"user","fsuid":"user","gid":"user","sgid":"user","suid":"user","uid":"user"},"selinux":{"user":"unconfined"}},"process":{"pid":"5482","ppid":"5470","title":"curl https://google.com","name":"curl","exe":"/usr/bin/curl"},"data":{"a0":"5","a1":"5611825b7088","a2":"10","a3":"0","arch":"x86_64","blockers":"net.connect_tcp","daddr":"142.250.179.110","dest":"80","domain":"1266faef9","exit":"EACCES","syscall":"connect","tty":"pts1"}}`

With these logging capabilities, Landlock provides everything required for detection engineers to build straightforward detection rules. 

Sekoia.io Endpoint Agent, as it uses go-libaudit library, collects by default the previously mentioned events. Since these logs are shipped into the Sekoia SOC platform, we can use Sigma to create this detection rule. Assuming a context where binaries with Landlock rules are fine-tuned, we look at the existence of the keys “domain” and “blockers” in the collected events, as it is [specific](https://docs.kernel.org/admin-guide/LSM/landlock.html#record-types) to Landlock.

## Landlock use cases

### Vulnerability in executable

A primary use case for Landlock is to bolster the security of sensitive services. Defenders can leverage it to monitor for and prevent potential exploitation attempts against exposed services.

For illustrative purposes, consider a straightforward example: an exploitable HTTP server that fails to properly sanitise user-supplied URI query parameters (code in appendix). Of course, this is a dumb, simple example to get to the point, as the vulnerable code is deliberately designed to be vulnerable and easy to fix.

Our “web server” has only read access to web pages from a specific location on the file system (“/var/lib/htdocs”), to prevent any other malicious access. This is enforced using a Landlock rule in this part of the code:

`const allowedDir = "/var/lib/htdocs"  
...  
landlock.V5.BestEffort().RestrictPaths(  
landlock.RODirs(allowedDir),  
)  
`

As soon as a user tries to request a path outside of this defined scope (_e.g._ “/etc/passwd”), even if it should be sanitised in a correctly coded web server, Landlock denies it:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5364b4041c6934346a0_6a92a16632517fc4025f0d66_6a2a800562f00361bfdd9a17.webp)

**_Figure 4. Shell commands trying to exploit the vulnerability_**

The successfully logged event (as explained in the first part) allows us to raise an alert in Sekoia SOC platform:

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5364b4041c69343469d_6a92a169a2f46752fd007f15_6a2a800562f00361bfdd9a1d.webp)

**_Figure 5. Landlock events in Sekoia SOC Platform_**

From our perspective, this host-level detection approach is more effective than relying on higher-level signals such as network monitoring. The sandboxed application operates with fewer required privileges making it harder for an attacker to evade. Landlock logging capabilities also allow defenders to observe when a successful attack path is being abused, rather than merely catching failed attempts from automated scanners.

### XZ Landlock integration

[XZ Utils](https://tukaani.org/xz/) is unfortunately a well-known case because of the CVE-2024-3094, when malicious code was discovered in some tarballs versions (5.6.0 and 5.6.1). Many articles describe the attack therefore this is not what we will focus on, but one part is of high interest: the attacker prevented the code containing Landlock from being compiled with [a single dot](https://github.com/tukaani-project/xz/commit/328c52da8a2bbb81307644efdb58db2c422d9ba7). No forensics evidence was able to prove he had a reason to perform that because it seems it was not needed for the full compilation chain in this [supply chain attack](https://gist.github.com/thesamesam/223949d5a074ebc3dce9ee78baad9e27).

Here is the [list of authorised rules](https://github.com/tukaani-project/xz/blob/8bb516887c1912106a72db96216cab46954e6190/src/xz/sandbox.c#L190) from Landlock, every other action will be denied:

  * LANDLOCK_ACCESS_FS_WRITE_FILE
  * LANDLOCK_ACCESS_FS_READ_FILE
  * LANDLOCK_ACCESS_FS_READ_DIR
  * LANDLOCK_ACCESS_FS_REMOVE_FILE
  * LANDLOCK_ACCESS_FS_MAKE_REG



The usage of XZ to deploy the backdoor was completely legitimate therefore, Landlock would not have blocked any part of the attack. So why remove Landlock at all? The question remains, and several hypotheses exist.

One possibility is that It could be a last-minute “panic” decision made prior launching its attack, like someone would disable an antivirus even if not necessary. Another hypothesis is that he found a vulnerability, or planned to introduce a new one, in XZ and could potentially execute code or contact its C2 through XZ, and that Landlock needed to be disabled.

In any case, this is a great demonstration of how Landlock is implemented in an open-source tool, and already targeted by attackers, just like security products would have. We still wanted to show an example of why Landlock is useful with XZ by using the well-known LD_PRELOAD hijacking technique to load a malicious library.

Our library simply recodes the write function which is used by XZ and launches the command “ls /tmp” as a child process of XZ. While this might not be the most realistic approach, it simulates a potential vulnerability or bug in a binary (XZ in this case) and still shows how Landlock can be useful in reducing attack surface in Linux binaries.

Once the library is compiled, LD_PRELOAD can be used to load it. We tried it with two different versions of XZ: 5.8.1 is the one installed by default in Debian Trixie and is compiled with Landlock.

The other one, located in ./src/xz/xz is an older version, 5.0.8, that is not compiled with Landlock. As shown below, the XZ binary compiled with**Landlock denies the execution** of “ls /tmp” thanks to Landlock whereas the older version allows the command to be executed.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5364b4041c693434694_6a92a16b9d3b9ef4d8bb7cf4_6a2a800562f00361bfdd9a27.webp)

**_Figure 6. Shell commands simulating a vulnerability in XZ to execute the “ls /tmp” command_**

As stated before, while it is amazing to have that malicious execution blocked, it is not enough as the attacker might find other ways. Thankfully, Landlock will log that denial, making defenders aware of a potential ongoing attack, and an alert will be triggered on the Sekoia SOC platform.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5364b4041c6934346a3_6a92a1653e6167cebbf55b71_6a2a800562f00361bfdd9a14.webp)

**_Figure 7. Landlock alert in Sekoia SOC platform_**

## Conclusion

Landlock has established itself as an interesting security mechanism and a valuable source of telemetry for detection, allowing SOCs to create precise sandboxes and behavioural rules with a low false positive rate. Its integration into common tools (like XZ Utils) and its targeting by attackers confirm its growing role.

It has been integrated in the Linux kernel since version 5.13, and the logging capabilities since 6.15. While this is relatively recent, several tools already use Landlock and more will in the future. 

For defenders, Landlock is an amazing tool for defence-in-depth logic. It first hardens the systems, but also allows to get new useful logs that can be used for alerting in SOCs. At Sekoia, we think defenders definitely need to have Landlock in their scope for hardening and future detection, the same way other security products are used today. Blocking an attack is great, knowing that the attack was blocked is even better.

We are continuously looking for new telemetry sources to expand our detection scope and create new detection rules to improve our coverage. Landlock allowed us to improve both and we will continue to follow its improvements as well as other LSMs in the future.

## Appendix

### Simple vulnerable Go web server

`package main  
import (  
"fmt"  
"io"  
"log"  
"net/http"  
"os"  
"path/filepath"  
"github.com/landlock-lsm/go-landlock/landlock"  
)  
  
const allowedDir = "/var/lib/htdocs"  
  
// vulnerableHandler reads the 'file' query parameter with no validation,  
// then opens and serves that file by joining it with allowedDir.  
func vulnerableHandler(w http.ResponseWriter, r *http.Request) {  
reqFile := r.URL.Query().Get("file")  
if reqFile == "" {  
http.Error(w, "'file' query parameter required", http.StatusBadRequest)  
return  
}  
  
path := filepath.Join(allowedDir, reqFile)  
fmt.Printf("Serving file: %s\n", path)  
file, err := os.Open(path)  
  
if err != nil {  
http.Error(w, "File not found or access denied", http.StatusNotFound)  
return  
}  
  
defer file.Close()  
  
if _, err := io.Copy(w, file); err != nil {  
http.Error(w, "Error reading file", http.StatusInternalServerError)  
}  
}  
  
func main() {  
err := landlock.V5.BestEffort().RestrictPaths(  
landlock.RODirs(allowedDir),  
)  
  
if err != nil {  
log.Fatalf("Failed to apply Landlock restrictions: %v", err)  
}  
  
http.HandleFunc("/", vulnerableHandler)  
fmt.Println("Vulnerable HTTP server with Landlock on :8080")  
log.Fatal(http.ListenAndServe(":8080", nil))  
}  
`

### Malicious library recoding “write” function

`#define _GNU_SOURCE  
#include <stdio.h>  
#include <dlfcn.h>  
#include <unistd.h>  
#include <errno.h>  
#include <string.h>  
#include <stdlib.h>  
#include <sys/wait.h>  
  
static ssize_t (*real_write)(int fd, const void *buf, size_t count) = NULL;  
  
ssize_t write(int fd, const void *buf, size_t count) {  
if (!real_write) real_write = dlsym(RTLD_NEXT, "write");  
  
static int attempted = 0;  
  
// Triggers if stdout (1) or file (>2)  
if (!attempted && (fd == 1 || fd > 2)) {  
attempted = 1;  
fprintf(stderr, "\nInjected - Trying to execute 'ls /tmp'...\n");  
pid_t pid = fork();  
  
if (pid == 0) {  
dup2(STDERR_FILENO, STDOUT_FILENO);  
execl("/usr/bin/ls", "ls", "/tmp", NULL);  
  
// If Landlock blocked, print error   
fprintf(stderr, "(%s)\n", strerror(errno));  
exit(1);  
} else if (pid > 0) {  
wait(NULL);  
}  
}  
return real_write(fd, buf, count);   
}  
`

### Sigma detection rule

`version: 2.0  
uuid: ef477b0d-71d8-4190-a6c7-c2187f7d6ddb  
rule: Landlock Denied Access  
description: >-  
Landlock LSM (Linux Security Module), has denied an access requests. This is logged by default for a sandboxed program if audit is enabled.  
sources: https://docs.kernel.org/admin-guide/LSM/landlock.html  
effort: intermediate  
detection:  
selection:  
action.properties.domain : '*'  
action.properties.blockers: '*'  
condition: selection  
tags:  
- Linux  
similarity_strategy:  
- action.properties.domain  
`