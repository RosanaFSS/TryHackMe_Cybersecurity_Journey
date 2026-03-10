<h1 align="center"><a href="https://tryhackme.com/room/m365monitoringbasics">M365 Monitoring Basics</a></h1>
  
<p align="center"><img width="1200px" src=""><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2010-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<h2>Task 1 &nbsp;・&nbsp; Introduction</h2> 
<p>During a routine SOC shift, you, a L2 SOC Analyst at FineGalo, received an alert about multiple failed authentication attempts against a cloud account, followed by a successful login. Shortly after, suspicious behavior is observed in the user’s Microsoft 365 services. On their own, each event might seem explainable, but together, they tell a more concerning story.<br>

The organization relies entirely on Microsoft Entra ID for authentication and Microsoft 365 (M365) for collaboration and email. There are no endpoint alerts and no network indicators to rely on. Every clue lives in the logs of these cloud solutions.</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/755acf2a-0dff-4b5d-bc2a-5212cbfa4cbf"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In this room, you’ll step into that investigation and learn the role of Entra ID and M365 in modern company environments by analyzing their logs!</p>

<h3>Learning Objectives</h3>
<p>
  
- Understand the risks of identities and why attackers target them in modern environments.<br>
- Understand Entra ID and M365 as critical log sources for modern SOC investigations.<br>
- Understand Entra ID and M365 log types and core structure.<br>
- Basic understanding of how to use logs to identify attacks with Entra ID and M365 logs.</p>


<h3>Learning Prerequisites</h3>
<p>
  
- <a href="https://tryhackme.com/room/splunkexploringspl">Splunk: Exploring SPL</a><br>
- <a href="https://tryhackme.com/room/introtologanalysis">Intro to Log Analysis</a></p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> <em>Let´s start</em><br><a id='1.1'></a>
>> <code>No answer needed</code></strong><br>

<br>
<h2>Task 2 &nbsp;・&nbsp; What are Identity Providers</h2> 
<h3>Why Companies Moved Identities to the Cloud?</h3>
<p>Before cloud identity providers, organizations like FineGalo managed identity separately for each platform. Security controls were tied to individual systems, meaning protections like MFA, strong password policies, and access restrictions were available only if the platform supported them, for example:</p>

<h6 align="center"><img width="9000px" src="https://github.com/user-attachments/assets/d3a6c5f3-d689-43b3-a3d0-7dfc6fefc804"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>As companies moved to SaaS platforms and remote work, this fragmented model became hard to manage and even harder to secure. Platforms like Microsoft Entra ID solve this by centralizing authentication</strong> (who the user is) and authorization</strong> (what the user is allowed to do) into a single control plane.<br>

This leads to the classic question: "Identities are only user (person) access credentials?"</p>

<h3>What Is an Identity?</h3>
<p>A <strong>digital identity</strong> is a set of attributes that uniquely represent an entity within a computer system. That entity can be a person, a device, or a software component. Identities are used to <strong>authenticate</strong> entities, <strong>authorize</strong> their access to resources, enable communication, and support actions such as accessing services or performing transactions.<br>

At a high level, identities can be grouped into three categories:<br>

- <strong>Human identities</strong>: Represent people, such as employees, contractors, partners, or customers.<br>
- <strong>Workload identities</strong>: Represent software components, including applications, services, scripts, or containers, that need to authenticate to other systems.<br>
- <strong>Device identities</strong>: Represent physical devices like desktops, laptops, mobile phones, and IoT devices. These identities are separate from the humans who use them.</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/eccdbf02-fe8f-4444-84fb-8281f04588fa"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>An <strong>Identity Provider</strong> (IdP) is the system responsible for creating and managing these identities. It handles authentication (verifying identity), authorization (controlling access), and auditing by recording identity-related activity across connected services.</p>

<h6 align="center"><img width="550px" src="https://github.com/user-attachments/assets/ade9735b-5fe3-4fa9-8dfa-04e83fb59f61"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Microsoft Entra ID is an example of a cloud-based identity provider. Other examples include Twitter, Google, Amazon, LinkedIn, and Apple.<br>
  
