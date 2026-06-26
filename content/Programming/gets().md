---
tags:
  - pwn
  - binary_exploitation
---
A function that will get a string from standard input into a buffer, doesn't check size of input string.
```c
gets(buff)
```
- [[fgets()]] is the safe replacement of this.
