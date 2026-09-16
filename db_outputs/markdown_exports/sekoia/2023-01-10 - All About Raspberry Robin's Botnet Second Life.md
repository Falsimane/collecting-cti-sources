# All About Raspberry Robin's Botnet Second Life

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/raspberry-robins-botnet-second-life
- **Date :** 2023-01-10

---

After our [first report about QNAPWorm](https://7095517.fs1.hubspotusercontent-na1.net/hubfs/7095517/FLINT%202022-016%20-%20QNAP%20worm_%20who%20benefits%20from%20crime%20\(1\).pdf?utm_campaign=FLINT%20-%20Communication%20RS&utm_source=Blogpost) dating back from March 2022, this malware made the headlines under the name of **Raspberry Robin** following a [RedCanary blogpost](https://redcanary.com/blog/raspberry-robin/). Since then, several vendors such as Microsoft, Secureworks and Avast investigated this malware and made connections to the infamous Russian cybercrime gang EvilCorp, responsible for the Dridex trojan and other malware, as well as several high profile financially motivated campaigns since at least 2014.

## **Raspberry Robin 101**

As a quick reminder, Raspberry Robin is a piece of malware which is downloaded via **infected thumb drives** and possibly **network shares**. The logic is quite straightforward: the infected device contains an LNK (Windows Shortcut). When the user plugs the thumb drive and launches the LNK which is disguised as a thumb drive or a network share, it will launch the Windows utility **msiexec**.

Once executed, and thanks to an URL specified in its arguments, msiexec will then download the main component of Raspberry Robin packed inside an MSI (Windows Installation Package) from a **compromised QNAP instance**. This process can be represented as follows:

![Three variants of Raspberry Robin LINK and their infection chain](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6276017750314a50dde_6a92a3c24b4041c69342dc22_6a2a7b7fb97c48a61ea4b452.webp)

Three variants of Raspberry Robin LINK and their infection chain

The main component of Raspberry Robin is a complex straint of malware that Sekoia analysts tried to reverse without success at the beginning of 2022. According to an [Avast research](https://decoded.avast.io/janvojtesek/raspberry-robins-roshtyak-a-little-lesson-in-trickery/), it has 14 layers of obfuscation, uses TOR _rendez-vous_ for its communications and innovative methods to remain undetected on a compromised system. Only a few specificities, such as dots at the end of dropped filenames, MSI execution associated with discriminant URLs patterns, rundll32 arguments or connection to TOR nodes from specific workstations allow defenders to hunt for Raspberry Robin in a network. 

As initially hypothesised with few of our customers, Raspberry Robin appears to be a type of Pay-Per-Install botnet, likely to be used by cybercriminals to distribute other malware on the infected systems such as coin miners, and other pieces of backdoors such as SocGholish, Bumblebee, TrueBot or IcedID, these ones eventually leading to hands-on-keyboard ransomware deployment.

Last year, Sekoia analysts observed Raspberry Robin deploying SocGholish on multiple occasions. SocGholish is a Microsoft JScript validator widely deployed through web browser [fake updates](/blog/clearfake-a-newcomer-to-the-fake-updates-threats-landscape) through malvertising campaigns. However, on these occasions SocGholish was deployed directly after a Raspberry Robin MSI execution in a high profile customer network, as shown below.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6276017750314a50ded_6a92a3c5e17eff730b65b162_6a2a7b80b97c48a61ea4b45d.webp)

Microsoft researchers reported encountering a similar infection chain, and assessed these SocGholish instances led to **lateralization inside the network via C2 Frameworks** followed by hands-on-keyboard ransomware deployment. In cases identified by Sekoia analysts, the infections stopped at the SocGholish execution stage as it was detected by the antivirus engine.

## **Raspberry Robin infrastructure**

Since our first FLINT, we decided to focus our research on the infrastructure contacted by msiexec to download the malicious MSI package which contains the main component of Raspberry Robin. Starting with a dozen domain names for the first FLINT, **we retrieved more than 270 domain names at the end of 2022** , used by this intrusion set since the creation of the botnet in July 2021.

To support the security community in defending against RaspberryRobin, @sekoia_io shared 270 known related domains on Github [available here](https://tinyurl.com/mtubjvxr).

Raspberry Robin uses compromised [QNAP Network-Attached Storage (NAS)](https://www.qnap.com/) resolved by domain names as its first C2 level. Each compromised QNAP seems to act as a validator and forwarder. If the received request is valid, it is redirected to an upper level of infrastructure. 

Thanks to our fellows at [TEAM CYMRU S2](https://www.team-cymru.com/blog/categories/threat-research), we were able to discover the second level of infrastructure. **This level is composed of (at least) eight VPS, hosted on Linode**. Sekoia analysts assess it is likely these VPS are used as forward proxies to a next infrastructure layer. However, we were unable to identify this next layer at the time of writing. These VPS have the same configuration, and two of them were contacted by the compromised QNAP on port 20001. Sekoia analysts associate them with the same infrastructure with high confidence.

![The two first levels of Raspberry Robin infrastructure. Source : Joint investigation between CYMRU S2 and Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6276017750314a50de7_6a92a3c4692919148899e3b8_6a2a7b7fb97c48a61ea4b458.webp)

The two first levels of Raspberry Robin infrastructure. Source : Joint investigation between CYMRU S2 and Sekoia

During the investigation, after identifying one of the compromised entities via their QNAP configuration and related *.myqnapcloud.com domain names, we also considered tapping one of the compromised QNAP based in France with a physical device (eg. with a Raspberry Pi). Even though a victim was identified and successfully contacted, we observed that the compromised QNAP instance was abandoned by the attackers within a few days: all domains resolving this QNAP instance switched to other compromised QNAPs.

This is one of the particularities of Raspberry Robin: the domain resolutions of its infrastructure are constantly changing, from a compromised QNAP to another. Dozens of new resolutions are made and new compromised QNAP are popping every day, limiting the risk of tapping or sinkholing it from an operator point of view. 

Here is a graph showing infrastructure changes between the 15, December 2022 and the 31, December 2022. During this time frame, 80 new QNAP instances were compromised and 1154 changes were made in DNS resolutions by active domain names.

![Evolution of Raspberry Robin domains resolutions and compromised QNAPs. Between 15/12/2022 and 31/12/2022.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6276017750314a50de1_6a92a3c1adf0bb92a651253d_6a2a7b7fb97c48a61ea4b44f.webp)

Evolution of Raspberry Robin domains resolutions and compromised QNAPs. Between 15/12/2022 and 31/12/2022.

## **Partial takedown**

It is worth noting that **on 26, October 2022, the botnet was partially taken down** leading to the deactivation of approximately 80 domains registered via namecheap.com. This represented around 30% of the domains used by Raspberry Robin. These domains had their DNS zone deleted and the tags clientHold, clientTransferProhibited were added to their status codes, leading to a total loss by the botnet operators. 

![Number pf operational domains form July to January 2023. Source : Statistics from Sekoia trackers.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6276017750314a50dea_6a92a3c3692919148899e261_6a2a7b7fb97c48a61ea4b455.webp)

Number pf operational domains form July to January 2023. Source : Statistics from Sekoia trackers.

## **The second life of Raspberry Robin**

One of the identified weaknesses of the Raspberry Robin worm is to rely on msiexec to download and execute the main payload, without control mechanism implemented to ensure the payload comes from a trusted source. Therefore, anyone able to hijack the request done by msiexec can get victims to download another rogue MSI payload. This can be achieved notably through DNS hijacking attacks, such as [QUANTUM DNS](https://theintercept.com/document/nsa-gchqs-quantumtheory-hacking-tactics/), or simply by purchasing domain names linked to this threat after their expiration.

As approximately thousands of USB thumb drives were compromised by Raspberry Robin, Sekoia analysts suspected it was almost certain this threat would remain active, even after domain names expire, possibly leading to a second life of this botnet, by other cybercriminals.

To show this hypothesis, we tried to sinkhole one of the first domain names used by the malicious LNKs to download and execute an MSI Package. Our research focused on tiua[.]uk and gloa[.]in, both registered on the first days of the Raspberry Robin campaign, on the 26 July 2021.

Few months ago, we got lucky when the domain tiua[.]uk was available for sale. This domain was used as a C2 between 2021-09-22 and 2022-11-30 until .UK registry suspended it, probably because of registrant contact information inaccuracies.

By pointing this domain to our sinkhole, we were able to obtain telemetry from one of the first domains used by Raspberry Robin operators. As we expected and since it was one of the first domains used by this worm, the telemetry of this specific domain was limited. Moreover, the shortcuts pointing to this domain were from the first generation of distributed LNKs, detected by most anti-virus solutions today.

However, we were still able to observe several victims, showing that it was still possible to repurpose a Raspberry Robin domain for malicious activities one year after the domain was created. As expected we also identified a few thumb drives passing from one computer to another, showing the potential of multiple computer infections from one single LNK.

It should be noted that as compromised entities or specific sectors use common IP addressing in Internet Service Providers Autonomous Systems, identifying them was particularly complex. Sekoia was able to identify the administration network of a European university thanks to the leak of its internal proxy in the Via: HTTP header and several businesses around the world.

We tried to map all of these infections to verify whether these first Raspberry Robin victims originated from specific countries, as commonly observed for USB worms such as [RETADUP](https://twitter.com/felixaime/status/1187761974958051334).

![Countries with first victims of Raspberry Robin. Source : Statistics from the tula.uk sinkholed domain.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a6276017750314a50de4_6a92a3c62e47a1e9fe0e4d3c_6a2a7b80b97c48a61ea4b460.webp)

Countries with first victims of Raspberry Robin. Source : Statistics from the tula.uk sinkholed domain.

It is worth noting the first infections are not located in a specific region of the world. Unlike RETADUP or other USB worms, the spreader of Raspberry Robin is not embedded in the main payload, and acts as a standalone executable which can be executed automatically or hands-on-keyboard by attackers. Sekoia analysts assess it is probable that the first Raspberry Robin USB infections were done by hands, relying on other malware and initial accesses. We further assess it is possible Raspberry Robin operators used another botnet to disseminate the first version of the worm. This hypothesis can be supported with the discovery of the [Raspberry Robin .NET spreader by Microsoft](https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/). 

During this research, Sekoia analysts sinkholed ynns[.]uk, another domain used by the botnet, and also blocked by the .UK registry. Therefore, it resolved compromised QNAP C2s for less than one month, from 2021-10-25 to 2021-11-19. **This domain allowed us to identify victims in additional countries, including the United States, Germany, Romania, Oman, Morocco, Bahrain and Kazakhstan.**

## **So, what’s next?**

This paper is an illustration of how botnets serve multiple purposes and can be reused and / or remodelled by their operators or even hijacked by other groups over time. As disclosed recently by Mandiant with TURLA guys [repurposing few domains of the Andromeda botnet](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity), **the repurposing of botnets and accesses (such as webshells) is not new** and [threat actors have already developed capabilities to do that in the past](https://arstechnica.com/information-technology/2015/01/nsa-secretly-hijacked-existing-malware-to-spy-on-n-korea-others/). 

As many botnets and worms, @sekoia_io demonstrated that RaspberryRobin can be repurposed by other threat actors to deploy their own implants. 

This further contributes to Sekoia analysts' confidence that the threat must be continuously monitored, investigated and reassessed to provide actionable Cyber Threat Intelligence.

Besides documenting the threat, it appears critical to create tailored rules to detect Raspberry Robin generated LNKs or msiexec processes communicating outside the network. As of today, even though security vendors offer strong detection on these two points, **Sekoia analysts assess Raspberry Robin operators possibly will update their infection chain** to evade detection to continue targeting organisations worldwide in the medium to long term. 

Therefore, Sekoia analysts will continue to monitor and report on this threat as an interesting cybercriminal case to follow through the time.