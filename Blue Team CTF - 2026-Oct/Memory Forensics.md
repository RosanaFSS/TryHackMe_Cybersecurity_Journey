<h1 align="left">CTF Blue Team &nbsp; ·  &nbsp; Memory Forensics</h1>

<p align="left">
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Difficulty-Medium-24292e?style=flat-square" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Completed-2026%2C%20Oct%2029-24292e?style=flat-square" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=flat-square&logo=github&color=24292e" alt="Follow Rosana on GitHub" /></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p> 


<br>
<p><em>Answer the questions below</em></p>
<p>Which executable contains the suspicious payload?<br>
<code>ReviewClient.exe</code></p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ ls
memory.mem  symbols  tools
```

<p>
  
- Is64Bit	<code>True</code></p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol -s ~/Desktop/artifacts/symbols -f memory.mem windows.info
Volatility 3 Framework 2.28.2
Progress:  100.00		PDB scanning finished                        
Variable	Value

Kernel Base	0xf8061f000000
DTB	0x1aa000
Symbols	file:///home/ubuntu/Desktop/artifacts/symbols/windows/ntkrnlmp.pdb/68A17FAF3012B7846079AEECDBE0A583-1.json.xz
Is64Bit	True
IsPAE	False
layer_name	0 WindowsIntel32e
memory_layer	1 Elf64Layer
base_layer	2 FileLayer
KdVersionBlock	0xf8061fc0f398
Major/Minor	15.19041
MachineType	34404
KeNumberProcessors	2
SystemTime	2026-10-05 03:54:42+00:00
NtSystemRoot	C:\Windows
NtProductType	NtProductWinNt
NtMajorVersion	10
NtMinorVersion	0
PE MajorOperatingSystemVersion	10
PE MinorOperatingSystemVersion	0
PE Machine	34404
PE TimeDateStamp	Wed Jun 28 04:14:26 1995
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ v windows.pslist  > ~/Desktop/artifacts/pslist.txt
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ v windows.pstree  > ~/Desktop/artifacts/pstree.txt
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ v windows.cmdline  > ~/Desktop/artifacts/pcmdline.txt
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ v windows.malfind  > ~/Desktop/artifacts/malfind.txt
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ grep -oP '\w+\.exe' pstree.txt | sort | uniq -c | sort -nr
    244 svchost.exe
     30 RuntimeBroker.exe
     27 backgroundTaskHost.exe
...
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ grep -oP '\w+\.exe' pstree.txt | sort | uniq -c | sort -n
      2 SppExtComObj.exehttps://study.learning.wiley.com/products/0035fefc-9796-49d5-8647-025a81694983/units/40d4cdc7-a3da-4bfd-87df-947d8c67ec5c?tab=assignments
      2 WWAHost.exe
      2 WmiPrvSE.exe
      2 explorer.exe
      2 userinit.exe
      2 wmiprvse.exe
      2 wwahost.exe
      3 ApplicationFrameHost.exe
      3 LocalBridge.exe
      3 MicrosoftEdgeUpdate.exe
      3 ReviewClient.exe
      3 SearchFilterHost.exe
```

<p>

- 6260 6164 ReviewClient.e <code>0xbd8fdbebd080</code> .... "C:\Users\s.reyes\Downloads\...\<code>ReviewClient.exe</code>"<br>
0x8e0fff
- 6280 6164 notepad.exe</p>

<p><em>pstree.txt</em></p>

```bash
PID	  PPID	ImageFileName	  Offset(V)	      hreads	Handles	SessionId	Wow64	CreateTime	ExitTime	Audit	Cmd	Path
6260	6164	ReviewClient.e	0xbd8fdbebd080	4	-	1	True	2026-10-05 03:54:18.000000 UTC	N/A	\Device\HarddiskVolume1\Users\s.reyes\Downloads\DocumentReview\ReviewClient.exe	"C:\Users\s.reyes\Downloads\DocumentReview\ReviewClient.exe" 	C:\Users\s.reyes\Downloads\DocumentReview\ReviewClient.exe
6280	6164	notepad.exe	    0xbd8fdc55e0c0	6	-	1	False	2026-10-05 03:54:18.000000 UTC	N/A	\Device\HarddiskVolume1\Windows\System32\notepad.exe	"C:\Windows\system32\notepad.exe" 	C:\Windows\system32\notepad.exe
```

<br>
<p>What is the starting virtual address of its private executable memory region?<br>
<code>0x8e0000</code></p>

<p><em>malfind.txt</em></p>

<p>

- 0x8e0009:	push	0x63<br>
- 0x8e000b:	push	0x6578<br>
- 0x8e000f:	push	0x456e6957<br>
- 0x8e0014:	mov	dword ptr [ebp - 4], esp<br>
- 0x8e0017:	mov	ebx, dword ptr fs:[esi + 0x30]</p>

