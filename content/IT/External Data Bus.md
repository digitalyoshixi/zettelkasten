---
tags:
  - hardware
aliases:
  - EDB
---
![[External Data Bus-20240516005926502.webp]]
Responsible for transmitting data from the [[Central Processing Unit|CPU]] to other devices on the motherboard.
# How it works
3 Buses: Data, Address and Control make up the EDB.
### Data Bus
Carries the actual data between CPU to peripheral devices.
Depending on the CPU, the databus can transmit 8 - 64 bits at one time.
### Address Bus
Carries address of the data which signifies which device it should go to. Not to be confused with [[Memory Chip Controller|MCC]] which sends RAM addresses to CPU
### Control Bus
Carries control signals which manage interaction between CPU and peripherals. It allows it to signal when data transfer start, when it ends, the timings, and other things to synchronize device operations.

