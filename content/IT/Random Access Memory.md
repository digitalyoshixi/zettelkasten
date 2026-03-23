---
tags:
  - hardware
  - memory
aliases:
  - RAM
  - Memory
---
![[Random Access Memory-20240516212846751.webp]]
Device responsible for holding data that the CPU requires. This data includes:
- Opened [[Process]] and sub-processes
- Data in processes (i.e images, js, videos in a webpage)
- Opened files with file data (can be unencrypted when in use)
- Opened [[Stream|File Handle]]
- Content in shared buffers (can have usernames, passwords, etc..)
# RAM
### RAM Chips
![[Random Access Memory-20240523005510612.webp|298]]
RAM is able to store binary data through capacitors and transistors.
Data is organized in [[Binary|Byte]] fashion and transferred to the [[Central Processing Unit|CPU]] byte by byte through the [[Memory Chip Controller|MCC]].
Address pins on the ram dictate how much bits can be sent to the [[Memory Chip Controller|MCC]] per clock cycle. In the above example, there are 10 address pins.
##### RAM Chip Types
- [[Static RAM|SRAM]]
- [[Dynamic RAM|DRAM]]
- [[Synchronized Dynamic RAM|SDRAM]]
- [[Double Data Rate|DDR SDRAM]]
### RAM Sticks
![[Random Access Memory-20240523012332526.webp|340]]
RAM sticks are small circuit boards which connect several RAM chips together as one to communicate with the [[Memory Chip Controller|MCC]].
It plugs into a [[Peripheral Component Interconnect Express]] slot.
RAM can be x32bit or x64bit 
##### Types
- [[Single Inline Memory Module|SIMM]]
- [[Dual Inline Memory Module|DIMM]]
- [[Small Outline Dual In-line Memory Module|SO-DIMM]]
# Installation
- [[Dual Inline Memory Module|DIMM Installation]]
- [[Small Outline Dual In-line Memory Module|SO-DIMM Installation]]
# Concepts
- [[Memory Profile|XMP]]
- [[Double Sided RAM]]
- [[CAS Latency]]
- [[Error Correction Code RAM|ECC RAM]]
- [[Buffered RAM]]
- [[Virtual Memory]]
- [[Double Data Rate]]
- [[Multi-Channel Architecture]]
- [[Windows RAM Requirements]]
- [[RAM Troubleshooting]]
- [[RAM Data Transfer Rate]]
- [[Virtual Memory Space]]
- [[Memory Segmentation]]
- [[Page File|Paging]]