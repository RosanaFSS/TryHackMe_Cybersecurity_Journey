
```splunk
index=vantage marcus.webb
|  table _time, recipient, Operation, Workload, ClientIP, ObjectId, Params
|  sort by +_time
```

<p>3. What subject line does the attacker's inbox rule match on?<br>
<code>invoice</code></p>

```splunk
index=vantage Operation=New-InboxRule
|  table _time, ClientIP, Operation, ObjectId, Params
```

<p>

- 2026-08-27 12:30:10 - malicious inbox rule (New-InboxRule)</p>

<img width="1327" height="495" alt="image" src="https://github.com/user-attachments/assets/da0b4a15-7c32-40c4-bfd1-678dc9a75b4a" />

<br>
<br>
<br>
<p>4. How much time elapsed between the malicious inbox rule being created and a matching reply email arriving in the mailbox? (e.g. 2 minutes 51 seconds)<br>
<code>10 minutes 59 seconds</code></p>

```splunk
index=vantage recipient="marcus.webb*" invoice
|  table _time, recipient, subject
|  sort by -_time
```

<img width="1337" height="448" alt="image" src="https://github.com/user-attachments/assets/829915a5-9419-4ef8-9f73-104606e45b51" />

<p>

- 2026-08-27 12:30:10 - malicious inbox rule (New-InboxRule)<br>
- 2026-08-27 12:41:09 - reply email arrived</p>

<br>
<br>
<br>
<p>5. Marcus Webb's account logged a Teams message that had a link attached to it. What file did this link reference?<br>
<code>Meridian_Invoice_Batch_Aug2026.pdf</code></p>

```splunk
index=vantage marcus.webb ClientIP="185.220.101.47"  Operation=FileDownloaded
|  table _time, UserId, Operation, SourceFileName, ObjectId
```

<img width="1314" height="410" alt="image" src="https://github.com/user-attachments/assets/a9691342-04b2-4371-a2d9-c669dba5945e" />

<p>

- 2026-08-27 12:30:10 - malicious inbox rule (New-InboxRule)<br>
- 2026-08-27 12:41:09 - reply email arrived<br>
- 2026-08-27 12:33:55 - pdf downloaded</p>

<br>
<br>
<br>
<p>6. What operating system was used in the suspicious sign-in to David Chen's account?<br>
<code>Linux</code></p>

```splunk
index=vantage UserId="david.chen*" Operation=UserLoggedIn
|  stats count by UserId, OS
|  sort +count
```

<img width="1330" height="430" alt="image" src="https://github.com/user-attachments/assets/1de6381f-f5d2-4215-b309-3a129233bc72" />

<br>
<br>
<br>
<p>7. What IP address was used in this same sign-in?<br>
<code>91.219.237.88</code></p>

```splunk
index=vantage UserId="david.chen*" Operation=UserLoggedIn OS=Linux
|  stats count by UserId, ClientIP
|  sort +count
```

<img width="1328" height="398" alt="image" src="https://github.com/user-attachments/assets/89c0530a-3ef3-4502-a5c9-e4d97d009abf" />

<br>
<br>
<br>
<p>8. How much time passed between this message being created and the suspicious sign-in to David Chen's account? (e.g. 2 minutes 51 seconds)<br>
<code>91.219.237.88</code></p>

```splunk
index=vantage UserId="david.chen*" Operation=UserLoggedIn OS=Linux
|  table _time, UserId, ClientIP
|  sort +_time
```

<img width="1313" height="549" alt="image" src="https://github.com/user-attachments/assets/cca46f85-3853-45c3-903f-def72e315644" />

```splunk
index=vantage "Meridian_Invoice_Batch_Aug2026.pdf" | table _time, Operation, UserId | sort +_time
```

<img width="1297" height="537" alt="image" src="https://github.com/user-attachments/assets/07276a8a-0870-48d7-a9e7-294805433c60" />


<p>

- 2026-08-27 13:27:01 - login<br>
- 2026-08-27 13:28:31 - file downloaded<br>
- 2026-08-27 08:27:03 - file modified</p>



<br>
<br>
<br>
<p>9. The file the attacker downloaded from David Chen's account was legitimately modified earlier that day. At what time? (Format: YYYY-MM-DD HH:MM:SS)<br>
<code>2026-08-27 08:27:03</code></p>

```splunk
index=vantage UserId="david.chen*" Operation=FileDownloaded
|  table _time, UserId, ClientIP, ObjectId
|  sort +_time
```

<img width="1327" height="448" alt="image" src="https://github.com/user-attachments/assets/0f1069ee-ec7c-44fa-8ed2-4b121d19d8df" />

```splunk
index=vantage UserId="david.chen*" Operation=FileModified Q4_Board_Financial_Summary.xlsx
|  table _time, UserId, ClientIP, Operation, ObjectId
|  sort -_time
```

<img width="1326" height="432" alt="image" src="https://github.com/user-attachments/assets/d6767823-1df7-4938-9026-9cc2d3087f5b" />

<br>
<br>
<br>
<p>10. What file stored on the Leadership site had a sensitivity label applied to it by the organization's data governance, prior to the incident?<br>
<code>Q4_Board_Financial_Summary.xlsx</code></p>

```splunk
index=vantage UserId="david.chen*" ObjectId="*Leadership*" Operation=FileSensitivityLabelApplied
|  table _time, UserId, ClientIP, Operation, ObjectId
|  sort -_time
```

<img width="1311" height="398" alt="image" src="https://github.com/user-attachments/assets/e3a649fb-286c-4af8-8344-995cecd9e6e0" />

<br>
<br>
<br>
<p>11. What file did the attacker create an external sharing link for?<br>
<code>Vendor_Onboarding_Notes.docx</code></p>


```splunk
index=vantage  command=SharingLinkUpdated
|  table _time UserId, SourceFileName
```

<img width="1334" height="319" alt="image" src="https://github.com/user-attachments/assets/5db77954-c608-4c7c-80b8-cfda1aee029e" />

<br>
<br>
<br>
<p>12. What file did the attacker create an external sharing link for?<br>
<code>Vendor_Onboarding_Notes.docx</code></p>

