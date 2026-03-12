<h1 align="center"><a href="https://tryhackme.com/room/entraidmonitoring">Entra ID Monitoring</a></h1>
<p align="center"><img width="1200px" src=""><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2012-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<h2>Task 1 &nbsp;・&nbsp; Introduction</h2> 
<p>Identity-based attacks are now the dominant initial access path in cloud environments. <a href="https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2023#section-master-ocb08f">According to Microsoft´s</a> own telemetry, over 99% of account compromise attacks are preventable with basic controls like MFA, yet attackers continue to succeed because misconfigurations and policy gaps remain widespread.<br>

This room walks through the most common attack techniques targeting Entra ID identities: how they work, what they leave behind in logs, and how to hunt for them with logs.</p>

<h3>Learning Objectives</h3>
<p>By the end of this room, you will be able to:<br>

- Understand common attack techniques targeting Entra ID identities.<br>
- Understand how Entra ID security features can help prevent or detect these attacks.<br>
- Learn how to use Sign-in and Audit logs to detect each technique.</p>

<h3>Prerequisites</h3>
<p>
  
- <a href="https://tryhackme.com/room/m365monitoringbasics">M365 Monitoring Basics</a><br>
- <a href="https://tryhackme.com/room/splunkexploringspl">Splunk: Exploring SPL</a><br>
- <a href="https://tryhackme.com/room/introtologanalysis">Intro to Log Analysis</a></p>

<h3>Lab Access</h3>
<p>Start the lab by clicking the Start Machine button below. You will then have access to the Splunk Web Interface. Please wait 4-5 minutes for the Splunk instance to launch.<br>
To access Splunk, please wait for the VM to start and follow this link:<br>

- https://LAB_WEB_URL.p.thmlabs.com<br>

Please wait 4-5 minutes for the Splunk instance to launch. Ensure to use Splunk’s All Time range for every search.<br>

Each task has its own index and log dataset in Splunk, so ensure you filter for the correct index with the task number to answer the questions properly.<br>
For example, use index=task-2 to answer questions for task 2.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> <em>Ready to learn!</em><br><a id='1.1'></a>
>> <code>No answer needed</code></strong><br>

<br>
<h2>Task 2 &nbsp;・&nbsp; Password-Based Attacks</h2> 


> <em>Which IP address is performing a password spraying?</em> Hint: A good starting point is looking for all events with "status.errorCode!=0".<br><a id='2.1'></a>
>> <code>94.20.222.248</code></strong><br>

index="task-2" sourcetype="azure:aad:signin" "status.errorCode"!=0 conditionalAccessStatus!=success
| stats dc(userPrincipalName) as targeted_accounts, count as failures by ipAddress
| sort - failures

<img width="1340" height="375" alt="image" src="https://github.com/user-attachments/assets/09eabb7a-4578-420c-9a05-e8ed568256c1" />



index="task-2" sourcetype="azure:aad:signin" "status.errorCode"!=0 conditionalAccessStatus!=success
| table _time, action, location.city, src, reason, user
| sort +_time

<img width="1343" height="692" alt="image" src="https://github.com/user-attachments/assets/2abc7e97-122a-48f3-a94e-b76445328df4" />


index="task-2" sourcetype="azure:aad:signin" "status.errorCode"!=0 conditionalAccessStatus!=success
| stats count by src, user
| sort +src

<img width="1341" height="518" alt="image" src="https://github.com/user-attachments/assets/76ff152e-23ab-493c-8456-fc5b93c5b3cf" />


> <em>Which IP address is performing a throttling brute force?</em><br><a id='2.2'></a>
>> <code>38.165.231.218</code></strong><br>

index="task-2" sourcetype="azure:aad:signin" "status.errorCode"!=0 conditionalAccessStatus!=success
| timechart count by ipAddress


<img width="1340" height="682" alt="image" src="https://github.com/user-attachments/assets/230c5a1d-ac8a-4371-b59c-85c6dda5875d" />


<br>

> <em>What is the user's email address that was compromised?</em> Hint: Legitimate user can miss their password by mistake! Not every login failure means a brute-force attack!<br><a id='2.3'></a>
>> <code>amanda.costa@finegalo.thm</code></strong><br>

index="task-2" sourcetype="azure:aad:signin" "status.errorCode"!=0 conditionalAccessStatus=success
| timechart count by ipAddress

<img width="1335" height="673" alt="image" src="https://github.com/user-attachments/assets/b5233f32-7c1e-4141-9af4-aa43b28a97ed" />

<br>
<br>

<p>

- Click over the suspicious IP bar (green).</p>

<img width="1337" height="544" alt="image" src="https://github.com/user-attachments/assets/a8e65507-4ba0-4c86-b8f5-3d81f9807808" />

<br>
<br>

<br>
<h2>Task 3 &nbsp;・&nbsp; Conditional Access Policies & Identity Protection</h2> 


