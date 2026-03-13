---
tags:
  - forensics
---
Any [[Mass Storage Device|Drives]] that do not retain old copies of data.
# Sterilization
Sterilzation must be done by overwriting all bytes on the device with `0x00`
Compare the hash afterwards with a 64-bit [[Checksum]] to see if you wiped everything.
### Tools:
- [[Paladin]]