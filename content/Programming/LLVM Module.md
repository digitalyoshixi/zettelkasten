---
tags:
  - llvm
---
Contains all the information associated with a program file.
If you want multi-file programs, the [[Linker]] parses the modules to optimize.
![[LLVM Module-20250101032322910.webp]]
# Creating Module
```cpp
static std::unique_ptr<Module> TheModule = std::make_unique<Module>("my cool jit", *TheContext);
```