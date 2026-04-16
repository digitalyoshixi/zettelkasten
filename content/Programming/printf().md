---
tags:
  - c
  - cpp
---
General-purpose format conversion function that will output the given arguments with a given format to [[Standard Output|stdout]].
Is not [[C Async Safe]]
```c
> printf("%d %4 haha", 7,2314);
7 2314 haha
```
### % formats
| symbol | meaning                                                                         |
| ------ | ------------------------------------------------------------------------------- |
| %d     | decimal integer                                                                 |
| %f     | float                                                                           |
| %1-9   | a character of length (1-9). example is printf("%5f", 23143);                   |
| $.1-9  | requests (1-9) digits after the decimal place. example is printf("%1.2f",6.23); |
| %o     | octal integer                                                                   |
| %x     | hex int                                                                         |
| %c     | character                                                                       |
| %s     | string                                                                          |
| %%     | just for % itself                                                               |