<em>Example: You can use your Google account credentials to log in to Spotify. Here, your Google Sign-In is the IdP, and Spotify is the service provider (SP).</em></p>

<h3>Benefits of an IdP</h3>
<p>

- <strong>Centralized authentication and management</strong>: All user sign-ins are handled in a single location, making it easier to manage access and investigate suspicious activity.<br>
- <strong>Single Sign-On (SSO)</strong>: One successful authentication grants access to multiple cloud services, improving usability while reducing password sprawl.<br>
- <strong>Stronger authentication</strong>: Features such as MFA and Conditional Access can be enforced uniformly across users and applications, rather than configured per system.<br>
- <strong>Better visibility and logging</strong>: Every authentication attempt generates rich identity logs, giving analysts the context needed to detect and investigate threats.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What type of application is Entra ID?</em><br><a id='2.1'></a>
>> <strong><code>Identity Provider</code></strong><br>
<br>

> <em>What type of identity is a server account?</em><br><a id='2.2'></a>
>> <strong><code>device</code></strong><br>
<br>

<h2>Task 3 &nbsp;・&nbsp;Identities as the Target</h2> 
<p>Now that you understand what an Identity Provider (IdP) is, it becomes clear why attackers target it. In a cloud-first organization like FineGalo, Entra ID is the gateway to everything. It authenticates users and authorizes access to services like Outlook, Teams, SharePoint, and internal applications. That means a single compromised account, especially a privileged one, can give an attacker legitimate access without needing malware, local system access, or a foothold inside the network.<br>

Before you dig into the alert, we’ll cover the attacker goals behind cloud identity attacks and the most common risks in identity platforms that enable them.</p>

<h3>Why Attackers Are Targeting Cloud Credentials</h3>
<p>Attackers target cloud-based identity providers because they provide:<br>

- <strong>Remote access from anywhere</strong>: Authentication occurs over the internet, so attackers don’t need access to the internal network.<br>
- <strong>Legitimate access to multiple services via SSO</strong>: One successful sign-in can unlock emails, files, chat, and connected apps for a user.<br>
- <strong>Out of the radar of traditional tools</strong>: Firewalls and endpoint tools may see nothing suspicious because the attacker is using valid credentials or the authentication is occurring outside of their visibility.<br>
- <strong>Direct access to high-value resources</strong>: Email and collaboration platforms contain sensitive data, internal communication, and often allow resetting account credentials and other authentication factors.<br>

Entra ID has plenty of features to better protect identities within a tenant and prevent attackers from being successful. This leads to another important question: “<strong>If Entra ID is so secure, how do these attacks still work?</strong>”</p>

<h3>Cloud Identity Providers Security Gaps</h3>
<p>Cloud identity providers usually offer strong security controls, but those controls only work when they’re properly configured and consistently enforced. In many incidents, attackers don’t rely on advanced exploits; they simply exploit the lack of these security configurations.<br>

Using Entra ID as an example, the diagram below illustrates how the platform evaluates authentication signals to decide whether to allow, block, or request MFA validation before a user can access the organization's apps and data.</p>

<h6 align="center"><img width="900px" src="https://github.com/user-attachments/assets/b7e2d3e1-9486-45b7-8003-0f16819ac63a"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Common misconfigurations (or lack of configuration) that increase the risk of compromise:<br>

- <strong>Lack of multi-factor authentication (MFA) enforcement</strong>: Attackers can gain access with simple stolen credentials, bypassing MFA entirely.<br>
- <strong>Overly permissive access policies</strong>: Broad policies or group exclusions create gaps, allowing sign-ins from any location or exempting admin accounts from security requirements.<br>
- <strong>Excessive administrative privileges</strong>: Too many admin accounts or standing privileges increase the attack surface and, if compromised, provide full tenant control.<br>
- <strong>Weak password policies</strong>: Default settings may allow easily guessable passwords without protection against known breaches or common password lists.<br>
- <strong>Disabled authentication risk policies</strong>: Risky authentication attempts from suspicious IPs or locations may be permitted if security policies aren’t enabled.<br>
- <strong>Insufficient logging and monitoring</strong>: Without active monitoring of sign-in and audit logs, suspicious activity can persist undetected for extended periods.</p>

