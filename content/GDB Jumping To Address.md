---
tags:
  - debugging
---
# Jump By Setting `rip`
1. `set $rip = *0x5555555564aa`
2. `n`
# Jump with `jump`
`jump *0x5555555564aa`