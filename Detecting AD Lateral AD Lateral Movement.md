<h1 align="center"><a href="https://tryhackme.com/room/detectingadlateralmovement">Detecting AD Lateral Movement</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b773919b-7351-4c3d-a71c-8f60ffe52e63"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2017-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<br>
<h2>Task 1 &nbsp;・&nbsp; Introduction</h2> 
<p>In an AD environment, attackers who compromise a single account rarely stop there. They use built-in protocols like SMB and RDP to move from the initial foothold to servers that hold what they actually want, like domain controllers, file servers, and databases. The tricky part for defenders is that these are the same protocols administrators use every day.<br>

This room covers three lateral movement techniques and the log artifacts they produce. We'll start by looking at normal traffic for each protocol, then investigate a simulated attack that uses SMB, PsExec, and RDP to move from a compromised workstation to the Domain Controller.</p>

<h3>Learning Objectives</h3>
<p>

- Detect AD discovery commands through process creation and PowerShell Script Block logs<br>
- Identify SMB-based lateral movement through admin share access patterns<br>
- Identify PsExec usage through service installation artifacts, named pipe creation, and correlate source and destination events<br>
- Detect RDP-based lateral movement using Logon Type 10 and trace multi-hop chains through Logon ID correlation and process artifacts<br>
- Correlate artifacts across source and destination systems to trace an attacker's path</p>

<h3>Prerequisites</h3>
<p>

- Active Directory monitoring: AD architecture, authentication protocols, Windows Event Log structure <a href="https://tryhackme.com/room/monitoringactivedirectory"> (Monitoring Active Directory room)</a><br>
- Initial access detection: How attackers gain their first foothold <a href="https://tryhackme.com/room/detectingadinitialaccess"> (Detecting AD Initial Access room)</a><br>
- Windows Event Logs: Event Viewer navigation, log channels, Event IDs <a href="https://tryhackme.com/room/windowseventlogs"> (Windows Event Logs room)</a><br>
- Splunk basics: SPL queries, filtering, stats commands <a href="https://tryhackme.com/room/splunkexploringspl"> (Splunk: Exploring SPL room)</a></p>

<p>Start the machine by clicking the Start Machine button below. Give the Splunk instance about 4-5 minutes to launch, then access it using the link below. Feel free to continue reading the next tasks while it boots:<br>

- https://LAB_WEB_URL.p.thmlabs.com</p><br>

<strong>Info</strong>: This Splunk instance is used throughout the entire room. The walkthrough tasks (2-6) use <code>index=win</code>. The investigation challenge (Task 7) uses <code>index=challenge</code>, which contains a separate dataset on the same machine. Make sure to set the time range to <strong>All Time</strong> in Splunk before running your queries.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> <em>I have successfully started my Splunk instance.</em><br><a id='1.1'></a>
>> <code>No answer needed</code></strong><br>

<br>
<h2>Task 2 &nbsp;・&nbsp; Discovery and Reconnaissance</h2> 
<p>Although our main focus in this room is lateral movement, we need to start with discovery.<br>

As shown in the image below, when attackers first gain access to a network, they don't know what's in it. They don't know which servers exist, which accounts have elevated privileges, or how the network is organized. So the first thing they do is run commands to map everything out. This helps them understand the environment they've compromised, identify valuable targets, and plan their next move.</p>


<p>...</p>

<p>In this task, we're focusing specifically on AD discovery, meaning commands that query Active Directory for information about domain accounts, groups, trusts, and networked systems. General host-level reconnaissance (like systeminfo or whoami) also happens during this phase, but AD discovery is what gives attackers the map they need to plan their lateral movement.</p>

<h3>What Discovery Looks Like</h3>
<p>Let's look at some Active Directory discovery commands commonly used in real-world attacks. The table below lists the commands you'll encounter most often:</p>

<img width="933" height="587" alt="image" src="https://github.com/user-attachments/assets/47a6aa31-c86c-4cd6-8a8a-9a5a4849f847" />

<p>None of these commands requires admin privileges. Active Directory grants read access to all authenticated domain users by default, which means any compromised account, even one belonging to a marketing or HR user, can enumerate every user, group, trust, and machine in the domain. This is by design, not a misconfiguration, and it's one of the reasons lateral movement planning might sometimes be easy for attackers.<br>

The table above covers the most common built-in commands. Also, attackers use third-party tools like adfind.exe (heavily used by ransomware groups like Conti and FIN7), dsquery, and PowerShell's [System.DirectoryServices.DirectorySearcher] class for raw LDAP queries.<br>

Volt Typhoon, the Chinese state-sponsored group, is known for this exact approach. CISA advisory AA24-038A(opens in new tab) documents their heavy use of commands like net user, nltest, netsh, and wmic for discovery, a technique known as "living off the land" (LOTL). Native commands don't trigger antivirus and blend in with normal administrative activity, which is exactly why they work.</p>

<h3>Detecting Discovery With Sysmon and PowerShell Logs</h3>
<p>We detect these commands through two log sources:

