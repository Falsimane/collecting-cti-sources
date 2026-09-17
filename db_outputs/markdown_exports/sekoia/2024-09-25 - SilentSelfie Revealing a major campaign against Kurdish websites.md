# SilentSelfie: Revealing a major campaign against Kurdish websites

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/silentselfie-uncovering-a-major-watering-hole-campaign-against-kurdish-websites
- **Date :** 2024-09-25

---

## **Introduction**

At the beginning of 2024, Sekoia Threat Detection & Research team (TDR) was put in relation with members of the **Kurdish minority** regarding a suspicious script on a legitimate website named **nuceciwan129[.]xyz**. This script, when visited, prompted users to activate their webcams and share their locations, arousing suspicion among some users. After a first investigation, our contacts discovered an obfuscated JavaScript code sending reconnaissance data to a PHP script hosted on the nuceciwan129[.]xyz server.

Following this initial discovery, we began a dedicated investigation to understand the attack chain and identify any other websites compromised by the same script or its variants. During this investigation, **we discovered 25 compromised websites linked to the Kurdish community** with four different variants of the framework found on nuceciwan129[.]xyz. These ranged from the simplest, which merely stole the **user's location** , to more complex ones that recorded images from the **selfie camera** and led selected users **to install a malicious APK** , i.e an application used on Android.

Even though **no sophisticated code was used in this attack** , such as using zero-day exploits to compromise the target's devices, it is worth mentioning **the size and duration of this campaign which makes it unique**. The first observations of compromised websites date back to the end of 2022. Therefore, some websites have been stealing users' locations for **over a year before being noticed**.

Cyber attacks against the Kurdish minority aiming to collect intelligence are common, often attributed to the StrongPity intrusion set in open sources. However, after days of investigation, **we found no links to previous StrongPity campaigns** , and the TTPs (Tactics, Techniques, and Procedures) used in these watering holes and the discovered APK do not match any known intrusion set active in the Middle East. **Therefore, we believe that a previously unknown activity cluster has been discovered**.

## Watering holes analysis

Across the 25 compromised kurdish websites, we identified **four distinct variants of a same script designed to gather intelligence from online visitors**. These scripts ranged from simple ones that exfiltrated the visitors' locations to more complex frameworks that accessed **the selfie camera to take pictures of the user** and redirected a selection of them to **a malicious APK installation web page**.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a8f2_6a92a272a7a0bb1897156ed9_6a2a7e10858397422f50bef6.webp)

It is worth noting that **these variants share multiple modules** , and different versions may have been deployed on the same website over time. For instance, the website **rojnews[.]news** has encountered three variants of these scripts since its initial compromise in December 2022, from the first variant to the fourth variant in November 2023 till today.

### **Variant 1 - Getting the user location**

We found this first variant on seventeen**websites**. The code is quite minimalistic: when the webpage is loaded, its body invokes the gL() (getLocation) method to execute the malicious JavaScript embedded in it. If the User-Agent is an Android or an iPhone, the current location of the user is retrieved - which requires the user's validation - and the location is sent to a PHP script hosted on the compromised website, often located under /wp-includes/ms-menu.php.

