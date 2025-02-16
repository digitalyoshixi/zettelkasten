---
tags:
  - go
  - javascript
  - programming
  - web
---
```go
import "encodings/json"



func main(){
	data := map[string]interface{}{
		"intValue":    1234,
		"boolValue":   true,
		"stringValue": "hello!",
		"objectValue": map[string]interface{}{
			"arrayValue": []int{1, 2, 3, 4},
		},
	}
	jsonData, err := json.Marshal(data)
}
```
