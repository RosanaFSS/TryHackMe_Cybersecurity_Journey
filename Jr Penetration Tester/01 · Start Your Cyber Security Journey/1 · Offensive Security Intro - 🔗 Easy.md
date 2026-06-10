<h2>Jr Penetration Tester Learning Path &nbsp; > &nbsp; 1 · Start Your Cyber Security Journey</h2> 
<h1><a href="https://tryhackme.com/room/offensivesecurityintro">Offensive Security Intro</a></h1>
<br>
<h2>Task 1 · What is Offensive Security?</h2>
<p>Which of the following options better represents the process where you simulate a hacker's actions to find vulnerabilities in a system? Hint: It involves breaking into computer systems, exploiting software bugs, and finding loopholes in applications to gain unauthorized access.<br>

- Offensive Security<br>
- Defensive Security<br>

<code>Offensive Security</code></p>

<h2>Task 2 · Hacking your first machine</h2>

<p>Above your account balance, you should now see a message indicating the answer to this question. Can you find the answer you need? Make sure your new balance is a positive number. If your balance still shows a negative value (even after refreshing the page), you may need to transfer more money.<br>
<code>BANK-HACKED</code><br>

- Click <strong>Start Lab Machine</strong>.<br>
- The <strong>Browser</strong> will open on the website <strong>http://fakebank.thm/</strong>.</p>

<img width="1208" height="829" alt="image" src="https://github.com/user-attachments/assets/6f53b32d-4d78-4878-9457-c35be1098f43" />

<br>
<p>
  
- Open <strong>Terminal</strong> (<strong>command-line application</strong>).<br>
- Execute <code>gobuster</code> command to enumerare website pages.<br>- &nbsp;&nbsp; <code>-u</code> &nbsp; : &nbsp; used to state the website we're scanning.<br>- &nbsp;&nbsp; <code>-w</code> &nbsp; : &nbsp; takes a list of words to interate through to find hidden pages.</p>

````bash
ubuntu@tryhackme:~/Desktop$ gobuster -u http://fakebank.thm -w wordlist.txt dir   

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://fakebank.thm/
[+] Threads      : 10
[+] Wordlist     : wordlist.txt
[+] Status codes : 200,204,301,302,307,403
[+] Timeout      : 10s
=====================================================
2026/06/10 16:25:40 Starting gobuster
=====================================================
/images (Status: 301)
/bank-transfer (Status: 200)
=====================================================
2026/06/10 16:25:51 Finished
=====================================================
````

<p>
  
- Navigate to <strong>http://fakebank.thm/bank-transfer</strong>.<br>
- Type <code>2276</code> in the <strong>Send from</strong> field.<br>
- Type <code>8881</code> in the <strong>Send to</strong> field.<br>
- Type <code>2000</code> in the <strong>Amount to send in USD</strong>.<br>
- Click <code>Send Money</code>.</p>

<img width="1207" height="619" alt="image" src="https://github.com/user-attachments/assets/f69b12d6-5fd5-4acd-9e8c-4703ce3ec8f1" />

<br>
<br>

<img width="1203" height="664" alt="image" src="https://github.com/user-attachments/assets/c05ec5c1-1f1c-448e-bcc6-2ab929cc9a72" />

<br>
<p>
  
- Go back to your account webpage <strong>http://fakebank.thm</strong>.</p>

<img width="1303" height="825" alt="image" src="https://github.com/user-attachments/assets/d59a85db-4774-4cbd-9008-0d0453a7bbd3" />

<br>
<h2>Task 3 · Careers in cyber security</h2>
<p>

- <strong>Penetration Tester</strong> &nbsp; : &nbsp; Responsible for testing technology products for finding exploitable security vulnerabilities.<br>
- <strong>Red Teamer</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp; Plays the role of an adversary, attacking an organization and providing feedback from an enemy's perspective.<br>
- <strong>Security Engineer</strong> &nbsp;&nbsp; : &nbsp; Design, monitor, and maintain security controls, networks, and systems to help prevent cyberattacks.</p>
