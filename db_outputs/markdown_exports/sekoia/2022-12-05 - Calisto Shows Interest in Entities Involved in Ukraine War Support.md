# Calisto Shows Interest in Entities Involved in Ukraine War Support

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/calisto-show-interests-into-entities-involved-in-ukraine-war-support
- **Date :** 2022-12-05

---

Calisto (aka Callisto, COLDRIVER) is suspected to be a Russian-nexus intrusion set active since at least April 2017. Although it was not publicly attributed to any Russian intelligence service, past Calisto operations showed objectives and victimology that align closely with Russian strategic interests.

[Calisto](/blog/calisto-continues-its-credential-harvesting-campaign) mainly focuses on Western countries, especially the United States, and Eastern European countries. The group was observed carrying out [phishing campaigns](/blog/phishing-campaigns-i-paid-twice-targeting-booking-com-hotels-and-customers) aiming at credential theft, targeting military and strategic research sectors such as NATO entities and a Ukraine-based defense contractor, as well as NGOs and think tanks. Additional victimology includes former ntelligence ofﬁcials, experts in Russian matters, and Russian citizens abroad.

While Security Service of Ukraine (SBU) publicly associated Calisto with Gamaredon Group, an intrusion set attributed to the Russian Federal Security Service (FSB) that focuses essentially on Ukraine operations since the beginning of the Russian invasion in February 2022, this link is not supported by other security companies or researchers. Sekoia conducted further technical investigations but did not ﬁnd any overlap between Calisto and Gamaredon activities.

## Technical analysis

Based on Sekoia EvilNgix trackers, we came across domains, known to us as aligning with past Calisto activities. Further investigations led to a larger infrastructure composed of more than 80 domains, including domains typosquatting entites.

As several of these domains were already known and resolving IP addresses already attributed to [Calisto activities](/blog/calisto-continues-its-credential-harvesting-campaign), Sekoia associates these domains to Calisto with high conﬁdence.

In past observed campaigns, Calisto operators sent malicious PDF attachments to their victims. The ﬁrst page of the PDF mimics an error in the PDF renderer engine, inciting the victim to open a link leading to a malicious web page. This webpage aims at gathering the victim’s credentials by using EvilGinx. Here are a few examples of PDF retrieved in this investigation:

![First pages of malicious PDF sent by Calisto](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62d1584be1e5d9db3ca_6a92a3d23e6167cebbf6ad77_6a2a7b604452dad8088d1753.webp)

Figure 1. First pages of malicious PDF sent by Calisto

The last pages of the documents contain blobs of spirals and text, as shown below. Sekoia analysts still don’t know why such gibberish is used as it appears useless as an anti-detection trick. However, the idea to put the phishing link in a PDF instead of in the email body prevents link analysis from email gateways and is a good tactic to remain undetected from an attacker point of view.

![Garbage present in the last document pages resulting from the technical analysis of Calisto](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a62d1584be1e5d9db3cd_6a92a3d32e47a1e9fe0e55b9_6a2a7b604452dad8088d1756.webp)

Figure 2. Garbage present in the last document pages resulting from the technical analysis of Calisto

## Victimology analysis

Sekoia conducted open-source research on the typosquatted domains, to identify targets. As we redact this paper, we found six private companies based in the US and Eastern Europe, and four Non-governmental organizations (NGOs), all involved in Ukraine support. Sekoia contacted the NGOs to get the phishing email or payload.

One of them shared the email exchange between the victim and the attacker using a spoofed email from a “trusted source”, including the malicious PDF payload, a technique previously observed in Calisto campaigns. The email exchange shows that the attacker did not include the malicious payload in the ﬁrst email, but waited to get an answer to build a relationship and avoid suspicion before sending the payload to the victim. That Calisto social engineering technique was already observed by Microsoft.

Most of the targeted private organizations are involved in military equipment, military logistics or humanitarian support for Ukraine, including a US company that provides humanitarian logistics and possibly tactical equipment to Kiev. Other sectors include communication technologies and cybersecurity (medium conﬁdence) :

  * **UMO** , Polish company, military equipment (high conﬁdence);
  * **Emcompass** , Ukrainian company, military logistic (high conﬁdence);
  * **DTGruelle** , US company, logistics (high conﬁdence);
  * **Global Ordnance** , US company, military and tactical equipment (high conﬁdence);
  * **BotGuard** , Estonian company, cybersecurity (medium conﬁdence);
  * **Blue Sky Network** , US company, satellite communications (high conﬁdence).



Additional potential victims include NGOs and think tanks involved in conﬂict resolution and war crime investigation, including an organization also involved in the Syrian civil war crime investigation and previously targeted by an Indian hack-for-hire company in June 2020. Most of the NGOs and think tanks targeted are publicly supporting Ukraine.

  * **International Center on Nonviolent Conﬂict** , US think tank promoting non-military strategies by civilian-based movements to defend human rights (high conﬁdence);
  * **Commission for International Justice and Accountability** , Europe-based NGO, proof collection for human rights violation and war crime (high conﬁdence);
  * **Centre for Humanitarian Dialogue** , Swiss-based NGO, mediation and diplomacy for conﬂict resolution (high conﬁdence);
  * **Foundation for support of reforms in Ukraine** , Ukraine-based NGO, economic reforms promotion, likely involved in post-war reconstruction planning (medium conﬁdence).



