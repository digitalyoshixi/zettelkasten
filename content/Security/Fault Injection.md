---
tags:
  - security
  - hardware
aliases:
  - FPGA Fault Injection
  - Hardware Glitching
  - Glitch
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
# [[Circuit Characterization]] Techniques
These are techniques to help us determine the [[Circuit Trace]] of a circuit.
- [[Circuit Characterization from Waveform View]]
- [[Circuit Characterization from Current Usage]]
# Triggering Techniques
These are techniques to help us find [[Trigger|Triggers]] for when to glitch the circuit.
- Trigger right after [[Universal Asynchronous Receiver Transmitter|UART]], [[Serial Peripheral Interface|SPI]], [[Universal Serial Bus|USB]] initialization 