---
tags:
  - security
  - web
---
A tool used to automatically [[Fuzzing|Fuzz]] requests with [[Burp Suite]].
# Example Fuzz Template
```
GET /api/v1/books?show=$file$ HTTP/1.1
...
```
- `$file$` will be fuzzed with targets
# Lists
1. Select selection to fuzz
2. Right click > Add payload position 
3. Payload Add from list...
	1. HTTP Verbs
