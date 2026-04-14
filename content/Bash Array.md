---
tags:
  - programming
  - bash
---
```bash
$ my_array=(apple banana orange)
# print indexes
$ echo ${my_array[0]}
apple
$ echo ${my_array[2]}
orange
# print all elements
$ echo "all elements: ${my_array[@]}"
apple banana orange
# print length
$ echo "length: ${#my_array[@]}"
3
# add a new element
my_array[3]=carrot
```