- Sysmon Event 1 captures process creation, where the CMD/PowerShell commands appear in the command line.<br>
- PowerShell Event 4104 captures Script Block Logging, which records the PowerShell commands and cmdlets executed.</p>

<h4>Scenario</h4>
<p>Let's say we want to investigate or hunt for Windows built-in discovery commands in our environment. We would start with Sysmon Event 1 to see what commands were executed:</p>

```bash
index=win EventCode=1
| search CommandLine IN ("*nltest*", "*net * user*", "*net * group*", "*net * view*", "*net * localgroup*")
| table _time, host, User, Image, CommandLine, ParentImage
| sort _time
```

<img width="2834" height="674" alt="image" src="https://github.com/user-attachments/assets/6dc7509c-3728-4aad-8ab9-c2b8383b4bbf" />

<p>The results show when the commands ran, what host they were executed on, and the User who ran them. The CommandLine field reveals what commands the attacker executed and what information they were after.<br>

Seeing discovery commands executed on a workstation that isn't expected to have them executed in a specific time frame is highly likely to indicate malicious discovery activity. And always remember that "context is everything".<br>

We can apply the same idea here for PowerShell-based discovery, but by filtering for Event 4104 (Script Block Logging) captures PowerShell cmdlets:</p>

```bash
index=win EventCode=4104
| search Message IN ("*Get-ADUser*", "*Get-ADGroupMember*", "*Get-ADComputer*")
| table _time, Message
| sort _time
```

<img width="2270" height="760" alt="image" src="https://github.com/user-attachments/assets/f6b5d3ec-8bff-4fc8-a1d9-212666b4d3a1" />

<p>The Message field captures the full script block content, including the cmdlet and all its parameters.</p>

<h3>Script Block Logging</h3>
<p>Script Block Logging can generate a high volume of events, so some organizations enable it only on high-value targets or during active investigations. If it's not available, we can fall back to Sysmon process creation events (Event ID 1) or Windows Security process creation events (Event ID 4688) with command-line auditing enabled. The tradeoff is that Sysmon and 4688 capture the powershell.exe process launch, but if an attacker runs cmdlets interactively within a session, each individual cmdlet won't generate a separate process creation event. Script Block Logging captures every command inside the session, regardless.</p>

> Tip: Attackers sometimes encode or obfuscate discovery commands to evade detection rules. Base64-encoded PowerShell (powershell -enc ...) or cmd.exe character escaping still generates a Sysmon Event 1 for the process creation, though the CommandLine may show the encoded form. Script Block Logging is more resilient here because PowerShell logs the decoded script block after it is processed.

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questios below}}$$ </h3>

> <em>What is the first discovery command the attacker executed? <strong>Note</strong>: The command has an extra whitespace; ensure you copy as it appears in Splunk.</em><br><a id='2.2'></a>
>> <code>nltest  /domain_trusts</code></strong><br>

```bash
index=win EventCode=1
| search CommandLine IN ("*nltest*", "*net * user*", "*net * group*", "*net * view*", "*net * localgroup*")
| table _time, host, User, Image, CommandLine, ParentImage
| sort +_time
```

<img width="1243" height="408" alt="image" src="https://github.com/user-attachments/assets/e396d57c-45a6-41e6-9d2d-0d921a7f3d09" />

<br>
<br>
<br>

> <em>What is the full PowerShell command used to enumerate domain users?</em> Hint: Check the full Message field in Event 4104.<br><a id='2.2'></a>
>> <code>Import-Module ActiveDirectory; Get-ADUser -Filter * -Properties MemberOf | Select-Object Name, SamAccountName</code></strong><br>

```bash
index=win EventCode=4104
| search Message IN ("*Get-ADUser*", "*Get-ADGroupMember*", "*Get-ADComputer*")
| table _time, Message
| sort +_time
```

<img width="1237" height="546" alt="image" src="https://github.com/user-attachments/assets/be5fef0a-afdc-448b-a5e9-c934cce4a6cb" />

<br>
<br>
<br>
<h2>Task 3 &nbsp;・&nbsp; Discovery and Reconnaissance</h2> 
<p>Now that we've seen the discovery phase, let's talk about what happens after the attacker has mapped out the network. They know which servers exist, which accounts have admin rights, and which machines are worth targeting. Their next step is to move to those targets so they can get closer to what they actually want, whether that's the Domain Controller, a database server, or a file share containing sensitive data.<br>

Every lateral movement technique follows the same basic pattern, where the attacker authenticates to a remote machine using stolen or misused credentials, then executes something on it. The technique might differ, but that authenticate-then-execute sequence is always there.</p>

<img width="744" height="455" alt="image" src="https://github.com/user-attachments/assets/71f8c4cf-8e10-4081-80cd-5c0f90d3d760" />


<h3>The Source and Destination Model</h3>
<p>Every remote connection creates artifacts on two machines:<br>

- One is the source, where the attacker initiates the connection. It also only sees which credentials were used and which target was chosen.<br>
- The other is the destination, where the session lands and the action happens. The destination sees that someone connected and what they did.<br>