> <em>What is the user email address that is at risk in the tenant?</em><br><a id='3.1'></a>
>> <code>allan.senna@finegalo.thm</code></strong><br>

index="task-3" sourcetype="azure:aad:identity_protection:risky_user"
| table _time, userPrincipalName, riskLevel, riskState, riskDetail 
| sort - _time

<img width="1337" height="297" alt="image" src="https://github.com/user-attachments/assets/f8b2a658-3b95-4766-aa9f-438bf536b86f" />

<br>
<br>

> <em>When was the last risky sign-in attempt from this risky user based on risk detection logs?Answer Example: 2026-01-01 14:00</em><br><a id='3.2'></a>
>> <code>2026-03-03 13:51</code></strong><br>

index="task-3" sourcetype="azure:aad:identity_protection:riskdetection"
| table _time, userPrincipalName, riskLevel, riskState, riskDetail 
| sort +_time

<img width="1282" height="374" alt="image" src="https://github.com/user-attachments/assets/fc999717-cd6b-41e5-8069-10edd2871c48" />

<br>
<br>

> <em>What is the type of risk identified during this risky user sign-in based on risk detection logs?</em><br><a id='3.3'></a>
>> <code>anonymizedIPAddress</code></strong><br>

<img width="1288" height="651" alt="image" src="https://github.com/user-attachments/assets/e499ffe0-a7f8-43e3-8a8a-98ae5cb7d911" />

<br>
<br>

> <em>What is the name of the CAP policy that was enforced and blocked some sign-in attempts from this risky user?</em><br><a id='3.4'></a>
>> <code>Block Suspicious Countries</code></strong><br>


index="task-3" sourcetype="azure:aad:signin" "status.errorCode"!=0 conditionalAccessStatus!=success  ipAddress="94.20.222.251"
|  table _time src user status.failureReason appliedConditionalAccessPolicies{}.displayName appliedConditionalAccessPolicies{}.enforcedGrantControls{}
|  sort by +_time


<img width="1302" height="638" alt="image" src="https://github.com/user-attachments/assets/e1b253ba-9ab3-4694-b0d2-3404a657686f" />

<br>
<br>

> <em>What was the IP address that was blocked from signing in this risky user?</em><br><a id='3.5'></a>
>> <code>94.20.222.251</code></strong><br>

sourcetype="azure:aad:signin" "status.errorCode"!=0 conditionalAccessStatus!=success | timechart count by ipAddress

<img width="1311" height="457" alt="image" src="https://github.com/user-attachments/assets/6e2b32a6-649c-4a7f-96a1-47d2c78d4b30" />

<br>
<br>

<br>
<h2>Task 4 &nbsp;・&nbsp; MFA Bypass Techniques</h2> 


<br>
<br>

> <em>Which user was the target of an MFA fatigue attack?</em> Hint: A good starting point is listing conditional access policies failures.<br><a id='4.1.'></a>
>> <code>igor.bicalho@finegalo.thm</code></strong><br>

index="task-4" sourcetype="azure:aad:signin" (status.errorCode=50074 OR status.errorCode=50076 OR status.errorCode=500121)
| stats count as mfa_failures values(status.errorCode) as errorCodes values(status.failureReason) as failureReasons by userPrincipalName, ipAddress
| sort - mfa_failures


<img width="1304" height="296" alt="image" src="https://github.com/user-attachments/assets/6a7fb211-d48b-4247-a5b2-c7a7138e9991" />

<br>
<br>

> <em>What is the error code of the failed MFA prompts?</em> Hint: Take a look in the "location" field.<br><a id='4.2.'></a>
>> <code>500121</code></strong><br>

<br>

> <em>What is the country code (e.g., UK, MX) that the user normally signs in before the attack?</em><br><a id='4.3.'></a>
>> <code>DK</code></strong><br>

index="task-4" sourcetype="azure:aad:signin" status.errorCode=0

<img width="1306" height="445" alt="image" src="https://github.com/user-attachments/assets/d957ba11-9b8b-47c8-aaad-944b3590ff46" />

<br>
<br>

> <em>When does the attacker successfully authenticate in the user account? Answer Example: 2026-01-01 15:20</em><br><a id='4.4.'></a>
>> <code>2026-03-04 13:26</code></strong><br>

index="task-4" sourcetype="azure:aad:signin" status.errorCode=0
| table _time, userPrincipalName, activity, ipAddress, location.countryOrRegion
| sort +_time

<img width="1297" height="444" alt="image" src="https://github.com/user-attachments/assets/669802a6-90c2-4c7a-9c8a-897b73c127c7" />


<br>
<h2>Task 5 &nbsp;・&nbsp; Privilege Escalation & Persistence</h2> 



<br>
<h2>Task 6 &nbsp;・&nbsp; OAuth Application Abuse</h2> 


<br>
<h2>Task 7 &nbsp;・&nbsp; Conclusion</h2> 

