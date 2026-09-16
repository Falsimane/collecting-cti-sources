# Citrix Gateway and Citrix ADC Security Bulletin | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2022/11/15/cve-2022-27510-critical-citrix-adc-and-gateway-remote-authentication-bypass-vulnerability/
- **Date :** 2025-06-02

---

On November 8, 2022, Citrix published [Citrix Gateway and Citrix ADC Security Bulletin for CVE-2022-27510 CVE-2022-27513 and CVE-2022-27516](https://support.citrix.com/article/CTX463706/citrix-gateway-and-citrix-adc-security-bulletin-for-cve202227510-cve202227513-and-cve202227516) announcing fixes for three vulnerabilities:

  * [CVE-2022-27510](https://nvd.nist.gov/vuln/detail/CVE-2022-27510) “Unauthorized access to Gateway user capabilities”
  * [CVE-2022-27513](https://nvd.nist.gov/vuln/detail/CVE-2022-27513) “Remote desktop takeover via phishing”
  * [CVE-2022-27516](https://nvd.nist.gov/vuln/detail/CVE-2022-27516) “User login brute force protection functionality bypass”



The most notable vulnerability, [CVE-2022-27510](https://nvd.nist.gov/vuln/detail/CVE-2022-27510), is rated a critical 9.8 for “appliances that are operating as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy),” per Citrix’s advisory, and allows for remote, unauthenticated attackers to take control of a vulnerable system.

Rapid7 has repeatedly observed attacker interest in high-value targets such as Citrix; historically, these appliances become exploited very quickly so **organizations that are impacted by CVE-2022-27510 should patch right away**. CISA has issued a warning about CVE-2022-27510 [here](https://www.cisa.gov/uscert/ncas/current-activity/2022/11/09/citrix-releases-security-updates-adc-and-gateway).

## Affected products

The following supported versions of Citrix ADC and Citrix Gateway on customer-managed appliances are affected by this vulnerability (Citrix-managed cloud services customers do not need to take any action):

  * Citrix ADC and Citrix Gateway 13.1 before 13.1-33.47
  * Citrix ADC and Citrix Gateway 13.0 before 13.0-88.12
  * Citrix ADC and Citrix Gateway 12.1 before 12.1.65.21
  * Citrix ADC 12.1-FIPS before 12.1-55.289
  * Citrix ADC 12.1-NDcPP before 12.1-55.289



## Mitigation guidance

Organizations that are impacted by CVE-2022-27510 should update to one of the versions listed below immediately. Additionally, it is strongly recommended that organizations ensure that gateway devices require multi-factor authentication (MFA) for logins and that all authentication attempts are logged and audited regularly.

  * Citrix ADC and Citrix Gateway 13.1-33.47 and later releases
  * Citrix ADC and Citrix Gateway 13.0-88.12 and later releases of 13.0
  * Citrix ADC and Citrix Gateway 12.1-65.21 and later releases of 12.1
  * Citrix ADC 12.1-FIPS 12.1-55.289 and later releases of 12.1-FIPS
  * Citrix ADC 12.1-NDcPP 12.1-55.289 and later releases of 12.1-NDcPP



## Rapid7 customers

InsightVM and Nexpose customers are able to assess their exposure to all three CVEs with vulnerability checks available in the November 15, 2022 content release (available as of 4pm ET).

## Article tags

  * [Emergent Threat Response](/blog/tag/emergent-threat-response/)
  * [Research](/blog/tag/research/)