---
tags:
  - haskell
  - programming
aliases:
  - Haskell Primative
---
These are types represented as literals on the stack.
# List
| type    | description                                              |
| ------- | -------------------------------------------------------- |
| Char    | Represents [[Unicode]] character                         |
| Bool    | Represents `True` or `False`                             |
| Int     | 32-bit or 64-bit wide signed integer                     |
| Integer | Signed integer of unbounded size                         |
| Double  | Signed floating point of 64-bit size                     |
| Float   | Signed floating poijnt of 32-bit size, slower to haskell |
| Unit    | The only element is () ([[Haskell Unit]])                |
 ```haskell
type Char#
type Bool#
type Int#
type Word#
type Addr#
type Float#
type Double#
type Int64#
type Word64#
```
