# Threat Intelligence Foundations: Crawl, Walk, Analyze - Part 3 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/03/11/threat-intelligence-foundations-crawl-walk-analyze-part-3/
- **Date :** 2025-06-02

---

_This is the third post in a three-part series on threat intelligence foundations, discussing the fundamentals of how threat intelligence can be used in security operations. Here's_[ _Part 1_](/blog/post/2016/03/09/threat-intelligence-foundations-crawl-walk-analyze-part-1/) _and_[ _Part 2_](/blog/post/2016/03/10/threat-intelligence-foundations-crawl-walk-analyze-part-2/) _._

## Intelligence Analysis in Security Operations

In the first two parts of this series we talked about frameworks for understanding and approaching intelligence: the levels of intelligence (strategic, operational, tactical) as well as the different types of intelligence (technical, current, long-term, etc). Regardless of the level or type of intelligence, the consistent theme was the need for analysis. Analysis is the core of intelligence, it takes data and turns it into intelligence that we can use to help us make informed decisions about complicated issues. 

### Analysis: The Missing Piece

I recently gave a talk at RSA where I compared the traditional intelligence cycle: 

to what the intelligence cycle often looks like in cyber [threat intelligence](/fundamentals/what-is-threat-intelligence/): 

We are good at collection and processing, and we are good at dissemination, however we tend to leave a lot of the critical parts of the cycle out which results in overwhelming alerts, excessive false positives, and really, really confused people.

It's easy to joke about or complain about, but here is the thing...analysis is hard. Saying that we should do more/better/more timely analysis is easy. Actually doing it is not, especially in a new and still developing field like cyber threat intelligence. Models and methods help us understand the process, but even determining what model to use can be difficult. There are multiple approaches; some work better in certain situations and others work best in others.

### What is Analysis?

The goal of intelligence analysis is to evaluate and interpret information in order to reduce uncertainty, provide warnings of threats, and help make informed decisions. Colin Powell gave perhaps the most succinct guidelines for intelligence analysis when he said: “Tell me what you know, tell me what you don't know, tell me what you think. Always distinguish which is which”. This statement sums up intelligence analysis.

Analysts take what is known—usually information that has been collected either by the analyst themselves or by others—identify gaps in the knowledge that might dictate a new collection requirement or may present a bias that needs to be taken into consideration, and then determine what they think that information means. 

Before you begin any analysis you should have an idea of what it is that you are trying to figure out. Ideally this would be driven by requirements from leadership, teams you support, or some other form of standing intelligence needs. There are many situations in CTI, however, where those requirements are not as well defined as we might hope. Understanding what it is that the organization needs from threat intelligence is critical. Therefore, step one should always be to understand what problems, concerns, or issues you are trying to address.

### Analytic Models

Once you understand what questions you are trying to answer through your analysis, there are various analytic models that can be used to conduct analysis. I have listed some good resources available to help understand some of the more popular models that are often used in threat intelligence.

Different models are used for different purposes. The SWOT method is good for conducting higher-level analysis to understand how your own strengths and weaknesses compared to an adversary's capabilities. F3EAD, the Diamond Model, and the Kill Chain and are useful for analyzing specific instructions or how different incidents or intrusions may be related. Target Centric Intelligence is a lesser known model, but can help with not only understanding individual incidents, but provides a collaborative approach to intelligence including the decision makers, collectors, and analysts in an iterative process aimed at avoiding the stove-piping and miscommunications that are often present in intelligence operations. 

  * [SWOT (Strengths, Weaknesses, Opportunities, Threats) ](https://en.wikipedia.org/wiki/SWOT_analysis)
  * [Find, Fix, Finish, Exploit, Analyze, Disseminate ](http://sroberts.github.io/2015/03/24/f3ead/)by @sroberts
  * [Target Centric Intelligence](https://en.wikipedia.org/wiki/Intelligence_cycle_\(target-centric_approach\))
  * [Diamond Model for Intrusion Analysis](https://www.threatconnect.com/wp-content/uploads/ThreatConnect-The-Diamond-Model-of-Intrusion-Analysis.pdf)
  * [Analysis of Adversary Campaigns and Intrusion Kill Chains](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf)



### A final note on collection

In many cases, analysis can only be as good as the information that it is based off of. Intelligence analysts are trained to evaluate the source of information in order to better understand if there are biases or concerns about the reliability that need to be taken into account. In cyber threat intelligence we, by and large, rely on data collected by others and may not have much information on its source, reliability, or applicability. This is one of the reasons that analyzing information from your own network is so important, however it is also important that we, as a community, are as transparent as possible with the information we are providing to others to be used in their analysis. There are always concerns about revealing sources and methods, so we need to find a balance between protecting those methods and enabling good analysis. 

## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)