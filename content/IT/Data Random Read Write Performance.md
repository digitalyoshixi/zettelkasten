---
tags:
  - memory
aliases:
  - Data IOPS
---
How many times per second a device can read or write to small chunks of data.
Measured in IOPS (Input Outputs per Second) or MBps.
# Hardware Level
- [[Hard Drive|HDD]] usually meet 105 IOPS
- [[M.2|NVMe SSD]] meet 100,000 IOPS
# OS Level
Operations with physical hardware are often the slowest part of a program.
We measure IOPS during:
- Finding a file
- Opening a file
- Reading a file
- Writing to a file
- Move the file pointer ([[seek()]])
- Close the file