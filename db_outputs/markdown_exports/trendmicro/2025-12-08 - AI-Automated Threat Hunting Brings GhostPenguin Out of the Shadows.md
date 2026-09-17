# AI-Automated Threat Hunting Brings GhostPenguin Out of the Shadows

- **Source :** trendmicro
- **URL :** https://www.trendmicro.com/en/research/25/l/ghostpenguin.html
- **Date :** 2025-12-08

---

Cyber Threats

# AI-Automated Threat Hunting Brings GhostPenguin Out of the Shadows

In this blog entry, Trend™ Research provides a comprehensive breakdown of GhostPenguin, a previously undocumented Linux backdoor with low detection rates that was discovered through AI-powered threat hunting and in-depth malware analysis.

By: Aliakbar Zahravi 2025/12/08 Read time:  ( words) 

[ ![Share](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/share-more.svg) ](https://www.addtoany.com/share) ![Print](https://www.trendmicro.com/etc.clientlibs/trendresearch/clientlibs/clientlib-trendresearch/resources/img/printer.svg)

Save to Folio

__

* * *

## Key takeaways

  * GhostPenguin is a multi-threaded Linux backdoor written in C++ that provides remote shell access and comprehensive file system operations over an RC5-encrypted UDP channel. It establishes communication through a structured session handshake mechanism and synchronizes multiple threads to handle registration, heartbeat signaling, and reliable command delivery.
  * GhostPenguin was discovered using Trend™ Research’s AI-driven, automated threat hunting pipeline that collected and analyzed zero-detection Linux samples from VirusTotal. The investigation involved building a structured database of extracted artifacts, using AI to automate profiling, and employing VirusTotal hunting queries to surface zero-detection samples for deeper analysis.
  * This approach allowed artifacts to be extracted from thousands of malware samples, generated structured profiles, and used custom YARA rules and VirusTotal queries to surface undetected threats like GhostPenguin.
  * Our analysis showed GhostPenguin is still in development, with debug artifacts and unused functions, highlighting the importance of advanced AI and automation in uncovering sophisticated, evasive threats.
  * Trend Vision One™ detects and blocks the specific indicators of compromise (IoCs) mentioned in this blog entry, and offers customers access to hunting queries, threat insights, and intelligence reports related to the GhostPenguin backdoor.



Hunting high-impact, advanced malware is a difficult task. It becomes even harder and more time-consuming when defenders focus on low-detection or zero-detection samples. Every day, a huge number of files are sent to platforms like VirusTotal, and the relevant ones often get lost in all that noise. Identifying malware with low or no detections is a particularly challenging process, especially when the malware is new, undocumented, and built largely from scratch. When threat actors avoid publicly available libraries, known GitHub code, or code borrowed from other malware families, they create previously unseen samples that can evade detection and make hunting them significantly harder.

In these cases, the threat actors carefully craft both the code and the network communication to minimize noise and keep the malware as inconspicuous as possible. They often use multi-stage architectures and secure communication channels that do not reveal subsequent stages unless the communication sequence unfolds exactly as expected. As a result, only a very small amount of data is transferred between the infected host and the command-and-control (C&C) server, further complicating detection and analysis.

Previously, Trend™ Research reported on the effects of [offensive GitHub projects and open-source red-teaming tools](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/from-defense-to-offense-the-misuse-of-red-teaming-tools-by-cybercriminals) on modern malware development ecosystem, and how defenders can use this as a chance to improve detection patterns and their overall approach for threat hunting. Our analysis also showed how [artificial intelligence (AI)](https://www.trendmicro.com/en_us/what-is/ai.html) and automation can speed up and improve the accuracy of detection when a new malware family is created and shares code from those open-source repositories.

In this blog entry, we demonstrate how AI can be utilized to find low-detection samples from VirusTotal and how this was used to analyze the GhostPenguin Linux backdoor.

## Threat hunting approach

Our approach focused on collecting, processing, and analyzing a large number of malware samples from known and reported attacks. The goal was to extract useful artifacts that help hunt for new, undetected threats.

**Hunting workflow**

**1\. Collect and extract artifacts**  
We gather many malware samples from known and reported attacks and extract key information from them such as strings, API calls, behaviors, function names, variable names, and constants. All collected data is stored in a structured database. Afterwards, we tag and categorize the samples so they are easier to search and compare.

**2\. Build VirusTotal hunting queries**  
Using the extracted artifacts, we create VirusTotal hunting rules and run them against samples with zero detections. When we find potential candidates, pass the samples to the profiling stage.

**3\. Profiling and analysis**  
Binary files are sent to IDA Pro (Hex-Rays) for decompilation and further artifact extraction. CAPA also utilized to identify specific capabilities (A custom rule has been generated based on the artifacts collected during Stage 1). Non-binary files like scripts or code are passed directly to the profiler for feature extraction. The profiler subsequently generates a unified profile in JSON format for each file, which is then forwarded to the next stage of analysis.

The AI agent Quick Inspect reviews the JSON profile created during the profiling stage. It analyzes the artifact, scores it, and determines if the file is malicious or not. Files below the threshold go into a monitoring list for later review, while files above the threshold tagged as malicious and move to the next stage.

The Deep Inspector agent performs a deeper analysis on files that pass the threshold and are tagged as malicious. It generates a detailed analysis report for the file based on the decompiled code and the metadata created during the profiling stage. The agent reviews the file profile and produces a code-analysis report that includes:

  * A short summary
  * Identified capabilities
  * Code execution flow
  * Technical analysis
  * MITRE ATT&CK framework mapping



We used this pipeline to hunt for a VirusTotal zero-detection sample that we named GhostPenguin. The sample was submitted on July 7, 2025, and remained undetected in VirusTotal for more than four months.

If a file is packed or obfuscated, the YARA scanner and AI model usually detect this and tags it. If you have automated scripts for unpacking, you can set up an MCP server that can route these files to your unpacking pipeline for dynamic, static, or manual unpacking. Simple obfuscation and unpacking process can often be handled directly by AI (by a AI resolver or AI generating script for deobfuscation/unpacking), but heavy or complex obfuscation should be processed by external automation, custom scripts or manual efforts.__

**Phase 1**

In this phase, in which we first need to gather as much intelligence as possible before we can hunt new and unknown threats, we built a structured database and populated it with detailed information about each sample. The database stores file metadata, category, tags, capabilities, MITRE techniques, strings, and [Malware Behavior Catalog](https://github.com/MBCProject) (MBC) behaviors of collected malware samples. This database is extremely valuable, as it can be used for AI model fine-tuning, context-based AI search, RAG workflows, building a knowledge base, malware similarity matching, APT attribution, and more.

We began by defining the main categories for our hunting workflow, using Google [Magika](https://github.com/google/magika) to help classify files automatically:

**Platform categories**

  * Windows
  * Linux
  * MacOS



**File types**

  * Binary
  * Script  
  




Binary files are passed to IDA Pro for fingerprinting and to generate the decompiled code. The decompiled output is then sent to the AI model for processing. At this stage, the AI performs function renaming, adds function and code comments, generates summaries, identifies capabilities, assigns tags, analyzes network communication patterns, and more.

Alongside the AI analysis, we also ran [CAPA](https://github.com/mandiant/capa), [FLOSS](https://github.com/mandiant/flare-floss), and [YARA](https://github.com/VirusTotal/yara-x) on the same samples. All results were stored in a structured JSON format and sent to the JSON parser. The parser extracted the relevant fields and mapped them into the database. We also stored the raw JSON files separately so they can be used later for research or processed by other tools.

This threat intelligence collection system is illustrated in Figure 1, though it’s important to note that this chart is highly simplified, and many modules and components have been removed for clarity and readability.

[ ![Figure 1. Threat intelligence collection system](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig01.png) ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig01.png)

Figure 1. Threat intelligence collection system

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig01.png)

**Phase 2**

For this research, our primary goal was to hunt for potential zero-detection Linux backdoors. To achieve this, we filtered out all Linux binaries and began identifying the most common API calls, strings, and behaviors. These findings guided our VirusTotal hunting queries and allowed us to build more accurate searches for unknown or undetected malware. These queries could be used as YARA rules for VirusTotal RetroHunt or Live Hunt, or they can be run as manual VirusTotal search queries (Figure 2). GhostPenguin was among the search results, as shown in Figure 3.

![Figure 2. Examples of VirusTotal RetroHunt YARA rules](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig02.png)

Figure 2. Examples of VirusTotal RetroHunt YARA rules

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig02.png)

![Figure 3. GhostPenguin VirusTotal detection](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig03.png)

Figure 3. GhostPenguin VirusTotal detection

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig03.png)

**Phase 3**

After collecting the potential candidates, the next step was to process and rank them. Since we focused on ELF binaries in this research, we passed these files directly into the decompilation pipeline. In the third phase, the automated script sent each file to IDA Pro to generate the decompiled output. Once the decompilation was complete, the script forwarded the result to the AI model for analysis. For this task, we used gemini-3-pro to process the code (Figure 4).

![Figure 4. AI scanner](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig04-2.png)

Figure 4. AI scanner

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig04-2.png)

Once the high-confidence malicious files were identified, they were passed to the next Deep Inspector. This stage generated a more comprehensive report that included detailed behavior, capabilities, and technical insights (Figure 5).

![Figure 5. AI-generated malware report](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig05.png)

Figure 5. AI-generated malware report

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig05.png)

