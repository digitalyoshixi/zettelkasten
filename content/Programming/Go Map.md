---
tags:
  - go
  - programming
---
A key-value [[Hash Map]].
- Map is unordered
- Map does not allow duplicates
- Empty maps have value `nil`
# Creating Map
```go
// first way with var
var a = map[KeyType]ValueType{key1:value1, key2:value2,...}  
// second way with walrus
b := map[KeyType]ValueType{key1:value1, key2:value2,...}
// empty map
var a map[KeyType]ValueType
fmt.Print(a == nil) // True
```
# Accessing Maps
```go
value = map_name[key]
// modifying values
map_name[key] = "something"
```
# Deleting Key-Value Pairs
```go
delete(map_name, key)
```
# Checking for Key Existence
```go
value, ok := map_name[key]
```