# Lapsus$: When Kiddies Play in the Big League

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/lapsus-when-kiddies-play-in-the-big-league
- **Date :** 2022-03-23

---

You may have recently heard about Lapsus$, a group that seems to specialize in extortion without necessarily leveraging ransomware.

At first glance, Lapsus$ check marks all elements that would make researchers put them in the low priority threats, especially considering their readiness to make dramas and OpSec failures. Except that the group has successfully managed to significantly enrich its victim list with high profile corporations, thus drawing all our attention.

In the following piece, we will describe the threat actor profile that was drawn by our investigations based either on OSINT, dark web or infrastructure analysis.

## **High profile targets**

Since the announcement of its first victim in December 2021, Lapsus$ has engaged in extortion attempts with at least 15 different entities.

![Lapsus$ has engaged in extortion attempts with at least 15 different entities.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56a2_6a92a4f4fd507e2a51b9e9c5_6a2a7800c5337e0183cdc9b5.webp)

Lapsus$ has engaged in extortion attempts with at least 15 different entities.

While initially focused on Brazilian government bodies, the group was recently targeting large technology, telecom, automotive and retail businesses around the world. Among its high-profile victims: Samsung, Nvidia Corporation and Vodafone.

The group recently announced a new victim on its Telegram channel, which is the authentication services provider Okta. Lapsus$ would have gained access in the company’s network on January, 21, if not earlier, and made its attack public on March 22. If confirmed, this incident may result in a very damaging software supply chain attack.

Despite some politicized statements (for example, a political message with curses to the Brazilian President Bolsonaro attackers left in one of their extortion letters), Lapsus$ argue they are only operating for financial gain purposes: “our only goal is money, we are not state sponsored and we are not in politics at all”.

## **Going further into their history**

While Lapsus$ is currently claiming to only operate via Telegram (“we don’t have any other socials”), the group seems to have a connection to a threat actor named “4c3” who has been active on several cybercrime forums since at least May 2021. 4c3 started by selling a German company’s customer data on RaidForums and Exploit underground forums and then two months later, he made his first major victim – the gaming giant Electronic Arts (EA). The group represented by 4c3 had leaked large amounts of data (20-25 terabytes) concerning EA, but also source code.

The point is that 4c3 has already declared being part of the Lapsus$ group on July 20, 2021, while discussing the EA attack on the RaidForums hacking forum and he signed its very last publications on several cybercrime forums as follows: “Please note that this account won’t be used again. Remember our name. LAPSUS$”.

![Statement of Lapsus$](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56aa_6a92a4f3fd507e2a51b9e90c_6a2a7800c5337e0183cdc9b2.webp)

Statement of Lapsus$

Thus, we can suppose that this group has moved from cybercrime forums to other methods of reaching out to the public and to the victims.

Another connecting element between the actors who compromised EA (with 4c3 as representative) and the Lapsus$ group: the Monero wallet address they communicate to victims. The ransom note sent to Electronic Arts which we were able to consult contained the address of this Monero wallet to be used for ransom payment: 

`42qLW1FiEDQKjeoSAFQRXaVpSUxB8fTYJ2Zeah8dcDTYDEjCb71iCR76ctGMysAB4nj3MTTCE5GuJMsC1eLuwKdu7v6FKf3`

This same address led us to another series of extortion attempts dated early August 2021 and signed Lapsus$. These extortion campaigns targeted the users and clients of the Lapsus$ victims, in order to put more pressure on them.

![extortion attempts of Lapsus$](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56b3_6a92a4fbdb65986262ae2a01_6a2a7801c5337e0183cdc9d2.webp)

extortion attempts of Lapsus$

![extortion attempts of Lapsus$](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56ad_6a92a4fac9e0b85494c04ef8_6a2a7801c5337e0183cdc9cf.webp)

extortion attempts of Lapsus$

## **Leaks sharing and extortion strategy**

In our knowledge, Lapsus$ used a website only once to claim its involvement in a campaign. For the vast majority of their operations, they rather chose to threaten their victims with the data leakage and share the related leaks on a Telegram channel they created in December 2021. The channel has at the time of writing more than 32400 subscribers.

Choosing to use Telegram rather than an onion website such as the majority of [ransomware or extortion groups](/blog/vice-society-a-discreet-but-steady-double-extortion-ransomware-group) could be a smart approach since a Telegram channel is more easily reachable by the large public in comparison with a website requiring the use of TOR.

They also use this channel to add pressure on victims by sharing polls asking their community to vote for the next leak to be shared by the group.

![Extortion strategy of Lapsus$](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56b6_6a92a4ff3e6167cebbf74837_6a2a7801c5337e0183cdc9dc.webp)

Extortion strategy of Lapsus$

