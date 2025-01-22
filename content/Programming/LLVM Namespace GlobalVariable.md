---
tags:
  - llvm
  - cpp
---
A custom class for global variables
```
GlobalVariable *globalVar = new GlobalVariable(module, globalVarType, /*isConstant*/ false,
              GlobalValue::ExternalLinkage, initValue, globalVarName)
```
