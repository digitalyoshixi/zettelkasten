---
tags:
  - c
  - programming
---
Coverts a string to a [[C Datatypes|Long Integer]].
```c
long int strtol(const char *str, char **endptr, int base)
```
- `str` is the string to be converted to an integer
- `endptr` is a character pointer used to store the pointer to the first character after the numeric value
- `base` the number base to convert to/from
# Example
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
  char *endptr;
  int num = strtol("55", &endptr, 10); 
  printf("%d\n",num); // 55
  printf("%d\n", *endptr); // 0, since there is no letter after the number
  int num2 = strtol("1109a", &endptr, 10); 
  printf("%d\n", num2); // 1109
  printf("%d\n", *endptr); // 97. this is the ascii representation of 'a'

  return 0;
}

```