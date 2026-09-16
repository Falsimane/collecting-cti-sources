# What is VERIS? | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2015/10/28/where-veris-smoke-veris-fire/
- **Date :** 2025-06-02

---

Data driven security is all the rage, and laughably few of us encode and analyze our programs… and for good reason. It isn't easy. This post will talk about VERIS, a framework for describing security incidents in a precise way.

We all have a plan, a security program, compliance regulations, and super busy calendars—but what is working? The answer is hidden in plain sight, it just needs to be analyzed. And this is why we all love the DBIR.

If you aren't familiar with Verizon's DBIR (Data Breach Investigation Report), check it out. I (and most of the industry) consider it the seminal report documenting trends in successful attacks and defensive failures.

Sports analogies are unavoidable here, and I won't apologize for them. The “Monday morning Quarterback” is a perfect analogy, and it applies to any sport, or activity. When you look back at a performance, just like the coaches do with the quarterback on Monday morning, you discuss more than outcomes, you talk about “what happened,” and “why it happened.”

##### Structured review, a meaningful critique, is based upon objective and accurate data.

Talking about incidents is hard. People take things personally, public statements are carefully tuned by PR, Marketing, and Legal teams, security professionals provide perspective to the news on very little in the way of facts— and that makes for difficult take aways for the rest of us.

Incidents happening in-house are often treated in a surprisingly similar fashion: carefully filtered facts get documented in writing, post mortem reports are often only narrative based, and the observations and lessons learned are limited to point-in-time assessments, or correlated only to recent audit findings or pinned to a convenient project.

Meaningful analysis across events requires a commitment to pragmatic event recording- this means structured data… which is why I'm excited to discuss VERIS.

## VERIS - Vocabulary for Event Recording and Incident Sharing

“VERIS is a set of metrics designed to provide a common language for describing security incidents in a structured and repeatable manner”

The overall goal “is to lay a foundation from which we can constructively and cooperatively learn from our experiences to better measure and manage risk”

By studying what incidents were stopped (near misses) and what path incidents came from, we can objectively evaluate our program strategies… this, in my opinion, is the magic of VERIS.

If our mission, as security professionals, is to inform the business of risk, ultimately stopping “the big one” — there is very little appetite to allow a [cybersecurity attack](/fundamentals/types-of-attacks/) to repeat itself.

## The A4

So VERIS describes an event using the 4 A's - and it's pretty simple when you think about it.

##### Actors take Actions, Assets have Attributes.

Yes. That's a blinding flash of the obvious.

Taking the obvious even further:

  * **Actors** often take lots of **Actions**
  * **Assets** may have multiple **Actions** taken against them
  * **Assets** may have multiple **Attributes** affected



So it makes sense this is more of a nested schema than something Excel spreadsheet friendly…

## Got it. Makes sense. Now what?

Get familiar with the A4 structure. We've got some videos here to save you some reading- but you'll want to read up after the overview.

First up, here are some videos giving an overview of **Actors, Actions, Assets, and** **Attributes** :

  * Actors


  * Actions



  * Assets


  * Attributes



## Article tags

  * [Verizon DBIR](/blog/tag/verizon-dbir/)