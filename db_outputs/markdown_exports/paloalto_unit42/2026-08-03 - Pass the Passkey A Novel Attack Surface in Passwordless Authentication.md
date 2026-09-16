# Pass the Passkey: A Novel Attack Surface in Passwordless Authentication

- **Source :** paloalto_unit42
- **URL :** https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/
- **Date :** 2026-08-03

---

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
  * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
  * [Malware](https://unit42.paloaltonetworks.com/category/malware/ "Malware")



[Malware](https://unit42.paloaltonetworks.com/category/malware/)

# Pass the Passkey: A Novel Attack Surface in Passwordless Authentication

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg) 17 min read 

Related Products

[![Cortex icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex](https://unit42.paloaltonetworks.com/product-category/cortex/ "Cortex")[![Cortex Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/cortex_RGB_logo_Icon_Color.png)Cortex Cloud](https://unit42.paloaltonetworks.com/product-category/cortex-cloud/ "Cortex Cloud")[![Unit 42 Incident Response icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/unit42_RGB_logo_Icon_Color.png)Unit 42 Incident Response](https://unit42.paloaltonetworks.com/product-category/unit-42-incident-response/ "Unit 42 Incident Response")

  * ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

By:
    * [Arie Olshtein](https://unit42.paloaltonetworks.com/author/arie-olshtein/)

  * ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

Published:August 3, 2026

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

Categories:
    * [Malware](https://unit42.paloaltonetworks.com/category/malware/)
    * [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)

  * ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

Tags:
    * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/)
    * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/)
    * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/)
    * [Identity](https://unit42.paloaltonetworks.com/tag/identity/)
    * [Key](https://unit42.paloaltonetworks.com/tag/key/)
    * [Passkey](https://unit42.paloaltonetworks.com/tag/passkey/)
    * [Passwordless](https://unit42.paloaltonetworks.com/tag/passwordless/)




  * [ ![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/?pdf=download&lg=en&_wpnonce=ac4b3be3b8 "Click here to download")
  * [ ![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/?pdf=print&lg=en&_wpnonce=ac4b3be3b8 "Click here to print")



Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

  * ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
  * [ ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)](mailto:?subject=Pass%20the%20Passkey:%20A%20Novel%20Attack%20Surface%20in%20Passwordless%20Authentication&body=Check%20out%20this%20article%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication-security-risks%2F "Share in email")
  * [ ![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication-security-risks%2F "Share in Facebook")
  * [ ![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication-security-risks%2F&title=Pass%20the%20Passkey:%20A%20Novel%20Attack%20Surface%20in%20Passwordless%20Authentication "Share in LinkedIn")
  * [ ![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication-security-risks%2F&text=Pass%20the%20Passkey:%20A%20Novel%20Attack%20Surface%20in%20Passwordless%20Authentication "Share in Twitter")
  * [ ![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication-security-risks%2F "Share in Reddit")
  * [ ![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Pass%20the%20Passkey:%20A%20Novel%20Attack%20Surface%20in%20Passwordless%20Authentication%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fpasswordless-authentication-security-risks%2F "Share in Mastodon")



## Executive Summary

This article analyzes new attack classes against passwordless authentication, focusing on Google’s synced passkey ecosystem and the Cloud Authenticator used by desktop clients. The attacks demonstrate how malware on a compromised endpoint can misuse onboarding, recovery and device trust workflows to take over passkey-protected accounts. We show how an attacker can authenticate without user interaction, bypass user verification requirements and extract all synced passkey private keys.

After decades of breaches and billions in losses, the attack vectors that defined the era of passwords and shared secrets are finally starting to fade. Passkeys replace passwords and traditional multi-factor authentication (MFA) with public-key cryptography, decreasing entire classes of attacks that have dominated the threat landscape for years.

With no shared secret to steal, reuse or phish, many of an attacker’s most reliable tools are becoming obsolete. This represents a significant disruption for the credential theft market.

Attackers, however, persist. They evolve, and defenders must prepare for a new generation of attacks. As passkeys become widely adopted and scale to billions of accounts, defenders must prepare for new attack surfaces, some of which we disclose in our research.

This article is part 3 in our series examining passkey adoption from a security perspective. If you haven’t read the previous parts, we recommend starting here:

Part 1: [The Art of the Invisible Key – Passkey Global Breakthrough](https://www.cyberark.com/resources/threat-research-blog/the-art-of-the-invisible-key-passkey-global-breakthrough)

Part 2: [Google Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/)

Palo Alto Networks customers are better protected from this new attack vector through the following products and services:

  * [Cortex Cloud Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security)
  * [Idira Threat Detection and Response](https://docs.cyberark.com/detect-and-respond/latest/en/content/get-started/what-is-detect-and-respond.htm)
  * [Idira Endpoint Privilege Manager](https://docs.cyberark.com/epm/latest/en/content/intro/introduction.htm)
  * [Idira Privilege Access Management ](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1)



If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

**Related Unit 42 Topics** | **[Google Authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/), [Cloud](https://unit42.paloaltonetworks.com/tag/cloud/), [Malware](https://unit42.paloaltonetworks.com/tag/malware/)**  
---|---  
  
## Setting the Stage

Google’s synced passkey implementation is particularly instructive due to its scale and how it creates a higher standard for private key protection in two critical ways:

  * Private keys are generated and used within a cloud-enclave isolation environment
  * Hardware-backed, client-device-bound keys control access to cloud-based cryptographic operations, attesting to the user’s presence on a trusted device



This article builds on the architectural analysis from [Part 1](https://www.cyberark.com/resources/threat-research-blog/the-art-of-the-invisible-key-passkey-global-breakthrough) and [Part 2](https://unit42.paloaltonetworks.com/passwordless-authentication/) of our previous articles in this series. We now shift from how passkeys are built and deployed to how attackers can misuse them.

We present three novel attacks that enable account takeover of passkey-protected accounts. Each attack challenges a different core assumption of passkey authentication security. When a client authenticates with a passkey, the following is expected:

  * Users provide [explicit consent](https://www.w3.org/TR/webauthn-2/#user-consent) on the device to verify [user presence](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html#makecred-up)
  * For MFA, users must also unlock the device to verify biometric (i.e., something you are) or knowledge-based (i.e., something you know) [authentication factors](https://pages.nist.gov/800-63-3/sp800-63-3.html#af)
  * Passkey private keys cannot be shared or copied



[The Google documentation](https://support.google.com/accounts/answer/13548313?hl=en#:~:text=Unlike%20passwords%2C%20passkeys,to%20unlock%20it.) reflects these core assumptions, describing the passkey login process as a secure alternative to passwords (as shown in Figure 1).

![A screenshot of Google Account Help page explaining passkeys. It highlights that passkeys are more secure than passwords as they cannot be shared, copied, or accidentally given away. Using a passkey to sign in ensures access to your device and its unlocking.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/word-image-198667-184120-1.png)Figure 1. [Google documentation](https://support.google.com/accounts/answer/13548313?hl=en#:~:text=Unlike%20passwords%2C%20passkeys,to%20unlock%20it.) describes passkeys as requiring device access, device unlock, and non-shareable credentials.

Challenging these expectations is a category of attacks we've nicknamed Pass-ta-key. This playful, layered name blends the word passkey and the phrase “pass the key,” with a light nod to the concept of plate of pasta, illustrating how tangled this key implementation can get.

These attacks each expose a different weakness in practice:

  * **Pass-ta-key attack:** An attacker takes over an account protected by a Google-synced passkey using malware running on the victim’s device, without requiring privilege escalation, device unlock or user interaction
  * **Silver Pass-ta-key attack:** An attacker deceives the Google Cloud Authenticator into believing the victim has unlocked the device with biometrics, leading to full account takeover without using the victim’s device during authentication
  * **Golden Pass-ta-key attack:** An attacker can extract all synced passkeys in a form that allows them to be shared or sold on the credential black market



These attacks demonstrate how malware can exploit synced passkeys, even when providers add hardware-backed protections to secure credentials within the cloud authenticator.

_Disclaimer: This research involved responsible and ethical security analysis. We responsibly disclosed all presented exploits._ _The cloud authenticator model is used by various passkey providers across multiple browsers and platforms. This work, however, focuses on Google Password Manager in Chrome on Windows, specifically on devices equipped with a Trusted Platform Module (TPM). All presented attacks rely on malware already existing on the victim’s device during the initial stage._

## Stage Zero Reconnaissance

Before attempting any of the attacks, the attacker needs visibility into how passkeys are used within the victim’s account. On a compromised endpoint, this visibility is readily available.

Chrome locally stores synced passkey data as part of its synchronization process. On Windows, Chrome persists this data as proto-encoded [WebauthnCredentialSpecifics](https://chromium.googlesource.com/chromium/src/+/main/components/sync/protocol/webauthn_credential_specifics.proto#27) records, which represent synced [WebAuthn](https://www.w3.org/2018/Talks/06-WebAuthn.pdf) credentials, within its sync database:

%LocalAppData%\Google\Chrome\User Data\<Profile>\Sync Data\LevelDB

Accessing these records does not require elevated privileges. The records allow an attacker to enumerate where the victim uses passkeys, along with associated usernames, credential identifiers and the encrypted private key.

After identifying a service where the victim uses passkeys, an attacker can attempt to authenticate as the victim.

The primary challenge for attackers is bypassing the protection of the private key, which is used to sign authentication challenges. This private key is secured by a master key. While an encrypted version of this master key is stored on each client device, only the cloud authenticator can decrypt it.

Despite this security, the architecture remains vulnerable to exploitation. The following sections detail methods attackers could use to exploit system mechanisms, authenticate as the victim, and compromise passkey-secured accounts.

## Device Identity Impersonation: The Pass-Ta-Key Attack

Our first attack is the most straightforward approach, which involves taking over a passkey-protected account by mimicking the behavior of Google Password Manager and Chrome during legitimate authentication. In a normal flow, Chrome sends a request to the cloud authenticator, signed using the device’s hardware-backed keys.

Unlike a legitimate user flow that requires user interaction and device unlock, this attack shows how malware can obtain the required signature silently, without user consent, biometrics, device unlock or elevated privileges.

To understand this, we focus on Chrome’s device identity key, which represents client device possession to the cloud authenticator. As previously explained (part 2:[ Login with Synced Passkey](https://unit42.paloaltonetworks.com/passwordless-authentication/#section6SubHeading1) and[ Device Key Signature](https://unit42.paloaltonetworks.com/passwordless-authentication/#section6SubHeading1)~~~~), generating the required assertion involves signing data sent to the cloud authenticator using one of the device’s hardware-backed keys. This is the identity key or the user verification key (UV key).

Although both keys are hardware-bound, they are not accessed in the same way. For the identity key, Chrome creates the conditions that allow it to request a signature while running as a user without elevated privileges and without triggering device unlock protections.

On Windows, Chrome calls the [NcryptCreatePersistedKey](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey) function without assigning a key name, making the TPM-backed key ephemeral and preventing it from being persisted to disk. Instead of storing the private key within the TPM, Chrome calls [NcryptExportKey](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey) to export the key as an NCRYPT_OPAQUE_KEY_BLOB, which instructs the TPM to encrypt the private key using a TPM-resident key. The resulting blob is stored as wrapped_identity_private_key in the passkey_enclave_state file, making it available for future use on the same physical TPM.

Malware can extract this wrapped_identity_private_key from disk or Chrome’s memory. It can then invoke cryptographic operations using standard Windows Cryptography API: Next Generation (CNG) [API](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey)s ([NCryptOpenStorageProvider](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey), [NCryptImportKey](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey), [NCryptSignHash](https://learn.microsoft.com/en-us/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey)), without elevated privileges, mimicking Chrome’s own actions.

Having established that malware can generate the required signature, we now detail the full Pass-ta-key attack flow (as shown in Figure 2). This flow allows a remote attacker with unprivileged malware on the victim’s device to authenticate as the victim.

![A flowchart illustrating a security process involving four entities: Relying Party, Attacker, Infected Victim, and Cloud Authenticator. The chart shows interactions like "Log in with passkey," "Noise NX handshake," and "Identity Key Signature". The process moves horizontally with lines and arrows indicating the flow of steps.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/Pass-the-Passkey_-Figure-2-1-1262x700.png)Figure 2. Pass-ta-key attack flow.

The attack flow consists of the following phases:

  1. After collecting the victim’s synced passkey records (Stage Zero: Reconnaissance), the attacker selects a targeted account and initiates a passkey login
  2. The relying party responds with a fresh authentication challenge
  3. The attacker initiates a WebSocket handshake with the Google Cloud Authenticator
  4. Using the hash of that handshake, the attacker interacts with the victim’s TPM and uses the extracted identity key to sign the handshake hash together with the assertion request
  5. The attacker sends an assertion request to the cloud authenticator, including the identity key signature
  6. From the cloud authenticator’s perspective, the request appears to be a trusted device making a valid request, so it produces a valid assertion response
  7. This assertion is then forwarded to the relying party, completing authentication and giving the attacker full control of the victim’s account



Video 1 demonstrates the attack as it would unfold in practice. (We have blurred the names of the relying parties to avoid naming.)

&lt;br /&gt; 

_Video 1. Example of a successful Pass-ta-key attack. _

As the video begins, the screen splits between the attacker's terminal and the victim's desktop. The video first shows the attacker establishing a command-and-control (C2) listener, passively waiting for victims to connect.

On the victim’s machine, the Trojan executes as a standard user, without elevated privileges. Once active, it collects the victim’s encrypted, synced passkeys and sends them back to the attacker’s C2 server. This provides visibility into the victim’s available passkeys.

The attacker selects a target, such as a messaging application account protected by a passkey, navigates to the application and chooses Login with passkey. The relying party then responds with a fresh authentication challenge.

Next, the attacker initiates communication with the Google Cloud Authenticator. After completing the handshake, the attacker triggers the Trojan to use the device’s identity key to sign the required data. Specifically, it uses the hash of the handshake combined with the hash of the serialized assertion request.

The attacker then attaches this signature to the request sent to the cloud authenticator. The cloud authenticator returns the requested assertion. The attacker forwards this valid assertion to the relying party and successfully logs in as the victim.

### UV Flag: When MFA Depends on a Single Bit

The Pass-ta-key attack is effective when the relying party does not strictly require user verification. Many relying parties configure WebAuthn’s userVerification parameter as preferred rather than required to support diverse devices and user experiences, making them susceptible to this attack.

When a relying party explicitly requires user verification, one would expect the cloud authenticator to reject requests that are not signed using a key gated by PIN or biometric verification. Surprisingly, this is not the case.

The cloud authenticator returns a valid assertion regardless of whether the request was signed using the identity key or the UV key. The difference comes down to a single bit in the authenticator data, the User Verified (UV) flag.

When the assertion is signed using the UV key, this flag is set to 1. When it is signed using the identity key, the flag remains 0.

While the Pass-ta-key attack produces cryptographically valid assertions matching the relying party’s public key, our testing shows attacks typically fail when user verification is required because the UV flag remains unset. For example, when attempting the attack against a passkey-protected GitHub account, the attacker receives an error message, as shown in Figure 3.

![A screenshot of a GitHub login screen with a circular logo above the text "Sign in to GitHub." A red error message states, "Unable to sign in with your passkey. Please sign in with your password."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/word-image-207176-184120-4.png)Figure 3. Message from GitHub passkey login failure.

Although authentication is typically rejected when user verification is required, this behavior is not always consistently enforced across relying parties. In our testing, we identified relying parties that accepted authentication because they did not properly validate the UV flag. This allowed the attack to succeed despite the absence of user verification.

The lack of validation effectively reduces the authentication process to a single factor. By compromising only the device identity key, the attacker is able to authenticate successfully and take over the account, even though MFA is required.

We reported this issue to the affected relying parties.

Video 2 demonstrates this behavior in practice on eBay. Although eBay sets the userVerification parameter to required, the demo recording shows a successful passkey login using the described technique, without any user interaction or additional authentication factors.

_We captured this recording before eBay fixed the issue. Following our report, eBay addressed this verification gap and now properly validates the UV flag._

&lt;br /&gt; 

_Video 2. Pass-ta-key attack succeeds despite the absence of user verification, even when the UV is required._

## Pending Attacker: The Silver Pass-Ta-Key Attack

When an account is protected by stronger authentication requirements, such as for financial or federal identity systems, the attacker must also bypass user verification. This initially appears to be a significant challenge.

The cloud authenticator requires a message signed with the UV key to set the UV flag. Client interaction controls access to this key, as the OS validates the user via the same mechanism used for device unlock. Without [escalating to system privileges](https://github.com/CCob/Shwmae#sign) or [physical access](https://www.cyberark.com/resources/threat-research-blog/bypassing-windows-hello-without-masks-or-plastic-surgery) to the victim device, an attacker has no apparent path to obtain such access.

Attackers can bypass this challenge through the following mechanism:

  * Instead of bypassing access to the UV key, the attacker invalidates the existing key registered in the cloud authenticator and registers a newly generated key under their control
  * Once the attacker-controlled key is registered, any message signed with it is accepted by the cloud authenticator as if the user had successfully performed device unlock



Figure 4 demonstrates the attacker-side authentication flow in the Silver Pass-ta-key attack, focusing on the authentication phase after the attacker-controlled UV key is registered.

![A diagram illustrating a security process involving four entities: Relying Party, Attacker, Infected Victim, and Cloud Authenticator. Each entity is in a colored box. Arrows show the flow of communication, including a "Noise NK handshake" to the Attacker, a "Fake UV Key signature" to Google Cloud Authenticator, and an "assertion response" returning to Relying Party.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/08/Pass-the-Passkey_-Figure-4-1422x700.png)Figure 4. Attacker-side authentication flow in the Silver Pass-ta-key attack.

This approach has important implications. It allows the attacker to fully automate authentication across all the victim’s accounts without human interaction, even where user verification is enforced. Furthermore, the attacker no longer needs live access to the victim’s device during authentication.

Unlike the previous attack, which required active malware on the victim’s device for each authentication, the Silver attack provides reusable access. This allows the attacker to access the victim’s passkey-protected accounts from their own environment, without requiring the victim’s device to be online or active. Ultimately, this enables account takeover across all passkeys associated with the victim without requiring elevated privileges.

### Invalidating the Existing User Verification Key

To carry out this attack, the first objective is to invalidate the existing UV key associated with the target device. From the previous attack, we learned how an attacker can use unprivileged malware to sign attacker-controlled requests with the device identity key and send them to the cloud authenticator. The attacker can leverage this capability to issue a device/forget command on behalf of the victim. A simpler option is to directly delete the victim’s passkey_enclave_state file, as there are no built-in protections that prevent its removal.

Regardless of the method, the next time the user attempts to use a passkey, Chrome is forced to re-onboard the device. This occurs either because Chrome no longer has access to the device key or because the cloud authenticator no longer recognizes the device as registered.

### **E** xploiting the Onboarding Flow

On Windows, device onboarding is only completed after the second use of a passkey on the same device. During the first use, Chrome begins onboarding with the cloud authenticator in the background while prompting the user to enter the Google Password Manager (GPM) recovery PIN.

If Chrome were to create the UV key at this point, it would also trigger a Windows Hello prompt, requiring the user to authenticate again using biometrics or a PIN. Since both steps may involve a PIN, presenting them back-to-back in the same flow can be confusing and lead to user errors. To avoid this, Chrome defers the creation of the UV key.

Instead, the device is initially registered in a uv_key_pending state. During this first interaction, the GPM recovery PIN satisfies user verification, and the actual UV key is only created and registered during the next passkey use, when the additional prompt is no longer needed.

After forcing the victim into this re-registration state, the attacker can exploit the uv_key_pending condition. In their own environment, the attacker generates an asymmetric key pair. They then send a device/add_uv_key command to the cloud authenticator, providing the attacker-controlled public key as the UV key.

The cloud authenticator does **not** validate the attestation of newly registered UV keys to verify whether they originate from secure hardware. As a result, the attacker-controlled key is stored alongside the legitimate device identity key:

devices[device_id] = { hw: identity_public_key, uv: (Attacker-controlled) uv_public_key }

12345 | devices[device_id] = { hw: identity_public_key, uv: (Attacker-controlled) uv_public_key }  
---|---  
  
From this point on, the attacker can use the forged UV key to request signatures for any passkey associated with the victim and obtain assertions with the UV bit set. This provides access to high-value accounts even when user verification is enforced and validated.

## Stealing the Master Key: The Golden Pass-Ta-Key Attack

In this attack, the attacker effectively gains the cloud authenticator’s superpower, the ability to decrypt synced passkeys. This is particularly impactful because it undermines the intended protection mechanism.

The passkey’s private key is protected using a symmetric master key called the security domain secret (SDS). This master key is not directly accessible, it is stored on the device as an encrypted wrapped_secret. Only the cloud authenticator can decrypt this wrapped_secret using its device-specific key (wrapping_key) within its isolated environment, as noted in Figure 5.

![A diagram showing a process between a client device and a cloud authenticator. Arrows indicate the flow from client device to cloud authenticator.](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/Pass-the-Passkey_-Figure-5-760x700.png)Figure 5. Synced passkey decryption inside the cloud authenticator.

_Figure 5. Synced passkey decryption inside the cloud authenticator._

This design aims to protect synced passkeys even if the client device is compromised. As Google noted in response to one of our [vulnerability reports](https://issues.chromium.org/issues/464996836):

“ _The (cloud) enclave authenticator’s primary function is to make it difficult to steal passkey private data, which would be an obvious target for malware if it were locally available._ ”

The security of this model ultimately hinges on the protection of the 32-byte SDS. If an attacker is able to obtain the SDS, they effectively gain the ability to decrypt all synced passkeys for that account. This allows them to authenticate as a fully verified user and take over every service where the victim relies on passkeys.

### **Leaking the SDS**

This secret should never be exposed to the client device, even during device loss or account recovery. However, we unexpectedly found the SDS present in Chrome’s logs during registration with the cloud authenticator, simply by opening chrome://device-log/FIDO, as noted in Figure 6.

![A screenshot showing a log entry with blurred sensitive information. It displays a JSON formatted message containing the command "keys/wrap" and the purpose labeled as "security domain secret."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/word-image-219134-184120-8-786x109.png)Figure 6. The SDS (the passkey master key) is exposed in plaintext in the device log.

In the current Chrome implementation, every device joining or rejoining an account’s security domain retrieves the SDS from the recovery key store, Google’s Trusted Vault service. The cloud authenticator includes a mechanism that allows Chrome to facilitate the recovery flow where the key cannot be decrypted on the client device, however this mechanism is not used. Instead, Chrome recovers the SDS in an accessible form.

One possible explanation is needing to standardize the device join and recovery process across platforms. Unlike desktop environments, Google Password Manager on iOS and Android does not rely on the cloud authenticator and must obtain the master key to decrypt synced passkeys. As a result, Chrome appears to follow the same recovery model, even though the cloud authenticator could enable a more isolated approach.

Although Google removed this secret from Chrome’s logging output [following our report](https://issuetracker.google.com/issues/464305542), the SDS is still sent to the client and remains accessible in Chrome’s process memory. If the attacker forces the victim to re-register with the cloud authenticator and knows the pattern to look for, they can extract the SDS directly from memory.

The Golden Pass-ta-key attack allows full account takeover through the following steps:

  1. The attacker forces Chrome to trigger a fresh onboarding using the same mechanisms as the Silver Pass-ta-key attack
  2. The attacker monitors the system for the recreation or modification of the passkey_enclave_state
  3. Once the file is recreated/modified, the attacker dumps Chrome’s process memory and extracts the SDS, which is temporarily present in plaintext
  4. The attacker reads the WebauthnCredentialSpecifics records from Chrome’s sync database (Stage Zero: Reconnaissance)
  5. Using the extracted SDS, the attacker decrypts the encrypted fields in each record and recovers the corresponding passkey private keys
  6. The attacker uses the recovered private keys to sign the relying party’s challenge and successfully authenticates as the victim



Figure 7 shows how an attacker would use the SDS to decrypt passkeys and forge a valid authentication response.

![A diagram illustrating an authentication attack involving entities like "Relying Party," "Attacker," "Infected Victim," and "Cloud Authenticator." The flow includes encrypted passkeys and a "Fake Authenticator" with steps labeled "challenge" and "assertion response." The attacker extracts a "Security Domain Secret."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/Pass-the-Passkey_-Figure-7-1-1422x700.png)Figure 7. Flow of the Golden Pass-ta-key attack.

Video 3 shows how an attacker uses the stolen SDS to log in to a high-value account (in this case, a crypto exchange).

&lt;br /&gt; 

_Video 3. How an attacker uses the stolen SDS to log in to a high-value account._

The Golden Pass-ta-key attack has a significantly broader impact. Beyond the reusable access from the attacker’s environment, the SDS allows the attacker to decrypt all existing passkeys as well as any future passkeys created for the account.

While the Silver attack is mitigated by unregistering or re-enrolling the device, the Golden attack provides strong persistence. Even if a compromise is detected, remediation is limited. In Google’s current implementation, there is no way to rotate or revoke the SDS, meaning all current and future synced passkeys remain protected by the same master key**.**

## Mitigations

### Enforce Strict User Verification (UV) Validation

Relying parties should require userVerification = required and validate the UV flag in all authentication responses. Failure to enforce this check can reduce authentication to a single factor. Figure 8 below shows the authenticator data layout.

![A diagram illustrating the structure of data fields, including RP ID Hash \(32 bytes\), Flags \(1 byte\), Counter \(4 bytes, big-endian unit32\), Attested Credential Data \(variable length if present\), and Extensions \(variable length if present, CBOR\). A red arrow highlights "Bit 2: User Verified \(UV\) result" in the Flags section, clarifying that "1 means the user is verified" and "0 means the user is not verified."](https://unit42.paloaltonetworks.com/wp-content/uploads/2026/07/word-image-227304-184120-11.png)Figure 8. Authenticator data layout. Source: [W3C, Web Authentication](https://www.w3.org/TR/webauthn-2/#sctn-authenticator-data).

### Validate Device Key Registration and Attestation

Credential managers should verify the origin and attestation of newly registered device keys, including UV and identity keys. Accepting arbitrary keys without validation allows unauthorized key registration and bypass of user verification requirements.

### Harden Recovery and Device Re-Registration Flows

Credential manager recovery PIN prompts are typically associated with onboarding or account recovery, not routine passkey authentication. Unexpected or repeated prompts during normal passkey usage may indicate re-triggering of onboarding or recovery, potentially due to phishing attempts or local manipulation of passkey state.

These flows are security-sensitive because recovery operations can re-establish device trust and restore access to synced credentials. In the scenarios from our research, triggering recovery enabled registration of new verification keys or exposure of key material used to decrypt synced passkeys.

Monitoring agents should detect and restrict unnecessary re-triggering of onboarding and recovery flows, especially after deletion or modification of local passkey state files. Additional verification should be required before re-establishing device trust or recovering synced credentials.

### Prevent Exposure of Sensitive Key Material on the Client

Sensitive material such as the master key should not be exposed to the client, including through memory or logs. Instead, credential managers should use designs where cryptographic operations are performed on behalf of the client, without transferring the underlying key material to the client environment.

### Restrict Access to Local Passkey Data

Access to passkey-related storage, such as Chrome’s sync database and local state files (e.g., passkey_enclave_state), should be limited to the browser process and protected through platform access controls. This reduces the ability to enumerate credentials, manipulate onboarding state or access device-bound key material from a compromised endpoint.

### Improve Detection of Abnormal Passkey Usage

WebAuthn defines a signature counter ([signCount](https://www.w3.org/TR/webauthn-2/#signature-counter)) mechanism intended to help relying parties detect cloned or unexpectedly reused credentials. In traditional authenticators, the counter increases with each authentication operation and can provide a signal of abnormal credential usage.

In synchronized passkey systems, authentication assertions commonly contain a constant signCount value. As a result, relying parties and credential providers have limited visibility into unauthorized use of synced credentials, including scenarios where passkeys are extracted or reused from unexpected environments.

[Google noted](https://issues.chromium.org/issues/465359916) that globally consistent signature counters are difficult to implement in synchronized passkey systems that operate across multiple devices and platforms, particularly when assertions originate from independent clients.

Credential managers that centrally coordinate authentication operations should consider implementing coordinated signature counter mechanisms that account for synchronization and multi-device consistency challenges. Such mechanisms can improve visibility and detection of unexpected credential usage or passkey reuse across environments.

## Conclusion

Passkeys represent a meaningful step forward in authentication security. By eliminating shared secrets, they reduce entire classes of attacks that have historically led to widespread account compromise. This changes the economics of credential theft and forces attackers to adopt new techniques.

The attacks presented in this research do not break the underlying cryptography. Instead, they exploit gaps between design assumptions and real-world implementations. These gaps include:

  * Trust placed in client devices
  * Inconsistencies in relying party validation
  * Weaknesses in onboarding and recovery flows



When combined with malware on the endpoint, these gaps enable account takeover scenarios that bypass the guarantees passkeys are expected to provide.

A central takeaway is that endpoint compromise remains a critical part of the threat model. When authentication decisions rely on signals from the user’s device, an attacker with access to that device can manipulate those signals in ways that are difficult to detect. Hardware-backed keys, secure enclaves and cloud isolation significantly raise the bar, but they do not fully eliminate this risk.

Passkey deployments should be treated as one layer in a broader security strategy. Relying parties must enforce strict validation, including proper handling of the user verification signal. Platform providers should continue hardening onboarding and recovery flows, and organizations should invest in protections against malware and memory access on endpoints.

As adoption continues to grow, so will attacker interest in this space. Understanding these emerging attack paths is essential to ensuring passwordless authentication delivers its intended security benefits in real-world conditions.

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

### Cortex Cloud Identity Security

[Cortex Cloud Identity Security](https://docs-cortex.paloaltonetworks.com/r/Cortex-CLOUD/Cortex-Cloud-Runtime-Security-Documentation/What-is-Cortex-Cloud-Identity-Security) encompasses Cloud Infrastructure Entitlement Management (CIEM), Identity Security Posture Management (ISPM), Data Access Governance (DAG) and Identity Threat Detection and Response (ITDR). It provides clients with the necessary capabilities to improve their identity-related security requirements by providing visibility into identities, and their permissions, within cloud and container environments. This helps accurately detect misconfigurations and unwanted access to sensitive data. It also allows real-time analysis surrounding usage and access patterns.

### Idira Threat Detection and Response

[Idira Threat Detection and Response (TDR)](https://docs.cyberark.com/detect-and-respond/latest/en/content/get-started/what-is-detect-and-respond.htm) enables security teams to counter identity-based attacks targeting Idira Next Generation Identity (NGI) Platform and the identities it secures. Using near real-time detection, powered by CORA AI, and leveraging Idira’s visibility across multiple contexts (like PAM, authentication, SSO, cloud, endpoints, browsers, and more), Idira ITP can apply automated, tailored non-disruptive in-session response to contain and minimize potential identity-based threats.

### Idira Endpoint Privilege Manager

[Idira Endpoint Privilege Manager (EPM)](https://docs.cyberark.com/epm/latest/en/content/intro/introduction.htm) enables enterprises to reduce risk, satisfy compliance, and streamline operations. It helps implement least privilege via policy-driven elevation and removal of standing admin rights, and blocks risky actions, such as execution of unvetted applications and access to memory of other processes, while providing audit-ready evidence and unified identity governance. Automation and consolidation improve efficiency and support Zero Trust strategies, strengthening security without slowing the business.

### Idira Privilege Access Management

[Idira Privilege Access Management ](https://docs.cyberark.com/secrets-manager-saas/latest/en/content/conjurcloud/cl_conjurcloudoverview.htm?tocpath=Get%20started%7C_____1)unifies privileged access across human, machine, and agentic identities to secure cloud access across multi-cloud environments. Building on proven PAM, it delivers centralized secrets management alongside modern controls like Just-in-Time access and Zero Standing Privileges. This enforces consistent least-privilege security across on-premises, cloud, and SaaS targets.

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

  * [The Art of the Invisible Key: Passkey Global Breakthrough](https://www.cyberark.com/resources/threat-research-blog/the-art-of-the-invisible-key-passkey-global-breakthrough) – CyberArk
  * [Google Cloud Authenticator: The Hidden Mechanisms of Passwordless Authentication](https://unit42.paloaltonetworks.com/passwordless-authentication/) – Palo Alto Networks Unit 42



Back to top

### Tags

  * [Google authenticator](https://unit42.paloaltonetworks.com/tag/google-authenticator/ "google authenticator")
  * [Google Chrome](https://unit42.paloaltonetworks.com/tag/google-chrome/ "Google Chrome")
  * [Google Cloud](https://unit42.paloaltonetworks.com/tag/google-cloud/ "Google Cloud")
  * [Identity](https://unit42.paloaltonetworks.com/tag/identity/ "identity")
  * [Key](https://unit42.paloaltonetworks.com/tag/key/ "key")
  * [Passkey](https://unit42.paloaltonetworks.com/tag/passkey/ "passkey")
  * [Passwordless](https://unit42.paloaltonetworks.com/tag/passwordless/ "passwordless")



[ Threat Research Center ](https://unit42.paloaltonetworks.com "Threat Research") [ Next: The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version ](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/ "The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version")

### Table of Contents

  *   * Executive Summary
  * Setting the Stage
  * Stage Zero Reconnaissance
  * Device Identity Impersonation: The Pass-Ta-Key Attack
    * UV Flag: When MFA Depends on a Single Bit
  * Pending Attacker: The Silver Pass-Ta-Key Attack
    * Invalidating the Existing User Verification Key
    * Exploiting the Onboarding Flow
  * Stealing the Master Key: The Golden Pass-Ta-Key Attack
    * Leaking the SDS
  * Mitigations
    * Enforce Strict User Verification (UV) Validation
    * Validate Device Key Registration and Attestation
    * Harden Recovery and Device Re-Registration Flows
    * Prevent Exposure of Sensitive Key Material on the Client
    * Restrict Access to Local Passkey Data
    * Improve Detection of Abnormal Passkey Usage
  * Conclusion
    * Cortex Cloud Identity Security
    * Idira Threat Detection and Response
    * Idira Endpoint Privilege Manager
    * Idira Privilege Access Management
  * Additional Resources



### Related Articles

  * [ Inside the Modern SOC: The Identity Front Door ](https://unit42.paloaltonetworks.com/soc-identity-front-door/ "article - table of contents")
  * [ The Global Namespace Risk: Universal Bucket Hijacking Technique for Cloud Data Exfiltration ](https://unit42.paloaltonetworks.com/cloud-bucket-hijacking-risks/ "article - table of contents")
  * [ Pickle in the Middle – Hijacking Vertex AI Model Uploads for Cross-Tenant RCE ](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/ "article - table of contents")



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
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")



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
  * [Malware](https://unit42.paloaltonetworks.com/tag/malware/ "malware")
  * [Threat intelligence](https://unit42.paloaltonetworks.com/tag/threat-intelligence/ "threat intelligence")



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



![Close button](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/close-modal.svg) ![Enlarged Image](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/)