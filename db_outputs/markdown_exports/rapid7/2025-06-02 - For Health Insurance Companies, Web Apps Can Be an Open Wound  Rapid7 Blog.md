# For Health Insurance Companies, Web Apps Can Be an Open Wound | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/02/23/for-health-insurance-companies-web-apps-can-be-an-open-wound/
- **Date :** 2025-06-02

---

At IntSights, a Rapid7 company, our goal is to ensure organizations everywhere understand the threats facing them in today's cyber landscape. With this in mind, we took a focused look at the insurance industry — a highly targeted vertical due to the amount of valuable data these organizations hold.

As part of this research, we reviewed threats specific to each vertical in the insurance industry. Healthcare insurance providers, in particular, have large targets on their backs. Criminals often aim to breach healthcare providers to gain access to various personal health information (PHI), which can include everything from sensitive patient health information to healthcare insurance policy details. Once this data falls into the wrong hands, it can be used to conduct fraud and exploit patients in a variety of ways.

This being the case, health insurance providers need to lock down their security perimeter as much as possible, and there's one broader problem affecting the industry we want to highlight here: [web app security](/fundamentals/web-application-security/). Security bugs or misconfigurations of public-facing customer web applications can often be overlooked, and they are major areas of concern because they serve as entry points for bad actors.

Let's explore why these vulnerabilities are dangerous, how they happen in the first place, and what healthcare insurance providers can do to mitigate these threats and protect their policyholders.

## Web apps as an entry point

Public-facing web applications are commonly used in the insurance industry to gather information about an individual or an organization. This data is often leveraged to generate a quote estimate for the type of insurance policy the person or company is looking for. While this can be a helpful way to personalize the customer experience and attract more customers to your business by showcasing competitive rates, it can also inadvertently expose inputted information if the app is misconfigured.

Take, for example, a vulnerability discovered in home and pet insurance provider [Lemonade's website](https://techcrunch.com/2021/05/13/lemonade-insurance-bug-exposed-account-data/). By simply clicking on public search results, a person could access and edit customers' accounts without providing any credentials. From there, a bad actor could steal personally identifiable data and exploit it with barely any hassle at all.

The shocking part of this incident is that Lemonade spokespeople claimed this website flaw was “by design." During the setup of the website, the team responsible likely didn't realize anyone could log in, access a customer's account, and even download a copy of that individual's insurance policy. Since then, the indexed search results have stopped working, but it just goes to show how a simple oversight like that can be an open door for bad actors, who usually have to search much harder to find and exploit a vulnerability.

This is why health insurance companies should pay extra attention to how their public-facing apps, websites, and portals are configured. With the treasure trove of PHI they store — including everything from COVID-19 vaccination records to insurance policy details that list patient Social Security numbers, birthdates, and even Medicare or Medicaid coverage — healthcare organizations are prime targets for hackers eager to conduct insurance fraud, and a misconfiguration could give them easy access to this data.

## How do misconfigurations happen?

Misconfigurations can happen at any level of an application stack, from the application server to the network services and beyond. As such, bad actors will try to exploit any misconfigurations in your stack by looking for unpatched flaws, unused pages, unprotected files or directories, and even dummy accounts that can get them into a system and open up access to data from within. This can lead to a complete system compromise and should be taken seriously.

But how do misconfigurations happen in the first place? Here are a few of the most common security [misconfigurations in web apps](https://betanews.com/2022/01/21/insurance-businesses-targeted-for-customer-details/):

  * **Exposing too much information** : If an attacker discovers what type of software you're using for a public-facing web application, it will be much easier for them to search for and find vulnerabilities. There are some clever ways they go about learning this information; for example, they may be able to tell from an error message what type of back end you're using. Anything that reveals stack traces or exposes information about what systems you're using needs to be taken care of.
  * **Default settings** : When deploying new software, it usually comes out of the box with all functionality activated. However, every extra functionality is just another point of entry that you need to lock down. Never leave all default settings on, and make sure to change default accounts and passwords for everything, from admin consoles to hardware.
  * **A lack of permissions** : When your user permissions or account security settings are not strict, attackers may be able to access an account and run commands in the operating system. In the Lemonade example, for instance, anyone that found the account pages through search could log into the accounts without inputting user credentials.
  * **Outdated software** : Updating and patching software regularly is required to shore up any security vulnerabilities. This is even more critical for public-facing applications, as bad actors will often run down a list of known vulnerabilities to exploit a system. If the software isn't up to date, it could leave a wide-open hole in your defenses.



## How to resolve and prevent configuration issues in web apps

For healthcare security and health IT teams looking to find, fix, and prevent configuration issues in web apps, here are a few ways you can start:

  * **Establish secure installation processes**. A repeatable hardening process will help you deploy new software faster and easier in the future. This process, once outlined, should then be configured identically across your environments and automated to minimize effort.
  * **Do not install unused features and frameworks**. When first setting up your application, don't deploy with the default settings. Review every feature, functionality, and framework, and remove any you do not want or plan to use. This will help you launch with a minimal platform that will be easier to harden.
  * **Implement strict permissions**. Ensure that different credentials are used in each environment, from development to production. Default user accounts and passwords should always be changed as soon as possible, and you will want to implement strict requirements for credentials.
  * **Review and update configurations regularly**. You might think you're done once you've deployed your app, but you should always come back to review and update configurations on a consistent basis. Scan for errors, apply patches, and verify the effectiveness of your configurations and settings in all environments for maximum protection.
  * **Generate a software bill of materials (SBOM) and cross-reference it against vulnerabilities often**. It's important to know every component comprised within a piece of software. You can easily generate an SBOM with a variety of open-source and commercially available third-party applications, and once you have it in hand, regularly cross-reference the components in it against known vulnerability lists.



Cyber threat intelligence can also help, as it can inform your health IT team about any threats facing your web app security. For example, threat intelligence can reveal what bad actors hope to acquire from your web apps and the methods they may try to use to obtain it. When you gather key information like this, you can tailor your defenses appropriately.

By leveraging robust cyber threat intelligence solutions and performing rigorous testing and scrutiny of public-facing web applications and other infrastructure, health insurance organizations and their healthcare security teams can better protect their environments and avoid inadvertently exposing customer data.

## Article tags

  * [Threat Intel](/blog/tag/threat-intel/)
  * [Application Security](/blog/tag/application-security/)