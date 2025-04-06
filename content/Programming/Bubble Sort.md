---
tags:
  - programming
---
Floats numbers to the top to order them from least to greatest
Compares 2 numbers. swap if you need to.
![[Pasted image 20231122135438.png]]
Eventually, the biggest number will bubble to the rightmost side.
# C Implementation
```c
void bubble_sort(int *arr, int size){
  int done = 0;
  while (done == 0){
    done = 1;
    for (int i = 0; i < size-1; i++){
      if (arr[i] > arr[i+1]){
        done = 0;
        int b = arr[i+1];
        arr[i+1] = arr[i];
        arr[i] = b;
      }
    }
  }
}
```
