---
tags:
  - win32api
aliases:
  - GDI
---
Component of [[IT/Windows]] to create [[Raster]] images like:
- [[Bitmap File]]
- PNG
- Fonts
- Vector graphics
For printing, it will convert all it sees as input including fonts into [[Bitmap File]] images before sending it to the printer.

In Win32 API, it can be used to draw images to the screen.
https://zetcode.com/gui/winapi/gdi/
# Graphics Process
1. Create a painstruct
	`PAINTSTRUCT ps;`
2. Obtain a [[Handle Device Context|HDC]] using BeginPaint
	`HDC hdc = BeginPaint(hWnd, &ps);`
	This prepares a window and a paintstruct for painting
3. You can either:
	1. Draw pixels with [[SetPixel()]]
	2. Draw a bitmap with [[BitBlt()]]
4. Close the [[Handle Device Context|HDC]] with EndPaint
	`BOOL _ = EndPaint(hWnd, &ps);`