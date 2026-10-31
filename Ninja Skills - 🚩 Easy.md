<h2 align="left">Linux Fundamentals &nbsp; ·  &nbsp; File Search and Metadata Extraction</h2>
<p align="left">
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Lab-Ninja Skills-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Difficulty-Easy-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Category-Linux%20Fundamentals-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Solved-2024--Aug--19-darkgreen?style=flat-square" /> &nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=flat-square&logo=github&color=24292e" alt="Follow Rosana on GitHub" /></a> &nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p> 

<br>
<br>

<p>I used <code>find</code>, <code>-exec</code>, and error suppression technique <code>2>/dev/null</code> to look for<br>
  
- Permissions & Text Ownership (Executable Status & Group Name)<br>

```bash
$ find / -type f \( -name filename1 -o -name filename2 -o -name filename3 ... \) -exec ls -l {} \; 2>/dev/null
```

- Numeric Ownership (UID/GID / File owner ID)<br>

```bash
$ find / -type f \( -name filename1 -o -name filename2 -o -name filename3 ... \) -exec ls -ln {} \; 2>/dev/null
```

- IP address<br>

```bash
$ find / -type f \( -name filename1 -o -name filename2 -o -name filename3 ... \) -exec grep -lE "([0-9]{1,3}\.){3}[0-9]{1,3}" {} \; 2>/dev/null
```

- SHA1 hash<br>

```bash
$ find / -type f \( -name filename1 -o -name filename2 -o -name filename3 ... \) -exec sha1sum {} \; 2>/dev/null | grep type_the_hash
```

- Quantity of lines in each file</p>

```bash
$ find / -type f \( -name filename1 -o -name filename2 -o -name filename3 ... \) -exec wc -l {} \; 2>/dev/null
```



<br>
<br>
<p>Let's have some fun with Linux. Deploy the machine and get started.<br>

This machine may take up to 3 minutes to configure.<br>

(If you prefer to SSH into the machine, use the credentials new-user as the username and password) Answer the questions about the following files:<br>

8V2L<br>
bny0<br>
c4ZX<br>
D8B3<br>
FHl1<br>
oiMO<br>
PFbD<br>
rmfX<br>
SRSq<br>
uqyw<br>
v2Vb<br>
X1Uy<br>

The aim is to answer the questions as efficiently as possible.</p>

<p><em>Answer the questions below</em></p>

<p>Which of the above files are owned by the best-group group(enter the answer separated by spaces in alphabetical order)<br>
<code>D8B3 v2Vb</code></p>

<p>Which file is executable by everyone?<br>
<code>8V2L</code></p>

```bash
[new-user@... home]$ file v2Vb
v2Vb: ASCII text
[new-user@... home]$ pwd
/home
[new-user@... home]$
```

```bash
[new-user...]$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -l {} \; 2>/dev/null
-rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /mnt/D8B3
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /mnt/c4ZX
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/FHl1
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/log/uqyw
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/PFbD
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/oiMO
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /media/rmfX
-rwxrwxr-x 1 new-user new-user 13545 Oct 23  2019 /etc/8V2L
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /etc/ssh/SRSq
-rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /home/v2Vb
-rw-rw-r-- 1 newer-user new-user 13545 Oct 23  2019 /X1Uy
```

<img width="1263" height="262" alt="image" src="https://github.com/user-attachments/assets/e5fee44b-8be5-4bd6-81ad-d5df365e0c26" />

<br>
<br>
<p>Which of these files contain an IP address?<br>
<code>oiMO</code></p>

```bash
[new-user@...]$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec grep -lE "([0-9]{1,3}\.){3}[0-9]{1,3}" {} \; 2>/dev/null
/opt/oiMO
```

<img width="920" height="110" alt="image" src="https://github.com/user-attachments/assets/b79302a3-b886-478d-af3a-a75cdb0a2259" />

<br>
<br>
<p>Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94<br>
<code>c4ZX</code></p>

```bash
[new-user@...]$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec sha1sum {} \; 2>/dev/null | grep 9d54da7584015647ba052173b84d45e8007eba94
9d54da7584015647ba052173b84d45e8007eba94  /mnt/c4ZX
```

<img width="922" height="110" alt="image" src="https://github.com/user-attachments/assets/3697e070-9585-467d-9a79-e103434515bf" />

<br>
<br>
<p>Which file contains 230 lines?<br>
<code>bny0</code></p>

```bash
[new-user@...]$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec wc -l {} \; 2>/dev/null
209 /mnt/D8B3
209 /mnt/c4ZX
209 /var/FHl1
209 /var/log/uqyw
209 /opt/PFbD
209 /opt/oiMO
209 /media/rmfX
209 /etc/8V2L
209 /etc/ssh/SRSq
209 /home/v2Vb
209 /X1Uy
```

<img width="949" height="278" alt="image" src="https://github.com/user-attachments/assets/191d65b4-3fbb-4285-ab9b-23fd124c7413" />

<br>
<br>
<p>Which file's owner has an ID of 502?<br>
<code>X1Uy</code></p>

```bash
[new-user@...]$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -ln {} \; 2>/dev/null
-rw-rw-r-- 1 501 502 13545 Oct 23  2019 /mnt/D8B3
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /mnt/c4ZX
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /var/FHl1
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /var/log/uqyw
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /opt/PFbD
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /opt/oiMO
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /media/rmfX
-rwxrwxr-x 1 501 501 13545 Oct 23  2019 /etc/8V2L
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /etc/ssh/SRSq
-rw-rw-r-- 1 501 502 13545 Oct 23  2019 /home/v2Vb
-rw-rw-r-- 1 502 501 13545 Oct 23  2019 /X1Uy
```


<img width="956" height="279" alt="image" src="https://github.com/user-attachments/assets/66121f29-ae0a-4dfe-9bd5-dcec4f35c7e8" />

<br>
<br>
<br>

<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/03ea4c76-3437-4979-a777-29aeb9341fe8"><br><br>
<img width="900px" src="https://github.com/user-attachments/assets/03f3f8d6-6d61-4a17-a9ab-b5a01300d00f"></p>
