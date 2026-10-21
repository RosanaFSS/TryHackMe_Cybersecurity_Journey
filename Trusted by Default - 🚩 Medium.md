<h1 align="left">Security Operations &nbsp; · &nbsp; Splunk &nbsp; · &nbsp; Trusted by Default</h1>
<p align="left"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20OCT%2021-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<br>

<p><em>Answer the questions below</em></p>

<p>Review the web logs for the unusual POST request associated with the start of the incident. What URI path was requested? Submit the complete path beginning with a forward slash.?<br>
<code>/portal/status.aspx</code></p>

```splunk
index=* POST
|  table _time, host, source, src, src_port, dest, dest_port, uri, sc_bytes
|  sort by +_time
```

<img width="1345" height="488" alt="image" src="https://github.com/user-attachments/assets/0d6c4866-9a52-444d-9daf-826929b6a2d1" />

<br>
<br>
<p>Inspect the same suspicious POST event and examine the client details recorded with it. Which source IP submitted the request? Submit the IP address only.<br>
<code>10.81.73.36</code></p></p>

<br>
<p>Correlate the suspicious web request with Windows logons on AUR-WEB01. Which non-system account received a batch logon shortly before the request?<br>
<code>svc-webapp</code></p>

<img width="1303" height="551" alt="image" src="https://github.com/user-attachments/assets/846613c7-6fe7-4470-9fec-68da9ad4dd3f" />

<br>
<br>

```splunk
index=* SubjectUserName="svc-webapp"
```

<img width="1336" height="577" alt="image" src="https://github.com/user-attachments/assets/07587171-d898-453d-ae6e-896f0dfb6eed" />

<br>
<br>
<p>What Windows logon type was recorded for that batch logon?<br>
<code>4</code></p>

```splunk
index=* EventCode=4624 TargetUserName=svc-webapp SubjectUserName!="-"
|  table _time, EventCode, host, TargetUserName, SubjectUserName, LogonType
|  sort by -_time
```

<img width="1334" height="564" alt="image" src="https://github.com/user-attachments/assets/1f0bf610-b8a9-493d-b4bf-66b8a8e212b8" />

<br>
<br>
<p>After the web-server activity, review Windows group-membership changes involving the Portal Application Service account. Which privileged group was modified? Submit the group name exactly as recorded.<br>
<code>a.ng</code></p>

```splunk
index=* EventCode IN (4735, 4737, 4750, 4755, 4760, 4784)
| table _time, host, TargetUserName, SubjectUserName, TargetDomainName, EventCode
| sort by +_time
```

<img width="1335" height="425" alt="image" src="https://github.com/user-attachments/assets/9740ecc7-f38b-4bd6-876e-fcc208e9ed3e" />

<br>
<br>

```splunk
index=*  SourceIp="10.81.73.36"  DestinationPort=3389
|  stats count by DestinationIp
```

<img width="1317" height="407" alt="image" src="https://github.com/user-attachments/assets/7898dc83-03d1-46ac-9440-7a0e0a176591" />

<br>
<br>
<p>Inspect the same group-membership event. Which user performed the change? Submit the username only.<br>
<code>10</code></p>

```splunk
index=* EventCode=4624 TargetUserName=svc-webapp SubjectUserName!="-"
|  table _time, EventCode, host, TargetUserName, SubjectUserName, LogonType
|  sort by -_time
```

<img width="1334" height="564" alt="image" src="https://github.com/user-attachments/assets/d36129df-2fdb-443e-b54a-a4c890fea1ad" />

<br>
<br>
<p>Continue into successful logon events on the file server during the short window after the group change. Which non-built-in account generated both network and remote-interactive logon types? Submit the account name only.<br>
<code>svc-webapp</code></p></p>

```splunk
index=* EventCode=4624 LogonType=10
| table _time, EventCode, host, TargetUserName, SubjectUserName, TargetDomainName
| sort by +_time
```

<img width="1307" height="428" alt="image" src="https://github.com/user-attachments/assets/786ec833-c544-41ce-8a18-dcd08e16e559" />

<br>
<br>
<p>Inspect the successful logons for that account. Which numeric LogonType identifies the remote-interactive session? Submit the number only.<br>
<code>10</code></p></p>

<br>

<p>Use the source IP from the suspicious POST as the source-side pivot and correlate RDP activity in the short incident window. Which destination IP is associated with the sustained connection rather than the immediately reset attempts? Submit the IP address only.<br>
<code>10.81.112.251</code></p></p>

```splunk
index=* SourceIp="10.81.73.36" DestinationPort=3389
|  stats count by DestinationIp
|  sort -count
```

<img width="1335" height="387" alt="image" src="https://github.com/user-attachments/assets/57b54a38-a096-46e3-936e-13b552293234" />

<br>
<br>
<p>Inspect the sustained RDP connection identified in the previous step. What resp_bytes value records the data returned by the destination? Submit digits only.<br>
<code>181717</code></p></p>

```splunk
index=* src="10.81.73.36" dest="10.81.112.251" 3389 resp_bytes!=0 resp_bytes!="-"
|  table _time, src, src_port, orig_bytes, dest, dest_port, resp_bytes
```

<img width="1334" height="331" alt="image" src="https://github.com/user-attachments/assets/1f5a75f8-0544-43d5-9d3c-af22662a0947" />


