<h1 align="center"><a href="https://tryhackme.com/room/sharepointonlinemonitoring">SharePoint Online Monitoring</a></h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/221bea8d-2222-47f2-84f7-14e5f777920c"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2020-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<br>
<h2>Task 1 &nbsp;・&nbsp; Introduction</h2> 
<p>SharePoint Online is one of the most targeted M365 services, as it often stores sensitive files and can be used to propagate the attack. This room will explore the most common attack scenarios on SharePoint Online and explain how to monitor for them as a SOC team.</p>

<h3>Learning Objectives</h3>
<p>

- Learn Entra ID and SharePoint audit log formats<br>
- Explore how attackers exfiltrate data from SharePoint<br>
- Discover how SharePoint can become an attack tool<br>
- Practice the learned topics through an attack scenario</p>

<h3>Prerequisites</h3>
<p>

- <a href="https://tryhackme.com/room/m365monitoringbasics">M365 Monitoring Basics</a><br>
- <a href="https://tryhackme.com/room/entraidmonitoring">Entra ID Monitoring</a></p>

<h3>Lab Access</h3>
<p>Start the lab by clicking the Start Machine button below. You will then have access to the Splunk Web Interface. Please wait 4-5 minutes for the Splunk instance to launch. To access Splunk, follow this link:<br>

- https://LAB_WEB_URL.p.thmlabs.com</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<p><em>Answer the question below</em></p>
<br>
<p>1.1. Start the VM and let's go!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 &nbsp;・&nbsp; SharePoint Overview</h2> 
<h3>SharePoint Overview</h3>
<p>SharePoint Online is a service within the Microsoft 365 suite that lets you store, organize, share, and access corporate information through a web browser. It is widely used by organizations that use the Microsoft stack to keep team documentation and collaborate on documents, spreadsheets, and presentations. It is basically a business version of Google Drive and Microsoft OneDrive:<br>

- <strong>Google Drive</strong>: A cloud service to store and collaborate on files through the web<br>
- <strong>Microsoft OneDrive</strong>: Microsoft's analogue of Google Drive, built for personal files<br>
- <strong>Microsoft SharePoint</strong>: A more powerful version of OneDrive for corporate use</p>

<h6 align="center"><img width="850px" src="https://github.com/user-attachments/assets/6fc86dba-d6c9-463b-ae6c-5a4ef73c2e50"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>For future reference, SharePoint organizes data into top-level containers called <strong>sites</strong>, where each site is tied to an email group (e.g. <strong>sales@tryhackme.thm</strong>) and contains files, folders, or web pages. Also, note that there is an on-premises version of SharePoint. It is rarely used and relies on Active Directory authentication. This room will only explain SharePoint Online, a cloud-based service.</p>

<h3>SharePoint and M365</h3>
<p>SharePoint is deeply integrated into the Microsoft 365 suite. For example, authentication to SharePoint is performed via an Entra ID login, so if an adversary breaches a corporate Microsoft account with the right permissions, they automatically get access to all the SharePoint files the victim has access to. Fortunately, you can always audit SharePoint logins in the Entra ID console:</p>

<h6 align="center"><img width="850px" src="https://github.com/user-attachments/assets/e098918d-9000-43f5-b642-27157e8b2527"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>SharePoint Risks</h3>
<p>

- IT sites may contain network diagrams, application source code, or even keys<br>
- Finance sites may contain internal reports and confidential documents<br>
- Sales sites typically contain big spreadsheets of partners and customers<br>
- In short, SharePoint is one of the most important M365 services to monitor</p>
<p><em>Answer the questions below</em></p>
<br>
<p>2.1. Which of the mentioned Microsoft services is like SharePoint, but for personal use?<br>
<code>OneDrive</code></p>

<br>
<p>2.2. How do you call the SharePoint top-level container that holds objects, such as files?<br>
<code>site</code></p>

<br>
<h2>Task 3 &nbsp;・&nbsp; SharePoint Logging</h2> 
<h3>SharePoint Sign-In Logs</h3>
<p>Same as with other M365 services, you need to combine Entra ID and M365 logs to monitor SharePoint properly. Entra ID sign-in logs show authentication attempts to SharePoint, and M365 unified audit logs show file operations: access, modification, and sharing. Let's start with the sign-in logs. Below is a chain of sign-in events you will see during a legitimate SharePoint access of Emily Turner:</p>

