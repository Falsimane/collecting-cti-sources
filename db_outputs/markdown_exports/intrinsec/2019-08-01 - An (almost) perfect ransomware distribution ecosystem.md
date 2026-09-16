# An (almost) perfect ransomware distribution ecosystem

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/ransomware-wordpress/
- **Date :** 2019-08-01

---

[et_pb_section fb_built= »1″ _builder_version= »3.26.5″][et_pb_row _builder_version= »3.26.5″][et_pb_column type= »4_4″ _builder_version= »3.26.5″][et_pb_text _builder_version= »3.26.5″]

[Intrinsic CERT](https://www.intrinsec.com/en/cert-intrinsec/) **have faced many ransomware attacks this year** , many interesting techniques were spotted when responding to these attacks including the uniqueness of samples, the use of advanced offensive tools and frameworks (ex. _Cobalt Strike)_ , the use of powerful botnets with brute forcing capabilities (ex. _GoldBrute_) etc.

While many researchers and security vendors have dissected these ransomware samples and came out with great papers and articles explaining the TTPs of the attackers, their motivations and how they get into victim systems; CERT Intrinsec didn't spot any deep dive in Watering holes—like techniques used for ransomware distribution and targeting (un)specific victims.

The distribution technique that we are going to expose, even if it targets a given population, does not fit in targeted attacks behind any motivations. **Threat actors, whom we are going to speak about target (un)specific users needing some type of documents, mostly French documents models or templates**.

## **Distribution Infrastructure**

The most remarkable part of these attacks is the infrastructure used to distribute and deliver their malicious samples, which consisted mainly of hacked WordPress legitimate websites. **Malware distributed actively during this campaign was GandCrab** , on its version 5.x.

While we started tracking websites that threat actors were manipulating by adding malicious links to download ransomware samples, we spotted many redirection techniques when visiting the compromised pages or links.

The page below represents an example of malicious content spotted ITW, which was present on a government website of Ministry of Finance:

[/et_pb_text][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/07/1-2.png" align="center" _builder_version="3.26.5" width="66%"][/et_pb_image][et_pb_text _builder_version="3.26.5"]

_Malicious page on compromised website recovered from [Google cache](http://web.archive.org/web/20190730082638/http:/webcache.googleusercontent.com/search?q=cache:tdaIAkNgH5IJ:finance.gov.ms/%3Fp%3D7805+&cd=1&hl=fr&ct=clnk&gl=fr)_

The content added to this Montserrat government website was surprisingly in French (attribution indicator?), **and many malicious URLs were embedded in the post that are maybe an indicator of SEO for malicious content distribution** :

[/et_pb_text][et_pb_text _builder_version= »3.26.5″ border_width_all= »2px » custom_margin= »|-2px||0px|false|false » custom_padding= »22px|0px|22px|12px|false|false »]

**hxxp://www[.]itls[.]tech/wordpress/?p=5995**

**hxxp://www[.]eips[.]nl/index[.]php?p=3798**

**hxxp://dmuller[.]net/wp/?p=5643**

**hxxp://ereadcost[.]eu/exemples-de-phrases-de-transition-dissertation/**

**hxxp://mhpc[.]cz/exemple-de-lettre-de-dommage-et-interet/**

**hxxp://taylorboger[.]com/wordpress/?p=5345**

**hxxp://www[.]koob[.]com[.]sa/exemple-de-diaporama-pour-le-parcours-avenir/**

**hxxp://www[.]bettingtopplista[.]se/exemple-de-la-fonction-si/**

**hxxp://podestakada[.]pl/?p=5174**

**hxxp://ashdeetech[.]com/wp/2018/12/14/exemple-cas-pratique-controle-de-gestion/**

[/et_pb_text][et_pb_text _builder_version= »3.26.5″ custom_padding= »14px||||| »]

The majority of these URLs were pointing, as discussed before, to document models and templates hosted on other websites. Pivoting on the first spotted URL, **with a simple Google dork, we got the following results** :

[/et_pb_text][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/08/2.png" _builder_version="3.26.6" align="center"][/et_pb_image][et_pb_text _builder_version="3.26.5"]

_Google Dork search_

## **The two-faced webpage**

While navigating to the first URL, visiting the same webpage twice resulted in two different views, we were thinking of **a traffic redirection system** (most commonly used by Exploit Kits) and it was almost the case.

[/et_pb_text][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/07/3-2.png" align="center" _builder_version="3.26.5" width="87.4%" min_height="436px" custom_margin="|62px||61px||" custom_padding="0px|1px|0px|0px||"][/et_pb_image][et_pb_text _builder_version="3.26.5"]

_The first time visiting the webpage_

When navigating to the webpage for the first time, a**fake forum page** where a small conversation is simulated (or faked) where the threat actor pretends to be the admin and link a download to the (malicious) document's model. Look at the page above and remember it since we are going to find exactly the same template on many other compromised websites.

[/et_pb_text][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/08/CaptureD.png" align="center"_builder_version="3.26.6" width="88%"][/et_pb_image][et_pb_text _builder_version="3.26.5"]

_The second time visiting the webpage_

Going back and refreshing the webpage, the fake forum page disappears and only a post shows to visitors. However, **how come that the page disappears?** The redirection system resulted because of a**JavaScript element** that we recovered from the website:

[/et_pb_text][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/07/JS.png" align="center" _builder_version="3.26.5" width="85%"]

Threat actors were inviting the users to download the document from this URL, which seemed, after a quick investigation, that it is another**compromised WordPress website**.

[/et_pb_text][et_pb_text _builder_version= »3.26.5″ border_width_all= »2px » custom_padding= »10px||10px|15px|false|false »]

**hxxp://www[.]zwoelfistei-haexe[.]ch/file[.]php bqkytcptqvmkl=476b7051524b43796e2f5063335a704d65496857545477462 b7451384b6e3168754a56676e386a384b495842763763396938427933436e30**

[/et_pb_text][et_pb_text _builder_version=»3.26.5″]

## ****

## ****

## ****

## **Pivoting**

Pivoting using the **same technique (Google dorks)** , we found hundreds of many other compromised websites pointing to each other or hosting the fake forum webpage. Here are two screenshots taken from random compromised WordPress websites:

[/et_pb_text][/et_pb_column][/et_pb_row][/et_pb_section][et_pb_section fb_built="1" _builder_version="3.26.5"][et_pb_row column_structure="1_2,1_2" _builder_version="3.26.5" custom_margin="-1px|auto||auto||"][et_pb_column type="1_2" _builder_version="3.26.5"][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/07/5-1.png" _builder_version="3.26.5"][/et_pb_image][/et_pb_column][et_pb_column type="1_2" _builder_version="3.26.5"][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/07/6.png" _builder_version="3.26.5"][/et_pb_image][/et_pb_column][/et_pb_row][/et_pb_section][et_pb_section fb_built="1" _builder_version="3.26.5"][et_pb_row _builder_version="3.26.5"][et_pb_column type="4_4" _builder_version="3.26.5"][et_pb_text _builder_version="3.26.5"]

As discussed above,**threat actors are using the same template** (JavaScript displayed above) and are **just changing documents' names and URLs pointing to the content** (or payload) download links that are hosted on other compromised WordPress websites.

The downloaded content or the distributed payload was**a zip file including a multi-technology malware** (JS launching a PowerShell dropper which decompress, load and execute a .NET DLL in memory). We will not dig into that payload since the main subject of this post aims to explain the distribution method and the attackers' infrastructure.

Although we didn't find any posts explaining or describing this distribution ecosystem, we think that we are not the only ones who have faced this threat.**Tea _Total Virus_ [Graph ](https://www.virustotal.com/graph/g99aea3bd0748489fbfa776feed9bbeb85eece989b03e4abba0fe218ebd9d7ac8)bellow was found while investigating on some compromised URLs**, the owner of this graph is unknown, but content distributed by this compromised WordPress (rickrockwell[.]net) is, as you can see, **GandCrab Ransowmare.**

[/et_pb_text][et_pb_image src="https://www.intrinsec.com/wp-content/uploads/2019/07/7.png" align="center" _builder_version="3.26.5"][/et_pb_image][et_pb_text _builder_version="3.26.5"]

## ****

****

## ****

## **Final thoughts**

Content analyzed during OSINT makes us believe that this campaign is **targeting French speakers only**. This technique of distribution, even if it is not advanced, **perfectly and may contaminates works both enterprise environments** (HR, Finance, etc.) and individuals who are often looking for documents' models and templates.

**Tracking this type of campaigns is hard to automate** , since Google dorks would be limited with captchas and since scanning every single page of a WordPress is not feasible. If you have any ideas that you would like to share, do not hesitate to get in touch with us.

**Securing and monitoring your websites today is necessary** ; threat actors are actively seeking vulnerable and unsecured websites to use them as part of their ransomware delivery infrastructure.

**If you think that your employees could be potential victims of this threat, you should also start thinking of and implementing awareness training and sessions (phishing simulations, awareness campaigns, etc.).**

Here is **a Yara rue to add to your security tools or to use to scan your WordPress** instances if you are running threat hunting programs or compromised assessments engagements.

[/et_pb_text]

**rule Compromised_WP {******

**meta:******

**author = «CERT Intrinsec»******

**description = «Detect malicious fake forum pages used for ransomware distribution»******

**date = "2019-07-26"«******

**reference = «https://www.intrinsec.com/blog/ransomware-wordpress»******

**strings:******

**$s1 = «document.all[i].tagName»******

**$s2 = «Super Moderator»******

**$s3 = «removeChild(elem); »****$s4 = " remove(elem) "«******

**$s5 = "Here is a link to"«******

**condition:******

**all of them**

**}**

[/et_pb_text][/et_pb_column][/et_pb_row][/et_pb_section]

#### Articles by category 

Select a category News Vulnerability notice Analysis Report CERT SSI Council Cyber Threat Intelligence Engineering Safety Assessment Event Partnership Research and Development Red Teaming part-time CISO Soc as a Service SOC Operational Security Testimonials Penetration test Threat Intelligence Report Security Watch