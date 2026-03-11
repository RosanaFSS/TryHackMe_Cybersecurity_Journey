<h1 align="center"><a href="https://tryhackme.com/room/detectingadinitialaccess">Detecting AD Initial Access</a></h1>
<p align="center"><img width="1200px" src=""><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2011-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<h2>Task 1 &nbsp;・&nbsp; Introduction</h2> 
<p>In an AD environment, every internet-facing service that authenticates against the domain is a potential entry point. This room teaches how to detect initial access attacks against three of the most common ones: IIS web applications, Exchange OWA, and VPN gateways.<br>

Each scenario uses a different application log source, but they share a common principle:<br>

- The attack is visible in the application logs first<br>
- Then, correlating with other log sources (e.g., Sysmon and Windows Security logs) to reveal the full scope</p>

<h3>Learning Objectives</h3>
<p>
  
- Analyze IIS logs to detect web application attacks and web shell activity<br>
- Correlate Exchange/OWA authentication events with Windows Security logs<br>
- Investigate VPN credential attacks using NPS event logs<br>
- Investigate post-authentication activity to determine the impact of a breach<br>
- Build investigation timelines by correlating application logs with Windows Security logs</p>

<h3>Learning Prerequisites</h3>
<p>
  
- <strong>Active Directory</strong>: How users, groups, and authentication work (<a href="https://tryhackme.com/room/winadbasics">Active Directory Basics</a> room)<br>
- <strong>Windows Event Logs</strong>: Reading and filtering Security events (<a href="https://tryhackme.com/room/windowseventlogs">Windows Event Logs</a> room)<br>
- <strong>Splunk</strong>: Writing SPL queries to search and filter log data (<a href="hhttps://tryhackme.com/room/splunkexploringspl">Splunk: Exploring SPL</a> room)<br>
- <strong>AD Monitoring</strong>: Understanding the main Event IDs needed to know what's normal in AD to detect abnormal (<a href="https://tryhackme.com/room/monitoringactivedirectory">Monitoring Active Directory</a> room)</p>

<h3>Machine Access</h3>
<p>Start the machine by clicking the Start Machine button below. Give the Splunk instance about 4-5 minutes to launch, then access it using the link below. Feel free to continue reading the next tasks while it boots:<br>

https://LAB_WEB_URL.p.thmlabs.com</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> <em>I have successfully started my Splunk instance.</em><br><a id='1.1'></a>
>> <code>No answer needed</code></strong><br>

<br>
<h2>Task 2 &nbsp;・&nbsp; Understanding IIS and Its Logs</h2> 
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> <em>Where does IIS store access logs by default?</em><br><a id='2.1'></a>
>> <code>C:\inetpub\logs\LogFiles\W3SVC1</code></strong><br>


<br>
<h2>Task 3 &nbsp;・&nbsp; Detecting Web Shell Deployment</h2> 
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What is the filename of the web shell the attacker used?</em><br><a id='3.1'></a>
>> <code>shell.aspx</code></strong><br>

```bash
index=iis sc_status=404
| stats count by c_ip
| sort - count
```

<img width="957" height="309" alt="image" src="https://github.com/user-attachments/assets/e36d66db-657e-429f-9c0f-eb8be6e82152" />

<br>
<br>

```bash
index=iis
| stats count by c_ip, sc_status
| sort - count
```

<img width="945" height="598" alt="image" src="https://github.com/user-attachments/assets/0d9d0cc3-bb0f-402d-87e7-6bcc37b38bbb" />

<br>
<br>

> <em>What IP address was used to interact with the web shell?</em><br><a id='3.2'></a>
>> <code>203.0.113.47</code></strong><br>

```bash
index=iis cs_uri_stem="*aspnet_client/*"
| stats count by c_ip, cs_uri_stem
| sort - count
```

<img width="957" height="350" alt="image" src="https://github.com/user-attachments/assets/c699775d-a727-4498-8bc1-0856c8cacc35" />

<br>
<br>

> <em>After accessing the web shell, what was the first reconnaissance command the attacker executed?</em><br><a id='3.3'></a>
>> <code>whoami</code></strong><br>

```bash
index=iis cs_uri_stem="*aspnet_client/*"
| table _time, c_ip, cs_method, cs_uri_query, sc_status
| sort -_time
```

