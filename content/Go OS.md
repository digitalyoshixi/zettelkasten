---
tags:
  - programming
  - go
---
A library used for accessing operating system
```go
import (
	"os"
)
file, err := os.Open("file.go") // For read access.
if err != nil {
	log.Fatal(err)
}
```
# Guides
- [[Go Read File]]