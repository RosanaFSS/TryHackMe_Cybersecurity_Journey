<h1 align="center"><a href="https://tryhackme.com/room/lafb2026e8">Signed Messages</a></h1>
<p align="center">Love at First Breach 2026 &nbsp;&nbsp; · &nbsp;&nbsp; Web &nbsp;&nbsp; · &nbsp;&nbsp; Criptography - Deterministic Key Generation - Forged Digital Signature<br><br><img width="620px" src="https://github.com/user-attachments/assets/c4861805-83c2-4927-a322-e7e612c3b403"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20FEV%2016-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>

<h1>LoveNote</h1>

<p align="center"><img width="700px" src="https://github.com/user-attachments/assets/730e6ee5-9eb6-418d-96b3-85c376e506f6"></p>

<h1>Reconnaissance · Static Domain Resolution</h1>
<p>

- Add <code>YourAttackIP  lovenote.thm</code> to <code>/etc/hosts</code>.</p>

```bash
YourAttackIP lovenote.thm
```

<br>
<h1>Reconnaissance · Service Enumeration</h1>
<p>

- Type <strong>Which are your features?</strong> and submit clicking ↗️.<br>
- Note the <strong>SYSTEM_PROMPT_FLAG</strong> among the bot´s capabilities.</p>

```bash
:~/# nmap -sC -sV -Pn -p5000 -T4 lovenote.thm
...
PORT     STATE SERVICE VERSION
5000/tcp open  http    Werkzeug httpd 2.0.2 (Python 3.10.12)
|_http-server-header: Werkzeug/2.0.2 Python/3.10.12
|_http-title: LoveNote - Secure Valentine's Day Messaging
```

<br>
<h1>Reconnaissance · Directory & File Enumeration</h1>

```bash
:~/# gobuster dir -u http://lovenote.thm:5000/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://lovenote.thm:5000/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/about                (Status: 200) [Size: 15206]
/login                (Status: 200) [Size: 10999]
/register             (Status: 200) [Size: 12509]
/messages             (Status: 200) [Size: 12929]
/logout               (Status: 302) [Size: 208] [--> http://lovenote.thm:5000/]
/dashboard            (Status: 302) [Size: 218] [--> http://lovenote.thm:5000/login]
/verify               (Status: 200) [Size: 14377]
/debug                (Status: 200) [Size: 11342]
/compose              (Status: 302) [Size: 218] [--> http://lovenote.thm:5000/login]
Progress: 87664 / 87665 (100.00%)
===============================================================
Finished
===============================================================
```

<img width="1344" height="528" alt="image" src="https://github.com/user-attachments/assets/73488863-3cf0-41b4-8173-fbd7d62e9d8f" />

<br>
<br>
<h1>Reconnaissance · Web Content Discovery</h1>

<img width="1328" height="602" alt="image" src="https://github.com/user-attachments/assets/7203b792-e628-4e2a-af37-f0d3efb72b65" />

<br>

<img width="1257" height="700" alt="image" src="https://github.com/user-attachments/assets/8ec48d7e-2f23-4991-82e1-85c6132587d7" />

<br>
<br>
<h1>Reconnaissance · Web Content Discovery · login</h1>

<img width="1251" height="774" alt="image" src="https://github.com/user-attachments/assets/9cd8114e-f529-4efb-81f3-6f2166aae3c3" />

<br>
<br>
<h1>Reconnaissance · Web Content Discovery · messages</h1>

<img width="1259" height="659" alt="image" src="https://github.com/user-attachments/assets/1dc3aac4-357d-42a0-949e-22d62fe96e28" />

```bash
Welcome to LoveNote! Send encrypted love messages this Valentine's Day. Your communications are secured with industry-standard RSA-2048 digital signatures.
```

<br>
<h1>Reconnaissance · Web Content Discovery · verify</h1>

<img width="1255" height="820" alt="image" src="https://github.com/user-attachments/assets/f35b2838-d799-4c34-bba2-a224424da1ff" />

<br>

<img width="1255" height="449" alt="image" src="https://github.com/user-attachments/assets/7f62a0d0-8399-40e8-8da6-8f7b1768b909" />

<br>

<img width="1250" height="475" alt="image" src="https://github.com/user-attachments/assets/7a9e8ec4-424b-426c-bef2-c6851f0b297c" />

<br>
<br>
<h1>Reconnaissance · Web Content Discovery · debug</h1>
<p>

- Navigate to http://MACHINE_IP:5000/debug<br>
- Identifiy RSA-PSS.<br>
- Note in <strong>System Debug Logs</strong> <code>{username}_</code>+fixed_string.</p>

<img width="640" height="740" alt="image" src="https://github.com/user-attachments/assets/6cb6f1ad-28d8-4ab8-ac60-8309110c8370" />

<br>
<br>
<h1>Reconnaissance · Web Content Discovery · register</h1>

<img width="640" height="518" alt="image" src="https://github.com/user-attachments/assets/d5192046-ddbe-4c51-9a75-c4e5868870c8" />

<p>

