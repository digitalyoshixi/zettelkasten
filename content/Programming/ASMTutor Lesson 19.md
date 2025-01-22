---
tags:
  - x86
  - ASMTutor
  - syscall
---
### Lesson 19 Execute command

Pivotal because we are not making our own functions now, we are using another person’s work for ourselves. We will use the sys_exec system call. This is actually a family of syscalls. There are several add ons we can give to sys_exec that can modify where arguments are given. Here is a list of them below:

**e** - executable path. Refers to the path for the executable file you want to execute. It is a null terminated string containing the full path or relative path to the executable file

**i** - list of command line arguments. Give an array of null terminated strings to pass to the command line. Terminated by a null value

**p** - list of environment variables. Give a pointer to an array of null terminated strings to pass to the command line. Uses the PATH environment variable

**v** - vector pointers. Essentially just eip all combined. Arrau of pointers which point to null terminated strings. First pointer points to executable path, subsequent pointers point to command line arguments. Terminated by null pointer

  
For our purposes, we will use the system call sys_execve.

It requires this:

eax is 11 for sy execve

ebx is the address of a string of the file to execute.

ecx is the address of the start of the arguments array.

edx is the address of the string of the environment variables

  

The simplest example is to look at this:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivc8_tmp_353c3beb41707267.png)

Ecx holds the arguments array. This means all arguments. It saves the file location as the first item, an argument for the second item and a null terminator to show the array has ended as its final item.

What is the point of making ebx the first item then? The bloody blokes haven’t the ingenuity to change what they’ve done.