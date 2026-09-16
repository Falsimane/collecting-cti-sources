# CALISTO Continues its Credential Harvesting Campaign

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/calisto-continues-its-credential-harvesting-campaign
- **Date :** 2022-06-22

---

‍ _This blog post on CALISTO threat actor is an extract of a FLINT report (_[_Sekoia_](/about-threat-detection-research-team) _Flash Intelligence) sent to our clients on June 16, 2022._

March 30, 2022, Google TAG published several [IOCs related to Calisto](https://blog.google/threat-analysis-group/update-on-cyber-activity-in-eastern-europe/) \- a Russia-nexus threat actor also known as COLDRIVER which targeted several Western NGOs, think tanks and the defense sector in the past. According to Google TAG, the operators used freshly created Gmail accounts to carry out a spear-phishing campaign.

Based on TAG’s findings, Calisto used, at least on one occasion, decoys documents hosted on Google Docs as well as Microsoft One drive, to entice the victim to click on a link leading to the phishing domain, purporting to display the document’s content. The tactic consists in using a legit service as a proxy for credential phishing, this aims at bypassing controls from the victim’s mail gateways as the email itself does not contain a malicious link any longer.

Additionally, TAG uncovered that On April 21, 2022, a new website named "_Very English Coop d'Etat_ '' surfaced. This website allegedly aims at revealing a plot related to the Brexit. However, as mentioned by [security researcher Costin Raiu on Twitter](https://twitter.com/craiu/status/1529744064253403139), at least one leaked document seems to be a fake from the attackers. Based on the leveraged design, method and screenshots,this activity reminds the “Hack and Leak'' campaigns operated between 2015 and 2019 and associated to [Russia](/blog/eternityteam-a-new-prominent-threat-group-on-underground-forums)-nexus intrusion sets SOFACY and HADES.

Even if the new website reminds the old ones from SOFACY, [Google TAG declared in an interview to Reuters](https://www.reuters.com/technology/exclusive-russian-hackers-are-linked-new-brexit-leak-website-google-says-2022-05-25/) that they’ve been able to “ technically link this website to CALISTO operations”, without mentioning the technical details leading to this attribution. As of today, while weak links can be established between past GRU associated cyber operations TTPs and this documented activity, Sekoia refrains from associating CALISTO’s operations to Russian Intelligence and Security Services.

## **Infrastructure analysis** of CALISTO

Following these two publications, Sekoia investigated the Calisto phishing domains in order to protect our customers. CALISTO uses [Evilginx](https://github.com/kgretzky/evilginx2) on its VPS to capture the victim’s credentials. This well known open source tool creates an SSL reverse proxy between the victim and a legitimate website to capture web credentials, [2FA](/blog/sneaky-2fa-exposing-a-new-aitm-phishing-as-a-service) tokens... 

It's worth mentioning that CALISTO operators just followed the Github README of the EvilGinx project, creating default redirection for some of their VPS to the Youtube Rick’roll video. Additional servers redirect to the New York Times home page, these two OPSEC fails allowing us to find more servers easily.

By digging deeper a phishing domain _(file-milgov[.]systems)_ targeting the Ukrainian MOD drew our attention. Unlike the previous CALISTO domains, this one uses a webpage written in PHP to capture credentials. It is worth mentioning that this domain have been catched also by Trellix in their article "[Growling Bears Make Thunderous Noise](https://www.trellix.com/en-us/about/newsroom/stories/research/growling-bears-make-thunderous-noise.html)" without attribution.

![Infrastructure analysis of calisto apt](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a667cd1cab63350d8dfb_6a92a4779f9b7f8b2cd0b532_6a2a7968b7830b743009f108.webp)

Infrastructure analysis of calisto apt

While it doesn't match our Evilginx heuristic, it was operated in the same network range as several CALISTO domains during the same time frame. Therefore, it is likely possible that this domain is associated with a spear-phishing operation from CALISTO, the link being determined with a low degree of confidence.

As of today, [Sekoia](/about) has been able to link 24 unique domains operating Evilginx related to CALISTO operations with medium to high confidence.

## **IoCs** of CALISTO

### **Domain names**

 _Please blacklist these domains and the associated FQDNs_

`documents-cloud[.]com   
cache-docs[.]com  
protect-link[.]online  
docs-shared[.]com  
documents-cloud[.]online  
drive-share[.]live  
hypertextteches[.]com  
proton-docs[.]com  
docs-drive[.]online  
cloud-docs[.]com  
drive-docs[.]com  
file-milgov[.]systems  
cache-dns[.]com  
office-protection[.]online  
proton-view[.]online  
pdf-shared[.]online  
proton-viewer[.]com  
protectionmail[.]online  
pdf-docs[.]online  
documents-pdf[.]online  
docs-cache[.]com  
pdf-cloud[.]online  
docs-info[.]com  
protection-office[.]live  
`