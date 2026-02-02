<h1 align="center"><a href="https://tryhackme.com/room/awssecuritylogging">AWS Security Logging</a></h1>
<p align="center">Dive into various AWS log sources and learn how they can help your SOC team.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/d80a12aa-0342-4a8d-8fe1-7558533d7245"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20FEV%202-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<br><br>
<h2>Task 1 . Introduction<a id='1'></a></h2>
<p>Amazon Web Services (AWS) is one of the most used IaaS cloud providers, and many companies worldwide, including TryHackMe, heavily use its compute, storage, databases, networking, and ML services. This room explains the tools to monitor the AWS cloud environment for threats and provides best practices on auditing AWS activities in SIEM by the SOC.<br>

<strong>Tip</strong>: It is a good idea to create your own AWS account and test each service as you go through the tasks. While this room focuses on the SIEM perspective, seeing how things appear in the AWS console will help you better understand the material. AWS has a free tier that you can try by following <a href="https://aws.amazon.com/free"> the link</a>. Just be mindful of the costs going beyond the free tier.</p>

<h3>Learning Objectives</h3>
<p>

- Explore control plane, managed services, and workload security<br>
- Practice using CloudTrail and GuardDuty for threat detection<br>
- Learn about cloud log sources, such as CloudFront and S3 logs<br>
- Gain a broad overview of how to log and monitor AWS as a SOC</p>

<h3>Prerequisites</h3>
<p>

- Complete the <a href="https://tryhackme.com/room/cloudsecuritypitfalls"> Cloud Security Pitfalls</a> room<br>
- Complete the <a href="https://tryhackme.com/room/splunk101"> Splunk: The Basics</a>  room<br>
- Preferably, complete the <a href="https://tryhackme.com/module/introduction-to-aws">  Introduction to AWS</a> module<br>
- Preferably, complete the <a href="https://tryhackme.com/path/outline/soclevel1">  OC Level 1 Analyst</a> path</p>

<h3>Lab Access</h3>
<p>Start the lab by clicking the <strong>Start Machine</strong> button below. You will then have access to the Splunk Web Interface. Please wait 4-5 minutes for the Splunk instance to launch. To access Splunk, follow this link:<br>

- https://LAB_WEB_URL.p.thmlabs.com</p>

<h4>Set up your virtual environment</h4>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the question below</em></p>

<p>1.1. <em>Start the lab and continue to the next task!</em><br>
<code>No answer needed</code></p>


<br><br>
<h2>Task 2 . What to Secure in AWS<a id='2'></a></h2>
<br>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>Which security area covers management actions within the AWS console?</em><br>
<code>Control Plane</code></p>

<p>2.2. <em>Which of the mentioned AWS services provides virtual machines in the cloud?</em><br>
<code>Amazon EC2</code></p>

<br><br>
<h2>Task 3 . Covering AWS Control Plane<a id='3'></a></h2>
<h3>Meet CloudTrail</h3>
<br>

<h3>Log Format</h3>
<br>

<h3>Key CloudTrail Fields</h3>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>From which IP did <strong>jeff.harrison</strong> user log in to AWS?</em><br>
<code>149.40.62.48</code></p>

```bash
index=aws eventName=ConsoleLogin
| table _time eventSource eventName recipientAccountId sourceIPAddress userName aws_account_id
| sort by +_time
```

<img width="1321" height="416" alt="image" src="https://github.com/user-attachments/assets/fb532bb0-4037-455a-8e08-0278d838cd8b" />

<br>
<br>
<p>3.2. <em>To which AWS account ID did <strong>jeff.harrison</strong> user log in?</em><br>
<code>398985017225</code></p>


<p>3.3. <em>What S3 bucket did <strong>jeff.harrison</strong> create after the login? Note: You will need to change your Splunk query.</em> Hint: Look for other actions of Jeff or filter by "CreateBucket" eventName.<br>
<code>prod-website-thm</code></p>

```bash
index=aws eventName=CreateBucket
| table _time eventSource eventName recipientAccountId sourceIPAddress userName aws_account_id object
| sort by +_time
```

<img width="1319" height="319" alt="image" src="https://github.com/user-attachments/assets/490cbfed-9b22-44f3-be03-9787595098b5" />


<br><br>
<h2>Task 4 . CloudTrail and GuardDuty<a id='4'></a></h2>
<h3>CloudTrail Usage</h3>
<br>


<p><em>Answer the questions below</em></p>

