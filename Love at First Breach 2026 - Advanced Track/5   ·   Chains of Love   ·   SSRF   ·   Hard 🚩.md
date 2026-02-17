<h1 align="center"><a href="https://tryhackme.com/room/lafbctf2026-advanced">Love at First Breach 2026 Advanced &nbsp;&nbsp; · &nbsp;&nbsp; Chains of Love</a></h1>
<p align="center">Web &nbsp;&nbsp; · &nbsp;&nbsp; SSRF (Server-Side Request Forgery) to RCE (Remote Code Execution)<br><br><img width="1200px" src="https://github.com/user-attachments/assets/e704c36d-3636-48d9-8ce3-69fe8188fa95"><br><img width="1200px" src="https://github.com/user-attachments/assets/56f5f111-e5f8-488f-9b6c-b06bba41e7af"><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20FEV%2017-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p

<br>
<h2>Chains of Love</h2>

```bash
My Dearest Hacker,

NovaDev Solutions is a software development house known for building secure enterprise platforms for clients across multiple countries and industries. Recently, NovaDev Solutions rolled out a new customer interaction feature on their website to improve communication between clients and developers.

Shortly after deployment, NovaDev began experiencing unusual traffic patterns and minor service disruptions. Internal developers suspect that something in the latest udpate may have exposed more than intended.

With love,
Chief Inspector Valentine 💕
```

<h3 align="left"> $$\textcolor{#f00c17}{\textnormal{Answer the question below}}$$ </h3>


> <em>What is the flag.txt</em><br><a id='1.1'></a>
>> <strong><code>THM{•••••••••••••••••••••••••••••••••••}</code></strong><br>
<p></p>


<h1 align="center">Reconnaissance · Static Domain Resolution</h1>
<p>

- navigate to http://MACHINE_IP<br>
- right-click<br>
- select Inspect<br>
- select Network tab<br>
- note that you will be redirect to http://nova.thm</p>

<img width="1153" height="125" alt="image" src="https://github.com/user-attachments/assets/88dc1722-7dcd-4deb-a120-0da6814c5086" />

<br>
<br>

```bash
:~/# echo "MACHINE_IP nova.thm" >> /etc/hosts
```

<h1 align="center">Reconnaissance · Port & Service Enumeration</h1>

```bash
:~/# nmap -Pn -n -p- -T4 nova.thm
...
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

```bash
:~/# nmap -sC -sV -Pn -n -p22,80 -T4 nova.thm
...
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
| http-git: 
|   MACHINE_IP:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: Preview Feature 
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).```
```

<h1 align="center">Reconnaissance · Directory & File Enumeration</h1>

```bash
:~/# ffuf -u http://nova.thm/FUZZ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -mc 200,302 -ic -c -e .js,.html,.py,.php -t 80

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://nova.thm/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Extensions       : .js .html .py .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 80
 :: Matcher          : Response status: 200,302
________________________________________________

                        [Status: 200, Size: 2873, Words: 370, Lines: 150]
about                   [Status: 200, Size: 2632, Words: 216, Lines: 149]
contact                 [Status: 200, Size: 2146, Words: 168, Lines: 131]
services                [Status: 200, Size: 2840, Words: 197, Lines: 149]
admin                   [Status: 302, Size: 211, Words: 18, Lines: 6]
app.py                  [Status: 200, Size: 3364, Words: 669, Lines: 133]
```

<img width="1247" height="530" alt="image" src="https://github.com/user-attachments/assets/ec18659d-fa3f-4020-a440-993c014f7b24" />

<br>
<br>
<h1 align="center">Reconnaissance · Web Interface Inspection</h1>

<img width="1275" height="820" alt="image" src="https://github.com/user-attachments/assets/e830c941-5a7c-43b3-b510-daca2f175d63" />

<br>

<img width="1337" height="532" alt="image" src="https://github.com/user-attachments/assets/517713d5-ba0d-46f7-8cb0-d9f9530cf98f" />

<br>
<br>
<p>About</p>

