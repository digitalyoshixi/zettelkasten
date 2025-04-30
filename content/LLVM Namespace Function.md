---
tags:
  - llvm
  - cpp
---
A base class used for [[LLVM API|LLVM codegen]] for [[Abstract Syntax Tree|AST]] nodes relating to functions.
# Creating a Function codegen
Within some [[Abstract Syntax Tree|AST]] [[C++ Class]]
```cpp
class PrototypeAST {
  std::string Name;
  std::vector<std::string> Args;

public:
  PrototypeAST(const std::string &Name, std::vector<std::string> Args)
      : Name(Name), Args(std::move(Args)) {}

  const std::string &getName() const { return Name; }
  Function *codegen();
};

```