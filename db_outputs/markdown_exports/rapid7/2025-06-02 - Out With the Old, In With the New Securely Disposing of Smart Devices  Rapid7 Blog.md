# Out With the Old, In With the New: Securely Disposing of Smart Devices | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2025/01/06/out-with-the-old-in-with-the-new-securely-disposing-of-smart-devices/
- **Date :** 2025-06-02

---

So, what did you get for Christmas this year?

Hopefully you received some cool smart technology, or maybe you just upgraded your smart camera or voice assistant to a newer model or version. If you upgraded to a new model or version, what is your plan for the old device? Is it still working or is it broken?

Either way, you will need to figure out what to do with it: Donate it, sell it online, or maybe dispose of it as electronic waste. Before you make up your mind, let’s think through a few things.

## Have you done a factory reset?

The key reason you want to do a factory reset is to make sure the device is no longer customized according to your environment and that personal information such as WiFi passwords, email addresses, username and account passwords, and your name and home address are properly removed from the device prior to it leaving your hands.

Factory resets are accomplished in different ways, depending upon the device. For example, some devices have a button you press and hold, while others may use a mobile or web application to trigger the reset. I have also seen devices where you just cycle the power multiple times in sequence to reset the devices. Regardless of what the manufacturer’s recommended process is, it is very important that you follow it.

But what if the device appears to be broken? Well, if your old device truly is 100% dead, then there’s not much you can do about that. But the truth is, an IoT device may not be completely functioning yet it may still allow a factory reset to be done. For example, if the device appears to power up but doesn’t communicate correctly, you can try pushing and holding the reset button and see if the device resets (often indicated by the lights).

Now, let's say the device has a web application online or a mobile application and it shows the device is online — such as a smart light bulb or an Amazon Echo — but you cannot get it to work correctly. For example, the LED lights on a smart bulb don't light up or the Echo doesn’t respond to your voice. If the application is still showing the device is online, then chances are the network communication is still working, and the application may allow you to remote reset the device.

Again, if you can find a way to accomplish a factory reset, then you should do it.

## What could go wrong?

What could happen if you don’t properly reset a device and then dispose of it by selling it or giving it to someone else, who may in turn sell the device?

Out of curiosity and an attempt to answer this question, I purchased a box full of previously owned Amazon Echos online. Many of them were supposed to be broken, with most of them marked “dead speakers.” With that said, I had an important question to answer. _Did the owner use the Amazon Alexa online application to factory reset and remove the Echo device before selling or giving the device to the person who sold it to me?_ I proceeded to disassemble 10 of these devices and dumped their memory so that I could evaluate the results to see if any of them were still provisioned and contained any user data.

![Screenshot-2024-12-26-at-11.40.12-AM.png](https://www.rapid7.com/cdn/images/bltfb9c1589c82f609d/683de6f170aa954cf5fe31fe/Screenshot-2024-12-26-at-11.40.12-AM.png)

Out of the 10 devices I examined, 4 were found to still be provisioned. As a small example of the potential data accessible on these 4 devices, I conducted further examination and found these devices still containing the WiFi SSID and Pre-shared Key (PSK) for the user’s home networks. Having the PSK in hand can give a malicious actor access to the user’s home network.

To make matters worse, in one of the 4 provisioned devices, the user used his last name for the SSID and his home phone number for PSK. Using personally identifiable information in an SSID, such as a name and/or phone number, greatly increases the ease in tracing a device back to a specific person and physical location. In other words, I highly recommend you not do this.

In the case of the Amazon Echo specifically, critical data such as personal Amazon authentication account information is currently stored in encrypted storage on the devices; therefore, it would take more work for someone to gain access to that, but I would not say it is impossible. Also, it’s important to note that although Echo devices may be encrypting the user account information they store, not all smart products on the market follow those recommendations. So — once again — to reduce the risk of your data being compromised, it is important that you factory reset your devices prior to disposal.

## The proliferation of consumer-grade IoT devices in business.

It’s important to point out that the issue I’ve been discussing here doesn’t just apply to general consumers but also to businesses. Often, we assume that consumer-grade IoT technologies are only used by home users when in fact businesses of all sizes can and do leverage consumer-based IoT technology in the workplace environment. 

It’s common to see WiFi access points, smart TVs, smart cameras, TV streaming boxes, smart exercise equipment, consumer-grade printers, and yes, even smart voice assistants, being used within a number of organizations. For example, every year I build out exercises for [DEF CON IoT Village](/blog/post/2024/10/16/root-access-for-data-control-a-def-con-iot-village-story/) to help expose people to, and train them on, various aspects of hardware hacking. I purchase devices on the secondary market for this training and every year at least 40-50% of the devices I’ve purchased have not been factory reset. On more than one occasion, I have even purchased blocks of devices from a single reseller to find that those devices were not factory reset and were still configured with data from an operational business.

## Start the year off securely.

To summarize, here are the key takeaways from my experiment and the bigger conversation around disposing of old smart devices:

  1. Business IT and security leaders should have clear, cradle-to-grave processes governing the IoT technologies purchased, so that the organization is not exposed to unnecessary risk. Cradle to grave covers initial installation and provisioning, ongoing maintenance, and, in the end, safe and secure disposal of the technology.
  2. Consumers should make sure to do a proper factory reset prior to the disposal or resale of any smart devices. Keep in mind that even if the device appears to be broken, a factory reset is still often possible — see my guidance earlier in this blog.
  3. If you cannot factory reset your device and you’re concerned about the data on the device, you can always change your SSID, PSK, and account password.



Finally, always remember to never dispose of your IoT technology in the trash, as landfills are not the proper place to send them. Instead, these devices should be sent to an electronic waste disposal option in your local area. 

If you are looking for a deeper dive check out this [research paper on Amazon echo dot devices](https://www.khoury.northeastern.edu/home/noubir/publications-local/GN2021.pdf) from Northeastern University. Happy New Year!

## Article tags

  * [IoT](/blog/tag/iot-security-news/)
  * [Research](/blog/tag/research/)