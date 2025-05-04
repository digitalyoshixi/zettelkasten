---
tags:
  - ctf
  - cryptography
---
1. `keepass2john Passwords.kdb >> database.hash`
2. `john --wordlist=/usr/share/wordlists/rockyou.txt -format:keepass database.hash`
   ![[BirthdayCTF2025 Password Cracking 2-20250504183642841.webp]]
3. So, we get the flag as `zebralicious`