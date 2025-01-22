---
tags:
  - llvm
---
Object used to incrementally build up our [[Intermediate Representation|IR]].
The equivalent of a file-pointer when reading/writing a file.

# Inserting Instructions at End of a block
```cpp
SetInsertPoint(BasicBlock *TheBB)
```
# Getting Current Basic Block
```cpp
GetInsertBlock()
```
# Creating Instructions
Using the `Create*()` methods of the IRBuilder object

Takes an optional `Twine` argument that gives the register a custom name like `iftmp`. which is the twine for this instruction: `%iftmp = phi i32 [ 1, %then ], [ %mult, %else]`

Refer to the https://llvm.org/doxygen/classllvm_1_1IRBuilderBase.html docs for help building instructions.
### CreateLoad
Creates a [[LLVM load]] instruction
### CreateSub
Creates a [[LLVM sub]] instruction
### CreateFSub
Creates a [[LLVM fsub]] instruction
### CreateAlloca
### CreateStore
# Getting Types
Using the `get*()` methods of the IRBuilder object
Example:
```cpp
Value *IRCodegenVisitor::codegen(const ExprIntegerIR &expr) {
  return ConstantInt::getSigned((Type::getInt32Ty(*context)),
                                      expr.val);
};
```

# Getting Function Types
Using the `FunctionType::get`
Requires parameters for:
- returntype
- paramater types
- whether the function is [[Variadic]]
```cpp
FunctionType::get(returnType, paramTypes, false /* doesn't have variadic args */);
```
# Creating Struct Types
```cpp
StructType *treeType = StructType::create(*context, StringRef("Tree"));
```

### Creating Multiple Structs
The best way to do this is to define all the structs initially like [[Preprocessor Directives]] and then define their bodies later.
```cpp
void IRCodegenVisitor::codegenClasses(
    const std::vector<std::unique_ptr<ClassIR>> &classes) {
  // create (opaque) struct types for each of the classes
  for (auto &currClass : classes) {
    StructType::create(*context, StringRef(currClass->className));
  }
  // fill in struct bodies
  for (auto &currClass : classes) {
    std::vector<Type *> bodyTypes;
    for (auto &field : currClass->fields) {
          // add field type
          bodyTypes.push_back(field->codegen(*this));
    }
    // get opaque class struct type from module symbol table
    StructType *classType =
        module->getTypeByName(StringRef(currClass->className));
    classType->setBody(ArrayRef<Type *>(bodyTypes));
  }
```
# Creating Globals
```cpp
module->getOrInsertGlobal(globalVarName, globalVarType);
...
GlobalVariable *globalVar = module->getNamedGlobal(globalVarName);
globalVar->setInitializer(initValue);
```
Or, use the [[LLVM Namespace GlobalVariable]]
# Creating [[LLVM getelementptr|LLVM GEP]]
```cpp
Value *ptr = builder->CreateGEP(baseType, basePtr, arrayofIndices);
```