If we only check the destination, we know the attack happened, but might not know where it originated. If we only check the source, we know the intent but not whether it succeeded.</p>

<img width="726" height="304" alt="image" src="https://github.com/user-attachments/assets/fc307bb7-07eb-44f7-ba2b-0073cd8d668c" />

<h3>Logon Type: The First Thing to Check</h3>
<p>When someone connects to a remote machine, Windows logs Event 4624 on the destination. The Logon_Type field tells us how they connected.</p>

<img width="937" height="205" alt="image" src="https://github.com/user-attachments/assets/4202b032-64c0-4095-921f-822eae0b4f71" />

<p>Type 10 is straightforward because it always means RDP. Type 3 is trickier because SMB and PsExec both generate Type 3 logons, so we need additional artifacts to tell them apart. We'll cover those in the upcoming tasks.</p>

> Note: If an attacker connects via RDP while the same account already has an active or disconnected session on that host, Windows reconnects them to the existing session instead of creating a new one. This generates a Type 7 (Unlock) logon instead of Type 10. During an investigation, if we see a Type 7 with a remote IP address (not 127.0.0.1), that indicates an RDP reconnection, not a physical workstation unlock. Keep this in mind when searching for RDP activity: filtering only for Logon_Type=10 will miss these reconnections. Also note that a reconnection assigns a new Logon_ID even though the RDP session itself persists, so Logon_ID-based correlation can break at disconnect/reconnect boundaries.

<h4>Event 4648: Tracing the Source</h4>
<p>Event 4648 (Logon Using Explicit Credentials) fires on the source machine when a process uses credentials other than those of the currently logged-in user.<br>

For example, as shown in the screenshot below, if liam.patel runs net use \\THM-SHR-SRV\ADMIN$ /user:luke.sullivan, Event 4648 is logged on THM-MKT-WS and records the original account (liam.patel), the alternate account (luke.sullivan), and the target server name (THM-SHR-SRV).</p>

<img width="1141" height="1263" alt="image" src="https://github.com/user-attachments/assets/c51fef4c-95fd-4905-87c8-5d3058091731" />

<p>This tells us directly which machine initiated the connection and what credentials were used. Most destination-side logs only show who connected, not who was sitting at the keyboard when the event occurred.<br>

Sysmon Event 1 (Process Creation) also captures the net.exe process with the full command line, including the target server and the account specified in the /user: flag and the password.</p>

<img width="1587" height="1232" alt="image" src="https://github.com/user-attachments/assets/aa27f6e2-b98e-4347-a683-4559b6f389e6" />

<p>Together, these two source-side events provide better context for the same activity.</p>

> Warning: Event 4648 only fires when credentials are explicitly provided, such as with net use /user:, runas, or entering credentials in an RDP dialog. It doesn't fire for Pass-the-Hash, Pass-the-Ticket, or Kerberos single sign-on, because those techniques reuse cached credentials without explicitly providing them.





<h3>Normal vs Suspicious: Same Events, Different Context</h3>
<p>A legitimate admin session and an attacker's lateral movement generate the same Event IDs. Both produce Event 4624, both can generate Event 4648, and both are "successful authentication to a remote host." What separates them is context.</p>

<img width="934" height="300" alt="image" src="https://github.com/user-attachments/assets/7be800a1-70f1-4301-84d9-6e963e3b759f" />

<p>We'll apply this concept of checking context around events throughout the rest of this room.</p>

<h3>Why Lateral Movement Succeeds</h3>
<p>Lateral movement mainly works because of common misconfigurations:<br>

- Password reuse across local admin accounts means that a compromised credential can unlock many machines (Microsoft LAPS is designed to prevent this)<br>
- Shared administrative accounts<br>
- Overly permissive group memberships<br>
- Bad network segmentation between hosts<br>
- Leaving RDP enabled on machines that don't need it widens the attack surface<br>

A single compromised credential can unlock an entire network when these misconfigurations exist. Detection is important, but hardening the environment to limit where credentials can be used is just as valuable.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What Logon Type in Event 4624 indicates a remote desktop session?</em><br><a id='3.1.'></a>
>> <code>10</code></strong><br>

<br>

> <em>What Event ID, logged on the source system, records when a process uses alternate credentials to connect to a remote resource?</em><br><a id='3.2.'></a>
>> <code>4648</code></strong><br>

<br>
<h2>Task 4 &nbsp;・&nbsp; Detecting SMB Lateral Movement</h2> 

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What account was used to access the ADMIN$ shares?</em><br><a id='4.1.'></a>
>> <code>luke.sullivan</code></strong><br>

```bash
index=win EventCode=5140 Share_Name IN ("*\\ADMIN$\*", "*\\C$\*")
| table _time, host, Source_Address, user, Share_Name
| sort +_time
```

<img width="1240" height="394" alt="image" src="https://github.com/user-attachments/assets/d91ece89-28c2-47e3-a1d8-a0d487c7cfd8" />

<br>
<br>
<br>

