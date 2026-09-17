# Conti Ransomware Group Internal Chats Leaked | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/03/01/conti-ransomware-group-internal-chats-leaked-over-russia-ukraine-conflict/
- **Date :** 2025-06-02

---

**_UPDATE:_**_As of March 2, 2022, Conti began taking down exposed infrastructure as a result of the chat disclosure. At that time, we assessed that due to their sophisticated capability, deep funding, and quick recovery from exposed infrastructure in November 2021, they remained an active and significant threat. As of March 9, 2022, our threat intelligence team has observed a resumption of normal operations from Conti._

On February 27, Twitter user [@ContiLeaks](https://twitter.com/contileaks) released a trove of chat logs from the ransomware group, Conti – a sophisticated ransomware group whose manual was publicly [leaked last year](https://blog.talosintelligence.com/2021/09/Conti-leak-translation.html). Ahead of the chat log disclosures, Conti pledged their support for the Russian Government following the Russian invasion of Ukraine. However, a number of members sided with Ukraine, causing strife within the organization. Two days later, Conti posted a second message revising their statement to condemn the war and to strike back only if Russian critical infrastructure is targeted.

![image3.png](https://www.rapid7.com/cdn/images/blt963ccc5b3f5d74e1/683de894aaf620341979e0b7/image3.png) ![image1.jpg](https://www.rapid7.com/cdn/images/blt1326fac6165df66f/683de8a9590d7fbe80de1e24/image1.jpg) ![image4.png](https://www.rapid7.com/cdn/images/blte1cda4323cf1c54a/683de8bf4c5a0951285e0dbb/image4.png)

At the time of the leak, a file titled `1.tgz` was released on the “AnonFiles” website, containing 14 megabytes of chat logs across 393 JSON files. However, some of the messages were encrypted and could not be read, so the information provided is necessarily incomplete. The remaining files contained internal Conti communications, screenshots of tools, and discussions of their exploits and design processes. 

On February 28 and March 1, a bevy of additional files were posted, along with a number of pro-Ukraine tweets. Among both sets of leaked messages, there were a number of usernames and passwords for a variety of accounts. Additionally, user @ContiLeaks shared access details for a number of alleged Conti command and control servers, plus storage servers for stolen files. However, we have not accessed any of the data necessitating access to remote servers or the use of usernames and passwords, and we strongly recommend against doing so. 

@ContiLeaks also shared a file that they purport to be the source code for the Conti ransomware but declined to share the password except with “trusted parties.” @ContiLeaks did, however, name one alleged Conti developer, providing their email address and Github. The scale of the leaked information suggests that the leaker is likely either a very senior member of the group or a coalition of disgruntled Conti affiliates.

## Conti is a business – and a well-funded one

Much of the discussion within the chat logs concerns fairly mundane things – interviewing potential operators of the group, payment for services, out-of-office messages, gossip, and discussions of products. Based on the leaked chats, the Conti interview process actually looks a lot like a standard technical interview, with coding exercises to be performed hosted on public code repositories, salary negotiations, and the status of ongoing products. 

In addition to other financial information related to specific actors, the leaked chats have revealed Conti’s primary Bitcoin address, which contains over **two billion USD** as of February 28, 2022. Moreover, a conversation on April 9, 2021 between “mango” and “johnyboy77” indicates Russian FSB involvement in some portion of their funding and that the FSB were interested in files from the media outlet Bellingcat on “Navalny” – an apparent reference to Alexei Navalny, the currently imprisoned opposition leader in Russia.

## Conti development

Conti seems to operate much like a software company – the chat logs disclose concerns with the development of specific features for targets and a particular difficulty in encrypting very large files. The Conti team also attempted to get demos of popular endpoint detection software with the intent to develop their malware to avoid detection.

Two of the actors, “lemur” and “terry” shared phishing templates (included verbatim in Appendix B at the end of this post) to be used against potential targets. Conti gains initial access in many ways, with phishing a popular line of attack due in part to its relatively high efficacy and low cost. Conti often uses phishing emails to establish a presence on targeted networks.

A screenshot of the Conti control panel was also leaked, showing a number of compromised hosts and a breakdown of the operating systems, antiviruses, user rights, and detailed information about the infected assets.

![image2.png](https://www.rapid7.com/cdn/images/blt0e00c34cba13045d/683de8d6aaf6207f8879e0d4/image2.png)

Further discussions detailed the use of infrastructure against targets, disclosing a number of both known and unknown Conti command and control domains. At the time of this post, only a small number of the previously unknown command and control domains appear to be active. Conversations between two operators, “Stern” and “Bentley” discuss the use of third parties for malicious documents, favoring certain providers over others. They also discuss logistics for how to deliver ransomware without being detected by dynamic analysis. In a conversation between the two back in June of 2021, Stern discloses that Conti wants to start their own cryptocurrency but does not know who to work with. There is no evidence that anything came of this desire, and Conti continues to use Bitcoin for their ransoms. 

## Other groups assert they are strictly business

In stark contrast to Conti, other groups have made it clear to the public that despite their “business model,” they take no public stance on this crisis. LockBit is remaining aloof from the conflict and made it clear that they intend to operate as usual. Although it is believed that LockBit is a Russian organization, they assert that “we are all simple and peaceful people, we are all Earthlings,” and “for us it is just business and we are all apolitical.” Another ransomware group, ALPHV, claims to be “extremely saddened” by Conti’s pledge of support and condemns Conti. Their message concludes, “The Internet, and even more so its dark side, is not the place for politics.”

## Rumors of Conti’s demise have been greatly exaggerated

Conti’s payment and “support” portal is still live, even following the infighting and leaks. Conti has repeatedly proven to be one of the most capable ransomware actors and these chats indicate that the group is well-organized and still very well-funded despite the schism. Any suggestion that these leaks spell the end for Conti is overstated, and we expect that Conti will continue to be a powerful player in the ransomware space.

## What you can do

We are keeping an eye on dark web activity related to Conti and other ransomware groups and want to reiterate the following steps for protecting yourself from ransomware:  


  * User education, especially related to well-crafted phishing campaigns
  * Asset and vulnerability management, including reducing your [external attack surface](/fundamentals/external-attack-surface-management-easm/)
  * Multi-factor authentication  




Additionally, it is worth ensuring that you are well-guarded against the exploits and malware commonly used by Conti (vulnerabilities provided in Appendix A at the end of this post). Furthermore, security teams should also take some time to review CISA’s recent report on the group. For further discussion on how to protect yourself from ransomware, see our [ransomware prevention solution](/solutions/ransomware-prevention/).   


## Appendix A – Conti known exploited vulnerabilities

CVE-2017-0143, CVE-2017-0144, CVE-2017-0145, CVE-2017-0146 (MS17-010; EternalBlue/EternalSynergy/EternalChampion)

CVE-2020-1472 (ZeroLogon)

CVE-2021-34527 (PrintNightmare)

CVE-2021-44228 (Log4Shell)

CVE-2021-34473, CVE-2021-34523, CVE-2021-31207 (ProxyShell/ProxyLogon)

## Appendix B – Phishing templates

{Greetings|Hello|Good afternoon|Hi|Good day|Greeting|Good morning|Good evening}!  
{Here|Right here|In this letter|With this letter} we {send|direct} you {all the|all the necessary|the most important} {documentation|papers|documents|records} {regarding|concerning|relating to} your {payment|deposit payment|last payment} {#|№|No. }НОМЕР ПЛАТЕЖА, right {as we|as we have} {discussed|revealed} {not so long ago|not too long ago|recently|just recently|not long ago}. Please {review the|check the|take a look at} аll {necessary|required|important} {information|data} in the {file attached|attached file}.  
Т: {Payment|Deposit payment} {invoice|receipt} {#|№|No. }НОМЕР ИНВОЙСА {prepared|formed}  
D: {payment|deposit|dep|paym}_{info|information|data}

{Hello|Greetings|Greetings to you|Good evening|Good morning|Good day|Good afternoon}{!|,|.|}  
Your {order|purchase order|online order} was {successfully|correctly|timely} {paid|compensated|covered} by you {yesterday|today|recently}. Your {documentation|docs|papers} and {bank check|receipt|paycheck} {can be found|are listed} in the {attached file|file attached}.  
T: {Invoice|Given invoice|Bill} {we|we have|we’ve} {sent|mailed|delivered} to you {is paid|is covered|is processed}.  
D: {Purchase order|Order} {verification|approval}

{Hello|Greetings|Greetings to you|Good evening|Good morning|Good day|Good afternoon}{!|,|.|}  
{We are contacting you to|This is to|This mail is to} {notify|remind} you {about|regarding} your {debt|unprocessed payment} for {our last|the recent|our recent} {contract|agreement}. All {compensation|payment} {data|information}, {agreement|contract} and prepared legal {documents|documentation} {can be found|are located} in the {file attached|attached file}.  
T: {Missing|Additional} payment {information|details|info} reminder  
D: {Contract|Agreement} 2815/2 {case|claim}

{Hello|Greetings|Greetings to you|Good evening|Good morning|Good day|Good afternoon}{!|,|.|}  
{Your payment|Your advance payment|Your obligatory payment|Payment you sent|Payment you made} was {successfully|correctly|timely|properly} {achieved|accomplished|approved|affirmed|received|obtained|collected|processed}. All {required documentation|necessary documents|important documentation|documents you need|details that can be important|essential documents} {can be found|you can find} in the {attached file|file attached}.  
T: {Invoicing|Invoice|Agreement|Contract|Payment} {info|data|information|details}  
D: {Receipt|Bill} {id|ID|Number|number|No.|No.|No|#|##} 3212-inv8

{Greetings|Hello|Good day|Good afternoon}{!|,|}  
{Thank you for|We are thankful for|We are grateful for|Many thanks for} {your|your recent} {on-line order|purchase order|order}. {We|Our financiers have|Our team has|We have|Our shop has} {received|collected|processed|checked} your {payment|advance payment|money transfer|funds transfer} НОМЕР ПЕРЕВОДА. Now we {are and ready to|begin to} {pack|prepare|compose} your {shipment|order|box}. Your {parcel|packet|shipment|box} {will|is going to|would} {arrive|be delivered} to {you|your residence} within {4|5|6|four|five|six} {days|business days}.  
{Total|Full|Whole} {order|purchase|payment} sum: СУММА  
You {can find|will find} {all|full} {relative information|order info|order and payment details} and your {receipt|check} НОМЕР ЧЕКА {in|in the} {attached file|file attached}.  
{Thank you!|Have a nice day!}  
ТЕМЫ: Your {order|purchase|on-line order|last order} НОМЕР ЗАКАЗА payment {processed|obtained|received}  
АТТАЧИ:  
ord_conf  
full.details  
compl_ord_7847  
buyer_auth_doc  
info_summr  
customer_docs  
spec-ed_info

  
 _**Additional reading**_

  * [ _Russia/Ukraine Conflict: What Is Rapid7 Doing to Protect My Organization?_](/blog/post/2022/02/25/russia-ukraine-conflict-what-is-rapid7-doing-to-protect-my-organization/)
  * [_Staying Secure in a Global Cyber Conflict_](/blog/post/2022/02/25/russia-ukraine-staying-secure-in-a-global-cyber-conflict/)
  * [ _Prudent Cybersecurity Preparation for the Potential Russia-Ukraine Conflict_](/blog/post/2022/02/15/prudent-cybersecurity-preparation-for-the-potential-russia-ukraine-conflict/)

  


## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)