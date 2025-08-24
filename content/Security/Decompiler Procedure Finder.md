---
tags:
  - reverse_engineering
aliases:
  - Decompiler Find Functions
---
The process that decompilers use to find functions within a [[Structured Object File Format]] binary.
Not all functions will be found by the [[File Reader]], so we need a specific process to find all functions.
# Finding Called Functions by Code Walking
After running the [[File Reader]], we get access to the code entry point and hopefully a list of symbols via the symbol table.
We [[Code Walking|Code Walk]] from the code entry point, and every symbol entry point, saving all found functions into a call list.
```
callList = entry_address
while callList not empty
   address = pop from callList
   functionList += new function starting at address
   while true
       if instr at address is jump
           workList += jump destination
       if instr at address is call
           callList += call destination
       if instr at address is ret
           if workList empty
               break
       if instr is not conditional
           address = pop from workList
           continue
       address += instr length
   end while
end while
```
# Finding Function Pointers
We might miss function pointers in the initial step as we are analyzing statically.
We can find function pointers through:
- Function addresses stored in memory
- [[Virtual Functions]] accessed through [[Virtual Function Table|vtable]]
- Extracting functions called by [[Trampoline Code]]
- Function pointers called by a register with a value we know
- Using a library signature engine to identify series of bytes associated with a specific librarys function call
- Checking sequences of bytes typically used by compilers to setup stack frame i.e:
```c
push ebp
move ebp, esp
sub esp, #
```
- Assume the first instruction after a `RET` is the entry of a new function (this is risky)