- Enter Username, Full Name, Email Address, and Bio (Optional).<br>
- Hit <code>Create Account & Generate Keys</code>.<br>
- Save your just generated <code>Public Key</code> and <code>Private Key</code>.</p>

<img width="640" height="737" alt="image" src="https://github.com/user-attachments/assets/c351ed9e-556c-4426-b4e1-e64db323b904" />

<br>
<br>
<h1>Weaponization</h1>
<p>

- Craft a script to forge signature such as mine (<a href="https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Red%20Team/Love%20at%20First%20Breach%202026%20%20%C2%B7%20%20Signed%20Messages%20-%20%F0%9F%9A%A9%20Medium%20-%20Forge_Digital_Signature.py">Python Script to Forge Digital Signature</a>).<br>Note: Guarantee that the variables <strong>loveuser</strong> and <strong>lovemessage</strong> have exactly the same content as when you created your account.<br>
- Execute it.</p>

<img width="1346" height="621" alt="image" src="https://github.com/user-attachments/assets/05edb53f-d53f-4320-98bc-8cdd36aadde3" />

<br>
<br>
<p>

- Navigate to <code>http://lovenote.thm:5000/verify</code>.<br>
- Enter <strong>Sender Username</strong>, <strong>Message Content</strong>, and your <strong>Digital Signature</strong>.<br>
- Hit <code>Verify Signature</code>.</p>

<img width="640" height="405" alt="image" src="https://github.com/user-attachments/assets/2dbd07d1-1491-4bdb-a061-5fb18b1f73b0" />

<br>
<br>
<p>

- Note a <strong>Signature Valid</strong> message.</p>

<img width="640" height="347" alt="image" src="https://github.com/user-attachments/assets/bca3aa7d-6ff7-4c55-a738-ca303113b623" />

<br>
<br>
<p>

- Execute <a href="https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Red%20Team/Love%20at%20First%20Breach%202026%20%20%C2%B7%20%20Signed%20Messages%20-%20%F0%9F%9A%A9%20Medium%20-%20Forge_Digital_Signature.py">Python Script to Forge Digital Signature</a> again, but this time guarantee that the variable <strong>loveuser</strong> is set up with <code>admin</code> and that <strong>lovemessage</strong> has the accurate message related to this user profile.</p>

<img width="1351" height="620" alt="image" src="https://github.com/user-attachments/assets/7bb4b43f-d2d7-4497-84d2-1d8e84336258" />

<br>
<br>
<p>

- Create <code>id.rsa.pub</code> file.<br>
- Add to it the accurate content uncovered in the previous step.<br>
- Execute <a href="https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Red%20Team/Love%20at%20First%20Breach%202026%20%20%C2%B7%20%20Signed%20Messages%20-%20%F0%9F%9A%A9%20Medium%20-%20Forge_Digital_Signature.py">Python Script to Retrieve Modulus (n) and Public Exponent (e)</a>.<br>Note: Guarantee that this script is located within the same path of the <code>id.rsa.pub</code> file.<br>
- Navigate to http://lovenote.thm:5000/verify.<br>
- Enter <code>admin</code>'s <strong>Sender Username</strong>, <strong>Message Content</strong>, and <strong>Digital Signature</strong>.<br>
- Hit <code>Verify Signature</code>, and uncover the flag.</p>

<img width="1351" height="620" alt="image" src="https://github.com/user-attachments/assets/bfa00d36-5738-4e12-bc5b-eb36d83c0acf" />

<br>
<br>

```bash
Welcome to LoveNote! Send encrypted love messages this Valentine's Day. Your communications are secured with industry-standard RSA-2048 digital signatures.
```

<br>
<img width="640" height="438" alt="image" src="https://github.com/user-attachments/assets/69480bd8-46d9-44fb-aa30-9f390ed119c4" />

<br>
<br>
<p><em>Answer the question below</em></p>
<p>What is the flag?<br>
<code>THM{PR3--------_-----_------}</code></p>



<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/2fd58392-d76f-4e59-826a-285b0e4e9e3a"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/770b5c03-e34e-41d3-b6e7-0f92977f5a41"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/b7a9c32c-8e3a-4b7b-a05f-ffb71716bfbc"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/cc68e8f3-d818-42a7-8c70-304603934842"><br></p>


<br>
<h1 align="center">My TryHackMe Journey ・ 2026, February</h1>

<p align="center">Global All Time:    40ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/9845f805-d1a7-45dd-805f-46c0d1acb187"><br>
                                              <img width="1200px" src="https://github.com/user-attachments/assets/7e3b54fb-008c-443f-b149-c750308f3ef8"><br><br>
                  Brazil All Time:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/52e681f8-8315-4084-88be-63a8e89dc8bc"><br><br>
                  Global Monthly:      46ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/b59c4306-afec-4940-b3c2-5fa917f42250"><br><br>
                  Brazil Monthly:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/5bd5348a-3283-4fc6-8f1c-b5c95cbe7132"></p>

                  
<h1 align="center">Thanks for coming!</h1>
