---
tags:
  - c
---
since i++ and ++i both return a value, you can use these return values for your own scenarios.

For example, if you had a loop that iterated through a string, it may look something like:
```c
i[c] = b;
c++;
```
instead, you can shorten it by doing
```c
i[c++] = b;
```
as c++ returns c and then adds to it.