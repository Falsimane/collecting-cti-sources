# Log4Shell : The defender’s worst nightmare?

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/log4shell-the-defenders-worst-nightmare
- **Date :** 2021-12-13

---

> **Note:** Since this post concerns a recently-published vulnerability, intelligence regarding latest research will be updated periodically.

On Thursday, December 9, 2021, a code execution vulnerability (dubbed Log4Shell and referenced as CVE-2021-44228) affecting the Java Log4j logging library was published on the Internet by a company named Lunasec. Log4j is a widely used logging library in Java desktop and server applications.

Tons of cloud services, web applications and desktop applications have been successfully tested and exploited. Its ease of use exploitation – by injecting a simple string of characters – caused asurge of automatic scan looking for vulnerable assets. In the FLINT we present the following topics: 

  * Technical analysis
  * ITW exploitation attempts
  * Log4Shell affected assets
  * Log4Shell detection strategy
  * Beyond this RCE, what’s next?
  * So, what to do?



## Technical analysis

The Log4j library has a mechanism called message lookup substitution allowing to [enrich the logs](/blog/enrich-your-graylog-with-sekoia-io) produced by the library with several contextual dynamic values called « Lookups ». These lookups allow, for example, to write in the logs the environment variables of the system on which it is running (Java Version, operating system). Until the Log4j version 2.15.0, Log4j allowed JNDI lookups.

JNDI (Java Naming and Directory Interface) is a Java interface used to query several naming and directory services. As described by a previous research, LDAP and RMI JNDI interfaces have weaknesses which allow them to execute arbitrary code by passing to the URI of an object which refers to a Java class file which will be executed by the Java instance. Thenceforth, Log4j can be subject to a vulnerability as the version before 2.16.0 allowed JNDI by default, and lookups injections from an attacker controlled value.

To trigger that vulnerability, an attacker only has to inject a JNDI lookup querying a (fake) LDAP server controlled by him to any field which will potentially be logged by the application, for example, a username or an HTTP field like a User-Agent. Here is an HTTP GET request example trying to trigger the vulnerability by injecting the User-Agent header field. 

![Sample of exploitation attempt ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a68a51e6f2012c1953ad_6a92a4cdc9e0b85494c041ec_6a2a786813d55907a34ca32f.webp)

Sample of exploitation attempt 

If the vulnerable application is using Log4j and processes in the logs the User-Agent, a LDAP JNDI lookup will be done by Java. Java will issue the LDAP query to look at the “foo” object which refers to an external Java class. Then, by following this reference, Java will issue an HTTP request to download and execute the Java class, as shown in the network capture below:

![Sample of exploitation attempt of Log4Shell](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a68a51e6f2012c1953b1_6a92a4d03e6167cebbf72ca7_6a2a786813d55907a34ca33a.webp)

Sample of exploitation attempt of Log4Shell

The exploitation method shown above is not the only one which can be used against a vulnerable application. Several other ways can be used such as embedding directly the malicious serialized Java Object in the LDAP answer or using LDAPS to prevent network signatures on LDAP answers.

## ITW exploitation attempts

During the weekend several public exploits have been released on the Internet. Since then, most of the massive Internet scans looking to exploit Log4Shell are no longer related to researchers but associated with malicious crypto mining activities and historical botnets like Mirai, Muhstik or Kinsing. However, the success of these “blind scans” looking for vulnerable servers just by sending HTTP requests seem to be overestimated by the security community. 

The success rate of these scans can be evaluated by looking at the “bingsearchlib” campaign. This massive scanning campaign seems to have been started on the 9th of December, the day when the domain “bingsearchlib[.]com” was registered and the Lunasec blog post was published. 

At the beginning of the crisis, a bot using TOR IP addresses seems to have scanned the entire Internet looking for vulnerable servers by sending this specific string as an HTTP User-Agent: 

![sending this specific string as an HTTP User-Agent](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a68a51e6f2012c1953a7_6a92a4cca2f46752fd0287ce_6a2a786813d55907a34ca32c.webp)

