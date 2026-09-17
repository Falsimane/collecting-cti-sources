# Sqlserver, or the Miner in the Basement - The DFIR Report

- **Source :** dfir-report
- **URL :** https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/
- **Date :** April 20, 2020

---

![](https://thedfirreport.com/wp-content/uploads/321.png)

[cryptominer](https://thedfirreport.com/category/cryptominer/)

# Sqlserver, or the Miner in the Basement

April 20, 2020 

A threat actor logged into the honeypot via RDP and installed XMRig with multiple persistence mechanisms. The actor used icacls and attrib to lock down directories and files to make detection and eradication difficult.

While bitcoin was at $20K, actors dropping mining software was all the rage, but with Bitcoin and most currencies less than half their peak value you’d be forgiven thinking the malicious cryptominer has gone away. These days the news points to big game ransomware as the hottest threat actor trend. And while that may be the case don’t forget about the cryptominers.

## Intial Access

Initial entry was completed by two different IP addresses via RDP.
    
    
    95.156.252.94   
    185.155.96.83

## Artifacts

### sqlsupdater.exe

## ![](https://thedfirreport.com/wp-content/uploads/2020/04/image-28.png)

### conhost.exe

Ever heard of the Non-Sucking Service Manager (NSSM)?

nssm is a service helper which doesn’t suck. srvany and other service helper programs suck because they don’t handle failure of the application running as a service. If you use such a program you may see a service listed as started when in fact the application has died. nssm monitors the running service and will restart it if it dies. With nssm you know that if a service says it’s running, it really is.

We think NSSM is used to manage the sqlserver.exe process which includes the miner. Read more about NSSM [here](https://nssm.cc/).

### install.bat

The install script does as is named and is used to deploy the actors payload. Some notable actions in the script include hiding the files in the C:\Windows\Fonts\ location and then using DACLs via icacls scripting to remove access to the miner. Additionally as with many late stage miners, they look to kill competition that may be running on the box they’ve infected. (There are multiple misspellings in these scripts but they do accomplish their overall goal.)

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-26.png)

### sqlserver.exe

This is the Monero coin miner binary known as XMRig. Here are a few strings from the binary.

![](https://thedfirreport.com/wp-content/uploads/2020/04/miner0408-6.png)

You can see from the below strings that this is most likely XMRig version 5.1.0.

![](https://thedfirreport.com/wp-content/uploads/2020/04/123-e1587397743466.png)

This binary is attempting to mimic sqlserver 2.7.8.2 which is not a real sql version.

![](https://thedfirreport.com/wp-content/uploads/2020/04/321.png)

For more information on XMRig see a write up on [securityintelligence.com](https://securityintelligence.com/xmrig-father-zeus-of-cryptocurrency-mining-malware/) and XMRigs [GitHub](https://github.com/xmrig/xmrig) page.

## sqlsupdater.sfx.exe

## ![](https://thedfirreport.com/wp-content/uploads/2020/04/image-29.png)

sqlsupdater.sfx.exe contained the two files above and appears to include Neshta which is usually used for persistence. Here are a couple interesting strings from the binary.

![](https://thedfirreport.com/wp-content/uploads/2020/04/aaa2.png)

Neshta installs itself into the registry for persistence using the following:

Registry key: HKLM\SOFTWARE\Classes\exefile\shell\open\command  
Value: %SystemRoot%\svchost.com “%1” %*

Read more about Neshta at [Cylance](https://threatvector.cylance.com/en_us/home/threat-spotlight-neshta-file-infector-endures.html).

## update.bat

update.bat is used to run an update (go figure). It deletes scheduled tasks if they exist, deletes old binaries, creates directories, sets permissions on the new files and then starts sqlsupdater.exe

![](https://thedfirreport.com/wp-content/uploads/2020/04/image-30.png)

Other pools that are used in crypto-currency mining are added to the hosts file and directed to local host. This may be to help protect the infected machine from competing crypto-mining malware campaigns.

![](https://thedfirreport.com/wp-content/uploads/2020/04/a2a.png)

The next sequence creates multiple scheduled tasks and then cleans up after itself.

![](https://thedfirreport.com/wp-content/uploads/2020/04/11.png)

## Mining

The miner is finally invoked via command-line arguments that include the mining pools in use for the payout as well as the key used.

![](https://thedfirreport.com/wp-content/uploads/2020/04/miner0408-3.png)

Thus far this particular wallet has received little payout. With 1.32 XMR or about $70 USD at time of publication. It is possible that they are using multiple keys across the campaign to avoid tracking or having funds locked by a pool for abuse reports.

![](https://thedfirreport.com/wp-content/uploads/2020/04/miner0408-2-1024x606.png)

Summary

Cryptomining is still alive and well! The attackers use of icacls and attrib were quite interesting and provide a few examples for easy detection writing. We also found it interesting that there were multiple persistent mechanisms from Neshta to NSSM to scheduled tasks and services.

If you get stuck in a position where you can’t see or access files, the easiest thing to do is to become system by using psexec or something similar. This allows you to access all files, folders, scheduled tasks, etc. We were fairly impressed by the completeness of this attack. It appears that these actors have been in the business for awhile or they are buying their tools.

Although the actors haven’t earned very much according to this wallet, if you do this at scale and/or without costs, the benefits are there, especially for operators in developing countries.

Enjoy our report? Please consider donating $1 or more to the project using [Patreon](https://www.patreon.com/thedfirreport). Thank you for your support!

## IOCs

Source IPs of RDP login
    
    
    95.156.252.94   
    185.155.96.83

Exe File hashes
    
    
    sqlsupdater.sfx.exe|77600facbd18746636921bab1a3918e0
    77600facbd18746636921bab1a3918e0
    bcb89eade054991169ebf1df6499011610198a5a
    cf3509a100b6110da866af3f7c1a514c6c27ca82b1105d0e45a2469f8e87426d
    sqlserver.exe|12959e0e561670229c98b4978d7b4738
    12959e0e561670229c98b4978d7b4738
    5b70d3e0182b553593cd8ca3c907d68018fd7f1f
    1acb9ba8ddf74e1b4a8da54390605f33b31c7976a49fa135b5ab0613b277196f

Mining pool domains:
    
    
    domain004.gleeze.com
    test1000.ooguy.com
    test1003.accesscam.org
    gamepanel2.theworkpc.com
    xmr-eu1.nanopool.org

[sqlsupdater.exe](https://app.any.run/tasks/a71d5a4b-88d5-4caa-97e2-fda19bb447f6)

![](https://thedfirreport.com/wp-content/uploads/2020/04/1-1.png)

[sqlsupdater.sfx.exe](https://app.any.run/tasks/e08cde64-dcf4-4b0b-9b51-c9b30e9a16df)

![](https://thedfirreport.com/wp-content/uploads/2020/04/1.png)

### Persistence Mechanisms

Registry key: HKLM\SOFTWARE\Classes\exefile\shell\open\command  
Value: %SystemRoot%\svchost.com “%1” %*

sqlbrowsers service name, multiple service names in the .bat files above in artifacts.

Multiple scheduled tasks were created, see the .bat files above in artifacts.

##### Share this entry

  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/&t=Sqlserver%2C%20or%20the%20Miner%20in%20the%20Basement)
  * [Share on X](https://x.com/share?text=Sqlserver%2C%20or%20the%20Miner%20in%20the%20Basement&url=https://thedfirreport.com/?p=44065)
  * [Share on WhatsApp](https://api.whatsapp.com/send?text=https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/)
  * [Share on Linkedin](https://linkedin.com/shareArticle?mini=true&title=Sqlserver%2C%20or%20the%20Miner%20in%20the%20Basement&url=https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/)
  * [Share on Reddit](https://reddit.com/submit?url=https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/&title=Sqlserver%2C%20or%20the%20Miner%20in%20the%20Basement)
  * [Share by Mail](/cdn-cgi/l/email-protection#a59ad6d0c7cfc0c6d198f6d4c9d6c0d7d3c0d78097e6809795cad7809795d1cdc0809795e8cccbc0d7809795cccb809795d1cdc0809795e7c4d6c0c8c0cbd1838695969d9ec7cac1dc98cdd1d1d5d69f8a8ad1cdc0c1c3ccd7d7c0d5cad7d18bc6cac88a979597958a95918a97958ad6d4c9d6c0d7d3c0d788cad788d1cdc088c8cccbc0d788cccb88d1cdc088c7c4d6c0c8c0cbd18a)