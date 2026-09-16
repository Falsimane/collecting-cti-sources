# DNS OverDoS: Are Private Endpoints Too Private?

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/
- **Date :** 2026-01-20

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [DNS](https://unit42.paloaltonetworks.com/category/dns/ "DNS")



[DNS](https://unit42.paloaltonetworks.com/category/dns/)

# DNS OverDoS: Are Private Endpoints Too Private?

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 10 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Golan Myers](https://unit42.paloaltonetworks.com/author/golan-myers/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:January 20, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
    * [DNS](https://unit42.paloaltonetworks.com/category/dns/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/)
    * [Networking](https://unit42.paloaltonetworks.com/tag/networking/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=DNS%20OverDoS:%20Are%20Private%20Endpoints%20Too%20Private?&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fdos-attacks-and-azure-private-endpoint%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdos-attacks-and-azure-private-endpoint%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdos-attacks-and-azure-private-endpoint%2F&title=DNS%20OverDoS:%20Are%20Private%20Endpoints%20Too%20Private? "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdos-attacks-and-azure-private-endpoint%2F&text=DNS%20OverDoS:%20Are%20Private%20Endpoints%20Too%20Private? "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fdos-attacks-and-azure-private-endpoint%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=DNS%20OverDoS:%20Are%20Private%20Endpoints%20Too%20Private?%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fdos-attacks-and-azure-private-endpoint%2F "Share in Mastodon")



## Executive Summary

We discovered an aspect of Azure’s [Private Endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview) architecture that could expose Azure resources to denial of service (DoS) attacks. In this article, we explore how both intentional and inadvertent acts could result in limited access to Azure resources through the Azure Private Link mechanism. We uncovered this issue while investigating irregular behavior in Azure test environments.

The risk is present in three scenarios:

  * Accidental - internal: A network administrator deploys Private Endpoints to improve network security within an Azure environment.
  * Accidental - vendor: A third-party vendor deploys Private Endpoints as part of its solution, for example to enable resource scanning by a security product.
  * Malicious - attacker: A threat actor who gained access to an Azure environment intentionally deploys Private Endpoints as part of a DoS attack.



Our research indicates that over 5% of Azure storage accounts currently operate with configurations that are subject to this DoS issue. In most environments, at least one resource in each of the following services is susceptible:

  * Key Vault
  * CosmosDB
  * Azure Container Registry (ACR)
  * Function Apps
  * OpenAI accounts



This issue has the potential to affect organizations in multiple ways. For example, denying service to storage accounts could cause [Azure Functions within FunctionApps](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) and subsequent updates to these apps to fail. In another scenario, the risk could lead to DoS to Key Vaults, resulting in a ripple effect on processes that depend on secrets within the vault.

Microsoft provides [fallback to internet](https://learn.microsoft.com/en-us/azure/dns/private-dns-fallback) advice that partially addresses this and other [known issues](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json#storage-access-constraints-for-clients-in-virtual-networks-with-private-endpoints) associated with Private Endpoints.

We discuss these issues, provide potential solutions and suggest ways that defenders can scan environments for resources that are susceptible to DoS attacks.

Palo Alto Networks customers are better protected from the threats discussed in this article through the following products:

  * [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud)



[Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is a strategic evaluation service that reviews your organization's cloud infrastructure to identify misconfigurations and security gaps, enabling teams to strengthen their posture against cloud-based threats.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | [**Microsoft Azure**](https://unit42.paloaltonetworks.com/tag/microsoft-azure/)**,**[**Cloud Research**](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)  
---|---  
  
## Azure Private Link Key Components, Concepts and Flows

As part of Azure’s networking offering, Microsoft created [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview). This mechanism offers a private, secure way to connect to supported Azure resources and Azure-hosted custom services using Azure’s backbone network.

### Definitions

To understand the solution and the secure connection process of resources using it, let’s first define the key components and concepts.

  * **Service** : Destination to which a connection is made
  * **Private Link** : Azure implementation that allows and handles the connections
  * **Private Endpoint** : A network interface within a customer’s virtual network that allows connectivity to the service
  * **Private DNS zone** : The default Domain Name System (DNS) service that is used with Private Endpoints
  * **Virtual network link** : The link created by default between a Private DNS zone and a virtual network
  * **DNS A record** : A DNS record that maps a domain or hostname to an IP address
  * **Network ACL** : Network access control lists (ACLs) define rules that allow or restrict traffic to a service, separate from the Private Link solution



Azure resources expose public endpoints by default. These endpoints resolve through standard DNS infrastructure — either public Azure DNS, or customer-managed DNS resolvers. When a client queries a service name such as mystorageaccount.blob.core.windows[.]net, the DNS resolver returns a public IP address owned by Microsoft. The IP address allows connectivity over the public internet or Azure service endpoints, depending on the network access controls that are applied.

When Azure Private Link is introduced, DNS resolution behavior changes. A Private DNS zone — for example, privatelink.blob.core.windows[.]net — can be linked to one or more virtual networks. If a virtual network has a link to a Private DNS zone for a given service type, Azure’s DNS resolution logic prioritizes that zone when resolving matching service names. If a matching record exists, the name resolves to the private IP address of the Private Endpoint, instead of the public endpoint.

Organizations commonly deploy one of the following architectures:

  * **Public-only architecture:** Resources are accessed using their public endpoints and standard DNS resolution. Network ACLs, firewalls or service endpoints restrict access.
  * **Private-only architecture:** All access to the resource occurs through Private Endpoints. Public network access is disabled, and DNS resolution is fully controlled through Private DNS zones.
  * **Hybrid architecture (public and private):** Some virtual networks or workloads access the resource through Private Endpoints, while others continue using the public endpoint. This model is frequently used during migrations, phased rollouts, third-party integrations, or shared service environments.



We use the example of storage accounts to demonstrate how Private Endpoints are used in Azure networking. However, the same concepts apply to any Private Link-supported service. By default, when a network administrator or a user with appropriate Azure Role-Based Access Control (RBAC) permissions creates a Private Endpoint linked to a resource, a Private DNS zone is created with a virtual network link to the same virtual network as the Private Endpoint.

The DNS zone’s name has a predetermined structure that is based on the [Private Endpoint’s destination service](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) (e.g., privatelink.blob.core.windows[.]net for blob storage). Additionally, an A record is created in the DNS zone, linking the name of the destination resource and the IP address of the Private Endpoint.

There are two ways to connect between a virtual machine VM and a storage account with a Network ACL:

  * Without a Private Endpoint (using public or service endpoints)
  * With a Private Endpoint



### Connection Flows

Figure 1 shows how a connection is made to a resource that does not use the Private Link solution.

![Diagram showing network architecture with four main components: VNET1 containing VM1, connected to a DNS Resolver and a Storage Account with a Network ACL listing two rules: 1. Allow VNET1, 2. Deny *. The connections are numbered to indicate the flow of interaction.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/2641_Azure-Private-Endpoints-Figures-3.png)Figure 1. Connection flow without the Private Link solution.

The flow in this case is as follows:

  1. When trying to access the storage account, the VM attempts to resolve the account’s name to an IP address. This usually occurs through an external DNS resolver, and the traffic traverses the public internet.
  2. If the resolver has a record for the storage account, it returns the corresponding IP address.
  3. Once the address is obtained, the VM tries to connect to the storage account.
  4. The storage account then evaluates the virtual machine’s IP address against its Network ACL. If the connection is allowed, the storage account responds with the requested information.



Figure 2 shows how the same connection is made when a Private Endpoint is used.

![Diagram showing network communication within Azure. VNET1 connects to a VM1 and a Private DNS Zone labeled as "privatelink.blob.core.windows.net." A Private Endpoint interacts between VM1 and a Storage Account, illustrating the flow of data marked with numbers 1 to 6, indicating the sequence of communication.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/2-2641_Azure-Private-Endpoints-Figures-4.png)Figure 2. Connection flow with the Private Link solution.

  1. Initially, the VM attempts to resolve the account’s name to an IP address. If a virtual network link exists in the virtual network (VNET) to a Private DNS zone that points to a Private Link service, Azure’s Private Link mechanism forces resolution using the Private DNS zone. This occurs when the connection is to a Private Link service of the same type (e.g., blob storage).
  2. When the DNS resolver identifies a matching A record, it provides the VM with the corresponding IP address.
  3. The VM then connects to the IP address, which belongs to the Private Endpoint.
  4. The Private Endpoint acts as a network interface for the storage account, evaluating the traffic and then forwarding it to the storage account.
  5. The storage account evaluates the request and supplies a response through the Private Link solution.
  6. The response is presented to the VM, which essentially accesses the storage account using Azure’s backbone network.



## Potential Private Link DNS Dangers

As outlined above, interactions with a Private Link service from a virtual network configured with a Private DNS zone for that service type are forced to resolve through the Private DNS zone.

Consider an environment where VM1 in VNET1 successfully accesses a storage account using its public endpoint. DNS resolution occurs through the default public DNS infrastructure, and access is permitted by the storage account’s Network ACLs. At this stage, the workload is operating normally.

Later, a Private Endpoint is created for the storage account in VNET2 — either intentionally, accidentally, or by a third-party deployment. As part of this process, a Private DNS zone for blob storage (privatelink.blob.core.windows[.]net) is linked to VNET1 or shared across virtual networks.

Once this DNS zone is linked, Azure’s DNS resolution logic forces all blob storage name resolution in VNET1 through the Private DNS zone. However, because no “A” record exists in the zone for the storage account within the context of VNET1, DNS resolution fails. VM1 can no longer resolve the storage account hostname and is unable to connect — even though the public endpoint remains accessible and unchanged.

This configuration change effectively creates a denial-of-service condition for workloads in VNET1 that previously functioned correctly. The outage is triggered solely by a DNS resolution side effect introduced by the Private Link configuration, without any change to the target resource itself.

Figure 3 demonstrates this example.

![Diagram showing two virtual networks, VNET1 and VNET2, connected by a storage account. VNET1 includes a VM1 and a private DNS zone. The storage account is positioned between both networks. This setup may result in failed connections, as indicated by red crosses on paths from VM1 to the storage account. VNET2 contains a private DNS zone and a linked private endpoint.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/3-2641_Azure-Private-Endpoints-Figures-5.png)Figure 3. Potential issue caused by using the Private Link solution.

The figure above shows that VM1 attempts to connect to the storage account. This storage account has a Private Endpoint in VNET2 and does not have a Private Endpoint in VNET1. Hypothetically, VM1 could try to connect using the storage account’s public endpoint. This would work if the VM’s virtual network did not have a Private DNS zone resolving to the same resource type. In this case, however, the Private DNS zone and the service are Private Link registered, so Private Link forces resolution through the Private DNS zone.

The process shown in Figure 3 occurs as follows:

  1. Private Link recognizes the blob storage Private DNS zone in VNET1 and identifies that the storage account is Private Link registered. Private Link forces DNS resolution through the Private DNS zone.
  2. The configuration in Figure 3 shows that no record was created for the storage account in the Private DNS zone linked to VNET1. As such, the virtual machine cannot resolve the service.
  3. Due to the DNS resolution issue in step 2, the subsequent steps – in which VM1 sends a request to the storage account and receives a response from it – do not occur.



This scenario causes a partial denial of service: any resource in VNET1 that tries to access the storage account will not be able to.

This risk can also be present when using local DNS resolvers, depending on the configurations and the records added. Additionally, although our example relates specifically to blob storage, any service that supports [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/availability) is potentially at risk.

## Mitigations and Recommendations

Azure Private Link was originally intended as a binary solution, to be either fully enabled, or disabled. When the service is implemented as intended, users can only access resources that use Private Link through those resources' Private Endpoints. This approach eliminates the need to use a combination of private, public and service endpoints. However, as over 5% of Azure storage accounts are configured in a way that is subject to this issue, we recognize the need to provide solutions that address the risks introduced by these implementations.

### Mitigations

Microsoft acknowledges that the binary nature of the solution is a known issue and mentions it in [their documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json#storage-access-constraints-for-clients-in-virtual-networks-with-private-endpoints). Microsoft also provides a partial solution: enabling a [fallback to internet](https://learn.microsoft.com/en-us/azure/dns/private-dns-fallback) option when creating a virtual network link. Using this fallback solution, when the DNS Resolver cannot find a record that matches the requested service, it falls back to the public internet. While this solution solves the issue, it does not necessarily match the main concept of Azure Private Link, which is to traverse Azure’s backbone network rather than the public internet.

A second, partial solution is to manually add a record for the affected resource in the necessary Private DNS zone. This option is less appropriate for large production environments, as it creates additional operational overhead.

Although neither fallback nor manually adding a record is a definitive solution, combining the above approaches with comprehensive discovery will help with mapping, finding and remediating affected configurations.

### Comprehensive Discovery and Scanning

There are two ways to scan and identify resources that are potentially at risk:

  1. Scanning for resources with each service individually
  2. Using [Azure Resource Graph Explorer](https://learn.microsoft.com/en-us/azure/governance/resource-graph/)



The second scanning method is more efficient and can easily be modified to match most resource types. We created a graph query that retrieves a list of all the virtual networks in the environment that are linked to a blob storage Private DNS zone (privatelink.blob.core.windows[.]net). These virtual networks are forced to resolve blob storage resources through their Private Endpoints when communicating with Private Link registered resources.

resources | where type == "microsoft.network/privatednszones/virtualnetworklinks" | extend zone = tostring(split(id, "/virtualNetworkLinks")[0]), vnetId = tostring(properties.virtualNetwork.id) | join kind=inner ( resources | where type == "microsoft.network/privatednszones" | where name == "privatelink.blob.core.windows.net" | project zoneId = id ) on $left.zone == $right.zoneId | project vnetId

123456789101112 | resources| where type == "microsoft.network/privatednszones/virtualnetworklinks"| extend  zone = tostring(split(id, "/virtualNetworkLinks")[0]), vnetId = tostring(properties.virtualNetwork.id)| join kind=inner ( resources | where type == "microsoft.network/privatednszones" | where name == "privatelink.blob.core.windows.net" | project zoneId = id) on $left.zone == $right.zoneId| project vnetId  
---|---  
  
In addition, it is important to identify which virtual networks interact with blob storage resources that do not have Private Endpoint connections. We created the following query for this purpose. This query retrieves storage accounts that allow access to their public endpoint and do not have a Private Endpoint connection.

Resources | where type == "microsoft.storage/storageaccounts" | extend publicNetworkAccess = properties.publicNetworkAccess | extend defaultAction = properties.networkAcls.defaultAction | extend vnetRules = properties.networkAcls.virtualNetworkRules | extend ipRules = properties.networkAcls.ipRules | extend privateEndpoints = properties.privateEndpointConnections | where publicNetworkAccess == "Enabled" | where defaultAction == "Deny" | where (isnull(privateEndpoints) or array_length(privateEndpoints) == 0) | extend allowedVnets = iif(isnull(vnetRules), 0, array_length(vnetRules)) | extend allowedIps = iif(isnull(ipRules), 0, array_length(ipRules)) | where allowedVnets > 0 or allowedIps > 0 | project id, name, vnetRules, ipRules

1234567891011121314 | Resources| where type == "microsoft.storage/storageaccounts"| extend publicNetworkAccess = properties.publicNetworkAccess| extend defaultAction = properties.networkAcls.defaultAction| extend vnetRules = properties.networkAcls.virtualNetworkRules| extend ipRules = properties.networkAcls.ipRules| extend privateEndpoints = properties.privateEndpointConnections| where publicNetworkAccess == "Enabled"| where defaultAction == "Deny"| where (isnull(privateEndpoints) or array_length(privateEndpoints) == 0)| extend allowedVnets = iif(isnull(vnetRules), 0, array_length(vnetRules))| extend allowedIps = iif(isnull(ipRules), 0, array_length(ipRules))| where allowedVnets > 0 or allowedIps > 0| project id, name, vnetRules, ipRules  
---|---  
  
This query identifies allowed virtual networks and also retrieves resources that allow specific IP addresses. This is useful when there is limited visibility into the DNS configurations for virtual networks, making it difficult to determine whether or not the configurations are affected.

Defenders should be aware that even resources that do not have Network ACLs could still be at risk. However, there is no way to use the configurations to determine which virtual networks, if any, attempt to communicate with such resources. To address this risk, use network logs to identify connections made from Azure network ranges to susceptible resources.

Defenders can change and match the resource and the Private DNS zone details in the above Resources query to detect Private Link-supported resources that are at risk.

## Conclusion

Fully understanding the limitations of Azure Private Link is vital to securing networks that rely on it. With certain configurations of components and architecture, the binary nature of Azure Private Link can lead to connectivity loss and in some cases, could enable DoS attacks.

Two of the possible solutions to secure Private Endpoints against this risk include:

  * Enabling fallback to public DNS resolution
  * Manually adding DNS records for affected resources



Defenders can increase the effectiveness of these solutions by querying resources, conducting comprehensive network scanning to identify resources at risk, and implementing the necessary protections.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed in this article through the following products:

  * [Cortex Cloud](https://www.paloaltonetworks.com/cortex/cloud) customers are better protected from the misuse of the Azure Private Endpoints discussed within this article through the proper placement of Cortex Cloud [XDR endpoint agent](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Endpoint-protection) and [serverless agents](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/Serverless-function-posture-security) within a cloud environment. Cortex Cloud is designed to protect a cloud’s posture and runtime operations against these types of threats. It helps detect and prevent the malicious operations or configuration alterations or exploitation discussed within this article.



[Unit 42 Cloud Security Assessment](https://www.paloaltonetworks.com/unit42/assess/cloud-security-assessment) is a strategic evaluation service that reviews your organization's cloud infrastructure to identify misconfigurations and security gaps, enabling teams to strengthen their posture against cloud-based threats.

If you think you might have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

  * [Azure Private Endpoint private DNS zone values](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) – Microsoft documentation
  * [Azure Private Link availability](https://learn.microsoft.com/en-us/azure/private-link/availability) – Microsoft documentation
  * [Azure Resource Graph Explorer](https://learn.microsoft.com/en-us/azure/governance/resource-graph/) – Microsoft documentation
  * [​​Storage access constraints for clients in virtual networks with private endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&bc=%2Fazure%2Fstorage%2Fblobs%2Fbreadcrumb%2Ftoc.json#storage-access-constraints-for-clients-in-virtual-networks-with-private-endpoints) – Microsoft documentation



Back to top

### Tags

  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")
  * [Networking](https://unit42.paloaltonetworks.com/tag/networking/ "networking")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Anatomy of an Attack: The Payroll Pirates and the Power of Social Engineering ](https://unit42.paloaltonetworks.com/social-engineering-payroll-pirates/ "Anatomy of an Attack: The Payroll Pirates and the Power of Social Engineering")

### Table of Contents

  *   * Executive Summary
  * Azure Private Link Key Components, Concepts and Flows
    * Definitions
    * Connection Flows
  * Potential Private Link DNS Dangers
  * Mitigations and Recommendations
    * Mitigations
    * Comprehensive Discovery and Scanning
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Additional Resources



### Related Articles

  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "article - table of contents")
  * [ Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "article - table of contents")



## Related Resources

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026 #### [Novel Technique to Detect Cloud Threat Actor Operations ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of automated detection. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Cloud_cybersecurity_research_Overview_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 14, 2026 #### [Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/ "cloud detection")
  * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/ "DevOps")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection")

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026 #### [Novel Technique to Detect Cloud Threat Actor Operations ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

![Pictorial representation of automated detection. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Cloud_cybersecurity_research_Overview_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 14, 2026 #### [Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud detection](https://unit42.paloaltonetworks.com/tag/cloud-detection/ "cloud detection")
  * [DevOps](https://unit42.paloaltonetworks.com/tag/devops/ "DevOps")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/ "Unmasking Cloud Identities: From Behavioral Clustering to Automated Detection")

![Pictorial representation of bucket hijacking technique for cloud data exfiltration. Digital illustration of Europe map highlighting network connections and nodes, depicted as glowing points and lines on a dark blue background, emphasizing major cities and connectivity across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/09_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 22, 2026 #### [The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/)

  * [AWS](https://unit42.paloaltonetworks.com/tag/aws/ "AWS")
  * [Bucket hijacking](https://unit42.paloaltonetworks.com/tag/bucket-hijacking/ "bucket hijacking")
  * [Cloud data exfiltration](https://unit42.paloaltonetworks.com/tag/cloud-data-exfiltration/ "cloud data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration")

![Pictorial representation of Vertex AI model uploads. Close-up view of a digital wall displaying various glowing icons, representing a high-tech network interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/AdobeStock_1270203474-1-786x354.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 16, 2026 #### [Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

  * [Bucket squatting](https://unit42.paloaltonetworks.com/tag/bucket-squatting/ "bucket squatting")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Joblib](https://unit42.paloaltonetworks.com/tag/joblib/ "joblib")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE")

![Pictorial representation of Cloud Logging services for defense evasion. A vibrant digital illustration depicting a glowing, neon blue cloud symbol positioned over a circuit board landscape. The cloud symbolizes cloud computing technology, and the landscape features intricate electronic circuits with glowing lines and nodes, suggesting high-tech data transfer and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/11_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) June 9, 2026 #### [Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/)

  * [AWS CloudTrail](https://unit42.paloaltonetworks.com/tag/aws-cloudtrail/ "AWS CloudTrail")
  * [Cloud logging](https://unit42.paloaltonetworks.com/tag/cloud-logging/ "cloud logging")
  * [Defense evasion](https://unit42.paloaltonetworks.com/tag/defense-evasion/ "defense evasion")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/ "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility")

![Pictorial representation of ROADtools framework in the cloud. An Asian man wearing glasses sits in front of a computer screen. Reflecting in the glasses are lines indicating analysis. Bright blue city lights illuminate the rest of the image.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/10_Cloud_cybersecurity_research_Overview_1920x900-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) May 22, 2026 #### [Paved With Intent: ROADtools and Nation-State Tactics in the Cloud ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)

  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Azure](https://unit42.paloaltonetworks.com/tag/microsoft-azure/ "Microsoft Azure")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/ "Paved With Intent: ROADtools and Nation-State Tactics in the Cloud")

![Pictorial representation of autonomous AI attack in cloud environments. Digital illustration of a glowing blue brain connected to a network of lines and lights.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/12_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 23, 2026 #### [Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/ "Cloud")
  * [Data exfiltration](https://unit42.paloaltonetworks.com/tag/data-exfiltration/ "data exfiltration")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/ "Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System")

![Pictorial representation of passwordless authentication. Futuristic cityscape with skyscrapers surrounded by glowing, neon-lit pathways and digital clouds. The sky is vibrant with pink and orange hues, giving a surreal, cyberpunk aesthetic.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/03/02_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) March 23, 2026 #### [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication ](https://unit42.paloaltonetworks.com/passwordless-authentication/)

  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/passwordless-authentication/ "Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication")

![Close-up of a black woman with glasses examining colorful computer code on a screen. The scene is illuminated by various lights, creating a focused and analytical atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/13_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) February 6, 2026 #### [Novel Technique to Detect Cloud Threat Actor Operations ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [IAM](https://unit42.paloaltonetworks.com/tag/iam/ "IAM")
  * [MITRE](https://unit42.paloaltonetworks.com/tag/mitre/ "MITRE")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/tracking-threat-groups-through-cloud-logging/ "Novel Technique to Detect Cloud Threat Actor Operations")

![Pictorial representation of cloud discovery with AzureHound. A digital representation of a cloud composed of blue light particles, superimposed over a blurred background of server racks in a data center.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/10/08_Cloud_cybersecurity_research_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) October 24, 2025 #### [Cloud Discovery With AzureHound ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/)

  * [Control plane](https://unit42.paloaltonetworks.com/tag/control-plane/ "control plane")
  * [Curious Serpens](https://unit42.paloaltonetworks.com/tag/curious-serpens/ "Curious Serpens")
  * [Data plane](https://unit42.paloaltonetworks.com/tag/data-plane/ "data plane")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/threat-actor-misuse-of-azurehound/ "Cloud Discovery With AzureHound")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/)