<h3>Importance of Identity Logs</h3>
<p>After learning the identity risks, one thing is clear: attackers don’t need advanced exploits — they just need a gap.<br>
Those gaps don’t always trigger alerts; the strongest evidence often lives in logs. That’s why we will cover many of these logs in this module, as they are a powerful resource for identifying both Entra ID and M365 threats.<br>

The logs can reveal to us:<br>

- Successful and failed logins<br>
- Reasons for failed logins (e.g., bad password)<br>
- Account lockouts<br><br>
- MFA prompts and results<br>
- Source IP address and users' geographic location<br>
- Device and browser information<br>
- Client/app used to authenticate (browser, mobile app, etc.).<br>
- Conditional Access outcomes (allowed, blocked, MFA required, etc.).<br>

You can also use this identity data to correlate with service logs, such as M365, to analyze what the user did after successfully accessing an account (mailbox access/management, file downloads, chat activity, etc.).</p>

<p align="center">It's important to mention that these logs can be tricky because they're very rich,<br> capturing every step of every interaction in Entra ID or M365 environments.<br> When analyzing them, use a timeline approach to understand<br> what's happening from a user or application perspective.</p>

<p>Now that you know the importance of cloud-based identity logs, we will start exploring them in the following task!</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What authentication resource can prevent attackers from authenticating with only a stolen password?</em><br><a id='3.1'></a>
>> <strong><code>MFA</code></strong><br>
<br>

> <em>What can help us detect and monitor cloud identity threats?</em><br><a id='3.2'></a>
>> <strong><code>Logs</code></strong><br>
<br>

<h2>Task 4 &nbsp;・&nbsp; Entra ID Sign-in Logs</h2> 
<p>After understanding why attackers target cloud identities, let's dive into how we use their logs. This is where Microsoft Entra ID's logging capabilities become your most valuable tool.<br>

Microsoft Entra ID generates detailed logs for every authentication attempt, configuration change, and administrative action within a tenant. These logs don't just tell you what happened, they tell you who did it, when, where from, and often why it succeeded or failed.</p>

<h3>Entra ID Core Components</h3>
<p>Before we explore the logs, let's understand the key components that generate them:</p>

<h4>Users and Sign-ins (Authentication)</h4>
<p>Every time a user attempts to authenticate to any service protected by Entra ID, a record is created. This includes successful logins, failed attempts, MFA challenges, and the context around each event (IP address, location, device, application, and others).</p>

<h4>Roles and Access Decisions (Authorization)</h4>
<p>After authentication, Entra ID determines what the user is allowed to do based on their assigned roles and permissions. Changes to these roles, group memberships, or permissions are all logged in audit events.</p>

<h4>Security Features</h4>
<p>Entra ID includes built-in security capabilities that generate their own logs:<br>

- <strong>Multi-factor authentication (MFA)</strong>: Logs show whether MFA was required, prompted, satisfied, or bypassed.<br>
- <strong>Conditional Access policies</strong>: These policies enforce rules like "require MFA from untrusted locations." Logs show which policies were applied and their outcomes (allowed, blocked, MFA required).<br>
- <strong>Identity Protection</strong>: Entra ID's native threat detection flags risky sign-ins (impossible travel, anonymous IP, password spray) and risky users. We won't dive deep into these in this room, but we will see how these logs can help us identify threats in the next room, Entra ID Monitoring (coming soon).</p>

<h3>Exploring Entra ID Logs</h3>
<p>To explore the Entra ID logs and investigate the alert, we will use a Splunk instance. Start the lab by clicking the Start Machine button below. You will then have access to the Splunk Web Interface.
To access Splunk, please wait for the VM to start and follow this link:<br>

- https://LAB_WEB_URL.p.thmlabs.com<br>

Please wait 4-5 minutes for the Splunk instance to launch. Use Splunk’s All Time range to search. The indexes where logs are stored for each practical exercise are present in each task.</p>

<h3>Set up your virtual environment</h3>
<p>To successfully complete this room, you'll need to set up your virtual environment. This involves starting the Target Machine, ensuring you're equipped with the necessary tools and access to tackle the challenges ahead.</p>

