---
tags:
  - linux
  - security
aliases:
  - eBPF
---
A platform that can run programs in a priviledged context used to safely extend the linux kernel.
- Can query about peripherals with 
# Process
1. Compile into eBPF bytecode `clang -target bpf`
2. eBPF verifier checks for safety and performance
3. eBPF JIT compiler compiles
4. Runs in the [[eBPF Virtual Machine]]
