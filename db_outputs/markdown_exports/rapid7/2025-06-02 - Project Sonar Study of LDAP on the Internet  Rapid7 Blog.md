# Project Sonar Study of LDAP on the Internet | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/11/08/project-sonar-study-of-ldap-on-the-internet/
- **Date :** 2025-06-02

---

The topic of today's post is a [Rapid7 Project Sonar](https://sonar.labs.rapid7.com/) study of publicly accessible LDAP services on the Internet. This research effort was started in July of this year and various portions of it continue today. In light of the Shadowserver Foundations's [recent announcement](https://ldapscan.shadowserver.org/) regarding the availability relevant reports we thought it would be a good time to make some of our results public. The study was originally intended to be an Internet scan for Connectionless LDAP (CLDAP) which was thought to only be used by Microsoft Active Directory. This protocol uses LDAP over UDP instead of the typical TCP. CLDAP was proposed in [RFC 1798](https://tools.ietf.org/html/rfc1798) in June of 1995 but its standard was marked as abandoned per [RFC 3352](https://tools.ietf.org/html/rfc3352) in March of 2003 due to lack of support and implementation. Microsoft uses CLDAP as part of the client's discovery mechanism via [LDAP Ping](https://msdn.microsoft.com/en-us/library/cc223811.aspx) [(additional reference)](https://msdn.microsoft.com/en-us/library/ff718294.aspx).

In the early phases of the study it was determined that the toolset could be used to survey LDAP over TCP and so the scope was expanded. In this document the term LDAP will used to interchangeably for both LDAP (TCP) and CLDAP (UDP).

The intent of the study was to attempt to answer multiple questions:

  1. How prevalent is publicly accessible LDAP on the Internet? The term "publicly accessible" in this case means services that allow connections from and communications with our various scanners. In no case did we test with any form of authentication other than that of an anonymous LDAP bind.
  2. Can we identify the remote service and, if so, determine if Microsoft Active Directory is the only product using CLDAP protocol?
  3. Would CLDAP be an effective service in DRDoS attacks?



## Study implementation

Like most other UDP services CLDAP will only respond to correctly formatted probes. In our study we performed service discovery using [Zmap](https://zmap.io/) with a probe file containing a [rootDSE](https://www.ldap.com/the-directory-information-tree) request. This request, defined in [RFC 4512 Section 5.1](https://tools.ietf.org/html/rfc4512#section-5.1), is part of the LDAP protocol standard and is essentially a request for information about the server and its capabilities. The rootDSE request was chosen as the functionality should be present on all LDAP servers and, importantly, it does not require authentication by [RFC definition](https://tools.ietf.org/html/rfc4513#section-4). This reduces the legal risk of the study as no authentication mechanisms needed to be bypassed.

During the study it was found that most of the LDAP responses were larger than a single packet and were fragmented in order to traverse the Internet. Fragment reassembly functionality [is not part of the Zmap use case](https://github.com/zmap/zmap/issues/358) at this time so we followed the scan with another scan against open services using a custom tool that performs a more comprehensive capture of the response.

Since the protocol for communicating with Microsoft's LDAP on UDP is pretty much per [RFC standard](https://tools.ietf.org/html/rfc4511), it would make sense that any tooling that works with LDAP over UDP should also work with LDAP over TCP with minor changes. This turned out to be the case and the study was expanded to the following ports and services:

Port/Proto| Description  
---|---  
389/tcp| Standard LDAP port, depending on product/config it may support STARTTLS  
636/tcp| LDAP over TLS  
3268/tcp| Microsoft Active Directory Global Catalog, may support STARTTLS  
3269/tcp| Microsoft Active Directory Global Catalog over TLS  
389/**udp**|  Connectionless LDAP implementation for Active Directory  
  
We've performed multiple Internet wide scans on these ports as part of the study. Where possible we negotiated TLS or STARTTLS.

The results published in this post are based on Internet wide IPv4 scans performed September 14th and 15th of this year.

## Study results

### Prevalence

The answer to the study's first question is that there are a significant number of publicly accessible LDAP servers on the Internet.

Port| Responses| Decoded as LDAP| Percent  
---|---|---|---  
389/tcp| 300,663| 264,536| 88.0%  
636/tcp| 91,842| 72,230| 78.6%  
268/tcp| 113,207| 96,270| 85.0%  
269/tcp| 30,199| 29,668| 98.2%  
389/**udp**| 79,667| 78,908| 99.0%  
  
The percentage of LDAP servers is actually slightly higher than reported. Some of the service responses that did not decode as LDAP were visually identified as fragments of legitimate LDAP responses.

### Service identification

A significant number of services returned information that allowed us to successfully fingerprint them. This fingerprinting capability was added to the Rapid7 Recog tool which is discussed later in this post. In our data set we found that most of the LDAP services were Microsoft Active Directory Controllers (ADC) or [Lightweight Directory Services (LDS)](https://msdn.microsoft.com/en-us/library/aa705886.aspx) (formerly [Active Directory Application Mode](https://technet.microsoft.com/en-us/library/cc738377.aspx))

Here is the breakdown of ADC and LDS services in the data set. The Samba ADC implementation has been included as well.

Port| Total LDAP| MS ADC| %| MS LDS| %| Samba AD| %  
---|---|---|---|---|---|---|---  
389/tcp| 264,536| 117,875| 44.6%| 4,209| 1.6%| 1,276| 0.5%  
636/tcp| 72,230| 37,848| 52.4%| 214| 0.3%| 1,222| 1.7%  
3268/tcp| 96,270| 95,057| 98.7%| 0| 0.0%| 1,169| 1.2%  
3269/tcp| 29,668| 28,470| 96.0%| 0| 0.0%| 1,159| 3.9%  
389/udp| 78,908| 76,356| 96.8%| 1,223| 1.5%| 1,283| 1.6%  
  
It turns out that it is possible to not only identify the software in most cases, but we can usually identify the host operating system as well. In the case of Microsoft ADC and LDS services, there is almost always enough information to determine the more specific operating system version such as Windows Server 2012 R2. Most of the ADC and LDS services in the data set are running supported versions of the OS. Some are ahead of the curve, some are behind. As a note, Microsoft ended **all** support for all versions of Windows Server 2003 as of [July 14, 2015](https://support.microsoft.com/en-us/lifecycle/search?alpha=Windows%20Server%202003%20R2).

Product| 389/tcp| %| 389/udp| %  
---|---|---|---|---  
Total AD and LDS| 122,084| | 77,579|   
MS Windows Server 2008 R2| 48,050| 39.4%| 21,309| 27.5%  
MS Windows Server 2012 R2| 35,159| 28.8%| 28,354| 36.6%  
MS Windows Server 2003| 15,476| 12.7%| 12,342| 15.9%  
MS Windows Server 2008| 12,307| 10.1%| 5,750| 7.4%  
MS Windows Server 2012| 10,868| 8.9%| 8,862| 11.4%  
MS Windows Server 2016| 224| 0.2%| 195| 0.3%  
MS Windows Server 2000| 0| 0.0%| 767| 1.0%  
  
We can also identify other products, just in smaller numbers. The table below contains a few examples selected from a much longer list.

Count| Product| Port  
---|---|---  
52,429| OpenLDAP OpenLDAP| 389/tcp  
13,962| OpenLDAP OpenLDAP| 636/tcp  
9,536| Kerio Connect| 636/tcp  
2,149| VMware Platform Services Controller 6.0.00| 389/tcp  
2,118| VMware Platform Services Controller 6.0.00| 636/tcp  
517| IBM Security Directory Server 6.3| 389/tcp  
435| Fedora Project Fedora Directory Server 1.0.4 B2007.304.11380| 389/tcp  
397| IBM Security Directory Server 6.1| 389/tcp  
248| innovaphone IPVA| 636/tcp  
154| Sun Microsystems Sun Java System Directory Server 5.2_Patch_6| 389/tcp  
148| IBM Domino LDAP Server 8.5.30| 389/tcp  
  
This allows us to answer the study's second question of the ability to identify services. We can successfully do this in many cases though there is a non-trivial number of generic LDAP response returned on 389/tcp. We've also determined that Microsoft ADC and LDS aren't the only services using CLDAP as we found six instances **Novel LDAP Agent for eDirectory** in the data set.

### DRDoS utility

The specific type of DDoS we are interested in was described by Rapid7 Labs researcher Jon Hart in a recent Rapid7 Community [blog post](/blog/post/2016/10/31/understanding-udp-amplification-vulnerabilities-through-rapid7-research/):

A distributed, reflected denial of service (DRDoS) attack is a specialized variant of the DDoS attack that typically exploits UDP amplification vulnerabilities. These are often referred to as volumetric DDoS attacks, a more generic type of DDoS attack that specifically attempts to consume precious network resources.

A UDP amplification vulnerability occurs when a UDP service responds with more data or packets than the initial request that elicited the response(s). Combined with IP packet spoofing/forgery, attackers send a large number of spoofed UDP datagrams to UDP endpoints known to be susceptible to UDP amplification using a source address corresponding to the IP address of the ultimate target of the DoS. In this sense, the forged packets cause the UDP service to "reflect" back at the DoS target.

Based on service responses to probes on 389/**udp** it would appear CLDAP does provide a significant amplification source. The UDP datagram probe that was used in the study was roughly 51 bytes. Most of the valid LDAP responses without the headers ranged from 1,700 to 3,500 bytes. There were a few outliers in the 5,000 to 17,700 range. The chart below shows the response size distribution with the larger outliers removed.

![udp_response_size_distribution.png](https://www.rapid7.com/cdn/images/blt974cde59c3f1e388/683dde842a7686fedebc83c5/udp_response_size_distribution.png)

The services returning a 3,000 bytes in response data are providing a 58x **bandwidth** amplification factor. We didn't track the number of packets returned but using almost any reasonable MTU value will result in a **packet** amplification factor of 2x or 3x. Based on this finding CLDAP is effective as a DRDoS amplification source. Its utility as such will primarily be limited by how prevalent public access to the service remains over time.

### Study success

When the study completed we were able to answer the study's primary questions. LDAP is fairly prevalent on the public Internet. We can identify the software providing most of the LDAP services. We were able to determine that Microsoft ADC and LDS weren't the only software providing CLDAP services though the Internet presence of others was statistically insignificant. We were also able to determine that CLDAP could be used in DRDoS attacks if significant numbers of services remain available on the public Internet.

## Community contributions

Rapid7 is a strong supporter of open source. In addition to well known projects like Metasploit we also open source some of our tools and utilities. Two such tools were used in this study and have been enhanced as a result of it.

### Recog

The initial scans provided us with a corpus of responses that we could use for generating product fingerprints. Reviewing the responses proved to be time consuming but very fruitful. The result was that Rapid7's open source fingerprinting tool [Recog](https://github.com/rapid7/recog) was updated to support LDAP fingerprints and an initial 55 fingerprints were added. Part of the update also included adding support to Recog for building fingerprints and examples with binary strings. This means that server responses can be handed directly to Recog without being processed or stripped if the fingerprint was constructed to support it. This functionality is available in the public [Recog GitHub repo](https://github.com/rapid7/recog) and gems as of version [2.0.22](https://rubygems.org/gems/recog) which was released on August 25, 2016.

### DAP

As part of our study process we often run the scan results through Rapid7's open source [Data Analysis Pipeline (DAP)](https://github.com/rapid7/DAP) tool for data enrichment. This generally includes adding geoIP tagging and protocol decoding if appropriate. DAP can also leverage Recog's version detection for determining the remote service's product, version, and/or operating system. Part of this study included adding support for decoding LDAP protocol responses to DAP. It will now decode a properly formatted LDAP response into a nested JSON structure. This functionality is available in the public [DAP GitHub repo](https://github.com/rapid7/DAP) and gems as of version [0.0.10](https://rubygems.org/gems/dap) which was released on August 2, 2016.

### Example

In the example below DAP is handed JSON formatted data that contains an IP, a base64 encoded server response, the port, and protocol. It returned additional data including version detection (**dap.recog**..), decoded LDAP response (**data.SearchResultEntry** …., **data.SearchResultDone**), and geoIP information (**ip.country** …, i**p.latitude** , **ip.longitude**). At the end the **jq** utility is used to improve the readability of the result.

**Command**
    
    
    bash echo '{"ip": "66.209.xxx.xxx", "data": "MDACAQdkKwQAMCcwJQQLb2JqZWN0Q2xhc3MxFgQDdG9wBA9PcGVuTERBUHJvb3REU0UwDAIBB2UHCgEABAAEAA==", "port": 389, "proto": "tcp"}' | \
    bin/dap json + \
    transform data=base64decode + annotate data=length + \
    recog data=ldap.search_result + \
    decode_ldap_search_result data + \
    remove data + geo_ip ip + \
    geo_ip_org ip + json | jq 
    

**Result**
    
    
    {  
      "ip": "66.209.xxx.xxx",  
      "port": 389,  
       "proto": "tcp",
       "data.length": 64,
       "data.recog.matched": "OpenLDAP",
       "data.recog.service.vendor": "OpenLDAP",
       "data.recog.service.product": "OpenLDAP",
       "data.SearchResultEntry": {
         "objectName": "",
         "PartialAttributes": {
           "objectClass": [
             "top",
             "OpenLDAProotDSE"
           ]
         }
       },
       "data.SearchResultDone": {
         "resultCode": 0,
         "resultDesc": "success",
         "resultMatchedDN": "",
         "resultdiagMessage": ""
       },
       "ip.country_code": "US",
       "ip.country_code3": "USA",
       "ip.country_name": "United States",
       "ip.latitude": "36.xx",
       "ip.longitude": "-115.xxxxxxxxx"
    }
    

This is one of the simpler examples. The responses from Active Directory Controllers contain significantly more information.

## Final thoughts

The results from the study were able to successfully answer the original questions but prompted new ones. Fortunately there is quite a bit of information that remains to be extracted from the data that we have. It is likely that there will be multiple future blog posts on the data, the software and versions identified in it, and information about the individual hosts that can be extracted from it.

Unlike other studies that Project Sonar publishes on [Scans.IO,](https://scans.io/) we have not yet made these data sets available. For those of you that are concerned that your network may be exposing LDAP services I recommend the following:

  * If your organization is a service provider or a company with assigned ASNs you can sign up for free [Shadowserver reports](https://www.shadowserver.org/wiki/pmwiki.php/Services/Reports). The [Shadowserver Foundation](https://www.shadowserver.org/wiki/) scans the Internet for certain services of concern, such as those that could be used in DDoS, and will provide regular reports on these to network owners. Last week they [announced](https://ldapscan.shadowserver.org/) support for discovering and reporting on CLDAP.

  * Use an external service, such as the Rapid7 Perimeter Scanning Service, or an externally hosted scan engine to perform scans of your Internet accessible IP space. Ensure that the ports listed above are included in the scan template. This will provide a more accurate picture of what your organization is exposing to the Internet than that provided by an internally hosted scanner.

  * Review firewall rules to determine if any are overly permissive.




As always, if you are interesting in having Sonar perform additional relevant studies, have interests in related research, or if you have questions, we welcome your comments here as well as by reaching out to us at [[email protected]](/cdn-cgi/l/email-protection#bac8dfc9dfdbc8d9d2fac8dbcad3de8d94d9d5d7).

## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)
  * [Labs](/blog/tag/labs/)