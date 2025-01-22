---
tags:
  - llvm
---
The base class that is extended to:
- [[LLVM Namespace Function]]
- [[LLVM Namespace BasicBlock]]
- Instruction
- Result of intermediate computation
Each of [[LLVM API|LLVM codegen]]'s methods returns a `Value *` object which represents the virtual register containing an expressions result.