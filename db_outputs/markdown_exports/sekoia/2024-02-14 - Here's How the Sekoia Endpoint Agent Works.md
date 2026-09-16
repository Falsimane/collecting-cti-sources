# Here's How the Sekoia Endpoint Agent Works

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/how-sekoia-io-endpoint-agent-works
- **Date :** 2024-02-14

---

According to [Global Cybersecurity Outlook 2024](https://www3.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2024.pdf?_gl=1*74noej*_up*MQ..&gclid=CjwKCAiAtt2tBhBDEiwALZuhANJgJjGH5FQWdDFX9yjDCOkjiAscWNututKECWMpFn2CxMaM2FWfrBoCpqoQAvD_BwE) by WEF,**29% of organizations** reported that they had been materially affected by a cyber incident in the past 12 months. Due to increasing risks and expanded attack surface, companies seek to establish reliable cyber resilience strategies and quickly identify attack vectors. The right tools for collecting and analyzing logs, including our Endpoint Agent, may help them recognize red flags and mitigate risks. 

In this way, Endpoint Agent stays at the forefront of revealing critical deficiencies in the organization's cybersecurity posture and taking action to defend the security layer – email, endpoint, server, cloud workloads, or network. 

In this blog post, we delve deeper into:

  * How Endpoint Agent collects log data.
  * What types of events from workstations and servers Endpoint Agent can forward to Sekoia SOC platform.
  * Why our Agent may be beneficial for SOC teams aiming to protect business assets.



## Exploring Endpoint Agent functionality

To start with, **Endpoint Agent collects and sends events to Sekoia SOC platform for further analysis against detection rules**. Agent covers various event categories, including access tokens, antivirus events, authentication logs, DLL monitoring, file monitoring, and more. It’s **available at no extra cost** and helps to remediate threats, preventing sophisticated fraud and cyberattacks.

The workflow for Endpoint Agentconsists of the following steps: 

  1. Сollect events from the host. 
  2. Normalize events in the [Elastic Common Schema](https://www.elastic.co/guide/en/ecs/current/index.html) format. 
  3. Send events to the Sekoia SOC platform using the HTTPS protocol. 



Note that events are sent in bulk, serving as an entry point at which the Sekoia platform starts to detect alerts. 

![How Endpoint Agent works ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5dea49553afbaf44ef1_6a92a2fd32517fc4025ffbbf_6a2a7cdba62fe29dde505304.webp)

How Endpoint Agent works

By capturing and transmitting security-related events directly to the Sekoia platform, Endpoint Agent provides analysts with real-time telemetry data for effective threat detection and response. Compared to other log collection methods, **Endpoint Agent offers a wide range of advantages** and can standardize and save events in a format that enables full-fledged analysis. Let’s take a closer look at these advantages. 

### **Preservation of log integrity**

The Sekoia Endpoint Detection Agent prioritizes the integrity of logs collected from the operating system event log. It strictly adheres to a non-modifying approach, ensuring that **logs remain unaltered during collection**.

### Supported operating systems

The Endpoint Detection Agent supports different operating systems, including Windows 8, Windows 10, Windows 11, Windows Server 2016, Windows Server 2019, and Windows Server 2022. The support extends to 64-bit versions of both Windows and Linux. Moreover, the Sekoia team works on replenishing this list of supported operating systems.

The Agent needs only a few privileges on the system (executed in userland mode). Additionally, if the Agent can’t establish a connection with the Sekoia platform, it stores data and sends it later. 

### Simplicity, security & resource consumption

The Agent uses the HTTPS protocol to securely transmit events. Users only need to open [specific streams and URLs](https://docs.sekoia.com/xdr/features/collect/integrations/endpoint/sekoiaio/#prerequisites) for seamless communication. We also offer [tailored URLs](https://docs.sekoia.com/getting_started/regions/) to meet advanced legal or safety constraints since Sekoia is currently available in several European regions. Despite this flexibility and a large number of available settings, our Agent ensures **minimal resource utilization, with average CPU usage below 1% and RAM consumption around 50MB**. 

## **Installation process**

The initial step involves creating a dedicated intake associated with the Agent on the Sekoia SOC platform. Then, you should choose the appropriate download link for your operating system.

Optionally, you can collect additional events using Sysmon, which generates more logs, including process, registry, and driver activities. 

Finally, execute installation commands to install the Agent. Once installed, it collects, normalizes, and transmits event logs to Sekoia.

Note that if an EDR is already installed on the system, you’ll need to [fine-tune detection rules](https://docs.sekoia.com/xdr/features/collect/integrations/endpoint/sekoiaio/#installation) to avoid false positive alerts when adding the Sekoia Endpoint Agent. However, compared to EDR, **the Agent can collect and send more significant events for subsequent security analysisby the Sekoia SOC platform**. 

Find more details on installation and collected logs in our [public documentation](https://docs.sekoia.com/xdr/features/collect/integrations/endpoint/sekoiaio/#:~:text=Sekoia.io%20provides%20its%20own,events%20directly%20to%20Sekoia.io.). 

## **Configuration options**

Our Agent offers beta support for monitoring and collecting logs from specific applications, such as NGINX. Configuration involves editing a YAML file to specify log file paths and associated intake keys. In scenarios where internet access is disrupted, the Agent stores logs locally on disk. Upon reestablishing connectivity, older logs are prioritized for transmission to Sekoia. 

Other configuration options allow specifying the region during installation, enabling automatic updates, and using web proxies. Our Agent supports automatic updates by default, but this feature can be deactivated to enable manual updates. In addition, the Sekoia Agent can use a proxy server for its HTTPS requests. This proxy server acts as a gateway between the Agent and the Sekoia platform.

## **Future of Endpoint Agent**

Centralized log collection helps establish a baseline of normal system behavior and identify patterns and deviations. Therefore, as the range of events requiring attention expands, we consistently communicate with clients to identify non-standard cases and refine log collection. 

> Our agent has been created with Sekoia.io in mind, ensuring the seamless collection of all critical events essential for analysis against detection rules. We focus on ongoing collaboration with the Threat Detection & Research (TDR) team to promptly update Endpoint Agent with new events, prioritizing accuracy in log collection. Our goal is to ensure simplicity, offering a tool which works out-of-the-box, yet can be customized according to customer needs.**  
>  —Raphaël Cohen, Architect and Senior Backend Developer**

As Endpoint Agent collects events from different sources, including applications, systems, tools, and hosts, normalizing the data to follow the same format may be challenging. The Sekoia team plans to further improve Endpoint Agent in terms of data normalization and make it even more efficient in the face of emerging cybersecurity risks.