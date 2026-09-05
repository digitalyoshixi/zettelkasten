---
tags:
  - verification
  - programming
---
A argumentless constructor.
Useful as a placeholder for data that is missing
```lean
inductive Unit : Type where
| unit : Unit
```