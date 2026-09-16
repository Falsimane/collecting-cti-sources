# The Story of Thanos and Spook Ransomware (Part 1)

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/the-story-of-a-ransomware-builder-from-thanos-to-spook-and-beyond-part-1
- **Date :** 2022-02-17

---

## Introduction

During an onsite incident response analysis, CERT-Sekoia was contacted in order to respond to a Spook ransomware attack.

After gathering the evidence, we identified that malicious actors used a legitimate VPN account to initiate the first connection. The account was also a  _Domain Administrator_ in the company Active Directory. All lateral movements used this account via RDP or SMB. We suspect that this valid account was acquired earlier in 2021, and potentially from an initial Access Broker, because:

  * Local computers’ files and artifacts show the presence of 2 executables containing Mimikatz and netscanner with a last modification date back in July 2021;
  * From the few residual logs available on the VPN appliance, shortly before the VPN session was established, the user was added to the VPN allowed group. We identified a web administration interface exposed to the internet;
  * The version of the software appliance was several months late in security updates, thus exposed to critical CVEs;
  * The duration of the attack (time elapsed between the 1st VPN connexion and the end of encryption routine) was less than an hour;
  * RDP and SMB failed authentications show errors with incorrect domains, these domains referring to known Spook’s victims, followed by other typo errors. It could indicate an operator making copy / paste actions.



Finally, three binaries were executed remotely via PSExec, which led to the encryption of all of the companies’ files. It occurred only on the few systems up at the time of the operation (4 AM on a Sunday morning). All 3 binaries had a prefix “Worker-”, but none of them were retrieved. We suppose that each of them has a specific purpose with the last one responsible for covering threat actor’s actions. A ransom note was dropped on the victim’s desktops detailing the payment and contact details to pay the ransom. The indicated website was the Spook leak website, hosted on a tor onion address.

While attempting to recover the client’s files, it appeared that  _Volume Shadow Copies_ (VSC) had not been deleted on the main file sharing server. Incident responders thus tested a VSC recovery on a sample of files, which happened successfully.

![CERT-Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655124_6a92a4daa2f46752fd02934d_6a2a782c9d93c6b6fdaf35f1.webp)

Source: CERT-Sekoia

## Understanding a Spook sample