> <em>Which user account was responsible for executing the lateral movement commands?</em><br><a id='4.2.'></a>
>> <code>michelle.smith</code></strong><br>

```bash
index=win EventCode=1 CommandLine="*ADMIN$*"
| table _time, User, Image, CommandLine
| sort +_time
```

<img width="1236" height="392" alt="image" src="https://github.com/user-attachments/assets/8e54c4b0-ef11-46cf-a92e-5c5358587ff7" />

<br>
<br>
<br>
<h2>Task 5 &nbsp;・&nbsp; Detecting PxExec Lateral Movement</h2> 
<p>In the previous task, we looked at raw admin share access through <code>net use</code>code>. That approach lets an attacker copy files and browse directories remotely, but it doesn't execute anything on the target. PsExec changes that. It's a Sysinternals tool that combines SMB admin share access with Windows service installation to run commands on remote systems.<br>

It's worth understanding how PsExec works under the hood, because it leaves a very specific trail of artifacts. Even when attackers rename the binary, the underlying behavior stays the same.</p>

<h3>How PsExec Works</h3>
<p>When an attacker already has an authenticated SMB session (via <code>net use</code>code>) and runs <code>PsExec.exe \\target cmd.exe</code>code>, the following happens:<br>

- PsExec connects to the target's <code>ADMIN$</code> share over SMB<br>
- Tt copies a service binary (<code>PSEXESVC.exe</code>) to the target's C:\Windows directory<br>
- It creates and starts a new Windows service on the target (System Event 7045)<br>
- The service creates named pipes for <code>stdin</code>/<code>stdout</code>/<code>stderr</code> communication (Sysmon Event 17)<br>
- That service executes whatever command the attacker specified<br>
- When the session ends, PsExec removes the service and cleans up the binary<br>

Event 7045 (A New Service Was Installed) in the System log is the signature artifact for PsExec, logged on the <strong>destination</strong> machine. This is what distinguishes PsExec from plain SMB access.<br>

The diagram below shows exactly this sequence.</p>

<img width="833" height="410" alt="image" src="https://github.com/user-attachments/assets/401e5cc8-ace4-420e-a438-372dd676601d" />

<h3>Why Attackers Use PsExec</h3>
<p>PsExec is a legitimate administration tool. Sysadmins use it daily to push patches, run scripts, and troubleshoot remote machines. From a protocol perspective, PsExec traffic appears identical to normal SMB administration traffic. The only difference is context: which account, from which machine, at what time, and how it was used.<br>

<strong>Wizard Spider</strong>, the group behind Ryuk and Conti ransomware, used PsExec extensively for deployment. In incidents documented by Red Canary(opens in new tab), they would compromise one machine, harvest credentials with Mimikatz, then use PsExec to push ransomware to every reachable server in minutes. Each lateral hop created a service via <code>ADMIN$</code>, recorded by Event 7045.</p>

<h3>Investigating PsExec Activity</h3>
<h4>Detecting PsExec: Destination Side</h4>
<p>The destination side is where PsExec's unique signature appears. Let's check Event 7045 (service installation):</p>

```bash
index=win EventCode=7045
| table _time, host, Service_Name, Service_File_Name, Service_Type, Service_Start_Type, Service_Account
| sort _time
```

<img width="2100" height="343" alt="image" src="https://github.com/user-attachments/assets/059b68bb-ac96-4a67-852f-2f6bd3aadc09" />

<p>In its default configuration, the service name is PSEXESVC and the binary path points to C:\Windows\PSEXESVC.exe (equivalent to %SystemRoot%\PSEXESVC.exe). The Service_Account field tells us which account the service runs under.<br>

By default, PsExec runs the remote command as the authenticating user. When run with the -s flag, the service runs as LocalSystem, granting SYSTEM-level access on the target.</p>

<h4>What Commands Did the Attacker Run></h4>
<p>Once we've identified the PsExec service through Event 7045, and the host it was created on, the next step is to find what commands the attacker actually executed through it.<br>

Since PSEXESVC.exe is the service that spawns the attacker's remote commands, we can use process creation events (e.g., Sysmon Event 1) and filter by ParentImage to find processes created or commands executed by the service binary:</p>

```bash
index=win EventCode=1 host={DESTINATION_HOST} ParentImage="*PSEXESVC*"
| table _time, host, User, ParentImage, Image, CommandLine
| sort _time
```

<img width="2755" height="316" alt="image" src="https://github.com/user-attachments/assets/eb26e035-9cdb-4757-902f-65adb061c2dd" />

<p>The ParentImage field shows which process spawned each command. By filtering for PSEXESVC, we see only the commands that were executed remotely through PsExec.</p>

<h4>Named Pipe Artifacts (Sysmon Event 17)</h4>
<p>PsExec uses named pipes to relay stdin, stdout, and stderr between the source and destination. Sysmon Event 17 (Pipe Created) captures these on the destination:</p>

```bash
index=win EventCode=17 Image="*PSEXESVC*"
| table _time, host, Image, PipeName
| sort _time
```

