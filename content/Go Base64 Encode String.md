---
tags:
  - web
  - programming
  - go
---
```go
package main

import (
	"encoding/base64"
	"fmt"
)

func main() {
	input := "Hello, World!"
	encoded := base64.StdEncoding.EncodeToString([]byte(input))
	fmt.Println(encoded) 
}
```