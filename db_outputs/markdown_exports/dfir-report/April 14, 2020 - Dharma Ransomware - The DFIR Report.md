# Dharma Ransomware - The DFIR Report

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2020/04/14/dharma-ransomware/
- **Date :** April 14, 2020

---

![](https://thedfirreport.com/wp-content/uploads/image-19.png)

[ransomware](https://thedfirreport.com/category/ransomware/)

# Dharma Ransomware

April 14, 2020 

An attacker logged into the honeypot via RDP from 178.239.173[.]172. Within 10 minutes the attacker went from local admin, to domain admin to installing ransomware on multiple machines. The attacker used Defender Control to turn off Defender and then used Mimikatz to dump credentials. From there the attacker used Network Scanner to scan the local subnet. The attacker then used RDP to log into each machine to manually run the ransomware payload.

![](https://i1.wp.com/thedfirreport.com/wp-content/uploads/2020/04/image-21.png?fit=1024%2C251&ssl=1)

Here is a screenshot of Network Scanner which was renamed by the actors to NSold.exe

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-13.png)

Logs showing the extraction and use of DefenderControl to disable Windows Defender during the attack:

![](https://thedfirreport.com/wp-content/uploads/2020/04/ss2-1.png)

Here is a screenshot of the ransom which pops up at login.

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-19.png)

This FILES ENCRYPTED file can be found in the root of C as well as on the desktop. This file appears to be written to every folder where encryption occured.

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-15.png)

We’ve seen the below command a few times in ransomware intrusions and it might be worth writing a rule to detect findstr.exe + /c:system$ and/or /c:sistem$ in the command line arguments.

![](https://i0.wp.com/thedfirreport.com/wp-content/uploads/2020/04/image-23.png?fit=1024%2C252&ssl=1)

We submitted information to [ID Ransomware](https://id-ransomware.malwarehunterteam.com/) which provided the below information.

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-17.png)

We’ve seen the same pdb path below used for Dharma in the past so this pdb path stays consistent and would be a good detection.

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-18.png)

More information about Dharma/Crysis can be found [here](https://id-ransomware.blogspot.com/2016/11/dharma-ransomware.html).

## Summary

This attacker was able to deploy ransomware to 5+ machines in under 10 minutes which was quite impressive. The attacker used Defender Control which we’ve seen in the past to disable Defender and Mimikatz to dump credentials. There are multiple detection rules that can be written from this intrusion which should help improve detection times moving forward. With that said when the attackers move this fast you must respond to incidents in a timely matter to catch the attacker before they accomplish their mission.

Enjoy our report? Please consider donating $1 or more to the project using [Patreon](https://www.patreon.com/thedfirreport). Thank you for your support!

## IOCs

The ransomware payload can be found at [Any.Run](https://app.any.run/tasks/364c4340-e547-4b52-aa9e-8ba927551019)

RDP login from 178.239.173[.]172

The ransomware payload created a few run keys

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-25.png)

##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2020/04/14/dharma-ransomware/&t=Dharma%20Ransomware)
  * [Share on X](https://x.com/share?text=Dharma%20Ransomware&url=https://thedfirreport.com/?p=111)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2020/04/14/dharma-ransomware/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=Dharma%20Ransomware&url=https://thedfirreport.com/2020/04/14/dharma-ransomware/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2020/04/14/dharma-ransomware/&title=Dharma%20Ransomware)
  * [Share by Mail](/cdn-cgi/l/email-protection#3e014d4b5c545b5d4a037a565f4c535f1b0c0e6c5f504d5153495f4c5b181d0e0d06055c515a4703564a4a4e4d0411114a565b5a58574c4c5b4e514c4a105d5153110c0e0c0e110e0a110f0a115a565f4c535f134c5f504d5153495f4c5b11)