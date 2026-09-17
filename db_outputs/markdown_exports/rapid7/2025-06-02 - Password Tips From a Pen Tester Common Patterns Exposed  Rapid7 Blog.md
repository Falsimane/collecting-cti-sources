# Password Tips From a Pen Tester: Common Patterns Exposed | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2018/06/12/password-tips-from-a-pen-tester-common-patterns-exposed/
- **Date :** 2025-06-02

---

When my colleagues and I are out on penetration tests, we have a fixed amount of time to complete the test. Efficiency is important. Analyzing password data like we’re doing here helps pen testers better understand the likelihood of password patterns and choices, and we use that knowledge to our advantage when we perform [penetration testing](/fundamentals/penetration-testing/) service engagements at Rapid7.

In my experience, most password complexity policies require _at least three_ of the following:

  * Lowercase letter
  * Uppercase letter
  * Number
  * Special character



When employees are faced with this requirement, they tend to:

  * Choose a dictionary word or a name
  * Make the first character uppercase
  * Add a number at the end, and/or an exclamation point



If we know that is a common pattern, then we know where to start: by figuring out the dictionary word employees choose. Let’s take a look at an example.

I recently went on a penetration test where I was able to get access to the company’s full database of accounts and password hashes because I successfully guessed one user’s password: Winter2018. Once I have a user’s password, I have the same access to servers and workstations as that user. From there, I test whether that user’s credentials will let me log in to other workstations and servers. If I can log in, I have tools where I can check if an administrator’s password has been stored in the computer’s memory. Then with an administrator’s password and elevated privileges, I can often access things like company financial data, payroll information, customer data, and anything else stored in servers. **Takeaway:** A weak password doesn’t just affect the user who created it; it can also impact the security of the entire company network.

Why did I try Winter2018? Pen testers have tools that can assist with password data analysis. One of these tools is Pipal. Pipal is able to read through a file with thousands of passwords and spot patterns and count similar words. Running a Pipal analysis on my 100K+-strong password dataset showed that many other people have used the season and year as a password. In fact, when I looked in the dataset of passwords that the Rapid7 pen testing team has cracked over the last few weeks, winter is the third most-common dictionary word used, behind two company names. summer is the fifth most-popular and spring is the tenth most-popular word that someone uses in a password. (I’m not sure what happened to autumn and fall!) Also note that Winter2018 meets the password complexity requirements described above. When we look at it that way, it doesn’t seem terribly secure, does it?

Pipal is also able to analyze the characters used in passwords. It can tell us if people are using just lowercase characters, or upper _and_ lowercase, or special characters. 55% of the passwords we cracked didn’t use a special character, but they still adhered to the password policy mentioned above (i.e., they have an upper, a lower, and a number, much like Winter2018 or Password1). Pipal also tells us that digits are most frequently appended to a password; the dataset shows the top four-digit combinations added to passwords are, 2018, 2017, and 1234. The top three-digit combos are 123, 018, and 017, and the top two-digit combos are 23, 18, and 17. Pattern unlocked!

It’s analysis like this that helps us to work efficiently. When time is short, we can refer back to what the data tells us and rely on pattern analysis to predict user choices. I bet next month I’ll be able to access a system with Summer2018, and in a year, Winter2019 will get me in. If that doesn’t work, I’ll add an exclamation point at the end.

If you’re someone who likes data and numbers, here are a few interesting points from the 104,000 passwords Rapid7 pen testers garnered over the last few weeks:

  * 46% of passwords were exactly eight characters
  * 15% were nine characters (the next most common length)
  * 40% matched the format: letters/digit
  * 43% had their first character as uppercase and the last character as a number or symbol



The longest password cracked was 67 characters (I definitely did not guess this one!). The top two words in the password sample dataset were a company’s name. And finally, 74 passwords were literally just password.

What types of questions do you have about password usage? What analysis are you curious about? What kind of information would be helpful to you in hardening your systems and networks? Please post your comments and questions below.

Interested in more password research from Rapid7? Check out The Attacker’s Dictionary, research based on nearly a year’s worth of opportunistic credential scanning data collected from Heisenberg, Rapid7’s public-facing network of low-interaction honeypots.

## Article tags

  * [Penetration Testing](/blog/tag/penetration-testing/)
  * [Research](/blog/tag/research/)