## GhostPenguin analysis

**Name** | systemd  
---|---  
**MD5** | 7d3bd0d04d3625322459dd9f11cc2ea3  
**SHA1** | 145da15a33b54e0602e0bbe810ef6c25f2701d50  
**SHA256** | 7b75ce1d60d3c38d7eb63627e4d3a8c7e6a0f8f65c70d0b0cc4756aab98e9ab7  
**Magic** | ELF 64-bit LSB executable, x86-64  
**File size** | 91.32 KB (93515 bytes)  
Table 1. GhostPenguin backdoor

GhostPenguin is a multi-thread backdoor written in C++ that targets the Linux platform. The malware collects system information including IP address, gateway, OS version, hostname, and username, and sends it to a C&C server during a registration phase. It then receives and executes commands from the C&C server. Supported commands allow the malware to provide a remote shell via “/bin/sh”, and perform various file and directory operations including creating, deleting, renaming, reading, and writing files, modifying file timestamps, and searching for files by extension. All C&C communication occurs over UDP port 53. The malware first requests a 16-byte session ID from the server, which is subsequently used as the key for an RC5 encryption algorithm to encrypt all traffic. The malware sends periodic heartbeats to maintain its connection. To prevent multiple instances from running, it creates a file named “.temp” in the user's home directory containing its process ID.

