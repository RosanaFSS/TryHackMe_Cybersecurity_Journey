<h3 align="center">Jr Penetration Tester &nbsp;&nbsp; · &nbsp;&nbsp; Web Application Vulnerabilities I</h3><h1  align="center"><a href="https://tryhackme.com/room/sqlinjectionintroduction">SQL Injection Introduction</a></h1>
<p align="center">Learn how to detect and exploit SQL Injection vulnerabilities.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/d812ad5d-de14-4c80-a6c6-947d0a0ee09e"><br>If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAY%2027-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p><br>

<h2>Task 1 - Introduction</h2>

<p><em>Answer the question below</em></p>
<p>1.1. I am ready to learn about SQL Injection!<br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 - SQL Essentials for Injection</h2>
<p><em>Answer the questions below</em></p>

<p>2.1. What SQL statement combines results from two SELECT queries into one result set?<br>
<code>UNION</code></p>

<p>2.2. What built-in database contains metadata about all other databases, tables, and columns in MySQL?<br>
<code>information_schema</code></p>

<br>
<h2>Task 3 - What is SQL Injection?</h2>
<p><em>Answer the questions below</em></p>

<p>3.1. What character is commonly used as a first test when probing for SQL Injection?<br>
<code>'</code></p>

<p>3.2. What type of SQL Injection returns results directly in the web page?<br>
<code>In-Band</code></p>

<br>
<h2>Task 4 - In-Band SQL Injection</h2>
<p><em>Answer the questions below</em></p>

<p>4.1. What subtype of In-Band SQLi relies on database error messages to extract information?<br>
<code>Error-Based</code></p>

<p>4.2. What SQL function returns the name of the current database in MySQL?<br>
<code>database()</code></p>

<br>
<h2>Task 5 - Blind SQL Injection: Authentication Bypass</h2>
<p><em>Answer the question below</em></p>

<p>5.1. What boolean condition is commonly injected to make a WHERE clause always evaluate to true?<br>
<code>1=1</code></p>

<br>
<h2>Task 6 - Blind SQL Injection: Boolean and Time-Based</h2>
<p><em>Answer the question below</em></p>

<p>6.1. What MySQL function causes a deliberate time delay in a query's response?<br>
<code>SLEEP</code></p>

<br>
<h2>Task 7 - Out-of-Band SQL Injection</h2>
<p><em>Answer the questions below</em></p>

<p>7.1. What protocol beginning with D is commonly used to exfiltrate data in Out-of-Band SQLi?<br>
<code>DNS</code></p>

<p>7.2. What MSSQL stored procedure can be used to trigger DNS lookups for data exfiltration?<br>
<code>xp_dirtree</code></p>

<br>
<h2>Task 8 - Remediation and Prevention</h2>
<p><em>Answer the questions below</em></p>

<p>8.1. What is the primary and most effective defence against SQL Injection?<br>
<code>Prepared Statements</code></p>

<br>
<h2>Task 9 - Practical: SQL Injection</h2>

<img width="875" height="520" alt="image" src="https://github.com/user-attachments/assets/b76a7bab-7a3c-46e1-a375-4e752e62da5f" />

<br>
<br>

<img width="871" height="525" alt="image" src="https://github.com/user-attachments/assets/f547b62c-a4f9-441d-8aa8-781a9986bc7c" />

<br>
<br>

<img width="863" height="517" alt="image" src="https://github.com/user-attachments/assets/45a25212-662c-47e8-abcb-4256d4cd0217" />

<br>
<br>

<img width="866" height="483" alt="image" src="https://github.com/user-attachments/assets/cbe4aad1-f7b7-442c-a414-480d2020b50c" />

<br>
<br>

<img width="849" height="503" alt="image" src="https://github.com/user-attachments/assets/5868678a-b192-42b4-bb33-860553c2ca58" />

<br>
<br>

<img width="861" height="518" alt="image" src="https://github.com/user-attachments/assets/4a1c554b-5f7c-47f9-8262-867d6f35c58b" />


<br>
<br>

