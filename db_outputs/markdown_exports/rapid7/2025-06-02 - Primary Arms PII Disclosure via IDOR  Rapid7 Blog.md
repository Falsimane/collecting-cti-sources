# Primary Arms PII Disclosure via IDOR | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/08/02/primary-arms-pii-disclosure-via-idor/
- **Date :** 2025-06-02

---

_Update August 2, 2022: This issue was resolved by Primary Arms the same day Rapid7 published this report, and the IDOR vulnerability appears to be no longer exploitable._

The Primary Arms website, a popular e-commerce site dealing in firearms and firearms-related merchandise, suffers from an insecure direct object reference (IDOR) vulnerability, which is an instance of [CWE-639: Authorization Bypass Through User-Controlled Key](https://cwe.mitre.org/data/definitions/639.html). 

Rapid7 is disclosing this vulnerability with the intent of providing information that has the potential to help protect the people who may be affected by it – in this case, Primary Arms users. Rapid7 [regularly conducts](/blog/tag/research/) vulnerability research and disclosure on a wide variety of technologies with the goal of improving cybersecurity. We typically disclose vulnerabilities to the vendor first, and in many cases, vulnerability disclosure coordinators like [CERT/CC](https://cert.org/). In situations where our previous disclosure through the aforementioned channels does not result in progress towards a solution or fix, we disclose unpatched vulnerabilities publicly. In this case, Rapid7 reached out to Primary Arms and federal and state agencies multiple times over a period of months (see “Disclosure Timeline,” below), but the vulnerability has yet to be addressed. 

Vulnerabilities in specific websites are usually unremarkable, don't usually warrant a CVE identifier, and are found and fixed every day. However, Rapid7 has historically publicized issues that presented an outsized risk to specific populations, were popularly mischaracterized, or remained poorly addressed by those most responsible. Some examples that leap to mind are the issues experienced by Ashley Madison and Grindr users, as well as a somewhat similar Yopify plugin issue for Shopify-powered e-commerce sites.

If exploited, this vulnerability has the potential to allow an authorized user to view the personally identifiable information (PII) of Primary Arms customers, including their home address, phone number, and tracking information of purchases. Note that "authorized users" includes all Primary Arms customers, and user account creation is free and unrestricted.

Because this is a vulnerability on a single website, no CVE identifier has been assigned for this issue. We estimate the CVSSv3.1 calculation to be 4.3 ([AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N&version=3.1)) or 5.3 (PR:N) if one considers this vulnerability is exploitable by any person able to complete a web form.

## Product description

Primary Arms is an online firearms and firearms accessories retailer based in Houston, Texas. According to their website, they cater to "firearms enthusiasts, professional shooters, and servicemen and women" and ship firearms to holders of a Federal Firearms License (FFL). The website is built with NetSuite SuiteCommerce.

## Discoverer

This issue was discovered by a Rapid7 security researcher and penetration tester through the normal course of personal business as a customer of Primary Arms. It is being disclosed in accordance with Rapid7's vulnerability disclosure policy.

## Exploitation

An authenticated user can inspect the purchase information of other Primary Arms customers by manually navigating to a known or guessed record sales order URL, as demonstrated in the series of screenshots below.

First, in order to demonstrate the vulnerability, I created an account with the username [[email protected]](/cdn-cgi/l/email-protection), which I call "FakeTod FakeBeardsley."

![image2.png](https://www.rapid7.com/cdn/images/blt90c59a5d941c24b4/683ddbdb4c5a091b145e094c/image2.png)

  


Note that FakeTod has no purchase history:

![image4.png](https://www.rapid7.com/cdn/images/bltc82e126afe74374d/683ddc013323a56d4c80a76b/image4.png)

Next, I'll simply navigate to the URL of a real purchase, made under my "real" account. An actual attacker would need to learn or guess this URL, which may be easy or difficult (see Impact, below). The screenshot below is a (redacted) view of that sales order receipt.

![image1-1.png](https://www.rapid7.com/cdn/images/blt6ef7dcd9c59de637/683ddc242a76864bf5bc82db/image1-1.png)

The redacted URL is hxxps://www.primaryarms.com/sca-dev-2019-2/my_account.ssp#purchases/view/salesorder/85460532, and the final 8-digit salesorder value is the insecure direct object reference. In this case, we can see:

  * Customer name
  * Purchased item
  * Last four digits and issuer of the credit card used
  * Billing address and phone number



Manipulating this value produces other sets of PII from other customers, though the distribution is non-uniform and currently unknown (see below, under Impact, for more information).

If a given salesorder reference includes a shipped item, that tracking information is also displayed, as shown in this redacted example:

![image3.png](https://www.rapid7.com/cdn/images/blt37fb4da2f1944551/683ddc4aabf2ad165a3c4227/image3.png)

Depending on the carrier and the age of the ordered item, this tracking information could then be used to monitor and possibly intercept delivery of the shipped items.

## Root cause

The landing page for primaryarms.com and other pages have this auto-generated comment in the HTML source:
    
    
    <!-- SuiteCommerce [ prodbundle_id "295132" ] [ baselabel "SC_2019.2" ] [ version "2019.2.3.a" ] [ datelabel "2020.00.00" ] [ buildno "0" ] -->
    <!-- 361 s: 25% #59 cache: 4% #17 -->
    <!-- Host [ sh14.prod.bos ] App Version [ 2022.1.15.30433 ] -->
    <!-- COMPID [ 3901023 ] URL [ /s.nl ] Time [ Mon Jul 11 09:33:51 PDT 2022 ] -->
    <!-- Not logging slowest SQL -->
    

This indicates a somewhat old version of SuiteCommerce, from 2019, being run in production. It's hard to say for sure that this is the culprit of the issue, or even if this comment is accurate, but our colleagues at CERT/CC noticed that NetSuite released an update in 2020 that addressed [CVE-2020-14728](https://nvd.nist.gov/vuln/detail/CVE-2020-14728), which may be related to this IDOR.

Outside of this hint, the root cause of this issue is unknown at the time of this writing. It may be as straightforward as updating the local NetSuite instance, or there may be more local configuration needed to ensure that sales order receipts require proper authentication in order to read them.

### Post-authentication considerations

Note that becoming an authenticated user is trivial for the Primary Arms website. New users are invited to create an account, and while a validly formatted email address is required, it is not authenticated. In the example gathered here, the simulated attacker, FakeTod, has the nonexistent email address of [[email protected]](/cdn-cgi/l/email-protection). Therefore, there is no practical difference between an unauthenticated user and an authenticated user for the purpose of exploitation.

## Impact

By exploiting this vulnerability, an attacker can learn the PII of likely firearms enthusiasts. However, exploiting this vulnerability at a reasonable scale may prove somewhat challenging.

### Possible valid IDOR values

It is currently unknown how the salesorder values are generated, as Rapid7 has conducted very limited testing in order to merely validate the existence of the IDOR issue. We're left with two possibilities.

It is the likely case that the salesorder values are sequential, start at a fixed point in the 8-digit space, and increment with every new transaction in a predictable way. If this is the case, exhausting the possible space of valid IDOR values is fairly trivial — only a few seconds to automate the discovery of newly created sales order records, and a few minutes to gather all past records. While limited testing indicates salesorder values are sequential, there are gaps in the sequence, likely due to abandoned and partial orders. We have not fully explored the attack surface of this issue out of an abundance of caution and restraint.

In the worst case (for the attacker), the numbers may be purely random out of a space of 100 million possibles. This seems unlikely according to Rapid7's limited testing. If this is the case, however, exhausting the entire space for all records would take about two years, assuming an average of 100 queries per second (this probing would be noticeable by the website operators assuming normal website instrumentation).

The truth of the salesorder value generation is probably somewhere closer to the former than the latter, given past experience with similar bugs of this nature, which leads us to this disclosure in the interest of public safety, documented in the next section.

### Possible attacks

We can imagine a few scenarios where attackers might find this collection of PII useful. The most obvious attack would be a follow-on phishing attack, identity theft, or other confidence scam, since PII is often useful in executing successful social engineering attacks. An attacker could pose as Primary Arms, another related organization, or the customer and be very convincing in such identity (to a third-party) when armed with the name, address, phone number, last four digits of a credit card, and recent purchase history.

Additionally, typical Primary Arms customers are self-identified firearms owners and enthusiasts. A recent data breach in June of 2022 involving [California Conceal Carry License](https://www.jdsupra.com/legalnews/california-department-of-justice-3366057/) holders caused a stir among firearms enthusiasts, [who worry](https://thereload.com/new-california-ag-website-leaks-massive-trove-of-gun-owner-private-information) that breach would lead to "increase the risk criminals will target their homes for burglaries."

Indeed, if it is possible to see recent transactions (again, depending on how salesorder values are generated), especially those involving FFL holders, it may be possible for criminals to intercept firearms and firearms accessories in transit by targeting specific delivery addresses.

Finally, there is the potential that domestic terrorist organizations and [foreign intelligence operations](https://www.opensecrets.org/news/2021/10/russia-pouring-millions-into-russian-foreign-influence-kremlin-propaganda-targeting-the-us/) could use this highly specialized PII in recruiting, disinformation, and propaganda efforts.

## Remediation

As mentioned above, it would appear that only Primary Arms is in a position to address this issue. We suspect this issue may be resolved by using a more current release of NetSuite SuiteCommerce. A similar e-commerce site, using similar technology but with a more updated version of SuiteCommerce, appears to not be subject to this specific attack technique, so it's unlikely this is a novel vulnerability in the underlying web technology stack.

Customers affected by this issue are encouraged to try to contact Primary Arms, either by email to [[email protected]](/cdn-cgi/l/email-protection#e38a8d858ca393918a8e82919a82918e90cd808c8e), or by calling customer service at +1 713.344.9600.

## Disclosure timeline

 _Update:_ Since the publication of this report, Primary Arms reached out to Rapid7 to confirm receipt of the original report and implemented a fix resolving the IDOR issue.

  * **May 2022** \- Issue discovered by a Rapid7 security researcher
  * **Mon, May 16, 2022** \- Initial contact to Primary Arms at [[email protected]](/cdn-cgi/l/email-protection)
  * **Wed, May 25, 2022** \- Attempt to contact Primary Arms CTO via guessed email address
  * **Wed, May 25, 2022** \- Internal write-up of IDOR issue completed and validated
  * **Thu, May 26, 2022** \- Attempt to contact Primary Arms CEO via guessed email address
  * **Tue, May 31, 2022** \- Called customer support, asked for clarification on contact, reported issue
  * **Thu, Jun 1, 2022** \- Notified CERT/CC via [[email protected]](/cdn-cgi/l/email-protection#2d4e485f596d4e485f5903425f4a) asking for advice
  * **Fri, Jun 10, 2022** \- Opened a case with CERT/CC, VRF#22-06-QFRZJ
  * **Thu, Jun 16, 2022** \- CERT/CC begins investigation and disclosure attempts, VU#615142
  * **June-July 2022** \- Collaboration with CERT/CC to validate and scope the issue
  * **Mon, Jul 11, 2022** \- Completed disclosure documentation presuming no contact from Primary Arms
  * **Tue, Jul 12, 2022** \- Sent a paper copy of this disclosure to Primary Arms via certified US mail, tracking number: 420770479514806664112193691642
  * **Thu, Jul 14, 2022** \- Disclosed details to the Texas Information Sharing and Analysis Organization ([TX-ISAO](https://dir.texas.gov/information-security/tx-isao)), Report #ISAO-CT-0052
  * **Mon, Jul 18, 2022** \- Paper copy received by Primary Arms
  * **Tue, Aug 2, 2022** \- This public disclosure
  * **Tue, Aug 2, 2022** \- Primary Arms acknowledges the reported issue and fixes the IDOR vulnerability

  


## Article tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Research](/blog/tag/research/)