<h6 align="center"><img width="850px" src="https://github.com/user-attachments/assets/0fcffe2b-2a22-4605-aba5-32b1eb502dca"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The first two events from the image indicate that Emily logged in to the M365 home portal (<strong>m365.cloud.microsoft</strong>). From there, she accessed the corporate SharePoint portal. The last event, login to Office365 Shell WCSS-Client, occurs automatically whenever a user navigates in M365 apps. If you want to monitor SharePoint logins, focus on sign-in events <strong>#3</strong> and <strong>#4</strong>. Also, please remember that logins from IPv6 can still be malicious. Never assume that IPv6 equals False Positive!</p>

<h3>SharePoint File Operations</h3>
<p>After signing in, Emily will interact with the site. You would see all her activities in M365 audit logs, with the Workload field always set to SharePoint. Let's see the simplest example, access to the Contract Templates document through SharePoint:</p>

```bash
{
  "CreationTime": "2026-01-29T15:08:32",
  "OrganizationId": "755c8cb5-4ddf-4c5e-[...]", // MS365 tenant ID
  "Operation": "FileAccessed",                  // Event name (action)
  "Workload": "SharePoint",                     // Target service
  "UserId": "emily.turner@tryhackme.thm",       // Source user email
  "AuthenticationType": "OAuth",
  "Site": "66c03890-ed18-42b3-[...]",           // SharePoint site ID
  "UserAgent": "MSWAC",                         // Internal SharePoint user-agent
  "ClientIP": "20.54.165.63",                   // IP of M365 server, not Emily's!
  "DeviceDisplayName": "20.54.165.63",          // Again, this is not Emily's IP!
  "SourceRelativeUrl": "Shared Documents",      // Folder of the file
  "SourceFileName": "Contract Template.docx",   // Accessed file name
  "SourceFileExtension": "docx",
  "ApplicationDisplayName": "WebWord",
  "SiteUrl": "https://tryhackme.sharepoint.com/sites/thm-sales/",
  "ObjectId": "https://tryhackme.sharepoint.com/sites/thm-sales/Shared Documents/Contract Template.docx"
}
```

<p>The event below follows a similar M365 log structure, where Workload, Operation, and UserId fields are always present, and other fields depend on the event. Note that you shouldn't blindly trust IPs and user agents in the logs, as they often refer to SharePoint servers rather than the actual clients. Overall, you should focus on the file operations below (Documentation(opens in new tab)):<br>

- <code>FileCreated</code>/<code>FileUploaded</code>: Useful to track suspicious file uploads
- <code>FileDeleted</code>/<code>FileRecycled</code>: Essential for audit and compliance purposes
- <code>FileAccessed</code>/<code>FileDownloaded</code>: Helpful for many types of cyber incidents</p>

<h3>File Sharing in SharePoint</h3>
<p>Another important monitoring aspect is file sharing. Microsoft reports both when sharing settings were changed and whenever a sharing link was used. That's great since file sharing can be abused in various scenarios that you will learn in the next tasks. Let's assume Emily shared a sensitive file with an external, untrusted email. You can start the hunt as:</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/1c15f03f-6bb1-4a84-9502-5eee2021f2e5"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>If there is a match, you will see which file was shared (ObjectId) and with whom (TargetUserOrGroupName). Note that it's only valid for external sharing. For internal sharing, better hunt for the SharingSet events and refer to the documentation(opens in new tab) for technical details. Next, you might want to check if the target user has already accessed the link, or if you have time to revoke the sharing before it's too late:</p>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ffc80502-3d70-46ab-a8b3-a6ce6672d08c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In Splunk, you can analyze both events in a single timeline. Below is an example showing how Emily shared a sensitive file with an external user (AddedToSecureLink), and how the user accessed the file a minute later (SecureLinkUsed). In most cases, these events are also followed by a FileAccessed event.</p>

<h6 align="center"><img width="850px" src="https://github.com/user-attachments/assets/ba1b64cb-8ee4-4cca-9588-f8c8b8048d03"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ba27d1bf-8a03-4b59-a6f5-f67b9d0f617c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>
<br>
<p>3.1. Refer to the Entra ID sign-in logs (<strong>azure:aad:signin</strong>). What is the event ID that confirms Emily's login to SharePoint? Hint: Find the right event in Entra ID logs and paste its "id" field.<br>
<code>22192ff2-272a-458c-8fac-7155db417700</code></p>

```bash
index=practice sourcetype="azure:aad:signin" appDisplayName="Office 365 SharePoint Online"
```

<img width="1902" height="666" alt="image" src="https://github.com/user-attachments/assets/8d31222e-b516-443f-8a12-d8d7e12736c0" />

