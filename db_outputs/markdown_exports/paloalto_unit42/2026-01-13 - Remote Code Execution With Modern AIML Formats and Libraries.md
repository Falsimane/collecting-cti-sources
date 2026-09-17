# Remote Code Execution With Modern AI/ML Formats and Libraries

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/
- **Date :** 2026-01-13

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/ "Vulnerabilities")



[Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

# Remote Code Execution With Modern AI/ML Formats and Libraries

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 11 min read 

Related Products

[![Code to Cloud Platform icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Code to Cloud Platform](https://unit42.paloaltonetworks.com/product-category/code-to-cloud-platform/ "Code to Cloud Platform")[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Prisma AIRS icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma AIRS](https://unit42.paloaltonetworks.com/product-category/prisma-airs/ "Prisma AIRS")[![Unit 42 AI Security Assessment icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 AI Security Assessment](https://unit42.paloaltonetworks.com/product-category/ai-security-assessment/ "Unit 42 AI Security Assessment")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Curtis Carmony](https://unit42.paloaltonetworks.com/author/curtis-carmony/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:January 13, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
    * [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Apple](https://unit42.paloaltonetworks.com/tag/apple/)
    * [CVE-2025-23304](https://unit42.paloaltonetworks.com/tag/cve-2025-23304/)
    * [CVE-2026-22584](https://unit42.paloaltonetworks.com/tag/cve-2026-22584/)
    * [NVIDIA](https://unit42.paloaltonetworks.com/tag/nvidia/)
    * [Python](https://unit42.paloaltonetworks.com/tag/python/)
    * [PyTorch](https://unit42.paloaltonetworks.com/tag/pytorch/)
    * [Salesforce](https://unit42.paloaltonetworks.com/tag/salesforce/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/?pdf=download&lg=en&_wpnonce=252a1929a6 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/?pdf=print&lg=en&_wpnonce=252a1929a6 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Remote%20Code%20Execution%20With%20Modern%20AI/ML%20Formats%20and%20Libraries&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Frce-vulnerabilities-in-ai-python-libraries%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Frce-vulnerabilities-in-ai-python-libraries%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Frce-vulnerabilities-in-ai-python-libraries%2F&title=Remote%20Code%20Execution%20With%20Modern%20AI/ML%20Formats%20and%20Libraries "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Frce-vulnerabilities-in-ai-python-libraries%2F&text=Remote%20Code%20Execution%20With%20Modern%20AI/ML%20Formats%20and%20Libraries "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Frce-vulnerabilities-in-ai-python-libraries%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Remote%20Code%20Execution%20With%20Modern%20AI/ML%20Formats%20and%20Libraries%20https%3A%2F%2Funit42.paloaltonetworks.com%2Frce-vulnerabilities-in-ai-python-libraries%2F "Share in Mastodon")



## Executive Summary

We identified vulnerabilities in three open-source artificial intelligence/machine learning (AI/ML) Python libraries published by Apple, Salesforce and NVIDIA on their GitHub repositories. Vulnerable versions of these libraries allow for remote code execution (RCE) when a model file with malicious metadata is loaded.

Specifically, these libraries are:

  * [**NeMo**](https://github.com/NVIDIA-NeMo/NeMo/tree/main)**:** A PyTorch-based framework created for research purposes that is designed for the development of diverse AI/ML models and complex systems created by NVIDIA
  * [**Uni2TS**](https://github.com/SalesforceAIResearch/uni2ts): A PyTorch library created for research purposes that is used by Salesforce's Morai, a foundation model for time series analysis that forecasts trends from vast datasets
  * [**FlexTok**](https://github.com/apple/ml-flextok)**:** A Python-based framework created for research purposes that enables AI/ML models to process images by handling the encoding and decoding functions, created by researchers at Apple and the Swiss Federal Institute of Technology’s Visual Intelligence and Learning Lab



These libraries are used in popular models on HuggingFace with tens of millions of downloads in total.

The vulnerabilities stem from libraries using metadata to configure complex models and pipelines, where a shared third-party library instantiates classes using this metadata. Vulnerable versions of these libraries simply execute the provided data as code. This allows an attacker to embed arbitrary code in model metadata, which would automatically execute when vulnerable libraries load these modified models.

As of December 2025, we have found no malicious examples using these vulnerabilities in the wild. Palo Alto Networks notified all affected vendors in April 2025 to ensure they had a chance to implement mitigations or resolve the issues before publication.

  * NVIDIA issued [CVE-2025-23304](https://nvidia.custhelp.com/app/answers/detail/a_id/5686), rated High severity, and released a fix in NeMo version 2.3.2
  * The researchers who created FlexTok updated their code in June 2025 to resolve the issues
  * Salesforce issued [CVE-2026-22584](https://help.salesforce.com/s/articleView?id=005239354&type=1), rated High severity, and deployed a fix on July 31, 2025



These vulnerabilities were discovered by [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security), which is able to identify models leveraging these vulnerabilities and extract their payloads.

Additionally, Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

  * Cortex Cloud’s [Vulnerability Management](https://www.paloaltonetworks.com/cortex/cloud/vulnerability-management)
  * The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/resources/datasheets/unit-42-ai-security-assessment) can help organizations reduce AI adoption risk, secure AI innovation and strengthen AI governance.
  * If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).



**Related Unit 42 Topics** | [**Python**](https://unit42.paloaltonetworks.com/tag/python/), **[LLMs](https://unit42.paloaltonetworks.com/tag/llm/), [**Machine Learning**](https://unit42.paloaltonetworks.com/tag/machine-learning/)**  
---|---  
  
## AI/ML Model Formats

AI/ML training and inference pipelines depend on saving complex internal states, such as learned weights and architecture definitions. These internal states are saved as model artifacts, and the artifacts must be shared between producers and consumers. Libraries provide built-in mechanisms to serialize these artifacts.

Python libraries for AI/ML have long depended on functionality from the [pickle](https://docs.python.org/3/library/pickle.html) module in the Python standard library to store and load Python objects to and from files. This module serializes Python objects by creating a simple program to reconstruct the objects, and the pickle module is executed when the Python objects are loaded. Because the pickle module executes code when loading files, using it brings significant security risks.

The PyTorch library’s [file format](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html) simply embeds .pickle files in a container format. Other libraries like [scikit-learn](https://scikit-learn.org/stable/model_persistence.html) use .pickle or other extensions used for pickle (like [.joblib](https://joblib.readthedocs.io/en/latest/persistence.html#persistence)) on their own. Most popular AI/ML libraries clearly document these risks and provide mature mitigations to prevent the execution of unexpected code by default.

## Security Issues in New Model Formats

Newer formats have been developed to address the security issues of these pickle-based formats. These “safe” formats largely achieve this by only supporting the serialization of model weights or by representing pipelines as data instead of code, using formats like JSON. For example, HuggingFace’s [safetensors](https://huggingface.co/docs/safetensors/en/index) format only allows for the storage of model weights and a single JSON object to store model metadata.

Older formats have also moved away from relying on the pickle module. For example, PyTorch will only load model weights [by default](https://docs.pytorch.org/docs/stable/generated/torch.load.html). If pickle loading is enabled, PyTorch will only execute functions from a predefined [allow list](https://docs.pytorch.org/docs/stable/notes/serialization.html#torch.serialization.add_safe_globals) that should prevent the execution of arbitrary code.

While these newer formats and updates remove the ability to serialize pipelines as code, they do not make applications and libraries using these models impervious to traditional exploits. Security [researchers at JFrog](https://jfrog.com/blog/machine-learning-bug-bonanza-exploiting-ml-clients-and-safe-models/) have identified vulnerabilities in applications that use these formats using well-known techniques such as XSS and path traversal.

## Technical Analysis

While newer formats have removed the ability to store model state and configurations as code, researchers still have use cases for serializing that information. Because these libraries are large and the configurations of their classes can be complex, many libraries use third-party tools to accomplish this.

[Hydra](https://hydra.cc/) is a Python library maintained by Meta that is a tool commonly used to serialize model state and configuration information.

We identified three open-source AI/ML Python libraries used by models on HuggingFace that leverage Hydra to load these configurations from model metadata in a way that allows for arbitrary code execution:

  * **NeMo:** A PyTorch-based framework created for research purposes designed for the development of diverse AI/ML models and complex systems created by NVIDIA
  * **Uni2TS** : A PyTorch library created for research purposes used by Salesforce's Morai, a foundation model for time series analysis that forecasts trends from vast datasets
  * **FlexTok:** A Python-based framework created for research purposes that enables AI/ML models to process images by handling the encoding and decoding functions, created by researchers at Apple and the Swiss Federal Institute of Technology’s Visual Intelligence and Learning Lab



### Hydra

All the vulnerabilities we identified use the [hydra.utils.instantiate()](https://hydra.cc/docs/advanced/instantiate_objects/overview/) function, which is intended to “instantiate different implementations of an interface.”

The Hydra API takes as arguments a configuration object (like a Python dictionary or an [OmegaConf object](https://omegaconf.readthedocs.io/en/2.3_branch/usage.html)) that describes the target interface to [instantiate](https://dataplatform.cloud.ibm.com/docs/content/wsd/nodes/type_instantiation.html?context=cpdaas) and optional *args and **kwargs parameters to be passed to that interface. This configuration expects a _target_ value specifying the class or [callable](https://typing.python.org/en/latest/spec/callables.html) to instantiate, and an optional _args_ value defining arguments for _target_.

In each of the cases we identified, hydra.utils.instantiate() is only used to instantiate instances of library classes with simple arguments stored in metadata. Figure 1 shows an example of the metadata NeMo passes to the instantiate() function.

![A screenshot of computer code containing configuration parameters for a machine learning model.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-33851-170309-1.png)Figure 1. Metadata from a NeMo file.

What these libraries appear to have overlooked is that instantiate() doesn’t just accept the name of classes to instantiate. It also takes the name of any callable and passes it the provided arguments.

By leveraging this, an attacker can more easily achieve RCE using Python's built-in functions like [eval()](https://docs.python.org/3/library/functions.html#eval) and [os.system()](https://docs.python.org/3/library/os.html#os.system). In all the proofs of concept we used to test these vulnerabilities, we employed a payload using builtins.exec() as the callable and a string containing Python as an argument.

Since these issues were first identified, [Hydra has been updated](https://github.com/facebookresearch/hydra/commit/4d30546745561adf4e92ad897edb2e340d5685f0) to add a warning to its documentation stating that RCE is possible when using instantiate() and to add a simple block-list mechanism. This mechanism works by comparing the _target_ value against a list of dangerous functions like builtins.exec() before it is called.

Because this mechanism uses exact matches against import targets before they are imported, it is trivially evaded by using implicit imports from the Python standard library (e.g., [enum.bltns.eval](https://github.com/python/cpython/blob/3.14/Lib/enum.py#L2)) or from the target application (e.g., [nemo.core.classes.common.os.system](https://github.com/NVIDIA-NeMo/NeMo/blob/main/nemo/core/classes/common.py)). However, the Hydra documentation clearly states that this mechanism is not exhaustive and shouldn’t be relied on solely to prevent the execution of malicious code. As of January 2026, this block-list mechanism is not yet available in a Hydra release.

### NeMo

NVIDIA has been developing the [NeMo](https://github.com/NVIDIA/NeMo/tree/main) library since 2019, as a “scalable and cloud-native generative AI framework.” NeMo uses [its own file formats](https://docs.nvidia.com/nemo-framework/user-guide/24.07/playbooks/ptq.html#convert-nemo-checkpoint-to-qnemo-format) with the .nemo and .qnemo file extensions, which are simply TAR files containing a model_config.yaml file that stores model metadata along with a .pt file or a .safetensors file, respectively.

The main entry points for loading these .nemo model files are [restore_from()](https://github.com/NVIDIA/NeMo/blob/cd55157cb05e0a60066caf31e3354ff0e690b086/nemo/core/classes/common.py#L580) and [from_pretrained()](https://github.com/NVIDIA/NeMo/blob/cd55157cb05e0a60066caf31e3354ff0e690b086/nemo/core/classes/common.py#L711). There are several layers of abstraction, but ultimately, the [serialization](https://github.com/NVIDIA/NeMo/blob/cd55157cb05e0a60066caf31e3354ff0e690b086/nemo/core/classes/common.py#L472) mix-in is used to handle loading the model configuration once it has been loaded from the embedded model_config.yaml file. Figure 2 shows the vulnerable call to hydra.utils.instantiate().

![A screenshot of computer code from the Hydra API, showing conditional statements written in Python for handling configuration-based instantiation.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-35928-170309-2.png)Figure 2. Call to hydra.utils.instantiate() in NeMo.

At no point is any sanitization done on the metadata before it is passed to instantiate(). Because the call is made before the target model class begins its initialization, it is easy to create a model_config.yaml file with a working payload, as shown in Figure 3.

![A screenshot of code in a text editor, featuring lines written in Python. The code includes a print statement with "Hello world".](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-37858-170309-3.png)Figure 3. Example metadata triggering the NeMo vulnerability.

NeMo also integrates with HuggingFace and supports passing the name of a model hosted on HuggingFace to from_pretrained(), which is the way most NeMo models on HuggingFace appear to be used. This call is also vulnerable because once the model is downloaded from HuggingFace, the same code paths are followed.

As of January 2026, over 700 models on HuggingFace from a variety of developers are provided in NeMo format NeMo. Many of these models are among the most popular on HuggingFace, such as NVIDIA’s [parakeet](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2). This vulnerability appears to have existed [since at least 2020](https://github.com/NVIDIA/NeMo/commit/3206fafab654d9448297211ac50dfd4089338fe5).

The PyTorch format that NeMo extends supports code execution with embedded .pickle files, but it [clearly documents this](https://docs.pytorch.org/docs/stable/generated/torch.load.html#torch.load). This PyTorch format also disables arbitrary execution by default and offers several safeguards, such as [allowlisting usable modules](https://docs.pytorch.org/docs/stable/notes/serialization.html#torch.serialization.add_safe_globals) during the loading of .pickle files. NeMo does allow for the loading of embedded .pickle files inside of the PyTorch files embedded in .nemo files, but the built-in allow list mechanism in PyTorch should prevent arbitrary code execution.

NVIDIA acknowledged this issue, released a CVE record [CVE-2025-23304](https://nvidia.custhelp.com/app/answers/detail/a_id/5686) rated High severity and issued a fix in NeMo version 2.3.2.

To address this issue, NeMo added a [safe_instantiate](https://github.com/NVIDIA-NeMo/NeMo/blob/v2.5.2/nemo/core/classes/common.py#L165) function to validate the _target_ values from Hydra configurations before they are executed. This function recursively looks for _target_ values in the configuration and validates each one, which prevents using nested objects for RCE. A new [_is_target_allowed](https://github.com/NVIDIA-NeMo/NeMo/blob/v2.5.2/nemo/core/classes/common.py#L92) function first checks each _target_ value against an allow list of prefixes containing package names from NeMo, PyTorch and related libraries.

This prefix check alone would not be sufficient to prevent implicit imports of dangerous modules, as is the case for Hydra’s new block-list mechanism. However, NeMo additionally imports each target using Hydra and checks to see whether:

  * It is a subclass of an expected class
  * The import has a module name from an allow list of expected modules



By checking the actual imported value against these allow lists, NeMo ensures only expected targets are executed. For example, the target nemo.core.classes.common.os.system resolves to the posix module, which is clearly not part of the NeMo library.

### Uni2TS

In 2024, Salesforce’s AI research team published an article titled [Unified Training of Universal Time Series Transformers](https://arxiv.org/abs/2402.02592), which introduced a set of models that were published on [HuggingFace](https://huggingface.co/collections/Salesforce/moirai-r-models-65c8d3a94c51428c300e0742). This research and the use of these models depend on [uni2TS](https://github.com/SalesforceAIResearch/uni2ts), an open-source Python library that accompanied the Salesforce article.

The uni2TS library exclusively works with .safetensors files, which were [explicitly designed](https://github.com/huggingface/safetensors?tab=readme-ov-file#safetensors-1) to provide a safe alternative to model formats that allow for code execution. The safetensors format also does not explicitly support storing model or pipeline configurations.

To facilitate storing these configurations, libraries such as HuggingFace’s [huggingface_hub](https://huggingface.co/docs/huggingface_hub/main/en/guides/integrations#config) use a config.json file stored in a model’s repository. For models using classes in one of HuggingFace’s core ML libraries, this is done securely because only parameters that can be stored directly in JSON primitive types are used. These values are then passed to a predefined, hard-coded set of classes.

However, huggingface_hub provides a [PyTorchModelHubMixin](https://huggingface.co/docs/huggingface_hub/en/package_reference/mixins#huggingface_hub.PyTorchModelHubMixin) interface for creating custom model classes that can be integrated with the rest of their framework. As part of this interface, values are read from the packaged config.json file and passed to the model class.

This interface provides a little-used mechanism for registering functions called coders, which process specific arguments before they are passed to the class. The uni2TS library [leverages this mechanism](https://github.com/SalesforceAIResearch/uni2ts/blob/964240482e1f444987fe8ef8451871f1a57dd568/src/uni2ts/model/moirai_moe/module.py#L59) to decode the configuration of a specific argument using a call to hydra.utils.instantiate() before it is passed to the target class, shown in Figure 4.

![Screenshot of Python code including a function to decode distribution output and a class definition using PyTorch.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-39658-170309-4.png)Figure 4. Call to hydra.utils.instantiate() in uni2TS.

This code is executed when one of the published models is loaded using either MoraiModule.from_pretrained() or MoraiMoEModule.from_pretrained(). By adding our payload to the config.json file packaged with models using uni2TS as shown in Figure 5, RCE can be achieved when the model is loaded.

![Screenshot of a JSON script containing a Python print function code that displays "Hello world".](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-41521-170309-5.png)Figure 5. Example config.json metadata triggering uni2TS vulnerability.

The Salesforce models using these libraries have hundreds of thousands of downloads so far on Hugging Face. Several adaptations of these models have also been published on HuggingFace by other users. No evidence of malicious activity involving these models has been discovered.

Salesforce has acknowledged this issue, released a CVE record [CVE-2026-22584](https://help.salesforce.com/s/articleView?id=005239354&type=1), rated High severity, and issued a fix on July 31. This fix implements an allow list and a strict validation check to ensure only explicitly permitted modules can be executed.

### ml-flextok

Early in 2025, [Apple and the Swiss Federal Institute of Technology’s Visual Intelligence and Learning Lab (EPFL VILAB) published research](https://arxiv.org/abs/2502.13967) that introduced a supporting Python library called [ml-flextok](https://github.com/apple/ml-flextok). Like uni2TS, ml-flextok works exclusively with the safetensors format and extends PyTorchModelHubMixin. It can also load metadata from a config.json file included in the model repository. This library also supports loading configuration data from the .safetensors file directly, storing this information in the metadata section of the file under the __metadata__ key.

Because the safetensors format represents metadata as a dictionary with string keys and string values, and because the model configuration depends on lists of parameters, a secondary encoding must be used. Ml-flextok leverages Python as this secondary encoding and uses [ast.literal_eval()](https://github.com/apple/ml-flextok/blob/87d00cc8babf4a25ffce0f3f0c4d8b529d3d6abf/flextok/utils/checkpoint.py#L35) in the Python standard library to decode the metadata.

[As documented](https://docs.python.org/3/library/ast.html#ast.literal_eval), this function does not allow for arbitrary code execution but is susceptible to attacks causing memory exhaustion, excessive CPU consumption and process crashes. After the metadata has been decoded, ml-flextok directly passes it to [hydra.utils.instantiate()](https://github.com/apple/ml-flextok/blob/87d00cc8babf4a25ffce0f3f0c4d8b529d3d6abf/flextok/utils/checkpoint.py#L78).

If the model is loaded from HuggingFace, this metadata is read from config.json and is not double-encoded since complex structures are supported. This JSON data is loaded as a dictionary, and specific sections are passed directly to [instantiate()](https://github.com/apple/ml-flextok/blob/82379009ef7ee69bcda648fce8a1bbe3226ae377/flextok/flextok_wrapper.py#L264).

In both cases, payloads are created with names matching instantiate() arguments. Depending on whether the payload is added to the .safetensors file directly or in the packaged config.json file, the encoding and placement of the payload differ slightly, but the payload is still straightforward. Figure 6 shows a payload placed in a .safetensors file's metadata.

![A line of code displayed on a dark background that includes the text "payload", "target", and "builtins."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/word-image-43354-170309-6.png)Figure 6. Example of .safetensors metadata triggering uni2TS vulnerability.

As of January 2026, no models on HuggingFace appear to be using the ml-flextok library other than those models published by EPFL VILAB, which have tens of thousands of downloads in total.

Apple and EPFL VILAB have updated their code to resolve these issues by using [YAML](https://yaml.org/) to parse their configurations and adding an [allow list of classes](https://github.com/apple/ml-flextok/blob/28e0ffc24e590bdab0099d4a317b601cdc674a5b/flextok/utils/checkpoint.py#L23) they will pass to Hydra’s instantiate() function. They have also [updated their documentation](https://github.com/apple/ml-flextok/blob/28e0ffc24e590bdab0099d4a317b601cdc674a5b/README.md#model-zoo) to indicate that strings stored in model files are executed as code and only models from trusted sources should be loaded.

## Conclusion

Palo Alto Networks has not identified any model files leveraging these vulnerabilities for attacks in the wild. However, there is ample opportunity for attackers to leverage them.

It is common for developers to create their own variations of state-of-the-art models with different fine-tunings and quantizations, often from researchers unaffiliated with any reputable institution. Attackers would just need to create a modification of an existing popular model, with either a real or claimed benefit, and then add malicious metadata.

Prior to this finding, there was no indication that these libraries could be insecure or that only files from trusted sources should be loaded. HuggingFace does not currently make the contents of the metadata for these files easily accessible to users as it does in other cases (e.g., APIs referenced in .pickle files). Neither does it flag files using the safetensors or NeMo formats as being potentially unsafe.

Because the latest advances in this space often require code and not just model weights, there is a proliferation of supporting libraries. In October 2025, we identified over a hundred different Python libraries used by models on HuggingFace, almost 50 of which use Hydra in some manner. While these formats on their own may be secure, there is a very large attack surface in the code that consumes them.

### Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

  * [Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) is able to identify models leveraging these vulnerabilities and extract their payloads.
  * Cortex Cloud’s [Vulnerability Management](https://www.paloaltonetworks.com/cortex/cloud/vulnerability-management) identifies and manages base images for cloud virtual machine and containerized environments. This allows for identification and alerting of vulnerabilities and misconfigurations, then provides remediation tasks for identified base level container images. The Cortex Cloud Agent can also detect the runtime operations discussed within this article.
  * The [Unit 42 AI Security Assessment](https://www.paloaltonetworks.com/resources/datasheets/unit-42-ai-security-assessment) can help organizations reduce AI adoption risk, secure AI innovation and strengthen AI governance.



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

  * [Hydra documentation](https://hydra.cc/) – Hydra
  * [NeMo source code](https://github.com/NVIDIA/NeMo/tree/main) – NVIDIA-NeMo on GitHub
  * [uni2ts source code](https://github.com/SalesforceAIResearch/uni2ts) – SalesforceAIResearch on GitHub
  * [ml-flextok source code](https://github.com/apple/ml-flextok) – Apple on GitHub
  * [Libraries of NeMo models](https://huggingface.co/models?library=nemo) – HuggingFace



Back to top

### Tags

  * [Apple](https://unit42.paloaltonetworks.com/tag/apple/ "Apple")
  * [CVE-2025-23304](https://unit42.paloaltonetworks.com/tag/cve-2025-23304/ "CVE-2025-23304")
  * [CVE-2026-22584](https://unit42.paloaltonetworks.com/tag/cve-2026-22584/ "CVE-2026-22584")
  * [NVIDIA](https://unit42.paloaltonetworks.com/tag/nvidia/ "NVIDIA")
  * [Python](https://unit42.paloaltonetworks.com/tag/python/ "Python")
  * [PyTorch](https://unit42.paloaltonetworks.com/tag/pytorch/ "PyTorch")
  * [Salesforce](https://unit42.paloaltonetworks.com/tag/salesforce/ "Salesforce")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: Securing Vibe Coding Tools: Scaling Productivity Without Scaling Risk ](https://unit42.paloaltonetworks.com/securing-vibe-coding-tools/ "Securing Vibe Coding Tools: Scaling Productivity Without Scaling Risk")

### Table of Contents

  *   * Executive Summary
  * AI/ML Model Formats
  * Security Issues in New Model Formats
  * Technical Analysis
    * Hydra
    * NeMo
    * Uni2TS
    * ml-flextok
  * Conclusion
    * Palo Alto Networks Protection and Mitigation
  * Additional Resources



### Related Articles

  * [ The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications ](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/ "article - table of contents")
  * [ Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "article - table of contents")
  * [ Weaponizing the Protectors: TeamPCP’s Multi-Stage Supply Chain Attack on Security Infrastructure ](https://unit42.paloaltonetworks.com/teampcp-supply-chain-attacks/ "article - table of contents")



## Related Vulnerabilities Resources

![Pictorial representation of BeyondTrust vulnerability CVE-2026-1731. Digital art depicting a stylized mountain range with vibrant blue and red hues. The peaks are accentuated by glowing particles and an abstract, starry backdrop, creating a futuristic landscape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/14_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 19, 2026 #### [VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)

  * [Bash](https://unit42.paloaltonetworks.com/tag/bash/ "bash")
  * [CVE-2026-1731](https://unit42.paloaltonetworks.com/tag/cve-2026-1731/ "CVE-2026-1731")
  * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/ "VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability \(CVE-2026-1731\)")

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/AdobeStock_1020436911-786x440.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 17, 2026 #### [Critical Vulnerabilities in Ivanti EPMM Exploited ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)

  * [CVE-2026-1281](https://unit42.paloaltonetworks.com/tag/cve-2026-1281/ "CVE-2026-1281")
  * [CVE-2026-1340](https://unit42.paloaltonetworks.com/tag/cve-2026-1340/ "CVE-2026-1340")
  * [Ivanti](https://unit42.paloaltonetworks.com/tag/ivanti/ "Ivanti")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/ "Critical Vulnerabilities in Ivanti EPMM Exploited")

![Pictorial representation of CVE-2025-0921. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/06_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 30, 2026 #### [Privileged File System Vulnerability Present in a SCADA System ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)

  * [CVE-2025-0921](https://unit42.paloaltonetworks.com/tag/cve-2025-0921/ "CVE-2025-0921")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
  * [SCADA](https://unit42.paloaltonetworks.com/tag/scada/ "SCADA")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/ "Privileged File System Vulnerability Present in a SCADA System")

![Pictorial representation of a group of people interacting with a dynamic 3D holographic display of colorful, undulating data waves on a table.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/11_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) August 4, 2026 #### [The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software ](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Frontier AI](https://unit42.paloaltonetworks.com/tag/frontier-ai/ "Frontier AI")
  * [Vulnerability Exploitation](https://unit42.paloaltonetworks.com/tag/vulnerability-exploitation/ "Vulnerability Exploitation")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/ "The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software")

![Pictorial representation of AI-enabled autonomous cyberattacks. A digital illustration depicting abstract, interconnected data streams in vibrant colors on a dark blue background](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/AdobeStock_992950050-3-782x440.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) July 30, 2026 #### [Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks ](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)

  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")
  * [CVEs](https://unit42.paloaltonetworks.com/tag/cves/ "CVEs")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/ "Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks")

![Pictorial representation of three zero-day vulnerabilities in Siemens ROX II OT switches. Digital illustration of a global network featuring interconnected lines and nodes over a map of the world, highlighted with neon lights and digital elements.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/03_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) July 17, 2026 #### [Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy ](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/)

  * [Command injection](https://unit42.paloaltonetworks.com/tag/command-injection/ "Command injection")
  * [CVE-2025-40947](https://unit42.paloaltonetworks.com/tag/cve-2025-40947/ "CVE-2025-40947")
  * [CVE-2025-40948](https://unit42.paloaltonetworks.com/tag/cve-2025-40948/ "CVE-2025-40948")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/ "Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy")

![Pictorial representation of PAN-OS CVE-2026-0257. A vibrant city skyline at night, with tall skyscrapers and glowing digital beams extending into the sky, suggesting advanced technology and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/07_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) June 9, 2026 #### [Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/)

  * [CVE-2026-0257](https://unit42.paloaltonetworks.com/tag/cve-2026-0257/ "CVE-2026-0257")
  * [Vulnerability](https://unit42.paloaltonetworks.com/tag/vulnerability/ "vulnerability")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/ "Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257")

![Pictorial representation of CVE-2026-30300. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/06_Vulnerabilities_1920x900-3-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 6, 2026 #### [Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/)

  * [CVE-2026-0300](https://unit42.paloaltonetworks.com/tag/cve-2026-0300/ "CVE-2026-0300")
  * [EarthWorm](https://unit42.paloaltonetworks.com/tag/earthworm/ "EarthWorm")
  * [PAN-OS](https://unit42.paloaltonetworks.com/tag/pan-os/ "PAN-OS")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/ "Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution")

![Pictorial representation of a severe Linux vulnerability. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/05_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 5, 2026 #### [Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/)

  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [CVE-2026-31431](https://unit42.paloaltonetworks.com/tag/cve-2026-31431/ "CVE-2026-31431")
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/ "Kubernetes")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years")

![Pictorial representation of CVE-2023-33538. Abstract image of a glowing red Wi-Fi symbol on a circuit board, with intricate patterns and a futuristic appearance.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/04_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 16, 2026 #### [A Deep Dive Into Attempted Exploitation of CVE-2023-33538 ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/)

  * [Botnet](https://unit42.paloaltonetworks.com/tag/botnet/ "botnet")
  * [Command injection](https://unit42.paloaltonetworks.com/tag/command-injection/ "Command injection")
  * [CVE-2023-33538](https://unit42.paloaltonetworks.com/tag/cve-2023-33538/ "CVE-2023-33538")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/ "A Deep Dive Into Attempted Exploitation of CVE-2023-33538")

![Pictorial representation of BeyondTrust vulnerability CVE-2026-1731. Digital art depicting a stylized mountain range with vibrant blue and red hues. The peaks are accentuated by glowing particles and an abstract, starry backdrop, creating a futuristic landscape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/14_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 19, 2026 #### [VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)

  * [Bash](https://unit42.paloaltonetworks.com/tag/bash/ "bash")
  * [CVE-2026-1731](https://unit42.paloaltonetworks.com/tag/cve-2026-1731/ "CVE-2026-1731")
  * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/ "VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability \(CVE-2026-1731\)")

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/AdobeStock_1020436911-786x440.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 17, 2026 #### [Critical Vulnerabilities in Ivanti EPMM Exploited ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)

  * [CVE-2026-1281](https://unit42.paloaltonetworks.com/tag/cve-2026-1281/ "CVE-2026-1281")
  * [CVE-2026-1340](https://unit42.paloaltonetworks.com/tag/cve-2026-1340/ "CVE-2026-1340")
  * [Ivanti](https://unit42.paloaltonetworks.com/tag/ivanti/ "Ivanti")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/ "Critical Vulnerabilities in Ivanti EPMM Exploited")

![Pictorial representation of CVE-2025-0921. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/06_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 30, 2026 #### [Privileged File System Vulnerability Present in a SCADA System ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)

  * [CVE-2025-0921](https://unit42.paloaltonetworks.com/tag/cve-2025-0921/ "CVE-2025-0921")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
  * [SCADA](https://unit42.paloaltonetworks.com/tag/scada/ "SCADA")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/ "Privileged File System Vulnerability Present in a SCADA System")

![Pictorial representation of a group of people interacting with a dynamic 3D holographic display of colorful, undulating data waves on a table.](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/09/11_Myth-Busting_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2025/08/Insights-icon-white.svg)Insights](https://unit42.paloaltonetworks.com/category/insights/) August 4, 2026 #### [The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software ](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/)

  * [AI](https://unit42.paloaltonetworks.com/tag/ai/ "AI")
  * [Frontier AI](https://unit42.paloaltonetworks.com/tag/frontier-ai/ "Frontier AI")
  * [Vulnerability Exploitation](https://unit42.paloaltonetworks.com/tag/vulnerability-exploitation/ "Vulnerability Exploitation")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/frontier-ai-vulnerability-burst/ "The Frontier AI Vulnerability Burst: Industrializing Autonomous Zero-Day Discovery in Open-Source Software")

![Pictorial representation of AI-enabled autonomous cyberattacks. A digital illustration depicting abstract, interconnected data streams in vibrant colors on a dark blue background](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/AdobeStock_992950050-3-782x440.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) July 30, 2026 #### [Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks ](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)

  * [ChatGPT](https://unit42.paloaltonetworks.com/tag/chatgpt/ "ChatGPT")
  * [Claude code](https://unit42.paloaltonetworks.com/tag/claude-code/ "Claude code")
  * [CVEs](https://unit42.paloaltonetworks.com/tag/cves/ "CVEs")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/ "Chinese-Speaking Threat Actor Harnesses AI Models for Autonomous Cyberattacks")

![Pictorial representation of three zero-day vulnerabilities in Siemens ROX II OT switches. Digital illustration of a global network featuring interconnected lines and nodes over a map of the world, highlighted with neon lights and digital elements.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/03_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) July 17, 2026 #### [Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy ](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/)

  * [Command injection](https://unit42.paloaltonetworks.com/tag/command-injection/ "Command injection")
  * [CVE-2025-40947](https://unit42.paloaltonetworks.com/tag/cve-2025-40947/ "CVE-2025-40947")
  * [CVE-2025-40948](https://unit42.paloaltonetworks.com/tag/cve-2025-40948/ "CVE-2025-40948")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/ "Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy")

![Pictorial representation of PAN-OS CVE-2026-0257. A vibrant city skyline at night, with tall skyscrapers and glowing digital beams extending into the sky, suggesting advanced technology and connectivity.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/06/07_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) June 9, 2026 #### [Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257 ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/)

  * [CVE-2026-0257](https://unit42.paloaltonetworks.com/tag/cve-2026-0257/ "CVE-2026-0257")
  * [Vulnerability](https://unit42.paloaltonetworks.com/tag/vulnerability/ "vulnerability")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/ "Threat Brief: Active Exploitation of PAN-OS CVE-2026-0257")

![Pictorial representation of CVE-2026-30300. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/06_Vulnerabilities_1920x900-3-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 6, 2026 #### [Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/)

  * [CVE-2026-0300](https://unit42.paloaltonetworks.com/tag/cve-2026-0300/ "CVE-2026-0300")
  * [EarthWorm](https://unit42.paloaltonetworks.com/tag/earthworm/ "EarthWorm")
  * [PAN-OS](https://unit42.paloaltonetworks.com/tag/pan-os/ "PAN-OS")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/captive-portal-zero-day/ "Threat Brief: Exploitation of PAN-OS Captive Portal Zero-Day for Unauthenticated Remote Code Execution")

![Pictorial representation of a severe Linux vulnerability. Close-up of a woman wearing glasses and focusing intently on a computer screen.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/05/05_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) May 5, 2026 #### [Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/)

  * [Containers](https://unit42.paloaltonetworks.com/tag/containers/ "Containers")
  * [CVE-2026-31431](https://unit42.paloaltonetworks.com/tag/cve-2026-31431/ "CVE-2026-31431")
  * [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/ "Kubernetes")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/ "Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years")

![Pictorial representation of CVE-2023-33538. Abstract image of a glowing red Wi-Fi symbol on a circuit board, with intricate patterns and a futuristic appearance.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/04/04_Vulnerabilities_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) April 16, 2026 #### [A Deep Dive Into Attempted Exploitation of CVE-2023-33538 ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/)

  * [Botnet](https://unit42.paloaltonetworks.com/tag/botnet/ "botnet")
  * [Command injection](https://unit42.paloaltonetworks.com/tag/command-injection/ "Command injection")
  * [CVE-2023-33538](https://unit42.paloaltonetworks.com/tag/cve-2023-33538/ "CVE-2023-33538")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/exploitation-of-cve-2023-33538/ "A Deep Dive Into Attempted Exploitation of CVE-2023-33538")

![Pictorial representation of BeyondTrust vulnerability CVE-2026-1731. Digital art depicting a stylized mountain range with vibrant blue and red hues. The peaks are accentuated by glowing particles and an abstract, starry backdrop, creating a futuristic landscape.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/14_Overview_1920x900-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 19, 2026 #### [VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability (CVE-2026-1731) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/)

  * [Bash](https://unit42.paloaltonetworks.com/tag/bash/ "bash")
  * [CVE-2026-1731](https://unit42.paloaltonetworks.com/tag/cve-2026-1731/ "CVE-2026-1731")
  * [PowerShell](https://unit42.paloaltonetworks.com/tag/powershell/ "PowerShell")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/beyondtrust-cve-2026-1731/ "VShell and SparkRAT Observed in Exploitation of BeyondTrust Critical Vulnerability \(CVE-2026-1731\)")

![](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/02/AdobeStock_1020436911-786x440.jpeg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/07/top-threats.svg)High Profile Threats](https://unit42.paloaltonetworks.com/category/top-cyberthreats/) February 17, 2026 #### [Critical Vulnerabilities in Ivanti EPMM Exploited ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)

  * [CVE-2026-1281](https://unit42.paloaltonetworks.com/tag/cve-2026-1281/ "CVE-2026-1281")
  * [CVE-2026-1340](https://unit42.paloaltonetworks.com/tag/cve-2026-1340/ "CVE-2026-1340")
  * [Ivanti](https://unit42.paloaltonetworks.com/tag/ivanti/ "Ivanti")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/ "Critical Vulnerabilities in Ivanti EPMM Exploited")

![Pictorial representation of CVE-2025-0921. Digital illustration of a map of North America with interconnected glowing lines and dots symbolizing network connections across the continent.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/01/06_Vulnerabilities_1920x900-2-1-786x368.jpg)

[![ category icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/icon-threat-research.svg)Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/) January 30, 2026 #### [Privileged File System Vulnerability Present in a SCADA System ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)

  * [CVE-2025-0921](https://unit42.paloaltonetworks.com/tag/cve-2025-0921/ "CVE-2025-0921")
  * [Privilege escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/ "privilege escalation")
  * [SCADA](https://unit42.paloaltonetworks.com/tag/scada/ "SCADA")



[ Read now ![Right arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-right-arrow-withtail.svg) ](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/ "Privileged File System Vulnerability Present in a SCADA System")

  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)
  * ![Slider arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/slider-arrow-left.svg)



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/rce-vulnerabilities-in-ai-python-libraries/)