```bash
...
260	ReviewClient.e	0x8e0000	0x8e0fff	VadS	PAGE_EXECUTE_READWRITE	1	1	Disabled	Function prologue
55 89 e5 83 ec 18 31 f6 56 6a 63 66 68 78 65 68 U.....1.Vjcfhxeh
57 69 6e 45 89 65 fc 64 8b 5e 30 8b 5b 0c 8b 5b WinE.e.d.^0.[..[
14 8b 1b 8b 1b 8b 5b 10 89 5d f8 8b 43 3c 01 d8 ......[..]..C<..
8b 40 78 01 d8 8b 48 24 01 d9 89 4d f4 31 c9 41 .@x...H$...M.1.A	
0x8e0000:	push	ebp
0x8e0001:	mov	ebp, esp
0x8e0003:	sub	esp, 0x18
0x8e0006:	xor	esi, esi
0x8e0008:	push	esi
0x8e0009:	push	0x63
0x8e000b:	push	0x6578
0x8e000f:	push	0x456e6957
0x8e0014:	mov	dword ptr [ebp - 4], esp
0x8e0017:	mov	ebx, dword ptr fs:[esi + 0x30]
0x8e001b:	mov	ebx, dword ptr [ebx + 0xc]
0x8e001e:	mov	ebx, dword ptr [ebx + 0x14]
0x8e0021:	mov	ebx, dword ptr [ebx]
0x8e0023:	mov	ebx, dword ptr [ebx]
0x8e0025:	mov	ebx, dword ptr [ebx + 0x10]
0x8e0028:	mov	dword ptr [ebp - 8], ebx
0x8e002b:	mov	eax, dword ptr [ebx + 0x3c]
0x8e002e:	add	eax, ebx
0x8e0030:	mov	eax, dword ptr [eax + 0x78]
0x8e0033:	add	eax, ebx
0x8e0035:	mov	ecx, dword ptr [eax + 0x24]
0x8e0038:	add	ecx, ebx
0x8e003a:	mov	dword ptr [ebp - 0xc], ecx
0x8e003d:	xor	ecx, ecx
0x8e003f:	inc	ecx
...
```

<img width="1342" height="249" alt="image" src="https://github.com/user-attachments/assets/24d8f071-a80e-4057-ae71-ebf67cebb1cb" />

<br>
<br>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol -f memory.mem windows.vadinfo --pid 6260 --dump
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ v windows.vadinfo --pid 6260 | grep -i -B2 -A8 '0x8e0000'
6260ressReviewClient.e	0xffffbd8fdc3934a0ng fin0x8d0000        0x8d0fff        VadS	PAGE_READWRITE	1	1	0xffffbd8fdc32b480	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc393680	0x7d0000	0x8cffff	VadS	PAGE_READWRITE	63	1	0xffffbd8fdc3934a0	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc394440	0x8e0000	0x8e0fff	VadS	PAGE_EXECUTE_READWRITE	1	10xffffbd8fdc3934a0	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc393b30	0x940000	0xa3ffff	VadS	PAGE_READWRITE	3	1	0xffffbd8fdc393630	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc394170	0x910000	0x910fff	VadS	PAGE_READWRITE	1	1	0xffffbd8fdc393b30	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc32c880	0x900000	0x903fff	Vad 	PAGE_READONLY	0	0	0xffffbd8fdc394170	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc32a440	0x920000	0x938fff	Vad 	PAGE_EXECUTE_WRITECOPY	4	00xffffbd8fdc394170	\Users\s.reyes\Downloads\DocumentReview\ReviewClient.exe	Disabled
6260	ReviewClient.e	0xffffbd8fdc32c600	0xa40000	0xc3ffff	Vad 	PAGE_READONLY	0	0	0xffffbd8fdc393b30	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc393f90	0x26e0000	0x275ffff	VadS	PAGE_READWRITE	1	1	0xffffbd8fdc32c420	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc3942b0	0x2460000	0x2467fff	VadS	PAGE_READWRITE	1	1	0xffffbd8fdc393f90	N/A	Disabled
6260	ReviewClient.e	0xffffbd8fdc3941c0	0x2320000	0x235ffff	VadS	PAGE_READWRITE	11	1	0xffffbd8fdc3942b0	N/A	Disabled
```

<br>
<p>Which file associated with the process also contains the same payload?<br>
<code>review-cover.png</code></p>

<p>

- review-cache.dat <code>0xbd8fdbcb3c60</code><br>
- review-cover.png</p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ v windows.handles --pid 6260 | grep -i file
6260ressReviewClient.e	0xbd8fdbca2640an0x40 finFile	0x100020	\Device\HarddiskVolume1\Windows
6260	ReviewClient.e	0xbd8fdbcb0bf0	0x84	File	0x100020	\Device\HarddiskVolume1\Users\s.reyes\Downloads\DocumentReview
6260	ReviewClient.e	0x9389f8b1b5e0	0xcc	Key	0x9	MACHINE\SOFTWARE\MICROSOFT\WINDOWS NT\CURRENTVERSION\IMAGE FILE EXECUTION OPTIONS
6260	ReviewClient.e	0xbd8fdbcb3c60	0x108	File	0x120089	\Device\HarddiskVolume1\Users\s.reyes\Downloads\DocumentReview\review-cache.dat
6260	ReviewClient.e	0xbd8fdbcb5a10	0x10c	File	0x120089	\Device\HarddiskVolume1\Users\s.reyes\Downloads\DocumentReview\review-cover.png
6260	ReviewClient.e	0xbd8fdbcb7180	0x1a0	File	0x100001	\Device\HarddiskVolume1\Windows\SysWOW64\en-US\user32.dll.mui
6260	ReviewClient.e	0xbd8fdbcb77c0	0x1b8	File	0x100001	\Device\CNG
6260	ReviewClient.e	0xbd8fdbcbb190	0x254	File	0x120089	\Device\HarddiskVolume1\Windows\Fonts\StaticCache.dat
```

