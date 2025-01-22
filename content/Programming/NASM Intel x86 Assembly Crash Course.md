---
tags:
  - x86
  - assembly
---

I've got decision paralysis. BUT, I think i've finally found the course.

[https://www.youtube.com/watch?v=DNPjBvZxE3E&list=PLg8UXNUgg11OdSQPUfFFtdPOclD1C2wsI](https://www.youtube.com/watch?v=DNPjBvZxE3E&list=PLg8UXNUgg11OdSQPUfFFtdPOclD1C2wsI)

Comments are written using ; semicolon

  

### Sections

Harken back to [may 28](#h.glwoosqgexl3), we learn there are 3 sections.

- Data for declaring constants like strings, magic numbers, terminating strings.
    
- BSS section to reserve memory for uninitialized data that will arrive in the future
    
- Text for writing the actual code.
    

  

### Exporting

For 64bit:

1. nasm -f elf64 -g file.asm -> file.o
    
2. ld -m elf_x86_64 -o file file.o
    
    1. There's also an alternative way by using the gcc compiler
        

ld also requires there be a _start: to actially link object file to executable file.

  

For 32bit:

1. Nasm -f elf32 -g file.asm -> file.o
    
2. ld -m elf_i386 -o file file.o
    

  

Differences vary vastly between 32bit and 64bit. One example being registers are called different. eax in 32bit is rax in 64bit. Actually u can still use eax in 64bit, since you know, backwards compatibility.

  

### Registers(again)

Hardware implemented variables. There are transistors in the cpu that hold data. Either 32bit or 64bit wide but they are hardcoded and always exist. If you want to perform operations on data, then you must load them inside these registers.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbn_tmp_a5222c46eef09580.png)

AH is upper 8 bits of EAX, AL is lower 8 bits of AX. An important thing to note of the image above, AH,AL,BH,BL,CH… are all dependant on their parent EAX,EBX,ECX,EDX to get their value. If you are using AH or AL or… for anything specific, then changing EAX,EBX… will alter them. I believe this is bad practice to even modify AH or AL, but idk anything about practices to begin with.

AX,BX,CX,DX are the first 16 bits and are NOT accessible. unfortunately.

ECX is called the counter register. We tend to use it as loop iterator variable. There are hardware implementations that make this register increment the fastest, so use this register always whenever you are looping.

EAX is called the accumulator register. It should be used to keep the result of your arithmetic.

ESI(source index) and EDI(destination index) are generally used to copy large datasets.

ESP(stack pointer) will be moved every time you pop or push

EBP(base pointer) will point to bottom of stack

  

### Instructions/Operands

To view all operands, go here: [http://ref.x86asm.net/coder32.html](http://ref.x86asm.net/coder32.html)


|**operand name**|**purpose**|**example**|**explanation**|
|-|-|-|-|
|mov(move)|Copies value of a source to destination.<br><br>mov dest, src|mov eax , 3|Eax is now 3|
|movzx(move with zero extend)|Similar to movzx in replacing destination value with source value. Zero out unused space in the register. Mov does this anyways, however it does not have the adaptability that movzx has. Movzx is used mainly when moving smaller values into larger registers|movzx eax, 3|eax is now 3. All unused bitspaces are now 0<br><br>Example: if eax was 11111111 before, and after we did movzx eax, 3, then eax would wipe out all unused binaries to zero and just keep 00000011(binary of 3)|
|||movzx eax, byte ptr [ebx]|If ebx is an array, then move the first byte of the array to eax. BUT if eax is 4 bytes in size(32bit), then we zero out the other unused bytes|
|movsx(move with sign extend)|Same concept as movzx except this is for signs. Sign extend up to the end of the register to be able to hold the current value. Usually the leftmost bit is for storing sign.|mov ebx, -3<br><br>movzx eax, bl|In this case in order to turn eax into a negative value, you must load the negative value first into a register that has the same byte size.|
|||movzx eax, byte -3|This is how you load a negative value without first loading it into another register.|
|cmp(compare)|subtracts second argument from the first and then changes flags accordingly. Usually paired with a jump operand to perform conditional structure.|cmp eax,ebx|eax - ebx if unsigned, may or may not change carry flag<br><br>eax - ebx if signed, may or may not change the overflow flag<br><br>if eax - ebx = 0 then zero flag will change, if not then zero flag wont change.|
|**Bitwise operations. These check the actual bis to see if values are same**||||
|and|Check 2 values. And dest, src. Any differences between the dest and src will lead to the corresponding bit in dest to perform go through the and logic. dest will hold the new value.|mov eax, 30<br><br>mov ebx, 78<br><br>and eax,ebx|So we compare binary of eax and binary of ebx.<br><br>eax = 00011110<br><br>ebx = 01001110<br><br>Lets work through each binary compare 1 by one. Starting left to right 8 times.<br><br>0 and 0. This results in 0<br><br>0 and 1. This results in 0<br><br>0 and 0. This results in 0<br><br>1 and 0. This results in 0<br><br>1 and 1. This results in 1<br><br>1 and 1. This results in 1<br><br>1 and 1. This results in 1<br><br>0 and 0. This results in 0<br><br>So final answer is 00001110.<br><br>Know that the logic of and only allows there to be 2 ones in order for it to return one.|
|or|Check 2 values in their differences in binary. 1 if any of the compared values have 1 in it. 0 if none of compared values have 1 in it|or eax,ebx|So similar to and, just that it uses or logic instead|
|xor|Check 2v values in their differences in binary. 1 if only one of the compared values have 1 in it. 0 if none or both have 1 in it.|xor eax,ebx|Similar to and, uses xor logic instead|
|||xor eax,eax|Zeroes out eax. Faster operation that clear or delete operands. This is how it goes:<br><br>eax = 11010010<br><br>If we eax it by itself we compare<br><br>11010010<br><br>11010010<br><br>1 and 1 = 0<br><br>1 and 1 = 0<br><br>0 and 0 = 0<br><br>1 and 1 = 0<br><br>0 and 0 = 0<br><br>0 and 0 = 0<br><br>1 and 1 = 0<br><br>0 and 0 = 0<br><br>So result is 00000000|
|test|Update zero flag if the result of an AND operation is zero. THIS DOES NOT CHANGE THE REGISTER GIVEN, ONLY THE FLAG|mov eax, 10<br><br>mov ebx, 5<br><br>test eax,ebx|Perform the and check between eax and ebx<br><br>eax = 1010<br><br>ebx = 0101<br><br>The result is 0000. This triggers the zero flag to be on|
|||mov eax,10<br><br>mov ebx,6<br><br>test eax,ebx|eax = 1010<br><br>ebx = 0110<br><br>Result is 0010. This is not zero, this is 2. We dont trigger any flag|
|**Arithmetic operations**||||
|add|Adds to the first argument, the value of the second|add eax, ebx|eax = eax + ebx|
|||add eax, 6|eax = eax + 6|
|||add edi, ‘0’|Turns edi into the ascii version of itself|
|sub(subtract)|Subtracts from the first arguments, the value of the second|sub eax, ebx|eax = eax - ebx|
|||sub eax, 7|eax = eax - 7|
|mul(multiply)|Multiply eax by another register. Intentional or unintentionally, it changes edx register aswell.|mov ax, 15<br><br>mul bx|dx:ax = ax * bx<br><br>ax will equal ax*bx granted the product can fit within ax’s byte size.<br><br>If not, and its larger, then dx will store the larger value of the product.|
|||mov eax, 15<br><br>mul ebx|edx:eax = eax*ebx|
|div(divide)|Divide the eax by a register given. Changes edx register as well|mov ax, 15<br><br>div bx|ax Rdx = dx:ax/bx<br><br>dx:ax will store the entire value of ax<br><br>dx:ax/bx will be stored in ax<br><br>Remainder of the division will be stored in dx|
|||mov rax, 15<br><br>div rbx|rax Rrdx = edx:eax/ebx|
|idiv(integer division)|Divide eax by the argument given. Store the quotient(rounded down) result in eax, and the remainder in edx|mov eax, 14<br><br>mov ebx, 5<br><br>idiv ebx|eax = 14/5(rounded down) = 2.8(round down) = 2<br><br>edx = 14 mod 5 = 4|
|inc(increment)|Add 1 to register|inc eax|eax = eax + 1|
|dec(decrement)|Subtract 1 from register|dec eax|eax = eax - 1|
|**Jump operations**||||
|jmp(jump)|Jump to a specific label. Used to skip lines and create non-linear program flow|jmp label|Changes EIP to the memory address of wherever the label is. Next execution will execute label code.|
|je(jump if equal)<br><br>jz(jump zero)|Jump to a specific label if the previous command above resulted in zero flag being 1. Traditionally used after a compare operand<br><br>jz is exact same as je|cmp eax, 5<br><br>je label|If the value in eax is equal to 5, then jump to label|
|jne(jump if not equal)<br><br>jnz(jump not zero)|Jump to a specific label if the previous command above resulted in zero flag being 0. Traditionally used after a compare operand<br><br>Jnz exact same as jne|cmp eax, 23<br><br>jne label|If value if eax is not equal to 23, then jump to label|
|jc(jump carry)<br><br>jb(jump below)<br><br>jnae(jump if not above or equal)|jump if carry flag is set from the previous command. This means that the previous operation, first argument smaller than second.<br><br>Unsigned arithmetic operation|add eax,ebx<br><br>jc label|Pretend eax is 8 bits and after adding ebx, it overflows to a 9bit value. Jump to label if eax value larger to hold within its bitsize|
|||cmp eax,ebx<br><br>jc label|if eax and ebx are unsigned integers and eax is smaller than ebx, jump to label|
|jnc(jump no carry)<br><br>ja(jump above)<br><br>jnbe(jump not below or equal)|Jump if no carry flag is set from previous command. Means that first argument larger than second.<br><br>Unsigned arithmetic operation|add eax,11<br><br>jnc label|Assuming eax has more bitsize than 2, this wont cause an overflow.|
|||cmp eax,ebx<br><br>jnc label|Say that eax = 10 and ebx = 5. Eax would be bigger than ebx, thus jump to label.|
|jo(jump overflow)|Jump if overflow flag is set. Signed arithmetic operation|mov eax, 111111111<br><br>jo label|Pretend eax is 8bits. Moving a 9bit value in eax would be too big so overflow flag is set.|
|jno(jump not overflow)|Jump if overflow flag is not set.|mov eax, 89239<br><br>jo label|If eax remains in its own bitsize, then we jump to label|
|jg(jump greater)<br><br>jnle(jump not less or equal)|Check between 2 values if the first is greater than the second, then jump. Checks zero flag and sign flag. Signed operation|cmp eax,ebx<br><br>jg label|Since cmp just subtracts ebx from eax, if eax >0 then eax is greater than ebx. Then we signal the jump. So first check zero flag to ensure its not same, then check sign flag to see it is not negative.|
|jl(jump less)<br><br>jnge(jump not greater or equal)|Check between 2 values if the first is smaller than the second, then jump. Checks zero flag and sign flag. Signed operation|cmp eax,ebx<br><br>jl label|eax-ebx < 0, then jump to label|
|js(jump sign)|Jump only if sign flag is 1. This means last operation resulted in a negative value|mov eax,-1<br><br>js label|eax = -1. eax is negative, so jump to next label|
|**Call operations. Jump operations that save return values. Uses stack push and pop**||||
|call|Saves current eip/rip to the stack. Then go jump to a given label|call label|Call is doing the following:<br><br>push eip<br><br>jmp label|
|ret(return)|Load the previous memory address saved in stack into the eip/rip|ret|Simply returning to next line after call.<br><br>pop eip|
|**Shift operations. Shifting binary left or right to multiply by 2 or divide by 2**||||
|shr(shift right)|Move binary of register x times to the right. Divides by 2 for every x.|shr eax,1|If eax was 00001111<br><br>Then eax would now be 00000111|
|shl(shift left)|Moves binary register x times to left. Multiplies by 2 for every x|shl eax,2|eax is 00011000<br><br>Then eax is 01100000|
|||shl eax,2|eax is 0111000<br><br>If we move left 2 times then it would be 9bit value<br><br>111000000<br><br>So, we move the extra bit into edx and flick on the carry flag. Eax stores only 8 bits of 11000000|
|sar(shift arithmetic right)|Keeps sign bit during a shift to right. This means the leftmost digit stays the same|mov eax,0b11110000<br><br>sar eax,2|eax = 11110000<br><br>Keep note of leftmost value. It is one.<br><br>Carry out the shift as if it was normal.<br><br>eax = 00111100<br><br>Now this is finished. Bring back the leftmost value of one.<br><br>eax = 10111100|
|sal(shift arithmetic left)|Keeps sign bit during shift to left.|mov eax,0b10110000<br><br>sal eax,3|eax = 10110000<br><br>Keep note of leftmost value<br><br>Shift left as if normal 3 times<br><br>110000000<br><br>It is now 9 bits.<br><br>Move extra into edx and flick on the carry flag. Eax stores 8 bits of 10000000<br><br>Now bring the leftmost value back, oh wait it already is there.<br><br>eax = 10000000<br><br>edx = 00000001|
|ror(rotate right)|Rotates all bits right. Around the world. Rightmost becomes leftmost|mov eax, 0b11000001<br><br>ror eax,1|eax = 11000001<br><br>Rotating right will shift every value right one and loop back if needed.<br><br>eax = 11100000|
|rol(rotate left)|Rotates all bits left. Leftmost becomes rightmost|mov eax, 0b11100100<br><br>rol eax,1|eax = 11100100<br><br>Rotate left and shift all values left. Loop back if needed<br><br>eax = 11001001|
|**System call. Give control to kernel to perform kernel actions**||||
|int|Invoke the kernel. Kernel reads the registers for what to do.|mov eax,1<br><br>mov ebx,0<br><br>int 0x80|Int 80h: system call<br><br>The 1 in eax tells system call that this will be a system exit call<br><br>The 0 in ebx is the return code. We return 0, exit without a hitch|

### Dereferencing

[] square brackets are a tool here. [] square brackets will get you that data. [address] is dereferencing and will give you your oh so delectable data.


### Hex to Binary

0x declares hex in this case.
0b declares binary in this case


In binary 0b1 is the same as 0x1
0b11 is same as 0x3 in hex
0b111 same as 0x7 in hex
0b1111 is the same as 0xF in hex

So we can simplify every 4 binary as 0xF.

All binary can be converted to hexadecimal. There's no special method. 0xF can be used to represent 0b1111.  
  

0xFF is 0b11111111 an 8bit value

0xFFF is 0b111111111111 a 12bitvalue

0xFFFF is 0b1111111111111111 a 16bitvalue

  

### Bitmasks

This is a method to mask out certain bits. For example, with the binary:

10101010

Say we only want the 3rd and 4th bits like this:

00110000

We must use AND operand to compare bitwise each bit. It would look like:

00100000

  

Say we have a 32bit register as follows:

eax = 1010101011001100001001010000111

Remember, AX,BX,CX,DX are not accessible, and maybe we want upper 16 bits. We would do a bitmask with same bitsize.

1010101011001100001001010000111 masks with

11111111111111110000000000000000 or 0xFFFF0000

Thus leading to result being

1010101011001110000000000000000

  

There is a simpler method to what we wanted above, and that is just to SHR 16 bits.

  

### Interrupt

An interrupt is raising a flag for the kernel to come help perform a task that is only doable in kernel mode. Every mouse click is an interrupt, every keyboard click is an interrupt.

Interrupts are called through operation INT 80h. They will look at registers, eax, ebx, ecx and edx for the arguments on what exactly the kernel is supposed to do.

eax is the certain order you want to do.

ebx is the return value or file descriptor/destination

ecx is char value

edx is size of char

  

[https://www.tutorialspoint.com/assembly_programming/assembly_system_calls.htm](https://www.tutorialspoint.com/assembly_programming/assembly_system_calls.htm)

There is a list of interrupt codes that can happen as a result of eax values.

  

Remember, 80h is the interrupt we are allowed to use for system calls. You will rarely see another interrupt vector other than 80h.

Interrupts modify register value after interrupt as well. So look at them when its finished.

### Data Type declaration

All of the following data types will be declared in the section .data portion. Note that ARM uses .section, Intel uses just section

all datatypes will follow this order: variablename db value

variablename will hold the memory address for the value

db is allocating the memory space. Dynamically for strings and integers its very smart

Value is whatever value you give it.
    
|**Datatype**|**Value format**|**example**|**Explanation**|**How to push to stack**|
|-|-|-|-|-|
|string|“value”<br><br>  <br><br>And you must also declare length variable aswell|mymessage db “Hello World!”<br><br>lenmymessage equ $ - mymessage|db declare byte will declare bytes for every character in the following string.<br><br>  <br><br>mymessage is the memory address for the ‘H’ in “Hello World!”. To find the length in bytes of the entire string, we do lenmymessage equ $ - mymessage which means:<br><br>length = current address - mymessage address<br><br>  <br><br>Example: if ‘H’ is stored at 0xFF00, and the final ‘!’ is stored at 0xFF0B. Then subtract it like 0xFF0B - 0xFF00 = B|push variablename|
|||hiworld db “Hello World!”, 0xA<br><br>len equ $ - hiworld|0xA represents the new line \n in NASM.||
|Int|value|age db 16|age memory space holds the decimal value 16|push [variablename]|

  

### Boilerplate

section .data

  

section .bss

  

global _start

section .text

_start:

  

### Hello world

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbq_tmp_73acd100204d49ad.png)

- We define a string and its length in the section .data segment.
    
- System write interrupt using all 4 registers.
    
- eax is sys_write code
    
- ebx,1 is standard out.
    
- Move address of string into ecx
    
- length of string into edx
    
- Interrupt 0x80 to system write
    
- System exit interrupt aswell
    

Lets compile by viewing here: [learning bog](https://docs.google.com/document/d/12VdtjQmzW7wk5B20ylAiP1rmu6cZLNOZ8atY0DSdbaU/edit#heading=h.ny30thmcpjt0)

Then run by doing gdb -q helloworld. Then type r

  

### Num to ascii string

If we want to be able to print out a number, we must turn it into the ascii version of itself first. To do this, you must add ‘0’ to the register. Example is:

add edi, ‘0’

To return the string back to a number, just subtract ‘0’.

sub edi, ‘0’

  

### Loop logic

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbq_tmp_41cd0db8118ac687.png)

Comments kind of explain but I will a second time

- Goal of the program is to do a for loop between 0-5. Print each index each iteration
    
- ln 9. Clear out the edi register first. This will be our iterator
    
- ln 13. Turn edi register into ascii so we can print it
    
- ln 15-19. Print the edi register
    
- ln 22. Return edi register to integer so we can increment it
    
- ln 24. Increment the edi register
    
- ln 27-28. If edi is less than 5, then keep continuing the loop
    

  

### C programming practices

For pushing and popping to stack:

- They like to push and pop in reverse order. This means that in functions like printf(“%d %d %d”) the last %d will be pushed first and first will be pushed last
    
- For branching off into functions, it will push all registers eax,ebx,ecx,edx. Then when function is over, pop them back in
    
- ![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivbq_tmp_4b70913626662952.png) This is done to simply reset the stack to the current esp. We dont want to worry about the memory addresses that we dont use. Looks like the stack is empty
    
- Oftentimes when asking for user input, we move inwards into the stack like esp+28