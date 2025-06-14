---
tags:
  - reverse_engineering
  - security
aliases:
  - Reverse Engineering Golang
---
Golang is notoriously hard to reverse engineer. The builtins and mutex systems make compiled binaries large and heavy.
![[Reverse Engineering Golang-20250614174130802.webp]]
![[Reverse Engineering Golang-20250614174148501.webp]]
# Process
1. If your golang binary was stripped, use [[Redress]]
2. [[Delve]] is a debugger that works well with goroutines
# Concepts
- [[Golang Main Function]]
- [[Golang Function Call Procedure]]
- [[Golang Stack Reuse]]
- [[Reverse Engineering Golang Goroutine]]