GhostPenguin’s internal architecture

[ ![Figure 6. Malware’s internal architecture](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig06-2.png) ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig06-2.png)

Figure 6. Malware’s internal architecture

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig06-2.png)

### Technical analysis

Upon execution, the malware first resolves its execution context by obtaining both the current user’s home directory and the full path of the running process. It uses _getpwuid()_ to retrieve the user’s home directory and _readlink("/proc/self/exe")_ to capture its own executable path. With this information, it constructs the path for its temporary PID file inside the user’s home directory (for example, _< home>/.temp_). Once the PID file location is prepared, the malware checks whether another running instance already exists. It does this by loading a PID value from its designated temporary lock file and verifying that the file contains at least four bytes enough to represent a valid 32-bit PID. After extracting the PID, it invokes _kill(pid, 0)_ to test whether that process is currently active (Figure 7). If the call confirms the PID corresponds to a live process, the malware concludes that an active instance is already running and aborts initialization; otherwise, the stale entry is ignored and execution proceeds.

![Figure 7. Initial setup](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig07.png)

Figure 7. Initial setup

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig07.png)

The malware then enters its main operational loop, which continues until a global exit flag _g_bIsClientExit_ is set. Inside this loop, it iterates through a list of C&C server addresses defined in a global configuration structure _g_lpLinuxClientHostCfg_. For each server, it attempts to establish a full communication session. The malware’s C&C configuration structure is shown below in Figure 8.

