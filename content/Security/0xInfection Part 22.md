---
tags:
  - reverse_engineering
  - x86
  - AT&T
---

### Part 22: x86 AT&T syntax pt1:

Every assembly program is divided into 3 sections

1. Data section. Section used for declaring constants and initial variables
    
2. BSS section. Section used for declaring uninitialized data or variables.
    
3. Text section. Section used for actual code. Begins with global _start
    
In AT&T syntax, we use the # symbol to write comments.


Basic instructions are written as such: mnemonic [operands]

Mnemonic is the name of the operation

Operands is the arguments required for the mnemonic

On occasion you may also have labels. Labels start with a period like .section, .data


  

### AT&T 32bit Operations/Opcode

  

|operation|example|pseudo demo|
|--|--|--|
|movl(move 32bit)|movl $100, %eax|eax = 100|
||movl (%eax), %ebx|ebx = eax|
||Movl $0x50, buffer|buffer(in memory) = 80|
|int (system interrupt)|int $0x80|System call. Only|

Certain register like eax will be able to regulate system calls. For example if you move 1 into register eax, and 0 into register ebx, then call a system interrupt. you will exit with a code of 0

  

To compile your newly written assembly, type:

as -32 -o [filename.o] [filename.s]

ld -m elf_i386 -o [filename] [filename.o]

### System call 0x80

In linux, there are 2 distinct areas of memory, user space and kernel space. These memories are further divided up. User space has stack, heap, assembly code, etc. Kernel space has a dispatcher, vector table, etc.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivaj_tmp_2f048ef0aa67b370.png)

As is common with assembly code, whenever we move out to a segment of memory that is not in the ASM code, we set the return address to the next line, so when we do finish what we were doing, we can return safely.

Now some linux versions are utilizting protected mode meaning you do NOT have access to the kernel space. We dont want malware modifying the OS and track keystrokes, activities and such.

Very often aswell, linux will rearrange and modify their os architecture meaning it will be a pain to play with this stuff.

Still, certain things will require kernel access. our gateway to communicating with the linux kernel is through use of kernel services call gate. This is a protected gateway between user space and kernel space and it is accessed through software interrupt 0x80.

  

At the very bottom of memory, where address 0 exists is a lookup table with 256 entries. This table is called the interrupt table and reserves 1024 bytes. NO OTHER CODE can be put here, the table cant be manipualted. Every entry is a memory address including segment and offset portions. Each address is called an interrupt vector which point to different kernel services. 0x80 is the lookup table for the system call service.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivaj_tmp_646634f685502621.png)

When we return using our return address, this is called IRET(interrupt return).