Sekoia notes that the observed victimology through the investigation matches known Calisto victimology, namely strategic research, civil society and military equipment sectors, as well as entities and individuals involved in Russian matters.

## Calisto targets non-directly related to Ukraine support

Among discovered Calisto malicious domains, three caught Sekoia analysts’ attention, mvd-redir[.]ru and dns-mvd[.]ru (high conﬁdence) that are highly likely typosquatting the **Russian Ministry of Interior** , and lk-nalog-gov[.]ru (_low_ conﬁdence) the Russian Federal Taxation Service. Based on the fact that Calisto was observed targeting Russian individuals abroad, **Sekoia assess it is plausible that Calisto conducts domestic surveillance as well**. Another less plausible hypothesis would be a false-ﬂag maneuver to raise doubts on the infrastructure’s attribution.

Sekoia found another potential victim that matches Calisto known targeting. The domain sangrail-share[.]com and sangrail-ltd[.]com are typosquatting **Sangrail Inc**., a private security company, [registered](https://find-and-update.company-information.service.gov.uk/company/12131777) in the UK on 31 July 2019 by Ian Walter Baharie. That name was used as well [to **register AC21**](https://www.ac21.co.uk/about), a British private intelligence company focused on African politics. Interestingly, that name showed up in a 17-years-old [data leak](https://cryptome.org/mi6-list2.htm) exposing a list of several MI6 oﬃcers on cryptome.org, a website dedicated to information leaks. That observation matches Microsoft [assessment](https://www.microsoft.com/en-us/security/blog/2022/08/15/disrupting-seaborgiums-ongoing-phishing-operations/) on **Calisto targeting former intelligence oﬃcers.**

## Conclusion

Despite the absence of technical evidence associating Calisto activities with a known Russian cyber offensive service, Sekoia assess that this intrusion set intelligence collection activities targeting parties involved in Ukraine support, especially those in the tactical equipment logistics, probably **contribute** to **Russian efforts** to **disrupt Kiev supply-chain** for military reinforcements.

Based on the targeting of Commission for International Justice and Accountability NGO, Sekoia assess that Calisto contributes to **Russian intelligence collection about identiﬁed war crime-related evidence** and/or international justice procedures, likely to anticipate and build counter narrative on future accusations.

To provide our customers with actionable intelligence, Sekoia analysts will continue to monitor state-sponsored advanced and persistent threats, including Calisto, as well as cybercrime related groups. **We welcome any feedback and / or additional input to further contribute to understanding and countering Calisto threat.**

## IOCs & Technical Details

`access-confirmation[.]com  
allow-access[.]com  
antibots-service[.]com  
apicomcloud[.]com  
as-mvd[.]ru  
attach-docs[.]com  
attach-update[.]com  
blueskynetwork-drive[.]com  
blueskynetwork-shared[.]com  
botguard-checker[.]com  
botguard-web[.]com  
challenge-identifier[.]com  
challenge-share[.]com  
checker-bot[.]com  
cija-docs[.]com  
cija-drive[.]com  
cloud-safety[.]online  
cloud-us[.]online  
default-dns[.]online  
disk-previewer[.]com  
dns-cache[.]online  
dns-challenge[.]com  
dns-cookie[.]com  
dns-mvd[.]ru  
docs-cache[.]online  
docs-collector[.]com  
docs-shared[.]online  
docs-storage-ltd[.]com  
docs-viewer[.]online  
docs-web[.]online  
document-guard[.]com  
document-sender[.]com  
drive-control[.]com  
drive-defender[.]com  
drive-global-ordnance[.]com  
drive-globalordnance[.]com  
drive-information[.]com  
drive-previewer[.]com  
drive-us[.]online  
dtgruelle-drive[.]com  
dtgruelle-us[.]com  
encompass-drive[.]com  
encompass-shared[.]com  
filter-bot[.]com  
global-ordnance-drive[.]com  
goweb-protect[.]com  
goweb-service[.]com  
guard-checker[.]com  
hd-centre-drive[.]com  
hd-docs-share[.]com  
hypertexttech[.]com  
hypertextttech[.]com  
land-of-service[.]com  
live-identifier[.]com  
mvd-cloud[.]ru  
mvd-redir[.]ru  
network-storage-ltd[.]com  
nonviolent-conflict-service[.]com  
nonviolent-conflict-storage[.]com  
online-word[.]com  
preview-docs[.]com  
preview-docs[.]online  
protectedshields-storage[.]com  
protection-web-app[.]com  
proxycrioisolation[.]com  
redir-document[.]com  
response-collector[.]com  
response-filter[.]com  
response-mvd[.]ru  
response-redir[.]com  
safe-proof[.]com  
sangrail-ltd[.]com  
sangrail-share[.]com  
selector-drafts[.]online  
share-drive-ua[.]com  
soaringeagle-drive[.]com  
storage-service[.]online  
threatcenterofreaserch[.]com  
threatcenterofresearch[.]com  
transfer-dns[.]com  
transfer-record[.]com  
umo-drive[.]com  
umopl-drive[.]com  
umopl[.]com  
webview-service[.]com  
`

Discover our:

  * [CTI platform](/platform/intelligence)
  * [SIEM platform](/platform/defend)