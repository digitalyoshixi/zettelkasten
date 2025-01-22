---
tags:
  - llvm
---
```c
define void @do_not_call(){
	unreachable
}
```
This code block will never be reachable.
If you enter this function, there will be undefined behavior.
# Use Cases
- Void pointers
- Error handling
- Explicit block-offs for [[Dead Code Elimination]]