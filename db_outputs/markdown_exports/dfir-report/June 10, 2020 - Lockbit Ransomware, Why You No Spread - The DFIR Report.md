# Lockbit Ransomware, Why You No Spread? - The DFIR Report

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2020/06/10/lockbit-ransomware-why-you-no-spread/
- **Date :** June 10, 2020

---

![](https://thedfirreport.com/wp-content/uploads/bit3.png)

[ransomware](https://thedfirreport.com/category/ransomware/)

# Lockbit Ransomware, Why You No Spread?

June 10, 2020 

RDP brute forcing continues to be a favorite entry point for ransomware actors. In this past month we saw activity from the Lockbit ransomware family.

### Initial Access:

RDP login from 165.231.142.36. Threat actor logged in, then switched accounts to a DA 15 minutes later.

### Action on Objectives:

Unlike other actors we’ve seen in the lab or in other reports take meticulous inventory and thoroughly enumerate a victim environment this actor moved straight into final phase activity.

They used a tool to disable the security defenses of the host they had access to with a program masquerading in the user Appdata location.
    
    
    %APPDATA%\svchost.exe

Which issued the following commands.
    
    
    netsh firewall set opmode disable
    net stop security center
    net stop WinDefend

The malware then kept a communication stream open to an Ukrainian FTP server even after ransomware deployment.

![](https://thedfirreport.com/wp-content/uploads/2020/06/bit5-1024x91.png)

svchost is seen sending key logs to the following FTP server using [Hakops15](https://www.turkhackteam.org/trojan-ve-virusler/1699779-hakops-keylogger-16-12-04-2018-a.html) which occurred once per day after infection.

![](https://thedfirreport.com/wp-content/uploads/2020/06/bit6.png)

![](https://thedfirreport.com/wp-content/uploads/2020/06/Capture.png)

Then they moved straight into the ransom deployment. With 2 tools apparently selected, screensaver.exe and 9689A16B72D48DAB.exe deployed right on the desktop.

![](https://media.giphy.com/media/ToMjGpjpXMFPshSYGLm/giphy.gif)

The screensaver executable doesn’t appear to have been used in attack and allows one to lock out access to the desktop.

![](https://thedfirreport.com/wp-content/uploads/2020/06/Annotation.png)![](https://thedfirreport.com/wp-content/uploads/2020/06/Annotation2.png)

Instead they ran the random number named executable which is of the Lockbit ransomware variety.

As expected we see the standard set of ransomware commands:
    
    
    \"C:\\Windows\\System32\\cmd.exe\" /c vssadmin delete shadows /all /quiet &amp; wmic shadowcopy delete &; bcdedit /set {default} bootstatuspolicy ignoreallfailures &; bcdedit /set {default} recoveryenabled no &; wbadmin delete catalog -quiet
    vssadmin delete shadows /all /quiet
    wmic shadowcopy delete
    bcdedit /set {default} bootstatuspolicy ignoreallfailures
    bcdedit /set {default} recoveryenabled no
    wbadmin delete catalog -quiet

Afterwards we saw the executable ping the entire /16 and then make SMB connections to alive hosts, but no actual infection was spread. We don’t understand why the ransomware did not spread as authentication was successful and shares were enumerated.

![](https://thedfirreport.com/wp-content/uploads/2020/06/bit1.png)

At this point, the malware completed its ransom of the one system leaving the following note below.

![](https://thedfirreport.com/wp-content/uploads/2020/06/bit2-e1591659124991.png)

Lockbit created the following reg keys:

![](https://thedfirreport.com/wp-content/uploads/2020/06/1.png)

### Lockbit Support Page:

This ransomware family uses a website and live chat functionality as opposed to previous families we investigated which have mostly relied on email contact.

![](https://thedfirreport.com/wp-content/uploads/2020/06/bit3-1024x646.png)

![](https://thedfirreport.com/wp-content/uploads/2020/06/bit4-1024x465.png)

##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2020/06/10/lockbit-ransomware-why-you-no-spread/&t=Lockbit%20Ransomware%2C%20Why%20You%20No%20Spread%3F)
  * [Share on X](https://x.com/share?text=Lockbit%20Ransomware%2C%20Why%20You%20No%20Spread%3F&url=https://thedfirreport.com/?p=392)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2020/06/10/lockbit-ransomware-why-you-no-spread/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=Lockbit%20Ransomware%2C%20Why%20You%20No%20Spread%3F&url=https://thedfirreport.com/2020/06/10/lockbit-ransomware-why-you-no-spread/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2020/06/10/lockbit-ransomware-why-you-no-spread/&title=Lockbit%20Ransomware%2C%20Why%20You%20No%20Spread%3F)
  * [Share by Mail](/cdn-cgi/l/email-protection#a19ed2d4c3cbc4c2d59cedcec2cac3c8d5849391f3c0cfd2ceccd6c0d3c48493e2849391f6c9d8849391f8ced4849391efce849391f2d1d3c4c0c58492e787829192999ac3cec5d89cc9d5d5d1d29b8e8ed5c9c4c5c7c8d3d3c4d1ced3d58fc2cecc8e939193918e91978e90918ecdcec2cac3c8d58cd3c0cfd2ceccd6c0d3c48cd6c9d88cd8ced48ccfce8cd2d1d3c4c0c58e)