# Securing Gold : Hunting typosquatted domains during the Olympics

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/securing-gold-hunting-typosquatted-domains-during-the-olympics
- **Date :** 2024-09-11

---

Anticipating Paris 2024 Olympics cyber threats, Sekoia.io has conducted**over July and August 2024** a proactive **hunting of Olympics-typosquatted domains** registered by malicious actors - cybercrime related and possibly APT campaigns - in order to detect any kind of operations though the detection of connexion to typosquatted domains (phishing, C2).

This work is complementary to [our general assessment of cyber threats on Paris Olympics](/blog/securing-gold-assessing-cyber-threats-on-paris-2024), published in January 2024. As stated at that time, every Olympic event is a boon for malicious actors, in particular for cybercrime-related, lucrative actors leveraging the Games to conduct campaigns involving phishing attacks, fraud schemes such as fake ticketing or online betting solutions.

We also estimated a risk for state sponsored-related cyber espionage or destructive operations, but **no major incidents** were reported in open source.

In this blogpost, we will expose our hunting techniques and analyse the suspicious domains we detected.

## **Our hunting typosquatted domains process**

Since early June 2024, the Sekoia Threat Detection & Research (TDR) team has been applying a methodology to **detect domain names attempting to fake official websites** responsible for the Paris 2024 Olympic Games. The objective of this monitoring was to **record the opportunistic websites newly registered** , on a day-to-day basis, and to investigate each infrastructure in detail to find malicious activity.

To achieve this, we established a comprehensive list of **legitimate and official domain** names related to the Olympics. In total, we identified over **149 legitimate domain names pertaining to 110 different sectors**. This list includes official websites dedicated to the Olympic Games, institutional entities, media partners, international partners and the cities in France hosting the events.

