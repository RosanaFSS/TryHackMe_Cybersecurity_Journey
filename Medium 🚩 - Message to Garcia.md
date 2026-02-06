
<h1>Message to Garcia</h1>
<p></p>Encryption and Key Management Challenge.</p>





https://tryhackme.com/room/messagetogarcia

<img width="920" height="152" alt="image" src="https://github.com/user-attachments/assets/d25cea7b-23f3-4d84-9eb2-e4c5b2d65342" />

<img width="1321" height="518" alt="image" src="https://github.com/user-attachments/assets/f2eb6469-a8df-4ae5-825d-66fbbd33d46f" />



<img width="1330" height="358" alt="image" src="https://github.com/user-attachments/assets/287ccce1-f7c9-4746-b38d-f2e57d21d9a5" />

:~# nano message.py



:~# python3 message.py
[*] Message to encrypt: Garcia, it seems I've cracked the code!! I need you to meet me at coordinates: 40.4168° N, 3.7038° W. The cipher is: TRACK
[*] Encryption key: TUVTU0FHRVRPR0FSQ0lBMjAyNF9LRVkhISEhISEhISE=

[+] Encrypted message saved to: message.enc
[+] File size: 248 bytes

[*] Testing decryption...
[+] Decrypted: Garcia, it seems I've cracked the code!! I need you to meet me at coordinates: 40.4168° N, 3.7038° W. The cipher is: TRACK
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




:~# curl -c cookies.txt -F "file=@message.enc" http://10.81.138.23/upload
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/success">/success</a>. If not, click the link.



:~# curl -b cookies.txt http://10.81.138.23/success
 
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


