<h2>Jr Penetration Tester Learning Path &nbsp; > &nbsp; 1 · Start Your Cyber Security Journey</h2>
<h1><a href="https://tryhackme.com/room/defensivesecurityintro">Defensive Security Intro</a></h1>

<br>
<h2>Task 1 · Introduction to Defensive Security</h2>
<p>In the previous lesson, we learned about offensive security, which aims to identify and exploit system vulnerabilities to enhance security measures. This includes exploiting software bugs, leveraging insecure setups, and taking advantage of unenforced access control policies, among other strategies. Red teams and penetration testers specialize in these offensive techniques.<br>

In this lesson, we will examine its counterpart, defensive security. It is concerned with two main tasks:<br>

- Preventing intrusions from occurring.<br>
- Detecting intrusions when they occur and responding properly.<br><br>

<strong>Blue teams</strong> are part of the defensive security landscape.<br><br>

Some of the tasks that are related to <strong>defensive security</strong> include:<br>

- <strong>User Cyber Security Awareness</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Training users about cyber security helps protect against attacks targeting their systems.<br>
- <strong>Documenting and Managing Assets</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; We need to know the systems and devices we must manage and protect adequately.<br>
- <strong>Updating and Patching Systems</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Ensuring that computers, servers, and network devices are correctly updated and patched against any known vulnerability (weakness).<br>
- <strong>Setting up Preventative Security Devices</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; firewall and intrusion prevention systems (IPS) are critical components of preventative security. Firewalls control what network traffic can go inside and what can leave the system or network.<br> IPS blocks any network traffic that matches present rules and attack signatures.<br>
- <strong>Setting up Logging and Monitoring Devices</strong> &nbsp; : &nbsp; Proper network logging and monitoring are essential for detecting malicious activities and intrusions. If a new unauthorized device appears on our network, we should be able to detect it.<br>

There is much more to defensive security.<br>
Aside from the above, we will also cover the following related topics:<br>

- <strong>Security Operations Center (SOC)</strong>.<br>
- <strong>Threat Intelligence</strong>.<br>
- <strong>Digital Forensics and Incident Response (DFIR)</strong>.<br>
- <strong>Malware Analysis</strong>.</p>

<p><em>Answer the question below</em></p>

<p>Which team focuses on defensive security?<br>
<code>Blue Team</code></p>

<br>
<h2>Task 2 · Area of Defensive Security</h2>
<p>In this task, we will cover two main topics related to defensive security:<br>

- Security Operations Center (SOC), where we cover Threat Intelligence<br>
- Digital Forensics and Incident Response (DFIR), where we also cover Malware Analysis</p>

<h3>Security Operations Center (SOC)</h3>
<p>A Security Operations Center (SOC) is a team of cyber security professionals that monitors the network and its systems to detect malicious cyber security events. Some of the main areas of interest for a SOC are:

- <strong>Vulnerabilities</strong>  &nbsp; :  &nbsp; Whenever a system vulnerability (weakness) is discovered, it is essential to fix it by installing a proper update or patch. When a fix is unavailable, the necessary measures should be taken to prevent an attacker from exploiting it. Although remediating vulnerabilities is vital to a SOC, it is not necessarily assigned to them.<br>
- <strong>Policy violations</strong>  &nbsp; :  &nbsp; A security policy is a set of rules required to protect the network and systems. For example, it might be a policy violation if users upload confidential company data to an online storage service.<br>
- <strong>Unauthorized activity</strong>  &nbsp; :  &nbsp; Consider the case where a user’s login name and password are stolen, and the attacker uses them to log into the network. A SOC must detect and block such an event as soon as possible before further damage is done.<br>
- <strong>Network intrusions</strong>  &nbsp; :  &nbsp; No matter how good your security is, there is always a chance for an intrusion. An intrusion can occur when a user clicks on a malicious link or when an attacker exploits a public server. Either way, when an intrusion occurs, we must detect it as soon as possible to prevent further damage.<br>

Security operations cover various tasks to ensure protection; one such task is <strong>threat intelligence</strong>.</p>

