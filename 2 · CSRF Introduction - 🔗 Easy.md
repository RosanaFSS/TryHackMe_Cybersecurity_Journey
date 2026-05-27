<h3 align="center">Jr Penetration Tester &nbsp;&nbsp; · &nbsp;&nbsp; Web Application Vulnerabilities I</h3><h1  align="center"><a href="[https://tryhackme.com/room/contentdiscoveryx](https://tryhackme.com/room/csrfintroduction)">CSRF Introduction </a></h1>
<p align="center">Understand CSRF vulnerability and practice exploiting insecure state-changing requests.<br>
<img width="1200px" src="https://github.com/user-attachments/assets/02878276-7637-4e33-9f3f-8dff91cc8bc7"><br>If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20APR%206-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p><br>
 
<h2>Task 1 - Introduction</h2>
<p><em>Answer the question below</em></p>
<p>1.1. I have successfully connected to the machine.<br><code>No answer needed</code></p>

<br>
<h2>Task 2- What is CSRF</h2>
<p><em>Answer the questions below</em></p>
<p>2.1. What relationship between the browser and the web application does a CSRF attack abuse?<br><code>Trust</code></p>
<p>2.2. What does the browser automatically include with requests after login?<br><code>Cookies</code></p>

<br>
<h2>Task 3 - Why CSRF Works</h2>
<p><em>Answer the question below</em></p>
<p>3.1. What type of action is usually required for a CSRF attack to succeed?<br><code>State-changing</code></p>
<br>
<h2>Task 4 - Finding CSRF Vulnerabilities</h2>
<p><em>Answer the questions below</em></p>
<p>4.1. What HTTP request method do many developers incorrectly believe prevents CSRF?<br><code>POST</code></p>
<p>4.2. What mechanism is commonly used to protect applications from CSRF attacks?<br><code>CSRF tokens</code></p>
<br>
<h2>Task 5 - Exploitation using HTML Forms</h2>
<p><em>Answer the questions below</em></p>
<p>5.1. What is the flag value after updating the email to attacker@evilmail.thm?<br><code>THM{Got_The_Evil_Email001}</code></p>
<p>5.2. What is the flag value after updating the email to special@evilmail.thm?<br><code>THM{My_Special_Email007}</code></p>
<br>
<img width="1199" height="458" alt="Screenshot 2026-04-06 143624" src="https://github.com/user-attachments/assets/7b33c2ae-92ec-4307-980a-09d3c7542759" />

<br>
<br>

<img width="1249" height="481" alt="Screenshot 2026-04-06 143800" src="https://github.com/user-attachments/assets/380b2f72-36f6-408d-8109-d5e005f59e2e" />

<br>
<br>

<img width="1195" height="781" alt="Screenshot 2026-04-06 143857" src="https://github.com/user-attachments/assets/92b9fe59-a328-430b-9e1d-597772f93d29" />

<br>
<br>

<img width="1191" height="794" alt="Screenshot 2026-04-06 143906" src="https://github.com/user-attachments/assets/ff4c4041-88bd-4422-987e-2b02e9c3b759" />

<br>
<br>

<img width="1191" height="480" alt="Screenshot 2026-04-06 144040" src="https://github.com/user-attachments/assets/9621d1bf-34c4-491d-822e-b8976076f59e" />

<br>
<br>

<img width="1730" height="660" alt="Screenshot 2026-04-06 144517" src="https://github.com/user-attachments/assets/d87150d5-1d54-44ba-93b0-459dc9a077fa" />

<br>
<br>

<img width="1730" height="787" alt="Screenshot 2026-04-06 144938" src="https://github.com/user-attachments/assets/8498805b-cc73-4c31-af99-ddfe6b31e43a" />

<br>
<br>

<img width="1732" height="686" alt="Screenshot 2026-04-06 145048" src="https://github.com/user-attachments/assets/9867f968-8702-4fd8-9dbe-05cd4cf55942" />

<br>
<br>

<img width="1740" height="118" alt="Screenshot 2026-04-06 145359" src="https://github.com/user-attachments/assets/078e79d2-92de-4da2-a787-62bf527fa5c6" />

<br>
<br>
<h2>Task 6 - Exploitation over Weak Tokens</h2>
<p><em>Answer the questions below</em></p>
<p>6.1. What is the flag value after demoting the user from admin to staff? Visit the dashboard page to get the flag.<br><code>THM{Weak_CSRF_Role_001}</code></p>
<p>6.2. In the above example, what is the name of the encoding scheme used by the developer for encoding CSRF tokens?<br><code>base64</code></p>

<img width="1737" height="611" alt="Screenshot 2026-04-06 145417" src="https://github.com/user-attachments/assets/6a5fd460-2ca9-4084-8b29-b0bf88cadfa7" />

<br>
<br>

<img width="1496" height="374" alt="Screenshot 2026-04-06 150313" src="https://github.com/user-attachments/assets/4e50958c-edfb-44e3-8f30-4280664737ca" />

<br>
<br>

<img width="1724" height="371" alt="Screenshot 2026-04-06 150531" src="https://github.com/user-attachments/assets/fe5e7365-7284-43ee-ae88-4c11f20dfd1a" />

<br>
<br>

<img width="1716" height="612" alt="Screenshot 2026-04-06 150612" src="https://github.com/user-attachments/assets/f2fa2c10-97a3-4770-804e-e99491963a16" />

<br>
<br>
<h2>Task 7 - Best Practices</h2>
<p><em>Answer the question below</em></p>
<p>7.1. I have understood the best practices.<br><code>No answer needed</code></p>

<br>
<h2>Task 8 - Conclusion</h2>
<p>In this room, we explored the concept of CSRF and how attackers can abuse a victim’s authenticated session to perform unintended actions. Through practical exercises, we observed that simple actions, such as submitting a hidden form or interacting with a webpage element, can trigger malicious requests.<br>

We also saw that even applications that implement CSRF protection can remain vulnerable if the protection mechanism is weak or predictable. By reversing a poorly designed token, you recreated a valid request and successfully bypassed the defence. Finally, we reviewed important practices that pentesters should follow when identifying CSRF vulnerabilities during assessments.<br>

Understanding how these attacks work and how they can be detected is essential for both security testers and developers building more secure applications.</p>
<p><em>Answer the question below</em></p>
<p>8.1. I have successfully completed the room.<br><code>No answer needed</code></p>

<h2 align="center">Completed</h2>
<p align="center">                                                       <img width="500px" src="https://github.com/user-attachments/assets/c96b3df9-3afb-4add-941b-49a6a4a1f9fc"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/17f26ca1-c19c-4e58-9338-fe9415d6c807"><br>
                                                                         <img width="1000px" src="https://github.com/user-attachments/assets/87161c99-558d-416e-b0f3-7b68c4087509"></p>
                                                                       
<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
