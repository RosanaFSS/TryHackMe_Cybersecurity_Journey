<h1>SEC1: Cyber Security 101 (SEC1) Certification</h1>
<br>
<h2>Certification Info</h2>

<p><strong>What is the Cyber Security 101 (SEC1) Certification?</strong><br>
The Cyber Security 101 (SEC1) Certification is a beginner-level, hands-on certification designed for learners who complete TryHackMe's Cyber Security 101 path. It validates foundational offensive, defensive, and investigative skills through real-world, practical scenarios.</p>

<p><strong>What skills does the certification validate?</strong><br>
It validates practical understanding of:<br>
— &nbsp; Basic offensive security (red team)<br>
— &nbsp; basic defensive security (blue team)<br>
— &nbsp; Investigative workflows across SIEM, artifacts, and compromised machines<br>
— &nbsp; Foundational cyber security concepts needed for junior roles.</p>

<p><strong>What are the prerequisites?</strong><br>
Recommended:<br>

— &nbsp; Completion of TryHackMe's Cyber Security 101 Path.<br>
— &nbsp; Basic familiarity with Windows, Linux, Networks, Blue & Red teams working on cyber security.<br>
— &nbsp; No formal prerequisites — but the exam is practical and assumes foundational knowledge.</p>

<p><strong>What is the exam format?</strong><br>
The exam is fully hands-on, split into 7 sections across:<br>
— &nbsp; Red Team<br>
— &nbsp; Blue Team<br>
— &nbsp; Purple Team<br>
It includes an analyst VM containing multiple artifacts. Each section includes scenario-based tasks and technical questions based on what you uncover.</p>
<h2></h2>
<h2>Certification Prep &nbsp; — &nbsp; Cyber Security 101 Learning Path<br><br>
▪ &nbsp; Operating Systems Fundamentals</strong><br>&nbsp;&nbsp;&nbsp;&nbsp; — &nbsp;&nbsp;&nbsp; 𝗟𝗶𝗻𝘂𝘅 𝗙𝘂𝗻𝗱𝗮𝗺𝗲𝗻𝘁𝗮𝗹𝘀 𝗣𝗮𝗿𝘁 𝟭<br>&nbsp;&nbsp;&nbsp;&nbsp; — &nbsp;&nbsp;&nbsp; 𝗟𝗶𝗻𝘂𝘅 𝗙𝘂𝗻𝗱𝗮𝗺𝗲𝗻𝘁𝗮𝗹𝘀 𝗣𝗮𝗿𝘁 𝟮<br>&nbsp;&nbsp;&nbsp;&nbsp; — &nbsp;&nbsp;&nbsp; 𝗟𝗶𝗻𝘂𝘅 𝗙𝘂𝗻𝗱𝗮𝗺𝗲𝗻𝘁𝗮𝗹𝘀 𝗣𝗮𝗿𝘁 𝟯</h2>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Linux powers: <br>
  
- Websites that you visit<br>
- Car entertainment/control panels<br>
- Point of Sale (PoS) systems such as checkout tills and registers in shops<br>
- Critical infrastructures such as traffic light controllers or industrial sensors<br>
- Phones, and similar small computing devices<br>
- And much much more!</p>

<div align="center"><p>

