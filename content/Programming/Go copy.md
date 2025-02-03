---
tags:
  - go
  - programming
---
A memory efficient way to copy variables.
`copy(dest,src)`
```go
numbers := []int{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}  
  
// Create copy with only needed numbers  
neededNumbers := numbers[:len(numbers)-10]  
numbersCopy := make([]int, len(neededNumbers))  
copy(numbersCopy, neededNumbers)
```