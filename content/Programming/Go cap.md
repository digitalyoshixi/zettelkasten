---
tags:
  - go
  - programming
---
The total size allocated for a go variable.
Different from [[Go len]], good for checking actual size of [[Go Slices]].
```go
myslice2 := []string{"Go", "GOING", "LANG"}
fmt.Println(cap(myslice2))
```