# Building a Backpack Hypervisor | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2017/09/29/building-a-backpack-hypervisor/
- **Date :** 2025-06-02

---

![](https://lh6.googleusercontent.com/PW950OD-Lm-mzuPkLAstCd7GOieLvoseK-Ej9_xo2j30l9NzYWWs9DdDbBVzhYFh_q-E4rtP9_JeIQjH9jGovVglb52mMkuBMC6H8-u4YavVwFoKueInmrxlqSFzcP2MuOZoY3wY)

Before I came to work for Rapid7 as a researcher and engineer, I was a developer, hacker, and technical trainer. Back then, I travelled across the country (and globe) to teach hacking, defense, and/or security tool development classes. Teaching those courses required access to targets and networks, so I almost always travelled with a powerful ESXi server. The ESXi server was contained in an 8-U portable rack and weighed around 200 pounds.

Since most of my teaching engagements were solo, I had to handle the logistics myself. Loading the mobile rack into SUVs and minivans, to be blunt, sucked. Those who travel will no doubt appreciate the problem of an expensive server that's too large to move easily, has no backup for hundreds of miles, and does not support full disk encryption.

The server contained targets, networks, and miscellaneous data that represented a large investment in development time. Because of its size, I could not easily pack it up at the end of the day and bring it back to the hotel where I could make sure it was safe. I had to trust our customers, shippers, and third-party sites to maintain security for our intellectual property, and protect the equipment from damage.

During my time as an instructor, I was sometimes assigned classrooms without locks. Equipment would sometimes arrive damaged because a forklift operator speared the shipping crate and did not bother to report it. In later engagements, we removed hard drives at the end of the day to at least protect the data. But juggling and jostling hard drives can create problems as well, and it only solves some security issues.

In short, the server itself was a logistical nightmare that relied on large, able-bodied instructors with little consideration for their backs. It created existential risks to the engagement and numerous security problems that all could have been fixed had we been able to more easily maintain physical possession of the server.

![](https://lh6.googleusercontent.com/0PtNeBLTKYuBNlgn_vuQk9Jw9-R5WO-XaWaH0dnf8bnEneBlTqJrNKukgH78hKUNIHEOsMWnhfb4S97hgXg-A74iWglMbLoGfWjU1ogsdjWXOlpGVJoKnU9cOWP6tRMoeCI5hpgN)

Back then, a fellow instructor and I pondered if we could build a miniaturized version of the server that was powerful enough to run a course, but small enough to maintain physical possession throughout a trip. It would need to be small enough to bring as a carry-on on a flight, and ideally be under the OSHA fifty-pound weight limit. 

Our first failed attempt was in 2013; technology and budget were a problem. A six-core AMD FX chip in a short 2-U server chassis with one SSD was simply unable to keep up with the demands of the course. The changes we made to the course to accommodate the server were, as my friends say, _suboptimal._ After that experience, we shelved the idea for a carry-on ESXi server. Soon after, we both found ourselves freelancing, and the idea of a carry-on hypervisor became even more compelling.

Before long, I became a remote employee at Rapid7. Rather than relying solely on the bandwidth of the company VPN, I decided to build my own research range at home. It would need to provide me as a researcher much the same capability that I needed as an instructor—but instead of being designed to let students bang on virtual machines, this time it would be for my own needs. 

At Rapid7, I am no longer traveling for teaching engagements, so size is not as important as it used to be; on the other hand, having moved from DC to Texas, I no longer have a creepy basement to use for large-loud-thing storage. So my server would need to be civilized, quiet, and unobtrusive; in other words, the server needed to be spouse-friendly. It required some planning, but I was relatively pleased with the results in function, size, and appearance. This is my experience.

### Goals

ESXi servers can vary greatly, and so I mapped the needs I saw for my purposes as an instructor. I figured each student would need:

  * Development Windows Machine (2 GB RAM)
  * Development Linux Machine (2 GB RAM)
  * 1-2 GHz of CPU power (12-24GHz total)
  * 60 GB Disk Space (720 GB Total)
  * No more than 4 students per mechanical disk or 6 per SSD
  * In addition to that, I'd need about 16 GB of RAM for targets and infrastructure
  * The server would need a multi-port Intel NIC so we could do multiple physical and virtual networks.
  * Financial goal: < $1500
  * Size goal: Must go in a carry-on. Laptop bag preferred, but small roller bag acceptable.



### Why not a workstation laptop?

You might be asking this question, and it is a valid one. Based on my experience using higher-end laptops at my previous job, I knew using a workstation laptop might be an option (though admittedly a very expensive one). When I left my job as a trainer and accepted a job with Rapid7, they gave me a swanky i7 laptop with 32 GB of RAM, and I was super excited because it was on par with some ESXi servers I’ve used in the classroom. Up to this point, my limiting factor on laptops was RAM; anytime I tried to push the laptop, I ran out of RAM almost immediately.

The laptop Rapid7 gave me had a lot of RAM, so I thought it might negate my need for a research range—but as it turns out, I was wrong. My work machine has a lot of RAM that helps when running resource-intensive VMs like my developer VMs, but it bogs down quickly in CPU performance when I spin up more than six or so lower-resource VMs like targets. I don’t think the laptop form factor can handle the heat generated by the CPU under full load, so it throttles the processor after a few seconds at full speed. (The laptop Rapid7 gave me is also way over my personal budget and requires more effort to upgrade!)

There are laptops out now that have twice the RAM but still have comparatively slow, low core-count processors and cost over $3000 when configured. Add into the mix that you tend to get one NIC on a laptop, and laptop hardware in general is a complete gamble when it comes to support in hypervisors. Based on that, I really wanted to avoid high-end laptops, but I have used them in the past for smaller engagements, and if that’s all you need and you have the budget, I think it is a great option.

### Build

![](https://lh3.googleusercontent.com/74aodMcC6Bo5sVkmonMcDvyrUEgFJTYy2J1luhEfC5z9BN5k0s9UDlyWPWFe1k9uhaBBrGRHJVlCnGZAoooYVKJ2JQv99hhM48rI0BIsoTRdTS8VSiYAhS79EUCNRf--AQmCl9R9) ![](https://lh5.googleusercontent.com/e3CNR9iGtiBplLFyRMBIrCT0OI9nNMbzL5n8kzGrRrYuMq-Q-T0IVWEHDnrfzEY3EkBEgoRkFimqeqRehE4-Q5LRhmhxQYx4bs-5uJEqBNbgIMZ-IYhWsY1AVorQiSNhBvp0eckP)

In the spirit of the completed photo first, here is the component list:

Item| Name| Link| Then| Now  
---|---|---|---|---  
CPU| Intel i7 6800K| [Microcenter]| 330| 330  
Motherboard| GA-X99-Gaming5| <http://www.gigabyte.com/Motherboard/GA-X99M-Gaming-5-rev-10#ov>| 100| 100  
Fan| Cooler Master GeminII M4| <https://www.amazon.com/gp/product/B0080ATR2Y>| 34| 34  
Case| IN-WIN Desktop Case Cases CE685.FH300TB3| <https://www.amazon.com/gp/product/B00J8LZDSG>| 70| 70  
SSD1| Samsung 850 EVO| <https://www.amazon.com/Samsung-2-5-Inch-Internal-MZ-75E1T0B-AM/dp/B00OBRFFAS>| 300| 330  
nvme| Samsung 960 EVO Series - 250GB PCIe NVMe| <https://www.amazon.com/gp/product/B01LYFKX41>| 127| 127  
SSD Enclosure| Max 2504 4-Bay Hot Swap Mobile Rack/Enclosure | <https://www.amazon.com/gp/product/B01N3KUQ22>| 43| 43  
Memory (x2)| Ballistix Sport LT 32GB Kit (16GBx2) DDR4 2400 | [https://www.amazon.com/Ballistix-Sport-4GBx2-PC4-19200-288-Pin/dp/B01EIJFQCK2&keywords=DDR4&th=1](https://www.amazon.com/Ballistix-Sport-4GBx2-PC4-19200-288-Pin/dp/B01EIJFQCK2&keywords=DDR4&th=1)| 436| 500  
Network Card| Intel T350| ebay…..| 60| 60  
Total| | | 1500| 1594  
  
### Choices

Some of you might wonder why I chose one component over another, so here are some quick explanations. Keep in mind these are simply my personal preferences and decisions.

#### CPU

For the CPU, I chose an Intel i7 6800K. I think the most important factor in the decision was that the 6800K supports 128 GB of RAM followed by a close second of the performance/price ratio.

Many people might think this was the perfect opportunity to use Ryzen. To be honest, I simply did not consider a Ryzen chip because of recent experience with AMD. Several years ago, I took a chance on the FX line from AMD. The hype said they’d made a chip with twice the cores as Intel, and they were competitive again, just like when they had the original Athlons! From my experience, the FX chips didn't live up to the hype. I always found myself deploying an Intel-based computer if I had one to spare rather than an AMD-based computer if performance was a requirement. Now, when I hear Ryzen is AMD’s new ‘Athlon,’ I’m just ignoring it until someone else takes the chance. They may be great, but I’ve already been disappointed by the ‘next Athlon!’

A second reason I went with Broadwell-E series specifically is that I’ve got an awesome i7 2600K I bought nearly five years ago. I use it to check email and surf the web. The chip is still a contender for speed, even if it does use a lot of power, and if it supported 64 GB of RAM, this section would be over already and I’d just use that chip and save $500. Unfortunately, it is limited to 32 GB of RAM, and that’s just not enough to make it as a server for me. I’m concerned that if I went with a Ryzen or Kaby Lake, I’d hit that same feeling again in 5 years since they are both limited to 64 GB of RAM.

To be honest, the Broadwell-E has a lot going against it. This is the last chip with the 2011-v3 socket, so no new motherboards are going to come out and the power requirement is higher. In the end, I settled on comparing the Kaby Lake 7700K to the Broadwell-E 6800K. I could probably make an entire blog post only on that choice, but not everyone gets as excited as I do about bus lines and all, so a brief overview was that the 7700 was $300, 4.2 GHz, and 4 cores, while the 6800K was $330, 3.4 GHz and 6 cores. For performance, it was ~17 GHZ on a newer architecture vs ~20 on an older architecture. Those numbers are about even in my opinion. If you buy into Intel's logical cores, that gap doubles through the magic of hyperthreading, though I’m not sure exactly how much faith I put in hyperthreading, personaly.

The 6800K gave a slight advantage in performance, and, arguably, with more cores it would split up highly parallelizable tasks better. Most importantly, it supported twice the RAM should I ever choose to upgrade. If I had gone with the 6800K, I would not have had another great chip sent to early retirement because of upgrade constraints. The Kaby Lake chip did edge out on being lower power and a newer chipset, plus the motherboards were way cheaper so I’d certainly not argue it is a bad choice.

#### Case

Since I wanted this to fit into a backpack, I needed a small form-factor case. On a few previous builds where size was a factor, I was a huge fan of this case: <https://www.amazon.com/gp/product/B00J8LZDSG>. It is an mATX case with a 300 watt power supply for about $70. It is a well-built tool-less case that you can work in without feeling like you’ve stuck your hand in razor wire. The case measures 4x13x15, which is small when you’re talking about a server—and sadly, I have to admit I really like that it fits perfectly in an Ikea Kallax shelf. (Married life is a threat to server racks!)

![](https://lh5.googleusercontent.com/E6-rS-cqcEmLJKa-862x5V8BEADBGXE5jK0K_1Fa9FMIPijOSDvxgBZHVPTTEyWkEBf5V3rRmIGIKQJQGs4Rsz-q_UiW98egupRVMjvHZJ1IjjIN5MxSOPses4ZT3UYR5KvAi7eV)

#### Memory

Memory is easy. I buy Crucial. I have had too many bad experiences and horrible troubleshooting woes to take a chance on any other brand. The motherboard was red, so I bought red Crucial RAM. (Red RAM! Red RAM! Over here!) The mATX motherboard only supports 64 GB, but that’s plenty for now, and I have the peace of mind that I can switch to another motherboard and get 128 down the road if I want, though I might have to use a larger case.

#### CPU Fan

For a normal build this would be hardly worth mentioning, but given the constraints, this was the hardest part of the entire build. I measured the case and realized I had about 75mm from the top of the CPU to the case wall, which meant I needed a CPU cooler that was less than 60mm tall so I could have good airflow. It also needed to support the 2011-v3 server socket. Further, I wanted it to be as quiet as possible, so I wanted to stay away from the truly server-style side-fan CPU coolers. Happily, pcpartpicker.com lets you put in the height requirement for CPU coolers, and I found [this one](https://www.amazon.com/gp/product/B0080ATR2Y%22). It fits like a charm!

#### Storage

Originally, I had a 1 TB Samsung SSD and a 512 GB nvme chip sitting around doing nothing (Yeah, good problem to have, I know). I put them both in and made the nvme the boot device for ESXi. In the first week, I noticed that any VM I stored on the nvme drive would not hold a snapshot, but anything on the SSD would be fine. I have no idea why or what happened, but because I could not seem to use the storage on the nvme for VMs, I pulled it and replaced it with a 250GB nvme and another 512 SSD. Now, the only thing on the nvme is the OS. It's on my to-do list to see if I can leverage the boot disk down to a small USB drive and pull out the nvme disk. The nvme disk is certainly overkill, but as we know, that’s the best kind of kill.

I later added another SSD to split the VMs and limit bootstorms when I launched testing scenarios. You could leave it at one or add multiple SSDs to get maximum throughput if you have high disk bandwidth requirements.

#### Network card:

There is a slight story here. Intel cards are awesome but way too expensive for my taste, so I have a habit of trying to pick up used ones on eBay. I can generally find older quad port intel cards for ~$40-$60. I found Intel T350s for $60 each, so I bought three.

When they arrived, I opened one and I was immediately suspicious. It was a quad port card that resembled a T350, but every Intel card I have ever had has sported the Intel logo. This card had nothing. I Googled “Knockoff Intel network cards” and then found out this is very common. Two of the three cards I got matched exactly the specs on knockoff Intel cards, right down to the memory chip manufacturer. One had the Intel logo and the right memory chips, so it appeared to be a completely legit Intel card. I put the real one in the server, and it works great (I’ve tried the other two on less critical infrastructure).

### The End Result

I'm very happy with the new backpack hypervisor. It really is small enough to put in my laptop bag with my laptop, though the bag does not zip completely. It fits with ease into a small roller laptop bag I have which will be my choice if I have to fly with it. Splitting the OS and VMs between multiple fast devices makes starting up VMs fast, and six cores makes it so that it can run lots of VMs and those VMs can do stuff rather than sit and idle as targets. I run automated testing scenarios now where I regularly run eight medium resource Linux VMs and more than a dozen Windows target machines, and it handles the load well. Another day on the research range!

## Article tags

  * [Research](/blog/tag/research/)