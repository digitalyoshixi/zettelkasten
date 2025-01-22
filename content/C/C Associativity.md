---
banner: 
tags:
  - c
---
The rules for how multiple of the same operation per expression is handled.

| Name       | Operators         | Associates |
| ---------- | ----------------- | ---------- |
| Equality   | `==` `!=`         | Left       |
| Comparison | `>` `>=` `<` `<=` | Left       |
| Term       | `-` `+`           | Left       |
| Factor     | `/` `*`           | Left       |
| Unary      | `!` `-`           | Right      |
