---
tags:
  - programming
aliases:
  - DBC
---
[[ASCII]] cannot display eastern languages like Chinese.
So, they made 2 bytes to display characters.
# Problem
- You cannot accurately determine string length if you do not parse through the string.
- You cannot do pointer arithmetic to go back or forth 1 character. You must parse the string

[[Unicode]] fixes these issues