<h3 align="center">Jr Penetration Tester &nbsp;&nbsp; · &nbsp;&nbsp; Web Application Security Fundamentals</h3><h1  align="center"><a href="https://tryhackme.com/room/webserverattacks2">Web Server Attacks - II</a></h1>
<p align="center">Attack IIS through fingerprinting, tilde enumeration, WebDAV shell upload, and learn automation.<br><br>
<img width="1200px" src="https://github.com/user-attachments/assets/2e7578b1-66d7-4ba9-9f62-850193bc73f7"><br>If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/badge/Follow-GitHub-24292e?style=for-the-badge&logo=github" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAY%2031-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p><br>

<br>
<h2>Task 1 - Introduction</h2>

<p><em>Answer the question below </em></p>

<p>1.1. I have deployed the virtual machines!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 - IIS Fingerprinting and Enumeration</h2>

<p><em>Answer the questions below </em></p>

<p>2.1. What HTTP response header reveals the IIS version?<br>
<code>Server</code></p>

<p>2.2. What is the HTTP response code after executing the PUT request on the <code>/webdav</code> directory?<br>
<code>Server</code></p>


<br>
<h2>Task 3 - IIS Tild (Short Filename) Enumeration</h2>

<p><em>Answer the questions below </em></p>

<p>3.1. What character in a URL path triggers the IIS tilde enumeration response difference?<br>
<code>~</code></p>

<p>3.2.What legacy Windows filename format does the tilde enumeration vulnerability exploit? (Answer Format: X.X)<br>
<code>8.3</code></p>

<p>3.3. What password is stored in the file discovered through tilde enumeration?<br>
<code>P@ssw0rd!123</code></p>

<br>
<h2>Task 4 - WebDAV Exploitation: Uploading an ASPC Shell</h2>

<p><em>Answer the questions below </em></p>

<p>4.1. What HTTP status code confirms a file was successfully created via <code>PUT</code>?<br>
<code>201</code></p>

<p>4.2.What <code>curl</code>code> flag is required to authenticate with NTLM when uploading via WebDAV?<br>
<code>--ntlm</code></p>

<br>
<h2>Task 5 - ASPX Web Shells</h2>

<p><em>Answer the questions below </em></p>

<p>5.1. After triggering the ASPX shell, what user account is returned by the <code>whoami</code> command? (Answer Format: lowercase, e.g., nt authority\system)<br>
<code>iis apppool\defaultapppool</code></p>

<p>5.2. What Windows privilege, visible in <code>whoami /priv</code> output from the reverse shell, enables Potato-style privilege escalation from an IIS shell?<br>
<code>SeImpersonatePrivilegentlm</code></p>

<br>
<h2>Task 6 - IIS Misconfiguration</h2>


<h3>Misconfiguration 1: Directory Listing Enabled</h3>

```bash
# curl http://10.67.155.50/uploads/
<html><head><title>10.67.155.50 - /uploads/</title></head><body><H1>10.67.155.50 - /uploads/</H1><hr>

<pre><A HREF="/">[To Parent Directory]</A><br><br> 4/13/2026  2:25 PM           31 <A HREF="/uploads/config.bak">config.bak</A><br> 4/13/2026
```

<h3>Misconfiguration 2: HTTP PUT and DELETE Without Authentication</h3>

```bash
# curl -X OPTIONS http://10.67.155.50/ -sv 2>&1 | grep "Allow:"
< Allow: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, DELETE, MOVE, PROPPATCH, MKCOL, LOCK, UNLOCK
```

<h3>Misconfiguration 3: web.config Exposure</h3>

```bash
# curl http://10.67.155.50/web.config
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>404 - File or directory not found.</title>
<style type="text/css">
<!--
body{margin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;}
fieldset{padding:0 15px 10px 15px;} 
h1{font-size:2.4em;margin:0;color:#FFF;}
h2{font-size:1.7em;margin:0;color:#CC0000;} 
h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;} 
#header{width:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;
background-color:#555555;}
#content{margin:0 0 0 2%;position:relative;}
.content-container{background:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;}
-->
</style>
</head>
<body>
<div id="header"><h1>Server Error</h1></div>
<div id="content">
 <div class="content-container"><fieldset>
  <h2>404 - File or directory not found.</h2>
  <h3>The resource you are looking for might have been removed, had its name changed, or is temporarily unavailable.</h3>
 </fieldset></div>
</div>
</body>
</html>
```


<h3>Misconfiguration 4: Verbose Error Messages</h3>

<p>...</p>

<h3>Misconfiguration 5: trace.axd Left Enabled</h3>

