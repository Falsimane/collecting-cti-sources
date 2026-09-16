# This One Time on a Pen Test: Doing Well With XML | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/10/07/this-one-time-on-a-pen-test-doing-well-with-xml/
- **Date :** 2025-06-02

---

Most recently, I was on what appeared to be a normal web application penetration test. Typically, our clients will provide us with a few user accounts, such as an admin account and maybe a few different user roles. They’ll also give us any relevant API documentation and examples, or design information. However, one thing that stood out to me in the documentation of the application was how by design, the application specifically allowed for uploading XML files. Once I began going through the usual web application testing methodology and got a feel for the application, I began creating specifically crafted XML files that would allow for XML External Entity processing.

If you’re not familiar with how XML External Entity processing attacks work, it goes something like this: A penetration tester, or malicious actor, will target application functionality that allows for the processing of malicious XML data by a weakly configured XML parser. If the malicious XML is successfully processed by the XML parser, the tester may introduce external entities into their payload, which could allow them to retrieve the web application server’s system files (think /etc/passwd), or perform Server Side Request Forgery (SSRF) attacks, instructing the web application server to make any HTTP request to any desired URL, given there isn’t any network egress filter server-side.

Since I knew that the web application accepted XML, I wanted to see whether it would blindly accept malicious XML that would make a request to a Rapid7-controlled web server. First, I crafted an XML file that would simply instruct the web application server to make a GET request to me. On my jump box, I fired up a simple temporary web server, then submitted the malicious XML to the web application. Instantly, I received an ‘GET’ request from an IP address. After a quick verification, I confirmed that it was the web application server’s IP address!

After knowing that the web application accepted my malicious XML file, I wanted to demonstrate additional risk and see whether I could perform additional actions, such as the SSRF attack mentioned previously. After a quick discussion and recommendations with some team members, I again crafted a new XML file, but this time, I defined the XML file to instruct the web application server to attempt the retrieval of a nonexistent file on my jump box. The web application server was Windows, so we knew that if the attack was successful, it would also transmit Windows NTLM hashes to me. Next, I fired up Responder, a program that allows for capturing Windows hashes, on my server and uploaded the payload to the application, which then successfully transmitted the web server’s hashed Windows credentials to me! However, the credentials were for a Windows machine account, which are notoriously difficult to crack during a reasonable time of a web application penetration test. However, my client responded positively and worked with us to resolve the vulnerability in a couple of days. 

While we do not come across this type of vulnerability in every application assessment, you can bet that it’s something we always test for, especially if an application allows for uploading content or submission of XML through an endpoint. We believe that the demonstration of risk by combining XML with SSRF also translated the level of severity to the client and allowed them to dedicate resources to the application to resolve the issue immediately. This is one of the most rewarding aspects of penetration testing, when you can see your work making a positive impact and improving security postures, where possible. 

_Interested in learning more about how Rapid7 pen testers conduct their assessments? Check back every week for a new story in the series._

  * [This One Time on a Pen Test: Playing Social Security Slots](/blog/post/2020/09/02/this-one-time-on-a-pen-test-playing-social-security-slots/)
  * [This One Time on a Pen Test: I’m Calling My Lawyer](/blog/post/2020/09/09/this-one-time-on-a-pen-test-im-calling-my-lawyer/)
  * [This One Time on a Pen Test: Outwitting the Vexing VPN](/blog/post/2020/09/16/this-one-time-on-a-pen-test-outwitting-the-vexing-vpn/)
  * [This One Time on a Pen Test: Ain't No Fence High Enough](/blog/post/2020/09/23/this-one-time-on-a-pen-test-aint-no-fence-high-enough/)
  * [This One Time on a Pen Test: I Know...Everything](/blog/post/2020/10/02/this-one-time-on-a-pen-test-i-know-everything/)



## Article tags

  * [This One Time on a Pen Test](/blog/tag/this-one-time-on-a-pen-test/)
  * [Penetration Testing](/blog/tag/penetration-testing/)
  * [Research](/blog/tag/research/)