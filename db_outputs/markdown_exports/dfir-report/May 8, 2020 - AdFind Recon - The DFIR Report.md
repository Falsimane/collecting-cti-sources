# AdFind Recon - The DFIR Report

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2020/05/08/adfind-recon/
- **Date :** May 8, 2020

---

![](https://thedfirreport.com/wp-content/uploads/image-1.png)

[rdp](https://thedfirreport.com/category/rdp/)

# AdFind Recon

May 8, 2020 

A threat actor logged into the RDP honeypot from 217[.]182[.]242[.]13 (OVH) with a hostname of WORK9F3B. Within 20 seconds they opened a command prompt and issued the following commands

![](https://thedfirreport.com/wp-content/uploads/2020/05/image.png)

They then logged off and 15 minutes later logged back in from a hostname of MacBook-Pro (the resolution was a lot better compared to whatever they were using before :) ). From there they ran whoami /upn and then dropped AdFind.

AdFind is described as the following:

> Command line Active Directory query tool. Mixture of ldapsearch, search.vbs, ldp, dsquery, and dsget tools with a ton of other cool features thrown in for good measure. This tool proceeded dsquery/dsget/etc by years though I did adopt some of the useful stuff from those tools.
> 
> <http://www.joeware.net/freetools/tools/adfind/>

The threat actor then ran a batch file which ran AdFind commands and output them to txt files.

![](https://thedfirreport.com/wp-content/uploads/2020/05/image-1.png)

  * objectcategory=person – Finds all person objects
  * objectcategory=computer – Finds all computers in domain
  * trustdmp – Dumps trust objects.
  * objectcategory=subnet – Finds all subnets
  * domainlist – Dumps all Domain NCs in forest in sorted DNS list format
  * dcmodes – Shows modes of all DCs in forest from config
  * adinfo – Shows Active Directory Info with whoami info.
  * dclist – Dumps Domain Controllers FQDNs.
  * computers_pwdnotreqd – Dumps users set with password not required.



AdFind usage can be found [here](https://www.joeware.net/freetools/tools/adfind/usage.htm).

The threat actors then added a local admin user named Adm.1c with a password of adm99!@. The actors were not seen again.

We’ve seen AdFind used numerous times for recon in the past and continue to see it today. Here are a few more examples of AdFind being used for recon:

  * FireEye recently published an article on Maze ransomware TTPs which included the use of AdFind and a script to run and output files. Read more [here](https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html).
  * Cybereason put out an article last year on a Trickbot infection which used AdFind. Read more [here](https://www.cybereason.com/blog/dropping-anchor-from-a-trickbot-infection-to-the-discovery-of-the-anchor-malware).
  * FireEye put out an article in April of 2019 which talked about a FIN6 intrusion which used AdFind. Read more [here](https://www.fireeye.com/blog/threat-research/2019/04/pick-six-intercepting-a-fin6-intrusion.html).
  * Visa put out a Situational Intelligence Report on FIN6 activities in 2019 which included the use of AdFind. Read more [here](https://usa.visa.com/dam/VCOM/global/support-legal/documents/fin6-cybercrime-group-expands-threat-To-ecommerce-merchants.pdf).



If you know of other instances where AdFind has been used for recon leading up to ransomware or other malicious activities please contact us so we can add it to the list. 

Enjoy our report? Please consider donating $1 or more to the project using [Patreon](https://www.patreon.com/thedfirreport). Thank you for your support!

##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2020/05/08/adfind-recon/&t=AdFind%20Recon)
  * [Share on X](https://x.com/share?text=AdFind%20Recon&url=https://thedfirreport.com/?p=357)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2020/05/08/adfind-recon/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=AdFind%20Recon&url=https://thedfirreport.com/2020/05/08/adfind-recon/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2020/05/08/adfind-recon/&title=AdFind%20Recon)
  * [Share by Mail](/cdn-cgi/l/email-protection#dce3afa9beb6b9bfa8e19db89ab5b2b8f9eeec8eb9bfb3b2faffecefe4e7beb3b8a5e1b4a8a8acafe6f3f3a8b4b9b8bab5aeaeb9acb3aea8f2bfb3b1f3eeeceeecf3ece9f3ece4f3bdb8bab5b2b8f1aeb9bfb3b2f3)