<img width="1342" height="386" alt="image" src="https://github.com/user-attachments/assets/07bd1035-b6e7-45de-872f-fd928604d711" />

<br>
<br>
<p>Services</p>

<img width="1344" height="601" alt="image" src="https://github.com/user-attachments/assets/45aa4729-4822-4382-bf84-6be06659e409" />

<br>
<br>
<p>Contact</p>

<img width="1341" height="596" alt="image" src="https://github.com/user-attachments/assets/8a068d4f-aae2-4658-983f-524b94f6082d" />

<br>
<br>
<p>admin</p>

<img width="1213" height="615" alt="image" src="https://github.com/user-attachments/assets/c8989d79-1c01-4cc3-810b-22721a431bdc" />

<br>
<br>
<p>app.py</p>

```bash
app = Flask(__name__, static_folder=".", static_url_path="")

JWT_SECRET = os.environ.get("ADMIN_SECRET", "••••••••••••••••••")

app.config["DEBUG"] = False
app.config["ENV"] = "production"
app.config["VERSION"] = "2.3.1"
app.config["DATABASE_URL"] = "postgresql://app_user:********@db.internal:5432/novadev"
app.config["REDIS_HOST"] = "redis.internal"
app.config["ADMIN_SECRET"] = ••••••••••

ADMIN_USERNAME = "•••••••••••••••••••••••"
ADMIN_PASSWORD = "••••••••••••••••••••"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        message = request.form.get("message", "").strip()

        # Security by Obscurity

        if message == "{{ config }}":

            return render_template_string(
            message,
            config=app.config
            )

        #This escapes all text
        safe_message = escape(message)

        template = f"""
        <h3>Thank you for your message</h3>
        <div class="preview-box">
            {safe_message}
        </div>
        """

        return template
    return render_template("contact.html")

def verify_jwt(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except Exception:
        return None

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            payload = {
                "user": username,
                "role": "admin",
                "iat": datetime.datetime.utcnow(),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }

            token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

            resp = redirect("/admin")
            resp.set_cookie("token", token)
            return resp

        return render_template("admin_login.html", error="Invalid credentials")

    return render_template("admin_login.html")

@app.route("/admin")
def admin():
    token = request.cookies.get("token")
    if not token:
        return redirect("/admin/login")

    data = verify_jwt(token)
    if not data or data.get("role") != "admin":
        return "Unauthorized"

    return render_template("admin.html")


@app.route("/admin/fetch")
def fetch():
    token = request.cookies.get("token")
    data = verify_jwt(token)

    if not data or data.get("role") != "admin":
        return "Unauthorized"

    url = request.args.get("url")
    if not url:
        return "No URL provided"

    if any(char.isdigit() for char in url):
        return "Digits are not allowed, we really like DNS!"

    try:
        response = requests.get(url, timeout=5)
        return response.text
    except Exception as e:
        return f"Request failed: {str(e)}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
```

<h1 align="center">Reconnaissance · Web Vulnerability Scanning</h1>

```bash
:~/ChainsofLove# nikto -h http://nova.thm/contact
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MACHINE_IP
+ Target Hostname:    nova.thm
+ Target Port:        80
+ Start Time:         2026-02-17 xx:xx:xx (GMT0)
---------------------------------------------------------------------------
+ Server: nginx/1.18.0 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-5737: WebLogic may reveal its internal IP or hostname in the Location header. The value is "http://nova.thm/".
+ Allowed HTTP Methods: GET, OPTIONS, HEAD 
+ 6544 items checked: 0 error(s) and 3 item(s) reported on remote host
+ End Time:           2026-02-17 xx:xx:xx (GMT0) (16 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<h1 align="center">Reconnaissance · Subdomain Enumeration</h1>

```bash
:~/# ffuf -u http://nova.thm/ -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.nova.thm" -ic -c -fs 178

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1
________________________________________________

 :: Method           : GET
 :: URL              : http://nova.thm/
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.nova.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
 :: Filter           : Response size: 178
________________________________________________

