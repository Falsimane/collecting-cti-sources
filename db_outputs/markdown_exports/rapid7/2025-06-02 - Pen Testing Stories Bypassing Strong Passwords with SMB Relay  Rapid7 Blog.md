# Pen Testing Stories: Bypassing Strong Passwords with SMB Relay | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/08/23/this-one-time-on-a-pen-test-missed-a-spot/
- **Date :** 2025-06-02

---

[Penetration testing](/solutions/penetration-testing/) is a valuable tool for clients to identify and remediate vulnerabilities and misconfigurations, especially when strong security controls and threat mitigation can miss the mark when only one or two systems fall through the cracks.

Like many internal network penetration tests, this one started by looking for NetBIOS Name Service (NBT-NS) and Link Local Multicast Name Resolution (LLMNR) requests to exploit. These auxiliary name resolution services can be used to resolve hostnames that are not found in DNS, which vulnerable hosts transmit out to the local network in broadcast requests and multicast requests. By sending poisoned responses to these requests, which claim the desired host name, a malicious actor can receive NetNTLMv2 password hashes from SMB connections.

Testing across two different local networks, I identified six hosts making NBT-NS requests. Among these hosts, though, poisoning attacks resulted in receiving SMB connections and password hashes for just one domain user. One of the most immediate risks of obtaining these password hashes is that they could be cracked. However, I was unable to crack the one NetNTLMv2 password hash that was obtained, so it must have been a pretty good, uncommon password. Good for them!

That said, another risk of being able to solicit these SMB connections is [SMB relay](/resources/smb-relay-attacks-explained/), where that challenge-response authentication traffic can be replayed against other hosts without the password needing to be cracked. Using RunFinger.py, I found just three SMB hosts that did not require message signing, and only one of which was actually joined to the domain.

Leveraging SMB connections from the one user account that was affected by NBT-NS poisoning, and using [Smbrelayx](https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbrelayx.py) to relay that connection to the one domain host that did not require SMB message signing, I was quickly able to retrieve password hashes for local user accounts from that host.

These NTLM password hashes are not challenge-response pairs, and can be used for ‘pass-the-hash’ authentication, where the uncracked password hash can be used as a stand-in for the actual password for network-based authentication. I was able to use these same local administrator credentials on nearly half of the SMB hosts in scope for the assessment. From there, it was quick work to retrieve cached plaintext passwords and password hashes with Mimikatz, a set of common local password recovery tools, which resulted in the discovery of a cached NTLM password hash for one of the domain administrators. Win.

Returning to cracking, now armed with the NTLM password hashes for all of the domain users, I still had very limited success. Valid credentials were only discovered for three working user accounts. While these accounts were enough to then find sensitive documents in file shares and SharePoint, the password cracking results showed that the client had a healthy culture of strong password generation among nearly the entire user base. When discussing these results during an onsite debrief, the client explained that most of their users have smart cards and long, randomly generated passwords. But, despite these strong passwords and very limited findings on most hosts, this engagement showed that just a handful of missed systems can still allow a malicious actor to gain a foothold using common attack techniques.

_Interested in learning more about how Rapid7 pen testers conduct their assessments? Check back every week for a new story in the series._

  * [This One Time on a Pen Test: Paging Doctor Hackerman](/blog/post/2019/08/09/this-one-time-on-a-pen-test-paging-doctor-hackerman/)
  * [This One Time on a Pen Test: How I Compromised a Healthcare Portal Before My Hot Cocoa Went Cold](/blog/post/2019/08/16/this-one-time-on-a-pen-test-how-i-compromised-a-healthcare-portal-before-my-hot-cocoa-went-cold/)
  * [This One Time on a Pen Test: Nerds in the NERC](/blog/post/2019/08/30/this-one-time-on-a-pen-test-nerds-in-the-nerc/)
  * [This One Time on a Pen Test: The Pizza of Doom](/blog/post/2019/09/12/this-one-time-on-a-pen-test-the-pizza-of-doom/)



## Article tags

  * [Penetration Testing](/blog/tag/penetration-testing/)
  * [This One Time on a Pen Test](/blog/tag/this-one-time-on-a-pen-test/)
  * [Research](/blog/tag/research/)