<img width="2463" height="407" alt="image" src="https://github.com/user-attachments/assets/d8b13ba4-5362-40e3-9f9e-8456dd29c1b1" />

<p>PsExec creates pipes with names like \PSEXESVC-<hostname>-<pid>-stdin, -stdout, and -stderr. These pipe names are useful because even if an attacker renames the PsExec binary, the pipe naming convention often remains unchanged (unless they modify the source code).</p>



<h4>Tracing PsExec Usage with Event 5145</h4>
<p>We've identified the service and the commands it executed. Now we need to identify who initiated this and where they connected from.<br>

Event 5145 (Detailed File Share) goes further, where it logs the specific files and objects accessed through that share, which are shown in the Relative_Target_Name field. For PsExec, this event is a goldmine.<br>

Replace {DESTINATION_HOST} with the target machine that we found earlier in the investigation.</p>

```bash
index=win EventCode=5145 host={DESTINATION_HOST} Relative_Target_Name="*PSEXE*"
| table _time, user, Source_Address, Share_Name, Relative_Target_Name
| sort _time
```

<img width="2693" height="803" alt="image" src="https://github.com/user-attachments/assets/883eefdc-950c-4963-92ab-6a275eb602d7" />

<p>Notice that the named pipe names contain the source hostname, revealing which machine the attacker is operating from.</p>

> Tip: Events 5140 and 5145 require "Audit File Share" and "Audit Detailed File Share" to be explicitly enabled via Group Policy. If we search for these events during an investigation and get zero results, it doesn't necessarily mean the activity didn't happen. It may mean the audit policy isn't enabled in that environment.



<h4>Detecting PsExec: Source Side</h4>
<p>Once we find the commands executed and the service name, we can easily track the source host from which PsExec was executed. Sysmon Event 1 captures the process creation with the full command line:</p>


```bash
index=win EventCode=1 host={SOURCE_HOST}
| search Image="*PsExec*"
| table _time, host, User, Image, CommandLine
| sort _time
```

<img width="2448" height="302" alt="image" src="https://github.com/user-attachments/assets/1197bfa2-869e-4fae-9ac3-0231eedbfe3d" />

<p>The CommandLine field shows which target was specified and what command is being run remotely.<br>

By correlating source and destination PsExec artifacts, we now have the full picture of what actually happened.</p>

<h3>Hunting for Renamed PsExec</h3>
<p>Attackers know that security tools look for PSEXESVC by name. PsExec's -r flag lets the operator specify a custom service name, so running PsExec -r renamed_psexec \\target cmd creates a service called renamed_psexec instead of PSEXESVC.<br>

Other tools like Impacket's psexec.py or Cobalt Strike's PsExec module generate random service names by default. But Event 7045 still fires regardless of the name.<br>

The pattern to look for is any new service with Service_Type of "user mode service" and Service_Start_Type of "demand start." The service name and binary might differ, but the demand-start, user-mode-service signature remains.<br>

<strong>On the Splunk instance, investigate the PsExec lateral movement using the Sysmon and System logs</strong>.</p>


<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>WWhat was the destination host the attacker targeted via PsExec?</em><br><a id='5.1.'></a>
>> <code>THM-SQL-SRV</code></strong><br>

```bash
index=win EventCode=7045
| table _time, host, Service_Name, Service_File_Name, Service_Type, Service_Start_Type, Service_Account
| sort +_time
```

<img width="1237" height="326" alt="image" src="https://github.com/user-attachments/assets/304dc013-df77-468a-a924-e55691f27d06" />

<br>
<br>
<br>

> <em>What is the first command that the attacker executed from the source machine using PsExec? <strong>Note</strong>: The command has an extra whitespace; ensure you copy as it appears in Splunk.</em><br><a id='5.2.'></a>
>> <code>C:\Tools\PsExec.exe  -accepteula \\THM-SQL-SRV cmd /c "hostname & whoami & ipconfig"</code></strong><br>

```bash
index=win "*PsExec*"
| table _time, host, Account_Name, Share_Name Source_Address User, ParentImage, Image, CommandLine
| sort +_time
```

<img width="1237" height="682" alt="image" src="https://github.com/user-attachments/assets/683784c6-2d92-42f1-b280-55d45a287182" />


<br>
<br>
<br>
<h2>Task 6 &nbsp;・&nbsp; Detecting RDP Lateral Movement</h2> 
<p>RDP gives the attacker a full interactive desktop session, but it doesn't leave the same kind of obvious hunting artifacts as the previous techniques. There's no service installation, no share access pattern, no unique process on the destination that says "this was RDP." So we rarely start an investigation by hunting for RDP sessions directly. Instead, we usually find RDP as the delivery mechanism after something else catches our attention.<br>

RDP's primary detection artifact is Event 4624 with Logon_Type=10 (RemoteInteractive), logged on the destination. It records the account name, the source IP address, and the session timestamp. While SMB and PsExec both produce Type 3 network logons, a successful RDP session produces Type 10, making it immediately distinguishable in the Security log. However, NLA introduces a variation worth understanding, covered in the info box below.</p>


