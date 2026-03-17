<h1 align="center"><a href="https://tryhackme.com/room/monitoringactivedirectory">Monitoring Active Directory</a></h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%204-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>
<p align="center"><img width="585px" src="https://github.com/user-attachments/assets/ae434338-1afa-4cfd-945d-6b67421bce4a"><br>It´s a premium medium-level walkthrough. Let's get started!</p>


<h2>Task 1 &nbsp;・&nbsp; Introduction</h2> 
<p>Every ransomware incident, every data breach, every domain compromise has one thing in common: interaction with Active Directory. AD is the identity backbone of most enterprise networks, making it a primary target for attackers.<br>
  
AD generates thousands of events per hour, including authentication requests, group changes, service tickets, and failed logins. Most of this activity is completely normal. So how do we find the malicious activity buried in all that noise?<br>

This room answers that question by teaching us to monitor AD from a defender's perspective. We'll learn what AD traffic looks like, what events get logged, how to configure logging for visibility, and how to find anomalies hiding in massive datasets.</p>
<h3>Learning Objectives</h3>
<p>By the end of this room, we'll be able to:<br>
  
- Identify the protocols that generate AD traffic and differentiate between domain and local user authentication<br>
- Interpret core AD Event IDs across authentication, account lifecycle, groups, and directory services<br>
- Establish baseline activity patterns and spot anomalies using stack counting<br>
- Configure audit policies to capture critical AD events<br>
- Query AD logs in Splunk to investigate user activity</p>

<h3>Prerequisites</h3>
<p>This room assumes foundational knowledge in:<br>
  
- Active Directory Basics: Core AD concepts like domains, users, groups, OUs, and how Kerberos/NTLM authentication works (Active Directory Basics room)
- Windows Event Logs: Event IDs like 4624, 4625, and how to read Security logs (Windows Event Logs room)
- SPL Querying: How to write search queries in Splunk (Splunk: Exploring SPL room)</p>

<h3>Machine Access</h3>
<p>Start the machine by clicking the Start Machine button below. Give the Splunk instance about 4–5 minutes to launch, then access it here:<br>

- https://LAB_WEB_URL.p.thmlabs.com</p>

<p><em>Answer the question below</em></p>

<p>1.1. Let´s begin<br>
<code>No answer needed</code></p>

<h2>Task 2 &nbsp;・&nbsp; AD Traffic and Logging</h2> 

<br>
<p><em>Answer the questions below</em></p>

<p>2.1. Read the above and click Check.<br>
<code>No answer needed</code></p>

<br>

```bash
index=* EventCode=4720
| table _time, SAM_Account_Name, Subject_Account_Name
```

<img width="1270" height="283" alt="image" src="https://github.com/user-attachments/assets/8307e640-6aa1-4139-8f04-d6371b99ea84" />

<br>
<br>

```bash
index=* EventCode=4624
| stats count by Logon_Type
| sort -count
```

<img width="1272" height="399" alt="image" src="https://github.com/user-attachments/assets/4506e197-e2ef-40d5-83c0-ffd8b685a628" />

<br>
<br>

```bash
index=* (EventCode=4728 OR EventCode=4732 OR EventCode=4756)
| table _time, Member_Account_Name, Group_Name, Subject_Account_Name
```

<img width="1275" height="293" alt="image" src="https://github.com/user-attachments/assets/56ee950c-0327-4177-b598-1b05669a194e" />

<br>
<br>

```bash
index=task2 (HeadObject OR GetObject) requestParameters.bucketName=secretbucket userIdentity.accountId=anonymous
| fillnull value=Success erroMessage
| timechart span=30s count by errorMessage
```

<img width="1342" height="630" alt="image" src="https://github.com/user-attachments/assets/9213d2bd-7c4c-44d5-bfbd-22c3e87c4cf1" />

<br>
<br>
<br>
<h2>Task 3 &nbsp;・&nbsp; Authentication Events</h2> 

