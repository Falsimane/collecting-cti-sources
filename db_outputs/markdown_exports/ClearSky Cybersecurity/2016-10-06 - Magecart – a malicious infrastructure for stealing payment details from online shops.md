# Magecart – a malicious infrastructure for stealing payment details from online shops

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/magecart/
- **Date :** 2016-10-06

---

Since March 2016, numerous credit cards and other details have been stolen during payment from dozens of online shops worldwide. Malicious JavaScript code acting as a form grabber or a simple “cloud based” keylogger was injected into breached shops. As buyers filled in their payment details, the data was captured and sent in real time to the attacker.

This means that the information got stolen even if the seller worked according to PCI standards and did not keep credit card details in a database after purchase completion. This method is different than other ways of stealing payment details, such as infecting the buyer’s computer, implanting malware in Point of Sale terminals, or dumping entire databases from breached online shops.

In this post we analyze the malicious code and other parts of the campaign. RiskIQ, who we collaborated with on the investigation, dubbed this campaign **Magecart**. In parallel to this post, they are publishing a [report ](https://www.riskiq.com/blog/labs/magecart-keylogger-injection/)reviewing other parts of the malicious infrastructure and compromised websites.

Security company Sucuri [revealed ](http://labs.sucuri.net/?note=2016-06-30)parts of this campaign back in July 30. Since, the attackers kept registering new domains and used them to host malicious JavaScript files, later injecting them into breached online shops.

### Malicous JavaScript injection in breached shops

In order to implant the malicious JavaScript code, the attackers first had to get access to change the source code of the website. They might have gained this access by exploiting a vulnerability in the web platform (such as Magento Commerce, Powerfront CMS, OpenCar, etc’) or by getting a hold of admin credentials.

Then, the attacker would add a <script> tag, loading JavaScript from one of tens of domains they own.

Below are screenshots of the source code in three different breached websites, showing the injected malicious JavaScript:

[![a](https://www.clearskysec.com/wp-content/uploads/2016/09/a-e1474970933830.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/a.png)

[![ac](https://www.clearskysec.com/wp-content/uploads/2016/09/ac.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/ac.png)

[![av](https://www.clearskysec.com/wp-content/uploads/2016/09/av.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/av.png)

In order to deceive security researches, in some cases visiting the root domain or the IP to which it points would return an empty page redirecting to google.com.

[![c](https://www.clearskysec.com/wp-content/uploads/2016/09/c.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/c.png)

### Valid SSL certificates

The malicious JavaScript code is served over HTTPS with a Valid SSL certificate. Using HTTPS is important for the attacker to keep its malicious activity undetected, because script loaded over HTTP would trigger a “mixed content” warning to the user.

below are some of the certificates used in the campaign:

**js-abuse[.]su**

[![aa](https://www.clearskysec.com/wp-content/uploads/2016/09/aa-1.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/aa-1.png)

Serial : ‎00 94 6e 7c aa 678e de 0c 33 c9 ee 01 d1 ff 36 fd  
Sha1 Thumbprint :63 ff a2 6b b9 45 46 99 00 8f c2 ff 24 38 76 68 cf 3a 8e 93

**cdn-js[.]link**

[![bb](https://www.clearskysec.com/wp-content/uploads/2016/09/bb.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/bb.png)

Serial : ‎ ‎00 b5 ac fc 35 dc db 7b 3b 44 3e e2 61 ba 9d d7 a1  
Sha1 Thumbprint :15 68 f9 67 5b c5 79 db 30 7f 52 01 dc 52 98 36 31 14 9e ef

**statsdot[.]eu**

[![cc](https://www.clearskysec.com/wp-content/uploads/2016/09/cc.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/cc.png)

Serial : ‎ ‎ ‎03 16 90 9f 7a d1 dd c5 2f c3 5c 7a 8c f2 c8 be 40 b0  
Sha1 Thumbprint :‎e6 28 c2 92 8c 4e 01 f5 a0 23 c0 12 52 71 45 b6 c7 25 f5 f7

**stat-sj[.]link**

[![dd](https://www.clearskysec.com/wp-content/uploads/2016/09/dd.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/dd.png)

Serial : ‎ ‎ ‎ 00 bd 60 18 62 e8 30 d6 17 f1 c9 b1 45 76 67 2d f8  
Sha1 Thumbprint :6e 6e 30 78 26 ee 2e 46 56 ad e7 bd 9e c4 71 23 d1 03 61 ac

**js-mod[.]su**

[![ee](https://www.clearskysec.com/wp-content/uploads/2016/09/ee.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/ee.png)

Serial : ‎ ‎ ‎ 00 80 df 54 15 a6 96 99 06 20 86 4a 6b 42 e2 cf 74  
Sha1 Thumbprint :18 e7 aa 7b 44 bc 12 16 c0 25 75 dd 52 25 1e 4c 33 44 ef c9

**sj-mod[.]link**

[![ff](https://www.clearskysec.com/wp-content/uploads/2016/09/ff.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/ff.png)

Serial : ‎ ‎ ‎ ‎73 07 83 4d 3b bf 49 4f 09 48 67 a8 b1 67 66 a2  
Sha1 Thumbprint :46 b9 73 f6 ec dc 44 4c 26 78 51 bb 20 c9 23 a1 d2 42 ff fd

### Credit card stealer functionality

The functionality of the credit card stealer is simple. Key parts are described below.

After data is filled by the buyer in form fields, attributes of the fields are checked against a predefined array. The array is composed of attributes used in the targeted payment platform, for example:

[![1](https://www.clearskysec.com/wp-content/uploads/2016/09/1.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/1.png)

If any of the fields are present, the value of each and every input field in the page is collected into a variable, along with the host (i.e. the web address of the form):

![2](https://www.clearskysec.com/wp-content/uploads/2016/09/2.png)

The collected data is sent via an AJAX PSOT request to a URL in one of the malicious domains the attacker owns.

![3](https://www.clearskysec.com/wp-content/uploads/2016/09/3.png)

Different versions of this basic code are used over the campaign. In some cases, the code is served obfuscated.

### Infrastructure

We used PassiveTotal to pivot off of IPs (such as 80.87.205.145) and Whois details (such as a registrant email – rudneva-y@mail.ua) to find further malicious domains:

[![4](https://www.clearskysec.com/wp-content/uploads/2016/09/4.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/4.png) [![5](https://www.clearskysec.com/wp-content/uploads/2016/09/5.png)](https://www.clearskysec.com/wp-content/uploads/2016/09/5.png)

This resulted in four clusters, sharing properties such as registrant email address and date of registration.

![6](https://www.clearskysec.com/wp-content/uploads/2016/09/6.png)

The full list of malicious domains, compromised eCommerce websites, and other Indicators of compromise can be found at RiskIQ’s post “[Compromised eCommerce Sites Lead to Web-Based Keyloggers](https://www.riskiq.com/blog/labs/magecart-keylogger-injection/)” (A [Hebrew version](https://www.clearskysec.com/wp-content/uploads/2016/11/magecard-חשיפת-תשתית-תקיפה-של-אתרי-מסחר-אלקטרוניים-.pdf) is available).