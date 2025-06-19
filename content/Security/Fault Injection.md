---
tags:
  - security
  - hardware
aliases:
  - FPGA Fault Injection
---
These are attacks on hardware systems that involve pushing chips past their physical limitations, just enough to change the behavior of the chip without breaking it.
Fault injection is a very [[Black Box Testing|Black Box]], we dont exactly know what we are changing, so we rely on [[Brute Force]].
# Uses
- Firmware Recovery
- [[One Time Programmable Memory|OTP]] Overwritting
- [[Remote Code Execution|RCE]]
- Hardware Spoofing
- [[Secure Boot]] bypass
- [[Code Readout Protection]] bypass
- [[Encrypted Flash]] bypass
- Setting up [[Joint Test Action Group|JTAG]]/[[Serial Wire Debug|SWD]] support