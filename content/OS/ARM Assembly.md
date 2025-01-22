---
tags:
  - assembly
  - programming
  - ARM
---
Most used CPU instruction set.
It is a [[Reduced Instruction Set Compiler|RISC]], making it very barebones.
### Create assembly program file(VS CODE)
1. Open vs code
2. New empty project
3. Create a .asm file
4. Right Click project > build dependencies > build customizations
5. Enable masm
6. Right Click .asm file > Properties > general > Item type
7. Change item type to Microsoft Macro Assembler
### Assembly structure

1. starts with a header. Lines denoted with a ; semicolon. Plain text like file name, file author, file description
2. file information like storage space, processor type, model type, exit protocol
3. .data segment that stores all variables. Variables not initialized will be followed by a ?
4. .code segment where the program algorithms are run


### Registers

Areas in memory that are very close to the cpu. Can be accessed quickly and written to quickly. But we have a limited amount of things to store. Data is stored in hexadecimal in 4 bits. ARM processors are all 32 bit

32 bit architecture will allow us to read from the word(32 bit in this case). A halfword is 16 bit a quarter word is 8 bit

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv9z_tmp_77a96e3226c0d1e7.png)

Certain registers are special. Registers r0-r6 are general purpose. You can store strings or ints here no worries.

r7 is special in relation to system calls. It dictates termination to the program. if r7 is 1, then terminate program

sp is stack pointer. Pointer to tell us what memory address the program starts at.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv9z_tmp_caf67dd1c6438248.png)

Memory and its addresses are separated by 4 bytes of hexadecimal. 00000010 is in hexadecimal so its 16.

lr is the link register. Stores the location that a function should return back to. Similar to the return used in higher level languages

pc is the program counter. Keep track of the next line to execute. this allows us to use breakpoints in debugging.

cpsr register is used to store information about the program. Can set flags in memory to tell us that this specific number is negative. It's a flagman. It sets certain flags for special edge cases

spsr register stores the cpsr data so it can be returned upon program reload.

  

### Syntax

(_) label You can think of the label as a function. A way to divy up to code. Using underscore means it is a label reserved in all programs. Most labels do not require underscore.

(:) terminator of label part of defining label. Just the terminator part of a label

(.global) global declares will define the labels. For every label you want

(.equ) constants you declare constants. Assign a name to a value

(.data) allocate storage you can create integers, lists

(.word) 32/64 bit datatype create some space in memory. Size varies from given arguments

(.ascii) ascii string create an ascii string. No null terminator given, must manually insert one

(.string/.asciz) string create an ascii string with a null terminator

(.-) len of string counts length of string until it meets null terminator

