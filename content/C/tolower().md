---
tags:
  - c
  - strings
---
turns a given char[] representation of a string into the lowercase version of itself.
e.g. `AYsndaU` -> `aysndau`

```c
#include <stdio.h>

char lower(char c){
    if (c >= 'A' && c <= 'Z'){
        return (c + 'a' - 'A');
    }
    else return c;

}

int main(){
    char thechar;

    for (thechar = 'A' ; thechar <= 'Z' ; thechar++){
		printf( "%c", lower(thechar));
    }   
    return 0;
}
```