<h3 align="center">Jr Penetration Tester &nbsp;&nbsp; · &nbsp;&nbsp; Web Application Vulnerabilities I</h3><h1  align="center">Topic Transition Recap</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/11adf64a-0018-4e0d-959d-dfb15fe653b2"><br>If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAY%2027-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p><br>

<h2></h2>
<p>Match each JWT component with its security implication:<br>
<strong>Header algorithm field</strong> &nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;&nbsp; Can be set to 'none' to bypass verification<br>
<strong>Signature verification</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;&nbsp; Prevents unauthorized token modification<br>
<strong>Token expiration time</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;&nbsp; Limits window for token replay attacks<br>
<strong>Payload role claim</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; : &nbsp;&nbsp; Can be modified for privileg escalation</p>

<h2></h2>
<p>True or False: JWT tokens contain three parts separated by dots<br>
✅  &nbsp;&nbsp; True.<br>
⬛  &nbsp;&nbsp; False<br>
❯❯❯❯ &nbsp;&nbsp; JWT consists of header, payload, and signature sections separated by dots.</p>

<h2></h2>
<p>Which type of SSRF vulnerability provides direct feedback to the attacker?<br>  
⬛ &nbsp;&nbsp; Time-based SSRF<br>
⬛ &nbsp;&nbsp; Reflected SSRF<br>
⬛ &nbsp;&nbsp; Stored SSRF<br>
✅ &nbsp;&nbsp; Regular SSRF<br>
⬛ &nbsp;&nbsp; Blind SSRF<br>
❯❯❯❯ &nbsp;&nbsp; Regular SSRF returns data directly to the attacker's screen, maling it easier to exploit and detect.</p>

<h2></h2>
<p>What command decodes the base64 CSRF token 'YWRtaW4=' to reveal its plaintext value?<br>
<code>echo 'YWRtaW4=' | base64 -d</code></p>

<h2></h2>
<p>True or False: Weak CSRF tokens that use predictable patterns can be reverse-engineered by attackers.<br>  
✅  &nbsp;&nbsp; True.<br>
⬛  &nbsp;&nbsp; False<br>
❯❯❯❯ &nbsp;&nbsp; Tokens based on predictable data like base64-encoded user roles can be easily reproduced by attackers.</p>

<h2></h2>
<p>Which command decodes the payload section of a JWT token stored in the variable $JWT?<br>
<code>echo $JWT | cut -f2 | base64 -d</code></p>

<br>
<p align="center"><img width="1000px" src="https://github.com/user-attachments/assets/aaf5eec1-ebf9-4339-8b0e-d4306627a495"><br>
                  <img width="1000px" src="https://github.com/user-attachments/assets/c6441b08-fc33-4561-9566-c8964b5b9d17"></p>

<h2 align="center">My TryHackMe Journey &nbsp; · &nbsp; 2026, May</h2>
<div align="center"><h6>

