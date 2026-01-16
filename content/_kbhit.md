---
tags:
  - programming
  - linux
---
A function that returns a non-zero value when a character is waiting in [[Standard Input|stdin]].
Used to test whether a user has pressed a key.
https://www.flipcode.com/archives/_kbhit_for_Linux.shtml
```cpp
#include <ncurses.h>
#include <unistd.h>  /* only for sleep() */

int kbhit(void)
{
    int ch = getch();

    if (ch != ERR) {
        ungetch(ch);
        return 1;
    } else {
        return 0;
    }
}
```