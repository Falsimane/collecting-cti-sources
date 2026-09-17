# Unveiling of a large resilient infrastructure distributing information stealers

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/unveiling-of-a-large-resilient-infrastructure-distributing-information-stealers
- **Date :** 2023-01-06

---

## Context

Information stealer (or infostealer) is a malware family designed to gather and exfiltrate sensitive information from the infected host. This threat became widespread over the past few years, and is increasingly distributed by multiple threat actors from the cybercrime ecosystem. The **distribution methods used to spread stealers** are varied, ranging from malspam to fake installers. As observed by SEKOIA.IO, most **infection chains leverage social engineering techniques** to lure victims into downloading and executing the [malicious](/blog/clearfake-a-newcomer-to-the-fake-updates-threats-landscape) payloads.

A **common scheme to trick the victim** is a tutorial that demonstrates how to install a **cracked software** , which turns out to be an information stealer. For the distribution method, the victim enters a malicious website either promoted through a **Google Ad** , or [**SEO poisoned** (Search Engine Optimization)](/glossary/seo-poisoning), or **shared in a legitimate community space**. To assist the victim in compromising its system, the tutorial often describes step-by-step how to disable the antivirus software, download the fake installer and run it.

SEKOIA.IO analysts **unveiled a large and resilient infrastructure** used to **distribute Raccoon and Vidar stealers** , likely since early 2020. The associated infection chain, leveraging this infrastructure of over **250 domains** , uses about a hundred of fake cracked software catalogue websites that redirect to several links before downloading the payload hosted on file share platforms, such as GitHub. This blogpost aims at presenting the current infection chain, payloads and the whole infrastructure tracked by SEKOIA.IO. We will contact the services abused by [the intrusion](/blog/aridviper-an-intrusion-set-allegedly-associated-with-hamas) set to forward the domain names and accounts used for malicious activities. 

## Infection chain leveraging fake cracked software

This part details the steps of an observed infection chain leveraging fake cracked software to distribute Raccoon and Vidar stealers. Following parts describe the final payloads distributed by the intrusion set, and unveil each stage of the infrastructure and how to track it.  
This report focuses on **one cluster that shares similarities on redirect links, domain registrar and final payload hosting**.

At the time of writing it is not clear to whom this infrastructure could be associated to. SEKOIA.IO analysts assess it is plausible this infrastructure is operated by a threat actor running a Traffic Distribution System (TDS), whose clients pay for the service to distribute their stealer builds. It is also likely this infrastructure is operated by an intrusion set distributing its own stealer builds.

Regardless, SEKOIA.IO analysts assess this **cluster is almost certainly operated by a single intrusion set**.

The infection consists in the following steps:

### Step 1 - Search engine displaying SEO poisoned websites

A basic search to find cracked software yields several malicious websites, as shown below.

![Search results for "download free cracked software" on Google.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a629a2f46752fd0361a6_6a92a3ca2e47a1e9fe0e5102_6a2a7b74009bb67f3ecddef7.webp)

Figure 1. Search results for &quot;download free cracked software&quot; on Google.

Searching for Adobe Photoshop paid software, a user is served the following SEO-poisoned webpage: “hxxps://crackist[.]com/adobe-photoshop-free/”.

![Webpage with instructions for downloading and installing the fake software \(SEKOIA.IO\).](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a629a2f46752fd0361a9_6a92a3c8692919148899e62f_6a2a7b74009bb67f3ecddef4.webp)

Figure 2. Webpage with instructions for downloading and installing the fake software (SEKOIA.IO).

This webpage contains information on the legitimate Adobe Photoshop software, increasing the capability to gain the trust of potential victims. It also contains dozens of URLs redirecting to other pages of this website, as well as to the legitimate Adobe website or other platforms, including YouTube. This contributes to improving the website indexing in search engines (SEO poisoning technique).  
The content of the webpages ends with a tutorial demonstrating how to install the cracked version of the software, and several download buttons redirecting the user to step 2.

### Step 2 - Redirection links disguising the malicious payload

Once the user clicks one of the download buttons, a new window opens in its browser and several HTTP/HTTPS communications follow until another webpage appears with further instructions.

The URL redirection chain is as described below. It is worth noting that looking at the URLs’ pattern allows us to track all other related domains (see part “Tracking the whole infrastructure”).

  1. A first URL containing several query parameters, including the title of the previous webpage, whose exact path is “/”:  
`hxxps://primrvils[.]click/?open=df3c9be1966401335aa7bec56362&d=1&x=183&close=f66f157fc6afa&p=Adobe%20Photoshop%20Crack%202022%20V23.1.1.202%20Full%20Version`
  2. A second similar URL with other query fields, whose exact path is, again “/”:  
`hxxp://162.243.164[.]175/?63a07a011f989=544d893fa927d23b4e6d0f0615d422be&63a07a011f992=183&63a07a011f994=1_adobe-photoshop-crack-2022-v23-1-1-202-full-version&gkss=178522&63a07a011f998=1`
  3. A third URL on another domain name:  
`hxxps://offsebike[.]cyou/?5da11e4c71470ca6198ad7c9a0ed05dd=83b9a10f0c2629348a2e3ef5e913400ea3e97b40&med=119801&src=63a07a02550ed`
  4. A fourth URL using href[.]li, which is an internal referral redirect:  
`hxxps://href[.]li/?hxxps://offsebike[.]cyou/?sandy=6518ca1b440a9f0afd64581b41f2fee10f9eaff6&63a07a064bd0e=605e5d3bbc94d53abe30c84684fe15cc`
  5. The final URL from this redirection chain:  
`hxxps://offsebike[.]cyou/?sandy=6518ca1b440a9f0afd64581b41f2fee10f9eaff6&63a07a064bd0e=605e5d3bbc94d53abe30c84684fe15cc`



