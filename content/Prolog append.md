---
tags:
  - programming
  - prolog
---
```c
% append(?X, ?Y, ?Z) iff Z is the result of appending list Y to list Z
append([],Y,Y)
append([H|T],Y,[H|Z]):-append(T,Y,Z)
```
# Examples
- `append([], [1,2,3], Y)` 