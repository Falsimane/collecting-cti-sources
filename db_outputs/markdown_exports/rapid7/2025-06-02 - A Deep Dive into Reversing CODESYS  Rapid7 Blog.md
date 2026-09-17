# A Deep Dive into Reversing CODESYS | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2023/02/14/a-deep-dive-into-reversing-codesys/
- **Date :** 2025-06-02

---

Industrial Control System (ICS) networking stacks are often the go-to [bogeyman](https://www.britannica.com/topic/bogeyman) for infosec and cybersecurity professionals, and doubly so for offensive, red-team style security folks. How often have you been new on site, all ready to run a bog-standard nmap scan across the internal address space, only to be stopped by a frantic senior manager, "No, you can't scan 192.168.69.0/24, that's where the factory floor operates!"

"Why not?" you might ask—after all, isn't it important to scan your IP-connected assets regularly to make sure they're all accounted for and patched? Isn't that kind of the one thing we tell literally anyone who asks, right after making sure your passwords are nice and long and random?

"Oh no," this manager might plead, "if you scan them, they fall over, and it kills production. Minutes of downtime costs millions!"

Well, I'm happy to report that today, Rapid7's Andreas Galauner has produced a [technical deep dive whitepaper](/info/codesys-white-paper/) into the mysterious and opaque world of PLC protocols, and specifically, how you, intrepid IT explorer, can safely and securely scan around your CODESYS-based ICS footprint.  


![](https://lh4.googleusercontent.com/eXcUc1kISXGDg5zu4gegy3ctJnJ67hFEGxxxyneHYEYNEnEF5W_nWkAlS6oniHlu_pxjh-Da6xoYltDubLbOQazjK3ZPp321RO8Heq8TOhzQx_fsLlTbF1ip4-P5pAuORh3PsSNQQb4gSvvbxse8rUo)

  
  
CODESYS is a protocol suite that runs a whole lot of industrial equipment. Sometimes it's labeled clearly as such, and sometimes it's not mentioned at all in the docs. While it is IP-based, it also uses some funky features of UDP multicast, which is one reason why scanning (or worse, fuzzing) these things blindly can cause a lot of trouble in the equipment that depends on it.

No spoilers, but if you're the sort who always wondered why, exactly, flinging packets at the ICS network can lead to heartache and lost productivity, this is the paper for you. This goes double if you're already a bit of a networking nerd.

If you're not sure, here's an easy test. Go and read this [Errata Security blog](https://blog.erratasec.com/2019/08/hacker-jeopardy-wrong-answers-only.html) about the infamous Hacker Jeopardy telnet question real quick. If you have any emotional response at all (hilarity, enlightenment, outrage, or a mix of all three), you're definitely in the audience for this paper.

Best of all, this paper comes with some tooling; Andy has graciously open sourced a Wireshark plugin for CODESYS analysis, and an Nmap NSE script for safer scanning. You can grab those, right now, at our [GitHub repo](https://github.com/rapid7/data/tree/main/codesys). Cower in the dark about ICS networks no more!

Download the whitepaper here: [https://www.rapid7.com/info/codesys-white-paper/](/info/codesys-white-paper/)

  


## Article tags

  * [Research](/blog/tag/research/)