> <strong>Threat Intelligence</strong>
>> In this context, <code><strong>intelligence</strong></code> refers to information you gather about actual and potential enemies.<br><br>
>> A <code>threat</code> is any action that can disrupt or adversely affect a system.<br><br>
>> <code>Threat</code> <code>intelligence</code> collects information to help the company better prepare against potential adversaries.<br><br>
>> The <code>purpose</code> would be to <code>achieve a threat-informed defence</code>.<br><br>
>> Different companies have different adversaries. Some adversaries might seek to steal customer data from a mobile operator; however, other adversaries are interested in halting the production in a petroleum refinery. Example adversaries include a nation-state cyber army working for political reasons and a ransomware group acting for financial purposes. Based on the company (target), we can expect adversaries.<br><br>
>> <code>Intelligence</code> needs <code>data</code>.<br><br>
>> <code>Data</code> has to be collected, processed, and analyzed.<br><br>
>> <code>Data</code> is <code>collected</code> from local sources such as network logs and public sources such as forums.<br><br>
>> <code>Data</code> <code>processing</code> arranges it into a format suitable for <code>analysis</code>.<br><br>
>> The <code>analysis</code> phase seeks to find more information about the attackers and their motives; moreover, it aims to create a list of <code>recommendations</code> and <code>actionable steps</code>.<br><br>
>> Learning about your adversaries lets you know their <code>tactics</code>, <code>techniques</code>, and <code>peocedured</code>.<br><br>
>> As a <code>result</code> of <code>threat intelligence</code>, we identify the threat actor (adversary) and predict their activity.<br><br>
>> Consequently, we can mitigate their attacks and prepare a response strategy.</p>

<h3>Digital Forensics and Incident Response (DFIR)</h3>
<p>This section is about Digital Forensics and Incident Response (DFIR), and we will cover:<br>

- Digital Forensics<br>
- Incident Response<br>
- Malware Analysis</p>

> <strong>Digital Forensics</strong>
>> <code>Forensics</code> is the application of science to investigate crimes and establish facts.<br><br>
>> With the use and spread of digital systems, such as computers and smartphones, a new branch of forensics was born to investigate related crimes: computer forensics, which later evolved into digital forensics.<br><br>
>> In defensive security, the <code>focus</code> of <code>digital</code> <code>forensics</code> shifts to analyzing evidence of an attack and its perpetrators and other areas such as intellectual property theft, cyber espionage, and possession of unauthorized content.<br><br>
>> Consequently, digital forensics will focus on different areas, such as:<br>
>> - <code>File System</code> : Analyzing a digital forensics image (low-level copy) of a system’s storage reveals much information, such as installed programs, created files, partially overwritten files, and deleted files.<br>
>> - <code>System memory</code> : If the attacker runs their malicious program in memory without saving it to the disk, taking a forensic image (low-level copy) of the system memory is the best way to analyze its contents and learn about the attack.<br>
>> - <code>System logs</code> : Each client and server computer maintains different log files about what is happening. Log files provide plenty of information about what happened on a system. Even if the attacker tries to clear their traces, some traces will remain.<br>
>> - <code>Network logs</code> : Logs of the network packets that have traversed a network would help answer more questions about whether an attack is occurring and what it entails.<br>

<br>

> <strong>Incident Response</strong>
>> An <code>incident</code> usually refers to a data breach or cyber attack; however, in some cases, it can be something less critical, such as a misconfiguration, an intrusion attempt, or a policy violation.<br><br>
>> Examples of a cyber attack include an attacker making our network or systems inaccessible, defacing (changing) the public website, and data breach (stealing company data).<br><br>
>> How would you respond to a cyber attack?<br><br>
>> <code>Incident</code> <code>response</code> specifies the methodology that should be followed to handle such a case.<br><br>
>> The aim is to reduce damage and recover in the shortest time possible. Ideally, you would develop a plan that is ready for incident response.<br><br>
>> The <strong>four major phases of the incident response process</strong> are:<br>
>> - <code>Preparation</code> : This requires a team trained and ready to handle incidents. Ideally, various measures are put in place to prevent incidents from happening in the first place.<br>
>> - <code>Detection</code> : The team has the necessary resources to detect any incident; moreover, it is essential to analyze any detected incident further to learn about its severity.<br>
>> - <code>Containment, Eradication, and Recovery</code> : Once an incident is detected, it is crucial to stop it from affecting other systems, eliminate it, and recover the affected systems. For instance, when we notice that a system is infected with a computer virus, we would like to stop (contain) the virus from spreading to other systems, clean (eradicate) the virus, and ensure proper system recovery.<br>
>> - <code>Post-Incident Actovity</code> : After a successful recovery, a report is produced, and the lesson learned is shared to prevent similar future incidents.<br>

<br>

