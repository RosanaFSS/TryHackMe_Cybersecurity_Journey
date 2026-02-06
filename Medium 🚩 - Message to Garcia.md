
<h1>Message to Garcia</h1>
https://tryhackme.com/room/messagetogarcia
<p></p>Encryption and Key Management Challenge.</p>

<p>Nmap</p>

<p>Gobuster</p>

<p>...</p>

<img width="1896" height="393" alt="image" src="https://github.com/user-attachments/assets/942128d6-48ec-45ac-92aa-1e804fa6f0d6" />


<br>

<img width="920" height="152" alt="image" src="https://github.com/user-attachments/assets/d25cea7b-23f3-4d84-9eb2-e4c5b2d65342" />


<img width="1330" height="358" alt="image" src="https://github.com/user-attachments/assets/287ccce1-f7c9-4746-b38d-f2e57d21d9a5" />

:~# nano message.py



:~# python3 message.py
[*] Message to encrypt: Garcia, ...
[*] Encryption key: ...

[+] Encrypted message saved to: message.enc
[+] File size: 248 bytes

[*] Testing decryption...
[+] Decrypted: Garcia, ...
[+] Match: True

============================================================
SUCCESS! Upload 'message.enc' to the application!
============================================================


file://create_message.py

<img width="1327" height="550" alt="image" src="https://github.com/user-attachments/assets/f9b2302f-3730-4e15-9b88-4b8db55c2aae" />



:~# ls -lah
...
-rw-r--r--  1 root root  248 Feb  6 21:43 message.enc
-rw-r--r--  1 root root 1.1K Feb  6 21:43 message.py




:~# curl -c cookies.txt -F "file=@message.enc" http://MACHINE_IP/upload
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/success">/success</a>. If not, click the link.



:~# curl -b cookies.txt http://MACHINE_IP/success
 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
...

     <div class="flex justify-center mb-6">
        <div class="bg-green rounded-full p-4">
          <svg class="w-16 h-16 text-black" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
          </svg>
        </div>
      </div>

      <!-- Title -->
      <h1 class="text-4xl font-bold text-center text-green mb-8">
        Mission Accomplished!
      </h1>

      <!-- Flag Display -->
      <div class="bg-slate-800 rounded-lg p-8 border border-green">
        <div class="font-mono text-3xl text-green text-center break-all select-all">
          THM{•••••••••••••••••••••••••••••••}
        </div>
      </div>


<img width="1007" height="705" alt="image" src="https://github.com/user-attachments/assets/00aef371-c349-4f2e-a241-e46932d284a7" />

<h1>Completed</h1>

<img width="1891" height="448" alt="image" src="https://github.com/user-attachments/assets/a480c382-b9d0-41c0-8633-1a49ad3687cb" />

<img width="1891" height="197" alt="image" src="https://github.com/user-attachments/assets/5008b8a5-24b0-42d0-bd66-33bf79ff6bbc" />

<img width="1901" height="769" alt="image" src="https://github.com/user-attachments/assets/9b625ce5-608f-463c-ad4a-1b2f48b38958" />

<h1>Journey</h1>



<img width="329" height="88" alt="image" src="https://github.com/user-attachments/assets/587c4eb7-42f4-4c79-9e60-31803441e9af" />

<img width="1900" height="900" alt="image" src="https://github.com/user-attachments/assets/7b1fc5cb-1ab8-47d5-9d04-25adf4d8232c" />

<img width="1896" height="890" alt="image" src="https://github.com/user-attachments/assets/5c4fac9d-b600-4170-82a3-514d4c162786" />

<img width="1889" height="888" alt="image" src="https://github.com/user-attachments/assets/9db76b9c-7e5f-4859-abeb-47e33dc77860" />

<img width="1889" height="895" alt="image" src="https://github.com/user-attachments/assets/7b898afd-6d5f-4042-a925-78bd01093689" />






