# Stopping Command Injection Attacks by Instrumenting Application Runtimes | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2017/11/09/stopping-command-injection-attacks-by-instrumenting-application-runtimes/
- **Date :** 2025-06-02

---

Command injection (CMDi) attacks are suspected to be behind several high-profile data breaches recently. 

**Command Injection Attacks – A Clear and Present Danger**

The massive [data breach at Equifax](/blog/post/2017/10/5-wrong-lessons-from-equifax-missed-opportunity-of-owasp/) was due to a [vulnerability](https://arstechnica.com/information-technology/2017/09/massive-equifax-breach-caused-by-failure-to-patch-two-month-old-bug/) in a popular web framework that allowed attackers to penetrate their systems through the front door, using what is called a “**Command Injection** ” attack.

What is a command injection attack? Simply, it is a specially crafted web request that attempts to trick a website or application server into executing an operating system command. By executing an arbitrary OS command on the server running the application, an attacker has the potential of further penetrating the system. Once an attacker has this level of access to a system, severe data breaches are possible. For instance, certain susceptible versions of Apache Struts, a widely-used web UI framework can be easily manipulated into executing OS commands with a single http request.

Traditional web security software attempts to detect command injection attacks by looking for certain patterns or special characters that would normally be out of place in a web request. Presence of these patterns provides circumstantial evidence that a request _may_ be attempting to perform a command injection attack. A type of security software called a Web Application Firewall, or WAF, uses this technique for detection of attacks by inspecting the incoming request data and applying static rules that look for incriminating patterns.

There are problems with this approach. Detection is limited to the currently known patterns. As Command Injection attacks become more sophisticated, an attacker can craft a request that evades known pattern detection. By the time new patterns are developed, it might be too late. A false negative can mean a compromised system. If an attack on a vulnerable system slips past a WAF’s pattern detectors, there is nothing a WAF can do to prevent the attack from being executed. Additionally, a WAF exists outside a web application and has no control over it. It can merely block requests it deems malicious. It has no knowledge of OS commands and It has no knowledge of what the application is attempting to execute and has no way of instructing it not to execute an OS command. It only knows patterns inside of requests.

**The tCell Approach**

tCell’s approach to command injection detection is different from WAFs. In addition to looking for circumstantial evidence of an attack, tCell’s agent instruments the runtime of the application where callouts to operating system commands occur. This is where the rubber meets the road. By intercepting calls at this level, all command injection attacks can be detected, reported and blocked. Any attack that slips past the pattern detectors will get stopped when it attempts to spawn an OS command because tCell’s instrumentation knows how these commands are executed and intercepts every single one. This type of protection is simply not possible with a WAF, since a WAF has no knowledge of the inner workings how OS commands are executed in an application runtime and no hooks into that runtime to control execution.

![tCell_Command_Injection.gif](https://www.rapid7.com/cdn/images/blta81e269b108d69fe/683de78a30073e348deb1a66/tCell_Command_Injection.gif)

To intercept commands where they callout to the operating system, tCell instruments the runtimes that major web frameworks run inside – protection is provided for the Java Virtual Machine (J2EE, Servlets, Struts, Spring MVC, Jersey), Node.js (Express, Hapi), Python (Django) and Ruby (Ruby on Rails). For example, in the Java virtual machine, all operating system commands are called from a class called [ProcessBuilder](https://docs.oracle.com/javase/8/docs/api/java/lang/ProcessBuilder.html). Using bytecode instrumentation, tCell efficiently intercepts calls to ProcessBuilder.[start](https://docs.oracle.com/javase/8/docs/api/java/lang/ProcessBuilder.html#start--)() and makes a decision on whether or not to block a command based on whitelist rules. Execution attempts are reported and viewable on tCell’s cloud-based dashboard.

**Undiscovered Vulnerabilities Covered**

If a malicious actor discovers a new vulnerability in a framework, the attack will still be detected at the point it attempts to execute a command. This level of protection is not susceptible to outdated pattern rules or undiscovered vulnerabilities. Additionally, it is not always possible to update vulnerable frameworks rapidly – significant developer time may be required to update older apps. tCell’s OS Command injection monitoring protects vulnerable applications until they can be updated.

tCell’s Command Injection protection includes fine-grained whitelisting of permitted OS commands. An application may legitimately trigger an OS command. For instance, a request may launch the generation of a report that requires an external process. Rather than a blanket ban of OS Commands, tCell allows site operators to run in a discovery mode that reports all OS command executions. Once a survey of allowed commands is made, tCell’s protection can lock down the application and only allow certain commands from certain routes.

**Conclusion**

Command Injection attacks are significant risk to an enterprise’s data security. With the increasing sophistication of attacks, the WAF approach to detect such attacks using patterns to look for evidence is insufficient. tCell’s approach of instrumenting the application runtime and intercepting all Operating System calls ensures past, present and future Command Injection vulnerabilities are covered and no attack slips past application security.

## Article tags

  * [Emerging Threats](/blog/tag/emerging-threats/)