Following the previous incident response, we chose to focus on Spook ransomware. As per many other ransomware, Spook was conceived using the Thanos builder. The Thanos builder was first advertised on the XSS forum in February 2020 by the actor Nosophoros. It was sold using a subscription format, which explained its integration in other ransomware considered as variants, such as Spook. The most common sample found through different resources has the SHA-256 hash: [8dad29bd09870ab9cacfdea9e7ab100d217ff128aea64fa4cac752362459991c](https://www.virustotal.com/gui/file/8dad29bd09870ab9cacfdea9e7ab100d217ff128aea64fa4cac752362459991c).

The executable is an obfuscated .NET binary. ExeInfo PE indicates the obfuscator commercial tool SmartAssembly in version 6.5.2–612.X.

![CERT-Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655127_6a92a4e1e9a71d422840ae9e_6a2a782e9d93c6b6fdaf3614.webp)

Source: CERT-Sekoia

With this information, we fire [de4dot from the archived repository](https://github.com/de4dot/de4dot) to get a readable version of our sample. Unfortunately, the tool failed to deobfuscate function names, class names, and the resource section that stores all the strings even though it detects an obfuscator. An [article from Fortinet](https://www.fortinet.com/blog/threat-research/analysis-of-net-thanos-ransomware-supporting-safeboot-with-networking-mode) dating back to July 2020 mentioned the same behavior, but did not provide the process to get a readable sample.

![CERT-Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655158_6a92a4ea878de395f10edda8_6a2a782f9d93c6b6fdaf366b.webp)

Source: CERT-Sekoia

After a few Google searches, we found this [very interesting article from Jason Reaves](https://medium.com/walmartglobaltech/decoding-smartassembly-strings-a-haron-ransomware-case-study-9d0c5af7080b), detailing how Haron (a former ransomware also built with Thanos) obfuscation works based on SmartAssembly. He has not provided the SmartAssembly version within the article, but from its sample it seems it’s 7.5.1.4370. By opening our sample in [DNSpy](https://github.com/dnSpy/dnSpy), we get v8.0.2.4779.

![CERT-Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e865511f_6a92a4e4a2f46752fd0299ed_6a2a782e9d93c6b6fdaf361d.webp)

Source: CERT-Sekoia

Even if the versions are different, we tried to follow his process. We retrieve the same type of constructor to retrieve a string. Each different class declares a first attribute of type  _GetString_. It leads us to the module  _SmartAssembly.Delegates_ in our .NET browser.

![CERT-Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655148_6a92a4e53e6167cebbf738cd_6a2a782e9d93c6b6fdaf3620.webp)

Source: CERT-Sekoia

The second point is the usage of  _Strings.CreateGetStringDelegate_ (from  _SmartAssembly.HouseofCards_ module) based on the class  _Strings_ (from  _SmartAssembly.StringsEncoding_) with the parameter  _typeof(NameOfTheClass)_.

![Searches about Thanos and spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e865513c_6a92a4e33e6167cebbf737a9_6a2a782e9d93c6b6fdaf361a.webp)

Searches about Thanos and spook ransomware / Source: CERT-Sekoia

This function retrieves the attribute  _GetType_ from the class parameter (of type GetString), and defines an unnamed  _DynamicMethod_ belonging to the class parameter’s module, taking an integer as input and returning a string. Then, it retrieves the first method of the  _Strings_ class which returns a  _string_ value: the  _Get_ method like the screenshot below shows.

![Searches about spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e865513f_6a92a4e23e6167cebbf73751_6a2a782e9d93c6b6fdaf3617.webp)

Searches about spook ransomware / Source: CERT-Sekoia

Let’s take a look at the Strings class now, where all the obfuscation mechanics happens. This class stores basic information regarding where strings are located associated with different constants:

• An offset value, hardcoded with 75 as a class attribute;

• An initial XOR value with the integer parameter sets to 107396847 (in hexa 0x666BEEF).

![Researches about Thanos and spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655155_6a92a4e62b0ef7af46bd8e37_6a2a782e9d93c6b6fdaf3623.webp)

Researches about Thanos and spook ransomware / Source: CERT-Sekoia

Notice, a cache feature to avoid decrypting a string several times, controlled by a class attribute  _cacheStrings_ sets at the initialization of the class with a default value to  _True_.

![CERT-Sekoia](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e865512a_6a92a4dd32517fc40260a028_6a2a782e9d93c6b6fdaf3608.webp)

Source: CERT-Sekoia

We learn that strings are located inside a manifest resource named  _{56258a19–7489–468b-86ee-e7899203d67c}_ and uncompressed with a custom  _Unzip_ command. This function is defined in the  _Zip_ module.

![Strings about spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655152_6a92a4e8a49553afbaf403c3_6a2a782f9d93c6b6fdaf364f.webp)

Strings about spook ransomware /Source: CERT-Sekoia

This decompression function starts by creating a custom  _ZipStream_ attribute which is a child class from  _MemoryStream_ with two additional methods:

•  _ReadShort_ which returns the result of the parent class method  _ReadByte_ , which reads and casts a byte to Int32. If the parent’s method return -1 (end of stream) the function returns 0;

•  _ReadInt_ , same function but for a word (16 bytes) by using the  _ReadShort_ method.

The next step checks a header inside the resource file against the value ‘{z}\x00’ (the code shows 8223355, which is the unsigned 32-bit value). From the resource we get ‘{z}\x03’.

![Strings about spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e865514f_6a92a4eac4c3270826c4f7e8_6a2a782f9d93c6b6fdaf3654.webp)

Strings about spook ransomware/ Source: CERT-Sekoia

To get the value where the next switch statement is based on, a 24 right bit-shift is performed on the initial unsigned 32-bit integer read (do not forget that we are in little endian) leading to value 0x03. The switch has only two cases:

• 1 = uncompress the content

• 3 = decrypts with the symmetric algorithm AES and hardcoded values for key and initial vector

In this case the stream is decrypted. In the screenshot below,  _array2_ represents the hardcoded key and  _array3_ the hardcoded initial vector for the symmetric AES encryption algorithm. Then, the new stream is passed again to the  _Unzip_ function.

![Strings about spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e865514b_6a92a4e03e6167cebbf735c7_6a2a782e9d93c6b6fdaf3611.webp)

Strings about spook ransomware / Source: CERT-Sekoia

Using the same process as described above we managed to decrypt the first stream. The newly decrypted one has the following header ‘{z}\x01’: the switch case will go in the first option where data is simply uncompressed.

![Strings about spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655136_6a92a4dba2f46752fd0293a5_6a2a782c9d93c6b6fdaf35f4.webp)

Strings about spook ransomware/ Source: CERT-Sekoia

Finally, we get a chain of strings prefixed with a one byte value. Based on the article of Jason Reaves, we thought that the integer prefix was the length of the string. We tried to use his proof of concept: it works for a small part of the data before raising an Exception regarding value to decode in UTF-8.

By looking in the  _GetFromResource_ method from the custom  _Strings_ class, it looks like different operations are run before returning the final string. The first byte of the string is actually related to its length but does not represent the value itself for a specific case: if the value after the logical AND with 0x80 is not 0. In this case, the string length is evaluated through a long lambda function. We can split it in 3 parts:

  * The condition is again an AND operation with 0x40 value
  * if true, then



(num & 0x1F) << 24) + (bytes[index++] << 16) + (bytes[index++] << 8) + bytes[index++]

  * if false



((num & 0x3F) << 8) + bytes[index++]

The 0x80 (10000000in binary) and 0x40 (01000000 in binary) values are linked to the UTF-8 stream of a string as explained in this [stack-overflow thread](https://stackoverflow.com/questions/3911536/utf-8-unicode-whats-with-0xc0-and-0x80).

![spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655133_6a92a4dbfd507e2a51b9e0be_6a2a782d9d93c6b6fdaf35f9.webp)

spook ransomware / Source: CERT-Sekoia

Compiling all this knowledge in a small Python script, we were able to decode the entire resource. Some of these strings show additional base64 and reversed base64 encoding schemas: we adjust the code to get a full plaintext.

![Thanos and spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655145_6a92a4e712f236c0e864b157_6a2a782e9d93c6b6fdaf364b.webp)

Thanos and spook ransomware/ Source: CERT-Sekoia

But one question remains, how to browse the original code and get the decoded string from the resource that the function we are currently analyzing uses (associating an integer to its readable value)?

![Thanos and spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655142_6a92a4dcfd507e2a51b9e14f_6a2a782e9d93c6b6fdaf3604.webp)

Thanos and spook ransomware/ Source: CERT-Sekoia

How to recover FTP method  _STOR_ from integer value  _107364636_ ?

![Thanos and spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e8655139_6a92a4dfdb65986262ae20ca_6a2a782e9d93c6b6fdaf360e.webp)

Thanos and spook ransomware/ Source: CERT-Sekoia

Splitting into parts the python code and passing the integer observed to a decode function does not work. We missed something.

Back to the delegate function in module  _HouseofCards_ and class  _Strings_ , we notice that 4 calls to Opcodes are used:

  * _OpCodes.Ldarg_0_ which pushes the argument at index 0 representing the integer used by the  _Get_ method in the Strings class;
  * _OpCodes.Ldc_I4_ which pushes a 32-bit integer on the stack, in this case the  _MetadataToken_ of the input class (the AND operation with 0xFFFFFF = 16777215 is meaningless);
  * _OpCodes.Sub_ which subtracts the last value to the previous value pushed on the stack;
  * _OpCodes.Call_ which simply call the function  _Get_ of the  _Strings_ class with the result of the previous subtraction.



![Research of CERT Sekoia about Thanos and spook ransomware](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a69212f236c0e865512e_6a92a4dec5553634ac94c0ae_6a2a782e9d93c6b6fdaf360b.webp)

Research of CERT Sekoia about Thanos and spook ransomware

The one-string decoder requires adding a subtraction with the value of the MetadaToken of the function, which is printed as RID in DNSpy.

We have released the source code on the [CERT GitHub repository](https://github.com/SekoiaLab/CERT-Services/tree/main/202202-thanos_story_of_a_ransomware), but [Jiří Vinopal](https://twitter.com/vinopaljiri/status/1470200362929901574?s=20) created an easier way to deal with SmartAssembly v8+ on [his late 2021 tweet](https://twitter.com/vinopaljiri/status/1470200362929901574?s=20). By using the latest version (2015) of [ _Simple Assembly Explorer_](https://github.com/wickyhu/simple-assembly-explorer/releases/tag/v1.14.4) and its integrated deobfuscator using the profile  _Name, String and Flow_ and checking the box  _Delegate Call_ , associated with the famous old one [ _de4dot_](https://github.com/de4dot/de4dot), you get the sample deobfuscated and more readable. You just have to spend some time on base64 strings.

Our script is able to decode:

  * The entire resource content previously extracted from the malware;
  * An unique integer associated to its RID function to a plaintext string;
  * Several strings associated to a rid.



All commands require the resource file (extracted from the sample), the key and initial vector hardcoded inside the [malware](/blog/nobeliums-envyscout-infection-chain-goes-in-the-registry-targeting-embassies) (Module  _SmartAssembly.Zip_ — Method  _Unzip_). The tool has been tested on different samples of Spook ransomware, but also on other ransomwares known for using the Thanos builder (Hackbit, Haron, RecoveryGroup) or even on most recent threat actors like Midas. This one has the same process, they just change the hardcoded value for the XOR and offset in the  _Get_ method of the custom  _Strings_ class. We adjust our code to be more customizable regarding this modification. The last version of SmartAssembly tested ([Midas ransomware](https://www.virustotal.com/gui/file/575d1ef0e51fbe96e7454b8f06b60118faf3e4ed7ef0f98908d0fcca6c0a9b82)) was v8.0.3.4821.

## Conclusion

To conclude, starting from an incident response involving an opportunist threat actor, we succeeded in providing fresh intelligence on how obfuscation is implemented by the Thanos builder. Considering that malicious actors can acquire this builder for a few dollars, we will see in the second part, written by Sekoia’s Threat and Detection Team (TDR), how the above-mentioned intelligence can be extended to the entire ransomware ecosystem. 

You can also read our [article on the log4shell vulnerability.](/blog/log4shell-the-defenders-worst-nightmare)

## External resources

  * ‍[Medium - Decoding SmartAssembly strings, a Haron ransomware case study](https://medium.com/walmartglobaltech/decoding-smartassembly-strings-a-haron-ransomware-case-study-9d0c5af7080b)[‍](https://stackoverflow.com/questions/3911536/utf-8-unicode-whats-with-0xc0-and-0x80)
  * [Stack Overflow - UTF-8 & Unicode, what's with 0xC0 and 0x80?](https://stackoverflow.com/questions/3911536/utf-8-unicode-whats-with-0xc0-and-0x80)[‍](https://www.fortinet.com/blog/threat-research/analysis-of-net-thanos-ransomware-supporting-safeboot-with-networking-mode)
  * [Fortinet - Analysis of .NET Thanos Ransomware Supporting Safeboot with Networking Mode](https://www.fortinet.com/blog/threat-research/analysis-of-net-thanos-ransomware-supporting-safeboot-with-networking-mode)[‍](https://github.com/SekoiaLab/CERT-Services/tree/main/202202-thanos_story_of_a_ransomware)
  * [GitHub - The story of a ransomware builder: from Thanos to Spook and beyond (Part 1)](https://github.com/SekoiaLab/CERT-Services/tree/main/202202-thanos_story_of_a_ransomware)