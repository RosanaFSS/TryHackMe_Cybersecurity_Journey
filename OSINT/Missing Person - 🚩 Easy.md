<h1 align="center"><a href="https://tryhackme.com/room/missingperson">Missing Person</a></h1>
<p align="center"><br><img width="1200px" src="https://github.com/user-attachments/assets/becf37bd-921f-4078-9b23-1fd80edd79f9"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20MAR%2017-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p
Follow the leads and find who's behind this operation.

<br>
<h2>Task 1 . OSINT</h2>
<P>"My friend went on holiday in 2025 and shared some photos, but I haven’t heard from him since. Can you help me track him down for the police report?"<BR>

Download the zip file attached to this task and start your investigation!</P>


<p><em>Answer the questions below</em></p>
<br>

<p>1.1 What is the commercial name of this circuit? Format: English, full commercial name.<br>
<code>Pertamina Mandalika International Street Circuit</code></p>
<p>

- Use <a href="https://yandex.com/">Yandex</a> to reverse the <strong>MotoGP.jpg</strong>.</p>

<img width="1338" height="357" alt="image" src="https://github.com/user-attachments/assets/83b09474-ee84-411c-ad00-00ab017769e0" />

<br>
<p>

- Use <code>Google</code>.</p>

<img width="902" height="238" alt="image" src="https://github.com/user-attachments/assets/123424f8-10b2-41d2-a29c-9dcb047de46d" />

<br>
<br>
<br>

<p>1.2. When did the event take place? Format: DD-DD/MM/YYYY.<br>
<code>03-05/10/2025</code></p>
<p>

- Use <code>exfitool</code> to inspect <strong>MotoGP.jpg</strong>´s properties.</p>

```bash
$ exiftool MotoGP.jpg
...
File Name                       : MotoGP.jpg
...
Date/Time Original              : 2025:10:05 12:33:12
Create Date                     : 2025:10:05
```

<p>

- Use <code>Google</code>.</p>

<img width="908" height="156" alt="image" src="https://github.com/user-attachments/assets/dd36f7ac-dae4-40cd-8721-b6008a815013" />

<br>
<br>
<br>

<p>1.3. He told me he ate delicious Mexican food. What is the name of the restaurant?<br>
<code>Cantina Mexicana</code></p>

<p>
  
- Use <code>Google</code> to reverse the <strong>food.jpg</strong>.</p>
                            
<img width="971" height="203" alt="image" src="https://github.com/user-attachments/assets/d6e8db84-1988-4e5b-869c-a4f50bd1fb50" />

<br>
<p>

- Check <strong>Cantina Mexicana</strong>´s address.<br>
- Identify <strong>Kuta Lombok</strong>.</p>

<img width="1305" height="153" alt="image" src="https://github.com/user-attachments/assets/a5462668-4b1a-45cd-90ed-dcb01d2c8b1c" />

<br>

<img width="382" height="185" alt="image" src="https://github.com/user-attachments/assets/a3399b56-ffae-4936-8efd-825cbfd188b9" />

<br>
<br>
<br>
<p>1.4. At what time was this photo taken? Format: HH:MM:SS.<br>
<code>19:55:30</code></p>
<p>

- Use <code>exfitool</code> to inspect <strong>food.jpg</strong>´s properties.</p>

```bash
$ exiftool food.jpg
...
File Name                       : food.jpg
...
Date/Time Original              : 2025:10:05 19:55:30
```

<br>
<p>1.5. He sent me a message, this is the last I heard from him: ”Went to this cool MotoGP after party, and became friends with one of the local DJs who played that night. We’re going to visit a cave tomorrow.” What is the full address of the bar’s location?<br>
<code>Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Bar</code></p>

<p>

- Use <code>Google</code> to search for <code>MOTOGP</code> AND <code>2025</code> AND <code>party</code> AND <code>DJ</code> AND <code>Mandalika</code>.<br>
- Navigate to <strong>Expeience and exclusive athmosphere, premium vibes ... party side by side with MotoGP riders. After Race Party - Mandalika GP Vol.3 ...</strong>.<br>
- Navigate to the <strong>https://megatix.co.id/events/mandalika-moto-gp=after-race-party</strong> link provided by the <strong>themandalikabeachblub</strong> profile in Instagram.<br>
- Identify <strong>Kuta, Pujut, Central Lombok Regency, <code>West Nusa Tengarra</code>.<br>
- Use <code>Tripadvisor</code> to search restaurants in <code>West Nusa Tengarra</code> > <code>Lombok</code> > <code>Kuta</code>.<br>
- Discover <code>KRNK Restaurant & Bar</code>´s address</p>


<img width="1060" height="277" alt="image" src="https://github.com/user-attachments/assets/daf9baa3-000f-40a3-8d25-9e512ef4df39" />

