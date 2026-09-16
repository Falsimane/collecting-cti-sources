# Unveiling the Inner Workings of DiceLoader

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/unveiling-the-intricacies-of-diceloader
- **Date :** 2024-02-01

---

## Introduction

**FIN7** is an intrusion set operating since at least 2015. The group is known to be **structured** as a corporate business composed of Russian-speaking members. FIN7 hides its illicit activities behind **front companies** , which are likewise used to recruit IT experts who are not aware of the malicious activities they are involved in.

The intrusion set targets various sectors of activity (_e.g._ retail, hospitality, food service industry) within different geographical areas such as the United States, the United Kingdom, Australia and France. 

FIN7 members were reported being affiliated to other cybercriminal organisations such as REvil, Lockbit, [Darkside](https://www.prodaft.com/m/reports/FIN7_TLPCLEAR.pdf) and also [BlackBasta](https://assets.sentinelone.com/sentinellabs22/SentinelLabs-BlackBasta).

The intrusion set’s arsenal notably includes malware such as loaders, ransomware or backdoor, of which a great part is custom malware (_e.g._ Carbanak Backdoor, Domino Loader, Domino Backdoor, DiceLoader, _etc_). **DiceLoader** appears to be also sold for quite a long time. However, we assess with high confidence that the malware is still used by this intrusion set in their campaigns. We observed, in the FIN7 context, that the malware is dropped by a PowerShell script that uses the FIN7 specific obfuscation along with other malware of their arsenal named Carbanak.

This report aims to detail the functioning of a malware used by FIN7 since 2021, named **DiceLoader** (also known **Icebot)** , and to provide a comprehensive approach of the threat by detailing the related _Techniques_ and _Procedures_.

The sample used for this analysis was extracted from this PowerShell (stage-0):

  * PowerShell: SHA-256: [ffb1573c4dd003c4750a2a5d66c1d9061a159e83f2f945f12d1b1c47cc62ab77](https://bazaar.abuse.ch/sample/ffb1573c4dd003c4750a2a5d66c1d9061a159e83f2f945f12d1b1c47cc62ab77/)
  * DiceLoader DLL: SHA-256: [75b9346e9c803f7e942c7be69d3a93902bfdc6b10ad4142c4e5be473546a9165](https://bazaar.abuse.ch/sample/8a287fbd024544c34b5db983af093504d25be864a821010f4cd2d00a2a6ad435/)



## Sample dissection

DiceLoader is a small-sized malware, part of the FIN7**arsenal** , belonging to the **downloader** family. It uses multiple **internal structures** to hinder analysis. The next sections of this report explain how the loader works by analysing its workflow along with the data **structures** , the program architecture, the different **obfuscation** techniques and finally its **network** state machines.

## Loader context

In FIN7 campaigns observed by Sekoia.io analysts, DiceLoader is dropped by a [PowerShell script](https://bazaar.abuse.ch/sample/ffb1573c4dd003c4750a2a5d66c1d9061a159e83f2f945f12d1b1c47cc62ab77/) along with other malware of the intrusion set’s arsenal such as Carbanak RAT (Remote Access Trojan). The loader is a DLL whose default entry point (exported function Ordinal #1) has a random name which corresponds to the “**Reflective DLL injection** ” module available on [Github](https://github.com/stephenfewer/ReflectiveDLLInjection).

This module is used to inject the DiceLoader main entry point into another process memory. Below, it refers to the function DllEntryPoint (address: 0x100018E3).

![Figure 1. Exported functions from DiceLoader DLL sample ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f876_6a92a30e2b0ef7af46bcd54c_6a2a7cb66d8eb6f373ee6028.webp)

Figure 1. Exported functions from DiceLoader DLL sample 

‍

**Reflective DLL injection** is a library injection technique in which the concept of reflective programming is employed to perform the loading of a library from memory into a host process. As such the library is responsible for loading itself by implementing a minimal Portable Executable (PE) file loader. It can then govern, with minimal interaction with the host system and process, how it will load and interact with the host ([source](https://github.com/stephenfewer/ReflectiveDLLInjection)).

_NB: To facilitate the analysis of a malware using the Reflective DLL Injection, here is an adjusted_[ _C header file_](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/DiceLoader/scripts/ReflectiveDLLInjection.h) _ingestible by IDA._

## Data structure used by DiceLoader

The first function executed by the malware sets up the principal **data structures** and **mechanisms** used by the loader for its future execution. 

In this function, it initialises four **criticalSections** used for the thread context to provide mutex objects and then creates a **IoCompletionPort** for the inter-thread communications. 

Finally, it allocates four empty **linked lists** used to connect each part of the program **to structure** the data in memory; this mechanism is detailed in a dedicated section.

### Threading and Io Completion Port

As introduced previously, DiceLoader starts multiple threads that consume a specific data structure which will be the subject of the next section; these threads are dubbed “**consumer** ” in the rest of this report. 

Part of the main thread activity is to receive, to parse and to format incoming TCP packets and to forward them to the Consumers. Consumers are infinite loops used to consume structured messages coming from the C2 server. 

![Usage of IoCompletionPort \(queue\) in DiceLoader execution. Source: Sekoia.io](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f89d_6a92a31e65cc84bc266e9bef_6a2a7cb66d8eb6f373ee6059.webp)

Figure 2. Usage of IoCompletionPort (queue) in DiceLoader execution. Source: Sekoia.io

The communications between the main thread and the Consumers are done by the [IoCompletionPort](https://learn.microsoft.com/en-us/windows/win32/fileio/i-o-completion-ports) file handle. 

 _NB-1: According to MSDN this mechanism has been designed to fit asynchronous needs and to provide an efficient threading model. Under the hood, IoCompletionPort are queues in first-in-first-out (FIFO) order._

_NB-2: The term file handle as used here refers to a system abstraction that represents an overlapped I/O endpoint, not only a file on disk. Any system objects that support overlapped I/O such as network endpoints, TCP sockets, named pipes, and mail slots can be used as file handles (_[_source_](https://learn.microsoft.com/en-us/windows/win32/fileio/i-o-completion-ports) _)._

On one hand, the threads consume the queue in the infinite loop using the GetQueuedCompletionStatus method, on the other hand the main thread pushes incoming messages using PostQueuedCompletionStatus. Regarding the threading context, DiceLoader uses a critical section to protect the shared resources (the four linked lists) from simultaneous access.

### Linked List used by DiceLoader

To access structued data during its execution, DiceLoader uses the **linked list** data structure - a **linear data structure** where the elements are **not stored** in a **contiguous** memory location. The data structure of a node in the list is the following one:

`struct node  
  
{  
  
_DWORD *head; // Pointer to the head of the list  
  
_DWORD *node; // Pointer to the current node data  
  
_DWORD size; // Size of the node  
  
_DWORD buff_size; // Internal node buffer size  
  
_BYTE nid; // ID used for the node creation  
  
};  
`

Code 1. C declaration of the linked list element structure

As introduced above, the loader required to access these linked list across threads; therefore implying the uses of critical section, here is the implementation of a new element insertion within the list:

![Linked List used by DiceLoader](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f86d_6a92a3112e47a1e9fe0dda4d_6a2a7cb66d8eb6f373ee6031.webp)

Figure 3. Function to insert an element in the linked list 

‍

During the analysis of the malware, only few functions were implemented to interact with the linked list: 

![List of functions implementation in DiceLoader to use linked list](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f87c_6a92a30fa49553afbaf31075_6a2a7cb66d8eb6f373ee602b.webp)

Figure 4. List of functions implementation in DiceLoader to use linked list 

The malware creates four linked lists dubbed **L0** , **L1** , **L2** and **L3** for the purpose of the analysis. These lists manipulate various structures such as the fingerprint of the host, the received payload and the shellcode wrapper.

This analysis is focused on **L0** and **L3** where **L0** is used to contain formatted messages coming from the C2 and **L3** is used to store the shellcode wrapper and the payload.

### Diceloader obfuscation methods

DiceLoader has **two** obfuscation methods:

1\. To deobfuscate the configuration **C2**(s): IP address(es) and port(s)

2\. To deobfuscation the **network** communication.

The configuration of the DiceLoader C2 server is obfuscated with a **XOR** operation with a fixed key length of 31 bytes. Both obfuscated C2(s) and the key are stored at the beginning of the .data section.

![data section containing the obfuscated port, the C2 and the XOR key](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f867_6a92a313a49553afbaf311b7_6a2a7cb66d8eb6f373ee6037.webp)

Figure 5. .data section containing the obfuscated port, the C2 and the XOR key 

‍

The function used to un-XOR the configuration is straightforward, it iterates over the input buffer (_e.g. C2 IP address(es) and the C2 port_), the length of the XOR key is hardcoded in the function (line 12, with the modulo 0x1f).

![Function to un-xor DiceLoader C2s](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f87f_6a92a3122b0ef7af46bcd78a_6a2a7cb66d8eb6f373ee6034.webp)

Figure 6. Function to un-xor DiceLoader C2s 

‍

A script to deobfuscate DiceLoader configuration is available on this [gist](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/DiceLoader/scripts/extractor.py).

The second obfuscation function is also based on the XOR operator. 

![Decompiled code of the second obfuscation method. Source: Sekoia Threat detection & research](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f89a_6a92a318bd6424423eef1ecd_6a2a7cb66d8eb6f373ee6047.webp)

Figure 7. Decompiled code of the second obfuscation method. Source: Sekoia Threat detection & research

This method involves a more complex obfuscation function: each byte (Cx) is XORed with a byte of the key (Kx) (at the same index regarding the key length), and is XORed with the previous byte result of the deobfuscation (Px-1). The figure below schematizes the obfuscation algorithm:

  * “**K** ” in the schema stands for the XOR key which is the function parameter “ _key_ ” in figure 8;
  * “**C** ” in the schema stands for the ciphertext which is the function parameter “ _buff_ ” in figure 8;
  * “**P** ” in the schema stands for the plaintext: the result of the deobfuscation.



_NB: In the DiceLoader scenario the “IV” of this algorithm is one byte long and is Zero._

![Schema of the second obfuscation method by DiceLoader](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f885_6a92a31fdc307112383268ca_6a2a7cb66d8eb6f373ee605c.webp)

Figure 8. Schema of the second obfuscation method by DiceLoader

The data can be deobfuscated with the following Python function:

`def xor_blob(blob: bytes, key: bytes) -> bytearray:  
  
"""DiceLoader uses XOR obfuscation"""  
  
output = bytearray()  
  
temp = blob[0] ^ key[0]  
  
output.append(temp)  
  
for index, value in enumerate(blob):  
  
if index == 0:  
  
continue  
  
temp = blob[index - 1] ^ value ^ key[index % len(key)]  
  
output.append(temp)  
  
return output  
`

Code 2. Python function to deobfuscate TCP packet

This second obfuscation is consolidated as it is used twice:

  1. With a fixed key stored in the PE (the same as the one used for the configuration);
  2. With a key sent by the C2 at the runtime.



![Decompiled code that deobfuscates the received payload with the two different keys.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f894_6a92a3154b4041c6934282cc_6a2a7cb66d8eb6f373ee603d.webp)

Figure 9. Decompiled code that deobfuscates the received payload with the two different keys.

## Fingerprint

To profile the victim’s machine, the malware takes a fingerprint of the infected host to generate a unique identifier. First, it hashes the concatenation of the MAC address, the username and the computer name. This hash is concatenated with the current process identifier and it is then re-hashed. The malware uses the [FNV-1](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function) (Fowler–Noll–V 1) hashing algorithm:

![Fowler–Noll–V 1 implementation in DiceLoader](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f873_6a92a3104538ee1e1c2e5faf_6a2a7cb66d8eb6f373ee602e.webp)

Figure 10. Fowler–Noll–V 1 implementation in DiceLoader

Later, this fingerprint hash is sent at the earliest stage of the communication with the C2 server. To manipulate this information afterwards, the malware creates the following structure:

`struct fingerprint  
  
{  
  
_DWORD cmd_id;  
  
_BYTE random[15];  
  
int *fingerprint;  
  
_DWORD current_process_id;  
  
_DWORD magic;  
  
_BYTE flag_event;  
  
_BYTE flag_arg2;  
  
_DWORD flag_arg3;  
  
_DWORD size1;  
  
_BYTE undef_flags[3];  
  
_DWORD size_local_ipaddress;  
  
char local_ipaddress;  
  
};  
`

Code 3. C declaration of the fingerprint made by the loader and inserted in the linked list

## Networking

As introduced in the previous section “Obfuscation”, the loader uses a **raw TCP** connection to communicate with its Command and Control, where the port is configurable for each C2 of each sample. 

At the time of digging deep in the reverse of the sample, the C2s were down. For analysis purposes a [fake DiceLoader C2](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/DiceLoader/scripts/fake_c2_tcp_server.py) was developed. Therefore, the data sent from this server are considered to be incorrect.

### Initialisation sequence

To declare itself to the C2, DiceLoader uses a unique sequence of bytes. The screenshot below represents the dissection of the first TCP packet sent to the C2 server.

![Diagram of the initial TCP sequence](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f864_6a92a31a6017750314a4c0c9_6a2a7cb66d8eb6f373ee604d.webp)

Figure 11. Diagram of the initial TCP sequence

The legend for the figure above is as follows:

  1. The **2** first bytes are random numbers (never reused afterwards);
  2. The next 15 bytes are **randomly generated** number used for **XOR** obfuscation (of note, the size is also random from 5 to 15 bytes);
  3. The following **22** bytes are the **fingerprint obfuscated;**
  4. The ensuing **19** bytes are the **local IP address obfuscated** ;
  5. The last **4** bytes are the **FNV-1 hash** of the**local IP address** ;



So, the fingerprint and the local IP address are obfuscated using the second obfuscation method with the XOR key stored in the PE and the XOR key obtained from the generated random number (2).

![Extract of the decompiled code related to the double obfuscation of the fingerprint and local IP address](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f88b_6a92a3143e6167cebbf63d4c_6a2a7cb66d8eb6f373ee603a.webp)

Figure 12. Extract of the decompiled code related to the double obfuscation of the fingerprint and local IP address

### Received C2 order

After initialising the communication, the loader received data from its C2 with the specific bytes sequence, format and structure that is used each time the C2 sends data. The main thread is in charge of this task with the following code:

![Decompiled code used to manage order received from the C2, part-1.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f897_6a92a31da49553afbaf316d1_6a2a7cb66d8eb6f373ee6056.webp)

Figure 13. Decompiled code used to manage order received from the C2, part-1.

‍

![Decompiled code used to manage order received from the C2, part-2 \(function: received_data\)](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f870_6a92a316e9a71d42283ffaa0_6a2a7cb66d8eb6f373ee6040.webp)

Figure 14. Decompiled code used to manage order received from the C2, part-2 (function: received_data)

**Received order**| **Description**| **Length (byte)**| **Ref code**  
---|---|---|---  
(1)| Length of packet (2)| 1| Figure 13, line 80  
(2)| Custom XOR key| 5-15: (result of (1) % 0xb + 5)| Figure 13, line 83  
(3)| Length of packet (4)| 4| Figure 13, line 86  
(4)| Data (payload)| Value defined in the previous packet| Figure 14, line 22  
(5)| FNV-1 hash of packet (4)| 4| Figure 14, line 22  
  
Table 1: Packet sequence used to received data from the C2 

Each time the C2 sends a command/data/operation to the infected host, it follows this same packet sequence. 

When the sequence is received, DiceLoader executes the function used to manage the downloaded payload (_c.f._ stage number 4 of table 1), this function is in charge of allocating memory on the heap and of structurizing it regarding the malware linked lists’ structure.

![Decompiled function used to allocate memory and deobfuscate the received packet](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f879_6a92a317693fca262e1b64ca_6a2a7cb66d8eb6f373ee6043.webp)

Figure 15. Decompiled function used to allocate memory and deobfuscate the received packet

As shown in figure 15, the received data is doubly deobfuscated (see the second obfuscation technique described in its dedicated section). Firstly, it deobfuscates with the XOR key stored in the sample and secondly, it uses the key forwarded by the server at stage (2) of the sequence described in table 1 to retrieve the cleartext message.

Then, the function looks at the first byte of the deobfuscated payload to search for an order ID which value can be:

**Order identifier**| **Description**  
---|---  
1| Insert the payload in the linked list **L0**  
2| Set the mutex flag to 1, that stops the malware  
3| Push the structure containing the payload to the IoCompletionPort (for afterwards usage by the consumer threads)  
4| Increment the next queue direction by one  
  
Table 2. DiceLoader order ID description 

For a better understanding of this thread, a [Python server](https://github.com/SEKOIA-IO/Community/blob/main/IOCs/DiceLoader/scripts/fake_c2_tcp_server.py) was developed to mimic a DiceLoader C2. 

![Extract of the TCP communication between the sample and the fake C2 server](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f88e_6a92a3203e6167cebbf645f5_6a2a7cb66d8eb6f373ee605f.webp)

Figure 16. Extract of the TCP communication between the sample and the fake C2 server

## Execution

The loader specialises in the execution of malicious code, orchestrating the initiation of more sophisticated and harmful payloads to serve attackers objectives. DiceLoader does not use advanced techniques to execute payload sent by the C2. It works the same way as a shellcode execution: 

  1. Use VirtualAlloc to copy the shellcode to the reserved memory (_n.b: with the correct allocation type:_ MEM_RESERVE|MEM_COMMIT _and the permissions to_ PAGE_EXECUTE_READWRITE _the region pages_);
  2. Copy shellcode in the allocated memory;
  3. Deobfuscate the shellcode (_c.f. section Obfuscation_);
  4. Inline function pointer declaration and execution.



![Disassembled code of the workflow used to execute a shellcode](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f888_6a92a31be9a71d42283ffcfd_6a2a7cb66d8eb6f373ee6050.webp)

Figure 17. Disassembled code of the workflow used to execute a shellcode

The technique is simple, however, the buffer that contains the code to execute is more complex than it seems at first glance. First to reach this part of the code, the loader must receive the order “3” (_c.f._ the section “Received C2 order” above) to trigger the windows API call to PostQueuedCompletionStatus in the IoCompletionPort that wakes up one consumer thread.

Then, the consumer thread manipulates the passed structure to search for another action identifier:

**Action ID**| **Observation**| **Confidence**  
---|---|---  
1| Search in **L3** for already allocated memory and execute the data provided previously| 60%: Few information on the structure of the memory required to execute the payload  
2| Allocate memory on the Heap and execute the data provided previously (c.f: figure 18)| 100%  
8| Search element in **L1** to execute a function pointer| 30%: Few information on the structure of element in **L1**  
Other| Insert element in **L2**|  100%  
  
Table 3. Interpretation of the action for its given action ID 

_Disclaimer: At this point in the analysis none of the 3 cases where an execution could be triggered were reached due to the lack of knowledge on the required memory structure, and also due to the C2 inactivity._

![Last part of the shellcode structure preparation](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f882_6a92a31ccd1cab63350ca953_6a2a7cb66d8eb6f373ee6053.webp)

Figure 18. Last part of the shellcode structure preparation

Execution of the additional payload is indirect, the attacker does not provide a DLL or a PE, the malware expects to have a proper memory structure. This shellcode executor has 4 parameters:

  1. A pointer to the current element in **L1** linked list;
  2. A pointer to a function used to create a structure insertable in **L2** ;
  3. Another pointer to a function that creates a structure insertable in **L2** that has more choices in the parameters;
  4. A function pointer to search an item in **L1**.



![Build of the parameters pushed to the shellcode function](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f86a_6a92a3196568d7e2b408d93c_6a2a7cb66d8eb6f373ee604a.webp)

Figure 19. Build of the parameters pushed to the shellcode function 

As indicated previously, triggering the execution of a payload in DiceLoader is not an easy task due to the different internal data structures and mechanisms.

## DiceLoader C2 infrastructure

Since early 2022, Sekoia.io analysts have proactively tracked a C2 infrastructure that we assess, with high confidence, is associated with the DiceLoader malware. The infrastructure has been consistently maintained, with an average of over 20 active servers, and approximately 50 active servers as of January 2023.

It is noteworthy that we identified PowerShell scripts, obfuscated in a manner consistent with known FIN7 techniques, that load Carbanak and DiceLoader. The C2 servers of this infrastructure are linked to these malicious payloads. We therefore assess with high confidence that the DiceLoader payloads, as well as the associated C2 servers, are used by the FIN7 intrusion set. 

Here are the results of our proactive tracking from the beginning of 2022 until January 2024 (at the time of writing):

![Number of active DiceLoader C2 servers by date](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e7a54c8f443fa4f891_6a92a321e9a71d4228400011_6a2a7cb76d8eb6f373ee608e.webp)

Figure 20. Number of active DiceLoader C2 servers by date 

‍

The number of presumed active DiceLoader C2 servers has significantly increased since December 2023, as shown in the above figure.

Two main hypotheses explaining this increase can be considered. Firstly, it is highly likely that **an intrusion set** , leveraging DiceLoader to load additional payloads in its campaigns, **has escalated its malicious activities**. This could be associated with FIN7 or another intrusion set that also employs DiceLoader malware. Secondly, it is plausible that **one or several new intrusion sets recently added DiceLoader to their arsenal**. At the time of writing, Sekoia.io has no evidence to affirm or refute these hypotheses. We are interested in obtaining more technical or strategic information about DiceLoader and intrusion sets leveraging the malware, including FIN7.

## Final words

While analysing DiceLoader malware is a task that can prove challenging as the different developed **mechanisms** show an advanced knowledge and technical expertise in **softwaredevelopment** , surprisingly the analysed sample does **not** have any technique for **anti-analysis** , nor any particular protection against execution in a dedicated environment (e.g.: virtual environments, sandboxes, etc.). The tracking of the infrastructure related to DiceLoader shows its consistent activity over the time. Sekoia TDR (Threat Detection & Research) assesses with high confidence that the malware is still used by intrusion sets as of January 2024, due to the ongoing development in the malware and the constant number of infrastructure spotted online.

## Annexes

### YARA

We have **removed** the YARA rule for matching too widely, stay tuned for its updated version.

### MITRE ATT&CK TTPs

**Tactic**| **Technique**  
---|---  
Defense Evasion| T1027 – Obfuscated Files or Information  
Defense Evasion| T1027.007 – Obfuscated Files or Information: Dynamic API Resolution  
Defense Evasion| T1140 – Deobfuscate/Decode Files or Information  
Defense Evasion| T1620 – Reflective Code Loading  
Command and Control| T1105 – Ingress Tool Transfer  
Command and Control| T1132.002 – Non-Standard Encoding  
Command and Control| T1571 – Non-Standard Port  
Discovery| T1057 – Process Discovery  
Discovery| T1082 – System Information Discovery