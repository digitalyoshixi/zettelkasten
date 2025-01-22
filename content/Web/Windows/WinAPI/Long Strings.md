---
tags:
  - win32api
---
Windows uses [[Unicode]].
To have a Unicode string, you must preface the string with `L`
```cpp
wchar_t uni_string = L"Hello";
```
Many default C functions do not work with wide strings, so they remade most of the basic C functions.
- [[strlen]] turns into [[wcslen]]
- [[printf()]] turns into [[wprintf]]