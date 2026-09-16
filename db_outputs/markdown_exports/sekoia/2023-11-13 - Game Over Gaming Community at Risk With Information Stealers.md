# Game Over: Gaming Community at Risk With Information Stealers

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/game-over-gaming-community-at-risk-with-information-stealers
- **Date :** 2023-11-13

---

_This report was originally published for our customers on 26 October 2023._

The world of online gaming, a thriving global community of millions, has become an enticing target for malicious actors seeking to exploit related vulnerabilities.

In their engagement with virtual experiences, gamers frequently interact with, and download, a vast array of digital content, from mods and cheats to in-game purchases. The inclination for customisation and enhancement, often inherent to the gaming experience, has inadvertently opened doors for malware operators to exploit. With deceptive tactics that range from fake cheat codes to enticing in-game offers, these threat actors lure gamers into running their malicious payloads, notably related to infostealer.

Once executed on the targeted system, these stealer malware strains operate silently, exfiltrating personal information, in-game assets, and sensitive credentials. The scale and sophistication of this digital threat continue to escalate, causing serious concerns for individuals and the gaming industry at large.

This report delves into the gaming industry targeted by information stealer malware, and details a specific campaign spreading via Discord messages and fake download websites. Sekoia.io analysts identified several information stealer families among the strains observed in this campaign.

## Context

The targeting of gamers with infostealer malware is not a recent development; this threat has a longstanding history.

