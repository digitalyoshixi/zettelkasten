---
tags:
  - security
  - programming
aliases:
  - LangSec
---
The study of how security degrades in a parsing context as the complexity of a language increases.
You must treat all input as a language and define a clear [[Backus-Naur Form|BNF]] spec for it to ensure security.
# Theorem
A sufficiently complex parser is indistinguishable from a compiler.
Therefore, once your data language has enough features, it becomes a accidental programming language ([[Weird Machine]])