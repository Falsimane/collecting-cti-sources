# PowerShell: the story of collaboration between AI and CTI teams - HarfangLab

- **Source :** harfanglab
- **URL :** https://harfanglab.io/insidethelab/owershell-collaboration-ia-cti/
- **Date :** 2023-03-07

---

At HarfangLab, the Artificial Intelligence (AI) and Cyber Threat Intelligence (CTI) teams can combine their strengths to prevent and detect threats. In the past year, we have worked on all of the aspects of AI to enhance our malware detection, mostly working with new types of data to improve our capabilities. Working on PowerShell scripts is a good example of a successful exchange. Let’s see how that went.

Securing computers is becoming more and more challenging, mainly with the increase of fileless malware attacks. The infection chain of these attacks entails a few – if any – files. Most of the infection part happens in the memory space (instead of the file system), which makes it easier to evade detection.

While tools like Microsoft PowerShell are legitimate, they can be used maliciously. Attackers can use PowerShell to drop malwares, to steal sensitive data, to delete files and even to gain unauthorized access to systems. These attacks led us, in addition to the rules written by the CTI, to explore how AI can contribute to their detection.

## **PowerShell scripts: an interesting source of data**

To begin the project, we needed to understand the PowerShell language and how scripts could be efficiently retrieved. The CTI team was here to provide the expertise needed in both of these steps.

### Understanding PowerShell

Microsoft PowerShell is an open source framework based on .NET. It is not only a shell but also an interpreted language with the ability to run scripts, which are a set of commands. It can be very powerful for automating administrative tasks and managing Windows operating systems. Beyond Windows, PowerShell also supports other platforms such as Linux and macOS.

### Collect PowerShell scripts to build a robust dataset

PowerShells are tracked in the Windows event log when you activate ScriptBlockLogging on the machine. Windows event log is an in-depth record of events related to the system, security, and application stored on a Windows operating system. It is used to monitor the system. You can see event logs in the event viewer.In our case, we’re looking at events with id `4104` and source name `Microsoft-Windows-PowerShell`.

