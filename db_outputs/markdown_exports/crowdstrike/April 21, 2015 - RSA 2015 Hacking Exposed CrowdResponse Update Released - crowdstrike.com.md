# RSA 2015 Hacking Exposed: CrowdResponse Update Released - crowdstrike.com

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/crowdresponse-windows-sticky-keys/
- **Date :** April 21, 2015

---

# RSA 2015 Hacking Exposed: CrowdResponse Update Released

April 21, 2015

• [ Robin](/en-us/blog/author.robin/ "Posts by Robin") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

George Kurtz, Dmitri Alperovitch and Elia Zaitsev have just finished up the [Hacking Exposed: Beyond the Malware session](https://www.rsaconference.com/events/us15/agenda/sessions/1815/hacking-exposed-beyond-the-malware) at the RSA 2015 Conference. In the session, they demonstrated how to conduct an end-to-end attack against an enterprise without use of any malware binaries. The attack included real adversary tradecraft that CrowdStrike's [Falcon Host](/en-us/products/) next-generation endpoint technology detected and stopped in our customer networks. The session also highlighted the need to leverage an Indicator of Attack (IOA) approach to detecting these threats, since Indicators of Compromise (IOCs) will not pick up non-malware based attacks. Click [here](https://s3.amazonaws.com/download.crowdstrike.com/presentations/RSA2015-HackingExposed.pdf) to download the presentation slides from the talk. The talk also demonstrated the use of a so-called Kerberos Golden Ticket attack, the use of which is becoming increasingly more common amongst advanced adversaries. CERT-EU has published an excellent paper explaining the attack and describing some detection and mitigation strategies for it. In our continuing advancement of the community  _CrowdResponse_ tool, today we also released another new module **@mal** that was demonstrated in the session.

### CrowdResponse Tool Update

This new module will eventually become a repository for a selection of common malware/hacking detection capabilities. These detections may already be possible with the tool through the use of other modules such as examination of a number of registry keys or files, but having a quick and easy one-stop solution for common tactics and procedures is very useful. Our first addition to the **@mal** module is detection for a well known but still very widely used exploit utilizing Windows accessibility options often referred to under the umbrella term of the **_Sticky Keys_** exploit. Our [Services](/en-us/services/) team regularly encounters this on their engagements even today, many years after this _feature_ was first seen to be abused. _Sticky Keys_ is an accessibility feature in Windows aiding handicapped users, allowing them to press a key, such as Shift, 5 times, to activate the feature. Once activated the user no longer needs to keep the Shift key simultaneously depressed when wanting to capitalize letters or use other key characters normally obtained by holding down a regular modifier key. Use of this _CrowdResponse_ module is simple. On the command line use syntax similar to this:
    
    
    CrowdResponse @mal -s
    

The **-s** option specifies the "Sticky Keys" feature in the **@mal** module. This will show the XML in the console window which is not terribly useful, so usually you'd send the results to a file for later examination or conversion by specifying the main -o option as in:
    
    
    CrowdResponse -o out.xml @mal -s
    

Conversion to another file format using the accompanying _CRConvert_ utility would then be done using a command such as this.
    
    
    CRConvert -v -f out.xml -o Results -c -h -x
    

You should then see CSV (-c), HTML (-h) and Text (-x) versions of the results in the _Results_ directory. In the case of Sticky Keys, the executable launched upon instantiation of the feature is usually located at _%SystemRoot%\System32\sethc.exe_. However, despite increased protection for these "system" binaries in later versions of Windows, the operating system does not check the integrity of this specific binary and thus a malicious user with sufficient privileges (admin level) can replace this with one of their choosing. Typically this is the command shell executable "_cmd.exe_ " which would result in the malicious user being able to launch an instance of the command console with full **SYSTEM** rights directly from a login prompt simply by pressing the Shift key 5 times. This completely bypasses all authentication that would normally be required to access the system. So you may be thinking that if you need elevated privileges to replace this binary, why would need to go to the trouble of placing this backdoor access when you already have total control over the affected system? There are several reasons.

  * Since you do not need to know credentials to gain access, this hack will circumvent any password changes made in an attempt to secure the system.
  * This hack does not typically use any 3rd party tools and so doesn't set off any alarms.
  * It works even on Terminal Servers - perfect for gaining and retaining remote access.



It's not just the Sticky Keys accessibility feature that can be hijacked. There are other features for different kinds of accessibility that can also be similarly utilized in a malicious manner by replacing their associated handler executable. These include:

  * utilman.exe (Utility manager)
  * magnify.exe (Screen Magnifier)
  * osk.exe (On-Screen Keyboard)
  * narrator.exe (Narrator)



In _CrowdResponse_ parlance you will see in the XML output (or CSV, HTML or Text if you convert the XML with the companion utility CRConvert) details of the "integrity" of the above mentioned files including a column saying whether the system appears to have been hijacked through misuse of the "_integrity _" of these files ("_ integrity/vulnerable: TRUE/FALSE_"). The process for determining vulnerability is:

  * Check for _sethc.exe_ , _utilman.exe_ , _magnify.exe_ , _osk.exe_ , _narrator.exe_ in the system directory (e.g. C:\Windows\system32).
    * Determine if they are genuine and not substitutes:
    * Vulnerability is TRUE if
      * File properties "_Company Name_ " is not "_Microsoft Corporation_ " OR
      * File properties "_Internal Name_ " is not as expected OR
      * Digital certificate is not valid or not signed as "_Microsoft Windows_ "



Full details of the utilized substitute file (if present) will be seen in the _CrowdResponse_ output.

### But wait! There's more!

Another way of hijacking accessibility features on Windows involves editing the Registry to tell the system that there is a debugger that should be used when referencing the respective files. A debugger for an application can be specified by creating a "Debugger" name entry at
    
    
    HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\<name of binary>
    

with the value given to the Debugger entry being the binary that should be used to launch the associated supposed "accessibility" application. Here is an example of implanting this backdoor from a command prompt using built-in Windows tools. Once the backdoor has been implanted you can access it at the logon prompt using the Windows accessibility features. In this case the on-screen keyboard. You will now find yourself prresented with **SYSTEM** level command prompt access! Once more, you will see in the _CrowdResponse_ output references to the "debugger" state of the mentioned files together with a column saying whether the system appears to have been hijacked through misuse of the "debugger" feature for these files. The process for determining vulnerability is:

  * Check the registry at _HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ for the "_ Debugger*" name and extract the associated file path value.
    * Vulnerability is TRUE if
      * Debugger value is present



Full details of the utilized file, if present, are also presented in the output along with a column representing determined vulnerability ("_debugger/vulnerable: TRUE/FALSE_ ") That's all for today. Stay tuned for new _CrowdResponse_ features coming soon! **Download _CrowdResponse 1.0.5.0_ [here](/en-us/community-tools/)**. For more information on CrowdStrike Falcon® Next-Generation Endpoint Protection, please visit [/content/crowdstrike-www/locale-sites/us/en-us/products/](/en-us/products/) or request a demo

[/content/crowdstrike-www/locale-sites/us/en-us/request-a-demo/](/en-us/request-a-demo/).

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)