> <strong>Info:</strong> Modern Windows enables Network Level Authentication (NLA) by default. With NLA, the user authenticates at the network level before the RDP session is established, which generates a brief Type 3 logon right before the Type 10. If we see a Type 3 from the same source IP appearing seconds before a Type 10, that's the NLA prelude, not a separate SMB or PsExec connection. The lab environment in this room has NLA enabled, so you may see these Type 3 events alongside the Type 10 logons in your query results.


<p><strong>BlackSuit</strong>  (the successor to Royal ransomware, covered in the updated CISA advisory AA23-061A(opens in new tab)) relies on RDP as a primary lateral movement method. According to the FBI, BlackSuit actors combine RDP, PsExec, and SMB to move through victim networks and, in one confirmed case, used a legitimate admin account to reach the domain controller directly.</p>

<h3>Normal vs Suspicious RDP Traffic</h3>
<p>Before we start investigating, it helps to have a mental model for which RDP connections are normal and which ones should raise questions. The direction of the connection matters:</p>

<img width="935" height="224" alt="image" src="https://github.com/user-attachments/assets/ed6f3a73-dd57-4ea8-9e88-6f9ec4e9898b" />

<p>These patterns aren't rules. There are environments where server-to-server RDP is normal (e.g., jump boxes). But as a starting point, any RDP session originating from a server rather than a workstation warrants a closer look.</p>

<h3>Investigating RDP Lateral Movement</h3>
<p>We wouldn't normally jump directly into RDP logs because they can be very noisy. Instead, let's say we received an alert for discovery commands being executed on our Domain Controller. We start by looking at process creation logs:</p>

```bash
index=win EventCode=1 host=THM-DC
| search CommandLine IN ("*nltest*", "*net * user*", "*net * group*", "*net * view*")
| table _time, host, User, Image, CommandLine, LogonId
| sort _time
```

<img width="2830" height="218" alt="image" src="https://github.com/user-attachments/assets/4f2f2ae3-9a8a-4f99-95bb-5c8297adc038" />


<p>We can see a discovery command being executed on the Domain Controller. The LogonId field tells us which session these commands belong to. Let's use it to find out how this session was created.</p>

<h4>Identify How the Attacker Reached the Domain Controller</h4>
<p>We take the LogonId from the suspicious commands and correlate it with Event 4624 (successful logon) on the same host:<br>

Replace {LOGON_ID} with the LogonId from the Sysmon event above.</p>

```bash
index=win EventCode=4624 host=THM-DC Logon_ID={LOGON_ID}
| table _time, user, Logon_Type, Source_Network_Address, Logon_ID
```

<img width="2809" height="213" alt="image" src="https://github.com/user-attachments/assets/295faaad-814f-44b9-b0df-3a6278189d7d" />

<p>The Logon_Type field shows 10, which means the attacker reached the Domain Controller over RDP. We can check the Source_Network_Address field to know where the attacker connected from.</p>

<h4>Identifying the Source Hostname</h4>
<p>We have the source IP from the Source_Network_Address field, but we need the hostname to query Sysmon logs on that machine. Using the same machine account technique from Task 4:<br>

Replace {SOURCE_IP} with the Source_Network_Address from the 4624 event above.</p>

```bash
index=win EventCode=4624 Source_Network_Address={SOURCE_IP} user=*$
| stats count by user, Source_Network_Address
| sort -count
```

<img width="2822" height="215" alt="image" src="https://github.com/user-attachments/assets/75246954-9224-4bdc-b689-4eb5b9bd6cf3" />

<p>The user ending with $ reveals the machine's hostname. Drop the $ suffix and use it in the next step.</p>

<h4>Find Evidence of the Outbound RDP Connection on the Source</h4>
<p>When someone initiates an RDP connection from a machine, mstsc.exe (the Windows Remote Desktop Client) runs on that machine. If Sysmon is capturing process creation on that host, we can search for it:<br>

Replace {SOURCE_SERVER} with the hostname identified above.</p>

```bash
index=win EventCode=1 host={SOURCE_SERVER} Image="*mstsc.exe*"
| table _time, User, Image, CommandLine, LogonId
| sort _time
```

<img width="2810" height="218" alt="image" src="https://github.com/user-attachments/assets/d621c495-0b23-4e91-a3bf-3a42925f7582" />

<p>This confirms that someone launched an outbound RDP connection from that server targeting the Domain Controller.<br>

Now we can trace how the attacker got onto this server in the first place.</p>

<h4>Trace How the Attacker Reached the Intermediate Server</h4>
<p>Using the same correlation technique, we take the LogonId from the mstsc.exe process and match it against Event 4624 on the same server:</p>

```bash
index=win EventCode=4624 host={SOURCE_SERVER} Logon_ID={LOGON_ID}
| table _time, user, Logon_Type, Source_Network_Address, Logon_ID
```