![Figure 8. GhostPenguin C&C configuration](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig08.png)

Figure 8. GhostPenguin C&C configuration

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig08.png)

Notably, a leftover debug configuration, _g_szConfigDebug_ , was identified in the binary. This global variable contains a separate, unused domain and IP address, which appears to be an artifact from the developer's testing (Figure 9).

![Figure 9. Debug configuration](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig09.png)

Figure 9. Debug configuration

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig09.png)

This artifact strongly suggests the malware is still in active development. This theory is further supported by the discovery of two fully implemented persistence functions (_ImpPresistence_ and _ImpUnPresistence_), but they are never used by the malware.

The malware contains several spelling errors:

  * ImpPresistence \- Misspelling of "Persistence"
  * Userame \- Misspelling of "Username" in the string "Userame:%s"
  * IsPorecessExistByPID \- Misspelling of "Process"



The code snippet in Figure 10 demonstrates the malware's main operation loop. The code iterates through a configured list of C&C servers, launching separate threads for asynchronous communication (heartbeating, data receiving, and sending) once a connection is established. This main thread then enters an idle state, waiting for a disconnect or an exit command.

![Figure 10. GhostPenguin main thread](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig10.png)

Figure 10. GhostPenguin main thread

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig10.png)

**Malware network communication**

![Figure 11. Network communication workflow](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig11.png)

Figure 11. Network communication workflow

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig11.png)

The first step in C&C communication is to acquire a session ID (Figure 12). The malware calls _GetSessionUDFromServer_ , which spawns a worker thread (_ThreadProcGetSessionIDFromServer_) and waits for five seconds at most for it to complete (Figure 13). The worker thread constructs and sends a 34-byte UDP packet with command 0x04 to the C&C server. This initial request packet is **not** encrypted and contains the placeholder session ID “FFFFFFFFFFFFFFFF”. To demonstrate the malware's capabilities and inspect the network traffic, we set up a C&C server in a lab environment and redirected the infected VM's traffic to our designated server where the C&C server is hosted.

![Figure 12. Initial traffic - Malware request for the session key from the server](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig12.png)

Figure 12. Initial traffic - Malware request for the session key from the server

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig12.png)

The malware network packet has the following structure:

> struct C2Packet {  
>  unsigned short totalLength; // Total packet size  
>  unsigned char sessionID[16]; // RC5 encryption key  
>  unsigned char commandType; // Command type  
>  unsigned char subCommand; // Direction and Acknowledgment packet flag  
>  unsigned short taskID; // Task identifier  
>  unsigned int taskInstanceID; // Instance ID  
>  unsigned int taskSequenceNum; // Sequence number  
>  unsigned char paddingLen; // Padding count  
>  unsigned char payload[]; // payload + padding  
>  };

![Figure 13. Malware generating initial handshake packet to retrieve the session ID from C&C server](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig13.png)

Figure 13. Malware generating initial handshake packet to retrieve the session ID from C&C server

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig13.png)

The malware then waits for a 34-byte response (Figure 14). If a valid response with command 0x04 is received, it extracts the new 16-byte session ID from the packet and stores it in the global variable _g_szSessionID_. This session ID serves as the RC5 encryption key for all subsequent communications.

![Figure 14. Server response with session ID](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig14.png)

Figure 14. Server response with session ID

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig14.png)

If a session ID is successfully obtained, the malware starts the main data receiver thread, _ThreadProcDataReceiver_. This thread enters an infinite loop, waiting to receive UDP packets from the C&C server. Upon receiving a packet, it performs several validation checks: the received size must match the packet's internal length field, the session ID must match the one obtained earlier, and the encrypted payload length must be a multiple of eight.

