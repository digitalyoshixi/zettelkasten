---
tags:
  - c
---
https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/security-init-cookie?view=msvc-170

You can just skip this one.

It is used to protect against buffer overruns it generates a cookie every stack change, checks if its the same as the initialized cookie. 
If its not, then it terminates the program.

Again, just security.