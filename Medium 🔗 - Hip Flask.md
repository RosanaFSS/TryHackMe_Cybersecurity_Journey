
```bash
:~# git clone https://github.com/laramies/theHarvester.git
```

```bash
uv sync
```

```bash
:~/theHarvester# uv run theHarvester
Created default proxies.yaml at /root/.theHarvester/proxies.yaml
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.10.0                                             *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*                                                                 *
*******************************************************************
usage: theHarvester [-h] -d DOMAIN [-l LIMIT] [-S START] [-p] [-s] [--screenshot SCREENSHOT] [-e DNS_SERVER] [-t]
                    [-r [DNS_RESOLVE]] [-n] [-c] [-f FILENAME] [-w WORDLIST] [-a] [-q] [-b SOURCE]
theHarvester: error: the following arguments are required: -d/--domain
```


```bash
:~/theHarvester# nmap 10.80.142.143
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:22 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for 10.80.142.143
Host is up (0.00046s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
53/tcp  open  domain
80/tcp  open  http
443/tcp open  https

Nmap done: 1 IP address (1 host up) scanned in 0.35 seconds
```

```bash
:~/theHarvester# nmap -vv 10.80.142.143 -oN Initial-SYN-Scan
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:22 GMT
Initiating Ping Scan at 18:22
Scanning 10.80.142.143 [4 ports]
Completed Ping Scan at 18:22, 0.03s elapsed (1 total hosts)
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Initiating SYN Stealth Scan at 18:22
Scanning 10.80.142.143 [1000 ports]
Discovered open port 443/tcp on 10.80.142.143
Discovered open port 80/tcp on 10.80.142.143
Discovered open port 53/tcp on 10.80.142.143
Discovered open port 22/tcp on 10.80.142.143
Completed SYN Stealth Scan at 18:22, 0.07s elapsed (1000 total ports)
Nmap scan report for 10.80.142.143
Host is up, received syn-ack ttl 64 (0.00064s latency).
Scanned at 2026-02-08 18:22:59 GMT for 0s
Not shown: 996 closed ports
Reason: 996 resets
PORT    STATE SERVICE REASON
22/tcp  open  ssh     syn-ack ttl 64
53/tcp  open  domain  syn-ack ttl 64
80/tcp  open  http    syn-ack ttl 64
443/tcp open  https   syn-ack ttl 64

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.24 seconds
           Raw packets sent: 1004 (44.152KB) | Rcvd: 1001 (40.060KB)
```
           


```bash
:~/theHarvester# nmap -p 22,53,80,443 -sV -Pn -vv 10.80.142.143 -oN service-scan
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:23 GMT
NSE: Loaded 45 scripts for scanning.
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Initiating SYN Stealth Scan at 18:23
Scanning 10.80.142.143 [4 ports]
Discovered open port 443/tcp on 10.80.142.143
Discovered open port 53/tcp on 10.80.142.143
Discovered open port 22/tcp on 10.80.142.143
Discovered open port 80/tcp on 10.80.142.143
Completed SYN Stealth Scan at 18:23, 0.03s elapsed (4 total ports)
Initiating Service scan at 18:23
Scanning 4 services on 10.80.142.143
Completed Service scan at 18:23, 16.01s elapsed (4 services on 1 host)
NSE: Script scanning 10.80.142.143.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:23
Completed NSE at 18:23, 0.07s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:23
Completed NSE at 18:23, 0.01s elapsed
Nmap scan report for 10.80.142.143
Host is up, received user-set (0.00039s latency).
Scanned at 2026-02-08 18:23:21 GMT for 16s

PORT    STATE SERVICE  REASON         VERSION
22/tcp  open  ssh      syn-ack ttl 64 OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
53/tcp  open  domain   syn-ack ttl 64 (unknown banner: Now why would you need this..?)
80/tcp  open  http     syn-ack ttl 64 nginx 1.18.0 (Ubuntu)
443/tcp open  ssl/http syn-ack ttl 64 nginx 1.18.0 (Ubuntu)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-TCP:V=7.80%I=7%D=2/8%Time=6988D4A4%P=x86_64-pc-linux-gnu%r(DNSVe
SF:rsionBindReqTCP,4B,"\0I\0\x06\x85\0\0\x01\0\x01\0\0\0\0\x07version\x04b
SF:ind\0\0\x10\0\x03\xc0\x0c\0\x10\0\x03\0\0\0\0\0\x1f\x1eNow\x20why\x20wo
SF:uld\x20you\x20need\x20this\.\.\?");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.58 seconds
           Raw packets sent: 4 (176B) | Rcvd: 4 (176B)

```