![Malicious javascript code related to the first variant namely: get the user's location.
Source: Sekoia's article on the influencer campaign targeting Kurdish community](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a8ef_6a92a271693fca262e1af8ae_6a2a7e10858397422f50bef3.webp)

Malicious javascript code related to the first variant namely: get the user's location.  
Source: Sekoia's article on the influencer campaign targeting Kurdish community  


### **Variant 2 - Adding user tracking via a cookie**

The second variant, found on **ronahi[.]net** , enhances users tracking capabilities by including the screen configuration option and a cookie named sessionIdVal in addition to the user's location. The value of this cookie is generated through a compromised third-party, Kurd-linked website, ronahi[.]video.

When ronahi[.]video/wo_cookie.php is requested by the malicious JavaScript code, the PHP script checks whether the cookie sessionIdVal is present in the client’s HTTP request for domain ronahi[.]video. If not, a random string is generated and stored in a cookie for a duration of one hour; otherwise, it returns the random string present in the cookie. This random string is then received and stored in a cookie associated with the compromised domain for 400 days. Also named sessionIdVal, its value is sent as a token in the HTTP request each time the user transmits their location data to the malicious PHP script hosted on the server, as shown below.

![Malicious javascript code related to the second variant namely: Add user tracking via a cookie.
Source: Sekoia's article on the cyber espionage campaign targeting Kurdish community](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a901_6a92a2742b0ef7af46bc90bb_6a2a7e10858397422f50befd.webp)

Malicious javascript code related to the second variant namely: Add user tracking via a cookie.  
Source: Sekoia's article on the cyber espionage campaign targeting Kurdish community  


From an operator's point of view, it allows to get all the public IP addresses used by a specific user (possibly retrieved via the PHP script receiving the data) and **track their location for 400 days** , which can be a valuable intelligence source. 

However, we can note two possible mistakes from the operators. First, the PHP script wo_cookie.php doesn’t exist on the ronahi[.]video domain. It is likely that the attackers made a typo, in fact the malicious script is wo_cookies.php. Moreover, the duration of one hour of the cookie present to the ronahi[.]video prevents the attackers from tracking the user for a long period across multiple compromised websites, which, we think, was the ultimate goal of resorting to a third-party domain.

### **Variant 3 - Browser configuration, user location, selfie**

The third variant is a more complex reconnaissance script that not only retrieves the user's location, tracking token and public IP address but also gathers various other pieces of information from the current browsing session. Different variants of this script exist; some are directly embedded in the webpage, as it was the case with **lekolin[.]org** and **ciwanensoresger[.]com** , while others are contained in a single JavaScript file and obfuscated with Obfuscator.io, as seen with **nuceciwan129[.]xyz**.

Similar to the first variant, this script is launched using the gL() method, but it now checks for a broader range of devices, including iPhones, iPads, iPods, and Android devices. If the User Agent matches one of these devices, the script first retrieves the local IP address using WebRTC and the current battery status using navigator.getBattery(). It then checks whether the browser is in private mode using the Incognito library. If the browser is not in private mode and if it passes a useless check derived from the current datetime, the script checks for the presence of a cookie named CSESSID.

If the CSESSID cookie is not set, a method named init() is called. This method attempts to retrieve images from the selfie camera using navigator.mediaDevices.getUserMedia and places them in a hidden HTML canvas on the webpage. The CSESSID cookie, with a duration of ten days, is then set. The image present in the canvas is converted to Base64 and sent to a PHP script along with various other information, such as:

  * The current URL;
  * The screen resolution;
  * An MD5 hash of the WebGL configuration;
  * The list of the local IP addresses retrieved from WebRTC;
  * The battery status via navigator.getBattery;
  * The current network related information via navigator.connection (if supported);
  * The current Wifi information via navigator.connection (if supported);
  * Other data from the navigator such as the number of CPUs, TouchPoints, language;
  * The remote IP which is retrieved from ronahi[.]video/wo_cookies.php;
  * The tracking token of the sessionIdVal cookie;



Then, the script gets the GPS location via navigator.geolocation.getCurrentPosition and sends this location along with the same parameters as the request for the image taken from the selfie camera.

![Malicious javascript code related to the third variant namely: get the user's location and retrieve the images from the selfie camera.
Source: Sekoia's article on the cyber espionage campaign targeting Kurdish community](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a8fe_6a92a26f16f788fda8e49d58_6a2a7e0f858397422f50bedb.webp)

Malicious javascript code related to the third variant namely: get the user's location and retrieve the images from the selfie camera.  
Source: Sekoia's article on the cyber espionage campaign targeting Kurdish community  


### **Variant 4 - Browser configuration, user location, user picture, APK installation**

The latest variant, referred to as Variant 4, has only been encountered the news websites **rojnews[.]news** , **hawarnews[.]com** and **targetplatform[.]net.** This variant represents an evolution from the previous codes into a framework where each main functionality is handled by separate modules. It is not launched via a call to the gL() method (which no longer exists) but instead is activated when the JavaScript file is loaded.

![Permissions requested when visiting Rojnews from a smartphone. 
Source: Screenshots extracted during the investigation by the Sekoia.io TDR team on the campaign to compromise Kurdish community](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a904_6a92a276a2f46752fd0115d9_6a2a7e10858397422f50bf00.webp)

Permissions requested when visiting Rojnews from a smartphone.   
Source: Screenshots extracted during the investigation by the Sekoia.io TDR team on the campaign to compromise Kurdish community  


When loaded, the main() method is called. Similar to Variant 2, it checks if the user agent matches an iPad, iPod, iPhone, or Android device and if the browsing session is not in private mode.

Once this check is successful, the script looks for the sessionIdVal cookie. If it is not set, the script creates it with a random string and a duration of 190 days, without requesting ronahi[.]video to create it. Then, several pieces of data are retrieved, such as the local IP address via WebRTC and the battery status. A list of modules to be executed is then established. By default, this list is set to 1110, where each position corresponds to a specific module: 1 indicates that the module should be executed, and 0 indicates that it should not.

Here are the modules that can be executed:

  * **Image module** : Retrieves an image from the selfie camera;
  * **Location module** : Retrieves the current location of the user;
  * **WebRTC module** : Retrieves the local IP addressing by using WebRTC;
  * **APK module** : Redirects the user to a fake APK installation webpage and sends telemetry about it;



Since the last character (0) in the default module list 1110 corresponds to the module that redirects the user to a fake APK installation page, this page can only be accessed by previously selected users.

It is worth noting that the list of modules to be executed can originate from different sources. It can be set via a cookie named modSession or through a URL parameter named uid. Operators aiming to push users to install a malicious APK likely send malicious URLs containing this parameter via internet messaging to their targets or set the modSession cookie through their PHP script.

We were only able to retrieve the fake APK installation page hosted on Rojnews, accessible at hxxps://rojnews[.]news/ku/wp-content/mobile.html. Both **hawarnews[.]com** and **targetplatform[.]net** redirect users to hxxps://targetplatform[.]net/mobile.html, which returned a 404 error during the investigation. The Rojnews APK installation page is straightforward, displaying a screenshot of the Android application. The APK is downloaded when the user clicks on the screenshot or the Google Play icon.

![Malicious Rojnews APK installation webpage. Source: Screenshots extracted during the investigation by the Sekoia.io TDR team on the campaign to compromise Kurdish community](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a8fb_6a92a273dae089660dfc1712_6a2a7e10858397422f50bef9.webp)

Malicious Rojnews APK installation webpage. Source: Screenshots extracted during the investigation by the Sekoia.io TDR team on the campaign to compromise Kurdish community

## RojNews malicious APK analysis

RojNews is a very simple application that only embeds the RojNews website using the Android Webview class. Android Webview is a system component that provides web browser viewing functions within an app. It allows any application to display a web page without having to switch to the device's Internet browser. As you can see below, when opening the application, only the website appears, allowing the user to browse it.

![Malicious RojNews Android application. The technical analysis applied here shows that the installation of the app - which addresses Kurdish news - requires access to contacts, current location, and access to storage.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a8f5_6a92a26e693fca262e1af6ef_6a2a7e0f858397422f50bed8.webp)

Malicious RojNews Android application. The technical analysis applied here shows that the installation of the app - which addresses Kurdish news - requires access to contacts, current location, and access to storage.

However, the code of RojNews, which is obfuscated by using the [ProGuard Java packer](https://github.com/Guardsquare/proguard) contains a malicious class named LocationHelper which is launched as a service and aimed to beacon the current user location to the RojNews webserver and receive commands to execute. By installing it, the user can directly notice with the requested permissions that something is going wrong with the installed app as it requires the access to the contacts, the current location and an access to the storage. Here are the commands supported:

  * 100 - This command is aimed at **retrieving system-related information** , from the device's properties to the installed applications and current network information (active network interface, WiFi BSSID & SSID, IP addressing, etc.).
  * 101 - This command is aimed at **retrieving a list of contacts** from the infected device, including associated properties for each contact.
  * 102 - This command **retrieves the current location** (latitude, longitude, altitude, accuracy) of the device. It is worth mentioning that by default, the device sends the result of this command as a beacon, and it is not implemented as a command to execute.
  * 103 - This command **sends back a list containing the files** and directories present on the local and external storage.
  * 104 - This command (not tested successfully in live environment) allows the operators to **retrieve a file from the local and external storage**. The file is sent back to the operators encoded in Base64.



It is worth noting that this malicious code doesn’t have any persistence mechanism but is only executed when the user opens the RojNews application. Once the user opens the application, and after 10 seconds, the LocationHelper service starts beaconning the background to the URL rojnews[.]news/wp-includes/sitemaps/ via HTTP POST requests, sharing the current location of the user and waiting for commands to execute.

## Hunting for additional infrastructure

The watering holes and the malicious Android application communicate through PHP scripts hosted on compromised web servers. This is a clever tactic by the attacker, as it **prevents network-based detection** and **reduces the likelihood of attribution based on its infrastructure**. Therefore, the infrastructure analysis is pretty weak.

Thanks to our contacts, we got one of the PHP scripts acting as a gateway to the attacker infrastructure. This PHP script, which contains dead code, transfers the received data and additional HTTP headers to an upstream server by using stream_context_create. The data are sent to webmail.onlinearuba[.]net/7b2[redacted]600a/logs.php, a server rented by the attacker hosted under the **AS 36352 (AS-COLOCROSSING)** with the IP address 23.95.14[.]63. This server has a directory named “update” with an HTML file including a script hosted at the URL hxxp://170.75.161[.]102/asd.js. Even though the file just presents a JavaScript alert, it gives us a new server associated with this intrusion set.

By looking at servers sharing similarities with 170.75.161[.]102, we found 24.246.223[.]228 that shares the same Apache version with limited headers - which are shared by four servers on the internet - and the same directory structure as the files /javascript/script/jquery.js and /javascript/script/jquery.min.js which are present on both servers. Even if this link is quite discriminant, **we consider it as weak**.

## Victimology analysis

Over the investigation, we quickly noticed that all the compromised websites we identified were **directly linked to the Kurdish community** , especially to the Kurdish-led de facto **Rojava authority** in North-East Syria, but also in Iraq and in Turkey. To better understand motivations for potential intelligence gathering through cyber espionage, it is useful to assess the political context of the Kurdish situation in Syria and the region.

### Political context of the Kurdish situation in Syria and Middle-East

Kurdish people are an ethnic group in the Middle East spread over a territory of more than 500,000 km2 spanning four countries: Turkey (about 18 million Kurdish inhabitants), Iran (8 million), Iraq (7 million), and Syria (2 million). They have a significant diaspora, primarily in Europe, with over 650,000 Kurds in Germany.

In Syria, in the context of the Syrian Civil War, the Kurdish party PYD, among other forces, established an Autonomous Administration of North and East Syria, also known as Rojava administration. The territorial control of Rojava was established by the YPG - the armed force affiliated with the PYD - which actively contributed to the defeat of the Islamic State organisation in Syria with the US-led international coalition. The relationship between the Syrian state and the Kurdish authority in Rojava is complex, characterised by successive periods of cooperation and conflict, as both sides deal with issues of autonomy, territorial control, and fight against common enemies and adversaries.

Turkey sees the Rojava administration as an extension of the PKK (Kurdistan Workers' Party), a Kurdish militant and political group engaged in an armed struggle with Turkey for Kurdish autonomy and rights since 1984. Thus, Ankara considers both the PYD and YPG forces as terrorist organizations and as a threat to national security due to the shared border between Turkey and Rojava, resulting in military interventions and ongoing tensions. Turkey's operations in Northern Syria, including Euphrates Shield (2016), Olive Branch (2018), and Peace Spring (2019), aimed to eliminate Kurdish forces and create a buffer zone.

In North-Eastern Iraq, the Kurdish region is ruled by a semi-autonomous Kurdish government within the Iraqi state (Kurdistan Regional Government, KRG). The main political force inside the KRG is opposed to the PKK/Rojava and is often reported as collaborating with Turkey over security affairs.

![Map by Pr. Tigrane Yegavian, Schiller International University
https://www.linkedin.com/in/tigrane-yegavian-18828641/?originalSubdomain=fr](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5a33e6167cebbf7a8f8_6a92a270a7a0bb1897156e3b_6a2a7e0f858397422f50bede.webp)

Map by Pr. Tigrane Yegavian, Schiller International University  
https://www.linkedin.com/in/tigrane-yegavian-18828641/?originalSubdomain=fr  


 _Map published in the the French-speaking article_[ _"Le Rojava, une oasis au sein du chaos"_](https://www.scienceshumaines.com/le-rojava-une-oasis-au-sein-du-chaos_fr_44017.html)_  
by Pr._[_Tigrane Yegavian_](https://www.linkedin.com/in/tigrane-yegavian-18828641/?originalSubdomain=fr) _, Sciences Humaines  
_

### Waterholed websites categorisation

Among the**21 kurdish websites compromised by waterholes** , we can categorise them into different types.

The first group is related to **Kurdish press and media** mainly based in North East Syria. This territory is ruled **de facto** by the Rojava administration. Compromised websites include local radio stations based in cities along the Syrian-Turkish border such as **Orkes FM** , **Dirbesiye FM** or **Star FM** , as well as official websites from the **Union of Free Media** \- Rojava’s de facto Ministry of Information - and one relative to **SDF Press**. Among those compromised websites, one is not based in Syria but in Iraq (Erbil), the **RojNews** agency (see analysis below).

The second group is websites related to the **Rojava administration and its armed forces** (YPG). Among them **YPG Rojava** , **Sehiden Rojava** (martyrs of Rojava, fallen YPG fighters), or the **Initiative for Afrin** (founded in Germany in August 2021, aiming to expose and address violations committed by Turkey and its affiliated armed groups in Afrin region of Syria since 2018). In addition, we could add to this group all compromised websites related to political parties or organisations supporting or linked to Rojava, such as **Peoples' United Revolutionary Movement** (HBDH), **Star Union of Women** (Kongra Star) or the **Movement for a Democratic Society** (TED-DEM), ypj-off.

The last group is related to **revolutionary far-left political parties** and organisations in Turkey and Kurdish regions, including those **linked to the PKK**. We were able to identify waterholed website from the **Party of Free Women in Kurdistan** (PAJK, linked to PKK), the **People's Liberation Party-Front of Turkey** (DHKP-C, classed as terrorist by Turkey, the US and the EU) and the **Halkın Devrimci Güçleri** (a group linked to DHKP-C).

#### The RojNews case study

RojNews is a **Kurdish news agency based in Erbil** , the capital of the Kurdistan Regional Government (KRG) of Iraq. RojNews publishes in Arabic, Kurdish and Turkish languages.

As described in the technical analysis above, the official website rojnews[.]news is compromised by what we called a type-4 waterhole. When a previously selected user visits the website, he is prompted to install the 'official' app, which is actually **a malicious android application** that can get the victim phone contacts, GPS coordinates, network configuration etc.

Our analysis made us assess that the RojNews website was compromised at least from December 2022. In October 2023, **RojNews reported the arrest of Silêman Ehmed, the Editor-in-chief from their Arabic section** , by KDP forces (the Kurdish main political force of the Kurdish Regional Government of Iraq). He was detained while returning to Sulaymaniyah from North East Syria (Rojava). This fact led us consider KDP forces as one of the attribution hypothesis (see below).<

### Attribution hypothesis of the cyber espionage campaign targeting the Kurdish websites

#### **Turkey**

The first attribution hypothesis we considered is a cyber espionage campaign conducted by **Turkish intelligence services**. For Ankara, there is no difference between the compromised websites (North-East Syria Kurdish medias, Rojava administration / YPG and far-left revolutionary parties PJAK or DHKP-C) : **all are considered as entities linked to PKK** and its armed secession fight against Turkey, thus viewed**as national security threats**.

As already mentioned, Ankara has already conducted 3 military operations in Syria targeting Kurdish forces from Rojava. Thus, this waterhole campaign would likely be conducted to gather actionable information (GPS coordinates location, and sometimes “selfie” picture and extended information) on individuals considered as involved in terrorist activities according to Turkish intelligence.

**However, we did not find any technical elements** or TTPs allowing us to link this operation to any open-source documented Turkey-nexus intrusion set such as StrongPity or Sea Turtle.

#### **Syria**

A second, yet less likely, attribution hypothesis would be the **Syrian intelligence services**. Now stabilised after years of uncertainty during the Syrian Civil War, the Syrian government is trying to regain territorial control of its full territory, including North-East Syria **de facto** ruled by the Rojava Kurdish administration. Although not in open confrontation with Rojava, the Syrian services might be interested in gathering intelligence on the activities of the armed forces of Rojava.

But that hypothesis would **not explain the compromise of some websites** , such as those **related to DHKP-C** , a left-wing revolutionary organisation active only in Turkey.

#### **Kurdistan Regional Government (Iraq)**

This attribution hypothesis, we assess a realistic possibility, is based on the opposition between Kurdish KRG (especially from KDP party) and Kurdish Rojava / PYD. According to many sources, the Kurdistan Regional Government of Iraq [collaborates with Turkish intelligence](https://www.washingtoninstitute.org/policy-analysis/turkeys-anti-pkk-operation-and-development-road-iraq-are-two-sides-same-coin) to collect and exchange information about PKK or Rojava forces. Moreover, the arrest of a journalist from RojNews, one of the compromised websites, by KDP forces raises questions about a possible link to the compromised website (over the same period), especially on the malicious RojNews app able to exfiltrate GPS coordinates from the victim.

Although no known intrusion set is linked to the Kurdistan Regional Government, **it is not impossible that the operation could be conducted by the KRG** , given the relatively moderate sophistication. Off note, the RojNews journalist arrest may also be part of intelligence exchange between Turkey and GRK.

#### **Other less likely hypotheses**

**Iran's** relationship with its Kurdish minority is characterised by significant government surveillance and repression to quell separatist movements and maintain control. Thus Iranian intelligence service, known to conduct cyber offensive and espionage operations, may have interests into gathering information on RojNews agency which publishes articles including on Iranian Kurdistan. Moreover, Iran is a strong supporter of the Syrian regime, which aims to regain control over Rojava territories. **We found no technical link to the Iran-nexus intrusion sets** we follow.

**Russia** is also a strong supporter of the Syrian regime and may have interests in collecting intelligence on Kurdish forces allied - or partner - to Western forces (US-led coalition against ISIS). **We found no technical link to the Russia-nexus intrusion sets** we follow.

## Conclusion

Even though this watering hole campaign is of low sophistication, it is notable for **the number of kurdish websites affected and its duration**. It went unnoticed for over a year and a half despite multiple notifications to visitors of the infected sites, urging them to share their location or access their front-facing camera.

Although Middle-East intelligence services are often suspected of cyber attacks against the Kurdish community, **we have not discovered any connections between this campaign and any known intrusion sets**. The campaign's low level of sophistication suggests it might be the work of an uncovered threat actor with limited capabilities and relatively **new to the field**.

## Indicators of compromise

**Compromised kurdish websites**

`orkesfm[.]com  
yra-ufm[.]com  
zindi24[.]com  
star-fm[.]net  
ypjrojava[.]net  
hbdh[.]info  
dirbesiye[.]fm  
leftkup[.]com  
ypj-office[.]com  
sehidenrojava[.]com  
init4afrin[.]org  
sdf-press[.]com  
lekolin[.]org  
ronahi[.]net  
pajk[.]org  
thkp-c[.]org  
halkin-dg[.]com  
kongra-star[.]org  
rojnews[.]news  
ciwanensoresger[.]com  
tev-dem[.]com  
nuceciwan129[.]xyz  
targetplatform[.]net  
hawarnews[.]com  
dicle[.]fm  
ronahi[.]video (no watering hole)  
`

**Infrastructure**

`webmail.onlinearuba[.]net  
23.95.14[.]63  
170.75.161[.]102  
24.246.223[.]228 (low confidence)  
`

**Rojnews APK hashes**

`7ff9e87f8c8ea10e6aa688c491c81283  
6c75d5f31fe386a1ec94b85cfb7f873b2e100062  
2d75110d4c227c59b9c8fb02cc54b99d0b41e33a2fe1ad50e2fdf0cfb1e701d5  
`

**Yara rules**

`rule apt_SilentSelfie_Rojnews_application_apk {  
meta:  
id = "8d9036f6-2603-4d8d-a33d-ecae0c0b1cd2"  
version = "1.0"  
description = "Detects malicious RojNews application"  
source = "Sekoia.io"  
creation_date = "2024-05-21"  
classification = "TLP:WHITE"  
strings:  
$ = { 00 05 4D 6F 64 65 6C 00 }  
$ = { 03 31 30 31 00 03 31 30 32 00 03 31 30 33 00 03 31 30 34 00 }  
$ = { 09 61 6E 64 72 6F 69 64 49 44 00 }  
$ = { 0A 61 6E 64 72 6F 69 64 5F 69 64 00 }  
$ = { 08 50 6F 73 74 44 61 74 65 00 }  
$ = { 0B 4E 65 74 77 6F 72 6B 49 6E 66 6F 00 }  
$ = { 0F 61 70 70 5F 70 61 63 6B 61 67 65 6E 61 6D 65 00 }  
$ = { 0F 61 70 70 5F 75 70 64 61 74 65 5F 64 61 74 65 00 }  
$ = { 15 6E 65 74 77 6F 72 6B 5F 6F 70 65 72 61 74 6F 72 5F 6E 61 6D 65 00 }  
condition:  
uint32be(0) == 0x6465780A and  
filesize < 3MB and  
8 of them  
}  
  
rule apt_SilentSelfie_WateringHole_compromised_html_body {  
meta:  
id = "ef1095e9-faa2-4fcb-bbc8-c7c98c4d86e0"  
version = "1.0"  
source = "Sekoia.io"  
creation_date = "2024-05-21"  
classification = "TLP:WHITE"  
strings:  
$s1 = "body" nocase  
$s2 = "gL()"  
condition:  
$s1 in (@s2-60..@s2)  
}  
  
rule apt_SilentSelfie_WateringHole_variant_one {  
meta:  
id = "d9b1427e-241d-4beb-8bb8-582116b2a4db"  
version = "1.0"  
source = "Sekoia.io"  
creation_date = "2024-05-21"  
classification = "TLP:WHITE"  
strings:  
$s0 = "navigator.userAgent.match("  
$s1 = ".php?';"  
$s2 = "params = 'log="  
$s3 = "+ ',' +"  
condition:  
$s1 in (@s0..@s2) and  
$s2 in (@s1..@s3)  
}  
  
rule apt_SilentSelfie_WateringHole_variant_two {  
meta:  
id = "ab5af795-808f-42b7-ba09-a910263855b5"  
version = "1.0"  
source = "Sekoia.io"  
creation_date = "2024-05-21"  
classification = "TLP:WHITE"  
strings:  
$ = "sC()"  
$ = "checkC"  
$ = "sessionIdVal"  
$ = "function sP("  
$ = "x.readyState===x.DONE&&200"  
condition:  
all of them  
}  
  
rule apt_SilentSelfie_WateringHole_variant_three {  
meta:  
id = "af264e75-73e8-4623-8565-f84fe4e91cbe"  
version = "1.0"  
source = "Sekoia.io"  
creation_date = "2024-05-21"  
classification = "TLP:WHITE"  
strings:  
$ = "hex_hmac_md5"  
$ = "facingMode"  
$ = "getWebRTC"  
$ = "sessionIdVal"  
$ = "function gL()"  
condition:  
all of them and filesize < 100KB  
}  
  
rule apt_SilentSelfie_WateringHole_variant_four {  
meta:  
id = "2d4f7ff1-35ed-4c3c-82f0-e169bd29e719"  
version = "1.0"  
source = "Sekoia.io"  
creation_date = "2024-05-21"  
classification = "TLP:WHITE"  
strings:  
$ = "checkRules("  
$ = "getModuleList("  
$ = "globalUAData"  
$ = "binl2rstr"  
$ = "sessionIdVal"  
$ = "&webrtc="  
$ = "handleSuccess"  
$ = "&referer="  
condition:  
all of them and filesize < 50KB  
}  
  
rule apt_SilentSelfie_WateringHole_php_gateway {  
meta:  
id = "5c4bc7c1-1512-4703-a407-f0dbc7f11d26"  
version = "1.0"  
source = "Sekoia.io"  
creation_date = "2024-05-21"  
classification = "TLP:WHITE"  
strings:  
$ = "sysOther" fullword  
$ = "sendRequest"  
$ = "base64_decode"  
$ = "otherHeader" fullword  
$ = "webrtc" fullword  
$ = "php://input"  
$ = "battery" fullword  
$ = "webgl" fullword  
condition:  
uint32be(0) == 0x3c3f7068 and  
filesize < 9KB and  
6 of them  
}  
`