internal                [Status: 403, Size: 162, Words: 4, Lines: 8]
:: Progress: [114528/114528] :: Job [1/1] :: 20000 req/sec :: Duration: [0:00:09] :: Errors: 0 ::
```

<img width="1366" height="507" alt="image" src="https://github.com/user-attachments/assets/48c195ef-1e83-4548-b6a4-804c72fc1f92" />

<br>
<br>
<h1 align="center">Reconnaissance · Static Host Mapping</h1>

```bash
MACHINE_IP nova.thm internal.nova.thm
```

<h1 align="center">Weaponization & Delivery & Exploitation · SSRF to RCE</h1>

<img width="1210" height="542" alt="image" src="https://github.com/user-attachments/assets/8da1f9da-ab3e-4879-8aa7-21bf196df183" />

<br>
<br>

<img width="1214" height="562" alt="image" src="https://github.com/user-attachments/assets/30c64dec-8aff-48bb-ad21-0cf81b5f4a78" />

<br>
<br>

<img width="1217" height="768" alt="image" src="https://github.com/user-attachments/assets/718c683f-49af-445a-b913-32e666d06bf4" />

<br>
<br>

<img width="1213" height="566" alt="image" src="https://github.com/user-attachments/assets/2ba390b5-5bf1-46cc-98aa-4cd62e933101" />

<br>
<br>

<img width="1371" height="762" alt="image" src="https://github.com/user-attachments/assets/6f390f60-0a91-4c0a-9f88-0cfd9433a181" />

<br>
<br>

<img width="1895" height="322" alt="image" src="https://github.com/user-attachments/assets/54f9d7ad-66c5-4652-aa26-e144a70995c8" />

<br>
<br>

<img width="1898" height="329" alt="image" src="https://github.com/user-attachments/assets/1cfeeb2a-0b4c-484f-a0a0-f873e3cba25d" />

<br>
<br>

<img width="1893" height="239" alt="image" src="https://github.com/user-attachments/assets/0f4b9707-dc21-43ea-81ab-da02d7dbc0ea" />

<br>
<br>

<img width="1249" height="275" alt="image" src="https://github.com/user-attachments/assets/4c35dc3d-d7ae-4818-b9fe-4f1b7085bdff" />

<br>
<br>

<img width="1891" height="311" alt="image" src="https://github.com/user-attachments/assets/aebeb1e9-9e2d-495b-b200-55d053e4e1b0" />

<br>
<br>

<img width="1890" height="314" alt="image" src="https://github.com/user-attachments/assets/fa7929f7-0144-458c-9573-eb66af0a31ef" />

<h1 align="center">Actions on Objectives</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/8631b6cd-eb55-41e4-b2f0-17a154dce6fb"></p>

<h1 align="center">Completed</h1>
<p align="center"><img width="1200px" src="https://github.com/user-attachments/assets/56f5f111-e5f8-488f-9b6c-b06bba41e7af"></p>

<h1 align="center">My TryHackMe Journey ・ 2026, February</h1>
<p align="center">Global All Time:     39ᵗʰ<br><img width="250px" src="https://github.com/user-attachments/assets/d968b6c7-b801-4ee9-bb64-20b9217d0349"><br>
                                               <img width="1200px" src="https://github.com/user-attachments/assets/96ae6a14-ac2c-4d09-9020-f78e1fcc2db6"><br><br>
                  Brazil All Time:      2ⁿᵈ<br><img width="1200px" src="https://github.com/user-attachments/assets/5f0bb0c4-63ae-4a13-babe-015a6065cf23"><br><br>
                  Global Monthly:      39ᵗʰ<br><img width="1200px" src="https://github.com/user-attachments/assets/847b6535-e2f5-4598-8e58-2eb95acb97fe"><br><br>
                  Brazil Monthly:       1ˢᵗ<br><img width="1200px" src="https://github.com/user-attachments/assets/683bfb0e-cee8-4968-a67c-cc88ac4bdd00"></p>

                  
<h1 align="center">Thanks for coming!</h1>
