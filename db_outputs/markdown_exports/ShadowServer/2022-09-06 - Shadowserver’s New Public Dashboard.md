# Shadowserver’s New Public Dashboard

- **Source :** ShadowServer
- **URL :** https://www.shadowserver.org/news/shadowservers-new-public-dashboard/
- **Date :** 2022-09-06

---

# Shadowserver’s New Public Dashboard

September 6, 2022

Keen watchers of Shadowserver will know that we have our own [unique view of the Internet](https://www.shadowserver.org/what-we-do/) – informed by our daily worldwide scanning for exposed and abusable services, our large honeypot sensor networks that are used for detecting attacks, our extensive botnet sinkholing efforts, and many other data streams that we collate as part of our public benefit mission.

We have a long history of providing [high quality, actionable cyber threat intelligence](https://www.shadowserver.org/what-we-do/network-reporting/) to network owners and National CSIRTs globally for free, every day. These technical data feeds are aimed at helping Internet defenders identify and remediate risks within their network/country that criminals seek to exploit, helping to raise the bar on cyber security globally.

We have always had the ambition of providing a graphical way to explore some of our extensive data sets. Unfortunately, new and improved data collection projects or support for the latest cybercrime disruption efforts have meant that we never actually made such a system available.

However, thanks to the generous support of the [UK Foreign, Commonwealth & Development Office (FCDO)](https://www.gov.uk/government/organisations/foreign-commonwealth-development-office), we are super excited to finally announce the launch of our new **Shadowserver Public Dashboard** :

<https://dashboard.shadowserver.org>

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_Home-1024x559.png)](/wp-content/uploads/2022/09/Dashboard_Home.png)

Our new Dashboard lets you explore some of the many facets of our Internet-scale data sets and learn more about how Shadowserver sees the state of cyber security globally, over a rolling period of the last two years. The Dashboard is based on aggregated country level data – no individual IP addresses or personally identifying information (PII) is included.

You can use our Dashboard to start with a global view, and then drill down into observations about a particular threat, or to compare statistics about two countries side by side. Initial filters for Sinkhole, Scan, Honeypot, Distributed Denial of Service (DDoS) and Industrial Control System / Operational Technology (ICS/OT) based data sets are included on the left navigation menu of the home page. There are various forms of data visualization available through the top navigation menu, such as time series graphs, world maps, region maps, treemaps and bubblecharts/tagclouds. Each data visualization should generate a unique URL for your query, so you can share links that easily recreate the same information and presentation style for others to view too, or for when you return to drill down further.

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_ICS_visualization-2-1024x711.png)](/wp-content/uploads/2022/09/Dashboard_ICS_visualization-2.png)

Our ambition for our new Dashboard is to empower security researchers, National CSIRTs, policy makers, journalists in the news media and other interested parties to use Shadowserver’s unique vantage point and extensive aggregated data sets as a public resource to help drive forward research and raise greater awareness of cyber security threats. With attribution, you can freely use our Dashboard for research purposes and to inform policy making, or to educate the public through news articles, but you are not permitted to scrape or resell the data. Please [contact us](https://www.shadowserver.org/contact/) if you have questions about [licensing](https://www.shadowserver.org/privacy-and-terms/#terms-of-service).

We will be posting a series of follow up articles that demonstrate how to use the new Dashboard effectively, and we will use Dashboard URLs to illustrate future blog posts and tweets.

To illustrate some of the new capabilities and data sets, here are some examples:

1) The impressive impact of the [Emotet botnet takedown](https://twitter.com/Shadowserver/status/1354407473898278915) on the number of daily infected unique victim IP addresses in March 2021:

[https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2021-03-25&d2=2021-06-10&source=sinkhole%2Bsinkhole6&tag=emotet&style=stacked](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=other&d1=2021-03-25&d2=2021-06-10&source=sinkhole%2Bsinkhole6&tag=emotet&style=stacked)

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_Emotet_sinkhole-1-1024x606.png)](/wp-content/uploads/2022/09/Dashboard_Emotet_sinkhole-1.png)

The distribution of infected Emotet victim IP addresses by country at the point of initial sinkholing:

[https://dashboard.shadowserver.org/statistics/combined/visualisation/?date_range=other&d1=2021-03-25&d2=2021-03-26&source=sinkhole%2Bsinkhole6&tag=emotet&dataset=unique_ips&group_by=geo&count_as=avg&style=bubble_diagram](https://dashboard.shadowserver.org/statistics/combined/visualisation/?date_range=other&d1=2021-03-25&d2=2021-03-26&source=sinkhole%2Bsinkhole6&tag=emotet&dataset=unique_ips&group_by=geo&count_as=avg&style=bubble_diagram)

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_Emotet_sinkhole_locations-1024x606.png)](/wp-content/uploads/2022/09/Dashboard_Emotet_sinkhole_locations.png)

2) Good news! The amount of exposed Zimbra Collaboration Suite instances vulnerable to CVE-2022-27925 / CVE-2022-37042 is decreasing. We[ started reporting these vulnerable instances](https://twitter.com/Shadowserver/status/1558861087491112961) on 2022-08-13:

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_Zimbra-1-1024x606.png)](/wp-content/uploads/2022/09/Dashboard_Zimbra-1.png)

