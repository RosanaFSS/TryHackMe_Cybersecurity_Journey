<h1>Hi</h1>
<br>

<h1>Operating Systems Fundamental Skills</h1>
<p>Understanding Windows and Linux architecture, file systems, user management, security, and basic command-line administration</p>

<h2>Linux</h2>
<p>Linux powers: <br>
  
- Websites that you visit<br>
- Car entertainment/control panels<br>
- Point of Sale (PoS) systems such as checkout tills and registers in shops<br>
- Critical infrastructures such as traffic light controllers or industrial sensors<br>
- Phones, and similar small computing devices<br>
- And much much more!</p>

<div align="left"><p>

|Command/<br>Keys             |Task<br><br>                                                       |Example<br><br>            |
|:----------------------------|:------------------------------------------------------------------|:---------------------|
|$ `whoami`<br><br>           |Tells you who you are on the system.<br> <br>                       |`www-data`<br><br>   |
|`↑` and `↓` arrow keys<br><br>|Press it to scroll through commands<br>that you have already entered.<br>|-<br><br>        |
|`echo`<br><br><br><br><br>$ `echo` rose<br><br><br><br><br>$ `echo` "beautiful rose"<br><br>|Is a building-block for the very<br>important skill that is being<br>able to send and store<br>information in Linux.<br><br>Output some specific text that is provided.<br><br><br><br><br>Output multiple words.<br><br>|-<br><br><br><br><br>$ `echo` rose<br>rose<br><br><br><br>$ `echo` "beautiful rose"<br>beautiful rose<br>|    
|$ `ls`<br><br><br><br>$ `ls -a` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OR<br>$ `ls --all`<br><br><br><br>`ls --help`<br><br><br><br><br>$ `ls -lh`<br><br><br><br><br>|List what's in the current folder.<br><br><br><br>Do not ignore entries starting with `.`<br><br><br><br><br>List the possible options that the<br>command accepts, provide a brief<br>description and example of how<br>to use it.<br><br>List permissions:<br>`l` use a long<br>listing format<br>`h` with -l and -s,<br>print sizes like 1K 234M 2G etc.<br>|$ `ls`<br>access.log<br><br><br>$ `ls -a`<br>.   .bash_logout  .cache    important  myfolder<br>..  .bashrc       .profile  myfile     unknown1<br><br><br><br><br><br><br><br>-<br><br><br><br><br>|
|$ `find`<br><br>             |Search for files by their name.<br><br>                             |$ `find` -name passwords.txt<br>./folder1/passwords.txt|
|$ `cd`<br><br>               |Change directory — move into a folder.<br><br>                     |$ `cd` folder1<br><br>          |
|$ `pwd`<br><br>              |Print working directory —<br>"where am I?"<br>                      |$ `pwd`<br><br>                 |
|$ `cat`<br><br>              |Show the contents of a file.<br><br>                                |$ `cat` passwords.txt<br>password123<br> |
|$ `grep`<br><br><br><br><br> |Searches inside for text.<br><br><br><br><br>                       |$ `grep` "password123" passwords.txt<br>password123<br><br>$ `grep` "THM" access.log <br>... THM{...}|
|`&`<br><br><br><br><br><br>  |Runs the command, but does not wait for<br>it to finish before you can do anything else.<br>The command runs in the backgorund,<br>and is helpful for commands that might<br>take a while to complete, or ones that<br> you want to keep running.|-<br><br><br><br><br><br>|
|`&&`<br><br><br>             |Runs both commands, but <strong><em>waits for the<br>first command to finish first</em></strong>, before<br>the next. Like a set of dominoes.<br>|-<br><br><br>|
|`>`<br><br><br><br>          |Used to redirect output. We can take<br>he output of a command and send it<br> to a file. This operator will overwrite<br>anything that exists in the file.|$ `echo` hey `>` welcome<br>$ `cat` welcome<br>hey<br><br>|
|`>>`<br><br><br><br>         |This redirector does the same thing, but<br>instead of overwriting, it will just add the<br>output to the bottom of the file.<br><br>|$ `echo` rose `>` welcome<br>$ `cat` welcome<br>hey<br>rose<br>|
|SSH<br><br><br><br><br><br><br>$ `ssh`<br><br>|Allows us to remotely execute commands<br>on another device remotely. Any data<br>sent between the devices is encrypted<br>when it is sent over a network such<br>as the Internet.<br><br><br>Log as <strong><em>username</em></strong> in <strong><em>IPaddress</em></strong> with<br>a provided password.|-<br><br><br><br><br><br><br>$ `ssh` username`@`IPaddress<br><br>|
|$ `man`<br><br><br><br><br><br><br><br><br><br><br>                    ||$ `man` `ls`<br>...<br>DESCRIPTION<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; List  information  about  the FILEs<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (the current directory by default).<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sort entries alphabetically<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if none of -cftuvSUX nor<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --sort  is  specified.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ...<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -a, --all  do not ignore<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; entries starting with .|
|`touch`<br><br>|Creates a blank file.<br><br>|$ `touch` support<br>File <em>support</em> was created.|
|`file` [OPTION...] [FILE...]<br><br>         |Determine type of FILEs.<br><br>|$ `file` a<br>a: UTF-8 Unicode text|
|`mkdir` [OPTION]... DIRECTORY...<br><br><br> |Create the DIRECTORY(ies), if they<br>do not already exist.<br><br>|$ `mkdir` study<br>Directory <em>study</em> was created.<br><br>|
|`cp` [OPTION]... [-T] SOURCE DEST<br>        |Copy SOURCE to DEST, or multiple<br>SOURCE(s) to DIRECTORY.<br>|$ `cp` support support1<br>File <em>support1</em> was created.|
|`mv` [OPTION]... [-T] SOURCE DEST<br><br><br><br><br><br>        |Rename SOURCE to DEST, or move<br>SOURCE(s) to DIRECTORY.<br><br><br><br><br>|$ `mv` support1 support2<br>File <em>support1</em> was renamed.<br><br>$ `mv` support2 study<br>File <em>support1</em> was moved to directory <em>study</em>.<br><br>|
|`rm` [OPTION]... [FILE]...<br><br>           |Remove (unlink) the FILE(s).<br><br>|$ `rm` support<br>File <em>support</em> was removed.|
|`su` [options] [-] [<user> [<argument>...]]<br><br><br>`su -l`|Change the effective user ID and group ID<br>to that of <user>.<br><br>Root is assumed.||

