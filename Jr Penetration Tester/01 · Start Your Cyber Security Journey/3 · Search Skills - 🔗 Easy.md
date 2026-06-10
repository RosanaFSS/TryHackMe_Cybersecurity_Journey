<h2>Jr Penetration Tester Learning Path &nbsp; > &nbsp; 1 · Start Your Cyber Security Journey</h2> 
<h1><a href="https://tryhackme.com/room/searchskills">Search Skills</a></h1>
<br>
<h2>Task 1 · Introduction</h2>
<p>This room will show you examples of popular websites and services that can be used to gather information for a variety of cyber security purposes, both offensive and defensive.<br><br>
Whether you're hunting down an exploit, trying to understand how a tool works, tracking a threat actor, knowing where to search is just as important as knowing what to search for.<br><br>
Using the internet and it's resources effectively is a critical skill in cyber security. <br><br>
If you're ready, let's explore some of these services below!</p>

<p><em>Answer the question below</em></p>

<p>I'm ready to begin!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 · Shodan (TryScanMe)</h2>
<p>Shodan is often described as a search engine for the Internet of Things (IoT), but that undersells it.<br><br>
Shodan continuously scans the internet, searching for networking equipment, industrial control systems, traffic cameras, and virtually anything else with a public network connection to see what's running and where.<br><br>
For example, searching <code>apache 2.4.1</code> will return a list of servers advertising that version in their HTTP headers, broken down by country, organisation, and port. During a penetration test or vulnerability assessment, that kind of visibility is extremely useful, particularly when paired with a known CVE affecting that version.<br><br>
Shodan also supports its own query filters, which let you narrow results significantly:</p>

<div><p>

|<strong>Filter</strong> |<strong>Description</strong>                         |<strong>Example</strong>            |
|:-----------------------|:----------------------------------------------------|:-----------------------------------|
|<code>country</code><br><br>|Restrict results to a specific country code.<br><br>     |<code>country:IE</code><br><br>         |
|<code>port</code><br><br>  |Filter by a specific port number or a range.<br><br>      |<code>port:22</code><br><br>            |
|<code>org</code><br><br>  |Scope results in a named organisation or ASN Identifier<br>Who owns a range of IP addresses).|<code>AS7224</code><br>(Amazon Web Services)<br>|
|<code>hostname</code><br><br>|Match against a specific hostname or domain.<br><br>     |<code>hostname:fakebank.thm</code><br><br> |

</div></p>

<h3>Practical</h3>
<p>Click the view site button below to start our Shodan simulation: [View Site]</p>
<h4>You'll need to...</h4>
<p>
  
- Search for the term <code>apache</code>code> in the search bar of TryScanMe. Apache is a popular type of web server.<br>
- Review the first entry within the list.<br>
- Use that information to answer the question below.</p>

<p><em>Answer the question below</em></p>

<p>What domain is associated with the IP address <code>185.243.115.47</code>?<br>
Hint: This is located within the entry as "domain" and ends in ".thm". There is a copy button next to it.<br>
<code>tryhackme.thm</code></p>

<img width="1390" height="306" alt="image" src="https://github.com/user-attachments/assets/c9580577-c4a5-4c2c-970f-3498a9cd6cef" />

<br>
<br>

<img width="1390" height="936" alt="image" src="https://github.com/user-attachments/assets/10938811-5110-40b4-870b-3c435759aed9" />

<br>
<h2>Task 3 · VirusTotal (TryDetectMe)</h2>
<p>VirusTotal collates results from over 70 antivirus engines and website scanners into a single interface. Submit a file, a URL, a domain, or a file hash. VirusTotal will tell you whether any of those engines have flagged it as malicious or not.<br><br>
Whilst not foolproof, VirusTotal is a popular resource in the blue teaming community for obtaining a general consensus on suspicious files and links, as well as for gathering intelligence on new threats on the move.</p>

<h3>Practical</h3>
<p>Click the view site button below to start our VirusTotal simulation: [View Site]</p>
<h4>You'll need to...</h4>
<p>
  
- Search for the file <code>invoice_payment.exe</code>on TryDetectMe.<br>
- Review the information that has been provided. You will see a list of security vendors that have identified the file we have provided as dangerous.<br>
- Determine how many security vendors have identified the file as dangerous to answer the question below.</p>

<p><em>Answer the question below</em></p>

<p>How many security vendors have identified the file as dangerous?<br>
You can see a total count at the top of the page.<br>
<code>52</code></p>

<img width="1389" height="311" alt="image" src="https://github.com/user-attachments/assets/dd5c1868-5898-48ab-8c08-6c2e7d9a6b95" />

<br>
<br>

<img width="1370" height="941" alt="image" src="https://github.com/user-attachments/assets/823a8a63-7544-4c26-9d31-67e119a99fa1" />


<br>
<h2>Task 4 · Vulnerability Databases (CVE)</h2>
<p>The <strong>Common Vulnerabilities and Exposures (CVE)</strong> programme is the closest thing the industry has to a universal dictionary of known vulnerabilities.<br><br>
Each confirmed vulnerability is assigned a unique identifier in the format <code>CVE-YEAR-NUMBER</code>, such as <code>CVE-2025-55182</code>. If the vulnerability is impactful enough, it may even get a moniker. You may have heard of vulnerabilities such as Heartbleed, React2Shell, and Log4Shell. These vulnerabilities are given a score (<strong>CVSS</strong>) based on a variety of factors, such as:<br>

- <strong>Impact</strong> - What damage can this vulnerability lead to?<br>
- <strong>Complexity</strong> - Is the vulnerability easy to exploit or not?<br> 
- <strong>Availability</strong> - How likely is it that someone can exploit this?</p>

