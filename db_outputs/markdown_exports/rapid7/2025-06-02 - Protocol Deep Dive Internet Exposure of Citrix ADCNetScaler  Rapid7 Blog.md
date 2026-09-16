# Protocol Deep Dive: Internet Exposure of Citrix ADC/NetScaler | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/11/04/nicer-protocol-deep-dive-internet-exposure-of-citrix-adc-netscaler/
- **Date :** 2025-06-02

---

Welcome to the NICER Protocol Deep Dive blog series! When we started researching what all was out on the internet way back in January, we had no idea we'd end up with a hefty, 137-page tome of a research report. The sheer length of such a thing might put off folks who might otherwise learn a thing or two about the nature of internet exposure, so we figured, why not break up all the protocol studies into their own reports?

So, here we are! What follows is taken directly from our National / Industry / Cloud Exposure Report (NICER), so if you don't want to wait around for the next installment, you can cheat and read ahead!

## Citrix ADC/NetScaler (TCP/Various)

_It's like VNC, but like if Plan9 ever escaped Bell Labs and got super popular._

### TLDR

**WHAT IT IS:** A client/server technology—similar to Microsoft Remote Desktop—that provides remote access to applications and/or entire operating systems desktop environments.

**HOW MANY:** 62,998 discovered nodes. 62,998 (100%) have Recog service version fingerprints

**VULNERABILITIES:** Tons! Most recently, a [severe, unauthenticated remote code execution vulnerability](/blog/post/2020/01/17/active-exploitation-of-citrix-netscaler-cve-2019-19781-what-you-need-to-know/) has been widely exploited since January 2020.

**ADVICE:** Use it! But, keep it patched and use multi-factor authentication.

**ALTERNATIVES:** Microsoft Remote Desktop, VNC, and other similar solutions used behind a well-oiled VPN.

Citrix was founded in 1989 and has a diverse array of remote access solutions over the years. Modern Citrix ADC (application delivery controller) and NetScaler solutions use the Microsoft Remote Desktop Services infrastructure to deliver virtual applications and desktops to remote users. Organizations have the ability to configure stronger access controls than with vanilla Remote Desktop, and there are other optimizations within the Citrix application delivery process that also make it faster and consume less bandwidth than raw Remote Desktop sessions.

### Discovery details

Identifying Citrix systems on the internet turns out to be pretty easy, since their HTTP and NTP servers [kind of go out of their way](https://github.com/rapid7/recog/search?q=citrix&unscoped_q=citrix) to proudly let you know they are, indeed, Citrix systems. This makes it easy for Rapid7 Labs researchers to track the spread of Citrix systems on the internet, and in March 2020, we also developed a method to fingerprint the server version based on the version fingerprint of the Citrix client that is offered for download (again, Citrix going out of its way to help folks identify their systems).

The Labs team spent time on this effort because attackers keep compromising systems that haven’t patched a [gnarly remote code execution vulnerability](https://attackerkb.com/topics/x22buZozYJ/cve-2019-19781), and we have many in-flight projects set up to model patch adoption rates of various technologies.

Unlike many other top 10 country lists in this report, China failed to even beat out Sweden in their internet-facing exposure of Citrix systems.

![citrix-1.png](https://www.rapid7.com/cdn/images/blt880884b5ad2f6455/683de8fae3c8aa8c10831019/citrix-1.png) ![citrix-2.png](https://www.rapid7.com/cdn/images/blta5b8bc2c98b86247/683de90e2cfe3254f9dc18cd/citrix-2.png)

The lack of Citrix in cloud environments makes sense, since this technology is usually associated with virtual desktop infrastructure (VDI), which is almost exclusively found in enterprise/business environments.

### Exposure information

With an actively exploited vulnerability in play and [regular government warnings](https://us-cert.cisa.gov/ncas/alerts/aa20-031a) about the situation, you’d likely guess that internet-facing Citrix servers were fully patched or had mitigations in place. And, you’d be wrong (again), but this time, the situation isn’t as grim as you might expect.

![citrix-3.png](https://www.rapid7.com/cdn/images/bltdb9581abb791414e/683de9213e68ee8c72889c29/citrix-3.png)

Our version fingerprinting technique showed that 73% of internet-facing Citrix systems have patches or mitigations in place, with the remaining 27% either being vulnerable or woefully outdated (thus having other issues to worry about). It has taken five months to get to a patch rate of 73%.

### Attacker’s view

The vast majority of our Heisenberg honeypot nodes are in cloud environments, and—as we’ve just seen—clouds are not where Citrix tends to live (at least on public internet cloud segments). Back in January, we caught attackers and researchers looking for exploitable systems quite regularly, but that activity has waned (though it hasn’t stopped).

![citrix-4.png](https://www.rapid7.com/cdn/images/blt6a9e49812bf64d55/683de9376b437b07234fa8a3/citrix-4.png)

Our honeypots do not emulate Citrix, so the lack of activity is more likely due to our nodes being ignored after each attacker inventory scan. Attackers may also be reusing initial inventory lists or have already established a foothold on the thousands of systems that took forever to be patched.

### Our advice

**IT and IT security teams** should relentlessly monitor vendor bulletins and CVE reports and patch Citrix environments as soon as possible. With attackers increasingly targeting remote access technologies over the past 18 months, it would also be a good idea to have enhanced monitoring with more detailed logging set up on these systems. 

**Cloud providers** likely can just keep doing what they’re doing with regard to Citrix since it does not seem to be widely used, despite Citrix-provided solutions for these environments.

**Government cybersecurity agencies** should keep up the great work they’ve been doing calling attention to threat actor activity and the severity of vulnerabilities in remote access technologies like Citrix.

## Article tags

  * [NICER Reports](/blog/tag/national-industry-cloud-exposure-report-nicer/)
  * [Research](/blog/tag/research/)