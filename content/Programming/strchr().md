---
tags:
  - c
---
`strchr(char s1[], char ch)`
searches the entire string for the first occurrence of given character
If it finds it, it returns a pointer to that character.
```c
char str1[] = "besidfss";
char myfav = 'i';
char *location = strchr(str1, myfav); // this is a mem location
```

[[strstr()]] is the string version of this