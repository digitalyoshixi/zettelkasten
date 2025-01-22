---
tags:
  - cpu
---
A core is a single CPU. A single core could only hit a max clock speed of 4GHz. Thus, manufacturers decided to include several cores in one chip.
Modern day CPUs may have 32cores(Threadripper)
# Difference from Multi threading
In multithreading, the OS and application must make specific accommodations to support multiple threads, whereas multi core processing can work with everything, but must be actively implemented to use its full potential.
# Dual Core Architecture
- 2 Execution units (2 individual pipeline groups)
- Shared cache
- Shared RAM
# Hybrid Core Architecture
- Chips come with High power and low power cores
- Can be high performance or high battery whenever it wants to
- Intel's Alder lake CPU has 8 performance cores sand 8 efficiency cores.
- Almost all ARM cpus have this functionality