<p>4.1. <em>Find the "AnomalousBehavior" GuardDuty alert in the logs. From which VPN did the suspicious activity originate?</em> Hint: You might need to expand JSON subkeys and dig deeper!<br>
<code>ProtonVPN</code></p>


```bash
index=aws index=aws sourcetype=aws:cloudwatch:guardduty Type="Discovery:IAMUser/AnomalousBehavior"
```

<img width="1296" height="310" alt="image" src="https://github.com/user-attachments/assets/c311b9d1-9f7a-4d9d-aace-fe1c699220e4" />

```bash	
| _time Type TitleService.Action.AwsApiCallAction.RemoteIpDetails.Organization.Isp
```

```bash	
| table _time eventName Type recipientAccountId sourceIPAddress userName aws_account_id object
| sort by +_time
```

```bash	
index=aws sourcetype=aws:cloudwatch:guardduty
```

<img width="1314" height="650" alt="image" src="https://github.com/user-attachments/assets/8d9040b2-781b-4a4f-ac4c-1ba86e2dde6d" />

<br>
<br>
<p>4.2. <em>Analyze two other alerts from the i-04fa0268276e1f763 EC2 instance. What is the path to the detected malware, and which domain did it query?</em> Hint: The answers can be hidden deep into the JSON subkeys.<br>
<code>/home/ubuntu/xmrig-6.24.0/xmrig, donate.v2.xmrig.com</code></p>

```bash	
index=aws sourcetype=aws:cloudwatch:guardduty "*bitco*"
```

<img width="1320" height="589" alt="image" src="https://github.com/user-attachments/assets/d35ba0f1-6f0a-424a-912f-4237b6b5358f" />

<br>
<br>
<p>4.3. <em>Continue to the CloudTrail logs to get more instance context. Who created the infected EC2 instance? Provide the full ARN field.</em> Hint: Filter for "RunInstances" event name or review all write events.<br>
<code>arn:aws:iam::398985017225:root</code></p>

```bash	
index=aws sourcetype=aws:cloudtrail action=created command=RunInstances
|  table _time sourceIPAddress userIdentity.arn
```

<br>
<br>
<p>4.4. <em>Which two risky ports did that user expose for the EC2 instance?Answer Example: 80, 443</em> Hint: The answer can be found in two "ModifySecurityGroupRules" events.<br>
<code>22, 3389</code></p>

```bash	
index=aws eventName=ModifySecurityGroupRules
|  table _time userName aws_account_id sourceIPAddress requestParameters.ModifySecurityGroupRulesRequest.SecurityGroupRule.SecurityGroupRule.ToPort
```

<img width="1366" height="323" alt="image" src="https://github.com/user-attachments/assets/0d0c69cd-bc2b-4233-b332-5e8f2fc241c8" />

<br><br>
<h2>Task 5 . Covering Managed Services<a id='5'></a></h2>
<br>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>Start with the CloudFront access logs. Which IP address logged in to the admin portal?</em> Hint: Look for the accessed web pages (cs_uri_stem field).<br>
<code>168.84.119.124</code></p>

```bash	
index=aws source="cloudfront.log"
```

<img width="1339" height="339" alt="image" src="https://github.com/user-attachments/assets/c4ccead1-fd9e-46f5-8282-c6ff450a0c58" />


<br>
<br>
<p>5.2. <em>Find an answer in the same CloudFront logs. How many IPs searched for the "tryhackme" keyword?</em> Hint: You might want to aggregate the logs by URI query.<br>
<code>14</code></p>

```bash	
index=aws source="cloudfront.log" "*admin*"
```

<img width="1364" height="613" alt="image" src="https://github.com/user-attachments/assets/60545c49-7856-4561-905c-1fc1167671f5" />

<br>
<br>
<p>5.3. <em>Now, move on to the S3 Data events. Which interesting S3 file has been accessed?</em><br>
<code>22, 3389</code></p>

```bash	
index=aws source="s3.json" command=GetObject
| table _time requestParameters.bucketName requestParameters.key
```

<img width="1365" height="338" alt="image" src="https://github.com/user-attachments/assets/111f4cb5-f7b0-4d6a-ada6-d9a22d8e6d99" />

<br><br>
<h2>Task 6 . Logging of AWS Workloads<a id='6'></a></h2>
<h3>Workloads and Services</h3>
<br>

<h3>Containerized Workloads</h3>
<br>

<p><em>Answer the questions below</em></p>

<p>6.1. <em>How would you call a service that is built and maintained by the cloud vendor?</em><br>
<code>Managed Service</code></p>