```bash
# curl http://10.67.155.50/trace.axd
<html>
<head>
<style type="text/css">
span.tracecontent b { color:white }
span.tracecontent { background-color:white; color:black;font: 10pt verdana, arial; }
span.tracecontent table { clear:left; font: 10pt verdana, arial; cellspacing:0; cellpadding:0; margin-bottom:25}
span.tracecontent tr.subhead { background-color:#cccccc;}
span.tracecontent th { padding:0,3,0,3 }
span.tracecontent th.alt { background-color:black; color:white; padding:3,3,2,3; }
span.tracecontent td { color: black; padding:0,3,0,3; text-align: left }
span.tracecontent td.err { color: red; }
span.tracecontent tr.alt { background-color:#eeeeee }
span.tracecontent h1 { font: 24pt verdana, arial; margin:0,0,0,0}
span.tracecontent h2 { font: 18pt verdana, arial; margin:0,0,0,0}
span.tracecontent h3 { font: 12pt verdana, arial; margin:0,0,0,0}
span.tracecontent th a { color:darkblue; font: 8pt verdana, arial; }
span.tracecontent a { color:darkblue;text-decoration:none }
span.tracecontent a:hover { color:darkblue;text-decoration:underline; }
span.tracecontent div.outer { width:90%; margin:15,15,15,15}
span.tracecontent table.viewmenu td { background-color:#006699; color:white; padding:0,5,0,5; }
span.tracecontent table.viewmenu td.end { padding:0,0,0,0; }
span.tracecontent table.viewmenu a {color:white; font: 8pt verdana, arial; }
span.tracecontent table.viewmenu a:hover {color:white; font: 8pt verdana, arial; }
span.tracecontent a.tinylink {color:darkblue; background-color:black; font: 8pt verdana, arial;text-decoration:underline;}
span.tracecontent a.link {color:darkblue; text-decoration:underline;}
span.tracecontent div.buffer {padding-top:7; padding-bottom:17;}
span.tracecontent .small { font: 8pt verdana, arial }
span.tracecontent table td { padding-right:20 }
span.tracecontent table td.nopad { padding-right:5 }
</style>
</head>
<body>
<span class="tracecontent">
<table cellspacing="0" cellpadding="0" width="100%">
	<tr>
		<td><h1>Application Trace</h1></td>
	</tr><tr>
		<td><h2><h2><p></td>
	</tr><tr>
		<td>[ <a href="Trace.axd?clear=1" class="link">clear current trace</a> ]</td>
	</tr><tr>
		<td>Physical Directory:C:\inetpub\wwwroot\</td>
	</tr>
</table><table cellspacing="0" cellpadding="0" width="100%">
	<tr>
		<th class="alt" align="left" colspan="5"><h3><b>Requests to this Application</b></h3></th><th class="alt" align="right">Remaining: 49</th>
	</tr><tr class="subhead" align="left">
		<th>No.</th><th>Time of Request</th><th>File</th><th>Status Code</th><th>Verb</th><th>&nbsp</th>
	</tr><tr class="alt">
		<td>1</td><td>5/31/2026 7:09:54 PM</td><td>uploads/</td><td>200</td><td>GET</td><td><a href="Trace.axd?id=0" class="link"><nobr>View Details</a></td>
	</tr>
</table><hr width=100% size=1 color=silver>

Microsoft .NET Framework Version:4.0.30319; ASP.NET Version:4.8.4330.0

</font>

</span>
</body>
</html>
```


<h3>Misconfiguration 6: TRACE Method Enabled</h3>

```bash
# curl -X TRACE http://10.67.155.50 -sv
*   Trying 10.67.155.50:80...
* TCP_NODELAY set
* Connected to 10.67.155.50 (10.67.155.50) port 80 (#0)
> TRACE / HTTP/1.1
> Host: 10.67.155.50
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 501 Not Implemented
< Content-Type: text/html
< Server: Microsoft-IIS/10.0
< X-Powered-By: ASP.NET
< Date: Sun, 31 May 2026 19:15:42 GMT
< Content-Length: 1508
< 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>501 - Header values specify a method that is not implemented.</title>
<style type="text/css">
<!--
body{margin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;}
fieldset{padding:0 15px 10px 15px;} 
h1{font-size:2.4em;margin:0;color:#FFF;}
h2{font-size:1.7em;margin:0;color:#CC0000;} 
h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;} 
#header{width:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;
background-color:#555555;}
#content{margin:0 0 0 2%;position:relative;}
.content-container{background:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;}
-->
</style>
</head>
<body>
<div id="header"><h1>Server Error</h1></div>
<div id="content">
 <div class="content-container"><fieldset>
  <h2>501 - Header values specify a method that is not implemented.</h2>
  <h3>The page you are looking for cannot be displayed because a header value in the request does not match certain configuration settings on the Web server. For example, a request header might specify a POST to a static file that cannot be posted to, or specify a Transfer-Encoding value that cannot make use of compression.</h3>
 </fieldset></div>
</div>
</body>
</html>
* Connection #0 to host 10.67.155.50 left intact


<h3>Misconfiguration 7: Application Pool Running as a Privileged Account</h3>

 curl "http://10.67.155.50/webdav/cmd.aspx?cmd=whoami"
<pre>iis apppool\defaultapppool
```

