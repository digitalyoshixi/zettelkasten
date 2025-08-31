---
tags:
  - programming
  - assembly
  - x86
aliases:
  - x86 movsb
  - x86 movsw
  - x86 movsd
---
A [[x86 mov]] for a array of values.
- Uses [[rsi]] and [[rdi]] to iterate through two arrays
- Uses [[rcx]] as the counter
Can be used to implement [[memcpy]].
The [[Direction Flag]] indicates the direction that memory is stored.
# Overwrite Previous Memory
In crafting [[Shellcode]], you can change [[Direction Flag]] to overwrite previous memory.