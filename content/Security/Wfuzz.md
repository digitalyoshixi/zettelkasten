---
tags:
  - redteam
  - web
---
A web [[Fuzzing|Fuzzer]] that can test multiple [[Rest API|HTTP Request]]. 
# Usage
```
wfuzz -w /usr/share/wordlists/mywordlist.txt 'http://127.0.0.1:500/api/v1/books?id=FUZZ'
```
# Flags
```
-hl # hide lines
-hc 404 # hide error code 404s
```