<p><em>Answer the questions below </em></p>

<p>6.1. Navigate to the <code>/uploads/</code> directory on the target. What sensitive file extension is visible in the directory listing? (Answer Format: include the dot, e.g., .bak)<br>
<code>.back</code></p>

<p>6.2. What ASP.NET diagnostic handler URL path should be disabled in production as it can expose session data, cookies, and request history?<br>
<code>.back</code></p>


<br>
<h2>Task 7 - Automation</h2>


<h3>NSE Scripts for IISM</h3>


<h3>Service Version Detection</h3>


<h3>Enumerating HTTP Methods</h3>


<h3>Detecting WebDAV</h3>


<h3>Identifying Authentication Requirements</h3>


<p><em>Answer the question below </em><p>

<p>7.1. What nmap NSE script enumerates allowed HTTP methods on a web server?<br>
<code>http-methods</code></p>



<br>
<h2>Task 8 - Conclusion</h2>
<p>You have worked through the IIS attack chain from initial reconnaissance to interactive shell access, and covered a survey of misconfigurations that appear across real-world engagements. The techniques here appear in public incident reports from major threat actor groups and in pentest findings across enterprise environments.</p>

<h3>Key Takeaways</h3>
<p>

- IIS fingerprinting establishes the version and feature surface before any active exploitation, because the version determines which CVEs apply and enabled features like WebDAV reveal direct attack paths.<br>
- The 8.3 tilde enumeration technique reveals hidden files and directories that wordlist brute-forcing misses, because the short-name format is predictable even when the full filename is not.<br>
- WebDAV shell upload requires three conditions to be met simultaneously: WebDAV enabled, write permission, and Script Execute permission on the same directory. The <code>PUT-MOVE</code> bypass works because handler mappings apply at request time, not at upload time.<br>
- ASPX web shells run under the Application Pool identity, which by default carries <code>SeImpersonatePrivilege</code>, making Potato-style privilege escalation the natural next step after shell acquisition.<br>
I- IS misconfigurations like directory listing, unauthenticated WebDAV, <code>web.config</code> exposure, and <code>trace.axd</code> being accessible each create exploitable conditions independently, without requiring any CVE.<br>

Stay tuned for more exciting rooms for mastering pentesting skills.<p>

<p><em>Answer the question below</em></p>

<p>8.1. I have successfully completed the room!<br>
<code>No answer needed</code></p>




<h2 align="center">Completed</h2>
<p align="center">                                                       <img width="1000px" src="https://github.com/user-attachments/assets/b75aafa6-43fc-40e0-a0b6-3f3f05c6259e"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/7ddd12e4-edea-4d73-a4f5-1a8e2f0a8e85"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/6c33e965-dab5-4fb4-a88d-bbfca8698916"></p>

<h2 align="center">My TryHackMe Journey &nbsp; · &nbsp; 2026, May</h2>
<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|31<br><br><br>      |109<br><br><br>       |Web Server Attacks - II<br><br> |Medium<br><br><br>|🔗<br><br><br>| 1,239<br><br><br>| 180,251<br><br><br>| 97<br><br><br>| 7ᵗʰ<br><br><br>| 28ᵗʰ<br><br><br>| 1ˢᵗ<br><br><br>| 2ⁿᵈ<br><br><br>|

</h6></div><br>

<p align="center">Capability Score &nbsp;&nbsp; <strong>109</strong> <br><img width="1000px" src="https://github.com/user-attachments/assets/07b28a36-aaff-4ef7-9e8b-ae0e9cc05a99"><br>
                  Stats                                              <br><img width="300px"  src="https://github.com/user-attachments/assets/2717476f-ab02-48de-bc13-1cd6f63b7c60"><br>
                  Global All Time &nbsp;&nbsp;  8ᵗʰ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/2469f884-58e0-4437-8c2e-b26a3ed83e0e"><br>
                  Global Monthly &nbsp;&nbsp;  28ᵗʰ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/2c8e2891-d29a-40d2-ad3f-6579cb353369"><br>
                  Brazil All Time &nbsp;&nbsp;  1ˢᵗ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/dbab8206-da3e-4b9c-b7ff-b88a629a7d1a"><br>
                  Brazil Monthly &nbsp;&nbsp;   2ⁿᵈ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/24f7bdfd-72eb-440f-ad88-5f9812859f98"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
