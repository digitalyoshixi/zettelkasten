---
tags:
  - security
  - reverse_engineering
  - ctf
---
1. run [[Fireeye Labs Obfuscated String Solver|FLOSS]] on the binary, and we find that it is packed with UPX packer
   ![[MagpieCTF2025 Black Market Binary-20250223172420523.webp]]
2. ![[MagpieCTF2025 Black Market Binary-20250223172507723.webp]]
3. ![[MagpieCTF2025 Black Market Binary-20250223173514788.webp]]
4. Obviously, there is a encryption algorithm within this code, and in fact, it is scrambling this flag
   ![[MagpieCTF2025 Black Market Binary-20250223173540581.webp]]
5. There is this decrypt files program that seems to output the same things
   ![[MagpieCTF2025 Black Market Binary-20250223173706227.webp]]
   ![[MagpieCTF2025 Black Market Binary-20250223173726372.webp]]
   Looks pretty useless to me.
6. Lets use GDB.
	1. Set a breakpoint anywhere after the gameloop is ran. I set mine here:
	   ![[MagpieCTF2025 Black Market Binary-20250223180437535.webp]]
	2. Set another breakpoint at scrambledata function
	   ![[MagpieCTF2025 Black Market Binary-20250223180624770.webp]]
	3. lets jump to the scrambledata function.
   ![[MagpieCTF2025 Black Market Binary-20250223174836785.webp]]
   1. Takes the strlen of `magpieCTF{s4mpl3_fl4g}` which is 22 or `0x16`
      ![[MagpieCTF2025 Black Market Binary-20250223180805790.webp]]
   2. Afterwards, enter a loop that goes 22 times, after that loop with all the operations, you land here:
      ![[MagpieCTF2025 Black Market Binary-20250223181245833.webp]]