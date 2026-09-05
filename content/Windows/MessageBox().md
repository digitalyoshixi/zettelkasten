---
tags:
  - win32api
---
```cpp
int MessageBox(
  [in, optional] HWND    hWnd,
  [in, optional] LPCTSTR lpText,
  [in, optional] LPCTSTR lpCaption,
  [in]           UINT    uType
);
```
An example is:
`MessageBox (NULL, TEXT ("Hello, Windows 98!"), TEXT ("Somewindowname"), 0) ;`
### MB_ Prefixed Constants List
The 4th argument can actually be a combination of MB_ prefixed constants.
```cpp
#define MB_OK 0x00000000L
#define MB_OKCANCEL 0x00000001L
#define MB_ABORTRETRYIGNORE 0x00000002L
#define MB_YESNOCANCEL 0x00000003L
#define MB_YESNO 0x00000004L
#define MB_RETRYCANCEL 0x00000005L
// main button constants. Says which button is main one
#define MB_DEFBUTTON1 0x00000000L
#define MB_DEFBUTTON2 0x00000100L
#define MB_DEFBUTTON3 0x00000200L
#define MB_DEFBUTTON4 0x00000300L
// icon of message box
#define MB_ICONHAND 0x00000010L
#define MB_ICONQUESTION 0x00000020L
#define MB_ICONEXCLAMATION 0x00000030L
#define MB_ICONASTERISK 0x00000040L
#define MB_ICONWARNING MB_ICONEXCLAMATION
#define MB_ICONERROR MB_ICONHAND
#define MB_ICONINFORMATION MB_ICONASTERISK
#define MB_ICONSTOP MB_ICONHAND
```
If my line is: `MessageBox (NULL, TEXT ("Hello, Windows 98!"), TEXT ("Somewindowname"), 0) ;`
the 4th argument is a value of 0, this is equivalent to MB_OK. it will have an OK box. Additionally, since its 0, it will have MB_DEFBUTTON1 meaning the first button is the main button,
![[MessageBox()-20240427220247149.webp]]
If I had 2 buttons like:
`MessageBox (NULL, TEXT ("Hello, Windows 98!"), TEXT ("Somewindowname"), MB_OK | MB_CANCEL) ;`
``
![[MessageBox()-20240427220610178.webp]]
The Ok button would be the main button and have focus since its button 0.
I would also have 2 buttons as I gave it 2 constants
# Return
The message box returns an int type. This int type is the response of the message box (which button they pressed).
`IDOK` is the value 1, which is the value returned when the user pressed on the OK button.
Messagebox can also return:
`IDYES`, `IDNO`, `IDCANCEL`, `IDABORT`, `IDRETRY`, or `IDIGNORE` with each of them having their respective int value representation.