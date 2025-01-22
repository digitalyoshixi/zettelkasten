---
tags:
  - ASMTutor
  - x86
  - networking
  - syscall
---
### Lesson 34 socket write

Similar to lesson 33. We will use the same file descriptor we get from socket accept. We will also use sys write to write the incoming socket connection. For this write, we are going to format the header in

eax is 4

ebx is socket file descriptor value

ecx is address of format variable

edx is length of variable

This is an example format:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivct_tmp_b9ac01c803e26312.png)

And it will output hello world once we send the curl command: curl http://localhost:9001