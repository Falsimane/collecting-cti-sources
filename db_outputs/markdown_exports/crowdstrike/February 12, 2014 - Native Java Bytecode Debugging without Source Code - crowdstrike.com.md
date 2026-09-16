# Native Java Bytecode Debugging without Source Code - crowdstrike.com

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/native-java-bytecode-debugging-without-source-code/
- **Date :** February 12, 2014

---

# Native Java Bytecode Debugging without Source Code

February 12, 2014

• [ editorialteam](/en-us/blog/author.editorialteam/ "Posts by editorialteam") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

At CrowdStrike, we’ve seen a moderate increase in Java-based malware recently, with Remote Access Tools (RATs) like Adwind becoming increasingly prevalent. Reverse engineering Java is typically very straightforward, since excellent Java binary decompilers have existed for years. Tools like [JD-GUI](http://jd.benow.ca/#jd-gui) make Java analysis a breeze and do an excellent job at recovering Java binaries’ source code (minus the comments). In cases where we need to dynamically debug Java programs, decompiled Java can be exported from the decompiler and then imported into a Java IDE like [Eclipse](http://www.eclipse.org/eclipse/) as part of a new Java project. This allows us to build a project using the decompiled code and then dynamically debug it through the IDE. However, this all goes out the window when dealing with Java bytecode-based obfuscation, as most Java IDEs won’t compile raw JVM instructions, nor allow you to step through these instructions without the original source code.

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase6464845a3af35e734e.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase6464845a3af35e734e.png)

_Decompiled Non-Obfuscated Java_

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64c4b7fcb3e87db84a.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64c4b7fcb3e87db84a.png)

_Decompiled Obfuscated Java_

The best solution we’ve found for debugging malware’s native Java bytecode is Dr. Garbage’s Bytecode Visualizer. We haven’t seen any thorough walkthroughs on installing and using Bytecode Visualizer, so this blog entry serves as a step-by-step guide on how to dynamically analyze native Java bytecode with Bytecode Visualizer:

## 1\. Install the Java SE JDK

The Java Standard Edition Development Kit can be downloaded from Oracle’s website at http://www.oracle.com/technetwork/java/javase/downloads/index.html. JDK 7 is currently the latest version and can be downloaded directly from http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html.

During the JDK installation, be sure to have the JDK installer install the Public JRE as well if it isn’t already installed:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64795d9fe79cbff847.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64795d9fe79cbff847.png)

_Installation Options_

## 2\. Install Eclipse

The Eclipse IDE for Java Developers can be downloaded from <https://www.eclipse.org/downloads/packages/eclipse-ide-java-developers/keplersr1> (the download links are on the right side of the page).

## 3\. Install Bytecode Visualizer

Run Eclipse and in the menu bar go to Help → Eclipse Marketplace…

In the Search tab of Eclipse Marketplace window, type “Dr. Garbage” into the Find textbox and press the Go button:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase6480112931cbe22f97.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase6480112931cbe22f97.png)

_Eclipse Marketplace_

Scroll to Bytecode Visualizer and press the Install button. Once installation is completed, restart Eclipse when prompted.

## 4\. Load the JAR to be Analyzed

Once Eclipse restarts, close the Welcome tab, and in the menu bar go to File → New → Java Project. Specify any project name you like and press the Next button:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64a420fad25441eff5_0.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64a420fad25441eff5_0.png)

_Create a Java Project_

In the Java Settings window, click the Libraries tab. In the Libraries tab, press the Add External JARs button and select the JAR file you want to debug, thereby adding it to the Java project’s build path:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64b0d0d1625a7f33f2.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64b0d0d1625a7f33f2.png)

_Java Settings_

Once the JAR has been added to the build path, press the Finish button.

## 5\. Open the JAR’s Code with Bytecode Visualizer

In the Package Explorer tab, expand your project’s Referenced Libraries to find your JAR file. Right-click on the class you want to debug and select Open with Bytecode Visualizer:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase645d60aef8c7557e95-1024x753.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase645d60aef8c7557e95.png)

_Open with Bytecode Visualizer_

## 6\. Set Breakpoints

With the JAR’s code now visible in Bytecode Visualizer, you can set breakpoints by double-clicking on the vertical gray bar to the left of the disassembled Java code:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64d6ea17c17e000ade-1024x753.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64d6ea17c17e000ade.png)

_Setting a Breakpoint_

Note that Bytecode Visualizer only allows you to set breakpoints on method entrypoints (the first instruction of a method); you can’t set breakpoints on arbitrary instructions.

## 7\. Debugging the Disassembled Code

You can now run the disassembled code by right-clicking on the class you want to debug and choosing Debug As → Java Application:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64cccd2ddaba2f8ce5-1024x753.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase64cccd2ddaba2f8ce5.png)

_Debug as Java Application_

In the Debug perspective view, there are buttons to Step Into Bytecode and Step Over Bytecode (circled in red below). Use the Step Over Bytecode button to perform standard single-stepping; use the Step Into Bytecode button only to step into calls. The Debug perspective also allows you to see local variable in the Variables tab, and to add your own watches in the Expressions tab (you can add this tab via Window → Show View → Expressions in the menu bar); you can see below that I added a watch/expression for variable b:

[![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase6450de3b4d71d6cc5e-1024x753.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/pngbase6450de3b4d71d6cc5e.png)

_Debug Perspective_

As far as we’ve seen, Bytecode Visualizer does not offer a view of the raw JVM stack, but even without it, tracing the code flow via single-stepping and examining memory with the Variables and Expressions tabs should typically allow you to successfully debug your target as needed.

For more information on Java-based malware or the adversaries using it, including detection logic or any of the adversaries tracked by CrowdStrike, please contact: [intelligence@crowdstrike.com](mailto:intelligence@crowdstrike.com) and inquire about our Intelligence subscription. To get full access to CrowdStrike's next-gen antivirus solution for 15 days visit the [**Falcon Prevent free trial page**](/content/crowdstrike-www/locale-sites/us/en-us/resources/free-trials/try-falcon-prevent/?ctm_source=Website&ctm_medium=Blog&ctm_campaign=Blog-Inline-Copy).

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)