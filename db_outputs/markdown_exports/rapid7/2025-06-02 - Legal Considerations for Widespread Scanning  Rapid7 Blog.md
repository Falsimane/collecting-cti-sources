# Legal Considerations for Widespread Scanning | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2013/10/30/legal-considerations-for-widespread-scanning/
- **Date :** 2025-06-02

---

Last month Rapid7 Labs launched [Project Sonar, ](/blog/post/2013/09/26/welcome-to-project-sonar/)a community effort to improve internet security through widespread scanning and analysis of public-facing computer systems. Though this project, Rapid7 is actively running large-scale scans to create datasets, sharing that information with others in the security community, and offering tools to help them create datasets, too.

Others in the security field are doing similar work. This fall, a research team at the University of Michigan introduced [ZMap](https://zmap.io/), an open-source tool capable of scanning the entire IPv4 address space. Errata Security has also launched [Masscan](http://blog.erratasec.com/2013/09/masscan-entire-internet-in-3-minutes.html), which can scan the entire internet in three minutes.

These scans have great benefits—the more information we collect and share about the security of the internet, the better equipped everyone will be to fix the problems they discover.

Of course, this sort of ambitious security research raises some daunting questions. What are the legal implications of scanning all the public-facing computers on the internet? The answer—as with many legal questions involving technology—isn't clear.

In the United States, the federal law most likely to come into play is the [Computer Fraud and Abuse Act](http://www.law.cornell.edu/uscode/text/18/1030), a computer trespass statute. Several provisions of the CFAA are particularly relevant in the context of widespread scanning. They make it illegal to:

  * _“intentionally access[] a computer without authorization or exceed[] authorized access, and thereby obtain[] . . . information from any protected computer[.]_ ” § 1030(a)(2)(C). (Notably, this is the broadest provision in the statute and the one most frequently abused by overzealous prosecutors.)


  * _“knowingly cause[] the transmission of a program, information, code, or command, and as a result of such conduct, intentionally cause[] damage without authorization, to a protected computer[.]”_ § 1030(a)(5)(A).


  * _“intentionally access[] a protected computer without authorization, and as a result of such conduct, recklessly cause[] damage[.]”_ § 1030(a)(5)(B).


  * _“intentionally access[] a protected computer without authorization, and as a result of such conduct, cause[] damage and loss[.]”_ § 1030(a)(5)(C).



The CFAA is both a criminal and civil statute. Violations can result in criminal prosecution, fines, and prison time. In addition, private parties harmed by violations can sue for money damages or injunctive relief (i.e., a court order forbidding or demanding certain behavior).

There are similar computer crime laws in many [states](http://www.ncsl.org/issues-research/telecom/computer-hacking-and-unauthorized-access-laws.aspx), as well as other countries.

The exact contours of the CFAA are a mystery. While many of the law's prohibitions hinge on accessing a computer “without authorization” or in a manner that “exceeds authorized access,” the law doesn't clearly explain what these phrases mean. “Without authorization” isn't defined at all. The term “exceeds authorized access” means “to access a computer with authorization and to use such access to obtain or alter information in the computer that the accesser is not entitled so to obtain or alter.” § 1030(e)(6). Unfortunately, the CFAA doesn't say what it means to access a computer “with authorization,” so this definition also leaves a lot to be desired.

This lack of clarity creates a great deal of legal grey area. In certain troubling cases, the courts have found that accessing a public-facing computer can amount to a CFAA violation despite the fact that no technical barrier was breached. Just last fall, Andrew Auernheimer was convicted of conspiracy to violate the CFAA when another person ran a script to scrape iPad users' email addresses from unsecured AT&T servers. That result is currently on appeal, and will hopefully be overturned. (Disclosure: I am a member of Auernheimer's defense team.)

While legal uncertainty is a fact of life for security researchers, there are ways to reduce the risk of angering someone enough to make an issue of your research, as well as the possibility that a court might rule that your research has violated computer crime law. Rapid7 Labs, the ZMap research team, and Errata Security have all chosen to take certain steps to reduce the likelihood of legal trouble. The ZMap team has also published an excellent set of [scanning best practices](https://zmap.io/documentation.html#bestpractices).

These researchers have:

  * Been transparent about the nature of their research and the public benefits of it. Network operators may not mind scans if they know who's doing it and why.


  * Avoided research tactics that could cause disruption to someone else's computer network. This decreases the likelihood of causing “damage” or “loss,” both of which are elements of certain CFAA offenses.


  * Respected exclusion requests from network operators who didn't want their systems to be scanned. One might also consider responding to exclusion requests by providing information about the public benefits of the community's research and see if the requester still wants to be excluded.



The vague language of the CFAA and many state computer crime laws creates a great deal of room for interpretation. There are many questions about whether certain conduct is legal, and these questions do not have simple, straightforward answers.

Given the inherent ambiguity of computer crime statutes and the law in general, it's never possible to know for sure that scanning public-facing computers won't create legal problems for you. If you're planning to contribute to Project Sonar, you should consult an attorney who can advise you about your particular situation.

## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)
  * [Labs](/blog/tag/labs/)