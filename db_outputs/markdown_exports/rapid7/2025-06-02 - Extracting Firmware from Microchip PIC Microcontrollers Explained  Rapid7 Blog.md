# Extracting Firmware from Microchip PIC Microcontrollers Explained | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/04/30/extracting-firmware-from-microcontrollers-onboard-flash-memory-part-3-microchip-pic-microcontrollers/
- **Date :** 2025-06-02

---

_This blog is part three in a four-part series on hardware hacking for the security professional and researcher. Be sure to check out_[ _part one_](/blog/post/2019/04/16/extracting-firmware-from-microcontrollers-onboard-flash-memory-part-1-atmel-microcontrollers/) _, which covers Atmel microcontrollers, and_[ _part two_](/blog/post/2019/04/23/extracting-firmware-from-microcontrollers-onboard-flash-memory-part-2-nordic-rf-microcontrollers/) _, which discusses Nordic RF microcontrollers._

In this blog, we will conduct further firmware extraction exercises and cover the Microchip PIC microcontroller PIC32MX695F512H. To be able to gain access to the firmware on PIC microcontrollers, we will need to read directly from the controller over the in-circuit serial programmer (ICSP).

The ICSP is another method that makes it possible for a microcontroller (MCU) to be programmed or reprogrammed while in-circuit. We will use the following tools and software to accomplish this:

  * [PICKit 3](https://www.microchip.com/developmenttools/ProductDetails/pg164130)
  * [Microchip MPLab X IDE Software](https://www.microchip.com/mplab/mplab-x-ide)
  * [Microchip PIC microcontroller Datasheet](http://ww1.microchip.com/downloads/en/devicedoc/60001156j.pdf)



The PICkit 3 is an inexpensive in-circuit debugger. Even cheaper generic versions of the device are available as well. In our experience, both brand-name and generic versions have worked well.

![1_PIN_Indicator.png](https://www.rapid7.com/cdn/images/blt6b3256ea595893d2/683de0a94b2b7f957ee1614e/1_PIN_Indicator.png)

PICkit 3| Function  
---|---  
VPP (or MCLR)| Programming voltage (usually 13V)  
VCC or VDD| Power (usually 5V)  
VSS or GND| Ground (0 volts)  
ICSPDAT \ PGD| Data – usual port and connection RB7 (PGED)  
ICSPCLK \ PGC| Clock – usual port and connection RB6 (PGEC)  
PGM – LVP| Low Voltage Programming – usual port and connection RB3/RB4  
  
When attaching the PICkit 3 to the circuit board for debugging, it is not uncommon to find an associated header on a circuit board for the PIC ICSP. An example of this is shown below:

![2_Header_PIC_MCU.png](https://www.rapid7.com/cdn/images/bltb7b1a782194ce676/683de0d14b2b7f0d31e1615e/2_Header_PIC_MCU.png)

It is also important to assume the ICSP header may not be pinned out as expected, meaning just plugging the PICkit 3 in may not have the expected results. We recommend validating the pinout first. This is best done using the datasheet for the MCU and a multimeter set on continuity to ring out the ICSP header to the actual pins on the chip.

In this example, using the datasheet for the PIC32MX695F512H MCU and a multimeter, we discovered that the header pinout is for the MCU’s ICSP, but its pin layout was not in the correct pinout order to connect directly, as shown below:

![3_ISCP_Pinout.png](https://www.rapid7.com/cdn/images/blt6c57d445e404da67/683de0f6a38fc55371032099/3_ISCP_Pinout.png)

As you can see, it is helpful to always double-check pinouts before attaching any debugger or analyzer to a circuit board. It will save you many headaches down the road and could help prevent damage to affected components. Also note that pin 6 PGM – LVP on the PICkit 3 is not used. This pin is only needed when programming certain MCU devices, and from what I understand is never needed when reading the flash memory.

Once the PICkit 3 is successfully attached to the target device, you will need to download and install the [MPLab X IDE](https://www.microchip.com/mplab/mplab-x-ide) software available from Microchip. Once installed, it is time to extract the firmware from the MCU.

![5_ISCP_Pinout.png](https://www.rapid7.com/cdn/images/blt6fdef5530050db85/683de11acc6042def32067ac/5_ISCP_Pinout.png)

Open the MPLAB X IDE software and create a new project. You can use the defaults for Category and Project Type. When prompted to select a device, select the Family and the device type being tested. In our example, we used the following:

  * Family: 32-bit MCUs (PIC32)
  * Device: PIC32MX695F512H



When prompted to select your tool, pick the debugger being used (in our case, the PICkit 3). In the next step, you will need to select Compiler for extracting firmware. You won’t need this, but it’s required to set up a project. Select what is available, or if you’re using this tool for the first time, you may be required to download a compiler. The final step is to give your project a name and select Finish.

At this point, you should be ready to read memory from the MCU. This is done by selecting the icon pictured here: 

![6_Icon.png](https://www.rapid7.com/cdn/images/blt6550594307ab77af/683de141bc38b12996477d24/6_Icon.png)

Then, select Read Device Memory.

If properly set up and connected, the PICkit 3 status light should begin blinking red and you should see the following information within the MPLAB application, followed by a prompt to save the file:

![7_MPLAB_Output.png](https://www.rapid7.com/cdn/images/blt6ae145762d494752/683de16318a5538ac7687070/7_MPLAB_Output.png)

When saving a file, it will be saved as an Intel Hex file type. To be able to examine and test the firmware further, you will need to convert it to a binary file type. This can easily be done using the Linux application hex2bin, as shown below:

![8_Hex2bin.png](https://www.rapid7.com/cdn/images/bltae18dcd9cbac3d81/683de186c26e07f2b628e7c3/8_Hex2bin.png)

Once it is converted to a binary, you will be able to do further testing against the firmware and use other applications such as Binwalk to extract data.

We also recommend exploring the features of MBLab X IDE. For example, once firmware is extracted, look under the configuration bits menu. This will show you the chip’s configuration and security settings.

![9_Configuration_Bits.png](https://www.rapid7.com/cdn/images/blt401e7f0898c95aae/683de1aaa38fc56e9b0320c3/9_Configuration_Bits.png)

_Check back next week for the fourth and final part of this series, which will go into detail on Texas Instrument RF microcontrollers._

## Article tags

  * [IoT](/blog/tag/iot-security-news/)
  * [Research](/blog/tag/research/)