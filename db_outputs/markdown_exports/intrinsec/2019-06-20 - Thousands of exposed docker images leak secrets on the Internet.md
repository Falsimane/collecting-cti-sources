# Thousands of exposed docker images leak secrets on the Internet

- **Source :** intrinsec
- **URL :** https://www.intrinsec.com/en/docker-leak/
- **Date :** 2019-06-20

---

[et_pb_section admin_label=»section»] [et_pb_row admin_label=»row»] [et_pb_column type=»4_4″][et_pb_text admin_label=»Text»] 

Docker is now mainstream, everywhere and has invaded every business regardless of the sector of activity. This massive adoption, although the Docker backend technology is nothing new, is due to its ease of use which, as we are going to see, can **lead to leaks of secrets** when the concepts are misunderstood.

Docker is a containerization engine that allows you to package an application with all its dependencies. This template of ready-to-use application is called a **Docker image**. There are various types of images like web servers or databases. Images can stack and depend on each other. Images can be retrieved on public registries such as [**Dockerhub**](https://hub.docker.com), which currently **hosts more than 2.3 million of them**.

Like Github you can save your images for free at the expense of letting it publicly available to anyone and having to pay for a private hosting. There is also the possibility to maintain your [own Docker personal registry](https://hub.docker.com/_/registry).

Whether it is by unawareness of risk, accident or a budget wise decision, those public registries contain Docker images that shouldn't be left exposed. Many of them leak internal code, secrets or personal information. We estimate that roughly **10% of Docker images hosted on Dockerhub should not be publicly exposed as they are leaking sensitive data**.

> For the rest of this blog post, image refers to Docker image.

## Why analyze a Docker image?

The main purpose of analyzing images is to check the integrity and the version of its components, for potential CVEs, to use it safely.

Checking the legitimacy is to avoid a malicious image. This is what happened in May 2017 when the same user has released 17 backdoored images on Dockerhub, which contained a [cryptocurrency miner and has generated about $90,000 in value](https://threatpost.com/malicious-docker-containers-earn-crypto-miners-90000/132816/.).

To check that there are no CVEs listed on the kernel or frameworks used, there are solutions such as Aqua, which also owns their own Docker registry, which will scan the images uploaded/built by users.

Our scope here is focused on data leakage of publicly exposed images. Code repositories monitoring to find secrets have been largely publicized after several cases such as 2016 [Uber's data leak](https://www.uber.com/newsroom/2016-data-incident/) whereas leaks from Docker images stay under the radar, hence this blog post. To be clear, the leak comes from misuse of users and not from Dockerhub or Docker platform as they prevent risks.

## What's inside a Docker image?

A Docker image is an archive containing, among other things, the filesystem necessary to make the application work. It is structured in layers representing each instruction given in the Dockerfile during the build of the given image.

For example if I want to kwow the instructions made to build the mysql image:
    
    
    docker pull mysql && docker history mysql

To explore in details the image you can export it as a tar archive and dive into layers
    
    
    docker save mysql | tar xvf - --one-top-level=mysql && ls mysql/*/layer.tar

Fortunately a wonderful tool has been released, by [Alex Goodman](https://twitter.com/alexgoodman87), to explore each layer in an image, called `[**dive**](https://github.com/wagoodman/dive)`. You can see what are the new files, those that have been edited or removed. In backend, `**dive**` also uses the tar archive of the image and proceeds on a differential of each layer.

![](https://www.intrinsec.com/wp-content/uploads/2019/05/docker_image_dive.png)Thanks to its nice UI, you can spot easily  _added/updated/removed_ files

## What could go wrong?

### Secrets embedded in code

The first bad practice is to embed secrets, like AWS key or Dropbox access token, inside your code. It is not relative to Docker but to secure development in general. When you copy your code inside the image you also copy the secrets and if the image go public your secrets too.

![](https://www.intrinsec.com/wp-content/uploads/2019/06/docker_image_inside_code.png)MongoDB database credentials inside code

> Remediation: Separate your secrets and configurations data from your code. Make the secrets as arguments or environment variables to be given when you run your image.

### Secrets in environment variables

Ok so you have separated your secrets and configuration files from your code by setting them in environment variables. But you specify this environment variables in you Dockerfile and again anyone can see them, either by printing history of commands used to build the image or by printing environment variables inside a running instance of the image.
    
    
    Docker history # OR docker run printenv

![](https://www.intrinsec.com/wp-content/uploads/2019/06/docker_image_printenv-3.png)Sensitive environment variables accessible in image

> Remediation: Set sensitive environment variables when running your image with the option `-e` or compiled in a file with `--env-file`.

###  A (secrets) file copied into you docker image

You now are using an environment file name `.env` containing all your secrets, in your work directory to give at run command but you forgot to ignore it when using `COPY` command in your Dockerfile (like copy your code to your image). So anyone can access those secrets which are copied in your docker image.

![](https://www.intrinsec.com/wp-content/uploads/2019/06/docker_image_file_env.png)All kinds of secrets over here

When you wildly copy your working directory, you can also copy the `.git` directory or non-code data files that were not meant to be in the image.

  * ![](https://www.intrinsec.com/wp-content/uploads/2019/06/docker_image_sensitive_data-1.png)Files that seem interesting to look at
  * ![](https://www.intrinsec.com/wp-content/uploads/2019/06/docker_image_xlsx-1024x408.png)Customer data



> Remediation: Use a `.dockerignore` specifying files to ignore when using build context like `.git` gold .`approx` files. For files that are not expected in the project code and so in `.dockerignore`, like result files or sample of production data to test, you may provide a script in the CI/CD chain to check the presence and alert on files with improbable extensions (`xlsx`, `docx` …) or suspicious filenames (`customer_name`, `financial_results`, …) according to local practices.

### Best practice

When managing sensitive data, the best thing to do is to use [Docker secrets](https://docs.docker.com/engine/swarm/secrets) or a third-party solution like [Vault](https://www.vaultproject.io).

###  Your code, your value

You are now safe, your sensitive data is not exposed within you image but must it be exposed to anyone on Internet? You took care not to use a public Github repository for your code but you just uploaded your image containing your code in a publicly exposed Docker repository. 

![](https://www.intrinsec.com/wp-content/uploads/2019/06/docker_image_code.png)

> Remediation: You must use a private repository for you image or hosting your own Docker registry, obviously not exposed to Internet.

![](https://www.intrinsec.com/wp-content/uploads/2019/05/dockerhub_private.png)Any new repository is public by default

##  Attack scenarios

### The opportunist

Goal is to target many images to get low-hanging fruit secrets, like Amazon AWS key or other cloud/computing access tokens, by grepping them in files that he will then be able to monetize (mining cryptocurrencies) or reuse to**explore accessible valuable data (S3 buckets, etc.)**.

How? By targeting images whose names contain words like `prod`, `backup`, `site` and it is best when meeting the possessive adjective `my` like `mybackup`. Tips: keep only little popularity images (< 50 downloads).

This way we target individuals and small structures, those are the ones who are probably less sensitive to security and therefore to good Docker practices.

However, largest structures are not spared, as shown in the case of Vine in March, 2016, where a researcher [found an image containing all their source codes](https://avicoder.me/2016/07/22/Twitter-Vine-Source-code-dump/) and was awarded a $10,080 bounty for his find.

This approach can be easy to automate for a malicious actor and therefore the **importance of monitoring new/updated publicly images that may concern your business to react in time**.

### The persistent

Someone targeting a (sector) business, will investigate deeply all published images related to the targeted company to find internal codes, secrets and to understand how it works. He aims at spying or preparing attack.

It is the same recognition we do for images that may concern our customers to warn them before someone exploits it.

##  Some figures to conclude

Beyond the automated approach to provided industrial and continuous monitoring provided by Intrinsec, for the purpose of this blog post, **we manually reviewed 100 random Docker images**. Yes, it is a small sample but it is more to have an order of magnitude rather than a precise metric.

  * **10% containing sensitive data** : credentials, private keys, API tokens and personal information of users or customer
  * **15% are images with bad practices but no sensitive data** : variable configuration, git folder, etc.
  * **48% seems legitimate** : absence of sensitive data and bad practices
  * **27% are inaccessible images** gone private or removed

![](https://www.intrinsec.com/wp-content/uploads/2019/06/pie_chart-1.png)

So if we only keep publicly pullable images, **14% of them should absolutely not be exposed and leak sensitive data**.

If this subject is of interest to you to protect your business, we would be glad to discuss with you about our threat intell services.

We would like to thank Vincent Delair and Jacques Lebeau for their help  
  
Authors:  
Guillaume Granjus: [@ggranjus](https://twitter.com/ggranjus)   
Charles Hiezely

[/et_pb_text][/et_pb_column] [/et_pb_row] [/et_pb_section] 

#### Articles by category 

Select a category News Vulnerability notice Analysis Report CERT SSI Council Cyber Threat Intelligence Engineering Safety Assessment Event Partnership Research and Development Red Teaming part-time CISO Soc as a Service SOC Operational Security Testimonials Penetration test Threat Intelligence Report Security Watch