In July 2023, French gaming influencers were targeted in a novel campaign. As detailed on X (previously known as Twitter), they were compromised leveraging an infection chain beginning with a message within a Discord channel or through a personal message, which aims to promote a new game offering exclusive access. An image of the post made on 18 July 2023, was [found on X](https://twitter.com/Sarouh_B/status/1681325962997256199):

![Message \(in French\) on a public discord channel to promote a fake game. Source: Sekoia TDR](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fd6568d7e2b409e22b_6a92a35c4b4041c69342a3f2_6a2a7c478b996da41bea5185.webp)

Message (in French) on a public discord channel to promote a fake game. Source: Sekoia TDR

Recently the cloud gaming company Shadow emailed its users to warn about a compromise of their data. [According to Shadow](https://www.it-connect.fr/shadow-victime-dun-piratage-les-donnees-personnelles-de-500-000-utilisateurs-ont-fuite/), the initial access was a fake game downloaded from Discord. This incident is part of the broader campaign described in this report.

Payloads are delivered through messages coming from compromised accounts, notably those belonging to individuals of interest, to enhance their impact. The link included in the message leads directly to the download of a malicious file or to a fake website.

## Fake download websites

Sekoia.io analysts identified a cluster of fake websites inciting users to download video games. A complete list is available in the Indicators of Compromise section.

![Sekoia.io analysts identified a cluster of fake websites inciting users to download video games. Source: Sekoia TDR](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fd6568d7e2b409e225_6a92a35ea2f46752fd019b55_6a2a7c488b996da41bea51ba.webp)

Sekoia.io analysts identified a cluster of fake websites inciting users to download video games. Example of fake website madrain[.]studio. Source: Sekoia TDR

Some of those websites trigger connections to ipinfo[.]io to get the IP address of visitors before sending it through Discord webhooks. The code used to perform this fingerprint is similar to the one found in the GitHub repository “simple-ip-grabber”.

Once the target clicks on one of the “Download” buttons, it activates the download of a malicious file. From our observations, the download link can redirect to:

  * A specific file hosted on the website
  * A Discord attachment file (with or without shortened URL service before)
  * A MEGA link



Most downloaded files seen during our investigation were:

  * Rar archives (password protected)
  * Zip archives
  * Executable files



Independently of the file format, the malicious payload is packaged as a fake Electron app the execution of which initiates the information stealer. Multiple information stealer families were found during the investigation, including the two we identified as Doenerium and Epsilon Stealer.

Since the initial publication of this report, we identified more families distributed, namely BBy Stealer and Nova Sentinel.

Depending on the information stealer embedded, the stolen information could differ but information stealer family focuses on:

  * Browser information (passwords, cookies, _etc._) 
  * Credentials from applications (_e.g._ WinSCP, video games, Discord, _etc._)
  * Cryptocurrencies wallets



The execution of the fake games instantly triggers the malicious payload stealing data of interest. Depending on the payload configuration, a fake page asking for a beta code is displayed as a lure:

![The execution of the fake games instantly triggers the malicious payload stealing data of interest. Source: Sekoia TDR](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fd6568d7e2b409e22e_6a92a35d693fca262e1b9259_6a2a7c488b996da41bea51b7.webp)

Lure window displayed to the user once the malicious file is executed. The execution of the fake games instantly triggers the malicious payload stealing data of interest. Source: Sekoia TDR

## Information stealer families

In this part, we delve into the two distinct information-stealer families we initially identified: Doenerium and Epsilon Stealer, the other detected families being under ongoing analysis. As of late October 2023, all malware families have low detection rates by antivirus.

### Doenerium

**Doenerium** is an information stealer available on GitHub. An updated version is also promoted on Telegram and hacking forums such as BlackHatRussia, HighSec, Haxf4rall FreeHacks and HireMeHacker.

The following are Doenerium features such as advertised on GitHub:

  * Autostart (Startup)
  * Discord Token
  * Discord Info - Username, Phone number, Email, Billing, Nitro Status & Backup Codes
  * Discord Friends with rare badges
  * Grabs crypto wallets 
  * Browser (Chrome, Opera, Firefox, OperaGX, Edge, Brave, Yandex) - Passwords, Cookies, Autofill & History (Searches for specific keywords such as PayPal, Coinbase _etc._ in them)
  * Screenshot(s)



All observed samples communicate with the following domain (or its subdomains): kqnfkpoccicxiudstqonfotuwsrhuxkwhqjjfsbjhonoubrccy[.]nl

Doenerium uses basic Windows commands to fingerprint the host:

  * %WINDIR%\system32\cmd.exe /d /s /c "chcp"
  * %WINDIR%\system32\cmd.exe /d /s /c "tasklist"



Those commands are also used by other information stealers, as well as by some legitimate software. While they can still be used for detection, it is highly likely that these commands will generate false positives and thus advanced filtering is needed.

### Epsilon Stealer

Epsilon Stealer is an information stealer sold on Telegram and Discord by its alleged author. 

#### Malware promotion on Telegram

Administrators of Telegram channel “Epsilon” (hxxps://t.me/s/epsilonoff) are two French-speaking users known as “chatnoir” and “benef”. According to messages posted in different channels, these actors operate a wide range of malicious activities beyond selling information stealers. 

An Epsilon licence is advertised on Telegram at:

  * $15 per week
  * $35 per month
  * $80 for three months



Both the alleged source code leaked on GitHub and the analysis of the malware behaviour offer some interesting detection opportunities, as detailed below.

Of note, on 27 October 2023, Epsilon channel administrators claimed the attack on Shadow discussed before:

![Shadow attack's claimed by Epsilon stealers administrators. Source: Sekoia TDR](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5fd6568d7e2b409e228_6a92a35b4b4041c69342a310_6a2a7c478b996da41bea5153.webp)

Shadow attack's claimed by Epsilon stealers administrators. Source: Sekoia TDR

#### Detection opportunities

The Command & Control server used by the malware changed from api.epsilon1337[.]com to wdb[.]life between June and August 2023. When detected in logs, the traces of these domains are indicative of a compromise by Epsilon Stealer.

## How to prevent these attacks?

To mitigate the risk of malware infection, it is recommended to only access official and trusted sources like official websites, app stores, or authorised distributors when downloading software, video games, applications, and other digital content. This practice can significantly lower the chances of executing malware.

It is also important not to interact with cracked or pirated software, video games, and media content. These unauthorised versions often include hidden malware or altered code that can put your security at risk.

It is also necessary to educate users about the tactics used by cybercriminals. Users should be cautious about enticing offers, fake notifications, or messages intended to induce alarm, designed to lure them into downloading harmful files.

## What to do after infection?

The first thing to do after being infected by an information stealer is to consider a reset of the impacted computer. Indeed, some malware are very persistent and are not well detected by antivirus software. 

Moreover, it is very important to change all the passwords used on your computer and your online accounts, as they should be considered as compromised. While changing your passwords for online accounts, make sure to revoke session cookies, that could allow threat actors to access accounts without authentication.

Users should also avoid password reuse, and we strongly recommend using a password manager.

## Conclusion

The gaming community must remain vigilant in the face of widespread and ever-evolving cybercrime threats. As these users often install various software to enhance their experience they become vulnerable to cybercriminals. Threat actors typically employ social engineering tactics through social networks to entice gamers into executing their malicious code. 

The accessibility and user-friendliness of information-stealer families make them an attractive option for less experienced threat actors, commonly referred to as "script kiddies", who aim to steal valuable data.

By arming themselves with knowledge and following best practices for online safety, gamers can continue to enjoy their virtual adventures without falling prey to malicious actors seeking to compromise their personal data. 

## Indicators of compromise

### Domains associated with fake game download website

#### Domains associated with doenerium

kqnfkpoccicxiudstqonfotuwsrhuxkwhqjjfsbjhonoubrccy[.]nl doenerium[.]kqnfkpoccicxiudstqonfotuwsrhuxkwhqjjfsbjhonoubrccy[.]nl

#### Domains associated with Epsilon

api.epsilon1337[.]com  
wdb[.]life