Based on this, we setted up DNS Fuzzing using the [DNSTwist](https://github.com/elceef/dnstwist) security tool. It is designed to detect typosquatting and phishing attempts by identifying possible permutations of domain names. It generates potential variations of a domain, checks whether these domains are active and inspects SSL certificates. Furthermore, a Censys request has been designed to monitor SSL certificates granted for newly created domains.

`(  
names:/olympics2024\..*/   
OR names:/jo2024\..*/   
OR names:/olympics2024\..*/   
OR names:/paris2024\..*/   
OR names:/sports.gouv\..*/   
OR names:/pass-jeux\..*/   
OR names:/anticiperlesjeux\..*/   
OR names:/ticketparis2024\..*/   
OR names:/transport-public-paris-2024\..*/   
OR names:/iledefrance-mobilites\..*/  
[...]  
)   
AND parsed.validity_period.not_before:[ now-10d TO * ]  
`

## **Our results**

From 13 June 2024 to 13 August 2024 - cut-off date for this paper - we found, assessed and monitored through the Sekoia SOC platform **more than 650 typosquatted Paris 2024 domains**. They are all in detection and linked to the STIX Infrastructure object named [Typosquatted domain names for the 2024 Olympic Games](https://app.sekoia.io/objects/infrastructure--40569a77-0f4a-45ba-ac11-88604ce54283), that we created for capitalising.

First, it was interesting to observe a **higher volume** of registration in the **weeks before the Olympics** , with **a spike** on the days before the opening ceremony. We compiled all registration dates in the following scheme.

![Typosquatted domain names for the 2024 Olympic Games.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a49f9b7f8b2cd152c4_6a92a2773e6167cebbf5e46d_6a2a7e00bf2797708e09b035.webp)

Typosquatted domain names for the 2024 Olympic Games.

The spike in registration on the days before the opening ceremony coincided with a worldwide media attention to the incoming event, with the arrival of national teams, athletes and foreign media. It shows the **opportunistic approach** to the majority of Olympics-typostatted domains.  
We worked on **sorting the domains** through their **supposed type** of cybercrime-related objectives or lucrative finality.

![Distribution of typosquatted websites types](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a49f9b7f8b2cd152c7_6a92a276cd1cab63350c80e8_6a2a7e00bf2797708e09b031.webp)

Distribution of typosquatted websites types

### **Ticketing scam**

Among the 650 domains we found and were able to qualify, close to 45% seems to be mimicking a ticketing selling or reselling platform. For example the following tickets.paris2024[.]biz, paris2024.ticket[.]net, tickets.paris2024[.]app, paris2024[.]app or tickets-paris2024[.]org are typosquatting the **official Paris2024 selling platform hosted at https://tickets.paris2024.org/**.

Of note, we observed a **large bulk of simultaneously registered domains** , the same day and with the same registrar. We assess it is **likely a defensive operation from organisers or national partners,** looking to anticipate typosquatting related to ticket scamming. All domains were lookalike, such as tickets.pa4ris2024[.]org, tickets.paaris2024[.]org, tickets.pabis2024[.]org or tickets.padis2024[.]org and probably were registered with a similar technique to DNSTwist described earlier, in order to block similar but malicious domain registration.

### **French official security organisation**

We observed a significant number of typosquatted domains mimicking French official websites, especially related to the security measures implemented for the opening ceremony. Due to the Seine river parade, the Interior Ministry established restricted areas only accessible with a QR code security pass “Passe Jeux”, with information available for locals and visitors on www.pass-jeux.gouv.fr and anticiperlesjeux.gouv.fr. Both websites, as well as other government-related ones, were concerned by typosquatting malicious domains, for instance:

  * pass-jeux[.]com, pass-jeux[.]fr
  * anticiperlesjeux[.]gauv.fr, 
  * anticiperlesjeux.gouv[.]it 
  * pass-jeux.gouv[.]uk
  * pass-jeux.gouv[.]es
  * pass-jeux.gouuv[.]fr
  * www.sports-gouv.signalement[.]net



We observed in our telemetry some hits among our clients on the domains gouuv[.]fr, on 9th and 10th July 2024, a week before the restricted area set up on 18th July. The mandatory security measures imposed by the government was likely a cause that brought some of our clients to be less cautious about these typosquatted domains.

### **Official Olympics website**

Another approximative quarter of typosquatted domains were related to official International Olympic Committee or to Paris2024 official website, for instance 0lympics[.]com, jo2024[.]club, paris2024[.]date, olymipcs[.]com or www.paris2024[.]it. It is difficult to assess the finality of those domains registration, since these domains have been registered but no service seems to be available when consulting their content (domain parking).

### **Information operation / deception**

In our general assessment of cyber threats on Paris Olympics we published, we assessed it was possible Paris 2024 could suffer from information operations, especially originating from countries currently on bad diplomatic terms with France, namely Russia, Belarus and Azerbaijan. 

So far, no such operation was reported in open source, but we observed the registration of 3**URLs pointing to the same website** , typosquatting Paris 2024 but without the objective of phishing or C2 connection masquerading, but rather **denigrating the event** \- paris2024.lol, jo2024.lol and jop2024.lol. It looks like the website was administered by a politically-motivated individual, opposed to the French government, criticising the social cost of the event.

## **Analysis in our telemetry**

Overall we have observed **very few hits in our telemetry** and most of the hits were not inherently malicious. Many domains are not official ones although not malicious either. We still wanted to put them in the Sekoia CTI to monitor that and follow them in case they were modified during the Olympics to add malicious payload. 

No such thing was observed, some websites actually seem great to use even if non-officials, but we still wonder sometimes how our customers ended up visiting them. For the malicious ones it was through phishing emails every time we had hit and the according logs. Users access typosquatted domains, probably in a hurry to consult a proof or make a last-minute purchase.

## **Conclusion**

Our efforts to hunt and qualify typosquatted domains during the Paris 2024 Olympics provided potential indicators of compromission into the Sekoia SOC plateform. While a significant number of domains aimed at ticketing scams and impersonating official websites were detected, no major hit in our telemetry indicated a possible compromission among our clients. Our findings rather underscore the opportunistic nature of cybercriminals exploiting high-profile events.