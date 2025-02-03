---
tags:
  - go
  - programming
---
[[Go Arrays]] that can have dynamic size.
```go
slice_name := []datatype{values}

// examples
myslice := []int{}
myslice2 := []int{1,2,3}

// indexing
fmt.Print(myslice2[0])
// modifying value
myslice2[0] = 20

// appending multiple elements
myslice2 = append(myslice2, 20, 21)
// appending slices
myslice3 = append(myslice1, myslice2)
```
# Slicing an Array
You can slice an array
```go
var myarray = [length]datatype{values} // An array  
myslice := myarray[start:end] // A slice made from the array
```
![[Go Slices-20250203014942957.webp]]