If the packet is valid, its payload (from offset 18 onwards) is decrypted in-place using a custom RC5 implementation (_CMyRC5::EncDecRC5_). The 16-byte session ID serves as the RC5 key. The decrypted packet is then passed to _OnReceivedPacket_ for processing. The RC5 encryption algorithm works in eight-byte blocks, which is why the encrypted portion of the packet (a total length of 18) must be a multiple of eight (Figure 15). 

![Figure 15. GhostPenguin packet receiver](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig15.png)

Figure 15. GhostPenguin packet receiver

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig15.png)

After starting the receiver, the malware attempts to register itself with the C&C server by calling _RegisterSelfToServer_. This function spawns another worker thread, _ThreadProcRegisterSelfToServer_ , and waits up to 10 seconds for it to complete. The registration thread gathers system information by creating an instance of the _CBasicInfoGather_ class. This information includes:

  * LAN IP address
  * Default gateway (obtained via Netlink sockets)
  * OS distribution Information (from /etc/redhat-release or /etc/os-release)
  * Host name
  * Current username (via whoami command)
  * OS architecture ("X64" or "X86")
  * Process ID (PID)
  * Process bitness (hardcoded to 64-bit)
  * Client architecture ID (32 for Linux x86, 33 for Linux x64)



This collected data is serialized into a buffer. The thread then enters a loop, sending this data to the C&C server inside a "New Task" packet. It sends Task ID 1 (_Set Status Initializing_) while the client status is **initializing** , and Task ID 3 (Set Status Active) when the status is **registering** (Figure 16). These registration packets are sent every second until the C&C server responds with a command that changes the client's status to **active**.

![Figure 16. Infected system registration packet](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig16.png)

Figure 16. Infected system registration packet

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig16.png)

Once the malware receives the Session ID, it utilizes it as a key to encrypt and decrypt all packet content starting from offset 0x12 (18). To complete the initialization, the C&C server sends a _'Set Status Active'_ packet, transitioning the implant into its fully operational state for command execution (Figure 17).

![Figure 17. Server sends Set Status Active packet](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig17.png)

Figure 17. Server sends Set Status Active packet

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig17.png)

Since UDP is a "connectionless" protocol (fire-and-forget), it does not guarantee that data arrives. The malware implements its own reliability layer to ensure commands and results are not lost. To achieve this, it saves a copy of every outgoing packet such as command output or file data into a global linked list named _g_ListPacketToSend_. A dedicated background thread continuously loops through this list and re-sends the packets until the C&C server confirms they were received. This confirmation arrives as a specific "Acknowledgment" (ACK) packet (Command Type 3). When the malware receives an ACK, the _AckPacket_ function verifies the IDs (Task, Instance, and Sequence) and deletes the packet from the waiting queue. This system guarantees that the C&C server receives all data, even if the network drops packets.

Once registration is successful, two more threads are started: _ThreadProcHeartBeat_ and _ThreadProcDataSender_ (Figure 18). The _ThreadProcHeartBeat_ thread periodically sends a 34-byte encrypted heartbeat packet (command 0x00) to the C&C server to signal that it is still online. The interval is configurable, with a default of 500 milliseconds.

![Figure 18. GhostPenguin heartbeat](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig18.png)

Figure 18. GhostPenguin heartbeat

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig18.png)

The _ThreadProcDataSender_ thread processes a global queue of outgoing packets (_g_ListPacketToSend_). It retrieves packets, encrypts their payload using the session ID as the key, and sends them to the C&C server. This queue has a built-in retry mechanism; packets are re-queued for transmission until they exceed a defined retry limit. The thread also cleans up stale packets from expired sessions.

![Figure 19. Heartbeat packet](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig19.png)

Figure 19. Heartbeat packet

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig19.png)

With all threads running, the main thread enters a waiting state, sleeping for one-second intervals as long as the client status remains **active**.

**Command handling**

