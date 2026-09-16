# Is the Internet of Things the Next Ransomware Target? | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/01/20/is-the-internet-of-things-the-next-ransomware-target/
- **Date :** 2025-06-02

---

[Ransomware attacks](/fundamentals/what-is-ransomware/) over the last couple years have been traumatic, impacting nearly every business sector and costing billions of dollars. The targets have mostly been our data: steal it, encrypt it, and then charge us a fee to get it back. 

Over the last several years, there's been [concern across the security community](https://www.iotsecurityfoundation.org/the-iot-ransomware-threat-is-more-serious-than-you-think/) about the risks related to the [Internet of Things (IoT)](/fundamentals/what-is-internet-of-things-iot-security/) being impacted by ransomware. For the most part, this has not occurred — although I wouldn’t be surprised if IoT has played a role as the entry point that malicious actors have used, on occasion, to gain access to [plant their ransomware on critical systems](/blog/post/2021/09/24/ransomware-is-critical-infrastructure-in-the-clear/). Also, we do know of examples where IoT technologies, such as those used within [medical](https://www.forbes.com/sites/thomasbrewster/2017/05/17/wannacry-ransomware-hit-real-medical-devices/?sh=22a68829425c) and industrial control environments, were impacted during ransomware attacks through key components of their ecosystem involving standard Windows server and desktop solutions.

## IoT ransomware risk and its implications

So, what would it take for IoT to be the target of ransomware? First, the IoT being attacked would need to be a large deployment with significant importance in its functions and capabilities. The attack would also need to be disruptive enough that an organization would be willing to pay. 

Personally, I’m not confident such an environment exists, at least as it would apply to the average organization. But let’s step back and look at this from the perspective of the vendor who remotely manages, controls, and updates their products over the Internet. For example, imagine what would happen if a malicious actor successfully breached an automotive organization with smart-capable cars — could they shut down every car and lock the company and owner out of fixing them? 

If we apply that train of thought across the board for all IoT deployed out there, it becomes very concerning. What if we shut down every multifunction printer by a major manufacturer, home thermostat, building HVAC, or building lighting solution? What happens if the target is a smart city and traffic lights are impacted? We could go on all day talking about the impact from smart city breaches or attacks against small deployed IoT solutions from major brands with global footprints.

## Building a threat model

So, are there steps we can take to head off such an event? The answer is yes. I believe IoT vendors and solution owners could best accomplish this by identifying the potential attack vector and risk through [threat modeling](/fundamentals/what-is-threat-modeling/).

As part of building out a threat model, the first step would be to identify and map out a complete conceptual structure of the IoT system that could be potentially targeted. In the case of IoT technology, this should consist of all components of the system ecosystem that make the solution function as intended, which would include:

  * Embedded hardware system actuators, sensors, and gateways
  * Management and control applications, such as mobile and cloud services, as well as thick clients on servers, desktops, and laptops systems
  * Communication infrastructure used for data and operational controls including Ethernet, Wi-Fi, and other radio frequency (RF)



Any component or subcomponent of this ecosystem is at potential risk for being targeted. Mapping out this information gives us the ability to better understand and consider the potential points of attack that a malicious actor could use to deliver or execute a ransomware style attack against IoT.

In the second step of this threat modeling process, we need to understand the possible goals of a malicious actor who would be targeting an IoT ecosystem, who they may be, and what their end game and potential methods of attack would look like. The threat actors would likely look very similar to any malicious actor or group that carries out ransomware attacks. I think the big difference would be how they would approach attacking IoT ecosystems.

This is the phase where creative thinking plays a big role, and having the right people involved can make all the difference. This means having people on the threat modeling team who can take an attacker mindset and apply that thinking against the IoT ecosystems to map out as many potential attack vectors as possible.

## Mapping out the threat and response

The third step in the threat modeling process is building a list of threats we would expect to be used against the above IoT ecosystems. One example, which is also common with typical ransomware attacks, is locking. By locking a component of the IoT solutions ecosystem, a malicious actor could prevent the IoT ecosystem from properly functioning or communicating with other key components, completely taking the technology out of service or preventing it from functioning as intended.

In the final part, we take the detailed information we’ve put together and map out specific attack scenarios with the greatest chance of success. Each scenario should define the various components of the IoT ecosystem potentially at risk, along with the perceived attacker motives, methods, and threats that can lead to the attacker being successful. Once you’ve mapped out these various scenarios in detail, you can use them to define and implement [specific controls](https://www.cisecurity.org/white-papers/internet-of-things-security-companion-to-the-cis-critical-security-controls/) to mitigate or reduce the probability of success for those attack scenarios.

Using these threat modeling methods will help IoT solution vendors and the organizations that use their products identify and [mitigate the risk and impact of ransomware attacks](/blog/post/2021/09/16/the-ransomware-killchain-how-it-works-and-how-to-protect-your-systems/) against IoT solutions before they happen.

  


## Article tags

  * [Ransomware](/blog/tag/ransomware/)
  * [IoT](/blog/tag/iot-security-news/)
  * [Research](/blog/tag/research/)