Location of vulnerable Zimbra Collaboration Suite systems, treemap by country:

[https://dashboard.shadowserver.org/statistics/combined/tree/?day=2022-08-31&source=http_vulnerable&tag=zimbra%3Bcve-2022-37042&geo=all&data_set=count](https://dashboard.shadowserver.org/statistics/combined/tree/?day=2022-08-31&source=http_vulnerable&tag=zimbra%3Bcve-2022-37042&geo=all&data_set=count)

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_Zimbra_locations-1-1024x606.png)](/wp-content/uploads/2022/09/Dashboard_Zimbra_locations-1.png)

Read more about recent Zimbra ZCS CVE-2022-27925 and CVE-2022-37042 here: <https://www.cisa.gov/uscert/ncas/alerts/aa22-228a>

Let’s push to reduce the amount of vulnerable instances even further!

3) Mirai/IoT related botnet infections are on the rise again. What is the root cause and how can we work together to more effectively combat these threats?

[https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=180&source=honeypot&tag=mirai&style=stacked](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=180&source=honeypot&tag=mirai&style=stacked)

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_Mirai-1024x606.png)](/wp-content/uploads/2022/09/Dashboard_Mirai.png)

World map of detected Mirai bot locations:

[https://dashboard.shadowserver.org/statistics/combined/map/?map_type=std&day=2022-08-31&source=honeypot&tag=mirai&geo=all&data_set=count&scale=log](https://dashboard.shadowserver.org/statistics/combined/map/?map_type=std&day=2022-08-31&source=honeypot&tag=mirai&geo=all&data_set=count&scale=log)

[![](https://www.shadowserver.org/wp-content/uploads/2022/09/Dashboard_Mirai_map-1-1024x639.png)](/wp-content/uploads/2022/09/Dashboard_Mirai_map-1.png)

As you can see, these examples are only the tip of the iceberg. Petabytes of global cyber threat data, including some unique data sets, are being aggregated and made available to the public for interactive exploration and visualization – for the first time. We hope you will be as excited about the new Shadowserver Dashboard as we are, and we look forward to hearing about any interesting trends or observations you find in the data.

Please [contact us](https://www.shadowserver.org/contact/) or [engage us on Twitter](https://twitter.com/Shadowserver) if you have any questions or insights to share, and do let the [UK FCDO know](https://twitter.com/LondonCyber) if you find our public Dashboard to be useful – we really appreciate their continued support for our free public benefit services.

We are always interested in collaboration and will be adding more data sets to the Dashboard over time, as it becomes our go-to landing place for exploring data about new and emerging threats. We hope to eventually provide our constituents with authenticated access to more granular views of our data about their own individual networks/country through expanded, private dashboards. Join our [new Shadowserver Alliance](https://www.shadowserver.org/partner/) to help influence future research direction and gain additional behind the scenes insight on threats to global cyber security.

If you operate a network or CSIRT and don’t already subscribe to Shadowserver’s [free daily network reports](https://www.shadowserver.org/what-we-do/network-reporting/), please [sign up here](https://www.shadowserver.org/what-we-do/network-reporting/get-reports/).

  * [Botnets](/topics/botnets/)
  * [Bots](/topics/bots/)
  * [DDoS](/topics/ddos/)
  * [Geo Locations](/topics/geo-locations/)
  * [Honeypots](/topics/honeypots/)
  * [Scans](/topics/scans/)
  * [Shadowserver](/topics/shadowserver/)
  * [Sinkholes](/topics/sinkholes/)
  * [Statistics](/topics/statistics/)
  * [Takedowns](/topics/takedowns/)
  * [Threat Intelligence](/topics/threat-intelligence/)



[« Back to News & Insights](/news-insights/)

### Recent Articles

  * #### [Shadowserver 2025: Highlights of the Year in Review](/news/shadowserver-2025-highlights-of-the-year-in-review/)

September 7, 2026

A review of Shadowserver’s 21st year as the world’s largest provider of free, timely, actionable, daily cyber threat… [Read more »](/news/shadowserver-2025-highlights-of-the-year-in-review/)

  * #### [Shadowserver Critical Community Infrastructure Cyber Resilience Project](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

August 5, 2026

The Shadowserver Critical Community Infrastructure (CCI) Project is designed to improve the cybersecurity posture of essential… [Read more »](/news/shadowserver-critical-community-infrastructure-cyber-resilience-project/)

  * #### [StealC Historical Bot Infection Special Report](/news/stealc-historical-bot-infection-special-report/)

June 25, 2026

On Wednesday 24th June 2026, international law enforcement partners announced additional successful cyber crime disruption… [Read more »](/news/stealc-historical-bot-infection-special-report/)

  * #### [SocGholish Compromised WordPress Sites Special Report](/news/socgholish-compromised-wordpress-sites-special-report/)

June 18, 2026

On Thursday 18th June 2026, international law enforcement partners announced another successful cyber crime disruption action as… [Read more »](/news/socgholish-compromised-wordpress-sites-special-report/)