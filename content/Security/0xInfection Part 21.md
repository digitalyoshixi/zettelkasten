---
tags:
  - 0xInfection
  - GDB
---

### Part 21: How to compile a program:

To compile a raw c program to executable, use gcc -ggdb -m32 -o [filename] [filename.c]

To compile a raw c program to raw assembly, use gcc -S -m32 -O0 [filename.c]

The big thing here is the -S flag. It converts c to AT&T syntax. -m32 creates an executable and -O0 will tell compiler binary optimization. We have 0 so no optimization, changing it to 1,2 or 3 would make the code so much smaller but omit some information.

.s is our assembly file extension.

To convert assembly code into a binary object file, use gcc -m32 -c [filename.s] -o [filename.o]

To create binary executable from the binary code, use gcc -m32 [filename.o] -o [filename]

  

Keep in mind we are using AT&T syntax now. If you run objdump, then you will view the result:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivaj_tmp_20acc6ae11409309.png)

Notice how the source and destinations are reversed and each one starts with a %

  

Now that we have the executable, we can start disassembling.

1. gdb -q [filename] to open the file
    
2. b main. Set breakpoint to main function
    
3. r. Run the program
    
4. disas. disassemble
    

  

Now if we want to make an assembly code then compile it, the process is as such

1. as –32 -gstabs -o [filename.o] [filename.s]
    
2. ld -m elf_i386 -o [filename] [filename.o]
    
3. ./[filename]

### Intel 32bit compiling

To compile your newly written assembly, type:

nasm -f elf32 [filename].asm

ld -m elf_i386 -0 [filename] [filename.o]

  
