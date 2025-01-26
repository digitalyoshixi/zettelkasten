---
tags:
  - c
---
`strcmp(str1, str2)`
compares the values of 2 strings.
- returns 0 if str1 = str2
- return <0 if str1\<str2
- returns >0 if str1>str2
# How it works
Its a very simply method actually.
```c
// pseudocode
char str1[];
char str2[];
int i = 0;

while (while str1 not completely equal to str2){
	if (str1[i] < str2[i])
		return str1[i] - str2[i]; // negative return
	else if (str1[i] > str2[i])
		return str1[i] - str2[i]; // positive return
}
return 0; // if they are equivalent
```
It keeps iterating and comparing strings until it finds 2 characters do not match, if they do not match, it returns the difference between the characters.
If they completely match, then it returns 0.