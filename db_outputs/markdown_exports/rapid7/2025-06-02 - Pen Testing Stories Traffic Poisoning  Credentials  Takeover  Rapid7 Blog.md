# Pen Testing Stories: Traffic Poisoning > Credentials > Takeover | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/10/02/this-one-time-on-a-pen-test-i-know-everything/
- **Date :** 2025-06-02

---

![](https://play.vidyard.com/K3n9EN4Q814EcwfFStn7Px.jpg)

It started as a standard internal network [penetration test](/fundamentals/penetration-testing/). A week before, another consultant had performed the external network penetration test and had already gained internal access. So, I began by taking a look at the broadcast and multicast traffic that was being sent. 

Per usual, I successfully poisoned some traffic and relayed credentials into a server that gave me hashes to a local administrator account. The client did not have Local Administrator Password Solution set up, so the local account granted me administrator access to essentially all the internal servers and workstations. I quickly identified a domain admin account and harvested the NTDS.dit. 

Now came the fun part: demonstrating impact. I knew the client had several sister companies, and I discovered one sold cell phone service and the other sold metadata collected from their mobile application and cell tower data.

I began to search for individuals with high levels of access, such as network engineers and security staff, to create my list of targets. Using passwords from the NTDS.dit, I began looking through emails and file shares. I quickly discovered a recently recorded Zoom call from a senior engineer debriefing engineers on how to take over his role during his last week of work. It showed me everything, from how to provision access for store employees to create new cell lines for customers, and how to get into their password safe. 

I decided the password safe was my best bet. Using some credentials from the NTDS.dit, I logged in to their main password management system. Thankfully they were very organized, and I quickly identified a tab called “Amazon Keys.” 

I then accessed their main S3 bucket using their AWS Access ID and Secret. It had everything. I found terabytes upon terabytes of cell tower data tracking their users, surrounding wireless SSID metadata, data of installed applications on clients’ phones, and best, yet: location data. Yup. Up-to-the-minute location data of everyone utilizing their services. 

That’s how I know where you are!

_Interested in learning more about how Rapid7 pen testers conduct their assessments? Check back every week for a new story in the series._

  * [This One Time on a Pen Test: Playing Social Security Slots](/blog/post/2020/09/02/this-one-time-on-a-pen-test-playing-social-security-slots/)
  * [This One Time on a Pen Test: I’m Calling My Lawyer](/blog/post/2020/09/09/this-one-time-on-a-pen-test-im-calling-my-lawyer/)
  * [This One Time on a Pen Test: How I Outwitted the Vexing VPN](/blog/post/2020/09/16/this-one-time-on-a-pen-test-outwitting-the-vexing-vpn/)
  * [This One Time on a Pen Test: Ain't No Fence High Enough](/blog/post/2020/09/23/this-one-time-on-a-pen-test-aint-no-fence-high-enough/)
  * [This One Time on a Pen Test: Doing Well With XML](/blog/post/2020/10/07/this-one-time-on-a-pen-test-doing-well-with-xml/)



## Article tags

  * [This One Time on a Pen Test](/blog/tag/this-one-time-on-a-pen-test/)
  * [Penetration Testing](/blog/tag/penetration-testing/)
  * [Research](/blog/tag/research/)