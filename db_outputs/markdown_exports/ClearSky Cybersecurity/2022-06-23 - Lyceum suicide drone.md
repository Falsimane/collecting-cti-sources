# Lyceum suicide drone

- **Source :** ClearSky Cybersecurity
- **URL :** https://www.clearskysec.com/lyceum-suicide-drone/
- **Date :** 2022-06-23

---

ClearSky discovered a new malware associated with the Iranian SiameseKitten (Lyceum) group with  
medium-high confidence.  
The file is downloaded from a domain registered on June 6th, and it communicates with a previously unknown command and control server whose IP address is adjacent to that of the domain. 

This indicates an attacker-controlled at least two IP’s on the same range.  
The downloaded file is a reverse shell that impersonates an Adobe update.   
The reverse shell is dropped by a parent file signed with a fake Microsoft certificate, along with a lure PDF document and an executable designed to establish persistence.  
There seems to be a shared use of fake Microsoft certificates by a variety of Iranian groups, as Phosphorus was previously observed.  
Additionally, the lure PDF document relates to drone attacks conducted in Iran, resembling a similar document previously employed by SiameseKitten3.

Read the full report: <https://www.clearskysec.com/wp-content/uploads/2022/06/Lyceum-suicide-drone-23.6.pdf>