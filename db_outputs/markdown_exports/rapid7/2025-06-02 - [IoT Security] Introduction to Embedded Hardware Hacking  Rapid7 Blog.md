# [IoT Security] Introduction to Embedded Hardware Hacking | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/02/20/iot-security-introduction-to-embedded-hardware-hacking/
- **Date :** 2025-06-02

---

Many security professionals and researchers are intrigued by the idea of opening up and exploring embedded technologies but aren’t sure where to start. In this blog post, we will point you toward a good starting point by covering a number of tools, basic methods, and concepts.

## Tools

Often, the first question people have when breaking into hardware hacking is, “Which tools do I need?” For the most part, only some basic tools are necessary to get started.

Tools commonly used by those conducting testing and research on embedded technology fall into the following categories:

  * Disassembly and assembly
  * Electronic signal analysis and measurement
  * System control and injection



These tools can come in many forms and cost anywhere from $20 to $30 each to upward of hundreds of dollars. In this guide, we’ll start with some basic tools in each category, but you can build out your tool sets further as you grow in experience and need.

### Disassembly and assembly

A good set of screwdrivers and pliers are very important here.

![1-1.png](https://www.rapid7.com/cdn/images/blt3f15a0ada0224fa4/683ddbb3ca9dfc18ee52651b/1-1.png)

Also, it’s typical to need to be able to solder and de-solder. Here, I would recommend spending a few extra dollars and buy an adjustable temperature soldering iron with interchangeable tips. You will need solder, solder flux, and de-solder wick.

![2.png](https://www.rapid7.com/cdn/images/blt68c116d8d04feb9d/683ddbd12cfe328f21dc14cc/2.png)

### Electronic signal analysis and measurement

In this category, I recommend two must-have tools: a simple digital multimeter and a logic analyzer.

![3.png](https://www.rapid7.com/cdn/images/blt18188f956b6fab24/683ddbfa543b8d7ae5bf1032/3.png)

A digital multimeter will come in hand for measuring voltage levels on devices and components, identifying ground, and mapping out circuit paths on circuit boards.

Logic analyzers are one of the primary analysis tools used by hardware researchers, testers, and engineers for analyzing digital signals on embedded devices. There are several brands out there, but I would recommend the Saleae, mainly because it’s a quality-built device and has several models available for different budgets.

![image3.png](https://www.rapid7.com/cdn/images/blt6c4fcbf2cc53bdf1/683ddc1dcc6042b34e206633/image3.png)

Another tool that can come in handy for identifying JTAG and UART ports is the JTAGULATOR. This tool allows you to connect all the pins of a header and automatically walk through and test all the possible pinout combinations to identify JTAG or UART.

![5.png](https://www.rapid7.com/cdn/images/bltd587f21b79b56157/683ddc427f8603e0be230660/5.png)

### System control and injection

This final group of tools helps with gaining access to, extracting, and/or altering data on the embedded technology. In this category, there are several inexpensive options available. The first is the faithful [Bus Pirate](https://dangerousprototypes.com/docs/Bus_Pirate_101_tutorial), which gives you the ability to connect to the UART, I2C, SPI, and JTAG communication protocols.

![6.png](https://www.rapid7.com/cdn/images/blt99e4f35d353d50ab/683ddc6673c8458117e8c232/6.png)

The [Shikra](https://int3.cc/products/the-shikra) is a similar device that supports UART, JTAG, and SPI protocol access, and is much faster than the Bus Pirate when extracting flash memory over SPI.

![7.png](https://www.rapid7.com/cdn/images/blt16e4073135900a2f/683ddc8f2a76869c57bc82ff/7.png)

The [Seggar J-link](https://www.segger.com/products/debug-probes/j-link/) is another tool for testing JTAG and Serial Wire Debug (SWD) and is more robust than Bus Pirate or Shikra. This JTAG tool is available in both a professional version and in a less-expensive education version.

![8.png](https://www.rapid7.com/cdn/images/blt0e0ea358e4b6a640/683ddcb32a768697cabc831b/8.png)

Also, for a good, all-around test tool, don’t forget about the [BeagleBone Black](https://beagleboard.org/black). This development platform can be used to conduct a number of tests.

![9.png](https://www.rapid7.com/cdn/images/blta9245afb7924bf5c/683ddcd84c5a098bab5e09a1/9.png)

To finish up, some basic odds and ends are needed, including jumper wires and headers that let you connect to the embedded devices for testing and hacking. Check out the following short list:

  * 1.27mm male straight single-row pin header
  * 2.54mm male straight single-row pin header
  * Male-to-male solderless flexible breadboard jumper wires
  * Male-to-female solderless flexible breadboard jumper wires



![10.png](https://www.rapid7.com/cdn/images/bltf8f7284480481045/683ddd0aaaf620273379dd5d/10.png)

## Hardware disassembly

The first phase of hardware hacking often involves gaining some physical access into the device. Here, you need to move slowly and be cautious to avoid damaging the equipment of injuring yourself.

A quick examination of the bottom of the device will often reveal screws used to disassemble the device. Sometimes these assembly screws can be hiding under labels and rubber feet, so don’t forget to check that out.

Another method is to look for FCC records. To do this, you first need to determine whether the device uses any wireless or radio frequency (RF) communication. If it does, it should have an FCC ID. This is often labeled on the device as a requirement by the FCC.

![11.png](https://www.rapid7.com/cdn/images/blt70a32b0c2cad9322/683ddd3318a55358b8686eef/11.png)

The FCC ID can be entered in at [this website](https://fccid.io/), which will return items such as RF test reports as well as internal and external images of the hardware. The internal images are the most helpful, as they’ll often reveal how the device is assembled.

![12.png](https://www.rapid7.com/cdn/images/blt7a45d1dea6200f5d/683ddd597f860373ab2306aa/12.png)

If you find out the case is glued or epoxied shut, all bets are off and you may need to use a Dremel tool or other potentially destructive tools to cut it yourself. If so, follow all safety precautions to ensure you don’t damage the circuit boards or worse, injure yourself. An example of this method is shown below:

![13.png](https://www.rapid7.com/cdn/images/bltb6d16de368fdabe7/683ddd80bc38b16768477bed/13.png)

## Circuit examination

Once inside the device, the goal is to identify and map out the circuit and components. A quick visual examination may reveal that the manufacturer has marked the board for key debugging connections such as JTAG, UART, and SWD:

![14.jpg](https://www.rapid7.com/cdn/images/bltce2e24daf6835f7f/683ddda43323a549e980a7ff/14.jpg)

After examining the board for obviously marked debug ports, I like to focus on identifying other important features such as header connections, which may be used for JTAG, UART, or other forms of debug access. Also, at this point, you will want to identify all the key IC chips (CPU, memory, RF, and WiFi).

![15.png](https://www.rapid7.com/cdn/images/bltb8db987e5cf26b08/683dddcc73c845b0fde8c290/15.png)

Once all the key IC chips have been identified, I recommend trying to download each of the identified component’s datasheets. These datasheets will play a significant role in further testing and analysis of the embedded device’s functionality and security. Most datasheets can be located by simply googling the device name and using the identifiers stamped on the face of the chips:

![16.png](https://www.rapid7.com/cdn/images/bltff72ef994c5eb3a5/683dddf53a1c5a4ea94ba7b7/16.png)

## Firmware

Examining firmware can also help reveal invaluable information when testing for security issues. There are a number of methods for gaining access to firmware. The first way is to see whether the vendor allows direct download over the internet. If firmware is not available directly from the vendor, my next step is attempting to capture it using Wireshark. This is accomplished by capturing all network communication while the embedded device is doing a firmware upgrade. If not encrypted, the firmware can often be extracted from the captured pcap data using the Export Objects feature within Wireshark.

![17.png](https://www.rapid7.com/cdn/images/blt9d6adc0dcfd714fd/683dde1b2a9b687cd82bd199/17.png)

If this is not possible, you may need to get more creative. Another option is via the examination of mobile application code used to manage or control the embedded device. It is not uncommon to see devices that are controlled and managed through your mobile phone also control the firmware upgrade process. With that in mind, examining the mobile application may reveal the URL Path and access codes needed to download the latest firmware.

Finally, when all else fails, it may be necessary to go directly to the flash memory storage on the device. There are multiple methods that are directly related to the type of flash memory on the board. This will require some research and analysis to identify the most effective method. For instance, can you read the flash in-circuit, or do you need it out of circuit, requiring you to de-solder the chip? Is it readable via SPI, or do you need some type of chip reader?

![18.png](https://www.rapid7.com/cdn/images/blt97cd882eeb344256/683dde4930073e79daeb1786/18.png)

Spending some time doing research online and looking at the datasheets will help you properly identify the memory storage and best methods for data extraction. I always try to seek out others who have encountered the same memory extraction issues. In those cases, Google can be your friend for finding them and their documented methods.

## Article tags

  * [IoT](/blog/tag/iot-security-news/)
  * [Research](/blog/tag/research/)