<img width="2813" height="200" alt="image" src="https://github.com/user-attachments/assets/61667a8d-657a-4557-a1f3-1bda3fcb37f5" />

<p>We can see another RDP login, but this time, from a different user and a different source than the one we saw on the Domain Controller.<br>

The attacker started on a compromised workstation, used RDP to reach the server, then, from within that session, opened another RDP connection to the Domain Controller using a different, more privileged account.<br>

This pattern is called RDP chaining, and it's common when attackers pivot through intermediate machines to reach sensitive targets like Domain Controllers. Each hop uses RDP, but the source IP address changes at each hop because the connection originates from the intermediate machine rather than the original workstation.<br>

The diagram below shows how RDP chaining works.</p>

<img width="732" height="242" alt="image" src="https://github.com/user-attachments/assets/733f3387-2337-4e51-bf77-e98dbb33bb12" />

<p><strong>On the Splunk instance, investigate the RDP lateral movement using the Security and Sysmon logs and answer the following questions.</strong></p>

<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What is the source IP address of the RDP session that landed on the Domain Controller?</em> Hint: Correlate the LogonId from the Sysmon process to Event 4624.<br><a id='6.1.'></a>
>> <code>10.5.30.120</code></strong><br>

<p>

- LogonId: 0x508C55A</p>

```bash
index=win EventCode=1 host=THM-DC
| search CommandLine IN ("*nltest*", "*net * user*", "*net * group*", "*net * view*")
| table _time, host, User, Image, CommandLine, LogonId
| sort _time
```

<img width="1233" height="325" alt="image" src="https://github.com/user-attachments/assets/c2954ab0-c960-421a-9504-bcd85548bf42" />

<br>
<br>

```bash
index=win EventCode=4624 host=THM-DC Logon_ID=0x508C55A
| table _time, user, Logon_Type, Source_Network_Address, Logon_ID
```

<img width="1230" height="297" alt="image" src="https://github.com/user-attachments/assets/68d2602d-bb25-4557-aec1-9e8fdc1897a0" />

<br>
<br>
<br>

> <em>Tracing backward through the chain, what is the original source IP where the RDP chain began?</em><br><a id='5.2.'></a>
>> <code>10.5.50.12</code></strong><br>

```bash
index=win EventCode=4624 Source_Network_Address=10.5.30.120 user=*$
| stats count by user, Source_Network_Address
| sort -count
```

<img width="1229" height="300" alt="image" src="https://github.com/user-attachments/assets/fc98837f-4900-4968-bbee-f38490ebc96f" />


<br>
<br>
<br>
<h2>Task 7 &nbsp;・&nbsp; Investigation Challenge</h2> 
<h3>Scenario</h3>
<p>The SOC team received an EDR alert for a suspicious service installation (svcupdate) on THM-SHR-SRV. The service name doesn't match any known software deployments, and no change requests were scheduled for that evening. Your task is to investigate this lateral movement activity and trace it back to its origin.</p>

<h3>Machine Access</h3>
<p>The challenge data is on the same Splunk instance you've been using, but in a different index.</p>

<p>ℹ️ &nbsp;&nbsp; <strong>Info</strong>: Use <code>index=challenge</code> for all queries in this task. This index contains a separate dataset from the walkthrough scenarios.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

<p>7.1. &nbsp;&nbsp; What is the full path of the service binary that was installed on the target?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hint: Check the Service_File_Name Event 7045.<a id='7.1.'></a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>%SystemRoot%\svcupdate.exe</code></p>

```bash
index=challenge EventCode=7045 
|  table _time, Service_File_Name
|  sort by +_time
```

<img width="1237" height="327" alt="image" src="https://github.com/user-attachments/assets/584e5c4d-0d8c-4cdd-b9eb-bc1f59c46435" />

<br>
<br>
<br>
<p>7.2. &nbsp;&nbsp; What account was used to access the ADMIN$ share on the target server?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hint: Use Event 5140 to check who accessed admin shares.<a id='7.2.'></a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>ryan.chen</code></p>


```bash
index=challenge EventCode=4624 host="THM-SQL-SRV" Logon_Type=10
|  table _time, host, Account_Name, Logon_Type, user, Source_Network_Address
|  sort by +_time
```

<img width="1230" height="308" alt="image" src="https://github.com/user-attachments/assets/fcab6efc-b434-41f4-903e-f8effaf8b32c" />

<br>
<br>
<br>
<p>7.3. &nbsp;&nbsp; What is the source IP address of the lateral movement to THM-SHR-SRV?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hint: Use Event 5140 to check who accessed admin shares<a id='7.3.'></a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>10.5.50.15</code></p>

<br>
<p>7.4. &nbsp;&nbsp; What is the first remote command the attacker executed on the target machine?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Answer Format: as shown in the <code>CommandLine</code> field)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hint: Use Sysmon Event 1 and filter by ParentImage to find commands run by the svcupdate service.<a id='7.4.'></a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>md" /c "hostname & whoami & ipconfig"</code></p>

