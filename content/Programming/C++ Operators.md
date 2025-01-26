---
tags:
  - cpp
---
operators require:
1. an operation
2. two operators(called operands)
operators are [[Lamba Functions]] which return(or not) a value depending on the operator used.
operators can have more than one meaning. eg, the `-` operator can be used to negate or subtract
# Operators
| operator | effect |
| ---- | ---- |
| + | returns sum of operand1 + operand2` |
| - | returns result of operand1 - operand2 or can be used to negate a number |
| * | returns product of operand1 * operand2 |
| / | returns division of operand1 / operand2 |
| == | returns boolean if operand1 equals operand2 |
| ?: | c ? a : b. if c is true, evaluate x, if c is false, evaluate y |
### C++ Exclusive
[[Extraction Operator]]
[[Insertation Operator]]
### Keyword Operators
| operator | effect |
| -------- | ------ |
| new      |      |
| delete   | does not return.       |
| throw    | does not return. throws an [[Exception]]       |

# Unary vs Binary
### Unary
Operators act on one operand. take for example `-a`. only one operand
### Binary
Operators act on two operand. `3+4` is one, `2-2` is one [[Insertation Operator]] and [[Extraction Operator]] are also binary
### Ternary
acts on 3 operands. the only one is the [[Conditional Operator]]
### Nullary
acts on 0 operands. the only one is throw
