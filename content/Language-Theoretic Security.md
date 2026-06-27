---
banner: "[[Language-Theoretic Security-20260627181544297.webp]]"
tags:
  - security
  - programming
aliases:
  - LangSec
---
The study of how security degrades in a parsing context as the complexity of a language increases.
You must:
- Treat all input as a language and define a clear [[Backus-Naur Form|BNF]] spec for it
- Parse completely before processing
# Theorem
A sufficiently complex parser is indistinguishable from a compiler.
Therefore, once your data language has enough features, it becomes a accidental programming language ([[Weird Machine]])
# Ideas
- [[Web Tower of Babel]]
- [[The Parser Problem]]
- [[Shotgun Parser]]
# Related Vulnerabilities
- [[Code Red Worm]]