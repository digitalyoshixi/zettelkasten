---
tags:
  - programming
aliases:
  - BNF
---
A [[Programming/Grammar|Grammar]] used to describe the syntax of programming languages.
It provides a structure to define how symbols can be combined to form valid strings in a langauge. Developed for [[FORTRAN]]
# Concepts
- [[Terminal]]
- [[Non-terminal]]
- [[Production]]
# BNF Rules
- Terminals are simply written out. `while`
- Non-terminals are enclosed in angle brackets: `<statement>`
- Productions are in the form: `<nonterminal> ::= <sequence of terminals or nonterminals>`
- We can use `|` to represent or
# Examples
```bnf
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<integer> ::= <digit> |  <digit><integer>
<floating point> ::= <integer>.<integer>
```