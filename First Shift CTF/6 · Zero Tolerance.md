<h1 align="center"><a href="https://tryhackme.com/room/first-shift-ctf">First Shift CTF</a> &nbsp;&nbsp; · &nbsp;&nbsp; Zero Trust</h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20JAN%2026-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<h2>Zero Trust</h2>
<p>It was supposed to be a regular morning at ProbablyFine Ltd. L2 had just returned from paternity leave. L3 was hosting a live webinar on "Proactive Threat Hunting." The morning standup was the usual mix of coffee, ticket updates, and small talk about last night's football match. Then the Slack notification came through from Sales:<br>

"<strong>NEW CLIENT ONBOARDED - VaultSecure Banking - Tier 1 Priority - Live monitoring starts NOW</strong>"

VaultSecure Banking wasn't just any client. They're a regional bank with two million customers. They had just fired their previous MSSP after a compliance audit revealed endpoints that had gone unmonitored for six months. The contract ProbablyFine signed was massive, enough to fund the company for the next two years. However, there’s a catch: a 90-day probation period with a "zero tolerance" clause - miss one critical alert, and the contract is terminated.</p>


<h2>The Alert</h2>
<p>You were barely skimming the onboarding docs before the SIEM lights up with a critical alert:<br>

"<strong>CRITICAL: Suspicious Persistence Mechanism Detected - VaultSecure Banking</strong>"<br>

You just stare at it for a second. It's been less than 4 hours since monitoring went live, and you're already staring at a critical alert. Your L2 is in back-to-back meetings with the new client. Your L3 is live on a webinar with 500 attendees. The company's future literally depends on how you handle this. For now, it's just you and this alert. It's time to show VaultSecure Banking why they chose ProbablyFine!</p>

<h2>Machine Access</h2>
<p>Start the lab by clicking the Start Machine button below. You will then have access to the Splunk Web Interface. Please wait 4-5 minutes for the Splunk instance to launch. To access Splunk, please follow this link:<br>

- <a href="https://lab_web_url.p.thmlabs.com/en-US/app/search/search?q=search%20index%3D*&display.page.search.mode=smart&dispatch.sample_ratio=1&workload_pool=&earliest=0&latest="> Splunk Web Interface</a><br>

You may also need downloadable artifacts from the compromised VM:<br>

- Google Drive <a href="https://drive.google.com/file/d/1YLn1Os_kfeeZadjG4cevcJBXheV06XCt/view?usp=sharing"> Link</a></p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the questions below</em></p>

<br>
<p>6.1. <em>What is the hostname where the Initial Access occurred?</em><br>
<code>JP-BROWN-WS</code></p>

```splunk
index=*
|  stats count by host
```

<img width="1333" height="418" alt="image" src="https://github.com/user-attachments/assets/5d608bda-2014-4566-b39e-6ecc8150cb69" />

<br>
<br>
<br>
<p>6.2. <em>What MITRE ATT&CK sub-technique ID describes the initial code execution method on the beachhead?</em><br>
<code>T1204.002</code></p>

<img width="1334" height="451" alt="image" src="https://github.com/user-attachments/assets/24fce10c-ac6f-4b26-aff0-03b195e4fc18" />

<br>

<img width="1348" height="375" alt="image" src="https://github.com/user-attachments/assets/19dafc31-ef74-4f6d-a078-e21b23d4ed7f" />


<br>
<br>
<br>
<p>6.3. <em>What is the full path of the malicious file that led to Initial Access?</em><br>
<code>C:\Users\jp.brown\Downloads\TravisClart_Resume.pdf.lnk</code></p>


<br>
<p>6.4. What is the full path to the LOLBin abused by the attacker for Initial Access?</em><br>
<code>C:\Windows\System32\mshta.exe</code></p>

<br>
<p>6.5. What is the full path to the LOLBin abused by the attacker for Initial Access?</em><br>
<code>10.10.14.174</code></p>

```splunk
index=* ComputerName="JP-BROWN-WS" EventCode=1  Image="*mshta*"
|  table _time, Image, CommandLine, ProcessId
|  sort by +_time
```