<img width="867" height="523" alt="image" src="https://github.com/user-attachments/assets/44d8c10d-af99-4a63-b2bc-008e85807359" />

<br>
<br>
<p>

- Enter <strong>martin</strong>'s password and login<p/>


<img width="868" height="524" alt="image" src="https://github.com/user-attachments/assets/1b0681f8-b051-41ce-9fec-df064eff9fdb" />

<br>
<br>

<img width="862" height="519" alt="image" src="https://github.com/user-attachments/assets/248f0bd7-2c4a-48d1-9b70-cd3a8e4bf5a0" />

<br>
<br>

<img width="865" height="488" alt="image" src="https://github.com/user-attachments/assets/b3076d50-2582-49d3-837d-a779c37615ee" />

<br>
<br>
<h3>Level 3</h3>
<p>
- Click <code>Level 3</code>.<br>
- Uncover the second flag.</p>


<img width="862" height="519" alt="image" src="https://github.com/user-attachments/assets/9f60774c-fe3a-4936-8413-ad7d097f9dc9" />

<br>
<br>


<p><code>https://website.thm/checkuser?username=admin123' UNION SELECT 1,2,3 where database() like 'sqli_three%';--</code></p>


<img width="863" height="491" alt="image" src="https://github.com/user-attachments/assets/f210ac1f-519c-42be-bf2f-641f8287425f" />



<p><code>admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'u%';--</code></p>


<h3>Level 4</h3>


<img width="869" height="490" alt="image" src="https://github.com/user-attachments/assets/5f4f85d5-d0d9-4f2e-8f4f-f6cf8910b523" />

<br>
<br>

<img width="867" height="444" alt="image" src="https://github.com/user-attachments/assets/832b3aac-8977-4a1d-857b-35bb5fb5d8bd" />


<br>
<br>

<h3>Level 5</h3>

<img width="866" height="195" alt="image" src="https://github.com/user-attachments/assets/b3f7c7f0-4698-4f4e-9305-167084c0bc72" />

<br>
<br>

<p><em>Answer the questions below</em></p>

<p>9.1. What is the flag after completing Level 1?<br>
<code>THM{---_--------_----}</code></p>

<p>9.2. What is the flag after completing Level 2?<br>
<code>THM{---_--------_----}</code></p>

<p>9.3. What is the flag after completing Level 3?<br>
<code>THM{---_--------_----}</code></p>

<p>9.4. What is the flag after completing Level 4?<br>
<code>THM{---_--------_----}</code></p>

<h2>Task 10 - Conclusion</h2>
<h6 align="center"><img width="1200px" src="https://github.com/user-attachments/assets/b7ed9123-7288-46bc-8091-e6fac989b624"><br>This image and all the theoretical content of the present article is TryHackMe´s property.</h6>

<p><em>Answer the question below</em></p>

<p>10.1. I have completed the SQL Injection room!<br>
<code>No answer needed</code></p>

<h2 align="center">Completed</h2>
<p align="center">                                                       <img width="1000px" src="https://github.com/user-attachments/assets/e9997e91-3a3e-4c1e-adba-79342841f4de"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/47a12ceb-e563-4a3f-9163-6497ae0dd1ce"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/bfe2fe03-0f68-4577-8705-7b531f353937"></p>

