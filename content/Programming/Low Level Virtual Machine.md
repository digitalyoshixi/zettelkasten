---
tags:
  - c
  - cpp
  - llvm
aliases:
  - LLVM
---
A toolchain and compiler used to create:
- Programming language frontends
- Instruction set backends
It is used in [[Clang]]
# Process
![[Low Level Virtual Machine-20250102214052503.webp]]
1. Create a [[Lexer]] to turn raw source-code text into [[LLVM Tokens]]
2. Define an [[Abstract Syntax Tree|AST]] to represent code structure and token relations using [[LLVM API]]
3. Create a [[Parser]] to loop over each token and fill out the [[Abstract Syntax Tree|AST]]
4. Import [[LLVM API]] primatives
5. Use the [[LLVM opt|opt]] tool to optimize and generate [[Intermediate Representation|IR]]
6. Write an [[LLVM Module]] that takes IR as input and returns executable object code
# Bibliography Pages
- [[LLVM Intermediate Representation]]
- [[LLVM Types]]
# Concepts
- [[Compiler]]
- [[Interpreter]]
- [[Lexer]]
- [[Parser]]
- [[Intermediate Representation]]
- [[LLVM Virtual Registers]]
- [[LLVM Global Variables]]
- [[LLVM Constant]]
- [[LLVM Functions]]
- [[LLVM Control Flow]]
- [[LLVM dot]]
- [[LLVM lli]]
- [[LLVM llc]]
- [[LLVM as]]
- [[LLVM dis]]
- [[LLVM Unreachable Codepath]]
- [[Static Single Assignment]]
- [[LLVM opt]]
- [[LLVM Block Domination]]
- [[LLVM Intrinsics]]
- [[LLVM Module]]
- [[LLVM API]]
- [[Kaleidoscope]]
- [[LLVM-config]]
- [[On Request Compilation|ORC]]
- [[JITLink]]
# Documentation
- https://llvm.org/docs/LangRef.html
# Guides
- https://mcyoung.xyz/2023/08/01/llvm-ir/
- https://llvm.org/docs/tutorial/
- https://mukulrathi.com/create-your-own-programming-language/llvm-ir-cpp-api-tutorial/