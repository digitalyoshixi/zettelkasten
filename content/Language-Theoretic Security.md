---
banner: "[[Language-Theoretic Security-20260627181544297.webp]]"
tags:
  - security
  - programming
aliases:
  - LangSec
---
The study of how security degrades in a parsing context as the complexity of a input language increases.
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
- [[No More Length Fields]]
- [[Message Sequence Chart]]
- [[Input Enabled State Machine]]
- [[Stateful Fuzzing]]
- [[Types for Special Strings]]
- [[Happy Flow]]
# Related Vulnerabilities
### [[Weird Machine]]
- [[Code Red Worm]]
### Broken State Machines
- [[CVE-2018-10933]]
- [[MIDPSSH]]
- [[edentifier2]]
### [[Injection Attack|Flawed Forwarding]]
- [[SQL Injection|SQLI]]
- [[LDAP Injection]]