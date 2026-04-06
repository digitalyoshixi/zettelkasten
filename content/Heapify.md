---
tags:
  - programming
---
A [[Heap]] operation that will bubble-down the top-most element as much as needed to maintain the heap property.
Has a time complexity of $O(\log n)$
![[Heapify-20260406204247608.webp]]
# Algorithm ([[Max-Heap]])
```cpp
#include <iostream>
#include<vector>
using namespace std;

// To heapify a subtree rooted with node i
void heapify(vector<int>& arr, int n, int i){
    // Initialize largest as root
    int largest = i;
    // left index = 2*i + 1
    int l = 2 * i + 1;
    // right index = 2*i + 2
    int r = 2 * i + 2;
    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;
    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;
    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}
```