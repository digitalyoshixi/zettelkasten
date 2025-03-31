---
tags:
  - ctf
---
![[SwampCTF2025 You Shall Not Passsss-20250331040717935.webp]]
https://ctf.swampctf.com/files/10ed11c19ea792d32db42fe63d217274/chal?token=eyJ1c2VyX2lkIjoxOTEsInRlYW1faWQiOjEwOCwiZmlsZV9pZCI6OX0.Z-oU4Q.PAkwNhds6tYYtyuL1FBr838q7Fw
If you disassemble this program, you will see this as the main function:
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
- It iterates through a loop, and it runs in it for __ times.
- Afterwards, it gradually pushes the word `Incorrect\n` onto the memory locations
  ![[SwampCTF2025 You Shall Not Passsss-20250330011457504.webp]]
- Then, it writes `Correct!\n` to the memory space afterwards
  ![[SwampCTF2025 You Shall Not Passsss-20250330011641406.webp]]
- Afterwards, save some data to the heap
  ![[SwampCTF2025 You Shall Not Passsss-20250330011916092.webp]]
- Enter a loop that repeats 181 times,
- Write the data, then jump into the next call. 
  ![[SwampCTF2025 You Shall Not Passsss-20250330012943579.webp]]
- Then, it tries to mmap, and it will jump out if it fails.
- It will then move some string contents into registers
  ![[SwampCTF2025 You Shall Not Passsss-20250330014202147.webp]]
- Moves some more things around
- Moves in some constants, then calls rbp 
  ![[SwampCTF2025 You Shall Not Passsss-20250330014231668.webp]]
- Inside rbp: string constants and data is being loaded
  ![[SwampCTF2025 You Shall Not Passsss-20250330014715885.webp]]
- Enters a loop that runs 38 times
  ![[SwampCTF2025 You Shall Not Passsss-20250330015105601.webp]]
- It should have a conditional move that occurs when dil is equal to r8b
  ![[SwampCTF2025 You Shall Not Passsss-20250330015859314.webp]] This is the key.
- Initially, before the start of the loop, rbx is `Correct!\n`
![[SwampCTF2025 You Shall Not Passsss-20250330020317536.webp]]
- After the loop, if esi is 0, then the value at r14 (which is `Incorrect`) is moved into rbx, then it prints rbx.
  ![[SwampCTF2025 You Shall Not Passsss-20250330020118146.webp]]
	- ![[SwampCTF2025 You Shall Not Passsss-20250330022515271.webp]] esi is initially set to 1, so something tampers with this
	  ![[SwampCTF2025 You Shall Not Passsss-20250330022544552.webp]]
	- If this comparison is not equal, then we will have to cmov
	- so, this comparison must be equal all 36 times
- Setting the first character to `s` passes the first check, so we know that it is decoding now character by character
- Lets note all these comparisons down:
![[SwampCTF2025 You Shall Not Passsss-20250330023400988.webp]]
```
0xdd
0x9a 
0xde
0x4e
0x69
0xe1
0xe9
0x2c
0xd2
0x4e
0xec
0xe7
0x18
0x26
0x6a
0x56
0x79
0xd8
0xa3
0x55
0x72
0xbc
0x76
0xc4
0xc 
0xf
0x9b
0xbe
0xc6
0x81
0xe2
0x41
0x47
0xa0
0xf4
0x26
```
- I gpt-ed a script to help me calculate the next character, since I did not want to reverse engineer the encryption process
![[SwampCTF2025 You Shall Not Passsss-20250330034013700.webp]]
Kept on running the script until i got the flag
```python
def find_a(b_hex, c_hex):
  """
  Finds the value of 'a' given 'a XOR b = c'.

  Args:
    b_hex: The hexadecimal representation of 'b'.
    c_hex: The hexadecimal representation of 'c'.

  Returns:
    The hexadecimal representation of 'a'.
  """

  b_int = int(b_hex, 16)  # Convert b from hex to integer
  c_int = int(c_hex, 16)  # Convert c from hex to integer

  a_int = c_int ^ b_int  # Perform the XOR operation

  a_hex = hex(a_int)  # Convert a back to hexadecimal

  return a_hex

# Example usage with -82 and 0xdd
#b_decimal = -82
b_decimal = int(input('b_decimal: '))
b_hex = hex(b_decimal & 0xFF) #ensure 8 bit representation.
#c_hex = "0xdd"
c_hex = input("c_hex: ")

result_hex = int(find_a(b_hex, c_hex), 16)
print(f"a = {result_hex}, chr(a) = {chr(result_hex)}")
```
*insert that video i took here*
`swampCTF{531F_L0AD1NG_T0TALLY_RUL3Z}`
# Thoughts
1. Is this program a flag checker?
2. When you run the first function, these are just constant hard-coded values that dont interact with the input right?
3. The user input function is likely within the rax.