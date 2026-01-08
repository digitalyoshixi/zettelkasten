---
tags:
  - programming
---
Checks every element in the array. If the element to the left is smaller, then continuously swap until there is nothing smaller.
![[Insertion Sort-20241122211007603.webp]]
# Intuition
You have a left hand and right hand. The left hand will have everything sorted, and the right hand is everything unsorted. Continue to pick from right hand that you insert into the left hand in order.
# Python Implementation
```python
def insertionsort(L) -> None:
	for i in range(len(L))
		value = L[i]
		j = i
		while j != 0 and L[j - a] > value:
			L[j] = L[j-1]
			j=j-1
		L[j] = value
```
# C Implementation
```c 
void insert_sort(int *arr, int size){
  for (int i = 1 ; i < size; i++){
    for (int j = i; j > 0; j--){
      if (arr[j] < arr[j-1]){
        int cpy = arr[j];
        arr[j] = arr[j-1];
        arr[j-1] = cpy;
      }
    }
  }
}
```