Sending this specific string as an HTTP User-Agent

The hexadecimal string in the sub domain seems to be unique per scanned host and seems to represent the IP address of the targeted server. Thenceforth, if the exploitation succeeds, a DNS request will be made to the domain name. This query will end up with a chance in Passive DNS cache such as PassiveTotal. 

By looking at such caches, there are only a few dozen subdomains have been seen, 140 on PassiveTotal. Kryptos Logic indicated in a tweet 10k vulnerable web servers after a scan done during the weekend on various HTTP fields – less than for the CVE-2021-41773. Among these 10,000 vulnerable servers, a certain number may be linked to Honeypots exposed by security researchers. Indeed, several projects have been shared on GitHub allowing to deploy services vulnerable to the Log4Shell vulnerability. By the way, few researchers complained about the noise created by scanners. **Since then, the real success rate of these actual blind exploitation campaigns done by botnets seems very limited at the scale of the Internet.**

However, many targeted attacks using Log4Shell seem to have started. Microsoft said in a blog-post that they already have observed Log4j post-exploitation activities including Cobalt Strike.

## Log4Shell affected assets

Beyond these blind scans, the scope of this vulnerability is difficult to estimate as it can target literally any application integrating a vulnerable implementation of the Log4j library. Consequently, the vulnerability does not impact only on web servers, contrary to what may be expected, but also desktop applications or embedded systems, which are often more complex or even impossible to update. 

With this, the exploitation vectors are multiple. Here is few examples, where an attacker can use malicious JNDI injections triggered by Log4j:

  * Web applications and APIs endpoints using Log4j by sending requests embedding a malicious JNDI injection;
  * Server, middleware and appliance using Log4j by sending specific request embedding a malicious JNDI injection (e.g. JAMES SMTP server);
  * Desktop applications using Log4j by forging – for example – a malicious file embedding a malicious JNDI injection to be opened by the application (e.g. the Ghidra vulnerability);
  * 2-tier / 3-tier client application written in Java and using Log4j by poisoning a database with malicious JNDI injection in order to infect the client systems retrieving data from the database;
  * Any processing application (eg. OCR) using Log4j by forging an input to be processed containing a malicious JNDI injection.



However, the [risk can be reduced](/blog/reduce-cyber-risks-through-automation) if the logged input has been checked against a valid pattern before the processing by the application and Log4j. 

As of today, many editors are looking at the potential attack surface and vulnerability of their products.**Thenceforth, it is highly likely that many open source and proprietary applications will receive major security updates in the coming days.**

## Log4Shell detection strategy

Due to the number of vectors through which the vulnerability can be triggered and the number of obfuscation ways of the malicious JNDI injections, the detection of an exploitation attempt by standard network and system signatures is mostly limited to the non-obfuscated JNDI injections. Here is an non exhaustive list of possible obfuscations for the JNDI lookup:

![possible obfuscations for the JNDI lookup](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a68a51e6f2012c1953aa_6a92a4cec9e0b85494c0422b_6a2a786813d55907a34ca332.webp)

Possible obfuscations for the JNDI lookup

The detection can be based on:

  * The process tree of Java executing specific utilities via heuristic signatures based on system logs like Sigma;
  * The detection of successful exploitation via network signatures on the LDAP, RMI and HTTP responses containing Java class when an exploitation is successful. Suricata signatures are shared by Sekoia at the end of this blogpost;
  * Known IOCs of callback domains which will be triggered if an exploitation is successful. 



In brief, exploitation attempts of the Log4j vulnerability are difficult to detect; it is important to patch vulnerable systems and focus the detection on the Kill Chain phases following the initial compromise.

## Beyond this RCE, what’s next ?