<br>
<br>
<p>3.2. Move on to the SharePoint logs (<strong>o365:management:activity</strong>). What PDF file did Emily upload to the SharePoint?<br>
<code>Instructions.pdf</code></p>

```bash
index=practice UserId=emily.turner@tryhackme.thm Workload=SharePoint Operation IN(FileCreated, FileUploaded)
```

<img width="1311" height="506" alt="image" src="https://github.com/user-attachments/assets/46509c23-7672-4246-a199-45b0744ca516" />

<br>
<br>
<br>
<p>3.3. Soon after, Emily shared the PDF with an external user. What is the email of the target user?<br>
<code>ahmad.khan@opendoor.thm   </code></p>

```bash
index=practice Workload=SharePoint Operation IN(SecureLinkUsed, AnonymousLinkUsed)
```

<img width="1310" height="511" alt="image" src="https://github.com/user-attachments/assets/2d115814-0ad8-4e15-b4dc-a746bf239c71" />


<br>
<br>
<h2>Task 4 &nbsp;・&nbsp; Detecting Data Exfiltration</h2> 
<h3>SharePoint Data Access</h3>

<p>SharePoint is one of the primary targets for threat actors. After an account is compromised, the adversary may explore the contents of their SharePoint and exfiltrate files of interest, such as contracts, reports, internal wiki pages, or source code. Depending on the type and size of data, the adversary may:<br>

- Open the file in the browser and read it without downloading. Generates the <strong>FileAccessed</strong> event for every file.<br>
- Download the needed file or folder. Generates a <strong>FileDownloaded</strong> or similar event for every downloaded file.<br>
- Share the file with anyone and access it anonymously via a link. Still generates share events and <strong>FileAccessed</strong>.<br>

<h3>Data Exfiltration via GUI</h3>
<p>The simplest way to view SharePoint data is through the M365 portal. Like legitimate users, attackers can browse folders, open files, and download sensitive data. Unfortunately, if attackers act cautiously, their activity is hard to distinguish from normal SharePoint usage. Still, you can alert on a spike in <strong>FileDownloaded</strong>strong> events, since downloading a folder generates one event per file inside. The search below shows how a single <strong>Reports-2025</strong>strong> folder download resulted in five events:</p>

<h6 align="center"><img width="850px" src="https://github.com/user-attachments/assets/9ec4940c-b0a2-4231-8c69-a20e03aedefe"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Data Exfiltration via App</h3>
<p>The M365 portal does not allow full site export and does not support advanced search. Therefore, if attackers want to dump gigabytes of data, they must resort to external tools. Examples include the OneDrive app, the Rclone CLI utility, and many more paid solutions that allow you to sync SharePoint content with your local PC or another cloud location. For Rclone, the data export will look like this:</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/5dd91b99-04ec-45ff-9461-addc80c1ece0"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Regular users rarely use external applications to interact with SharePoint, especially CLI tools like Rclone. Thus, you can start by alerting on new applications on a per-user basis. To do this, focus on the ApplicationDisplayName and UserAgent fields, which are present in all file-related records. Below are the logs generated when running the Rclone commands shown in the illustration above:</p>

<h6 align="center"><img width="850px" src="https://github.com/user-attachments/assets/0a3a0afb-0fd4-48f1-9135-78f72dfe3eb9"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d5101c68-4212-4e6b-8daa-352e7a649058"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>
<br>
<p>4.1. Which M365 event is generated every time the file is downloaded?<br>
<code>FileDownloaded</code></p>

```bash
index=*  Operation=FileDownloaded
| stats count values(SourceFileName) by SiteUrl, SourceRelativeUrl UserId
```

<img width="1271" height="387" alt="image" src="https://github.com/user-attachments/assets/afd31c95-d30c-415d-aa7c-caa7a4f277ed" />

<br>
<br>
<br>
<p>4.2. Which M365 field can you use to identify the application behind the event?<br>
<code>ApplicationDisplayName</code></p>

```bash
index=*  Operation=FileDownloaded
| stats count values(SourceFileName) by SiteUrl, SourceRelativeUrl UserId, ApplicationDisplayName
```

<img width="1283" height="386" alt="image" src="https://github.com/user-attachments/assets/a30f414a-25f7-458f-b6cb-dfad2a3847ca" />

<br>
<br>
<h2>Task 5 &nbsp;・&nbsp; Detecting SharedPoint Abuse</h2> 
<h3>SharePoint as an Attack Tool</h3>
<p>Imagine you are an attacker who has compromised the account of a B2B Sales Lead. You discover a CSV file containing hundreds of partner email addresses, including contacts from large, well-known companies. How can this be abused? You could launch a phishing campaign on all addresses while impersonating the Sales Lead. And to bypass anti-phishing controls, you can send the emails via SharePoint!</p>

