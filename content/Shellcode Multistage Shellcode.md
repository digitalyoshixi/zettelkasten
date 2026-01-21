---
tags:
  - security
  - binary_exploitation
---
A method to bypass complex constraints on your shellcode.
You write shellcode that can read future shellcode.
# Process
1. Stage 1: `read(0, rip, 1000)`
	1. Get rip with `lea rax, [rip]`
2. Stage 2: whatever you want
