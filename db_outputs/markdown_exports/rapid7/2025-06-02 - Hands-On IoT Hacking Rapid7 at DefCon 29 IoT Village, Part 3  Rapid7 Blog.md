# Hands-On IoT Hacking: Rapid7 at DefCon 29 IoT Village, Part 3 | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2021/11/04/hands-on-iot-hacking-rapid7-at-defcon-29-iot-village-part-3/
- **Date :** 2025-06-02

---

In our [first post](/blog/post/2021/10/21/hands-on-iot-hacking-rapid7-at-defcon-iot-village-pt-1/) in this series, we covered the setup of Rapid7's hands-on exercise at Defcon 29's IoT Village. [Last week](/blog/post/2021/10/28/hands-on-iot-hacking-rapid7-at-defcon-29-iot-village-pt-2/), we discussed how to determine the UART status of the header we created and how to actually start hacking on the IoT device. The goal in this next phase of the IoT hacking exercise is to turn the console back on.

To accomplish this, we need to reenter the bootargs variable without the console setting. To change the bootargs variable, the "setenv" command should be used**.** In the case of this exercise, enter the following command as shown in Figure 16. You can see that the "console=off" has been removed. This will overwrite the current bootargs environment variable setting.

![Untitled--16-.png](https://www.rapid7.com/cdn/images/blt4a2861bd01063abf/683dead265b8ea8a22cc8fcd/Untitled--16-.png)

Once you've run this command, we recommend verifying that you've correctly made the changes to the bootargs variable by running the "printenv" command again and observing that the output shows that "console=off" has been removed. It is very common to accidentally mistype an environment variable, which will cause errors on reboot or just create an entirely new variable that has no usable value. The correct bootargs variable line should read as shown in Figure 17:

![Untitled--17-.png](https://www.rapid7.com/cdn/images/blt24f9c1ab810616f4/683dead6a38fc53df003234d/Untitled--17-.png)

Once you're sure the changes made to bootargs are correct, you'll need to save the environment variable settings. To do this, you'll use the "saveenv" command. Enter this command in the UART console, and hit enter. If you miss this step, then none of the changes made to the environment variables of U-Boot will be saved and all will be lost on reboot.

The saveenv should cause the U-Boot environment variables to be written to flash and return a response indicating it is being saved. An example of this is shown in Figure 18:

![Untitled--18-.png](https://www.rapid7.com/cdn/images/blta9a34d5387c83070/683deada2cfe32717ddc1974/Untitled--18-.png)

## Reboot and capture logs for review

Once you've made all the needed changes to the U-Boot environment variables and saved them, you can reboot the device, observe console logs from the boot process, and save the console log data to a file for further review. The boot log data from the console will play a critical role in the next steps as you work toward gaining full root access to the device.

Next, reboot the systems. You can do this in a couple of different ways. You can either type the "reset" command within the U-Boot console and hit enter, which tells the MCU to reset and causes the system to restart, or just cycle the power on the device. After entering the reset command or power cycling the device, the device should reboot. The console should now be unlocked, and you should see the kernel boot up. If you still do not have a functioning console, you either entered the wrong data for bootargs or failed to save the settings with the "saveenv" command. I must admit I am personally guilty of both many times.

During the Defcon IoT Village exercise, we had the attendees capture console logs to a file for review using the following process in GtkTerm. If you are using a different serial console application, this process will be different for capture and saving logs.

In GtkTerm, to capture logs for review, select "Log" on the task bar pulldown menu on GtkTerm as shown below in Figure 19:

![Untitled--19-.png](https://www.rapid7.com/cdn/images/blt3175b93cd4276793/683deadd237ea61a7d91c555/Untitled--19-.png)

Once "Log" is selected, a window will pop up. From here, you need to select the file to write out the logs to. In this case, we had the attendees select the defcon_log.txt file on the laptops desktop as shown below in Figure 20:

![Untitled--20-.png](https://www.rapid7.com/cdn/images/blt20027f83ca187e4b/683deae030073e7a5beb1b5b/Untitled--20-.png)

Once you've selected a log file, you should now start capturing logs to that file. From here, the device can be powered back on or restarted to start capturing logs for review. Let the system boot up completely. Once it appears to be up and running, you can turn off logging by selecting "Log" and then selecting "Stop" in the dropdown, as shown in Figure 21:

![Untitled--21-.png](https://www.rapid7.com/cdn/images/bltebb71cca1cbb3aca/683deae22cfe32490adc1978/Untitled--21-.png)

Once logging is stopped, you can open the captured log file and review the contents. During the Defcon IoT Village exercise, we had the participants search for the keyword "failsafe" in the captured logs. Searching for failsafe should take you to the log entry containing the line:

  * "Press the [f] key and hit [enter] to enter failsafe mode"



This is a prompt that allows you to hit the "f" key followed by return to boot the system into single-user mode. You won't find this mode on all IoT devices, but you will find it on some, like in this case with the LUMA device. Single-user mode will start the system up with limited functionality and is often used for conducting maintenance on an operating system — and, yes, this is root-level access to the device, but with none of the critical system function running that would allow network service, USB access, and applications that are run as part of the device's normal operation features. Our goal later is to use this access and the following data to eventually gain full running system root access.

There is also another critical piece of data in the log file just shortly after the failsafe mode prompt, which we need to note. Approximately 8 lines below failsafe prompt, there is a reference to “rootfs_data" as shown in Figure 22:

![Untitled--22-.png](https://www.rapid7.com/cdn/images/blt296bfb76d19a005e/683deae465b8ea0a5bcc8fd1/Untitled--22-.png)

The piece of data we need from this line is the [Unsorted Block Image File System (UBIFS)](https://en.wikipedia.org/wiki/UBIFS) device number and the volume number. This will let us properly mount the rootfs_data partition later. With the LUMA, we found this to be one of the two following values.

  * Device 0, volume 2
  * Device 0, volume 3



## Boot into single-user mode

Now that the captured logs have been reviewed, allowing us to identify the failsafe mode and the UBIFS mount data. The next step is to reboot the system into single-user mode, so we can work on getting full root access to the devices. To do this, you'll need to monitor the system booting up in the UART console, watching for the failsafe mode prompt as shown below in Figure 23:

![Untitled--23-.png](https://www.rapid7.com/cdn/images/bltb7ccdf61754d8693/683deae6abf2ad9c2d3c46ee/Untitled--23-.png)

When this prompt shows up, you will only have a couple of seconds to press the “f" key followed by the return key to get the system to launch into single-user root access mode. If you miss this, you'll need to reboot and start over. If you're successful, the UART console should show the following prompt (Figure 24):

![Untitled--24-.png](https://www.rapid7.com/cdn/images/bltc1a93b33ed16881e/683deae870aa95be15fe32eb/Untitled--24-.png)

In single-user mode, you'll have root access, although most of the partitions, applications, networks, and associated functions will not be loaded or running. Our goal will be to make changes so you can boot the device up into full operation system mode and have root access.

In our fourth and final installment of this series, we'll go over how to configure user accounts, and finally, how to reboot the device and login. Check back with us next week!

  


## Article tags

  * [IoT](/blog/tag/iot-security-news/)
  * [Research](/blog/tag/research/)