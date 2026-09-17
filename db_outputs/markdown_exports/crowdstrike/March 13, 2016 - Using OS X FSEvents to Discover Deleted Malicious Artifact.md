# Using OS X FSEvents to Discover Deleted Malicious Artifact

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/using-os-x-fsevents-discover-deleted-malicious-artifact/
- **Date :** March 13, 2016

---

# Using OS X FSEvents to Discover Deleted Malicious Artifacts

March 13, 2016

• [ William Tan](/en-us/blog/author.william-tan/ "Posts by William Tan") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


File System Events (FSEvents) in OS X 10.7+ introduced the capability to monitor changes to a directory. FSevents are logged by the file system events daemon (fseventsd) process; the daemon writes these events to a log file located in the root of each volume in a folder named “.fseventsd”, which acts as a staging or buffer area.

An application accesses these logs using the FSEvents API to immediately ‘see’ when an event modified a directory, including file creation, file modification, files deletion, etc. Malware often attempts to remove traces of itself after execution and when it does, the File System Events (FSEvents) artifact can help us discover the existence of deleted files. Using this artifact we can obtain evidence of a file even after the malware has removed itself and traces of its execution. By parsing FSEvents logs we can easily obtain a full path, creation, and deletion dates for deleted files, long after a system was compromised. While we can see historical changes, it is important to note that file system events do not live indefinitely in the “.fseventsd” folder as it merely acts as a staging area for OS X to keep track of file system changes. The lifespan of events are dictated by a 64-bit incrementing counter. CrowdStrike has observed four month old events on a typical system. This post will provide an overview of FSEvents as a forensic artifact. When a FSEventStream is created, some flags are created by default but additional flags can be passed to indicate the type of action. A selection of possible flags that can be set when creating a FSEventStream can be seen in the table below: 

**FSEvent Stream EventFlag**| **Description**  
---|---  
None| Default Flag. A change occurred in this directory but no event flag was set with this change.  
MustScanSubDirs| Informs the application needs to rescan the affected directory and subdirectories under it.  
UserDropped| Error occurred during setting flag, application should perform full scan of directory for changes.  
KernelDropped| Error occurred during setting flag, application should perform full scan of directory for changes.  
EventIdsWrapped| 64-bit event ID counter wrapped around, previously-issued event ID's are no longer valid  
HistoryDone| Marker Flag to indicate when previous set flags should be ignored.  
RootChanged| Flag set when change occurred in a directory along the path of a watched directory.  
Mount| A volume was mounted under one that was being watched.  
Unmount| A volume was unmounted under one that was being watched.  
ItemCreated| Flag set when a file or directory is created  
ItemRemoved| Flag set when file or directory is deleted  
ItemInodeMetaMod| Flag set when inode metadata has been modified  
ItemRenamed| Flag set when file or directory is renamed  
ItemModified| Flag set when file or directory is modified  
ItemFinderInfoMod| File's finder metadata was modified  
ItemChangeOwner| Owner of file or directory has been changed.  
ItemXattrMod| Extended attributes of file or directory modified  
ItemIsFile| Item is a file  
ItemIsDir| Item is a directory  
ItemIsSymlink| Item is a symbolic link  
  
## How to Parse FSEvents

FSEvents are logged in folder named .fseventsd at the top level of every volume. This folder is only root accessible and contains multiple gzipped files. As an example, /Volumes/Macintosh HD/.fseventsd contains the FSEvents for my local hard drive. These files are difficult to work with directly, as events are represented as a hex value. David Cowen released an excellent python based tool called FSEventsParser which can carve out FSEvent records from the gzipped files in the .fseventsd directory of a volume. [![dir](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/dir.png)](/content/dam/crowdstrike/www/en-us/wp/2016/03/dir.png) The parser outputs in both text and SQLite formats, but due to the file structure I find working with the SQLite file to be easier when performing queries. Each record of output can contain these header values: 

> record_filename|record_mask|record_mask_hex|asl_name_date_stripped|record_ wd|record_number_parse_order|record_length|max_wd_record_number|record_end _relative_offset|current_page_size|source_fsevents_filesize|source_fsevents_file| source_fsevents_path|file_header-unknown_hex|file_header-unknown_int

The reference for these values can be found on FSEventsParser’s Github page. The records are stored in the “fsevents” table, and below is an example of a query for all events with the record_mask of “ItemRemoved”. 

