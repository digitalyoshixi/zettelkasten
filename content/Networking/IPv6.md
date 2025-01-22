---
tags:
  - networking
---
Newer IP addressing scheme that has addresses of 128-bit.
![[IPv6-20240717161256046.webp]]
It is comprised of 8 fields of 16-bit numbers commonly represented in [[Hexadecimal]].
# Writing Conventions
- Leading `0`'s within a field can be removed. `:0dc8:` -> `:dc8:`
- A field of `0000` can be omitted and and written just as `:`
- consecutive fields of `0000` can be written as `::`
  ![[IPv6-20240717161910725.webp]]
  however. You can only have one of these `::` in an address.
  Having 2 would mean this address `::1111::` is indecipherable as we would not know how big the zero chunks are
# Multiple IPv6
Each device comes with multiple IPv6 addresses.
- [[Link-Local Address]]
# Concepts
- [[IPv6 Prefixes]]
- [[Neighbor Discovery Protocol]]
