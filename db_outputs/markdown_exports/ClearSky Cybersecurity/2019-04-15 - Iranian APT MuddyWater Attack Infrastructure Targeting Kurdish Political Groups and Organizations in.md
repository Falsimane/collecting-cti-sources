# Iranian APT MuddyWater Attack Infrastructure Targeting Kurdish Political Groups and Organizations in Turkey

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/muddywater-targets-kurdish-groups-turkish-orgs/
- **Date :** 2019-04-15

---

In our ongoing investigations of Iranian APTs, we recently detected additional documents related to previously attack infrastructures used by the Iranian APT – “MuddyWater”, which we [reported](https://www.clearskysec.com/muddywater-operations-in-lebanon-and-oman/) on in late November 2018. 

As a reminder, we identified two domains, that were hacked by the group and used to host the code of POWERSTATS; a malware associated to the group. For additional information on the attack see item – “MuddyWater Operations in Lebanon and Oman”.

However, unlike the previous vector, we did not identify this time any compromised servers used to host the malware’s code. Instead, the lure document already contains the malicious code. We also detected five additional files that operate in a similar file to the aforementioned document; but unlike that file, these do not have any content. 

We believe (with medium certainty) that this is due to the attackers testing the malicious document to see if it is detected by various anti-virus engines. 

## **Targets**

Most of the targets in this wave of attacks are part of Kurdish groups (such as ” Komala” – a Kurdish-Iranian party in Iraq), as well as various organizations in Turkey affiliated with the Turkish army and defense sector. 

## **Attack Vector**

The initial infection vector is via emails attached with a malicious word document. Below are screen-captures of the document sent to the Kurdish party:

![](https://lh3.googleusercontent.com/GQHTFJNAin6Yk-dE61m1ZgI2V4aMsNcHxm4X8Brh8zWPfeNii6DvuhXNJQ45RzAztxN1RBh6UW-LpIWFhGiH3Du25NX-Kfhq7E-9be88dwh5CfNL_t_3yve3I24rfEqCTIAwTcJlTtd8bZCpwQ)

Note that the document is “blurred” and contains the official logo of the Kurdistan Regional Government: 

![](https://lh6.googleusercontent.com/SvvfhOcJUToR7h4LCxBU-Accy-H6VpCsbUlN_JerHz2CPxPOedKHTtscohmrelq2hbEcLdJUbWQs_hZEMZpA2M3gEAyQX1_iWa89LhUs_z9z9YVCxTKt62Fb4E0f5sQN94cn9zTc8hbZHTnCvA)

## **Technical Analysis**

#### _The file used to target the Kurdish party_

As seen, the lure document contains a blurred image that impersonates an official document of the Kurdistan Regional Government. The target is then prompted to Enable Editing or Enable Content, supposedly to view the content. However, this in fact executes an embedded malicious Macro command. 

![](https://lh3.googleusercontent.com/fuX_W0me--enToWa2qxeSh5b4c8RONnYP9HiIanuPLe4MMe_jXbch7kCipWM9M8HvbjoOD0wk24aBLLlral3jC-gPHIeIrJ4__SvuIdDCQpGIY6967nnxqIT-r47XuMQo1YVfE9OvU7Oqz3OVw) ![](https://lh6.googleusercontent.com/RbKp_2fHjJCSBfJH_VjtZUPTJKCLeEVMDE6CEMgYodybIJ_Y_q-SRnWmgjbqNJ3j5GPFC5ZLbaOeI-NMbAK5HaYzslAWV3LJ8Dntk-yJUoDqTvIsy5u-cS_VbrK3CAhc0RcB0bHWkcz-ysN2QA)

This Macro is named Gladiator_CRK. The attacker also used this handle for the Author name in the document’s OLE details: 

![](https://lh6.googleusercontent.com/BIDFTw1rMynQz38qqQWmUOZgDYwCvR5u0uUnYXt_7mPfrHzD68rmweEFNDRF73PKDEeqkztf7mlJwSw5YUdS6z_YgoyRHFDMXx3POYQP5EcV52qZikJSDmvwy5kCyjOnU2ca0pbeQG6B7M9yew)

When investigating this name, we identified several documents that behave to the above document; however, most have no content. It is likely that these files were uploaded to VirusTotal with minor changes to test whether they are detected by the various anti-virus engines. 

It should be noted that all of the content-less files were uploaded from Germany, while the malicious lure document was uploaded from Iraq. This further corroborates our assessment that the content-less files were uploaded for test purposes. 

Similarly to previous attacks by the group, this Macro uses embedded com object that runs Microsoft Excel and concurrently executes various commands. Post execution, the malicious Macro edits certain Registry values in order for the malicious code continues operation even after the compromised system is rebooted, thus insuring persistency. 

![](https://lh4.googleusercontent.com/unZzlmYWn1UcumFrHQ0No-LqwhjmV_L7wAaspXKKbT4rsXVhxWcLTytoLu_Nh9B84eWfOEyuvrX7siSOmsNzkN-44F-D8LgvSycyBpEDTyucTWoT-AR1V7M7H7na2angMAE6BbJvL46bv4AcBg)

Moreover, in a similar fashion to previous attacks, two files are created within the Temp folder. 

These files contain segments of the malicious code used to extract the POWERSTATS malware. 

![](https://lh5.googleusercontent.com/i2YIKOQ2AT2uX6wszsMrUdixnxNKNi8wpqKHZqK4UqbLDqMcDl5SSMfuCmqmuNBOcPkeqo-NAS4BcjvTIPvSGg0jjTAiLKC_ReXNDnxMfKUEXA5pKFHDtoHFVywDdEh-OLTQZ5sAAtglk9PGbA) ![](https://lh5.googleusercontent.com/cxdkM899US4nXsXE6JcYVGoUsChYjiVHRwWbTCDPrPFWRioa7EJpmS29N0FCcK0BWxrVV6tYgN5j2DyPrCPt2Dh58naC-Rrnvw4mhy-q5HYHZZpily70hJkefGZhVRrfLBtkE_QOlqynUhQyyQ)

As seen above, the PowerShell uses Windows Script Host (WScript executable) to decode VBE code from the first image file (icon.ico). This code executes a JavaScript embedded in the second image file (picture.jpg), which is encoded in base64:

![](https://lh6.googleusercontent.com/VfbQWUcS_quTDglWgqFcKRA_XvfYSvzQVd2GXsTFNhOZWbcO2srDRRXzQ6Ov8-SxymLevi0jTWXgLQdn2odM_-oYjeTiW7lCMf6RqPB7QdbG3zCSGNrwL9vi5-2JpvkdBzs04ionipDa6gTckQ)

This method is different from previous attacks, in which that malware was downloaded a C2 server. But, in this attack we did not detect any such request, and the malware were was extracted from the dropper file. 

Below is a screen-capture of files with different content.

![](https://lh5.googleusercontent.com/S8H9sBgvpYl69GxUwwp0OfJ-pB1dWeFEQRC66AG_aWytItJ3Y5v8zUdqfqxjxC3xPrj68JdbfkMn-36Yh2uDCEC3FDKsQCv2wnwumE5nqpciEM_M20g7JUK4Zjl4sqduPs6sB5ObAXmIfMrH-A) ![](https://lh4.googleusercontent.com/QhQDbUQAYY8qYZo5KbMRJeNzL1H1uZzhnbDMjjbtnTiBQk-sq-jzDr8CrHbuACn50830h-Fb3jx7evYguf4m2YxlECRXM2lYKu9Ye_aGYItENEx93_ptBMWRQlcAj_GhwMgWRry3nR0dl5zMAg)

In this attack vector we found that after the target enables the execution of the Macro, an encrypted txt file by the name Win32ApiSyncLog.txt is created. This file contains a base64 encoded Backdoor that downloads the malware from the following URL 94.23.148[.]194/serverscrpit/clientFroneLine/helloServer[.]php. 

![](https://lh3.googleusercontent.com/GwPNavZCyMtBxZKHsnLzQFmLDQnu94yRG07Qrj3rQ-HlJ9hY9OR9sON9CgExSrlyionz6z6XfvL8WO4Fr8WffIqPwbVJOFWUnVl6Dw13fCfAD_NsQ78HozH4kN5SiQOhYETciyh4S84XVchyLg) ![](https://lh5.googleusercontent.com/22fsJghW79c8vXVWBurltwXGCvSjV659bmbLFY5DBzy4VVUy2yoh8bKsBQkt_HMMxkakeuNphyjHNUW62kKItXM4mj3OrA3aIoBscIUVW6AmmooPvoXdU84ohJR_7KI8IfEuUtGi2vpYIggqmg)

Furthermore, a Batch file named Win32ApiSync.bat, which contains the script in charge of running the aforementioned code is created. 

![](https://lh5.googleusercontent.com/RSBm3sOHUenDu2xqq6Lg6C2oV7edpWJP2lryrbMDfIFi97lMkyKX7SKXq0xPV-nGaY07hTgWXaOLr9b_m7vJl11C-RMuqenhaPqT11g-GKoKKeFfeGbU2022ANL-l9RPqhtmyR1hHbVyWsyCXw)

This script creates a scheduled task (schtasks) that creates, reads and extracts the Win32ApiSync file every hour. 

![](https://lh3.googleusercontent.com/mtZ3wWaJ3cKJEg6f1j9DMmX29Bu_fCAw80yfEwp9IBjzW9xfJ7Sqn8-R20PMRrroSzlCGFoJ1ZfG4K36TSHd3_NTb-wHmCXDhTknEcmOZ1wi8b5y88YLWaxKHlFLFNtQQeU1qxOWceufZ7tqCg)

However, unlike the first document, despite the “enable content” prompt, this document does not contain any malicious Macros. 

This may explain way, unlike the other file, no PowerShell were installed on the computer via an Excel process. From the OLE details it seems that the file was recently edited by an individual named ” Babak Amiri”. 

When searching for additional files additional by this author we detected several documents, but they too did not contain any Macros. 

![](https://lh5.googleusercontent.com/pxeKPdmsZeP-j3bhJ-89xi7UcjlZHMbr5W7vUkL3aEbeC_a_NIZlw2v1GcIfm4lAN-iFQ6fpu4wcyx52iAijBW2ukCfwT8bFFn7tYjhJ5kqe_Q80tJkpds8qEmTJuL4xB667KEuE5YxcSJaqNQ)

![](https://lh5.googleusercontent.com/nyGyfAZM3qFTqGUwEkk_HNRACu0JV4a74zJ1f3g1hS0mVaivXMP5GTUsx70tEh6mMg-sCOQ1T3TM7nyHJOTWMxkr3VGXEnUMYIkhflQrauFSaaEAbUhnNwJ0qKCyiRWyottGx3y4l2fdYWkfdg) ![](https://lh6.googleusercontent.com/RuD83DJlMNDtq_jSP8VCXvxgEVM_B2hGIy3cww_Wxi7ikxUn8V80BjQCBumgI3QgnsDyI-lSlS_QMRSxRixsxTixj1z6fMM71Z6lrBMBtbt16OVmZX14UySLqSHQY5QUtPxxF40tX0ux1k9zsg)

#### **Indicators**

**Indicators of Compromise (IoC) are available for subscribers of ClearSky threat intelligence services in MISP events numbers – 1449, 1493**

d4de6b8ffcd878359315594515dd33c0  
cc183b583d24147766533876d9b9b54b6f1f4aaf  
d4de6b8ffcd878359315594515dd33c0  
21aebece73549b3c4355a6060df410e9  
2b938a9b20e7abcadd28a0f461a4e5d8  
062a8728e7fcf2ff453efc56da60631c738d9cd6853d8701818f18a4e77f8717  
4dd641df0f47cb7655032113343d53c0e7180d42e3549d08eb7cb83296b22f60  
eed599981c097944fa143e7d7f7e17b1  
7b4da8f9ffa435c689923b7245133ee032f99fcd841516f2e2275fb4b76d28f9  
78c1279f80c76d12debf9e875d14b4788bd88a39  
bef9051bb6e85d94c4cfc4e03359b31584be027e87758483e3b1e65d389483e6  
b604dd6517dfd0df72e52ebc3f92da699c1396cd  
dbab599d65a65976e68764b421320ab5af60236f  
0638adf8fb4095d60fbef190a759aa9e  
5c6148619abb10bb3789dcfb32f759a6 a3bb6b3872dd7f0812231a480881d4d818d2dea7d2c8baed858b20cb318da981  
0d3e0c26f7f53dff444a37758b414720286f92da55e33ca0e69edc3c7f040ce2  
c8b271efec98e83a343933a32eff30d5  
6d0050f16c61cf1584bdfd6ab891d5b9d4d6bbf3  
34bfdae99838f048d9950614d338ec06653eacee  
6f882cc0cddd03bc123c8544c4b1c8b9267f4143936964a128aa63762e582aad  
c25eeac6044dbc87c37063a9c6ed80c73966e41d50fc96065c2793fbf841ef3c  
9732cf8c9e84e992d8856537dc5988371bb73f7c  
f12bab5541a7d8ef4bbca81f6fc835a3  
a066f5b93f4ac85e9adfe5ff3b10bc28  
8a004e93d7ee3b26d94156768bc0839d  
09aabd2613d339d90ddbd4b7c09195a9  
8a7b2167c14a0158b3e9a43453a3e8f3  
cfa845995b851aacdf40b8e6a5b87ba7  
76f6c0bf075f9ae02a9a9e08cce1297d  
5c1af7d3dbb9bc455b793f1e3e0b2554  
51.255.219.222  
46.105.84.146  
185.247.137.89  
94.23.148.194  
46.105.84[.]146:443/WordOffice.jpg