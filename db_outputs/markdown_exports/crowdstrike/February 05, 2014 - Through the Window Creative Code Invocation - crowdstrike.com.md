# Through the Window: Creative Code Invocation - crowdstrike.com

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/through-window-creative-code-invocation/
- **Date :** February 05, 2014

---

# Through the Window: Creative Code Invocation

February 05, 2014

• [ christian.dietrich](/en-us/blog/author.christian-dietrich/ "Posts by christian.dietrich") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")

![](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2016/03/Blue.jpg)

Recently, while analyzing a targeted attack, CrowdStrike observed an interesting code invocation technique that we want to describe here. This particular technique can be used to invoke code that has been injected into explorer.exe. Many targeted attacks involve executing malicious code. No matter how a target gets infected, at some point an adversary typically aims to execute some kind of remote access tool (RAT), which is then used, for example, to exfiltrate critical information from the victim. Furthermore, malware often strives for persistence and stealth. A popular way to achieve persistence and stealth on 32-bit Windows is to inject the malware into the process explorer.exe. Since explorer.exe is always running and since it is deemed benign, the malware has a higher chance to persist. The basic procedure to execute injected code consists of two steps: code injection and code invocation. First, the code to be executed has to be injected into a target process, such as explorer.exe. Then, this injected code must be triggered in order to execute. Windows offers a variety of ways to inject code into another process and have this code executed, and many of these techniques are well known. For example, one of the simpler ways to achieve this is the following:

  1. The malware acquires a handle to the target process, e.g., using OpenProcess().
  2. It allocates memory space in the target process and writes the code to be executed into the target process, e.g., using WriteProcessMemory().
  3. Finally, the malware can use the function CreateRemoteThread() to execute the newly injected code.



However, anti-virus solutions are aware of this specific method and will handle it appropriately. As a result, adversaries tend to use more subtle injection and invocation methods.

## Using Window Handling Procedures for Invocation

