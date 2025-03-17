---
tags:
  - binary_exploitation
  - pwn
---
# Recon
1. ![[PicoCTF2025 Valley-20250314032131655.webp]]
2. The string buffer size is 200 characters
   ![[PicoCTF2025 Valley-20250314030204489.webp]]
3. Jacky told me there is a format string vulnerability which it does have
   ![[PicoCTF2025 Valley-20250314032141658.webp]]
4. ![[PicoCTF2025 Valley-20250314032219761.webp]], and lets see what the corresponding output is in the debugger? Couldnt find this...
5. Note that we want to change the return address to the return address that points to `print_flag()`
   ![[PicoCTF2025 Valley-20250314034138923.webp]]
6. The relative offset for print_flag() is:
   ![[PicoCTF2025 Valley-20250314034645351.webp]]
7. The main-function body is seen in the 6th item on the stack when we start running
   ![[PicoCTF2025 Valley-20250314040002887.webp]]
# What we need to do
1. Leak the base address for print_flag(), the offset for print_flag() is `0x1269`
2. Modify the return address with [[Format String Exploitation]] to be the address where print_flag() is located
3. Leak the [[Stack Canary]] and then
   
   