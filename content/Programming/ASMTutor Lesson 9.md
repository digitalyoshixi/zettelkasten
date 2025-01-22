---
tags:
  - x86
  - ASMTutor
---
### BSS Bullshit

BSS stands for block started by symbol. Its a place in the program to reserve memory for uninitialized variables that will change in value during execution. To declare a bss variable, you will need to allocate space like such:
 
|method|explanation|
|-|-|
|resb|Reserve space for byte|
|resw|Reserve space for word|
|resd|Reserve space for double word|
|resq|Reserve space for double precision float(quad word)|
|rest|Reserve space for extended precision float|

Following the method, you will give it a quantity. 1 byte, 2 bytes, etc… you really just need resb, but the other methods can be used aswell if you find them better

An example bss variable declared:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbx_tmp_e8028d336da97a1e.png)

### Lesson 9 sys read

MAN I'M A BOOKWORM. I AM A READER, A BOOK READER, A WORM EATER. This is how its done:

eax is 3 for sysread call

ebx is the file we read from. 0 for sys in

ecx is address of bss variable

edx is the max bytesize of our bss variable

  

For inputs, the program checks until a linefeed.