Recently, CrowdStrike has noticed increased use of a less-obvious code invocation technique. While the technique itself has been known to the security community [since at least the end of 2012](http://www.welivesecurity.com/2012/12/27/win32gapz-steps-of-evolution/), it is not as commonly observed as other techniques and bears witness of a skilled adversary. In this case, code injection into the running explorer.exe process is achieved by means of a shared section. For example, a malicious process would create a new section, and map views of this section into itself and explorer.exe. Subsequently, when the malicious process writes code into this shared section, the code will also be available from inside the target process. As part of the mapping, the base address of the shared section’s view in explorer.exe can be acquired. This will be needed later on, when preparing to trigger the injected code. Once the injection has worked, the injected code needs to be executed, and here creativity comes into play. In short, the goal of the malware is to overwrite a function pointer used by the taskbar’s window handling procedure. More precisely, Windows exhibits a feature called [extra window memory](http://msdn.microsoft.com/en-us/library/windows/desktop/ms633574\(v=vs.85\).aspx#extra_window_memory). Extra window memory allocates up to 40 bytes of memory with each instance of a window class that makes use of the extra window memory feature. In order to access and modify data of the extra window memory, the functions GetWindowLong() and SetWindowLong() can be used. In the context of malware, this extra window memory feature can be used for invocation under certain circumstances. For this to work, the malware acquires a handle to the taskbar window that is the only window of the window class “Shell_TrayWnd”. This window is always associated with explorer.exe. Thus, the malware calls FindWindowA(className=”Shell_TrayWnd”) to get a handle to the corresponding window. As a next step, the function SetWindowLong() is called. As described above, this function is intended to change attributes of a specific window and allows the malware to change values in the [extra window memory](http://msdn.microsoft.com/en-us/library/windows/desktop/ms633574\(v=vs.85\).aspx#extra_window_memory). The taskbar window uses extra window memory and stores a function pointer at offset 0. The disassembly below shows the corresponding part of the taskbar’s window handling procedure, located in explorer.exe. The taskbar’s window handling procedure makes use of the function pointer at offset 0 in the extra memory (contained in ESI):

`01001b48 mov eax, ; esi is a pointer to a pointer to a function 01001b4a push esi 01001b4b call` By calling SetWindowLong() with the taskbar’s window handle, an offset of 0, and a pointer to the entrypoint of the injected code as parameters, the malware can effectively replace the function pointer used by the taskbar’s window handler. The Relative Virtual Address (RVA) of the entry point needs to be adjusted to the base address of the shared section in the target process. Conveniently, this base address is stored in a pointer argument when calling MapViewOfSection(). In order to make sure that the modified function pointer of the window handler is triggered, the malware sends a message to the window, e.g., using SendNotifyMessageA() or PostMessageA(). In effect, this will result in the injected code being executed in the context of explorer.exe. Interestingly, overwriting the taskbar’s window handling procedure ([SetWindowLong() with offset GWL_WNDPROC](http://msdn.microsoft.com/en-us/library/windows/desktop/ms633591\(v=vs.85\).aspx)) is only allowed from the handling process itself (explorer.exe). However, overwriting the function pointer at offset 0 as discussed above is not bound to this restriction.

In summary, a typical sequence of API calls used in this invocation technique is shown in the pseudo code snippet below:

`// Create a shared section and map it into both, the current process`

`// as well as explorer.exe`

`ntdll.NtCreateSection(..)`

`ntdll.MapViewOfSection(hCurrentProcess, ..)`

`ntdll.MapViewOfSection(hExplorerProcess, ..)`

`// Find the taskbar window and overwrite the function pointer

`

`// used by its window handling procedure`

`hTaskbarWnd = user32.FindWindowA(..)`

`user32.SetWindowLong(hTaskbarWnd, 0, ppMalwareEP)`

`// Trigger the taskbar window handling procedure`

`PostMessageA(..)

or

SendNotifyMessageA(..)`

## 

## Example of a Recent Targeted Attack

Let’s turn to a recent sample used in a targeted attack. In fact, the PE binary with an MD5 hash of 111ed2f02d8af54d0b982d8c9dd4932e has been observed as part of an attack alleged to [have targeted embassies in a Middle East capital](http://blog.trendmicro.com/trendlabs-security-intelligence/recent-windows-zero-day-targeted-embassies-used-syria-related-email.html). Interestingly, this sample makes use of the above-mentioned invocation technique. While the sample employs a variety of methods to hinder analysis, we are primarily interested in the malware’s code injection and invocation in explorer.exe. In this case, the malware proceeds exactly as described above. First, it creates a shared section as shown in the disassembly below:

## 

[![13.04.51.CreateSection](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/13.04.51.CreateSection.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/13.04.51.CreateSection.png) Following that, the malware maps views of the section into its own process and into explorer.exe. The following figure shows the disassembly of the second call to MapViewOfSection where a pointer to the base address of the shared section’s view is stored in EDX. [![13.08.51.MapViewOfSection2](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/13.08.51.MapViewOfSection2.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/13.08.51.MapViewOfSection2.png)

Then, it proceeds by retrieving a handle to the taskbar window using FindWindowA() with a class name of Shell_TrayWnd. The class name string is decrypted by XOR’ing each character with 0x2E. Afterward, it overwrites the pointer used by the window handling function with the entry point of its injected code and triggers it using PostMessageA().

## [![13.13.30.FindWindow.full](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/13.13.30.FindWindow.full_.png)](https://www.crowdstrike.com/content/dam/crowdstrike/www/en-us/wp/2014/02/13.13.30.FindWindow.full_.png)

## Technique Variations and Improvements

This invocation technique exists in several variants. For example, one variant saves (using GetWindowLong()) and restores the original pointer to the window handling procedure for the taskbar window, once the injected code has been triggered. This particular variant has been observed with a malware referred to as [Powerloader](http://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/), as well as the [Hesperbot](http://www.welivesecurity.com/2013/09/06/hesperbot-technical-analysis-part-12/) banking trojan and the Gapz malware family.

Another related variant has been observed to avoid creating a new section, and instead it opens an existing shared section, such as BaseNamedObjectsShimSharedMemory. Using an existing shared section avoids the need to map a view of a newly created section into explorer.exe and is thus even less obvious. A more advanced variant of this technique attempts to tackle [DEP by means of Return-Oriented Programming (ROP)](http://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html).

In summary, this blog post examined a way of invoking code injected into explorer.exe by overwriting a function pointer used by the taskbar’s window handling procedure. Interestingly, this specific technique has been observed with both selected malware families in the cyber crime domain (Powerloader, Hesperbot banking trojan, Gapz), as well as at least one recent targeted attack.

For more information on this technique for process injection or the adversaries using it, including detection logic or any of the adversaries tracked by CrowdStrike, please contact: intelligence@crowdstrike.com and inquire about our Intelligence subscription.

[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Forrester%20Wave%20Threat%20Intel%202026-2-1060x698_Blog?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 17, 2026  CrowdStrike Named a Leader in The Forrester Wave™: External Threat Intelligence Service Providers, Q3 2026 ](/en-us/blog/crowdstrike-named-leader-forrester-wave-external-threat-intelligence-q3-2026/) [ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/)