</p></div>

<br>
<h3>File Permissions</h3>
<p>

- Many Linux commands use numeric values<br>
- You can quickly identify security risks<br>
- You can control who can access sensitive files</p>

<div align="left"><p>

|`ls -lh`<br><br><br><br><br><br><br><br>`chmod`<br>|Shows [Owner] [Group] [Others]<br>Read (`r`) = `4`; Write (`w`) =  `2`; Execute (`x`) = `1`<br><br>rwxr-xr-x	&nbsp;&nbsp; `755`	Owner can do everything, others can read and execute<br>rw-r--r-- &nbsp;&nbsp;	`644`	Owner can read/write, others can only read<br>rwx------	&nbsp;&nbsp; `700`	Only the owner has access<br><br><br>Change the mode of each FILE to MODE.<br>|[Owner] &nbsp; [Group] &nbsp; [Others]<br>rwxrwxrwx<br>[&nbsp; rwx &nbsp;&nbsp;] &nbsp; [&nbsp; rwx &nbsp;&nbsp;] &nbsp; [&nbsp; rwx &nbsp;&nbsp;]<br>[&nbsp; &nbsp; 7 &nbsp;&nbsp;&nbsp;] &nbsp;&nbsp;&nbsp; [&nbsp; &nbsp; 7 &nbsp;&nbsp;&nbsp;] &nbsp; [&nbsp; &nbsp; 7 &nbsp;&nbsp;&nbsp;]<br><br><br><br><br>`chmod` 750 filename.extension<br>|
|:----------------------------|:------------------------------------------------------------------|:---------------------|

</p></div>

<br>
<h3>𝗖ommon Directories & Files</h3>
<div align="left"><p>

|`etc` &nbsp;&nbsp;&nbsp; Stores system files that are used by OS.<br><br>`var` &nbsp;&nbsp;&nbsp; Stores data that is frequently accessed<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; or written by services or applications<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; running on the system.<br><br>`root` &nbsp;&nbsp;  Is the home for the "root" system user.<br><br>`tmp` &nbsp;&nbsp;&nbsp; Is volatile and is used to store data that is only<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; needed to be accessed once or twice.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; It is similar to how RAM on a computer works.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Any user can write to this folder by default.|`/etc/passwd`, `/etc/shadow`, `/etc/sudoers`, `/etc/sudoers.d` files.<br><br>`/var/backups`, `/var/log`, `/var/tmp`, `/var/opt`, `/var/www` files.<br><br><br><br>`/home/root`<br><br><br><br><br><br>|
|:------------------------------------------------------------------|:---------------------|

</p></div>

<br>
<h3>Terminal Text Editors</h3>
<div align="left"><p>

|`nano` &nbsp;&nbsp;&nbsp; Stores system files that are used by OS.<br><br>`VIM` &nbsp;&nbsp;&nbsp; Stores data that is frequently accessed|.|
|:------------------------------------------------------------------|:---------------------|

</p></div>

<br>
<br>

```bash
rm -R` ... Remove directory.   $ `rm -R ` support   Directory support removed.|
```


<br>
<h1>Network Traffic Analysis</h1>
<p>Interpreting network protocols, analysing packets, spotting anomalous traffic, and understanding network data flow.</p>

<br>
<br>
<h1>Web Application Security</h1>
<p>Recognising web vulnerabilities, understanding how web apps work, and applying pentesting methods to find weaknesses.</p>

<br>
<br>
<h1>Security Operations</h1>
<p>Applying defensive security: log analysis, threat detection, incident response, and SOC monitoring tools.</p>


<h1>Password Attacks and Credential Security</h1>
<p>Understanding brute-force and dictionary attacks, password cracking techniques, and authentication mechanisms.</p>

<br>
<br>
<h1>Malware Analysis Fundamentals</h1>
<p>Identifying malware types, understanding their behaviour, and using basic static and dynamic analysis techniques.</p>