````txt
Organisations use scoring like this to prioritise their level of risk. Addressing the highest scoring first.
`````

<p>These identifiers function as a reference point among vendors, researchers, security tools, and documentation, ensuring that everyone discussing a vulnerability refers to the same issue. Websites like ExploitDB compile this information alongside "Proof of Concepts" (PoCs), which are scripts capable of demonstrating the vulnerability.</p>

<h3>Practical</h3>
<p>For this section, you will be interacting with TryHackMe's Vulnerability Database. Click the "Show Site" button below to get started.<br>
[View Site]</p>
<h4>You'll need to...</h4>
<p>
  
- Search the Vulnerability Database for <code>CVE-2026-1337</code>.<br>
- Review the details about the vulnerability.<br>
- Find the CVSS scoring to answer the question.</p>

<p><em>Answer the question below</em></p>

<p>What <strong>CVSS</strong> (Common Vulnerability Scoring System) classification did the vulnerability get?<br>
Hint: This number is located in the "CVSS SCORING" heading towards the top of the page.<br>
<code>10</code></p>

<img width="1378" height="328" alt="image" src="https://github.com/user-attachments/assets/1c746d86-97bd-4669-a7b0-460427010610" />

<br>
<br>

<img width="1362" height="944" alt="image" src="https://github.com/user-attachments/assets/7ebc552c-04fb-45b4-8a4f-2352df9b663a" />

<br>
<h2>Task 5 · Technical Documentation (MAN)</h2>
<h3>Product and Tool Documentation</h3>
<p>Each major security tool or platform provides its own documentation, which is the most reliable and up-to-date than any third-party tutorials.<br><br>

When you're troubleshooting unexpected behaviour or trying to understand how to use a tool in a certain way, the official documentation should always be your first stop - not your last.</p>

<h3>Linus Man Pages</h3>
<p>Have you ever come across a command-line tool or command that you're not familiar with? Linux <strong>MAN</strong>ual pages have got your back. These pages serve as documentation that you can read within your terminal about any command on Linux, and a majority of cybersecurity tooling <br><br>

To view the manual page, run <code>man <command></code>. For example:</p>

<p><em>A Snipped of the MAN page of "nc"</em></p>

````bash
user@thm$ man nc
NC
                                                                                  
NAME
       nc — arbitrary TCP and UDP connections and listens

SYNOPSIS
       nc  [-46bCDdFhklNnrStUuvZz]  [-I  length]  [-i  interval]  [-M  ttl] [-m minttl] [-O length] [-P proxy_username] [-p source_port] [-q seconds] [-s sourceaddr] [-T keyword] [-V rtable] [-W recvlimit] [-w timeout]
          [-X proxy_protocol] [-x proxy_address[:port]] [destination] [port]
````

<h3>Practical</h3>
<p>For this section of the practical, you will be interacting with a simulation of these manual pages. Click the "Show Site" button below to get started.<br>
[View Site]</p>
<h4>You'll need to...</h4>
<p>
  
- Search the MANual pages for the tool <code>nc</code> (netcat).<br>
- Find the example command that allows you to open a connection for <code>host.example.com on port 42</code> (<strong>this is located at the bottom of the output</strong>).<br>
- Copy and paste the command to answer the question below.</p>

<p><em>Answer the question below</em></p>

<p>What is the example command?<br>
Hint: You will need to copy the example command for connecting to host.example.com on port 42, located at the bottom of the page.<br>
<code>nc host.example.com 42</code></p>

<img width="1375" height="183" alt="image" src="https://github.com/user-attachments/assets/7c7f78e5-18a9-4cca-9676-1f569f8a9896" />

<br>
<br>

<img width="1370" height="936" alt="image" src="https://github.com/user-attachments/assets/dd251802-95da-41b1-acd5-d691693389e4" />

<br>
<br>

<img width="1362" height="937" alt="image" src="https://github.com/user-attachments/assets/9fc41a95-7e4d-4423-bee5-d98e92ae76f8" />

<br>
<h2>Task 6 · GitHub</h2>
<p>GitHub can be a great resource for staying updated on the latest threats and vulnerabilities. Researchers often publish proof-of-concept (PoC) code, exploitation tools, and detailed technical reports there, which are usually faster than official channels.<br><br>
Searching for a CVE identifier (e.g., <code>CVE-2026-1337</code>) directly on GitHub often reveals repositories containing PoC code, scanner scripts, or detailed analyses of the vulnerability.<br><br>
That said, not all PoCs are equally reliable. Some are incomplete, some are intentionally flawed, and occasionally a "PoC" repository is malicious itself. Always verify what you're about to execute.</p>
<h3>Practical</h3>
<p>For the final portion of the practical, you will be interacting with a repository that contains an. Click the "Show Site" button below to get started.<br>
[View Site]</p>
<h4>You'll need to...</h4>
<p>
  
- Review the repository for the fictious CVE <code>CVE-2026-1337</code>.<br>
- Read the README about the vulnerability.<br>
- Use that information to answer the question below.</p>

<p><em>Answer the question below</em></p>

<p>What is the name of the script in the repository that will demonstrate the vulnerability?<br>
Hint: You can see a list of files at the top of the page. Other files include README.md.<br>
<code>exploit.py</code></p>

<img width="1388" height="285" alt="image" src="https://github.com/user-attachments/assets/2fb7f7b4-3c67-43de-ad1e-b420d34257f4" />

<br>
<br>

<img width="1363" height="936" alt="image" src="https://github.com/user-attachments/assets/02c2b33b-5997-4024-8543-1a3d62711fbb" />

<br>
<br>

<img width="1354" height="943" alt="image" src="https://github.com/user-attachments/assets/569a25b6-cc26-4b15-b089-cb4b5efc3182" />