<br>
<br>

<img width="1232" height="509" alt="image" src="https://github.com/user-attachments/assets/05ee6abe-6c66-48ae-a689-94f76f72dc83" />

<br>
<br>

<img width="1869" height="855" alt="image" src="https://github.com/user-attachments/assets/c0fc6935-3db5-43b0-8c5d-1c7fed6a4282" />

<br>
<br>

<img width="1080" height="826" alt="image" src="https://github.com/user-attachments/assets/6c1c2766-d032-4de7-b81d-0c13fba18b17" />

<br>
<br>
<br>
<p>1.6. What is the DJ's stage name?<br>
<code>Bong Leleh</code></p>
<p>

- Use <code>Google</code> to search for <code>MOTOGP</code> AND <code>2025</code> AND <code>party</code> AND <code>DJ</code> AND <code>Mandalika</code>.<br>
- Navigate to <strong>Get ready for the biggest party after the Moto GP race!</strong>.</p>

<img width="1284" height="579" alt="image" src="https://github.com/user-attachments/assets/3f7ab82d-a3f7-4c86-8a4f-80dc13df934c" />

<br>
<br>
<br>
<p>1.7. What is the name of the cave?<br>
<code>Gua Sumur</code></p>

<p>

- Use <code>Google</code> to search for <code>Caves close to Jl. Raya Kuta, Kuta, Kec. Pujut, Kabupaten Lombok Tengah, Nusa Tenggara Bar</code>.</p>


<img width="1282" height="471" alt="image" src="https://github.com/user-attachments/assets/1270e406-4103-4501-a981-0fca18c552a2" />

<br>
<br>
<br>
<p>1.7.What is the phone number linked to his old business? Format: Full number, no country code.<br>
<code>85333137345</code></p>
<p>

- Use <code>Google</code> to search for <code>bongleleh lombok</code>.<br>
- Navigate to <code>Gua Sumur Lombok (@bongleleh)</code> profile in <strong>Facebook</strong>.</p>

<img width="1210" height="463" alt="image" src="https://github.com/user-attachments/assets/95235106-a779-45f2-9358-4478ad62e3f1" />

<img width="1876" height="709" alt="image" src="https://github.com/user-attachments/assets/2d473a0e-92fc-4e95-8936-aa42657c35a4" />

<br>
<br>
<br>
<h1 align="center">Completed</h1>

<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/4f337ebc-9521-4da4-9095-456bef2102a7"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/8c421766-01bb-4b2c-b18f-4f86001b5bee"><br>
                  <img width="900px" src="https://github.com/user-attachments/assets/60714437-aaaf-4170-b088-143bb0fca00d"></p>

         
<h1 align="center">My TryHackMe Journey ・ 2026, March<a id='9'></a></h1>

<div align="center"><h6>

|Day<br><br><br> |Streak<br><br><br>|Room Name<br><br><br>|Level<br><br><br>|Type<br><br><br>|Rooms<br>Completed<br><br>|Points<br><br><br>|Badges<br><br><br>|Global<br>All<br>Time<br>|Global<br>Monthly<br><br>|Brazil<br>All<br>Time<br>|Brazil<br>Monthly<br><br>|League<br><br><br>|
|---------------:|-----------------:|:----------------|:---------------|:----------------------------------------:|-------------------------:|-----------------:|-----------------:|--------------------:|------------------------:|--------------------:|---------------:|---------------:|
|17<br><br>      |75<br><br>        |Missing Person<br><br>           |Medium<br><br> |🚩<br><br>| 1,150<br><br>| 161,123<br><br>| 91<br><br>| 16ᵗʰ<br><br>| 10ᵗʰ<br><br>| 2ⁿᵈ<br><br>| 1ˢᵗ<br><br>|1ˢᵗ<br><br>|
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

<p align="center">Global All Time:     16ᵗʰ<br><img width="1200px"  src="https://github.com/user-attachments/assets/8ddd86e7-31d6-4798-a0e9-8871ab2709db"><br><br>
                  Global Monthly:      10ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/6938f69e-51e8-4539-aa7a-c22fddab5333"><br><br>
                  Brazil All Time:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/7dbf7189-15e5-48b0-ad01-7d0bcecc2ee7"><br><br>
                  Brazil Monthly:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/745b0d84-e1e2-414b-821f-c51575b3c651"></p>


<h1 align="center">Thanks for coming!</h1>
<p align="center">Follow me on <a href="https://medium.com/@RosanaFS">Medium</a>, here on <a href="https://github.com/RosanaFSS/TryHackMe">GitHub</a>, and on <a href="https://www.linkedin.com/in/rosanafssantos/">LinkedIN</a>.</p>