<h3>Sign-in Logs</h3>
<p>The alert you are tasked to investigate mentions multiple failed authentication attempts followed by a successful login. The Sign-in logs capture every authentication attempt made against a tenant. It will show you the brute force pattern and the moment the attacker succeeded!<br>

In the Splunk instance, you can start hunting by filtering all the Sign-in (authentication) logs:</p>

<br>
<div align="center"><p>

| List all Sign-in events                                           |  
|:-----------------------------------------------------------------:|

</p></div>

```bash
index=scenario sourcetype="azure:aad:signin"
```

<p align="center"><strong>Entra ID was previously named Azure Active Directory (Azure AD).<br>When you see "Azure Active Directory" or "Azure AD"<br> in the logs or elsewhere, it is the same as Entra ID.</strong></p>

<p>The structure of a Sign-in log has a couple of fields that may help you identify a suspicious authentication attempt:</p>

```bash
{
  "id": "014adaeb-c9db-4119-8a9b-a9f68dd4b700",
  "createdDateTime": "2026-02-11T17:15:10Z",
  "userDisplayName": "John Doe",
  "userPrincipalName": "john.doe@contoso.onmicrosoft.com", // The user address
  "userId": "a1b2c3d4-e5f6-7890-a1b2-c3d4e5f67890",
  "appId": "4765445b-32c6-49b0-83e6-1d93765276ca",
  "appDisplayName": "OfficeHome", // Which application the user logged in to. In this case, the main web portal (office.com)
  "ipAddress": "203.0.113.45", // The IP address used by the user.
  "clientAppUsed": "Browser",
  "correlationId": "dc8fb3db-403c-43e4-b759-21aa137a143a",
  "conditionalAccessStatus": "success",
  "isInteractive": true,
  [...]
  "resourceDisplayName": "OfficeHome",
  "resourceId": "4765445b-32c6-49b0-83e6-1d93765276ca",
  "status": {
    "errorCode": 0, // The result of the authentication. Code 0 means successful.
    "failureReason": "Other.",
    "additionalDetails": null
 [...]
  "location": {  // Details about the location from the IP address used by the user.
    "city": "New York",
    "state": "New York",
    "countryOrRegion": "US",
    "geoCoordinates": {
      "altitude": null,
      "latitude": 40.7128,
      "longitude": -74.0060
    }
  },
  "appliedConditionalAccessPolicies": [ // Information about which access control policy was applied during the authentication process.
    {
      "id": "c63499f4-64b6-4943-bfc3-52fbb641ef10",
      "displayName": "Require MFA",
      "enforcedGrantControls": ["Block"],
      "enforcedSessionControls": [],
      "result": "notApplied"
    }
  ]
}
```

<p>With this context, you can use the <code>errorCode</code> to find failure attempts and other relevant data:</p>

<br>
<div align="center"><p>

| List all failed Sign-ins                                          |  
|:-----------------------------------------------------------------:|

</p></div>

```bash
index="scenario" sourcetype="azure:aad:signin" "status.errorCode"!=0
| stats count as event_count values(ipAddress) as ip_addresses
 values(appDisplayName) as applications values(status.errorCode) as errorCodes  by userPrincipalName
| sort - event_count
| table applications, userPrincipalName, ip_addresses, errorCodes, event_count
```

<p>Error codes are a big ally when analyzing suspicious authentication alerts. They can help you to understand the stage of a credential attack the attacker is in. Below are common error codes:<br>

- <code>50126</code>: Invalid username or password<br>
- <code>50053</code>: Account locked due to too many failed attempts<br>
- <code>50074</code>: MFA required but not provided<br>
- <code>50055</code>: Password expired<br>

If you want to verify what an error code means, Microsoft has a useful <a href="https://login.microsoftonline.com/error">tool</a> to help you research it.<br>

In the same query results, you can see that all failed attempts are from the same source IP in the <code>ipAddress</code> field. This is relevant information for further investigation into what this IP address has done in the tenant.<br>

Now, you can filter the successful logins from this source and validate which account was compromised and the applications the attacker accessed by changing the <code>ADD-IPHERE</code> placeholder to the IP address you want to investigate in the following query:</p>

<br>
<div align="center"><p>

