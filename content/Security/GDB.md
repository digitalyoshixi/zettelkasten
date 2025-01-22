---
tags:
  - GDB
  - assembly
  - debugging
---
Gnu Debugger
# Running
`gdb --args programname arg1 arg2 arg3`
# Commands
https://users.ece.utexas.edu/~adnan/gdb-refcard.pdf
**continue(c)**: continue from break
**break(b)**: set breakpoint at current line
**break N**: set breakpoint at line N
**break \*(main+offset)**: Break at memory location
**break fn**: set breakpoint at function(requires [[Debugging Symbol Tables]])
**delete N**: delete breakpoint Ns
**info**
- **registers**: gets info of registers
- **break**: gets all breakpoints
- **frame**: info about current frame
**run(r) arg1 arg2**: run til next breakpoint or error
**f**: run til current function is finished
**step(s)**: run next line of program(step)
**step N**: run next N lines
**stepi**: step foillowing machine instructions
**finish**: get out of current function
**jump**: jump to specific line number or address
**p var**: print variable value. may need [[GDB Typecasting]]
**p addr**: print value at address
**bt**: print stack trace
**up**: go up stack frame
**down**: go down stack frame
**watch condition**: set a watch point like watch x=3. to check for changes in variable x
**quit**: exit GDB
**lay next**: show beautiful layout
**lay src**: show source code
**list**: show current line executed in source code
**ref**: refresh view
**set** : set a register like `set $eax=0`
# Debugging Symbols

# Other
- [[GDB Typecasting]]
- [[GDB Finding main()]]
- [[Pwndbg]]
- [[GEF]]
- [[GDB Dumping Memory Addr]]