```bash
:~/theHarvester# nmap -sU --top-ports 50 -Pn -vv --open  10.80.142.143 -oN udp-top-ports
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:24 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Initiating UDP Scan at 18:24
Scanning 10.80.142.143 [50 ports]
Increasing send delay for 10.80.142.143 from 0 to 50 due to max_successful_tryno increase to 4
Increasing send delay for 10.80.142.143 from 50 to 100 due to max_successful_tryno increase to 5
Increasing send delay for 10.80.142.143 from 100 to 200 due to max_successful_tryno increase to 6
Increasing send delay for 10.80.142.143 from 200 to 400 due to max_successful_tryno increase to 7
Increasing send delay for 10.80.142.143 from 400 to 800 due to max_successful_tryno increase to 8
Discovered open port 53/udp on 10.80.142.143
Completed UDP Scan at 18:25, 53.91s elapsed (50 total ports)
Nmap scan report for 10.80.142.143
Host is up, received user-set (0.00087s latency).
Scanned at 2026-02-08 18:24:22 GMT for 54s
Not shown: 46 closed ports
Reason: 46 port-unreaches
PORT     STATE         SERVICE  REASON
53/udp   open          domain   udp-response ttl 64
68/udp   open|filtered dhcpc    no-response
631/udp  open|filtered ipp      no-response
5353/udp open|filtered zeroconf no-response

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 54.03 seconds
           Raw packets sent: 162 (6.039KB) | Rcvd: 49 (3.297KB)

```

<img width="951" height="131" alt="image" src="https://github.com/user-attachments/assets/08ad5a93-89d9-4597-9c59-8e88cac8989e" />



```bash
:~/theHarvester# dig axfr hipflasks.thm @10.80.142.143

; <<>> DiG 9.18.28-0ubuntu0.20.04.1-Ubuntu <<>> axfr hipflasks.thm @10.80.142.143
;; global options: +cmd
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400
hipflasks.thm.		86400	IN	NS	ns1.hipflasks.thm.
hipflasks.thm.		86400	IN	NS	localhost.
hipper.hipflasks.thm.	86400	IN	A	10.80.142.143
www.hipper.hipflasks.thm. 86400	IN	A	10.80.142.143
ns1.hipflasks.thm.	86400	IN	A	10.80.142.143
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400
;; Query time: 0 msec
;; SERVER: 10.80.142.143#53(10.80.142.143) (TCP)
;; WHEN: Sun Feb 08 18:36:53 GMT 2026
;; XFR size: 7 records (messages 1, bytes 242)
```



```bash
:~/theHarvester# host -t axfr hipflasks.thm 10.80.142.143
Trying "hipflasks.thm"
Using domain server:
Name: 10.80.142.143
Address: 10.80.142.143#53
Aliases: 

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49499
;; flags: qr aa ra; QUERY: 1, ANSWER: 7, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hipflasks.thm.			IN	AXFR

;; ANSWER SECTION:
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400
hipflasks.thm.		86400	IN	NS	ns1.hipflasks.thm.
hipflasks.thm.		86400	IN	NS	localhost.
hipper.hipflasks.thm.	86400	IN	A	10.80.142.143
www.hipper.hipflasks.thm. 86400	IN	A	10.80.142.143
ns1.hipflasks.thm.	86400	IN	A	10.80.142.143
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400

Received 203 bytes from 10.80.142.143#53 in 0 ms
```


```bash
hipper
```



<img width="958" height="768" alt="image" src="https://github.com/user-attachments/assets/532242af-19fd-4cdc-b93b-12e10516bd85" />

<img width="1101" height="803" alt="image" src="https://github.com/user-attachments/assets/b2ec99cd-3284-4398-8bff-555e137463b2" />


<img width="1075" height="256" alt="image" src="https://github.com/user-attachments/assets/1b7b8af2-e51d-4377-8402-173b841daf21" />

<img width="1095" height="698" alt="image" src="https://github.com/user-attachments/assets/130abbe6-259d-441a-a659-799f132dce8a" />


```bash
:~/theHarvester# nikto -h https://hipper.hipflasks.thm -ssl
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.80.142.143
+ Target Hostname:    hipper.hipflasks.thm
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject: /C=GB/ST=Argyll and Bute/L=Oban/O=Hip Flasks Inc/CN=hipflasks.thm/emailAddress=webmaster@hipflasks.thm
                   Ciphers: TLS_AES_256_GCM_SHA384
                   Issuer:  /C=GB/ST=Argyll and Bute/L=Oban/O=Hip Flasks Inc/CN=hipflasks.thm/emailAddress=webmaster@hipflasks.thm
+ Start Time:         2026-02-08 18:46:33 (GMT0)
---------------------------------------------------------------------------
+ Server: waitress
+ Cookie session created without the secure flag
+ Cookie session created without the httponly flag
+ Uncommon header 'x-frame-options' found, with contents: SAMEORIGIN
+ Uncommon header 'x-content-type-options' found, with contents: nosniff
+ Uncommon header 'front-end-https' found, with contents: on
+ Uncommon header 'strict-transport-security' found, with contents: max-age=31536000; includeSubDomains
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server banner has changed from 'waitress' to 'nginx/1.18.0 (Ubuntu)' which may suggest a WAF, load balancer or proxy is in place
+ Hostname 'hipper.hipflasks.thm' does not match certificate's CN 'hipflasks.thm/emailAddress=webmaster@hipflasks.thm'
+ Allowed HTTP Methods: GET, OPTIONS, HEAD 
...
```