| List all successfull Sign-ins from an IP address                  |  
|:-----------------------------------------------------------------:|

</p></div>

```bash
index=scenario sourcetype="azure:aad:signin" "status.errorCode"=0 ipAddress="<ADD-IP-HERE>"
| stats values(ipAddress) as ip_addresses values(appDisplayName) as applications  by userPrincipalName
| table applications, userPrincipalName, ip_addresses
```

<p>You should see the exact account that the attacker compromised!</p>

<h4>Practice</h4>
<p>For this task, you will answer a couple of questions regarding this suspicious authentication.<br>
With the filter <code>index=scenario sourcetype="azure:aad:signin"</code>, you will be able to see all Sign-in logs, but feel free to use any other queries you learned in this task.<br>
Remember to search for All Time to find all log activity.</p>


<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What is the email address of the compromised identity?</em><br><a id='4.1'></a>
>> <strong><code>allan.smith@finegalo.thm</code></strong><br>

<br>
<p><code>56</code> sign-ins</p>

```bash
index=scenario sourcetype="azure:aad:signin"
```

<img width="1348" height="369" alt="image" src="https://github.com/user-attachments/assets/aa5e40be-e802-467a-b289-78340027c6fc" />

<br>
<br>
<p><code>26</code> failed sign-ins</p>

```bash
index="scenario" sourcetype="azure:aad:signin" "status.errorCode"!=0
| stats count as event_count values(ipAddress) as ip_addresses
 values(appDisplayName) as applications values(status.errorCode) as errorCodes  by userPrincipalName
| sort - event_count
| table applications, userPrincipalName, ip_addresses, errorCodes, event_count
```

<img width="1352" height="341" alt="image" src="https://github.com/user-attachments/assets/be17c472-7629-4ef8-9900-5d0685e17695" />

<br>
<br>
<br>

> <em>What is the IP address used by the attacker?</em><br><a id='4.2'></a>
>> <strong><code>2804:2488:7082:a4c0:fd97:b11b:9895:49c0</code></strong><br>

<img width="1352" height="341" alt="image" src="https://github.com/user-attachments/assets/be17c472-7629-4ef8-9900-5d0685e17695" />

<br>
<br>
<br>

> <em>What is the city of the IP address used by the attacker?</em><br><a id='4.3'></a>
>> <strong><code>Belo Horizonte</code></strong><br>

```bash
index="scenario" sourcetype="azure:aad:signin" status.errorCode="0" ipAddress="2804:2488:7082:a4c0:fd97:b11b:9895:49c0"
| table _time appDisplayName, userDisplayName, userPrincipalName, ipAddress, deviceDetail.browser, status.errorCode, location.city, status.failureReason
| sort by -_time
```

<img width="1349" height="670" alt="image" src="https://github.com/user-attachments/assets/4c674ae3-4a4d-4d8b-8f8a-57789fd6c056" />

<br>
<br>
<br>

> <em>When was the first successful sign-in in the compromised account after the failure attempts? Answer Format: 1/12/25 1:15:00.000 PM (Exact Splunk <code>Time</code> value)</em><br><a id='4.4'></a>
>> <strong><code>2/11/26 6:16:53.000 PM</code></strong><br>

```bash
index=scenario sourcetype="azure:aad:signin" "status.errorCode"=0 ipAddress="2804:2488:7082:a4c0:fd97:b11b:9895:49c0"
| table _time signinDateTime ipAddress appDisplayName userPrincipalName
|  sort by +_time
```

<img width="1347" height="473" alt="image" src="https://github.com/user-attachments/assets/acda097a-9136-49c8-b92c-252719f11031" />

<br>
<br>

<img width="1274" height="120" alt="image" src="https://github.com/user-attachments/assets/59fe1cdd-fd11-4a00-831b-c8c93976fb85" />

<br>
<br>
<br>

> <em>What is the first application the attacker accessed after the office home page? Answer Format: The exact value of the <code>appDisplayName</code> field.</em><br><a id='4.4'></a>
>> <strong><code>One Outlook Web</code></strong><br>


<img width="1349" height="431" alt="image" src="https://github.com/user-attachments/assets/e1e9829b-c84d-4737-8619-b9e0dba2bc5e" />