|Day<br><br><br> |Capability<br>Score<br><br>|Room<br>Name<br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|
|27<br><br><br><br><br> >      |109<br><br><br><br><br>        |Web Application Vulnerabilities I - Topic Transition Recap<br>         |<br><br><br><br><br>    |<br><br><br><br><br>  | 1,219<br><br><br><br><br> | 177,869<br><br><br><br><br> | 97<br><br><br><br><br> | 9ᵗʰ<br><br><br><br><br>| 5%ʰ<br><br><br><br><br>| 1ˢᵗ<br><br><br><br><br>| 3ʳᵈ<br><br><br><br><br>|
|27<br><br>      |109<br><br>       |[XSS Introduction](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/7%20%C2%B7%20Web%20Application%20Vulnerabilities%20I/3%20%C2%B7%20XSS%20Introduction%20-%20%F0%9F%94%97%20Medium.md)<br>     |Medium<br><br>    |🔗<br><br>  | 1,219<br><br>| 177,829<br><br>| 97<br><br>| 9ᵗʰ<br><br>| 5%<br><br>| 1ˢᵗ<br><br>| 3ʳᵈ<br><br>|
|27<br><br>      |109<br><br>       |[SQL Injection Introduction](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/7%20%C2%B7%20Web%20Application%20Vulnerabilities%20I/1%20%C2%B7%20SQL%20Injection%20Introduction%20-%20%F0%9F%94%97%20Easy.md)<br>     |Easy<br><br>    |🔗<br><br>  | 1,218<br><br>| 177,733<br><br>| 97<br><br>| 9ᵗʰ<br><br>| 5%<br><br>| 1ˢᵗ<br><br>| 3ʳᵈ<br><br>|
|23<br><br>      |109<br><br>       |[Content Discovery](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/4%20%C2%B7%20Web%20Application%20Security%20Fundamentals/2%20%C2%B7%20Content%20Discovery%20-%20%F0%9F%94%97%20Easy.md)<br>              |Easy<br><br>    |🔗<br><br>  | 1,217<br><br>| 177,613<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 40ᵗʰ<br><br>| 1ˢᵗ<br><br>| 2ⁿᵈ<br><br>|
|23<br><br>      |109<br><br>       |[Walking An Application](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/4%20%C2%B7%20Web%20Application%20Security%20Fundamentals/1%20%C2%B7%20Walking%20an%20Application%20-%20%F0%9F%94%97%20Easy.md)<br>         |Easy<br><br>    |🔗<br><br>  | 1,216<br><br>| 177,517<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 41ˢᵗ<br><br>| 1ˢᵗ<br><br>| 2ⁿᵈ<br><br>|
|23<br><br>      |109<br><br>       |[Nmap - Topic Transition Recap](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/3%20%C2%B7%20Nmap/5%20%C2%B7%20Transition%20Topic%20Recap.md)<br>         |<br><br>    |<br><br>  | 1,215<br><br>| 177,445<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 39ᵗʰ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|
|23<br><br><br><br><br>      |109<br><br><br><br><br>       |[Penetration Testing Foundations - Topic Transition Recap](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/6%20%C2%B7%20Topic%20Transition%20Recap.md)<br>         |<br><br><br><br><br>    |<br><br><br><br><br>  | 1,215<br><br><br><br><br> | 177,397<br><br><br><br><br> | 96<br><br><br><br><br> | 8ᵗʰ<br><br><br><br><br>| 40ᵗʰ<br><br><br><br><br>| 1ˢᵗ<br><br><br><br><br>| 1ˢᵗ<br><br><br><br><br>|
|23<br><br><br>  |109<br><br><br>   |[Penetration Testing Frameworks](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/5%20%C2%B7%20Penetration%20Testing%20Frameworkds%20-%20%F0%9F%94%97%20Easy.md)<br> |Easy<br><br><br>|🔗<br><br><br>| 1,215<br><br><br>| 177,349<br><br><br>| 96<br><br><br>| 8ᵗʰ<br><br><br>| 43ʳᵈ<br><br><br>| 1ˢᵗ<br><br><br>| 1ˢᵗ<br><br><br>|
|22<br><br>      |109<br><br>       |[Dive Into Pentesting](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/3%20%C2%B7%20Dive%20Into%20Pentesting%20-%20%F0%9F%94%97%20Easy.md)<br>           |Easy<br><br>|🔗<br><br>| 1,214<br><br>| 177,205<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 41ˢᵗ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|
|22<br><br>      |109<br><br>       |[Guided Pentest: Infrastructure](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-&-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/2%20%C2%B7%20Guided%20Pentest:%20Infrastructure%20-%20%F0%9F%94%97%20Easy.md)<br> |Easy<br><br>|🔗<br><br>| 1,213<br><br>| 177,085<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 40ᵗʰ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|
|22<br><br>      |109<br><br>       |[Guided Pentest: Web](https://github.com/RosanaFSS/TryHackMe_Cybersecurity_Journey/blob/CTFs-%26-Infos/Jr%20Penetration%20Tester/1%20%C2%B7%20Penetration%20Testing%20Foundations/1%20%C2%B7%20Guided%20Pentest%3A%20Web%20-%20%F0%9F%94%97%20Easy.md)<br>            |Easy<br><br>|🔗<br><br>| 1,212<br><br>| 177,045<br><br>| 96<br><br>| 8ᵗʰ<br><br>| 41ˢᵗ<br><br>| 1ˢᵗ<br><br>| 1ˢᵗ<br><br>|

</h6></div>
<h2 align="center">Thanks for coming!</h2>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