<img width="956" height="468" alt="image" src="https://github.com/user-attachments/assets/98be912b-36a9-4d76-baac-ef53e010e5fb" />

<br>
<br>
<br>
<h2>Task 4 &nbsp;・&nbsp; Exchange, OWA, and Credential Attacks</h2> 
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What virtual directory path provides access to the Exchange admin console? (Answer Format: /path)</em><br><a id='4.1'></a>
>> <code>/ecp</code></strong><br>

<br>

> <em>What virtual directory path provides access to the Exchange admin console? (Answer Format: /path)</em><br><a id='4.1'></a>
>> <code>4625</code></strong><br>

<br>
<h2>Task 5 &nbsp;・&nbsp; Detecting OWA Brute-Force Attacks</h2> 
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>How many failed login attempts occurred during the OWA brute-force attack?</em><br><a id='5.1'></a>
>> <code>   </code></strong><br>

```bash
index=iis cs_uri_stem="/owa/auth.owa" cs_method=POST
| bin _time span=5m
| stats count by _time, c_ip
| where count > 10
| sort - count
```

<img width="1270" height="334" alt="image" src="https://github.com/user-attachments/assets/20544de9-a1b7-49fe-8da0-e8df23f6d31e" />

<br>
<br>

> <em>What username was successfully compromised in this attack?)</em><br><a id='5.2'></a>
>> <code>sarah.kim</code></strong><br>

```bash
index=win EventCode=4625
| stats count by user, Logon_Type
| sort - count
```

<img width="1267" height="369" alt="image" src="https://github.com/user-attachments/assets/58915438-ae67-44a3-baac-f0583e0d1429" />

<br>
<br>

```bash
index=win EventCode=4625
| stats count by user, Logon_Type
| sort - count
```

<img width="1267" height="369" alt="image" src="https://github.com/user-attachments/assets/58915438-ae67-44a3-baac-f0583e0d1429" />

<br>
<br>

```bash
index=win EventCode IN (4624, 4625) user="sarah.kim" Logon_Type=8
| table _time, EventCode, user, Process_Name, Logon_Type
| sort +_time
```

<img width="1269" height="684" alt="image" src="https://github.com/user-attachments/assets/1882b40f-d1c7-4606-8962-95390154c11f" />


<br>
<br>

> <em>What source IP address conducted this brute-force attack?</em><br><a id='5.3'></a>
>> <code>203.0.113.47</code></strong><br>

<br>

> <em>After the successful login, what path did the attacker access to reach the Exchange admin console? (Answer Format: /path)</em><br><a id='5.4'></a>
>> <code>/ecp</code></strong><br>

```bash
index=iis
|  table _time, EventCode, cs_method, cs_uri_query, cs_uri_stem, c_ip, s_ip, s_port, cmd
|  sort by +_time
```

<img width="1263" height="735" alt="image" src="https://github.com/user-attachments/assets/d802113d-9caf-47ac-b744-bf338dc03cb5" />

<br>
<br>
<h2>Task 6 &nbsp;・&nbsp; VPN and Active Directory</h2> 
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What Windows Event ID indicates that NPS granted network access to a VPN user?</em><br><a id='6.1'></a>
>> <code>6272</code></strong><br>

<br>

> <em>In a typical enterprise VPN deployment, what protocol does the VPN gateway use to communicate authentication requests to NPS?</em><br><a id='6.2'></a>
>> <code>RADIUS</code></strong><br>

<br>
<h2>Task 7 &nbsp;・&nbsp; Detecting VPN Credetntial Attacks</h2> 
<br>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What username was successfully compromised via VPN after the credential attack?</em><br><a id='7.1'></a>
>> <code>david.chen</code></strong><br>

<br>

> <em>Based on the NPS access-accept event, at what time did the successful VPN authentication occur? (Answer Format: HH:MM:SS)</em><br><a id='7.2'></a>
>> <code>10:47:06</code></strong><br>


```bash
index=win EventCode=6273
|  table _time, EventCode, cs_method, User_Account_Name, Client_IP_Address
|  sort by +_time
```

<img width="1267" height="504" alt="image" src="https://github.com/user-attachments/assets/31a6bcdb-f56d-4838-ace9-42df51d52fc6" />