<br>
<br>
<br>
<h2>Task 5 &nbsp;・&nbsp; Entra ID Audit Logs</h2> 

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What was the first change made by the attacker in the compromised user account? Answer Format: Paste the exact value of <code>activityDisplayName</code></em><br><a id='5.1'></a>
>> <strong><code>User started security info registration</code></strong><br>

```bash
index=scenario sourcetype="azure:aad:audit" targetResources{}.userPrincipalName="allan.smith@finegalo.thm"
| table _time activityDisplayName initiatedBy.app.displayName initiatedBy.app.servicePrincipalId result operationType loggedByService targetResources{}.userPrincipalName
|  sort by +_time
```

<img width="1341" height="638" alt="image" src="https://github.com/user-attachments/assets/83d86205-0a52-430f-a34d-47f53c723a3c" />

<br>
<br>
<br>

```bash
index=scenario sourcetype="azure:aad:audit" targetResources{}.userPrincipalName="allan.smith@finegalo.thm"
| eval initiator=coalesce('initiatedBy.user.userPrincipalName', 'initiatedBy.app.displayName')
| sort - _time
| table _time, initiator, activityDisplayName, result, targetResources{}.userPrincipalName
```

<img width="1340" height="600" alt="image" src="https://github.com/user-attachments/assets/566ce09b-748a-4d30-b479-9ed676c1a562" />

<br>
<br>
<br>

> <em>What is the <code>activityDisplayName</code> that reveals all the details of the modified properties in a user?</em> Hint: Explore the logs content beyond the queries you learned in this task. For example, remove the table function to explore raw logs.<br><a id='5.2'></a>
>> <strong><code>Update User</code></strong><br>

```bash
index=scenario sourcetype="azure:aad:audit" initiatedBy.user.userPrincipalName="allan.smith@finegalo.thm"
| table _time activityDisplayName initiatedBy.app.displayName result initiatedBy.app.servicePrincipalId result operationType loggedByService targetResources{}.userPrincipalName
|  sort by +_time
```

<img width="1349" height="471" alt="image" src="https://github.com/user-attachments/assets/fa2a46a5-6571-442d-8a40-fdd01a24c288" />


<br>
<br>
<br>

> <em>What is the second change made in the account? Answer Format: Paste the exact value of the <code>activityDisplayName</code> field.</em> Hint: Remember that one change can generate multiple logs.<br><a id='5.3'></a>
>> <strong><code>   </code></strong><br>

```bash
index=scenario sourcetype="azure:aad:audit" targetResources{}.userPrincipalName="allan.smith@finegalo.thm"
| eval initiator=coalesce('initiatedBy.user.userPrincipalName', 'initiatedBy.app.displayName')
| sort - _time
| table _time, initiator, activityDisplayName, result, targetResources{}.userPrincipalName
```

<img width="1349" height="471" alt="image" src="https://github.com/user-attachments/assets/b0d6ba0b-a994-4f8e-8e1c-2f4dd5db4550" />

<br>
<br>
<br>

```bash
index=scenario sourcetype="azure:aad:audit" initiatedBy.user.userPrincipalName="allan.smith@finegalo.thm"
| eval initiator=coalesce('initiatedBy.user.userPrincipalName', 'initiatedBy.app.displayName')
| sort - _time
| table _time, initiator, activityDisplayName, result, targetResources{}.userPrincipalName
```

<img width="1341" height="481" alt="image" src="https://github.com/user-attachments/assets/0fe24eed-fd36-4600-969a-877ab95094da" />

<br>
<br>
<br>
<h2>Task 6 &nbsp;・&nbsp; M365 Introduction</h2> 

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> <em>Let's explore M365 logs!</em><br><a id='6.1'></a>
>> <strong><code>Prevention</code></strong><br>
<br>

<br>
<h2>Task 7 &nbsp;・&nbsp; M365 Audit Logs</h2> 

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the questions below}}$$ </h3>

> <em>What is the application used by the attacker? Answer Format: Paste the exact value of the <code>Workload</code> field.</em><br><a id='7.1'></a>
>> <strong><code>    </code></strong><br>

```bash
mm
```


<br>
<br>
<br>

