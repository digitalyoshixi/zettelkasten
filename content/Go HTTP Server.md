---
tags:
  - go
  - programming
---
```go
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"encoding/json"
)

// root endpoint
func getRoot(w http.ResponseWriter, r *http.Request) {
	fmt.Printf("got / request\n")
	io.WriteString(w, "This is my website!\n")
}

func getUrlAPI(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	switch r.Method {
		case "POST":
			fmt.Println("POST request received")
			decoder := json.NewDecoder(r.Body)
			var data map[string]interface{}
			err := decoder.Decode(&data)
			if err != nil {
				log.Fatal(err)
			}
			url := data["url"].(string)
			fmt.Println("URL: ", url)
			resp := "hello" + url
			io.WriteString(w, resp)
		default:
			io.WriteString(w, "Only POST method is allowed")
	}
}

func main() {
	http.HandleFunc("/", getRoot)
	http.HandleFunc("/geturl", getUrlAPI)

	// Add error handling for ListenAndServe
	if err := http.ListenAndServe(":3333", nil); err != nil {
		log.Fatal(err)
	}
}

```