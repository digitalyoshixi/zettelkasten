---
tags:
  - ctf
  - reverse_engineering
---
# Challenge
![[ImaginaryCTF 2024 Rust-20240722004653302.webp]]
https://cybersharing.net/s/4a47f2774279abd1
### Initial Recon
![[ImaginaryCTF 2024 Rust-20240722005000629.webp]]
The output file contains an encrypted list of 21 elements.
![[ImaginaryCTF 2024 Rust-20240722005635260.webp]]
If we try to run the file normally, we see that the size of the list is equivalent to the number of characters you input.
We can assume that the flag will be 21 characters long then
# Solution
https://vaktibabat.github.io/posts/ictf_2024/
[[Decompile]] with [[Ghidra]].
### main()
1. Takes input through stdin
2. Sends input to encrypt()
### encrypt() function
1. create an `encrypted` vector
2. iterate over all bytes of user's input message
	1. next element in the iterator is put into `0Var1`
	2. ![[ImaginaryCTF 2024 Rust-20240722020144048.webp]]
   this section of the code likely handles the encryption, as it pushes to the `encrypted` vector at the end
3. `encrypted` vector is printed out
### Using GDB to investigate
For the encryption portion:
Input:
- message is `ABCDE`
- key is `0x1234`
1. some local variables are moved into `rcx` and `rax` 
   ![[ImaginaryCTF 2024 Rust-20240722020324303.webp]]
2. stepping 2 instructions shows the values of rax and rcx
   ![[ImaginaryCTF 2024 Rust-20240722020430200.webp]]
   rcx contains byte of message (`A` in this case)
   rax contains `0`
3. 5th instructions shift `rcx` to the left 5 times 
   ![[ImaginaryCTF 2024 Rust-20240722020659442.webp]]
4. later instructions involve another shift
   ![[ImaginaryCTF 2024 Rust-20240722022240148.webp]]
5. 
   ![[ImaginaryCTF 2024 Rust-20240722022549201.webp]] 
   inspecting this:
   - rax is 0
   - rdi is the (current byte << 2
   - rsi is a pointer to a newline
6. 
   ![[ImaginaryCTF 2024 Rust-20240722022810720.webp]]
   ![[ImaginaryCTF 2024 Rust-20240722022920571.webp]]
   so far what was done was:
   b = a ^ key
7. ![[ImaginaryCTF 2024 Rust-20240722023014286.webp]]
   b = a ^ key + 0x539
8. ![[ImaginaryCTF 2024 Rust-20240722023134868.webp]]
   b = -(a ^ key + 0x539)
so the algorithm is:
![[ImaginaryCTF 2024 Rust-20240722023159848.webp]]
The script to solve this is:
```python
for y in output_of_flag:
	x = ~y
	x -= 0x539
	x ^= key
	x = x >> 2
	flag.append(x)
print("".join([chr(c) for c in flag]))
```
`ictf{ru57_r3v_7f4d3a}`
