# Hardware Hacking: Extracting Firmware from Nordic RF Micrcontrollers | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/04/23/extracting-firmware-from-microcontrollers-onboard-flash-memory-part-2-nordic-rf-microcontrollers/
- **Date :** 2025-06-02

---

_This blog is part two in a four-part series on hardware hacking for the security professional and researcher._[_Click here to check out Part 1_](/blog/post/2019/04/16/extracting-firmware-from-microcontrollers-onboard-flash-memory-part-1-atmel-microcontrollers/) _, which covers Atmel microcontrollers._

In this blog, we will conduct another firmware extraction exercise dealing with the Nordic RF microcontroller (nRF51822). To be able to gain access to the firmware on nRF51822, we will access the controller using Serial Wire Debug (SWD).

SWD is a common two-pin JTAG debug interface most often found on small form-factor MCUs:

  1. SWDIO
  2. SWCLK



For this example, we will use the following tool, application, and datasheet:

  * [nRFJProg](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/nRF5-Command-Line-Tools/Download)
  * [Segger J-Link Debugger](https://www.segger.com/products/debug-probes/j-link/)
  * [nRF51822 Datasheet](https://infocenter.nordicsemi.com/pdf/nRF51822_PS_v3.1.pdf)



The Segger J-Link debugger is a professional JTAG device and can be expensive—starting at nearly $400—but for not-for-profit educational purposes, Segger does make available an [EDU version](https://www.segger.com/products/debug-probes/j-link/models/j-link-edu/) with some limited functionality, for about €50.

Our target device today is a Bluetooth Low Energy (BLE) tracking device running a Nordic nRF51822 MCU. This tracking device is typically used to find your lost keys.

![BLE-tracking-device.png](https://www.rapid7.com/cdn/images/blt60a0d03e5534b616/683ddefb3beff0a8eba7c3a9/BLE-tracking-device.png)

The nice thing about this device is that it appears to have a location for a four-pin 1.27 mm header. We will need to ring out this header to determine whether it connects to our SWD debug on this chip. First, we will need to download the datasheet for the nRF51822 and determine the locations of the following pins. Then, we can use a multimeter set on the continuity check to trace out the pins to the header pins:

  1. SWDIO
  2. SWCLK
  3. VDD = 3v Power
  4. VSS = Ground



![VDD.png](https://www.rapid7.com/cdn/images/blt4fe509b22eb20f0b/683ddf2170aa957879fe3002/VDD.png)

Using the above datasheet pinout and the multimeter, we successfully traced out the necessary SWD connection to the header, as shown below

![GND.png](https://www.rapid7.com/cdn/images/bltef5ceafa2c375cc7/683ddf4ccc604231a020672a/GND.png)

The next step is to solder headers onto the circuit board and connect the device to the Segger J-Link SWD using the following arrangement:

Tracker| J-link  
---|---  
Ground| Pin 4 GND  
SWCLK| Pin 9 SWCLK  
SWDIO| Pin 7 SWDIO  
3V Power| Pin 1 VTref  
  
In this example, we used some small clips to connect the J-Link to the headers on the circuit board. It is also important to ensure the device has sufficient power. This simple device is powered by a common three-volt coin cell battery.

![USB.png](https://www.rapid7.com/cdn/images/bltb0c3ba476a94ec1c/683ddf715619a1835cc6ea31/USB.png)

Once you’re connected and the J-Link is plugged into your host USB, the next step is to install the nRF5 Command Line Tools. This software is available for Windows, Linux, and macOS. The version we are using is for macOS. Once downloaded and extracted, you can change directories into the extracted archive folder and run the command-line application nRFJPROG. Here is an example command to read the MCU’s registries:

./nrfjprog --readregs

![AUS-MBP-big.png](https://www.rapid7.com/cdn/images/blt79f0fa075862486d/683ddf943d7b5ed1a21365e6/AUS-MBP-big.png)

Next, we can use the command-line application to also read and write other key segments of the device’s memory. We recommend examining the other arguments of the nrfjprog application, which can be listed by running this command:

./nrfjprog --help

Here is an example command to read the MCU’s flash and output it to a file:

./nrfjprog --readcode dump_nRF51822.hex

![AUS-MBP-SMALL.png](https://www.rapid7.com/cdn/images/blt508d4b2311873ecc/683ddfb8aaf620aef379de3d/AUS-MBP-SMALL.png)

Once the flash is extracted, it will need to be converted to binary. This can be done with the hex2bin application using the following command:

hex2bin dump_nRF51822.hex

![hex2bin.png](https://www.rapid7.com/cdn/images/blt17485fae1259b77c/683ddfe65619a1c192c6ea4f/hex2bin.png)

This command will convert the intel hex file (dump_nRF51822.hex) to a binary file format (dump_nRF51822.bin) for further testing and examination.

Be sure to check out the other blogs in this series here:

  * [Part One: Extracting Firmware from Atmel Microcontrollers](/blog/post/2019/04/16/extracting-firmware-from-microcontrollers-onboard-flash-memory-part-1-atmel-microcontrollers/)
  * [Part Three: Extracting Firmware from Microchip PIC Microcontrollers](/blog/post/2019/04/30/extracting-firmware-from-microcontrollers-onboard-flash-memory-part-3-microchip-pic-microcontrollers/)



## Article tags

  * [IoT](/blog/tag/iot-security-news/)
  * [Research](/blog/tag/research/)