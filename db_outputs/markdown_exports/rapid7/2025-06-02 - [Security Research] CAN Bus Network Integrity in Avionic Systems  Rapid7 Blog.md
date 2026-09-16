# [Security Research] CAN Bus Network Integrity in Avionic Systems | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/07/30/new-research-investigating-and-reversing-avionics-can-bus-systems/
- **Date :** 2025-06-02

---

Today, I'm pleased to announce the release of a paper covering a project I am passionate about, [Investigating CAN Bus Network Integrity in Avionics Systems](/research/report/investigating-can-bus-network-integrity-in-avionics-systems). This paper examines the security (or lack thereof) in CAN bus networks, specifically as they are implemented in small aircraft.

####   
Read the full research report today: Investigating CAN Bus Network Integrity in Avionics Systems

[Get Started](/research/report/investigating-can-bus-network-integrity-in-avionics-systems)

  


## What are CAN bus systems?

![Avionics_Cover-1.jpg](https://www.rapid7.com/cdn/images/blt9f5ccbf58310e138/683de3dc3beff0a7b9a7c54f/Avionics_Cover-1.jpg) I've run into CAN bus before, specifically in automotive applications. Back in 2017 while attending an air show to advance my project to build my own Rutan derived airplane (don't judge me, I live in Las Vegas, this is what I do), I pretty quickly ran into CAN bus for aviation. After all, it's inexpensive, easy to connect (just two wires), EMI-resistant, and it's rapidly becoming the de-facto standard network that connects electronically controlled sensors and actuators in all sorts of vehicles, aircraft included.

So, as both a pilot and a hacker, I figured we should probably take a look at aviation CAN bus implementations and see if they're on the same security path that automotive is.

## How secure are CAN bus avionics systems?

Unfortunately, it looks like the avionics sector is lagging in [network security](/fundamentals/what-is-network-security/) when it comes to CAN bus, and I think part of the reason is the heavy reliance on the physical security of airplanes. Cars are relatively easy to get your hands on—people just leave them parked on the street—but airplanes exist in a much more secure environment, which typically includes a lot of physical security controls.

But, just as [football helmets may actually raise the risk of brain injuries](http://freakonomics.com/podcast/the-dangers-of-safety-a-freakonomics-radio-rebroadcast/), the increased perceived physical security of aircraft may be paradoxically making them more vulnerable to cyber-attack, not less. Think about it: If you felt like your internal LAN was totally and completely untouchable by attackers, you probably wouldn't worry much about software patching or password management. Of course, LANs aren't impregnable, and neither are CAN bus networks, so we're worried about this mindset when it comes to avionics security. While physical restrictions are great, we really feel like avionics, in particular, need to implement defense-in-depth.

## Where do we go from here?

As mentioned above, the security implications of deploying CAN bus have been much discussed in the automotive industry. It’s well known that the same technology is used across various other transport sectors, yet most of the public discussion and response has focused solely on the automotive industry. This scrutiny has led to the automotive industry taking steps to mitigate the risks and even exploring alternatives to CAN bus.

Aviation is different to automotive for a whole lot of reasons, and we know that. Physical access controls are incredibly important in this sector, but as cybersecurity professionals, we are rarely satisfied with a single point of defense (also known as a potential single point of failure), particularly when it does not relate to the technical system itself. Bear in mind that avionics systems will often be deployed for decades, giving a determined attacker plenty of time to figure out an approach that gets around current mitigations. Our goal for this research paper is to drive more focus on this issue in the aviation industry so that hopefully a more nuanced approach to mitigating the risk of CAN bus emerges.

So, please, [take a look at the research report](/research/report/investigating-can-bus-network-integrity-in-avionics-systems)—it goes into how CAN bus is implemented in small aircraft, how I was able to reverse and replay CAN bus messages, and some recommendations for how to start securing CAN bus before this gets to be a really major problem.

## Learn more at the Aviation Village

If reading papers isn't your thing or you want to get into the research in more depth, you can come talk to me directly about these and other findings at the [Avionics Village](https://www.defcon.org/html/defcon-27/dc-27-villages.html#aviation) at DEFCON next week! It's our first year to have something aviation-specific, and I'm really excited to be a part of it. I'll be showing how I built my test environment and how avionics systems work. I’m always happy to help educate folks on the do's and don'ts of CAN bus. In fact, the whole reason we’re issuing this research now is because we believe the Aviation Village is a very important opportunity to educate the community and participate in conversations on aviation security, and hopefully, the use of CAN bus. Our intention was to give people some time to consume the research and then come and chat with us; however, I will confess that we are behind where we wanted to be timing-wise because this disclosure took us much longer than normal as we really wanted to ensure we were working with all the relevant parties and taking the appropriate steps to avoid causing unintended consequences.

On that note, I'd like to thank the Cybersecurity and Infrastructure Security Agency (CISA) of the U.S. Department of Homeland Security and Idaho National Labs (INL) for verifying the findings and [issuing their own alert](https://www.us-cert.gov/ics/alerts/ics-alert-19-211-01). I’d also like to thank the U.S. Federal Aviation Agency (FAA),the Aviation Information Sharing and Analysis Center (A-ISAC), and various members of the security research community for their guidance and feedback through the disclosure process. All provided invaluable insights into aviation safety and security, and really shaped how we approached this research. If you're ever worried about coordinating vulnerability disclosure with The Government, don't be! It might take a little longer, but ultimately, we were able to talk about these issues in a sane and sober way with experts from all over. All in all, it was a great experience, and I'm looking forward to my next coordinated disclosure on complex issues in a highly regulated environment (cue cliffhanger outro).

####   
Read the full research report today: Investigating CAN Bus Network Integrity in Avionics Systems

[Read the Report](/research/report/investigating-can-bus-network-integrity-in-avionics-systems)

  


## Article tags

  * [Research](/blog/tag/research/)