At this stage, the last URL displays a webpage containing instructions, a Cuttly shortened link (hxxps://cutt[.]ly/u0PdXuo) and a password. The shortened URL is not clickable, as the HTML code storing the link uses the class “form_class”, which is normally intended to submit data.

![Webpage containing the Cuttly shortened download link and the password \(SEKOIA.IO\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a629a2f46752fd0361ac_6a92a3c7dc3071123832d243_6a2a7b74009bb67f3ecdded3.webp)

Figure 3. Webpage containing the Cuttly shortened download link and the password (SEKOIA.IO)

SEKOIA.IO assess the whole redirection chain is likely used to harden the analysis, avoid detection and make the infrastructure stealth, for the following reasons:

  * Using several redirections complicates automated analysis by security solutions, and can be used to filter webclients based on their HTTP fingerprint and geolocation;
  * Getting the malicious payloads requires much hopping, and a human action. These hops hinder automatic collection of the payloads from the SEO-poisoned website;
  * Carving the infrastructure as such is almost certainly designed to ensure resilience, making it easier and quicker to update or change a step, for instance in the case of a temporary malfunction or dismantlement of part of this infrastructure. Additionally, we observed that each stage has multiple instances (domains, or IP addresses) that change regularly.



Moreover, creating additional steps between the initial webpage and the malicious payload allows the operator to maintain a good reputation in the website leveraging SEO poisoning, and prevent its infrastructure from being discovered.

### Step 3 - Final payload hosted on GitHub

Browsing the Cuttly redirects the user to the download page of an archive, hosted on the legitimate file sharing platform GitHub:  
`hxxps://raw.githubusercontent[.]com/davids1a/soulmate/main/NewInstaller_1234_FullVersion_B4.rar`

The victim downloads it, decompresses the archive with the password “1234” (or “2022” in more recent infection chains) and executes the PE file, named “Setup.exe” in most cases. In the analysed infection chain, the payload embeds [Raccoon Stealer](https://blog.sekoia.io/raccoon-stealer-v2-part-1-the-return-of-the-dead/).

Based on the pattern used by the intrusion set to name the archive hosted on GitHub, SEKOIA.IO analysts were able to find a dozen of accounts used to store the malicious payloads.

## Malware distributed by this stealth infrastructure

SEKOIA.IO collected over 120 samples distributed by this infection chain, which all correspond to samples of Raccoon or [Vidar stealer](https://blog.sekoia.io/stealc-a-copycat-of-vidar-and-raccoon-infostealers-gaining-in-popularity-part-1/), from 6 unique botnets. Most of the password-protected archives are hosted on GitHub, on over a dozen accounts.

## GitHub accounts abused to host malicious payloads

All downloaded files are RAR archives and share similarities in their naming convention, which includes:

  * Password “1234” (or “2022” more recently) in the file name;
  * Keywords, such as _Application_ , _Complete_ ,_File_ , _Release_ , _Version_ ;
  * Underscores between keywords and passwords;
  * Random alphanumeric characters, often put at the end of the file name, as a unique identifier;
  * Upper case letter at the beginning of words.



Here are some examples of password-protected archive file names:

`hxxps://github[.]com/ppsinstall  
hxxps://github[.]com/Mughalshughal (banned at time of writing)  
hxxps://github[.]com/Jonybba (banned at time of writing) hxxps://github[.]com/GoldenMa-Re  
hxxps://github[.]com/dljack  
hxxps://github[.]com/Hashmi1211  
hxxps://github[.]com/davids1a  
hxxps://github[.]com/mega1211  
hxxps://github[.]com/moonh1211 (banned at time of writing)  
hxxps://github[.]com/shoby149 (banned at time of writing)  
hxxps://github[.]com/dodlosi  
hxxps://github[.]com/megajackson  
hxxps://github[.]com/chillqueem  
hxxps://github[.]com/maxiwel123  
hxxps://github[.]com/gilisoftt (banned at time of writing)  
hxxps://github[.]com/primaryy1 (banned at time of writing)  
hxxps://github[.]com/moonshon (banned at time of writing)  
hxxps://github[.]com/msdon1211  
hxxps://github[.]com/max1t7 (banned at time of writing)  
hxxps://github[.]com/leojack1211 (banned at time of writing)  
hxxps://github[.]com/naomibrown178 (banned at time of writing)`

More than a hundred files were committed on these accounts between 24, November and 20, December, 2022, as shown in the following figure.

![Activity on GitHub accounts hosting malicious payloads, on December 20, 2022 \(SEKOIA.IO\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62aa2f46752fd0361b9_6a92a3ccdae089660dfcde66_6a2a7b74009bb67f3ecddf3b.webp)

Figure 4. Activity on GitHub accounts hosting malicious payloads, on December 20, 2022 (SEKOIA.IO)

## Payload analysis

We collected and analysed every payload still available from these accounts, as some of them were already banned by GitHub. We identified 70 samples of Vidar stealer, and 54 samples of [Raccoon stealer](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/).  
As Vidar and Raccoon are infostealers sold as a Malware-as-a-Service, we could reasonably expect to identify clients of the botnet service. We therefore listed the different botnets identifiers that we were able to extract from the samples:

  * Vidar: 1707, 1364 and 1839;
  * Raccoon: b4f472421ce1f18efd9f610339c3dae1 and 007ada2d73f5e9d5967b69ee7ea5e489.



![Distribution of malware/botnets associated with payloads hosted on GitHub \(SEKOIA.IO\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62aa2f46752fd0361b4_6a92a3cadc3071123832d437_6a2a7b74009bb67f3ecddefc.webp)

Figure 5. Distribution of malware/botnets associated with payloads hosted on GitHub (SEKOIA.IO)

All this information is valuable to understand that this whole infrastructure is only used to distribute two malware families, associated with a few botnets. At this stage, it is reasonable to postulate that this activity matches the one of an intrusion set working for its own personal interest, or on behalf of a few exclusive partners - in opposition to a large Traffic Distribution System, or Pay-Per-Install service, which spread a wide range of payloads at a larger-scale, managed by multiple cybercriminals.

Most collected payloads implement Defense Evasion techniques to avoid being executed in virtual environments, such as sandbox or virtual machines, and complexify static analysis. We observed the following techniques:

  * Payload packed with **Themida** , a commercial packer notably designed to disable a software code source from being disassembled, _e.g._<https://tria.ge/221220-qs8hsshe99>:  
`NewstVersion_1234_InstallerPass.rar/Setup.exe  
SHA256: ef70efe0a3cd860831657fa7ee8d832d49c8d8489df4b35d2480cc043bbb1b04`
  * Payload packed with **VMProtect** , another commercial packer protecting code being executed on a virtual machine, _e.g._<https://tria.ge/221220-qvjbpahf32>:  
`Open_New_Pass_1234_G4_Active.rar/Setup.exe  
SHA256: b66d3f7fc15dce8aca5a8489ddb7135b2a49fc2e39653ae9ac8ac4f6ea815412`
  * Payload packed with **Eziriz’s .NET Reactor** , a commercial packer used to prevent reverse engineering of .NET applications, _e.g._<https://tria.ge/221220-qyhvbshf57>:  
`LatestVersion_2022_PasSWrd_Active.rar/Setup.exe  
SHA256: 49c4fafc75e388a656e4e29fa2e8419d54c37cd700eaf48f67de67f13314ad78`
  * Payload leveraging **sandbox evasion** by query the Registry key associated to VirtualBox “HKLM\HARDWARE\ACPI\DSDT\VBOX__”, _e.g._<https://tria.ge/221220-q2hzhahf75>:  
`Active_APpLicatiOn_1234_Vr6ty-Oz.rar/Setup.exe  
SHA256: aa80f09c015c63a1b140be6cc7f6e102fbac728a94e9d7063caaaede90bbf364`
  * Payload leveraging **time based evasion** by executing the base64-encoded PowerShell command line “start-sleep -seconds 20”, _e.g._<https://tria.ge/221220-q5fcsahf97>:  
`FullActive_setup_1234_New_Version.rar/Setup.exe  
SHA256: 77cf1211c5fbbac802da6f3acfabfcd83a94e8e0fef6f50f925ddcc7bee412db`
  * Payload excluding the Windows repository “C:\” of Windows Defender monitoring by executing the base64-encoded PowerShell command line “set-mppreference -exclusionpath C:\”, _e.g._[https://tria.ge/submit/221220-q9wwbshg49](https://tria.ge/221220-q9wwbshg49):  
`PrimeSetup_1234_FullVersion_Active.rar/Setup.exe  
SHA256: d5c1c64135fad708c51d88ecc889a1b50404bfd3233f01a7b5f0d26b2c718b2e`



![Distribution of Defense Evasion techniques implemented by payloads hosted on GitHub \(SEKOIA.IO\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a629a2f46752fd0361af_6a92a3cb6568d7e2b4092992_6a2a7b74009bb67f3ecddeff.webp)

Figure 6. Distribution of Defense Evasion techniques implemented by payloads hosted on GitHub (SEKOIA.IO)

In addition to the techniques outlined above, all payloads are **compressed in password-encrypted RAR archives**. This **technique is very common among cybercriminals distributing commodity malware** , as it avoids the detection of the encrypted malicious executable. Moreover, the executables are **padded with zero-bytes to reach a large size** (more than 400MB), a size that is not accepted by most analysis tools.  
By using the previous defense evasion techniques, the intrusion set can increase the chances of successfully compromising a target system, making antivirus detection more difficult.

## Tracking this large infrastructure

In this part, we focus on the**illumination of the infrastructure used for the infection chain** leading to the distribution of Raccoon and Vidar payloads hosted on GitHub. As previously discussed, the infection chain uses several websites, domains and IP addresses for different stages, as detailed below.

### First stage - SEO poisoned websites advertising cracked software

The domain “crackist[.]com” hosting the websites leveraging SEO-poisoning is registered with a Namecheap privacy service and resolves a shared IP address provided by Amazon (99.83.154[.]118), which makes it difficult to pivot to other domain names.

By using the DNS records, and manually checking the results, SEKOIA.IO analysts identified the following list of 46 domain names, hosting cracked software websites:

allactivationkey[.]com  
allcracker[.]com  
audioplugins[.]net  
completecrack[.]com  
crackeyfree[.]com  
crackglobal[.]com  
crackist[.]com  
crackmykeys[.]com  
crackproduct[.]com  
crackregister[.]com  
crackservices[.]com  
crackwebs[.]com  
crackwebs[.]com  
crackwindow[.]com  
crackzero[.]com  
easywindowsactivator[.]com| forevercrack[.]com  
freewindowsactivator[.]com  
fullkeypro[.]com  
fullportable[.]com  
giantcrack[.]com  
hitpcgames[.]com  
latestproductkey[.]com  
macapps-download[.]com  
macdownloadpro[.]com  
macsoftwarepro[.]com  
masterforpc[.]com  
minicrack[.]com  
mocrack[.]com  
newactivationkey[.]com  
newcracksoft[.]com  
newlicensekeys[.]com| opcracks[.]com  
pandacracks[.]com  
plugin-torrent[.]com  
portabledownloads[.]com  
premiumcrack[.]com  
procracksoftware[.]com  
softkeygenpro[.]com  
softwarekeygen[.]com  
thecracksoftware[.]com  
totalcracks[.]com  
vst-crack[.]com  
vst-torrent[.]net  
windowsactivatorpro[.]com  
windowscrack[.]com  
---|---|---  
  
 _Table 1. Domain names sharing similarities with “crackist[.]com” in DNS records, and hosting SEO poisoned websites_

All these domains share the same JARM fingerprint, which seems to be specific to a default Cloudflare certificate. By correlating the JARM with the registrar, and again manually checking the results, we retrieved the 82 following domain names:

allcracker[.]comallsoftwarepro[.]com  
crack-line[.]com  
crack-warez[.]com  
crack-win[.]com  
crackask[.]com  
crackcow[.]com  
crackedfilez[.]com  
cracker01[.]com  
crackexe[.]net  
crackfaqs[.]com  
crackinges[.]com  
cracklet[.]com  
crackmyapps[.]com  
crackname[.]com  
cracknkeys[.]com  
cracknpc[.]com  
crackny[.]com  
crackpcpro[.]com  
crackre[.]com  
crackrepack[.]com  
cracks-full[.]com  
cracks11[.]com  
cracksbuddy[.]com  
cracksfree[.]net  
crackspromax[.]com  
cracksroom[.]com  
crackstores[.]com| cracktera[.]comcrackzsoft[.]com  
crackzsoft[.]me  
dailycracks[.]com  
dll-crack[.]com  
dllcrackz[.]com  
fitcrack[.]com  
free-crack[.]com  
full-crack[.]com  
full-cracked[.]com  
full-softwares[.]com  
fullcrackapp[.]com  
fullcrackfile[.]com  
hdstreamzforpcdl[.]com  
hitcrackspc[.]com  
icrackpro[.]com  
icracx[.]com  
inshotforpc[.]com  
keygen4u[.]com  
keygenguru[.]net  
license4softs[.]com  
macgamers[.]net  
nomanpc[.]com  
onecracks[.]com  
opcracks[.]com  
ovacrack[.]com  
patchzip[.]com  
pccrackspro[.]com| procrackapp[.]comprocracklink[.]com  
procracksfile[.]com  
samdownloads[.]net  
sharemeforpc[.]com  
softs32[.]com  
softskeygen[.]com  
tekken3forpc[.]com  
thecrackfiles[.]com  
thepccrack[.]com  
tocracks[.]com  
totalcracks[.]com  
trycracks[.]com  
unacademyforpc[.]com  
uploadpk[.]com  
uploadproper[.]net  
urcracks[.]net  
uscracks[.]com  
vysorforpc[.]com  
wecracks[.]com  
windowspatch[.]com  
wowcracks[.]com  
ycracks[.]com  
yourcracks[.]com  
---|---|---  
  
 _Table 2.Domain names sharing the same JARM and registrar as “crackist[.]com”, hosting SEO poisoned websites_

Although used templates differ between each website, most of them do embed download buttons redirecting to the second stage of our infrastructure.

Among theses websites we notably identified “inshotforpc[.]com” a website dedicated to the “InShot” software, also redirecting the user to the same infrastructure, using a tutorial and download buttons. Using the DNS records, we pivoted on other similar domain names.

dikshaappforpc[.]com  
hdstreamzforpcdl[.]com  
inshotforpc[.]com  
kinemasterforpcdl[.]com  
masterforpc[.]com| mobilelegendsforpc[.]com  
sharemeforpc[.]com  
tekken3forpc[.]com  
unacademyforpc[.]com  
vysorforpc[.]com  
---|---  
  
 _Table 3. Domain names related to the same distribution infrastructure using DNS records_

### Second stage - Redirect URLs containing the website title

Based on the identified websites, we retrieved second stage URLs, including:  
`hxxp://iglo0host[.]click/?z=2237&n=$TITLE  
hxxp://mikavika[.]click/?z=2938&f=3&n=$TITLE  
hxxps://myhasrnga[.]xyz/?z=1618&n=$TITLE  
hxxps://pingatinga[.]click/?it=12ec3f5c1fbe4c278&d=1&x=112&do=550b7d3b6&p=$TITLE  
hxxps://primrvils[.]click/?open=4d6eb9c6b47&d=1&x=183&close=fc476d220f&p=$TITLE  
hxxps://top3hostngc[.]xyz/?d=1&s=2739&q=$TITLE`  
These URLs are stage 1 of the redirection chain. They share common patterns that can be used to find more domains. Here are some characteristics:

  * TLD is either .click, .xyz or .cfd;
  * Exact path of the URLs is “/”;
  * Query fields are associations of two or more keywords, such as “z”/“n” or “open”/“d”/”x”/”close”.



By using indigestible regular expressions on URL scanning platforms, we found the following list of 108 domain names, extracted from the URLs. As the URL contains a webpage title related to a cracked software, SEKOIA.IO analysts associate these results to the same activity with high confidence.

We used the [following](https://urlscan.io/search/#\(task.url.keyword%3A%2Fhttp.*%5C.\(click%7Cxyz%7Ccfd\)%5C%2F%5C%3F\(s%7Cz%7Cd%7Copen%7Cit\)%3D.*%5C%26\(q%7Cn%7Cp\)%3D.*\(crack%7Cfree%7Cdownload%7Clicense%7Cpatch%7Chack\).*%2F%20OR%20task.url.keyword%3A%2Fhttp.*%5C.\(click%7Cxyz%7Ccfd\)%5C%2F%5C%3Fi%3D.*\(crack%7Cfree%7Cdownload%7Clicense%7Cpatch%7Chack\).*%2F%20OR%20page.url.keyword%3A%2Fhttp.*%5C.\(click%7Cxyz%7Ccfd\)%5C%2F%5C%3F\(s%7Cz%7Cd%7Copen%7Cit\)%3D.*%5C%26\(q%7Cn%7Cp\)%3D.*\(crack%7Cfree%7Cdownload%7Clicense%7Cpatch%7Chack\).*%2F%20OR%20page.url.keyword%3A%2Fhttp.*%5C.\(click%7Cxyz%7Ccfd\)%5C%2F%5C%3Fi%3D.*\(crack%7Cfree%7Cdownload%7Clicense%7Cpatch%7Chack\).*%2F\)) query on urlscan[.]io.

aboxwithfilez[.]xyz  
asperhost[.]xyz  
azilominehostz[.]xyz  
bdomicfilez[.]xyz  
binaryfile[.]cfd  
bitloservx[.]click  
blakbooot[.]click  
bnr45iqly[.]cfd  
bokywodzfa[.]xyz  
bottlecap1[.]click  
brownrabr[.]click  
bubl-filez[.]xyz  
ceedohostzcomi[.]xyz  
chondimahiy[.]xyz  
cl0nytig[.]xyz  
corokeralama[.]xyz  
corpyfoxiy[.]xyz  
crookhost[.]cfd  
crop18king[.]xyz  
ditlivhostz[.]xyz  
eros0hostz[.]xyz  
eroxyhost[.]xyz  
evosurver[.]click  
fiiezofcloude[.]xyz  
find2sitrox[.]xyz  
fishsurver[.]click  
fizzzhost[.]xyz  
freefiles22[.]xyz  
gooddata[.]xyz  
greenbottz[.]xyz  
heifan2survr[.]xyz  
hersiz00d[.]xyz  
hft76yu[.]cfd  
hificellfon[.]click  
hy3srver[.]xyz  
hyphnhostn[.]xyz| iee2kolmoz[.]xyz  
iglo0host[.]click  
itforhost[.]xyz  
kihygenvc[.]xyz  
kinbo112[.]xyz  
king-host[.]xyz  
kitefly[.]xyz  
kitlybitli44[.]xyz  
klimyteioz2b[.]xyz  
koptikbaj4[.]xyz  
krimikomrew4[.]xyz  
lowfeedo1[.]xyz  
loyabonzy[.]xyz  
lvihostng[.]click  
massraphost[.]xyz  
mattservrz[.]xyz  
mikavika[.]click  
minghost[.]cfd  
mo21srver[.]xyz  
moyakanj0[.]xyz  
myclotb0e[.]xyz  
myhasrnga[.]xyz  
myloster2v1[.]xyz  
mypklboy3[.]xyz  
mysite-servrz[.]xyz  
mytallphon[.]click  
naswarlobi[.]xyz  
neonhost[.]click  
nikuserver[.]xyz  
nysicforma[.]xyz  
odibolngup[.]click  
ooxyzhost[.]xyz  
opetafruith[.]xyz  
osr1file[.]xyz  
pepatoniyac[.]click  
pingatinga[.]click| pinkbotts2[.]xyz  
pozitfiiezi[.]xyz  
primrvils[.]click  
purplbogi[.]click  
purplebot21[.]xyz  
qcellphone[.]click  
qoli-filez[.]xyz  
quy32-filez[.]xyz  
ridsosurver1[.]xyz  
rizonfoggy[.]xyz  
roizohozt19[.]xyz  
safehand[.]xyz  
setserverfile[.]xyz  
sid4time[.]xyz  
sigrat4hyp[.]xyz  
singlwirre[.]click  
sitka-pyrok[.]xyz  
sixcozrevoli[.]xyz  
slom0wise4[.]xyz  
slugmefilehos[.]xyz  
surbexdillx[.]xyz  
survrhostngs[.]xyz  
tolby-file[.]xyz  
toloserverz[.]click  
top3hostngc[.]xyz  
trollhost[.]xyz  
urconsolest[.]click  
urhandups[.]xyz  
urstolupzo[.]xyz  
vig0boat[.]click  
ww16[.]ping-host[.]xyz  
ww16[.]tolby-file[.]xyz  
ww25[.]qoli-filez[.]xyz  
ww38[.]tolby-file[.]xyz  
xo-xohost[.]xyz  
yellokomput[.]xyz  
---|---|---  
  
 _Table 4. Domain names used for the second-stage redirecting from the SEO poisoned website_

### Third stage - Redirect URLs containing IP address

URLs of the third stage are only redirect URLs between stage 2 and stage 4. The method for stage 2 is applicable to stage 3. Here is the list of links used for this stage:

`hxxp://157.230.87[.]146/?639d9e9b635aa=74b9487b6e942ed6a2bcbdfe0ac54f51&639d9e9b635b4=2938&639d9e9b635b5=$TITLE&dfgdfg=169134&639d9e9b635b6=3  
hxxp://157.230.87[.]146/?639da05c274d8=df482a952ba365c515ca367f56ad72e5&639da05c274e1=2237&639da05c274e3=$TITLE&gkss=609427  
hxxp://157.230.87[.]146/?639da2cb59b39=ad790e90651d6c4e835e1790cab8f32a&639da2cb59b57=2337&639da2cb59b59=$TITLE&gkss=950459  
hxxps://162.243.164[.]175/?639d9f7a287a1=227a54a6b6fc0db3a0353afba97e1c92&639d9f7a287af=2739&639d9f7a287b0=$TITLE&gkss=87743`

The characteristics shared by these URLs are:

  * URLs are built from an IP address;
  * Exact path of the URLs is “/”;
  * All URLs contain the query field “gkss”, followed by an integer.



To find other related IP addresses, SEKOIA.IO analysts used the [following](https://urlscan.io/search/#page.url.keyword%3A%2Fhttps%3F%3A%5C%2F%5C%2F%5B0-9%5D%7B1%2C3%7D%5C.%5B0-9%5D%7B1%2C3%7D%5C.%5B0-9%5D%7B1%2C3%7D%5C.%5B0-9%5D%7B1%2C3%7D%5C%2F%5C%3F.*%5C%26gkss%3D%5B0-9%5D*%2F) query on urlscan[.]io.

By querying several URL sharing platforms, we found the following IP addresses:

**IP addresses**| **Valid on**  
---|---  
157.230.87[.]146| December 2022  
162.243.164[.]175| December 2022  
159.223.97[.]209| November 2022  
143.244.212[.]228| November 2022  
137.184.159[.]42| October 2022  
146.190.12[.]4| October 2022  
137.184.227[.]198| October 2022  
137.184.43[.]153| October 2022  
143.198.164[.]102| July 2022  
134.122.115[.]190| January 2022  
34.203.142[.]179| September 2021  
44.198.126[.]45| September 2021  
18.144.113[.]48| September 2021  
  
 _Table 5. IP addresses used for the stage 3 redirect URLs_

### Fourth stage - Webpages with instructions, download link and password

The stage 4 URLs display the webpage containing instructions, a download link and the password. Here is a list of links we manually collected:

`hxxps://entry4hide[.]cyou/?sandy=$REDACTED&639da05ebe3e1=$REDACTED  
hxxps://exitlocat[.]cyou/?a242f0edf87047a434e9b97d7f5c1b6e=$REDACTED&med=64084&src=639da2cc00c7e  
hxxps://exitlocat[.]cyou/?sandy=$REDACTED&639da2d1adb62=$REDACTED  
hxxps://jytibarose[.]xyz/?5a7bf36ab2a6d5859c470e6500cdc697=$REDACTED&med=121806&src=639dadb0a1639  
hxxps://jytibarose[.]xyz/?sandy=$REDACTED&639dadb20b907=$REDACTED  
hxxps://offsebike[.]cyou/?26be43758227d03fa58175aeb7c44ff8=$REDACTED&med=65518&src=639d9f8d23663  
hxxps://offsebike[.]cyou/?sandy=$REDACTED&639d9f8ed265d=$REDACTED  
hxxps://sigmarole[.]cyou/?b85e2ca0574125a3ef42b1a186dfde2e=$REDACTED&med=139248&src=639ee405f0b1a `

Same method again, URLs share the following characteristics:

  * TLD is either .cyou, .xyz or .click;
  * Exact path of the URLs is “/”;
  * URLs contain either the query field “sandy”, or “med” and “src”.



SEKOIA.IO analysts used the [following](https://urlscan.io/search/#page.url.keyword%3A%2Fhttps%3F%3A%5C%2F%5C%2F%5B%5E%5C%2F%5D*%5C.\(cyou%7Cxyz%7Cclick\)%5C%2F%5C%3F\(sandy%3D%7C.*%5C%26med%3D.*%5C%26src%3D\).*%2F) query on urlscan[.]io.

Using this query on URL sharing platforms results in the 20 following domains:

bitclandng[.]click  
entry4hide[.]cyou  
exitlocat[.]cyou  
geclandz[.]click  
get4pc[.]click  
get4pcsoft[.]click  
hosngclowz[.]cyou| jytibarose[.]xyz  
komikata[.]click  
landkemoty[.]click  
mekaofland[.]click  
monitorcrack[.]click  
offsebike[.]cyou  
pccracking[.]click| pirtibox[.]click  
sigmarole[.]cyou  
tikalandof[.]click  
whitr0sez[.]xyz  
withylndng[.]click  
woldcup20[.]cyou  
---|---|---  
  
 _Table 5. Domain names hosting the webpages with instructions, download URL and password_

## Conclusion

Sekoia.io illuminated a whole [infostealer](/blog/overview-of-the-russian-speaking-infostealer-ecosystem-the-logs) distribution infrastructure by pivoting on technical artefacts, such as DNS, JARM fingerprint, registrars and URLs. With these tracking methods, we were able to trace an infection chain leveraging fake cracked software back to a large and stealth infrastructure of over 250 domain names, that we assess to be almost certainly used since at least 2020.

Given the resilience of this infrastructure, the intrusion set will surely continue to leverage it in the near future to distribute the malicious payloads. It will be interesting to follow the possible changes in the distributed malware families to track down new threats, or new trends in defense evasion techniques.

More importantly, this blogpost highlights the potential risks of downloading cracked software, a very common social engineering technique to install malware. We highly recommend only downloading and installing software from trusted, official websites. Beyond the indicators of compromise, detection teams can hunt for infection chains leveraging fake cracked software by searching for weak signals, such as communications to unusual TLD and to URLs containing IP addresses, or looking for suspicious file names.

## IoCs & Technical Details

### IoCs

The list of IoCs is available on [SEKOIA.IO Community GitHub](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/infra_seo_crack_stealers/infra_seo_crack_stealers_iocs_20230106.csv).

#### Stage 1 (Websites leveraging SEO-poisoning)

allactivationkey[.]com  
allcracker[.]com  
allsoftwarepro[.]com  
audioplugins[.]net  
completecrack[.]com  
crack-line[.]com  
crack-warez[.]com  
crack-win[.]com  
crackask[.]com  
crackcow[.]com  
crackedfilez[.]com  
cracker01[.]com  
crackexe[.]net  
crackeyfree[.]com  
crackfaqs[.]com  
crackglobal[.]com  
crackinges[.]com  
crackist[.]com  
cracklet[.]com  
crackmyapps[.]com  
crackmykeys[.]com  
crackname[.]com  
cracknkeys[.]com  
cracknpc[.]com  
crackny[.]com  
crackpcpro[.]com  
crackproduct[.]com  
crackre[.]com  
crackregister[.]com  
crackrepack[.]com  
cracks-full[.]com  
cracks11[.]com  
cracksbuddy[.]com  
crackservices[.]com  
cracksfree[.]net  
crackspromax[.]com  
cracksroom[.]com  
crackstores[.]com  
cracktera[.]com  
crackwebs[.]com  
crackwindow[.]com  
crackzero[.]com  
crackzsoft[.]com| crackzsoft[.]me  
dailycracks[.]com  
dikshaappforpc[.]com  
dll-crack[.]com  
dllcrackz[.]com  
easywindowsactivator[.]com  
fitcrack[.]com  
forevercrack[.]com  
free-crack[.]com  
freewindowsactivator[.]com  
full-crack[.]com  
full-cracked[.]com  
full-softwares[.]com  
fullcrackapp[.]com  
fullcrackfile[.]com  
fullkeypro[.]com  
fullportable[.]com  
giantcrack[.]com  
hdstreamzforpcdl[.]com  
hitcrackspc[.]com  
hitpcgames[.]com  
icrackpro[.]com  
icracx[.]com  
inshotforpc[.]com  
keygen4u[.]com  
keygenguru[.]net  
kinemasterforpcdl[.]com  
latestproductkey[.]com  
license4softs[.]com  
macapps-download[.]com  
macdownloadpro[.]com  
macgamers[.]net  
macsoftwarepro[.]com  
masterforpc[.]com  
minicrack[.]com  
mobilelegendsforpc[.]com  
mocrack[.]com  
newactivationkey[.]com  
newcracksoft[.]com  
newlicensekeys[.]com  
nomanpc[.]com  
onecracks[.]com  
opcracks[.]com| ovacrack[.]com  
pandacracks[.]com  
patchzip[.]com  
pccrackspro[.]com  
pcgamesguru[.]com  
pcsoftkit[.]com  
plugin-torrent[.]com  
portabledownloads[.]com  
premiumcrack[.]com  
procrackapp[.]com  
procracklink[.]com  
procracksfile[.]com  
procracksoftware[.]com  
samdownloads[.]net  
sharemeforpc[.]com  
softkeygenpro[.]com  
softs32[.]com  
softskeygen[.]com  
softwarekeygen[.]com  
tekken3forpc[.]com  
thecrackfiles[.]com  
thecracksoftware[.]com  
thepccrack[.]com  
tocracks[.]com  
torrdroidforpc[.]com  
totalcracks[.]com  
trycracks[.]com  
unacademyforpc[.]com  
uploadpk[.]com  
uploadproper[.]net  
urcracks[.]net  
uscracks[.]com  
vst-crack[.]com  
vst-torrent[.]net  
vysorforpc[.]com  
wecracks[.]com  
windowsactivatorpro[.]com  
windowscrack[.]com  
windowspatch[.]com  
wowcracks[.]com  
ycracks[.]com  
yourcracks[.]com  
---|---|---  
  
#### Stage 2 (Redirect URL containing the webpage title)

aboxwithfilez[.]xyz  
asperhost[.]xyz  
azilominehostz[.]xyz  
bdomicfilez[.]xyz  
binaryfile[.]cfd  
bitloservx[.]click  
blakbooot[.]click  
bnr45iqly[.]cfd  
bokywodzfa[.]xyz  
bottlecap1[.]click  
brownrabr[.]click  
bubl-filez[.]xyz  
ceedohostzcomi[.]xyz  
chondimahiy[.]xyz  
cl0nytig[.]xyz  
corokeralama[.]xyz  
corpyfoxiy[.]xyz  
crookhost[.]cfd  
crop18king[.]xyz  
ditlivhostz[.]xyz  
eros0hostz[.]xyz  
eroxyhost[.]xyz  
evosurver[.]click  
fiiezofcloude[.]xyz  
find2sitrox[.]xyz  
fishsurver[.]click  
fizzzhost[.]xyz  
freefiles22[.]xyz  
gooddata[.]xyz  
greenbottz[.]xyz  
heifan2survr[.]xyz  
hersiz00d[.]xyz  
hft76yu[.]cfd  
hificellfon[.]click  
hy3srver[.]xyz  
hyphnhostn[.]xyz| iee2kolmoz[.]xyz  
iglo0host[.]click  
itforhost[.]xyz  
kihygenvc[.]xyz  
kinbo112[.]xyz  
king-host[.]xyz  
kitefly[.]xyz  
kitlybitli44[.]xyz  
klimyteioz2b[.]xyz  
koptikbaj4[.]xyz  
krimikomrew4[.]xyz  
lowfeedo1[.]xyz  
loyabonzy[.]xyz  
lvihostng[.]click  
massraphost[.]xyz  
mattservrz[.]xyz  
mikavika[.]click  
minghost[.]cfd  
mo21srver[.]xyz  
moyakanj0[.]xyz  
myclotb0e[.]xyz  
myhasrnga[.]xyz  
myloster2v1[.]xyz  
mypklboy3[.]xyz  
mysite-servrz[.]xyz  
mytallphon[.]click  
naswarlobi[.]xyz  
neonhost[.]click  
nikuserver[.]xyz  
nysicforma[.]xyz  
odibolngup[.]click  
ooxyzhost[.]xyz  
opetafruith[.]xyz  
osr1file[.]xyz  
pepatoniyac[.]click  
pingatinga[.]click| pinkbotts2[.]xyz  
pozitfiiezi[.]xyz  
primrvils[.]click  
purplbogi[.]click  
purplebot21[.]xyz  
qcellphone[.]click  
qoli-filez[.]xyz  
quy32-filez[.]xyz  
ridsosurver1[.]xyz  
rizonfoggy[.]xyz  
roizohozt19[.]xyz  
safehand[.]xyz  
setserverfile[.]xyz  
sid4time[.]xyz  
sigrat4hyp[.]xyz  
singlwirre[.]click  
sitka-pyrok[.]xyz  
sixcozrevoli[.]xyz  
slom0wise4[.]xyz  
slugmefilehos[.]xyz  
surbexdillx[.]xyz  
survrhostngs[.]xyz  
tolby-file[.]xyz  
toloserverz[.]click  
top3hostngc[.]xyz  
trollhost[.]xyz  
urconsolest[.]click  
urhandups[.]xyz  
urstolupzo[.]xyz  
vig0boat[.]click  
ww16[.]ping-host[.]xyz  
ww16[.]tolby-file[.]xyz  
ww25[.]qoli-filez[.]xyz  
ww38[.]tolby-file[.]xyz  
xo-xohost[.]xyz  
yellokomput[.]xyz  
---|---|---  
  
#### Stage 3 (Redirect IP addresses)

**IP addresses**| **Valid on**  
---|---  
157.230.87[.]146| December 2022  
162.243.164[.]175| December 2022  
159.223.97[.]209| November 2022  
143.244.212[.]228| November 2022  
137.184.159[.]42| October 2022  
146.190.12[.]4| October 2022  
137.184.227[.]198| October 2022  
137.184.43[.]153| October 2022  
143.198.164[.]102| July 2022  
134.122.115[.]190| January 2022  
34.203.142[.]179| September 2021  
44.198.126[.]45| September 2021  
18.144.113[.]48| September 2021  
  
#### Stage 4 (Webpages with instructions)

bitclandng[.]click  
entry4hide[.]cyou  
exitlocat[.]cyou  
geclandz[.]click  
get4pc[.]click  
get4pcsoft[.]click  
hosngclowz[.]cyou| jytibarose[.]xyz  
komikata[.]click  
landkemoty[.]click  
mekaofland[.]click  
monitorcrack[.]click  
offsebike[.]cyou  
pccracking[.]click| pirtibox[.]click  
sigmarole[.]cyou  
tikalandof[.]click  
whitr0sez[.]xyz  
withylndng[.]click  
woldcup20[.]cyou  
---|---|---  
  
### GitHub account abused to host payloads

hxxps://github[.]com/ppsinstall  
hxxps://github[.]com/Mughalshughal  
hxxps://github[.]com/Jonybba  
hxxps://github[.]com/GoldenMa-Re  
hxxps://github[.]com/dljack  
hxxps://github[.]com/Hashmi1211  
hxxps://github[.]com/davids1a  
hxxps://github[.]com/mega1211  
hxxps://github[.]com/moonh1211  
hxxps://github[.]com/shoby149  
hxxps://github[.]com/dodlosi  
hxxps://github[.]com/megajackson  
hxxps://github[.]com/chillqueem  
hxxps://github[.]com/maxiwel123  
hxxps://github[.]com/gilisoftt  
hxxps://github[.]com/primaryy1  
hxxps://github[.]com/moonshon  
hxxps://github[.]com/msdon1211  
hxxps://github[.]com/max1t7  
hxxps://github[.]com/leojack1211  
hxxps://github[.]com/naomibrown178  
---  
  
### Payloads mentioned in the blogpost

cda1504b1d4004c8bf3b90b9035ebeb8  
46832d82bc25c7363f32b3473872936e97cfe990  
4d18cd22365f3f3d714fca4a674014fc7a68d6029da4c53a94fe950189f9c956 (Raccoon)  
  
6a8fddac3de8f8b18c3789d7455a506f  
af822992f28e35504d8185fa558094e297a749ee  
8c5d344c77678fee2bf370d77313cd82a72442c4128ddfe9b4e32333e60116cd (Vidar)  
  
cda1504b1d4004c8bf3b90b9035ebeb8  
46832d82bc25c7363f32b3473872936e97cfe990  
4d18cd22365f3f3d714fca4a674014fc7a68d6029da4c53a94fe950189f9c956 (Raccoon)  
  
963011155b7b84c8850878c68b99445a  
f5f6cdfd1d12df787cf358e0e5eae8483ab6d06e  
ed9194aab02f28532a292a55883d17d4c6d9e1398b417c89c49274ef394730c1 (Vidar)  
  
c0d7637078d5dfa01af93ab2dda9b426  
c092990822a34d403bbbc0a640a2672e7d3e17d  
f77cf1211c5fbbac802da6f3acfabfcd83a94e8e0fef6f50f925ddcc7bee412db (Raccoon)  
  
bf6b5f2d76fb058e3e6a38cbdbdd22a5  
dfef116bd3994f05476040608d63fd8af19d09d7  
b2f86cda9f22b4adc43c5bb08dfc2625619ab487c5f172b35ce190ac6d8782a9 (Raccoon)  
---  
  
**More IoCs are available in the commercial CTI feed of SEKOIA.IO.**

### MITRE ATT&CK TTPs

**Tactic**  
| **Technique**  
---|---  
Resource Development| T1583.001 – Acquire Infrastructure: Domains  
Resource Development| T1583.004 – Acquire Infrastructure: Server  
Resource Development| T1588.001 – Obtain Capabilities: Malware  
Resource Development| T1588.002 – Obtain Capabilities: Tool  
Resource Development| T1608.006 – Stage Capabilities: SEO Poisoning  
Execution| T1204.002 – User Execution: Malicious File  
Defense Evasion| T1027 – Obfuscated Files or Information  
Defense Evasion| T1036 – Masquerading  
Defense Evasion| T1497.003 – Virtualization/Sandbox Evasion: Time Based Evasion  
Defense Evasion| T1562.001 – Impair Defenses: Disable or Modify Tools  
Defense Evasion| T1622 – Debugger Evasion  
Command and Control| T1102 – Web Service  
  
 _Table 6. MITRE ATT &CK TTPs related to this large and resilient infrastructure distributing information stealers_