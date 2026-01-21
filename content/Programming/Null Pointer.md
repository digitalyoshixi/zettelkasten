---
tags:
  - c
aliases:
  - nullptr
---
If you are initializing a pointer with no exact address, it is best practice to assign the pointer to be a null pointer.

If you do not, the pointer will grab garbage addresses. [[Stack Overflow]] vuln
![[Null Pointer-20240201025235210.webp]]

# Null PTR
```c
int *ptr = 0; // make a null pointer
printf("%d", ptr); // will always be 0
```
`0`
The value of a null pointer is always 0.
