---
tags:
  - ctf
---
1. If you disassemble this program, you will see this as the main function:
# Control Flow
1. ![[SwampCTF2025 You Shall Not Passsss-20250329220906539.webp]]
### sub_10c0
1. Allocates 3 pointers and 1 variable
   ![[SwampCTF2025 You Shall Not Passsss-20250329221123570.webp]]
	1. ![[SwampCTF2025 You Shall Not Passsss-20250329221142883.webp]]
	2. ![[SwampCTF2025 You Shall Not Passsss-20250329221211010.webp]]
2. does a while loop until i is not the address of data_405, which might just be 0. So continue changing i until it is a non-zero address.
   ![[SwampCTF2025 You Shall Not Passsss-20250329221322794.webp]]
	1. ![[SwampCTF2025 You Shall Not Passsss-20250329221300230.webp]]
3. A lot more assignments to variables 
   ![[SwampCTF2025 You Shall Not Passsss-20250329221516101.webp|180]] ![[SwampCTF2025 You Shall Not Passsss-20250329221546877.webp|156]]![[SwampCTF2025 You Shall Not Passsss-20250329221555936.webp|205]]
	1. They assign 8 variables to each character from 4060->4068
	2. For variables data_4030, they apply a hashing function like:
```
int32_t rax_11 = (rax * 0x14a + 0x64) s% 0x8ff
data_4030 = data_4030 ^ r13 ^ rax_11.b
```
3. We see that this sort-of-thing is applied ~20 times, which means this may be suitable to the flag encoding process
4. ![[SwampCTF2025 You Shall Not Passsss-20250329222417730.webp]]
	1. Set some variable to some value in memory
	2. ![[SwampCTF2025 You Shall Not Passsss-20250329222249174.webp]]
	3. A new variable i_1 is assigned, then this while loop will continue to change i_1 until its not equal to the address of data_423c
	4. ![[SwampCTF2025 You Shall Not Passsss-20250329222335706.webp]]
	5. Set that original memory value to the new value changed in the funtion
### sub_17e0
1. [[mmap()]] a page-size of the programs memory, and return an error if it could not be memory mapped.
   ![[SwampCTF2025 You Shall Not Passsss-20250329223306922.webp]]
2. ![[SwampCTF2025 You Shall Not Passsss-20250329223403206.webp]]
   Construct a list of ?, and the first element of that list is called as a function, this means data_4180 is a function
# Debugging
- Enter [[libc_start_main]]
- Continue until we enter main which is here:
  ![[SwampCTF2025 You Shall Not Passsss-20250330005156235.webp]]
- Step into that call, then keep moving until we call rax. Our entry is at `0x5555555550c0`. This is what it looks like:
  ![[SwampCTF2025 You Shall Not Passsss-20250330005619495.webp]]
- 
# Thoughts
1. Is this program a flag checker?
2. When you run the first function, these are just constant hard-coded values that dont interact with the input right?
3. The user input function is likely within the rax.