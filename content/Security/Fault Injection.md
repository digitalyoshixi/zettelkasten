---
tags:
  - security
  - hardware
aliases:
  - FPGA Fault Injection
  - Hardware Glitching
  - Glitch
  - Glitching
---
These are attacks on hardware systems that involve pushing chips past their physical limitations, just enough to change the behavior of the chip without breaking it.

Fault injection is a very [[Black Box Testing|Black Box]], we dont exactly know what we are changing, so we rely on [[Brute Force]].

These are also attacks that quite frequently require modifications of the original hardware, or require connection of a external circuit to carry through with an attack.
# Uses
- [[Fault Injection Clock Signal Glitching]]
- [[Firmware Reverse Engineering]]
- [[RCE]]
- [[One Time Programmable Memory|OTP]] Overwritting
- [[Secure Boot]] bypass
- [[Code Readout Protection]] bypass
- [[Encrypted Flash]] bypass
- Setting up [[Joint Test Action Group|JTAG]]/[[Serial Wire Debug|SWD]] support
# Glitching Device Implementations
- [[Electromagnetic Frequency Injection]]
- [[The Crowbar]]
- [[ChipWhisperer Husky]]
# [[Circuit Characterization]] Techniques
These are techniques to help us determine the [[Circuit Trace]] of a circuit.
- [[Circuit Characterization from Waveform View]]
- [[Circuit Characterization from Current Usage]]
# Triggering Techniques
These are techniques to help us find [[Trigger|Triggers]] for when to glitch the circuit.
- Trigger right after [[Universal Asynchronous Receiver Transmitter|UART]], [[Serial Peripheral Interface|SPI]], [[Universal Serial Bus|USB]] initialization 
# Resources
- https://www.hextree.io
- The Art of Fault Injection ($4000+)