---
tags:
  - windows
  - win32api
---
https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createwindowa
Creating a new window.
```cpp
HWND window = CreateWindow("Window name", "My First Game", WS_OVERLAPPEDWINDOW | WS_VISIBLE, CW_USEDEFAULT, CW_USEDEFAULT, 1280, 720, 0, 0, hInstance,0);
```
# Getting Handle
```cpp
HDC hdc = GetDC(window);
```