<h6 align="center"><img width="850px" src="https://github.com/user-attachments/assets/e6da30f8-ce17-4403-a5b3-bb395e76675c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Whenever you share a file via SharePoint, the recipient receives a notification email sent from your account. An attacker can abuse this by creating a document inside the compromised SharePoint (often a OneNote file), embedding malicious instructions or links, and sharing it with targeted victims. Because both email servers and users usually trust these notifications, SharePoint becomes a tool for distributing malware or phishing. The screenshot above is a classic example of this attack.</p>

<h3>Detecting SharePoint Abuse</h3>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/d83c0253-a352-4fbc-b272-0125b5fd7f5f"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>If you fail to notify all sharing recipients in time, your company may start a supply chain attack. For example, if an IT firm in Europe is breached, attackers may share malware with its retail clients in the USA. If lateral movement succeeds, the same attack can then spread from the retailer to its supplier, a larger manufacturer in Asia. It is essential to secure not only yourself, but also all partners and clients your company could affect.</p>

<h3>Advanced SharePoint Abuse</h3>
<p>Note that M365 logging can be confusing at times, and attackers are often very creative. For example, instead of creating a new file, they may backdoor an existing one (which results in a <strong>FileModified</strong> event). They can also lure other users into creating and sharing malware, which will mess up the logs. This is why, during an incident, you should review all activities in a chronological timeline instead of simply searching for specific events or indicators.</p>

<p><em>Answer the questions below</em></p>
<br>

<p>5.1. Which file type is often abused to share phishing through SharePoint?<br>
<code>OneNote</code></p>
<br>

<p>5.2. Which event is generated when someone shares a file with an external user?<br>
<code>AddedToSecureLink</code></p>

<br>
<br>
<h2>Task 6 &nbsp;・&nbsp; Real-world Scenario</h2> 
<p>The phone rings, it's the SOC manager:<br>

"Hey, quick one: our CEO, Michael, wants us to look into a OneNote file that was just shared by Emma Lawson, our Head of Customer Relationships. The file seems suspicious, and he can't recall approving any pricing updates. Before your shift ends, could you take a look and make sure everything is clean? I'll forward you the screenshots Michael sent me; check your inbox:"</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/914e1491-b211-45ba-a9a1-28adfd1af40a"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/ff76a4bc-bc91-4390-bf5b-a74028f2281a"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>
<br>

<p>6.1. When did Michael open the shared OneNote file? Answer Example: 2026-02-01 12:30:45<br>
<code>2026-02-03 12:49:44</code></p>

```bash
index=challenge "*Michael*"
| table _time UserId Operation ObjectId
|  sort by +_time
```

```bash
index=challenge "*Michael*"
|  table _time, Operation, UserId, ActorIpAddress
```

<img width="1290" height="353" alt="image" src="https://github.com/user-attachments/assets/fb86b6bf-5492-4bfe-9a76-a79b5bbe13b7" />

<br>
<br>
<br>
<p>6.2. With which three external emails did Emma share the file, too? Answer Format: Emails via comma, alphabetical order<br>
<code>li.wang@tryhatme.thm, susan.moore@deceptitech.thm, william.baker@probablyfine.thm</code></p>

```bash
index=challenge UserId=emma.lawson@tryhackme.thm Operation IN(AddedToSecureLink, SharingSet) action=shared
|  stats count values(TargetUserOrGroupName) by ObjectId
```

<img width="1276" height="411" alt="image" src="https://github.com/user-attachments/assets/46dd68bc-4bbc-408f-bda5-fe1750e24d1f" />

<br>
<br>
<br>
<p>6.3. One of the users from Question 2 already accessed the malicious file. What <strong>CorrelationId</strong> value proves that the sharing link has been opened?<br>
<code>945ff3a1-e059-0000-b054-6e5ee5ff2a81</code></p>

```bash
index=challenge Operation IN(*LinkUsed, FileAccessed) file_path="Shared Documents/Important Updates Regarding Pricing [B2B and B2E]"
|  stats count values(UserId) by CorrelationId
```

<img width="1278" height="431" alt="image" src="https://github.com/user-attachments/assets/7ac99c09-e13e-4e8e-bc00-8536d7c5409f" />

```bash
index=challenge Operation=SecureLinkUsed file_path="Shared Documents/Important Updates Regarding Pricing [B2B and B2E]"
|  table _time UserId CorrelationId
```

