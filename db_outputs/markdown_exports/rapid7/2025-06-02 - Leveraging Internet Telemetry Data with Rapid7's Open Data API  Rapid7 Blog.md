# Leveraging Internet Telemetry Data with Rapid7's Open Data API | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2019/02/13/level-up-your-internet-intelligence-using-the-rapid7-open-data-api-and-r/
- **Date :** 2025-06-02

---

Last year, Rapid7 Labs launched the [Open Data Portal](https://opendata.rapid7.com/) on our [Insight platform](/products/insight-platform/), putting our planetary-scale internet telemetry data into the hands of data scientists, threat intelligence analysts, enterprise teams, and individual security researchers all _for free_. All you need to do is request access (we do some light vetting in an effort to ensure the data goes into the hands of defenders, not attackers), and once you gain access to the platform, you can search for and select from our wide array of datasets.

Interactive use is all well and good, but we also provide [API access](https://opendata.rapid7.com/apihelp/) that makes it possible to set up automated operational or data science workflows. We recently published an R package, ropendata, to access the Rapid7 Sonar Data API on [CRAN](https://cran.r-project.org/web/packages/ropendata/).

Let's take a look at how you can use ropendata in R to search for available studies, download datasets, and explore the data.

First, you'll need to install the package, which is as simple as:
    
    
    install.packages("ropendata")
    

Now, we grab the current list of studies and take a look at them:
    
    
    library(ropendata)
    library(tidyverse)
    
    studies <- list_studies()
    
    glimpse(studies)
    
    
    
    ## Observations: 13
    ## Variables: 15
    ## $ uniqid               <chr> "sonar.ssl", "sonar.fdns_v2", "sonar.cio", "sona…
    ## $ name                 <chr> "SSL Certificates", "Forward DNS (FDNS)", "Criti…
    ## $ short_desc           <chr> "X.509 certificate metadata observed when commun…
    ## $ long_desc            <chr> "The dataset contains a collection of metadata r…
    ## $ study_url            <chr> "https://github.com/rapid7/sonar/wiki/SSL-Certif…
    ## $ study_name           <chr> "Project Sonar: IPv4 SSL Certificates", "Forward…
    ## $ study_venue          <chr> "Project Sonar", "Project Sonar", "RSA Security …
    ## $ study_bibtext        <chr> "", "", "", "", "", "", "", "", "", "", "", "", …
    ## $ contact_name         <chr> "Rapid7 Labs", "Rapid7 Labs", "Rapid7 Labs", "Ra…
    ## $ contact_email        <chr> "[[email protected]](/cdn-cgi/l/email-protection)", "[[email protected]](/cdn-cgi/l/email-protection)", "r…
    ## $ organization_name    <chr> "Rapid7", "Rapid7", "Rapid7", "Rapid7", "Rapid7"…
    ## $ organization_website <chr> "http://www.rapid7.com", "http://www.rapid7.com/…
    ## $ created_at           <chr> "2018-06-07", "2018-06-20", "2018-05-15", "2018-…
    ## $ updated_at           <chr> "2019-02-09", "2019-02-09", "2013-04-01", "2018-…
    ## $ sonarfile_set        <list> [<"20190209/2019-02-09-1549672918-https_get_208…
    

If you've ever pursued the Sonar Data portal, the metadata elements will look familiar. Even if all of this is brand-new territory, you can see that you have access to the study name, description, and timestamps of study creation and update dates. Let's take a look at the main study categories:
    
    
    select(studies, name, uniqid) %>% 
      arrange(name) %>% 
      print(n=20)
    
    
    
    ## # A tibble: 13 x 2
    ##    name                                         uniqid                 
    ##    <chr>                                        <chr>                  
    ##  1 Critical.IO Service Fingerprints             sonar.cio              
    ##  2 Forward DNS (FDNS)                           sonar.fdns_v2          
    ##  3 Forward DNS (FDNS) -- ANY 2014-2017          sonar.fdns             
    ##  4 HTTP GET Responses                           sonar.http             
    ##  5 HTTPS GET Responses                          sonar.https            
    ##  6 More SSL Certificates (non-443)              sonar.moressl          
    ##  7 National Exposure Scans                      sonar.national_exposure
    ##  8 Rapid7 Heisenberg Cloud Honeypot cowrie Logs heisenberg.cowrie      
    ##  9 Reverse DNS (RDNS)                           sonar.rdns_v2          
    ## 10 Reverse DNS (RDNS) -- 2013-2017              sonar.rdns             
    ## 11 SSL Certificates                             sonar.ssl              
    ## 12 TCP Scans                                    sonar.tcp              
    ## 13 UDP Scans                                    sonar.udp
    

For this introductory post, we're going to use one of our smaller datasets, which should make it easier to work with the data, especially for those new to internet scan data and security data analysis in general.

Let's see what Rapid7 Labs has been doing in the UDP space recently:
    
    
    filter(studies, uniqid == "sonar.udp") %>% 
      pull(sonarfile_set) %>% 
      flatten_chr() %>% 
      head(10)
    
    
    
    ##  [1] "2019-02-04-1549303426-udp_ubiquiti_discovery_10001.csv.gz"
    ##  [2] "2019-02-04-1549300200-udp_coap_5683.csv.gz"               
    ##  [3] "2019-02-04-1549296290-udp_ripv1_520.csv.gz"               
    ##  [4] "2019-02-04-1549292633-udp_chargen_19.csv.gz"              
    ##  [5] "2019-02-04-1549289039-udp_qotd_17.csv.gz"                 
    ##  [6] "2019-02-04-1549285686-udp_dns_53.csv.gz"                  
    ##  [7] "2019-02-04-1549284002-udp_wdbrpc_17185.csv.gz"            
    ##  [8] "2019-02-04-1549281938-udp_mssql_1434.csv.gz"              
    ##  [9] "2019-02-04-1549281910-udp_bacnet_rpm_47808.csv.gz"        
    ## [10] "2019-02-04-1549271093-udp_upnp_1900.csv.gz"
    

Ah, that Ubiquiti study was pretty fun and informative and the [blog post we wrote about it](/blog/post/2019/02/01/ubiquiti-discovery-service-exposures/) garnered a great deal of attention. Let's see how big it is:
    
    
    get_file_details(
      study_name = "sonar.udp", 
      file_name = "2019-02-04-1549303426-udp_ubiquiti_discovery_10001.csv.gz"
    ) %>% 
      glimpse()
    
    
    
    ## Observations: 1
    ## Variables: 4
    ## $ name        <chr> "2019-02-04-1549303426-udp_ubiquiti_discovery_10001.csv.g…
    ## $ fingerprint <chr> "1669feb358ef7bc13fb28915c95b8a315770ed67"
    ## $ size        <int> 39740649
    ## $ updated_at  <chr> "2019-02-04"
    

Sweet! It's only around 38 MB. The get_file_details() function has an include_download_link parameter that defaults to FALSE, since every time you generate a download link, it goes against your download credits. Those credits exist primarily to prevent abuse from errant automation scripts and the limits are fairly high, so it's unlikely you'll run into any issues. So, we'll re-issue the call for details, include the link, and download the study data:
    
    
    get_file_details(
      study_name = "sonar.udp", 
      file_name = "2019-02-04-1549303426-udp_ubiquiti_discovery_10001.csv.gz",
      include_download_link = TRUE
    ) -> ubi_dl 
    
    download.file(ubi_dl$url[1], "~/Data/019-02-04-1549303426-udp_ubiquiti_discovery_10001.csv.gz")
    

Since it's a CSV, there's nothing super-special we need to do to read it into R. We're using readr::read_csv() here but you may want to give data.table::fread() a try as well since this is going to end up being a structure with about half a million rows, including payload data, and fread() is super fast.
    
    
    read_csv(
      file = "~/Data/2019-02-04-1549303426-udp_ubiquiti_discovery_10001.csv.gz",
      col_types = "dcdcdddc"
    ) -> ubi_df
    
    select(ubi_df, -daddr)
    
    
    
    ## # A tibble: 503,997 x 7
    ##    timestamp_ts saddr     sport dport  ipid   ttl data                          
    ##           <dbl> <chr>     <dbl> <dbl> <dbl> <dbl> <chr>                         
    ##  1   1549303435 177.38.2… 10001 10001     0    51 0100009302000a002722bccf9db12…
    ##  2   1549303435 176.122.… 10001 10001 25312    45 0100009902000a0027222c17d4b07…
    ##  3   1549303435 177.44.1… 10001 10001     0    47 0100009302000a0000221ae991b12…
    ##  4   1549303435 187.121.… 10001 10001     0    49 0100009302000a0027220ee9a0bb7…
    ##  5   1549303435 211.228.… 10001 10001     0    49 010000000000001605040001      
    ##  6   1549303435 138.117.… 10001 10001     2    47 0100007402000a0027225874dd8a7…
    ##  7   1549303435 195.116.… 10001 10001     0    45 0100009802000a802aa82679f2c37…
    ##  8   1549303435 191.37.1… 10001 10001     0    51 0100009302000a44d9e77e44b5bf2…
    ##  9   1549303435 198.204.… 10001 10001   574    51 010000b202000a0027225fabb3c0a…
    ## 10   1549303435 221.157.… 10001 10001     0    48 010000000000001605040001      
    ## # … with 503,987 more rows
    

Note that I redacted the IP addresses (daddr) field solely to make it a bit harder for attackers or infosec pranksters to poke at those nodes.

Along with the missing daddr field, the other salient addresses for analysis are saddr, which is the Sonar study node that performed the probe (we publish them so you can avoid alerting on them and let our scans work so we can help keep the internet safe), and dport, the port we scanned for, along with data, which has the response payload from the UDP probe.

Let's first take a look at where these Ubiquiti nodes are. To do that, we'll use the rgeolocate package to geolocate them using the [MaxMind free databases](https://dev.maxmind.com/geoip/geoip2/geolite2/#Downloads):
    
    
    library(rgeolocate)
    
    bind_cols(
      ubi_df,
      maxmind(
        ips = ubi_df$daddr, 
        file = "/data/maxmind/prod/GeoLite2-City_20190205/GeoLite2-City.mmdb",
        fields = c("country_code", "country_name")
      )
    ) -> ubi_df
    
    count(ubi_df, country_name, sort=TRUE) %>% 
      mutate(pct = n/sum(n))
    

country_name| n| pct  
---|---|---  
United Kingdom| 265,322| 52.64%  
United States| 238,675| 47.36%  
  
  
  
  
  

    
    
    devtools::install_git("https://git.sr.ht/~hrbrmstr/udpprobe")
    
    library(udpprobe)
    

As noted, the data column is the hex-encoded version of the response payload, which means every two characters is a byte value. We'll need to get this into a R raw vector format so we can decode it. While we _could_ do this in R, a small C++ helper function will speed things up dramatically:
    
    
    library(Rcpp)
    
    cppFunction(depends = "BH", '
      List dehexify(StringVector input) {
      
        List out(input.size()); // make room for our return value
        
        for (unsigned int i=0; i<input.size(); i++) { // iterate over the input 
        
          if (StringVector::is_na(input[i]) || (input[i].size() == 0)) {
            out[i] = StringVector::create(NA_STRING); // bad input
          } else if (input[i].size() % 2 == 0) { // likely to be ok input
          
            RawVector tmp(input[i].size() / 2); // only need half the space
            std::string h = boost::algorithm::unhex(Rcpp::as<std::string>(input[i])); // do the work
            std::copy(h.begin(), h.end(), tmp.begin()); // copy it to our raw vector
            
            out[i] = tmp; // save it to the List
    
          } else {
            out[i] =  StringVector::create(NA_STRING); // bad input
          }
          
        }
        
        return(out);
        
      }
    ', includes = c('#include <boost/algorithm/hex.hpp>'))
    

Let's test it out:
    
    
    parse_ubnt_discovery_response(
      unlist(dehexify(ubi_df[["data"]][[1]]))
    )
    
    
    
    ## [Model: AG5-HP; Firmware: XM.ar7240.v5.6.3.28591.151130.1749; Uptime: 0.3 (hrs)
    

Looking good! Let's decode all of them:
    
    
    # infix helper for assigning a default value 'b' in the event the length of 'a' is 0
    `%l0%` <- function(a, b) if (length(a)) a else b 
    
    ubi_df %>% 
      # scanning the internet is dark and full of terrors and some are dead responses despite stage2 . iprocessing
      filter(!is.na(data)) %>% 
      # turn it into something we can use
      mutate(decoded = dehexify(data)) %>% 
      # this takes a bit since the parser was originally meant just to show how to 
      # work with binary data in R directly and it not optimized for production use
      mutate(decoded = map(decoded, parse_ubnt_discovery_response)) %>% 
      # extract some useful elements; note that we need to still be careful
      # to ignore fields that are potentially malformed or missing; again, scanning
      # the internet is fraught with peril, esp when it comes to UDP
      mutate(
        name = map_chr(decoded, ~.x$name %l0% NA_character_),
        firmware = map_chr(decoded, ~.x$firmware %l0% NA_character_),
        model = map_chr(decoded, ~.x$model_short %l0% .x$model_long %l0% NA_character_)
      ) %>% 
      select(name, firmware, model) %>% 
      filter(!is.na(firmware)) -> device_info
    
    print(device_info)
    
    
    
    ## # A tibble: 483,281 x 3
    ##    name                                 firmware                          model 
    ##    <chr>                                <chr>                             <chr> 
    ##  1 bjs.erenildo                         XM.ar7240.v5.6.3.28591.151130.17… AG5-HP
    ##  2 HACKED-ROUTER-HELP-SOS-HAD-DEFAULT-… XM.ar7240.v5.3.5.11245.111219.20… LM5   
    ##  3 85171 Sandra Mara                    XM.ar7240.v6.0-beta8.28865.16030… N5N   
    ##  4 Elcio Donizette Vieira               XM.ar7240.v5.6.3.28591.151130.17… AG5-HP
    ##  5 ag-6672                              XM.ar7240.v5.3.5.11245.111219.20… AG5   
    ##  6 kazimierzow126                       XW.ar934x.v5.6.5.29033.160515.21… AG5-HP
    ##  7 ZANETE CARMINATI                     XW.ar934x.v5.6.2.27929.150716.11… AG5-HP
    ##  8 [[email protected]](/cdn-cgi/l/email-protection)           XM.ar7240.v5.6.dpn.5014.160726.1… NB5   
    ##  9 LOCO Kwiatkowska M                   XS5.ar2313.v4.0.4.5074.150724.13… LC5   
    ## 10 UBNT-2155                            XW.ar934x.v6.0.30097.161219.1705  P5B-3…
    ## # … with 483,271 more rows
    

We can also take a look at some of the extracted data. First, let's see the top 20 Ubiquiti models using the raw model name response:
    
    
    count(device_info, model, sort=TRUE) %>% 
      mutate(pct = n/sum(n)) %>% 
      slice(1:20)
    

model| n| pct  
---|---|---  
AG5-HP| 121,308| 25.1%  
LM5| 88,888| 18.4%  
LB5| 42,156| 8.7%  
N5N| 33,509| 6.9%  
P5B-400| 18,543| 3.8%  
P5B-300| 18,014| 3.7%  
NB5| 17,245| 3.6%  
N5B-16| 16,189| 3.3%  
NS5| 11,862| 2.5%  
LC5| 11,441| 2.4%  
WOM5AMiMo| 11,429| 2.4%  
N2N| 8,886| 1.8%  
LAP| 8,822| 1.8%  
LAP-HP| 6,059| 1.3%  
BS2| 5,725| 1.2%  
ERLite-3| 4,972| 1.0%  
LM2| 4,698| 1.0%  
AG5| 3,778| 0.8%  
NS2| 3,649| 0.8%  
ER-X| 3,057| 0.6%  
  
We can also see if any have (theoretically) been "hacked":
    
    
    filter(device_info, str_detect(name, "HACKED")) %>% 
      count(name, sort=TRUE)
    

name| n  
---|---  
HACKED-ROUTER-HELP-SOS-HAD-DUPE-PASSWORD| 8,813  
HACKED-ROUTER-HELP-SOS-WAS-MFWORM-INFECTED| 3,852  
HACKED-ROUTER-HELP-SOS-DEFAULT-PASSWORD| 1,616  
HACKED-ROUTER-HELP-SOS-VULN-EDB-39701| 1,135  
HACKED-ROUTER-HELP-SOS-HAD-DEFAULT-PASSWORD| 1,047  
HACKED-ROUTER-HELP-SOS-WEAK-PASSWORD| 110  
HACKED-ROUTER-HELP-SOS-CLONEPW-LEAKED-BY-MFW| 33  
HACKED| 1  
HACKED ROUTER| 1  
HACKED-ROUTER| 1  
YOU HAVE BEEN HACKED| 1  
  
  
  
  
  


## Fin

I hope you've enjoyed this first foray into using our Sonar Data API and working with data from one of our scans. Drop us a note at [[email protected]](/cdn-cgi/l/email-protection#c3b1a6b0a6a2b1a0ab83b1a2b3aaa7f4eda0acae) with any questions about this post, the Sonar Data portal/API, or the new ropendata package.

You can find the code used in this post over at [Rapid7’s GitHub](https://github.com/rapid7/data/tree/master/blogs/2019/2019-02-ropendata).

## Article tags

  * [Research](/blog/tag/research/)