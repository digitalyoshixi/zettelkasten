---
tags:
  - security
---
This is a linux library used for generating [[Digital Certificate]].
But, its pretty bad!
# Create [[Falcon]] key
- `openssl genpkey -algorithm falcon512 -provider oqsprovider -provider-path <path_here> -out falcon512.key` (private key)
- `openssl pkey -in falcon512.key -pubout -out falcon512.pub` (generate public from private)