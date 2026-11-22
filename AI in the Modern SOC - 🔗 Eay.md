<h1 align="left">AI in the Modern SOC</h1>

<p align="left">
  <img src="https://img.shields.io/static/v1?label=Category&message=SOC&color=24292e&style=flat-square&v=1" /> &nbsp;
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Level-Easy-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Completed-2026, Nov 22%20-darkgreen?style=flat-square" /> &nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white"  alt="LinkedIn"/></a> &nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white" height="30" alt="GitHub"/></a> &nbsp;
</p> 

<h3>Incident Scenario</h3>
<h4>Castellane Capital: Security Operations</h4>

<p>The finance team is closing its month-end work, and the shift is busy.<br><br>
A detection has now fired on finance analyst Owen Farrelly's laptop, <code>FIN-LT-0142</code>, after suspicious PowerShell activity, and it has been assigned to us.<br><br>
We have the alert, the affected host and a narrow time window, but we have not yet traced the surrounding process and network events.<br><br>
An automated triage workflow has collected some context and prepared a Case note for us.<br><br>
It may have saved several searches, but no analyst has checked its important observation against the original event.<br><br>
Please investigate the alert, compare the findings with the prepared note and record what the evidence supports.<br><br>
If anything important remains unresolved, leave Tier 2 a handover they can continue without repeating our work.</p>
<br>
<br>

<img width="1909" height="215" alt="image" src="https://github.com/user-attachments/assets/103361eb-2d05-48c8-b75b-522b1d89a328" />

<br>
<br>
<p><em>Answer the questions below</em></p>

<br>
<p>Open the alert for FIN-LT-0142 in Elastic Security. What is the exact name of the detection rule that fired?<br>
<code>Encoded PowerShell started by Windows Script Host</code></p>

<img width="1908" height="673" alt="image" src="https://github.com/user-attachments/assets/b64dcbd0-3707-4032-a498-d47e666085e9" />

<br>
<br>

<img width="1904" height="623" alt="image" src="https://github.com/user-attachments/assets/bfdae08a-18a0-4440-9779-642498debb36" />


<br>
<br>
<p>Using Timeline, open the alert's powershell.exe event. What numeric value does process.parent.pid record for its parent process?<br>
<code>6064</code></p>

<img width="1907" height="789" alt="image" src="https://github.com/user-attachments/assets/c9714c01-05a1-4287-a3a0-37dc1a199ab8" />

<br>
<br>
<p>Using the ES|QL query in Discover, find the network event made by curl.exe. What destination IP address does it connect to?<br>
<code>10.40.20.77</code></p>

<br>
<p>Compare the two process-start events in Timeline. How many whole seconds elapsed between wscript.exe starting and powershell.exe starting?<br>
<code>12</code>

<p>
- Aug 7, 2026 @ 07:42:31.000<br>
- Aug 7, 2026 @ 07:42:43.000</p>

<br>
<p>What is the process.parent.entity_id value recorded on the powershell.exe source event?<br>
<code>e65ceea-0b45-5362-824c-12abe5e33edf</code></p>
  
<br>
<br>

<p>In the labelled AI-prepared Case note, what run ID is recorded for this workflow run?<br>
<code>-----------------------</code></p>

<img width="1902" height="680" alt="image" src="https://github.com/user-attachments/assets/e00ace5f-5d13-4357-be30-1ba335176290" />

<br>
<br>
<p>Reopen the document cited by the AI-prepared Case note. What value is shown in winlog.record_id for that native event?<br>
<code>321</code></p>

<img width="1901" height="359" alt="image" src="https://github.com/user-attachments/assets/ea1fb55f-1c2a-4fad-a25f-75f7bd9b9fc0" />

<br>
<br>

<img width="1905" height="325" alt="image" src="https://github.com/user-attachments/assets/77510cfe-cd88-49f3-bc54-43de567a6fd0" />


<br>
<br>

<img width="1912" height="808" alt="image" src="https://github.com/user-attachments/assets/11650232-9963-4615-9730-98835581adf9" />

<br>
<br>
<p>Open the ... menu at the top right of the Case and choose Copy case ID. What Case UUID is copied?<br>
<code>699---------------------------------</code></p>

<img width="1891" height="386" alt="image" src="https://github.com/user-attachments/assets/2e54a1db-d333-482a-847d-a0d53cd000e0" />

<br>
<br>
<p>Which verdict do the cited event's native fields support for the prepared observation: Supported, Incomplete or Not Supported?<br>
<code>---------</code></p>

<br>
<p>Our handover names the outbound destination returned by ES|QL in Task 4. Which destination port did curl.exe connect to?<br>
<code>443</code></p>

<br>
<p>After marking the Case for Tier 2 review, who still owns the conclusion?<br><code>analyst</code></p>

<br>
<br>
<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/ec92f43d-8862-4523-9a8a-3c29a65b23ee"><br>
                  <img width="300px" src="https://github.com/user-attachments/assets/dbd0b200-e8ba-4b97-b067-188d93bd0965"></p>