<br>
<p><em>Answer the questions below</em></p>

<p>3.1. Which file stores domain user credentials on the domain controller?<br>
<code>NTDS.dit</code></p>

<p>3.2. A local user authenticates to a workstation. Will this generate any events on the Domain Controller? (Answer Format: Yea or Nay)<br>
<code>Nay</code></p>

<p>3.3. What Event ID is generated when a user requests a TGT?<br>
<code>4768</code></p>

<p>3.4. In win index in Splunk, how many unique accounts requested TGTs in the dataset across all time?<br>
<code>14</code></p>

<h2>Task 4 &nbsp;・&nbsp; Accounts, Groups and Resource Access Events</h2> 

<br>
<p><em>Answer the questions below</em></p>

<p>4.1. Which file stores domain user credentials on the domain controller?<br>
<code>Group_Name</code></p>

<p>4.2. A local user authenticates to a workstation. Will this generate any events on the Domain Controller? (Answer Format: Yea or Nay)<br>
<code>3</code></p>

<br>

```bash
index=* EventCode=4720
| table _time, SAM_Account_Name, Subject_Account_Name
```

<img width="1276" height="290" alt="image" src="https://github.com/user-attachments/assets/22197e06-54b0-4ee4-8bf7-03ed612b4e8d" />

<br>
<br>

```bash
index=* (EventCode=4728 OR EventCode=4732 OR EventCode=4756)
| table _time, Member_Account_Name, Group_Name, Subject_Account_Name
```

<img width="1274" height="285" alt="image" src="https://github.com/user-attachments/assets/09dfa88a-cb56-4e85-954d-2249c4607254" />

<br>
<br>

```bash
index=* EventCode=4624
| stats count by Logon_Type
| sort -count
```

<img width="1276" height="394" alt="image" src="https://github.com/user-attachments/assets/0372d211-fafa-4abb-959b-456d6bf16ce2" />

<br>
<br>
<br>
<h2>Task 5 &nbsp;・&nbsp; Understanding Baseline Activity</h2>
<br>
<p><em>Answer the questions below</em></p>

<p>5.1. What character suffix identifies computer accounts in AD?<br>
<code>$</code></p>

<p>5.2. Using Event ID 4769, what is the MOST frequently requested service?<br>
<code>THM-DC$</code></p>

<br>

```bash
index=* EventCode IN (4624, 4768, 4769)
| eval AccountType=if(like(Account_Name, "%$%"), "Computer Account", "User Account")
| stats count by AccountType, EventCode
| sort AccountType, -count
```

<img width="1277" height="443" alt="image" src="https://github.com/user-attachments/assets/d67c0d0b-60f6-4547-b647-88c3ed4855a7" />

<br>
<br>

```bash
index=* EventCode=4769 NOT Account_Name="*$*"
| stats count by Account_Name
| sort -count
```

<img width="1273" height="422" alt="image" src="https://github.com/user-attachments/assets/11e43769-d389-401c-8df6-52e16f8faa50" />

<br>
<br>

```bash
index=*
| stats count by Service_Name, EventCode
| sort -count
```

<img width="1278" height="598" alt="image" src="https://github.com/user-attachments/assets/90398484-2a6b-40ee-a9f6-2c98630aefe0" />

<br>
<br>
<br>
<h2>Task 6 &nbsp;・&nbsp; Audit Policy Configuration</h2> 
<br>
<p><em>Answer the question below</em></p>

<p>6.1. What command displays all current audit policy settings on a domain controller?<br>
<code>auditpol /get /category:*</code></p>


<h2>Task 7 &nbsp;・&nbsp; Scenario: New Employee Onboarding Audit</h2> 
<br>
<p><em>Answer the questions below</em></p>

<p>7.1. What is the name of the newly created account?<br>
<code>nathan.brooks</code></p>

<p>7.2. Who created this account?<br>
<code>adm-luke.sullivan</code></p>

