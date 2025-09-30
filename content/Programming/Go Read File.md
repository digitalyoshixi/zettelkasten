---
tags:
  - programming
  - go
aliases:
  - Go Open File
---
```go
package main
import (
	"fmt"
	"os"
)

func main(){
	file, err := os.Open("file.go") // For read access.
	data := make([]byte, 100) // read 100 bytes
	count, err := file.Read(data)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("read %d bytes: %q\n", count, data[:count])
}

```