> Williams-MBP:FSEventsParser williamtan$ sqlite3 fsevents.sqlite SQLite version 3.8.10.2 2015-05-20 18:17:19 Enter ".help" for usage hints. sqlite> .databases seq name file \--- --------------- ---------------------------------------------------------- 0 main /Users/williamtan/Desktop/FSEventsParser/fsevents.sqlite sqlite> SELECT * FROM fsevents WHERE record_mask LIKE "ItemRemoved;"; private/var/run/vncserver.agent.0.sock|ItemRemoved;|0x02000000|2015.12.21| 26118|4983|51|38400|575191|51929|576173|0000000000009600|/Volumes/Macintosh HD/.fseventsd|0x820193a3|2744320386 private/var/run/vncserver.agent.501.sock|ItemRemoved;|0x02000000|UNKNOWN| 163723|4997|53|167716|533063|8976|533227|0000000000028f24|/Volumes/Macintosh HD/.fseventsd|0x29572659|1495684905 private/var/folders/nh/p6dq7q1d7_sg5rzsqlc64z0r0000gn/T/vmware-williamtan/thnuclnt-7089/socket|ItemRemoved;|0x02000000|2015.12.21|6582951|4817|107|6637050|495701| 249174|511241|00000000006545fa|/Volumes/Macintosh HD/.fseventsd|0x1ef4eaeb|3958043678 private/var/folders/nh/p6dq7q1d7_sg5rzsqlc64z0r0000gn/T/vmware-williamtan/thnuclnt-7758/socket|ItemRemoved;|0x02000000|2015.12.21|6587030|4822|107|6637050|496248| 249174|511241|00000000006545fa|/Volumes/Macintosh HD/.fseventsd|0x1ef4eaeb|3958043678

The parser output allows you to see a file path, date of event, type of action or event, and the process associated with this event. 

## Forensic Value - What should we be looking at?

Parsed FSEvents can exceed 1 million records so it is important to focus on narrowing down specific events of interest. While FSEvents might not be the first place to investigate suspicious activity, it has incredible value as a supplemental artifact that can help indicate the existence of a file and actions a user or application performed. As an example, try filtering records for all plist files modified or created on a specific date. Plists are similar to registry hives in Windows, and for persistence OS X malware often creates plist files in /Library/LaunchAgents, Library/Preferences, /Library/LaunchDaemons, or /Library/Internet Plugins. One shortcoming of FSevent records is they do not include timestamps. This is because FSEventStreams does not log the exact timestamp, as the API’s expected usage is for an application to query all ordered events after a time or id. FSEventsParser is able to approximate an event’s occurrence by extracting the filename date from the Apple System Log file that was modified/created within an FSEvents file. Although FSEvents is a valuable artifact enabled by default, it is also it is possible to disable FSEvents completely. This is done by creating a .fseventsd

directory at the top level of the volume and then creating an empty no_log file in that directory. From our analysis of thousands of enterprise OS X systems, we have rarely observed this practice. 

## Using FSEvents to detect OS X Malware

As an example, let’s use FSEventsparser to identify a piece of malware called OSX/Iworm. Iworm is an OS X Trojan that connects infected hosts to a botnet by fetching IP addresses from social media website Reddit. After unleashing the Iworm on a virtual machine, we executed FSEventsParser on the system. Since malware often uses launch daemons as a persistence mechanism, we searched FSEventsParser on changes to folders /System/Library/LaunchDaemons/ and/Library/LaunchDaemons. Our search returned /Library/LaunchDaemons/com.JawaW.plist was created on 2/1/2016. Filtering on event flags ItemCreated, ItemModified, and ItemIsfile shows us multiple files were also created on the same date in a newly created folder /Library/Application Support/JavaW. [![lib](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/lib.png)](/content/dam/crowdstrike/www/en-us/wp/2016/03/lib.png) With a date and malware locations in hand, we can pivot on these artifacts to further identify the source of the compromise. 

## Closing thoughts

As enterprises adopt more Mac endpoints in their environment, the requirement for OS X forensic analysis will only become more prevalent. FSEvents is a valuable supplemental artifact to identify and investigate malicious artifacts that may no longer exist. This can play a major role in many different investigation types when other artifacts may not provide sufficient evidence. 

CrowdStrike now offers an OS X version of [Falcon Host](/en-us/products/falcon-host/) to assist and support Mac users for protecting their endpoints from today’s cyber attacks. Falcon Host’s ability to stop malware and non-malware attacks — along with the ability to act as a DVR for the endpoint to discover and investigate current and historic endpoint activity in seconds — augments the OS X features outlined in this blog for identifying and stopping malicious activity.

## References

https://developer.apple.com/library/prerelease/mac/documentation/Darwin/Reference/FSEvents_Ref/ https://github.com/dlcowen/FSEventsParser https://developer.apple.com/library/mac/documentation/Darwin/Conceptual/FSEvents_ProgGuide/ FileSystemEventSecurity/FileSystemEventSecurity.html#//apple_ref/doc/uid/TP40005289-CH6-SW1 http://blog.hostilefork.com/trashes-fseventsd-and-spotlight-v100/

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)