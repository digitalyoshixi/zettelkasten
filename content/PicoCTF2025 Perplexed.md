---
tags:
  - ctf
---
# Recon
![[PicoCTF2025 Perplexed-20250309145859456.webp]]
This is the correct output of the binary that we want to each
![[PicoCTF2025 Perplexed-20250309150054452.webp]]
Looks like it has a check for the string length of the input first
![[PicoCTF2025 Perplexed-20250309150159071.webp]]
There is this function called check
![[PicoCTF2025 Perplexed-20250309170526844.webp]]
So it runs the check function after user input, and depending on its result it puts success or fail
![[PicoCTF2025 Perplexed-20250309170622519.webp]]
# Decompilation
![[PicoCTF2025 Perplexed-20250309170804306.webp]]
### Check()
![[PicoCTF2025 Perplexed-20250309171501960.webp]]
First, the flag must have a length of 26 characters