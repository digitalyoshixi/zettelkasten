---
tags:
  - c
---
Local variables are those are declared within functions.

```c
void f() {
    int i;
    i = 1; // OK: in scope
}
```

They will be freed once the program exists the scope