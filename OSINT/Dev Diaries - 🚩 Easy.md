<h1 align="center"><a href="https://tryhackme.com/room/devdiaries">Dev Diaries</a></h1>
<p align="center">If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://githubhttps://github.com/user-attachments/assets/f9d56f26-bf87-4309-b5d8-f98cbb0302b0com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2018-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>
<p align="center"><img width="595px" src="https://github.com/user-attachments/assets/d8a77fce-9603-4577-acdc-dbb4c46b15a1"><br>It´s a 🆓 easy-level challenge. Let's get started!</p> 


<br>
<h2>Task 1 . Challenge</h2>
<p>We have just launched a website developed by a freelance developer. The source code was not shared with us, and the developer has since disappeared without handing it over.<br>

Despite this, traces of the development process and earlier versions of the website may still exist online.<br>

You are only given the website's primary domain as a starting point: <code>marvenly.com</code></p>

<p><em>Answer the questions below</em></p>
<br>

<p>1.1. What is the subdomain where the development version of the website is hosted?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>uat-testing.marvenly.com</code></p>

<p>Choose your preferred search engine for Certificate Transparency to get details of <code>marvenly.com</code>:<br>

- <a href="https://www.merklemap.com/">Merklemap</a><br>
- <a href="https://sslmate.com/ct_search_api/">Cert Spotter</a><br>
- <a href="https://scantower.io/certificate-transparency-checker">Scan Tower</a><br>
- <a href="https://www.certkit.io/tools/ct-logs/">CertKit</a><br>
- <a href="https://platform.censys.io/home">Censys</a><br>
- <a href="https://crt.sh/">cert.sh</a><br></p>

<p>Identify:<br>  
  
- admin<code>.marvenly.com</code><br>
- uat-testing<code>.marvenly.com</code><br>
- www<code>.marvenly.com</code><br><br><img width="1800px"  src="https://github.com/user-attachments/assets/e6e55541-2f72-42d0-a11f-b9c32941ec9c"><br>Ref: Merklemap<br></p>

<br>
<p>1.2. What is the GitHub username of the developer?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>notvibecoder23</code></p>

<p>

- Navigate to <code>uat-testing.marvenly.com</code>.<br>
- Scroll down or click <strong>Contact</strong>.<br>
- Identify <strong>Website developed by <code>notvibecoder23</code></strong>.<br><br><img width="1200px"  src="https://github.com/user-attachments/assets/f466c7ac-9100-4a6b-bfc9-22459da1148a"><br>Ref: uat-testing.marvenly.com<br><br><img width="1200px"  src="https://github.com/user-attachments/assets/4860d905-84ec-405f-b331-c357d738f784"><br>Ref: uat-testing.marvenly.com/#contact</p>

<br>
<p>1.3. What is the developer's email address?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>freelancedevbycoder23@gmail.com</code></p>
<p>
  
- Choose you preferred user account search engine.<br>
- Identify <code>https://github.com/notvibecoder23</code>.<br><br><img width="1200px"  src="https://github.com/user-attachments/assets/efd61cf7-fe92-455c-a76d-990d044d53f4"><br>Ref: https://whatsmyname.app/</p>

<br>
<p>

- Navigate to the GitHub profile discovered.<br>
- Select the <strong>marvenly_site</strong> repository.<br><br><img width="1200px"  src="https://github.com/user-attachments/assets/46380f09-4042-42a2-82b2-951b1c57a431"><br>Ref: https://github.com/notvibecoder23</p>

<br>

<p>
  
- Click over the <strong>4 Commits</strong> at the right upper corner.<br><img width="1200px"  src="https://github.com/user-attachments/assets/86a553ca-9e4b-4310-a00b-1c753f954ed0"><br>Ref: https://github.com/notvibecoder23/marvenly_site/commits/main/<br><br>
- Select the 3ʳᵈ commit and click <strong>View commit details</strong>.<br>
- Add <code>.patch</code> to its URL.<br><br><img width="1200px" src="https://github.com/user-attachments/assets/954cb388-25b6-4684-a3e6-78e18bd2a6e1"><br>Ref: https://github.com/notvibecoder23/marvenly_site/commit/33c59e5feedcbcbfee7a1f6d3a435225698f616f.patch</p>

<br>
<p>1.4. What reason did the developer mention in the commit history for removing the source code?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>The project was marked as abandoned due to a payment dispute</code></p>

<p><img width="1200px"  src="https://github.com/user-attachments/assets/25ad7b97-5102-4cdc-a972-f34edd3a1f5a"><br>Ref:https://github.com/notvibecoder23/marvenly_site/commits/main/</p>

<br>
<p>1.5. What reason did the developer mention in the commit history for removing the source code?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>THM{••••••••••••••••••••••••}</code></p>
<p>

- Discover the answer in 1.3.</p>

<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/0eb8f576-0b11-47fc-b241-8602c1e3c25e"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/a90e8102-969e-491b-9b6b-7e9d182e40f5"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/b398cedd-e077-4931-b20b-26cd6e9bbb92"></p>

       
<h1 align="center">My TryHackMe Journey ・ 2026, March<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Room Name<br><br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|League<br><br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|---------------:|
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

<p align="center">Global All Time:     16ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/ab434249-1cfb-4329-8610-fe35871b214f"><br><br>
                  Global Monthly:      10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/409b9ecd-6c0f-4271-abf4-908f318442e0"><br><br>
                  Brazil All Time:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/c7a6c671-7cfe-4a5c-9ef0-46b6d8ce8963"><br><br>
                  Brazil Monthly:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/c998f9de-75c3-439c-8ef7-5adafb945117"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