> <strong>Malware Analysis</strong>
>> <code>Malware</code> stands for malicious software.<br><br>
>> <code>Software</code> refers to programs, documents, and files you can save on a disk or send over the network.<br><br>
>> <code>Malware</code> includes many types, such as:<br>
>> - A <code>virus</code> is a piece of code (part of a program) that attaches itself to a program. It is designed to spread from one computer to another and works by altering, overwriting, and deleting files once it infects a computer. The result ranges from the computer becoming slow to unusable.<br>
>> - <code>Trojan</code> <code>Horse</code> is a program that shows one desirable function but hides a malicious function underneath. For example, a victim might download a video player from a shady website that gives the attacker complete control over their system.<br>
>> - <code>Ransomware</code> is a malicious program that encrypts the user’s files. Encryption makes the files unreadable without knowing the encryption password. The attacker offers the user the encryption password if the user is willing to pay a “ransom.”<br><br>
>> <code>Malware</code> <code>analysis</code> ims to learn about such malicious programs using various means:<br>
>> - <code>Static nalysis</code> works by inspecting the malicious program without running it. This usually requires solid knowledge of assembly language (the processor’s instruction set, i.e., the computer’s fundamental instructions).<br>
>> - <code>Dynamic analysis</code> works by running the malware in a controlled environment and monitoring its activities. It lets you observe how the malware behaves when running.<br>

<p><em>Answer the questions below</em></p>

<p>What would you call a team of cyber security professionals that monitors a network and its systems for malicious events?<br>
<code>Security Operations Center</code></p>

<p>What does DFIR stand for?<br>
<code>Digital Forensics and Incident Response</code></p>

<p>Which kind of malware requires the user to pay money to regain access to their files?<br>
<code>ransomware</code></p>

<br>
<h2>Task 3 · Practical Example of Defensive Security</h2>
<h3></h3>The Scenario</h3>
<p>Let us pretend you are a Security Operations Center (SOC) analyst responsible for protecting a bank. This bank's SOC uses a Security Information and Event Management (SIEM) tool, which gathers security-related information and events from various sources and presents them in one dashboard. If the SIEM finds something suspicious, an alert will be generated.<br><br>
Not all alerts are malicious, however. It is up to the analyst to use their expertise in cyber security to investigate which ones are harmful.<br><br>
For example, you may encounter an alert where a user has failed multiple login attempts. While suspicious, this kind of thing happens, especially if the user has forgotten their password and continues to try to log in.<br><br>
Additionally, there might be alerts related to connections from unknown IP addresses. An IP address is like a home address for your computer on the Internet—it tells other computers where to send the information you request. When these addresses are unknown, it could mean that someone new is trying to connect or someone is attempting unauthorized access.</p>

<h3>Simulating a SIEM</h3>
<p>We have prepared a simplified, interactive simulation of a SIEM system to provide you with a hands-on experience similar to what cyber security analysts encounter.<br><br>
To start this simulation, please click the "View Site" button below.<br><br>
[<strong>View Site</strong>]<br>

This action will open a "static site" on the right side of your screen. Follow the step-by-step instructions provided within the simulation to navigate through the events and locate the "flag." A flag is a series of characters with a format like this: "THM{RANDOM_WORDS}". Use this flag to answer questions from lessons here in TryHackMe, like the one below.</p>
<h3>What's next?</h3>
<p>In this lesson, we've discussed the different subfields (SOC, Threat Intelligence, Malware Analysis, and DFIR) and experienced firsthand how to deal with alerts in a simulated SIEM environment. While we've covered a lot, the depth and complexity of this field mean there's more to learn and explore. The lessons learned here will serve as your foundation as cyber threats evolve, demanding continuous learning, vigilance, and adaptation.<br><br>
Continue learning by checking out the next lesson in this series, "Search Skills." This lesson will teach you valuable techniques for searching for information online to aid your investigations and learning.</p>

<p><em>Answer the questions below</em></p>

<p>What is the flag that you obtained by following along?<br>
<code>THM{THREAT-BLOCKED}</code></p>

<img width="1377" height="941" alt="image" src="https://github.com/user-attachments/assets/d4fd94e0-e691-4798-9f9b-2eb0384fc61d" />

<br>
<br>

<img width="1379" height="944" alt="image" src="https://github.com/user-attachments/assets/7b89aa1d-6039-479f-bb8d-e35a0e92d2bf" />

<br>
<br>

<img width="1381" height="939" alt="image" src="https://github.com/user-attachments/assets/148ab42f-2314-4e8d-9dc2-1c40d3c1c3ab" />

<br>
<br>

<img width="1384" height="936" alt="image" src="https://github.com/user-attachments/assets/b33cccf2-f982-42a5-897f-529e9f4c5e24" />

<br>
<br>

<img width="1378" height="942" alt="image" src="https://github.com/user-attachments/assets/66e12447-a1de-4cea-9dd2-f4586bab0c5e" />

<br>
<br>

<img width="1380" height="940" alt="image" src="https://github.com/user-attachments/assets/272d0d36-2607-48f2-860b-ad96b9276348" />
