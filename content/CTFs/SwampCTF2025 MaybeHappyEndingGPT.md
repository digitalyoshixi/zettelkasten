---
tags:
  - machine_learning
---
![[SwampCTF2025 MaybeHappyEndingGPT-20250331040127873.webp]]
http://chals.swampctf.com:50207/
https://ctf.swampctf.com/files/68f09c26e413cc219c7711c6e945d8fc/MaybeHappyEndingGPT.zip?token=eyJ1c2VyX2lkIjoxOTEsInRlYW1faWQiOjEwOCwiZmlsZV9pZCI6Mzd9.Z-oTmg.qLXXXrIORiDeBtnveM7ITCvmXr0
1. We find references of flag
   ![[SwampCTF2025 MaybeHappyEndingGPT-20250329024842303.webp]]
2. We see that there is a hint here, and that it is using eval()
   ![[SwampCTF2025 MaybeHappyEndingGPT-20250329025250183.webp]]
3. It is reading the LLM's response and then evaluating it and returning the eval's output as a response
4. ![[SwampCTF2025 MaybeHappyEndingGPT-20250329025206732.webp]]
5. ![[SwampCTF2025 MaybeHappyEndingGPT-20250329025218377.webp]]