# Chinese Darcula Phishing Kit Harvesting Taiwanese Credit Card Data - TeamT5

- **Source :** teamt5
- **URL :** https://teamt5.org/en/posts/chinese-darcula-phishing-kit-harvesting-taiwanese-credit-card-data/
- **Date :** 2026-09-07

---

Threat Intelligence

SubscribeRSS

# Chinese Darcula Phishing Kit Harvesting Taiwanese Credit Card Data

2026.09.07Cyber Threat Intelligence

Share: 

## Campaign Snapshot

  * Campaign Timeframe: Jan 2026 to May 2026

  * Delivery Methods: Phishing

  * Victim Country: Taiwan

  * Phishing Kit: Darcula

  * Actor Assessment: Simplified Chinese Users




## Executive Summary

In May, we intercepted a phishing campaign harvesting Taiwanese credit card data. The threat actor leveraged a fake Taiwanese e-invoice platform to lure victims into submitting their credit card information through phishing pages. Our technical analysis found that the campaign encrypts victim data using the Rabbit encryption algorithm. The Rabbit encryption algorithm is the same encryption mechanism previously observed in the Darcula phishing kit. Based on this technical overlap, we assess with high confidence that the campaign was conducted using the Darcula phishing kit. We list all the malicious URLs in the IoCs section below.

## Campaign Details

### 1\. Phishing Emails

In this campaign, the actor delivered the phishing emails from a compromised email account belonging to Korea University[1]. In these emails, the actor impersonated the Taiwanese e-commerce platform MOMO and instructed victims to click the malicious links to verify their e-invoice. The actor prepared several malicious URLs that direct victims to the fake e-invoice platform:

  * `https://0023.ehrscripts.com/`

  * `https://av11.pdjekqa.online/`

  * `https://einvoiceg.com/gov/`

  * `https://einvoicegs.com/gov/`




### 2\. Fake Taiwanese E-invoice Platform

At the time of our analysis, we were only able to access two URLs `https://einvoiceg.com/gov/` and `https://einvoicegs.com/gov/`. The two URLs show the page identical to the legitimate e-invoice platform. However, the icon of the page displays the logo of Taiwanese commercial bank CTBC rather than the logo of Ministry of Finance used by the legitimate site.

![](https://uploads.teamt5.org/upload/original/912x460/pic1_chinese-darcula-phishing-kit-harvesting-taiwanese-credit-card-data.png)

Figure 1: The fake e-invoice platform   


While the fake e-invoice platform requires a phone number to sign in, we found that any number entered resulted in a successful login. Once logged in, the page requests credit card information so that the e-invoice can be linked with the credit card. This lure is effective because e-invoices in Taiwan are eligible for a government-run lottery, and residents routinely retain their invoices in the hope of winning a prize.

![](https://uploads.teamt5.org/upload/original/912x460/pic2_chinese-darcula-phishing-kit-harvesting-taiwanese-credit-card-data.png)

Figure 2: The fake platform that requires phone number to sign in   


Our research shows that the phishing page performs basic validation of the credit card information. Notably, the error messages shown for invalid input are displayed in Simplified Chinese.

![](https://uploads.teamt5.org/upload/original/912x460/pic3_chinese-darcula-phishing-kit-harvesting-taiwanese-credit-card-data.png)

Figure 3: Simplified Chinese error messages   


After the credit card information is submitted, the page redirects to a second page requesting two-factor authentication (2FA) information. We assess that this data is likely synchronized to the phishing kit's backend server in near real time.

![](https://uploads.teamt5.org/upload/original/912x460/pic4_chinese-darcula-phishing-kit-harvesting-taiwanese-credit-card-data.png)

Figure 4: The page requesting 2FA authentication

### 3\. Relations to Darcula

Our technical analysis of the phishing kit’s source code reveals that the victim data is encrypted with the Rabbit algorithm. The algorithm has been previously documented in the Darcula analysis.[2] Specifically, we identify a file `app/chunk/DgZYu39z.js` that contains an encryption and decryption mechanism sharing the same structure as the Darcula phishing kit. Therefore, we assess with high confidence that the campaign was deployed using the Darcula phishing kit. Notably, the actor may have used AI during development, as we identified numerous Simplified Chinese strings along with emoji characters in the source code.

### Footnotes

[1] Korea University <https://www.korea.ac.kr/sites/ko/index.do>

[2] Exposing Darcula: a rare look behind the scenes of a global Phishing-as-a-Service operation <https://www.mnemonic.io/resources/blog/exposing-darcula-a-rare-look-behind-the-scenes-of-a-global-phishing-as-a-service-operation>

2026.09.07Cyber Threat Intelligence

Share: 

![](https://teamt5.org/en/posts/chinese-darcula-phishing-kit-harvesting-taiwanese-credit-card-data/)