<br>
<br>

```bash
index=win EventCode=6273
| stats count by User_Account_Name, Client_IP_Address
| sort - count
```

<img width="1261" height="292" alt="image" src="https://github.com/user-attachments/assets/25fe4bc5-5263-4707-a2e0-07a5626f4be9" />

<br>
<br>

```bash
index=win User_Account_Name=david.chen
|  table _time, EventCode, cs_method, User_Account_Name, Client_IP_Address
|  sort by +_time
```

<img width="1265" height="476" alt="image" src="https://github.com/user-attachments/assets/4952104b-7ffc-4b9a-9d41-4eefc03350b9" />

<br>
<br>

```bash
index=win User_Account_Name=david.chen
|  table _time, EventCode, cs_method, User_Account_Name, Client_IP_Address
|  sort by +_time
```

<img width="1270" height="481" alt="image" src="https://github.com/user-attachments/assets/8b8506ea-dc4b-4527-a2a7-6e4e346ab245" />

<br>
<br>

```bash
index=win EventCode IN (4624,4625,6273,6272) "*david.chen*"
|  table _time, EventCode, host, Client_IP_Address, user, User_Account_Name
|  sort by +_time
```

<img width="1262" height="318" alt="image" src="https://github.com/user-attachments/assets/c89980d9-dd1e-4834-9898-4ea45b99f1da" />

<br>
<br>

<br>
<h2>Task 8 &nbsp;・&nbsp; Investigation Challenge</h2> 
<h3>Scenario</h3>
<p>The SOC team received an alert about suspicious HTTP activity on one of the organization's IIS web servers. The alert was triggered by an unusual volume of HTTP 404 responses originating from a single external IP address.<br>

As part of the SOC team, you're tasked with reconstructing what happened.</p>

<h3>Machine Access</h3>
<p>Before starting this machine, you can stop the first machine from Task 1 as it's no longer needed.<br>

To start the second machine, click the Start Machine button below. This is a separate investigation environment with its own Splunk instance and log data, independent from the walkthrough machine. Give it 4-5 minutes to launch, then access it here:<br>

https://.....reverse-proxy.cell-prod-eu-west-1b.vm.tryhackme.com<br>

Info: This machine uses the same indexes: index=iis for IIS access logs and index=win for Windows Security and Sysmon events. Remember to set the time picker to All time if your queries return no results.</p>

<h3>Your virtual environment has been set up</h3>
<p>All machine details can be found at the top of the page.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What is the filename of the web shell the attacker deployed?</em><br><a id='8.1'></a>
>> <code>error.aspx</code></strong><br>

```bash
index=iis cs_uri_stem="*aspnet_client/*"
| stats count by c_ip, cs_uri_stem
| sort - count
```

<img width="1264" height="342" alt="image" src="https://github.com/user-attachments/assets/a1dce23d-08dd-44df-81b8-ae3d9e903b1a" />

<br>
<br>

> <em>What was the first reconnaissance command the attacker executed through the web shell?</em> Hint: Check process creation events<br><a id='8.2'></a>
>> <code>hostname</code></strong><br>

```bash
index=iis cs_uri_stem="*aspnet_client/*"
| table _time, EventCode, c_ip, cs_method, cs_uri_query, cmd, s_ip, s_port, sc_status
| sort +_time
```

<img width="1267" height="444" alt="image" src="https://github.com/user-attachments/assets/30b0c73f-69ab-4fa3-8c13-c20d7c3dded2" />

<br>
<br>

> <em>What URI path was used to upload the web shell to the server? (Answer Format: /path/file.ext)</em><br><a id='8.3'></a>
>> <code>/internalapp/upload.aspx</code></strong><br>


```bash
index=iis cs_method="POST" 
| table _time, EventCode, c_ip, cs_method, cs_uri_query, cs_uri_stem, s_ip, s_port, sc_status
| sort +_time
```

<img width="1271" height="324" alt="image" src="https://github.com/user-attachments/assets/1526196a-89e3-4c52-884a-60dc94fdedea" />

<br>
<br>

> <em>At what time was the web shell file created on the server? (Answer Format: HH:MM:SS)</em> Hint: Check Sysmon file creation events<br><a id='8.4'></a>
>> <code>david.chen2</code></strong><br>





