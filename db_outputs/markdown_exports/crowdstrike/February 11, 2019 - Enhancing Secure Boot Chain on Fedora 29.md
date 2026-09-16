# Enhancing Secure Boot Chain on Fedora 29

- **Source :** crowdstrike
- **URL :** https://www.crowdstrike.com/en-us/blog/enhancing-secure-boot-chain-on-fedora-29/
- **Date :** February 11, 2019

---

# Enhancing Secure Boot Chain on Fedora 29

February 11, 2019

• [ Hanno Heinrichs and Florent Hochwelker](/en-us/blog/author.hanno-heinrichs-and-florent-hochwelker/ "Posts by Hanno Heinrichs and Florent Hochwelker") • [Threat Hunting & Intel](/en-us/blog/category.counter-adversary-operations/ "Threat Hunting & Intel")


_This blog is from the CrowdStrike Intelligence Advanced Research Team_

## Motivation

What is worse than a failing system? A (silently) compromised, yet operational system! While there are many attack vectors that allow for the compromise of a modern computer system, Secure Boot tries to address one of them: It aims to secure the pre-boot environment against unauthenticated manipulations such as rootkits and bootkits. It was introduced in the [Unified Extensible Firmware Interface (UEFI) 2.3.1 ](https://uefi.org/sites/default/files/resources/UEFI_2_3_1_C.pdf)specification (Errata C) in 2012, and has widely been adopted by computer manufacturers since then. The basic idea behind Secure Boot is that the UEFI firmware may only redirect control flow to those bootloaders that it could cryptographically verify against a pre-distributed set of public keys, signatures and hashes of executable modules. While such efforts may sound appealing at first, security-conscious individuals may have the following concerns:

  * What entities actually have control over the private key counterparts?
  * What entities are entitled to enroll or update public keys, signatures and hashes in UEFI firmware?
  * How far does my Linux distribution extend the chain of trust?
  * Can mechanisms like Fedora’s “shim” or Linux Foundation’s “pre-bootloader” be used to execute unsigned code?



In this blog, we will describe the standard Secure Boot configuration of a Fedora 29 installation on a Dell Latitude E5470 laptop, which we use in our day-to-day work, and show you how to harden it to a reasonable extent.

## Make it **Your** Platform

The UEFI acts as a trust anchor for the Secure Boot chain. It contains a _Platform Key_ (PK), a _Key Exchange Key_ database (KEK), a _Signature Database_ (db) and a _Forbidden Signature Database_ (dbx), which are all stored in so-called UEFI variables. A good read on what these keys and databases are used for can be found in [the blog by James Bottomley](https://blog.hansenpartnership.com/the-meaning-of-all-the-uefi-keys/)

or in the [Ubuntu Wiki](https://wiki.ubuntu.com/UEFI/SecureBoot/Testing). Typical implementations will have a hardware OEM’s key stored in PK, and OS vendor keys stored in KEK and db. On a Dell Latitude E5470, the following keys were found to be pre-installed:

  * **PK**
    * Issuer: DC=com, DC=dell, CN=Configuration, CN=Services, CN=Public Key Services, CN=AIA, CN=Dell Inc. Issuing CA 1 Subject: DC=com, DC=dell, OU=1, OU=Signing, CN=Dell Inc. UEFI Platform Key Expired in 2014, Digital Signature, Code Signing, not a CA
  * **KEK**
    * Issuer: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Corporation Third Party Marketplace Root Subject: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Corporation KEK CA 2011 Digital Signature, Certificate Sign, CRL Sign, CA
  * **db**
    * Issuer: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Root Certificate Authority 2010 Subject: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Windows Production PCA 2011 Digital Signature, Certificate Sign, CRL Sign, CA
    * Issuer: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Corporation Third Party Marketplace Root Subject: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Corporation UEFI CA 2011 Digital Signature, Certificate Sign, CRL Sign, CA



In total, there are three Microsoft-owned keys eligible for signing binaries installed (KEK and two db entries), as well as a PK from Dell which would allow the modification of the KEK and db. As the end user cannot verify which parties the corresponding private keys have been shared with, it is not unreasonable to deploy your own keys on your hardware. The certificates and keys can be created as follows:

`$ openssl req -new -x509 -newkey rsa:2048 -subj "/CN=John Doe UEFI Platform Key.html" -keyout PK.key -out PK.crt -days 3650 -sha256` `$ openssl req -new -x509 -newkey rsa:2048 -subj "/CN=John Doe UEFI Key Exchange Key.html" -keyout KEK.key -out KEK.crt -days 3650 -sha256` `$ openssl req -new -x509 -newkey rsa:2048 -subj "/CN=John Doe Signing Key.html" -keyout db.key -out db.crt -days 3650 -sha256`

Finally, the PK needs to be converted to a (self-)signed EFI signature list as follows:

`$ cert-to-efi-sig-list -g "$(uuidgen)" PK.crt PK.esl $ sign-efi-sig-list -k PK.key -c PK.crt PK PK.esl PK.auth Timestamp is 2019-1-16 13:41:35 Authentication Payload size 887 Signature of size 1217 Signature at: 40`

Both programs, `cert-to-efi-sig-list` and `sign-efi-sig-list` are part of the [Linux EFI toolkit ](https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git). However, Fedora does not seem to ship such a package. Therefore, you will need to compile it yourself after making some minor changes to the Makefile (please see Appendix A). Even though it is typically possible to reset the enrolled keys back to their defaults from System setup, it is probably a good idea to back up what is currently stored in the respective UEFI variables. This can be done with the help of the `efi-readvar` program, which is also part of the Linux EFI Tools.

`# efi-readvar -v PK -o PK.esl Variable PK, length 1395 # efi-readvar -v KEK -o KEK.esl Variable KEK, length 1560 # efi-readvar -v db -o db.esl Variable db, length 3143 # efi-readvar -v dbx -o dbx.esl Variable dbx, length 2343`

With all relevant UEFI variables backed up, they can now be cleared. To do so, reboot the machine and enter System Setup. Under “Expert Key Management,” change the Secure Boot mode of operation to “Custom Mode” and choose “Delete All Keys.” Then boot the machine and verify that the UEFI variables actually got cleared:

`# efi-readvar Variable PK has no entries Variable KEK has no entries Variable db has no entries Variable dbx has no entries Variable MokList has no entries`

The installation of the new keys is also easy and can be achieved conveniently without rebooting:

`# efi-updatevar -c KEK.crt KEK # efi-updatevar -c db.crt db # efi-updatevar -f PK.auth PK`

A final check on the variables should reveal that the changes were successful:

`# efi-readvar` `Variable PK, length 847` `PK: List 0, type X509` `Signature 0, size 819, owner b26f3b13-7627-4abd-8ff7-09d12d4a988a` `Subject:` `CN=John Doe UEFI Platform Key` `Issuer:` `CN=John Doe UEFI Platform Key` `Variable KEK, length 855` `KEK: List 0, type X509` `Signature 0, size 827, owner 605dab50-e046-4300-abb6-3dd810dd8b23` `Subject:` `CN=John Doe UEFI Key Exchange Key` `Issuer:` `CN=John Doe UEFI Key Exchange Key` `Variable db, length 845` `db: List 0, type X509` `Signature 0, size 817, owner 605dab50-e046-4300-abb6-3dd810dd8b23` `Subject:` `CN=John Doe UEFI Signing Key` `Issuer:` `CN=John Doe UEFI Signing Key` `Variable dbx has no entries` `Variable MokList has no entries`

Home sweet home.

## Custom Shim Deployment

With custom keys enrolled, it is time to think about what to actually sign and verify with them. Both Fedora and Ubuntu, for example, use the so-called "shim" as a first-stage bootloader. The shim is signed by Microsoft and includes a signing certificate of the respective Linux distribution. Subsequently, the shim verifies and loads the second stage, for example, GRUB. Finally, before booting a kernel, GRUB validates that it carries a valid signature by calling back into the shim. If Secure Boot is enabled and the validation succeeds, the Linux kernel is booted and will subsequently detect that it was started as part of a Secure Boot chain. This will cause it to enable several additional security mechanisms, for example:

  * It will require that modules are signed by a distribution-specific public key before loading them.
  * It will disable functionality such as kexec or hibernation. The rationale here is that these features might allow the start of a compromised, unsigned kernel from a securely booted, signed kernel.



Neither GRUB nor the kernel validate the GRUB configuration or any userspace components of the initial RAM disk, both of which are also part of the boot process. The initial ramdisk could be an especially valuable target for malicious modification as it usually handles setting up encryption during boot, i.e., it prompts for encryption passphrases and unlocks encrypted devices. Furthermore, Fedora’s shim mechanismas well as the [Linux Foundation’s pre-bootloader mechanism](https://blog.hansenpartnership.com/linux-foundation-secure-boot-system-released/)can be used to enroll hashes of arbitrary unsigned binaries into UEFI’s Machine Owner Key (MOK) variable during a system’s startup phase. To do so, the system does not need to be in “Setup Mode” and a user does not need to provide any credentials like the UEFI supervisor password. Afterwards, such unsigned binaries are allowed to execute, as long as the system is booted via [one of the two mechanisms](https://lwn.net/Articles/519618/). Depending on your threat model, such behavior may be unwanted. To address these drawbacks, it is possible to replace the shim with a customized GRUB boot image that verifies configuration files created by Fedora before loading them, and subsequently, also verifies any kernels and initial ramdisks it loads. This is facilitated with the help of [GRUB’s `check_signature` setting](https://www.gnu.org/software/grub/manual/grub/html_node/Using-digital-signatures.html). To build the customized GRUB boot image, create a file called _memdisk.tar_ with the following directory structure:

  * boot
    * grub
      * grub.cfg



The contained `grub.cfg` checks the integrity of the second-stage GRUB config and loads it:

`menuentry "Signed Internal Drive" --unrestricted {

# load a signed stage2 configuration from boot drive

if verify_detached (hd0,gpt1)/EFI/fedora/grub.cfg (hd0,gpt1)/EFI/fedora/grub.cfg.sig; then

configfile (hd0,gpt1)/EFI/fedora/grub.cfg

elif verify_detached (hd0,msdos1)/EFI/fedora/grub.cfg (hd0,msdos1)/EFI/fedora/grub.cfg.sig; then

configfile (hd0,msdos1)/EFI/fedora/grub.cfg

else

echo Could verify neither (hd0,gpt1)/EFI/fedora/grub.cfg nor (hd0,msdos1)/EFI/fedora/grub.cfg

fi }`

Additionally, another GRUB configuration file must be created in order to lock down the bootloader in a way that requires authentication before it allows changes to the boot options. The _DEADBEEF_ hash should be replaced with your own password derivation (use `grub2-mkpasswd-pbkdf2 --iteration-count=65536` for that):

`set pager=1 set gfxpayload=keep set gfxmode=auto``set superusers=admin password_pbkdf2 admin grub.pbkdf2.sha512.65536.DEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF``set check_signatures=enforce`

Note that this configuration also sets the `check_signatures` flag to “enforce”. The final component of the first-stage GRUB is the public key of the GPG key pair. Alternatively, we can use an existing one. That key pair will later be used for signing and verifying kernels, ramdisks, and Fedora’s GRUB configuration files. A new key pair can be generated as follows: `gpg2 --generate-key --default-new-key-algo rsa2048` Afterwards, we need to export the public key as a DER encoded file: `gpg2 --output pubkey.gpg --export john.doe@example.org` Finally, we can create the unsigned first-stage GRUB by using `grub2-mkimage:`

`grub2-mkimage --format=x86_64-efi --output=grub-verify-unsigned.efi --config=grub.cfg \ --pubkey=pubkey.gpg --memdisk=memdisk.tar \ all_video boot btrfs cat chain configfile echo efifwsetup efinet ext2 fat font gfxmenu gfxterm \ gzio halt hfsplus iso9660 jpeg loadenv loopback lvm mdraid09 mdraid1x minicmd normal part_apple \ part_msdos part_gpt password_pbkdf2 png reboot search search_fs_uuid search_fs_file search_label \ serial sleep syslinuxcfg test tftp video xfs backtrace usb usbserial_common usbserial_pl2303 \ usbserial_ftdi usbserial_usbdebug linux tar memdisk verify gcry_rsa gcry_dsa gcry_sha256 hashsum`

The last step is to sign the newly created first-stage GRUB with `sbsign` from the `sbsigntools` package: `sbsign --key db.key --cert db.crt --output grub-verify.efi grub-verify-unsigned.efi` Now the signed EFI binary can be copied over to the boot partition: `mkdir -p /boot/efi/EFI/grub-verify cp grub-verify.efi /boot/efi/EFI/grub-verify/`

## Automating the Signature Creation Process

Often, security mechanisms get in the way of day-to-day tasks, and that's also the case here. While we have now successfully created a secure boot chain that validates the boot loader, kernel, and initramfs, manually repeating these steps and signing every kernel or initramfs upgrade would be a tedious task; and if we were to forget to do it, we might end up with an unbootable system.Luckily, Linux distributions typically perform various automated tasks when upgrading any of these components, and we can hook into these tasks. Fedora is no exception. In this section we describe the Fedora-specific changes we made to allow for semi-automatic signing of kernels, ramdisks, and GRUB configurations. The following code was appended to `/etc/default/grub` and ensures automatic re-signing of `grub.cfg`, whenever it needs to be changed:

`GPG_SIGN_HOMEDIR="/home/jd/.gnupg"` `GPG_SIGN_KEYID="1F439B99B7981A8EB6CEE97F0F088D703EF16F6C"``grub_cfg="${grub_cfg:-/boot/efi/EFI/fedora/grub.cfg}"` `# /etc/default/grub is sourced by grub2-mkconfig after grub-mkconfig_lib is` `# sourced. Overwrite grub_file_is_not_garbage to also ignore signature files.` `echo default grub $0 "${@}"` `grub_file_is_not_garbage ()` `{` `

if test -f "$1" ; then` `

case "$1" in` `

*.dpkg-*) return 1 ;; # debian dpkg` `

*.rpmsave|*.rpmnew) return 1 ;;` `

*.sig) return 1 ;;` `

README*|*/README*)

return 1 ;; # documentation` `

esac` `

else` `

return 1` `

fi` `

return 0` `}` `# Unfortunately, this is not sufficient, as /etc/grub.d/10_linux sources` `# grub-mkconfig_lib again. It does try to do so from "${pkgdatadir}" though, so` `# that we can make it use a patched lib:` `TMPDIR="$(mktemp -d)"` `sed -e 's,\*\.rpmsave<^)>*),*.rpmsave|*.rpmnew|*.sig),' /usr/share/grub/grub-mkconfig_lib > "${TMPDIR}/grub-mkconfig_lib"` `export pkgdatadir="${TMPDIR}"` `cleanup() {` `

rm -rf "${TMPDIR}"` `}` `function sign() {` `

>&2 echo "About to create signature of '${grub_cfg}' with GPG key '${GPG_SIGN_KEYID}'"` `

# Don't warn about permissions, we're root and the homedir belongs to a` `

# different user, so that's okay.` `

gpg2 --quiet --no-permission-warning --homedir "${GPG_SIGN_HOMEDIR}" --detach-sign --default-key "${GPG_SIGN_KEYID}" < "${grub_cfg}" > "${grub_cfg}.sig"` `

cleanup` `}` `trap sign EXIT` `trap cleanup TERM INT`

The following post kernel installation hook in `/etc/kernel/postinst.d/99-sign-kernel.sh` is responsible for signing new kernels and ramdisks after their installation:

`#!/bin/sh` `# On Fedora, copy to /etc/kernel/postinst.d to automatically sign new kernels,` `# initramfs images and grub configuration on kernel package installations` `PATH="/bin:/usr/bin:/sbin:/usr/sbin"` `SELF="$(readlink -f "${0}")"` `KERNEL_VERSION="${1}"` `KERNEL_IMAGE="${2}"` `MAIN_GRUB_CFG="/boot/efi/EFI/fedora/grub.cfg"` `GPG_SIGN_HOMEDIR="/home/jd/.gnupg"` `GPG_SIGN_KEYID="1F439B99B7981A8EB6CEE97F0F088D703EF16F6C"` `echo "$(date)" "${0}" "${@}" > $(mktemp /tmp/signkernel-XXXXXXXXXX.log)` `sha256sum /boot/efi/EFI/fedora/grub.cfg` `function sign() {` `

echo "About to sign file '${1}' with GPG key '${GPG_SIGN_KEYID}'"` `

# Don't warn about permissions, we're root and the homedir belongs to a` `

# different user, so that's okay.` `

gpg2 --quiet --no-permission-warning --homedir "${GPG_SIGN_HOMEDIR}" --detach-sign --default-key "${GPG_SIGN_KEYID}" < "${1}" > "${1}.sig"` `}``sign "${MAIN_GRUB_CFG}"` `sign "${KERNEL_IMAGE}"` `sign "/boot/initramfs-${KERNEL_VERSION}.img"`

The last hook removes obsolete signatures when kernels get removed. The pre-kernel removal hook resides in `/etc/kernel/prerm.d/99-rm-sigs.sh`:

`#!/bin/sh``# On Fedora, copy to /etc/kernel/prerm.d to automatically remove signatures on` `# kernel package deinstallation``PATH="/bin:/usr/bin:/sbin:/usr/sbin"` `SELF="$(readlink -f "${0}")"``KERNEL_VERSION="${1}"` `KERNEL_IMAGE="${2}"``rm "${KERNEL_IMAGE}.sig"` `rm "/boot/initramfs-${KERNEL_VERSION}.img.sig"`

Please note that the two variables, `GPG_SIGN_HOMEDIR` and `GPG_SIGN_KEYID`, need to be changed to reflect the path to your GnuPG directory, as well as your signing key ID. You probably also need to `export GPG_TTY=$(tty)` in `/root/.bashrc` if you intend to run `dnf` as root. In order to test the hooks, you can re-install the current kernel as follows: `dnf reinstall kernel-core` During the process, you should be prompted to unlock your GPG signing key once. Afterward, the following signatures should have been created:

`# find /boot -name '*.sig'` `/boot/initramfs-4.20.3-200.fc29.x86_64.img.sig` `/boot/vmlinuz-4.20.3-200.fc29.x86_64.sig` `/boot/efi/EFI/fedora/grub.cfg.sig`

You should now be able to reboot into your firmware and make `grub-verify.efi` the only allowed boot entry. Lastly, you should protect your firmware settings with a strong password to prevent tampering. If all went well, you should see two instances of GRUB during the boot process before reaching Plymouth.

## Best Practices and Attack Surface

### **Protection of Private Keys**

The private key half of any PK, KEK, or db is a valuable target for an attacker. Therefore, it makes sense to reduce the number of entities who have control over such keys as far as possible. We tried to achieve this by enrolling our own keys. In our setup, these private keys are only known to the machine owner. They are encrypted with a unique passphrase and stored externally. For the day-to-day signing of kernels, ramdisks and GRUB configuration files, we use GPG keys that are also encrypted. They are unlocked on a per request basis with the help of a unique passphrase. However, a residual risk of GPG key compromise remains.

### **BIOS rootkit**

For a remote attacker, the UEFI could be rewritten in order to inject a BIOS bootkit and get a full persistence on the system even if the victim changes or formats the hard drive. If the BIOS is reflashed with a custom one, or if the SPI Flash is overwritten, the whole signature chain we setup is vulnerable. The BIOS must use all the enforce features in order to protect against any rewrite of the SPI flash, certificates or a reflashing via the “update firmware” feature. Most modern BIOS use a signature check before updating. This verification does not protect against memory corruption vulnerabilities before or during the signature check. Security audits that employ reverse engineering and fuzzing of the latest available firmware update is the only solution against unwanted backdoor “features” or vulnerabilities like buffer overflows. One such endeavour was described by [Kallenberg, Butterworth, Cornwell, and Kovah](https://conference.hitb.org/hitbsecconf2013kul/materials/D1T1%20-%20Kallenberg,%20Kovah,%20Butterworth%20-%20Defeating%20Signed%20BIOS%20Enforcement.pdf). Any misconfiguration by a platform-specific BIOS implementation can lead to security-relevant vulnerabilities. In order to protect the chipset against any rewrite attacks, the BIOS Control register (BIOS CNTL) must be correctly set. The [open-source Chipsec framework](https://github.com/chipsec/chipsec)

can be used to dump this register and check similar misconfigurations:

`# python chipsec_main.py -m common.bios_wp``<*> running module: chipsec.modules.common.bios_wp` `< =======================================================================` `< Module: BIOS Region Write Protection` `< =======================================================================` `<*> BC = 0x000002AA << BIOS Control (b:d.f 00:31.5 + 0xDC)` `<00> BIOSWE = 0 << BIOS Write Enable` `<01> BLE = 1 << BIOS Lock Enable` `<02> SRC = 2 << SPI Read Configuration` `<04> TSS = 0 << Top Swap Status` `<05> SMM_BWP = 1 << SMM BIOS Write Protection` `<06> BBS = 0 << Boot BIOS Strap` `<07> BILD = 1 << BIOS Interface Lock Down` `<+> BIOS region write protection is enabled (writes restricted to SMM)`

The BIOS Control register needs to have the BIOS Write Enable (BIOSWE) bit set to 0 as it will protect the SPI flash memory from being overwritten. However, this bit can be set back to 1 from ring 0. If BLE is set to 1, a System Management Interrupt (SMI) will be triggered and set back BIOSWE to 0. This implementation is vulnerable to race condition attacks. Therefore, the BIOS should have the SMM_BWP bit set to 1 as it will require the processor to be in System Management Mode (SMM) in order to modify this register. Chipsec tells you if it detects any problems. The command `python chipsec_main.py` can be used to check if every mitigation against other advanced attacks like SMM cache poisoning are enabled. DMA attack could also be mitigated by an IOMMU engine like the Intel

Virtualization Technology for Directed I/O (VT-d). Finally, with the Intel

BootGuard technology (since the 4th Intel**®**), the root of trust is locked by hardware. During the manufacturing process, the public key of the BIOS signature is burned into the field programmable fuses (FPFs) in the Intel****

****

**** Management Engine (ME). This memory region is one-time programmable. During each subsequent boot, the firmware signature is checked by the processor, and therefore, prevents any malicious modifications. Only verified and trusted firmware can be executed. However, vulnerabilities were found in the past in the manufacturer’s implementation of [BootGuard ](https://github.com/REhints/BlackHat_2017/blob/master/Betraying%20the%20BIOS.pdf). Because CPU and chipset need to be physically connected to fuse the public key, a self-assembled computer will not have BootGuard functionality. In the BIOS settings there are also a few things to disable:

  * BIOS Downgrade: Except if you plan to downgrade your BIOS, it is advisable to disable BIOS downgrades. This would prevent attackers from installing older firmwares with known vulnerabilities.
  * Absolute (CompuTrace)’s LoJack: A feature to find and/or wipe a laptop in case it gets stolen. However, this is facilitated by bootkit-like means.
  * BIOS encapsulate update from Windows or Linux: If one is already on the latest firmware version that is available, this option could be cleared until the next update gets published (if any).



### **Physical access**

If attackers gain physical access to a computer they will be able to compromise the BIOS or boot partition, regardless of any disk encryption. Because we use our own certificate and SecureBoot is enabled, attackers cannot use a malicious bootloader without our private key. However, attackers could disable SecureBoot in the BIOS. By adding an administrator passphrase, we slow down the attackers but also force them to either reset the BIOS or use a master passphrase. Some vendors can compute master passphrases that unlock the BIOS settings, in case customers forget their own. Depending on the BIOS and vendor, the master passphrase can be computed from the laptop serial number or from the hash shown on the screen after [three bad attempts.](https://github.com/bacher09/pwgen-for-bios) Do not let someone get physical access to your laptop.

## Appendix

### A) Linux EFI Tools Patch

`$ git diff` `diff --git a/Make.rules b/Make.rules` `index 903a5a4..6567a2f 100644` `--- a/Make.rules` `+++ b/Make.rules` `@@ -17,14 +17,17 @@ INCDIR

= -I$(TOPDIR)include/ -I/usr/include/efi -I/usr/include/efi/$(ARCH) -I` `CPPFLAGS

= -DCONFIG_$(ARCH)`` CFLAGS

= -O2 -g $(ARCH3264) -fpic -Wall -fshort-wchar -fno-strict-aliasing -fno-merge-constants -fno-stack-protector -ffreestanding -fno-stack-check` `LDFLAGS

= -nostdlib` `-CRTOBJ

= crt0-efi-$(ARCH).o` `+CRTOBJ

= crt0-efi-x64.o` `CRTPATHS

= /lib /lib64 /lib/efi /lib64/efi /usr/lib /usr/lib64 /usr/lib/efi /usr/lib64/efi /usr/lib/gnuefi /usr/lib64/gnuefi` `CRTPATH

= $(shell for f in $(CRTPATHS); do if < -e $$f/$(CRTOBJ) >; then echo $$f; break; fi; done)` `CRTOBJS

= $(CRTPATH)/$(CRTOBJ)` `# there's a bug in the gnu tools ... the .reloc section has to be` `# aligned otherwise the file alignment gets screwed up` `-LDSCRIPT

= elf_$(ARCH)_efi.lds` `-LDFLAGS

+= -shared -Bsymbolic $(CRTOBJS) -L $(CRTPATH) -L /usr/lib -L /usr/lib64 -T $(LDSCRIPT)` `+LDSCRIPT

= elf_x64_efi.lds` `/usr/lib -L /usr/lib64 -T $(LDSCRIPT)` `+LDFLAGS

+= -shared -Bsymbolic $(CRTOBJS) -L $(CRTPATH) -L /usr/lib -L /usr/lib64 -L /usr/lib64/gnuefi -T $(LDSCRIPT)` `LOADLIBES

= -lefi -lgnuefi $(shell $(CC) $(ARCH3264) -print-libgcc-file-name)` `FORMAT

= --target=efi-app-$(ARCH)` `OBJCOPY

= objcopy`

#### **Additional Resources**

  * Hear a comprehensive discussion of today’s top cyberthreats by CrowdStrike experts: register for a webinar on the

[ 2020 Global Threat Report](/resources/reports/2020-crowdstrike-global-threat-report.html)
  * Learn more about comprehensive endpoint protection with the CrowdStrike Falcon® platform by [visiting the product page](/en-us/products/).
  * Test CrowdStrike next-gen AV for yourself. Start your [free trial of Falcon Prevent™](/en-us/resources/free-trials/try-falcon-prevent/) today.



[ ](https://www.linkedin.com/shareArticle) [ ](https://twitter.com/share)

* * *

#### Related Content

[ ![PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-InfoStealer?wid=2048&hei=1349&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 15, 2026  PhantomRaven: An LLM-Generated Information Stealer Developed for Bug Bounty Hunting ](/en-us/blog/phantomraven-llm-generated-information-stealer-for-bug-bounty-hunting/) [ ![Peer Pressure: Inside the Sality Botnet Disruption Operation](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-FalCon-Sality?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Sep 01, 2026  Peer Pressure: Inside the Sality Botnet Disruption Operation ](/en-us/blog/inside-sality-botnet-disruption-operation/) [ ![CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates](https://assets.crowdstrike.com/is/image/crowdstrikeinc/Blog-THR-2026?wid=1060&hei=698&fmt=png-alpha&qlt=95,0&resMode=sharp2&op_usm=3.0,0.3,2,0) Threat Hunting & Intel | Aug 03, 2026  CrowdStrike 2026 Threat Hunting Report: Exploitation Window Closes as AI Use Accelerates ](/en-us/blog/crowdstrike-2026-threat-hunting-report/)