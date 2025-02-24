---
tags:
  - ctf
---
1. The webpage is at: http://challenges.magpiectf.ca:13000/
2. Convert this from base64 and you get: `We need someone to fix /login, it's been broken for far too long.`
   ![[MagpieCTF2025 Cops like Ciphers and Cookies-20250223045331252.webp]]
3. Remember that the key is `consistency`
4. ![[MagpieCTF2025 Cops like Ciphers and Cookies-20250223045442634.webp]]
5. In base64, this is: `vignere`
6. Note that when you access this webpage, you get a cookie and value
   ![[MagpieCTF2025 Cops like Ciphers and Cookies-20250223045528082.webp]]
7. In cyberchef, we get:
   ![[MagpieCTF2025 Cops like Ciphers and Cookies-20250223045739832.webp]]
   ![[MagpieCTF2025 Cops like Ciphers and Cookies-20250223045753773.webp]]
8. Then, lets just change guest to admin, and we get:
   ![[MagpieCTF2025 Cops like Ciphers and Cookies-20250223045823069.webp]]
9. ![[MagpieCTF2025 Cops like Ciphers and Cookies-20250223045842738.webp]]