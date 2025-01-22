---
tags:
  - reverse_engineering
---
Immutable objects that represent the state of a program at a given time.
this includes:
- Memory
- Registers
- OS information
- Symbolic solver state
- Entry of program
- etc
![[angr SimState Objects-20240629174557877.webp]]
https://docs.angr.io/en/latest/_modules/angr/sim_state.html

You can pass this initial state to the [[angr Simulation Manager]] and explore until the desired branch is reached, or all branches are terminated.

**Most of the problems with our angr scripts occur when the initial state is not properly set.**
# State Generators
https://docs.angr.io/en/latest/core-concepts/states.html
### Entry_State
Entry state is the most generic constructor of the possible program states at an the program's entry point. constructs a state ready to execute at the main binary’s entry point
```python
state = p.factory.entry_state()
```
### Blank_State
constructs a “blank slate” blank state, with most of its data left uninitialized. When accessing uninitialized data, an unconstrained symbolic value will be returned
```python
state = p.factory.blank_state()
```
### Full_init_State
constructs a state that is ready to execute through any initializers that need to be run before the main binary’s entry point, for example, shared library constructors or preinitializers. When it is finished with these it will jump to the entry point
```python
state = p.factory.full_init_state()
```
### Call_State
```python
state = p.factory.call_state()
```
# State Options
#### UNICORN 
Implements [[Symbolic Execution|Dynamic Symbolic Execution]]. 
Better than [[VEX IR]] when it comes to emulating instructions
##### ZERO_FILL_UNCONSTRAINED_MEMORY/REGISTERS
If a path in unconstrained, then zero fill it and move on
##### LAZY_SOLVES
If there is a state with many possible inputs, then dump that path and move on
##### BYPASS_UNSUPPORTED_SYSCALL
Wont fail if there is an unrecognized [[Syscall]]
##### DOWNSIZE_Z3
Reduces [[Random Access Memory|RAM]] usage of the [[z3]] solver
##### USE_SYSTEM_TIMES
Good when analyzing binaries which utilize system time.
# Attributes
### state.regs
Returns the project's [[angr Registers]] 
### state.mem
Returns the project's [[angr Memory Space]]