The _OnReceivedPacket_ function is the central dispatcher. It first sends an acknowledgment (ACK) packet (command 0x03) back to the C&C server for any incoming task that requires it. It then dispatches the packet based on its command type. New tasks (command type 1) are handled by _OnReceivedPacketNewTask_ , which uses a large switch statement on the task ID to call the appropriate function.

The malware supports a wide range of commands, which can be categorized as shown in Table 2:

**Task ID** | **Command Name** | **Category** | **Description**  
---|---|---|---  
1 | Set Status Initializing | Status | Resets client to "Status 0". Forces the client to (re)send its OS info and registration packet.  
2 | Set Status Connecting | Status | Sets client to "Status 1". Client is connecting to C&C server  
3 | Set Status Active | Status | Sets client to "Status 2". Confirms the connection is successful. Client begins heartbeating and accepting tasks.  
9 | Client Offline | Control | Uninstall and xit  
15 | RShell Start | Remote Shell | Start remote shell session (fork /bin/sh)  
16 | RShell Send Data | Remote Shell | Send command to remote shell stdin  
17 | RShell Stop | Remote Shell | Stop remote shell and cleanup  
18 | RShell Data Result | Remote Shell | Client sends shell output back to C&C server  
19 | Get Drives | File System | List drives/root directory  
20 | List Directory | File System | List directory contents with metadata  
21 | Write File Data | File System | Write data to existing file at offset  
22 | Create File | File System | Create empty file with specified size  
23 | Create File Success | File System | ACK: File creation succeeded  
24 | Create File Failed | File System | ACK: File creation failed  
25 | Read File Data | File System | Read file data from offset  
26,27 | Delete File | File System | Delete a file  
28 | Rename File | File System | Rename file  
29,30,31 | Modify File Time | File System | Modify file timestamp attributes  
32 | Get File Size | File System | Get file size in bytes  
33 | Search Files by Extension | File System | Search for files with specific extension  
34 | Create Directory | Directory Ops | Create a new directory  
35 | Delete Directory | Directory Ops | Delete Directory (Recursive)  
36 | Modify Directory Time (Create) | Directory Ops | Modify directory creation time  
37 | Modify Directory Time (Modify) | Directory Ops | Modify directory modification time  
38 | Get Directory Data | Directory Ops | Get detailed directory tree data  
39 | Get Directory File Size | Directory Ops | Get size of file in directory  
40 | Get Directory File Data | Directory Ops | Get file data from directory  
Table 2. The malware’s commands

File and directory operations are comprehensive, allowing for full filesystem manipulation, including listing, reading, writing, creating, deleting, renaming, and searching for files, as well as creating and deleting directories. Large data transfers, such as directory listings and file reads, are fragmented into multiple packets to fit within the UDP payload limits.

The following code snippets demonstrates the command execution for “List Directory” command (Figure 20) and the malware’s response (Figure 21):

![Figure 20. Server issues a “List Directory” command](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig20.png)

Figure 20. Server issues a “List Directory” command

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig20.png)

