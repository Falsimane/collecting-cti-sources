# Threat Intelligence Foundations: Crawl, Walk, Analyze - Part 2 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/03/10/threat-intelligence-foundations-crawl-walk-analyze-part-2/
- **Date :** 2025-06-02

---

_This is the second post in a three-part series on threat intelligence foundations, discussing the fundamentals of how threat intelligence can be used in security operations._[_Read Part One here_](/blog/post/2016/03/09/threat-intelligence-foundations-crawl-walk-analyze-part-1/) _._

## Tinker, Tailor, Soldier, Spy: Utilizing Multiple Types of Intelligence

Just as there are different operational levels of intelligence—discussed in detail in the [first post](/blog/post/2016/03/09/threat-intelligence-foundations-crawl-walk-analyze-part-1/) of this series—there are also different types of intelligence that can be leveraged in an organization to help them better understand, prepare for, and respond to threats facing them.

Don't laugh—but a great basic resource for understanding the types of intelligence is the CIA's Kid Zone, where they break intelligence down for the 6-12th graders that we all are at heart (or K-5, no judgement here).

#### They break intelligence down into several different types:

  * #### Scientific and Technical – providing information on adversary technologies and capabilities.

  * #### Current – looking at day-to-day events and their implications.

  * #### Warning – giving notice of of urgent matters that may require immediate attention.

  * #### Estimative – looking at what might be or what might happen.

  * #### Research – providing an in-depth study of an issue.




While most organizations may not work with all of these types of intelligence, or do so in the same way that the CIA does (and please don't tell me if you do), it is useful to understand the spectrum and what each type provides. The different types of intelligence require varying levels of human analysis and time. Some, like technical intelligence, are easier to automate and therefore can be produced at a regular cadence, while some, like threat landscape research, will always rely heavily on human analysis.

### 

## Technical Intelligence

In information security operations, technical intelligence is used to understand the capabilities and the technologies used by an adversary. It can include details such as IP addresses and domains used in command and control, names and hashes of malicious files, as well as some TTP details such as vulnerabilities that a particular actor targets or a particular callback pattern for a beaconing implant.

Technical intelligence is most often used in machine-to-machine operations, and is therefore automated as much as possible to handle the large volume of information. In many cases, technical intelligence does not contain much context, even if context is available in other places, because machines do not care as much about the context as their humans do. A firewall doesn't need to know why to block traffic to a malicious domain, it just needs to do it. The human on the other end of that firewall change might want to know, however, in case the change ends up triggering a massive amount of alerts. Technical intelligence must have been analyzed prior to consumption, otherwise it is just data or information at best. For more information see [Robert Lee's post on the data vs information vs intelligence debate](http://www.robertmlee.org/data-information-and-intelligence-your-threat-feed-is-not-threat-intelligence).

If you are not using technical intelligence that you generated yourself, it is critical that you understand the source of the technical intelligence and how it was analyzed, especially if it was analyzed using automated means. I am going out on a limb here by stating that there is a way to analyze and produce [threat intelligence](/fundamentals/what-is-threat-intelligence/) in an automated fashion that can be utilized machine-to-machine. Do NOT prove me wrong—do the analysis!

## Current Intelligence

Current Intelligence deals with day-to-day events and situations that may require immediate action. I have heard several people say that, “news isn't intelligence,” and that is a true statement; however, threat information in the public domain, when analyzed for implications to your specific organization, network, or operations, becomes intelligence.

An example of the use of current intelligence is a report that an exploit kit has integrated a vulnerability that was just announced three days ago. If you know that you are on a thirty-day patch cycle that means (best case) you have twenty-seven days where you will be vulnerable to these attacks. Understanding how this threat impacts your organization and how to detect and block malicious activity associated with it is an example of current intelligence. Current intelligence can also be generated from information within an organization's networks. Analyzing an intrusion or a spearphishing attack against executives can also generate current intelligence that needs to be acted on quickly.

When you do generate current intelligence from your own network, document it! It can then contribute to threat trending and threat landscape research, which we will discuss shortly. It can also be shared with other organizations.

## Threat Trending (Estimation)

All of the intelligence gathered at the tactical level (technical intelligence, current intelligence) can be further analyzed to generate threat trends. Threat trending takes time because of the nature of trending, you are analyzing patterns over time to see how things change and how they stay the same. Threat trending can be an analysis of a particular threat that has impacted your network repeatedly, or it can be an analysis of how an actor group or malware family has evolved over time. The more relevant a threat trend is to your network or organization, the more useful it will be to you.

Threat trending allows us to move from an analysis of something that we have seen and know is bad towards predicting or estimating future threats.

## Threat Landscape Research

Speaking of trending, there has been a long trend in intelligence analysis of focusing on time-sensitive, current intelligence at the expense of longer term, strategic research. Consider how many tactical level, technical IOCs we have in the community compared to strategic intelligence resources. How many new programs are focused on providing “real-time intelligence” versus “deliberate, in-depth analysis.” There are legitimate reasons for that: there are not enough analysts as it is, and they are usually focused on the time-sensitive tasks because they are, well, time sensitive. In addition, we don't always have the right data to conduct strategic level analysis, both because we are not accustomed to collecting it from our own networks and most people who are willing to share tactical indicators of threats are not as willing to share information on how those threats impacted them.

We need to change this, because you cannot (or should not) make decisions about the future of your security program without a strategy, and you cannot (or should not) have a security strategy without understanding the logic behind it. Threat landscape research—which is a long term analysis of the threats in your environment, what they target, how they operate, and how you are able to respond to those threats—will drive your strategy. The tactical level information you have been collecting and analyzing from your network on a daily basis can all contribute to threat landscape research. Current intelligence, yours and public domain information, can also contribute to threat landscape research. One framework for capturing and analyzing this information is [VERIS](https://verisframework.org/)—the Vocabulary for Event Recording and Incident Sharing, which the DBIR is based off of. Just remember, this type of intelligence analysis takes time and effort, but it will be worth it.

## Information Sharing

There is currently an emphasis on sharing IOCs and other technical information, however any of the types of intelligence we have discussed in this post are good candidates for information sharing. Sharing information on best practices and processes is also incredibly beneficial.

Sharing information on what has been seen in an organization's network is a good way to understand new threats as they emerge and increase situational awareness. Information sharing essentially generates intelligence to warn others of threats that may impact them. Information sharing is becoming increasingly automated, which is great for handling higher volumes of information, however, unless there is an additional layer of analysis that focuses on how this information is relevant or impacts your organization then it will stay information (not intelligence) and will not be as useful as it could be. For more information see Alex Pinto's presentation on his recent research on [measuring the effectiveness of threat intelligence sharing.](https://www.youtube.com/watch?v=qcLKueGR-Vs)

Even if you are not yet convinced of the value of generating your own intelligence from your environment, consuming threat intelligence still requires analysis to understand how it is relevant to you and what actions you should take. A solid understanding of the different types of intelligence and how they are used will help guide how you should approach that analysis.

## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)