---
tags:
  - syscall
  - x86
  - ASMTutor
---
### Lesson 27 File updating (sys_iseek)

Its called seek, and for the reason of hide and seek but you seek and actually this doesn’t make sense why is it called seek? Who knows, the developers are long gone. The first part is just opening the file. Once you open the file, you navigate the file like a spider. Think of this update like a selection. You start somewhere, and then you select all characters to replace. If you dont want to repleace and just append, then make the offset 0 and youre good to go. Edx and ecx are the important registers. Edx is whence you start and ecx is the offset. Here is how to interrupt:

eax is 19

ebx is file descriptor value

ecx is cursor offset

edx is 0, 1 or 2 for seek set(beginning), seek cur(current offset) or seek end(end of file)