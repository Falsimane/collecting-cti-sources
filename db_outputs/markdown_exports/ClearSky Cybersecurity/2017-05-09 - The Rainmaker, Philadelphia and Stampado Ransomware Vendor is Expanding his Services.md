# The Rainmaker, Philadelphia and Stampado Ransomware Vendor is Expanding his Services

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/the-rainmaker/
- **Date :** 2017-05-09

---

ClearSky conducts consistent monitoring of various Darknet actors and communities, including specific actors that develop and sell malware, exploits, bots and ransomware.

We have recently encountered very aggressive jabber spam campaign, advertising the “Philadelphia” ransomware.

As Brian Krebs wrote in one of his recent post, Philadelphia is a ransomware-as-a-service crime ware package that is sold for roughly $400 to would-be cyber criminals who dream of carving out their own ransomware empires. Philadelphia has many features, including the ability to generate PDF reports and charts of victims to track the campaigns, as well as the ability to plot victims around the world using Google Maps.[1]

This is a screenshot of the jabber spam campaign:

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/jabber-1.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/jabber-1.png)

In his post from March, Brian Krebs described the highly professional YouTube movie[2] advertising this Ransomware.

In addition to this movie, a professional and well-designed website was created by Philadelphia vendor in February 2017:[![](https://www.clearskysec.com/wp-content/uploads/2017/05/rainmaker.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/rainmaker.png)

This website advertises both the Philadelphia and Stampado Ransomware, but also advertises other services and tools that are provided by the same person:

  1. **_CyanoBinder_** – File Joiner that allows to join multiple files into only one executable file (the price is 14$ for unlimited license)
  2. **_SkypeBomber_** – a tool that conducts phone DDOS, using Skype to call a specific number repeatedly (the price is 29$ for unlimited license)
  3. **_V-Eye_** – a RAT that includes keylogger that collect passwords, and control mouse, watch webcam or desktop, send and retrieve files and more (the price is 239$ for unlimited license).
  4. **_RemoTV_** – an application that bundles and opens a hidden modified TeamViewer application on a machine and sends the credentials to you (the price is 49$ for unlimited license)
  5. **_Mailer_** – PHP script that allows you to send e-mails to multiple addresses at once (the price is 9$ for unlimited license)



In comparison to other vendors in cybercrime markets, the prices are relatively low.

While checking the information of the domain of the “store” in we were able to find traces about other activities of this malware provider that allows us to connect him to Brazil.

The common assumption, till now, was that the vendor that is behind Philadelphia ransomware[3], is Russian cybercriminal. But based on those findings and the fact that the communication language of the vendor, in one of the main Russian cybercrime forums, is **English** , we can assume that the vendor is potentially Brazilian.

In the Diagram below, we have uncovered the connections of the registrants information behind the website :

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/diagram.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/diagram.png)

As we can see in the above diagram and using “Passive Total” with reverse whois search on the registrar e-mail (rubens_alexandre_mar@hotmail.com), during 2016 he registered 4 other domain names, three out of them with the name Viracopos:

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/viracopos.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/viracopos.png)

Viracopos is an international airport in São Paulo, Brazil, which has a legitimate website under the domain viracopos.com. So we can assume that the malware vendor conducted in 2016 some kind of phishing activity connected to the Viracopos airport.

Below is the registration information for the above domain names, as we can see, there was use of legitimate people names:

**Rainer Brust details:**

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/brust.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/brust.png)

**Rita J Kula details:**

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/rita.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/rita.png)

Pivoting the IP on which the main website of the vendor is hosted, we found a mirror website to the main website that was registered in May 2016 and was active till last week:

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/another.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/another.png)

This phone number (as well as the registrant name and e-mail) is connected to a huge network of more than 1000 domains that were registered during 2016 and are unavailable now.

Using the Domain Tools Risk Score engine we can see that with high probability all those domains were malicious:

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/risk-1.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/risk-1.png)

Also checking the registrant mail (rajsingh01114@gmail.com) we see that the 490 abuses that were reported against domain names registered with this e-mails[4] :

[![](https://www.clearskysec.com/wp-content/uploads/2017/05/KNUJ-1.png)](https://www.clearskysec.com/wp-content/uploads/2017/05/KNUJ-1.png)

### **Conclusions**

From this research we can learn the following:

  1. Philadelphia vendor is expanding his activity and investing a lot of efforts in marketing.
  2. This vendor run during 2016 a huge network of malicious websites, and probably conducted specific phishing activity connected to Viracopos airport.
  3. We assume, with high probability, that the malware vendor of Philadelphia is not Russian, we assess with moderate probability that the vendor is Brazilian.



### **Indicators of compromise**

viracopos.me  
viracopos.club  
viracopos.biz  
whitecor.com  
80.82.69.139  
rubens_alexandre_mar@hotmail.com  
rajsingh01114@gmail.com  
918989616042

[1] <https://krebsonsecurity.com/2017/03/ransomware-for-dummies-anyone-can-do-it/>

[2] <https://www.youtube.com/watch?v=5WJ2KHoo5Fo>

[3] <https://blog.vadesecure.com/en/raas-ransomware-as-a-service/>

[4] <http://knujon.com/owners/rajsingh01114@gmail_com.html>