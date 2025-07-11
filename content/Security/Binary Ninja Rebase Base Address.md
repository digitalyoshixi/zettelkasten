---
tags:
  - reverse_engineering
---
Used when you have a position dependent executable.
`Analysis > Rebase > New Address`
# Finding New Address with [[GDB]]
1. `r`
2. `CTRL+C`
3. `info proc mappings`
And, select the starting address corresponding to the first executable segment
![[Binary Ninja Rebase Base Address-20250509213006571.webp]]