<p>7.3. What group was this user added to?<br>
<code>Marketing</code></p>

<p>7.4.What was the source IP address of nathan.brooks's first TGT request?<br>
<code>10.5.50.12</code></p>

<br>

```bash
index=* EventCode=4720
```

<img width="1268" height="459" alt="image" src="https://github.com/user-attachments/assets/1eb70984-65b9-4d0a-bf41-8e417a84bb73" />

<br>
<br>

```bash
index=* EventCode=4728
```

<img width="1281" height="388" alt="image" src="https://github.com/user-attachments/assets/1e7d5de6-db0b-49d3-a24e-a03d24516c70" />

<br>
<br>

```bash
index=* EventCode=4768 Account_Name=nathan.brooks
```

<img width="1264" height="392" alt="image" src="https://github.com/user-attachments/assets/d7bc79af-fefe-4678-a432-e1219b4c86ee" />

<br>
<br>
<br>
<h2>Task 8 &nbsp;・&nbsp; Conclusion</h2> 
<p>We've now built the foundation for AD monitoring. We went through what protocols generate AD traffic, what events get logged, how to configure audit policies, and how to find anomalies using stack counting.</p>
<h3>Takeaways</h3>
<p>
  
- Kerberos, LDAP, SMB, and RDP generate most AD traffic, and understanding them helps us interpret events.<br>
- Authentication events appear on DCs, logon sessions appear on targets, and we need both.<br>
- Without proper configuration, many events aren't logged at all.<br>
- Thousands of events per day are expected. Use stack counting to find anomalies.<br>
- Individual events are data, but correlated sequences reveal what actually happened.</p>

<p><em>Answer the question below</em></p>

<p>8.1. Click Check to finish this room.<br>
<code>No answer needed</code></p>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/b8471cb1-3af5-4eff-bb21-e646f0df48c6"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/48311784-6abe-41c6-847a-48d4cd7a34e8"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/d97a8db0-0a88-45e1-aace-70a97c480d98"></p>

            
<h1 align="center">My TryHackMe Journey ・ 2026, March<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Room Name<br><br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|League<br><br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|---------------:|
|4<br><br>       |62<br><br>        |Monitoring Active Directory<br>  |Medium<br><br> |🔗<br><br>| 1,136<br><br>| 157,396<br><br>| 90<br><br>| 22ⁿᵈ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
|3<br><br>       |61<br><br>        |Monitoring AWS Services<br>      |Medium<br><br> |🔗<br><br>| 1,135<br><br>|        <br><br>| 90<br><br>| 22ⁿᵈ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|<br><br>|
|2<br><br>       |60<br><br>        |<br><br>                         |      <br><br> |  <br><br>|      <br><br>|        <br><br>|   <br><br>|     <br><br>|    <br><br>|    <br><br>|    <br><br>|<br><br>|
|1<br><br>       |59<br><br>        |<br><br>                         |      <br><br> |  <br><br>|      <br><br>|        <br><br>|   <br><br>|     <br><br>|    <br><br>|    <br><br>|    <br><br>|<br><br>|


</h6></div><br>


<h1 align="center">My TryHackMe Journey ・ 2026, March</h1>
<p align="center">Global All Time:      22ⁿᵈ<br><img width="250px" src="https://github.com/user-attachments/assets/b38ede9d-b29e-4ee9-aeb5-76897f9ff1b3"><br>
                                               <img width="1200px" src="https://github.com/user-attachments/assets/9bc50fda-7a84-45c3-99b5-e1631587851e"><br><br>
                  Global Monthly:       10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6cfabd6e-4c20-489d-ac90-df91ed604fb6"><br><br>
                  Brazil All Time:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/dc3846e6-a10b-4c77-9f48-b873c7b01edb"><br><br>
                  Brazil Monthly:        1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/9bdebaa5-26eb-465f-954f-a68835b13c77"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
