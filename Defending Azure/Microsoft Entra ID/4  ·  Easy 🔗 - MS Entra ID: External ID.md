<h1 align="center"><a href="https://tryhackme.com/room/entraidexternalid">MS Entra ID: External ID</a></h1>
<h3 align="center">Defending Azure Learning Path &nbsp;|&nbsp; Microsot Entra ID</h3>
<p align="center"><img width="1200px" src=""><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20FEV%202-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  External Identity: [Guest Users](#1)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Inviting [External Users](#2)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Lab [Instructions](#3)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Lab-03: &nbsp;&nbsp; [External Collaboration Settings](#4)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Lab-04: &nbsp;&nbsp; [Inviting Guest Users](#5)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Security Best Practices: [User Settings](#6)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  [Conclusion](#7)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  My TryHackMe [Journey](#8)

<br><br>
<h2>Task 1 . External Identity: Guest Users<a id='1'></a></h2>
<h3>What Are External Identities?</h3>
<p>Microsoft Entra ID external users, or B2B (business-to-business) users, are individuals or user accounts that are not part of your organization's internal Active Directory but need to access resources or securely collaborate with your organization; you can collaborate with partners, distributors, suppliers, or vendors, you can share your resources and define how your internal users can access external organizations. In this case, the external user’s identity provider manages their identity, and you manage access to your apps with Microsoft Entra ID or Azure AD B2C to protect your organization's resources.<<br>
  
Here are some ways external identities are represented in MS Entra ID:<br>

- <strong>B2B collaboration</strong>: Invite external users to sign in to your Microsoft Entra organization using their credentials to access the apps and resources you want to share with them.<br> - Scenario: External users need access to the organization's Office 365, SaaS apps, and line-of-business applications.<br> - When: Partner doesn't use MS Entra ID.<br> - B2B Credentials: None in MS Entra ID. B2B users are added to your MS Entra ID but authenticated with their organization or identity provider (IdP).<br> - How: Use cross-tenant access settings to manage B2B collaboration.<br>
- <strong>B2B direct connect</strong>: Let your organization's users collaborate with external users from multiple organizations with a Teams shared channel for chat, calls, file sharing, and app sharing.<br>- Scenario: Microsoft Teams collaboration.<br>- When: Partner does use MS Entra ID.<br>- B2B credentials: None in MS Entra ID. B2B direct connect users are also not added to the MS Entra directory.<br>- How: Use cross-tenant access settings to manage B2B collaboration.
- <strong>Azure AD B2C</strong>: This is a Customer Identity and Access Management (CIAM) solution used if the organization is developing customer-facing apps. It provides business-to-customer identity as a service.<br>- Scenario: Publish apps to consumers and customers using Azure AD B2C for identity experiences.<br>- When: Customers of your product need to authenticate via their own social media, government, or other business ID accounts.<br>- B2C credentials: These users are managed in a separate Microsoft Entra directory, i.e., B2C directory.<br>- How: Via creating a separate Azure AD B2C tenant.<br

[ Tutorial ]</p>

<p><em>Answer the questions below</em></p>

<p>1.1. <em>Which external identity option is best if you want external users to collaborate with your line-of-business applications?</em><br>
<code>b2b collaboration</code></p>

<p>1.2. <em>Which external identity option is best suited if users will be logging in with their social media accounts?</em><br>
<code>Azure AD B2C</code></p>

<br><br>
<h2>Task 2 . Inviting External Users<a id='2'></a></h2>
<p>Guest users can be invited to an MS Entra ID directory, a group, or an application. Once invited, the user is added to MS Entra ID with the user type Guest.<br>

The experience of adding guest users is similar to adding internal users, as seen below:</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/d1171943-883c-44db-8010-f7d5d63ae406"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>Here, you can compose an invitation message and assign groups and roles for the external user.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/03b9ce9f-ddf7-4e37-bace-46563ce14f8c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>In a scenario where a new partnership has been established with your company, in the interim, employees of the partner company could be added as guests via <strong>bulk invite</strong>.</p>

<h6 align="center"><img width="500px" src="https://github.com/user-attachments/assets/57e291e3-a27c-403f-8468-1c27534cce18"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p>The user is added to the inviting tenant directory with a user principal name (UPN) in the format <code>user@email.com#EXT#@domain</code>. E.g., <code>john_doe.com#EXT#@tryhackme.onmicrosoft.com</code>.</p>

<h3>MS Entra ID Kill Chain - Guest Users</h3>
<p>As for security best practices, it is important to limit the users who can send guest invites since a guest user account would be a major attack primitive for initial access in the MS Entra ID kill chain. We will look into the MS Entra ID kill chain later on, but for now, let's note that the kill chain consists of five different roles:<br>

<code>Outsider</code> -> <code>Guest</code> -> <code>Insider</code> -> <code>Admin</code> -> <code>On-prem admin</code><br>

It is worth remembering that although guest users have restricted access to MS Entra ID, they can still gather lots of useful tenant information using various APIs, such as the MS Graph API.</p>

<h4>Guest Inviter Role</h4>
<p>There is also a specific "<strong>Guest Inviter</strong>" role for inviting external users, which could be utilized if a dedicated user in the organization needs to invite users.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/4a109d87-13ca-4eff-97ee-8f2566d5aa28"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Note that <strong>Guest Inviter</strong> role can still invite guests even if the following external collaboration settings are restricted, i.e., when the "<strong>Members can invite</strong>" user setting is set to <strong>No</strong>.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/6eeb127f-ef92-487d-be37-94f19273b208"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h4>Email One-Time Passcode (OTP)</h4>
<p>The <strong>email one-time passcode (OTP)</strong> feature can be used to authenticate B2B collaboration users when they can't be authenticated through other means, such as Microsoft Entra ID, Microsoft account (MSA), or social identity providers.<br>

A temporary passcode can be requested when a B2B guest user tries to redeem the guest invitation or sign in to shared resources. This passcode is then sent to their email address. They enter this passcode to continue signing in.<br>

Conditions when an email OTP becomes a sign-in option for guest users:<br>

- The guest user has no <strong>Microsoft Entra account</strong>.<br>
- The guest user has no <strong>Microsoft account</strong>.<br>
- Guest users have no other authentication method or <strong>any password-backed accounts</strong>.<br>
- The inviting tenant didn't set up a federation with social (like Google) or other identity providers.<br>
- <strong>Email one-time passcode for guests</strong> setting is <strong>enabled</strong> in Microsoft Entra ID.</p>

<p><em>Answer the questions below</em></p>

<p>2.1. <em>Which least privileged role is specifically for inviting external users?</em><br>
<code>guest inviter</code></p>

<p>2.2. <em>In the MS Entra kill chain, what type of users could be the first target of initial access?</em><br>
<code>guest</code></p>

<p>2.3. <em>Is it a security best practice to restrict who can invite guest users? (Yea/Nay)</em><br>
<code>Yea</code></p>

<p>2.4. <em>What can be used to invite guests if they have no other means of authenticating themselves?</em><br>
<code>email one-time passcode</code></p>

<br><br>
<h2>Task 3 . Lab Instructions<a id='3'></a></h2>
<p>Kindly follow the instructions below to access your labs for the next tasks.<br>

On your lab task (<strong>Lab-03: External Collaboration Settings</strong>: Task 4; <strong>Lab-04: Inviting Guest Users</strong>: Task 5), click the <strong>Cloud Details</strong> button.<br>

On the <strong>Environment</strong> tab, click the Join Lab button to deploy your lab environment.</p>


<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/65d92fb7-7dc9-4eca-b5f3-50874cef7a06"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Click the <strong>Open Lab</strong> button to launch a new tab. This will direct you to the Microsoft Entra admin center.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/82c2ba5a-724e-42bc-b378-ea747ff8ac12"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Select the <strong>Credentials</strong> tab to view your login credentials required to access the Microsoft Entra admin center.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/149c3559-3670-4848-8a7b-65e3da14506c"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Sign in using your <strong>Username</strong> and <strong>Password</strong> from the Credential tab. Then click <strong>Next</strong> to continue.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/5d7fc553-b421-43c1-9e03-cab301506c3e"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>With the new Microsoft multifactor authentication enforcement, you will be required to set up MFA to sign in to the Microsoft Entra admin center. Click <strong>Next</strong> to configure MFA using your preferred method.</p>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/1dd45ad4-935b-45c5-9d5a-9496887d1a97"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>By clicking on <strong>I want to set up a different method</strong> you can see all available MFA options.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/e3ed067d-1f74-44b9-a362-a40c1eda075a"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>The default authentication method is to use the free Microsoft Authenticator app. If it is installed on your mobile device, select Next and follow the prompts to add this account. If you don't have it installed, a link is provided to download it.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/f70ed07d-3604-4a09-a5d1-66a572e71cde"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>Complete the authentication process to sign in to the Microsoft Entra admin center.<br>

<strong>Note</strong>: Lab access will expire after 1 hour.</p>
<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/fa805cbc-feaa-4e9f-9662-59ae11f76c6f"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>


<p><em>Answer the question below</em></p>

<p>3.1. <em>I am ready to go hands-on!</em><br>
<code>No answer needed</code></p>

<br><br>
<h2>Task 4 . Lab-03: External Collaboration Settings<a id='4'></a></h2>
<h4>Microsoft Entra ID Lab Rules</h4>
<p>

- You are being assigned a privileged role, so be careful not to break things which will affect your other colleagues.<br>
- Labs are shared cloud environments for all learners in your organization.<br>
- You might be able to see other learners' lab assets, such as directory objects (users, groups, and more).<br>
- Only modify or delete the lab assets you own or create in the lab environment.</p>

<h4>Context</h4>
<p>You work for a company that provides clients with on-demand virtual environments for cyber security training.</p>

<h4>Role</h4>
<p> You are logged in as:<br>
  
- <a href="https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference?WT.mc_id=Portal-Microsoft_AAD_IAM#global-administrator">Global Administrator</a></p>

<p>Check out the  <a href="https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-by-task#external-identitiesazure-ad-b2c-least-privileged-roles">legal roles by task</a> for external collaboration settings.</p>

<h4>Lab Scenario</h4>
<p>You have been tasked with reviewing and hardening guest user settings in Microsoft Entra ID as part of organizational security hardening and <strong>attack surface reduction (ASR)</strong> initiatives.</p>

<p>Access your lab by clicking the Cloud Details button below in conjunction with the lab instructions from Task 3:<br>

[ Cloud Details ]</p>


<h3>Step 1: Review and Harden External Collaboration Settings</h3>

<div align="center"><h6>

|Guest user access restrictions<br><br>         |Guest invite restrictions<br><br>               |Note<br><br>                                  |
|:----------------------------------------------|:-----------------------------------------------|:----------------------------------------------|
|This settings determines whether guests:<br>- &nbsp;&nbsp; Have <strong>full access to enumerate all users and group memberships</strong> (most inclusive - not the best idea!)<br>- &nbsp;&nbsp; Have <strong>limited access</strong> to other users and memberships<br>- &nbsp;&nbsp; Have <strong>no access</strong> to other users and group memberships, including groups they are a member of (most restrictive - that sounds better!). The most restrictive setting here will significantly reduce a potential staged guest user's <strong>reconnaissance capabilities</strong> on the tenant.<br><br>|This setting controls who can invite guests to the directory to collaborate on resources secured by the organization, such as SharePoint sites or Azure resources.<br>- &nbsp;&nbsp; Ensure "<strong>only users assigned to specific admin roles can invite guest users</strong>" is set.<br><br><br>|<strong>Guest user</strong> invites are a prime "<strong>initial access</strong>" and "persistence" attack vector!<br> - &nbsp;&nbsp; On Microsoft Entra admin center<br>- &nbsp;&nbsp; Navigate to <code>Identity</code> > <code>External Identities</code> > <code>External collaboration settings</code><br><br>|

</h6></div>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/b5dd7011-52db-41bf-a9ce-b07ce9bcf0ee"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Step 2: Disable Email One-Time Passcode (OTP) for Guests</h3>
<p>The email OTP feature is turned on by default for all new tenants and for any existing tenants for whom you haven’t explicitly turned it off. Better turn it off!<br>

<code>Identity</code> > <code>External Identities</code> > <code>All identity providers</code> > <code>Email one-time passcode</code> > <code>No</code></p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/b9d62543-b2cb-40d5-8ab6-e33e3e6bdbec"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>Are guest users potential attack vectors? (Yea/Nay)</em><br>
<code>Yea</code></p>

<p>4.2. <em>If guest user access is not restricted, what can a guest user easily perform on the tenant?</em><br>
<code>Reconnaissance</code></p>

<p>4.3. <em>Which setting, when enabled will allow users who don't have Microsoft Entra or Microsoft account to sign in without having to create an account?</em><br>
<code>Email one-time passcode for guests</code></p>

<h2 align="center">Lab-03: External Collaboration Settings</h2>
<p align="center">Rosana´s hands on</p>

<h6 align="center"><img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""></h6>

<br><br>
<h2>Task 5 . Lab-04: Inviting Guest Users<a id='5'></a></h2>
<h4>Context</h4>
<p>Your company hired some external penetration testers for a limited engagement. As part of this engagement, pentesters will need to evaluate the reconnaissance capabilities of a guest user and what kind of Entra ID directory objects are visible to a guest user based on the organization's current Entra ID configuration.</p>

<h4>Role</h4>
<p> You are logged in as:<br>
  
- <a href="https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#guest-inviter">Guest Inviter</a></p>

<h4>Lab Scenario</h4>
<p>You have been tasked with inviting pentesters to your Entra ID so that they can start the engagement.<br>

Leave the previous Lab by clicking the <strong>Leave Lab</strong> button, then access this lab by clicking the <strong>Cloud Details</strong> button below in conjunction with the lab instructions from Task 3:<br>

[ Cloud Details]</p>


<h3>Step 1: Confirm You Have the Guest Inviter Role Assignment Prior To Inviting Guest Users</h3>
<p>
  
- Log in to Microsoft Entra ID center<br>
- Navigate to <code>Identity</code> > <code>Users</code> > <code>All Users</code> > <code>usr-AZURE_LAB_ID</code> > <code>Assigned roles</code><br>
- Guest Inviter</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/52e051e0-f66f-47c9-a129-ba8f5134efce"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Step 2: Invite External User</h3>
<p>

- <code>Identity</code> > <code>Users</code> > <code>All Users</code> > <code>New Users</code> >  <code>Invite external user</code><br>
- <stong>Note</strong>: As a Guest Inviter, you cannot create a new (member) user<br>
- Fill out the "<code>Invite external user</code>" form to send the invite<br>
- Click <strong>Refresh</strong> to see the new user</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/0a69e400-4af9-4ff5-a43f-d9639c2635b2"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/fa805cbc-feaa-4e9f-9662-59ae11f76c6f"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/2f27ec65-3aff-4636-9000-718c0841b78f"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<h3>Step 3: Review the Invitation State</h3>
<p>

- <code>Identity</code> > <code>Users</code> > <code>All Users</code> > <code>Select guest user</code> > <code>Overview</code> > <code>B2B invitation</code><br>
- Select the guest user you've just invited to see the invitation state</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/972f1fc0-d432-4abf-9a3c-f8d3d33a7252"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h3>Step 4: (Optional) Redeem the Invitation as a Guest User</h3>
<p>

- Invite yourself as a guest user (using a personal test email account).<br>
- Check <strong>the guest invitation email and accept the invitation</strong>.<br>
- Request an <strong>email one-time passcode (OTP)</strong>.<br>
- Enter the email OTP and accept the invitation.</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/39b7b5a9-7ef7-4692-9362-4db656eeeadc"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="600px" src="https://github.com/user-attachments/assets/79137846-e002-4c32-a6c6-2dc4f7674713"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/1bcba418-bea1-492c-aa2e-0ac6589d0f30"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<h3>Step 5: Confirm Invitation State Accepted</h3>
<p>

- <code>Identity</code> > <code>Users</code> > <code>All Users</code> > <code>Select guest user</code> > <code>Overview</code> > <code>B2B invitation</code><br>
- Guest user</p>

<h6 align="center"><img width="400px" src="https://github.com/user-attachments/assets/5ca74ec2-afd1-42d5-932a-383011bc3f6a"><br>This image and all the theoretical content of<br>the present article is TryHackMe´s property.</h6>

<p><em>Answer the question below</em></p>

<p>5.1. <em>Can you create a new internal user with your Guest Inviter role? (Yea/Nay)</em><br>
<code>Nay</code></p>

<h2 align="center">Lab-04: Inviting Guest Users</h2>
<p align="center">Rosana´s hands on</p>

<h6 align="center"><img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                    <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""><br><br>
                   <img width="1200px" src=""></h6>

<br><br>
<h2>Task 6 . Security Best Practices: User Settings<a id='6'></a></h2>
<p>Here are some security best practices for "User settings". Remembering the least privilege access principle and limiting certain actions for general users is essential.</p>

<h3>Default User Role Permissions</h3>
<p>By default, in Entra ID, all users can register applications and manage all aspects of the applications they create. Everyone can also consent to apps accessing company data on their behalf. Application Developer role members or other admins should only perform this action, not all users.<br>

- Default: Yes<br>
- Best Practice: No</p>

<h3>Guest User Access Restrictions</h3>
<p>By default, guest users in Entra ID are set to a limited permission level, while the default for member users is the full set of user permissions. When guest access is restricted, guests can view only their own user profile. Permission to view other users isn't allowed even if the guest searches by user principal name(UPN) or objectId. Restricted access also prevents guest users from seeing the membership of their groups.<br>

Guest user accounts are common entry points to get <strong>initial access</strong>, and restricting guest user access to directory objects is vital to reduce the attack surface.</p>

<h6 align="center"><img width="800px" src="https://github.com/user-attachments/assets/55a3389c-5116-47a7-9e4c-b7fac8d55258"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p>If you are interested in learning more about how to exploit guest user access, even if you do not apply the above guest user access restrictions, here is a great <a href="https://aadinternals.com/post/quest_for_guest/">article</a> showcasing the idea in detail from Dr. Nestori Syynimaa (@DrAzureAD), author of the tool <a href="https://aadinternals.com/">AADInternals</a>.<br>

For this technique, you can also refer to the Azure Threat Research Matrix (ATRM) <a href="https://microsoft.github.io/Azure-Threat-Research-Matrix/Reconnaissance/AZT104/AZT104/">AZT104—Gather User Information</a>.</p>

<p><em>Answer the question below</em></p>

<p>6.1. <em>Which user account type is a common entry for malicious actors to get initial access?</em><br>
<code>Guest</code></p>

<br><br>
<h2>Task 7 . Conclusion<a id='7'></a></h2>
<h3>Summary</h3>
<p>In this room, we covered how external identities are represented and implemented in Microsoft Entra ID. Next, we will learn how to secure identities. We have specifically covered the following topics:<br>

- Guest users as external identities<br>
- External collaboration settings<br>
- Inviting guest users<br>
- User settings</p>

<p><em>Answer the question below</em></p>

<p>7.1. <em>I am ready to move on to the <a href="https://tryhackme.com/r/room/entraidzerotrust"> MS Entra ID: Zero Trust</a> room!</em><br>
<code>No answer needed</code></p>

<br><br>
<h1 align="center">Completed</h1>

<p align="center"><img width="900px" src=""><br>
                  <img width="900px" src=""><br>
                  <img width="900px" src=""></p>

                
<h1 align="center">My TryHackMe Journey ・ 2026, February<a id='8'></a></h1>

<div align="center"><p>

|Day<br><br><br> |Streak<br><br><br>|Level<br><br><br>|Type<br><br><br>|Name<br><br><br>                         |Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Brazil<br>Monthly<br><br>|Brazil<br>All<br>Time|Global<br>Monthly<br><br>|Global<br>All<br>Time|
|:--------------:|:----------------:|:---------------:|:--------------:|:----------------------------------------|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|2<br><br>       |28<br><br>        |Easy<br><br>     |🔗<br><br>     |MS Entra ID: External ID                  |                    1,100<br><br>|        1111,1111<br><br>|               90<br><br>|                  60ᵗʰ<br><br>|                     3ʳᵈ<br><br>|                 67ᵗʰ<br><br>|             2ⁿᵈ<br><br>|     

</p></div><br>

<p align="center">
Global All Time: &nbsp; <strong>60</strong>ᵗʰ<br>
<img width="300px" src="https://github.com/user-attachments/assets/1f7641b6-5ad9-487d-8058-0557bf52663e"><br>
Brazil Monthly: &nbsp; <strong>60</strong>ᵗʰ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
Brazil All Time: &nbsp; <strong>3</strong>ʳᵈ<br><img width="450px" hspace="20" src="https://github.com/user-attachments/assets/9527c0d3-78ff-4a1a-9719-18adf54dce74"><img width="450px" src="https://github.com/user-attachments/assets/9527c0d3-78ff-4a1a-9719-18adf54dce74"><br><br>
Global Montlhy: &nbsp; <strong>67</strong>ᵗʰ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
Global All Time: &nbsp; <strong>3</strong>ʳᵈ<br>
<img width="450px" hspace="20" src="https://github.com/user-attachments/assets/9527c0d3-78ff-4a1a-9719-18adf54dce74">
<img width="450px" src="https://github.com/user-attachments/assets/9527c0d3-78ff-4a1a-9719-18adf54dce74"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
