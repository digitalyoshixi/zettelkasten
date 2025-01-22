---
tags:
  - 0xInfection
  - GDB
---

### Part 20: instruction code handling:

Every process has a PID(process ID) which is a numerical value assigned to each running program.

Instruction code is a group of bytes that tells the computer to perform specific operations. From a glance, instruction code isn’t any different than bytes that contain data, this is because it is in bytes duh.

Now, the ESP keeps track of where the data area in the stack starts. The EIP helps the CPU keep track of which instruction codes have been processed and which to process next

  

We are given this tool called objdump. This tool allows us to view assembly code of a program. Creating a executable using gcc of a c file, then you can type objdump -d -M intel [filename]. You can also pipe this into a grep to get smaller results

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivaj_tmp_db6f98febc4b1227.png)

This is a snippet of an output of a c program. Just a boilerplate c program that does nothing except run and stop.

On the left we have memory addresses, in the center we have opcodes and on the right we have our human readable assembly

opcode 55 means push EBP. Opcode 89 e5 means mov EBP, ESP