<p>6.2. <em>Which cloud workload monitoring tool was mentioned as an alternative to Auditd?</em><br>
<code>Falco</code></p>

<br><br>
<h2>Task 7 . Conclusion<a id='7'></a></h2>
<p>CloudTrail, CloudFront, CloudWatch, and many more - feels like a lot to learn, right? Don't worry, you will explore some of these services in much greater detail in the upcoming rooms. Think of this room as a general reference you can return to whenever you need a refresher. Hopefully, you enjoyed it!</p>

<h3>Note for Other Clouds</h3>
<p>The concepts explained throughout this room are applicable to most cloud providers. For example, AWS CloudTrail maps to Azure Activity Log in Microsoft Azure and to Cloud Audit Logs in Google Cloud. By understanding the fundamentals explained in this room, especially the three security areas, you will be able to switch between cloud platforms with ease after some practice.</p>

<p><em>Answer the question below</em></p>

<p>7.1. <em>Hope you enjoyed the room!</em><br>
<code>Managed Service</code></p>



Completed

<img width="1888" height="844" alt="image" src="https://github.com/user-attachments/assets/168b0f7c-bb91-4819-8e26-d9a6ec7f8ae0" />

<img width="719" height="193" alt="image" src="https://github.com/user-attachments/assets/76beb2a7-37b2-4721-882f-d6c5b118b052" />

<img width="1902" height="892" alt="image" src="https://github.com/user-attachments/assets/c70cf342-e978-47a1-a581-ea2988d3fd24" />


<br><br>
<h1 align="center">Completed</h1>

<p align="center"><img width="900px" src="https://github.com/user-attachments/assets/a6ad26e1-0c4e-4c69-b6b7-d4f89096efbf"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/5e4c37ce-4e32-4473-a486-177fa6a7e296"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/ec0b95e4-ba1e-43f2-baf2-33fac76c0041"></p>

            
<h1 align="center">My TryHackMe Journey ・ 2026, February<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Level<br><br><br>|Type<br><br><br>|Name<br><br><br>                         |Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Brazil<br>Monthly<br><br>|Brazil<br>All<br>Time|Global<br>Monthly<br><br>|Global<br>All<br>Time|
|:--------------:|:----------------:|:---------------:|:--------------:|:----------------------------------------|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|2<br><br>       |32<br><br>        |Medium<br><br>   |🔗<br><br>     |AWS Security Logging<br>                 |                    1,081<br><br>|       146,193<br><br>|               90<br><br>|                  22ⁿᵈ<br><br>|                     3ʳᵈ<br><br>|                 1,372ⁿᵈ<br><br>|             54ᵗʰ<br><br>|
|2<br><br>       |32<br><br>        |Medium<br><br>   |🔗<br><br>     |MS Entra ID: Authentication<br>          |                    1,081<br><br>|       146,081<br><br>|               90<br><br>|                  36ᵗʰ<br><br>|                     3ʳᵈ<br><br>|                 2,469ᵗʰ<br><br>|             54ᵗʰ<br><br>|     
|2<br><br>       |32<br><br>        |Easy<br><br>     |🔗<br><br>     |MS Entra ID: External ID<br>              |                    1,080<br><br>|       146,073<br><br>|               90<br><br>|                  35ᵗʰ<br><br>|                     3ʳᵈ<br><br>|                 2,403ʳᵈ<br><br>|             54ᵗʰ<br><br>|     

</h6></div><br>

<p align="center">
Global All Time: &nbsp; <strong>54</strong>ᵗʰ<br><img width="300px" src="https://github.com/user-attachments/assets/856a0215-017b-4be7-b2c9-abe62b9b79ea"><br>Brazil Monthly: &nbsp; <strong>22</strong>ⁿᵈ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
Brazil All Time: &nbsp; <strong>3</strong>ʳᵈ<br><img width="450px" hspace="20" src="https://github.com/user-attachments/assets/9df63d3f-0752-4b41-ac06-3e02b1d38643"><img width="450px" src="https://github.com/user-attachments/assets/8b3fdc2b-4878-4c13-b5f2-67a13804f821"><br><br>Global Monthly: &nbsp; <strong>1,372</strong>ⁿᵈ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
Global All Time: &nbsp; <strong>54</strong>ᵗʰ<br>
<img width="450px" hspace="20" src="https://github.com/user-attachments/assets/7c917f96-2b7a-4d68-bd10-17b6a6d14439">
<img width="450px" src="https://github.com/user-attachments/assets/91d37f3b-aae1-45f8-b246-b4d4ce4bb88e"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
