---
tags:
  - llvm
---
Object to tie the whole code generation together.
- Allows access to core LLVM data structures
- Allows access to LLVM modules
- Allows access to [[LLVM Namespace IRBuilder]]
# Making A Context called "Module"
```cpp
context = make_unique<LLVMContext>();
builder = std::unique_ptr<IRBuilder<>>(new IRBuilder<>(*context));
module = make_unique<Module>("Module", *context);
```