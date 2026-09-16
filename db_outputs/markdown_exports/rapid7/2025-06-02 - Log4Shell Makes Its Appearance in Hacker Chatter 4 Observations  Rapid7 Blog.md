# Log4Shell Makes Its Appearance in Hacker Chatter: 4 Observations | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/12/14/log4j-makes-its-appearance-in-hacker-chatter-4-observations/
- **Date :** 2025-06-02

---

It's been a long few days as organizations' security teams have worked to map, quantify, and mitigate the immense risk presented by the [Log4Shell vulnerability within Log4j](/blog/post/2021/12/10/widespread-exploitation-of-critical-remote-code-execution-in-apache-log4j/). As can be imagined, cybercriminals are working overtime as well, as they seek out ways to exploit this vulnerability.

The Rapid7 Threat Intelligence team is tracking the attacker's-eye view and the related chatter on the clear, deep, and dark web within our [Threat Intelligence platform](/platform/threat-intelligence-tip/). Here are 4 observations based on what we've seen at the onset of the identification of CVE-2021-44228.

## 1\. We see a spike in hacker chatter and security researchers' publications about Log4j.

![image--1---1-.png](https://www.rapid7.com/cdn/images/blt495e413792f4a0d9/683ddf50ca9dfcb9cb52662c/image--1---1-.png)

Increased hacker chatter is a key indicator of an emerging threat that security teams must account for. Clearly the spike here is no surprise – however, it is important to monitor and understand the types and scope of the chatter in order to get a clear picture of what's on the horizon.

## 2\. Hackers – specifically from the Russian, Chinese, and Turkish communities – show interest in the vulnerability and are actively sharing scanners and exploits.

![image--3---1-.png](https://www.rapid7.com/cdn/images/blte2f579f2fa0d6dfb/683ddf75ca9dfc6da652663c/image--3---1-.png)

The following two screenshots show that bad actors have already developed and shared proof of concepts exploiting the vulnerability in Log4j. They also show the extent to which this vulnerability impacts user communities such as PC gamers, social media users, Apple/iCloud customers, and more.

![gaMakuZonQaJeuLsXz3cWSrDRO6If3MPsgUIkj3iGS1rjLG2X5NJ1FuhbBBwkm3BHlQv1bdd16Ect_rI6cuglprD3ZEzSn-wFEPiALTXzeA3bhYna8dnEnL2W0ZmtXAUeRzaGSj7dMmN.png](https://www.rapid7.com/cdn/images/bltd335c10c55b0c5fb/683ddf9870aa9569c5fe3022/gaMakuZonQaJeuLsXz3cWSrDRO6If3MPsgUIkj3iGS1rjLG2X5NJ1FuhbBBwkm3BHlQv1bdd16Ect_rI6cuglprD3ZEzSn-wFEPiALTXzeA3bhYna8dnEnL2W0ZmtXAUeRzaGSj7dMmN.png) ![XdrOplpt_joV9HDI6J7FZj4_35JbmkiUUJ9KRTY6Ohhp-DZnlBjb0ztWEPANZuy6NLfPoiHYXlOLJ5L8Ej4QiQBMa6PW2zqkbJ9xwqKrQ9xOC98WSXpbPheScvx-TITZ6FTV4KSqd45i.png](https://www.rapid7.com/cdn/images/blt2ac39f75c97d04e5/683ddfbdff6aa9a2af0ea81a/XdrOplpt_joV9HDI6J7FZj4_35JbmkiUUJ9KRTY6Ohhp-DZnlBjb0ztWEPANZuy6NLfPoiHYXlOLJ5L8Ej4QiQBMa6PW2zqkbJ9xwqKrQ9xOC98WSXpbPheScvx-TITZ6FTV4KSqd45i.png)

## 3\. Code with a proof of concept for the exploit has been published on GitHub.

![image--4---1-.png](https://www.rapid7.com/cdn/images/blt46dc3279d39c2110/683ddfeb2a76862fa3bc8441/image--4---1-.png)

The underground cybercrime community functions like any other business model, but what sets it apart is the spirit with which bad actors share their work for mass consumption. The example above is completely open and free for anyone to access and utilize.

## 4\. Various scanners were published on GitHub to identify vulnerable systems.

Scanners are the cybercriminal's tool of choice for finding specific vulnerabilities in networks communicating via the internet. Using a scanner, any company — regardless of size — can be a target.

![Untitled--35-.png](https://www.rapid7.com/cdn/images/bltd71a4a09e768610e/683de019543b8d83aebf115b/Untitled--35-.png) ![image--5---1-.png](https://www.rapid7.com/cdn/images/bltb51b206dd4376edf/683de03caaf62058bc79de76/image--5---1-.png) ![t8hCwTxT3RS6zRgIyIrSScwjJ2fV2CV19bzTh9ufApos9E3O5Yyk7gWauF5DTzOheyEIjNLE1R0Le5WwDD-4nbG1yTbndOW8Z8e3mJj899oSl3iIo56UOIY-SIuJupiO6_3CGOtwx4C3.png](https://www.rapid7.com/cdn/images/blt3eb4879f8ebb29d4/683de067590d7f570dde1b9a/t8hCwTxT3RS6zRgIyIrSScwjJ2fV2CV19bzTh9ufApos9E3O5Yyk7gWauF5DTzOheyEIjNLE1R0Le5WwDD-4nbG1yTbndOW8Z8e3mJj899oSl3iIo56UOIY-SIuJupiO6_3CGOtwx4C3.png)

## While others look inside, we look outside

The bottom line is that threat actors are showing great interest in Log4j within underground communities, and they are leveraging these communities to share information and experience regarding exploiting this vulnerability. That emphasizes the need to quickly patch this vulnerability, before multiple cybercriminals put their hands on an exploit and start to utilize it on a large scale.

## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)