This Log4Shell vulnerability, we could expect in the coming days and weeks, **multiple new specific vulnerabilities** within the **affected products and possible worms exploiting this vulnerability**. [Security](/blog/cybersecurity-skills-shortage-4-advices-to-better-deal-with-it) researchers and threat actors (APT, ransomware groups and other [cybercriminal](/blog/ongoing-roaming-mantis-smishing-campaign-targeting-france) groups) will hunt for these, leading to some **potential exploitation in the wild**. Sekoia has identified at least one ransomware group (LockBit) working on the Log4j vulnerability, according to our Darkweb insights:

![legasov \(about the LockBit representative being offline for a while\): “he went offline and never showed up again“
chinarules: “they told me they are working on log4j”](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a68a51e6f2012c1953a4_6a92a4cfa49553afbaf3f865_6a2a786813d55907a34ca336.webp)

legasov (about the LockBit representative being offline for a while): “he went offline and never showed up again“  
chinarules: “they told me they are working on log4j”  


## So, what to do ?

First, **keep calm**. Despite the lot of noise on that vulnerability, the massive scans right now are just blind scans, which don’t target any specific application so their success rate is quite limited. However, this vulnerability is serious and will generate new vulnerabilities in several well known software used in the public and private sectors. Since then:

  * Keep an eye on the advisories and updates published by software vendors. We can expect – with medium confidence – that a rain of critical vulnerabilities related to specific products will come in the following days;
  * As your top priority, focus on your external attack surface for patching (business software, mail and web servers, any server and application connected to your network and reachable from the Internet);
  * Deploy system and network based detection signatures. Not on exploitation attempts as it will burn your SOC analysts, but on successful exploitation (e.g. HTTP answers containing a malicious JavaClass, LDAP answer referring to Java objects etc.);
  * If you have developed business Java applications using log4j, ask your dev teams to patch them.



### Course of action

  1. ‍**Update software** : Many software editors using Log4j library have available updates.**‍**
  2. **Alternative mitigation** : When you can not upgrade to the latest version of Log4j: either modifying the existing Log4j usage, or the Java virtual machine configuration.**‍**
  3. **Firewall rules** : Review the allowed outgoing server connections to the Internet. Prevent your server to initiate connection to untrusted assets on the Internet by using a [firewall](/glossary/firewall).



## **IoCs & technical details**

