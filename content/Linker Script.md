---
tags:
  - programming
---
A script defining how the final program should be [[Linker|Linked]] by the linker.
# GCC Link Flag
```
gcc -T linker.ld -o myos boot.o kernel.o
```
# Example
```c
ENTRY(_start)

SECTIONS
{
  . = 2M; /* 2MB offset */
  .text BLOCK(4K) : ALIGN(4K)
  {
    *(.multiboot)
    *(.text)
  }

  .rodata BLOCK(4K) : ALIGN(4K)
  {
    *(.rodata)
  }

  .data BLOCK(4K) : ALIGN(4K)
  {
    *(.data)
  }

  .bss BLOCK(4K) : ALIGN(4K)
  {
    *(COMMON)
    *(.bss)
  }

}
```