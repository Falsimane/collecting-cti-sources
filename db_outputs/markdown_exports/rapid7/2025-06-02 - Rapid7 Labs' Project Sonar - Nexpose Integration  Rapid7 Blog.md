# Rapid7 Labs' Project Sonar - Nexpose Integration | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2015/10/15/project-sonar-integration-in-nexpose/
- **Date :** 2025-06-02

---

With the release of Nexpose 5.17, customers were enabled to easily gain an outsider's view of their internet-facing assets. This capability was made possible through integration with Rapid7 Labs' [Project Sonar](/blog/post/2013/09/26/welcome-to-project-sonar/).

## What is Project Sonar?

Project Sonar is a community effort to improve security through the active analysis of public networks. This includes running scans across public internet-facing systems, organizing the results, and sharing the data with the information security community. Sonar regularly ‘scans the internet' and gathered data is archived and made publicly available in cooperation with the University of Michigan.

## Integration with Nexpose

When designing the integration with Project Sonar, we spent a lot of time determining the ‘best fit' for a seamless integration into the Nexpose workflow. We wanted it to make it both easy and intuitive to retrieve and view data from this new external data source.

### Connecting to Sonar

Working with Rapid7 Labs engineers, we were able to create an ‘always there', trusted connection to Sonar based on the user's Nexpose license. A properly licensed Nexpose console install (with internet access) would be able to automatically authenticate with and connect to the Sonar service. No action is required from the user.

We wanted the user to be able to confirm this connection was active. Since Sonar represents a new way for the user to discover assets, showing the connection in the ‘Discovery Connections' listing was a natural fit.

![Screen_Shot_2015-10-05_at_5.31.53_PM.png](https://www.rapid7.com/cdn/images/blt3254030a6d6ab7e6/683ddb56ca9dfca5595264f1/Screen_Shot_2015-10-05_at_5.31.53_PM.png)

*note: Since the Sonar connection is always available, edit and delete have been disabled. If your console is not licensed or cannot reach the internet, the Sonar connection will not exist in this table.

### Asset Data

When determining how to organize and present Sonar gathered data, we considered that Nexpose assets are divided into 3 categories:

  * **_Discovered by Connection_** : Assets that have been discovered from an external connection (ie: DHCP). Very little is known about these assets otherthan their hostname and ip address.
  * **_Discovered by Scan:_ **This category holds assets that have been scanned in some way (ie: discovery scanned) so that more catalog information is known about the asset.
  * **_Assessed_**. To be categorized as assessed, an asset has been Nexpose scanned and evaluated for vulnerabilities or policy. (ie: full audit scan)



![Screen_Shot_2015-10-05_at_6.14.08_PM.png](https://www.rapid7.com/cdn/images/blt96a06cb0075781f6/683ddb6cabf2add3e63c41e5/Screen_Shot_2015-10-05_at_6.14.08_PM.png)

Sonar data fits best into the ‘Discovered by Scan' state, as there is a variety of asset information cataloged, but it does not contain vulnerability and policy data that would be gathered and evaluated during a typical Nexpose scan.

On the Nexpose assets page, imported Sonar assets will be found in the ‘scanned' asset listing. The ‘assessed' column will say ‘no'.

![Screen_Shot_2015-10-05_at_6.33.06_PM.jpg](https://www.rapid7.com/cdn/images/blt0d8a96212362f248/683ddb895619a10bb4c6e91c/Screen_Shot_2015-10-05_at_6.33.06_PM.jpg)

### Retrieving Data from Sonar

Sonar ‘scans the internet' so it contains a huge dataset with has varying degrees of freshness. We could not automatically collect data without user input. In the simplest case, a target ‘search domain' would be required. We already had a mechanism in place for specifying a set of filters to be applied to a connection from which assets could be pulled. When creating a site, the user is given several options to specify which assets to scan. One of those options is via discovery connection. And discovery connections allow the user to create filters.

![Screen_Shot_2015-10-06_at_3.17.16_PM.png](https://www.rapid7.com/cdn/images/bltba02ce0a750b1ef8/683ddba57f8603b1af230634/Screen_Shot_2015-10-06_at_3.17.16_PM.png)

This is how you bring in assets from Sonar. Create a site and select 'specify assets by connection.' The Sonar connection will be in the dropdown list (again, properly licensed, console with an internet connection). Add a search domain on which to filter and click the 'filter' button to see a listing of assets that would be brought into Nexpose when that site is saved and scanned. A 10,000 asset limit was imposed for a given Sonar site to help the user avoid retrieving more assets than expected. Remember, Sonar's dataset is the internet.

### A Note on 'scanning' a site based on a Sonar connection

![Screen_Shot_2015-10-06_at_3.43.21_PM.png](https://www.rapid7.com/cdn/images/bltdf79b9db0e6cf8c1/683ddbbf3a1c5a690d4ba6f6/Screen_Shot_2015-10-06_at_3.43.21_PM.png)

When the a Sonar site is 'scanned', what is actually happening is that we retrieve the most current asset data archived in the Sonar dataset. Project Sonar has done the actual exploratory scan of the asset at different times as it works its way through scanning the internet.

'Scanning' a Sonar site _does not_ perform a Nexpose assessment of those assets, it simply retrieves archived scan data from Sonar. (note: The 'last scan' date in the asset listing will show the last time it was seen by Sonar, not the last time time a Sonar data retrieval was performed. We realize this will create some confusion with users who would like to perform a full-audit scan of their discovered externally facing assets.

Think of a Sonar scan as a discovery scan that retrieves a larger set of data per asset. It does not assess for vulnerabilities or policy but does find relevant assets and ip addresses that the user might want to more carefully audit. To audit assets discovered by the Sonar site, the user will need to create an **Asset Group** (dynamic or static) containing the assets which are desired for a full-audit. That asset group can then be scanned by Nexpose in the traditional way.

![Screen_Shot_2015-10-06_at_4.01.25_PM.png](https://www.rapid7.com/cdn/images/blt724a38b292f9d563/683ddbe15619a1614ec6e946/Screen_Shot_2015-10-06_at_4.01.25_PM.png)

### What is Next?

We are reaching out and listening to users to discover how they would like us to evolve this functionality. We are planning to add more complex filtering to the initial import of Sonar data. A big example of this is filtering by last Sonar scan date. The Sonar project does not currently age out asset information. We want to give users the ability to say "I only want to retrieve assets that have been seen by Sonar within the last X days".

Additionally, we're thinking about alleviating the extra steps required to perform a Nexpose scan of assets imported from Project Sonar. We want to make this process as easy as possible while making sure users don't full-audit scan unintentionally large datasets (or assets that they don't own).

### From the Engineers

We hope our community is excited to have yet another method for discovering their full surface area and for this unique 'outsider's' view of their internet presence. We are actively working with customers, project management, and other stakeholders to make sure Project Sonar integration is a valuable and seamless addition to the Nexpose product.

## Article tags

  * [Project Sonar](/blog/tag/project-sonar/)
  * [Labs](/blog/tag/labs/)