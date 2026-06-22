---
tags:
  - security
aliases:
  - DBI
---
A method for [[Software Instrumentation]] that adds hooks at run-time.
DBI tools expost an API to write user defined DBI tooling.
# Architecture
![[Dynamic Instrumentation-20260622222203195.webp]]
1. Fetch code from the process, instrument it, compile with [[Just-in-time Compilation|JIT]], write into code cache
2. Code in code cache is executed until there is a control flow that requires fetching new code