<br>
<p>Which MITRE ATT&CK sub-technique best describes how the payload is stored in the recovered PNG file?<br>
<code>T1027.009</code></p>

<img width="1337" height="453" alt="image" src="https://github.com/user-attachments/assets/32f6885d-e5d9-4218-98b1-d2de8dc56c03" />

<br>
<br>
<p>Which Windows API does the payload call to launch its next stage?<br>
<code>kernel32.WinExec</code></p>

<img width="1025" height="416" alt="image" src="https://github.com/user-attachments/assets/83f527df-d00c-4b41-95e5-ed2db54808a0" />

<br>
<br>
<p>What encryption key does the decoded stage use to decrypt the document cache? Hint: Submit the key as 64 hexadecimal characters, without spaces or a 0x prefix.<br>
<code>REDACTED</code></p>


```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol -f memory.mem windows.malfind --pid 6260 --dump
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ ls
... pid.6260.vad.0x8e0000-0x8e0fff.dmp 
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ speakeasy -t pid.6260.vad.0x8e0000-0x8e0fff.dmp -a x86 -r
/home/ubuntu/Desktop/artifacts/tools/venv/lib/python3.12/site-packages/unicorn/unicorn.py:6: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
* exec: shellcode
0x153d: 'kernel32.WinExec("powershell.exe -NoProfile -EncodedCommand JABREDACTEDoAaQBwACcALAAkAGQAKQA=", 0x5)' -> 0x20
* Finished emulating
```

<img width="1360" height="321" alt="image" src="https://github.com/user-attachments/assets/8a0a0119-3aae-4656-b451-6484bd726110" />



<br>

<img width="1326" height="452" alt="image" src="https://github.com/user-attachments/assets/0f28e1d2-d9fb-4190-b2a7-9cd7f4cd6dee" />



<br>
<br>
<p>What is the flag?<br>
<code>REDACTED</code></p>


```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol -f memory.mem windows.filescan | grep "review-cache.dat"
Progress:  100.00		PDB scanning finished                        

0xbd8fdbca6650	\Users\s.reyes\Downloads\DocumentReview\review-cache.dat
0xbd8fdbcb3c60	\Users\s.reyes\Downloads\DocumentReview\review-cache.dat
0xbd8fdbe27d00	\LabTransfer\review-cache.dat
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ vol -f memory.mem windows.dumpfiles --virtaddr 0xbd8fdbca6650
Volatility 3 Framework 2.28.2
Progress:  100.00		PDB scanning finished                        
Cache	FileObject	FileName	Result

DataSectionObject	0xbd8fdbca6650	review-cache.dat	file.0xbd8fdbca6650.0xbd8fdc40ce10.DataSectionObject.review-cache.dat.dat
SharedCacheMap	0xbd8fdbca6650	review-cache.dat	file.0xbd8fdbca6650.0xbd8fdc2f6d40.SharedCacheMap.review-cache.dat.vacb
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ mv file.0xbd8fdbca6650.0xbd8fdc40ce10.DataSectionObject.review-cache.dat.dat review-cache.dat
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ xxd -p -l 16 review-cache.dat | tr -d '\n' > iv.txt
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ cat iv.txt
REDACTED
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ dd if=review-cache.dat of=ciphertext.bin bs=16 skip=1
```


```bash
ubuntu@tryhackme:~/Desktop/artifacts$ openssl enc -d -aes-256-cbc -in ciphertext.bin -out review-cache.zip -K REDACTED -iv REDACTED
```

<img width="560" height="134" alt="image" src="https://github.com/user-attachments/assets/e6ad218c-ac2c-49ad-b8cb-18941fb49c91" />