### IoCs associated to Log4j exploitation

  * On Sekoia: 
    * [IoCs](/glossary/ioc) are associated to the [campaign](https://app.sekoia.io/intelligence/objects/campaign--654f433f-1d97-4aca-96f7-d880994a2bac) “Massive exploitation campaign targeting the CVE-2021-44228”. They were obtained from different sources such as GreyNoise, Twitter, URLhaus or ThreatFox. They will be updated regularly.
    * Hundreds of observables related to scanning have also been added to the Sekoia observables database with the tag “CVE-2021-44228”. They will be updated regularly.
  * Shared on URLhaus: <https://urlhaus.abuse.ch/browse/tag/log4j/>
  * Shared on ThreatFox: <https://threatfox.abuse.ch/browse/tag/log4j/>



### Yara Rules

Sekoia [YARA rules](/blog/playbooks-yara-rules-iocs-explanation-about-the-news) detecting string used for JNDI lookup injection used for Log4Shell exploitation:

`rule Log4Shell_JNDI_Lookup_LDAP_Injection {  
meta:  
id = "cf8d4455-189d-4350-b448-99fdba158053"  
description = "Detects JNDI lookup LDAP injection attempt"  
version = "1.0"  
creation_date = "2021-12-13"  
modification_date = "2021-12-13"  
classification = "TLP:WHITE"  
source="SEKOIA"  
version="1.0"  
strings:  
$ = { 24 7b [0-15] (6a|4a)  
[0-15] (6e|4e) [0-15]  
(64|44) [0-15] (69|49)  
[0-15] 3a [0-15] (6c|4c)  
[0-15] (64|44) [0-15]  
(61|41) [0-15] (70|50)  
[10-120] 7d }  
condition:  
$  
}  
  
rule Log4Shell_JNDI_Lookup_RMI_Injection {  
meta:  
id = "cf8d4455-189d-4350-b448-99fdba158053"  
description = "Detects JNDI lookup RMI injection attempt"  
version = "1.0"  
creation_date = "2021-12-13"  
modification_date = "2021-12-13"  
classification = "TLP:WHITE"  
source="SEKOIA"  
version="1.0"  
strings:  
$ = { 24 7b [0-15] (6a|4a)  
[0-15] (6e|4e) [0-15]  
(64|44) [0-15] (69|49)  
[0-15] 3a [0-15] [0-15]  
(72|52) [0-15] (6d|4d)  
[0-15] (69|49) [10-120] 7d }  
condition:  
$  
}  
`

### Snort Rules

Emerging Threats shared open-source Suricata rules to detect and hunt Log4j RCE exploitation attempt:  
<https://rules.emergingthreatspro.com/open/>

**LDAP answer with javaNamingReference to an HTTP URL**

`alert tcp $EXTERNAL_NET any -> $HOME_NET any (flow: from_server, established;content:”0″;startswith;content:”objectClass”;content:”javaNamingReference”;  
content:”javaClassName”;content:”javaCodeBase”;pcre:/http(s)?:\/\//;depth:300;  
msg:”Detect LDAP answer with javaNamingReference to an HTTP URL #log4shell”;sid:XXXXXXXXX; rev:001;  
reference:url,www.sekoia.io/en/log4shell-the-defenders-worst-nightmare;)  
`

**TCP Packet with JavaClass Magic and containing compiled getRuntime-exec.**

`alert tcp $EXTERNAL_NET any -> $HOME_NET any (flow: from_server, established;content:”|ca fe ba be 00 00 00|”;content:”java/lang/Runtime”;content:”|04 65 78 65 63 01|”;depth:2000; msg:”Detect JAVA class using getRuntime().exec over unencrypted protocol #log4shell”; sid:XXXXXXXXX; rev:001;reference:url,www.sekoia.io/en/log4shell-the-defenders-worst-nightmare;)`

**TCP Packet with JavaClass Magic and containing compiled ProcessBuilder-command.**

`alert tcp $EXTERNAL_NET any -> $HOME_NET any (flow: from_server, established;content:”|ca fe ba be 00 00 00|”;content:”java/lang/ProcessBuilder”;content:”|07 63 6f 6d 6d 61 6e 64 01|”;depth:2000;msg:”Detect JAVA class using builder.command over unencrypted protocol #log4shell”;sid:XXXXXXXXX; rev:001;reference:url,www.sekoia.io/en/log4shell-the-defenders-worst-nightmare;)`

## External references

  1. ‍[[CVE MITRE] CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228)
  2. ‍[[](https://www.govcert.ch/blog/zero-day-exploit-targeting-popular-java-library-log4j/)[GovCERT.ch]](https://www.govcert.ch/)[ Zero-Day Exploit Targeting Popular Java Library Log4j](https://www.govcert.ch/blog/zero-day-exploit-targeting-popular-java-library-log4j/)
  3. ‍[[CERT-FR]](https://www.govcert.ch/blog/zero-day-exploit-targeting-popular-java-library-log4j/)[ Bulletin d’alerte du CERT-FR](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2021-ALE-022/)
  4. ‍[[MOGWAI LABS] Vulnerability notes: Log4Shell](https://mogwailabs.de/en/blog/2021/12/vulnerability-notes-log4shell/)
  5. ‍[[Blackhat] A journey from JNDI/LDAP manipulation to remote code execution dream land](https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE.pdf)
  6. ‍[[Microsoft] Guidance for preventing, detecting, and hunting for CVE-2021-44228 Log4j 2 exploitation](https://www.microsoft.com/en-us/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/)
  7. ‍[[SwitHak’s GitHub] BlueTeam CheatSheet: Bulletins linked to Log4Shell](https://gist.github.com/SwitHak/b66db3a06c2955a9cb71a8718970c592)
  8. [nice0e3’s GitHub] log4j_POC