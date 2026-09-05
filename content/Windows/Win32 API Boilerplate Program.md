---
tags:
  - win32api
---
```cpp
#include <windows.h>

// get window messages
LRESULT CALLBACK window_callback(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	LRESULT result = 0;
	// message handler
	switch (uMsg) {
	case WM_CLOSE:

	case WM_DESTROY: { // game window closed. exit the game
		
	}break;

	case WM_SIZE: { // window size changed. we need to remake the buffer

	}break;

	default: {
		result = DefWindowProc(hwnd, uMsg, wParam, lParam);
	}
	}

	return result;
}




// --------  MAIN FUNCTION -------
int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {
	// Create Window Class
	WNDCLASS window_class = {};
	window_class.style = CS_HREDRAW | CS_VREDRAW;
	window_class.lpszClassName = "MonkeyWindow";
	window_class.lpfnWndProc = window_callback;
	// Register Class
	RegisterClass(&window_class);
	// Create Window
	HWND window = CreateWindowEx(WS_EX_TOPMOST, window_class.lpszClassName, "", WS_CLIPSIBLINGS | WS_CLIPCHILDREN | WS_POPUPWINDOW | WS_VISIBLE, CW_USEDEFAULT, CW_USEDEFAULT, 300, 300, 0, 0, hInstance, 0);
	// Create image window
	HWND img_window = CreateWindow("Static", NULL, WS_VISIBLE | WS_CHILD | SS_BITMAP | WS_EX_LAYERED, 0, 0, 300, 300, window, 0, 0, 0);

	// loop
	while (true) { 
		

	}
}
```
