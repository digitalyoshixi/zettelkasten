---
tags:
  - programming
  - reverse_engineering
---
A [[Disassembler]] for python bytecode.
# Usage
```python
import dis
code_obj = marshal.loads(bytecode)
dis.dis(code_obj)
```