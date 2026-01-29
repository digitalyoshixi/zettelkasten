---
tags:
  - c
  - cpp
aliases:
  - EOF
---
A special character to signify that this is the end of the current input stream.
A file is just another way of saying input stream.
# EOF Value
It is `CTRL+D` in linux systems
it is `CTRL+Z` in windows

EOF is either -1 or 0.
In newer C language, EOF is set as -1.
[[stdio.h]] automatically defines EOF as a [[C Macro]]

https://stackoverflow.com/questions/1782080/what-is-eof-in-the-c-programming-language

# EOF Use-case
Input streams may switch. Every input stream is prefaced with a CTRL+D character to signify the input stream has switched.

You may want to check for these if you want to check for input stream switches.
