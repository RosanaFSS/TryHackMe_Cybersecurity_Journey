

<p><em>Answer the questions below</em></p>

<p>Which application endpoint was abused to execute commands on the server?<br>
<code>/api/albums/1/export</code></p>


```bash
ubuntu@tryhackme:~/Desktop/artifacts$ ls
disk.img  tools
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ file disk.img
disk.img: DOS/MBR boot sector, extended partition table (last)
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ /usr/sbin/sfdisk -l disk.img
Disk disk.img: 12 GiB, 12884901888 bytes, 25165824 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: E14D0243-D31D-4718-846E-D99094E48A2A

Device       Start      End  Sectors  Size Type
disk.img1  2099200 25165790 23066591   11G Linux filesystem
disk.img14    2048    10239     8192    4M BIOS boot
disk.img15   10240   227327   217088  106M EFI System
disk.img16  227328  2097152  1869825  913M Linux extended boot

Partition table entries are not in disk order.
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ sudo mkdir -p /mnt/forensic
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ sudo mount -o ro,loop,offset=$((2099200*512)) disk.img /mnt/forensic
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ ls -la /mnt/forensic
```

```bash
buntu@tryhackme:/mnt/forensic/var/log$ ls
README            auth.log               dist-upgrade  journal    nginx    unattended-upgrades
alternatives.log  btmp                   dmesg         kern.log   private  wtmp
apport.log        cloud-init-output.log  dpkg.log      landscape  syslog
apt               cloud-init.log         gunicorn      lastlog    sysstat
```


```bash
ubuntu@tryhackme:/mnt/forensic/var/log/nginx$ cat error.log
2026/10/19 05:28:29 [notice] 1831#1831: using inherited sockets from "5;6;"
```

```bash
ubuntu@tryhackme:/mnt/forensic/var/log/nginx$ grep POST gallery-access.log
10.0.2.2 - - [20/Oct/2026:05:36:37 +0000] "POST /login HTTP/1.1" 302 189 "-" "MeridianUploader/1.3"
10.0.2.2 - - [20/Oct/2026:05:36:37 +0000] "POST /api/photos HTTP/1.1" 201 29 "-" "MeridianUploader/1.3"
10.0.2.2 - - [20/Oct/2026:05:36:37 +0000] "POST /api/albums/1/export HTTP/1.1" 202 43 "-" "MeridianUploader/1.3"
10.0.2.2 - - [20/Oct/2026:05:36:41 +0000] "POST /login HTTP/1.1" 302 189 "-" "MeridianUploader/1.3"
10.0.2.2 - - [20/Oct/2026:05:36:41 +0000] "POST /api/photos HTTP/1.1" 201 29 "-" "MeridianUploader/1.3"
10.0.2.2 - - [20/Oct/2026:05:36:41 +0000] "POST /api/albums/1/export HTTP/1.1" 202 43 "-" "MeridianUploader/1.3"
10.0.2.2 - - [20/Oct/2026:05:36:50 +0000] "POST /api/photos HTTP/1.1" 201 29 "-" "MeridianUploader/1.3"
10.0.2.2 - - [20/Oct/2026:05:36:54 +0000] "POST /api/albums/1/export HTTP/1.1" 202 43 "-" "MeridianUploader/1.3"
```

<br>
<p>What was the full path of the executable responsible for encrypting the images?<br>
<code>/srv/gallery/.cache/.indexd</code></p>

```bash

```

<br>
<p>What is the SHA-256 hash of that executable?<br>
<code>REDACTED</code></p>


```bash
root@tryhackme:/mnt/forensic/srv/gallery/.cache# file .indexd
.indexd: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f8f0e4efdd56a53819f0b57035bf9483ef3cf96f, for GNU/Linux 3.2.0, stripped
```

```bash
root@tryhackme:/mnt/forensic/srv/gallery/.cache# sha256sum .indexd
```

<br>
<p>Which encryption algorithm and mode protected the images?<br>
<code>AES-256-GCM</code></p>

```bash
root@tryhackme:/mnt/forensic/srv/gallery/.cache# strings .indexd | grep -C 2 Encrypt
_ITM_deregisterTMCloneTable
_ITM_registerTMCloneTable
EVP_EncryptUpdate
EVP_CIPHER_CTX_ctrl
EVP_EncryptInit_ex
RAND_bytes
OPENSSL_cleanse
--
EVP_aes_256_gcm
EVP_CIPHER_CTX_free
EVP_EncryptFinal_ex
gethostname
clock_gettime
```

<br>
<p>What initial seed value was used to generate the encryption key?<br>
<code>AES-256-GCM</code></p>
