---
tags:
  - programming
---
# Process
- Swap each bit with the subsequent one
- Swap each [[Binary|Pair]] with the subsequent one
- Swap each [[Binary|Nibble]] with the subsequent one
- Swap each [[Binary|Byte]] with the subsequent one
- Swap each [[Binary|Word]] with the subsequent one
- ...
# Code
```c
uint32_t reverse(uint32_t x, int bits)
{
    x = ((x & 0x55555555) << 1) | ((x & 0xAAAAAAAA) >> 1); // Swap _<>_
    x = ((x & 0x33333333) << 2) | ((x & 0xCCCCCCCC) >> 2); // Swap __<>__
    x = ((x & 0x0F0F0F0F) << 4) | ((x & 0xF0F0F0F0) >> 4); // Swap ____<>____
    x = ((x & 0x00FF00FF) << 8) | ((x & 0xFF00FF00) >> 8); // Swap ...
    x = ((x & 0x0000FFFF) << 16) | ((x & 0xFFFF0000) >> 16); // Swap ...
    return x >> (32 - bits);
}
```