To build our dataset, we went through a lot of public databases. Most of them are on Github, user [danielbohannon](https://github.com/danielbohannon) has a great collection of commands to generate malicious PowerShell and we found another dataset that comes from the paper [ _Effective method for detecting malicious PowerShell scripts based on hybrid features_](https://www.sciencedirect.com/science/article/abs/pii/S0925231221005099?via%3Dihub)by Fang Yong, Zhou Xiangyu and Huang Cheng. To extend our dataset, we asked the CTI which known malware families use PowerShell scripts. After collecting our data, the model can be built.

## **Detecting malicious PowerShell scripts: an iterative development between the CTI and AI teams**

The AI team works on a malicious PowerShell detection module powered by machine learning. It works on PowerShell files and gives, for each sample, a “score of potential maliciousness”. During the reflection of the project, the AI team worked in collaboration with the CTI team to understand how often PowerShell scripts are used in attacks and how recognize parts of a script that are malicious.

### Converting PowerShell scripts to Abstract Syntax Tree (AST)

We needed to find a way to represent PowerShell scripts, so that we can easily extract features from them. The AST conversion is a PowerShell feature for code analysis. It essentially breaks down the code into a hierarchical tree with each element representing a part of the tree.

Let’s have an example with a simple script containing one command: `Get-Date.ps1`. We can use two methods (demonstrated below) to convert the PowerShell script to an `AST` : from the file or from the source code.
    
    
    # get AST object from script file
    $script = Get-Date.ps1
    $AST = [System.Management.Automation.Language.Parser]::ParseFile($script, [ref]$null, [ref]$null)
    
    # get AST object from PowerShell code
    $code = 'Get-Date -Format "dddd dd/MM/yyyy HH:mm K"'
    $AST = [System.Management.Automation.Language.Parser]::ParseInput($code, [ref]$null, [ref]$null)

To show the graphical representation of an `AST`object, you can use the `ShowPSAst` of PowerShell.
    
    
    # install ShowPSAst module
    Install-Module -Name ShowPSAst -Scope CurrentUser -Force
    # import commands from ShowPSAst  module
    Import-Module ShowPSAst
    # show the AST of a script or script module
    Show-Ast Get-Date.ps1

![](https://harfanglab.io/medias/2023/12/ast-explanation2.png) AST representation of the command Get-Date -Format “dddd dd/MM/yyyy HH:mm K”

### Building our model to detect malicious PowerShell scripts

Our algorithm works in three steps :

  1. The PowerShell script is converted to an AST.
  2. Relevant features are computed and extracted from the given AST, thus giving a numerical representation of the file.
  3. This representation is then submitted to our classification model, which is composed of a set of decision trees, trained using the [_gradient boosting_ technique](https://towardsdatascience.com/gradient-boosting-classification-explained-through-python-60cc980eeb3d) _._



We gathered a list of PowerShell commands and we selected the 2000 most frequent words as vocabulary. To extract features, we use term frequency-inverse document frequency [TF-IDF ](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) _(term frequency-inverse document frequency_), which is a statistical measure that evaluates how relevant a word is to a given file in a collection of files.

![](https://harfanglab.io/medias/2023/12/chocard-process1-2048x241-1.png) Scheme of the use of our algorithm

### Work with the CTI team to optimize results

When analyzing unseen (and unlabeled) PowerShell scripts, it is hard to determine whether they are malicious or benign. That’s where experts come in: the CTI team can efficiently qualify our data and provide feedback on the effectiveness of this algorithm. On a subset of data, when our model found potential malicious PowerShell scripts, we sent them to the CTI in order to analyze them. Thanks to these feedbacks, we were able to improve our dataset and identify the number of false positives.

After having validated the design and performance of our model, we decided to test it against some real production data. We gathered PowerShell scripts from telemetry data (from windows event logs) and we inspected them with our model. Our model identified some PowerShell scripts that were not detected by our rule-based and signature-based engine.

What’s really interesting in this approach is that in order to create new rules, the CTI team has to constantly study scripts, sometimes thousands of them. Using our model, we can reduce this analysis to a dozen files, finding among the batch which are really malicious. The process of writing new rules can therefore be lightened.

## **Conclusion: identifying threats and increasing added value with AI**

Collaboration between AI and CTI teams is the key in the creation of new models. In our scenario, the CTI team identified a resource where AI could bring value: PowerShell scripts. With their help, our team was able to qualify data and improve the model, resulting in a robust detection of malicious PowerShell scripts. The next step in this collaboration is to see how well our model can help the CTI write new rules. We also need to qualify the false positives in our model, to make sure we are providing a reliable tool to the team.

It’s always when you leverage each other’s strengths that you build the most powerful defense.

[ ![AI: Deep Learning & batch normalization](https://harfanglab.io/medias/2023/12/boxes-424x283.jpg) Embedding images and executable files Embedding images into a lower-dimensional representation is a blooming research field in Deep Learning. With a small vector representation of each image, many new tasks can be easily done afterward such as zero-shot learning and… ](https://harfanglab.io/insidethelab/normalisation-batch-data/)[ ![AI-Image-Manipulation](https://harfanglab.io/medias/2023/12/ai-image-manipulation-424x283.jpg) Removing image manipulation approximations from image-like modelling in Deep Learning Deep Learning for image analysis With Convolutional Neural Networks (CNN) in Deep Learning, the computer vision field has had significant breakthroughs in recent years in the processing and classification of… ](https://harfanglab.io/insidethelab/image-manipulations-deteriorate-deep-learning/)[ ![ITL-Machine-learning](https://harfanglab.io/medias/2023/12/itl-machine-learning-424x283.jpg) Why bother with strings? When analyzing a new sample found “inthewild”, it may make sense to extract the strings within it to identify IP addresses, domains, log files or C&C server signatures. For example, if an Artificial Intelligence model such… ](https://harfanglab.io/insidethelab/using-machine-learning-to-find-malicious-strings-in-a-file/)[ ![Cybersecurity - Workspace Detection and Protection Platform - Artifical Intelligence Engine](https://harfanglab.io/medias/2023/12/graph1-1.png) Description Ashley Binaries is a malware detection module powered by machine learning and deep learning. It works on executable files (PE files for windows and ELF for linux) and gives, for each sample, a “score of potential maliciousness”. This state-of-the-art… ](https://harfanglab.io/insidethelab/hl-ai-binaries-versions/)