# Penetration Testing Stories: Our Accidental Win | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/09/25/this-one-time-on-a-pen-test-our-accidental-win/
- **Date :** 2025-06-02

---

One day, we were working on a web app penetration test for an online retailer client. While testing the login process with the client’s prior written consent, it looked like we were able to identify valid usernames through response times for failed logins.

To get a nice, thorough proof-of-concept, we took some common email domains and first and last names to create a decent-sized list of enumerated users. When doing user enumeration, it’s good advice to first focus on confirming all the users you can and only worry about guessing passwords after you know which users are valid. So, we started enumeration using a placeholder password: a short, simple word with no special characters, numbers, or capitalization.

At some point, the responses we got weren’t what we were expecting. So, we went back down through them and found that one login had actually been successful with the placeholder password! The client wasn’t really a fan of forcing users to choose complex passwords, but hopefully our accidental account compromise while demonstrating user enumeration was a good learning experience.

_Interested in learning more about how Rapid7 pen testers conduct their assessments? Check back every week for a new story in the series._

  * [This One Time on a Pen Test: Paging Doctor Hackerman](/blog/post/2019/08/09/this-one-time-on-a-pen-test-paging-doctor-hackerman/)
  * [This One Time on a Pen Test: How I Compromised a Healthcare Portal Before My Hot Cocoa Went Cold](/blog/post/2019/08/16/this-one-time-on-a-pen-test-how-i-compromised-a-healthcare-portal-before-my-hot-cocoa-went-cold/)
  * [This One Time on a Pen Test: Missed a Spot](/blog/post/2019/08/23/this-one-time-on-a-pen-test-missed-a-spot/)
  * [This One Time on a Pen Test: Nerds in the NERC](/blog/post/2019/08/30/this-one-time-on-a-pen-test-nerds-in-the-nerc/)
  * [This One Time on a Pen Test: The Pizza of Doom](/blog/post/2019/09/12/this-one-time-on-a-pen-test-the-pizza-of-doom/)
  * [This One Time on a Pen Test: What’s in the Box?](/blog/post/2019/09/19/this-one-time-on-a-pen-test-whats-in-the-box/)



## Article tags

  * [Penetration Testing](/blog/tag/penetration-testing/)
  * [This One Time on a Pen Test](/blog/tag/this-one-time-on-a-pen-test/)
  * [Research](/blog/tag/research/)