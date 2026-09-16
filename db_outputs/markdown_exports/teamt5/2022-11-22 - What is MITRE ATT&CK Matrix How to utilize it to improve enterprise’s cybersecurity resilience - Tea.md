# What is MITRE ATT&CK Matrix? How to utilize it to improve enterprise’s cybersecurity resilience? - TeamT5

- **Source :** teamt5
- **URL :** https://teamt5.org/en/posts/what-is-mitre-att-and-ck-matrix/
- **Date :** 2022-11-22

---

ThreatVision Resources

SubscribeRSS

# What is MITRE ATT&CK Matrix? How to utilize it to improve enterprise’s cybersecurity resilience?

2022.11.22Product Management

Share: 

## About MITRE ATT&CK Matrix

MITRE is a non-profit organization in the United States that conducts various advanced technology research for the United States government. Cybersecurity is a key part of its research and development.

MITRE launched the ATT&CK (Adversarial Tactics, Techniques & Common Knowledge) concept in 2013, aiming to help enterprises and organizations have a common language and structure to understand and analyze network attack methods, and then plan cybersecurity countermeasures.

## Framework of MITRE ATT&CK Matrix

MITRE ATT&CK Matrix is presented as a table which is easy for people to read. It also provides 2 types of info which can be automatically read by systems -   
**1\. STIX** : A structured language for threat intelligence   
**2\. TAXII** : Threat intelligence transmission mechanism   


## MITRE ATT&CK Matrix 3 major types

MITRE ATT&CK Matrix is ​​divided into three categories. Users can simply judge based on their own situation and refer to different tables to judge threats and plan security countermeasures.

**1\. Enterprise Matrix** : Provides attack methods used on computer devices such as Windows, Linux, MacOS, etc.   
**2\. Mobile Matrix** : Provides attack methods used on mobile devices   
**3\. Pre-ATT &CK**: Provides pre-attack methods before infection   


## Basic elements of MITRE ATT&CK Matrix

By interpreting the basic items in the MITRE ATT&CK form (see Figure 1), companies can communicate across teams and organizations more effectively.

First, explain the meaning of the table fields:

  * The first column represents "Tactics": it can be understood as the goal that the attacker wants to achieve.

  * The multiple items below the row represent "Techniques": they can be understood as the types of techniques used to achieve tactical goals.




![what-is-mitre-att-and-ck-matrix_pic1](https://uploads.teamt5.org/upload/original/what-is-mitre-att-and-ck-matrix_pic1.jpg) Figure 1: Enterprise Matrix (Source: [MITRE](https://attack.mitre.org/matrices/enterprise/))

For example, if an attacker wants to complete the tactic "Execution" (*Note 1) numbered TA0002, he must use the technical methods underlying this tactic to complete it, such as: Deploy container, Native API, etc.

And if the vision is further improved to a complete attack behavior, the tactical sequence is usually from left to right (for reference only, the actual attack behavior will be more complicated). Therefore, a complete attack behavior may be woven from multiple "Tactics" and their corresponding "Techniques".   
  
Secondly, we continue to dismantle MITRE ATT&CK, in which "Techniques" provides the following information:

  * Describe

  * Example

  * Reference

  * Recommendations for mitigation and detection




These contents not only help MITRE readers understand, but more importantly, users can use these common languages ​​to find trustworthy threat intelligence and cybersecurity vendors, and obtain more and more effective investigation reports and tools.

### How can enterprises achieve cybersecurity defense goals through the combination of threat intelligence and MITRE ATT&CK Matrix?

The MITRE ATT&CK Matrix not only serves as a recognized technical communication language, but also serves as a common framework for malicious behavior between attack and defense parties. Therefore, the MITRE ATT&CK Matrix can become a classification reference for enterprises’ daily defense behaviors to help enterprises confirm their current cybersecurity status, and can also serve as the basis for penetration testing and red team drills.

As mentioned above, the MITRE ATT&CK Matrix is ​​very easy to use in actual fields when paired with threat intelligence. Enterprises can track malicious groups (or hacker groups) through the correlation of known technologies and strategies. This is because defenders provide a clear picture of the current situation.

Enterprises only need to organize the following two pieces of information to quickly check whether their own unit's preventive measures against certain malicious groups are accurate, and use the IoC and Tool kit provided by intelligence vendors to immediately strengthen weaknesses -

  1. What techniques can the current unit’s cybersecurity configuration effectively prevent?

  2. The malicious groups we are currently facing and their usual methods (can be known through intelligence reports)




Enterprises can use the above two pieces of information at the same time to create MITRE ATT&CK Navigator entries for specific malicious groups. Based on the current security environment and the known information of specific malicious groups, enterprises can use it as a visual analysis method to confirm their own strengths and weaknesses. As shown in Figure 2. ![what-is-mitre-att-and-ck-matrix_pic2](https://uploads.teamt5.org/upload/original/what-is-mitre-att-and-ck-matrix_pic2.jpg) Figure 2: MITRE ATT&CK Navigator entries (Source: [MITRE](https://mitre-attack.github.io/attack-navigator/v2/mobile/))

## Summarize

Senior positions such as Chief Information Security Officer (CISO) or head of the information technology department can have a clear understanding when thinking about the planning and allocation of the cybersecurity budget. This framework is also useful for cybersecurity researchers and the cybersecurity incident response unit to quickly identify its own weaknesses and prioritize investigation using specific methods.

In addition, members of the information department and Security Control Center (SOC) that extend to the front line can also very clearly obtain and import Indicators of Compromise (IoC) and various prevention tools for specific techniques. Members only need to use the formats mentioned at the beginning of this article - STIX format and TAXII transmission mechanism to easily import these IoC or tools into devices and systems.

TeamT5 recommends that the security team can use the MITRE ATT&CK Matrix, a common language, to not only connect the communication bridge between attack and defense, but also create a platform for the security team to move from top to bottom (strategic level - tactical level - actual combat level) The language of communication enables the cybersecurity team to better implement the guidelines at all levels proposed in the threat intelligence report to ensure that cybersecurity protection at all levels can be quickly strengthened through the application of threat intelligence reports.   
  


*Note 1: "Execution" refers to malicious attackers executing malicious code, executing malicious instructions through Cmd or Powershell in Windows, even programming languages ​​​​(Python or JavaScript), and possibly through the Internet. The device's CLI to execute malicious commands.

  


> TeamT5 consists of top cyber threat analysts. Leveraging our geographic and cultural advantages, we have the best understanding of cyber attackers in Asia Pacific. TeamT5 is frequently invited to share insights at top cybersecurity conferences. Our threat intelligence research expertise and solutions are recognized as the 2023 Company of the Year Award in Taiwanese Threat Intelligence by Frost & Sullivan. Our endpoint detection and response solution is wardesd Golden Award from Computex - Best Choice Award.
> 
> Contact us now to take the crucial step of enterprise cybersecurity defense: <https://teamt5.org/en/contact-us/>

2022.11.22Product Management

Share: 

### Related Post

[ThreatSonar Resources2022.10.31](/en/posts/threatsonar-as-rapid-test/)

#### [Preventing hackers is like preventing epidemics. Enterprise computers should also do rapid tests!](/en/posts/threatsonar-as-rapid-test/)

APT

![](https://teamt5.org/en/posts/what-is-mitre-att-and-ck-matrix/)