> <em>What is the change made in the user application by the attacker? Answer Format: Paste the exact value of the <code>Operation</code> field.</em><br><a id='7.2'></a>
>> <strong><code>    </code></strong><br>

```bash
mm
```


<br>
<br>
<br>

> <em>What is the subject of the email message sent by the attacker?</em><br><a id='7.3'></a>
>> <strong><code>    </code></strong><br>

```bash
mm
```


<br>
<br>
<br>

> <em>When did the attacker access the response to the message? Answer Format: 1/12/25 1:15:00.000 PM (Exact Splunk <code>Time</code> value)</em> Hint: Explore the logs content beyond the queries you learned in this task. For example, remove the table function to explore raw logs.<br><a id='7.4'></a>
>> <strong><code>    </code></strong><br>

```bash
mm
```


<br>
<br>
<br>

> <em>Which path was the response stored in? Answer Format: \PathName</em> HInt: Email answers usually starts with "Re:" in English conversations in outlook.<br><a id='7.5'></a>
>> <strong><code>    </code></strong><br>

```bash
mm
```


<br>
<br>
<br>

<br>
<h2>Task 8 &nbsp;・&nbsp; Conclusion</h2> 
<p>Congratulations! You've completed your first investigation into a compromised cloud identity using Entra ID and M365 logs.</p>

<h3>What You've Learned</h3>

<p>

- Learned why attackers target Entra ID and M365, and the common gaps they exploit.<br>
- Learned that the real power of these log sources lies in correlating them to build a complete timeline of an attack.<br>
- Understand that Entra ID Sign-in logs are the investigation starting point to identify:<br>Suspicious authentication attempts.<br>If an attacker successfully authenticates.<br>The location from which the authentications are coming.<br>
- Understand that Entra ID Audit logs help you to identify privilege escalation or persistence at the identity level.<br>
- Understand that M365 Audit logs help you to identify what the attacker did with legitimate access in the company's applications, such as Outlook, SharePoint, and others.<br>

In the next room, Entra ID Monitoring (coming soon), you'll learn about multiple common techniques attackers use when targeting Entra ID identities and how you can detect or prevent them.</p>

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>

> <em>Ready to explore Entra ID threats!</em><br><a id='8.1'></a>
>> <strong><code>No answer needed</code></strong><br>
<br>

<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="900px" src=""><br>
                  <img width="900px" src=""><br>
                  <img width="900px" src=""></p>

            
<h1 align="center">My TryHackMe Journey ・ 2026, March<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Level<br><br><br>|Type<br><br><br>|Name<br><br><br>                         |Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Brazil<br>Monthly<br><br>|Brazil<br>All<br>Time|Global<br>Monthly<br><br>|Global<br>All<br>Time|
|:---------------|:-----------------|:----------------|:---------------|:----------------------------------------|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|10<br><br>      |68<br><br>        |Medium<br><br>   |🔗<br><br>     |M365 Monitoring Basics<br><br>           |             1,023<br><br>|   xxx,xxxx<br><br>|       91<br><br>|          xxx<br><br>|               2ⁿᵈ<br><br>|          xxx<br><br>|    xxx<br><br>|

</h6></div><br>

<p align="center">
Global All Time: &nbsp; <strong>54</strong>ᵗʰ<br><img width="300px" src=""><br>Brazil Monthly: &nbsp; <strong>22</strong>ⁿᵈ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
Brazil All Time: &nbsp; <strong>3</strong>ʳᵈ<br><img width="450px" hspace="20" src="https://github.com/user-attachments/assets/9df63d3f-0752-4b41-ac06-3e02b1d38643"><img width="450px" src="https://github.com/user-attachments/assets/8b3fdc2b-4878-4c13-b5f2-67a13804f821"><br><br>Global Monthly: &nbsp; <strong>1,372</strong>ⁿᵈ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
Global All Time: &nbsp; <strong>54</strong>ᵗʰ<br>
<img width="450px" hspace="20" src="https://github.com/user-attachments/assets/7c917f96-2b7a-4d68-bd10-17b6a6d14439">
<img width="450px" src="https://github.com/user-attachments/assets/91d37f3b-aae1-45f8-b246-b4d4ce4bb88e"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
