# Akkadian Provisioning Manager Multiple Vulnerabilities Disclosure | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/06/08/akkadian-provisioning-manager-multiple-vulnerabilities-disclosure/
- **Date :** 2025-06-02

---

Over the course of routine security research, Rapid7 researchers discovered that the Akkadian Provisioning Manager version 4.50.18, a provisioning solution for a Cisco Unified Communications environment, has a trio of vulnerabilities, which, when combined, can lead to remote code execution on the affected device with elevated privileges. Those issues are summarized in the table below.

CVE Identifier| CWE Identifier| CVSS score (Severity)| Remediation  
---|---|---|---  
CVE-2021-31579| [CWE-798](https://cwe.mitre.org/data/definitions/798.html): Use of Hard-Coded Credentials| [8.2](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:N&version=3.1) (High)| Updated in [5.1.0](https://doc.clickup.com/d/h/24t9j-27923/b7180168c8cf855/24t9j-1673)  
CVE-2021-31580| [CWE-78](https://cwe.mitre.org/data/definitions/78.html): Improper Neutralization of Special Elements used in an OS Command (exec)| [7.9](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:N&version=3.1) (High)| Updated in [5.1.0](https://doc.clickup.com/d/h/24t9j-27923/b7180168c8cf855/24t9j-1673)  
CVE-2021-31581| [CWE-269](https://cwe.mitre.org/data/definitions/269.html): Improper Neutralization of Special Elements used in an OS Command (vi)| [7.9](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:N&version=3.1) (High)| Updated in [5.1.0](https://doc.clickup.com/d/h/24t9j-27923/b7180168c8cf855/24t9j-1673)  
  
In addition to these issues, two other questionable findings were discovered: the ability to read the cleartext local MariaDB credentials, and the inadvertent shipping of an entire GitHub repo with commit history. At the time of this writing, it's unclear if these findings present unique security issues, but nonetheless, should be reviewed by the vendor.

Product Description

Akkadian Provisioning Manager (PME) is a management platform for Cisco Unified Communications (UC) devices and applications, which are largely VoIP and video solutions for communications. PME is usually seen in larger enterprises where provisioning and reconfiguring these solutions is a fairly common occurrence. More can be learned about Akkadian PME from the [vendor's website](https://www.akkadianlabs.com/products/akkadian-provisioning-manager/).

Credit

These issues were discovered by Cale Black, Ryan Villarreal ([@XjCrazy09](https://twitter.com/XjCrazy09)), and Jonathan Peterson ([@deadjakk](https://twitter.com/deadjakk)) of Rapid7, and it is being disclosed in accordance with [Rapid7's vulnerability disclosure policy](/security/disclosure/).

Exploitation

The following were observed and tested on version 4.50.18 GA 2020-04-07 - Build 1.1.36 (Linux) of the Akkadian Provisioning Manager (PME).

### CVE-2021-31579: Use of Hard-Coded Credentials

During a penetration test on a client site, Rapid7 researchers were able to gain access to a PME OVA virtualized appliance and was able to interrupt the boot process and force the init system to be an interactive shell, as can be seen below:

![Screen-Shot-2021-06-07-at-12.38.27-PM.png](https://www.rapid7.com/cdn/images/blt8bfd8bd15a89a3dc/683ddd337f8603d8d02306a2/Screen-Shot-2021-06-07-at-12.38.27-PM.png)

This successfully presented Rapid7 researchers with a root shell environment:

![Screen-Shot-2021-06-07-at-12.39.28-PM.png](https://www.rapid7.com/cdn/images/blt3d8c58b4c83e0463/683ddd583323a58d0f80a7e5/Screen-Shot-2021-06-07-at-12.39.28-PM.png)

Once shell access was achieved testers identified the enabled **`akkadianuser`** in the user /etc/passwd database:

![Screen-Shot-2021-06-07-at-12.40.41-PM.png](https://www.rapid7.com/cdn/images/blta9250d0dd209f442/683ddd7f2a9b68bc4c2bd16b/Screen-Shot-2021-06-07-at-12.40.41-PM.png)

Investigating the user home directory revealed a set of developer files on the production server:

![Screen-Shot-2021-06-07-at-12.41.55-PM.png](https://www.rapid7.com/cdn/images/blt527cdc1ccfadabb8/683ddda3590d7f0159de1a9d/Screen-Shot-2021-06-07-at-12.41.55-PM.png)

Rapid7 researchers identified developer configuration scripts for configuring a high availability user, **/home/akkadianuser/scripts/create_haakkadianuser.sh and /home/akkadianuser/tmp/akkappmanager_installation/scripts/create_haakkadianuser.sh**. These scripts revealed that the high availability user was created with the default password **`haakkadianpassword`** as can be seen below:

![Screen-Shot-2021-06-07-at-12.44.08-PM.png](https://www.rapid7.com/cdn/images/blt6143aa1d9314f323/683dddcb73c8455164e8c28c/Screen-Shot-2021-06-07-at-12.44.08-PM.png)

Using the knowledge of the created high availability user password, Rapid7 researchers were able to successfully guess the credential of the existing **`hakkadianuser`** user, which was **`hakkadianpassword`**. Rapid7 was able to verify this credential would give access to the Akkadian PME restricted shell:

![Screen-Shot-2021-06-07-at-12.44.59-PM.png](https://www.rapid7.com/cdn/images/blt33bf1ff5adccdfc1/683dddf5abf2ad46423c42bf/Screen-Shot-2021-06-07-at-12.44.59-PM.png)

Rapid7 was then able to successfully bypass the restricted shell menu environment via the techniques described below, CVE-2021-31580 and CVE-2021-31580, and identified that the running **`akkadianuser`** user was given unrestricted sudo privileges without a password:

![Screen-Shot-2021-06-07-at-12.45.47-PM.png](https://www.rapid7.com/cdn/images/bltc622b8b2889c3ca7/683dde1a3d7b5e8d2f136580/Screen-Shot-2021-06-07-at-12.45.47-PM.png)

This was confirmed by using the shell escapes with the sudo command, allowing Rapid7 researchers full access to the root user:

![Screen-Shot-2021-06-07-at-12.46.57-PM.png](https://www.rapid7.com/cdn/images/blt8b08f4abf33bd3d9/683dde492a9b68add42bd1a1/Screen-Shot-2021-06-07-at-12.46.57-PM.png)

### CVE-2021-31580: Shell Escape via 'exec' command

Rapid7 researchers identified that the restricted shell in use by the Akkadian Appliance Manager component of the PME was not directly set to the restricted shell binary, and instead was set to bash, and could be bypassed by the procedure outlined below. First, the default bash shell was observed:

![Screen-Shot-2021-06-07-at-12.47.59-PM.png](https://www.rapid7.com/cdn/images/bltc6082721302dde1d/683dde7b2cfe32b43adc15aa/Screen-Shot-2021-06-07-at-12.47.59-PM.png)

The restricted shell environment is triggered via the **/home/akkadianuser/.bashrc** configuration file which invokes the **`akkadianAppManager`** shell via sudo: 

![Screen-Shot-2021-06-07-at-12.49.01-PM.png](https://www.rapid7.com/cdn/images/blt5c6666bac02f20ad/683ddeb5cc6042108d206700/Screen-Shot-2021-06-07-at-12.49.01-PM.png)

Knowing that the shell was bash and that the python restricted shell environment was interactive, Rapid7 researchers switched the OpenSSH channel from **`shell`** to **`exec`** by providing the ssh client a single execution parameter. This triggered the interactive Python script to unsuccessfully find the **`/dev/tty`** file and exit, but as the shell is running in the context of a bash shell, the failed exit condition does not fail the parent shell and the command is passed on through to the operating system allowing a bypass, as shown below.

![Screen-Shot-2021-06-07-at-12.50.19-PM.png](https://www.rapid7.com/cdn/images/bltdc395966811c70df/683ddedd5619a13a8dc6ea12/Screen-Shot-2021-06-07-at-12.50.19-PM.png)

Combining this issue with the default hard-coded root user, **hakkadianuser:hakkadianpassword** , will allow an otherwise unauthenticated, network-based attacker with unrestricted access to an interactive shell with root privileges.

### CVE-2021-31581: Shell Escape via 'vi' editor interface

Rapid7 researchers identified that the restricted shell environment of the Akkadian Appliance Manager component of the PME could be bypassed using the shipped version of **`vi`** , a popular terminal-based text editor. When authenticated, normally, the following prompt is shown:

![Screen-Shot-2021-06-07-at-12.51.20-PM.png](https://www.rapid7.com/cdn/images/blt872043c7b43c438e/683ddf05bc38b14dfd477c71/Screen-Shot-2021-06-07-at-12.51.20-PM.png)

Select 4: Product Settings Menu and the next set of options gets prompted:

![Screen-Shot-2021-06-07-at-12.51.52-PM.png](https://www.rapid7.com/cdn/images/blta517066fd3cd7261/683ddf2cabf2ad90cb3c432b/Screen-Shot-2021-06-07-at-12.51.52-PM.png)

Select 1: Akkadian PM/HCS Services and the next set of options appears:

![Screen-Shot-2021-06-07-at-12.52.20-PM.png](https://www.rapid7.com/cdn/images/blt6aadbaec2bf20791/683ddf55237ea6aadc91c211/Screen-Shot-2021-06-07-at-12.52.20-PM.png)

Select 2: MySQL Service option and follow to the next screen:

![Screen-Shot-2021-06-07-at-12.52.49-PM.png](https://www.rapid7.com/cdn/images/bltcc88c9695f8882dc/683ddf7bff6aa9be610ea802/Screen-Shot-2021-06-07-at-12.52.49-PM.png)

Select 4: Edit MySQL Configuration (my.cnf), which finally drops the user into a vi editor interface for **`/etc/my.cnf`** :

![Screen-Shot-2021-06-07-at-12.53.32-PM.png](https://www.rapid7.com/cdn/images/blt50a3a6baa1ecb554/683ddfa0da5c3020f4a83452/Screen-Shot-2021-06-07-at-12.53.32-PM.png)

This can be bypassed by using the execution functionality in the shipped version of **`vi`** on the PME by hitting **`:!`** and then the desired command. The following screenshot shows that the restricted shell is running as the root user (due to the sudo invocation of the shell as mentioned in CVE-2021-31580):

![Screen-Shot-2021-06-07-at-12.54.33-PM.png](https://www.rapid7.com/cdn/images/blt543965a6e220d620/683ddfc88ac17c67a629ad90/Screen-Shot-2021-06-07-at-12.54.33-PM.png)

Combining this issue with the default hard-coded root user, **hakkadianuser:hakkadianpassword** , will allow an otherwise unauthenticated, network-based attacker with unrestricted access to an interactive shell with root privileges.

### CVE-2021-31581: Exposure of Sensitive Information

Rapid7 researchers also identified that the application was serving sensitive data via the exposed web server. Listing the **`/var/www/html/pme/`** directory Rapid7 identified the ionCube packed PHP files, but an additional set of files that were marked with readable permissions:

![Screen-Shot-2021-06-07-at-12.55.36-PM.png](https://www.rapid7.com/cdn/images/blt4dfd127b0d16cc85/683ddff15619a12c67c6ea53/Screen-Shot-2021-06-07-at-12.55.36-PM.png)

Many of these files contained sensitive data that was accessible via the web server. Of note the **`/pme/database/pme/phinx.yml`** file contained cleartext local MariaDB usernames and passwords:

![Screen-Shot-2021-06-07-at-12.56.21-PM.png](https://www.rapid7.com/cdn/images/bltbb5572ce9e8634b6/683de01f65b8eaf5afcc8c7d/Screen-Shot-2021-06-07-at-12.56.21-PM.png)

Rapid7 researchers were able to use local shell access in order to successfully validate that these credentials were valid and worked to connect to the underlying MariaDB host listening locally. The scope of the original client's penetration test additionally included an LDAP integrated environment, and this issue was leveraged to successfully recover cleartext LDAP BIND credentials from the database:

![Screen-Shot-2021-06-07-at-12.57.13-PM.png](https://www.rapid7.com/cdn/images/blt4498cac1a406fd9d/683de0432a9b68dbdd2bd22d/Screen-Shot-2021-06-07-at-12.57.13-PM.png)

## Additional Finding: Shipping Git Repository (No CVE ID)

The web server additionally exposed a git repository **`.git/`** directory. This was verified by visiting **`/pme/.git/config`** which exposed information about the ionCube packed Akkadian PME repository:

![Screen-Shot-2021-06-07-at-12.58.13-PM.png](https://www.rapid7.com/cdn/images/blta1f2bba515bbc889/683de06c543b8d63b7bf117b/Screen-Shot-2021-06-07-at-12.58.13-PM.png)

Due to the predictable structure of git repositories, Rapid7 was able to extract the repos directly from the exposed network facing web server:

![Screen-Shot-2021-06-07-at-12.58.51-PM.png](https://www.rapid7.com/cdn/images/bltb8ab3c3943c4f840/683de08fabf2ad5a4e3c43ad/Screen-Shot-2021-06-07-at-12.58.51-PM.png)

Rapid7 then extracted each of the commits and was able to view additional files and the ionCube encoded backend PHP files, both historical and current:

![Screen-Shot-2021-06-07-at-1.00.12-PM.png](https://www.rapid7.com/cdn/images/bltfecdfb55dbdeb307/683de0b6590d7f3cddde1bb6/Screen-Shot-2021-06-07-at-1.00.12-PM.png)

While this git structure does seem to include sensitive information, Rapid7 researchers did not validate if that information was useful to an attacker. In any event, it should be removed from production installations of Akkadian devices.

## Impact

As mentioned previously, combining CVE-2021-31579 and either CVE-2021-31580 or CVE-2021-31581 will allow an otherwise unauthorized attacker complete, root-level shell access to the affected devices; this can open a door to installing cryptominers, keystroke loggers, persistent shells, and any other type of Linux-based malware.

While further access to the Cisco Unified Communications environment appears technically possible, it appears unlikely that real time or recorded calls or conferences could be gathered directly from these compromised devices.

## Remediation

For the first issue, network access to the SSH port (22/tcp) should be limited only to trusted users, and certainly not exposed to the internet. Furthermore, system operators should know that, in the absence of a fix, users who have access to the Akkadian Appliance Manager effectively have root shell access to the device, due to the second and third issues described above.

Rapid7 researchers have attempted to communicate with Akkadian Labs, but were unable to elicit a response to this vulnerability disclosure. Customers should seek out their sales representatives to inquire about a fix timeline, after ensuring only authorized users have access to affected devices' SSH ports.

## Disclosure Timeline

**January, 2021** : Issues discovered by Rapid7 researchers Cale “poptart” Black, Ryan Villarreal, and Jonathan “deadjakk” Peterson

**Wed, Feb 3, 2021** : Initial disclosure attempt to the vendor, ticket 51058 created.

**Mon, Feb 22, 2021** : Followup to the vendor via support ticket

**Wed, Mar 10, 2021** : Second followup to the vendor via support ticket

**Tue, Jun 8, 2021** : Public Disclosure

**Wed, Jun 11, 2021:** Vendor provided information about fixes

** _Update:_**__ On June 11, 2021, the vendor reached out to Rapid7 and provided information regarding fixed versions of the components tested. On June 16th, it was determined that the issues described here are resolved in the following components and versions: Akkadian OVA appliance version 3.0 (and later), Akkadian Provisioning Manager 5.0.2 (and later), and Akkadian Appliance Manager 3.3.0.314-4a349e0 (and later).

## Article tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Vulnerability Management](/blog/tag/vulnerability-management/)
  * [Research](/blog/tag/research/)