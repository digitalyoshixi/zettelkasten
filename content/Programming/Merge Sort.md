---
tags:
  - programming
  - algorithm
---
Recursively dividing an array into smaller sub-arrays, then merging them back together to get a fully sorted array.
Is $O(n\log_{2}(n))$ time
# Merging Algorithm
![[Merge Sort-20250317164509910.webp]]
1. Split up the list into sub-arrays of 1
2. Check which sub-list is smaller than the other, and merge in proper order
# Pseudocode
![[Merge Sort-20250317204934325.webp]]
# C++ Implementation
```cpp
#include <vector>
using namespace std;
vector<int> merge(vector<int> l, vector<int> r){
    vector<int> retlist;
    int lptr = 0;
    int rptr = 0;
    while (lptr < l.size() && rptr < r.size()){
        if (l[lptr] < r[rptr])retlist.push_back(l[lptr++]);
        else retlist.push_back(r[rptr++]);
    }
    while (lptr < l.size()){
        retlist.push_back(l[lptr++]);
    }
    while (rptr < r.size()){
        retlist.push_back(r[rptr++]);
    }
    return retlist;
}

vector<int> mergesort(vector<int> a){
    if (a.size() <= 1) return a;
    int mid = a.size()/2;
    vector<int> left;
    vector<int> right;
    for (int i = 0; i < a.size(); i++){
        if (i < mid) left.push_back(a[i]);
        else right.push_back(a[i]);
    }
    left = mergesort(left);
    right = mergesort(right);
    return merge(left, right);
}
```
# C Implementation
```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_LEN = 1024

void print_list(int* list, int len){
  for (int i = 0; i < len; i++){
    printf("%d, ", list[i]);
  }
}

int* merge(int* list1, int* list2, int len1, int len2){
  // create a new max list size with len1+len2
  //printf("list1: ");
  //print_list(list1, len1);
  //printf("list2: ");
  //print_list(list2, len2);
  int* ret_list = (int*)calloc(len1+len2, sizeof(int));
  int ptr1 = 0;
  int ptr2 = 0;
  int ptr_list = 0;
  while (ptr1 < len1 && ptr2 < len2){
    if (list1[ptr1] < list2[ptr2]){
      ret_list[ptr_list] = list1[ptr1];
      ptr1++;
    }
    else{
      ret_list[ptr_list] = list2[ptr2];
      ptr2++;
    }
    ptr_list++;
  }
  // dump last things 
  if (ptr1 < len1){
    for (int i = ptr1; i < len1; i++){
      ret_list[ptr_list] = list1[i];
      ptr_list++;
    }
  }
  else if (ptr2 < len2){
    for (int i = ptr2; i < len2; i++){
      ret_list[ptr_list] = list2[i];
      ptr_list++;
    }
  }
  //printf("ret_list:");
  //print_list(ret_list, len1+len2);
  return ret_list;
}

int* merge_sort(int* arr, int len){
  if (len == 1){
    return arr;
  }
  return merge(merge_sort(arr, len/2), merge_sort(arr+len/2, len-len/2), len/2, len-len/2);
}

int main(){
  int mylist[10] = {2, 5, 2 ,6, 7, 1, 4, 10, 9, 3};
  int* newlist = merge_sort(mylist, 10);
  print_list(newlist, 10);
  return 0;
}
```