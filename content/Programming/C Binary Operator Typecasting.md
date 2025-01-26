---
tags:
  - c
---
When an binary operator occurs with 2 datatypes that are not the same.
e.g. `uint * int`
then, the 'lower' datatype is promoted to the 'higher' datatype before the operation proceeds.

- `char` and `short` are converted to `int`
- `float` is converted to `double`
- if any are `double` then `*` is converted to `double`
- if any are `long` then `*` is converted to `long`
- if any are `unsigned` then `*` is converted to `unsigned`
- All float values are converted to `double` **All floating point arithmetic in C is done in double precision**
- otherwise, the operands must be `int` and result is `int`