# UserAuthenticationMethod: Understanding M365 Sign-In Logs

- **Source :** sekoia
- **URL :** https://www.sekoia.com/blog/userauthenticationmethod-microsoft-365-decode
- **Date :** 2025-10-21

---

## Introduction

When users sign in to Microsoft's cloud services, authentication events are recorded in two places: Microsoft Entra sign-in logs and Microsoft 365 audit logs1. While these logs capture the same authentication events, they use different formats and fields to represent the information.

Anyone who has spent time analysing Microsoft 365 sign-in events2 has encountered the `UserAuthenticationMethod` field. This field contains only a numeric value (like 16, 272, or 33554432) with **no documentation from Microsoft** explaining what these numbers mean.

Through correlation with Microsoft Entra sign-in logs, Sekoia.io analysts have discovered that this field is **a bitfield where each bit represents a different authentication method**. This article documents how to decode these numeric values into human-readable descriptions, particularly useful for security analysts and incident responders who may encounter environments where only Microsoft 365 audit logs are available.

## The bitfield mapping

The following table documents the mappings we've identified through our analysis.

Each bit position in the `UserAuthenticationMethod` value corresponds to a specific authentication method:

**Bit**| **Decimal Value**| **Authentication Method**  
---|---|---  
0| 1[](https://learn.microsoft.com/en-us/microsoft-365/enterprise/cloud-only-identities)| Password in the cloud  
1| 2[](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass)| Temporary Access Pass  
2| 4[](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso)| Seamless SSO  
3| 8[](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-pta)| Pass-through Authentication  
4| 16[](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-phs)| Password Hash Sync  
6| 64| Passwordless phone sign-in  
8| 256|  [via Staged Rollout](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-staged-rollout) (combined with a method)  
18| 262144[](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/)| Windows Hello for Business  
19| 524288| QR code ([authentication transfer](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-transfer),  _e.g._ Outlook Android)  
20| 1048576[](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-sms-signin)| SMS Sign-in  
21| 2097152[](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-certificate-based-authentication)| X.509 Certificate  
23| 8388608[](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passwordless#platform-credential-for-macos)| MacOS Platform Credentials  
24| 16777216[](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-qr-code)| QR code pin  
25| 33554432[](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2#types-of-passkeys)| Passkey (device-bound), including [Microsoft Authenticator passkeys](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-authenticator-app#passkey-sign-in)  
2667108864[Passkey (synced)](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2#types-of-passkeys)27| 134217728[](https://learn.microsoft.com/en-us/entra/external-id/one-time-passcode)| Email verification code  
  
Note: Several bits remain unmapped (bits 5, 7, 9-17, 22). If you observe these values, please share your findings.

Multiple bits can be set simultaneously. For example, to decode the value 272:

  * Convert 272 to binary: `100010000`
  * Identify active bits: 
    * Bit 4 (16): Password Hash Sync
    * Bit 8 (256): via Staged Rollout
  * Combined meaning: "Password Hash Sync via Staged Rollout"



### What's included (and what's not)

This bitfield appears to only include authentication methods that can serve as _primary_ authentication. Common _secondary-only_ factors3, such as Microsoft Authenticator push notifications or Software OATH tokens, don't seem to be represented in this field.

When a primary-capable method is used _as_ a second factor (for example, a Passkey used after a password), it _still_ appears in the bitfield alongside the first factor.

The `UserAuthenticationMethod` field doesn't reflect either the protocol type (_e.g._ OAuth or SAML) or grant flow (_e.g._ device code flow or ROPC flow) used in the authentication.

## Methodology: correlating Microsoft 365 and Entra ID logs

To decode these values, we correlated Microsoft 365 audit log events with Entra ID sign-in logs for the same authentication events. The key is that both log sources share a [correlation identifier](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-sign-in-log-activity-details#unique-identifiers):

  * Microsoft 365 audit log: `InterSystemsId` field
  * Entra ID logs: `correlationId` field



While Microsoft 365 logs contain the opaque `UserAuthenticationMethod` numeric value, Entra ID logs provide detailed authentication method descriptions in fields like `authenticationMethodDetail`. By matching events across both log sources, we mapped each numeric value to its corresponding authentication method.

We also validated some mappings by deliberately using specific authentication methods in a test environment and observing the resulting logs. This testing was particularly helpful for disambiguating similar-sounding methods. For instance, it helped us distinguish between "QR code" (bit 19), which refers to the authentication transfer method used by mobile apps like Outlook on Android, and "QR code pin" (bit 24), the more common single-factor authentication method.

### Investigation example using Sekoia Operating Language (SOL)

The relevant fields from both log sources are indexed in the Sekoia platform as follows:

Log source| Field name| Sekoia field name  
---|---|---  
Microsoft 365| `UserAuthenticationMethod`| `office365.auth.user_authentication_method`  
Microsoft 365| `InterSystemsId`| `office365.context.correlation.id`  
Microsoft Entra| `correlationId`| `azuread.correlationId`  
  
Here's how one can investigate a specific `UserAuthenticationMethod` value by correlating Microsoft 365 and Entra ID logs using [Sekoia Operating Language (SOL)](https://docs.sekoia.com/xdr/features/investigate/sekoia_operating_language/):

`let TargetAuthMethod = 262144; // UserAuthenticationMethod value  
let TimeWindow = ago(30d);  
  
// Step 1: Find M365 sign-ins with the target authentication method value  
let CorrelationIds = events  
| where timestamp >= TimeWindow  
| where office365.record_type == 15 // AzureActiveDirectoryStsLogon  
| where office365.auth.user_authentication_method == TargetAuthMethod  
| distinct office365.context.correlation.id;  
  
// Step 2: Get corresponding Entra ID sign-ins using the correlation IDs  
events  
| where timestamp >= TimeWindow  
| where azuread.operationName == "Sign-in activity"  
| where azuread.correlationId in CorrelationIds  
| aggregate Count = count()  
by AuthenticationMethod = azuread.authenticationDetails.authenticationMethod  
| order by Count desc`

This query first identifies Microsoft 365 audit log entries with a specific authentication method value, then uses their correlation IDs to find the corresponding Entra ID sign-ins, revealing what authentication methods that numeric value represents.

Note that this query typically returns multiple authentication method names because the correlation ID matches all steps of a sign-in flow, including MFA steps. The count and ordering help identify the primary mapping: the top result is likely the authentication method corresponding to the target value.

For some authentication methods, the `authenticationMethodDetail` field in Entra ID details the specific variant. For example, when the `authenticationMethod` shows "Password", the `authenticationMethodDetail` field distinguishes between "Password in the cloud", "Pass-through Authentication", and "Password Hash Sync".

### Example: multi-factor authentication flow

A single sign-in flow consists of multiple steps (submitting credentials, selecting an MFA method, completing the MFA challenge), each generating a separate audit record. These records share the same correlation ID and can be distinguished by their `RequestType`, which indicates the endpoint called at each step.

This real example demonstrates how the bitfield accumulates values during an MFA sequence:

#### Step 1 - First factor (password):

Microsoft 365 audit log shows:

`**RequestType**`| `Login:login`  
---|---  
`**UserAuthenticationMethod**`| `272`  
  
Entra ID log shows:

`**authenticationMethodDetail**`| `Password Hash Sync via Staged Rollout`  
---|---  
  
`UserAuthenticationMethod`**272** breaks down as:

  * Password Hash Sync (16)
  * via Staged Rollout (256)



#### Step 2 - Second factor (passkey):

Microsoft 365 audit log shows:

`**RequestType**`| `SAS:ProcessAuth`  
---|---  
`**UserAuthenticationMethod**`| `33554704`  
  
Entra ID log shows:

`**authenticationMethod**`| `Passkey (device-bound)`  
---|---  
`**authenticationMethodDetail**`| `Password Hash Sync via Staged Rollout`  
  
`UserAuthenticationMethod`**33554704** breaks down as:

  * Password Hash Sync (16)
  * via Staged Rollout (256)
  * Passkey (33554432)



In this event, the `UserAuthenticationMethod` value reflects both the first factor (password) and the second factor (passkey) used in the authentication flow.

## Applications and limitations

Understanding what the `UserAuthenticationMethod` values represent in Microsoft 365 audit logs enables security teams to identify authentication methods during incident investigations, track staged rollout progress, and assess whether accounts use [phishing-resistant authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/phishing-resistant-authentication-videos) like Passkeys or Windows Hello for Business.

However, **several bits remain unmapped**. We haven't observed all possible values in the logs available to us. Microsoft also regularly adds new authentication methods, which will likely correspond to new bit positions.

We encourage the security community to **validate these findings** in your own environments, **share discoveries** about unmapped bits or corrections to these mappings, and request official documentation from Microsoft.

If you've observed different values or can map additional bits, please share your findings with the community, or contact the Sekoia.io Threat Detection and Research team directly at _tdr [ at ] sekoia [ dot ] io._

## Updates

**2026-04-11** — Added bit 26 = **Passkey (synced)** (value `67108864`). This value first appeared in our telemetry on 2026-01-28, during Microsoft's synced passkey public preview, and the feature reached [general availability in March 2026](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new#general-availability---synced-passkeys-in-microsoft-entra-id). The primary reference link for bit 25 (Passkey device-bound) now points at the dedicated _Passkeys (FIDO2)_ concept page that Microsoft split out of its passwordless authentication documentation shortly after this article was originally published.