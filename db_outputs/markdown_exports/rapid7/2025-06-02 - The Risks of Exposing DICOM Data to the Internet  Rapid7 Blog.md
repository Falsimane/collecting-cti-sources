# The Risks of Exposing DICOM Data to the Internet | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2023/10/11/the-risks-of-exposing-dicom-data-to-the-internet/
- **Date :** 2025-06-02

---

### Introduction

Digital Imaging and Communications in Medicine (DICOM) is the international standard for the transmission, storage, retrieval, print, and display of medical images and related information. While DICOM has revolutionized the medical imaging industry, allowing for enhanced patient care through the easy exchange of imaging data, it also presents potential vulnerabilities when exposed to the open internet. 

About five years ago, I was in the hospital while an ultrasound was taken of my pregnant wife. While the doctor made the images, a small message on the screen got my attention: “writing image to disk - transfer DICOM.” Digging into the DICOM standard at the time resulted in being able to discover exposed systems over the internet, retrieve medical images, use demo software, and 3D-print a pelvis. An example of that research is still available online [here](https://www.forbes.com/video/5814849480001/what-a-3d-printed-pelvis-can-teach-us-about-network-security/). It’s now five years later, so I was curious to see if things had changed (and no worries—I will not 3D-print another body part 😉).

This article delves into the risks associated with the unintended exposure of DICOM data and the importance of safeguarding this data.

### Understanding DICOM

DICOM is more than just an image format; it encompasses a suite of protocols that allow different medical imaging devices and systems, such as MRI machines, X-ray devices, and computer workstations, to communicate with each other. A typical DICOM file not only contains the image but also the associated metadata, which may have patient demographic information, clinical data, and sometimes even the patient’s full name, date of birth, and other personal identifiers.

### What Are the Exposure Risks?

  1. Breach of Patient Confidentiality: The most pressing concern is the breach of patient confidentiality. If DICOM data is exposed online, there's a high risk of unauthorized access to sensitive patient information. Such breaches have the potential to result in legal consequences, financial penalties, and damage to the reputations of medical institutions.
  2. Data Manipulation: An unprotected system might allow malicious entities not only to view but also to alter medical data. Such manipulations have the potential to lead to mis-diagnoses, inappropriate treatments, or other medical errors.
  3. Ransomware Attacks: In recent years, healthcare institutions have become prime targets for ransomware attacks. Exposing DICOM data could potentially provide a gateway for cybercriminals to encrypt vital medical information and demand a ransom for its release.
  4. Data Loss: Without proper security measures, data could be accidentally or maliciously deleted, leading to loss of crucial medical records.
  5. Service Interruptions: Unprotected DICOM servers could be vulnerable to denial-of-service (DoS) attacks, disrupting medical services and interfering with patient care.



### Research

While previously I focused on the imaging part of the protocol, this time I looked into the possibility of retrieving PII data* from openly exposed DICOM servers. 

Using Sonar, Rapid7’s proprietary internet scan engine, a study was conducted to scan for the DICOM port exposed to the internet. Using the output of the scan, a simple Python script was created that used the IP addresses discovered as input, whereby a basic set of DICOM descriptors from the “PATIENT” root-level were queried. The standard itself is very extensive and contains many fields that can be retrieved, such as PII related data including name, date of birth, comments on the treatment, and many more.

Unfortunately, we were able to quickly retrieve sensitive patient information. No need for authentication; we received the information simply by requesting it. The following screenshot is an example of what we retrieved, with the PII altered for privacy purposes.

Importantly, our results not only discovered hospitals, but also private practice and veterinary clinics.

When scanning for systems connected to the internet, we focused on the two main TCP ports: TCP port 104 and TCP port 11112. We ignored the TCP port 4242 since that is mostly used to send images. In total we discovered more than 3600 results that replied to these two ports.

Although it might be interesting to geolocate where these systems are, we believe that it is better to investigate which systems are really possible candidates that we can retrieve data from and geolocate those.

### TCP port 104 stats

After retrieving the list of IP addresses that responded to the open port and matched a DICOM reply, we scanned the list by using a custom script that would query if a connection could be established or not. The following diagram shows the results of this scan.

In 45% of cases, the remote server was accepting a connection that could be used for retrieving information.

### TCP port 11112 stats

Next, we used the list of IP addresses that responded to a DICOM ping reply on TCP port 1112. Again we used our script to query if a connection could be established or not. The diagram below shows the results of this particular scan.

Of the total number of 1921 discovered systems responding to our DICOM connection verification script, 43% of these systems were accepting a connection that could be used for retrieving data.

Since we now know how many systems are connected, accepting connections to retrieve the information, let’s map those out on a global map, where each orange colored country is a country where systems were discovered:  
  
Not much seems to have changed since my initial research in 2018; even searching for medical images using a fairly simple Google query results in the ability to download images from DICOM systems, including complete MRI sets. The image below showcases an innocent example from a veterinary clinic where an X-ray of an unfortunate pet was made.

### Conclusion

While DICOM has proven invaluable in the world of medical imaging, its exposure to the internet poses significant risks. Healthcare institutions are the prime targets of threat actors; therefore, these risks have detrimental implications on patients' healthcare services and consumer trust, and they cause legal and financial damage to healthcare providers.

It's essential for healthcare institutions to recognize these risks and implement robust measures to protect both patient data and their reputations. As the cyber landscape continues to evolve, so too must the defenses that guard against potential threats. Healthcare organizations should make it a part of their business strategy to regularly scan their exposure to the internet and institute robust protections against potential risks.   


_*Note: Where possible, Rapid7 used their connections with National CERTS to inform them of our findings. All data that was discovered has been securely removed from the researcher’s system._

## Article tags

  * [Research](/blog/tag/research/)