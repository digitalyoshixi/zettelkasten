---
tags:
  - debugging
---
If you have a stripped binary with no debug symbols and you want to get to main, you can do this:
# Trying Common Names
- `_start`
- `_libc_start_main`
- `main`
# Locating From `starti`
1. `info files` and copy the entry point
   ![[GDB Finding main()-20250104060021939.webp|856]]
2. `x/20i <entryaddress>`
   ![[GDB Finding main()-20250104060244612.webp]]
3. The lea before the call has a comment that holds the actual main address.
   ![[GDB Finding main()-20250104060328803.webp]]