(#) digit a base 10 digit. Can be used like mov eax,#30 to store 30 in eax

(=) equals value of label stored

([]) sqrbracket value of register

({}) curlbracket several items

(!) preincrement assigning a value of an address incremented by a specific number. For example: ldr 32, [r0,#4]! Will assign r2 the value at address r0+4.

(//) comment this be a comment

  

### Operations/Opcode

Like x86, these are operations to modify memory. Know that operations can be capital letters aswell
They follow the structure: operation [operands,..]

| operation                                | example        | explanation                                                                                                               |
| ---------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------- |
| mov (move)                               | mov ebx, 123   | ebx = 123                                                                                                                 |
|                                          | Mov eax, ebx   | eax = ebx                                                                                                                 |
| add                                      | add ebx, ecx   | ebx += ecx                                                                                                                |
| adc                                      | adc ebx, ecx   | ebx += ecx BUT if (ebx + ecx) > 0xFFFFFFFF, then it carries the remainder in cpsr.TLDR: ebx = ecx 100% regardless of size |
| sub                                      | sub ebx, edx   | ebx -= edx                                                                                                                |
|                                          | sub r2,r1,r0   | r2 = r1-r0                                                                                                                |
| subs                                     | subs r2,r1,r0  | r2 = r1-r0 BUT it keeps negative sign                                                                                     |
| mul (multiply)                           | mul ebx        | eax = ebx                                                                                                                 |
| div                                      | div edx        | eax /= edx                                                                                                                |
| swi (software interrupt)                 | swi 0          | Software interruption. Check if program ends                                                                              |
| ldr (stack->register)                    | ldr r0,=list   | r0 = data at list                                                                                                         |
|                                          | ldr r1,[r0]    | r1 = data at address of r0                                                                                                |
|                                          | ldr r2,[r0,#4] | r1 = data at address of r0+4                                                                                              |
| str (register->stack)                    | Str r1,[r0]    | Store value of r1 into the location of r0.                                                                                |
| and                                      | and r0,r1,r2   | r0 = r1 and r2                                                                                                            |
|                                          | And eax,0xFC   | Clear eax registry(unless 0xFC values exist)                                                                              |
| orr (or)                                 | orr r0,r1,r2   | r0 = r1 or r2.                                                                                                            |
| eor (xor)                                | eor r0,r1,r2   | r0 = r1 xor r2                                                                                                            |
| mvn (move negative)                      | mvn r0,r0      | r0 = not r0 Move to source and negate. A true would turn false                                                            |
| lsl (logical left shift)                 | lsl r0,#1      | Logical left r0 one time                                                                                                  |
| rsl (logical right shift)                | rsl r0,#2      | Logical right r0 2 times                                                                                                  |
| lsr (rotational left shift)              | lsr r0,#1      | Rotational left r0 one time                                                                                               |
| rsr (rotational left shift)              | rsr r0,#2      | rotational right r0 2 times                                                                                               |
| cmp (compare)                            | cmp r0,r1      | Compare r0 and r1. Opens up the door for branches                                                                         |
| bgt (branch if greater than)             | bgt some_label | Will branch if previous compare have first value larger than second into some_label function                              |
| bge (branch if greater than or equal to) | bge some_label | branches to another label if previous compare’s 1st arg is greater or equal to 2nd arg                                    |
| bal (branch always)                      | bal some_label | Unconditionally branch to this label. unavoidable                                                                         |
| blt (branch less than)                   | blt some_label | Branches if 1st argument is smaller than second argument                                                                  |
| beq (branch equals)                      | beq some_label | Branches if both arguments are equal                                                                                      |
| bne (branch not equal)                   | bne some_label | Branches if both arguments not equal                                                                                      |
| bx (branch to register)                  | bx lr          | Branch to linked register                                                                                                 |
| bl (branch label)                        | bl some_label  | Branch to some label                                                                                                      |
| push (push onto stack)                   | push {r0,r1}   | Push r0 and r1 into stack                                                                                                 |
| pop (pop from stack)                     | pop {r0,r1}    | Retireve r0 and r1 from the stack                                                                                         |

### Chaining operations

Certain operations can be completed in tandem with other operations. An example being move and logical shift

mov r1,r0,lsl #1

will first assign r1 to r0 and then logical shift it by one

### Conditional instructions

Like chaining operations, we can also chain conditions to operations. Eg. addlt only triggers if the first number is smaller than the second

  

### Conditions

To create conditional statements, it is worthy to note that a condition requires 2 or more branches. In order to branch, some code must be skipped.

1. Compare 2 registers/memory/imm eg. CMP r0,r1
    
2. Branch into a different label using some branch like bgt
    
    1. Code after branch is else statement(will be skipped if true)
        
    2. Code inside label is if statement
        


### Loops

Simply branch to another function or branch back to current function to loop.

Know that to iterate through a list, you must have a null terminator OR use 0xaaaaaaaa(blank memory) to sequence the end of the list. For each loop, check if it is the end, then go on

  

### Link register

If we want to go back to the original label that issued another label, we must consult the lr register.

To branch to the link register, use bx lr. Very shrimple

  

### Push and pop

To preserve variable integrity, you must secure them into the memory. Remember that r0,r1,r2….. Is all volatile and very temporary. To preserve them, use push to push them onto the stack

push {r0,r1}

To retrieve these values again, you must use pop

pop {r0,r1}

  

### Hardware interactions

if you are declaring variables within the 0xf…… range, then you must first declare them as constants in the .equ

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv9z_tmp_d91e11d57e112248.png)

Look at the hardware devices here. Each have their own memory address. If we create a constant with memory address 0xff200040, then we can access switches.

Then, if you ldr the value of the constant into a register, then ldr the register into another register like such:

ldr r0,=constantforswitches

ldr r1,[r0]

You can flick those buttons in switches panel to change the value of r1

### Namespaces

These allow for variable/function names to be repeated through the global and local concept. To create a local label, just put a period . at the begining of their labelname.

This labelname wil remain tied to whatever actions are below it until it is declared again with a different set of actions.

### Datatype declaration 2. Declaring size

We know that there is 3 parts to declaring variables inside the section .data segment. Variablename declaresize value. For declaresize, this can be in several sizes:

  


|characters|size|
|-|-|
|db|Declare bytes|
|dw|Declare word|
|dd|Declare double word|
|dq|Declare quad word|

