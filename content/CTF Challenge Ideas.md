---
tags:
  - security
---
# List
# Emulator RE
https://hxp.io/blog/119/hxp-38C3-CTF-yasashiimon/
# Runtime Trampolines
- A program with runtime trampolines for every line of code
# Request Smuggling
- [[HTTP Smuggling|HTTP Request Smuggling]]
# Confused State
A RE challenge where you abuse a state machine with a confused state.
## Curious machine
Description: Enigma machine challenge with multiple substitution ciphers and a given graph, similar to the one at cybersci?

Solution: decode the enigma machine by finding the ciphers required

## Premature MAC
A secret prefix mac lengthening attack

## Bootstraps
A custom [[Bootstring]] implementation, only encoding function provided, and flag is encoded
# Linux interpreter fun
https://www.youtube.com/watch?v=kUMCAzSOY-o&t=600s
# SillyVM:
Simple VM for a register based language with LOAD, STORE, GET operations. Code is written in that language’s bytecode.
Solution: Reverse the VM and then understand the bytecode provided

# Character flow graph
Control flow graph of a program steganography

# Uncompress:
Packer program that compresses a file and inserts a unpacker inside the first lines of the program (maybe arithmetic encoding).
Solution: Use debugger to get to the segment after program is unpacked, then 
