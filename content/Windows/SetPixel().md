---
tags:
  - win32api
---
Changes a single pixel on the [[Handle Device Context]] to be a given color.
`COLORREF SetPixel(HDC hdc, int x, int y, COLORREF crColor);`

# Example
This is a program that draws random red dots on the screen
```cpp
PAINTSTRUCT ps;
RECT r;

GetClientRect(hwnd, &r);
if (r.bottom == 0) {    
    return;
}
HDC hdc = BeginPaint(hwnd, &ps);

for (int i=0; i<1000; i++) {
	int x = rand() % r.right;
    int y = rand() % r.bottom;
    SetPixel(hdc, x, y, RGB(255, 0, 0));
}
EndPaint(hwnd, &ps);
}
```