<img width="1282" height="305" alt="image" src="https://github.com/user-attachments/assets/d2993111-7c5b-4bce-a6fb-ff71fddb23e2" />

<br>
<br>
<br>
<p>6.4. Before sharing the malicious file, attackers reviewed Emma's SharePoint. Which PowerPoint presentation file did they exfiltrate?<br>
<code>THM PoC B2E.pptx</code></p>

```bash
index=challenge UserId=emma.lawson@tryhackme.thm "*.pptx*"
|  table _time UserId Operation ObjectId
```

<img width="1284" height="454" alt="image" src="https://github.com/user-attachments/assets/34352387-b5bc-4227-89eb-739f931eb2b1" />

<br>
<br>
<br>
<p>6.5. According to Entra ID logs, from which city was the malicious login performed?<br>
<code>Amsterdam</code></p>

```bash
index=challenge Operation IN(FileUploaded, FileCreated)
|  table _time UserId Operation ObjectId
|  sort by +_time
```

<img width="1275" height="347" alt="image" src="https://github.com/user-attachments/assets/c5ebc0bc-bedd-498e-895c-ef6d07e04490" />

```bash
index=challenge sourcetype="azure:aad:signin" userDisplayName="Emma Lawson" appDisplayName="SharePoint Online Web Client Extensibility"
```

<img width="1281" height="555" alt="image" src="https://github.com/user-attachments/assets/3b3b5964-c86c-4aa8-b4d5-8da092e08779" />

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/eb621e73-381b-4cf2-8696-b90823decf12"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/d9a0ba9e-0075-4b27-910a-03123930426e"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/bb6991ed-20c4-4394-81fc-51484766ec46"></p>


<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Room Name<br><br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|League<br><br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|---------------:|
|20<br><br>      |78<br><br>        |SharePoint Online Monitoring<br> |Medium<br><br> |🔗<br><br>| 1,153<br><br>| 161,629<br><br>| 91<br><br>| 14ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|19<br><br>      |77<br><br>        |Detecting AD Post-Exploitation<br>|Hard<br><br>  |🔗<br><br>| 1,152<br><br>| 161,517<br><br>| 91<br><br>| 14ᵗʰ<br><br>| 9ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|19<br><br>      |77<br><br>        |DockMagic - in progress<br><br>  |Medium<br><br> |🚩<br><br>| 1,151<br><br>|       -<br><br>|  -<br><br>|    -<br><br>|   -<br><br>|   -<br><br>|   -<br><br>|  -<br><br>|
|18<br><br>      |76<br><br>        |Phishing Unfolding<br><br>       |Medium<br><br> |⚙️<br><br>| 1,151<br><br>|       -<br><br>|  -<br><br>|    -<br><br>|   -<br><br>|   -<br><br>|   -<br><br>|  -<br><br>|
|18<br><br>      |76<br><br>        |Introduction to Phishing<br><br> |Easy<br><br>   |⚙️<br><br>| 1,151<br><br>|       -<br><br>|  -<br><br>|    -<br><br>|   -<br><br>|   -<br><br>|   -<br><br>|  -<br><br>|
|18<br><br>      |76<br><br>        |Dev Diaries<br><br>              |Easy<br><br>   |🚩<br><br>| 1,151<br><br>| 161,273<br><br>| 91<br><br>| 16ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|3ʳᵈ<br><br>|
|17<br><br>      |75<br><br>        |Missing Person<br><br>           |Easy<br><br>   |🚩<br><br>| 1,150<br><br>| 161,123<br><br>| 91<br><br>| 16ᵗʰ<br><br>|10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|1ˢᵗ<br><br>|
|17<br><br><br>  |75<br><br><br>    |Detecting AD Lateral Movement<br><br>|Medium<br><br><br>|🔗<br><br><br>| 1,149<br><br><br>| 160,883<br><br><br>| 91<br><br><br>| 16ᵗʰ<br><br><br>| 9ᵗʰ<br><br><br>| 2ⁿᵈ<br><br><br>| 1ˢᵗ<br><br><br>|-<br><br><br>|
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


<h1 align="center">My TryHackMe Journey ・ 2026, March</h1>
<p align="center">Global All Time:      14ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/4c572073-195b-4a60-9b8d-038d4bc9a1c2"><br><br>
                  Global Monthly:       10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/1f4c1657-d9fb-4919-a1c0-214d26a9f88e"><br><br>
                  Brazil All Time:       2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/27d1dc68-3683-4d59-a42f-e1b59174fa8a"><br><br>
                  Brazil Monthly:        1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/b4d1280f-19e1-498a-8a25-fe012f0556c8"></p>



<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
