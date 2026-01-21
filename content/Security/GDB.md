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
### Movement
- **break(b)**: set breakpoint at current line
	- **break N**: set breakpoint at line N
	- **break \*(main+offset)**: Break at memory location
	- **break fn**: set breakpoint at function(requires [[Debugging Symbol Tables]])
- **run(r) arg1 arg2**: run til next breakpoint or error
- **continue(c)**: continue from break
- **finish(f)**: run til current function is finished
- **step(s)**: run next line of program(step)
	- **step N**: run next N lines
- **stepi**: step foillowing machine instructions
- **starti** : start at the first entry point of the binary
- **jump**: jump to specific line number or address
### Info
- **del** : delete all breakpoints
	- **del N**: delete breakpoint Ns
- **info**
	- **registers**: getst info of registers
	- **break**: gets all breakpoints
	- **frame**: info about current frame
	- **locals**: info about all variables in current function
### printing
- **p** : print some value
	- **p var**: print variable value. may need [[GDB Typecasting]]
	- **p addr**: print value at address
- **bt**: print stack trace
- **watch condition**: set a watch point like watch x=3. to check for changes in variable x
- **x** : examine memory
	- **x/10i addr** : print the 10 instructions at an address
	- **x/8x $rbp - 0x0** : print the 8-bytes at the stack base pointer
	- **x/1xb addr** : print the 1 byte at that address
- **whatis [variablename]** : Prints the datatype of the varaible
### Modifying
- **set** : set a register like `set $eax=0`
### Meta
**quit**: exit GDB
**lay next**: show beautiful layout
**lay src**: show source code
**list**: show current line executed in source code
**ref**: refresh view
# Debugging Symbols

# Guides
- [[GDB Finding main()]]
- [[GDB Dumping Memory Addr]]
- [[GDB Changing Register Values]]
- [[GDB Changing Memory Values]]
- [[GDB Jumping To Address]]
- [[GDB Disable ASLR]]
# Other
- [[GDB Typecasting]]
- [[GDB starti]]
- [[Pwndbg]]
- [[GEF]]
- [[PEDA]]
- [[pwngdb]]
- [[GDB View Return Address]]