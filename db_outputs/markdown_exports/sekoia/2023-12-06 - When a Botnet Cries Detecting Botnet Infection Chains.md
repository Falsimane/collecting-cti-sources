# When a Botnet Cries: Detecting Botnet Infection Chains

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/when-a-botnet-cries-detecting-botnet-infection-chains
- **Date :** 2023-12-06

---

Infection chains used by commodity malware are constantly evolving and use various tricks to bypass security measures and/or user awareness. BumbleBee, QNAPWorm, IcedID and Qakbot are all often used as first-stage malicious code, allowing other more specific payloads to be dropped.

The following paper was submitted and presented by Erwan Chevalier and Guillaume Couchard (Threat & Detection Research team @ Sekoia.io) at [Virus Bulletin 2023](https://www.virusbulletin.com/conference/vb2023/abstracts/when-botnet-cries-detecting-botnets-infection-chains/) conference and focused on:

  * an overview of the infection chains and common detection methods used against them,
  * an outline of how generic detection rules on these infection chains can help in the fight against botnets,
  * and finally a look at how threat intelligence at scale, combined with the rest, creates a solid defence.



## Welcome to the Jungle of the infection chains

First, we provide our analysis of the evolution in the infection chains of a few of the most common botnets seen in 2022 and early 2023. Our study shows how quickly their techniques evolve. It also cover some detection use cases for these techniques to show how pointless it can be to build overly specific detection rules for these types of threats.

![Welcome to the Jungle of the infection chains](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f3e9a71d422840fb00_6a92a33b693fca262e1b7c9b_6a2a7c6cfe2babd36952c68b.webp)

Welcome to the Jungle of the infection chains

‍

## ISO-LNK infection chain - correlation rule

Secondly, we dig into the creation of more generic rules against known infection chains to detect future threats. Moreover, we show how these rules can be relevant and more effective than classic detection rules, which are focused on one technique inside an infection chain. These generic rules are based on Sigma correlation, which allows the use of multiple Sigma rules, which will be triggered depending on different criteria, such as time range.

![ISO-LNK infection chain - correlation rule](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f3e9a71d422840fb03_6a92a3393e6167cebbf65806_6a2a7c6cfe2babd36952c685.webp)

ISO-LNK infection chain - correlation rule

‍

## Infection chains Pyramid Of Pain 

Finally, and as an opening to further discussions, we detail our own threat intelligence and detection pipeline which, thanks to command-and-control (C2) server tracking, samples configuration extraction and detonation, allows testing detection rules for non regression, all in a common workflow.

![Infection chains Pyramid Of Pain ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5f3e9a71d422840fafd_6a92a33a2e47a1e9fe0df48a_6a2a7c6cfe2babd36952c688.webp)

Infection chains Pyramid Of Pain 

‍

## Want to know more? 

Watch the talk on YouTube...