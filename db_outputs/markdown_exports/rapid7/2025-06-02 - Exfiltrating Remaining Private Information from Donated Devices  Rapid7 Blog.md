# Exfiltrating Remaining Private Information from Donated Devices | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/03/19/buy-one-device-get-data-free-private-information-remains-on-donated-devices/
- **Date :** 2025-06-02

---

When you have old computers, flash drives, phones, or hard drives that you no longer use, you might take them to a resale shop, thrift store, or recycling center. However, have you ever wondered what happens to these devices and the data within them? Does your data get destroyed, or are your items resold with all your memories and personal data perfectly packaged up for the new owner to access? And, if that data _is_ still available, what happens when someone like me starts shopping at all the thrift stores and resale shops in my area with the sole purpose of seeing how much personal data I can get my hands on?

To find out, I spent six months extracting all the data I could from devices available at businesses that sell refurbished computers or accept donated items to sell after supposedly wiping them. By the end of this experiment, this research revealed that many businesses do not follow through on their guarantee to wipe the data from the devices people hand over to them.

Let’s take a look at how I conducted this experiment, the types of data I discovered, and some methods to ensure all data is safely removed from all your old devices before they leave your possession.

## The process

My first step was probably the least interesting part of this experiment: I researched all the businesses that sold refurbished, donated, or used computers around my home in Wisconsin. I visited a total of 31 businesses and bought whatever I could get my hands on for a grand total of around $600. Here is a breakdown of all the devices I purchased:

Device Type| Number of Devices Bought  
---|---  
Desktop or laptop computer| 41  
Removable media (such as flash drives and memory cards)| 27  
Hard disk| 11  
Cell phone| 6  
  
After buying the devices, I took them to my command center (a cool name for my basement) and began the data extraction process. Whenever I brought a computer back, I booted it up to see whether it was bootable and whether it required a password to log in. I wrote a [script in PowerShell](https://gist.github.com/jfrantz1-r7/edff3b7ca214695c925c5b5de6cb7618) that would run through and index all the images, documents, saved emails, and conversation histories through instant messengers. It would then zip it up nice and organized on the desktop, and I would pull it off with a USB drive (I know, you were expecting something much fancier). Only one Dell laptop had been erased properly.

With hard disks, most of them were IDE, so I used this IDE toaster to quickly download everything I could—this time, using a [Python script](https://gist.github.com/jfrantz1-r7/10e5372aab910989f5b5c64245101dee) to go through all the data and organize it. What I found was that none of the drives were encrypted, and all seemed to function properly (with the exception of one old Hitachi 20GB hard drive that had been wiped).

The cell phones I bought were very old and required three proprietary chargers I had to buy on eBay, putting my total cost around $650 (without factoring in gas, coffee, or my family’s road trip misery). The cell phones didn’t require PINs, and for a few of them, I couldn’t find software to interface with my computer to pull anything off.

I simply plugged in flash drives and memory cards and used that Python script again to organize the data.

Overall, what I found was astounding: Out of the 85 devices I purchased, only two (the Dell laptop and Hitachi hard drive) were erased properly. Additionally, only three of the devices were encrypted.

## The data

Armed with a bunch of data and a basement littered with technology older than myself, I developed a plan to sift through all this data for potentially private information. I used [pyocr](https://gitlab.gnome.org/World/OpenPaperwork/pyocr) to try to identify Social Security numbers, dates of birth, credit card numbers, and phone numbers on images and PDFs. I then used PowerShell to go through all documents, emails, and text files for the same information. You can find the regular expressions I used to identify the personal information [here](https://gist.github.com/jfrantz1-r7/a099416b00f36bf7fd2f9d1a90d23621).

Despite the fact that OCR is not 100% accurate and there could have been data I couldn’t extract from images by themselves or within PDFs, I can verify that the regular expressions used for Social Security numbers, credit cards, dates of birth, and driver’s license numbers were fairly comprehensive.

Below are the final counts on processed data (not including several instances of MSN/AIM conversation history) and which file formats were used to calculate this. I also excluded a few file extensions (such as XML, HTML, and CSS) for brevity and relevance.

Images (JPEG, TIFF, GIF, BMP, PNG, BPG, SVG)| Documents (DOC, DOCX, PDF, CSV, TXT, RTF, ODT)| Emails (PST, MSG, DBX, EMLX)  
---|---|---  
214,019| 3,406| 148,903  
  
As you can see, many files were found. The best (or worst) part about this is that I extracted a lot of personally identifiable information (PII). Here is the breakdown of unique values for every set:

Type of PII| Unique Value  
---|---  
Email address| 611  
Date of birth| 50  
SSN| 41  
Credit card number| 19  
Driver’s license number| 6  
Passport number| 2  
  
Surprisingly, most of the credit card numbers were from scans or images of the front and/or back of the card. The two passport numbers were also scanned into the computer.

## The price

Researching further, I realized just how cheap it is to buy people’s information on the Darknet. Social Security numbers only fetch around $1 apiece, while full documents (dox) fetch around $3 each. No matter how we calculate the value of the data gathered, we would never recoup our initial investment of around $600.

This raises a fascinating point: [Data leakage](/fundamentals/what-is-data-leakage/)/extraction is so common that it has driven down the cost of the data itself. I saw several dumps of Social Security numbers on the Darknet for even less than $1 each.

## How to safely dispose of your technology

When donating or selling your technology, you should be sure to wipe it yourself rather than relying on the seller to do it for you. There are [several great guides](https://www.greenbot.com/article/2451612/how-to-properly-and-securely-erase-your-android-device.html) available for wiping your computers, phones, and tablets, so we won’t dive too deep into that topic here.

However, if you are planning on recycling your technology, the following are some ways to make sure your data is irretrievable by destroying the device (or storage disk) irrevocably:

  * Hammer
  * Incineration (be careful of toxic by-products)
  * Industrial shredding
  * Drill/drill press
  * Acid
  * Electrolysis
  * Microwaves
  * Thermite



If using any of these methods, you’re going to need to secure your location and wear reasonable safety gear (at a minimum, appropriate goggles and gloves). Once your safety situation is handled, secure destruction can be loads of fun.

Below is one video that shows how to use thermite to destroy a desktop PC:

Realistically, unless you physically destroy a device, forensic experts can potentially extract data from it. If you’re worried about potential data exfiltration, it’s best to err on the side of caution and destroy it. However, wiping your device is usually enough, and can be a very easy and relatively painless process using the guides above.

All kidding aside, if you’re looking to wipe a hard disk drive, DBAN is your best option, and there is a very handy guide [here](https://www.lifewire.com/how-to-erase-a-hard-drive-using-dban-2619148) on how to do that. Please note that this will not work for solid-state drives for RAID arrays. If you’re looking to wipe solid-state drives or multiple disks in a RAID, PartedMagic works really well, and there is an easy-to-follow guide [here](https://linhost.info/2010/06/parted-magic-erase-a-hard-drive/).

## In conclusion

If you’re worried about your data ending up in the wrong person’s hands, destroy the data. If you wish to do a good deed and donate your technology so others can benefit, make sure it’s at least wiped to an acceptable standard. Even if you get it in writing that your data will be erased, there’s no good way to know whether that’s actually true unless you perform the wipe yourself. If this research was any indication, it likely isn’t being wiped in a reasonably secure way.

Thanks for reading, and be sure to leave any feedback below in the comments!

## Article tags

  * [Research](/blog/tag/research/)