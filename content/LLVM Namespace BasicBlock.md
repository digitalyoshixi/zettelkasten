---
tags:
  - programming
  - llvm
---
Implementing a [[LLVM Namespace BasicBlock]] within [[Low Level Virtual Machine|LLVM]]
```cpp
BasicBlock *BB = BasicBlock::Create(*TheContext, "block_name", TheFunction);
```