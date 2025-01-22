---
tags:
  - c
---
Global variables are variables declared at the start of the source file.
```c
int i;
void f() {
    i = 1; // OK: in scope
}
void g() {
    i = 2; // OK: still in scope
}
```
They will just die when the program terminates.