|Command/<br>Keys             |Task<br><br>                                                       |Example<br><br>            |
|:----------------------------|:------------------------------------------------------------------|:---------------------|
|$ `whoami`<br><br>           |Tells you who you are on the system.<br> <br>                       |`tryhackme`<br><br>   |
|`↑` and `↓` arrow keys<br><br>|Press it to scroll through commands<br>that you have already entered.<br>|-<br><br>        |
|`echo`<br><br><br><br><br>$ `echo` rose<br><br><br><br><br><br>$ `echo` "beautiful rose"<br>|Is a building-block for the very<br>important skill that is being<br>able to send and store<br>information in Linux.<br><br>Output some specific text that is provided.<br><br><br><br><br>Output multiple words.<br><br>|-<br><br><br><br><br>$ `echo` rose<br>rose<br><br><br><br><br>$ `echo` "beautiful rose"<br>beautiful rose<br>|    
|$ `ls`<br><br><br><br>$ `ls -a` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OR<br>$ `ls --all`<br><br><br>`ls --help`<br><br><br><br><br>$ `ls -lh`<br><br>|List what's in the current folder.<br><br><br><br>Do not ignore entries starting with `.`<br><br><br><br>List the possible options that the<br>command accepts, provide a brief<br>description and example of how<br>to use it.<br><br>List permissions: `l` use a long listing format<br> `h` with -l and -s, print sizes like 1K 234M 2G etc.<br>|$ `ls`<br>access.log<br><br><br>$ `ls -a`<br>.   .bash_logout  .cache    important  myfolder<br>..  .bashrc       .profile  myfile     unknown1<br><br><br><br><br><br><br>-<br><br>|
|$ `find`<br><br>             |Search for files by their name.<br><br>                             |$ `find` -name passwords.txt<br>./folder1/passwords.txt|
|$ `cd`<br><br>               |Change directory — move into a folder.<br><br>                     |$ `cd` folder1<br><br>          |
|$ `pwd`<br><br>              |Print working directory —<br>"where am I?"<br>                      |$ `pwd`<br><br>                 |
|$ `cat`<br><br>              |Show the contents of a file.<br><br>                                |$ `cat` passwords.txt<br>password123<br> |
|$ `grep`<br><br><br><br><br> |Searches inside for text.<br><br><br><br><br>                       |$ `grep` "password123" passwords.txt<br>password123<br><br>$ `grep` "THM" access.log <br>... THM{...}|
|`&`<br><br><br><br><br><br>  |Runs the command, but does not wait for<br>it to finish before you can do anything else.<br>The command runs in the backgorund,<br>and is helpful for commands that might<br>take a while to complete, or ones that<br> you want to keep running.|-<br><br><br><br><br><br>|
|`&&`<br><br><br>             |Runs both commands, but <strong><em>waits for the<br>first command to finish first</em></strong>, before<br>the next. Like a set of dominoes.<br>|-<br><br><br>|
|`>`<br><br><br><br>          |Used to redirect output. We can take<br>he output of a command and send it<br> to a file. This operator will overwrite<br>anything that exists in the file.|$ `echo` hey `>` welcome<br>$ `cat` welcome<br>hey<br><br>|
|`>>`<br><br><br><br>         |This redirector does the same thing, but<br>instead of overwriting, it will just add the<br>output to the bottom of the file.<br><br>|$ `echo` rose `>` welcome<br>$ `cat` welcome<br>hey<br>rose<br>|
|||
|SSH<br><br><br><br><br><br><br>$ `ssh`<br><br>|Allows us to remotely execute commands<br>on another device remotely. Any data<br>sent between the devices is encrypted<br>when it is sent over a network such<br>as the Internet.<br><br><br>Log as <strong><em>username</em></strong> in <strong><em>IPaddress</em></strong> with<br>a provided password.|-<br><br><br><br><br><br><br>$ `ssh` username`@`IPaddress<br><br>|
|$ `man`<br><br><br><br><br><br><br><br><br><br><br>                     ||$ `man` `ls`<br>...<br>DESCRIPTION<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; List  information  about  the FILEs<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (the current directory by default).<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sort entries alphabetically<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if none of -cftuvSUX nor<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --sort  is  specified.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ...<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -a, --all  do not ignore<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; entries starting with .|
|||
|`touch`<br><br>|Creates a blank file.<br><br>|$ `touch` support<br>File <em>support</em> was created.|
|`file` [OPTION...] [FILE...]<br><br>         |Determine type of FILEs.<br><br>|$ `file` a<br>a: UTF-8 Unicode text|
|`mkdir` [OPTION]... DIRECTORY...<br><br>     |Create the DIRECTORY(ies), if they do not already exist.<br><br>|$ `mkdir` study<br>Directory <em>study</em> was created.|
|`cp` [OPTION]... [-T] SOURCE DEST<br>        |Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.<br>|$ `cp` support support1<br>File <em>support1</em> was created.|
|`mv` [OPTION]... [-T] SOURCE DEST<br><br><br><br><br>        |Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.<br><br><br><br><br>|$ `mv` support1 support2<br>File <em>support1</em> was renamed.<br><br>$ `mv` support2 study<br>File <em>support1</em> was moved to directory <em>study</em>.|
|`rm` [OPTION]... [FILE]...<br><br>           |Remove (unlink) the FILE(s).<br><br>|$ `rm` support<br>File <em>support</em> was removed.|
|`su` [options] [-] [<user> [<argument>...]]|Change the effective user ID and group ID to that of <user>.||
|`su -l` |Root is assumed.||
| File Permissions<br><br>|[Owner][Groupe][Others]<br>`r` = read; `w` = write; `x` = execute|rwxrwxrwx<br><br>|
|`rm -R` ...<br><br>|Remove directory.<br><br>|$ `rm -R ` support<br>Directory <em>support</em> was created.|

</p></div>

<br>
<h2>⦿ &nbsp; Network Traffic Analysis</h2>
<p>Interpreting network protocols, analysing packets, spotting anomalous traffic, and understanding network data flow.</p>

<h2>⦿ &nbsp; Web Application Security</h2>
<p>Recognising web vulnerabilities, understanding how web apps work, and applying pentesting methods to find weaknesses.</p>


<h2>⦿ &nbsp; Security Operations</h2>
<p>Applying defensive security: log analysis, threat detection, incident response, and SOC monitoring tools.</p>


<h2>⦿ &nbsp; Password Attacks and Credential Security</h2>
<p>Understanding brute-force and dictionary attacks, password cracking techniques, and authentication mechanisms.</p>

<h2>⦿ &nbsp; Malware Analysis Fundamentals</h2>
<p>Identifying malware types, understanding their behaviour, and using basic static and dynamic analysis techniques.</p>
