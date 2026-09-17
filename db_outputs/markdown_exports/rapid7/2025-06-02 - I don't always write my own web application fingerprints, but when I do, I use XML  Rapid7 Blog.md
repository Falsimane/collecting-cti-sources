# I don't always write my own web application fingerprints, but when I do, I use XML | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2014/07/31/i-dont-always-write-my-own-web-application-fingerprints-but-when-i-do-i-use-xml/
- **Date :** 2025-06-02

---

One of the awesome things about Nexpose is its extensibility. Nexpose now allows you to write your own custom web application fingerprints, using a combination of XPath and regular expressions. Coupled with the ability to [add your own custom checks](/blog/post/2013/06/13/custom-vulnerability-checks-using-nexposes-vulnerability-schemas/), this allows you to write your own web application vulnerability coverage.

This fingerprinting functionality can be used on any web application that provides its version information on an unauthenticated page, such as a login page. It is surprisingly common for web applications to advertise their versions to unauthenticated users. For example, look at [the Apache project's Jira instance.](https://issues.apache.org/jira/secure/Dashboard.jspa) Near the bottom of the page, there is a line advertising the Jira version, which at the time of this writing reads "Atlassian JIRA (v6.2#6252-sha1:aa34325)".

## Great! How does it work?

The fingerprinter uses two well-known technologies:

  * XPath to identify relevant fields of a web page
  * Regular expressions, particularly the variant supported by Java's standard Pattern class, to identify text in these fields



You do not have the know XPath or regular expressions to use Nexpose, but if you're comfortable with these technologies, you can add your own custom fingerprints. As an example fingerprint, the following XML is used to fingerprint Confluence.
    
    
    <!-- Atlassian Confluence -->  
      
    <fingerprint>  
      <get path="/"/>  
      <get path="/login.action"/>  
      <test xpath="//div[@id='footer']/ul[@id='poweredby']/descendant-or-self::node()"  
          regex="Atlassian Confluence ([\d\.]+)[, ]">  
          <param pos="0" name="vendor" value="Atlassian"/>  
          <param pos="0" name="product" value="Confluence"/>  
          <param pos="1" name="version"/>  
      </test>  
    </fingerprint>  
    

## How do I add custom content?

Let's walk through an example. At the time of this writing, the site community.rapid7.com is running on [Jive](http://www.jivesoftware.com/). We're going to add a fingerprint for Jive. Since you're reading this post, you're already viewing community.rapid7.com, so view the page source in your browser. You will see that there is a non-displaying field that identifies the Jive version:
    
    
    <div>Jive Software Version: 6.0.1.1 , revision: 201302191025.7ae0697.release_6_0_1_1</div>  
    

You can also use the Inspect Element functionality in Chrome or Firefox to see the tree structure of the HTML document. For example, here is how it looks in Firefox:

![inspect-element.png](https://www.rapid7.com/cdn/images/blt38c79c8c142627dc/683dda94c26e079a5f28e546/inspect-element.png)

Since the class "j-footer-jiveVersion", coupled with text identifying the Jive version, is almost certain not to appear unless the page is powered by Jive, looking for a div with this class is probably safe, and this is easy to write an XPath expression for.

To add the fingerprint, you must have access to the host running your Nexpose scan engine; for example, via SSH login. Create or edit the file plugins/webapp-fp/custom/xpath_webapps.xml in your Nexpose installation. Since the version information appears on the landing page, Nexpose only needs to do an HTTP GET for "/". The fingerprint for Jive should look like this:
    
    
    root@ub1204-6acu0-z1:/opt/rapid7/nexpose# cat plugins/webapp-fp/custom/xpath_webapps.xml   
      
    <fingerprints>  
      
      <!-- Jive-->  
      <fingerprint>  
          <get page="/"/>  
          <test xpath="//div[@class='j-footer-jiveVersion']"  
            regex="Jive Software Version: ([\d\.]+)">  
            <param pos="0" name="vendor" value="Jive Software"/>  
            <param pos="0" name="product" value="Jive"/>  
            <param pos="1" name="version"/>  
          </test>  
      </fingerprint>  
      
    </fingerprints>  
    

**Congratulations, you've just added a fingerprint to Nexpose!**

We're now ready to test the fingerprint using Nexpose. Note that you do NOT have to restart the Security Console after adding this fingerprint; the fingerprints for this functionality are re-read at the start of each scan. Ensure that your scan template includes port 443 and scan community.rapid7.com. If you click HTTPS in the service listing for the host, you will see that "Jive 6.0.1.1" is asserted as a configuration item for the Tomcat web server.

![fingerprint-jive.png](https://www.rapid7.com/cdn/images/bltcd0a23f47761fc1c/683dda9b2cfe327a90dc1482/fingerprint-jive.png)

## Can you give me an example of a custom check?

Sure thing. When Nexpose fingerprints a web application, it stores it as a component of the HTTP server running the application. Your check thus needs to do a version check on the named component. Here is an example vulnerability check for CVE-2014-3994 in the Review Board code review application:
    
    
    <?xml version="1.0" encoding="UTF-8"?>  
    <VulnerabilityCheck scope="endpoint">  
      <NetworkService type="HTTP|HTTPS">  
        <Product>  
          <Component name="Review Board">  
            <version>  
              <range>  
                <high inclusive="0">1.7.26</high>  
              </range>  
            </version>  
            <version>  
              <range>  
                <low inclusive="1">2.0</low>  
                <high inclusive="0">2.0.2</high>  
              </range>  
            </version>  
          </Component>  
        </Product>  
      </NetworkService>  
    </VulnerabilityCheck>  
    

By changing the component name and versions, you can write similar checks for other web applications.  


## Article tags

  * [Research](/blog/tag/research/)