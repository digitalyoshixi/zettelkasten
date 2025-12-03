---
tags:
  - programming
  - compilers
---
# Present Terminals
- [[yacc ID]]
- `INT`
- `VAR`
# Grammar Rules
For a grammar like: $\alpha \to \beta_{1} \beta_{2} \dots \beta_{k}$ with:
- $\alpha$ as a non-terminal
- $\beta_{i}$ as a non-terminal or terminal
```
expr := INT
  { $$ = new IntegerLiteral(@1, $1); };
```
- First line is the grammar rule, where we produce an int token
- `$$` is the result of the production rule
- `@1` is the source location of $\beta$
- `$1` is the value of $\beta_{1}$, here `INT`