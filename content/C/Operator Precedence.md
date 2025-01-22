---
tags:
  - c
aliases:
  - Expression Precedence
---
`(c=getchar()) != EOF`
is not the same as
`c = getchar() != EOF`
because `getchar () != EOF` would be evaluated first.
It is not left to right, it is precedence based booleans

# Hierarchy
https://en.cppreference.com/w/c/language/operator_precedence
| Precedence | Operator               |
| ---------- | ---------------------- |
| 1          | `++` `--` postfix      |
|            | `()`                   |
|            | `[]`                   |
|            | `.`                    |
|            | `->`                   |
|            | `(_type_){_list_}`     |
| 2          | `++` `--` prefix       |
|            | `+` `-`                |
|            | `!` `~`                |
|            | `(_type_)` typecasting |
|            | `*` dereference        |
|            | `&`                    |
|            | `sizeof`               |
|            | `_Alignof`             |
| 3          | `*` `/` `%`            |
| 4          | `+` `-`                |
| 5          | `<<` `>>`              |
| 6          | `<` `<=`               |
|            | `>` `>=`               |
| 7          | `==` `!=`              |
| 8          | `&`                    |
| 9          | `^`**                  |
| 10         | `\|`                   |
| 11         | `&&`                   |
| 12         | `\|`                   |
| 13         | `?:`                   |
| 14         | `=`                    |
|            | `+=` `-=`              |
|            | `*=` `/=` `%=`         |
|            | `<<=` `>>=`            |
|            | `&=` `^=` `\|=`        |
| 15         | `,`                    |


