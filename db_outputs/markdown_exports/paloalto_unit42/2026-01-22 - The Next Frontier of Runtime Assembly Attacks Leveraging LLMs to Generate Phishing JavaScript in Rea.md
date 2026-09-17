# The Next Frontier of Runtime Assembly Attacks: Leveraging LLMs to Generate Phishing JavaScript in Real Time

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/real-time-malicious-javascript-through-llms/
- **Date :** 2026-01-22

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# The Next Frontier of Runtime Assembly Attacks: Leveraging LLMs to Generate Phishing JavaScript in Real Time

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 9 min read 

Related Products

[![Advanced URL Filtering icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Advanced URL Filtering](https://unit42.paloaltonetworks.com/product-category/advanced-url-filtering/ "Advanced URL Filtering")[![Cloud-Delivered Security Services icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/strata_RGB_logo_Icon_Color.png)Cloud-Delivered Security Services](https://unit42.paloaltonetworks.com/product-category/cloud-delivered-security-services/ "Cloud-Delivered Security Services")[![Code to Cloud Platform icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Code to Cloud Platform](https://unit42.paloaltonetworks.com/product-category/code-to-cloud-platform/ "Code to Cloud Platform")[![Prisma AIRS icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma AIRS](https://unit42.paloaltonetworks.com/product-category/prisma-airs/ "Prisma AIRS")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI Security Assessment](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Shehroze Farooqi](https://unit42.paloaltonetworks.com/author/shehroze-farooqi/)
    * [Alex Starov](https://unit42.paloaltonetworks.com/author/alex-starov/)
    * [Diva-Oriane Marty](https://unit42.paloaltonetworks.com/author/diva-oriane-marty/)
    * [Billy Melicher](https://unit42.paloaltonetworks.com/author/billy-melicher/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:January 22, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [API](https://unit42.paloaltonetworks.com/tag/api/)
    * [DeepSeek](https://unit42.paloaltonetworks.com/tag/deepseek/)
    * [Google](https://unit42.paloaltonetworks.com/tag/google/)
    * [JavaScript](https://unit42.paloaltonetworks.com/tag/javascript/)
    * [LLM](https://unit42.paloaltonetworks.com/tag/llm/)
    * [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/real-time-malicious-javascript-through-llms/?pdf=download&lg=en&_wpnonce=252a1929a6 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/real-time-malicious-javascript-through-llms/?pdf=print&lg=en&_wpnonce=252a1929a6 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=The%20Next%20Frontier%20of%20Runtime%20Assembly%20Attacks:%20Leveraging%20LLMs%20to%20Generate%20Phishing%20JavaScript%20in%20Real%20Time&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Freal-time-malicious-javascript-through-llms%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Freal-time-malicious-javascript-through-llms%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Freal-time-malicious-javascript-through-llms%2F&title=The%20Next%20Frontier%20of%20Runtime%20Assembly%20Attacks:%20Leveraging%20LLMs%20to%20Generate%20Phishing%20JavaScript%20in%20Real%20Time "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Freal-time-malicious-javascript-through-llms%2F&text=The%20Next%20Frontier%20of%20Runtime%20Assembly%20Attacks:%20Leveraging%20LLMs%20to%20Generate%20Phishing%20JavaScript%20in%20Real%20Time "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Freal-time-malicious-javascript-through-llms%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=The%20Next%20Frontier%20of%20Runtime%20Assembly%20Attacks:%20Leveraging%20LLMs%20to%20Generate%20Phishing%20JavaScript%20in%20Real%20Time%20https%3A%2F%2Funit42.paloaltonetworks.com%2Freal-time-malicious-javascript-through-llms%2F "Share in Mastodon")



## Executive Summary

Imagine visiting a webpage that looks perfectly safe. It has no malicious code, no suspicious links. Yet, within seconds, it transforms into a personalized phishing page.

This isn't merely an illusion. It's the next frontier of web attacks where attackers use generative AI (GenAI) to build a threat that’s loaded after the victim has already visited a seemingly innocuous webpage.

In other words, this article demonstrates a novel attack technique where a seemingly benign webpage uses client-side API calls to trusted large language model (LLM) services for generating malicious JavaScript dynamically in real time. Attackers could use carefully engineered prompts to bypass AI safety guardrails, tricking the LLM into returning malicious code snippets. These snippets are returned via the LLM service API, then assembled and executed in the victim's browser at runtime, resulting in a fully functional phishing page.

This AI-augmented runtime assembly technique is designed to be evasive:

  * The code for the phishing page is polymorphic, so there’s a unique, syntactically different variant for each visit
  * The malicious content is delivered from a trusted LLM domain, bypassing network analysis
  * It is assembled and executed at runtime



The most effective defense against this new class of threat is runtime behavioral analysis that can detect and block malicious activity at the point of execution, directly within the browser.

Palo Alto Networks customers are better protected through the following products and services:

  * [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering)
  * [Prisma AIRS](https://www.deploybravely.com/?utm_source=google-jg-amer-portfolio-brnd-port&utm_medium=paid_search&utm_campaign=google-portfolio-ai_netsec-amer-multi-awareness-en-brand&utm_content=701Ki000000ov6EIAQ&utm_term=&cq_plac=&cq_net=&gad_source=1&gad_campaignid=22490755190&gbraid=0AAAAADHVeKmI_vEpNpBJwzqZKjEH9iYW2&gclid=CjwKCAiAmKnKBhBrEiwAaqAnZ4el2jU9ELl0BlR9j7x1ugBYcXrw-mYH1IeeT33a_UTm7HNdMqF2UhoCstsQAvD_BwE#webinar)  
[Prisma Browser](https://www.paloaltonetworks.com/sase/prisma-browser?utm_source=google-jg-amer-sase-smco-sfow&utm_medium=paid_search&utm_campaign=google-sase-prisma_access_browser-amer-multi-lead_gen-en-brand&utm_content=7014u000001eJvUAAU&utm_term=prisma%20browser&cq_plac=&cq_net=g&gad_source=1&gad_campaignid=21238548378&gbraid=0AAAAADHVeKmIT56W3Z1uQWD9jZtvf_Sns&gclid=CjwKCAiAmKnKBhBrEiwAaqAnZyWF477utwE7Lu4rmDga-zkelcMsRE8cvkfZ6jydw9qeZK75nFrseBoCfUAQAvD_BwE) with Advanced Web Protection



The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment) can help empower safe AI use and development across your organization.

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | [**JavaScript**](https://unit42.paloaltonetworks.com/tag/javascript/), **[LLMs](https://unit42.paloaltonetworks.com/tag/llm/)** , [**Phishing**](https://unit42.paloaltonetworks.com/tag/phishing/)  
---|---  
  
## LLM-Augmented Runtime Assembly Attack Model

Our [previous research](https://unit42.paloaltonetworks.com/using-llms-obfuscate-malicious-javascript/) shows how attackers can effectively use LLMs to obfuscate their malicious JavaScript samples offline. Reports from other sources have documented campaigns that leverage LLMs during runtime execution on compromised machines to tailor attacks (e.g., LLM-powered [malware](https://cybersecuritynews.com/llm-powered-malware-from-apt28-hackers-integrates-ai-capabilities/amp/) and [ransomware](https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/)).

Anthropic researchers have also published reports indicating that LLMs have [aided cybercriminals](https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf) and played a role in [AI-orchestrated cyberespionage campaigns](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf). Motivated by these recent discoveries, we researched how threat actors could leverage LLMs to generate, assemble and execute phishing attack payloads within a webpage at runtime, making it challenging to detect with network analysis. Below we outline our proof of concept (POC) for this attack scenario and offer steps to help mitigate the impact of this potential attack.

### Attack Model For Our PoC

The attack scenario begins with a seemingly benign page. Once loaded in the victim's browser, the initial webpage makes requests for client-side JavaScript to popular and trusted LLM clients (e.g., DeepSeek and Google Gemini, though the PoC could be effective across a number of models.).

Attackers can then trick the LLM into returning malicious JavaScript snippets using carefully engineered prompts that circumvent safety guardrails. These snippets are then assembled and executed in the browser's runtime to render a fully functional phishing page. This leaves behind no static, detectable payload.

Figure 1 shows how we developed our PoC to leverage LLMs to enhance existing attacks and bypass defenses. The first two steps involve initial preparation, while the final step details the generation and execution of phishing code within the browser at runtime.

![Flowchart demonstrating a cybersecurity threat involving phishing. The process includes selecting a phishing page, translating malicious code into LLM prompts to circumvent security, and executing scripts in the browser to display a benign-looking page while malicious content is processed in the background. Icons represent coding, engineering, and trusted API endpoints, focusing on a 'SecureBank Login' example.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/ENG_llm-augmented-runtime-attack-2-786x417.png)Figure 1. Workflow of the PoC. The first two steps are initial preparation, and the third is an example of generating malicious content to be rendered in the browser.

#### Step 1: Select a Malicious or Phishing Webpage

The attacker’s first step would be to select a webpage from an active phishing or malicious campaign to use as a model for the type of malicious code that would perform the desired function. From there, they can create JavaScript code snippets that will be generated in real-time to dynamically render the final page displayed to the user.

#### Step 2: Translate Malicious JavaScript Code Into LLM Prompts

The attacker’s next step would be to craft prompts describing the JavaScript code's functionality to the LLM in plain text. They could iteratively refine prompts, generating malicious code that bypasses existing LLM guardrails. These generated snippets could differ structurally and syntactically, allowing attackers to create [polymorphic code](https://medium.com/@RocketMeUpCybersecurity/polymorphic-malware-understanding-evasive-attack-strategies-6e1708780a56) with the same functionality.

#### Step 3: Generate and Execute Malicious Scripts at Runtime

From there, attackers could embed these engineered prompts inside a webpage, which would load on the victim's browser. The webpage would then use the prompt to request a popular, legitimate LLM API endpoint to generate malicious code snippets. These snippets could then be transmitted over popular, trusted domains to bypass network analysis. Subsequently, these generated scripts could be assembled and executed to render malicious code or phishing content.

### How This Attack Technique Helps with Evasion

This technique builds upon existing evasive runtime assembly behaviors that we often observe on phishing and malware delivery URLs. For example, 36% of malicious webpages we detect daily exhibit runtime assembly behavior, such as executing constructed child scripts with an eval function (e.g., retrieved, decoded or assembled payloads). Leveraging LLMs during runtime on a webpage gives attackers the following benefits:

  * **Evading network analysis:** The malicious code generated by an LLM could be transferred over the network from a trusted domain, as access to domains of popular LLM API endpoints is often allowed from the client side.
  * **Increasing the diversity of malicious scripts** **with each visit** : An LLM can generate new variants of phishing code, leading to higher polymorphism. This can make detection more challenging.
  * **Using runtime assembly and executing JavaScript code** **to complicate detection:** Assembling and executing these code snippets during runtime enables more tailored phishing campaigns, such as selecting a target brand based on the victim's location or email address.
  * **Obfuscating code in plain text:** Translating code into text for subsequent concealment within a webpage can be viewed as a form of obfuscation. Attackers commonly employ various conventional techniques (e.g., encoding, encryption and code fragmenting) to visually conceal malicious code and evade detection. While advanced analyses often identify conventional obfuscation methods by evaluating expressions, it will be more challenging for defenders to evaluate text as executable code without subjecting each snippet to an LLM.



### PoC Example

In researching the PoC we were able to demonstrate how this augmentation could be applied to a real-world phishing campaign, illustrating its ability to enhance evasion techniques through the steps we outline above. A brief overview of this PoC is provided below.

#### Step 1: Selecting a Malicious/phishing Webpage

For our PoC, we replicated a webpage from an advanced real-world phishing campaign known as [LogoKit](https://cyble.com/blog/logokit-being-leveraged-for-credential-theft/). The original phishing attack uses a static JavaScript payload to transform a benign-looking web form into a convincing phishing lure. This script performs two key functions: personalizing the page based on the victim’s email in the address bar and exfiltrating captured credentials to an attacker's web server.

#### Step 2: Translating Malicious JavaScript Code Into LLM prompts

Our PoC uses a popular LLM service, accessible via a chat API query from within the browser's JavaScript. To mitigate potential misuse by attackers, we are not disclosing the name of this specific API. We used this LLM API to dynamically generate the code necessary for credential harvesting and impersonate target webpages. Because the malicious payload is generated dynamically in the browser, the initial page transmitted over the network is benign, allowing it to inherently bypass network-based security detectors.

The attack's success hinged on careful prompt engineering to bypass the LLM's built-in safeguards. We found simple rephrasing was remarkably effective.

For instance, a request for a generic $AJAX POST function was permitted (shown in Figure 2), while a direct request for "code to exfiltrate credentials" was blocked. Furthermore, indicators of compromise (IoCs) (e.g., Base64-encoded exfiltration URLs) could also be hidden within the prompt itself to keep the initial page clean.

![Screenshot displaying a document containing text instructions on coding. The text includes a red underlined URL and several coding commands and explanations related to AJAX requests. The document has a plain white background with red and black text. At the top of the image is the Base64 encoded URL. The second paragraph is the ask to make the AJAX request instead of credential exfiltration. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-829680-170747-2.png)Figure 2. Example of prompt engineering to bypass LLM guardrails and generate JavaScript code for phishing content.

The non-deterministic output of the model provided a high degree of polymorphism, with each query returning a syntactically unique yet functionally identical variant of the malicious code. For example, Figure 3 shows differences in code snippets highlighted in red. This constant mutation makes detection more difficult.

![Screenshot of two side-by-side code comparisons in an IDE, focusing on different methods of extracting and handling URLs and domain data in JavaScript. The left code extract uses requests while the right code analyzes email-based URLs for domain extraction, highlighted with annotations and marked steps.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-832076-170747-3.jpeg)Figure 3. Polymorphism creating multiple variants of dynamically generated JavaScript code.

Of note, LLM-generated code can include hallucinations but we mitigated this through prompt refinement and increased specificity, effectively reducing syntax errors. As a result, the final, highly specific prompt successfully generated functional code in most instances.

#### Step 3: Executing Malicious Scripts at Runtime

The generated script was assembled and executed at runtime on the webpage to render the phishing content. This process successfully constructed a functional, brand-impersonating phishing page, validating the attack's viability (shown in Figure 4). The successful execution of the generated code, which rendered the phishing page without error, confirmed the efficacy of our PoC.

![Screenshot collage showing a phishing attack process. Top image: a fake login page. Middle image: a fake login page for Palo Alto Networks for detecting the phishing page. Bottom image: a phishing code generator interface.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-834502-170747-4.jpeg)Figure 4. Example of a phishing page rendered by assembling dynamically generated JavaScript on runtime in-browser.

## Generalizing the Threat and Expanding the Attack Surface

### Alternate Methods to Request LLM API

Our attack model, demonstrated through a PoC, could be implemented in various ways. However, each methodology described in the PoC speaks to how an attacker connects to LLM APIs for transferring malicious code as snippets that are executed in the browser at runtime.

As shown in our PoC, attackers could bypass security measures by directly connecting to a well-known LLM service API endpoint from a browser to execute code-generation prompts. Alternatively, they might use a backend proxy server on trusted domains or content delivery networks (CDNs) to connect to the LLM service for prompt execution. A further tactic could involve connecting to this backend proxy server via non-HTTP connections such as WebSockets, a method we have [previously reported](https://x.com/Unit42_Intel/status/1978875677962088507) in phishing campaigns.

### Other Abuses of Trusted Domains

Attackers have abused the trust of legitimate domains to circumvent detections in the past, as seen in instances like [EtherHiding](https://guard.io/labs/etherhiding-hiding-web2-malicious-code-in-web3-smart-contracts). In EtherHiding, attackers concealed malicious payloads on public blockchains associated with reputable and trusted smart contract platforms.

The attack detailed in this article uses a combination of diverse, LLM-generated malicious code snippets and the transmission of this malicious code through a trusted domain, to evade detection.

### Translation of Malicious Code Into Text Prompts for More Attacks

This article focuses on the conversion of malicious JavaScript code into a text prompt to facilitate the rendering of a phishing webpage. This methodology presents a potential vector for malicious actors to generate diverse forms of hostile code. For example, they could develop malware or establish a command-and-control (C2) channel on a compromised machine that generates and transmits malicious code from trusted domains associated with popular LLMs.

### Attacks Leveraging In-Browser Runtime Assembly Behaviors

The attack model presented here exemplifies runtime assembly behaviors, where malicious webpages are dynamically constructed within a browser. Prior research has also documented different variants of runtime assembly for crafting phishing pages or malware delivery. For example, this[ article](https://securitybrief.com.au/story/attackers-break-malware-into-tiny-pieces-and-bypass-your-secure-web-gateway) mentions a technique where an attacker breaks down malicious code into smaller components, subsequently reassembling them for execution at runtime within the browser (termed by SquareX as [last mile reassembling attack](https://sqrx.com/lastmilereassemblyattacks)). Various reports describe attackers using [HTML smuggling](https://attack.mitre.org/techniques/T1027/006/) techniques to deliver malware.

The attack model outlined in this post goes further, as it involves the runtime generation of novel script variants that are later assembled and executed, posing a significantly elevated challenge to detection.

## Recommendations for Defenders

The dynamic nature of this attack in combination with runtime assembly in the browser makes it a formidable defense challenge. This attack model creates a unique variant for every victim. Each malicious payload is dynamically generated and unique, transmitted over a trusted domain.

This scenario signals a critical shift in the security landscape. Detection of these attacks (while possible through enhanced browser-based crawlers) ​​requires runtime behavioral analysis within the browser.

Defenders should also restrict the use of unsanctioned LLM services at workplaces. While this is not a complete solution, it can serve as an important preventative measure.

Finally, our work highlights the need for more robust safety guardrails in LLM platforms, as we demonstrated how careful prompt engineering can circumvent existing protections and enable malicious use.

## Conclusion

This article demonstrates a novel AI-augmented approach where a malicious webpage uses LLM services to dynamically generate numerous variants of malicious code in real-time within the browser. To combat this, the most effective strategy is runtime behavioral analysis at the point of execution through in-browser protection and by running offline analysis with browser-based sandboxes that render the final webpage.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

[Prisma AIRS](https://www.deploybravely.com/?utm_source=google-jg-amer-portfolio-brnd-port&utm_medium=paid_search&utm_campaign=google-portfolio-ai_netsec-amer-multi-awareness-en-brand&utm_content=701Ki000000ov6EIAQ&utm_term=&cq_plac=&cq_net=&gad_source=1&gad_campaignid=22490755190&gbraid=0AAAAADHVeKmI_vEpNpBJwzqZKjEH9iYW2&gclid=CjwKCAiAmKnKBhBrEiwAaqAnZ4el2jU9ELl0BlR9j7x1ugBYcXrw-mYH1IeeT33a_UTm7HNdMqF2UhoCstsQAvD_BwE#webinar) customers can secure their in-house built GenAI applications against inputs that attempt to circumvent guardrails.

Customers using [Advanced URL Filtering](https://docs.paloaltonetworks.com/advanced-url-filtering) and [Prisma Browser](https://www.paloaltonetworks.com/sase/prisma-browser?utm_source=google-jg-amer-sase-smco-sfow&utm_medium=paid_search&utm_campaign=google-sase-prisma_access_browser-amer-multi-lead_gen-en-brand&utm_content=7014u000001eJvUAAU&utm_term=prisma%20browser&cq_plac=&cq_net=g&gad_source=1&gad_campaignid=21238548378&gbraid=0AAAAADHVeKmIT56W3Z1uQWD9jZtvf_Sns&gclid=CjwKCAiAmKnKBhBrEiwAaqAnZyWF477utwE7Lu4rmDga-zkelcMsRE8cvkfZ6jydw9qeZK75nFrseBoCfUAQAvD_BwE) (with Advanced Web Protection) are better protected against various runtime assembly attacks.

[Prisma Browser](https://www.paloaltonetworks.com/sase/prisma-browser?utm_source=google-jg-amer-sase-smco-sfow&utm_medium=paid_search&utm_campaign=google-sase-prisma_access_browser-amer-multi-lead_gen-en-brand&utm_content=7014u000001eJvUAAU&utm_term=prisma%20browser&cq_plac=&cq_net=g&gad_source=1&gad_campaignid=21238548378&gbraid=0AAAAADHVeKmIT56W3Z1uQWD9jZtvf_Sns&gclid=CjwKCAiAmKnKBhBrEiwAaqAnZyWF477utwE7Lu4rmDga-zkelcMsRE8cvkfZ6jydw9qeZK75nFrseBoCfUAQAvD_BwE) customers with Advanced Web Protection are protected against Runtime Re-assembly attacks from the first attempt, or "patient zero" hit, because the defense uses runtime behavioral analysis directly within the browser to detect and block malicious activity at the point of execution.

The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/unit42/assess/ai-security-assessment) can help empower safe AI use and development across your organization.

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

  * North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
  * UK: +44.20.3743.3660
  * Europe and Middle East: +31.20.299.3130
  * Asia: +65.6983.8730
  * Japan: +81.50.1790.0200
  * Australia: +61.2.4062.7950
  * India: 000 800 050 45107
  * South Korea: +82.080.467.8774



Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Additional Resources

  * [Now You See Me, Now You Don’t: Using LLMs to Obfuscate Malicious JavaScript](https://unit42.paloaltonetworks.com/using-llms-obfuscate-malicious-javascript/) – Unit 42, Palo Alto Networks
  * [First known AI-powered ransomware uncovered by ESET Research](https://www.welivesecurity.com/en/ransomware/first-known-ai-powered-ransomware-uncovered-eset-research/) – ESET
  * [First Known LLM-Powered Malware From APT28 Hackers Integrates AI Capabilities into Attack Methodology](https://cybersecuritynews.com/llm-powered-malware-from-apt28-hackers-integrates-ai-capabilities/amp/) – Cybersecurity News
  * [UAC-0001 Cyberattacks on Security/Defense Sector Using LLM-Based LAMEHUG Tool](https://cert.gov.ua/article/6284730) – CERT-UA [Ukrainian]
  * [AI-orchestrated cyber espionage campaigns [PDF]](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) – Anthropic Report
  * [Attackers break malware into tiny pieces and bypass your Secure Web Gateway](https://securitybrief.com.au/story/attackers-break-malware-into-tiny-pieces-and-bypass-your-secure-web-gateway) – SecurityBrief Australia
  * [What are Last Mile Reassembly Attacks?](https://sqrx.com/lastmilereassemblyattacks) – SquareX
  * [“EtherHiding:” Hiding Web2 Malicious Code in Web3 Smart Contracts](https://guard.io/labs/etherhiding-hiding-web2-malicious-code-in-web3-smart-contracts) – Guardio



Back to top

### Tags

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [DeepSeek](https://unit42.paloaltonetworks.com/tag/deepseek/ "DeepSeek")
  * [Google](https://unit42.paloaltonetworks.com/tag/google/ "Google")
  * [JavaScript](https://unit42.paloaltonetworks.com/tag/javascript/ "JavaScript")
  * [LLM](https://unit42.paloaltonetworks.com/tag/llm/ "LLM")
  * [Phishing](https://unit42.paloaltonetworks.com/tag/phishing/ "phishing")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: DNS OverDoS: Are Private Endpoints Too Private? ](https://unit42.paloaltonetworks.com/dos-attacks-and-azure-private-endpoint/ "DNS OverDoS: Are Private Endpoints Too Private?")

### Table of Contents

  *   * Executive Summary
  * LLM-Augmented Runtime Assembly Attack Model
    * Attack Model For Our PoC
      * Step 1: Select a Malicious or Phishing Webpage
      * Step 2: Translate Malicious JavaScript Code Into LLM Prompts
      * Step 3: Generate and Execute Malicious Scripts at Runtime
    * How This Attack Technique Helps with Evasion
    * PoC Example
      * Step 1: Selecting a Malicious/phishing Webpage
      * Step 2: Translating Malicious JavaScript Code Into LLM prompts
      * Step 3: Executing Malicious Scripts at Runtime
  * Generalizing the Threat and Expanding the Attack Surface
    * Alternate Methods to Request LLM API
    * Other Abuses of Trusted Domains
    * Translation of Malicious Code Into Text Prompts for More Attacks
    * Attacks Leveraging In-Browser Runtime Assembly Behaviors
  * Recommendations for Defenders
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Additional Resources



### Related Articles

  * [ The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "article - table of contents")
  * [ Perturbation Probing: A New Diagnostic for the Fragility of LLM Safety ](https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/ "article - table of contents")
  * [ Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks ](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/ "article - table of contents")



## Related Malware Resources

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

![Pictorial representation of a magnifying glass illuminating a glowing orange circular digital circuit interface on a dark, high-tech background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) September 16, 2026 #### [Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")
  * [Unit 42](https://unit42.paloaltonetworks.com/tag/unit-42/ "Unit 42")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS \(AMOS\) Stealer Activity")

![Pictorial representation of post-exploitation identity misuse in SPIFFE/SPIRE. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 10, 2026 #### [The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [Cryptographic](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")

![Pictorial representation of a pay-per-install threat group campaign prodiving infection service for spreading malware. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip, symbolizing data processing and transfer. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 9, 2026 #### [Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

  * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")
  * [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")
  * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")

![Pictorial representation of attackers using AI tools to target Latin American organizations. A vibrant cityscape with silhouettes of numerous people walking along a bustling street. The scene is illuminated by bright urban lights and digital-like particles, creating a dynamic and futuristic atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2026 #### [Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")

![Pictorial representation of vishing campaigns in Microsoft Teams. A digital image of a skull formed by blue binary code on a black background, with scattered ones and zeros and digital noise, symbolizes how stealthy prompt injection attacks can exploit AI logic to bypass security controls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 31, 2026 #### [Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

  * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")

![Pictorial representation of AI-enabled malware. A vibrant digital interface displaying various icons and graphs, resembling a futuristic network or data analysis dashboard. The scene is illuminated with glowing lights and patterns.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 25, 2026 #### [The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

  * [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")
  * [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
  * [DLL hijacking](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")

![Pictorial representation of identity abuse through trusted communication channels. Close-up view of a digital screen displaying a glitched and pixelated image of a skull-like shape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 20, 2026 #### [Identity Abuse Through Trusted Communication Channels ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

  * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")
  * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

![Pictorial representation of a magnifying glass illuminating a glowing orange circular digital circuit interface on a dark, high-tech background.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) September 16, 2026 #### [Atomic macOS (AMOS) Stealer Activity ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/)

  * [MacOS](https://unit42.paloaltonetworks.com/tag/macos/ "macOS")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")
  * [Unit 42](https://unit42.paloaltonetworks.com/tag/unit-42/ "Unit 42")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/ "Atomic macOS \(AMOS\) Stealer Activity")

![Pictorial representation of post-exploitation identity misuse in SPIFFE/SPIRE. Close-up of a person wearing glasses, with computer code reflected in the lenses.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/12_Security-Technology_Category_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 10, 2026 #### [The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/)

  * [API](https://unit42.paloaltonetworks.com/tag/api/ "API")
  * [Cryptographic](https://unit42.paloaltonetworks.com/tag/cryptographic/ "cryptographic")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/ "The Machine With Many Faces: Post-Exploitation Identity Misuse in SPIFFE/SPIRE")

![Pictorial representation of a pay-per-install threat group campaign prodiving infection service for spreading malware. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip, symbolizing data processing and transfer. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/04_Malware_Category_1920x900-6-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 9, 2026 #### [Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/)

  * [ARKTunnel](https://unit42.paloaltonetworks.com/tag/arktunnel/ "ARKTunnel")
  * [C2](https://unit42.paloaltonetworks.com/tag/c2/ "C2")
  * [CL-CRI-1171](https://unit42.paloaltonetworks.com/tag/cl-cri-1171/ "CL-CRI-1171")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/ "Untracked Nightmares: The Threats Hiding Behind Commodity Infrastructure")

![Pictorial representation of attackers using AI tools to target Latin American organizations. A vibrant cityscape with silhouettes of numerous people walking along a bustling street. The scene is illuminated by bright urban lights and digital-like particles, creating a dynamic and futuristic atmosphere.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/09/AdobeStock_768915868-2-1-786x373.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) September 3, 2026 #### [Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)

  * [Agentic AI](https://unit42.paloaltonetworks.com/tag/agentic-ai/ "Agentic AI")
  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [CL-CRI-1131](https://unit42.paloaltonetworks.com/tag/cl-cri-1131/ "CL-CRI-1131")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/ "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America")

![Pictorial representation of vishing campaigns in Microsoft Teams. A digital image of a skull formed by blue binary code on a black background, with scattered ones and zeros and digital noise, symbolizes how stealthy prompt injection attacks can exploit AI logic to bypass security controls.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/01_Malware_Category_1920x900-5-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 31, 2026 #### [Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/)

  * [Cloaked Ursa](https://unit42.paloaltonetworks.com/tag/cloaked-ursa/ "Cloaked Ursa")
  * [Entra ID](https://unit42.paloaltonetworks.com/tag/entra-id/ "Entra ID")
  * [Microsoft Teams](https://unit42.paloaltonetworks.com/tag/microsoft-teams/ "Microsoft Teams")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/ "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams")

![Pictorial representation of AI-enabled malware. A vibrant digital interface displaying various icons and graphs, resembling a futuristic network or data analysis dashboard. The scene is illuminated with glowing lights and patterns.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/AdobeStock_1270203474-2-1-786x368.png)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 25, 2026 #### [The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/)

  * [Backdoor](https://unit42.paloaltonetworks.com/tag/backdoor/ "backdoor")
  * [Bitcoin](https://unit42.paloaltonetworks.com/tag/bitcoin/ "Bitcoin")
  * [DLL hijacking](https://unit42.paloaltonetworks.com/tag/dll-hijacking/ "DLL hijacking")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ai-enabled-malware-analysis/ "The State of AI-Enabled Malware August 2026: From Brand Abuse to Agentic Execution")

![Pictorial representation of identity abuse through trusted communication channels. Close-up view of a digital screen displaying a glitched and pixelated image of a skull-like shape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/02_Malware_Category_1920x900-2-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 20, 2026 #### [Identity Abuse Through Trusted Communication Channels ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/)

  * [Authentication](https://unit42.paloaltonetworks.com/tag/authentication/ "authentication")
  * [Identity theft](https://unit42.paloaltonetworks.com/tag/identity-theft/ "identity theft")
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/ "Identity Abuse Through Trusted Communication Channels")

![Pictorial representation of Kimwolf botnet malware family. Digital screen with a warning sign reading "Malware." The background features lines of computer code and graphics, creating a sense of cybersecurity threat.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/07_Malware_Category_1920x900-3-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 11, 2026 #### [Kimwolf v7: An Evolution of the Kimwolf Botnet ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/)

  * [Android APK](https://unit42.paloaltonetworks.com/tag/android-apk/ "Android APK")
  * [Ethereum](https://unit42.paloaltonetworks.com/tag/ethereum/ "Ethereum")
  * [HTTP](https://unit42.paloaltonetworks.com/tag/http/ "HTTP")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/ "Kimwolf v7: An Evolution of the Kimwolf Botnet")

![Pictorial representatiom pf Aeternum's blockchain C2. A close-up of a computer circuit board with a central microchip is depicted. Red digital data streams in the form of glowing binary numbers and arrows appear to flow in and out of the chip. The scene is illuminated with a futuristic blue and red glow.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/04_Malware_Category_1920x900-4-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) August 10, 2026 #### [The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/)

  * [Aeternum](https://unit42.paloaltonetworks.com/tag/aeternum/ "Aeternum")
  * [Infection chain](https://unit42.paloaltonetworks.com/tag/infection-chain/ "infection chain")
  * [JSON](https://unit42.paloaltonetworks.com/tag/json/ "JSON")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications")

![Pictorial representation of ChainDrop, a self-propagating npm worm. An artistic depiction of a digital workspace featuring an open laptop with a red virus on the screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/03_Malware_Category_1920x900-7-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) August 6, 2026 #### [ChainDrop: Inside a Self-Propagating npm Worm ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)

  * [Blockchain](https://unit42.paloaltonetworks.com/tag/blockchain/ "blockchain")
  * [ChainDrop](https://unit42.paloaltonetworks.com/tag/chaindrop/ "ChainDrop")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/ "ChainDrop: Inside a Self-Propagating npm Worm")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/real-time-malicious-javascript-through-llms/)