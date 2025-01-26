---
tags:
  - c
---
yes, array inside array

```c
int rawdata[2][3] = {
	{3,2,1},
	{6,0,6}
}

 for (int i = 0; i<2; i++){
        for (int v = 0; v<3; v++){
            printf("%d\n", rawdata[i][v]);
        }
}
```