![Figure 21. Malware response to “List Directory” command](https://www.trendmicro.com/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig21.png)

Figure 21. Malware response to “List Directory” command

[ download ](/content/dam/trendmicro/global/en/research/25/l/ghostpenguin/GhostPenguin_Fig21.png)

If the malware receives the _CLIENT_OFFLINE_ command (Task 9), it sends a confirmation response to the C&C three times, sets the _g_bIsClientExit_ flag to 1, and changes its status to _CLIENT_STATUS_OFFLINE_. This signals the main loop to break, leading to a full teardown. During this teardown, all threads are canceled, resources are uninitialized, and a call to _SelfDel()_ is made to try to delete the malware's executable from the disk. Finally, the PID file is removed before the process terminates.

## Conclusion

Hunting low-detection malware like GhostPenguin demands an adaptive approach, as traditional detection methods may not measure up against novel threats. By integrating AI-driven automation, structured intelligence databases, and advanced profiling techniques, defenders can systematically sift through vast volumes of data to identify and analyze even the most inconspicuous malware. Through our investigation into this backdoor, we demonstrate how multi-stage workflows combining automated artifact extraction, in-depth decompilation, and layered AI analysis can reveal the architecture and communication methods of threats that would otherwise remain hidden. This case study exemplifies the increasing complexity of modern malware and the critical need for security researchers to continuously evolve their threat hunting strategies, combining human expertise with new technologies to outpace more complex adversaries. As attackers continue to refine their methods, proactive and intelligence-led defenses can ensure organizations stay resilient against threats like GhostPenguin.

## Proactive security with Trend Vision One™

[Trend Vision One™](https://www.trendmicro.com/en_us/business/products/security-operations.html) is the only AI-powered enterprise cybersecurity platform that centralizes cyber risk exposure management and security operations, delivering robust layered protection across on-premises, hybrid, and multi-cloud environments.

## Trend Vision One™ Network Security

  * 46704: UDP: Backdoor.Linux.GhostPenguin.A Runtime Detection



## Trend Micro™ Threat Intelligence

To stay ahead of evolving threats, Trend customers can access [Trend Vision One™ Threat Insights](https://www.trendmicro.com/en_us/business/products/threat-intelligence.html) which provides the latest insights from Trend ™ Research on emerging threats and threat actors. 

**Trend Vision One Threat Insights**

  * Emerging Threats: ****[Hunting the Invisible: How utilize AI to Unmasked a "Zero-Detection" Linux Backdoor GhostPenguin](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Hunting%20the%20Invisible%3A%20How%20utilize%20AI%20to%20Unmasked%20a%20%22Zero-Detection%22%20Linux%20Backdoor%20GhostPenguin)



**Trend Vision One Intelligence Reports (IOC Sweeping)**

  * [Hunting the Invisible: How utilize AI to Unmasked a "Zero-Detection" Linux Backdoor GhostPenguin](https://portal.xdr.trendmicro.com/index.html#/app/ti/intelligence_insights?name=Hunting%20the%20Invisible%3A%20How%20utilize%20AI%20to%20Unmasked%20a%20%22Zero-Detection%22%20Linux%20Backdoor%20GhostPenguin)



## Hunting Queries 

**Trend Vision One Search App**

Trend Vision One customers can use the Search App to match or hunt the malicious indicators mentioned in this blog post with data in their environment.__

**_Linux Hunting query for GhostPenguin C2._**

eventSubId:204 AND ((dst:"65.20.72.101" AND dpt:53) OR (dst:"124.221.109.147"))

## Indicators of Compromise (IOCs)

**Primary modules**

**SHA-256** | **Description** | **Detection**  
---|---|---  
7b75ce1d60d3c38d7eb63627e4d3a8c7e6a0f8f65c70d0b0cc4756aab98e9ab7 | systemd  | Backdoor.Linux.GHOSTPENGUIN.A  
  
**C &C servers**

  * 65[.]20[.]72[.]101:53
  * www[.]iytest[.]com:5679
  * 124[.]221[.]109[.]147:5679



Tags

[Latest News](/en/research.html?category=trend-micro-research:article-type/latest-news) | [Articles, News, Reports](/en/research.html?category=trend-micro-research:medium/article) | [Research](/en/research.html?category=trend-micro-research:article-type/research)

###  Authors 

  * Aliakbar Zahravi

Staff Researcher




[ Contact Us ](mailto:tm_research@trendmicro.com)

### Related Articles

  * [ Unveiling Earth Kapre aka RedCurl’s Cyberespionage Tactics With Trend Micro MDR, Threat Intelligence ](/en/research/24/c/unveiling-earth-kapre-aka-redcurls-cyberespionage-tactics-with-t.html)
  * [ A Secure Access Service Edge (SASE) Guide for Leaders ](/en/research/22/h/secure-access-service-edge-sase-security-company.html)
  * [ Why the Open Secure AI Alliance Matters: Open Frontier Models, Open Deployment Flexibility ](/en/research/26/g/open-secure-ai-alliance.html)



[ See all articles ](/en/research.html)

[ ](/en/research.html)