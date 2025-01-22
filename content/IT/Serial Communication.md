---
tags:
  - hardware
---
![[Serial Communication-20240526014109647.webp]]
Serial interface transmits bit data one at a time through a single wire.
It is marginally slower then [[Parallel Communication]] in theory, but modern day serial communication is fast enough to ignore these downsides
Serial interface trumps [[Parallel Communication]] as all data comes in a contiguous chunk, unimpeded by [[Race Condition]] between wires where one wire may send before another, unintentionally corrupting data