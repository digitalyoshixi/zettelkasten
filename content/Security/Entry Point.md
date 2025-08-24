---
tags:
  - reverse_engineering
  - software
aliases:
  - OEP
  - EP
---
This is where the CPU begins execution of a program.
# Pseudocode to find Entry Point
Used by [[Decomp]]
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