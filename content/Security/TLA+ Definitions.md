---
tags:
  - verification
---
The ability to bind a name to a TLA+ expression.
Conventional names in all programs are:
- `Init` : starting state
- `Next` : next state

```tla
Name == pc = "start" /\ i = 20
```