---
tags:
  - programming
aliases:
  - C memcpy
---
# Boilerplate
```c
int arr1[] = {1, 2, 3, 4, 5};
int n = sizeof(arr1) / sizeof(arr1[0]);
int arr2[n];

// Use memcpy to copy arr1 to arr2
memcpy(arr2, arr1, n * sizeof(arr1[0]));

```