In parallel, they also created an open Telegram channel named “Lapsus$ chat” where every member (more than 8500 members currently) is invited to talk about various hacking topics.

Discussions in this chat are mainly kept in Portuguese. More recently, Russian-speaking participants have also joined the discussion. Moreover, this chat is also used as a platform to encourage cooperation between its members and serve as a recruitment mechanism between the chat members themselves, for various tasks related to upcoming cyber attacks.

![Extortion strategy of Lapsus$](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56cc_6a92a500c5553634ac94cab6_6a2a7802c5337e0183cdc9e4.webp)

Extortion strategy of Lapsus$

Hence, It will not be surprising that abusing a legit service, such as Telegram, would become a trend towards which cybercriminals will tend in the future to threaten their victims with data disclosure.

For the first time since its existence, Тelegram became the most popular instant messenger in Russia in mid-March, being both a communication tool and one of the main sources of information (after Russia restricted the access to other social networks and messengers). Globally, Telegram is becoming increasingly popular among threat actors, competing with other messaging apps such as Discord.

The Lapsus$ group representative is actually communicating on its Telegram channel in both Portuguese and English. The Portuguese language was used in the Ministry of Health of Brazil’s defacement campaign. Nevertheless, there are indications that the group uses machine translation to communicate in Portuguese. According to a [tweet](https://twitter.com/YourAnonNewsBR/status/1469307958160932869) by the group Anonymous Brazil, Lapsus$ would be formed by people of Spanish and Colombian nationality. This statement can not be validated at the moment.

## **Lapsus$, the art of self-doxing and first OpSec failures**

Few months ago, Doxbin, a famous data-sharing website that includes huge amounts of personal information on both attackers and their victims, was sold to an individual under the nickname of “White”, who is/was allegedly a high ranked member of the Lapsus$ group, if not the leader. While things did not go as planned, White agreed to sell the website back to the previous owners.

Eventually, he got upset when the owners excluded him from the community Discord server. After some drama, White decided in revenge to leak the user database in plaintext.

![Lapsus$, the art of self-doxing and first OpSec failures](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56c9_6a92a4f5db65986262ae280c_6a2a7800c5337e0183cdc9b8.webp)

Lapsus$, the art of self-doxing and first OpSec failures

The biggest OpSec failure here is that White, aka Alexander, leaked the database that also includes its own personal information and passwords, which people quickly took advantage of.

Hence, the dox revealed that “White” aka Alexander, of the Lapsus$ group, was a 16 years-old boy native of Albania, living with his mother in the United Kingdom, where he was attending a specialized school.

![Lapsus$, the art of self-doxing and first OpSec failures](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56b0_6a92a4f832517fc40260aed9_6a2a7801c5337e0183cdc9c9.webp)

Lapsus$, the art of self-doxing and first OpSec failures

While our investigations lead us to believe that it is highly likely that the dox content is truthful, it is expected that it will quickly lead the law enforcement to an arrest.

![Lapsus$, the art of self-doxing and first OpSec failures](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56bc_6a92a4fc69291914889aa060_6a2a7801c5337e0183cdc9d5.webp)

Lapsus$, the art of self-doxing and first OpSec failures

Furthermore, we have reasons to think that Alexander aka White is also the owner of the account doxbinwh1ite on Exploit. In December 2021, this user was looking to be recruited by HelloKitty or REvil groups, arguing he owned access to companies such as LG, Samsung and EA Games. A victim list that accurately matches the companies that Lapsus$ announced to have breached.

This would lead us to think that while he didn’t succeed in joining these [ransomware groups](https://www.sekoia.com/blog/sekoia-io-mid-2023-ransomware-threat-landscape), he rather has chosen to use these accesses to build Lapsus$ reputation instead.

## **Drama and a proven immaturity**

In the meantime, the threat actor is still exposing internal conflicts within the group, doxxing each other. In the message below, which was quickly deleted, Lapsus$ exposed the Telegram user @redeyeg0d, formerly a member of the group.

![Proven immaturity of Lapsus$](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56c6_6a92a4fda2f46752fd02ae3e_6a2a7801c5337e0183cdc9d8.webp)

Proven immaturity of Lapsus$

While investigating the footprints of this user, we found a ransom note left following the encryption of a victim’s systems by a strain of Babuk ransomware. In the note, it was mentioned that 200 GB of data were exfiltrated and all the files were encrypted. At the end of the note, the victim is invited to contact @redeyeg0d on Telegram. Since only @redeyeg0d was mentioned in the ransom note, we can not bind the Lapsus$ group to this usage of Babuk ransomware, or any other ransomware.

### **Pretty bad OpSec we said ?**

Investigating Lapsus$ recent infrastructure, we surprisingly found that the IP address used as a C2 in a campaign resolves to a domain dubbed after the group’s name.

Hence, it appears that Lapsus$ used the associated website to claim for an attack where they allegedly encrypt the victim’s system with ransomware. This is the only mention that they may have used ransomware in a campaign.

![Lapsus$ threatening one of their victims. In translation from Portuguese, the message reads “Hello. We are back \[…\] Let’s explain a few things: our only goal is to get money, we don’t care about the Bolsonaro family \[…\] a bunch of servers have been sent to the ‘dead data’ cemetery. The solution is to pay the ransom](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56a7_6a92a4f6db65986262ae284a_6a2a7800c5337e0183cdc9bd.webp)

Lapsus$ threatening one of their victims. In translation from Portuguese, the message reads “Hello. We are back […] Let’s explain a few things: our only goal is to get money, we don’t care about the Bolsonaro family […] a bunch of servers have been sent to the ‘dead data’ cemetery. The solution is to pay the ransom."

The same IP was on our Sekoia IOCs database, since it was used to host metasploit service on its default ssl port 3790, also using the default metasploit ssl certificate.

![Enter the SSL port that the Metasploit service should use. By default, the server uses port 3790 for HTTPS.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56b9_6a92a4f29f9b7f8b2cd0eaef_6a2a7800c5337e0183cdc9af.webp)

Enter the SSL port that the Metasploit service should use. By default, the server uses port 3790 for HTTPS.

Hence, the attacker has made no effort to change the basic configuration of the metasploit framework in a will to avoid detection.

### **Too big to be real?**

Earlier this month, Lapsus$ shared another message on its Telegram before, once again, quickly deleting it.

In this message, they uploaded a picture to potentially claim being at the origin of a disruption on the bleepingcomputer website (which was not disrupted at that time), or announce a future attack on the target.

![Figure 12. A picture uploaded by a Lapsus$ member on their telegram before quickly deleting it](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56c2_6a92a4f7db65986262ae28a3_6a2a7800c5337e0183cdc9c0.webp)

A picture uploaded by a Lapsus$ member on their telegram before quickly deleting it

By looking carefully at the bookmarked pages, we can see the threat actor bookmarked a GitHub account that includes links to metasploit framework, brute force modules and qbot scanner setup.

![The bookmarked github account](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56bf_6a92a4f963e0c17b5dade99a_6a2a7801c5337e0183cdc9cc.webp)

The bookmarked github account

Whether the bookmarked account belongs to a member of the Lapsus$ group is not clear, however this would not be the first OpSec failure known by the group.

### **Nevertheless talented kiddies**

Despite all the drama and OpSec failures these investigations have revealed regarding Lapsus$ group, they undoubtedly are talented hackers who successfully managed to get into high profile victims. Unless an arrest comes to disrupt their operations and integrity as a group, Lapsus$ is a threat not to be underestimated.

Furthermore, at the moment, the group has not shown any desire to cease its activities. On March 10, Lapsus$ announced on its Telegram channel they were recruiting for employees/insiders working in the telecommunications, IT and Internet providers sectors. They specify that they are not looking for data but employees able to provide VPN or Citrix accesses. Which is consistent with the incidents we know of, where the favorite initial access leveraged by the group was spear [phishing campaigns](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers) leading to valid accounts.

![Lapsus$ insiders recruitment announcement](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69a69291914889b56cf_6a92a4ff69291914889aa262_6a2a7802c5337e0183cdc9e0.webp)

Lapsus$ insiders recruitment announcement

It would seem that the group’s appeal has already resulted in the compromise of a big corporation through an insider. According to the declarations of an alleged Lapsus$ member on March 22, 2022, the group has corrupted an employee of one of the world’s leading technology companies and this insider would be “the only person [they] paid”.

### **Fame and glory?**

For the very recent victims announced by Lapsus$ group, there is no evidence that Lapsus$ have publicly threatened them to pay a ransom in order to keep their data safe from being shared, unlike previous victims. Thus driving us to question the real motivations of the group.

The analysis of their behavior highly clays for a willingness to prompt people to talk about the group, thus drawing the profile of individual(s) looking for fame and glory, as we have seen in the past with the LulzSec group for instance.

### **TTPs (ATT &CK)**

Phishing (T1566)  
Exploit Public-Facing Application (T1190)  
Valid Accounts: Local Accounts (T1078.003)  
Valid Accounts: Cloud Accounts (T1078.004)  
External Defacement (T1491.001)  
Automated Exfiltration (T1020)

You can also discover our:

  * [CTI platform](https://www.sekoia.com/platform/intelligence)
  * [AI SOC platform](https://www.sekoia.com/platform)
  * [SIEM solution](https://www.sekoia.com/platform/defend)