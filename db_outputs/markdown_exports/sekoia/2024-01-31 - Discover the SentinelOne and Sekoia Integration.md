# Discover the SentinelOne and Sekoia Integration

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/sentinelone-and-sekoia-io-integration
- **Date :** 2024-01-31

---

Expanding tech stack and increasing number of tools urge security operations teams to seek a one-stop solution for centralizing events and alerts.

Under these conditions of growing risks, the Sekoia SOC platform becomes a silver-bullet solution for backing up SOC teams. It serves as a control tower for cybersecurity and easily collects, correlates, and analyzes events and alerts from all over the information system. 

Sekoia.io offers [300+ integrations](/integrations) with our SOC platform. In this blog post, we’ll dive into integrating our platform with SentinelOne EDR solution.

## Collect SentinelOne EDR Threat and Activity events in the Sekoia SOC platform

Sekoia.io leverages SentinelOne’s management SDK to collect threat and activity events from the SentinelOne management console.

## Sekoia detection rules for SentinelOne

The Sekoia SOC platform relies on several Sigma rules that determine which SentinelOne Threat events should raise an alert in the Sekoia platform. This granularity reduces alert fatigue, enabling analysts to focus on alerts that weren’t blocked or mitigated by the SentinelOne EDR agent.

![Detection rules for SentinelOne Threat events ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a82_6a92a307e36224e46e90befc_6a2a7cc96cac9e5521dd1169.webp)

Detection rules for SentinelOne Threat events 

In addition, Sekoia.io offers specific detection rules to identify potential malicious activity on the SentinelOne management console, such as successful brute force attacks or agents being disabled from the console.

![Detection rules for SentinelOne Activity events ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a70_6a92a30832517fc40260020a_6a2a7cc96cac9e5521dd116c.webp)

Detection rules for SentinelOne Activity events 

SentinelOne events ingested in Sekoia.io are normalized to the [ECS format](https://www.elastic.co/elasticsearch/common-schema). Other detection rules from the Sekoia.io catalog can apply as well. For example, it’s possible to use the Sekoia Intelligence Feed rule to search for IoCs from Sekoia.io CTI in events. 

In the example below, a malicious code detected by SentinelOne also generated an alert raised by the Sekoia Intelligence Feed detection rule. This allows analysts to obtain more information about threats detected or blocked by the SentinelOne EDR agent. The alert contains information about a threat, campaign, and threat actor obtained from Sekoia.io CTI.

![Sekoia Intelligence Feed alert on SentinelOne Threats ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a85_6a92a30b2b0ef7af46bcd364_6a2a7cc96cac9e5521dd1177.webp)

Sekoia Intelligence Feed alert on SentinelOne Threats 

Analysts use the Sekoia platform to correlate SentinelOne Threat events with other logs collected by the platform, such as proxy, firewall, or NDR events. This approach makes it possible to retrace every step that led to the threat event.

![Graph investigation of combined events and alerts from different sources \(SentinelOne Threat event and Windows events\) ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a7c_6a92a3066568d7e2b408cfc1_6a2a7cc96cac9e5521dd1162.webp)

Graph investigation of combined events and alerts from different sources (SentinelOne Threat event and Windows events) 

Another feature of the Sekoia SOC platform is playbooks. SOC analyst launch them to remediate a threat from a SentinelOne alert. 

For instance, following an analysis of a SentinelOne alert, the analyst might deactivate the user account in Azure Active Directory. This action helps mitigate risks for user accounts with compromised credentials.

![Launching a playbook from a SentinelOne alert ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a7f_6a92a3092e47a1e9fe0dd660_6a2a7cc96cac9e5521dd116f.webp)

Launching a playbook from a SentinelOne alert 

## Ingest telemetry events in the Sekoia SOC platform

In addition to SentinelOne Threat and Activity events, it’s possible to ingest telemetry events in our SOC platform using SentinelOne Cloud Funnel 2.0. Telemetry events are activities captured by the SentinelOne EDR agent, such as process execution, network connections, DNS resolutions, and registry actions, even though the SentinelOne EDR agent triggers no threat events for them.

_Check our_[ _public documentation_](https://docs.sekoia.com/xdr/features/collect/integrations/endpoint/sentinelone_cloudfunnel2.0/) _to find more integration configuration details._

These events are beneficial to extend the detection capabilities using Sekoia. Sigma detection rules. More than 250 rules are currently available and compatible with this integration. 

The Sekoia Intelligence Feed rule, which looks for IoCs from Sekoia CTI in events, effectively assists in detecting threats based on the SentinelOne telemetry events. The Sekoia SOC platform's automatic retrohunt capabilities look for new IoCs in past telemetry events up to 30 days before the addition of new IoCs in the Sekoia database.

![](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a73_6a92a30a693fca262e1b60eb_6a2a7cc96cac9e5521dd1172.webp)

Sekoia Intelligence Feed alert 

The example above shows that the SentinelOne EDR agent recorded a connection from an endpoint to a public IP address identified as malicious by Sekoia.io. Analysts can access all the context related to that IP address, such as malware, campaigns, and intrusion sets. 

## Automating actions in SentinelOne from Sekoia

Playbooks can be launched from alerts to automate enrichment or remediation actions. Our SOC platform has several playbook actions, which allow customers to interact with different security solutions from the platform. The documentation for these actions is available [here](https://docs.sekoia.com/xdr/features/automate/library/sentinelone/).

![Current list of playbook actions available for SentinelOne ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a76_6a92a30416f788fda8e4cf43_6a2a7cc86cac9e5521dd1142.webp)

Current list of playbook actions available for SentinelOne 

‍

Enrichment or remediation actions can help to build a playbook for isolating an endpoint with the SentinelOne EDR agent from any alert raised by the Sekoia SOC platform. 

![Playbook to isolate an endpoint using SentinelOne EDR agent ](https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6a92a5e2dc30711238340a79_6a92a30532517fc40260002c_6a2a7cc86cac9e5521dd1147.webp)

Playbook to isolate an endpoint using SentinelOne EDR agent 

In the future, the Sekoia.io team plans to add playbook actions for SentinelOne to the catalog. For example, we’ll add an action to disseminate IoCs from Sekoia to the SentinelOne management console.

## Wrapping up

We’ve overviewed different integrations between the Sekoia SOC platform and the SentinelOne EDR agent, from retrieval of threat events to task automation. 

The partnership between SentinelOne and Sekoia.io is another milestone in building new integrations that bring more value to clients by combining the best cybersecurity solutions.