<h2 align="center">My TryHackMe Journey &nbsp; · &nbsp; 2026, May</h2>
<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|27<br><br>      |109<br><br>       |SQL Injection Introduction<br>     |<br><br>    |<br><br>  | 1,218<br><br>| 177,733<br><br>| 97<br><br>| 9ᵗʰ<br><br>| 5%<br><br>| 1ˢᵗ<br><br>| 3ʳᵈ<br><br>|
|23<br><br>      |109<br><br>       |[Content Discovery](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/4%20%C2%B7%20Web%20Application%20Security%20Fundamentals/2%20%C2%B7%20Content%20Discovery.md)<br>              |<br><br>    |<br><br>  | 1,217<br><br>| 177,613<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 40ᵗʰ<br><br>| 1ˢᵗ<br><br>| 2ⁿᵈ<br><br>|
|23<br><br>      |109<br><br>       |[Walking An Application](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/4%20%C2%B7%20Web%20Application%20Security%20Fundamentals/1%20%C2%B7%20Walking%20an%20Application%20-%20%F0%9F%94%97%20Easy.md)<br>         |<br><br>    |<br><br>  | 1,216<br><br>| 177,517<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 41ˢᵗ<br><br>| 1ˢᵗ<br><br>| 2ⁿᵈ<br><br>|
|23<br><br>      |109<br><br>       |[Nmap - Topic Transition Recap](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/3%20%C2%B7%20Nmap/5%20%C2%B7%20Transition%20Topic%20Recap.md)<br>         |<br><br>    |<br><br>  | 1,215<br><br>| 177,445<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 39ᵗʰ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|
|23<br><br><br><br><br>      |109<br><br><br><br><br>       |[Penetration Testing Foundations - Topic Transition Recap](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/6%20%C2%B7%20Topic%20Transition%20Recap.md)<br>         |<br><br><br><br><br>    |<br><br><br><br><br>  | 1,215<br><br><br><br><br> | 177,397<br><br><br><br><br> | 96<br><br><br><br><br> | 8ᵗʰ<br><br><br><br><br>| 40ᵗʰ<br><br><br><br><br>| 1ˢᵗ<br><br><br><br><br>| 1ˢᵗ<br><br><br><br><br>|
|23<br><br><br>  |109<br><br><br>   |[Penetration Testing Frameworks](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/5%20%C2%B7%20Penetration%20Testing%20Frameworkds%20-%20%F0%9F%94%97%20Easy.md)<br> |Easy<br><br><br>|🔗<br><br><br>| 1,215<br><br><br>| 177,349<br><br><br>| 96<br><br><br>| 8ᵗʰ<br><br><br>| 43ʳᵈ<br><br><br>| 1ˢᵗ<br><br><br>| 1ˢᵗ<br><br><br>|
|22<br><br>      |109<br><br>       |[Dive Into Pentesting](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/3%20%C2%B7%20Dive%20Into%20Pentesting%20-%20%F0%9F%94%97%20Easy.md)<br>           |Easy<br><br>|🔗<br><br>| 1,214<br><br>| 177,205<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 41ˢᵗ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|
|22<br><br>      |109<br><br>       |[Guided Pentest: Infrastructure](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-&-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/2%20%C2%B7%20Guided%20Pentest:%20Infrastructure%20-%20%F0%9F%94%97%20Easy.md)<br> |Easy<br><br>|🔗<br><br>| 1,213<br><br>| 177,085<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 40ᵗʰ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|
|22<br><br>      |109<br><br>       |[Guided Pentest: Web](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/1%20%C2%B7%20Guided%20Pentest%3A%20Web%20-%20%F0%9F%94%97%20Easy.md)<br>            |Easy<br><br>|🔗<br><br>| 1,212<br><br>| 177,045<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 41ˢᵗ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|

</h6></div>

<p align="center">Capability Score &nbsp;&nbsp; <strong>109</strong> <br><img width="1000px" src="https://github.com/user-attachments/assets/e1415476-ac10-4bf1-a95d-90967831db33"><br>
                  Stats                                              <br><img width="300px"  src="https://github.com/user-attachments/assets/dfccdc44-032a-4cd9-9f06-34e125ff29b4"><br>
                  Global All Time &nbsp;&nbsp;  9ᵗʰ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/e6580134-53f6-4a73-bd48-ec4add7b85ee"><br>
                  Global Monthly &nbsp;&nbsp;  Top 5%                <br><img width="1000px" src="https://github.com/user-attachments/assets/fcdd45ed-6aa1-47eb-a1fe-098ad7201b46"><br>
                  Brazil All Time &nbsp;&nbsp;  1ˢᵗ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/8187069b-22a9-4bc0-b8a0-3aa443b19290"><br>
                  Brazil Monthly &nbsp;&nbsp;   3rᵈ                  <br><img width="1000px" src="https://github.com/user-attachments/assets/ef55d86d-0630-47cf-a8f7-bca867b3e7a3"></p>

<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
