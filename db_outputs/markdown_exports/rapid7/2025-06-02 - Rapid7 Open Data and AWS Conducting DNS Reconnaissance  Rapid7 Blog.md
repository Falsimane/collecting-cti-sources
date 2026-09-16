# Rapid7 Open Data and AWS: Conducting DNS Reconnaissance | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2018/10/16/how-to-conduct-dns-reconnaissance-for-02-using-rapid7-open-data-and-aws/
- **Date :** 2025-06-02

---

[Project Sonar](/research/project-sonar/) regularly performs active scans of the internet to understand global exposure and common vulnerabilities. One of the most popular datasets Sonar produces is the [FDNS ANY dataset](https://opendata.rapid7.com/sonar.fdns_v2/), which performs ANY queries against domain names. With this information, researchers and organizations can understand DNS misconfigurations, such as malicious and hijackable domains, as well as get a sense of internet-facing surface area.

We’re happy to announce that a subset of the Sonar data is now available on Amazon Web Services (AWS). In this post, we will show how you can use [AWS Athena](https://aws.amazon.com/athena/) to quickly and easily perform normally expensive and time-consuming domain enumeration, costing no more than a few cents.

**Disclaimer:** If you don’t have an [AWS account](https://portal.aws.amazon.com/billing/signup#/start) already, you will need to get one. Also, working through this document will incur charges against your AWS account related to AWS Athena and AWS S3 storage fees.

## Getting Athena ready to analyze the dataset

If you go to s3/buckets/rapid7-opendata/fdns/any/and take a look at the buckets where the data is stored in S3, you’ll notice the data is stored in compressed parquet formats. This is great for storage, but not the most straightforward for exploring the data. Luckily, there’s AWS Athena, which provides a quick and painless way to query the data.

**Note:** You can also query this data through the aws cli:

aws s3 ls s3://rapid7-opendata/ --no-sign-request

![Raw_Parquet_Data.jpg](https://www.rapid7.com/cdn/images/bltf4edf75865b369e6/683de76dca9dfcadbd526862/Raw_Parquet_Data.jpg)

AWS Athena is a serviceless query service that will allow you to explore over 90 GB worth of FDNS ANY data efficiently using standard SQL. With Athena’s affordable pricing model, you only pay for the data scanned by the queries you run.

To start, you will need an AWS account with access to Athena. Once you have that, you can begin to register the Sonar fdns_any dataset with your Athena instance:

  * Open up the Athena console, and make sure your are pointed to US-EAST-1 Region (or wherever you’re hosted)
  * Next, go in the query editor copy and execute the following table definition:


    
    
    CREATE EXTERNAL TABLE IF NOT EXISTS rapid7_fdns_any (
      `timestamp` timestamp,
      `name` string,
      `type` string,
      `value` string 
    ) PARTITIONED BY (
      date string 
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
    WITH SERDEPROPERTIES (
      'serialization.format' = '1'
    ) LOCATION 's3://rapid7-opendata/fdns/any/v1/'
    TBLPROPERTIES ('has_encrypted_data'='false');
    

The columns are defined as follows:

  * **Timestamp:** The time when this response was received in seconds since the epoch
  * **Name:** The record name
  * **Type:** The record type
  * **Value:** The response received for a record of the given name and type



You can find more about the schema of the dataset [here](https://opendata.rapid7.com/sonar.fdns_v2/).

![Athena_Table.jpg](https://www.rapid7.com/cdn/images/blt5a04bfe8ef18fea3/683de7a670aa9548fffe322c/Athena_Table.jpg)

Now you have a table called rapid7_fdns that reflects the parquet data in the s3 buckets! To help keep the costs low when querying, we’ve partitioned the data via date. Datasets will be updated once a month, so to make sure your table is using the latest partitions. It’s a good idea to repair the table both now and periodically as you continue to use the dataset.

**msck repair table rapid7_fdns_any**

![Repair_Table.jpg](https://www.rapid7.com/cdn/images/blt7d6d50448f928ce0/683de7c87f86031a912309a8/Repair_Table.jpg)

Now that we have the repaired the table to use the latest partitions, let’s query a couple of rows of the data and see what it looks like:

**SELECT * FROM rapid7_fdns_any LIMIT 10;**

![Basic_SELECT_query-1.jpg](https://www.rapid7.com/cdn/images/blt64b5ef3990215da0/683de7e570aa954051fe3244/Basic_SELECT_query-1.jpg)

## Deeper analysis with FDNS

Now that we can do some basic queries on the data, let’s go into a couple of case studies to show how you can use the FDNS ANY dataset get more meaningful results.

### Case study No. 1: Discover internet-facing infrastructure for a specific domain

"Getting the list of all subdomains can help find domains that are susceptible to hijacking or are pointing to malicious destinations."

An important application of the data we can use is discovering all DNS records for a wildcard domain name. This allows us to see all the internet-facing infrastructure for a specific domain as well as the list of all subdomains. Getting the list of all subdomains can help find domains that are susceptible to hijacking or are pointing to malicious destinations. Such information is invaluable for security researchers, pen testers, and anyone looking to secure their own domain.

With the query below, we can use the dataset to find all the subdomains of example.com from the most recent month.

**> > SELECT * FROM rapid7_fdns_any WHERE name LIKE '%.example.com' AND date = (SELECT MAX(date) from rapid7_fdns_any);**

![Domain_Infrastructure.jpg](https://www.rapid7.com/cdn/images/blta801de3137a0875e/683de7ff30073e7700eb1a86/Domain_Infrastructure.jpg)

Removing the date condition from the WHERE clause will also allow you to see more of the historical DNS mappings as opposed to what’s being used currently. Please be aware that removing the date condition from the WHERE clause will cause more data to be scanned, which will increase the cost of running the query.

### Case study No. 2: Looking for offsite hijacking

We can continue to modify our query for potentially hijackable domains. To do this, we need to limit our query search to CNAME records. CNAME records show domains that resolve to another domain called a canonical domain. Often, many of these canonical domains are no longer in use, and a potential attacker could register and use these domains for malicious intent.

One query for finding these orphaned CNAMES for cleanup could be:

SELECT * FROM rapid7_fdns_any WHERE name NOT LIKE '%.herokuapp.com' AND value LIKE '%.herokuapp.com' AND type = 'cname' LIMIT 150;

### A case study for you: Domain generation algorithms

Domain generation algorithms are used by malware authors to better enable the survivability of their botnets. Algorithms are used to compute new domains, which the malware will then use to communicate with the command and control (CnC) server.

A description of DGAs and sample algorithms can be found on [Wikipedia](https://en.wikipedia.org/wiki/Domain_generation_algorithm), but many organizations and researchers have also written on this topic.

The Rapid7 Sonar Data Forward DNS dataset can be used to study DGAs. A challenge to the reader is to perform a study on DGAs. Let us know where you get!

## Conclusion

We hope the uses case above help you get started using the data. The files are available directly in parquet format at : s3://rapid7-opendata/fdns/any/v1/. To find out more on the DNS records and the other network information that Sonar provides, check out [Rapid7 OpenData](https://opendata.rapid7.com/). We appreciate any community analysis results and hope to collaborate with you in the future. Don’t hesitate to contact us at [[email protected]](/cdn-cgi/l/email-protection#c7b5a2b4a2a6b5a4af87b5a6b7aea3f0e9a4a8aa) with any further questions!

_Image source:_[_Flickr_](https://www.flickr.com/photos/30661646@N00/231526044)

## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)
  * [AWS](/blog/tag/aws-cloud-security/)