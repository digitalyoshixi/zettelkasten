---
tags:
  - c
---
turns an ascii representation of a number into an integer.
for example: `"992310"` -> `992310`
```c
#include <stdio.h>

int atoi(char s[]){
    int i,n;
    n=0;
    for (i=0; s[i] >= '0' && s[i] <= '9'; i++){
        n = 10 * n + s[i] - '0';
    }
    return (n);
}


int main(){
    char strig[] = {'9','2','0','6','5','1','\0'};
    printf("%d", atoi(strig));
    return 0;
}
```
