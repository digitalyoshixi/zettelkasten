---
tags:
  - win32api
---
This is equivalent to the main() function of regular C.
```cpp
int
WINAPI
WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR lpCmdLine,
	int nShowCmd
);
```
1. Handle to program executable. [[Instance Handle]]
2. Obsolete feature. Always NULL now.
3. command line arguments
When the program is run, windows automatically passes parameters in so that you have values. 