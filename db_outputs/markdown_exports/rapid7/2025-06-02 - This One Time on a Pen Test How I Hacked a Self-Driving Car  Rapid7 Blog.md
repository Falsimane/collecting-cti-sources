# This One Time on a Pen Test: How I Hacked a Self-Driving Car | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/11/06/this-one-time-on-a-pen-test-how-i-hacked-a-self-driving-car/
- **Date :** 2025-06-02

---

Play Video

![Vidyard video](https://play.vidyard.com/9uy8iWrx5WJDmwhicb39Va.jpg)

![](https://play.vidyard.com/9uy8iWrx5WJDmwhicb39Va.jpg)

An organization hired us to perform a [penetration test](/fundamentals/penetration-testing/) on a self-driving car—as it turns out, there are several self-driving projects available on the market today, so we were tasked with assessing the attack surface of the vehicle to enumerate vulnerabilities that could lead to remote control of the vehicle. This included testing a somewhat broad scope of the vehicle, including its CAN Bus and TCP/IP networking. 

I was responsible for testing the TCP/IP portion of the assessment. Through testing, we followed a similar methodology to an internal penetration test. We connected to the network using an ethernet cable, scanned the vehicle’s Local Area Network identifying alive hosts, port scanned to fingerprint for services, etc. 

While scanning, we found that anonymous FTP was enabled on a couple of the hosts. Upon further inspection, we learned that it allowed Read and Write with Root permissions to the Root directory of its Linux operating system. We uploaded our own private key to the system using the anonymous login and found that we could then SSH in. Turns out the hosts were part of the radar controller unit. This system failing while the vehicle was in motion could lead to the car crashing.

Continuing our testing, we also found that the system had several instances of Docker listening. The Docker interfaces were bound to the hosts’ external TCP/IP interface. Insecure Docker images are pretty common on corporate networks, and sure enough, this proved to be the case with the car! Not only was the service bound to the hosts external interface, it also was not configured with authentication. This led to us accessing the Docker host as well as the Docker images with Root privileges. Turns out, these systems were the controllers for the Autonomous Vehicle System, the device that stored proprietary software for how the vehicles leverage its Artificial Intelligence and Machine Learning algorithms. 

_Interested in learning more about how Rapid7 pen testers conduct their assessments? Check back every week for a new story in the series._

  * [This One Time on a Pen Test: Playing Social Security Slots](/blog/post/2020/09/02/this-one-time-on-a-pen-test-playing-social-security-slots/)
  * [This One Time on a Pen Test: I’m Calling My Lawyer](/blog/post/2020/09/09/this-one-time-on-a-pen-test-im-calling-my-lawyer/)
  * [This One Time on a Pen Test: Outwitting the Vexing VPN](/blog/post/2020/09/16/this-one-time-on-a-pen-test-outwitting-the-vexing-vpn/)
  * [This One Time on a Pen Test: Ain't No Fence High Enough](/blog/post/2020/09/23/this-one-time-on-a-pen-test-aint-no-fence-high-enough/)
  * [This One Time on a Pen Test: I Know...Everything](/blog/post/2020/10/02/this-one-time-on-a-pen-test-i-know-everything/)
  * [This One Time on a Pen Test: Doing Well With XML](/blog/post/2020/10/07/this-one-time-on-a-pen-test-doing-well-with-xml/)



#### NEVER MISS A BLOG

Get the latest stories, expertise, and news about security today.

Subscribe

  


## Article tags

  * [This One Time on a Pen Test](/blog/tag/this-one-time-on-a-pen-test/)
  * [Penetration Testing](/blog/tag/penetration-testing/)
  * [Research](/blog/tag/research/)