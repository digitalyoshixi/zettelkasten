---
tags:
  - ctf
  - reverse_engineering
---
1. We find that there are a TON of function calls in the disassembly. We dont care about the first few, just set a breakpoint right after the user input
   ![[CTF@CIT Secure Keygen-20250427152820230.webp]]
2. Now, we find that 0x47deb0 will actually act as [[scanf()]], so this stores the user input
	1. We can also assume that 0x467a60 is [[printf()]]
3. Note that this stuff at the bottom will be the [[Stack Canary]] check
   ![[CTF@CIT Secure Keygen-20250427152944724.webp]]
4. So, this leaves us with all the key checking logic in these four functions
   ![[CTF@CIT Secure Keygen-20250427153007555.webp]]
### sub_47d9b0
1. ![[CTF@CIT Secure Keygen-20250427153057708.webp]]
2. There is a user input length check to see if the string length of our key is greater than 16 (you can check rdx in the debugger)
3. True case:
	1. Then, it checks if the string length is smaller than maxint. if it is higher, then segfault
	   ![[CTF@CIT Secure Keygen-20250427153633113.webp]]
	2. Then, it checks if string length is bigger than 0, if it is not, then dont do anyting
	   ![[CTF@CIT Secure Keygen-20250427153836310.webp]]
	3. True:
		1. 