<img width="1333" height="398" alt="image" src="https://github.com/user-attachments/assets/903780b4-83a0-42e6-9ae6-550a8feb4423" />

<br>
<br>
<br>
<p>6.6. What is the full path of the process responsible for the C2 beaconing?</em><br>
<code>C:\Windows\Temp\RuntimeBroker.exe</code></p>

```splunk
index=* ComputerName="JP-BROWN-WS" EventCode=1  10.10.14.174
|  table _time, ProcessId, CommandLine, ParentProcessId, ParentCommandLine
|  sort by +_time
```

<img width="1340" height="510" alt="image" src="https://github.com/user-attachments/assets/08397258-581a-472f-add1-1c59eaa192fc" />

<br>
<br>
<br>
<p>6.7. What is the full registry path that the threat actor modified for persistence on the beachhead host?</em><br>
<code>HKCU\Software\Microsoft\Windows\CurrentVersion\Run\SystemMonitor</code></p>

```splunk
index=* ComputerName="JP-BROWN-WS" EventCode=1  10.10.14.174
|  table _time, ProcessId, CommandLine, ParentProcessId, ParentCommandLine
|  sort by +_time
```

<img width="1340" height="510" alt="image" src="https://github.com/user-attachments/assets/08397258-581a-472f-add1-1c59eaa192fc" />

<br>
<br>
<br>
<p>6.8. What tool and parameter did the threat actor use for credential dumping?</em><br>
<code>Invoke-Mimikatz -DumpCreds</code></p>

```splunk
index=* ComputerName="JP-BROWN-WS"  "-DumpCreds"
|  table _time, ProcessId, CommandLine, ParentProcessId, ParentCommandLine
|  sort by +_time
```

<img width="1340" height="473" alt="image" src="https://github.com/user-attachments/assets/10b75966-f825-4af0-89c1-7193d82ac6a4" />

<br>
<br>
<br>
<p>6.9. The threat actor used PowerShell to weaken endpoint defenses. What specific parameter did they attempt to change?</em><br>
<code>IDisableRealtimeMonitoring</code></p>

<br>
<p>6.10. The threat actor used a remote administration tool to execute commands on another machine. What is the PID of the process that initiated the remote execution?</em><br>
<code>6612</code></p>

```splunk
index=* ComputerName="JP-BROWN-WS"  ParentProcessId=6748
|  table _time, User, ProcessId, Image, CommandLine, ParentProcessId, ParentCommandLine
|  sort by +_time
```

<img width="1324" height="365" alt="image" src="https://github.com/user-attachments/assets/d922ccf3-246f-49aa-bcd6-faf109b258fe" />


<br>
<br>
<br>
<p>6.11. At what time did the threat actor successfully log in to the remote system from the beachhead?</em><br>
<code>2025-11-14 05:19:42</code></p>

```splunk
index=* ComputerName=JP-BROWN-WS RuleName=RDP
|  table ProcessId, ComputerName, _time, SourceIp, SourcePort, ComputerName, DestinationIp, DestinationPort, DestinationHostname
|  sort by +_time
```

<img width="1336" height="580" alt="image" src="https://github.com/user-attachments/assets/fb0d1213-c9cf-40a4-b8ec-9ccce56786d3" />

```splunk
index=* ComputerName=JP-BROWN-WS RuleName=RDP
|  table ProcessId, ComputerName, _time, SourceIp, SourcePort, ComputerName, DestinationIp, DestinationPort, DestinationHostname
|  sort by +_time
```

<br>
<br>
<br>
<p>6.12. What is the full path of the PowerShell script used by the threat actor to collect data?</em><br>
<code>C:\Windows\Temp\Setup-BackupServer.ps12</code></p>

```splunk
index=* ComputerName="BKUP-SRV01" "*-OutFile*"
|  table _time, User, ProcessId, CommandLine, ParentProcessId, ParentCommandLine
|  sort by -_time
```

<img width="1344" height="420" alt="image" src="https://github.com/user-attachments/assets/c946afc6-19df-45ae-ba27-8810d84defe2" />

<br>
<br>
<br>
<p>6.13. What are the first four file extensions targeted by this script for collection?</em><br>
<code>2025-11-14 05:19:42</code></p>

