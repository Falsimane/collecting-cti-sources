# [Research Recap] Rapid7 Quarterly Threat Report: 2020 Q1 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2020/06/03/rapid7-quarterly-threat-report-2020-q1/
- **Date :** 2025-06-02

---

If calendars still hold any meaning for you, you may be dimly aware that it's now midway through the second quarter of 2020, which means we've just wrapped up our first-quarter analysis of the threat landscape out there on the internet. Or is it, "in here on the internet?" I'm having trouble deciding what preposition to use now. (But seriously, be safe, limit your contact, and we'll get through this without crashing our hospital capacity.)

You can download the latest Quarterly Threat Report [here](/research/report/2020Q1-threat-report/), but if you need just a smidge more convincing to dive into the data, here are the highlights:

## Enterprise applications are under attack

This past quarter, we saw an uptick in our reported incidents that involved exploitation against known-vulnerable, internet-facing enterprise applications, including Microsoft Exchange Outlook Web Application (OWA), which continues to see laggy patch adoption rates. At first blush, this might sound like old news—attackers gonna attack, after all—but in past quarters, most of the breaches that required incident response were either credential-based (reused passwords) or started off with a malware-dropping phishing lure. This shift in tactics shows that even in a time of pandemic, attackers are both keeping up with vulnerability and exploitation R&D, and are more than willing to seek out the softest targets available.

## The user is still the key

While this spike in vuln-based exploitation is apparent in our breach statistics, the overall number of security incidents (most of which do _not_ lead to a breach) are still squarely focused on the user. In total, 96% (or just over 19 out of 20) of our [Managed Detection and Response (MDR)](/services/managed-detection-and-response-mdr/) reports involve some flavor of stolen credentials, with the top three industries reporting these incidents being Finance (19%), Professional Services (17%), and, tragically, Healthcare (9%).

Because of this, we can't recommend multi-factor authentication (MFA) enough. MFA takes the sting out of a credential dump that may or may not affect your organization, and buys you time to investigate the dump and change out any passwords that happen to line up.

## Endpoints, endpoints everywhere

In the Beforetimes, we could count on at least most of our nine-to-five assets to be comfortably tucked away behind corporate firewalls, unable to make direct connections to the internet without at least some kind of network monitoring solution noticing. The violent shift to work-at-home for a huge percentage of knowledge workers changed all that, so monitoring for endpoint-based indicators of compromise is more important than ever. This quarter's Threat Report goes into detail on what those threats look like, and the tactics that any Endpoint Detection and Response (EDR) solution should be employing to pick them up early enough in the [ATT&CK kill chain](/fundamentals/mitre-attack-framework/) before they cause serious damage to the enterprise.

## Go get it!

It's not like you have any meetings to go to, so feel free to paste up your pre-recorded paying attention face on your Zoom camera (oh, it's a thing), and dive into the Quarterly Threat Report to catch up on latest in real-world readouts on the state of cybersecurity. At the very least, it'll help you sound super-informed at the next security ops planning session, where you actually _will_ be paying attention.

## Article tags

  * [Research](/blog/tag/research/)