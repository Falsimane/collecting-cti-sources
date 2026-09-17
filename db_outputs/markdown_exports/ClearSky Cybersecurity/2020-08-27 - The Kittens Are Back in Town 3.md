# The Kittens Are Back in Town 3

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/the-kittens-are-back-in-town-3/
- **Date :** 2020-08-27

---

During 2017-2019, Clearsky had published several reports about the Iranian APT group “Charming Kitten”. One of the group’s most common attack vectors is impersonating journalists, particularly those from the German “Deutsche Welle” broadcasting company and the “Jewish Journal” magazine.

Starting July 2020, we have identified a **new TTP of the group** , impersonating “Deutsche Welle” and the “Jewish Journal” using emails **_alongside WhatsApp messages_** as their main platform to approach the target and convince them to open a malicious link. To gain the victim’s trust and ensure the opening of the link, the attackers use fake **_LinkedIn_** **profiles** as well. This is the first time we identified an attack by Charming Kitten conducted through WhatsApp and LinkedIn, including **_attempts to conduct phone call between the victim and the Iranian hackers_**. Charming Kitten chooses to impersonate Persian speaking journalists, to **neutralize detection through accent while having the phone call**. In this report, we expose for the first time the full conversation between Charming Kitten to a victim, conducted on WhatsApp.

Read the full report: **[The Kittens Are Back in Town 3](https://www.clearskysec.com/wp-content/uploads/2020/08/The-Kittens-are-Back-in-Town-3.pdf)**

The malicious link is embedded in a legitimate, compromised “Deutsche Welle” domain, with Waterhole methods. Each victim receives a personalized link, tailored to their specific email account. We identified an attempt to send a **malicious ZIP file** to the victim as well, additional to a message that was sent to the victim via a fake LinkedIn profile. We assess that in some cases, Charming Kitten would try to infect the victim with malware instead of stealing its credentials.

Here is a timeline of their operations involving “Deutsche Welle” and “Jewish Journal” in the past 3 years:

[![](https://www.clearskysec.com/wp-content/uploads/2020/08/timeline-550x319.png)](https://www.clearskysec.com/wp-content/uploads/2020/08/timeline.png)

It should be noted that this attack vector is unique to Charming Kitten, but it has not the only attack vector that has been used in recent months by this threat actor. More information about recent campaigns by the group can be found in our raw threat intelligence or on our blog.