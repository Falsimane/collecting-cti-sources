# The Data Science Process at Rapid7 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2016/11/15/the-data-science-process-at-rapid7/
- **Date :** 2025-06-02

---

Data Science is more than just math. A successful Data Science team and successful Data Science projects require relationships with outside teams, clear communication, as well as good decision making, problem solving and critical thinking abilities. Thus, when we talk about Data Science at Rapid7, we talk about the Data Science Process our teams use to take a Data Science project from inception to completion, where math and analysis are important, but not the only aspects of the project.

## What are we talking about here?

To be clear about terms, we consider Data Science to be composed of several related disciplines, such as statistics, machine learning, visualization and to some extent, data engineering and management.

Additionally, Data Science (and machine learning in particular) is the right tool to address **_some_** problems. However, it is important to distinguish between machine learning applied to problems for which it is the right tool to solve them, and machine learning applied to problems for the sake of being able to market “more machine learning.”

## Why does Rapid7 use Data Science?

Rapid7's motivation for using Data Science is to solve complex problems to make our products more effective and our customers happier. Specifically, _it is not_ to be able to market the inclusion of machine learning capabilities in our products. When a problem we're working on can be best addressed by machine learning, we will try to use machine learning techniques to address that problem, otherwise, we will find another more appropriate way to address the problem, possibly even a simple rule.

## Ok, walk me through this process

When people or groups within Rapid7 (problem owners) have a problem they think can be solved or addressed by the Data Team, they come to us to figure out if we can help. Throughout the entire process described below, the Data Team and the problem owner are in contact to make sure the assumptions we make about the problem, the data, and the solution are correct.

There are six steps involved in the Data Science Process:

  1. Understand the problem
  2. Identify relevant data
  3. Determine viability
  4. Research research research
  5. Report
  6. Hand off



### Understand the problem

The first step is to get a deep understanding of the problem to be solved. This involves a few rounds of questions and answers with the problem owner to make sure they are convinced that the people from the Data Team really do understand the problem. Without this deep understanding of the problem (Why is it a problem in the first place? Why does it need to be solved? What does a good solution look like?), it is easy to end up with a solution that isn't what the problem owner really needs.

### Identify relevant data

The next step is to figure out if there is data that can help solve the problem, and if there is, where that data lives. Do we already have it? Do we need to gather it? Buy it? Generate it? Working together with the problem owner, as much as they are able to, we make a determination together about whether or not the data we plan to work with is appropriate for the problem, or if there is other data we should be using.

### 

### Determine viability

This is the squishiest step of them all, but is crucial. In this step, the Data Team will determine whether or not the relevant data is sufficient to try to solve the problem, or at least start research. This isn't an attempt to rate the quality of the available data from a mathematical or statistical point of view, but rather to take a step back from the work that's been done thus far and take stock of whether or not there is enough available data to do anything worthwhile.

For instance, if the available data consists of two data sets from two different sources which share a field in column that can link the two, but the intersection of these data sets is some very small proportion of either, it's worth taking time here to evaluate if there's more data that can be gathered to make that intersection larger, or whether there's a different way to join the data.

### Research research research

This is the stage where the Data Science team will do the work they probably consider the most interesting and fun. They will investigate whether different Data Science techniques are appropriate to solve the problem. If machine learning looks viable, they will identify which machine learning algorithms are appropriate and see if they can make an interesting model. Ideally, this is the stage where the problem is solved, or if it can't be solved, it becomes clear why that is.

It is also crucial that through this phase the Data Team and the problem owner consult with each other frequently about the progress being made and the issues that come up. In most cases the problem owner will have more domain knowledge about the problem and the data at hand than the Data Team does, so being able to check in frequently and run new findings by domain experts will help the Data Team quickly readjust their efforts when necessary.

### Report

The reporting stage is an opportunity for the Data Team to communicate back to the problem owner everything they've done in the “research research research” phase. This is the inverse of the first stage, in that now the problem owner should be making sure they understand as much as they can about the outcome of the research. The Data Team will explain data they used, why it was useful, the methods they used to transform and analyze that data, and what they've come up with as a solution to the problem. Additionally, they will present an overview (or as much detail as the problem owner wants) about specifically what did not work.

This stage is crucial to the Data Science Process. It allows both the Data Team and the problem owner to come back together and fully evaluate whether or not the outcome of the research addresses the problem, and if the Data Team has achieved its goal from the first stage when they identified what a good solution would look like.

### Hand off

The final stage of the process is to work with the problem owner to hand off the research output and make it useful. In this stage, both the Data Team and the problem owner need to figure out:

  * What will an embodiment of the solution look like? (A command line tool? A hosted service? A shared library? An additional API? A serialized model?)
  * Who will update and maintain that embodiment?
  * Where does it live? And who gets the call at 3:00 a.m. when something breaks?



Without a clear plan for how to incorporate the solution into a system that can make use of it, it can easily wither and not be adopted.

## Great, this seems familiar, how is this specific to Data Science?

Except for the details of the “research research research” phase, very little of this is specific to Data Science. This process is derived from and can be applied to other disciplines, but just spelling it out and going through the process has been immensely useful to our Data Team.

We have had projects where we didn't fully understand the problem and found ourselves at the end of a project presenting something back to the problem owner that they already knew or knew how to do.

We have had projects where we didn't fully explore the available data, or determine whether that data was viable, and we worked on incomplete data sets and ended up with a solution that didn't give the problem owners much confidence in the solution's utility.

We have had projects where we didn't communicate our findings well or thoroughly to the problem owner and as a result, our research output was not adopted due to incorrect conclusions drawn about it.

And we have certainly had projects where everything works well up until the point where we try to figure out where the solution lives, and it sits in limbo instead of being useful.

The Data Science Process emphasizes and requires communication throughout, and relies on teams to establish and maintain relationships instead of working in isolation. With a prescribed set of steps that keep the Data Science team and the problem owner in sync, from establishing expectations about the problem and solution at the outset, to working together to find a home for the solution, the Data Science Process has enabled our Data Team to be more successful and useful to the Rapid7 community, internally and externally. It allows us to make our engineers, our consultants, our products and ultimately you, our customers, happier, more efficient, and more secure.

## Article tags

  * [Research](/blog/tag/research/)