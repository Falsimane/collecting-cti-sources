# PlugX worm disinfection campaign feedbacks

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/plugx-worm-disinfection-campaign-feedbacks
- **Date :** 2024-12-26

---

In September 2023, **we successfully took ownership of one of the IP addresses used by the PlugX worm** —a variant of PlugX associated with Mustang Panda, which possesses worming capabilities by infecting flash drives. Following this success, we studied the inner workings of this malware to determine whether there was any possibility, by using the access we had gained, to disinfect the thousands of computers making requests to our sinkhole every second.

This research resulted in a [**blog post**](/blog/unplugging-plugx-sinkholing-the-plugx-usb-worm-botnet) and a [**talk at BotConf 2024**](https://www.youtube.com/watch?v=oega_kLTch0), where Charles Meslay and Félix Aimé shared their findings and **two disinfection methods that can be used to remotely clean infected workstations**. The first method involved sending a simple and reliable self-delete command to the compromised workstation. The second method was more intrusive, as it aimed to send and execute specific code to remove PlugX from the workstation and from any connected flash drives, if present.

We concluded our blog post with **a call to national CERTs and law enforcement agencies (LEAs) to contact us if they wished to disinfect systems within their countries** , promoting the **concept of sovereign disinfection** and addressing the legal aspects associated with such operations.

Following this call, and with the support of the **Paris Public Prosecutor's Office** and the **French Gendarmerie National Cyber Unit** , **more than twenty countries responded** , pushing us to move from theory to practice. This blogpost aims at showing how it has been done, what we have developped for that and the limits of such process.

## From theory to practice

Creating a disinfection process is somewhat more complex than setting up a simple sinkhole. In our case, **we wanted each country to have the ability to disinfect specific assets**. Therefore, within one week, we developed an ergonomic interface that allows any country to log in, access statistics on compromised assets (via both an API and a graphical user interface), and send a list of the assets to be disinfected.

![PlugXworm disinfection portal home page created by Sekoia Threat Detection & Research team.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a57fa49553afbaf43c98_6a92a21e6017750314a497d7_6a2a7eb8b7c63a873a2ab60d.webp)

PlugXworm disinfection portal home page created by Sekoia Threat Detection & Research team.

Since each IP address reaching the sinkholed C2 was automatically enriched with its country, autonomous system, and CIDR from the beginning of the sinkholing operation, **we were able to easily show each participant the compromised autonomous systems and IP addresses within their respective countries**.

Once this information was in hand, participants in the operation simply had to select specific autonomous systems or, more precisely, provide the application with a CIDR block or an IP address to disinfect in order to start the process. Additionally, we provided countries with the option **to activate a country-wide disinfection operation by simply checking a few checkboxes and pressing a button**.

![PlugXworm disinfection portal in images. This portal was created by Sekoia Threat Detection & Research team.](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a580a49553afbaf43c9c_6a92a21f65cc84bc266e8267_6a2a7eb8b7c63a873a2ab610.webp)

PlugXworm disinfection portal in images. This portal was created by Sekoia Threat Detection & Research team.

Since all participants wanted to prevent any side effects, **only the first method of disinfection was used during the campaign**. Therefore, technically speaking, the process was straightforward: if an IP address met one of the rules set by the operators, the sinkhole would respond with our disinfection payload, which consisted of just a few bytes. It would also save in a database which IP address received the payload, along with the rule it followed and the associated timestamp.

## PlugX worm disinfection campaign results

This disinfection campaign was the first of its kind for us—a proof of concept for **sovereign disinfection**. It enabled us to collaborate actively with various foreign authorities, most of the time under the supervision of the Paris Public Prosecutor's Office and the French Gendarmerie National Cyber Unit, ensuring reliable and trusted communication with all participants.

At the end of the campaign, **34 countries requested simple sinkhole logs** to identify which networks were compromised, **22 countries expressed interest in the disinfection process** , and we were able to establish **a legal framework and conduct disinfection operations for 10 countries**.

In total, **59,475 disinfection payloads were sent during the campaign, targeting 5,539 IP addresses** , sometimes hundreds of times to a single IP address (probably related to VPN exit nodes or SAT links). The relatively small number of IP addresses receiving the payloads is not surprising, as the countries requesting disinfection were not the most infected ones and some countries added only specific autonomous systems and/or IP addresses.

## Conclusion

Beyond the purely technical aspect, this disinfection campaign presented several legal limitations, which were already detailed in our first blog post. **It would have been impossible to carry out this campaign within a legal framework without the involvement of the Paris Public Prosecutor's Office and the French Gendarmerie National Cyber Unit.**

We remain available to any public or private entity interested in **discussing the technical aspects of this operation in greater detail, including sharing the source code** used for the disinfection portal/process.