```bash
:~# curl https://hipper.hipflasks.thm/main.py -k
#!/usr/bin/python3
from flask import Flask, redirect, render_template, request, session
from datetime import datetime
from waitress import serve
from modules import abp
from libs.db import AuthConn, StatsConn

app = Flask(__name__)
app.template_folder="views"
app.config["SECRET_KEY"] = "1a98164eacf96276995566d0c4a4a413"


@app.before_request
def befReq():
	conn = StatsConn()
	if not session.get("visited"):
		conn.addView("uniqueViews")
		session["visited"] = "True"
	conn.addView("totalViews")


@app.route("/")
def home():
	return render_template("index.html", year=datetime.now().date().strftime("%Y")), 200

app.register_blueprint(abp, url_prefix="/admin")


@app.errorhandler(403)
def error403(e):
	return "You are not authorised to access this", 403


#Confirm that there is an admin account in place
AuthConn()

serve(app, host="127.0.0.1", port=8000)
```



```bash
:~# cat __init__.py
from modules.admin import abp
```

```bash
:~# curl https://hipper.hipflasks.thm/modules/admin.py -ks | head
#!/usr/bin/python3
from flask import Blueprint, render_template_string, request, redirect, session, abort, url_for, flash, get_flashed_messages
from libs.auth import authCheck, checkAuth
from libs.db import AuthConn, StatsConn

abp = Blueprint("abp", __name__)

@abp.route("/")
@authCheck
def manageHome():
```

```bash
:~# curl -k https://hipper.hipflasks.thm/libs/auth.py
from flask import session, redirect, url_for, flash
from functools import wraps

checkAuth = lambda: session.get("auth") == "True"

def authCheck(func):
    @wraps(func)
    def innerCheck(*args, **kwargs):
        if checkAuth():
            return func(*args, **kwargs)
        else:
            flash("Please login before accessing the admin area")
            return redirect(url_for("abp.loginRoute")), 301
    return innerCheck



:~# curl -k https://hipper.hipflasks.thm/libs/db/__init__.py
from libs.db.base import Conn
from libs.db.auth import AuthConn
from libs.db.stats import StatsConn
```





```bash
:~/lesson# curl -k https://hipper.hipflasks.thm/data/users.db -o users.db
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12288  100 12288    0     0   307k      0 --:--:-- --:--:-- --:--:--  315k
```

```bash
:~/lesson# ls -lah
total 20K
drwxr-xr-x  2 root root 4.0K Feb  8 19:13 .
drwxr-xr-x 53 root root 4.0K Feb  8 19:13 ..
-rw-r--r--  1 root root  12K Feb  8 19:13 users.db
```


```bash
:~/lesson# curl -k https://hipper.hipflasks.thm/data/stats.db -o stats.db
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12288  100 12288    0     0   631k      0 --:--:-- --:--:-- --:--:--  631k
```


```bash
:~/lesson# ls -lah
total 32K
drwxr-xr-x  2 root root 4.0K Feb  8 19:14 .
drwxr-xr-x 53 root root 4.0K Feb  8 19:13 ..
-rw-r--r--  1 root root  12K Feb  8 19:14 stats.db
-rw-r--r--  1 root root  12K Feb  8 19:13 users.db
```

```bash
:~/lesson# ls -lah
total 52K
drwxr-xr-x  2 root root 4.0K Feb  8 19:18 .
drwxr-xr-x 53 root root 4.0K Feb  8 19:13 ..
-rw-r--r--  1 root root 4.8K Feb  8 19:17 admin.py
-rw-r--r--  1 root root  435 Feb  8 19:18 auth.py
-rw-r--r--  1 root root  100 Feb  8 19:16 __init__.py
-rw-r--r--  1 root root  862 Feb  8 19:18 main.py
-rw-r--r--  1 root root  12K Feb  8 19:14 stats.db
-rw-r--r--  1 root root  12K Feb  8 19:13 users.db

```


```bash
:~/lesson# python3 -m venv poc-venv
```


```bash
:~/lesson# source poc-venv/bin/activate
(poc-venv) r...:~/lesson# 
```


```bash
(poc-venv) r...:~/lesson# pip3 install flask requests waitress
```


```bash

```



```bash

```


```bash

```



```bash

```


```bash

```



```bash

```


```bash

```