```bash
index=challenge EventCode=1 ParentImage="*svcupdate*"
|  table _time host, ParentCommandLine, ParentImage, CommandLine, Image, RuleName
|  sort by +_time
```

<img width="1236" height="325" alt="image" src="https://github.com/user-attachments/assets/6f61c9f0-cdf3-4adf-8199-e6bf41ed3f4a" />

<br>
<br>
<br>
<p>7.5. &nbsp;&nbsp; What host did the attack originate from?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hint: Check Event 5145 on the target. The named pipe names in the Relative_Target_Name field contain the source hostname.<a id='7.5.'></a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>THM-HR-WS</code></p>

```bash
index=challenge EventCode=5145 user=ryan.chen host="THM-SHR-SRV"
|  table _time, Source_Address, Accesses, file_name, file_path, Share_Name, Relative_Target_Name
|  sort by +_time
```

<img width="1233" height="708" alt="image" src="https://github.com/user-attachments/assets/d21dfb53-2655-44e8-9305-681b7f095712" />

<br>
<br>

```bash
index=challenge EventCode=5145 user="ryan.chen" host="THM-SHR-SRV"
| stats earliest(_time) as start_time, latest(_time) as end_time, values(Accesses) as actions, values(Relative_Target_Name) as files_touched by Source_Address, Share_Name
| eval duration = end_time - start_time
| table start_time, Source_Address, Share_Name, files_touched, actions
```

<img width="1239" height="489" alt="image" src="https://github.com/user-attachments/assets/b20182f2-86e1-4c26-bf07-d74d76785882" />

<br>
<br>
<br>
<h2>Task 8 &nbsp;・&nbsp; Clonclusion</h2> 
<p>This room covered three lateral movement techniques (SMB, PsExec, RDP), how each authenticates against Active Directory, and the traces they leave on both source and destination machines.</p>

<h3>Takeaways</h3>
<p>

- Discovery commands in process creation logs are often the first indicator that triggers a lateral movement investigation. Spotting enumeration early can lead to catching lateral movement before it reaches sensitive targets.<br><br>
- The same Event <code>4624</code> fires for a legitimate admin and an attacker.<br>Source workstation, account, timing, and target pattern are what distinguish them.<br><br>
- Type <code>10</code> means <code>RDP</code>.<br>Type <code>3</code> covers <code>SMB</code> and <code>PsExec</code>, where additional artifacts (Event <code>5140</code>, Event <code>7045</code>, Sysmon Event <code>17</code>) separate the two.<br><br>
- Event <code>4648</code> ties the <code>initiating user to the target connection</code> by recording alternate credential use on the source, but only for explicit credentials, not Pass-the-Hash or Kerberos SSO.<br><br>
- Admin share access (<code>ADMIN$</code>, <code>C$</code>) from unexpected sources is a strong <code>lateral movement indicator</code>.<br>Event <code>5140</code> captures <code>who accessed which share and from where</code>.<br><br>
- Sysmon Event <code>17</code> detects characteristic <code>PsExec pipe patterns</code> that persist even when the binary is renamed.<br>Event <code>7045</code> (service installation) is <code>PsExec</code>'s signature artifact.<br><br>
- Link RDP sessions with <code>Logon_ID</code> and look for <code>mstsc.exe</code> on intermediate hosts to trace chained hops. Each hop changes the source IP, so tracing the full chain requires checking both source and destination logs.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

<p>8.1. &nbsp;&nbsp; Great work! You have completed the Detecting AD Lateral Movement room.<a id='8.1.'></a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>No answer needed</code></p>

<br>
<br>

<h1 align="center">Completed</h1>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/db9582db-b6b1-4f25-8648-66367576cacb"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/64626f48-025d-45c2-9cd7-8773d2e891c0"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/9126e6ae-8405-4e26-ab48-a1328aa14ebe"></p>

         
<h1 align="center">My TryHackMe Journey ・ 2026, March<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Room Name<br><br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|League<br><br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|---------------:|
|17<br><br><br>  |75<br><br><br>    |Detecting AD Lateral Movement|Medium<br><br><br>|🔗<br><br><br>| 1,149<br><br><br>| 160,883<br><br><br>| 91<br><br><br>| 16ᵗʰ<br><br><br>| 9ᵗʰ<br><br><br>| 2ⁿᵈ<br><br><br>| 1ˢᵗ<br><br><br>|-<br><br><br>|
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

<p align="center">Global All Time:     16ᵗʰ<br><img width="250px"  src="https://github.com/user-attachments/assets/9254d3dd-9fdb-498a-996e-e0acd3f924d7"><br>
                                               <img width="1200px" src="https://github.com/user-attachments/assets/2955bfca-c529-4c78-85ea-5ff819038380"><br><br>
                  Global Monthly:       9ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/729fd187-ad49-4c0d-bfa7-e9bd4dde25ff"><br><br>
                  Brazil All Time:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/e9562a96-41c3-4d4b-bd98-589c12b3bf40"><br><br>
                  Brazil Monthly:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/797d7328-0b1e-4597-b083-5178fa24ed75"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
